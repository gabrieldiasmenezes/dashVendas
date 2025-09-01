import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader

def create_financial_report(kpis_text: str, graphs: list, save_path: str = "output/report/financial_report.pdf"):
    """
    Cria um PDF com os KPIs e gráficos da análise financeira, com layout organizado.

    Args:
        kpis_text (str): Texto com os KPIs calculados.
        graphs (list): Lista de paths para os gráficos PNG.
        save_path (str): Caminho do arquivo PDF a ser gerado.
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    c = canvas.Canvas(save_path, pagesize=A4)
    width, height = A4

    # Configuração de margens
    left_margin, right_margin, top_margin, bottom_margin = 2*cm, 2*cm, 2*cm, 2*cm
    available_width = width - left_margin - right_margin
    y_pos = height - top_margin

    # Adiciona título
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, y_pos, "Relatório Financeiro")
    y_pos -= 1.5*cm

    # Adiciona KPIs (quebra de linha automática)
    text_obj = c.beginText(left_margin, y_pos)
    text_obj.setFont("Helvetica", 11)
    line_height = 14  # px aproximado
    for line in kpis_text.split("\n"):
        if y_pos - line_height < bottom_margin:
            # Nova página
            c.drawText(text_obj)
            c.showPage()
            y_pos = height - top_margin
            text_obj = c.beginText(left_margin, y_pos)
            text_obj.setFont("Helvetica", 11)
        text_obj.textLine(line)
        y_pos -= line_height
    c.drawText(text_obj)
    y_pos -= 1*cm  # espaço após KPIs

    # Adiciona gráficos
    max_graph_height = 8*cm
    for graph_path in graphs:
        if os.path.exists(graph_path):
            # Se não houver espaço, cria nova página
            if y_pos - max_graph_height < bottom_margin:
                c.showPage()
                y_pos = height - top_margin

            img = ImageReader(graph_path)
            c.drawImage(img, left_margin, y_pos - max_graph_height,
                        width=available_width, height=max_graph_height,
                        preserveAspectRatio=True, anchor='n')

            y_pos -= max_graph_height + 1*cm  # espaço entre gráficos
        else:
            print(f"⚠ Gráfico não encontrado: {graph_path}")

    c.save()
    print(f"✅ Relatório PDF gerado em: {save_path}")
