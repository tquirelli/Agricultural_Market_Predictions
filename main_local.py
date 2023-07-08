import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import seaborn as sns
from preprocesador import all_preprocessor
from XGBoot import initialize_train_model, mape_score

LOCAL_PATH = 'Agricultural_data/consolidado_final.csv'
consolidado = pd.read_csv(LOCAL_PATH)


def input_usuario(month_date:int = 2, year_date:int = 2022, consolidado:pd.DataFrame = consolidado):
    # verificar que se encuentre en la base de datos
    df = all_preprocessor(consolidado)
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

def train_xgboost(consolidado:pd.DataFrame = consolidado, filtered_df = None) -> pd.DataFrame:
    df = all_preprocessor(consolidado)
    # Defining test and train size
    # df_train = df[df.date<="2017-12-01"]
    # df_test = df[df.date>="2018-01-01"]
    # Choose 90% of the rows randomly
    df = df.sample(frac=0.9, random_state=42)
    df = df.drop(columns=['date'], axis=1)
    Scores = {}
    Results = {}
    User_results = {}
    N_month_predict = 3 # Choice between 3 and 6

    Variables = feature_selection(df, N_month_predict)
    y_log = Variables['y_{}'.format(N_month_predict)]
    X = Variables['X_{}'.format(N_month_predict)]
    X_train, X_test, y_train_log, y_test_log = train_test_split(X,y_log,test_size=0.3,random_state=42)
    model_init = initialize_train_model()

    score = cross_val_score(model_init,X,y_log,cv=5,scoring=mape_score(),n_jobs=-1).mean()
    initialize_train_model, mape_score
    Scores['cross_val_score_{}'.format(N_month_predict)] = score
    model_init.fit(X_train, y_train_log,
        verbose=False,
        eval_set=[(X_train, y_train_log)],
        eval_metric=["mape"],
        early_stopping_rounds=10)
    Results['y_predict_{}'.format(N_month_predict)] = np.exp(model_init.predict(X_test))
    Results['y_test_{}'.format(N_month_predict)] = np.exp(y_test_log)
    filtered_df = input_usuario()
    filtered_df = filtered_df.drop(columns=['date'], axis=1)
    features = X.columns
    User_results['y_predict_{}'.format(N_month_predict)] = np.exp(model_init.predict(filtered_df[features]))
    print(User_results)



if __name__ == '__main__':
    try:
        train_xgboost()

    except:
        import sys
        import traceback

        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
