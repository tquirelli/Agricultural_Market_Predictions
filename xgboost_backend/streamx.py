import streamlit as st
from modelx import predict_price
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from actual_price import actualprice
from graphs import graph_soy
##last_price, last_date



# Streamlit app code
last_price, last_date = actualprice(("ZC=F"))
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
    graph = graph_soy(prediction, prediction_horizon)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(graph)


# graph_soy(prediction,mes)
