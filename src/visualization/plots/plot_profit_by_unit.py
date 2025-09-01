import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_profit_by_unit(unit:pd.DataFrame,save_path:str="output/graph/unit_profit.png")-> None:
    """
        Gera gráfico de barras horizontais com lucro por unidade de negócio.

        Args:
            unit:pd.DataFrame:Dataframe com colunas ['business_unit','profit_total','margin_%']
            save_path:str: Caminho para salvar o gráfico em PNG
    """
    if os.path.exists(save_path):
        print(f"Gráfico já existe: {save_path}")
    else:
        plt.style.use("seaborn-v0_8-whitegrid")
        fig,ax=plt.subplots(figsize=(10,6))

        #Ordena pelo lucro para melhor visualização
        unit_sorted=unit.sort_values("profit_total")

        #Aplicando diferentes cores por condicao
        low = unit_sorted['profit_total'].quantile(0.33)   # 33% mais baixos → vermelho
        high = unit_sorted['profit_total'].quantile(0.66)  # 33% mais altos → verde
        colors=[]
        for profit in unit_sorted['profit_total']:
            if profit <low:
                colors.append("#e74c3c")
            elif profit>high:
                colors.append("#2ecc71")
            else:
                colors.append("#f1c40f")

        # Barra horizontal
        ax.barh(
            unit_sorted["business_unit"],
            unit_sorted["profit_total"],
            color=colors
        )

        #Valores de lucro acima das barras
        for i,(profit,margin) in enumerate(zip(unit_sorted["profit_total"],unit_sorted["margin_%"])):
            ax.text(profit+ max(unit_sorted["profit_total"])*0.01,i,
                    f"R${profit:,.0f} ({margin:.1f}%)",
                    va="center",fontsize=9,color="#333333")
        
        #Título e labels
        ax.set_title("Lucro por unidade de Negócio",fontsize=16, fontweight="bold")
        ax.set_xlabel("Lucro Total (R$)",fontsize=12)
        ax.set_ylabel("Unidade de Negócio",fontsize=12)

        #Grid leve
        ax.grid(axis="x",alpha=0.3,linestyle="--")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.tight_layout()
        plt.savefig(save_path,dpi=300)
        plt.close()
        print(f"Gráfico salvo em: {save_path}")