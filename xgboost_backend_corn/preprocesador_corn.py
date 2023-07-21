import pandas as pd
import numpy as np


def new_lags(data, lag_soybean_price, steps):
    ##Para 1 mes
    lag_col= ['price_corn', 'real_interest_rate', 'SP500', 'usa_corn_prod']
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

def all_preprocessor_xgb_corn(df) -> pd.DataFrame:
    # Select the desired columns
    df = df[['date', 'price_corn', 'real_interest_rate', 'SP500', 'usa_corn_prod']]

    ## selected_columns = ['real_interest_rate', 'SP500', 'SOYBEANS - USA PRODUCTION [mTons]'] se utilizará abajo para escalar todas las features

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Remove the year 2023
    # df = df[df['date'].dt.year != 2023]

    # Select rows based on condition of date since 01-2005
    df = df.loc[(df['date'] >= '2008-01-01')]

    # Choose 90% of the rows randomly
    # df = df.sample(frac=0.9, random_state=42)

    # Scale usa_prod and SP500 by minimum value
    df['usa_corn_prod'] = df['usa_corn_prod'] / df['usa_corn_prod'].min()
    df['SP500'] = df['SP500'] / df['SP500'].min()


    # Instantiate the function to add the labels --> 1, 3 and 6 months
    df = new_lags(df, lag_soybean_price = 7, steps = 3)

    # Scale soybean prices for 1, 3 and 6 months
    df['price_corn (t-1)'] = df['price_corn (t-1)'] / df['price_corn (t-1)'].min()
    df['price_corn (t-3)'] = df['price_corn (t-3)'] / df['price_corn (t-3)'].min()
    df['price_corn (t-6)'] = df['price_corn (t-6)'] / df['price_corn (t-6)'].min()

    # Extract month and year
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    # Create cyclic features using sine and cosine transformations
    df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
    df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

    # Drop date columns
    date_column = df['date']
    df = df.drop(columns=['date', 'month'], axis=1)

    # Fill null values with rolling median and backfill remaining nulls
    rolling_median = df.rolling(window=12, min_periods=1).median()
    df_filled = df.fillna(rolling_median)
    df = df_filled.fillna(method='bfill')

    num_null_rows = df.isnull().sum(axis=1).sum()

    # Reinsert date column
    df['date'] = date_column

    # To save the dataframe in the dataser folder
    #df.to_csv("Agricultural_data/scaled_data.csv", index=False)

    return df

def all_preprocessor_train_xgb_corn(df) -> pd.DataFrame:
    # Select the desired columns
    df = df[['date', 'price_corn', 'real_interest_rate', 'SP500', 'usa_corn_prod']]

    ## selected_columns = ['real_interest_rate', 'SP500', 'SOYBEANS - USA PRODUCTION [mTons]'] se utilizará abajo para escalar todas las features

    # Rename column USA Production
    #df = df.rename(columns={'SOYBEANS - USA PRODUCTION [mTons]': 'usa_prod'})

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Remove the year 2023
    df = df[df['date'].dt.year != 2023]

    # Select rows based on condition of date since 01-2005
    df = df.loc[(df['date'] >= '2008-01-01')]

    # Choose 90% of the rows randomly
    # df = df.sample(frac=0.9, random_state=42)

    # Scale usa_prod and SP500 by minimum value
    df['usa_corn_prod'] = df['usa_corn_prod'] / df['usa_corn_prod'].min()
    df['SP500'] = df['SP500'] / df['SP500'].min()


    # Instantiate the function to add the labels --> 1, 3 and 6 months
    df = new_lags(df, lag_soybean_price = 7, steps = 3)

    # Scale soybean prices for 1, 3 and 6 months
    df['price_corn (t-1)'] = df['price_corn (t-1)'] / df['price_corn (t-1)'].min()
    df['price_corn (t-3)'] = df['price_corn (t-3)'] / df['price_corn (t-3)'].min()
    df['price_corn (t-6)'] = df['price_corn (t-6)'] / df['price_corn (t-6)'].min()

    # Extract month and year
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    # Create cyclic features using sine and cosine transformations
    df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
    df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

    # Drop date columns
    date_column = df['date']
    df = df.drop(columns=['date', 'month'], axis=1)

    # Fill null values with rolling median and backfill remaining nulls
    rolling_median = df.rolling(window=12, min_periods=1).median()
    df_filled = df.fillna(rolling_median)
    df = df_filled.fillna(method='bfill')

    num_null_rows = df.isnull().sum(axis=1).sum()

    # Reinsert date column
    df['date'] = date_column

    # To save the dataframe in the dataser folder
    # df.to_csv("Agricultural_data/scaled_data.csv", index=False)

    return df