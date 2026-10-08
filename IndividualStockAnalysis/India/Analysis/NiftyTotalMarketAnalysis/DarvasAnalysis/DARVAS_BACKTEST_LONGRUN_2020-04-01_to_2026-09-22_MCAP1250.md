# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 2272 symbols, fetched once into `ROLLING_MCAP1250_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹181.37** | **+9.64% a year** |
| The same system before costs and taxes | ₹206.52 | +11.86% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹288.59 | +17.80% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹181.37** (+9.64% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 455 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹11.92** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹23.16**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹15.34 | ₹0.00 | ₹3.0685 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹36.83 | ₹11.83 | ₹8.8443 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹8.24 | ₹19.44 | ₹4.0776 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹35.85 | ₹0.00 | ₹7.1701 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹13.97 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹31.70 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹22.56 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 127.25 | +27.3% | +27.9% | +70.1% |
| 2021 (2021-12-31) | 179.67 | +41.2% | +45.4% | +26.2% |
| 2022 (2022-12-30) | 212.93 | +18.5% | +20.0% | +4.3% |
| 2023 (2023-12-29) | 250.64 | +17.7% | +20.5% | +20.0% |
| 2024 (2024-12-27) | 232.01 | -7.4% | -4.2% | +9.6% |
| 2025 (2025-12-26) | 183.21 | -21.0% | -19.9% | +9.4% |
| 2026 (2026-09-22) | 181.37 | -1.0% | +0.1% | -10.4% |

## What it took to earn it

- **Maximum drawdown: -36.3%** (peak 2024-09-13 → trough 2026-04-02, on weekly closes).
- **209 closed trades**: 84 winners (40%), average winner +30.2%, average loser -12.0%.
- Best closed trade 21STCENMGM +281.0%; worst MRPL -40.3%.
- Median holding period 51 days.
- Cash share of equity averaged 9% across all weeks (median 3%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.20 | 59.96 | 4 |
| 2020-05-29 | 113.44 | 0.00 | 10 |
| 2020-06-26 | 124.75 | 0.00 | 10 |
| 2020-07-31 | 127.90 | 23.71 | 8 |
| 2020-08-28 | 126.01 | 0.00 | 10 |
| 2020-09-25 | 124.77 | 31.94 | 7 |
| 2020-10-30 | 122.73 | 6.17 | 9 |
| 2020-11-27 | 128.04 | 4.48 | 10 |
| 2020-12-24 | 127.25 | 66.35 | 5 |
| 2021-01-29 | 127.53 | 21.94 | 8 |
| 2021-02-26 | 134.03 | 0.00 | 10 |
| 2021-03-26 | 127.07 | 13.89 | 9 |
| 2021-04-30 | 137.19 | 0.00 | 11 |
| 2021-05-28 | 144.21 | 0.00 | 11 |
| 2021-06-25 | 163.90 | 0.00 | 11 |
| 2021-07-30 | 172.32 | 13.91 | 10 |
| 2021-08-27 | 161.82 | 18.53 | 9 |
| 2021-09-24 | 177.64 | 2.22 | 10 |
| 2021-10-29 | 181.04 | 31.84 | 8 |
| 2021-11-26 | 185.10 | 34.53 | 8 |
| 2021-12-31 | 179.67 | 17.61 | 10 |
| 2022-01-28 | 182.99 | 47.84 | 8 |
| 2022-02-25 | 164.63 | 30.71 | 9 |
| 2022-03-25 | 183.00 | 15.78 | 10 |
| 2022-04-29 | 182.73 | 2.16 | 10 |
| 2022-05-27 | 199.00 | 0.00 | 10 |
| 2022-06-24 | 194.41 | 0.00 | 10 |
| 2022-07-29 | 206.60 | 8.88 | 9 |
| 2022-08-26 | 222.87 | 8.88 | 9 |
| 2022-09-30 | 207.56 | 27.97 | 8 |
| 2022-10-28 | 217.39 | 7.22 | 9 |
| 2022-11-25 | 224.36 | 7.64 | 9 |
| 2022-12-30 | 212.93 | 0.00 | 10 |
| 2023-01-27 | 203.70 | 18.77 | 9 |
| 2023-02-24 | 188.32 | 0.00 | 10 |
| 2023-03-31 | 179.56 | 95.91 | 5 |
| 2023-04-28 | 196.23 | 2.98 | 10 |
| 2023-05-26 | 206.07 | 2.98 | 10 |
| 2023-06-30 | 214.38 | 2.98 | 10 |
| 2023-07-28 | 215.61 | 1.70 | 10 |
| 2023-08-25 | 226.82 | 0.00 | 10 |
| 2023-09-29 | 226.13 | 0.00 | 10 |
| 2023-10-27 | 227.14 | 62.71 | 7 |
| 2023-11-24 | 238.16 | 18.77 | 9 |
| 2023-12-29 | 250.64 | 0.00 | 10 |
| 2024-01-25 | 254.57 | 0.00 | 11 |
| 2024-02-23 | 255.62 | 5.10 | 11 |
| 2024-03-28 | 238.89 | 5.86 | 10 |
| 2024-04-26 | 244.60 | 0.00 | 10 |
| 2024-05-31 | 238.86 | 32.93 | 9 |
| 2024-06-28 | 236.86 | 7.01 | 10 |
| 2024-07-26 | 258.88 | 49.86 | 8 |
| 2024-08-30 | 259.59 | 4.06 | 10 |
| 2024-09-27 | 257.21 | 4.83 | 10 |
| 2024-10-25 | 243.37 | 23.27 | 10 |
| 2024-11-29 | 237.53 | 0.00 | 11 |
| 2024-12-27 | 232.01 | 69.57 | 7 |
| 2025-01-31 | 206.20 | 109.56 | 5 |
| 2025-02-28 | 188.28 | 29.86 | 9 |
| 2025-03-28 | 202.69 | 25.72 | 9 |
| 2025-04-25 | 221.57 | 0.08 | 10 |
| 2025-05-30 | 215.61 | 20.11 | 9 |
| 2025-06-27 | 233.73 | 0.00 | 10 |
| 2025-07-25 | 226.28 | 0.00 | 10 |
| 2025-08-29 | 221.51 | 28.59 | 8 |
| 2025-09-26 | 214.02 | 25.35 | 9 |
| 2025-10-31 | 209.62 | 0.00 | 11 |
| 2025-11-28 | 194.57 | 11.96 | 10 |
| 2025-12-26 | 183.21 | 0.00 | 11 |
| 2026-01-30 | 170.97 | 23.09 | 9 |
| 2026-02-27 | 177.75 | 47.13 | 8 |
| 2026-03-27 | 168.53 | 39.85 | 8 |
| 2026-04-30 | 185.03 | 5.71 | 10 |
| 2026-05-29 | 184.74 | 0.00 | 11 |
| 2026-06-25 | 181.99 | 0.00 | 11 |
| 2026-07-31 | 180.24 | 0.00 | 11 |
| 2026-08-28 | 186.07 | 0.00 | 11 |
| 2026-09-22 | 181.37 | 0.00 | 11 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| AVTNPL | 2026-08-24 | 87.80 | 98.26 | 62.04 | +11.9% |
| CRAFTSMAN | 2026-05-11 | 9,039.50 | 10,602.00 | 10,380.65 | +17.3% |
| GANESHHOU | 2026-07-13 | 860.50 | 736.80 | 712.60 | -14.4% |
| HARITASEAT | 2021-02-01 | 532.00 | 766.55 | 676.59 | +44.1% |
| INDORAMA | 2026-09-21 | 91.50 | 103.57 | 76.48 | +13.2% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| NRBBEARING | 2026-09-21 | 531.10 | 520.50 | 430.82 | -2.0% |
| PRABHAT | 2021-03-08 | 88.95 | 99.60 | 82.70 | +12.0% |
| SAMBHV | 2026-09-21 | 151.10 | 151.94 | 116.85 | +0.6% |
| SHOPERSTOP | 2026-09-21 | 398.60 | 392.50 | 351.39 | -1.5% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| VINYLINDIA | 2020-05-18 | 62.55 | 2020-07-27 | 84.55 | +35.2% |
| MANGCHEFER | 2020-05-11 | 33.75 | 2020-07-31 | 33.73 | -0.1% |
| PANACEABIO | 2020-06-15 | 230.00 | 2020-08-20 | 184.01 | -20.0% |
| ZENTEC | 2020-08-03 | 58.80 | 2020-08-31 | 80.56 | +37.0% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| LSIL | 2020-05-18 | 0.65 | 2020-09-08 | 0.74 | +13.8% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| TIPSINDLTD | 2020-09-07 | 23.19 | 2020-09-22 | 22.08 | -4.8% |
| CYBERTECH | 2020-09-14 | 60.50 | 2020-09-22 | 55.13 | -8.9% |
| SASTASUNDR | 2020-08-24 | 107.00 | 2020-10-28 | 83.12 | -22.3% |
| ALEMBICLTD | 2020-06-22 | 81.65 | 2020-11-02 | 91.41 | +12.0% |
| ADVENZYMES | 2020-05-18 | 159.95 | 2020-11-03 | 292.33 | +82.8% |
| VIDHIING | 2020-09-28 | 111.70 | 2020-12-02 | 115.50 | +3.4% |
| TEXMOPIPES | 2020-11-02 | 16.30 | 2020-12-21 | 18.83 | +15.5% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| TCI | 2020-09-14 | 242.00 | 2020-12-22 | 234.75 | -3.0% |
| M100 | 2020-11-09 | 19.00 | 2020-12-22 | 19.58 | +3.1% |
| MANGCHEFER | 2020-12-07 | 40.75 | 2020-12-22 | 37.95 | -6.9% |
| NAHARPOLY | 2020-12-28 | 97.00 | 2021-01-11 | 85.70 | -11.6% |
| GOLDIAM | 2020-12-28 | 43.40 | 2021-01-15 | 42.26 | -2.6% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| TERASOFT | 2020-12-28 | 51.25 | 2021-01-27 | 44.32 | -13.5% |
| SPLIL | 2021-01-18 | 44.80 | 2021-02-11 | 39.50 | -11.8% |
| MTNL | 2020-12-28 | 14.10 | 2021-02-16 | 12.06 | -14.5% |
| JINDWORLD | 2020-11-09 | 50.00 | 2021-03-01 | 52.12 | +4.2% |
| MAHINDCIE | 2021-02-22 | 188.00 | 2021-03-19 | 158.46 | -15.7% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| NDGL | 2020-08-03 | 551.05 | 2021-04-12 | 682.63 | +23.9% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| ELGIRUBCO | 2021-02-01 | 30.75 | 2021-04-16 | 26.11 | -15.1% |
| NAHARCAP | 2021-03-22 | 111.80 | 2021-04-19 | 91.40 | -18.2% |
| MCL | 2021-04-19 | 91.20 | 2021-07-12 | 79.28 | -13.1% |
| DPWIRES | 2021-01-18 | 119.00 | 2021-07-20 | 175.56 | +47.5% |
| WELINV | 2021-04-19 | 423.00 | 2021-07-29 | 424.65 | +0.4% |
| SWANENERGY | 2021-08-02 | 149.45 | 2021-08-04 | 131.29 | -12.2% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| SANDESH | 2021-07-19 | 932.00 | 2021-08-11 | 853.69 | -8.4% |
| KANORICHEM | 2020-09-28 | 38.50 | 2021-08-20 | 143.54 | +272.8% |
| MSPL | 2021-04-19 | 10.75 | 2021-08-24 | 9.04 | -15.9% |
| MAHESHWARI | 2021-08-09 | 130.00 | 2021-08-25 | 91.85 | -29.3% |
| SAKSOFT | 2021-08-23 | 798.90 | 2021-10-20 | 1,002.30 | +25.5% |
| XCHANGING | 2021-07-26 | 132.00 | 2021-10-25 | 100.32 | -24.0% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| HIRECT | 2021-08-30 | 92.55 | 2021-11-18 | 85.00 | -8.2% |
| SHOPERSTOP | 2021-10-25 | 326.00 | 2021-11-22 | 335.82 | +3.0% |
| TTKPRESTIG | 2021-11-01 | 11,040.00 | 2021-11-26 | 10,070.05 | -8.8% |
| NBIFIN | 2021-08-23 | 2,845.00 | 2021-11-29 | 2,108.17 | -25.9% |
| 21STCENMGM | 2021-03-30 | 14.20 | 2021-12-03 | 54.10 | +281.0% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| MBLINFRA | 2021-12-06 | 33.00 | 2021-12-20 | 27.42 | -16.9% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| UNIVPHOTO | 2021-12-06 | 687.00 | 2021-12-29 | 675.55 | -1.7% |
| TVTODAY | 2021-11-22 | 320.24 | 2022-01-24 | 311.68 | -2.7% |
| BIL | 2021-12-20 | 273.80 | 2022-01-24 | 284.42 | +3.9% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| ALPA | 2021-04-26 | 67.40 | 2022-02-14 | 77.08 | +14.4% |
| PIONEEREMB | 2022-01-03 | 64.55 | 2022-02-14 | 53.58 | -17.0% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| DHUNINV | 2021-02-15 | 294.00 | 2022-02-22 | 614.90 | +109.1% |
| PRESSMN | 2022-01-31 | 47.80 | 2022-03-22 | 41.85 | -12.4% |
| EMAMIREAL | 2021-12-27 | 96.80 | 2022-03-29 | 60.84 | -37.1% |
| KAMATHOTEL | 2022-03-28 | 71.45 | 2022-05-10 | 72.91 | +2.0% |
| DENORA | 2021-12-06 | 490.00 | 2022-06-07 | 647.13 | +32.1% |
| ADVANIHOTR | 2022-02-21 | 101.85 | 2022-06-09 | 64.65 | -36.5% |
| MRPL | 2022-06-13 | 116.65 | 2022-07-06 | 69.61 | -40.3% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| TCPLPACK | 2022-02-21 | 748.70 | 2022-09-16 | 1,207.26 | +61.2% |
| DBCORP | 2022-09-19 | 138.00 | 2022-09-26 | 114.42 | -17.1% |
| PREMEXPLN | 2022-01-31 | 299.00 | 2022-09-27 | 426.50 | +42.6% |
| APOLSINHOT | 2022-10-03 | 1,249.00 | 2022-11-15 | 1,343.06 | +7.5% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| MRO-TEK | 2022-05-16 | 57.00 | 2022-12-22 | 56.49 | -0.9% |
| IRFC | 2022-11-21 | 27.50 | 2022-12-23 | 28.20 | +2.5% |
| NECLIFE | 2022-12-26 | 28.40 | 2023-01-17 | 21.74 | -23.5% |
| CREST | 2022-12-26 | 197.80 | 2023-01-27 | 176.79 | -10.6% |
| INDBANK | 2022-12-26 | 30.20 | 2023-02-02 | 25.44 | -15.8% |
| LSIL | 2023-01-30 | 23.20 | 2023-02-07 | 20.04 | -13.6% |
| DHUNINV | 2022-09-12 | 699.75 | 2023-02-13 | 628.21 | -10.2% |
| SPECIALITY | 2023-01-23 | 276.85 | 2023-02-14 | 221.73 | -19.9% |
| CGCL | 2022-02-28 | 597.90 | 2023-02-17 | 704.95 | +17.9% |
| MANAKSTEEL | 2023-02-06 | 48.20 | 2023-02-27 | 41.23 | -14.5% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| UNIENTER | 2023-02-13 | 179.30 | 2023-03-27 | 138.28 | -22.9% |
| LINC | 2023-02-20 | 550.00 | 2023-03-28 | 475.14 | -13.6% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| CIGNITITEC | 2023-02-20 | 731.95 | 2023-03-29 | 705.14 | -3.7% |
| FOSECOIND | 2023-03-06 | 2,310.00 | 2023-03-31 | 2,222.91 | -3.8% |
| ANURAS | 2023-04-03 | 868.95 | 2023-07-03 | 1,007.67 | +16.0% |
| ANMOL | 2023-04-03 | 183.65 | 2023-07-18 | 218.88 | +19.2% |
| GANESHHOUC | 2023-07-24 | 457.00 | 2023-08-14 | 418.62 | -8.4% |
| INGERRAND | 2023-04-03 | 2,690.00 | 2023-09-13 | 3,022.99 | +12.4% |
| ALANKIT | 2023-07-10 | 10.20 | 2023-10-23 | 10.31 | +1.1% |
| SUVEN | 2023-09-18 | 76.25 | 2023-10-23 | 66.97 | -12.2% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| TEXMOPIPES | 2023-08-21 | 78.35 | 2023-11-20 | 68.88 | -12.1% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| CONTROLPR | 2023-04-03 | 521.00 | 2024-02-06 | 884.21 | +69.7% |
| GEEKAYWIRE | 2023-03-27 | 40.98 | 2024-03-06 | 48.29 | +17.9% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| BALAXI | 2024-02-12 | 126.00 | 2024-03-06 | 101.86 | -19.2% |
| GOACARBON | 2024-01-23 | 731.40 | 2024-03-12 | 742.64 | +1.5% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| DHUNINV | 2023-11-28 | 1,309.00 | 2024-03-13 | 1,118.91 | -14.5% |
| DOLLAR | 2024-03-11 | 527.95 | 2024-03-13 | 461.65 | -12.6% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| HERCULES | 2024-03-18 | 517.70 | 2024-04-15 | 500.03 | -3.4% |
| JUSTDIAL | 2024-04-22 | 1,084.00 | 2024-05-09 | 1,008.00 | -7.0% |
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| SMSPHARMA | 2024-03-18 | 189.20 | 2024-06-04 | 181.36 | -4.1% |
| GRPLTD | 2024-05-13 | 7,884.20 | 2024-06-04 | 8,103.50 | +2.8% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| MATRIMONY | 2024-06-10 | 643.50 | 2024-07-23 | 564.77 | -12.2% |
| BHAGCHEM | 2024-06-10 | 238.99 | 2024-08-05 | 333.45 | +39.5% |
| NAHARINDUS | 2024-07-29 | 157.45 | 2024-08-05 | 146.39 | -7.0% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| SPORTKING | 2024-07-29 | 1,299.00 | 2024-09-13 | 1,358.45 | +4.6% |
| DLINKINDIA | 2024-05-21 | 415.85 | 2024-10-04 | 589.05 | +41.6% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| ARROWGREEN | 2024-08-12 | 853.00 | 2024-10-07 | 723.58 | -15.2% |
| HERANBA | 2024-08-19 | 467.00 | 2024-10-07 | 451.30 | -3.4% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| MAANALU | 2024-10-07 | 180.00 | 2024-11-05 | 193.14 | +7.3% |
| SRHHYPOLTD | 2024-10-14 | 893.10 | 2024-11-13 | 647.47 | -27.5% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| KIRLPNU | 2024-11-04 | 1,698.00 | 2024-12-23 | 1,596.00 | -6.0% |
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
| MPSLTD | 2025-02-24 | 2,648.95 | 2025-02-25 | 2,360.51 | -10.9% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| MBAPL | 2025-01-27 | 58.20 | 2025-03-27 | 53.39 | -8.3% |
| TAJGVK | 2025-02-24 | 440.40 | 2025-04-02 | 453.34 | +2.9% |
| APOLLO | 2025-02-03 | 126.50 | 2025-04-07 | 112.29 | -11.2% |
| TCPLPACK | 2025-02-24 | 3,997.25 | 2025-04-07 | 4,002.68 | +0.1% |
| ROHLTD | 2025-04-07 | 341.50 | 2025-04-30 | 366.23 | +7.2% |
| GRMOVER | 2025-03-10 | 252.00 | 2025-05-07 | 290.80 | +15.4% |
| VADILALIND | 2025-04-15 | 5,898.90 | 2025-05-30 | 5,401.40 | -8.4% |
| PARAS | 2025-05-05 | 1,372.20 | 2025-07-04 | 1,417.98 | +3.3% |
| SINDHUTRAD | 2025-07-07 | 36.89 | 2025-07-30 | 27.56 | -25.3% |
| KPRMILL | 2025-05-12 | 1,302.00 | 2025-08-01 | 1,108.74 | -14.8% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| PUNJABCHEM | 2025-08-04 | 1,403.00 | 2025-08-18 | 1,208.88 | -13.8% |
| HIRECT | 2025-08-04 | 961.85 | 2025-08-21 | 842.13 | -12.4% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| SPMLINFRA | 2025-04-15 | 213.00 | 2025-09-26 | 252.27 | +18.4% |
| IPL | 2025-06-02 | 207.95 | 2025-10-14 | 197.80 | -4.9% |
| VASCONEQ | 2025-09-22 | 64.00 | 2025-10-14 | 62.70 | -2.0% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| GANDHITUBE | 2025-09-01 | 865.00 | 2025-10-16 | 871.15 | +0.7% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| ORIENTTECH | 2025-10-20 | 454.90 | 2025-11-11 | 399.91 | -12.1% |
| GUJTHEM | 2025-10-20 | 432.05 | 2025-11-19 | 422.75 | -2.2% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| RISHABH | 2025-08-25 | 424.25 | 2025-12-08 | 383.85 | -9.5% |
| PGIL | 2025-11-17 | 844.05 | 2025-12-09 | 765.71 | -9.3% |
| VLSFINANCE | 2025-12-01 | 311.80 | 2025-12-16 | 276.07 | -11.5% |
| NACLIND | 2025-04-07 | 128.14 | 2025-12-17 | 164.20 | +28.1% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| SEQUENT | 2025-11-24 | 240.37 | 2026-01-12 | 195.04 | -18.9% |
| ASIANTILES | 2025-12-22 | 72.69 | 2026-01-12 | 70.21 | -3.4% |
| KICL | 2025-10-27 | 6,006.00 | 2026-01-19 | 4,607.98 | -23.3% |
| BHAGERIA | 2025-10-27 | 237.00 | 2026-01-20 | 160.92 | -32.1% |
| GMRAIRPORT | 2025-12-15 | 103.95 | 2026-01-23 | 92.10 | -11.4% |
| JAYBARMARU | 2026-01-27 | 84.25 | 2026-01-28 | 85.51 | +1.5% |
| NITCO | 2026-01-19 | 89.00 | 2026-02-19 | 75.12 | -15.6% |
| INFOBEAN | 2025-12-15 | 696.70 | 2026-02-27 | 770.07 | +10.5% |
| APEX | 2025-12-22 | 288.50 | 2026-02-27 | 389.22 | +34.9% |
| KIRIINDUS | 2026-01-19 | 530.30 | 2026-03-02 | 427.56 | -19.4% |
| RBA | 2026-01-27 | 64.07 | 2026-03-12 | 61.08 | -4.7% |
| HINDCOPPER | 2026-02-02 | 590.15 | 2026-03-12 | 528.63 | -10.4% |
| AYMSYNTEX | 2026-03-02 | 197.99 | 2026-03-12 | 174.33 | -12.0% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-02 | 116.20 | 2026-03-23 | 110.67 | -4.8% |
| AGIIL | 2026-01-12 | 295.60 | 2026-03-30 | 271.80 | -8.1% |
| KSB | 2026-03-02 | 738.00 | 2026-05-04 | 917.42 | +24.3% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| BAJAJHIND | 2026-03-30 | 16.42 | 2026-05-14 | 17.96 | +9.4% |
| EXPLEOSOL | 2026-05-18 | 903.95 | 2026-06-10 | 799.25 | -11.6% |
| CIEINDIA | 2025-10-20 | 432.50 | 2026-06-11 | 429.88 | -0.6% |
| SEAMECLTD | 2026-04-06 | 1,525.00 | 2026-06-17 | 1,398.40 | -8.3% |
| PRECWIRE | 2026-03-09 | 328.00 | 2026-07-07 | 376.20 | +14.7% |
| SASKEN | 2026-05-18 | 1,680.10 | 2026-07-08 | 1,933.72 | +15.1% |
| SPAL | 2026-06-22 | 1,030.00 | 2026-07-16 | 1,027.62 | -0.2% |
| JUSTDIAL | 2026-07-20 | 766.00 | 2026-08-18 | 658.64 | -14.0% |
| ABB | 2026-03-16 | 6,400.00 | 2026-09-15 | 7,158.25 | +11.8% |
| APCOTEXIND | 2026-05-11 | 528.95 | 2026-09-15 | 576.75 | +9.0% |
| MUNJALAU | 2026-07-13 | 100.50 | 2026-09-15 | 104.60 | +4.1% |
| PANAMAPET | 2026-06-15 | 384.80 | 2026-09-16 | 440.87 | +14.6% |
| CLSEL | 2026-06-15 | 297.00 | 2026-09-16 | 274.60 | -7.5% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_MCAP1250.csv` beside this report (32245 events in all).*

```
2020-04-13  DEEPAKNTR   BUY ₹10.00 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.81× weekly, month 2.50×, ladder rising; stop ₹241.64; charges ₹0.0118)
2020-04-27  CADILAHC    BUY ₹10.01 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 5.13×, ladder rising; stop ₹310.03; charges ₹0.0119)
2020-04-27  SYNGENE     BUY ₹10.02 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.37× weekly, month 1.94×, ladder rising; stop ₹285.95; charges ₹0.0119)
2020-04-27  TAJGVK      BUY ₹10.01 at ₹133.40 (fresh Friday signal — BUY: 6.67× weekly, month 2.22×, ladder rising; stop ₹106.49; charges ₹0.0119)
2020-05-11  APLLTD      BUY ₹9.98 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.72× weekly, month 6.13×, ladder rising; stop ₹694.45; charges ₹0.0118)
2020-05-11  IOLCP       BUY ₹9.98 at ₹66.18 (fresh Friday signal — BUY: 2.24× weekly, month 2.69×, ladder rising; stop ₹51.22; charges ₹0.0118)
2020-05-11  MANGCHEFER  BUY ₹9.98 at ₹33.75 (fresh Friday signal — BUY: surged 2.89× weekly on 2020-04-30 (month 2.29×), ladder rising NOW — promoted from the ladder watch; stop ₹29.50; charges ₹0.0118)
2020-05-18  ADVENZYMES  BUY ₹9.40 at ₹159.95 (fresh Friday signal — ACCUMULATE: 3.14× weekly, month 1.99×, ladder rising; stop ₹126.20; charges ₹0.0111)
2020-05-18  LSIL        BUY ₹10.42 at ₹0.65 (fresh Friday signal — BUY: 5.29× weekly, month 1.92×, ladder rising; stop ₹0.38; charges ₹0.0123)
2020-05-18  VINYLINDIA  BUY ₹10.20 at ₹62.55 (fresh Friday signal — ACCUMULATE: 13.29× weekly, month 10.04×, ladder rising; stop ₹52.87; charges ₹0.0121)
2020-06-12  DEEPAKNTR   SELL ₹9.97 at stop ₹474.05 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-06-15  PANACEABIO  BUY ₹9.97 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.25×, ladder rising; stop ₹114.11; charges ₹0.0118)
2020-06-16  IOLCP       SELL ₹10.43 at stop ₹69.35 (+4.8%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2020-06-22  ALEMBICLTD  BUY ₹10.43 at ₹81.65 (fresh Friday signal — BUY: 11.73× weekly, month 8.47×, ladder rising; stop ₹44.84; charges ₹0.0124)
2020-07-27  VINYLINDIA  SELL ₹13.76 at stop ₹84.55 (+35.2%, charges ₹0.0143) — the cash goes back to work at the next Friday screen
2020-07-31  MANGCHEFER  SELL ₹9.95 at stop ₹33.73 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-08-03  NDGL        BUY ₹13.01 at ₹551.05 (fresh Friday signal — BUY: 32.96× weekly, month 9.69×, ladder rising; stop ₹408.60; charges ₹0.0154)
2020-08-03  ZENTEC      BUY ₹10.70 at ₹58.80 (fresh Friday signal — ACCUMULATE: 4.33× weekly, month 4.89×, ladder rising; stop ₹42.67; charges ₹0.0127)
2020-08-20  PANACEABIO  SELL ₹7.96 at stop ₹184.01 (-20.0%, charges ₹0.0083) — the cash goes back to work at the next Friday screen
2020-08-24  SASTASUNDR  BUY ₹7.96 at ₹107.00 (fresh Friday signal — ACCUMULATE: 11.14× weekly, month 4.01×, ladder rising; stop ₹75.74; charges ₹0.0094)
2020-08-31  ZENTEC      SELL ₹14.63 at stop ₹80.56 (+37.0%, charges ₹0.0152) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.93 at stop ₹928.62 (+19.9%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹12.27 at ₹1,398.95 (fresh Friday signal — BUY: 5.23× weekly, month 3.88×, ladder rising; stop ₹1,211.25; charges ₹0.0145)
2020-09-07  TIPSINDLTD  BUY ₹12.21 at ₹23.19 (fresh Friday signal — BUY: 6.28× weekly, month 4.00×, ladder rising; stop ₹16.01; charges ₹0.0145)
2020-09-08  CADILAHC    SELL ₹11.04 at stop ₹364.99 (+10.5%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-08  LSIL        SELL ₹11.83 at stop ₹0.74 (+13.8%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2020-09-14  CYBERTECH   BUY ₹11.96 at ₹60.50 (fresh Friday signal — BUY: 6.47× weekly, month 5.69×, ladder rising; stop ₹43.46; charges ₹0.0142)
2020-09-14  TCI         BUY ₹12.99 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.71× weekly, month 3.76×, ladder rising; stop ₹190.07; charges ₹0.0154)
2020-09-22  CYBERTECH   SELL ₹10.87 at stop ₹55.13 (-8.9%, charges ₹0.0113) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹9.47 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-22  TIPSINDLTD  SELL ₹11.60 at stop ₹22.08 (-4.8%, charges ₹0.0120) — the cash goes back to work at the next Friday screen
2020-09-28  KANORICHEM  BUY ₹6.75 at ₹38.50 (fresh Friday signal — ACCUMULATE: 4.08× weekly, month 1.54×, ladder rising; stop ₹30.91; charges ₹0.0080)
2020-09-28  SAKSOFT     BUY ₹12.61 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.34×, ladder rising; stop ₹303.81; charges ₹0.0149)
2020-09-28  VIDHIING    BUY ₹12.58 at ₹111.70 (fresh Friday signal — BUY: 4.70× weekly, month 4.47×, ladder rising; stop ₹77.90; charges ₹0.0149)
2020-10-28  SASTASUNDR  SELL ₹6.17 at stop ₹83.12 (-22.3%, charges ₹0.0064) — the cash goes back to work at the next Friday screen
2020-11-02  ALEMBICLTD  SELL ₹11.66 at stop ₹91.41 (+12.0%, charges ₹0.0121) — the cash goes back to work at the next Friday screen
2020-11-02  TEXMOPIPES  BUY ₹6.17 at ₹16.30 (fresh Friday signal — ACCUMULATE: 4.01× weekly, month 2.60×, ladder rising; stop ₹12.54; charges ₹0.0073)
2020-11-03  ADVENZYMES  SELL ₹17.14 at stop ₹292.33 (+82.8%, charges ₹0.0178) — the cash goes back to work at the next Friday screen
2020-11-09  JINDWORLD   BUY ₹12.15 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.34× weekly, month 1.54×, ladder rising; stop ₹39.81; charges ₹0.0144)
2020-11-09  M100        BUY ₹12.17 at ₹19.00 (fresh Friday signal — ACCUMULATE: 7.21× weekly, month 1.52×, ladder rising; stop ₹16.34; charges ₹0.0144)
2020-12-02  VIDHIING    SELL ₹12.98 at stop ₹115.50 (+3.4%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2020-12-07  MANGCHEFER  BUY ₹13.19 at ₹40.75 (fresh Friday signal — BUY: 11.07× weekly, month 3.88×, ladder rising; stop ₹30.21; charges ₹0.0156)
2020-12-21  TEXMOPIPES  SELL ₹7.11 at stop ₹18.83 (+15.5%, charges ₹0.0074) — the cash goes back to work at the next Friday screen
2020-12-22  M100        SELL ₹12.51 at stop ₹19.58 (+3.1%, charges ₹0.0130) — the cash goes back to work at the next Friday screen
2020-12-22  MANGCHEFER  SELL ₹12.25 at stop ₹37.95 (-6.9%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹12.57 at stop ₹234.75 (-3.0%, charges ₹0.0130) — the cash goes back to work at the next Friday screen
2020-12-28  GOLDIAM     BUY ₹12.92 at ₹43.40 (fresh Friday signal — BUY: 7.27× weekly, month 2.65×, ladder rising; stop ₹35.32; charges ₹0.0153)
2020-12-28  MTNL        BUY ₹12.89 at ₹14.10 (fresh Friday signal — BUY: 9.99× weekly, month 4.75×, ladder rising; stop ₹8.26; charges ₹0.0153)
2020-12-28  NAHARPOLY   BUY ₹12.86 at ₹97.00 (fresh Friday signal — BUY: 7.67× weekly, month 3.92×, ladder rising; stop ₹67.74; charges ₹0.0152)
2020-12-28  PAISALO     BUY ₹12.83 at ₹56.99 (fresh Friday signal — BUY: 32.49× weekly, month 7.40×, ladder rising; stop ₹33.56; charges ₹0.0152)
2020-12-28  TERASOFT    BUY ₹12.95 at ₹51.25 (fresh Friday signal — BUY: 13.80× weekly, month 7.51×, ladder rising; stop ₹25.77; charges ₹0.0153)
2021-01-11  NAHARPOLY   SELL ₹11.34 at stop ₹85.70 (-11.6%, charges ₹0.0118) — the cash goes back to work at the next Friday screen
2021-01-15  GOLDIAM     SELL ₹12.55 at stop ₹42.26 (-2.6%, charges ₹0.0130) — the cash goes back to work at the next Friday screen
2021-01-18  DPWIRES     BUY ₹13.27 at ₹119.00 (fresh Friday signal — BUY: 39.11× weekly, month 14.01×, ladder rising; stop ₹71.03; charges ₹0.0157)
2021-01-18  SPLIL       BUY ₹12.52 at ₹44.80 (fresh Friday signal — BUY: 15.25× weekly, month 6.40×, ladder rising; stop ₹26.32; charges ₹0.0148)
2021-01-25  SAKSOFT     SELL ₹10.77 at stop ₹341.10 (-14.4%, charges ₹0.0112) — the cash goes back to work at the next Friday screen
2021-01-27  TERASOFT    SELL ₹11.17 at stop ₹44.32 (-13.5%, charges ₹0.0116) — the cash goes back to work at the next Friday screen
2021-02-01  ELGIRUBCO   BUY ₹12.75 at ₹30.75 (fresh Friday signal — BUY: 7.89× weekly, month 8.56×, ladder rising; stop ₹18.27; charges ₹0.0151)
2021-02-01  HARITASEAT  BUY ₹9.19 at ₹532.00 (fresh Friday signal — BUY: 5.70× weekly, month 8.57×, ladder rising; stop ₹438.90; charges ₹0.0109)
2021-02-11  SPLIL       SELL ₹11.02 at stop ₹39.50 (-11.8%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2021-02-15  DHUNINV     BUY ₹11.02 at ₹294.00 (fresh Friday signal — BUY: 24.10× weekly, month 3.95×, ladder rising; stop ₹224.82; charges ₹0.0131)
2021-02-16  MTNL        SELL ₹11.00 at stop ₹12.06 (-14.5%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2021-02-22  MAHINDCIE   BUY ₹11.00 at ₹188.00 (fresh Friday signal — BUY: 22.74× weekly, month 4.25×, ladder rising; stop ₹143.79; charges ₹0.0130)
2021-03-01  JINDWORLD   SELL ₹12.64 at stop ₹52.12 (+4.2%, charges ₹0.0131) — the cash goes back to work at the next Friday screen
2021-03-08  PRABHAT     BUY ₹12.64 at ₹88.95 (fresh Friday signal — BUY: 14.34× weekly, month 4.59×, ladder rising; stop ₹64.98; charges ₹0.0150)
2021-03-19  MAHINDCIE   SELL ₹9.25 at stop ₹158.46 (-15.7%, charges ₹0.0096) — the cash goes back to work at the next Friday screen
2021-03-22  NAHARCAP    BUY ₹9.25 at ₹111.80 (fresh Friday signal — BUY: 8.15× weekly, month 7.42×, ladder rising; stop ₹86.78; charges ₹0.0110)
2021-03-25  BANARISUG   SELL ₹13.89 at stop ₹1,586.36 (+13.4%, charges ₹0.0144) — the cash goes back to work at the next Friday screen
2021-03-30  21STCENMGM  BUY ₹12.73 at ₹14.20 (fresh Friday signal — BUY: 6.71× weekly, month 2.46×, ladder rising; stop ₹11.02; charges ₹0.0151)
2021-04-01  21STCENMGM  TRIM 1.5% (₹0.18 at ₹13.70) to pay the tax bill
2021-04-01  DHUNINV     TRIM 1.5% (₹0.15 at ₹272.05) to pay the tax bill
2021-04-01  DPWIRES     TRIM 1.5% (₹0.18 at ₹105.80) to pay the tax bill
2021-04-01  ELGIRUBCO   TRIM 1.5% (₹0.17 at ₹27.20) to pay the tax bill
2021-04-01  HARITASEAT  TRIM 1.5% (₹0.19 at ₹735.45) to pay the tax bill
2021-04-01  KANORICHEM  TRIM 1.5% (₹0.16 at ₹59.70) to pay the tax bill
2021-04-01  NAHARCAP    TRIM 1.5% (₹0.14 at ₹109.25) to pay the tax bill
2021-04-01  NDGL        TRIM 1.5% (₹0.27 at ₹750.20) to pay the tax bill
2021-04-01  PAISALO     TRIM 1.5% (₹0.26 at ₹78.11) to pay the tax bill
2021-04-01  PRABHAT     TRIM 1.5% (₹0.21 at ₹97.00) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹3.0685 paid (STCG ₹15.34 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-12  NDGL        SELL ₹15.84 at stop ₹682.63 (+23.9%, charges ₹0.0164) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹16.02 at stop ₹72.41 (+27.1%, charges ₹0.0166) — the cash goes back to work at the next Friday screen
2021-04-16  ELGIRUBCO   SELL ₹10.64 at stop ₹26.11 (-15.1%, charges ₹0.0110) — the cash goes back to work at the next Friday screen
2021-04-19  MCL         BUY ₹11.94 at ₹91.20 (fresh Friday signal — ACCUMULATE: 5.03× weekly, month 3.15×, ladder rising; stop ₹78.30; charges ₹0.0142)
2021-04-19  MOREPENLAB  BUY ₹6.79 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.06×, ladder rising; stop ₹28.01; charges ₹0.0080)
2021-04-19  MSPL        BUY ₹11.84 at ₹10.75 (fresh Friday signal — BUY: 2.56× weekly, month 2.27×, ladder rising; stop ₹5.85; charges ₹0.0140)
2021-04-19  NAHARCAP    SELL ₹7.43 at stop ₹91.40 (-18.2%, charges ₹0.0077) — the cash goes back to work at the next Friday screen
2021-04-19  WELINV      BUY ₹11.93 at ₹423.00 (fresh Friday signal — ACCUMULATE: 2.91× weekly, month 2.30×, ladder rising; stop ₹332.58; charges ₹0.0141)
2021-04-26  ALPA        BUY ₹7.43 at ₹67.40 (fresh Friday signal — BUY: 9.87× weekly, month 4.10×, ladder rising; stop ₹39.03; charges ₹0.0088)
2021-07-12  MCL         SELL ₹10.36 at stop ₹79.28 (-13.1%, charges ₹0.0107) — the cash goes back to work at the next Friday screen
2021-07-19  SANDESH     BUY ₹10.36 at ₹932.00 (fresh Friday signal — BUY: 16.72× weekly, month 5.11×, ladder rising; stop ₹726.85; charges ₹0.0123)
2021-07-20  DPWIRES     SELL ₹19.24 at stop ₹175.56 (+47.5%, charges ₹0.0200) — the cash goes back to work at the next Friday screen
2021-07-26  XCHANGING   BUY ₹17.28 at ₹132.00 (fresh Friday signal — BUY: 14.79× weekly, month 9.49×, ladder rising; stop ₹72.24; charges ₹0.0205)
2021-07-29  WELINV      SELL ₹11.95 at stop ₹424.65 (+0.4%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2021-08-02  SWANENERGY  BUY ₹13.91 at ₹149.45 (fresh Friday signal — BUY: 17.17× weekly, month 4.67×, ladder rising; stop ₹131.29; charges ₹0.0165)
2021-08-04  SWANENERGY  SELL ₹12.19 at stop ₹131.29 (-12.2%, charges ₹0.0126) — the cash goes back to work at the next Friday screen
2021-08-09  MAHESHWARI  BUY ₹12.19 at ₹130.00 (fresh Friday signal — BUY: 13.73× weekly, month 2.95×, ladder rising; stop ₹91.85; charges ₹0.0144)
2021-08-10  MOREPENLAB  SELL ₹10.18 at stop ₹56.33 (+50.4%, charges ₹0.0106) — the cash goes back to work at the next Friday screen
2021-08-11  SANDESH     SELL ₹9.47 at stop ₹853.69 (-8.4%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹16.43 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.42×, ladder rising; stop ₹2,675.86; charges ₹0.0195)
2021-08-20  KANORICHEM  SELL ₹24.72 at stop ₹143.54 (+272.8%, charges ₹0.0256) — the cash goes back to work at the next Friday screen
2021-08-23  NBIFIN      BUY ₹12.30 at ₹2,845.00 (fresh Friday signal — ACCUMULATE: 3.56× weekly, month 3.63×, ladder rising; stop ₹2,108.17; charges ₹0.0146)
2021-08-23  SAKSOFT     BUY ₹15.63 at ₹798.90 (fresh Friday signal — BUY: 4.51× weekly, month 1.59×, ladder rising; stop ₹601.49; charges ₹0.0185)
2021-08-24  MSPL        SELL ₹9.94 at stop ₹9.04 (-15.9%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2021-08-25  MAHESHWARI  SELL ₹8.59 at stop ₹91.85 (-29.3%, charges ₹0.0089) — the cash goes back to work at the next Friday screen
2021-08-30  HIRECT      BUY ₹16.31 at ₹92.55 (fresh Friday signal — BUY: 8.36× weekly, month 3.07×, ladder rising; stop ₹68.64; charges ₹0.0193)
2021-10-20  SAKSOFT     SELL ₹19.57 at stop ₹1,002.30 (+25.5%, charges ₹0.0203) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹14.35 at stop ₹3,220.59 (-12.5%, charges ₹0.0149) — the cash goes back to work at the next Friday screen
2021-10-25  SHOPERSTOP  BUY ₹17.40 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹0.0206)
2021-10-25  XCHANGING   SELL ₹13.10 at stop ₹100.32 (-24.0%, charges ₹0.0136) — the cash goes back to work at the next Friday screen
2021-11-01  TCIEXP      BUY ₹13.55 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0161)
2021-11-01  TTKPRESTIG  BUY ₹18.29 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.0217)
2021-11-18  HIRECT      SELL ₹14.94 at stop ₹85.00 (-8.2%, charges ₹0.0155) — the cash goes back to work at the next Friday screen
2021-11-22  SHOPERSTOP  SELL ₹17.88 at stop ₹335.82 (+3.0%, charges ₹0.0186) — the cash goes back to work at the next Friday screen
2021-11-22  TVTODAY     BUY ₹14.94 at ₹320.24 (fresh Friday signal — BUY: 15.58× weekly, month 3.55×, ladder rising; stop ₹253.08; charges ₹0.0177)
2021-11-26  TTKPRESTIG  SELL ₹16.65 at stop ₹10,070.05 (-8.8%, charges ₹0.0173) — the cash goes back to work at the next Friday screen
2021-11-29  NBIFIN      SELL ₹9.10 at stop ₹2,108.17 (-25.9%, charges ₹0.0094) — the cash goes back to work at the next Friday screen
2021-11-29  RAYMOND     BUY ₹16.33 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0193)
2021-11-29  RSYSTEMS    BUY ₹18.20 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0216)
2021-12-03  21STCENMGM  SELL ₹47.65 at stop ₹54.10 (+281.0%, charges ₹0.0494) — the cash goes back to work at the next Friday screen
2021-12-06  DENORA      BUY ₹18.01 at ₹490.00 (fresh Friday signal — BUY: 12.65× weekly, month 2.85×, ladder rising; stop ₹330.38; charges ₹0.0213)
2021-12-06  MBLINFRA    BUY ₹17.92 at ₹33.00 (fresh Friday signal — BUY: 15.92× weekly, month 4.06×, ladder rising; stop ₹17.32; charges ₹0.0212)
2021-12-06  UNIVPHOTO   BUY ₹17.94 at ₹687.00 (fresh Friday signal — BUY: 6.38× weekly, month 2.65×, ladder rising; stop ₹378.29; charges ₹0.0213)
2021-12-16  RSYSTEMS    SELL ₹16.28 at stop ₹291.18 (-10.4%, charges ₹0.0169) — the cash goes back to work at the next Friday screen
2021-12-20  BIL         BUY ₹17.41 at ₹273.80 (fresh Friday signal — BUY: 30.84× weekly, month 7.22×, ladder rising; stop ₹167.10; charges ₹0.0206)
2021-12-20  MBLINFRA    SELL ₹14.86 at stop ₹27.42 (-16.9%, charges ₹0.0154) — the cash goes back to work at the next Friday screen
2021-12-21  TCIEXP      SELL ₹15.06 at stop ₹2,039.74 (+11.4%, charges ₹0.0156) — the cash goes back to work at the next Friday screen
2021-12-27  EMAMIREAL   BUY ₹17.55 at ₹96.80 (fresh Friday signal — BUY: 7.16× weekly, month 2.84×, ladder rising; stop ₹60.84; charges ₹0.0208)
2021-12-27  SWANENERGY  BUY ₹14.11 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0167)
2021-12-29  UNIVPHOTO   SELL ₹17.61 at stop ₹675.55 (-1.7%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2022-01-03  PIONEEREMB  BUY ₹17.61 at ₹64.55 (fresh Friday signal — BUY: 4.66× weekly, month 1.62×, ladder rising; stop ₹53.58; charges ₹0.0209)
2022-01-24  BIL         SELL ₹18.05 at stop ₹284.42 (+3.9%, charges ₹0.0187) — the cash goes back to work at the next Friday screen
2022-01-24  TVTODAY     SELL ₹14.51 at stop ₹311.68 (-2.7%, charges ₹0.0151) — the cash goes back to work at the next Friday screen
2022-01-25  SWANENERGY  SELL ₹15.28 at stop ₹162.64 (+8.5%, charges ₹0.0158) — the cash goes back to work at the next Friday screen
2022-01-31  PREMEXPLN   BUY ₹11.69 at ₹299.00 (fresh Friday signal — BUY: 4.43× weekly, month 1.92×, ladder rising; stop ₹223.25; charges ₹0.0139)
2022-01-31  PRESSMN     BUY ₹18.07 at ₹47.80 (fresh Friday signal — BUY: 13.67× weekly, month 5.92×, ladder rising; stop ₹30.59; charges ₹0.0214)
2022-01-31  SHARDACROP  BUY ₹18.08 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0214)
2022-02-11  SHARDACROP  SELL ₹16.77 at stop ₹545.30 (-7.1%, charges ₹0.0174) — the cash goes back to work at the next Friday screen
2022-02-14  ALPA        SELL ₹8.48 at stop ₹77.08 (+14.4%, charges ₹0.0088) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹16.77 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0199)
2022-02-14  PIONEEREMB  SELL ₹14.58 at stop ₹53.58 (-17.0%, charges ₹0.0151) — the cash goes back to work at the next Friday screen
2022-02-15  RAYMOND     SELL ₹18.57 at stop ₹679.35 (+14.0%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2022-02-21  ADVANIHOTR  BUY ₹16.85 at ₹101.85 (fresh Friday signal — ACCUMULATE: 8.91× weekly, month 7.66×, ladder rising; stop ₹64.65; charges ₹0.0200)
2022-02-21  TCPLPACK    BUY ₹16.72 at ₹748.70 (fresh Friday signal — BUY: 6.12× weekly, month 3.47×, ladder rising; stop ₹480.00; charges ₹0.0198)
2022-02-22  DHUNINV     SELL ₹22.65 at stop ₹614.90 (+109.1%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2022-02-28  CGCL        BUY ₹16.82 at ₹597.90 (fresh Friday signal — ACCUMULATE: 2.99× weekly, month 3.16×, ladder rising; stop ₹536.75; charges ₹0.0199)
2022-02-28  DANGEE      BUY ₹13.88 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0164)
2022-03-22  PRESSMN     SELL ₹15.78 at stop ₹41.85 (-12.4%, charges ₹0.0164) — the cash goes back to work at the next Friday screen
2022-03-28  KAMATHOTEL  BUY ₹15.78 at ₹71.45 (fresh Friday signal — BUY: 3.56× weekly, month 2.29×, ladder rising; stop ₹44.72; charges ₹0.0187)
2022-03-29  EMAMIREAL   SELL ₹11.01 at stop ₹60.84 (-37.1%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹8.8443 paid (STCG ₹36.83 @20%, LTCG ₹11.83 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-05-10  KAMATHOTEL  SELL ₹16.07 at stop ₹72.91 (+2.0%, charges ₹0.0167) — the cash goes back to work at the next Friday screen
2022-05-16  MRO-TEK     BUY ₹18.23 at ₹57.00 (fresh Friday signal — ACCUMULATE: 2.51× weekly, month 5.06×, ladder rising; stop ₹49.34; charges ₹0.0216)
2022-06-07  DENORA      SELL ₹23.73 at stop ₹647.13 (+32.1%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2022-06-09  ADVANIHOTR  SELL ₹10.67 at stop ₹64.65 (-36.5%, charges ₹0.0111) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹19.49 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0231)
2022-06-13  MRPL        BUY ₹14.91 at ₹116.65 (fresh Friday signal — BUY: 3.64× weekly, month 4.35×, ladder rising; stop ₹69.61; charges ₹0.0177)
2022-07-06  MRPL        SELL ₹8.88 at stop ₹69.61 (-40.3%, charges ₹0.0092) — the cash goes back to work at the next Friday screen
2022-09-06  DANGEE      SELL ₹22.12 at stop ₹375.25 (+59.7%, charges ₹0.0229) — the cash goes back to work at the next Friday screen
2022-09-12  DHUNINV     BUY ₹22.24 at ₹699.75 (fresh Friday signal — BUY: 21.10× weekly, month 1.76×, ladder rising; stop ₹558.65; charges ₹0.0264)
2022-09-16  TCPLPACK    SELL ₹26.91 at stop ₹1,207.26 (+61.2%, charges ₹0.0279) — the cash goes back to work at the next Friday screen
2022-09-19  DBCORP      BUY ₹13.69 at ₹138.00 (fresh Friday signal — BUY: 15.57× weekly, month 10.93×, ladder rising; stop ₹94.19; charges ₹0.0162)
2022-09-19  JSWHL       BUY ₹21.96 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0260)
2022-09-26  DBCORP      SELL ₹11.33 at stop ₹114.42 (-17.1%, charges ₹0.0118) — the cash goes back to work at the next Friday screen
2022-09-27  PREMEXPLN   SELL ₹16.64 at stop ₹426.50 (+42.6%, charges ₹0.0173) — the cash goes back to work at the next Friday screen
2022-10-03  APOLSINHOT  BUY ₹20.75 at ₹1,249.00 (fresh Friday signal — BUY: 13.10× weekly, month 3.98×, ladder rising; stop ₹794.34; charges ₹0.0246)
2022-11-15  APOLSINHOT  SELL ₹22.26 at stop ₹1,343.06 (+7.5%, charges ₹0.0231) — the cash goes back to work at the next Friday screen
2022-11-21  IRFC        BUY ₹21.84 at ₹27.50 (fresh Friday signal — BUY: 16.56× weekly, month 6.85×, ladder rising; stop ₹23.09; charges ₹0.0259)
2022-12-21  ELECON      SELL ₹32.15 at stop ₹202.49 (+65.3%, charges ₹0.0334) — the cash goes back to work at the next Friday screen
2022-12-22  MRO-TEK     SELL ₹18.03 at stop ₹56.49 (-0.9%, charges ₹0.0187) — the cash goes back to work at the next Friday screen
2022-12-23  IRFC        SELL ₹22.35 at stop ₹28.20 (+2.5%, charges ₹0.0232) — the cash goes back to work at the next Friday screen
2022-12-26  CREST       BUY ₹21.05 at ₹197.80 (fresh Friday signal — BUY: 6.59× weekly, month 1.51×, ladder rising; stop ₹172.47; charges ₹0.0249)
2022-12-26  INDBANK     BUY ₹16.84 at ₹30.20 (fresh Friday signal — BUY: surged 20.51× weekly on 2022-12-16 (month 12.63×), ladder rising NOW — promoted from the ladder watch; stop ₹24.29; charges ₹0.0200)
2022-12-26  KRISHANA    BUY ₹21.01 at ₹83.60 (fresh Friday signal — BUY: 3.61× weekly, month 2.28×, ladder rising; stop ₹75.36; charges ₹0.0249)
2022-12-26  NECLIFE     BUY ₹21.27 at ₹28.40 (fresh Friday signal — BUY: 14.66× weekly, month 2.32×, ladder rising; stop ₹20.28; charges ₹0.0252)
2023-01-17  NECLIFE     SELL ₹16.24 at stop ₹21.74 (-23.5%, charges ₹0.0169) — the cash goes back to work at the next Friday screen
2023-01-23  SPECIALITY  BUY ₹16.24 at ₹276.85 (fresh Friday signal — BUY: 6.65× weekly, month 2.62×, ladder rising; stop ₹221.73; charges ₹0.0192)
2023-01-27  CREST       SELL ₹18.77 at stop ₹176.79 (-10.6%, charges ₹0.0195) — the cash goes back to work at the next Friday screen
2023-01-30  LSIL        BUY ₹18.77 at ₹23.20 (fresh Friday signal — BUY: 2.27× weekly, month 3.60×, ladder rising; stop ₹11.29; charges ₹0.0222)
2023-02-02  INDBANK     SELL ₹14.16 at stop ₹25.44 (-15.8%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2023-02-06  MANAKSTEEL  BUY ₹14.16 at ₹48.20 (fresh Friday signal — ACCUMULATE: 3.72× weekly, month 4.50×, ladder rising; stop ₹41.23; charges ₹0.0168)
2023-02-07  LSIL        SELL ₹16.18 at stop ₹20.04 (-13.6%, charges ₹0.0168) — the cash goes back to work at the next Friday screen
2023-02-13  DHUNINV     SELL ₹19.93 at stop ₹628.21 (-10.2%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2023-02-13  UNIENTER    BUY ₹16.18 at ₹179.30 (fresh Friday signal — BUY: 19.11× weekly, month 5.40×, ladder rising; stop ₹119.20; charges ₹0.0192)
2023-02-14  SPECIALITY  SELL ₹12.98 at stop ₹221.73 (-19.9%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2023-02-17  CGCL        SELL ₹19.79 at stop ₹704.95 (+17.9%, charges ₹0.0205) — the cash goes back to work at the next Friday screen
2023-02-20  CIGNITITEC  BUY ₹14.47 at ₹731.95 (fresh Friday signal — BUY: 2.02× weekly, month 1.77×, ladder rising; stop ₹568.10; charges ₹0.0171)
2023-02-20  LINC        BUY ₹19.06 at ₹550.00 (fresh Friday signal — BUY: 2.23× weekly, month 3.07×, ladder rising; stop ₹452.72; charges ₹0.0226)
2023-02-20  TIIL        BUY ₹19.17 at ₹1,116.70 (fresh Friday signal — BUY: 8.50× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0227)
2023-02-27  MANAKSTEEL  SELL ₹12.08 at stop ₹41.23 (-14.5%, charges ₹0.0125) — the cash goes back to work at the next Friday screen
2023-03-06  FOSECOIND   BUY ₹12.08 at ₹2,310.00 (fresh Friday signal — BUY: 13.30× weekly, month 1.88×, ladder rising; stop ₹1,867.03; charges ₹0.0143)
2023-03-20  KRISHANA    SELL ₹23.67 at stop ₹94.40 (+12.9%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2023-03-27  GEEKAYWIRE  BUY ₹18.30 at ₹40.98 (fresh Friday signal — BUY: 2.59× weekly, month 3.64×, ladder rising; stop ₹30.40; charges ₹0.0217)
2023-03-27  UNIENTER    SELL ₹12.45 at stop ₹138.28 (-22.9%, charges ₹0.0129) — the cash goes back to work at the next Friday screen
2023-03-28  LINC        SELL ₹16.43 at stop ₹475.14 (-13.6%, charges ₹0.0170) — the cash goes back to work at the next Friday screen
2023-03-29  CIGNITITEC  SELL ₹13.91 at stop ₹705.14 (-3.7%, charges ₹0.0144) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹36.15 at stop ₹112.36 (+116.1%, charges ₹0.0375) — the cash goes back to work at the next Friday screen
2023-03-31  FOSECOIND   SELL ₹11.60 at stop ₹2,222.91 (-3.8%, charges ₹0.0120) — the cash goes back to work at the next Friday screen
2023-04-03  ANMOL       BUY ₹17.73 at ₹183.65 (fresh Friday signal — BUY: surged 8.07× weekly on 2023-03-03 (month 3.18×), ladder rising NOW — promoted from the ladder watch; stop ₹157.04; charges ₹0.0210)
2023-04-03  ANURAS      BUY ₹17.79 at ₹868.95 (fresh Friday signal — BUY: surged 2.13× weekly on 2023-03-10 (month 1.83×), ladder rising NOW — promoted from the ladder watch; stop ₹691.46; charges ₹0.0211)
2023-04-03  CONTROLPR   BUY ₹17.77 at ₹521.00 (fresh Friday signal — ACCUMULATE: 2.94× weekly, month 2.01×, ladder rising; stop ₹439.28; charges ₹0.0211)
2023-04-03  HAL         BUY ₹17.76 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.04×, ladder rising; stop ₹1,171.71; charges ₹0.0210)
2023-04-03  INGERRAND   BUY ₹17.80 at ₹2,690.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2023-03-10 (month 1.53×), ladder rising NOW — promoted from the ladder watch; stop ₹2,170.84; charges ₹0.0211)
2023-04-03  TAX         FY2023 settled: ₹4.0776 paid (STCG ₹8.24 @20%, LTCG ₹19.44 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-07-03  ANURAS      SELL ₹20.58 at stop ₹1,007.67 (+16.0%, charges ₹0.0213) — the cash goes back to work at the next Friday screen
2023-07-10  ALANKIT     BUY ₹21.40 at ₹10.20 (fresh Friday signal — BUY: 17.11× weekly, month 4.17×, ladder rising; stop ₹6.52; charges ₹0.0254)
2023-07-18  ANMOL       SELL ₹21.08 at stop ₹218.88 (+19.2%, charges ₹0.0219) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹21.55 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.91×, ladder rising; stop ₹359.10; charges ₹0.0255)
2023-08-14  GANESHHOUC  SELL ₹19.70 at stop ₹418.62 (-8.4%, charges ₹0.0204) — the cash goes back to work at the next Friday screen
2023-08-21  TEXMOPIPES  BUY ₹21.39 at ₹78.35 (fresh Friday signal — BUY: 14.27× weekly, month 4.58×, ladder rising; stop ₹49.82; charges ₹0.0253)
2023-09-13  INGERRAND   SELL ₹19.96 at stop ₹3,022.99 (+12.4%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2023-09-18  SUVEN       BUY ₹19.96 at ₹76.25 (fresh Friday signal — BUY: 10.57× weekly, month 4.60×, ladder rising; stop ₹57.05; charges ₹0.0236)
2023-10-23  ALANKIT     SELL ₹21.58 at stop ₹10.31 (+1.1%, charges ₹0.0224) — the cash goes back to work at the next Friday screen
2023-10-23  SUVEN       SELL ₹17.49 at stop ₹66.97 (-12.2%, charges ₹0.0181) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹23.64 at stop ₹1,840.70 (+33.4%, charges ₹0.0245) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹17.44 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0207)
2023-10-30  KKCL        BUY ₹22.64 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.93×, ladder rising; stop ₹674.12; charges ₹0.0268)
2023-10-30  SHAREINDIA  BUY ₹22.63 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.63×, ladder rising; stop ₹261.25; charges ₹0.0268)
2023-11-20  TEXMOPIPES  SELL ₹18.77 at stop ₹68.88 (-12.1%, charges ₹0.0195) — the cash goes back to work at the next Friday screen
2023-11-28  DHUNINV     BUY ₹18.77 at ₹1,309.00 (fresh Friday signal — BUY: 12.16× weekly, month 5.91×, ladder rising; stop ₹764.13; charges ₹0.0222)
2024-01-17  TIIL        SELL ₹40.04 at stop ₹2,337.00 (+109.3%, charges ₹0.0415) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹24.56 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0291)
2024-01-23  GOACARBON   BUY ₹15.48 at ₹731.40 (fresh Friday signal — BUY: 16.67× weekly, month 5.69×, ladder rising; stop ₹532.86; charges ₹0.0183)
2024-02-06  CONTROLPR   SELL ₹30.10 at stop ₹884.21 (+69.7%, charges ₹0.0312) — the cash goes back to work at the next Friday screen
2024-02-12  BALAXI      BUY ₹25.00 at ₹126.00 (fresh Friday signal — BUY: 19.83× weekly, month 5.34×, ladder rising; stop ₹79.07; charges ₹0.0296)
2024-03-06  BALAXI      SELL ₹20.16 at stop ₹101.86 (-19.2%, charges ₹0.0209) — the cash goes back to work at the next Friday screen
2024-03-06  GEEKAYWIRE  SELL ₹21.52 at stop ₹48.29 (+17.9%, charges ₹0.0223) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹26.88 at stop ₹357.20 (+19.1%, charges ₹0.0279) — the cash goes back to work at the next Friday screen
2024-03-11  DOLLAR      BUY ₹24.21 at ₹527.95 (fresh Friday signal — BUY: 4.55× weekly, month 2.48×, ladder rising; stop ₹461.65; charges ₹0.0287)
2024-03-11  SILINV      BUY ₹24.30 at ₹551.20 (fresh Friday signal — BUY: 10.53× weekly, month 4.88×, ladder rising; stop ₹421.85; charges ₹0.0288)
2024-03-11  SOLARINDS   BUY ₹24.16 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0286)
2024-03-12  GOACARBON   SELL ₹15.68 at stop ₹742.64 (+1.5%, charges ₹0.0163) — the cash goes back to work at the next Friday screen
2024-03-13  DHUNINV     SELL ₹16.00 at stop ₹1,118.91 (-14.5%, charges ₹0.0166) — the cash goes back to work at the next Friday screen
2024-03-13  DOLLAR      SELL ₹21.13 at stop ₹461.65 (-12.6%, charges ₹0.0219) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹19.99 at stop ₹674.12 (-11.5%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹24.61 at stop ₹666.47 (+0.5%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2024-03-18  FORCEMOT    BUY ₹23.12 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.51×, ladder rising; stop ₹5,500.61; charges ₹0.0274)
2024-03-18  HERCULES    BUY ₹23.12 at ₹517.70 (fresh Friday signal — BUY: 7.76× weekly, month 3.01×, ladder rising; stop ₹376.18; charges ₹0.0274)
2024-03-18  INDIGO      BUY ₹23.09 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0274)
2024-03-18  SMSPHARMA   BUY ₹23.22 at ₹189.20 (fresh Friday signal — ACCUMULATE: 1.84× weekly, month 7.08×, ladder rising; stop ₹146.81; charges ₹0.0275)
2024-04-01  CUPID       TRIM 0.6% (₹0.15 at ₹186.62) to pay the tax bill
2024-04-01  FORCEMOT    TRIM 0.6% (₹0.15 at ₹7,540.95) to pay the tax bill
2024-04-01  HARITASEAT  TRIM 0.6% (₹0.07 at ₹766.55) to pay the tax bill
2024-04-01  HERCULES    TRIM 0.6% (₹0.13 at ₹530.60) to pay the tax bill
2024-04-01  INDIGO      TRIM 0.6% (₹0.14 at ₹3,548.95) to pay the tax bill
2024-04-01  JSWHL       TRIM 0.6% (₹0.19 at ₹7,225.05) to pay the tax bill
2024-04-01  PRABHAT     TRIM 0.6% (₹0.08 at ₹99.60) to pay the tax bill
2024-04-01  SILINV      TRIM 0.6% (₹0.12 at ₹506.00) to pay the tax bill
2024-04-01  SMSPHARMA   TRIM 0.6% (₹0.13 at ₹186.05) to pay the tax bill
2024-04-01  SOLARINDS   TRIM 0.6% (₹0.15 at ₹8,726.05) to pay the tax bill
2024-04-01  TAX         FY2024 settled: ₹7.1701 paid (STCG ₹35.85 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-15  HERCULES    SELL ₹22.15 at stop ₹500.03 (-3.4%, charges ₹0.0230) — the cash goes back to work at the next Friday screen
2024-04-22  JUSTDIAL    BUY ₹22.15 at ₹1,084.00 (fresh Friday signal — BUY: 11.71× weekly, month 3.19×, ladder rising; stop ₹821.08; charges ₹0.0262)
2024-05-09  JUSTDIAL    SELL ₹20.56 at stop ₹1,008.00 (-7.0%, charges ₹0.0213) — the cash goes back to work at the next Friday screen
2024-05-13  GRPLTD      BUY ₹20.56 at ₹7,884.20 (fresh Friday signal — BUY: 16.40× weekly, month 3.05×, ladder rising; stop ₹6,175.00; charges ₹0.0244)
2024-05-13  JSWHL       SELL ₹29.12 at stop ₹6,280.45 (+33.6%, charges ₹0.0302) — the cash goes back to work at the next Friday screen
2024-05-21  DLINKINDIA  BUY ₹24.42 at ₹415.85 (fresh Friday signal — BUY: 21.84× weekly, month 3.73×, ladder rising; stop ₹292.50; charges ₹0.0289)
2024-05-28  FORCEMOT    SELL ₹28.24 at stop ₹8,083.64 (+23.1%, charges ₹0.0293) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹24.10 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0286)
2024-06-04  GRPLTD      SELL ₹21.08 at stop ₹8,103.50 (+2.8%, charges ₹0.0219) — the cash goes back to work at the next Friday screen
2024-06-04  SMSPHARMA   SELL ₹22.09 at stop ₹181.36 (-4.1%, charges ₹0.0229) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹25.30 at stop ₹7,980.95 (+5.5%, charges ₹0.0262) — the cash goes back to work at the next Friday screen
2024-06-10  BHAGCHEM    BUY ₹23.36 at ₹238.99 (fresh Friday signal — BUY: 8.45× weekly, month 2.68×, ladder rising; stop ₹175.70; charges ₹0.0277)
2024-06-10  FIEMIND     BUY ₹23.43 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0278)
2024-06-10  MATRIMONY   BUY ₹23.50 at ₹643.50 (fresh Friday signal — BUY: 5.35× weekly, month 1.60×, ladder rising; stop ₹496.18; charges ₹0.0278)
2024-07-23  FIEMIND     SELL ₹22.27 at stop ₹1,257.56 (-4.7%, charges ₹0.0231) — the cash goes back to work at the next Friday screen
2024-07-23  MATRIMONY   SELL ₹20.58 at stop ₹564.77 (-12.2%, charges ₹0.0213) — the cash goes back to work at the next Friday screen
2024-07-29  NAHARINDUS  BUY ₹23.99 at ₹157.45 (fresh Friday signal — BUY: 11.88× weekly, month 3.04×, ladder rising; stop ₹124.68; charges ₹0.0284)
2024-07-29  SPORTKING   BUY ₹25.87 at ₹1,299.00 (fresh Friday signal — BUY: 15.26× weekly, month 8.80×, ladder rising; stop ₹817.24; charges ₹0.0306)
2024-08-05  BHAGCHEM    SELL ₹32.52 at stop ₹333.45 (+39.5%, charges ₹0.0337) — the cash goes back to work at the next Friday screen
2024-08-05  NAHARINDUS  SELL ₹22.26 at stop ₹146.39 (-7.0%, charges ₹0.0231) — the cash goes back to work at the next Friday screen
2024-08-12  ARROWGREEN  BUY ₹24.74 at ₹853.00 (fresh Friday signal — BUY: 6.29× weekly, month 3.90×, ladder rising; stop ₹603.20; charges ₹0.0293)
2024-08-12  OSWALAGRO   BUY ₹24.58 at ₹60.80 (fresh Friday signal — BUY: 16.74× weekly, month 2.15×, ladder rising; stop ₹42.18; charges ₹0.0291)
2024-08-16  CAMPUS      SELL ₹23.29 at stop ₹277.07 (-3.1%, charges ₹0.0242) — the cash goes back to work at the next Friday screen
2024-08-19  HERANBA     BUY ₹24.70 at ₹467.00 (fresh Friday signal — BUY: 8.02× weekly, month 3.41×, ladder rising; stop ₹342.95; charges ₹0.0293)
2024-09-13  SPORTKING   SELL ₹26.99 at stop ₹1,358.45 (+4.6%, charges ₹0.0280) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹26.22 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0311)
2024-10-04  DLINKINDIA  SELL ₹34.52 at stop ₹589.05 (+41.6%, charges ₹0.0358) — the cash goes back to work at the next Friday screen
2024-10-07  ARROWGREEN  SELL ₹20.94 at stop ₹723.58 (-15.2%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹14.90 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0177)
2024-10-07  HERANBA     SELL ₹23.82 at stop ₹451.30 (-3.4%, charges ₹0.0247) — the cash goes back to work at the next Friday screen
2024-10-07  INDIGO      SELL ₹32.11 at stop ₹4,485.14 (+40.2%, charges ₹0.0333) — the cash goes back to work at the next Friday screen
2024-10-07  MAANALU     BUY ₹24.44 at ₹180.00 (fresh Friday signal — BUY: 18.92× weekly, month 4.26×, ladder rising; stop ₹126.35; charges ₹0.0290)
2024-10-14  DBCORP      BUY ₹25.14 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0298)
2024-10-14  SKIPPER     BUY ₹24.94 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0295)
2024-10-14  SRHHYPOLTD  BUY ₹25.04 at ₹893.10 (fresh Friday signal — BUY: 3.73× weekly, month 8.71×, ladder rising; stop ₹647.47; charges ₹0.0297)
2024-10-25  DBCORP      SELL ₹21.52 at stop ₹302.08 (-14.2%, charges ₹0.0223) — the cash goes back to work at the next Friday screen
2024-10-28  CUPID       SELL ₹22.69 at stop ₹158.66 (+31.1%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2024-11-04  AKZOINDIA   BUY ₹24.24 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.0572)
2024-11-04  KIRLPNU     BUY ₹21.72 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.0513)
2024-11-05  MAANALU     SELL ₹26.14 at stop ₹193.14 (+7.3%, charges ₹0.0581) — the cash goes back to work at the next Friday screen
2024-11-11  SIYSIL      BUY ₹23.46 at ₹701.85 (fresh Friday signal — BUY: 10.52× weekly, month 5.04×, ladder rising; stop ₹439.76; charges ₹0.0554)
2024-11-13  SRHHYPOLTD  SELL ₹18.09 at stop ₹647.47 (-27.5%, charges ₹0.0402) — the cash goes back to work at the next Friday screen
2024-11-14  ASTRAZEN    SELL ₹13.68 at stop ₹6,854.77 (-7.9%, charges ₹0.0304) — the cash goes back to work at the next Friday screen
2024-11-18  SASKEN      BUY ₹22.65 at ₹2,015.25 (fresh Friday signal — BUY: 9.07× weekly, month 2.15×, ladder rising; stop ₹1,640.65; charges ₹0.0535)
2024-11-18  VHL         BUY ₹11.80 at ₹5,080.00 (fresh Friday signal — BUY: 6.85× weekly, month 5.05×, ladder rising; stop ₹3,556.30; charges ₹0.0278)
2024-12-23  KIRLPNU     SELL ₹20.32 at stop ₹1,596.00 (-6.0%, charges ₹0.0451) — the cash goes back to work at the next Friday screen
2024-12-26  PRSMJOHNSN  SELL ₹20.78 at stop ₹170.55 (-20.5%, charges ₹0.0462) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹18.28 at stop ₹3,423.18 (-24.2%, charges ₹0.0406) — the cash goes back to work at the next Friday screen
2024-12-27  VHL         SELL ₹10.19 at stop ₹4,408.00 (-13.2%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹23.04 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.0544)
2024-12-30  KFINTECH    BUY ₹22.96 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.0542)
2024-12-30  NACLIND     BUY ₹23.06 at ₹67.60 (fresh Friday signal — BUY: 1.75× weekly, month 2.31×, ladder rising; stop ₹53.45; charges ₹0.0544)
2025-01-10  SKIPPER     SELL ₹21.45 at stop ₹477.28 (-13.7%, charges ₹0.0476) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹21.96 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0518)
2025-01-15  KFINTECH    SELL ₹17.53 at stop ₹1,159.14 (-23.3%, charges ₹0.0389) — the cash goes back to work at the next Friday screen
2025-01-20  ZOTA        BUY ₹17.53 at ₹1,016.45 (fresh Friday signal — ACCUMULATE: 3.76× weekly, month 3.93×, ladder rising; stop ₹863.60; charges ₹0.0414)
2025-01-21  SASKEN      SELL ₹22.30 at stop ₹1,993.24 (-1.1%, charges ₹0.0495) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹18.34 at stop ₹700.36 (-16.1%, charges ₹0.0407) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹20.27 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0478)
2025-01-27  MBAPL       BUY ₹20.38 at ₹58.20 (fresh Friday signal — ACCUMULATE: 3.22× weekly, month 3.87×, ladder rising; stop ₹50.92; charges ₹0.0481)
2025-01-27  NACLIND     SELL ₹20.81 at stop ₹61.28 (-9.3%, charges ₹0.0462) — the cash goes back to work at the next Friday screen
2025-01-27  OSWALAGRO   SELL ₹24.34 at stop ₹60.42 (-0.6%, charges ₹0.0541) — the cash goes back to work at the next Friday screen
2025-01-27  SILINV      SELL ₹23.95 at stop ₹548.20 (-0.5%, charges ₹0.0532) — the cash goes back to work at the next Friday screen
2025-01-28  ZOTA        SELL ₹14.82 at stop ₹863.60 (-15.0%, charges ₹0.0329) — the cash goes back to work at the next Friday screen
2025-01-30  SIYSIL      SELL ₹25.63 at stop ₹770.45 (+9.8%, charges ₹0.0569) — the cash goes back to work at the next Friday screen
2025-02-03  APOLLO      BUY ₹20.44 at ₹126.50 (fresh Friday signal — ACCUMULATE: 1.55× weekly, month 3.75×, ladder rising; stop ₹98.89; charges ₹0.0483)
2025-02-03  ZENSARTECH  BUY ₹20.37 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.0481)
2025-02-12  JINDWORLD   SELL ₹21.05 at stop ₹374.11 (-8.2%, charges ₹0.0467) — the cash goes back to work at the next Friday screen
2025-02-24  GODFRYPHLP  BUY ₹19.24 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.0454)
2025-02-24  MPSLTD      BUY ₹19.17 at ₹2,648.95 (fresh Friday signal — BUY: surged 3.92× weekly on 2025-01-31 (month 3.29×), ladder rising NOW — promoted from the ladder watch; stop ₹2,360.51; charges ₹0.0453)
2025-02-24  TAJGVK      BUY ₹19.23 at ₹440.40 (fresh Friday signal — BUY: 2.16× weekly, month 2.07×, ladder rising; stop ₹349.09; charges ₹0.0454)
2025-02-24  TCPLPACK    BUY ₹19.30 at ₹3,997.25 (fresh Friday signal — BUY: 8.08× weekly, month 1.73×, ladder rising; stop ₹2,770.57; charges ₹0.0456)
2025-02-25  MPSLTD      SELL ₹17.01 at stop ₹2,360.51 (-10.9%, charges ₹0.0378) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹18.78 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0443)
2025-03-03  ZENSARTECH  SELL ₹15.58 at stop ₹727.84 (-23.1%, charges ₹0.0346) — the cash goes back to work at the next Friday screen
2025-03-10  GRMOVER     BUY ₹19.56 at ₹252.00 (fresh Friday signal — BUY: surged 3.52× weekly on 2025-02-07 (month 1.72×), ladder rising NOW — promoted from the ladder watch; stop ₹203.86; charges ₹0.0462)
2025-03-27  MBAPL       SELL ₹18.61 at stop ₹53.39 (-8.3%, charges ₹0.0413) — the cash goes back to work at the next Friday screen
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹13.97 / LT ₹0.00)
2025-04-02  TAJGVK      SELL ₹19.70 at stop ₹453.34 (+2.9%, charges ₹0.0438) — the cash goes back to work at the next Friday screen
2025-04-07  APOLLO      SELL ₹18.06 at stop ₹112.29 (-11.2%, charges ₹0.0401) — the cash goes back to work at the next Friday screen
2025-04-07  NACLIND     BUY ₹19.85 at ₹128.14 (fresh Friday signal — BUY: surged 9.31× weekly on 2025-03-21 (month 10.01×), ladder rising NOW — promoted from the ladder watch; stop ₹89.22; charges ₹0.0468)
2025-04-07  ROHLTD      BUY ₹19.73 at ₹341.50 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 1.60×, ladder rising; stop ₹359.48; charges ₹0.0466)
2025-04-07  TCPLPACK    SELL ₹19.24 at stop ₹4,002.68 (+0.1%, charges ₹0.0427) — the cash goes back to work at the next Friday screen
2025-04-15  SPMLINFRA   BUY ₹21.50 at ₹213.00 (fresh Friday signal — ACCUMULATE: 2.58× weekly, month 4.14×, ladder rising; stop ₹109.59; charges ₹0.0508)
2025-04-15  VADILALIND  BUY ₹21.57 at ₹5,898.90 (fresh Friday signal — ACCUMULATE: 2.22× weekly, month 6.18×, ladder rising; stop ₹4,500.03; charges ₹0.0509)
2025-04-30  ROHLTD      SELL ₹21.07 at stop ₹366.23 (+7.2%, charges ₹0.0468) — the cash goes back to work at the next Friday screen
2025-05-05  PARAS       BUY ₹21.14 at ₹1,372.20 (fresh Friday signal — BUY: 25.15× weekly, month 2.24×, ladder rising; stop ₹973.27; charges ₹0.0499)
2025-05-07  GRMOVER     SELL ₹22.47 at stop ₹290.80 (+15.4%, charges ₹0.0499) — the cash goes back to work at the next Friday screen
2025-05-12  KPRMILL     BUY ₹22.02 at ₹1,302.00 (fresh Friday signal — BUY: 15.89× weekly, month 3.16×, ladder rising; stop ₹938.50; charges ₹0.0520)
2025-05-30  VADILALIND  SELL ₹19.66 at stop ₹5,401.40 (-8.4%, charges ₹0.0437) — the cash goes back to work at the next Friday screen
2025-06-02  IPL         BUY ₹20.11 at ₹207.95 (fresh Friday signal — BUY: 11.52× weekly, month 2.94×, ladder rising; stop ₹126.73; charges ₹0.0475)
2025-07-04  PARAS       SELL ₹21.75 at stop ₹1,417.98 (+3.3%, charges ₹0.0483) — the cash goes back to work at the next Friday screen
2025-07-07  SINDHUTRAD  BUY ₹21.75 at ₹36.89 (fresh Friday signal — BUY: 7.60× weekly, month 3.46×, ladder rising; stop ₹22.20; charges ₹0.0513)
2025-07-30  SINDHUTRAD  SELL ₹16.17 at stop ₹27.56 (-25.3%, charges ₹0.0359) — the cash goes back to work at the next Friday screen
2025-08-01  KPRMILL     SELL ₹18.66 at stop ₹1,108.74 (-14.8%, charges ₹0.0415) — the cash goes back to work at the next Friday screen
2025-08-04  HIRECT      BUY ₹12.55 at ₹961.85 (fresh Friday signal — BUY: 12.48× weekly, month 5.91×, ladder rising; stop ₹615.65; charges ₹0.0296)
2025-08-04  NH          SELL ₹23.40 at stop ₹1,814.78 (+25.2%, charges ₹0.0520) — the cash goes back to work at the next Friday screen
2025-08-04  PUNJABCHEM  BUY ₹22.29 at ₹1,403.00 (fresh Friday signal — BUY: 43.22× weekly, month 9.53×, ladder rising; stop ₹1,208.88; charges ₹0.0526)
2025-08-11  RAIN        BUY ₹22.38 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.0528)
2025-08-18  PUNJABCHEM  SELL ₹19.11 at stop ₹1,208.88 (-13.8%, charges ₹0.0425) — the cash goes back to work at the next Friday screen
2025-08-21  HIRECT      SELL ₹10.94 at stop ₹842.13 (-12.4%, charges ₹0.0243) — the cash goes back to work at the next Friday screen
2025-08-25  RISHABH     BUY ₹22.44 at ₹424.25 (fresh Friday signal — BUY: 41.22× weekly, month 7.62×, ladder rising; stop ₹263.20; charges ₹0.0530)
2025-08-26  RAIN        SELL ₹19.97 at stop ₹143.64 (-10.4%, charges ₹0.0444) — the cash goes back to work at the next Friday screen
2025-09-01  GANDHITUBE  BUY ₹22.31 at ₹865.00 (fresh Friday signal — BUY: 9.32× weekly, month 5.18×, ladder rising; stop ₹709.84; charges ₹0.0527)
2025-09-16  GODFRYPHLP  SELL ₹29.71 at stop ₹8,967.50 (+55.1%, charges ₹0.0660) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹13.91 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.81× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.0328)
2025-09-22  VASCONEQ    BUY ₹22.08 at ₹64.00 (fresh Friday signal — BUY: 10.29× weekly, month 4.47×, ladder rising; stop ₹51.69; charges ₹0.0521)
2025-09-26  SPMLINFRA   SELL ₹25.35 at stop ₹252.27 (+18.4%, charges ₹0.0563) — the cash goes back to work at the next Friday screen
2025-09-29  SUBROS      BUY ₹21.74 at ₹1,132.00 (fresh Friday signal — BUY: 8.24× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0513)
2025-10-14  IPL         SELL ₹19.04 at stop ₹197.80 (-4.9%, charges ₹0.0423) — the cash goes back to work at the next Friday screen
2025-10-14  SUBROS      SELL ₹20.01 at stop ₹1,046.90 (-7.5%, charges ₹0.0445) — the cash goes back to work at the next Friday screen
2025-10-14  VASCONEQ    SELL ₹21.53 at stop ₹62.70 (-2.0%, charges ₹0.0478) — the cash goes back to work at the next Friday screen
2025-10-16  GANDHITUBE  SELL ₹22.37 at stop ₹871.15 (+0.7%, charges ₹0.0497) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹20.86 at ₹1,574.50 (fresh Friday signal — BUY: 13.09× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0492)
2025-10-20  CIEINDIA    BUY ₹20.89 at ₹432.50 (fresh Friday signal — ACCUMULATE: 5.25× weekly, month 2.01×, ladder rising; stop ₹377.39; charges ₹0.0493)
2025-10-20  CREDITACC   SELL ₹30.25 at stop ₹1,274.42 (+49.9%, charges ₹0.0672) — the cash goes back to work at the next Friday screen
2025-10-20  GUJTHEM     BUY ₹20.90 at ₹432.05 (fresh Friday signal — ACCUMULATE: 2.67× weekly, month 1.73×, ladder rising; stop ₹384.85; charges ₹0.0493)
2025-10-20  ORIENTTECH  BUY ₹20.99 at ₹454.90 (fresh Friday signal — ACCUMULATE: 1.80× weekly, month 4.13×, ladder rising; stop ₹399.91; charges ₹0.0496)
2025-10-27  BHAGERIA    BUY ₹21.03 at ₹237.00 (fresh Friday signal — BUY: 24.69× weekly, month 8.89×, ladder rising; stop ₹159.69; charges ₹0.0496)
2025-10-27  KICL        BUY ₹12.15 at ₹6,006.00 (fresh Friday signal — BUY: 7.09× weekly, month 2.03×, ladder rising; stop ₹4,575.39; charges ₹0.0287)
2025-11-06  FDC         SELL ₹12.05 at stop ₹425.79 (-13.0%, charges ₹0.0268) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹12.05 at ₹1,014.90 (fresh Friday signal — BUY: 23.91× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.0284)
2025-11-11  ORIENTTECH  SELL ₹18.37 at stop ₹399.91 (-12.1%, charges ₹0.0408) — the cash goes back to work at the next Friday screen
2025-11-17  PGIL        BUY ₹18.37 at ₹844.05 (fresh Friday signal — BUY: 19.68× weekly, month 3.52×, ladder rising; stop ₹612.56; charges ₹0.0434)
2025-11-19  GUJTHEM     SELL ₹20.35 at stop ₹422.75 (-2.2%, charges ₹0.0452) — the cash goes back to work at the next Friday screen
2025-11-20  ANANDRATHI  SELL ₹19.12 at stop ₹1,450.17 (-7.9%, charges ₹0.0425) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹11.54 at stop ₹976.41 (-3.8%, charges ₹0.0256) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹19.54 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0461)
2025-11-24  SEQUENT     BUY ₹19.51 at ₹240.37 (fresh Friday signal — BUY: 4.85× weekly, month 1.56×, ladder rising; stop ₹185.91; charges ₹0.0461)
2025-12-01  VLSFINANCE  BUY ₹11.96 at ₹311.80 (fresh Friday signal — ACCUMULATE: 7.01× weekly, month 5.08×, ladder rising; stop ₹276.07; charges ₹0.0282)
2025-12-08  RISHABH     SELL ₹20.21 at stop ₹383.85 (-9.5%, charges ₹0.0449) — the cash goes back to work at the next Friday screen
2025-12-09  PGIL        SELL ₹16.59 at stop ₹765.71 (-9.3%, charges ₹0.0368) — the cash goes back to work at the next Friday screen
2025-12-15  GMRAIRPORT  BUY ₹18.37 at ₹103.95 (fresh Friday signal — BUY: 1.56× weekly, month 2.58×, ladder rising; stop ₹89.73; charges ₹0.0434)
2025-12-15  INFOBEAN    BUY ₹18.21 at ₹696.70 (fresh Friday signal — ACCUMULATE: 3.25× weekly, month 2.25×, ladder rising; stop ₹586.67; charges ₹0.0430)
2025-12-16  VLSFINANCE  SELL ₹10.54 at stop ₹276.07 (-11.5%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2025-12-17  NACLIND     SELL ₹25.31 at stop ₹164.20 (+28.1%, charges ₹0.0562) — the cash goes back to work at the next Friday screen
2025-12-22  APEX        BUY ₹18.47 at ₹288.50 (fresh Friday signal — ACCUMULATE: 5.61× weekly, month 12.16×, ladder rising; stop ₹221.66; charges ₹0.0436)
2025-12-22  ASIANTILES  BUY ₹17.62 at ₹72.69 (fresh Friday signal — BUY: 4.41× weekly, month 1.60×, ladder rising; stop ₹53.03; charges ₹0.0416)
2026-01-09  RADICO      SELL ₹17.48 at stop ₹2,956.49 (-10.1%, charges ₹0.0388) — the cash goes back to work at the next Friday screen
2026-01-12  AGIIL       BUY ₹17.48 at ₹295.60 (fresh Friday signal — ACCUMULATE: 5.45× weekly, month 2.06×, ladder rising; stop ₹202.47; charges ₹0.0413)
2026-01-12  ASIANTILES  SELL ₹16.94 at stop ₹70.21 (-3.4%, charges ₹0.0376) — the cash goes back to work at the next Friday screen
2026-01-12  SEQUENT     SELL ₹15.76 at stop ₹195.04 (-18.9%, charges ₹0.0350) — the cash goes back to work at the next Friday screen
2026-01-19  KICL        SELL ₹9.28 at stop ₹4,607.98 (-23.3%, charges ₹0.0206) — the cash goes back to work at the next Friday screen
2026-01-19  KIRIINDUS   BUY ₹15.09 at ₹530.30 (fresh Friday signal — ACCUMULATE: 2.70× weekly, month 9.40×, ladder rising; stop ₹382.56; charges ₹0.0356)
2026-01-19  NITCO       BUY ₹17.61 at ₹89.00 (fresh Friday signal — ACCUMULATE: 5.88× weekly, month 2.19×, ladder rising; stop ₹75.12; charges ₹0.0416)
2026-01-20  BHAGERIA    SELL ₹14.21 at stop ₹160.92 (-32.1%, charges ₹0.0316) — the cash goes back to work at the next Friday screen
2026-01-23  GMRAIRPORT  SELL ₹16.20 at stop ₹92.10 (-11.4%, charges ₹0.0360) — the cash goes back to work at the next Friday screen
2026-01-27  JAYBARMARU  BUY ₹16.81 at ₹84.25 (fresh Friday signal — BUY: surged 4.48× weekly on 2026-01-02 (month 2.25×), ladder rising NOW — promoted from the ladder watch; stop ₹85.51; charges ₹0.0397)
2026-01-27  RBA         BUY ₹16.77 at ₹64.07 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.49×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.0396)
2026-01-28  JAYBARMARU  SELL ₹16.98 at stop ₹85.51 (+1.5%, charges ₹0.0377) — the cash goes back to work at the next Friday screen
2026-02-02  HINDCOPPER  BUY ₹17.09 at ₹590.15 (fresh Friday signal — BUY: 2.81× weekly, month 4.88×, ladder rising; stop ₹485.74; charges ₹0.0403)
2026-02-19  NITCO       SELL ₹14.80 at stop ₹75.12 (-15.6%, charges ₹0.0329) — the cash goes back to work at the next Friday screen
2026-02-23  VESUVIUS    BUY ₹18.50 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.56×, ladder rising; stop ₹464.31; charges ₹0.0437)
2026-02-27  APEX        SELL ₹24.80 at stop ₹389.22 (+34.9%, charges ₹0.0551) — the cash goes back to work at the next Friday screen
2026-02-27  INFOBEAN    SELL ₹20.03 at stop ₹770.07 (+10.5%, charges ₹0.0445) — the cash goes back to work at the next Friday screen
2026-03-02  AYMSYNTEX   BUY ₹11.69 at ₹197.99 (fresh Friday signal — BUY: 2.17× weekly, month 1.58×, ladder rising; stop ₹167.00; charges ₹0.0276)
2026-03-02  J&KBANK     BUY ₹17.72 at ₹116.20 (fresh Friday signal — BUY: 8.67× weekly, month 1.90×, ladder rising; stop ₹96.50; charges ₹0.0418)
2026-03-02  KIRIINDUS   SELL ₹12.11 at stop ₹427.56 (-19.4%, charges ₹0.0269) — the cash goes back to work at the next Friday screen
2026-03-02  KSB         BUY ₹17.72 at ₹738.00 (fresh Friday signal — BUY: 52.86× weekly, month 4.75×, ladder rising; stop ₹658.54; charges ₹0.0418)
2026-03-09  PRECWIRE    BUY ₹12.11 at ₹328.00 (fresh Friday signal — BUY: surged 8.31× weekly on 2026-02-20 (month 3.38×), ladder rising NOW — promoted from the ladder watch; stop ₹268.96; charges ₹0.0286)
2026-03-12  AYMSYNTEX   SELL ₹10.25 at stop ₹174.33 (-12.0%, charges ₹0.0228) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹15.24 at stop ₹528.63 (-10.4%, charges ₹0.0338) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹15.91 at stop ₹61.08 (-4.7%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2026-03-16  ABB         BUY ₹17.14 at ₹6,400.00 (fresh Friday signal — BUY: 1.80× weekly, month 1.91×, ladder rising; stop ₹5,486.25; charges ₹0.0405)
2026-03-16  JBCHEPHARM  BUY ₹17.18 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0406)
2026-03-23  J&KBANK     SELL ₹16.80 at stop ₹110.67 (-4.8%, charges ₹0.0373) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹15.98 at stop ₹464.31 (-13.2%, charges ₹0.0355) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹16.69 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0394)
2026-03-30  AGIIL       SELL ₹16.00 at stop ₹271.80 (-8.1%, charges ₹0.0355) — the cash goes back to work at the next Friday screen
2026-03-30  BAJAJHIND   BUY ₹16.61 at ₹16.42 (fresh Friday signal — ACCUMULATE: 2.06× weekly, month 1.79×, ladder rising; stop ₹13.87; charges ₹0.0392)
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹31.70 / LT ₹0.00)
2026-04-06  SEAMECLTD   BUY ₹16.85 at ₹1,525.00 (fresh Friday signal — BUY: 1.99× weekly, month 1.63×, ladder rising; stop ₹1,188.45; charges ₹0.0398)
2026-05-04  KSB         SELL ₹21.93 at stop ₹917.42 (+24.3%, charges ₹0.0487) — the cash goes back to work at the next Friday screen
2026-05-11  APCOTEXIND  BUY ₹9.58 at ₹528.95 (fresh Friday signal — BUY: 18.49× weekly, month 4.38×, ladder rising; stop ₹365.75; charges ₹0.0226)
2026-05-11  CRAFTSMAN   BUY ₹18.06 at ₹9,039.50 (fresh Friday signal — BUY: 22.97× weekly, month 3.93×, ladder rising; stop ₹7,119.77; charges ₹0.0426)
2026-05-14  AETHER      SELL ₹16.26 at stop ₹1,125.84 (-2.1%, charges ₹0.0361) — the cash goes back to work at the next Friday screen
2026-05-14  BAJAJHIND   SELL ₹18.08 at stop ₹17.96 (+9.4%, charges ₹0.0402) — the cash goes back to work at the next Friday screen
2026-05-18  EXPLEOSOL   BUY ₹17.05 at ₹903.95 (fresh Friday signal — BUY: 23.54× weekly, month 5.55×, ladder rising; stop ₹757.15; charges ₹0.0402)
2026-05-18  SASKEN      BUY ₹17.30 at ₹1,680.10 (fresh Friday signal — BUY: 74.07× weekly, month 16.58×, ladder rising; stop ₹1,161.09; charges ₹0.0408)
2026-06-10  EXPLEOSOL   SELL ₹15.00 at stop ₹799.25 (-11.6%, charges ₹0.0333) — the cash goes back to work at the next Friday screen
2026-06-11  CIEINDIA    SELL ₹20.66 at stop ₹429.88 (-0.6%, charges ₹0.0459) — the cash goes back to work at the next Friday screen
2026-06-15  CLSEL       BUY ₹17.55 at ₹297.00 (fresh Friday signal — ACCUMULATE: 27.01× weekly, month 6.47×, ladder rising; stop ₹238.93; charges ₹0.0414)
2026-06-15  PANAMAPET   BUY ₹18.11 at ₹384.80 (fresh Friday signal — BUY: 27.33× weekly, month 13.61×, ladder rising; stop ₹274.50; charges ₹0.0428)
2026-06-17  SEAMECLTD   SELL ₹15.38 at stop ₹1,398.40 (-8.3%, charges ₹0.0342) — the cash goes back to work at the next Friday screen
2026-06-22  SPAL        BUY ₹15.38 at ₹1,030.00 (fresh Friday signal — BUY: 66.34× weekly, month 8.68×, ladder rising; stop ₹746.08; charges ₹0.0363)
2026-07-07  PRECWIRE    SELL ₹13.82 at stop ₹376.20 (+14.7%, charges ₹0.0307) — the cash goes back to work at the next Friday screen
2026-07-08  SASKEN      SELL ₹19.82 at stop ₹1,933.72 (+15.1%, charges ₹0.0440) — the cash goes back to work at the next Friday screen
2026-07-13  GANESHHOU   BUY ₹15.67 at ₹860.50 (fresh Friday signal — BUY: 9.80× weekly, month 2.00×, ladder rising; stop ₹712.60; charges ₹0.0370)
2026-07-13  MUNJALAU    BUY ₹17.97 at ₹100.50 (fresh Friday signal — BUY: 19.01× weekly, month 7.01×, ladder rising; stop ₹81.15; charges ₹0.0424)
2026-07-16  SPAL        SELL ₹15.27 at stop ₹1,027.62 (-0.2%, charges ₹0.0339) — the cash goes back to work at the next Friday screen
2026-07-20  JUSTDIAL    BUY ₹15.27 at ₹766.00 (fresh Friday signal — BUY: 127.42× weekly, month 29.52×, ladder rising; stop ₹509.20; charges ₹0.0360)
2026-08-18  JUSTDIAL    SELL ₹13.07 at stop ₹658.64 (-14.0%, charges ₹0.0290) — the cash goes back to work at the next Friday screen
2026-08-24  AVTNPL      BUY ₹13.07 at ₹87.80 (fresh Friday signal — BUY: 10.00× weekly, month 2.79×, ladder rising; stop ₹62.04; charges ₹0.0309)
2026-09-15  ABB         SELL ₹19.09 at stop ₹7,158.25 (+11.8%, charges ₹0.0424) — the cash goes back to work at the next Friday screen
2026-09-15  APCOTEXIND  SELL ₹10.39 at stop ₹576.75 (+9.0%, charges ₹0.0231) — the cash goes back to work at the next Friday screen
2026-09-15  MUNJALAU    SELL ₹18.62 at stop ₹104.60 (+4.1%, charges ₹0.0414) — the cash goes back to work at the next Friday screen
2026-09-16  CLSEL       SELL ₹16.16 at stop ₹274.60 (-7.5%, charges ₹0.0359) — the cash goes back to work at the next Friday screen
2026-09-16  PANAMAPET   SELL ₹20.66 at stop ₹440.87 (+14.6%, charges ₹0.0459) — the cash goes back to work at the next Friday screen
2026-09-21  AVALON      BUY ₹13.02 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.0307)
2026-09-21  INDORAMA    BUY ₹17.99 at ₹91.50 (fresh Friday signal — BUY: 3.12× weekly, month 5.66×, ladder rising; stop ₹56.44; charges ₹0.0425)
2026-09-21  NRBBEARING  BUY ₹17.96 at ₹531.10 (fresh Friday signal — BUY: 4.28× weekly, month 1.73×, ladder rising; stop ₹419.14; charges ₹0.0424)
2026-09-21  SAMBHV      BUY ₹17.95 at ₹151.10 (fresh Friday signal — BUY: 4.17× weekly, month 2.31×, ladder rising; stop ₹116.85; charges ₹0.0424)
2026-09-21  SHOPERSTOP  BUY ₹17.98 at ₹398.60 (fresh Friday signal — ACCUMULATE: 5.07× weekly, month 1.54×, ladder rising; stop ₹351.39; charges ₹0.0425)
```
