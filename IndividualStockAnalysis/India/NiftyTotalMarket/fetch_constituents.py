"""
Fetch the constituents of the NSE 'NIFTY TOTAL MARKET' index.

The official source (niftyindices.com / nseindia.com archives) is
WAF-blocked from automated clients, so this script combines TWO
publicly accessible mirrors:

  1. The universe of NIFTY TOTAL MARKET symbols comes from
     screener.in's `/company/NFTYTOTMKT/` page, paginated through
     all `?page=N#constituents` views (~30 pages × ~25 cos).

  2. The ISIN and canonical name for each symbol come from
     Groww's instruments master at
     ``https://growwapi-assets.groww.in/instruments/instrument.csv``
     filtered to ``exchange=NSE, segment=CASH, instrument_type=EQ``.

  3. Industry tags are pulled from our existing Nifty 500 master
     (``../Nifty500/nifty500_constituents.csv``) where present.

Outputs:
  niftytotalmarket_constituents.csv  — nse_symbol, company_name, industry,
                                       series, isin (one row per constituent)
  _fetch_log.csv                     — per-co provenance log
  _README.md                         — provenance + run timestamp
"""

from __future__ import annotations

import io
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime
from html import unescape
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
OUT_CSV = HERE / "niftytotalmarket_constituents.csv"
LOG_CSV = HERE / "_fetch_log.csv"
N500_MASTER = HERE.parent / "Nifty500" / "nifty500_constituents.csv"

INDEX_URL_TPL = "https://www.screener.in/company/NFTYTOTMKT/?page={page}#constituents"
GROWW_INSTRUMENTS_URL = "https://growwapi-assets.groww.in/instruments/instrument.csv"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
)
DELAY = 0.3
TIMEOUT = 60


def http_get(url: str) -> bytes | None:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,text/csv,application/csv,*/*;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.screener.in/",
    })
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.read()
    except Exception:
        return None


SEC_RE = re.compile(
    r'<section[^>]*id="constituents"[^>]*>(.*?)</section>',
    re.DOTALL | re.IGNORECASE,
)
PAIR_RE = re.compile(
    r'<a\s+href="/company/([A-Z][A-Z0-9&_\-]{1,15})/[^"]*"[^>]*>'
    r'\s*([^<]+?)\s*</a>',
    re.DOTALL,
)


def fetch_index_symbols() -> dict[str, str]:
    """Paginate the screener.in index page; return {symbol: short_name}."""
    seen: dict[str, str] = {}
    for page in range(1, 60):
        body = http_get(INDEX_URL_TPL.format(page=page))
        if not body:
            print(f"  page {page}: HTTP error — stopping")
            break
        html = body.decode("utf-8", errors="ignore")
        m = SEC_RE.search(html)
        if not m:
            break
        before = len(seen)
        for sym, name in PAIR_RE.findall(m.group(1)):
            if sym == "NFTYTOTMKT":
                continue
            name = unescape(re.sub(r"\s+", " ", name)).strip()
            seen.setdefault(sym, name)
        added = len(seen) - before
        print(f"  page {page}: +{added}, total {len(seen)}")
        if added == 0:
            break
        time.sleep(DELAY)
    return seen


def load_groww_master() -> pd.DataFrame:
    """Download Groww's NSE instruments CSV; return slim NSE-equity table."""
    body = http_get(GROWW_INSTRUMENTS_URL)
    if body is None:
        raise RuntimeError("Failed to download Groww instruments CSV")
    df = pd.read_csv(io.BytesIO(body), low_memory=False)
    eq = df[(df["exchange"] == "NSE") &
            (df["segment"] == "CASH") &
            (df["instrument_type"] == "EQ")].copy()
    eq = eq.sort_values(["trading_symbol", "series"]).drop_duplicates(
        "trading_symbol", keep="first")
    return eq[["trading_symbol", "name", "isin", "series"]].rename(
        columns={"trading_symbol": "nse_symbol", "name": "groww_name"})


def main() -> None:
    print("Step 1: scraping NIFTY TOTAL MARKET symbols from screener.in ...")
    universe = fetch_index_symbols()
    print(f"  collected {len(universe)} unique constituents.")

    print("\nStep 2: downloading Groww NSE instruments master "
          "for ISIN / canonical name ...")
    master = load_groww_master()
    print(f"  loaded {len(master)} NSE-equity rows.")

    # Optional: industry + longer-form name from existing Nifty 500 master
    n500_map: dict[str, dict] = {}
    if N500_MASTER.exists():
        n500 = pd.read_csv(N500_MASTER)
        n500_map = n500.set_index("nse_symbol").to_dict("index")
        print(f"  loaded {len(n500_map)} cos from local Nifty500 master "
              "(for industry tags + canonical names).")

    master_by_sym = master.set_index("nse_symbol").to_dict("index")

    rows: list[dict] = []
    log: list[dict] = []
    for sym, short_name in sorted(universe.items()):
        mast = master_by_sym.get(sym, {})
        n5 = n500_map.get(sym, {})
        isin = mast.get("isin") or ""
        series = mast.get("series") or "EQ"
        # Preference order for company_name:
        #   Nifty500 master (proper-case) → Groww (truncated) → screener short
        name = (n5.get("company_name") if n5 and pd.notna(n5.get("company_name"))
                and str(n5["company_name"]).strip()
                else (mast.get("groww_name") or short_name))
        industry = (n5.get("industry") if n5 and pd.notna(n5.get("industry"))
                    else "")
        rows.append({
            "nse_symbol": sym,
            "company_name": name,
            "industry": industry,
            "series": series,
            "isin": isin,
        })
        log.append({
            "nse_symbol": sym,
            "isin_source": "groww_master" if isin else "missing",
            "name_source": ("nifty500_master" if n5.get("company_name")
                            else "groww_master" if mast.get("groww_name")
                            else "screener"),
        })

    df = pd.DataFrame(rows).sort_values("nse_symbol").reset_index(drop=True)
    df.to_csv(OUT_CSV, index=False)
    pd.DataFrame(log).to_csv(LOG_CSV, index=False)

    print()
    print(f"Wrote {OUT_CSV} ({len(df)} rows)")
    print(f"  with ISIN     : {(df['isin'].astype(str).str.len() > 0).sum()}")
    print(f"  with industry : {(df['industry'].astype(str).str.len() > 0).sum()}")

    readme = HERE / "_README.md"
    readme.write_text(
        "# NIFTY Total Market — constituents\n\n"
        f"**Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"
        "**Universe:** the ~750 cos that comprise the NSE NIFTY TOTAL MARKET "
        "index (Nifty 500 ∪ Nifty Microcap 250).\n\n"
        "## Files\n"
        "- `niftytotalmarket_constituents.csv` — `nse_symbol, company_name, "
        "industry, series, isin`\n"
        "- `_fetch_log.csv` — provenance of ISIN & name per company\n"
        "- `fetch_constituents.py` — re-runnable fetcher\n\n"
        "## Data source chain\n"
        "Because NSE's own index CSVs (niftyindices.com / nseindia.com "
        "archives) are WAF-blocked from headless clients, the script uses:\n\n"
        "1. **screener.in** `/company/NFTYTOTMKT/` (paginated) for the "
        "constituent universe (NSE symbols).\n"
        "2. **Groww** instruments master "
        "(`growwapi-assets.groww.in/instruments/instrument.csv`) for the "
        "ISIN and canonical company name. Groww's CSV is publicly "
        "downloadable and updated daily by Groww.\n"
        "3. **Local Nifty500 master** "
        "(`../Nifty500/nifty500_constituents.csv`) for the longer "
        "proper-cased company names and industry tags (used preferentially "
        "where present).\n\n"
        "## Reproducibility\n"
        "`python3 fetch_constituents.py`\n"
    )
    print(f"Wrote {readme}")


if __name__ == "__main__":
    main()
