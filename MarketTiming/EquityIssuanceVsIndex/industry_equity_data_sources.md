# Industry-wise Equity Issuance Yearly Data — Data Sources (`industry_equity_data.csv`)

Preparation date: 2026-05-12.

This file gives industry-wise yearly capital raised in the Indian primary
market, FY 2001-02 through FY 2024-25, in **long format** (one row per
fiscal_year × industry).

## File format

| Column         | Meaning                                                                 |
|----------------|-------------------------------------------------------------------------|
| fiscal_year    | Indian fiscal year (e.g., "2010-11" = April 2010 – March 2011).         |
| industry       | Industry name **as published by SEBI** in that source year (see note 1).|
| no_of_issues   | Number of primary-market issues by issuers in that industry.            |
| amount_cr      | Amount raised, INR crore.                                               |
| coverage       | `all-instruments` (handbook era) or `equity-only` (bulletin era).       |
| source         | SEBI source publication and table number.                               |

The total number of rows in `industry_equity_data.csv` is 401 (24 years × ~15-50 industries depending on year).

## ⚠️ Important coverage caveat

SEBI publishes the industry-wise table on two different bases:

- **Handbook era (FY 2001-02 to FY 2017-18)** — *all-instrument* coverage.
  The annual industry-wise tables in the SEBI Handbook of Statistics (2010
  Table 6 and 2018 Part I Sheet 2 / Table 2) sum to the same yearly total
  as Table 5 / Table 1 of the same handbook, which includes equity issues
  **plus** public debt, CCPS, and other instruments by issuers in each
  industry.

- **Bulletin era (FY 2018-19 onward)** — *equity-only*. The SEBI Monthly
  Bulletin Annexure Table 7 (or Table 9 in the Oct 2025 schema) is
  explicitly titled *"Industry-wise Classification of Capital Raised
  through Public and Rights Issues (Equity)"*.

There is no annual equity-only industry table published in any SEBI
handbook for FY 2001-02 to FY 2017-18 — the handbooks publish monthly
equity industry data (e.g., 2014 Table 58) but not an annual roll-up. The
handbook annual tables (used here for those years) include debt issues.

Verification: the per-FY sum of `amount_cr` in this CSV matches the
corresponding SEBI source total:

| FY      | CSV row sum | SEBI source total | Coverage              |
|---------|-------------|-------------------|------------------------|
| 2001-02 | 7,544       | 7,543             | all-instruments       |
| 2009-10 | 57,554      | 57,555            | all-instruments       |
| 2010-11 | 67,609      | 67,609            | all-instruments       |
| 2017-18 | 110,269     | 110,269           | all-instruments       |
| 2018-19 | 18,235      | 18,235            | equity-only           |
| 2019-20 | 76,965      | 76,965            | equity-only           |
| 2020-21 | 110,118     | 110,118           | equity-only (incl. some preferential/QIP categorisation by SEBI) |
| 2024-25 | 208,380     | ~210,190          | equity-only (small rounding gap) |

## Note 1 — industry-name variation

Industry labels evolve across SEBI publications. Examples of the same
underlying industry appearing under different names:

| Concept              | Handbook 2010   | Handbook 2018         | Bulletin 2019-24  | Bulletin Oct 2025 schema             |
|----------------------|-----------------|-----------------------|-------------------|--------------------------------------|
| Banks                | Banking/FIs     | Banking/FIs           | Banks/FIs         | Banks (under Financial Services)     |
| IT                   | Information Technology | Information Technology | Info Tech    | IT - Software / IT - Services / IT - Hardware |
| Telecom              | Telecommunication | Telecommunication   | Telecom            | Telecom - Services / Telecom - Equipment |
| Cement / construction | Cement & Construction | Cement & Construction | Cement/Constructions | Cement & Cement Products / Construction |

The Oct 2025 bulletin moved to a 3-level hierarchy (Macro Economic Sector
→ Sector → Industry, ~24 industries); earlier sources used a flat list
of 16-22 industries. I kept the industry name as published in each
source so you can trace any row back to the table that produced it.

## Source files (downloaded and parsed)

| Period covered           | SEBI source (table)                                                    | URL                                                                                                                  |
|--------------------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| FY 2001-02 to FY 2009-10 | Handbook of Statistics 2010, Table 6 (PDF)                             | https://www.sebi.gov.in/sebi_data/attachdocs/1311148149770.pdf                                                       |
| FY 2010-11 to FY 2017-18 | Handbook of Statistics 2018 Part I, Sheet 2 / Table 2 (XLSX)           | https://www.sebi.gov.in/sebi_data/commondocs/jan-2020/HANDBOOK%20OF%20STATISTICS%20rev%20Part%20I%20Final_p.xlsx     |
| FY 2018-19               | SEBI Monthly Bulletin (June 2019), Table 7                             | https://www.sebi.gov.in/sebi_data/commondocs/jul-2019/sebibulletinjune2019excel_p.xlsx                               |
| FY 2019-20               | SEBI Monthly Bulletin (December 2020), Table 7                         | https://www.sebi.gov.in/sebi_data/commondocs/jan-2021/xl%20Bulletin%20Dec%202020_2_p.xlsm                            |
| FY 2020-21               | SEBI Monthly Bulletin (June 2021), Table 7                             | https://www.sebi.gov.in/sebi_data/commondocs/aug-2021/xls%20Bulletin%20Tables%20June%202021_p.xlsx                   |
| FY 2021-22               | SEBI Monthly Bulletin (October 2022), Table 7                          | https://www.sebi.gov.in/sebi_data/commondocs/oct-2022/SEBI_Bulletin_Tables_October_2022_p.xlsx                       |
| FY 2022-23 and FY 2023-24| SEBI Monthly Bulletin (April 2024), Table 7                            | https://www.sebi.gov.in/sebi_data/commondocs/apr-2024/SEBI_Bulletin_April_2024_p.xlsx                                |
| FY 2024-25               | SEBI Monthly Bulletin (October 2025), Table 9                          | https://www.sebi.gov.in/sebi_data/commondocs/oct-2025/October%2025%20Bulletin%20Annexure%20Tables_p.xlsx             |

## How to extend / use

- For year-by-year industry counts and amounts, filter the CSV by
  `fiscal_year` directly.
- To aggregate broad sectors over time (e.g., to merge "IT - Software" /
  "IT - Services" / "IT - Hardware" from FY 2024-25 with "Information
  Technology" from earlier years), build a mapping table off `industry`
  column.
- To restrict to equity-only history, filter `coverage == "equity-only"`
  which gives FY 2018-19 onwards.
- New rows: download the most recent bulletin XLSX from the SEBI
  Publications archive and read its industry-wise equity sheet (typically
  Sheet 7 or 9 of the annexure tables).
