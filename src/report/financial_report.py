from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
import os

# Importando módulos separados
from .sections.cover import build_cover
from .sections.kpis import build_kpis
from .sections.graphs import build_graphs
from .sections.conclusion import build_conclusion
from .utils.header_footer import HeaderFooter

def create_financial_report(kpis_dict, graphs, save_path="output/report/financial_report.pdf"):
    """
    Cria um relatório financeiro corporativo em PDF, com capa, KPIs, gráficos e conclusão.
    """
    # Cria a pasta de saída caso não exista
    if os.path.exists(save_path):
         print(f"Exportação não realizada, arquivo já existe: {save_path}")
    else:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Configuração do documento
        doc = SimpleDocTemplate(
            save_path,
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=3.5*cm,
            bottomMargin=2.5*cm
        )

        story = []  # Lista que armazenará os elementos do PDF
        width, height = A4

        # ====== CAPA ======
        draw_cover_func = build_cover(story, width, height)

        # ====== SEÇÃO KPIs ======
        build_kpis(story, kpis_dict)

        # ====== SEÇÃO GRÁFICOS ======
        build_graphs(story, graphs)

        # ====== CONCLUSÃO ======
        build_conclusion(
            story,
            "O relatório demonstra crescimento estável da receita e aumento gradual da margem operacional. "
            "Sugere-se intensificar investimentos em inovação e expandir para novos mercados estratégicos."
        )

        # ====== Cabeçalho e Rodapé ======
        def on_page(canvas, doc_ref):
            HeaderFooter(canvas, doc_ref).draw()

        # ====== Construção final do PDF ======
        doc.build(
            story,
            onFirstPage=draw_cover_func,  # Capa personalizada
            onLaterPages=on_page          # Cabeçalho/rodapé nas demais páginas
        )

        print(f"✅ Relatório PDF gerado em: {save_path}")
