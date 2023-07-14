import streamlit as st
from model import predict_price

# Streamlit app code
st.title("Soybean Price Prediction")

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
