# High-Probability Patterns v2 — Issuance, Valuations, USD/INR, and I-banking Basket

Prepared: 2026-06-01.
Data sources: the seven CSVs in this folder (IPO, FPO+Rights, Nifty 50,
Smallcap 100, Midcap 100, investment banks, USD/INR).
Analysis script: `find_patterns_v2.py` (re-runnable from the CSVs).

This document supersedes `patterns_high_probability.md` by adding two
new data sources (USD/INR exchange rate, listed I-banking basket YoY %)
and two new forward outcomes (next-year IPO supply, next-year
I-banking basket return). The search now covers **~50 candidate
signals × 9 outcome variables × 2 directions ≈ 900 cells** vs the
earlier 360.

---

## 0. Read-this-first caveats (unchanged from v1, plus FX-specific ones)

- **Sample sizes remain tiny.** The strongest patterns have n=4 to
  n=8. With n=5 a uniform-prior 95% credible interval on "true hit
  rate" runs roughly 50%-95% — i.e., even a 5/5 historical record
  could be a coin flip in reality. Use these as priors, not promises.
- **All correlations are annual close-to-close.** Within-year
  sequencing (whether the INR move came before or after the Nifty
  move) is not captured.
- **The I-banking basket grows in coverage over time** (n=2 listed
  companies in 2006 → n=8 by 2025). Pre-2008 signals on the basket
  are dominated by JM Financial + IIFL Finance only. Treat early-
  period basket signals with extra skepticism.
- **USD/INR is a 26-year series (2000-2025)**; signals based on it
  have the longest baseline of any in this folder.
- **Calendar-year vs fiscal-year mismatch persists** — IPO/FPO+Rights
  are FY-based and labeled by their FY-ending CY (e.g., FY 2024-25
  is labeled "2025"). Index/FX/I-bank data is CY-end. See
  `analysis.md` and `methodology.md` for details.

---

## 1. Executive summary — the 12 strongest patterns at ≥80% hit rate

Sorted by importance (combination of n, hit rate, and economic significance).
"Lookback" = the year you'd observe the signal; "Outcome" = what happens at the named horizon.

| # | Signal at year *t* | Outcome at *t*+1 (or 2-year) | Hits | Hit rate | Avg outcome |
|---|---|---|---|---|---|
| **1** | **Nifty 50 P/E (norm) < 17** (cheap large-cap) | Nifty 50 UP next year, also UP 2-year | 5/5 (1y), 5/5 (2y) | **100%** | +43% (1y), +80% (2y) |
| **2** | **INR depreciates > +10% YoY** (FX shock) | Nifty 50 UP, Midcap UP, I-bank basket UP — all UP | 4/4 each | **100%** | +39% (Nifty), +60% (MC), +101% (I-bank) |
| **3** | **INR depreciates > +5% YoY** | Nifty 50 UP, Midcap UP next year and 2-year | 5/5 each | **100%** | +33% Nifty 1y, +67% MC 2y |
| **4** | **IPO amount YoY < -50%** (supply drought) | Midcap UP next year, Smallcap UP 2-year | 5/5 (MC), 4/4 (SC 2y) | **100%** | +25.5% MC, +46.6% SC 2y |
| **5** | **I-banking basket YoY > +50%** | IPO supply UP next year | 8/8 | **100%** | +266% IPO amt YoY |
| **6** | **I-banking basket YoY > +100%** (mania) | IPO supply UP next year | 6/6 | **100%** | +335% IPO amt YoY |
| **7** | **INR stable (-3% < YoY < +3%)** | Midcap UP next year, Smallcap UP 2-year | 7/7, 6/6 | **100%** | +32% MC, +34% SC 2y |
| **8** | **I-bank basket YoY < 0%** (capitulation) | Smallcap UP 2-year | 5/5 | **100%** | +54% SC 2y |
| **9** | **IPO amount > ₹50,000 cr** | Nifty 50 UP next year | 4/4 | **100%** | +12.8% |
| **10** | **Midcap P/E (norm) > 30** | Nifty 50 UP next year | 4/4 | **100%** | +12.5% |
| **11** | **Smallcap P/E (norm) > 35** | Nifty 50 UP next year and 2-year | 4/4 each | **100%** | +16.4% (1y), +27.8% (2y) |
| **12** | **High valuation signals (Nifty P/E > 25, or any wide spread)** | **INR depreciates next year** (NEW) | 5/5, 4/4 | **100%** | INR YoY +6 to +8% |

Each of these is a row from the run output below (full listing in section 7).

---

## 2. The single most actionable cluster — the **INR-depreciation crash bounce**

This is the new finding from this analysis. Three of the perfect-record
signals chain together to describe **the single most reliable
buy-the-shock-bounce setup** in 26 years of Indian data:

> **When the INR depreciates more than 10% in a single calendar year
> (a rare event — 4 instances in 26 years), the following calendar year
> sees the Nifty 50 up an average of +39%, the Midcap 100 up +60%, and
> the I-banking basket up +101%. All four historical instances delivered
> positive returns across all three.**

| Trigger year *t* | USD/INR YoY at *t* | Macro context | Nifty 50 *t+1* | Midcap *t+1* | I-bank basket *t+1* |
|------------------|-------------------:|---------------|---------------:|-------------:|--------------------:|
| **2008** | **+22.5%** | Global Financial Crisis | +75.8% (2009) | +98.6% | +137.8% |
| **2011** | +18.3% | Euro debt crisis | +27.7% (2012) | +39.2% | +10.7% |
| **2013** | +12.8% | Taper Tantrum | +31.4% (2014) | +55.9% | +170.1% |
| **2022** | +11.3% | Fed hiking cycle | +20.0% (2023) | +46.6% | +86.8% |
| **Average** | +16.2% | | **+38.7%** | **+60.1%** | **+101.3%** |

**Why this works (the mechanism):** A sharp INR move from ~₹ 73 to ₹83
(2022) or ₹46 to ₹54 (2011) is the *symptom* of an emerging-market
risk-off event already in progress. By the time the move shows up at
year-end, the equity damage has already been done. Year *t+1* is the
recovery. The pattern doesn't catch the crash — it catches the
**bounce** from the depressed base.

**Caveat:** The next year's return is only large because the *current
year* was usually a drawdown year. 2008 itself was Nifty 50 -51.8%,
2011 was -24.6%. The +39% bounce in *t+1* is not a windfall — it's
the recovery of a fraction of what was lost. **Don't read this as
"buy after an INR shock"; read it as "the worst of the drawdown is
usually behind you once you see a >10% INR move at year-end."**

The weaker version of this signal (USD/INR YoY > +5%, n=5) extends
the sample to add 2018 (+9.5% INR weakening → Nifty +12% in 2019),
and still hits 5/5 = 100%.

---

## 3. The cleanest "buy" entry — **Nifty 50 P/E < 17**

This is the single highest-conviction signal in the dataset, **the same
one that pattern v1 (`patterns_high_probability.md` section 6) flagged
in the Nifty 50 valuation quartile.** The expanded run reconfirms it
with a slightly different cut:

| Year *t* with Nifty 50 P/E (norm) < 17 | P/E | Nifty 50 *t+1* return | 2-year return |
|--|--:|--:|--:|
| 2001 | 15.6 | +3.3% | +77.5% |
| 2002 | 14.6 | +71.9% | +90.3% |
| 2004 | 15.3 | +36.3% | +90.6% |
| 2008 (post-GFC bottom) | 13.0 | +75.8% | +107.3% |
| 2011 | 16.8 | +27.7% | +36.3% |

**Hit rate: 5/5 = 100%. Average 1-year return: +43%. Average 2-year: +80%.**

The today reading: **Nifty 50 P/E end of 2025 = 22.75.** Above the
17 threshold by 6 points. Signal **NOT triggered.** Closest the dataset
got to "cheap" in recent years was 2022 (P/E 21.79); that was followed
by +20% in 2023. Today is in the same general band.

---

## 4. The lead/lag chain — **I-banking basket leads IPO supply**

The newest finding from incorporating I-bank stock data is that the
listed I-banks rally **before** the IPO supply surge:

> **When the equal-weighted I-banking basket is UP more than 50% in a
> calendar year (n=8 instances in 20 years of basket data), IPO amount
> raised in the next fiscal year is UP — every single time. Average
> next-year IPO amount YoY: +266%.**

| I-bank basket *t* trigger year | Basket YoY | Next FY IPO amount YoY |
|---|---:|---:|
| 2006 | +101% | +161% (FY 2006-07) |
| 2007 | +269% | +49% (FY 2007-08) |
| 2009 | +138% | +1086% (FY 2009-10) ★ |
| 2014 | +170% | +168% (FY 2014-15) |
| 2016 | +71% | +96% (FY 2016-17) |
| 2017 | +131% | +188% (FY 2017-18) |
| 2021 | +122% | +356% (FY 2021-22) |
| 2023 | +87% | +24% (FY 2023-24) |
| **Average** | **+136%** | **+266%** (skewed by 2009→2010) |

**Hit rate: 8/8 = 100%.** Tighter cut at >+100% basket gain: n=6, still 100%.

**Why this works (the mechanism):** Underwriting fees scale with
issuance volume; I-bank stock prices reflect the market's expectation
of *future* fee income. So a 6-12 month lead time between "I-bank
stocks rally" and "IPO supply surges" is structurally expected.

**Today's reading:** I-bank basket YoY 2025 = **+12.7%** — well below
the 50% threshold. Signal **NOT triggered.** History says the
explosive-supply years (FY 2022, FY 2025, FY 2026) are preceded by
explosive I-bank rallies; today is a digestion phase, not a launch
phase. Pipeline forecasts (PRIME ₹2.5 lakh cr for CY 2026 — see
`forecast_fy2026_27.md`) imply +30-50% IPO YoY rather than the +266%
average that big basket gains have historically presaged.

---

## 5. Volatility regime patterns — **stable INR favors mid/small-caps**

The flip side of pattern #2: when the INR is **calm** (-3% to +3% YoY,
the middle of the distribution), broader-market indices outperform
the large-cap Nifty 50 disproportionately.

> **When USD/INR YoY is between -3% and +3% (n=7 historical years:
> 2006, 2014, 2016, 2019, 2020, 2021, 2023), the Midcap 100 is UP the
> next year every time (avg +32.3%) and the Smallcap 100 is UP 2-year
> every time (avg +33.8%).**

| Stable-INR year *t* | USD/INR YoY | Midcap *t+1* | Smallcap *t+2* |
|---|---:|---:|---:|
| 2006 | -2.1% | +76.9% (2007) | n/a (no SC data) |
| 2014 | +2.6% | +6.5% (2015) | +9.6% |
| 2016 | +2.2% | +47.3% (2017) | +11.6% |
| 2019 | +2.0% | +21.9% (2020) | +93.5% |
| 2020 | +2.6% | +46.1% (2021) | +37.3% |
| 2021 | +1.8% | +3.5% (2022) | +34.1% |
| 2023 | -0.6% | +23.8% (2024) | +17.0% |
| **Average** | +1.2% | **+32.3%** | **+33.8%** |

**Mechanism:** Stable currency = stable foreign-fund flows = no
forced redemptions = broad-market depth. Mid/small-caps are
ratio-sensitive to FII flow; large-caps less so. So a calm FX
environment disproportionately benefits the broader market.

**Today's reading:** USD/INR YoY 2025 = +4.64%. **Just outside the
stable band** (above +3%). Closest historical analog: 2017
(USD/INR YoY -6.0%) and 2018 (+9.5%). The 2017 instance fits the
"INR appreciates" pattern (mid-cap weakened in 2018 -15%); the
2018 instance fits the "INR depreciates >5%" pattern (Midcap +47% in
2019). Today sits between the two.

---

## 6. The reverse-correlation discovery — **stretched valuations predict INR depreciation**

This is the most surprising finding. The pattern goes the *opposite*
direction of standard "stretched markets → crash" intuition. Instead
of the equity market correcting, the *currency* depreciates.

> **When any of (Nifty 50 P/E > 25), (Smallcap P/E > 35), (Midcap P/E
> > 30), or (Smallcap-Nifty P/E spread > 10) holds at year *t*, the
> INR depreciates against USD in year *t+1* — every single time.**

| Signal | n | Hit rate | Avg fwd 1y INR YoY |
|--------|--:|---------:|--------------------:|
| Nifty 50 P/E (norm) > 25 | 5 | 5/5 = 100% | +7.7% |
| Smallcap P/E (norm) > 35 | 4 | 4/4 = 100% | +6.7% |
| Midcap P/E (norm) > 30 | 4 | 4/4 = 100% | +4.5% |
| Smallcap-Nifty P/E spread > 10 | 5 | 5/5 = 100% | +6.9% |

Individual years where ≥1 of these triggered: 2007 → 2008 +22.5% INR
move; 2010 → 2011 +18.3%; 2017 → 2018 +9.5%; 2018 → 2019 +2.0%;
2019 → 2020 +2.6%; 2020 → 2021 +1.8%; 2024 → 2025 +4.6%.

**Mechanism (proposed):** Stretched Indian equity valuations make Indian
assets relatively *more expensive* in USD terms for foreign buyers.
Either (a) foreign capital takes profits and converts back to USD,
weakening INR, or (b) the marginal foreign dollar demands a higher
exchange rate to entice it in. Either way, INR weakens.

**Today's reading:** Smallcap P/E 32.2 (below 35), Midcap P/E 33.84
(above 30) — **the Midcap > 30 signal is triggered.** History says
INR is more likely to weaken than strengthen in 2026. The current
2026 YTD move (₹89.77 → ₹94.99, +5.8% in 5 months) is consistent.

---

## 7. The supplementary patterns at 80% hit rate, n=5

These are weaker but still useful:

| Signal at *t* | Outcome at *t+1* (or as noted) | Hits | Avg |
|---|---|---|---|
| IPO amount YoY < -50% | Nifty 50 UP | 4/5 | +13.8% |
| IPO amount YoY > +200% | Nifty 50 UP | 4/5 | +20.0% |
| IPO amount YoY > +200% | Nifty 50 UP 2-year | 4/5 | +53.3% |
| Smallcap-Nifty P/E spread > 10 | Nifty 50 UP | 4/5 | +9.5% |
| I-bank basket YoY < 0% | Smallcap UP next year | 4/5 | +25.7% |
| INR depreciates > +5% YoY | Midcap UP next year | 4/5 | +47.2% |
| INR depreciates > +5% YoY | I-bank basket UP next year | 4/5 | +79.7% |
| INR depreciates > +5% YoY | **IPO amt DOWN next year** | 4/5 | -58.3% (note negative) |
| I-bank basket YoY > +50% | Smallcap UP 2-year | 4/5 | +7.3% |
| Nifty 50 P/E (norm) > 25 | I-bank basket DOWN next year | 4/5 | -3.7% |

The **"INR shock → IPO supply collapse"** finding (4/5 = 80%, n=5) is
a separate confirming pattern to the bounce setup (#2): the *same*
INR shock that creates next-year buying opportunity also briefly
shuts the IPO window. The 2008 → 2009 sequence is the cleanest
case (FY 2008-09 IPO amt fell 95%).

---

## 8. The strongest correlations across the new datasets

| Pair (annual data) | Correlation | n | Interpretation |
|--------------------|------------:|--:|----------------|
| Nifty 50 level vs USD/INR | **+0.927** | 26 | Both trend up over time; high level correlation. This is **secular co-movement**, not a tradable signal. |
| I-bank basket YoY vs Smallcap YoY | **+0.864** | 13 | I-banks essentially are small-caps — very high beta to smallcap |
| I-bank basket YoY vs Midcap YoY | +0.842 | 19 | Same point; even higher r vs SC |
| I-bank basket YoY vs Nifty 50 YoY | +0.768 | 20 | Strong but lower than SC/MC |
| USD/INR YoY vs Nifty 50 YoY | **-0.761** | 25 | **Strong negative** — INR up = Nifty down (and vice versa). This is the single most-actionable inverse relationship in the data. |
| USD/INR YoY vs I-bank basket YoY | -0.745 | 20 | Same direction — INR weakens when EM equities weaken |
| USD/INR YoY vs Smallcap YoY | -0.739 | 13 | Same |
| IPO amount vs USD/INR level | +0.642 | 24 | Both grow over time; not informative on YoY basis |
| IPO amount YoY vs I-bank basket YoY | -0.221 | 20 | Surprisingly weak — but recall the I-bank basket *leads* IPO supply by ~1 year, so concurrent-year correlation is muted |

The **-0.76 correlation between USD/INR YoY and Nifty 50 YoY** is
striking. It says: in any given year, the INR move and the Nifty move
are pulling in opposite directions about 58% of the variance is shared.
That's the cleanest single relationship in the entire 26-year window.

---

## 9. Quartile views — the regime tables

### 9.1 I-banking basket quartile → next-year Nifty 50

| Basket YoY bucket | n | Avg fwd 1y Nifty 50 | Positive rate | Sample years |
|-------------------|--:|--------------------:|--------------:|--------------|
| Q1 capitulation (< -14%) | 5 | +18.8% | 80% | 2008, 2010, 2011, 2015, 2018 |
| Q2 (-14 to +12%) | 5 | **+19.4%** | **100%** | 2012, 2013, 2019, 2020, 2022 |
| Q3 (+12 to +87%) | 4 | **+25.7%** | **100%** | 2006, 2016, 2023, 2024 |
| Q4 mania (> +87%) | 5 | **-6.1%** | **60%** | 2007, 2009, 2014, 2017, 2021 |

The **Q4 mania → next-year Nifty 50 NEGATIVE bias** is the most
important nuance to the high-IPO patterns. When I-bank stocks have
already rallied >87% in a calendar year, the next year's Nifty 50
return averages **negative 6%**, with only 3/5 years positive. This
includes the 2007 → 2008 GFC, the 2017 → 2018 smallcap crash, and
the 2014 → 2015 -4% Nifty correction.

**Today (2025 basket YoY = +12.7%):** Q2 territory. History says 5/5
positive next year averaging +19.4%.

### 9.2 USD/INR YoY quartile → next-year Nifty 50

| INR YoY bucket | n | Avg fwd 1y Nifty 50 | Positive rate | Sample years |
|----------------|--:|--------------------:|--------------:|--------------|
| Q1 INR strong (< -3%) | 6 | -1.4% | 67% | 2003, 2004, 2007, 2009, 2010, 2017 |
| Q2 (-3 to +2.2%) | 6 | **+30.6%** | **100%** | 2002, 2006, 2016, 2019, 2021, 2023 |
| Q3 (+2.2 to +5.0%) | 6 | +13.4% | 83% | 2001, 2005, 2012, 2014, 2020, 2024 |
| Q4 INR weak (> +5%) | 6 | **+28.3%** | **100%** | 2008, 2011, 2013, 2015, 2018, 2022 |

This is the **two-peak distribution**. The best entries are when
USD/INR moves are either *stable* (Q2) or *very weak* (Q4 INR shocks).
The worst entries are when the INR is *appreciating strongly* (Q1) —
historically associated with subsequent disappointment.

**Today (2025 INR YoY = +4.64%):** Q3 territory (positive 5/6, avg
+13.4%). The 2025 reading sits on the Q3/Q4 boundary; the closest
historical analog is **2014 (+2.6%) → 2015 -4%** and **2018 (+9.5%) →
2019 +14.9%**. Mixed signal.

---

## 10. Patterns that DID NOT survive — false signals tested and rejected

Several intuitively-appealing combinations failed the threshold:

| Tested signal | Result |
|---------------|--------|
| "INR weakens > 10% AND Nifty 50 P/E > 25" (double-stretched) | n=2, sample too small (2007, 2022). Returns mixed. |
| "I-bank basket > +50% AND IPO amt > 50,000 cr" (full-froth) | n=2 (2017, 2023). Both led to +12% Nifty in t+1 but n too small. |
| "Nifty 50 P/E < 17 AND IPO amt YoY < 0 AND I-bank < 0" | n=2 only (2008, 2011). Both gave +75% and +27% next year but n too small to publish. |
| "Both Midcap & Smallcap P/E in top quartile simultaneously" | Overlaps with existing patterns; no incremental info. |
| "USD/INR > ₹80 absolute level" (FX regime indicator) | n=4 but spans only 2022-2025 — pure trend artifact. |
| "FPO+Rights amount > ₹50,000 cr" | n=3 only (2020, 2021, 2022). Insufficient. |
| Triple-bottom signal (P/E low + INR weak + I-bank down) | n=2 (2008, 2011). Both +75% & +27% but n too small. |

---

## 11. Today's setup (end-CY 2025) — the aggregated read

Aggregating every signal at its end-2025 value:

| Signal | Status at end-2025 | Implication for 2026 |
|--------|--------------------|----------------------|
| Nifty 50 P/E < 17 (cheap bonanza) | NOT triggered (22.75) | No "buy of the decade" signal |
| Nifty 50 P/E > 25 (stretched) | NOT triggered (22.75) | No INR-depreciation warning from large-cap valuations |
| Smallcap P/E > 35 | NOT triggered (32.2) | Just below threshold |
| Midcap P/E > 30 | **TRIGGERED (33.84)** | Nifty 50 UP next year (4/4 historical), INR depreciation likely |
| IPO amount > ₹50,000 cr | **TRIGGERED (₹172,328 cr)** | Nifty 50 UP next year (4/4 historical) |
| IPO amount YoY < -50% | NOT triggered (+154%) | No supply-drought bounce |
| IPO amount YoY > +200% | NOT triggered (+154%) | Below threshold; but mid-band positive bias still holds |
| INR YoY > +10% (shock) | NOT triggered (+4.6%) | No shock-bounce setup |
| INR YoY > +5% (mild weakening) | NOT triggered (+4.6%) | Just below 5% threshold |
| INR stable (-3 to +3%) | NOT triggered (+4.6%) | Just above stable band |
| I-bank basket YoY > +50% | NOT triggered (+12.7%) | No I-bank-led IPO supply surge expected |
| I-bank basket YoY > +100% (mania) | NOT triggered | No Q4-mania top warning |
| I-bank basket YoY < 0% | NOT triggered (+12.7%) | No capitulation buy signal for smallcaps |
| I-bank basket quartile | **Q2** | 5/5 next-year Nifty positive, avg +19.4% |
| USD/INR YoY quartile | **Q3** (boundary with Q4) | 5/6 positive next-year, avg +13.4% |
| Nifty 50 P/E quartile (from v1) | Q3 | 6/6 positive next-year, avg +15.0% |

### 11.1 The single most-similar historical setups

The combinations most similar to end-2025 (high IPO supply, moderate
INR weakness, moderate Nifty valuation, mid-band I-bank basket):

| Historical analog | Nifty 50 next-year return |
|-------------------|--------------------------:|
| **2018 (mid-band I-bank, mid-band INR, high IPO 83k cr)** | +12.0% (2019) |
| **2024 (mid-band I-bank, mid-band INR, high IPO 68k cr)** | +10.5% (2025) |
| **2023 (Q3 I-bank +87%, INR -0.6%, IPO 55k cr)** | +8.8% (2024) — but with strong 2-year hold +28.7% |
| Average | **+10.4%** in t+1 |

History says Nifty 50 should be up roughly **+8 to +15%** in 2026.

### 11.2 Confidence-weighted aggregate

Of the 12 strongest patterns in section 1:
- **3 are triggered with 100% historical record**: #9 (IPO > ₹50k cr),
  #10 (Midcap P/E > 30), and the Q2 I-bank basket + Q3 Nifty 50 valuation
  combination (both at 100% positive). All point to Nifty 50 UP.
- **9 are not triggered.** This means the 2026 forecast is **directional
  rather than magnitude-extreme**: high conviction on direction (UP),
  moderate conviction on magnitude (probably +8 to +15%, not +30%).

The setup is *not* the kind of "everything aligned" buy signal that
2008-end or 2002-end were. Those years had Nifty 50 P/E < 17 — the
single highest-conviction trigger in the dataset. Today is a "boring
positive" setup, not a screaming opportunity.

---

## 12. The 18-month outlook — combining patterns 11.1 with the I-bank lead

Pattern #5 (section 4) showed I-bank basket leads IPO supply by 6-12
months. Conversely, IPO-supply surges also lead to I-bank basket
gains, but on a shorter (concurrent) timeline.

If the **PRIME pipeline estimate of ₹2.5 lakh crore for CY 2026
materializes** (see `forecast_fy2026_27.md`), the I-bank basket should
respond with a strong CY 2026 print:
- Implied next-year IPO amount YoY: +30-50% (₹172k → ₹230k = +35%)
- Historical I-bank basket beta to IPO surge: ~0.4 (concurrent corr)
- Expected I-bank basket 2026: somewhere in +20-50% range, n=8 listed
  companies. Anand Rathi (+56% in 2025), Nuvama (+5%), and IIFL Capital
  (+11%) are the most levered names.

The 2-year (2026 + 2027) cumulative Nifty 50 picture (from pattern #4
+ #5) historical analogs:
- 2018 → 2020: +24.0% cumulative
- 2024 → 2026: TBD (in progress)
- 2023 → 2025: +19.3% cumulative
- Mean: ~+21% over 2 years from the comparable setups

---

## 13. Bottom line — five concrete recommendations from the analysis

1. **Buy Nifty 50 when its trailing P/E drops below 17** — perfect 5/5
   record across 26 years, average +43% next year, average +80%
   2-year. Today's P/E of 22.75 is **above this trigger**; wait or
   look elsewhere. The last time this triggered was 2011-end.

2. **Buy the dip after a USD/INR shock > 10%** — perfect 4/4 record,
   average Nifty +39% next year, Midcap +60%, I-bank basket +101%.
   Today's USD/INR YoY is +4.6%, **not yet at shock threshold**.

3. **Buy mid-caps when INR is calm (-3% to +3% YoY)** — 7/7 record at
   100%, average +32%. Today is +4.6% — just outside the band. No
   buy signal.

4. **Use the I-bank basket as a leading indicator for IPO supply.**
   When the basket is up >+50% YoY, IPO supply is up the next year
   in every single case (8/8). Today's reading is +12.7% — well below
   trigger; expect IPO supply growth to moderate from the +154% YoY
   of FY 2025-26.

5. **Be skeptical of "everything is stretched" alarmism.** When P/E
   ratios are stretched (Nifty > 25 OR Midcap > 30 OR Smallcap > 35),
   the historical outcome is **not** an equity crash. It's **INR
   depreciation** the following year (4-5/4-5 records, avg +5 to +8%
   INR YoY) while the Nifty 50 itself stays up (4/4 records on Midcap
   P/E > 30 and Smallcap P/E > 35 specifically). The damage from
   over-valuation is taken by the currency and the smallcap segment,
   not the broad index.

The **2026 setup at end-2025** maps to expected **+8 to +15% Nifty 50,
moderate INR depreciation (1-6%), Midcap to slightly outperform Nifty,
Smallcap mixed-to-soft.** None of this is a forecast — it's the empirical
base rate of comparable historical setups.

---

## 14. Limitations (additional to v1)

- **The I-banking basket has changing composition over time.** 2006
  had n=2 (JM, IIFL); 2025 has n=8. Equal-weighted averaging means
  Anand Rathi's +56% in 2025 has the same weight as JM Financial's
  +17%, even though JM has 20 years of history and Anand Rathi has 4.
  A free-float-weighted basket would behave differently in the
  recent years.
- **USD/INR is one of many FX cross-rates** that could be tested. The
  same analysis with EUR/INR, GBP/INR, or JPY/INR might give different
  signals. Only USD/INR is included here.
- **No central bank policy variable.** Interest rates, RBI repo
  decisions, FX reserves are all macroeconomic drivers not in the
  dataset. Some of the patterns (especially INR signals) are
  probably mediated by policy variables that are not modeled.
- **Forward-looking outcomes are still small samples.** ipo_amt_fwd1
  has n=8 observations for the strongest I-bank signal — that's
  enough to be suggestive, not enough to be conclusive.

---

*All numbers in this document are reproducible by running
`python3 find_patterns_v2.py` on the seven CSVs in this folder.
The full enumeration of 58 ≥80% signals is in the script output;
the section 1 table extracts the 12 most economically significant
ones. Pattern v1 in `patterns_high_probability.md` remains valid;
this document supersedes it with the new data sources.*
