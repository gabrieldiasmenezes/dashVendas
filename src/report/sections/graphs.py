from reportlab.platypus import Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

try:
    pdfmetrics.registerFont(TTFont("Montserrat", "Montserrat-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Montserrat-Bold", "Montserrat-Bold.ttf"))
    MAIN_FONT = "Montserrat"
except:
    MAIN_FONT = "Helvetica"

def build_graphs(story, graphs):
    section_title = ParagraphStyle("SectionTitle", fontName=MAIN_FONT, fontSize=18, textColor=colors.HexColor("#003366"), spaceBefore=10, spaceAfter=20, alignment=1)
    story.append(PageBreak())
    story.append(Paragraph(" Análises Gráficas", section_title))
    story.append(Spacer(1, 0.8*cm))
    for graph_path in graphs:
        if os.path.exists(graph_path):
            story.append(Image(graph_path, width=14*cm, height=8*cm))
            story.append(Spacer(1, 1.5*cm))
        else:
            print(f"⚠ Gráfico não encontrado: {graph_path}")
