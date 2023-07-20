import streamlit as st
from modelx import predict_price
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from actual_price import actualprice

import streamlit as st

def get_actual_price(ticker):
    price, date = actualprice(ticker)
    return price, date

ticker = ""
col1, col2 = st.columns(2)

if col1.button("SOY"):
    ticker = "ZS=F"
    st.text("Welcome to the Soybean price predictor")

if col2.button("CORN"):
    ticker = "ZC=F"
    st.text("Welcome to the Corn price predictor")

price= None
date = None

if ticker:
    price, date = get_actual_price(ticker)

st.title("Price Prediction")



st.subheader(f"Last available data is from: {date} and last price is: ${price}")




if st.button("1 Month"):
    prediction_horizon = "1 Month"

if st.button("3 Months"):
    prediction_horizon = "3 Months"


if st.button("6 Months"):
    prediction_horizon = "6 Months"

# Predict and display the message if a time horizon is selected
if 'prediction_horizon' in locals():
    prediction = predict_price(prediction_horizon)
    st.subheader(f"Predicted Soybean Price for {prediction_horizon}:")


    st.write(prediction)
