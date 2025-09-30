import asyncio
import datetime
import inspect
from PySide6.QtCore import QThread, Signal
# from services.modbus_service import ModbusService
from services.mock_service_emetteur import MockModbusService
from models.dashboard_model import DashboardModel

class DashboardController(QThread):
    update = Signal(object)    # émet un dict summary au UI
    started_signal = Signal()
    stopped_signal = Signal()

    def __init__(self, device_id=1, poll_interval=3, parent=None):
        super().__init__(parent)
        self.device_id = device_id
        self.modbus = MockModbusService(device_id=device_id)
        self.model = DashboardModel()
        self.poll_interval = poll_interval
        self._running = False
        self._loop = None

    def run(self):
        """Méthode QThread: démarre un event-loop asyncio dans ce thread et exécute la coroutine principale."""
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._running = True
        self.started_signal.emit()
        try:
            self._loop.run_until_complete(self._async_start())
        except Exception as e:
            print("DashboardController.run error:", e)
        finally:
            # cleanup
            if not self._loop.is_closed():
                self._loop.close()
            self.stopped_signal.emit()

    async def _maybe_await(self, x):
        """Si x est awaitable, l'attendre, sinon retourner la valeur directement."""
        import inspect
        if inspect.isawaitable(x):
            return await x
        return x

    async def _async_start(self):
        connected = await self._maybe_await(self.modbus.connect())
        if not connected:
            print("Warning: Modbus connect failed")
        while self._running:
            try:
                summary = {"timestamp": datetime.datetime.now(), "devices": []}

                # read_holding peut être sync ou async selon l'implémentation du mock/service
                regs = await self._maybe_await(self.modbus.read_holding(0, 7))

                # utiliser self.device_id (assure-toi d'avoir self.device_id défini dans __init__)
                if regs is None:
                    device_data = {"id": self.device_id, "online": False}
                else:
                    device_data = {
                        "id": self.device_id,
                        "online": True,
                        "frequency_mhz": regs[0] / 100.0 if len(regs) > 0 else None,
                        "power_pct": regs[1] / 10.0 if len(regs) > 1 else None,
                        "temperature_c": regs[2] / 10.0 if len(regs) > 2 else None,
                    }

                summary["devices"].append(device_data)

                summary["recent_alerts"] = await asyncio.to_thread(self.model.get_recent_alerts, 6)
                summary["system_state"] = await asyncio.to_thread(self.model.get_current_system_state)
                summary["last_update"] = await asyncio.to_thread(self.model.get_last_update_time)

                self.update.emit(summary)

            except Exception as e:
                print("DashboardController loop error:", e)

            await asyncio.sleep(self.poll_interval)

    def stop(self):
        """Arrêter la boucle et quitter le thread proprement."""
        self._running = False
        # si on veut forcer l'arrêt immédiat de l'event-loop,
        # appeler call_soon_threadsafe(loop.stop) depuis le thread appeler.
        if self._loop and self._loop.is_running():
            # planifier l'arrêt depuis l'extérieur du loop
            self._loop.call_soon_threadsafe(self._loop.stop)
