import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import streamlit as st

# Set the ticker symbol for soybean futures
ticker = "ZS=F"

# Fetch the historical data for soybean futures
data = yf.download(ticker, period="2y")

# Set seaborn style
sns.set(style="darkgrid")

# Plotting the closing prices
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
actual_price = data['Close'][-1]
prediction_value = 1600

# Calculate percentage difference
percentage_difference = ((prediction_value - actual_price) / actual_price) * 100

# Add red spot for the predicted value
plt.scatter(prediction_date, prediction_value, color='red', label='1 Month Prediction = 1600')

# Add legend
plt.legend()

plt.show()

""" # Print bullish or bearish based on percentage difference
if percentage_difference > 0:
    st.write(f"Bullish: Percentage difference is {percentage_difference:.2f}%")
elif percentage_difference < 0:
    st.write(f"Bearish: Percentage difference is {percentage_difference:.2f}%")

# Display the graph using Streamlit
st.pyplot(plt) """
