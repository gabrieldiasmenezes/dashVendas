import os
from src.processing.export_data import export_to_csv
from src.processing.aggregate import( 
    aggregate_by_month,
    aggregate_by_business_unit,
    aggregate_by_region,
    aggregate_by_client
)
from src.processing.calculate_profit import calculate_profit
from src.data.clean_data import clean_sales_data
from src.data.load_data import load_sales_data
from src.visualization import (
    plot_monthly_profit, 
    plot_profit_by_unit,
    plot_profit_by_region,
    plot_profit_by_client,
    plot_monthly_margin,
    plot_revenue_vs_profit_by_region,
    plot_top_bottom_unit,
    plot_heatmap_unit_region
    )
from src.report.financial_report import create_financial_report




os.system('cls')

url="data/sales.csv"

#O if __name__ == "__main__": serve para rodar código apenas quando o arquivo for executado diretamente, e não quando ele for importado.
try:
    if __name__=="__main__":

        #Carregando os dados importados do csv
        df=load_sales_data(url)
        
        if df is  None:
            exit()

        #Limpeza do csv
        df_clean=clean_sales_data(df)

        #Calculos dos KPIs
        df_profit,kpis_text=calculate_profit(df_clean)

        #Agregações
        monthly_profit=aggregate_by_month(df_profit)
        unit_profit=aggregate_by_business_unit(df_profit)
        region_profit=aggregate_by_region(df_profit)
        client_profit=aggregate_by_client(df_profit)

        print("\n Lucro por mês:")
        print(monthly_profit)

        print("\n Lucro por unidade de negócio:")
        print(unit_profit)

        print("\n Lucro por região:")
        print(region_profit)

        print("\n Lucro por cliente:")
        print(client_profit)

        #Exportando os novos DataFrames criados para o relatorio baseado nos dados do DataFrame importado exportando-os para a pasta output
        export_to_csv(df_profit, "output/csv/processed_data.csv")
        export_to_csv(monthly_profit, "output/csv/monthly_profit.csv")
        export_to_csv(unit_profit, "output/csv/unit_profit.csv")
        export_to_csv(region_profit, "output/csv/region_profit.csv")
        export_to_csv(client_profit, "output/csv/cilent_profit.csv")

        #Criação dos gráficos a partir do csv
        plot_monthly_profit(monthly_profit,save_path="output/graph/monthly_profit.png")
        plot_profit_by_unit(unit_profit,save_path="output/graph/unit_profit.png")
        plot_profit_by_region(region_profit,save_path="output/graph/region_profit.png")
        plot_profit_by_client(client_profit,save_path="output/graph/client_profit.png")
        plot_monthly_margin(monthly_profit,save_path="output/graph/monthly_margin.png")
        plot_revenue_vs_profit_by_region(region_profit,save_path="output/graph/revenue_vs_profit_by_region.png")
        plot_top_bottom_unit(unit_profit,save_path="output/graph/top_bottom_unit.png")
        plot_heatmap_unit_region(df_profit,save_path="output/graph/heatmap_unit_region.png")

        #Geração do relatorio
        graphs = [
            "output/graph/monthly_profit.png",
            "output/graph/unit_profit.png",
            "output/graph/region_profit.png",
            "output/graph/client_profit.png",
            "output/graph/monthly_margin.png",
            "output/graph/revenue_vs_profit_by_region.png",
            "output/graph/top_bottom_unit.png",
            "output/graph/heatmap_unit_region.png"
        ]
        create_financial_report(kpis_text,graphs,save_path="output/report/financial_report.pdf")
except Exception as e:
    print(f"Erro: {e}")