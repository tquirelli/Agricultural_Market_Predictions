import streamlit as st
import os
from PIL import Image
from model import predict_price_soybean, predict_price_corn
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from xgboost_backend_soybean.actual_price import actualprice
from xgboost_backend_soybean.graphs import graph_soy
from xgboost_backend_corn.graphs import graph_corn
from rf_backend_corn.graphs import graph_corn_1month
from rf_backend_soy.graphs import graph_soy_1month



st.markdown("# About :green[AgrIcast] :seedling:")
st.sidebar.markdown("# About :green[AgrIcast] :seedling:")
st.sidebar.markdown('<a href="https://github.com/tquirelli/Agricultural_Market_Predictions" target="_self" style="color: black; border: 2px solid green; text-decoration: none; padding: 5px 10px; background-color: lightgreen; border-radius: 5px;"><b>Our GitHub https://github.com/tquirelli/Agricultural_Market_Predictions</b></a>', unsafe_allow_html=True)
st.subheader('_ML applied to predict future prices of the main agricultural commodities in the region_')


# Text
st.write('The following project was born with the intention of offering a tool or platform for users who need to know '
         'the trend that soybean and corn commodities will have in the coming months. They can access these values and '+
         'make data-driven decisions, adding value to their business or activity. ')

st.write('The goal is to predict the prices of agricultural products using machine learning tools and data analysis, '+
         'obtaining highly useful forecasts for farmers, traders, and market participants. The 3 target prediction horizons '+
         'are 1, 3, and 6 months.')
image = Image.open('pages/project.png')
st.image(image, caption='Project Description')

st.subheader('Data Collection :mag_right:')
st.write('Our sources for collecting data were:')
st.write(':small_blue_diamond: TraidingView Platform')
st.write(':small_blue_diamond: USDA: United States Department of Agriculture')
image = Image.open('pages/features.png')
st.image(image, caption='Data Collection')

st.subheader('Data Cleaning and Data Preparation :bulb:')
st.write('After the tasks of data collection and cleaning, we performed a comprehensive analysis of the different '+
         'variables and selected the important ones that significantly influence and have a strong correlation with '+
         'each other. The selected variables include:')
st.write(':small_blue_diamond: Historical prices of commodities')
st.write(':small_blue_diamond: Moving averages of historical prices')
st.write(':small_blue_diamond: SP 500')
st.write(':small_blue_diamond: USA Production')
st.write(':small_blue_diamond: Real interest rate USA')
image = Image.open('pages/process.png')
st.image(image, caption='Data Cleaning and Data Preparation')

st.subheader('Model Training :computer:')
st.write('Based on the preceding steps and in line with the proposed objectives (horizons and type of prediction), '+
         'we carried out tests and training of different predictive models, seeking those that achieve the best '+
         'performance and metrics, while considering techniques to prevent overfitting and data leakage.')
st.write('The selected models are:')
st.write(':small_blue_diamond: For the 1-month predictive horizon: :green[RandomForest]')
st.write(':small_blue_diamond: For the 3 and 6-month predictive horizons: :green[XGBoost]')
image = Image.open('pages/models.png')
st.image(image, caption='Models Training')

st.subheader('Performance Evaluation and Metrics :chart_with_downwards_trend:')
st.write('We conducted performance evaluations and calculated various metrics to validate the accuracy of the selected models.')
st.write('The obtained results are shown below:')
image = Image.open('pages/result1.png')
st.image(image, caption='Comparison of actual and predicted prices for a 1-month time horizon')
image = Image.open('pages/result2.png')
st.image(image, caption='Comparison of actual and predicted prices for time horizons of 3 and 6 months, respectively')


st.subheader('Deployment and User Interface :rocket:')
st.write('For our project, we used Streamlit, a Python library that allows us to deploy and put our model into use in a very simple way.')



st.subheader('Our team :busts_in_silhouette:')
image = Image.open('pages/team.png')
st.image(image, caption='The team')

st.subheader('We invite you to visualize and enjoy :mortar_board:')
st.write('GitHub: https://github.com/tquirelli/Agricultural_Market_Predictions')
st.write('Streamlit: https://agriculturalmarketpredictions-project.streamlit.app/About_the_project')
