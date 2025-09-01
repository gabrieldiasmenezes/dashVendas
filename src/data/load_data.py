import pandas as pd
from typing import Optional

def load_sales_data(file_path:str)->Optional[pd.DataFrame]:
    """
        Carrega is dados de vendas de um arquivo CSV

        Args:
            file_path:str-Caminhio para o arquivo CSV
        
        Returns:
            Optional[pd.DataFrame]-DataFrame com os dados carregados ou None em casi de erro
    """
    try:
        df=pd.read_csv(file_path)
        
        #Convertendo coluna 'date' para datetime
        df['date']=pd.to_datetime(df['date'],errors='coerce')

        #Verificando se há uma data inválida
        if df['date'].isna().any():
            print('Atenção:Existem registros com datas inválidas que foram convertidos para NaT.')
        
        #Exibir resumo inicial
        print(f"""
Dados carregados com sucesso!

Total de registros: {len(df)}
-------------------------------------------------
Período: de {df['date'].min().date()} até {df['date'].max().date()}
-------------------------------------------------
Colunas: {list(df.columns)}

        """)
        return df
    except FileNotFoundError:
        print(f"Arquivo não encontradi em: {file_path}")
    
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        

