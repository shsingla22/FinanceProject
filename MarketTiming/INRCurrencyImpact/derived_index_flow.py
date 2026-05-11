"""Derive per-Nifty-index FII flow from per-stock shareholding patterns.

For each constituent stock s of Nifty index I and each quarter t:

    fii_holding_inr_t = fii_pct_t/100 × shares_outstanding × close_t

Net flow per stock for the period (t-1, t) — isolating the flow
component from the valuation component:

    flow_s_t  =  (fii_pct_t - fii_pct_t-1)/100  ×  shares  ×  avg_close

Per Nifty index per calendar year (Q4 vs prior Q4):

    flow_I_y  =  Σ_{s ∈ I}  flow_s_Q4(y)

Inputs (all REAL, all from a single source family):
  - Per-stock quarterly FII % (Tickertape API)
  - Per-stock close price (Yahoo Finance via yfinance)
  - Per-stock shares outstanding (Yahoo Finance fast_info)

Tickertape currently exposes ~6 calendar quarters per stock, so the
derived per-index flow series typically covers only one year-over-year
window (Dec-prev to Dec-current). Earlier years are NaN.
"""

from __future__ import annotations
import os
import warnings
from datetime import datetime

import pandas as pd
import yfinance as yf

from constituents import NIFTY_50, NIFTY_MIDCAP_100, NIFTY_SMALLCAP_100
from per_stock_fii import fetch_all_holdings
from fii_inflows import _fred_dexinus_yearly_avg

warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(HERE, ".cache")
SHARES_CACHE = os.path.join(CACHE_DIR, "shares_outstanding.csv")
PRICE_PANEL_CACHE = os.path.join(CACHE_DIR, "constituent_prices_panel.csv")


def _load_shares_cache() -> dict[str, float]:
    if os.path.exists(SHARES_CACHE):
        df = pd.read_csv(SHARES_CACHE)
        return {r["ticker"]: r["shares"] for _, r in df.iterrows()
                if pd.notna(r["shares"])}
    return {}


def _save_shares_cache(cache: dict[str, float]) -> None:
    rows = [{"ticker": k, "shares": v} for k, v in cache.items()
            if v is not None]
    pd.DataFrame(rows).to_csv(SHARES_CACHE, index=False)


def _fast_shares_outstanding(ticker: str,
                             cache: dict[str, float]) -> float | None:
    if ticker in cache:
        return cache[ticker]
    try:
        t = yf.Ticker(f"{ticker}.NS")
        try:
            fi = t.fast_info
            so = fi.get("shares") or fi.get("sharesOutstanding")
        except Exception:
            so = None
        if not so:
            try:
                info = t.info or {}
                so = info.get("sharesOutstanding") or info.get(
                    "impliedSharesOutstanding")
            except Exception:
                so = None
        if so:
            cache[ticker] = float(so)
            return float(so)
    except Exception:
        pass
    cache[ticker] = None
    return None


def _bulk_prices(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    """Fetch close prices for many tickers in one shot via yf.download."""
    if os.path.exists(PRICE_PANEL_CACHE):
        df = pd.read_csv(PRICE_PANEL_CACHE, index_col=0, parse_dates=True)
        if set(tickers).issubset(set(df.columns)):
            return df[tickers]
    yahoo_tickers = [f"{t}.NS" for t in tickers]
    data = yf.download(yahoo_tickers, start=start, end=end,
                       progress=False, auto_adjust=True, threads=True,
                       group_by="ticker")
    out = {}
    for t in tickers:
        try:
            s = data[f"{t}.NS"]["Close"]
        except Exception:
            continue
        out[t] = s
    df = pd.concat(out, axis=1).sort_index()
    df.to_csv(PRICE_PANEL_CACHE)
    return df


def _quarter_end_close(panel: pd.DataFrame,
                       date: pd.Timestamp) -> pd.Series:
    """Return last available close for each ticker on or before `date`."""
    sl = panel[panel.index <= date + pd.Timedelta(days=2)]
    if sl.empty:
        return pd.Series(dtype="float64")
    # forward-fill recent days to handle holidays
    return sl.ffill().iloc[-1]


def build_per_index_flows() -> pd.DataFrame:
    """Build a year-indexed DataFrame with derived per-Nifty-index net
    FII flow in INR cr and USD mn."""
    all_t = sorted(set(NIFTY_50 + NIFTY_MIDCAP_100 + NIFTY_SMALLCAP_100))

    # 1. fetch FII % per stock (Tickertape) — already cached after first run
    print(f"Loading FII holdings for {len(all_t)} constituents...")
    holdings = fetch_all_holdings(all_t)
    print(f"  {len(holdings)} stocks have shareholding data")

    # 2. collect quarter-end dates we need
    qe_dates = sorted({
        pd.to_datetime(row["quarter_end"]).tz_localize(None)
        for df in holdings.values() for _, row in df.iterrows()
    })
    if not qe_dates:
        return pd.DataFrame()
    earliest = qe_dates[0] - pd.Timedelta(days=30)
    latest   = qe_dates[-1] + pd.Timedelta(days=2)

    # 3. shares outstanding (snapshot)
    print("Fetching shares outstanding (fast_info)...")
    shares_cache = _load_shares_cache()
    tickers_in = sorted(holdings.keys())
    for i, t in enumerate(tickers_in, 1):
        _fast_shares_outstanding(t, shares_cache)
        if i % 25 == 0:
            _save_shares_cache(shares_cache)
            print(f"  ... shares fetched {i}/{len(tickers_in)}")
    _save_shares_cache(shares_cache)

    # 4. bulk close prices over the full window
    valid_tickers = [t for t in tickers_in if shares_cache.get(t)]
    print(f"Bulk-fetching close prices for {len(valid_tickers)} tickers "
          f"{earliest.date()} -> {latest.date()} ...")
    prices = _bulk_prices(
        valid_tickers,
        earliest.strftime("%Y-%m-%d"),
        latest.strftime("%Y-%m-%d"),
    )

    # 5. assemble per-stock quarterly panel
    panel_rows = []
    for ticker, hold_df in holdings.items():
        sh = shares_cache.get(ticker)
        if not sh:
            continue
        if ticker not in prices.columns:
            continue
        for _, row in hold_df.iterrows():
            qe = pd.to_datetime(row["quarter_end"]).tz_localize(None)
            fii_pct = row["fii_pct"]
            if pd.isna(fii_pct):
                continue
            ce = _quarter_end_close(prices[[ticker]], qe)
            if ticker not in ce or pd.isna(ce[ticker]):
                continue
            panel_rows.append({
                "ticker":     ticker,
                "quarter_end": qe,
                "fii_pct":    float(fii_pct),
                "close":      float(ce[ticker]),
                "shares":     float(sh),
            })
    panel = pd.DataFrame(panel_rows)
    panel["fii_holding_inr"] = (
        panel["fii_pct"] / 100.0 * panel["shares"] * panel["close"]
    )
    panel["year"] = panel["quarter_end"].dt.year
    panel["month"] = panel["quarter_end"].dt.month
    print(f"Panel: {len(panel)} (ticker, quarter) rows across "
          f"{panel['quarter_end'].nunique()} quarters")

    # 6. annual flow per Nifty index — Q4 vs prior Q4
    def _index_flow(members: list[str]) -> pd.Series:
        sub = panel[panel["ticker"].isin(members) & (panel["month"] == 12)]
        if sub.empty:
            return pd.Series(dtype="float64")
        sub = sub.sort_values(["ticker", "year"]).copy()
        sub["fii_pct_prev"] = sub.groupby("ticker")["fii_pct"].shift(1)
        sub["close_prev"]   = sub.groupby("ticker")["close"].shift(1)
        sub = sub.dropna(subset=["fii_pct_prev", "close_prev"])
        if sub.empty:
            return pd.Series(dtype="float64")
        sub["avg_price"]   = (sub["close"] + sub["close_prev"]) / 2.0
        sub["share_delta"] = (sub["fii_pct"] - sub["fii_pct_prev"]) / 100.0 \
                              * sub["shares"]
        sub["flow_inr"]    = sub["share_delta"] * sub["avg_price"]
        return sub.groupby("year")["flow_inr"].sum()

    flow_50  = _index_flow(NIFTY_50)
    flow_mid = _index_flow(NIFTY_MIDCAP_100)
    flow_sm  = _index_flow(NIFTY_SMALLCAP_100)

    out = pd.DataFrame({
        "fii_flow_nifty50_inr_cr":  flow_50  / 1e7,
        "fii_flow_midcap_inr_cr":   flow_mid / 1e7,
        "fii_flow_smallcap_inr_cr": flow_sm  / 1e7,
    })
    out.index.name = "year"

    # 7. USD conversion (FRED DEXINUS yearly avg)
    inr = _fred_dexinus_yearly_avg()
    out = out.join(inr, how="left")
    rate = out["inr_per_usd_yearly_avg"]
    for col in [
        "fii_flow_nifty50_inr_cr",
        "fii_flow_midcap_inr_cr",
        "fii_flow_smallcap_inr_cr",
    ]:
        usd_col = col.replace("_inr_cr", "_usd_mn")
        out[usd_col] = out[col] * 1e7 / rate / 1e6
    return out


if __name__ == "__main__":
    df = build_per_index_flows()
    print(df.to_string())
