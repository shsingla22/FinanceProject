# The Darvas screen, run for six years — 2020-06-01 → 2026-09-11

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-11, 1374 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-13/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹351.42** | **+22.21% a year** |
| The same system before costs and taxes | ₹444.83 | +26.89% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹230.70 | +14.27% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.40 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹351.02** (+22.18% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.27 years, 328 weekly screens, 401 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹14.91** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹45.60**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹9.82 | ₹0.00 | ₹1.9639 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹49.18 | ₹0.00 | ₹9.8353 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹42.34 | ₹40.83 | ₹13.5708 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹101.16 | ₹0.00 | ₹20.2312 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹5.87 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹2.94 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹2.02 | ₹0.00 | ₹0.4050 | ₹0.00 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 117.33 | +17.3% | +17.9% | +35.6% |
| 2021 (2021-12-31) | 204.71 | +74.5% | +71.9% | +26.2% |
| 2022 (2022-12-30) | 247.12 | +20.7% | +30.3% | +4.3% |
| 2023 (2023-12-29) | 336.70 | +36.2% | +45.4% | +20.0% |
| 2024 (2024-12-27) | 340.61 | +1.2% | +8.0% | +9.6% |
| 2025 (2025-12-26) | 323.19 | -5.1% | -3.3% | +9.4% |
| 2026 (2026-09-11) | 351.42 | +8.7% | +10.9% | -10.2% |

## What it took to earn it

- **Maximum drawdown: -27.5%** (peak 2024-07-05 → trough 2026-04-02, on weekly closes).
- **193 closed trades**: 79 winners (41%), average winner +36.6%, average loser -11.0%.
- Best closed trade BIGBLOC +258.3%; worst COMPINFO -35.4%.
- Median holding period 63 days.
- Cash share of equity averaged 11% across all weeks (median 4%); the portfolio sat FULLY in cash for 1 of 328 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-06-26 | 102.85 | 0.00 | 10 |
| 2020-07-31 | 100.98 | 8.44 | 9 |
| 2020-08-28 | 110.37 | 0.78 | 10 |
| 2020-09-25 | 103.03 | 32.07 | 6 |
| 2020-10-30 | 98.36 | 0.98 | 9 |
| 2020-11-27 | 101.15 | 0.00 | 10 |
| 2020-12-24 | 117.33 | 10.46 | 9 |
| 2021-01-29 | 117.31 | 28.59 | 8 |
| 2021-02-26 | 125.15 | 15.31 | 9 |
| 2021-03-26 | 126.48 | 13.47 | 9 |
| 2021-04-30 | 132.30 | 5.78 | 9 |
| 2021-05-28 | 143.04 | 5.78 | 9 |
| 2021-06-25 | 153.90 | 1.94 | 9 |
| 2021-07-30 | 183.87 | 1.94 | 9 |
| 2021-08-27 | 174.61 | 0.00 | 9 |
| 2021-09-24 | 169.14 | 20.02 | 8 |
| 2021-10-29 | 171.99 | 33.99 | 7 |
| 2021-11-26 | 209.55 | 55.25 | 7 |
| 2021-12-31 | 204.71 | 0.00 | 10 |
| 2022-01-28 | 206.16 | 40.51 | 8 |
| 2022-02-25 | 189.78 | 77.78 | 5 |
| 2022-03-25 | 202.70 | 17.93 | 8 |
| 2022-04-29 | 213.20 | 23.52 | 7 |
| 2022-05-27 | 217.60 | 0.00 | 8 |
| 2022-06-24 | 213.55 | 31.30 | 7 |
| 2022-07-29 | 230.53 | 9.84 | 8 |
| 2022-08-26 | 240.10 | 0.00 | 9 |
| 2022-09-30 | 237.16 | 44.60 | 7 |
| 2022-10-28 | 243.29 | 0.00 | 9 |
| 2022-11-25 | 258.99 | 0.00 | 9 |
| 2022-12-30 | 247.12 | 89.26 | 6 |
| 2023-01-27 | 243.08 | 0.00 | 10 |
| 2023-02-24 | 244.77 | 0.00 | 10 |
| 2023-03-31 | 232.87 | 78.19 | 7 |
| 2023-04-28 | 231.63 | 42.17 | 8 |
| 2023-05-26 | 236.00 | 0.00 | 10 |
| 2023-06-30 | 241.32 | 0.00 | 10 |
| 2023-07-28 | 256.71 | 0.60 | 10 |
| 2023-08-25 | 280.75 | 0.60 | 10 |
| 2023-09-29 | 289.34 | 26.35 | 9 |
| 2023-10-27 | 289.37 | 74.30 | 7 |
| 2023-11-24 | 322.60 | 3.60 | 10 |
| 2023-12-29 | 336.70 | 0.00 | 10 |
| 2024-01-25 | 353.05 | 13.74 | 10 |
| 2024-02-23 | 374.67 | 5.90 | 10 |
| 2024-03-28 | 365.79 | 95.39 | 8 |
| 2024-04-26 | 367.26 | 5.55 | 10 |
| 2024-05-31 | 362.59 | 81.36 | 8 |
| 2024-06-28 | 368.39 | 7.51 | 10 |
| 2024-07-26 | 370.52 | 40.64 | 9 |
| 2024-08-30 | 371.56 | 7.01 | 10 |
| 2024-09-27 | 371.40 | 0.00 | 10 |
| 2024-10-25 | 334.13 | 140.74 | 7 |
| 2024-11-29 | 355.96 | 0.00 | 11 |
| 2024-12-27 | 340.61 | 72.24 | 9 |
| 2025-01-31 | 308.35 | 189.33 | 4 |
| 2025-02-28 | 291.39 | 189.81 | 4 |
| 2025-03-27 | 311.79 | 122.54 | 6 |
| 2025-04-25 | 313.93 | 113.39 | 6 |
| 2025-05-30 | 328.09 | 0.00 | 10 |
| 2025-06-27 | 346.66 | 0.00 | 10 |
| 2025-07-25 | 354.56 | 0.00 | 10 |
| 2025-08-29 | 343.07 | 36.80 | 9 |
| 2025-09-26 | 328.73 | 64.49 | 8 |
| 2025-10-31 | 317.38 | 12.41 | 11 |
| 2025-11-28 | 325.08 | 61.54 | 9 |
| 2025-12-26 | 323.19 | 18.61 | 10 |
| 2026-01-30 | 313.08 | 167.31 | 5 |
| 2026-02-27 | 297.00 | 75.64 | 8 |
| 2026-03-27 | 282.96 | 138.28 | 6 |
| 2026-04-30 | 306.70 | 8.14 | 10 |
| 2026-05-29 | 318.49 | 11.90 | 10 |
| 2026-06-25 | 314.93 | 0.89 | 10 |
| 2026-07-31 | 325.39 | 35.66 | 9 |
| 2026-08-28 | 341.58 | 0.00 | 10 |
| 2026-09-11 | 351.42 | 32.62 | 9 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| ABB | 2026-02-23 | 6,090.00 | 7,274.00 | 7,158.25 | +19.4% |
| ASKAUTOLTD | 2026-08-10 | 648.95 | 624.55 | 598.78 | -3.8% |
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,754.90 | 2,376.52 | +38.4% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,572.90 | 1,242.60 | +59.0% |
| CRAFTSMAN | 2026-05-11 | 9,039.50 | 11,669.00 | 10,380.65 | +29.1% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| RUBICON | 2026-06-08 | 1,190.00 | 1,835.40 | 1,653.47 | +54.2% |
| STRTECH | 2020-06-08 | 112.00 | 151.30 | 140.17 | +35.1% |
| TMB | 2026-08-03 | 864.90 | 910.90 | 796.29 | +5.3% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| EIHAHOTELS | 2020-06-08 | 137.50 | 2020-06-16 | 110.67 | -19.5% |
| HATHWAY | 2020-06-22 | 34.80 | 2020-06-29 | 31.40 | -9.8% |
| WENDT | 2020-06-08 | 2,456.00 | 2020-07-07 | 2,047.46 | -16.6% |
| MANGCHEFER | 2020-06-08 | 38.75 | 2020-07-31 | 33.73 | -13.0% |
| EIDPARRY | 2020-06-08 | 219.00 | 2020-08-17 | 273.03 | +24.7% |
| APCOTEXIND | 2020-08-24 | 164.95 | 2020-08-31 | 151.95 | -7.9% |
| KIRLOSBROS | 2020-06-08 | 106.50 | 2020-09-08 | 120.79 | +13.4% |
| BDL | 2020-07-06 | 192.10 | 2020-09-08 | 168.93 | -12.1% |
| RCF | 2020-06-08 | 45.20 | 2020-09-09 | 45.84 | +1.4% |
| SUNFLAG | 2020-06-08 | 43.00 | 2020-09-22 | 39.67 | -7.7% |
| TAJGVK | 2020-06-08 | 174.00 | 2020-09-22 | 126.45 | -27.3% |
| HAL | 2020-07-13 | 475.00 | 2020-09-22 | 390.57 | -17.8% |
| SATIA | 2020-09-14 | 122.00 | 2020-09-22 | 102.97 | -15.6% |
| ALEMBICLTD | 2020-06-08 | 56.40 | 2020-11-02 | 91.41 | +62.1% |
| GLAXO | 2020-09-14 | 1,675.00 | 2020-11-02 | 1,441.55 | -13.9% |
| KPITTECH | 2020-09-28 | 113.60 | 2020-11-02 | 93.15 | -18.0% |
| ADVENZYMES | 2020-08-03 | 194.00 | 2020-11-03 | 292.33 | +50.7% |
| TCI | 2020-09-14 | 242.00 | 2020-12-22 | 234.75 | -3.0% |
| PILANIINVS | 2020-11-17 | 2,054.50 | 2021-01-04 | 2,132.80 | +3.8% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| TRENT | 2020-11-17 | 503.33 | 2021-01-29 | 417.53 | -17.0% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| JINDWORLD | 2020-11-09 | 50.00 | 2021-03-01 | 52.12 | +4.2% |
| RCF | 2021-03-01 | 80.00 | 2021-03-17 | 79.16 | -1.1% |
| APTECHT | 2021-02-01 | 178.45 | 2021-03-19 | 204.25 | +14.5% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| KKCL | 2021-01-11 | 985.00 | 2021-03-30 | 856.90 | -13.0% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| CENTRUM | 2021-03-30 | 28.40 | 2021-04-12 | 24.89 | -12.4% |
| AUBANK | 2021-04-05 | 631.00 | 2021-04-12 | 533.06 | -15.5% |
| GFLLIMITED | 2021-03-22 | 93.00 | 2021-04-13 | 74.39 | -20.0% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| KIRLFER | 2020-11-17 | 97.00 | 2021-08-10 | 279.49 | +188.1% |
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
| TVTODAY | 2021-11-22 | 320.24 | 2022-01-24 | 311.68 | -2.7% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| TV18BRDCST | 2022-01-31 | 58.90 | 2022-02-22 | 58.38 | -0.9% |
| CHAMBLFERT | 2021-12-06 | 407.45 | 2022-02-24 | 353.85 | -13.2% |
| COMPINFO | 2022-01-10 | 45.00 | 2022-02-24 | 29.08 | -35.4% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| EXCELINDUS | 2022-03-07 | 1,523.00 | 2022-03-29 | 1,438.30 | -5.6% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| RCF | 2022-04-04 | 96.40 | 2022-05-04 | 93.15 | -3.4% |
| MFL | 2022-05-02 | 1,430.00 | 2022-05-11 | 1,225.50 | -14.3% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| JSWENERGY | 2021-03-08 | 81.85 | 2022-06-20 | 201.99 | +146.8% |
| JKIL | 2022-05-09 | 229.70 | 2022-08-05 | 308.80 | +34.4% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| NAVNETEDUL | 2022-08-08 | 130.50 | 2022-09-26 | 127.30 | -2.5% |
| TVSSRICHAK | 2022-08-08 | 2,242.10 | 2022-09-26 | 2,432.24 | +8.5% |
| SUNDARMHLD | 2022-10-03 | 103.50 | 2022-10-11 | 92.20 | -10.9% |
| FAIRCHEMOR | 2022-10-17 | 2,240.00 | 2022-11-01 | 1,790.15 | -20.1% |
| APARINDS | 2022-06-27 | 1,004.00 | 2022-11-03 | 1,358.50 | +35.3% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| RVNL | 2022-11-07 | 46.85 | 2022-12-26 | 60.57 | +29.3% |
| GICRE | 2023-01-02 | 179.20 | 2023-02-01 | 167.72 | -6.4% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| SUNFLAG | 2023-01-02 | 113.00 | 2023-02-27 | 129.20 | +14.3% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| IOB | 2023-01-02 | 32.40 | 2023-03-20 | 22.18 | -31.5% |
| JINDALSAW | 2023-02-06 | 65.22 | 2023-03-27 | 67.92 | +4.1% |
| WONDERLA | 2023-03-06 | 456.00 | 2023-03-27 | 384.27 | -15.7% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| KIRLOSBROS | 2023-04-10 | 425.00 | 2023-04-26 | 403.85 | -5.0% |
| MUKANDLTD | 2023-01-02 | 136.70 | 2023-05-17 | 116.23 | -15.0% |
| FAIRCHEMOR | 2023-05-02 | 1,272.00 | 2023-05-19 | 1,141.04 | -10.3% |
| ANURAS | 2023-03-27 | 867.00 | 2023-07-03 | 1,007.67 | +16.2% |
| KSB | 2023-03-27 | 417.98 | 2023-07-12 | 407.74 | -2.4% |
| NEULANDLAB | 2023-05-22 | 2,831.90 | 2023-09-13 | 3,457.30 | +22.1% |
| KIRLOSIND | 2023-04-10 | 2,724.00 | 2023-09-25 | 3,202.97 | +17.6% |
| SJVN | 2023-09-18 | 75.35 | 2023-10-23 | 66.03 | -12.4% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| SHARDAMOTR | 2023-05-22 | 380.00 | 2023-10-25 | 465.07 | +22.4% |
| GENUSPOWER | 2023-07-10 | 162.85 | 2023-11-16 | 234.03 | +43.7% |
| ISMTLTD | 2023-11-20 | 94.60 | 2023-12-20 | 88.35 | -6.6% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| MMFL | 2023-12-26 | 1,023.60 | 2024-01-30 | 912.05 | -10.9% |
| GLS | 2023-05-02 | 509.05 | 2024-03-05 | 779.48 | +53.1% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| TCI | 2024-02-05 | 987.60 | 2024-03-11 | 790.40 | -20.0% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| DOLLAR | 2024-03-11 | 527.95 | 2024-03-13 | 461.65 | -12.6% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| ANANDRATHI | 2023-07-17 | 265.70 | 2024-03-27 | 862.65 | +224.7% |
| PILANIINVS | 2023-10-03 | 2,380.05 | 2024-05-09 | 3,710.37 | +55.9% |
| JSWHL | 2022-10-03 | 4,261.60 | 2024-05-13 | 6,280.45 | +47.4% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| DMART | 2024-04-01 | 4,570.00 | 2024-05-31 | 4,322.83 | -5.4% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| BOSCHLTD | 2024-03-18 | 29,500.05 | 2024-06-04 | 29,015.09 | -1.6% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| KIRLOSBROS | 2024-05-21 | 1,844.00 | 2024-08-05 | 1,987.46 | +7.8% |
| THERMAX | 2024-06-03 | 5,640.00 | 2024-08-05 | 4,719.70 | -16.3% |
| JWL | 2024-05-13 | 490.00 | 2024-08-06 | 552.00 | +12.7% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| CERA | 2024-08-12 | 10,499.95 | 2024-09-19 | 8,198.93 | -21.9% |
| DABUR | 2024-06-10 | 604.20 | 2024-10-03 | 602.49 | -0.3% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| PCBL | 2024-08-12 | 393.00 | 2024-10-18 | 476.85 | +21.3% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| ALKYLAMINE | 2024-09-23 | 2,432.85 | 2024-10-22 | 2,106.24 | -13.4% |
| INDIAGLYCO | 2024-07-22 | 515.00 | 2024-10-25 | 587.91 | +14.2% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| GOPAL | 2024-10-21 | 473.05 | 2024-12-12 | 416.05 | -12.0% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| KIRLPNU | 2024-11-04 | 1,698.00 | 2024-12-23 | 1,596.00 | -6.0% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| PAYTM | 2024-10-28 | 747.70 | 2025-01-09 | 893.05 | +19.4% |
| GARFIBRES | 2024-11-25 | 956.00 | 2025-01-09 | 829.35 | -13.2% |
| SWANENERGY | 2024-12-16 | 781.90 | 2025-01-09 | 671.32 | -14.1% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| CARERATING | 2024-10-28 | 1,396.00 | 2025-01-13 | 1,239.70 | -11.2% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| MOTILALOFS | 2024-10-21 | 1,021.95 | 2025-01-17 | 788.79 | -22.8% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| AVANTIFEED | 2025-03-17 | 842.55 | 2025-04-07 | 648.95 | -23.0% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
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

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-06-01_to_2026-09-11.csv` beside this report (2161 events in all).*

```
2020-06-08  ALEMBICLTD  BUY ₹9.70 at ₹56.40 (fresh Friday signal — ACCUMULATE: 2.95× weekly, month 2.79×, ladder rising; stop ₹44.84; charges ₹0.0115)
2020-06-08  EIDPARRY    BUY ₹9.80 at ₹219.00 (fresh Friday signal — BUY: 4.34× weekly, month 3.58×, ladder rising; stop ₹132.60; charges ₹0.0116)
2020-06-08  EIHAHOTELS  BUY ₹9.76 at ₹137.50 (fresh Friday signal — BUY: 3.47× weekly, month 7.29×, ladder rising; stop ₹110.67; charges ₹0.0116)
2020-06-08  KIRLOSBROS  BUY ₹9.70 at ₹106.50 (fresh Friday signal — ACCUMULATE: 2.95× weekly, month 1.69×, ladder rising; stop ₹91.63; charges ₹0.0115)
2020-06-08  MANGCHEFER  BUY ₹9.72 at ₹38.75 (fresh Friday signal — BUY: 2.14× weekly, month 1.72×, ladder rising; stop ₹30.64; charges ₹0.0115)
2020-06-08  RCF         BUY ₹9.73 at ₹45.20 (fresh Friday signal — BUY: 2.38× weekly, month 2.28×, ladder rising; stop ₹35.25; charges ₹0.0115)
2020-06-08  STRTECH     BUY ₹9.76 at ₹112.00 (fresh Friday signal — BUY: 2.56× weekly, month 1.57×, ladder rising; stop ₹89.21; charges ₹0.0116)
2020-06-08  SUNFLAG     BUY ₹9.92 at ₹43.00 (fresh Friday signal — BUY: 5.47× weekly, month 2.36×, ladder rising; stop ₹24.38; charges ₹0.0118)
2020-06-08  TAJGVK      BUY ₹9.67 at ₹174.00 (fresh Friday signal — BUY: 1.90× weekly, month 1.62×, ladder rising; stop ₹107.73; charges ₹0.0115)
2020-06-08  WENDT       BUY ₹10.00 at ₹2,456.00 (fresh Friday signal — BUY: 21.78× weekly, month 4.65×, ladder rising; stop ₹1,457.89; charges ₹0.0118)
2020-06-16  EIHAHOTELS  SELL ₹7.84 at stop ₹110.67 (-19.5%, charges ₹0.0081) — the cash goes back to work at the next Friday screen
2020-06-22  HATHWAY     BUY ₹10.08 at ₹34.80 (fresh Friday signal — BUY: 9.17× weekly, month 6.59×, ladder rising; stop ₹19.97; charges ₹0.0119)
2020-06-29  HATHWAY     SELL ₹9.07 at stop ₹31.40 (-9.8%, charges ₹0.0094) — the cash goes back to work at the next Friday screen
2020-07-06  BDL         BUY ₹9.07 at ₹192.10 (fresh Friday signal — BUY: 20.22× weekly, month 9.90×, ladder rising; stop ₹123.59; charges ₹0.0108)
2020-07-07  WENDT       SELL ₹8.32 at stop ₹2,047.46 (-16.6%, charges ₹0.0086) — the cash goes back to work at the next Friday screen
2020-07-13  HAL         BUY ₹8.32 at ₹475.00 (fresh Friday signal — BUY: 16.26× weekly, month 17.08×, ladder rising; stop ₹358.48; charges ₹0.0099)
2020-07-31  MANGCHEFER  SELL ₹8.44 at stop ₹33.73 (-13.0%, charges ₹0.0088) — the cash goes back to work at the next Friday screen
2020-08-03  ADVENZYMES  BUY ₹8.44 at ₹194.00 (fresh Friday signal — BUY: 4.31× weekly, month 2.51×, ladder rising; stop ₹149.98; charges ₹0.0100)
2020-08-17  EIDPARRY    SELL ₹12.19 at stop ₹273.03 (+24.7%, charges ₹0.0126) — the cash goes back to work at the next Friday screen
2020-08-24  APCOTEXIND  BUY ₹11.41 at ₹164.95 (fresh Friday signal — BUY: 8.08× weekly, month 5.83×, ladder rising; stop ₹119.51; charges ₹0.0135)
2020-08-31  APCOTEXIND  SELL ₹10.49 at stop ₹151.95 (-7.9%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹10.79 at ₹1,398.95 (fresh Friday signal — BUY: 5.36× weekly, month 3.91×, ladder rising; stop ₹1,211.25; charges ₹0.0128)
2020-09-08  BDL         SELL ₹7.96 at stop ₹168.93 (-12.1%, charges ₹0.0083) — the cash goes back to work at the next Friday screen
2020-09-08  KIRLOSBROS  SELL ₹10.98 at stop ₹120.79 (+13.4%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2020-09-09  RCF         SELL ₹9.85 at stop ₹45.84 (+1.4%, charges ₹0.0102) — the cash goes back to work at the next Friday screen
2020-09-14  GLAXO       BUY ₹7.65 at ₹1,675.00 (fresh Friday signal — BUY: 2.58× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.0091)
2020-09-14  SATIA       BUY ₹10.81 at ₹122.00 (fresh Friday signal — ACCUMULATE: 2.86× weekly, month 6.16×, ladder rising; stop ₹102.97; charges ₹0.0128)
2020-09-14  TCI         BUY ₹10.81 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.76× weekly, month 3.77×, ladder rising; stop ₹190.07; charges ₹0.0128)
2020-09-22  HAL         SELL ₹6.82 at stop ₹390.57 (-17.8%, charges ₹0.0071) — the cash goes back to work at the next Friday screen
2020-09-22  SATIA       SELL ₹9.10 at stop ₹102.97 (-15.6%, charges ₹0.0094) — the cash goes back to work at the next Friday screen
2020-09-22  SUNFLAG     SELL ₹9.13 at stop ₹39.67 (-7.7%, charges ₹0.0095) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹7.01 at stop ₹126.45 (-27.3%, charges ₹0.0073) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹10.36 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0123)
2020-09-28  KPITTECH    BUY ₹10.35 at ₹113.60 (fresh Friday signal — ACCUMULATE: 2.60× weekly, month 3.04×, ladder rising; stop ₹93.15; charges ₹0.0123)
2020-09-28  SAKSOFT     BUY ₹10.38 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.0123)
2020-11-02  ALEMBICLTD  SELL ₹15.69 at stop ₹91.41 (+62.1%, charges ₹0.0163) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹6.57 at stop ₹1,441.55 (-13.9%, charges ₹0.0068) — the cash goes back to work at the next Friday screen
2020-11-02  KPITTECH    SELL ₹8.47 at stop ₹93.15 (-18.0%, charges ₹0.0088) — the cash goes back to work at the next Friday screen
2020-11-03  ADVENZYMES  SELL ₹12.69 at stop ₹292.33 (+50.7%, charges ₹0.0132) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹9.70 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.0115)
2020-11-09  JINDWORLD   BUY ₹9.71 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.28× weekly, month 1.55×, ladder rising; stop ₹39.81; charges ₹0.0115)
2020-11-17  KIRLFER     BUY ₹5.15 at ₹97.00 (fresh Friday signal — ACCUMULATE: 2.24× weekly, month 3.73×, ladder rising; stop ₹85.97; charges ₹0.0061)
2020-11-17  PILANIINVS  BUY ₹9.91 at ₹2,054.50 (fresh Friday signal — ACCUMULATE: 3.04× weekly, month 1.77×, ladder rising; stop ₹1,752.75; charges ₹0.0117)
2020-11-17  TRENT       BUY ₹9.93 at ₹503.33 (fresh Friday signal — ACCUMULATE: 3.30× weekly, month 1.95×, ladder rising; stop ₹367.93; charges ₹0.0118)
2020-12-22  TCI         SELL ₹10.46 at stop ₹234.75 (-3.0%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2020-12-28  PAISALO     BUY ₹10.46 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0124)
2021-01-04  PILANIINVS  SELL ₹10.27 at stop ₹2,132.80 (+3.8%, charges ₹0.0106) — the cash goes back to work at the next Friday screen
2021-01-11  KKCL        BUY ₹10.27 at ₹985.00 (fresh Friday signal — BUY: 9.34× weekly, month 2.08×, ladder rising; stop ₹748.60; charges ₹0.0122)
2021-01-20  BORORENEW   SELL ₹24.03 at stop ₹247.59 (+148.3%, charges ₹0.0249) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹11.92 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.79×, ladder rising; stop ₹92.41; charges ₹0.0141)
2021-01-25  MAHLOG      BUY ₹12.04 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹0.0143)
2021-01-25  SAKSOFT     SELL ₹8.86 at stop ₹341.10 (-14.4%, charges ₹0.0092) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹11.44 at stop ₹928.05 (+10.7%, charges ₹0.0119) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹8.22 at stop ₹417.53 (-17.0%, charges ₹0.0085) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹11.79 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.0140)
2021-02-01  GAEL        BUY ₹11.91 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.71× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.0141)
2021-02-23  GAEL        SELL ₹10.43 at stop ₹62.70 (-12.3%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2021-03-01  JINDWORLD   SELL ₹10.10 at stop ₹52.12 (+4.2%, charges ₹0.0105) — the cash goes back to work at the next Friday screen
2021-03-01  RCF         BUY ₹12.62 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.13×, ladder rising; stop ₹50.16; charges ₹0.0150)
2021-03-08  JSWENERGY   BUY ₹12.71 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.50×, ladder rising; stop ₹65.79; charges ₹0.0151)
2021-03-17  RCF         SELL ₹12.46 at stop ₹79.16 (-1.1%, charges ₹0.0129) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹13.46 at stop ₹204.25 (+14.5%, charges ₹0.0140) — the cash goes back to work at the next Friday screen
2021-03-22  GFLLIMITED  BUY ₹12.40 at ₹93.00 (fresh Friday signal — ACCUMULATE: 6.17× weekly, month 3.98×, ladder rising; stop ₹74.39; charges ₹0.0147)
2021-03-22  VIDHIING    BUY ₹12.34 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0146)
2021-03-25  BANARISUG   SELL ₹12.20 at stop ₹1,586.36 (+13.4%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2021-03-30  CENTRUM     BUY ₹12.66 at ₹28.40 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 6.70×, ladder rising; stop ₹24.89; charges ₹0.0150)
2021-03-30  KKCL        SELL ₹8.91 at stop ₹856.90 (-13.0%, charges ₹0.0092) — the cash goes back to work at the next Friday screen
2021-04-01  TAX         FY2021 settled: ₹1.9639 paid (STCG ₹9.82 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-05  AUBANK      BUY ₹7.75 at ₹631.00 (fresh Friday signal — ACCUMULATE: 3.80× weekly, month 2.03×, ladder rising; stop ₹533.06; charges ₹0.0092)
2021-04-12  AUBANK      SELL ₹6.53 at stop ₹533.06 (-15.5%, charges ₹0.0068) — the cash goes back to work at the next Friday screen
2021-04-12  CENTRUM     SELL ₹11.07 at stop ₹24.89 (-12.4%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹13.27 at stop ₹72.41 (+27.1%, charges ₹0.0138) — the cash goes back to work at the next Friday screen
2021-04-13  GFLLIMITED  SELL ₹9.90 at stop ₹74.39 (-20.0%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2021-04-19  EMAMIPAP    BUY ₹11.70 at ₹125.00 (fresh Friday signal — ACCUMULATE: 2.31× weekly, month 22.17×, ladder rising; stop ₹81.22; charges ₹0.0139)
2021-04-19  KPRMILL     BUY ₹11.64 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0138)
2021-04-19  MOREPENLAB  BUY ₹11.65 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹0.0138)
2021-06-18  VIDHIING    SELL ₹11.55 at stop ₹182.64 (-6.2%, charges ₹0.0120) — the cash goes back to work at the next Friday screen
2021-06-21  SOMANYCERA  BUY ₹15.39 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0182)
2021-08-10  KIRLFER     SELL ₹14.79 at stop ₹279.49 (+188.1%, charges ₹0.0153) — the cash goes back to work at the next Friday screen
2021-08-10  MOREPENLAB  SELL ₹17.49 at stop ₹56.33 (+50.4%, charges ₹0.0181) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹17.35 at stop ₹352.48 (+49.4%, charges ₹0.0180) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹17.81 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.0211)
2021-08-16  INDOCO      BUY ₹15.96 at ₹484.30 (fresh Friday signal — BUY: 4.80× weekly, month 2.73×, ladder rising; stop ₹412.30; charges ₹0.0189)
2021-08-16  TATAINVEST  BUY ₹17.80 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0211)
2021-09-20  GDL         SELL ₹20.02 at stop ₹266.00 (+68.4%, charges ₹0.0208) — the cash goes back to work at the next Friday screen
2021-09-27  NEOGEN      BUY ₹17.32 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0205)
2021-10-25  BASF        SELL ₹15.56 at stop ₹3,220.59 (-12.5%, charges ₹0.0161) — the cash goes back to work at the next Friday screen
2021-10-25  NEOGEN      SELL ₹15.73 at stop ₹1,142.85 (-8.9%, charges ₹0.0163) — the cash goes back to work at the next Friday screen
2021-11-01  TCIEXP      BUY ₹16.84 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0200)
2021-11-01  TTKPRESTIG  BUY ₹17.15 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.0203)
2021-11-12  INDOCO      SELL ₹13.56 at stop ₹412.30 (-14.9%, charges ₹0.0141) — the cash goes back to work at the next Friday screen
2021-11-15  BIGBLOC     BUY ₹13.56 at ₹39.80 (fresh Friday signal — BUY: 6.89× weekly, month 4.00×, ladder rising; stop ₹142.59; charges ₹0.0161)
2021-11-16  BIGBLOC     SELL ₹48.46 at stop ₹142.59 (+258.3%, charges ₹0.0503) — the cash goes back to work at the next Friday screen
2021-11-22  EMAMIPAP    SELL ₹13.22 at stop ₹141.55 (+13.2%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2021-11-22  SUPRAJIT    BUY ₹20.70 at ₹454.00 (fresh Friday signal — BUY: 10.19× weekly, month 1.96×, ladder rising; stop ₹309.33; charges ₹0.0245)
2021-11-22  TVTODAY     BUY ₹20.84 at ₹320.24 (fresh Friday signal — BUY: 15.58× weekly, month 3.55×, ladder rising; stop ₹253.08; charges ₹0.0247)
2021-11-26  TATAINVEST  SELL ₹19.50 at stop ₹1,436.49 (+9.8%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹15.61 at stop ₹10,070.05 (-8.8%, charges ₹0.0162) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹14.25 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.0169)
2021-11-29  RAYMOND     BUY ₹20.45 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0242)
2021-11-29  RSYSTEMS    BUY ₹20.56 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0244)
2021-11-29  SOMANYCERA  SELL ₹19.50 at stop ₹755.11 (+26.9%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2021-11-30  MAHLOG      SELL ₹15.86 at stop ₹654.55 (+32.0%, charges ₹0.0165) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹20.27 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0240)
2021-12-06  CHAMBLFERT  BUY ₹15.09 at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹0.0179)
2021-12-13  SUPRAJIT    SELL ₹17.80 at stop ₹391.40 (-13.8%, charges ₹0.0185) — the cash goes back to work at the next Friday screen
2021-12-16  RSYSTEMS    SELL ₹18.39 at stop ₹291.18 (-10.4%, charges ₹0.0191) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹19.90 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0236)
2021-12-20  MINDAIND    BUY ₹16.29 at ₹1,026.00 (fresh Friday signal — BUY: 5.05× weekly, month 1.81×, ladder rising; stop ₹787.66; charges ₹0.0193)
2021-12-21  TCIEXP      SELL ₹18.72 at stop ₹2,039.74 (+11.4%, charges ₹0.0194) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹18.72 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0222)
2022-01-07  MINDAIND    SELL ₹17.24 at stop ₹1,088.41 (+6.1%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2022-01-10  COMPINFO    BUY ₹17.24 at ₹45.00 (fresh Friday signal — BUY: 4.39× weekly, month 5.27×, ladder rising; stop ₹25.44; charges ₹0.0204)
2022-01-24  TVTODAY     SELL ₹20.24 at stop ₹311.68 (-2.7%, charges ₹0.0210) — the cash goes back to work at the next Friday screen
2022-01-25  SWANENERGY  SELL ₹20.27 at stop ₹162.64 (+8.5%, charges ₹0.0210) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹20.64 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0245)
2022-01-31  TV18BRDCST  BUY ₹19.87 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.0235)
2022-02-11  SHARDACROP  SELL ₹19.14 at stop ₹545.30 (-7.1%, charges ₹0.0199) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹12.98 at stop ₹424.65 (-8.7%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹19.14 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0227)
2022-02-15  RAYMOND     SELL ₹23.25 at stop ₹679.35 (+14.0%, charges ₹0.0241) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹19.43 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0230)
2022-02-22  GREENLAM    SELL ₹17.13 at stop ₹313.67 (-13.7%, charges ₹0.0178) — the cash goes back to work at the next Friday screen
2022-02-22  TV18BRDCST  SELL ₹19.65 at stop ₹58.38 (-0.9%, charges ₹0.0204) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹13.08 at stop ₹353.85 (-13.2%, charges ₹0.0136) — the cash goes back to work at the next Friday screen
2022-02-24  COMPINFO    SELL ₹11.11 at stop ₹29.08 (-35.4%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹19.19 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0227)
2022-02-28  SHANTIGEAR  BUY ₹19.18 at ₹185.30 (fresh Friday signal — BUY: 2.90× weekly, month 1.90×, ladder rising; stop ₹170.29; charges ₹0.0227)
2022-03-07  EXCELINDUS  BUY ₹19.41 at ₹1,523.00 (fresh Friday signal — BUY: 6.93× weekly, month 5.51×, ladder rising; stop ₹1,016.01; charges ₹0.0230)
2022-03-07  GTLINFRA    BUY ₹19.55 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0232)
2022-03-21  BSE         SELL ₹17.49 at stop ₹1,634.39 (-13.5%, charges ₹0.0181) — the cash goes back to work at the next Friday screen
2022-03-29  EXCELINDUS  SELL ₹18.29 at stop ₹1,438.30 (-5.6%, charges ₹0.0190) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹9.8353 paid (STCG ₹49.18 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  RCF         BUY ₹19.04 at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.0226)
2022-04-29  GTLINFRA    SELL ₹16.18 at stop ₹1.41 (-17.1%, charges ₹0.0168) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹21.15 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.0251)
2022-05-04  RCF         SELL ₹18.36 at stop ₹93.15 (-3.4%, charges ₹0.0190) — the cash goes back to work at the next Friday screen
2022-05-09  JKIL        BUY ₹20.73 at ₹229.70 (fresh Friday signal — BUY: 6.96× weekly, month 3.58×, ladder rising; stop ₹192.28; charges ₹0.0246)
2022-05-11  MFL         SELL ₹18.09 at stop ₹1,225.50 (-14.3%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹18.09 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0214)
2022-06-06  VBL         SELL ₹16.10 at stop ₹196.27 (-10.8%, charges ₹0.0167) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹16.10 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0191)
2022-06-20  JSWENERGY   SELL ₹31.30 at stop ₹201.99 (+146.8%, charges ₹0.0325) — the cash goes back to work at the next Friday screen
2022-06-27  APARINDS    BUY ₹21.46 at ₹1,004.00 (fresh Friday signal — BUY: 7.05× weekly, month 6.41×, ladder rising; stop ₹706.80; charges ₹0.0254)
2022-08-05  JKIL        SELL ₹27.80 at stop ₹308.80 (+34.4%, charges ₹0.0288) — the cash goes back to work at the next Friday screen
2022-08-08  NAVNETEDUL  BUY ₹23.08 at ₹130.50 (fresh Friday signal — BUY: 14.73× weekly, month 3.84×, ladder rising; stop ₹88.40; charges ₹0.0273)
2022-08-08  TVSSRICHAK  BUY ₹14.56 at ₹2,242.10 (fresh Friday signal — BUY: 10.49× weekly, month 1.64×, ladder rising; stop ₹1,791.98; charges ₹0.0172)
2022-09-06  DANGEE      SELL ₹30.58 at stop ₹375.25 (+59.7%, charges ₹0.0317) — the cash goes back to work at the next Friday screen
2022-09-12  SHREECEM    BUY ₹24.21 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0287)
2022-09-26  NAVNETEDUL  SELL ₹22.47 at stop ₹127.30 (-2.5%, charges ₹0.0233) — the cash goes back to work at the next Friday screen
2022-09-26  TVSSRICHAK  SELL ₹15.76 at stop ₹2,432.24 (+8.5%, charges ₹0.0163) — the cash goes back to work at the next Friday screen
2022-10-03  JSWHL       BUY ₹20.99 at ₹4,261.60 (fresh Friday signal — ACCUMULATE: 4.98× weekly, month 4.78×, ladder rising; stop ₹3,403.99; charges ₹0.0249)
2022-10-03  SUNDARMHLD  BUY ₹23.61 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹0.0280)
2022-10-11  SUNDARMHLD  SELL ₹20.98 at stop ₹92.20 (-10.9%, charges ₹0.0218) — the cash goes back to work at the next Friday screen
2022-10-17  FAIRCHEMOR  BUY ₹20.98 at ₹2,240.00 (fresh Friday signal — ACCUMULATE: 2.93× weekly, month 2.97×, ladder rising; stop ₹1,790.15; charges ₹0.0249)
2022-11-01  FAIRCHEMOR  SELL ₹16.73 at stop ₹1,790.15 (-20.1%, charges ₹0.0174) — the cash goes back to work at the next Friday screen
2022-11-03  APARINDS    SELL ₹28.97 at stop ₹1,358.50 (+35.3%, charges ₹0.0301) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹24.64 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0292)
2022-11-07  RVNL        BUY ₹21.07 at ₹46.85 (fresh Friday signal — BUY: 4.42× weekly, month 4.42×, ladder rising; stop ₹33.77; charges ₹0.0250)
2022-12-21  ELECON      SELL ₹26.56 at stop ₹202.49 (+65.3%, charges ₹0.0275) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹35.69 at stop ₹345.56 (+86.5%, charges ₹0.0370) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹24.55 at stop ₹139.84 (-0.1%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2022-12-26  KRISHANA    BUY ₹24.72 at ₹83.60 (fresh Friday signal — BUY: 3.70× weekly, month 2.29×, ladder rising; stop ₹75.36; charges ₹0.0293)
2022-12-26  RVNL        SELL ₹27.18 at stop ₹60.57 (+29.3%, charges ₹0.0282) — the cash goes back to work at the next Friday screen
2023-01-02  GICRE       BUY ₹14.93 at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 11.18×, ladder rising; stop ₹137.57; charges ₹0.0177)
2023-01-02  IOB         BUY ₹24.79 at ₹32.40 (fresh Friday signal — ACCUMULATE: 4.77× weekly, month 30.16×, ladder rising; stop ₹21.23; charges ₹0.0294)
2023-01-02  MUKANDLTD   BUY ₹24.80 at ₹136.70 (fresh Friday signal — BUY: 6.81× weekly, month 2.54×, ladder rising; stop ₹103.76; charges ₹0.0294)
2023-01-02  SUNFLAG     BUY ₹24.74 at ₹113.00 (fresh Friday signal — ACCUMULATE: 3.55× weekly, month 1.84×, ladder rising; stop ₹86.70; charges ₹0.0293)
2023-02-01  GICRE       SELL ₹13.94 at stop ₹167.72 (-6.4%, charges ₹0.0145) — the cash goes back to work at the next Friday screen
2023-02-06  JINDALSAW   BUY ₹13.94 at ₹65.22 (fresh Friday signal — BUY: 2.72× weekly, month 3.57×, ladder rising; stop ₹51.25; charges ₹0.0165)
2023-02-17  CGCL        SELL ₹22.79 at stop ₹704.95 (+17.6%, charges ₹0.0236) — the cash goes back to work at the next Friday screen
2023-02-20  TIIL        BUY ₹22.79 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0270)
2023-02-27  SUNFLAG     SELL ₹28.23 at stop ₹129.20 (+14.3%, charges ₹0.0293) — the cash goes back to work at the next Friday screen
2023-03-06  WONDERLA    BUY ₹24.88 at ₹456.00 (fresh Friday signal — BUY: 4.06× weekly, month 2.13×, ladder rising; stop ₹384.27; charges ₹0.0295)
2023-03-20  IOB         SELL ₹16.93 at stop ₹22.18 (-31.5%, charges ₹0.0176) — the cash goes back to work at the next Friday screen
2023-03-20  KRISHANA    SELL ₹27.85 at stop ₹94.40 (+12.9%, charges ₹0.0289) — the cash goes back to work at the next Friday screen
2023-03-27  ANURAS      BUY ₹23.36 at ₹867.00 (fresh Friday signal — BUY: 7.51× weekly, month 4.46×, ladder rising; stop ₹691.46; charges ₹0.0277)
2023-03-27  JINDALSAW   SELL ₹14.49 at stop ₹67.92 (+4.1%, charges ₹0.0150) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹23.25 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.61×, ladder rising; stop ₹372.21; charges ₹0.0275)
2023-03-27  WONDERLA    SELL ₹20.92 at stop ₹384.27 (-15.7%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹41.27 at stop ₹112.36 (+116.1%, charges ₹0.0428) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹22.17 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.0263)
2023-04-03  TAX         FY2023 settled: ₹13.5708 paid (STCG ₹42.34 @20%, LTCG ₹40.83 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-10  KIRLOSBROS  BUY ₹20.00 at ₹425.00 (fresh Friday signal — BUY: 1.86× weekly, month 2.36×, ladder rising; stop ₹357.44; charges ₹0.0237)
2023-04-10  KIRLOSIND   BUY ₹22.46 at ₹2,724.00 (fresh Friday signal — BUY: 2.29× weekly, month 2.42×, ladder rising; stop ₹2,256.25; charges ₹0.0266)
2023-04-24  SHREECEM    SELL ₹23.21 at stop ₹23,636.00 (-3.9%, charges ₹0.0241) — the cash goes back to work at the next Friday screen
2023-04-26  KIRLOSBROS  SELL ₹18.96 at stop ₹403.85 (-5.0%, charges ₹0.0197) — the cash goes back to work at the next Friday screen
2023-05-02  FAIRCHEMOR  BUY ₹19.17 at ₹1,272.00 (fresh Friday signal — BUY: 3.67× weekly, month 1.62×, ladder rising; stop ₹1,054.59; charges ₹0.0227)
2023-05-02  GLS         BUY ₹23.00 at ₹509.05 (fresh Friday signal — BUY: 4.14× weekly, month 2.64×, ladder rising; stop ₹351.50; charges ₹0.0272)
2023-05-17  MUKANDLTD   SELL ₹21.04 at stop ₹116.23 (-15.0%, charges ₹0.0218) — the cash goes back to work at the next Friday screen
2023-05-19  FAIRCHEMOR  SELL ₹17.16 at stop ₹1,141.04 (-10.3%, charges ₹0.0178) — the cash goes back to work at the next Friday screen
2023-05-22  NEULANDLAB  BUY ₹15.20 at ₹2,831.90 (fresh Friday signal — BUY: 6.13× weekly, month 4.03×, ladder rising; stop ₹1,908.60; charges ₹0.0180)
2023-05-22  SHARDAMOTR  BUY ₹23.01 at ₹380.00 (fresh Friday signal — BUY: 9.54× weekly, month 2.31×, ladder rising; stop ₹342.95; charges ₹0.0273)
2023-07-03  ANURAS      SELL ₹27.09 at stop ₹1,007.67 (+16.2%, charges ₹0.0281) — the cash goes back to work at the next Friday screen
2023-07-10  GENUSPOWER  BUY ₹24.27 at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.48×, ladder rising; stop ₹99.51; charges ₹0.0288)
2023-07-12  KSB         SELL ₹22.63 at stop ₹407.74 (-2.4%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹24.85 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0294)
2023-09-13  NEULANDLAB  SELL ₹18.51 at stop ₹3,457.30 (+22.1%, charges ₹0.0192) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹19.11 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.67×, ladder rising; stop ₹58.28; charges ₹0.0226)
2023-09-25  KIRLOSIND   SELL ₹26.35 at stop ₹3,202.97 (+17.6%, charges ₹0.0273) — the cash goes back to work at the next Friday screen
2023-10-03  PILANIINVS  BUY ₹26.35 at ₹2,380.05 (fresh Friday signal — BUY: 3.07× weekly, month 7.66×, ladder rising; stop ₹2,018.75; charges ₹0.0312)
2023-10-23  SJVN        SELL ₹16.71 at stop ₹66.03 (-12.4%, charges ₹0.0173) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹29.50 at stop ₹1,840.70 (+33.4%, charges ₹0.0306) — the cash goes back to work at the next Friday screen
2023-10-25  SHARDAMOTR  SELL ₹28.09 at stop ₹465.07 (+22.4%, charges ₹0.0291) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹16.57 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0196)
2023-10-30  KKCL        BUY ₹28.88 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0342)
2023-10-30  SHAREINDIA  BUY ₹28.86 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0342)
2023-11-16  GENUSPOWER  SELL ₹34.80 at stop ₹234.03 (+43.7%, charges ₹0.0361) — the cash goes back to work at the next Friday screen
2023-11-20  ISMTLTD     BUY ₹31.20 at ₹94.60 (fresh Friday signal — BUY: 5.37× weekly, month 1.93×, ladder rising; stop ₹80.18; charges ₹0.0370)
2023-12-20  ISMTLTD     SELL ₹29.08 at stop ₹88.35 (-6.6%, charges ₹0.0302) — the cash goes back to work at the next Friday screen
2023-12-26  MMFL        BUY ₹32.68 at ₹1,023.60 (fresh Friday signal — BUY: 9.43× weekly, month 3.43×, ladder rising; stop ₹821.80; charges ₹0.0387)
2024-01-17  TIIL        SELL ₹47.60 at stop ₹2,337.00 (+109.3%, charges ₹0.0494) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹33.86 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0401)
2024-01-30  MMFL        SELL ₹29.05 at stop ₹912.05 (-10.9%, charges ₹0.0301) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹36.89 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0437)
2024-03-05  GLS         SELL ₹35.14 at stop ₹779.48 (+53.1%, charges ₹0.0364) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹34.28 at stop ₹357.20 (+19.1%, charges ₹0.0356) — the cash goes back to work at the next Friday screen
2024-03-11  DOLLAR      BUY ₹37.59 at ₹527.95 (fresh Friday signal — BUY: 4.55× weekly, month 2.48×, ladder rising; stop ₹461.65; charges ₹0.0445)
2024-03-11  SOLARINDS   BUY ₹37.51 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0444)
2024-03-11  TCI         SELL ₹29.46 at stop ₹790.40 (-20.0%, charges ₹0.0306) — the cash goes back to work at the next Friday screen
2024-03-13  DOLLAR      SELL ₹32.80 at stop ₹461.65 (-12.6%, charges ₹0.0340) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹25.50 at stop ₹674.12 (-11.5%, charges ₹0.0264) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹33.94 at stop ₹666.47 (+0.5%, charges ₹0.0352) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹35.80 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.0424)
2024-03-18  FORCEMOT    BUY ₹35.64 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.0422)
2024-03-18  INDIGO      BUY ₹35.59 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0422)
2024-03-27  ANANDRATHI  SELL ₹80.51 at stop ₹862.65 (+224.7%, charges ₹0.0835) — the cash goes back to work at the next Friday screen
2024-04-01  DMART       BUY ₹34.85 at ₹4,570.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.56×, ladder rising; stop ₹3,695.50; charges ₹0.0413)
2024-04-01  SHRIRAMFIN  BUY ₹34.76 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0412)
2024-04-01  TAX         FY2024 settled: ₹20.2312 paid (STCG ₹101.16 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-09  PILANIINVS  SELL ₹40.98 at stop ₹3,710.37 (+55.9%, charges ₹0.0425) — the cash goes back to work at the next Friday screen
2024-05-13  JSWHL       SELL ₹30.86 at stop ₹6,280.45 (+47.4%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2024-05-13  JWL         BUY ₹35.81 at ₹490.00 (fresh Friday signal — BUY: 7.12× weekly, month 2.51×, ladder rising; stop ₹370.93; charges ₹0.0424)
2024-05-21  KIRLOSBROS  BUY ₹36.88 at ₹1,844.00 (fresh Friday signal — BUY: 5.41× weekly, month 1.62×, ladder rising; stop ₹1,221.51; charges ₹0.0437)
2024-05-28  FORCEMOT    SELL ₹43.76 at stop ₹8,083.64 (+23.1%, charges ₹0.0454) — the cash goes back to work at the next Friday screen
2024-05-31  DMART       SELL ₹32.89 at stop ₹4,322.83 (-5.4%, charges ₹0.0341) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹37.24 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0441)
2024-06-03  THERMAX     BUY ₹37.10 at ₹5,640.00 (fresh Friday signal — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹0.0440)
2024-06-04  BOSCHLTD    SELL ₹35.13 at stop ₹29,015.09 (-1.6%, charges ₹0.0364) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹32.31 at stop ₹441.77 (-6.8%, charges ₹0.0335) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹39.49 at stop ₹7,980.95 (+5.5%, charges ₹0.0410) — the cash goes back to work at the next Friday screen
2024-06-10  DABUR       BUY ₹35.39 at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹0.0419)
2024-06-10  FIEMIND     BUY ₹35.59 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0422)
2024-06-10  UNOMINDA    BUY ₹35.47 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0420)
2024-07-19  UNOMINDA    SELL ₹35.83 at stop ₹981.87 (+1.2%, charges ₹0.0372) — the cash goes back to work at the next Friday screen
2024-07-22  INDIAGLYCO  BUY ₹36.53 at ₹515.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.25×, ladder rising; stop ₹429.42; charges ₹0.0433)
2024-07-23  FIEMIND     SELL ₹33.83 at stop ₹1,257.56 (-4.7%, charges ₹0.0351) — the cash goes back to work at the next Friday screen
2024-07-29  THYROCARE   BUY ₹37.36 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0443)
2024-08-05  KIRLOSBROS  SELL ₹39.66 at stop ₹1,987.46 (+7.8%, charges ₹0.0411) — the cash goes back to work at the next Friday screen
2024-08-05  THERMAX     SELL ₹30.98 at stop ₹4,719.70 (-16.3%, charges ₹0.0321) — the cash goes back to work at the next Friday screen
2024-08-06  JWL         SELL ₹40.25 at stop ₹552.00 (+12.7%, charges ₹0.0417) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹35.96 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0426)
2024-08-12  CERA        BUY ₹35.90 at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹0.0425)
2024-08-12  PCBL        BUY ₹35.83 at ₹393.00 (fresh Friday signal — BUY: 4.82× weekly, month 4.03×, ladder rising; stop ₹246.00; charges ₹0.0425)
2024-08-16  CAMPUS      SELL ₹36.00 at stop ₹277.07 (-3.1%, charges ₹0.0373) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹35.46 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0420)
2024-09-19  CERA        SELL ₹27.97 at stop ₹8,198.93 (-21.9%, charges ₹0.0290) — the cash goes back to work at the next Friday screen
2024-09-23  ALKYLAMINE  BUY ₹34.98 at ₹2,432.85 (fresh Friday signal — BUY: 9.32× weekly, month 3.52×, ladder rising; stop ₹2,106.24; charges ₹0.0415)
2024-10-03  DABUR       SELL ₹35.21 at stop ₹602.49 (-0.3%, charges ₹0.0365) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹35.21 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0417)
2024-10-07  INDIGO      SELL ₹49.77 at stop ₹4,485.14 (+40.2%, charges ₹0.0516) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹37.81 at stop ₹796.15 (+1.4%, charges ₹0.0392) — the cash goes back to work at the next Friday screen
2024-10-14  DBCORP      BUY ₹37.08 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0439)
2024-10-14  SKIPPER     BUY ₹36.94 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0438)
2024-10-18  PCBL        SELL ₹43.38 at stop ₹476.85 (+21.3%, charges ₹0.0450) — the cash goes back to work at the next Friday screen
2024-10-21  GOPAL       BUY ₹21.56 at ₹473.05 (fresh Friday signal — BUY: 2.89× weekly, month 3.23×, ladder rising; stop ₹361.19; charges ₹0.0255)
2024-10-21  MOTILALOFS  BUY ₹35.37 at ₹1,021.95 (fresh Friday signal — BUY: 7.74× weekly, month 5.64×, ladder rising; stop ₹656.59; charges ₹0.0419)
2024-10-22  ALKYLAMINE  SELL ₹30.22 at stop ₹2,106.24 (-13.4%, charges ₹0.0313) — the cash goes back to work at the next Friday screen
2024-10-22  BASF        SELL ₹37.15 at stop ₹7,611.30 (+3.6%, charges ₹0.0385) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹31.75 at stop ₹302.08 (-14.2%, charges ₹0.0329) — the cash goes back to work at the next Friday screen
2024-10-25  INDIAGLYCO  SELL ₹41.61 at stop ₹587.91 (+14.2%, charges ₹0.0432) — the cash goes back to work at the next Friday screen
2024-10-28  CARERATING  BUY ₹31.38 at ₹1,396.00 (fresh Friday signal — BUY: 7.47× weekly, month 3.86×, ladder rising; stop ₹1,066.23; charges ₹0.0372)
2024-10-28  CUPID       SELL ₹21.68 at stop ₹158.66 (+31.1%, charges ₹0.0225) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹31.50 at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.0373)
2024-11-04  AKZOINDIA   BUY ₹34.56 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.0816)
2024-11-04  KIRLPNU     BUY ₹34.37 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.0811)
2024-11-11  JSWHL       BUY ₹30.61 at ₹15,500.00 (fresh Friday signal — BUY: 8.83× weekly, month 3.54×, ladder rising; stop ₹8,434.53; charges ₹0.0723)
2024-11-14  ASTRAZEN    SELL ₹32.32 at stop ₹6,854.77 (-7.9%, charges ₹0.0718) — the cash goes back to work at the next Friday screen
2024-11-25  GARFIBRES   BUY ₹32.32 at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹0.0763)
2024-12-12  GOPAL       SELL ₹18.90 at stop ₹416.05 (-12.0%, charges ₹0.0420) — the cash goes back to work at the next Friday screen
2024-12-16  SWANENERGY  BUY ₹18.90 at ₹781.90 (fresh Friday signal — BUY: 3.50× weekly, month 2.49×, ladder rising; stop ₹574.13; charges ₹0.0446)
2024-12-17  SUPRIYA     SELL ₹48.01 at stop ₹717.25 (+35.8%, charges ₹0.1066) — the cash goes back to work at the next Friday screen
2024-12-23  KIRLPNU     SELL ₹32.16 at stop ₹1,596.00 (-6.0%, charges ₹0.0714) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹33.99 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.0802)
2024-12-27  AKZOINDIA   SELL ₹26.06 at stop ₹3,423.18 (-24.2%, charges ₹0.0579) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹34.07 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.0804)
2024-12-30  KFINTECH    BUY ₹33.96 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.0802)
2025-01-09  GARFIBRES   SELL ₹27.91 at stop ₹829.35 (-13.2%, charges ₹0.0620) — the cash goes back to work at the next Friday screen
2025-01-09  KSL         SELL ₹30.07 at stop ₹1,059.30 (-11.1%, charges ₹0.0668) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹37.49 at stop ₹893.05 (+19.4%, charges ₹0.0833) — the cash goes back to work at the next Friday screen
2025-01-09  SWANENERGY  SELL ₹16.15 at stop ₹671.32 (-14.1%, charges ₹0.0359) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹31.77 at stop ₹477.28 (-13.7%, charges ₹0.0706) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹31.14 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0735)
2025-01-13  CARERATING  SELL ₹27.77 at stop ₹1,239.70 (-11.2%, charges ₹0.0617) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹31.06 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.0733)
2025-01-15  KFINTECH    SELL ₹25.92 at stop ₹1,159.14 (-23.3%, charges ₹0.0576) — the cash goes back to work at the next Friday screen
2025-01-17  MOTILALOFS  SELL ₹27.21 at stop ₹788.79 (-22.8%, charges ₹0.0604) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹26.01 at stop ₹700.36 (-16.1%, charges ₹0.0578) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹29.97 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0708)
2025-01-28  LLOYDSME    SELL ₹26.99 at stop ₹1,258.75 (-12.7%, charges ₹0.0600) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹30.64 at ₹947.00 (fresh Friday signal — BUY: 2.25× weekly, month 2.40×, ladder rising; stop ₹727.84; charges ₹0.0723)
2025-02-12  JINDWORLD   SELL ₹31.13 at stop ₹374.11 (-8.2%, charges ₹0.0691) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹29.02 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0685)
2025-03-03  ZENSARTECH  SELL ₹23.44 at stop ₹727.84 (-23.1%, charges ₹0.0521) — the cash goes back to work at the next Friday screen
2025-03-17  AVANTIFEED  BUY ₹30.14 at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹0.0711)
2025-03-24  INDIASHLTR  BUY ₹31.55 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.0745)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹5.87 / LT ₹0.00)
2025-04-07  AVANTIFEED  SELL ₹23.10 at stop ₹648.95 (-23.0%, charges ₹0.0513) — the cash goes back to work at the next Friday screen
2025-04-07  INDIASHLTR  SELL ₹29.19 at stop ₹738.82 (-7.1%, charges ₹0.0648) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹30.67 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.0724)
2025-04-15  INDIASHLTR  BUY ₹30.79 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.0727)
2025-04-28  FORCEMOT    BUY ₹31.32 at ₹9,275.00 (fresh Friday signal — ACCUMULATE: 2.06× weekly, month 1.62×, ladder rising; stop ₹7,647.50; charges ₹0.0739)
2025-04-28  KIMS        BUY ₹31.22 at ₹679.50 (fresh Friday signal — BUY: 1.93× weekly, month 1.58×, ladder rising; stop ₹486.11; charges ₹0.0737)
2025-04-28  WHIRLPOOL   BUY ₹31.20 at ₹1,153.90 (fresh Friday signal — BUY: 2.21× weekly, month 1.77×, ladder rising; stop ₹1,017.54; charges ₹0.0737)
2025-05-05  PARAS       BUY ₹19.65 at ₹1,372.20 (fresh Friday signal — BUY: 25.56× weekly, month 2.22×, ladder rising; stop ₹973.27; charges ₹0.0464)
2025-07-04  PARAS       SELL ₹20.21 at stop ₹1,417.98 (+3.3%, charges ₹0.0449) — the cash goes back to work at the next Friday screen
2025-07-07  ASTERDM     BUY ₹20.21 at ₹633.90 (fresh Friday signal — BUY: 6.11× weekly, month 1.72×, ladder rising; stop ₹509.77; charges ₹0.0477)
2025-08-04  JSWHL       SELL ₹37.56 at stop ₹19,106.01 (+23.3%, charges ₹0.0834) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹36.16 at stop ₹1,814.78 (+25.2%, charges ₹0.0803) — the cash goes back to work at the next Friday screen
2025-08-07  WHIRLPOOL   SELL ₹35.04 at stop ₹1,301.97 (+12.8%, charges ₹0.0778) — the cash goes back to work at the next Friday screen
2025-08-11  PGHL        BUY ₹33.66 at ₹6,345.00 (fresh Friday signal — BUY: 1.64× weekly, month 2.94×, ladder rising; stop ₹5,320.00; charges ₹0.0795)
2025-08-11  RAIN        BUY ₹33.72 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.0796)
2025-08-18  VSTTILLERS  BUY ₹34.67 at ₹5,260.00 (fresh Friday signal — BUY: 7.75× weekly, month 4.61×, ladder rising; stop ₹4,193.97; charges ₹0.0818)
2025-08-26  RAIN        SELL ₹30.09 at stop ₹143.64 (-10.4%, charges ₹0.0668) — the cash goes back to work at the next Friday screen
2025-09-01  RSYSTEMS    BUY ₹34.12 at ₹460.00 (fresh Friday signal — BUY: 3.48× weekly, month 6.66×, ladder rising; stop ₹394.44; charges ₹0.0805)
2025-09-24  RSYSTEMS    SELL ₹31.25 at stop ₹423.23 (-8.0%, charges ₹0.0694) — the cash goes back to work at the next Friday screen
2025-09-25  INDIASHLTR  SELL ₹30.56 at stop ₹862.60 (-0.3%, charges ₹0.0679) — the cash goes back to work at the next Friday screen
2025-09-29  LGBBROSLTD  BUY ₹32.07 at ₹1,411.60 (fresh Friday signal — BUY: 3.53× weekly, month 1.72×, ladder rising; stop ₹1,258.75; charges ₹0.0757)
2025-09-29  SUBROS      BUY ₹32.42 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0765)
2025-10-03  KIMS        SELL ₹31.12 at stop ₹680.34 (+0.1%, charges ₹0.0691) — the cash goes back to work at the next Friday screen
2025-10-06  ASTRAMICRO  BUY ₹31.12 at ₹1,119.85 (fresh Friday signal — BUY: 3.17× weekly, month 1.83×, ladder rising; stop ₹1,026.00; charges ₹0.0735)
2025-10-09  FORCEMOT    SELL ₹51.59 at stop ₹15,350.10 (+65.5%, charges ₹0.1146) — the cash goes back to work at the next Friday screen
2025-10-13  RAMKY       BUY ₹32.16 at ₹622.35 (fresh Friday signal — BUY: 20.34× weekly, month 6.75×, ladder rising; stop ₹529.58; charges ₹0.0759)
2025-10-13  SHAILY      BUY ₹19.44 at ₹2,434.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 1.66×, ladder rising; stop ₹1,942.00; charges ₹0.0459)
2025-10-14  SUBROS      SELL ₹29.84 at stop ₹1,046.90 (-7.5%, charges ₹0.0663) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹29.84 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0704)
2025-10-20  CREDITACC   SELL ₹44.73 at stop ₹1,274.42 (+49.9%, charges ₹0.0994) — the cash goes back to work at the next Friday screen
2025-10-27  SKYGOLD     BUY ₹32.32 at ₹370.00 (fresh Friday signal — BUY: 1.65× weekly, month 2.25×, ladder rising; stop ₹304.38; charges ₹0.0763)
2025-11-06  ASTRAMICRO  SELL ₹28.38 at stop ₹1,026.00 (-8.4%, charges ₹0.0630) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹31.36 at stop ₹5,938.45 (-6.4%, charges ₹0.0697) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹32.62 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.0770)
2025-11-10  CUB         BUY ₹32.79 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.0774)
2025-11-20  ANANDRATHI  SELL ₹27.36 at stop ₹1,450.17 (-7.9%, charges ₹0.0608) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹31.24 at stop ₹976.41 (-3.8%, charges ₹0.0694) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹32.42 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0765)
2025-11-25  SKYGOLD     SELL ₹28.62 at stop ₹329.13 (-11.0%, charges ₹0.0636) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹32.55 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.33×, ladder rising; stop ₹535.37; charges ₹0.0768)
2025-12-01  RAMKY       SELL ₹29.74 at stop ₹578.17 (-7.1%, charges ₹0.0660) — the cash goes back to work at the next Friday screen
2025-12-01  SANSERA     BUY ₹28.99 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.0684)
2025-12-05  ASTERDM     SELL ₹20.42 at stop ₹643.62 (+1.5%, charges ₹0.0454) — the cash goes back to work at the next Friday screen
2025-12-08  KIRLOSENG   BUY ₹18.80 at ₹1,130.00 (fresh Friday signal — BUY: 1.67× weekly, month 2.31×, ladder rising; stop ₹886.54; charges ₹0.0444)
2025-12-08  NATCOPHARM  BUY ₹31.36 at ₹934.70 (fresh Friday signal — BUY: 3.52× weekly, month 3.33×, ladder rising; stop ₹825.79; charges ₹0.0740)
2025-12-15  SHAILY      SELL ₹18.61 at stop ₹2,340.80 (-3.8%, charges ₹0.0413) — the cash goes back to work at the next Friday screen
2025-12-29  HINDCOPPER  BUY ₹18.61 at ₹545.05 (fresh Friday signal — BUY: 3.05× weekly, month 3.40×, ladder rising; stop ₹345.04; charges ₹0.0439)
2026-01-08  EUREKAFORB  SELL ₹28.75 at stop ₹589.10 (-11.3%, charges ₹0.0638) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹29.01 at stop ₹2,956.49 (-10.1%, charges ₹0.0644) — the cash goes back to work at the next Friday screen
2026-01-12  KIRLOSENG   SELL ₹18.89 at stop ₹1,140.95 (+1.0%, charges ₹0.0420) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹31.21 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.0737)
2026-01-20  LGBBROSLTD  SELL ₹38.76 at stop ₹1,713.80 (+21.4%, charges ₹0.0861) — the cash goes back to work at the next Friday screen
2026-01-20  NATCOPHARM  SELL ₹27.58 at stop ₹825.79 (-11.7%, charges ₹0.0613) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹27.94 at stop ₹748.60 (-8.5%, charges ₹0.0621) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹27.59 at stop ₹1,672.76 (-4.4%, charges ₹0.0613) — the cash goes back to work at the next Friday screen
2026-02-17  NATIONALUM  SELL ₹29.61 at stop ₹335.49 (-4.7%, charges ₹0.0658) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹30.14 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.67×, ladder rising; stop ₹5,440.18; charges ₹0.0711)
2026-02-23  E2E         BUY ₹30.50 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0720)
2026-02-23  HAPPYFORGE  BUY ₹30.04 at ₹1,370.00 (fresh Friday signal — BUY: 1.58× weekly, month 2.15×, ladder rising; stop ₹1,188.64; charges ₹0.0709)
2026-02-23  VESUVIUS    BUY ₹30.59 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.0722)
2026-03-02  J&KBANK     BUY ₹29.45 at ₹116.20 (fresh Friday signal — BUY: 8.67× weekly, month 1.90×, ladder rising; stop ₹96.50; charges ₹0.0695)
2026-03-02  KSB         BUY ₹29.45 at ₹738.00 (fresh Friday signal — BUY: 52.86× weekly, month 4.79×, ladder rising; stop ₹658.54; charges ₹0.0695)
2026-03-02  TORNTPOWER  BUY ₹16.74 at ₹1,491.00 (fresh Friday signal — BUY: 1.57× weekly, month 1.69×, ladder rising; stop ₹1,315.84; charges ₹0.0395)
2026-03-04  HAPPYFORGE  SELL ₹26.94 at stop ₹1,234.05 (-9.9%, charges ₹0.0598) — the cash goes back to work at the next Friday screen
2026-03-05  VSTTILLERS  SELL ₹35.60 at stop ₹5,425.45 (+3.1%, charges ₹0.0791) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹32.28 at stop ₹251.43 (-1.1%, charges ₹0.0717) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹17.97 at stop ₹528.63 (-3.0%, charges ₹0.0399) — the cash goes back to work at the next Friday screen
2026-03-16  JBCHEPHARM  BUY ₹28.85 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0681)
2026-03-23  J&KBANK     SELL ₹27.92 at stop ₹110.67 (-4.8%, charges ₹0.0620) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹26.42 at stop ₹464.31 (-13.2%, charges ₹0.0587) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹28.18 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0665)
2026-03-30  TORNTPOWER  SELL ₹14.71 at stop ₹1,315.84 (-11.7%, charges ₹0.0327) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹2.94 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹28.17 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0665)
2026-04-13  INOXINDIA   BUY ₹28.92 at ₹1,299.10 (fresh Friday signal — BUY: 4.08× weekly, month 2.14×, ladder rising; stop ₹1,091.46; charges ₹0.0683)
2026-04-13  THERMAX     BUY ₹29.17 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.0689)
2026-04-20  GALLANTT    BUY ₹30.41 at ₹862.10 (fresh Friday signal — BUY: 15.07× weekly, month 23.99×, ladder rising; stop ₹612.75; charges ₹0.0718)
2026-05-04  KSB         SELL ₹36.44 at stop ₹917.42 (+24.3%, charges ₹0.0809) — the cash goes back to work at the next Friday screen
2026-05-11  CRAFTSMAN   BUY ₹30.56 at ₹9,039.50 (fresh Friday signal — BUY: 22.97× weekly, month 3.93×, ladder rising; stop ₹7,119.77; charges ₹0.0721)
2026-05-13  INOXINDIA   SELL ₹30.41 at stop ₹1,372.18 (+5.6%, charges ₹0.0675) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹27.45 at stop ₹1,125.84 (-2.1%, charges ₹0.0610) — the cash goes back to work at the next Friday screen
2026-05-14  GALLANTT    SELL ₹27.52 at stop ₹783.75 (-9.1%, charges ₹0.0611) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹29.17 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.0689)
2026-05-18  CAPLIPOINT  BUY ₹29.17 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.0689)
2026-05-18  NLCINDIA    BUY ₹29.16 at ₹351.55 (fresh Friday signal — BUY: 5.83× weekly, month 6.05×, ladder rising; stop ₹278.49; charges ₹0.0688)
2026-06-05  E2E         SELL ₹24.29 at stop ₹2,330.72 (-20.0%, charges ₹0.0539) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹30.42 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0718)
2026-06-09  NLCINDIA    SELL ₹26.47 at stop ₹320.62 (-8.8%, charges ₹0.0588) — the cash goes back to work at the next Friday screen
2026-06-15  SFL         BUY ₹31.35 at ₹724.95 (fresh Friday signal — BUY: 2.17× weekly, month 4.11×, ladder rising; stop ₹542.50; charges ₹0.0740)
2026-07-29  THERMAX     SELL ₹34.77 at stop ₹4,306.64 (+19.8%, charges ₹0.0772) — the cash goes back to work at the next Friday screen
2026-08-03  TMB         BUY ₹33.23 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.0784)
2026-08-06  SFL         SELL ₹30.07 at stop ₹698.73 (-3.6%, charges ₹0.0668) — the cash goes back to work at the next Friday screen
2026-08-10  ASKAUTOLTD  BUY ₹32.51 at ₹648.95 (fresh Friday signal — BUY: 30.11× weekly, month 6.37×, ladder rising; stop ₹440.80; charges ₹0.0767)
2026-09-10  ALKYLAMINE  SELL ₹32.62 at stop ₹1,920.99 (+12.3%, charges ₹0.0725) — the cash goes back to work at the next Friday screen
```
