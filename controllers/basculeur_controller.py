import asyncio
import datetime
import threading
from typing import Optional

# from services.modbus_service import ModbusService
from services.mock_service_basculeur import MockModbusService
from models.basculeur_model import BasculeurModel
from models.alerte_model import AlerteModel
from models.historique_model import HistoriqueModel
from services.alert_sound import AlertSoundManager

class BasculeurController:
    """
    Poll Modbus regs for basculeur and provide actions:
    - manual_switch(target: 'PRINCIPAL'|'SECOURS')
    - set_auto(enable: bool)
    - get_history()

    Mapping Modbus attendu (holding registers, base offset configurable dans ModbusService):
      regs[0] = active_code       (0 => PRINCIPAL, 1 => SECOURS)
      regs[1] = auto_enabled      (0/1)
      regs[2] = cause_code        (0=Manuel,1=Automatique,2=Défaillance,3=Commande Externe)
    """
    def __init__(self, device_id: int = 3, poll_interval: float = 3.0):
        self.modbus = MockModbusService(device_id=device_id)
        self.model = BasculeurModel()
        self.alert_model = AlerteModel()
        self.histo = HistoriqueModel()
        self.sound = AlertSoundManager()
        self.poll_interval = poll_interval
        self._running = False
        self._thread = None
        self._stop = threading.Event()
        self.data_callback: Optional[Callable[[dict], None]] = None

        # stocker l’état précédent pour détecter les transitions
        self._last_path: Optional[str] = None
        self._last_cause_code: Optional[str] = None

        # mapping codes (consistent with spec) -> texte
        self.cause_map = {
            0: "Manuel",
            1: "Automatique",
            2: "Défaillance",
            3: "Commande Externe",
        }


    # start the asyncio loop in thread
    def start(self):
        if self._thread and self._thread.is_alive():
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def _run_loop(self, id_basculeur = 1):
        self._running = asyncio.new_event_loop()
        asyncio.set_event_loop(self._running)
        # schedule the main polling coroutine
        self._running.create_task(self._polling_task(id_basculeur))
        try:
            self._running.run_forever()
        finally:
            self._running.close()

    async def _polling_task(self, id_basculeur = 1):
        # connect client once if possible
        await asyncio.to_thread(self.modbus.connect)
        while not self._stop.is_set():
            try:
                # lecture registres base 0 (3 regs)
                regs = await self.modbus.read_holding(0, 3)
                if regs is None:
                    return None
                try:
                    active_code = int(regs[0]) # 0 principal, 1 secours
                    auto_enabled = bool(int(regs[1]))
                    cause_code = int(regs[2])
                    # if ts_raw is minutes since epoch or timestamp, adapt — here treat as unix ts if > 100000
                    # fallback - consider 0 or small value => now
                    last_switch = datetime.datetime.now()
                    active_path = "PRINCIPAL" if active_code == 0 else "SECOURS"
                    cause_str = self.cause_map.get(cause_code, f"CODE_{cause_code}")

                    data = {
                        "active_path": active_path,
                        "auto_enabled": auto_enabled,
                        "cause_code": cause_code,
                        "cause_basculement": cause_str,
                        "last_switch": last_switch
                    }
                except Exception as e:
                    print("Decode basculeur regs error:", e)
                    return None

                # Persistance basculeur (synchrones -> exécuter dans thread)
                await asyncio.to_thread(self.model.save_basculeur, data, id_basculeur)

                # evaluate tolerances (synchronously here)
                alert_data = await self._evaluate_alerts(data, id_basculeur, self._last_path)
                data["alert_data"] = alert_data

                # Mémorise état précédent
                self._last_path = data["active_path"]
                self._last_cause_code = data["cause_code"]

                # emit callback to UI (non-blocking)
                if self.data_callback:
                    try:
                        # call in main thread via callback; UI receiver should forward thread-safely
                        self.data_callback(data)
                    except Exception:
                        # in case callback is not thread-safe, ignore here (UI wrapper should handle)
                        pass
                else:
                    # no regs -> offline; you may notify UI via callback with None or offline flag
                    pass
            except Exception as e:
                print("Polling exception:", e)
            # wait poll_interval seconds
            await asyncio.sleep(self.poll_interval)

    def stop(self):
        # stop loop
        self._stop.set()
        if self._running:
            self._running.call_soon_threadsafe(self._running.stop)
        # close modbus
        try:
            self.modbus.close()
        except Exception:
            pass
        if self._thread:
            self._thread.join(timeout=2)

    async def _evaluate_alerts(self, data: dict, equipment_id: int = 1, prev_state: Optional[str] = None):
        """
        Détecte conditions et sauvegarde alertes/historique en incluant la cause_basculement.
        Toutes les opérations BD/IO synchrones sont faites via asyncio.to_thread.
        """
        active_path = data.get("active_path", "PRINCIPAL")
        auto_enabled = data.get("auto_enabled", False)
        cause_code = data.get("cause_code", None)
        cause_label = data.get("cause_basculement", None)
        now = datetime.datetime.now()

        # --- Cas critique : défaillance du canal principal détectée ---
        # Condition : on est sur SECOURS et auto_enabled==True et (prev_state != SECOURS OR cause_code==2)
        if active_path == "SECOURS" and auto_enabled:
            # si on vient juste de basculer ou la cause indique une défaillance, CRITICAL
            is_new_transition = (prev_state != "SECOURS")
            if is_new_transition or cause_code == 2:
                # jouer son critique
                self.sound.play("CRITICAL")
                # enregistrer alerte (incluant la cause)
                await asyncio.to_thread(self.alert_model.save, "BASCULEUR", equipment_id, "Défaillance canal principal", "CRITICAL", now)
                data = {
                    "event_type": "Défaillance",
                    "description": f"Basculement vers secours (cause: {cause_label})",
                    "equipment_type": "BASCULEUR"
                }
                # historique
                await asyncio.to_thread(self.histo.save_event, data)
                return ("CRITICAL", "Défaillance canal principal", "Une défaillance a été détectée sur le canal principal. Le basculement automatique est recommandé.")

        # --- Basculement non prévu (warning) ---
        if active_path == "SECOURS" and not auto_enabled:
            # warning; ce basculement s'est produit alors que le mode auto est désactivé
            self.sound.play("WARNING")
            await asyncio.to_thread(self.alert_model.save, "BASCULEUR", equipment_id, "Basculement non prévu", "WARNING", now)
            data = {
                "event_type": "Anomalie",
                "description": f"Basculement inattendu sans auto activé (cause: {cause_label})",
                "equipment_type": "BASCULEUR"
            }
            await asyncio.to_thread(self.histo.save_event, data)
            return ("WARNING", "Basculement non prévu", "Un basculement inattendu s'est produit. Veuillez vérifier les journaux pour plus de détails.")

        # S'il n'y a aucune alerte, retourner un état normal
        return ("INFO", "État de fonctionnement normal", "Aucun message")

        # --- Mode automatique désactivé (info) ---
        if not auto_enabled:
            # info: signaler la configuration (peut être résolu)
            self.sound.play("INFO")
            await asyncio.to_thread(self.alert_model.save, "BASCULEUR", equipment_id, "Mode automatique désactivé", "INFO", now, True)

        # --- Retour sur canal principal : signaler dans l'historique ---
        if active_path == "PRINCIPAL" and prev_state == "SECOURS":
            self.sound.play("INFO")
            data = {
                "event_type": "Retour service",
                "description": f"Retour sur canal principal",
                "equipment_type": "BASCULEUR"
            }
            await asyncio.to_thread(self.histo.save_event, data)

    # actions callable from UI
    def manual_switch_async(self, target: str):
        """
        target: 'PRINCIPAL' or 'SECOURS'
        Writes register 0 to 0 or 1 and sets cause=0 (manuel)
        """
        code = 0 if target.upper().startswith("P") else 1
        cause_code = 0
        ok1 = self.modbus.write_register(0, int(code))
        ok2 = self.modbus.write_register(2, int(cause_code))  # cause = manuel
        if ok1 and ok2:
            # log history
            data = {
                "event_type": "Basculement manuel",
                "description": f"Basculement manuel vers {target}",
                "equipment_type": "BASCULEUR"
            }
            self.histo.save_event(data)
            return True, None
        return False, "Échec écriture Modbus (manual_switch)."

    def set_auto(self, enable: bool):
        val = 1 if enable else 0
        ok = self.modbus.write_register(1, int(val))
        if ok:
            data = {
                "event_type": "Configuration bascule automatique",
                "description": f"Bascule automatique {'activée' if enable else 'désactivée'}",
                "equipment_type": "BASCULEUR"
            }
            self.histo.save_event(data)
            return True, None
        return False, "Échec écriture Modbus (set_auto)."

    def get_history(self, limit=50):
        return self.histo.get_events(None, None, None, None, limit)
