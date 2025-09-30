import datetime
from collections import deque
from PySide6.QtCore import QCoreApplication, QTimer, QThread, Signal, Slot, Qt, QObject
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QDialog, QDialogButtonBox
from PySide6.QtGui import QPixmap
from views.emetteur.ui_emetteur import Ui_MainWindow
from controllers.emetteur_controller import EmetteurController

# Intégration de Matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates

class Emetteur_Screen(QMainWindow):
    # Signal pour recevoir les données du thread du contrôleur de manière sécurisée
    data_signal = Signal(dict)

    def __init__(self, user_id: int = None, parent=None, duration: int = 2500):
        super().__init__(parent)

        self.duration = duration

        self.user_id = user_id

        # Create an instance of the controller
        self.controller = EmetteurController()

        # Données pour les graphiques
        self.timestamps = deque(maxlen=30)
        self.power_values = deque(maxlen=30)
        self.temp_values = deque(maxlen=30)

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Les données des graphiques
        self.power_chart = MatplotlibCanvas()
        self.temp_chart = MatplotlibCanvas()
        
        self.ui.verticalLayout.addWidget(self.power_chart)

        self.ui.verticalLayout_2.addWidget(self.temp_chart)

        self.setup_controller()
        
        # Connexions
        self.ui.pushButton_4.clicked.connect(self.handle_set_frequency)
        self.ui.pushButton_5.clicked.connect(self.handle_set_power)
        self.ui.pushButton.clicked.connect(self.handle_set_tdm)
        self.ui.pushButton_6.clicked.connect(self.handle_toggle_enabled)
            
    def setup_controller(self):
        # Le callback du contrôleur émettra notre signal thread-safe
        self.controller.data_callback = self.data_signal.emit
        # Le signal est connecté au slot qui met à jour l'UI
        self.data_signal.connect(self.update_ui)
        # Démarrage du contrôleur
        self.controller.start()
        print("Contrôleur démarré en arrière-plan.")

    @Slot(dict)
    def update_ui(self, data):
        self.ui.label_4.setText(f"{data['frequency_mhz']:.2f} MHz")
        self.ui.label_5.setText(f"{data['power_pct']:.1f} W")
        self.ui.label_8.setText(f"{data['temperature_c']:.1f} °C")
        self.ui.label_9.setText(f"{data['modulation_rate']:.1f} %")
        self.ui.label_11.setText(f"{data['tension_alim']:.1f} V")
        self.ui.label_20.setText(f"{data['ROS']:.1f}")
        self.ui.label_18.setText("ACTIF" if data['enabled'] else "DÉSACTIVÉ")
        self.ui.label_18.setStyleSheet("color: green;" if data['enabled'] else "color: red;")

        # Mise à jour du message d'alerte et de son style
        alert_message = data.get("alert_message", ("INFO", "Aucun message."))
        severity, message = alert_message
        self.show_alert(message, severity)
        
        # Mettre à jour les données des graphiques
        now = datetime.datetime.now()
        self.timestamps.append(now)
        self.power_values.append(data['power_pct'])
        self.temp_values.append(data['temperature_c'])
        self.update_charts()

    def update_charts(self):
        # Graphique Puissance
        self.power_chart.axes.clear()
        self.power_chart.axes.plot(self.timestamps, self.power_values, 'o', color='blue') # 'o' pour les cercles
        self.power_chart.axes.set_ylabel("Puissance (W)")
        self.power_chart.axes.grid(True)
        
        # Graphique Température
        self.temp_chart.axes.clear()
        self.temp_chart.axes.plot(self.timestamps, self.temp_values, 'o', color='red')
        self.temp_chart.axes.set_ylabel("Température (°C)")
        self.temp_chart.axes.grid(True)
        
        # Formatage commun
        for chart in [self.power_chart, self.temp_chart]:
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
        dialog = InputDialog(self, "Modifier la Fréquence", "Nouvelle fréquence (MHz):")
        if dialog.exec():
            value = dialog.get_value()
            if value is not None: self.run_blocking_task(self.controller.set_frequency, value)

    def handle_set_power(self):
        dialog = InputDialog(self, "Régler la Puissance", "Nouvelle puissance (W):")
        if dialog.exec():
            value = dialog.get_value()
            if value is not None: self.run_blocking_task(self.controller.set_power, value)

    def handle_set_tdm(self):
        dialog = InputDialog(self, "Modifier le Taux de modulation", "Nouvelle TDM (%):")
        if dialog.exec():
            value = dialog.get_value()
            if value is not None: self.run_blocking_task(self.controller.set_tdm, value)

    def handle_toggle_enabled(self):
        self.run_blocking_task(self.controller.toggle_enabled)

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
            self.ui.label_16.setPixmap(QPixmap(u":/icons/icons/exclamation-circle.svg"))
        elif level == "WARNING":
            bg = "#f0ad4e"
            fg = "#FFFFFF"
            self.ui.label_16.setPixmap(QPixmap(u":/icons/icons/alert-triangle.svg"))
        else:
            bg = "#5bc0de"
            fg = "#FFFFFF"
            self.ui.label_16.setPixmap(QPixmap(u":/icons/icons/circle-check.svg"))
            
        self.ui.frame_5.setStyleSheet(f"width: 1120px; height: 74px; background-color: {bg}; border-radius: 8px; border: 1px solid {bg};")
        self.ui.label_15.setStyleSheet(f"border: none; font-size: 14px; font-weight: 600; color: {fg};")

        self.ui.label_15.setText(QCoreApplication.translate("MainWindow", text, None))

        self.ui.frame_5.setVisible(True)
        QTimer.singleShot(self.duration, self.clear_alert)

    def clear_alert(self):
        self.ui.frame_5.setVisible(False)
        self.ui.label_15.setText("")

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(5, 2.5), dpi=100)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        self.setParent(parent)

class InputDialog(QDialog):
    """Fenêtre de dialogue simple pour la saisie d'une valeur."""
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
