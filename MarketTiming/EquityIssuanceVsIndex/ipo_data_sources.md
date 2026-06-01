# IPO Yearly Count & Amount — Data Sources (`ipo_data.csv`)

Preparation date: 2026-05-12.

This file documents every value in `ipo_data.csv`, the SEBI URL it came
from, and what each column means. All amounts are gross capital raised at
issue price (fresh + offer-for-sale), in INR crore. The SEBI tables count
an issue based on the listing date (since April 2018; opening date before).

## Year basis

- `fiscal_year` = Indian fiscal year (April Y-1 to March Y), the basis on
  which SEBI publishes data.
- `year_label` = the calendar year in which the fiscal year ends
  (FY 2001-02 → 2002). This is the convention used by the chart in
  `plot.py` and the columns in `data.csv`.

## Column definitions

| Column                       | Meaning                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| ipo_count_total              | Total IPOs (mainboard + SME) listed during the fiscal year.             |
| ipo_amount_cr_total          | Gross amount raised (₹ cr) by all those IPOs.                           |
| ipo_count_mainboard          | Mainboard IPOs only (where SEBI's table breaks this out — FY23 onward). |
| ipo_amount_cr_mainboard      | Gross amount raised by mainboard IPOs (₹ cr).                           |
| ipo_count_sme                | SME-platform IPOs only.                                                 |
| ipo_amount_cr_sme            | Gross amount raised by SME IPOs (₹ cr).                                 |

For FY 2001-02 through FY 2021-22, SEBI tables show one combined "IPOs"
column (which includes SME-platform IPOs from FY 2012-13 onward — the
SME platform launched in 2012). The mainboard / SME split is only
separately published from FY 2022-23 onward.

## Source files (downloaded and parsed)

| Period covered           | SEBI source                                            | URL                                                                                                                  |
|--------------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| FY 2001-02 to FY 2009-10 | Handbook of Statistics 2010, Table 5 (PDF)             | https://www.sebi.gov.in/sebi_data/attachdocs/1311148149770.pdf                                                       |
| FY 2010-11 to FY 2017-18 | Handbook of Statistics 2018 Part I, Table 1 (XLSX)     | https://www.sebi.gov.in/sebi_data/commondocs/jan-2020/HANDBOOK%20OF%20STATISTICS%20rev%20Part%20I%20Final_p.xlsx     |
| FY 2018-19               | SEBI Monthly Bulletin (June 2019 issue), Table 5       | https://www.sebi.gov.in/sebi_data/commondocs/jul-2019/sebibulletinjune2019excel_p.xlsx                               |
| FY 2019-20               | SEBI Monthly Bulletin (December 2020 issue), Table 5   | https://www.sebi.gov.in/sebi_data/commondocs/jan-2021/xl%20Bulletin%20Dec%202020_2_p.xlsm                            |
| FY 2020-21               | SEBI Monthly Bulletin (June 2021 issue), Table 5       | https://www.sebi.gov.in/sebi_data/commondocs/aug-2021/xls%20Bulletin%20Tables%20June%202021_p.xlsx                   |
| FY 2021-22               | SEBI Monthly Bulletin (October 2022 issue), Table 5B   | https://www.sebi.gov.in/sebi_data/commondocs/oct-2022/SEBI_Bulletin_Tables_October_2022_p.xlsx                       |
| FY 2022-23 and FY 2023-24| SEBI Monthly Bulletin (April 2024 issue), Table 6      | https://www.sebi.gov.in/sebi_data/commondocs/apr-2024/SEBI_Bulletin_April_2024_p.xlsx                                |
| FY 2024-25               | SEBI Monthly Bulletin (October 2025 issue), Table 6    | https://www.sebi.gov.in/sebi_data/commondocs/oct-2025/October%2025%20Bulletin%20Annexure%20Tables_p.xlsx             |

## Cross-checks (overlapping years across sources)

- FY 2010-11 to FY 2013-14 appear in both the 2014 Handbook (Table 9) and
  the 2017/2018 Handbooks (Table 1) with identical numbers — confirms
  table is stable once finalised.
- FY 2017-18 is reported as 201 IPOs / ₹83,684 cr in the 2018 Handbook;
  the Dec 2018 Bulletin shows 199 / ₹83,774 cr (small restatement of two
  issues). The Handbook value is used because it is the finalised
  end-of-year figure.

## Notes on definitions

- "Equity public issues also include issues listed on SME platform" —
  this caveat appears in every SEBI table from FY 2012-13 onward, so the
  combined `ipo_count_total` line is comparable across the whole series.
- Until April 2018, SEBI classified equity issues by **opening date**;
  from April 2018, by **listing date**. This causes a small
  reclassification at the FY 2017-18 / FY 2018-19 boundary but does not
  invalidate yearly comparisons.
- The IPO _amount_ in older SEBI tables is gross capital raised. The
  fresh-issue vs offer-for-sale split is only available from the
  consolidated table in SEBI bulletins from FY 2022-23 onward.

## How to extend

Future-year rows can be added by downloading the latest SEBI Monthly
Bulletin annexure XLSX from
https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=4&ssid=80&smid=107
and reading Sheet `6` (older bulletins: Sheet `5` or `5B`). The "IPO
(Total)" row C, columns "No. of Issues" / "Amount (₹ crore)", under the
"FY YYYY-YY" header gives the values directly.
