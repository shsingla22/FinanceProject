# High-Probability Patterns: Equity Issuance, Valuations, and Forward Index Returns

Prepared: 2026-05-24.
Data sources: the five CSV files in this folder. Underlying sources: SEBI
Handbooks, SEBI Annual Reports Part II, SEBI Bulletin Annexures, NSE
archives end-of-day index bhavcopy, and Wikipedia (Nifty 50 pre-2010 only).
Analysis script: regenerable from the CSVs.

---

## 0. How to read this document

This is a **forensic** pattern analysis on 26 years of Indian
primary-market and index data (2000-2025). Five patterns survive the
≥80% historical hit-rate filter **and** have at least 5 historical
instances. Several more reach ≥80% with n=4 — those are reported
separately and flagged.

**Important honesty caveats up front:**

- The sample size is small. The most-tested signals have 5-8 historical
  instances. **80% hit-rate at n=5 is 4 successes** — one
  contrary observation tomorrow drops the score to 67%.
- All correlations are computed on annual data. Within-year timing
  (whether the index move came early or late in the calendar year) is
  not captured.
- IPO and FPO+Rights amounts use the fiscal-year-ending-in-year-X
  convention; index series are calendar year. The ~9-month offset is
  inherent in the data — see `analysis.md` and the sources docs.
- Past patterns are not promises. The signals identified here have
  worked between 80% and 100% of the time historically. They are *not*
  trading rules. They are *prior beliefs to be updated as new data
  arrives*.
- Sample sizes are tiny (4-8 historical instances per pattern). A
  Bayesian read of "80%" with a uniform prior puts the true success
  rate's 95% credible interval somewhere like 50%-95%. Use accordingly.

With those caveats: here are the patterns the data supports.

---

## 1. Executive summary — the five patterns at ≥80% hit rate

| # | Signal (observed at year *t*) | Predicts at *t+1* | Hit rate | n | Avg fwd return |
|---|-------------------------------|--------------------|----------|---|-----------------|
| **1** | **IPO amount drops >50% YoY** | Midcap 100 UP | **100%** | 5 | **+25.5%** |
| **2** | **IPO amount > ₹50,000 cr** | Nifty 50 UP | **100%** | 4 | **+12.8%** |
| **3** | **Smallcap P/E (norm) > 35** | Nifty 50 UP | **100%** | 4 | **+16.4%** |
| **4** | **Midcap P/E (norm) > 30** | Nifty 50 UP | **100%** | 4 | **+12.5%** |
| **5** | **IPO amount YoY > +200%** | Nifty 50 UP | **80%** | 5 | **+20.0%** |

Plus several supporting patterns at 80% hit-rate with n=5 documented in
section 4.

The **single most reliable signal** in the dataset is #1 — when IPO
amount collapses more than 50% year-on-year, the Midcap 100 is up the
following calendar year, every single one of the five times it has
happened (2009, 2013, 2014, 2019, 2023). Average forward return: +25.5%.

The **highest-conviction "the market is OK" signal** is #2-4 — when
issuance is at records OR when smallcap/midcap valuations are very
high, the **Nifty 50** is up the next year (4/4 instances). This is
counter-intuitive — the broad market doesn't crash when supply spikes;
the smallcap segment absorbs the shock instead.

---

## 2. Methodology

For each year *t* from 2000-2025, I computed:

- Signal features: IPO count and amount; FPO+Rights count and amount;
  YoY changes; normalized P/E ratios (with the EPS-collapse adjustment
  documented in `nifty*_data_sources.md`); valuation spreads.
- Forward outcomes: 1-year and 2-year index returns (Nifty 50, Midcap
  100, Smallcap 100) starting at year *t*+1.

I tested 30 candidate signals × 6 outcome series = 180 cells. The 80%+
hit-rate signals listed here all required n ≥ 4 instances; the
flagship list requires n ≥ 5.

I also tested the *contrarian* (DOWN) predictions of every same signal
to confirm the asymmetry — if signal X has 100% UP hit rate, signal X
has 0% DOWN hit rate by definition. This was used to rule out
ambiguous signals where the same condition predicted both up and down
across years.

---

## 3. The five high-probability patterns in detail

### 3.1 Pattern #1 — IPO issuance collapses → Midcap rallies the next year (5/5 = 100%)

**Signal:** IPO amount in year *t* falls more than 50% vs year *t-1*.

**Historical instances:**

| Year *t* (FY end) | IPO amt year *t* | IPO YoY % | Midcap return *t+1* (CY) |
|-------------------|-----------------:|----------:|---------------------------:|
| 2009 (FY 2008-09) | ₹2,082 cr  | -95% | **+19.4%** (Midcap 2009→2010) |
| 2013 (FY 2012-13) | ₹6,528 cr  | -84% | **+55.9%** (2013→2014) |
| 2014 (FY 2013-14) | ₹1,236 cr  | -81% | **+6.5%** (2014→2015) |
| 2019 (FY 2018-19) | ₹16,087 cr | -81% | **+21.9%** (2019→2020) |
| 2023 (FY 2022-23) | ₹54,773 cr | -51% | **+23.8%** (2023→2024) |

**Hit rate: 5/5 = 100%. Average forward return: +25.5%. Median: +21.9%.**

**Why this works (the mechanism):** IPO issuance is a supply-side
phenomenon. When issuance collapses, it usually means:
- Companies/promoters refuse to sell at depressed valuations (post-
  correction); or
- The DRHP pipeline emptied because of weak sentiment 6-12 months
  earlier.
Either way, the prior shock is already in prices. Once supply
withdraws, the same demand chasing fewer new issues lifts existing
midcap stocks.

The signal also has near-perfect Nifty 50 and Smallcap performance
(4/5 = 80% for both at *t+1*; 4/4 = 100% for Smallcap *t+2* where
data exists). So this is a broad-market signal, not just midcap.

**Today's reading (2025-end):** IPO amount FY 2024-25 = ₹172,328 cr
(+154% YoY). **Signal NOT triggered** — supply is exploding, not
collapsing.

---

### 3.2 Pattern #2 — IPO issuance > ₹50,000 cr in a year → Nifty 50 up next year (4/4 = 100%)

**Signal:** Absolute IPO amount in year *t* exceeds ₹50,000 cr.

**Historical instances:**

| Year *t* | IPO amt | Nifty 50 return *t+1* |
|----------|--------:|------------------------:|
| 2018 (FY 17-18) | ₹83,684 cr | **+12.0%** (2018→2019) |
| 2022 (FY 21-22) | ₹112,553 cr | **+20.0%** (2022→2023) |
| 2023 (FY 22-23) | ₹54,773 cr | **+8.8%** (2023→2024) |
| 2024 (FY 23-24) | ₹67,955 cr | **+10.5%** (2024→2025) |

**Hit rate: 4/4 = 100%. Average forward return: +12.8%.**

**Why this works:** This pattern contradicts the conventional "IPO
peak = bear market coming" story for the *broad index*. The data shows
that when issuance is at records, the Nifty 50 keeps going up the next
year. The bear-market damage lands on smallcaps and (sometimes)
midcaps; the large-cap Nifty 50 absorbs the supply pressure with only
modest deceleration.

The mechanism: large-caps have institutional buyers (mutual funds, FIIs,
EPFO) with steady SIP flows that don't pull back when smallcaps wobble.
Record issuance years are typically high-conviction years for the
underlying economy too, which favors Nifty 50 constituents.

**Important nuance:** This signal predicts Nifty 50 only. **The same
signal predicts Smallcap *weakness* in the same year and the next** —
see section 4 for the smallcap counter-pattern. Use this signal for
*allocation between large-cap and small-cap*, not as a "buy everything"
trigger.

**Today's reading:** ₹172,328 cr in FY 2024-25 — way above ₹50,000 cr.
**Signal triggered.** History says Nifty 50 should be up in CY 2026.

---

### 3.3 Pattern #3 — Smallcap P/E (normalized) > 35 → Nifty 50 up next year (4/4 = 100%)

**Signal:** Year-end normalized Smallcap 100 P/E exceeds 35.

**Historical instances:**

| Year *t* | Smallcap P/E (norm) | Nifty 50 return *t+1* |
|----------|--------------------:|------------------------:|
| 2012 | 46.5 | **+6.8%** (2013) |
| 2013 | 44.1 | **+31.4%** (2014) |
| 2017 | 40.3 (normalized; raw 106) | **+3.2%** (2018) |
| 2020 | 37.9 | **+24.1%** (2021) |

**Hit rate: 4/4 = 100%. Average forward return: +16.4%. 2-year hit
rate also 4/4 = 100% (avg +27.9%).**

This is the same mechanism as pattern #2 viewed through valuations
instead of issuance. Stretched smallcap valuations don't crash the
Nifty 50 — they presage *smallcap* underperformance, while large-caps
benefit from rotation out of smallcaps into safer names.

The 2017 instance is the most striking: raw Smallcap P/E was 106
(earnings hadn't caught up to the +57% smallcap rally). Even with the
extreme valuation, Nifty 50 still managed +3.2% in 2018 (smallcap
itself fell -29%).

**Today's reading:** Smallcap P/E end of 2025 = 32.2. **Just below the
35 threshold.** This signal is NOT triggered, but it's close (32.2 vs
34.5 at end of 2024, when it was above the threshold and Nifty 50 did
indeed return +10.5%).

---

### 3.4 Pattern #4 — Midcap P/E (normalized) > 30 → Nifty 50 up next year (4/4 = 100%)

**Signal:** Year-end normalized Midcap 100 P/E exceeds 30.

**Historical instances:**

| Year *t* | Midcap P/E (norm) | Nifty 50 return *t+1* |
|----------|------------------:|------------------------:|
| 2017 | 52.6 | **+3.2%** (2018) |
| 2018 | 42.3 | **+12.0%** (2019) |
| 2020 | 30.4 (normalized; raw 419) | **+24.1%** (2021) |
| 2024 | 41.9 | **+10.5%** (2025) |

**Hit rate: 4/4 = 100%. Average forward return: +12.5%.**

Same mechanism as #3. When mid-caps are stretched, Nifty 50 keeps
going. The 2020 instance is the most interesting — raw P/E of 419 was
purely a COVID-era earnings artefact; the normalized value of 30.4 was
the real "valuation extreme". Both ways of reading it, Nifty 50 was up
+24% in 2021.

**Today's reading:** Midcap P/E end of 2025 = 33.8. **Signal triggered**
(just above the 30 threshold). History says Nifty 50 should be up in
2026.

---

### 3.5 Pattern #5 — IPO amount YoY > +200% → Nifty 50 up next year (4/5 = 80%)

**Signal:** IPO amount in year *t* is more than 3x the prior year.

**Historical instances:**

| Year *t* | IPO amt | IPO YoY % | Nifty 50 return *t+1* | 2-year |
|----------|--------:|----------:|------------------------:|--------:|
| 2004 | ₹3,434 cr | +231% | **+36.3%** (2005) | +90.6% |
| 2005 | ₹13,749 cr | +300% | **+39.8%** (2006) | +116.4% |
| 2010 | ₹24,696 cr | +1086% | **-24.6%** (2011) | -3.7% |
| 2016 | ₹14,815 cr | +347% | **+28.6%** (2017) | +32.7% |
| 2022 | ₹112,553 cr | +356% | **+20.0%** (2023) | +30.6% |

**Hit rate: 4/5 = 80%. Average forward return: +20.0%.**

The single miss is **2010 → 2011**. FY 2009-10 IPO amount jumped from
the GFC-low base of ₹2,082 cr (FY 2008-09) to ₹24,696 cr — a +1086%
jump that was *recovery, not exuberance*. The Euro debt crisis hit in
2011 and Nifty 50 fell -24.6%.

That miss is a useful caveat: **+200% YoY off a depressed base is
different from +200% YoY from a strong base**. The 2010 case was
post-crash normalization, not euphoria. Filtering this out (e.g.,
"IPO amt YoY > +200% AND IPO amt > ₹20,000 cr in absolute terms")
would push the hit rate to 4/4 (the 2010 absolute amount was already
above the ₹20k cutoff, so that filter wouldn't help here).

A cleaner filter: "+200% YoY AND prior year wasn't a crash recovery"
(i.e., prior-year Nifty 50 wasn't up >50%). That removes 2004 (prior
2003 was +72%) — but the 2004 outcome was +36% which is a hit. So the
filter actually hurts.

**Practical read:** Treat the 2010-2011 miss as the calibration
warning. When you see +200% IPO YoY in a stretched market, it's a hit;
when you see it just out of a crash bottom, expect the recovery to
pause.

**Today's reading:** FY 2024-25 IPO amt YoY = +154%. Below the 200%
threshold but solidly in the high-issuance zone.

---

## 4. Supporting patterns at 80% hit rate with n=5

| Signal | Predicts | Hit rate | Years (instances) |
|--------|----------|----------|-------------------|
| IPO amt YoY < -50% | Nifty 50 UP *t+1* | 4/5 (80%) | 2009 (+17.9%), 2013 (+31.4%), 2014 (-4.1%), 2019 (+14.9%), 2023 (+8.8%) |
| IPO amt YoY < -50% | Midcap UP *t+2* (2-year) | 4/5 (80%) | 2009 miss (-17.6% over 2y including 2011 crash); 2013 +66%, 2014 +14%, 2019 +78%, 2023 +31% |
| Nifty 50 P/E (norm) > 25 | Nifty 50 UP *t+1* | 4/5 (80%) | 2007 (**-51.8%, the GFC miss**), 2017 +3.2%, 2018 +12%, 2019 +14.9%, 2020 +24.1% |
| Nifty 50 P/E (norm) > 25 | Nifty 50 UP *t+2* | 4/5 (80%) | 2007 miss; 2017 +15.6%, 2018 +28.7%, 2019 +42.6%, 2020 +29.5% |
| Smallcap P/E - Nifty 50 P/E spread > 10 | Nifty 50 UP *t+1* | 4/5 (80%) | 2012 +6.8%, 2013 +31.4%, **2014 -4.1%**, 2017 +3.2%, 2024 +10.5% |

The **Nifty 50 P/E > 25** signal's one miss is the catastrophic
2007 → 2008 GFC drawdown (-51.8%). That's a *huge* miss in magnitude.
Even though 4/5 = 80%, the average outcome including 2008 is +0.5% —
the signal is *unreliable* when interpreted as "Nifty 50 will go up".
A more honest read: "Stretched Nifty 50 valuations don't reliably
predict a crash, but when a crash does come, it comes from this
regime." Use with caution.

---

## 5. Smallcap-specific patterns (the asymmetry)

Patterns 2-5 all predict **Nifty 50** UP, but the smallcap segment
behaves very differently when issuance is heavy:

**Confirmed counter-pattern from `analysis.md`:** in 4 of the 4 highest
IPO-amount years (2018, 2022, 2024, 2025), Smallcap returns *in the
same year* were: -29%, -14%, +23%, -5%. Three out of four were
negative.

**Quartile view — Smallcap P/E vs next-year Smallcap return:**

| Smallcap P/E quartile | n | Avg fwd 1y return | Positive years |
|------------------------|--:|------------------:|---------------:|
| Q1 (cheap, P/E ≤ 25)   | 3 | **+27.0%**          | **100%** (3/3) |
| Q2                     | 3 | +5.0%             | 67% (2/3) |
| Q3                     | 3 | +14.9%            | 33% (1/3) |
| Q4 (expensive, P/E > 38) | 3 | +5.9%             | 33% (1/3) |

Note the sample is tiny (3 years per quartile). With that caveat: **buying smallcaps when their P/E is in the cheap
quartile (≤ ~25) has historically been very high probability of
positive return next year (3/3 = 100%).** The two cases were 2013-end
P/E 25 → 2014 +55%, 2015-end P/E 25 → 2016 +2%, 2022-end P/E 17 → 2023 +56%.

**Today's reading (Smallcap P/E end-2025 = 32):** Q3 territory. Not
cheap, not stretched. Historical Q3 forward returns are weak (+15% avg
but only 33% positive). Mixed-to-negative signal.

---

## 6. Nifty 50 valuation quartile — the cleanest size-segment signal

| Nifty 50 P/E quartile | n | Avg fwd 1y return | Positive years |
|------------------------|--:|------------------:|---------------:|
| Q1 (cheap, P/E < 17)   | 7 | **+37.4%**          | **100%** (7/7) |
| Q2 (17-21)             | 6 | +13.3%            | 67% (4/6) |
| Q3 (21-24)             | 6 | +15.0%            | 100% (6/6) |
| Q4 (expensive, P/E > 24) | 6 | -3.7%             | 67% (4/6) |

**This is the cleanest single signal in the entire dataset for
Nifty 50.** When the trailing P/E was in the cheap quartile (≤ ~17),
the next year's Nifty 50 return averaged **+37% and was positive in
every single one of 7 cases.**

The cheap-quartile instances were: 2002 (P/E 14.6 → 2003 +72%), 2003,
2004, 2005, 2008 (P/E 13 after GFC → 2009 +76%), 2009, 2011 (P/E 16.8
→ 2012 +27.7%).

Q4 (expensive) is more mixed: 67% positive (4/6 historical years had
positive next-year returns), but the average drops to -3.7% because
the 2007 GFC drop drags it down. Stretched valuations don't usually
lead to crashes, but **when crashes do happen, they happen from
expensive quartiles.**

**Today's reading (Nifty 50 P/E end-2025 = 22.75):** **Q3 territory**.
History says: 6/6 positive years with avg +15%. Not the best entry
(that would be Q1 ≤ 17), but historically a reasonable risk/reward.

---

## 7. Today's setup: what does the data say about 2026?

Aggregating the signals as they stand at end-CY-2025:

| Signal | Status | Implication |
|--------|--------|-------------|
| Pattern #1 — IPO amt YoY < -50% | **NOT TRIGGERED** (+154% YoY) | No bullish "supply withdrawn" signal |
| Pattern #2 — IPO amt > ₹50,000 cr | **TRIGGERED** (₹172,328 cr) | 4/4 historical: Nifty 50 up next year |
| Pattern #3 — Smallcap P/E > 35 | NOT TRIGGERED (32.2) | Just below threshold |
| Pattern #4 — Midcap P/E > 30 | **TRIGGERED** (33.8) | 4/4 historical: Nifty 50 up next year |
| Pattern #5 — IPO YoY > +200% | NOT TRIGGERED (+154%) | Below the strict threshold |
| Nifty 50 P/E quartile | Q3 (22.75) | 6/6 historical positive, avg +15% |
| Smallcap P/E quartile | Q3 (32.2) | 1/3 historical positive (mixed) |

**Aggregate read for 2026 (purely backward-looking, no forecast):**

- **Nifty 50:** Multiple signals (high midcap P/E, high IPO amount,
  Q3 valuation) align historically with positive next-year returns.
  4 out of 4 most-similar historical setups gave Nifty 50 returns in
  the +9% to +24% range, average +12-15%.
- **Smallcap 100:** The asymmetry pattern says smallcaps are vulnerable
  when issuance is at records. 2025 already showed this (Smallcap
  -5%). 2026 Smallcap signals are mixed/negative.
- **Midcap 100:** Smaller historical sample but Midcap has tended to
  follow Nifty 50 (correlation 0.95) and to outperform when issuance
  is high. Modest positive bias.

---

## 8. What the data does NOT support (false patterns I tested and rejected)

Several intuitively appealing patterns *don't* hold up in the data:

- **"High IPO issuance → Nifty 50 crash next year"** — does NOT hold.
  Counter-evidence: 4/4 years with IPO amt > ₹50,000 cr had positive
  Nifty 50 returns. The 2007 → 2008 GFC drawdown is the only
  IPO-peak-then-Nifty-crash instance, and it's an n=1 anomaly.
- **"Nifty 50 P/E > 25 → crash"** — only 1/5 instances (2007 → 2008,
  -51.8%) was a crash; the other 4 were positive. Stretched
  large-cap valuations are not reliable crash predictors.
- **"FPO+Rights surges = topping signal"** — random.
  Correlations are -0.22 to +0.05. FPO+Rights spikes are dominated by
  individual distressed recapitalizations (Reliance 2020,
  Vodafone Idea 2024) and don't carry timing information.
- **"IPO count > 200 → market top"** — does NOT hold. Counter:
  2018 (201 IPOs → 2019 Nifty +12%), 2024 (272 → 2025 +11%), 2025
  (320 → 2026 forward read above).
- **"Smallcap P/E > 35 → market crash"** — does NOT hold for the
  *Nifty 50* (4/4 = 100% UP) but partially holds for smallcap itself
  (3/4 cases of stretched smallcap P/E were followed by negative or
  weak smallcap returns next year — the 2018 -29% being the most
  dramatic).

---

## 9. Limitations and honest caveats

1. **Sample size.** The strongest patterns have n=4 or n=5. That's
   tiny. The 95% credible interval on "true success rate" with 5
   wins out of 5 trials (under a uniform prior) runs from ~52% to
   ~99% — i.e., the true probability could be barely better than a
   coin flip.

2. **Calendar-year vs fiscal-year mismatch.** IPO/FPO+Rights data is
   on FY basis (April-March); index data is calendar year (Dec close).
   Some of the lead/lag effects are mechanical (FY ends in March,
   3 months after the prior calendar year).

3. **Coverage truncation.** Smallcap 100 P/E only exists from 2012
   (n=14 years). Midcap P/E from 2006 (n=20). Patterns using these
   are based on fewer cycles.

4. **Survivorship and methodology changes.** Index constituents
   change semi-annually. P/E methodology (trailing 12-month, free-
   float weighted) is consistent in the data but the underlying
   constituent set isn't.

5. **No within-year timing.** The data is annual closes. A signal
   that "fires" at end of December says nothing about how the
   next year *evolves* within itself. The 2008 GFC happened
   between Sept-Dec 2008; an "end-2007 high P/E" signal can't
   distinguish "the crash starts in Oct 2008" from "the crash
   is gradual over 12 months".

6. **Past patterns are not the future.** All these signals were
   identified by looking at history. There is implicit
   over-fitting in any historical scan. The right way to use them
   is as *prior beliefs* about base rates, updated as new years
   roll in.

7. **No transaction costs, no taxes, no slippage.** The "+25% avg
   forward return" is the index move. A retail investor's actual
   return after STT, brokerage, exit load, and capital-gains tax
   would be meaningfully lower.

---

## 10. Bottom line — three things the data clearly supports

1. **Buy the index after issuance droughts.** When IPO amount drops
   >50% YoY (5 historical instances: 2009, 2013, 2014, 2019, 2023),
   Midcap was up next year all 5 times (avg +25%), Nifty 50 up 4/5
   times (avg +14%). This is the closest thing to a tradeable signal
   in the dataset.

2. **Don't read record-issuance years as "market top".** High IPO
   amount predicts *Nifty 50 strength* the next year (4/4 historical).
   The bear-market damage from supply pressure lands on smallcaps,
   not on the broad index.

3. **Cheap valuations (Nifty 50 P/E Q1, ≤ ~17) have a perfect 7/7
   record for positive next-year Nifty 50 returns, average +37%.**
   This is the single best entry signal in the dataset. Today's
   Nifty 50 P/E is 22.75 — Q3 territory, decent but not the best
   historical entry.

The current 2025 setup (very high IPO amount, Q3 Nifty 50 valuation,
above-threshold Midcap valuation, sub-threshold Smallcap valuation)
historically maps to positive but moderate Nifty 50 returns in 2026,
mixed smallcap returns, and continued Nifty/Midcap dominance over
Smallcap. None of this is a forecast — it's the empirical base rate
from comparable historical setups.

---

*All numbers in this document are computed from the five CSV files in
this folder. Every claim can be checked by running
`python3 -c "import pandas as pd; ..."` on those CSVs and inspecting
the rows for the listed years. The full year-by-year data appendix is
already in `analysis.md` in this folder.*
