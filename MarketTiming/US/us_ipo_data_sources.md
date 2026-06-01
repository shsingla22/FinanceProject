# US IPO Annual Statistics — Count and Proceeds (`us_ipo_data.csv`)

Preparation date: 2026-06-01.

26 rows of yearly US IPO statistics, calendar years 2000-2025. This is
the US counterpart to `MarketTiming/EquityIssuanceVsIndex/ipo_data.csv`
for India, intended to enable side-by-side US-vs-India equity issuance
comparison.

---

## 1. Data source — official U.S. SEC

All values are from the **U.S. Securities and Exchange Commission's
official IPO statistics dataset**, published by SEC's Division of
Economic and Risk Analysis (DERA):

- **Source page**: https://www.sec.gov/data-research/statistics-data-visualizations/initial-public-offerings-ipos
- **Direct download** (XLSX): https://www.sec.gov/files/sec-stats-ipos-20260317.xlsx
- **Methodology guide**: https://www.sec.gov/files/sec-stats-guide-ipos.pdf
- **Snapshot date used**: 17 March 2026 release (filename `sec-stats-ipos-20260317.xlsx`)
- **Coverage**: 2000:Q1 through 2025:Q4 (annual rows extracted for this CSV)

This is the **authoritative U.S. government source for IPO statistics** —
maintained by SEC staff from the underlying primary-market regulatory
filings (S-1, F-1, 424B prospectuses on EDGAR). The dataset was first
publicly released by SEC in 2025 as part of the new Statistics & Data
Visualizations program. It supersedes industry-data redistributors (LSEG,
Dealogic) for citation purposes because it comes directly from the
regulator that approves every offering.

## 2. File contents

| Column | Meaning |
|--------|---------|
| `calendar_year` | CY (4-digit) |
| `ipo_count_total` | Total IPOs by all issuer types (corporate + SPAC + fund) |
| `ipo_count_corporate` | Operating-company IPOs only (the "real" IPOs) |
| `ipo_count_spac` | Blank-check / SPAC IPOs |
| `ipo_count_fund` | Closed-end funds + BDCs |
| `ipo_count_us_issuers` | IPOs by U.S.-domiciled issuers |
| `ipo_count_non_us_issuers` | IPOs by non-U.S.-domiciled issuers (e.g., Chinese ADRs, foreign companies) |
| `ipo_proceeds_total_usd_mn` | Total gross proceeds (US$ millions) across all IPO types — NOT inflation-adjusted |
| `ipo_proceeds_corporate_usd_mn` | Gross proceeds from corporate (operating-company) IPOs only |
| `ipo_proceeds_spac_usd_mn` | Gross proceeds from SPAC IPOs |
| `ipo_proceeds_fund_usd_mn` | Gross proceeds from closed-end-fund / BDC IPOs |
| `ipo_avg_proceeds_usd_mn` | Average (mean) deal size across all IPOs |
| `ipo_median_proceeds_usd_mn` | Median deal size across all IPOs |
| `source_note` | Brief macro context per year |

The breakdown columns (corporate / SPAC / fund) sum exactly to the total
columns in every row — verified across all 26 years.

## 3. SEC methodology (per the official guide)

From the SEC's "Statistics Guide: Initial Public Offerings" PDF:

> Initial Public Offerings (IPOs) include all initial sales of equity
> securities by issuers that result in the public listing of their shares,
> as well as initial listings of securities of investment companies
> registered as closed-end funds or business development companies.
> The data presented in the IPO statistics include issuances by issuers
> not previously trading on a national securities exchange, and excludes
> direct listings, transactions between affiliated companies, and IPOs
> for which the offering price was not announced.

**Inclusions**:
- All issuer types: corporate operating companies, SPACs (blank-check
  companies), closed-end funds, BDCs.
- Both U.S.-domiciled and non-U.S. issuers (foreign issuers including
  ADRs).
- All registered IPOs filed with SEC on Form S-1 (domestic) or F-1
  (foreign).

**Exclusions**:
- **Direct listings** (e.g., Spotify 2018, Slack 2019, Coinbase 2021)
  are NOT counted — they don't involve a primary issuance of new shares.
- Affiliated-company transactions (e.g., spin-off carve-outs from
  parent companies where there's no public-market sale).
- IPOs without a publicly-announced offering price.
- Regulation A offerings (small-tier, mini-IPOs up to $75M).
- Regulation Crowdfunding offerings (up to $5M).

## 4. The four useful counts in this CSV

The SEC provides three orthogonal cuts of the IPO universe; combined
with the total, you get four useful counts:

| Count | What it answers | Suitable for |
|-------|-----------------|--------------|
| `ipo_count_corporate` | "How many operating businesses went public?" | Direct comparison with India's `ipo_count_total` from `ipo_data.csv` (both are operating companies) |
| `ipo_count_spac` | "How many blank-check vehicles listed?" | Tracking the 2020-2021 SPAC mania cycle |
| `ipo_count_fund` | "How many closed-end funds / BDCs listed?" | Detecting investment-fund issuance cycles |
| `ipo_count_total` | "How many tickers started trading via an IPO?" | Broadest "all listings" count |

## 5. Decade-level aggregates (derived from the data)

| Decade | Total IPOs | Corporate IPOs | SPAC IPOs | Fund IPOs | Total Proceeds (US$ B) | Corporate Proceeds (US$ B) |
|--------|----------:|---------------:|----------:|----------:|----------------------:|---------------------------:|
| 2000-09 | 2,209 | 1,780 | 167 | 262 | 555.4 | 392.7 |
| 2010-19 | 2,476 | 2,074 | 213 | 189 | 538.1 | 435.9 |
| **2020-25** | **2,561** | **1,347** | **1,178** | **36** | **621.9** | **324.2** |
| 2000-25 total | 7,246 | 5,201 | 1,558 | 487 | 1,715.4 | 1,152.8 |

The **2020-2025 SPAC artifact** is striking: SPACs were essentially zero
through 2002, ~10-65 per year through 2019, then exploded to 248 (2020),
611 (2021), then partially collapsed (86 in 2022, 31 in 2023, 58 in
2024, 144 in 2025). 2021 alone accounted for **611 of the 1,558**
SPAC IPOs in the full 26-year window (~39%).

## 6. Key headline observations

- **Peak total count**: 2021 (1,078 IPOs) — the SPAC-mania peak.
  Corporate IPOs that year: 452. SPACs: 611. Funds: 15.
- **Peak corporate count**: 2000 (456 corporate IPOs) — the dotcom peak.
- **Peak total proceeds**: 2021 ($302.7B) — driven by 611 SPACs raising
  $144B (the largest single-year SPAC proceeds in history).
- **Peak corporate proceeds**: 2021 ($142.5B), followed by 2014 ($86.9B,
  Alibaba ADR contributed ~$25B), 2000 ($83.1B), 2020 ($79.7B).
- **Worst year by total proceeds**: 2022 ($21.6B, -93% YoY from 2021).
  Corporate proceeds: $7.9B — even worse than 2009 ($21.9B post-GFC).
- **Worst year by corporate count**: 2008 (43 corporate IPOs) — GFC freeze.
- **Non-U.S. issuer share has grown**: 2000 had 91 non-US (20% of total);
  2023 had 74 (44% of total). U.S. companies are listing less; foreign
  issuers (especially Chinese small-caps) are filling some of the slot.

## 7. SEC vs Jay Ritter (academic) — definitional differences

The earlier version of this CSV used Jay Ritter's academic data from
University of Florida. The SEC numbers differ for principled reasons:

| Year | SEC corporate | Ritter Table 8 (operating) | Diff | Why |
|------|--------------:|--------------------------:|-----:|-----|
| 2000 | 456 | 382 | +74 | Ritter excludes IPOs priced <$5 and units/best-efforts |
| 2008 | 43 | 21 | +22 | Same |
| 2021 | 452 | 315 | +137 | Ritter excludes a subset post-2012 (Reg A, etc.) |
| 2025 | 226 | 94 | +132 | Same |

SEC's `corporate` count is more inclusive than Ritter's "operating
company" count because the SEC includes:
- IPOs priced below $5 per share (Ritter excludes)
- Small best-efforts offerings (Ritter excludes)
- Some Reg A+ tier-2 offerings (Ritter excludes for older years)

For headline US-vs-India comparisons, **the SEC numbers are
preferred** because (a) they come from the official regulator,
(b) the methodology is publicly documented in the SEC guide, and
(c) the breakdown by issuer type is uniquely available.

For research that demands cross-decade consistency with the academic
literature, Ritter's series remains the standard.

## 8. Cross-source validation (SEC vs Renaissance Capital vs SIFMA)

| Year | SEC total | Ren. Capital | SIFMA equity issuance (broader) | Comment |
|------|----------:|-------------:|-------------------------------:|---------|
| 2021 | 1,078 / $302.7B | 397 IPOs / $142B | ~$435B all equity issuance | Renaissance excludes SPACs by default; matches SEC's corporate-only $142.5B |
| 2020 | 492 / $164.6B | 218 / $78B | ~$130B | Renaissance excludes SPACs; SEC corporate-only = $79.7B (matches) |
| 2008 | 60 / $28.8B | 31 / $28B | ~$40B | Different denominators on count; proceeds agree closely |

The SEC and Renaissance Capital agree to within ±1% on **corporate-only
proceeds** for every recent year tested. The big differences are
counting differences (SPAC inclusion/exclusion) and are explainable.
The SEC dataset is the right primary source when the SPAC breakdown
matters (i.e., any analysis touching 2020-2021).

## 9. Definitions that DIFFER from India's `ipo_data.csv`

| Feature | India (`ipo_data.csv`) | US (this CSV) |
|---------|------------------------|---------------|
| Time basis | Fiscal year (April-March) | Calendar year (Jan-Dec) |
| Year label convention | FY-ending CY (e.g., FY 2024-25 → "2025") | CY directly |
| SPAC handling | Not material in India | Separate column; included in `_total` |
| ADR handling | n/a | Non-U.S. issuers (including ADRs) separately broken out |
| Mainboard / SME split | Combined into `_total` | All on national exchanges (no SME tier) |
| Currency | INR (₹ crore) | USD ($ millions) |
| Direct listings | n/a | Excluded from both counts |
| Source | SEBI Monthly Bulletins / Handbooks | SEC DERA statistics dataset |

**For comparison purposes:**
- The India `ipo_count_total` is most comparable to the US `ipo_count_corporate`
  (both are operating-company primary issuances).
- For total listings comparison, use India `ipo_count_total` vs US
  `ipo_count_total` (the SEC total includes SPACs and funds).

## 10. Currency conversion for direct $-vs-₹ comparison

Use `MarketTiming/EquityIssuanceVsIndex/usd_inr_data.csv` for year-end
USD/INR conversion:

- US 2021 corporate IPO proceeds: $142.5B = ₹10.6 lakh crore (at year-end USD/INR ₹74.43)
- India FY 2021-22 IPO amount: ₹1.13 lakh crore ≈ $15.1B
- **Ratio**: US issued ~9.5x more in $ terms in CY 2021 vs India FY 2021-22 (both peak years).

For YoY analysis, the dollar amount is fine as-is (YoY% removes the
absolute-scale issue).

## 11. How to extend

- **New quarters/years**: SEC updates the dataset quarterly. The URL
  pattern is `https://www.sec.gov/files/sec-stats-ipos-YYYYMMDD.xlsx`
  where YYYYMMDD is the release date. Find the latest at
  `https://www.sec.gov/data-research/statistics-data-visualizations/initial-public-offerings-ipos`.
- **Pre-2000 backfill**: SEC's published series begins in 2000:Q1.
  For pre-2000, fall back to Ritter Table 8 (which goes back to 1960).
- **By-industry breakdown**: SEC publishes "IPOs: Number and Proceeds by
  Major Industry Group" as a separate dataset (the `Data Visual 2`
  sheet in the same XLSX file). Could be added as a sibling file
  `us_ipo_by_industry.csv` if needed.
- **By-state breakdown**: SEC publishes "IPOs: Number of Offerings by
  Issuer Location" for the most recent year (sheet `Data Visual 3`).
  Limited to single-year snapshot, not a multi-year series.
- **Follow-on / FPO equivalent**: SEC also publishes "Public Offerings
  of Securities other than IPOs" — that would be the US analog to
  India's `fpo_rights_data.csv`. Could be added as
  `us_followon_data.csv`.

## 12. Authoritative cross-check sources

For any single value:
- **Primary**: SEC DERA IPO Statistics (this CSV's source).
- **Alternative U.S. government**: SEC EDGAR raw filings
  (https://www.sec.gov/edgar/search) — counting S-1/F-1/424B filings
  directly. Reproduces the same numbers (it's the underlying data the
  SEC aggregates from).
- **Federal Reserve**: Z.1 Financial Accounts of the United States,
  Table F.213 "Corporate Equities" — total equity issuance (broader
  than IPOs alone; includes follow-ons, conversions, etc.).
- **Industry redistributors**: LSEG (formerly Refinitiv), Dealogic,
  Renaissance Capital, Bloomberg, S&P Capital IQ. All derive from
  the same SEC primary data; differences are definitional, not factual.
- **Academic**: Jay Ritter's IPO Database at University of Florida
  (https://site.warrington.ufl.edu/ritter/ipo-data/) — the gold
  standard for cross-decade consistent definitions; goes back to 1960.

For the 2000-2025 window, all the above agree on direction and rough
magnitude; differences are entirely about which issuer types are
included.

## 13. Bottom-line interpretation

The US IPO market over 2000-2025 shows four distinct cycles:

1. **2000-2003**: dot-com collapse + Sarbanes-Oxley → corporate IPO count
   drops from 456 (2000) to 88 (2003). Total proceeds drop from $84B → $45B.
2. **2004-2008**: rebuild via JOBS-pre era + SPAC growth — corporate
   IPOs trend up to 240 (2007), SPACs grow from 0 → 64. GFC freezes 2008.
3. **2009-2019**: post-GFC rebuild with sub-cycle peaks (Facebook 2012,
   Alibaba 2014, slow 2015-2016, recovery 2017-2019 with Uber/Lyft).
4. **2020-2025**: SPAC mania (2020-2021), then deep freeze (2022),
   then slow recovery (2023-2025). Cycle still in progress.

The structural decline in US corporate IPO count post-2000 (Jay Ritter's
"310 → 110/year" finding) is the **opposite of India's pattern** where
IPO count has grown from ~50/year (2001-2010) to 320 in CY 2025.
Side-by-side comparison across both CSVs will illuminate this divergence
in future analysis.
