import matplotlib.pyplot as plt
import pandas as pd
import datetime
import yfinance as yf

#ticker_soy ticker="ZS=F"
#ticker_corn="ZC=F"

def actualprice(tickers):
    ticker = tickers
    data = yf.download(ticker, period="2y", interval="1mo")
    ld = data.index[-1]
    last_date = ld.strftime('%Y-%m-%d')
    last_price = data['Close'][-1]
    return last_price, last_date

# price, date = actualprice("ZC=F")
# print("Last Price:", price)
# print("Last Date:", date)
