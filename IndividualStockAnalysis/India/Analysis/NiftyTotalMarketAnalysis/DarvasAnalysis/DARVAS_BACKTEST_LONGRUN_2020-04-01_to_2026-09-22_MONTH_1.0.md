# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 1388 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹430.01** | **+25.29% a year** |
| The same system before costs and taxes | ₹554.03 | +30.30% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹288.59 | +17.80% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹430.01** (+25.29% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 451 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹23.79** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹78.16**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹29.19 | ₹0.00 | ₹5.8379 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹66.75 | ₹54.27 | ₹20.1324 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹69.91 | ₹68.44 | ₹22.5377 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹142.93 | ₹8.50 | ₹29.6491 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹55.04 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹72.77 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹46.02 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 142.86 | +42.9% | +43.5% | +70.1% |
| 2021 (2021-12-31) | 315.52 | +120.9% | +130.1% | +26.2% |
| 2022 (2022-12-30) | 387.16 | +22.7% | +31.7% | +4.3% |
| 2023 (2023-12-29) | 513.05 | +32.5% | +39.2% | +20.0% |
| 2024 (2024-12-27) | 482.28 | -6.0% | -0.6% | +9.6% |
| 2025 (2025-12-26) | 428.15 | -11.2% | -9.6% | +9.4% |
| 2026 (2026-09-22) | 430.01 | +0.4% | +1.8% | -10.4% |

## What it took to earn it

- **Maximum drawdown: -34.0%** (peak 2024-05-03 → trough 2026-04-02, on weekly closes).
- **208 closed trades**: 92 winners (44%), average winner +38.2%, average loser -10.5%.
- Best closed trade KIRLFER +354.1%; worst COMPINFO -35.4%.
- Median holding period 64 days.
- Cash share of equity averaged 9% across all weeks (median 2%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.20 | 59.96 | 4 |
| 2020-05-29 | 106.62 | 0.27 | 10 |
| 2020-06-26 | 117.68 | 0.00 | 10 |
| 2020-07-31 | 126.16 | 0.00 | 10 |
| 2020-08-28 | 127.41 | 0.00 | 10 |
| 2020-09-25 | 127.95 | 27.55 | 7 |
| 2020-10-30 | 123.35 | 1.21 | 9 |
| 2020-11-27 | 128.21 | 0.00 | 10 |
| 2020-12-24 | 142.86 | 29.89 | 8 |
| 2021-01-29 | 151.65 | 25.97 | 8 |
| 2021-02-26 | 164.75 | 0.00 | 10 |
| 2021-03-26 | 160.20 | 25.93 | 8 |
| 2021-04-30 | 174.32 | 0.00 | 10 |
| 2021-05-28 | 194.50 | 0.00 | 10 |
| 2021-06-25 | 206.47 | 0.00 | 10 |
| 2021-07-30 | 249.35 | 0.00 | 10 |
| 2021-08-27 | 232.60 | 0.00 | 11 |
| 2021-09-24 | 248.16 | 16.99 | 10 |
| 2021-10-29 | 257.29 | 29.24 | 9 |
| 2021-11-26 | 322.72 | 70.65 | 9 |
| 2021-12-31 | 315.52 | 5.31 | 10 |
| 2022-01-28 | 310.76 | 73.50 | 8 |
| 2022-02-25 | 280.95 | 108.21 | 6 |
| 2022-03-25 | 313.37 | 0.00 | 10 |
| 2022-04-29 | 328.23 | 23.50 | 8 |
| 2022-05-27 | 334.97 | 1.60 | 8 |
| 2022-06-24 | 318.56 | 30.15 | 7 |
| 2022-07-29 | 349.25 | 0.00 | 8 |
| 2022-08-26 | 368.18 | 0.00 | 8 |
| 2022-09-30 | 345.34 | 40.41 | 7 |
| 2022-10-28 | 362.24 | 1.82 | 8 |
| 2022-11-25 | 403.53 | 0.47 | 8 |
| 2022-12-30 | 387.16 | 57.03 | 8 |
| 2023-01-27 | 371.67 | 55.72 | 8 |
| 2023-02-24 | 359.79 | 6.87 | 9 |
| 2023-03-31 | 356.34 | 100.16 | 7 |
| 2023-04-28 | 347.32 | 44.99 | 8 |
| 2023-05-26 | 348.99 | 43.45 | 8 |
| 2023-06-30 | 363.64 | 8.58 | 9 |
| 2023-07-28 | 383.28 | 5.44 | 9 |
| 2023-08-25 | 411.81 | 0.00 | 9 |
| 2023-09-29 | 428.41 | 0.00 | 9 |
| 2023-10-27 | 426.14 | 123.60 | 6 |
| 2023-11-24 | 481.54 | 1.36 | 9 |
| 2023-12-29 | 513.05 | 0.00 | 9 |
| 2024-01-25 | 532.96 | 24.30 | 9 |
| 2024-02-23 | 547.09 | 7.60 | 9 |
| 2024-03-28 | 532.06 | 114.66 | 8 |
| 2024-04-26 | 552.54 | 0.00 | 10 |
| 2024-05-31 | 536.80 | 64.29 | 9 |
| 2024-06-28 | 527.35 | 0.00 | 10 |
| 2024-07-26 | 534.50 | 91.54 | 8 |
| 2024-08-30 | 517.88 | 0.00 | 10 |
| 2024-09-27 | 528.81 | 0.00 | 10 |
| 2024-10-25 | 479.21 | 97.94 | 8 |
| 2024-11-29 | 502.83 | 0.00 | 10 |
| 2024-12-27 | 482.28 | 91.64 | 8 |
| 2025-01-31 | 430.37 | 139.11 | 6 |
| 2025-02-28 | 386.83 | 149.34 | 6 |
| 2025-03-27 | 418.70 | 16.05 | 9 |
| 2025-04-25 | 445.18 | 0.00 | 9 |
| 2025-05-30 | 452.36 | 50.02 | 8 |
| 2025-06-27 | 463.64 | 54.26 | 8 |
| 2025-07-25 | 452.64 | 8.33 | 9 |
| 2025-08-29 | 447.98 | 56.20 | 8 |
| 2025-09-26 | 424.14 | 36.10 | 9 |
| 2025-10-31 | 423.78 | 19.49 | 10 |
| 2025-11-28 | 416.92 | 104.32 | 7 |
| 2025-12-26 | 428.15 | 19.06 | 9 |
| 2026-01-30 | 415.91 | 230.25 | 4 |
| 2026-02-27 | 413.58 | 0.00 | 10 |
| 2026-03-27 | 368.69 | 151.19 | 6 |
| 2026-04-30 | 411.98 | 39.46 | 9 |
| 2026-05-29 | 405.76 | 0.00 | 10 |
| 2026-06-25 | 413.37 | 0.00 | 10 |
| 2026-07-31 | 408.10 | 95.12 | 8 |
| 2026-08-28 | 435.23 | 11.87 | 10 |
| 2026-09-22 | 430.01 | 14.39 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| BLUESTONE | 2026-08-03 | 823.40 | 930.40 | 758.29 | +13.0% |
| CAPLIPOINT | 2026-06-15 | 2,435.00 | 2,777.30 | 2,376.52 | +14.1% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,392.00 | 1,242.60 | +40.7% |
| GANESHHOU | 2026-07-13 | 860.50 | 736.80 | 712.60 | -14.4% |
| GLAND | 2026-05-25 | 2,369.80 | 2,916.60 | 2,637.30 | +23.1% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| RUBICON | 2026-06-08 | 1,190.00 | 1,671.20 | 1,653.47 | +40.4% |
| SUNDRMFAST | 2026-09-15 | 1,277.30 | 1,190.90 | 1,127.74 | -6.8% |
| TMB | 2026-08-03 | 864.90 | 883.75 | 817.00 | +2.2% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| LGBBROSLTD | 2020-05-11 | 198.45 | 2020-06-11 | 209.95 | +5.8% |
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| EIDPARRY | 2020-05-11 | 164.00 | 2020-08-17 | 273.03 | +66.5% |
| PANACEABIO | 2020-06-15 | 230.00 | 2020-08-20 | 184.01 | -20.0% |
| APCOTEXIND | 2020-08-24 | 164.95 | 2020-08-31 | 151.95 | -7.9% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| BALAJITELE | 2020-05-04 | 61.40 | 2020-09-09 | 74.07 | +20.6% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| KIOCL | 2020-08-24 | 152.50 | 2020-09-22 | 115.10 | -24.5% |
| SATIA | 2020-09-14 | 122.00 | 2020-09-22 | 102.97 | -15.6% |
| PRINCEPIPE | 2020-09-07 | 208.00 | 2020-10-12 | 220.88 | +6.2% |
| ALEMBICLTD | 2020-06-22 | 81.65 | 2020-11-02 | 91.41 | +12.0% |
| ADVENZYMES | 2020-05-18 | 159.95 | 2020-11-03 | 292.33 | +82.8% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| TCI | 2020-09-14 | 242.00 | 2020-12-22 | 234.75 | -3.0% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
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
| KIRLFER | 2020-06-15 | 61.55 | 2021-08-10 | 279.49 | +354.1% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| GDL | 2021-02-01 | 159.15 | 2021-09-20 | 266.00 | +67.1% |
| GTPL | 2021-08-16 | 249.70 | 2021-10-19 | 267.90 | +7.3% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| NEOGEN | 2021-09-27 | 1,255.00 | 2021-10-25 | 1,142.85 | -8.9% |
| KICL | 2021-08-16 | 2,157.20 | 2021-10-28 | 1,976.00 | -8.4% |
| INDOCO | 2021-08-16 | 484.30 | 2021-11-12 | 412.30 | -14.9% |
| BIGBLOC | 2021-11-15 | 39.80 | 2021-11-16 | 142.59 | +258.3% |
| SHOPERSTOP | 2021-10-25 | 326.00 | 2021-11-22 | 335.82 | +3.0% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-10-25 | 9,508.95 | 2021-11-26 | 10,070.05 | +5.9% |
| SHANKARA | 2021-03-30 | 413.00 | 2021-11-29 | 489.25 | +18.5% |
| SOMANYCERA | 2021-06-21 | 594.85 | 2021-11-29 | 755.11 | +26.9% |
| SUPRAJIT | 2021-11-22 | 454.00 | 2021-12-13 | 391.40 | -13.8% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| MINDAIND | 2021-12-20 | 1,026.00 | 2022-01-07 | 1,088.41 | +6.1% |
| LTTS | 2020-10-19 | 1,745.00 | 2022-01-21 | 4,856.88 | +178.3% |
| TVTODAY | 2021-11-22 | 320.24 | 2022-01-24 | 311.68 | -2.7% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| BSOFT | 2021-11-22 | 473.00 | 2022-02-14 | 424.65 | -10.2% |
| BEML | 2021-12-06 | 1,918.90 | 2022-02-14 | 1,719.50 | -10.4% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| TV18BRDCST | 2022-01-31 | 58.90 | 2022-02-22 | 58.38 | -0.9% |
| COMPINFO | 2022-01-10 | 45.00 | 2022-02-24 | 29.08 | -35.4% |
| JSWISPL | 2022-01-24 | 37.50 | 2022-02-24 | 30.25 | -19.3% |
| M&MFIN | 2022-02-21 | 153.80 | 2022-03-04 | 138.95 | -9.7% |
| EXCELINDUS | 2022-03-07 | 1,523.00 | 2022-03-29 | 1,438.30 | -5.6% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| JAGRAN | 2022-02-14 | 73.30 | 2022-05-06 | 63.98 | -12.7% |
| ADANITRANS | 2021-03-30 | 896.00 | 2022-05-11 | 2,299.37 | +156.6% |
| MFL | 2022-05-02 | 1,430.00 | 2022-05-11 | 1,225.50 | -14.3% |
| COSMOFILMS | 2022-05-09 | 2,008.00 | 2022-05-11 | 1,677.90 | -16.4% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| KRISHANA | 2022-05-16 | 67.96 | 2022-06-16 | 54.77 | -19.4% |
| JSWENERGY | 2021-03-08 | 81.85 | 2022-06-20 | 201.99 | +146.8% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| RAJMET | 2022-03-07 | 278.00 | 2022-09-15 | 359.30 | +29.2% |
| GALAXYSURF | 2022-06-27 | 2,890.05 | 2022-09-29 | 2,959.34 | +2.4% |
| SUNDARMHLD | 2022-10-03 | 103.50 | 2022-10-11 | 92.20 | -10.9% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| RVNL | 2022-10-17 | 36.85 | 2022-12-26 | 60.57 | +64.4% |
| KSL | 2022-12-26 | 330.10 | 2023-01-27 | 328.23 | -0.6% |
| JINDWORLD | 2022-12-26 | 415.10 | 2023-02-01 | 389.50 | -6.2% |
| GICRE | 2022-12-26 | 157.00 | 2023-02-01 | 167.72 | +6.8% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| GRAVITA | 2023-01-30 | 493.40 | 2023-03-02 | 448.45 | -9.1% |
| CHOLAFIN | 2023-02-06 | 777.55 | 2023-03-24 | 727.37 | -6.5% |
| MBAPL | 2022-02-21 | 50.00 | 2023-03-29 | 112.36 | +124.7% |
| SONATSOFTW | 2023-03-06 | 400.75 | 2023-03-29 | 371.45 | -7.3% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| AEGISCHEM | 2023-02-06 | 369.90 | 2023-05-15 | 368.36 | -0.4% |
| MUKANDLTD | 2023-01-02 | 136.70 | 2023-05-17 | 116.23 | -15.0% |
| GUJALKALI | 2023-05-02 | 688.15 | 2023-05-23 | 646.14 | -6.1% |
| KSB | 2023-03-27 | 417.98 | 2023-07-12 | 407.74 | -2.4% |
| THANGAMAYL | 2023-05-29 | 1,344.00 | 2023-07-17 | 1,344.25 | +0.0% |
| GANESHHOUC | 2023-07-24 | 457.00 | 2023-08-14 | 418.62 | -8.4% |
| NEULANDLAB | 2023-05-22 | 2,831.90 | 2023-09-13 | 3,457.30 | +22.1% |
| SJVN | 2023-09-18 | 75.35 | 2023-10-23 | 66.03 | -12.4% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| SHARDAMOTR | 2023-05-22 | 380.00 | 2023-10-25 | 465.07 | +22.4% |
| NATCOPHARM | 2023-04-03 | 569.80 | 2023-11-01 | 771.40 | +35.4% |
| SUNDARMHLD | 2023-11-06 | 144.75 | 2023-12-20 | 145.40 | +0.4% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| MMFL | 2023-12-26 | 1,023.60 | 2024-01-30 | 912.05 | -10.9% |
| SUVENPHAR | 2022-12-26 | 510.00 | 2024-02-06 | 623.20 | +22.2% |
| ASTRAZEN | 2023-08-21 | 4,099.85 | 2024-02-09 | 5,795.95 | +41.4% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| TCI | 2024-02-05 | 987.60 | 2024-03-11 | 790.40 | -20.0% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| ANANDRATHI | 2023-07-17 | 265.70 | 2024-03-27 | 862.65 | +224.7% |
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| UNICHEMLAB | 2024-02-12 | 520.00 | 2024-06-04 | 514.85 | -1.0% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| CENTURYTEX | 2024-04-01 | 1,660.00 | 2024-06-04 | 1,715.70 | +3.4% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| TRENT | 2024-03-18 | 2,709.27 | 2024-07-22 | 3,464.36 | +27.9% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| BECTORFOOD | 2024-06-10 | 298.88 | 2024-08-02 | 263.77 | -11.7% |
| KIRLOSBROS | 2024-05-21 | 1,844.00 | 2024-08-05 | 1,987.46 | +7.8% |
| ADANIPOWER | 2024-06-10 | 783.00 | 2024-08-12 | 632.75 | -19.2% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| AVANTIFEED | 2024-07-29 | 697.65 | 2024-09-09 | 650.13 | -6.8% |
| IOB | 2024-02-12 | 71.50 | 2024-10-03 | 56.57 | -20.9% |
| VGUARD | 2024-08-19 | 524.15 | 2024-10-04 | 420.24 | -19.8% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| TCI | 2024-07-22 | 943.95 | 2024-10-07 | 1,008.09 | +6.8% |
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| JUBLPHARMA | 2024-08-05 | 840.00 | 2024-10-07 | 1,072.08 | +27.6% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| CIGNITITEC | 2024-10-28 | 1,515.00 | 2024-11-18 | 1,330.00 | -12.2% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| AKZOINDIA | 2024-10-14 | 4,122.30 | 2024-12-23 | 3,444.70 | -16.4% |
| PRSMJOHNSN | 2024-09-16 | 214.51 | 2024-12-26 | 170.55 | -20.5% |
| GARFIBRES | 2024-11-25 | 956.00 | 2025-01-09 | 829.35 | -13.2% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| GANECOS | 2024-10-14 | 2,103.85 | 2025-01-10 | 1,751.78 | -16.7% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| COFORGE | 2024-10-28 | 1,543.10 | 2025-01-13 | 1,801.20 | +16.7% |
| CARERATING | 2024-11-04 | 1,510.00 | 2025-01-13 | 1,239.70 | -17.9% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| PGIL | 2025-01-20 | 833.02 | 2025-01-21 | 705.52 | -15.3% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| ANANTRAJ | 2025-01-13 | 879.10 | 2025-01-27 | 764.73 | -13.0% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| JISLJALEQS | 2025-01-13 | 72.00 | 2025-02-12 | 62.58 | -13.1% |
| AUBANK | 2025-02-03 | 595.00 | 2025-02-17 | 516.80 | -13.1% |
| BSE | 2024-10-14 | 4,536.00 | 2025-02-28 | 4,954.63 | +9.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| BAJAJFINSV | 2025-02-24 | 1,868.00 | 2025-03-05 | 1,760.35 | -5.8% |
| GRWRHITECH | 2025-03-10 | 4,219.95 | 2025-04-03 | 3,602.82 | -14.6% |
| AVANTIFEED | 2025-03-10 | 806.00 | 2025-04-07 | 648.95 | -19.5% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| KSCL | 2025-03-24 | 1,285.00 | 2025-05-15 | 1,334.75 | +3.9% |
| HCG | 2025-01-20 | 504.95 | 2025-05-26 | 559.08 | +10.7% |
| COROMANDEL | 2025-04-07 | 1,870.00 | 2025-06-27 | 2,246.75 | +20.1% |
| CARERATING | 2025-05-19 | 1,527.50 | 2025-07-31 | 1,703.35 | +11.5% |
| JSWHL | 2024-11-18 | 19,990.00 | 2025-08-04 | 19,106.01 | -4.4% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| LICI | 2025-06-02 | 477.00 | 2025-08-07 | 438.21 | -8.1% |
| ALKYLAMINE | 2025-06-30 | 2,263.00 | 2025-08-07 | 2,087.62 | -7.7% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| DELHIVERY | 2025-08-11 | 464.65 | 2025-10-01 | 436.10 | -6.1% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| PGHL | 2025-08-04 | 6,440.00 | 2025-11-06 | 5,938.45 | -7.8% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| ASTRAMICRO | 2025-10-06 | 1,119.85 | 2025-11-06 | 1,026.00 | -8.4% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| FLUOROCHEM | 2025-09-22 | 3,820.00 | 2025-11-24 | 3,412.02 | -10.7% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| TDPOWERSYS | 2025-11-10 | 389.50 | 2025-11-24 | 357.49 | -8.2% |
| PSB | 2025-10-27 | 30.80 | 2025-12-03 | 29.05 | -5.7% |
| CUMMINSIND | 2025-08-11 | 3,806.90 | 2026-01-06 | 4,191.50 | +10.1% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| GRAVITA | 2025-12-01 | 1,825.10 | 2026-01-09 | 1,678.56 | -8.0% |
| KIRLOSENG | 2025-12-08 | 1,130.00 | 2026-01-12 | 1,140.95 | +1.0% |
| UPL | 2025-08-11 | 688.95 | 2026-01-20 | 729.12 | +5.8% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| MARUTI | 2025-09-01 | 14,790.00 | 2026-01-23 | 15,657.90 | +5.9% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| CEIGALL | 2026-02-09 | 297.00 | 2026-03-04 | 266.33 | -10.3% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| TATASTEEL | 2026-02-02 | 185.38 | 2026-03-09 | 190.52 | +2.8% |
| HINDCOPPER | 2026-01-12 | 532.00 | 2026-03-12 | 528.63 | -0.6% |
| RBA | 2026-01-19 | 67.50 | 2026-03-12 | 61.08 | -9.5% |
| HINDALCO | 2026-02-02 | 905.70 | 2026-03-23 | 862.65 | -4.8% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-16 | 121.14 | 2026-03-23 | 110.67 | -8.6% |
| BRITANNIA | 2026-02-02 | 5,733.00 | 2026-03-24 | 5,436.85 | -5.2% |
| SOLARINDS | 2026-03-09 | 15,250.00 | 2026-03-30 | 12,217.95 | -19.9% |
| INDIANB | 2026-02-02 | 843.15 | 2026-04-30 | 815.10 | -3.3% |
| INOXINDIA | 2026-03-30 | 1,185.00 | 2026-05-13 | 1,372.18 | +15.8% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| GRSE | 2026-05-04 | 2,956.00 | 2026-05-18 | 2,586.30 | -12.5% |
| NTPC | 2026-03-16 | 384.50 | 2026-06-02 | 364.80 | -5.1% |
| NLCINDIA | 2026-05-18 | 351.55 | 2026-06-09 | 320.62 | -8.8% |
| MCX | 2026-02-02 | 2,212.70 | 2026-07-07 | 2,618.20 | +18.3% |
| THERMAX | 2026-04-06 | 3,295.80 | 2026-07-29 | 4,306.64 | +30.7% |
| VTL | 2026-03-30 | 520.95 | 2026-07-31 | 592.80 | +13.8% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-03-16 | 6,400.00 | 2026-09-15 | 7,158.25 | +11.8% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_MONTH_1.0.csv` beside this report (27962 events in all).*

```
2020-04-13  DEEPAKNTR   BUY ₹10.00 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 2.47×, ladder rising; stop ₹240.25; charges ₹0.0118)
2020-04-27  CADILAHC    BUY ₹10.01 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 5.12×, ladder rising; stop ₹310.03; charges ₹0.0119)
2020-04-27  SYNGENE     BUY ₹10.02 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.94×, ladder rising; stop ₹285.95; charges ₹0.0119)
2020-04-27  TAJGVK      BUY ₹10.01 at ₹133.40 (fresh Friday signal — BUY: 6.65× weekly, month 2.23×, ladder rising; stop ₹106.49; charges ₹0.0119)
2020-05-04  BALAJITELE  BUY ₹9.94 at ₹61.40 (fresh Friday signal — BUY: surged 4.19× weekly on 2020-04-24 (month 2.47×), ladder rising NOW — promoted from the ladder watch; stop ₹48.55; charges ₹0.0118)
2020-05-11  APLLTD      BUY ₹9.89 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.70× weekly, month 6.10×, ladder rising; stop ₹694.45; charges ₹0.0117)
2020-05-11  EIDPARRY    BUY ₹9.92 at ₹164.00 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 1.46×, ladder rising; stop ₹132.60; charges ₹0.0118)
2020-05-11  IOLCP       BUY ₹9.89 at ₹66.18 (fresh Friday signal — BUY: 2.18× weekly, month 2.65×, ladder rising; stop ₹51.22; charges ₹0.0117)
2020-05-11  LGBBROSLTD  BUY ₹9.93 at ₹198.45 (fresh Friday signal — ACCUMULATE: 3.61× weekly, month 1.11×, ladder rising; stop ₹175.24; charges ₹0.0118)
2020-05-18  ADVENZYMES  BUY ₹10.12 at ₹159.95 (fresh Friday signal — ACCUMULATE: 3.12× weekly, month 2.00×, ladder rising; stop ₹126.20; charges ₹0.0120)
2020-06-11  LGBBROSLTD  SELL ₹10.48 at stop ₹209.95 (+5.8%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2020-06-12  DEEPAKNTR   SELL ₹9.97 at stop ₹474.05 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-06-15  KIRLFER     BUY ₹9.53 at ₹61.55 (fresh Friday signal — BUY: 8.70× weekly, month 2.09×, ladder rising; stop ₹48.49; charges ₹0.0113)
2020-06-15  PANACEABIO  BUY ₹11.19 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.25×, ladder rising; stop ₹114.11; charges ₹0.0133)
2020-06-16  IOLCP       SELL ₹10.34 at stop ₹69.35 (+4.8%, charges ₹0.0107) — the cash goes back to work at the next Friday screen
2020-06-22  ALEMBICLTD  BUY ₹10.34 at ₹81.65 (fresh Friday signal — BUY: 11.73× weekly, month 8.49×, ladder rising; stop ₹44.84; charges ₹0.0122)
2020-08-17  EIDPARRY    SELL ₹16.49 at stop ₹273.03 (+66.5%, charges ₹0.0171) — the cash goes back to work at the next Friday screen
2020-08-20  PANACEABIO  SELL ₹8.93 at stop ₹184.01 (-20.0%, charges ₹0.0093) — the cash goes back to work at the next Friday screen
2020-08-24  APCOTEXIND  BUY ₹12.96 at ₹164.95 (fresh Friday signal — BUY: 8.08× weekly, month 5.83×, ladder rising; stop ₹119.51; charges ₹0.0154)
2020-08-24  KIOCL       BUY ₹12.45 at ₹152.50 (fresh Friday signal — BUY: 7.39× weekly, month 5.13×, ladder rising; stop ₹107.06; charges ₹0.0148)
2020-08-31  APCOTEXIND  SELL ₹11.92 at stop ₹151.95 (-7.9%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.82 at stop ₹928.62 (+19.9%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹12.35 at ₹1,398.95 (fresh Friday signal — BUY: 5.36× weekly, month 3.91×, ladder rising; stop ₹1,211.25; charges ₹0.0146)
2020-09-07  PRINCEPIPE  BUY ₹11.39 at ₹208.00 (fresh Friday signal — BUY: 3.47× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.0135)
2020-09-08  CADILAHC    SELL ₹11.04 at stop ₹364.99 (+10.5%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-09  BALAJITELE  SELL ₹11.96 at stop ₹74.07 (+20.6%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-14  SATIA       BUY ₹10.34 at ₹122.00 (fresh Friday signal — ACCUMULATE: 2.86× weekly, month 6.16×, ladder rising; stop ₹102.97; charges ₹0.0122)
2020-09-14  TCI         BUY ₹12.67 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.76× weekly, month 3.77×, ladder rising; stop ₹190.07; charges ₹0.0150)
2020-09-22  KIOCL       SELL ₹9.38 at stop ₹115.10 (-24.5%, charges ₹0.0097) — the cash goes back to work at the next Friday screen
2020-09-22  SATIA       SELL ₹8.70 at stop ₹102.97 (-15.6%, charges ₹0.0090) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹9.47 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹12.86 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0152)
2020-09-28  SAKSOFT     BUY ₹12.89 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.0153)
2020-10-12  PRINCEPIPE  SELL ₹12.06 at stop ₹220.88 (+6.2%, charges ₹0.0125) — the cash goes back to work at the next Friday screen
2020-10-19  LTTS        BUY ₹12.66 at ₹1,745.00 (fresh Friday signal — BUY: 4.76× weekly, month 2.59×, ladder rising; stop ₹1,482.95; charges ₹0.0150)
2020-11-02  ALEMBICLTD  SELL ₹11.55 at stop ₹91.41 (+12.0%, charges ₹0.0120) — the cash goes back to work at the next Friday screen
2020-11-03  ADVENZYMES  SELL ₹18.46 at stop ₹292.33 (+82.8%, charges ₹0.0191) — the cash goes back to work at the next Friday screen
2020-11-09  GREENPANEL  BUY ₹6.73 at ₹86.40 (fresh Friday signal — BUY: 2.76× weekly, month 1.37×, ladder rising; stop ₹63.17; charges ₹0.0080)
2020-11-09  JINDWORLD   BUY ₹12.25 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.28× weekly, month 1.55×, ladder rising; stop ₹39.81; charges ₹0.0145)
2020-11-09  RAMCOIND    BUY ₹12.24 at ₹199.00 (fresh Friday signal — ACCUMULATE: 2.92× weekly, month 1.31×, ladder rising; stop ₹155.29; charges ₹0.0145)
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹12.26 at stop ₹234.75 (-3.0%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2020-12-28  MTNL        BUY ₹14.63 at ₹14.10 (fresh Friday signal — BUY: 9.97× weekly, month 4.77×, ladder rising; stop ₹8.26; charges ₹0.0173)
2020-12-28  PAISALO     BUY ₹14.50 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0172)
2021-01-25  SAKSOFT     SELL ₹11.00 at stop ₹341.10 (-14.4%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹14.20 at stop ₹928.05 (+10.7%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹15.41 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.0183)
2021-02-01  GDL         BUY ₹10.56 at ₹159.15 (fresh Friday signal — BUY: 2.82× weekly, month 6.27×, ladder rising; stop ₹92.41; charges ₹0.0125)
2021-02-16  MTNL        SELL ₹12.48 at stop ₹12.06 (-14.5%, charges ₹0.0129) — the cash goes back to work at the next Friday screen
2021-02-22  MAHINDCIE   BUY ₹12.48 at ₹188.00 (fresh Friday signal — BUY: 22.74× weekly, month 4.25×, ladder rising; stop ₹143.79; charges ₹0.0148)
2021-03-01  JINDWORLD   SELL ₹12.74 at stop ₹52.12 (+4.2%, charges ₹0.0132) — the cash goes back to work at the next Friday screen
2021-03-08  JSWENERGY   BUY ₹12.74 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.50×, ladder rising; stop ₹65.79; charges ₹0.0151)
2021-03-19  APTECHT     SELL ₹17.60 at stop ₹204.25 (+14.5%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2021-03-19  MAHINDCIE   SELL ₹10.50 at stop ₹158.46 (-15.7%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2021-03-19  RAMCOIND    SELL ₹14.49 at stop ₹236.22 (+18.7%, charges ₹0.0150) — the cash goes back to work at the next Friday screen
2021-03-22  GFLLIMITED  BUY ₹15.87 at ₹93.00 (fresh Friday signal — ACCUMULATE: 6.17× weekly, month 3.98×, ladder rising; stop ₹74.39; charges ₹0.0188)
2021-03-22  KEI         BUY ₹10.93 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.0130)
2021-03-22  VIDHIING    BUY ₹15.79 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0187)
2021-03-25  BANARISUG   SELL ₹13.98 at stop ₹1,586.36 (+13.4%, charges ₹0.0145) — the cash goes back to work at the next Friday screen
2021-03-25  GREENPANEL  SELL ₹11.96 at stop ₹153.89 (+78.1%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2021-03-30  ADANITRANS  BUY ₹9.76 at ₹896.00 (fresh Friday signal — BUY: 1.91× weekly, month 1.35×, ladder rising; stop ₹693.23; charges ₹0.0116)
2021-03-30  SHANKARA    BUY ₹16.17 at ₹413.00 (fresh Friday signal — ACCUMULATE: 1.99× weekly, month 1.30×, ladder rising; stop ₹354.55; charges ₹0.0192)
2021-04-01  ADANITRANS  TRIM 3.5% (₹0.38 at ₹999.20) to pay the tax bill
2021-04-01  GDL         TRIM 3.5% (₹0.41 at ₹177.90) to pay the tax bill
2021-04-01  GFLLIMITED  TRIM 3.5% (₹0.65 at ₹108.35) to pay the tax bill
2021-04-01  JSWENERGY   TRIM 3.5% (₹0.50 at ₹90.70) to pay the tax bill
2021-04-01  KEI         TRIM 3.5% (₹0.39 at ₹528.60) to pay the tax bill
2021-04-01  KIRLFER     TRIM 3.5% (₹0.94 at ₹173.50) to pay the tax bill
2021-04-01  LTTS        TRIM 3.5% (₹0.69 at ₹2,720.60) to pay the tax bill
2021-04-01  PAISALO     TRIM 3.5% (₹0.70 at ₹78.11) to pay the tax bill
2021-04-01  SHANKARA    TRIM 3.5% (₹0.58 at ₹425.05) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹5.8379 paid (STCG ₹29.19 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  VIDHIING    TRIM 3.5% (₹0.59 at ₹207.10) to pay the tax bill
2021-04-12  PAISALO     SELL ₹17.73 at stop ₹72.41 (+27.1%, charges ₹0.0184) — the cash goes back to work at the next Friday screen
2021-04-13  GFLLIMITED  SELL ₹12.22 at stop ₹74.39 (-20.0%, charges ₹0.0127) — the cash goes back to work at the next Friday screen
2021-04-19  KPRMILL     BUY ₹14.87 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0176)
2021-04-19  MOREPENLAB  BUY ₹15.08 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹0.0179)
2021-06-18  VIDHIING    SELL ₹14.26 at stop ₹182.64 (-6.2%, charges ₹0.0148) — the cash goes back to work at the next Friday screen
2021-06-21  SOMANYCERA  BUY ₹14.26 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0169)
2021-08-10  KIRLFER     SELL ₹41.65 at stop ₹279.49 (+354.1%, charges ₹0.0432) — the cash goes back to work at the next Friday screen
2021-08-10  MOREPENLAB  SELL ₹22.63 at stop ₹56.33 (+50.4%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹22.16 at stop ₹352.48 (+49.4%, charges ₹0.0230) — the cash goes back to work at the next Friday screen
2021-08-16  GTPL        BUY ₹23.76 at ₹249.70 (fresh Friday signal — BUY: 3.92× weekly, month 1.57×, ladder rising; stop ₹168.53; charges ₹0.0281)
2021-08-16  INDOCO      BUY ₹23.77 at ₹484.30 (fresh Friday signal — BUY: 4.80× weekly, month 2.73×, ladder rising; stop ₹412.30; charges ₹0.0282)
2021-08-16  KICL        BUY ₹15.10 at ₹2,157.20 (fresh Friday signal — BUY: 3.73× weekly, month 2.45×, ladder rising; stop ₹1,895.58; charges ₹0.0179)
2021-08-16  TATAINVEST  BUY ₹23.82 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0282)
2021-09-20  GDL         SELL ₹16.99 at stop ₹266.00 (+67.1%, charges ₹0.0176) — the cash goes back to work at the next Friday screen
2021-09-27  NEOGEN      BUY ₹16.99 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0201)
2021-10-19  GTPL        SELL ₹25.43 at stop ₹267.90 (+7.3%, charges ₹0.0264) — the cash goes back to work at the next Friday screen
2021-10-22  KEI         SELL ₹17.20 at stop ₹853.10 (+63.4%, charges ₹0.0178) — the cash goes back to work at the next Friday screen
2021-10-25  NEOGEN      SELL ₹15.43 at stop ₹1,142.85 (-8.9%, charges ₹0.0160) — the cash goes back to work at the next Friday screen
2021-10-25  SHOPERSTOP  BUY ₹17.29 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹0.0205)
2021-10-25  TTKPRESTIG  BUY ₹25.34 at ₹9,508.95 (fresh Friday signal — BUY: 6.63× weekly, month 1.31×, ladder rising; stop ₹8,326.75; charges ₹0.0300)
2021-10-28  KICL        SELL ₹13.81 at stop ₹1,976.00 (-8.4%, charges ₹0.0143) — the cash goes back to work at the next Friday screen
2021-11-01  TCIEXP      BUY ₹25.96 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0308)
2021-11-12  INDOCO      SELL ₹20.19 at stop ₹412.30 (-14.9%, charges ₹0.0209) — the cash goes back to work at the next Friday screen
2021-11-15  BIGBLOC     BUY ₹23.47 at ₹39.80 (fresh Friday signal — BUY: 6.89× weekly, month 4.00×, ladder rising; stop ₹142.59; charges ₹0.0278)
2021-11-16  BIGBLOC     SELL ₹83.88 at stop ₹142.59 (+258.3%, charges ₹0.0870) — the cash goes back to work at the next Friday screen
2021-11-22  BSOFT       BUY ₹19.76 at ₹473.00 (fresh Friday signal — BUY: 6.30× weekly, month 1.77×, ladder rising; stop ₹375.44; charges ₹0.0234)
2021-11-22  SHOPERSTOP  SELL ₹17.78 at stop ₹335.82 (+3.0%, charges ₹0.0184) — the cash goes back to work at the next Friday screen
2021-11-22  SUPRAJIT    BUY ₹31.95 at ₹454.00 (fresh Friday signal — BUY: 10.19× weekly, month 1.96×, ladder rising; stop ₹309.33; charges ₹0.0379)
2021-11-22  TVTODAY     BUY ₹32.17 at ₹320.24 (fresh Friday signal — BUY: 15.58× weekly, month 3.55×, ladder rising; stop ₹253.08; charges ₹0.0381)
2021-11-26  TATAINVEST  SELL ₹26.10 at stop ₹1,436.49 (+9.8%, charges ₹0.0271) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹26.77 at stop ₹10,070.05 (+5.9%, charges ₹0.0278) — the cash goes back to work at the next Friday screen
2021-11-29  RAYMOND     BUY ₹31.49 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0373)
2021-11-29  RSYSTEMS    BUY ₹31.66 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0375)
2021-11-29  SHANKARA    SELL ₹18.44 at stop ₹489.25 (+18.5%, charges ₹0.0191) — the cash goes back to work at the next Friday screen
2021-11-29  SOMANYCERA  SELL ₹18.06 at stop ₹755.11 (+26.9%, charges ₹0.0187) — the cash goes back to work at the next Friday screen
2021-12-06  BEML        BUY ₹31.36 at ₹1,918.90 (fresh Friday signal — BUY: 5.62× weekly, month 1.07×, ladder rising; stop ₹1,434.50; charges ₹0.0372)
2021-12-13  SUPRAJIT    SELL ₹27.48 at stop ₹391.40 (-13.8%, charges ₹0.0285) — the cash goes back to work at the next Friday screen
2021-12-16  RSYSTEMS    SELL ₹28.31 at stop ₹291.18 (-10.4%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹30.48 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0361)
2021-12-20  MINDAIND    BUY ₹30.28 at ₹1,026.00 (fresh Friday signal — BUY: 5.05× weekly, month 1.81×, ladder rising; stop ₹787.66; charges ₹0.0359)
2021-12-21  TCIEXP      SELL ₹28.86 at stop ₹2,039.74 (+11.4%, charges ₹0.0299) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹31.23 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0370)
2022-01-07  MINDAIND    SELL ₹32.05 at stop ₹1,088.41 (+6.1%, charges ₹0.0332) — the cash goes back to work at the next Friday screen
2022-01-10  COMPINFO    BUY ₹32.30 at ₹45.00 (fresh Friday signal — BUY: 4.39× weekly, month 5.27×, ladder rising; stop ₹25.44; charges ₹0.0383)
2022-01-21  LTTS        SELL ₹33.92 at stop ₹4,856.88 (+178.3%, charges ₹0.0352) — the cash goes back to work at the next Friday screen
2022-01-24  JSWISPL     BUY ₹30.52 at ₹37.50 (fresh Friday signal — BUY: 5.58× weekly, month 4.04×, ladder rising; stop ₹27.79; charges ₹0.0362)
2022-01-24  TVTODAY     SELL ₹31.25 at stop ₹311.68 (-2.7%, charges ₹0.0324) — the cash goes back to work at the next Friday screen
2022-01-25  SWANENERGY  SELL ₹33.81 at stop ₹162.64 (+8.5%, charges ₹0.0351) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹31.12 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0369)
2022-01-31  TV18BRDCST  BUY ₹31.10 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.0368)
2022-02-11  SHARDACROP  SELL ₹28.86 at stop ₹545.30 (-7.1%, charges ₹0.0299) — the cash goes back to work at the next Friday screen
2022-02-14  BEML        SELL ₹28.04 at stop ₹1,719.50 (-10.4%, charges ₹0.0291) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹17.70 at stop ₹424.65 (-10.2%, charges ₹0.0184) — the cash goes back to work at the next Friday screen
2022-02-14  JAGRAN      BUY ₹29.61 at ₹73.30 (fresh Friday signal — ACCUMULATE: 7.50× weekly, month 1.34×, ladder rising; stop ₹62.00; charges ₹0.0351)
2022-02-15  RAYMOND     SELL ₹35.81 at stop ₹679.35 (+14.0%, charges ₹0.0371) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹28.79 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0341)
2022-02-21  M&MFIN      BUY ₹28.74 at ₹153.80 (fresh Friday signal — ACCUMULATE: 2.29× weekly, month 1.05×, ladder rising; stop ₹138.95; charges ₹0.0341)
2022-02-21  MBAPL       BUY ₹28.73 at ₹50.00 (fresh Friday signal — BUY: surged 3.35× weekly on 2022-01-28 (month 1.18×), ladder rising NOW — promoted from the ladder watch; stop ₹35.45; charges ₹0.0340)
2022-02-22  GREENLAM    SELL ₹26.24 at stop ₹313.67 (-13.7%, charges ₹0.0272) — the cash goes back to work at the next Friday screen
2022-02-22  TV18BRDCST  SELL ₹30.75 at stop ₹58.38 (-0.9%, charges ₹0.0319) — the cash goes back to work at the next Friday screen
2022-02-24  COMPINFO    SELL ₹20.83 at stop ₹29.08 (-35.4%, charges ₹0.0216) — the cash goes back to work at the next Friday screen
2022-02-24  JSWISPL     SELL ₹24.56 at stop ₹30.25 (-19.3%, charges ₹0.0255) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹28.49 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0338)
2022-02-28  SHANTIGEAR  BUY ₹28.62 at ₹185.30 (fresh Friday signal — BUY: surged 3.40× weekly on 2022-02-11 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹170.29; charges ₹0.0339)
2022-03-04  M&MFIN      SELL ₹25.91 at stop ₹138.95 (-9.7%, charges ₹0.0269) — the cash goes back to work at the next Friday screen
2022-03-07  EXCELINDUS  BUY ₹20.06 at ₹1,523.00 (fresh Friday signal — BUY: surged 1.57× weekly on 2022-02-25 (month 3.32×), ladder rising NOW — promoted from the ladder watch; stop ₹1,016.01; charges ₹0.0238)
2022-03-07  GTLINFRA    BUY ₹28.51 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0338)
2022-03-07  RAJMET      BUY ₹28.43 at ₹278.00 (fresh Friday signal — BUY: surged 6.93× weekly on 2022-02-18 (month 4.62×), ladder rising NOW — promoted from the ladder watch; stop ₹226.96; charges ₹0.0337)
2022-03-29  EXCELINDUS  SELL ₹18.91 at stop ₹1,438.30 (-5.6%, charges ₹0.0196) — the cash goes back to work at the next Friday screen
2022-04-01  ADANITRANS  TRIM 0.4% (₹0.11 at ₹2,421.45) to pay the tax bill
2022-04-01  CGCL        TRIM 0.4% (₹0.12 at ₹614.95) to pay the tax bill
2022-04-01  DANGEE      TRIM 0.4% (₹0.16 at ₹310.25) to pay the tax bill
2022-04-01  GTLINFRA    TRIM 0.4% (₹0.11 at ₹1.55) to pay the tax bill
2022-04-01  JAGRAN      TRIM 0.4% (₹0.11 at ₹67.10) to pay the tax bill
2022-04-01  JSWENERGY   TRIM 0.4% (₹0.16 at ₹253.45) to pay the tax bill
2022-04-01  MBAPL       TRIM 0.4% (₹0.19 at ₹80.05) to pay the tax bill
2022-04-01  RAJMET      TRIM 0.4% (₹0.15 at ₹349.70) to pay the tax bill
2022-04-01  SHANTIGEAR  TRIM 0.4% (₹0.12 at ₹183.85) to pay the tax bill
2022-04-01  TAX         FY2022 settled: ₹20.1324 paid (STCG ₹66.75 @20%, LTCG ₹54.27 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-29  GTLINFRA    SELL ₹23.50 at stop ₹1.41 (-17.1%, charges ₹0.0244) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹23.50 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.0278)
2022-05-06  JAGRAN      SELL ₹25.68 at stop ₹63.98 (-12.7%, charges ₹0.0266) — the cash goes back to work at the next Friday screen
2022-05-09  COSMOFILMS  BUY ₹25.68 at ₹2,008.00 (fresh Friday signal — ACCUMULATE: 3.00× weekly, month 1.17×, ladder rising; stop ₹1,677.90; charges ₹0.0304)
2022-05-11  ADANITRANS  SELL ₹24.02 at stop ₹2,299.37 (+156.6%, charges ₹0.0249) — the cash goes back to work at the next Friday screen
2022-05-11  COSMOFILMS  SELL ₹21.41 at stop ₹1,677.90 (-16.4%, charges ₹0.0222) — the cash goes back to work at the next Friday screen
2022-05-11  MFL         SELL ₹20.09 at stop ₹1,225.50 (-14.3%, charges ₹0.0208) — the cash goes back to work at the next Friday screen
2022-05-16  KRISHANA    BUY ₹31.97 at ₹67.96 (fresh Friday signal — ACCUMULATE: 1.67× weekly, month 1.86×, ladder rising; stop ₹54.77; charges ₹0.0379)
2022-05-16  VBL         BUY ₹31.96 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0379)
2022-06-06  VBL         SELL ₹28.45 at stop ₹196.27 (-10.8%, charges ₹0.0295) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹30.05 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0356)
2022-06-16  KRISHANA    SELL ₹25.71 at stop ₹54.77 (-19.4%, charges ₹0.0267) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹25.71 at ₹950.15 (fresh Friday signal — BUY: surged 6.84× weekly on 2022-06-10 (month 1.49×), ladder rising NOW — promoted from the ladder watch; stop ₹706.80; charges ₹0.0305)
2022-06-20  JSWENERGY   SELL ₹30.15 at stop ₹201.99 (+146.8%, charges ₹0.0313) — the cash goes back to work at the next Friday screen
2022-06-27  GALAXYSURF  BUY ₹30.15 at ₹2,890.05 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 1.11×, ladder rising; stop ₹2,589.70; charges ₹0.0357)
2022-09-06  DANGEE      SELL ₹45.20 at stop ₹375.25 (+59.7%, charges ₹0.0469) — the cash goes back to work at the next Friday screen
2022-09-12  SHREECEM    BUY ₹36.49 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0432)
2022-09-15  RAJMET      SELL ₹36.50 at stop ₹359.30 (+29.2%, charges ₹0.0379) — the cash goes back to work at the next Friday screen
2022-09-19  JSWHL       BUY ₹35.60 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0422)
2022-09-29  GALAXYSURF  SELL ₹30.80 at stop ₹2,959.34 (+2.4%, charges ₹0.0319) — the cash goes back to work at the next Friday screen
2022-10-03  SUNDARMHLD  BUY ₹34.37 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹0.0407)
2022-10-11  SUNDARMHLD  SELL ₹30.55 at stop ₹92.20 (-10.9%, charges ₹0.0317) — the cash goes back to work at the next Friday screen
2022-10-17  RVNL        BUY ₹34.77 at ₹36.85 (fresh Friday signal — BUY: 4.04× weekly, month 1.42×, ladder rising; stop ₹31.21; charges ₹0.0412)
2022-11-03  APARINDS    SELL ₹36.67 at stop ₹1,358.50 (+43.0%, charges ₹0.0380) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹38.02 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0451)
2022-12-21  ELECON      SELL ₹49.56 at stop ₹202.49 (+65.3%, charges ₹0.0514) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹53.04 at stop ₹345.56 (+86.5%, charges ₹0.0550) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹37.90 at stop ₹139.84 (-0.1%, charges ₹0.0393) — the cash goes back to work at the next Friday screen
2022-12-26  GICRE       BUY ₹26.33 at ₹157.00 (fresh Friday signal — BUY: surged 4.73× weekly on 2022-12-02 (month 1.82×), ladder rising NOW — promoted from the ladder watch; stop ₹134.14; charges ₹0.0312)
2022-12-26  JINDWORLD   BUY ₹38.20 at ₹415.10 (fresh Friday signal — BUY: 3.67× weekly, month 1.21×, ladder rising; stop ₹362.90; charges ₹0.0453)
2022-12-26  KSL         BUY ₹38.07 at ₹330.10 (fresh Friday signal — BUY: surged 5.50× weekly on 2022-12-09 (month 2.50×), ladder rising NOW — promoted from the ladder watch; stop ₹328.23; charges ₹0.0451)
2022-12-26  RVNL        SELL ₹57.03 at stop ₹60.57 (+64.4%, charges ₹0.0592) — the cash goes back to work at the next Friday screen
2022-12-26  SUVENPHAR   BUY ₹38.36 at ₹510.00 (fresh Friday signal — BUY: 2.08× weekly, month 1.08×, ladder rising; stop ₹427.98; charges ₹0.0454)
2023-01-02  MUKANDLTD   BUY ₹39.08 at ₹136.70 (fresh Friday signal — BUY: 6.81× weekly, month 2.54×, ladder rising; stop ₹103.76; charges ₹0.0463)
2023-01-27  KSL         SELL ₹37.77 at stop ₹328.23 (-0.6%, charges ₹0.0392) — the cash goes back to work at the next Friday screen
2023-01-30  GRAVITA     BUY ₹37.25 at ₹493.40 (fresh Friday signal — BUY: 2.54× weekly, month 1.13×, ladder rising; stop ₹376.61; charges ₹0.0441)
2023-02-01  GICRE       SELL ₹28.06 at stop ₹167.72 (+6.8%, charges ₹0.0291) — the cash goes back to work at the next Friday screen
2023-02-01  JINDWORLD   SELL ₹35.77 at stop ₹389.50 (-6.2%, charges ₹0.0371) — the cash goes back to work at the next Friday screen
2023-02-06  AEGISCHEM   BUY ₹36.43 at ₹369.90 (fresh Friday signal — BUY: 3.47× weekly, month 1.02×, ladder rising; stop ₹296.92; charges ₹0.0432)
2023-02-06  CHOLAFIN    BUY ₹36.31 at ₹777.55 (fresh Friday signal — BUY: 2.87× weekly, month 1.34×, ladder rising; stop ₹661.25; charges ₹0.0430)
2023-02-17  CGCL        SELL ₹33.64 at stop ₹704.95 (+17.6%, charges ₹0.0349) — the cash goes back to work at the next Friday screen
2023-02-20  TIIL        BUY ₹36.34 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0431)
2023-03-02  GRAVITA     SELL ₹33.78 at stop ₹448.45 (-9.1%, charges ₹0.0350) — the cash goes back to work at the next Friday screen
2023-03-06  SONATSOFTW  BUY ₹36.63 at ₹400.75 (fresh Friday signal — BUY: 3.29× weekly, month 4.54×, ladder rising; stop ₹325.85; charges ₹0.0434)
2023-03-24  CHOLAFIN    SELL ₹33.89 at stop ₹727.37 (-6.5%, charges ₹0.0352) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹35.77 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.61×, ladder rising; stop ₹372.21; charges ₹0.0424)
2023-03-29  MBAPL       SELL ₹64.15 at stop ₹112.36 (+124.7%, charges ₹0.0665) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹33.88 at stop ₹371.45 (-7.3%, charges ₹0.0351) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹33.84 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.0401)
2023-04-03  NATCOPHARM  BUY ₹33.78 at ₹569.80 (fresh Friday signal — ACCUMULATE: 1.84× weekly, month 1.46×, ladder rising; stop ₹494.24; charges ₹0.0400)
2023-04-03  TAX         FY2023 settled: ₹22.5377 paid (STCG ₹69.91 @20%, LTCG ₹68.44 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-24  SHREECEM    SELL ₹34.99 at stop ₹23,636.00 (-3.9%, charges ₹0.0363) — the cash goes back to work at the next Friday screen
2023-05-02  GUJALKALI   BUY ₹34.35 at ₹688.15 (fresh Friday signal — BUY: 22.10× weekly, month 1.42×, ladder rising; stop ₹590.90; charges ₹0.0407)
2023-05-15  AEGISCHEM   SELL ₹36.19 at stop ₹368.36 (-0.4%, charges ₹0.0375) — the cash goes back to work at the next Friday screen
2023-05-17  MUKANDLTD   SELL ₹33.15 at stop ₹116.23 (-15.0%, charges ₹0.0344) — the cash goes back to work at the next Friday screen
2023-05-22  NEULANDLAB  BUY ₹34.32 at ₹2,831.90 (fresh Friday signal — BUY: 6.13× weekly, month 4.03×, ladder rising; stop ₹1,908.60; charges ₹0.0407)
2023-05-22  SHARDAMOTR  BUY ₹34.40 at ₹380.00 (fresh Friday signal — BUY: 9.54× weekly, month 2.31×, ladder rising; stop ₹342.95; charges ₹0.0408)
2023-05-23  GUJALKALI   SELL ₹32.18 at stop ₹646.14 (-6.1%, charges ₹0.0334) — the cash goes back to work at the next Friday screen
2023-05-29  THANGAMAYL  BUY ₹34.87 at ₹1,344.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.50×, ladder rising; stop ₹1,116.30; charges ₹0.0413)
2023-07-12  KSB         SELL ₹34.82 at stop ₹407.74 (-2.4%, charges ₹0.0361) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹35.39 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0419)
2023-07-17  THANGAMAYL  SELL ₹34.80 at stop ₹1,344.25 (+0.0%, charges ₹0.0361) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹37.36 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.84×, ladder rising; stop ₹359.10; charges ₹0.0443)
2023-08-14  GANESHHOUC  SELL ₹34.15 at stop ₹418.62 (-8.4%, charges ₹0.0354) — the cash goes back to work at the next Friday screen
2023-08-21  ASTRAZEN    BUY ₹39.59 at ₹4,099.85 (fresh Friday signal — BUY: 6.03× weekly, month 2.40×, ladder rising; stop ₹3,562.50; charges ₹0.0469)
2023-09-13  NEULANDLAB  SELL ₹41.80 at stop ₹3,457.30 (+22.1%, charges ₹0.0434) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹41.80 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.67×, ladder rising; stop ₹58.28; charges ₹0.0495)
2023-10-23  SJVN        SELL ₹36.55 at stop ₹66.03 (-12.4%, charges ₹0.0379) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹45.04 at stop ₹1,840.70 (+33.4%, charges ₹0.0467) — the cash goes back to work at the next Friday screen
2023-10-25  SHARDAMOTR  SELL ₹42.01 at stop ₹465.07 (+22.4%, charges ₹0.0436) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹38.42 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0455)
2023-10-30  KKCL        BUY ₹42.61 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0505)
2023-10-30  SHAREINDIA  BUY ₹42.57 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0504)
2023-11-01  NATCOPHARM  SELL ₹45.63 at stop ₹771.40 (+35.4%, charges ₹0.0473) — the cash goes back to work at the next Friday screen
2023-11-06  SUNDARMHLD  BUY ₹44.27 at ₹144.75 (fresh Friday signal — BUY: 3.35× weekly, month 1.95×, ladder rising; stop ₹109.72; charges ₹0.0525)
2023-12-20  SUNDARMHLD  SELL ₹44.37 at stop ₹145.40 (+0.4%, charges ₹0.0460) — the cash goes back to work at the next Friday screen
2023-12-26  MMFL        BUY ₹45.73 at ₹1,023.60 (fresh Friday signal — BUY: 9.43× weekly, month 3.43×, ladder rising; stop ₹821.80; charges ₹0.0542)
2024-01-17  TIIL        SELL ₹75.89 at stop ₹2,337.00 (+109.3%, charges ₹0.0787) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹51.59 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0611)
2024-01-30  MMFL        SELL ₹40.65 at stop ₹912.05 (-10.9%, charges ₹0.0422) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹55.10 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0653)
2024-02-06  SUVENPHAR   SELL ₹46.77 at stop ₹623.20 (+22.2%, charges ₹0.0485) — the cash goes back to work at the next Friday screen
2024-02-09  ASTRAZEN    SELL ₹55.84 at stop ₹5,795.95 (+41.4%, charges ₹0.0579) — the cash goes back to work at the next Friday screen
2024-02-12  IOB         BUY ₹52.35 at ₹71.50 (fresh Friday signal — BUY: 7.81× weekly, month 2.91×, ladder rising; stop ₹38.71; charges ₹0.0620)
2024-02-12  UNICHEMLAB  BUY ₹52.51 at ₹520.00 (fresh Friday signal — BUY: 12.96× weekly, month 1.04×, ladder rising; stop ₹418.24; charges ₹0.0622)
2024-03-06  SHAREINDIA  SELL ₹50.58 at stop ₹357.20 (+19.1%, charges ₹0.0525) — the cash goes back to work at the next Friday screen
2024-03-11  SOLARINDS   BUY ₹54.35 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0644)
2024-03-11  TCI         SELL ₹44.00 at stop ₹790.40 (-20.0%, charges ₹0.0456) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹37.62 at stop ₹674.12 (-11.5%, charges ₹0.0390) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹51.72 at stop ₹666.47 (+0.5%, charges ₹0.0536) — the cash goes back to work at the next Friday screen
2024-03-18  FORCEMOT    BUY ₹52.35 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.0620)
2024-03-18  INDIGO      BUY ₹52.27 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0619)
2024-03-18  TRENT       BUY ₹32.55 at ₹2,709.27 (fresh Friday signal — ACCUMULATE: 1.86× weekly, month 1.33×, ladder rising; stop ₹2,395.27; charges ₹0.0386)
2024-03-27  ANANDRATHI  SELL ₹114.66 at stop ₹862.65 (+224.7%, charges ₹0.1189) — the cash goes back to work at the next Friday screen
2024-04-01  CENTURYTEX  BUY ₹34.26 at ₹1,660.00 (fresh Friday signal — BUY: 3.85× weekly, month 1.15×, ladder rising; stop ₹1,241.53; charges ₹0.0406)
2024-04-01  SHRIRAMFIN  BUY ₹50.76 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0601)
2024-04-01  TAX         FY2024 settled: ₹29.6491 paid (STCG ₹142.93 @20%, LTCG ₹8.50 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-13  JSWHL       SELL ₹47.47 at stop ₹6,280.45 (+33.6%, charges ₹0.0492) — the cash goes back to work at the next Friday screen
2024-05-21  KIRLOSBROS  BUY ₹47.47 at ₹1,844.00 (fresh Friday signal — BUY: 5.41× weekly, month 1.62×, ladder rising; stop ₹1,221.51; charges ₹0.0562)
2024-05-28  FORCEMOT    SELL ₹64.29 at stop ₹8,083.64 (+23.1%, charges ₹0.0667) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹55.25 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0655)
2024-06-04  CENTURYTEX  SELL ₹35.33 at stop ₹1,715.70 (+3.4%, charges ₹0.0366) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹47.18 at stop ₹441.77 (-6.8%, charges ₹0.0489) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹57.22 at stop ₹7,980.95 (+5.5%, charges ₹0.0594) — the cash goes back to work at the next Friday screen
2024-06-04  UNICHEMLAB  SELL ₹51.88 at stop ₹514.85 (-1.0%, charges ₹0.0538) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹52.29 at ₹783.00 (fresh Friday signal — BUY: 7.38× weekly, month 1.40×, ladder rising; stop ₹632.75; charges ₹0.0620)
2024-06-10  BECTORFOOD  BUY ₹43.68 at ₹298.88 (fresh Friday signal — BUY: 3.33× weekly, month 1.12×, ladder rising; stop ₹225.86; charges ₹0.0518)
2024-06-10  FIEMIND     BUY ₹52.46 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0622)
2024-06-10  UNOMINDA    BUY ₹52.20 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0618)
2024-07-19  UNOMINDA    SELL ₹52.72 at stop ₹981.87 (+1.2%, charges ₹0.0547) — the cash goes back to work at the next Friday screen
2024-07-22  TCI         BUY ₹52.58 at ₹943.95 (fresh Friday signal — ACCUMULATE: 3.64× weekly, month 1.04×, ladder rising; stop ₹866.40; charges ₹0.0623)
2024-07-22  TRENT       SELL ₹41.53 at stop ₹3,464.36 (+27.9%, charges ₹0.0431) — the cash goes back to work at the next Friday screen
2024-07-23  FIEMIND     SELL ₹49.87 at stop ₹1,257.56 (-4.7%, charges ₹0.0517) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹37.83 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0448)
2024-07-29  THYROCARE   BUY ₹53.71 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0636)
2024-08-02  BECTORFOOD  SELL ₹38.46 at stop ₹263.77 (-11.7%, charges ₹0.0399) — the cash goes back to work at the next Friday screen
2024-08-05  JUBLPHARMA  BUY ₹38.46 at ₹840.00 (fresh Friday signal — BUY: 9.28× weekly, month 2.22×, ladder rising; stop ₹675.64; charges ₹0.0456)
2024-08-05  KIRLOSBROS  SELL ₹51.05 at stop ₹1,987.46 (+7.8%, charges ₹0.0529) — the cash goes back to work at the next Friday screen
2024-08-12  ADANIPOWER  SELL ₹42.17 at stop ₹632.75 (-19.2%, charges ₹0.0437) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹51.05 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0605)
2024-08-16  CAMPUS      SELL ₹53.41 at stop ₹277.07 (-3.1%, charges ₹0.0554) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹51.11 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0606)
2024-08-19  VGUARD      BUY ₹44.47 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.0527)
2024-09-09  AVANTIFEED  SELL ₹35.17 at stop ₹650.13 (-6.8%, charges ₹0.0365) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹35.17 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0417)
2024-10-03  IOB         SELL ₹41.33 at stop ₹56.57 (-20.9%, charges ₹0.0429) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹35.57 at stop ₹420.24 (-19.8%, charges ₹0.0369) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹50.79 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0602)
2024-10-07  INDIGO      SELL ₹73.10 at stop ₹4,485.14 (+40.2%, charges ₹0.0758) — the cash goes back to work at the next Friday screen
2024-10-07  JUBLPHARMA  SELL ₹48.98 at stop ₹1,072.08 (+27.6%, charges ₹0.0508) — the cash goes back to work at the next Friday screen
2024-10-07  TCI         SELL ₹56.03 at stop ₹1,008.09 (+6.8%, charges ₹0.0581) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹54.35 at stop ₹796.15 (+1.4%, charges ₹0.0564) — the cash goes back to work at the next Friday screen
2024-10-14  AKZOINDIA   BUY ₹51.97 at ₹4,122.30 (fresh Friday signal — BUY: 2.58× weekly, month 1.14×, ladder rising; stop ₹3,444.70; charges ₹0.0616)
2024-10-14  BSE         BUY ₹51.66 at ₹4,536.00 (fresh Friday signal — BUY: 2.79× weekly, month 4.25×, ladder rising; stop ₹3,393.93; charges ₹0.0612)
2024-10-14  DBCORP      BUY ₹51.19 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0606)
2024-10-14  GANECOS     BUY ₹50.99 at ₹2,103.85 (fresh Friday signal — BUY: 3.56× weekly, month 1.32×, ladder rising; stop ₹1,646.57; charges ₹0.0604)
2024-10-14  SKIPPER     BUY ₹51.40 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0609)
2024-10-22  BASF        SELL ₹52.74 at stop ₹7,611.30 (+3.6%, charges ₹0.0547) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹43.83 at stop ₹302.08 (-14.2%, charges ₹0.0455) — the cash goes back to work at the next Friday screen
2024-10-28  CIGNITITEC  BUY ₹42.93 at ₹1,515.00 (fresh Friday signal — BUY: 9.95× weekly, month 1.36×, ladder rising; stop ₹1,308.67; charges ₹0.0509)
2024-10-28  COFORGE     BUY ₹42.80 at ₹1,543.10 (fresh Friday signal — BUY: 3.74× weekly, month 1.36×, ladder rising; stop ₹1,274.91; charges ₹0.0507)
2024-10-28  CUPID       SELL ₹50.26 at stop ₹158.66 (+31.1%, charges ₹0.0521) — the cash goes back to work at the next Friday screen
2024-11-04  CARERATING  BUY ₹49.35 at ₹1,510.00 (fresh Friday signal — BUY: surged 3.30× weekly on 2024-10-11 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹1,066.23; charges ₹0.1165)
2024-11-14  ASTRAZEN    SELL ₹46.62 at stop ₹6,854.77 (-7.9%, charges ₹0.1035) — the cash goes back to work at the next Friday screen
2024-11-18  CIGNITITEC  SELL ₹37.56 at stop ₹1,330.00 (-12.2%, charges ₹0.0834) — the cash goes back to work at the next Friday screen
2024-11-18  JSWHL       BUY ₹48.47 at ₹19,990.00 (fresh Friday signal — BUY: 3.46× weekly, month 4.62×, ladder rising; stop ₹8,434.53; charges ₹0.1144)
2024-11-25  GARFIBRES   BUY ₹48.83 at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹0.1153)
2024-12-17  SUPRIYA     SELL ₹69.19 at stop ₹717.25 (+35.8%, charges ₹0.1537) — the cash goes back to work at the next Friday screen
2024-12-23  AKZOINDIA   SELL ₹43.28 at stop ₹3,444.70 (-16.4%, charges ₹0.0961) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹48.70 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.1150)
2024-12-26  PRSMJOHNSN  SELL ₹27.87 at stop ₹170.55 (-20.5%, charges ₹0.0619) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹48.09 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.1135)
2024-12-30  KFINTECH    BUY ₹43.55 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.1028)
2025-01-09  GARFIBRES   SELL ₹42.17 at stop ₹829.35 (-13.2%, charges ₹0.0937) — the cash goes back to work at the next Friday screen
2025-01-09  KSL         SELL ₹43.08 at stop ₹1,059.30 (-11.1%, charges ₹0.0957) — the cash goes back to work at the next Friday screen
2025-01-10  GANECOS     SELL ₹42.31 at stop ₹1,751.78 (-16.7%, charges ₹0.0940) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹44.21 at stop ₹477.28 (-13.7%, charges ₹0.0982) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹44.25 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.1045)
2025-01-13  ANANTRAJ    BUY ₹44.13 at ₹879.10 (fresh Friday signal — BUY: 2.36× weekly, month 1.12×, ladder rising; stop ₹762.04; charges ₹0.1042)
2025-01-13  CARERATING  SELL ₹40.33 at stop ₹1,239.70 (-17.9%, charges ₹0.0896) — the cash goes back to work at the next Friday screen
2025-01-13  COFORGE     SELL ₹49.79 at stop ₹1,801.20 (+16.7%, charges ₹0.1106) — the cash goes back to work at the next Friday screen
2025-01-13  JISLJALEQS  BUY ₹43.85 at ₹72.00 (fresh Friday signal — ACCUMULATE: 1.79× weekly, month 1.09×, ladder rising; stop ₹62.58; charges ₹0.1035)
2025-01-13  LLOYDSME    BUY ₹39.53 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.0933)
2025-01-15  KFINTECH    SELL ₹33.25 at stop ₹1,159.14 (-23.3%, charges ₹0.0738) — the cash goes back to work at the next Friday screen
2025-01-20  HCG         BUY ₹45.38 at ₹504.95 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 1.41×, ladder rising; stop ₹429.63; charges ₹0.1071)
2025-01-20  PGIL        BUY ₹45.45 at ₹833.02 (fresh Friday signal — BUY: 1.74× weekly, month 1.23×, ladder rising; stop ₹705.52; charges ₹0.1073)
2025-01-21  PGIL        SELL ₹38.32 at stop ₹705.52 (-15.3%, charges ₹0.0851) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹36.96 at stop ₹700.36 (-16.1%, charges ₹0.0821) — the cash goes back to work at the next Friday screen
2025-01-27  ANANTRAJ    SELL ₹38.21 at stop ₹764.73 (-13.0%, charges ₹0.0849) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹41.27 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0974)
2025-01-28  LLOYDSME    SELL ₹34.35 at stop ₹1,258.75 (-12.7%, charges ₹0.0763) — the cash goes back to work at the next Friday screen
2025-02-03  AUBANK      BUY ₹42.85 at ₹595.00 (fresh Friday signal — ACCUMULATE: 2.57× weekly, month 1.06×, ladder rising; stop ₹516.80; charges ₹0.1012)
2025-02-03  ZENSARTECH  BUY ₹42.94 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.1014)
2025-02-12  JINDWORLD   SELL ₹43.93 at stop ₹374.11 (-8.2%, charges ₹0.0976) — the cash goes back to work at the next Friday screen
2025-02-12  JISLJALEQS  SELL ₹37.94 at stop ₹62.58 (-13.1%, charges ₹0.0843) — the cash goes back to work at the next Friday screen
2025-02-17  AUBANK      SELL ₹37.05 at stop ₹516.80 (-13.1%, charges ₹0.0823) — the cash goes back to work at the next Friday screen
2025-02-24  BAJAJFINSV  BUY ₹39.50 at ₹1,868.00 (fresh Friday signal — BUY: surged 1.73× weekly on 2025-01-31 (month 1.03×), ladder rising NOW — promoted from the ladder watch; stop ₹1,613.29; charges ₹0.0932)
2025-02-24  GODFRYPHLP  BUY ₹39.64 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.0936)
2025-02-28  BSE         SELL ₹56.24 at stop ₹4,954.63 (+9.2%, charges ₹0.1249) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹38.27 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0903)
2025-03-03  ZENSARTECH  SELL ₹32.85 at stop ₹727.84 (-23.1%, charges ₹0.0730) — the cash goes back to work at the next Friday screen
2025-03-05  BAJAJFINSV  SELL ₹37.05 at stop ₹1,760.35 (-5.8%, charges ₹0.0823) — the cash goes back to work at the next Friday screen
2025-03-10  AVANTIFEED  BUY ₹39.60 at ₹806.00 (fresh Friday signal — BUY: 2.82× weekly, month 1.23×, ladder rising; stop ₹648.95; charges ₹0.0935)
2025-03-10  GRWRHITECH  BUY ₹39.67 at ₹4,219.95 (fresh Friday signal — BUY: surged 2.69× weekly on 2025-02-14 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹3,504.00; charges ₹0.0937)
2025-03-24  INDIASHLTR  BUY ₹42.81 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.1011)
2025-03-24  KSCL        BUY ₹42.84 at ₹1,285.00 (fresh Friday signal — BUY: 3.75× weekly, month 1.42×, ladder rising; stop ₹978.55; charges ₹0.1011)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹55.04 / LT ₹0.00)
2025-04-03  GRWRHITECH  SELL ₹33.72 at stop ₹3,602.82 (-14.6%, charges ₹0.0749) — the cash goes back to work at the next Friday screen
2025-04-07  AVANTIFEED  SELL ₹31.74 at stop ₹648.95 (-19.5%, charges ₹0.0705) — the cash goes back to work at the next Friday screen
2025-04-07  COROMANDEL  BUY ₹41.12 at ₹1,870.00 (fresh Friday signal — BUY: surged 1.58× weekly on 2025-03-21 (month 1.48×), ladder rising NOW — promoted from the ladder watch; stop ₹1,849.08; charges ₹0.0971)
2025-04-07  INDIASHLTR  SELL ₹39.61 at stop ₹738.82 (-7.1%, charges ₹0.0880) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹43.62 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.1030)
2025-04-15  INDIASHLTR  BUY ₹36.36 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.0858)
2025-05-15  KSCL        SELL ₹44.29 at stop ₹1,334.75 (+3.9%, charges ₹0.0984) — the cash goes back to work at the next Friday screen
2025-05-19  CARERATING  BUY ₹44.29 at ₹1,527.50 (fresh Friday signal — BUY: 11.23× weekly, month 2.66×, ladder rising; stop ₹1,144.84; charges ₹0.1046)
2025-05-26  HCG         SELL ₹50.02 at stop ₹559.08 (+10.7%, charges ₹0.1111) — the cash goes back to work at the next Friday screen
2025-06-02  LICI        BUY ₹44.94 at ₹477.00 (fresh Friday signal — BUY: 6.84× weekly, month 1.25×, ladder rising; stop ₹399.00; charges ₹0.1061)
2025-06-27  COROMANDEL  SELL ₹49.18 at stop ₹2,246.75 (+20.1%, charges ₹0.1092) — the cash goes back to work at the next Friday screen
2025-06-30  ALKYLAMINE  BUY ₹45.93 at ₹2,263.00 (fresh Friday signal — BUY: 7.48× weekly, month 1.62×, ladder rising; stop ₹1,832.27; charges ₹0.1084)
2025-07-31  CARERATING  SELL ₹49.17 at stop ₹1,703.35 (+11.5%, charges ₹0.1092) — the cash goes back to work at the next Friday screen
2025-08-04  JSWHL       SELL ₹46.11 at stop ₹19,106.01 (-4.4%, charges ₹0.1024) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹47.68 at stop ₹1,814.78 (+25.2%, charges ₹0.1059) — the cash goes back to work at the next Friday screen
2025-08-04  PGHL        BUY ₹43.49 at ₹6,440.00 (fresh Friday signal — BUY: 6.30× weekly, month 2.58×, ladder rising; stop ₹5,320.00; charges ₹0.1027)
2025-08-07  ALKYLAMINE  SELL ₹42.18 at stop ₹2,087.62 (-7.7%, charges ₹0.0937) — the cash goes back to work at the next Friday screen
2025-08-07  LICI        SELL ₹41.10 at stop ₹438.21 (-8.1%, charges ₹0.0913) — the cash goes back to work at the next Friday screen
2025-08-11  CUMMINSIND  BUY ₹43.41 at ₹3,806.90 (fresh Friday signal — BUY: 1.98× weekly, month 1.12×, ladder rising; stop ₹3,307.43; charges ₹0.1025)
2025-08-11  DELHIVERY   BUY ₹43.39 at ₹464.65 (fresh Friday signal — BUY: 2.15× weekly, month 1.25×, ladder rising; stop ₹383.90; charges ₹0.1024)
2025-08-11  RAIN        BUY ₹43.46 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.1026)
2025-08-11  UPL         BUY ₹43.39 at ₹688.95 (fresh Friday signal — ACCUMULATE: 1.66× weekly, month 1.47×, ladder rising; stop ₹625.10; charges ₹0.1024)
2025-08-26  RAIN        SELL ₹38.78 at stop ₹143.64 (-10.4%, charges ₹0.0861) — the cash goes back to work at the next Friday screen
2025-09-01  MARUTI      BUY ₹44.46 at ₹14,790.00 (fresh Friday signal — BUY: 1.52× weekly, month 1.18×, ladder rising; stop ₹11,415.20; charges ₹0.1050)
2025-09-16  GODFRYPHLP  SELL ₹61.22 at stop ₹8,967.50 (+55.1%, charges ₹0.1360) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹43.56 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.75× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.1028)
2025-09-22  FLUOROCHEM  BUY ₹29.39 at ₹3,820.00 (fresh Friday signal — BUY: 5.40× weekly, month 2.64×, ladder rising; stop ₹3,396.25; charges ₹0.0694)
2025-09-25  INDIASHLTR  SELL ₹36.10 at stop ₹862.60 (-0.3%, charges ₹0.0802) — the cash goes back to work at the next Friday screen
2025-09-29  SUBROS      BUY ₹36.10 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0852)
2025-10-01  DELHIVERY   SELL ₹40.54 at stop ₹436.10 (-6.1%, charges ₹0.0900) — the cash goes back to work at the next Friday screen
2025-10-06  ASTRAMICRO  BUY ₹40.54 at ₹1,119.85 (fresh Friday signal — BUY: 3.17× weekly, month 1.83×, ladder rising; stop ₹1,026.00; charges ₹0.0957)
2025-10-14  SUBROS      SELL ₹33.23 at stop ₹1,046.90 (-7.5%, charges ₹0.0738) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹33.23 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0784)
2025-10-20  CREDITACC   SELL ₹61.60 at stop ₹1,274.42 (+49.9%, charges ₹0.1368) — the cash goes back to work at the next Friday screen
2025-10-27  PSB         BUY ₹42.11 at ₹30.80 (fresh Friday signal — BUY: 2.36× weekly, month 1.24×, ladder rising; stop ₹27.07; charges ₹0.0994)
2025-11-06  ASTRAMICRO  SELL ₹36.97 at stop ₹1,026.00 (-8.4%, charges ₹0.0821) — the cash goes back to work at the next Friday screen
2025-11-06  FDC         SELL ₹37.72 at stop ₹425.79 (-13.0%, charges ₹0.0838) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹39.92 at stop ₹5,938.45 (-7.8%, charges ₹0.0887) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹41.69 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.0984)
2025-11-10  CUB         BUY ₹41.90 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.0989)
2025-11-10  TDPOWERSYS  BUY ₹41.88 at ₹389.50 (fresh Friday signal — BUY: 3.09× weekly, month 2.39×, ladder rising; stop ₹276.78; charges ₹0.0989)
2025-11-20  ANANDRATHI  SELL ₹30.47 at stop ₹1,450.17 (-7.9%, charges ₹0.0677) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹39.92 at stop ₹976.41 (-3.8%, charges ₹0.0887) — the cash goes back to work at the next Friday screen
2025-11-24  FLUOROCHEM  SELL ₹26.13 at stop ₹3,412.02 (-10.7%, charges ₹0.0580) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹39.10 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0923)
2025-11-24  TDPOWERSYS  SELL ₹38.26 at stop ₹357.49 (-8.2%, charges ₹0.0850) — the cash goes back to work at the next Friday screen
2025-12-01  GRAVITA     BUY ₹41.91 at ₹1,825.10 (fresh Friday signal — BUY: 2.31× weekly, month 1.47×, ladder rising; stop ₹1,592.29; charges ₹0.0989)
2025-12-01  SANSERA     BUY ₹41.92 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.0989)
2025-12-03  PSB         SELL ₹39.53 at stop ₹29.05 (-5.7%, charges ₹0.0878) — the cash goes back to work at the next Friday screen
2025-12-08  KIRLOSENG   BUY ₹40.97 at ₹1,130.00 (fresh Friday signal — BUY: 1.67× weekly, month 2.31×, ladder rising; stop ₹886.54; charges ₹0.0967)
2026-01-06  CUMMINSIND  SELL ₹47.58 at stop ₹4,191.50 (+10.1%, charges ₹0.1057) — the cash goes back to work at the next Friday screen
2026-01-09  GRAVITA     SELL ₹38.37 at stop ₹1,678.56 (-8.0%, charges ₹0.0852) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹34.98 at stop ₹2,956.49 (-10.1%, charges ₹0.0777) — the cash goes back to work at the next Friday screen
2026-01-12  HINDCOPPER  BUY ₹40.95 at ₹532.00 (fresh Friday signal — BUY: surged 1.55× weekly on 2025-12-12 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹456.95; charges ₹0.0967)
2026-01-12  KIRLOSENG   SELL ₹41.17 at stop ₹1,140.95 (+1.0%, charges ₹0.0915) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹40.98 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.0967)
2026-01-19  RBA         BUY ₹41.17 at ₹67.50 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.51×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.0972)
2026-01-20  UPL         SELL ₹45.71 at stop ₹729.12 (+5.8%, charges ₹0.1015) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹39.74 at stop ₹748.60 (-8.5%, charges ₹0.0883) — the cash goes back to work at the next Friday screen
2026-01-23  MARUTI      SELL ₹46.86 at stop ₹15,657.90 (+5.9%, charges ₹0.1041) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹39.89 at stop ₹1,672.76 (-4.4%, charges ₹0.0886) — the cash goes back to work at the next Friday screen
2026-02-02  BRITANNIA   BUY ₹40.85 at ₹5,733.00 (fresh Friday signal — ACCUMULATE: 1.60× weekly, month 1.09×, ladder rising; stop ₹5,436.85; charges ₹0.0964)
2026-02-02  HINDALCO    BUY ₹40.75 at ₹905.70 (fresh Friday signal — BUY: 1.78× weekly, month 1.30×, ladder rising; stop ₹849.30; charges ₹0.0962)
2026-02-02  INDIANB     BUY ₹41.01 at ₹843.15 (fresh Friday signal — BUY: surged 1.85× weekly on 2026-01-02 (month 1.10×), ladder rising NOW — promoted from the ladder watch; stop ₹815.10; charges ₹0.0968)
2026-02-02  MCX         BUY ₹40.56 at ₹2,212.70 (fresh Friday signal — BUY: 2.10× weekly, month 1.32×, ladder rising; stop ₹2,132.75; charges ₹0.0957)
2026-02-02  TATASTEEL   BUY ₹40.95 at ₹185.38 (fresh Friday signal — BUY: 1.55× weekly, month 1.14×, ladder rising; stop ₹171.84; charges ₹0.0967)
2026-02-09  CEIGALL     BUY ₹26.14 at ₹297.00 (fresh Friday signal — BUY: 1.88× weekly, month 1.26×, ladder rising; stop ₹253.32; charges ₹0.0617)
2026-02-17  NATIONALUM  SELL ₹38.88 at stop ₹335.49 (-4.7%, charges ₹0.0864) — the cash goes back to work at the next Friday screen
2026-02-23  VESUVIUS    BUY ₹38.88 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.0918)
2026-03-04  CEIGALL     SELL ₹23.33 at stop ₹266.33 (-10.3%, charges ₹0.0518) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹41.25 at stop ₹251.43 (-1.1%, charges ₹0.0916) — the cash goes back to work at the next Friday screen
2026-03-09  SOLARINDS   BUY ₹23.33 at ₹15,250.00 (fresh Friday signal — BUY: 2.55× weekly, month 1.15×, ladder rising; stop ₹12,217.95; charges ₹0.0551)
2026-03-09  TATASTEEL   SELL ₹41.89 at stop ₹190.52 (+2.8%, charges ₹0.0931) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹40.51 at stop ₹528.63 (-0.6%, charges ₹0.0900) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹37.09 at stop ₹61.08 (-9.5%, charges ₹0.0824) — the cash goes back to work at the next Friday screen
2026-03-16  ABB         BUY ₹39.02 at ₹6,400.00 (fresh Friday signal — BUY: 1.80× weekly, month 1.92×, ladder rising; stop ₹5,486.25; charges ₹0.0921)
2026-03-16  J&KBANK     BUY ₹38.95 at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.95×, ladder rising; stop ₹103.27; charges ₹0.0919)
2026-03-16  JBCHEPHARM  BUY ₹38.87 at ₹2,136.00 (fresh Friday signal — BUY: surged 1.57× weekly on 2026-02-27 (month 1.33×), ladder rising NOW — promoted from the ladder watch; stop ₹1,875.30; charges ₹0.0918)
2026-03-16  NTPC        BUY ₹38.90 at ₹384.50 (fresh Friday signal — BUY: 1.64× weekly, month 1.11×, ladder rising; stop ₹345.90; charges ₹0.0918)
2026-03-23  HINDALCO    SELL ₹38.63 at stop ₹862.65 (-4.8%, charges ₹0.0858) — the cash goes back to work at the next Friday screen
2026-03-23  J&KBANK     SELL ₹35.42 at stop ₹110.67 (-8.6%, charges ₹0.0787) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹33.59 at stop ₹464.31 (-13.2%, charges ₹0.0746) — the cash goes back to work at the next Friday screen
2026-03-24  BRITANNIA   SELL ₹38.56 at stop ₹5,436.85 (-5.2%, charges ₹0.0857) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹36.54 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0863)
2026-03-30  INOXINDIA   BUY ₹36.35 at ₹1,185.00 (fresh Friday signal — BUY: 2.69× weekly, month 1.27×, ladder rising; stop ₹1,067.80; charges ₹0.0858)
2026-03-30  SOLARINDS   SELL ₹18.61 at stop ₹12,217.95 (-19.9%, charges ₹0.0413) — the cash goes back to work at the next Friday screen
2026-03-30  VTL         BUY ₹36.31 at ₹520.95 (fresh Friday signal — BUY: surged 1.53× weekly on 2026-02-27 (month 2.21×), ladder rising NOW — promoted from the ladder watch; stop ₹485.45; charges ₹0.0857)
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹72.77 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹23.54 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0556)
2026-04-06  THERMAX     BUY ₹37.05 at ₹3,295.80 (fresh Friday signal — ACCUMULATE: 2.18× weekly, month 1.22×, ladder rising; stop ₹2,897.50; charges ₹0.0875)
2026-04-30  INDIANB     SELL ₹39.46 at stop ₹815.10 (-3.3%, charges ₹0.0877) — the cash goes back to work at the next Friday screen
2026-05-04  GRSE        BUY ₹39.46 at ₹2,956.00 (fresh Friday signal — BUY: 4.44× weekly, month 1.64×, ladder rising; stop ₹2,318.95; charges ₹0.0932)
2026-05-13  INOXINDIA   SELL ₹41.90 at stop ₹1,372.18 (+15.8%, charges ₹0.0931) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹35.59 at stop ₹1,125.84 (-2.1%, charges ₹0.0791) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹40.41 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.0954)
2026-05-18  GRSE        SELL ₹34.37 at stop ₹2,586.30 (-12.5%, charges ₹0.0763) — the cash goes back to work at the next Friday screen
2026-05-18  NLCINDIA    BUY ₹37.09 at ₹351.55 (fresh Friday signal — BUY: 5.83× weekly, month 6.05×, ladder rising; stop ₹278.49; charges ₹0.0876)
2026-05-25  GLAND       BUY ₹34.37 at ₹2,369.80 (fresh Friday signal — BUY: 25.14× weekly, month 3.48×, ladder rising; stop ₹1,722.35; charges ₹0.0811)
2026-06-02  NTPC        SELL ₹36.74 at stop ₹364.80 (-5.1%, charges ₹0.0816) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹36.74 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0867)
2026-06-09  NLCINDIA    SELL ₹33.67 at stop ₹320.62 (-8.8%, charges ₹0.0748) — the cash goes back to work at the next Friday screen
2026-06-15  CAPLIPOINT  BUY ₹33.67 at ₹2,435.00 (fresh Friday signal — BUY: 4.02× weekly, month 3.90×, ladder rising; stop ₹1,852.50; charges ₹0.0795)
2026-07-07  MCX         SELL ₹47.77 at stop ₹2,618.20 (+18.3%, charges ₹0.1061) — the cash goes back to work at the next Friday screen
2026-07-13  GANESHHOU   BUY ₹41.98 at ₹860.50 (fresh Friday signal — BUY: 9.80× weekly, month 2.00×, ladder rising; stop ₹712.60; charges ₹0.0991)
2026-07-29  THERMAX     SELL ₹48.19 at stop ₹4,306.64 (+30.7%, charges ₹0.1070) — the cash goes back to work at the next Friday screen
2026-07-31  VTL         SELL ₹41.13 at stop ₹592.80 (+13.8%, charges ₹0.0914) — the cash goes back to work at the next Friday screen
2026-08-03  BLUESTONE   BUY ₹41.61 at ₹823.40 (fresh Friday signal — ACCUMULATE: 5.63× weekly, month 9.43×, ladder rising; stop ₹664.75; charges ₹0.0982)
2026-08-03  TMB         BUY ₹41.64 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.0983)
2026-09-10  ALKYLAMINE  SELL ₹45.18 at stop ₹1,920.99 (+12.3%, charges ₹0.1004) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹43.45 at stop ₹7,158.25 (+11.8%, charges ₹0.0965) — the cash goes back to work at the next Friday screen
2026-09-15  SUNDRMFAST  BUY ₹43.14 at ₹1,277.30 (fresh Friday signal — BUY: 3.14× weekly, month 1.81×, ladder rising; stop ₹1,127.74; charges ₹0.1018)
2026-09-21  AVALON      BUY ₹42.97 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.1014)
```
