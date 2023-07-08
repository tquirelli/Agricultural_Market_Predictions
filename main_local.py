import pandas as pd
import numpy as np
from preprocesador import all_preprocessor

LOCAL_PATH = 'Agricultural_data/consolidado_final.csv'
consolidado = pd.read_csv(LOCAL_PATH)


def input_usuario(month_date:int = 2, year_date:int = 2022, consolidado:pd.DataFrame = consolidado):
    # verificar que se encuentre en la base de datos
    df = all_preprocessor(consolidado)
    # df['date'] = pd.to_datetime(df['date'])
    date = pd.to_datetime(f'{year_date}-{month_date:02d}-01')
    if date in df['date'].values:
        filtered_df = df[df['date'].dt.month == month_date]
        filtered_df = filtered_df[filtered_df['date'].dt.year == year_date]
        print(f"✅ data is valid")
        print(filtered_df)
        return filtered_df
    else:
        print(f"❌ data is not valid, please try again")
        return "❌ data is not valid, please try again"

def train(date) -> pd.DataFrame:
    pass




if __name__ == '__main__':
    try:

        input_usuario()
        # search_features(date)
        # preprocess()
        # train()
        # pred()
    except:
        import sys
        import traceback

        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
