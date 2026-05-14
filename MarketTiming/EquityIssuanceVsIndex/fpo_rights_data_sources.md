# FPO + Rights Combined Yearly Data — Data Sources (`fpo_rights_data.csv`)

Preparation date: 2026-05-12.

This file documents every value in `fpo_rights_data.csv`. The series
covers **equity** FPO + equity Rights issues, FY 2001-02 through
FY 2024-25, sourced from SEBI Handbooks of Statistics and SEBI Monthly
Bulletin Annexure Tables.

## Year basis

- `fiscal_year` = Indian fiscal year (April Y-1 to March Y).
- `year_label` = the calendar year in which the fiscal year ends
  (FY 2001-02 → 2002).

## Column definitions

| Column                  | Meaning                                                                  |
|-------------------------|--------------------------------------------------------------------------|
| fpo_rights_count        | Combined equity FPO + equity Rights count (the primary series).          |
| fpo_rights_amount_cr    | Combined equity FPO + equity Rights amount, ₹ crore.                     |
| fpo_count               | Equity FPO count alone (only populated where SEBI publishes split).      |
| fpo_amount_cr           | Equity FPO amount, ₹ crore.                                              |
| rights_count            | Equity Rights count alone.                                               |
| rights_amount_cr        | Equity Rights amount, ₹ crore.                                           |
| methodology             | How the row was computed (see "Methodology" below).                      |
| source                  | SEBI publication providing the data.                                     |

## Methodology

SEBI tables classify primary-market issuance in three orthogonal ways:
1. **Category** — Public vs. Rights.
2. **Issuer Type** — IPOs (first-time listings) vs. Listed (already-listed companies).
3. **Instrument** — At Par equity, At Premium equity, CCPS, Bonds, Others.

By construction, the **Listed issuer-type column = equity FPO + equity Rights
+ debt FPOs + debt rights by listed companies**. So:

- **FY 2018-19 onwards** (SEBI Bulletin era): Bulletin Table 5 / 5B is
  titled *"Capital Raised from the Primary Market through Public and Rights
  Issues (Equity)"* — the **Listed** issuer-type column is already
  equity-only. Used directly.

- **FY 2001-02 to FY 2017-18** (SEBI Handbook era): Handbook Table 5 / 9 /
  Table 1 mixes equity and debt in the Listed column. Equity-only
  FPO + Rights is derived as:

      equity FPO + Rights count  = (At Par + At Premium) count - IPO count
      equity FPO + Rights amount = (At Par + At Premium) amount - IPO amount

  This relies on the assumption that **all IPOs are equity** (the standard
  Indian convention; debt IPOs are rare). For one year (FY 2011-12) the
  assumption fails (IPO count = 54 exceeds equity total count = 51, so
  ≥ 3 IPOs were debt instruments). For that year the Rights category count
  and amount are used as the FPO + Rights value (since rights are
  near-universally equity-only).

- **FY 2022-23 onwards** (new bulletin format with explicit FPO + Rights
  split): the consolidated table (Table 5 / Table 6 of bulletins from
  April 2024 onwards) gives FPO (Mainboard + SME) and Rights as separate
  rows. Summed directly.

## Source files (downloaded and parsed)

| Period covered           | SEBI source (table)                                    | URL                                                                                                                  |
|--------------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| FY 2001-02 to FY 2009-10 | Handbook of Statistics 2010 (Table 5, PDF)             | https://www.sebi.gov.in/sebi_data/attachdocs/1311148149770.pdf                                                       |
| FY 2010-11 to FY 2017-18 | Handbook of Statistics 2018 Part I (Table 1, XLSX)     | https://www.sebi.gov.in/sebi_data/commondocs/jan-2020/HANDBOOK%20OF%20STATISTICS%20rev%20Part%20I%20Final_p.xlsx     |
| FY 2018-19               | SEBI Monthly Bulletin (June 2019, Table 5)             | https://www.sebi.gov.in/sebi_data/commondocs/jul-2019/sebibulletinjune2019excel_p.xlsx                               |
| FY 2019-20               | SEBI Monthly Bulletin (December 2020, Table 5)         | https://www.sebi.gov.in/sebi_data/commondocs/jan-2021/xl%20Bulletin%20Dec%202020_2_p.xlsm                            |
| FY 2020-21               | SEBI Monthly Bulletin (June 2021, Table 5)             | https://www.sebi.gov.in/sebi_data/commondocs/aug-2021/xls%20Bulletin%20Tables%20June%202021_p.xlsx                   |
| FY 2021-22               | SEBI Monthly Bulletin (October 2022, Table 5B)         | https://www.sebi.gov.in/sebi_data/commondocs/oct-2022/SEBI_Bulletin_Tables_October_2022_p.xlsx                       |
| FY 2022-23 and FY 2023-24| SEBI Monthly Bulletin (April 2024, Table 6)            | https://www.sebi.gov.in/sebi_data/commondocs/apr-2024/SEBI_Bulletin_April_2024_p.xlsx                                |
| FY 2024-25               | SEBI Monthly Bulletin (October 2025, Table 6)          | https://www.sebi.gov.in/sebi_data/commondocs/oct-2025/October%2025%20Bulletin%20Annexure%20Tables_p.xlsx             |

## Source-table extracts (raw values used in derivation)

### Handbook 2010 Table 5, instrument-wise panel (FY 2001-02 to FY 2009-10)

| FY      | At Par No / Amt | At Prem No / Amt | Equity Tot No / Amt | IPO No / Amt    | Derived (Eq − IPO) |
|---------|-----------------|------------------|---------------------|-----------------|--------------------|
| 2001-02 | 7 / 151         | 8 / 1,121        | 15 / 1,272          | 7 / 1,202       | 8 / 70             |
| 2002-03 | 6 / 143         | 11 / 1,314       | 17 / 1,457          | 6 / 1,039       | 11 / 418           |
| 2003-04 | 14 / 360        | 37 / 18,589      | 51 / 18,949         | 21 / 3,434      | 30 / 15,515        |
| 2004-05 | 6 / 420         | 49 / 23,968      | 55 / 24,388         | 23 / 13,749     | 32 / 10,639        |
| 2005-06 | 10 / 372        | 128 / 27,000     | 138 / 27,372        | 79 / 10,936     | 59 / 16,436        |
| 2006-07 | 2 / 12          | 119 / 32,889     | 121 / 32,901        | 77 / 28,504     | 44 / 4,397         |
| 2007-08 | 7 / 387         | 113 / 79,352     | 120 / 79,739        | 85 / 42,595     | 35 / 37,144        |
| 2008-09 | 5 / 96          | 40 / 14,176      | 45 / 14,272         | 21 / 2,082      | 24 / 12,190        |
| 2009-10 | 1 / 9           | 71 / 54,866      | 72 / 54,875         | 39 / 24,696     | 33 / 30,179        |

### Handbook 2018 Part I Table 1 (FY 2010-11 to FY 2017-18)

| FY      | At Par No / Amt | At Prem No / Amt | Equity Tot No / Amt | IPO No / Amt    | Derived (Eq − IPO)        |
|---------|-----------------|------------------|---------------------|-----------------|---------------------------|
| 2010-11 | 2 / 50          | 78 / 57,617      | 80 / 57,667         | 53 / 35,559     | 27 / 22,108               |
| 2011-12 | 4 / 104         | 47 / 12,753      | 51 / 12,857         | 54 / 41,515     | -3 → fall back to Rights  |
| 2012-13 | 4 / 571         | 45 / 14,902      | 49 / 15,473         | 33 / 6,528      | 16 / 8,945                |
| 2013-14 | 19 / 824        | 36 / 12,445      | 55 / 13,269         | 38 / 1,236      | 17 / 12,033               |
| 2014-15 | 8 / 49          | 55 / 8,740       | 63 / 8,788          | 46 / 3,311      | 17 / 5,477                |
| 2015-16 | 13 / 672        | 74 / 23,382      | 87 / 24,054         | 74 / 14,815     | 13 / 9,239                |
| 2016-17 | 1 / 3           | 117 / 32,518     | 118 / 32,521        | 106 / 29,104    | 12 / 3,417                |
| 2017-18 | 20 / 16,354     | 203 / 88,742     | 223 / 105,097       | 201 / 83,684    | 22 / 21,413               |

### Bulletin era — Listed column from equity-only Table 5 / 5B

| FY      | Listed (eq) No / Amt | Public eq | Rights eq    | IPO eq     |
|---------|----------------------|-----------|--------------|------------|
| 2018-19 | 10 / 2,149           | 123/16,087 | 10/2,149    | 123/16,087 |
| 2019-20 | 19 / 55,679          | 60/21,323 | 16/55,642   | 57/21,286  |
| 2020-21 | 19 / 78,987          | 41/39,678 | 18/63,987   | 40/24,678  |
| 2021-22 | 44 / 26,342          | 121/112,568| 43/26,327  | 120/112,553 |

### Bulletin era — explicit FPO / Rights from consolidated Table 6

| FY      | FPO No / Amt   | Rights No / Amt | Sum (FPO+Rights) No / Amt |
|---------|----------------|-----------------|---------------------------|
| 2022-23 | 1 / 4,300      | 73 / 6,751      | 74 / 11,051               |
| 2023-24 | 1 / 27         | 67 / 15,110     | 68 / 15,137               |
| 2024-25 | 2 / 18,150     | 142 / 19,712    | 144 / 37,862              |

## Notes

- The huge FY 2019-20 Rights figure (₹55,642 cr) is dominated by Reliance
  Industries' rights issue (~₹53,124 cr in May/June 2020).
- The FY 2020-21 figure includes follow-on activity from listed cos
  during the post-COVID-19 capital-raising wave.
- The FY 2024-25 jump in FPO+Rights amount is driven by Vodafone Idea's
  ₹18,000 cr FPO (1 issue) plus 142 Rights issues totalling ₹19,712 cr.

## How to extend

For each future fiscal year, download the SEBI Monthly Bulletin annexure
XLSX from the publications archive
(https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=4&ssid=80&smid=107)
and read either Table 5 (equity-only, "Listed" column) for years before
the FPO/Rights split, or Table 6 (Consolidated Resource Mobilisation,
rows "F. FPO (Total)" + "H. Rights Issue") for the new format. Append a
row to `fpo_rights_data.csv` and rerun any chart script.
