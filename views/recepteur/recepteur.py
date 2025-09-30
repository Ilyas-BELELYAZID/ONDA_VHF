import asyncio
import datetime
from collections import deque

from PySide6.QtCore import QCoreApplication, QThread, QTimer, Signal, Slot, Qt, QObject
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.recepteur.ui_recepteur import Ui_MainWindow
from controllers.recepteur_controller import RecepteurController

# Intégration de Matplotlib dans PySide6
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates


class Recepteur_Screen(QMainWindow):
    # Signal pour recevoir les données du thread du contrôleur de manière sécurisée
    data_signal = Signal(dict)
    def __init__(self, user_id: int = None, parent=None, duration: int = 2000):
        super().__init__(parent)

        self.duration = duration

        self.user_id = user_id

        # Create an instance of the controller
        self.controller = RecepteurController()

        # --- Données pour le graphique ---
        self.timestamps = deque(maxlen=50) # Garde les 50 dernières valeurs
        self.snr_values = deque(maxlen=50)
        self.tmp_values = deque(maxlen=50)

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Les données de graphique
        self.snr_plot = MatplotlibCanvas(self, width=6, height=5, dpi=100)
        self.ui.verticalLayout.addWidget(self.snr_plot)

        self.tmp_plot = MatplotlibCanvas(self, width=6, height=5, dpi=100)
        self.ui.verticalLayout_7.addWidget(self.tmp_plot)

        # --- Démarrage du contrôleur ---
        self.setup_controller()

        # --- Connexion des signaux ---
        self.ui.changeFreqButton.clicked.connect(self.handle_set_frequency)
        self.ui.adjustSquelchButton.clicked.connect(self.handle_set_squelch)

    def setup_controller(self):
        # Le callback du contrôleur émettra notre signal thread-safe
        self.controller.data_callback = self.data_signal.emit
        # Le signal est connecté au slot qui met à jour l'UI
        self.data_signal.connect(self.update_ui)
        # Démarrage du contrôleur
        self.controller.start()
        print("Contrôleur démarré en arrière-plan.")

    @Slot(dict)
    def update_ui(self, data: dict):
        print(f"[UI] Données reçues: {data}")
        # --- Mise à jour des labels ---
        self.ui.freqValueLabel.setText(f"{data.get('frequency_mhz', 0):.2f} MHz")
        self.ui.powerValueLabel.setText(f"{data.get('rssi_dbm', 0)} dBm")
        self.ui.noiseValueLabel.setText(f"{data.get('snr_db', 0):.1f} dB")
        self.ui.squelchValueLabel.setText(f"{data.get('squelch', 0)}")
        self.ui.tmpValueLabel.setText(f"{data.get('temperature_c', 0):.1f} °C")
        self.ui.alimValueLabel.setText(f"{data.get('tension_alim', 0)} V")

        # Mise à jour du message d'alerte et de son style
        alert_data = data.get("alert_data", ("INFO", "Aucun message."))
        severity, message = alert_data
        self.show_alert(message, severity)
        
        # --- Mise à jour du graphique ---
        self.timestamps.append(datetime.datetime.now())
        self.snr_values.append(data.get('snr_db', 0))
        self.tmp_values.append(data.get('temperature_c', 0))
        self.update_plot()

    def update_plot(self):

        # Graphique SNR
        self.snr_plot.axes.clear()
        self.snr_plot.axes.plot(self.timestamps, self.snr_values, marker='o')
        
        # Formatage du graphique
        self.snr_plot.axes.set_ylabel("SNR (dB)")
        self.snr_plot.axes.grid(True)

        # Graphique Température
        self.tmp_plot.axes.clear()
        self.tmp_plot.axes.plot(self.timestamps, self.tmp_values, marker='o', color='red')
        
        # Formatage du graphique
        self.tmp_plot.axes.set_ylabel("Température (°C)")
        self.tmp_plot.axes.grid(True)

        for chart in [self.snr_plot, self.tmp_plot]:
            chart.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            chart.figure.autofmt_xdate()
            chart.draw()

    def run_blocking_task(self, task_function, *args):
        """Exécute une fonction bloquante dans un thread séparé pour ne pas geler l'UI."""
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
        try:
            freq = float(self.ui.freqLineEdit.text())
            reply = QMessageBox.question(self, "Confirmation", f"Changer la fréquence pour {freq:.2f} MHz ?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.run_blocking_task(self.controller.set_frequency, freq)
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer une fréquence valide.")
            
    def handle_set_squelch(self):
        try:
            sq = int(self.ui.squelchLineEdit.text())
            reply = QMessageBox.question(self, "Confirmation", f"Changer le squelch pour {sq} ?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.run_blocking_task(self.controller.set_squelch, sq)
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer une valeur de squelch valide.")

    @Slot(object)
    def on_command_result(self, result):
        ok, error_message = result
        if not ok:
            QMessageBox.critical(self, "Échec de la Commande", error_message)
        else:
            print("[UI] Commande exécutée avec succès.")

    def show_alert(self, text: str, level="CRITICAL"):
        # Levels: CRITICAL (red), WARNING (orange), INFO (blue)
        if level == "CRITICAL":
            bg = "#d9534f"
            fg = "#FFFFFF"
            self.ui.label_2.setPixmap(QPixmap(u":/icons/icons/exclamation-circle.svg"))
        elif level == "WARNING":
            bg = "#f0ad4e"
            fg = "#FFFFFF"
            self.ui.label_2.setPixmap(QPixmap(u":/icons/icons/alert-triangle.svg"))
        else:
            bg = "#5bc0de"
            fg = "#FFFFFF"
            self.ui.label_2.setPixmap(QPixmap(u":/icons/icons/circle-check.svg"))
            
        self.ui.alertFrame.setStyleSheet(f"background-color: {bg}; border-radius: 8px; border: 1px solid {bg};")
        self.ui.alertLabel.setStyleSheet(f"border: none; font-size: 14px; font-weight: 600; color: {fg};")
        self.ui.label_2.setStyleSheet(f"border: none;")

        self.ui.alertLabel.setText(QCoreApplication.translate("MainWindow", text, None))

        self.ui.alertFrame.setVisible(True)
        QTimer.singleShot(self.duration, self.clear_alert)

    def clear_alert(self):
        self.ui.alertFrame.setVisible(False)
        self.ui.alertLabel.setText("")

class MatplotlibCanvas(FigureCanvas):
    """Widget Matplotlib pour l'intégration dans PySide6."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)

# Worker pour exécuter les tâches bloquantes sans geler l'UI
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
