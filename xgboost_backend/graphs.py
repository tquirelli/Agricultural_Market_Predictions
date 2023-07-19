import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import streamlit as st

def graph_soy(prediction,mes):
    ticker = "ZS=F"
    data = yf.download(ticker, period="2y")
    sns.set(style="darkgrid")


    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data['Close'])
    plt.title('Soybean Futures Prices - Last 24 Months')
    plt.xlabel('Date')
    plt.ylabel('Price')

    # Calculate today's date
    today_date = datetime.date.today()

    # Calculate prediction date as today's date plus 1 month
    prediction_date = today_date + datetime.timedelta(days=30)

    # Define the actual price and prediction value
    actual_price = data['Close'][mes*-1]
    prediction_value = prediction



    # Add red spot for the predicted value
    plt.scatter(prediction_date, prediction_value, color='red', label=f'{mes} Month Prediction = {prediction}')

    # Add legend
    plt.legend()
    x=plt.show()

    return x
