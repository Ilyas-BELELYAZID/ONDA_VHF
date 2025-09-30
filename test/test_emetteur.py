import sys
import asyncio
import threading
import time
import datetime
from typing import Optional, Callable
from collections import deque

# --- Dépendances à installer: pip install PySide6 matplotlib ---
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox, QDialog, QDialogButtonBox
)
from PySide6.QtCore import QThread, Signal, Slot, Qt, QObject
from PySide6.QtGui import QFont

# Intégration de Matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates

# =============================================================================
# 1. CLASSES MOCK (SIMULATIONS DE VOS SERVICES ET MODÈLES)
# =============================================================================

class MockModbusService:
    """Simule un client Modbus avec des valeurs qui changent pour tester les alertes."""
    def __init__(self, device_id=1):
        print(f"[MockModbus] Initialisé pour l'appareil {device_id}.")
        # [Freq, Power, Temp, Mod, Volt, Enabled]
        self.regs = [11870, 500, 350, 850, 240, 1]
        self.start_time = time.time()

    def connect(self):
        print("[MockModbus] Connexion (bloquante) simulée.")
        time.sleep(0.2) # Simule un appel réseau bloquant
        return True

    def read_holding(self, address, count):
        # Simule des conditions changeantes
        elapsed = time.time() - self.start_time
        cycle_time = 40

        if (elapsed % cycle_time) < 10: # Normal
            self.regs[2] = 350 # Temp = 35°C
            self.regs[1] = 500 # Power = 50W
            self.regs[4] = 240 # Volt = 24V
        elif (elapsed % cycle_time) < 20: # Température haute (Warning)
            self.regs[2] = 480 # Temp = 48°C
        elif (elapsed % cycle_time) < 30: # Température critique
            self.regs[2] = 600 # Temp = 60°C
        else: # Puissance hors bornes
            self.regs[1] = 40 # Power = 4W
        
        print(f"[MockModbus] Lecture (bloquante)... retourne {self.regs}")
        time.sleep(0.3)
        return self.regs

    def write_register(self, address: int, value: int):
        print(f"[MockModbus] Écriture (bloquante)... reg[{address}] = {value}")
        if address < len(self.regs):
            self.regs[address] = value
            time.sleep(0.1)
            return True
        return False

    def close(self):
        print("[MockModbus] Connexion fermée.")

class MockEmetteurModel:
    def __init__(self): self.latest_data = {}
    def save_emetteur(self, data, id_emetteur): pass
    def get_latest(self, id_emetteur): return self.latest_data

class MockAlerteModel:
    def save(self, eq_type, eq_id, type, severity, resolved=False):
        if not resolved:
            print(f"[MockAlerteDB] Alerte '{severity}' sauvegardée: {type}")

class MockAlertSoundManager:
    def play(self, sound_type: str):
        if sound_type != "INFO":
            print(f"🎵 [AlertSoundManager] JOUER SON: {sound_type} 🎵")

# =============================================================================
# 2. VOTRE CLASSE EMETTEURCONTROLLER (ADAPTÉE POUR LES MOCKS)
# =============================================================================
class EmetteurController:
    def __init__(self, device_id=1, poll_interval=2):
        self.modbus = MockModbusService(device_id=device_id)
        self.model = MockEmetteurModel()
        self.alerte_model = MockAlerteModel()
        self.sound = MockAlertSoundManager()
        self._loop = None
        self._thread = None
        self.poll_interval = poll_interval
        self._stop_event = threading.Event()
        self.data_callback: Optional[Callable[[dict], None]] = None
        self.tolerances = {"temp_max": 55.0, "power_min": 5.0, "power_max": 55.0, "tension_min": 21.0, "tension_max": 31.0}

    def start(self):
        if self._thread and self._thread.is_alive(): return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def _run_loop(self):
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._loop.create_task(self._polling_task())
        try:
            self._loop.run_forever()
        finally:
            self._loop.close()

    async def _polling_task(self, id_emetteur=1):
        await asyncio.to_thread(self.modbus.connect)
        while not self._stop_event.is_set():
            try:
                regs = await asyncio.to_thread(self.modbus.read_holding, 0, 6)
                if regs:
                    data = {
                        "frequency_mhz": regs[0] / 100.0, "power_pct": regs[1] / 10.0,
                        "temperature_c": regs[2] / 10.0, "modulation_rate": regs[3] / 10.0,
                        "tension_alim": regs[4] / 10.0, "enabled": bool(regs[5])
                    }
                    await asyncio.to_thread(self.model.save_emetteur, data, id_emetteur)
                    self.model.latest_data = data
                    
                    # Récupérer le tuple (sévérité, message) et l'ajouter aux données
                    alert_data = await asyncio.to_thread(self._evaluate_alerts, data)
                    data["alert_data"] = alert_data

                    if self.data_callback:
                        self.data_callback(data)
            except Exception as e:
                print("Polling exception:", e)
            await asyncio.sleep(self.poll_interval)

    def stop(self):
        self._stop_event.set()
        if self._loop: self._loop.call_soon_threadsafe(self._loop.stop)
        try: self.modbus.close()
        except Exception: pass
        if self._thread: self._thread.join(timeout=2)

    def _evaluate_alerts(self, data: dict, id_equipement=1):
        """
        Évalue les données, sauvegarde les alertes et retourne un tuple (SEVERITE, message).
        La priorité est CRITICAL > WARNING > INFO.
        """
        # --- Temperature ---
        if data["temperature_c"] >= self.tolerances["temp_max"]:
            self.sound.play("CRITICAL")
            self.alerte_model.save("EMETTEUR", id_equipement, "Surchauffe", "CRITICAL")
            return ("CRITICAL", f"Surchauffe ({data['temperature_c']:.1f}°C)")
        elif data["temperature_c"] >= (self.tolerances["temp_max"] - 10):
            self.sound.play("WARNING")
            self.alerte_model.save("EMETTEUR", id_equipement, "Température proche du seuil", "WARNING")
            return ("WARNING", f"Température élevée ({data['temperature_c']:.1f}°C)")

        # --- Puissance ---
        if not (self.tolerances["power_min"] <= data["power_pct"] <= self.tolerances["power_max"]):
            self.sound.play("CRITICAL")
            self.alerte_model.save("EMETTEUR", id_equipement, "Puissance hors bornes", "CRITICAL")
            return ("CRITICAL", f"Puissance hors bornes ({data['power_pct']:.1f} W)")

        # --- Tension ---
        if not (self.tolerances["tension_min"] <= data["tension_alim"] <= self.tolerances["tension_max"]):
            self.sound.play("CRITICAL")
            self.alerte_model.save("EMETTEUR", id_equipement, "Tension hors bornes", "CRITICAL")
            return ("CRITICAL", f"Tension hors bornes ({data['tension_alim']:.1f} V)")

        # S'il n'y a aucune alerte, retourner un état normal
        return ("INFO", "État de fonctionnement normal.")

    def set_frequency(self, frequency_mhz):
        if not (118.0 <= frequency_mhz <= 144.0): return False, "Fréquence hors plage."
        return self.modbus.write_register(0, int(frequency_mhz * 100)), None
    
    def set_power(self, power_w):
        if not (5.0 <= power_w <= 55.0): return False, "Puissance hors plage."
        return self.modbus.write_register(1, int(power_w * 10)), None

    def toggle_enabled(self, equipment_id=1):
        current = self.model.get_latest(equipment_id).get("enabled", True)
        return self.modbus.write_register(5, 0 if current else 1), None

# =============================================================================
# 3. FENÊTRE DE TEST PYSIDE6
# =============================================================================
class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(5, 2.5), dpi=100)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        self.setParent(parent)

class InputDialog(QDialog):
    def __init__(self, parent, title, prompt, is_float=True):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel(prompt))
        self.input = QLineEdit()
        self.layout.addWidget(self.input)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout.addWidget(buttons)
        self.is_float = is_float

    def get_value(self):
        try:
            return float(self.input.text()) if self.is_float else int(self.input.text())
        except (ValueError, TypeError):
            return None

class Worker(QObject):
    finished = Signal(object)
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
    @Slot()
    def run(self):
        result = self.func(*self.args, **self.kwargs)
        self.finished.emit(result)

class TestWindow(QMainWindow):
    data_signal = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Test Interface Émetteur")
        self.setGeometry(100, 100, 900, 600)
        self.controller = EmetteurController()
        self.timestamps = deque(maxlen=30)
        self.power_values = deque(maxlen=30)
        self.temp_values = deque(maxlen=30)
        self.setup_ui()
        self.setup_controller()

    def setup_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_panel.setFixedWidth(350)

        alert_title_label = QLabel("État Actuel de l'Équipement:")
        alert_title_label.setFont(QFont("Arial", 10, QFont.Bold))
        self.alert_status_label = QLabel("Initialisation...")
        self.alert_status_label.setFont(QFont("Arial", 11, QFont.Bold))
        self.alert_status_label.setStyleSheet("padding: 5px; border-radius: 4px; background-color: #e9ecef;")
        self.alert_status_label.setAlignment(Qt.AlignCenter)
        self.alert_status_label.setWordWrap(True)

        grid = QGridLayout()
        self.freq_label = self.create_data_label()
        self.power_label = self.create_data_label()
        self.temp_label = self.create_data_label()
        self.mod_label = self.create_data_label()
        self.volt_label = self.create_data_label()
        self.status_label = self.create_data_label()
        
        grid.addWidget(QLabel("Fréquence:"), 0, 0); grid.addWidget(self.freq_label, 0, 1)
        grid.addWidget(QLabel("Puissance:"), 1, 0); grid.addWidget(self.power_label, 1, 1)
        grid.addWidget(QLabel("Température:"), 2, 0); grid.addWidget(self.temp_label, 2, 1)
        grid.addWidget(QLabel("Modulation:"), 3, 0); grid.addWidget(self.mod_label, 3, 1)
        grid.addWidget(QLabel("Tension:"), 4, 0); grid.addWidget(self.volt_label, 4, 1)
        grid.addWidget(QLabel("État:"), 5, 0); grid.addWidget(self.status_label, 5, 1)

        self.freq_btn = QPushButton("Modifier Fréquence")
        self.power_btn = QPushButton("Régler Puissance")
        self.toggle_btn = QPushButton("Activer/Désactiver")
        
        left_layout.addWidget(alert_title_label)
        left_layout.addWidget(self.alert_status_label)
        left_layout.addSpacing(15)
        left_layout.addLayout(grid)
        left_layout.addSpacing(20)
        left_layout.addWidget(self.freq_btn)
        left_layout.addWidget(self.power_btn)
        left_layout.addWidget(self.toggle_btn)
        left_layout.addStretch()

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        self.power_chart = MatplotlibCanvas()
        self.temp_chart = MatplotlibCanvas()
        right_layout.addWidget(QLabel("<h3>Puissance d'Émission (W)</h3>"))
        right_layout.addWidget(self.power_chart)
        right_layout.addWidget(QLabel("<h3>Température Interne (°C)</h3>"))
        right_layout.addWidget(self.temp_chart)

        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)

        self.freq_btn.clicked.connect(self.handle_set_frequency)
        self.power_btn.clicked.connect(self.handle_set_power)
        self.toggle_btn.clicked.connect(self.handle_toggle_enabled)

    def create_data_label(self):
        label = QLabel("N/A")
        label.setFont(QFont("Arial", 12, QFont.Bold))
        return label

    def setup_controller(self):
        self.controller.data_callback = self.data_signal.emit
        self.data_signal.connect(self.update_ui)
        self.controller.start()
        print("Contrôleur démarré en arrière-plan.")

    @Slot(dict)
    def update_ui(self, data):
        self.freq_label.setText(f"{data['frequency_mhz']:.2f} MHz")
        self.power_label.setText(f"{data['power_pct']:.1f} W")
        self.temp_label.setText(f"{data['temperature_c']:.1f} °C")
        self.mod_label.setText(f"{data['modulation_rate']:.1f} %")
        self.volt_label.setText(f"{data['tension_alim']:.1f} V")
        self.status_label.setText("ACTIF" if data['enabled'] else "DÉSACTIVÉ")
        self.status_label.setStyleSheet("color: green;" if data['enabled'] else "color: red;")
        
        # Mise à jour du message d'alerte et de son style
        alert_data = data.get("alert_data", ("INFO", "Aucun message."))
        severity, message = alert_data
        
        self.alert_status_label.setText(message)
        
        if severity == "CRITICAL":
            style = "background-color: #dc3545; color: white;" # Rouge
        elif severity == "WARNING":
            style = "background-color: #ffc107; color: black;" # Jaune/Orange
        else: # INFO ou état normal
            style = "background-color: #28a745; color: white;" # Vert

        self.alert_status_label.setStyleSheet(f"padding: 5px; border-radius: 4px; {style}")
        
        now = datetime.datetime.now()
        self.timestamps.append(now)
        self.power_values.append(data['power_pct'])
        self.temp_values.append(data['temperature_c'])
        self.update_charts()

    def update_charts(self):
        self.power_chart.axes.clear()
        self.power_chart.axes.plot(self.timestamps, self.power_values, 'o', color='blue')
        self.power_chart.axes.set_ylabel("Puissance (W)")
        self.power_chart.axes.grid(True)
        
        self.temp_chart.axes.clear()
        self.temp_chart.axes.plot(self.timestamps, self.temp_values, 'o', color='red')
        self.temp_chart.axes.set_ylabel("Température (°C)")
        self.temp_chart.axes.grid(True)
        
        for chart in [self.power_chart, self.temp_chart]:
            chart.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            chart.figure.autofmt_xdate()
            chart.draw()

    def run_blocking_task(self, task_function, *args):
        self.thread = QThread()
        self.worker = Worker(task_function, *args)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_command_result)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def handle_set_frequency(self):
        dialog = InputDialog(self, "Modifier la Fréquence", "Nouvelle fréquence (MHz):")
        if dialog.exec():
            value = dialog.get_value()
            if value is not None: self.run_blocking_task(self.controller.set_frequency, value)

    def handle_set_power(self):
        dialog = InputDialog(self, "Régler la Puissance", "Nouvelle puissance (W):")
        if dialog.exec():
            value = dialog.get_value()
            if value is not None: self.run_blocking_task(self.controller.set_power, value)

    def handle_toggle_enabled(self):
        self.run_blocking_task(self.controller.toggle_enabled)

    @Slot(object)
    def on_command_result(self, result):
        ok, error_message = result
        if not ok:
            QMessageBox.critical(self, "Échec de la Commande", error_message)
        else:
            print("[UI] Commande exécutée avec succès.")

    def closeEvent(self, event):
        print("Fermeture de l'application...")
        self.controller.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())

