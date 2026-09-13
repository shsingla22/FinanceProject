# The Darvas screen, run for six years — 2020-06-01 → 2026-09-11

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-11, 741 symbols, fetched once into `2019-06-01_to_2026-09-13/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **Two limits that cannot be engineered away:** the universe is TODAY'S NiftyTotalMarket constituents (survivorship bias — companies that later failed or left the index are missing from the early years, which flatters results), and Yahoo serves split-adjusted history as it stands today. No costs, no slippage, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹788.82** | **+39.04% a year** |
| The same system before costs and taxes | ₹1,050.49 | +45.54% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹230.70 | +14.27% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹6.38 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹782.44** (+38.86% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.27 years, 328 weekly screens, 425 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹27.58** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹120.33**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹51.45 | ₹0.00 | ₹10.2909 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹84.66 | ₹0.00 | ₹16.9329 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹83.74 | ₹4.00 | ₹17.2485 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹251.30 | ₹0.00 | ₹50.2609 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹65.15 | ₹36.67 | ₹17.6142 | ₹0.00 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹39.90 | ₹0.00 | ₹7.9809 | ₹0.00 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹31.89 | ₹0.00 | ₹6.3789 | ₹0.00 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 149.03 | +49.0% | +49.8% | +35.6% |
| 2021 (2021-12-31) | 256.28 | +72.0% | +81.9% | +26.2% |
| 2022 (2022-12-30) | 316.25 | +23.4% | +31.5% | +4.3% |
| 2023 (2023-12-29) | 569.39 | +80.0% | +93.6% | +20.0% |
| 2024 (2024-12-27) | 661.71 | +16.2% | +19.2% | +9.6% |
| 2025 (2025-12-26) | 648.81 | -1.9% | +3.7% | +9.4% |
| 2026 (2026-09-11) | 788.82 | +21.6% | +22.5% | -10.2% |

## What it took to earn it

- **Maximum drawdown: -26.4%** (peak 2024-03-01 → trough 2025-04-11, on weekly closes).
- **205 closed trades**: 100 winners (49%), average winner +37.5%, average loser -10.6%.
- Best closed trade ANANDRATHI +224.7%; worst IOB -31.5%.
- Median holding period 70 days.
- Cash share of equity averaged 15% across all weeks (median 6%); the portfolio sat FULLY in cash for 1 of 328 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-06-26 | 104.31 | 0.61 | 10 |
| 2020-07-31 | 107.40 | 16.12 | 8 |
| 2020-08-28 | 119.98 | 5.09 | 9 |
| 2020-09-25 | 119.66 | 18.03 | 8 |
| 2020-10-30 | 125.57 | 18.56 | 8 |
| 2020-11-27 | 129.68 | 0.00 | 10 |
| 2020-12-24 | 149.03 | 27.09 | 8 |
| 2021-01-29 | 153.13 | 65.80 | 6 |
| 2021-02-26 | 164.84 | 59.42 | 6 |
| 2021-03-26 | 157.68 | 32.74 | 8 |
| 2021-04-30 | 160.88 | 20.36 | 8 |
| 2021-05-28 | 179.09 | 3.98 | 9 |
| 2021-06-25 | 195.71 | 8.55 | 9 |
| 2021-07-30 | 235.11 | 0.00 | 9 |
| 2021-08-27 | 225.77 | 59.51 | 7 |
| 2021-09-24 | 240.91 | 0.00 | 10 |
| 2021-10-29 | 238.34 | 35.25 | 8 |
| 2021-11-26 | 245.23 | 60.44 | 7 |
| 2021-12-31 | 256.28 | 23.98 | 9 |
| 2022-01-28 | 236.92 | 118.54 | 5 |
| 2022-02-25 | 222.22 | 130.41 | 4 |
| 2022-03-25 | 244.79 | 130.41 | 4 |
| 2022-04-29 | 261.86 | 0.00 | 9 |
| 2022-05-27 | 249.20 | 65.78 | 6 |
| 2022-06-24 | 245.76 | 16.85 | 8 |
| 2022-07-29 | 274.24 | 11.54 | 8 |
| 2022-08-26 | 293.42 | 75.31 | 6 |
| 2022-09-30 | 300.55 | 15.61 | 8 |
| 2022-10-28 | 299.16 | 12.17 | 9 |
| 2022-11-25 | 312.77 | 50.74 | 8 |
| 2022-12-30 | 316.25 | 205.06 | 3 |
| 2023-01-27 | 312.11 | 15.35 | 9 |
| 2023-02-24 | 307.72 | 53.30 | 8 |
| 2023-03-31 | 297.19 | 115.09 | 6 |
| 2023-04-28 | 299.95 | 67.11 | 7 |
| 2023-05-26 | 319.09 | 33.02 | 8 |
| 2023-06-30 | 355.41 | 0.00 | 9 |
| 2023-07-28 | 408.13 | 0.00 | 9 |
| 2023-08-25 | 411.51 | 2.32 | 9 |
| 2023-09-29 | 442.41 | 2.32 | 9 |
| 2023-10-27 | 445.22 | 168.77 | 6 |
| 2023-11-24 | 545.23 | 0.00 | 10 |
| 2023-12-29 | 569.39 | 0.00 | 10 |
| 2024-01-25 | 637.42 | 52.30 | 9 |
| 2024-02-23 | 721.84 | 40.69 | 9 |
| 2024-03-28 | 714.58 | 112.09 | 8 |
| 2024-04-26 | 691.03 | 0.00 | 9 |
| 2024-05-31 | 667.04 | 82.42 | 8 |
| 2024-06-28 | 655.80 | 0.00 | 10 |
| 2024-07-26 | 679.15 | 117.61 | 8 |
| 2024-08-30 | 719.51 | 0.00 | 10 |
| 2024-09-27 | 696.12 | 100.81 | 8 |
| 2024-10-25 | 624.52 | 263.91 | 6 |
| 2024-11-29 | 671.33 | 5.90 | 10 |
| 2024-12-27 | 661.71 | 177.07 | 7 |
| 2025-01-24 | 598.60 | 230.29 | 6 |
| 2025-02-28 | 561.04 | 444.88 | 2 |
| 2025-03-28 | 576.77 | 331.40 | 4 |
| 2025-04-25 | 567.84 | 250.79 | 5 |
| 2025-05-30 | 605.96 | 23.55 | 9 |
| 2025-06-27 | 655.25 | 23.55 | 9 |
| 2025-07-25 | 745.37 | 23.55 | 9 |
| 2025-08-29 | 745.56 | 66.25 | 8 |
| 2025-09-26 | 702.19 | 164.45 | 7 |
| 2025-10-31 | 672.46 | 240.16 | 7 |
| 2025-11-28 | 662.80 | 186.58 | 8 |
| 2025-12-26 | 648.81 | 2.02 | 11 |
| 2026-01-30 | 622.61 | 294.07 | 5 |
| 2026-02-27 | 620.86 | 281.83 | 5 |
| 2026-03-27 | 592.70 | 279.36 | 5 |
| 2026-04-24 | 620.65 | 30.65 | 9 |
| 2026-05-29 | 641.48 | 0.00 | 10 |
| 2026-06-26 | 665.71 | 0.00 | 10 |
| 2026-07-31 | 721.02 | 72.06 | 9 |
| 2026-08-28 | 750.33 | 0.00 | 10 |
| 2026-09-11 | 788.82 | 67.68 | 9 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| ABB | 2026-02-23 | 6,090.00 | 7,274.00 | 7,158.25 | +19.4% |
| AEGISLOG | 2026-06-15 | 954.95 | 1,353.60 | 1,086.67 | +41.7% |
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,754.90 | 2,376.52 | +38.4% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,572.90 | 1,242.60 | +59.0% |
| CRAFTSMAN | 2026-05-11 | 9,039.50 | 11,669.00 | 10,380.65 | +29.1% |
| DIACABS | 2026-05-18 | 196.45 | 369.05 | 291.41 | +87.9% |
| TMB | 2026-08-03 | 864.90 | 910.90 | 796.29 | +5.3% |
| VARROC | 2026-08-10 | 804.00 | 872.00 | 767.65 | +8.5% |
| WOCKPHARMA | 2026-05-11 | 1,613.90 | 2,179.40 | 1,741.63 | +35.0% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| IGL | 2020-06-08 | 247.75 | 2020-07-07 | 208.81 | -15.7% |
| RELAXO | 2020-06-08 | 759.45 | 2020-07-28 | 603.77 | -20.5% |
| LLOYDSENGG | 2020-06-08 | 0.87 | 2020-07-31 | 0.71 | -18.0% |
| EIDPARRY | 2020-06-08 | 219.00 | 2020-08-17 | 273.03 | +24.7% |
| GRANULES | 2020-06-15 | 216.75 | 2020-08-31 | 286.95 | +32.4% |
| ZENTEC | 2020-08-03 | 58.80 | 2020-08-31 | 80.56 | +37.0% |
| KIRLOSBROS | 2020-06-08 | 106.50 | 2020-09-08 | 120.79 | +13.4% |
| RCF | 2020-06-08 | 45.20 | 2020-09-09 | 45.84 | +1.4% |
| HAL | 2020-07-13 | 475.00 | 2020-09-22 | 390.57 | -17.8% |
| SCHAEFFLER | 2020-09-14 | 814.00 | 2020-09-23 | 724.67 | -11.0% |
| INDIAMART | 2020-09-07 | 2,124.50 | 2020-10-19 | 2,315.62 | +9.0% |
| CAPLIPOINT | 2020-06-15 | 383.80 | 2020-10-30 | 498.06 | +29.8% |
| GLAXO | 2020-09-14 | 1,675.00 | 2020-11-02 | 1,441.55 | -13.9% |
| ADVENZYMES | 2020-06-15 | 172.70 | 2020-11-03 | 292.33 | +69.3% |
| THYROCARE | 2020-08-24 | 263.35 | 2020-11-12 | 338.83 | +28.7% |
| ATGL | 2020-09-14 | 209.75 | 2020-12-21 | 332.60 | +58.6% |
| SYNGENE | 2020-06-08 | 373.90 | 2020-12-22 | 562.40 | +50.4% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| JUSTDIAL | 2020-10-26 | 584.00 | 2021-01-25 | 622.35 | +6.6% |
| PIIND | 2020-11-17 | 2,348.20 | 2021-01-25 | 2,107.67 | -10.2% |
| HFCL | 2020-11-23 | 18.20 | 2021-01-28 | 28.12 | +54.5% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| TRENT | 2020-11-17 | 755.00 | 2021-01-29 | 626.30 | -17.0% |
| TATAELXSI | 2021-01-25 | 2,608.00 | 2021-02-22 | 2,660.00 | +2.0% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| KPRMILL | 2020-11-02 | 151.00 | 2021-02-24 | 166.62 | +10.3% |
| ITC | 2021-02-08 | 228.69 | 2021-02-26 | 197.41 | -13.7% |
| INDIAMART | 2021-01-25 | 3,990.00 | 2021-03-02 | 4,137.25 | +3.7% |
| GRAVITA | 2020-12-28 | 69.65 | 2021-03-17 | 96.13 | +38.0% |
| RCF | 2021-03-01 | 80.00 | 2021-03-17 | 79.16 | -1.1% |
| UJJIVANSFB | 2021-02-08 | 37.15 | 2021-03-18 | 32.12 | -13.5% |
| MAHABANK | 2021-02-08 | 16.45 | 2021-03-19 | 18.37 | +11.7% |
| HONAUT | 2020-12-28 | 38,887.75 | 2021-03-22 | 41,911.15 | +7.8% |
| GESHIP | 2021-03-01 | 315.90 | 2021-04-12 | 290.70 | -8.0% |
| IOB | 2021-03-01 | 18.90 | 2021-04-28 | 14.82 | -21.6% |
| POLYMED | 2020-09-07 | 449.70 | 2021-06-14 | 950.00 | +111.3% |
| VAIBHAVGBL | 2021-03-01 | 708.00 | 2021-07-20 | 767.90 | +8.5% |
| WELSPUNLIV | 2021-03-22 | 81.45 | 2021-08-10 | 124.64 | +53.0% |
| MARKSANS | 2021-05-03 | 70.95 | 2021-08-10 | 77.14 | +8.7% |
| JSWENERGY | 2021-03-08 | 81.85 | 2021-08-11 | 228.00 | +178.6% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| JWL | 2021-06-21 | 30.80 | 2021-08-23 | 30.42 | -1.2% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| TDPOWERSYS | 2021-09-06 | 32.80 | 2021-10-22 | 30.53 | -6.9% |
| HAL | 2021-09-06 | 705.00 | 2021-10-28 | 636.50 | -9.7% |
| DEEPAKFERT | 2021-03-22 | 237.00 | 2021-11-11 | 385.70 | +62.7% |
| GRAVITA | 2021-08-23 | 188.60 | 2021-11-22 | 197.03 | +4.5% |
| TATAINVEST | 2021-08-16 | 130.81 | 2021-11-26 | 143.65 | +9.8% |
| NHPC | 2021-09-06 | 27.90 | 2021-11-29 | 30.11 | +7.9% |
| MPHASIS | 2021-07-26 | 2,512.00 | 2021-11-30 | 2,912.57 | +15.9% |
| KPITTECH | 2021-03-30 | 182.00 | 2021-12-20 | 458.85 | +152.1% |
| UNOMINDA | 2021-12-27 | 590.00 | 2022-01-07 | 544.21 | -7.8% |
| LTM | 2021-10-25 | 6,555.00 | 2022-01-24 | 6,270.00 | -4.3% |
| PERSISTENT | 2021-11-01 | 1,977.15 | 2022-01-24 | 2,067.34 | +4.6% |
| PGEL | 2022-01-03 | 80.99 | 2022-01-24 | 72.44 | -10.6% |
| GOKULAGRO | 2021-11-15 | 31.05 | 2022-01-25 | 35.00 | +12.7% |
| AFFLE | 2022-01-10 | 1,307.00 | 2022-01-25 | 1,206.50 | -7.7% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| GABRIEL | 2021-08-16 | 149.30 | 2022-02-14 | 125.40 | -16.0% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| CHAMBLFERT | 2021-12-06 | 407.45 | 2022-02-24 | 353.85 | -13.2% |
| CCL | 2022-02-07 | 503.55 | 2022-02-24 | 441.75 | -12.3% |
| ESCORTS | 2021-11-29 | 1,875.00 | 2022-02-25 | 1,754.65 | -6.4% |
| RCF | 2022-04-04 | 96.40 | 2022-05-04 | 93.15 | -3.4% |
| GNFC | 2022-02-14 | 553.00 | 2022-05-06 | 792.16 | +43.2% |
| BSE | 2021-12-06 | 209.99 | 2022-05-10 | 255.87 | +21.8% |
| MINDACORP | 2022-04-11 | 230.05 | 2022-05-11 | 186.63 | -18.9% |
| LTFOODS | 2022-04-18 | 91.70 | 2022-05-11 | 73.86 | -19.5% |
| SPLPETRO | 2022-04-04 | 475.00 | 2022-05-24 | 424.27 | -10.7% |
| MRPL | 2022-05-09 | 78.00 | 2022-07-06 | 69.61 | -10.8% |
| VBL | 2022-05-16 | 146.67 | 2022-08-22 | 188.52 | +28.5% |
| BLS | 2022-04-11 | 82.50 | 2022-08-23 | 110.67 | +34.1% |
| HOMEFIRST | 2022-08-29 | 944.95 | 2022-09-14 | 849.35 | -10.1% |
| SIEMENS | 2022-08-29 | 1,688.21 | 2022-09-26 | 1,618.44 | -4.1% |
| TSFINV | 2022-10-03 | 103.50 | 2022-10-11 | 92.20 | -10.9% |
| ADANIPOWER | 2022-02-21 | 26.40 | 2022-10-14 | 66.80 | +153.0% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| KALYANKJIL | 2022-08-29 | 78.10 | 2022-11-22 | 94.53 | +21.0% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| MAHSCOOTER | 2022-09-19 | 5,103.50 | 2022-12-22 | 4,617.00 | -9.5% |
| ACC | 2022-05-23 | 2,260.00 | 2022-12-23 | 2,465.15 | +9.1% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| IRFC | 2022-11-28 | 32.00 | 2022-12-23 | 28.20 | -11.9% |
| APOLLO | 2022-10-17 | 24.00 | 2022-12-26 | 24.42 | +1.8% |
| GODFRYPHLP | 2022-10-24 | 483.67 | 2022-12-26 | 547.85 | +13.3% |
| TIINDIA | 2022-07-25 | 2,135.00 | 2023-01-11 | 2,598.35 | +21.7% |
| GICRE | 2023-01-02 | 179.20 | 2023-02-01 | 167.72 | -6.4% |
| LLOYDSENGG | 2023-01-02 | 15.63 | 2023-02-07 | 19.27 | +23.3% |
| CGCL | 2022-02-21 | 567.08 | 2023-03-08 | 666.82 | +17.6% |
| ANUP | 2023-01-16 | 476.12 | 2023-03-10 | 527.27 | +10.7% |
| YESBANK | 2023-01-02 | 20.85 | 2023-03-13 | 15.34 | -26.4% |
| IOB | 2023-01-02 | 32.40 | 2023-03-20 | 22.18 | -31.5% |
| UCOBANK | 2022-11-28 | 21.05 | 2023-03-27 | 23.46 | +11.4% |
| JINDALSAW | 2023-02-06 | 65.22 | 2023-03-27 | 67.92 | +4.1% |
| SONATSOFTW | 2023-02-27 | 360.00 | 2023-03-29 | 371.45 | +3.2% |
| JSL | 2023-01-02 | 241.00 | 2023-04-13 | 256.98 | +6.6% |
| CERA | 2023-02-27 | 6,150.00 | 2023-04-26 | 6,037.30 | -1.8% |
| KIRLOSBROS | 2023-04-10 | 425.00 | 2023-04-26 | 403.85 | -5.0% |
| MARKSANS | 2023-04-24 | 78.00 | 2023-05-22 | 71.87 | -7.9% |
| GSFC | 2023-01-02 | 140.70 | 2023-05-29 | 155.85 | +10.8% |
| ASHAPURMIN | 2023-05-02 | 143.10 | 2023-05-29 | 134.24 | -6.2% |
| ANURAS | 2023-03-20 | 755.90 | 2023-07-03 | 1,007.67 | +33.3% |
| KSB | 2023-03-27 | 417.98 | 2023-07-12 | 407.74 | -2.4% |
| REFEX | 2023-05-02 | 65.32 | 2023-08-11 | 121.69 | +86.3% |
| EPL | 2023-06-05 | 201.90 | 2023-08-11 | 200.50 | -0.7% |
| CEATLTD | 2023-07-10 | 2,408.00 | 2023-08-14 | 2,244.85 | -6.8% |
| FORCEMOT | 2023-06-05 | 1,951.00 | 2023-10-20 | 3,709.99 | +90.2% |
| THANGAMAYL | 2023-05-29 | 672.00 | 2023-10-23 | 1,368.00 | +103.6% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| VARROC | 2023-08-14 | 385.40 | 2023-10-25 | 450.92 | +17.0% |
| TSFINV | 2023-11-06 | 144.75 | 2023-12-20 | 145.40 | +0.4% |
| ANGELONE | 2023-10-30 | 253.50 | 2024-01-23 | 296.88 | +17.1% |
| ZFCVINDIA | 2023-04-24 | 1,697.50 | 2024-02-02 | 2,473.96 | +45.7% |
| APOLLO | 2023-10-23 | 76.15 | 2024-02-13 | 112.10 | +47.2% |
| JKPAPER | 2023-08-21 | 370.90 | 2024-02-21 | 374.44 | +1.0% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| RATEGAIN | 2023-08-14 | 547.00 | 2024-03-13 | 730.99 | +33.6% |
| RITES | 2024-01-29 | 342.50 | 2024-03-13 | 314.37 | -8.2% |
| PRUDENT | 2024-02-19 | 1,332.00 | 2024-03-13 | 1,176.05 | -11.7% |
| OIL | 2023-12-26 | 251.27 | 2024-03-15 | 344.53 | +37.1% |
| ANANDRATHI | 2023-07-17 | 265.70 | 2024-03-27 | 862.65 | +224.7% |
| CRISIL | 2024-02-26 | 4,905.25 | 2024-04-18 | 4,546.70 | -7.3% |
| JUSTDIAL | 2024-04-22 | 1,084.00 | 2024-05-09 | 1,008.00 | -7.0% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.65 | +23.1% |
| CUPID | 2023-10-30 | 6.05 | 2024-06-04 | 17.77 | +193.7% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| JIOFIN | 2024-03-18 | 346.95 | 2024-06-04 | 317.61 | -8.5% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| TDPOWERSYS | 2023-03-27 | 84.62 | 2024-07-19 | 188.72 | +123.0% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| NCC | 2024-06-10 | 327.60 | 2024-07-23 | 297.87 | -9.1% |
| JWL | 2024-05-13 | 490.00 | 2024-08-06 | 552.00 | +12.7% |
| ADANIPOWER | 2024-06-10 | 156.60 | 2024-08-12 | 126.55 | -19.2% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| AVANTIFEED | 2024-07-29 | 697.65 | 2024-09-09 | 650.13 | -6.8% |
| CERA | 2024-08-12 | 10,499.95 | 2024-09-19 | 8,198.93 | -21.9% |
| PGIL | 2024-07-22 | 405.00 | 2024-09-23 | 434.53 | +7.3% |
| DABUR | 2024-06-10 | 604.20 | 2024-10-03 | 602.49 | -0.3% |
| VGUARD | 2024-08-19 | 524.15 | 2024-10-04 | 420.24 | -19.8% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 261.67 | 2024-10-07 | 265.38 | +1.4% |
| GODFRYPHLP | 2024-02-05 | 848.30 | 2024-10-22 | 2,086.31 | +145.9% |
| VIYASH | 2024-09-30 | 216.00 | 2024-10-23 | 172.84 | -20.0% |
| INDIAGLYCO | 2024-07-22 | 515.00 | 2024-10-25 | 587.91 | +14.2% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| KIRLPNU | 2024-11-04 | 849.00 | 2024-12-23 | 798.00 | -6.0% |
| PRSMJOHNSN | 2024-09-16 | 214.51 | 2024-12-26 | 170.55 | -20.5% |
| JSWDULUX | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| PAYTM | 2024-10-14 | 729.60 | 2025-01-09 | 893.05 | +22.4% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| ZENTEC | 2024-12-23 | 2,555.00 | 2025-01-13 | 2,213.55 | -13.4% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| MOTILALOFS | 2024-11-11 | 998.05 | 2025-01-17 | 788.79 | -21.0% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| JSLL | 2025-01-06 | 2,400.00 | 2025-01-27 | 2,014.22 | -16.1% |
| FSL | 2024-11-11 | 367.05 | 2025-01-28 | 332.14 | -9.5% |
| LLOYDSME | 2025-01-06 | 1,439.00 | 2025-01-28 | 1,258.75 | -12.5% |
| APOLLO | 2025-01-20 | 131.50 | 2025-02-17 | 110.19 | -16.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-02-17 | 814.20 | -14.0% |
| BSE | 2024-10-07 | 1,396.67 | 2025-02-28 | 1,651.54 | +18.2% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| CEMPRO | 2024-10-07 | 655.05 | 2025-04-11 | 524.92 | -19.9% |
| PARAS | 2025-05-05 | 686.10 | 2025-07-28 | 708.99 | +3.3% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| WHIRLPOOL | 2025-04-28 | 1,153.90 | 2025-08-07 | 1,301.97 | +12.8% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| PARADEEP | 2025-08-04 | 218.91 | 2025-09-08 | 193.88 | -11.4% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| SMLMAH | 2025-04-28 | 1,680.00 | 2025-09-26 | 3,255.67 | +93.8% |
| FORCEMOT | 2025-04-28 | 9,275.00 | 2025-10-09 | 15,350.10 | +65.5% |
| ABFRL | 2025-09-15 | 88.58 | 2025-10-13 | 82.04 | -7.4% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| GALLANTT | 2025-04-21 | 474.75 | 2025-10-20 | 616.41 | +29.8% |
| BLACKBUCK | 2025-08-18 | 553.00 | 2025-10-28 | 642.20 | +16.1% |
| NETWEB | 2025-09-08 | 3,135.50 | 2025-11-06 | 3,515.95 | +12.1% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| NLCINDIA | 2025-09-29 | 280.30 | 2025-11-24 | 241.39 | -13.9% |
| TDPOWERSYS | 2025-11-03 | 382.27 | 2025-11-24 | 357.49 | -6.5% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| SHAILY | 2025-10-13 | 2,434.00 | 2025-12-15 | 2,340.80 | -3.8% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.50 | -10.1% |
| VIYASH | 2025-10-13 | 216.04 | 2026-01-12 | 195.04 | -9.7% |
| KIRLOSENG | 2025-12-22 | 1,258.30 | 2026-01-12 | 1,140.95 | -9.3% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| LTF | 2025-11-10 | 304.00 | 2026-01-21 | 281.77 | -7.3% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| GMRAIRPORT | 2025-12-01 | 108.90 | 2026-01-23 | 92.10 | -15.4% |
| HINDZINC | 2026-01-27 | 733.00 | 2026-02-02 | 602.35 | -17.8% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| CUB | 2025-11-10 | 190.65 | 2026-03-09 | 188.57 | -1.1% |
| HINDCOPPER | 2026-02-02 | 590.15 | 2026-03-12 | 528.63 | -10.4% |
| MAHABANK | 2025-11-03 | 59.70 | 2026-03-30 | 61.05 | +2.3% |
| TORNTPOWER | 2026-03-02 | 1,491.00 | 2026-03-30 | 1,315.84 | -11.7% |
| KSB | 2026-03-02 | 738.00 | 2026-05-04 | 917.42 | +24.3% |
| INOXINDIA | 2026-04-13 | 1,299.10 | 2026-05-13 | 1,372.18 | +5.6% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| GALLANTT | 2026-04-20 | 862.10 | 2026-05-14 | 783.75 | -9.1% |
| NLCINDIA | 2026-04-20 | 303.60 | 2026-06-09 | 320.62 | +5.6% |
| CIEINDIA | 2025-10-20 | 432.50 | 2026-06-11 | 429.88 | -0.6% |
| THERMAX | 2026-04-13 | 3,596.00 | 2026-07-29 | 4,306.63 | +19.8% |
| SFL | 2026-06-15 | 724.95 | 2026-08-06 | 698.73 | -3.6% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-06-01_to_2026-09-11.csv` beside this report (1974 events in all).*

```
2020-06-08  EIDPARRY    BUY ₹10.00 at ₹219.00 (fresh Friday signal — BUY: 4.34× weekly, month 3.59×, ladder rising; stop ₹132.60; charges ₹0.0118)
2020-06-08  IGL         BUY ₹9.95 at ₹247.75 (fresh Friday signal — BUY: 1.53× weekly, month 1.89×, ladder rising; stop ₹208.81; charges ₹0.0118)
2020-06-08  KIRLOSBROS  BUY ₹9.96 at ₹106.50 (fresh Friday signal — ACCUMULATE: 2.95× weekly, month 1.69×, ladder rising; stop ₹91.63; charges ₹0.0118)
2020-06-08  LLOYDSENGG  BUY ₹10.00 at ₹0.87 (fresh Friday signal — BUY: 4.83× weekly, month 4.76×, ladder rising; stop ₹0.46; charges ₹0.0118)
2020-06-08  RCF         BUY ₹10.02 at ₹45.20 (fresh Friday signal — BUY: 2.38× weekly, month 2.29×, ladder rising; stop ₹35.25; charges ₹0.0119)
2020-06-08  RELAXO      BUY ₹10.00 at ₹759.45 (fresh Friday signal — BUY: 1.89× weekly, month 1.81×, ladder rising; stop ₹603.77; charges ₹0.0118)
2020-06-08  SYNGENE     BUY ₹9.95 at ₹373.90 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 2.27×, ladder rising; stop ₹323.19; charges ₹0.0118)
2020-06-15  ADVENZYMES  BUY ₹9.87 at ₹172.70 (fresh Friday signal — BUY: 4.13× weekly, month 2.92×, ladder rising; stop ₹126.20; charges ₹0.0117)
2020-06-15  CAPLIPOINT  BUY ₹9.82 at ₹383.80 (fresh Friday signal — BUY: 5.39× weekly, month 2.09×, ladder rising; stop ₹291.46; charges ₹0.0116)
2020-06-15  GRANULES    BUY ₹9.82 at ₹216.75 (fresh Friday signal — BUY: 3.46× weekly, month 2.65×, ladder rising; stop ₹170.34; charges ₹0.0116)
2020-07-07  IGL         SELL ₹8.36 at stop ₹208.81 (-15.7%, charges ₹0.0087) — the cash goes back to work at the next Friday screen
2020-07-13  HAL         BUY ₹8.97 at ₹475.00 (fresh Friday signal — BUY: 14.34× weekly, month 18.24×, ladder rising; stop ₹353.71; charges ₹0.0106)
2020-07-28  RELAXO      SELL ₹7.93 at stop ₹603.77 (-20.5%, charges ₹0.0082) — the cash goes back to work at the next Friday screen
2020-07-31  LLOYDSENGG  SELL ₹8.18 at stop ₹0.71 (-18.0%, charges ₹0.0085) — the cash goes back to work at the next Friday screen
2020-08-03  ZENTEC      BUY ₹11.10 at ₹58.80 (fresh Friday signal — ACCUMULATE: 4.33× weekly, month 4.91×, ladder rising; stop ₹42.67; charges ₹0.0132)
2020-08-17  EIDPARRY    SELL ₹12.44 at stop ₹273.03 (+24.7%, charges ₹0.0129) — the cash goes back to work at the next Friday screen
2020-08-24  THYROCARE   BUY ₹12.37 at ₹263.35 (fresh Friday signal — BUY: 7.09× weekly, month 4.48×, ladder rising; stop ₹199.77; charges ₹0.0147)
2020-08-31  GRANULES    SELL ₹12.98 at stop ₹286.95 (+32.4%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2020-08-31  ZENTEC      SELL ₹15.17 at stop ₹80.56 (+37.0%, charges ₹0.0157) — the cash goes back to work at the next Friday screen
2020-09-07  INDIAMART   BUY ₹11.46 at ₹2,124.50 (fresh Friday signal — BUY: 2.46× weekly, month 1.96×, ladder rising; stop ₹1,655.61; charges ₹0.0136)
2020-09-07  POLYMED     BUY ₹11.53 at ₹449.70 (fresh Friday signal — BUY: 2.13× weekly, month 2.66×, ladder rising; stop ₹372.40; charges ₹0.0137)
2020-09-08  KIRLOSBROS  SELL ₹11.27 at stop ₹120.79 (+13.4%, charges ₹0.0117) — the cash goes back to work at the next Friday screen
2020-09-09  RCF         SELL ₹10.14 at stop ₹45.84 (+1.4%, charges ₹0.0105) — the cash goes back to work at the next Friday screen
2020-09-14  ATGL        BUY ₹7.68 at ₹209.75 (fresh Friday signal — BUY: 1.66× weekly, month 1.67×, ladder rising; stop ₹159.58; charges ₹0.0091)
2020-09-14  GLAXO       BUY ₹11.97 at ₹1,675.00 (fresh Friday signal — BUY: 2.55× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.0142)
2020-09-14  SCHAEFFLER  BUY ₹12.00 at ₹814.00 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 1.89×, ladder rising; stop ₹724.67; charges ₹0.0142)
2020-09-22  HAL         SELL ₹7.36 at stop ₹390.57 (-17.8%, charges ₹0.0076) — the cash goes back to work at the next Friday screen
2020-09-23  SCHAEFFLER  SELL ₹10.66 at stop ₹724.67 (-11.0%, charges ₹0.0111) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹12.19 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0144)
2020-10-19  INDIAMART   SELL ₹12.46 at stop ₹2,315.62 (+9.0%, charges ₹0.0129) — the cash goes back to work at the next Friday screen
2020-10-26  JUSTDIAL    BUY ₹12.46 at ₹584.00 (fresh Friday signal — BUY: 4.99× weekly, month 1.82×, ladder rising; stop ₹383.80; charges ₹0.0148)
2020-10-30  CAPLIPOINT  SELL ₹12.72 at stop ₹498.06 (+29.8%, charges ₹0.0132) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹10.28 at stop ₹1,441.55 (-13.9%, charges ₹0.0107) — the cash goes back to work at the next Friday screen
2020-11-02  KPRMILL     BUY ₹12.28 at ₹151.00 (fresh Friday signal — BUY: 2.37× weekly, month 3.11×, ladder rising; stop ₹108.58; charges ₹0.0146)
2020-11-03  ADVENZYMES  SELL ₹16.67 at stop ₹292.33 (+69.3%, charges ₹0.0173) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹12.47 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 1.65×, ladder rising; stop ₹77.16; charges ₹0.0148)
2020-11-12  THYROCARE   SELL ₹15.88 at stop ₹338.83 (+28.7%, charges ₹0.0165) — the cash goes back to work at the next Friday screen
2020-11-17  PIIND       BUY ₹12.77 at ₹2,348.20 (fresh Friday signal — ACCUMULATE: 1.62× weekly, month 1.81×, ladder rising; stop ₹2,107.67; charges ₹0.0151)
2020-11-17  TRENT       BUY ₹12.79 at ₹755.00 (fresh Friday signal — ACCUMULATE: 3.32× weekly, month 1.93×, ladder rising; stop ₹551.90; charges ₹0.0152)
2020-11-23  HFCL        BUY ₹11.06 at ₹18.20 (fresh Friday signal — BUY: 3.09× weekly, month 1.77×, ladder rising; stop ₹15.20; charges ₹0.0131)
2020-12-21  ATGL        SELL ₹12.15 at stop ₹332.60 (+58.6%, charges ₹0.0126) — the cash goes back to work at the next Friday screen
2020-12-22  SYNGENE     SELL ₹14.93 at stop ₹562.40 (+50.4%, charges ₹0.0155) — the cash goes back to work at the next Friday screen
2020-12-28  GRAVITA     BUY ₹11.80 at ₹69.65 (fresh Friday signal — BUY: 2.45× weekly, month 4.29×, ladder rising; stop ₹46.41; charges ₹0.0140)
2020-12-28  HONAUT      BUY ₹15.29 at ₹38,887.75 (fresh Friday signal — BUY: 5.49× weekly, month 1.69×, ladder rising; stop ₹29,024.49; charges ₹0.0181)
2021-01-20  BORORENEW   SELL ₹30.89 at stop ₹247.59 (+148.3%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2021-01-25  INDIAMART   BUY ₹15.34 at ₹3,990.00 (fresh Friday signal — BUY: 2.37× weekly, month 1.58×, ladder rising; stop ₹3,323.20; charges ₹0.0182)
2021-01-25  JUSTDIAL    SELL ₹13.25 at stop ₹622.35 (+6.6%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2021-01-25  PIIND       SELL ₹11.44 at stop ₹2,107.67 (-10.2%, charges ₹0.0119) — the cash goes back to work at the next Friday screen
2021-01-25  TATAELXSI   BUY ₹15.55 at ₹2,608.00 (fresh Friday signal — BUY: 2.94× weekly, month 2.74×, ladder rising; stop ₹1,712.61; charges ₹0.0184)
2021-01-28  HFCL        SELL ₹17.06 at stop ₹28.12 (+54.5%, charges ₹0.0177) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹13.46 at stop ₹928.05 (+10.7%, charges ₹0.0140) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹10.59 at stop ₹626.30 (-17.0%, charges ₹0.0110) — the cash goes back to work at the next Friday screen
2021-02-01  GAEL        BUY ₹15.60 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.70× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.0185)
2021-02-08  ITC         BUY ₹15.79 at ₹228.69 (fresh Friday signal — BUY: 2.38× weekly, month 1.68×, ladder rising; stop ₹184.60; charges ₹0.0187)
2021-02-08  MAHABANK    BUY ₹15.76 at ₹16.45 (fresh Friday signal — BUY: 2.17× weekly, month 3.37×, ladder rising; stop ₹9.50; charges ₹0.0187)
2021-02-08  UJJIVANSFB  BUY ₹15.83 at ₹37.15 (fresh Friday signal — ACCUMULATE: 2.60× weekly, month 2.19×, ladder rising; stop ₹32.12; charges ₹0.0188)
2021-02-22  TATAELXSI   SELL ₹15.83 at stop ₹2,660.00 (+2.0%, charges ₹0.0164) — the cash goes back to work at the next Friday screen
2021-02-23  GAEL        SELL ₹13.66 at stop ₹62.70 (-12.3%, charges ₹0.0142) — the cash goes back to work at the next Friday screen
2021-02-24  KPRMILL     SELL ₹13.52 at stop ₹166.62 (+10.3%, charges ₹0.0140) — the cash goes back to work at the next Friday screen
2021-02-26  ITC         SELL ₹13.60 at stop ₹197.41 (-13.7%, charges ₹0.0141) — the cash goes back to work at the next Friday screen
2021-03-01  GESHIP      BUY ₹16.91 at ₹315.90 (fresh Friday signal — BUY: 2.93× weekly, month 1.80×, ladder rising; stop ₹219.84; charges ₹0.0200)
2021-03-01  IOB         BUY ₹17.01 at ₹18.90 (fresh Friday signal — ACCUMULATE: 3.52× weekly, month 9.60×, ladder rising; stop ₹13.70; charges ₹0.0202)
2021-03-01  RCF         BUY ₹16.78 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.12×, ladder rising; stop ₹50.16; charges ₹0.0199)
2021-03-01  VAIBHAVGBL  BUY ₹8.73 at ₹708.00 (fresh Friday signal — BUY: 2.74× weekly, month 2.17×, ladder rising; stop ₹523.07; charges ₹0.0103)
2021-03-02  INDIAMART   SELL ₹15.87 at stop ₹4,137.25 (+3.7%, charges ₹0.0165) — the cash goes back to work at the next Friday screen
2021-03-08  JSWENERGY   BUY ₹15.87 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.49×, ladder rising; stop ₹65.79; charges ₹0.0188)
2021-03-17  GRAVITA     SELL ₹16.25 at stop ₹96.13 (+38.0%, charges ₹0.0169) — the cash goes back to work at the next Friday screen
2021-03-17  RCF         SELL ₹16.56 at stop ₹79.16 (-1.1%, charges ₹0.0172) — the cash goes back to work at the next Friday screen
2021-03-18  UJJIVANSFB  SELL ₹13.66 at stop ₹32.12 (-13.5%, charges ₹0.0142) — the cash goes back to work at the next Friday screen
2021-03-19  MAHABANK    SELL ₹17.56 at stop ₹18.37 (+11.7%, charges ₹0.0182) — the cash goes back to work at the next Friday screen
2021-03-22  DEEPAKFERT  BUY ₹15.94 at ₹237.00 (fresh Friday signal — BUY: 2.43× weekly, month 1.82×, ladder rising; stop ₹184.78; charges ₹0.0189)
2021-03-22  HONAUT      SELL ₹16.44 at stop ₹41,911.15 (+7.8%, charges ₹0.0171) — the cash goes back to work at the next Friday screen
2021-03-22  KEI         BUY ₹15.85 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.0188)
2021-03-22  WELSPUNLIV  BUY ₹15.93 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.45×, ladder rising; stop ₹67.45; charges ₹0.0189)
2021-03-30  KPITTECH    BUY ₹15.84 at ₹182.00 (fresh Friday signal — BUY: 1.71× weekly, month 2.75×, ladder rising; stop ₹136.62; charges ₹0.0188)
2021-04-01  TAX         FY2021 settled: ₹10.2909 paid (STCG ₹51.45 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-12  GESHIP      SELL ₹15.52 at stop ₹290.70 (-8.0%, charges ₹0.0161) — the cash goes back to work at the next Friday screen
2021-04-19  KPRMILL     BUY ₹15.08 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0179)
2021-04-28  IOB         SELL ₹13.31 at stop ₹14.82 (-21.6%, charges ₹0.0138) — the cash goes back to work at the next Friday screen
2021-05-03  MARKSANS    BUY ₹16.39 at ₹70.95 (fresh Friday signal — ACCUMULATE: 3.13× weekly, month 3.97×, ladder rising; stop ₹64.12; charges ₹0.0194)
2021-06-14  POLYMED     SELL ₹24.31 at stop ₹950.00 (+111.3%, charges ₹0.0252) — the cash goes back to work at the next Friday screen
2021-06-21  JWL         BUY ₹19.73 at ₹30.80 (fresh Friday signal — BUY: 6.73× weekly, month 3.20×, ladder rising; stop ₹18.23; charges ₹0.0234)
2021-07-20  VAIBHAVGBL  SELL ₹9.45 at stop ₹767.90 (+8.5%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2021-07-26  MPHASIS     BUY ₹18.00 at ₹2,512.00 (fresh Friday signal — BUY: 2.75× weekly, month 1.90×, ladder rising; stop ₹1,875.30; charges ₹0.0213)
2021-08-10  MARKSANS    SELL ₹17.78 at stop ₹77.14 (+8.7%, charges ₹0.0184) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNLIV  SELL ₹24.33 at stop ₹124.64 (+53.0%, charges ₹0.0252) — the cash goes back to work at the next Friday screen
2021-08-11  JSWENERGY   SELL ₹44.11 at stop ₹228.00 (+178.6%, charges ₹0.0458) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹22.47 at stop ₹352.48 (+49.4%, charges ₹0.0233) — the cash goes back to work at the next Friday screen
2021-08-16  GABRIEL     BUY ₹23.25 at ₹149.30 (fresh Friday signal — BUY: 2.50× weekly, month 3.57×, ladder rising; stop ₹118.77; charges ₹0.0275)
2021-08-16  TATAINVEST  BUY ₹23.29 at ₹130.81 (fresh Friday signal — BUY: 8.45× weekly, month 4.82×, ladder rising; stop ₹103.11; charges ₹0.0276)
2021-08-23  GRAVITA     BUY ₹22.09 at ₹188.60 (fresh Friday signal — BUY: 2.16× weekly, month 1.88×, ladder rising; stop ₹151.95; charges ₹0.0262)
2021-08-23  JWL         SELL ₹19.45 at stop ₹30.42 (-1.2%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2021-09-06  HAL         BUY ₹22.90 at ₹705.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.49×, ladder rising; stop ₹500.63; charges ₹0.0271)
2021-09-06  NHPC        BUY ₹22.95 at ₹27.90 (fresh Friday signal — BUY: 5.07× weekly, month 1.59×, ladder rising; stop ₹24.13; charges ₹0.0272)
2021-09-06  TDPOWERSYS  BUY ₹13.65 at ₹32.80 (fresh Friday signal — BUY: 2.60× weekly, month 4.52×, ladder rising; stop ₹25.56; charges ₹0.0162)
2021-10-22  KEI         SELL ₹25.85 at stop ₹853.10 (+63.4%, charges ₹0.0268) — the cash goes back to work at the next Friday screen
2021-10-22  TDPOWERSYS  SELL ₹12.68 at stop ₹30.53 (-6.9%, charges ₹0.0132) — the cash goes back to work at the next Friday screen
2021-10-25  LTM         BUY ₹23.92 at ₹6,555.00 (fresh Friday signal — BUY: 4.63× weekly, month 1.86×, ladder rising; stop ₹5,353.77; charges ₹0.0283)
2021-10-28  HAL         SELL ₹20.63 at stop ₹636.50 (-9.7%, charges ₹0.0214) — the cash goes back to work at the next Friday screen
2021-11-01  PERSISTENT  BUY ₹24.10 at ₹1,977.15 (fresh Friday signal — ACCUMULATE: 1.71× weekly, month 2.09×, ladder rising; stop ₹1,728.75; charges ₹0.0286)
2021-11-11  DEEPAKFERT  SELL ₹25.88 at stop ₹385.70 (+62.7%, charges ₹0.0268) — the cash goes back to work at the next Friday screen
2021-11-15  GOKULAGRO   BUY ₹25.15 at ₹31.05 (fresh Friday signal — BUY: 2.63× weekly, month 1.60×, ladder rising; stop ₹24.87; charges ₹0.0298)
2021-11-22  GRAVITA     SELL ₹23.02 at stop ₹197.03 (+4.5%, charges ₹0.0239) — the cash goes back to work at the next Friday screen
2021-11-26  TATAINVEST  SELL ₹25.53 at stop ₹143.65 (+9.8%, charges ₹0.0265) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹24.18 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.0286)
2021-11-29  ESCORTS     BUY ₹24.22 at ₹1,875.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.18×, ladder rising; stop ₹1,369.04; charges ₹0.0287)
2021-11-29  NHPC        SELL ₹24.71 at stop ₹30.11 (+7.9%, charges ₹0.0256) — the cash goes back to work at the next Friday screen
2021-11-30  MPHASIS     SELL ₹20.82 at stop ₹2,912.57 (+15.9%, charges ₹0.0216) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹24.43 at ₹209.99 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹158.85; charges ₹0.0289)
2021-12-06  CHAMBLFERT  BUY ₹24.37 at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹0.0289)
2021-12-20  KPITTECH    SELL ₹39.85 at stop ₹458.85 (+152.1%, charges ₹0.0413) — the cash goes back to work at the next Friday screen
2021-12-27  UNOMINDA    BUY ₹24.65 at ₹590.00 (fresh Friday signal — BUY: 3.66× weekly, month 2.64×, ladder rising; stop ₹464.60; charges ₹0.0292)
2022-01-03  PGEL        BUY ₹23.98 at ₹80.99 (fresh Friday signal — BUY: 2.09× weekly, month 2.90×, ladder rising; stop ₹56.96; charges ₹0.0284)
2022-01-07  UNOMINDA    SELL ₹22.68 at stop ₹544.21 (-7.8%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2022-01-10  AFFLE       BUY ₹22.68 at ₹1,307.00 (fresh Friday signal — BUY: 4.57× weekly, month 1.57×, ladder rising; stop ₹955.80; charges ₹0.0269)
2022-01-24  LTM         SELL ₹22.82 at stop ₹6,270.00 (-4.3%, charges ₹0.0237) — the cash goes back to work at the next Friday screen
2022-01-24  PERSISTENT  SELL ₹25.14 at stop ₹2,067.34 (+4.6%, charges ₹0.0261) — the cash goes back to work at the next Friday screen
2022-01-24  PGEL        SELL ₹21.40 at stop ₹72.44 (-10.6%, charges ₹0.0222) — the cash goes back to work at the next Friday screen
2022-01-25  AFFLE       SELL ₹20.89 at stop ₹1,206.50 (-7.7%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2022-01-25  GOKULAGRO   SELL ₹28.29 at stop ₹35.00 (+12.7%, charges ₹0.0293) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹23.87 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0283)
2022-02-07  CCL         BUY ₹24.01 at ₹503.55 (fresh Friday signal — BUY: 4.07× weekly, month 1.58×, ladder rising; stop ₹408.60; charges ₹0.0284)
2022-02-11  SHARDACROP  SELL ₹22.14 at stop ₹545.30 (-7.1%, charges ₹0.0230) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹22.02 at stop ₹424.65 (-8.7%, charges ₹0.0228) — the cash goes back to work at the next Friday screen
2022-02-14  GABRIEL     SELL ₹19.48 at stop ₹125.40 (-16.0%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2022-02-14  GNFC        BUY ₹22.91 at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹0.0271)
2022-02-21  ADANIPOWER  BUY ₹22.97 at ₹26.40 (fresh Friday signal — BUY: 8.22× weekly, month 2.70×, ladder rising; stop ₹18.02; charges ₹0.0272)
2022-02-21  CGCL        BUY ₹22.76 at ₹567.08 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹507.72; charges ₹0.0270)
2022-02-24  CCL         SELL ₹21.02 at stop ₹441.75 (-12.3%, charges ₹0.0218) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹21.12 at stop ₹353.85 (-13.2%, charges ₹0.0219) — the cash goes back to work at the next Friday screen
2022-02-25  ESCORTS     SELL ₹22.61 at stop ₹1,754.65 (-6.4%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹16.9329 paid (STCG ₹84.66 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  RCF         BUY ₹24.58 at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.0291)
2022-04-04  SPLPETRO    BUY ₹24.70 at ₹475.00 (fresh Friday signal — BUY: 4.41× weekly, month 2.84×, ladder rising; stop ₹398.29; charges ₹0.0293)
2022-04-11  BLS         BUY ₹25.02 at ₹82.50 (fresh Friday signal — BUY: 8.78× weekly, month 1.73×, ladder rising; stop ₹54.82; charges ₹0.0296)
2022-04-11  MINDACORP   BUY ₹25.00 at ₹230.05 (fresh Friday signal — BUY: 2.10× weekly, month 1.60×, ladder rising; stop ₹186.63; charges ₹0.0296)
2022-04-18  LTFOODS     BUY ₹14.18 at ₹91.70 (fresh Friday signal — BUY: 12.80× weekly, month 1.79×, ladder rising; stop ₹73.86; charges ₹0.0168)
2022-05-04  RCF         SELL ₹23.70 at stop ₹93.15 (-3.4%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2022-05-06  GNFC        SELL ₹32.74 at stop ₹792.16 (+43.2%, charges ₹0.0340) — the cash goes back to work at the next Friday screen
2022-05-09  MRPL        BUY ₹24.79 at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹0.0294)
2022-05-10  BSE         SELL ₹29.70 at stop ₹255.87 (+21.8%, charges ₹0.0308) — the cash goes back to work at the next Friday screen
2022-05-11  LTFOODS     SELL ₹11.40 at stop ₹73.86 (-19.5%, charges ₹0.0118) — the cash goes back to work at the next Friday screen
2022-05-11  MINDACORP   SELL ₹20.24 at stop ₹186.63 (-18.9%, charges ₹0.0210) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹23.61 at ₹146.67 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.79×, ladder rising; stop ₹130.85; charges ₹0.0280)
2022-05-23  ACC         BUY ₹25.59 at ₹2,260.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹0.0303)
2022-05-24  SPLPETRO    SELL ₹22.01 at stop ₹424.27 (-10.7%, charges ₹0.0228) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹25.05 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0297)
2022-06-20  APARINDS    BUY ₹23.88 at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹0.0283)
2022-07-06  MRPL        SELL ₹22.07 at stop ₹69.61 (-10.8%, charges ₹0.0229) — the cash goes back to work at the next Friday screen
2022-07-25  TIINDIA     BUY ₹27.39 at ₹2,135.00 (fresh Friday signal — BUY: 4.17× weekly, month 2.43×, ladder rising; stop ₹1,862.00; charges ₹0.0324)
2022-08-22  VBL         SELL ₹30.28 at stop ₹188.52 (+28.5%, charges ₹0.0314) — the cash goes back to work at the next Friday screen
2022-08-23  BLS         SELL ₹33.49 at stop ₹110.67 (+34.1%, charges ₹0.0347) — the cash goes back to work at the next Friday screen
2022-08-29  HOMEFIRST   BUY ₹29.48 at ₹944.95 (fresh Friday signal — ACCUMULATE: 3.67× weekly, month 2.49×, ladder rising; stop ₹849.35; charges ₹0.0349)
2022-08-29  KALYANKJIL  BUY ₹29.51 at ₹78.10 (fresh Friday signal — BUY: 9.54× weekly, month 2.93×, ladder rising; stop ₹65.55; charges ₹0.0350)
2022-08-29  SIEMENS     BUY ₹16.32 at ₹1,688.21 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 1.62×, ladder rising; stop ₹1,573.13; charges ₹0.0193)
2022-09-14  HOMEFIRST   SELL ₹26.44 at stop ₹849.35 (-10.1%, charges ₹0.0274) — the cash goes back to work at the next Friday screen
2022-09-19  MAHSCOOTER  BUY ₹26.44 at ₹5,103.50 (fresh Friday signal — BUY: 10.17× weekly, month 2.61×, ladder rising; stop ₹3,847.79; charges ₹0.0313)
2022-09-26  SIEMENS     SELL ₹15.61 at stop ₹1,618.44 (-4.1%, charges ₹0.0162) — the cash goes back to work at the next Friday screen
2022-10-03  TSFINV      BUY ₹15.61 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹0.0185)
2022-10-11  TSFINV      SELL ₹13.87 at stop ₹92.20 (-10.9%, charges ₹0.0144) — the cash goes back to work at the next Friday screen
2022-10-14  ADANIPOWER  SELL ₹57.99 at stop ₹66.80 (+153.0%, charges ₹0.0602) — the cash goes back to work at the next Friday screen
2022-10-17  APOLLO      BUY ₹29.60 at ₹24.00 (fresh Friday signal — BUY: 6.98× weekly, month 4.78×, ladder rising; stop ₹14.17; charges ₹0.0351)
2022-10-24  GODFRYPHLP  BUY ₹30.10 at ₹483.67 (fresh Friday signal — BUY: 4.48× weekly, month 3.07×, ladder rising; stop ₹403.15; charges ₹0.0357)
2022-11-03  APARINDS    SELL ₹34.07 at stop ₹1,358.50 (+43.0%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹31.14 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0369)
2022-11-22  KALYANKJIL  SELL ₹35.64 at stop ₹94.53 (+21.0%, charges ₹0.0370) — the cash goes back to work at the next Friday screen
2022-11-28  IRFC        BUY ₹19.22 at ₹32.00 (fresh Friday signal — BUY: 9.02× weekly, month 13.28×, ladder rising; stop ₹23.09; charges ₹0.0228)
2022-11-28  UCOBANK     BUY ₹31.52 at ₹21.05 (fresh Friday signal — BUY: 13.59× weekly, month 16.04×, ladder rising; stop ₹13.59; charges ₹0.0373)
2022-12-21  ELECON      SELL ₹41.32 at stop ₹202.49 (+65.3%, charges ₹0.0429) — the cash goes back to work at the next Friday screen
2022-12-22  MAHSCOOTER  SELL ₹23.87 at stop ₹4,617.00 (-9.5%, charges ₹0.0248) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹27.86 at stop ₹2,465.15 (+9.1%, charges ₹0.0289) — the cash goes back to work at the next Friday screen
2022-12-23  IRFC        SELL ₹16.90 at stop ₹28.20 (-11.9%, charges ₹0.0175) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹31.04 at stop ₹139.84 (-0.1%, charges ₹0.0322) — the cash goes back to work at the next Friday screen
2022-12-26  APOLLO      SELL ₹30.06 at stop ₹24.42 (+1.8%, charges ₹0.0312) — the cash goes back to work at the next Friday screen
2022-12-26  GODFRYPHLP  SELL ₹34.01 at stop ₹547.85 (+13.3%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2023-01-02  GICRE       BUY ₹31.67 at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 11.13×, ladder rising; stop ₹137.57; charges ₹0.0375)
2023-01-02  GSFC        BUY ₹32.22 at ₹140.70 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.67×, ladder rising; stop ₹111.58; charges ₹0.0382)
2023-01-02  IOB         BUY ₹31.61 at ₹32.40 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 28.89×, ladder rising; stop ₹21.23; charges ₹0.0375)
2023-01-02  JSL         BUY ₹32.06 at ₹241.00 (fresh Friday signal — BUY: 2.24× weekly, month 2.14×, ladder rising; stop ₹192.61; charges ₹0.0380)
2023-01-02  LLOYDSENGG  BUY ₹31.81 at ₹15.63 (fresh Friday signal — ACCUMULATE: 2.36× weekly, month 2.74×, ladder rising; stop ₹10.86; charges ₹0.0377)
2023-01-02  YESBANK     BUY ₹31.55 at ₹20.85 (fresh Friday signal — ACCUMULATE: 2.89× weekly, month 3.19×, ladder rising; stop ₹15.00; charges ₹0.0374)
2023-01-11  TIINDIA     SELL ₹33.26 at stop ₹2,598.35 (+21.7%, charges ₹0.0345) — the cash goes back to work at the next Friday screen
2023-01-16  ANUP        BUY ₹32.03 at ₹476.12 (fresh Friday signal — ACCUMULATE: 4.79× weekly, month 1.56×, ladder rising; stop ₹364.75; charges ₹0.0380)
2023-02-01  GICRE       SELL ₹29.57 at stop ₹167.72 (-6.4%, charges ₹0.0307) — the cash goes back to work at the next Friday screen
2023-02-06  JINDALSAW   BUY ₹30.76 at ₹65.22 (fresh Friday signal — BUY: 2.71× weekly, month 3.60×, ladder rising; stop ₹51.25; charges ₹0.0364)
2023-02-07  LLOYDSENGG  SELL ₹39.13 at stop ₹19.27 (+23.3%, charges ₹0.0406) — the cash goes back to work at the next Friday screen
2023-02-27  CERA        BUY ₹23.07 at ₹6,150.00 (fresh Friday signal — BUY: 5.94× weekly, month 1.75×, ladder rising; stop ₹5,579.40; charges ₹0.0273)
2023-02-27  SONATSOFTW  BUY ₹30.23 at ₹360.00 (fresh Friday signal — BUY: 9.70× weekly, month 3.34×, ladder rising; stop ₹282.62; charges ₹0.0358)
2023-03-08  CGCL        SELL ₹26.71 at stop ₹666.82 (+17.6%, charges ₹0.0277) — the cash goes back to work at the next Friday screen
2023-03-10  ANUP        SELL ₹35.40 at stop ₹527.27 (+10.7%, charges ₹0.0367) — the cash goes back to work at the next Friday screen
2023-03-13  YESBANK     SELL ₹23.16 at stop ₹15.34 (-26.4%, charges ₹0.0240) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹30.15 at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.60×, ladder rising; stop ₹691.46; charges ₹0.0357)
2023-03-20  IOB         SELL ₹21.59 at stop ₹22.18 (-31.5%, charges ₹0.0224) — the cash goes back to work at the next Friday screen
2023-03-27  JINDALSAW   SELL ₹31.96 at stop ₹67.92 (+4.1%, charges ₹0.0331) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹29.90 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.85×, ladder rising; stop ₹372.21; charges ₹0.0354)
2023-03-27  TDPOWERSYS  BUY ₹29.85 at ₹84.62 (fresh Friday signal — BUY: 1.62× weekly, month 2.13×, ladder rising; stop ₹64.12; charges ₹0.0354)
2023-03-27  UCOBANK     SELL ₹35.05 at stop ₹23.46 (+11.4%, charges ₹0.0364) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹31.12 at stop ₹371.45 (+3.2%, charges ₹0.0323) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹28.07 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.04×, ladder rising; stop ₹1,171.71; charges ₹0.0333)
2023-04-03  TAX         FY2023 settled: ₹17.2485 paid (STCG ₹83.74 @20%, LTCG ₹4.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-10  KIRLOSBROS  BUY ₹28.38 at ₹425.00 (fresh Friday signal — BUY: 1.86× weekly, month 2.34×, ladder rising; stop ₹357.44; charges ₹0.0336)
2023-04-13  JSL         SELL ₹34.12 at stop ₹256.98 (+6.6%, charges ₹0.0354) — the cash goes back to work at the next Friday screen
2023-04-24  MARKSANS    BUY ₹28.96 at ₹78.00 (fresh Friday signal — ACCUMULATE: 1.64× weekly, month 1.51×, ladder rising; stop ₹71.87; charges ₹0.0343)
2023-04-24  ZFCVINDIA   BUY ₹28.93 at ₹1,697.50 (fresh Friday signal — ACCUMULATE: 7.38× weekly, month 1.55×, ladder rising; stop ₹1,561.17; charges ₹0.0343)
2023-04-26  CERA        SELL ₹22.59 at stop ₹6,037.30 (-1.8%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2023-04-26  KIRLOSBROS  SELL ₹26.91 at stop ₹403.85 (-5.0%, charges ₹0.0279) — the cash goes back to work at the next Friday screen
2023-05-02  ASHAPURMIN  BUY ₹30.30 at ₹143.10 (fresh Friday signal — BUY: 2.05× weekly, month 2.10×, ladder rising; stop ₹123.50; charges ₹0.0359)
2023-05-02  REFEX       BUY ₹30.41 at ₹65.32 (fresh Friday signal — BUY: 4.73× weekly, month 1.57×, ladder rising; stop ₹54.53; charges ₹0.0360)
2023-05-22  MARKSANS    SELL ₹26.62 at stop ₹71.87 (-7.9%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2023-05-29  ASHAPURMIN  SELL ₹28.36 at stop ₹134.24 (-6.2%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2023-05-29  GSFC        SELL ₹35.62 at stop ₹155.85 (+10.8%, charges ₹0.0369) — the cash goes back to work at the next Friday screen
2023-05-29  THANGAMAYL  BUY ₹32.06 at ₹672.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.52×, ladder rising; stop ₹558.15; charges ₹0.0380)
2023-06-05  EPL         BUY ₹32.12 at ₹201.90 (fresh Friday signal — ACCUMULATE: 6.59× weekly, month 6.26×, ladder rising; stop ₹170.76; charges ₹0.0381)
2023-06-05  FORCEMOT    BUY ₹32.82 at ₹1,951.00 (fresh Friday signal — BUY: 23.21× weekly, month 3.12×, ladder rising; stop ₹1,289.01; charges ₹0.0389)
2023-07-03  ANURAS      SELL ₹40.10 at stop ₹1,007.67 (+33.3%, charges ₹0.0416) — the cash goes back to work at the next Friday screen
2023-07-10  CEATLTD     BUY ₹35.79 at ₹2,408.00 (fresh Friday signal — BUY: 4.55× weekly, month 2.41×, ladder rising; stop ₹1,892.78; charges ₹0.0424)
2023-07-12  KSB         SELL ₹29.11 at stop ₹407.74 (-2.4%, charges ₹0.0302) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹33.41 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0396)
2023-08-11  EPL         SELL ₹31.83 at stop ₹200.50 (-0.7%, charges ₹0.0330) — the cash goes back to work at the next Friday screen
2023-08-11  REFEX       SELL ₹56.53 at stop ₹121.69 (+86.3%, charges ₹0.0586) — the cash goes back to work at the next Friday screen
2023-08-14  CEATLTD     SELL ₹33.30 at stop ₹2,244.85 (-6.8%, charges ₹0.0345) — the cash goes back to work at the next Friday screen
2023-08-14  RATEGAIN    BUY ₹39.42 at ₹547.00 (fresh Friday signal — BUY: 5.36× weekly, month 1.91×, ladder rising; stop ₹422.99; charges ₹0.0467)
2023-08-14  VARROC      BUY ₹39.52 at ₹385.40 (fresh Friday signal — BUY: 6.86× weekly, month 2.37×, ladder rising; stop ₹304.00; charges ₹0.0468)
2023-08-21  JKPAPER     BUY ₹40.39 at ₹370.90 (fresh Friday signal — BUY: 3.19× weekly, month 1.71×, ladder rising; stop ₹312.45; charges ₹0.0479)
2023-10-20  FORCEMOT    SELL ₹62.27 at stop ₹3,709.99 (+90.2%, charges ₹0.0646) — the cash goes back to work at the next Friday screen
2023-10-23  APOLLO      BUY ₹44.43 at ₹76.15 (fresh Friday signal — BUY: 3.56× weekly, month 3.24×, ladder rising; stop ₹59.94; charges ₹0.0526)
2023-10-23  THANGAMAYL  SELL ₹65.12 at stop ₹1,368.00 (+103.6%, charges ₹0.0675) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹37.36 at stop ₹1,840.70 (+33.4%, charges ₹0.0388) — the cash goes back to work at the next Friday screen
2023-10-25  VARROC      SELL ₹46.13 at stop ₹450.92 (+17.0%, charges ₹0.0479) — the cash goes back to work at the next Friday screen
2023-10-30  ANGELONE    BUY ₹44.76 at ₹253.50 (fresh Friday signal — BUY: 1.84× weekly, month 2.75×, ladder rising; stop ₹194.37; charges ₹0.0530)
2023-10-30  CUPID       BUY ₹44.69 at ₹6.05 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹3.66; charges ₹0.0529)
2023-10-30  SHAREINDIA  BUY ₹44.73 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0530)
2023-11-06  TSFINV      BUY ₹34.60 at ₹144.75 (fresh Friday signal — BUY: 3.35× weekly, month 1.95×, ladder rising; stop ₹109.72; charges ₹0.0410)
2023-12-20  TSFINV      SELL ₹34.68 at stop ₹145.40 (+0.4%, charges ₹0.0360) — the cash goes back to work at the next Friday screen
2023-12-26  OIL         BUY ₹34.68 at ₹251.27 (fresh Friday signal — BUY: 6.09× weekly, month 3.92×, ladder rising; stop ₹186.55; charges ₹0.0411)
2024-01-23  ANGELONE    SELL ₹52.30 at stop ₹296.88 (+17.1%, charges ₹0.0542) — the cash goes back to work at the next Friday screen
2024-01-29  RITES       BUY ₹52.30 at ₹342.50 (fresh Friday signal — BUY: 11.32× weekly, month 2.99×, ladder rising; stop ₹240.21; charges ₹0.0620)
2024-02-02  ZFCVINDIA   SELL ₹42.07 at stop ₹2,473.96 (+45.7%, charges ₹0.0436) — the cash goes back to work at the next Friday screen
2024-02-05  GODFRYPHLP  BUY ₹42.07 at ₹848.30 (fresh Friday signal — BUY: 10.17× weekly, month 1.74×, ladder rising; stop ₹653.92; charges ₹0.0499)
2024-02-13  APOLLO      SELL ₹65.26 at stop ₹112.10 (+47.2%, charges ₹0.0677) — the cash goes back to work at the next Friday screen
2024-02-19  PRUDENT     BUY ₹65.26 at ₹1,332.00 (fresh Friday signal — BUY: 19.33× weekly, month 4.96×, ladder rising; stop ₹1,008.17; charges ₹0.0773)
2024-02-21  JKPAPER     SELL ₹40.69 at stop ₹374.44 (+1.0%, charges ₹0.0422) — the cash goes back to work at the next Friday screen
2024-02-26  CRISIL      BUY ₹40.69 at ₹4,905.25 (fresh Friday signal — BUY: 7.72× weekly, month 2.77×, ladder rising; stop ₹4,132.60; charges ₹0.0482)
2024-03-06  SHAREINDIA  SELL ₹53.13 at stop ₹357.20 (+19.1%, charges ₹0.0551) — the cash goes back to work at the next Friday screen
2024-03-11  SOLARINDS   BUY ₹53.13 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0630)
2024-03-13  PRUDENT     SELL ₹57.49 at stop ₹1,176.05 (-11.7%, charges ₹0.0596) — the cash goes back to work at the next Friday screen
2024-03-13  RATEGAIN    SELL ₹52.57 at stop ₹730.99 (+33.6%, charges ₹0.0545) — the cash goes back to work at the next Friday screen
2024-03-13  RITES       SELL ₹47.90 at stop ₹314.37 (-8.2%, charges ₹0.0497) — the cash goes back to work at the next Friday screen
2024-03-15  OIL         SELL ₹47.45 at stop ₹344.53 (+37.1%, charges ₹0.0492) — the cash goes back to work at the next Friday screen
2024-03-18  FORCEMOT    BUY ₹67.11 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 3.03× weekly, month 1.69×, ladder rising; stop ₹5,500.61; charges ₹0.0795)
2024-03-18  INDIGO      BUY ₹67.02 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0794)
2024-03-18  JIOFIN      BUY ₹67.42 at ₹346.95 (fresh Friday signal — BUY: 2.56× weekly, month 2.25×, ladder rising; stop ₹290.75; charges ₹0.0799)
2024-03-27  ANANDRATHI  SELL ₹108.24 at stop ₹862.65 (+224.7%, charges ₹0.1123) — the cash goes back to work at the next Friday screen
2024-04-01  SHRIRAMFIN  BUY ₹61.83 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0733)
2024-04-01  TAX         FY2024 settled: ₹50.2609 paid (STCG ₹251.30 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-18  CRISIL      SELL ₹37.63 at stop ₹4,546.70 (-7.3%, charges ₹0.0390) — the cash goes back to work at the next Friday screen
2024-04-22  JUSTDIAL    BUY ₹37.63 at ₹1,084.00 (fresh Friday signal — BUY: 11.71× weekly, month 3.19×, ladder rising; stop ₹821.08; charges ₹0.0446)
2024-05-09  JUSTDIAL    SELL ₹34.91 at stop ₹1,008.00 (-7.0%, charges ₹0.0362) — the cash goes back to work at the next Friday screen
2024-05-13  JWL         BUY ₹34.91 at ₹490.00 (fresh Friday signal — BUY: 7.12× weekly, month 2.53×, ladder rising; stop ₹370.93; charges ₹0.0414)
2024-05-28  FORCEMOT    SELL ₹82.42 at stop ₹8,083.65 (+23.1%, charges ₹0.0855) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹67.90 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0805)
2024-06-04  CUPID       SELL ₹130.97 at stop ₹17.77 (+193.7%, charges ₹0.1359) — the cash goes back to work at the next Friday screen
2024-06-04  JIOFIN      SELL ₹61.58 at stop ₹317.61 (-8.5%, charges ₹0.0639) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹57.48 at stop ₹441.77 (-6.8%, charges ₹0.0596) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹55.94 at stop ₹7,980.95 (+5.5%, charges ₹0.0580) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹65.05 at ₹156.60 (fresh Friday signal — BUY: 7.81× weekly, month 1.77×, ladder rising; stop ₹126.55; charges ₹0.0771)
2024-06-10  DABUR       BUY ₹64.78 at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹0.0767)
2024-06-10  FIEMIND     BUY ₹65.26 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0773)
2024-06-10  NCC         BUY ₹60.45 at ₹327.60 (fresh Friday signal — BUY: 2.80× weekly, month 1.63×, ladder rising; stop ₹260.92; charges ₹0.0716)
2024-06-10  UNOMINDA    BUY ₹64.94 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.61×, ladder rising; stop ₹769.64; charges ₹0.0769)
2024-07-19  TDPOWERSYS  SELL ₹66.41 at stop ₹188.72 (+123.0%, charges ₹0.0689) — the cash goes back to work at the next Friday screen
2024-07-19  UNOMINDA    SELL ₹65.59 at stop ₹981.87 (+1.2%, charges ₹0.0680) — the cash goes back to work at the next Friday screen
2024-07-22  INDIAGLYCO  BUY ₹65.67 at ₹515.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.25×, ladder rising; stop ₹429.42; charges ₹0.0778)
2024-07-22  PGIL        BUY ₹65.60 at ₹405.00 (fresh Friday signal — BUY: 3.81× weekly, month 8.12×, ladder rising; stop ₹335.38; charges ₹0.0777)
2024-07-23  FIEMIND     SELL ₹62.04 at stop ₹1,257.56 (-4.7%, charges ₹0.0644) — the cash goes back to work at the next Friday screen
2024-07-23  NCC         SELL ₹54.84 at stop ₹297.87 (-9.1%, charges ₹0.0569) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹49.06 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0581)
2024-07-29  THYROCARE   BUY ₹68.54 at ₹261.67 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹196.33; charges ₹0.0812)
2024-08-06  JWL         SELL ₹39.24 at stop ₹552.00 (+12.7%, charges ₹0.0407) — the cash goes back to work at the next Friday screen
2024-08-12  ADANIPOWER  SELL ₹52.45 at stop ₹126.55 (-19.2%, charges ₹0.0544) — the cash goes back to work at the next Friday screen
2024-08-12  CERA        BUY ₹39.24 at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹0.0465)
2024-08-16  CAMPUS      SELL ₹65.64 at stop ₹277.07 (-3.1%, charges ₹0.0681) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹68.44 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.15×, ladder rising; stop ₹361.00; charges ₹0.0811)
2024-08-19  VGUARD      BUY ₹49.65 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.0588)
2024-09-09  AVANTIFEED  SELL ₹45.62 at stop ₹650.13 (-6.8%, charges ₹0.0473) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹45.62 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0541)
2024-09-19  CERA        SELL ₹30.58 at stop ₹8,198.93 (-21.9%, charges ₹0.0317) — the cash goes back to work at the next Friday screen
2024-09-23  PGIL        SELL ₹70.23 at stop ₹434.53 (+7.3%, charges ₹0.0728) — the cash goes back to work at the next Friday screen
2024-09-30  VIYASH      BUY ₹69.09 at ₹216.00 (fresh Friday signal — BUY: 5.97× weekly, month 2.57×, ladder rising; stop ₹161.73; charges ₹0.0819)
2024-10-03  DABUR       SELL ₹64.45 at stop ₹602.49 (-0.3%, charges ₹0.0669) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹39.72 at stop ₹420.24 (-19.8%, charges ₹0.0412) — the cash goes back to work at the next Friday screen
2024-10-07  BSE         BUY ₹65.26 at ₹1,396.67 (fresh Friday signal — ACCUMULATE: 2.88× weekly, month 3.26×, ladder rising; stop ₹1,131.31; charges ₹0.0773)
2024-10-07  CEMPRO      BUY ₹65.72 at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹0.0779)
2024-10-07  INDIGO      SELL ₹93.73 at stop ₹4,485.14 (+40.2%, charges ₹0.0972) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹69.36 at stop ₹265.38 (+1.4%, charges ₹0.0719) — the cash goes back to work at the next Friday screen
2024-10-14  PAYTM       BUY ₹68.82 at ₹729.60 (fresh Friday signal — BUY: 1.93× weekly, month 2.08×, ladder rising; stop ₹617.60; charges ₹0.0815)
2024-10-14  SKIPPER     BUY ₹68.47 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.80×, ladder rising; stop ₹418.00; charges ₹0.0811)
2024-10-22  GODFRYPHLP  SELL ₹103.25 at stop ₹2,086.31 (+145.9%, charges ₹0.1071) — the cash goes back to work at the next Friday screen
2024-10-23  VIYASH      SELL ₹55.16 at stop ₹172.84 (-20.0%, charges ₹0.0572) — the cash goes back to work at the next Friday screen
2024-10-25  INDIAGLYCO  SELL ₹74.80 at stop ₹587.91 (+14.2%, charges ₹0.0776) — the cash goes back to work at the next Friday screen
2024-11-04  JSWDULUX    BUY ₹64.71 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.1528)
2024-11-04  KIRLPNU     BUY ₹64.36 at ₹849.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.99×, ladder rising; stop ₹594.25; charges ₹0.1519)
2024-11-11  FSL         BUY ₹64.38 at ₹367.05 (fresh Friday signal — BUY: 1.56× weekly, month 1.99×, ladder rising; stop ₹309.80; charges ₹0.1520)
2024-11-11  MOTILALOFS  BUY ₹64.56 at ₹998.05 (fresh Friday signal — ACCUMULATE: 1.60× weekly, month 4.35×, ladder rising; stop ₹788.79; charges ₹0.1524)
2024-12-17  SUPRIYA     SELL ₹92.66 at stop ₹717.25 (+35.8%, charges ₹0.2058) — the cash goes back to work at the next Friday screen
2024-12-23  KIRLPNU     SELL ₹60.22 at stop ₹798.00 (-6.0%, charges ₹0.1338) — the cash goes back to work at the next Friday screen
2024-12-23  ZENTEC      BUY ₹66.65 at ₹2,555.00 (fresh Friday signal — BUY: 3.53× weekly, month 2.25×, ladder rising; stop ₹1,537.95; charges ₹0.1573)
2024-12-26  PRSMJOHNSN  SELL ₹36.15 at stop ₹170.55 (-20.5%, charges ₹0.0803) — the cash goes back to work at the next Friday screen
2024-12-27  JSWDULUX    SELL ₹48.81 at stop ₹3,423.18 (-24.2%, charges ₹0.1084) — the cash goes back to work at the next Friday screen
2024-12-30  KFINTECH    BUY ₹66.67 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.22×, ladder rising; stop ₹1,159.14; charges ₹0.1574)
2025-01-06  JSLL        BUY ₹45.11 at ₹2,400.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.93×, ladder rising; stop ₹2,014.22; charges ₹0.1065)
2025-01-06  LLOYDSME    BUY ₹65.29 at ₹1,439.00 (fresh Friday signal — BUY: 2.97× weekly, month 1.94×, ladder rising; stop ₹1,064.09; charges ₹0.1541)
2025-01-09  PAYTM       SELL ₹83.95 at stop ₹893.05 (+22.4%, charges ₹0.1865) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹58.89 at stop ₹477.28 (-13.7%, charges ₹0.1308) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹60.81 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 4.81×, ladder rising; stop ₹697.76; charges ₹0.1435)
2025-01-13  ZENTEC      SELL ₹57.48 at stop ₹2,213.55 (-13.4%, charges ₹0.1277) — the cash goes back to work at the next Friday screen
2025-01-15  KFINTECH    SELL ₹50.90 at stop ₹1,159.14 (-23.3%, charges ₹0.1131) — the cash goes back to work at the next Friday screen
2025-01-17  MOTILALOFS  SELL ₹50.79 at stop ₹788.79 (-21.0%, charges ₹0.1128) — the cash goes back to work at the next Friday screen
2025-01-20  APOLLO      BUY ₹61.70 at ₹131.50 (fresh Friday signal — ACCUMULATE: 1.93× weekly, month 5.79×, ladder rising; stop ₹110.19; charges ₹0.1457)
2025-01-24  AEGISLOG    SELL ₹50.79 at stop ₹700.36 (-16.1%, charges ₹0.1128) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹57.84 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.1365)
2025-01-27  JSLL        SELL ₹37.68 at stop ₹2,014.22 (-16.1%, charges ₹0.0837) — the cash goes back to work at the next Friday screen
2025-01-28  FSL         SELL ₹57.99 at stop ₹332.14 (-9.5%, charges ₹0.1288) — the cash goes back to work at the next Friday screen
2025-01-28  LLOYDSME    SELL ₹56.85 at stop ₹1,258.75 (-12.5%, charges ₹0.1263) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹58.84 at ₹947.00 (fresh Friday signal — BUY: 4.92× weekly, month 3.02×, ladder rising; stop ₹727.84; charges ₹0.1389)
2025-02-17  APOLLO      SELL ₹51.47 at stop ₹110.19 (-16.2%, charges ₹0.1143) — the cash goes back to work at the next Friday screen
2025-02-17  ZENSARTECH  SELL ₹50.36 at stop ₹814.20 (-14.0%, charges ₹0.1119) — the cash goes back to work at the next Friday screen
2025-02-28  BSE         SELL ₹76.91 at stop ₹1,651.54 (+18.2%, charges ₹0.1708) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹55.84 at ₹1,450.00 (fresh Friday signal — BUY: 4.67× weekly, month 1.70×, ladder rising; stop ₹1,235.90; charges ₹0.1318)
2025-03-24  INDIASHLTR  BUY ₹57.63 at ₹794.95 (fresh Friday signal — BUY: 4.59× weekly, month 1.56×, ladder rising; stop ₹692.55; charges ₹0.1361)
2025-04-01  TAX         FY2025 settled: ₹17.6142 paid (STCG ₹65.15 @20%, LTCG ₹36.67 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2025-04-07  INDIASHLTR  SELL ₹53.32 at stop ₹738.82 (-7.1%, charges ₹0.1184) — the cash goes back to work at the next Friday screen
2025-04-11  CEMPRO      SELL ₹52.49 at stop ₹524.92 (-19.9%, charges ₹0.1166) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹55.87 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.61× weekly, month 1.63×, ladder rising; stop ₹492.75; charges ₹0.1319)
2025-04-15  INDIASHLTR  BUY ₹55.77 at ₹865.00 (fresh Friday signal — BUY: 1.66× weekly, month 2.04×, ladder rising; stop ₹738.82; charges ₹0.1316)
2025-04-21  GALLANTT    BUY ₹57.16 at ₹474.75 (fresh Friday signal — BUY: 3.71× weekly, month 3.71×, ladder rising; stop ₹328.99; charges ₹0.1349)
2025-04-28  FORCEMOT    BUY ₹56.73 at ₹9,275.00 (fresh Friday signal — ACCUMULATE: 1.94× weekly, month 1.70×, ladder rising; stop ₹7,633.31; charges ₹0.1339)
2025-04-28  SMLMAH      BUY ₹56.55 at ₹1,680.00 (fresh Friday signal — BUY: 1.70× weekly, month 3.85×, ladder rising; stop ₹1,419.23; charges ₹0.1335)
2025-04-28  WHIRLPOOL   BUY ₹56.52 at ₹1,153.90 (fresh Friday signal — BUY: 2.17× weekly, month 1.78×, ladder rising; stop ₹1,017.54; charges ₹0.1334)
2025-05-05  PARAS       BUY ₹57.45 at ₹686.10 (fresh Friday signal — BUY: 25.11× weekly, month 4.49×, ladder rising; stop ₹486.64; charges ₹0.1356)
2025-07-28  PARAS       SELL ₹59.09 at stop ₹708.99 (+3.3%, charges ₹0.1313) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹69.57 at stop ₹1,814.78 (+25.2%, charges ₹0.1545) — the cash goes back to work at the next Friday screen
2025-08-04  PARADEEP    BUY ₹72.27 at ₹218.91 (fresh Friday signal — BUY: 5.24× weekly, month 2.97×, ladder rising; stop ₹177.27; charges ₹0.1706)
2025-08-07  WHIRLPOOL   SELL ₹63.48 at stop ₹1,301.97 (+12.8%, charges ₹0.1410) — the cash goes back to work at the next Friday screen
2025-08-11  RAIN        BUY ₹74.25 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.83×, ladder rising; stop ₹143.64; charges ₹0.1753)
2025-08-18  BLACKBUCK   BUY ₹69.17 at ₹553.00 (fresh Friday signal — ACCUMULATE: 3.19× weekly, month 5.00×, ladder rising; stop ₹473.20; charges ₹0.1633)
2025-08-26  RAIN        SELL ₹66.25 at stop ₹143.64 (-10.4%, charges ₹0.1471) — the cash goes back to work at the next Friday screen
2025-09-08  NETWEB      BUY ₹66.25 at ₹3,135.50 (fresh Friday signal — BUY: 6.14× weekly, month 4.05×, ladder rising; stop ₹2,081.16; charges ₹0.1564)
2025-09-08  PARADEEP    SELL ₹63.72 at stop ₹193.88 (-11.4%, charges ₹0.1415) — the cash goes back to work at the next Friday screen
2025-09-15  ABFRL       BUY ₹63.72 at ₹88.58 (fresh Friday signal — BUY: 1.65× weekly, month 3.17×, ladder rising; stop ₹72.61; charges ₹0.1504)
2025-09-25  INDIASHLTR  SELL ₹55.36 at stop ₹862.60 (-0.3%, charges ₹0.1230) — the cash goes back to work at the next Friday screen
2025-09-26  SMLMAH      SELL ₹109.09 at stop ₹3,255.67 (+93.8%, charges ₹0.2423) — the cash goes back to work at the next Friday screen
2025-09-29  NLCINDIA    BUY ₹70.11 at ₹280.30 (fresh Friday signal — BUY: 4.24× weekly, month 1.86×, ladder rising; stop ₹241.39; charges ₹0.1655)
2025-09-29  SUBROS      BUY ₹69.74 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.1646)
2025-10-09  FORCEMOT    SELL ₹93.45 at stop ₹15,350.10 (+65.5%, charges ₹0.2076) — the cash goes back to work at the next Friday screen
2025-10-13  ABFRL       SELL ₹58.74 at stop ₹82.04 (-7.4%, charges ₹0.1305) — the cash goes back to work at the next Friday screen
2025-10-13  SHAILY      BUY ₹69.91 at ₹2,434.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 1.99×, ladder rising; stop ₹1,942.00; charges ₹0.1650)
2025-10-13  VIYASH      BUY ₹48.15 at ₹216.04 (fresh Friday signal — BUY: 3.38× weekly, month 2.33×, ladder rising; stop ₹174.14; charges ₹0.1137)
2025-10-14  SUBROS      SELL ₹64.20 at stop ₹1,046.90 (-7.5%, charges ₹0.1426) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹67.82 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.36×, ladder rising; stop ₹1,311.00; charges ₹0.1601)
2025-10-20  CIEINDIA    BUY ₹55.13 at ₹432.50 (fresh Friday signal — ACCUMULATE: 5.23× weekly, month 2.05×, ladder rising; stop ₹377.39; charges ₹0.1301)
2025-10-20  CREDITACC   SELL ₹86.33 at stop ₹1,274.42 (+49.9%, charges ₹0.1917) — the cash goes back to work at the next Friday screen
2025-10-20  GALLANTT    SELL ₹73.88 at stop ₹616.41 (+29.8%, charges ₹0.1641) — the cash goes back to work at the next Friday screen
2025-10-28  BLACKBUCK   SELL ₹79.96 at stop ₹642.20 (+16.1%, charges ₹0.1776) — the cash goes back to work at the next Friday screen
2025-11-03  MAHABANK    BUY ₹67.38 at ₹59.70 (fresh Friday signal — ACCUMULATE: 2.08× weekly, month 1.71×, ladder rising; stop ₹53.69; charges ₹0.1591)
2025-11-03  TDPOWERSYS  BUY ₹66.94 at ₹382.27 (fresh Friday signal — BUY: 4.87× weekly, month 1.96×, ladder rising; stop ₹276.78; charges ₹0.1580)
2025-11-06  NETWEB      SELL ₹73.95 at stop ₹3,515.95 (+12.1%, charges ₹0.1642) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹67.00 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.1582)
2025-11-10  CUB         BUY ₹67.34 at ₹190.65 (fresh Friday signal — BUY: 6.02× weekly, month 1.75×, ladder rising; stop ₹160.31; charges ₹0.1590)
2025-11-10  LTF         BUY ₹45.46 at ₹304.00 (fresh Friday signal — BUY: 2.98× weekly, month 1.55×, ladder rising; stop ₹250.80; charges ₹0.1073)
2025-11-20  ANANDRATHI  SELL ₹62.18 at stop ₹1,450.17 (-7.9%, charges ₹0.1381) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹64.16 at stop ₹976.41 (-3.8%, charges ₹0.1425) — the cash goes back to work at the next Friday screen
2025-11-24  NLCINDIA    SELL ₹60.10 at stop ₹241.39 (-13.9%, charges ₹0.1335) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹62.18 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.37×, ladder rising; stop ₹2,956.50; charges ₹0.1468)
2025-11-24  TDPOWERSYS  SELL ₹62.31 at stop ₹357.49 (-6.5%, charges ₹0.1384) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹66.43 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.35×, ladder rising; stop ₹535.37; charges ₹0.1568)
2025-12-01  GMRAIRPORT  BUY ₹53.85 at ₹108.90 (fresh Friday signal — BUY: 1.69× weekly, month 1.84×, ladder rising; stop ₹89.73; charges ₹0.1271)
2025-12-01  SANSERA     BUY ₹66.30 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.61×, ladder rising; stop ₹1,413.60; charges ₹0.1565)
2025-12-15  SHAILY      SELL ₹66.93 at stop ₹2,340.80 (-3.8%, charges ₹0.1487) — the cash goes back to work at the next Friday screen
2025-12-22  KIRLOSENG   BUY ₹64.91 at ₹1,258.30 (fresh Friday signal — BUY: 4.09× weekly, month 1.72×, ladder rising; stop ₹1,014.88; charges ₹0.1532)
2026-01-08  EUREKAFORB  SELL ₹58.67 at stop ₹589.10 (-11.3%, charges ₹0.1303) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹55.63 at stop ₹2,956.50 (-10.1%, charges ₹0.1236) — the cash goes back to work at the next Friday screen
2026-01-12  KIRLOSENG   SELL ₹58.59 at stop ₹1,140.95 (-9.3%, charges ₹0.1301) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹62.82 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.57×, ladder rising; stop ₹246.34; charges ₹0.1483)
2026-01-12  VIYASH      SELL ₹43.27 at stop ₹195.04 (-9.7%, charges ₹0.0961) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹50.90 at stop ₹748.60 (-8.5%, charges ₹0.1130) — the cash goes back to work at the next Friday screen
2026-01-21  LTF         SELL ₹41.94 at stop ₹281.77 (-7.3%, charges ₹0.0932) — the cash goes back to work at the next Friday screen
2026-01-23  GMRAIRPORT  SELL ₹45.33 at stop ₹92.10 (-15.4%, charges ₹0.1007) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹63.10 at stop ₹1,672.76 (-4.4%, charges ₹0.1402) — the cash goes back to work at the next Friday screen
2026-01-27  HINDZINC    BUY ₹62.55 at ₹733.00 (fresh Friday signal — BUY: 3.59× weekly, month 3.42×, ladder rising; stop ₹602.35; charges ₹0.1477)
2026-02-02  HINDCOPPER  BUY ₹60.99 at ₹590.15 (fresh Friday signal — BUY: 2.81× weekly, month 4.41×, ladder rising; stop ₹485.74; charges ₹0.1440)
2026-02-02  HINDZINC    SELL ₹51.17 at stop ₹602.35 (-17.8%, charges ₹0.1136) — the cash goes back to work at the next Friday screen
2026-02-17  NATIONALUM  SELL ₹59.60 at stop ₹335.49 (-4.7%, charges ₹0.1324) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹62.00 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.69×, ladder rising; stop ₹5,440.18; charges ₹0.1464)
2026-03-02  KSB         BUY ₹61.57 at ₹738.00 (fresh Friday signal — BUY: 52.86× weekly, month 4.80×, ladder rising; stop ₹658.54; charges ₹0.1454)
2026-03-02  TORNTPOWER  BUY ₹61.58 at ₹1,491.00 (fresh Friday signal — BUY: 1.57× weekly, month 1.71×, ladder rising; stop ₹1,315.84; charges ₹0.1454)
2026-03-09  CUB         SELL ₹66.30 at stop ₹188.57 (-1.1%, charges ₹0.1473) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹54.39 at stop ₹528.63 (-10.4%, charges ₹0.1208) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹58.55 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.1382)
2026-03-30  MAHABANK    SELL ₹68.58 at stop ₹61.05 (+2.3%, charges ₹0.1523) — the cash goes back to work at the next Friday screen
2026-03-30  TORNTPOWER  SELL ₹54.10 at stop ₹1,315.84 (-11.7%, charges ₹0.1202) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹7.9809 paid (STCG ₹39.90 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹58.31 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.66×, ladder rising; stop ₹891.29; charges ₹0.1376)
2026-04-13  INOXINDIA   BUY ₹59.94 at ₹1,299.10 (fresh Friday signal — BUY: 4.08× weekly, month 2.14×, ladder rising; stop ₹1,091.46; charges ₹0.1415)
2026-04-13  THERMAX     BUY ₹60.44 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.1427)
2026-04-20  GALLANTT    BUY ₹63.07 at ₹862.10 (fresh Friday signal — BUY: 15.07× weekly, month 24.00×, ladder rising; stop ₹612.75; charges ₹0.1489)
2026-04-20  NLCINDIA    BUY ₹63.11 at ₹303.60 (fresh Friday signal — BUY: 5.54× weekly, month 2.42×, ladder rising; stop ₹248.05; charges ₹0.1490)
2026-05-04  KSB         SELL ₹76.19 at stop ₹917.42 (+24.3%, charges ₹0.1692) — the cash goes back to work at the next Friday screen
2026-05-11  CRAFTSMAN   BUY ₹63.19 at ₹9,039.50 (fresh Friday signal — BUY: 22.97× weekly, month 3.93×, ladder rising; stop ₹7,119.77; charges ₹0.1492)
2026-05-11  WOCKPHARMA  BUY ₹43.66 at ₹1,613.90 (fresh Friday signal — BUY: 16.73× weekly, month 2.98×, ladder rising; stop ₹1,312.90; charges ₹0.1031)
2026-05-13  INOXINDIA   SELL ₹63.02 at stop ₹1,372.18 (+5.6%, charges ₹0.1400) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹57.03 at stop ₹1,125.84 (-2.1%, charges ₹0.1267) — the cash goes back to work at the next Friday screen
2026-05-14  GALLANTT    SELL ₹57.08 at stop ₹783.75 (-9.1%, charges ₹0.1268) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹60.52 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.24×, ladder rising; stop ₹1,502.04; charges ₹0.1429)
2026-05-18  CAPLIPOINT  BUY ₹60.51 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.1428)
2026-05-18  DIACABS     BUY ₹56.10 at ₹196.45 (fresh Friday signal — BUY: 4.25× weekly, month 2.41×, ladder rising; stop ₹159.66; charges ₹0.1324)
2026-06-09  NLCINDIA    SELL ₹66.34 at stop ₹320.62 (+5.6%, charges ₹0.1474) — the cash goes back to work at the next Friday screen
2026-06-11  CIEINDIA    SELL ₹54.55 at stop ₹429.88 (-0.6%, charges ₹0.1212) — the cash goes back to work at the next Friday screen
2026-06-15  AEGISLOG    BUY ₹65.57 at ₹954.95 (fresh Friday signal — BUY: 14.40× weekly, month 5.74×, ladder rising; stop ₹710.17; charges ₹0.1548)
2026-06-15  SFL         BUY ₹55.32 at ₹724.95 (fresh Friday signal — BUY: 2.17× weekly, month 4.31×, ladder rising; stop ₹542.50; charges ₹0.1306)
2026-07-29  THERMAX     SELL ₹72.06 at stop ₹4,306.63 (+19.8%, charges ₹0.1601) — the cash goes back to work at the next Friday screen
2026-08-03  TMB         BUY ₹72.06 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.57×, ladder rising; stop ₹748.60; charges ₹0.1701)
2026-08-06  SFL         SELL ₹53.07 at stop ₹698.73 (-3.6%, charges ₹0.1179) — the cash goes back to work at the next Friday screen
2026-08-10  VARROC      BUY ₹53.07 at ₹804.00 (fresh Friday signal — BUY: 26.81× weekly, month 4.71×, ladder rising; stop ₹599.50; charges ₹0.1253)
2026-09-10  ALKYLAMINE  SELL ₹67.68 at stop ₹1,920.99 (+12.3%, charges ₹0.1503) — the cash goes back to work at the next Friday screen
```
