"""Single trusted data source: Yahoo Finance (via yfinance).

Fetches:
  - INR/USD exchange rate                              (ticker: INR=X)
  - Nifty 50                                            (^NSEI)
  - Nifty Midcap 100                                    (NIFTY_MIDCAP_100.NS)
  - Nifty Smallcap 100 proxy: BSE Smallcap              (BSE-SMLCAP.BO)
  - All current constituents of the three indices       (<SYMBOL>.NS)

The same Yahoo Finance source is used for every series in this folder
so all numbers come from one provider.

Note on data start dates (Yahoo Finance limitations):
  - INR=X                : data from Dec-2003 onward
  - ^NSEI                : data from Sep-2007 onward
  - NIFTY_MIDCAP_100.NS  : data from Sep-2005 onward
  - BSE-SMLCAP.BO        : data from Apr-2003 through May-2024
Years prior to each series' start appear as missing on the charts.
"""

from __future__ import annotations
import os
import warnings
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf

from constituents import (
    NIFTY_50, NIFTY_MIDCAP_100, NIFTY_SMALLCAP_100, to_yahoo,
)

warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(HERE, ".cache")
os.makedirs(CACHE_DIR, exist_ok=True)


def _fetch(ticker: str, start: str, end: str) -> pd.Series:
    df = yf.download(ticker, start=start, end=end,
                     progress=False, auto_adjust=True, threads=False)
    if df is None or len(df) == 0:
        return pd.Series(dtype="float64", name=ticker)
    close = df["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    close.name = ticker
    return close


def _cached_or_fetch(ticker: str, start: str, end: str) -> pd.Series:
    safe = ticker.replace("/", "_").replace("&", "and")
    path = os.path.join(CACHE_DIR, f"{safe}.csv")
    if os.path.exists(path):
        s = pd.read_csv(path, index_col=0, parse_dates=True)["close"]
        s.name = ticker
        return s
    s = _fetch(ticker, start, end)
    if len(s):
        pd.DataFrame({"close": s}).to_csv(path)
    return s


def fetch_inr_usd(start: str, end: str) -> pd.Series:
    s = _cached_or_fetch("INR=X", start, end)
    s.name = "inr_per_usd"
    return s


def fetch_indices(start: str, end: str) -> pd.DataFrame:
    n50 = _cached_or_fetch("^NSEI", start, end)
    n50.name = "nifty50"
    midcap = _cached_or_fetch("NIFTY_MIDCAP_100.NS", start, end)
    midcap.name = "nifty_midcap"
    smallcap = _cached_or_fetch("BSE-SMLCAP.BO", start, end)
    smallcap.name = "nifty_smallcap"
    return pd.concat([n50, midcap, smallcap], axis=1).sort_index()


def fetch_constituent_prices(symbols: list[str], start: str,
                             end: str) -> pd.DataFrame:
    """Return a wide DataFrame of daily close prices indexed by date,
    one column per symbol. Symbols with no data are dropped silently."""
    series = {}
    for sym in symbols:
        y = to_yahoo(sym)
        s = _cached_or_fetch(y, start, end)
        if len(s):
            series[sym] = s
    df = pd.concat(series, axis=1).sort_index()
    return df


def annual_year_end(s_or_df) -> pd.DataFrame | pd.Series:
    """Resample to year-end, indexed by integer calendar year."""
    out = s_or_df.resample("YE").last()
    out.index = out.index.year
    out.index.name = "year"
    return out


def yearly_median_of_constituents(prices: pd.DataFrame) -> pd.Series:
    """For each calendar year, return the median of all constituent
    year-end close prices (across stocks that have data that year)."""
    yearly = prices.resample("YE").last()
    yearly.index = yearly.index.year
    yearly.index.name = "year"
    med = yearly.median(axis=1, skipna=True)
    med.name = "median_close_inr"
    return med


if __name__ == "__main__":
    start = "2001-01-01"
    end = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    print("Fetching INR/USD...")
    inr = fetch_inr_usd(start, end)
    print(f"  {len(inr)} rows, "
          f"{inr.index.min().date() if len(inr) else 'NA'} -> "
          f"{inr.index.max().date() if len(inr) else 'NA'}")

    print("Fetching indices...")
    idx = fetch_indices(start, end)
    print(idx.tail().to_string())

    print("Fetching Nifty 50 constituents...")
    p50 = fetch_constituent_prices(NIFTY_50, start, end)
    print(f"  {p50.shape[1]} stocks loaded")
    print("Fetching Nifty Midcap 100 constituents...")
    pmid = fetch_constituent_prices(NIFTY_MIDCAP_100, start, end)
    print(f"  {pmid.shape[1]} stocks loaded")
    print("Fetching Nifty Smallcap 100 constituents...")
    psmall = fetch_constituent_prices(NIFTY_SMALLCAP_100, start, end)
    print(f"  {psmall.shape[1]} stocks loaded")

    print("\nMedians:")
    print(pd.concat({
        "nifty50_median":   yearly_median_of_constituents(p50),
        "midcap_median":    yearly_median_of_constituents(pmid),
        "smallcap_median":  yearly_median_of_constituents(psmall),
    }, axis=1).to_string())
