import pandas as pd

def clean_sales_data(df:pd.DataFrame)->pd.DataFrame:
    """
        Limpa e valida os dados de vendas

        Args:
            df:df.DataFrame:DataFrame carregado com os dados
        
        Returns:
            pd.DataFrame:Dataframe limpo e validado
    """
    df=df.copy()
    initial_rows=len(df)

    # 1.Remover linhas com valores nulos
    df.dropna(inplace=True)

    # 2.Remover valores negativos ou zero nas colunas numéricas
    numeric_cols=["quantity","unit_price","unit_cost"]
    for col in numeric_cols:
        invalid_mask=df[col]<=0
        count_invalid=invalid_mask.sum()
        if count_invalid>0:
            print(f"foram removidas {count_invalid} linhas por terem valores <=0")
        df=df[~invalid_mask] #Manterá apenas as linhas com valores válidos
    
    # 3. Verificar coluna 'date'
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        df['date']=pd.to_datetime(df['date'],errors='coerce')#Caso um valor nao se converter para datetime na coluna date,será convertido para NaT
        df.dropna(subset=['date'],inplace=True)
    
    final_rows=len(df)
    print(f"Limpeza concluída: {initial_rows} -> {final_rows} linhas restantes")

    return df.reset_index(drop=True) # retorna o DataFrame com o indice resetado (0)

