import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Select the desired columns
df = df[['date', 'price_soybean', 'real_interest_rate', 'SP500', 'SOYBEANS - USA PRODUCTION [mTons]']]

## selected_columns = ['real_interest_rate', 'SP500', 'SOYBEANS - USA PRODUCTION [mTons]'] se utilizará abajo para escalar todas las features

# Rename column USA Production
df = df.rename(columns={'SOYBEANS - USA PRODUCTION [mTons]': 'usa_prod'})

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'b])

# Remove the year 2023
df = df[df['date'].dt.year != 2023]

# Select rows based on condition of date since 01-2005
df = df.loc[(df['date'] >= '2005-01-01')]

# Choose 90% of the rows randomly
df = df.sample(frac=0.9, random_state=42)

# Scale usa_prod and SP500 by minimum value
df['usa_prod'] = df['usa_prod'] / df['usa_prod'].min()
df['SP500'] = df['SP500'] / df['SP500'].min()

# Create lag columns
""" df['previous_price_soybean'] = df['price_soybean'].shift(1)
df['previous_usa_production'] = df['SOYBEANS - USA PRODUCTION [mTons]'].shift(6)
df['previous_SP500'] = df['SP500'].shift(1)
df['previous_real_interest_rate'] = df['real_interest_rate'].shift(1)
df['price_soybean_avg_3_months'] = df['price_soybean'].rolling(window=3).mean()
df['price_soybean_avg_6_months'] = df['price_soybean'].rolling(window=6).mean()
df['price_soybean_avg_12_months'] = df['price_soybean'].rolling(window=12).mean()
df['3mprevious_price_soybean'] = df['price_soybean'].shift(3)
df['3mprevious_SP500'] = df['SP500'].shift(3)
df['3mprevious_real_interest_rate'] = df['real_interest_rate'].shift(6)
df['6mprevious_price_soybean'] = df['price_soybean'].shift(6)
df['6mprevious_SP500'] = df['SP500'].shift(6)
df['6mprevious_real_interest_rate'] = df['real_interest_rate'].shift(6) """

# Function to create lag columns
# Reference: https://github.com/guptapiyush340/Soybean-Price-Prediction-Winning-solution-MinneAnalytics-Data-Science-Challenge/blob/master/XGBoost%20-%20Final%20Model.ipynb

def new_lags(data, lag_soybean_price, steps):
    ##Para 1 mes
    lag_col= ['price_soybean', 'real_interest_rate', 'SP500', 'usa_prod']
    t = 1
    data=data.assign(**{'{} (t-{})'.format(col, t): data[col].shift(+t) for col in lag_col})
    ##Para 3 y 6 meses
    lags = range(3, lag_soybean_price, steps)
    data=data.assign(**{
        '{} (t-{})'.format(col, t): data[col].shift(+t)
        for t in lags
        for col in lag_col
    })

    return data

# Instantiate the function to add the labels --> 1, 3 and 6 months
df = new_lags(df, lag_soybean_price = 7, steps = 3)

# Scale soybean prices for 1, 3 and 6 months
df['price_soybean (t-1)'] = df['price_soybean (t-1)'] / df['price_soybean (t-1)'].min()
df['price_soybean (t-3)'] = df['price_soybean (t-3)'] / df['price_soybean (t-3)'].min()
df['price_soybean (t-6)'] = df['price_soybean (t-6)'] / df['price_soybean (t-6)'].min()

# Extract month and year
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Create cyclic features using sine and cosine transformations
df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)
# df['year_sin'] = np.sin(2 * np.pi * df['year'] / df['year'].max())
# df['year_cos'] = np.cos(2 * np.pi * df['year'] / df['year'].max())

# Drop date columns
df = df.drop(columns=['date', 'month'], axis=1)

# Replace 0 values in 'price_soybean' column with the next positive value
df['price_soybean'] = df['price_soybean'].replace(0, np.nan).ffill()

# Fill null values with rolling median and backfill remaining nulls
rolling_median = df.rolling(window=12, min_periods=1).median()
df_filled = df.fillna(rolling_median)
df = df_filled.fillna(method='bfill')

# Scale selected columns using MinMaxScaler
# scaler = MinMaxScaler()
# df[selected_columns] = scaler.fit_transform(df[selected_columns])

# Check for any remaining null values
num_null_rows = df.isnull().sum(axis=1).sum()
