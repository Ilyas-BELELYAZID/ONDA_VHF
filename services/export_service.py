import asyncio
import os
import pandas as pd
import datetime
from PIL import Image as PILImage, ImageDraw, ImageFont

# --- Importations pour le graphique ---
import matplotlib.pyplot as plt
import matplotlib

from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image as ReportLabImage
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Flowable

# Configuration pour Matplotlib en mode non-interactif
matplotlib.use('Agg')

# ==============================================================================
# === CLASSE DE THÈME AVEC COULEURS DE GRAVITÉ ==================================
# ==============================================================================
class ModernTheme:
    """Centralise les couleurs pour un design cohérent et facile à modifier."""
    PRIMARY = colors.HexColor("#2F54EB")
    TEXT_COLOR = colors.HexColor("#333333")
    TITLE_COLOR = colors.HexColor("#1D3557")
    ROW_LIGHT = colors.HexColor("#FFFFFF")
    ROW_DARK = colors.HexColor("#F0F2F5")
    GRID_COLOR = colors.HexColor("#E0E0E0")

    SEVERITY_CRITICAL = (colors.HexColor("#D92D20"), colors.whitesmoke)
    SEVERITY_HIGH     = (colors.HexColor("#D92D20"), colors.whitesmoke)
    SEVERITY_MEDIUM   = (colors.HexColor("#F79009"), colors.HexColor("#1E293B"))
    SEVERITY_LOW      = (colors.HexColor("#039855"), colors.whitesmoke)
    SEVERITY_DEFAULT  = (colors.HexColor("#64748B"), colors.whitesmoke)

    @staticmethod
    def get_severity_style(severity: str):
        s_lower = str(severity).lower()
        if "critique" in s_lower:
            return ModernTheme.SEVERITY_CRITICAL
        if "élevée" in s_lower or "haute" in s_lower:
            return ModernTheme.SEVERITY_HIGH
        if "moyenne" in s_lower:
            return ModernTheme.SEVERITY_MEDIUM
        if "faible" in s_lower:
            return ModernTheme.SEVERITY_LOW
        return ModernTheme.SEVERITY_DEFAULT

    @staticmethod
    def to_rgb(color):
        """ReportLab Color -> (R,G,B) ints 0-255"""
        return tuple(int(c * 255) for c in color.rgb())

    @staticmethod
    def to_hex(color):
        """ReportLab Color -> '#rrggbb' compatible matplotlib."""
        hexval = color.hexval()
        if hexval.startswith("0x"):
            hexval = "#" + hexval[2:]
        return hexval

    @staticmethod
    def darken_color(color, factor=0.8):
        """Renvoie une version plus sombre du reportlab Color (tuple RGB 0-255)."""
        r, g, b = ModernTheme.to_rgb(color)
        r = max(0, min(255, int(r * factor)))
        g = max(0, min(255, int(g * factor)))
        b = max(0, min(255, int(b * factor)))
        return (r, g, b)

    @staticmethod
    def contrast_text_color_from_rgb(rgb):
        """Retourne (255,255,255) ou (0,0,0) selon contraste (luminance simple)."""
        r, g, b = rgb
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        return (255, 255, 255) if lum < 140 else (0, 0, 0)

# ==============================================================================
# === CLASSE EXPORTSERVICE MISE À JOUR =========================================
# ==============================================================================
class SeverityBadge(Flowable):
    def __init__(self, text, border_color, row_index, font_size=9, padding_x=8, padding_y=5):
        super().__init__()
        self.text = text
        self.border_color = border_color
        self.row_index = row_index
        self.font_size = font_size
        self.padding_x = padding_x
        self.padding_y = padding_y

        # Mesurer la largeur du texte
        from reportlab.pdfbase.pdfmetrics import stringWidth
        self.text_width = stringWidth(self.text, "Helvetica", self.font_size)
        self.width = 60 # self.text_width + 2 * self.padding_x
        self.height = 20 # self.font_size + 2 * self.padding_y
        self.radius = 10  # arrondi

    def draw(self):
        c = self.canv

        # Fond alterné (blanc / gris clair)
        bg_color = colors.HexColor("#F0F2F5") if self.row_index % 2 == 0 else colors.white

        # Dessiner rectangle arrondi
        c.setFillColor(bg_color)
        c.setStrokeColor(self.border_color)
        c.setLineWidth(1)
        c.roundRect(0, 0, self.width, self.height, self.radius, stroke=1, fill=1)

        # Texte centré
        c.setFont("Helvetica", self.font_size)
        c.setFillColor(self.border_color)
        text_x = self.width / 2
        text_y = (self.height - self.font_size) / 2 + 1
        c.drawCentredString(text_x, text_y, self.text)

class ExportService:
    _badge_cache = {}
    
    @staticmethod
    def _cleanup_badges():
        """Nettoie les fichiers de badges temporaires."""
        for path in ExportService._badge_cache.values():
            if os.path.exists(path):
                os.remove(path)
        ExportService._badge_cache.clear()

    # Les méthodes export_excel et _header_footer ne changent pas (omises pour la clarté)
    @staticmethod
    def export_excel(events: list, output_path: str):
        print(f"  [Thread] Début de la génération du fichier Excel : {output_path}")
        df = pd.DataFrame(events) if events else pd.DataFrame(columns=["timestamp","event_type","equipment_type","description","severity"])
        cols = ["timestamp","event_type","equipment_type","description","severity"]
        df = df[cols]
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        df.to_excel(output_path, index=False, engine="xlsxwriter")
        print(f"  [Thread] Fichier Excel généré.")
        return output_path

    @staticmethod
    def _header_footer(canvas_obj, doc, logo_path=None, title="Historique des événements"):
        canvas_obj.saveState()
        width, height = landscape(A4)
        if logo_path and os.path.exists(logo_path):
            try:
                canvas_obj.drawImage(logo_path, 25, height - 87, width=130, height=90, preserveAspectRatio=True, mask='auto')
            except Exception:
                pass
        canvas_obj.setFont("Helvetica-Bold", 18)
        canvas_obj.setFillColor(ModernTheme.TITLE_COLOR)
        canvas_obj.drawCentredString(width / 2.0, height - 35, title)
        canvas_obj.setFont("Helvetica", 11)
        canvas_obj.setFillColor(ModernTheme.TEXT_COLOR)
        canvas_obj.drawRightString(width - 35, height - 40, datetime.datetime.now().strftime("%d %B %Y à %H:%M"))
        canvas_obj.setStrokeColor(ModernTheme.GRID_COLOR)
        canvas_obj.line(30, height - 90, width - 30, height - 90)
        canvas_obj.setFont("Helvetica-Bold", 9)
        canvas_obj.setFillColor(colors.grey)
        canvas_obj.drawCentredString(width / 2.0, 20, f"- Page {doc.page} -")
        canvas_obj.restoreState()

    @staticmethod
    def _create_events_chart(events: list, output_path: str):
        if not events: return
        print(f"  [Thread] Génération du graphique des événements...")
        df = pd.DataFrame(events)
        event_counts = df['severity'].value_counts()
        colors_map = [ModernTheme.to_hex(ModernTheme.get_severity_style(s)[0]) for s in event_counts.index]
        # => ["#d92d20", "#f79009", ...] ✅
        plt.style.use('seaborn-v0_8-whitegrid')
        fig, ax = plt.subplots(figsize=(10, 4), dpi=300)
        bars = ax.bar(event_counts.index, event_counts.values, color=colors_map)
        ax.set_title("Répartition par Gravité", fontsize=14, color=ModernTheme.to_hex(ModernTheme.TITLE_COLOR), pad=20)
        ax.set_ylabel("Nombre d'événements", fontsize=10, color=ModernTheme.to_hex(ModernTheme.TEXT_COLOR))
        ax.tick_params(axis='x', colors=ModernTheme.to_hex(ModernTheme.TEXT_COLOR), rotation=0)
        ax.tick_params(axis='y', colors=ModernTheme.to_hex(ModernTheme.TEXT_COLOR))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(ModernTheme.to_hex(ModernTheme.GRID_COLOR))
        ax.spines['bottom'].set_color(ModernTheme.to_hex(ModernTheme.GRID_COLOR))
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom', fontsize=9)
        plt.tight_layout()
        plt.savefig(output_path, format='png', transparent=True)
        plt.close()
        print(f"  [Thread] Graphique enregistré sous '{output_path}'")


    @staticmethod
    def export_pdf(events: list, output_path: str, title="Historique des événements",
                   analysis_text: str = "", logo_path: str = "assets/logo_onda_officiel.png"):
        try:
            print(f"  [Thread] Début de la génération du fichier PDF professionnel : {output_path}")
            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            
            chart_image_path = "temp_chart.png"
            ExportService._create_events_chart(events, chart_image_path)

            doc = SimpleDocTemplate(output_path, pagesize=landscape(A4), leftMargin=inch*0.5, rightMargin=inch*0.5, topMargin=inch*1.4, bottomMargin=inch*0.5)

            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='TitleSection', parent=styles['h2'], fontName='Helvetica-Bold', fontSize=12, textColor=ModernTheme.TITLE_COLOR, spaceBefore=20, spaceAfter=10))
            styles.add(ParagraphStyle(name='Analysis', parent=styles['Normal'], fontName='Helvetica', fontSize=10, textColor=ModernTheme.TEXT_COLOR, leading=14))

            flowables = []
            
            if os.path.exists(chart_image_path):
                flowables.append(Paragraph("Aperçu Visuel", styles['TitleSection']))
                img = ReportLabImage(chart_image_path, width=8*inch, height=2.6*inch)
                img.hAlign = 'CENTER'
                flowables.append(img)
                flowables.append(Spacer(1, 24))

            if analysis_text:
                flowables.append(Paragraph("Analyse et Recommandations", styles['TitleSection']))
                flowables.append(Paragraph(analysis_text, styles['Analysis']))
                flowables.append(Spacer(1, 24))

            flowables.append(Paragraph("Détails des Événements", styles['TitleSection']))
            
            header = ["Date/Heure", "Type", "Équipement", "Description", "Gravité"]
            data = [header]

            for idx, r in enumerate(events):
                dt = r.get("timestamp", "")
                if hasattr(dt, "strftime"):
                    dt = dt.strftime("%Y-%m-%d %H:%M:%S")
                desc = (r.get("description", "")[:220] + "...") if len(r.get("description", "")) > 220 else r.get("description", "")

                severity_text = r.get("severity", "Inconnue")
                border_color, _ = ModernTheme.get_severity_style(severity_text)

                badge = SeverityBadge(severity_text, border_color, idx)

                row_data = [
                    Paragraph(str(dt), styles['Normal']),
                    Paragraph(str(r.get("event_type", "")), styles['Normal']),
                    Paragraph(str(r.get("equipment_type", "")), styles['Normal']),
                    Paragraph(desc, styles['Normal']),
                    badge  # inséré directement
                ]
                data.append(row_data)


            tbl = Table(data, colWidths=[110, 110, 110, 390, 80], repeatRows=1, rowHeights=None)
            
            # --- Style de tableau mis à jour ---
            table_style = TableStyle([
                ('BACKGROUND', (0,0), (-1,0), ModernTheme.PRIMARY),
                ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('FONTSIZE', (0,0), (-1,0), 10),
                ('BOTTOMPADDING', (0,0), (-1,0), 10),
                ('TOPPADDING', (0,0), (-1,0), 10),
                ('ALIGN', (0,0), (-1,0), 'CENTER'),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), # ALIGNEMENT VERTICAL AU CENTRE POUR TOUT LE TABLEAU
                ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
                ('FONTSIZE', (0,1), (-1,-1), 9),
                ('TEXTCOLOR', (0,1), (-1,-1), ModernTheme.TEXT_COLOR),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
                ('RIGHTPADDING', (0,0), (-1,-1), 8),
                ('TOPPADDING', (0,1), (-1,-1), 8),
                ('BOTTOMPADDING', (0,1), (-1,-1), 8),
                ('LINEBELOW', (0,0), (-1,0), 1.5, ModernTheme.PRIMARY),
                ('LINEBELOW', (0,1), (-1,-1), 0.5, ModernTheme.GRID_COLOR),
            ])

            for i in range(1, len(data)):
                if i % 2 != 0:
                     table_style.add('BACKGROUND', (0,i), (-1,i), ModernTheme.ROW_DARK)

            tbl.setStyle(table_style)
            flowables.append(tbl)
            
            on_first_page = lambda c, d: ExportService._header_footer(c, d, logo_path, title)
            on_later_pages = lambda c, d: ExportService._header_footer(c, d, logo_path, title)
            
            doc.build(flowables, onFirstPage=on_first_page, onLaterPages=on_later_pages)
            print(f"  [Thread] Fichier PDF professionnel généré.")
            return output_path
        
        finally:
            # --- NOUVEAU : Nettoyage final ---
            if os.path.exists("temp_chart.png"):
                os.remove("temp_chart.png")
            ExportService._cleanup_badges()
