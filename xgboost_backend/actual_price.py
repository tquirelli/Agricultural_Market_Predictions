import matplotlib.pyplot as plt
import pandas as pd
import datetime
import yfinance as yf

# Set the ticker symbol for soybean futures
ticker = "ZS=F"

# Fetch the historical data for soybean futures
data = yf.download(ticker, period="2y",interval="1mo")

# Get the last date and its corresponding price
ld = data.index[-1]

last_date = ld.strftime('%Y-%m-%d')

last_price = data['Close'][-1]

def last_p(last_price):
    y=print(last_price)

    return y

def last_d(last_date):
    y=print(last_date)

    return y
