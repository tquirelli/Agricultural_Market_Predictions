import streamlit as st
from modelx import predict_price
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from actual_price import last_price, last_date



# Streamlit app code
st.title("Soybean Price Prediction")
st.title(f'Last month price from {last_date} is ${int(last_price)}')

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
