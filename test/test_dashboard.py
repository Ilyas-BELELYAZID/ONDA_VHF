import sys
import asyncio
import datetime
import time
import random
from collections import deque

# --- Dépendances à installer: pip install PySide6 matplotlib ---
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QTableWidget, QTableWidgetItem, QHeaderView
)
from PySide6.QtCore import QThread, Signal, Slot, Qt
from PySide6.QtGui import QFont

# Intégration de Matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates

# =============================================================================
# 1. CLASSES MOCK (SIMULATIONS DE VOS SERVICES ET MODÈLES)
# =============================================================================

class MockModbusService:
    """Simule un client Modbus avec des données dynamiques."""
    def __init__(self, device_id=1):
        print(f"[MockModbus] Initialisé pour l'appareil {device_id}.")
        self.start_time = time.time()

    async def connect(self):
        print("[MockModbus] Connexion asynchrone simulée.")
        await asyncio.sleep(0.2)
        return True

    async def read_holding(self, address, count):
        # Simule des données qui varient
        elapsed = time.time() - self.start_time
        # Température variant sinusoïdalement sur 24h
        temp_variation = 15 * (1 +__import__('math').sin(2 * 3.14159 * elapsed / (24 * 3600))) # Varie entre 15 et 45°C
        temp = 300 + int(temp_variation * 10) # 30.0 à 45.0°C
        # Puissance variant aléatoirement
        power = random.randint(750, 950) # 75.0 à 95.0%
        
        regs = [11870, power, temp, 850, 240, 1]
        await asyncio.sleep(0.3)
        return regs

    async def close(self):
        print("[MockModbus] Connexion fermée.")

class MockDashboardModel:
    """Simule le modèle de la base de données."""
    def get_equipment_count(self):
        # print("[MockDB] get_equipment_count")
        time.sleep(0.02)
        return 8

    def get_recent_alerts(self, limit):
        # print("[MockDB] get_recent_alerts")
        time.sleep(0.05)
        now = datetime.datetime.now()
        return [
            {'date': now - datetime.timedelta(minutes=5), 'type': 'Anomalie', 'desc': 'Puissance faible sur TX-02', 'status': 'Ouvert', 'severity': 'WARNING'},
            {'date': now - datetime.timedelta(hours=1), 'type': 'Défaillance', 'desc': 'Surchauffe RX-01', 'status': 'Ouvert', 'severity': 'CRITICAL'},
            {'date': now - datetime.timedelta(hours=3), 'type': 'Info', 'desc': 'Maintenance préventive effectuée', 'status': 'Fermé', 'severity': 'INFO'},
        ]

    def get_current_system_state(self):
        # print("[MockDB] get_current_system_state")
        time.sleep(0.01)
        return "Opérationnel - Dégradé"

    def get_last_update_time(self):
        # print("[MockDB] get_last_update_time")
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# =============================================================================
# 2. VOTRE CLASSE DASHBOARDCONTROLLER (ADAPTÉE POUR LES MOCKS)
# =============================================================================
class DashboardController(QThread):
    update = Signal(object)
    started_signal = Signal()
    stopped_signal = Signal()

    def __init__(self, device_id=1, poll_interval=3, parent=None):
        super().__init__(parent)
        self.modbus = MockModbusService(device_id=device_id)
        self.model = MockDashboardModel()
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
        finally:
            if self._loop and not self._loop.is_closed():
                self._loop.run_until_complete(self.modbus.close())
                self._loop.close()
            self.stopped_signal.emit()

    async def _async_start(self):
        connected = await self.modbus.connect()
        if not connected:
            print("Warning: Modbus connect failed")
        while self._running:
            try:
                summary = {"timestamp": datetime.datetime.now(), "devices": []}
                regs = await self.modbus.read_holding(0, 6)
                if regs is None:
                    device_data = {"id": 1, "online": False}
                else:
                    device_data = {
                        "id": 1, "online": True,
                        "frequency_mhz": regs[0] / 100.0,
                        "power_pct": regs[1] / 10.0,
                        "temperature_c": regs[2] / 10.0,
                    }
                summary["devices"].append(device_data)
                
                summary["equipment_count"] = await asyncio.to_thread(self.model.get_equipment_count)
                summary["recent_alerts"] = await asyncio.to_thread(self.model.get_recent_alerts, 6)
                summary["system_state"] = await asyncio.to_thread(self.model.get_current_system_state)
                summary["last_update"] = await asyncio.to_thread(self.model.get_last_update_time)

                self.update.emit(summary)
            except Exception as e:
                print("DashboardController loop error:", e)
            await asyncio.sleep(self.poll_interval)

    def stop(self):
        self._running = False
        if self._loop and self._loop.is_running():
            self._loop.call_soon_threadsafe(self._loop.stop)

# =============================================================================
# 3. WIDGETS PERSONNALISÉS ET FENÊTRE DE TEST
# =============================================================================
class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

class InfoWidget(QWidget):
    """Widget stylisé pour la vue d'ensemble."""
    def __init__(self, title: str, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.title_label = QLabel(title)
        self.value_label = QLabel("N/A")
        
        self.title_label.setAlignment(Qt.AlignCenter)
        self.value_label.setAlignment(Qt.AlignCenter)
        
        self.value_label.setFont(QFont("Arial", 20, QFont.Bold))
        
        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)
        
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: #f8f9fa; border-radius: 8px;")

    def set_value(self, text: str, color: str = "black"):
        self.value_label.setText(text)
        self.value_label.setStyleSheet(f"color: {color};")

class TestWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Test Interface Dashboard")
        self.setGeometry(50, 50, 1400, 800)
        
        # Données pour les graphiques
        self.temp_timestamps = deque(maxlen=288) # 24h * 12 (5 min par point)
        self.temp_values = deque(maxlen=288)
        
        self.setup_ui()
        self.setup_controller()

    def setup_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # --- Ligne 1: Vue d'ensemble ---
        overview_layout = QGridLayout()
        self.state_widget = InfoWidget("État Général du Système")
        self.equip_widget = InfoWidget("Équipements Connectés")
        self.alerts_widget = InfoWidget("Alertes en Cours")
        self.update_widget = InfoWidget("Dernière Mise à Jour")
        overview_layout.addWidget(self.state_widget, 0, 0)
        overview_layout.addWidget(self.equip_widget, 0, 1)
        overview_layout.addWidget(self.alerts_widget, 0, 2)
        overview_layout.addWidget(self.update_widget, 0, 3)

        # --- Ligne 2: Graphiques ---
        charts_layout = QHBoxLayout()
        self.temp_chart = MatplotlibCanvas()
        self.power_chart = MatplotlibCanvas()
        charts_layout.addWidget(self.temp_chart)
        charts_layout.addWidget(self.power_chart)

        # --- Ligne 3: Journal des alertes ---
        self.alerts_table = QTableWidget()
        self.alerts_table.setColumnCount(5)
        self.alerts_table.setHorizontalHeaderLabels(["Date", "Type", "Description", "Statut", "Gravité"])
        self.alerts_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.alerts_table.verticalHeader().setVisible(False)

        main_layout.addLayout(overview_layout)
        main_layout.addLayout(charts_layout)
        main_layout.addWidget(self.alerts_table)
        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 3)
        main_layout.setStretch(2, 2)

    def setup_controller(self):
        self.controller = DashboardController()
        self.controller.update.connect(self.update_ui)
        self.controller.start()
        print("Contrôleur démarré.")

    @Slot(object)
    def update_ui(self, summary: dict):
        # --- Mise à jour de la vue d'ensemble ---
        state = summary.get('system_state', 'Inconnu')
        state_color = "#dc3545" if "Dégradé" in state else "#28a745"
        self.state_widget.set_value(state, state_color)
        self.equip_widget.set_value(str(summary.get('equipment_count', 0)))
        
        alerts = summary.get('recent_alerts', [])
        open_alerts = [a for a in alerts if a.get('status') == 'Ouvert']
        alert_color = "#ffc107" if open_alerts else "black"
        self.alerts_widget.set_value(str(len(open_alerts)), alert_color)
        self.update_widget.set_value(summary.get('last_update', 'N/A').split(" ")[1])

        # --- Mise à jour des graphiques ---
        device_data = summary['devices'][0] if summary['devices'] else {}
        if device_data.get('online', False):
            self.update_temp_chart(summary['timestamp'], device_data['temperature_c'])
            self.update_power_chart(device_data['power_pct'])

        # --- Mise à jour du tableau d'alertes ---
        self.update_alerts_table(alerts)

    def update_temp_chart(self, timestamp, temp):
        self.temp_timestamps.append(timestamp)
        self.temp_values.append(temp)
        
        ax = self.temp_chart.axes
        ax.clear()
        ax.plot(self.temp_timestamps, self.temp_values, label='Température (°C)')
        
        # Formatage de l'axe X
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=4)) # Un tick toutes les 4h
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.set_xlim(datetime.datetime.now() - datetime.timedelta(hours=24), datetime.datetime.now())
        
        ax.set_title("Courbe de Température (24h)")
        ax.set_ylabel("°C")
        ax.grid(True)
        ax.legend()
        self.temp_chart.draw()

    def update_power_chart(self, power):
        ax = self.power_chart.axes
        ax.clear()
        
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 1)
        ax.barh([0.5], [power], height=0.2, color='skyblue')
        ax.text(power + 2, 0.5, f"{power:.1f}%", va='center', fontweight='bold')
        
        ax.set_yticks([]) # Cache l'axe Y
        ax.set_title("Puissance d'Émission Actuelle")
        self.power_chart.draw()

    def update_alerts_table(self, alerts):
        self.alerts_table.setRowCount(len(alerts))
        for row, alert in enumerate(alerts):
            self.alerts_table.setItem(row, 0, QTableWidgetItem(alert['date'].strftime('%Y-%m-%d %H:%M')))
            self.alerts_table.setItem(row, 1, QTableWidgetItem(alert['type']))
            self.alerts_table.setItem(row, 2, QTableWidgetItem(alert['desc']))
            self.alerts_table.setItem(row, 3, QTableWidgetItem(alert['status']))
            self.alerts_table.setItem(row, 4, QTableWidgetItem(alert['severity']))

    def closeEvent(self, event):
        print("Fermeture de l'application...")
        self.controller.stop()
        self.controller.wait(2000) # Attendre que le thread se termine
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())
