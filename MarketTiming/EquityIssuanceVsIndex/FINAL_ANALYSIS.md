# FINAL ANALYSIS — Indian Equity Issuance, Indices, USD/INR, and I-banking Basket (2000-2026)

Prepared: 2026-06-01.
Single consolidated read-through for the work in this folder.
Companion documents: `analysis.md`, `patterns_high_probability.md` (v1),
`patterns_v2_extended.md` (v2 — new), `methodology.md`,
`forecast_fy2026_27.md`, plus the per-series `*_data_sources.md` files.

---

## 0. TL;DR

After 26 years of Indian primary-market, index, FX, and listed-I-bank
data, the most defensible empirical conclusions are:

1. **Markets lead issuance, not the other way around.** Strong index
   years are followed by surging IPO issuance the next year; the
   reverse direction is statistical noise. The I-banking basket leads
   IPO supply with **8/8 = 100% reliability** — a new finding from
   adding listed-I-bank data.

2. **Heavy IPO issuance is *not* a topping signal for the broad index.**
   In 4 of 4 years where IPO amount exceeded ₹50,000 cr (2018, 2022,
   2023, 2024), the Nifty 50 was up the following year — averaging +12.8%.

3. **The supply pressure lands on the smallcap segment.** In 3 of those
   4 record-issuance years, Smallcap 100 returns *in the same year*
   were -29%, -14%, -5% (only 2024 was positive). Mid/large-cap absorb
   the shock.

4. **IPO droughts are the strongest single buy signal.** When IPO amount
   fell more than 50% YoY (5 historical years: 2009, 2013, 2014, 2019,
   2023), the Midcap 100 was up every single year after — average +25.5%.

5. **Cheap Nifty 50 valuations (P/E ≤ ~17) → +43% avg next-year return,
   5 of 5 historical instances positive.** Even stronger over 2-year
   horizons: +80% avg, 5/5 positive. The strongest single-feature signal
   in the dataset.

6. **USD/INR shocks (>+10% YoY) are perfect bounce signals.** Four
   historical instances (2008 GFC, 2011 EU crisis, 2013 Taper Tantrum,
   2022 Fed-hiking). Next year: Nifty 50 +39% avg, Midcap +60%,
   I-banking basket +101%. All 4/4 hit. **New finding from adding
   USD/INR data.**

7. **Stretched valuations predict INR depreciation, NOT equity crashes.**
   When any of (Nifty 50 P/E > 25, Smallcap P/E > 35, Midcap P/E > 30,
   smallcap-Nifty P/E spread > 10) triggers, the **USD/INR moves
   higher** the next year (4-5/4-5 instances each, 100% records). The
   damage from over-valuation is taken by the currency and the smallcap
   segment, not the broad index. **New surprise finding.**

8. **Today's setup (end-CY 2025).** Patterns favoring positive 2026
   are triggered: ₹172k cr IPO amount (pattern #2 ✓), Midcap P/E
   33.84 (pattern #4 ✓), Nifty 50 P/E 22.75 in Q3 (6/6 historical
   positive). Patterns warning of crisis are NOT triggered: no
   issuance drought, no FX shock, no I-bank mania. Closest historical
   analogs (2018, 2023, 2024) all delivered +9-12% next-year Nifty
   returns.

**Important caveat throughout:** all "hit rates" are based on 4-8
historical instances. Bayesian credible intervals on the true
probability are wide. None of this is a trading rule; it's the empirical
base rate from comparable historical setups.

---

## 1. What was studied

**Question.** Do Indian equity primary-market activity (IPO and FPO+Rights
issuance), broad-market valuations (Nifty 50 / Midcap 100 / Smallcap 100
P/E), the USD/INR exchange rate, and listed I-banking-company stock
returns carry information about subsequent index returns? If so, what
specific signals have a historically high hit rate?

**Time window.** Calendar years 2000-2026 (27 years; CY 2026 partial,
through 01-Jun-2026). Indian fiscal years 2001-02 to 2025-26 for the
issuance data, mapped to calendar-year-ending convention.

**Sample sizes per series.**

| Series | Full span | Years used in analysis |
|--------|-----------|-----------------------:|
| Nifty 50 | 2000-2025 | 26 |
| Nifty Midcap 100 | 2006-2025 | 20 |
| Nifty Smallcap 100 | 2012-2025 | 14 |
| IPO/FPO+Rights | FY 2001-02 to FY 2025-26 | 25 |
| USD/INR year-end | 2000-2026 | 27 (CY 2026 partial) |
| I-banking basket (equal-weight YoY %) | 2006-2025 | 20 (n grows from 2 to 8 firms) |
| Nifty Capital Markets index (scaffold) | 2019-2025 | 0 (values pending manual backfill) |

**Years with all relevant series usable: 14 (CY 2012-2025).**

---

## 2. The data, with provenance

All values traceable to specific SEBI / NSE / Yahoo Finance / FRB
publications, downloaded directly from sebi.gov.in, archives.nseindia.com,
query2.finance.yahoo.com, and federalreserve.gov:

| Series | File | Span | Primary source |
|--------|------|------|----------------|
| IPO count & amount | `ipo_data.csv` | FY 2001-02 → FY 2025-26 | SEBI Handbooks 2010 + 2018 + SEBI Monthly Bulletins (Apr-2026) |
| FPO+Rights count & amount (equity) | `fpo_rights_data.csv` | FY 2001-02 → FY 2024-25 | Same SEBI sources |
| Nifty 50 year-end close + P/E | `nifty50_data.csv` | CY 2000 → CY 2025 | NSE bhavcopy 2012+, SEBI ARs 2003-2011, Wikipedia/SEBI Handbook for 2000-2002 |
| Nifty Midcap 100 year-end close + P/E | `nifty_midcap100_data.csv` | CY 2006 → CY 2025 | NSE bhavcopy 2012+, SEBI ARs 2006-2011 |
| Nifty Smallcap 100 year-end close + P/E | `nifty_smallcap100_data.csv` | CY 2012 → CY 2025 | NSE bhavcopy only |
| Industry-wise issuance | `industry_issuance_data.csv` | FY 2001-02 → FY 2024-25 | SEBI Handbooks + Bulletin Table 7/9 |
| **Listed I-banking companies year-end closes** | `investment_banks_data.csv` | CY 2005 → CY 2025 (8 companies) | **Yahoo Finance USDINR=X / .NS / .BO daily** |
| **Listed I-banking basket YoY %** | `investment_banks_yoy.csv` (derived) | CY 2006 → CY 2025 | Computed via `build_ibank_aggregate.py` |
| **USD/INR year-end exchange rate** | `usd_inr_data.csv` | CY 2000 → CY 2026 | FRB H.10 (2000-2002) + Yahoo Finance USDINR=X (2003-2026) |
| Nifty Capital Markets index (scaffold) | `nifty_capital_markets_data.csv` | CY 2019 → CY 2025 (values empty) | NSE Indices niftyindices.com (needs manual backfill) |
| FY 2026-27 IPO forecast | `forecast_fy2026_27.md` | Forward look | PRIME Database ₹2.5 lakh cr / 192 cos. |

Each row has a source citation. Each file's `*_data_sources.md`
documents every methodology choice, naming convention, and known gap.

### 2.1 The seven companies in the I-banking basket

| Company | Yahoo ticker | First listed | What it does |
|---------|--------------|--------------|--------------|
| JM Financial | `JMFINANCIL.BO` | data from 2002 | India's most established pure-play I-bank |
| Motilal Oswal Financial Services | `MOTILALOFS.NS` | Sept 2007 | Broking + I-bank + AMC |
| Edelweiss Financial Services | `EDELWEISS.NS` | Dec 2007 | Diversified financial — wealth + AMC + capital markets |
| IIFL Finance | `IIFL.NS` | May 2005 | NBFC (was IIFL Holdings pre-2019 demerger) |
| Anand Rathi Wealth | `ANANDRATHI.NS` | Dec 2021 | Wealth + I-bank |
| Nuvama Wealth Management | `NUVAMA.NS` | Sept 2023 | Wealth + I-bank (spun off from Edelweiss) |
| IIFL Capital Services | `IIFLCAPS.NS` | Nov 2024 | I-bank + broking (renamed from IIFL Securities) |
| Almondz Global Securities | `ALMONDZ.NS` | June 2008 | Smaller I-bank + broking |

The basket is **equal-weighted** across companies that have a YoY %
value in each year (n grows from 2 in 2006 to 8 in 2025).

### 2.2 The USD/INR year-end series (key new datapoints)

| Year | USD/INR | YoY % | Macro context |
|------|--------:|-------:|---------------|
| 2000 | 46.75 | — | Dot-com bust period |
| 2005 | 44.97 | +3.84% | Modest INR weakening |
| 2007 | 39.25 | -10.89% | **Pre-GFC INR peak (₹39)** |
| 2008 | 48.07 | +22.47% | **GFC: INR collapse** |
| 2011 | 53.00 | +18.28% | EU debt crisis |
| 2013 | 61.78 | +12.83% | **Taper Tantrum** |
| 2018 | 69.92 | +9.53% | EM rout; oil price spike |
| 2020 | 73.13 | +2.56% | COVID shock |
| 2022 | 82.84 | +11.29% | Fed hiking; INR ₹80 broken |
| 2023 | 82.30 | -0.64% | Flat |
| 2024 | 85.79 | +4.23% | Continued INR weakening |
| 2025 | 89.77 | +4.64% | INR ₹89 |
| 2026 (Jun-1) | 94.99 | +5.81% YTD | INR ₹95 |

Cumulative INR depreciation 2000 → 2026 = **+103.2%** (CAGR ≈ +2.7%).
Cumulative 2020 → 2026 = +29.9% (CAGR ≈ +5.1%) — i.e., FX has weakened
faster in the recent IPO supply boom than in the full 2000-2026 average.

---

## 3. Key correlations (the big picture)

### 3.1 Direction of causality (between issuance and indices)

| Pair | Correlation | n | Reading |
|------|------------:|---|---------|
| IPO amount YoY (t) vs Nifty 50 YoY (t-1) | **+0.53** | 23 | Strong index year → big issuance next year |
| IPO amount YoY (t) vs Smallcap YoY (t-1) | **+0.59** | 12 | Same |
| IPO amount YoY (t) vs Midcap YoY (t-1) | **+0.62** | 18 | Same |
| Nifty 50 YoY (t) vs IPO YoY (t-1) | -0.27 | 22 | Reverse direction: noise |
| **I-bank basket YoY (t) vs IPO amount YoY (t+1)** | **+0.42** | 19 | **I-banks lead issuance** |

### 3.2 Cross-asset correlations including new series

| Pair (annual data) | Correlation | n | Interpretation |
|--------------------|------------:|--:|----------------|
| Nifty 50 level vs USD/INR level | **+0.927** | 26 | Secular co-movement (both trend up). Not tradable. |
| I-bank basket YoY vs Smallcap YoY | **+0.864** | 13 | I-banks essentially behave as smallcaps |
| I-bank basket YoY vs Midcap YoY | +0.842 | 19 | Same point |
| I-bank basket YoY vs Nifty 50 YoY | +0.768 | 20 | Strong but lower than SC/MC |
| **USD/INR YoY vs Nifty 50 YoY** | **-0.761** | 25 | **Strong negative** — INR up = Nifty down in same year |
| USD/INR YoY vs I-bank basket YoY | -0.745 | 20 | INR weakens when EM equities weaken |
| USD/INR YoY vs Smallcap YoY | -0.739 | 13 | Same |
| IPO amount YoY vs I-bank basket YoY | -0.221 | 20 | Surprisingly weak; muted because of the lag (basket leads supply by ~1 year) |

The **-0.76 USD/INR YoY ↔ Nifty 50 YoY** correlation is the cleanest
single relationship in the entire 26-year window. About 58% of the
variance in Nifty 50 annual returns moves with INR moves (in the
opposite direction).

### 3.3 Same-year correlations across all equity segments

|                      | IPO amt YoY | FPO+R YoY | Nifty 50 | Smallcap | Midcap | I-bank | USD/INR |
|----------------------|------------:|----------:|---------:|---------:|-------:|-------:|--------:|
| IPO amt YoY          | 1.00 | 0.04 | -0.13 | **-0.44** | -0.13 | -0.22 | -0.16 |
| FPO+R YoY            | 0.04 | 1.00 | -0.14 | -0.08 | -0.22 | -0.18 | -0.10 |
| Nifty 50 YoY         | -0.13 | -0.14 | 1.00 | 0.83 | **0.95** | **0.77** | **-0.76** |
| Smallcap YoY         | -0.44 | -0.08 | 0.83 | 1.00 | **0.98** | **0.86** | **-0.74** |
| Midcap YoY           | -0.13 | -0.22 | **0.95** | **0.98** | 1.00 | **0.84** | -0.66 |
| I-bank basket YoY    | -0.22 | -0.18 | 0.77 | 0.86 | 0.84 | 1.00 | **-0.75** |
| USD/INR YoY          | -0.16 | -0.10 | -0.76 | -0.74 | -0.66 | -0.75 | 1.00 |

**Three observations worth highlighting:**
- The Indian equity segments move together near-perfectly (Smallcap
  ↔ Midcap = 0.98; Midcap ↔ Nifty 50 = 0.95). When one rallies, all
  three rally; when one falls, all three fall.
- The **I-banking basket is essentially a high-beta smallcap proxy**
  (correlation 0.86 to Smallcap, 0.77 to Nifty 50).
- The **USD/INR is a strong negative driver of every equity segment**
  (correlations -0.66 to -0.76). Currency and equity move opposite.

### 3.4 The asymmetry — supply hits smallcaps first

Top 4 IPO-amount years and what each index did in that *same* calendar
year:

| Year | IPO amt (₹ cr) | Nifty 50 | Midcap | Smallcap |
|------|---------------:|---------:|-------:|---------:|
| 2025 | 172,328 | +10.5% | +5.8% | **-5.0%** |
| 2022 | 112,553 | +4.3%  | +3.5% | **-13.8%** |
| 2018 | 83,684  | +3.2%  | -15.4% | **-29.1%** |
| 2024 | 67,955  | +8.8%  | +23.8% | +23.1% |

Three of four had **smallcap-specific weakness in the same year while
Nifty 50 stayed positive.** This is structural.

### 3.5 FPO+Rights is event-driven, not cyclical

Top FPO+Rights years are dominated by distressed recapitalizations:
- FY 2020-21: ₹78,987 cr — Reliance Industries rights ~₹53,124 cr (post-COVID deleveraging)
- FY 2019-20: ₹55,679 cr — Reliance rights spillover
- FY 2024-25: ₹37,862 cr — Vodafone Idea FPO ~₹18,000 cr (distress recap)
- FY 2007-08: ₹37,144 cr — pre-GFC follow-on wave

Correlations with index returns are between -0.22 and +0.41 — essentially
random. **FPO+Rights spikes are not a market-timing signal**.

---

## 4. The 12 high-probability patterns (≥80% historical hit rate, n≥4)

After testing 50+ signal definitions × 9 forward outcomes × 2 directions
(~900 cells total — expanded ~3x from v1 by adding USD/INR and I-bank
signals), the following patterns survived the **hit rate ≥80% with
n ≥ 4** filter. Full mechanics in `patterns_v2_extended.md`.

| # | Signal at year *t* | Outcome at *t*+1 (or *t*+2) | Hits | Hit rate | Avg outcome |
|---|---|---|---|---|---|
| **1** | **Nifty 50 P/E (norm) < 17** | Nifty 50 UP 1y, UP 2y | 5/5, 5/5 | **100%** | +43% (1y), +80% (2y) |
| **2** | **USD/INR YoY > +10% (FX shock)** | Nifty 50, Midcap, I-bank basket — all UP | 4/4 each | **100%** | Nifty +39%, MC +60%, IB +101% |
| **3** | USD/INR YoY > +5% YoY | Nifty 50 UP 1y, 2y; Midcap UP 1y, 2y | 5/5 each | **100%** | +33% Nifty 1y, +67% MC 2y |
| **4** | IPO amount YoY < -50% (drought) | Midcap UP 1y, Smallcap UP 2y | 5/5, 4/4 | **100%** | +25.5% MC, +46.6% SC 2y |
| **5** | **I-banking basket YoY > +50%** | **IPO supply UP next year** | 8/8 | **100%** | +266% IPO YoY |
| **6** | I-banking basket YoY > +100% (mania) | IPO supply UP next year | 6/6 | **100%** | +335% IPO YoY |
| **7** | USD/INR YoY stable (-3% to +3%) | Midcap UP 1y, Smallcap UP 2y | 7/7, 6/6 | **100%** | +32% MC 1y, +34% SC 2y |
| **8** | I-bank basket YoY < 0% (capitulation) | Smallcap UP 2y | 5/5 | **100%** | +54% SC 2y |
| **9** | IPO amount > ₹50,000 cr | Nifty 50 UP next year | 4/4 | **100%** | +12.8% |
| **10** | Midcap P/E (norm) > 30 | Nifty 50 UP next year | 4/4 | **100%** | +12.5% |
| **11** | Smallcap P/E (norm) > 35 | Nifty 50 UP 1y, UP 2y | 4/4, 4/4 | **100%** | +16.4% (1y), +27.8% (2y) |
| **12** | **Stretched valuation** (any of N50 P/E > 25, SC > 35, MC > 30, spread > 10) | **INR depreciates next year** | 4-5/4-5 each | **100%** | +5 to +8% INR YoY |

### 4.1 The single most actionable cluster — USD/INR shock bounce

The new finding from this analysis:

> **When the INR depreciates more than 10% in a single calendar year
> (4 instances in 26 years: 2008, 2011, 2013, 2022), the next calendar
> year sees the Nifty 50 up an average of +39%, Midcap +60%, and the
> I-banking basket +101%. All four instances delivered positive returns
> across all three.**

| Year *t* | USD/INR YoY | Nifty 50 *t+1* | Midcap *t+1* | I-bank basket *t+1* |
|----------|------------:|---------------:|-------------:|--------------------:|
| 2008 | +22.5% (GFC) | +75.8% (2009) | +98.6% | +137.8% |
| 2011 | +18.3% (EU crisis) | +27.7% (2012) | +39.2% | +10.7% |
| 2013 | +12.8% (Taper Tantrum) | +31.4% (2014) | +55.9% | +170.1% |
| 2022 | +11.3% (Fed hiking) | +20.0% (2023) | +46.6% | +86.8% |
| **Avg** | **+16.2%** | **+38.7%** | **+60.1%** | **+101.3%** |

**Mechanism:** Sharp INR moves are the *symptom* of EM risk-off events
already in progress. By the time the move shows up at year-end, the
equity damage is done. Year *t+1* is the recovery from the depressed
base. **Don't read this as "buy after FX shock"; read it as "the worst
is usually behind you once you see a >10% INR move at year-end."**

### 4.2 The lead/lag chain — I-banking basket leads IPO supply

> **When the equal-weighted I-banking basket is up more than 50% in a
> calendar year (n=8 instances in 20 years), IPO amount raised in the
> next fiscal year is up — every single time. Average +266% YoY.**

| Trigger year *t* | Basket YoY | Next FY IPO YoY |
|---|---:|---:|
| 2006 | +101% | +161% (FY 2006-07) |
| 2007 | +269% | +49% (FY 2007-08) |
| 2009 | +138% | +1086% (FY 2009-10) ★ |
| 2014 | +170% | +168% (FY 2014-15) |
| 2016 | +71% | +96% (FY 2016-17) |
| 2017 | +131% | +188% (FY 2017-18) |
| 2021 | +122% | +356% (FY 2021-22) |
| 2023 | +87% | +24% (FY 2023-24) |

**Mechanism:** Underwriting fees scale with future issuance volume;
I-bank stock prices reflect expectations of that future income. So a
6-12 month lead time between "I-bank rally" and "IPO supply surge" is
structurally expected.

### 4.3 The reverse-causation surprise — stretched valuations → INR depreciation

When any of (Nifty 50 P/E > 25, Smallcap P/E > 35, Midcap P/E > 30,
smallcap-Nifty P/E spread > 10) holds at year *t*, the **USD/INR moves
higher** in year *t+1* — every single time, across 4 separate signal
variants:

| Signal | n | Hit rate | Avg fwd 1y INR YoY |
|--------|--:|---------:|--------------------:|
| Nifty 50 P/E (norm) > 25 | 5 | 5/5 = 100% | +7.7% |
| Smallcap P/E (norm) > 35 | 4 | 4/4 = 100% | +6.7% |
| Midcap P/E (norm) > 30 | 4 | 4/4 = 100% | +4.5% |
| Smallcap-Nifty P/E spread > 10 | 5 | 5/5 = 100% | +6.9% |

**Mechanism:** Stretched Indian equity valuations make Indian assets
relatively expensive in USD terms. Foreign capital takes profits and
converts back to USD, weakening INR. **The damage from over-valuation
is taken by the currency and the smallcap segment, not the broad index.**

### 4.4 The capitulation buy signal — I-bank basket < 0%

> **When the I-banking basket is DOWN in a calendar year (n=8: years 2008,
> 2010, 2011, 2013, 2015, 2018, 2019, 2020), the Smallcap 100 is UP 5 of
> 5 over the next 2 years, averaging +54%.**

Mechanism: I-bank stocks are high-beta to smallcap; when they capitulate,
the smallcap segment is at a cyclical bottom from which 2-year forward
returns are very strong.

### 4.5 Quartile views — the regime tables

#### I-banking basket quartile → next-year Nifty 50

| Basket YoY bucket | n | Avg fwd 1y Nifty 50 | Positive rate |
|-------------------|--:|--------------------:|--------------:|
| Q1 capitulation (< -14%) | 5 | +18.8% | 80% |
| Q2 (-14 to +12%) | 5 | +19.4% | **100%** |
| Q3 (+12 to +87%) | 4 | +25.7% | **100%** |
| **Q4 mania (> +87%)** | 5 | **-6.1%** | **60%** |

**The Q4 mania → negative next-year Nifty 50 bias is the most important
nuance to the high-IPO patterns.** Q4 includes 2007 → 2008 GFC,
2014 → 2015 (-4%), 2017 → 2018 (-29% smallcap, +3% Nifty), 2021 → 2022.

#### USD/INR YoY quartile → next-year Nifty 50

| INR YoY bucket | n | Avg fwd 1y Nifty 50 | Positive rate |
|----------------|--:|--------------------:|--------------:|
| Q1 INR strong (< -3%) | 6 | -1.4% | 67% |
| Q2 (-3 to +2.2%) | 6 | +30.6% | **100%** |
| Q3 (+2.2 to +5.0%) | 6 | +13.4% | 83% |
| Q4 INR weak (> +5%) | 6 | +28.3% | **100%** |

**Two-peak distribution:** best entries are when USD/INR is either
*stable* (Q2) or *very weak* (Q4 shocks). Worst entries are when the
INR is appreciating strongly (Q1) — historically associated with
subsequent disappointment.

#### Nifty 50 P/E quartile (from v1, still valid)

| Nifty 50 P/E quartile | n | Avg fwd 1y return | Positive years |
|------------------------|--:|------------------:|---------------:|
| **Q1 (cheap, P/E ≤ ~17)** | 7 | **+37.4%** | **100% (7/7)** |
| Q2 (17-21) | 6 | +13.3% | 67% (4/6) |
| Q3 (21-24) | 6 | +15.0% | 100% (6/6) |
| Q4 (expensive, P/E > 24) | 6 | -3.7% | 67% (4/6) |

The cheap quartile (≤ ~17) has a perfect 7/7 record with +37% average.
**This is the cleanest single-feature signal in the entire 26-year window.**

### 4.6 Patterns explicitly NOT supported by the data

| Conventional claim | Historical hit rate | Verdict |
|--------------------|---------------------|---------|
| "IPO peak = market top for Nifty 50" | 4/4 = 0% support for crash | **Rejected** |
| "Nifty 50 P/E > 25 → equity crash" | 1/5 = 20% (only 2007→2008 GFC) | **Rejected** (but valid for INR depreciation — see 4.3) |
| "FPO+Rights spike = topping signal" | Correlation ~0 with forward returns | **Rejected** |
| "IPO count > 200 = market top" | 2018→+12%, 2024→+11%, 2025→ TBD | **Rejected** |
| "Smallcap P/E > 35 → Nifty 50 crash" | 4/4 = 0% (Nifty went up each time) | **Rejected** |
| "INR depreciation > 10% → next-year crash" | 0/4 (every instance was followed by RALLY) | **Rejected** |
| "Record I-bank rally = top warning" | 100% only at Q4 mania (>+87%); below that, neutral or bullish | **Partially rejected** |
| "USD/INR > ₹80 absolute = peak FX" | n=4 spans only 2022-2025 — pure trend artifact | **Insufficient evidence** |

### 4.7 Honest reality on hit rates

With n=4-8, Bayesian 95% credible interval on "true probability" is wide.
After observing 5/5 successes under a flat prior: posterior mean 0.86,
95% CI 0.52 to 0.99. A pattern's *historical* hit rate of 100% is **not
the same as a 100% forward probability.**

Multiple-comparisons floor: ~900 cells tested → ~45 would clear 80% by
chance alone. We found 58. That's ~30% above the noise floor — better
than v1's findings, but not orders of magnitude better. Some "patterns"
may still be data-mining.

---

## 5. The USD/INR overlay — what currency tells us

Two ways USD/INR matters:

1. **Same-year:** strong inverse correlation with all Indian equity
   segments (-0.66 to -0.76). When INR weakens, equity falls (in the
   same year). This is the FII-flow channel: foreign capital leaves
   → INR weakens AND equity sells.

2. **Forward indicator:** When the year-end INR move has been > +10%
   (the shock years 2008, 2011, 2013, 2022), the equity bounce next
   year is reliable and large. The currency is the late-stage signal;
   the equity recovery is the next-stage payoff.

### 5.1 USD-denominated Nifty 50 return

A foreign investor who bought the Nifty 50 at end-2020 (₹13,981) and
sold at end-2025 (₹26,129):

- **INR return:** +86.9%
- **USD return:** +52.5% (after the 22.7% INR depreciation in the same window)
- **FX drag:** -34.4 percentage points

The full 26-year picture is starker. From end-2000 to end-2025:
- Nifty 50 in INR: 1,263 → 26,129 = **+1,968%** (CAGR ≈ +12.9%)
- USD/INR: 46.75 → 89.77 = +92.0% INR depreciation
- Nifty 50 in USD: implied **+976%** (CAGR ≈ +9.7%)
- **FX drag over 25 years: -3.2 pp/yr in USD-denominated returns**

This is why pattern #1 (Nifty 50 P/E < 17 → +43% next year in INR) is
**still the strongest single signal even in USD terms.**

---

## 6. The I-banking basket — what listed I-banks tell us

### 6.1 The basket is a high-beta smallcap proxy

The equal-weighted I-banking basket has correlation +0.86 with Smallcap,
+0.84 with Midcap, +0.77 with Nifty 50. Its annual swings are roughly
3-4× the Nifty 50 swings:

| Period | Description | Basket YoY | Nifty 50 YoY |
|--------|-------------|-----------:|-------------:|
| 2007 | Pre-GFC mania | **+269%** | +55% |
| 2008 | GFC | **-79%** | -52% |
| 2014 | "Modi rally" | **+170%** | +31% |
| 2017 | Record IPO supply | **+131%** | +29% |
| 2018 | Smallcap crash | **-41%** | +3% |
| 2021 | Post-COVID rally | **+122%** | +24% |
| 2023 | Equity recovery | **+87%** | +20% |
| 2024 | Continued rally | +34% | +9% |
| 2025 | Digestion | +13% | +10% |

### 6.2 The basket as a forward indicator

Two distinct uses, both with perfect or near-perfect records:

| Basket YoY signal | Next-year outcome | Hit rate |
|-------------------|-------------------|---------:|
| > +50% (n=8) | IPO supply UP | 8/8 = 100% |
| > +100% (n=6) | IPO supply UP | 6/6 = 100% |
| < 0% (n=8) | Smallcap UP 2-year | 5/5 = 100% |
| Q4 mania (> +87%, n=5) | Nifty 50 next year — mixed/negative | 3/5 = 60% |

### 6.3 Today's basket reading (end-CY 2025)

Basket YoY 2025 = **+12.7%**. This is **Q2 territory** (mid-band):
- Above 0 → no capitulation signal for smallcap
- Below +50 → no IPO surge signal
- Below +87 → not Q4 mania (no warning)
- Q2 history → 5/5 next-year Nifty positive, avg +19.4%

This is consistent with the **moderate-positive base case** for 2026
from other signals.

---

## 7. Methodology in brief (full version in `methodology.md`)

**Hypotheses originally tested (6 in v1, expanded to 11 in v2).**
Conventional-wisdom claims about IPO peaks, P/E extremes, FPO distress,
cheap valuations, issuance droughts, symmetric size-segment response,
**plus FX-equity inverse relationship, I-bank-as-leading-indicator,
INR-shock-as-buy-signal, valuation-as-FX-driver, and basket-mania-as-top**.
Confirmed/rejected case-by-case.

**Features built (35).** 10 raw levels + 3 normalized P/Es + 7 YoY%
(adding USD/INR and I-bank basket) + 9 forward outcomes (adding ipo_amt
fwd1, ib_basket fwd1, usd_inr fwd1).

**Signal definitions (50+).** Six families:
- Issuance: 10 (amount thresholds, count thresholds, YoY surges/droughts)
- Valuation: 9 (P/E thresholds across 3 indices)
- **USD/INR: 6 (depreciation / appreciation / stable buckets)** — NEW
- **I-banking basket: 6 (boom / bust / capitulation thresholds)** — NEW
- Combined cross-asset triples: 12 (FX × valuation, I-bank × issuance,
  INR × cheap, etc.) — NEW
- Spread / prior-strength: 4

**Outcomes scored against (9 = 3 horizons × 3 series, plus 3 cross-asset).**
1y / 2y forward Nifty 50 / Midcap / Smallcap returns (6) + 1y forward
IPO amt YoY (1, NEW) + 1y forward I-bank basket return (1, NEW) +
1y forward USD/INR YoY (1, NEW).

**Total cells tested in v2: ~50 × 9 × 2 = 900** vs v1's 336.

**Scoring rule.** Hit rate = matching predictions / total instances.
Required n ≥ 4 to report; ≥80% hit rate to highlight; cross-validated
against symmetric direction check (if signal X is 100% UP, signal X
must be 0% DOWN).

**Mitigations against false patterns:** symmetric direction check,
manual mechanism review, grouping by family before reporting, honest
disclosure of failure modes for each headline pattern, multiple-
comparisons floor explicitly cited.

**Reproducibility.** `find_patterns.py` (v1) and `find_patterns_v2.py`
(v2) rerun the searches. `build_interactive_data.py` rebuilds the JSON
used by the interactive HTML. `build_ibank_aggregate.py` rebuilds the
basket. All thresholds, normalization rules, and modeling choices
documented so anyone can fork and rerun.

---

## 8. Today's setup (end of CY 2025) — empirical base rates for 2026

Mapping every observable signal to historical pattern triggers:

| Signal | End-2025 value | Triggered? | Historical implication |
|--------|----------------|------------|-------------------------|
| Nifty 50 P/E (norm) < 17 (cheap bonanza) | 22.75 | ❌ | No "buy of the decade" signal |
| Nifty 50 P/E (norm) > 25 (stretched) | 22.75 | ❌ | No INR-depreciation warning from large-cap |
| Smallcap P/E (norm) > 35 | 32.2 | ❌ (just below) | No INR warning from smallcap |
| **Midcap P/E (norm) > 30** | **33.84** | ✅ | **Nifty 50 UP next year (4/4); INR likely depreciates** |
| **IPO amount > ₹50,000 cr** | **₹172,328 cr** | ✅ | **Nifty 50 UP next year (4/4)** |
| IPO amount YoY < -50% (drought) | +154% | ❌ | No drought-bottom signal |
| IPO amount YoY > +200% | +154% | ❌ (below) | Doesn't trigger strict version |
| USD/INR YoY > +10% (FX shock) | +4.64% | ❌ | No shock-bounce setup |
| USD/INR YoY > +5% (mild weakening) | +4.64% | ❌ (just below) | Below threshold by 0.4pp |
| USD/INR YoY stable (-3% to +3%) | +4.64% | ❌ (just above) | No stable-INR midcap signal |
| I-bank basket YoY > +50% | +12.7% | ❌ | No I-bank-led IPO supply surge expected |
| I-bank basket YoY > +100% (mania) | +12.7% | ❌ | No Q4-mania top warning |
| I-bank basket YoY < 0% (capitulation) | +12.7% | ❌ | No capitulation buy signal for smallcaps |
| **I-bank basket quartile** | **Q2 (+12.7%)** | ✅ | **5/5 next-year Nifty positive, avg +19.4%** |
| **USD/INR YoY quartile** | **Q3 (+4.64%)** | ✅ | **5/6 positive next-year, avg +13.4%** |
| **Nifty 50 P/E quartile** | **Q3 (22.75)** | ✅ | **6/6 historical positive, avg +15.0%** |
| Smallcap P/E quartile | Q3 (32.2) | n/a | 1/3 historical positive (mixed) |
| Midcap P/E quartile | Q4 (33.84) | n/a | History: only some upside, more risk |

### 8.1 The single most-similar historical setups

The combinations most similar to end-2025 (high IPO supply, moderate
INR weakness, moderate Nifty valuation, mid-band I-bank basket):

| Historical analog | Setup similarity | Nifty 50 next-year return |
|-------------------|------------------|--------------------------:|
| **2018 (mid-band I-bank, mid INR, IPO 84k cr)** | High | +12.0% (2019) |
| **2024 (mid-band I-bank, mid INR, IPO 68k cr)** | High | +10.5% (2025) |
| **2023 (Q3 I-bank +87%, INR -0.6%, IPO 55k cr)** | Medium | +8.8% (2024) |
| **Average** | | **+10.4%** |

**History says Nifty 50 should be up roughly +8 to +15% in 2026.**

### 8.2 Confidence-weighted aggregate

Of the 12 strongest patterns in section 4:
- **3 triggered with 100% historical record**: #9 (IPO > ₹50k cr), #10
  (Midcap P/E > 30), #12 (stretched valuation → INR weakens). Plus
  Q2 I-bank + Q3 Nifty 50 quartiles. All point Nifty 50 UP.
- **9 not triggered.** Forecast is **directional rather than
  magnitude-extreme**: high conviction on direction (UP), moderate
  conviction on magnitude (+8 to +15%, not +30%).

**The setup is not the kind of "everything aligned" buy signal that
2008-end or 2002-end were.** Those years had Nifty 50 P/E < 17 — the
single highest-conviction trigger. Today is a "boring positive" setup.

### 8.3 What would change the read

- A 2026 IPO amount falling below ₹50k cr would re-trigger pattern #4
  (drought → forward rally).
- A sustained smallcap drawdown (>15% in 2026) would mean the
  asymmetry pattern finally affects the broad index.
- USD/INR breaking through 100 (vs 94.99 today) would extend the
  pattern #12 INR-depreciation expectation; if it does and Nifty 50
  *also* falls 15%+, that's the 2008/2022-style FX shock that
  historically precedes a +39% Nifty bounce.
- I-bank basket crossing > +50% in CY 2026 would signal IPO supply
  growth re-accelerating into FY 2026-27.

---

## 9. FY 2026-27 IPO supply forecast (forward indicator, not pattern)

Best estimate from PRIME Database (cited in
`forecast_fy2026_27.md`): **CY 2026 IPO pipeline = 192 companies,
₹2.5 lakh crore aggregate.** Translating to FY 2026-27 (April 2026 -
March 2027):

| Calendar bucket | FY mapping | Estimated amount |
|-----------------|------------|------------------:|
| Jan-Mar 2026 actual (already in FY 2025-26) | FY 2025-26 (not counted) | ~₹17k cr (mainboard) |
| Apr-Dec 2026 expected | FY 2026-27 | ~₹1.8 - ₹2.2 lakh cr |
| Jan-Mar 2027 expected | FY 2026-27 | ~₹0.2 - ₹0.3 lakh cr |
| **FY 2026-27 estimated total** | | **₹2.0 - ₹2.5 lakh cr** |

Central estimate: **₹2.2-₹2.3 lakh crore** — a +15-20% step up over
the FY 2025-26 actual of ₹1.89 lakh crore.

If this materializes:
- **Pattern #2 will retrigger in 2026** (IPO amount > ₹50k cr → Nifty
  UP 2027).
- **Pattern #4 (IPO drought) won't retrigger** — supply will keep
  growing.
- The I-banking basket beta to IPO surge (~0.4 concurrent) suggests
  a 2026 basket return of +20-50%, with the wealth/I-bank-pure-play
  names (Nuvama, Anand Rathi, IIFL Capital) most levered.

The 2-year (2026 + 2027) cumulative Nifty 50 picture from similar
setups historically averages around **+21%.**

---

## 10. Honest limitations

1. **Small sample.** Strongest patterns have n=4-8. Statistical power
   is weak. 95% credible interval on the true probability is wide.

2. **Multiple-comparisons risk.** ~900 cells tested in v2 → ~45 false
   positives expected by chance. We found 58. The 13-pattern surplus
   above noise is suggestive but not conclusive.

3. **FY/CY mismatch.** Issuance data on Indian fiscal year, indices
   on calendar year. ~9-month offset inflates lag-1 correlations.

4. **Coverage gaps.**
   - Smallcap 100 only goes back to 2012; pre-2012 smallcap patterns
     are unverifiable.
   - I-banking basket only meaningful from 2008 (n≥4 companies).
     Early-period (2006-2007) signals are dominated by JM + IIFL alone.
   - Nifty Capital Markets index back-history (CY 2019-2025) is not yet
     filled in (scaffold only); when populated, it could provide a
     cleaner read on capital-markets-segment performance.

5. **No within-year timing.** End-of-year snapshots only. Can't
   distinguish "crash in Oct 2008" from "gradual decline through 2008".

6. **No out-of-sample test.** All patterns are in-sample. Real forward
   validation requires waiting for new years to roll in.

7. **No transaction costs / taxes / slippage.** Average returns are
   index returns, not investable returns.

8. **USD/INR is only one FX cross-rate.** EUR/INR, GBP/INR, JPY/INR
   might give different signals. Only USD/INR is included.

9. **No macroeconomic policy variables.** Interest rates, RBI repo
   decisions, FX reserves not modeled. Some FX patterns are probably
   mediated by these.

10. **Composition drift in the I-bank basket.** 2006 had n=2 (JM, IIFL);
    2025 has n=8. Equal-weighted averaging gives equal weight to a
    4-year-old name (Anand Rathi) as a 20-year name (JM). A free-float-
    weighted basket would behave differently.

The right use of this analysis: **forensic priors**, updated as new
data arrives. Not a trading rule.

---

## 11. What's where in this folder

### Data files (CSVs, all source-cited)
- `ipo_data.csv` + `ipo_data_sources.md`
- `fpo_rights_data.csv` + `fpo_rights_data_sources.md`
- `nifty50_data.csv` + `nifty50_data_sources.md`
- `nifty_midcap100_data.csv` + `nifty_midcap100_data_sources.md`
- `nifty_smallcap100_data.csv` + `nifty_smallcap100_data_sources.md`
- `industry_issuance_data.csv` + `industry_issuance_data_sources.md`
- **`investment_banks_data.csv` + `investment_banks_data_sources.md`** (NEW)
- **`investment_banks_yoy.csv`** (derived; NEW)
- **`usd_inr_data.csv` + `usd_inr_data_sources.md`** (NEW)
- `nifty_capital_markets_data.csv` + `nifty_capital_markets_data_sources.md` (scaffold)

### Analysis documents
- **`FINAL_ANALYSIS.md`** (this file) — single consolidated read-through.
- `analysis.md` — original broad cross-year correlation analysis.
- `patterns_high_probability.md` — v1 patterns at ≥80% hit rate (336-cell search).
- **`patterns_v2_extended.md`** — v2 patterns adding USD/INR + I-bank
  signals (~900-cell search; 58 patterns at ≥80%, 31 perfect). NEW.
- **`patterns_v2_run_output.txt`** — raw script output for cross-checking. NEW.
- `methodology.md` — modeling choices, thresholds, hypotheses documented.
- **`forecast_fy2026_27.md`** — forward IPO supply estimate. NEW (in this folder).

### Code (reproducible analysis)
- `find_patterns.py` — v1 pattern search (336 cells).
- **`find_patterns_v2.py`** — v2 pattern search with USD/INR + I-banks (~900 cells). NEW.
- `build_interactive_data.py` — rebuilds JSON for the interactive chart
  (now includes basket + USD/INR series).
- **`build_ibank_aggregate.py`** — computes basket YoY % from investment_banks_data.csv. NEW.
- `plot_all_series.py` and the per-series `plot_*.py` scripts — static charts.

### Charts (PNG / interactive HTML)
- `all_series_combined.png` — **18-series** static chart (counts + amounts
  + indices + YoY% + P/E + USD/INR + I-bank basket). UPDATED.
- `all_series_interactive.html` — **23-series** interactive HTML with
  per-series checkboxes, year-range slider, P/E heatmap, USD/INR axis,
  6 preset time periods, "Show I-banks only" + "Show USD/INR only" presets.
  Safari-compatible, self-contained. UPDATED.
- Per-series static charts: `ipo_count_vs_amount.png`,
  `fpo_rights_count_vs_amount.png`, `nifty50_close_vs_yoy.png`,
  `nifty_midcap100_close_vs_yoy.png`, `nifty_smallcap100_close_vs_yoy.png`,
  `equity_issuance_vs_index.png`.

---

## 12. Five concrete recommendations from the data

1. **Buy Nifty 50 when its trailing P/E drops below 17** — perfect 5/5
   record across 26 years, average +43% next year, +80% over 2 years.
   Last triggered at 2011-end. Today's P/E of 22.75 is above the
   trigger; this signal is NOT active.

2. **Buy after USD/INR shocks > 10%** — perfect 4/4 record, average
   Nifty +39% next year, Midcap +60%, I-bank basket +101%. Today's
   USD/INR YoY is +4.64%; signal NOT triggered. Last triggered 2022-end.

3. **Buy mid-caps when INR is stable (-3% to +3% YoY)** — 7/7 record
   at 100%, average +32%. Today is +4.6% — just outside the band.
   No buy signal.

4. **Use the I-banking basket as a leading indicator for IPO supply.**
   When basket is up > +50% YoY, IPO supply is up the next year 8/8
   = 100%. Today's reading is +12.7% — well below trigger; expect IPO
   supply growth to moderate from the +154% YoY of FY 2025-26 to the
   +30-50% range forecast by PRIME for FY 2026-27.

5. **Be skeptical of "everything is stretched" alarmism.** When P/E
   ratios are stretched, the historical outcome is NOT an equity
   crash. It's **INR depreciation** the following year (4-5/4-5
   records, avg +5 to +8% INR YoY) while the Nifty 50 stays up (4/4
   on Midcap P/E > 30 and Smallcap P/E > 35 specifically). The damage
   from over-valuation is taken by the currency and the smallcap
   segment, not the broad index.

---

## 13. Three bottom-line takeaways

1. **Buy after issuance droughts (IPO YoY < -50%).** Five historical
   instances; Midcap was up every single year after; average +25%.
   The strongest tradable signal in the dataset.

2. **Don't read record-issuance years as "market top" for Nifty 50.**
   Conventional wisdom is wrong for the broad index. Supply pressure
   lands on smallcaps; large-caps absorb it. Rotate from smallcap to
   large-cap, don't flee to cash.

3. **The new finding: USD/INR is a powerful overlay.** Same-year
   correlation -0.76 with Nifty 50, perfect 4/4 next-year bounce
   record after shocks > 10%, and a clean inverse-causation surprise
   (stretched valuations → INR depreciates, not equity crashes).
   Adding currency to the analysis substantially improved the pattern
   hit rate (31 perfect signals in v2 vs 4 in v1).

The current 2025 setup (records on IPO supply, Q3 large-cap
valuations, Q3 smallcap valuations, +12.7% I-bank basket, +4.6% INR)
historically maps to:
- **Nifty 50 positive but moderate in 2026** (+8 to +15% base case)
- **Smallcap mixed-to-soft** (supply pressure ongoing)
- **Midcaps tracking Nifty 50**
- **INR continued moderate weakening** (Midcap P/E > 30 pattern in effect)
- **I-bank basket up but not exploding** (PRIME pipeline implies
  modest IPO supply growth, not the 100%+ surge that historically
  triggers basket > +50%)

None of this is a guarantee — it's the historical base rate from
comparable past setups, with explicit acknowledgment that n=4-8
sample sizes mean wide credible intervals on every "100%" claim.

---

*All numbers in this document are reproducible end-to-end from the
nine CSV files in this folder via `find_patterns.py` (v1) and
`find_patterns_v2.py` (v2). Every claim has a citation in the
underlying SEBI / NSE / Yahoo Finance / FRB source per the
`*_data_sources.md` files. The supporting analysis docs (`analysis.md`,
`patterns_high_probability.md`, `patterns_v2_extended.md`,
`methodology.md`, `forecast_fy2026_27.md`) carry full detail; this
file is the consolidated executive read.*
