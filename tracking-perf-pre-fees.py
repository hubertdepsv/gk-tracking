# https://towardsdatascience.com/python-how-to-get-live-market-data-less-than-0-1-second-lag-c85ee280ed93

# useful packages
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

# loading data
ticker = "0P0000WLAC.F"
data = yf.download(tickers=ticker, period="5y", interval="1wk")

# slice from the investment date
df = data["2019-11-20":]

# add a performance column w.r.t. the investment date
perf = 100 * df["clot"] / df["clot"][0]
col_names = df.columns.append("perf")
df_final = pd.concat([df, perf], axis=1, names=col_names)

# TODO change to a line plot

# declare figure
fig = go.Figure()

# Candlestick
fig.add_trace(
    go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        name="market data",
    )
)

# Add titles
fig.update_layout(
    title="Gavekal China Fixed Income (Class A) NAV evolution",
    yaxis_title="NAV (EUR per Shares)",
)

# Show
fig.show()
