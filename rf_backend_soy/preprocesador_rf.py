import pandas as pd
import numpy as np

def all_preprocessor(df) -> pd.DataFrame:
    # Select the desired columns
    df = df.rename(columns={'SOYBEANS - USA PRODUCTION [mTons]': 'usa_prod'})
    df = df[['date', 'price_soybean', 'real_interest_rate', 'SP500', 'usa_prod']]

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date']).dt.to_period('M')
    df.set_index(["date"],inplace=True)
    # Add lagged values
    df2 = df.copy()
    for i in range(1, 13):
        df2[f'x_{i}'] = df["price_soybean"].shift(i)


    # Extract the trend using a well-chosen moving average
    df2['ma_6'] = df2['price_soybean'].shift(1).rolling(window=6).mean()
    df2['ma_3'] = df2['price_soybean'].shift(1).rolling(window=3).mean()
    df2['ma_2'] = df2['price_soybean'].shift(1).rolling(window=2).mean()

    # Moving average with halflife
    df2["ewma_2"] = df2["price_soybean"].shift(1).ewm(halflife=2).mean()
    df2["ewma_3"] = df2["price_soybean"].shift(1).ewm(halflife=3).mean()
    df2["ewma_6"] = df2["price_soybean"].shift(1).ewm(halflife=6).mean()

    #Drop nan by eliminating first 12 months
    df2=df2[df2.index >= "1989-07-01"]

    return df2
