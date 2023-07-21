import sys
sys.path.insert(0, '/xgboost_backend')
from xgboost_backend_soybean.main_local import input_usuario_xgboost_soybean, predict_xgboost_soybean
from xgboost_backend_corn.main_local import input_usuario_xgboost_corn, predict_xgboost_corn
from rf_backend_corn.main_local import input_usuario_rf_corn, predict_rf_corn
from rf_backend_soy.main_local import input_usuario_rf_soybean, predict_rf_soybean
import pandas as pd
import os
import yfinance as yf
#from xgboost_backend.graphs import plt
import datetime
import streamlit as st


def predict_price_soybean(time_horizon):

    if time_horizon == "1 Month":
        LOCAL_PATH = 'Agricultural_data/consolidado_soycorn.csv'
        script_path = os.path.dirname(__file__)
        #csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        csv_path = os.path.join(script_path, LOCAL_PATH)
        consolidado = pd.read_csv(LOCAL_PATH)
        N_month_predict = 1
        filtered_df, N_month_predict = input_usuario_rf_soybean(N_month_predict, consolidado)
        result = predict_rf_soybean(filtered_df, N_month_predict)
        return result

    elif time_horizon == "3 Months":

        LOCAL_PATH = 'Agricultural_data/consolidado_soycorn.csv'
        script_path = os.path.dirname(__file__)
        #csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        csv_path = os.path.join(script_path, LOCAL_PATH)
        consolidado = pd.read_csv(LOCAL_PATH)
        N_month_predict = 3
        filtered_df, N_month_predict = input_usuario_xgboost_soybean(N_month_predict, consolidado)
        result = predict_xgboost_soybean(filtered_df, N_month_predict)
        return result

    elif time_horizon == "6 Months":

        LOCAL_PATH = 'Agricultural_data/consolidado_soycorn.csv'
        script_path = os.path.dirname(__file__)
        #csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        csv_path = os.path.join(script_path, LOCAL_PATH)
        consolidado = pd.read_csv(LOCAL_PATH)
        N_month_predict = 6
        filtered_df, N_month_predict = input_usuario_xgboost_soybean(N_month_predict, consolidado)
        result = predict_xgboost_soybean(filtered_df, N_month_predict)

        return result
    else:
        return ""

def predict_price_corn(time_horizon):
    if time_horizon == "1 Month":

        LOCAL_PATH = 'Agricultural_data/consolidado_soycorn.csv'
        script_path = os.path.dirname(__file__)
        #csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        csv_path = os.path.join(script_path, LOCAL_PATH)
        consolidado = pd.read_csv(LOCAL_PATH)
        N_month_predict = 1
        filtered_df, N_month_predict = input_usuario_rf_corn(N_month_predict, consolidado)
        result = predict_rf_corn(filtered_df, N_month_predict)
        return result

    elif time_horizon == "3 Months":

        LOCAL_PATH = 'Agricultural_data/consolidado_soycorn.csv'
        script_path = os.path.dirname(__file__)
        #csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        csv_path = os.path.join(script_path, LOCAL_PATH)
        consolidado = pd.read_csv(LOCAL_PATH)
        N_month_predict = 3
        filtered_df, N_month_predict = input_usuario_xgboost_corn(N_month_predict, consolidado)
        result = predict_xgboost_corn(filtered_df, N_month_predict)
        return result

    elif time_horizon == "6 Months":

        LOCAL_PATH = 'Agricultural_data/consolidado_soycorn.csv'
        script_path = os.path.dirname(__file__)
        #csv_path = os.path.join(script_path, "..", LOCAL_PATH)
        csv_path = os.path.join(script_path, LOCAL_PATH)
        consolidado = pd.read_csv(LOCAL_PATH)
        N_month_predict = 6
        filtered_df, N_month_predict = input_usuario_xgboost_corn(N_month_predict, consolidado)
        result = predict_xgboost_corn(filtered_df, N_month_predict)

        return result
    else:
        return ""
