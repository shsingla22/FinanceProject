"""
Fetch 10+ years of DETAILED Profit & Loss statement data for all 500
Nifty 500 companies from screener.in (NSE-mirror, SEBI-aware Indian
financial data service) and store:

  - One detailed wide-format CSV per company in this folder
  - One consolidated long-format CSV (_all_profit_loss_long.csv)
  - One fetch log (_fetch_log.csv)

Each per-company CSV contains the headline P&L line items (Sales,
Expenses, Operating Profit, OPM %, Other Income, Interest,
Depreciation, Profit before tax, Tax %, Net Profit, EPS, Dividend
Payout %) PLUS the sub-component breakdowns of the four expandable
items (Sales→Sales Growth%; Expenses→Material/Manufacturing/Employee/
Other Cost %; Other Income→Exceptional items + Other income normal;
Net Profit→Profit from Associates / Minority share / Exceptional
items AT / Profit excl Excep / Profit for PE / Profit for EPS /
Profit Growth %).

Sub-items are fetched via screener.in's documented schedules API:
  /api/company/{companyId}/schedules/?parent={Parent}&section=profit-loss&consolidated=

Inputs:
  ../Nifty500/nifty500_constituents.csv (500 NSE symbols)

Outputs (this folder):
  {NSE_SYMBOL}.csv             — wide format
  _all_profit_loss_long.csv    — long format combining all companies
  _fetch_log.csv               — status per company

Re-running the script overwrites everything.

Usage:
  python3 fetch_profit_loss.py
"""

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
CONST_CSV = HERE.parent / "Nifty500" / "nifty500_constituents.csv"
LOG_CSV = HERE / "_fetch_log.csv"
LONG_CSV = HERE / "_all_profit_loss_long.csv"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
DELAY_BETWEEN_REQUESTS = 0.4
TIMEOUT = 25

# Expandable parents in the P&L section.
SCHEDULE_PARENTS = ["Sales", "Expenses", "Other Income", "Net Profit"]


def _get(url: str, json_endpoint: bool = False) -> tuple[int, str | None]:
    headers = {
        "User-Agent": UA,
        "Accept": "*/*" if json_endpoint else "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.screener.in/",
    }
    if json_endpoint:
        headers["X-Requested-With"] = "XMLHttpRequest"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as e:
        return e.code, None


def parse_main_pl(html: str) -> tuple[pd.DataFrame, list[str], str, bool] | None:
    """Returns (df_headline, year_columns_only, company_id, is_consolidated_view) or None.

    The P&L table on screener.in has trailing growth-summary columns
    ('Compounded Sales Growth', 'Compounded Profit Growth', 'Stock
    Price CAGR', 'Return on Equity'). We keep only the actual year
    columns (those starting with a month abbreviation + year).
    """
    m = re.search(r'<section[^>]*id="profit-loss"[^>]*>(.*?)</section>', html, re.DOTALL)
    if not m:
        return None
    block = m.group(1)

    headers_all = [t.strip() for t in re.findall(r"<th[^>]*>\s*([^<]+?)\s*</th>", block, re.DOTALL)]
    if not headers_all:
        return None

    # Keep only headers that look like "Mon YYYY" (e.g., "Mar 2015", "Dec 2024")
    year_pat = re.compile(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}$")
    year_indices = [i for i, h in enumerate(headers_all) if year_pat.match(h)]
    year_headers = [headers_all[i] for i in year_indices]
    if not year_headers:
        return None

    rows = re.findall(
        r'<tr[^>]*>\s*<td[^>]*class="text"[^>]*>(.*?)</td>(.*?)</tr>',
        block, re.DOTALL,
    )
    data: dict[str, list[float | None]] = {}
    for label_cell, rest in rows:
        label = re.sub(r"<[^>]+>", "", label_cell).strip().replace("\xa0", " ").replace("&nbsp;", "")
        label = re.sub(r"\s*\+\s*$", "", label).strip()
        if not label:
            continue
        values_all = re.findall(r"<td[^>]*>\s*([-\d,\.%]+)\s*</td>", rest)
        clean_all: list[float | None] = []
        for v in values_all:
            v = v.replace(",", "").replace("%", "").strip()
            try:
                clean_all.append(float(v))
            except ValueError:
                clean_all.append(None)
        # Keep only the year columns (first len(year_indices) values, taking the
        # indices corresponding to the year columns in the original header)
        clean_year: list[float | None] = []
        for yi in year_indices:
            if yi < len(clean_all):
                clean_year.append(clean_all[yi])
            else:
                clean_year.append(None)
        data[label] = clean_year
    if not data:
        return None

    df = pd.DataFrame(data, index=year_headers).T
    df.index.name = "line_item"

    company_id_match = re.search(r'data-company-id="(\d+)"', html)
    if not company_id_match:
        return None
    company_id = company_id_match.group(1)
    is_consolidated = bool(re.search(r"data-consolidated\b", html))
    return df, year_headers, company_id, is_consolidated


def parse_schedule(json_text: str, headers: list[str]) -> pd.DataFrame:
    try:
        obj = json.loads(json_text)
    except json.JSONDecodeError:
        return pd.DataFrame()
    if not obj:
        return pd.DataFrame()
    data: dict[str, list[float | None]] = {}
    for label, year_dict in obj.items():
        if not isinstance(year_dict, dict):
            continue
        row: list[float | None] = []
        for col in headers:
            raw = year_dict.get(col, "")
            raw = str(raw).replace(",", "").replace("%", "").strip()
            try:
                row.append(float(raw))
            except ValueError:
                row.append(None)
        data[label.strip()] = row
    if not data:
        return pd.DataFrame()
    return pd.DataFrame(data, index=headers).T


def fetch_company_detailed(symbol: str) -> tuple[pd.DataFrame | None, list[dict], str]:
    encoded = urllib.parse.quote(symbol, safe="")
    main_html = None
    main_url_kind = None
    for variant in ("consolidated/", ""):
        url = f"https://www.screener.in/company/{encoded}/{variant}"
        code, html = _get(url)
        if code == 200 and html:
            parsed = parse_main_pl(html)
            if parsed is not None:
                main_html = html
                main_url_kind = "consolidated" if variant == "consolidated/" else "standalone"
                break
    if main_html is None:
        return None, [], "no_data_on_either_url"

    parsed = parse_main_pl(main_html)
    if parsed is None:
        return None, [], "pl_parse_failed"
    headline_df, year_cols, company_id, is_consolidated = parsed

    combined = headline_df.copy()
    combined.insert(0, "parent_line_item", "")

    schedule_status = []
    for parent in SCHEDULE_PARENTS:
        if parent not in headline_df.index:
            continue
        params = {"parent": parent, "section": "profit-loss"}
        if is_consolidated:
            params["consolidated"] = ""
        qs = urllib.parse.urlencode(params)
        sched_url = f"https://www.screener.in/api/company/{company_id}/schedules/?{qs}"
        time.sleep(DELAY_BETWEEN_REQUESTS)
        code, body = _get(sched_url, json_endpoint=True)
        if code != 200 or not body:
            schedule_status.append(f"{parent}=HTTP{code}")
            continue
        sub_df = parse_schedule(body, year_cols)
        if sub_df.empty:
            schedule_status.append(f"{parent}=empty")
            continue
        sub_df.insert(0, "parent_line_item", parent)
        combined = pd.concat([combined, sub_df])
        schedule_status.append(f"{parent}={len(sub_df)}")

    long_rows = []
    for line_item, row in combined.iterrows():
        parent = row["parent_line_item"]
        for year_col in year_cols:
            long_rows.append({
                "nse_symbol": symbol,
                "year": year_col,
                "line_item": line_item,
                "parent_line_item": parent,
                "value": row[year_col],
            })

    status = f"ok:{main_url_kind}:headline={len(headline_df)}:cols={len(year_cols)};schedules=" + ",".join(schedule_status)
    return combined, long_rows, status


def main() -> None:
    constituents = pd.read_csv(CONST_CSV)
    symbols = constituents["nse_symbol"].dropna().unique().tolist()
    print(f"Total symbols to fetch: {len(symbols)}")
    print(f"Output folder: {HERE}")
    print(f"Estimated time: {len(symbols) * 5 * DELAY_BETWEEN_REQUESTS / 60:.1f} min")
    print("-" * 70)

    all_long_rows: list[dict] = []
    log_rows: list[dict] = []

    for i, sym in enumerate(symbols, 1):
        try:
            combined_df, long_rows, status = fetch_company_detailed(sym)
        except Exception as e:
            combined_df, long_rows, status = None, [], f"exception:{type(e).__name__}:{str(e)[:50]}"

        if combined_df is not None:
            safe_name = sym.replace("&", "_AND_")
            out_path = HERE / f"{safe_name}.csv"
            combined_df.to_csv(out_path)
        all_long_rows.extend(long_rows)
        log_rows.append({"nse_symbol": sym, "status": status})

        if i % 20 == 0 or i == len(symbols):
            ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
            print(f"  [{i:4d}/{len(symbols)}] last={sym:<14s} ok={ok}/{i} last_status={status[:80]}")

        time.sleep(DELAY_BETWEEN_REQUESTS)

    pd.DataFrame(log_rows).to_csv(LOG_CSV, index=False)
    long_df = pd.DataFrame(all_long_rows)
    long_df.to_csv(LONG_CSV, index=False)

    print("-" * 70)
    ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
    print(f"DONE. ok={ok}/{len(symbols)}")
    print(f"Combined long CSV: {LONG_CSV} ({len(long_df):,} rows)")
    print(f"Log: {LOG_CSV}")


if __name__ == "__main__":
    main()
