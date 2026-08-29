"""
fetch_index_data.py — build and save the Nifty 50 index series this skill
divides every company by.

Produces, under ../data/:

  nifty50_price_monthly.csv   month-end closes of ^NSEI (Yahoo Finance),
                              one row per calendar month, ~17 years back —
                              lets reports match a company's own fiscal
                              year-end month (Mar, Jun, Dec, ...)
  nifty50_price_yearly.csv    the March close per fiscal year (FY label
                              "Mar YYYY"), the last 15+ fiscal years
  nifty50_constituents.csv    the current 50 constituents (screener.in
                              mirror of the NIFTY index page — the official
                              NSE archive is WAF-blocked for scripts)
  nifty50_earnings_yearly.csv per fiscal year: the summed Net Profit (PAT)
                              and summed Operating Profit (Financing Profit
                              for lenders) of the current constituents,
                              aggregated from the stored Nifty 500
                              profit-and-loss data, with coverage counts
  _README.md                  provenance + run timestamp

Honest limits, stated rather than hidden:
  - Index PAT / Operating Profit are NOT published by NSE; they are
    aggregated here over the CURRENT 50 constituents (survivorship applies
    to older years).
  - The stored statements cover FY2015..FY2026, so the earnings series is
    ~12 fiscal years even though the price series goes back 15+.

Usage (from anywhere):
  python3 fetch_index_data.py
"""

from __future__ import annotations

import csv
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
INDIA = HERE.parent.parent.parent          # .../IndividualStockAnalysis/India
PL_LONG = INDIA / "ProfitStatement" / "Nifty500" / "_all_profit_loss_long.csv"

YAHOO = ("https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI"
         "?range=17y&interval=1mo")
SCREENER = "https://www.screener.in/company/NIFTY/?page={page}"
UA = {"User-Agent": "Mozilla/5.0 (research tooling; index ratio skill)"}

FY_YEARS = 15                              # fiscal years of price history


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def fetch_monthly_prices() -> pd.DataFrame:
    """^NSEI month closes from Yahoo Finance chart API."""
    payload = json.loads(_get(YAHOO))
    result = payload["chart"]["result"][0]
    stamps = result["timestamp"]
    closes = result["indicators"]["quote"][0]["close"]
    rows = []
    for ts, close in zip(stamps, closes):
        if close is None:
            continue
        d = datetime.fromtimestamp(ts, tz=timezone.utc)
        rows.append({"month": d.strftime("%b %Y"), "year": d.year,
                     "month_num": d.month, "close": round(float(close), 2)})
    df = pd.DataFrame(rows)
    # one row per calendar month (Yahoo repeats the live month; keep last)
    df = df.drop_duplicates(subset=["year", "month_num"], keep="last")
    return df.sort_values(["year", "month_num"]).reset_index(drop=True)


def yearly_from_monthly(monthly: pd.DataFrame) -> pd.DataFrame:
    """March close per fiscal year, newest FY_YEARS fiscal years."""
    mar = monthly[monthly.month_num == 3].copy()
    mar["fy"] = "Mar " + mar["year"].astype(str)
    mar = mar[["fy", "close"]].tail(FY_YEARS)
    return mar.reset_index(drop=True)


def fetch_constituents() -> list[str]:
    """Current Nifty 50 symbols from screener.in's NIFTY index pages."""
    import re
    syms: list[str] = []
    for page in (1, 2, 3):
        html = _get(SCREENER.format(page=page)).decode("utf-8", "replace")
        found = re.findall(r'/company/([A-Z0-9&\-]+)/', html)
        for s in found:
            if s not in ("NIFTY",) and not s.isdigit() and s not in syms:
                syms.append(s)
        if len(syms) >= 50:
            break
    if len(syms) < 45:
        raise RuntimeError(f"constituent scrape looks wrong: got {len(syms)}")
    return syms[:50]


def aggregate_earnings(symbols: list[str]) -> pd.DataFrame:
    """Sum PAT and Operating/Financing Profit of the constituents per FY."""
    pl = pd.read_csv(PL_LONG)
    pl = pl[pl.nse_symbol.isin(symbols)]

    def fy_label(y: str) -> str:
        # map any year-end month to the fiscal year it belongs to:
        # Apr..Dec YYYY -> FY "Mar YYYY+1"; Jan..Mar YYYY -> FY "Mar YYYY"
        mon, yr = y.split()
        m = datetime.strptime(mon, "%b").month
        return f"Mar {int(yr) + 1}" if m >= 4 else f"Mar {yr}"

    pl = pl.assign(fy=pl.year.map(fy_label))
    pat = pl[pl.line_item == "Net Profit"]
    # non-financial companies report Operating Profit; lenders report
    # Financing Profit — take Operating Profit, else Financing Profit
    op_pref = pl[pl.line_item.isin(["Operating Profit", "Financing Profit"])]
    op_pref = (op_pref.sort_values("line_item")   # "Financing..." < "Operating..."
               .drop_duplicates(subset=["nse_symbol", "fy"], keep="last"))

    rows = []
    for fy in sorted(pat.fy.unique(), key=lambda s: int(s.split()[1])):
        p = pat[pat.fy == fy]
        o = op_pref[op_pref.fy == fy]
        rows.append({
            "fy": fy,
            "index_pat": round(p.value.sum(), 1),
            "pat_companies": p.nse_symbol.nunique(),
            "index_op": round(o.value.sum(), 1),
            "op_companies": o.nse_symbol.nunique(),
        })
    df = pd.DataFrame(rows)
    # keep only fiscal years where at least 40 of 50 constituents reported —
    # thinner years would silently misstate the index aggregate
    return df[df.pat_companies >= 40].reset_index(drop=True)


def main() -> None:
    DATA.mkdir(exist_ok=True)

    monthly = fetch_monthly_prices()
    monthly.to_csv(DATA / "nifty50_price_monthly.csv", index=False)

    yearly = yearly_from_monthly(monthly)
    yearly.to_csv(DATA / "nifty50_price_yearly.csv", index=False)

    symbols = fetch_constituents()
    pd.DataFrame({"nse_symbol": symbols}).to_csv(
        DATA / "nifty50_constituents.csv", index=False)

    earnings = aggregate_earnings(symbols)
    earnings.to_csv(DATA / "nifty50_earnings_yearly.csv", index=False)

    (DATA / "_README.md").write_text(f"""# Nifty 50 index series — provenance

Fetched {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}.

- `nifty50_price_monthly.csv` — ^NSEI month closes, Yahoo Finance chart API
  ({len(monthly)} months).
- `nifty50_price_yearly.csv` — March close per fiscal year, last
  {len(yearly)} fiscal years ({yearly.fy.iloc[0]} .. {yearly.fy.iloc[-1]}).
- `nifty50_constituents.csv` — current 50 constituents, screener.in mirror
  of the NIFTY index page.
- `nifty50_earnings_yearly.csv` — per fiscal year, the summed Net Profit and
  summed Operating Profit (Financing Profit for lenders) of the current
  constituents, aggregated from the stored Nifty 500 profit-and-loss data
  ({earnings.fy.iloc[0]} .. {earnings.fy.iloc[-1]}; survivorship caveat:
  today's constituents, not the historical membership).
""")
    print(f"prices: {len(monthly)} months, {len(yearly)} fiscal years "
          f"({yearly.fy.iloc[0]}..{yearly.fy.iloc[-1]})")
    print(f"constituents: {len(symbols)}")
    print(f"earnings: {len(earnings)} fiscal years "
          f"({earnings.fy.iloc[0]}..{earnings.fy.iloc[-1]})")


if __name__ == "__main__":
    main()
