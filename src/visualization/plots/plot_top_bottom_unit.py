import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_top_bottom_unit(unit:pd.DataFrame,save_path:str="output/graph/top_bottom_unit.png")->None:
    """
        Gera um gráfico de lolipop para as 3 unidades com maior  e menor lucro total.

        Args:
            unit: pd.DataFrame - Dataframe com colunas ['business_unit','profit_total']
            save_path:str: Caminho para salvar o gráfico em PNG
    """
    if os.path.exists(save_path):
        print(f"Gráfico já existe: {save_path}")
    else:
        #Ordena a unidade por lucro
        unit_sorted=unit.sort_values(by='profit_total',ascending=False)

        #Seleciona Top 3 e Bottom 3
        top_bottom=pd.concat([unit_sorted.head(3),unit_sorted.tail(3)])

        #Lógica de cores
        low = top_bottom['profit_total'].quantile(0.33)   # 33% mais baixos → vermelho
        high = top_bottom['profit_total'].quantile(0.66)  # 33% mais altos → verde
        colors=[]
        for profit in top_bottom['profit_total']:
            if profit <low:
                colors.append("#e74c3c")
            elif profit>high:
                colors.append("#2ecc71")
            else:
                colors.append("#f1c40f")
        
        fig,ax=plt.subplots(figsize=(10,6))

        x=range(len(top_bottom))
        y=top_bottom['profit_total']
        labels=top_bottom['business_unit']

        #Desenha os "palitos"(linhas verticais)
        for i,val in enumerate(y):
            ax.vlines( x=i , ymin=0 , ymax=val , color=colors[i] , linewidth=2)
            ax.plot(i,val,'o',color=colors[i],markersize=10)
        
        #Labels e títulos
        ax.set_xticks(x)
        ax.set_xticklabels(labels,rotation=45,ha='right')
        ax.set_ylabel("Lucro Total (R$)",fontsize=12)
        ax.set_title("Top e Bottom 3 Unidades de Negócio (Lolipop)",fontsize=16, fontweight='bold')

        ax.grid(axis="x",alpha=0.3,linestyle="--")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.tight_layout()
        plt.savefig(save_path,dpi=300)
        plt.close()
        print(f"Gráfico salvo em: {save_path}")
