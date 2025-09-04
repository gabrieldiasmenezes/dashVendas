import pandas as pd

def calculate_profit(df:pd.DataFrame)-> pd.DataFrame:
    """
        Calcula receita,custo e lucro de cada venda e mostra KPI's gerais.

        Args:
            df:pd.DataFrame:Dataframe limpo
        Returns:
            pd.DataFrame:DataFrame com colunas adicionais: 'revenue','cost','profit'.
    """
    df=df.copy()

    #Calculos
    df['revenue']=df['quantity'] * df['unit_price']
    df['cost']=df['quantity'] * df['unit_cost']
    df['profit']=df['revenue'] - df['cost']

    #KPIs
    total_revenue=df['revenue'].sum()
    total_cost=df['cost'].sum()
    total_profit=df['profit'].sum()
    margin=(total_profit/total_revenue)*100 if total_revenue !=0 else 0
    
    avg_revenue=df['revenue'].mean() # Verifica quanto cada transação gera de receita
    avg_cost=df['cost'].mean() # Verifica quanto cada transacao gera de custo
    avg_profit=df['profit'].mean() # Verifica quanto cada transacao gera de lucro
    profitable_percentage=(df['profit']>0).mean() *100 # Mostra quantos negócios realmente deram lucro
    negative_profit_count=(df['profit']<0).sum() # Mostra vendas que geraram lucros negativos
    kpis_dict = {
        "KPIs Gerais da Empresa": {
            "Receita total": f"R$ {total_revenue:,.2f}",
            "Custo total": f"R$ {total_cost:,.2f}",
            "Lucro total": f"R$ {total_profit:,.2f}",
            "Margem média": f"{margin:.1f} %"
        },
        "Médias por venda": {
            "Receita média": f"R$ {avg_revenue:,.2f}",
            "Custo médio": f"R$ {avg_cost:,.2f}",
            "Lucro médio": f"R$ {avg_profit:,.2f}"
        },
        "Performance": {
            "Porcentagem de vendas lucrativas": f"{profitable_percentage:.1f} %",
            "Vendas com prejuízo": f"{negative_profit_count}"
        }
    }
    
    print("\n===== KPIs CALCULADOS =====")
    for section,value in kpis_dict.items():
        print(f"\n {section}")
        print("-" * 40)
        for k,v in value.items():
            print(f"{k:<35} {v}")

    return df,kpis_dict


