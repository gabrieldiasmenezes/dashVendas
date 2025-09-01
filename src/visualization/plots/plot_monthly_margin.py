import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_monthly_margin(monthly:pd.DataFrame,save_path:str="output/graph/monthly_margin.png")->None:
    """
        Gera um gráfico de área com a margem percentual mensal

        Args:
            monthly:pd.DataFrame-DataFrame com colunas ['month','margin_%']
            save_path:str - Caminho para salvar o gráfico em PNG
    """
    if os.path.exists(save_path):
        print(f"Gráfico já existe: {save_path}")
    else:
        plt.style.use('seaborn-v0_8-whitegrid')
        fig,ax=plt.subplots(figsize=(12,6))

        x=range(len(monthly))
        y=monthly['margin_%']

        for i in range(1,len(y)):
            if y[1] >= y[i-1]:
                color="#2ecc71"
            else:
                color="#e74c3c"
            ax.fill_between(x[i-1:i+1],y[i-1:i+1],color=color,alpha=0.4)
        
            #Linha da margem
        ax.plot(x,y,marker="o",color="#000",linewidth=2,markersize=6)

        #Adicina valores acima dos pontos
        for i,v in enumerate(y):
            ax.text(i,v+max(y)*0.02,f"{v:.1f}%",ha="center",fontsize=9,color="#333333")
        
        #Título e labels
        ax.set_title("Margem Mensal (%)",fontsize=16,fontweight="bold")
        ax.set_xlabel("Mês",fontsize=12)
        ax.set_ylabel("Margem (%)",fontsize=12)

         #Remove bordas desnecessárias
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.tight_layout()
        plt.savefig(save_path,dpi=300)
        plt.close()
        print(f"✅ Gráfico salvo em: {save_path}")
