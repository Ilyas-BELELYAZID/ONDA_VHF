import sys
import asyncio
import datetime
from PySide6.QtCore import QThread, Signal, QObject, Slot, QCoreApplication, QTimer

from services.modbus_service import ModbusService
from models.dashboard_model import DashboardModel

class DashboardController(QThread):
    update = Signal(object)      # émet un dict summary au UI
    started_signal = Signal()
    stopped_signal = Signal()

    def __init__(self, device_id=1, poll_interval=5, parent=None):
        super().__init__(parent)
        self.modbus = ModbusService(device_id=device_id)
        self.model = DashboardModel()
        self.poll_interval = poll_interval
        self._running = False
        self._loop = None

    def run(self):
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._running = True
        self.started_signal.emit()
        try:
            self._loop.run_until_complete(self._async_start())
        except Exception as e:
            print(f"ERREUR DANS DashboardController.run: {e}")
        finally:
            try:
                if not self._loop.is_closed():
                    print("Nettoyage de la boucle asyncio...")
                    tasks = asyncio.all_tasks(self._loop)
                    for task in tasks:
                        task.cancel()
                    group = asyncio.gather(*tasks, return_exceptions=True)
                    self._loop.run_until_complete(group)
                    self._loop.run_until_complete(self.modbus.close())
            except Exception as e:
                print(f"Erreur lors du nettoyage: {e}")
            finally:
                self._loop.close()
                print("Boucle fermée.")
                self.stopped_signal.emit()

    async def _async_start(self):
        connected = await self.modbus.connect()
        if not connected:
            print("AVERTISSEMENT: La connexion Modbus a échoué")
            
        while self._running:
            print("\n--- Début du cycle de lecture ---")
            try:
                summary = {"timestamp": datetime.datetime.now(), "devices": []}
                devices_id = 1
                
                regs = await self.modbus.read_holding(0, 6)
                if regs is None:
                    device_data = {"id": devices_id, "online": False}
                else:
                    device_data = {
                        "id": devices_id,
                        "online": True,
                        "frequency_mhz": regs[0] / 100.0,
                        "power_pct": regs[1] / 10.0,
                        "temperature_c": regs[2] / 10.0,
                    }
                summary["devices"].append(device_data)

                # --- CORRECTION APPLIQUÉE ICI ---
                # On utilise asyncio.to_thread pour les appels synchrones (bloquants)
                # afin de ne pas geler la boucle événementielle asyncio.
                # `asyncio.run()` ne peut pas être utilisé ici car une boucle est déjà en cours.
                summary["equipment_count"] = await asyncio.to_thread(self.model.get_equipment_count)
                summary["recent_alerts"] = await asyncio.to_thread(self.model.get_recent_alerts, 6)
                summary["system_state"] = await asyncio.to_thread(self.model.get_current_system_state)
                summary["last_update"] = await asyncio.to_thread(self.model.get_last_update_time)

                self.update.emit(summary)

            except Exception as e:
                print(f"ERREUR dans la boucle _async_start: {e}")
            
            print("--- Fin du cycle, en attente... ---")
            await asyncio.sleep(self.poll_interval)

    def stop(self):
        print("Signal d'arrêt reçu par le contrôleur...")
        self._running = False
        if self._loop and self._loop.is_running():
            self._loop.call_soon_threadsafe(self._loop.stop)


# =============================================================================
# 3. SCRIPT DE TEST
# =============================================================================

class ConsoleTester(QObject):
    @Slot(object)
    def on_update_received(self, summary):
        print("\n" + "="*25 + " MISE À JOUR REÇUE " + "="*25)
        print(f"Horodatage: {summary['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 68)
        for device in summary['devices']:
            if device['online']:
                print(f"  Appareil {device['id']}: EN LIGNE")
                print(f"    Fréquence  : {device['frequency_mhz']:.2f} MHz")
                print(f"    Puissance  : {device['power_pct']:.1f} %")
                print(f"    Température: {device['temperature_c']:.1f} °C")
            else:
                print(f"  Appareil {device['id']}: HORS LIGNE")
        print("-" * 68)
        print(f"Aperçu du système:")
        print(f"  Nombre d'équipements: {summary.get('equipment_count', 'N/A')}")
        print(f"  État du système     : {summary.get('system_state', 'N/A')}")
        print(f"  Dernière alerte     : {summary.get('recent_alerts', [('N/A',)])[0]}")
        print("=" * 68 + "\n")

    @Slot()
    def on_controller_started(self):
        print("\n\033[92m[TESTEUR] Le thread du contrôleur a démarré.\033[0m")

    @Slot()
    def on_controller_stopped(self):
        print("\n\033[91m[TESTEUR] Le thread du contrôleur s'est arrêté. Fermeture de l'application.\033[0m")
        QCoreApplication.quit()


if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    
    print("Initialisation du test du DashboardController...")
    
    # Instance du contrôleur avec un intervalle de 3 secondes
    controller = DashboardController(poll_interval=10)
    
    # Instance de notre classe de test qui reçoit les signaux
    tester = ConsoleTester()
    
    # Connexion des signaux du contrôleur aux slots du testeur
    controller.update.connect(tester.on_update_received)
    controller.started_signal.connect(tester.on_controller_started)
    controller.stopped_signal.connect(tester.on_controller_stopped)
    
    # Démarrage du thread du contrôleur
    controller.start()
    
    # On arrête le contrôleur après 15 secondes pour le test
    TEST_DURATION_SECONDS = 15
    print(f"Le test s'exécutera pendant {TEST_DURATION_SECONDS} secondes...")
    QTimer.singleShot(TEST_DURATION_SECONDS * 1000, controller.stop)
    
    sys.exit(app.exec())