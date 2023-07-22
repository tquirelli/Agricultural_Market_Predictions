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


# Sidebar
st.sidebar.markdown("# Welcome to :seedling: :green[AgrIcast] :ear_of_rice:")


# Streamlit app code
last_price_soy, last_date_soy, data_soy_finance = actualprice(("ZS=F"))
last_price_corn, last_date_corn, data_corn_finance = actualprice(("ZC=F"))
ticker_soy = "ZS=F"
ticker_corn = "ZC=F"
st.title('Welcome to :seedling: :green[AgrIcast] :ear_of_rice:')
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
        prediction = round(predict_price_soybean(prediction_horizon),2)
        #st.write(f'#{str(prediction)}') #2772db ; #388e3c;
        if int(prediction) >= int(last_price_soy):
            st.subheader(f"Predicted Soybean Price for {prediction_horizon}:  :arrow_up: ")
            html_str = f"""
            <style>
            p.a {{
                font: bolder 30px sans-serif;
                color: #00b906;
                background-color: #eaeaea;
                text-align: center;
                }}
            </style>
            <p class="a">${prediction}</p>"""
        else:
            st.subheader(f"Predicted Soybean Price for {prediction_horizon}:  :arrow_down: ")
            html_str = f"""
            <style>
            p.a {{
                font: bolder 30px sans-serif;
                color: #ff0000;
                background-color: #eaeaea;
                text-align: center;
                }}
            </style>
            <p class="a"> ${round(float(prediction),2)}</p>"""
        st.markdown(html_str, unsafe_allow_html=True)
        if prediction_horizon == "1 Month":
            graph = graph_soy_1month(prediction, prediction_horizon, ticker_soy)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)
        elif prediction_horizon == "3 Months":
            prediction_1month = predict_price_soybean("1 Month")
            graph = graph_soy(prediction, prediction_horizon, ticker_soy)
            prediction_date_1month = datetime.date(2023, 6, 30) + datetime.timedelta(days=30)
            prediction_date_3months = datetime.date(2023, 6, 30) + datetime.timedelta(days=90)
            plt.scatter(prediction_date_1month, prediction_1month, color='blue', label=f'1 Month Prediction = ${round(prediction_1month)}')
            plt.legend()
            #last_date = data_soy_finance.index[-1]
            last_date = datetime.date(2023, 6, 30)
            #plt.plot([last_date, prediction_date_1month], [data_soy_finance['Close'].iloc[-1], prediction_1month], 'r-')
            plt.plot([last_date, prediction_date_1month], [last_price_soy, prediction_1month], color='gray', linestyle='dashed')
            plt.plot([prediction_date_1month, prediction_date_3months], [prediction_1month, prediction], color='gray', linestyle='dashed')
            #plt.plot([last_date, prediction_date_1month], [data_soy_finance['Close'][0], prediction_1month], 'r--')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)
        elif prediction_horizon == "6 Months":
            prediction_1month = predict_price_soybean("1 Month")
            prediction_3month = predict_price_soybean("3 Months")
            graph = graph_soy(prediction, prediction_horizon, ticker_soy)
            #prediction_date_1month = datetime.date.today() + datetime.timedelta(days=30)
            prediction_date_1month = datetime.date(2023, 6, 30) + datetime.timedelta(days=30)
            prediction_date_3months = datetime.date(2023, 6, 30) + datetime.timedelta(days=90)
            prediction_date_6months = datetime.date(2023, 6, 30) + datetime.timedelta(days=180)
            plt.scatter(prediction_date_1month, prediction_1month, color='blue', label=f'1 Month Prediction = ${round(prediction_1month)}')
            plt.scatter(prediction_date_3months, prediction_3month, color='blue', label=f'3 Months Prediction = ${round(prediction_3month)}')
            plt.legend()
            #last_date = data_soy_finance.index[-1]
            #last_date = datetime.date.today()
            last_date = datetime.date(2023, 6, 30)
            plt.plot([last_date, prediction_date_1month], [last_price_soy, prediction_1month], color='gray', linestyle='dashed')
            plt.plot([prediction_date_1month, prediction_date_3months], [prediction_1month, prediction_3month], color='gray', linestyle='dashed')
            plt.plot([prediction_date_3months, prediction_date_6months], [prediction_3month, prediction], color='gray', linestyle='dashed')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)
        else:
            print('error')


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
        prediction = round(predict_price_corn(prediction_horizon),2)
        if int(prediction) >= int(last_price_corn):
            st.subheader(f"Predicted Corn Price for {prediction_horizon}:  :arrow_up: ")
            #st.write(prediction)
            html_str = f"""
            <style>
            p.a {{
                font: bolder 30px sans-serif;
                color: #00b906;
                background-color: #eaeaea;
                text-align: center;
                }}
            </style>
            <p class="a">${round(float(prediction),2)}</p>"""
        else:
            st.subheader(f"Predicted Corn Price for {prediction_horizon}:  :arrow_down: ")
            #st.write(prediction)
            html_str = f"""
            <style>
            p.a {{
                font: bolder 30px sans-serif;
                color: #ff0000;
                background-color: #eaeaea;
                text-align: center;
                }}
            </style>
            <p class="a">${prediction}</p>"""
        st.markdown(html_str, unsafe_allow_html=True)
        if prediction_horizon == "1 Month":
            graph = graph_corn_1month(prediction, prediction_horizon, ticker_corn)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)
        elif prediction_horizon == "3 Months":
            prediction_1month = predict_price_corn("1 Month")
            graph = graph_corn(prediction, prediction_horizon, ticker_corn)
            prediction_date_1month = datetime.date(2023, 6, 30) + datetime.timedelta(days=30)
            prediction_date_3months = datetime.date(2023, 6, 30) + datetime.timedelta(days=90)
            plt.scatter(prediction_date_1month, prediction_1month, color='blue', label=f'1 Month Prediction = ${round(prediction_1month)}')
            plt.legend()
            #last_date = data_soy_finance.index[-1]
            last_date = datetime.date(2023, 6, 30)
            plt.plot([last_date, prediction_date_1month], [last_price_corn, prediction_1month], color='gray', linestyle='dashed')
            plt.plot([prediction_date_1month, prediction_date_3months], [prediction_1month, prediction], color='gray', linestyle='dashed')
            #plt.plot([last_date, prediction_date_1month], [data_soy_finance['Close'][0], prediction_1month], 'r--')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)
        elif prediction_horizon == "6 Months":
            prediction_1month = predict_price_corn("1 Month")
            prediction_3month = predict_price_corn("3 Months")
            graph = graph_corn(prediction, prediction_horizon, ticker_corn)
            prediction_date_1month = datetime.date(2023, 6, 30) + datetime.timedelta(days=30)
            prediction_date_3months = datetime.date(2023, 6, 30) + datetime.timedelta(days=90)
            prediction_date_6months = datetime.date(2023, 6, 30) + datetime.timedelta(days=180)
            plt.scatter(prediction_date_1month, prediction_1month, color='blue', label=f'1 Month Prediction = ${round(prediction_1month)}')
            plt.scatter(prediction_date_3months, prediction_3month, color='blue', label=f'3 Months Prediction = ${round(prediction_3month)}')
            plt.legend()
            #last_date = data_soy_finance.index[-1]
            last_date = datetime.date(2023, 6, 30)
            plt.plot([last_date, prediction_date_1month], [last_price_corn, prediction_1month], color='gray', linestyle='dashed')
            plt.plot([prediction_date_1month, prediction_date_3months], [prediction_1month, prediction_3month], color='gray', linestyle='dashed')
            plt.plot([prediction_date_3months, prediction_date_6months], [prediction_3month, prediction], color='gray', linestyle='dashed')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(graph)
        else:
            print('error')
else:
    st.write('Invalid Option"')
# graph_soy(prediction,mes)
