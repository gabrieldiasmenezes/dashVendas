import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_monthly_profit(monthly:pd.DataFrame,save_path:str= "output/graph/monthly_profit.png")->None:
    """
        Gera um gráfico de linha com lucro mensal.

        Args:
            monthly:pd.DataFrame- DataFrame com colunas ['month','profit_total']
            save_path:str :Caminho para salvar o gráfico em PNG
    """
    if os.path.exists(save_path):
        print(f"Gráfico já existe: {save_path}")
    else:
        plt.style.use('seaborn-v0_8-whitegrid')
        fig,ax=plt.subplots(figsize=(12,6))
        x=range(len(monthly))
        y=monthly['profit_total']

        #Desenha segmentos coloridos
        for i in range(1,len(y)):
            if y[i]>=y[i-1]:
                color="#2ecc71"
            else:
                color="#e74c3c"
            #Linha do lucro
            ax.plot(
                x[i-1:i+1],
                y[i-1:i+1],
                color=color,
                linewidth=2,
                marker="o",
                markersize=8
            )

        #Adiciona valores de lucro acima dos pontos
        for i,v in enumerate(y):
            ax.text(
                i,v +max(y)*0.02, 
                f"R${v:,.0f}", 
                ha="center",
                fontsize=9,
                color="#333333")
        
        #Títulos e labels
        ax.set_title("Lucro Mensal",fontsize=16,fontweight="bold")
        ax.set_xlabel("Mês",fontsize=12)
        ax.set_ylabel("Lucro Total",fontsize=12)

        #Ajuste de ticks e grid
        ax.set_xticks(range(len(monthly)))
        ax.set_xticklabels(monthly["month"].astype(str),rotation=45,ha="right")
        ax.grid(alpha=0.4,linestyle="--")

        #Remove bordas desnecessárias
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.tight_layout()
        plt.savefig(save_path,dpi=300)
        plt.close()
        print(f"✅ Gráfico salvo em: {save_path}")
