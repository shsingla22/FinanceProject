"""
Fetch 10+ years of working-capital metrics — Debtor Days, Inventory
Days, Days Payable, Cash Conversion Cycle, Working Capital Days
(plus ROCE %) — for every Nifty Total Market constituent from
screener.in's "Ratios" section, mirroring the BS / PL / CashFlow
storage layout.

screener.in renders these six metrics inside the
``<section id="ratios">`` block of every company page (consolidated
preferred, standalone fallback). They are computed by screener from
the audited annual report numbers, with a March-fiscal-year axis
(or Dec / Jun / Sep / Nov for non-Mar reporters).

Inputs:
  ../NiftyTotalMarket/niftytotalmarket_constituents.csv (742 cos)

Outputs (in NiftyTotalMarket/):
  {NSE_SYMBOL}.csv             wide format; rows = metric, cols = year-end strings
  _all_working_capital_long.csv long format combining all cos
                                  (nse_symbol, year, metric, value)
  _fetch_log.csv               per-co status

Usage:
  python3 fetch_working_capital.py                       # NiftyTotalMarket
  python3 fetch_working_capital.py --universe Nifty500   # alternate universe
  python3 fetch_working_capital.py --skip-existing       # incremental
"""

from __future__ import annotations

import argparse
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent

UNIVERSES = {
    "NiftyTotalMarket": {
        "const": HERE.parent / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv",
        "out": HERE / "NiftyTotalMarket",
    },
    "Nifty500": {
        "const": HERE.parent / "Nifty500" / "nifty500_constituents.csv",
        "out": HERE / "Nifty500",
    },
}

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
DELAY_BETWEEN_REQUESTS = 0.4
TIMEOUT = 25

# Metrics to keep from the screener.in ratios section.
# (Other rows there are kept too — see parse_ratios — but these are
# the ones that always exist if the section exists.)
WC_METRICS = {
    "Debtor Days",
    "Inventory Days",
    "Days Payable",
    "Cash Conversion Cycle",
    "Working Capital Days",
    "ROCE %",
}

YEAR_RE = re.compile(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}$")


def _get(url: str) -> tuple[int, str | None]:
    headers = {
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.screener.in/",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception:
        return 0, None


def parse_ratios(html: str) -> pd.DataFrame | None:
    m = re.search(r'<section[^>]*id="ratios"[^>]*>(.*?)</section>', html, re.DOTALL)
    if not m:
        return None
    block = m.group(1)

    headers_all = [t.strip() for t in
                   re.findall(r"<th[^>]*>\s*([^<]+?)\s*</th>", block, re.DOTALL)]
    year_indices = [i for i, h in enumerate(headers_all) if YEAR_RE.match(h)]
    headers = [headers_all[i] for i in year_indices]
    if not headers:
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
        clean: list[float | None] = []
        for v in values_all:
            v = v.replace(",", "").replace("%", "").strip()
            try:
                clean.append(float(v))
            except ValueError:
                clean.append(None)
        aligned = [clean[i] if i < len(clean) else None for i in year_indices]
        data[label] = aligned
    if not data:
        return None
    df = pd.DataFrame(data, index=headers).T
    df.index.name = "metric"
    return df


def fetch_company(symbol: str) -> tuple[pd.DataFrame | None, list[dict], str]:
    encoded = urllib.parse.quote(symbol, safe="")
    df = None
    main_url_kind = None
    for variant in ("consolidated/", ""):
        url = f"https://www.screener.in/company/{encoded}/{variant}"
        code, html = _get(url)
        if code == 200 and html:
            parsed = parse_ratios(html)
            if parsed is not None and len(parsed):
                df = parsed
                main_url_kind = "consolidated" if variant == "consolidated/" else "standalone"
                break
    if df is None:
        return None, [], "no_ratios_section"

    year_cols = list(df.columns)
    long_rows = []
    for metric, row in df.iterrows():
        for year_col in year_cols:
            long_rows.append({
                "nse_symbol": symbol,
                "year": year_col,
                "metric": metric,
                "value": row[year_col],
            })

    metrics_present = set(df.index) & WC_METRICS
    status = (f"ok:{main_url_kind}:rows={len(df)}:cols={len(year_cols)}:"
              f"wc_present={len(metrics_present)}/{len(WC_METRICS)}")
    return df, long_rows, status


def reload_csv_to_long(out_dir: Path, sym: str) -> list[dict]:
    safe_name = sym.replace("&", "_AND_")
    path = out_dir / f"{safe_name}.csv"
    if not path.exists():
        return []
    df = pd.read_csv(path, index_col=0)
    year_cols = list(df.columns)
    rows = []
    for metric, row in df.iterrows():
        for year_col in year_cols:
            rows.append({
                "nse_symbol": sym,
                "year": year_col,
                "metric": metric,
                "value": row[year_col],
            })
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--universe", choices=list(UNIVERSES), default="NiftyTotalMarket")
    ap.add_argument("--skip-existing", action="store_true")
    args = ap.parse_args()

    cfg = UNIVERSES[args.universe]
    const_csv = cfg["const"]
    out_dir = cfg["out"]
    out_dir.mkdir(parents=True, exist_ok=True)
    log_csv = out_dir / "_fetch_log.csv"
    long_csv = out_dir / "_all_working_capital_long.csv"

    constituents = pd.read_csv(const_csv)
    symbols = constituents["nse_symbol"].dropna().unique().tolist()

    if args.skip_existing:
        existing_stems = {p.stem for p in out_dir.glob("*.csv")
                          if not p.stem.startswith("_")}
        to_fetch = [s for s in symbols
                    if s.replace("&", "_AND_") not in existing_stems]
        skipped = len(symbols) - len(to_fetch)
    else:
        to_fetch = symbols
        skipped = 0

    print(f"Universe: {args.universe} ({len(symbols)} cos)")
    print(f"Already present: {skipped} cos — reloaded from local CSV")
    print(f"To HTTP-fetch  : {len(to_fetch)} cos")
    print(f"Output folder  : {out_dir}")
    print(f"Estimated HTTP time: {len(to_fetch) * DELAY_BETWEEN_REQUESTS / 60:.1f} min")
    print("-" * 70)

    all_long_rows: list[dict] = []
    log_rows: list[dict] = []
    to_fetch_set = set(to_fetch)

    for i, sym in enumerate(symbols, 1):
        if sym not in to_fetch_set:
            long_rows = reload_csv_to_long(out_dir, sym)
            all_long_rows.extend(long_rows)
            log_rows.append({"nse_symbol": sym, "status": "skip:existing"})
            continue

        try:
            df, long_rows, status = fetch_company(sym)
        except Exception as e:
            df, long_rows, status = None, [], f"exception:{type(e).__name__}:{str(e)[:50]}"

        if df is not None:
            safe_name = sym.replace("&", "_AND_")
            df.to_csv(out_dir / f"{safe_name}.csv")
        all_long_rows.extend(long_rows)
        log_rows.append({"nse_symbol": sym, "status": status})

        if i % 25 == 0 or i == len(symbols):
            ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
            print(f"  [{i:4d}/{len(symbols)}] last={sym:<14s} ok={ok}/{i} "
                  f"last_status={status[:70]}")

        time.sleep(DELAY_BETWEEN_REQUESTS)

    pd.DataFrame(log_rows).to_csv(log_csv, index=False)
    long_df = pd.DataFrame(all_long_rows)
    long_df.to_csv(long_csv, index=False)

    ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
    re_used = sum(1 for r in log_rows if r["status"].startswith("skip"))
    print("-" * 70)
    print(f"DONE. ok={ok}/{len(symbols)}  (re-used={re_used})")
    print(f"Combined long CSV: {long_csv} ({len(long_df):,} rows)")
    print(f"Log: {log_csv}")


if __name__ == "__main__":
    main()
