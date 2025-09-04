from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
try:
    pdfmetrics.registerFont(TTFont("Montserrat", "Montserrat-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Montserrat-Bold", "Montserrat-Bold.ttf"))
    MAIN_FONT = "Montserrat"
except:
    MAIN_FONT = "Helvetica"

def build_conclusion(story, texto):
    section_title = ParagraphStyle("SectionTitle", fontName=MAIN_FONT, fontSize=18, textColor=colors.HexColor("#003366"), spaceBefore=10, spaceAfter=20, alignment=1)
    story.append(PageBreak())
    story.append(Paragraph(" Conclusões e Recomendações", section_title))
    story.append(Spacer(1, 0.5*cm))
    conclusion_box = Table([[Paragraph(texto, getSampleStyleSheet()["Normal"])]], colWidths=[16*cm])
    conclusion_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E3F2FD")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#003366")),
        ("FONTNAME", (0, 0), (-1, -1), MAIN_FONT),
        ("PADDING", (0, 0), (-1, -1), 14),
    ]))
    story.append(conclusion_box)
