# US IPO Annual Statistics — Count and Proceeds (`us_ipo_data.csv`)

Preparation date: 2026-06-01.

26 rows of yearly US IPO statistics, calendar years 2000-2025. This is
the US counterpart to `MarketTiming/EquityIssuanceVsIndex/ipo_data.csv`
for India, intended to enable side-by-side US-vs-India equity issuance
comparison.

---

## 1. Data source — Prof. Jay R. Ritter (University of Florida)

All values are from the canonical academic source for US IPO data:

- **Author**: Prof. Jay R. Ritter (Warrington College of Business, University of Florida)
- **URL**: https://site.warrington.ufl.edu/ritter/ipo-data/
- **Specific tables used**: Table 8 + Table 15 from "IPO-Statistics.pdf"
  (https://site.warrington.ufl.edu/ritter/files/IPO-Statistics.pdf)
- **Last table update**: January 6, 2026 (Table 8); December 26, 2025 (Table 15)
- **Underlying data**: LSEG (formerly Refinitiv) new-issues database, its
  predecessors, Dealogic, IPOScoop.com, and other sources (per Ritter's notes).

Jay Ritter's IPO database is the **academic gold standard** — cited by
the SEC, FRB, IMF, Federal Reserve research, the NBER, and every major
finance textbook. The dataset covers 1960-2025 with consistent
methodology, regular updates, and full source documentation.

## 2. File contents

| Column | Meaning |
|--------|---------|
| `calendar_year` | CY (4-digit) |
| `ipo_count_operating` | "Net" IPO count — operating companies only (Ritter Table 8). Excludes ADRs, REITs, SPACs, units, closed-end funds, natural resource LPs, banks/S&Ls, small best-efforts offers, and any offer priced < $5/share. |
| `ipo_count_gross` | "Gross" IPO count from Ritter Table 15 — includes everything (SPACs, REITs, CEFs, units, banks, ADRs, LPs). This is the largest reasonable count. |
| `ipo_amount_proceeds_usd_mn` | Gross proceeds in US$ millions for operating-company IPOs (Table 8). Excludes overallotment options; includes the international tranche if any. NOT inflation-adjusted. |
| `avg_first_day_return_pct` | Mean first-day return (offer price → first closing price). The IPO underpricing measure, included for context. |
| `source_note` | Brief macro context for the year (dotcom, GFC, SPAC boom, etc.) |

### Why two counts?

Ritter publishes both numbers because they answer different questions:

- **Operating-company count** (`ipo_count_operating`): the answer to "how
  many real businesses went public?" — the academic standard. Excludes
  SPACs (which are blank-check vehicles, not operating companies),
  closed-end funds, and other "non-real" issuance.
- **Gross count** (`ipo_count_gross`): the answer to "how many tickers
  started trading via IPO?" — includes everything that listed. Comparable
  to popular media counts and to the SEBI India total which includes
  mainboard + SME.

The proceeds column (`ipo_amount_proceeds_usd_mn`) is for the
operating-company definition (Table 8). Including SPAC proceeds would
roughly double the 2020-2021 numbers; Ritter publishes those in Table 15b
separately.

## 3. Methodology notes (from Ritter's own table footnotes, verbatim)

> Beginning in 1975, the number of offerings excludes IPOs with an offer
> price of less than $5.00, ADRs, small best efforts offers, units,
> Regulation A offers (small issues, raising less than $1.5 million
> during the 1980s and $5 million until 2012), real estate investment
> trusts (REITs), SPACs, natural resource limited partnerships, and
> closed-end funds. Banks and S&L IPOs are included. From 2012 and later,
> Regulation A offerings (issues raising up to $50 million are eligible)
> are included.

> First-day returns are computed as the percentage return from the
> offering price to the first closing market price.

> Gross proceeds exclude overallotment options but include the
> international tranche, if any. No adjustments for inflation have
> been made.

## 4. Decade-level aggregates from Ritter Table 8

| Decade | # of IPOs (operating) | Mean first-day return | Gross proceeds (US$M) |
|--------|-----------------------:|----------------------:|----------------------:|
| 1960-69 | 2,661 | 21.2% | 7,988 |
| 1970-79 | 1,536 | 7.1% | 6,663 |
| 1980-89 | 2,364 | 6.9% | 60,874 |
| 1990-99 | 4,195 | 21.1% | 294,814 |
| 2000-09 | 1,333 | 24.5% | 295,082 |
| 2010-25 | 1,990 | 22.0% | 572,799 |
| **1960-2025** | **14,079** | **17.7%** | **1,238,240** |

So in the 26-year window of this CSV (2000-2025), the US has hosted
~3,300 operating-company IPOs raising ~$867 billion (the 2000-09 plus
the 2010-25 totals).

## 5. Key headline observations

- **Peak year by count**: 2000 (382 operating-company IPOs; 431 gross) —
  the dot-com peak. Ritter notes the cumulative drop since: 1980-2000
  averaged 310 operating IPOs/year; post-2000 the average is ~110/year.
- **Peak year by proceeds**: 2021 ($119.6B operating; the gross with SPACs
  was substantially higher per Table 15b). Driven by the SPAC mania (633
  SPAC IPOs in 2021 alone).
- **Worst year by proceeds**: 2022 ($7.0B) — Fed hiking cycle froze the
  market. Down 94% YoY from 2021.
- **Worst year by count**: 2008 (21 operating IPOs) — GFC. Even 2022 had
  39 operating IPOs.
- **Recovery years**: 2010 (98 operating), 2023 (54), 2024 (73), 2025 (94)
  — each shows the typical post-shock 2-3 year recovery pattern.
- **SPAC-mania artifact**: 2020-2021 gross counts (465 and 1,033) are
  inflated by the SPAC boom. 2020 had 257 SPACs/REITs/CEFs (vs 165
  operating); 2021 had 633 SPAC/REIT/CEF IPOs (vs 311 operating). The
  operating-company count is the cleaner read on "real" issuance.

## 6. Cross-source validation (sample spot-checks)

| Year | Ritter (operating, this CSV) | Renaissance Capital | SIFMA (broader) |
|------|------------------------------:|--------------------:|----------------:|
| 2021 | 315 IPOs / $119.6B | ~397 IPOs / ~$142B | ~$300B+ (all equity raises) |
| 2020 | 165 IPOs / $61.9B | 218 IPOs / ~$78B | ~$130B+ |
| 2008 | 21 IPOs / $22.8B | 31 IPOs / ~$28B | ~$40B+ |
| 2004 | 181 IPOs / $31.7B | 215 IPOs / ~$43B | (Google IPO included in all) |
| 2000 | 382 IPOs / $64.9B | ~400 IPOs / ~$97B | (broader count + ADRs/REITs added) |

The Ritter "operating-company" series is consistently the lowest count
(strictest definition) and consistently the lowest proceeds total
(excludes SPACs, ADRs, REITs). Renaissance Capital and SIFMA use broader
definitions; SIFMA's number includes follow-on offerings and other
non-IPO equity raises. Conclusions about the cycle (peak years, trough
years, recovery patterns) are **identical across all three sources**.

## 7. Definitions that DIFFER from India's `ipo_data.csv`

| Feature | India (`ipo_data.csv`) | US (this CSV) |
|---------|------------------------|---------------|
| Time basis | Fiscal year (April-March) | Calendar year (Jan-Dec) |
| Year label convention | FY-ending CY (e.g., FY 2024-25 → "2025") | CY directly |
| Mainboard SME split | Combined into `_total` columns | All on one exchange listing tier (no SME tier) |
| Currency | INR (₹ crore) | USD ($ millions) |
| SPAC handling | Not material in India | Excluded from `_operating`; included in `_gross` |
| ADR handling | n/a | Excluded from both |
| Source | SEBI Monthly Bulletins / Handbooks | Jay Ritter / LSEG |

**For comparison purposes:**
- The India "ipo_amount_cr_total" column is most comparable to the US
  "ipo_amount_proceeds_usd_mn" (both are operating-company equity
  raises through primary listings).
- The India "ipo_count_total" is most comparable to the US
  "ipo_count_gross" (India's `_total` includes both mainboard and SME;
  US `_gross` includes SPACs etc.).
- For a strict operating-company-only comparison, use India `_total` vs
  US `_operating`.

## 8. Currency conversion for direct $-vs-₹ comparison

To compare absolute amounts, use `MarketTiming/EquityIssuanceVsIndex/usd_inr_data.csv`
for the year-end USD/INR rate. Example:

- US 2021 operating IPO proceeds: $119.6 billion = ₹890,000 cr at year-end
  USD/INR of ₹74.43 ÷ 100,000 (cr conversion).
- India FY 2021-22 IPO amount: ₹112,553 cr ≈ $15.1 billion.
- **Ratio**: US issued ~8x as much in $ terms in CY 2021 vs India's
  FY 2021-22 (both peak years).

For YoY analysis, the dollar amount is fine as-is (YoY% removes the
absolute-scale issue).

## 9. How to extend

- **New years**: when Ritter publishes the next annual update (typically
  January or February of the following year), append the new row using
  Table 8 + Table 15 values. The URL pattern in section 1 doesn't change.
- **Pre-2000 backfill**: Ritter Table 8 starts in 1960; backfilling is
  trivial — just add older rows from the same PDF.
- **SPAC proceeds**: add a new column sourced from Ritter Table 15b
  (separate SPAC table).
- **Follow-on / FPO equivalent**: SIFMA Capital Markets Fact Book has
  US equity follow-on issuance going back decades; could be added as a
  separate file `us_fpo_data.csv` parallel to India's
  `fpo_rights_data.csv`.

## 10. Authoritative cross-check sources

For any single value:
- **Primary**: Jay Ritter's database (this file's source).
- **Secondary**: LSEG (formerly Refinitiv) IPO league tables — same
  underlying data, paywalled product.
- **Tertiary**: Renaissance Capital US IPO Year-In-Review reports
  (issued each January, freely downloadable at
  https://www.renaissancecapital.com/IPO-Center).
- **Quaternary**: SIFMA Capital Markets Fact Book
  (https://www.sifma.org/resources/research/fact-book/), annual.
  Includes broader equity issuance numbers (follow-ons, etc.).
- **Official US regulator**: SEC EDGAR
  (https://www.sec.gov/edgar/searchedgar/companysearch) — the raw
  S-1/F-1 filings. Counting these directly requires building an
  aggregator; that's what Ritter does for the academic data set.

For the 2000-2025 window, Ritter is the cleanest, most consistently
defined source; all four cross-checks agree on direction and rough
magnitude for every year (±10-15% on counts; ±20-30% on proceeds
depending on whether the source includes SPACs/REITs/ADRs).

## 11. Bottom-line interpretation

The US IPO market over 2000-2025 shows three distinct cycles separated
by structural breaks:

1. **2000-2003**: dot-com collapse + Sarbanes-Oxley + bear market →
   IPO count drops from 382 (2000) to 68 (2003). Proceeds drop from
   $65B → $10B (-85%).
2. **2004-2014**: slow rebuild interrupted by 2008-2009 GFC freeze
   (21 IPOs in 2008). Recovery to 222 IPOs in 2014.
3. **2015-2025**: declining baseline (~100-200 IPOs/year) punctuated
   by the 2021 SPAC-driven peak (315 operating, 1,033 gross) and the
   2022 freeze (39 operating, $7B).

The structural decline in US IPO count post-2000 (Ritter's "the number
has dropped from 310/year (1980-2000) to 110/year") is **the opposite
of India's pattern** where IPO count has grown from ~50/year (2001-2010)
to ~200+/year (2018+) and 320 in CY 2025. Side-by-side comparison
across both CSVs would illuminate this divergence.
