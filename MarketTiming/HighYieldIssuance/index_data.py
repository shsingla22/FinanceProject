"""Fetch live historical index data via yfinance (Yahoo Finance).

Indices (real, live data — no assumed values):
  - ^GSPC                  : S&P 500 (USA) — full 25y+ history on Yahoo.
  - ^NSEI                  : Nifty 50 (India) — Yahoo serves data from
                             2007-09-17 onward. For the years 2001-2007 we
                             pad the Nifty 50 series using the BSE Sensex
                             (^BSESN) rescaled to the Nifty 50 level on the
                             first overlapping date, so the line is
                             continuous over the full 25y window.
  - NIFTY_MIDCAP_100.NS    : Nifty Midcap 100 (India) — Yahoo data from
                             2005-09-26 onward.
  - BSE-SMLCAP.BO          : BSE Smallcap Index (India) used as the Nifty
                             Smallcap 100 proxy. Yahoo serves the official
                             Nifty Smallcap 100 ticker (^CNXSC) only as
                             empty bars. BSE Smallcap has the longest free
                             history (from 2003-04-01) and ~95%+ rolling
                             correlation with Nifty Smallcap 100.
  - ^BSESN                 : BSE Sensex — used for the pre-2007 Nifty 50
                             back-fill and also exposed as a standalone
                             series ("sensex").
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
    "nifty_smallcap": "BSE-SMLCAP.BO",
    "sensex":         "^BSESN",
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


def fetch_nifty50_with_sensex_backfill(start: str, end: str) -> pd.Series:
    """Fetch ^NSEI but pad pre-2007 with rescaled ^BSESN so the series
    spans the full 25y window."""
    nifty = fetch_index("^NSEI", start, end)
    sensex = fetch_index("^BSESN", start, end)

    overlap = nifty.index.intersection(sensex.index)
    if len(overlap) == 0:
        return nifty  # no overlap, give up on backfill
    anchor = overlap.min()
    scale = nifty.loc[anchor] / sensex.loc[anchor]
    sensex_rescaled = sensex * scale

    backfill_mask = sensex.index < nifty.index.min()
    backfill = sensex_rescaled[backfill_mask]
    combined = pd.concat([backfill, nifty]).sort_index()
    combined = combined[~combined.index.duplicated(keep="last")]
    combined.name = "nifty50"
    return combined


def fetch_all(start: str = "2001-01-01",
              end: str | None = None) -> pd.DataFrame:
    """Fetch all five indices and return a wide DataFrame indexed by date.
    The nifty50 column is back-filled pre-2007 using a rescaled Sensex."""
    if end is None:
        end = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    series = {}
    print(f"Fetching sp500 (^GSPC) {start} -> {end} ...")
    series["sp500"] = fetch_index("^GSPC", start, end)
    print(f"Fetching sensex (^BSESN) {start} -> {end} ...")
    series["sensex"] = fetch_index("^BSESN", start, end)
    print(f"Fetching nifty50 (^NSEI, back-filled with Sensex pre-2007) ...")
    series["nifty50"] = fetch_nifty50_with_sensex_backfill(start, end)
    print(f"Fetching nifty_midcap (NIFTY_MIDCAP_100.NS) ...")
    series["nifty_midcap"] = fetch_index("NIFTY_MIDCAP_100.NS", start, end)
    print(f"Fetching nifty_smallcap (BSE-SMLCAP.BO) ...")
    series["nifty_smallcap"] = fetch_index("BSE-SMLCAP.BO", start, end)

    df = pd.concat(series, axis=1).sort_index()
    return df


def annual_year_end(df: pd.DataFrame) -> pd.DataFrame:
    """Year-end close for each index, indexed by calendar year."""
    yearly = df.resample("YE").last()
    yearly.index = yearly.index.year
    yearly.index.name = "year"
    return yearly


if __name__ == "__main__":
    df = fetch_all(start="2001-01-01")
    print("\nDaily data shape:", df.shape)
    print("Date range:", df.index.min().date(), "->", df.index.max().date())
    print("\nLast 5 rows:")
    print(df.tail().to_string())
    print("\nYear-end close per index:")
    print(annual_year_end(df).to_string())
