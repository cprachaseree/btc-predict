import os
import numpy as np
import pandas as pd
from datetime import datetime
import yfinance as yf

cur_script_path = os.path.abspath(os.path.dirname(__file__))

data_path = os.path.join(cur_script_path, "..", "data")

def get_data():
    # get data
    tickers = 'BTC-USD ETH-USD GLD SPY ^GSPC ^IXIC SGD=X'
    period="60d"
    #start, end = "2023-01-20", ""
    interval = "15m"
    #now = datetime.now()
    #dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
    if period:
        data = yf.download(tickers=tickers, period=period,
                        interval=interval, prepost=False,)
        tickers = "_".join(tickers.split())
    else:
        data = yf.download(tickers=tickers, start=start,
                        interval=interval, prepost=False,)
    
    return data
# start_date="2023-01-20 9:30:00"
def trim_data(data):
    data = data.replace('', np.nan).ffill()
    print(data.head())
    print(data.index)
    print(data['Adj Close']['BTC-USD'])
    vi = data['Adj Close']['BTC-USD'].first_valid_index()
    print("vi:", vi)
    data = data[vi:]
    return data

def split_data(data):
    split_data_len = int(len(data) * 0.9)
    data["Next Close"] = data[('Close', 'BTC-USD')].shift(-1)
    train = data.iloc[:split_data_len]
    test = data.iloc[split_data_len:]
    train.to_csv(os.path.join(data_path, 'train.csv'), index=False)
    test.to_csv(os.path.join(data_path, 'test.csv'), index=False)

def main():
    data = get_data()
    data = trim_data(data)
    data.reset_index(inplace=True)
    data.to_csv(os.path.join(data_path, 'data.csv'), index=False)
    split_data(data)
    return data

if __name__ == "__main__":
    main()
