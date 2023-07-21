from main_local import input_usuario, predict_xgboost
import pandas as pd
import os
import yfinance as yf
from graphs import plt
import datetime
import streamlit as st


def predict_price(time_horizon):



    if time_horizon == "1 Month":

        return "En desarrollo"

    elif time_horizon == "3 Months":

        LOCAL_PATH = 'Agricultural_data/consolidado_final1.csv'
        script_path = os.path.dirname(__file__)
        csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        consolidado = pd.read_csv(csv_path)
        N_month_predict = 3
        filtered_df, N_month_predict = input_usuario(N_month_predict, consolidado)
        result = predict_xgboost(filtered_df, N_month_predict)





        return result


    elif time_horizon == "6 Months":

        LOCAL_PATH = 'Agricultural_data/consolidado_final1.csv'
        script_path = os.path.dirname(__file__)
        csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        consolidado = pd.read_csv(csv_path)
        N_month_predict = 6
        filtered_df, N_month_predict = input_usuario(N_month_predict, consolidado)
        result = predict_xgboost(filtered_df, N_month_predict)

        return result
    else:
        return ""
