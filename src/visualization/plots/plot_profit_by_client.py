import matplotlib.pyplot as plt
import pandas as pd
import os
def plot_profit_by_client(client:pd.DataFrame,save_path:str= "output/graph/client_profit.png")->None:
    """
        Gera um gráfico de Pareto com lucro por cliente (Top 10).

        Args:
            monthly:pd.DataFrame- DataFrame com colunas ['client','profit_total']
            save_path:str :Caminho para salvar o gráfico em PNG
    """
    if os.path.exists(save_path):
        print(f"Gráfico já existe: {save_path}")
    else:
        client['cum_percentage']=client['profit_total'].cumsum()/client['profit_total'].sum()*100

        plt.style.use("seaborn-v0_8-whitegrid")
        fig,ax1=plt.subplots(figsize=(12,6))
        x=client['client']
        y=client['profit_total']
        low = y.quantile(0.33)   # 33% mais baixos → vermelho
        high = y.quantile(0.66)  # 33% mais altos → verde
        colors=[]
        for profit in y:
            if profit <low:
                colors.append("#e74c3c")
            elif profit>high:
                colors.append("#2ecc71")
            else:
                colors.append("#f1c40f")
        #Gráfico de Barras(lucro por cliente)
        bars=ax1.bar(x,y,color=colors)
        ax1.set_xlabel("Cliente",fontsize=12)
        ax1.set_ylabel("Lucro Total (R$)", fontsize=12)
        ax1.tick_params(axis="y")
        ax1.set_xticks(range(len(x)))
        ax1.set_xticklabels(x,rotation=45,ha='right')

        #Linha acumulada
        ax2=ax1.twinx()
        ax2.plot(
            x,client["cum_percentage"],
            color="#000",
            marker="o",
            linewidth=2
            )
        ax2.set_ylabel("Percentual Acumulado (%)",fontsize=12)
        ax2.tick_params(axis="y")
        ax2.set_ylim(0,110)

        #Titulo
        plt.title("Pareto-Lucro por Cliente",fontsize=16,fontweight="bold")

        plt.tight_layout()
        plt.savefig(save_path,dpi=300)
        plt.close()
        print(f"✅ Gráfico salvo em: {save_path}")