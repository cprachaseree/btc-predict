# Introduction
Testing RandomForestRegression to predict Bitcoin prices given Bitcoin, Ethereum, Gold, S&P500 ETF, S&P500 index, NASDAQ, Singapore Dollars

# Running The Code
## Install environment

```console
foo@bar:~$ conda create -n btc_predict python=3.10
foo@bar:~$ conda activate btc_predict
foo@bar:~$ pip install yfinance notebook scikit-learn matplotlib plotly seaborn
```

## Get Data
```console
foo@bar:~$ python scripts/get_data.py
```

## Visualize Data
```console
foo@bar:~$ jupyter notebook scripts/EDA.ipynb
```

## Train and test RMSE
```console
foo@bar:~$ jupyter notebook "scripts/Train Models.ipynb"
```

# References
