import inspect
import asyncio
import datetime

from PySide6.QtCore import QCoreApplication, QThread, QTimer, Signal, Slot, QObject, Qt, QRect
from PySide6.QtGui import QPixmap, QColor, QPalette, QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QStyledItemDelegate, QStyle
from views.basculeur.ui_basculeur import Ui_MainWindow
from controllers.basculeur_controller import BasculeurController

class Basculeur_Screen(QMainWindow):
    # Signal pour recevoir les données du thread du contrôleur de manière sécurisée
    data_signal = Signal(dict)

    def __init__(self, user_id: int = None, parent=None, duration: int = 2000):
        super().__init__(parent)

        self.duration = duration

        self.user_id = user_id

        # Create an instance of the controller
        self.controller = BasculeurController()

        # --- Données d'état ---
        self.current_state = {}

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Démarrage du contrôleur ---
        self.setup_controller()

        # --- APPLICATION DU DÉLÉGUÉ ---
        pill_delegate = PillDelegate(self.ui.tableWidget)
        self.ui.tableWidget.setItemDelegateForColumn(1, pill_delegate)

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()

        # --- Connexion des signaux des boutons ---
        self.ui.btnManuel.clicked.connect(self.handle_manual_switch)
        self.ui.btnConfigurer.clicked.connect(self.handle_set_auto)

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
        """Ce slot est appelé à chaque fois que le contrôleur envoie de nouvelles données."""
        print(f"[UI] Données reçues: {data}")
        self.current_state = data
        
        # --- Mise à jour de l'état (Principal/Secours) ---
        active_path = data.get("active_path", "INCONNU")
        self.ui.label_2.setText(active_path)
        color = "#28a745" if active_path == "PRINCIPAL" else "#1570D1" # Vert ou Rouge
        self.ui.label_2.setStyleSheet(f"font-family: Open Sans; font-size: 20px; font-weight: 700; color: {color};")

        # Mise à jour du message d'alerte et de son style
        alert_data = data.get("alert_data", ("INFO", "Aucun message."))
        severity, message, sous_message = alert_data
        self.show_alert(message, sous_message, severity)
        
        # --- Mise à jour du texte du bouton Auto ---
        auto_enabled = data.get("auto_enabled", False)

        # --- Mise à jour de l'historique ---
        self.refresh_history_table()

    def run_blocking_task(self, task_function, *args, callback=None):
        """Exécute une fonction bloquante dans un thread séparé pour ne pas geler l'UI."""
        self.thread = QThread()
        self.worker = Worker(task_function, *args)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        if callback:
            self.worker.finished.connect(callback)
        else:
            self.worker.finished.connect(self.on_command_result)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

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
            self.run_blocking_task(self.controller.manual_switch_async, target_path)

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
            self.run_blocking_task(self.controller.set_auto, target_auto_state)
            # Exécute la coroutine sur la boucle asyncio du thread du contrôleur

    def refresh_history_table(self):
        """Demande l'historique au contrôleur et met à jour le tableau."""
        # lance la récupération en arrière-plan et connecte le résultat à populate_history_table
        self.run_blocking_task(self.controller.get_history, 50, callback=self.populate_history_table)

    def populate_history_table(self, result):
        """Callback pour remplir le tableau une fois les données d'historique reçues.

        Accepts either:
        - a list already (emitted by Worker), or
        - a future-like object with .result()
        """
        try:
            # Accepter soit un future-like, soit la liste directement
            if hasattr(result, "result") and callable(result.result):
                history_data = result.result()
            else:
                history_data = result

            if history_data is None:
                history_data = []

            # S'assurer que c'est une liste
            if not isinstance(history_data, list):
                try:
                    history_data = list(history_data)
                except Exception:
                    # fallback : encapsuler en liste
                    history_data = [history_data]

            self.ui.tableWidget.setRowCount(len(history_data))
            for row, event in enumerate(history_data):
                # timestamp peut être datetime, str ou absent
                ts_val = event.get('timestamp', datetime.datetime.now())
                if isinstance(ts_val, str):
                    try:
                        ts = datetime.datetime.fromisoformat(ts_val)
                    except Exception:
                        ts = datetime.datetime.now()
                elif isinstance(ts_val, datetime.datetime):
                    ts = ts_val
                else:
                    # si c'est un nombre (timestamp) ou autre
                    try:
                        ts = datetime.datetime.fromtimestamp(float(ts_val))
                    except Exception:
                        ts = datetime.datetime.now()

                ts_str = ts.strftime('%Y-%m-%d %H:%M:%S')
                # --- normalisation et création de l'item pour la colonne "event_type" ---
                event_type_raw = event.get('event_type', 'N/A')

                desc = event.get('description', 'N/A')

                # Normaliser les libellés
                if event_type_raw == "Configuration bascule automatique":
                    event_text = "Automatique"
                elif event_type_raw == "Basculement manuel":
                    event_text = "Manuel"
                else:
                    event_text = str(event_type_raw)

                # Créer l'item de tableau
                item_event = QTableWidgetItem(event_text)

                # Insérer les items dans la table
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(ts_str))
                self.ui.tableWidget.setItem(row, 1, item_event)
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(desc))                
        except Exception as e:
            print(f"Erreur lors de la mise à jour du tableau d'historique: {e}")

    @Slot(object)
    def on_command_result(self, result):
        """
        result peut être :
        - un bool (True/False)
        - un tuple (ok, message, ...)
        - un autre objet (erreur ou info)
        Cette fonction normalise ça en ok, error_message.
        """
        try:
            if isinstance(result, tuple):
                ok = bool(result[0])
                error_message = result[1] if len(result) > 1 else None
            elif isinstance(result, bool):
                ok = result
                error_message = None
            elif result is None:
                ok = True
                error_message = None
            else:
                # tentative de désassemblage (fallback)
                try:
                    ok, error_message = result
                    ok = bool(ok)
                except Exception:
                    ok = False
                    error_message = str(result)
        except Exception as e:
            ok = False
            error_message = f"Erreur traitement résultat: {e}"

        if not ok:
            QMessageBox.critical(self, "Échec de la Commande", error_message or "Erreur inconnue")
        else:
            print("[UI] Commande exécutée avec succès.")

    def show_alert(self, text: str, sous_text: str, level="CRITICAL"):
        # Levels: CRITICAL (red), WARNING (gris), INFO (blue)
        if level == "CRITICAL":
            bg = "#991B1B"
            fg = "#FFFFFF"
            self.ui.iconAlertRed.setPixmap(QPixmap(u":/icons/icons/exclamation-circle.svg"))
        elif level == "WARNING":
            bg = "#f3f4f6"
            fg = "#C9534F"
            self.ui.iconAlertRed.setPixmap(QPixmap(u":/icons/icons/git-pull-request1.svg"))
        else:
            bg = "#5bc0de"
            fg = "#FFFFFF"
            self.ui.iconAlertRed.setPixmap(QPixmap(u":/icons/icons/circle-check.svg"))
            
        self.ui.alertRed.setStyleSheet(f"background-color: {bg}; border-radius: 10px; border: 1px solid {bg};")
        self.ui.alertRedTitle.setStyleSheet(f"font-family: Open Sans; font-size: 16px; font-weight: 500; color: {fg};")
        self.ui.alertRedBody.setStyleSheet(f"font-family: Open Sans; font-size: 14px; font-weight: 400; color: {fg};")
        # self.ui.iconAlertRed.setStyleSheet(f"background-color: {fg};")

        self.ui.alertRedTitle.setText(QCoreApplication.translate("MainWindow", text, None))
        self.ui.alertRedBody.setText(QCoreApplication.translate("MainWindow", sous_text, None))

        self.ui.alertRed.setVisible(True)
        QTimer.singleShot(self.duration, self.clear_alert)

    def clear_alert(self):
        self.ui.alertRed.setVisible(False)
        self.ui.alertRedTitle.setText("")
        self.ui.alertRedBody.setText("")

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
        try:
            # si la fonction est une coroutine, l'exécuter proprement dans ce thread
            if inspect.iscoroutinefunction(self.func):
                result = asyncio.run(self.func(*self.args, **self.kwargs))
            else:
                result = self.func(*self.args, **self.kwargs)
        except Exception as e:
            # standardiser le retour en cas d'erreur
            result = (False, str(e))
        # émettre le résultat (ex: (ok, message) ou autre)
        self.finished.emit(result)

class PillDelegate(QStyledItemDelegate):
    """
    Ce délégué dessine un fond en forme de pilule colorée
    avec des coins arrondis uniquement derrière le texte de la cellule.
    """
    def paint(self, painter: QPainter, option, index):
        # Étape 1: Récupérer les données et le texte de la cellule
        text = index.data(Qt.DisplayRole)
        
        # Sauvegarder l'état du painter pour ne pas affecter les autres cellules
        painter.save()

        # Étape 2: Dessiner le fond de la cellule (par exemple pour la sélection)
        # On dessine d'abord l'arrière-plan par défaut de la cellule.
        # Si la cellule est sélectionnée, elle sera surlignée en bleu.
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        # Étape 3: Définir les couleurs en fonction du contenu du texte
        if text == "Défaillance":
            pill_color = QColor("#dc3545") # Rouge
            text_color = QColor("white")
        elif text == "Automatique":
            pill_color = QColor("#E0E0E0") # Gris
            text_color = QColor("black")
        elif text == "Manuel":
            pill_color = QColor("#E0E0E0") # Gris
            text_color = QColor("black")
        elif text == "Anomalie":
            pill_color = QColor("#FAAD14") # Orange
            text_color = QColor("white")
        else:
            # Style par défaut pour les autres textes
            # On dessine simplement le texte sans fond coloré
            painter.restore()
            super().paint(painter, option, index) # On laisse le parent dessiner
            return

        # Étape 4: Calculer le rectangle qui entoure le texte
        # C'est la clé pour que le fond ne prenne pas toute la cellule.
        text_rect = painter.fontMetrics().boundingRect(option.rect, Qt.AlignCenter, text)

        # Étape 5: Ajouter un "padding" pour que la pilule soit plus large que le texte
        # On ajuste le rectangle pour qu'il soit plus grand de 8 pixels en largeur et 4 en hauteur
        pill_rect = text_rect.adjusted(-8, -4, 8, 4)

        # Étape 6: Dessiner la "pilule" (le rectangle arrondi)
        painter.setBrush(pill_color)
        border_pen = QPen(pill_color, 2)
        painter.setPen(border_pen) # Pas de bordure autour de la pilule
        
        # Le border-radius est défini ici (ex: 10)
        border_radius = pill_rect.height() / 2
        painter.drawRoundedRect(pill_rect, border_radius, border_radius)

        # Étape 7: Dessiner le texte par-dessus la pilule
        painter.setPen(text_color)
        # On utilise option.rect pour que le texte reste bien centré dans la cellule
        painter.drawText(option.rect, Qt.AlignCenter, text)

        # Restaurer l'état du painter
        painter.restore()
