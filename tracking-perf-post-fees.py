# https://towardsdatascience.com/python-how-to-get-live-market-data-less-than-0-1-second-lag-c85ee280ed93

# Line graph of the fund's post-fees performance since the investment date

# useful packages
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px

# loading data
ticker = "0P0000WLAC.F"
data = yf.download(tickers=ticker, period="5y", interval="1d")

data.drop(data.columns[[0, 1, 2, 4, 5]], axis=1, inplace=True)

# slice from the investment date
df = data["2019-11-20":]

# compute performance columns
post_fee_price = 165.00396
df.loc[:, "post_fee_perf"] = 100 * df.loc[:, "Close"] / post_fee_price

fig = px.line(df, x=df.index, y="post_fee_perf")

fig.update_layout(
    title="Gavekal China Fixed Income post-fees performance since investment date",
    xaxis_title="Date",
    yaxis_title="Performance (%)",
)
fig.update_layout(
    shapes=[
        dict(
            type="line",
            yref="y",
            y0=100,
            y1=100,  # adding a horizontal line at Y = 1
            xref="paper",
            x0=0,
            x1=1,
        )
    ]
)
fig.update_xaxes(rangeslider_visible=True)

fig.show()
