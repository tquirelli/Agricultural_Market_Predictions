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

    return last_price, last_date, data


print(actualprice("ZC=F"))
