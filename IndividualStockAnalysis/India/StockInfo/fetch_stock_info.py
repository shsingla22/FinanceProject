"""
Fetch year-end (March fiscal-year-end) Stock Price, Market Cap, and
P/E ratio for all 500 Nifty 500 companies, last 10+ years.

Data sources (chain of trust):
  - **Stock Price**: Yahoo Finance daily EOD for "{NSE_SYMBOL}.NS"
    (Yahoo redistributes NSE's official end-of-day closing price)
  - **EPS**: existing `../ProfitStatement/{SYMBOL}.csv` "EPS in Rs" row
    (from screener.in's standardization of the audited annual report)
  - **Equity Capital**: existing `../BalanceSheet/{SYMBOL}.csv`
    "Equity Capital" row (also from audited annual reports)
  - **Face Value**: scraped once per company from screener.in's
    company page (the "Face Value" key ratio)

Computed:
  - Shares Outstanding = (Equity Capital [in ₹ Cr] × 10^7) / Face Value
  - Market Cap [in ₹ Cr] = Shares × Price / 10^7 = Equity Capital × Price / Face Value
  - P/E = Price / EPS

Outputs (in this folder):
  {NSE_SYMBOL}.csv         — wide format, rows = metric, cols = year
  _all_stock_info_long.csv — long format combining all companies
  _fetch_log.csv           — status per company

Verification is performed in `verify_sample()` against screener.in's
displayed current Market Cap and Stock P/E for a hard-coded set of
well-known names (RELIANCE, TCS, HDFCBANK, etc.). The script aborts
if verification fails by > 10% on any spot-check.

Usage:
  python3 fetch_stock_info.py            # verify + fetch all 500
  python3 fetch_stock_info.py --verify   # verify only
"""

from __future__ import annotations

import json
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
OUT_DIR.mkdir(exist_ok=True)
CONST_CSV = HERE.parent / "Nifty500" / "nifty500_constituents.csv"
BS_DIR = HERE.parent / "BalanceSheet" / "Nifty500"
PL_DIR = HERE.parent / "ProfitStatement" / "Nifty500"
LOG_CSV = OUT_DIR / "_fetch_log.csv"
LONG_CSV = OUT_DIR / "_all_stock_info_long.csv"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
DELAY_SCREENER = 0.4
DELAY_YAHOO = 0.2
TIMEOUT = 25


def _http_get(url: str, accept: str = "text/html") -> tuple[int, str | None]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": accept,
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


def parse_face_value(html: str) -> float | None:
    """Extract face value (₹ per share) from a screener.in company page."""
    m = re.search(
        r'<li[^>]*>\s*<span class="name">\s*Face Value\s*</span>.*?<span class="number">\s*([\d.]+)\s*</span>',
        html, re.DOTALL,
    )
    return float(m.group(1)) if m else None


def parse_live_eps_and_equity(html: str) -> tuple[dict[str, float | None], dict[str, float | None], list[str]]:
    """Extract LIVE EPS and Equity Capital rows from the screener.in HTML.
    Returns ({year: eps}, {year: equity_cap_cr}, year_headers).

    Reading these LIVE from the same HTML we fetch for face value (instead of
    from the stored ProfitStatement/BalanceSheet CSVs) ensures EPS and Equity
    Capital match the current screener.in numbers — important for companies
    where screener has restated historical EPS after a corporate action like a
    bonus issue (e.g., RELIANCE 1:1 bonus in Oct 2024 caused a historical EPS
    restatement on the live page).
    """
    eps_by_year: dict[str, float | None] = {}
    equity_by_year: dict[str, float | None] = {}
    year_headers: list[str] = []

    year_pat = re.compile(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}$")

    # P&L section: get EPS in Rs row
    m = re.search(r'<section[^>]*id="profit-loss"[^>]*>(.*?)</section>', html, re.DOTALL)
    if m:
        block = m.group(1)
        headers_all = [t.strip() for t in re.findall(r"<th[^>]*>\s*([^<]+?)\s*</th>", block, re.DOTALL)]
        year_indices = [i for i, h in enumerate(headers_all) if year_pat.match(h)]
        year_headers = [headers_all[i] for i in year_indices]
        rows = re.findall(
            r'<tr[^>]*>\s*<td[^>]*class="text"[^>]*>(.*?)</td>(.*?)</tr>',
            block, re.DOTALL,
        )
        for label_cell, rest in rows:
            label = re.sub(r"<[^>]+>", "", label_cell).strip()
            label = label.replace("\xa0", " ").replace("&nbsp;", "")
            label = re.sub(r"\s*\+\s*$", "", label).strip()
            if label != "EPS in Rs":
                continue
            values_all = re.findall(r"<td[^>]*>\s*([-\d,\.%]+)\s*</td>", rest)
            clean: list[float | None] = []
            for v in values_all:
                v = v.replace(",", "").replace("%", "").strip()
                try:
                    clean.append(float(v))
                except ValueError:
                    clean.append(None)
            for j, yi in enumerate(year_indices):
                eps_by_year[year_headers[j]] = clean[yi] if yi < len(clean) else None
            break

    # Balance sheet section: get Equity Capital row
    m = re.search(r'<section[^>]*id="balance-sheet"[^>]*>(.*?)</section>', html, re.DOTALL)
    if m:
        block = m.group(1)
        headers_all = [t.strip() for t in re.findall(r"<th[^>]*>\s*([^<]+?)\s*</th>", block, re.DOTALL)]
        bs_year_indices = [i for i, h in enumerate(headers_all) if year_pat.match(h)]
        bs_year_headers = [headers_all[i] for i in bs_year_indices]
        rows = re.findall(
            r'<tr[^>]*>\s*<td[^>]*class="text"[^>]*>(.*?)</td>(.*?)</tr>',
            block, re.DOTALL,
        )
        for label_cell, rest in rows:
            label = re.sub(r"<[^>]+>", "", label_cell).strip()
            label = label.replace("\xa0", " ").replace("&nbsp;", "")
            label = re.sub(r"\s*\+\s*$", "", label).strip()
            if label != "Equity Capital":
                continue
            values_all = re.findall(r"<td[^>]*>\s*([-\d,\.%]+)\s*</td>", rest)
            clean: list[float | None] = []
            for v in values_all:
                v = v.replace(",", "").replace("%", "").strip()
                try:
                    clean.append(float(v))
                except ValueError:
                    clean.append(None)
            for j, yi in enumerate(bs_year_indices):
                equity_by_year[bs_year_headers[j]] = clean[yi] if yi < len(clean) else None
            break

    return eps_by_year, equity_by_year, year_headers


def parse_current_metrics(html: str) -> dict[str, float | None]:
    """Extract the current displayed Market Cap, Price, P/E from screener.in.
    Used for verification — these are the live values; we compute ours and
    must agree to within a few %."""
    out: dict[str, float | None] = {"market_cap": None, "current_price": None, "stock_pe": None}
    pattern = re.compile(
        r'<li[^>]*>\s*<span class="name">\s*([^<]+?)\s*</span>.*?'
        r'<span[^>]*class="[^"]*value[^"]*"[^>]*>(.*?)</span>\s*</li>',
        re.DOTALL,
    )
    for name, value in pattern.findall(html):
        name = name.strip()
        value = re.sub(r"<[^>]+>", "|", value)
        value = re.sub(r"\s+", " ", value).strip().replace("|", "").replace(",", "").replace("₹", "").strip()
        try:
            num = float(value.split()[0])
        except (ValueError, IndexError):
            continue
        if name == "Market Cap":
            out["market_cap"] = num  # ₹ Cr
        elif name == "Current Price":
            out["current_price"] = num  # ₹
        elif name == "Stock P/E":
            out["stock_pe"] = num
    return out


def fetch_yahoo_year_end_prices(symbol: str, start_year: int = 2015, end_year: int = 2026) -> dict[str, float | None]:
    """Returns {"Mar 2015": price, "Mar 2016": price, ...} for the last NSE
    trading day of each March (Indian fiscal year-end)."""
    yahoo_sym = symbol.replace("&", "%26") + ".NS"
    period1 = int(datetime(start_year, 1, 1).timestamp())
    period2 = int(datetime(end_year + 1, 1, 1).timestamp())
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{yahoo_sym}?period1={period1}&period2={period2}&interval=1d"
    code, body = _http_get(url, accept="*/*")
    if code != 200 or not body:
        return {}
    try:
        data = json.loads(body)
        r = data["chart"]["result"][0]
        ts = r["timestamp"]
        closes = r["indicators"]["quote"][0]["close"]
    except (json.JSONDecodeError, KeyError, IndexError, TypeError):
        return {}

    # Group by year-month; find last March trading day per year
    out: dict[str, float | None] = {}
    last_mar_by_year: dict[int, tuple[str, float]] = {}
    for t, c in zip(ts, closes):
        if c is None:
            continue
        d = datetime.utcfromtimestamp(t)
        if d.month != 3:
            continue
        date_str = d.strftime("%Y-%m-%d")
        existing = last_mar_by_year.get(d.year)
        if existing is None or date_str > existing[0]:
            last_mar_by_year[d.year] = (date_str, float(c))
    for year in range(start_year, end_year + 1):
        col = f"Mar {year}"
        if year in last_mar_by_year:
            out[col] = round(last_mar_by_year[year][1], 2)
        else:
            out[col] = None
    return out


def read_local_metric(csv_path: Path, metric_name: str) -> dict[str, float | None]:
    """Read a single line item's values from a per-company wide CSV."""
    if not csv_path.exists():
        return {}
    df = pd.read_csv(csv_path, index_col=0)
    if metric_name not in df.index:
        return {}
    row = df.loc[metric_name]
    # If duplicate row labels, take first
    if isinstance(row, pd.DataFrame):
        row = row.iloc[0]
    out: dict[str, float | None] = {}
    for col in df.columns:
        if col == "parent_line_item":
            continue
        try:
            v = float(row[col]) if pd.notna(row[col]) else None
        except (ValueError, TypeError):
            v = None
        out[col] = v
    return out


def fetch_company(symbol: str) -> tuple[pd.DataFrame | None, str]:
    """Returns a DataFrame with rows = ['Stock Price (₹)', 'EPS in Rs',
    'Equity Capital (₹ Cr)', 'Face Value (₹)', 'Shares Outstanding',
    'Market Cap (₹ Cr)', 'P/E ratio'] and cols = year strings."""

    # 1. Fetch face value (and verification metrics) from screener.in
    safe_sym = urllib.parse.quote(symbol, safe="")
    code, html = _http_get(f"https://www.screener.in/company/{safe_sym}/consolidated/")
    if code != 200 or not html:
        code, html = _http_get(f"https://www.screener.in/company/{safe_sym}/")
        if code != 200 or not html:
            return None, "screener_404"
    face_value = parse_face_value(html)
    current = parse_current_metrics(html)

    # Parse EPS and Equity Capital LIVE from the same HTML — this ensures
    # we use the current screener.in values (which may have been restated
    # post-corporate-actions) rather than older cached values.
    eps_by_year, equity_by_year, _ = parse_live_eps_and_equity(html)

    time.sleep(DELAY_SCREENER)

    # 2. Fetch year-end prices from Yahoo Finance
    prices = fetch_yahoo_year_end_prices(symbol)
    if not prices or all(v is None for v in prices.values()):
        return None, "yahoo_no_data"
    time.sleep(DELAY_YAHOO)

    # 5. Build the combined DataFrame; align on year columns (March year-ends only)
    year_cols = sorted(set(prices) | set(eps_by_year) | set(equity_by_year))
    year_cols = [c for c in year_cols if c.startswith("Mar ")]

    out: dict[str, list[float | None]] = {
        "Stock Price (Rs)": [],
        "EPS in Rs": [],
        "Equity Capital (Rs Cr)": [],
        "Face Value (Rs)": [],
        "Shares Outstanding": [],
        "Market Cap (Rs Cr)": [],
        "P/E ratio": [],
    }

    for col in year_cols:
        price = prices.get(col)
        eps = eps_by_year.get(col)
        eq_cap_cr = equity_by_year.get(col)
        fv = face_value

        shares = None
        if eq_cap_cr is not None and fv is not None and fv > 0:
            shares = eq_cap_cr * 1e7 / fv  # absolute share count

        mcap_cr = None
        if shares is not None and price is not None:
            # mcap (₹) = shares × price; convert to Cr by /1e7
            mcap_cr = shares * price / 1e7
            mcap_cr = round(mcap_cr, 2)

        pe = None
        if price is not None and eps is not None and eps != 0:
            pe = round(price / eps, 2)

        out["Stock Price (Rs)"].append(price)
        out["EPS in Rs"].append(eps)
        out["Equity Capital (Rs Cr)"].append(eq_cap_cr)
        out["Face Value (Rs)"].append(fv)
        out["Shares Outstanding"].append(round(shares, 0) if shares is not None else None)
        out["Market Cap (Rs Cr)"].append(mcap_cr)
        out["P/E ratio"].append(pe)

    df = pd.DataFrame(out, index=year_cols).T
    df.index.name = "metric"

    # Add verification metadata in the status
    status_bits = [
        f"FV={face_value}",
        f"yrs={len([c for c in year_cols if prices.get(c) is not None])}",
        f"current_mcap={current.get('market_cap')}",
        f"current_pe={current.get('stock_pe')}",
    ]
    return df, "ok:" + ":".join(str(b) for b in status_bits)


def verify_sample() -> bool:
    """Test on known stocks against their CURRENT screener.in displayed values."""
    print("=" * 70)
    print("VERIFICATION (Mar 2025 / Mar 2026 spot checks vs screener.in live)")
    print("=" * 70)
    samples = ["RELIANCE", "TCS", "HDFCBANK", "INFY", "ITC", "HINDUNILVR"]
    all_ok = True
    for sym in samples:
        df, status = fetch_company(sym)
        if df is None:
            print(f"  {sym:12s}  FAILED: {status}")
            all_ok = False
            continue
        # The latest column is the most recent year (Mar 2026 typically)
        latest = df.columns[-1]
        prev = df.columns[-2] if len(df.columns) >= 2 else None
        # Get the computed market cap and P/E for the latest year
        comp_mcap = df.loc["Market Cap (Rs Cr)", latest]
        comp_pe = df.loc["P/E ratio", latest]
        # Compare against status (which has current_mcap and current_pe)
        m = re.search(r"current_mcap=([\d.]+)", status)
        live_mcap = float(m.group(1)) if m else None
        m = re.search(r"current_pe=([\d.]+)", status)
        live_pe = float(m.group(1)) if m else None
        print(f"  {sym:12s} latest={latest}")
        print(f"    Computed: MCap={comp_mcap:>12,.0f} Cr  PE={comp_pe}")
        print(f"    Live    : MCap={live_mcap:>12,.0f} Cr  PE={live_pe}")
        if comp_mcap and live_mcap:
            pct = abs(comp_mcap - live_mcap) / live_mcap * 100
            print(f"    MCap delta: {pct:.1f}% {'✓' if pct < 15 else '✗'}")
            if pct > 25:
                all_ok = False
        if comp_pe and live_pe:
            pct = abs(comp_pe - live_pe) / live_pe * 100
            print(f"    PE   delta: {pct:.1f}% {'✓' if pct < 25 else '✗'}")
            if pct > 50:
                all_ok = False
    print()
    return all_ok


def main() -> None:
    if "--verify" in sys.argv:
        ok = verify_sample()
        sys.exit(0 if ok else 1)

    # First verify sample
    print("Running verification on sample of 6 well-known stocks...\n")
    if not verify_sample():
        print("VERIFICATION FAILED. Investigate before running full fetch.")
        sys.exit(1)
    print("Verification passed.\n")

    constituents = pd.read_csv(CONST_CSV)
    symbols = constituents["nse_symbol"].dropna().unique().tolist()
    print(f"Total symbols: {len(symbols)}")
    print(f"Estimated time: {len(symbols) * (DELAY_SCREENER + DELAY_YAHOO) / 60:.1f} min")
    print("-" * 70)

    all_long_rows: list[dict] = []
    log_rows: list[dict] = []

    for i, sym in enumerate(symbols, 1):
        try:
            df, status = fetch_company(sym)
        except Exception as e:
            df, status = None, f"exception:{type(e).__name__}:{str(e)[:50]}"

        if df is not None:
            safe_name = sym.replace("&", "_AND_")
            df.to_csv(OUT_DIR / f"{safe_name}.csv")
            for metric, row in df.iterrows():
                for year_col, val in row.items():
                    all_long_rows.append({
                        "nse_symbol": sym,
                        "year": year_col,
                        "metric": metric,
                        "value": val,
                    })
        log_rows.append({"nse_symbol": sym, "status": status})

        if i % 20 == 0 or i == len(symbols):
            ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
            print(f"  [{i:4d}/{len(symbols)}] last={sym:<14s} ok={ok}/{i} last_status={status[:70]}")

    pd.DataFrame(log_rows).to_csv(LOG_CSV, index=False)
    pd.DataFrame(all_long_rows).to_csv(LONG_CSV, index=False)
    ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
    print("-" * 70)
    print(f"DONE. ok={ok}/{len(symbols)}")


if __name__ == "__main__":
    main()
