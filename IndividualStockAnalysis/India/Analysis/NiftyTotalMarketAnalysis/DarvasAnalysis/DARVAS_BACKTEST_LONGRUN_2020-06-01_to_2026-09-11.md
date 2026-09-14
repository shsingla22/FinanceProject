# The Darvas screen, run for six years — 2020-06-01 → 2026-09-11

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-11, 1785 symbols, fetched once into `ROLLING_IPO3M_2019-06-01_to_2026-09-13/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹180.09** | **+9.84% a year** |
| The same system before costs and taxes | ₹213.92 | +12.90% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹230.70 | +14.27% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹180.09** (+9.84% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.27 years, 328 weekly screens, 403 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹8.99** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹20.74**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹8.50 | ₹0.00 | ₹1.7002 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹47.23 | ₹0.00 | ₹9.4455 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹2.87 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹47.95 | ₹0.00 | ₹9.5897 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹3.20 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹28.68 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹34.30 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 114.88 | +14.9% | +15.5% | +35.6% |
| 2021 (2021-12-31) | 171.56 | +49.3% | +55.1% | +26.2% |
| 2022 (2022-12-30) | 162.31 | -5.4% | +2.1% | +4.3% |
| 2023 (2023-12-29) | 218.90 | +34.9% | +40.9% | +20.0% |
| 2024 (2024-12-27) | 208.57 | -4.7% | -3.2% | +9.6% |
| 2025 (2025-12-26) | 179.28 | -14.0% | -15.2% | +9.4% |
| 2026 (2026-09-11) | 180.09 | +0.5% | +1.1% | -10.2% |

## What it took to earn it

- **Maximum drawdown: -35.4%** (peak 2024-07-05 → trough 2026-04-02, on weekly closes).
- **188 closed trades**: 79 winners (42%), average winner +25.6%, average loser -12.5%.
- Best closed trade BORORENEW +148.3%; worst BCG -59.0%.
- Median holding period 58 days.
- Cash share of equity averaged 8% across all weeks (median 4%); the portfolio sat FULLY in cash for 1 of 328 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-06-26 | 102.17 | 0.23 | 10 |
| 2020-07-31 | 102.83 | 16.09 | 8 |
| 2020-08-28 | 110.89 | 14.60 | 9 |
| 2020-09-25 | 106.77 | 32.63 | 6 |
| 2020-10-30 | 104.70 | 2.25 | 9 |
| 2020-11-27 | 105.43 | 0.00 | 10 |
| 2020-12-24 | 114.88 | 28.74 | 7 |
| 2021-01-29 | 114.52 | 32.16 | 7 |
| 2021-02-26 | 126.54 | 10.23 | 9 |
| 2021-03-26 | 127.48 | 4.95 | 9 |
| 2021-04-30 | 137.37 | 5.92 | 9 |
| 2021-05-28 | 147.43 | 5.92 | 9 |
| 2021-06-25 | 152.27 | 7.34 | 9 |
| 2021-07-30 | 161.44 | 21.55 | 8 |
| 2021-08-27 | 156.86 | 0.00 | 10 |
| 2021-09-24 | 163.83 | 19.63 | 9 |
| 2021-10-29 | 165.65 | 29.01 | 9 |
| 2021-11-26 | 167.16 | 49.65 | 8 |
| 2021-12-31 | 171.56 | 0.00 | 11 |
| 2022-01-28 | 170.97 | 37.74 | 9 |
| 2022-02-25 | 155.66 | 60.02 | 7 |
| 2022-03-25 | 159.90 | 13.99 | 10 |
| 2022-04-29 | 153.74 | 28.00 | 8 |
| 2022-05-27 | 135.39 | 9.85 | 10 |
| 2022-06-24 | 137.83 | 2.49 | 10 |
| 2022-07-29 | 149.62 | 0.00 | 10 |
| 2022-08-26 | 157.80 | 4.41 | 10 |
| 2022-09-30 | 156.79 | 15.01 | 9 |
| 2022-10-28 | 160.36 | 0.24 | 10 |
| 2022-11-25 | 166.93 | 2.21 | 10 |
| 2022-12-30 | 162.31 | 85.68 | 5 |
| 2023-01-27 | 154.35 | 3.18 | 10 |
| 2023-02-24 | 151.88 | 14.61 | 9 |
| 2023-03-31 | 158.10 | 30.05 | 8 |
| 2023-04-28 | 166.90 | 0.90 | 10 |
| 2023-05-26 | 180.95 | 0.90 | 10 |
| 2023-06-30 | 183.32 | 0.90 | 10 |
| 2023-07-28 | 188.99 | 8.54 | 10 |
| 2023-08-25 | 207.90 | 29.49 | 9 |
| 2023-09-29 | 208.26 | 8.38 | 10 |
| 2023-10-27 | 205.71 | 48.79 | 8 |
| 2023-11-24 | 212.40 | 0.00 | 11 |
| 2023-12-29 | 218.90 | 0.00 | 11 |
| 2024-01-25 | 217.13 | 3.78 | 11 |
| 2024-02-23 | 219.68 | 0.00 | 11 |
| 2024-03-28 | 215.83 | 0.00 | 11 |
| 2024-04-26 | 217.48 | 0.00 | 11 |
| 2024-05-31 | 221.86 | 5.79 | 11 |
| 2024-06-28 | 223.03 | 0.00 | 11 |
| 2024-07-26 | 217.62 | 34.56 | 9 |
| 2024-08-30 | 215.84 | 2.87 | 11 |
| 2024-09-27 | 223.90 | 0.70 | 11 |
| 2024-10-25 | 206.29 | 43.70 | 9 |
| 2024-11-29 | 207.40 | 0.00 | 12 |
| 2024-12-27 | 208.57 | 34.65 | 10 |
| 2025-01-31 | 186.49 | 24.68 | 10 |
| 2025-02-28 | 176.29 | 45.55 | 9 |
| 2025-03-27 | 190.76 | 5.46 | 11 |
| 2025-04-25 | 196.40 | 8.17 | 10 |
| 2025-05-30 | 186.41 | 20.59 | 10 |
| 2025-06-27 | 193.82 | 1.99 | 11 |
| 2025-07-25 | 190.85 | 19.13 | 10 |
| 2025-08-29 | 178.20 | 16.00 | 10 |
| 2025-09-26 | 179.30 | 49.24 | 8 |
| 2025-10-31 | 177.68 | 8.60 | 11 |
| 2025-11-28 | 174.23 | 20.12 | 10 |
| 2025-12-26 | 179.28 | 0.00 | 11 |
| 2026-01-30 | 171.31 | 15.69 | 9 |
| 2026-02-27 | 157.58 | 37.48 | 8 |
| 2026-03-27 | 150.47 | 31.98 | 8 |
| 2026-04-30 | 158.03 | 3.34 | 10 |
| 2026-05-29 | 164.96 | 2.61 | 10 |
| 2026-06-25 | 160.64 | 0.00 | 10 |
| 2026-07-31 | 166.46 | 0.00 | 10 |
| 2026-08-28 | 176.42 | 0.00 | 10 |
| 2026-09-11 | 180.09 | 0.00 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| ABB | 2026-03-02 | 5,840.00 | 7,274.00 | 7,158.25 | +24.6% |
| APOLLOPIPE | 2026-03-16 | 407.55 | 554.90 | 440.44 | +36.2% |
| BLUESTONE | 2026-07-27 | 793.00 | 890.35 | 747.41 | +12.3% |
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,754.90 | 2,376.52 | +38.4% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,572.90 | 1,242.60 | +59.0% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| JTLINFRA | 2022-10-24 | 292.00 | 295.80 | 217.12 | +1.3% |
| RUBICON | 2026-06-08 | 1,190.00 | 1,835.40 | 1,653.47 | +54.2% |
| STRTECH | 2020-06-08 | 112.00 | 151.30 | 140.17 | +35.1% |
| SUBEX | 2020-10-19 | 15.55 | 16.95 | 11.11 | +9.0% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| EIHAHOTELS | 2020-06-08 | 137.50 | 2020-06-16 | 110.67 | -19.5% |
| DHANBANK | 2020-06-22 | 15.95 | 2020-07-14 | 12.82 | -19.6% |
| RELAXO | 2020-06-08 | 759.45 | 2020-07-28 | 603.77 | -20.5% |
| MANGCHEFER | 2020-06-08 | 38.75 | 2020-07-31 | 33.73 | -13.0% |
| EIDPARRY | 2020-06-08 | 219.00 | 2020-08-17 | 273.03 | +24.7% |
| COSMOFILMS | 2020-06-08 | 286.90 | 2020-08-28 | 410.40 | +43.0% |
| DYNPRO | 2020-08-03 | 200.00 | 2020-08-31 | 186.68 | -6.7% |
| LINCOLN | 2020-08-03 | 191.80 | 2020-08-31 | 224.20 | +16.9% |
| APCOTEXIND | 2020-08-24 | 164.95 | 2020-08-31 | 151.95 | -7.9% |
| RCF | 2020-06-08 | 45.20 | 2020-09-09 | 45.84 | +1.4% |
| SUNFLAG | 2020-06-08 | 43.00 | 2020-09-22 | 39.67 | -7.7% |
| TAJGVK | 2020-06-08 | 174.00 | 2020-09-22 | 126.45 | -27.3% |
| DLINKINDIA | 2020-08-31 | 127.00 | 2020-09-22 | 96.95 | -23.7% |
| SATIA | 2020-09-14 | 122.00 | 2020-09-22 | 102.97 | -15.6% |
| PRINCEPIPE | 2020-09-07 | 208.00 | 2020-10-12 | 220.88 | +6.2% |
| INDIAMART | 2020-09-07 | 2,124.50 | 2020-10-19 | 2,315.62 | +9.0% |
| ALEMBICLTD | 2020-06-08 | 56.40 | 2020-11-02 | 91.41 | +62.1% |
| VIDHIING | 2020-09-28 | 111.70 | 2020-12-02 | 115.50 | +3.4% |
| APOLLO | 2020-07-20 | 11.76 | 2020-12-21 | 11.88 | +1.0% |
| LASA | 2020-11-09 | 80.50 | 2020-12-21 | 77.95 | -3.2% |
| MANGCHEFER | 2020-12-07 | 40.75 | 2020-12-22 | 37.95 | -6.9% |
| ITDC | 2020-12-28 | 338.55 | 2021-01-18 | 304.38 | -10.1% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| JUSTDIAL | 2020-10-26 | 584.00 | 2021-01-25 | 622.35 | +6.6% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| RCF | 2021-03-01 | 80.00 | 2021-03-17 | 79.16 | -1.1% |
| TATAMOTORS | 2021-01-25 | 296.90 | 2021-03-19 | 296.97 | +0.0% |
| APTECHT | 2021-02-01 | 178.45 | 2021-03-19 | 204.25 | +14.5% |
| MHRIL | 2021-02-01 | 224.00 | 2021-03-19 | 210.90 | -5.8% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| POLYMED | 2020-09-07 | 449.70 | 2021-06-14 | 950.00 | +111.3% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| RIIL | 2021-06-21 | 758.50 | 2021-07-27 | 712.50 | -6.1% |
| WELSPUNIND | 2021-03-22 | 81.45 | 2021-08-10 | 124.64 | +53.0% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| GDL | 2021-01-25 | 158.00 | 2021-09-20 | 266.00 | +68.4% |
| GNA | 2021-08-02 | 328.00 | 2021-10-19 | 489.25 | +49.2% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| NEOGEN | 2021-09-27 | 1,255.00 | 2021-10-25 | 1,142.85 | -8.9% |
| INDOCO | 2021-08-16 | 484.30 | 2021-11-12 | 412.30 | -14.9% |
| SHOPERSTOP | 2021-10-25 | 326.00 | 2021-11-22 | 335.82 | +3.0% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-11-01 | 11,040.00 | 2021-11-26 | 10,070.05 | -8.8% |
| SOMANYCERA | 2021-06-21 | 594.85 | 2021-11-29 | 755.11 | +26.9% |
| NHPC | 2021-10-25 | 32.90 | 2021-11-29 | 30.11 | -8.5% |
| MAHLOG | 2021-01-25 | 495.85 | 2021-11-30 | 654.55 | +32.0% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| MINDAIND | 2021-12-27 | 1,180.00 | 2022-01-07 | 1,088.41 | -7.8% |
| LTI | 2021-10-25 | 6,555.00 | 2022-01-24 | 6,270.00 | -4.3% |
| MIRZAINT | 2021-12-06 | 107.00 | 2022-01-24 | 143.07 | +33.7% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| ZEELEARN | 2022-01-10 | 17.80 | 2022-02-22 | 13.28 | -25.4% |
| TV18BRDCST | 2022-01-31 | 58.90 | 2022-02-22 | 58.38 | -0.9% |
| CHAMBLFERT | 2021-12-06 | 407.45 | 2022-02-24 | 353.85 | -13.2% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| EXCELINDUS | 2022-03-07 | 1,523.00 | 2022-03-29 | 1,438.30 | -5.6% |
| EVERESTIND | 2022-02-21 | 740.00 | 2022-04-28 | 594.70 | -19.6% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| RCF | 2022-04-04 | 96.40 | 2022-05-04 | 93.15 | -3.4% |
| GNFC | 2022-02-14 | 553.00 | 2022-05-06 | 792.16 | +43.2% |
| ADSL | 2021-11-15 | 122.30 | 2022-05-09 | 134.90 | +10.3% |
| MAWANASUG | 2022-03-07 | 115.00 | 2022-05-09 | 135.09 | +17.5% |
| MFL | 2022-05-02 | 1,430.00 | 2022-05-11 | 1,225.50 | -14.3% |
| MOL | 2022-05-09 | 129.80 | 2022-05-11 | 113.62 | -12.5% |
| RIIL | 2022-05-02 | 1,100.00 | 2022-05-26 | 863.73 | -21.5% |
| BCG | 2021-11-29 | 134.10 | 2022-06-06 | 55.00 | -59.0% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| GRAUWEIL | 2022-05-23 | 82.70 | 2022-06-13 | 61.82 | -25.2% |
| MRPL | 2022-05-09 | 78.00 | 2022-07-06 | 69.61 | -10.8% |
| JKIL | 2022-05-09 | 229.70 | 2022-08-05 | 308.80 | +34.4% |
| MARATHON | 2022-07-11 | 215.00 | 2022-09-19 | 232.80 | +8.3% |
| NAVNETEDUL | 2022-08-08 | 130.50 | 2022-09-26 | 127.30 | -2.5% |
| VADILALIND | 2022-05-23 | 1,805.00 | 2022-10-20 | 2,295.06 | +27.2% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| HEIDELBERG | 2022-09-26 | 205.20 | 2022-12-21 | 190.00 | -7.4% |
| SHANTIGEAR | 2022-06-06 | 238.05 | 2022-12-22 | 345.56 | +45.2% |
| ACC | 2022-05-23 | 2,260.00 | 2022-12-23 | 2,465.16 | +9.1% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| WESTLIFE | 2022-10-03 | 728.00 | 2023-01-16 | 708.51 | -2.7% |
| GICRE | 2023-01-02 | 179.20 | 2023-02-01 | 167.72 | -6.4% |
| SPECIALITY | 2023-01-23 | 276.85 | 2023-02-14 | 221.73 | -19.9% |
| CGCL | 2022-03-07 | 600.00 | 2023-02-17 | 704.95 | +17.5% |
| SPIC | 2023-01-02 | 88.25 | 2023-02-23 | 65.74 | -25.5% |
| ATULAUTO | 2023-02-20 | 387.95 | 2023-03-13 | 335.92 | -13.4% |
| IOB | 2023-01-02 | 32.40 | 2023-03-20 | 22.18 | -31.5% |
| CIGNITITEC | 2023-02-20 | 731.95 | 2023-03-29 | 705.14 | -3.7% |
| SONATSOFTW | 2023-02-27 | 360.00 | 2023-03-29 | 371.45 | +3.2% |
| JSL | 2023-01-02 | 241.00 | 2023-04-13 | 256.98 | +6.6% |
| MOLDTECH | 2023-02-06 | 189.00 | 2023-07-03 | 292.84 | +54.9% |
| ANURAS | 2023-03-20 | 755.90 | 2023-07-03 | 1,007.67 | +33.3% |
| HARIOMPIPE | 2023-01-02 | 363.95 | 2023-07-10 | 603.25 | +65.8% |
| KSB | 2023-04-10 | 451.00 | 2023-07-12 | 407.74 | -9.6% |
| SATIN | 2023-07-17 | 187.00 | 2023-08-25 | 207.10 | +10.7% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| HPL | 2023-07-10 | 173.00 | 2023-10-26 | 187.31 | +8.3% |
| GENUSPOWER | 2023-07-10 | 162.85 | 2023-11-16 | 234.03 | +43.7% |
| LINDEINDIA | 2023-08-28 | 6,050.00 | 2023-12-20 | 5,542.11 | -8.4% |
| TIIL | 2023-04-17 | 1,495.35 | 2024-01-17 | 2,337.00 | +56.3% |
| BALMLAWRIE | 2023-12-26 | 238.25 | 2024-02-12 | 240.49 | +0.9% |
| RVNL | 2024-01-23 | 332.00 | 2024-02-12 | 241.04 | -27.4% |
| GEEKAYWIRE | 2023-03-27 | 40.98 | 2024-03-06 | 48.29 | +17.9% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| GEPIL | 2023-11-20 | 218.00 | 2024-03-06 | 273.88 | +25.6% |
| AEGISCHEM | 2024-02-19 | 436.55 | 2024-03-13 | 394.30 | -9.7% |
| ZENTEC | 2023-07-17 | 595.40 | 2024-05-09 | 896.89 | +50.6% |
| SOLARINDS | 2023-11-20 | 7,500.00 | 2024-06-04 | 7,980.95 | +6.4% |
| SMSPHARMA | 2024-03-11 | 179.00 | 2024-06-04 | 181.36 | +1.3% |
| BHEL | 2024-03-11 | 259.10 | 2024-06-04 | 251.68 | -2.9% |
| BOSCHLTD | 2024-03-11 | 29,819.95 | 2024-06-04 | 29,015.09 | -2.7% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| ARE&M | 2024-06-10 | 1,450.00 | 2024-07-22 | 1,502.14 | +3.6% |
| NCC | 2024-06-10 | 327.60 | 2024-07-23 | 297.87 | -9.1% |
| JWL | 2024-05-13 | 490.00 | 2024-08-06 | 552.00 | +12.7% |
| AVANTIFEED | 2024-07-29 | 697.65 | 2024-09-09 | 650.13 | -6.8% |
| KSCL | 2024-07-29 | 1,068.40 | 2024-09-30 | 973.63 | -8.9% |
| DABUR | 2024-06-10 | 604.20 | 2024-10-03 | 602.49 | -0.3% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| GEOJITFSL | 2024-07-22 | 111.55 | 2024-10-07 | 138.18 | +23.9% |
| KIOCL | 2024-02-19 | 491.55 | 2024-10-22 | 342.29 | -30.4% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| KIRLPNU | 2024-11-04 | 1,698.00 | 2024-12-23 | 1,596.00 | -6.0% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| MOTISONS | 2024-09-16 | 272.00 | 2024-12-31 | 265.10 | -2.5% |
| PAYTM | 2024-10-28 | 747.70 | 2025-01-09 | 893.05 | +19.4% |
| GARFIBRES | 2024-11-25 | 956.00 | 2025-01-09 | 829.35 | -13.2% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| CAMLINFINE | 2025-01-06 | 137.04 | 2025-01-13 | 120.37 | -12.2% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| APOLLO | 2025-01-20 | 131.50 | 2025-02-17 | 110.19 | -16.2% |
| BSE | 2024-10-14 | 4,536.00 | 2025-02-28 | 4,954.63 | +9.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| TAJGVK | 2025-01-06 | 446.90 | 2025-04-02 | 453.34 | +1.4% |
| BAJAJHCARE | 2025-01-20 | 690.00 | 2025-04-07 | 521.14 | -24.5% |
| AVANTIFEED | 2025-03-17 | 842.55 | 2025-04-07 | 648.95 | -23.0% |
| ITDCEM | 2024-10-07 | 655.05 | 2025-04-11 | 524.92 | -19.9% |
| GRMOVER | 2025-03-10 | 252.00 | 2025-05-07 | 290.80 | +15.4% |
| VADILALIND | 2025-04-07 | 4,820.55 | 2025-05-30 | 5,401.40 | +12.0% |
| PREMEXPLN | 2025-05-26 | 520.00 | 2025-07-14 | 537.70 | +3.4% |
| TECHNOE | 2025-06-02 | 1,421.00 | 2025-07-24 | 1,467.84 | +3.3% |
| KPRMILL | 2025-05-12 | 1,302.00 | 2025-08-01 | 1,108.74 | -14.8% |
| JSWHL | 2024-11-11 | 15,500.00 | 2025-08-04 | 19,106.01 | +23.3% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| PUNJABCHEM | 2025-08-04 | 1,403.00 | 2025-08-18 | 1,208.88 | -13.8% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| SPIC | 2025-08-25 | 111.40 | 2025-09-23 | 97.50 | -12.5% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| BOMDYEING | 2025-07-28 | 181.45 | 2025-09-25 | 172.67 | -4.8% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| NETWEB | 2025-09-08 | 3,135.50 | 2025-11-06 | 3,515.95 | +12.1% |
| ORIENTTECH | 2025-10-06 | 440.00 | 2025-11-11 | 399.91 | -9.1% |
| PRAKASH | 2025-08-11 | 178.70 | 2025-11-14 | 147.31 | -17.6% |
| ANANDRATHI | 2025-07-21 | 1,313.00 | 2025-11-20 | 1,450.17 | +10.4% |
| SKYGOLD | 2025-10-27 | 370.00 | 2025-11-25 | 329.13 | -11.0% |
| MUFIN | 2025-11-10 | 121.00 | 2025-12-01 | 103.08 | -14.8% |
| PRECWIRE | 2025-11-17 | 272.00 | 2025-12-08 | 230.47 | -15.3% |
| LUMAXIND | 2025-09-29 | 4,863.80 | 2026-01-01 | 5,078.70 | +4.4% |
| KIRIINDUS | 2026-01-05 | 622.00 | 2026-01-08 | 525.16 | -15.6% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| NATCOPHARM | 2025-12-08 | 934.70 | 2026-01-20 | 825.79 | -11.7% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| GMRAIRPORT | 2025-12-15 | 103.95 | 2026-01-23 | 92.10 | -11.4% |
| MMFL | 2026-01-12 | 400.95 | 2026-01-27 | 370.50 | -7.6% |
| SILVER | 2025-10-20 | 166.50 | 2026-02-02 | 234.68 | +40.9% |
| GROWWSLVR | 2026-01-27 | 31.00 | 2026-02-02 | 22.32 | -28.0% |
| INFOBEAN | 2026-01-27 | 813.10 | 2026-02-27 | 770.07 | -5.3% |
| APEX | 2026-02-09 | 355.00 | 2026-02-27 | 389.22 | +9.6% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| HINDCOPPER | 2026-02-02 | 590.15 | 2026-03-12 | 528.63 | -10.4% |
| SILVERCASE | 2026-01-27 | 32.00 | 2026-03-23 | 20.91 | -34.7% |
| J&KBANK | 2026-03-02 | 116.20 | 2026-03-23 | 110.67 | -4.8% |
| AGIIL | 2026-01-12 | 295.60 | 2026-03-30 | 271.80 | -8.1% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| BAJAJHIND | 2026-04-06 | 17.08 | 2026-05-14 | 17.96 | +5.2% |
| E2E | 2026-02-23 | 2,914.00 | 2026-06-05 | 2,330.72 | -20.0% |
| NLCINDIA | 2026-05-18 | 351.55 | 2026-06-09 | 320.62 | -8.8% |
| NRBBEARING | 2026-06-15 | 438.00 | 2026-07-22 | 391.97 | -10.5% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-06-01_to_2026-09-11.csv` beside this report (2031 events in all).*

```
2020-06-08  ALEMBICLTD  BUY ₹9.78 at ₹56.40 (fresh Friday signal — ACCUMULATE: 2.95× weekly, month 2.79×, ladder rising; stop ₹44.84; charges ₹0.0116)
2020-06-08  COSMOFILMS  BUY ₹9.57 at ₹286.90 (fresh Friday signal — BUY: 1.76× weekly, month 1.66×, ladder rising; stop ₹221.62; charges ₹0.0113)
2020-06-08  EIDPARRY    BUY ₹9.88 at ₹219.00 (fresh Friday signal — BUY: 4.34× weekly, month 3.58×, ladder rising; stop ₹132.60; charges ₹0.0117)
2020-06-08  EIHAHOTELS  BUY ₹9.84 at ₹137.50 (fresh Friday signal — BUY: 3.47× weekly, month 7.29×, ladder rising; stop ₹110.67; charges ₹0.0117)
2020-06-08  MANGCHEFER  BUY ₹9.74 at ₹38.75 (fresh Friday signal — BUY: 2.14× weekly, month 1.72×, ladder rising; stop ₹30.64; charges ₹0.0115)
2020-06-08  RCF         BUY ₹9.75 at ₹45.20 (fresh Friday signal — BUY: 2.38× weekly, month 2.28×, ladder rising; stop ₹35.25; charges ₹0.0116)
2020-06-08  RELAXO      BUY ₹9.62 at ₹759.45 (fresh Friday signal — BUY: 1.89× weekly, month 1.81×, ladder rising; stop ₹603.77; charges ₹0.0114)
2020-06-08  STRTECH     BUY ₹9.78 at ₹112.00 (fresh Friday signal — BUY: 2.56× weekly, month 1.57×, ladder rising; stop ₹89.21; charges ₹0.0116)
2020-06-08  SUNFLAG     BUY ₹10.00 at ₹43.00 (fresh Friday signal — BUY: 5.47× weekly, month 2.36×, ladder rising; stop ₹24.38; charges ₹0.0118)
2020-06-08  TAJGVK      BUY ₹9.69 at ₹174.00 (fresh Friday signal — BUY: 1.90× weekly, month 1.62×, ladder rising; stop ₹107.73; charges ₹0.0115)
2020-06-16  EIHAHOTELS  SELL ₹7.90 at stop ₹110.67 (-19.5%, charges ₹0.0082) — the cash goes back to work at the next Friday screen
2020-06-22  DHANBANK    BUY ₹10.03 at ₹15.95 (fresh Friday signal — BUY: 9.57× weekly, month 4.60×, ladder rising; stop ₹9.66; charges ₹0.0119)
2020-07-14  DHANBANK    SELL ₹8.05 at stop ₹12.82 (-19.6%, charges ₹0.0083) — the cash goes back to work at the next Friday screen
2020-07-20  APOLLO      BUY ₹8.27 at ₹11.76 (fresh Friday signal — BUY: 8.19× weekly, month 7.62×, ladder rising; stop ₹9.39; charges ₹0.0098)
2020-07-28  RELAXO      SELL ₹7.63 at stop ₹603.77 (-20.5%, charges ₹0.0079) — the cash goes back to work at the next Friday screen
2020-07-31  MANGCHEFER  SELL ₹8.46 at stop ₹33.73 (-13.0%, charges ₹0.0088) — the cash goes back to work at the next Friday screen
2020-08-03  DYNPRO      BUY ₹10.37 at ₹200.00 (fresh Friday signal — BUY: 6.82× weekly, month 11.46×, ladder rising; stop ₹156.56; charges ₹0.0123)
2020-08-03  LINCOLN     BUY ₹5.72 at ₹191.80 (fresh Friday signal — ACCUMULATE: 4.53× weekly, month 3.32×, ladder rising; stop ₹156.51; charges ₹0.0068)
2020-08-17  EIDPARRY    SELL ₹12.29 at stop ₹273.03 (+24.7%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2020-08-24  APCOTEXIND  BUY ₹11.35 at ₹164.95 (fresh Friday signal — BUY: 8.08× weekly, month 5.83×, ladder rising; stop ₹119.51; charges ₹0.0134)
2020-08-28  COSMOFILMS  SELL ₹13.66 at stop ₹410.40 (+43.0%, charges ₹0.0142) — the cash goes back to work at the next Friday screen
2020-08-31  APCOTEXIND  SELL ₹10.43 at stop ₹151.95 (-7.9%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2020-08-31  DLINKINDIA  BUY ₹10.62 at ₹127.00 (fresh Friday signal — BUY: 5.59× weekly, month 7.20×, ladder rising; stop ₹95.28; charges ₹0.0126)
2020-08-31  DYNPRO      SELL ₹9.66 at stop ₹186.68 (-6.7%, charges ₹0.0100) — the cash goes back to work at the next Friday screen
2020-08-31  LINCOLN     SELL ₹6.67 at stop ₹224.20 (+16.9%, charges ₹0.0069) — the cash goes back to work at the next Friday screen
2020-09-07  INDIAMART   BUY ₹10.64 at ₹2,124.50 (fresh Friday signal — BUY: 2.47× weekly, month 1.96×, ladder rising; stop ₹1,655.61; charges ₹0.0126)
2020-09-07  POLYMED     BUY ₹9.45 at ₹449.70 (fresh Friday signal — BUY: 2.13× weekly, month 2.67×, ladder rising; stop ₹372.40; charges ₹0.0112)
2020-09-07  PRINCEPIPE  BUY ₹10.66 at ₹208.00 (fresh Friday signal — BUY: 3.47× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.0126)
2020-09-09  RCF         SELL ₹9.87 at stop ₹45.84 (+1.4%, charges ₹0.0102) — the cash goes back to work at the next Friday screen
2020-09-14  SATIA       BUY ₹9.87 at ₹122.00 (fresh Friday signal — ACCUMULATE: 2.86× weekly, month 6.16×, ladder rising; stop ₹102.97; charges ₹0.0117)
2020-09-22  DLINKINDIA  SELL ₹8.09 at stop ₹96.95 (-23.7%, charges ₹0.0084) — the cash goes back to work at the next Friday screen
2020-09-22  SATIA       SELL ₹8.31 at stop ₹102.97 (-15.6%, charges ₹0.0086) — the cash goes back to work at the next Friday screen
2020-09-22  SUNFLAG     SELL ₹9.21 at stop ₹39.67 (-7.7%, charges ₹0.0095) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹7.02 at stop ₹126.45 (-27.3%, charges ₹0.0073) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹10.70 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0127)
2020-09-28  SAKSOFT     BUY ₹10.74 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.0127)
2020-09-28  VIDHIING    BUY ₹10.72 at ₹111.70 (fresh Friday signal — BUY: 4.70× weekly, month 4.56×, ladder rising; stop ₹77.90; charges ₹0.0127)
2020-10-12  PRINCEPIPE  SELL ₹11.29 at stop ₹220.88 (+6.2%, charges ₹0.0117) — the cash goes back to work at the next Friday screen
2020-10-19  INDIAMART   SELL ₹11.57 at stop ₹2,315.62 (+9.0%, charges ₹0.0120) — the cash goes back to work at the next Friday screen
2020-10-19  SUBEX       BUY ₹10.57 at ₹15.55 (fresh Friday signal — BUY: 6.85× weekly, month 4.86×, ladder rising; stop ₹11.11; charges ₹0.0125)
2020-10-26  JUSTDIAL    BUY ₹10.51 at ₹584.00 (fresh Friday signal — BUY: 4.99× weekly, month 1.82×, ladder rising; stop ₹383.80; charges ₹0.0125)
2020-11-02  ALEMBICLTD  SELL ₹15.81 at stop ₹91.41 (+62.1%, charges ₹0.0164) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹7.60 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.0090)
2020-11-09  LASA        BUY ₹10.46 at ₹80.50 (fresh Friday signal — BUY: 3.08× weekly, month 2.96×, ladder rising; stop ₹65.41; charges ₹0.0124)
2020-12-02  VIDHIING    SELL ₹11.06 at stop ₹115.50 (+3.4%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-12-07  MANGCHEFER  BUY ₹10.79 at ₹40.75 (fresh Friday signal — BUY: 11.02× weekly, month 3.91×, ladder rising; stop ₹30.21; charges ₹0.0128)
2020-12-21  APOLLO      SELL ₹8.34 at stop ₹11.88 (+1.0%, charges ₹0.0086) — the cash goes back to work at the next Friday screen
2020-12-21  LASA        SELL ₹10.11 at stop ₹77.95 (-3.2%, charges ₹0.0105) — the cash goes back to work at the next Friday screen
2020-12-22  MANGCHEFER  SELL ₹10.03 at stop ₹37.95 (-6.9%, charges ₹0.0104) — the cash goes back to work at the next Friday screen
2020-12-28  ITDC        BUY ₹11.83 at ₹338.55 (fresh Friday signal — BUY: 10.22× weekly, month 4.03×, ladder rising; stop ₹247.29; charges ₹0.0140)
2020-12-28  PAISALO     BUY ₹11.72 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0139)
2021-01-18  ITDC        SELL ₹10.61 at stop ₹304.38 (-10.1%, charges ₹0.0110) — the cash goes back to work at the next Friday screen
2021-01-20  BORORENEW   SELL ₹18.83 at stop ₹247.59 (+148.3%, charges ₹0.0195) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹11.68 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.79×, ladder rising; stop ₹92.41; charges ₹0.0138)
2021-01-25  JUSTDIAL    SELL ₹11.18 at stop ₹622.35 (+6.6%, charges ₹0.0116) — the cash goes back to work at the next Friday screen
2021-01-25  MAHLOG      BUY ₹11.81 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹0.0140)
2021-01-25  SAKSOFT     SELL ₹9.17 at stop ₹341.10 (-14.4%, charges ₹0.0095) — the cash goes back to work at the next Friday screen
2021-01-25  TATAMOTORS  BUY ₹11.13 at ₹296.90 (fresh Friday signal — BUY: 3.10× weekly, month 2.05×, ladder rising; stop ₹171.38; charges ₹0.0132)
2021-01-29  HCLTECH     SELL ₹11.82 at stop ₹928.05 (+10.7%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹11.56 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.0137)
2021-02-01  GAEL        BUY ₹11.68 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.71× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.0138)
2021-02-01  MHRIL       BUY ₹8.92 at ₹224.00 (fresh Friday signal — BUY: 1.64× weekly, month 1.67×, ladder rising; stop ₹200.74; charges ₹0.0106)
2021-02-23  GAEL        SELL ₹10.23 at stop ₹62.70 (-12.3%, charges ₹0.0106) — the cash goes back to work at the next Friday screen
2021-03-01  RCF         BUY ₹10.23 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.13×, ladder rising; stop ₹50.16; charges ₹0.0121)
2021-03-17  RCF         SELL ₹10.10 at stop ₹79.16 (-1.1%, charges ₹0.0105) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹13.20 at stop ₹204.25 (+14.5%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2021-03-19  MHRIL       SELL ₹8.38 at stop ₹210.90 (-5.8%, charges ₹0.0087) — the cash goes back to work at the next Friday screen
2021-03-19  TATAMOTORS  SELL ₹11.11 at stop ₹296.97 (+0.0%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2021-03-22  KEI         BUY ₹12.61 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.0149)
2021-03-22  VIDHIING    BUY ₹12.55 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0149)
2021-03-22  WELSPUNIND  BUY ₹12.68 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.42×, ladder rising; stop ₹67.45; charges ₹0.0150)
2021-04-01  TAX         FY2021 settled: ₹1.7002 paid (STCG ₹8.50 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-12  PAISALO     SELL ₹14.86 at stop ₹72.41 (+27.1%, charges ₹0.0154) — the cash goes back to work at the next Friday screen
2021-04-19  MOREPENLAB  BUY ₹12.20 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹0.0145)
2021-06-14  POLYMED     SELL ₹19.91 at stop ₹950.00 (+111.3%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2021-06-18  VIDHIING    SELL ₹11.74 at stop ₹182.64 (-6.2%, charges ₹0.0122) — the cash goes back to work at the next Friday screen
2021-06-21  RIIL        BUY ₹15.16 at ₹758.50 (fresh Friday signal — BUY: 10.58× weekly, month 6.50×, ladder rising; stop ₹365.27; charges ₹0.0180)
2021-06-21  SOMANYCERA  BUY ₹15.08 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0179)
2021-07-27  RIIL        SELL ₹14.21 at stop ₹712.50 (-6.1%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2021-08-02  GNA         BUY ₹16.41 at ₹328.00 (fresh Friday signal — BUY: 5.92× weekly, month 3.92×, ladder rising; stop ₹238.02; charges ₹0.0194)
2021-08-10  MOREPENLAB  SELL ₹18.31 at stop ₹56.33 (+50.4%, charges ₹0.0190) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNIND  SELL ₹19.36 at stop ₹124.64 (+53.0%, charges ₹0.0201) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹15.77 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.0187)
2021-08-16  INDOCO      BUY ₹11.28 at ₹484.30 (fresh Friday signal — BUY: 4.80× weekly, month 2.73×, ladder rising; stop ₹412.30; charges ₹0.0134)
2021-08-16  TATAINVEST  BUY ₹15.75 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0187)
2021-09-20  GDL         SELL ₹19.63 at stop ₹266.00 (+68.4%, charges ₹0.0204) — the cash goes back to work at the next Friday screen
2021-09-27  NEOGEN      BUY ₹16.77 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0199)
2021-10-19  GNA         SELL ₹24.42 at stop ₹489.25 (+49.2%, charges ₹0.0253) — the cash goes back to work at the next Friday screen
2021-10-22  KEI         SELL ₹20.57 at stop ₹853.10 (+63.4%, charges ₹0.0213) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹13.77 at stop ₹3,220.59 (-12.5%, charges ₹0.0143) — the cash goes back to work at the next Friday screen
2021-10-25  LTI         BUY ₹16.93 at ₹6,555.00 (fresh Friday signal — BUY: 4.63× weekly, month 1.84×, ladder rising; stop ₹5,353.77; charges ₹0.0201)
2021-10-25  NEOGEN      SELL ₹15.24 at stop ₹1,142.85 (-8.9%, charges ₹0.0158) — the cash goes back to work at the next Friday screen
2021-10-25  NHPC        BUY ₹14.13 at ₹32.90 (fresh Friday signal — BUY: 3.94× weekly, month 2.28×, ladder rising; stop ₹27.60; charges ₹0.0167)
2021-10-25  SHOPERSTOP  BUY ₹16.79 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹0.0199)
2021-11-01  TCIEXP      BUY ₹12.37 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0147)
2021-11-01  TTKPRESTIG  BUY ₹16.63 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.0197)
2021-11-12  INDOCO      SELL ₹9.58 at stop ₹412.30 (-14.9%, charges ₹0.0099) — the cash goes back to work at the next Friday screen
2021-11-15  ADSL        BUY ₹9.58 at ₹122.30 (fresh Friday signal — BUY: 5.56× weekly, month 3.06×, ladder rising; stop ₹77.80; charges ₹0.0114)
2021-11-22  SHOPERSTOP  SELL ₹17.25 at stop ₹335.82 (+3.0%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2021-11-26  TATAINVEST  SELL ₹17.26 at stop ₹1,436.49 (+9.8%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹15.14 at stop ₹10,070.05 (-8.8%, charges ₹0.0157) — the cash goes back to work at the next Friday screen
2021-11-29  BCG         BUY ₹16.61 at ₹134.10 (fresh Friday signal — BUY: 1.94× weekly, month 1.58×, ladder rising; stop ₹55.00; charges ₹0.0197)
2021-11-29  BSOFT       BUY ₹16.58 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.0196)
2021-11-29  NHPC        SELL ₹12.90 at stop ₹30.11 (-8.5%, charges ₹0.0134) — the cash goes back to work at the next Friday screen
2021-11-29  RAYMOND     BUY ₹16.41 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0194)
2021-11-29  SOMANYCERA  SELL ₹19.10 at stop ₹755.11 (+26.9%, charges ₹0.0198) — the cash goes back to work at the next Friday screen
2021-11-30  MAHLOG      SELL ₹15.55 at stop ₹654.55 (+32.0%, charges ₹0.0161) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹16.21 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0192)
2021-12-06  CHAMBLFERT  BUY ₹15.23 at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹0.0180)
2021-12-06  MIRZAINT    BUY ₹16.17 at ₹107.00 (fresh Friday signal — BUY: 3.65× weekly, month 3.62×, ladder rising; stop ₹73.21; charges ₹0.0192)
2021-12-21  TCIEXP      SELL ₹13.75 at stop ₹2,039.74 (+11.4%, charges ₹0.0143) — the cash goes back to work at the next Friday screen
2021-12-27  MINDAIND    BUY ₹13.75 at ₹1,180.00 (fresh Friday signal — BUY: 3.66× weekly, month 2.64×, ladder rising; stop ₹929.20; charges ₹0.0163)
2022-01-07  MINDAIND    SELL ₹12.66 at stop ₹1,088.41 (-7.8%, charges ₹0.0131) — the cash goes back to work at the next Friday screen
2022-01-10  ZEELEARN    BUY ₹12.66 at ₹17.80 (fresh Friday signal — BUY: 14.73× weekly, month 5.09×, ladder rising; stop ₹13.06; charges ₹0.0150)
2022-01-24  LTI         SELL ₹16.16 at stop ₹6,270.00 (-4.3%, charges ₹0.0168) — the cash goes back to work at the next Friday screen
2022-01-24  MIRZAINT    SELL ₹21.58 at stop ₹143.07 (+33.7%, charges ₹0.0224) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹17.15 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0203)
2022-01-31  TV18BRDCST  BUY ₹17.14 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.0203)
2022-02-11  SHARDACROP  SELL ₹15.91 at stop ₹545.30 (-7.1%, charges ₹0.0165) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹15.10 at stop ₹424.65 (-8.7%, charges ₹0.0157) — the cash goes back to work at the next Friday screen
2022-02-14  GNFC        BUY ₹16.43 at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹0.0195)
2022-02-15  RAYMOND     SELL ₹18.66 at stop ₹679.35 (+14.0%, charges ₹0.0194) — the cash goes back to work at the next Friday screen
2022-02-21  EVERESTIND  BUY ₹16.23 at ₹740.00 (fresh Friday signal — BUY: 3.34× weekly, month 1.68×, ladder rising; stop ₹522.67; charges ₹0.0192)
2022-02-22  TV18BRDCST  SELL ₹16.95 at stop ₹58.38 (-0.9%, charges ₹0.0176) — the cash goes back to work at the next Friday screen
2022-02-22  ZEELEARN    SELL ₹9.42 at stop ₹13.28 (-25.4%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹13.19 at stop ₹353.85 (-13.2%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2022-03-07  CGCL        BUY ₹15.51 at ₹600.00 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 3.19×, ladder rising; stop ₹536.75; charges ₹0.0184)
2022-03-07  EXCELINDUS  BUY ₹15.34 at ₹1,523.00 (fresh Friday signal — BUY: 6.93× weekly, month 5.51×, ladder rising; stop ₹1,016.01; charges ₹0.0182)
2022-03-07  GTLINFRA    BUY ₹13.72 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0163)
2022-03-07  MAWANASUG   BUY ₹15.45 at ₹115.00 (fresh Friday signal — ACCUMULATE: 2.21× weekly, month 7.30×, ladder rising; stop ₹84.08; charges ₹0.0183)
2022-03-21  BSE         SELL ₹13.99 at stop ₹1,634.39 (-13.5%, charges ₹0.0145) — the cash goes back to work at the next Friday screen
2022-03-29  EXCELINDUS  SELL ₹14.46 at stop ₹1,438.30 (-5.6%, charges ₹0.0150) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹9.4455 paid (STCG ₹47.23 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  RCF         BUY ₹15.37 at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.0182)
2022-04-28  EVERESTIND  SELL ₹13.01 at stop ₹594.70 (-19.6%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2022-04-29  GTLINFRA    SELL ₹11.35 at stop ₹1.41 (-17.1%, charges ₹0.0118) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹15.42 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.0183)
2022-05-02  RIIL        BUY ₹12.58 at ₹1,100.00 (fresh Friday signal — BUY: 5.17× weekly, month 3.64×, ladder rising; stop ₹852.81; charges ₹0.0149)
2022-05-04  RCF         SELL ₹14.82 at stop ₹93.15 (-3.4%, charges ₹0.0154) — the cash goes back to work at the next Friday screen
2022-05-06  GNFC        SELL ₹23.49 at stop ₹792.16 (+43.2%, charges ₹0.0244) — the cash goes back to work at the next Friday screen
2022-05-09  ADSL        SELL ₹10.54 at stop ₹134.90 (+10.3%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2022-05-09  JKIL        BUY ₹14.49 at ₹229.70 (fresh Friday signal — BUY: 6.96× weekly, month 3.58×, ladder rising; stop ₹192.28; charges ₹0.0172)
2022-05-09  MAWANASUG   SELL ₹18.11 at stop ₹135.09 (+17.5%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2022-05-09  MOL         BUY ₹14.51 at ₹129.80 (fresh Friday signal — BUY: 6.75× weekly, month 2.56×, ladder rising; stop ₹113.62; charges ₹0.0172)
2022-05-09  MRPL        BUY ₹9.30 at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹0.0110)
2022-05-11  MFL         SELL ₹13.19 at stop ₹1,225.50 (-14.3%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2022-05-11  MOL         SELL ₹12.67 at stop ₹113.62 (-12.5%, charges ₹0.0131) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹13.79 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0163)
2022-05-23  ACC         BUY ₹13.88 at ₹2,260.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹0.0164)
2022-05-23  GRAUWEIL    BUY ₹13.98 at ₹82.70 (fresh Friday signal — BUY: 5.06× weekly, month 7.54×, ladder rising; stop ₹56.42; charges ₹0.0166)
2022-05-23  VADILALIND  BUY ₹12.86 at ₹1,805.00 (fresh Friday signal — BUY: 1.51× weekly, month 1.94×, ladder rising; stop ₹1,567.50; charges ₹0.0152)
2022-05-26  RIIL        SELL ₹9.85 at stop ₹863.73 (-21.5%, charges ₹0.0102) — the cash goes back to work at the next Friday screen
2022-06-06  BCG         SELL ₹6.80 at stop ₹55.00 (-59.0%, charges ₹0.0070) — the cash goes back to work at the next Friday screen
2022-06-06  SHANTIGEAR  BUY ₹9.85 at ₹238.05 (fresh Friday signal — BUY: 1.57× weekly, month 2.31×, ladder rising; stop ₹179.53; charges ₹0.0117)
2022-06-06  VBL         SELL ₹12.27 at stop ₹196.27 (-10.8%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹13.95 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0165)
2022-06-13  GRAUWEIL    SELL ₹10.43 at stop ₹61.82 (-25.2%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹13.05 at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹0.0155)
2022-07-06  MRPL        SELL ₹8.29 at stop ₹69.61 (-10.8%, charges ₹0.0086) — the cash goes back to work at the next Friday screen
2022-07-11  MARATHON    BUY ₹10.78 at ₹215.00 (fresh Friday signal — BUY: 2.48× weekly, month 6.64×, ladder rising; stop ₹186.25; charges ₹0.0128)
2022-08-05  JKIL        SELL ₹19.44 at stop ₹308.80 (+34.4%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2022-08-08  NAVNETEDUL  BUY ₹15.03 at ₹130.50 (fresh Friday signal — BUY: 14.73× weekly, month 3.84×, ladder rising; stop ₹88.40; charges ₹0.0178)
2022-09-19  MARATHON    SELL ₹11.65 at stop ₹232.80 (+8.3%, charges ₹0.0121) — the cash goes back to work at the next Friday screen
2022-09-26  HEIDELBERG  BUY ₹15.67 at ₹205.20 (fresh Friday signal — BUY: 9.09× weekly, month 6.26×, ladder rising; stop ₹180.55; charges ₹0.0186)
2022-09-26  NAVNETEDUL  SELL ₹14.63 at stop ₹127.30 (-2.5%, charges ₹0.0152) — the cash goes back to work at the next Friday screen
2022-10-03  WESTLIFE    BUY ₹15.01 at ₹728.00 (fresh Friday signal — ACCUMULATE: 2.19× weekly, month 1.94×, ladder rising; stop ₹633.65; charges ₹0.0178)
2022-10-20  VADILALIND  SELL ₹16.32 at stop ₹2,295.06 (+27.2%, charges ₹0.0169) — the cash goes back to work at the next Friday screen
2022-10-24  JTLINFRA    BUY ₹16.08 at ₹292.00 (fresh Friday signal — ACCUMULATE: 5.50× weekly, month 7.34×, ladder rising; stop ₹217.12; charges ₹0.0190)
2022-11-03  APARINDS    SELL ₹18.62 at stop ₹1,358.50 (+43.0%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹16.65 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0197)
2022-12-21  ELECON      SELL ₹23.01 at stop ₹202.49 (+65.3%, charges ₹0.0239) — the cash goes back to work at the next Friday screen
2022-12-21  HEIDELBERG  SELL ₹14.48 at stop ₹190.00 (-7.4%, charges ₹0.0150) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹14.27 at stop ₹345.56 (+45.2%, charges ₹0.0148) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹15.11 at stop ₹2,465.16 (+9.1%, charges ₹0.0157) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹16.60 at stop ₹139.84 (-0.1%, charges ₹0.0172) — the cash goes back to work at the next Friday screen
2023-01-02  GICRE       BUY ₹16.18 at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 11.18×, ladder rising; stop ₹137.57; charges ₹0.0192)
2023-01-02  HARIOMPIPE  BUY ₹16.20 at ₹363.95 (fresh Friday signal — ACCUMULATE: 5.91× weekly, month 2.06×, ladder rising; stop ₹264.86; charges ₹0.0192)
2023-01-02  IOB         BUY ₹16.22 at ₹32.40 (fresh Friday signal — ACCUMULATE: 4.77× weekly, month 30.16×, ladder rising; stop ₹21.23; charges ₹0.0192)
2023-01-02  JSL         BUY ₹16.26 at ₹241.00 (fresh Friday signal — BUY: 2.29× weekly, month 2.13×, ladder rising; stop ₹192.61; charges ₹0.0193)
2023-01-02  SPIC        BUY ₹16.17 at ₹88.25 (fresh Friday signal — BUY: 4.81× weekly, month 3.70×, ladder rising; stop ₹54.66; charges ₹0.0192)
2023-01-16  WESTLIFE    SELL ₹14.57 at stop ₹708.51 (-2.7%, charges ₹0.0151) — the cash goes back to work at the next Friday screen
2023-01-23  SPECIALITY  BUY ₹16.04 at ₹276.85 (fresh Friday signal — BUY: 6.67× weekly, month 2.61×, ladder rising; stop ₹221.73; charges ₹0.0190)
2023-02-01  GICRE       SELL ₹15.11 at stop ₹167.72 (-6.4%, charges ₹0.0157) — the cash goes back to work at the next Friday screen
2023-02-06  MOLDTECH    BUY ₹15.53 at ₹189.00 (fresh Friday signal — BUY: 3.10× weekly, month 4.84×, ladder rising; stop ₹142.35; charges ₹0.0184)
2023-02-14  SPECIALITY  SELL ₹12.82 at stop ₹221.73 (-19.9%, charges ₹0.0133) — the cash goes back to work at the next Friday screen
2023-02-17  CGCL        SELL ₹18.18 at stop ₹704.95 (+17.5%, charges ₹0.0189) — the cash goes back to work at the next Friday screen
2023-02-20  ATULAUTO    BUY ₹15.56 at ₹387.95 (fresh Friday signal — BUY: 1.96× weekly, month 4.05×, ladder rising; stop ₹335.92; charges ₹0.0184)
2023-02-20  CIGNITITEC  BUY ₹15.61 at ₹731.95 (fresh Friday signal — BUY: 2.05× weekly, month 1.77×, ladder rising; stop ₹568.10; charges ₹0.0185)
2023-02-23  SPIC        SELL ₹12.02 at stop ₹65.74 (-25.5%, charges ₹0.0125) — the cash goes back to work at the next Friday screen
2023-02-27  SONATSOFTW  BUY ₹14.61 at ₹360.00 (fresh Friday signal — BUY: 9.70× weekly, month 3.45×, ladder rising; stop ₹282.62; charges ₹0.0173)
2023-03-13  ATULAUTO    SELL ₹13.44 at stop ₹335.92 (-13.4%, charges ₹0.0139) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹13.44 at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.57×, ladder rising; stop ₹691.46; charges ₹0.0159)
2023-03-20  IOB         SELL ₹11.08 at stop ₹22.18 (-31.5%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2023-03-27  GEEKAYWIRE  BUY ₹11.08 at ₹40.98 (fresh Friday signal — BUY: 2.59× weekly, month 3.65×, ladder rising; stop ₹30.40; charges ₹0.0131)
2023-03-29  CIGNITITEC  SELL ₹15.01 at stop ₹705.14 (-3.7%, charges ₹0.0156) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹15.04 at stop ₹371.45 (+3.2%, charges ₹0.0156) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹15.71 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.0186)
2023-04-03  TAX         FY2023 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹2.87 / LT ₹0.00)
2023-04-10  KSB         BUY ₹14.34 at ₹451.00 (fresh Friday signal — BUY: 2.21× weekly, month 2.22×, ladder rising; stop ₹372.21; charges ₹0.0170)
2023-04-13  JSL         SELL ₹17.30 at stop ₹256.98 (+6.6%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2023-04-17  TIIL        BUY ₹16.40 at ₹1,495.35 (fresh Friday signal — BUY: 3.27× weekly, month 2.15×, ladder rising; stop ₹1,036.90; charges ₹0.0194)
2023-07-03  ANURAS      SELL ₹17.88 at stop ₹1,007.67 (+33.3%, charges ₹0.0185) — the cash goes back to work at the next Friday screen
2023-07-03  MOLDTECH    SELL ₹24.01 at stop ₹292.84 (+54.9%, charges ₹0.0249) — the cash goes back to work at the next Friday screen
2023-07-10  GENUSPOWER  BUY ₹18.04 at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.48×, ladder rising; stop ₹99.51; charges ₹0.0214)
2023-07-10  HARIOMPIPE  SELL ₹26.79 at stop ₹603.25 (+65.8%, charges ₹0.0278) — the cash goes back to work at the next Friday screen
2023-07-10  HPL         BUY ₹18.04 at ₹173.00 (fresh Friday signal — BUY: 7.50× weekly, month 5.53×, ladder rising; stop ₹121.17; charges ₹0.0214)
2023-07-12  KSB         SELL ₹12.93 at stop ₹407.74 (-9.6%, charges ₹0.0134) — the cash goes back to work at the next Friday screen
2023-07-17  SATIN       BUY ₹18.96 at ₹187.00 (fresh Friday signal — ACCUMULATE: 5.33× weekly, month 5.21×, ladder rising; stop ₹157.75; charges ₹0.0225)
2023-07-17  ZENTEC      BUY ₹18.92 at ₹595.40 (fresh Friday signal — BUY: 8.06× weekly, month 3.59×, ladder rising; stop ₹364.54; charges ₹0.0224)
2023-08-25  SATIN       SELL ₹20.95 at stop ₹207.10 (+10.7%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2023-08-28  LINDEINDIA  BUY ₹21.11 at ₹6,050.00 (fresh Friday signal — BUY: 8.50× weekly, month 2.50×, ladder rising; stop ₹4,628.40; charges ₹0.0250)
2023-10-25  HAL         SELL ₹20.91 at stop ₹1,840.70 (+33.4%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2023-10-26  HPL         SELL ₹19.49 at stop ₹187.31 (+8.3%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹20.51 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0243)
2023-10-30  SHAREINDIA  BUY ₹20.53 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0243)
2023-11-16  GENUSPOWER  SELL ₹25.86 at stop ₹234.03 (+43.7%, charges ₹0.0268) — the cash goes back to work at the next Friday screen
2023-11-20  GEPIL       BUY ₹21.07 at ₹218.00 (fresh Friday signal — BUY: 4.38× weekly, month 2.06×, ladder rising; stop ₹158.46; charges ₹0.0250)
2023-11-20  SOLARINDS   BUY ₹12.53 at ₹7,500.00 (fresh Friday signal — BUY: 3.85× weekly, month 2.17×, ladder rising; stop ₹4,746.06; charges ₹0.0148)
2023-12-20  LINDEINDIA  SELL ₹19.29 at stop ₹5,542.11 (-8.4%, charges ₹0.0200) — the cash goes back to work at the next Friday screen
2023-12-26  BALMLAWRIE  BUY ₹19.29 at ₹238.25 (fresh Friday signal — BUY: 6.98× weekly, month 5.17×, ladder rising; stop ₹158.70; charges ₹0.0229)
2024-01-17  TIIL        SELL ₹25.58 at stop ₹2,337.00 (+56.3%, charges ₹0.0265) — the cash goes back to work at the next Friday screen
2024-01-23  RVNL        BUY ₹21.80 at ₹332.00 (fresh Friday signal — BUY: 6.89× weekly, month 1.60×, ladder rising; stop ₹157.32; charges ₹0.0258)
2024-02-12  BALMLAWRIE  SELL ₹19.43 at stop ₹240.49 (+0.9%, charges ₹0.0202) — the cash goes back to work at the next Friday screen
2024-02-12  RVNL        SELL ₹15.79 at stop ₹241.04 (-27.4%, charges ₹0.0164) — the cash goes back to work at the next Friday screen
2024-02-19  AEGISCHEM   BUY ₹21.77 at ₹436.55 (fresh Friday signal — BUY: 4.51× weekly, month 2.11×, ladder rising; stop ₹343.05; charges ₹0.0258)
2024-02-19  KIOCL       BUY ₹17.24 at ₹491.55 (fresh Friday signal — BUY: 4.30× weekly, month 2.57×, ladder rising; stop ₹318.79; charges ₹0.0204)
2024-03-06  GEEKAYWIRE  SELL ₹13.02 at stop ₹48.29 (+17.9%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2024-03-06  GEPIL       SELL ₹26.42 at stop ₹273.88 (+25.6%, charges ₹0.0274) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹24.39 at stop ₹357.20 (+19.1%, charges ₹0.0253) — the cash goes back to work at the next Friday screen
2024-03-11  BHEL        BUY ₹21.12 at ₹259.10 (fresh Friday signal — BUY: 3.01× weekly, month 1.67×, ladder rising; stop ₹188.78; charges ₹0.0250)
2024-03-11  BOSCHLTD    BUY ₹21.08 at ₹29,819.95 (fresh Friday signal — BUY: 1.81× weekly, month 2.03×, ladder rising; stop ₹26,525.90; charges ₹0.0250)
2024-03-11  SMSPHARMA   BUY ₹21.34 at ₹179.00 (fresh Friday signal — BUY: 8.20× weekly, month 12.63×, ladder rising; stop ₹132.95; charges ₹0.0253)
2024-03-13  AEGISCHEM   SELL ₹19.62 at stop ₹394.30 (-9.7%, charges ₹0.0203) — the cash goes back to work at the next Friday screen
2024-03-18  INDIGO      BUY ₹19.92 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0236)
2024-04-01  BHEL        TRIM 4.4% (₹0.91 at ₹253.75) to pay the tax bill
2024-04-01  BOSCHLTD    TRIM 4.4% (₹0.94 at ₹30,282.30) to pay the tax bill
2024-04-01  CUPID       TRIM 4.4% (₹1.39 at ₹186.62) to pay the tax bill
2024-04-01  INDIGO      TRIM 4.4% (₹0.97 at ₹3,548.95) to pay the tax bill
2024-04-01  JTLINFRA    TRIM 4.4% (₹0.72 at ₹295.80) to pay the tax bill
2024-04-01  KIOCL       TRIM 4.4% (₹0.63 at ₹411.25) to pay the tax bill
2024-04-01  SMSPHARMA   TRIM 4.4% (₹0.98 at ₹186.05) to pay the tax bill
2024-04-01  SOLARINDS   TRIM 4.4% (₹0.64 at ₹8,726.05) to pay the tax bill
2024-04-01  STRTECH     TRIM 4.4% (₹0.58 at ₹151.30) to pay the tax bill
2024-04-01  SUBEX       TRIM 4.4% (₹0.51 at ₹16.95) to pay the tax bill
2024-04-01  TAX         FY2024 settled: ₹9.5897 paid (STCG ₹47.95 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-01  ZENTEC      TRIM 4.4% (₹1.32 at ₹945.60) to pay the tax bill
2024-05-09  ZENTEC      SELL ₹27.19 at stop ₹896.89 (+50.6%, charges ₹0.0282) — the cash goes back to work at the next Friday screen
2024-05-13  JWL         BUY ₹21.40 at ₹490.00 (fresh Friday signal — BUY: 7.12× weekly, month 2.51×, ladder rising; stop ₹370.93; charges ₹0.0254)
2024-06-04  BHEL        SELL ₹19.57 at stop ₹251.68 (-2.9%, charges ₹0.0203) — the cash goes back to work at the next Friday screen
2024-06-04  BOSCHLTD    SELL ₹19.56 at stop ₹29,015.09 (-2.7%, charges ₹0.0203) — the cash goes back to work at the next Friday screen
2024-06-04  SMSPHARMA   SELL ₹20.62 at stop ₹181.36 (+1.3%, charges ₹0.0214) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹12.72 at stop ₹7,980.95 (+6.4%, charges ₹0.0132) — the cash goes back to work at the next Friday screen
2024-06-10  ARE&M       BUY ₹21.61 at ₹1,450.00 (fresh Friday signal — BUY: 3.00× weekly, month 2.35×, ladder rising; stop ₹916.60; charges ₹0.0256)
2024-06-10  DABUR       BUY ₹21.56 at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹0.0255)
2024-06-10  NCC         BUY ₹13.47 at ₹327.60 (fresh Friday signal — BUY: 2.80× weekly, month 1.63×, ladder rising; stop ₹260.92; charges ₹0.0160)
2024-06-10  UNOMINDA    BUY ₹21.61 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0256)
2024-07-19  UNOMINDA    SELL ₹21.83 at stop ₹981.87 (+1.2%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2024-07-22  ARE&M       SELL ₹22.34 at stop ₹1,502.14 (+3.6%, charges ₹0.0232) — the cash goes back to work at the next Friday screen
2024-07-22  GEOJITFSL   BUY ₹21.83 at ₹111.55 (fresh Friday signal — BUY: 3.55× weekly, month 1.64×, ladder rising; stop ₹90.61; charges ₹0.0259)
2024-07-23  NCC         SELL ₹12.22 at stop ₹297.87 (-9.1%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹21.84 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0259)
2024-07-29  KSCL        BUY ₹12.72 at ₹1,068.40 (fresh Friday signal — BUY: 5.64× weekly, month 1.78×, ladder rising; stop ₹875.38; charges ₹0.0151)
2024-08-06  JWL         SELL ₹24.06 at stop ₹552.00 (+12.7%, charges ₹0.0250) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹21.19 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0251)
2024-09-09  AVANTIFEED  SELL ₹20.30 at stop ₹650.13 (-6.8%, charges ₹0.0211) — the cash goes back to work at the next Friday screen
2024-09-16  MOTISONS    BUY ₹22.47 at ₹272.00 (fresh Friday signal — BUY: 9.68× weekly, month 2.93×, ladder rising; stop ₹164.70; charges ₹0.0266)
2024-09-30  KSCL        SELL ₹11.57 at stop ₹973.63 (-8.9%, charges ₹0.0120) — the cash goes back to work at the next Friday screen
2024-10-03  DABUR       SELL ₹21.45 at stop ₹602.49 (-0.3%, charges ₹0.0222) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹21.49 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0255)
2024-10-07  GEOJITFSL   SELL ₹26.98 at stop ₹138.18 (+23.9%, charges ₹0.0280) — the cash goes back to work at the next Friday screen
2024-10-07  INDIGO      SELL ₹26.63 at stop ₹4,485.14 (+40.2%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2024-10-07  ITDCEM      BUY ₹12.23 at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹0.0145)
2024-10-14  BSE         BUY ₹21.68 at ₹4,536.00 (fresh Friday signal — BUY: 2.79× weekly, month 4.25×, ladder rising; stop ₹3,393.93; charges ₹0.0257)
2024-10-14  SKIPPER     BUY ₹21.57 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0256)
2024-10-22  BASF        SELL ₹21.89 at stop ₹7,611.30 (+3.6%, charges ₹0.0227) — the cash goes back to work at the next Friday screen
2024-10-22  KIOCL       SELL ₹11.45 at stop ₹342.29 (-30.4%, charges ₹0.0119) — the cash goes back to work at the next Friday screen
2024-10-28  CUPID       SELL ₹25.66 at stop ₹158.66 (+31.1%, charges ₹0.0266) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹17.94 at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.0213)
2024-11-04  AKZOINDIA   BUY ₹20.57 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.0485)
2024-11-04  KIRLPNU     BUY ₹20.45 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.0483)
2024-11-11  JSWHL       BUY ₹10.40 at ₹15,500.00 (fresh Friday signal — BUY: 8.83× weekly, month 3.54×, ladder rising; stop ₹8,434.53; charges ₹0.0245)
2024-11-14  ASTRAZEN    SELL ₹19.72 at stop ₹6,854.77 (-7.9%, charges ₹0.0438) — the cash goes back to work at the next Friday screen
2024-11-25  GARFIBRES   BUY ₹19.72 at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹0.0466)
2024-12-23  KIRLPNU     SELL ₹19.14 at stop ₹1,596.00 (-6.0%, charges ₹0.0425) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹15.51 at stop ₹3,423.18 (-24.2%, charges ₹0.0345) — the cash goes back to work at the next Friday screen
2024-12-30  KFINTECH    BUY ₹20.83 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.0492)
2024-12-31  MOTISONS    SELL ₹21.83 at stop ₹265.10 (-2.5%, charges ₹0.0485) — the cash goes back to work at the next Friday screen
2025-01-06  CAMLINFINE  BUY ₹15.55 at ₹137.04 (fresh Friday signal — BUY: 3.44× weekly, month 1.90×, ladder rising; stop ₹109.44; charges ₹0.0367)
2025-01-06  TAJGVK      BUY ₹20.09 at ₹446.90 (fresh Friday signal — BUY: 4.69× weekly, month 2.27×, ladder rising; stop ₹325.01; charges ₹0.0474)
2025-01-09  GARFIBRES   SELL ₹17.03 at stop ₹829.35 (-13.2%, charges ₹0.0378) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹21.35 at stop ₹893.05 (+19.4%, charges ₹0.0474) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹18.55 at stop ₹477.28 (-13.7%, charges ₹0.0412) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹18.88 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0446)
2025-01-13  CAMLINFINE  SELL ₹13.60 at stop ₹120.37 (-12.2%, charges ₹0.0302) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹18.83 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.0445)
2025-01-15  KFINTECH    SELL ₹15.90 at stop ₹1,159.14 (-23.3%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2025-01-20  APOLLO      BUY ₹19.11 at ₹131.50 (fresh Friday signal — ACCUMULATE: 1.93× weekly, month 3.48×, ladder rising; stop ₹110.19; charges ₹0.0451)
2025-01-20  BAJAJHCARE  BUY ₹19.39 at ₹690.00 (fresh Friday signal — BUY: 1.75× weekly, month 4.12×, ladder rising; stop ₹451.06; charges ₹0.0458)
2025-01-24  AEGISLOG    SELL ₹15.77 at stop ₹700.36 (-16.1%, charges ₹0.0350) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹17.69 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0418)
2025-01-28  LLOYDSME    SELL ₹16.37 at stop ₹1,258.75 (-12.7%, charges ₹0.0364) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹18.66 at ₹947.00 (fresh Friday signal — BUY: 2.25× weekly, month 2.40×, ladder rising; stop ₹727.84; charges ₹0.0440)
2025-02-17  APOLLO      SELL ₹15.94 at stop ₹110.19 (-16.2%, charges ₹0.0354) — the cash goes back to work at the next Friday screen
2025-02-28  BSE         SELL ₹23.60 at stop ₹4,954.63 (+9.2%, charges ₹0.0524) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹17.52 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0414)
2025-03-03  ZENSARTECH  SELL ₹14.28 at stop ₹727.84 (-23.1%, charges ₹0.0317) — the cash goes back to work at the next Friday screen
2025-03-10  GRMOVER     BUY ₹18.25 at ₹252.00 (fresh Friday signal — BUY: 1.55× weekly, month 1.68×, ladder rising; stop ₹203.86; charges ₹0.0431)
2025-03-17  AVANTIFEED  BUY ₹18.60 at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹0.0439)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹3.20 / LT ₹0.00)
2025-04-02  TAJGVK      SELL ₹20.29 at stop ₹453.34 (+1.4%, charges ₹0.0451) — the cash goes back to work at the next Friday screen
2025-04-07  AVANTIFEED  SELL ₹14.26 at stop ₹648.95 (-23.0%, charges ₹0.0317) — the cash goes back to work at the next Friday screen
2025-04-07  BAJAJHCARE  SELL ₹14.58 at stop ₹521.14 (-24.5%, charges ₹0.0324) — the cash goes back to work at the next Friday screen
2025-04-07  VADILALIND  BUY ₹18.46 at ₹4,820.55 (fresh Friday signal — BUY: 9.88× weekly, month 5.69×, ladder rising; stop ₹4,255.30; charges ₹0.0436)
2025-04-11  ITDCEM      SELL ₹9.77 at stop ₹524.92 (-19.9%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹18.82 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.0444)
2025-04-15  INDIASHLTR  BUY ₹18.90 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.0446)
2025-05-07  GRMOVER     SELL ₹20.97 at stop ₹290.80 (+15.4%, charges ₹0.0466) — the cash goes back to work at the next Friday screen
2025-05-12  KPRMILL     BUY ₹19.59 at ₹1,302.00 (fresh Friday signal — BUY: 15.99× weekly, month 3.16×, ladder rising; stop ₹938.50; charges ₹0.0463)
2025-05-26  PREMEXPLN   BUY ₹9.55 at ₹520.00 (fresh Friday signal — BUY: 4.83× weekly, month 13.10×, ladder rising; stop ₹403.75; charges ₹0.0225)
2025-05-30  VADILALIND  SELL ₹20.59 at stop ₹5,401.40 (+12.0%, charges ₹0.0457) — the cash goes back to work at the next Friday screen
2025-06-02  TECHNOE     BUY ₹18.60 at ₹1,421.00 (fresh Friday signal — BUY: 6.29× weekly, month 1.64×, ladder rising; stop ₹1,150.36; charges ₹0.0439)
2025-07-14  PREMEXPLN   SELL ₹9.82 at stop ₹537.70 (+3.4%, charges ₹0.0218) — the cash goes back to work at the next Friday screen
2025-07-21  ANANDRATHI  BUY ₹11.81 at ₹1,313.00 (fresh Friday signal — BUY: 9.57× weekly, month 3.05×, ladder rising; stop ₹966.20; charges ₹0.0279)
2025-07-24  TECHNOE     SELL ₹19.13 at stop ₹1,467.84 (+3.3%, charges ₹0.0425) — the cash goes back to work at the next Friday screen
2025-07-28  BOMDYEING   BUY ₹18.89 at ₹181.45 (fresh Friday signal — BUY: 21.87× weekly, month 4.30×, ladder rising; stop ₹148.64; charges ₹0.0446)
2025-08-01  KPRMILL     SELL ₹16.61 at stop ₹1,108.74 (-14.8%, charges ₹0.0369) — the cash goes back to work at the next Friday screen
2025-08-04  JSWHL       SELL ₹12.76 at stop ₹19,106.01 (+23.3%, charges ₹0.0283) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹21.83 at stop ₹1,814.78 (+25.2%, charges ₹0.0485) — the cash goes back to work at the next Friday screen
2025-08-04  PUNJABCHEM  BUY ₹16.85 at ₹1,403.00 (fresh Friday signal — BUY: 43.22× weekly, month 11.54×, ladder rising; stop ₹1,208.88; charges ₹0.0398)
2025-08-11  PRAKASH     BUY ₹16.66 at ₹178.70 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 2.58×, ladder rising; stop ₹145.68; charges ₹0.0393)
2025-08-11  RAIN        BUY ₹17.93 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.0423)
2025-08-18  PUNJABCHEM  SELL ₹14.45 at stop ₹1,208.88 (-13.8%, charges ₹0.0321) — the cash goes back to work at the next Friday screen
2025-08-25  SPIC        BUY ₹14.45 at ₹111.40 (fresh Friday signal — BUY: 8.68× weekly, month 5.72×, ladder rising; stop ₹77.81; charges ₹0.0341)
2025-08-26  RAIN        SELL ₹16.00 at stop ₹143.64 (-10.4%, charges ₹0.0355) — the cash goes back to work at the next Friday screen
2025-09-08  NETWEB      BUY ₹16.00 at ₹3,135.50 (fresh Friday signal — BUY: 6.14× weekly, month 4.02×, ladder rising; stop ₹2,081.16; charges ₹0.0378)
2025-09-23  SPIC        SELL ₹12.59 at stop ₹97.50 (-12.5%, charges ₹0.0280) — the cash goes back to work at the next Friday screen
2025-09-25  BOMDYEING   SELL ₹17.89 at stop ₹172.67 (-4.8%, charges ₹0.0397) — the cash goes back to work at the next Friday screen
2025-09-25  INDIASHLTR  SELL ₹18.76 at stop ₹862.60 (-0.3%, charges ₹0.0417) — the cash goes back to work at the next Friday screen
2025-09-29  LUMAXIND    BUY ₹17.79 at ₹4,863.80 (fresh Friday signal — BUY: 1.79× weekly, month 2.69×, ladder rising; stop ₹3,878.38; charges ₹0.0420)
2025-09-29  SUBROS      BUY ₹17.70 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0418)
2025-10-06  ORIENTTECH  BUY ₹13.75 at ₹440.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.58×, ladder rising; stop ₹320.10; charges ₹0.0324)
2025-10-14  SUBROS      SELL ₹16.29 at stop ₹1,046.90 (-7.5%, charges ₹0.0362) — the cash goes back to work at the next Friday screen
2025-10-20  CREDITACC   SELL ₹26.40 at stop ₹1,274.42 (+49.9%, charges ₹0.0586) — the cash goes back to work at the next Friday screen
2025-10-20  SILVER      BUY ₹16.29 at ₹166.50 (fresh Friday signal — BUY: 5.23× weekly, month 7.95×, ladder rising; stop ₹104.33; charges ₹0.0385)
2025-10-27  SKYGOLD     BUY ₹17.80 at ₹370.00 (fresh Friday signal — BUY: 1.65× weekly, month 2.25×, ladder rising; stop ₹304.38; charges ₹0.0420)
2025-11-06  NETWEB      SELL ₹17.86 at stop ₹3,515.95 (+12.1%, charges ₹0.0397) — the cash goes back to work at the next Friday screen
2025-11-10  CUB         BUY ₹17.22 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.0406)
2025-11-10  MUFIN       BUY ₹9.23 at ₹121.00 (fresh Friday signal — BUY: 4.87× weekly, month 7.06×, ladder rising; stop ₹89.40; charges ₹0.0218)
2025-11-11  ORIENTTECH  SELL ₹12.44 at stop ₹399.91 (-9.1%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2025-11-14  PRAKASH     SELL ₹13.67 at stop ₹147.31 (-17.6%, charges ₹0.0304) — the cash goes back to work at the next Friday screen
2025-11-17  PRECWIRE    BUY ₹17.51 at ₹272.00 (fresh Friday signal — BUY: 9.56× weekly, month 6.88×, ladder rising; stop ₹205.29; charges ₹0.0413)
2025-11-20  ANANDRATHI  SELL ₹12.98 at stop ₹1,450.17 (+10.4%, charges ₹0.0288) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹17.22 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0407)
2025-11-25  SKYGOLD     SELL ₹15.76 at stop ₹329.13 (-11.0%, charges ₹0.0350) — the cash goes back to work at the next Friday screen
2025-12-01  MUFIN       SELL ₹7.83 at stop ₹103.08 (-14.8%, charges ₹0.0174) — the cash goes back to work at the next Friday screen
2025-12-01  SANSERA     BUY ₹17.49 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.0413)
2025-12-08  NATCOPHARM  BUY ₹10.46 at ₹934.70 (fresh Friday signal — BUY: 3.52× weekly, month 3.33×, ladder rising; stop ₹825.79; charges ₹0.0247)
2025-12-08  PRECWIRE    SELL ₹14.77 at stop ₹230.47 (-15.3%, charges ₹0.0328) — the cash goes back to work at the next Friday screen
2025-12-15  GMRAIRPORT  BUY ₹14.77 at ₹103.95 (fresh Friday signal — BUY: 1.56× weekly, month 2.60×, ladder rising; stop ₹89.73; charges ₹0.0349)
2026-01-01  LUMAXIND    SELL ₹18.49 at stop ₹5,078.70 (+4.4%, charges ₹0.0411) — the cash goes back to work at the next Friday screen
2026-01-05  KIRIINDUS   BUY ₹18.06 at ₹622.00 (fresh Friday signal — BUY: 24.50× weekly, month 6.65×, ladder rising; stop ₹525.16; charges ₹0.0426)
2026-01-08  KIRIINDUS   SELL ₹15.18 at stop ₹525.16 (-15.6%, charges ₹0.0337) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹15.41 at stop ₹2,956.49 (-10.1%, charges ₹0.0342) — the cash goes back to work at the next Friday screen
2026-01-12  AGIIL       BUY ₹17.37 at ₹295.60 (fresh Friday signal — ACCUMULATE: 5.45× weekly, month 2.03×, ladder rising; stop ₹202.47; charges ₹0.0410)
2026-01-12  MMFL        BUY ₹13.65 at ₹400.95 (fresh Friday signal — BUY: 4.29× weekly, month 3.26×, ladder rising; stop ₹332.21; charges ₹0.0322)
2026-01-20  NATCOPHARM  SELL ₹9.20 at stop ₹825.79 (-11.7%, charges ₹0.0204) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹17.15 at stop ₹748.60 (-8.5%, charges ₹0.0381) — the cash goes back to work at the next Friday screen
2026-01-23  GMRAIRPORT  SELL ₹13.02 at stop ₹92.10 (-11.4%, charges ₹0.0289) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹16.65 at stop ₹1,672.76 (-4.4%, charges ₹0.0370) — the cash goes back to work at the next Friday screen
2026-01-27  GROWWSLVR   BUY ₹17.54 at ₹31.00 (fresh Friday signal — BUY: 5.65× weekly, month 5.51×, ladder rising; stop ₹19.45; charges ₹0.0414)
2026-01-27  INFOBEAN    BUY ₹17.73 at ₹813.10 (fresh Friday signal — ACCUMULATE: 3.29× weekly, month 6.74×, ladder rising; stop ₹683.81; charges ₹0.0418)
2026-01-27  MMFL        SELL ₹12.56 at stop ₹370.50 (-7.6%, charges ₹0.0279) — the cash goes back to work at the next Friday screen
2026-01-27  SILVERCASE  BUY ₹17.63 at ₹32.00 (fresh Friday signal — BUY: 5.18× weekly, month 9.06×, ladder rising; stop ₹20.91; charges ₹0.0416)
2026-02-02  GROWWSLVR   SELL ₹12.57 at stop ₹22.32 (-28.0%, charges ₹0.0279) — the cash goes back to work at the next Friday screen
2026-02-02  HINDCOPPER  BUY ₹15.49 at ₹590.15 (fresh Friday signal — BUY: 2.81× weekly, month 4.89×, ladder rising; stop ₹485.74; charges ₹0.0366)
2026-02-02  SILVER      SELL ₹22.86 at stop ₹234.68 (+40.9%, charges ₹0.0508) — the cash goes back to work at the next Friday screen
2026-02-09  APEX        BUY ₹15.70 at ₹355.00 (fresh Friday signal — BUY: 2.98× weekly, month 4.24×, ladder rising; stop ₹221.66; charges ₹0.0371)
2026-02-23  E2E         BUY ₹16.30 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0385)
2026-02-27  APEX        SELL ₹17.14 at stop ₹389.22 (+9.6%, charges ₹0.0381) — the cash goes back to work at the next Friday screen
2026-02-27  INFOBEAN    SELL ₹16.71 at stop ₹770.07 (-5.3%, charges ₹0.0371) — the cash goes back to work at the next Friday screen
2026-03-02  ABB         BUY ₹15.91 at ₹5,840.00 (fresh Friday signal — ACCUMULATE: 2.01× weekly, month 1.63×, ladder rising; stop ₹5,486.25; charges ₹0.0376)
2026-03-02  J&KBANK     BUY ₹15.86 at ₹116.20 (fresh Friday signal — BUY: 8.67× weekly, month 1.90×, ladder rising; stop ₹96.50; charges ₹0.0374)
2026-03-09  CUB         SELL ₹16.95 at stop ₹251.43 (-1.1%, charges ₹0.0377) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹13.81 at stop ₹528.63 (-10.4%, charges ₹0.0307) — the cash goes back to work at the next Friday screen
2026-03-16  APOLLOPIPE  BUY ₹15.52 at ₹407.55 (fresh Friday signal — BUY: 65.78× weekly, month 26.51×, ladder rising; stop ₹315.92; charges ₹0.0366)
2026-03-16  JBCHEPHARM  BUY ₹15.47 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0365)
2026-03-23  J&KBANK     SELL ₹15.04 at stop ₹110.67 (-4.8%, charges ₹0.0334) — the cash goes back to work at the next Friday screen
2026-03-23  SILVERCASE  SELL ₹11.46 at stop ₹20.91 (-34.7%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹14.87 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0351)
2026-03-30  AGIIL       SELL ₹15.90 at stop ₹271.80 (-8.1%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹28.68 / LT ₹0.00)
2026-04-06  BAJAJHIND   BUY ₹14.82 at ₹17.08 (fresh Friday signal — ACCUMULATE: 2.33× weekly, month 1.97×, ladder rising; stop ₹13.87; charges ₹0.0350)
2026-04-06  CHENNPETRO  BUY ₹14.84 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0350)
2026-05-14  AETHER      SELL ₹14.49 at stop ₹1,125.84 (-2.1%, charges ₹0.0322) — the cash goes back to work at the next Friday screen
2026-05-14  BAJAJHIND   SELL ₹15.51 at stop ₹17.96 (+5.2%, charges ₹0.0345) — the cash goes back to work at the next Friday screen
2026-05-18  CAPLIPOINT  BUY ₹15.37 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.0363)
2026-05-18  NLCINDIA    BUY ₹15.37 at ₹351.55 (fresh Friday signal — BUY: 5.83× weekly, month 6.05×, ladder rising; stop ₹278.49; charges ₹0.0363)
2026-06-05  E2E         SELL ₹12.98 at stop ₹2,330.72 (-20.0%, charges ₹0.0288) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹15.58 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0368)
2026-06-09  NLCINDIA    SELL ₹13.95 at stop ₹320.62 (-8.8%, charges ₹0.0310) — the cash goes back to work at the next Friday screen
2026-06-15  NRBBEARING  BUY ₹13.95 at ₹438.00 (fresh Friday signal — BUY: 10.53× weekly, month 6.95×, ladder rising; stop ₹331.98; charges ₹0.0329)
2026-07-22  NRBBEARING  SELL ₹12.43 at stop ₹391.97 (-10.5%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2026-07-27  BLUESTONE   BUY ₹12.43 at ₹793.00 (fresh Friday signal — BUY: 47.94× weekly, month 6.10×, ladder rising; stop ₹559.17; charges ₹0.0293)
```
