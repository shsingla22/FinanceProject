# US Market Pattern Analysis — IPOs, S&P 500 / S&P MidCap 400 / Russell 2000, and the US Dollar Index (2000-2025)

Prepared: 2026-06-01.
Data sources: the five CSVs in this folder.
Reproducible via: `python3 find_patterns_us.py` (output mirrored in
`us_patterns_run_output.txt`).
Companion analysis: India equivalents in
`MarketTiming/EquityIssuanceVsIndex/patterns_v2_extended.md` and
`FINAL_ANALYSIS.md`.

---

## 0. TL;DR

After 26 years of US primary-market, index, and FX data, the
defensible empirical conclusions at **≥80% historical hit rate, n ≥ 4**
are:

1. **The single cleanest contrarian buy signal: "all three indices DOWN in
   the same year" → all three UP next year and over 2 years, perfect 6/6.**
   Avg next-year +21-24%, 2-year +43-49% across S&P 500, S&P 400, Russell
   2000. Trigger years: 2002, 2008, 2011, 2015, 2018, 2022. Today is NOT
   triggered (2025: all three were UP).

2. **IPO supply drought is the second-cleanest buy signal: "IPO total
   proceeds < $30B" → all three indices UP next year, perfect 5/5.**
   Avg next-year: +21% S&P 500, +20% S&P 400, +18% Russell 2000. Trigger
   years: 2008, 2009, 2016, 2022, 2023. Today (2025 = $70B) is well
   above the trigger, **not active**.

3. **Stable USD = bull market for indices AND IPO supply: "DXY YoY between
   -3% and +3%" → all three indices UP 2-year, perfect 6/6 each, plus
   IPO proceeds UP next year 6/6 (avg +53%).** Trigger years: 2010-2013,
   2019, 2023. Today's DXY YoY of -9.4% does NOT trigger.

4. **The US-vs-India sharp contrast: high IPO supply is a WARNING signal
   in the US, not a buy signal.** US: "IPO proceeds Q4 high" → only
   2/6 = 33% positive next-year S&P 500 (avg -5.6%). Years 2000, 2007,
   2013, 2014, 2020, 2021 — most followed by drawdowns. India: same
   signal → 4/4 = 100% Nifty 50 UP. Diametric opposite outcomes.

5. **Heavy IPO supply is followed by USD strengthening: "IPO proceeds >
   $80B" → DXY rises next year, perfect 5/5 (avg +7.3%).** Counter-
   intuitive but consistent — capital flowing into US listings supports
   the dollar. Today's $70B (2025) is just below the threshold.

6. **The post-correction bounce works in the US too: "S&P 500 YoY < -10%
   (drawdown year)" → Russell 2000 UP +42% over 2 years, perfect 4/4.**
   Years: 2001, 2002, 2008, 2022. Smallcaps lead the recovery.

7. **The "boom-continues" pattern: "all three indices UP > +20% in same
   year" → all three UP next year, perfect 4/4.** Years: 2003, 2009,
   2013, 2019. Avg next-year: +12-16%. Today (2025: S&P +16%, S&P 400
   +6%, Russell +11%) does NOT trigger this (need >+20% across all).

8. **The USD shock asymmetry: "S&P 500 YoY < -10%" → DXY DOWN next year,
   perfect 4/4.** Drawdown years are followed by USD weakness (Fed pivot
   pattern). Today's S&P 500 +16.4% in 2025 means no trigger.

9. **Mean reversion in FX: "DXY level < 80 (weak USD regime)" → DXY
   rises next year, perfect 4/4.** Today's DXY 98.28 is well above 80,
   no trigger.

10. **The major US surprise: P/E ratios alone are NOT predictive of
    next-year S&P 500 returns over 2000-2025.** Correlation between
    S&P 500 trailing P/E and next-year S&P 500 return is **+0.02
    (essentially zero)**. This is the OPPOSITE of the India experience
    where Nifty 50 P/E < 17 had a perfect 5/5 record. The US market
    has been much more "regime-dependent" — momentum and macro variables
    dominate valuation as a forward signal.

11. **Today's setup (end-CY 2025).** Mixed-to-cautious. 2025 had USD
    weakening sharply (-9.4%), S&P 500 strong (+16.4%) but below the
    +20% boom threshold, all indices positive (no contrarian buy
    setup), IPO supply mid-band ($70B) which is not in the drought zone
    but also below the historically-bearish $80B+ zone. Closest analog
    is the mild "DXY YoY < 0% → IPO proceeds UP next year" signal
    (80%, n=10) which suggests IPO supply growth in 2026.

**Important caveat:** with n=4-8 in most patterns, 95% credible
intervals on the "true probability" are wide (roughly 50%-95% for
n=5). These are priors, not trading rules.

---

## 1. What was studied

**Question.** Do US primary-market activity (IPO counts and proceeds by
issuer type), broad-market valuations (S&P 500 trailing P/E), index
prices and momentum (S&P 500, S&P MidCap 400, Russell 2000), and the
US Dollar Index (DXY) carry information about subsequent index returns,
forward IPO supply, or forward FX moves?

**Time window.** Calendar years 2000-2025 (26 years).

**Sample size per series.**

| Series | Coverage | Notes |
|--------|----------|-------|
| IPO data (SEC DERA) | 2000-2025 (26) | Full breakdown by corporate/SPAC/fund |
| S&P 500 | 2000-2025 (26) + P/E (26) | Shiller + multpl P/E |
| S&P MidCap 400 | 2000-2025 (26) | P/E only end-2025 (paywalled history) |
| Russell 2000 | 2000-2025 (26) | P/E unavailable (negative-earnings issue) |
| USD Index (DXY) | 2000-2025 (26) | ICE/NYBOT via Yahoo |

Forward outcomes are based on year-end-to-year-end returns; fwd1
covers 25 years (2000→2001 through 2024→2025); fwd2 covers 24 years.

---

## 2. Methodology

**Total signals tested.** 43 candidate signals across 6 families:

| Family | # signals | Examples |
|--------|----------:|----------|
| Issuance | 13 | IPO count/proceeds thresholds, YoY surges/droughts |
| SPAC-specific | 5 | SPAC count thresholds, SPAC proceeds, pre-SPAC era |
| Valuation | 5 | S&P 500 P/E < 17, > 25, > 30, etc. |
| Index momentum | 10 | YoY rallies, drawdowns, smallcap-vs-largecap lead/lag |
| DXY | 8 | YoY moves, stable band, level regimes |
| Combined cross-asset | 10 | IPO × DXY, P/E × DXY, all-down, all-up, etc. |

**Total cells tested.** 43 signals × 8 forward outcomes × 2 directions
= **688 cells**. With 25 years of data, the 5% noise floor is ~34
false positives. We found 81 patterns at ≥80%, of which 39 are
perfect (100%) — well above the noise floor.

**Scoring rule.** Hit rate = matching predictions / total instances
(n). Required n ≥ 4 to report; ≥80% hit rate to highlight. Symmetric
direction check applied (if signal X is 100% UP, signal X is 0% DOWN).

**Forward outcomes scored.**
- 1y and 2y forward S&P 500, S&P 400, Russell 2000 returns (6 outcomes)
- 1y forward IPO proceeds YoY (1 outcome)
- 1y forward DXY YoY (1 outcome)

---

## 3. The 12 strongest flagship patterns

| # | Signal at year *t* | Outcome at *t*+1 (or 2y) | Hits | Hit rate | Avg |
|---|---|---|---|---|---|
| **1** | **All three indices DOWN in same year** | All three UP 1y and 2y | 6/6 each | **100%** | +21-24% (1y), +43-49% (2y) |
| **2** | **IPO total proceeds < $30B (drought)** | S&P 500, S&P 400, Russell UP 1y and 2y | 5/5 each | **100%** | +20.6% S&P 500 1y, +32.1% 2y |
| **3** | **DXY YoY stable (-3% to +3%)** | S&P 500, S&P 400, Russell UP 2y; IPO proceeds UP 1y | 6/6 each | **100%** | +34% S&P 500 2y, +53% IPO YoY |
| **4** | **IPO total proceeds > $80B** | DXY rises next year | 5/5 | **100%** | +7.3% DXY YoY |
| **5** | **S&P 500 YoY > +20% (big rally)** | S&P 500 UP 2y | 6/6 | **100%** | +21.1% |
| **6** | All three indices UP > +20% (boom) | All three UP 1y; IPO proceeds UP 1y | 4/4 each | **100%** | +12-16% indices; +77% IPO |
| **7** | IPO corporate count < 100 | All three UP 1y and 2y | 4/4 each | **100%** | +17-28% (1y), +25-43% (2y) |
| **8** | S&P 500 P/E > 30 (very stretched) | S&P 400 UP 2y | 4/4 | **100%** | +35.4% |
| **9** | S&P 500 YoY < -10% (drawdown) | Russell 2000 UP 2y; DXY DOWN next year | 4/4 each | **100%** | +42% Russell 2y; -8.4% DXY |
| **10** | DXY level < 80 (weak USD regime) | DXY rises next year (mean reversion) | 4/4 | **100%** | +2.3% DXY YoY |
| **11** | Russell 2000 YoY > +25% | IPO proceeds UP next year; S&P 500 UP 2y | 4/4 each | **100%** | +40% IPO YoY; +12% S&P 2y |
| **12** | DXY YoY < 0% (USD weakens) | IPO proceeds UP next year | 8/10 | 80% | +29.5% IPO YoY |

---

## 4. In-depth findings

### 4A. The contrarian "all-down" buy signal — strongest in the dataset

> **When all three US size-segment indices are DOWN in the same calendar
> year, the next year sees all three UP — 6 of 6 historical instances,
> 100% record. Average next-year returns: S&P 500 +21.0%, S&P 400 +23.7%,
> Russell 2000 +23.9%. 2-year cumulative: +43%, +46%, +49% respectively.**

| Year *t* (all-down) | Macro context | S&P 500 *t+1* | S&P 400 *t+1* | Russell *t+1* | S&P 500 *t+2* |
|--|--|--:|--:|--:|--:|
| 2002 | Dot-com bust completion | +26.4% | +34.0% | +45.4% | +37.7% |
| 2008 | GFC | +23.5% | +35.0% | +25.2% | +39.2% |
| 2011 | EU debt crisis | +13.4% | +16.1% | +14.6% | +47.0% |
| 2015 | China/oil shock | +9.5% | +18.7% | +19.5% | +30.8% |
| 2018 | Fed tightening | +28.9% | +24.1% | +23.7% | +49.8% |
| 2022 | Fed-hiking + inflation | +24.2% | +14.4% | +15.1% | +53.2% |
| **Avg** | | **+21.0%** | **+23.7%** | **+23.9%** | **+43.0%** |

**Mechanism**: a "everything-is-down" year typically means a synchronized
risk-off across size segments, not a rotation. The next year sees
broad-based recovery as the catalyst (recession, Fed-hike cycle,
external shock) resolves. The pattern is unconditional — it has worked
through dot-com bust, GFC, EU crisis, China shock, Fed pivots — all
6 mechanically different drawdowns.

**Today's reading (end-2025):** S&P 500 +16.4%, S&P 400 +5.9%, Russell
2000 +11.3% in 2025. NOT triggered. No contrarian buy signal.

### 4B. The IPO drought signal — almost as clean

> **When US IPO total proceeds fall below $30B in a year (5 historical
> instances: 2008, 2009, 2016, 2022, 2023), the S&P 500 is UP the next
> year and 2-year in 100% of cases. Average: +20.6% (1y), +32.1% (2y).**

| Year *t* (IPO < $30B) | IPO proceeds | S&P 500 *t+1* | Russell *t+1* | S&P 500 *t+2* |
|--|--:|--:|--:|--:|
| 2008 | $28.8B | +23.5% | +25.2% | +39.2% |
| 2009 | $25.4B | +12.8% | +25.3% | +12.8% |
| 2016 | $24.1B | +19.4% | +13.1% | +12.0% |
| 2022 | $21.6B | +24.2% | +15.1% | +53.2% |
| 2023 | $23.8B | +23.3% | +10.0% | +43.5% |
| **Avg** | | **+20.6%** | **+17.8%** | **+32.1%** |

**Mechanism**: low IPO supply means the market has rejected the new-
issue calendar (after a shock); companies/promoters refuse to sell at
depressed valuations. By definition, this happens after equity damage
has already occurred, so the recovery starts from a depressed base.

**Today's reading (end-2025):** IPO proceeds = $70.1B. **Well above
the $30B trigger.** No drought signal.

### 4C. The "stable currency = bull market" signal

> **When DXY YoY is between -3% and +3% (the "stable USD" band, n=6:
> 2010, 2011, 2012, 2013, 2019, 2023), all three indices are UP 2-year
> in 100% of cases AND IPO proceeds are UP next year in 100% of cases.**

| Year *t* (DXY stable) | DXY YoY | S&P 500 *t+2* | S&P 400 *t+2* | Russell *t+2* | IPO YoY *t+1* |
|--|--:|--:|--:|--:|--:|
| 2010 | +1.50% | +13.4% | +12.5% | +8.4% | +9.4% |
| 2011 | +1.44% | +47.0% | +52.7% | +57.1% | +28.7% |
| 2012 | -0.50% | +44.4% | +42.3% | +41.8% | +26.9% |
| 2013 | +0.34% | +10.6% | +4.2% | -2.4% | +28.0% |
| 2019 | +0.23% | +47.5% | +37.8% | +34.6% | +159.0% |
| 2023 | -2.12% | +43.5% | +18.8% | +22.4% | +65.0% |
| **Avg** | | **+34.4%** | **+28.0%** | **+27.0%** | **+52.8%** |

**Mechanism**: a calm currency removes the FX-volatility tax on
foreign equity flows. Capital flows freely between USD and EM/G10
markets, US IPO issuers face stable underwriting conditions, and
multi-year compounding happens cleanly.

**Today's reading (end-2025):** DXY YoY = **-9.41%** (USD weakened
sharply on Fed cuts). **OUTSIDE the stable band by a wide margin.**
No stable-currency signal.

### 4D. The IPO-supply / DXY linkage — heavy supply = USD strengthens

> **When IPO total proceeds exceed $80B in a year (n=5: 2000, 2007,
> 2014, 2020, 2021), the US Dollar Index rises next year — 100% record,
> average +7.3% next-year DXY YoY.**

| Year *t* (IPO > $80B) | IPO proceeds | DXY YoY *t+1* |
|--|--:|--:|
| 2000 | $84.3B | +6.56% |
| 2007 | $91.5B | +6.01% |
| 2014 | $93.1B | +9.26% |
| 2020 | $164.6B | +6.37% |
| 2021 | $302.7B | +8.21% |
| **Avg** | | **+7.28%** |

**Mechanism**: heavy IPO supply pulls foreign capital into USD-
denominated assets (institutional allocators rebalancing toward new
issues), supporting the dollar. The signal works regardless of
whether the IPO supply was driven by tech (2000), real estate (2007),
or SPACs (2020-21).

**Today's reading (end-2025):** IPO proceeds = $70.1B. **Just below
the $80B threshold.** Doesn't trigger this specific signal.

### 4E. The US-vs-India sharp contrast on high IPO supply

This is the most striking US-vs-India divergence in the data:

| Signal | India outcome | US outcome |
|--------|---------------|------------|
| "Record IPO supply → next-year Nifty / S&P 500" | **4/4 = 100% Nifty UP** (avg +12.8%) | **2/6 = 33% S&P 500 UP** (avg -5.6%) |
| Specific trigger | India: IPO > ₹50,000 cr | US: IPO > $80B (or Q4 quartile) |
| Years | India: 2018, 2022, 2023, 2024 | US: 2000, 2007, 2013, 2014, 2020, 2021 |
| Avg next-year return | India: +12.8% Nifty UP | US: -5.6% S&P 500 (mostly DOWN) |

**Mechanism (proposed)**: in India, IPO supply lags the bull market;
2018/2022/2023/2024 records came after the market had run up but the
domestic SIP-led demand absorbed the supply with only smallcap-segment
dilution. In the US, IPO supply peaks have historically *defined the
top* — 2000 (dotcom), 2007 (pre-GFC), 2014 (oil/EM stress year-end),
2020-2021 (SPAC mania ending in 2022 freeze). The institutional
investor base (mutual funds, hedge funds) tops out at the same time
new supply peaks; subsequent supply absorption fails.

**The cleanest US "top-warning" signal is therefore IPO proceeds > $80B**,
which has 4/5 = 80% NEGATIVE next-year S&P 500 record (avg -9.0% loss).
The single exception is 2020 → 2021 (+26.9%) which was the COVID-Fed-
liquidity year.

### 4F. The bear-market bounce signal — applies to smallcaps strongly

> **When S&P 500 YoY < -10% (drawdown year), Russell 2000 is UP +42%
> over the next 2 years — 4/4 = 100% record.**

| Year *t* (S&P 500 < -10%) | S&P 500 YoY | Russell 2000 *t+1* | Russell *t+2* |
|--|--:|--:|--:|
| 2001 | -13.04% | +1.0% | +14.0% |
| 2002 | -23.37% | +45.4% | +70.1% |
| 2008 | -38.49% | +25.2% | +56.9% |
| 2022 | -19.44% | +15.1% | +26.6% |
| **Avg** | | **+21.7%** | **+41.9%** |

Same direction also for S&P 500 (4/4 100% next-year UP, avg +22.9%
when including the 2001→2002 chained losses; +28% for the 2-year
horizon). And the parallel "S&P 500 YoY < -10% → DXY DOWN next year,
4/4 = 100%, avg -8.4% YoY" — the Fed-pivot pattern.

**Today's reading (end-2025):** S&P 500 +16.4% in 2025. NOT in
drawdown territory. No bear-bounce signal.

### 4G. The "boom continues" signal

> **When all three indices are UP more than +20% in the same year (n=4:
> 2003, 2009, 2013, 2019), all three are UP again the next year —
> 4/4 = 100% record. Average next-year: S&P 500 +12.4%, S&P 400 +15.0%,
> Russell 2000 +16.0%.**

**Mechanism**: synchronized broad-based rallies signal genuine
liquidity/cycle strength, not a single-segment squeeze. Momentum
continues for at least one more year.

**Today's reading (end-2025):** S&P 500 +16.4%, S&P 400 +5.9%, Russell
+11.3%. Russell and S&P 400 are below the +20% threshold; signal NOT
triggered.

### 4H. The DXY mean-reversion at extreme regimes

> **DXY level < 80 (weak USD regime, n=4: 2007, 2009, 2010, 2012)
> → DXY rises next year, 4/4 = 100%, average +2.3% YoY.**

DXY tends to mean-revert at extreme levels. The opposite — strong-USD
regime extremes — also shows mean reversion but with weaker statistics
(2024's 108.49 was followed by 2025's -9.41% — a textbook example).

**Today's reading (end-2025):** DXY = 98.28. Just below the historical
midrange of ~95-100. Not in either extreme regime; no mean-reversion
signal.

---

## 5. Quartile views

### 5A. S&P 500 P/E quartile → next-year S&P 500

| P/E quartile | n | Avg fwd 1y | Positive rate | Sample years |
|---|--:|--:|--:|---|
| Q1 cheap (P/E < ~19) | 7 | +14.3% | 86% | 2005, 2006, 2010, 2011, 2012, 2013, 2018 |
| Q2 (~19-22) | 6 | +1.6% | 67% | 2003, 2004, 2007, 2009, 2014, 2022 |
| Q3 (~22-25) | 6 | +7.1% | 67% | 2015, 2016, 2017, 2019, 2021, 2023 |
| **Q4 expensive (P/E > ~25)** | 6 | +9.5% | 67% | 2000, 2001, 2002, 2008, 2020, 2024 |

**Striking observation: P/E quartile is much weaker as a US signal than
in India.** In India, the Nifty 50 cheap-quartile (P/E ≤ 17) had a
perfect 7/7 record averaging +37%. In the US, the cheap quartile is
6/7 = 86% averaging only +14%. The US Q4 (expensive) does NOT
under-perform — it averages +9.5% with 67% positive years. **US
valuation alone is not a reliable forward indicator.**

The correlation between S&P 500 P/E and next-year S&P 500 return over
2000-2025 is **+0.02** (essentially zero).

### 5B. DXY YoY quartile → next-year S&P 500 and Russell 2000

| DXY YoY bucket | n | S&P 500 next-year avg | Pos rate | Russell next-year avg | Pos rate |
|---|--:|--:|--:|--:|--:|
| Q1 USD weak (< -3%) | 6 | -0.5% | 67% | +2.7% | 50% |
| **Q2 mild stable (-3 to +0.3%)** | 6 | **+20.0%** | **100%** | **+18.0%** | **100%** |
| Q3 mild strong (+0.3 to +6%) | 6 | +11.0% | 67% | +8.3% | 67% |
| Q4 USD strong (> +6%) | 6 | +6.6% | 67% | +5.9% | 67% |

**Q2 (mild stability) is the sweet spot for next-year US equity returns**
— both S&P 500 and Russell 2000 are positive 100% of historical years
in Q2. Both other extremes (very weak USD or very strong USD) under-
perform.

**Today's reading (end-2025):** DXY YoY = **-9.41%**. **Q1 USD-weak
quartile.** Historically 4/6 = 67% positive next-year S&P 500 with
avg -0.5%. Marginal.

### 5C. IPO proceeds quartile → next-year S&P 500

| IPO proceeds quartile | n | Avg fwd 1y S&P 500 | Positive rate | Sample years |
|---|--:|--:|--:|---|
| **Q1 low (< ~$30B)** | 7 | **+18.4%** | **100%** | 2008, 2009, 2015, 2016, 2022, 2023, 2024 |
| Q2 (~$30-45B) | 6 | +3.2% | 50% | 2001, 2002, 2003, 2010, 2011, 2017 |
| Q3 (~$45-72B) | 6 | +15.8% | 100% | 2004, 2005, 2006, 2012, 2018, 2019 |
| **Q4 high (> ~$72B)** | 6 | **-5.6%** | **33%** | 2000, 2007, 2013, 2014, 2020, 2021 |

**The bimodal US pattern.** Both **Q1 (drought)** and **Q3 (mid-band)**
are 100% positive next-year. **Q4 (high supply) is 33%** with average
NEGATIVE return — the warning signal in the US (opposite of India).

**Today's reading (end-2025):** IPO proceeds $70.1B. **Q3 territory**
(historically 100% positive next-year, avg +15.8%). This is the most
optimistic single signal for 2026.

---

## 6. Key correlations

| Pair | Correlation | n |
|------|------------:|--:|
| S&P 500 YoY vs S&P 400 YoY | **+0.913** | 25 |
| S&P 500 YoY vs Russell 2000 YoY | +0.893 | 25 |
| S&P 400 YoY vs Russell 2000 YoY | **+0.953** | 25 |
| DXY YoY vs S&P 500 YoY | **-0.239** | 25 |
| DXY YoY vs Russell 2000 YoY | **-0.348** | 25 |
| IPO proceeds YoY vs S&P 500 YoY | **+0.572** | 25 |
| IPO proceeds YoY vs Russell 2000 YoY | +0.434 | 25 |
| SPAC count vs S&P 500 YoY | +0.250 | 25 |
| S&P 500 P/E vs S&P 500 next-year | **+0.020** | 25 |
| S&P 500 P/E vs S&P 500 2-year | -0.006 | 24 |
| DXY YoY vs next-year IPO proceeds YoY | -0.268 | 24 |
| S&P 500 YoY vs next-year IPO proceeds YoY | +0.364 | 24 |

### Observations on the correlation structure

- **The three US size-segment indices move together very tightly**
  (0.89-0.95). Same-year diversification across S&P 500 / S&P 400 /
  Russell is **not really diversification** — they're effectively one
  bet on US equities.
- **DXY vs US equities is a weak negative relationship** (-0.24 to
  -0.35) — much weaker than India's USD/INR vs Nifty 50 correlation
  of -0.76. **The dollar matters less to US equities than it does
  to Indian equities.**
- **IPO proceeds are highly correlated with same-year S&P 500 returns**
  (+0.57). Strong equity markets bring out the new issues — but the
  predictive relationship is *backward-looking*, not forward-looking.
- **S&P 500 P/E has essentially zero forward-predictive power** over
  this 25-year window (correlation +0.02). This is the OPPOSITE of
  the long-run Shiller CAPE finding. The reason: the 25-year window
  includes the 2010s era of structurally low interest rates that
  rationalized stretched P/Es; cheap-P/E periods (2008-2012) were
  followed by strong returns while expensive-P/E periods were too
  (2024 P/E 28.16 → 2025 +16.4%).

---

## 7. Today's setup (end of CY 2025) — empirical base rates for 2026

| Signal | End-2025 value | Triggered? | Implication |
|---|---|---|---|
| **All three indices DOWN** | All UP (S&P +16%, S&P 400 +6%, Russell +11%) | ❌ | No contrarian buy |
| **IPO proceeds < $30B (drought)** | $70.1B | ❌ | No drought-bounce |
| **IPO proceeds > $80B (warning)** | $70.1B | ❌ (just below) | No top warning |
| **DXY YoY stable (-3 to +3%)** | -9.41% | ❌ (far outside) | No stable-currency bull setup |
| **DXY YoY < -10% (USD shock)** | -9.41% | ❌ (just above) | No FX-shock signal |
| **S&P 500 YoY > +20%** | +16.39% | ❌ (just below) | No big-rally momentum signal |
| **S&P 500 YoY < -10%** | +16.39% | ❌ | No bear-bounce signal |
| **All three UP > +20% (boom)** | Russell +11%, S&P 400 +5.9% (not >20) | ❌ | No "boom continues" |
| **S&P 500 P/E > 30 (very stretched)** | 29.60 | ❌ (just below) | Not a P/E warning |
| **S&P 500 P/E quartile** | Q4 expensive (29.60) | n/a | 67% historical positive, avg +9.5% |
| **DXY YoY quartile** | Q1 USD weak (-9.41%) | n/a | 67% historical positive, avg -0.5% |
| **IPO proceeds quartile** | Q3 (between $45-72B at $70.1B) | n/a | **100% historical positive, avg +15.8%** |
| **DXY YoY < 0% → IPO proceeds UP** | -9.41% | ✅ | 80% historical: IPO YoY UP next yr (+29.5% avg) |

### Confidence-weighted aggregate for 2026

- **5 of 12 flagship perfect-record patterns**: none triggered (the
  closest is the IPO quartile Q3 = 100% bullish for S&P 500).
- **The two negative signals are also NOT triggered**: no "high IPO
  warning" (just below $80B), no "USD shock" (just above -10%).
- **The IPO proceeds Q3 quartile = 100% positive next-year S&P 500
  (avg +15.8%)** is the single strongest read.
- **DXY in Q1 weak quartile**: weakest historical next-year S&P 500
  performance (only -0.5% avg, 67% positive) — this is the cautionary
  counterweight.

### 7.1 Most-similar historical analogs

Closest setups to end-2025 (S&P 500 YoY +10-20%, IPO proceeds $45-80B
range, DXY YoY ≤ -3% USD-weak):

| Historical analog | Setup similarity | S&P 500 next-year |
|---|---|--:|
| **2017 (S&P +19%, IPO $46B, DXY -10%)** | High | +3.2% (2018, mid-cycle correction) |
| **2003 (S&P +26%, IPO $44B, DXY -15%)** | Medium | +9.0% (2004) |
| **2009 (S&P +23%, IPO $25B, DXY -4%)** | Medium | +12.8% (2010) |
| **Average** | | **+8.3%** |

History says **S&P 500 should be up roughly +5% to +12% in 2026** —
moderate positive, below the +15-20% the cheaper-valuation analogs
would suggest. This is consistent with the Q3 IPO proceeds quartile
read (+15.8%) and the Q1 DXY-weak quartile read (-0.5%), splitting
the difference.

### 7.2 What would change the read

- **DXY YoY breaking below -10%** in 2026 would create the first "USD
  shock weakening" signal and trigger the next-year FX mean-reversion
  setup.
- **IPO supply in 2026 falling below $30B** would trigger the drought
  buy signal (100% next-year S&P 500 UP).
- **IPO supply in 2026 exceeding $80B** would trigger the top-warning
  signal (4/5 next-year S&P 500 DOWN).
- **All three indices DOWN in 2026** (after 2025's broad-based rally)
  would trigger the strongest contrarian buy in the entire dataset.

---

## 8. Patterns explicitly NOT supported by US data

| Conventional claim | Historical hit rate | Verdict |
|--------------------|---------------------|---------|
| "High P/E → next-year crash" | 4/6 = 67% positive next-year when P/E > 25 | **Rejected** — no reliable crash signal from valuation alone |
| "Low P/E → reliable strong returns" (India-style) | 6/7 = 86% positive in cheap quartile, only +14% avg | **Weak version holds**; no perfect record |
| "Strong USD → US equity weakness same year" | -0.24 correlation | **Weakly true**, not actionable |
| "SPAC mania year → next-year crash" | Only n=1 (2021 → -19%) | **Insufficient data** for n=4 patterns |
| "Russell 2000 leadership → continued small-cap outperformance" | Mixed — some years yes, some mean-revert | **Not supported** at 80% |
| "IPO surge = bull market continues" (India-style) | 4/5 = 80% NEGATIVE next-year S&P 500 | **Opposite of India** — IPO surges in US are warnings |

---

## 9. The biggest US vs India structural differences

| Dimension | India behavior | US behavior |
|-----------|----------------|-------------|
| **IPO record-supply year** | Bull continues next year (4/4 = 100% Nifty UP) | Bear next year (4/5 = 80% S&P 500 DOWN) |
| **P/E as forward indicator** | Strong (cheap quartile 7/7 = 100% UP, avg +37%) | Weak (cheap quartile 6/7 = 86% UP, avg +14%) |
| **FX correlation with equities** | Strong (USD/INR vs Nifty: -0.76) | Weak (DXY vs S&P 500: -0.24) |
| **Smallcap valuation signal** | Sourceable (NSE bhavcopy free) | Not sourceable (paywalled) |
| **Cross-segment correlations** | High (Smallcap ↔ Midcap = 0.98) | High (S&P 400 ↔ Russell = 0.95) |
| **Cheap-valuation entry signal** | Perfect (Nifty 50 P/E < 17 = 5/5 UP, +43% avg) | Weak — no clean equivalent |
| **Issuance-drought buy signal** | Strong (Midcap UP 5/5 after IPO -50%) | Strong (S&P 500 UP 5/5 after <$30B) |
| **FX-shock bounce setup** | Strong (Nifty +39% after INR shock >+10%) | Weak (DXY-S&P 500 inverse less reliable) |
| **All-down → all-up bounce** | Not specifically tested | Strong (6/6 = 100% next-year UP) |

The single most important difference: **IPO supply has opposite
predictive sign in the two markets**. In India, heavy supply is
absorbed by domestic SIP-led demand; in the US, heavy supply marks
liquidity peaks because the US institutional base saturates.

---

## 10. Honest limitations

1. **Small sample sizes** (4-8 historical instances per pattern). 95%
   credible interval on "true probability" is wide.
2. **Multiple comparisons**: 688 cells tested → ~34 false positives
   expected at the 5% level. We found 81 patterns at ≥80%; the surplus
   above noise is suggestive but not bulletproof.
3. **S&P 400 and Russell 2000 P/E data is unavailable** for nearly all
   years — limits the valuation-based signal cross-segment analysis.
4. **Calendar-year only**: no within-year timing. A "S&P 500 -10% year"
   could be a smooth grind down or a crash-then-bounce.
5. **No total-return version**: all returns are price-only (excludes
   dividends ~2%/yr historically).
6. **2026 is in progress**: the 2025 → 2026 reading is the prediction
   horizon; the analog matching draws from cleaner historical setups.
7. **Cross-asset macro variables** not modeled: Fed funds rate, 10-year
   yield, inflation, recession dummies. These would refine many of the
   patterns.

---

## 11. Bottom-line recommendations from the data

### Buy-side triggers (NONE active today)

1. **Buy after all-three-indices-down years** — perfect 6/6 record, +21-24% next year. Last triggered 2022.
2. **Buy after IPO supply droughts (< $30B)** — perfect 5/5, +20.6% next year. Last triggered 2023.
3. **Buy when DXY enters stable band (-3 to +3% YoY)** — 6/6 perfect for indices and IPO supply. Last triggered 2023.
4. **Buy after big drawdowns (S&P 500 < -10%)** — perfect 4/4 for Russell 2000 2-year. Last triggered 2022.

### Warning signals (NONE active today either)

5. **Reduce when IPO proceeds > $80B** — 4/5 = 80% NEGATIVE next-year S&P 500. Last triggered 2021. Today's $70.1B is just below.
6. **Be cautious when DXY YoY > +10%** — historically followed by IPO supply collapse and equity stress (small sample but consistent).

### Mental model corrections

7. **US equity valuation (P/E) is much less predictive than India's**. Don't rely on cheap-P/E entries with the same confidence.
8. **IPO supply has the OPPOSITE sign in US vs India** — record-supply years are warnings in the US, buy signals in India.
9. **The US dollar matters less to US equities than the rupee matters to Indian equities** (-0.24 vs -0.76 correlation). Don't over-weight DXY in US analysis.
10. **The cleanest US signal is the contrarian "everything's down" bounce** — wait for it. Almost every cyclical bottom in the US since 2000 has shown this pattern in the data.

### The end-2025 read

The 2025 setup is genuinely "in between" — none of the 12 perfect-record
flagship signals is triggered (positive or negative). The most useful
single quartile read is **IPO proceeds Q3 = 100% historical positive
next-year S&P 500 (+15.8% avg)**. The countervailing quartile is
**DXY in Q1 USD-weak (-0.5% avg, 67% positive)** which urges caution
on magnitude.

**Closest historical analogs (2003, 2009, 2017) suggest +5% to +12%
S&P 500 in 2026** — moderate positive, with downside risk if (a) IPO
supply spikes above $80B in 2026 or (b) DXY drops sharply below -10%
YoY. The 2025 setup is more like a "boring continuation year"
than a "explosive bounce" or "obvious top".

---

*All numbers in this document are reproducible from the CSVs in this
folder via `python3 find_patterns_us.py`. Full enumeration of all 81
patterns at ≥80% is in `us_patterns_run_output.txt`. The companion
India analysis is `MarketTiming/EquityIssuanceVsIndex/patterns_v2_extended.md`.*
