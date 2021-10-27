import pandas as pd
import yfinance as yf

ticker = "0P0000WLAC.F"
data = yf.download(tickers=ticker, period="5y", interval="1wk")

print(data.head())
