import streamlit as st
import requests
import numpy as np
import pandas as pd
import streamlit as st
from xgboost_backend.XGBoot import predict_price
from PIL import Image
import base64
import streamlit as st



st.set_page_config(
    page_title="Agricultural Market Prediction",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    body {
        background-image:url('https://www.infocampo.com.ar/wp-content/uploads/2020/01/agricultura-soja-infocampo.jpg');
        background-size: cover;
        background-repeat: no-repeat;
    }

    .main-container {
        padding: 4rem;
        color: white;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("Soybean Price Prediction")

if st.button("1 Month"):
    time_horizon = "1 Month"
    params = {'time_horizon': time_horizon}
    url_rf='http://127.0.0.1:8000/predict_1'
    prediction_rf = requests.get(url_rf,params=params).json()
    st.header(f'Future Price in a Month:¢/bu {round(prediction_rf,2)}')

if st.button("3 Months"):
    time_horizon = "3 Months"
    params = {'time_horizon': time_horizon}
    url_xg='http://127.0.0.1:8000/predict_3_6'
    prediction_xg = requests.get(url_xg,params=params).json()
    st.header(f'Future Price in three Month:¢/bu {prediction_xg}')
    
if st.button("6 Months"):
    time_horizon = "6 Months"
    params = {'time_horizon': time_horizon}
    url_xg='http://127.0.0.1:8000/predict_3_6'
    prediction_xg = requests.get(url_xg,params=params).json()
    st.header(f'Future Price in six Month:¢/bu {(prediction_xg)}')
    

