import asyncio

from typing import Callable
from PySide6.QtCore import QCoreApplication, QThread, Signal, Slot, QObject, QDate, Qt
from PySide6.QtGui import QPixmap, QColor, QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QStyledItemDelegate, QStyle
from views.historique.ui_historique import Ui_MainWindow
from controllers.historique_controller import HistoriqueController

# Intégration de Matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class historique_Screen(QMainWindow):
    def __init__(self, user_id: int = None):
        super().__init__()

        self.user_id = user_id

        # Create an instance of the controller
        self.controller = HistoriqueController()

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Graphique d'Évolution ---
        self.chart = MatplotlibCanvas()

        self.ui.verticalLayout_6.addWidget(self.chart)

        # --- APPLICATION DU DÉLÉGUÉ ---
        pill_delegate = PillDelegate(self.ui.tableEvents)
        self.ui.tableEvents.setItemDelegateForColumn(4, pill_delegate)

        self.ui.tableEvents.resizeColumnsToContents()
        self.ui.tableEvents.resizeRowsToContents()

        self.current_events = [] # Garde en mémoire les événements affichés
        self.connect_signals()
        self.apply_filters() # Premier chargement avec les valeurs par défaut

    def connect_signals(self):
        self.ui.btnAppliquer.clicked.connect(self.apply_filters)
        self.ui.btnExportPDF.clicked.connect(self.handle_export_pdf)
        self.ui.btnExportExcel.clicked.connect(self.handle_export_excel)

    @Slot()
    def apply_filters(self):
        """Récupère les données via le contrôleur et met à jour toute l'interface."""
        start_date = self.ui.dateEdit.date().toPython()
        end_date = self.ui.dateEdit_2.date().toPython()
        event_type = self.ui.comboTypeEvent.currentText()
        equip_type = self.ui.comboEquipement.currentText()
        
        # Les fonctions du contrôleur sont synchrones, pas besoin de thread ici
        self.current_events = self.controller.get_events(start_date, end_date, event_type, equip_type, 500)
        trend_data = self.controller.get_trend_series(QDate.currentDate().year())
        
        self.update_table(self.current_events)
        self.update_chart(trend_data)

    def update_table(self, events):
        self.ui.tableEvents.setRowCount(len(events))
        for row, event in enumerate(events):
            # Normaliser les libellés
            if event['severity'] == "Moyenne":
                event_text = "Majeure"
            elif event['severity'] == "Faible":
                event_text = "Mineure"
            else:
                event_text = str(event['severity'])

            # Créer l'item de tableau
            item_event = QTableWidgetItem(event_text)

            self.ui.tableEvents.setItem(row, 0, QTableWidgetItem(event['timestamp'].strftime('%Y-%m-%d')))
            self.ui.tableEvents.setItem(row, 1, QTableWidgetItem(event['timestamp'].strftime('%H:%M')))
            self.ui.tableEvents.setItem(row, 2, QTableWidgetItem(event['equipment_type']))
            self.ui.tableEvents.setItem(row, 3, QTableWidgetItem(event['event_type']))
            self.ui.tableEvents.setItem(row, 4, QTableWidgetItem(item_event))
    
    def update_chart(self, trend_data):
        self.chart.axes.clear()
        months = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Aoû", "Sep", "Oct", "Nov", "Déc"]
        self.chart.axes.bar(months, trend_data, color='blue', label='Événements')
        self.chart.axes.legend()
        self.chart.axes.grid(axis='y', linestyle='--', alpha=0.3)
        self.chart.draw()

    def run_async_task(self, coro, *args, **kwargs):
        """Lance une coroutine dans un thread de travail."""
        self.thread = QThread()
        self.worker = Worker(coro, *args, **kwargs)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_export_finished)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        # Désactiver les boutons pendant l'export
        self.ui.btnExportPDF.setEnabled(False)
        self.ui.btnExportExcel.setEnabled(False)

    def handle_export_pdf(self):
        if not self.current_events:
            QMessageBox.warning(self, "Exportation impossible", "Aucun événement à exporter.")
            return
        self.run_async_task(self.controller.export_pdf, self.current_events)

    def handle_export_excel(self):
        if not self.current_events:
            QMessageBox.warning(self, "Exportation impossible", "Aucun événement à exporter.")
            return
        self.run_async_task(self.controller.export_excel, self.current_events)

    @Slot(object)
    def on_export_finished(self, result):
        # Réactiver les boutons
        self.ui.btnExportPDF.setEnabled(True)
        self.ui.btnExportExcel.setEnabled(True)
        
        if isinstance(result, Exception):
            QMessageBox.critical(self, "Erreur d'Exportation", f"Une erreur est survenue: {result}")
        else:
            QMessageBox.information(self, "Exportation Réussie", f"Le rapport a été sauvegardé avec succès dans:\n{result}")

        

# =============================================================================
# WORKER POUR TÂCHES ASYNCHRONES
# =============================================================================
class Worker(QObject):
    """Worker qui exécute une coroutine asyncio dans un thread séparé."""
    finished = Signal(object)
    def __init__(self, coro: Callable, *args, **kwargs):
        super().__init__()
        self.coro = coro
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(self.coro(*self.args, **self.kwargs))
            self.finished.emit(result)
        except Exception as e:
            self.finished.emit(e)

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(10, 3), dpi=100)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

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
        if text == "Haute":
            pill_color = QColor("#dc3545") # Rouge
            text_color = QColor("white")
        elif text == "Critique":
            pill_color = QColor("#dc3545") # Rouge
            text_color = QColor("white")
        elif text == "Majeure":
            pill_color = QColor("#faad14") # Orange
            text_color = QColor("white")
        elif text == "Mineure":
            pill_color = QColor("#E0E0E0") # Gris
            text_color = QColor("black")
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
