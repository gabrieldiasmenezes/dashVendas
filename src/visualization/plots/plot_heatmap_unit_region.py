import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_heatmap_unit_region(df:pd.DataFrame,save_path:str="output/graph/top_bottom_unit.png")->None:
    """
        Gera um gráfico de lolipop para as 3 unidades com maior  e menor lucro total.

        Args:
            df: pd.DataFrame - Dataframe com colunas ['business_unit','profit_total']
            save_path:str: Caminho para salvar o gráfico em PNG
    """
    if os.path.exists(save_path):
        print(f"Gráfico já existe: {save_path}")
    else:
        #Criacao da matriz unidade x regiao
        heatmap_data=df.pivot_table(
            index="business_unit",
            columns="region",
            values="profit",
            aggfunc="sum",
            fill_value=0
        )
        plt.style.use('seaborn-v0_8-whitegrid')
        plt.figure(figsize=(12,6))

        #Criaçaõ do heatmap
        ax=sns.heatmap(
            heatmap_data,
            annot=True,
            fmt=".0f",
            cmap="RdYlGn", 
            linewidths=0.5,
            linecolor='gray',
            cbar_kws={'label':'Lucro Total (R$)'}
        )
        ax.set_title("Performace por Unidade de Negócio x Região",fontsize=16,fontweight="bold")
        ax.set_xlabel("Região",fontsize=12)
        ax.set_ylabel("Unidade de Negócio",fontsize=12)

        plt.tight_layout()
        plt.savefig(save_path,dpi=300)
        plt.close()
        print(f"Gráfico salvo em: {save_path}")


