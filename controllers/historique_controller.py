import asyncio
import datetime
import os
from models.historique_model import HistoriqueModel
from services.export_service import ExportService

class HistoriqueController:
    def __init__(self):
        self.model = HistoriqueModel()

    def get_events(self, start_date=None, end_date=None, event_type=None, equipment_type=None, limit=500):
        """
        Parameters can be date strings 'YYYY-MM-DD' or datetime.date objects.
        """
        return self.model.get_events(start_date, end_date, event_type, equipment_type, limit)

    def get_trend_series(self, year: int = None):
        """
        Return monthly counts for given year. If year None, use current year.
        Returns list of 12 integers (Jan..Dec).
        """
        year = year or datetime.datetime.now().year
        rows = self.model.count_by_month(year)
        # build map month->count
        month_map = {r["month"]: r["count"] for r in rows}
        return [month_map.get(m, 0) for m in range(1,13)]

    def _build_output_path(self, base_dir: str, base_name: str, ext: str) -> str:
        """
        Construit un chemin unique avec horodatage : ex. rapport_evenements_2025-09-09_12-34-56.pdf
        """
        os.makedirs(base_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return os.path.join(base_dir, f"{base_name}_{timestamp}{ext}")

    async def export_pdf(self, events, **kwargs):
        """
        Exporte les événements en PDF avec horodatage unique.
        kwargs -> options passées à ExportService.export_pdf
        """
        output_path = self._build_output_path("export/pdf", "rapport_evenements", ".pdf")
        return await asyncio.to_thread(
            ExportService.export_pdf, events, output_path, **kwargs
        )

    async def export_excel(self, events):
        """
        Exporte les événements en Excel avec horodatage unique.
        """
        output_path = self._build_output_path("export/excel", "rapport_evenements", ".xlsx")
        return await asyncio.to_thread(
            ExportService.export_excel, events, output_path
        )
