import asyncio
import threading
from datetime import datetime
from typing import Optional, Callable, Dict
# from services.modbus_service import ModbusService
from services.mock_service_emetteur import MockModbusService
from models.emetteur_model import EmetteurModel
from models.alerte_model import AlerteModel
from services.alert_sound import AlertSoundManager

class EmetteurController:
    """
    Async controller:
    - Runs an asyncio loop in a background thread.
    - Uses asyncio.to_thread to call blocking ModbusService methods safely.
    - Emits data via a user-provided callback (data_callback).
    """
    def __init__(self, device_id=1, poll_interval=3):
        self.modbus = MockModbusService(device_id=device_id)
        self.model = EmetteurModel()
        self.alerte_model = AlerteModel()
        self.sound = AlertSoundManager()
        self._loop = None
        self._thread = None
        self.poll_interval = poll_interval
        self._stop_event = threading.Event()
        self.data_callback: Optional[Callable[[dict], None]] = None
        # tolerance config (could come from config.yml)
        self.tolerances = {
            "temp_max": 55.0,
            "power_min": 5.0,
            "power_max": 55.0,
            "tension_min": 21.0,
            "tension_max": 31.0,
        }

        # état de protection pour éviter actions répétées
        self._protection = {
            "reduced_half": False,
            "reduced_11pct": False,
            "cut": False,
            "nominal_power": None, # puissance nominale sauvegardée (W)
        }

        # seuils ROS (configurable)
        self.ros_warning_threshold = 2.0
        self.ros_reduce_half_threshold = 3.0    # si ROS monte au-dessus -> réduire 50%
        self.ros_reduce_11pct_threshold = 6.0   # si ROS monte au-dessus -> réduire à ~11%
        self.ros_infinite_threshold = float("inf")  # détection ROS infini via math.isinf


    # start the asyncio loop in thread
    def start(self):
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def _run_loop(self, id_emetteur = 1):
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        # schedule the main polling coroutine
        self._loop.create_task(self._polling_task(id_emetteur))
        try:
            self._loop.run_forever()
        finally:
            self._loop.close()

    async def _polling_task(self, id_emetteur = 1):
        # connect client once if possible
        await asyncio.to_thread(self.modbus.connect)
        while not self._stop_event.is_set():
            try:
                # read registers using to_thread (blocking call)
                regs = await asyncio.to_thread(self.modbus.read_holding, 0, 7)
                if regs:
                    # expected mapping:
                    # regs[0] = frequency * 100 (e.g. 11870 -> 118.70 MHz)
                    # regs[1] = power W
                    # regs[2] = temperature C
                    # regs[3] = modulation %
                    # regs[4] = tension * 1 (V)
                    # regs[6] = enabled (ON/OFF)
                    data = {
                        "frequency_mhz": regs[0] / 100.0,
                        "power_pct": regs[1] / 10.0,
                        "temperature_c": regs[2] / 10.0,
                        "modulation_rate": regs[3] / 10.0,
                        "tension_alim": regs[4] / 10.0,
                        "ROS": regs[5] / 10.0,
                        "enabled": regs[6]
                    }
                    # persist in DB (run in thread)
                    await asyncio.to_thread(self.model.save_emetteur, data, id_emetteur)

                    # evaluate tolerances (synchronously here)
                    alert_message = await asyncio.to_thread(self._evaluate_alerts, data)
                    data["alert_message"] = alert_message

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
        self._stop_event.set()
        if self._loop:
            self._loop.call_soon_threadsafe(self._loop.stop)
        # close modbus
        try:
            self.modbus.close()
        except Exception:
            pass
        if self._thread:
            self._thread.join(timeout=2)


    def _store_nominal_power(self, current_power):
        if self._protection["nominal_power"] is None and current_power:
            try:
                self._protection["nominal_power"] = float(current_power)
            except Exception:
                self._protection["nominal_power"] = None

    def _apply_power_write(self, power_w, id_equipement=1):
        """Écrit la puissance sur le matériel (register 1 = puissance * 10)."""
        try:
            val = int(round(power_w * 10))
            ok = self.modbus.write_register(1, val)
            if ok:
                # sauvegarde locale / modèle (optionnel)
                try:
                    self.model.save_emetteur({"power_pct": power_w}, id_equipement)
                except Exception:
                    pass
            return bool(ok)
        except Exception:
            return False

    def _cut_emission_hw(self, id_equipement=1):
        """Coupe l'émission (register 6 = enabled flag -> 0)."""
        try:
            ok = self.modbus.write_register(6, 0)
            if ok:
                try:
                    self.model.save_emetteur({"enabled": 0}, id_equipement)
                except Exception:
                    pass
            return bool(ok)
        except Exception:
            return False

    def _restore_nominal_power_and_enable(self, id_equipement=1):
        """Restaure la puissance nominale et réactive si besoin."""
        nominal = self._protection.get("nominal_power")
        restored = False
        if nominal:
            restored = self._apply_power_write(nominal, id_equipement)
        # si on avait coupé l'émission, tenter de réactiver (register 6 -> 1)
        if self._protection.get("cut"):
            try:
                ok2 = self.modbus.write_register(6, 1)
                restored = restored or bool(ok2)
                try:
                    self.model.save_emetteur({"enabled": 1}, id_equipement)
                except Exception:
                    pass
            except Exception:
                pass
        # reset flags si restauration OK
        if restored:
            self._protection["reduced_half"] = False
            self._protection["reduced_11pct"] = False
            self._protection["cut"] = False
        return restored


    def _evaluate_alerts(self, data: dict, id_equipement=1):
        # --- Gestion des alertes ROS (Réflexion d'Onde Stationnaire) ---
        ros = data.get("ROS")
        try:
            import math
            is_inf = ros is not None and (isinstance(ros, float) and math.isinf(ros))
        except Exception:
            is_inf = False

        # store nominal power once for calculs de restauration
        self._store_nominal_power(data.get("power_pct"))

        # 1) ROS infini -> coupure immédiate (CRITICAL maximal)
        if ros is None:
            # pas d'info : on n'agit pas
            pass
        elif is_inf:
            if not self._protection.get("cut"):
                self._cut_emission_hw(id_equipement)
                self._protection["cut"] = True
                self.sound.play("CRITICAL")
                self.alerte_model.save("EMETTEUR", id_equipement, "Coupure Émission : ROS Infini détecté !", "CRITICAL", datetime.now())
                return ("CRITICAL", "Coupure Émission : ROS Infini détecté !")

        else:
            # 2) WARNING visuelle : ROS dépasse seuil d'alerte (ex: > 2.0)
            try:
                ros_val = float(ros)
            except Exception:
                ros_val = None

            if ros_val is not None and ros_val > self.ros_warning_threshold:
                # jouer le son WARNING et sauver en base (alert visuelle)
                self.sound.play("WARNING")
                self.alerte_model.save("EMETTEUR", id_equipement, f"ROS élevé: {ros_val:.2f}", "WARNING", datetime.now())
                # NOTE: on ne return pas tout de suite: on peut aussi enchaîner actions de protection si nécessaire.

            # 3) Protection progressive : réduire la puissance si ROS augmente
            if ros_val is not None and ros_val >= self.ros_reduce_half_threshold and not self._protection.get("reduced_half"):
                # premier palier : réduire à 50%
                nominal = self._protection.get("nominal_power") or data.get("power_pct", 0)
                target = max(1.0, nominal / 2.0)
                ok = self._apply_power_write(target, id_equipement)
                if ok:
                    self._protection["reduced_half"] = True
                    self.sound.play("CRITICAL")
                    self.alerte_model.save("EMETTEUR", id_equipement, f"Réduction automatique puissance -> 50% ({target:.1f} W)", "CRITICAL", datetime.now())
                    return ("CRITICAL", f"Protection: puissance réduite à 50% ({target:.1f} W)")

            if ros_val is not None and ros_val >= self.ros_reduce_11pct_threshold and not self._protection.get("reduced_11pct"):
                # second palier : réduire drastiquement (~11% de nominal)
                nominal = self._protection.get("nominal_power") or data.get("power_pct", 0)
                target = max(1.0, nominal * 0.11)
                ok = self._apply_power_write(target, id_equipement)
                if ok:
                    self._protection["reduced_11pct"] = True
                    self.sound.play("CRITICAL")
                    self.alerte_model.save("EMETTEUR", id_equipement, f"Réduction automatique puissance -> 11% ({target:.1f} W)", "CRITICAL", datetime.now())
                    return ("CRITICAL", f"Protection: puissance réduite (~11%) ({target:.1f} W)")

            # 4) Si le ROS est redescendu sous le seuil d'alerte, restaurer (si des protections avaient été appliquées)
            if ros_val is not None and ros_val < self.ros_warning_threshold:
                if any((self._protection["reduced_half"], self._protection["reduced_11pct"], self._protection["cut"])):
                    restored = self._restore_nominal_power_and_enable(id_equipement)
                    if restored:
                        self.alerte_model.save("EMETTEUR", id_equipement, "Restauration automatique puissance/émission", "INFO", datetime.now(), True)
                        self.sound.play("INFO")
                        # continuer l'évaluation normale après restauration (ne pas return)

        # --- Temperature ---
        if data["temperature_c"] >= self.tolerances["temp_max"]:
            # critical alert
            self.sound.play("CRITICAL")
            self.alerte_model.save("EMETTEUR", id_equipement, "Surchauffe", "CRITICAL", datetime.now())
            print(f"[ALERTE CRITIQUE] Température élevée: {data["temperature_c"]} °C")
            return ("CRITICAL", f"Surchauffe ({data['temperature_c']:.1f}°C)")

        elif data["temperature_c"] >= (self.tolerances["temp_max"] - 10):
            self.sound.play("WARNING")
            self.alerte_model.save("EMETTEUR", id_equipement, "Température proche du seuil", "WARNING", datetime.now())
            print(f"[ALERTE] Température élevée (proche du seuil): {data["temperature_c"]} °C")
            return ("WARNING", f"Température élevée ({data['temperature_c']:.1f}°C)")

        else:
            self.sound.play("INFO")
            self.alerte_model.save("EMETTEUR", id_equipement, "Température Normale", "INFO", datetime.now(), True)
            print(f"[INFO] Température normale: {data["temperature_c"]} °C")

        # --- Puissance ---
        if data["power_pct"] < self.tolerances["power_min"] or data["power_pct"] > self.tolerances["power_max"]:
            self.sound.play("CRITICAL")
            self.alerte_model.save("EMETTEUR", id_equipement, "Puissance hors bornes", "CRITICAL", datetime.now())
            print(f"[ALERTE CRITIQUE] Puissance hors bornes: {data["power_pct"]} W")
            return ("CRITICAL", f"Puissance hors bornes ({data['power_pct']:.1f} W)")

        elif data["power_pct"] <= (self.tolerances["power_max"]) and data["power_pct"] >= (self.tolerances["power_min"]):
            # dans la plage normale
            self.sound.play("INFO")
            self.alerte_model.save("EMETTEUR", id_equipement, "Puissance Normale", "INFO", datetime.now(), True)
            print(f"[INFO] Puissance dans la plage normale: {data["power_pct"]} W")

        # --- Tension ---
        if data["tension_alim"] < self.tolerances["tension_min"]:
            self.sound.play("CRITICAL")
            self.alerte_model.save("EMETTEUR", id_equipement, "Sous-tension", "CRITICAL", datetime.now())
            print(f"[ALERTE CRITIQUE] Tension trop basse: {data['tension_alim']} V")
            return ("CRITICAL", f"Tension trop basse: ({data['tension_alim']} V)")

        elif data["tension_alim"] > self.tolerances["tension_max"]:
            self.sound.play("CRITICAL")
            self.alerte_model.save("EMETTEUR", id_equipement, "Sur-tension", "CRITICAL", datetime.now())
            print(f"[ALERTE CRITIQUE] Tension trop élevée: {data['tension_alim']} V")
            return ("CRITICAL", f"Tension trop élevée: ({data['tension_alim']} V)")

        elif (self.tolerances["tension_min"] <= data["tension_alim"] <= self.tolerances["tension_min"] + 1) or \
             (self.tolerances["tension_max"] - 1 <= data["tension_alim"] <= self.tolerances["tension_max"]):
            self.sound.play("WARNING")
            self.alerte_model.save("EMETTEUR", id_equipement, "Tension Proche Limite", "WARNING", datetime.now())
            print(f"[ALERTE] Tension proche des limites: {data['tension_alim']} V")
            return ("WARNING", f"Tension proche des limites: ({data['tension_alim']} V)")

        else:
            self.sound.play("INFO")
            self.alerte_model.save("EMETTEUR", id_equipement, "Tension Normale", "INFO", datetime.now(), True)
            print(f"[INFO] Tension normale: {data['tension_alim']} V")

        # S'il n'y a aucune alerte, retourner un état normal
        return ("INFO", "État de fonctionnement normal.")

    # sync wrappers to call from UI directly (execute as blocking via modbus write)
    def set_frequency(self, frequency_mhz):
        # validate
        if frequency_mhz < 118.0 or frequency_mhz > 144.0:
            return False, "Fréquence hors plage autorisée."
        return self.modbus.write_register(0, int(frequency_mhz * 100)), None

    def set_power(self, power_pct):
        if power_pct < 5.0 or power_pct > 55.0:
            return False, "Puissance hors plage (5W-55W)."
        return self.modbus.write_register(1, int(power_pct * 10)), None

    def set_tdm(self, tdm):
        if tdm < 0.0 or tdm > 100.0:
            return False, "Taux de modulation hors plage (0%-100%)."
        return self.modbus.write_register(3, int(tdm * 10)), None
        
    def toggle_enabled(self, equipment_id=1):
        # read current from DB then toggle
        row = self.model.get_latest(equipment_id)
        current = True if (row and row.get("enabled", 1)) else False
        return self.modbus.write_register(6, 0 if current else 1), None
