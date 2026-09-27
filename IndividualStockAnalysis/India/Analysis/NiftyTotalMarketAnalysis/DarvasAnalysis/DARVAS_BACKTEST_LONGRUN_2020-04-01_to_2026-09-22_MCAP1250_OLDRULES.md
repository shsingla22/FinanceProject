# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 2272 symbols, fetched once into `ROLLING_MCAP1250_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹158.87** | **+7.42% a year** |
| The same system before costs and taxes | ₹188.65 | +10.31% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹288.59 | +17.80% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹158.87** (+7.42% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 453 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹10.61** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹21.37**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹3.64 | ₹0.00 | ₹0.7285 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹25.63 | ₹0.00 | ₹5.1250 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹8.63 | ₹15.71 | ₹3.6897 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹59.15 | ₹0.00 | ₹11.8291 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹13.55 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹38.53 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹37.59 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 111.13 | +11.1% | +11.6% | +70.1% |
| 2021 (2021-12-31) | 146.80 | +32.1% | +33.9% | +26.2% |
| 2022 (2022-12-30) | 176.29 | +20.1% | +24.1% | +4.3% |
| 2023 (2023-12-29) | 219.61 | +24.6% | +28.9% | +20.0% |
| 2024 (2024-12-27) | 212.82 | -3.1% | +2.9% | +9.6% |
| 2025 (2025-12-26) | 163.09 | -23.4% | -21.9% | +9.4% |
| 2026 (2026-09-22) | 158.87 | -2.6% | -1.9% | -10.4% |

## What it took to earn it

- **Maximum drawdown: -38.7%** (peak 2024-09-13 → trough 2026-04-02, on weekly closes).
- **213 closed trades**: 79 winners (37%), average winner +29.3%, average loser -12.0%.
- Best closed trade 21STCENMGM +281.0%; worst MRPL -40.3%.
- Median holding period 60 days.
- Cash share of equity averaged 9% across all weeks (median 4%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.20 | 59.96 | 4 |
| 2020-05-29 | 112.49 | 0.00 | 10 |
| 2020-06-26 | 118.63 | 0.00 | 10 |
| 2020-07-31 | 126.84 | 23.71 | 8 |
| 2020-08-28 | 128.72 | 0.00 | 10 |
| 2020-09-25 | 120.22 | 23.55 | 7 |
| 2020-10-30 | 117.95 | 6.17 | 8 |
| 2020-11-27 | 111.54 | 0.96 | 9 |
| 2020-12-24 | 111.13 | 61.76 | 4 |
| 2021-01-29 | 111.77 | 20.08 | 8 |
| 2021-02-26 | 121.31 | 3.17 | 9 |
| 2021-03-26 | 115.54 | 15.00 | 8 |
| 2021-04-30 | 114.02 | 0.00 | 10 |
| 2021-05-28 | 127.17 | 0.00 | 10 |
| 2021-06-25 | 140.66 | 0.00 | 10 |
| 2021-07-30 | 140.74 | 10.88 | 9 |
| 2021-08-27 | 134.29 | 15.77 | 8 |
| 2021-09-24 | 142.43 | 19.02 | 8 |
| 2021-10-29 | 145.92 | 18.37 | 8 |
| 2021-11-26 | 146.73 | 26.05 | 7 |
| 2021-12-31 | 146.80 | 14.02 | 10 |
| 2022-01-28 | 147.76 | 41.05 | 8 |
| 2022-02-25 | 132.18 | 11.21 | 10 |
| 2022-03-25 | 142.14 | 23.91 | 9 |
| 2022-04-29 | 146.04 | 2.30 | 10 |
| 2022-05-27 | 159.71 | 0.00 | 10 |
| 2022-06-24 | 154.14 | 0.00 | 10 |
| 2022-07-29 | 165.54 | 7.16 | 9 |
| 2022-08-26 | 182.24 | 7.16 | 9 |
| 2022-09-30 | 172.65 | 25.11 | 8 |
| 2022-10-28 | 183.60 | 7.84 | 9 |
| 2022-11-25 | 187.70 | 7.86 | 9 |
| 2022-12-30 | 176.29 | 31.78 | 8 |
| 2023-01-27 | 165.57 | 28.00 | 8 |
| 2023-02-24 | 153.69 | 2.84 | 9 |
| 2023-03-31 | 147.32 | 72.03 | 5 |
| 2023-04-28 | 158.80 | 0.00 | 10 |
| 2023-05-26 | 165.49 | 0.00 | 10 |
| 2023-06-30 | 174.77 | 0.00 | 10 |
| 2023-07-28 | 175.59 | 0.00 | 10 |
| 2023-08-25 | 191.57 | 0.00 | 10 |
| 2023-09-29 | 195.28 | 17.32 | 9 |
| 2023-10-27 | 190.94 | 36.76 | 9 |
| 2023-11-24 | 206.08 | 12.60 | 10 |
| 2023-12-29 | 219.61 | 0.00 | 11 |
| 2024-01-25 | 224.61 | 26.75 | 10 |
| 2024-02-23 | 234.46 | 0.00 | 11 |
| 2024-03-28 | 218.36 | 0.00 | 11 |
| 2024-04-26 | 224.32 | 0.00 | 11 |
| 2024-05-31 | 221.51 | 24.97 | 10 |
| 2024-06-28 | 219.95 | 7.53 | 10 |
| 2024-07-26 | 240.46 | 45.91 | 8 |
| 2024-08-30 | 237.57 | 2.37 | 10 |
| 2024-09-27 | 232.49 | 6.31 | 10 |
| 2024-10-25 | 214.28 | 19.28 | 10 |
| 2024-11-29 | 213.61 | 2.88 | 10 |
| 2024-12-27 | 212.82 | 54.35 | 7 |
| 2025-01-31 | 190.81 | 90.87 | 5 |
| 2025-02-28 | 176.41 | 59.37 | 7 |
| 2025-03-28 | 187.33 | 16.39 | 9 |
| 2025-04-25 | 196.73 | 9.45 | 9 |
| 2025-05-30 | 184.60 | 19.89 | 9 |
| 2025-06-27 | 196.75 | 0.00 | 10 |
| 2025-07-25 | 198.02 | 0.00 | 10 |
| 2025-08-29 | 186.66 | 17.08 | 9 |
| 2025-09-26 | 187.31 | 41.14 | 8 |
| 2025-10-31 | 180.18 | 0.00 | 11 |
| 2025-11-28 | 171.90 | 22.81 | 9 |
| 2025-12-26 | 163.09 | 7.75 | 10 |
| 2026-01-30 | 151.48 | 44.67 | 7 |
| 2026-02-27 | 156.21 | 39.93 | 8 |
| 2026-03-27 | 148.35 | 30.43 | 8 |
| 2026-04-30 | 159.77 | 0.94 | 10 |
| 2026-05-29 | 167.78 | 3.75 | 10 |
| 2026-06-25 | 157.15 | 0.00 | 10 |
| 2026-07-31 | 156.93 | 0.00 | 10 |
| 2026-08-28 | 164.61 | 0.00 | 10 |
| 2026-09-22 | 158.87 | 2.49 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| APOLLOPIPE | 2026-03-16 | 407.55 | 526.10 | 468.60 | +29.1% |
| AVTNPL | 2026-08-24 | 87.80 | 98.26 | 62.04 | +11.9% |
| BLUESTONE | 2026-07-27 | 793.00 | 930.40 | 758.29 | +17.3% |
| CRAFTSMAN | 2026-05-11 | 9,039.50 | 10,602.00 | 10,380.65 | +17.3% |
| FOSECOIND | 2026-09-21 | 6,748.00 | 6,562.00 | 5,714.73 | -2.8% |
| HARITASEAT | 2021-02-01 | 532.00 | 766.55 | 676.59 | +44.1% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| NPST | 2026-09-21 | 1,820.00 | 1,888.80 | 1,539.95 | +3.8% |
| NRBBEARING | 2026-09-21 | 531.10 | 520.50 | 430.82 | -2.0% |
| SHOPERSTOP | 2026-09-21 | 398.60 | 392.50 | 351.39 | -1.5% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| ORIENTBELL | 2020-06-22 | 106.75 | 2020-07-20 | 72.28 | -32.3% |
| VINYLINDIA | 2020-05-18 | 62.55 | 2020-07-27 | 84.55 | +35.2% |
| MANGCHEFER | 2020-05-11 | 33.75 | 2020-07-31 | 33.73 | -0.1% |
| PANACEABIO | 2020-06-15 | 230.00 | 2020-08-20 | 184.01 | -20.0% |
| DYNPRO | 2020-08-03 | 200.00 | 2020-08-31 | 186.68 | -6.7% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| ASAHISONG | 2020-07-27 | 207.35 | 2020-09-01 | 186.89 | -9.9% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| TIPSINDLTD | 2020-09-07 | 23.19 | 2020-09-22 | 22.08 | -4.8% |
| SASTASUNDR | 2020-08-24 | 107.00 | 2020-10-28 | 83.12 | -22.3% |
| HATHWAY | 2020-05-18 | 24.50 | 2020-11-09 | 28.34 | +15.7% |
| VIDHIING | 2020-09-28 | 111.70 | 2020-12-02 | 115.50 | +3.4% |
| APOLLO | 2020-05-18 | 8.70 | 2020-12-21 | 11.88 | +36.6% |
| TEXMOPIPES | 2020-11-02 | 16.30 | 2020-12-21 | 18.83 | +15.5% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| TCI | 2020-09-14 | 242.00 | 2020-12-22 | 234.75 | -3.0% |
| MANGCHEFER | 2020-12-07 | 40.75 | 2020-12-22 | 37.95 | -6.9% |
| ITDC | 2020-12-28 | 338.55 | 2021-01-18 | 304.38 | -10.1% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| TERASOFT | 2020-12-28 | 51.25 | 2021-01-27 | 44.32 | -13.5% |
| VESUVIUS | 2020-12-28 | 109.66 | 2021-02-01 | 101.74 | -7.2% |
| MTNL | 2020-12-28 | 14.10 | 2021-02-16 | 12.06 | -14.5% |
| MAHINDCIE | 2021-02-22 | 188.00 | 2021-03-19 | 158.46 | -15.7% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| NDGL | 2020-08-03 | 551.05 | 2021-04-12 | 682.63 | +23.9% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| ELGIRUBCO | 2021-02-01 | 30.75 | 2021-04-16 | 26.11 | -15.1% |
| NAHARCAP | 2021-03-22 | 111.80 | 2021-04-19 | 91.40 | -18.2% |
| MCL | 2021-04-19 | 91.20 | 2021-07-12 | 79.28 | -13.1% |
| CELEBRITY | 2020-11-17 | 5.50 | 2021-07-15 | 8.26 | +50.2% |
| WELINV | 2021-04-19 | 423.00 | 2021-07-29 | 424.65 | +0.4% |
| SWANENERGY | 2021-08-02 | 149.45 | 2021-08-04 | 131.29 | -12.2% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| ZODIACLOTH | 2021-07-19 | 134.50 | 2021-08-10 | 124.08 | -7.7% |
| SANDESH | 2021-07-19 | 932.00 | 2021-08-11 | 853.69 | -8.4% |
| MSPL | 2021-04-19 | 10.75 | 2021-08-24 | 9.04 | -15.9% |
| MAHESHWARI | 2021-08-09 | 130.00 | 2021-08-25 | 91.85 | -29.3% |
| GDL | 2021-01-25 | 158.00 | 2021-09-20 | 266.00 | +68.4% |
| GENUSPAPER | 2020-12-28 | 7.80 | 2021-10-21 | 10.97 | +40.6% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| HIRECT | 2021-08-30 | 92.55 | 2021-11-18 | 85.00 | -8.2% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-11-01 | 11,040.00 | 2021-11-26 | 10,070.05 | -8.8% |
| NDTV | 2021-09-27 | 91.50 | 2021-11-30 | 76.00 | -16.9% |
| 21STCENMGM | 2021-03-30 | 14.20 | 2021-12-03 | 54.10 | +281.0% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| MBLINFRA | 2021-12-06 | 33.00 | 2021-12-20 | 27.42 | -16.9% |
| UNIVPHOTO | 2021-12-06 | 687.00 | 2021-12-29 | 675.55 | -1.7% |
| JHS | 2021-08-16 | 28.60 | 2022-01-24 | 27.36 | -4.3% |
| TVTODAY | 2021-11-22 | 320.24 | 2022-01-24 | 311.68 | -2.7% |
| BIL | 2021-12-20 | 273.80 | 2022-01-24 | 284.42 | +3.9% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| ALPA | 2021-04-26 | 67.40 | 2022-02-14 | 77.08 | +14.4% |
| PIONEEREMB | 2022-01-03 | 64.55 | 2022-02-14 | 53.58 | -17.0% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| VISASTEEL | 2021-10-25 | 17.30 | 2022-02-22 | 13.72 | -20.7% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| PRESSMN | 2022-01-31 | 47.80 | 2022-03-22 | 41.85 | -12.4% |
| EMAMIREAL | 2021-12-27 | 96.80 | 2022-03-29 | 60.84 | -37.1% |
| KAMATHOTEL | 2022-03-28 | 71.45 | 2022-05-10 | 72.91 | +2.0% |
| DENORA | 2021-12-06 | 490.00 | 2022-06-07 | 647.13 | +32.1% |
| ADVANIHOTR | 2022-02-21 | 101.85 | 2022-06-09 | 64.65 | -36.5% |
| MRPL | 2022-06-13 | 116.65 | 2022-07-06 | 69.61 | -40.3% |
| DANGEE | 2022-03-28 | 303.00 | 2022-09-06 | 375.25 | +23.8% |
| TCPLPACK | 2022-02-21 | 748.70 | 2022-09-16 | 1,207.26 | +61.2% |
| DBCORP | 2022-09-19 | 138.00 | 2022-09-26 | 114.42 | -17.1% |
| PREMEXPLN | 2022-01-31 | 299.00 | 2022-09-27 | 426.50 | +42.6% |
| APOLSINHOT | 2022-10-03 | 1,249.00 | 2022-11-15 | 1,343.06 | +7.5% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| MRO-TEK | 2022-05-16 | 57.00 | 2022-12-22 | 56.49 | -0.9% |
| HUDCO | 2022-11-21 | 46.85 | 2022-12-23 | 46.08 | -1.6% |
| NECLIFE | 2022-12-26 | 28.40 | 2023-01-17 | 21.74 | -23.5% |
| ARVSMART | 2023-01-02 | 324.60 | 2023-01-25 | 285.00 | -12.2% |
| CREST | 2022-12-26 | 197.80 | 2023-01-27 | 176.79 | -10.6% |
| LSIL | 2023-01-30 | 23.20 | 2023-02-07 | 20.04 | -13.6% |
| DHUNINV | 2022-09-12 | 699.75 | 2023-02-13 | 628.21 | -10.2% |
| SANDESH | 2023-01-02 | 1,239.00 | 2023-02-14 | 864.40 | -30.2% |
| SPECIALITY | 2023-01-23 | 276.85 | 2023-02-14 | 221.73 | -19.9% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| SUNFLAG | 2023-01-30 | 130.00 | 2023-02-27 | 129.20 | -0.6% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| UNIENTER | 2023-02-13 | 179.30 | 2023-03-27 | 138.28 | -22.9% |
| LINC | 2023-02-20 | 550.00 | 2023-03-28 | 475.14 | -13.6% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| FOSECOIND | 2023-03-06 | 2,310.00 | 2023-03-31 | 2,222.91 | -3.8% |
| CLSEL | 2023-02-20 | 169.30 | 2023-05-29 | 176.89 | +4.5% |
| ANURAS | 2023-03-27 | 867.00 | 2023-07-03 | 1,007.67 | +16.2% |
| KSB | 2023-04-10 | 451.00 | 2023-07-12 | 407.74 | -9.6% |
| ANMOL | 2023-04-10 | 205.00 | 2023-07-18 | 218.88 | +6.8% |
| GANESHHOUC | 2023-07-24 | 457.00 | 2023-08-14 | 418.62 | -8.4% |
| KIRLOSIND | 2023-04-10 | 2,724.00 | 2023-09-25 | 3,202.97 | +17.6% |
| FORCEMOT | 2023-06-05 | 1,951.00 | 2023-10-20 | 3,709.99 | +90.2% |
| ALANKIT | 2023-07-10 | 10.20 | 2023-10-23 | 10.31 | +1.1% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| TEXMOPIPES | 2023-08-21 | 78.35 | 2023-11-20 | 68.88 | -12.1% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| PREMEXPLN | 2023-07-17 | 794.70 | 2024-01-24 | 1,420.25 | +78.7% |
| CONTROLPR | 2023-04-03 | 521.00 | 2024-02-06 | 884.21 | +69.7% |
| MUNJALAU | 2023-11-28 | 81.50 | 2024-02-09 | 96.33 | +18.2% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| BALAXI | 2024-02-12 | 126.00 | 2024-03-06 | 101.86 | -19.2% |
| SASKEN | 2023-10-09 | 1,320.00 | 2024-03-11 | 1,616.00 | +22.4% |
| GANDHITUBE | 2024-01-29 | 811.30 | 2024-03-11 | 726.75 | -10.4% |
| DHUNINV | 2023-10-23 | 1,020.00 | 2024-03-13 | 1,118.91 | +9.7% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| HERCULES | 2024-03-18 | 517.70 | 2024-04-15 | 500.03 | -3.4% |
| JUSTDIAL | 2024-04-22 | 1,084.00 | 2024-05-09 | 1,008.00 | -7.0% |
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| ASAL | 2024-02-12 | 652.00 | 2024-06-04 | 769.50 | +18.0% |
| SMSPHARMA | 2024-03-11 | 179.00 | 2024-06-04 | 181.36 | +1.3% |
| SOLARINDS | 2024-03-18 | 8,900.05 | 2024-06-04 | 7,980.95 | -10.3% |
| BOSCHLTD | 2024-03-18 | 29,500.05 | 2024-06-04 | 29,015.09 | -1.6% |
| GRPLTD | 2024-05-13 | 7,884.20 | 2024-06-04 | 8,103.50 | +2.8% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| MATRIMONY | 2024-06-10 | 643.50 | 2024-07-23 | 564.77 | -12.2% |
| BHAGCHEM | 2024-06-10 | 238.99 | 2024-08-05 | 333.45 | +39.5% |
| NAHARINDUS | 2024-07-29 | 157.45 | 2024-08-05 | 146.39 | -7.0% |
| AWHCL | 2024-07-29 | 890.05 | 2024-08-09 | 742.33 | -16.6% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| SPORTKING | 2024-07-22 | 1,100.00 | 2024-09-13 | 1,358.45 | +23.5% |
| DLINKINDIA | 2024-05-21 | 415.85 | 2024-10-04 | 589.05 | +41.6% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| ARROWGREEN | 2024-08-12 | 853.00 | 2024-10-07 | 723.58 | -15.2% |
| GHCLTEXTIL | 2024-08-12 | 109.60 | 2024-10-07 | 95.47 | -12.9% |
| HERANBA | 2024-08-19 | 467.00 | 2024-10-07 | 451.30 | -3.4% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| MAANALU | 2024-10-07 | 180.00 | 2024-11-05 | 193.14 | +7.3% |
| ABAN | 2023-10-23 | 58.30 | 2024-11-13 | 59.43 | +1.9% |
| SRHHYPOLTD | 2024-10-14 | 893.10 | 2024-11-13 | 647.47 | -27.5% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| PRSMJOHNSN | 2024-09-16 | 214.51 | 2024-12-26 | 170.55 | -20.5% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| VHL | 2024-11-18 | 5,080.00 | 2024-12-27 | 4,408.00 | -13.2% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| SASKEN | 2024-11-18 | 2,015.25 | 2025-01-21 | 1,993.24 | -1.1% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| SILINV | 2024-03-11 | 551.20 | 2025-01-27 | 548.20 | -0.5% |
| OSWALAGRO | 2024-08-12 | 60.80 | 2025-01-27 | 60.42 | -0.6% |
| NACLIND | 2024-12-30 | 67.60 | 2025-01-27 | 61.28 | -9.3% |
| ZOTA | 2025-01-20 | 1,016.45 | 2025-01-28 | 863.60 | -15.0% |
| SIYSIL | 2024-11-11 | 701.85 | 2025-01-30 | 770.45 | +9.8% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| BSE | 2024-10-14 | 4,536.00 | 2025-02-28 | 4,954.63 | +9.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| MBAPL | 2025-01-27 | 58.20 | 2025-03-27 | 53.39 | -8.3% |
| TAJGVK | 2025-02-24 | 440.40 | 2025-04-02 | 453.34 | +2.9% |
| APOLLO | 2025-02-03 | 126.50 | 2025-04-07 | 112.29 | -11.2% |
| TCPLPACK | 2025-02-24 | 3,997.25 | 2025-04-07 | 4,002.68 | +0.1% |
| AVANTIFEED | 2025-03-17 | 842.55 | 2025-04-07 | 648.95 | -23.0% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| GRMOVER | 2025-03-10 | 252.00 | 2025-05-07 | 290.80 | +15.4% |
| VADILALIND | 2025-04-07 | 4,820.55 | 2025-05-30 | 5,401.40 | +12.0% |
| SPORTKING | 2025-05-12 | 113.50 | 2025-06-02 | 107.55 | -5.2% |
| NDRAUTO | 2025-06-09 | 1,079.95 | 2025-07-28 | 976.51 | -9.6% |
| KPRMILL | 2025-05-12 | 1,302.00 | 2025-08-01 | 1,108.74 | -14.8% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| PUNJABCHEM | 2025-08-04 | 1,403.00 | 2025-08-18 | 1,208.88 | -13.8% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| SPMLINFRA | 2025-04-15 | 213.00 | 2025-09-26 | 252.27 | +18.4% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-26 | 857.85 | -0.8% |
| IPL | 2025-06-02 | 207.95 | 2025-10-14 | 197.80 | -4.9% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| GANDHITUBE | 2025-09-01 | 865.00 | 2025-10-16 | 871.15 | +0.7% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| PVSL | 2025-10-20 | 148.00 | 2025-11-11 | 132.82 | -10.3% |
| PRAKASH | 2025-08-11 | 178.70 | 2025-11-14 | 147.31 | -17.6% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| TVSELECT | 2025-09-29 | 627.00 | 2025-11-25 | 545.26 | -13.0% |
| RISHABH | 2025-08-25 | 424.25 | 2025-12-08 | 383.85 | -9.5% |
| PGIL | 2025-11-17 | 844.05 | 2025-12-09 | 765.71 | -9.3% |
| VLSFINANCE | 2025-12-01 | 311.80 | 2025-12-16 | 276.07 | -11.5% |
| NACLIND | 2025-04-07 | 128.14 | 2025-12-17 | 164.20 | +28.1% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| ESABINDIA | 2025-12-15 | 6,203.50 | 2026-01-12 | 5,605.00 | -9.6% |
| ASIANTILES | 2025-12-22 | 72.69 | 2026-01-12 | 70.21 | -3.4% |
| KICL | 2025-10-27 | 6,006.00 | 2026-01-19 | 4,607.98 | -23.3% |
| BHAGERIA | 2025-10-27 | 237.00 | 2026-01-20 | 160.92 | -32.1% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| NATIONALUM | 2026-02-02 | 347.10 | 2026-02-17 | 335.49 | -3.3% |
| NITCO | 2026-01-19 | 89.00 | 2026-02-19 | 75.12 | -15.6% |
| INFOBEAN | 2025-12-15 | 696.70 | 2026-02-27 | 770.07 | +10.5% |
| APEX | 2025-12-22 | 288.50 | 2026-02-27 | 389.22 | +34.9% |
| KIRIINDUS | 2026-01-19 | 530.30 | 2026-03-02 | 427.56 | -19.4% |
| HINDCOPPER | 2026-02-02 | 590.15 | 2026-03-12 | 528.63 | -10.4% |
| AYMSYNTEX | 2026-03-02 | 197.99 | 2026-03-12 | 174.33 | -12.0% |
| AUTOAXLES | 2026-02-09 | 1,950.00 | 2026-03-13 | 1,776.59 | -8.9% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-02 | 116.20 | 2026-03-23 | 110.67 | -4.8% |
| AGIIL | 2026-01-12 | 295.60 | 2026-03-30 | 271.80 | -8.1% |
| KSB | 2026-03-02 | 738.00 | 2026-05-04 | 917.42 | +24.3% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| BAJAJHIND | 2026-03-30 | 16.42 | 2026-05-14 | 17.96 | +9.4% |
| E2E | 2026-02-23 | 2,914.00 | 2026-06-05 | 2,330.72 | -20.0% |
| EXPLEOSOL | 2026-05-18 | 903.95 | 2026-06-10 | 799.25 | -11.6% |
| CIEINDIA | 2025-10-20 | 432.50 | 2026-06-11 | 429.88 | -0.6% |
| SEAMECLTD | 2026-04-06 | 1,525.00 | 2026-06-17 | 1,398.40 | -8.3% |
| SOTL | 2026-06-08 | 545.00 | 2026-06-29 | 509.53 | -6.5% |
| SASKEN | 2026-05-18 | 1,680.10 | 2026-07-08 | 1,933.72 | +15.1% |
| SPAL | 2026-06-22 | 1,030.00 | 2026-07-16 | 1,027.62 | -0.2% |
| RAMCOSYS | 2026-07-06 | 815.50 | 2026-07-24 | 722.48 | -11.4% |
| JUSTDIAL | 2026-07-20 | 766.00 | 2026-08-18 | 658.64 | -14.0% |
| ABB | 2026-03-16 | 6,400.00 | 2026-09-15 | 7,158.25 | +11.8% |
| MUNJALAU | 2026-07-13 | 100.50 | 2026-09-15 | 104.60 | +4.1% |
| PANAMAPET | 2026-06-15 | 384.80 | 2026-09-16 | 440.87 | +14.6% |
| CLSEL | 2026-06-15 | 297.00 | 2026-09-16 | 274.60 | -7.5% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_MCAP1250_OLDRULES.csv` beside this report (43259 events in all).*

```
2020-04-13  DEEPAKNTR   BUY ₹10.00 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.81× weekly, month 2.50×, ladder rising; stop ₹241.64; charges ₹0.0118)
2020-04-27  CADILAHC    BUY ₹10.01 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 5.13×, ladder rising; stop ₹310.03; charges ₹0.0119)
2020-04-27  SYNGENE     BUY ₹10.02 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.37× weekly, month 1.94×, ladder rising; stop ₹285.95; charges ₹0.0119)
2020-04-27  TAJGVK      BUY ₹10.01 at ₹133.40 (fresh Friday signal — BUY: 6.67× weekly, month 2.22×, ladder rising; stop ₹106.49; charges ₹0.0119)
2020-05-11  APLLTD      BUY ₹9.97 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.72× weekly, month 6.13×, ladder rising; stop ₹694.45; charges ₹0.0118)
2020-05-11  IOLCP       BUY ₹9.98 at ₹66.18 (fresh Friday signal — BUY: 2.24× weekly, month 2.69×, ladder rising; stop ₹51.22; charges ₹0.0118)
2020-05-11  MANGCHEFER  BUY ₹9.98 at ₹33.75 (fresh Friday signal — BUY: 2.58× weekly, month 2.92×, ladder rising; stop ₹29.50; charges ₹0.0118)
2020-05-18  APOLLO      BUY ₹9.41 at ₹8.70 (fresh Friday signal — BUY: 6.27× weekly, month 5.31×, ladder rising; stop ₹6.07; charges ₹0.0111)
2020-05-18  HATHWAY     BUY ₹10.42 at ₹24.50 (fresh Friday signal — BUY: 8.42× weekly, month 4.72×, ladder rising; stop ₹15.52; charges ₹0.0123)
2020-05-18  VINYLINDIA  BUY ₹10.20 at ₹62.55 (fresh Friday signal — ACCUMULATE: 13.29× weekly, month 10.04×, ladder rising; stop ₹52.87; charges ₹0.0121)
2020-06-12  DEEPAKNTR   SELL ₹9.97 at stop ₹474.05 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-06-15  PANACEABIO  BUY ₹9.97 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.25×, ladder rising; stop ₹114.11; charges ₹0.0118)
2020-06-16  IOLCP       SELL ₹10.43 at stop ₹69.35 (+4.8%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2020-06-22  ORIENTBELL  BUY ₹10.43 at ₹106.75 (fresh Friday signal — BUY: 12.61× weekly, month 7.71×, ladder rising; stop ₹63.46; charges ₹0.0124)
2020-07-20  ORIENTBELL  SELL ₹7.05 at stop ₹72.28 (-32.3%, charges ₹0.0073) — the cash goes back to work at the next Friday screen
2020-07-27  ASAHISONG   BUY ₹7.05 at ₹207.35 (fresh Friday signal — BUY: 10.62× weekly, month 8.14×, ladder rising; stop ₹134.78; charges ₹0.0083)
2020-07-27  VINYLINDIA  SELL ₹13.76 at stop ₹84.55 (+35.2%, charges ₹0.0143) — the cash goes back to work at the next Friday screen
2020-07-31  MANGCHEFER  SELL ₹9.95 at stop ₹33.73 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-08-03  DYNPRO      BUY ₹11.04 at ₹200.00 (fresh Friday signal — BUY: 6.69× weekly, month 11.29×, ladder rising; stop ₹156.56; charges ₹0.0131)
2020-08-03  NDGL        BUY ₹12.67 at ₹551.05 (fresh Friday signal — BUY: 32.96× weekly, month 9.69×, ladder rising; stop ₹408.60; charges ₹0.0150)
2020-08-20  PANACEABIO  SELL ₹7.96 at stop ₹184.01 (-20.0%, charges ₹0.0083) — the cash goes back to work at the next Friday screen
2020-08-24  SASTASUNDR  BUY ₹7.96 at ₹107.00 (fresh Friday signal — ACCUMULATE: 11.14× weekly, month 4.01×, ladder rising; stop ₹75.74; charges ₹0.0094)
2020-08-31  DYNPRO      SELL ₹10.28 at stop ₹186.68 (-6.7%, charges ₹0.0107) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.93 at stop ₹928.62 (+19.9%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-01  ASAHISONG   SELL ₹6.34 at stop ₹186.89 (-9.9%, charges ₹0.0066) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹12.18 at ₹1,398.95 (fresh Friday signal — BUY: 5.23× weekly, month 3.88×, ladder rising; stop ₹1,211.25; charges ₹0.0144)
2020-09-07  TIPSINDLTD  BUY ₹12.12 at ₹23.19 (fresh Friday signal — BUY: 6.28× weekly, month 4.00×, ladder rising; stop ₹16.01; charges ₹0.0144)
2020-09-08  CADILAHC    SELL ₹11.04 at stop ₹364.99 (+10.5%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-14  TCI         BUY ₹12.71 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.71× weekly, month 3.76×, ladder rising; stop ₹190.07; charges ₹0.0151)
2020-09-22  TAJGVK      SELL ₹9.47 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-22  TIPSINDLTD  SELL ₹11.52 at stop ₹22.08 (-4.8%, charges ₹0.0119) — the cash goes back to work at the next Friday screen
2020-09-28  SAKSOFT     BUY ₹12.15 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.34×, ladder rising; stop ₹303.81; charges ₹0.0144)
2020-09-28  VIDHIING    BUY ₹11.40 at ₹111.70 (fresh Friday signal — BUY: 4.70× weekly, month 4.47×, ladder rising; stop ₹77.90; charges ₹0.0135)
2020-10-28  SASTASUNDR  SELL ₹6.17 at stop ₹83.12 (-22.3%, charges ₹0.0064) — the cash goes back to work at the next Friday screen
2020-11-02  TEXMOPIPES  BUY ₹6.17 at ₹16.30 (fresh Friday signal — ACCUMULATE: 4.01× weekly, month 2.60×, ladder rising; stop ₹12.54; charges ₹0.0073)
2020-11-09  HATHWAY     SELL ₹12.02 at stop ₹28.34 (+15.7%, charges ₹0.0125) — the cash goes back to work at the next Friday screen
2020-11-17  CELEBRITY   BUY ₹11.06 at ₹5.50 (fresh Friday signal — BUY: 7.12× weekly, month 2.95×, ladder rising; stop ₹4.16; charges ₹0.0131)
2020-12-02  VIDHIING    SELL ₹11.76 at stop ₹115.50 (+3.4%, charges ₹0.0122) — the cash goes back to work at the next Friday screen
2020-12-07  MANGCHEFER  BUY ₹11.62 at ₹40.75 (fresh Friday signal — BUY: 11.07× weekly, month 3.88×, ladder rising; stop ₹30.21; charges ₹0.0138)
2020-12-21  APOLLO      SELL ₹12.82 at stop ₹11.88 (+36.6%, charges ₹0.0133) — the cash goes back to work at the next Friday screen
2020-12-21  TEXMOPIPES  SELL ₹7.11 at stop ₹18.83 (+15.5%, charges ₹0.0074) — the cash goes back to work at the next Friday screen
2020-12-22  MANGCHEFER  SELL ₹10.80 at stop ₹37.95 (-6.9%, charges ₹0.0112) — the cash goes back to work at the next Friday screen
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹12.30 at stop ₹234.75 (-3.0%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2020-12-28  GENUSPAPER  BUY ₹11.20 at ₹7.80 (fresh Friday signal — BUY: 10.44× weekly, month 6.76×, ladder rising; stop ₹4.89; charges ₹0.0133)
2020-12-28  ITDC        BUY ₹11.17 at ₹338.55 (fresh Friday signal — BUY: 10.24× weekly, month 3.95×, ladder rising; stop ₹247.29; charges ₹0.0132)
2020-12-28  MTNL        BUY ₹11.15 at ₹14.10 (fresh Friday signal — BUY: 9.99× weekly, month 4.75×, ladder rising; stop ₹8.26; charges ₹0.0132)
2020-12-28  PAISALO     BUY ₹11.15 at ₹56.99 (fresh Friday signal — BUY: 32.49× weekly, month 7.40×, ladder rising; stop ₹33.56; charges ₹0.0132)
2020-12-28  TERASOFT    BUY ₹11.25 at ₹51.25 (fresh Friday signal — BUY: 13.80× weekly, month 7.51×, ladder rising; stop ₹25.77; charges ₹0.0133)
2020-12-28  VESUVIUS    BUY ₹5.84 at ₹109.66 (fresh Friday signal — BUY: 7.96× weekly, month 3.72×, ladder rising; stop ₹95.92; charges ₹0.0069)
2021-01-18  ITDC        SELL ₹10.02 at stop ₹304.38 (-10.1%, charges ₹0.0104) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹10.02 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.80×, ladder rising; stop ₹92.41; charges ₹0.0119)
2021-01-25  SAKSOFT     SELL ₹10.37 at stop ₹341.10 (-14.4%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2021-01-27  TERASOFT    SELL ₹9.71 at stop ₹44.32 (-13.5%, charges ₹0.0101) — the cash goes back to work at the next Friday screen
2021-02-01  ELGIRUBCO   BUY ₹11.23 at ₹30.75 (fresh Friday signal — BUY: 7.89× weekly, month 8.56×, ladder rising; stop ₹18.27; charges ₹0.0133)
2021-02-01  HARITASEAT  BUY ₹8.85 at ₹532.00 (fresh Friday signal — BUY: 5.70× weekly, month 8.57×, ladder rising; stop ₹438.90; charges ₹0.0105)
2021-02-01  VESUVIUS    SELL ₹5.40 at stop ₹101.74 (-7.2%, charges ₹0.0056) — the cash goes back to work at the next Friday screen
2021-02-16  MTNL        SELL ₹9.51 at stop ₹12.06 (-14.5%, charges ₹0.0099) — the cash goes back to work at the next Friday screen
2021-02-22  MAHINDCIE   BUY ₹11.75 at ₹188.00 (fresh Friday signal — BUY: 22.74× weekly, month 4.25×, ladder rising; stop ₹143.79; charges ₹0.0139)
2021-03-19  MAHINDCIE   SELL ₹9.88 at stop ₹158.46 (-15.7%, charges ₹0.0102) — the cash goes back to work at the next Friday screen
2021-03-22  NAHARCAP    BUY ₹11.83 at ₹111.80 (fresh Friday signal — BUY: 8.15× weekly, month 7.42×, ladder rising; stop ₹86.78; charges ₹0.0140)
2021-03-25  BANARISUG   SELL ₹13.79 at stop ₹1,586.36 (+13.4%, charges ₹0.0143) — the cash goes back to work at the next Friday screen
2021-03-30  21STCENMGM  BUY ₹11.58 at ₹14.20 (fresh Friday signal — BUY: 6.71× weekly, month 2.46×, ladder rising; stop ₹11.02; charges ₹0.0137)
2021-04-01  TAX         FY2021 settled: ₹0.7285 paid (STCG ₹3.64 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-12  NDGL        SELL ₹15.67 at stop ₹682.63 (+23.9%, charges ₹0.0162) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹14.14 at stop ₹72.41 (+27.1%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2021-04-16  ELGIRUBCO   SELL ₹9.51 at stop ₹26.11 (-15.1%, charges ₹0.0099) — the cash goes back to work at the next Friday screen
2021-04-19  MCL         BUY ₹10.88 at ₹91.20 (fresh Friday signal — ACCUMULATE: 5.03× weekly, month 3.15×, ladder rising; stop ₹78.30; charges ₹0.0129)
2021-04-19  MOREPENLAB  BUY ₹9.48 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.06×, ladder rising; stop ₹28.01; charges ₹0.0112)
2021-04-19  MSPL        BUY ₹10.79 at ₹10.75 (fresh Friday signal — BUY: 2.56× weekly, month 2.27×, ladder rising; stop ₹5.85; charges ₹0.0128)
2021-04-19  NAHARCAP    SELL ₹9.65 at stop ₹91.40 (-18.2%, charges ₹0.0100) — the cash goes back to work at the next Friday screen
2021-04-19  WELINV      BUY ₹10.86 at ₹423.00 (fresh Friday signal — ACCUMULATE: 2.91× weekly, month 2.30×, ladder rising; stop ₹332.58; charges ₹0.0129)
2021-04-26  ALPA        BUY ₹9.65 at ₹67.40 (fresh Friday signal — BUY: 9.87× weekly, month 4.10×, ladder rising; stop ₹39.03; charges ₹0.0114)
2021-07-12  MCL         SELL ₹9.44 at stop ₹79.28 (-13.1%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2021-07-15  CELEBRITY   SELL ₹16.58 at stop ₹8.26 (+50.2%, charges ₹0.0172) — the cash goes back to work at the next Friday screen
2021-07-19  SANDESH     BUY ₹14.36 at ₹932.00 (fresh Friday signal — BUY: 16.72× weekly, month 5.11×, ladder rising; stop ₹726.85; charges ₹0.0170)
2021-07-19  ZODIACLOTH  BUY ₹11.65 at ₹134.50 (fresh Friday signal — BUY: 12.64× weekly, month 6.30×, ladder rising; stop ₹100.89; charges ₹0.0138)
2021-07-29  WELINV      SELL ₹10.88 at stop ₹424.65 (+0.4%, charges ₹0.0113) — the cash goes back to work at the next Friday screen
2021-08-02  SWANENERGY  BUY ₹10.88 at ₹149.45 (fresh Friday signal — BUY: 17.17× weekly, month 4.67×, ladder rising; stop ₹131.29; charges ₹0.0129)
2021-08-04  SWANENERGY  SELL ₹9.54 at stop ₹131.29 (-12.2%, charges ₹0.0099) — the cash goes back to work at the next Friday screen
2021-08-09  MAHESHWARI  BUY ₹9.54 at ₹130.00 (fresh Friday signal — BUY: 13.73× weekly, month 2.95×, ladder rising; stop ₹91.85; charges ₹0.0113)
2021-08-10  MOREPENLAB  SELL ₹14.23 at stop ₹56.33 (+50.4%, charges ₹0.0148) — the cash goes back to work at the next Friday screen
2021-08-10  ZODIACLOTH  SELL ₹10.73 at stop ₹124.08 (-7.7%, charges ₹0.0111) — the cash goes back to work at the next Friday screen
2021-08-11  SANDESH     SELL ₹13.12 at stop ₹853.69 (-8.4%, charges ₹0.0136) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹13.83 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.42×, ladder rising; stop ₹2,675.86; charges ₹0.0164)
2021-08-16  JHS         BUY ₹13.82 at ₹28.60 (fresh Friday signal — ACCUMULATE: 8.70× weekly, month 5.66×, ladder rising; stop ₹13.88; charges ₹0.0164)
2021-08-16  TATAINVEST  BUY ₹10.43 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0124)
2021-08-24  MSPL        SELL ₹9.05 at stop ₹9.04 (-15.9%, charges ₹0.0094) — the cash goes back to work at the next Friday screen
2021-08-25  MAHESHWARI  SELL ₹6.72 at stop ₹91.85 (-29.3%, charges ₹0.0070) — the cash goes back to work at the next Friday screen
2021-08-30  HIRECT      BUY ₹13.59 at ₹92.55 (fresh Friday signal — BUY: 8.36× weekly, month 3.07×, ladder rising; stop ₹68.64; charges ₹0.0161)
2021-09-20  GDL         SELL ₹16.83 at stop ₹266.00 (+68.4%, charges ₹0.0175) — the cash goes back to work at the next Friday screen
2021-09-27  NDTV        BUY ₹14.28 at ₹91.50 (fresh Friday signal — BUY: 4.89× weekly, month 1.89×, ladder rising; stop ₹60.48; charges ₹0.0169)
2021-10-21  GENUSPAPER  SELL ₹15.72 at stop ₹10.97 (+40.6%, charges ₹0.0163) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹12.08 at stop ₹3,220.59 (-12.5%, charges ₹0.0125) — the cash goes back to work at the next Friday screen
2021-10-25  VISASTEEL   BUY ₹14.16 at ₹17.30 (fresh Friday signal — BUY: 6.99× weekly, month 4.93×, ladder rising; stop ₹11.97; charges ₹0.0168)
2021-11-01  TTKPRESTIG  BUY ₹14.74 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.0175)
2021-11-18  HIRECT      SELL ₹12.46 at stop ₹85.00 (-8.2%, charges ₹0.0129) — the cash goes back to work at the next Friday screen
2021-11-22  TVTODAY     BUY ₹14.88 at ₹320.24 (fresh Friday signal — BUY: 15.58× weekly, month 3.55×, ladder rising; stop ₹253.08; charges ₹0.0176)
2021-11-26  TATAINVEST  SELL ₹11.43 at stop ₹1,436.49 (+9.8%, charges ₹0.0119) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹13.42 at stop ₹10,070.05 (-8.8%, charges ₹0.0139) — the cash goes back to work at the next Friday screen
2021-11-29  RAYMOND     BUY ₹11.59 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0137)
2021-11-29  RSYSTEMS    BUY ₹14.46 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0171)
2021-11-30  NDTV        SELL ₹11.83 at stop ₹76.00 (-16.9%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2021-12-03  21STCENMGM  SELL ₹44.01 at stop ₹54.10 (+281.0%, charges ₹0.0456) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹12.93 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0153)
2021-12-06  DENORA      BUY ₹14.34 at ₹490.00 (fresh Friday signal — BUY: 12.65× weekly, month 2.85×, ladder rising; stop ₹330.38; charges ₹0.0170)
2021-12-06  MBLINFRA    BUY ₹14.28 at ₹33.00 (fresh Friday signal — BUY: 15.92× weekly, month 4.06×, ladder rising; stop ₹17.32; charges ₹0.0169)
2021-12-06  UNIVPHOTO   BUY ₹14.29 at ₹687.00 (fresh Friday signal — BUY: 6.38× weekly, month 2.65×, ladder rising; stop ₹378.29; charges ₹0.0169)
2021-12-16  RSYSTEMS    SELL ₹12.93 at stop ₹291.18 (-10.4%, charges ₹0.0134) — the cash goes back to work at the next Friday screen
2021-12-20  BIL         BUY ₹12.93 at ₹273.80 (fresh Friday signal — BUY: 30.84× weekly, month 7.22×, ladder rising; stop ₹167.10; charges ₹0.0153)
2021-12-20  MBLINFRA    SELL ₹11.84 at stop ₹27.42 (-16.9%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2021-12-27  EMAMIREAL   BUY ₹11.84 at ₹96.80 (fresh Friday signal — BUY: 7.16× weekly, month 2.84×, ladder rising; stop ₹60.84; charges ₹0.0140)
2021-12-29  UNIVPHOTO   SELL ₹14.02 at stop ₹675.55 (-1.7%, charges ₹0.0145) — the cash goes back to work at the next Friday screen
2022-01-03  PIONEEREMB  BUY ₹14.02 at ₹64.55 (fresh Friday signal — BUY: 4.66× weekly, month 1.62×, ladder rising; stop ₹53.58; charges ₹0.0166)
2022-01-24  BIL         SELL ₹13.40 at stop ₹284.42 (+3.9%, charges ₹0.0139) — the cash goes back to work at the next Friday screen
2022-01-24  JHS         SELL ₹13.19 at stop ₹27.36 (-4.3%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2022-01-24  TVTODAY     SELL ₹14.45 at stop ₹311.68 (-2.7%, charges ₹0.0150) — the cash goes back to work at the next Friday screen
2022-01-31  PREMEXPLN   BUY ₹11.84 at ₹299.00 (fresh Friday signal — BUY: 4.43× weekly, month 1.92×, ladder rising; stop ₹223.25; charges ₹0.0140)
2022-01-31  PRESSMN     BUY ₹14.60 at ₹47.80 (fresh Friday signal — BUY: 13.67× weekly, month 5.92×, ladder rising; stop ₹30.59; charges ₹0.0173)
2022-01-31  SHARDACROP  BUY ₹14.61 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0173)
2022-02-11  SHARDACROP  SELL ₹13.55 at stop ₹545.30 (-7.1%, charges ₹0.0141) — the cash goes back to work at the next Friday screen
2022-02-14  ALPA        SELL ₹11.01 at stop ₹77.08 (+14.4%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹13.55 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0161)
2022-02-14  PIONEEREMB  SELL ₹11.61 at stop ₹53.58 (-17.0%, charges ₹0.0120) — the cash goes back to work at the next Friday screen
2022-02-15  RAYMOND     SELL ₹13.18 at stop ₹679.35 (+14.0%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2022-02-21  ADVANIHOTR  BUY ₹13.63 at ₹101.85 (fresh Friday signal — ACCUMULATE: 8.91× weekly, month 7.66×, ladder rising; stop ₹64.65; charges ₹0.0162)
2022-02-21  CGCL        BUY ₹8.65 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0102)
2022-02-21  TCPLPACK    BUY ₹13.53 at ₹748.70 (fresh Friday signal — BUY: 6.12× weekly, month 3.47×, ladder rising; stop ₹480.00; charges ₹0.0160)
2022-02-22  VISASTEEL   SELL ₹11.21 at stop ₹13.72 (-20.7%, charges ₹0.0116) — the cash goes back to work at the next Friday screen
2022-02-28  SHANTIGEAR  BUY ₹11.21 at ₹185.30 (fresh Friday signal — BUY: 2.90× weekly, month 1.90×, ladder rising; stop ₹170.29; charges ₹0.0133)
2022-03-21  BSE         SELL ₹11.15 at stop ₹1,634.39 (-13.5%, charges ₹0.0116) — the cash goes back to work at the next Friday screen
2022-03-22  PRESSMN     SELL ₹12.75 at stop ₹41.85 (-12.4%, charges ₹0.0132) — the cash goes back to work at the next Friday screen
2022-03-28  DANGEE      BUY ₹14.24 at ₹303.00 (fresh Friday signal — BUY: 5.95× weekly, month 4.75×, ladder rising; stop ₹237.50; charges ₹0.0169)
2022-03-28  KAMATHOTEL  BUY ₹9.67 at ₹71.45 (fresh Friday signal — BUY: 3.56× weekly, month 2.29×, ladder rising; stop ₹44.72; charges ₹0.0115)
2022-03-29  EMAMIREAL   SELL ₹7.42 at stop ₹60.84 (-37.1%, charges ₹0.0077) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹5.1250 paid (STCG ₹25.63 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-05-10  KAMATHOTEL  SELL ₹9.84 at stop ₹72.91 (+2.0%, charges ₹0.0102) — the cash goes back to work at the next Friday screen
2022-05-16  MRO-TEK     BUY ₹12.14 at ₹57.00 (fresh Friday signal — ACCUMULATE: 2.51× weekly, month 5.06×, ladder rising; stop ₹49.34; charges ₹0.0144)
2022-06-07  DENORA      SELL ₹18.90 at stop ₹647.13 (+32.1%, charges ₹0.0196) — the cash goes back to work at the next Friday screen
2022-06-09  ADVANIHOTR  SELL ₹8.63 at stop ₹64.65 (-36.5%, charges ₹0.0090) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹15.52 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0184)
2022-06-13  MRPL        BUY ₹12.02 at ₹116.65 (fresh Friday signal — BUY: 3.64× weekly, month 4.35×, ladder rising; stop ₹69.61; charges ₹0.0142)
2022-07-06  MRPL        SELL ₹7.16 at stop ₹69.61 (-40.3%, charges ₹0.0074) — the cash goes back to work at the next Friday screen
2022-09-06  DANGEE      SELL ₹17.59 at stop ₹375.25 (+23.8%, charges ₹0.0182) — the cash goes back to work at the next Friday screen
2022-09-12  DHUNINV     BUY ₹18.37 at ₹699.75 (fresh Friday signal — BUY: 21.10× weekly, month 1.76×, ladder rising; stop ₹558.65; charges ₹0.0218)
2022-09-16  TCPLPACK    SELL ₹21.77 at stop ₹1,207.26 (+61.2%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2022-09-19  DBCORP      BUY ₹9.98 at ₹138.00 (fresh Friday signal — BUY: 15.57× weekly, month 10.93×, ladder rising; stop ₹94.19; charges ₹0.0118)
2022-09-19  JSWHL       BUY ₹18.16 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0215)
2022-09-26  DBCORP      SELL ₹8.26 at stop ₹114.42 (-17.1%, charges ₹0.0086) — the cash goes back to work at the next Friday screen
2022-09-27  PREMEXPLN   SELL ₹16.85 at stop ₹426.50 (+42.6%, charges ₹0.0175) — the cash goes back to work at the next Friday screen
2022-10-03  APOLSINHOT  BUY ₹17.27 at ₹1,249.00 (fresh Friday signal — BUY: 13.10× weekly, month 3.98×, ladder rising; stop ₹794.34; charges ₹0.0205)
2022-11-15  APOLSINHOT  SELL ₹18.53 at stop ₹1,343.06 (+7.5%, charges ₹0.0192) — the cash goes back to work at the next Friday screen
2022-11-21  HUDCO       BUY ₹18.51 at ₹46.85 (fresh Friday signal — BUY: 18.83× weekly, month 8.20×, ladder rising; stop ₹38.05; charges ₹0.0219)
2022-12-21  ELECON      SELL ₹25.60 at stop ₹202.49 (+65.3%, charges ₹0.0266) — the cash goes back to work at the next Friday screen
2022-12-22  MRO-TEK     SELL ₹12.01 at stop ₹56.49 (-0.9%, charges ₹0.0125) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹20.85 at stop ₹345.56 (+86.5%, charges ₹0.0216) — the cash goes back to work at the next Friday screen
2022-12-23  HUDCO       SELL ₹18.16 at stop ₹46.08 (-1.6%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2022-12-26  CREST       BUY ₹17.51 at ₹197.80 (fresh Friday signal — BUY: 6.59× weekly, month 1.51×, ladder rising; stop ₹172.47; charges ₹0.0208)
2022-12-26  KRISHANA    BUY ₹17.49 at ₹83.60 (fresh Friday signal — BUY: 3.61× weekly, month 2.28×, ladder rising; stop ₹75.36; charges ₹0.0207)
2022-12-26  NECLIFE     BUY ₹17.70 at ₹28.40 (fresh Friday signal — BUY: 14.66× weekly, month 2.32×, ladder rising; stop ₹20.28; charges ₹0.0210)
2023-01-02  ARVSMART    BUY ₹14.13 at ₹324.60 (fresh Friday signal — BUY: 9.51× weekly, month 2.74×, ladder rising; stop ₹233.27; charges ₹0.0167)
2023-01-02  SANDESH     BUY ₹17.65 at ₹1,239.00 (fresh Friday signal — BUY: 62.35× weekly, month 13.57×, ladder rising; stop ₹710.60; charges ₹0.0209)
2023-01-17  NECLIFE     SELL ₹13.52 at stop ₹21.74 (-23.5%, charges ₹0.0140) — the cash goes back to work at the next Friday screen
2023-01-23  SPECIALITY  BUY ₹13.52 at ₹276.85 (fresh Friday signal — BUY: 6.65× weekly, month 2.62×, ladder rising; stop ₹221.73; charges ₹0.0160)
2023-01-25  ARVSMART    SELL ₹12.38 at stop ₹285.00 (-12.2%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2023-01-27  CREST       SELL ₹15.62 at stop ₹176.79 (-10.6%, charges ₹0.0162) — the cash goes back to work at the next Friday screen
2023-01-30  LSIL        BUY ₹16.44 at ₹23.20 (fresh Friday signal — BUY: 2.27× weekly, month 3.60×, ladder rising; stop ₹11.29; charges ₹0.0195)
2023-01-30  SUNFLAG     BUY ₹11.56 at ₹130.00 (fresh Friday signal — BUY: 2.22× weekly, month 3.13×, ladder rising; stop ₹105.97; charges ₹0.0137)
2023-02-07  LSIL        SELL ₹14.17 at stop ₹20.04 (-13.6%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2023-02-13  DHUNINV     SELL ₹16.45 at stop ₹628.21 (-10.2%, charges ₹0.0171) — the cash goes back to work at the next Friday screen
2023-02-13  UNIENTER    BUY ₹14.17 at ₹179.30 (fresh Friday signal — BUY: 19.11× weekly, month 5.40×, ladder rising; stop ₹119.20; charges ₹0.0168)
2023-02-14  SANDESH     SELL ₹12.29 at stop ₹864.40 (-30.2%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2023-02-14  SPECIALITY  SELL ₹10.80 at stop ₹221.73 (-19.9%, charges ₹0.0112) — the cash goes back to work at the next Friday screen
2023-02-17  CGCL        SELL ₹10.15 at stop ₹704.95 (+17.6%, charges ₹0.0105) — the cash goes back to work at the next Friday screen
2023-02-20  CLSEL       BUY ₹15.59 at ₹169.30 (fresh Friday signal — BUY: 4.02× weekly, month 3.47×, ladder rising; stop ₹135.94; charges ₹0.0185)
2023-02-20  LINC        BUY ₹15.58 at ₹550.00 (fresh Friday signal — BUY: 2.23× weekly, month 3.07×, ladder rising; stop ₹452.72; charges ₹0.0185)
2023-02-20  TIIL        BUY ₹15.68 at ₹1,116.70 (fresh Friday signal — BUY: 8.50× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0186)
2023-02-27  SUNFLAG     SELL ₹11.46 at stop ₹129.20 (-0.6%, charges ₹0.0119) — the cash goes back to work at the next Friday screen
2023-03-06  FOSECOIND   BUY ₹14.30 at ₹2,310.00 (fresh Friday signal — BUY: 13.30× weekly, month 1.88×, ladder rising; stop ₹1,867.03; charges ₹0.0169)
2023-03-20  KRISHANA    SELL ₹19.70 at stop ₹94.40 (+12.9%, charges ₹0.0204) — the cash goes back to work at the next Friday screen
2023-03-27  ANURAS      BUY ₹14.95 at ₹867.00 (fresh Friday signal — BUY: 7.51× weekly, month 4.47×, ladder rising; stop ₹691.46; charges ₹0.0177)
2023-03-27  UNIENTER    SELL ₹10.90 at stop ₹138.28 (-22.9%, charges ₹0.0113) — the cash goes back to work at the next Friday screen
2023-03-28  LINC        SELL ₹13.43 at stop ₹475.14 (-13.6%, charges ₹0.0139) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹29.21 at stop ₹112.36 (+116.1%, charges ₹0.0303) — the cash goes back to work at the next Friday screen
2023-03-31  FOSECOIND   SELL ₹13.73 at stop ₹2,222.91 (-3.8%, charges ₹0.0142) — the cash goes back to work at the next Friday screen
2023-04-03  CONTROLPR   BUY ₹14.52 at ₹521.00 (fresh Friday signal — ACCUMULATE: 2.94× weekly, month 2.01×, ladder rising; stop ₹439.28; charges ₹0.0172)
2023-04-03  HAL         BUY ₹14.51 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.04×, ladder rising; stop ₹1,171.71; charges ₹0.0172)
2023-04-03  TAX         FY2023 settled: ₹3.6897 paid (STCG ₹8.63 @20%, LTCG ₹15.71 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-10  ANMOL       BUY ₹14.76 at ₹205.00 (fresh Friday signal — BUY: 4.03× weekly, month 3.15×, ladder rising; stop ₹163.45; charges ₹0.0175)
2023-04-10  KIRLOSIND   BUY ₹14.76 at ₹2,724.00 (fresh Friday signal — BUY: 2.29× weekly, month 2.40×, ladder rising; stop ₹2,256.25; charges ₹0.0175)
2023-04-10  KSB         BUY ₹9.79 at ₹451.00 (fresh Friday signal — BUY: 2.21× weekly, month 2.24×, ladder rising; stop ₹372.21; charges ₹0.0116)
2023-05-29  CLSEL       SELL ₹16.25 at stop ₹176.89 (+4.5%, charges ₹0.0169) — the cash goes back to work at the next Friday screen
2023-06-05  FORCEMOT    BUY ₹16.25 at ₹1,951.00 (fresh Friday signal — BUY: 23.21× weekly, month 3.12×, ladder rising; stop ₹1,289.01; charges ₹0.0193)
2023-07-03  ANURAS      SELL ₹17.34 at stop ₹1,007.67 (+16.2%, charges ₹0.0180) — the cash goes back to work at the next Friday screen
2023-07-10  ALANKIT     BUY ₹17.30 at ₹10.20 (fresh Friday signal — BUY: 17.11× weekly, month 4.17×, ladder rising; stop ₹6.52; charges ₹0.0205)
2023-07-12  KSB         SELL ₹8.83 at stop ₹407.74 (-9.6%, charges ₹0.0092) — the cash goes back to work at the next Friday screen
2023-07-17  PREMEXPLN   BUY ₹8.87 at ₹794.70 (fresh Friday signal — BUY: 33.13× weekly, month 10.49×, ladder rising; stop ₹376.43; charges ₹0.0105)
2023-07-18  ANMOL       SELL ₹15.72 at stop ₹218.88 (+6.8%, charges ₹0.0163) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹15.72 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.91×, ladder rising; stop ₹359.10; charges ₹0.0186)
2023-08-14  GANESHHOUC  SELL ₹14.37 at stop ₹418.62 (-8.4%, charges ₹0.0149) — the cash goes back to work at the next Friday screen
2023-08-21  TEXMOPIPES  BUY ₹14.37 at ₹78.35 (fresh Friday signal — BUY: 14.27× weekly, month 4.58×, ladder rising; stop ₹49.82; charges ₹0.0170)
2023-09-25  KIRLOSIND   SELL ₹17.32 at stop ₹3,202.97 (+17.6%, charges ₹0.0180) — the cash goes back to work at the next Friday screen
2023-10-09  SASKEN      BUY ₹17.32 at ₹1,320.00 (fresh Friday signal — BUY: 11.93× weekly, month 9.60×, ladder rising; stop ₹962.02; charges ₹0.0205)
2023-10-20  FORCEMOT    SELL ₹30.84 at stop ₹3,709.99 (+90.2%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2023-10-23  ABAN        BUY ₹11.69 at ₹58.30 (fresh Friday signal — BUY: 8.09× weekly, month 4.41×, ladder rising; stop ₹39.55; charges ₹0.0139)
2023-10-23  ALANKIT     SELL ₹17.45 at stop ₹10.31 (+1.1%, charges ₹0.0181) — the cash goes back to work at the next Friday screen
2023-10-23  DHUNINV     BUY ₹19.14 at ₹1,020.00 (fresh Friday signal — BUY: 13.93× weekly, month 2.94×, ladder rising; stop ₹690.60; charges ₹0.0227)
2023-10-25  HAL         SELL ₹19.31 at stop ₹1,840.70 (+33.4%, charges ₹0.0200) — the cash goes back to work at the next Friday screen
2023-10-30  KKCL        BUY ₹19.03 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.93×, ladder rising; stop ₹674.12; charges ₹0.0225)
2023-10-30  SHAREINDIA  BUY ₹17.73 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.63×, ladder rising; stop ₹261.25; charges ₹0.0210)
2023-11-20  TEXMOPIPES  SELL ₹12.60 at stop ₹68.88 (-12.1%, charges ₹0.0131) — the cash goes back to work at the next Friday screen
2023-11-28  MUNJALAU    BUY ₹12.60 at ₹81.50 (fresh Friday signal — BUY: 19.68× weekly, month 7.19×, ladder rising; stop ₹58.90; charges ₹0.0149)
2024-01-17  TIIL        SELL ₹32.75 at stop ₹2,337.00 (+109.3%, charges ₹0.0340) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹21.81 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0258)
2024-01-24  PREMEXPLN   SELL ₹15.82 at stop ₹1,420.25 (+78.7%, charges ₹0.0164) — the cash goes back to work at the next Friday screen
2024-01-29  GANDHITUBE  BUY ₹23.15 at ₹811.30 (fresh Friday signal — BUY: 14.99× weekly, month 2.73×, ladder rising; stop ₹677.87; charges ₹0.0274)
2024-02-06  CONTROLPR   SELL ₹24.59 at stop ₹884.21 (+69.7%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2024-02-09  MUNJALAU    SELL ₹14.86 at stop ₹96.33 (+18.2%, charges ₹0.0154) — the cash goes back to work at the next Friday screen
2024-02-12  ASAL        BUY ₹20.37 at ₹652.00 (fresh Friday signal — BUY: 10.94× weekly, month 5.39×, ladder rising; stop ₹417.18; charges ₹0.0241)
2024-02-12  BALAXI      BUY ₹22.69 at ₹126.00 (fresh Friday signal — BUY: 19.83× weekly, month 5.34×, ladder rising; stop ₹79.07; charges ₹0.0269)
2024-03-06  BALAXI      SELL ₹18.30 at stop ₹101.86 (-19.2%, charges ₹0.0190) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹21.06 at stop ₹357.20 (+19.1%, charges ₹0.0218) — the cash goes back to work at the next Friday screen
2024-03-11  GANDHITUBE  SELL ₹20.69 at stop ₹726.75 (-10.4%, charges ₹0.0215) — the cash goes back to work at the next Friday screen
2024-03-11  SASKEN      SELL ₹21.16 at stop ₹1,616.00 (+22.4%, charges ₹0.0219) — the cash goes back to work at the next Friday screen
2024-03-11  SILINV      BUY ₹22.29 at ₹551.20 (fresh Friday signal — BUY: 10.53× weekly, month 4.88×, ladder rising; stop ₹421.85; charges ₹0.0264)
2024-03-11  SMSPHARMA   BUY ₹17.07 at ₹179.00 (fresh Friday signal — BUY: 8.20× weekly, month 12.63×, ladder rising; stop ₹132.95; charges ₹0.0202)
2024-03-13  DHUNINV     SELL ₹20.95 at stop ₹1,118.91 (+9.7%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹16.80 at stop ₹674.12 (-11.5%, charges ₹0.0174) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹21.86 at stop ₹666.47 (+0.5%, charges ₹0.0227) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹16.60 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.0197)
2024-03-18  FORCEMOT    BUY ₹21.16 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.51×, ladder rising; stop ₹5,500.61; charges ₹0.0251)
2024-03-18  HERCULES    BUY ₹21.24 at ₹517.70 (fresh Friday signal — BUY: 7.76× weekly, month 3.01×, ladder rising; stop ₹376.18; charges ₹0.0252)
2024-03-18  INDIGO      BUY ₹21.22 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0251)
2024-03-18  SOLARINDS   BUY ₹21.25 at ₹8,900.05 (fresh Friday signal — BUY: 4.28× weekly, month 2.84×, ladder rising; stop ₹5,332.29; charges ₹0.0252)
2024-04-01  ABAN        TRIM 5.3% (₹0.92 at ₹86.20) to pay the tax bill
2024-04-01  ASAL        TRIM 5.3% (₹0.99 at ₹594.55) to pay the tax bill
2024-04-01  BOSCHLTD    TRIM 5.3% (₹0.91 at ₹30,282.30) to pay the tax bill
2024-04-01  FORCEMOT    TRIM 5.3% (₹1.29 at ₹7,540.95) to pay the tax bill
2024-04-01  HARITASEAT  TRIM 5.3% (₹0.68 at ₹766.55) to pay the tax bill
2024-04-01  HERCULES    TRIM 5.3% (₹1.16 at ₹530.60) to pay the tax bill
2024-04-01  INDIGO      TRIM 5.3% (₹1.25 at ₹3,548.95) to pay the tax bill
2024-04-01  JSWHL       TRIM 5.3% (₹1.49 at ₹7,225.05) to pay the tax bill
2024-04-01  SILINV      TRIM 5.3% (₹1.09 at ₹506.00) to pay the tax bill
2024-04-01  SMSPHARMA   TRIM 5.3% (₹0.94 at ₹186.05) to pay the tax bill
2024-04-01  SOLARINDS   TRIM 5.3% (₹1.11 at ₹8,726.05) to pay the tax bill
2024-04-01  TAX         FY2024 settled: ₹11.8291 paid (STCG ₹59.15 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-15  HERCULES    SELL ₹19.38 at stop ₹500.03 (-3.4%, charges ₹0.0201) — the cash goes back to work at the next Friday screen
2024-04-22  JUSTDIAL    BUY ₹19.38 at ₹1,084.00 (fresh Friday signal — BUY: 11.71× weekly, month 3.19×, ladder rising; stop ₹821.08; charges ₹0.0230)
2024-05-09  JUSTDIAL    SELL ₹17.98 at stop ₹1,008.00 (-7.0%, charges ₹0.0187) — the cash goes back to work at the next Friday screen
2024-05-13  GRPLTD      BUY ₹17.98 at ₹7,884.20 (fresh Friday signal — BUY: 16.40× weekly, month 3.05×, ladder rising; stop ₹6,175.00; charges ₹0.0213)
2024-05-13  JSWHL       SELL ₹22.92 at stop ₹6,280.45 (+33.6%, charges ₹0.0238) — the cash goes back to work at the next Friday screen
2024-05-21  DLINKINDIA  BUY ₹22.55 at ₹415.85 (fresh Friday signal — BUY: 21.84× weekly, month 3.73×, ladder rising; stop ₹292.50; charges ₹0.0267)
2024-05-28  FORCEMOT    SELL ₹24.60 at stop ₹8,083.64 (+23.1%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹22.37 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0265)
2024-06-04  ASAL        SELL ₹22.70 at stop ₹769.50 (+18.0%, charges ₹0.0236) — the cash goes back to work at the next Friday screen
2024-06-04  BOSCHLTD    SELL ₹15.42 at stop ₹29,015.09 (-1.6%, charges ₹0.0160) — the cash goes back to work at the next Friday screen
2024-06-04  GRPLTD      SELL ₹18.44 at stop ₹8,103.50 (+2.8%, charges ₹0.0191) — the cash goes back to work at the next Friday screen
2024-06-04  SMSPHARMA   SELL ₹16.34 at stop ₹181.36 (+1.3%, charges ₹0.0169) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹18.00 at stop ₹7,980.95 (-10.3%, charges ₹0.0187) — the cash goes back to work at the next Friday screen
2024-06-10  BHAGCHEM    BUY ₹21.43 at ₹238.99 (fresh Friday signal — BUY: 8.45× weekly, month 2.68×, ladder rising; stop ₹175.70; charges ₹0.0254)
2024-06-10  FIEMIND     BUY ₹21.50 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0255)
2024-06-10  MATRIMONY   BUY ₹21.56 at ₹643.50 (fresh Friday signal — BUY: 5.35× weekly, month 1.60×, ladder rising; stop ₹496.18; charges ₹0.0255)
2024-06-10  UNOMINDA    BUY ₹21.48 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0255)
2024-07-19  UNOMINDA    SELL ₹21.70 at stop ₹981.87 (+1.2%, charges ₹0.0225) — the cash goes back to work at the next Friday screen
2024-07-22  SPORTKING   BUY ₹22.64 at ₹1,100.00 (fresh Friday signal — BUY: 13.36× weekly, month 3.52×, ladder rising; stop ₹817.24; charges ₹0.0268)
2024-07-23  FIEMIND     SELL ₹20.44 at stop ₹1,257.56 (-4.7%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2024-07-23  MATRIMONY   SELL ₹18.88 at stop ₹564.77 (-12.2%, charges ₹0.0196) — the cash goes back to work at the next Friday screen
2024-07-29  AWHCL       BUY ₹21.78 at ₹890.05 (fresh Friday signal — BUY: 11.66× weekly, month 4.34×, ladder rising; stop ₹529.53; charges ₹0.0258)
2024-07-29  NAHARINDUS  BUY ₹24.13 at ₹157.45 (fresh Friday signal — BUY: 11.88× weekly, month 3.04×, ladder rising; stop ₹124.68; charges ₹0.0286)
2024-08-05  BHAGCHEM    SELL ₹29.83 at stop ₹333.45 (+39.5%, charges ₹0.0309) — the cash goes back to work at the next Friday screen
2024-08-05  NAHARINDUS  SELL ₹22.38 at stop ₹146.39 (-7.0%, charges ₹0.0232) — the cash goes back to work at the next Friday screen
2024-08-09  AWHCL       SELL ₹18.12 at stop ₹742.33 (-16.6%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2024-08-12  ARROWGREEN  BUY ₹22.32 at ₹853.00 (fresh Friday signal — BUY: 6.29× weekly, month 3.90×, ladder rising; stop ₹603.20; charges ₹0.0264)
2024-08-12  GHCLTEXTIL  BUY ₹22.47 at ₹109.60 (fresh Friday signal — BUY: 6.24× weekly, month 3.75×, ladder rising; stop ₹95.47; charges ₹0.0266)
2024-08-12  OSWALAGRO   BUY ₹22.18 at ₹60.80 (fresh Friday signal — BUY: 16.74× weekly, month 2.15×, ladder rising; stop ₹42.18; charges ₹0.0263)
2024-08-16  CAMPUS      SELL ₹21.63 at stop ₹277.07 (-3.1%, charges ₹0.0224) — the cash goes back to work at the next Friday screen
2024-08-19  HERANBA     BUY ₹22.63 at ₹467.00 (fresh Friday signal — BUY: 8.02× weekly, month 3.41×, ladder rising; stop ₹342.95; charges ₹0.0268)
2024-09-13  SPORTKING   SELL ₹27.89 at stop ₹1,358.45 (+23.5%, charges ₹0.0289) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹23.96 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0284)
2024-10-04  DLINKINDIA  SELL ₹31.87 at stop ₹589.05 (+41.6%, charges ₹0.0331) — the cash goes back to work at the next Friday screen
2024-10-07  ARROWGREEN  SELL ₹18.89 at stop ₹723.58 (-15.2%, charges ₹0.0196) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹16.33 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0193)
2024-10-07  GHCLTEXTIL  SELL ₹19.53 at stop ₹95.47 (-12.9%, charges ₹0.0203) — the cash goes back to work at the next Friday screen
2024-10-07  HERANBA     SELL ₹21.82 at stop ₹451.30 (-3.4%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2024-10-07  INDIGO      SELL ₹28.09 at stop ₹4,485.14 (+40.2%, charges ₹0.0291) — the cash goes back to work at the next Friday screen
2024-10-07  MAANALU     BUY ₹21.85 at ₹180.00 (fresh Friday signal — BUY: 18.92× weekly, month 4.26×, ladder rising; stop ₹126.35; charges ₹0.0259)
2024-10-14  BSE         BUY ₹21.06 at ₹4,536.00 (fresh Friday signal — BUY: 2.79× weekly, month 4.25×, ladder rising; stop ₹3,393.93; charges ₹0.0250)
2024-10-14  DBCORP      BUY ₹22.51 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0267)
2024-10-14  SKIPPER     BUY ₹22.33 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0265)
2024-10-14  SRHHYPOLTD  BUY ₹22.42 at ₹893.10 (fresh Friday signal — BUY: 3.73× weekly, month 8.71×, ladder rising; stop ₹647.47; charges ₹0.0266)
2024-10-25  DBCORP      SELL ₹19.28 at stop ₹302.08 (-14.2%, charges ₹0.0200) — the cash goes back to work at the next Friday screen
2024-11-04  AKZOINDIA   BUY ₹19.28 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.0455)
2024-11-05  MAANALU     SELL ₹23.37 at stop ₹193.14 (+7.3%, charges ₹0.0519) — the cash goes back to work at the next Friday screen
2024-11-11  SIYSIL      BUY ₹21.45 at ₹701.85 (fresh Friday signal — BUY: 10.52× weekly, month 5.04×, ladder rising; stop ₹439.76; charges ₹0.0506)
2024-11-13  ABAN        SELL ₹11.25 at stop ₹59.43 (+1.9%, charges ₹0.0250) — the cash goes back to work at the next Friday screen
2024-11-13  SRHHYPOLTD  SELL ₹16.20 at stop ₹647.47 (-27.5%, charges ₹0.0360) — the cash goes back to work at the next Friday screen
2024-11-14  ASTRAZEN    SELL ₹14.99 at stop ₹6,854.77 (-7.9%, charges ₹0.0333) — the cash goes back to work at the next Friday screen
2024-11-18  SASKEN      BUY ₹20.69 at ₹2,015.25 (fresh Friday signal — BUY: 9.07× weekly, month 2.15×, ladder rising; stop ₹1,640.65; charges ₹0.0488)
2024-11-18  VHL         BUY ₹20.77 at ₹5,080.00 (fresh Friday signal — BUY: 6.85× weekly, month 5.05×, ladder rising; stop ₹3,556.30; charges ₹0.0490)
2024-12-26  PRSMJOHNSN  SELL ₹18.98 at stop ₹170.55 (-20.5%, charges ₹0.0422) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹14.54 at stop ₹3,423.18 (-24.2%, charges ₹0.0323) — the cash goes back to work at the next Friday screen
2024-12-27  VHL         SELL ₹17.94 at stop ₹4,408.00 (-13.2%, charges ₹0.0399) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹21.15 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.0499)
2024-12-30  KFINTECH    BUY ₹21.08 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.0498)
2024-12-30  NACLIND     BUY ₹12.12 at ₹67.60 (fresh Friday signal — BUY: 1.75× weekly, month 2.31×, ladder rising; stop ₹53.45; charges ₹0.0286)
2025-01-10  SKIPPER     SELL ₹19.21 at stop ₹477.28 (-13.7%, charges ₹0.0427) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹19.21 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0453)
2025-01-15  KFINTECH    SELL ₹16.09 at stop ₹1,159.14 (-23.3%, charges ₹0.0357) — the cash goes back to work at the next Friday screen
2025-01-20  ZOTA        BUY ₹16.09 at ₹1,016.45 (fresh Friday signal — ACCUMULATE: 3.76× weekly, month 3.93×, ladder rising; stop ₹863.60; charges ₹0.0380)
2025-01-21  SASKEN      SELL ₹20.37 at stop ₹1,993.24 (-1.1%, charges ₹0.0453) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹16.05 at stop ₹700.36 (-16.1%, charges ₹0.0356) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹18.84 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0445)
2025-01-27  MBAPL       BUY ₹17.58 at ₹58.20 (fresh Friday signal — ACCUMULATE: 3.22× weekly, month 3.87×, ladder rising; stop ₹50.92; charges ₹0.0415)
2025-01-27  NACLIND     SELL ₹10.94 at stop ₹61.28 (-9.3%, charges ₹0.0243) — the cash goes back to work at the next Friday screen
2025-01-27  OSWALAGRO   SELL ₹21.97 at stop ₹60.42 (-0.6%, charges ₹0.0488) — the cash goes back to work at the next Friday screen
2025-01-27  SILINV      SELL ₹20.92 at stop ₹548.20 (-0.5%, charges ₹0.0465) — the cash goes back to work at the next Friday screen
2025-01-28  ZOTA        SELL ₹13.61 at stop ₹863.60 (-15.0%, charges ₹0.0302) — the cash goes back to work at the next Friday screen
2025-01-30  SIYSIL      SELL ₹23.44 at stop ₹770.45 (+9.8%, charges ₹0.0521) — the cash goes back to work at the next Friday screen
2025-02-03  APOLLO      BUY ₹18.85 at ₹126.50 (fresh Friday signal — ACCUMULATE: 1.55× weekly, month 3.75×, ladder rising; stop ₹98.89; charges ₹0.0445)
2025-02-03  ZENSARTECH  BUY ₹18.97 at ₹947.00 (fresh Friday signal — BUY: 2.25× weekly, month 2.40×, ladder rising; stop ₹727.84; charges ₹0.0448)
2025-02-12  JINDWORLD   SELL ₹19.32 at stop ₹374.11 (-8.2%, charges ₹0.0429) — the cash goes back to work at the next Friday screen
2025-02-24  TAJGVK      BUY ₹17.93 at ₹440.40 (fresh Friday signal — BUY: 2.16× weekly, month 2.07×, ladder rising; stop ₹349.09; charges ₹0.0423)
2025-02-24  TCPLPACK    BUY ₹18.00 at ₹3,997.25 (fresh Friday signal — BUY: 8.08× weekly, month 1.73×, ladder rising; stop ₹2,770.57; charges ₹0.0425)
2025-02-28  BSE         SELL ₹22.92 at stop ₹4,954.63 (+9.2%, charges ₹0.0509) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹17.62 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0416)
2025-03-03  ZENSARTECH  SELL ₹14.51 at stop ₹727.84 (-23.1%, charges ₹0.0322) — the cash goes back to work at the next Friday screen
2025-03-10  GRMOVER     BUY ₹18.34 at ₹252.00 (fresh Friday signal — BUY: 1.55× weekly, month 1.68×, ladder rising; stop ₹203.86; charges ₹0.0433)
2025-03-17  AVANTIFEED  BUY ₹18.48 at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹0.0436)
2025-03-24  INDIASHLTR  BUY ₹19.09 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.0451)
2025-03-27  MBAPL       SELL ₹16.05 at stop ₹53.39 (-8.3%, charges ₹0.0357) — the cash goes back to work at the next Friday screen
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹13.55 / LT ₹0.00)
2025-04-02  TAJGVK      SELL ₹18.37 at stop ₹453.34 (+2.9%, charges ₹0.0408) — the cash goes back to work at the next Friday screen
2025-04-07  APOLLO      SELL ₹16.66 at stop ₹112.29 (-11.2%, charges ₹0.0370) — the cash goes back to work at the next Friday screen
2025-04-07  AVANTIFEED  SELL ₹14.17 at stop ₹648.95 (-23.0%, charges ₹0.0315) — the cash goes back to work at the next Friday screen
2025-04-07  INDIASHLTR  SELL ₹17.66 at stop ₹738.82 (-7.1%, charges ₹0.0392) — the cash goes back to work at the next Friday screen
2025-04-07  NACLIND     BUY ₹16.93 at ₹128.14 (fresh Friday signal — BUY: 3.16× weekly, month 13.84×, ladder rising; stop ₹89.22; charges ₹0.0400)
2025-04-07  TCPLPACK    SELL ₹17.94 at stop ₹4,002.68 (+0.1%, charges ₹0.0398) — the cash goes back to work at the next Friday screen
2025-04-07  VADILALIND  BUY ₹17.84 at ₹4,820.55 (fresh Friday signal — BUY: 9.64× weekly, month 5.36×, ladder rising; stop ₹4,255.30; charges ₹0.0421)
2025-04-15  AVANTIFEED  BUY ₹18.99 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.62× weekly, month 1.80×, ladder rising; stop ₹492.75; charges ₹0.0448)
2025-04-15  INDIASHLTR  BUY ₹19.06 at ₹865.00 (fresh Friday signal — BUY: 1.57× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.0450)
2025-04-15  SPMLINFRA   BUY ₹18.93 at ₹213.00 (fresh Friday signal — ACCUMULATE: 2.58× weekly, month 4.14×, ladder rising; stop ₹109.59; charges ₹0.0447)
2025-05-07  GRMOVER     SELL ₹21.07 at stop ₹290.80 (+15.4%, charges ₹0.0468) — the cash goes back to work at the next Friday screen
2025-05-12  KPRMILL     BUY ₹19.50 at ₹1,302.00 (fresh Friday signal — BUY: 15.89× weekly, month 3.16×, ladder rising; stop ₹938.50; charges ₹0.0460)
2025-05-12  SPORTKING   BUY ₹11.01 at ₹113.50 (fresh Friday signal — ACCUMULATE: 5.52× weekly, month 3.14×, ladder rising; stop ₹97.85; charges ₹0.0260)
2025-05-30  VADILALIND  SELL ₹19.89 at stop ₹5,401.40 (+12.0%, charges ₹0.0442) — the cash goes back to work at the next Friday screen
2025-06-02  IPL         BUY ₹18.47 at ₹207.95 (fresh Friday signal — BUY: 11.52× weekly, month 2.94×, ladder rising; stop ₹126.73; charges ₹0.0436)
2025-06-02  SPORTKING   SELL ₹10.39 at stop ₹107.55 (-5.2%, charges ₹0.0231) — the cash goes back to work at the next Friday screen
2025-06-09  NDRAUTO     BUY ₹11.81 at ₹1,079.95 (fresh Friday signal — BUY: 10.88× weekly, month 3.06×, ladder rising; stop ₹778.90; charges ₹0.0279)
2025-07-28  NDRAUTO     SELL ₹10.63 at stop ₹976.51 (-9.6%, charges ₹0.0236) — the cash goes back to work at the next Friday screen
2025-08-01  KPRMILL     SELL ₹16.53 at stop ₹1,108.74 (-14.8%, charges ₹0.0367) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹21.95 at stop ₹1,814.78 (+25.2%, charges ₹0.0488) — the cash goes back to work at the next Friday screen
2025-08-04  PUNJABCHEM  BUY ₹19.34 at ₹1,403.00 (fresh Friday signal — BUY: 43.22× weekly, month 9.53×, ladder rising; stop ₹1,208.88; charges ₹0.0456)
2025-08-11  PRAKASH     BUY ₹10.63 at ₹178.70 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 2.59×, ladder rising; stop ₹145.68; charges ₹0.0251)
2025-08-11  RAIN        BUY ₹19.15 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.0452)
2025-08-18  PUNJABCHEM  SELL ₹16.59 at stop ₹1,208.88 (-13.8%, charges ₹0.0368) — the cash goes back to work at the next Friday screen
2025-08-25  RISHABH     BUY ₹16.59 at ₹424.25 (fresh Friday signal — BUY: 41.22× weekly, month 7.62×, ladder rising; stop ₹263.20; charges ₹0.0392)
2025-08-26  RAIN        SELL ₹17.08 at stop ₹143.64 (-10.4%, charges ₹0.0379) — the cash goes back to work at the next Friday screen
2025-09-01  GANDHITUBE  BUY ₹17.08 at ₹865.00 (fresh Friday signal — BUY: 9.32× weekly, month 5.18×, ladder rising; stop ₹709.84; charges ₹0.0403)
2025-09-26  INDIASHLTR  SELL ₹18.82 at stop ₹857.85 (-0.8%, charges ₹0.0418) — the cash goes back to work at the next Friday screen
2025-09-26  SPMLINFRA   SELL ₹22.32 at stop ₹252.27 (+18.4%, charges ₹0.0496) — the cash goes back to work at the next Friday screen
2025-09-29  SUBROS      BUY ₹18.63 at ₹1,132.00 (fresh Friday signal — BUY: 8.24× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0440)
2025-09-29  TVSELECT    BUY ₹18.73 at ₹627.00 (fresh Friday signal — BUY: 6.94× weekly, month 4.12×, ladder rising; stop ₹379.50; charges ₹0.0442)
2025-10-14  IPL         SELL ₹17.49 at stop ₹197.80 (-4.9%, charges ₹0.0389) — the cash goes back to work at the next Friday screen
2025-10-14  SUBROS      SELL ₹17.15 at stop ₹1,046.90 (-7.5%, charges ₹0.0381) — the cash goes back to work at the next Friday screen
2025-10-16  GANDHITUBE  SELL ₹17.13 at stop ₹871.15 (+0.7%, charges ₹0.0380) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹18.06 at ₹1,574.50 (fresh Friday signal — BUY: 13.09× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0426)
2025-10-20  CIEINDIA    BUY ₹18.09 at ₹432.50 (fresh Friday signal — ACCUMULATE: 5.25× weekly, month 2.01×, ladder rising; stop ₹377.39; charges ₹0.0427)
2025-10-20  CREDITACC   SELL ₹28.12 at stop ₹1,274.42 (+49.9%, charges ₹0.0625) — the cash goes back to work at the next Friday screen
2025-10-20  PVSL        BUY ₹18.10 at ₹148.00 (fresh Friday signal — BUY: 4.97× weekly, month 1.77×, ladder rising; stop ₹129.21; charges ₹0.0427)
2025-10-27  BHAGERIA    BUY ₹18.39 at ₹237.00 (fresh Friday signal — BUY: 24.69× weekly, month 8.89×, ladder rising; stop ₹159.69; charges ₹0.0434)
2025-10-27  KICL        BUY ₹11.04 at ₹6,006.00 (fresh Friday signal — BUY: 7.09× weekly, month 2.03×, ladder rising; stop ₹4,575.39; charges ₹0.0261)
2025-11-11  PVSL        SELL ₹16.17 at stop ₹132.82 (-10.3%, charges ₹0.0359) — the cash goes back to work at the next Friday screen
2025-11-14  PRAKASH     SELL ₹8.72 at stop ₹147.31 (-17.6%, charges ₹0.0194) — the cash goes back to work at the next Friday screen
2025-11-17  PGIL        BUY ₹17.58 at ₹844.05 (fresh Friday signal — BUY: 19.68× weekly, month 3.52×, ladder rising; stop ₹612.56; charges ₹0.0415)
2025-11-20  ANANDRATHI  SELL ₹16.56 at stop ₹1,450.17 (-7.9%, charges ₹0.0368) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹17.26 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0407)
2025-11-25  TVSELECT    SELL ₹16.21 at stop ₹545.26 (-13.0%, charges ₹0.0360) — the cash goes back to work at the next Friday screen
2025-12-01  VLSFINANCE  BUY ₹17.09 at ₹311.80 (fresh Friday signal — ACCUMULATE: 7.01× weekly, month 5.08×, ladder rising; stop ₹276.07; charges ₹0.0403)
2025-12-08  RISHABH     SELL ₹14.94 at stop ₹383.85 (-9.5%, charges ₹0.0332) — the cash goes back to work at the next Friday screen
2025-12-09  PGIL        SELL ₹15.88 at stop ₹765.71 (-9.3%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2025-12-15  ESABINDIA   BUY ₹16.33 at ₹6,203.50 (fresh Friday signal — BUY: 2.22× weekly, month 2.04×, ladder rising; stop ₹5,247.99; charges ₹0.0386)
2025-12-15  INFOBEAN    BUY ₹16.19 at ₹696.70 (fresh Friday signal — ACCUMULATE: 3.25× weekly, month 2.25×, ladder rising; stop ₹586.67; charges ₹0.0382)
2025-12-16  VLSFINANCE  SELL ₹15.06 at stop ₹276.07 (-11.5%, charges ₹0.0335) — the cash goes back to work at the next Friday screen
2025-12-17  NACLIND     SELL ₹21.59 at stop ₹164.20 (+28.1%, charges ₹0.0480) — the cash goes back to work at the next Friday screen
2025-12-22  APEX        BUY ₹16.47 at ₹288.50 (fresh Friday signal — ACCUMULATE: 5.61× weekly, month 12.16×, ladder rising; stop ₹221.66; charges ₹0.0389)
2025-12-22  ASIANTILES  BUY ₹16.45 at ₹72.69 (fresh Friday signal — BUY: 4.41× weekly, month 1.60×, ladder rising; stop ₹53.03; charges ₹0.0388)
2026-01-09  RADICO      SELL ₹15.44 at stop ₹2,956.49 (-10.1%, charges ₹0.0343) — the cash goes back to work at the next Friday screen
2026-01-12  AGIIL       BUY ₹16.00 at ₹295.60 (fresh Friday signal — ACCUMULATE: 5.45× weekly, month 2.06×, ladder rising; stop ₹202.47; charges ₹0.0378)
2026-01-12  ASIANTILES  SELL ₹15.82 at stop ₹70.21 (-3.4%, charges ₹0.0351) — the cash goes back to work at the next Friday screen
2026-01-12  ESABINDIA   SELL ₹14.69 at stop ₹5,605.00 (-9.6%, charges ₹0.0326) — the cash goes back to work at the next Friday screen
2026-01-19  KICL        SELL ₹8.43 at stop ₹4,607.98 (-23.3%, charges ₹0.0187) — the cash goes back to work at the next Friday screen
2026-01-19  KIRIINDUS   BUY ₹15.58 at ₹530.30 (fresh Friday signal — ACCUMULATE: 2.70× weekly, month 9.40×, ladder rising; stop ₹382.56; charges ₹0.0368)
2026-01-19  NITCO       BUY ₹15.61 at ₹89.00 (fresh Friday signal — ACCUMULATE: 5.88× weekly, month 2.19×, ladder rising; stop ₹75.12; charges ₹0.0368)
2026-01-20  BHAGERIA    SELL ₹12.43 at stop ₹160.92 (-32.1%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹17.30 at stop ₹748.60 (-8.5%, charges ₹0.0384) — the cash goes back to work at the next Friday screen
2026-02-02  HINDCOPPER  BUY ₹15.14 at ₹590.15 (fresh Friday signal — BUY: 2.81× weekly, month 4.88×, ladder rising; stop ₹485.74; charges ₹0.0357)
2026-02-02  NATIONALUM  BUY ₹15.19 at ₹347.10 (fresh Friday signal — BUY: 1.65× weekly, month 2.02×, ladder rising; stop ₹335.49; charges ₹0.0359)
2026-02-09  AUTOAXLES   BUY ₹14.34 at ₹1,950.00 (fresh Friday signal — BUY: 2.95× weekly, month 1.68×, ladder rising; stop ₹1,727.19; charges ₹0.0339)
2026-02-17  NATIONALUM  SELL ₹14.61 at stop ₹335.49 (-3.3%, charges ₹0.0325) — the cash goes back to work at the next Friday screen
2026-02-19  NITCO       SELL ₹13.11 at stop ₹75.12 (-15.6%, charges ₹0.0291) — the cash goes back to work at the next Friday screen
2026-02-23  E2E         BUY ₹11.37 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0268)
2026-02-23  VESUVIUS    BUY ₹16.36 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.56×, ladder rising; stop ₹464.31; charges ₹0.0386)
2026-02-27  APEX        SELL ₹22.12 at stop ₹389.22 (+34.9%, charges ₹0.0491) — the cash goes back to work at the next Friday screen
2026-02-27  INFOBEAN    SELL ₹17.81 at stop ₹770.07 (+10.5%, charges ₹0.0396) — the cash goes back to work at the next Friday screen
2026-03-02  AYMSYNTEX   BUY ₹8.84 at ₹197.99 (fresh Friday signal — BUY: 2.17× weekly, month 1.58×, ladder rising; stop ₹167.00; charges ₹0.0209)
2026-03-02  J&KBANK     BUY ₹15.54 at ₹116.20 (fresh Friday signal — BUY: 8.67× weekly, month 1.90×, ladder rising; stop ₹96.50; charges ₹0.0367)
2026-03-02  KIRIINDUS   SELL ₹12.50 at stop ₹427.56 (-19.4%, charges ₹0.0278) — the cash goes back to work at the next Friday screen
2026-03-02  KSB         BUY ₹15.54 at ₹738.00 (fresh Friday signal — BUY: 52.86× weekly, month 4.75×, ladder rising; stop ₹658.54; charges ₹0.0367)
2026-03-12  AYMSYNTEX   SELL ₹7.75 at stop ₹174.33 (-12.0%, charges ₹0.0172) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹13.50 at stop ₹528.63 (-10.4%, charges ₹0.0300) — the cash goes back to work at the next Friday screen
2026-03-13  AUTOAXLES   SELL ₹13.01 at stop ₹1,776.59 (-8.9%, charges ₹0.0289) — the cash goes back to work at the next Friday screen
2026-03-16  ABB         BUY ₹15.03 at ₹6,400.00 (fresh Friday signal — BUY: 1.80× weekly, month 1.91×, ladder rising; stop ₹5,486.25; charges ₹0.0355)
2026-03-16  APOLLOPIPE  BUY ₹15.10 at ₹407.55 (fresh Friday signal — BUY: 65.78× weekly, month 26.35×, ladder rising; stop ₹315.92; charges ₹0.0357)
2026-03-16  JBCHEPHARM  BUY ₹15.06 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0356)
2026-03-23  J&KBANK     SELL ₹14.74 at stop ₹110.67 (-4.8%, charges ₹0.0327) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹14.13 at stop ₹464.31 (-13.2%, charges ₹0.0314) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹14.67 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0346)
2026-03-30  AGIIL       SELL ₹14.65 at stop ₹271.80 (-8.1%, charges ₹0.0325) — the cash goes back to work at the next Friday screen
2026-03-30  BAJAJHIND   BUY ₹14.60 at ₹16.42 (fresh Friday signal — ACCUMULATE: 2.06× weekly, month 1.79×, ladder rising; stop ₹13.87; charges ₹0.0345)
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹38.53 / LT ₹0.00)
2026-04-06  SEAMECLTD   BUY ₹14.86 at ₹1,525.00 (fresh Friday signal — BUY: 1.99× weekly, month 1.63×, ladder rising; stop ₹1,188.45; charges ₹0.0351)
2026-05-04  KSB         SELL ₹19.23 at stop ₹917.42 (+24.3%, charges ₹0.0427) — the cash goes back to work at the next Friday screen
2026-05-11  CRAFTSMAN   BUY ₹15.75 at ₹9,039.50 (fresh Friday signal — BUY: 22.97× weekly, month 3.93×, ladder rising; stop ₹7,119.77; charges ₹0.0372)
2026-05-14  AETHER      SELL ₹14.29 at stop ₹1,125.84 (-2.1%, charges ₹0.0317) — the cash goes back to work at the next Friday screen
2026-05-14  BAJAJHIND   SELL ₹15.89 at stop ₹17.96 (+9.4%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2026-05-18  EXPLEOSOL   BUY ₹15.50 at ₹903.95 (fresh Friday signal — BUY: 23.54× weekly, month 5.55×, ladder rising; stop ₹757.15; charges ₹0.0366)
2026-05-18  SASKEN      BUY ₹15.36 at ₹1,680.10 (fresh Friday signal — BUY: 74.07× weekly, month 16.58×, ladder rising; stop ₹1,161.09; charges ₹0.0363)
2026-06-05  E2E         SELL ₹9.06 at stop ₹2,330.72 (-20.0%, charges ₹0.0201) — the cash goes back to work at the next Friday screen
2026-06-08  SOTL        BUY ₹12.81 at ₹545.00 (fresh Friday signal — BUY: 36.35× weekly, month 21.97×, ladder rising; stop ₹369.30; charges ₹0.0302)
2026-06-10  EXPLEOSOL   SELL ₹13.64 at stop ₹799.25 (-11.6%, charges ₹0.0303) — the cash goes back to work at the next Friday screen
2026-06-11  CIEINDIA    SELL ₹17.89 at stop ₹429.88 (-0.6%, charges ₹0.0397) — the cash goes back to work at the next Friday screen
2026-06-15  CLSEL       BUY ₹15.64 at ₹297.00 (fresh Friday signal — ACCUMULATE: 27.01× weekly, month 6.47×, ladder rising; stop ₹238.93; charges ₹0.0369)
2026-06-15  PANAMAPET   BUY ₹15.89 at ₹384.80 (fresh Friday signal — BUY: 27.33× weekly, month 13.61×, ladder rising; stop ₹274.50; charges ₹0.0375)
2026-06-17  SEAMECLTD   SELL ₹13.57 at stop ₹1,398.40 (-8.3%, charges ₹0.0301) — the cash goes back to work at the next Friday screen
2026-06-22  SPAL        BUY ₹13.57 at ₹1,030.00 (fresh Friday signal — BUY: 66.34× weekly, month 8.68×, ladder rising; stop ₹746.08; charges ₹0.0320)
2026-06-29  SOTL        SELL ₹11.92 at stop ₹509.53 (-6.5%, charges ₹0.0265) — the cash goes back to work at the next Friday screen
2026-07-06  RAMCOSYS    BUY ₹11.92 at ₹815.50 (fresh Friday signal — BUY: 12.59× weekly, month 27.42×, ladder rising; stop ₹499.70; charges ₹0.0281)
2026-07-08  SASKEN      SELL ₹17.59 at stop ₹1,933.72 (+15.1%, charges ₹0.0391) — the cash goes back to work at the next Friday screen
2026-07-13  MUNJALAU    BUY ₹15.81 at ₹100.50 (fresh Friday signal — BUY: 19.01× weekly, month 7.01×, ladder rising; stop ₹81.15; charges ₹0.0373)
2026-07-16  SPAL        SELL ₹13.47 at stop ₹1,027.62 (-0.2%, charges ₹0.0299) — the cash goes back to work at the next Friday screen
2026-07-20  JUSTDIAL    BUY ₹15.26 at ₹766.00 (fresh Friday signal — BUY: 127.42× weekly, month 29.52×, ladder rising; stop ₹509.20; charges ₹0.0360)
2026-07-24  RAMCOSYS    SELL ₹10.51 at stop ₹722.48 (-11.4%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2026-07-27  BLUESTONE   BUY ₹10.51 at ₹793.00 (fresh Friday signal — BUY: 47.94× weekly, month 6.10×, ladder rising; stop ₹559.17; charges ₹0.0248)
2026-08-18  JUSTDIAL    SELL ₹13.06 at stop ₹658.64 (-14.0%, charges ₹0.0290) — the cash goes back to work at the next Friday screen
2026-08-24  AVTNPL      BUY ₹13.06 at ₹87.80 (fresh Friday signal — BUY: 10.00× weekly, month 2.79×, ladder rising; stop ₹62.04; charges ₹0.0308)
2026-09-15  ABB         SELL ₹16.73 at stop ₹7,158.25 (+11.8%, charges ₹0.0372) — the cash goes back to work at the next Friday screen
2026-09-15  MUNJALAU    SELL ₹16.38 at stop ₹104.60 (+4.1%, charges ₹0.0364) — the cash goes back to work at the next Friday screen
2026-09-16  CLSEL       SELL ₹14.39 at stop ₹274.60 (-7.5%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2026-09-16  PANAMAPET   SELL ₹18.13 at stop ₹440.87 (+14.6%, charges ₹0.0403) — the cash goes back to work at the next Friday screen
2026-09-21  FOSECOIND   BUY ₹15.80 at ₹6,748.00 (fresh Friday signal — BUY: 12.20× weekly, month 9.17×, ladder rising; stop ₹5,714.73; charges ₹0.0373)
2026-09-21  NPST        BUY ₹15.83 at ₹1,820.00 (fresh Friday signal — BUY: 15.64× weekly, month 6.01×, ladder rising; stop ₹1,539.95; charges ₹0.0374)
2026-09-21  NRBBEARING  BUY ₹15.75 at ₹531.10 (fresh Friday signal — BUY: 4.28× weekly, month 1.73×, ladder rising; stop ₹419.14; charges ₹0.0372)
2026-09-21  SHOPERSTOP  BUY ₹15.77 at ₹398.60 (fresh Friday signal — ACCUMULATE: 5.07× weekly, month 1.54×, ladder rising; stop ₹351.39; charges ₹0.0372)
```
