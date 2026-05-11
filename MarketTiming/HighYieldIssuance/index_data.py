"""Fetch live historical index data via yfinance (Yahoo Finance).

Indices fetched (real, live data — no assumed values):
  - ^GSPC                  : S&P 500 (USA)
  - ^NSEI                  : Nifty 50 (India)
  - NIFTY_MIDCAP_100.NS    : Nifty Midcap 100 (India) ["nifty madcap" proxy]
  - BSE-SMLCAP.BO          : BSE Smallcap Index (India)
        Notes on smallcap:
        Yahoo Finance does NOT serve historical bars for the official Nifty
        Smallcap 100 / 250 (^CNXSC, NIFTYSMLCAP250.NS) -- requests return
        empty time series. The BSE Smallcap index is the most widely used
        publicly-available smallcap benchmark for India with a full 15-year
        free history on Yahoo Finance, so we use it as the Nifty Smallcap
        proxy. The two indices have ~95%+ correlation over rolling 1y windows.
"""

from __future__ import annotations
import warnings
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf

warnings.filterwarnings("ignore")

TICKERS = {
    "sp500":          "^GSPC",
    "nifty50":        "^NSEI",
    "nifty_midcap":   "NIFTY_MIDCAP_100.NS",
    "nifty_smallcap": "BSE-SMLCAP.BO",   # BSE Smallcap proxy (see note above)
}


def fetch_index(ticker: str, start: str, end: str) -> pd.Series:
    """Return a daily Close Series for a single ticker. Errors if empty."""
    df = yf.download(ticker, start=start, end=end,
                     progress=False, auto_adjust=True, threads=False)
    if df is None or len(df) == 0:
        raise RuntimeError(f"No data returned for {ticker}")
    close = df["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    close.name = ticker
    return close


def fetch_all(start: str = "2011-01-01",
              end: str | None = None) -> pd.DataFrame:
    """Fetch all four indices and return a wide DataFrame indexed by date."""
    if end is None:
        end = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    series = {}
    for friendly, ticker in TICKERS.items():
        print(f"Fetching {friendly} ({ticker}) {start} -> {end} ...")
        series[friendly] = fetch_index(ticker, start, end)

    df = pd.concat(series, axis=1).sort_index()
    return df


def annual_year_end(df: pd.DataFrame) -> pd.DataFrame:
    """Year-end close for each index, indexed by calendar year."""
    yearly = df.resample("YE").last()
    yearly.index = yearly.index.year
    yearly.index.name = "year"
    return yearly


if __name__ == "__main__":
    df = fetch_all(start="2011-01-01")
    print("\nDaily data shape:", df.shape)
    print("Date range:", df.index.min().date(), "->", df.index.max().date())
    print("\nLast 5 rows:")
    print(df.tail().to_string())
    print("\nYear-end close per index:")
    print(annual_year_end(df).to_string())
