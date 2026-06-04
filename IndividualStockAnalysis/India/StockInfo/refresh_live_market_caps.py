"""
Refresh LIVE current Market Cap, Current Price, and Stock P/E for every
Nifty 500 constituent by scraping the screener.in company-page header.

Why: the historical year-end fetcher (fetch_stock_info.py) computes
Market Cap as Equity Capital × Price / Face Value, which fails for
companies where Equity Capital is missing from screener.in's BS section
(e.g. ABB, CRISIL, VBL) or for non-Mar fiscal-year reporters. The
screener.in header always carries a current Market Cap tile, so this
script reads it directly for all 500 cos.

Outputs (in StockInfo/Nifty500/):
  live_market_data.csv     — nse_symbol, market_cap_rs_cr,
                             current_price_rs, stock_pe, fetched_at, status
  _live_fetch_log.csv      — full per-co status log

This also updates each per-company CSV by adding/refreshing a
``Live`` column carrying the live values, and appends matching rows
to ``_all_stock_info_long.csv`` under year="Live".
"""

from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
OUT_DIR = HERE / "Nifty500"
CONST_CSV = HERE.parent / "Nifty500" / "nifty500_constituents.csv"
LIVE_CSV = OUT_DIR / "live_market_data.csv"
LOG_CSV = OUT_DIR / "_live_fetch_log.csv"
LONG_CSV = OUT_DIR / "_all_stock_info_long.csv"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
DELAY = 0.4
TIMEOUT = 25


def _http_get(url: str) -> tuple[int, str | None]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.screener.in/",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception:
        return 0, None


HEADER_LI_RE = re.compile(
    r'<li[^>]*>\s*<span class="name">\s*([^<]+?)\s*</span>.*?'
    r'<span[^>]*class="[^"]*value[^"]*"[^>]*>(.*?)</span>\s*</li>',
    re.DOTALL,
)


def parse_header(html: str) -> dict[str, float | None]:
    out = {"market_cap": None, "current_price": None, "stock_pe": None}
    for name, value in HEADER_LI_RE.findall(html):
        name = name.strip()
        cleaned = re.sub(r"<[^>]+>", "", value)
        cleaned = re.sub(r"\s+", " ", cleaned).strip().replace(",", "").replace("₹", "").strip()
        try:
            num = float(cleaned.split()[0])
        except (ValueError, IndexError):
            continue
        if name == "Market Cap":
            out["market_cap"] = num
        elif name == "Current Price":
            out["current_price"] = num
        elif name == "Stock P/E":
            out["stock_pe"] = num
    return out


def fetch_one(symbol: str) -> tuple[dict[str, float | None], str]:
    """Try consolidated and standalone screener pages, with retries for
    429 rate-limits. Returns the best available header values."""
    safe_sym = urllib.parse.quote(symbol, safe="")
    urls = [
        f"https://www.screener.in/company/{safe_sym}/consolidated/",
        f"https://www.screener.in/company/{safe_sym}/",
    ]

    best = {"market_cap": None, "current_price": None, "stock_pe": None}
    last_status = "no_response"
    last_code = 0
    for url in urls:
        # Up to 4 retries on 429 with exponential backoff
        for attempt in range(4):
            code, html = _http_get(url)
            last_code = code
            if code == 429:
                time.sleep(2 ** attempt)
                continue
            break
        if code != 200 or not html:
            last_status = f"http_{code}"
            continue
        data = parse_header(html)
        # Merge: prefer non-None values, fill gaps from later URLs
        for k in best:
            if best[k] is None and data[k] is not None:
                best[k] = data[k]
        if best["market_cap"] is not None:
            return best, "ok"
        last_status = "ok_no_mcap"
    return best, last_status if last_code else "no_response"


def main() -> None:
    only = None
    if "--only" in sys.argv:
        i = sys.argv.index("--only")
        only = sys.argv[i + 1].split(",")

    constituents = pd.read_csv(CONST_CSV)
    symbols = constituents["nse_symbol"].dropna().astype(str).unique().tolist()
    if only:
        symbols = [s for s in symbols if s in only]
    print(f"Fetching live header values for {len(symbols)} symbols ...")
    print(f"Estimated time: {len(symbols) * DELAY / 60:.1f} min")

    rows = []
    log_rows = []
    fetched_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    for i, sym in enumerate(symbols, 1):
        try:
            data, status = fetch_one(sym)
        except Exception as e:
            data, status = {"market_cap": None, "current_price": None, "stock_pe": None}, f"exception:{type(e).__name__}"
        rows.append({
            "nse_symbol": sym,
            "market_cap_rs_cr": data["market_cap"],
            "current_price_rs": data["current_price"],
            "stock_pe": data["stock_pe"],
            "fetched_at": fetched_at,
            "status": status,
        })
        log_rows.append({"nse_symbol": sym, "status": status})
        time.sleep(DELAY)
        if i % 25 == 0 or i == len(symbols):
            ok = sum(1 for r in rows if r["market_cap_rs_cr"] is not None)
            print(f"  [{i:4d}/{len(symbols)}] mcap_ok={ok}/{i} last={sym} status={status}")

    df = pd.DataFrame(rows)
    # If --only was used, merge with any pre-existing live CSV so we don't
    # lose the rows we already fetched in prior runs.
    if only and LIVE_CSV.exists():
        prior = pd.read_csv(LIVE_CSV)
        prior = prior[~prior["nse_symbol"].isin(df["nse_symbol"])]
        df = pd.concat([prior, df], ignore_index=True)
    df.to_csv(LIVE_CSV, index=False)
    pd.DataFrame(log_rows).to_csv(LOG_CSV, index=False)
    n_ok = df["market_cap_rs_cr"].notna().sum()
    print()
    print(f"Wrote {LIVE_CSV}: {len(df)} rows, {n_ok} with live mcap")
    print(f"Wrote {LOG_CSV}")

    # Apply to per-company CSVs: add/refresh a "Live" column carrying live values
    print()
    print("Updating per-company CSVs with a 'Live' column ...")
    apply_live_to_per_company_csvs(df)

    # Apply to _all_stock_info_long.csv: append "Live" pseudo-year rows
    print("Updating _all_stock_info_long.csv with 'Live' rows ...")
    apply_live_to_long_csv(df)
    print("Done.")


def apply_live_to_per_company_csvs(live: pd.DataFrame) -> None:
    """For each Nifty 500 company, add a 'Live' column to its wide CSV
    populating Stock Price (Rs), Market Cap (Rs Cr), P/E ratio. Other
    metrics are left blank for the Live column.
    """
    by_sym = {r["nse_symbol"]: r for _, r in live.iterrows()}
    updated = 0
    for sym, row in by_sym.items():
        safe_name = sym.replace("&", "_AND_")
        path = OUT_DIR / f"{safe_name}.csv"
        if not path.exists():
            continue
        df = pd.read_csv(path, index_col=0)
        live_col = {}
        if "Stock Price (Rs)" in df.index:
            live_col["Stock Price (Rs)"] = row["current_price_rs"]
        if "Market Cap (Rs Cr)" in df.index:
            live_col["Market Cap (Rs Cr)"] = row["market_cap_rs_cr"]
        if "P/E ratio" in df.index:
            live_col["P/E ratio"] = row["stock_pe"]
        # Apply
        df["Live"] = pd.NA
        for idx, val in live_col.items():
            df.at[idx, "Live"] = val
        df.to_csv(path)
        updated += 1
    print(f"  Updated {updated} per-company CSVs")


def apply_live_to_long_csv(live: pd.DataFrame) -> None:
    """Refresh the long-form CSV: remove any existing year='Live' rows,
    then append new ones from the live data."""
    if not LONG_CSV.exists():
        return
    long_df = pd.read_csv(LONG_CSV)
    long_df = long_df[long_df["year"] != "Live"]
    new_rows = []
    for _, r in live.iterrows():
        sym = r["nse_symbol"]
        if pd.notna(r["current_price_rs"]):
            new_rows.append({"nse_symbol": sym, "year": "Live",
                             "metric": "Stock Price (Rs)",
                             "value": r["current_price_rs"]})
        if pd.notna(r["market_cap_rs_cr"]):
            new_rows.append({"nse_symbol": sym, "year": "Live",
                             "metric": "Market Cap (Rs Cr)",
                             "value": r["market_cap_rs_cr"]})
        if pd.notna(r["stock_pe"]):
            new_rows.append({"nse_symbol": sym, "year": "Live",
                             "metric": "P/E ratio",
                             "value": r["stock_pe"]})
    if new_rows:
        long_df = pd.concat([long_df, pd.DataFrame(new_rows)], ignore_index=True)
    long_df.to_csv(LONG_CSV, index=False)
    print(f"  Refreshed {LONG_CSV}: now {len(long_df)} rows ({len(new_rows)} Live rows)")


if __name__ == "__main__":
    main()
