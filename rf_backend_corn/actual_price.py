import matplotlib.pyplot as plt
import pandas as pd
import datetime
import yfinance as yf

#ticker_soy ticker="ZS=F"
#ticker_corn="ZC=F"
def actualprice(tickers):
    ticker = tickers

    # Fetch the historical data for soybean futures
    data = yf.download(ticker, period="2y",interval="1mo")

    # Get the last date and its corresponding price
    ld = data.index[-1]

    last_date = ld.strftime('%Y-%m-%d')

    last_price = data['Close'][-1]

    return last_price, last_date


print(actualprice("ZC=F"))


#def actualprice(tickers, target_date="2023-06-30"):
    #   ticker = tickers
    # Fetch the historical data for soybean futures
    #data = yf.download(ticker, period="2y",interval="1mo")
    #data = yf.download(ticker, start=target_date, end=target_date)
    # Get the last date and its corresponding price
    #ld = data.index[-1]
    #last_date = ld.strftime('%Y-%m-%d')
    #last_price = data['Close'][-1]
    #data = yf.download(ticker, start=target_date, end=target_date)
    #if data.empty:
        #target_date = datetime.strptime(target_date, '%Y-%m-%d')
        #data = yf.download(ticker, start=target_date)
    # Get the last date and its corresponding price
    #ld = data.index[0]
    #last_date = ld.strftime('%Y-%m-%d')
    #last_price = data['Close'][0]z

    #return last_price, last_date
