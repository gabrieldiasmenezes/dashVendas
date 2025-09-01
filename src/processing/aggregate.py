import pandas as pd
import numpy as np
def aggregate_by_month(df: pd.DataFrame)->pd.DataFrame:
    """
        Agrega o lucro total por mes e calcula crescimento percentual.
        Args:
            df:pd.DataFrame:Dataframe atualizado com os calculos necessarios para o relatorio
        Returns:
            pd.DataFrame:DataFrame com os lucros mensais
    """
    df=df.copy()
    df['month']=df['date'].dt.to_period('M')
    monthly=df.groupby('month',as_index=False).agg(
        revenue_total=("revenue","sum"),
        profit_total=("profit","sum")
        )
    monthly["margin_%"]=(monthly["profit_total"]/monthly["revenue_total"])*100
    monthly["margin_%"].replace([np.inf,-np.inf],np.nan,inplace=True)
    monthly["margin_%"] = monthly["margin_%"].round(2) 
    monthly['growth_%']=monthly['profit_total'].pct_change()*100
    monthly["growth_%"] = monthly["growth_%"].round(2)

    return monthly

def aggregate_by_business_unit(df: pd.DataFrame)->pd.DataFrame:
    """
        Agrega lucro total e margem por unidade de negócio
        Args:
            df:pd.DataFrame:Dataframe atualizado com os calculos necessarios para o relatorio
        Returns:
            pd.DataFrame:DataFrame dos lucros totais e margens por unidade de negócio
    """
    df=df.copy()
    unit=df.groupby('business_unit',as_index=False).agg(
        profit_total=('profit','sum'),
        revenue_total=('revenue','sum')
    )
    unit['margin_%']=(unit['profit_total'] / unit['revenue_total'])*100
    unit["margin_%"].replace([np.inf,-np.inf],np.nan,inplace=True)
    unit["margin_%"] = unit["margin_%"].round(2) 
    unit.sort_values(by='profit_total',ascending=False,inplace=True)
    return unit

def aggregate_by_region(df: pd.DataFrame)->pd.DataFrame:
    """
        Agrega lucro total e margem por região
        Args:
            df:pd.DataFrame:Dataframe atualizado com os calculos necessarios para o relatorio
        Returns:
            pd.DataFrame:DataFrame dos lucros totais e margens por região
    """
    df=df.copy()
    region=df.groupby('region',as_index=False).agg(
        profit_total=('profit','sum'),
        revenue_total=('revenue','sum')
    )
    region['margin_%']=(region['profit_total'] / region['revenue_total'])*100
    region["margin_%"].replace([np.inf,-np.inf],np.nan,inplace=True)
    region["margin_%"] = region["margin_%"].round(2) 
    region.sort_values(by='profit_total',ascending=False,inplace=True)
    return region



def aggregate_by_client(df: pd.DataFrame,top_n:int=10)->pd.DataFrame:
    """
        Agrega lucro total por cliente e ordena por lucro
        Args:
            df:pd.DataFrame:Dataframe atualizado com os calculos necessarios para o relatorio
            top_n: int=10:Retorna os 10 melhores clientes por lucro
        Returns:
            pd.DataFrame:DataFrame dos lucros totais por cliente
    """
    df=df.copy()
    client=df.groupby('client',as_index=False).agg(
        profit_total=("profit","sum"),
        revenue_total=("revenue","sum")
    )
    client['margin_%']=(client['profit_total'] / client['revenue_total'])*100
    client["margin_%"].replace([np.inf,-np.inf],np.nan,inplace=True)
    client["margin_%"] = client["margin_%"].round(2) 
    client.sort_values(by='profit_total',ascending=False,inplace=True)
    return client.head(top_n)


