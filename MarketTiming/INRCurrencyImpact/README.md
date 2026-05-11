# INRCurrencyImpact

Yearly INR/USD exchange rate alongside Nifty 50, Nifty Midcap 100 and Nifty
Smallcap 100 index levels and constituent-price medians, for the **last 25
years**.

## Files

| File | Purpose |
| --- | --- |
| `constituents.py` | Current constituent lists for Nifty 50, Nifty Midcap 100 and Nifty Smallcap 100 (NSE ticker symbols). |
| `data_fetcher.py` | Yahoo Finance fetcher for INR/USD, the three indices and every constituent stock. CSV-caches each ticker to `.cache/` to avoid refetching. |
| `plot_inr_usd.py` | Chart 1 — INR per 1 USD, year-end close, 25-year line graph. |
| `plot_indices.py` | Chart 2 — Nifty 50 / Midcap 100 / Smallcap year-end close on one chart. |
| `plot_medians.py` | Chart 3 — median year-end close of constituent stocks in each of the three indices on one chart. |
| `fii_inflows.py` | Annual net FII equity inflows to **total** Indian equity from CDSL (INR crore, FY 1998-99 → FY 2024-25), USD-converted using FRED DEXINUS yearly average. |
| `plot_combined.py` | Chart 4 — 8 series on a single chart with four y-axes (INR/USD on the left, median constituent close, index level, and net FII inflow each on a separate right-side axis). |
| `plot_interactive.py` | Interactive Plotly HTML versions of all four charts — click legend to toggle lines, drag the range slider or use the quick-pick buttons to change the year window. |
| `run_all.py` | Convenience entry point: builds and renders all four charts (PNG **and** interactive HTML). |
| `inr_vs_usd.{png,csv}` / `inr_vs_usd_interactive.html` | Chart 1 output. |
| `nifty_indices.{png,csv}` / `nifty_indices_interactive.html` | Chart 2 output. |
| `constituent_medians.{png,csv}` / `constituent_medians_interactive.html` | Chart 3 output. |
| `combined_all.{png,csv}` / `combined_all_interactive.html` | Chart 4 output — 8 series (INR/USD, 3 index levels, 3 median constituent closes, total net FII equity inflow). |

### Interactive HTML controls

Every `*_interactive.html` exposes the same two controls:

1. **Enable/disable lines** — single-click any legend entry to hide that
   line; click again to show it; double-click an entry to isolate it
   (hide every other line).
2. **Adjust the year window** — drag either end of the range slider
   below the chart, click the **Last 5y / 10y / 15y / 25y / All**
   quick-pick buttons above the chart, or click-drag directly on the
   plot to zoom into a custom range. Double-click the plot to reset.

## Run

```bash
pip install yfinance pandas matplotlib
python run_all.py
```

The lookback window is controlled by `YEARS_BACK` in each `plot_*.py`
(default: 25).

## FII inflow data source

| Series | Source |
| --- | --- |
| Total India equity FII inflow (INR crore, by FY) | **CDSL** FPI/FII Investment Details (Financial Year): <https://www.cdslindia.com/Publications/FIIFPIInvstmntFinYrData.aspx> |
| INR/USD yearly average for USD conversion | FRED **DEXINUS** (India / U.S. Foreign Exchange Rate): <https://fred.stlouisfed.org/series/DEXINUS> |

### Why only the TOTAL FII series — not Nifty 50 / Midcap / Smallcap

CDSL/NSDL/SEBI/NSE do not publish net FII flow broken down by Nifty 50 /
Midcap 100 / Smallcap 100 as a clean, single-source data series. They
publish total India-equity FII flow (used here), FPI ownership % per
Nifty index, and per-stock FPI ownership — but not per-index flow.

Per-index flow can only be derived (e.g. by aggregating per-stock
shareholding-pattern changes across each index's constituents). An
earlier revision of this chart included such a derivation; it has been
removed at the reviewer's request so that every line on the chart is
sourced from actual, factually-published data rather than a derivation.

## Yahoo Finance source for prices

Every series in this module is fetched from Yahoo Finance via the
`yfinance` Python library. Specifically:

| Series | Ticker(s) |
| --- | --- |
| INR per 1 USD | `INR=X` |
| Nifty 50 (year-end close) | `^NSEI` |
| Nifty Midcap 100 (year-end close) | `NIFTY_MIDCAP_100.NS` |
| Nifty Smallcap (year-end close) | `BSE-SMLCAP.BO` *(Nifty Smallcap proxy — see note)* |
| Median Nifty 50 constituent close | 50 × `<SYMBOL>.NS` |
| Median Nifty Midcap 100 constituent close | 100 × `<SYMBOL>.NS` |
| Median Nifty Smallcap 100 constituent close | 100 × `<SYMBOL>.NS` |

### Notes

- **Data start dates** (Yahoo Finance has these as the earliest
  available bars):
  - `INR=X` — December 2003
  - `^NSEI` (Nifty 50) — September 2007
  - `NIFTY_MIDCAP_100.NS` — September 2005
  - `BSE-SMLCAP.BO` — April 2003 (last bar May 2024 on Yahoo)
  - Individual stocks vary by listing/IPO date.
- Years prior to a series' Yahoo start date appear blank on the chart.
- **Nifty Smallcap index proxy**: the official Nifty Smallcap 100 / 250
  tickers (`^CNXSC`, `NIFTYSMLCAP250.NS`) do not return historical bars
  from Yahoo Finance — only empty series — so the BSE Smallcap index is
  used as the smallcap benchmark for Chart 2. The constituent universe
  used for Chart 3 (median price) is still the actual current Nifty
  Smallcap 100 membership list.
- **Constituent universe**: the constituent lists are the *current* index
  membership snapshot (see `constituents.py`). Index membership changes
  semi-annually; using the current universe means the median is computed
  over the same set of names in every year (those that existed in that
  year), which gives a consistent like-for-like view.
- **Median methodology**: for each calendar year and each index, the
  median is taken across the year-end close prices of all *current*
  constituents that have price data for that year. Stocks that hadn't
  listed yet are excluded from that year's median.
