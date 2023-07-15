import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Set the ticker symbol for soybean futures
ticker = "ZS=F"

# Fetch the historical data for soybean futures
data = yf.download(ticker, period="2y",interval="1mo")

# Get the last date and its corresponding price
last_date = data.index[-1]
last_price = data['Close'][-1]

# Print the last date and price
print("Last Date:", last_date)
print("Last Price:", last_price)


# Set seaborn style
sns.set(style="darkgrid")

# Plotting the closing prices
plt.figure(figsize=(10, 6))
sns.lineplot(data=data['Close'])
plt.title('Soybean Futures Prices - Last 24 Months')
plt.xlabel('Date')
plt.ylabel('Price')

# Plot blue spots for past values
plt.scatter(data.index, data['Close'], color='blue', label='Past Values')


# Calculate today's date
today_date = datetime.date.today()

# Calculate prediction date as today's date plus 1 month
prediction_date = today_date + datetime.timedelta(days=30)

# Define the prediction value
prediction_value = 1600

# Add red spot for the predicted value
plt.scatter(prediction_date, prediction_value, color='red', label='1 Month Prediction = 1600')

# Add legend
plt.legend()

plt.show()


""" # Calculate percentage difference
percentage_difference = ((prediction_value - last_price) / last_price) * 100


# Print bullish or bearish based on percentage difference
if percentage_difference > 0:
    print(f"Bullish: Percentage difference is {percentage_difference:.2f}%")
elif percentage_difference < 0:
    print(f"Bearish: Percentage difference is {percentage_difference:.2f}%") """
