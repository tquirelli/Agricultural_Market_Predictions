import streamlit as st
from model import predict_price_soybean, predict_price_corn
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from xgboost_backend_soybean.actual_price import actualprice
from xgboost_backend_soybean.graphs import graph_soy
from xgboost_backend_corn.graphs import graph_corn
from rf_backend_corn.graphs import graph_corn_1month
from rf_backend_soy.graphs import graph_soy_1month
##last_price, last_date

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    #layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "## This is a header. This is an *extremely* cool app!"
    }
)

# Streamlit app code
last_price_soy, last_date_soy, data_soy_finance = actualprice(("ZS=F"))
last_price_corn, last_date_corn, data_corn_finance = actualprice(("ZC=F"))
ticker_soy = "ZS=F"
ticker_corn = "ZC=F"
st.title('Welcome to :green[AgrIcast] :seedling::ear_of_rice:')
st.header("Choose an option to predict the price")
#btn = st.button("Press Me")

page_names = ['Soybean Price', 'Corn Price']
page = st.radio('Navigation', page_names)
if page == 'Soybean Price':
    st.header("Soybean Price Prediction")
    st.header(f'_Last_ _month_ _price_ _from_ {last_date_soy} _is_ $*{int(last_price_soy)}*')

    if st.button("1 Month"):
        prediction_horizon = "1 Month"

    if st.button("3 Months"):
        prediction_horizon = "3 Months"

    if st.button("6 Months"):
        prediction_horizon = "6 Months"

    # Predict and display the message if a time horizon is selected
    if 'prediction_horizon' in locals():
        prediction = predict_price_soybean(prediction_horizon)
        st.subheader(f"Predicted Soybean Price for {prediction_horizon}:")
        #st.write(f'#{str(prediction)}') #2772db;
        html_str = f"""
        <style>
        p.a {{
            font: bolder 30px sans-serif;
            color: #388e3c;
            background-color: #eaeaea;
            text-align: center;
            }}
        </style>
        <p class="a">{prediction}</p>"""
        st.markdown(html_str, unsafe_allow_html=True)
        if prediction_horizon == "1 Month":
            graph = graph_soy_1month(prediction, prediction_horizon, ticker_soy)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)
        elif prediction_horizon == "3 Months":
            prediction_1month = predict_price_soybean("1 Month")
            graph = graph_soy(prediction, prediction_horizon, ticker_soy)
            prediction_date = datetime.date.today() + datetime.timedelta(days=30)
            plt.scatter(prediction_date, prediction_1month, color='blue', label=f'1 Month Prediction = ${prediction_1month}')
            last_date = data_soy_finance.index[-1]
            plt.plot([last_date, prediction_date], [data_soy_finance['Close'].iloc[-1], prediction], 'r--')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)

elif page == 'Corn Price':
    st.header("Corn Price Prediction")
    st.header(f'Last month price from {last_date_corn} is ${int(last_price_corn)}')

    if st.button("1 Month"):
        prediction_horizon = "1 Month"

    if st.button("3 Months"):
        prediction_horizon = "3 Months"

    if st.button("6 Months"):
        prediction_horizon = "6 Months"

    # Predict and display the message if a time horizon is selected
    if 'prediction_horizon' in locals():
        prediction = predict_price_corn(prediction_horizon)
        st.subheader(f"Predicted Corn Price for {prediction_horizon}:")
        #st.write(prediction)
        html_str = f"""
        <style>
        p.a {{
            font: bolder 30px sans-serif;
            color: #2772db;
            background-color: #eaeaea;
            text-align: center;
            }}
        </style>
        <p class="a">{prediction}</p>"""
        st.markdown(html_str, unsafe_allow_html=True)
        if prediction_horizon == "1 Month":
            graph = graph_corn_1month(prediction, prediction_horizon, ticker_corn)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)
        else:
            graph = graph_corn(prediction, prediction_horizon, ticker_corn)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)
else:
    st.write('Invalid Option"')
# graph_soy(prediction,mes)
