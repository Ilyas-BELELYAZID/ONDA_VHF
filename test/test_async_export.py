import asyncio
import os
import pandas as pd
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image as ReportLabImage
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
import datetime
from PIL import Image as PILImage, ImageDraw # Pour créer les images de démo

# ==============================================================================
# === VOTRE CLASSE EXPORTSERVICE (INCHANGÉE) ====================================
# ==============================================================================

class ExportService:
    @staticmethod
    def export_excel(events: list, output_path: str):
        print(f"  [Thread] Début de la génération du fichier Excel : {output_path}")
        if not events:
            df = pd.DataFrame(columns=["created_at","event_type","equipment_type","description","severity"])
        else:
            df = pd.DataFrame(events)
        cols = ["created_at","event_type","equipment_type","description","severity"]
        cols = [c for c in cols if c in df.columns] + [c for c in df.columns if c not in cols]
        df = df[cols]
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        df.to_excel(output_path, index=False, engine="xlsxwriter")
        print(f"  [Thread] Fichier Excel généré.")
        return output_path

    @staticmethod
    def _header_footer(canvas_obj, doc, logo_path=None, title="Historique des événements"):
        canvas_obj.saveState()
        width, height = landscape(A4)
        # Logo à gauche
        if logo_path and os.path.exists(logo_path):
            try:
                img_w, img_h = 130, 90
                canvas_obj.drawImage(logo_path, 25, height - 87, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')
            except Exception:
                pass
        # Titre au centre
        canvas_obj.setFont("Helvetica-Bold", 18)
        canvas_obj.drawCentredString(width/2.0, height - 35, title)
        # Date à droite
        canvas_obj.setFont("Helvetica", 11)
        canvas_obj.drawRightString(width - 35, height - 35, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        # Pied de page (numéro de page)
        canvas_obj.setFont("Helvetica-Bold", 9)
        canvas_obj.drawCentredString(width/2.0, 17, f"- Page {doc.page} -")
        canvas_obj.restoreState()

    @staticmethod
    def export_pdf(events: list, output_path: str, title="Historique des événements",
                   analysis_text: str = "", logo_path: str = None, chart_image_path: str = None):
        print(f"  [Thread] Début de la génération du fichier PDF : {output_path}")
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        doc = SimpleDocTemplate(output_path, pagesize=landscape(A4),
                                leftMargin=30, rightMargin=30, topMargin=95, bottomMargin=40)

        styles = getSampleStyleSheet()
        normal = styles["Normal"]
        
        flowables = []
        # Image du graphique (optionnel)
        if chart_image_path and os.path.exists(chart_image_path):
            try:
                img = ReportLabImage(chart_image_path, width=9*inch, height=3*inch)
                flowables.append(img)
                flowables.append(Spacer(1, 12))
            except Exception:
                pass

        # Texte d'analyse
        if analysis_text:
            flowables.append(Paragraph(f"<b>Analyse IA :</b> {analysis_text}", normal))
            flowables.append(Spacer(1, 12))

        # Construction des données de la table
        header = ["Date/Heure", "Type", "Équipement", "Description", "Gravité"]
        data = [header]
        for r in events:
            dt = r.get("created_at", "")
            if hasattr(dt, "strftime"):
                dt = dt.strftime("%Y-%m-%d %H:%M:%S")
            desc = r.get("description", "")
            data.append([
                dt,
                r.get("event_type", ""),
                r.get("equipment_type", ""),
                (desc[:220] + "...") if len(desc) > 220 else desc,
                r.get("severity", "")
            ])

        tbl = Table(data, colWidths=[110, 120, 120, 380, 70], repeatRows=1)
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#f5f7fa")),
            ("TEXTCOLOR", (0,0), (-1,0), colors.black),
            ("GRID", (0,0), (-1,-1), 0.25, colors.grey),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 9),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
            ("RIGHTPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ]))
        flowables.append(tbl)

        # Construction du PDF avec les callbacks pour l'en-tête et le pied de page
        on_first_page = lambda c, d: ExportService._header_footer(c, d, logo_path, title)
        on_later_pages = lambda c, d: ExportService._header_footer(c, d, logo_path, title)

        doc.build(flowables, onFirstPage=on_first_page, onLaterPages=on_later_pages)
        print(f"  [Thread] Fichier PDF généré.")
        return output_path

# ==============================================================================
# === SCRIPT DE TEST ASYNCHRONE ================================================
# ==============================================================================

def create_placeholder_image(path: str, size: tuple, text: str):
    """Crée une image simple pour les tests."""
    if not os.path.exists(path):
        img = PILImage.new('RGB', size, color='white')
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, size[0]-1, size[1]-1], outline='black')
        d.text((10, size[1]//2 - 5), text, fill='black')
        img.save(path)
        print(f"Image de démonstration créée : '{path}'")

async def main():
    """Fonction principale pour lancer les exports de manière asynchrone."""
    print("🚀 Début du script de test d'exportation asynchrone...")

    # --- 1. Préparation des données et des ressources ---
    now = datetime.datetime.now()
    sample_events = [
        {"created_at": now - datetime.timedelta(hours=1), "event_type": "Alarme", "equipment_type": "Caméra PTZ-01", "description": "Mouvement détecté dans la zone 3.", "severity": "Élevée"},
        {"created_at": now - datetime.timedelta(minutes=30), "event_type": "Notification", "equipment_type": "Serveur de stockage", "description": "Espace disque faible, 85% utilisé.", "severity": "Moyenne"},
        {"created_at": now - datetime.timedelta(minutes=10), "event_type": "Erreur Système", "equipment_type": "Contrôleur d'accès", "description": "Échec de la communication avec le lecteur de badge de la porte principale. Tentative de reconnexion en cours. L'incident a été enregistré pour analyse.", "severity": "Élevée"},
        {"created_at": now, "event_type": "Info", "equipment_type": "Système", "description": "Le service de surveillance a redémarré avec succès après une mise à jour planifiée.", "severity": "Faible"},
        {"created_at": now - datetime.timedelta(hours=1), "event_type": "Alarme", "equipment_type": "Caméra PTZ-01", "description": "Mouvement détecté dans la zone 3.", "severity": "Élevée"},
        {"created_at": now - datetime.timedelta(minutes=30), "event_type": "Notification", "equipment_type": "Serveur de stockage", "description": "Espace disque faible, 85% utilisé.", "severity": "Moyenne"},
        {"created_at": now - datetime.timedelta(minutes=10), "event_type": "Erreur Système", "equipment_type": "Contrôleur d'accès", "description": "Échec de la communication avec le lecteur de badge de la porte principale. Tentative de reconnexion en cours. L'incident a été enregistré pour analyse.", "severity": "Élevée"},
        {"created_at": now, "event_type": "Info", "equipment_type": "Système", "description": "Le service de surveillance a redémarré avec succès après une mise à jour planifiée.", "severity": "Faible"},
        {"created_at": now - datetime.timedelta(hours=1), "event_type": "Alarme", "equipment_type": "Caméra PTZ-01", "description": "Mouvement détecté dans la zone 3.", "severity": "Élevée"},
        {"created_at": now - datetime.timedelta(minutes=30), "event_type": "Notification", "equipment_type": "Serveur de stockage", "description": "Espace disque faible, 85% utilisé.", "severity": "Moyenne"},
        {"created_at": now - datetime.timedelta(minutes=10), "event_type": "Erreur Système", "equipment_type": "Contrôleur d'accès", "description": "Échec de la communication avec le lecteur de badge de la porte principale. Tentative de reconnexion en cours. L'incident a été enregistré pour analyse.", "severity": "Élevée"},
        {"created_at": now, "event_type": "Info", "equipment_type": "Système", "description": "Le service de surveillance a redémarré avec succès après une mise à jour planifiée.", "severity": "Faible"},
        {"created_at": now - datetime.timedelta(hours=1), "event_type": "Alarme", "equipment_type": "Caméra PTZ-01", "description": "Mouvement détecté dans la zone 3.", "severity": "Élevée"},
        {"created_at": now - datetime.timedelta(minutes=30), "event_type": "Notification", "equipment_type": "Serveur de stockage", "description": "Espace disque faible, 85% utilisé.", "severity": "Moyenne"},
        {"created_at": now - datetime.timedelta(minutes=10), "event_type": "Erreur Système", "equipment_type": "Contrôleur d'accès", "description": "Échec de la communication avec le lecteur de badge de la porte principale. Tentative de reconnexion en cours. L'incident a été enregistré pour analyse.", "severity": "Élevée"},
        {"created_at": now, "event_type": "Info", "equipment_type": "Système", "description": "Le service de surveillance a redémarré avec succès après une mise à jour planifiée.", "severity": "Faible"},
    ]
    
    # Création d'images fictives pour que le script fonctionne directement
    logo_path = "assets/logo_onda_officiel.png"
    chart_path = "chart_placeholder.png"
    create_placeholder_image(logo_path, (200, 60), "LOGO")
    create_placeholder_image(chart_path, (800, 250), "Graphique de démonstration")

    # --- 2. Lancement des tâches d'exportation avec asyncio.to_thread ---
    
    # Tâche d'exportation Excel
    excel_path = "rapport_evenements.xlsx"
    print(f"\n[Main] Lancement de l'exportation Excel vers '{excel_path}' dans un thread...")
    excel_task = asyncio.to_thread(
        ExportService.export_excel, 
        sample_events, 
        excel_path
    )

    # Tâche d'exportation PDF
    pdf_path = "rapport_evenements.pdf"
    analysis = "La majorité des événements critiques sont liés à des erreurs de communication matérielle."
    print(f"[Main] Lancement de l'exportation PDF vers '{pdf_path}' dans un thread...")
    pdf_task = asyncio.to_thread(
        ExportService.export_pdf,
        sample_events,
        pdf_path,
        title="Rapport d'Événements Asynchrone",
        analysis_text=analysis,
        logo_path=logo_path,
        chart_image_path=chart_path
    )
    
    # --- 3. Attente de la fin des tâches ---
    print("[Main] En attente de la fin des deux tâches d'exportation...")
    excel_result, pdf_result = await asyncio.gather(excel_task, pdf_task)
    
    print("\n✅ Tâches terminées !")
    print(f"   -> Fichier Excel enregistré ici : {os.path.abspath(excel_result)}")
    print(f"   -> Fichier PDF enregistré ici : {os.path.abspath(pdf_result)}")


if __name__ == "__main__":
    asyncio.run(main())