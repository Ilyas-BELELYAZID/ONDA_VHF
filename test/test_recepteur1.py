# views/recepteur_vhf_controller.py
# -*- coding: utf-8 -*-
"""
Contrôleur pour `ui_recepteur_vhf.py`.
Requirements:
  pip install PySide6 matplotlib
"""

from collections import deque
import random
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QDoubleValidator, QIntValidator, QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QWidget, QVBoxLayout
)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# importe l'Ui générée
from views.ui_recepteur_vhf import Ui_MainWindow


class RecepteurVHFWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # === Validators ===
        # Plage VHF typique 30 - 300 MHz
        freq_validator = QDoubleValidator(30.0, 300.0, 3, self)
        self.ui.freqLineEdit.setValidator(freq_validator)

        squelch_validator = QIntValidator(0, 40, self)
        self.ui.squelchLineEdit.setValidator(squelch_validator)

        # === Connect signals ===
        self.ui.changeFreqButton.clicked.connect(self.on_change_freq)
        self.ui.adjustSquelchButton.clicked.connect(self.on_adjust_squelch)
        self.ui.settingsButton.clicked.connect(self.on_settings)
        self.ui.helpButton.clicked.connect(self.on_help)
        self.ui.receiverButton.toggled.connect(self.on_receiver_toggled)

        # Set some tooltips
        self.ui.freqLineEdit.setToolTip("Entrer la fréquence en MHz (ex: 146.520)")
        self.ui.squelchLineEdit.setToolTip("Niveau de squelch (0-40)")

        # === Matplotlib SNR plot ===
        self._setup_snr_plot()

        # Data buffers for graph
        self.snr_history = deque(maxlen=200)
        for _ in range(40):
            self.snr_history.append(10.0)  # valeur initiale

        # === Timer pour simulation/rafraîchissement ===
        self.update_timer = QTimer(self)
        self.update_timer.setInterval(500)  # ms
        self.update_timer.timeout.connect(self._update_measurements)
        self.update_timer.start()

        # Threshold d'alerte (dBm) — ajuste selon ton matos
        self.alert_threshold_dbm = -95.0

        # quelques valeurs d'initialisation affichées par défaut dans UI
        self.ui.freqValueLabel.setText("146.520 MHz")
        self.ui.powerValueLabel.setText("-85 dBm")
        self.ui.noiseValueLabel.setText("2.3 %")
        self.ui.squelchValueLabel.setText("Ouvert")

    # ---------- UI handlers ----------
    def on_change_freq(self):
        text = self.ui.freqLineEdit.text().strip()
        if not text:
            QMessageBox.warning(self, "Fréquence invalide", "Entrez une fréquence en MHz.")
            return
        try:
            freq = float(text)
        except ValueError:
            QMessageBox.warning(self, "Fréquence invalide", "Format invalide pour la fréquence.")
            return
        # mise à jour de l'affichage
        self.ui.freqValueLabel.setText(f"{freq:.3f} MHz")
        # TODO: ici appeler la fonction qui modifie réellement la fréquence du récepteur
        # ex: self.receiver.set_frequency(freq)
        self._flash_message(f"Fréquence changée vers {freq:.3f} MHz")

    def on_adjust_squelch(self):
        text = self.ui.squelchLineEdit.text().strip()
        if not text:
            QMessageBox.warning(self, "Squelch invalide", "Entrez un niveau de squelch (0-40).")
            return
        try:
            level = int(text)
        except ValueError:
            QMessageBox.warning(self, "Squelch invalide", "Format invalide pour le squelch.")
            return
        self.ui.squelchValueLabel.setText(str(level))
        # TODO: appliquer le squelch au matériel / service
        self._flash_message(f"Squelch réglé sur {level}")

    def on_settings(self):
        QMessageBox.information(self, "Paramètres", "Ouvre la fenêtre de configuration (à implémenter).")

    def on_help(self):
        QMessageBox.information(self, "Aide", "Aide / documentation rapide (à compléter).")

    def on_receiver_toggled(self, checked: bool):
        if checked:
            self._flash_message("Récepteur activé")
            # réactiver timer si besoin
            if not self.update_timer.isActive():
                self.update_timer.start()
        else:
            self._flash_message("Récepteur désactivé")
            # arrêter temporisation si réception coupée
            # (on continue la simulation ; pour matériel réel, couper la lecture)
            # self.update_timer.stop()

    # ---------- Mesures & simulation ----------
    def _update_measurements(self):
        """Simulation de nouvelles mesures (remplace par acquisition réelle)."""
        # Simuler puissance reçue en dBm autour de -80 à -110
        power = random.gauss(-85, 5)
        noise_pct = max(0.0, min(100.0, random.gauss(2.5, 1.5)))
        # calculer SNR simulé (simple)
        snr = random.gauss(12.0, 3.0)

        # mettre à jour labels
        self.ui.powerValueLabel.setText(f"{power:.1f} dBm")
        self.ui.noiseValueLabel.setText(f"{noise_pct:.1f} %")
        # squelch label déjà mis via bouton ; on peut montrer "Fermé" si power < threshold + hysteresis
        squelch_level_text = self.ui.squelchValueLabel.text()
        try:
            squ_lvl = int(squelch_level_text)
        except Exception:
            squ_lvl = None

        # déterminer état squelch simple (ex: fermer si puissance < threshold - 5)
        if power < (self.alert_threshold_dbm - 5):
            self.ui.squelchValueLabel.setText("Fermé")
        else:
            # si l'utilisateur avait un nombre, réaffiche le nombre, sinon 'Ouvert'
            if squ_lvl is not None:
                self.ui.squelchValueLabel.setText(str(squ_lvl))
            else:
                self.ui.squelchValueLabel.setText("Ouvert")

        # alerte si faible signal
        if power < self.alert_threshold_dbm:
            self._show_alert(True, f"Alerte — signal faible ({power:.1f} dBm)")
        else:
            self._show_alert(False)

        # mise à jour du graphe SNR
        self.snr_history.append(snr)
        self._update_snr_plot()

    # ---------- Alertes ----------
    def _show_alert(self, show: bool, message: str = None):
        if show:
            self.ui.alertFrame.setVisible(True)
            if message:
                self.ui.alertLabel.setText(f"<b>Alerte</b> {message}")
        else:
            self.ui.alertFrame.setVisible(False)

    # ---------- petites utilitaires ----------
    def _flash_message(self, text: str):
        # notif discrète (statusbar)
        self.statusBar().showMessage(text, 2500)

    # ---------- Matplotlib plot ----------
    def _setup_snr_plot(self):
        # remplacer le QLabel graphPlaceholder par un canvas Matplotlib
        placeholder = self.ui.graphPlaceholder
        parent_layout = placeholder.parentWidget().layout()
        # create canvas
        self.figure = Figure(figsize=(4, 2.5), tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("SNR (temps réel)")
        self.ax.set_xlabel("échantillons")
        self.ax.set_ylabel("dB")
        self.ax.set_ylim(0, 30)
        self.line, = self.ax.plot([], [], linewidth=1.5)

        # Clear placeholder and add canvas
        try:
            # enlever le label du layout si présent
            # trouver l'index et remplacer
            for i in range(parent_layout.count()):
                item = parent_layout.itemAt(i)
                if item and item.widget() is placeholder:
                    widget_item = parent_layout.takeAt(i)
                    widget_item.widget().setParent(None)
                    break
        except Exception:
            pass

        parent_layout.addWidget(self.canvas)

    def _update_snr_plot(self):
        y = list(self.snr_history)
        x = list(range(len(y)))
        self.line.set_data(x, y)
        if y:
            ymin = max(0, min(y) - 2)
            ymax = max(20, max(y) + 2)
            self.ax.set_ylim(ymin, ymax)
            self.ax.set_xlim(0, max(50, len(y)))
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw_idle()


# === Exécutable simple pour test ===
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Optionnel: charger icône de l'application (si tu as un .png)
    # window_icon = QIcon("assets/icons/radio.png")
    # app.setWindowIcon(window_icon)

    w = RecepteurVHFWindow()
    w.resize(1200, 800)
    w.show()
    sys.exit(app.exec())
