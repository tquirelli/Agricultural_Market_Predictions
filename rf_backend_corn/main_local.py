import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import cross_val_score
from rf_backend_corn.preprocesador_rf import all_preprocessor
from rf_backend_corn.RandomForest import initialize_rf, mape_score
from dateutil.relativedelta import relativedelta

LOCAL_PATH = 'Agricultural_data/consolidado_soycorn.csv'
script_path = os.path.dirname(__file__)
csv_path = os.path.join(script_path, "..", LOCAL_PATH)
consolidado = pd.read_csv(LOCAL_PATH,parse_dates=["date"],header=0)

def get_new_date(N_month_predict):
    Current_date = pd.Timestamp.now()
    New_date = Current_date + relativedelta(months=N_month_predict)
    month = New_date.month
    year = New_date.year
    print("Mes a predecir:", month)
    print("Año a predecir:", year)
    return int(month), int(year)

def get_current_date():
    Current_date = pd.Timestamp.now()
    month = Current_date.month
    year = Current_date.year
    return int(month), int(year)

def input_usuario(N_month_predict:int, consolidado:pd.DataFrame = consolidado):
    # verificar que se encuentre en la base de datos
    df = all_preprocessor(consolidado) # preprocesando el dataframe completo
    month_date, year_date = get_new_date(N_month_predict) # obteniendo mes y año actual
    #date = pd.to_datetime(f'{year_date}-{month_date:02d}-01')
    # Sumar los meses a la fecha actual utilizando relativedelta

    date = f'{year_date}-{month_date}'
    print(date)
    if date in df.index:
        filtered_df = df[df.index == date]
        print(f"✅ data is valid")
        print(filtered_df.index)
        return filtered_df, N_month_predict
    else:
        print(f"❌ data is not valid, please try again")
        return "❌ data is not valid, please try again"

def train_rf(consolidado:pd.DataFrame = consolidado) -> pd.DataFrame:
    df = all_preprocessor(consolidado)

    #Scores = {}
    #Results = {}
    #User_results = {}

    features = [
    "ewma_2", "ewma_3", "ewma_6", "ma_2", "ma_3", "ma_6", "x_1",
    "x_2", "x_3", "x_4", "x_5", "x_6", "x_7", "x_8", "x_9", "x_10", "x_11", "x_12",
    "usa_corn_prod", "SP500", "real_interest_rate"
    ]

    new_features = df[features].fillna(0).values
    mo,ye=get_current_date()
    # create df_train and df_test
    df_train = df[df.index<=f"{ye}-{mo}"]
    #df_test = df[df.index>="2016-07-01"]

    # Keep track of test_indexes
    #test_indexes = np.arange(len(df_train), len(df_train)+len(df_test))
    #test_indexes

    model_init = initialize_rf()

    #score = cross_val_score(model_init,X,y_log,cv=5,scoring=mape_score(),n_jobs=-1).mean()

    #initialize_train_model, mape_score
    #Scores['cross_val_score_{}'.format(N_month_predict)] = score

    X_train=df_train[["usa_corn_prod","x_1","x_2","x_3","x_4","x_5","x_6","x_7","x_8","x_9","x_10","x_11","x_12","ma_2","ma_3","ma_6","ewma_2","ewma_3","ewma_6","real_interest_rate"]]
    y_train=df_train["price_corn"]

    model=model_init.fit(X_train, y_train)
    save_rf_model(model)

    return model

def save_rf_model(model):
    model_path = os.path.join(script_path, 'model_rf_corn')
    with open(model_path, 'wb') as archivo:
        pickle.dump(model, archivo)
    print("Modelo RF guardado ✅.")

###
def predict_rf(filtered_df, N_month_predict):
    #if meses --> cargar modelo
    User_results = {}
    try:
        model_path = os.path.join(script_path, 'model_rf_corn')
        with open(model_path, 'rb') as archivo:
            load_model = pickle.load(archivo)
        print("Modelo RF cargado exitosamente ✅.")
        predict_features=filtered_df[["usa_corn_prod","x_1","x_2","x_3","x_4","x_5","x_6","x_7","x_8","x_9","x_10","x_11","x_12","ma_2","ma_3","ma_6","ewma_2","ewma_3","ewma_6","real_interest_rate"]] #tendrían que ser las features solo del Mes que quiero predecir!
        User_results['y_predict_{}'.format(N_month_predict)] = load_model.predict(predict_features)
        print(predict_features)
        price_corn_result = User_results['y_predict_{}'.format(N_month_predict)][0]
        print("El precio del maíz dentro de {} mes será de $: ".format(N_month_predict),price_corn_result)
        return price_corn_result

    except FileNotFoundError:
        train_rf(consolidado)

###

if __name__ == '__main__':
    try:
        LOCAL_PATH = 'Agricultural_data/consolidado_soycorn.csv'
        script_path = os.path.dirname(__file__)
        csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        consolidado = pd.read_csv(csv_path,parse_dates=["date"],header=0)
        N_month_predict = 1
        filtered_df, N_month_predict = input_usuario(N_month_predict, consolidado)
        predict_rf(filtered_df, N_month_predict)

    except:
        import sys
        import traceback

        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
