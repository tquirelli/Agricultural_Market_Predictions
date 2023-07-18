import pandas as pd
from fastapi import FastAPI
from rf_backend_soy.main_local import input_usuario, predict_rf
from xgboost_backend.XGBoot import predict_price
import requests
import os

app = FastAPI()


@app.get("/predict_1")
def predict_api_1(time_horizon):
    LOCAL_PATH_rf = '/home/simon/code/tquirelli/Agricultural_Market_Predictions/Agricultural_data/consolidado_final.csv'
    #script_path = os.path.dirname(__file__)
    #csv_path = os.path.join(script_path, "..", LOCAL_PATH)
    #csv_path ='/home/simon/code/tquirelli/Agricultural_Market_Predictions/Agricultural_data/consolidado_final.csv'
    consolidado_rf = pd.read_csv(LOCAL_PATH_rf,parse_dates=["date"],header=0)
    N_month_predict = 1
    filtered_df, N_month_predict = input_usuario(N_month_predict, consolidado_rf)
 
    return predict_rf(filtered_df, N_month_predict)

    


@app.get("/predict_3_6")
def predict_api_3_6 (time_horizon):
    LOCAL_PATH = '/home/simon/code/tquirelli/Agricultural_Market_Predictions/Agricultural_data/consolidado_final1.csv'
    consolidado = pd.read_csv(LOCAL_PATH)
    return (predict_price(time_horizon,consolidado))

       

#@app.get("/get_ejemplo")
#def obtener_elementos():
    #return {"datos": datos}