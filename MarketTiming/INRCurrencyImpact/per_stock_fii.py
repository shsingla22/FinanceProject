"""Per-stock FII shareholding pattern from Tickertape (single source).

Tickertape exposes per-stock quarterly Foreign Institutional ownership %
via its public API. For each NSE ticker we:

1. Resolve the Tickertape `sid` via the search API:
       https://www.tickertape.in/stocks/search?text=<NSE_TICKER>
2. Fetch the quarterly shareholding history:
       https://api.tickertape.in/stocks/holdings/<sid>
   The response contains an array of {date, data.fiPctT} entries (last
   ~6 calendar quarters). `fiPctT` is the Foreign-Institutions percent
   of total shares outstanding.

These two endpoints are the single source for the per-stock FII
ownership % series used to derive per-Nifty-index FII flow.

Results are cached to .cache/ as CSV per stock so reruns don't hit the
API repeatedly.
"""

from __future__ import annotations
import json
import os
import time
import urllib.request
import urllib.parse
from typing import Optional

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(HERE, ".cache")
SID_CACHE = os.path.join(CACHE_DIR, "tickertape_sids.json")
HOLDINGS_DIR = os.path.join(CACHE_DIR, "tickertape_holdings")
os.makedirs(HOLDINGS_DIR, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
TICKERTAPE_HEADERS = {
    "User-Agent": UA,
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.tickertape.in",
    "Referer": "https://www.tickertape.in/",
}


def _http_json(url: str, retries: int = 4) -> dict:
    import time as _time
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=TICKERTAPE_HEADERS)
            with urllib.request.urlopen(req, timeout=20) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            last_err = e
            # back off on transient errors (502/503/connection)
            _time.sleep(2 * (attempt + 1))
    raise last_err if last_err else RuntimeError("HTTP failed")


def _load_sid_cache() -> dict:
    if os.path.exists(SID_CACHE):
        with open(SID_CACHE) as f:
            return json.load(f)
    return {}


def _save_sid_cache(d: dict) -> None:
    with open(SID_CACHE, "w") as f:
        json.dump(d, f, indent=2, sort_keys=True)


def resolve_sid(nse_ticker: str, cache: Optional[dict] = None) -> Optional[str]:
    """Map an NSE ticker (e.g. 'RELIANCE') to its Tickertape sid (e.g. 'RELI')."""
    if cache is not None and nse_ticker in cache:
        return cache[nse_ticker]
    try:
        url = (
            "https://api.tickertape.in/stocks/search?"
            + urllib.parse.urlencode({"text": nse_ticker})
        )
        data = _http_json(url)
        results = (data.get("data") or {}).get("searchResults", [])
        for s in results:
            info = (s.get("stock") or {}).get("info", {})
            t = info.get("ticker") or ""
            ex = info.get("exchange") or ""
            if t == nse_ticker and ex.upper() == "NSE":
                sid = s.get("sid")
                if cache is not None:
                    cache[nse_ticker] = sid
                return sid
        # fallback: take first result
        if results:
            sid = results[0].get("sid")
            if cache is not None:
                cache[nse_ticker] = sid
            return sid
    except Exception as e:
        print(f"  resolve_sid({nse_ticker}) ERR: {e}")
    return None


def fetch_holdings(sid: str) -> pd.DataFrame:
    """Return DataFrame with columns ['quarter_end', 'fii_pct',
    'mf_pct', 'di_pct', 'promoter_pct']."""
    path = os.path.join(HOLDINGS_DIR, f"{sid}.csv")
    if os.path.exists(path):
        return pd.read_csv(path, parse_dates=["quarter_end"])
    try:
        url = f"https://api.tickertape.in/stocks/holdings/{sid}"
        data = _http_json(url)
        rows = []
        for entry in data.get("data") or []:
            d = entry.get("data") or {}
            rows.append({
                "quarter_end": pd.to_datetime(entry["date"]).tz_localize(None),
                "fii_pct":      d.get("fiPctT"),
                "mf_pct":       d.get("mfPctT"),
                "di_pct":       d.get("diPctT"),
                "promoter_pct": d.get("pmPctT"),
            })
        df = pd.DataFrame(rows)
        df.to_csv(path, index=False)
        return df
    except Exception as e:
        print(f"  fetch_holdings({sid}) ERR: {e}")
        return pd.DataFrame()


def fetch_all_holdings(nse_tickers: list[str]) -> dict[str, pd.DataFrame]:
    """Fetch FII shareholding history for every NSE ticker in the list."""
    sid_cache = _load_sid_cache()
    out: dict[str, pd.DataFrame] = {}
    for i, t in enumerate(nse_tickers, 1):
        sid = resolve_sid(t, cache=sid_cache)
        if sid is None:
            continue
        df = fetch_holdings(sid)
        if len(df):
            out[t] = df
        time.sleep(0.4)  # gentle pace to avoid rate limit
        if i % 25 == 0:
            _save_sid_cache(sid_cache)
            print(f"  ... fetched {i}/{len(nse_tickers)} stocks "
                  f"({len(out)} with data)")
    _save_sid_cache(sid_cache)
    return out


if __name__ == "__main__":
    from constituents import NIFTY_50, NIFTY_MIDCAP_100, NIFTY_SMALLCAP_100
    all_tickers = sorted(set(NIFTY_50 + NIFTY_MIDCAP_100 + NIFTY_SMALLCAP_100))
    print(f"Resolving and fetching holdings for {len(all_tickers)} tickers...")
    holdings = fetch_all_holdings(all_tickers)
    print(f"\nLoaded FII holdings for {len(holdings)} stocks.")
    # Sample
    if holdings:
        sym = next(iter(holdings))
        print(f"\nSample for {sym}:")
        print(holdings[sym].to_string())
