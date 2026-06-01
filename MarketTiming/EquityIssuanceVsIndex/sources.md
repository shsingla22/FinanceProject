# Data Sources & Provenance — EquityIssuanceVsIndex

This document records the source of every numeric value in `data.csv`.

Preparation date: 2026-05-12.

## Year basis (important)

The user requested calendar-year data. SEBI's official statistics for
2001-2017 only exist on a fiscal-year (April–March) basis, while
calendar-year data is reliably available from 2021 onward via news
aggregation citing PRIME Database. To keep the dataset honest:

- Rows 2001-2020 use **Fiscal Year ending in March of that year**
  (i.e. row "2002" = FY 2001-02 = Apr-01 to Mar-02). Column `year_basis`
  is set to `FY ending Mar`.
- Rows 2021-2025 use **Calendar Year Jan-Dec** (column = `CY (Jan-Dec)`).

The Nifty year-end-close values are always CY (Dec 31). The chart pairs
each row's issuance number with that row's Nifty Dec-31 close. Within a
given year-label, the issuance window and the index close are offset by
~9 months for 2001-2020 rows.

If you need a pure CY dataset, the SEBI 2018 Handbook of Statistics has
month-level public-issues data that can be re-aggregated to CY for
2010-2018; the SEBI Oct-2025 bulletin Annexure Tables provide that for
the current period.

## Conventions for amounts

- All amounts in INR crore (1 crore = 10 million).
- `ipo_amount_cr` is the gross capital raised at issue price (fresh +
  offer-for-sale). SEBI's older handbooks do not separate fresh from
  OFS. For FY 2024-25 the SEBI Oct-2025 bulletin shows the split was
  ₹66,704 cr fresh + ₹105,624 cr OFS = ₹172,328 cr total across 320
  mainboard + SME IPOs. Earlier rows are gross only.
- `fpo_amount_cr` is derived as (Public issues amount − IPO amount)
  from SEBI Table 1/Table 5 of the handbooks. This is a conservative
  proxy: it includes a small amount of public debt issuance by listed
  companies in some years (e.g. FY13-14, where most of the gap is
  bonds), so use with caution. For pure equity FPO splits, see PRIME
  Database.
- `total_capital_raised_cr` is total primary-market equity mobilisation:
  IPO + FPO + Rights + Preferential + QIP. Calendar-year values are from
  PRIME Database (cited in Business Standard, Equentis, prokerala).
  FY-basis values for 2015-2017 are the SEBI handbook "Total" column
  for public+rights+listed equity issuance.

## Nifty 50 year-end close (verified, complete)

Aggregated public reporting of NSE Nifty 50 year-end closing values,
cross-referenced via Wikipedia and Yahoo Finance/Investing.com. 2025
close (26,130) from Business Standard year-end report (31 Dec 2025).

## Nifty Midcap 100 year-end close (partial)

Verified for 2015-2024 from public market summaries. Values prior to
2015 and the 2025 year-end close could not be cross-verified at
preparation time and are left blank.

## Nifty Smallcap 100 year-end close (gaps)

Index launched 30 March 2011 with base date 1 January 2004 (base = 1000).
NSE Nifty Indices and Yahoo Finance restrict programmatic access. Best
free public surface mentions 1-yr return of ~15% to mid-2026 (no
year-end Dec-31 closes recoverable from snippets). All values left
blank — fill from https://www.niftyindices.com/reports/historical-data
(CSV export) after manual download.

## Nifty Smallcap 100 constituent median (gaps)

Definition (per user): median of the year-end closing prices of the 100
Nifty Smallcap 100 constituent stocks. Reliable historical computation
requires:
  1. Year-end constituent lists from NSE Indices (semi-annually revised).
  2. Adjusted closing prices for each constituent on each year-end date
     (split/bonus/consolidation adjusted) from NSE Bhavcopy archives.

Not surfacable from free web snippets. All values left blank.

## IPO / FPO / Total — source table

Numbers below are reproduced from primary sources:

### FY 2001-02 to FY 2009-10
Source: SEBI Handbook of Statistics on the Indian Securities Market
2010, Table 5 "Resources Mobilised from the Primary Market"
https://www.sebi.gov.in/sebi_data/attachdocs/1311148149770.pdf

| FY      | Total Pub+Rts | Public Amt | IPO No | IPO Amt | FPO No (derived) | FPO Amt (derived) |
|---------|---------------|------------|--------|---------|------------------|-------------------|
| 2001-02 | 35 / 7,543    | 6,502      | 7      | 1,202   | 13               | 5,300             |
| 2002-03 | 26 / 4,070    | 3,639      | 6      | 1,039   | 8                | 2,600             |
| 2003-04 | 57 / 23,272   | 22,265     | 21     | 3,434   | 14               | 18,831            |
| 2004-05 | 60 / 28,256   | 24,640     | 23     | 13,749  | 11               | 10,891            |
| 2005-06 | 139 / 27,382  | 23,294     | 79     | 10,936  | 24               | 12,358            |
| 2006-07 | 124 / 33,508  | 29,796     | 77     | 28,504  | 8                | 1,292             |
| 2007-08 | 124 / 87,029  | 54,511     | 85     | 42,595  | 7                | 11,916            |
| 2008-09 | 47 / 16,220   | 3,582      | 21     | 2,082   | 1                | 1,500             |
| 2009-10 | 76 / 57,555   | 49,236     | 39     | 24,696  | 8                | 24,540            |

### FY 2010-11 to FY 2017-18
Source: SEBI Handbook of Statistics on the Indian Securities Market 2018,
Table 1, Part I XLSX
https://www.sebi.gov.in/sebi_data/commondocs/jan-2020/HANDBOOK%20OF%20STATISTICS%20rev%20Part%20I%20Final_p.xlsx

| FY      | Public No / Amt | IPO No / Amt   | FPO No (derived) / Amt | Total (Pub+Rts) |
|---------|-----------------|----------------|------------------------|-----------------|
| 2010-11 | 68 / 58,105     | 53 / 35,559    | 15 / 22,546            | 67,609          |
| 2011-12 | 55 / 46,093     | 54 / 41,515    | 1 / 4,578              | 48,468          |
| 2012-13 | 53 / 23,510     | 33 / 6,528     | 20 / 16,982            | 32,455          |
| 2013-14 | 75 / 51,075     | 38 / 1,236     | 37 / 49,839 (mostly bonds) | 55,652      |
| 2014-15 | 70 / 12,452     | 44 / 3,311     | 26 / 9,141             | 19,202          |
| 2015-16 | 95 / 48,927     | 74 / 14,815    | 21 / 34,112            | 58,166          |
| 2016-17 | 122 / 58,651    | 106 / 29,104   | 16 / 29,547            | 62,067          |
| 2017-18 | 210 / 88,869    | 201 / 83,684   | 9 / 5,185              | 110,269         |

### FY 2018-19 / FY 2019-20 / FY 2020-21 (gaps)
The SEBI handbooks for these years (2019, 2020, 2021, 2022) published
on sebi.gov.in are now TOC-only PDFs; their data XLSX files are no
longer accessible at the historical URL pattern. Calendar-year
aggregates from PRIME Database below cover this period instead.

### CY 2021 — CY 2025 (calendar year, PRIME Database)
Sources (all cite PRIME Database):
- Business Standard, "Fundraising via equity, debt hit all-time high
  in 2024: Prime Database" (9 Jan 2025).
- 5paisa news, "How public equity fundraising more than halved in 2022"
  (PRIME Database cited).
- Business Standard, "QIPs hit all-time high in 2024, exceeds Rs 1
  trillion" (15 Dec 2024).
- Business Standard, "India 2025 IPOs: Record listings" (30 Dec 2025).
- Whalesbook, "India's IPO Boom Masks 18% Fundraising Crash" (Dec 2025).

| CY   | Mainboard IPO | Mainboard IPO Amt | Total Public Equity (PRIME) |
|------|---------------|-------------------|------------------------------|
| 2021 | n/a in snip   | n/a in snip       | 2,02,048                     |
| 2022 | n/a in snip   | n/a in snip       | 90,995                       |
| 2023 | 57            | 49,434            | 1,44,000                     |
| 2024 | 90            | 1,64,000          | 3,73,000                     |
| 2025 | 102-103       | 1,76,000-1,80,000 | 3,06,000                     |

CY 2021 / CY 2022 IPO count and amount and FPO data per year were not
surfacable verbatim from free aggregator snippets at preparation time
(cells left blank). PRIME Database access would close these gaps.

### FY 2024-25 (latest full FY, for cross-reference)
Source: SEBI Bulletin October 2025, Annexure Table 6 XLSX
https://www.sebi.gov.in/sebi_data/commondocs/oct-2025/October%2025%20Bulletin%20Annexure%20Tables_p.xlsx

- IPO Main Board: 79 issues, ₹1,62,517 cr (fresh ₹57,639 + OFS ₹1,04,878)
- IPO SME: 241 issues, ₹9,811 cr
- IPO Total: 320 issues, ₹1,72,328 cr
- FPO Main Board: 1 issue, ₹18,000 cr (fresh)
- FPO SME: 1 issue, ₹150 cr
- Rights: 142 issues, ₹19,712 cr
- Preferential: 988 issues, ₹84,084 cr
- QIPs: 91 issues, ₹1,35,597 cr
- Total Equity Raised: 1,543 issues, ₹4,29,870 cr (FY24-25 SEBI definition)

## How to complete the dataset

1. Subscribe to PRIME Database "Public Issues" calendar-year summary
   for CY 2018, 2019, 2020 (gap years for total + IPO + FPO + QIP).
2. Download Nifty Smallcap 100 and Nifty Midcap 100 historical EOD data
   from https://www.niftyindices.com/reports/historical-data — take the
   31 December close (or last NSE trading day of December) of each year.
3. For the smallcap constituent median: from NSE Indices, download the
   "Nifty Smallcap 100 — index constituents" file effective at each
   31 December; then fetch each constituent's adjusted close on that
   date from NSE Bhavcopy archives; compute `median(prices)`.
4. Append values into `data.csv` and re-run `python3 plot.py`.
