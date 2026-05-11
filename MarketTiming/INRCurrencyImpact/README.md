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
| `plot_combined.py` | Chart 4 — all seven series from Charts 1-3 on a single chart with three y-axes (INR per USD on the left, median constituent close in the middle, index level on the far right). |
| `run_all.py` | Convenience entry point: builds and renders all four charts. |
| `inr_vs_usd.{png,csv}` | Chart 1 output and data. |
| `nifty_indices.{png,csv}` | Chart 2 output and data. |
| `constituent_medians.{png,csv}` | Chart 3 output and data. |
| `combined_all.{png,csv}` | Chart 4 output and data. |

## Run

```bash
pip install yfinance pandas matplotlib
python run_all.py
```

The lookback window is controlled by `YEARS_BACK` in each `plot_*.py`
(default: 25).

## Single trusted data source: Yahoo Finance

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
