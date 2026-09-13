# The Darvas Screen — NiftyTotalMarket

> **BACKTEST — as of 2026-03-31.** Price and volume data cover 2025-06-01 to 2026-03-31 ONLY, stored separately in `VolumeAndPricingBacktest/`. Statements are cut at fiscal year Mar 2026; note that in reality Mar 2026 annual results would not all have been published by 2026-03-31 — they are included because the backtest's rule is 'no data after Mar 2026', stated here so the optimism is visible. The conference-call read is EXCLUDED (the transcript archive contains calls after the window), so every 'new-age' verdict below is 'not assessed' by design, and the live ledger is untouched.

*Run 2026-09-13 on data fetched 2026-09-13T07:26:31+00:00 · 741 stocks scanned (741 fetched, 1 unavailable) · trigger week beginning 2026-03-30.*

**The method, in one line:** a surge in weekly volume with the price appreciating is the trigger; rising earnings power (ideally in a new-age industry) is the confirmation; the stock's own boxes give the buy point, the add point and the stop; a drop to a lower box is the exit.

## Step 1 — The volume trigger

A stock qualifies when its LATEST week — the running (partial) week when there is one, pro-rated to five days — traded at least 1.5× its average weekly volume of the prior 12 completed weeks AND the price rose. 47 of 741 qualified; every qualifier, best volume reaction first, with the last four weeks of volume shown:

| # | Stock | Vol W−3 | Vol W−2 | Vol W−1 | Vol latest wk | 12-wk avg | Multiple | Price latest wk | Close |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | KNRCON | 6,669,101 | 5,529,939 | 7,184,597 | 122,305,524* | 6,525,027 | **93.72×*** | +3.12% | ₹113.0 |
| 2 | EPL | 2,479,969 | 3,213,358 | 2,837,613 | 8,269,617* | 2,422,283 | **17.07×*** | +3.36% | ₹205.3 |
| 3 | RENUKA | 37,675,877 | 26,286,130 | 54,395,702 | 52,555,870* | 24,518,406 | **10.72×*** | +3.81% | ₹27.5 |
| 4 | IRB | 76,766,784 | 73,728,606 | 106,276,698 | 104,692,549* | 75,213,506 | **6.96×*** | +8.18% | ₹22.1 |
| 5 | JLHL | 175,665 | 448,500 | 1,383,005 | 760,735* | 607,990 | **6.26×*** | +0.13% | ₹256.2 |
| 6 | WEWORK | 834,609 | 628,211 | 1,335,001 | 872,557* | 705,353 | **6.19×*** | +1.07% | ₹455.4 |
| 7 | TRAVELFOOD | 225,329 | 994,180 | 713,836 | 347,312* | 352,611 | **4.92×*** | +6.93% | ₹1,261.8 |
| 8 | URBANCO | 13,627,695 | 203,281,844 | 40,072,618 | 30,536,917* | 34,016,450 | **4.49×*** | +3.75% | ₹118.9 |
| 9 | EIEL | 42,265,060 | 5,098,745 | 5,010,696 | 5,841,937* | 6,756,686 | **4.32×*** | +1.73% | ₹140.4 |
| 10 | SHYAMMETL | 564,470 | 1,505,261 | 1,259,292 | 747,503* | 870,611 | **4.29×*** | +0.11% | ₹771.1 |
| 11 | THERMAX | 553,295 | 1,839,711 | 430,796 | 541,315* | 657,297 | **4.12×*** | +2.00% | ₹3,260.7 |
| 12 | ARVINDFASN | 1,025,547 | 858,329 | 900,856 | 878,937* | 1,107,092 | **3.97×*** | +5.50% | ₹403.5 |
| 13 | DMART | 2,901,339 | 1,784,056 | 3,597,696 | 1,738,503* | 2,310,992 | **3.76×*** | +1.37% | ₹3,956.8 |
| 14 | WESTLIFE | 544,162 | 595,059 | 707,865 | 1,240,049* | 1,792,659 | **3.46×*** | +8.79% | ₹481.3 |
| 15 | AIAENG | 224,589 | 1,005,604 | 377,809 | 220,600* | 327,098 | **3.37×*** | +5.15% | ₹3,636.6 |
| 16 | SAIL | 75,910,084 | 103,932,792 | 88,938,438 | 70,851,364* | 108,024,123 | **3.28×*** | +3.38% | ₹151.4 |
| 17 | ABDL | 1,150,353 | 2,087,732 | 3,311,187 | 1,446,683* | 2,281,732 | **3.17×*** | +1.76% | ₹404.1 |
| 18 | DBL | 1,855,490 | 794,901 | 1,416,788 | 799,397* | 1,355,943 | **2.95×*** | +0.27% | ₹387.2 |
| 19 | GALLANTT | 924,427 | 387,967 | 660,762 | 286,774* | 512,834 | **2.80×*** | +1.09% | ₹548.6 |
| 20 | PHOENIXLTD | 2,331,857 | 3,183,873 | 2,759,214 | 1,275,726* | 2,338,431 | **2.73×*** | +0.33% | ₹1,506.3 |
| 21 | ASKAUTOLTD | 918,422 | 668,892 | 1,142,719 | 396,356* | 733,102 | **2.70×*** | +1.37% | ₹444.8 |
| 22 | CARBORUNIV | 388,143 | 410,796 | 739,366 | 406,933* | 872,313 | **2.33×*** | +1.06% | ₹775.7 |
| 23 | UTIAMC | 437,658 | 329,697 | 367,862 | 184,978* | 406,844 | **2.27×*** | +0.07% | ₹937.4 |
| 24 | AFFLE | 1,438,581 | 1,866,532 | 2,305,798 | 546,166* | 1,243,744 | **2.20×*** | +0.21% | ₹1,449.1 |
| 25 | SAMMAANCAP | 34,821,341 | 36,412,890 | 194,998,299 | 25,387,575* | 57,683,157 | **2.20×*** | +0.79% | ₹149.5 |
| 26 | AXISCADES | 634,637 | 638,922 | 883,695 | 276,517* | 634,224 | **2.18×*** | +3.75% | ₹1,514.4 |
| 27 | ONGC | 129,590,573 | 94,290,832 | 115,988,360 | 44,866,906* | 102,760,084 | **2.18×*** | +0.96% | ₹284.6 |
| 28 | GLAXO | 245,942 | 183,210 | 251,398 | 129,602* | 310,374 | **2.09×*** | +1.04% | ₹2,283.0 |
| 29 | IPCALAB | 1,208,125 | 1,390,372 | 1,286,102 | 450,008* | 1,087,744 | **2.07×*** | +0.96% | ₹1,601.2 |
| 30 | MANYAVAR | 3,385,030 | 3,981,631 | 3,398,529 | 688,201* | 1,679,194 | **2.05×*** | +0.26% | ₹351.0 |
| 31 | CHENNPETRO | 10,156,029 | 27,925,376 | 11,729,409 | 3,916,367* | 9,646,011 | **2.03×*** | +0.79% | ₹967.4 |
| 32 | HINDALCO | 31,324,752 | 34,321,976 | 23,495,726 | 12,727,309* | 31,298,829 | **2.03×*** | +2.05% | ₹884.5 |
| 33 | BAYERCROP | 109,013 | 218,196 | 100,891 | 42,184* | 104,286 | **2.02×*** | +3.09% | ₹4,645.6 |
| 34 | DCMSHRIRAM | 484,911 | 433,555 | 265,809 | 103,297* | 261,564 | **1.97×*** | +0.38% | ₹1,116.5 |
| 35 | NATIONALUM | 96,903,238 | 93,084,691 | 48,224,284 | 31,797,909* | 80,640,944 | **1.97×*** | +4.07% | ₹386.1 |
| 36 | COALINDIA | 84,205,755 | 65,115,861 | 56,299,421 | 19,114,688* | 50,305,496 | **1.90×*** | +1.21% | ₹450.4 |
| 37 | CCAVENUE | 55,625,882 | 43,051,885 | 35,728,388 | 17,161,041* | 46,577,898 | **1.84×*** | +1.90% | ₹13.4 |
| 38 | RHIM | 1,720,138 | 886,590 | 1,021,220 | 451,293* | 1,225,880 | **1.84×*** | +1.12% | ₹337.9 |
| 39 | ATUL | 173,083 | 93,717 | 242,365 | 44,569* | 124,838 | **1.79×*** | +2.06% | ₹6,368.5 |
| 40 | CHAMBLFERT | 5,682,486 | 4,375,913 | 3,373,975 | 1,421,758* | 4,148,486 | **1.71×*** | +1.61% | ₹426.7 |
| 41 | RAMCOCEM | 1,196,581 | 980,961 | 1,554,471 | 428,482* | 1,283,024 | **1.67×*** | +1.05% | ₹920.1 |
| 42 | GAIL | 92,515,736 | 65,947,910 | 75,071,548 | 21,810,845* | 65,713,645 | **1.66×*** | +0.38% | ₹137.7 |
| 43 | BIKAJI | 667,410 | 650,527 | 667,770 | 259,743* | 790,203 | **1.64×*** | +0.80% | ₹622.0 |
| 44 | ZFCVINDIA | 361,740 | 470,352 | 440,898 | 139,548* | 428,876 | **1.63×*** | +0.66% | ₹2,294.7 |
| 45 | GAEL | 2,553,526 | 3,693,686 | 2,208,657 | 1,339,219* | 4,210,272 | **1.59×*** | +1.39% | ₹135.9 |
| 46 | VEDL | 66,559,293 | 71,759,889 | 66,438,998 | 24,457,507* | 77,258,258 | **1.58×*** | +0.83% | ₹654.8 |
| 47 | VOLTAMP | 189,312 | 111,307 | 103,319 | 54,894* | 173,420 | **1.58×*** | +2.92% | ₹8,685.5 |

\* the latest week is still running — its multiple is pro-rated to a full five-day week (volume ÷ (average × days traded ÷ 5)); the raw volume shown is what has actually traded so far.

The top 25 go on to the earnings and box steps below.

## The recommendations

| Stock | Action | Box (₹) | Own box height | Stop loss | Volume trend | Earnings power | New-age |
|---|---|---|---:|---:|---|---|---|
| KNRCON | **SELL** | 116.9–148.0 | 26.6% | exit | SPIKE ONLY | FALLING | not assessed |
| EPL | **WATCH** | 176.4–205.8 | 16.6% | ₹167.59 | SPIKE ONLY | RISING | not assessed |
| RENUKA | **WATCH** | 23.0–26.0 | 13.0% | ₹22.11 | SPIKE ONLY | FALLING | not assessed |
| IRB | **WATCH** | 19.8–22.5 | 13.3% | ₹19.03 | SPIKE ONLY | FALLING | not assessed |
| JLHL | **WATCH** | 239.8–279.3 | 16.5% | ₹227.90 | SPIKE ONLY | FALLING | not assessed |
| WEWORK | **WATCH** | 421.0–552.8 | 31.3% | ₹381.46 | SPIKE ONLY | FALLING | not assessed |
| TRAVELFOOD | **BUY** | 1,089.0–1,138.0 | 4.5% | ₹1,074.30 | SPIKE ONLY | RISING | not assessed |
| URBANCO | **WATCH** | 109.2–131.4 | 20.3% | ₹102.57 | SPIKE ONLY | FALLING | not assessed |
| EIEL | **WATCH** | 134.7–163.5 | 21.4% | ₹126.07 | SPIKE ONLY | FLAT | not assessed |
| SHYAMMETL | **WATCH** | 752.1–821.0 | 9.2% | ₹731.42 | SPIKE ONLY | RISING | not assessed |
| THERMAX | **ACCUMULATE** | 3,050.0–3,347.2 | 9.7% | ₹2,960.84 | SPIKE ONLY | RISING | not assessed |
| ARVINDFASN | **WATCH** | 370.5–470.5 | 27.0% | ₹340.50 | SPIKE ONLY | RISING | not assessed |
| DMART | **SELL** | 3,736.1–4,056.0 | 8.6% | exit | SPIKE ONLY | RISING | not assessed |
| WESTLIFE | **WATCH** | forming | — | — | STEPPED UP | FLAT | not assessed |
| AIAENG | **SELL** | 3,545.0–3,974.6 | 12.1% | exit | SPIKE ONLY | RISING | not assessed |
| SAIL | **WATCH** | 142.3–158.5 | 11.4% | ₹137.38 | SPIKE ONLY | RISING | not assessed |
| ABDL | **WATCH** | 382.1–432.6 | 13.2% | ₹366.97 | SPIKE ONLY | RISING | not assessed |
| DBL | **SELL** | 422.5–472.4 | 11.8% | exit | SPIKE ONLY | FALLING | not assessed |
| GALLANTT | **WATCH** | 515.1–674.8 | 31.0% | ₹467.21 | SPIKE ONLY | FLAT | not assessed |
| PHOENIXLTD | **ACCUMULATE** | 1,465.6–1,633.9 | 11.5% | ₹1,415.11 | SPIKE ONLY | RISING | not assessed |
| ASKAUTOLTD | **BUY** | 392.3–424.7 | 8.3% | ₹382.58 | SPIKE ONLY | RISING | not assessed |
| CARBORUNIV | **SELL** | 780.0–855.5 | 9.7% | exit | BUILDING (2 mo) | FALLING | not assessed |
| UTIAMC | **SELL** | 927.2–1,107.5 | 19.4% | exit | SPIKE ONLY | FALLING | not assessed |
| AFFLE | **BUY** | 1,251.3–1,360.0 | 8.7% | ₹1,218.69 | SPIKE ONLY | RISING | not assessed |
| SAMMAANCAP | **SELL** | 137.2–162.0 | 18.1% | exit | SPIKE ONLY | FALLING | not assessed |

## KNRCON — SELL

**Why:** closed below its box bottom — Darvas's red flag; a stock dropping to a lower box is sold, not averaged.

**The trigger numbers:** 122,305,524 shares traded in the week of 2026-03-30 against a 12-week average of 6,525,027 in 1 trading day of a week still running — 18.74× the weekly average already, 93.72× pro-rated to five days (multifold), with the price +3.12% on the week.

### Price and volume together, week by week

```
         │ 
    ₹152 │           ●  ●
         │  ●  ●    ╱      ●
         │        ●           ●
         │                       ●
         │                          ●  ●
         │                                ●
    ₹110 │                                   ●  ●
         │ 
         ┼───────────────────────────────────────
12.23 Cr │                                      █
         │                                      █
         │                                      █
         │                                      █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 12.23 Cr, close ₹113.0
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 55,271,595 |  |  |
| 2025-07 | 21,588,638 | ▼ -61% |  |
| 2025-08 | 10,593,423 | ▼ -51% |  |
| 2025-09 | 100,646,771 | ▲ +850% |  |
| 2025-10 | 17,252,202 | ▼ -83% |  |
| 2025-11 | 19,715,985 | ▲ +14% |  |
| 2025-12 | 63,495,946 | ▲ +222% |  |
| 2026-01 | 20,920,601 | ▼ -67% |  |
| 2026-02 | 34,176,897 | ▲ +63% |  |
| 2026-03 | 146,749,046 | ▲ +329% | partial — 19 days |

### The boxes

```
┌ ₹   148.00 ─ top    (2026-02-17)
│   box height 26.6%
└ ₹   116.91 ─ bottom (2026-03-09)  broke DOWN — red flag
┌ ₹   161.00 ─ top    (2026-02-03)
│   box height 12.3%
└ ₹   143.31 ─ bottom (2026-02-06)  broke DOWN — red flag
┌ ₹   186.00 ─ top    (2025-12-26)
│   box height 33.1%
└ ₹   139.76 ─ bottom (2026-01-12)  broke DOWN — red flag
┌ ₹   167.33 ─ top    (2025-12-01)
│   box height 16.7%
└ ₹   143.40 ─ bottom (2025-12-09)  broke DOWN — red flag
┌ ₹   174.60 ─ top    (2025-11-17)
│   box height 8.1%
└ ₹   161.45 ─ bottom (2025-11-24)  broke DOWN — red flag
┌ ₹   184.29 ─ top    (2025-11-03)
│   box height 5.2%
└ ₹   175.20 ─ bottom (2025-11-06)  broke DOWN — red flag
┌ ₹   204.95 ─ top    (2025-09-29)
│   box height 11.9%
└ ₹   183.20 ─ bottom (2025-10-16)  broke DOWN — red flag
┌ ₹   220.00 ─ top    (2025-09-17)
│   box height 8.3%
└ ₹   203.10 ─ bottom (2025-09-19)  broke DOWN — red flag
┌ ₹   202.10 ─ top    (2025-09-04)
│   box height 4.5%
└ ₹   193.40 ─ bottom (2025-09-15)  broke UP
┌ ₹   211.10 ─ top    (2025-08-11)
│   box height 6.9%
└ ₹   197.55 ─ bottom (2025-08-18)  broke DOWN — red flag
┌ ₹   228.00 ─ top    (2025-07-22)
│   box height 9.1%
└ ₹   209.00 ─ bottom (2025-07-31)  broke DOWN — red flag
┌ ₹   245.00 ─ top    (2025-06-26)
│   box height 12.9%
└ ₹   217.02 ─ bottom (2025-07-03)  broke DOWN — red flag
┌ ₹   225.00 ─ top    (2025-06-11)
│   box height 7.9%
└ ₹   208.61 ─ bottom (2025-06-13)  broke DOWN — red flag
┌ ₹   214.80 ─ top    (2025-06-03)
│   box height 4.0%
└ ₹   206.51 ─ bottom (2025-06-04)  broke UP
  ✂ ₹   107.58 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **26.6%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA -55.8%, PAT -56.4%, EBITDA-margin change -8.0pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 918.0 | 1,049.0 | 1,610.0 | 711.0 |
| EBITDA margin % | 23.0 | 24.0 | 34.0 | 26.0 |
| PAT | 439.0 | 752.0 | 1,002.0 | 437.0 |
| PAT margin % | 10.8 | 17.0 | 21.1 | 16.2 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## EPL — WATCH

**Why:** moving inside its box on trigger volume — the entry is a close above the box top.

**The trigger numbers:** 8,269,617 shares traded in the week of 2026-03-30 against a 12-week average of 2,422,283 in 1 trading day of a week still running — 3.41× the weekly average already, 17.07× pro-rated to five days (multifold), with the price +3.36% on the week.

### Price and volume together, week by week

```
         │ 
    ₹218 │              ●  ●     ●
         │  ●          ╱      ●    ╲
         │     ●       ╱           ╲            ●
         │        ●    ╱            ●        ●
         │          ╲  ╱              ╲     ╱
         │           ●                ╲   ●
    ₹184 │                             ●
         │ 
         ┼───────────────────────────────────────
 82.70 L │                                      █
         │                                      █
         │                    █           █     █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 82.70 L, close ₹205.3
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 14,229,385 |  |  |
| 2025-07 | 9,432,925 | ▼ -34% |  |
| 2025-08 | 14,589,965 | ▲ +55% |  |
| 2025-09 | 12,594,638 | ▼ -14% |  |
| 2025-10 | 7,377,219 | ▼ -41% |  |
| 2025-11 | 16,244,843 | ▲ +120% |  |
| 2025-12 | 16,941,300 | ▬ +4% |  |
| 2026-01 | 10,042,407 | ▼ -41% |  |
| 2026-02 | 9,354,213 | ▼ -7% |  |
| 2026-03 | 19,191,051 | ▲ +105% | partial — 19 days |

### The boxes

```
┌ ₹   205.77 ─ top    (2026-03-05)
│   box height 16.6%   close ₹205.27 inside
└ ₹   176.40 ─ bottom (2026-03-16)  ◀ current box
┌ ₹   224.02 ─ top    (2026-02-10)
│   box height 8.5%
└ ₹   206.52 ─ bottom (2026-02-16)  broke DOWN — red flag
┌ ₹   202.49 ─ top    (2026-01-27)
│   box height 7.6%
└ ₹   188.20 ─ bottom (2026-02-02)  broke UP
┌ ₹   210.50 ─ top    (2026-01-09)
│   box height 3.2%
└ ₹   204.01 ─ bottom (2026-01-13)  broke DOWN — red flag
┌ ₹   222.15 ─ top    (2025-12-16)
│   box height 6.9%
└ ₹   207.75 ─ bottom (2025-12-19)  broke DOWN — red flag
┌ ₹   211.27 ─ top    (2025-10-23)
│   box height 11.8%
└ ₹   189.00 ─ bottom (2025-11-11)  broke UP
┌ ₹   218.80 ─ top    (2025-10-08)
│   box height 6.2%
└ ₹   205.93 ─ bottom (2025-10-13)  broke DOWN — red flag
┌ ₹   216.60 ─ top    (2025-09-23)
│   box height 5.9%
└ ₹   204.48 ─ bottom (2025-09-29)  broke UP
┌ ₹   241.90 ─ top    (2025-08-25)
│   box height 11.0%
└ ₹   218.00 ─ bottom (2025-09-02)  broke DOWN — red flag
┌ ₹   237.90 ─ top    (2025-08-06)
│   box height 8.1%
└ ₹   220.02 ─ bottom (2025-08-07)  broke UP
┌ ₹   251.00 ─ top    (2025-07-01)
│   box height 10.0%
└ ₹   228.16 ─ bottom (2025-07-09)  broke DOWN — red flag
┌ ₹   254.00 ─ top    (2025-06-03)
│   box height 8.7%
└ ₹   233.72 ─ bottom (2025-06-04)  broke DOWN — red flag
  ✂ ₹   167.59 ─ stop loss (bottom − 0.3 × box height)
  ▲ ₹   205.77 ─ buy on a close above the box top
```

This stock's own box height is **16.6%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +15.3% and PAT +8.2% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 575.0 | 715.0 | 837.0 | 965.0 |
| EBITDA margin % | 16.0 | 18.0 | 20.0 | 20.0 |
| PAT | 231.0 | 210.0 | 364.0 | 394.0 |
| PAT margin % | 6.3 | 5.4 | 8.6 | 8.3 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## RENUKA — WATCH

**Why:** closed above its box top on trigger volume — reaching for the higher box; buy the break; DOWNGRADED to WATCH — the latest statements show falling earnings power, and Darvas required rising earnings under the volume.

**The trigger numbers:** 52,555,870 shares traded in the week of 2026-03-30 against a 12-week average of 24,518,406 in 1 trading day of a week still running — 2.14× the weekly average already, 10.72× pro-rated to five days (multifold), with the price +3.81% on the week.

### Price and volume together, week by week

```
         │ 
     ₹28 │                                      ●
         │                                   ●
         │                                  ╱
         │  ●  ●     ●                      ╱
         │       ╲  ╱   ●        ●        ●
         │       ╲  ╱      ●  ●     ●  ●
     ₹23 │        ●
         │ 
         ┼───────────────────────────────────────
 6.56 Cr │                          █
         │                          █        █  █
         │                          █  █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 5.26 Cr, close ₹27.5
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 113,183,040 |  |  |
| 2025-07 | 67,126,379 | ▼ -41% |  |
| 2025-08 | 41,070,136 | ▼ -39% |  |
| 2025-09 | 306,414,440 | ▲ +646% |  |
| 2025-10 | 59,185,568 | ▼ -81% |  |
| 2025-11 | 46,901,350 | ▼ -21% |  |
| 2025-12 | 73,117,499 | ▲ +56% |  |
| 2026-01 | 53,390,426 | ▼ -27% |  |
| 2026-02 | 60,823,225 | ▲ +14% |  |
| 2026-03 | 236,502,169 | ▲ +289% | partial — 19 days |

### The boxes

```
┌ ₹    26.00 ─ top    (2026-02-10)
│   box height 13.0%
└ ₹    23.01 ─ bottom (2026-02-24)  broke UP
┌ ₹    24.51 ─ top    (2026-01-20)
│   box height 7.3%
└ ₹    22.85 ─ bottom (2026-01-21)  broke UP
┌ ₹    28.16 ─ top    (2025-11-24)
│   box height 12.6%
└ ₹    25.02 ─ bottom (2025-12-09)  broke DOWN — red flag
┌ ₹    29.90 ─ top    (2025-11-10)
│   box height 6.7%
└ ₹    28.02 ─ bottom (2025-11-11)  broke DOWN — red flag
┌ ₹    30.32 ─ top    (2025-10-23)
│   box height 5.6%
└ ₹    28.70 ─ bottom (2025-10-28)  broke DOWN — red flag
┌ ₹    31.77 ─ top    (2025-09-29)
│   box height 7.7%
└ ₹    29.51 ─ bottom (2025-09-30)  broke DOWN — red flag
┌ ₹    33.50 ─ top    (2025-09-02)
│   box height 8.2%
└ ₹    30.95 ─ bottom (2025-09-05)  broke DOWN — red flag
┌ ₹    31.05 ─ top    (2025-07-30)
│   box height 11.1%
└ ₹    27.95 ─ bottom (2025-08-13)  broke UP
┌ ₹    35.85 ─ top    (2025-06-11)
│   box height 16.2%
└ ₹    30.85 ─ bottom (2025-06-23)  broke DOWN — red flag
  ✂ ₹    22.11 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **13.0%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA -96.9%, PAT -164.0%, EBITDA-margin change -5.8pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 590.0 | 685.0 | 609.0 | 19.0 |
| EBITDA margin % | 7.0 | 6.0 | 6.0 | 0.2 |
| PAT | -197.0 | -627.0 | -300.0 | -792.0 |
| PAT margin % | -2.2 | -5.5 | -2.8 | -8.6 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## IRB — WATCH

**Why:** sealed a higher box after an upward break and is holding it — add while it stabilises in the higher box; DOWNGRADED to WATCH — the latest statements show falling earnings power, and Darvas required rising earnings under the volume.

**The trigger numbers:** 104,692,549 shares traded in the week of 2026-03-30 against a 12-week average of 75,213,506 in 1 trading day of a week still running — 1.39× the weekly average already, 6.96× pro-rated to five days (multifold), with the price +8.18% on the week.

### Price and volume together, week by week

```
         │ 
     ₹22 │                 ●                    ●
         │              ●    ╲                 ╱
         │             ╱     ╲                 ╱
         │             ╱     ╲   ●             ╱
         │  ●  ●     ●       ╲  ╱  ╲   ●  ●    ╱
         │       ╲  ╱         ●     ●        ●
     ₹20 │        ●
         │ 
         ┼───────────────────────────────────────
10.63 Cr │                                   █  █
         │  █     █     █  █           █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 10.47 Cr, close ₹22.1
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 717,451,862 |  |  |
| 2025-07 | 386,760,612 | ▼ -46% |  |
| 2025-08 | 424,489,932 | ▲ +10% |  |
| 2025-09 | 345,326,616 | ▼ -19% |  |
| 2025-10 | 345,791,898 | ▬ +0% |  |
| 2025-11 | 504,378,636 | ▲ +46% |  |
| 2025-12 | 281,341,692 | ▼ -44% |  |
| 2026-01 | 301,249,766 | ▲ +7% |  |
| 2026-02 | 299,837,228 | ▬ -0% |  |
| 2026-03 | 423,982,683 | ▲ +41% | partial — 19 days |

### The boxes

```
┌ ₹    22.46 ─ top    (2026-02-10)
│   box height 13.3%   close ₹22.14 inside
└ ₹    19.82 ─ bottom (2026-02-24)  ◀ current box
┌ ₹    20.96 ─ top    (2026-01-14)
│   box height 8.7%
└ ₹    19.29 ─ bottom (2026-01-21)  broke UP
┌ ₹    21.55 ─ top    (2025-12-24)
│   box height 4.7%
└ ₹    20.58 ─ bottom (2025-12-30)  broke DOWN — red flag
┌ ₹    21.67 ─ top    (2025-12-10)
│   box height 5.7%
└ ₹    20.50 ─ bottom (2025-12-12)  broke DOWN — red flag
┌ ₹    22.98 ─ top    (2025-11-17)
│   box height 8.1%
└ ₹    21.26 ─ bottom (2025-11-24)  broke DOWN — red flag
┌ ₹    22.75 ─ top    (2025-10-27)
│   box height 3.6%
└ ₹    21.95 ─ bottom (2025-10-29)  broke DOWN — red flag
┌ ₹    22.25 ─ top    (2025-09-17)
│   box height 9.8%
└ ₹    20.25 ─ bottom (2025-09-26)  broke UP
┌ ₹    21.93 ─ top    (2025-09-02)
│   box height 4.2%
└ ₹    21.05 ─ bottom (2025-09-05)  broke UP
┌ ₹    24.50 ─ top    (2025-07-16)
│   box height 13.3%
└ ₹    21.62 ─ bottom (2025-08-11)  broke DOWN — red flag
┌ ₹    27.14 ─ top    (2025-06-10)
│   box height 13.6%
└ ₹    23.90 ─ bottom (2025-06-19)  broke DOWN — red flag
┌ ₹    26.12 ─ top    (2025-06-02)
│   box height 3.8%
└ ₹    25.16 ─ bottom (2025-06-06)  broke UP
  ✂ ₹    19.03 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **13.3%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA 14.7%, PAT -86.9%, EBITDA-margin change 6.0pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 3,130.0 | 3,022.0 | 3,472.0 | 3,982.0 |
| EBITDA margin % | 49.0 | 41.0 | 46.0 | 52.0 |
| PAT | 720.0 | 606.0 | 6,481.0 | 850.0 |
| PAT margin % | 11.2 | 8.2 | 85.1 | 11.1 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## JLHL — WATCH

**Why:** moving inside its box on trigger volume — the entry is a close above the box top.

**The trigger numbers:** 760,735 shares traded in the week of 2026-03-30 against a 12-week average of 607,990 in 1 trading day of a week still running — 1.25× the weekly average already, 6.26× pro-rated to five days (multifold), with the price +0.13% on the week.

### Price and volume together, week by week

```
         │ 
    ₹270 │     ●     ●
         │  ●     ●    ╲
         │             ╲
         │             ╲                     ●  ●
         │              ●        ●  ●     ●
         │                 ●    ╱      ●
    ₹242 │                    ●
         │ 
         ┼───────────────────────────────────────
 15.78 L │              █                    █
         │              █                    █
         │              █                    █  █
         │  █  █  █  █  █  █  █  █  █     █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 7.61 L, close ₹256.2
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 4,897,950 |  |  |
| 2025-07 | 4,463,425 | ▼ -9% |  |
| 2025-08 | 5,463,325 | ▲ +22% |  |
| 2025-09 | 3,823,015 | ▼ -30% |  |
| 2025-10 | 3,234,930 | ▼ -15% |  |
| 2025-11 | 15,916,365 | ▲ +392% |  |
| 2025-12 | 3,117,115 | ▼ -80% |  |
| 2026-01 | 2,208,340 | ▼ -29% |  |
| 2026-02 | 2,800,315 | ▲ +27% |  |
| 2026-03 | 3,188,410 | ▲ +14% | partial — 19 days |

### The boxes

```
┌ ₹   279.30 ─ top    (2026-01-30)
│   box height 16.5%   close ₹256.24 inside
└ ₹   239.76 ─ bottom (2026-02-05)  ◀ current box
┌ ₹   279.80 ─ top    (2026-01-13)
│   box height 6.0%
└ ₹   264.00 ─ bottom (2026-01-14)  broke DOWN — red flag
┌ ₹   288.58 ─ top    (2025-12-16)
│   box height 6.3%
└ ₹   271.40 ─ bottom (2025-12-18)  broke DOWN — red flag
┌ ₹   325.00 ─ top    (2025-10-30)
│   box height 15.7%
└ ₹   281.00 ─ bottom (2025-11-24)  broke DOWN — red flag
┌ ₹   317.40 ─ top    (2025-10-21)
│   box height 7.6%
└ ₹   294.90 ─ bottom (2025-10-23)  broke UP
┌ ₹   310.00 ─ top    (2025-09-30)
│   box height 5.2%
└ ₹   294.62 ─ bottom (2025-10-06)  broke UP
┌ ₹   301.56 ─ top    (2025-09-10)
│   box height 5.8%
└ ₹   285.04 ─ bottom (2025-09-12)  broke UP
┌ ₹   292.38 ─ top    (2025-08-14)
│   box height 5.4%
└ ₹   277.46 ─ bottom (2025-08-21)  broke UP
┌ ₹   311.38 ─ top    (2025-06-11)
│   box height 11.2%
└ ₹   280.00 ─ bottom (2025-06-24)  broke DOWN — red flag
  ✂ ₹   227.90 ─ stop loss (bottom − 0.3 × box height)
  ▲ ₹   279.30 ─ buy on a close above the box top
```

This stock's own box height is **16.5%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA 13.2%, PAT 0.0%, EBITDA-margin change 0.0pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 201.0 | 242.0 | 303.0 | 343.0 |
| EBITDA margin % | 23.0 | 23.0 | 23.0 | 23.0 |
| PAT | 73.0 | 177.0 | 194.0 | 194.0 |
| PAT margin % | 8.2 | 16.5 | 14.9 | 12.9 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## WEWORK — WATCH

**Why:** moving inside its box on trigger volume — the entry is a close above the box top.

**The trigger numbers:** 872,557 shares traded in the week of 2026-03-30 against a 12-week average of 705,353 in 1 trading day of a week still running — 1.24× the weekly average already, 6.19× pro-rated to five days (multifold), with the price +1.07% on the week.

### Price and volume together, week by week

```
         │ 
    ₹615 │  ●  ●
         │        ●  ●  ●
         │                 ●
         │                    ●
         │                      ╲
         │                       ●
    ₹450 │                          ●  ●  ●  ●  ●
         │ 
         ┼───────────────────────────────────────
 15.14 L │  █                                █
         │  █        █                       █
         │  █        █                 █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 8.73 L, close ₹455.4
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-10 | 15,485,461 |  |  |
| 2025-11 | 6,945,134 | ▼ -55% |  |
| 2025-12 | 2,309,818 | ▼ -67% |  |
| 2026-01 | 3,914,059 | ▲ +69% |  |
| 2026-02 | 1,536,748 | ▼ -61% |  |
| 2026-03 | 4,073,845 | ▲ +165% | partial — 19 days |

### The boxes

```
┌ ₹   552.80 ─ top    (2026-02-19)
│   box height 31.3%   close ₹455.35 inside
└ ₹   421.00 ─ bottom (2026-03-09)  ◀ current box
┌ ₹   595.80 ─ top    (2026-01-22)
│   box height 7.2%
└ ₹   555.60 ─ bottom (2026-01-27)  broke DOWN — red flag
┌ ₹   624.95 ─ top    (2026-01-02)
│   box height 5.5%
└ ₹   592.40 ─ bottom (2026-01-06)  broke DOWN — red flag
┌ ₹   615.00 ─ top    (2025-12-09)
│   box height 7.9%
└ ₹   570.10 ─ bottom (2025-12-17)  broke UP
┌ ₹   608.95 ─ top    (2025-11-26)
│   box height 5.4%
└ ₹   577.70 ─ bottom (2025-12-02)  broke UP
┌ ₹   650.15 ─ top    (2025-10-10)
│   box height 8.2%
└ ₹   601.10 ─ bottom (2025-10-14)  broke DOWN — red flag
  ✂ ₹   381.46 ─ stop loss (bottom − 0.3 × box height)
  ▲ ₹   552.80 ─ buy on a close above the box top
```

This stock's own box height is **31.3%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA 27.0%, PAT -41.4%, EBITDA-margin change 0.0pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 796.0 | 1,047.0 | 1,239.0 | 1,574.0 |
| EBITDA margin % | 61.0 | 63.0 | 64.0 | 64.0 |
| PAT | -147.0 | -136.0 | 128.0 | 75.0 |
| PAT margin % | -11.2 | -8.2 | 6.6 | 3.1 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## TRAVELFOOD — BUY

**Why:** closed above its box top on trigger volume — reaching for the higher box; buy the break.

**The trigger numbers:** 347,312 shares traded in the week of 2026-03-30 against a 12-week average of 352,611 in 1 trading day of a week still running — 0.98× the weekly average already, 4.92× pro-rated to five days (multifold), with the price +6.93% on the week.

### Price and volume together, week by week

```
         │ 
  ₹1,262 │                                      ●
         │                    ●  ●             ╱
         │                   ╱      ●        ●
         │  ●              ●           ●    ╱
         │     ●          ╱              ╲  ╱
         │       ╲      ●                 ●
  ₹1,065 │        ●  ●
         │ 
         ┼───────────────────────────────────────
  9.94 L │                                █
         │                                █  █
         │  █     █                       █  █
         │  █  █  █        █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 3.47 L, close ₹1,261.8
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-07 | 17,559,568 |  |  |
| 2025-08 | 7,364,745 | ▼ -58% |  |
| 2025-09 | 4,366,953 | ▼ -41% |  |
| 2025-10 | 2,171,916 | ▼ -50% |  |
| 2025-11 | 2,032,439 | ▼ -6% |  |
| 2025-12 | 1,500,698 | ▼ -26% |  |
| 2026-01 | 1,482,941 | ▬ -1% |  |
| 2026-02 | 874,166 | ▼ -41% |  |
| 2026-03 | 2,499,717 | ▲ +186% | partial — 19 days |

### The boxes

```
┌ ₹ 1,138.00 ─ top    (2026-03-18)
│   box height 4.5%
└ ₹ 1,089.00 ─ bottom (2026-03-24)  broke UP
┌ ₹ 1,249.00 ─ top    (2026-02-13)
│   box height 8.3%
└ ₹ 1,153.50 ─ bottom (2026-02-16)  broke DOWN — red flag
┌ ₹ 1,110.00 ─ top    (2026-01-22)
│   box height 7.2%
└ ₹ 1,035.30 ─ bottom (2026-01-27)  broke UP
┌ ₹ 1,212.90 ─ top    (2025-12-26)
│   box height 6.9%
└ ₹ 1,134.50 ─ bottom (2025-12-30)  broke DOWN — red flag
┌ ₹ 1,445.00 ─ top    (2025-11-27)
│   box height 19.2%
└ ₹ 1,212.50 ─ bottom (2025-12-08)  broke DOWN — red flag
┌ ₹ 1,334.00 ─ top    (2025-10-31)
│   box height 6.7%
└ ₹ 1,250.50 ─ bottom (2025-11-07)  broke UP
┌ ₹ 1,394.80 ─ top    (2025-09-22)
│   box height 6.4%
└ ₹ 1,310.50 ─ bottom (2025-09-23)  broke DOWN — red flag
┌ ₹ 1,340.10 ─ top    (2025-09-04)
│   box height 9.6%
└ ₹ 1,222.40 ─ bottom (2025-09-16)  broke UP
┌ ₹ 1,264.00 ─ top    (2025-08-21)
│   box height 6.1%
└ ₹ 1,191.00 ─ bottom (2025-08-28)  broke UP
┌ ₹ 1,187.80 ─ top    (2025-07-22)
│   box height 17.8%
└ ₹ 1,008.50 ─ bottom (2025-08-04)  broke UP
┌ ₹ 1,130.00 ─ top    (2025-07-14)
│   box height 8.8%
└ ₹ 1,038.10 ─ bottom (2025-07-16)  broke UP
  ✂ ₹ 1,074.30 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **4.5%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +17.1% and PAT +18.9% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 374.0 | 417.0 | 554.0 | 649.0 |
| EBITDA margin % | 35.0 | 30.0 | 33.0 | 39.0 |
| PAT | 251.0 | 298.0 | 380.0 | 452.0 |
| PAT margin % | 23.5 | 21.3 | 22.5 | 27.4 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## URBANCO — WATCH

**Why:** sealed a higher box after an upward break and is holding it — add while it stabilises in the higher box; DOWNGRADED to WATCH — the latest statements show falling earnings power, and Darvas required rising earnings under the volume.

**The trigger numbers:** 30,536,917 shares traded in the week of 2026-03-30 against a 12-week average of 34,016,450 in 1 trading day of a week still running — 0.90× the weekly average already, 4.49× pro-rated to five days (multifold), with the price +3.75% on the week.

### Price and volume together, week by week

```
         │ 
    ₹136 │  ●
         │     ●
         │        ●  ●
         │              ●  ●                    ●
         │                    ●              ●
         │                      ╲         ●
    ₹106 │                       ●  ●  ●
         │ 
         ┼───────────────────────────────────────
20.33 Cr │                                █
         │                                █
         │                                █
         │  █                    █        █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 3.05 Cr, close ₹118.9
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-09 | 654,230,988 |  |  |
| 2025-10 | 173,493,981 | ▼ -73% |  |
| 2025-11 | 114,347,464 | ▼ -34% |  |
| 2025-12 | 128,885,635 | ▲ +13% |  |
| 2026-01 | 78,226,229 | ▼ -39% |  |
| 2026-02 | 59,281,999 | ▼ -24% |  |
| 2026-03 | 305,731,270 | ▲ +416% | partial — 19 days |

### The boxes

```
┌ ₹   131.44 ─ top    (2026-03-18)
│   box height 20.3%   close ₹118.86 inside
└ ₹   109.23 ─ bottom (2026-03-23)  ◀ current box
┌ ₹   115.70 ─ top    (2026-03-12)
│   box height 7.9%
└ ₹   107.22 ─ bottom (2026-03-17)  broke UP
┌ ₹   112.90 ─ top    (2026-02-24)
│   box height 12.1%
└ ₹   100.70 ─ bottom (2026-03-04)  broke UP
┌ ₹   132.44 ─ top    (2026-01-19)
│   box height 13.6%
└ ₹   116.58 ─ bottom (2026-01-27)  broke DOWN — red flag
┌ ₹   139.51 ─ top    (2026-01-05)
│   box height 5.7%
└ ₹   132.00 ─ bottom (2026-01-08)  broke DOWN — red flag
┌ ₹   129.94 ─ top    (2025-12-17)
│   box height 6.7%
└ ₹   121.75 ─ bottom (2025-12-18)  broke UP
┌ ₹   142.70 ─ top    (2025-11-26)
│   box height 13.9%
└ ₹   125.23 ─ bottom (2025-12-08)  broke DOWN — red flag
┌ ₹   148.44 ─ top    (2025-11-11)
│   box height 7.0%
└ ₹   138.71 ─ bottom (2025-11-14)  broke DOWN — red flag
┌ ₹   167.85 ─ top    (2025-10-15)
│   box height 15.6%
└ ₹   145.17 ─ bottom (2025-10-24)  broke DOWN — red flag
┌ ₹   201.18 ─ top    (2025-09-22)
│   box height 23.8%
└ ₹   162.50 ─ bottom (2025-09-30)  broke DOWN — red flag
  ✂ ₹   102.57 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **20.3%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA -535.0%, PAT -197.9%, EBITDA-margin change -12.5pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | -364.0 | -146.0 | -40.0 | -254.0 |
| EBITDA margin % | -57.0 | -18.0 | -3.5 | -16.0 |
| PAT | -312.0 | -93.0 | 240.0 | -235.0 |
| PAT margin % | -49.0 | -11.2 | 21.0 | -15.1 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## EIEL — WATCH

**Why:** moving inside its box on trigger volume — the entry is a close above the box top.

**The trigger numbers:** 5,841,937 shares traded in the week of 2026-03-30 against a 12-week average of 6,756,686 in 1 trading day of a week still running — 0.86× the weekly average already, 4.32× pro-rated to five days (multifold), with the price +1.73% on the week.

### Price and volume together, week by week

```
         │ 
    ₹189 │  ●  ●
         │       ╲   ●  ●
         │        ●       ╲
         │                 ●  ●
         │                       ●
         │                         ╲   ●  ●
    ₹138 │                          ●        ●  ●
         │ 
         ┼───────────────────────────────────────
 4.23 Cr │                             █
         │                             █
         │                             █
         │                 █           █        █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 58.42 L, close ₹140.4
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 123,846,880 |  |  |
| 2025-07 | 254,348,343 | ▲ +105% |  |
| 2025-08 | 51,200,015 | ▼ -80% |  |
| 2025-09 | 37,568,581 | ▼ -27% |  |
| 2025-10 | 17,225,785 | ▼ -54% |  |
| 2025-11 | 14,599,064 | ▼ -15% |  |
| 2025-12 | 11,470,745 | ▼ -21% |  |
| 2026-01 | 11,346,917 | ▬ -1% |  |
| 2026-02 | 14,782,285 | ▲ +30% |  |
| 2026-03 | 61,495,872 | ▲ +316% | partial — 19 days |

### The boxes

```
┌ ₹   163.50 ─ top    (2026-02-26)
│   box height 21.4%   close ₹140.39 inside
└ ₹   134.71 ─ bottom (2026-03-09)  ◀ current box
┌ ₹   194.58 ─ top    (2026-02-09)
│   box height 22.4%
└ ₹   159.00 ─ bottom (2026-02-16)  broke DOWN — red flag
┌ ₹   194.46 ─ top    (2026-01-09)
│   box height 7.4%
└ ₹   181.11 ─ bottom (2026-01-12)  broke DOWN — red flag
┌ ₹   207.97 ─ top    (2025-12-15)
│   box height 6.2%
└ ₹   195.78 ─ bottom (2025-12-18)  broke DOWN — red flag
┌ ₹   205.00 ─ top    (2025-12-08)
│   box height 7.3%
└ ₹   191.12 ─ bottom (2025-12-09)  broke UP
┌ ₹   223.90 ─ top    (2025-11-19)
│   box height 7.9%
└ ₹   207.50 ─ bottom (2025-11-24)  broke DOWN — red flag
┌ ₹   257.66 ─ top    (2025-10-30)
│   box height 14.5%
└ ₹   225.05 ─ bottom (2025-11-11)  broke DOWN — red flag
┌ ₹   276.10 ─ top    (2025-09-22)
│   box height 14.6%
└ ₹   241.00 ─ bottom (2025-09-30)  broke DOWN — red flag
┌ ₹   271.33 ─ top    (2025-07-28)
│   box height 16.3%
└ ₹   233.30 ─ bottom (2025-08-11)  broke UP
┌ ₹   287.99 ─ top    (2025-07-14)
│   box height 8.7%
└ ₹   265.02 ─ bottom (2025-07-15)  broke DOWN — red flag
┌ ₹   252.00 ─ top    (2025-06-25)
│   box height 8.1%
└ ₹   233.16 ─ bottom (2025-06-26)  broke DOWN — red flag
┌ ₹   222.58 ─ top    (2025-06-17)
│   box height 6.8%
└ ₹   208.32 ─ bottom (2025-06-20)  broke UP
┌ ₹   237.82 ─ top    (2025-06-03)
│   box height 6.2%
└ ₹   224.00 ─ bottom (2025-06-06)  broke DOWN — red flag
  ✂ ₹   126.07 ─ stop loss (bottom − 0.3 × box height)
  ▲ ₹   163.50 ─ buy on a close above the box top
```

This stock's own box height is **21.4%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FLAT** — growing, but not the step-up Darvas looked for.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 82.0 | 166.0 | 268.0 | 277.0 |
| EBITDA margin % | 24.0 | 23.0 | 25.0 | 24.0 |
| PAT | 55.0 | 106.0 | 177.0 | 188.0 |
| PAT margin % | 16.3 | 14.5 | 16.6 | 16.4 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## SHYAMMETL — WATCH

**Why:** moving inside its box on trigger volume — the entry is a close above the box top.

**The trigger numbers:** 747,503 shares traded in the week of 2026-03-30 against a 12-week average of 870,611 in 1 trading day of a week still running — 0.86× the weekly average already, 4.29× pro-rated to five days (multifold), with the price +0.11% on the week.

### Price and volume together, week by week

```
         │ 
    ₹879 │                 ●
         │           ●  ●     ●  ●
         │          ╱              ╲
         │          ╱              ╲
         │  ●  ●    ╱              ╲
         │       ╲  ╱               ●     ●
    ₹770 │        ●                    ●     ●  ●
         │ 
         ┼───────────────────────────────────────
 17.08 L │           █                    █
         │           █     █              █  █
         │     █  █  █     █  █     █     █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 7.48 L, close ₹771.1
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 5,976,128 |  |  |
| 2025-07 | 13,605,856 | ▲ +128% |  |
| 2025-08 | 4,140,859 | ▼ -70% |  |
| 2025-09 | 3,711,732 | ▼ -10% |  |
| 2025-10 | 4,367,325 | ▲ +18% |  |
| 2025-11 | 4,776,952 | ▲ +9% |  |
| 2025-12 | 3,638,583 | ▼ -24% |  |
| 2026-01 | 3,703,292 | ▬ +2% |  |
| 2026-02 | 2,821,411 | ▼ -24% |  |
| 2026-03 | 4,785,241 | ▲ +70% | partial — 19 days |

### The boxes

```
┌ ₹   821.05 ─ top    (2026-03-05)
│   box height 9.2%   close ₹771.10 inside
└ ₹   752.10 ─ bottom (2026-03-09)  ◀ current box
┌ ₹   912.80 ─ top    (2026-02-11)
│   box height 10.9%
└ ₹   823.10 ─ bottom (2026-02-24)  broke DOWN — red flag
┌ ₹   872.90 ─ top    (2026-01-29)
│   box height 5.5%
└ ₹   827.65 ─ bottom (2026-02-02)  broke UP
┌ ₹   858.00 ─ top    (2026-01-05)
│   box height 8.2%
└ ₹   792.90 ─ bottom (2026-01-12)  broke DOWN — red flag
┌ ₹   839.80 ─ top    (2025-12-23)
│   box height 2.9%
└ ₹   816.00 ─ bottom (2025-12-30)  broke UP
┌ ₹   824.30 ─ top    (2025-12-09)
│   box height 5.6%
└ ₹   780.70 ─ bottom (2025-12-10)  broke UP
┌ ₹   871.85 ─ top    (2025-11-24)
│   box height 8.6%
└ ₹   803.20 ─ bottom (2025-11-25)  broke DOWN — red flag
┌ ₹   933.35 ─ top    (2025-10-21)
│   box height 11.7%
└ ₹   835.50 ─ bottom (2025-11-06)  broke DOWN — red flag
┌ ₹   988.00 ─ top    (2025-10-06)
│   box height 7.8%
└ ₹   916.45 ─ bottom (2025-10-07)  broke DOWN — red flag
┌ ₹   939.00 ─ top    (2025-09-24)
│   box height 4.1%
└ ₹   902.10 ─ bottom (2025-09-26)  broke UP
┌ ₹   950.00 ─ top    (2025-09-08)
│   box height 4.8%
└ ₹   906.20 ─ bottom (2025-09-12)  broke DOWN — red flag
┌ ₹ 1,001.00 ─ top    (2025-07-31)
│   box height 6.6%
└ ₹   938.95 ─ bottom (2025-08-06)  broke DOWN — red flag
┌ ₹   894.55 ─ top    (2025-06-10)
│   box height 11.0%
└ ₹   805.60 ─ bottom (2025-06-19)  broke UP
┌ ₹   879.45 ─ top    (2025-06-03)
│   box height 3.8%
└ ₹   847.00 ─ bottom (2025-06-04)  broke UP
  ✂ ₹   731.42 ─ stop loss (bottom − 0.3 × box height)
  ▲ ₹   821.05 ─ buy on a close above the box top
```

This stock's own box height is **9.2%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +25.0% and PAT +16.6% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 1,499.0 | 1,570.0 | 1,866.0 | 2,333.0 |
| EBITDA margin % | 12.0 | 12.0 | 12.0 | 13.0 |
| PAT | 843.0 | 1,029.0 | 909.0 | 1,060.0 |
| PAT margin % | 6.7 | 7.8 | 6.0 | 5.7 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## THERMAX — ACCUMULATE

**Why:** sealed a higher box after an upward break and is holding it — add while it stabilises in the higher box.

**The trigger numbers:** 541,315 shares traded in the week of 2026-03-30 against a 12-week average of 657,297 in 1 trading day of a week still running — 0.82× the weekly average already, 4.12× pro-rated to five days (multifold), with the price +2.00% on the week.

### Price and volume together, week by week

```
         │ 
  ₹3,261 │                             ●  ●     ●
         │                    ●     ●        ●
         │                   ╱   ●
         │                   ╱
         │  ●                ╱
         │     ●             ╱
  ₹2,873 │        ●  ●  ●  ●
         │ 
         ┼───────────────────────────────────────
 18.40 L │                                █
         │                                █
         │              █  █  █           █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 5.41 L, close ₹3,260.7
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 3,002,152 |  |  |
| 2025-07 | 7,048,652 | ▲ +135% |  |
| 2025-08 | 8,361,527 | ▲ +19% |  |
| 2025-09 | 2,243,946 | ▼ -73% |  |
| 2025-10 | 1,581,758 | ▼ -30% |  |
| 2025-11 | 2,358,603 | ▲ +49% |  |
| 2025-12 | 1,961,128 | ▼ -17% |  |
| 2026-01 | 1,774,432 | ▼ -10% |  |
| 2026-02 | 3,067,291 | ▲ +73% |  |
| 2026-03 | 3,726,431 | ▲ +21% | partial — 19 days |

### The boxes

```
┌ ₹ 3,347.20 ─ top    (2026-03-19)
│   box height 9.7%   close ₹3,260.70 inside
└ ₹ 3,050.00 ─ bottom (2026-03-23)  ◀ current box
┌ ₹ 3,246.60 ─ top    (2026-02-26)
│   box height 9.4%
└ ₹ 2,966.80 ─ bottom (2026-03-04)  broke UP
┌ ₹ 2,985.70 ─ top    (2026-02-11)
│   box height 8.6%
└ ₹ 2,749.80 ─ bottom (2026-02-13)  broke UP
┌ ₹ 2,959.90 ─ top    (2026-01-23)
│   box height 7.6%
└ ₹ 2,751.10 ─ bottom (2026-01-30)  broke UP
┌ ₹ 3,120.00 ─ top    (2026-01-08)
│   box height 6.8%
└ ₹ 2,919.90 ─ bottom (2026-01-12)  broke DOWN — red flag
┌ ₹ 2,958.40 ─ top    (2025-12-12)
│   box height 4.8%
└ ₹ 2,824.00 ─ bottom (2025-12-18)  broke UP
┌ ₹ 2,985.90 ─ top    (2025-11-20)
│   box height 5.1%
└ ₹ 2,840.00 ─ bottom (2025-11-24)  broke DOWN — red flag
┌ ₹ 3,353.00 ─ top    (2025-10-28)
│   box height 12.3%
└ ₹ 2,986.00 ─ bottom (2025-11-12)  broke DOWN — red flag
┌ ₹ 3,398.40 ─ top    (2025-09-23)
│   box height 8.9%
└ ₹ 3,121.00 ─ bottom (2025-09-29)  broke DOWN — red flag
┌ ₹ 3,490.00 ─ top    (2025-09-10)
│   box height 6.1%
└ ₹ 3,288.80 ─ bottom (2025-09-15)  broke DOWN — red flag
┌ ₹ 3,588.00 ─ top    (2025-08-06)
│   box height 12.1%
└ ₹ 3,201.10 ─ bottom (2025-08-13)  broke DOWN — red flag
┌ ₹ 4,091.80 ─ top    (2025-07-17)
│   box height 10.8%
└ ₹ 3,691.20 ─ bottom (2025-07-28)  broke DOWN — red flag
┌ ₹ 3,583.70 ─ top    (2025-07-03)
│   box height 5.9%
└ ₹ 3,384.10 ─ bottom (2025-07-08)  broke UP
┌ ₹ 3,659.90 ─ top    (2025-06-11)
│   box height 9.1%
└ ₹ 3,354.00 ─ bottom (2025-06-20)  broke DOWN — red flag
  ✂ ₹ 2,960.84 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **9.7%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +14.1% and PAT +14.8% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 601.0 | 797.0 | 910.0 | 1,038.0 |
| EBITDA margin % | 7.0 | 9.0 | 9.0 | 10.0 |
| PAT | 451.0 | 643.0 | 627.0 | 720.0 |
| PAT margin % | 5.6 | 6.9 | 6.0 | 6.7 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## ARVINDFASN — WATCH

**Why:** moving inside its box on trigger volume — the entry is a close above the box top.

**The trigger numbers:** 878,937 shares traded in the week of 2026-03-30 against a 12-week average of 1,107,092 in 1 trading day of a week still running — 0.79× the weekly average already, 3.97× pro-rated to five days (multifold), with the price +5.50% on the week.

### Price and volume together, week by week

```
         │ 
    ₹484 │  ●        ●  ●  ●
         │     ●    ╱        ╲
         │       ╲  ╱         ●
         │        ●              ●  ●
         │                            ╲
         │                            ╲   ●     ●
    ₹382 │                             ●     ●
         │ 
         ┼───────────────────────────────────────
 29.19 L │        █
         │        █
         │        █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 8.79 L, close ₹403.5
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 8,001,443 |  |  |
| 2025-07 | 16,841,346 | ▲ +110% |  |
| 2025-08 | 5,364,733 | ▼ -68% |  |
| 2025-09 | 6,229,389 | ▲ +16% |  |
| 2025-10 | 3,734,386 | ▼ -40% |  |
| 2025-11 | 6,375,260 | ▲ +71% |  |
| 2025-12 | 4,336,517 | ▼ -32% |  |
| 2026-01 | 6,562,442 | ▲ +51% |  |
| 2026-02 | 3,614,491 | ▼ -45% |  |
| 2026-03 | 4,206,939 | ▲ +16% | partial — 19 days |

### The boxes

```
┌ ₹   470.50 ─ top    (2026-02-20)
│   box height 27.0%   close ₹403.50 inside
└ ₹   370.50 ─ bottom (2026-03-16)  ◀ current box
┌ ₹   514.20 ─ top    (2026-02-03)
│   box height 7.9%
└ ₹   476.50 ─ bottom (2026-02-06)  broke DOWN — red flag
┌ ₹   463.65 ─ top    (2026-01-23)
│   box height 9.9%
└ ₹   421.80 ─ bottom (2026-01-28)  broke UP
┌ ₹   495.00 ─ top    (2026-01-07)
│   box height 8.1%
└ ₹   457.80 ─ bottom (2026-01-12)  broke DOWN — red flag
┌ ₹   521.00 ─ top    (2025-12-16)
│   box height 5.0%
└ ₹   495.95 ─ bottom (2025-12-18)  broke DOWN — red flag
┌ ₹   495.45 ─ top    (2025-12-08)
│   box height 6.9%
└ ₹   463.50 ─ bottom (2025-12-09)  broke UP
┌ ₹   569.00 ─ top    (2025-11-03)
│   box height 15.4%
└ ₹   493.05 ─ bottom (2025-11-11)  broke DOWN — red flag
┌ ₹   526.90 ─ top    (2025-10-14)
│   box height 5.8%
└ ₹   498.00 ─ bottom (2025-10-20)  broke UP
┌ ₹   579.00 ─ top    (2025-09-17)
│   box height 13.2%
└ ₹   511.45 ─ bottom (2025-09-29)  broke DOWN — red flag
┌ ₹   564.30 ─ top    (2025-08-01)
│   box height 14.0%
└ ₹   494.95 ─ bottom (2025-08-14)  broke UP
┌ ₹   515.90 ─ top    (2025-07-23)
│   box height 4.6%
└ ₹   493.10 ─ bottom (2025-07-28)  broke UP
┌ ₹   471.70 ─ top    (2025-07-08)
│   box height 4.6%
└ ₹   451.00 ─ bottom (2025-07-14)  broke UP
┌ ₹   500.00 ─ top    (2025-06-16)
│   box height 6.9%
└ ₹   467.80 ─ bottom (2025-06-19)  broke DOWN — red flag
┌ ₹   476.65 ─ top    (2025-06-04)
│   box height 5.7%
└ ₹   451.10 ─ bottom (2025-06-06)  broke UP
  ✂ ₹   340.50 ─ stop loss (bottom − 0.3 × box height)
  ▲ ₹   470.50 ─ buy on a close above the box top
```

This stock's own box height is **27.0%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +16.9% and PAT +457.6% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 440.0 | 525.0 | 616.0 | 720.0 |
| EBITDA margin % | 11.0 | 12.0 | 13.0 | 14.0 |
| PAT | 87.0 | 137.0 | 33.0 | 184.0 |
| PAT margin % | 2.1 | 3.2 | 0.7 | 3.5 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## DMART — SELL

**Why:** closed below its box bottom — Darvas's red flag; a stock dropping to a lower box is sold, not averaged.

**The trigger numbers:** 1,738,503 shares traded in the week of 2026-03-30 against a 12-week average of 2,310,992 in 1 trading day of a week still running — 0.75× the weekly average already, 3.76× pro-rated to five days (multifold), with the price +1.37% on the week.

### Price and volume together, week by week

```
         │ 
  ₹3,957 │                                      ●
         │              ●  ●        ●        ●
         │             ╱      ●  ●     ●    ╱
         │  ●          ╱                 ╲  ╱
         │     ●       ╱                  ●
         │       ╲     ╱
  ₹3,666 │        ●  ●
         │ 
         ┼───────────────────────────────────────
 40.59 L │     █                             █
         │  █  █                       █     █
         │  █  █  █  █  █        █  █  █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 17.39 L, close ₹3,956.8
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 14,691,814 |  |  |
| 2025-07 | 18,742,627 | ▲ +28% |  |
| 2025-08 | 11,462,555 | ▼ -39% |  |
| 2025-09 | 9,178,655 | ▼ -20% |  |
| 2025-10 | 8,332,623 | ▼ -9% |  |
| 2025-11 | 7,252,624 | ▼ -13% |  |
| 2025-12 | 7,366,680 | ▬ +2% |  |
| 2026-01 | 12,023,316 | ▲ +63% |  |
| 2026-02 | 6,514,584 | ▼ -46% |  |
| 2026-03 | 11,745,009 | ▲ +80% | partial — 19 days |

### The boxes

```
┌ ₹ 4,056.00 ─ top    (2026-03-13)
│   box height 8.6%
└ ₹ 3,736.10 ─ bottom (2026-03-16)  broke DOWN — red flag
┌ ₹ 4,032.20 ─ top    (2026-02-11)
│   box height 6.2%
└ ₹ 3,798.60 ─ bottom (2026-02-24)  broke DOWN — red flag
┌ ₹ 3,868.00 ─ top    (2025-12-22)
│   box height 7.3%
└ ₹ 3,605.10 ─ bottom (2026-01-06)  broke UP
┌ ₹ 3,975.20 ─ top    (2025-12-02)
│   box height 5.4%
└ ₹ 3,770.00 ─ bottom (2025-12-11)  broke DOWN — red flag
┌ ₹ 4,222.00 ─ top    (2025-11-04)
│   box height 6.0%
└ ₹ 3,984.60 ─ bottom (2025-11-07)  broke DOWN — red flag
┌ ₹ 4,571.00 ─ top    (2025-09-29)
│   box height 9.0%
└ ₹ 4,192.10 ─ bottom (2025-10-13)  broke DOWN — red flag
┌ ₹ 4,949.50 ─ top    (2025-09-04)
│   box height 8.5%
└ ₹ 4,562.60 ─ bottom (2025-09-11)  broke DOWN — red flag
┌ ₹ 4,759.90 ─ top    (2025-08-20)
│   box height 2.6%
└ ₹ 4,636.80 ─ bottom (2025-08-22)  broke UP
┌ ₹ 4,495.50 ─ top    (2025-07-02)
│   box height 14.4%
└ ₹ 3,930.00 ─ bottom (2025-07-14)  broke UP
┌ ₹ 4,358.60 ─ top    (2025-06-23)
│   box height 2.9%
└ ₹ 4,236.70 ─ bottom (2025-06-25)  broke UP
┌ ₹ 4,244.80 ─ top    (2025-06-05)
│   box height 8.0%
└ ₹ 3,928.90 ─ bottom (2025-06-10)  broke UP
  ✂ ₹ 3,640.13 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **8.6%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +15.4% and PAT +9.7% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 3,639.0 | 4,106.0 | 4,495.0 | 5,189.0 |
| EBITDA margin % | 8.0 | 8.0 | 8.0 | 8.0 |
| PAT | 2,378.0 | 2,536.0 | 2,707.0 | 2,970.0 |
| PAT margin % | 5.6 | 5.0 | 4.6 | 4.3 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## WESTLIFE — WATCH

**Why:** broke down through its box but has since CLOSED back above the old box top on the trigger volume — a recovery, not a standing breakdown; with no new box sealed there is no honest stop yet, so wait for the next box before buying.

**The trigger numbers:** 1,240,049 shares traded in the week of 2026-03-30 against a 12-week average of 1,792,659 in 1 trading day of a week still running — 0.69× the weekly average already, 3.46× pro-rated to five days (multifold), with the price +8.79% on the week.

### Price and volume together, week by week

```
         │ 
    ₹542 │              ●
         │             ╱   ●
         │  ●          ╱      ●
         │     ●  ●  ●           ●  ●
         │                            ╲         ●
         │                             ●       ╱
    ₹438 │                                ●  ●
         │ 
         ┼───────────────────────────────────────
 1.50 Cr │              █
         │              █
         │              █
         │              █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 12.40 L, close ₹481.3
```

### Is the volume building, or a one-week event?

**STEPPED UP** — the last complete month traded well above the months before it.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 8,192,275 |  |  |
| 2025-07 | 2,886,889 | ▼ -65% |  |
| 2025-08 | 3,341,600 | ▲ +16% |  |
| 2025-09 | 3,430,200 | ▬ +3% |  |
| 2025-10 | 4,157,993 | ▲ +21% |  |
| 2025-11 | 4,533,114 | ▲ +9% |  |
| 2025-12 | 2,428,707 | ▼ -46% |  |
| 2026-01 | 2,407,361 | ▬ -1% |  |
| 2026-02 | 17,036,639 | ▲ +608% |  |
| 2026-03 | 3,410,177 | ▼ -80% | partial — 19 days |

### The boxes

```
┌ ₹   460.80 ─ top    (2026-03-13)
│   box height 8.0%
└ ₹   426.85 ─ bottom (2026-03-16)  broke DOWN — red flag
┌ ₹   527.00 ─ top    (2026-02-17)
│   box height 12.6%
└ ₹   468.00 ─ bottom (2026-03-02)  broke DOWN — red flag
┌ ₹   559.20 ─ top    (2026-02-05)
│   box height 8.4%
└ ₹   516.00 ─ bottom (2026-02-10)  broke DOWN — red flag
┌ ₹   569.70 ─ top    (2025-12-31)
│   box height 19.4%
└ ₹   477.00 ─ bottom (2026-01-20)  broke DOWN — red flag
┌ ₹   537.95 ─ top    (2025-12-17)
│   box height 4.9%
└ ₹   513.00 ─ bottom (2025-12-18)  broke UP
┌ ₹   645.00 ─ top    (2025-10-13)
│   box height 21.4%
└ ₹   531.20 ─ bottom (2025-11-19)  broke DOWN — red flag
┌ ₹   734.90 ─ top    (2025-09-23)
│   box height 11.9%
└ ₹   656.65 ─ bottom (2025-09-29)  broke DOWN — red flag
┌ ₹   775.00 ─ top    (2025-09-04)
│   box height 6.3%
└ ₹   728.75 ─ bottom (2025-09-05)  broke DOWN — red flag
┌ ₹   738.70 ─ top    (2025-08-01)
│   box height 13.0%
└ ₹   653.80 ─ bottom (2025-08-12)  broke UP
┌ ₹   819.20 ─ top    (2025-07-09)
│   box height 11.6%
└ ₹   734.15 ─ bottom (2025-07-23)  broke DOWN — red flag
┌ ₹   752.00 ─ top    (2025-06-09)
│   box height 10.0%
└ ₹   683.45 ─ bottom (2025-06-18)  broke UP
┌ ₹   679.70 ─ top    (2025-06-02)
│   box height 2.5%
└ ₹   663.00 ─ bottom (2025-06-04)  broke UP
```

### Earnings power (step 2)

**FLAT** — growing, but not the step-up Darvas looked for.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 382.0 | 377.0 | 329.0 | 337.0 |
| EBITDA margin % | 17.0 | 16.0 | 13.0 | 13.0 |
| PAT | 112.0 | 69.0 | 12.0 | 32.0 |
| PAT margin % | 4.9 | 2.9 | 0.5 | 1.2 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## AIAENG — SELL

**Why:** closed below its box bottom — Darvas's red flag; a stock dropping to a lower box is sold, not averaged.

**The trigger numbers:** 220,600 shares traded in the week of 2026-03-30 against a 12-week average of 327,098 in 1 trading day of a week still running — 0.67× the weekly average already, 3.37× pro-rated to five days (multifold), with the price +5.15% on the week.

### Price and volume together, week by week

```
         │ 
  ₹3,989 │  ●  ●     ●        ●
         │       ╲  ╱   ●  ●     ●
         │       ╲  ╱              ╲
         │        ●                 ●  ●
         │                               ╲      ●
         │                               ╲     ╱
  ₹3,410 │                                ●  ●
         │ 
         ┼───────────────────────────────────────
 10.06 L │                                █
         │                                █
         │  █                             █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 2.21 L, close ₹3,636.6
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 1,599,522 |  |  |
| 2025-07 | 1,091,963 | ▼ -32% |  |
| 2025-08 | 1,284,067 | ▲ +18% |  |
| 2025-09 | 2,297,590 | ▲ +79% |  |
| 2025-10 | 1,609,119 | ▼ -30% |  |
| 2025-11 | 2,119,557 | ▲ +32% |  |
| 2025-12 | 1,432,476 | ▼ -32% |  |
| 2026-01 | 1,366,056 | ▬ -5% |  |
| 2026-02 | 917,002 | ▼ -33% |  |
| 2026-03 | 1,989,282 | ▲ +117% | partial — 19 days |

### The boxes

```
┌ ₹ 3,974.60 ─ top    (2026-02-26)
│   box height 12.1%
└ ₹ 3,545.00 ─ bottom (2026-03-09)  broke DOWN — red flag
┌ ₹ 4,143.90 ─ top    (2026-01-29)
│   box height 7.9%
└ ₹ 3,841.90 ─ bottom (2026-02-02)  broke DOWN — red flag
┌ ₹ 4,168.70 ─ top    (2026-01-08)
│   box height 9.2%
└ ₹ 3,819.00 ─ bottom (2026-01-13)  broke DOWN — red flag
┌ ₹ 3,920.00 ─ top    (2025-12-01)
│   box height 8.3%
└ ₹ 3,618.90 ─ bottom (2025-12-08)  broke UP
┌ ₹ 3,851.00 ─ top    (2025-11-20)
│   box height 5.4%
└ ₹ 3,652.50 ─ bottom (2025-11-24)  broke UP
┌ ₹ 3,394.40 ─ top    (2025-10-16)
│   box height 3.3%
└ ₹ 3,287.00 ─ bottom (2025-10-20)  broke DOWN — red flag
┌ ₹ 3,295.00 ─ top    (2025-10-10)
│   box height 3.4%
└ ₹ 3,186.00 ─ bottom (2025-10-14)  broke UP
┌ ₹ 3,270.50 ─ top    (2025-10-03)
│   box height 3.8%
└ ₹ 3,150.60 ─ bottom (2025-10-07)  broke UP
┌ ₹ 3,140.00 ─ top    (2025-09-02)
│   box height 4.0%
└ ₹ 3,018.00 ─ bottom (2025-09-08)  broke UP
┌ ₹ 3,222.00 ─ top    (2025-07-30)
│   box height 6.5%
└ ₹ 3,025.00 ─ bottom (2025-08-04)  broke DOWN — red flag
┌ ₹ 3,469.00 ─ top    (2025-06-13)
│   box height 8.4%
└ ₹ 3,200.00 ─ bottom (2025-06-20)  broke DOWN — red flag
┌ ₹ 3,550.00 ─ top    (2025-06-05)
│   box height 1.8%
└ ₹ 3,486.90 ─ bottom (2025-06-06)  broke DOWN — red flag
  ✂ ₹ 3,416.12 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **12.1%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +8.8% and PAT +19.7% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 1,245.0 | 1,340.0 | 1,154.0 | 1,256.0 |
| EBITDA margin % | 25.0 | 28.0 | 27.0 | 28.0 |
| PAT | 1,056.0 | 1,137.0 | 1,060.0 | 1,269.0 |
| PAT margin % | 21.5 | 23.4 | 24.7 | 28.7 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## SAIL — WATCH

**Why:** moving inside its box on trigger volume — the entry is a close above the box top.

**The trigger numbers:** 70,851,364 shares traded in the week of 2026-03-30 against a 12-week average of 108,024,123 in 1 trading day of a week still running — 0.66× the weekly average already, 3.28× pro-rated to five days (multifold), with the price +3.38% on the week.

### Price and volume together, week by week

```
         │ 
    ₹166 │                       ●
         │              ●       ╱  ╲
         │             ╱   ●  ●    ╲
         │             ╱            ●     ●
         │             ╱              ╲  ╱  ╲   ●
         │     ●  ●  ●                 ●    ╲  ╱
    ₹146 │  ●                                ●
         │ 
         ┼───────────────────────────────────────
17.61 Cr │                       █
         │        █  █  █        █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 7.09 Cr, close ₹151.4
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 267,636,910 |  |  |
| 2025-07 | 282,780,230 | ▲ +6% |  |
| 2025-08 | 155,886,430 | ▼ -45% |  |
| 2025-09 | 233,501,173 | ▲ +50% |  |
| 2025-10 | 545,316,685 | ▲ +134% |  |
| 2025-11 | 387,625,515 | ▼ -29% |  |
| 2025-12 | 375,933,599 | ▬ -3% |  |
| 2026-01 | 488,846,547 | ▲ +30% |  |
| 2026-02 | 483,076,481 | ▬ -1% |  |
| 2026-03 | 430,750,244 | ▼ -11% | partial — 19 days |

### The boxes

```
┌ ₹   158.54 ─ top    (2026-03-20)
│   box height 11.4%   close ₹151.42 inside
└ ₹   142.26 ─ bottom (2026-03-23)  ◀ current box
┌ ₹   168.21 ─ top    (2026-03-02)
│   box height 16.2%
└ ₹   144.80 ─ bottom (2026-03-09)  broke DOWN — red flag
┌ ₹   163.00 ─ top    (2026-02-12)
│   box height 6.0%
└ ₹   153.84 ─ bottom (2026-02-17)  broke UP
┌ ₹   160.00 ─ top    (2026-01-29)
│   box height 13.2%
└ ₹   141.30 ─ bottom (2026-02-02)  broke UP
┌ ₹   152.80 ─ top    (2026-01-06)
│   box height 6.7%
└ ₹   143.25 ─ bottom (2026-01-08)  broke UP
┌ ₹   132.60 ─ top    (2025-12-12)
│   box height 6.9%
└ ₹   124.00 ─ bottom (2025-12-19)  broke UP
┌ ₹   145.90 ─ top    (2025-11-13)
│   box height 11.3%
└ ₹   131.10 ─ bottom (2025-11-25)  broke DOWN — red flag
┌ ₹   143.27 ─ top    (2025-10-29)
│   box height 6.1%
└ ₹   135.00 ─ bottom (2025-10-31)  broke UP
┌ ₹   132.93 ─ top    (2025-10-16)
│   box height 4.1%
└ ₹   127.74 ─ bottom (2025-10-20)  broke UP
┌ ₹   138.75 ─ top    (2025-09-24)
│   box height 6.4%
└ ₹   130.40 ─ bottom (2025-09-26)  broke DOWN — red flag
┌ ₹   134.79 ─ top    (2025-09-08)
│   box height 4.4%
└ ₹   129.11 ─ bottom (2025-09-09)  broke UP
┌ ₹   128.61 ─ top    (2025-07-28)
│   box height 7.4%
└ ₹   119.75 ─ bottom (2025-08-01)  broke DOWN — red flag
┌ ₹   139.98 ─ top    (2025-07-03)
│   box height 6.8%
└ ₹   131.00 ─ bottom (2025-07-09)  broke DOWN — red flag
┌ ₹   135.98 ─ top    (2025-06-09)
│   box height 9.8%
└ ₹   123.85 ─ bottom (2025-06-19)  broke UP
  ✂ ₹   137.38 ─ stop loss (bottom − 0.3 × box height)
  ▲ ₹   158.54 ─ buy on a close above the box top
```

This stock's own box height is **11.4%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +12.3% and PAT +42.2% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 8,038.0 | 11,149.0 | 10,690.0 | 12,000.0 |
| EBITDA margin % | 8.0 | 11.0 | 10.0 | 11.0 |
| PAT | 2,177.0 | 3,067.0 | 2,372.0 | 3,373.0 |
| PAT margin % | 2.1 | 2.9 | 2.3 | 3.0 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## ABDL — WATCH

**Why:** moving inside its box on trigger volume — the entry is a close above the box top.

**The trigger numbers:** 1,446,683 shares traded in the week of 2026-03-30 against a 12-week average of 2,281,732 in 1 trading day of a week still running — 0.63× the weekly average already, 3.17× pro-rated to five days (multifold), with the price +1.76% on the week.

### Price and volume together, week by week

```
         │ 
    ₹529 │              ●  ●
         │  ●          ╱      ●
         │     ●     ●           ●  ●
         │       ╲  ╱                 ╲
         │        ●                    ●
         │                               ╲
    ₹397 │                                ●  ●  ●
         │ 
         ┼───────────────────────────────────────
 42.58 L │  █
         │  █     █  █                       █
         │  █  █  █  █  █  █        █     █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 14.47 L, close ₹404.1
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 12,944,711 |  |  |
| 2025-07 | 15,445,277 | ▲ +19% |  |
| 2025-08 | 7,618,886 | ▼ -51% |  |
| 2025-09 | 8,826,372 | ▲ +16% |  |
| 2025-10 | 13,479,521 | ▲ +53% |  |
| 2025-11 | 12,454,681 | ▼ -8% |  |
| 2025-12 | 7,711,476 | ▼ -38% |  |
| 2026-01 | 13,133,171 | ▲ +70% |  |
| 2026-02 | 6,415,767 | ▼ -51% |  |
| 2026-03 | 10,410,742 | ▲ +62% | partial — 19 days |

### The boxes

```
┌ ₹   432.55 ─ top    (2026-03-18)
│   box height 13.2%   close ₹404.05 inside
└ ₹   382.10 ─ bottom (2026-03-23)  ◀ current box
┌ ₹   622.00 ─ top    (2026-01-01)
│   box height 44.8%
└ ₹   429.50 ─ bottom (2026-01-21)  broke DOWN — red flag
┌ ₹   633.50 ─ top    (2025-12-05)
│   box height 6.3%
└ ₹   595.85 ─ bottom (2025-12-09)  broke DOWN — red flag
┌ ₹   696.80 ─ top    (2025-11-04)
│   box height 14.6%
└ ₹   608.00 ─ bottom (2025-11-11)  broke DOWN — red flag
┌ ₹   562.00 ─ top    (2025-10-10)
│   box height 7.0%
└ ₹   525.10 ─ bottom (2025-10-15)  broke UP
┌ ₹   539.15 ─ top    (2025-09-24)
│   box height 6.8%
└ ₹   505.00 ─ bottom (2025-09-30)  broke UP
┌ ₹   565.50 ─ top    (2025-09-15)
│   box height 5.9%
└ ₹   534.00 ─ bottom (2025-09-17)  broke DOWN — red flag
┌ ₹   539.80 ─ top    (2025-08-05)
│   box height 11.1%
└ ₹   485.70 ─ bottom (2025-08-11)  broke UP
┌ ₹   505.90 ─ top    (2025-07-15)
│   box height 8.0%
└ ₹   468.35 ─ bottom (2025-07-21)  broke DOWN — red flag
┌ ₹   454.80 ─ top    (2025-06-10)
│   box height 11.7%
└ ₹   407.20 ─ bottom (2025-06-13)  broke UP
  ✂ ₹   366.97 ─ stop loss (bottom − 0.3 × box height)
  ▲ ₹   432.55 ─ buy on a close above the box top
```

This stock's own box height is **13.2%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +25.8% and PAT +12.8% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 186.0 | 243.0 | 431.0 | 542.0 |
| EBITDA margin % | 6.0 | 7.0 | 12.0 | 14.0 |
| PAT | 2.0 | 2.0 | 195.0 | 220.0 |
| PAT margin % | 0.1 | 0.1 | 5.5 | 5.6 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## DBL — SELL

**Why:** closed below its box bottom — Darvas's red flag; a stock dropping to a lower box is sold, not averaged.

**The trigger numbers:** 799,397 shares traded in the week of 2026-03-30 against a 12-week average of 1,355,943 in 1 trading day of a week still running — 0.59× the weekly average already, 2.95× pro-rated to five days (strong), with the price +0.27% on the week.

### Price and volume together, week by week

```
         │ 
    ₹471 │     ●  ●
         │    ╱      ●  ●     ●     ●
         │  ●             ╲  ╱  ╲  ╱   ●
         │                 ●    ╲  ╱     ╲
         │                       ●        ●
         │                                  ╲
    ₹386 │                                   ●  ●
         │ 
         ┼───────────────────────────────────────
 34.92 L │                    █
         │                    █
         │                 █  █  █  █  █     █
         │  █  █  █     █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 7.99 L, close ₹387.2
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 7,228,352 |  |  |
| 2025-07 | 3,365,798 | ▼ -53% |  |
| 2025-08 | 3,889,690 | ▲ +16% |  |
| 2025-09 | 15,409,298 | ▲ +296% |  |
| 2025-10 | 6,861,636 | ▼ -55% |  |
| 2025-11 | 12,295,630 | ▲ +79% |  |
| 2025-12 | 8,412,744 | ▼ -32% |  |
| 2026-01 | 3,184,281 | ▼ -62% |  |
| 2026-02 | 7,740,039 | ▲ +143% |  |
| 2026-03 | 6,295,434 | ▼ -19% | partial — 19 days |

### The boxes

```
┌ ₹   472.40 ─ top    (2026-03-11)
│   box height 11.8%
└ ₹   422.50 ─ bottom (2026-03-16)  broke DOWN — red flag
┌ ₹   461.65 ─ top    (2026-02-18)
│   box height 7.6%
└ ₹   429.10 ─ bottom (2026-02-20)  broke DOWN — red flag
┌ ₹   481.00 ─ top    (2025-11-28)
│   box height 11.1%
└ ₹   433.00 ─ bottom (2025-12-09)  broke DOWN — red flag
┌ ₹   468.75 ─ top    (2025-11-17)
│   box height 10.3%
└ ₹   425.15 ─ bottom (2025-11-24)  broke UP
┌ ₹   581.50 ─ top    (2025-09-18)
│   box height 23.7%
└ ₹   470.00 ─ bottom (2025-09-30)  broke DOWN — red flag
┌ ₹   499.50 ─ top    (2025-08-19)
│   box height 8.6%
└ ₹   460.00 ─ bottom (2025-08-29)  broke DOWN — red flag
┌ ₹   484.40 ─ top    (2025-07-24)
│   box height 6.5%
└ ₹   454.80 ─ bottom (2025-08-01)  broke UP
┌ ₹   554.65 ─ top    (2025-06-12)
│   box height 14.7%
└ ₹   483.40 ─ bottom (2025-06-23)  broke DOWN — red flag
  ✂ ₹   407.53 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **11.8%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA -18.2%, PAT 66.4%, EBITDA-margin change 1.0pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 957.0 | 1,421.0 | 2,159.0 | 1,766.0 |
| EBITDA margin % | 9.0 | 12.0 | 19.0 | 20.0 |
| PAT | -1.0 | 201.0 | 840.0 | 1,398.0 |
| PAT margin % | -0.0 | 1.7 | 7.4 | 15.6 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## GALLANTT — WATCH

**Why:** moving inside its box on trigger volume — the entry is a close above the box top.

**The trigger numbers:** 286,774 shares traded in the week of 2026-03-30 against a 12-week average of 512,834 in 1 trading day of a week still running — 0.56× the weekly average already, 2.80× pro-rated to five days (strong), with the price +1.09% on the week.

### Price and volume together, week by week

```
         │ 
    ₹589 │              ●
         │  ●          ╱  ╲      ●
         │    ╲        ╱  ╲   ●    ╲
         │     ●       ╱   ●       ╲      ●
         │       ╲     ╱           ╲   ●     ●  ●
         │        ●    ╱            ●
    ₹520 │           ●
         │ 
         ┼───────────────────────────────────────
  9.33 L │              █  █           █
         │              █  █           █     █
         │  █           █  █  █  █  █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 2.87 L, close ₹548.6
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 6,954,128 |  |  |
| 2025-07 | 12,570,536 | ▲ +81% |  |
| 2025-08 | 5,366,864 | ▼ -57% |  |
| 2025-09 | 8,693,168 | ▲ +62% |  |
| 2025-10 | 6,791,604 | ▼ -22% |  |
| 2025-11 | 16,122,437 | ▲ +137% |  |
| 2025-12 | 8,004,266 | ▼ -50% |  |
| 2026-01 | 1,340,736 | ▼ -83% |  |
| 2026-02 | 2,636,903 | ▲ +97% |  |
| 2026-03 | 2,612,111 | ▬ -1% | partial — 19 days |

### The boxes

```
┌ ₹   674.75 ─ top    (2025-10-16)
│   box height 31.0%   close ₹548.60 inside
└ ₹   515.10 ─ bottom (2025-10-27)  ◀ current box
┌ ₹   754.05 ─ top    (2025-09-10)
│   box height 16.2%
└ ₹   648.85 ─ bottom (2025-09-22)  broke DOWN — red flag
┌ ₹   802.25 ─ top    (2025-08-05)
│   box height 30.7%
└ ₹   613.85 ─ bottom (2025-08-18)  broke DOWN — red flag
┌ ₹   610.00 ─ top    (2025-07-10)
│   box height 6.5%
└ ₹   573.00 ─ bottom (2025-07-14)  broke UP
┌ ₹   568.65 ─ top    (2025-06-25)
│   box height 9.3%
└ ₹   520.35 ─ bottom (2025-07-01)  broke UP
┌ ₹   474.40 ─ top    (2025-06-02)
│   box height 12.2%
└ ₹   423.00 ─ bottom (2025-06-09)  broke UP
  ✂ ₹   467.21 ─ stop loss (bottom − 0.3 × box height)
  ▲ ₹   674.75 ─ buy on a close above the box top
```

This stock's own box height is **31.0%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FLAT** — growing, but not the step-up Darvas looked for.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 364.0 | 448.0 | 694.0 | 716.0 |
| EBITDA margin % | 9.0 | 11.0 | 16.0 | 16.0 |
| PAT | 141.0 | 225.0 | 401.0 | 484.0 |
| PAT margin % | 3.5 | 5.3 | 9.3 | 11.0 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## PHOENIXLTD — ACCUMULATE

**Why:** sealed a higher box after an upward break and is holding it — add while it stabilises in the higher box.

**The trigger numbers:** 1,275,726 shares traded in the week of 2026-03-30 against a 12-week average of 2,338,431 in 1 trading day of a week still running — 0.55× the weekly average already, 2.73× pro-rated to five days (strong), with the price +0.33% on the week.

### Price and volume together, week by week

```
         │ 
  ₹1,904 │  ●  ●
         │       ╲
         │       ╲      ●  ●  ●
         │        ●    ╱        ╲
         │           ●           ●
         │                          ●  ●
  ₹1,501 │                                ●  ●  ●
         │ 
         ┼───────────────────────────────────────
 34.33 L │              █                 █
         │  █     █  █  █              █  █  █
         │  █  █  █  █  █  █     █  █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 12.76 L, close ₹1,506.3
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 18,779,153 |  |  |
| 2025-07 | 24,880,182 | ▲ +32% |  |
| 2025-08 | 11,770,516 | ▼ -53% |  |
| 2025-09 | 15,018,284 | ▲ +28% |  |
| 2025-10 | 11,457,929 | ▼ -24% |  |
| 2025-11 | 10,512,007 | ▼ -8% |  |
| 2025-12 | 8,104,260 | ▼ -23% |  |
| 2026-01 | 10,639,907 | ▲ +31% |  |
| 2026-02 | 7,945,694 | ▼ -25% |  |
| 2026-03 | 11,312,877 | ▲ +42% | partial — 19 days |

### The boxes

```
┌ ₹ 1,633.90 ─ top    (2026-03-18)
│   box height 11.5%   close ₹1,506.30 inside
└ ₹ 1,465.60 ─ bottom (2026-03-24)  ◀ current box
┌ ₹ 1,615.50 ─ top    (2026-03-10)
│   box height 7.2%
└ ₹ 1,507.00 ─ bottom (2026-03-16)  broke UP
┌ ₹ 1,993.00 ─ top    (2026-01-12)
│   box height 24.6%
└ ₹ 1,600.00 ─ bottom (2026-02-02)  broke DOWN — red flag
┌ ₹ 1,871.00 ─ top    (2025-12-26)
│   box height 2.3%
└ ₹ 1,829.00 ─ bottom (2025-12-30)  broke UP
┌ ₹ 1,785.60 ─ top    (2025-11-07)
│   box height 7.4%
└ ₹ 1,662.80 ─ bottom (2025-11-24)  broke UP
┌ ₹ 1,716.40 ─ top    (2025-10-16)
│   box height 4.5%
└ ₹ 1,642.00 ─ bottom (2025-10-21)  broke UP
┌ ₹ 1,655.00 ─ top    (2025-09-22)
│   box height 8.0%
└ ₹ 1,533.00 ─ bottom (2025-09-30)  broke UP
┌ ₹ 1,599.50 ─ top    (2025-08-25)
│   box height 8.8%
└ ₹ 1,470.80 ─ bottom (2025-08-29)  broke UP
┌ ₹ 1,545.30 ─ top    (2025-07-25)
│   box height 10.2%
└ ₹ 1,402.50 ─ bottom (2025-08-11)  broke UP
┌ ₹ 1,515.10 ─ top    (2025-07-17)
│   box height 5.6%
└ ₹ 1,434.30 ─ bottom (2025-07-24)  broke UP
┌ ₹ 1,642.90 ─ top    (2025-06-24)
│   box height 10.7%
└ ₹ 1,483.50 ─ bottom (2025-07-02)  broke DOWN — red flag
┌ ₹ 1,692.80 ─ top    (2025-06-11)
│   box height 8.0%
└ ₹ 1,567.00 ─ bottom (2025-06-13)  broke DOWN — red flag
┌ ₹ 1,623.00 ─ top    (2025-06-03)
│   box height 4.3%
└ ₹ 1,556.70 ─ bottom (2025-06-05)  broke UP
  ✂ ₹ 1,415.11 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **11.5%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +22.0% and PAT +19.1% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 1,519.0 | 2,182.0 | 2,162.0 | 2,637.0 |
| EBITDA margin % | 58.0 | 55.0 | 57.0 | 60.0 |
| PAT | 1,478.0 | 1,333.0 | 1,307.0 | 1,557.0 |
| PAT margin % | 56.5 | 33.6 | 34.3 | 35.2 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## ASKAUTOLTD — BUY

**Why:** closed above its box top on trigger volume — reaching for the higher box; buy the break.

**The trigger numbers:** 396,356 shares traded in the week of 2026-03-30 against a 12-week average of 733,102 in 1 trading day of a week still running — 0.54× the weekly average already, 2.70× pro-rated to five days (strong), with the price +1.37% on the week.

### Price and volume together, week by week

```
         │ 
    ₹475 │  ●  ●
         │       ╲      ●
         │       ╲   ●    ╲                     ●
         │       ╲  ╱      ●  ●              ●
         │        ●              ●          ╱
         │                         ╲      ●
    ₹392 │                          ●  ●
         │ 
         ┼───────────────────────────────────────
 14.03 L │                    █
         │                    █        █     █
         │  █  █     █  █  █  █     █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 3.96 L, close ₹444.8
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 7,945,943 |  |  |
| 2025-07 | 5,340,280 | ▼ -33% |  |
| 2025-08 | 3,867,990 | ▼ -28% |  |
| 2025-09 | 8,883,075 | ▲ +130% |  |
| 2025-10 | 5,581,535 | ▼ -37% |  |
| 2025-11 | 13,345,959 | ▲ +139% |  |
| 2025-12 | 4,004,821 | ▼ -70% |  |
| 2026-01 | 2,460,003 | ▼ -39% |  |
| 2026-02 | 3,149,406 | ▲ +28% |  |
| 2026-03 | 3,774,821 | ▲ +20% | partial — 19 days |

### The boxes

```
┌ ₹   424.70 ─ top    (2026-03-19)
│   box height 8.3%
└ ₹   392.30 ─ bottom (2026-03-23)  broke UP
┌ ₹   407.00 ─ top    (2026-03-02)
│   box height 8.4%
└ ₹   375.30 ─ bottom (2026-03-09)  broke UP
┌ ₹   469.65 ─ top    (2026-02-03)
│   box height 11.2%
└ ₹   422.50 ─ bottom (2026-02-13)  broke DOWN — red flag
┌ ₹   446.55 ─ top    (2026-01-21)
│   box height 10.9%
└ ₹   402.75 ─ bottom (2026-01-27)  broke UP
┌ ₹   501.00 ─ top    (2025-11-28)
│   box height 12.3%
└ ₹   446.15 ─ bottom (2025-12-09)  broke DOWN — red flag
┌ ₹   474.70 ─ top    (2025-11-10)
│   box height 5.2%
└ ₹   451.05 ─ bottom (2025-11-12)  broke UP
┌ ₹   578.50 ─ top    (2025-09-24)
│   box height 23.8%
└ ₹   467.20 ─ bottom (2025-10-14)  broke DOWN — red flag
┌ ₹   555.00 ─ top    (2025-07-16)
│   box height 23.6%
└ ₹   449.05 ─ bottom (2025-08-07)  broke UP
┌ ₹   547.70 ─ top    (2025-06-30)
│   box height 8.4%
└ ₹   505.25 ─ bottom (2025-07-07)  broke UP
┌ ₹   472.00 ─ top    (2025-06-06)
│   box height 7.6%
└ ₹   438.60 ─ bottom (2025-06-17)  broke UP
  ✂ ₹   382.58 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **8.3%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +22.9% and PAT +19.8% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 231.0 | 301.0 | 432.0 | 531.0 |
| EBITDA margin % | 9.0 | 10.0 | 12.0 | 13.0 |
| PAT | 123.0 | 174.0 | 248.0 | 297.0 |
| PAT margin % | 4.8 | 5.8 | 6.9 | 7.1 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## CARBORUNIV — SELL

**Why:** closed below its box bottom — Darvas's red flag; a stock dropping to a lower box is sold, not averaged.

**The trigger numbers:** 406,933 shares traded in the week of 2026-03-30 against a 12-week average of 872,313 in 1 trading day of a week still running — 0.47× the weekly average already, 2.33× pro-rated to five days (strong), with the price +1.06% on the week.

### Price and volume together, week by week

```
         │ 
    ₹844 │                    ●
         │                 ●     ●
         │     ●  ●       ╱        ╲
         │  ●       ╲     ╱         ●
         │           ●    ╱           ╲
         │              ●             ╲         ●
    ₹756 │                             ●  ●  ●
         │ 
         ┼───────────────────────────────────────
 17.15 L │        █     █
         │        █     █  █  █
         │  █     █  █  █  █  █  █           █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 4.07 L, close ₹775.7
```

### Is the volume building, or a one-week event?

**BUILDING** — volume has risen month over month for the last 2 complete months — buying pressure has been building, not arriving in one week.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 3,123,021 |  |  |
| 2025-07 | 3,745,892 | ▲ +20% |  |
| 2025-08 | 9,201,465 | ▲ +146% |  |
| 2025-09 | 4,039,294 | ▼ -56% |  |
| 2025-10 | 1,907,235 | ▼ -53% |  |
| 2025-11 | 10,511,259 | ▲ +451% |  |
| 2025-12 | 2,183,796 | ▼ -79% |  |
| 2026-01 | 3,948,956 | ▲ +81% |  |
| 2026-02 | 4,867,859 | ▲ +23% |  |
| 2026-03 | 2,242,780 | ▼ -54% | partial — 19 days |

### The boxes

```
┌ ₹   855.45 ─ top    (2026-02-23)
│   box height 9.7%
└ ₹   780.00 ─ bottom (2026-03-02)  broke DOWN — red flag
┌ ₹   847.40 ─ top    (2026-02-11)
│   box height 4.5%
└ ₹   811.00 ─ bottom (2026-02-16)  broke UP
┌ ₹   840.55 ─ top    (2026-01-28)
│   box height 12.3%
└ ₹   748.50 ─ bottom (2026-02-02)  broke UP
┌ ₹   821.95 ─ top    (2026-01-09)
│   box height 4.5%
└ ₹   786.80 ─ bottom (2026-01-12)  broke DOWN — red flag
┌ ₹   904.00 ─ top    (2025-12-03)
│   box height 10.0%
└ ₹   822.10 ─ bottom (2025-12-09)  broke DOWN — red flag
┌ ₹   877.00 ─ top    (2025-11-18)
│   box height 7.8%
└ ₹   813.30 ─ bottom (2025-11-21)  broke UP
┌ ₹   942.20 ─ top    (2025-10-30)
│   box height 7.5%
└ ₹   876.20 ─ bottom (2025-11-07)  broke DOWN — red flag
┌ ₹ 1,018.00 ─ top    (2025-08-20)
│   box height 13.9%
└ ₹   893.85 ─ bottom (2025-08-28)  broke DOWN — red flag
┌ ₹   926.00 ─ top    (2025-08-05)
│   box height 11.2%
└ ₹   833.05 ─ bottom (2025-08-11)  broke UP
┌ ₹ 1,004.60 ─ top    (2025-07-18)
│   box height 9.1%
└ ₹   921.15 ─ bottom (2025-07-29)  broke DOWN — red flag
┌ ₹ 1,009.70 ─ top    (2025-07-01)
│   box height 3.4%
└ ₹   976.50 ─ bottom (2025-07-02)  broke DOWN — red flag
┌ ₹   986.00 ─ top    (2025-06-25)
│   box height 4.3%
└ ₹   945.55 ─ bottom (2025-06-27)  broke UP
┌ ₹   955.95 ─ top    (2025-06-13)
│   box height 4.4%
└ ₹   915.50 ─ bottom (2025-06-20)  broke UP
┌ ₹ 1,001.15 ─ top    (2025-06-02)
│   box height 6.3%
└ ₹   941.90 ─ bottom (2025-06-06)  broke DOWN — red flag
  ✂ ₹   757.37 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **9.7%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA -18.8%, PAT -43.8%, EBITDA-margin change -4.0pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 655.0 | 741.0 | 717.0 | 582.0 |
| EBITDA margin % | 14.0 | 16.0 | 15.0 | 11.0 |
| PAT | 442.0 | 476.0 | 299.0 | 168.0 |
| PAT margin % | 9.5 | 10.1 | 6.1 | 3.2 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## UTIAMC — SELL

**Why:** closed below its box bottom — Darvas's red flag; a stock dropping to a lower box is sold, not averaged.

**The trigger numbers:** 184,978 shares traded in the week of 2026-03-30 against a 12-week average of 406,844 in 1 trading day of a week still running — 0.45× the weekly average already, 2.27× pro-rated to five days (strong), with the price +0.07% on the week.

### Price and volume together, week by week

```
         │ 
  ₹1,087 │  ●  ●           ●  ●
         │       ╲      ●       ╲
         │       ╲     ╱        ╲
         │       ╲     ╱        ╲
         │       ╲     ╱         ●
         │        ●  ●              ●
    ₹937 │                             ●  ●  ●  ●
         │ 
         ┼───────────────────────────────────────
  6.19 L │        █  █
         │  █     █  █  █        █     █
         │  █  █  █  █  █  █  █  █  █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 1.85 L, close ₹937.4
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 7,471,254 |  |  |
| 2025-07 | 8,776,242 | ▲ +17% |  |
| 2025-08 | 2,664,005 | ▼ -70% |  |
| 2025-09 | 1,947,997 | ▼ -27% |  |
| 2025-10 | 5,275,236 | ▲ +171% |  |
| 2025-11 | 2,236,484 | ▼ -58% |  |
| 2025-12 | 2,699,298 | ▲ +21% |  |
| 2026-01 | 1,999,216 | ▼ -26% |  |
| 2026-02 | 1,507,884 | ▼ -25% |  |
| 2026-03 | 1,701,035 | ▲ +13% | partial — 19 days |

### The boxes

```
┌ ₹ 1,107.50 ─ top    (2026-01-16)
│   box height 19.4%
└ ₹   927.20 ─ bottom (2026-01-27)  broke DOWN — red flag
┌ ₹ 1,147.40 ─ top    (2025-12-04)
│   box height 4.9%
└ ₹ 1,094.00 ─ bottom (2025-12-11)  broke DOWN — red flag
┌ ₹ 1,259.90 ─ top    (2025-10-31)
│   box height 10.8%
└ ₹ 1,136.70 ─ bottom (2025-11-21)  broke DOWN — red flag
┌ ₹ 1,409.00 ─ top    (2025-10-17)
│   box height 11.5%
└ ₹ 1,263.30 ─ bottom (2025-10-20)  broke DOWN — red flag
┌ ₹ 1,418.00 ─ top    (2025-09-23)
│   box height 9.5%
└ ₹ 1,295.00 ─ bottom (2025-09-29)  broke DOWN — red flag
┌ ₹ 1,364.70 ─ top    (2025-09-03)
│   box height 3.7%
└ ₹ 1,315.50 ─ bottom (2025-09-09)  broke UP
┌ ₹ 1,494.80 ─ top    (2025-07-22)
│   box height 16.0%
└ ₹ 1,288.60 ─ bottom (2025-08-06)  broke DOWN — red flag
┌ ₹ 1,450.00 ─ top    (2025-07-15)
│   box height 2.3%
└ ₹ 1,417.00 ─ bottom (2025-07-17)  broke UP
┌ ₹ 1,304.80 ─ top    (2025-07-01)
│   box height 3.8%
└ ₹ 1,257.00 ─ bottom (2025-07-02)  broke UP
┌ ₹ 1,288.90 ─ top    (2025-06-09)
│   box height 6.4%
└ ₹ 1,211.00 ─ bottom (2025-06-13)  broke UP
  ✂ ₹   873.11 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **19.4%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA -26.0%, PAT -41.9%, EBITDA-margin change -12.0pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 612.0 | 1,034.0 | 1,102.0 | 816.0 |
| EBITDA margin % | 48.0 | 60.0 | 60.0 | 48.0 |
| PAT | 440.0 | 802.0 | 813.0 | 472.0 |
| PAT margin % | 34.7 | 46.2 | 43.9 | 27.7 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## AFFLE — BUY

**Why:** closed above its box top on trigger volume — reaching for the higher box; buy the break.

**The trigger numbers:** 546,166 shares traded in the week of 2026-03-30 against a 12-week average of 1,243,744 in 1 trading day of a week still running — 0.44× the weekly average already, 2.20× pro-rated to five days (strong), with the price +0.21% on the week.

### Price and volume together, week by week

```
         │ 
  ₹1,784 │  ●  ●
         │       ╲      ●
         │        ●    ╱  ╲
         │           ●     ●
         │                    ●              ●  ●
         │                       ●          ╱
  ₹1,286 │                          ●  ●  ●
         │ 
         ┼───────────────────────────────────────
 24.37 L │                       █           █
         │                       █        █  █
         │              █  █     █  █  █  █  █
         │  █  █  █  █  █  █  █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 5.46 L, close ₹1,449.1
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 8,416,644 |  |  |
| 2025-07 | 6,215,885 | ▼ -26% |  |
| 2025-08 | 3,508,079 | ▼ -44% |  |
| 2025-09 | 8,968,975 | ▲ +156% |  |
| 2025-10 | 3,219,490 | ▼ -64% |  |
| 2025-11 | 4,430,951 | ▲ +38% |  |
| 2025-12 | 5,645,185 | ▲ +27% |  |
| 2026-01 | 3,322,870 | ▼ -41% |  |
| 2026-02 | 5,128,612 | ▲ +54% |  |
| 2026-03 | 7,188,236 | ▲ +40% | partial — 19 days |

### The boxes

```
┌ ₹ 1,360.00 ─ top    (2026-03-18)
│   box height 8.7%
└ ₹ 1,251.30 ─ bottom (2026-03-23)  broke UP
┌ ₹ 1,698.00 ─ top    (2026-02-11)
│   box height 28.5%
└ ₹ 1,321.10 ─ bottom (2026-02-27)  broke DOWN — red flag
┌ ₹ 1,645.20 ─ top    (2026-01-21)
│   box height 9.1%
└ ₹ 1,508.00 ─ bottom (2026-01-27)  broke UP
┌ ₹ 1,829.10 ─ top    (2026-01-06)
│   box height 8.4%
└ ₹ 1,687.30 ─ bottom (2026-01-12)  broke DOWN — red flag
┌ ₹ 1,805.00 ─ top    (2025-12-30)
│   box height 2.6%
└ ₹ 1,760.00 ─ bottom (2026-01-02)  broke UP
┌ ₹ 1,729.00 ─ top    (2025-11-21)
│   box height 9.5%
└ ₹ 1,579.60 ─ bottom (2025-12-09)  broke UP
┌ ₹ 1,832.80 ─ top    (2025-11-06)
│   box height 7.2%
└ ₹ 1,710.00 ─ bottom (2025-11-10)  broke DOWN — red flag
┌ ₹ 2,185.90 ─ top    (2025-09-22)
│   box height 16.4%
└ ₹ 1,878.80 ─ bottom (2025-10-07)  broke DOWN — red flag
┌ ₹ 1,954.90 ─ top    (2025-09-03)
│   box height 3.6%
└ ₹ 1,886.50 ─ bottom (2025-09-04)  broke UP
┌ ₹ 2,025.00 ─ top    (2025-07-29)
│   box height 6.5%
└ ₹ 1,901.00 ─ bottom (2025-07-31)  broke DOWN — red flag
┌ ₹ 1,920.70 ─ top    (2025-07-22)
│   box height 8.3%
└ ₹ 1,773.00 ─ bottom (2025-07-28)  broke UP
┌ ₹ 2,080.00 ─ top    (2025-07-03)
│   box height 9.0%
└ ₹ 1,907.80 ─ bottom (2025-07-08)  broke DOWN — red flag
┌ ₹ 1,985.00 ─ top    (2025-06-10)
│   box height 7.8%
└ ₹ 1,841.50 ─ bottom (2025-06-13)  broke UP
  ✂ ₹ 1,218.69 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **8.7%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**RISING** — EBITDA +26.3% and PAT +19.1% in the latest year with margins holding.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| EBITDA | 288.0 | 360.0 | 483.0 | 610.0 |
| EBITDA margin % | 20.0 | 20.0 | 21.0 | 23.0 |
| PAT | 245.0 | 297.0 | 382.0 | 455.0 |
| PAT margin % | 17.1 | 16.1 | 16.9 | 16.8 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## SAMMAANCAP — SELL

**Why:** closed below its box bottom — Darvas's red flag; a stock dropping to a lower box is sold, not averaged.

**The trigger numbers:** 25,387,575 shares traded in the week of 2026-03-30 against a 12-week average of 57,683,157 in 1 trading day of a week still running — 0.44× the weekly average already, 2.20× pro-rated to five days (strong), with the price +0.79% on the week.

### Price and volume together, week by week

```
         │ 
    ₹154 │                    ●
         │           ●       ╱   ●              ●
         │          ╱  ╲     ╱     ╲         ●
         │          ╱   ●    ╱     ╲        ╱
         │  ●       ╱      ●       ╲        ╱
         │    ╲     ╱               ●       ╱
    ₹138 │     ●  ●                    ●  ●
         │ 
         ┼───────────────────────────────────────
19.50 Cr │                                   █
         │                                   █
         │           █           █           █
         │  █  █  █  █  █     █  █  █  █  █  █  █
         └───────────────────────────────────────
          01-05 01-19 02-02 02-16 03-02 03-16 03-30
           latest week (partial: 1 days so far): volume 2.54 Cr, close ₹149.5
```

### Is the volume building, or a one-week event?

**SPIKE ONLY** — monthly volumes were flat before the trigger — the surge is a one-week event so far, not a building trend.

| Month | Volume | vs prior month | |
|---|---:|---:|---|
| 2025-06 | 233,804,101 |  |  |
| 2025-07 | 380,016,853 | ▲ +63% |  |
| 2025-08 | 218,582,267 | ▼ -42% |  |
| 2025-09 | 640,204,467 | ▲ +193% |  |
| 2025-10 | 653,180,919 | ▬ +2% |  |
| 2025-11 | 454,313,723 | ▼ -30% |  |
| 2025-12 | 359,214,952 | ▼ -21% |  |
| 2026-01 | 243,176,491 | ▼ -32% |  |
| 2026-02 | 178,904,656 | ▼ -26% |  |
| 2026-03 | 321,640,721 | ▲ +80% | partial — 19 days |

### The boxes

```
┌ ₹   162.00 ─ top    (2026-02-25)
│   box height 18.1%
└ ₹   137.19 ─ bottom (2026-03-09)  broke DOWN — red flag
┌ ₹   152.38 ─ top    (2026-01-30)
│   box height 7.9%
└ ₹   141.20 ─ bottom (2026-02-02)  broke UP
┌ ₹   153.22 ─ top    (2025-12-15)
│   box height 10.8%
└ ₹   138.28 ─ bottom (2025-12-18)  broke DOWN — red flag
┌ ₹   185.00 ─ top    (2025-11-18)
│   box height 24.9%
└ ₹   148.10 ─ bottom (2025-11-25)  broke DOWN — red flag
┌ ₹   191.20 ─ top    (2025-10-27)
│   box height 5.6%
└ ₹   181.10 ─ bottom (2025-10-29)  broke DOWN — red flag
┌ ₹   170.20 ─ top    (2025-10-01)
│   box height 10.9%
└ ₹   153.51 ─ bottom (2025-10-06)  broke UP
┌ ₹   145.49 ─ top    (2025-09-19)
│   box height 9.6%
└ ₹   132.80 ─ bottom (2025-09-25)  broke UP
┌ ₹   141.50 ─ top    (2025-09-03)
│   box height 5.2%
└ ₹   134.44 ─ bottom (2025-09-05)  broke UP
┌ ₹   125.46 ─ top    (2025-08-12)
│   box height 6.8%
└ ₹   117.50 ─ bottom (2025-08-14)  broke UP
┌ ₹   146.82 ─ top    (2025-06-25)
│   box height 20.6%
└ ₹   121.71 ─ bottom (2025-07-08)  broke DOWN — red flag
┌ ₹   135.39 ─ top    (2025-06-11)
│   box height 14.7%
└ ₹   118.01 ─ bottom (2025-06-23)  broke UP
  ✂ ₹   129.75 ─ stop loss (bottom − 0.3 × box height)
```

This stock's own box height is **18.1%** — box edges are taken from its actual highs and lows (an edge stands only after 3 sessions fail to better it), never from a fixed percentage.

### Earnings power (step 2)

**FALLING** — EBITDA 3.2%, PAT -295.4%, EBITDA-margin change -1.0pp.

| Measure | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|
| Financing profit | 1,683.0 | 1,690.0 | -2,295.0 | -2,221.0 |
| Financing profit margin % | 19.0 | 20.0 | -26.0 | -27.0 |
| PAT | 1,130.0 | 1,214.0 | -1,807.0 | -7,145.0 |
| PAT margin % | 13.0 | 14.2 | -20.8 | -87.5 |

**New-age industry:** not assessed (excluded_from_backtest) — stated honestly rather than guessed.

## The stop-loss ledger

Positions carried between runs. The rhythm: this skill runs weekly after Friday's close; every held stop is recomputed from the stock's CURRENT box (stop = box bottom − 0.3 × box height) and only ever moves UP — a stock seals a higher box only after three quiet sessions on each edge, so the ratchet is decisive by construction. A SELL row means the stock closed below its box bottom — the red flag.

| Stock | First flagged | Action | Box (₹) | Stop | Updated |
|---|---|---|---|---:|---|
| ABDL | 2026-09-13 | WATCH | 382.1–432.6 | ₹366.97 | 2026-09-13 |
| AFFLE | 2026-09-13 | BUY | 1,251.3–1,360.0 | ₹1,218.69 | 2026-09-13 |
| AIAENG | 2026-09-13 | SELL | 3,545.0–3,974.6 | exit | 2026-09-13 |
| ARVINDFASN | 2026-09-13 | WATCH | 370.5–470.5 | ₹340.50 | 2026-09-13 |
| ASKAUTOLTD | 2026-09-13 | BUY | 392.3–424.7 | ₹382.58 | 2026-09-13 |
| CARBORUNIV | 2026-09-13 | SELL | 780.0–855.5 | exit | 2026-09-13 |
| DBL | 2026-09-13 | SELL | 422.5–472.4 | exit | 2026-09-13 |
| DMART | 2026-09-13 | SELL | 3,736.1–4,056.0 | exit | 2026-09-13 |
| EIEL | 2026-09-13 | WATCH | 134.7–163.5 | ₹126.07 | 2026-09-13 |
| EPL | 2026-09-13 | WATCH | 176.4–205.8 | ₹167.59 | 2026-09-13 |
| GALLANTT | 2026-09-13 | WATCH | 515.1–674.8 | ₹467.21 | 2026-09-13 |
| IRB | 2026-09-13 | WATCH | 19.8–22.5 | ₹19.03 | 2026-09-13 |
| JLHL | 2026-09-13 | WATCH | 239.8–279.3 | ₹227.90 | 2026-09-13 |
| KNRCON | 2026-09-13 | SELL | 116.9–148.0 | exit | 2026-09-13 |
| PHOENIXLTD | 2026-09-13 | ACCUMULATE | 1,465.6–1,633.9 | ₹1,415.11 | 2026-09-13 |
| RENUKA | 2026-09-13 | WATCH | 23.0–26.0 | ₹22.11 | 2026-09-13 |
| SAIL | 2026-09-13 | WATCH | 142.3–158.5 | ₹137.38 | 2026-09-13 |
| SAMMAANCAP | 2026-09-13 | SELL | 137.2–162.0 | exit | 2026-09-13 |
| SHYAMMETL | 2026-09-13 | WATCH | 752.1–821.0 | ₹731.42 | 2026-09-13 |
| THERMAX | 2026-09-13 | ACCUMULATE | 3,050.0–3,347.2 | ₹2,960.84 | 2026-09-13 |
| TRAVELFOOD | 2026-09-13 | BUY | 1,089.0–1,138.0 | ₹1,074.30 | 2026-09-13 |
| URBANCO | 2026-09-13 | WATCH | 109.2–131.4 | ₹102.57 | 2026-09-13 |
| UTIAMC | 2026-09-13 | SELL | 927.2–1,107.5 | exit | 2026-09-13 |
| WESTLIFE | 2026-09-13 | WATCH | — | exit | 2026-09-13 |
| WEWORK | 2026-09-13 | WATCH | 421.0–552.8 | ₹381.46 | 2026-09-13 |

## How this screen was built

- **Data:** daily bars for the last six months for every NiftyTotalMarket symbol, fetched fresh THIS run (2026-09-13T07:26:31+00:00) from Yahoo Finance into `IndividualStockAnalysis/India/VolumeAndPricing/NiftyTotalMarket/`, aggregated into completed Monday-Friday weeks. 1 symbols were unavailable and are listed in `_fetch_log.csv`, never silently skipped.
- **Trigger:** last completed week's volume ÷ mean of up to 12 prior completed weeks (minimum 6); qualification needs ≥1.5× AND a positive week. Tiers: ≥3× multifold, ≥2× strong, ≥1.5× elevated.
- **Boxes:** Darvas's own rule — a top stands after 3 sessions fail to exceed it, then a bottom stands after 3 sessions fail to undercut it; a close above the top reaches for the higher box, a close below the bottom is the red flag.
- **Stops:** bottom − 0.3 × box height, ratcheted up only (a 50–55 box stops near 48.5, a 70–85 box near 65.5 — the worked examples of the method).
- **Volume trend:** month-wise totals from the same daily bars; BUILDING = volume rose month over month for at least the last two complete months; the running month is shown but never argued from.
- **Earnings power:** EBITDA, EBITDA margin, PAT and PAT margin from the stored statements; the new-age read comes from the conference calls via the judge model and is cached per transcript. Anything unassessable is marked, never guessed.
- Research tooling — not investment advice.

## What actually happened next (post-window evaluation)

*Added after the as-of run, from the LIVE archive's real prices (2026-04-01 to 2026-09-11). Rules: BUY/ACCUMULATE enter at the window's last close and honour the INITIAL stop only (no weekly ratcheting, no costs — conservative and simple); WATCH and SELL rows show the raw subsequent move. Benchmark: the Nifty 50 returned **+4.8%** over the same period (22,331 → 23,398).*

| Stock | Action | Entry (31 Mar) | Stop | Outcome | Close 11 Sep | System return |
|---|---|---:|---:|---|---:|---:|
| ASKAUTOLTD | BUY | ₹444.8 | ₹382.6 | held | ₹624.5 | +40.4% |
| AFFLE | BUY | ₹1,449.1 | ₹1,218.7 | held | ₹1,567.6 | +8.2% |
| TRAVELFOOD | BUY | ₹1,261.8 | ₹1,074.3 | stopped 2026-05-18 | ₹1,253.6 | -14.9% |
| PHOENIXLTD | ACCUMULATE | ₹1,506.3 | ₹1,415.1 | held | ₹1,890.0 | +25.5% |
| THERMAX | ACCUMULATE | ₹3,260.7 | ₹2,960.8 | held | ₹3,682.0 | +12.9% |
| ABDL | WATCH | ₹404.1 | ₹367.0 | held | ₹632.5 | +56.5% |
| EIEL | WATCH | ₹140.4 | ₹126.1 | held | ₹207.1 | +47.5% |
| WEWORK | WATCH | ₹455.4 | ₹381.5 | held | ₹670.2 | +47.2% |
| URBANCO | WATCH | ₹118.9 | ₹102.6 | held | ₹166.9 | +40.4% |
| SHYAMMETL | WATCH | ₹771.1 | ₹731.4 | held | ₹1,074.8 | +39.4% |
| WESTLIFE | WATCH | ₹481.3 | — | held | ₹569.6 | +18.3% |
| SAIL | WATCH | ₹151.4 | ₹137.4 | held | ₹179.0 | +18.2% |
| EPL | WATCH | ₹205.3 | ₹167.6 | held | ₹239.3 | +16.6% |
| ARVINDFASN | WATCH | ₹403.5 | ₹340.5 | held | ₹446.5 | +10.7% |
| JLHL | WATCH | ₹256.2 | ₹227.9 | held | ₹279.1 | +8.9% |
| GALLANTT | WATCH | ₹548.6 | ₹467.2 | held | ₹546.4 | -0.4% |
| RENUKA | WATCH | ₹27.5 | ₹22.1 | held | ₹24.9 | -9.6% |
| IRB | WATCH | ₹22.1 | ₹19.0 | held | ₹19.6 | -11.3% |
| CARBORUNIV | SELL | ₹775.7 | — | held | ₹1,075.2 | +38.6% |
| AIAENG | SELL | ₹3,636.6 | — | held | ₹4,096.6 | +12.6% |
| KNRCON | SELL | ₹113.0 | — | held | ₹125.7 | +11.2% |
| DBL | SELL | ₹387.2 | — | held | ₹403.4 | +4.2% |
| SAMMAANCAP | SELL | ₹149.5 | — | held | ₹147.3 | -1.5% |
| UTIAMC | SELL | ₹937.4 | — | held | ₹910.0 | -2.9% |
| DMART | SELL | ₹3,956.8 | — | held | ₹3,688.0 | -6.8% |

**The scorecard, 25 deep-dived picks, 5.4 months forward:**

- **BUY / ACCUMULATE (5):** average **+14.4%** with initial stops honoured, vs the Nifty 50's +4.8% — 4 of 5 positive, one stopped out (TRAVELFOOD, −14.9%, the stop doing its job of capping the loss).
- **WATCH (13):** average raw move **+21.7%** — the watchlist carried real winners (ABDL +56.5%, EIEL +47.5%, WEWORK +47.2%); this walk-forward did not evaluate their buy-above triggers, so none of that is claimed as system return.
- **SELL (7):** average subsequent move **+7.9%** — mixed: DMART, UTIAMC and SAMMAANCAP fell after the exit as the red flag predicted, but CARBORUNIV (+38.6%) and AIAENG (+12.6%) rallied — breakdown exits protect capital at the cost of some recoveries.

*Honest limits of this evaluation: statements were cut at FY Mar 2026 although those annuals would not all have been public on 31 March; stops were not ratcheted weekly as the live rhythm would; no transaction costs; one 5.4-month window is one sample, not proof.*

## The weekly-ratcheting walk-forward (2026-03-31 → 2026-09-11)

*The SAME picks as the as-of run — the stocks were never re-chosen. Rules replayed exactly as the skill prescribes: a standing stop checked DAILY (a low at the stop exits at the stop price); a WEEKLY run on each week's last trading day that re-seals boxes on the trailing six months and ratchets the stop up — never down — when a higher box seals, and exits at that day's close when the state is BREAKDOWN (the skill's SELL signal); WATCH picks enter on their own instruction, the first daily close above their box top. Prices are the two archives stitched with a verified seam. No re-entry, no costs.*

### The complete trade blotter, in date order

```
2026-03-30  AFFLE       BUY at ₹1,449.10 (BUY as of 2026-03-31; initial stop ₹1,218.69)
2026-03-30  ASKAUTOLTD  BUY at ₹444.75 (BUY as of 2026-03-31; initial stop ₹382.58)
2026-03-30  PHOENIXLTD  BUY at ₹1,506.30 (ACCUMULATE as of 2026-03-31; initial stop ₹1,415.11)
2026-03-30  THERMAX     BUY at ₹3,260.70 (ACCUMULATE as of 2026-03-31; initial stop ₹2,960.84)
2026-03-30  TRAVELFOOD  BUY at ₹1,261.80 (BUY as of 2026-03-31; initial stop ₹1,074.30)
2026-04-01  EIEL        BUY at ₹163.57 (WATCH trigger: first close above the ₹163.50 box top; initial stop ₹126.07)
2026-04-01  EPL         BUY at ₹215.23 (WATCH trigger: first close above the ₹205.77 box top; initial stop ₹167.59)
2026-04-01  RENUKA      BUY at ₹28.09 (WATCH trigger: first close above the ₹26.00 box top; initial stop ₹22.11)
2026-04-06  SAIL        BUY at ₹160.44 (WATCH trigger: first close above the ₹158.54 box top; initial stop ₹137.38)
2026-04-07  SHYAMMETL   BUY at ₹821.85 (WATCH trigger: first close above the ₹821.05 box top; initial stop ₹731.42)
2026-04-08  ABDL        BUY at ₹457.15 (WATCH trigger: first close above the ₹432.55 box top; initial stop ₹366.97)
2026-04-10  AFFLE       SELL at ₹1,401.60 — weekly SELL signal (closed below its box) (-3.3%)
2026-04-10  ARVINDFASN  BUY at ₹481.50 (WATCH trigger: first close above the ₹470.50 box top; initial stop ₹340.50)
2026-04-10  ASKAUTOLTD  RAISE STOP ₹382.58 → ₹411.81 (new box ₹422.00–₹455.95 sealed)
2026-04-10  RENUKA      RAISE STOP ₹22.11 → ₹26.49 (new box ₹27.05–₹28.93 sealed)
2026-04-10  TRAVELFOOD  RAISE STOP ₹1,074.30 → ₹1,222.47 (new box ₹1,239.90–₹1,298.00 sealed)
2026-04-10  URBANCO     BUY at ₹134.52 (WATCH trigger: first close above the ₹131.44 box top; initial stop ₹102.57)
2026-04-13  GALLANTT    BUY at ₹678.85 (WATCH trigger: first close above the ₹674.75 box top; initial stop ₹467.21)
2026-04-17  GALLANTT    RAISE STOP ₹467.21 → ₹624.90 (new box ₹645.00–₹712.00 sealed)
2026-04-17  SHYAMMETL   RAISE STOP ₹731.42 → ₹797.33 (new box ₹811.10–₹857.00 sealed)
2026-04-24  EIEL        RAISE STOP ₹126.07 → ₹193.99 (new box ₹201.10–₹224.79 sealed)
2026-04-24  GALLANTT    SELL at ₹828.70 — weekly SELL signal (closed below its box) (+22.1%)
2026-04-27  WEWORK      BUY at ₹566.80 (WATCH trigger: first close above the ₹552.80 box top; initial stop ₹381.46)
2026-05-01  EPL         RAISE STOP ₹167.59 → ₹213.94 (new box ₹220.14–₹240.80 sealed)
2026-05-01  URBANCO     RAISE STOP ₹102.57 → ₹138.39 (new box ₹141.16–₹150.39 sealed)
2026-05-08  ABDL        RAISE STOP ₹366.97 → ₹506.10 (new box ₹525.00–₹588.00 sealed)
2026-05-08  ARVINDFASN  RAISE STOP ₹340.50 → ₹405.09 (new box ₹424.05–₹487.25 sealed)
2026-05-08  PHOENIXLTD  RAISE STOP ₹1,415.11 → ₹1,694.50 (new box ₹1,726.90–₹1,834.90 sealed)
2026-05-08  SAIL        RAISE STOP ₹137.38 → ₹176.88 (new box ₹179.70–₹189.10 sealed)
2026-05-08  SHYAMMETL   RAISE STOP ₹797.33 → ₹851.40 (new box ₹864.60–₹908.60 sealed)
2026-05-08  THERMAX     RAISE STOP ₹2,960.84 → ₹3,807.75 (new box ₹3,922.50–₹4,305.00 sealed)
2026-05-08  URBANCO     SELL at ₹138.39 — stop hit (+2.9%)
2026-05-08  WEWORK      RAISE STOP ₹381.46 → ₹515.01 (new box ₹528.05–₹571.50 sealed)
2026-05-11  RENUKA      SELL at ₹26.49 — stop hit (-5.7%)
2026-05-11  TRAVELFOOD  SELL at ₹1,222.47 — stop hit (-3.1%)
2026-05-11  WEWORK      SELL at ₹515.01 — stop hit (-9.1%)
2026-05-12  SAIL        SELL at ₹176.88 — stop hit (+10.2%)
2026-05-12  SHYAMMETL   SELL at ₹851.40 — stop hit (+3.6%)
2026-05-14  EIEL        SELL at ₹193.99 — stop hit (+18.6%)
2026-05-15  EPL         SELL at ₹213.94 — stop hit (-0.6%)
2026-05-15  THERMAX     RAISE STOP ₹3,807.75 → ₹4,258.47 (new box ₹4,401.90–₹4,880.00 sealed)
2026-05-18  PHOENIXLTD  SELL at ₹1,694.50 — stop hit (+12.5%)
2026-05-19  ABDL        SELL at ₹506.10 — stop hit (+10.7%)
2026-05-21  IRB         BUY at ₹22.84 (WATCH trigger: first close above the ₹22.46 box top; initial stop ₹19.03)
2026-05-22  THERMAX     SELL at ₹4,454.60 — weekly SELL signal (closed below its box) (+36.6%)
2026-06-05  IRB         RAISE STOP ₹19.03 → ₹19.91 (new box ₹20.84–₹23.95 sealed)
2026-06-12  IRB         SELL at ₹20.81 — weekly SELL signal (closed below its box) (-8.9%)
2026-06-30  JLHL        BUY at ₹284.18 (WATCH trigger: first close above the ₹279.30 box top; initial stop ₹227.90)
2026-07-03  ASKAUTOLTD  SELL at ₹454.65 — weekly SELL signal (closed below its box) (+2.2%)
2026-07-24  JLHL        RAISE STOP ₹227.90 → ₹302.83 (new box ₹306.00–₹316.58 sealed)
2026-08-11  JLHL        SELL at ₹302.83 — stop hit (+6.6%)
2026-09-11  ARVINDFASN  STILL HELD at ₹446.50 — held through the period (-7.3%)
```

### The core positions: initial stop vs the weekly ratchet

| Stock | Entry (₹) | Initial stop | Buy & hold | Initial-stop only | WEEKLY RATCHET | Ratchets | Final stop | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| AFFLE | 1,449.1 | 1,218.7 | +8.2% | +8.2% | **-3.3%** | 0 | ₹1,218.7 | weekly SELL signal (closed below its box), 2026-04-10 |
| ASKAUTOLTD | 444.8 | 382.6 | +40.4% | +40.4% | **+2.2%** | 1 | ₹411.8 | weekly SELL signal (closed below its box), 2026-07-03 |
| PHOENIXLTD | 1,506.3 | 1,415.1 | +25.5% | +25.5% | **+12.5%** | 1 | ₹1,694.5 | stop hit, 2026-05-18 |
| THERMAX | 3,260.7 | 2,960.8 | +12.9% | +12.9% | **+36.6%** | 2 | ₹4,258.5 | weekly SELL signal (closed below its box), 2026-05-22 |
| TRAVELFOOD | 1,261.8 | 1,074.3 | -0.6% | -14.9% | **-3.1%** | 1 | ₹1,222.5 | stop hit, 2026-05-11 |

**Averages (5 core positions):** buy & hold +17.3% · initial-stop only +14.4% · weekly ratchet **+9.0%**.

### The WATCH picks, traded by their own instruction

12 of 12 WATCH picks closed above their box top and became buys:

| Stock | Buy above | Entry date | Entry (₹) | WEEKLY RATCHET | Ratchets | Exit |
|---|---:|---|---:|---:|---:|---|
| ABDL | 432.6 | 2026-04-08 | 457.1 | **+10.7%** | 1 | stop hit, 2026-05-19 |
| ARVINDFASN | 470.5 | 2026-04-10 | 481.5 | **-7.3%** | 1 | held through the period, 2026-09-11 |
| EIEL | 163.5 | 2026-04-01 | 163.6 | **+18.6%** | 1 | stop hit, 2026-05-14 |
| EPL | 205.8 | 2026-04-01 | 215.2 | **-0.6%** | 1 | stop hit, 2026-05-15 |
| GALLANTT | 674.8 | 2026-04-13 | 678.9 | **+22.1%** | 1 | weekly SELL signal (closed below its box), 2026-04-24 |
| IRB | 22.5 | 2026-05-21 | 22.8 | **-8.9%** | 1 | weekly SELL signal (closed below its box), 2026-06-12 |
| JLHL | 279.3 | 2026-06-30 | 284.2 | **+6.6%** | 1 | stop hit, 2026-08-11 |
| RENUKA | 26.0 | 2026-04-01 | 28.1 | **-5.7%** | 1 | stop hit, 2026-05-11 |
| SAIL | 158.5 | 2026-04-06 | 160.4 | **+10.2%** | 1 | stop hit, 2026-05-12 |
| SHYAMMETL | 821.0 | 2026-04-07 | 821.9 | **+3.6%** | 2 | stop hit, 2026-05-12 |
| URBANCO | 131.4 | 2026-04-10 | 134.5 | **+2.9%** | 1 | stop hit, 2026-05-08 |
| WEWORK | 552.8 | 2026-04-27 | 566.8 | **-9.1%** | 1 | stop hit, 2026-05-11 |

**Average over the 12 triggered WATCH trades: +3.6%**.

**The whole system under the rhythm — 17 trades taken: average +5.2%, 10 of 17 positive, vs the Nifty 50's +4.8% over the same period.**

*Honest limits: entries at the daily close that triggered (no slippage), stop exits assume a fill at the stop price, no costs, one period is one sample.*

## Re-entry after a stop-out (2026-03-31 → 2026-09-11)

*Same stocks, same rhythm, ONE new rule: after a stop-out or weekly SELL, the stock is re-bought on the first day BOTH of the skill's own signals say go — boxes re-sealed on the trailing six months put it in BREAKOUT (or RECOVERY), AND the weekly volume trigger fires again as of that day (latest week, pro-rated if running, at ≥1.5× the prior 12 completed weeks with the weekly price up). A RECOVERY re-entry starts with no stop until its first box seals — a stale box gives no honest stop. Each stock's slice of capital compounds through its own legs and sits idle between them.*

### The complete trade blotter with re-entries

```
2026-03-30  AFFLE       BUY at ₹1,449.10; stop ₹1,218.69
2026-03-30  ASKAUTOLTD  BUY at ₹444.75; stop ₹382.58
2026-03-30  PHOENIXLTD  BUY at ₹1,506.30; stop ₹1,415.11
2026-03-30  THERMAX     BUY at ₹3,260.70; stop ₹2,960.84
2026-03-30  TRAVELFOOD  BUY at ₹1,261.80; stop ₹1,074.30
2026-04-01  EIEL        BUY at ₹163.57; stop ₹126.07
2026-04-01  EPL         BUY at ₹215.23; stop ₹167.59
2026-04-01  RENUKA      BUY at ₹28.09; stop ₹22.11
2026-04-06  SAIL        BUY at ₹160.44; stop ₹137.38
2026-04-07  SHYAMMETL   BUY at ₹821.85; stop ₹731.42
2026-04-08  ABDL        BUY at ₹457.15; stop ₹366.97
2026-04-10  AFFLE       SELL at ₹1,401.60 — weekly SELL signal (closed below its box) (-3.3%)
2026-04-10  ARVINDFASN  BUY at ₹481.50; stop ₹340.50
2026-04-10  ASKAUTOLTD  RAISE STOP ₹382.58 → ₹411.81
2026-04-10  RENUKA      RAISE STOP ₹22.11 → ₹26.49
2026-04-10  TRAVELFOOD  RAISE STOP ₹1,074.30 → ₹1,222.47
2026-04-10  URBANCO     BUY at ₹134.52; stop ₹102.57
2026-04-13  GALLANTT    BUY at ₹678.85; stop ₹467.21
2026-04-17  GALLANTT    RAISE STOP ₹467.21 → ₹624.90
2026-04-17  SHYAMMETL   RAISE STOP ₹731.42 → ₹797.33
2026-04-24  EIEL        RAISE STOP ₹126.07 → ₹193.99
2026-04-24  GALLANTT    SELL at ₹828.70 — weekly SELL signal (closed below its box) (+22.1%)
2026-04-27  WEWORK      BUY at ₹566.80; stop ₹381.46
2026-05-01  EPL         RAISE STOP ₹167.59 → ₹213.94
2026-05-01  URBANCO     RAISE STOP ₹102.57 → ₹138.39
2026-05-08  ABDL        RAISE STOP ₹366.97 → ₹506.10
2026-05-08  ARVINDFASN  RAISE STOP ₹340.50 → ₹405.09
2026-05-08  PHOENIXLTD  RAISE STOP ₹1,415.11 → ₹1,694.50
2026-05-08  SAIL        RAISE STOP ₹137.38 → ₹176.88
2026-05-08  SHYAMMETL   RAISE STOP ₹797.33 → ₹851.40
2026-05-08  THERMAX     RAISE STOP ₹2,960.84 → ₹3,807.75
2026-05-08  URBANCO     SELL at ₹138.39 — stop hit (+2.9%)
2026-05-08  WEWORK      RAISE STOP ₹381.46 → ₹515.01
2026-05-11  AFFLE       RE-ENTER at ₹1,637.50; stop ₹1,350.93
2026-05-11  RENUKA      SELL at ₹26.49 — stop hit (-5.7%)
2026-05-11  TRAVELFOOD  SELL at ₹1,222.47 — stop hit (-3.1%)
2026-05-11  WEWORK      SELL at ₹515.01 — stop hit (-9.1%)
2026-05-12  SAIL        SELL at ₹176.88 — stop hit (+10.2%)
2026-05-12  SHYAMMETL   SELL at ₹851.40 — stop hit (+3.6%)
2026-05-13  SAIL        RE-ENTER at ₹201.31; no stop until the first box seals
2026-05-14  EIEL        SELL at ₹193.99 — stop hit (+18.6%)
2026-05-15  EPL         SELL at ₹213.94 — stop hit (-0.6%)
2026-05-15  THERMAX     RAISE STOP ₹3,807.75 → ₹4,258.47
2026-05-18  PHOENIXLTD  SELL at ₹1,694.50 — stop hit (+12.5%)
2026-05-19  ABDL        SELL at ₹506.10 — stop hit (+10.7%)
2026-05-20  SHYAMMETL   RE-ENTER at ₹922.60; no stop until the first box seals
2026-05-21  IRB         BUY at ₹22.84; stop ₹19.03
2026-05-21  WEWORK      RE-ENTER at ₹573.90; stop ₹460.76
2026-05-22  SAIL        RAISE STOP — → ₹181.76
2026-05-22  THERMAX     SELL at ₹4,454.60 — weekly SELL signal (closed below its box) (+36.6%)
2026-05-25  EIEL        RE-ENTER at ₹209.69; stop ₹179.52
2026-05-27  TRAVELFOOD  RE-ENTER at ₹1,221.90; stop ₹990.50
2026-05-29  THERMAX     RE-ENTER at ₹4,982.70; no stop until the first box seals
2026-05-29  WEWORK      RAISE STOP ₹460.76 → ₹523.21
2026-06-05  IRB         RAISE STOP ₹19.03 → ₹19.91
2026-06-05  SHYAMMETL   RAISE STOP — → ₹946.50
2026-06-05  THERMAX     SELL at ₹4,832.10 — weekly SELL signal (closed below its box) (-3.0%)
2026-06-08  EIEL        SELL at ₹179.52 — stop hit (-14.4%)
2026-06-10  SAIL        SELL at ₹181.76 — stop hit (-9.7%)
2026-06-12  ABDL        RE-ENTER at ₹644.45; stop ₹476.69
2026-06-12  IRB         SELL at ₹20.81 — weekly SELL signal (closed below its box) (-8.9%)
2026-06-12  TRAVELFOOD  RAISE STOP ₹990.50 → ₹1,121.80
2026-06-15  RENUKA      RE-ENTER at ₹24.06; stop ₹20.42
2026-06-16  PHOENIXLTD  RE-ENTER at ₹1,868.20; stop ₹1,637.63
2026-06-19  ABDL        RAISE STOP ₹476.69 → ₹610.87
2026-06-19  SHYAMMETL   SELL at ₹970.30 — weekly SELL signal (closed below its box) (+5.2%)
2026-06-19  WEWORK      SELL at ₹630.55 — weekly SELL signal (closed below its box) (+9.9%)
2026-06-22  EIEL        RE-ENTER at ₹224.91; no stop until the first box seals
2026-06-23  ABDL        SELL at ₹610.87 — stop hit (-5.2%)
2026-06-29  ABDL        RE-ENTER at ₹659.50; stop ₹610.87
2026-06-29  SAIL        RE-ENTER at ₹175.23; stop ₹162.65
2026-06-29  THERMAX     RE-ENTER at ₹5,125.10; stop ₹4,370.79
2026-06-30  JLHL        BUY at ₹284.18; stop ₹227.90
2026-06-30  WEWORK      RE-ENTER at ₹689.30; no stop until the first box seals
2026-07-03  AFFLE       SELL at ₹1,464.60 — weekly SELL signal (closed below its box) (-10.6%)
2026-07-03  ASKAUTOLTD  SELL at ₹454.65 — weekly SELL signal (closed below its box) (+2.2%)
2026-07-03  EIEL        RAISE STOP — → ₹205.88
2026-07-03  RENUKA      RAISE STOP ₹20.42 → ₹21.20
2026-07-03  TRAVELFOOD  RAISE STOP ₹1,121.80 → ₹1,263.10
2026-07-06  EPL         RE-ENTER at ₹241.67; no stop until the first box seals
2026-07-07  ASKAUTOLTD  RE-ENTER at ₹467.95; stop ₹435.42
2026-07-08  SAIL        SELL at ₹162.65 — stop hit (-7.2%)
2026-07-10  EPL         SELL at ₹237.56 — weekly SELL signal (closed below its box) (-1.7%)
2026-07-13  AFFLE       RE-ENTER at ₹1,539.30; stop ₹1,422.64
2026-07-13  SHYAMMETL   RE-ENTER at ₹1,029.35; no stop until the first box seals
2026-07-14  THERMAX     SELL at ₹4,370.79 — stop hit (-14.7%)
2026-07-17  ABDL        SELL at ₹610.87 — stop hit (-7.4%)
2026-07-17  ASKAUTOLTD  RAISE STOP ₹435.42 → ₹455.60
2026-07-17  EIEL        SELL at ₹220.23 — weekly SELL signal (closed below its box) (-2.1%)
2026-07-17  WEWORK      SELL at ₹677.95 — weekly SELL signal (closed below its box) (-1.6%)
2026-07-24  AFFLE       SELL at ₹1,422.64 — stop hit (-7.6%)
2026-07-24  JLHL        RAISE STOP ₹227.90 → ₹302.83
2026-07-24  RENUKA      SELL at ₹22.23 — weekly SELL signal (closed below its box) (-7.6%)
2026-07-24  TRAVELFOOD  SELL at ₹1,263.10 — stop hit (+3.4%)
2026-07-28  AFFLE       RE-ENTER at ₹1,631.80; no stop until the first box seals
2026-07-31  AFFLE       SELL at ₹1,586.00 — weekly SELL signal (closed below its box) (-2.8%)
2026-07-31  SHYAMMETL   RAISE STOP — → ₹986.46
2026-08-07  PHOENIXLTD  RAISE STOP ₹1,637.63 → ₹1,789.55
2026-08-07  SHYAMMETL   SELL at ₹986.46 — stop hit (-4.2%)
2026-08-07  TRAVELFOOD  RE-ENTER at ₹1,428.60; stop ₹1,241.80
2026-08-11  JLHL        SELL at ₹302.83 — stop hit (+6.6%)
2026-08-12  EPL         RE-ENTER at ₹243.64; stop ₹220.18
2026-08-14  ASKAUTOLTD  RAISE STOP ₹455.60 → ₹613.08
2026-08-17  RENUKA      RE-ENTER at ₹23.00; stop ₹21.22
2026-08-21  ASKAUTOLTD  SELL at ₹621.15 — weekly SELL signal (closed below its box) (+32.7%)
2026-08-21  EPL         RAISE STOP ₹220.18 → ₹236.22
2026-08-21  URBANCO     RE-ENTER at ₹158.60; stop ₹106.28
2026-08-25  SAIL        RE-ENTER at ₹184.59; stop ₹152.32
2026-08-28  SHYAMMETL   RE-ENTER at ₹1,099.80; stop ₹957.55
2026-09-02  EPL         SELL at ₹236.22 — stop hit (-3.0%)
2026-09-04  RENUKA      RAISE STOP ₹21.22 → ₹22.01
2026-09-04  SAIL        RAISE STOP ₹152.32 → ₹187.04
2026-09-04  SHYAMMETL   RAISE STOP ₹957.55 → ₹1,042.23
2026-09-08  SAIL        SELL at ₹187.04 — stop hit (+1.3%)
2026-09-09  EIEL        RE-ENTER at ₹206.06; stop ₹183.11
2026-09-10  IRB         RE-ENTER at ₹19.91; stop ₹18.48
2026-09-11  ARVINDFASN  STILL HELD at ₹446.50 — held through the period (-7.3%)
2026-09-11  EIEL        STILL HELD at ₹207.11 — held through the period (+0.5%)
2026-09-11  IRB         STILL HELD at ₹19.64 — held through the period (-1.4%)
2026-09-11  PHOENIXLTD  STILL HELD at ₹1,890.00 — held through the period (+1.2%)
2026-09-11  RENUKA      STILL HELD at ₹24.87 — held through the period (+8.1%)
2026-09-11  SHYAMMETL   STILL HELD at ₹1,074.80 — held through the period (-2.3%)
2026-09-11  TRAVELFOOD  STILL HELD at ₹1,253.60 — held through the period (-12.2%)
2026-09-11  URBANCO     STILL HELD at ₹166.89 — held through the period (+5.2%)
```

### Per stock: legs and the compounded result

| Stock | Legs | Leg returns | Compounded |
|---|---:|---|---:|
| ASKAUTOLTD | 2 | +2.2% → +32.7% | **+35.7%** |
| GALLANTT | 1 | +22.1% | **+22.1%** |
| PHOENIXLTD | 2 | +12.5% → +1.2% | **+13.8%** |
| THERMAX | 3 | +36.6% → -3.0% → -14.7% | **+13.0%** |
| URBANCO | 2 | +2.9% → +5.2% | **+8.3%** |
| JLHL | 1 | +6.6% | **+6.6%** |
| SHYAMMETL | 4 | +3.6% → +5.2% → -4.2% → -2.3% | **+2.0%** |
| EIEL | 4 | +18.6% → -14.4% → -2.1% → +0.5% | **-0.1%** |
| WEWORK | 3 | -9.1% → +9.9% → -1.6% | **-1.8%** |
| ABDL | 3 | +10.7% → -5.2% → -7.4% | **-2.8%** |
| EPL | 3 | -0.6% → -1.7% → -3.0% | **-5.3%** |
| RENUKA | 3 | -5.7% → -7.6% → +8.1% | **-5.8%** |
| SAIL | 4 | +10.2% → -9.7% → -7.2% → +1.3% | **-6.4%** |
| ARVINDFASN | 1 | -7.3% | **-7.3%** |
| IRB | 2 | -8.9% → -1.4% | **-10.1%** |
| TRAVELFOOD | 3 | -3.1% → +3.4% → -12.2% | **-12.1%** |
| AFFLE | 4 | -3.3% → -10.6% → -7.6% → -2.8% | **-22.3%** |

**28 re-entries were taken across 17 stocks; the re-entry legs alone averaged -1.8% (9 of 28 positive).**

**₹100 outcome (equal 1/17 slice per stock, each compounding through its own legs): ₹101.62 (+1.62%) — against ₹105.18 with no re-entry and ₹104.80 in the Nifty 50.**

*Same limits as before: close-price entries, stop-price fills, no costs, one period.*
