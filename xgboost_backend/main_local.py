import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import seaborn as sns
import pickle
import os
from dateutil.relativedelta import relativedelta
from preprocesador import all_preprocessor, all_preprocessor_train
from XGBoot import initialize_train_model, mape_score, MAPE_validation


LOCAL_PATH = 'Agricultural_data/consolidado_final1.csv'
script_path = os.path.dirname(__file__)
csv_path = os.path.join(script_path, "..", LOCAL_PATH)

consolidado = pd.read_csv(LOCAL_PATH)

def get_current_date(N_month_predict):
    Current_date = pd.Timestamp.now()
    New_date = Current_date + relativedelta(months=N_month_predict)
    month = New_date.month
    year = New_date.year
    print("Mes a predecir:", month)
    print("Año a predecir:", year)
    return int(month), int(year)


def input_usuario(N_month_predict:int, consolidado:pd.DataFrame = consolidado):
    # verificar que se encuentre en la base de datos
    df = all_preprocessor(consolidado) # preprocesando el dataframe completo
    month_date, year_date = get_current_date(N_month_predict) # obteniendo mes y año actual
    #date = pd.to_datetime(f'{year_date}-{month_date:02d}-01')
    # Sumar los meses a la fecha actual utilizando relativedelta

    date = pd.to_datetime(f'{year_date}-{month_date}-01')
    print(date)
    if date in df['date'].values:
        filtered_df = df[df['date'].dt.month == month_date]
        filtered_df = filtered_df[filtered_df['date'].dt.year == year_date]
        print(f"✅ data is valid")
        print(filtered_df['date'])
        return filtered_df, N_month_predict
    else:
        print(f"❌ data is not valid, please try again")
        return "❌ data is not valid, please try again"

def feature_selection(df, N_month_predict):
    Variables = {}

    Variables['y_{}'.format(N_month_predict)] = np.log(df['price_soybean'])
    Selected_features = [df.columns.tolist()[i] for i in range(16, df.shape[1])]
    Selected_features.append('{} (t-{})'.format('price_soybean', N_month_predict))
    Selected_features.append('{} (t-{})'.format('real_interest_rate', N_month_predict))
    Selected_features.append('{} (t-{})'.format('SP500', N_month_predict))
    Selected_features.append('{} (t-{})'.format('usa_prod', N_month_predict))
    Variables['X_{}'.format(N_month_predict)] = df[Selected_features]
    return Variables

def train_xgboost(N_month_predict, consolidado:pd.DataFrame = consolidado) -> pd.DataFrame:
    df = all_preprocessor_train(consolidado)
    # Choose 90% of the rows randomly
    # df = df.sample(frac=0.9, random_state=42)
    df = df.drop(columns=['date'], axis=1)
    Scores = {}
    Results = {}
    # Seleccionando features de acuerdo a cuántos meses se va a predecir
    selection = feature_selection(df, N_month_predict)
    y_log = selection['y_{}'.format(N_month_predict)]
    X = selection['X_{}'.format(N_month_predict)]
    X_train, X_test, y_train_log, y_test_log = train_test_split(X,y_log,test_size=0.3,random_state=42)
    model_init = initialize_train_model()
    # Chequear el mape score del target y original --> aplicando la exponencial al logaritmo
    score = cross_val_score(model_init,X,np.exp(y_log),cv=15,scoring=mape_score(),n_jobs=-1).mean()
    Scores['cross_val_score_{}'.format(N_month_predict)] = score
    model = model_init.fit(X_train, y_train_log,
                           verbose=False,
                           eval_set=[(X_train, y_train_log)],
                           eval_metric=["mape"],
                           early_stopping_rounds=10)
    Results['y_predict_{}'.format(N_month_predict)] = np.exp(model_init.predict(X_test))
    Results['y_test_{}'.format(N_month_predict)] = np.exp(y_test_log)
    results = pd.DataFrame.from_dict(Results)
    # Chequear el mape score con los resultados --> y_test, y_predict
    mape_validation = MAPE_validation(Results['y_predict_{}'.format(N_month_predict)],
                                      Results['y_test_{}'.format(N_month_predict)])
    # print(results)
    print(Scores)
    print("MAPE Validation {}: ".format(N_month_predict), mape_validation)
    # Saving XGBoot Model
    save_xgboot_model(model, N_month_predict)
    return model

def save_xgboot_model(model, N_month_predict):
    model_path = os.path.join(script_path, 'model_XGBoost_{}'.format(N_month_predict))
    with open(model_path, 'wb') as archivo:
        pickle.dump(model, archivo)
    print("Modelo XGBoost guardado ✅.")


def predict_xgboost(filtered_df, N_month_predict):
    #if meses --> cargar modelo
    User_results = {}
    try:
        model_path = os.path.join(script_path, 'model_XGBoost_{}'.format(N_month_predict))
        with open(model_path, 'rb') as archivo:
            load_model = pickle.load(archivo)
        print("Modelo XGBoost cargado exitosamente ✅.")
        filtered_df = filtered_df.drop(columns=['date'], axis=1)
        selection = feature_selection(filtered_df, N_month_predict)
        X = selection['X_{}'.format(N_month_predict)]
        features = X.columns
        User_results['y_predict_{}'.format(N_month_predict)] = np.exp(load_model.predict(filtered_df[features]))
        print(X)
        price_soybean_result = User_results['y_predict_{}'.format(N_month_predict)][0]
        print("El precio de la soja dentro de {} meses será de $: ".format(N_month_predict),price_soybean_result)
        return price_soybean_result

    except FileNotFoundError:
        train_xgboost(N_month_predict, consolidado)



if __name__ == '__main__':
    try:
        LOCAL_PATH = 'Agricultural_data/consolidado_final1.csv'
        script_path = os.path.dirname(__file__)
        csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        consolidado = pd.read_csv(csv_path)
        N_month_predict = 3
        filtered_df, N_month_predict = input_usuario(N_month_predict, consolidado)
        predict_xgboost(filtered_df, N_month_predict)

    except:
        import sys
        import traceback

        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
