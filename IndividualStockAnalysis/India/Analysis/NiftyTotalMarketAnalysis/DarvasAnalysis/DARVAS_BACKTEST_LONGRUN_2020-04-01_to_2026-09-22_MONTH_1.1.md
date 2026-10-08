# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 1388 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹503.96** | **+28.40% a year** |
| The same system before costs and taxes | ₹677.54 | +34.41% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹288.59 | +17.80% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹503.96** (+28.40% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 469 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹27.16** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹88.92**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹29.19 | ₹0.00 | ₹5.8379 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹69.50 | ₹54.27 | ₹20.6832 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹81.23 | ₹67.73 | ₹24.7120 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹188.41 | ₹0.00 | ₹37.6827 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹61.46 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹49.98 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹15.08 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 142.86 | +42.9% | +43.5% | +70.1% |
| 2021 (2021-12-31) | 320.54 | +124.4% | +133.7% | +26.2% |
| 2022 (2022-12-30) | 395.72 | +23.5% | +32.7% | +4.3% |
| 2023 (2023-12-29) | 550.02 | +39.0% | +49.6% | +20.0% |
| 2024 (2024-12-27) | 556.81 | +1.2% | +9.2% | +9.6% |
| 2025 (2025-12-26) | 514.03 | -7.7% | -6.0% | +9.4% |
| 2026 (2026-09-22) | 503.96 | -2.0% | -0.8% | -10.4% |

## What it took to earn it

- **Maximum drawdown: -29.9%** (peak 2024-05-24 → trough 2026-04-02, on weekly closes).
- **217 closed trades**: 103 winners (47%), average winner +37.4%, average loser -10.8%.
- Best closed trade KIRLFER +354.1%; worst COMPINFO -35.4%.
- Median holding period 64 days.
- Cash share of equity averaged 9% across all weeks (median 1%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

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
| 2021-12-31 | 320.54 | 4.12 | 10 |
| 2022-01-28 | 314.11 | 72.64 | 8 |
| 2022-02-25 | 288.49 | 106.58 | 6 |
| 2022-03-25 | 327.94 | 27.06 | 9 |
| 2022-04-29 | 343.95 | 23.34 | 9 |
| 2022-05-27 | 344.08 | 1.79 | 9 |
| 2022-06-24 | 332.90 | 28.38 | 8 |
| 2022-07-29 | 362.53 | 0.00 | 9 |
| 2022-08-26 | 385.13 | 0.00 | 9 |
| 2022-09-30 | 363.06 | 29.00 | 8 |
| 2022-10-28 | 377.30 | 0.00 | 9 |
| 2022-11-25 | 409.38 | 34.18 | 8 |
| 2022-12-30 | 395.72 | 57.23 | 8 |
| 2023-01-27 | 382.42 | 55.79 | 8 |
| 2023-02-24 | 387.72 | 0.00 | 10 |
| 2023-03-31 | 371.23 | 157.71 | 6 |
| 2023-04-28 | 369.83 | 36.65 | 9 |
| 2023-05-26 | 369.20 | 68.14 | 8 |
| 2023-06-30 | 382.05 | 0.00 | 10 |
| 2023-07-28 | 398.75 | 0.00 | 10 |
| 2023-08-25 | 443.37 | 0.00 | 10 |
| 2023-09-29 | 464.42 | 0.00 | 10 |
| 2023-10-27 | 454.99 | 164.78 | 6 |
| 2023-11-24 | 524.65 | 0.00 | 10 |
| 2023-12-29 | 550.02 | 0.00 | 10 |
| 2024-01-25 | 574.14 | 12.11 | 10 |
| 2024-02-23 | 595.72 | 0.00 | 10 |
| 2024-03-28 | 578.70 | 141.97 | 8 |
| 2024-04-26 | 595.01 | 0.00 | 10 |
| 2024-05-31 | 590.58 | 69.32 | 9 |
| 2024-06-28 | 576.09 | 0.00 | 10 |
| 2024-07-26 | 582.60 | 127.16 | 8 |
| 2024-08-30 | 574.58 | 0.00 | 10 |
| 2024-09-27 | 580.73 | 0.00 | 10 |
| 2024-10-25 | 518.26 | 145.10 | 7 |
| 2024-11-29 | 577.88 | 0.00 | 10 |
| 2024-12-27 | 556.81 | 103.52 | 8 |
| 2025-01-31 | 490.57 | 243.36 | 4 |
| 2025-02-28 | 457.26 | 199.42 | 5 |
| 2025-03-27 | 508.32 | 0.00 | 9 |
| 2025-04-25 | 539.49 | 0.00 | 9 |
| 2025-05-30 | 546.80 | 55.62 | 8 |
| 2025-06-27 | 560.09 | 49.91 | 8 |
| 2025-07-25 | 543.30 | 0.00 | 9 |
| 2025-08-29 | 536.89 | 46.08 | 9 |
| 2025-09-26 | 509.10 | 52.42 | 9 |
| 2025-10-31 | 509.41 | 61.56 | 9 |
| 2025-11-28 | 501.90 | 90.57 | 8 |
| 2025-12-26 | 514.03 | 0.00 | 10 |
| 2026-01-30 | 498.40 | 275.12 | 4 |
| 2026-02-27 | 481.17 | 0.00 | 10 |
| 2026-03-27 | 429.24 | 139.20 | 7 |
| 2026-04-30 | 483.97 | 0.53 | 10 |
| 2026-05-29 | 499.61 | 0.00 | 10 |
| 2026-06-25 | 490.42 | 12.12 | 9 |
| 2026-07-31 | 483.77 | 123.27 | 7 |
| 2026-08-28 | 509.30 | 22.22 | 9 |
| 2026-09-22 | 503.96 | 25.47 | 9 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| BLUESTONE | 2026-08-03 | 823.40 | 930.40 | 758.29 | +13.0% |
| CAPLIPOINT | 2026-06-15 | 2,435.00 | 2,777.30 | 2,376.52 | +14.1% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,392.00 | 1,242.60 | +40.7% |
| GANESHHOU | 2026-07-13 | 860.50 | 736.80 | 712.60 | -14.4% |
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
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| TV18BRDCST | 2022-01-31 | 58.90 | 2022-02-22 | 58.38 | -0.9% |
| COMPINFO | 2022-01-10 | 45.00 | 2022-02-24 | 29.08 | -35.4% |
| JSWISPL | 2022-01-24 | 37.50 | 2022-02-24 | 30.25 | -19.3% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| GNFC | 2022-02-14 | 553.00 | 2022-05-06 | 792.16 | +43.2% |
| ADANITRANS | 2021-03-30 | 896.00 | 2022-05-11 | 2,299.37 | +156.6% |
| SARDAEN | 2022-03-28 | 115.59 | 2022-05-11 | 104.88 | -9.3% |
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
| TIMETECHNO | 2022-05-16 | 91.25 | 2022-11-21 | 95.09 | +4.2% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| IRFC | 2022-11-28 | 32.00 | 2022-12-23 | 28.20 | -11.9% |
| RVNL | 2022-10-17 | 36.85 | 2022-12-26 | 60.57 | +64.4% |
| KSL | 2022-12-26 | 330.10 | 2023-01-27 | 328.23 | -0.6% |
| JINDWORLD | 2022-12-26 | 415.10 | 2023-02-01 | 389.50 | -6.2% |
| GICRE | 2022-12-26 | 157.00 | 2023-02-01 | 167.72 | +6.8% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| GRAVITA | 2023-01-30 | 493.40 | 2023-03-02 | 448.45 | -9.1% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| CHOLAFIN | 2023-02-06 | 777.55 | 2023-03-24 | 727.37 | -6.5% |
| JINDALSAW | 2023-02-06 | 65.22 | 2023-03-27 | 67.92 | +4.1% |
| MBAPL | 2022-02-21 | 50.00 | 2023-03-29 | 112.36 | +124.7% |
| CIGNITITEC | 2023-02-13 | 673.00 | 2023-03-29 | 705.14 | +4.8% |
| SONATSOFTW | 2023-03-06 | 400.75 | 2023-03-29 | 371.45 | -7.3% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| MUKANDLTD | 2023-01-02 | 136.70 | 2023-05-17 | 116.23 | -15.0% |
| GUJALKALI | 2023-05-02 | 688.15 | 2023-05-23 | 646.14 | -6.1% |
| DCAL | 2023-03-27 | 127.95 | 2023-05-24 | 115.42 | -9.8% |
| ANURAS | 2023-04-03 | 868.95 | 2023-07-03 | 1,007.67 | +16.0% |
| KSB | 2023-03-27 | 417.98 | 2023-07-12 | 407.74 | -2.4% |
| THANGAMAYL | 2023-05-29 | 1,344.00 | 2023-07-17 | 1,344.25 | +0.0% |
| GANESHHOUC | 2023-07-24 | 457.00 | 2023-08-14 | 418.62 | -8.4% |
| INGERRAND | 2023-04-03 | 2,690.00 | 2023-09-13 | 3,022.99 | +12.4% |
| SCHNEIDER | 2023-05-29 | 236.80 | 2023-10-23 | 315.45 | +33.2% |
| SJVN | 2023-09-18 | 75.35 | 2023-10-23 | 66.03 | -12.4% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| SHARDAMOTR | 2023-05-22 | 380.00 | 2023-10-25 | 465.07 | +22.4% |
| KRISHANA | 2023-10-30 | 49.86 | 2023-10-31 | 94.05 | +88.6% |
| NATCOPHARM | 2023-04-03 | 569.80 | 2023-11-01 | 771.40 | +35.4% |
| GENUSPOWER | 2023-07-10 | 162.85 | 2023-11-16 | 234.03 | +43.7% |
| SUNDARMHLD | 2023-11-06 | 144.75 | 2023-12-20 | 145.40 | +0.4% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| MMFL | 2023-12-26 | 1,023.60 | 2024-01-30 | 912.05 | -10.9% |
| ASTRAZEN | 2023-08-21 | 4,099.85 | 2024-02-09 | 5,795.95 | +41.4% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| TCI | 2024-02-05 | 987.60 | 2024-03-11 | 790.40 | -20.0% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| RATEGAIN | 2023-11-06 | 701.00 | 2024-03-13 | 730.99 | +4.3% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| ANANDRATHI | 2023-07-17 | 265.70 | 2024-03-27 | 862.65 | +224.7% |
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| SOLARINDS | 2023-11-20 | 7,500.00 | 2024-06-04 | 7,980.95 | +6.4% |
| BHEL | 2024-03-11 | 259.10 | 2024-06-04 | 251.68 | -2.9% |
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
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| PCBL | 2024-08-05 | 364.05 | 2024-10-18 | 476.85 | +31.0% |
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
| GRWRHITECH | 2024-11-18 | 4,320.00 | 2025-01-10 | 4,702.55 | +8.9% |
| COFORGE | 2024-10-28 | 1,543.10 | 2025-01-13 | 1,801.20 | +16.7% |
| ACE | 2025-01-13 | 1,325.05 | 2025-01-14 | 1,356.69 | +2.4% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| MOTILALOFS | 2024-10-21 | 1,021.95 | 2025-01-17 | 788.79 | -22.8% |
| PGIL | 2025-01-20 | 833.02 | 2025-01-21 | 705.52 | -15.3% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| ASHOKA | 2025-01-13 | 271.65 | 2025-01-24 | 262.67 | -3.3% |
| ANANTRAJ | 2025-01-13 | 879.10 | 2025-01-27 | 764.73 | -13.0% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| GRWRHITECH | 2025-03-10 | 4,219.95 | 2025-04-03 | 3,602.82 | -14.6% |
| AVANTIFEED | 2025-03-10 | 806.00 | 2025-04-07 | 648.95 | -19.5% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| KSCL | 2025-03-24 | 1,285.00 | 2025-05-15 | 1,334.75 | +3.9% |
| HCG | 2025-01-20 | 504.95 | 2025-05-26 | 559.08 | +10.7% |
| COROMANDEL | 2025-04-07 | 1,870.00 | 2025-06-27 | 2,246.75 | +20.1% |
| CARERATING | 2025-05-19 | 1,527.50 | 2025-07-31 | 1,703.35 | +11.5% |
| JSWHL | 2024-10-28 | 9,600.00 | 2025-08-04 | 19,106.01 | +99.0% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| LICI | 2025-06-02 | 477.00 | 2025-08-07 | 438.21 | -8.1% |
| ALKYLAMINE | 2025-06-30 | 2,263.00 | 2025-08-07 | 2,087.62 | -7.7% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| DELHIVERY | 2025-08-11 | 464.65 | 2025-10-01 | 436.10 | -6.1% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| BLACKBUCK | 2025-08-18 | 553.00 | 2025-10-28 | 642.20 | +16.1% |
| PGHL | 2025-08-04 | 6,440.00 | 2025-11-06 | 5,938.45 | -7.8% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| ASTRAMICRO | 2025-10-06 | 1,119.85 | 2025-11-06 | 1,026.00 | -8.4% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| TDPOWERSYS | 2025-11-10 | 389.50 | 2025-11-24 | 357.49 | -8.2% |
| PSB | 2025-10-27 | 30.80 | 2025-12-03 | 29.05 | -5.7% |
| CUMMINSIND | 2025-08-11 | 3,806.90 | 2026-01-06 | 4,191.50 | +10.1% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| KIRLOSENG | 2025-12-08 | 1,130.00 | 2026-01-12 | 1,140.95 | +1.0% |
| UPL | 2025-08-11 | 688.95 | 2026-01-20 | 729.12 | +5.8% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| MARUTI | 2025-09-01 | 14,790.00 | 2026-01-23 | 15,657.90 | +5.9% |
| RRKABEL | 2025-11-03 | 1,475.40 | 2026-01-23 | 1,358.31 | -7.9% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| CEIGALL | 2026-02-09 | 297.00 | 2026-03-04 | 266.33 | -10.3% |
| PTC | 2026-02-09 | 180.62 | 2026-03-04 | 156.89 | -13.1% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| TATASTEEL | 2026-02-02 | 185.38 | 2026-03-09 | 190.52 | +2.8% |
| HINDCOPPER | 2026-01-12 | 532.00 | 2026-03-12 | 528.63 | -0.6% |
| RBA | 2026-01-19 | 67.50 | 2026-03-12 | 61.08 | -9.5% |
| HINDALCO | 2026-02-02 | 905.70 | 2026-03-23 | 862.65 | -4.8% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-16 | 121.14 | 2026-03-23 | 110.67 | -8.6% |
| SOLARINDS | 2026-03-09 | 15,250.00 | 2026-03-30 | 12,217.95 | -19.9% |
| TORNTPOWER | 2026-03-09 | 1,451.00 | 2026-03-30 | 1,315.84 | -9.3% |
| INOXINDIA | 2026-03-30 | 1,185.00 | 2026-05-13 | 1,372.18 | +15.8% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| NTPC | 2026-03-16 | 384.50 | 2026-06-02 | 364.80 | -5.1% |
| E2E | 2026-02-16 | 2,464.00 | 2026-06-05 | 2,330.72 | -5.4% |
| NLCINDIA | 2026-05-18 | 351.55 | 2026-06-09 | 320.62 | -8.8% |
| MCX | 2026-02-02 | 2,212.70 | 2026-07-07 | 2,618.20 | +18.3% |
| THERMAX | 2026-04-06 | 3,295.80 | 2026-07-29 | 4,306.64 | +30.7% |
| VTL | 2026-03-30 | 520.95 | 2026-07-31 | 592.80 | +13.8% |
| MASTEK | 2026-08-03 | 1,874.80 | 2026-08-19 | 1,700.50 | -9.3% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-03-16 | 6,400.00 | 2026-09-15 | 7,158.25 | +11.8% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_MONTH_1.1.csv` beside this report (25573 events in all).*

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
2021-12-06  BSE         BUY ₹31.36 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0372)
2021-12-13  SUPRAJIT    SELL ₹27.48 at stop ₹391.40 (-13.8%, charges ₹0.0285) — the cash goes back to work at the next Friday screen
2021-12-16  RSYSTEMS    SELL ₹28.31 at stop ₹291.18 (-10.4%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹30.86 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0366)
2021-12-20  MINDAIND    BUY ₹30.65 at ₹1,026.00 (fresh Friday signal — BUY: 5.05× weekly, month 1.81×, ladder rising; stop ₹787.66; charges ₹0.0363)
2021-12-21  TCIEXP      SELL ₹28.86 at stop ₹2,039.74 (+11.4%, charges ₹0.0299) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹31.66 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0375)
2022-01-07  MINDAIND    SELL ₹32.44 at stop ₹1,088.41 (+6.1%, charges ₹0.0337) — the cash goes back to work at the next Friday screen
2022-01-10  COMPINFO    BUY ₹32.51 at ₹45.00 (fresh Friday signal — BUY: 4.39× weekly, month 5.27×, ladder rising; stop ₹25.44; charges ₹0.0385)
2022-01-21  LTTS        SELL ₹33.92 at stop ₹4,856.88 (+178.3%, charges ₹0.0352) — the cash goes back to work at the next Friday screen
2022-01-24  JSWISPL     BUY ₹30.86 at ₹37.50 (fresh Friday signal — BUY: 5.58× weekly, month 4.04×, ladder rising; stop ₹27.79; charges ₹0.0366)
2022-01-24  TVTODAY     SELL ₹31.25 at stop ₹311.68 (-2.7%, charges ₹0.0324) — the cash goes back to work at the next Friday screen
2022-01-25  SWANENERGY  SELL ₹34.28 at stop ₹162.64 (+8.5%, charges ₹0.0356) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹31.39 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0372)
2022-01-31  TV18BRDCST  BUY ₹31.37 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.0372)
2022-02-11  SHARDACROP  SELL ₹29.11 at stop ₹545.30 (-7.1%, charges ₹0.0302) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹17.70 at stop ₹424.65 (-10.2%, charges ₹0.0184) — the cash goes back to work at the next Friday screen
2022-02-14  GNFC        BUY ₹30.34 at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹0.0359)
2022-02-15  RAYMOND     SELL ₹35.81 at stop ₹679.35 (+14.0%, charges ₹0.0371) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹29.51 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0350)
2022-02-21  MBAPL       BUY ₹29.46 at ₹50.00 (fresh Friday signal — BUY: surged 3.35× weekly on 2022-01-28 (month 1.18×), ladder rising NOW — promoted from the ladder watch; stop ₹35.45; charges ₹0.0349)
2022-02-22  GREENLAM    SELL ₹26.56 at stop ₹313.67 (-13.7%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2022-02-22  TV18BRDCST  SELL ₹31.02 at stop ₹58.38 (-0.9%, charges ₹0.0322) — the cash goes back to work at the next Friday screen
2022-02-24  COMPINFO    SELL ₹20.96 at stop ₹29.08 (-35.4%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2022-02-24  JSWISPL     SELL ₹24.84 at stop ₹30.25 (-19.3%, charges ₹0.0258) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹29.32 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0347)
2022-02-28  SHANTIGEAR  BUY ₹29.45 at ₹185.30 (fresh Friday signal — BUY: surged 3.40× weekly on 2022-02-11 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹170.29; charges ₹0.0349)
2022-03-07  GTLINFRA    BUY ₹30.07 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0356)
2022-03-07  RAJMET      BUY ₹17.74 at ₹278.00 (fresh Friday signal — BUY: surged 6.93× weekly on 2022-02-18 (month 4.62×), ladder rising NOW — promoted from the ladder watch; stop ₹226.96; charges ₹0.0210)
2022-03-21  BSE         SELL ₹27.06 at stop ₹1,634.39 (-13.5%, charges ₹0.0281) — the cash goes back to work at the next Friday screen
2022-03-28  SARDAEN     BUY ₹27.06 at ₹115.59 (fresh Friday signal — BUY: surged 3.26× weekly on 2022-03-11 (month 1.13×), ladder rising NOW — promoted from the ladder watch; stop ₹97.38; charges ₹0.0321)
2022-04-01  ADANITRANS  TRIM 6.2% (₹1.58 at ₹2,421.45) to pay the tax bill
2022-04-01  CGCL        TRIM 6.2% (₹1.88 at ₹614.95) to pay the tax bill
2022-04-01  DANGEE      TRIM 6.2% (₹2.41 at ₹310.25) to pay the tax bill
2022-04-01  GNFC        TRIM 6.2% (₹2.94 at ₹862.75) to pay the tax bill
2022-04-01  GTLINFRA    TRIM 6.2% (₹1.71 at ₹1.55) to pay the tax bill
2022-04-01  JSWENERGY   TRIM 6.2% (₹2.37 at ₹253.45) to pay the tax bill
2022-04-01  MBAPL       TRIM 6.2% (₹2.93 at ₹80.05) to pay the tax bill
2022-04-01  RAJMET      TRIM 6.2% (₹1.39 at ₹349.70) to pay the tax bill
2022-04-01  SARDAEN     TRIM 6.2% (₹1.65 at ₹113.45) to pay the tax bill
2022-04-01  SHANTIGEAR  TRIM 6.2% (₹1.82 at ₹183.85) to pay the tax bill
2022-04-01  TAX         FY2022 settled: ₹20.6832 paid (STCG ₹69.50 @20%, LTCG ₹54.27 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-29  GTLINFRA    SELL ₹23.34 at stop ₹1.41 (-17.1%, charges ₹0.0242) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹23.34 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.0276)
2022-05-06  GNFC        SELL ₹40.66 at stop ₹792.16 (+43.2%, charges ₹0.0422) — the cash goes back to work at the next Friday screen
2022-05-09  COSMOFILMS  BUY ₹34.11 at ₹2,008.00 (fresh Friday signal — ACCUMULATE: 3.00× weekly, month 1.17×, ladder rising; stop ₹1,677.90; charges ₹0.0404)
2022-05-11  ADANITRANS  SELL ₹22.62 at stop ₹2,299.37 (+156.6%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2022-05-11  COSMOFILMS  SELL ₹28.44 at stop ₹1,677.90 (-16.4%, charges ₹0.0295) — the cash goes back to work at the next Friday screen
2022-05-11  MFL         SELL ₹19.95 at stop ₹1,225.50 (-14.3%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2022-05-11  SARDAEN     SELL ₹22.97 at stop ₹104.88 (-9.3%, charges ₹0.0238) — the cash goes back to work at the next Friday screen
2022-05-16  KRISHANA    BUY ₹32.94 at ₹67.96 (fresh Friday signal — ACCUMULATE: 1.67× weekly, month 1.86×, ladder rising; stop ₹54.77; charges ₹0.0390)
2022-05-16  TIMETECHNO  BUY ₹32.88 at ₹91.25 (fresh Friday signal — BUY: surged 5.09× weekly on 2022-04-22 (month 3.01×), ladder rising NOW — promoted from the ladder watch; stop ₹86.50; charges ₹0.0390)
2022-05-16  VBL         BUY ₹32.93 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0390)
2022-06-06  VBL         SELL ₹29.31 at stop ₹196.27 (-10.8%, charges ₹0.0304) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹31.10 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0368)
2022-06-16  KRISHANA    SELL ₹26.48 at stop ₹54.77 (-19.4%, charges ₹0.0275) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹26.48 at ₹950.15 (fresh Friday signal — BUY: surged 6.84× weekly on 2022-06-10 (month 1.49×), ladder rising NOW — promoted from the ladder watch; stop ₹706.80; charges ₹0.0314)
2022-06-20  JSWENERGY   SELL ₹28.38 at stop ₹201.99 (+146.8%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2022-06-27  GALAXYSURF  BUY ₹28.38 at ₹2,890.05 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 1.11×, ladder rising; stop ₹2,589.70; charges ₹0.0336)
2022-09-06  DANGEE      SELL ₹43.80 at stop ₹375.25 (+59.7%, charges ₹0.0454) — the cash goes back to work at the next Friday screen
2022-09-12  SHREECEM    BUY ₹38.23 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0453)
2022-09-15  RAJMET      SELL ₹21.45 at stop ₹359.30 (+29.2%, charges ₹0.0223) — the cash goes back to work at the next Friday screen
2022-09-19  JSWHL       BUY ₹27.02 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0320)
2022-09-29  GALAXYSURF  SELL ₹29.00 at stop ₹2,959.34 (+2.4%, charges ₹0.0301) — the cash goes back to work at the next Friday screen
2022-10-03  SUNDARMHLD  BUY ₹29.00 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹0.0344)
2022-10-11  SUNDARMHLD  SELL ₹25.78 at stop ₹92.20 (-10.9%, charges ₹0.0267) — the cash goes back to work at the next Friday screen
2022-10-17  RVNL        BUY ₹25.78 at ₹36.85 (fresh Friday signal — BUY: 4.04× weekly, month 1.42×, ladder rising; stop ₹31.21; charges ₹0.0305)
2022-11-03  APARINDS    SELL ₹37.78 at stop ₹1,358.50 (+43.0%, charges ₹0.0392) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹37.78 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0448)
2022-11-21  TIMETECHNO  SELL ₹34.18 at stop ₹95.09 (+4.2%, charges ₹0.0355) — the cash goes back to work at the next Friday screen
2022-11-28  IRFC        BUY ₹34.18 at ₹32.00 (fresh Friday signal — BUY: 6.87× weekly, month 11.74×, ladder rising; stop ₹23.09; charges ₹0.0405)
2022-12-21  ELECON      SELL ₹51.31 at stop ₹202.49 (+65.3%, charges ₹0.0532) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹51.39 at stop ₹345.56 (+86.5%, charges ₹0.0533) — the cash goes back to work at the next Friday screen
2022-12-23  IRFC        SELL ₹30.06 at stop ₹28.20 (-11.9%, charges ₹0.0312) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹37.66 at stop ₹139.84 (-0.1%, charges ₹0.0391) — the cash goes back to work at the next Friday screen
2022-12-26  GICRE       BUY ₹39.06 at ₹157.00 (fresh Friday signal — BUY: surged 4.73× weekly on 2022-12-02 (month 1.82×), ladder rising NOW — promoted from the ladder watch; stop ₹134.14; charges ₹0.0463)
2022-12-26  JINDWORLD   BUY ₹38.81 at ₹415.10 (fresh Friday signal — BUY: 3.67× weekly, month 1.21×, ladder rising; stop ₹362.90; charges ₹0.0460)
2022-12-26  KRISHANA    BUY ₹38.61 at ₹83.60 (fresh Friday signal — BUY: 3.70× weekly, month 2.29×, ladder rising; stop ₹75.36; charges ₹0.0458)
2022-12-26  KSL         BUY ₹38.97 at ₹330.10 (fresh Friday signal — BUY: surged 5.50× weekly on 2022-12-09 (month 2.50×), ladder rising NOW — promoted from the ladder watch; stop ₹328.23; charges ₹0.0462)
2022-12-26  RVNL        SELL ₹42.28 at stop ₹60.57 (+64.4%, charges ₹0.0439) — the cash goes back to work at the next Friday screen
2023-01-02  MUKANDLTD   BUY ₹40.10 at ₹136.70 (fresh Friday signal — BUY: 6.81× weekly, month 2.54×, ladder rising; stop ₹103.76; charges ₹0.0475)
2023-01-27  KSL         SELL ₹38.66 at stop ₹328.23 (-0.6%, charges ₹0.0401) — the cash goes back to work at the next Friday screen
2023-01-30  GRAVITA     BUY ₹38.41 at ₹493.40 (fresh Friday signal — BUY: 2.54× weekly, month 1.13×, ladder rising; stop ₹376.61; charges ₹0.0455)
2023-02-01  GICRE       SELL ₹41.64 at stop ₹167.72 (+6.8%, charges ₹0.0432) — the cash goes back to work at the next Friday screen
2023-02-01  JINDWORLD   SELL ₹36.34 at stop ₹389.50 (-6.2%, charges ₹0.0377) — the cash goes back to work at the next Friday screen
2023-02-06  CHOLAFIN    BUY ₹37.53 at ₹777.55 (fresh Friday signal — BUY: 2.87× weekly, month 1.34×, ladder rising; stop ₹661.25; charges ₹0.0445)
2023-02-06  JINDALSAW   BUY ₹37.55 at ₹65.22 (fresh Friday signal — BUY: 2.72× weekly, month 3.57×, ladder rising; stop ₹51.25; charges ₹0.0445)
2023-02-13  CIGNITITEC  BUY ₹20.27 at ₹673.00 (fresh Friday signal — BUY: 3.13× weekly, month 1.41×, ladder rising; stop ₹568.10; charges ₹0.0240)
2023-02-17  CGCL        SELL ₹32.46 at stop ₹704.95 (+17.6%, charges ₹0.0337) — the cash goes back to work at the next Friday screen
2023-02-20  TIIL        BUY ₹32.46 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0385)
2023-03-02  GRAVITA     SELL ₹34.83 at stop ₹448.45 (-9.1%, charges ₹0.0361) — the cash goes back to work at the next Friday screen
2023-03-06  SONATSOFTW  BUY ₹34.83 at ₹400.75 (fresh Friday signal — BUY: 3.29× weekly, month 4.54×, ladder rising; stop ₹325.85; charges ₹0.0413)
2023-03-20  KRISHANA    SELL ₹43.51 at stop ₹94.40 (+12.9%, charges ₹0.0451) — the cash goes back to work at the next Friday screen
2023-03-24  CHOLAFIN    SELL ₹35.03 at stop ₹727.37 (-6.5%, charges ₹0.0363) — the cash goes back to work at the next Friday screen
2023-03-27  DCAL        BUY ₹37.55 at ₹127.95 (fresh Friday signal — BUY: surged 6.76× weekly on 2023-02-24 (month 4.70×), ladder rising NOW — promoted from the ladder watch; stop ₹114.43; charges ₹0.0445)
2023-03-27  JINDALSAW   SELL ₹39.01 at stop ₹67.92 (+4.1%, charges ₹0.0405) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹37.62 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.61×, ladder rising; stop ₹372.21; charges ₹0.0446)
2023-03-29  CIGNITITEC  SELL ₹21.19 at stop ₹705.14 (+4.8%, charges ₹0.0220) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹61.93 at stop ₹112.36 (+124.7%, charges ₹0.0642) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹32.22 at stop ₹371.45 (-7.3%, charges ₹0.0334) — the cash goes back to work at the next Friday screen
2023-04-03  ANURAS      BUY ₹27.14 at ₹868.95 (fresh Friday signal — BUY: surged 2.13× weekly on 2023-03-10 (month 1.83×), ladder rising NOW — promoted from the ladder watch; stop ₹691.46; charges ₹0.0322)
2023-04-03  HAL         BUY ₹35.33 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.0419)
2023-04-03  INGERRAND   BUY ₹35.26 at ₹2,690.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2023-03-10 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹2,170.84; charges ₹0.0418)
2023-04-03  NATCOPHARM  BUY ₹35.26 at ₹569.80 (fresh Friday signal — ACCUMULATE: 1.84× weekly, month 1.46×, ladder rising; stop ₹494.24; charges ₹0.0418)
2023-04-03  TAX         FY2023 settled: ₹24.7120 paid (STCG ₹81.23 @20%, LTCG ₹67.73 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-24  SHREECEM    SELL ₹36.65 at stop ₹23,636.00 (-3.9%, charges ₹0.0380) — the cash goes back to work at the next Friday screen
2023-05-02  GUJALKALI   BUY ₹36.65 at ₹688.15 (fresh Friday signal — BUY: 22.10× weekly, month 1.42×, ladder rising; stop ₹590.90; charges ₹0.0434)
2023-05-17  MUKANDLTD   SELL ₹34.02 at stop ₹116.23 (-15.0%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2023-05-22  SHARDAMOTR  BUY ₹34.02 at ₹380.00 (fresh Friday signal — BUY: 9.54× weekly, month 2.31×, ladder rising; stop ₹342.95; charges ₹0.0403)
2023-05-23  GUJALKALI   SELL ₹34.34 at stop ₹646.14 (-6.1%, charges ₹0.0356) — the cash goes back to work at the next Friday screen
2023-05-24  DCAL        SELL ₹33.80 at stop ₹115.42 (-9.8%, charges ₹0.0351) — the cash goes back to work at the next Friday screen
2023-05-29  SCHNEIDER   BUY ₹31.32 at ₹236.80 (fresh Friday signal — BUY: 11.77× weekly, month 1.59×, ladder rising; stop ₹175.42; charges ₹0.0371)
2023-05-29  THANGAMAYL  BUY ₹36.81 at ₹1,344.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.50×, ladder rising; stop ₹1,116.30; charges ₹0.0436)
2023-07-03  ANURAS      SELL ₹31.40 at stop ₹1,007.67 (+16.0%, charges ₹0.0326) — the cash goes back to work at the next Friday screen
2023-07-10  GENUSPOWER  BUY ₹31.40 at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.48×, ladder rising; stop ₹99.51; charges ₹0.0372)
2023-07-12  KSB         SELL ₹36.62 at stop ₹407.74 (-2.4%, charges ₹0.0380) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹36.62 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0434)
2023-07-17  THANGAMAYL  SELL ₹36.74 at stop ₹1,344.25 (+0.0%, charges ₹0.0381) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹36.74 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.84×, ladder rising; stop ₹359.10; charges ₹0.0435)
2023-08-14  GANESHHOUC  SELL ₹33.58 at stop ₹418.62 (-8.4%, charges ₹0.0348) — the cash goes back to work at the next Friday screen
2023-08-21  ASTRAZEN    BUY ₹33.58 at ₹4,099.85 (fresh Friday signal — BUY: 6.03× weekly, month 2.40×, ladder rising; stop ₹3,562.50; charges ₹0.0398)
2023-09-13  INGERRAND   SELL ₹39.54 at stop ₹3,022.99 (+12.4%, charges ₹0.0410) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹39.54 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.67×, ladder rising; stop ₹58.28; charges ₹0.0468)
2023-10-23  SCHNEIDER   SELL ₹41.63 at stop ₹315.45 (+33.2%, charges ₹0.0432) — the cash goes back to work at the next Friday screen
2023-10-23  SJVN        SELL ₹34.57 at stop ₹66.03 (-12.4%, charges ₹0.0359) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹47.02 at stop ₹1,840.70 (+33.4%, charges ₹0.0488) — the cash goes back to work at the next Friday screen
2023-10-25  SHARDAMOTR  SELL ₹41.55 at stop ₹465.07 (+22.4%, charges ₹0.0431) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹45.39 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0538)
2023-10-30  KKCL        BUY ₹45.47 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0539)
2023-10-30  KRISHANA    BUY ₹28.49 at ₹49.86 (fresh Friday signal — BUY: surged 2.94× weekly on 2023-09-29 (month 1.67×), ladder rising NOW — promoted from the ladder watch; stop ₹94.05; charges ₹0.0338)
2023-10-30  SHAREINDIA  BUY ₹45.43 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0538)
2023-10-31  KRISHANA    SELL ₹53.62 at stop ₹94.05 (+88.6%, charges ₹0.0556) — the cash goes back to work at the next Friday screen
2023-11-01  NATCOPHARM  SELL ₹47.64 at stop ₹771.40 (+35.4%, charges ₹0.0494) — the cash goes back to work at the next Friday screen
2023-11-06  RATEGAIN    BUY ₹49.82 at ₹701.00 (fresh Friday signal — BUY: 2.09× weekly, month 1.19×, ladder rising; stop ₹549.53; charges ₹0.0590)
2023-11-06  SUNDARMHLD  BUY ₹49.73 at ₹144.75 (fresh Friday signal — BUY: 3.35× weekly, month 1.95×, ladder rising; stop ₹109.72; charges ₹0.0589)
2023-11-16  GENUSPOWER  SELL ₹45.02 at stop ₹234.03 (+43.7%, charges ₹0.0467) — the cash goes back to work at the next Friday screen
2023-11-20  SOLARINDS   BUY ₹46.73 at ₹7,500.00 (fresh Friday signal — BUY: 3.85× weekly, month 2.17×, ladder rising; stop ₹4,746.06; charges ₹0.0554)
2023-12-20  SUNDARMHLD  SELL ₹49.85 at stop ₹145.40 (+0.4%, charges ₹0.0517) — the cash goes back to work at the next Friday screen
2023-12-26  MMFL        BUY ₹49.85 at ₹1,023.60 (fresh Friday signal — BUY: 9.43× weekly, month 3.43×, ladder rising; stop ₹821.80; charges ₹0.0591)
2024-01-17  TIIL        SELL ₹67.78 at stop ₹2,337.00 (+109.3%, charges ₹0.0703) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹55.67 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0660)
2024-01-30  MMFL        SELL ₹44.32 at stop ₹912.05 (-10.9%, charges ₹0.0460) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹56.42 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0669)
2024-02-09  ASTRAZEN    SELL ₹47.36 at stop ₹5,795.95 (+41.4%, charges ₹0.0491) — the cash goes back to work at the next Friday screen
2024-02-12  IOB         BUY ₹47.36 at ₹71.50 (fresh Friday signal — BUY: 7.81× weekly, month 2.91×, ladder rising; stop ₹38.71; charges ₹0.0561)
2024-03-06  SHAREINDIA  SELL ₹53.97 at stop ₹357.20 (+19.1%, charges ₹0.0560) — the cash goes back to work at the next Friday screen
2024-03-11  BHEL        BUY ₹53.97 at ₹259.10 (fresh Friday signal — BUY: 3.01× weekly, month 1.67×, ladder rising; stop ₹188.78; charges ₹0.0639)
2024-03-11  TCI         SELL ₹45.06 at stop ₹790.40 (-20.0%, charges ₹0.0467) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹40.14 at stop ₹674.12 (-11.5%, charges ₹0.0416) — the cash goes back to work at the next Friday screen
2024-03-13  RATEGAIN    SELL ₹51.84 at stop ₹730.99 (+4.3%, charges ₹0.0538) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹55.81 at stop ₹666.47 (+0.5%, charges ₹0.0579) — the cash goes back to work at the next Friday screen
2024-03-18  FORCEMOT    BUY ₹56.45 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.0669)
2024-03-18  INDIGO      BUY ₹56.37 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0668)
2024-03-18  TRENT       BUY ₹56.70 at ₹2,709.27 (fresh Friday signal — ACCUMULATE: 1.86× weekly, month 1.33×, ladder rising; stop ₹2,395.27; charges ₹0.0672)
2024-03-27  ANANDRATHI  SELL ₹118.63 at stop ₹862.65 (+224.7%, charges ₹0.1231) — the cash goes back to work at the next Friday screen
2024-04-01  CENTURYTEX  BUY ₹49.59 at ₹1,660.00 (fresh Friday signal — BUY: 3.85× weekly, month 1.15×, ladder rising; stop ₹1,241.53; charges ₹0.0588)
2024-04-01  SHRIRAMFIN  BUY ₹54.70 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0648)
2024-04-01  TAX         FY2024 settled: ₹37.6827 paid (STCG ₹188.41 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-13  JSWHL       SELL ₹36.03 at stop ₹6,280.45 (+33.6%, charges ₹0.0374) — the cash goes back to work at the next Friday screen
2024-05-21  KIRLOSBROS  BUY ₹36.03 at ₹1,844.00 (fresh Friday signal — BUY: 5.41× weekly, month 1.62×, ladder rising; stop ₹1,221.51; charges ₹0.0427)
2024-05-28  FORCEMOT    SELL ₹69.32 at stop ₹8,083.64 (+23.1%, charges ₹0.0719) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹61.00 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0723)
2024-06-04  BHEL        SELL ₹52.31 at stop ₹251.68 (-2.9%, charges ₹0.0543) — the cash goes back to work at the next Friday screen
2024-06-04  CENTURYTEX  SELL ₹51.14 at stop ₹1,715.70 (+3.4%, charges ₹0.0530) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹50.84 at stop ₹441.77 (-6.8%, charges ₹0.0527) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹49.61 at stop ₹7,980.95 (+6.4%, charges ₹0.0515) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹57.06 at ₹783.00 (fresh Friday signal — BUY: 7.38× weekly, month 1.40×, ladder rising; stop ₹632.75; charges ₹0.0676)
2024-06-10  BECTORFOOD  BUY ₹40.96 at ₹298.88 (fresh Friday signal — BUY: 3.33× weekly, month 1.12×, ladder rising; stop ₹225.86; charges ₹0.0485)
2024-06-10  FIEMIND     BUY ₹57.25 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0678)
2024-06-10  UNOMINDA    BUY ₹56.96 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0675)
2024-07-19  UNOMINDA    SELL ₹57.53 at stop ₹981.87 (+1.2%, charges ₹0.0597) — the cash goes back to work at the next Friday screen
2024-07-22  HBLPOWER    BUY ₹57.13 at ₹585.00 (fresh Friday signal — BUY: 3.57× weekly, month 1.41×, ladder rising; stop ₹522.78; charges ₹0.0677)
2024-07-22  TRENT       SELL ₹72.34 at stop ₹3,464.36 (+27.9%, charges ₹0.0750) — the cash goes back to work at the next Friday screen
2024-07-23  FIEMIND     SELL ₹54.42 at stop ₹1,257.56 (-4.7%, charges ₹0.0564) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹58.22 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0690)
2024-07-29  THYROCARE   BUY ₹58.27 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0690)
2024-08-02  BECTORFOOD  SELL ₹36.06 at stop ₹263.77 (-11.7%, charges ₹0.0374) — the cash goes back to work at the next Friday screen
2024-08-05  KIRLOSBROS  SELL ₹38.74 at stop ₹1,987.46 (+7.8%, charges ₹0.0402) — the cash goes back to work at the next Friday screen
2024-08-05  PCBL        BUY ₹46.74 at ₹364.05 (fresh Friday signal — BUY: 10.04× weekly, month 2.68×, ladder rising; stop ₹246.00; charges ₹0.0554)
2024-08-12  ADANIPOWER  SELL ₹46.01 at stop ₹632.75 (-19.2%, charges ₹0.0477) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹38.74 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0459)
2024-08-16  CAMPUS      SELL ₹58.96 at stop ₹277.07 (-3.1%, charges ₹0.0612) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹56.56 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0670)
2024-08-19  VGUARD      BUY ₹48.41 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.0574)
2024-09-09  AVANTIFEED  SELL ₹54.13 at stop ₹650.13 (-6.8%, charges ₹0.0561) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹54.13 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0641)
2024-10-03  IOB         SELL ₹37.39 at stop ₹56.57 (-20.9%, charges ₹0.0388) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹38.72 at stop ₹420.24 (-19.8%, charges ₹0.0402) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹55.24 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0655)
2024-10-07  INDIGO      SELL ₹78.83 at stop ₹4,485.14 (+40.2%, charges ₹0.0818) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹58.97 at stop ₹796.15 (+1.4%, charges ₹0.0612) — the cash goes back to work at the next Friday screen
2024-10-14  DBCORP      BUY ₹55.94 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0663)
2024-10-14  GANECOS     BUY ₹55.72 at ₹2,103.85 (fresh Friday signal — BUY: 3.56× weekly, month 1.32×, ladder rising; stop ₹1,646.57; charges ₹0.0660)
2024-10-14  SKIPPER     BUY ₹47.00 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0557)
2024-10-18  PCBL        SELL ₹61.09 at stop ₹476.85 (+31.0%, charges ₹0.0634) — the cash goes back to work at the next Friday screen
2024-10-21  MOTILALOFS  BUY ₹54.86 at ₹1,021.95 (fresh Friday signal — BUY: 7.74× weekly, month 5.64×, ladder rising; stop ₹656.59; charges ₹0.0650)
2024-10-22  BASF        SELL ₹40.03 at stop ₹7,611.30 (+3.6%, charges ₹0.0415) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹47.90 at stop ₹302.08 (-14.2%, charges ₹0.0497) — the cash goes back to work at the next Friday screen
2024-10-25  HBLPOWER    SELL ₹50.94 at stop ₹522.78 (-10.6%, charges ₹0.0528) — the cash goes back to work at the next Friday screen
2024-10-28  CIGNITITEC  BUY ₹45.95 at ₹1,515.00 (fresh Friday signal — BUY: 9.95× weekly, month 1.36×, ladder rising; stop ₹1,308.67; charges ₹0.0544)
2024-10-28  COFORGE     BUY ₹45.80 at ₹1,543.10 (fresh Friday signal — BUY: 3.74× weekly, month 1.36×, ladder rising; stop ₹1,274.91; charges ₹0.0543)
2024-10-28  CUPID       SELL ₹59.39 at stop ₹158.66 (+31.1%, charges ₹0.0616) — the cash goes back to work at the next Friday screen
2024-10-28  JSWHL       BUY ₹45.80 at ₹9,600.00 (fresh Friday signal — BUY: 3.86× weekly, month 1.32×, ladder rising; stop ₹7,629.63; charges ₹0.0543)
2024-11-04  AKZOINDIA   BUY ₹52.69 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.1244)
2024-11-14  ASTRAZEN    SELL ₹50.70 at stop ₹6,854.77 (-7.9%, charges ₹0.1126) — the cash goes back to work at the next Friday screen
2024-11-18  CIGNITITEC  SELL ₹40.20 at stop ₹1,330.00 (-12.2%, charges ₹0.0893) — the cash goes back to work at the next Friday screen
2024-11-18  GRWRHITECH  BUY ₹55.40 at ₹4,320.00 (fresh Friday signal — BUY: 2.02× weekly, month 1.17×, ladder rising; stop ₹3,235.65; charges ₹0.1308)
2024-11-25  GARFIBRES   BUY ₹49.75 at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹0.1174)
2024-12-17  SUPRIYA     SELL ₹76.58 at stop ₹717.25 (+35.8%, charges ₹0.1701) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹55.69 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.1315)
2024-12-26  PRSMJOHNSN  SELL ₹42.89 at stop ₹170.55 (-20.5%, charges ₹0.0953) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹39.74 at stop ₹3,423.18 (-24.2%, charges ₹0.0883) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹55.62 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.1313)
2024-12-30  KFINTECH    BUY ₹47.90 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.1131)
2025-01-09  GARFIBRES   SELL ₹42.96 at stop ₹829.35 (-13.2%, charges ₹0.0954) — the cash goes back to work at the next Friday screen
2025-01-09  KSL         SELL ₹49.26 at stop ₹1,059.30 (-11.1%, charges ₹0.1094) — the cash goes back to work at the next Friday screen
2025-01-10  GANECOS     SELL ₹46.24 at stop ₹1,751.78 (-16.7%, charges ₹0.1027) — the cash goes back to work at the next Friday screen
2025-01-10  GRWRHITECH  SELL ₹60.03 at stop ₹4,702.55 (+8.9%, charges ₹0.1333) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹40.43 at stop ₹477.28 (-13.7%, charges ₹0.0898) — the cash goes back to work at the next Friday screen
2025-01-13  ACE         BUY ₹50.10 at ₹1,325.05 (fresh Friday signal — BUY: surged 3.80× weekly on 2024-12-20 (month 1.17×), ladder rising NOW — promoted from the ladder watch; stop ₹1,356.69; charges ₹0.1183)
2025-01-13  AEGISLOG    BUY ₹50.82 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.1200)
2025-01-13  ANANTRAJ    BUY ₹50.68 at ₹879.10 (fresh Friday signal — BUY: 2.36× weekly, month 1.12×, ladder rising; stop ₹762.04; charges ₹0.1196)
2025-01-13  ASHOKA      BUY ₹36.96 at ₹271.65 (fresh Friday signal — BUY: surged 1.88× weekly on 2024-12-13 (month 1.31×), ladder rising NOW — promoted from the ladder watch; stop ₹262.67; charges ₹0.0873)
2025-01-13  COFORGE     SELL ₹53.28 at stop ₹1,801.20 (+16.7%, charges ₹0.1183) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹50.36 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.1189)
2025-01-14  ACE         SELL ₹51.06 at stop ₹1,356.69 (+2.4%, charges ₹0.1134) — the cash goes back to work at the next Friday screen
2025-01-15  KFINTECH    SELL ₹36.56 at stop ₹1,159.14 (-23.3%, charges ₹0.0812) — the cash goes back to work at the next Friday screen
2025-01-17  MOTILALOFS  SELL ₹42.20 at stop ₹788.79 (-22.8%, charges ₹0.0937) — the cash goes back to work at the next Friday screen
2025-01-20  HCG         BUY ₹50.47 at ₹504.95 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 1.41×, ladder rising; stop ₹429.63; charges ₹0.1191)
2025-01-20  PGIL        BUY ₹50.54 at ₹833.02 (fresh Friday signal — BUY: 1.74× weekly, month 1.23×, ladder rising; stop ₹705.52; charges ₹0.1193)
2025-01-21  PGIL        SELL ₹42.61 at stop ₹705.52 (-15.3%, charges ₹0.0946) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹42.45 at stop ₹700.36 (-16.1%, charges ₹0.0943) — the cash goes back to work at the next Friday screen
2025-01-24  ASHOKA      SELL ₹35.58 at stop ₹262.67 (-3.3%, charges ₹0.0790) — the cash goes back to work at the next Friday screen
2025-01-27  ANANTRAJ    SELL ₹43.89 at stop ₹764.73 (-13.0%, charges ₹0.0975) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹47.02 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.1110)
2025-01-28  LLOYDSME    SELL ₹43.76 at stop ₹1,258.75 (-12.7%, charges ₹0.0972) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹48.86 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.1153)
2025-02-12  JINDWORLD   SELL ₹50.81 at stop ₹374.11 (-8.2%, charges ₹0.1129) — the cash goes back to work at the next Friday screen
2025-02-24  GODFRYPHLP  BUY ₹45.89 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.1083)
2025-03-03  NH          BUY ₹45.42 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.1072)
2025-03-03  ZENSARTECH  SELL ₹37.38 at stop ₹727.84 (-23.1%, charges ₹0.0830) — the cash goes back to work at the next Friday screen
2025-03-10  AVANTIFEED  BUY ₹47.76 at ₹806.00 (fresh Friday signal — BUY: 2.82× weekly, month 1.23×, ladder rising; stop ₹648.95; charges ₹0.1127)
2025-03-10  GRWRHITECH  BUY ₹47.85 at ₹4,219.95 (fresh Friday signal — BUY: surged 2.69× weekly on 2025-02-14 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹3,504.00; charges ₹0.1130)
2025-03-24  INDIASHLTR  BUY ₹52.24 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.1233)
2025-03-24  KSCL        BUY ₹43.53 at ₹1,285.00 (fresh Friday signal — BUY: 3.75× weekly, month 1.42×, ladder rising; stop ₹978.55; charges ₹0.1028)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹61.46 / LT ₹0.00)
2025-04-03  GRWRHITECH  SELL ₹40.67 at stop ₹3,602.82 (-14.6%, charges ₹0.0903) — the cash goes back to work at the next Friday screen
2025-04-07  AVANTIFEED  SELL ₹38.28 at stop ₹648.95 (-19.5%, charges ₹0.0850) — the cash goes back to work at the next Friday screen
2025-04-07  COROMANDEL  BUY ₹40.67 at ₹1,870.00 (fresh Friday signal — BUY: surged 1.58× weekly on 2025-03-21 (month 1.48×), ladder rising NOW — promoted from the ladder watch; stop ₹1,849.08; charges ₹0.0960)
2025-04-07  INDIASHLTR  SELL ₹48.33 at stop ₹738.82 (-7.1%, charges ₹0.1073) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹52.84 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.1247)
2025-04-15  INDIASHLTR  BUY ₹33.76 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.0797)
2025-05-15  KSCL        SELL ₹45.01 at stop ₹1,334.75 (+3.9%, charges ₹0.1000) — the cash goes back to work at the next Friday screen
2025-05-19  CARERATING  BUY ₹45.01 at ₹1,527.50 (fresh Friday signal — BUY: 11.23× weekly, month 2.66×, ladder rising; stop ₹1,144.84; charges ₹0.1063)
2025-05-26  HCG         SELL ₹55.62 at stop ₹559.08 (+10.7%, charges ₹0.1235) — the cash goes back to work at the next Friday screen
2025-06-02  LICI        BUY ₹54.34 at ₹477.00 (fresh Friday signal — BUY: 6.84× weekly, month 1.25×, ladder rising; stop ₹399.00; charges ₹0.1283)
2025-06-27  COROMANDEL  SELL ₹48.64 at stop ₹2,246.75 (+20.1%, charges ₹0.1080) — the cash goes back to work at the next Friday screen
2025-06-30  ALKYLAMINE  BUY ₹49.91 at ₹2,263.00 (fresh Friday signal — BUY: 7.48× weekly, month 1.62×, ladder rising; stop ₹1,832.27; charges ₹0.1178)
2025-07-31  CARERATING  SELL ₹49.96 at stop ₹1,703.35 (+11.5%, charges ₹0.1110) — the cash goes back to work at the next Friday screen
2025-08-04  JSWHL       SELL ₹90.85 at stop ₹19,106.01 (+99.0%, charges ₹0.2018) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹56.58 at stop ₹1,814.78 (+25.2%, charges ₹0.1257) — the cash goes back to work at the next Friday screen
2025-08-04  PGHL        BUY ₹49.96 at ₹6,440.00 (fresh Friday signal — BUY: 6.30× weekly, month 2.58×, ladder rising; stop ₹5,320.00; charges ₹0.1179)
2025-08-07  ALKYLAMINE  SELL ₹45.84 at stop ₹2,087.62 (-7.7%, charges ₹0.1018) — the cash goes back to work at the next Friday screen
2025-08-07  LICI        SELL ₹49.69 at stop ₹438.21 (-8.1%, charges ₹0.1104) — the cash goes back to work at the next Friday screen
2025-08-11  CUMMINSIND  BUY ₹51.58 at ₹3,806.90 (fresh Friday signal — BUY: 1.98× weekly, month 1.12×, ladder rising; stop ₹3,307.43; charges ₹0.1218)
2025-08-11  DELHIVERY   BUY ₹51.56 at ₹464.65 (fresh Friday signal — BUY: 2.15× weekly, month 1.25×, ladder rising; stop ₹383.90; charges ₹0.1217)
2025-08-11  RAIN        BUY ₹51.64 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.1219)
2025-08-11  UPL         BUY ₹51.55 at ₹688.95 (fresh Friday signal — ACCUMULATE: 1.66× weekly, month 1.47×, ladder rising; stop ₹625.10; charges ₹0.1217)
2025-08-18  BLACKBUCK   BUY ₹36.62 at ₹553.00 (fresh Friday signal — ACCUMULATE: 3.19× weekly, month 4.96×, ladder rising; stop ₹473.20; charges ₹0.0865)
2025-08-26  RAIN        SELL ₹46.08 at stop ₹143.64 (-10.4%, charges ₹0.1023) — the cash goes back to work at the next Friday screen
2025-09-01  MARUTI      BUY ₹46.08 at ₹14,790.00 (fresh Friday signal — BUY: 1.52× weekly, month 1.18×, ladder rising; stop ₹11,415.20; charges ₹0.1088)
2025-09-16  GODFRYPHLP  SELL ₹70.88 at stop ₹8,967.50 (+55.1%, charges ₹0.1574) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹51.98 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.75× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.1227)
2025-09-25  INDIASHLTR  SELL ₹33.52 at stop ₹862.60 (-0.3%, charges ₹0.0744) — the cash goes back to work at the next Friday screen
2025-09-29  SUBROS      BUY ₹50.63 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.1195)
2025-10-01  DELHIVERY   SELL ₹48.17 at stop ₹436.10 (-6.1%, charges ₹0.1070) — the cash goes back to work at the next Friday screen
2025-10-06  ASTRAMICRO  BUY ₹49.96 at ₹1,119.85 (fresh Friday signal — BUY: 3.17× weekly, month 1.83×, ladder rising; stop ₹1,026.00; charges ₹0.1179)
2025-10-14  SUBROS      SELL ₹46.61 at stop ₹1,046.90 (-7.5%, charges ₹0.1035) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹46.61 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.1100)
2025-10-20  CREDITACC   SELL ₹70.17 at stop ₹1,274.42 (+49.9%, charges ₹0.1559) — the cash goes back to work at the next Friday screen
2025-10-27  PSB         BUY ₹50.94 at ₹30.80 (fresh Friday signal — BUY: 2.36× weekly, month 1.24×, ladder rising; stop ₹27.07; charges ₹0.1203)
2025-10-28  BLACKBUCK   SELL ₹42.33 at stop ₹642.20 (+16.1%, charges ₹0.0940) — the cash goes back to work at the next Friday screen
2025-11-03  RRKABEL     BUY ₹51.15 at ₹1,475.40 (fresh Friday signal — BUY: 11.98× weekly, month 1.21×, ladder rising; stop ₹1,122.52; charges ₹0.1208)
2025-11-06  ASTRAMICRO  SELL ₹45.56 at stop ₹1,026.00 (-8.4%, charges ₹0.1012) — the cash goes back to work at the next Friday screen
2025-11-06  FDC         SELL ₹45.00 at stop ₹425.79 (-13.0%, charges ₹0.0999) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹45.86 at stop ₹5,938.45 (-7.8%, charges ₹0.1019) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹49.85 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.1177)
2025-11-10  CUB         BUY ₹50.10 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.1183)
2025-11-10  TDPOWERSYS  BUY ₹46.88 at ₹389.50 (fresh Friday signal — BUY: 3.09× weekly, month 2.39×, ladder rising; stop ₹276.78; charges ₹0.1107)
2025-11-20  ANANDRATHI  SELL ₹42.73 at stop ₹1,450.17 (-7.9%, charges ₹0.0949) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹47.74 at stop ₹976.41 (-3.8%, charges ₹0.1060) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹42.73 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.1009)
2025-11-24  TDPOWERSYS  SELL ₹42.83 at stop ₹357.49 (-8.2%, charges ₹0.0951) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹50.44 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.33×, ladder rising; stop ₹535.37; charges ₹0.1191)
2025-12-01  SANSERA     BUY ₹40.14 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.0947)
2025-12-03  PSB         SELL ₹47.83 at stop ₹29.05 (-5.7%, charges ₹0.1062) — the cash goes back to work at the next Friday screen
2025-12-08  KIRLOSENG   BUY ₹47.83 at ₹1,130.00 (fresh Friday signal — BUY: 1.67× weekly, month 2.31×, ladder rising; stop ₹886.54; charges ₹0.1129)
2026-01-06  CUMMINSIND  SELL ₹56.54 at stop ₹4,191.50 (+10.1%, charges ₹0.1256) — the cash goes back to work at the next Friday screen
2026-01-08  EUREKAFORB  SELL ₹44.54 at stop ₹589.10 (-11.3%, charges ₹0.0989) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹38.23 at stop ₹2,956.49 (-10.1%, charges ₹0.0849) — the cash goes back to work at the next Friday screen
2026-01-12  HINDCOPPER  BUY ₹49.39 at ₹532.00 (fresh Friday signal — BUY: surged 1.55× weekly on 2025-12-12 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹456.95; charges ₹0.1166)
2026-01-12  KIRLOSENG   SELL ₹48.07 at stop ₹1,140.95 (+1.0%, charges ₹0.1068) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹49.42 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.1167)
2026-01-19  RBA         BUY ₹49.54 at ₹67.50 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.51×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.1169)
2026-01-20  UPL         SELL ₹54.31 at stop ₹729.12 (+5.8%, charges ₹0.1206) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹48.14 at stop ₹748.60 (-8.5%, charges ₹0.1069) — the cash goes back to work at the next Friday screen
2026-01-23  MARUTI      SELL ₹48.56 at stop ₹15,657.90 (+5.9%, charges ₹0.1079) — the cash goes back to work at the next Friday screen
2026-01-23  RRKABEL     SELL ₹46.88 at stop ₹1,358.31 (-7.9%, charges ₹0.1041) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹38.20 at stop ₹1,672.76 (-4.4%, charges ₹0.0848) — the cash goes back to work at the next Friday screen
2026-02-02  HINDALCO    BUY ₹48.82 at ₹905.70 (fresh Friday signal — BUY: 1.78× weekly, month 1.30×, ladder rising; stop ₹849.30; charges ₹0.1153)
2026-02-02  MCX         BUY ₹48.60 at ₹2,212.70 (fresh Friday signal — BUY: 2.10× weekly, month 1.32×, ladder rising; stop ₹2,132.75; charges ₹0.1147)
2026-02-02  TATASTEEL   BUY ₹48.95 at ₹185.38 (fresh Friday signal — BUY: 1.55× weekly, month 1.14×, ladder rising; stop ₹171.84; charges ₹0.1155)
2026-02-09  CEIGALL     BUY ₹49.84 at ₹297.00 (fresh Friday signal — BUY: 1.88× weekly, month 1.26×, ladder rising; stop ₹253.32; charges ₹0.1176)
2026-02-09  PTC         BUY ₹49.65 at ₹180.62 (fresh Friday signal — BUY: surged 3.24× weekly on 2026-01-30 (month 1.13×), ladder rising NOW — promoted from the ladder watch; stop ₹156.89; charges ₹0.1172)
2026-02-16  E2E         BUY ₹29.27 at ₹2,464.00 (fresh Friday signal — BUY: surged 2.17× weekly on 2026-02-06 (month 1.26×), ladder rising NOW — promoted from the ladder watch; stop ₹2,223.00; charges ₹0.0691)
2026-02-17  NATIONALUM  SELL ₹46.89 at stop ₹335.49 (-4.7%, charges ₹0.1042) — the cash goes back to work at the next Friday screen
2026-02-23  VESUVIUS    BUY ₹46.89 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.1107)
2026-03-04  CEIGALL     SELL ₹44.49 at stop ₹266.33 (-10.3%, charges ₹0.0988) — the cash goes back to work at the next Friday screen
2026-03-04  PTC         SELL ₹42.93 at stop ₹156.89 (-13.1%, charges ₹0.0953) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹49.33 at stop ₹251.43 (-1.1%, charges ₹0.1096) — the cash goes back to work at the next Friday screen
2026-03-09  SOLARINDS   BUY ₹46.30 at ₹15,250.00 (fresh Friday signal — BUY: 2.55× weekly, month 1.15×, ladder rising; stop ₹12,217.95; charges ₹0.1093)
2026-03-09  TATASTEEL   SELL ₹50.07 at stop ₹190.52 (+2.8%, charges ₹0.1112) — the cash goes back to work at the next Friday screen
2026-03-09  TORNTPOWER  BUY ₹41.12 at ₹1,451.00 (fresh Friday signal — BUY: surged 4.10× weekly on 2026-02-13 (month 1.21×), ladder rising NOW — promoted from the ladder watch; stop ₹1,315.84; charges ₹0.0971)
2026-03-12  HINDCOPPER  SELL ₹48.85 at stop ₹528.63 (-0.6%, charges ₹0.1085) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹44.62 at stop ₹61.08 (-9.5%, charges ₹0.0991) — the cash goes back to work at the next Friday screen
2026-03-16  ABB         BUY ₹45.55 at ₹6,400.00 (fresh Friday signal — BUY: 1.80× weekly, month 1.92×, ladder rising; stop ₹5,486.25; charges ₹0.1075)
2026-03-16  J&KBANK     BUY ₹45.47 at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.95×, ladder rising; stop ₹103.27; charges ₹0.1073)
2026-03-16  JBCHEPHARM  BUY ₹45.38 at ₹2,136.00 (fresh Friday signal — BUY: surged 1.57× weekly on 2026-02-27 (month 1.33×), ladder rising NOW — promoted from the ladder watch; stop ₹1,875.30; charges ₹0.1071)
2026-03-16  NTPC        BUY ₹45.41 at ₹384.50 (fresh Friday signal — BUY: 1.64× weekly, month 1.11×, ladder rising; stop ₹345.90; charges ₹0.1072)
2026-03-23  HINDALCO    SELL ₹46.29 at stop ₹862.65 (-4.8%, charges ₹0.1028) — the cash goes back to work at the next Friday screen
2026-03-23  J&KBANK     SELL ₹41.35 at stop ₹110.67 (-8.6%, charges ₹0.0918) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹40.50 at stop ₹464.31 (-13.2%, charges ₹0.0900) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹42.51 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.1004)
2026-03-30  INOXINDIA   BUY ₹42.29 at ₹1,185.00 (fresh Friday signal — BUY: 2.69× weekly, month 1.27×, ladder rising; stop ₹1,067.80; charges ₹0.0998)
2026-03-30  SOLARINDS   SELL ₹36.92 at stop ₹12,217.95 (-19.9%, charges ₹0.0820) — the cash goes back to work at the next Friday screen
2026-03-30  TORNTPOWER  SELL ₹37.11 at stop ₹1,315.84 (-9.3%, charges ₹0.0824) — the cash goes back to work at the next Friday screen
2026-03-30  VTL         BUY ₹42.25 at ₹520.95 (fresh Friday signal — BUY: surged 1.53× weekly on 2026-02-27 (month 2.21×), ladder rising NOW — promoted from the ladder watch; stop ₹485.45; charges ₹0.0997)
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹49.98 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹42.81 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.1011)
2026-04-06  THERMAX     BUY ₹42.84 at ₹3,295.80 (fresh Friday signal — ACCUMULATE: 2.18× weekly, month 1.22×, ladder rising; stop ₹2,897.50; charges ₹0.1011)
2026-05-13  INOXINDIA   SELL ₹48.75 at stop ₹1,372.18 (+15.8%, charges ₹0.1083) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹41.41 at stop ₹1,125.84 (-2.1%, charges ₹0.0920) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹47.87 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.1130)
2026-05-18  NLCINDIA    BUY ₹42.82 at ₹351.55 (fresh Friday signal — BUY: 5.83× weekly, month 6.05×, ladder rising; stop ₹278.49; charges ₹0.1011)
2026-06-02  NTPC        SELL ₹42.89 at stop ₹364.80 (-5.1%, charges ₹0.0953) — the cash goes back to work at the next Friday screen
2026-06-05  E2E         SELL ₹27.56 at stop ₹2,330.72 (-5.4%, charges ₹0.0612) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹48.10 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.1135)
2026-06-09  NLCINDIA    SELL ₹38.88 at stop ₹320.62 (-8.8%, charges ₹0.0864) — the cash goes back to work at the next Friday screen
2026-06-15  CAPLIPOINT  BUY ₹49.11 at ₹2,435.00 (fresh Friday signal — BUY: 4.02× weekly, month 3.90×, ladder rising; stop ₹1,852.50; charges ₹0.1159)
2026-07-07  MCX         SELL ₹57.24 at stop ₹2,618.20 (+18.3%, charges ₹0.1271) — the cash goes back to work at the next Friday screen
2026-07-13  GANESHHOU   BUY ₹49.67 at ₹860.50 (fresh Friday signal — BUY: 9.80× weekly, month 2.00×, ladder rising; stop ₹712.60; charges ₹0.1173)
2026-07-29  THERMAX     SELL ₹55.73 at stop ₹4,306.64 (+30.7%, charges ₹0.1238) — the cash goes back to work at the next Friday screen
2026-07-31  VTL         SELL ₹47.86 at stop ₹592.80 (+13.8%, charges ₹0.1063) — the cash goes back to work at the next Friday screen
2026-08-03  BLUESTONE   BUY ₹49.31 at ₹823.40 (fresh Friday signal — ACCUMULATE: 5.63× weekly, month 9.43×, ladder rising; stop ₹664.75; charges ₹0.1164)
2026-08-03  MASTEK      BUY ₹24.61 at ₹1,874.80 (fresh Friday signal — BUY: 3.74× weekly, month 1.34×, ladder rising; stop ₹1,476.39; charges ₹0.0581)
2026-08-03  TMB         BUY ₹49.35 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.1165)
2026-08-19  MASTEK      SELL ₹22.22 at stop ₹1,700.50 (-9.3%, charges ₹0.0494) — the cash goes back to work at the next Friday screen
2026-09-10  ALKYLAMINE  SELL ₹53.53 at stop ₹1,920.99 (+12.3%, charges ₹0.1189) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹50.72 at stop ₹7,158.25 (+11.8%, charges ₹0.1127) — the cash goes back to work at the next Friday screen
2026-09-15  SUNDRMFAST  BUY ₹50.69 at ₹1,277.30 (fresh Friday signal — BUY: 3.14× weekly, month 1.81×, ladder rising; stop ₹1,127.74; charges ₹0.1197)
2026-09-21  AVALON      BUY ₹50.31 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.1188)
```
