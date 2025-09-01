import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_revenue_vs_profit_by_region(region:pd.DataFrame,save_path:str="output/graph/revenue_vs_profit_by_region.png")->None:
    """
        Gera gráfico de barras agrupadas comparando Receita e Lucro por Região

        Args:
            region:pd.DataFrame:Dataframe com colunas ['region','profit_total','revenue_total']
            save_path:str: Caminho para salvar o gráfico em PNG
    """
    if os.path.exists(save_path):
        print(f"Gráfico já existe: {save_path}")
    else:

        plt.style.use('seaborn-v0_8-whitegrid')
        fig,ax=plt.subplots(figsize=(12,6))
        x= np.arange(len(region)) # Posição no eixo x
        width=0.34 #Latgora das barras

        #Barras
        rects1=ax.bar(x-width/2,region['revenue_total'],width,label='Receita',color="#3498db")
        rects2=ax.bar(x-width/2,region['profit_total'],width,label='Lucro',color="#2ecc71")

        #Valores acima das barras
        for rect in rects1+rects2:
            height=rect.get_height()
            ax.text(
                rect.get_x() + rect.get_width()/2,
                height + max(region['revenue_total'])*0.01,
                f"R${height:,.0f}",ha='center',va='bottom',fontsize=9
            )

        #Labels e título
        ax.set_xlabel("Região",fontsize=12)
        ax.set_ylabel("Valor (R$)",fontsize=12)
        ax.set_title("Comparativo Receita x Lucro por Região",fontsize=16,fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels(region['region'],rotation=45,ha='right')
        ax.legend()

        #Grid e layout
        ax.grid(alpha=0.4,linestyle="--")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)


        plt.tight_layout()
        plt.savefig(save_path,dpi=300)
        plt.close()
        print(f"Gráfico salvo em: {save_path}")
            



     
    
