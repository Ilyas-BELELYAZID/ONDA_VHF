import sys
import asyncio
import time
import datetime
from collections import deque

# --- Dépendances à installer: pip install PySide6 matplotlib ---
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox
)
from PySide6.QtCore import QThread, Signal, Slot, Qt
from PySide6.QtGui import QFont

# Intégration de Matplotlib dans PySide6
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates

# =============================================================================
# 1. CLASSES MOCK (SIMULATIONS DE VOS SERVICES ET MODÈLES)
# =============================================================================

class MockModbusService:
    """
    Simule un client Modbus avec des valeurs qui changent pour tester les alertes.
    """
    def __init__(self, device_id=2):
        print(f"[MockModbus] Initialisé pour l'appareil {device_id}.")
        # [Freq*100, RSSI, SNR*10, Squelch]
        self.regs = [12550, 65486, 250, 10] # Freq=125.5, RSSI=-50, SNR=25.0
        self.start_time = time.time()

    async def connect(self):
        print("[MockModbus] Connexion simulée réussie.")
        await asyncio.sleep(0.1)
        return True

    async def read_holding(self, address, count):
        # Simule des conditions changeantes toutes les ~10 secondes
        elapsed = time.time() - self.start_time
        cycle_time = 30 # Durée d'un cycle complet de simulation

        if (elapsed % cycle_time) < 10: # 0-10s: Signal Normal
            self.regs[1] = 65486 # RSSI = -50 dBm (signed: -50 + 65536)
            self.regs[2] = 250   # SNR = 25.0 dB
        elif (elapsed % cycle_time) < 20: # 10-20s: Signal Faible (Warning/Critical)
            self.regs[1] = 65436 # RSSI = -100 dBm
        else: # 20-30s: Interférences (SNR bas)
            self.regs[1] = 65486 # Retour à RSSI normal
            self.regs[2] = 50    # SNR = 5.0 dB

        print(f"[MockModbus] Lecture... retourne {self.regs}")
        await asyncio.sleep(0.2)
        return self.regs

    async def write_register(self, address: int, value: int):
        print(f"[MockModbus] Écriture... reg[{address}] = {value}")
        if address < len(self.regs):
            self.regs[address] = value
            await asyncio.sleep(0.1)
            return True
        return False

    async def close(self):
        print("[MockModbus] Connexion fermée.")


class MockRecepteurModel:
    def save_recepteur(self, data, id_recepteur):
        # Dans une vraie app, ceci écrit en BDD. Ici, on affiche juste.
        # print(f"[MockRecepteurDB] Sauvegarde de l'état pour récepteur {id_recepteur}.")
        pass

class MockAlerteModel:
    def save(self, alert_data):
        if not alert_data.get("resolved", False):
            print(f"[MockAlerteDB] Alerte '{alert_data['severity']}' sauvegardée: {alert_data['type']}")

class MockAlertSoundManager:
    def play(self, sound_type: str):
        if sound_type != "INFO": # Ne pas spammer la console pour les cas normaux
            print(f"🎵 [AlertSoundManager] JOUER SON: {sound_type} 🎵")

# =============================================================================
# 2. INTÉGRATION DU CONTRÔLEUR DANS UN QTHREAD
# =============================================================================

# --- COLLEZ VOTRE CLASSE RecepteurController ICI ---
# Le code est recopié et adapté pour utiliser les Mocks définis ci-dessus.
class RecepteurController:
    # ... (Le code de votre RecepteurController est inséré ici) ...
    # Modifications:
    # - Remplacement des imports par les Mocks
    # - La méthode `save_recepteur` est maintenant asynchrone pour simuler un appel BDD
    
    # --- Début de la copie adaptée de votre code ---
    def __init__(self, device_id=2, poll_interval=2): # Intervalle court pour un test réactif
        self.modbus = MockModbusService(device_id=device_id)
        self.model = MockRecepteurModel()
        self.alert_model = MockAlerteModel()
        self.sound = MockAlertSoundManager()
        self.poll_interval = poll_interval
        self.running = False
        self.thresholds = {
            "rssi_weak_dbm": -100, "snr_low_db": 8.0,
            "squelch_expected_min": 0, "squelch_expected_max": 50
        }

    async def start_polling(self, callback=None):
        self.running = True
        ok = await self.modbus.connect()
        if not ok:
            print("La connexion Modbus a échoué.")
            self.running = False
            return

        while self.running:
            data = await self.read_recepteur()
            if data and callback:
                if asyncio.iscoroutinefunction(callback):
                    await callback(data)
                else:
                    callback(data)
            await asyncio.sleep(self.poll_interval)

    def stop_polling(self):
        self.running = False
        asyncio.create_task(self.close())

    async def read_recepteur(self, id_recepteur=1):
        regs = await self.modbus.read_holding(0, 4)
        if regs is None:
            return None

        def signed16(v): return v - 65536 if v > 32767 else v
        
        data = {
            "frequency_mhz": regs[0] / 100.0, "rssi_dbm": signed16(regs[1]),
            "snr_db": regs[2] / 10.0, "squelch": regs[3],
        }
        await asyncio.to_thread(self.model.save_recepteur, data, id_recepteur)
        await self._evaluate_alerts(data, id_recepteur)
        return data

    async def _evaluate_alerts(self, data, equipment_id=1):
        # RSSI
        if data["rssi_dbm"] <= self.thresholds["rssi_weak_dbm"]:
            self.sound.play("CRITICAL")
            await asyncio.to_thread(self.alert_model.save, {"equipment_type": "RECEPTEUR", "equipment_id": equipment_id, "type": "Signal faible", "severity": "CRITICAL"})
        # SNR
        if data["snr_db"] <= self.thresholds["snr_low_db"]:
            self.sound.play("CRITICAL")
            await asyncio.to_thread(self.alert_model.save, {"equipment_type": "RECEPTEUR", "equipment_id": equipment_id, "type": "Interférences (SNR bas)", "severity": "CRITICAL"})
        # Squelch
        sq = data.get("squelch", 0)
        if not (self.thresholds["squelch_expected_min"] <= sq <= self.thresholds["squelch_expected_max"]):
            self.sound.play("WARNING")
            await asyncio.to_thread(self.alert_model.save, {"equipment_type": "RECEPTEUR", "equipment_id": equipment_id, "type": "Squelch hors plage", "severity": "WARNING"})

    async def set_frequency(self, frequency_mhz):
        if not (118.0 <= frequency_mhz <= 144.0): return False, "Fréquence hors plage."
        ok = await self.modbus.write_register(0, int(frequency_mhz * 100))
        return ok, None if ok else "Échec écriture Modbus."

    async def set_squelch(self, squelch_value: int):
        if not (0 <= squelch_value <= 50): return False, "Valeur de squelch hors plage."
        ok = await self.modbus.write_register(3, int(squelch_value))
        return ok, None if ok else "Échec écriture Modbus."

    async def close(self):
        if self.modbus:
            await self.modbus.close()
    # --- Fin de la copie ---


class ControllerThread(QThread):
    """Ce thread gère la boucle asyncio pour le contrôleur."""
    data_ready = Signal(dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = RecepteurController()
        self.loop = None

    def run(self):
        try:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
            self.loop.run_until_complete(self.controller.start_polling(self.data_ready.emit))
        except Exception as e:
            print(f"Erreur dans le thread du contrôleur: {e}")
        finally:
            if self.loop: self.loop.close()

    def stop(self):
        print("Arrêt du thread du contrôleur...")
        if self.controller: self.controller.stop_polling()
        if self.loop and self.loop.is_running(): self.loop.call_soon_threadsafe(self.loop.stop)
        self.quit()
        self.wait(2000)

# =============================================================================
# 3. FENÊTRE DE TEST PYSIDE6
# =============================================================================

class MatplotlibCanvas(FigureCanvas):
    """Widget Matplotlib pour l'intégration dans PySide6."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)

class TestWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Test Interface Récepteur")
        self.setGeometry(100, 100, 800, 600)

        # --- Données pour le graphique ---
        self.timestamps = deque(maxlen=50) # Garde les 50 dernières valeurs
        self.snr_values = deque(maxlen=50)

        # --- Création des widgets ---
        self.setup_ui()

        # --- Démarrage du contrôleur ---
        self.setup_controller_thread()

    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        # --- Colonne de Gauche: Données et Contrôles ---
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # -- Section 1: Données Techniques --
        tech_data_grid = QGridLayout()
        self.freq_label = self.create_data_label()
        self.rssi_label = self.create_data_label()
        self.snr_label = self.create_data_label()
        self.squelch_label = self.create_data_label()
        tech_data_grid.addWidget(QLabel("Fréquence:"), 0, 0)
        tech_data_grid.addWidget(self.freq_label, 0, 1)
        tech_data_grid.addWidget(QLabel("RSSI:"), 1, 0)
        tech_data_grid.addWidget(self.rssi_label, 1, 1)
        tech_data_grid.addWidget(QLabel("SNR:"), 2, 0)
        tech_data_grid.addWidget(self.snr_label, 2, 1)
        tech_data_grid.addWidget(QLabel("Squelch:"), 3, 0)
        tech_data_grid.addWidget(self.squelch_label, 3, 1)

        # -- Section 2: Contrôles --
        self.freq_input = QLineEdit()
        self.freq_button = QPushButton("Changer Fréquence")
        self.squelch_input = QLineEdit()
        self.squelch_button = QPushButton("Changer Squelch")
        
        controls_layout = QGridLayout()
        controls_layout.addWidget(self.freq_input, 0, 0)
        controls_layout.addWidget(self.freq_button, 0, 1)
        controls_layout.addWidget(self.squelch_input, 1, 0)
        controls_layout.addWidget(self.squelch_button, 1, 1)
        
        left_layout.addLayout(tech_data_grid)
        left_layout.addSpacing(20)
        left_layout.addLayout(controls_layout)
        left_layout.addStretch()

        # --- Colonne de Droite: Graphique Matplotlib ---
        self.snr_plot = MatplotlibCanvas(self, width=6, height=5, dpi=100)
        
        main_layout.addWidget(left_panel, 1) # Poids de 1
        main_layout.addWidget(self.snr_plot, 2) # Poids de 2 (plus large)
        
        # --- Connexion des signaux ---
        self.freq_button.clicked.connect(self.handle_set_frequency)
        self.squelch_button.clicked.connect(self.handle_set_squelch)

    def create_data_label(self):
        label = QLabel("N/A")
        label.setFont(QFont("Arial", 14, QFont.Bold))
        label.setStyleSheet("color: #333;")
        return label

    def setup_controller_thread(self):
        self.controller_thread = ControllerThread(self)
        self.controller_thread.data_ready.connect(self.update_ui)
        self.controller_thread.start()
        print("Thread du contrôleur démarré.")

    @Slot(dict)
    def update_ui(self, data: dict):
        print(f"[UI] Données reçues: {data}")
        # --- Mise à jour des labels ---
        self.freq_label.setText(f"{data.get('frequency_mhz', 0):.2f} MHz")
        self.rssi_label.setText(f"{data.get('rssi_dbm', 0)} dBm")
        self.snr_label.setText(f"{data.get('snr_db', 0):.1f} dB")
        self.squelch_label.setText(f"{data.get('squelch', 0)}")
        
        # --- Mise à jour du graphique ---
        self.timestamps.append(datetime.datetime.now())
        self.snr_values.append(data.get('snr_db', 0))
        self.update_plot()

    def update_plot(self):
        self.snr_plot.axes.clear()
        self.snr_plot.axes.plot(self.timestamps, self.snr_values, marker='o', linestyle='-')
        
        # Formatage du graphique
        self.snr_plot.axes.set_title("Taux de Bruit (SNR) en Temps Réel")
        self.snr_plot.axes.set_ylabel("SNR (dB)")
        self.snr_plot.axes.grid(True)
        self.snr_plot.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        self.snr_plot.figure.autofmt_xdate()
        
        self.snr_plot.draw()

    def handle_set_frequency(self):
        try:
            freq = float(self.freq_input.text())
            reply = QMessageBox.question(self, "Confirmation", f"Changer la fréquence pour {freq:.2f} MHz ?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                future = asyncio.run_coroutine_threadsafe(
                    self.controller_thread.controller.set_frequency(freq),
                    self.controller_thread.loop)
                future.add_done_callback(self.on_command_result)
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer une fréquence valide.")
            
    def handle_set_squelch(self):
        try:
            sq = int(self.squelch_input.text())
            reply = QMessageBox.question(self, "Confirmation", f"Changer le squelch pour {sq} ?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                future = asyncio.run_coroutine_threadsafe(
                    self.controller_thread.controller.set_squelch(sq),
                    self.controller_thread.loop)
                future.add_done_callback(self.on_command_result)
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer une valeur de squelch valide.")

    def on_command_result(self, future):
        """Callback qui affiche le résultat d'une commande envoyée au contrôleur."""
        try:
            ok, err_msg = future.result()
            if not ok:
                QMessageBox.critical(self, "Échec de la Commande", err_msg)
            else:
                print("[UI] Commande exécutée avec succès.")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Une erreur est survenue: {e}")

    def closeEvent(self, event):
        print("Fermeture de l'application...")
        self.controller_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())
