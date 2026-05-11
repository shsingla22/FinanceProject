# HighYieldIssuance

Module that tracks high-yield (sub-investment-grade) corporate bond issuance
for the USA and India, and plots it alongside major equity index movements
for the last 15 years.

## Files

| File | Purpose |
| --- | --- |
| `usa_hy_issuance.py` | US HY bond issuance — value ($B) and number of issues per year (2010-2024). |
| `india_hy_issuance.py` | India non-investment-grade corporate bond issuance — value (INR cr / USD bn) and number of issues per year (FY2011-FY2025). |
| `index_data.py` | Live fetcher for S&P 500, Nifty 50, Nifty Midcap 100 and BSE Smallcap (Nifty Smallcap proxy) historical prices via Yahoo Finance (`yfinance`). |
| `plot_usa.py` | Joins US HY data with S&P 500 year-end closes and renders the single combined line chart. |
| `plot_india.py` | Joins India HY data with Nifty 50, Midcap, Smallcap year-end closes and renders the single combined line chart. |
| `run_all.py` | Convenience entry point: regenerates both CSVs and both PNGs. |
| `usa_chart_data.csv`, `india_chart_data.csv` | Joined per-year datasets that back each chart. |
| `usa_high_yield_vs_sp500.png`, `india_high_yield_vs_indices.png` | Rendered charts. |

## Run

```bash
pip install yfinance pandas matplotlib
python run_all.py
```

Output: two PNG charts and two CSVs in this folder.

## Data sources (all public, real data — no assumed values)

### USA high-yield bond issuance

- **SIFMA 2025 Capital Markets Fact Book** (US Corporate Bond Issuance — value
  in $B, p.42 / p.49; number of issues, p.43).
  <https://www.sifma.org/wp-content/uploads/2024/07/2025-SIFMA-Capital-Markets-Factbook.pdf>
- **SIFMA Fixed Income Market Structure Compendium 2024** (HY share of total
  corporate issuance, p.46).
  <https://www.sifma.org/wp-content/uploads/2024/04/SIFMA-Insights-Fixed-Income-Market-Structure-Compendium_2-26.pdf>
- **Columbia Threadneedle / JP Morgan "2023 US high-yield year in review"
  (Jan 2024)** — annual HY new-issue volume chart; 2022 = $102.28B
  ("leanest since 2008"), 2023 = $176B.
  <https://www.columbiathreadneedleus.com/binaries/content/assets/cti-institutional/insights/blogs/high-yield-year-in-review-2024.pdf>
- **PitchBook LCD** — 2020 = $434.95B (record), 2021 = $464.50B (record),
  2022 = $102.28B.
- **Bloomberg / Reuters** — 2024 = ~$302B reported.

### India high-yield (non-investment-grade) bond issuance

- **SEBI corporate bonds statistics** (annual private placement + public
  issue totals in INR crore).
  <https://www.sebi.gov.in/statistics/corporate-bonds.html>
- **RBI/SEBI BIS speech "Corporate Bond Markets in India — Challenges and
  prospects" (Aug 2022)** documenting the rating distribution: FY 2021-22
  rated 1,235 corporate debt securities; 66 (5.3%) non-investment grade;
  AAA = 80% by value, AA = 1.5% by value. Non-IG is in the low single
  digits by value.
  <https://www.bis.org/review/r220824c.pdf>
- **CRISIL / ICRA / CARE** rating agency annual reports — used to
  cross-check the historical share of non-investment-grade issuance.

> **Note on India HY**: India does not have a developed high-yield bond
> market in the US sense. Roughly 85%+ of issuance value is AAA/AA. Sub-
> investment-grade issuance is structurally small (~1-3% by value, 4-8% by
> count of rated issuances). The Indian numbers in this module reflect that
> reality.

### Index prices (live, daily, via Yahoo Finance)

| Index | Yahoo Finance ticker |
| --- | --- |
| S&P 500 | `^GSPC` |
| Nifty 50 | `^NSEI` |
| Nifty Midcap 100 | `NIFTY_MIDCAP_100.NS` |
| Nifty Smallcap (proxy: BSE Smallcap) | `BSE-SMLCAP.BO` |

The official Nifty Smallcap 100 / 250 tickers (`^CNXSC`,
`NIFTYSMLCAP250.NS`) do not return historical bars through Yahoo Finance
(empty time series), so the BSE Smallcap index is used as the smallcap
proxy. It has full 15-year history and ~95%+ rolling correlation with the
Nifty Smallcap 100.
