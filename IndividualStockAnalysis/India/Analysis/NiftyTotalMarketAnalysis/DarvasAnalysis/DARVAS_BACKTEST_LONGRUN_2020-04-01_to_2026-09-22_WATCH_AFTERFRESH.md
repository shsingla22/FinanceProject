# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 1388 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹388.18** | **+23.32% a year** |
| The same system before costs and taxes | ₹488.27 | +27.78% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹289.64 | +17.87% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹388.18** (+23.32% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 441 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹21.19** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹71.47**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹31.44 | ₹0.00 | ₹6.2878 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹51.74 | ₹46.17 | ₹16.1201 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹61.14 | ₹45.49 | ₹17.9139 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹155.75 | ₹0.00 | ₹31.1500 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹19.05 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹62.21 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹51.48 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 142.92 | +42.9% | +43.6% | +70.1% |
| 2021 (2021-12-31) | 278.04 | +94.5% | +103.5% | +26.2% |
| 2022 (2022-12-30) | 327.32 | +17.7% | +25.7% | +4.3% |
| 2023 (2023-12-29) | 444.80 | +35.9% | +44.2% | +20.0% |
| 2024 (2024-12-27) | 440.25 | -1.0% | +2.3% | +9.6% |
| 2025 (2025-12-26) | 396.06 | -10.0% | -11.8% | +9.4% |
| 2026 (2026-09-22) | 388.18 | -2.0% | +2.1% | -10.1% |

## What it took to earn it

- **Maximum drawdown: -36.6%** (peak 2024-07-05 → trough 2026-04-02, on weekly closes).
- **202 closed trades**: 83 winners (41%), average winner +40.1%, average loser -10.1%.
- Best closed trade KIRLFER +354.1%; worst COMPINFO -35.4%.
- Median holding period 62 days.
- Cash share of equity averaged 9% across all weeks (median 3%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.38 | 50.01 | 5 |
| 2020-05-29 | 102.31 | 8.82 | 9 |
| 2020-06-26 | 108.07 | 0.00 | 10 |
| 2020-07-31 | 118.05 | 0.00 | 10 |
| 2020-08-28 | 120.53 | 0.00 | 10 |
| 2020-09-25 | 119.29 | 28.39 | 7 |
| 2020-10-30 | 113.35 | 5.15 | 9 |
| 2020-11-27 | 119.74 | 4.17 | 9 |
| 2020-12-24 | 142.92 | 21.78 | 8 |
| 2021-01-29 | 148.84 | 28.53 | 8 |
| 2021-02-26 | 161.87 | 0.00 | 10 |
| 2021-03-26 | 162.57 | 13.16 | 9 |
| 2021-04-30 | 173.08 | 0.00 | 10 |
| 2021-05-28 | 186.90 | 0.00 | 10 |
| 2021-06-25 | 198.66 | 0.00 | 10 |
| 2021-07-30 | 237.63 | 0.00 | 10 |
| 2021-08-27 | 226.51 | 10.61 | 10 |
| 2021-09-24 | 225.85 | 34.81 | 9 |
| 2021-10-29 | 227.36 | 40.72 | 9 |
| 2021-11-26 | 282.98 | 69.32 | 9 |
| 2021-12-31 | 278.04 | 0.00 | 11 |
| 2022-01-28 | 277.33 | 52.53 | 9 |
| 2022-02-25 | 251.28 | 110.82 | 6 |
| 2022-03-25 | 273.61 | 32.25 | 9 |
| 2022-04-29 | 284.57 | 20.42 | 9 |
| 2022-05-27 | 297.17 | 0.00 | 9 |
| 2022-06-24 | 282.94 | 26.82 | 8 |
| 2022-07-29 | 312.53 | 0.00 | 9 |
| 2022-08-26 | 326.57 | 0.00 | 9 |
| 2022-09-30 | 305.90 | 36.81 | 8 |
| 2022-10-28 | 312.66 | 2.70 | 9 |
| 2022-11-25 | 332.39 | 0.00 | 9 |
| 2022-12-30 | 327.32 | 29.02 | 9 |
| 2023-01-27 | 320.73 | 31.63 | 9 |
| 2023-02-24 | 322.49 | 0.00 | 10 |
| 2023-03-31 | 314.25 | 115.27 | 7 |
| 2023-04-28 | 307.51 | 38.06 | 9 |
| 2023-05-26 | 303.84 | 58.41 | 8 |
| 2023-06-30 | 322.92 | 0.00 | 10 |
| 2023-07-28 | 342.45 | 0.00 | 10 |
| 2023-08-25 | 367.19 | 0.00 | 10 |
| 2023-09-29 | 383.48 | 0.00 | 10 |
| 2023-10-27 | 374.96 | 120.22 | 7 |
| 2023-11-24 | 422.90 | 7.52 | 10 |
| 2023-12-29 | 444.80 | 7.52 | 10 |
| 2024-01-25 | 482.78 | 22.22 | 10 |
| 2024-02-23 | 516.17 | 12.59 | 10 |
| 2024-03-28 | 503.63 | 93.24 | 9 |
| 2024-04-26 | 497.63 | 14.37 | 10 |
| 2024-05-31 | 488.94 | 65.70 | 9 |
| 2024-06-28 | 499.48 | 16.84 | 10 |
| 2024-07-26 | 508.72 | 111.04 | 8 |
| 2024-08-30 | 496.01 | 1.13 | 10 |
| 2024-09-27 | 486.55 | 0.00 | 10 |
| 2024-10-25 | 447.97 | 171.84 | 7 |
| 2024-11-29 | 460.36 | 5.05 | 11 |
| 2024-12-27 | 440.25 | 90.10 | 9 |
| 2025-01-31 | 403.83 | 142.09 | 7 |
| 2025-02-28 | 372.06 | 139.17 | 7 |
| 2025-03-27 | 404.79 | 17.79 | 10 |
| 2025-04-25 | 429.95 | 0.00 | 10 |
| 2025-05-30 | 421.82 | 0.00 | 10 |
| 2025-06-27 | 436.15 | 49.45 | 9 |
| 2025-07-25 | 427.12 | 6.30 | 10 |
| 2025-08-29 | 430.70 | 40.81 | 9 |
| 2025-09-26 | 400.77 | 96.32 | 8 |
| 2025-10-31 | 386.77 | 19.03 | 11 |
| 2025-11-28 | 399.28 | 73.00 | 9 |
| 2025-12-26 | 396.06 | 0.00 | 11 |
| 2026-01-30 | 386.87 | 173.17 | 6 |
| 2026-02-27 | 369.71 | 0.00 | 11 |
| 2026-03-27 | 338.12 | 97.76 | 8 |
| 2026-04-30 | 361.11 | 0.00 | 11 |
| 2026-05-29 | 379.29 | 0.00 | 11 |
| 2026-06-25 | 377.93 | 0.00 | 11 |
| 2026-07-31 | 379.51 | 61.61 | 9 |
| 2026-08-28 | 395.19 | 0.00 | 11 |
| 2026-09-22 | 388.18 | 4.38 | 11 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| BLUESTONE | 2026-08-03 | 823.40 | 930.40 | 758.29 | +13.0% |
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,777.30 | 2,376.52 | +39.6% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,392.00 | 1,242.60 | +40.7% |
| GANESHHOU | 2026-07-13 | 860.50 | 736.80 | 712.60 | -14.4% |
| HEXAWARE | 2020-09-14 | 420.70 | 470.80 | 440.51 | +11.9% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| RUBICON | 2026-06-08 | 1,190.00 | 1,671.20 | 1,653.47 | +40.4% |
| SBICARD | 2026-09-07 | 653.10 | 634.95 | 581.97 | -2.8% |
| SUNDRMFAST | 2026-09-15 | 1,277.30 | 1,190.90 | 1,127.74 | -6.8% |
| TMB | 2026-08-03 | 864.90 | 883.75 | 817.00 | +2.2% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| GREENPLY | 2020-05-04 | 100.05 | 2020-05-08 | 89.49 | -10.6% |
| JKPAPER | 2020-05-11 | 96.95 | 2020-05-26 | 87.25 | -10.0% |
| LGBBROSLTD | 2020-06-01 | 222.00 | 2020-06-11 | 209.95 | -5.4% |
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| PANACEABIO | 2020-06-15 | 230.00 | 2020-08-20 | 184.01 | -20.0% |
| APCOTEXIND | 2020-08-24 | 164.95 | 2020-08-31 | 151.95 | -7.9% |
| NESTLEIND | 2020-04-27 | 879.25 | 2020-09-01 | 793.25 | -9.8% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| BALAJITELE | 2020-05-04 | 61.40 | 2020-09-09 | 74.07 | +20.6% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| DEEPAKFERT | 2020-05-11 | 101.00 | 2020-09-22 | 154.26 | +52.7% |
| PRINCEPIPE | 2020-09-07 | 208.00 | 2020-10-12 | 220.88 | +6.2% |
| ALEMBICLTD | 2020-06-22 | 81.65 | 2020-11-02 | 91.41 | +12.0% |
| GLAXO | 2020-09-14 | 1,675.00 | 2020-11-02 | 1,441.55 | -13.9% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| JINDWORLD | 2020-11-09 | 50.00 | 2021-03-01 | 52.12 | +4.2% |
| APTECHT | 2021-02-01 | 178.45 | 2021-03-19 | 204.25 | +14.5% |
| MHRIL | 2021-02-01 | 224.00 | 2021-03-19 | 210.90 | -5.8% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| CENTRUM | 2021-03-30 | 28.40 | 2021-04-12 | 24.89 | -12.4% |
| GFLLIMITED | 2021-03-22 | 93.00 | 2021-04-13 | 74.39 | -20.0% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| KIRLFER | 2020-06-15 | 61.55 | 2021-08-10 | 279.49 | +354.1% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| GDL | 2021-01-25 | 158.00 | 2021-09-20 | 266.00 | +68.4% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| NEOGEN | 2021-09-27 | 1,255.00 | 2021-10-25 | 1,142.85 | -8.9% |
| INDOCO | 2021-08-16 | 484.30 | 2021-11-12 | 412.30 | -14.9% |
| BIGBLOC | 2021-11-15 | 39.80 | 2021-11-16 | 142.59 | +258.3% |
| EMAMIPAP | 2021-04-19 | 125.00 | 2021-11-22 | 141.55 | +13.2% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-11-01 | 11,040.00 | 2021-11-26 | 10,070.05 | -8.8% |
| SOMANYCERA | 2021-06-21 | 594.85 | 2021-11-29 | 755.11 | +26.9% |
| MAHLOG | 2021-01-25 | 495.85 | 2021-11-30 | 654.55 | +32.0% |
| SUPRAJIT | 2021-11-22 | 454.00 | 2021-12-13 | 391.40 | -13.8% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| MINDAIND | 2021-12-20 | 1,026.00 | 2022-01-07 | 1,088.41 | +6.1% |
| LTTS | 2020-10-19 | 1,745.00 | 2022-01-21 | 4,856.88 | +178.3% |
| TVTODAY | 2021-11-22 | 320.24 | 2022-01-24 | 311.68 | -2.7% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| TV18BRDCST | 2022-01-31 | 58.90 | 2022-02-22 | 58.38 | -0.9% |
| CHAMBLFERT | 2021-12-06 | 407.45 | 2022-02-24 | 353.85 | -13.2% |
| COMPINFO | 2022-01-10 | 45.00 | 2022-02-24 | 29.08 | -35.4% |
| JSWISPL | 2022-01-24 | 37.50 | 2022-02-24 | 30.25 | -19.3% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| BAJAJHLDNG | 2021-09-27 | 4,979.00 | 2022-05-11 | 4,853.07 | -2.5% |
| EVEREADY | 2022-03-28 | 344.00 | 2022-05-11 | 310.46 | -9.8% |
| MFL | 2022-05-02 | 1,430.00 | 2022-05-11 | 1,225.50 | -14.3% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| KRISHANA | 2022-05-16 | 67.96 | 2022-06-16 | 54.77 | -19.4% |
| JSWENERGY | 2021-03-08 | 81.85 | 2022-06-20 | 201.99 | +146.8% |
| MFL | 2022-06-27 | 1,262.00 | 2022-08-05 | 1,398.40 | +10.8% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| RAJMET | 2022-02-28 | 265.00 | 2022-09-15 | 359.30 | +35.6% |
| NAVNETEDUL | 2022-08-08 | 130.50 | 2022-09-26 | 127.30 | -2.5% |
| SUNDARMHLD | 2022-10-03 | 103.50 | 2022-10-11 | 92.20 | -10.9% |
| FAIRCHEMOR | 2022-10-17 | 2,240.00 | 2022-11-01 | 1,790.15 | -20.1% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| RVNL | 2022-11-07 | 46.85 | 2022-12-26 | 60.57 | +29.3% |
| KSL | 2022-12-26 | 330.10 | 2023-01-27 | 328.23 | -0.6% |
| GICRE | 2022-12-26 | 157.00 | 2023-02-01 | 167.72 | +6.8% |
| LSIL | 2023-01-30 | 23.20 | 2023-02-07 | 20.04 | -13.6% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| KABRAEXTRU | 2022-12-26 | 441.95 | 2023-03-14 | 506.92 | +14.7% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| JINDALSAW | 2023-02-06 | 65.22 | 2023-03-27 | 67.92 | +4.1% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| SONATSOFTW | 2023-03-20 | 397.50 | 2023-03-29 | 371.45 | -6.6% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| MUKANDLTD | 2023-01-02 | 136.70 | 2023-05-17 | 116.23 | -15.0% |
| DCAL | 2023-03-27 | 127.95 | 2023-05-24 | 115.42 | -9.8% |
| VSSL | 2023-02-13 | 345.70 | 2023-05-26 | 324.52 | -6.1% |
| KSB | 2023-04-03 | 426.00 | 2023-07-12 | 407.74 | -4.3% |
| THANGAMAYL | 2023-05-29 | 1,344.00 | 2023-07-17 | 1,344.25 | +0.0% |
| GANESHHOUC | 2023-07-24 | 457.00 | 2023-08-14 | 418.62 | -8.4% |
| INGERRAND | 2023-04-03 | 2,690.00 | 2023-09-13 | 3,022.99 | +12.4% |
| OLECTRA | 2023-04-03 | 623.50 | 2023-10-19 | 1,121.00 | +79.8% |
| SCHNEIDER | 2023-05-29 | 236.80 | 2023-10-23 | 315.45 | +33.2% |
| SJVN | 2023-09-18 | 75.35 | 2023-10-23 | 66.03 | -12.4% |
| SHARDAMOTR | 2023-05-22 | 380.00 | 2023-10-25 | 465.07 | +22.4% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| ASTRAZEN | 2023-08-21 | 4,099.85 | 2024-02-09 | 5,795.95 | +41.4% |
| GLS | 2023-05-02 | 509.05 | 2024-03-05 | 779.48 | +53.1% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| TIPSINDLTD | 2023-10-23 | 358.00 | 2024-03-13 | 453.39 | +26.6% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| DOLLAR | 2024-03-11 | 527.95 | 2024-03-13 | 461.65 | -12.6% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| ANANDRATHI | 2023-07-17 | 265.70 | 2024-03-27 | 862.65 | +224.7% |
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| BOSCHLTD | 2024-03-18 | 29,500.05 | 2024-06-04 | 29,015.09 | -1.6% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| ARE&M | 2024-06-10 | 1,450.00 | 2024-07-22 | 1,502.14 | +3.6% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| KIRLOSBROS | 2024-05-21 | 1,844.00 | 2024-08-05 | 1,987.46 | +7.8% |
| EMUDHRA | 2024-03-18 | 583.90 | 2024-08-13 | 793.11 | +35.8% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| AVANTIFEED | 2024-07-29 | 697.65 | 2024-09-09 | 650.13 | -6.8% |
| IOB | 2024-02-12 | 71.50 | 2024-10-03 | 56.57 | -20.9% |
| VGUARD | 2024-08-19 | 524.15 | 2024-10-04 | 420.24 | -19.8% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| INDIAGLYCO | 2024-07-22 | 515.00 | 2024-10-25 | 587.91 | +14.2% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| PRAJIND | 2024-10-28 | 687.95 | 2024-11-13 | 675.21 | -1.9% |
| ASTRAZEN | 2024-10-28 | 7,142.20 | 2024-11-14 | 6,854.77 | -4.0% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| UNICHEMLAB | 2024-11-18 | 893.55 | 2024-12-20 | 711.49 | -20.4% |
| PRSMJOHNSN | 2024-09-16 | 214.51 | 2024-12-26 | 170.55 | -20.5% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| PAYTM | 2024-10-28 | 747.70 | 2025-01-09 | 893.05 | +19.4% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| EMSLIMITED | 2024-12-23 | 916.85 | 2025-01-10 | 802.65 | -12.5% |
| CARERATING | 2024-10-28 | 1,396.00 | 2025-01-13 | 1,239.70 | -11.2% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| PTCIL | 2025-01-20 | 16,420.00 | 2025-01-21 | 15,417.55 | -6.1% |
| VARROC | 2025-01-13 | 590.00 | 2025-01-22 | 563.49 | -4.5% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| BSE | 2024-10-07 | 4,190.00 | 2025-02-28 | 4,954.63 | +18.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| GRWRHITECH | 2025-03-10 | 4,219.95 | 2025-04-03 | 3,602.82 | -14.6% |
| SUVENPHAR | 2025-03-10 | 1,166.00 | 2025-04-07 | 1,038.10 | -11.0% |
| AARTIPHARM | 2025-03-10 | 744.90 | 2025-04-07 | 640.24 | -14.1% |
| ITDCEM | 2024-10-07 | 655.05 | 2025-04-11 | 524.92 | -19.9% |
| TEJASNET | 2025-04-15 | 859.00 | 2025-05-09 | 679.16 | -20.9% |
| FINEORG | 2025-04-07 | 3,600.15 | 2025-06-23 | 4,498.25 | +24.9% |
| KPRMILL | 2025-05-12 | 1,302.00 | 2025-08-01 | 1,108.74 | -14.8% |
| JSWHL | 2024-11-18 | 19,990.00 | 2025-08-04 | 19,106.01 | -4.4% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| ALKYLAMINE | 2025-06-30 | 2,263.00 | 2025-08-07 | 2,087.62 | -7.7% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| PARADEEP | 2025-08-11 | 226.25 | 2025-09-08 | 193.88 | -14.3% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| RSYSTEMS | 2025-09-01 | 460.00 | 2025-09-24 | 423.23 | -8.0% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| DMART | 2025-01-20 | 3,624.00 | 2025-10-03 | 4,404.96 | +21.5% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| SHOPERSTOP | 2025-08-11 | 512.60 | 2025-11-04 | 485.55 | -5.3% |
| PGHL | 2025-08-04 | 6,440.00 | 2025-11-06 | 5,938.45 | -7.8% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| ASTRAMICRO | 2025-10-06 | 1,119.85 | 2025-11-06 | 1,026.00 | -8.4% |
| VMART | 2025-10-27 | 858.00 | 2025-11-07 | 806.50 | -6.0% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| TDPOWERSYS | 2025-11-10 | 389.50 | 2025-11-24 | 357.49 | -8.2% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| GRAVITA | 2025-11-10 | 1,711.00 | 2026-01-09 | 1,678.56 | -1.9% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| LGBBROSLTD | 2025-09-29 | 1,411.60 | 2026-01-20 | 1,713.80 | +21.4% |
| JBMA | 2026-01-19 | 592.05 | 2026-01-20 | 556.03 | -6.1% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| LTF | 2025-11-10 | 304.00 | 2026-01-21 | 281.77 | -7.3% |
| MARUTI | 2025-09-15 | 15,350.00 | 2026-01-23 | 15,657.90 | +2.0% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| TATAELXSI | 2026-02-02 | 5,448.00 | 2026-02-12 | 5,016.48 | -7.9% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| CEIGALL | 2026-02-02 | 274.95 | 2026-03-04 | 266.33 | -3.1% |
| HAPPYFORGE | 2026-02-23 | 1,370.00 | 2026-03-04 | 1,234.05 | -9.9% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| HINDCOPPER | 2026-01-12 | 532.00 | 2026-03-12 | 528.63 | -0.6% |
| RBA | 2026-01-27 | 64.07 | 2026-03-12 | 61.08 | -4.7% |
| HEROMOTOCO | 2025-10-06 | 5,527.00 | 2026-03-13 | 5,237.35 | -5.2% |
| SANSERA | 2026-03-09 | 2,125.10 | 2026-03-13 | 2,033.00 | -4.3% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-16 | 121.14 | 2026-03-23 | 110.67 | -8.6% |
| MAHABANK | 2026-02-02 | 60.48 | 2026-03-30 | 61.05 | +0.9% |
| ABSLAMC | 2026-03-23 | 937.90 | 2026-03-30 | 876.18 | -6.6% |
| INOXINDIA | 2026-04-13 | 1,299.10 | 2026-05-13 | 1,372.18 | +5.6% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| GALLANTT | 2026-04-20 | 862.10 | 2026-05-14 | 783.75 | -9.1% |
| E2E | 2026-02-23 | 2,914.00 | 2026-06-05 | 2,330.72 | -20.0% |
| NLCINDIA | 2026-05-18 | 351.55 | 2026-06-09 | 320.62 | -8.8% |
| POWERMECH | 2026-06-15 | 2,859.90 | 2026-07-07 | 2,603.29 | -9.0% |
| THERMAX | 2026-04-13 | 3,596.00 | 2026-07-29 | 4,306.64 | +19.8% |
| VTL | 2026-03-09 | 532.95 | 2026-07-31 | 592.80 | +11.2% |
| BHARATFORG | 2026-03-23 | 1,700.00 | 2026-09-04 | 1,953.29 | +14.9% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-02-23 | 6,090.00 | 2026-09-15 | 7,158.25 | +17.5% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_WATCH_AFTERFRESH.csv` beside this report (19763 events in all).*

```
2020-04-13  DEEPAKNTR   BUY ₹10.00 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 2.47×, ladder rising; stop ₹240.25; charges ₹0.0118)
2020-04-27  CADILAHC    BUY ₹9.98 at ₹330.30 (fresh Friday signal — ACCUMULATE: surged 10.60× weekly on 2020-04-09 (month 3.50×), ladder rising NOW — promoted from the ladder watch; stop ₹310.03; charges ₹0.0118)
2020-04-27  NESTLEIND   BUY ₹9.99 at ₹879.25 (fresh Friday signal — ACCUMULATE: surged 2.03× weekly on 2020-04-09 (month 2.43×), ladder rising NOW — promoted from the ladder watch; stop ₹793.25; charges ₹0.0118)
2020-04-27  SYNGENE     BUY ₹10.01 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.94×, ladder rising; stop ₹285.95; charges ₹0.0119)
2020-04-27  TAJGVK      BUY ₹10.01 at ₹133.40 (fresh Friday signal — BUY: 6.65× weekly, month 2.23×, ladder rising; stop ₹106.49; charges ₹0.0119)
2020-05-04  BALAJITELE  BUY ₹9.93 at ₹61.40 (fresh Friday signal — BUY: surged 4.19× weekly on 2020-04-24 (month 2.47×), ladder rising NOW — promoted from the ladder watch; stop ₹48.55; charges ₹0.0118)
2020-05-04  GREENPLY    BUY ₹9.86 at ₹100.05 (fresh Friday signal — ACCUMULATE: surged 3.61× weekly on 2020-04-24 (month 1.51×), ladder rising NOW — promoted from the ladder watch; stop ₹89.49; charges ₹0.0117)
2020-05-08  GREENPLY    SELL ₹8.80 at stop ₹89.49 (-10.6%, charges ₹0.0091) — the cash goes back to work at the next Friday screen
2020-05-11  APLLTD      BUY ₹9.82 at ₹774.70 (fresh Friday signal — ACCUMULATE: surged 5.92× weekly on 2020-04-24 (month 3.96×), ladder rising NOW — promoted from the ladder watch; stop ₹694.45; charges ₹0.0116)
2020-05-11  DEEPAKFERT  BUY ₹9.56 at ₹101.00 (fresh Friday signal — ACCUMULATE: surged 4.08× weekly on 2020-04-30 (month 3.79×), ladder rising NOW — promoted from the ladder watch; stop ₹91.29; charges ₹0.0113)
2020-05-11  IOLCP       BUY ₹9.82 at ₹66.18 (fresh Friday signal — BUY: 2.18× weekly, month 2.65×, ladder rising; stop ₹51.22; charges ₹0.0116)
2020-05-11  JKPAPER     BUY ₹9.82 at ₹96.95 (fresh Friday signal — ACCUMULATE: surged 4.21× weekly on 2020-04-30 (month 1.95×), ladder rising NOW — promoted from the ladder watch; stop ₹87.25; charges ₹0.0116)
2020-05-26  JKPAPER     SELL ₹8.82 at stop ₹87.25 (-10.0%, charges ₹0.0091) — the cash goes back to work at the next Friday screen
2020-06-01  LGBBROSLTD  BUY ₹8.82 at ₹222.00 (fresh Friday signal — BUY: 6.99× weekly, month 2.00×, ladder rising; stop ₹175.24; charges ₹0.0104)
2020-06-11  LGBBROSLTD  SELL ₹8.32 at stop ₹209.95 (-5.4%, charges ₹0.0086) — the cash goes back to work at the next Friday screen
2020-06-12  DEEPAKNTR   SELL ₹9.97 at stop ₹474.05 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-06-15  KIRLFER     BUY ₹7.75 at ₹61.55 (fresh Friday signal — BUY: 8.70× weekly, month 2.09×, ladder rising; stop ₹48.49; charges ₹0.0092)
2020-06-15  PANACEABIO  BUY ₹10.54 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.25×, ladder rising; stop ₹114.11; charges ₹0.0125)
2020-06-16  IOLCP       SELL ₹10.27 at stop ₹69.35 (+4.8%, charges ₹0.0107) — the cash goes back to work at the next Friday screen
2020-06-22  ALEMBICLTD  BUY ₹10.27 at ₹81.65 (fresh Friday signal — BUY: 11.73× weekly, month 8.49×, ladder rising; stop ₹44.84; charges ₹0.0122)
2020-08-20  PANACEABIO  SELL ₹8.41 at stop ₹184.01 (-20.0%, charges ₹0.0087) — the cash goes back to work at the next Friday screen
2020-08-24  APCOTEXIND  BUY ₹8.41 at ₹164.95 (fresh Friday signal — BUY: 8.08× weekly, month 5.83×, ladder rising; stop ₹119.51; charges ₹0.0100)
2020-08-31  APCOTEXIND  SELL ₹7.73 at stop ₹151.95 (-7.9%, charges ₹0.0080) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.74 at stop ₹928.62 (+19.9%, charges ₹0.0122) — the cash goes back to work at the next Friday screen
2020-09-01  NESTLEIND   SELL ₹8.99 at stop ₹793.25 (-9.8%, charges ₹0.0093) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹11.63 at ₹1,398.95 (fresh Friday signal — BUY: 5.36× weekly, month 3.91×, ladder rising; stop ₹1,211.25; charges ₹0.0138)
2020-09-07  PRINCEPIPE  BUY ₹11.58 at ₹208.00 (fresh Friday signal — BUY: 3.47× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.0137)
2020-09-08  CADILAHC    SELL ₹11.00 at stop ₹364.99 (+10.5%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2020-09-09  BALAJITELE  SELL ₹11.95 at stop ₹74.07 (+20.6%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-14  GLAXO       BUY ₹11.91 at ₹1,675.00 (fresh Friday signal — BUY: 2.58× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.0141)
2020-09-14  HEXAWARE    BUY ₹11.95 at ₹420.70 (fresh Friday signal — ACCUMULATE: 2.47× weekly, month 2.36×, ladder rising; stop ₹371.55; charges ₹0.0142)
2020-09-22  DEEPAKFERT  SELL ₹14.57 at stop ₹154.26 (+52.7%, charges ₹0.0151) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹9.47 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹11.97 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0142)
2020-09-28  SAKSOFT     BUY ₹12.00 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.0142)
2020-10-12  PRINCEPIPE  SELL ₹12.27 at stop ₹220.88 (+6.2%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2020-10-19  LTTS        BUY ₹11.55 at ₹1,745.00 (fresh Friday signal — BUY: 4.76× weekly, month 2.59×, ladder rising; stop ₹1,482.95; charges ₹0.0137)
2020-11-02  ALEMBICLTD  SELL ₹11.47 at stop ₹91.41 (+12.0%, charges ₹0.0119) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹10.23 at stop ₹1,441.55 (-13.9%, charges ₹0.0106) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹11.33 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.0134)
2020-11-09  JINDWORLD   BUY ₹11.35 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.28× weekly, month 1.55×, ladder rising; stop ₹39.81; charges ₹0.0134)
2020-12-22  SYNGENE     SELL ₹17.61 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-28  PAISALO     BUY ₹14.69 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0174)
2021-01-20  BORORENEW   SELL ₹28.07 at stop ₹247.59 (+148.3%, charges ₹0.0291) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹14.97 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.79×, ladder rising; stop ₹92.41; charges ₹0.0177)
2021-01-25  MAHLOG      BUY ₹15.13 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹0.0179)
2021-01-25  SAKSOFT     SELL ₹10.24 at stop ₹341.10 (-14.4%, charges ₹0.0106) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹13.22 at stop ₹928.05 (+10.7%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹15.02 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.0178)
2021-02-01  MHRIL       BUY ₹13.51 at ₹224.00 (fresh Friday signal — BUY: 1.64× weekly, month 1.67×, ladder rising; stop ₹200.74; charges ₹0.0160)
2021-03-01  JINDWORLD   SELL ₹11.80 at stop ₹52.12 (+4.2%, charges ₹0.0122) — the cash goes back to work at the next Friday screen
2021-03-08  JSWENERGY   BUY ₹11.80 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.50×, ladder rising; stop ₹65.79; charges ₹0.0140)
2021-03-19  APTECHT     SELL ₹17.15 at stop ₹204.25 (+14.5%, charges ₹0.0178) — the cash goes back to work at the next Friday screen
2021-03-19  MHRIL       SELL ₹12.69 at stop ₹210.90 (-5.8%, charges ₹0.0132) — the cash goes back to work at the next Friday screen
2021-03-22  GFLLIMITED  BUY ₹13.95 at ₹93.00 (fresh Friday signal — ACCUMULATE: 6.17× weekly, month 3.98×, ladder rising; stop ₹74.39; charges ₹0.0165)
2021-03-22  VIDHIING    BUY ₹15.89 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0188)
2021-03-25  BANARISUG   SELL ₹13.16 at stop ₹1,586.36 (+13.4%, charges ₹0.0136) — the cash goes back to work at the next Friday screen
2021-03-30  CENTRUM     BUY ₹13.16 at ₹28.40 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 6.70×, ladder rising; stop ₹24.89; charges ₹0.0156)
2021-04-01  CENTRUM     TRIM 3.8% (₹0.49 at ₹28.35) to pay the tax bill
2021-04-01  GDL         TRIM 3.8% (₹0.63 at ₹177.90) to pay the tax bill
2021-04-01  GFLLIMITED  TRIM 3.8% (₹0.61 at ₹108.35) to pay the tax bill
2021-04-01  HEXAWARE    TRIM 3.8% (₹0.50 at ₹470.80) to pay the tax bill
2021-04-01  JSWENERGY   TRIM 3.8% (₹0.49 at ₹90.70) to pay the tax bill
2021-04-01  KIRLFER     TRIM 3.8% (₹0.82 at ₹173.50) to pay the tax bill
2021-04-01  LTTS        TRIM 3.8% (₹0.68 at ₹2,720.60) to pay the tax bill
2021-04-01  MAHLOG      TRIM 3.8% (₹0.66 at ₹574.75) to pay the tax bill
2021-04-01  PAISALO     TRIM 3.8% (₹0.76 at ₹78.11) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹6.2878 paid (STCG ₹31.44 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  VIDHIING    TRIM 3.8% (₹0.64 at ₹207.10) to pay the tax bill
2021-04-12  CENTRUM     SELL ₹11.07 at stop ₹24.89 (-12.4%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹17.92 at stop ₹72.41 (+27.1%, charges ₹0.0186) — the cash goes back to work at the next Friday screen
2021-04-13  GFLLIMITED  SELL ₹10.71 at stop ₹74.39 (-20.0%, charges ₹0.0111) — the cash goes back to work at the next Friday screen
2021-04-19  EMAMIPAP    BUY ₹9.46 at ₹125.00 (fresh Friday signal — ACCUMULATE: surged 37.60× weekly on 2021-03-19 (month 15.67×), ladder rising NOW — promoted from the ladder watch; stop ₹81.22; charges ₹0.0112)
2021-04-19  KPRMILL     BUY ₹15.12 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0179)
2021-04-19  MOREPENLAB  BUY ₹15.13 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹0.0179)
2021-06-18  VIDHIING    SELL ₹14.31 at stop ₹182.64 (-6.2%, charges ₹0.0148) — the cash goes back to work at the next Friday screen
2021-06-21  SOMANYCERA  BUY ₹14.31 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0170)
2021-08-10  KIRLFER     SELL ₹33.79 at stop ₹279.49 (+354.1%, charges ₹0.0351) — the cash goes back to work at the next Friday screen
2021-08-10  MOREPENLAB  SELL ₹22.71 at stop ₹56.33 (+50.4%, charges ₹0.0236) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹22.53 at stop ₹352.48 (+49.4%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹22.84 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.0271)
2021-08-16  INDOCO      BUY ₹22.77 at ₹484.30 (fresh Friday signal — BUY: 4.80× weekly, month 2.73×, ladder rising; stop ₹412.30; charges ₹0.0270)
2021-08-16  TATAINVEST  BUY ₹22.82 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0270)
2021-09-20  GDL         SELL ₹24.20 at stop ₹266.00 (+68.4%, charges ₹0.0251) — the cash goes back to work at the next Friday screen
2021-09-27  BAJAJHLDNG  BUY ₹11.94 at ₹4,979.00 (fresh Friday signal — BUY: 4.52× weekly, month 1.97×, ladder rising; stop ₹4,184.75; charges ₹0.0141)
2021-09-27  NEOGEN      BUY ₹22.87 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0271)
2021-10-25  BASF        SELL ₹19.94 at stop ₹3,220.59 (-12.5%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2021-10-25  NEOGEN      SELL ₹20.78 at stop ₹1,142.85 (-8.9%, charges ₹0.0216) — the cash goes back to work at the next Friday screen
2021-11-01  TCIEXP      BUY ₹17.94 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0213)
2021-11-01  TTKPRESTIG  BUY ₹22.79 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.0270)
2021-11-12  INDOCO      SELL ₹19.34 at stop ₹412.30 (-14.9%, charges ₹0.0201) — the cash goes back to work at the next Friday screen
2021-11-15  BIGBLOC     BUY ₹19.34 at ₹39.80 (fresh Friday signal — BUY: 6.89× weekly, month 4.00×, ladder rising; stop ₹142.59; charges ₹0.0229)
2021-11-16  BIGBLOC     SELL ₹69.14 at stop ₹142.59 (+258.3%, charges ₹0.0717) — the cash goes back to work at the next Friday screen
2021-11-22  EMAMIPAP    SELL ₹10.69 at stop ₹141.55 (+13.2%, charges ₹0.0111) — the cash goes back to work at the next Friday screen
2021-11-22  SUPRAJIT    BUY ₹28.02 at ₹454.00 (fresh Friday signal — BUY: 10.19× weekly, month 1.96×, ladder rising; stop ₹309.33; charges ₹0.0332)
2021-11-22  TVTODAY     BUY ₹28.22 at ₹320.24 (fresh Friday signal — BUY: 15.58× weekly, month 3.55×, ladder rising; stop ₹253.08; charges ₹0.0334)
2021-11-26  TATAINVEST  SELL ₹25.00 at stop ₹1,436.49 (+9.8%, charges ₹0.0259) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹20.74 at stop ₹10,070.05 (-8.8%, charges ₹0.0215) — the cash goes back to work at the next Friday screen
2021-11-29  RAYMOND     BUY ₹27.62 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0327)
2021-11-29  RSYSTEMS    BUY ₹27.78 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0329)
2021-11-29  SOMANYCERA  SELL ₹18.13 at stop ₹755.11 (+26.9%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2021-11-30  MAHLOG      SELL ₹19.17 at stop ₹654.55 (+32.0%, charges ₹0.0199) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹27.53 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0326)
2021-12-06  CHAMBLFERT  BUY ₹23.69 at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹0.0281)
2021-12-13  SUPRAJIT    SELL ₹24.11 at stop ₹391.40 (-13.8%, charges ₹0.0250) — the cash goes back to work at the next Friday screen
2021-12-16  RSYSTEMS    SELL ₹24.84 at stop ₹291.18 (-10.4%, charges ₹0.0258) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹26.85 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0318)
2021-12-20  MINDAIND    BUY ₹22.10 at ₹1,026.00 (fresh Friday signal — BUY: 5.05× weekly, month 1.81×, ladder rising; stop ₹787.66; charges ₹0.0262)
2021-12-21  TCIEXP      SELL ₹19.93 at stop ₹2,039.74 (+11.4%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹19.93 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0236)
2022-01-07  MINDAIND    SELL ₹23.39 at stop ₹1,088.41 (+6.1%, charges ₹0.0243) — the cash goes back to work at the next Friday screen
2022-01-10  COMPINFO    BUY ₹23.39 at ₹45.00 (fresh Friday signal — BUY: 4.39× weekly, month 5.27×, ladder rising; stop ₹25.44; charges ₹0.0277)
2022-01-21  LTTS        SELL ₹30.86 at stop ₹4,856.88 (+178.3%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2022-01-24  JSWISPL     BUY ₹27.32 at ₹37.50 (fresh Friday signal — BUY: 5.58× weekly, month 4.04×, ladder rising; stop ₹27.79; charges ₹0.0324)
2022-01-24  TVTODAY     SELL ₹27.41 at stop ₹311.68 (-2.7%, charges ₹0.0284) — the cash goes back to work at the next Friday screen
2022-01-25  SWANENERGY  SELL ₹21.58 at stop ₹162.64 (+8.5%, charges ₹0.0224) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹27.63 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0327)
2022-01-31  TV18BRDCST  BUY ₹24.89 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.0295)
2022-02-11  SHARDACROP  SELL ₹25.63 at stop ₹545.30 (-7.1%, charges ₹0.0266) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹25.63 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0304)
2022-02-15  RAYMOND     SELL ₹31.42 at stop ₹679.35 (+14.0%, charges ₹0.0326) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹25.93 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0307)
2022-02-22  GREENLAM    SELL ₹23.11 at stop ₹313.67 (-13.7%, charges ₹0.0240) — the cash goes back to work at the next Friday screen
2022-02-22  TV18BRDCST  SELL ₹24.62 at stop ₹58.38 (-0.9%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹20.53 at stop ₹353.85 (-13.2%, charges ₹0.0213) — the cash goes back to work at the next Friday screen
2022-02-24  COMPINFO    SELL ₹15.08 at stop ₹29.08 (-35.4%, charges ₹0.0156) — the cash goes back to work at the next Friday screen
2022-02-24  JSWISPL     SELL ₹21.99 at stop ₹30.25 (-19.3%, charges ₹0.0228) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹25.40 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0301)
2022-02-28  RAJMET      BUY ₹25.52 at ₹265.00 (fresh Friday signal — ACCUMULATE: surged 6.93× weekly on 2022-02-18 (month 4.62×), ladder rising NOW — promoted from the ladder watch; stop ₹226.96; charges ₹0.0302)
2022-02-28  SHANTIGEAR  BUY ₹25.67 at ₹185.30 (fresh Friday signal — BUY: surged 3.40× weekly on 2022-02-11 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹170.29; charges ₹0.0304)
2022-03-07  GTLINFRA    BUY ₹25.73 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0305)
2022-03-21  BSE         SELL ₹23.75 at stop ₹1,634.39 (-13.5%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2022-03-28  EVEREADY    BUY ₹27.12 at ₹344.00 (fresh Friday signal — ACCUMULATE: surged 3.19× weekly on 2022-03-04 (month 2.42×), ladder rising NOW — promoted from the ladder watch; stop ₹310.46; charges ₹0.0321)
2022-04-01  BAJAJHLDNG  TRIM 4.1% (₹0.53 at ₹5,398.85) to pay the tax bill
2022-04-01  CGCL        TRIM 4.1% (₹1.08 at ₹614.95) to pay the tax bill
2022-04-01  DANGEE      TRIM 4.1% (₹1.37 at ₹310.25) to pay the tax bill
2022-04-01  EVEREADY    TRIM 4.1% (₹1.09 at ₹338.95) to pay the tax bill
2022-04-01  GTLINFRA    TRIM 4.1% (₹0.96 at ₹1.55) to pay the tax bill
2022-04-01  HEXAWARE    TRIM 4.1% (₹0.52 at ₹470.80) to pay the tax bill
2022-04-01  JSWENERGY   TRIM 4.1% (₹1.43 at ₹253.45) to pay the tax bill
2022-04-01  MBAPL       TRIM 4.1% (₹1.61 at ₹80.05) to pay the tax bill
2022-04-01  RAJMET      TRIM 4.1% (₹1.37 at ₹349.70) to pay the tax bill
2022-04-01  SHANTIGEAR  TRIM 4.1% (₹1.04 at ₹183.85) to pay the tax bill
2022-04-01  TAX         FY2022 settled: ₹16.1201 paid (STCG ₹51.74 @20%, LTCG ₹46.17 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-29  GTLINFRA    SELL ₹20.42 at stop ₹1.41 (-17.1%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹20.42 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.0242)
2022-05-11  BAJAJHLDNG  SELL ₹11.14 at stop ₹4,853.07 (-2.5%, charges ₹0.0116) — the cash goes back to work at the next Friday screen
2022-05-11  EVEREADY    SELL ₹23.43 at stop ₹310.46 (-9.8%, charges ₹0.0243) — the cash goes back to work at the next Friday screen
2022-05-11  MFL         SELL ₹17.46 at stop ₹1,225.50 (-14.3%, charges ₹0.0181) — the cash goes back to work at the next Friday screen
2022-05-16  KRISHANA    BUY ₹23.63 at ₹67.96 (fresh Friday signal — ACCUMULATE: 1.67× weekly, month 1.86×, ladder rising; stop ₹54.77; charges ₹0.0280)
2022-05-16  VBL         BUY ₹28.40 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0336)
2022-06-06  VBL         SELL ₹25.28 at stop ₹196.27 (-10.8%, charges ₹0.0262) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹25.28 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0300)
2022-06-16  KRISHANA    SELL ₹19.00 at stop ₹54.77 (-19.4%, charges ₹0.0197) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹19.00 at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹0.0225)
2022-06-20  JSWENERGY   SELL ₹26.82 at stop ₹201.99 (+146.8%, charges ₹0.0278) — the cash goes back to work at the next Friday screen
2022-06-27  MFL         BUY ₹26.82 at ₹1,262.00 (fresh Friday signal — ACCUMULATE: surged 1.77× weekly on 2022-06-03 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹1,064.04; charges ₹0.0318)
2022-08-05  MFL         SELL ₹29.65 at stop ₹1,398.40 (+10.8%, charges ₹0.0308) — the cash goes back to work at the next Friday screen
2022-08-08  NAVNETEDUL  BUY ₹29.65 at ₹130.50 (fresh Friday signal — BUY: 14.73× weekly, month 3.84×, ladder rising; stop ₹88.40; charges ₹0.0351)
2022-09-06  DANGEE      SELL ₹38.82 at stop ₹375.25 (+59.7%, charges ₹0.0403) — the cash goes back to work at the next Friday screen
2022-09-12  SHREECEM    BUY ₹32.41 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0384)
2022-09-15  RAJMET      SELL ₹33.12 at stop ₹359.30 (+35.6%, charges ₹0.0344) — the cash goes back to work at the next Friday screen
2022-09-19  JSWHL       BUY ₹31.57 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0374)
2022-09-26  NAVNETEDUL  SELL ₹28.86 at stop ₹127.30 (-2.5%, charges ₹0.0299) — the cash goes back to work at the next Friday screen
2022-10-03  SUNDARMHLD  BUY ₹30.45 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹0.0361)
2022-10-11  SUNDARMHLD  SELL ₹27.07 at stop ₹92.20 (-10.9%, charges ₹0.0281) — the cash goes back to work at the next Friday screen
2022-10-17  FAIRCHEMOR  BUY ₹30.72 at ₹2,240.00 (fresh Friday signal — ACCUMULATE: 2.93× weekly, month 2.97×, ladder rising; stop ₹1,790.15; charges ₹0.0364)
2022-11-01  FAIRCHEMOR  SELL ₹24.50 at stop ₹1,790.15 (-20.1%, charges ₹0.0254) — the cash goes back to work at the next Friday screen
2022-11-03  APARINDS    SELL ₹27.11 at stop ₹1,358.50 (+43.0%, charges ₹0.0281) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹31.81 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0377)
2022-11-07  RVNL        BUY ₹22.50 at ₹46.85 (fresh Friday signal — BUY: 4.42× weekly, month 4.42×, ladder rising; stop ₹33.77; charges ₹0.0267)
2022-12-21  ELECON      SELL ₹41.70 at stop ₹202.49 (+65.3%, charges ₹0.0433) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹45.82 at stop ₹345.56 (+86.5%, charges ₹0.0475) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹31.71 at stop ₹139.84 (-0.1%, charges ₹0.0329) — the cash goes back to work at the next Friday screen
2022-12-26  GICRE       BUY ₹31.96 at ₹157.00 (fresh Friday signal — BUY: surged 4.73× weekly on 2022-12-02 (month 1.82×), ladder rising NOW — promoted from the ladder watch; stop ₹134.14; charges ₹0.0379)
2022-12-26  KABRAEXTRU  BUY ₹23.65 at ₹441.95 (fresh Friday signal — BUY: surged 4.67× weekly on 2022-11-25 (month 1.52×), ladder rising NOW — promoted from the ladder watch; stop ₹457.95; charges ₹0.0280)
2022-12-26  KRISHANA    BUY ₹31.72 at ₹83.60 (fresh Friday signal — BUY: 3.70× weekly, month 2.29×, ladder rising; stop ₹75.36; charges ₹0.0376)
2022-12-26  KSL         BUY ₹31.89 at ₹330.10 (fresh Friday signal — BUY: surged 5.50× weekly on 2022-12-09 (month 2.50×), ladder rising NOW — promoted from the ladder watch; stop ₹328.23; charges ₹0.0378)
2022-12-26  RVNL        SELL ₹29.02 at stop ₹60.57 (+29.3%, charges ₹0.0301) — the cash goes back to work at the next Friday screen
2023-01-02  MUKANDLTD   BUY ₹29.02 at ₹136.70 (fresh Friday signal — BUY: 6.81× weekly, month 2.54×, ladder rising; stop ₹103.76; charges ₹0.0344)
2023-01-27  KSL         SELL ₹31.63 at stop ₹328.23 (-0.6%, charges ₹0.0328) — the cash goes back to work at the next Friday screen
2023-01-30  LSIL        BUY ₹31.63 at ₹23.20 (fresh Friday signal — BUY: 2.28× weekly, month 3.56×, ladder rising; stop ₹11.29; charges ₹0.0375)
2023-02-01  GICRE       SELL ₹34.07 at stop ₹167.72 (+6.8%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2023-02-06  JINDALSAW   BUY ₹31.66 at ₹65.22 (fresh Friday signal — BUY: 2.72× weekly, month 3.57×, ladder rising; stop ₹51.25; charges ₹0.0375)
2023-02-07  LSIL        SELL ₹27.27 at stop ₹20.04 (-13.6%, charges ₹0.0283) — the cash goes back to work at the next Friday screen
2023-02-13  VSSL        BUY ₹29.68 at ₹345.70 (fresh Friday signal — ACCUMULATE: surged 2.11× weekly on 2023-01-20 (month 2.73×), ladder rising NOW — promoted from the ladder watch; stop ₹286.40; charges ₹0.0352)
2023-02-17  CGCL        SELL ₹29.18 at stop ₹704.95 (+17.6%, charges ₹0.0303) — the cash goes back to work at the next Friday screen
2023-02-20  TIIL        BUY ₹29.18 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0346)
2023-03-14  KABRAEXTRU  SELL ₹27.07 at stop ₹506.92 (+14.7%, charges ₹0.0281) — the cash goes back to work at the next Friday screen
2023-03-20  KRISHANA    SELL ₹35.74 at stop ₹94.40 (+12.9%, charges ₹0.0371) — the cash goes back to work at the next Friday screen
2023-03-20  SONATSOFTW  BUY ₹27.07 at ₹397.50 (fresh Friday signal — BUY: 2.89× weekly, month 5.95×, ladder rising; stop ₹357.20; charges ₹0.0321)
2023-03-27  DCAL        BUY ₹31.60 at ₹127.95 (fresh Friday signal — BUY: surged 6.76× weekly on 2023-02-24 (month 4.70×), ladder rising NOW — promoted from the ladder watch; stop ₹114.43; charges ₹0.0374)
2023-03-27  JINDALSAW   SELL ₹32.89 at stop ₹67.92 (+4.1%, charges ₹0.0341) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹53.00 at stop ₹112.36 (+116.1%, charges ₹0.0550) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹25.24 at stop ₹371.45 (-6.6%, charges ₹0.0262) — the cash goes back to work at the next Friday screen
2023-04-03  INGERRAND   BUY ₹30.21 at ₹2,690.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2023-03-10 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹2,170.84; charges ₹0.0358)
2023-04-03  KSB         BUY ₹30.14 at ₹426.00 (fresh Friday signal — ACCUMULATE: surged 4.48× weekly on 2023-03-10 (month 1.97×), ladder rising NOW — promoted from the ladder watch; stop ₹372.21; charges ₹0.0357)
2023-04-03  OLECTRA     BUY ₹30.02 at ₹623.50 (fresh Friday signal — ACCUMULATE: surged 5.11× weekly on 2023-03-10 (month 12.52×), ladder rising NOW — promoted from the ladder watch; stop ₹534.05; charges ₹0.0356)
2023-04-03  TAX         FY2023 settled: ₹17.9139 paid (STCG ₹61.14 @20%, LTCG ₹45.49 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-24  SHREECEM    SELL ₹31.07 at stop ₹23,636.00 (-3.9%, charges ₹0.0322) — the cash goes back to work at the next Friday screen
2023-05-02  GLS         BUY ₹30.24 at ₹509.05 (fresh Friday signal — BUY: 4.14× weekly, month 2.64×, ladder rising; stop ₹351.50; charges ₹0.0358)
2023-05-17  MUKANDLTD   SELL ₹24.62 at stop ₹116.23 (-15.0%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2023-05-22  SHARDAMOTR  BUY ₹30.27 at ₹380.00 (fresh Friday signal — BUY: 9.54× weekly, month 2.31×, ladder rising; stop ₹342.95; charges ₹0.0359)
2023-05-24  DCAL        SELL ₹28.44 at stop ₹115.42 (-9.8%, charges ₹0.0295) — the cash goes back to work at the next Friday screen
2023-05-26  VSSL        SELL ₹27.80 at stop ₹324.52 (-6.1%, charges ₹0.0288) — the cash goes back to work at the next Friday screen
2023-05-29  SCHNEIDER   BUY ₹28.02 at ₹236.80 (fresh Friday signal — BUY: 11.77× weekly, month 1.59×, ladder rising; stop ₹175.42; charges ₹0.0332)
2023-05-29  THANGAMAYL  BUY ₹30.39 at ₹1,344.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.50×, ladder rising; stop ₹1,116.30; charges ₹0.0360)
2023-07-12  KSB         SELL ₹28.78 at stop ₹407.74 (-4.3%, charges ₹0.0299) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹28.78 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0341)
2023-07-17  THANGAMAYL  SELL ₹30.33 at stop ₹1,344.25 (+0.0%, charges ₹0.0315) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹30.33 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.84×, ladder rising; stop ₹359.10; charges ₹0.0359)
2023-08-14  GANESHHOUC  SELL ₹27.72 at stop ₹418.62 (-8.4%, charges ₹0.0288) — the cash goes back to work at the next Friday screen
2023-08-21  ASTRAZEN    BUY ₹27.72 at ₹4,099.85 (fresh Friday signal — BUY: 6.03× weekly, month 2.40×, ladder rising; stop ₹3,562.50; charges ₹0.0328)
2023-09-13  INGERRAND   SELL ₹33.87 at stop ₹3,022.99 (+12.4%, charges ₹0.0351) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹33.87 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.67×, ladder rising; stop ₹58.28; charges ₹0.0401)
2023-10-19  OLECTRA     SELL ₹53.85 at stop ₹1,121.00 (+79.8%, charges ₹0.0559) — the cash goes back to work at the next Friday screen
2023-10-23  SCHNEIDER   SELL ₹37.24 at stop ₹315.45 (+33.2%, charges ₹0.0386) — the cash goes back to work at the next Friday screen
2023-10-23  SJVN        SELL ₹29.62 at stop ₹66.03 (-12.4%, charges ₹0.0307) — the cash goes back to work at the next Friday screen
2023-10-23  TIPSINDLTD  BUY ₹37.45 at ₹358.00 (fresh Friday signal — BUY: 4.52× weekly, month 1.76×, ladder rising; stop ₹270.23; charges ₹0.0444)
2023-10-25  SHARDAMOTR  SELL ₹36.96 at stop ₹465.07 (+22.4%, charges ₹0.0383) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹37.54 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0445)
2023-10-30  KKCL        BUY ₹37.60 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0445)
2023-10-30  SHAREINDIA  BUY ₹37.57 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0445)
2024-01-17  TIIL        SELL ₹60.93 at stop ₹2,337.00 (+109.3%, charges ₹0.0632) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹46.22 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0548)
2024-02-09  ASTRAZEN    SELL ₹39.11 at stop ₹5,795.95 (+41.4%, charges ₹0.0406) — the cash goes back to work at the next Friday screen
2024-02-12  IOB         BUY ₹48.74 at ₹71.50 (fresh Friday signal — BUY: 7.81× weekly, month 2.91×, ladder rising; stop ₹38.71; charges ₹0.0577)
2024-03-05  GLS         SELL ₹46.21 at stop ₹779.48 (+53.1%, charges ₹0.0479) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹44.63 at stop ₹357.20 (+19.1%, charges ₹0.0463) — the cash goes back to work at the next Friday screen
2024-03-11  DOLLAR      BUY ₹50.98 at ₹527.95 (fresh Friday signal — BUY: 4.55× weekly, month 2.48×, ladder rising; stop ₹461.65; charges ₹0.0604)
2024-03-11  SOLARINDS   BUY ₹50.88 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0603)
2024-03-13  DOLLAR      SELL ₹44.48 at stop ₹461.65 (-12.6%, charges ₹0.0461) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹33.20 at stop ₹674.12 (-11.5%, charges ₹0.0344) — the cash goes back to work at the next Friday screen
2024-03-13  TIPSINDLTD  SELL ₹47.33 at stop ₹453.39 (+26.6%, charges ₹0.0491) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹46.33 at stop ₹666.47 (+0.5%, charges ₹0.0481) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹48.52 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.0575)
2024-03-18  EMUDHRA     BUY ₹27.85 at ₹583.90 (fresh Friday signal — BUY: 1.54× weekly, month 3.10×, ladder rising; stop ₹529.77; charges ₹0.0330)
2024-03-18  FORCEMOT    BUY ₹48.30 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.0572)
2024-03-18  INDIGO      BUY ₹48.24 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0572)
2024-03-27  ANANDRATHI  SELL ₹93.24 at stop ₹862.65 (+224.7%, charges ₹0.0967) — the cash goes back to work at the next Friday screen
2024-04-01  SHRIRAMFIN  BUY ₹47.71 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0565)
2024-04-01  TAX         FY2024 settled: ₹31.1500 paid (STCG ₹155.75 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-13  JSWHL       SELL ₹42.10 at stop ₹6,280.45 (+33.6%, charges ₹0.0437) — the cash goes back to work at the next Friday screen
2024-05-21  KIRLOSBROS  BUY ₹50.09 at ₹1,844.00 (fresh Friday signal — BUY: 5.41× weekly, month 1.62×, ladder rising; stop ₹1,221.51; charges ₹0.0594)
2024-05-28  FORCEMOT    SELL ₹59.32 at stop ₹8,083.64 (+23.1%, charges ₹0.0615) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹50.14 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0594)
2024-06-04  BOSCHLTD    SELL ₹47.62 at stop ₹29,015.09 (-1.6%, charges ₹0.0494) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹44.35 at stop ₹441.77 (-6.8%, charges ₹0.0460) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹53.56 at stop ₹7,980.95 (+5.5%, charges ₹0.0556) — the cash goes back to work at the next Friday screen
2024-06-10  ARE&M       BUY ₹47.95 at ₹1,450.00 (fresh Friday signal — BUY: 3.00× weekly, month 2.35×, ladder rising; stop ₹916.60; charges ₹0.0568)
2024-06-10  FIEMIND     BUY ₹48.23 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0571)
2024-06-10  UNOMINDA    BUY ₹48.07 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0570)
2024-07-19  UNOMINDA    SELL ₹48.55 at stop ₹981.87 (+1.2%, charges ₹0.0504) — the cash goes back to work at the next Friday screen
2024-07-22  ARE&M       SELL ₹49.57 at stop ₹1,502.14 (+3.6%, charges ₹0.0514) — the cash goes back to work at the next Friday screen
2024-07-22  INDIAGLYCO  BUY ₹49.76 at ₹515.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.25×, ladder rising; stop ₹429.42; charges ₹0.0590)
2024-07-23  FIEMIND     SELL ₹45.84 at stop ₹1,257.56 (-4.7%, charges ₹0.0476) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹51.13 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0606)
2024-07-29  THYROCARE   BUY ₹51.17 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0606)
2024-08-05  KIRLOSBROS  SELL ₹53.87 at stop ₹1,987.46 (+7.8%, charges ₹0.0559) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹49.82 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0590)
2024-08-13  EMUDHRA     SELL ₹37.74 at stop ₹793.11 (+35.8%, charges ₹0.0391) — the cash goes back to work at the next Friday screen
2024-08-16  CAMPUS      SELL ₹48.46 at stop ₹277.07 (-3.1%, charges ₹0.0503) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹48.91 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0579)
2024-08-19  VGUARD      BUY ₹48.96 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.0580)
2024-09-09  AVANTIFEED  SELL ₹47.54 at stop ₹650.13 (-6.8%, charges ₹0.0493) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹48.67 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0577)
2024-10-03  IOB         SELL ₹38.48 at stop ₹56.57 (-20.9%, charges ₹0.0399) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹39.17 at stop ₹420.24 (-19.8%, charges ₹0.0406) — the cash goes back to work at the next Friday screen
2024-10-07  BSE         BUY ₹30.12 at ₹4,190.00 (fresh Friday signal — ACCUMULATE: 2.88× weekly, month 3.26×, ladder rising; stop ₹3,393.93; charges ₹0.0357)
2024-10-07  INDIGO      SELL ₹67.46 at stop ₹4,485.14 (+40.2%, charges ₹0.0700) — the cash goes back to work at the next Friday screen
2024-10-07  ITDCEM      BUY ₹47.52 at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹0.0563)
2024-10-07  THYROCARE   SELL ₹51.79 at stop ₹796.15 (+1.4%, charges ₹0.0537) — the cash goes back to work at the next Friday screen
2024-10-14  DBCORP      BUY ₹48.74 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0578)
2024-10-14  SKIPPER     BUY ₹48.56 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0575)
2024-10-22  BASF        SELL ₹51.48 at stop ₹7,611.30 (+3.6%, charges ₹0.0534) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹41.74 at stop ₹302.08 (-14.2%, charges ₹0.0433) — the cash goes back to work at the next Friday screen
2024-10-25  INDIAGLYCO  SELL ₹56.68 at stop ₹587.91 (+14.2%, charges ₹0.0588) — the cash goes back to work at the next Friday screen
2024-10-28  ASTRAZEN    BUY ₹39.64 at ₹7,142.20 (fresh Friday signal — ACCUMULATE: surged 13.24× weekly on 2024-09-27 (month 4.07×), ladder rising NOW — promoted from the ladder watch; stop ₹6,768.80; charges ₹0.0470)
2024-10-28  CARERATING  BUY ₹39.59 at ₹1,396.00 (fresh Friday signal — BUY: surged 3.30× weekly on 2024-10-11 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹1,066.23; charges ₹0.0469)
2024-10-28  CUPID       SELL ₹49.11 at stop ₹158.66 (+31.1%, charges ₹0.0509) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹39.73 at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.0471)
2024-10-28  PRAJIND     BUY ₹39.74 at ₹687.95 (fresh Friday signal — ACCUMULATE: surged 2.65× weekly on 2024-09-27 (month 1.53×), ladder rising NOW — promoted from the ladder watch; stop ₹675.21; charges ₹0.0471)
2024-11-04  AKZOINDIA   BUY ₹45.92 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.1084)
2024-11-13  PRAJIND     SELL ₹38.87 at stop ₹675.21 (-1.9%, charges ₹0.0863) — the cash goes back to work at the next Friday screen
2024-11-14  ASTRAZEN    SELL ₹37.92 at stop ₹6,854.77 (-4.0%, charges ₹0.0842) — the cash goes back to work at the next Friday screen
2024-11-18  JSWHL       BUY ₹44.21 at ₹19,990.00 (fresh Friday signal — BUY: 3.46× weekly, month 4.62×, ladder rising; stop ₹8,434.53; charges ₹0.1044)
2024-11-18  UNICHEMLAB  BUY ₹43.86 at ₹893.55 (fresh Friday signal — ACCUMULATE: surged 9.84× weekly on 2024-10-25 (month 3.48×), ladder rising NOW — promoted from the ladder watch; stop ₹711.49; charges ₹0.1035)
2024-12-17  SUPRIYA     SELL ₹66.21 at stop ₹717.25 (+35.8%, charges ₹0.1471) — the cash goes back to work at the next Friday screen
2024-12-20  UNICHEMLAB  SELL ₹34.76 at stop ₹711.49 (-20.4%, charges ₹0.0772) — the cash goes back to work at the next Friday screen
2024-12-23  EMSLIMITED  BUY ₹44.56 at ₹916.85 (fresh Friday signal — BUY: 5.57× weekly, month 2.01×, ladder rising; stop ₹802.65; charges ₹0.1052)
2024-12-23  KSL         BUY ₹44.56 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.1052)
2024-12-26  PRSMJOHNSN  SELL ₹38.56 at stop ₹170.55 (-20.5%, charges ₹0.0857) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹34.63 at stop ₹3,423.18 (-24.2%, charges ₹0.0769) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹43.72 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.1032)
2024-12-30  KFINTECH    BUY ₹43.57 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.1028)
2025-01-09  KSL         SELL ₹39.42 at stop ₹1,059.30 (-11.1%, charges ₹0.0875) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹47.29 at stop ₹893.05 (+19.4%, charges ₹0.1050) — the cash goes back to work at the next Friday screen
2025-01-10  EMSLIMITED  SELL ₹38.83 at stop ₹802.65 (-12.5%, charges ₹0.0863) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹41.76 at stop ₹477.28 (-13.7%, charges ₹0.0928) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹40.71 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0961)
2025-01-13  CARERATING  SELL ₹35.04 at stop ₹1,239.70 (-11.2%, charges ₹0.0778) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹40.61 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.0959)
2025-01-13  VARROC      BUY ₹40.40 at ₹590.00 (fresh Friday signal — ACCUMULATE: surged 1.67× weekly on 2025-01-03 (month 2.95×), ladder rising NOW — promoted from the ladder watch; stop ₹563.49; charges ₹0.0954)
2025-01-15  KFINTECH    SELL ₹33.26 at stop ₹1,159.14 (-23.3%, charges ₹0.0739) — the cash goes back to work at the next Friday screen
2025-01-20  DMART       BUY ₹40.68 at ₹3,624.00 (fresh Friday signal — ACCUMULATE: surged 3.63× weekly on 2025-01-03 (month 2.27×), ladder rising NOW — promoted from the ladder watch; stop ₹3,226.13; charges ₹0.0960)
2025-01-20  PTCIL       BUY ₹40.66 at ₹16,420.00 (fresh Friday signal — ACCUMULATE: surged 3.56× weekly on 2025-01-10 (month 2.38×), ladder rising NOW — promoted from the ladder watch; stop ₹15,417.55; charges ₹0.0960)
2025-01-21  PTCIL       SELL ₹38.01 at stop ₹15,417.55 (-6.1%, charges ₹0.0844) — the cash goes back to work at the next Friday screen
2025-01-22  VARROC      SELL ₹38.41 at stop ₹563.49 (-4.5%, charges ₹0.0853) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹34.01 at stop ₹700.36 (-16.1%, charges ₹0.0755) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹38.97 at ₹850.00 (fresh Friday signal — ACCUMULATE: surged 9.13× weekly on 2025-01-10 (month 6.49×), ladder rising NOW — promoted from the ladder watch; stop ₹825.52; charges ₹0.0920)
2025-01-28  LLOYDSME    SELL ₹35.29 at stop ₹1,258.75 (-12.7%, charges ₹0.0784) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹40.44 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.0955)
2025-02-12  JINDWORLD   SELL ₹39.94 at stop ₹374.11 (-8.2%, charges ₹0.0887) — the cash goes back to work at the next Friday screen
2025-02-24  GODFRYPHLP  BUY ₹37.92 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.0895)
2025-02-28  BSE         SELL ₹35.50 at stop ₹4,954.63 (+18.2%, charges ₹0.0788) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹36.95 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0872)
2025-03-03  ZENSARTECH  SELL ₹30.94 at stop ₹727.84 (-23.1%, charges ₹0.0687) — the cash goes back to work at the next Friday screen
2025-03-10  AARTIPHARM  BUY ₹38.36 at ₹744.90 (fresh Friday signal — ACCUMULATE: surged 1.58× weekly on 2025-02-21 (month 4.42×), ladder rising NOW — promoted from the ladder watch; stop ₹640.24; charges ₹0.0906)
2025-03-10  GRWRHITECH  BUY ₹38.48 at ₹4,219.95 (fresh Friday signal — BUY: surged 2.69× weekly on 2025-02-14 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹3,504.00; charges ₹0.0908)
2025-03-10  SUVENPHAR   BUY ₹38.52 at ₹1,166.00 (fresh Friday signal — ACCUMULATE: surged 4.03× weekly on 2025-02-21 (month 1.56×), ladder rising NOW — promoted from the ladder watch; stop ₹1,038.10; charges ₹0.0909)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹19.05 / LT ₹0.00)
2025-04-03  GRWRHITECH  SELL ₹32.70 at stop ₹3,602.82 (-14.6%, charges ₹0.0726) — the cash goes back to work at the next Friday screen
2025-04-07  AARTIPHARM  SELL ₹32.82 at stop ₹640.24 (-14.1%, charges ₹0.0729) — the cash goes back to work at the next Friday screen
2025-04-07  FINEORG     BUY ₹39.76 at ₹3,600.15 (fresh Friday signal — ACCUMULATE: surged 2.90× weekly on 2025-03-27 (month 1.61×), ladder rising NOW — promoted from the ladder watch; stop ₹3,791.55; charges ₹0.0939)
2025-04-07  SUVENPHAR   SELL ₹34.14 at stop ₹1,038.10 (-11.0%, charges ₹0.0758) — the cash goes back to work at the next Friday screen
2025-04-11  ITDCEM      SELL ₹37.95 at stop ₹524.92 (-19.9%, charges ₹0.0843) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹41.58 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.0981)
2025-04-15  INDIASHLTR  BUY ₹41.74 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.0985)
2025-04-15  TEJASNET    BUY ₹32.33 at ₹859.00 (fresh Friday signal — ACCUMULATE: surged 5.18× weekly on 2025-04-04 (month 4.12×), ladder rising NOW — promoted from the ladder watch; stop ₹679.16; charges ₹0.0763)
2025-05-09  TEJASNET    SELL ₹25.45 at stop ₹679.16 (-20.9%, charges ₹0.0565) — the cash goes back to work at the next Friday screen
2025-05-12  KPRMILL     BUY ₹25.45 at ₹1,302.00 (fresh Friday signal — BUY: 15.99× weekly, month 3.16×, ladder rising; stop ₹938.50; charges ₹0.0601)
2025-06-23  FINEORG     SELL ₹49.45 at stop ₹4,498.25 (+24.9%, charges ₹0.1098) — the cash goes back to work at the next Friday screen
2025-06-30  ALKYLAMINE  BUY ₹43.15 at ₹2,263.00 (fresh Friday signal — BUY: 7.48× weekly, month 1.62×, ladder rising; stop ₹1,832.27; charges ₹0.1019)
2025-08-01  KPRMILL     SELL ₹21.57 at stop ₹1,108.74 (-14.8%, charges ₹0.0479) — the cash goes back to work at the next Friday screen
2025-08-04  JSWHL       SELL ₹42.06 at stop ₹19,106.01 (-4.4%, charges ₹0.0934) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹46.04 at stop ₹1,814.78 (+25.2%, charges ₹0.1023) — the cash goes back to work at the next Friday screen
2025-08-04  PGHL        BUY ₹27.87 at ₹6,440.00 (fresh Friday signal — BUY: 6.30× weekly, month 2.58×, ladder rising; stop ₹5,320.00; charges ₹0.0658)
2025-08-07  ALKYLAMINE  SELL ₹39.62 at stop ₹2,087.62 (-7.7%, charges ₹0.0880) — the cash goes back to work at the next Friday screen
2025-08-11  PARADEEP    BUY ₹41.22 at ₹226.25 (fresh Friday signal — ACCUMULATE: surged 7.72× weekly on 2025-07-25 (month 1.69×), ladder rising NOW — promoted from the ladder watch; stop ₹193.88; charges ₹0.0973)
2025-08-11  RAIN        BUY ₹41.29 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.0975)
2025-08-11  SHOPERSTOP  BUY ₹41.24 at ₹512.60 (fresh Friday signal — ACCUMULATE: surged 7.37× weekly on 2025-07-18 (month 1.59×), ladder rising NOW — promoted from the ladder watch; stop ₹485.55; charges ₹0.0974)
2025-08-26  RAIN        SELL ₹36.84 at stop ₹143.64 (-10.4%, charges ₹0.0818) — the cash goes back to work at the next Friday screen
2025-09-01  RSYSTEMS    BUY ₹40.81 at ₹460.00 (fresh Friday signal — BUY: surged 17.81× weekly on 2025-08-22 (month 4.67×), ladder rising NOW — promoted from the ladder watch; stop ₹394.44; charges ₹0.0963)
2025-09-08  PARADEEP    SELL ₹35.16 at stop ₹193.88 (-14.3%, charges ₹0.0781) — the cash goes back to work at the next Friday screen
2025-09-15  MARUTI      BUY ₹35.16 at ₹15,350.00 (fresh Friday signal — BUY: 1.51× weekly, month 1.52×, ladder rising; stop ₹11,415.20; charges ₹0.0830)
2025-09-16  GODFRYPHLP  SELL ₹58.56 at stop ₹8,967.50 (+55.1%, charges ₹0.1301) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹41.05 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.75× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.0969)
2025-09-24  RSYSTEMS    SELL ₹37.37 at stop ₹423.23 (-8.0%, charges ₹0.0830) — the cash goes back to work at the next Friday screen
2025-09-25  INDIASHLTR  SELL ₹41.43 at stop ₹862.60 (-0.3%, charges ₹0.0920) — the cash goes back to work at the next Friday screen
2025-09-29  LGBBROSLTD  BUY ₹39.76 at ₹1,411.60 (fresh Friday signal — BUY: 3.53× weekly, month 1.72×, ladder rising; stop ₹1,258.75; charges ₹0.0939)
2025-09-29  SUBROS      BUY ₹39.56 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0934)
2025-10-03  DMART       SELL ₹49.22 at stop ₹4,404.96 (+21.5%, charges ₹0.1093) — the cash goes back to work at the next Friday screen
2025-10-06  ASTRAMICRO  BUY ₹39.85 at ₹1,119.85 (fresh Friday signal — BUY: 3.17× weekly, month 1.83×, ladder rising; stop ₹1,026.00; charges ₹0.0941)
2025-10-06  HEROMOTOCO  BUY ₹26.37 at ₹5,527.00 (fresh Friday signal — BUY: 3.12× weekly, month 1.55×, ladder rising; stop ₹5,004.60; charges ₹0.0622)
2025-10-14  SUBROS      SELL ₹36.42 at stop ₹1,046.90 (-7.5%, charges ₹0.0809) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹36.42 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0860)
2025-10-20  CREDITACC   SELL ₹58.16 at stop ₹1,274.42 (+49.9%, charges ₹0.1292) — the cash goes back to work at the next Friday screen
2025-10-27  VMART       BUY ₹39.13 at ₹858.00 (fresh Friday signal — ACCUMULATE: surged 13.79× weekly on 2025-10-03 (month 3.80×), ladder rising NOW — promoted from the ladder watch; stop ₹806.50; charges ₹0.0924)
2025-11-04  SHOPERSTOP  SELL ₹38.89 at stop ₹485.55 (-5.3%, charges ₹0.0864) — the cash goes back to work at the next Friday screen
2025-11-06  ASTRAMICRO  SELL ₹36.35 at stop ₹1,026.00 (-8.4%, charges ₹0.0807) — the cash goes back to work at the next Friday screen
2025-11-06  FDC         SELL ₹35.54 at stop ₹425.79 (-13.0%, charges ₹0.0789) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹25.58 at stop ₹5,938.45 (-7.8%, charges ₹0.0568) — the cash goes back to work at the next Friday screen
2025-11-07  VMART       SELL ₹36.61 at stop ₹806.50 (-6.0%, charges ₹0.0813) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹38.92 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.0919)
2025-11-10  CUB         BUY ₹39.12 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.0923)
2025-11-10  GRAVITA     BUY ₹35.74 at ₹1,711.00 (fresh Friday signal — BUY: 2.50× weekly, month 1.58×, ladder rising; stop ₹1,544.13; charges ₹0.0844)
2025-11-10  LTF         BUY ₹39.12 at ₹304.00 (fresh Friday signal — BUY: 2.98× weekly, month 1.53×, ladder rising; stop ₹250.80; charges ₹0.0923)
2025-11-10  TDPOWERSYS  BUY ₹39.10 at ₹389.50 (fresh Friday signal — BUY: 3.09× weekly, month 2.39×, ladder rising; stop ₹276.78; charges ₹0.0923)
2025-11-20  ANANDRATHI  SELL ₹33.39 at stop ₹1,450.17 (-7.9%, charges ₹0.0742) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹37.27 at stop ₹976.41 (-3.8%, charges ₹0.0828) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹33.39 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0788)
2025-11-24  TDPOWERSYS  SELL ₹35.72 at stop ₹357.49 (-8.2%, charges ₹0.0793) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹39.87 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.33×, ladder rising; stop ₹535.37; charges ₹0.0941)
2025-12-01  SANSERA     BUY ₹33.12 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.0782)
2026-01-08  EUREKAFORB  SELL ₹35.21 at stop ₹589.10 (-11.3%, charges ₹0.0782) — the cash goes back to work at the next Friday screen
2026-01-09  GRAVITA     SELL ₹34.91 at stop ₹1,678.56 (-1.9%, charges ₹0.0775) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹29.87 at stop ₹2,956.49 (-10.1%, charges ₹0.0663) — the cash goes back to work at the next Friday screen
2026-01-12  HINDCOPPER  BUY ₹38.53 at ₹532.00 (fresh Friday signal — BUY: surged 1.55× weekly on 2025-12-12 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹456.95; charges ₹0.0910)
2026-01-12  NATIONALUM  BUY ₹38.56 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.0910)
2026-01-19  JBMA        BUY ₹22.90 at ₹592.05 (fresh Friday signal — ACCUMULATE: surged 4.93× weekly on 2026-01-02 (month 2.87×), ladder rising NOW — promoted from the ladder watch; stop ₹556.03; charges ₹0.0541)
2026-01-20  JBMA        SELL ₹21.41 at stop ₹556.03 (-6.1%, charges ₹0.0476) — the cash goes back to work at the next Friday screen
2026-01-20  LGBBROSLTD  SELL ₹48.06 at stop ₹1,713.80 (+21.4%, charges ₹0.1067) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹37.87 at stop ₹748.60 (-8.5%, charges ₹0.0841) — the cash goes back to work at the next Friday screen
2026-01-21  LTF         SELL ₹36.09 at stop ₹281.77 (-7.3%, charges ₹0.0802) — the cash goes back to work at the next Friday screen
2026-01-23  MARUTI      SELL ₹35.71 at stop ₹15,657.90 (+2.0%, charges ₹0.0793) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹31.52 at stop ₹1,672.76 (-4.4%, charges ₹0.0700) — the cash goes back to work at the next Friday screen
2026-01-27  RBA         BUY ₹37.49 at ₹64.07 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.51×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.0885)
2026-02-02  CEIGALL     BUY ₹37.76 at ₹274.95 (fresh Friday signal — ACCUMULATE: surged 4.16× weekly on 2026-01-02 (month 1.71×), ladder rising NOW — promoted from the ladder watch; stop ₹253.32; charges ₹0.0891)
2026-02-02  MAHABANK    BUY ₹37.67 at ₹60.48 (fresh Friday signal — ACCUMULATE: surged 1.87× weekly on 2026-01-16 (month 1.60×), ladder rising NOW — promoted from the ladder watch; stop ₹59.76; charges ₹0.0889)
2026-02-02  TATAELXSI   BUY ₹37.69 at ₹5,448.00 (fresh Friday signal — ACCUMULATE: surged 3.74× weekly on 2026-01-09 (month 1.70×), ladder rising NOW — promoted from the ladder watch; stop ₹5,016.48; charges ₹0.0890)
2026-02-12  TATAELXSI   SELL ₹34.55 at stop ₹5,016.48 (-7.9%, charges ₹0.0767) — the cash goes back to work at the next Friday screen
2026-02-17  NATIONALUM  SELL ₹36.58 at stop ₹335.49 (-4.7%, charges ₹0.0813) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹36.95 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.67×, ladder rising; stop ₹5,440.18; charges ₹0.0872)
2026-02-23  E2E         BUY ₹37.40 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0883)
2026-02-23  HAPPYFORGE  BUY ₹19.32 at ₹1,370.00 (fresh Friday signal — BUY: surged 6.09× weekly on 2026-02-13 (month 1.85×), ladder rising NOW — promoted from the ladder watch; stop ₹1,188.64; charges ₹0.0456)
2026-02-23  VESUVIUS    BUY ₹37.51 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.0885)
2026-03-04  CEIGALL     SELL ₹36.41 at stop ₹266.33 (-3.1%, charges ₹0.0809) — the cash goes back to work at the next Friday screen
2026-03-04  HAPPYFORGE  SELL ₹17.33 at stop ₹1,234.05 (-9.9%, charges ₹0.0385) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹38.51 at stop ₹251.43 (-1.1%, charges ₹0.0855) — the cash goes back to work at the next Friday screen
2026-03-09  SANSERA     BUY ₹35.00 at ₹2,125.10 (fresh Friday signal — ACCUMULATE: surged 4.58× weekly on 2026-02-13 (month 2.89×), ladder rising NOW — promoted from the ladder watch; stop ₹2,033.00; charges ₹0.0826)
2026-03-09  VTL         BUY ₹18.73 at ₹532.95 (fresh Friday signal — ACCUMULATE: surged 1.53× weekly on 2026-02-27 (month 2.21×), ladder rising NOW — promoted from the ladder watch; stop ₹485.45; charges ₹0.0442)
2026-03-12  HINDCOPPER  SELL ₹38.11 at stop ₹528.63 (-0.6%, charges ₹0.0846) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹35.58 at stop ₹61.08 (-4.7%, charges ₹0.0790) — the cash goes back to work at the next Friday screen
2026-03-13  HEROMOTOCO  SELL ₹24.87 at stop ₹5,237.35 (-5.2%, charges ₹0.0552) — the cash goes back to work at the next Friday screen
2026-03-13  SANSERA     SELL ₹33.33 at stop ₹2,033.00 (-4.3%, charges ₹0.0740) — the cash goes back to work at the next Friday screen
2026-03-16  J&KBANK     BUY ₹34.51 at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.95×, ladder rising; stop ₹103.27; charges ₹0.0815)
2026-03-16  JBCHEPHARM  BUY ₹34.57 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0816)
2026-03-23  ABSLAMC     BUY ₹33.76 at ₹937.90 (fresh Friday signal — ACCUMULATE: surged 4.88× weekly on 2026-03-13 (month 2.34×), ladder rising NOW — promoted from the ladder watch; stop ₹876.18; charges ₹0.0797)
2026-03-23  BHARATFORG  BUY ₹33.58 at ₹1,700.00 (fresh Friday signal — ACCUMULATE: surged 1.59× weekly on 2026-02-27 (month 1.77×), ladder rising NOW — promoted from the ladder watch; stop ₹1,564.35; charges ₹0.0793)
2026-03-23  J&KBANK     SELL ₹31.38 at stop ₹110.67 (-8.6%, charges ₹0.0697) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹32.40 at stop ₹464.31 (-13.2%, charges ₹0.0720) — the cash goes back to work at the next Friday screen
2026-03-30  ABSLAMC     SELL ₹31.40 at stop ₹876.18 (-6.6%, charges ₹0.0697) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹33.33 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0787)
2026-03-30  MAHABANK    SELL ₹37.86 at stop ₹61.05 (+0.9%, charges ₹0.0841) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹62.21 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹33.15 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0783)
2026-04-13  INOXINDIA   BUY ₹33.99 at ₹1,299.10 (fresh Friday signal — BUY: 4.08× weekly, month 2.14×, ladder rising; stop ₹1,091.46; charges ₹0.0802)
2026-04-13  THERMAX     BUY ₹34.28 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.0809)
2026-04-20  GALLANTT    BUY ₹32.26 at ₹862.10 (fresh Friday signal — BUY: surged 135.50× weekly on 2026-04-10 (month 10.32×), ladder rising NOW — promoted from the ladder watch; stop ₹612.75; charges ₹0.0761)
2026-05-13  INOXINDIA   SELL ₹35.74 at stop ₹1,372.18 (+5.6%, charges ₹0.0794) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹32.47 at stop ₹1,125.84 (-2.1%, charges ₹0.0721) — the cash goes back to work at the next Friday screen
2026-05-14  GALLANTT    SELL ₹29.19 at stop ₹783.75 (-9.1%, charges ₹0.0648) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹34.87 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.0823)
2026-05-18  CAPLIPOINT  BUY ₹34.87 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.0823)
2026-05-18  NLCINDIA    BUY ₹27.66 at ₹351.55 (fresh Friday signal — BUY: 5.83× weekly, month 6.05×, ladder rising; stop ₹278.49; charges ₹0.0653)
2026-06-05  E2E         SELL ₹29.78 at stop ₹2,330.72 (-20.0%, charges ₹0.0661) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹29.78 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0703)
2026-06-09  NLCINDIA    SELL ₹25.11 at stop ₹320.62 (-8.8%, charges ₹0.0558) — the cash goes back to work at the next Friday screen
2026-06-15  POWERMECH   BUY ₹25.11 at ₹2,859.90 (fresh Friday signal — BUY: 1.56× weekly, month 1.66×, ladder rising; stop ₹2,217.30; charges ₹0.0593)
2026-07-07  POWERMECH   SELL ₹22.75 at stop ₹2,603.29 (-9.0%, charges ₹0.0505) — the cash goes back to work at the next Friday screen
2026-07-13  GANESHHOU   BUY ₹22.75 at ₹860.50 (fresh Friday signal — BUY: 9.80× weekly, month 2.00×, ladder rising; stop ₹712.60; charges ₹0.0537)
2026-07-29  THERMAX     SELL ₹40.87 at stop ₹4,306.64 (+19.8%, charges ₹0.0908) — the cash goes back to work at the next Friday screen
2026-07-31  VTL         SELL ₹20.74 at stop ₹592.80 (+11.2%, charges ₹0.0461) — the cash goes back to work at the next Friday screen
2026-08-03  BLUESTONE   BUY ₹22.94 at ₹823.40 (fresh Friday signal — ACCUMULATE: 5.63× weekly, month 9.43×, ladder rising; stop ₹664.75; charges ₹0.0541)
2026-08-03  TMB         BUY ₹38.67 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.0913)
2026-09-04  BHARATFORG  SELL ₹38.41 at stop ₹1,953.29 (+14.9%, charges ₹0.0853) — the cash goes back to work at the next Friday screen
2026-09-07  SBICARD     BUY ₹38.41 at ₹653.10 (fresh Friday signal — ACCUMULATE: 4.90× weekly, month 2.54×, ladder rising; stop ₹579.50; charges ₹0.0907)
2026-09-10  ALKYLAMINE  SELL ₹39.00 at stop ₹1,920.99 (+12.3%, charges ₹0.0866) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹43.23 at stop ₹7,158.25 (+17.5%, charges ₹0.0960) — the cash goes back to work at the next Friday screen
2026-09-15  SUNDRMFAST  BUY ₹38.98 at ₹1,277.30 (fresh Friday signal — BUY: 3.14× weekly, month 1.81×, ladder rising; stop ₹1,127.74; charges ₹0.0920)
2026-09-21  AVALON      BUY ₹38.87 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.0917)
```
