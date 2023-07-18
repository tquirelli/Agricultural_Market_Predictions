from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import make_scorer
from .main_local import input_usuario,predict_xgboost
from .preprocesador import all_preprocessor
import pandas as pd
import os
import datetime
import streamlit as st

def initialize_train_model():
    # Instanciate model
    model_xgb = XGBRegressor(max_depth=10, n_estimators=300, learning_rate=0.1)
    return model_xgb

def mape_score():
    mape = make_scorer(lambda y_true, y_pred: mean_absolute_percentage_error(y_true, y_pred))
    return mape

def MAPE_validation(y_train, y_train_predict):
    return round(mean_absolute_percentage_error(y_train,y_train_predict),2)



def predict_price(time_horizon,consolidado):


    if time_horizon == "1 Month":

        return "En desarrollo"

    elif time_horizon == "3 Months":

        N_month_predict = 3
        filtered_df, N_month_predict = input_usuario(N_month_predict, consolidado)
        result = predict_xgboost(filtered_df, N_month_predict)

        return str(result)


    elif time_horizon == "6 Months":

        N_month_predict = 6
        filtered_df, N_month_predict = input_usuario(N_month_predict, consolidado)
        result = predict_xgboost(filtered_df, N_month_predict)

        return str(result)
    else:
        return ""