# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 1388 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹446.91** | **+26.04% a year** |
| The same system before costs and taxes | ₹576.16 | +31.09% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹288.59 | +17.80% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹446.91** (+26.04% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 432 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹21.67** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹75.37**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹49.80 | ₹0.00 | ₹9.9593 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹30.10 | ₹21.33 | ₹8.6855 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹75.12 | ₹71.50 | ₹23.9612 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹163.80 | ₹0.00 | ₹32.7597 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹58.84 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹34.38 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹11.01 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 148.03 | +48.0% | +48.7% | +70.1% |
| 2021 (2021-12-31) | 252.71 | +70.7% | +82.0% | +26.2% |
| 2022 (2022-12-30) | 345.53 | +36.7% | +41.1% | +4.3% |
| 2023 (2023-12-29) | 471.36 | +36.4% | +42.2% | +20.0% |
| 2024 (2024-12-27) | 441.54 | -6.3% | +4.5% | +9.6% |
| 2025 (2025-12-26) | 434.88 | -1.5% | -1.7% | +9.4% |
| 2026 (2026-09-22) | 446.91 | +2.8% | +3.4% | -10.4% |

## What it took to earn it

- **Maximum drawdown: -30.7%** (peak 2024-03-07 → trough 2026-04-02, on weekly closes).
- **203 closed trades**: 93 winners (46%), average winner +35.6%, average loser -10.7%.
- Best closed trade ANANDRATHI +224.7%; worst KIOCL -24.5%.
- Median holding period 70 days.
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
| 2020-11-27 | 124.43 | 0.00 | 10 |
| 2020-12-24 | 148.03 | 29.99 | 8 |
| 2021-01-29 | 160.26 | 21.03 | 9 |
| 2021-02-26 | 173.55 | 0.22 | 10 |
| 2021-03-26 | 167.59 | 35.16 | 8 |
| 2021-04-30 | 170.88 | 0.97 | 10 |
| 2021-05-28 | 193.35 | 0.97 | 10 |
| 2021-06-25 | 207.52 | 0.00 | 10 |
| 2021-07-30 | 244.84 | 0.00 | 10 |
| 2021-08-27 | 236.19 | 0.00 | 10 |
| 2021-09-24 | 252.04 | 25.49 | 9 |
| 2021-10-29 | 251.35 | 43.80 | 8 |
| 2021-11-26 | 260.07 | 45.93 | 8 |
| 2021-12-31 | 252.71 | 3.07 | 9 |
| 2022-01-28 | 253.58 | 54.50 | 7 |
| 2022-02-25 | 238.91 | 90.30 | 5 |
| 2022-03-25 | 265.59 | 21.81 | 8 |
| 2022-04-29 | 290.82 | 20.50 | 8 |
| 2022-05-27 | 293.92 | 0.00 | 9 |
| 2022-06-24 | 280.68 | 29.46 | 8 |
| 2022-07-29 | 310.24 | 1.34 | 9 |
| 2022-08-26 | 326.57 | 1.34 | 9 |
| 2022-09-30 | 307.29 | 30.80 | 8 |
| 2022-10-28 | 320.32 | 0.00 | 9 |
| 2022-11-25 | 352.50 | 15.82 | 8 |
| 2022-12-30 | 345.53 | 44.96 | 8 |
| 2023-01-27 | 339.60 | 43.32 | 8 |
| 2023-02-24 | 338.35 | 1.07 | 9 |
| 2023-03-31 | 330.78 | 128.08 | 6 |
| 2023-04-28 | 330.59 | 41.84 | 8 |
| 2023-05-26 | 338.48 | 36.48 | 8 |
| 2023-06-30 | 343.64 | 2.81 | 9 |
| 2023-07-28 | 357.26 | 9.42 | 9 |
| 2023-08-25 | 394.02 | 3.23 | 9 |
| 2023-09-29 | 412.36 | 0.00 | 9 |
| 2023-10-27 | 410.15 | 114.94 | 6 |
| 2023-11-24 | 453.83 | 5.27 | 9 |
| 2023-12-29 | 471.36 | 0.00 | 9 |
| 2024-01-25 | 496.13 | 23.37 | 9 |
| 2024-02-23 | 531.31 | 17.75 | 9 |
| 2024-03-28 | 497.24 | 108.89 | 8 |
| 2024-04-26 | 495.24 | 0.00 | 10 |
| 2024-05-31 | 487.18 | 87.42 | 8 |
| 2024-06-28 | 489.32 | 0.00 | 10 |
| 2024-07-26 | 493.47 | 108.34 | 8 |
| 2024-08-30 | 465.47 | 0.00 | 10 |
| 2024-09-27 | 457.95 | 0.00 | 10 |
| 2024-10-25 | 418.61 | 144.11 | 7 |
| 2024-11-29 | 467.58 | 0.00 | 11 |
| 2024-12-27 | 441.54 | 118.12 | 8 |
| 2025-01-31 | 425.31 | 146.22 | 6 |
| 2025-02-28 | 386.70 | 146.91 | 6 |
| 2025-03-27 | 429.65 | 15.75 | 9 |
| 2025-04-25 | 450.99 | 14.05 | 8 |
| 2025-05-30 | 453.71 | 60.69 | 7 |
| 2025-06-27 | 471.02 | 66.14 | 7 |
| 2025-07-25 | 457.86 | 66.12 | 7 |
| 2025-08-29 | 454.29 | 50.42 | 8 |
| 2025-09-26 | 421.45 | 127.54 | 7 |
| 2025-10-31 | 425.45 | 68.95 | 9 |
| 2025-11-28 | 436.55 | 101.36 | 8 |
| 2025-12-26 | 434.88 | 14.57 | 10 |
| 2026-01-30 | 434.12 | 206.83 | 5 |
| 2026-02-27 | 417.26 | 0.00 | 10 |
| 2026-03-27 | 383.11 | 72.50 | 8 |
| 2026-04-30 | 417.13 | 0.00 | 10 |
| 2026-05-29 | 437.94 | 0.00 | 10 |
| 2026-06-25 | 430.18 | 0.00 | 10 |
| 2026-07-31 | 426.04 | 79.57 | 8 |
| 2026-08-28 | 451.86 | 0.00 | 10 |
| 2026-09-22 | 446.91 | 5.75 | 10 |

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
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| SAKSOFT | 2020-09-21 | 391.45 | 2021-01-25 | 341.10 | -12.9% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| MTNL | 2020-12-28 | 14.10 | 2021-02-16 | 12.06 | -14.5% |
| JINDWORLD | 2020-11-09 | 50.00 | 2021-03-01 | 52.12 | +4.2% |
| RAMCOIND | 2020-11-09 | 199.00 | 2021-03-19 | 236.22 | +18.7% |
| APTECHT | 2021-02-01 | 178.45 | 2021-03-19 | 204.25 | +14.5% |
| MAHINDCIE | 2021-02-22 | 188.00 | 2021-03-19 | 158.46 | -15.7% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| GREENPANEL | 2020-11-09 | 86.40 | 2021-03-25 | 153.89 | +78.1% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| GFLLIMITED | 2021-03-22 | 93.00 | 2021-04-13 | 74.39 | -20.0% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| GDL | 2021-01-25 | 158.00 | 2021-09-20 | 266.00 | +68.4% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| NEOGEN | 2021-09-27 | 1,255.00 | 2021-10-25 | 1,142.85 | -8.9% |
| KKCL | 2021-11-01 | 1,227.00 | 2021-11-15 | 1,130.50 | -7.9% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-10-25 | 9,508.95 | 2021-11-26 | 10,070.05 | +5.9% |
| SHANKARA | 2021-03-30 | 413.00 | 2021-11-29 | 489.25 | +18.5% |
| SOMANYCERA | 2021-06-21 | 594.85 | 2021-11-29 | 755.11 | +26.9% |
| MAHLOG | 2021-01-25 | 495.85 | 2021-11-30 | 654.55 | +32.0% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| LTTS | 2020-10-19 | 1,745.00 | 2022-01-21 | 4,856.88 | +178.3% |
| TVTODAY | 2021-11-22 | 320.24 | 2022-01-24 | 311.68 | -2.7% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| DIAMONDYD | 2021-12-06 | 800.00 | 2022-01-31 | 817.00 | +2.1% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| TV18BRDCST | 2022-01-31 | 58.90 | 2022-02-22 | 58.38 | -0.9% |
| JSWISPL | 2022-01-24 | 37.50 | 2022-02-24 | 30.25 | -19.3% |
| CCL | 2022-02-07 | 503.55 | 2022-02-24 | 441.75 | -12.3% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| RCF | 2022-04-04 | 96.40 | 2022-05-04 | 93.15 | -3.4% |
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
| TIMETECHNO | 2022-05-16 | 91.25 | 2022-11-21 | 95.09 | +4.2% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| RVNL | 2022-10-17 | 36.85 | 2022-12-26 | 60.57 | +64.4% |
| KSL | 2022-12-26 | 330.10 | 2023-01-27 | 328.23 | -0.6% |
| GICRE | 2022-12-26 | 157.00 | 2023-02-01 | 167.72 | +6.8% |
| LSIL | 2023-01-30 | 23.20 | 2023-02-07 | 20.04 | -13.6% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| KABRAEXTRU | 2022-12-26 | 441.95 | 2023-03-14 | 506.92 | +14.7% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| CHOLAFIN | 2023-02-06 | 777.55 | 2023-03-24 | 727.37 | -6.5% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| CIGNITITEC | 2023-02-13 | 673.00 | 2023-03-29 | 705.14 | +4.8% |
| SONATSOFTW | 2023-03-27 | 413.70 | 2023-03-29 | 371.45 | -10.2% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| MUKANDLTD | 2023-01-02 | 136.70 | 2023-05-17 | 116.23 | -15.0% |
| GUJALKALI | 2023-05-02 | 688.15 | 2023-05-23 | 646.14 | -6.1% |
| ANURAS | 2023-03-20 | 755.90 | 2023-07-03 | 1,007.67 | +33.3% |
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
| DOLLAR | 2024-03-11 | 527.95 | 2024-03-13 | 461.65 | -12.6% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| OIL | 2023-12-26 | 251.27 | 2024-03-15 | 344.53 | +37.1% |
| ANANDRATHI | 2023-07-17 | 265.70 | 2024-03-27 | 862.65 | +224.7% |
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| DMART | 2024-04-01 | 4,570.00 | 2024-05-31 | 4,322.83 | -5.4% |
| SOLARINDS | 2024-03-18 | 8,900.05 | 2024-06-04 | 7,980.95 | -10.3% |
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
| ALKYLAMINE | 2024-09-23 | 2,432.85 | 2024-10-22 | 2,106.24 | -13.4% |
| HBLPOWER | 2024-07-22 | 585.00 | 2024-10-25 | 522.78 | -10.6% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| CIGNITITEC | 2024-10-28 | 1,515.00 | 2024-11-18 | 1,330.00 | -12.2% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| KIRLPNU | 2024-11-04 | 1,698.00 | 2024-12-23 | 1,596.00 | -6.0% |
| PRSMJOHNSN | 2024-09-16 | 214.51 | 2024-12-26 | 170.55 | -20.5% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| GARFIBRES | 2024-11-25 | 956.00 | 2025-01-09 | 829.35 | -13.2% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| GANECOS | 2024-10-14 | 2,103.85 | 2025-01-10 | 1,751.78 | -16.7% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| COFORGE | 2024-10-28 | 1,543.10 | 2025-01-13 | 1,801.20 | +16.7% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| ASHOKA | 2025-01-13 | 271.65 | 2025-01-24 | 262.67 | -3.3% |
| LLOYDSME | 2024-12-30 | 1,189.90 | 2025-01-28 | 1,258.75 | +5.8% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| GANESHHOUC | 2024-11-18 | 1,059.00 | 2025-02-28 | 1,090.38 | +3.0% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| GRWRHITECH | 2025-03-10 | 4,219.95 | 2025-04-03 | 3,602.82 | -14.6% |
| AVANTIFEED | 2025-03-17 | 842.55 | 2025-04-07 | 648.95 | -23.0% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| ITDCEM | 2024-10-07 | 655.05 | 2025-04-11 | 524.92 | -19.9% |
| HCG | 2025-01-20 | 504.95 | 2025-05-26 | 559.08 | +10.7% |
| COROMANDEL | 2025-04-07 | 1,870.00 | 2025-06-27 | 2,246.75 | +20.1% |
| TECHNOE | 2025-06-02 | 1,421.00 | 2025-07-24 | 1,467.84 | +3.3% |
| JSWHL | 2024-10-28 | 9,600.00 | 2025-08-04 | 19,106.01 | +99.0% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| ALKYLAMINE | 2025-06-30 | 2,263.00 | 2025-08-07 | 2,087.62 | -7.7% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| RSYSTEMS | 2025-09-01 | 460.00 | 2025-09-24 | 423.23 | -8.0% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| BOMDYEING | 2025-07-28 | 181.45 | 2025-09-25 | 172.67 | -4.8% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| BLACKBUCK | 2025-08-18 | 553.00 | 2025-10-28 | 642.20 | +16.1% |
| PGHL | 2025-08-11 | 6,345.00 | 2025-11-06 | 5,938.45 | -6.4% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| NETWEB | 2025-09-29 | 3,700.00 | 2025-11-06 | 3,515.95 | -5.0% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| FLUOROCHEM | 2025-09-22 | 3,820.00 | 2025-11-24 | 3,412.02 | -10.7% |
| TDPOWERSYS | 2025-11-03 | 382.27 | 2025-11-24 | 357.49 | -6.5% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| M&MFIN | 2025-11-03 | 316.55 | 2026-01-07 | 360.81 | +14.0% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| UPL | 2025-08-11 | 688.95 | 2026-01-20 | 729.12 | +5.8% |
| LGBBROSLTD | 2025-09-29 | 1,411.60 | 2026-01-20 | 1,713.80 | +21.4% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| LTF | 2025-11-10 | 304.00 | 2026-01-21 | 281.77 | -7.3% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| QPOWER | 2026-02-23 | 895.00 | 2026-03-02 | 803.80 | -10.2% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| HINDCOPPER | 2026-01-12 | 532.00 | 2026-03-12 | 528.63 | -0.6% |
| RBA | 2026-01-19 | 67.50 | 2026-03-12 | 61.08 | -9.5% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-16 | 121.14 | 2026-03-23 | 110.67 | -8.6% |
| MAHABANK | 2025-10-27 | 59.00 | 2026-03-30 | 61.05 | +3.5% |
| TORNTPOWER | 2026-02-23 | 1,540.00 | 2026-03-30 | 1,315.84 | -14.6% |
| SUNPHARMA | 2026-03-09 | 1,772.90 | 2026-04-02 | 1,651.01 | -6.9% |
| INOXINDIA | 2026-04-06 | 1,253.90 | 2026-05-13 | 1,372.18 | +9.4% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| E2E | 2026-02-23 | 2,914.00 | 2026-06-05 | 2,330.72 | -20.0% |
| AUROPHARMA | 2026-04-06 | 1,344.00 | 2026-06-15 | 1,403.53 | +4.4% |
| MCX | 2026-02-02 | 2,212.70 | 2026-07-07 | 2,618.20 | +18.3% |
| THERMAX | 2026-04-13 | 3,596.00 | 2026-07-29 | 4,306.64 | +19.8% |
| VTL | 2026-03-23 | 534.00 | 2026-07-31 | 592.80 | +11.0% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-02-23 | 6,090.00 | 2026-09-15 | 7,158.25 | +17.5% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_MONTH_1.3.csv` beside this report (21036 events in all).*

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
2020-11-09  BORORENEW   BUY ₹10.64 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.0126)
2020-11-09  GREENPANEL  BUY ₹11.87 at ₹86.40 (fresh Friday signal — BUY: 2.76× weekly, month 1.37×, ladder rising; stop ₹63.17; charges ₹0.0141)
2020-11-09  JINDWORLD   BUY ₹11.90 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.28× weekly, month 1.55×, ladder rising; stop ₹39.81; charges ₹0.0141)
2020-11-09  RAMCOIND    BUY ₹11.88 at ₹199.00 (fresh Friday signal — ACCUMULATE: 2.92× weekly, month 1.31×, ladder rising; stop ₹155.29; charges ₹0.0141)
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹12.36 at stop ₹234.75 (-3.0%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2020-12-28  MTNL        BUY ₹14.73 at ₹14.10 (fresh Friday signal — BUY: 9.97× weekly, month 4.77×, ladder rising; stop ₹8.26; charges ₹0.0175)
2020-12-28  PAISALO     BUY ₹15.26 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0181)
2021-01-20  BORORENEW   SELL ₹26.35 at stop ₹247.59 (+148.3%, charges ₹0.0273) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹15.98 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.79×, ladder rising; stop ₹92.41; charges ₹0.0189)
2021-01-25  MAHLOG      BUY ₹10.37 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹0.0123)
2021-01-25  SAKSOFT     SELL ₹6.83 at stop ₹341.10 (-12.9%, charges ₹0.0071) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹14.20 at stop ₹928.05 (+10.7%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹16.26 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.0193)
2021-02-16  MTNL        SELL ₹12.57 at stop ₹12.06 (-14.5%, charges ₹0.0130) — the cash goes back to work at the next Friday screen
2021-02-22  MAHINDCIE   BUY ₹17.12 at ₹188.00 (fresh Friday signal — BUY: 22.74× weekly, month 4.25×, ladder rising; stop ₹143.79; charges ₹0.0203)
2021-03-01  JINDWORLD   SELL ₹12.37 at stop ₹52.12 (+4.2%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2021-03-08  JSWENERGY   BUY ₹12.60 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.50×, ladder rising; stop ₹65.79; charges ₹0.0149)
2021-03-19  APTECHT     SELL ₹18.57 at stop ₹204.25 (+14.5%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2021-03-19  MAHINDCIE   SELL ₹14.40 at stop ₹158.46 (-15.7%, charges ₹0.0149) — the cash goes back to work at the next Friday screen
2021-03-19  RAMCOIND    SELL ₹14.07 at stop ₹236.22 (+18.7%, charges ₹0.0146) — the cash goes back to work at the next Friday screen
2021-03-22  GFLLIMITED  BUY ₹16.65 at ₹93.00 (fresh Friday signal — ACCUMULATE: 6.17× weekly, month 3.98×, ladder rising; stop ₹74.39; charges ₹0.0197)
2021-03-22  KEI         BUY ₹13.83 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.0164)
2021-03-22  VIDHIING    BUY ₹16.56 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0196)
2021-03-25  BANARISUG   SELL ₹14.07 at stop ₹1,586.36 (+13.4%, charges ₹0.0146) — the cash goes back to work at the next Friday screen
2021-03-25  GREENPANEL  SELL ₹21.09 at stop ₹153.89 (+78.1%, charges ₹0.0219) — the cash goes back to work at the next Friday screen
2021-03-30  ADANITRANS  BUY ₹16.93 at ₹896.00 (fresh Friday signal — BUY: 1.91× weekly, month 1.35×, ladder rising; stop ₹693.23; charges ₹0.0201)
2021-03-30  SHANKARA    BUY ₹16.90 at ₹413.00 (fresh Friday signal — ACCUMULATE: 1.99× weekly, month 1.30×, ladder rising; stop ₹354.55; charges ₹0.0200)
2021-04-01  ADANITRANS  TRIM 5.0% (₹0.95 at ₹999.20) to pay the tax bill
2021-04-01  GDL         TRIM 5.0% (₹0.90 at ₹177.90) to pay the tax bill
2021-04-01  GFLLIMITED  TRIM 5.0% (₹0.97 at ₹108.35) to pay the tax bill
2021-04-01  JSWENERGY   TRIM 5.0% (₹0.70 at ₹90.70) to pay the tax bill
2021-04-01  KEI         TRIM 5.0% (₹0.70 at ₹528.60) to pay the tax bill
2021-04-01  LTTS        TRIM 5.0% (₹0.99 at ₹2,720.60) to pay the tax bill
2021-04-01  MAHLOG      TRIM 5.0% (₹0.60 at ₹574.75) to pay the tax bill
2021-04-01  PAISALO     TRIM 5.0% (₹1.05 at ₹78.11) to pay the tax bill
2021-04-01  SHANKARA    TRIM 5.0% (₹0.87 at ₹425.05) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹9.9593 paid (STCG ₹49.80 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  VIDHIING    TRIM 5.0% (₹0.88 at ₹207.10) to pay the tax bill
2021-04-12  PAISALO     SELL ₹18.37 at stop ₹72.41 (+27.1%, charges ₹0.0191) — the cash goes back to work at the next Friday screen
2021-04-13  GFLLIMITED  SELL ₹12.62 at stop ₹74.39 (-20.0%, charges ₹0.0131) — the cash goes back to work at the next Friday screen
2021-04-19  KPRMILL     BUY ₹15.00 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0178)
2021-04-19  MOREPENLAB  BUY ₹15.02 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹0.0178)
2021-06-18  VIDHIING    SELL ₹14.72 at stop ₹182.64 (-6.2%, charges ₹0.0153) — the cash goes back to work at the next Friday screen
2021-06-21  SOMANYCERA  BUY ₹15.69 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0186)
2021-08-10  MOREPENLAB  SELL ₹22.54 at stop ₹56.33 (+50.4%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹22.36 at stop ₹352.48 (+49.4%, charges ₹0.0232) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹23.65 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.0280)
2021-08-16  TATAINVEST  BUY ₹21.25 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0252)
2021-09-20  GDL         SELL ₹25.49 at stop ₹266.00 (+68.4%, charges ₹0.0264) — the cash goes back to work at the next Friday screen
2021-09-27  NEOGEN      BUY ₹25.47 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0302)
2021-10-22  KEI         SELL ₹21.41 at stop ₹853.10 (+63.4%, charges ₹0.0222) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹20.65 at stop ₹3,220.59 (-12.5%, charges ₹0.0214) — the cash goes back to work at the next Friday screen
2021-10-25  NEOGEN      SELL ₹23.14 at stop ₹1,142.85 (-8.9%, charges ₹0.0240) — the cash goes back to work at the next Friday screen
2021-10-25  TTKPRESTIG  BUY ₹21.44 at ₹9,508.95 (fresh Friday signal — BUY: 6.63× weekly, month 1.31×, ladder rising; stop ₹8,326.75; charges ₹0.0254)
2021-11-01  KKCL        BUY ₹18.56 at ₹1,227.00 (fresh Friday signal — ACCUMULATE: 3.82× weekly, month 58.67×, ladder rising; stop ₹915.66; charges ₹0.0220)
2021-11-01  TCIEXP      BUY ₹25.24 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0299)
2021-11-15  KKCL        SELL ₹17.06 at stop ₹1,130.50 (-7.9%, charges ₹0.0177) — the cash goes back to work at the next Friday screen
2021-11-22  TVTODAY     BUY ₹17.06 at ₹320.24 (fresh Friday signal — BUY: 15.58× weekly, month 3.55×, ladder rising; stop ₹253.08; charges ₹0.0202)
2021-11-26  TATAINVEST  SELL ₹23.28 at stop ₹1,436.49 (+9.8%, charges ₹0.0242) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹22.65 at stop ₹10,070.05 (+5.9%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2021-11-29  RAYMOND     BUY ₹20.51 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0243)
2021-11-29  RSYSTEMS    BUY ₹25.43 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0301)
2021-11-29  SHANKARA    SELL ₹18.97 at stop ₹489.25 (+18.5%, charges ₹0.0197) — the cash goes back to work at the next Friday screen
2021-11-29  SOMANYCERA  SELL ₹19.87 at stop ₹755.11 (+26.9%, charges ₹0.0206) — the cash goes back to work at the next Friday screen
2021-11-30  MAHLOG      SELL ₹12.98 at stop ₹654.55 (+32.0%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹25.27 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0299)
2021-12-06  DIAMONDYD   BUY ₹25.21 at ₹800.00 (fresh Friday signal — BUY: 4.19× weekly, month 1.42×, ladder rising; stop ₹652.65; charges ₹0.0299)
2021-12-16  RSYSTEMS    SELL ₹22.74 at stop ₹291.18 (-10.4%, charges ₹0.0236) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹24.07 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0285)
2021-12-21  TCIEXP      SELL ₹28.05 at stop ₹2,039.74 (+11.4%, charges ₹0.0291) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹24.98 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0296)
2022-01-21  LTTS        SELL ₹33.25 at stop ₹4,856.88 (+178.3%, charges ₹0.0345) — the cash goes back to work at the next Friday screen
2022-01-24  JSWISPL     BUY ₹25.43 at ₹37.50 (fresh Friday signal — BUY: 5.58× weekly, month 4.04×, ladder rising; stop ₹27.79; charges ₹0.0301)
2022-01-24  TVTODAY     SELL ₹16.57 at stop ₹311.68 (-2.7%, charges ₹0.0172) — the cash goes back to work at the next Friday screen
2022-01-25  SWANENERGY  SELL ₹27.04 at stop ₹162.64 (+8.5%, charges ₹0.0280) — the cash goes back to work at the next Friday screen
2022-01-31  DIAMONDYD   SELL ₹25.69 at stop ₹817.00 (+2.1%, charges ₹0.0266) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹25.33 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0300)
2022-01-31  TV18BRDCST  BUY ₹25.31 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.0300)
2022-02-07  CCL         BUY ₹26.14 at ₹503.55 (fresh Friday signal — BUY: 4.07× weekly, month 1.58×, ladder rising; stop ₹408.60; charges ₹0.0310)
2022-02-11  SHARDACROP  SELL ₹23.49 at stop ₹545.30 (-7.1%, charges ₹0.0244) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹24.85 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0294)
2022-02-15  RAYMOND     SELL ₹23.32 at stop ₹679.35 (+14.0%, charges ₹0.0242) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹24.18 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0287)
2022-02-22  GREENLAM    SELL ₹20.72 at stop ₹313.67 (-13.7%, charges ₹0.0215) — the cash goes back to work at the next Friday screen
2022-02-22  TV18BRDCST  SELL ₹25.03 at stop ₹58.38 (-0.9%, charges ₹0.0260) — the cash goes back to work at the next Friday screen
2022-02-24  CCL         SELL ₹22.88 at stop ₹441.75 (-12.3%, charges ₹0.0237) — the cash goes back to work at the next Friday screen
2022-02-24  JSWISPL     SELL ₹20.47 at stop ₹30.25 (-19.3%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹24.34 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0288)
2022-02-28  SHANTIGEAR  BUY ₹24.45 at ₹185.30 (fresh Friday signal — BUY: surged 3.40× weekly on 2022-02-11 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹170.29; charges ₹0.0290)
2022-03-07  GTLINFRA    BUY ₹24.77 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0293)
2022-03-07  RAJMET      BUY ₹16.74 at ₹278.00 (fresh Friday signal — BUY: surged 6.93× weekly on 2022-02-18 (month 4.62×), ladder rising NOW — promoted from the ladder watch; stop ₹226.96; charges ₹0.0198)
2022-03-21  BSE         SELL ₹21.81 at stop ₹1,634.39 (-13.5%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹8.6855 paid (STCG ₹30.10 @20%, LTCG ₹21.33 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  RCF         BUY ₹13.12 at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.0155)
2022-04-29  GTLINFRA    SELL ₹20.50 at stop ₹1.41 (-17.1%, charges ₹0.0213) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹20.50 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.0243)
2022-05-04  RCF         SELL ₹12.65 at stop ₹93.15 (-3.4%, charges ₹0.0131) — the cash goes back to work at the next Friday screen
2022-05-11  ADANITRANS  SELL ₹41.17 at stop ₹2,299.37 (+156.6%, charges ₹0.0427) — the cash goes back to work at the next Friday screen
2022-05-11  MFL         SELL ₹17.53 at stop ₹1,225.50 (-14.3%, charges ₹0.0182) — the cash goes back to work at the next Friday screen
2022-05-16  KRISHANA    BUY ₹28.07 at ₹67.96 (fresh Friday signal — ACCUMULATE: 1.67× weekly, month 1.86×, ladder rising; stop ₹54.77; charges ₹0.0333)
2022-05-16  TIMETECHNO  BUY ₹15.21 at ₹91.25 (fresh Friday signal — BUY: surged 5.09× weekly on 2022-04-22 (month 3.01×), ladder rising NOW — promoted from the ladder watch; stop ₹86.50; charges ₹0.0180)
2022-05-16  VBL         BUY ₹28.06 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0332)
2022-06-06  VBL         SELL ₹24.98 at stop ₹196.27 (-10.8%, charges ₹0.0259) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹24.98 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0296)
2022-06-16  KRISHANA    SELL ₹22.57 at stop ₹54.77 (-19.4%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹22.57 at ₹950.15 (fresh Friday signal — BUY: surged 6.84× weekly on 2022-06-10 (month 1.49×), ladder rising NOW — promoted from the ladder watch; stop ₹706.80; charges ₹0.0267)
2022-06-20  JSWENERGY   SELL ₹29.46 at stop ₹201.99 (+146.8%, charges ₹0.0306) — the cash goes back to work at the next Friday screen
2022-06-27  INSECTICID  BUY ₹28.12 at ₹844.00 (fresh Friday signal — BUY: 1.82× weekly, month 1.31×, ladder rising; stop ₹712.50; charges ₹0.0333)
2022-09-06  DANGEE      SELL ₹38.77 at stop ₹375.25 (+59.7%, charges ₹0.0402) — the cash goes back to work at the next Friday screen
2022-09-12  SHREECEM    BUY ₹32.21 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0382)
2022-09-15  RAJMET      SELL ₹21.59 at stop ₹359.30 (+29.2%, charges ₹0.0224) — the cash goes back to work at the next Friday screen
2022-09-19  JSWHL       BUY ₹29.50 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0350)
2022-09-29  INSECTICID  SELL ₹30.80 at stop ₹926.73 (+9.8%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2022-10-03  SUNDARMHLD  BUY ₹30.51 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹0.0362)
2022-10-11  SUNDARMHLD  SELL ₹27.12 at stop ₹92.20 (-10.9%, charges ₹0.0281) — the cash goes back to work at the next Friday screen
2022-10-17  RVNL        BUY ₹27.41 at ₹36.85 (fresh Friday signal — BUY: 4.04× weekly, month 1.42×, ladder rising; stop ₹31.21; charges ₹0.0325)
2022-11-03  APARINDS    SELL ₹32.20 at stop ₹1,358.50 (+43.0%, charges ₹0.0334) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹32.20 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0382)
2022-11-21  TIMETECHNO  SELL ₹15.82 at stop ₹95.09 (+4.2%, charges ₹0.0164) — the cash goes back to work at the next Friday screen
2022-12-21  ELECON      SELL ₹41.21 at stop ₹202.49 (+65.3%, charges ₹0.0427) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹45.50 at stop ₹345.56 (+86.5%, charges ₹0.0472) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹32.09 at stop ₹139.84 (-0.1%, charges ₹0.0333) — the cash goes back to work at the next Friday screen
2022-12-26  GICRE       BUY ₹33.74 at ₹157.00 (fresh Friday signal — BUY: surged 4.73× weekly on 2022-12-02 (month 1.82×), ladder rising NOW — promoted from the ladder watch; stop ₹134.14; charges ₹0.0400)
2022-12-26  KABRAEXTRU  BUY ₹33.72 at ₹441.95 (fresh Friday signal — BUY: surged 4.67× weekly on 2022-11-25 (month 1.52×), ladder rising NOW — promoted from the ladder watch; stop ₹457.95; charges ₹0.0400)
2022-12-26  KRISHANA    BUY ₹33.49 at ₹83.60 (fresh Friday signal — BUY: 3.70× weekly, month 2.29×, ladder rising; stop ₹75.36; charges ₹0.0397)
2022-12-26  KSL         BUY ₹33.66 at ₹330.10 (fresh Friday signal — BUY: surged 5.50× weekly on 2022-12-09 (month 2.50×), ladder rising NOW — promoted from the ladder watch; stop ₹328.23; charges ₹0.0399)
2022-12-26  RVNL        SELL ₹44.96 at stop ₹60.57 (+64.4%, charges ₹0.0466) — the cash goes back to work at the next Friday screen
2023-01-02  MUKANDLTD   BUY ₹35.04 at ₹136.70 (fresh Friday signal — BUY: 6.81× weekly, month 2.54×, ladder rising; stop ₹103.76; charges ₹0.0415)
2023-01-27  KSL         SELL ₹33.40 at stop ₹328.23 (-0.6%, charges ₹0.0346) — the cash goes back to work at the next Friday screen
2023-01-30  LSIL        BUY ₹34.37 at ₹23.20 (fresh Friday signal — BUY: 2.28× weekly, month 3.56×, ladder rising; stop ₹11.29; charges ₹0.0407)
2023-02-01  GICRE       SELL ₹35.97 at stop ₹167.72 (+6.8%, charges ₹0.0373) — the cash goes back to work at the next Friday screen
2023-02-06  CHOLAFIN    BUY ₹33.65 at ₹777.55 (fresh Friday signal — BUY: 2.87× weekly, month 1.34×, ladder rising; stop ₹661.25; charges ₹0.0399)
2023-02-07  LSIL        SELL ₹29.62 at stop ₹20.04 (-13.6%, charges ₹0.0307) — the cash goes back to work at the next Friday screen
2023-02-13  CIGNITITEC  BUY ₹34.05 at ₹673.00 (fresh Friday signal — BUY: 3.13× weekly, month 1.41×, ladder rising; stop ₹568.10; charges ₹0.0403)
2023-02-17  CGCL        SELL ₹28.38 at stop ₹704.95 (+17.6%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2023-02-20  TIIL        BUY ₹34.14 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0404)
2023-03-14  KABRAEXTRU  SELL ₹38.59 at stop ₹506.92 (+14.7%, charges ₹0.0400) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹33.06 at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.57×, ladder rising; stop ₹691.46; charges ₹0.0392)
2023-03-20  KRISHANA    SELL ₹37.73 at stop ₹94.40 (+12.9%, charges ₹0.0391) — the cash goes back to work at the next Friday screen
2023-03-24  CHOLAFIN    SELL ₹31.41 at stop ₹727.37 (-6.5%, charges ₹0.0326) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹33.36 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.61×, ladder rising; stop ₹372.21; charges ₹0.0395)
2023-03-27  SONATSOFTW  BUY ₹33.30 at ₹413.70 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 4.94×, ladder rising; stop ₹371.45; charges ₹0.0395)
2023-03-29  CIGNITITEC  SELL ₹35.60 at stop ₹705.14 (+4.8%, charges ₹0.0369) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹53.57 at stop ₹112.36 (+116.1%, charges ₹0.0556) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹29.83 at stop ₹371.45 (-10.2%, charges ₹0.0309) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹31.09 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.0368)
2023-04-03  INGERRAND   BUY ₹31.03 at ₹2,690.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2023-03-10 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹2,170.84; charges ₹0.0368)
2023-04-03  NATCOPHARM  BUY ₹31.03 at ₹569.80 (fresh Friday signal — ACCUMULATE: 1.84× weekly, month 1.46×, ladder rising; stop ₹494.24; charges ₹0.0368)
2023-04-03  TAX         FY2023 settled: ₹23.9612 paid (STCG ₹75.12 @20%, LTCG ₹71.50 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-24  SHREECEM    SELL ₹30.88 at stop ₹23,636.00 (-3.9%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2023-05-02  GUJALKALI   BUY ₹32.83 at ₹688.15 (fresh Friday signal — BUY: 22.10× weekly, month 1.42×, ladder rising; stop ₹590.90; charges ₹0.0389)
2023-05-17  MUKANDLTD   SELL ₹29.72 at stop ₹116.23 (-15.0%, charges ₹0.0308) — the cash goes back to work at the next Friday screen
2023-05-22  SHARDAMOTR  BUY ₹33.01 at ₹380.00 (fresh Friday signal — BUY: 9.54× weekly, month 2.31×, ladder rising; stop ₹342.95; charges ₹0.0391)
2023-05-23  GUJALKALI   SELL ₹30.76 at stop ₹646.14 (-6.1%, charges ₹0.0319) — the cash goes back to work at the next Friday screen
2023-05-29  THANGAMAYL  BUY ₹33.67 at ₹1,344.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.50×, ladder rising; stop ₹1,116.30; charges ₹0.0399)
2023-07-03  ANURAS      SELL ₹43.97 at stop ₹1,007.67 (+33.3%, charges ₹0.0456) — the cash goes back to work at the next Friday screen
2023-07-10  GENUSPOWER  BUY ₹34.61 at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.48×, ladder rising; stop ₹99.51; charges ₹0.0410)
2023-07-12  KSB         SELL ₹32.47 at stop ₹407.74 (-2.4%, charges ₹0.0337) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹33.61 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0398)
2023-07-17  THANGAMAYL  SELL ₹33.60 at stop ₹1,344.25 (+0.0%, charges ₹0.0349) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹35.21 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.84×, ladder rising; stop ₹359.10; charges ₹0.0417)
2023-08-14  GANESHHOUC  SELL ₹32.18 at stop ₹418.62 (-8.4%, charges ₹0.0334) — the cash goes back to work at the next Friday screen
2023-08-21  ASTRAZEN    BUY ₹38.37 at ₹4,099.85 (fresh Friday signal — BUY: 6.03× weekly, month 2.40×, ladder rising; stop ₹3,562.50; charges ₹0.0455)
2023-09-13  INGERRAND   SELL ₹34.80 at stop ₹3,022.99 (+12.4%, charges ₹0.0361) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹38.03 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.67×, ladder rising; stop ₹58.28; charges ₹0.0451)
2023-10-23  SJVN        SELL ₹33.25 at stop ₹66.03 (-12.4%, charges ₹0.0345) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹41.38 at stop ₹1,840.70 (+33.4%, charges ₹0.0429) — the cash goes back to work at the next Friday screen
2023-10-25  SHARDAMOTR  SELL ₹40.31 at stop ₹465.07 (+22.4%, charges ₹0.0418) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹33.05 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0392)
2023-10-30  KKCL        BUY ₹40.96 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0485)
2023-10-30  SHAREINDIA  BUY ₹40.93 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0485)
2023-11-01  NATCOPHARM  SELL ₹41.92 at stop ₹771.40 (+35.4%, charges ₹0.0435) — the cash goes back to work at the next Friday screen
2023-11-06  SUNDARMHLD  BUY ₹41.92 at ₹144.75 (fresh Friday signal — BUY: 3.35× weekly, month 1.95×, ladder rising; stop ₹109.72; charges ₹0.0497)
2023-11-16  GENUSPOWER  SELL ₹49.63 at stop ₹234.03 (+43.7%, charges ₹0.0515) — the cash goes back to work at the next Friday screen
2023-11-20  ISMTLTD     BUY ₹44.36 at ₹94.60 (fresh Friday signal — BUY: 5.37× weekly, month 1.93×, ladder rising; stop ₹80.18; charges ₹0.0526)
2023-12-20  ISMTLTD     SELL ₹41.34 at stop ₹88.35 (-6.6%, charges ₹0.0429) — the cash goes back to work at the next Friday screen
2023-12-20  SUNDARMHLD  SELL ₹42.01 at stop ₹145.40 (+0.4%, charges ₹0.0436) — the cash goes back to work at the next Friday screen
2023-12-26  MMFL        BUY ₹47.54 at ₹1,023.60 (fresh Friday signal — BUY: 9.43× weekly, month 3.43×, ladder rising; stop ₹821.80; charges ₹0.0563)
2023-12-26  OIL         BUY ₹41.08 at ₹251.27 (fresh Friday signal — BUY: 6.09× weekly, month 3.92×, ladder rising; stop ₹186.55; charges ₹0.0487)
2024-01-17  TIIL        SELL ₹71.28 at stop ₹2,337.00 (+109.3%, charges ₹0.0739) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹47.91 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0568)
2024-01-30  MMFL        SELL ₹42.27 at stop ₹912.05 (-10.9%, charges ₹0.0438) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹52.10 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0617)
2024-02-09  ASTRAZEN    SELL ₹54.12 at stop ₹5,795.95 (+41.4%, charges ₹0.0561) — the cash goes back to work at the next Friday screen
2024-02-12  IOB         BUY ₹49.92 at ₹71.50 (fresh Friday signal — BUY: 7.81× weekly, month 2.91×, ladder rising; stop ₹38.71; charges ₹0.0591)
2024-03-06  SHAREINDIA  SELL ₹48.63 at stop ₹357.20 (+19.1%, charges ₹0.0504) — the cash goes back to work at the next Friday screen
2024-03-11  DOLLAR      BUY ₹53.20 at ₹527.95 (fresh Friday signal — BUY: 4.55× weekly, month 2.48×, ladder rising; stop ₹461.65; charges ₹0.0630)
2024-03-11  TCI         SELL ₹41.60 at stop ₹790.40 (-20.0%, charges ₹0.0432) — the cash goes back to work at the next Friday screen
2024-03-13  DOLLAR      SELL ₹46.41 at stop ₹461.65 (-12.6%, charges ₹0.0481) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹36.17 at stop ₹674.12 (-11.5%, charges ₹0.0375) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹48.03 at stop ₹666.47 (+0.5%, charges ₹0.0498) — the cash goes back to work at the next Friday screen
2024-03-15  OIL         SELL ₹56.20 at stop ₹344.53 (+37.1%, charges ₹0.0583) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹46.01 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.0545)
2024-03-18  FORCEMOT    BUY ₹48.76 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.0578)
2024-03-18  INDIGO      BUY ₹48.89 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0579)
2024-03-18  SOLARINDS   BUY ₹48.96 at ₹8,900.05 (fresh Friday signal — BUY: 4.28× weekly, month 2.84×, ladder rising; stop ₹5,332.29; charges ₹0.0580)
2024-03-18  TRENT       BUY ₹48.98 at ₹2,709.27 (fresh Friday signal — ACCUMULATE: 1.86× weekly, month 1.33×, ladder rising; stop ₹2,395.27; charges ₹0.0580)
2024-03-27  ANANDRATHI  SELL ₹108.89 at stop ₹862.65 (+224.7%, charges ₹0.1129) — the cash goes back to work at the next Friday screen
2024-04-01  DMART       BUY ₹29.18 at ₹4,570.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.56×, ladder rising; stop ₹3,695.50; charges ₹0.0346)
2024-04-01  SHRIRAMFIN  BUY ₹46.95 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0556)
2024-04-01  TAX         FY2024 settled: ₹32.7597 paid (STCG ₹163.80 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-13  JSWHL       SELL ₹39.33 at stop ₹6,280.45 (+33.6%, charges ₹0.0408) — the cash goes back to work at the next Friday screen
2024-05-21  KIRLOSBROS  BUY ₹39.33 at ₹1,844.00 (fresh Friday signal — BUY: 5.41× weekly, month 1.62×, ladder rising; stop ₹1,221.51; charges ₹0.0466)
2024-05-28  FORCEMOT    SELL ₹59.88 at stop ₹8,083.64 (+23.1%, charges ₹0.0621) — the cash goes back to work at the next Friday screen
2024-05-31  DMART       SELL ₹27.54 at stop ₹4,322.83 (-5.4%, charges ₹0.0286) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹49.94 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0592)
2024-06-03  THERMAX     BUY ₹37.48 at ₹5,640.00 (fresh Friday signal — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹0.0444)
2024-06-04  BOSCHLTD    SELL ₹45.15 at stop ₹29,015.09 (-1.6%, charges ₹0.0468) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹43.64 at stop ₹441.77 (-6.8%, charges ₹0.0453) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹43.80 at stop ₹7,980.95 (-10.3%, charges ₹0.0454) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹48.08 at ₹783.00 (fresh Friday signal — BUY: 7.38× weekly, month 1.40×, ladder rising; stop ₹632.75; charges ₹0.0570)
2024-06-10  FIEMIND     BUY ₹48.23 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0571)
2024-06-10  UNOMINDA    BUY ₹36.28 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0430)
2024-07-19  UNOMINDA    SELL ₹36.65 at stop ₹981.87 (+1.2%, charges ₹0.0380) — the cash goes back to work at the next Friday screen
2024-07-22  HBLPOWER    BUY ₹36.65 at ₹585.00 (fresh Friday signal — BUY: 3.57× weekly, month 1.41×, ladder rising; stop ₹522.78; charges ₹0.0434)
2024-07-22  TRENT       SELL ₹62.49 at stop ₹3,464.36 (+27.9%, charges ₹0.0648) — the cash goes back to work at the next Friday screen
2024-07-23  FIEMIND     SELL ₹45.85 at stop ₹1,257.56 (-4.7%, charges ₹0.0476) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹49.35 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0585)
2024-07-29  THYROCARE   BUY ₹49.39 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0585)
2024-08-05  KIRLOSBROS  SELL ₹42.30 at stop ₹1,987.46 (+7.8%, charges ₹0.0439) — the cash goes back to work at the next Friday screen
2024-08-05  THERMAX     SELL ₹31.29 at stop ₹4,719.70 (-16.3%, charges ₹0.0325) — the cash goes back to work at the next Friday screen
2024-08-12  ADANIPOWER  SELL ₹38.77 at stop ₹632.75 (-19.2%, charges ₹0.0402) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹47.73 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0566)
2024-08-12  CERA        BUY ₹35.46 at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹0.0420)
2024-08-16  CAMPUS      SELL ₹48.27 at stop ₹277.07 (-3.1%, charges ₹0.0501) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹46.66 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0553)
2024-08-19  VGUARD      BUY ₹40.39 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.0478)
2024-09-09  AVANTIFEED  SELL ₹45.88 at stop ₹650.13 (-6.8%, charges ₹0.0476) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹45.88 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0544)
2024-09-19  CERA        SELL ₹27.63 at stop ₹8,198.93 (-21.9%, charges ₹0.0287) — the cash goes back to work at the next Friday screen
2024-09-23  ALKYLAMINE  BUY ₹27.63 at ₹2,432.85 (fresh Friday signal — BUY: 9.32× weekly, month 3.52×, ladder rising; stop ₹2,106.24; charges ₹0.0327)
2024-10-03  IOB         SELL ₹39.41 at stop ₹56.57 (-20.9%, charges ₹0.0409) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹32.31 at stop ₹420.24 (-19.8%, charges ₹0.0335) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹44.26 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0524)
2024-10-07  INDIGO      SELL ₹68.37 at stop ₹4,485.14 (+40.2%, charges ₹0.0709) — the cash goes back to work at the next Friday screen
2024-10-07  ITDCEM      BUY ₹27.46 at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹0.0325)
2024-10-07  THYROCARE   SELL ₹49.98 at stop ₹796.15 (+1.4%, charges ₹0.0518) — the cash goes back to work at the next Friday screen
2024-10-14  DBCORP      BUY ₹44.67 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0529)
2024-10-14  GANECOS     BUY ₹44.50 at ₹2,103.85 (fresh Friday signal — BUY: 3.56× weekly, month 1.32×, ladder rising; stop ₹1,646.57; charges ₹0.0527)
2024-10-14  SKIPPER     BUY ₹29.18 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0346)
2024-10-22  ALKYLAMINE  SELL ₹23.86 at stop ₹2,106.24 (-13.4%, charges ₹0.0248) — the cash goes back to work at the next Friday screen
2024-10-22  BASF        SELL ₹49.32 at stop ₹7,611.30 (+3.6%, charges ₹0.0512) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹38.25 at stop ₹302.08 (-14.2%, charges ₹0.0397) — the cash goes back to work at the next Friday screen
2024-10-25  HBLPOWER    SELL ₹32.68 at stop ₹522.78 (-10.6%, charges ₹0.0339) — the cash goes back to work at the next Friday screen
2024-10-28  CIGNITITEC  BUY ₹37.37 at ₹1,515.00 (fresh Friday signal — BUY: 9.95× weekly, month 1.36×, ladder rising; stop ₹1,308.67; charges ₹0.0443)
2024-10-28  COFORGE     BUY ₹37.25 at ₹1,543.10 (fresh Friday signal — BUY: 3.74× weekly, month 1.36×, ladder rising; stop ₹1,274.91; charges ₹0.0441)
2024-10-28  CUPID       SELL ₹43.24 at stop ₹158.66 (+31.1%, charges ₹0.0449) — the cash goes back to work at the next Friday screen
2024-10-28  JSWHL       BUY ₹37.26 at ₹9,600.00 (fresh Friday signal — BUY: 3.86× weekly, month 1.32×, ladder rising; stop ₹7,629.63; charges ₹0.0441)
2024-11-04  AKZOINDIA   BUY ₹42.38 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.1000)
2024-11-04  KIRLPNU     BUY ₹33.09 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.0781)
2024-11-14  ASTRAZEN    SELL ₹40.62 at stop ₹6,854.77 (-7.9%, charges ₹0.0902) — the cash goes back to work at the next Friday screen
2024-11-18  CIGNITITEC  SELL ₹32.70 at stop ₹1,330.00 (-12.2%, charges ₹0.0726) — the cash goes back to work at the next Friday screen
2024-11-18  GANESHHOUC  BUY ₹40.62 at ₹1,059.00 (fresh Friday signal — BUY: surged 4.01× weekly on 2024-10-18 (month 1.75×), ladder rising NOW — promoted from the ladder watch; stop ₹867.10; charges ₹0.0959)
2024-11-25  GARFIBRES   BUY ₹32.70 at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹0.0772)
2024-12-17  SUPRIYA     SELL ₹63.16 at stop ₹717.25 (+35.8%, charges ₹0.1403) — the cash goes back to work at the next Friday screen
2024-12-23  KIRLPNU     SELL ₹30.96 at stop ₹1,596.00 (-6.0%, charges ₹0.0688) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹44.32 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.1046)
2024-12-26  PRSMJOHNSN  SELL ₹36.36 at stop ₹170.55 (-20.5%, charges ₹0.0808) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹31.96 at stop ₹3,423.18 (-24.2%, charges ₹0.0710) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹44.34 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.1047)
2024-12-30  KFINTECH    BUY ₹44.19 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.1043)
2024-12-30  LLOYDSME    BUY ₹29.58 at ₹1,189.90 (fresh Friday signal — BUY: surged 1.68× weekly on 2024-12-20 (month 1.50×), ladder rising NOW — promoted from the ladder watch; stop ₹1,064.09; charges ₹0.0698)
2025-01-09  GARFIBRES   SELL ₹28.23 at stop ₹829.35 (-13.2%, charges ₹0.0627) — the cash goes back to work at the next Friday screen
2025-01-09  KSL         SELL ₹39.21 at stop ₹1,059.30 (-11.1%, charges ₹0.0871) — the cash goes back to work at the next Friday screen
2025-01-10  GANECOS     SELL ₹36.93 at stop ₹1,751.78 (-16.7%, charges ₹0.0820) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹25.10 at stop ₹477.28 (-13.7%, charges ₹0.0558) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹41.55 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0981)
2025-01-13  ASHOKA      BUY ₹41.44 at ₹271.65 (fresh Friday signal — BUY: surged 1.88× weekly on 2024-12-13 (month 1.31×), ladder rising NOW — promoted from the ladder watch; stop ₹262.67; charges ₹0.0978)
2025-01-13  COFORGE     SELL ₹43.34 at stop ₹1,801.20 (+16.7%, charges ₹0.0963) — the cash goes back to work at the next Friday screen
2025-01-15  KFINTECH    SELL ₹33.73 at stop ₹1,159.14 (-23.3%, charges ₹0.0749) — the cash goes back to work at the next Friday screen
2025-01-20  HCG         BUY ₹42.32 at ₹504.95 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 1.41×, ladder rising; stop ₹429.63; charges ₹0.0999)
2025-01-24  AEGISLOG    SELL ₹34.71 at stop ₹700.36 (-16.1%, charges ₹0.0771) — the cash goes back to work at the next Friday screen
2025-01-24  ASHOKA      SELL ₹39.89 at stop ₹262.67 (-3.3%, charges ₹0.0886) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹40.76 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0962)
2025-01-28  LLOYDSME    SELL ₹31.15 at stop ₹1,258.75 (+5.8%, charges ₹0.0692) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹42.22 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.0997)
2025-02-12  JINDWORLD   SELL ₹40.51 at stop ₹374.11 (-8.2%, charges ₹0.0900) — the cash goes back to work at the next Friday screen
2025-02-24  GODFRYPHLP  BUY ₹39.24 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.0926)
2025-02-28  GANESHHOUC  SELL ₹41.64 at stop ₹1,090.38 (+3.0%, charges ₹0.0925) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹38.35 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0905)
2025-03-03  ZENSARTECH  SELL ₹32.30 at stop ₹727.84 (-23.1%, charges ₹0.0717) — the cash goes back to work at the next Friday screen
2025-03-10  GRWRHITECH  BUY ₹40.35 at ₹4,219.95 (fresh Friday signal — BUY: surged 2.69× weekly on 2025-02-14 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹3,504.00; charges ₹0.0952)
2025-03-17  AVANTIFEED  BUY ₹40.81 at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹0.0963)
2025-03-24  INDIASHLTR  BUY ₹43.95 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.1038)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹58.84 / LT ₹0.00)
2025-04-03  GRWRHITECH  SELL ₹34.29 at stop ₹3,602.82 (-14.6%, charges ₹0.0762) — the cash goes back to work at the next Friday screen
2025-04-07  AVANTIFEED  SELL ₹31.29 at stop ₹648.95 (-23.0%, charges ₹0.0695) — the cash goes back to work at the next Friday screen
2025-04-07  COROMANDEL  BUY ₹42.24 at ₹1,870.00 (fresh Friday signal — BUY: surged 1.58× weekly on 2025-03-21 (month 1.48×), ladder rising NOW — promoted from the ladder watch; stop ₹1,849.08; charges ₹0.0997)
2025-04-07  INDIASHLTR  SELL ₹40.66 at stop ₹738.82 (-7.1%, charges ₹0.0903) — the cash goes back to work at the next Friday screen
2025-04-11  ITDCEM      SELL ₹21.93 at stop ₹524.92 (-19.9%, charges ₹0.0487) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹43.73 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.1032)
2025-04-15  INDIASHLTR  BUY ₹43.90 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.1036)
2025-05-26  HCG         SELL ₹46.65 at stop ₹559.08 (+10.7%, charges ₹0.1036) — the cash goes back to work at the next Friday screen
2025-06-02  TECHNOE     BUY ₹45.07 at ₹1,421.00 (fresh Friday signal — BUY: 6.29× weekly, month 1.64×, ladder rising; stop ₹1,150.36; charges ₹0.1064)
2025-06-27  COROMANDEL  SELL ₹50.52 at stop ₹2,246.75 (+20.1%, charges ₹0.1122) — the cash goes back to work at the next Friday screen
2025-06-30  ALKYLAMINE  BUY ₹46.37 at ₹2,263.00 (fresh Friday signal — BUY: 7.48× weekly, month 1.62×, ladder rising; stop ₹1,832.27; charges ₹0.1095)
2025-07-24  TECHNOE     SELL ₹46.34 at stop ₹1,467.84 (+3.3%, charges ₹0.1029) — the cash goes back to work at the next Friday screen
2025-07-28  BOMDYEING   BUY ₹45.16 at ₹181.45 (fresh Friday signal — BUY: 21.87× weekly, month 4.30×, ladder rising; stop ₹148.64; charges ₹0.1066)
2025-08-04  JSWHL       SELL ₹73.90 at stop ₹19,106.01 (+99.0%, charges ₹0.1641) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹47.78 at stop ₹1,814.78 (+25.2%, charges ₹0.1061) — the cash goes back to work at the next Friday screen
2025-08-07  ALKYLAMINE  SELL ₹42.58 at stop ₹2,087.62 (-7.7%, charges ₹0.0946) — the cash goes back to work at the next Friday screen
2025-08-11  PGHL        BUY ₹43.27 at ₹6,345.00 (fresh Friday signal — BUY: 1.64× weekly, month 2.94×, ladder rising; stop ₹5,320.00; charges ₹0.1022)
2025-08-11  RAIN        BUY ₹43.32 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.1023)
2025-08-11  UPL         BUY ₹43.25 at ₹688.95 (fresh Friday signal — ACCUMULATE: 1.66× weekly, month 1.47×, ladder rising; stop ₹625.10; charges ₹0.1021)
2025-08-18  BLACKBUCK   BUY ₹43.59 at ₹553.00 (fresh Friday signal — ACCUMULATE: 3.19× weekly, month 4.96×, ladder rising; stop ₹473.20; charges ₹0.1029)
2025-08-26  RAIN        SELL ₹38.66 at stop ₹143.64 (-10.4%, charges ₹0.0859) — the cash goes back to work at the next Friday screen
2025-09-01  RSYSTEMS    BUY ₹44.97 at ₹460.00 (fresh Friday signal — BUY: surged 17.81× weekly on 2025-08-22 (month 4.67×), ladder rising NOW — promoted from the ladder watch; stop ₹394.44; charges ₹0.1062)
2025-09-16  GODFRYPHLP  SELL ₹60.60 at stop ₹8,967.50 (+55.1%, charges ₹0.1346) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹43.30 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.75× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.1022)
2025-09-22  FLUOROCHEM  BUY ₹22.74 at ₹3,820.00 (fresh Friday signal — BUY: 5.40× weekly, month 2.64×, ladder rising; stop ₹3,396.25; charges ₹0.0537)
2025-09-24  RSYSTEMS    SELL ₹41.19 at stop ₹423.23 (-8.0%, charges ₹0.0915) — the cash goes back to work at the next Friday screen
2025-09-25  BOMDYEING   SELL ₹42.78 at stop ₹172.67 (-4.8%, charges ₹0.0950) — the cash goes back to work at the next Friday screen
2025-09-25  INDIASHLTR  SELL ₹43.58 at stop ₹862.60 (-0.3%, charges ₹0.0968) — the cash goes back to work at the next Friday screen
2025-09-29  LGBBROSLTD  BUY ₹42.25 at ₹1,411.60 (fresh Friday signal — BUY: 3.53× weekly, month 1.72×, ladder rising; stop ₹1,258.75; charges ₹0.0997)
2025-09-29  NETWEB      BUY ₹42.13 at ₹3,700.00 (fresh Friday signal — BUY: 2.97× weekly, month 7.27×, ladder rising; stop ₹2,674.79; charges ₹0.0994)
2025-09-29  SUBROS      BUY ₹42.03 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0992)
2025-10-14  SUBROS      SELL ₹38.69 at stop ₹1,046.90 (-7.5%, charges ₹0.0859) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹39.83 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0940)
2025-10-20  CREDITACC   SELL ₹60.83 at stop ₹1,274.42 (+49.9%, charges ₹0.1351) — the cash goes back to work at the next Friday screen
2025-10-27  MAHABANK    BUY ₹42.27 at ₹59.00 (fresh Friday signal — ACCUMULATE: 1.84× weekly, month 1.48×, ladder rising; stop ₹53.69; charges ₹0.0998)
2025-10-28  BLACKBUCK   SELL ₹50.39 at stop ₹642.20 (+16.1%, charges ₹0.1119) — the cash goes back to work at the next Friday screen
2025-11-03  M&MFIN      BUY ₹25.97 at ₹316.55 (fresh Friday signal — BUY: 3.42× weekly, month 1.43×, ladder rising; stop ₹281.39; charges ₹0.0613)
2025-11-03  TDPOWERSYS  BUY ₹42.98 at ₹382.27 (fresh Friday signal — BUY: 4.87× weekly, month 1.95×, ladder rising; stop ₹276.78; charges ₹0.1015)
2025-11-06  FDC         SELL ₹37.49 at stop ₹425.79 (-13.0%, charges ₹0.0833) — the cash goes back to work at the next Friday screen
2025-11-06  NETWEB      SELL ₹39.85 at stop ₹3,515.95 (-5.0%, charges ₹0.0885) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹40.32 at stop ₹5,938.45 (-6.4%, charges ₹0.0895) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹42.94 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.1014)
2025-11-10  CUB         BUY ₹43.16 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.1019)
2025-11-10  LTF         BUY ₹31.55 at ₹304.00 (fresh Friday signal — BUY: 2.98× weekly, month 1.53×, ladder rising; stop ₹250.80; charges ₹0.0745)
2025-11-20  ANANDRATHI  SELL ₹36.52 at stop ₹1,450.17 (-7.9%, charges ₹0.0811) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹41.12 at stop ₹976.41 (-3.8%, charges ₹0.0913) — the cash goes back to work at the next Friday screen
2025-11-24  FLUOROCHEM  SELL ₹20.22 at stop ₹3,412.02 (-10.7%, charges ₹0.0449) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹36.52 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0862)
2025-11-24  TDPOWERSYS  SELL ₹40.01 at stop ₹357.49 (-6.5%, charges ₹0.0889) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹43.43 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.33×, ladder rising; stop ₹535.37; charges ₹0.1025)
2025-12-01  SANSERA     BUY ₹43.35 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.1023)
2026-01-07  M&MFIN      SELL ₹29.47 at stop ₹360.81 (+14.0%, charges ₹0.0655) — the cash goes back to work at the next Friday screen
2026-01-08  EUREKAFORB  SELL ₹38.36 at stop ₹589.10 (-11.3%, charges ₹0.0852) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹32.67 at stop ₹2,956.49 (-10.1%, charges ₹0.0726) — the cash goes back to work at the next Friday screen
2026-01-12  HINDCOPPER  BUY ₹42.99 at ₹532.00 (fresh Friday signal — BUY: surged 1.55× weekly on 2025-12-12 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹456.95; charges ₹0.1015)
2026-01-12  NATIONALUM  BUY ₹43.03 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.1016)
2026-01-19  RBA         BUY ₹29.05 at ₹67.50 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.51×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.0686)
2026-01-20  LGBBROSLTD  SELL ₹51.06 at stop ₹1,713.80 (+21.4%, charges ₹0.1134) — the cash goes back to work at the next Friday screen
2026-01-20  UPL         SELL ₹45.57 at stop ₹729.12 (+5.8%, charges ₹0.1012) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹39.84 at stop ₹748.60 (-8.5%, charges ₹0.0885) — the cash goes back to work at the next Friday screen
2026-01-21  LTF         SELL ₹29.11 at stop ₹281.77 (-7.3%, charges ₹0.0647) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹41.26 at stop ₹1,672.76 (-4.4%, charges ₹0.0916) — the cash goes back to work at the next Friday screen
2026-02-02  MCX         BUY ₹42.05 at ₹2,212.70 (fresh Friday signal — BUY: 2.10× weekly, month 1.32×, ladder rising; stop ₹2,132.75; charges ₹0.0993)
2026-02-17  NATIONALUM  SELL ₹40.82 at stop ₹335.49 (-4.7%, charges ₹0.0907) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹41.68 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.67×, ladder rising; stop ₹5,440.18; charges ₹0.0984)
2026-02-23  E2E         BUY ₹42.19 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0996)
2026-02-23  QPOWER      BUY ₹41.55 at ₹895.00 (fresh Friday signal — BUY: 2.56× weekly, month 1.40×, ladder rising; stop ₹719.96; charges ₹0.0981)
2026-02-23  TORNTPOWER  BUY ₹37.87 at ₹1,540.00 (fresh Friday signal — BUY: 1.78× weekly, month 1.47×, ladder rising; stop ₹1,315.84; charges ₹0.0894)
2026-02-23  VESUVIUS    BUY ₹42.31 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.0999)
2026-03-02  QPOWER      SELL ₹37.15 at stop ₹803.80 (-10.2%, charges ₹0.0825) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹42.49 at stop ₹251.43 (-1.1%, charges ₹0.0944) — the cash goes back to work at the next Friday screen
2026-03-09  SUNPHARMA   BUY ₹37.15 at ₹1,772.90 (fresh Friday signal — BUY: surged 1.86× weekly on 2026-02-06 (month 1.39×), ladder rising NOW — promoted from the ladder watch; stop ₹1,626.40; charges ₹0.0877)
2026-03-12  HINDCOPPER  SELL ₹42.53 at stop ₹528.63 (-0.6%, charges ₹0.0945) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹26.17 at stop ₹61.08 (-9.5%, charges ₹0.0581) — the cash goes back to work at the next Friday screen
2026-03-16  J&KBANK     BUY ₹39.54 at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.95×, ladder rising; stop ₹103.27; charges ₹0.0933)
2026-03-16  JBCHEPHARM  BUY ₹39.61 at ₹2,136.00 (fresh Friday signal — BUY: surged 1.57× weekly on 2026-02-27 (month 1.33×), ladder rising NOW — promoted from the ladder watch; stop ₹1,875.30; charges ₹0.0935)
2026-03-23  J&KBANK     SELL ₹35.96 at stop ₹110.67 (-8.6%, charges ₹0.0799) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹36.55 at stop ₹464.31 (-13.2%, charges ₹0.0812) — the cash goes back to work at the next Friday screen
2026-03-23  VTL         BUY ₹32.03 at ₹534.00 (fresh Friday signal — BUY: surged 1.53× weekly on 2026-02-27 (month 2.21×), ladder rising NOW — promoted from the ladder watch; stop ₹485.45; charges ₹0.0756)
2026-03-30  AETHER      BUY ₹37.76 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0891)
2026-03-30  MAHABANK    SELL ₹43.54 at stop ₹61.05 (+3.5%, charges ₹0.0967) — the cash goes back to work at the next Friday screen
2026-03-30  TORNTPOWER  SELL ₹32.21 at stop ₹1,315.84 (-14.6%, charges ₹0.0715) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹34.38 / LT ₹0.00)
2026-04-02  SUNPHARMA   SELL ₹34.43 at stop ₹1,651.01 (-6.9%, charges ₹0.0765) — the cash goes back to work at the next Friday screen
2026-04-06  AUROPHARMA  BUY ₹37.54 at ₹1,344.00 (fresh Friday signal — BUY: surged 1.58× weekly on 2026-03-13 (month 1.44×), ladder rising NOW — promoted from the ladder watch; stop ₹1,178.00; charges ₹0.0886)
2026-04-06  CHENNPETRO  BUY ₹37.58 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0887)
2026-04-06  INOXINDIA   BUY ₹37.70 at ₹1,253.90 (fresh Friday signal — BUY: 2.23× weekly, month 1.48×, ladder rising; stop ₹1,067.80; charges ₹0.0890)
2026-04-13  THERMAX     BUY ₹32.10 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.0758)
2026-05-13  INOXINDIA   SELL ₹41.06 at stop ₹1,372.18 (+9.4%, charges ₹0.0912) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹36.78 at stop ₹1,125.84 (-2.1%, charges ₹0.0817) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹41.56 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.0981)
2026-05-18  CAPLIPOINT  BUY ₹36.29 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.0857)
2026-06-05  E2E         SELL ₹33.59 at stop ₹2,330.72 (-20.0%, charges ₹0.0746) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹33.59 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0793)
2026-06-15  AUROPHARMA  SELL ₹39.03 at stop ₹1,403.53 (+4.4%, charges ₹0.0867) — the cash goes back to work at the next Friday screen
2026-06-22  GARFIBRES   BUY ₹39.03 at ₹796.00 (fresh Friday signal — BUY: 14.56× weekly, month 3.47×, ladder rising; stop ₹639.35; charges ₹0.0921)
2026-07-07  MCX         SELL ₹49.53 at stop ₹2,618.20 (+18.3%, charges ₹0.1100) — the cash goes back to work at the next Friday screen
2026-07-13  GANESHHOU   BUY ₹43.63 at ₹860.50 (fresh Friday signal — BUY: 9.80× weekly, month 2.00×, ladder rising; stop ₹712.60; charges ₹0.1030)
2026-07-29  THERMAX     SELL ₹38.27 at stop ₹4,306.64 (+19.8%, charges ₹0.0850) — the cash goes back to work at the next Friday screen
2026-07-31  VTL         SELL ₹35.40 at stop ₹592.80 (+11.0%, charges ₹0.0786) — the cash goes back to work at the next Friday screen
2026-08-03  BLUESTONE   BUY ₹35.96 at ₹823.40 (fresh Friday signal — ACCUMULATE: 5.63× weekly, month 9.43×, ladder rising; stop ₹664.75; charges ₹0.0849)
2026-08-03  TMB         BUY ₹43.61 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.1029)
2026-09-10  ALKYLAMINE  SELL ₹46.47 at stop ₹1,920.99 (+12.3%, charges ₹0.1032) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹48.76 at stop ₹7,158.25 (+17.5%, charges ₹0.1083) — the cash goes back to work at the next Friday screen
2026-09-15  SUNDRMFAST  BUY ₹44.84 at ₹1,277.30 (fresh Friday signal — BUY: 3.14× weekly, month 1.81×, ladder rising; stop ₹1,127.74; charges ₹0.1059)
2026-09-21  AVALON      BUY ₹44.65 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.1054)
```
