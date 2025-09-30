import sys
import asyncio
import datetime
import os
import time
import random
from typing import Callable

# --- Dépendances à installer: pip install PySide6 matplotlib ---
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QComboBox, QDateEdit, QTableWidget, QTableWidgetItem,
    QHeaderView, QMessageBox, QTextEdit
)
from PySide6.QtCore import QThread, Signal, Slot, QObject, QDate, Qt

# Intégration de Matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# =============================================================================
# 1. CLASSES MOCK (SIMULATIONS DE VOS SERVICES ET MODÈLES)
# =============================================================================

class MockHistoriqueModel:
    """Simule la base de données de l'historique avec des données générées."""
    def __init__(self):
        self.events = self._generate_sample_data()

    def _generate_sample_data(self):
        data = []
        now = datetime.datetime.now()
        event_types = ["Défaillance", "Anomalie", "Retour service", "Configuration"]
        equip_types = ["EMETTEUR", "RECEPTEUR", "BASCULEUR"]
        severities = ["CRITICAL", "WARNING", "INFO"]
        
        for i in range(300):
            # Génère des événements sur les 6 derniers mois
            event_date = now - datetime.timedelta(days=random.randint(0, 180))
            data.append({
                "timestamp": event_date,
                "equipment_type": random.choice(equip_types),
                "event_type": random.choice(event_types),
                "severity": random.choice(severities) if random.random() > 0.3 else "INFO",
                "description": f"Événement simulé #{i+1}"
            })
        return sorted(data, key=lambda x: x['timestamp'], reverse=True)

    def get_events(self, start_date=None, end_date=None, event_type=None, equipment_type=None, limit=500):
        print(f"[MockDB] Recherche: start={start_date}, end={end_date}, event={event_type}, equip={equipment_type}")
        
        # Convertir les dates si elles sont des chaînes
        if isinstance(start_date, str): start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        if isinstance(end_date, str): end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        
        filtered = self.events
        if start_date:
            filtered = [e for e in filtered if e['timestamp'].date() >= start_date]
        if end_date:
            filtered = [e for e in filtered if e['timestamp'].date() <= end_date]
        if event_type and event_type != "Tous":
            filtered = [e for e in filtered if e['event_type'] == event_type]
        if equipment_type and equipment_type != "Tous":
            filtered = [e for e in filtered if e['equipment_type'] == equipment_type]
            
        return filtered[:limit]

    def count_by_month(self, year):
        print(f"[MockDB] Comptage des événements par mois pour l'année {year}")
        counts = {m: 0 for m in range(1, 13)}
        for event in self.events:
            if event['timestamp'].year == year:
                counts[event['timestamp'].month] += 1
        
        return [{"month": m, "count": c} for m, c in counts.items()]

class MockExportService:
    """Simule la création de fichiers d'export."""
    @staticmethod
    def export_pdf(events, output_path, **kwargs):
        print(f"[MockExport] Création d'un PDF avec {len(events)} événements vers '{output_path}'...")
        time.sleep(2) # Simule une tâche longue
        print("[MockExport] PDF créé.")
        return output_path

    @staticmethod
    def export_excel(events, output_path):
        print(f"[MockExport] Création d'un fichier Excel avec {len(events)} événements vers '{output_path}'...")
        time.sleep(1.5)
        print("[MockExport] Excel créé.")
        return output_path

# =============================================================================
# 2. VOTRE CLASSE HISTORIQUECONTROLLER (ADAPTÉE POUR LES MOCKS)
# =============================================================================
class HistoriqueController:
    # --- Votre code est collé ici, adapté pour utiliser les Mocks ---
    def __init__(self):
        self.model = MockHistoriqueModel()

    def get_events(self, start_date=None, end_date=None, event_type=None, equipment_type=None, limit=500):
        return self.model.get_events(start_date, end_date, event_type, equipment_type, limit)

    def get_trend_series(self, year: int = None):
        year = year or datetime.datetime.now().year
        rows = self.model.count_by_month(year)
        month_map = {r["month"]: r["count"] for r in rows}
        return [month_map.get(m, 0) for m in range(1, 13)]

    def _build_output_path(self, base_dir: str, base_name: str, ext: str) -> str:
        os.makedirs(base_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return os.path.join(base_dir, f"{base_name}_{timestamp}{ext}")

    async def export_pdf(self, events, **kwargs):
        output_path = self._build_output_path("export/pdf", "rapport_evenements", ".pdf")
        return await asyncio.to_thread(MockExportService.export_pdf, events, output_path, **kwargs)

    async def export_excel(self, events):
        output_path = self._build_output_path("export/excel", "rapport_evenements", ".xlsx")
        return await asyncio.to_thread(MockExportService.export_excel, events, output_path)

# =============================================================================
# 3. WORKER POUR TÂCHES ASYNCHRONES
# =============================================================================
class AsyncWorker(QObject):
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

# =============================================================================
# 4. FENÊTRE DE TEST PYSIDE6
# =============================================================================
class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(10, 3), dpi=100)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class TestWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Test Interface Historique")
        self.setGeometry(50, 50, 1200, 800)
        self.controller = HistoriqueController()
        self.current_events = [] # Garde en mémoire les événements affichés
        self.setup_ui()
        self.connect_signals()
        self.apply_filters() # Premier chargement avec les valeurs par défaut

    def setup_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # --- Ligne 1: Filtres et Exports ---
        top_layout = QHBoxLayout()
        # Filtres
        self.start_date_edit = QDateEdit(calendarPopup=True)
        self.end_date_edit = QDateEdit(calendarPopup=True)
        self.event_type_combo = QComboBox()
        self.equip_type_combo = QComboBox()
        self.apply_btn = QPushButton("Appliquer")
        
        # Initialisation des filtres
        self.start_date_edit.setDate(QDate.currentDate().addMonths(-1))
        self.end_date_edit.setDate(QDate.currentDate())
        self.event_type_combo.addItems(["Tous", "Défaillance", "Anomalie", "Retour service", "Configuration"])
        self.equip_type_combo.addItems(["Tous", "EMETTEUR", "RECEPTEUR", "BASCULEUR"])
        
        filter_group = QHBoxLayout()
        filter_group.addWidget(QLabel("Période:"))
        filter_group.addWidget(self.start_date_edit)
        filter_group.addWidget(QLabel("à"))
        filter_group.addWidget(self.end_date_edit)
        filter_group.addWidget(QLabel("Type d'événement:"))
        filter_group.addWidget(self.event_type_combo)
        filter_group.addWidget(QLabel("Équipement:"))
        filter_group.addWidget(self.equip_type_combo)
        filter_group.addWidget(self.apply_btn)
        
        # Exports
        self.export_pdf_btn = QPushButton("Exporter en PDF")
        self.export_excel_btn = QPushButton("Exporter en Excel")

        top_layout.addLayout(filter_group)
        top_layout.addStretch()
        top_layout.addWidget(self.export_pdf_btn)
        top_layout.addWidget(self.export_excel_btn)
        
        # --- Ligne 2: Graphique d'Évolution ---
        self.chart = MatplotlibCanvas()
        
        # --- Ligne 3: Tableau de Détails et Analyse IA ---
        bottom_layout = QHBoxLayout()
        # Tableau
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Date", "Heure", "Équipement", "Type", "Gravité"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # Analyse IA
        ia_panel = QVBoxLayout()
        ia_label = QLabel("<h3>Analyse IA: Tendances et Prédictions</h3>")
        self.ia_text = QTextEdit()
        self.ia_text.setReadOnly(True)
        ia_panel.addWidget(ia_label)
        ia_panel.addWidget(self.ia_text)
        
        bottom_layout.addWidget(self.table, 3) # Le tableau prend 3/4 de la place
        bottom_layout.addLayout(ia_panel, 1) # L'analyse prend 1/4

        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.chart)
        main_layout.addLayout(bottom_layout)

    def connect_signals(self):
        self.apply_btn.clicked.connect(self.apply_filters)
        self.export_pdf_btn.clicked.connect(self.handle_export_pdf)
        self.export_excel_btn.clicked.connect(self.handle_export_excel)

    @Slot()
    def apply_filters(self):
        """Récupère les données via le contrôleur et met à jour toute l'interface."""
        start_date = self.start_date_edit.date().toPython()
        end_date = self.end_date_edit.date().toPython()
        event_type = self.event_type_combo.currentText()
        equip_type = self.equip_type_combo.currentText()
        
        # Les fonctions du contrôleur sont synchrones, pas besoin de thread ici
        self.current_events = self.controller.get_events(start_date, end_date, event_type, equip_type)
        trend_data = self.controller.get_trend_series(QDate.currentDate().year())
        
        self.update_table(self.current_events)
        self.update_chart(trend_data)
        self.update_ai_analysis(self.current_events)

    def update_table(self, events):
        self.table.setRowCount(len(events))
        for row, event in enumerate(events):
            self.table.setItem(row, 0, QTableWidgetItem(event['timestamp'].strftime('%Y-%m-%d')))
            self.table.setItem(row, 1, QTableWidgetItem(event['timestamp'].strftime('%H:%M:%S')))
            self.table.setItem(row, 2, QTableWidgetItem(event['equipment_type']))
            self.table.setItem(row, 3, QTableWidgetItem(event['event_type']))
            self.table.setItem(row, 4, QTableWidgetItem(event['severity']))
    
    def update_chart(self, trend_data):
        self.chart.axes.clear()
        months = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Aoû", "Sep", "Oct", "Nov", "Déc"]
        self.chart.axes.bar(months, trend_data, color='blue', label='Événements')
        self.chart.axes.set_title("Évolution Historique des Événements")
        self.chart.axes.set_ylabel("Nombre d'événements")
        self.chart.axes.legend()
        self.chart.axes.grid(axis='y', linestyle='--', alpha=0.7)
        self.chart.draw()
        
    def update_ai_analysis(self, events):
        if not events:
            self.ia_text.setText("Aucune donnée à analyser pour la période sélectionnée.")
            return

        critical_count = sum(1 for e in events if e['severity'] == 'CRITICAL')
        equip_counter = {}
        for e in events:
            equip_counter[e['equipment_type']] = equip_counter.get(e['equipment_type'], 0) + 1
        
        most_problematic_equip = "N/A"
        if equip_counter:
            most_problematic_equip = max(equip_counter, key=equip_counter.get)

        analysis = (
            f"<b>Synthèse de la période :</b><br>"
            f"Un total de <b>{len(events)}</b> événements ont été enregistrés.<br>"
            f"Dont <b>{critical_count}</b> événements critiques nécessitant une attention immédiate.<br><br>"
            f"<b>Équipement le plus affecté :</b><br>"
            f"L'équipement <b>{most_problematic_equip}</b> a généré le plus d'événements ({equip_counter.get(most_problematic_equip, 0)}). "
            f"Une maintenance préventive est recommandée.<br><br>"
            f"<b>Tendance et Prédiction :</b><br>"
            f"Le volume d'événements critiques semble indiquer une usure potentielle des composants. "
            f"Il est prédit une augmentation de 15% des alertes de type 'Défaillance' le mois prochain si aucune action n'est prise."
        )
        self.ia_text.setHtml(analysis)

    def run_async_task(self, coro, *args, **kwargs):
        """Lance une coroutine dans un thread de travail."""
        self.thread = QThread()
        self.worker = AsyncWorker(coro, *args, **kwargs)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_export_finished)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        # Désactiver les boutons pendant l'export
        self.export_pdf_btn.setEnabled(False)
        self.export_excel_btn.setEnabled(False)

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
        self.export_pdf_btn.setEnabled(True)
        self.export_excel_btn.setEnabled(True)
        
        if isinstance(result, Exception):
            QMessageBox.critical(self, "Erreur d'Exportation", f"Une erreur est survenue: {result}")
        else:
            QMessageBox.information(self, "Exportation Réussie", f"Le rapport a été sauvegardé avec succès dans:\n{result}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())
