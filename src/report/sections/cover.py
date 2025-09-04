from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm

# registro de fontes
try:
    pdfmetrics.registerFont(TTFont("Montserrat", "Montserrat-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Montserrat-Bold", "Montserrat-Bold.ttf"))
    MAIN_FONT = "Montserrat"
except:
    MAIN_FONT = "Helvetica"

def build_cover(story, width, height):
    capa_title = ParagraphStyle("CapaTitulo", fontName=MAIN_FONT, fontSize=32, textColor=colors.white, alignment=1, spaceAfter=20)
    capa_sub = ParagraphStyle("CapaSub", fontName=MAIN_FONT, fontSize=16, textColor=colors.white, alignment=1)
    
    def draw_cover(canvas, doc):
        canvas.setFillColor(colors.HexColor("#003366"))
        canvas.rect(0, 0, width, height, stroke=0, fill=1)
    
    story.append(Spacer(1, 7*cm))
    story.append(Paragraph("Relatório Financeiro Corporativo", capa_title))
    story.append(Paragraph("Empresa XYZ Tech", capa_sub))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("Período: Jan - Dez 2025", capa_sub))
    story.append(PageBreak())
    
    return draw_cover
