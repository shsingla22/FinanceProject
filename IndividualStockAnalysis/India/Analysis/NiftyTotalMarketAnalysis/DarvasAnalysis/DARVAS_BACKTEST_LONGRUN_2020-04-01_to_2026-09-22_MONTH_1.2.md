# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 1388 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹418.92** | **+24.78% a year** |
| The same system before costs and taxes | ₹575.15 | +31.05% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹288.59 | +17.80% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹418.92** (+24.78% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 436 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹21.22** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹69.47**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹34.16 | ₹0.00 | ₹6.8328 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹33.79 | ₹21.46 | ₹9.4406 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹70.96 | ₹67.11 | ₹22.5800 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹153.07 | ₹0.00 | ₹30.6147 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹49.74 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹45.26 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹11.69 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 133.69 | +33.7% | +34.3% | +70.1% |
| 2021 (2021-12-31) | 232.04 | +73.6% | +82.7% | +26.2% |
| 2022 (2022-12-30) | 329.29 | +41.9% | +43.9% | +4.3% |
| 2023 (2023-12-29) | 436.51 | +32.6% | +55.3% | +20.0% |
| 2024 (2024-12-27) | 438.91 | +0.5% | +6.3% | +9.6% |
| 2025 (2025-12-26) | 413.50 | -5.8% | -3.9% | +9.4% |
| 2026 (2026-09-22) | 418.92 | +1.3% | +2.7% | -10.4% |

## What it took to earn it

- **Maximum drawdown: -31.0%** (peak 2024-03-07 → trough 2026-04-02, on weekly closes).
- **205 closed trades**: 91 winners (44%), average winner +34.7%, average loser -10.4%.
- Best closed trade ANANDRATHI +224.7%; worst KIOCL -24.5%.
- Median holding period 66 days.
- Cash share of equity averaged 9% across all weeks (median 3%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.20 | 59.96 | 4 |
| 2020-05-29 | 104.86 | 0.00 | 10 |
| 2020-06-26 | 120.17 | 0.00 | 10 |
| 2020-07-31 | 127.31 | 0.00 | 10 |
| 2020-08-28 | 126.52 | 0.00 | 10 |
| 2020-09-25 | 128.10 | 26.83 | 7 |
| 2020-10-30 | 120.01 | 0.38 | 9 |
| 2020-11-27 | 121.06 | 0.00 | 10 |
| 2020-12-24 | 133.69 | 29.99 | 8 |
| 2021-01-29 | 144.48 | 23.70 | 8 |
| 2021-02-26 | 155.94 | 10.07 | 9 |
| 2021-03-26 | 148.96 | 41.14 | 7 |
| 2021-04-30 | 151.90 | 0.00 | 10 |
| 2021-05-28 | 170.20 | 0.00 | 10 |
| 2021-06-25 | 185.19 | 0.00 | 10 |
| 2021-07-30 | 219.80 | 0.00 | 10 |
| 2021-08-27 | 210.89 | 0.00 | 10 |
| 2021-09-24 | 228.26 | 14.35 | 9 |
| 2021-10-29 | 228.66 | 32.48 | 8 |
| 2021-11-26 | 235.44 | 65.50 | 6 |
| 2021-12-31 | 232.04 | 11.37 | 8 |
| 2022-01-28 | 240.53 | 24.80 | 8 |
| 2022-02-25 | 227.56 | 88.16 | 5 |
| 2022-03-25 | 253.08 | 19.85 | 8 |
| 2022-04-29 | 275.84 | 29.90 | 7 |
| 2022-05-27 | 278.73 | 9.42 | 8 |
| 2022-06-24 | 264.39 | 31.44 | 7 |
| 2022-07-29 | 293.99 | 5.00 | 8 |
| 2022-08-26 | 308.77 | 5.00 | 8 |
| 2022-09-30 | 290.87 | 33.83 | 7 |
| 2022-10-28 | 305.75 | 1.26 | 8 |
| 2022-11-25 | 340.47 | 5.95 | 8 |
| 2022-12-30 | 329.29 | 48.14 | 8 |
| 2023-01-27 | 317.86 | 47.05 | 8 |
| 2023-02-24 | 319.56 | 3.99 | 9 |
| 2023-03-31 | 307.84 | 150.44 | 5 |
| 2023-04-28 | 305.54 | 41.22 | 8 |
| 2023-05-26 | 312.10 | 37.17 | 8 |
| 2023-06-30 | 318.49 | 6.07 | 9 |
| 2023-07-28 | 331.31 | 5.16 | 9 |
| 2023-08-25 | 365.51 | 0.00 | 9 |
| 2023-09-29 | 382.83 | 0.00 | 9 |
| 2023-10-27 | 380.86 | 104.12 | 6 |
| 2023-11-24 | 420.39 | 4.92 | 9 |
| 2023-12-29 | 436.51 | 0.00 | 9 |
| 2024-01-25 | 459.54 | 22.53 | 9 |
| 2024-02-23 | 493.03 | 16.45 | 9 |
| 2024-03-28 | 476.73 | 100.98 | 8 |
| 2024-04-26 | 475.41 | 0.00 | 10 |
| 2024-05-31 | 467.96 | 81.21 | 8 |
| 2024-06-28 | 470.04 | 0.00 | 10 |
| 2024-07-26 | 473.97 | 103.75 | 8 |
| 2024-08-30 | 447.02 | 0.00 | 10 |
| 2024-09-27 | 438.81 | 0.00 | 10 |
| 2024-10-25 | 405.21 | 122.42 | 8 |
| 2024-11-29 | 457.12 | 0.00 | 11 |
| 2024-12-27 | 438.91 | 82.62 | 9 |
| 2025-01-31 | 412.35 | 99.21 | 7 |
| 2025-02-28 | 371.21 | 137.86 | 6 |
| 2025-03-27 | 415.00 | 12.34 | 9 |
| 2025-04-25 | 435.67 | 10.17 | 8 |
| 2025-05-30 | 438.34 | 56.59 | 7 |
| 2025-06-27 | 449.96 | 61.83 | 7 |
| 2025-07-25 | 437.86 | 17.51 | 8 |
| 2025-08-29 | 436.83 | 45.01 | 8 |
| 2025-09-26 | 403.39 | 101.08 | 7 |
| 2025-10-31 | 401.97 | 67.45 | 9 |
| 2025-11-28 | 410.07 | 64.39 | 8 |
| 2025-12-26 | 413.50 | 0.00 | 10 |
| 2026-01-30 | 397.89 | 228.66 | 4 |
| 2026-02-27 | 382.45 | 0.00 | 10 |
| 2026-03-27 | 350.24 | 103.09 | 7 |
| 2026-04-30 | 390.44 | 0.00 | 10 |
| 2026-05-29 | 411.39 | 0.00 | 10 |
| 2026-06-25 | 405.01 | 0.00 | 10 |
| 2026-07-31 | 399.19 | 89.07 | 8 |
| 2026-08-28 | 422.34 | 7.49 | 10 |
| 2026-09-22 | 418.92 | 8.03 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| BLUESTONE | 2026-08-03 | 823.40 | 930.40 | 758.29 | +13.0% |
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,777.30 | 2,376.52 | +39.6% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,392.00 | 1,242.60 | +40.7% |
| GANESHHOU | 2026-07-13 | 860.50 | 736.80 | 712.60 | -14.4% |
| GARFIBRES | 2026-06-22 | 796.00 | 800.45 | 701.74 | +0.6% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| RUBICON | 2026-06-08 | 1,190.00 | 1,671.20 | 1,653.47 | +40.4% |
| SUNDRMFAST | 2026-09-15 | 1,277.30 | 1,190.90 | 1,127.74 | -6.8% |
| TMB | 2026-08-03 | 864.90 | 883.75 | 817.00 | +2.2% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| HATHWAY | 2020-06-22 | 34.80 | 2020-06-29 | 31.40 | -9.8% |
| EIDPARRY | 2020-05-11 | 164.00 | 2020-08-17 | 273.03 | +66.5% |
| PANACEABIO | 2020-06-15 | 230.00 | 2020-08-20 | 184.01 | -20.0% |
| APCOTEXIND | 2020-08-24 | 164.95 | 2020-08-31 | 151.95 | -7.9% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| BALAJITELE | 2020-05-04 | 61.40 | 2020-09-09 | 74.07 | +20.6% |
| NBIFIN | 2020-07-06 | 1,610.00 | 2020-09-17 | 1,362.07 | -15.4% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| KIOCL | 2020-08-24 | 152.50 | 2020-09-22 | 115.10 | -24.5% |
| SATIA | 2020-09-14 | 122.00 | 2020-09-22 | 102.97 | -15.6% |
| PRINCEPIPE | 2020-09-07 | 208.00 | 2020-10-12 | 220.88 | +6.2% |
| ALEMBICLTD | 2020-05-18 | 54.90 | 2020-11-02 | 91.41 | +66.5% |
| KPITTECH | 2020-09-28 | 113.60 | 2020-11-02 | 93.15 | -18.0% |
| ADVENZYMES | 2020-05-18 | 159.95 | 2020-11-03 | 292.33 | +82.8% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| TCI | 2020-09-14 | 242.00 | 2020-12-22 | 234.75 | -3.0% |
| SAKSOFT | 2020-09-21 | 391.45 | 2021-01-25 | 341.10 | -12.9% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| MTNL | 2020-12-28 | 14.10 | 2021-02-16 | 12.06 | -14.5% |
| DABUR | 2020-11-09 | 530.00 | 2021-02-22 | 503.12 | -5.1% |
| JINDWORLD | 2020-11-09 | 50.00 | 2021-03-01 | 52.12 | +4.2% |
| RCF | 2021-03-01 | 80.00 | 2021-03-17 | 79.16 | -1.1% |
| RAMCOIND | 2020-11-09 | 199.00 | 2021-03-19 | 236.22 | +18.7% |
| APTECHT | 2021-02-01 | 178.45 | 2021-03-19 | 204.25 | +14.5% |
| MAHINDCIE | 2021-02-22 | 188.00 | 2021-03-19 | 158.46 | -15.7% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| GREENPANEL | 2020-11-09 | 86.40 | 2021-03-25 | 153.89 | +78.1% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| CENTRUM | 2021-03-30 | 28.40 | 2021-04-12 | 24.89 | -12.4% |
| GFLLIMITED | 2021-03-22 | 93.00 | 2021-04-13 | 74.39 | -20.0% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| GDL | 2021-02-01 | 159.15 | 2021-09-20 | 266.00 | +67.1% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| NEOGEN | 2021-09-27 | 1,255.00 | 2021-10-25 | 1,142.85 | -8.9% |
| EMAMIPAP | 2021-04-19 | 125.00 | 2021-11-22 | 141.55 | +13.2% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-10-25 | 9,508.95 | 2021-11-26 | 10,070.05 | +5.9% |
| SHANKARA | 2021-03-30 | 413.00 | 2021-11-29 | 489.25 | +18.5% |
| SOMANYCERA | 2021-06-21 | 594.85 | 2021-11-29 | 755.11 | +26.9% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| LTTS | 2020-10-19 | 1,745.00 | 2022-01-21 | 4,856.88 | +178.3% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| SHARDACROP | 2022-01-24 | 420.00 | 2022-02-11 | 545.30 | +29.8% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| TV18BRDCST | 2022-01-31 | 58.90 | 2022-02-22 | 58.38 | -0.9% |
| LAXMIMACH | 2022-02-21 | 10,118.80 | 2022-02-22 | 10,169.75 | +0.5% |
| JSWISPL | 2022-01-24 | 37.50 | 2022-02-24 | 30.25 | -19.3% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| ADANITRANS | 2021-03-30 | 896.00 | 2022-05-11 | 2,299.37 | +156.6% |
| MFL | 2022-05-02 | 1,430.00 | 2022-05-11 | 1,225.50 | -14.3% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| KRISHANA | 2022-05-16 | 67.96 | 2022-06-16 | 54.77 | -19.4% |
| JSWENERGY | 2021-03-08 | 81.85 | 2022-06-20 | 201.99 | +146.8% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| RAJMET | 2022-03-07 | 278.00 | 2022-09-15 | 359.30 | +29.2% |
| INSECTICID | 2022-06-27 | 844.00 | 2022-09-29 | 926.73 | +9.8% |
| SUNDARMHLD | 2022-10-03 | 103.50 | 2022-10-11 | 92.20 | -10.9% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| RVNL | 2022-10-17 | 36.85 | 2022-12-26 | 60.57 | +64.4% |
| KSL | 2022-12-26 | 330.10 | 2023-01-27 | 328.23 | -0.6% |
| JINDWORLD | 2022-12-26 | 415.10 | 2023-02-01 | 389.50 | -6.2% |
| GICRE | 2022-12-26 | 157.00 | 2023-02-01 | 167.72 | +6.8% |
| LSIL | 2023-01-30 | 23.20 | 2023-02-07 | 20.04 | -13.6% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| CHOLAFIN | 2023-02-06 | 777.55 | 2023-03-24 | 727.37 | -6.5% |
| JINDALSAW | 2023-02-06 | 65.22 | 2023-03-27 | 67.92 | +4.1% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| CIGNITITEC | 2023-02-13 | 673.00 | 2023-03-29 | 705.14 | +4.8% |
| SONATSOFTW | 2023-03-27 | 413.70 | 2023-03-29 | 371.45 | -10.2% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| MUKANDLTD | 2023-01-02 | 136.70 | 2023-05-17 | 116.23 | -15.0% |
| GUJALKALI | 2023-05-02 | 688.15 | 2023-05-23 | 646.14 | -6.1% |
| ANURAS | 2023-04-03 | 868.95 | 2023-07-03 | 1,007.67 | +16.0% |
| KSB | 2023-03-27 | 417.98 | 2023-07-12 | 407.74 | -2.4% |
| THANGAMAYL | 2023-05-29 | 1,344.00 | 2023-07-17 | 1,344.25 | +0.0% |
| GANESHHOUC | 2023-07-24 | 457.00 | 2023-08-14 | 418.62 | -8.4% |
| INGERRAND | 2023-04-03 | 2,690.00 | 2023-09-13 | 3,022.99 | +12.4% |
| SJVN | 2023-09-18 | 75.35 | 2023-10-23 | 66.03 | -12.4% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| SHARDAMOTR | 2023-05-22 | 380.00 | 2023-10-25 | 465.07 | +22.4% |
| NATCOPHARM | 2023-04-03 | 569.80 | 2023-11-01 | 771.40 | +35.4% |
| GENUSPOWER | 2023-07-10 | 162.85 | 2023-11-16 | 234.03 | +43.7% |
| SUNDARMHLD | 2023-11-06 | 144.75 | 2023-12-20 | 145.40 | +0.4% |
| ISMTLTD | 2023-11-20 | 94.60 | 2023-12-20 | 88.35 | -6.6% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| MMFL | 2023-12-26 | 1,023.60 | 2024-01-30 | 912.05 | -10.9% |
| ASTRAZEN | 2023-08-21 | 4,099.85 | 2024-02-09 | 5,795.95 | +41.4% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| TCI | 2024-02-05 | 987.60 | 2024-03-11 | 790.40 | -20.0% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| OIL | 2023-12-26 | 251.27 | 2024-03-15 | 344.53 | +37.1% |
| ANANDRATHI | 2023-07-17 | 265.70 | 2024-03-27 | 862.65 | +224.7% |
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| DMART | 2024-04-01 | 4,570.00 | 2024-05-31 | 4,322.83 | -5.4% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| BOSCHLTD | 2024-03-18 | 29,500.05 | 2024-06-04 | 29,015.09 | -1.6% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| TRENT | 2024-03-18 | 2,709.27 | 2024-07-22 | 3,464.36 | +27.9% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| KIRLOSBROS | 2024-05-21 | 1,844.00 | 2024-08-05 | 1,987.46 | +7.8% |
| THERMAX | 2024-06-03 | 5,640.00 | 2024-08-05 | 4,719.70 | -16.3% |
| ADANIPOWER | 2024-06-10 | 783.00 | 2024-08-12 | 632.75 | -19.2% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| AVANTIFEED | 2024-07-29 | 697.65 | 2024-09-09 | 650.13 | -6.8% |
| CERA | 2024-08-12 | 10,499.95 | 2024-09-19 | 8,198.93 | -21.9% |
| IOB | 2024-02-12 | 71.50 | 2024-10-03 | 56.57 | -20.9% |
| VGUARD | 2024-08-19 | 524.15 | 2024-10-04 | 420.24 | -19.8% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| HBLPOWER | 2024-07-22 | 585.00 | 2024-10-25 | 522.78 | -10.6% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| CIGNITITEC | 2024-10-28 | 1,515.00 | 2024-11-18 | 1,330.00 | -12.2% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| PRSMJOHNSN | 2024-09-16 | 214.51 | 2024-12-26 | 170.55 | -20.5% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| GARFIBRES | 2024-11-25 | 956.00 | 2025-01-09 | 829.35 | -13.2% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| GANECOS | 2024-10-14 | 2,103.85 | 2025-01-10 | 1,751.78 | -16.7% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| COFORGE | 2024-10-28 | 1,543.10 | 2025-01-13 | 1,801.20 | +16.7% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| PGIL | 2025-01-20 | 833.02 | 2025-01-21 | 705.52 | -15.3% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| ASHOKA | 2025-01-13 | 271.65 | 2025-01-24 | 262.67 | -3.3% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| BSE | 2024-09-23 | 4,001.00 | 2025-02-28 | 4,954.63 | +23.8% |
| GANESHHOUC | 2024-11-18 | 1,059.00 | 2025-02-28 | 1,090.38 | +3.0% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| GRWRHITECH | 2025-03-10 | 4,219.95 | 2025-04-03 | 3,602.82 | -14.6% |
| AVANTIFEED | 2025-03-10 | 806.00 | 2025-04-07 | 648.95 | -19.5% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| ITDCEM | 2024-10-07 | 655.05 | 2025-04-11 | 524.92 | -19.9% |
| HCG | 2025-01-20 | 504.95 | 2025-05-26 | 559.08 | +10.7% |
| COROMANDEL | 2025-04-07 | 1,870.00 | 2025-06-27 | 2,246.75 | +20.1% |
| JSWHL | 2024-10-28 | 9,600.00 | 2025-08-04 | 19,106.01 | +99.0% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| LICI | 2025-06-02 | 477.00 | 2025-08-07 | 438.21 | -8.1% |
| ALKYLAMINE | 2025-06-30 | 2,263.00 | 2025-08-07 | 2,087.62 | -7.7% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| RSYSTEMS | 2025-09-01 | 460.00 | 2025-09-24 | 423.23 | -8.0% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| DELHIVERY | 2025-08-11 | 464.65 | 2025-10-01 | 436.10 | -6.1% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| BLACKBUCK | 2025-08-18 | 553.00 | 2025-10-28 | 642.20 | +16.1% |
| PGHL | 2025-08-11 | 6,345.00 | 2025-11-06 | 5,938.45 | -6.4% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| NETWEB | 2025-09-29 | 3,700.00 | 2025-11-06 | 3,515.95 | -5.0% |
| ASTRAMICRO | 2025-10-06 | 1,119.85 | 2025-11-06 | 1,026.00 | -8.4% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| TDPOWERSYS | 2025-11-03 | 382.27 | 2025-11-24 | 357.49 | -6.5% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| PSB | 2025-10-27 | 30.80 | 2025-12-03 | 29.05 | -5.7% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| KIRLOSENG | 2025-12-08 | 1,130.00 | 2026-01-12 | 1,140.95 | +1.0% |
| UPL | 2025-08-11 | 688.95 | 2026-01-20 | 729.12 | +5.8% |
| LGBBROSLTD | 2025-09-29 | 1,411.60 | 2026-01-20 | 1,713.80 | +21.4% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| LTF | 2025-11-10 | 304.00 | 2026-01-21 | 281.77 | -7.3% |
| RRKABEL | 2025-11-03 | 1,475.40 | 2026-01-23 | 1,358.31 | -7.9% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| CEIGALL | 2026-02-09 | 297.00 | 2026-03-04 | 266.33 | -10.3% |
| PTC | 2026-02-09 | 180.62 | 2026-03-04 | 156.89 | -13.1% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| TATASTEEL | 2026-02-16 | 201.00 | 2026-03-09 | 190.52 | -5.2% |
| HINDCOPPER | 2026-01-12 | 532.00 | 2026-03-12 | 528.63 | -0.6% |
| RBA | 2026-01-19 | 67.50 | 2026-03-12 | 61.08 | -9.5% |
| HINDALCO | 2026-02-02 | 905.70 | 2026-03-23 | 862.65 | -4.8% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-16 | 121.14 | 2026-03-23 | 110.67 | -8.6% |
| TORNTPOWER | 2026-03-09 | 1,451.00 | 2026-03-30 | 1,315.84 | -9.3% |
| SUNPHARMA | 2026-03-09 | 1,772.90 | 2026-04-02 | 1,651.01 | -6.9% |
| INOXINDIA | 2026-03-30 | 1,185.00 | 2026-05-13 | 1,372.18 | +15.8% |
| AETHER | 2026-03-23 | 1,149.80 | 2026-05-14 | 1,125.84 | -2.1% |
| E2E | 2026-02-16 | 2,464.00 | 2026-06-05 | 2,330.72 | -5.4% |
| AUROPHARMA | 2026-04-06 | 1,344.00 | 2026-06-15 | 1,403.53 | +4.4% |
| MCX | 2026-02-02 | 2,212.70 | 2026-07-07 | 2,618.20 | +18.3% |
| THERMAX | 2026-04-06 | 3,295.80 | 2026-07-29 | 4,306.64 | +30.7% |
| VTL | 2026-03-30 | 520.95 | 2026-07-31 | 592.80 | +13.8% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-03-16 | 6,400.00 | 2026-09-15 | 7,158.25 | +11.8% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_MONTH_1.2.csv` beside this report (23135 events in all).*

```
2020-04-13  DEEPAKNTR   BUY ₹10.00 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 2.47×, ladder rising; stop ₹240.25; charges ₹0.0118)
2020-04-27  CADILAHC    BUY ₹10.01 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 5.12×, ladder rising; stop ₹310.03; charges ₹0.0119)
2020-04-27  SYNGENE     BUY ₹10.02 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.94×, ladder rising; stop ₹285.95; charges ₹0.0119)
2020-04-27  TAJGVK      BUY ₹10.01 at ₹133.40 (fresh Friday signal — BUY: 6.65× weekly, month 2.23×, ladder rising; stop ₹106.49; charges ₹0.0119)
2020-05-04  BALAJITELE  BUY ₹9.94 at ₹61.40 (fresh Friday signal — BUY: surged 4.19× weekly on 2020-04-24 (month 2.47×), ladder rising NOW — promoted from the ladder watch; stop ₹48.55; charges ₹0.0118)
2020-05-11  APLLTD      BUY ₹9.89 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.70× weekly, month 6.10×, ladder rising; stop ₹694.45; charges ₹0.0117)
2020-05-11  EIDPARRY    BUY ₹9.93 at ₹164.00 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 1.46×, ladder rising; stop ₹132.60; charges ₹0.0118)
2020-05-11  IOLCP       BUY ₹9.89 at ₹66.18 (fresh Friday signal — BUY: 2.18× weekly, month 2.65×, ladder rising; stop ₹51.22; charges ₹0.0117)
2020-05-18  ADVENZYMES  BUY ₹10.18 at ₹159.95 (fresh Friday signal — ACCUMULATE: 3.12× weekly, month 2.00×, ladder rising; stop ₹126.20; charges ₹0.0121)
2020-05-18  ALEMBICLTD  BUY ₹10.13 at ₹54.90 (fresh Friday signal — ACCUMULATE: 2.50× weekly, month 2.01×, ladder rising; stop ₹44.84; charges ₹0.0120)
2020-06-12  DEEPAKNTR   SELL ₹9.97 at stop ₹474.05 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-06-15  PANACEABIO  BUY ₹9.97 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.25×, ladder rising; stop ₹114.11; charges ₹0.0118)
2020-06-16  IOLCP       SELL ₹10.34 at stop ₹69.35 (+4.8%, charges ₹0.0107) — the cash goes back to work at the next Friday screen
2020-06-22  HATHWAY     BUY ₹10.34 at ₹34.80 (fresh Friday signal — BUY: 9.17× weekly, month 6.59×, ladder rising; stop ₹19.97; charges ₹0.0123)
2020-06-29  HATHWAY     SELL ₹9.31 at stop ₹31.40 (-9.8%, charges ₹0.0097) — the cash goes back to work at the next Friday screen
2020-07-06  NBIFIN      BUY ₹9.31 at ₹1,610.00 (fresh Friday signal — ACCUMULATE: 9.85× weekly, month 1.32×, ladder rising; stop ₹1,362.07; charges ₹0.0110)
2020-08-17  EIDPARRY    SELL ₹16.49 at stop ₹273.03 (+66.5%, charges ₹0.0171) — the cash goes back to work at the next Friday screen
2020-08-20  PANACEABIO  SELL ₹7.96 at stop ₹184.01 (-20.0%, charges ₹0.0083) — the cash goes back to work at the next Friday screen
2020-08-24  APCOTEXIND  BUY ₹12.84 at ₹164.95 (fresh Friday signal — BUY: 8.08× weekly, month 5.83×, ladder rising; stop ₹119.51; charges ₹0.0152)
2020-08-24  KIOCL       BUY ₹11.61 at ₹152.50 (fresh Friday signal — BUY: 7.39× weekly, month 5.13×, ladder rising; stop ₹107.06; charges ₹0.0138)
2020-08-31  APCOTEXIND  SELL ₹11.80 at stop ₹151.95 (-7.9%, charges ₹0.0122) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.83 at stop ₹928.62 (+19.9%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹12.43 at ₹1,398.95 (fresh Friday signal — BUY: 5.36× weekly, month 3.91×, ladder rising; stop ₹1,211.25; charges ₹0.0147)
2020-09-07  PRINCEPIPE  BUY ₹11.20 at ₹208.00 (fresh Friday signal — BUY: 3.47× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.0133)
2020-09-08  CADILAHC    SELL ₹11.04 at stop ₹364.99 (+10.5%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-09  BALAJITELE  SELL ₹11.96 at stop ₹74.07 (+20.6%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-14  SATIA       BUY ₹10.23 at ₹122.00 (fresh Friday signal — ACCUMULATE: 2.86× weekly, month 6.16×, ladder rising; stop ₹102.97; charges ₹0.0121)
2020-09-14  TCI         BUY ₹12.77 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.76× weekly, month 3.77×, ladder rising; stop ₹190.07; charges ₹0.0151)
2020-09-17  NBIFIN      SELL ₹7.86 at stop ₹1,362.07 (-15.4%, charges ₹0.0082) — the cash goes back to work at the next Friday screen
2020-09-21  SAKSOFT     BUY ₹7.86 at ₹391.45 (fresh Friday signal — BUY: 10.05× weekly, month 5.99×, ladder rising; stop ₹236.70; charges ₹0.0093)
2020-09-22  KIOCL       SELL ₹8.74 at stop ₹115.10 (-24.5%, charges ₹0.0091) — the cash goes back to work at the next Friday screen
2020-09-22  SATIA       SELL ₹8.62 at stop ₹102.97 (-15.6%, charges ₹0.0089) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹9.47 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹12.85 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0152)
2020-09-28  KPITTECH    BUY ₹12.85 at ₹113.60 (fresh Friday signal — ACCUMULATE: 2.60× weekly, month 3.04×, ladder rising; stop ₹93.15; charges ₹0.0152)
2020-10-12  PRINCEPIPE  SELL ₹11.87 at stop ₹220.88 (+6.2%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2020-10-19  LTTS        BUY ₹12.61 at ₹1,745.00 (fresh Friday signal — BUY: 4.76× weekly, month 2.59×, ladder rising; stop ₹1,482.95; charges ₹0.0149)
2020-11-02  ALEMBICLTD  SELL ₹16.83 at stop ₹91.41 (+66.5%, charges ₹0.0175) — the cash goes back to work at the next Friday screen
2020-11-02  KPITTECH    SELL ₹10.51 at stop ₹93.15 (-18.0%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2020-11-03  ADVENZYMES  SELL ₹18.56 at stop ₹292.33 (+82.8%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2020-11-09  DABUR       BUY ₹10.64 at ₹530.00 (fresh Friday signal — ACCUMULATE: 1.81× weekly, month 1.28×, ladder rising; stop ₹480.94; charges ₹0.0126)
2020-11-09  GREENPANEL  BUY ₹11.87 at ₹86.40 (fresh Friday signal — BUY: 2.76× weekly, month 1.37×, ladder rising; stop ₹63.17; charges ₹0.0141)
2020-11-09  JINDWORLD   BUY ₹11.90 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.28× weekly, month 1.55×, ladder rising; stop ₹39.81; charges ₹0.0141)
2020-11-09  RAMCOIND    BUY ₹11.88 at ₹199.00 (fresh Friday signal — ACCUMULATE: 2.92× weekly, month 1.31×, ladder rising; stop ₹155.29; charges ₹0.0141)
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹12.36 at stop ₹234.75 (-3.0%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2020-12-28  MTNL        BUY ₹13.72 at ₹14.10 (fresh Friday signal — BUY: 9.97× weekly, month 4.77×, ladder rising; stop ₹8.26; charges ₹0.0163)
2020-12-28  PAISALO     BUY ₹13.60 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0161)
2021-01-25  SAKSOFT     SELL ₹6.83 at stop ₹341.10 (-12.9%, charges ₹0.0071) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹14.20 at stop ₹928.05 (+10.7%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹14.70 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.0174)
2021-02-01  GDL         BUY ₹9.01 at ₹159.15 (fresh Friday signal — BUY: 2.82× weekly, month 6.27×, ladder rising; stop ₹92.41; charges ₹0.0107)
2021-02-16  MTNL        SELL ₹11.71 at stop ₹12.06 (-14.5%, charges ₹0.0121) — the cash goes back to work at the next Friday screen
2021-02-22  DABUR       SELL ₹10.07 at stop ₹503.12 (-5.1%, charges ₹0.0104) — the cash goes back to work at the next Friday screen
2021-02-22  MAHINDCIE   BUY ₹11.71 at ₹188.00 (fresh Friday signal — BUY: 22.74× weekly, month 4.25×, ladder rising; stop ₹143.79; charges ₹0.0139)
2021-03-01  JINDWORLD   SELL ₹12.37 at stop ₹52.12 (+4.2%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2021-03-01  RCF         BUY ₹10.07 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.13×, ladder rising; stop ₹50.16; charges ₹0.0119)
2021-03-08  JSWENERGY   BUY ₹12.37 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.50×, ladder rising; stop ₹65.79; charges ₹0.0147)
2021-03-17  RCF         SELL ₹9.95 at stop ₹79.16 (-1.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹16.78 at stop ₹204.25 (+14.5%, charges ₹0.0174) — the cash goes back to work at the next Friday screen
2021-03-19  MAHINDCIE   SELL ₹9.85 at stop ₹158.46 (-15.7%, charges ₹0.0102) — the cash goes back to work at the next Friday screen
2021-03-19  RAMCOIND    SELL ₹14.07 at stop ₹236.22 (+18.7%, charges ₹0.0146) — the cash goes back to work at the next Friday screen
2021-03-22  GFLLIMITED  BUY ₹14.89 at ₹93.00 (fresh Friday signal — ACCUMULATE: 6.17× weekly, month 3.98×, ladder rising; stop ₹74.39; charges ₹0.0176)
2021-03-22  KEI         BUY ₹14.97 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.0177)
2021-03-22  VIDHIING    BUY ₹14.81 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0175)
2021-03-25  BANARISUG   SELL ₹14.07 at stop ₹1,586.36 (+13.4%, charges ₹0.0146) — the cash goes back to work at the next Friday screen
2021-03-25  GREENPANEL  SELL ₹21.09 at stop ₹153.89 (+78.1%, charges ₹0.0219) — the cash goes back to work at the next Friday screen
2021-03-30  ADANITRANS  BUY ₹15.03 at ₹896.00 (fresh Friday signal — BUY: 1.91× weekly, month 1.35×, ladder rising; stop ₹693.23; charges ₹0.0178)
2021-03-30  CENTRUM     BUY ₹11.11 at ₹28.40 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 6.70×, ladder rising; stop ₹24.89; charges ₹0.0132)
2021-03-30  SHANKARA    BUY ₹15.00 at ₹413.00 (fresh Friday signal — ACCUMULATE: 1.99× weekly, month 1.30×, ladder rising; stop ₹354.55; charges ₹0.0178)
2021-04-01  ADANITRANS  TRIM 4.5% (₹0.75 at ₹999.20) to pay the tax bill
2021-04-01  CENTRUM     TRIM 4.5% (₹0.49 at ₹28.35) to pay the tax bill
2021-04-01  GDL         TRIM 4.5% (₹0.45 at ₹177.90) to pay the tax bill
2021-04-01  GFLLIMITED  TRIM 4.5% (₹0.77 at ₹108.35) to pay the tax bill
2021-04-01  JSWENERGY   TRIM 4.5% (₹0.61 at ₹90.70) to pay the tax bill
2021-04-01  KEI         TRIM 4.5% (₹0.67 at ₹528.60) to pay the tax bill
2021-04-01  LTTS        TRIM 4.5% (₹0.87 at ₹2,720.60) to pay the tax bill
2021-04-01  PAISALO     TRIM 4.5% (₹0.83 at ₹78.11) to pay the tax bill
2021-04-01  SHANKARA    TRIM 4.5% (₹0.69 at ₹425.05) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹6.8328 paid (STCG ₹34.16 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  VIDHIING    TRIM 4.5% (₹0.70 at ₹207.10) to pay the tax bill
2021-04-12  CENTRUM     SELL ₹9.28 at stop ₹24.89 (-12.4%, charges ₹0.0096) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹16.47 at stop ₹72.41 (+27.1%, charges ₹0.0171) — the cash goes back to work at the next Friday screen
2021-04-13  GFLLIMITED  SELL ₹11.35 at stop ₹74.39 (-20.0%, charges ₹0.0118) — the cash goes back to work at the next Friday screen
2021-04-19  EMAMIPAP    BUY ₹10.18 at ₹125.00 (fresh Friday signal — ACCUMULATE: 2.31× weekly, month 22.17×, ladder rising; stop ₹81.22; charges ₹0.0121)
2021-04-19  KPRMILL     BUY ₹13.45 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0159)
2021-04-19  MOREPENLAB  BUY ₹13.47 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹0.0160)
2021-06-18  VIDHIING    SELL ₹13.24 at stop ₹182.64 (-6.2%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2021-06-21  SOMANYCERA  BUY ₹13.24 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0157)
2021-08-10  MOREPENLAB  SELL ₹20.21 at stop ₹56.33 (+50.4%, charges ₹0.0210) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹20.05 at stop ₹352.48 (+49.4%, charges ₹0.0208) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹21.41 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.0254)
2021-08-16  TATAINVEST  BUY ₹18.86 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0223)
2021-09-20  GDL         SELL ₹14.35 at stop ₹266.00 (+67.1%, charges ₹0.0149) — the cash goes back to work at the next Friday screen
2021-09-27  NEOGEN      BUY ₹14.35 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0170)
2021-10-22  KEI         SELL ₹23.32 at stop ₹853.10 (+63.4%, charges ₹0.0242) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹18.70 at stop ₹3,220.59 (-12.5%, charges ₹0.0194) — the cash goes back to work at the next Friday screen
2021-10-25  NEOGEN      SELL ₹13.04 at stop ₹1,142.85 (-8.9%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2021-10-25  TTKPRESTIG  BUY ₹22.58 at ₹9,508.95 (fresh Friday signal — BUY: 6.63× weekly, month 1.31×, ladder rising; stop ₹8,326.75; charges ₹0.0268)
2021-11-01  TCIEXP      BUY ₹23.00 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0273)
2021-11-22  EMAMIPAP    SELL ₹11.50 at stop ₹141.55 (+13.2%, charges ₹0.0119) — the cash goes back to work at the next Friday screen
2021-11-26  TATAINVEST  SELL ₹20.66 at stop ₹1,436.49 (+9.8%, charges ₹0.0214) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹23.86 at stop ₹10,070.05 (+5.9%, charges ₹0.0247) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹19.46 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.0231)
2021-11-29  RAYMOND     BUY ₹22.96 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0272)
2021-11-29  RSYSTEMS    BUY ₹23.09 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0274)
2021-11-29  SHANKARA    SELL ₹16.94 at stop ₹489.25 (+18.5%, charges ₹0.0176) — the cash goes back to work at the next Friday screen
2021-11-29  SOMANYCERA  SELL ₹16.77 at stop ₹755.11 (+26.9%, charges ₹0.0174) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹23.00 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0273)
2021-12-16  RSYSTEMS    SELL ₹20.65 at stop ₹291.18 (-10.4%, charges ₹0.0214) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹22.64 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0268)
2021-12-21  TCIEXP      SELL ₹25.57 at stop ₹2,039.74 (+11.4%, charges ₹0.0265) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹22.91 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0271)
2022-01-21  LTTS        SELL ₹33.45 at stop ₹4,856.88 (+178.3%, charges ₹0.0347) — the cash goes back to work at the next Friday screen
2022-01-24  JSWISPL     BUY ₹23.12 at ₹37.50 (fresh Friday signal — BUY: 5.58× weekly, month 4.04×, ladder rising; stop ₹27.79; charges ₹0.0274)
2022-01-24  SHARDACROP  BUY ₹21.70 at ₹420.00 (fresh Friday signal — BUY: 5.41× weekly, month 2.31×, ladder rising; stop ₹342.00; charges ₹0.0257)
2022-01-25  SWANENERGY  SELL ₹24.80 at stop ₹162.64 (+8.5%, charges ₹0.0257) — the cash goes back to work at the next Friday screen
2022-01-31  TV18BRDCST  BUY ₹24.06 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.0285)
2022-02-11  SHARDACROP  SELL ₹28.12 at stop ₹545.30 (+29.8%, charges ₹0.0292) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹17.72 at stop ₹424.65 (-8.7%, charges ₹0.0184) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹23.56 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0279)
2022-02-15  RAYMOND     SELL ₹26.11 at stop ₹679.35 (+14.0%, charges ₹0.0271) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹22.94 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0272)
2022-02-21  LAXMIMACH   BUY ₹22.90 at ₹10,118.80 (fresh Friday signal — BUY: surged 2.17× weekly on 2022-01-21 (month 1.69×), ladder rising NOW — promoted from the ladder watch; stop ₹10,169.75; charges ₹0.0271)
2022-02-22  GREENLAM    SELL ₹19.49 at stop ₹313.67 (-13.7%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2022-02-22  LAXMIMACH   SELL ₹22.96 at stop ₹10,169.75 (+0.5%, charges ₹0.0238) — the cash goes back to work at the next Friday screen
2022-02-22  TV18BRDCST  SELL ₹23.80 at stop ₹58.38 (-0.9%, charges ₹0.0247) — the cash goes back to work at the next Friday screen
2022-02-24  JSWISPL     SELL ₹18.61 at stop ₹30.25 (-19.3%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹23.17 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0274)
2022-02-28  SHANTIGEAR  BUY ₹23.28 at ₹185.30 (fresh Friday signal — BUY: surged 3.40× weekly on 2022-02-11 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹170.29; charges ₹0.0276)
2022-03-07  GTLINFRA    BUY ₹23.56 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0279)
2022-03-07  RAJMET      BUY ₹18.15 at ₹278.00 (fresh Friday signal — BUY: surged 6.93× weekly on 2022-02-18 (month 4.62×), ladder rising NOW — promoted from the ladder watch; stop ₹226.96; charges ₹0.0215)
2022-03-21  BSE         SELL ₹19.85 at stop ₹1,634.39 (-13.5%, charges ₹0.0206) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹9.4406 paid (STCG ₹33.79 @20%, LTCG ₹21.46 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-29  GTLINFRA    SELL ₹19.50 at stop ₹1.41 (-17.1%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹27.64 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.0328)
2022-05-11  ADANITRANS  SELL ₹36.77 at stop ₹2,299.37 (+156.6%, charges ₹0.0381) — the cash goes back to work at the next Friday screen
2022-05-11  MFL         SELL ₹23.64 at stop ₹1,225.50 (-14.3%, charges ₹0.0245) — the cash goes back to work at the next Friday screen
2022-05-16  KRISHANA    BUY ₹26.63 at ₹67.96 (fresh Friday signal — ACCUMULATE: 1.67× weekly, month 1.86×, ladder rising; stop ₹54.77; charges ₹0.0316)
2022-05-16  VBL         BUY ₹26.62 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0315)
2022-06-06  VBL         SELL ₹23.70 at stop ₹196.27 (-10.8%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹26.44 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0313)
2022-06-16  KRISHANA    SELL ₹21.41 at stop ₹54.77 (-19.4%, charges ₹0.0222) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹25.76 at ₹950.15 (fresh Friday signal — BUY: surged 6.84× weekly on 2022-06-10 (month 1.49×), ladder rising NOW — promoted from the ladder watch; stop ₹706.80; charges ₹0.0305)
2022-06-20  JSWENERGY   SELL ₹29.11 at stop ₹201.99 (+146.8%, charges ₹0.0302) — the cash goes back to work at the next Friday screen
2022-06-27  INSECTICID  BUY ₹26.44 at ₹844.00 (fresh Friday signal — BUY: 1.82× weekly, month 1.31×, ladder rising; stop ₹712.50; charges ₹0.0313)
2022-09-06  DANGEE      SELL ₹36.91 at stop ₹375.25 (+59.7%, charges ₹0.0383) — the cash goes back to work at the next Friday screen
2022-09-12  SHREECEM    BUY ₹30.40 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0360)
2022-09-15  RAJMET      SELL ₹23.40 at stop ₹359.30 (+29.2%, charges ₹0.0243) — the cash goes back to work at the next Friday screen
2022-09-19  JSWHL       BUY ₹30.06 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0356)
2022-09-29  INSECTICID  SELL ₹28.97 at stop ₹926.73 (+9.8%, charges ₹0.0300) — the cash goes back to work at the next Friday screen
2022-10-03  SUNDARMHLD  BUY ₹28.94 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹0.0343)
2022-10-11  SUNDARMHLD  SELL ₹25.72 at stop ₹92.20 (-10.9%, charges ₹0.0267) — the cash goes back to work at the next Friday screen
2022-10-17  RVNL        BUY ₹29.35 at ₹36.85 (fresh Friday signal — BUY: 4.04× weekly, month 1.42×, ladder rising; stop ₹31.21; charges ₹0.0348)
2022-11-03  APARINDS    SELL ₹36.75 at stop ₹1,358.50 (+43.0%, charges ₹0.0381) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹32.06 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0380)
2022-12-21  ELECON      SELL ₹43.62 at stop ₹202.49 (+65.3%, charges ₹0.0452) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹43.31 at stop ₹345.56 (+86.5%, charges ₹0.0449) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹31.95 at stop ₹139.84 (-0.1%, charges ₹0.0331) — the cash goes back to work at the next Friday screen
2022-12-26  GICRE       BUY ₹27.69 at ₹157.00 (fresh Friday signal — BUY: surged 4.73× weekly on 2022-12-02 (month 1.82×), ladder rising NOW — promoted from the ladder watch; stop ₹134.14; charges ₹0.0328)
2022-12-26  JINDWORLD   BUY ₹32.39 at ₹415.10 (fresh Friday signal — BUY: 3.67× weekly, month 1.21×, ladder rising; stop ₹362.90; charges ₹0.0384)
2022-12-26  KRISHANA    BUY ₹32.22 at ₹83.60 (fresh Friday signal — BUY: 3.70× weekly, month 2.29×, ladder rising; stop ₹75.36; charges ₹0.0382)
2022-12-26  KSL         BUY ₹32.52 at ₹330.10 (fresh Friday signal — BUY: surged 5.50× weekly on 2022-12-09 (month 2.50×), ladder rising NOW — promoted from the ladder watch; stop ₹328.23; charges ₹0.0385)
2022-12-26  RVNL        SELL ₹48.14 at stop ₹60.57 (+64.4%, charges ₹0.0499) — the cash goes back to work at the next Friday screen
2023-01-02  MUKANDLTD   BUY ₹33.35 at ₹136.70 (fresh Friday signal — BUY: 6.81× weekly, month 2.54×, ladder rising; stop ₹103.76; charges ₹0.0395)
2023-01-27  KSL         SELL ₹32.26 at stop ₹328.23 (-0.6%, charges ₹0.0335) — the cash goes back to work at the next Friday screen
2023-01-30  LSIL        BUY ₹31.89 at ₹23.20 (fresh Friday signal — BUY: 2.28× weekly, month 3.56×, ladder rising; stop ₹11.29; charges ₹0.0378)
2023-02-01  GICRE       SELL ₹29.52 at stop ₹167.72 (+6.8%, charges ₹0.0306) — the cash goes back to work at the next Friday screen
2023-02-01  JINDWORLD   SELL ₹30.32 at stop ₹389.50 (-6.2%, charges ₹0.0315) — the cash goes back to work at the next Friday screen
2023-02-06  CHOLAFIN    BUY ₹30.95 at ₹777.55 (fresh Friday signal — BUY: 2.87× weekly, month 1.34×, ladder rising; stop ₹661.25; charges ₹0.0367)
2023-02-06  JINDALSAW   BUY ₹30.96 at ₹65.22 (fresh Friday signal — BUY: 2.72× weekly, month 3.57×, ladder rising; stop ₹51.25; charges ₹0.0367)
2023-02-07  LSIL        SELL ₹27.48 at stop ₹20.04 (-13.6%, charges ₹0.0285) — the cash goes back to work at the next Friday screen
2023-02-13  CIGNITITEC  BUY ₹31.45 at ₹673.00 (fresh Friday signal — BUY: 3.13× weekly, month 1.41×, ladder rising; stop ₹568.10; charges ₹0.0373)
2023-02-17  CGCL        SELL ₹26.91 at stop ₹704.95 (+17.6%, charges ₹0.0279) — the cash goes back to work at the next Friday screen
2023-02-20  TIIL        BUY ₹32.04 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0380)
2023-03-20  KRISHANA    SELL ₹36.30 at stop ₹94.40 (+12.9%, charges ₹0.0377) — the cash goes back to work at the next Friday screen
2023-03-24  CHOLAFIN    SELL ₹28.89 at stop ₹727.37 (-6.5%, charges ₹0.0300) — the cash goes back to work at the next Friday screen
2023-03-27  JINDALSAW   SELL ₹32.17 at stop ₹67.92 (+4.1%, charges ₹0.0334) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹31.33 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.61×, ladder rising; stop ₹372.21; charges ₹0.0371)
2023-03-27  SONATSOFTW  BUY ₹31.28 at ₹413.70 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 4.94×, ladder rising; stop ₹371.45; charges ₹0.0371)
2023-03-29  CIGNITITEC  SELL ₹32.88 at stop ₹705.14 (+4.8%, charges ₹0.0341) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹50.79 at stop ₹112.36 (+116.1%, charges ₹0.0527) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹28.02 at stop ₹371.45 (-10.2%, charges ₹0.0291) — the cash goes back to work at the next Friday screen
2023-04-03  ANURAS      BUY ₹28.92 at ₹868.95 (fresh Friday signal — BUY: surged 2.13× weekly on 2023-03-10 (month 1.83×), ladder rising NOW — promoted from the ladder watch; stop ₹691.46; charges ₹0.0343)
2023-04-03  HAL         BUY ₹28.99 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.0343)
2023-04-03  INGERRAND   BUY ₹28.94 at ₹2,690.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2023-03-10 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹2,170.84; charges ₹0.0343)
2023-04-03  NATCOPHARM  BUY ₹28.94 at ₹569.80 (fresh Friday signal — ACCUMULATE: 1.84× weekly, month 1.46×, ladder rising; stop ₹494.24; charges ₹0.0343)
2023-04-03  TAX         FY2023 settled: ₹22.5800 paid (STCG ₹70.96 @20%, LTCG ₹67.11 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-24  SHREECEM    SELL ₹29.14 at stop ₹23,636.00 (-3.9%, charges ₹0.0302) — the cash goes back to work at the next Friday screen
2023-05-02  GUJALKALI   BUY ₹30.30 at ₹688.15 (fresh Friday signal — BUY: 22.10× weekly, month 1.42×, ladder rising; stop ₹590.90; charges ₹0.0359)
2023-05-17  MUKANDLTD   SELL ₹28.30 at stop ₹116.23 (-15.0%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2023-05-22  SHARDAMOTR  BUY ₹30.44 at ₹380.00 (fresh Friday signal — BUY: 9.54× weekly, month 2.31×, ladder rising; stop ₹342.95; charges ₹0.0361)
2023-05-23  GUJALKALI   SELL ₹28.39 at stop ₹646.14 (-6.1%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2023-05-29  THANGAMAYL  BUY ₹31.09 at ₹1,344.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.50×, ladder rising; stop ₹1,116.30; charges ₹0.0368)
2023-07-03  ANURAS      SELL ₹33.46 at stop ₹1,007.67 (+16.0%, charges ₹0.0347) — the cash goes back to work at the next Friday screen
2023-07-10  GENUSPOWER  BUY ₹32.09 at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.48×, ladder rising; stop ₹99.51; charges ₹0.0380)
2023-07-12  KSB         SELL ₹30.50 at stop ₹407.74 (-2.4%, charges ₹0.0316) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹31.17 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0369)
2023-07-17  THANGAMAYL  SELL ₹31.03 at stop ₹1,344.25 (+0.0%, charges ₹0.0322) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹32.65 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.84×, ladder rising; stop ₹359.10; charges ₹0.0387)
2023-08-14  GANESHHOUC  SELL ₹29.84 at stop ₹418.62 (-8.4%, charges ₹0.0310) — the cash goes back to work at the next Friday screen
2023-08-21  ASTRAZEN    BUY ₹35.00 at ₹4,099.85 (fresh Friday signal — BUY: 6.03× weekly, month 2.40×, ladder rising; stop ₹3,562.50; charges ₹0.0415)
2023-09-13  INGERRAND   SELL ₹32.45 at stop ₹3,022.99 (+12.4%, charges ₹0.0337) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹32.45 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.67×, ladder rising; stop ₹58.28; charges ₹0.0384)
2023-10-23  SJVN        SELL ₹28.37 at stop ₹66.03 (-12.4%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹38.58 at stop ₹1,840.70 (+33.4%, charges ₹0.0400) — the cash goes back to work at the next Friday screen
2023-10-25  SHARDAMOTR  SELL ₹37.17 at stop ₹465.07 (+22.4%, charges ₹0.0386) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹28.08 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0333)
2023-10-30  KKCL        BUY ₹38.03 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0451)
2023-10-30  SHAREINDIA  BUY ₹38.00 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0450)
2023-11-01  NATCOPHARM  SELL ₹39.09 at stop ₹771.40 (+35.4%, charges ₹0.0405) — the cash goes back to work at the next Friday screen
2023-11-06  SUNDARMHLD  BUY ₹39.09 at ₹144.75 (fresh Friday signal — BUY: 3.35× weekly, month 1.95×, ladder rising; stop ₹109.72; charges ₹0.0463)
2023-11-16  GENUSPOWER  SELL ₹46.01 at stop ₹234.03 (+43.7%, charges ₹0.0477) — the cash goes back to work at the next Friday screen
2023-11-20  ISMTLTD     BUY ₹41.10 at ₹94.60 (fresh Friday signal — BUY: 5.37× weekly, month 1.93×, ladder rising; stop ₹80.18; charges ₹0.0487)
2023-12-20  ISMTLTD     SELL ₹38.30 at stop ₹88.35 (-6.6%, charges ₹0.0397) — the cash goes back to work at the next Friday screen
2023-12-20  SUNDARMHLD  SELL ₹39.18 at stop ₹145.40 (+0.4%, charges ₹0.0406) — the cash goes back to work at the next Friday screen
2023-12-26  MMFL        BUY ₹44.04 at ₹1,023.60 (fresh Friday signal — BUY: 9.43× weekly, month 3.43×, ladder rising; stop ₹821.80; charges ₹0.0522)
2023-12-26  OIL         BUY ₹38.35 at ₹251.27 (fresh Friday signal — BUY: 6.09× weekly, month 3.92×, ladder rising; stop ₹186.55; charges ₹0.0454)
2024-01-17  TIIL        SELL ₹66.90 at stop ₹2,337.00 (+109.3%, charges ₹0.0694) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹44.37 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0526)
2024-01-30  MMFL        SELL ₹39.15 at stop ₹912.05 (-10.9%, charges ₹0.0406) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹48.29 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0572)
2024-02-09  ASTRAZEN    SELL ₹49.37 at stop ₹5,795.95 (+41.4%, charges ₹0.0512) — the cash goes back to work at the next Friday screen
2024-02-12  IOB         BUY ₹46.31 at ₹71.50 (fresh Friday signal — BUY: 7.81× weekly, month 2.91×, ladder rising; stop ₹38.71; charges ₹0.0549)
2024-03-06  SHAREINDIA  SELL ₹45.15 at stop ₹357.20 (+19.1%, charges ₹0.0468) — the cash goes back to work at the next Friday screen
2024-03-11  SOLARINDS   BUY ₹49.38 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0585)
2024-03-11  TCI         SELL ₹38.56 at stop ₹790.40 (-20.0%, charges ₹0.0400) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹33.58 at stop ₹674.12 (-11.5%, charges ₹0.0348) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹44.47 at stop ₹666.47 (+0.5%, charges ₹0.0461) — the cash goes back to work at the next Friday screen
2024-03-15  OIL         SELL ₹52.47 at stop ₹344.53 (+37.1%, charges ₹0.0544) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹41.10 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.0487)
2024-03-18  FORCEMOT    BUY ₹46.69 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.0553)
2024-03-18  INDIGO      BUY ₹46.62 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0552)
2024-03-18  TRENT       BUY ₹46.90 at ₹2,709.27 (fresh Friday signal — ACCUMULATE: 1.86× weekly, month 1.33×, ladder rising; stop ₹2,395.27; charges ₹0.0556)
2024-03-27  ANANDRATHI  SELL ₹100.98 at stop ₹862.65 (+224.7%, charges ₹0.1048) — the cash goes back to work at the next Friday screen
2024-04-01  DMART       BUY ₹25.30 at ₹4,570.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.56×, ladder rising; stop ₹3,695.50; charges ₹0.0300)
2024-04-01  SHRIRAMFIN  BUY ₹45.07 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0534)
2024-04-01  TAX         FY2024 settled: ₹30.6147 paid (STCG ₹153.07 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-13  JSWHL       SELL ₹40.08 at stop ₹6,280.45 (+33.6%, charges ₹0.0416) — the cash goes back to work at the next Friday screen
2024-05-21  KIRLOSBROS  BUY ₹40.08 at ₹1,844.00 (fresh Friday signal — BUY: 5.41× weekly, month 1.62×, ladder rising; stop ₹1,221.51; charges ₹0.0475)
2024-05-28  FORCEMOT    SELL ₹57.33 at stop ₹8,083.64 (+23.1%, charges ₹0.0595) — the cash goes back to work at the next Friday screen
2024-05-31  DMART       SELL ₹23.88 at stop ₹4,322.83 (-5.4%, charges ₹0.0248) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹48.03 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0569)
2024-06-03  THERMAX     BUY ₹33.18 at ₹5,640.00 (fresh Friday signal — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹0.0393)
2024-06-04  BOSCHLTD    SELL ₹40.33 at stop ₹29,015.09 (-1.6%, charges ₹0.0418) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹41.89 at stop ₹441.77 (-6.8%, charges ₹0.0435) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹51.99 at stop ₹7,980.95 (+5.5%, charges ₹0.0539) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹46.05 at ₹783.00 (fresh Friday signal — BUY: 7.38× weekly, month 1.40×, ladder rising; stop ₹632.75; charges ₹0.0546)
2024-06-10  FIEMIND     BUY ₹46.20 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0547)
2024-06-10  UNOMINDA    BUY ₹41.96 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0497)
2024-07-19  UNOMINDA    SELL ₹42.38 at stop ₹981.87 (+1.2%, charges ₹0.0440) — the cash goes back to work at the next Friday screen
2024-07-22  HBLPOWER    BUY ₹42.38 at ₹585.00 (fresh Friday signal — BUY: 3.57× weekly, month 1.41×, ladder rising; stop ₹522.78; charges ₹0.0502)
2024-07-22  TRENT       SELL ₹59.83 at stop ₹3,464.36 (+27.9%, charges ₹0.0621) — the cash goes back to work at the next Friday screen
2024-07-23  FIEMIND     SELL ₹43.92 at stop ₹1,257.56 (-4.7%, charges ₹0.0456) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹47.39 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0561)
2024-07-29  THYROCARE   BUY ₹47.43 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0562)
2024-08-05  KIRLOSBROS  SELL ₹43.10 at stop ₹1,987.46 (+7.8%, charges ₹0.0447) — the cash goes back to work at the next Friday screen
2024-08-05  THERMAX     SELL ₹27.70 at stop ₹4,719.70 (-16.3%, charges ₹0.0287) — the cash goes back to work at the next Friday screen
2024-08-12  ADANIPOWER  SELL ₹37.13 at stop ₹632.75 (-19.2%, charges ₹0.0385) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹45.82 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0543)
2024-08-12  CERA        BUY ₹33.92 at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹0.0402)
2024-08-16  CAMPUS      SELL ₹46.43 at stop ₹277.07 (-3.1%, charges ₹0.0482) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹44.85 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0531)
2024-08-19  VGUARD      BUY ₹38.72 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.0459)
2024-09-09  AVANTIFEED  SELL ₹44.06 at stop ₹650.13 (-6.8%, charges ₹0.0457) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹44.06 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0522)
2024-09-19  CERA        SELL ₹26.43 at stop ₹8,198.93 (-21.9%, charges ₹0.0274) — the cash goes back to work at the next Friday screen
2024-09-23  BSE         BUY ₹26.43 at ₹4,001.00 (fresh Friday signal — BUY: 9.15× weekly, month 2.06×, ladder rising; stop ₹2,565.09; charges ₹0.0313)
2024-10-03  IOB         SELL ₹36.56 at stop ₹56.57 (-20.9%, charges ₹0.0379) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹30.97 at stop ₹420.24 (-19.8%, charges ₹0.0321) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹42.61 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0505)
2024-10-07  INDIGO      SELL ₹65.20 at stop ₹4,485.14 (+40.2%, charges ₹0.0676) — the cash goes back to work at the next Friday screen
2024-10-07  ITDCEM      BUY ₹24.92 at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹0.0295)
2024-10-07  THYROCARE   SELL ₹48.00 at stop ₹796.15 (+1.4%, charges ₹0.0498) — the cash goes back to work at the next Friday screen
2024-10-14  DBCORP      BUY ₹43.55 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0516)
2024-10-14  GANECOS     BUY ₹43.38 at ₹2,103.85 (fresh Friday signal — BUY: 3.56× weekly, month 1.32×, ladder rising; stop ₹1,646.57; charges ₹0.0514)
2024-10-14  SKIPPER     BUY ₹26.27 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0311)
2024-10-22  BASF        SELL ₹47.34 at stop ₹7,611.30 (+3.6%, charges ₹0.0491) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹37.29 at stop ₹302.08 (-14.2%, charges ₹0.0387) — the cash goes back to work at the next Friday screen
2024-10-25  HBLPOWER    SELL ₹37.79 at stop ₹522.78 (-10.6%, charges ₹0.0392) — the cash goes back to work at the next Friday screen
2024-10-28  CIGNITITEC  BUY ₹36.79 at ₹1,515.00 (fresh Friday signal — BUY: 9.95× weekly, month 1.36×, ladder rising; stop ₹1,308.67; charges ₹0.0436)
2024-10-28  COFORGE     BUY ₹36.68 at ₹1,543.10 (fresh Friday signal — BUY: 3.74× weekly, month 1.36×, ladder rising; stop ₹1,274.91; charges ₹0.0435)
2024-10-28  CUPID       SELL ₹36.74 at stop ₹158.66 (+31.1%, charges ₹0.0381) — the cash goes back to work at the next Friday screen
2024-10-28  JSWHL       BUY ₹36.68 at ₹9,600.00 (fresh Friday signal — BUY: 3.86× weekly, month 1.32×, ladder rising; stop ₹7,629.63; charges ₹0.0435)
2024-11-04  AKZOINDIA   BUY ₹41.32 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.0975)
2024-11-14  ASTRAZEN    SELL ₹39.11 at stop ₹6,854.77 (-7.9%, charges ₹0.0869) — the cash goes back to work at the next Friday screen
2024-11-18  CIGNITITEC  SELL ₹32.19 at stop ₹1,330.00 (-12.2%, charges ₹0.0715) — the cash goes back to work at the next Friday screen
2024-11-18  GANESHHOUC  BUY ₹43.80 at ₹1,059.00 (fresh Friday signal — BUY: surged 4.01× weekly on 2024-10-18 (month 1.75×), ladder rising NOW — promoted from the ladder watch; stop ₹867.10; charges ₹0.1034)
2024-11-25  GARFIBRES   BUY ₹35.20 at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹0.0831)
2024-12-17  SUPRIYA     SELL ₹60.71 at stop ₹717.25 (+35.8%, charges ₹0.1349) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹44.18 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.1043)
2024-12-26  PRSMJOHNSN  SELL ₹34.91 at stop ₹170.55 (-20.5%, charges ₹0.0776) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹31.17 at stop ₹3,423.18 (-24.2%, charges ₹0.0692) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹44.13 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.1042)
2024-12-30  KFINTECH    BUY ₹38.49 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.0909)
2025-01-09  GARFIBRES   SELL ₹30.39 at stop ₹829.35 (-13.2%, charges ₹0.0675) — the cash goes back to work at the next Friday screen
2025-01-09  KSL         SELL ₹39.08 at stop ₹1,059.30 (-11.1%, charges ₹0.0868) — the cash goes back to work at the next Friday screen
2025-01-10  GANECOS     SELL ₹36.00 at stop ₹1,751.78 (-16.7%, charges ₹0.0800) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹22.59 at stop ₹477.28 (-13.7%, charges ₹0.0502) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹40.90 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0966)
2025-01-13  ASHOKA      BUY ₹40.59 at ₹271.65 (fresh Friday signal — BUY: surged 1.88× weekly on 2024-12-13 (month 1.31×), ladder rising NOW — promoted from the ladder watch; stop ₹262.67; charges ₹0.0958)
2025-01-13  COFORGE     SELL ₹42.66 at stop ₹1,801.20 (+16.7%, charges ₹0.0948) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹40.80 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.0963)
2025-01-15  KFINTECH    SELL ₹29.38 at stop ₹1,159.14 (-23.3%, charges ₹0.0653) — the cash goes back to work at the next Friday screen
2025-01-20  HCG         BUY ₹42.11 at ₹504.95 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 1.41×, ladder rising; stop ₹429.63; charges ₹0.0994)
2025-01-20  PGIL        BUY ₹35.71 at ₹833.02 (fresh Friday signal — BUY: 1.74× weekly, month 1.23×, ladder rising; stop ₹705.52; charges ₹0.0843)
2025-01-21  PGIL        SELL ₹30.10 at stop ₹705.52 (-15.3%, charges ₹0.0669) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹34.17 at stop ₹700.36 (-16.1%, charges ₹0.0759) — the cash goes back to work at the next Friday screen
2025-01-24  ASHOKA      SELL ₹39.07 at stop ₹262.67 (-3.3%, charges ₹0.0868) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹39.58 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0934)
2025-01-28  LLOYDSME    SELL ₹35.45 at stop ₹1,258.75 (-12.7%, charges ₹0.0787) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹41.00 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.0968)
2025-02-12  JINDWORLD   SELL ₹40.31 at stop ₹374.11 (-8.2%, charges ₹0.0895) — the cash goes back to work at the next Friday screen
2025-02-24  GODFRYPHLP  BUY ₹38.17 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.0901)
2025-02-28  BSE         SELL ₹32.61 at stop ₹4,954.63 (+23.8%, charges ₹0.0724) — the cash goes back to work at the next Friday screen
2025-02-28  GANESHHOUC  SELL ₹44.89 at stop ₹1,090.38 (+3.0%, charges ₹0.0997) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹36.81 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0869)
2025-03-03  ZENSARTECH  SELL ₹31.37 at stop ₹727.84 (-23.1%, charges ₹0.0697) — the cash goes back to work at the next Friday screen
2025-03-10  AVANTIFEED  BUY ₹38.76 at ₹806.00 (fresh Friday signal — BUY: 2.82× weekly, month 1.23×, ladder rising; stop ₹648.95; charges ₹0.0915)
2025-03-10  GRWRHITECH  BUY ₹38.84 at ₹4,219.95 (fresh Friday signal — BUY: surged 2.69× weekly on 2025-02-14 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹3,504.00; charges ₹0.0917)
2025-03-24  INDIASHLTR  BUY ₹42.47 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.1003)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹49.74 / LT ₹0.00)
2025-04-03  GRWRHITECH  SELL ₹33.01 at stop ₹3,602.82 (-14.6%, charges ₹0.0733) — the cash goes back to work at the next Friday screen
2025-04-07  AVANTIFEED  SELL ₹31.07 at stop ₹648.95 (-19.5%, charges ₹0.0690) — the cash goes back to work at the next Friday screen
2025-04-07  COROMANDEL  BUY ₹40.79 at ₹1,870.00 (fresh Friday signal — BUY: surged 1.58× weekly on 2025-03-21 (month 1.48×), ladder rising NOW — promoted from the ladder watch; stop ₹1,849.08; charges ₹0.0963)
2025-04-07  INDIASHLTR  SELL ₹39.29 at stop ₹738.82 (-7.1%, charges ₹0.0873) — the cash goes back to work at the next Friday screen
2025-04-11  ITDCEM      SELL ₹19.90 at stop ₹524.92 (-19.9%, charges ₹0.0442) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹42.24 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.0997)
2025-04-15  INDIASHLTR  BUY ₹42.41 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.1001)
2025-05-26  HCG         SELL ₹46.42 at stop ₹559.08 (+10.7%, charges ₹0.1031) — the cash goes back to work at the next Friday screen
2025-06-02  LICI        BUY ₹43.54 at ₹477.00 (fresh Friday signal — BUY: 6.84× weekly, month 1.25×, ladder rising; stop ₹399.00; charges ₹0.1028)
2025-06-27  COROMANDEL  SELL ₹48.78 at stop ₹2,246.75 (+20.1%, charges ₹0.1084) — the cash goes back to work at the next Friday screen
2025-06-30  ALKYLAMINE  BUY ₹44.32 at ₹2,263.00 (fresh Friday signal — BUY: 7.48× weekly, month 1.62×, ladder rising; stop ₹1,832.27; charges ₹0.1046)
2025-08-04  JSWHL       SELL ₹72.75 at stop ₹19,106.01 (+99.0%, charges ₹0.1616) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹45.86 at stop ₹1,814.78 (+25.2%, charges ₹0.1019) — the cash goes back to work at the next Friday screen
2025-08-07  ALKYLAMINE  SELL ₹40.70 at stop ₹2,087.62 (-7.7%, charges ₹0.0904) — the cash goes back to work at the next Friday screen
2025-08-07  LICI        SELL ₹39.82 at stop ₹438.21 (-8.1%, charges ₹0.0884) — the cash goes back to work at the next Friday screen
2025-08-11  DELHIVERY   BUY ₹41.71 at ₹464.65 (fresh Friday signal — BUY: 2.15× weekly, month 1.25×, ladder rising; stop ₹383.90; charges ₹0.0985)
2025-08-11  PGHL        BUY ₹41.75 at ₹6,345.00 (fresh Friday signal — BUY: 1.64× weekly, month 2.94×, ladder rising; stop ₹5,320.00; charges ₹0.0986)
2025-08-11  RAIN        BUY ₹41.78 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.0986)
2025-08-11  UPL         BUY ₹41.73 at ₹688.95 (fresh Friday signal — ACCUMULATE: 1.66× weekly, month 1.47×, ladder rising; stop ₹625.10; charges ₹0.0985)
2025-08-18  BLACKBUCK   BUY ₹41.93 at ₹553.00 (fresh Friday signal — ACCUMULATE: 3.19× weekly, month 4.96×, ladder rising; stop ₹473.20; charges ₹0.0990)
2025-08-26  RAIN        SELL ₹37.28 at stop ₹143.64 (-10.4%, charges ₹0.0828) — the cash goes back to work at the next Friday screen
2025-09-01  RSYSTEMS    BUY ₹43.24 at ₹460.00 (fresh Friday signal — BUY: surged 17.81× weekly on 2025-08-22 (month 4.67×), ladder rising NOW — promoted from the ladder watch; stop ₹394.44; charges ₹0.1021)
2025-09-16  GODFRYPHLP  SELL ₹58.94 at stop ₹8,967.50 (+55.1%, charges ₹0.1309) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹41.33 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.75× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.0976)
2025-09-24  RSYSTEMS    SELL ₹39.60 at stop ₹423.23 (-8.0%, charges ₹0.0880) — the cash goes back to work at the next Friday screen
2025-09-25  INDIASHLTR  SELL ₹42.10 at stop ₹862.60 (-0.3%, charges ₹0.0935) — the cash goes back to work at the next Friday screen
2025-09-29  LGBBROSLTD  BUY ₹40.39 at ₹1,411.60 (fresh Friday signal — BUY: 3.53× weekly, month 1.72×, ladder rising; stop ₹1,258.75; charges ₹0.0953)
2025-09-29  NETWEB      BUY ₹20.52 at ₹3,700.00 (fresh Friday signal — BUY: 2.97× weekly, month 7.27×, ladder rising; stop ₹2,674.79; charges ₹0.0484)
2025-09-29  SUBROS      BUY ₹40.17 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0948)
2025-10-01  DELHIVERY   SELL ₹38.97 at stop ₹436.10 (-6.1%, charges ₹0.0866) — the cash goes back to work at the next Friday screen
2025-10-06  ASTRAMICRO  BUY ₹38.97 at ₹1,119.85 (fresh Friday signal — BUY: 3.17× weekly, month 1.83×, ladder rising; stop ₹1,026.00; charges ₹0.0920)
2025-10-14  SUBROS      SELL ₹36.98 at stop ₹1,046.90 (-7.5%, charges ₹0.0821) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹36.98 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0873)
2025-10-20  CREDITACC   SELL ₹59.07 at stop ₹1,274.42 (+49.9%, charges ₹0.1312) — the cash goes back to work at the next Friday screen
2025-10-27  PSB         BUY ₹40.10 at ₹30.80 (fresh Friday signal — BUY: 2.36× weekly, month 1.24×, ladder rising; stop ₹27.07; charges ₹0.0947)
2025-10-28  BLACKBUCK   SELL ₹48.47 at stop ₹642.20 (+16.1%, charges ₹0.1077) — the cash goes back to work at the next Friday screen
2025-11-03  RRKABEL     BUY ₹40.88 at ₹1,475.40 (fresh Friday signal — BUY: 11.98× weekly, month 1.21×, ladder rising; stop ₹1,122.52; charges ₹0.0965)
2025-11-03  TDPOWERSYS  BUY ₹26.57 at ₹382.27 (fresh Friday signal — BUY: 4.87× weekly, month 1.95×, ladder rising; stop ₹276.78; charges ₹0.0627)
2025-11-06  ASTRAMICRO  SELL ₹35.54 at stop ₹1,026.00 (-8.4%, charges ₹0.0789) — the cash goes back to work at the next Friday screen
2025-11-06  FDC         SELL ₹35.78 at stop ₹425.79 (-13.0%, charges ₹0.0795) — the cash goes back to work at the next Friday screen
2025-11-06  NETWEB      SELL ₹19.41 at stop ₹3,515.95 (-5.0%, charges ₹0.0431) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹38.90 at stop ₹5,938.45 (-6.4%, charges ₹0.0864) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹40.53 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.0957)
2025-11-10  CUB         BUY ₹40.73 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.0961)
2025-11-10  LTF         BUY ₹40.71 at ₹304.00 (fresh Friday signal — BUY: 2.98× weekly, month 1.53×, ladder rising; stop ₹250.80; charges ₹0.0961)
2025-11-20  ANANDRATHI  SELL ₹33.91 at stop ₹1,450.17 (-7.9%, charges ₹0.0753) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹38.81 at stop ₹976.41 (-3.8%, charges ₹0.0862) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹40.72 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0961)
2025-11-24  TDPOWERSYS  SELL ₹24.73 at stop ₹357.49 (-6.5%, charges ₹0.0549) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹40.88 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.33×, ladder rising; stop ₹535.37; charges ₹0.0965)
2025-12-01  SANSERA     BUY ₹23.51 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.0555)
2025-12-03  PSB         SELL ₹37.65 at stop ₹29.05 (-5.7%, charges ₹0.0836) — the cash goes back to work at the next Friday screen
2025-12-08  KIRLOSENG   BUY ₹37.65 at ₹1,130.00 (fresh Friday signal — BUY: 1.67× weekly, month 2.31×, ladder rising; stop ₹886.54; charges ₹0.0889)
2026-01-08  EUREKAFORB  SELL ₹36.10 at stop ₹589.10 (-11.3%, charges ₹0.0802) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹36.43 at stop ₹2,956.49 (-10.1%, charges ₹0.0809) — the cash goes back to work at the next Friday screen
2026-01-12  HINDCOPPER  BUY ₹32.47 at ₹532.00 (fresh Friday signal — BUY: surged 1.55× weekly on 2025-12-12 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹456.95; charges ₹0.0766)
2026-01-12  KIRLOSENG   SELL ₹37.84 at stop ₹1,140.95 (+1.0%, charges ₹0.0840) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹40.06 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.0946)
2026-01-19  RBA         BUY ₹37.84 at ₹67.50 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.51×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.0893)
2026-01-20  LGBBROSLTD  SELL ₹48.81 at stop ₹1,713.80 (+21.4%, charges ₹0.1084) — the cash goes back to work at the next Friday screen
2026-01-20  UPL         SELL ₹43.96 at stop ₹729.12 (+5.8%, charges ₹0.0977) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹38.48 at stop ₹748.60 (-8.5%, charges ₹0.0855) — the cash goes back to work at the next Friday screen
2026-01-21  LTF         SELL ₹37.56 at stop ₹281.77 (-7.3%, charges ₹0.0834) — the cash goes back to work at the next Friday screen
2026-01-23  RRKABEL     SELL ₹37.47 at stop ₹1,358.31 (-7.9%, charges ₹0.0832) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹22.37 at stop ₹1,672.76 (-4.4%, charges ₹0.0497) — the cash goes back to work at the next Friday screen
2026-02-02  HINDALCO    BUY ₹39.07 at ₹905.70 (fresh Friday signal — BUY: 1.78× weekly, month 1.30×, ladder rising; stop ₹849.30; charges ₹0.0922)
2026-02-02  MCX         BUY ₹38.89 at ₹2,212.70 (fresh Friday signal — BUY: 2.10× weekly, month 1.32×, ladder rising; stop ₹2,132.75; charges ₹0.0918)
2026-02-09  CEIGALL     BUY ₹39.55 at ₹297.00 (fresh Friday signal — BUY: 1.88× weekly, month 1.26×, ladder rising; stop ₹253.32; charges ₹0.0934)
2026-02-09  PTC         BUY ₹39.40 at ₹180.62 (fresh Friday signal — BUY: 1.52× weekly, month 1.21×, ladder rising; stop ₹156.89; charges ₹0.0930)
2026-02-16  E2E         BUY ₹33.49 at ₹2,464.00 (fresh Friday signal — BUY: surged 2.17× weekly on 2026-02-06 (month 1.26×), ladder rising NOW — promoted from the ladder watch; stop ₹2,223.00; charges ₹0.0790)
2026-02-16  TATASTEEL   BUY ₹38.27 at ₹201.00 (fresh Friday signal — BUY: 1.92× weekly, month 1.26×, ladder rising; stop ₹173.42; charges ₹0.0903)
2026-02-17  NATIONALUM  SELL ₹38.01 at stop ₹335.49 (-4.7%, charges ₹0.0844) — the cash goes back to work at the next Friday screen
2026-02-23  VESUVIUS    BUY ₹38.01 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.0897)
2026-03-04  CEIGALL     SELL ₹35.31 at stop ₹266.33 (-10.3%, charges ₹0.0784) — the cash goes back to work at the next Friday screen
2026-03-04  PTC         SELL ₹34.07 at stop ₹156.89 (-13.1%, charges ₹0.0757) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹40.10 at stop ₹251.43 (-1.1%, charges ₹0.0891) — the cash goes back to work at the next Friday screen
2026-03-09  SUNPHARMA   BUY ₹32.51 at ₹1,772.90 (fresh Friday signal — BUY: surged 1.86× weekly on 2026-02-06 (month 1.39×), ladder rising NOW — promoted from the ladder watch; stop ₹1,626.40; charges ₹0.0767)
2026-03-09  TATASTEEL   SELL ₹36.11 at stop ₹190.52 (-5.2%, charges ₹0.0802) — the cash goes back to work at the next Friday screen
2026-03-09  TORNTPOWER  BUY ₹36.86 at ₹1,451.00 (fresh Friday signal — BUY: surged 4.10× weekly on 2026-02-13 (month 1.21×), ladder rising NOW — promoted from the ladder watch; stop ₹1,315.84; charges ₹0.0870)
2026-03-12  HINDCOPPER  SELL ₹32.12 at stop ₹528.63 (-0.6%, charges ₹0.0713) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹34.08 at stop ₹61.08 (-9.5%, charges ₹0.0757) — the cash goes back to work at the next Friday screen
2026-03-16  ABB         BUY ₹36.59 at ₹6,400.00 (fresh Friday signal — BUY: 1.80× weekly, month 1.92×, ladder rising; stop ₹5,486.25; charges ₹0.0864)
2026-03-16  J&KBANK     BUY ₹36.53 at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.95×, ladder rising; stop ₹103.27; charges ₹0.0862)
2026-03-16  JBCHEPHARM  BUY ₹36.48 at ₹2,136.00 (fresh Friday signal — BUY: surged 1.57× weekly on 2026-02-27 (month 1.33×), ladder rising NOW — promoted from the ladder watch; stop ₹1,875.30; charges ₹0.0861)
2026-03-23  AETHER      BUY ₹32.80 at ₹1,149.80 (fresh Friday signal — BUY: 1.80× weekly, month 1.22×, ladder rising; stop ₹928.15; charges ₹0.0774)
2026-03-23  HINDALCO    SELL ₹37.04 at stop ₹862.65 (-4.8%, charges ₹0.0823) — the cash goes back to work at the next Friday screen
2026-03-23  J&KBANK     SELL ₹33.22 at stop ₹110.67 (-8.6%, charges ₹0.0738) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹32.83 at stop ₹464.31 (-13.2%, charges ₹0.0729) — the cash goes back to work at the next Friday screen
2026-03-30  INOXINDIA   BUY ₹34.53 at ₹1,185.00 (fresh Friday signal — BUY: 2.69× weekly, month 1.27×, ladder rising; stop ₹1,067.80; charges ₹0.0815)
2026-03-30  TORNTPOWER  SELL ₹33.28 at stop ₹1,315.84 (-9.3%, charges ₹0.0739) — the cash goes back to work at the next Friday screen
2026-03-30  VTL         BUY ₹34.49 at ₹520.95 (fresh Friday signal — BUY: surged 1.53× weekly on 2026-02-27 (month 2.21×), ladder rising NOW — promoted from the ladder watch; stop ₹485.45; charges ₹0.0814)
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹45.26 / LT ₹0.00)
2026-04-02  SUNPHARMA   SELL ₹30.14 at stop ₹1,651.01 (-6.9%, charges ₹0.0669) — the cash goes back to work at the next Friday screen
2026-04-06  AUROPHARMA  BUY ₹27.94 at ₹1,344.00 (fresh Friday signal — BUY: surged 1.58× weekly on 2026-03-13 (month 1.44×), ladder rising NOW — promoted from the ladder watch; stop ₹1,178.00; charges ₹0.0660)
2026-04-06  CHENNPETRO  BUY ₹34.76 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0821)
2026-04-06  THERMAX     BUY ₹34.79 at ₹3,295.80 (fresh Friday signal — ACCUMULATE: 2.18× weekly, month 1.22×, ladder rising; stop ₹2,897.50; charges ₹0.0821)
2026-05-13  INOXINDIA   SELL ₹39.80 at stop ₹1,372.18 (+15.8%, charges ₹0.0884) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹31.97 at stop ₹1,125.84 (-2.1%, charges ₹0.0710) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹38.95 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.0919)
2026-05-18  CAPLIPOINT  BUY ₹32.82 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.0775)
2026-06-05  E2E         SELL ₹31.53 at stop ₹2,330.72 (-5.4%, charges ₹0.0700) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹31.53 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0744)
2026-06-15  AUROPHARMA  SELL ₹29.04 at stop ₹1,403.53 (+4.4%, charges ₹0.0645) — the cash goes back to work at the next Friday screen
2026-06-22  GARFIBRES   BUY ₹29.04 at ₹796.00 (fresh Friday signal — BUY: 14.56× weekly, month 3.47×, ladder rising; stop ₹639.35; charges ₹0.0686)
2026-07-07  MCX         SELL ₹45.80 at stop ₹2,618.20 (+18.3%, charges ₹0.1017) — the cash goes back to work at the next Friday screen
2026-07-13  GANESHHOU   BUY ₹41.05 at ₹860.50 (fresh Friday signal — BUY: 9.80× weekly, month 2.00×, ladder rising; stop ₹712.60; charges ₹0.0969)
2026-07-29  THERMAX     SELL ₹45.25 at stop ₹4,306.64 (+30.7%, charges ₹0.1005) — the cash goes back to work at the next Friday screen
2026-07-31  VTL         SELL ₹39.07 at stop ₹592.80 (+13.8%, charges ₹0.0868) — the cash goes back to work at the next Friday screen
2026-08-03  BLUESTONE   BUY ₹40.78 at ₹823.40 (fresh Friday signal — ACCUMULATE: 5.63× weekly, month 9.43×, ladder rising; stop ₹664.75; charges ₹0.0963)
2026-08-03  TMB         BUY ₹40.81 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.0963)
2026-09-10  ALKYLAMINE  SELL ₹43.55 at stop ₹1,920.99 (+12.3%, charges ₹0.0967) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹40.74 at stop ₹7,158.25 (+11.8%, charges ₹0.0905) — the cash goes back to work at the next Friday screen
2026-09-15  SUNDRMFAST  BUY ₹41.98 at ₹1,277.30 (fresh Friday signal — BUY: 3.14× weekly, month 1.81×, ladder rising; stop ₹1,127.74; charges ₹0.0991)
2026-09-21  AVALON      BUY ₹41.78 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.0986)
```
