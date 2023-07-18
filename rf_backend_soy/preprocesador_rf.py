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


    #Drop nan by eliminating first 12 months
    df2=df2[df2.index >= "1989-07-01"]
    
    return df2
