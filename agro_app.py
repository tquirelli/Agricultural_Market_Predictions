import streamlit as st
from model import predict

year = st.text_input("Year","")


st.text(predict(year))

print("viva la patria")
