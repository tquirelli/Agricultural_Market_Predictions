import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import streamlit as st

def graph_soy_1month(prediction,mes, ticker):
    ticker = "ZS=F"
    data = yf.download(ticker, period="2y", interval='1d')
    data = data[data.index <= "2023-06-30"]
    sns.set(style="darkgrid")


    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data['Close'])
    plt.title('Soybean Futures Prices - Last 24 Months')
    plt.xlabel('Date')
    plt.ylabel('Price')

    # Calculate today's date
    #today_date = datetime.date.today()
    today_date = datetime.date(2023, 6, 30)

    # Calculate prediction date as today's date plus 1 month

    prediction_date = today_date + datetime.timedelta(days=30)

    # Define the actual price and prediction value
    # actual_price = data['Close'][mes*-1]
    prediction_value = round(prediction)

    # Plot a line from the last historical data point to the predicted value
    #last_date = data.index[-1]
    last_date = datetime.date(2023, 6, 30)
    plt.plot([last_date, prediction_date], [data['Close'].iloc[-1], prediction], color='gray', linestyle='dashed')



    # Add red spot for the predicted value
    mean_price = data['Close'].mean()
    plt.axhline(mean_price, color='gray', linestyle='dashed', label='Mean price 2 years')
    plt.scatter(prediction_date, prediction_value, color='red', label=f'{mes} Prediction = ${prediction_value}')
    #plt.axhline(y=prediction_value, color='gray', linestyle='dashed', alpha=0.5)


    # Add legend
    plt.legend()
    x=plt.show()

    return x
