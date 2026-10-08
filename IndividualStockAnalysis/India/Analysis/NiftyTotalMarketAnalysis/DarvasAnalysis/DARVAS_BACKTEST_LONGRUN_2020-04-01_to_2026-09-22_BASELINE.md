# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 1388 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹342.79** | **+20.98% a year** |
| The same system before costs and taxes | ₹415.96 | +24.65% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹289.64 | +17.87% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹342.79** (+20.98% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 419 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹15.87** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹49.53**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹36.02 | ₹0.00 | ₹7.2042 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹29.10 | ₹0.00 | ₹5.8207 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹50.50 | ₹44.32 | ₹15.6403 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹104.35 | ₹0.00 | ₹20.8698 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹9.09 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹13.14 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹4.29 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 140.43 | +40.4% | +41.1% | +70.1% |
| 2021 (2021-12-31) | 201.18 | +43.3% | +47.3% | +26.2% |
| 2022 (2022-12-30) | 262.10 | +30.3% | +32.5% | +4.3% |
| 2023 (2023-12-29) | 353.22 | +34.8% | +44.2% | +20.0% |
| 2024 (2024-12-27) | 340.45 | -3.6% | +1.5% | +9.6% |
| 2025 (2025-12-26) | 328.07 | -3.6% | -2.4% | +9.4% |
| 2026 (2026-09-22) | 342.79 | +4.5% | +5.7% | -10.1% |

## What it took to earn it

- **Maximum drawdown: -27.1%** (peak 2024-07-05 → trough 2026-04-02, on weekly closes).
- **201 closed trades**: 87 winners (43%), average winner +31.2%, average loser -10.3%.
- Best closed trade ANANDRATHI +224.7%; worst IOB -31.5%.
- Median holding period 63 days.
- Cash share of equity averaged 11% across all weeks (median 4%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.20 | 59.96 | 4 |
| 2020-05-29 | 103.00 | 0.00 | 10 |
| 2020-06-26 | 117.13 | 0.00 | 10 |
| 2020-07-31 | 120.76 | 0.00 | 10 |
| 2020-08-28 | 124.69 | 0.00 | 10 |
| 2020-09-25 | 125.00 | 25.12 | 7 |
| 2020-10-30 | 119.57 | 0.00 | 9 |
| 2020-11-27 | 122.87 | 0.00 | 10 |
| 2020-12-24 | 140.43 | 29.69 | 8 |
| 2021-01-29 | 137.33 | 34.67 | 8 |
| 2021-02-26 | 149.25 | 19.06 | 9 |
| 2021-03-26 | 149.00 | 15.71 | 9 |
| 2021-04-30 | 149.04 | 0.00 | 10 |
| 2021-05-28 | 163.04 | 0.00 | 10 |
| 2021-06-25 | 178.17 | 0.00 | 10 |
| 2021-07-30 | 209.66 | 0.00 | 10 |
| 2021-08-27 | 202.93 | 0.00 | 10 |
| 2021-09-24 | 202.61 | 31.47 | 8 |
| 2021-10-29 | 200.85 | 40.42 | 8 |
| 2021-11-26 | 205.29 | 74.70 | 6 |
| 2021-12-31 | 201.18 | 2.45 | 10 |
| 2022-01-28 | 204.47 | 37.39 | 8 |
| 2022-02-25 | 193.35 | 67.55 | 6 |
| 2022-03-25 | 208.27 | 26.11 | 8 |
| 2022-04-29 | 225.55 | 0.00 | 9 |
| 2022-05-27 | 228.20 | 1.29 | 8 |
| 2022-06-24 | 222.21 | 37.27 | 7 |
| 2022-07-29 | 240.95 | 0.00 | 9 |
| 2022-08-26 | 251.88 | 5.39 | 9 |
| 2022-09-30 | 250.57 | 34.55 | 8 |
| 2022-10-28 | 256.33 | 6.43 | 9 |
| 2022-11-25 | 276.07 | 4.75 | 9 |
| 2022-12-30 | 262.10 | 108.13 | 6 |
| 2023-01-27 | 262.16 | 0.00 | 10 |
| 2023-02-24 | 262.45 | 0.00 | 10 |
| 2023-03-31 | 248.91 | 107.64 | 6 |
| 2023-04-28 | 242.00 | 47.14 | 8 |
| 2023-05-26 | 245.58 | 16.20 | 9 |
| 2023-06-30 | 250.64 | 0.00 | 10 |
| 2023-07-28 | 265.96 | 0.00 | 10 |
| 2023-08-25 | 291.41 | 0.00 | 10 |
| 2023-09-29 | 297.53 | 28.00 | 9 |
| 2023-10-27 | 300.03 | 81.02 | 7 |
| 2023-11-24 | 334.25 | 4.30 | 10 |
| 2023-12-29 | 353.22 | 0.00 | 10 |
| 2024-01-25 | 368.98 | 0.00 | 11 |
| 2024-02-23 | 379.18 | 14.19 | 10 |
| 2024-03-28 | 371.59 | 81.33 | 9 |
| 2024-04-26 | 376.36 | 0.00 | 11 |
| 2024-05-31 | 379.25 | 74.36 | 9 |
| 2024-06-28 | 379.52 | 0.00 | 11 |
| 2024-07-26 | 382.22 | 35.43 | 10 |
| 2024-08-30 | 368.70 | 0.00 | 11 |
| 2024-09-27 | 360.18 | 0.00 | 11 |
| 2024-10-25 | 327.74 | 134.56 | 7 |
| 2024-11-29 | 349.62 | 0.00 | 11 |
| 2024-12-27 | 340.45 | 71.84 | 9 |
| 2025-01-31 | 315.05 | 142.65 | 6 |
| 2025-02-28 | 295.85 | 166.28 | 5 |
| 2025-03-27 | 318.40 | 97.83 | 7 |
| 2025-04-25 | 319.11 | 117.09 | 6 |
| 2025-05-30 | 333.83 | 0.00 | 10 |
| 2025-06-27 | 352.71 | 0.00 | 10 |
| 2025-07-25 | 360.07 | 0.00 | 10 |
| 2025-08-29 | 348.01 | 40.23 | 9 |
| 2025-09-26 | 333.51 | 68.38 | 8 |
| 2025-10-31 | 321.95 | 12.73 | 11 |
| 2025-11-28 | 330.03 | 64.09 | 9 |
| 2025-12-26 | 328.07 | 19.74 | 10 |
| 2026-01-30 | 317.73 | 173.98 | 5 |
| 2026-02-27 | 301.23 | 81.02 | 8 |
| 2026-03-27 | 286.52 | 141.14 | 6 |
| 2026-04-30 | 310.46 | 13.22 | 10 |
| 2026-05-29 | 327.38 | 0.00 | 11 |
| 2026-06-25 | 321.94 | 0.00 | 11 |
| 2026-07-31 | 331.55 | 35.20 | 10 |
| 2026-08-28 | 347.53 | 0.00 | 11 |
| 2026-09-22 | 342.79 | 0.00 | 11 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| ACMESOLAR | 2026-09-21 | 439.00 | 458.65 | 370.12 | +4.5% |
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,777.30 | 2,376.52 | +39.6% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,392.00 | 1,242.60 | +40.7% |
| CRAFTSMAN | 2026-05-11 | 9,039.50 | 10,602.00 | 10,380.65 | +17.3% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| RUBICON | 2026-06-08 | 1,190.00 | 1,671.20 | 1,653.47 | +40.4% |
| SUBEX | 2020-10-19 | 15.55 | 16.95 | 11.11 | +9.0% |
| SUNDRMFAST | 2026-09-15 | 1,277.30 | 1,190.90 | 1,127.74 | -6.8% |
| TMB | 2026-08-03 | 864.90 | 883.75 | 817.00 | +2.2% |
| WOCKPHARMA | 2026-05-11 | 1,613.90 | 2,185.40 | 1,868.93 | +35.4% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| HATHWAY | 2020-05-18 | 24.50 | 2020-06-29 | 31.40 | +28.2% |
| VINDHYATEL | 2020-06-22 | 735.00 | 2020-07-23 | 667.14 | -9.2% |
| PANACEABIO | 2020-06-15 | 230.00 | 2020-08-20 | 184.01 | -20.0% |
| APCOTEXIND | 2020-08-24 | 164.95 | 2020-08-31 | 151.95 | -7.9% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| BDL | 2020-07-06 | 192.10 | 2020-09-08 | 168.93 | -12.1% |
| KIRLOSBROS | 2020-07-27 | 122.55 | 2020-09-08 | 120.79 | -1.4% |
| RCF | 2020-05-18 | 39.90 | 2020-09-09 | 45.84 | +14.9% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| SATIA | 2020-09-14 | 122.00 | 2020-09-22 | 102.97 | -15.6% |
| PRINCEPIPE | 2020-09-07 | 208.00 | 2020-10-12 | 220.88 | +6.2% |
| ALEMBICLTD | 2020-05-18 | 54.90 | 2020-11-02 | 91.41 | +66.5% |
| GLAXO | 2020-09-14 | 1,675.00 | 2020-11-02 | 1,441.55 | -13.9% |
| ADVENZYMES | 2020-05-18 | 159.95 | 2020-11-03 | 292.33 | +82.8% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| TCI | 2020-09-14 | 242.00 | 2020-12-22 | 234.75 | -3.0% |
| PILANIINVS | 2020-11-17 | 2,054.50 | 2021-01-04 | 2,132.80 | +3.8% |
| ITDC | 2020-12-28 | 338.55 | 2021-01-18 | 304.38 | -10.1% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| TRENT | 2020-11-17 | 503.33 | 2021-01-29 | 417.53 | -17.0% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| JINDWORLD | 2020-11-09 | 50.00 | 2021-03-01 | 52.12 | +4.2% |
| RCF | 2021-03-01 | 80.00 | 2021-03-17 | 79.16 | -1.1% |
| TATAMOTORS | 2021-01-25 | 296.90 | 2021-03-19 | 296.97 | +0.0% |
| APTECHT | 2021-02-01 | 178.45 | 2021-03-19 | 204.25 | +14.5% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| KKCL | 2021-01-11 | 985.00 | 2021-03-30 | 856.90 | -13.0% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| CENTRUM | 2021-03-30 | 28.40 | 2021-04-12 | 24.89 | -12.4% |
| GFLLIMITED | 2021-03-22 | 93.00 | 2021-04-13 | 74.39 | -20.0% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| SUPPETRO | 2021-04-26 | 670.90 | 2021-09-13 | 703.10 | +4.8% |
| GDL | 2021-01-25 | 158.00 | 2021-09-20 | 266.00 | +68.4% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| NEOGEN | 2021-09-27 | 1,255.00 | 2021-10-25 | 1,142.85 | -8.9% |
| EMAMIPAP | 2021-04-19 | 125.00 | 2021-11-22 | 141.55 | +13.2% |
| SHOPERSTOP | 2021-10-25 | 326.00 | 2021-11-22 | 335.82 | +3.0% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-11-01 | 11,040.00 | 2021-11-26 | 10,070.05 | -8.8% |
| SOMANYCERA | 2021-06-21 | 594.85 | 2021-11-29 | 755.11 | +26.9% |
| MAHLOG | 2021-01-25 | 495.85 | 2021-11-30 | 654.55 | +32.0% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| TVTODAY | 2021-11-29 | 328.80 | 2022-01-24 | 311.68 | -5.2% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| TV18BRDCST | 2022-01-31 | 58.90 | 2022-02-22 | 58.38 | -0.9% |
| CHAMBLFERT | 2021-12-06 | 407.45 | 2022-02-24 | 353.85 | -13.2% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| EXCELINDUS | 2022-03-07 | 1,523.00 | 2022-03-29 | 1,438.30 | -5.6% |
| RCF | 2022-04-04 | 96.40 | 2022-05-04 | 93.15 | -3.4% |
| INOXLEISUR | 2022-04-04 | 520.85 | 2022-05-06 | 470.35 | -9.7% |
| BAJAJHLDNG | 2021-09-27 | 4,979.00 | 2022-05-11 | 4,853.07 | -2.5% |
| MOL | 2022-05-09 | 129.80 | 2022-05-11 | 113.62 | -12.5% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| JSWENERGY | 2021-03-08 | 81.85 | 2022-06-20 | 201.99 | +146.8% |
| JKIL | 2022-05-09 | 229.70 | 2022-08-05 | 308.80 | +34.4% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| NAVNETEDUL | 2022-08-08 | 130.50 | 2022-09-26 | 127.30 | -2.5% |
| SUNDARMHLD | 2022-10-03 | 103.50 | 2022-10-11 | 92.20 | -10.9% |
| FAIRCHEMOR | 2022-10-17 | 2,240.00 | 2022-11-01 | 1,790.15 | -20.1% |
| APARINDS | 2022-06-27 | 1,004.00 | 2022-11-03 | 1,358.50 | +35.3% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| RVNL | 2022-11-07 | 46.85 | 2022-12-26 | 60.57 | +29.3% |
| TIINDIA | 2022-07-25 | 2,135.00 | 2023-01-11 | 2,598.34 | +21.7% |
| GICRE | 2023-01-02 | 179.20 | 2023-02-01 | 167.72 | -6.4% |
| LSIL | 2023-01-16 | 19.35 | 2023-02-07 | 20.04 | +3.6% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| SUNFLAG | 2023-01-02 | 113.00 | 2023-02-27 | 129.20 | +14.3% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| IOB | 2023-01-02 | 32.40 | 2023-03-20 | 22.18 | -31.5% |
| JINDALSAW | 2023-02-06 | 65.22 | 2023-03-27 | 67.92 | +4.1% |
| WONDERLA | 2023-03-06 | 456.00 | 2023-03-27 | 384.27 | -15.7% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| CIGNITITEC | 2023-02-20 | 731.95 | 2023-03-29 | 705.14 | -3.7% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| KIRLOSBROS | 2023-04-10 | 425.00 | 2023-04-26 | 403.85 | -5.0% |
| MUKANDLTD | 2023-01-02 | 136.70 | 2023-05-17 | 116.23 | -15.0% |
| FAIRCHEMOR | 2023-05-02 | 1,272.00 | 2023-05-19 | 1,141.04 | -10.3% |
| VSSL | 2023-04-10 | 414.00 | 2023-05-26 | 324.52 | -21.6% |
| ANURAS | 2023-03-27 | 867.00 | 2023-07-03 | 1,007.67 | +16.2% |
| KSB | 2023-03-27 | 417.98 | 2023-07-12 | 407.74 | -2.4% |
| THANGAMAYL | 2023-05-29 | 1,344.00 | 2023-07-17 | 1,344.25 | +0.0% |
| GANESHHOUC | 2023-07-24 | 457.00 | 2023-08-14 | 418.62 | -8.4% |
| NEULANDLAB | 2023-05-22 | 2,831.90 | 2023-09-13 | 3,457.30 | +22.1% |
| KIRLOSIND | 2023-04-10 | 2,724.00 | 2023-09-25 | 3,202.97 | +17.6% |
| SJVN | 2023-09-18 | 75.35 | 2023-10-23 | 66.03 | -12.4% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| SHARDAMOTR | 2023-05-22 | 380.00 | 2023-10-25 | 465.07 | +22.4% |
| GENUSPOWER | 2023-07-10 | 162.85 | 2023-11-16 | 234.03 | +43.7% |
| ISMTLTD | 2023-11-20 | 94.60 | 2023-12-20 | 88.35 | -6.6% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| MMFL | 2023-12-26 | 1,023.60 | 2024-01-30 | 912.05 | -10.9% |
| ASTRAZEN | 2023-08-21 | 4,099.85 | 2024-02-09 | 5,795.95 | +41.4% |
| RVNL | 2024-01-23 | 332.00 | 2024-02-12 | 241.04 | -27.4% |
| GLS | 2023-05-02 | 509.05 | 2024-03-05 | 779.48 | +53.1% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| TCI | 2024-02-05 | 987.60 | 2024-03-11 | 790.40 | -20.0% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| DOLLAR | 2024-03-11 | 527.95 | 2024-03-13 | 461.65 | -12.6% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| ANANDRATHI | 2023-07-17 | 265.70 | 2024-03-27 | 862.65 | +224.7% |
| PILANIINVS | 2023-10-03 | 2,380.05 | 2024-05-09 | 3,710.37 | +55.9% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| DMART | 2024-04-01 | 4,570.00 | 2024-05-31 | 4,322.83 | -5.4% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| BOSCHLTD | 2024-03-18 | 29,500.05 | 2024-06-04 | 29,015.09 | -1.6% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| THERMAX | 2024-06-03 | 5,640.00 | 2024-08-05 | 4,719.70 | -16.3% |
| JWL | 2024-05-13 | 490.00 | 2024-08-06 | 552.00 | +12.7% |
| EMUDHRA | 2024-03-18 | 583.90 | 2024-08-13 | 793.11 | +35.8% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| CERA | 2024-08-12 | 10,499.95 | 2024-09-19 | 8,198.93 | -21.9% |
| IOB | 2024-02-12 | 71.50 | 2024-10-03 | 56.57 | -20.9% |
| DABUR | 2024-06-10 | 604.20 | 2024-10-03 | 602.49 | -0.3% |
| VGUARD | 2024-08-19 | 524.15 | 2024-10-04 | 420.24 | -19.8% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| ALKYLAMINE | 2024-09-23 | 2,432.85 | 2024-10-22 | 2,106.24 | -13.4% |
| INDIAGLYCO | 2024-07-22 | 515.00 | 2024-10-25 | 587.91 | +14.2% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| KIRLPNU | 2024-11-04 | 1,698.00 | 2024-12-23 | 1,596.00 | -6.0% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| PAYTM | 2024-10-28 | 747.70 | 2025-01-09 | 893.05 | +19.4% |
| GARFIBRES | 2024-11-25 | 956.00 | 2025-01-09 | 829.35 | -13.2% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| CARERATING | 2024-10-28 | 1,396.00 | 2025-01-13 | 1,239.70 | -11.2% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| BSE | 2024-10-14 | 4,536.00 | 2025-02-28 | 4,954.63 | +9.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| AVANTIFEED | 2025-03-17 | 842.55 | 2025-04-07 | 648.95 | -23.0% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| ITDCEM | 2024-10-07 | 655.05 | 2025-04-11 | 524.92 | -19.9% |
| PARAS | 2025-05-05 | 1,372.20 | 2025-07-04 | 1,417.98 | +3.3% |
| JSWHL | 2024-11-11 | 15,500.00 | 2025-08-04 | 19,106.01 | +23.3% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| WHIRLPOOL | 2025-04-28 | 1,153.90 | 2025-08-07 | 1,301.97 | +12.8% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| RSYSTEMS | 2025-09-01 | 460.00 | 2025-09-24 | 423.23 | -8.0% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| KIMS | 2025-04-28 | 679.50 | 2025-10-03 | 680.34 | +0.1% |
| FORCEMOT | 2025-04-28 | 9,275.00 | 2025-10-09 | 15,350.10 | +65.5% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| PGHL | 2025-08-11 | 6,345.00 | 2025-11-06 | 5,938.45 | -6.4% |
| ASTRAMICRO | 2025-10-06 | 1,119.85 | 2025-11-06 | 1,026.00 | -8.4% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| SKYGOLD | 2025-10-27 | 370.00 | 2025-11-25 | 329.13 | -11.0% |
| RAMKY | 2025-10-13 | 622.35 | 2025-12-01 | 578.17 | -7.1% |
| ASTERDM | 2025-07-07 | 633.90 | 2025-12-05 | 643.62 | +1.5% |
| SHAILY | 2025-10-13 | 2,434.00 | 2025-12-15 | 2,340.80 | -3.8% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| KIRLOSENG | 2025-12-08 | 1,130.00 | 2026-01-12 | 1,140.95 | +1.0% |
| LGBBROSLTD | 2025-09-29 | 1,411.60 | 2026-01-20 | 1,713.80 | +21.4% |
| NATCOPHARM | 2025-12-08 | 934.70 | 2026-01-20 | 825.79 | -11.7% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| HAPPYFORGE | 2026-02-23 | 1,370.00 | 2026-03-04 | 1,234.05 | -9.9% |
| VSTTILLERS | 2025-08-18 | 5,260.00 | 2026-03-05 | 5,425.45 | +3.1% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| HINDCOPPER | 2025-12-29 | 545.05 | 2026-03-12 | 528.63 | -3.0% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-02 | 116.20 | 2026-03-23 | 110.67 | -4.8% |
| TORNTPOWER | 2026-03-02 | 1,491.00 | 2026-03-30 | 1,315.84 | -11.7% |
| KSB | 2026-03-02 | 738.00 | 2026-05-04 | 917.42 | +24.3% |
| INOXINDIA | 2026-04-13 | 1,299.10 | 2026-05-13 | 1,372.18 | +5.6% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| GALLANTT | 2026-04-20 | 862.10 | 2026-05-14 | 783.75 | -9.1% |
| E2E | 2026-02-23 | 2,914.00 | 2026-06-05 | 2,330.72 | -20.0% |
| NLCINDIA | 2026-05-18 | 351.55 | 2026-06-09 | 320.62 | -8.8% |
| THERMAX | 2026-04-13 | 3,596.00 | 2026-07-29 | 4,306.64 | +19.8% |
| SFL | 2026-06-15 | 724.95 | 2026-08-06 | 698.73 | -3.6% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-02-23 | 6,090.00 | 2026-09-15 | 7,158.25 | +17.5% |
| ASKAUTOLTD | 2026-08-10 | 648.95 | 2026-09-16 | 598.78 | -7.7% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_BASELINE.csv` beside this report (23582 events in all).*

```
2020-04-13  DEEPAKNTR   BUY ₹10.00 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 2.47×, ladder rising; stop ₹240.25; charges ₹0.0118)
2020-04-27  CADILAHC    BUY ₹10.01 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 5.12×, ladder rising; stop ₹310.03; charges ₹0.0119)
2020-04-27  SYNGENE     BUY ₹10.02 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.94×, ladder rising; stop ₹285.95; charges ₹0.0119)
2020-04-27  TAJGVK      BUY ₹10.01 at ₹133.40 (fresh Friday signal — BUY: 6.65× weekly, month 2.23×, ladder rising; stop ₹106.49; charges ₹0.0119)
2020-05-11  APLLTD      BUY ₹9.98 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.70× weekly, month 6.10×, ladder rising; stop ₹694.45; charges ₹0.0118)
2020-05-11  IOLCP       BUY ₹9.98 at ₹66.18 (fresh Friday signal — BUY: 2.18× weekly, month 2.65×, ladder rising; stop ₹51.22; charges ₹0.0118)
2020-05-18  ADVENZYMES  BUY ₹10.28 at ₹159.95 (fresh Friday signal — ACCUMULATE: 3.12× weekly, month 2.00×, ladder rising; stop ₹126.20; charges ₹0.0122)
2020-05-18  ALEMBICLTD  BUY ₹10.26 at ₹54.90 (fresh Friday signal — ACCUMULATE: 2.50× weekly, month 2.01×, ladder rising; stop ₹44.84; charges ₹0.0122)
2020-05-18  HATHWAY     BUY ₹10.24 at ₹24.50 (fresh Friday signal — BUY: 8.39× weekly, month 4.73×, ladder rising; stop ₹15.52; charges ₹0.0121)
2020-05-18  RCF         BUY ₹9.22 at ₹39.90 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 2.55×, ladder rising; stop ₹35.25; charges ₹0.0109)
2020-06-12  DEEPAKNTR   SELL ₹9.97 at stop ₹474.05 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-06-15  PANACEABIO  BUY ₹9.97 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.25×, ladder rising; stop ₹114.11; charges ₹0.0118)
2020-06-16  IOLCP       SELL ₹10.43 at stop ₹69.35 (+4.8%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2020-06-22  VINDHYATEL  BUY ₹10.43 at ₹735.00 (fresh Friday signal — BUY: 8.86× weekly, month 4.88×, ladder rising; stop ₹570.95; charges ₹0.0124)
2020-06-29  HATHWAY     SELL ₹13.09 at stop ₹31.40 (+28.2%, charges ₹0.0136) — the cash goes back to work at the next Friday screen
2020-07-06  BDL         BUY ₹11.69 at ₹192.10 (fresh Friday signal — BUY: 20.22× weekly, month 9.90×, ladder rising; stop ₹123.59; charges ₹0.0139)
2020-07-23  VINDHYATEL  SELL ₹9.45 at stop ₹667.14 (-9.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-07-27  KIRLOSBROS  BUY ₹10.85 at ₹122.55 (fresh Friday signal — ACCUMULATE: 9.32× weekly, month 6.82×, ladder rising; stop ₹97.15; charges ₹0.0129)
2020-08-20  PANACEABIO  SELL ₹7.96 at stop ₹184.01 (-20.0%, charges ₹0.0083) — the cash goes back to work at the next Friday screen
2020-08-24  APCOTEXIND  BUY ₹7.96 at ₹164.95 (fresh Friday signal — BUY: 8.08× weekly, month 5.83×, ladder rising; stop ₹119.51; charges ₹0.0094)
2020-08-31  APCOTEXIND  SELL ₹7.31 at stop ₹151.95 (-7.9%, charges ₹0.0076) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.93 at stop ₹928.62 (+19.9%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹12.21 at ₹1,398.95 (fresh Friday signal — BUY: 5.36× weekly, month 3.91×, ladder rising; stop ₹1,211.25; charges ₹0.0145)
2020-09-07  PRINCEPIPE  BUY ₹7.03 at ₹208.00 (fresh Friday signal — BUY: 3.47× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.0083)
2020-09-08  BDL         SELL ₹10.26 at stop ₹168.93 (-12.1%, charges ₹0.0106) — the cash goes back to work at the next Friday screen
2020-09-08  CADILAHC    SELL ₹11.04 at stop ₹364.99 (+10.5%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-08  KIRLOSBROS  SELL ₹10.67 at stop ₹120.79 (-1.4%, charges ₹0.0111) — the cash goes back to work at the next Friday screen
2020-09-09  RCF         SELL ₹10.57 at stop ₹45.84 (+14.9%, charges ₹0.0110) — the cash goes back to work at the next Friday screen
2020-09-14  GLAXO       BUY ₹12.45 at ₹1,675.00 (fresh Friday signal — BUY: 2.58× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.0148)
2020-09-14  SATIA       BUY ₹12.46 at ₹122.00 (fresh Friday signal — ACCUMULATE: 2.86× weekly, month 6.16×, ladder rising; stop ₹102.97; charges ₹0.0148)
2020-09-14  TCI         BUY ₹12.46 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.76× weekly, month 3.77×, ladder rising; stop ₹190.07; charges ₹0.0148)
2020-09-22  SATIA       SELL ₹10.49 at stop ₹102.97 (-15.6%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹9.47 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹12.54 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0149)
2020-09-28  SAKSOFT     BUY ₹12.59 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.0149)
2020-10-12  PRINCEPIPE  SELL ₹7.45 at stop ₹220.88 (+6.2%, charges ₹0.0077) — the cash goes back to work at the next Friday screen
2020-10-19  SUBEX       BUY ₹7.45 at ₹15.55 (fresh Friday signal — BUY: 6.85× weekly, month 4.86×, ladder rising; stop ₹11.11; charges ₹0.0088)
2020-11-02  ALEMBICLTD  SELL ₹17.05 at stop ₹91.41 (+66.5%, charges ₹0.0177) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹10.69 at stop ₹1,441.55 (-13.9%, charges ₹0.0111) — the cash goes back to work at the next Friday screen
2020-11-03  ADVENZYMES  SELL ₹18.75 at stop ₹292.33 (+82.8%, charges ₹0.0195) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹11.78 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.0140)
2020-11-09  JINDWORLD   BUY ₹11.80 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.28× weekly, month 1.55×, ladder rising; stop ₹39.81; charges ₹0.0140)
2020-11-17  PILANIINVS  BUY ₹10.74 at ₹2,054.50 (fresh Friday signal — ACCUMULATE: 3.04× weekly, month 1.77×, ladder rising; stop ₹1,752.75; charges ₹0.0127)
2020-11-17  TRENT       BUY ₹12.18 at ₹503.33 (fresh Friday signal — ACCUMULATE: 3.30× weekly, month 1.95×, ladder rising; stop ₹367.93; charges ₹0.0144)
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹12.06 at stop ₹234.75 (-3.0%, charges ₹0.0125) — the cash goes back to work at the next Friday screen
2020-12-28  ITDC        BUY ₹14.71 at ₹338.55 (fresh Friday signal — BUY: 10.22× weekly, month 4.03×, ladder rising; stop ₹247.29; charges ₹0.0174)
2020-12-28  PAISALO     BUY ₹14.58 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0173)
2021-01-04  PILANIINVS  SELL ₹11.13 at stop ₹2,132.80 (+3.8%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2021-01-11  KKCL        BUY ₹11.52 at ₹985.00 (fresh Friday signal — BUY: 9.34× weekly, month 2.08×, ladder rising; stop ₹748.60; charges ₹0.0137)
2021-01-18  ITDC        SELL ₹13.20 at stop ₹304.38 (-10.1%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2021-01-20  BORORENEW   SELL ₹29.19 at stop ₹247.59 (+148.3%, charges ₹0.0303) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹14.12 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.79×, ladder rising; stop ₹92.41; charges ₹0.0167)
2021-01-25  MAHLOG      BUY ₹14.27 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹0.0169)
2021-01-25  SAKSOFT     SELL ₹10.74 at stop ₹341.10 (-14.4%, charges ₹0.0111) — the cash goes back to work at the next Friday screen
2021-01-25  TATAMOTORS  BUY ₹14.00 at ₹296.90 (fresh Friday signal — BUY: 3.10× weekly, month 2.05×, ladder rising; stop ₹171.38; charges ₹0.0166)
2021-01-29  HCLTECH     SELL ₹13.85 at stop ₹928.05 (+10.7%, charges ₹0.0144) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹10.08 at stop ₹417.53 (-17.0%, charges ₹0.0105) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹13.86 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.0164)
2021-02-01  GAEL        BUY ₹14.01 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.71× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.0166)
2021-02-23  GAEL        SELL ₹12.26 at stop ₹62.70 (-12.3%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2021-03-01  JINDWORLD   SELL ₹12.27 at stop ₹52.12 (+4.2%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2021-03-01  RCF         BUY ₹15.05 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.13×, ladder rising; stop ₹50.16; charges ₹0.0178)
2021-03-08  JSWENERGY   BUY ₹15.14 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.50×, ladder rising; stop ₹65.79; charges ₹0.0179)
2021-03-17  RCF         SELL ₹14.86 at stop ₹79.16 (-1.1%, charges ₹0.0154) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹15.83 at stop ₹204.25 (+14.5%, charges ₹0.0164) — the cash goes back to work at the next Friday screen
2021-03-19  TATAMOTORS  SELL ₹13.97 at stop ₹296.97 (+0.0%, charges ₹0.0145) — the cash goes back to work at the next Friday screen
2021-03-22  GFLLIMITED  BUY ₹14.63 at ₹93.00 (fresh Friday signal — ACCUMULATE: 6.17× weekly, month 3.98×, ladder rising; stop ₹74.39; charges ₹0.0173)
2021-03-22  KEI         BUY ₹14.72 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.0174)
2021-03-22  VIDHIING    BUY ₹14.56 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0172)
2021-03-25  BANARISUG   SELL ₹13.82 at stop ₹1,586.36 (+13.4%, charges ₹0.0143) — the cash goes back to work at the next Friday screen
2021-03-30  CENTRUM     BUY ₹14.93 at ₹28.40 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 6.70×, ladder rising; stop ₹24.89; charges ₹0.0177)
2021-03-30  KKCL        SELL ₹10.00 at stop ₹856.90 (-13.0%, charges ₹0.0104) — the cash goes back to work at the next Friday screen
2021-04-01  TAX         FY2021 settled: ₹7.2042 paid (STCG ₹36.02 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-12  CENTRUM     SELL ₹13.05 at stop ₹24.89 (-12.4%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹18.48 at stop ₹72.41 (+27.1%, charges ₹0.0192) — the cash goes back to work at the next Friday screen
2021-04-13  GFLLIMITED  SELL ₹11.68 at stop ₹74.39 (-20.0%, charges ₹0.0121) — the cash goes back to work at the next Friday screen
2021-04-19  EMAMIPAP    BUY ₹13.17 at ₹125.00 (fresh Friday signal — ACCUMULATE: 2.31× weekly, month 22.17×, ladder rising; stop ₹81.22; charges ₹0.0156)
2021-04-19  KPRMILL     BUY ₹13.10 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0155)
2021-04-19  MOREPENLAB  BUY ₹13.12 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹0.0155)
2021-04-26  SUPPETRO    BUY ₹7.41 at ₹670.90 (fresh Friday signal — BUY: 6.51× weekly, month 2.36×, ladder rising; stop ₹453.05; charges ₹0.0088)
2021-06-18  VIDHIING    SELL ₹13.63 at stop ₹182.64 (-6.2%, charges ₹0.0141) — the cash goes back to work at the next Friday screen
2021-06-21  SOMANYCERA  BUY ₹13.63 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0161)
2021-08-10  MOREPENLAB  SELL ₹19.69 at stop ₹56.33 (+50.4%, charges ₹0.0204) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹19.53 at stop ₹352.48 (+49.4%, charges ₹0.0203) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹20.55 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.0243)
2021-08-16  TATAINVEST  BUY ₹18.66 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0221)
2021-09-13  SUPPETRO    SELL ₹7.75 at stop ₹703.10 (+4.8%, charges ₹0.0080) — the cash goes back to work at the next Friday screen
2021-09-20  GDL         SELL ₹23.72 at stop ₹266.00 (+68.4%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2021-09-27  BAJAJHLDNG  BUY ₹10.88 at ₹4,979.00 (fresh Friday signal — BUY: 4.52× weekly, month 1.97×, ladder rising; stop ₹4,184.75; charges ₹0.0129)
2021-09-27  NEOGEN      BUY ₹20.59 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0244)
2021-10-22  KEI         SELL ₹24.00 at stop ₹853.10 (+63.4%, charges ₹0.0249) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹17.95 at stop ₹3,220.59 (-12.5%, charges ₹0.0186) — the cash goes back to work at the next Friday screen
2021-10-25  NEOGEN      SELL ₹18.71 at stop ₹1,142.85 (-8.9%, charges ₹0.0194) — the cash goes back to work at the next Friday screen
2021-10-25  SHOPERSTOP  BUY ₹20.23 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹0.0240)
2021-11-01  TCIEXP      BUY ₹20.04 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0237)
2021-11-01  TTKPRESTIG  BUY ₹20.04 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.0237)
2021-11-22  EMAMIPAP    SELL ₹14.88 at stop ₹141.55 (+13.2%, charges ₹0.0154) — the cash goes back to work at the next Friday screen
2021-11-22  SHOPERSTOP  SELL ₹20.80 at stop ₹335.82 (+3.0%, charges ₹0.0216) — the cash goes back to work at the next Friday screen
2021-11-26  TATAINVEST  SELL ₹20.45 at stop ₹1,436.49 (+9.8%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹18.23 at stop ₹10,070.05 (-8.8%, charges ₹0.0189) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹20.25 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.0240)
2021-11-29  RAYMOND     BUY ₹20.04 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0237)
2021-11-29  RSYSTEMS    BUY ₹20.16 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0239)
2021-11-29  SOMANYCERA  SELL ₹17.26 at stop ₹755.11 (+26.9%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2021-11-29  TVTODAY     BUY ₹14.25 at ₹328.80 (fresh Friday signal — ACCUMULATE: 2.49× weekly, month 4.40×, ladder rising; stop ₹277.73; charges ₹0.0169)
2021-11-30  MAHLOG      SELL ₹18.79 at stop ₹654.55 (+32.0%, charges ₹0.0195) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹20.08 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0238)
2021-12-06  CHAMBLFERT  BUY ₹15.98 at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹0.0189)
2021-12-16  RSYSTEMS    SELL ₹18.03 at stop ₹291.18 (-10.4%, charges ₹0.0187) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹18.03 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0214)
2021-12-21  TCIEXP      SELL ₹22.27 at stop ₹2,039.74 (+11.4%, charges ₹0.0231) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹19.82 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0235)
2022-01-24  TVTODAY     SELL ₹13.48 at stop ₹311.68 (-5.2%, charges ₹0.0140) — the cash goes back to work at the next Friday screen
2022-01-25  SWANENERGY  SELL ₹21.46 at stop ₹162.64 (+8.5%, charges ₹0.0223) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹20.58 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0244)
2022-01-31  TV18BRDCST  BUY ₹16.81 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.0199)
2022-02-11  SHARDACROP  SELL ₹19.08 at stop ₹545.30 (-7.1%, charges ₹0.0198) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹18.44 at stop ₹424.65 (-8.7%, charges ₹0.0191) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹19.08 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0226)
2022-02-15  RAYMOND     SELL ₹22.80 at stop ₹679.35 (+14.0%, charges ₹0.0236) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹19.67 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0233)
2022-02-22  GREENLAM    SELL ₹15.52 at stop ₹313.67 (-13.7%, charges ₹0.0161) — the cash goes back to work at the next Friday screen
2022-02-22  TV18BRDCST  SELL ₹16.63 at stop ₹58.38 (-0.9%, charges ₹0.0172) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹13.84 at stop ₹353.85 (-13.2%, charges ₹0.0144) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹19.55 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0232)
2022-02-28  SHANTIGEAR  BUY ₹19.54 at ₹185.30 (fresh Friday signal — BUY: 2.90× weekly, month 1.90×, ladder rising; stop ₹170.29; charges ₹0.0231)
2022-03-07  EXCELINDUS  BUY ₹19.69 at ₹1,523.00 (fresh Friday signal — BUY: 6.93× weekly, month 5.51×, ladder rising; stop ₹1,016.01; charges ₹0.0233)
2022-03-21  BSE         SELL ₹17.33 at stop ₹1,634.39 (-13.5%, charges ₹0.0180) — the cash goes back to work at the next Friday screen
2022-03-29  EXCELINDUS  SELL ₹18.55 at stop ₹1,438.30 (-5.6%, charges ₹0.0192) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹5.8207 paid (STCG ₹29.10 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  INOXLEISUR  BUY ₹18.77 at ₹520.85 (fresh Friday signal — ACCUMULATE: 7.27× weekly, month 3.35×, ladder rising; stop ₹470.35; charges ₹0.0222)
2022-04-04  RCF         BUY ₹20.06 at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.0238)
2022-05-04  RCF         SELL ₹19.34 at stop ₹93.15 (-3.4%, charges ₹0.0201) — the cash goes back to work at the next Friday screen
2022-05-06  INOXLEISUR  SELL ₹16.91 at stop ₹470.35 (-9.7%, charges ₹0.0175) — the cash goes back to work at the next Friday screen
2022-05-09  JKIL        BUY ₹22.11 at ₹229.70 (fresh Friday signal — BUY: 6.96× weekly, month 3.58×, ladder rising; stop ₹192.28; charges ₹0.0262)
2022-05-09  MOL         BUY ₹14.14 at ₹129.80 (fresh Friday signal — BUY: 6.75× weekly, month 2.56×, ladder rising; stop ₹113.62; charges ₹0.0168)
2022-05-11  BAJAJHLDNG  SELL ₹10.58 at stop ₹4,853.07 (-2.5%, charges ₹0.0110) — the cash goes back to work at the next Friday screen
2022-05-11  MOL         SELL ₹12.35 at stop ₹113.62 (-12.5%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹21.64 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0256)
2022-06-06  VBL         SELL ₹19.26 at stop ₹196.27 (-10.8%, charges ₹0.0200) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹20.55 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0244)
2022-06-20  JSWENERGY   SELL ₹37.27 at stop ₹201.99 (+146.8%, charges ₹0.0387) — the cash goes back to work at the next Friday screen
2022-06-27  APARINDS    BUY ₹22.32 at ₹1,004.00 (fresh Friday signal — BUY: 7.05× weekly, month 6.41×, ladder rising; stop ₹706.80; charges ₹0.0264)
2022-07-25  TIINDIA     BUY ₹14.96 at ₹2,135.00 (fresh Friday signal — BUY: 4.17× weekly, month 2.43×, ladder rising; stop ₹1,862.00; charges ₹0.0177)
2022-08-05  JKIL        SELL ₹29.66 at stop ₹308.80 (+34.4%, charges ₹0.0308) — the cash goes back to work at the next Friday screen
2022-08-08  NAVNETEDUL  BUY ₹24.27 at ₹130.50 (fresh Friday signal — BUY: 14.73× weekly, month 3.84×, ladder rising; stop ₹88.40; charges ₹0.0288)
2022-09-06  DANGEE      SELL ₹31.15 at stop ₹375.25 (+59.7%, charges ₹0.0323) — the cash goes back to work at the next Friday screen
2022-09-12  SHREECEM    BUY ₹25.62 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0304)
2022-09-26  NAVNETEDUL  SELL ₹23.62 at stop ₹127.30 (-2.5%, charges ₹0.0245) — the cash goes back to work at the next Friday screen
2022-10-03  SUNDARMHLD  BUY ₹24.90 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹0.0295)
2022-10-11  SUNDARMHLD  SELL ₹22.13 at stop ₹92.20 (-10.9%, charges ₹0.0230) — the cash goes back to work at the next Friday screen
2022-10-17  FAIRCHEMOR  BUY ₹25.35 at ₹2,240.00 (fresh Friday signal — ACCUMULATE: 2.93× weekly, month 2.97×, ladder rising; stop ₹1,790.15; charges ₹0.0300)
2022-11-01  FAIRCHEMOR  SELL ₹20.21 at stop ₹1,790.15 (-20.1%, charges ₹0.0210) — the cash goes back to work at the next Friday screen
2022-11-03  APARINDS    SELL ₹30.13 at stop ₹1,358.50 (+35.3%, charges ₹0.0313) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹26.04 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0309)
2022-11-07  RVNL        BUY ₹25.98 at ₹46.85 (fresh Friday signal — BUY: 4.42× weekly, month 4.42×, ladder rising; stop ₹33.77; charges ₹0.0308)
2022-12-21  ELECON      SELL ₹33.91 at stop ₹202.49 (+65.3%, charges ₹0.0352) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹36.35 at stop ₹345.56 (+86.5%, charges ₹0.0377) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹25.95 at stop ₹139.84 (-0.1%, charges ₹0.0269) — the cash goes back to work at the next Friday screen
2022-12-26  KRISHANA    BUY ₹26.36 at ₹83.60 (fresh Friday signal — BUY: 3.70× weekly, month 2.29×, ladder rising; stop ₹75.36; charges ₹0.0312)
2022-12-26  RVNL        SELL ₹33.52 at stop ₹60.57 (+29.3%, charges ₹0.0348) — the cash goes back to work at the next Friday screen
2023-01-02  GICRE       BUY ₹26.44 at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 11.18×, ladder rising; stop ₹137.57; charges ₹0.0313)
2023-01-02  IOB         BUY ₹26.27 at ₹32.40 (fresh Friday signal — ACCUMULATE: 4.77× weekly, month 30.16×, ladder rising; stop ₹21.23; charges ₹0.0311)
2023-01-02  MUKANDLTD   BUY ₹26.28 at ₹136.70 (fresh Friday signal — BUY: 6.81× weekly, month 2.54×, ladder rising; stop ₹103.76; charges ₹0.0311)
2023-01-02  SUNFLAG     BUY ₹26.22 at ₹113.00 (fresh Friday signal — ACCUMULATE: 3.55× weekly, month 1.84×, ladder rising; stop ₹86.70; charges ₹0.0311)
2023-01-11  TIINDIA     SELL ₹18.16 at stop ₹2,598.34 (+21.7%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2023-01-16  LSIL        BUY ₹21.08 at ₹19.35 (fresh Friday signal — BUY: 3.42× weekly, month 3.18×, ladder rising; stop ₹11.29; charges ₹0.0250)
2023-02-01  GICRE       SELL ₹24.69 at stop ₹167.72 (-6.4%, charges ₹0.0256) — the cash goes back to work at the next Friday screen
2023-02-06  JINDALSAW   BUY ₹24.69 at ₹65.22 (fresh Friday signal — BUY: 2.72× weekly, month 3.57×, ladder rising; stop ₹51.25; charges ₹0.0293)
2023-02-07  LSIL        SELL ₹21.78 at stop ₹20.04 (+3.6%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2023-02-17  CGCL        SELL ₹23.08 at stop ₹704.95 (+17.6%, charges ₹0.0239) — the cash goes back to work at the next Friday screen
2023-02-20  CIGNITITEC  BUY ₹18.40 at ₹731.95 (fresh Friday signal — BUY: 2.05× weekly, month 1.77×, ladder rising; stop ₹568.10; charges ₹0.0218)
2023-02-20  TIIL        BUY ₹26.47 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0314)
2023-02-27  SUNFLAG     SELL ₹29.91 at stop ₹129.20 (+14.3%, charges ₹0.0310) — the cash goes back to work at the next Friday screen
2023-03-06  WONDERLA    BUY ₹26.83 at ₹456.00 (fresh Friday signal — BUY: 4.06× weekly, month 2.13×, ladder rising; stop ₹384.27; charges ₹0.0318)
2023-03-20  IOB         SELL ₹17.94 at stop ₹22.18 (-31.5%, charges ₹0.0186) — the cash goes back to work at the next Friday screen
2023-03-20  KRISHANA    SELL ₹29.70 at stop ₹94.40 (+12.9%, charges ₹0.0308) — the cash goes back to work at the next Friday screen
2023-03-27  ANURAS      BUY ₹25.12 at ₹867.00 (fresh Friday signal — BUY: 7.51× weekly, month 4.46×, ladder rising; stop ₹691.46; charges ₹0.0298)
2023-03-27  JINDALSAW   SELL ₹25.66 at stop ₹67.92 (+4.1%, charges ₹0.0266) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹25.00 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.61×, ladder rising; stop ₹372.21; charges ₹0.0296)
2023-03-27  WONDERLA    SELL ₹22.56 at stop ₹384.27 (-15.7%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2023-03-29  CIGNITITEC  SELL ₹17.69 at stop ₹705.14 (-3.7%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹41.14 at stop ₹112.36 (+116.1%, charges ₹0.0427) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹23.61 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.0280)
2023-04-03  TAX         FY2023 settled: ₹15.6403 paid (STCG ₹50.50 @20%, LTCG ₹44.32 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-10  KIRLOSBROS  BUY ₹23.81 at ₹425.00 (fresh Friday signal — BUY: 1.86× weekly, month 2.36×, ladder rising; stop ₹357.44; charges ₹0.0282)
2023-04-10  KIRLOSIND   BUY ₹23.86 at ₹2,724.00 (fresh Friday signal — BUY: 2.29× weekly, month 2.42×, ladder rising; stop ₹2,256.25; charges ₹0.0283)
2023-04-10  VSSL        BUY ₹20.71 at ₹414.00 (fresh Friday signal — BUY: 1.74× weekly, month 3.18×, ladder rising; stop ₹324.52; charges ₹0.0245)
2023-04-24  SHREECEM    SELL ₹24.56 at stop ₹23,636.00 (-3.9%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2023-04-26  KIRLOSBROS  SELL ₹22.58 at stop ₹403.85 (-5.0%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2023-05-02  FAIRCHEMOR  BUY ₹23.15 at ₹1,272.00 (fresh Friday signal — BUY: 3.67× weekly, month 1.62×, ladder rising; stop ₹1,054.59; charges ₹0.0274)
2023-05-02  GLS         BUY ₹23.99 at ₹509.05 (fresh Friday signal — BUY: 4.14× weekly, month 2.64×, ladder rising; stop ₹351.50; charges ₹0.0284)
2023-05-17  MUKANDLTD   SELL ₹22.29 at stop ₹116.23 (-15.0%, charges ₹0.0231) — the cash goes back to work at the next Friday screen
2023-05-19  FAIRCHEMOR  SELL ₹20.72 at stop ₹1,141.04 (-10.3%, charges ₹0.0215) — the cash goes back to work at the next Friday screen
2023-05-22  NEULANDLAB  BUY ₹18.80 at ₹2,831.90 (fresh Friday signal — BUY: 6.13× weekly, month 4.03×, ladder rising; stop ₹1,908.60; charges ₹0.0223)
2023-05-22  SHARDAMOTR  BUY ₹24.21 at ₹380.00 (fresh Friday signal — BUY: 9.54× weekly, month 2.31×, ladder rising; stop ₹342.95; charges ₹0.0287)
2023-05-26  VSSL        SELL ₹16.20 at stop ₹324.52 (-21.6%, charges ₹0.0168) — the cash goes back to work at the next Friday screen
2023-05-29  THANGAMAYL  BUY ₹16.20 at ₹1,344.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.50×, ladder rising; stop ₹1,116.30; charges ₹0.0192)
2023-07-03  ANURAS      SELL ₹29.14 at stop ₹1,007.67 (+16.2%, charges ₹0.0302) — the cash goes back to work at the next Friday screen
2023-07-10  GENUSPOWER  BUY ₹25.44 at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.48×, ladder rising; stop ₹99.51; charges ₹0.0301)
2023-07-12  KSB         SELL ₹24.33 at stop ₹407.74 (-2.4%, charges ₹0.0252) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹25.11 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0297)
2023-07-17  THANGAMAYL  SELL ₹16.16 at stop ₹1,344.25 (+0.0%, charges ₹0.0168) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹19.09 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.84×, ladder rising; stop ₹359.10; charges ₹0.0226)
2023-08-14  GANESHHOUC  SELL ₹17.45 at stop ₹418.62 (-8.4%, charges ₹0.0181) — the cash goes back to work at the next Friday screen
2023-08-21  ASTRAZEN    BUY ₹17.45 at ₹4,099.85 (fresh Friday signal — BUY: 6.03× weekly, month 2.40×, ladder rising; stop ₹3,562.50; charges ₹0.0207)
2023-09-13  NEULANDLAB  SELL ₹22.90 at stop ₹3,457.30 (+22.1%, charges ₹0.0238) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹22.90 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.67×, ladder rising; stop ₹58.28; charges ₹0.0271)
2023-09-25  KIRLOSIND   SELL ₹28.00 at stop ₹3,202.97 (+17.6%, charges ₹0.0290) — the cash goes back to work at the next Friday screen
2023-10-03  PILANIINVS  BUY ₹28.00 at ₹2,380.05 (fresh Friday signal — BUY: 3.07× weekly, month 7.66×, ladder rising; stop ₹2,018.75; charges ₹0.0332)
2023-10-23  SJVN        SELL ₹20.03 at stop ₹66.03 (-12.4%, charges ₹0.0208) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹31.43 at stop ₹1,840.70 (+33.4%, charges ₹0.0326) — the cash goes back to work at the next Friday screen
2023-10-25  SHARDAMOTR  SELL ₹29.57 at stop ₹465.07 (+22.4%, charges ₹0.0307) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹21.08 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0250)
2023-10-30  KKCL        BUY ₹29.98 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0355)
2023-10-30  SHAREINDIA  BUY ₹29.96 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0355)
2023-11-16  GENUSPOWER  SELL ₹36.48 at stop ₹234.03 (+43.7%, charges ₹0.0378) — the cash goes back to work at the next Friday screen
2023-11-20  ISMTLTD     BUY ₹32.17 at ₹94.60 (fresh Friday signal — BUY: 5.37× weekly, month 1.93×, ladder rising; stop ₹80.18; charges ₹0.0381)
2023-12-20  ISMTLTD     SELL ₹29.98 at stop ₹88.35 (-6.6%, charges ₹0.0311) — the cash goes back to work at the next Friday screen
2023-12-26  MMFL        BUY ₹34.28 at ₹1,023.60 (fresh Friday signal — BUY: 9.43× weekly, month 3.43×, ladder rising; stop ₹821.80; charges ₹0.0406)
2024-01-17  TIIL        SELL ₹55.26 at stop ₹2,337.00 (+109.3%, charges ₹0.0573) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹35.68 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0423)
2024-01-23  RVNL        BUY ₹19.59 at ₹332.00 (fresh Friday signal — BUY: 6.89× weekly, month 1.60×, ladder rising; stop ₹157.32; charges ₹0.0232)
2024-01-30  MMFL        SELL ₹30.48 at stop ₹912.05 (-10.9%, charges ₹0.0316) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹30.48 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0361)
2024-02-09  ASTRAZEN    SELL ₹24.61 at stop ₹5,795.95 (+41.4%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2024-02-12  IOB         BUY ₹24.61 at ₹71.50 (fresh Friday signal — BUY: 7.81× weekly, month 2.91×, ladder rising; stop ₹38.71; charges ₹0.0292)
2024-02-12  RVNL        SELL ₹14.19 at stop ₹241.04 (-27.4%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2024-03-05  GLS         SELL ₹36.65 at stop ₹779.48 (+53.1%, charges ₹0.0380) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹35.59 at stop ₹357.20 (+19.1%, charges ₹0.0369) — the cash goes back to work at the next Friday screen
2024-03-11  DOLLAR      BUY ₹37.77 at ₹527.95 (fresh Friday signal — BUY: 4.55× weekly, month 2.48×, ladder rising; stop ₹461.65; charges ₹0.0448)
2024-03-11  SOLARINDS   BUY ₹37.69 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0447)
2024-03-11  TCI         SELL ₹24.34 at stop ₹790.40 (-20.0%, charges ₹0.0252) — the cash goes back to work at the next Friday screen
2024-03-13  DOLLAR      SELL ₹32.96 at stop ₹461.65 (-12.6%, charges ₹0.0342) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹26.47 at stop ₹674.12 (-11.5%, charges ₹0.0275) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹35.76 at stop ₹666.47 (+0.5%, charges ₹0.0371) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹35.99 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.0426)
2024-03-18  EMUDHRA     BUY ₹22.91 at ₹583.90 (fresh Friday signal — BUY: 1.54× weekly, month 3.10×, ladder rising; stop ₹529.77; charges ₹0.0271)
2024-03-18  FORCEMOT    BUY ₹35.82 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.0424)
2024-03-18  INDIGO      BUY ₹35.77 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0424)
2024-03-27  ANANDRATHI  SELL ₹81.33 at stop ₹862.65 (+224.7%, charges ₹0.0844) — the cash goes back to work at the next Friday screen
2024-04-01  DMART       BUY ₹25.09 at ₹4,570.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.56×, ladder rising; stop ₹3,695.50; charges ₹0.0297)
2024-04-01  SHRIRAMFIN  BUY ₹35.37 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0419)
2024-04-01  TAX         FY2024 settled: ₹20.8698 paid (STCG ₹104.35 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-09  PILANIINVS  SELL ₹43.55 at stop ₹3,710.37 (+55.9%, charges ₹0.0452) — the cash goes back to work at the next Friday screen
2024-05-13  JWL         BUY ₹36.87 at ₹490.00 (fresh Friday signal — BUY: 7.12× weekly, month 2.51×, ladder rising; stop ₹370.93; charges ₹0.0437)
2024-05-28  FORCEMOT    SELL ₹43.99 at stop ₹8,083.64 (+23.1%, charges ₹0.0456) — the cash goes back to work at the next Friday screen
2024-05-31  DMART       SELL ₹23.68 at stop ₹4,322.83 (-5.4%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹39.01 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0462)
2024-06-03  THERMAX     BUY ₹35.35 at ₹5,640.00 (fresh Friday signal — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹0.0419)
2024-06-04  BOSCHLTD    SELL ₹35.31 at stop ₹29,015.09 (-1.6%, charges ₹0.0366) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹32.87 at stop ₹441.77 (-6.8%, charges ₹0.0341) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹39.68 at stop ₹7,980.95 (+5.5%, charges ₹0.0412) — the cash goes back to work at the next Friday screen
2024-06-10  DABUR       BUY ₹33.58 at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹0.0398)
2024-06-10  FIEMIND     BUY ₹37.21 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0441)
2024-06-10  UNOMINDA    BUY ₹37.09 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0439)
2024-07-19  UNOMINDA    SELL ₹37.46 at stop ₹981.87 (+1.2%, charges ₹0.0389) — the cash goes back to work at the next Friday screen
2024-07-22  INDIAGLYCO  BUY ₹37.40 at ₹515.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.25×, ladder rising; stop ₹429.42; charges ₹0.0443)
2024-07-23  FIEMIND     SELL ₹35.37 at stop ₹1,257.56 (-4.7%, charges ₹0.0367) — the cash goes back to work at the next Friday screen
2024-07-29  THYROCARE   BUY ₹35.43 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0420)
2024-08-05  THERMAX     SELL ₹29.52 at stop ₹4,719.70 (-16.3%, charges ₹0.0306) — the cash goes back to work at the next Friday screen
2024-08-06  JWL         SELL ₹41.44 at stop ₹552.00 (+12.7%, charges ₹0.0430) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹37.00 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0438)
2024-08-12  CERA        BUY ₹33.96 at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹0.0402)
2024-08-13  EMUDHRA     SELL ₹31.04 at stop ₹793.11 (+35.8%, charges ₹0.0322) — the cash goes back to work at the next Friday screen
2024-08-16  CAMPUS      SELL ₹37.71 at stop ₹277.07 (-3.1%, charges ₹0.0391) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹36.25 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0429)
2024-08-19  VGUARD      BUY ₹32.50 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.0385)
2024-09-19  CERA        SELL ₹26.46 at stop ₹8,198.93 (-21.9%, charges ₹0.0274) — the cash goes back to work at the next Friday screen
2024-09-23  ALKYLAMINE  BUY ₹26.46 at ₹2,432.85 (fresh Friday signal — BUY: 9.32× weekly, month 3.52×, ladder rising; stop ₹2,106.24; charges ₹0.0313)
2024-10-03  DABUR       SELL ₹33.41 at stop ₹602.49 (-0.3%, charges ₹0.0347) — the cash goes back to work at the next Friday screen
2024-10-03  IOB         SELL ₹19.43 at stop ₹56.57 (-20.9%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹26.00 at stop ₹420.24 (-19.8%, charges ₹0.0270) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹35.30 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0418)
2024-10-07  INDIGO      SELL ₹50.03 at stop ₹4,485.14 (+40.2%, charges ₹0.0519) — the cash goes back to work at the next Friday screen
2024-10-07  ITDCEM      BUY ₹35.48 at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹0.0420)
2024-10-07  THYROCARE   SELL ₹35.86 at stop ₹796.15 (+1.4%, charges ₹0.0372) — the cash goes back to work at the next Friday screen
2024-10-14  BSE         BUY ₹21.96 at ₹4,536.00 (fresh Friday signal — BUY: 2.79× weekly, month 4.25×, ladder rising; stop ₹3,393.93; charges ₹0.0260)
2024-10-14  DBCORP      BUY ₹36.06 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0427)
2024-10-14  SKIPPER     BUY ₹35.92 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0426)
2024-10-22  ALKYLAMINE  SELL ₹22.85 at stop ₹2,106.24 (-13.4%, charges ₹0.0237) — the cash goes back to work at the next Friday screen
2024-10-22  BASF        SELL ₹38.23 at stop ₹7,611.30 (+3.6%, charges ₹0.0397) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹30.88 at stop ₹302.08 (-14.2%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2024-10-25  INDIAGLYCO  SELL ₹42.60 at stop ₹587.91 (+14.2%, charges ₹0.0442) — the cash goes back to work at the next Friday screen
2024-10-28  CARERATING  BUY ₹29.94 at ₹1,396.00 (fresh Friday signal — BUY: 7.47× weekly, month 3.86×, ladder rising; stop ₹1,066.23; charges ₹0.0355)
2024-10-28  CUPID       SELL ₹27.58 at stop ₹158.66 (+31.1%, charges ₹0.0286) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹30.05 at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.0356)
2024-11-04  AKZOINDIA   BUY ₹33.69 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.0795)
2024-11-04  KIRLPNU     BUY ₹33.51 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.0791)
2024-11-11  JSWHL       BUY ₹33.39 at ₹15,500.00 (fresh Friday signal — BUY: 8.83× weekly, month 3.54×, ladder rising; stop ₹8,434.53; charges ₹0.0788)
2024-11-14  ASTRAZEN    SELL ₹32.40 at stop ₹6,854.77 (-7.9%, charges ₹0.0720) — the cash goes back to work at the next Friday screen
2024-11-25  GARFIBRES   BUY ₹33.96 at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹0.0802)
2024-12-17  SUPRIYA     SELL ₹49.08 at stop ₹717.25 (+35.8%, charges ₹0.1090) — the cash goes back to work at the next Friday screen
2024-12-23  KIRLPNU     SELL ₹31.35 at stop ₹1,596.00 (-6.0%, charges ₹0.0696) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹33.99 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.0802)
2024-12-27  AKZOINDIA   SELL ₹25.41 at stop ₹3,423.18 (-24.2%, charges ₹0.0564) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹33.95 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.0801)
2024-12-30  KFINTECH    BUY ₹33.83 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.0799)
2025-01-09  GARFIBRES   SELL ₹29.32 at stop ₹829.35 (-13.2%, charges ₹0.0651) — the cash goes back to work at the next Friday screen
2025-01-09  KSL         SELL ₹30.07 at stop ₹1,059.30 (-11.1%, charges ₹0.0668) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹35.77 at stop ₹893.05 (+19.4%, charges ₹0.0795) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹30.89 at stop ₹477.28 (-13.7%, charges ₹0.0686) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹31.44 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0742)
2025-01-13  CARERATING  SELL ₹26.50 at stop ₹1,239.70 (-11.2%, charges ₹0.0589) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹31.35 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.0740)
2025-01-15  KFINTECH    SELL ₹25.83 at stop ₹1,159.14 (-23.3%, charges ₹0.0574) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹26.26 at stop ₹700.36 (-16.1%, charges ₹0.0583) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹30.51 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0720)
2025-01-28  LLOYDSME    SELL ₹27.25 at stop ₹1,258.75 (-12.7%, charges ₹0.0605) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹31.29 at ₹947.00 (fresh Friday signal — BUY: 2.25× weekly, month 2.40×, ladder rising; stop ₹727.84; charges ₹0.0739)
2025-02-12  JINDWORLD   SELL ₹31.01 at stop ₹374.11 (-8.2%, charges ₹0.0689) — the cash goes back to work at the next Friday screen
2025-02-28  BSE         SELL ₹23.91 at stop ₹4,954.63 (+9.2%, charges ₹0.0531) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹29.41 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0694)
2025-03-03  ZENSARTECH  SELL ₹23.94 at stop ₹727.84 (-23.1%, charges ₹0.0532) — the cash goes back to work at the next Friday screen
2025-03-17  AVANTIFEED  BUY ₹30.74 at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹0.0726)
2025-03-24  INDIASHLTR  BUY ₹32.24 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.0761)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹9.09 / LT ₹0.00)
2025-04-07  AVANTIFEED  SELL ₹23.57 at stop ₹648.95 (-23.0%, charges ₹0.0524) — the cash goes back to work at the next Friday screen
2025-04-07  INDIASHLTR  SELL ₹29.82 at stop ₹738.82 (-7.1%, charges ₹0.0662) — the cash goes back to work at the next Friday screen
2025-04-11  ITDCEM      SELL ₹28.34 at stop ₹524.92 (-19.9%, charges ₹0.0629) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹31.17 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.0736)
2025-04-15  INDIASHLTR  BUY ₹31.29 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.0739)
2025-04-28  FORCEMOT    BUY ₹31.83 at ₹9,275.00 (fresh Friday signal — ACCUMULATE: 2.06× weekly, month 1.62×, ladder rising; stop ₹7,647.50; charges ₹0.0752)
2025-04-28  KIMS        BUY ₹31.74 at ₹679.50 (fresh Friday signal — BUY: 1.93× weekly, month 1.58×, ladder rising; stop ₹486.11; charges ₹0.0749)
2025-04-28  WHIRLPOOL   BUY ₹31.72 at ₹1,153.90 (fresh Friday signal — BUY: 2.21× weekly, month 1.77×, ladder rising; stop ₹1,017.54; charges ₹0.0749)
2025-05-05  PARAS       BUY ₹21.80 at ₹1,372.20 (fresh Friday signal — BUY: 25.56× weekly, month 2.22×, ladder rising; stop ₹973.27; charges ₹0.0515)
2025-07-04  PARAS       SELL ₹22.43 at stop ₹1,417.98 (+3.3%, charges ₹0.0498) — the cash goes back to work at the next Friday screen
2025-07-07  ASTERDM     BUY ₹22.43 at ₹633.90 (fresh Friday signal — BUY: 6.11× weekly, month 1.72×, ladder rising; stop ₹509.77; charges ₹0.0529)
2025-08-04  JSWHL       SELL ₹40.97 at stop ₹19,106.01 (+23.3%, charges ₹0.0910) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹36.64 at stop ₹1,814.78 (+25.2%, charges ₹0.0814) — the cash goes back to work at the next Friday screen
2025-08-07  WHIRLPOOL   SELL ₹35.62 at stop ₹1,301.97 (+12.8%, charges ₹0.0791) — the cash goes back to work at the next Friday screen
2025-08-11  PGHL        BUY ₹34.14 at ₹6,345.00 (fresh Friday signal — BUY: 1.64× weekly, month 2.94×, ladder rising; stop ₹5,320.00; charges ₹0.0806)
2025-08-11  RAIN        BUY ₹34.20 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.0807)
2025-08-18  VSTTILLERS  BUY ₹35.18 at ₹5,260.00 (fresh Friday signal — BUY: 7.75× weekly, month 4.61×, ladder rising; stop ₹4,193.97; charges ₹0.0830)
2025-08-26  RAIN        SELL ₹30.51 at stop ₹143.64 (-10.4%, charges ₹0.0678) — the cash goes back to work at the next Friday screen
2025-09-01  RSYSTEMS    BUY ₹34.61 at ₹460.00 (fresh Friday signal — BUY: 3.48× weekly, month 6.66×, ladder rising; stop ₹394.44; charges ₹0.0817)
2025-09-24  RSYSTEMS    SELL ₹31.70 at stop ₹423.23 (-8.0%, charges ₹0.0704) — the cash goes back to work at the next Friday screen
2025-09-25  INDIASHLTR  SELL ₹31.07 at stop ₹862.60 (-0.3%, charges ₹0.0690) — the cash goes back to work at the next Friday screen
2025-09-29  LGBBROSLTD  BUY ₹33.06 at ₹1,411.60 (fresh Friday signal — BUY: 3.53× weekly, month 1.72×, ladder rising; stop ₹1,258.75; charges ₹0.0780)
2025-09-29  SUBROS      BUY ₹32.89 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0776)
2025-10-03  KIMS        SELL ₹31.63 at stop ₹680.34 (+0.1%, charges ₹0.0703) — the cash goes back to work at the next Friday screen
2025-10-06  ASTRAMICRO  BUY ₹33.26 at ₹1,119.85 (fresh Friday signal — BUY: 3.17× weekly, month 1.83×, ladder rising; stop ₹1,026.00; charges ₹0.0785)
2025-10-09  FORCEMOT    SELL ₹52.45 at stop ₹15,350.10 (+65.5%, charges ₹0.1165) — the cash goes back to work at the next Friday screen
2025-10-13  RAMKY       BUY ₹32.64 at ₹622.35 (fresh Friday signal — BUY: 20.34× weekly, month 6.75×, ladder rising; stop ₹529.58; charges ₹0.0770)
2025-10-13  SHAILY      BUY ₹20.62 at ₹2,434.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 1.66×, ladder rising; stop ₹1,942.00; charges ₹0.0487)
2025-10-14  SUBROS      SELL ₹30.28 at stop ₹1,046.90 (-7.5%, charges ₹0.0672) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹30.28 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0715)
2025-10-20  CREDITACC   SELL ₹45.54 at stop ₹1,274.42 (+49.9%, charges ₹0.1011) — the cash goes back to work at the next Friday screen
2025-10-27  SKYGOLD     BUY ₹32.81 at ₹370.00 (fresh Friday signal — BUY: 1.65× weekly, month 2.25×, ladder rising; stop ₹304.38; charges ₹0.0774)
2025-11-06  ASTRAMICRO  SELL ₹30.33 at stop ₹1,026.00 (-8.4%, charges ₹0.0674) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹31.81 at stop ₹5,938.45 (-6.4%, charges ₹0.0707) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹33.12 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.0782)
2025-11-10  CUB         BUY ₹33.28 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.0786)
2025-11-20  ANANDRATHI  SELL ₹27.76 at stop ₹1,450.17 (-7.9%, charges ₹0.0617) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹31.71 at stop ₹976.41 (-3.8%, charges ₹0.0704) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹32.91 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0777)
2025-11-25  SKYGOLD     SELL ₹29.05 at stop ₹329.13 (-11.0%, charges ₹0.0645) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹33.04 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.33×, ladder rising; stop ₹535.37; charges ₹0.0780)
2025-12-01  RAMKY       SELL ₹30.18 at stop ₹578.17 (-7.1%, charges ₹0.0670) — the cash goes back to work at the next Friday screen
2025-12-01  SANSERA     BUY ₹31.04 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.0733)
2025-12-05  ASTERDM     SELL ₹22.67 at stop ₹643.62 (+1.5%, charges ₹0.0503) — the cash goes back to work at the next Friday screen
2025-12-08  KIRLOSENG   BUY ₹21.04 at ₹1,130.00 (fresh Friday signal — BUY: 1.67× weekly, month 2.31×, ladder rising; stop ₹886.54; charges ₹0.0497)
2025-12-08  NATCOPHARM  BUY ₹31.81 at ₹934.70 (fresh Friday signal — BUY: 3.52× weekly, month 3.33×, ladder rising; stop ₹825.79; charges ₹0.0751)
2025-12-15  SHAILY      SELL ₹19.74 at stop ₹2,340.80 (-3.8%, charges ₹0.0438) — the cash goes back to work at the next Friday screen
2025-12-29  HINDCOPPER  BUY ₹19.74 at ₹545.05 (fresh Friday signal — BUY: 3.05× weekly, month 3.40×, ladder rising; stop ₹345.04; charges ₹0.0466)
2026-01-08  EUREKAFORB  SELL ₹29.18 at stop ₹589.10 (-11.3%, charges ₹0.0648) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹29.44 at stop ₹2,956.49 (-10.1%, charges ₹0.0654) — the cash goes back to work at the next Friday screen
2026-01-12  KIRLOSENG   SELL ₹21.14 at stop ₹1,140.95 (+1.0%, charges ₹0.0470) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹31.67 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.0748)
2026-01-20  LGBBROSLTD  SELL ₹39.95 at stop ₹1,713.80 (+21.4%, charges ₹0.0887) — the cash goes back to work at the next Friday screen
2026-01-20  NATCOPHARM  SELL ₹27.98 at stop ₹825.79 (-11.7%, charges ₹0.0621) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹28.40 at stop ₹748.60 (-8.5%, charges ₹0.0631) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹29.54 at stop ₹1,672.76 (-4.4%, charges ₹0.0656) — the cash goes back to work at the next Friday screen
2026-02-17  NATIONALUM  SELL ₹30.05 at stop ₹335.49 (-4.7%, charges ₹0.0667) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹30.56 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.67×, ladder rising; stop ₹5,440.18; charges ₹0.0722)
2026-02-23  E2E         BUY ₹30.94 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0730)
2026-02-23  HAPPYFORGE  BUY ₹30.47 at ₹1,370.00 (fresh Friday signal — BUY: 1.58× weekly, month 2.15×, ladder rising; stop ₹1,188.64; charges ₹0.0719)
2026-02-23  VESUVIUS    BUY ₹31.03 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.0732)
2026-03-02  J&KBANK     BUY ₹29.87 at ₹116.20 (fresh Friday signal — BUY: 8.67× weekly, month 1.90×, ladder rising; stop ₹96.50; charges ₹0.0705)
2026-03-02  KSB         BUY ₹29.87 at ₹738.00 (fresh Friday signal — BUY: 52.86× weekly, month 4.79×, ladder rising; stop ₹658.54; charges ₹0.0705)
2026-03-02  TORNTPOWER  BUY ₹21.28 at ₹1,491.00 (fresh Friday signal — BUY: 1.57× weekly, month 1.69×, ladder rising; stop ₹1,315.84; charges ₹0.0502)
2026-03-04  HAPPYFORGE  SELL ₹27.32 at stop ₹1,234.05 (-9.9%, charges ₹0.0607) — the cash goes back to work at the next Friday screen
2026-03-05  VSTTILLERS  SELL ₹36.12 at stop ₹5,425.45 (+3.1%, charges ₹0.0802) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹32.77 at stop ₹251.43 (-1.1%, charges ₹0.0728) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹19.05 at stop ₹528.63 (-3.0%, charges ₹0.0423) — the cash goes back to work at the next Friday screen
2026-03-16  JBCHEPHARM  BUY ₹29.24 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0690)
2026-03-23  J&KBANK     SELL ₹28.32 at stop ₹110.67 (-4.8%, charges ₹0.0629) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹26.80 at stop ₹464.31 (-13.2%, charges ₹0.0595) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹28.52 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0673)
2026-03-30  TORNTPOWER  SELL ₹18.69 at stop ₹1,315.84 (-11.7%, charges ₹0.0415) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹13.14 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹28.51 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0673)
2026-04-13  INOXINDIA   BUY ₹29.28 at ₹1,299.10 (fresh Friday signal — BUY: 4.08× weekly, month 2.14×, ladder rising; stop ₹1,091.46; charges ₹0.0691)
2026-04-13  THERMAX     BUY ₹29.52 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.0697)
2026-04-20  GALLANTT    BUY ₹30.78 at ₹862.10 (fresh Friday signal — BUY: 15.07× weekly, month 23.99×, ladder rising; stop ₹612.75; charges ₹0.0727)
2026-05-04  KSB         SELL ₹36.96 at stop ₹917.42 (+24.3%, charges ₹0.0821) — the cash goes back to work at the next Friday screen
2026-05-11  CRAFTSMAN   BUY ₹30.93 at ₹9,039.50 (fresh Friday signal — BUY: 22.97× weekly, month 3.93×, ladder rising; stop ₹7,119.77; charges ₹0.0730)
2026-05-11  WOCKPHARMA  BUY ₹19.25 at ₹1,613.90 (fresh Friday signal — BUY: 16.73× weekly, month 3.02×, ladder rising; stop ₹1,312.90; charges ₹0.0455)
2026-05-13  INOXINDIA   SELL ₹30.78 at stop ₹1,372.18 (+5.6%, charges ₹0.0684) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹27.78 at stop ₹1,125.84 (-2.1%, charges ₹0.0617) — the cash goes back to work at the next Friday screen
2026-05-14  GALLANTT    SELL ₹27.85 at stop ₹783.75 (-9.1%, charges ₹0.0619) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹29.48 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.0696)
2026-05-18  CAPLIPOINT  BUY ₹29.47 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.0696)
2026-05-18  NLCINDIA    BUY ₹27.47 at ₹351.55 (fresh Friday signal — BUY: 5.83× weekly, month 6.05×, ladder rising; stop ₹278.49; charges ₹0.0648)
2026-06-05  E2E         SELL ₹24.63 at stop ₹2,330.72 (-20.0%, charges ₹0.0547) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹24.63 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0581)
2026-06-09  NLCINDIA    SELL ₹24.94 at stop ₹320.62 (-8.8%, charges ₹0.0554) — the cash goes back to work at the next Friday screen
2026-06-15  SFL         BUY ₹24.94 at ₹724.95 (fresh Friday signal — BUY: 2.17× weekly, month 4.11×, ladder rising; stop ₹542.50; charges ₹0.0589)
2026-07-29  THERMAX     SELL ₹35.20 at stop ₹4,306.64 (+19.8%, charges ₹0.0782) — the cash goes back to work at the next Friday screen
2026-08-03  TMB         BUY ₹33.92 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.0801)
2026-08-06  SFL         SELL ₹23.93 at stop ₹698.73 (-3.6%, charges ₹0.0531) — the cash goes back to work at the next Friday screen
2026-08-10  ASKAUTOLTD  BUY ₹25.20 at ₹648.95 (fresh Friday signal — BUY: 30.11× weekly, month 6.37×, ladder rising; stop ₹440.80; charges ₹0.0595)
2026-09-10  ALKYLAMINE  SELL ₹32.96 at stop ₹1,920.99 (+12.3%, charges ₹0.0732) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹35.76 at stop ₹7,158.25 (+17.5%, charges ₹0.0794) — the cash goes back to work at the next Friday screen
2026-09-15  SUNDRMFAST  BUY ₹32.96 at ₹1,277.30 (fresh Friday signal — BUY: 3.14× weekly, month 1.81×, ladder rising; stop ₹1,127.74; charges ₹0.0778)
2026-09-16  ASKAUTOLTD  SELL ₹23.15 at stop ₹598.78 (-7.7%, charges ₹0.0514) — the cash goes back to work at the next Friday screen
2026-09-21  ACMESOLAR   BUY ₹24.37 at ₹439.00 (fresh Friday signal — BUY: 1.96× weekly, month 1.82×, ladder rising; stop ₹370.12; charges ₹0.0575)
2026-09-21  AVALON      BUY ₹34.54 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.0815)
```
