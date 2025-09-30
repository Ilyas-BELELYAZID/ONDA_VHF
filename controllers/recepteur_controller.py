import asyncio
import threading
from datetime import datetime
from typing import Optional, Callable, Dict
# from services.modbus_service import ModbusService
from services.mock_service_recepteur import MockModbusService
from models.recepteur_model import RecepteurModel
from models.alerte_model import AlerteModel
from services.alert_sound import AlertSoundManager

class RecepteurController:
    def __init__(self, device_id=2, poll_interval=3):
        self.modbus = MockModbusService(device_id=device_id)
        self.model = RecepteurModel()
        self.alert_model = AlerteModel()
        self.sound = AlertSoundManager()
        self.poll_interval = poll_interval
        self._running = False
        self._thread = None
        self._stop = threading.Event()
        self.data_callback: Optional[Callable[[dict], None]] = None
        # tolerances / thresholds (configurable)
        self.thresholds = {
            "temp_max": 55.0,
            "tension_min": 21.0,
            "tension_max": 31.0,
            "rssi_weak_dbm": -100,    # example: RSSI <-100 dBm considered weak
            "snr_low_db": 8.0,        # SNR < 8 dB low (interference)
            "squelch_expected_min": 0,
            "squelch_expected_max": 50
        }
    
    # start the asyncio loop in thread
    def start(self):
        if self._thread and self._thread.is_alive():
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def _run_loop(self, id_recepteur = 1):
        self._running = asyncio.new_event_loop()
        asyncio.set_event_loop(self._running)
        # schedule the main polling coroutine
        self._running.create_task(self._polling_task(id_recepteur))
        try:
            self._running.run_forever()
        finally:
            self._running.close()

    async def _polling_task(self, id_recepteur = 1):
        # connect client once if possible
        await asyncio.to_thread(self.modbus.connect)
        while not self._stop.is_set():
            try:
                """
                Read holding registers for receiver.
                Mapping (example):
                regs[0] = frequency * 100  (e.g. 12390 -> 123.90 MHz)
                regs[1] = rssi in dBm as signed int (e.g. 65500 => -36)
                regs[2] = snr*10 (e.g. 152 -> 15.2 dB)
                regs[3] = squelch level (integer)
                regs[4] = temperature C
                regs[5] = tension * 1 (V)
                """
                regs = await self.modbus.read_holding(0, 6)
                if regs is None:
                    return None

                def signed16(v):
                    return v - 65536 if v > 32767 else v

                data = {
                    "frequency_mhz": regs[0] / 100.0,
                    "rssi_dbm": signed16(regs[1]),
                    "snr_db": regs[2] / 10.0,
                    "squelch": regs[3],
                    "temperature_c": regs[4] / 10.0,
                    "tension_alim": regs[5] / 10.0
                }

                # persist in DB (run in thread)
                await asyncio.to_thread(self.model.save_recepteur, data, id_recepteur)
                
                # evaluate tolerances (synchronously here)
                alert_data = await self._evaluate_alerts(data, id_recepteur)
                data["alert_data"] = alert_data
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

    async def _evaluate_alerts(self, data, equipment_id=1):
        # --- Temperature ---
        if data["temperature_c"] >= self.thresholds["temp_max"]:
            # critical alert
            self.sound.play("CRITICAL")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Surchauffe", "CRITICAL", datetime.now())
            print(f"[ALERTE CRITIQUE] Température élevée: {data["temperature_c"]} °C")
            return ("CRITICAL", f"Surchauffe ({data['temperature_c']:.1f}°C)")

        elif data["temperature_c"] >= (self.thresholds["temp_max"] - 10):
            self.sound.play("WARNING")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Température proche du seuil", "WARNING", datetime.now())
            print(f"[ALERTE] Température élevée (proche du seuil): {data["temperature_c"]} °C")
            return ("WARNING", f"Température élevée ({data['temperature_c']:.1f}°C)")

        else:
            self.sound.play("INFO")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Température Normale", "INFO", datetime.now(), True)
            print(f"[INFO] Température normale: {data["temperature_c"]} °C")

        # RSSI weak
        if data["rssi_dbm"] <= self.thresholds["rssi_weak_dbm"]:
            self.sound.play("CRITICAL")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Signal faible", "CRITICAL", datetime.now())
            print("[ALERTE CRITIQUE] Signal faible:", data["rssi_dbm"], "dBm")
            return ("CRITICAL", f"Signal faible: ({data['rssi_dbm']:.1f}dBm)")

        elif data["rssi_dbm"] <= (self.thresholds["rssi_weak_dbm"] + 10):
            self.sound.play("WARNING")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Signal bas", "WARNING", datetime.now())
            print("[ALERTE] Signal bas:", data["rssi_dbm"], "dBm")
            return ("WARNING", f"Signal bas: ({data['rssi_dbm']:.1f}dBm)")

        else:
            self.sound.play("INFO")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Signal normale", "INFO", datetime.now(), True)
            print("[INFO] Signal normale:", data["rssi_dbm"], "dBm")

        # SNR low -> interference
        if data["snr_db"] <= self.thresholds["snr_low_db"]:
            self.sound.play("CRITICAL")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Interférences (SNR bas)", "CRITICAL", datetime.now())
            print("[ALERTE CRITIQUE] SNR bas:", data["snr_db"], "dB")
            return ("CRITICAL", f"SNR bas: ({data['snr_db']:.1f}dB)")

        else:
            self.sound.play("INFO")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "SNR normale", "INFO", datetime.now(), True)
            print("[INFO] SNR normale:", data["snr_db"], "dB")

        # Squelch out of expected range
        if data["squelch"] < self.thresholds["squelch_expected_min"] or data["squelch"] > self.thresholds["squelch_expected_max"]:
            self.sound.play("WARNING")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Squelch hors plage", "WARNING", datetime.now())
            print("[ALERTE] Squelch hors plage:", data["squelch"])
            return ("WARNING", f"Squelch hors plage: {data['squelch']}")

        else:
            self.sound.play("INFO")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Squelch normale", "INFO", datetime.now(), True)
            print("[INFO] Squelch normale:", data["squelch"])

        # --- Tension ---
        if data["tension_alim"] < self.thresholds["tension_min"]:
            self.sound.play("CRITICAL")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Sous-tension", "CRITICAL", datetime.now())
            print(f"[ALERTE CRITIQUE] Tension trop basse: {data['tension_alim']} V")
            return ("CRITICAL", f"Tension trop basse: ({data['tension_alim']} V)")

        elif data["tension_alim"] > self.thresholds["tension_max"]:
            self.sound.play("CRITICAL")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Sur-tension", "CRITICAL", datetime.now())
            print(f"[ALERTE CRITIQUE] Tension trop élevée: {data['tension_alim']} V")
            return ("CRITICAL", f"Tension trop élevée: ({data['tension_alim']} V)")

        elif (self.thresholds["tension_min"] <= data["tension_alim"] <= self.thresholds["tension_min"] + 1) or \
             (self.thresholds["tension_max"] - 1 <= data["tension_alim"] <= self.thresholds["tension_max"]):
            self.sound.play("WARNING")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Tension Proche Limite", "WARNING", datetime.now())
            print(f"[ALERTE] Tension proche des limites: {data['tension_alim']} V")
            return ("WARNING", f"Tension proche des limites: ({data['tension_alim']} V)")

        else:
            self.sound.play("INFO")
            await asyncio.to_thread(self.alert_model.save, "RECEPTEUR", equipment_id, "Tension Normale", "INFO", datetime.now(), True)
            print(f"[INFO] Tension normale: {data['tension_alim']} V")

        # S'il n'y a aucune alerte, retourner un état normal
        return ("INFO", "État de fonctionnement normal.")

    # Actions from UI
    def set_frequency(self, frequency_mhz):
        # validate
        if frequency_mhz < 118.0 or frequency_mhz > 144.0:
            return False, "Fréquence hors plage autorisée."
        return self.modbus.write_register(0, int(frequency_mhz * 100)), None

    def set_squelch(self, squelch_value: int):
        if squelch_value < 0 or squelch_value > 50:
            return False, "Valeur de squelch hors plage."
        return self.modbus.write_register(3, int(squelch_value)), None
            