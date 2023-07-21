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



st.markdown("# About :seedling: :green[A]gr:green[I]cast")
st.sidebar.markdown("# About ❄️")

# Streamlit app code

#st.title('Welcome to :seedling: :green[AgrIcast] :ear_of_rice:')
