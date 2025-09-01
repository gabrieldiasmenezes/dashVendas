import pandas as pd
import os
def export_to_csv(df:pd.DataFrame,file_path:str):
    """
        Exporta um DataFrame para CSV
        Args:
            df:pd.DataFrame:DataFrame a ser exportado
            file_path:str:Caminho do arquivo de saída
    """
    try:
        if os.path.exists(file_path):
            print(f"Exportação não realizada, arquivo já existe: {file_path}")
        else:
            df.to_csv(file_path,index=False,encoding="utf-8")
            print(f"Dados exportados para:{file_path}")
    except Exception as e:
        print(f"Erro ao exportar dados para {file_path}: {e}")


