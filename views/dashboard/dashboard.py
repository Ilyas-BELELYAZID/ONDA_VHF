import datetime
from collections import deque

from PySide6.QtCore import QCoreApplication, Slot, Qt
from PySide6.QtGui import QPixmap, QColor, QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QStyledItemDelegate, QStyle
from views.dashboard.ui_dashboard import Ui_MainWindow
from controllers.dashboard_controller import DashboardController

# Intégration de Matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates

class Dashboard_Screen(QMainWindow):
    def __init__(self, user_id: int = None):
        super().__init__()

        self.user_id = user_id

        # Create an instance of the controller
        self.controller = DashboardController()

        # Données pour les graphiques
        self.temp_timestamps = deque(maxlen=288) # 24h * 12 (5 min par point)
        self.temp_values = deque(maxlen=288)

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Les données de graphique
        self.temp_chart = MatplotlibCanvas()
        self.ui.verticalLayout_8.addWidget(self.temp_chart)

        # --- APPLICATION DU DÉLÉGUÉ ---
        pill_delegate = PillDelegate(self.ui.tableWidget)
        border_delegate = BorderPillDelegate(self.ui.tableWidget)

        self.ui.tableWidget.setItemDelegateForColumn(3, pill_delegate)
        self.ui.tableWidget.setItemDelegateForColumn(4, border_delegate)

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()

        # --- Démarrage du contrôleur ---
        self.controller.update.connect(self.update_ui)
        self.controller.start()
        print("Contrôleur démarré.")

    @Slot(object)
    def update_ui(self, summary: dict):
        # --- Mise à jour de la vue d'ensemble ---
        state = summary.get('system_state', 'Inconnu')
        if state == "Dégradé":
            self.ui.label_19.setPixmap(QPixmap(u":/icons/icons/shield-exclamation.svg"))
            fg = "#FAAD14"
            desc = "Fonctionnement dégradé — certaines\nfonctionnalités peuvent être limitées."
        elif state == "Erreur":
            self.ui.label_19.setPixmap(QPixmap(u":/icons/icons/shield-x.svg"))
            fg = "#DC3848"
            desc = "Erreur critique détectée — intervention\nrequise immédiatement."
        else:
            self.ui.label_19.setPixmap(QPixmap(u":/icons/icons/shield-check.svg"))
            fg = "#171A1F"
            desc = "Tous les systèmes fonctionnent\nnormalement."

        self.ui.label_3.setStyleSheet(f"color: {fg}; font-family: Roboto; font-size: 36px; font-weight: 700;")
        self.ui.label_19.setStyleSheet(u"padding-top: 5px;")

        self.ui.label_3.setText(state)
        self.ui.label_4.setText(desc)
        self.ui.label_6.setText(str(summary.get('equipment_count', 3)))
        
        alerts = summary.get('recent_alerts', [])
        open_alerts = [a for a in alerts if a.get('resolved') == 0]
        self.ui.label_9.setText(str(len(open_alerts)))
        # --- Remplacer l'appel direct par ce bloc robuste ---
        last_update = summary.get('last_update')

        # Gérer plusieurs formats possibles
        if isinstance(last_update, datetime.datetime):
            time_str = last_update.strftime('%Y-%m-%d\n%H:%M:%S')
        elif isinstance(last_update, str):
            # essayer isoformat d'abord, sinon tomber back sur split
            try:
                time_str = datetime.datetime.fromisoformat(last_update).strftime('%Y-%m-%d\n%H:%M:%S')
            except Exception:
                parts = last_update.split()
                time_str = parts[1] if len(parts) > 1 else last_update
        else:
            time_str = 'N/A'

        self.ui.label_12.setText(time_str)

        # --- Mise à jour des graphiques ---
        device_data = summary['devices'][0] if summary['devices'] else {}
        if device_data.get('online', False):
            self.update_temp_chart(summary['timestamp'], device_data['temperature_c'])
            self.ui.gaugeLabel.setText(f"{device_data.get('power_pct', 0):.1F} W")

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
        
        ax.set_ylabel("°C")
        ax.grid(axis='y', linestyle='--', alpha=0.3)
        ax.legend()
        self.temp_chart.draw()

    def update_alerts_table(self, alerts):
        self.ui.tableWidget.setRowCount(len(alerts))
        for row, alert in enumerate(alerts):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(alert['timestamp'].strftime('%Y-%m-%d %H:%M')))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(alert['equipment_type']))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(alert['type']))
            if alert['severity'] == "CRITICAL":
                status = "Critique"
                gravite = "Haute"
            elif alert['severity'] == "WARNING":
                status = "En cours"
                gravite = "Moyenne"
            elif alert['severity'] == "INFO":
                status = "Résolue"
                gravite = "Faible"
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(status))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(gravite))

    def closeEvent(self, event):
        print("Fermeture de l'application...")
        self.controller.stop()
        self.controller.wait(2000) # Attendre que le thread se termine
        event.accept()

        

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

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
        if text == "Critique":
            pill_color = QColor("#dc3545") # Rouge
        elif text == "En cours":
            pill_color = QColor("#FAAD14") # Orange
        elif text == "Résolue":
            pill_color = QColor("#28a745") # Vert
            
        else:
            # Style par défaut pour les autres textes
            # On dessine simplement le texte sans fond coloré
            painter.restore()
            super().paint(painter, option, index) # On laisse le parent dessiner
            return

        text_color = QColor("white")
        # Étape 4: Calculer le rectangle qui entoure le texte
        # C'est la clé pour que le fond ne prenne pas toute la cellule.
        text_rect = painter.fontMetrics().boundingRect(option.rect, Qt.AlignCenter, text)

        # Étape 5: Ajouter un "padding" pour que la pilule soit plus large que le texte
        # On ajuste le rectangle pour qu'il soit plus grand de 8 pixels en largeur et 4 en hauteur
        pill_rect = text_rect.adjusted(-8, -4, 8, 4)

        # Étape 6: Dessiner la "pilule" (le rectangle arrondi)
        painter.setBrush(pill_color)
        border_pen = QPen(pill_color, 2)
        painter.setPen(border_pen)
        
        # Le border-radius est défini ici (ex: 10)
        border_radius = pill_rect.height() / 2
        painter.drawRoundedRect(pill_rect, border_radius, border_radius)

        # Étape 7: Dessiner le texte par-dessus la pilule
        painter.setPen(text_color)
        # On utilise option.rect pour que le texte reste bien centré dans la cellule
        painter.drawText(option.rect, Qt.AlignCenter, text)

        # Restaurer l'état du painter
        painter.restore()

class BorderPillDelegate(QStyledItemDelegate):
    """
    Ce délégué dessine une bordure arrondie et colorée autour du texte,
    tout en laissant le fond de la cellule transparent pour voir les
    couleurs alternées du tableau.
    """
    def paint(self, painter: QPainter, option, index):
        # Étape 1: Récupérer les données et sauvegarder l'état du painter
        text = index.data(Qt.DisplayRole)
        painter.save()

        # Étape 2: Gérer l'affichage de la sélection de la cellule
        # Si la cellule est sélectionnée, on dessine le fond de sélection bleu par défaut.
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())
            # On s'assure que le texte sera lisible sur le fond de sélection
            text_pen = QPen(option.palette.highlightedText())
        else:
            # Si non sélectionnée, on ne dessine aucun fond, ce qui le laisse transparent.
            text_pen = None # La couleur sera définie plus bas

        # Étape 3: Définir la couleur du contour et du texte en fonction du contenu
        if text == "Haute":
            outline_color = QColor("#dc3545") # Rouge
        elif text == "Moyenne":
            outline_color = QColor("#FAAD14") # Jaune foncé pour la lisibilité
        elif text == "Faible":
            outline_color = QColor("#28a745") # Vert
        else:
            # Pour tout autre texte, on laisse Qt dessiner la cellule par défaut
            painter.restore()
            super().paint(painter, option, index)
            return

        # Étape 4: Calculer le rectangle de la pilule (comme avant)
        text_rect = painter.fontMetrics().boundingRect(option.rect, Qt.AlignCenter, text)
        pill_rect = text_rect.adjusted(-8, -4, 8, 4)

        # Étape 5: Dessiner UNIQUEMENT la bordure de la pilule
        painter.setRenderHint(QPainter.Antialiasing) # Pour des bords plus lisses
        
        # --- C'EST LA PARTIE CLÉ ---
        # On ne veut pas de remplissage
        painter.setBrush(Qt.NoBrush) 
        # On définit un stylo avec notre couleur et une épaisseur de 1.5 pixels
        border_pen = QPen(outline_color, 1.5)
        painter.setPen(border_pen)
        
        border_radius = pill_rect.height() / 2
        painter.drawRoundedRect(pill_rect, border_radius, border_radius)

        # Étape 6: Dessiner le texte
        # Si l'item n'était pas sélectionné, on utilise la couleur du contour pour le texte
        if text_pen is None:
            text_pen = QPen(outline_color)
        
        painter.setPen(text_pen)
        painter.drawText(option.rect, Qt.AlignCenter, text)

        painter.restore()