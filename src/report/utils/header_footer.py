from reportlab.platypus import Flowable
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

try:
    pdfmetrics.registerFont(TTFont("Montserrat", "Montserrat-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Montserrat-Bold", "Montserrat-Bold.ttf"))
    MAIN_FONT = "Montserrat"
except:
    MAIN_FONT = "Helvetica"

class HeaderFooter(Flowable):
    """
    Classe que desenha cabeçalho e rodapé em cada página do PDF.
    Deve ser chamada no 'onLaterPages' do SimpleDocTemplate.
    """
    def __init__(self, canvas, doc):
        self.canvas = canvas
        self.doc = doc

    def draw(self):
        width, height = self.doc.pagesize

        # ====== Cabeçalho ======
        self.canvas.setFillColor(colors.HexColor("#003366"))
        self.canvas.setFont(MAIN_FONT, 9)
        self.canvas.rect(0, height-30, width, 30, stroke=0, fill=1)
        self.canvas.setFillColor(colors.white)
        self.canvas.drawString(2*72, height-20, "Relatório Financeiro - Empresa XYZ Tech")  # 2*72 = 2 polegadas
        self.canvas.drawRightString(width - 2*72, height-20, f"Página {self.doc.page}")

        # ====== Rodapé ======
        self.canvas.setFillColor(colors.HexColor("#003366"))
        self.canvas.setFont(MAIN_FONT, 8)
        self.canvas.drawCentredString(width/2, 15, "Confidencial • Uso Interno • 2025")
