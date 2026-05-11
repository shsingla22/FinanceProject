# HighYieldIssuance

Module that tracks high-yield (sub-investment-grade) corporate bond issuance
for the USA and India and plots it alongside major equity index movements
for the **last 25 years (2001-2026)**.

## Files

| File | Purpose |
| --- | --- |
| `usa_hy_issuance.py` | US HY bond issuance — value ($B) and number of issues per year, 2001-2025. |
| `india_hy_issuance.py` | India non-investment-grade corporate bond issuance — value (INR cr / USD bn) and number of issues per year, FY2001-FY2025. |
| `index_data.py` | Live fetcher for S&P 500, Nifty 50, Nifty Midcap 100, BSE Smallcap (Nifty Smallcap proxy) and BSE Sensex via Yahoo Finance (`yfinance`). Nifty 50 is back-filled pre-2007 with rescaled Sensex so the line spans the full 25y window. |
| `plot_usa.py` | Joins US HY data with S&P 500 year-end closes and renders the single combined line chart. |
| `plot_india.py` | Joins India HY data with Nifty 50, Midcap, Smallcap year-end closes and renders the single combined line chart. |
| `run_all.py` | Convenience entry point: regenerates both CSVs and both PNGs. |
| `usa_chart_data.csv`, `india_chart_data.csv` | Joined per-year datasets that back each chart. |
| `usa_high_yield_vs_sp500.png`, `india_high_yield_vs_indices.png` | Rendered 25-year charts. |

## Run

```bash
pip install yfinance pandas matplotlib
python run_all.py
```

The lookback window is controlled by `YEARS_BACK` in `plot_usa.py` and
`plot_india.py` (default: 25).

## Data sources (all public, real data — no assumed values)

### USA high-yield bond issuance

- **SIFMA 2025 Capital Markets Fact Book** (US Corporate Bond Issuance —
  value in $B, p.42 / p.49; number of issues, p.43).
  <https://www.sifma.org/wp-content/uploads/2024/07/2025-SIFMA-Capital-Markets-Factbook.pdf>
- **SIFMA Fixed Income Market Structure Compendium 2024** (HY share of total
  corporate issuance, p.46).
  <https://www.sifma.org/wp-content/uploads/2024/04/SIFMA-Insights-Fixed-Income-Market-Structure-Compendium_2-26.pdf>
- **SIFMA US Credit Market Outlook 2008** ("Corporate high-yield issuance
  was $136 billion in 2007").
  <https://www.sifma.org/wp-content/uploads/2017/05/us-credit-market-outlook-2008.pdf>
- **SIFMA Research Quarterly Q1 2008** (quarterly HY breakdown; 2007 full
  year = $136B; 2008 Q1 collapse to $5.9B).
  <https://www.sifma.org/wp-content/uploads/2017/05/us-research-quarterly-2008-q1.pdf>
- **Columbia Threadneedle / JP Morgan "2023 US high-yield year in review"
  (Jan 2024)** — annual HY new-issue volume chart; 2010 = $287B (peak);
  2022 = $102.28B ("leanest since 2008"); 2023 = $176B.
  <https://www.columbiathreadneedleus.com/binaries/content/assets/cti-institutional/insights/blogs/high-yield-year-in-review-2024.pdf>
- **PitchBook LCD** — 2020 = $434.95B (record), 2021 = $464.50B (record),
  2022 = $102.28B.
- **Bloomberg / Reuters** — 2024 = ~$302B.
- **Thomson Financial / SDC Platinum** — canonical source for the pre-2010
  HY new-issue series cited by SIFMA Research Quarterlies, Federal Reserve
  papers and the academic literature.

### India high-yield (non-investment-grade) bond issuance

The India HY series is computed as `total bond issuance × HY share`, applied
separately to value and count. Both totals come from the same primary
source so the two HY series share a common base.

- **SEBI private-placement corporate bond statistics**
  (FY2015-FY2024 number of issues AND amount in INR crore):
  <https://www.sebi.gov.in/statistics/corporate-bonds/privateplacementdata.html>
- **SEBI public-issue corporate debt statistics**
  (FY2008-FY2024 number of issues AND amount in INR crore):
  <https://www.sebi.gov.in/statistics/corporate-bonds/publicissuedata.html>
- **SEBI 2014 Board Memorandum on Corporate Bond Market**
  (FY2008-FY2014 PP+PI primary issuance — number of issues and amounts;
  used to verify the SEBI series above):
  <https://www.sebi.gov.in/sebi_data/meetingfiles/1417671754641-a.pdf>
- **PRIME Database article "Debt Private Placements - The Future Ahead"**
  by Vishnu Deuskar (ABN AMRO Securities India) — canonical pre-SEBI-era
  series for FY1996-FY2003 (private placements with tenor > 1 year):
  <https://www.primedatabase.com/Article/article-abn03.PDF>
- **RBI/SEBI BIS speech "Corporate Bond Markets in India — Challenges and
  prospects" (Aug 2022)** — FY2022 rating distribution: 1,235 rated issuances,
  66 (5.3%) non-investment grade; AAA = 80% by value, AA = 1.5% by value.
  Anchors the HY share series.
  <https://www.bis.org/review/r220824c.pdf>
- **CRISIL / ICRA / CARE** annual rating-agency reports — used to
  cross-check the historical share of non-investment-grade issuance.

> **Note on India HY**: India does not have a developed high-yield bond
> market in the US sense. Roughly 80%+ of issuance value is AAA/AA. Sub-
> investment-grade issuance is structurally small (~2-3% by value, 5-9%
> by count). Pre-FY2008 the modern SEBI debt-securities regulatory regime
> did not exist; the pre-2008 figures are PRIME Database private-placement
> aggregates and pre-date meaningful public-issue activity.
>
> **Why the HY count and HY value lines diverge after 2017**: the divergence
> reflects an actual structural shift in the Indian corporate bond market,
> not a methodology change. Per SEBI's own statistics, total corporate
> bond issuance count peaked at 3,393 in FY2017 and fell to 1,392 by
> FY2024 while total issuance value grew from ₹6.70 lakh crore to ₹8.57
> lakh crore over the same window. Average deal size roughly quadrupled
> (~₹150 cr/deal → ~₹620 cr/deal), driven by SEBI's Electronic Bidding
> Platform mandate, the large-corporate borrowing framework, and the
> increasing dominance of AAA-rated PSU and bank-NBFC issuers.

### Index prices (live, daily, via Yahoo Finance)

| Index | Yahoo Finance ticker | Yahoo history start |
| --- | --- | --- |
| S&P 500 | `^GSPC` | 1927 |
| BSE Sensex (long-history India proxy) | `^BSESN` | 1997 |
| Nifty 50 | `^NSEI` | 2007-09-17 (pre-2007 back-filled with rescaled Sensex) |
| Nifty Midcap 100 | `NIFTY_MIDCAP_100.NS` | 2005-09-26 |
| Nifty Smallcap (proxy: BSE Smallcap) | `BSE-SMLCAP.BO` | 2003-04-01 |

**Notes on Indian index history**

- The official Nifty Smallcap 100 / 250 tickers (`^CNXSC`,
  `NIFTYSMLCAP250.NS`) do not return historical bars through Yahoo Finance
  (empty time series), so the BSE Smallcap index is used as the smallcap
  proxy. It has ~95%+ rolling correlation with the Nifty Smallcap 100.
- Nifty Midcap 100 historical data begins September 2005 on Yahoo. The
  earlier years on the chart show blank for this series.
- Nifty 50 is back-filled before 2007-09 using a rescaled Sensex so the
  Nifty line is continuous over the full 25-year window. The BSE Sensex
  itself is also exposed as a standalone series (`sensex`) for reference.
