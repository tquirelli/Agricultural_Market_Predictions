import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import streamlit as st

def graph_soy(prediction,mes, ticker):

    data = yf.download(ticker, period="2y")
    sns.set(style="darkgrid")


    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data['Close'])
    plt.title('Soybean Futures Prices - Last 24 Months')
    plt.xlabel('Date')
    plt.ylabel('Price')

    # Calculate today's date
    today_date = datetime.date.today()
    # Start = datetime.date.today() - datetime.timedelta(365)

    # Calculate prediction date as today's date plus 1 month
    if mes == '3 Months':
        prediction_date = today_date + datetime.timedelta(days=90)
    else:
        prediction_date = today_date + datetime.timedelta(days=180)

    # Define the actual price and prediction value
    # actual_price = data['Close'][mes*-1]
    prediction_value = round(prediction, 2)



    # Add red spot for the predicted value
    mean_price = data['Close'].mean()
    plt.axhline(mean_price, color='gray', linestyle='dashed', label='Mean price 2 years')
    plt.scatter(prediction_date, prediction_value, color='red', label=f'{mes} Month Prediction = {round(int(prediction_value))}')
    #plt.axhline(y=prediction_value, color='gray', linestyle='dashed', alpha=0.5)




    # Add legend
    plt.legend()
    x=plt.show()

    return x
