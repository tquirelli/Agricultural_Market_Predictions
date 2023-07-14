from xgboost_backend.main_local import input_usuario, predict_xgboost
import pandas as pd
import os




def predict_price(time_horizon):
    if time_horizon == "1 Month":
        LOCAL_PATH = 'Agricultural_data/consolidado_final1.csv'
        script_path = os.path.dirname(__file__)
        csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        consolidado = pd.read_csv(csv_path)
        N_month_predict = 1
        filtered_df, N_month_predict = input_usuario(N_month_predict, consolidado)

        result = predict_xgboost(filtered_df, N_month_predict)
        return result
    elif time_horizon == "3 Months":
        return "Welcome to the 3 Months prediction"
    elif time_horizon == "6 Months":
        return "Welcome to the 6 Months prediction"
    else:
        return ""
