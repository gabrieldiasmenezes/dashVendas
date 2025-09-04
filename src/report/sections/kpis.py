from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

try:
    pdfmetrics.registerFont(TTFont("Montserrat", "Montserrat-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Montserrat-Bold", "Montserrat-Bold.ttf"))
    MAIN_FONT = "Montserrat"
except:
    MAIN_FONT = "Helvetica"

def build_kpis(story, kpis_dict):
    section_title = ParagraphStyle("SectionTitle", fontName=MAIN_FONT, fontSize=18, textColor=colors.HexColor("#003366"), spaceBefore=10, spaceAfter=20, alignment=1)
    story.append(Paragraph(" Indicadores-Chave de Performance (KPIs)", section_title))
    story.append(Spacer(1, 0.5*cm))

    styles = getSampleStyleSheet()
    for section, values in kpis_dict.items():
        story.append(Paragraph(section, ParagraphStyle("SubSection", fontName=MAIN_FONT, fontSize=14, textColor=colors.HexColor("#0055A4"), alignment=1, spaceAfter=10)))
        data = []
        for k, v in values.items():
            bg = "#F5F7FA"
            if "Lucro" in k: bg = "#E8F5E9"
            elif "Receita" in k: bg = "#E3F2FD"
            elif "Custo" in k: bg = "#FFF3E0"
            data.append([Paragraph(f"<b>{k}</b>", styles["Normal"]), Paragraph(f"<b>{v}</b>", styles["Normal"])])
        table = Table(data, colWidths=[8*cm, 6*cm])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg)),
            ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#DDDDDD")),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CCCCCC")),
            ("FONTNAME", (0, 0), (-1, -1), MAIN_FONT),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        story.append(table)
        story.append(Spacer(1, 1.2*cm))
