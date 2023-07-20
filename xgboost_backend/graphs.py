import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import streamlit as st



#ticker_soy ticker="ZS=F"
#ticker_corn="ZC=F"

def graph(prediction,mes,tickers):
    ticker = tickers
    data = yf.download(ticker, period="2y")
    sns.set(style="darkgrid")


    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data['Close'])
    plt.title('Soybean Futures Prices - Last 24 Months')
    plt.xlabel('Date')
    plt.ylabel('Price')


    today_date = datetime.date.today()


    prediction_date = today_date + datetime.timedelta(days=30 * mes)

    # Define the actual price and prediction value
    actual_price = data['Close'][mes*-1]
    prediction_value = prediction

# Plot a line from the last historical data point to the predicted value
    last_date = data.index[-1]
    plt.plot([last_date, prediction_date], [data['Close'].iloc[-1], prediction], 'r--')

    # Add red spot for the predicted value
    plt.scatter(prediction_date, prediction_value, color='red', label=f'{mes} Month Prediction = {prediction}')

    # Add legend
    plt.legend()
    x=plt.show()

    return x

graph(1500,3,"ZS=F")
