import os
import matplotlib.pyplot as plt
import pandas as pd

def plot_profit_by_region(region:pd.DataFrame,save_path: str="output/graph/region_profit.png")->None:
    """
        Gera gráfico de barras verticais com lucro por região.

        Args:
            region:pd.DataFrame:Dataframe com colunas ['region','profit_total','margin_%']
            save_path:str: Caminho para salvar o gráfico em PNG
    """
    if os.path.exists(save_path):
        print(f"Gráfico já existe: {save_path}")
    else:
        plt.style.use("seaborn-v0_8-whitegrid")
        fig,ax=plt.subplots(figsize=(10,6))
        region_sorted=region.sort_values(by='profit_total',ascending=False).reset_index(drop=True)
        
        #Definfindo cores por performace usando percentils
        low=region_sorted['profit_total'].quantile(0.33)
        high=region_sorted['profit_total'].quantile(0.66)
        colors=[]
        for profit in region_sorted['profit_total']:
            if profit<low:
                colors.append("#e74c3c")
            elif profit>high:
                colors.append("#2ecc71")
            else:
                colors.append("#f1c40f") 
        
        #Criacao do gráfico
        ax.bar(region_sorted['region'],region_sorted['profit_total'],color=colors)

        #Valores acima das barras
        for i,v in enumerate(region_sorted['profit_total']):
            ax.text(
                i,v+max(region_sorted['profit_total'])*0.01,
                f"R${v:,.0f}",
                ha="center",
                fontsize=9,
                color="#333333"
            )
         #Título e labels
        ax.set_title("Lucro por Região ",fontsize=16, fontweight="bold")
        ax.set_xlabel("Região",fontsize=12)
        ax.set_ylabel("Lucro Total (R$)",fontsize=12)

        #Grid leve
        ax.grid(axis="y",alpha=0.4,linestyle="--")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.tight_layout()
        plt.savefig(save_path,dpi=300)
        plt.close()
        print(f"Gráfico salvo em: {save_path}")



