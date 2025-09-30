import sys
import asyncio
import datetime
import time
from typing import Optional, List, Dict, Any

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHeaderView,
    QMessageBox
)
from PySide6.QtCore import QThread, Signal, Slot, Qt
from PySide6.QtGui import QFont, QColor

from services.alert_sound import AlertSoundManager
# =============================================================================
# 1. CLASSES MOCK (SIMULATIONS DE VOS SERVICES ET MODÈLES)
# =============================================================================

class MockModbusService:
    """Simule un client Modbus. Change d'état toutes les 15 secondes."""
    def __init__(self, device_id=3):
        print(f"[MockModbus] Initialisé pour l'appareil {device_id}.")
        self.regs = [0, 1, 1]  # [active_path, auto_enabled, cause_code]
        self.last_change_time = time.time()
        self.state_cycle = [
            # Normal -> Défaillance -> Manuel -> Retour Normal
            {'regs': [0, 1, 1], 'duration': 15},  # Principal, Auto, Cause: Auto
            {'regs': [1, 1, 2], 'duration': 10},  # Secours, Auto, Cause: Défaillance
            {'regs': [1, 0, 0], 'duration': 12},  # Secours, Manuel, Cause: Manuel
            {'regs': [0, 1, 1], 'duration': 15},  # Retour Principal
        ]
        self.current_state_index = 0

    async def connect(self):
        print("[MockModbus] Connexion simulée réussie.")
        await asyncio.sleep(0.1)
        return True

    async def read_holding(self, address, count):
        # Simule un changement d'état après une certaine durée
        current_state = self.state_cycle[self.current_state_index]
        if time.time() - self.last_change_time > current_state['duration']:
            self.current_state_index = (self.current_state_index + 1) % len(self.state_cycle)
            self.regs = self.state_cycle[self.current_state_index]['regs']
            self.last_change_time = time.time()
            print(f"[MockModbus] CHANGEMENT D'ÉTAT SIMULÉ -> {self.regs}")

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


class MockHistoriqueModel:
    def __init__(self):
        self.events = []
    def save_event(self, event_data: dict):
        print(f"[MockHistorique] Sauvegarde de l'événement: {event_data['description']}")
        event_data['timestamp'] = datetime.datetime.now()
        self.events.insert(0, event_data) # Ajoute au début
    def get_events(self, limit=50):
        print(f"[MockHistorique] Récupération des {limit} derniers événements.")
        return self.events[:limit]

class MockAlerteModel:
    def save(self, alert_data):
        print(f"[MockAlerte] Alerte '{alert_data['severity']}' sauvegardée: {alert_data['type']}")

class MockBasculeurModel:
    def save_basculeur(self, data, id_basculeur):
        print(f"[MockBasculeur] Sauvegarde de l'état pour basculeur {id_basculeur}.")

class MockAlertSoundManager:
    def play(self, sound_type: str):
        # REMARQUE: Ceci est une alerte NON-VISUELLE, comme demandé.
        # Elle s'affiche dans la console au lieu de bloquer l'UI avec une QMessageBox.
        print(f"🎵 [AlertSoundManager] JOUER SON: {sound_type} 🎵")

# =============================================================================
# 2. INTÉGRATION DU CONTRÔLEUR DANS UN QTHREAD
#    (Votre code de contrôleur va ici, légèrement adapté pour les mocks)
# =============================================================================

# Remplace les vraies classes par nos mocks pour le test
services = {
    'modbus_service': MockModbusService,
    'alert_sound': MockAlertSoundManager
}
models = {
    'basculeur_model': MockBasculeurModel,
    'alerte_model': MockAlerteModel,
    'historique_model': MockHistoriqueModel
}

# --- COLLEZ VOTRE CLASSE BasculeurController ICI ---
# J'ai recopié votre classe en l'adaptant pour utiliser les Mocks
# Assurez-vous que les imports pointent vers les classes Mock
class BasculeurController:
    # ... (Le code de votre BasculeurController est inséré ici) ...
    # J'ai fait les changements suivants :
    # self.modbus = services['modbus_service'](device_id=device_id)
    # self.histo = models['historique_model']()
    # etc. pour tous les modèles et services.
    # J'ai aussi corrigé une petite erreur dans manual_switch_async
    
    # --- Début de la copie adaptée de votre code ---
    def __init__(self, device_id: int = 3, poll_interval: float = 2.0): # Intervalle plus court pour le test
        self.modbus = services['modbus_service'](device_id=device_id)
        self.model = models['basculeur_model']()
        self.alert_model = models['alerte_model']()
        self.histo = models['historique_model']()
        self.sound = AlertSoundManager()
        self.poll_interval = poll_interval
        self._running = False
        self._last_path: Optional[str] = None
        self._last_cause_code: Optional[int] = None
        self.cause_map = {0: "Manuel", 1: "Automatique", 2: "Défaillance", 3: "Commande Externe"}

    async def start(self, data_callback=None):
        self._running = True
        connected = await self.modbus.connect()
        if not connected:
            print("⚠️ Modbus async connect failed")
        while self._running:
            try:
                data = await self.read_basculeur()
                if data and data_callback:
                    if asyncio.iscoroutinefunction(data_callback):
                        await data_callback(data)
                    else:
                        data_callback(data)
            except Exception as e:
                print("Polling async error:", e)
            await asyncio.sleep(self.poll_interval)

    def stop_polling(self):
        self._running = False
        try:
            asyncio.create_task(self.modbus.close())
        except Exception:
            pass

    async def read_basculeur(self, id_basculeur=1):
        regs = await self.modbus.read_holding(0, 3)
        if regs is None:
            return None
        try:
            active_code, auto_enabled_code, cause_code = int(regs[0]), int(regs[1]), int(regs[2])
            active_path = "PRINCIPAL" if active_code == 0 else "SECOURS"
            cause_str = self.cause_map.get(cause_code, f"CODE_{cause_code}")
            data = {
                "active_path": active_path, "auto_enabled": bool(auto_enabled_code),
                "cause_code": cause_code, "cause_basculement": cause_str,
                "last_switch": datetime.datetime.now()
            }
        except Exception as e:
            print("Decode basculeur regs error:", e)
            return None

        await asyncio.to_thread(self.model.save_basculeur, data, id_basculeur)
        
        # J'ajoute prev_cause pour le log de retour à la normale
        prev_cause = self._last_cause_code
        await self._evaluate_async(data, equipment_id=id_basculeur, prev_state=self._last_path, prev_cause=prev_cause)
        
        self._last_path = data["active_path"]
        self._last_cause_code = data["cause_code"]
        return data

    async def _evaluate_async(self, data: dict, equipment_id: int = 1, prev_state: Optional[str] = None, prev_cause: Optional[int] = None):
        active_path, auto_enabled = data["active_path"], data["auto_enabled"]
        cause_code, cause_label = data["cause_code"], data["cause_basculement"]
        now = datetime.datetime.now()
        is_new_transition = (prev_state != active_path)

        if active_path == "SECOURS" and (is_new_transition or cause_code == 2):
            severity = "CRITICAL" if cause_code == 2 else "WARNING"
            self.sound.play(severity)
            alert_type = "Défaillance canal principal" if cause_code == 2 else "Basculement non prévu"
            await asyncio.to_thread(self.alert_model.save, {
                "equipment_type": "BASCULEUR", "equipment_id": equipment_id, "type": alert_type,
                "severity": severity, "timestamp": now
            })
            await asyncio.to_thread(self.histo.save_event, {
                "event_type": alert_type, "description": f"Basculement vers secours (cause: {cause_label})",
                "equipment_type": "BASCULEUR"
            })
        elif active_path == "PRINCIPAL" and prev_state == "SECOURS":
            self.sound.play("INFO")
            prev_cause_label = self.cause_map.get(prev_cause, f"CODE_{prev_cause}")
            await asyncio.to_thread(self.histo.save_event, {
                "event_type": "Retour service", "description": f"Retour sur canal principal (cause précédente: {prev_cause_label})",
                "equipment_type": "BASCULEUR"
            })

    async def manual_switch_async(self, target: str):
        code = 0 if target.upper().startswith("P") else 1
        cause_code_manual = 0
        ok1 = await self.modbus.write_register(0, int(code))
        ok2 = await self.modbus.write_register(2, int(cause_code_manual))
        if ok1 and ok2:
            await asyncio.to_thread(self.histo.save_event, {
                "event_type": "Basculement manuel", "description": f"Commande manuelle vers {target}",
                "equipment_type": "BASCULEUR"
            })
            return True, None
        return False, "Échec écriture Modbus (manual_switch)."

    async def set_auto(self, enable: bool):
        val = 1 if enable else 0
        ok = await self.modbus.write_register(1, int(val))
        if ok:
            await asyncio.to_thread(self.histo.save_event, {
                "event_type": "Configuration", "description": f"Bascule automatique {'activée' if enable else 'désactivée'}",
                "equipment_type": "BASCULEUR"
            })
            return True, None
        return False, "Échec écriture Modbus (set_auto)."
    
    async def get_history(self, limit=50):
        return await asyncio.to_thread(self.histo.get_events, limit=limit)
    # --- Fin de la copie ---


class ControllerThread(QThread):
    """Ce thread gère la boucle asyncio pour le contrôleur."""
    data_ready = Signal(dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = BasculeurController()
        self.loop = None

    def run(self):
        try:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
            self.loop.run_until_complete(self.controller.start(self.data_ready.emit))
        except Exception as e:
            print(f"Erreur dans le thread du contrôleur: {e}")
        finally:
            if self.loop:
                self.loop.close()

    def stop(self):
        print("Arrêt du thread du contrôleur...")
        self.controller.stop_polling()
        if self.loop and self.loop.is_running():
            self.loop.call_soon_threadsafe(self.loop.stop)
        self.quit()
        self.wait(2000)

# =============================================================================
# 3. FENÊTRE DE TEST PYSIDE6
# =============================================================================

class TestWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Test Interface Basculeur")
        self.setGeometry(100, 100, 700, 500)

        # --- Données d'état ---
        self.current_state = {}

        # --- Création des widgets ---
        self.setup_ui()

        # --- Démarrage du contrôleur en arrière-plan ---
        self.setup_controller_thread()

    def setup_ui(self):
        """Crée et organise tous les widgets de l'interface."""
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        # -- Section 1: État Actuel --
        status_layout = QHBoxLayout()
        status_label_title = QLabel("Équipement Actif:")
        self.status_label_value = QLabel("EN ATTENTE...")
        self.status_label_value.setFont(QFont("Arial", 24, QFont.Bold))
        status_layout.addWidget(status_label_title)
        status_layout.addWidget(self.status_label_value)
        status_layout.addStretch()

        # -- Section 2: Boutons d'Action --
        buttons_layout = QHBoxLayout()
        self.manual_switch_btn = QPushButton("Basculer Manuellement")
        self.auto_switch_btn = QPushButton("Activer/Désactiver Auto")
        buttons_layout.addWidget(self.manual_switch_btn)
        buttons_layout.addWidget(self.auto_switch_btn)

        # -- Section 3: Tableau d'Historique --
        history_label = QLabel("Historique des Basculements")
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(3)
        self.history_table.setHorizontalHeaderLabels(["Horodatage", "Événement", "Description"])
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.history_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # -- Ajout des sections au layout principal --
        main_layout.addLayout(status_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(history_label)
        main_layout.addWidget(self.history_table)
        
        # --- Connexion des signaux des boutons ---
        self.manual_switch_btn.clicked.connect(self.handle_manual_switch)
        self.auto_switch_btn.clicked.connect(self.handle_set_auto)

    def setup_controller_thread(self):
        """Initialise et démarre le thread qui exécute le contrôleur."""
        self.controller_thread = ControllerThread(self)
        # Le signal 'data_ready' du thread est connecté au slot 'update_ui' de la fenêtre
        self.controller_thread.data_ready.connect(self.update_ui)
        self.controller_thread.start()
        print("Thread du contrôleur démarré.")

    @Slot(dict)
    def update_ui(self, data: dict):
        """Ce slot est appelé à chaque fois que le contrôleur envoie de nouvelles données."""
        print(f"[UI] Données reçues: {data}")
        self.current_state = data
        
        # --- Mise à jour de l'état (Principal/Secours) ---
        active_path = data.get("active_path", "INCONNU")
        self.status_label_value.setText(active_path)
        color = "#28a745" if active_path == "PRINCIPAL" else "#dc3545" # Vert ou Rouge
        self.status_label_value.setStyleSheet(f"color: {color};")
        
        # --- Mise à jour du texte du bouton Auto ---
        auto_enabled = data.get("auto_enabled", False)
        self.auto_switch_btn.setText(f"Désactiver le Mode Auto" if auto_enabled else "Activer le Mode Auto")

        # --- Mise à jour de l'historique ---
        self.refresh_history_table()

    def handle_manual_switch(self):
        """Gère le clic sur le bouton de basculement manuel."""
        if not self.current_state:
            return
            
        current_path = self.current_state.get("active_path")
        target_path = "SECOURS" if current_path == "PRINCIPAL" else "PRINCIPAL"
        
        reply = QMessageBox.question(self, "Confirmation", 
            f"Êtes-vous sûr de vouloir basculer manuellement vers l'équipement {target_path} ?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
        if reply == QMessageBox.Yes:
            print(f"[UI] Commande de basculement manuel vers {target_path}...")
            # Exécute la coroutine sur la boucle asyncio du thread du contrôleur
            asyncio.run_coroutine_threadsafe(
                self.controller_thread.controller.manual_switch_async(target_path),
                self.controller_thread.loop
            )

    def handle_set_auto(self):
        """Gère le clic sur le bouton de configuration auto."""
        if not self.current_state:
            return
            
        current_auto_state = self.current_state.get("auto_enabled", False)
        target_auto_state = not current_auto_state
        action_text = "activer" if target_auto_state else "désactiver"

        reply = QMessageBox.question(self, "Confirmation",
            f"Êtes-vous sûr de vouloir {action_text} le mode de bascule automatique ?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            print(f"[UI] Commande pour {action_text} le mode auto...")
            # Exécute la coroutine sur la boucle asyncio du thread du contrôleur
            asyncio.run_coroutine_threadsafe(
                self.controller_thread.controller.set_auto(target_auto_state),
                self.controller_thread.loop
            )

    def refresh_history_table(self):
        """Demande l'historique au contrôleur et met à jour le tableau."""
        if self.controller_thread and self.controller_thread.loop:
            # On demande les données de manière asynchrone
            future = asyncio.run_coroutine_threadsafe(
                self.controller_thread.controller.get_history(50),
                self.controller_thread.loop
            )
            # On ajoute un callback qui s'exécutera quand les données seront prêtes
            future.add_done_callback(self.populate_history_table)

    def populate_history_table(self, future_result):
        """Callback pour remplir le tableau une fois les données d'historique reçues."""
        try:
            history_data = future_result.result()
            self.history_table.setRowCount(len(history_data))
            for row, event in enumerate(history_data):
                ts = event.get('timestamp', datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
                event_type = event.get('event_type', 'N/A')
                desc = event.get('description', 'N/A')
                self.history_table.setItem(row, 0, QTableWidgetItem(ts))
                self.history_table.setItem(row, 1, QTableWidgetItem(event_type))
                self.history_table.setItem(row, 2, QTableWidgetItem(desc))
        except Exception as e:
            print(f"Erreur lors de la mise à jour du tableau d'historique: {e}")

    def closeEvent(self, event):
        """S'assure que le thread s'arrête proprement à la fermeture de la fenêtre."""
        print("Fermeture de l'application...")
        self.controller_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())
