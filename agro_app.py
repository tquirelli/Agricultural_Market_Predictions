import streamlit as st

import datetime
import requests

'''
# TaxiFareModel front

This front queries the Le Wagon [taxi fare model API](https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2)
'''

with st.form(key='params_for_api'):

    Mes = st.number_input('Año', value=40.6413111)
    Año = st.number_input('Mes', value=-73.7803331)


    st.form_submit_button('Make prediction')

params = dict(
    Mes=Mes,
    Año=Año,
   )

soypredictor_url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(wagon_cab_api_url, params=params)

prediction = response.json()

pred = prediction['fare']

st.header(f'Fare amount: ${round(pred, 2)}')
