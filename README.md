# 📊 DashVendas — Relatório Financeiro Automatizado

**Autor:** Gabriel Dias Menezes  
**Descrição:** O **DashVendas** é uma aplicação em **Python** que automatiza a análise de vendas a partir de um CSV e gera um **relatório financeiro completo em PDF**, incluindo KPIs, agregações e gráficos profissionais.  

---

## 🚀 Visão Geral
O DashVendas transforma dados brutos de vendas em insights visuais e executivos prontos para apresentação.  
Ele:
- Processa e limpa dados de vendas.
- Calcula **KPIs financeiros** (receita, custo, lucro, margem, vendas lucrativas).
- Agrega informações por **mês**, **unidade de negócio**, **região** e **cliente**.
- Cria múltiplos gráficos (linha, barra, heatmap, lollipop, comparativos).
- Exporta CSVs processados e um **PDF consolidado** com tudo.

---

## 🛠️ Tecnologias Utilizadas
- [Python 3.10+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/) — manipulação de dados  
- [Matplotlib](https://matplotlib.org/) e [Seaborn](https://seaborn.pydata.org/) — gráficos  
- [ReportLab](https://www.reportlab.com/) — geração de PDF  

---

## 📂 Estrutura do Projeto
```graphql
DashVendas/
├─ data/
│  └─ sales.csv                # CSV exemplo (mantido no repo)
│
├─ output/
│  ├─ csv/                     # CSVs gerados pelo pipeline
│  ├─ graph/                   # Imagens PNG dos gráficos gerados
│  └─ report/                  # PDF final
│
├─ src/
│  ├─ data/
│  │  ├─ load_data.py
│  │  └─ clean_data.py
│  │
│  ├─ processing/
│  │  ├─ calculate_profit.py
│  │  ├─ aggregate.py
│  │  └─ export_data.py
│  │
│  ├─ visualization/
│  │  └─ plots/
│  │     ├─ plot_monthly_profit.py
│  │     ├─ plot_monthly_margin.py
│  │     ├─ plot_profit_by_unit.py
│  │     ├─ plot_profit_by_region.py
│  │     ├─ plot_profit_by_client.py
│  │     ├─ plot_revenue_vs_profit_by_region.py
│  │     ├─ plot_top_bottom_unit.py
│  │     └─ plot_heatmap_unit_region.py
│  │
│  └─ report/
│     ├─ __init__.py
│     └─ financial_report.py    # create_financial_report()
│
├─ main.py
├─ requirements.txt
└─ .gitignore

```
## ▶️ Como Executar
1. Clone o repositório
  No prompt de comando digite:
```bash
git clone https://github.com/gabrieldiasmenezes/dashVendas.git
cd dashVendas
```
2. Crie e ative o ambiente virtual
```bash
python -m venv venv
# Ativar:
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3. Instale as dependências
```bash
pip install -r requirements.txt
```
4.Rode o pipeline
```bash
python main.py
```
  ✅ Isso vai gerar:

  - CSVs em output/csv/

  - Gráficos em output/graph/

  - Relatório PDF em output/report/financial_report.pdf

## 📈 Gráficos Incluídos

- Lucro mensal (linha)

- Margem mensal (área)

- Lucro por unidade de negócio (barras horizontais)

- Lucro por região (barras verticais)

- Lucro por cliente (Pareto)

- Receita × Lucro por região (barras agrupadas)

- Top/Bottom unidades (lollipop)

- Heatmap de performance (unidade × região)

## 📑 Relatório Final
O relatório PDF inclui:

- KPIs executivos formatados

- Todos os gráficos listados

- Layout paginado automaticamente

📍 Exemplo de saída: `` output/report/financial_report.pdf ``







































