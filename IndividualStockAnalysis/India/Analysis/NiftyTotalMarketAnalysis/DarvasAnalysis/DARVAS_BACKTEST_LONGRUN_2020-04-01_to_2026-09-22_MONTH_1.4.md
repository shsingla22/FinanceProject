# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 1388 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹399.97** | **+23.90% a year** |
| The same system before costs and taxes | ₹581.74 | +31.28% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹288.59 | +17.80% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹399.97** (+23.90% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 440 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹19.90** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹66.60**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹45.03 | ₹0.00 | ₹9.0054 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹27.39 | ₹29.49 | ₹9.1647 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹58.38 | ₹45.89 | ₹17.4119 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹155.11 | ₹0.00 | ₹31.0226 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹27.77 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹44.25 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹20.26 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 152.79 | +52.8% | +53.5% | +70.1% |
| 2021 (2021-12-31) | 240.59 | +57.5% | +67.6% | +26.2% |
| 2022 (2022-12-30) | 293.57 | +22.0% | +27.0% | +4.3% |
| 2023 (2023-12-29) | 422.68 | +44.0% | +56.3% | +20.0% |
| 2024 (2024-12-27) | 399.92 | -5.4% | +10.0% | +9.6% |
| 2025 (2025-12-26) | 382.30 | -4.4% | -2.2% | +9.4% |
| 2026 (2026-09-22) | 399.97 | +4.6% | +5.9% | -10.4% |

## What it took to earn it

- **Maximum drawdown: -34.9%** (peak 2024-03-07 → trough 2026-04-02, on weekly closes).
- **207 closed trades**: 96 winners (46%), average winner +33.3%, average loser -10.8%.
- Best closed trade ANANDRATHI +224.7%; worst KIOCL -24.5%.
- Median holding period 67 days.
- Cash share of equity averaged 10% across all weeks (median 3%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.20 | 59.96 | 4 |
| 2020-05-29 | 104.86 | 0.00 | 10 |
| 2020-06-26 | 120.17 | 0.00 | 10 |
| 2020-07-31 | 129.47 | 0.00 | 10 |
| 2020-08-28 | 129.21 | 0.00 | 10 |
| 2020-09-25 | 131.38 | 26.38 | 7 |
| 2020-10-30 | 125.20 | 0.00 | 9 |
| 2020-11-27 | 129.76 | 0.00 | 10 |
| 2020-12-24 | 152.79 | 30.26 | 8 |
| 2021-01-29 | 153.56 | 34.28 | 8 |
| 2021-02-26 | 165.25 | 13.75 | 9 |
| 2021-03-26 | 163.13 | 14.32 | 9 |
| 2021-04-30 | 166.02 | 0.00 | 10 |
| 2021-05-28 | 179.94 | 0.00 | 10 |
| 2021-06-25 | 198.64 | 0.00 | 10 |
| 2021-07-30 | 236.97 | 0.00 | 10 |
| 2021-08-27 | 231.23 | 0.00 | 10 |
| 2021-09-24 | 237.20 | 24.86 | 9 |
| 2021-10-29 | 234.85 | 44.30 | 8 |
| 2021-11-26 | 242.19 | 83.39 | 6 |
| 2021-12-31 | 240.59 | 0.00 | 9 |
| 2022-01-28 | 250.18 | 31.45 | 8 |
| 2022-02-25 | 232.94 | 91.68 | 5 |
| 2022-03-25 | 252.64 | 20.41 | 8 |
| 2022-04-29 | 259.55 | 26.33 | 7 |
| 2022-05-27 | 266.93 | 0.00 | 8 |
| 2022-06-24 | 253.11 | 30.04 | 7 |
| 2022-07-29 | 274.12 | 3.62 | 8 |
| 2022-08-26 | 286.99 | 3.62 | 8 |
| 2022-09-30 | 274.36 | 11.40 | 8 |
| 2022-10-28 | 285.06 | 11.40 | 8 |
| 2022-11-25 | 293.57 | 1.41 | 8 |
| 2022-12-30 | 293.57 | 0.00 | 9 |
| 2023-01-27 | 291.27 | 28.24 | 8 |
| 2023-02-24 | 302.25 | 0.00 | 9 |
| 2023-03-31 | 289.22 | 113.57 | 6 |
| 2023-04-28 | 296.04 | 40.72 | 8 |
| 2023-05-26 | 305.59 | 38.86 | 8 |
| 2023-06-30 | 320.04 | 8.54 | 9 |
| 2023-07-28 | 331.33 | 9.85 | 9 |
| 2023-08-25 | 365.23 | 3.91 | 9 |
| 2023-09-29 | 372.50 | 40.10 | 8 |
| 2023-10-27 | 371.34 | 69.77 | 7 |
| 2023-11-24 | 403.73 | 6.53 | 9 |
| 2023-12-29 | 422.68 | 0.00 | 9 |
| 2024-01-25 | 442.31 | 15.35 | 9 |
| 2024-02-23 | 479.04 | 11.79 | 9 |
| 2024-03-28 | 462.63 | 100.85 | 8 |
| 2024-04-26 | 462.99 | 0.00 | 10 |
| 2024-05-31 | 459.63 | 83.03 | 8 |
| 2024-06-28 | 466.71 | 0.00 | 10 |
| 2024-07-26 | 470.62 | 43.18 | 9 |
| 2024-08-30 | 438.16 | 0.00 | 10 |
| 2024-09-27 | 439.36 | 0.00 | 10 |
| 2024-10-25 | 380.53 | 151.49 | 6 |
| 2024-11-29 | 408.63 | 0.13 | 10 |
| 2024-12-27 | 399.92 | 80.92 | 8 |
| 2025-01-31 | 369.27 | 130.51 | 6 |
| 2025-02-28 | 341.27 | 140.31 | 6 |
| 2025-03-27 | 370.17 | 0.00 | 10 |
| 2025-04-25 | 388.25 | 19.90 | 9 |
| 2025-05-30 | 394.40 | 40.73 | 9 |
| 2025-06-27 | 412.20 | 37.21 | 9 |
| 2025-07-25 | 402.80 | 40.29 | 9 |
| 2025-08-29 | 399.55 | 34.17 | 9 |
| 2025-09-26 | 369.46 | 106.67 | 7 |
| 2025-10-31 | 373.01 | 60.84 | 9 |
| 2025-11-28 | 381.70 | 109.74 | 7 |
| 2025-12-26 | 382.30 | 0.00 | 10 |
| 2026-01-30 | 378.21 | 168.31 | 5 |
| 2026-02-27 | 360.44 | 0.00 | 10 |
| 2026-03-27 | 334.31 | 101.88 | 7 |
| 2026-04-30 | 359.02 | 6.34 | 10 |
| 2026-05-29 | 384.29 | 3.18 | 10 |
| 2026-06-25 | 383.22 | 0.00 | 10 |
| 2026-07-31 | 386.09 | 110.84 | 7 |
| 2026-08-28 | 402.57 | 0.00 | 10 |
| 2026-09-22 | 399.97 | 2.25 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| BLUESTONE | 2026-08-03 | 823.40 | 930.40 | 758.29 | +13.0% |
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,777.30 | 2,376.52 | +39.6% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,392.00 | 1,242.60 | +40.7% |
| GARFIBRES | 2026-06-22 | 796.00 | 800.45 | 701.74 | +0.6% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| RUBICON | 2026-06-08 | 1,190.00 | 1,671.20 | 1,653.47 | +40.4% |
| SUNDRMFAST | 2026-09-15 | 1,277.30 | 1,190.90 | 1,127.74 | -6.8% |
| TIIL | 2026-08-17 | 3,125.00 | 2,983.00 | 2,915.55 | -4.5% |
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
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| KIOCL | 2020-08-24 | 152.50 | 2020-09-22 | 115.10 | -24.5% |
| SATIA | 2020-09-14 | 122.00 | 2020-09-22 | 102.97 | -15.6% |
| BHARATRAS | 2020-07-06 | 1,901.25 | 2020-10-09 | 2,210.00 | +16.2% |
| PRINCEPIPE | 2020-09-07 | 208.00 | 2020-10-12 | 220.88 | +6.2% |
| ALEMBICLTD | 2020-05-18 | 54.90 | 2020-11-02 | 91.41 | +66.5% |
| ADVENZYMES | 2020-05-18 | 159.95 | 2020-11-03 | 292.33 | +82.8% |
| THYROCARE | 2020-10-12 | 1,071.90 | 2020-11-12 | 1,016.50 | -5.2% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| TCI | 2020-09-14 | 242.00 | 2020-12-22 | 234.75 | -3.0% |
| GODREJPROP | 2020-11-09 | 964.00 | 2021-01-18 | 1,306.25 | +35.5% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| TRENT | 2020-11-17 | 503.33 | 2021-01-29 | 417.53 | -17.0% |
| MTNL | 2020-12-28 | 14.10 | 2021-02-16 | 12.06 | -14.5% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| JINDWORLD | 2020-11-09 | 50.00 | 2021-03-01 | 52.12 | +4.2% |
| RCF | 2021-03-01 | 80.00 | 2021-03-17 | 79.16 | -1.1% |
| TATAMOTORS | 2021-01-25 | 296.90 | 2021-03-19 | 296.97 | +0.0% |
| APTECHT | 2021-02-01 | 178.45 | 2021-03-19 | 204.25 | +14.5% |
| MAHINDCIE | 2021-02-22 | 188.00 | 2021-03-19 | 158.46 | -15.7% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| CENTRUM | 2021-03-30 | 28.40 | 2021-04-12 | 24.89 | -12.4% |
| GFLLIMITED | 2021-03-22 | 93.00 | 2021-04-13 | 74.39 | -20.0% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| GDL | 2021-01-25 | 158.00 | 2021-09-20 | 266.00 | +68.4% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| NEOGEN | 2021-09-27 | 1,255.00 | 2021-10-25 | 1,142.85 | -8.9% |
| EMAMIPAP | 2021-04-19 | 125.00 | 2021-11-22 | 141.55 | +13.2% |
| SHOPERSTOP | 2021-10-25 | 326.00 | 2021-11-22 | 335.82 | +3.0% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-11-01 | 11,040.00 | 2021-11-26 | 10,070.05 | -8.8% |
| SOMANYCERA | 2021-06-21 | 594.85 | 2021-11-29 | 755.11 | +26.9% |
| MAHLOG | 2021-01-25 | 495.85 | 2021-11-30 | 654.55 | +32.0% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| LTTS | 2020-10-19 | 1,745.00 | 2022-01-21 | 4,856.88 | +178.3% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| DIAMONDYD | 2021-12-06 | 800.00 | 2022-01-31 | 817.00 | +2.1% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| LAXMIMACH | 2022-02-21 | 10,118.80 | 2022-02-22 | 10,169.75 | +0.5% |
| JSWISPL | 2022-01-24 | 37.50 | 2022-02-24 | 30.25 | -19.3% |
| CCL | 2022-02-07 | 503.55 | 2022-02-24 | 441.75 | -12.3% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| RAJRATAN | 2021-03-22 | 763.95 | 2022-03-28 | 1,553.82 | +103.4% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| RCF | 2022-04-04 | 96.40 | 2022-05-04 | 93.15 | -3.4% |
| MFL | 2022-05-02 | 1,430.00 | 2022-05-11 | 1,225.50 | -14.3% |
| MOL | 2022-05-09 | 129.80 | 2022-05-11 | 113.62 | -12.5% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| KRISHANA | 2022-05-16 | 67.96 | 2022-06-16 | 54.77 | -19.4% |
| JSWENERGY | 2021-03-08 | 81.85 | 2022-06-20 | 201.99 | +146.8% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| RAJMET | 2022-03-07 | 278.00 | 2022-09-15 | 359.30 | +29.2% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| 3MINDIA | 2022-07-11 | 22,701.00 | 2023-01-02 | 21,626.80 | -4.7% |
| KSL | 2022-12-26 | 330.10 | 2023-01-27 | 328.23 | -0.6% |
| GICRE | 2022-12-26 | 157.00 | 2023-02-01 | 167.72 | +6.8% |
| LSIL | 2023-01-30 | 23.20 | 2023-02-07 | 20.04 | -13.6% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| MAHINDCIE | 2023-02-06 | 395.20 | 2023-03-10 | 391.69 | -0.9% |
| KABRAEXTRU | 2022-12-26 | 441.95 | 2023-03-14 | 506.92 | +14.7% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| JINDALSAW | 2023-01-09 | 55.85 | 2023-03-27 | 67.92 | +21.6% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| CIGNITITEC | 2023-02-13 | 673.00 | 2023-03-29 | 705.14 | +4.8% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| GUJALKALI | 2023-05-02 | 688.15 | 2023-05-23 | 646.14 | -6.1% |
| ANURAS | 2023-03-20 | 755.90 | 2023-07-03 | 1,007.67 | +33.3% |
| KSB | 2023-03-27 | 417.98 | 2023-07-12 | 407.74 | -2.4% |
| THANGAMAYL | 2023-05-29 | 1,344.00 | 2023-07-17 | 1,344.25 | +0.0% |
| GANESHHOUC | 2023-07-24 | 457.00 | 2023-08-14 | 418.62 | -8.4% |
| INGERRAND | 2023-04-03 | 2,690.00 | 2023-09-13 | 3,022.99 | +12.4% |
| KIRLOSIND | 2023-03-13 | 2,300.00 | 2023-09-25 | 3,202.97 | +39.3% |
| SJVN | 2023-09-18 | 75.35 | 2023-10-23 | 66.03 | -12.4% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
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
| PILANIINVS | 2023-10-03 | 2,380.05 | 2024-05-09 | 3,710.37 | +55.9% |
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| DMART | 2024-04-01 | 4,570.00 | 2024-05-31 | 4,322.83 | -5.4% |
| SOLARINDS | 2024-03-18 | 8,900.05 | 2024-06-04 | 7,980.95 | -10.3% |
| BOSCHLTD | 2024-03-18 | 29,500.05 | 2024-06-04 | 29,015.09 | -1.6% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| KIRLOSBROS | 2024-05-21 | 1,844.00 | 2024-08-05 | 1,987.46 | +7.8% |
| THERMAX | 2024-06-03 | 5,640.00 | 2024-08-05 | 4,719.70 | -16.3% |
| JWL | 2024-05-13 | 490.00 | 2024-08-06 | 552.00 | +12.7% |
| ADANIPOWER | 2024-06-10 | 783.00 | 2024-08-12 | 632.75 | -19.2% |
| EMUDHRA | 2024-03-18 | 583.90 | 2024-08-13 | 793.11 | +35.8% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| CERA | 2024-08-12 | 10,499.95 | 2024-09-19 | 8,198.93 | -21.9% |
| IOB | 2024-02-12 | 71.50 | 2024-10-03 | 56.57 | -20.9% |
| VGUARD | 2024-08-19 | 524.15 | 2024-10-04 | 420.24 | -19.8% |
| POLYPLEX | 2024-08-19 | 1,298.00 | 2024-10-04 | 1,125.80 | -13.3% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| PCBL | 2024-08-12 | 393.00 | 2024-10-18 | 476.85 | +21.3% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| ALKYLAMINE | 2024-09-23 | 2,432.85 | 2024-10-22 | 2,106.24 | -13.4% |
| HBLPOWER | 2024-07-22 | 585.00 | 2024-10-25 | 522.78 | -10.6% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| KIRLPNU | 2024-11-04 | 1,698.00 | 2024-12-23 | 1,596.00 | -6.0% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| PAYTM | 2024-10-28 | 747.70 | 2025-01-09 | 893.05 | +19.4% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| CARERATING | 2024-10-28 | 1,396.00 | 2025-01-13 | 1,239.70 | -11.2% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| MOTILALOFS | 2024-10-21 | 1,021.95 | 2025-01-17 | 788.79 | -22.8% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| BSE | 2024-10-14 | 4,536.00 | 2025-02-28 | 4,954.63 | +9.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| GRWRHITECH | 2025-03-10 | 4,219.95 | 2025-04-03 | 3,602.82 | -14.6% |
| AVANTIFEED | 2025-03-17 | 842.55 | 2025-04-07 | 648.95 | -23.0% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| ITDCEM | 2024-10-07 | 655.05 | 2025-04-11 | 524.92 | -19.9% |
| KSCL | 2025-03-24 | 1,285.00 | 2025-05-15 | 1,334.75 | +3.9% |
| HCG | 2025-01-20 | 504.95 | 2025-05-26 | 559.08 | +10.7% |
| COROMANDEL | 2025-04-07 | 1,870.00 | 2025-06-27 | 2,246.75 | +20.1% |
| TECHNOE | 2025-06-02 | 1,421.00 | 2025-07-24 | 1,467.84 | +3.3% |
| CARERATING | 2025-05-19 | 1,527.50 | 2025-07-31 | 1,703.35 | +11.5% |
| JSWHL | 2024-11-18 | 19,990.00 | 2025-08-04 | 19,106.01 | -4.4% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| WHIRLPOOL | 2025-04-28 | 1,153.90 | 2025-08-07 | 1,301.97 | +12.8% |
| ALKYLAMINE | 2025-06-30 | 2,263.00 | 2025-08-07 | 2,087.62 | -7.7% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| THYROCARE | 2025-08-18 | 1,408.00 | 2025-09-15 | 1,184.93 | -15.8% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| RSYSTEMS | 2025-09-01 | 460.00 | 2025-09-24 | 423.23 | -8.0% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| BOMDYEING | 2025-07-28 | 181.45 | 2025-09-25 | 172.67 | -4.8% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| BLACKBUCK | 2025-08-18 | 553.00 | 2025-10-28 | 642.20 | +16.1% |
| PGHL | 2025-08-04 | 6,440.00 | 2025-11-06 | 5,938.45 | -7.8% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| NETWEB | 2025-09-29 | 3,700.00 | 2025-11-06 | 3,515.95 | -5.0% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| FLUOROCHEM | 2025-09-22 | 3,820.00 | 2025-11-24 | 3,412.02 | -10.7% |
| TDPOWERSYS | 2025-11-03 | 382.27 | 2025-11-24 | 357.49 | -6.5% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| M&MFIN | 2025-11-03 | 316.55 | 2026-01-07 | 360.81 | +14.0% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| GRAVITA | 2025-12-01 | 1,825.10 | 2026-01-09 | 1,678.56 | -8.0% |
| UPL | 2025-08-11 | 688.95 | 2026-01-20 | 729.12 | +5.8% |
| LGBBROSLTD | 2025-09-29 | 1,411.60 | 2026-01-20 | 1,713.80 | +21.4% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| HAPPYFORGE | 2026-02-23 | 1,370.00 | 2026-03-04 | 1,234.05 | -9.9% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| HINDCOPPER | 2026-01-12 | 532.00 | 2026-03-12 | 528.63 | -0.6% |
| RBA | 2026-01-19 | 67.50 | 2026-03-12 | 61.08 | -9.5% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-16 | 121.14 | 2026-03-23 | 110.67 | -8.6% |
| MAHABANK | 2025-10-27 | 59.00 | 2026-03-30 | 61.05 | +3.5% |
| TORNTPOWER | 2026-02-23 | 1,540.00 | 2026-03-30 | 1,315.84 | -14.6% |
| INOXINDIA | 2026-04-06 | 1,253.90 | 2026-05-13 | 1,372.18 | +9.4% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| E2E | 2026-02-23 | 2,914.00 | 2026-06-05 | 2,330.72 | -20.0% |
| AUROPHARMA | 2026-04-06 | 1,344.00 | 2026-06-15 | 1,403.53 | +4.4% |
| ACUTAAS | 2026-02-23 | 2,123.60 | 2026-07-28 | 3,180.60 | +49.8% |
| THERMAX | 2026-04-13 | 3,596.00 | 2026-07-29 | 4,306.64 | +19.8% |
| VTL | 2026-03-23 | 534.00 | 2026-07-31 | 592.80 | +11.0% |
| SENCO | 2026-08-03 | 408.90 | 2026-08-12 | 347.45 | -15.0% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-02-23 | 6,090.00 | 2026-09-15 | 7,158.25 | +17.5% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_MONTH_1.4.csv` beside this report (19224 events in all).*

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
2020-07-06  BHARATRAS   BUY ₹9.31 at ₹1,901.25 (fresh Friday signal — BUY: 4.45× weekly, month 1.97×, ladder rising; stop ₹1,626.88; charges ₹0.0110)
2020-08-17  EIDPARRY    SELL ₹16.49 at stop ₹273.03 (+66.5%, charges ₹0.0171) — the cash goes back to work at the next Friday screen
2020-08-20  PANACEABIO  SELL ₹7.96 at stop ₹184.01 (-20.0%, charges ₹0.0083) — the cash goes back to work at the next Friday screen
2020-08-24  APCOTEXIND  BUY ₹13.12 at ₹164.95 (fresh Friday signal — BUY: 8.08× weekly, month 5.83×, ladder rising; stop ₹119.51; charges ₹0.0155)
2020-08-24  KIOCL       BUY ₹11.33 at ₹152.50 (fresh Friday signal — BUY: 7.39× weekly, month 5.13×, ladder rising; stop ₹107.06; charges ₹0.0134)
2020-08-31  APCOTEXIND  SELL ₹12.06 at stop ₹151.95 (-7.9%, charges ₹0.0125) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.83 at stop ₹928.62 (+19.9%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹12.65 at ₹1,398.95 (fresh Friday signal — BUY: 5.36× weekly, month 3.91×, ladder rising; stop ₹1,211.25; charges ₹0.0150)
2020-09-07  PRINCEPIPE  BUY ₹11.23 at ₹208.00 (fresh Friday signal — BUY: 3.47× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.0133)
2020-09-08  CADILAHC    SELL ₹11.04 at stop ₹364.99 (+10.5%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-09  BALAJITELE  SELL ₹11.96 at stop ₹74.07 (+20.6%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-14  SATIA       BUY ₹9.95 at ₹122.00 (fresh Friday signal — ACCUMULATE: 2.86× weekly, month 6.16×, ladder rising; stop ₹102.97; charges ₹0.0118)
2020-09-14  TCI         BUY ₹13.05 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.76× weekly, month 3.77×, ladder rising; stop ₹190.07; charges ₹0.0155)
2020-09-22  KIOCL       SELL ₹8.53 at stop ₹115.10 (-24.5%, charges ₹0.0089) — the cash goes back to work at the next Friday screen
2020-09-22  SATIA       SELL ₹8.38 at stop ₹102.97 (-15.6%, charges ₹0.0087) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹9.47 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹13.16 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0156)
2020-09-28  SAKSOFT     BUY ₹13.22 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.0157)
2020-10-09  BHARATRAS   SELL ₹10.80 at stop ₹2,210.00 (+16.2%, charges ₹0.0112) — the cash goes back to work at the next Friday screen
2020-10-12  PRINCEPIPE  SELL ₹11.90 at stop ₹220.88 (+6.2%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2020-10-12  THYROCARE   BUY ₹10.80 at ₹1,071.90 (fresh Friday signal — BUY: 8.93× weekly, month 4.49×, ladder rising; stop ₹705.09; charges ₹0.0128)
2020-10-19  LTTS        BUY ₹11.90 at ₹1,745.00 (fresh Friday signal — BUY: 4.76× weekly, month 2.59×, ladder rising; stop ₹1,482.95; charges ₹0.0141)
2020-11-02  ALEMBICLTD  SELL ₹16.83 at stop ₹91.41 (+66.5%, charges ₹0.0175) — the cash goes back to work at the next Friday screen
2020-11-03  ADVENZYMES  SELL ₹18.56 at stop ₹292.33 (+82.8%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹12.38 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.0147)
2020-11-09  GODREJPROP  BUY ₹10.60 at ₹964.00 (fresh Friday signal — BUY: surged 4.07× weekly on 2020-10-23 (month 2.56×), ladder rising NOW — promoted from the ladder watch; stop ₹927.67; charges ₹0.0126)
2020-11-09  JINDWORLD   BUY ₹12.40 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.28× weekly, month 1.55×, ladder rising; stop ₹39.81; charges ₹0.0147)
2020-11-12  THYROCARE   SELL ₹10.22 at stop ₹1,016.50 (-5.2%, charges ₹0.0106) — the cash goes back to work at the next Friday screen
2020-11-17  TRENT       BUY ₹10.22 at ₹503.33 (fresh Friday signal — ACCUMULATE: 3.30× weekly, month 1.95×, ladder rising; stop ₹367.93; charges ₹0.0121)
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹12.63 at stop ₹234.75 (-3.0%, charges ₹0.0131) — the cash goes back to work at the next Friday screen
2020-12-28  MTNL        BUY ₹14.50 at ₹14.10 (fresh Friday signal — BUY: 9.97× weekly, month 4.77×, ladder rising; stop ₹8.26; charges ₹0.0172)
2020-12-28  PAISALO     BUY ₹15.76 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0187)
2021-01-18  GODREJPROP  SELL ₹14.34 at stop ₹1,306.25 (+35.5%, charges ₹0.0149) — the cash goes back to work at the next Friday screen
2021-01-20  BORORENEW   SELL ₹30.69 at stop ₹247.59 (+148.3%, charges ₹0.0318) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹15.65 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.79×, ladder rising; stop ₹92.41; charges ₹0.0185)
2021-01-25  MAHLOG      BUY ₹15.81 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹0.0187)
2021-01-25  SAKSOFT     SELL ₹11.28 at stop ₹341.10 (-14.4%, charges ₹0.0117) — the cash goes back to work at the next Friday screen
2021-01-25  TATAMOTORS  BUY ₹13.56 at ₹296.90 (fresh Friday signal — BUY: 3.10× weekly, month 2.05×, ladder rising; stop ₹171.38; charges ₹0.0161)
2021-01-29  HCLTECH     SELL ₹14.54 at stop ₹928.05 (+10.7%, charges ₹0.0151) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹8.46 at stop ₹417.53 (-17.0%, charges ₹0.0088) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹15.55 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.0184)
2021-02-01  GAEL        BUY ₹15.71 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.71× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.0186)
2021-02-16  MTNL        SELL ₹12.37 at stop ₹12.06 (-14.5%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2021-02-22  MAHINDCIE   BUY ₹15.40 at ₹188.00 (fresh Friday signal — BUY: 22.74× weekly, month 4.25×, ladder rising; stop ₹143.79; charges ₹0.0182)
2021-02-23  GAEL        SELL ₹13.75 at stop ₹62.70 (-12.3%, charges ₹0.0143) — the cash goes back to work at the next Friday screen
2021-03-01  JINDWORLD   SELL ₹12.90 at stop ₹52.12 (+4.2%, charges ₹0.0134) — the cash goes back to work at the next Friday screen
2021-03-01  RCF         BUY ₹13.75 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.13×, ladder rising; stop ₹50.16; charges ₹0.0163)
2021-03-08  JSWENERGY   BUY ₹12.90 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.50×, ladder rising; stop ₹65.79; charges ₹0.0153)
2021-03-17  RCF         SELL ₹13.57 at stop ₹79.16 (-1.1%, charges ₹0.0141) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹17.75 at stop ₹204.25 (+14.5%, charges ₹0.0184) — the cash goes back to work at the next Friday screen
2021-03-19  MAHINDCIE   SELL ₹12.95 at stop ₹158.46 (-15.7%, charges ₹0.0134) — the cash goes back to work at the next Friday screen
2021-03-19  TATAMOTORS  SELL ₹13.54 at stop ₹296.97 (+0.0%, charges ₹0.0140) — the cash goes back to work at the next Friday screen
2021-03-22  GFLLIMITED  BUY ₹16.04 at ₹93.00 (fresh Friday signal — ACCUMULATE: 6.17× weekly, month 3.98×, ladder rising; stop ₹74.39; charges ₹0.0190)
2021-03-22  KEI         BUY ₹16.14 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.0191)
2021-03-22  RAJRATAN    BUY ₹9.67 at ₹763.95 (fresh Friday signal — BUY: 4.06× weekly, month 2.74×, ladder rising; stop ₹590.19; charges ₹0.0115)
2021-03-22  VIDHIING    BUY ₹15.96 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0189)
2021-03-25  BANARISUG   SELL ₹14.32 at stop ₹1,586.36 (+13.4%, charges ₹0.0149) — the cash goes back to work at the next Friday screen
2021-03-30  CENTRUM     BUY ₹14.32 at ₹28.40 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 6.70×, ladder rising; stop ₹24.89; charges ₹0.0170)
2021-04-01  CENTRUM     TRIM 5.4% (₹0.77 at ₹28.35) to pay the tax bill
2021-04-01  GDL         TRIM 5.4% (₹0.95 at ₹177.90) to pay the tax bill
2021-04-01  GFLLIMITED  TRIM 5.4% (₹1.01 at ₹108.35) to pay the tax bill
2021-04-01  JSWENERGY   TRIM 5.4% (₹0.77 at ₹90.70) to pay the tax bill
2021-04-01  KEI         TRIM 5.4% (₹0.88 at ₹528.60) to pay the tax bill
2021-04-01  LTTS        TRIM 5.4% (₹1.00 at ₹2,720.60) to pay the tax bill
2021-04-01  MAHLOG      TRIM 5.4% (₹0.99 at ₹574.75) to pay the tax bill
2021-04-01  PAISALO     TRIM 5.4% (₹1.17 at ₹78.11) to pay the tax bill
2021-04-01  RAJRATAN    TRIM 5.4% (₹0.53 at ₹771.90) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹9.0054 paid (STCG ₹45.03 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  VIDHIING    TRIM 5.4% (₹0.92 at ₹207.10) to pay the tax bill
2021-04-12  CENTRUM     SELL ₹11.84 at stop ₹24.89 (-12.4%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹18.90 at stop ₹72.41 (+27.1%, charges ₹0.0196) — the cash goes back to work at the next Friday screen
2021-04-13  GFLLIMITED  SELL ₹12.11 at stop ₹74.39 (-20.0%, charges ₹0.0126) — the cash goes back to work at the next Friday screen
2021-04-19  EMAMIPAP    BUY ₹13.83 at ₹125.00 (fresh Friday signal — ACCUMULATE: 2.31× weekly, month 22.17×, ladder rising; stop ₹81.22; charges ₹0.0164)
2021-04-19  KPRMILL     BUY ₹14.50 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0172)
2021-04-19  MOREPENLAB  BUY ₹14.52 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹0.0172)
2021-06-18  VIDHIING    SELL ₹14.13 at stop ₹182.64 (-6.2%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2021-06-21  SOMANYCERA  BUY ₹14.13 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0167)
2021-08-10  MOREPENLAB  SELL ₹21.79 at stop ₹56.33 (+50.4%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹21.61 at stop ₹352.48 (+49.4%, charges ₹0.0224) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹23.21 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.0275)
2021-08-16  TATAINVEST  BUY ₹20.19 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0239)
2021-09-20  GDL         SELL ₹24.86 at stop ₹266.00 (+68.4%, charges ₹0.0258) — the cash goes back to work at the next Friday screen
2021-09-27  NEOGEN      BUY ₹23.99 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0284)
2021-10-22  KEI         SELL ₹24.89 at stop ₹853.10 (+63.4%, charges ₹0.0258) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹20.27 at stop ₹3,220.59 (-12.5%, charges ₹0.0210) — the cash goes back to work at the next Friday screen
2021-10-25  NEOGEN      SELL ₹21.80 at stop ₹1,142.85 (-8.9%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2021-10-25  SHOPERSTOP  BUY ₹23.53 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹0.0279)
2021-11-01  TCIEXP      BUY ₹20.73 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0246)
2021-11-01  TTKPRESTIG  BUY ₹23.57 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.0279)
2021-11-22  EMAMIPAP    SELL ₹15.63 at stop ₹141.55 (+13.2%, charges ₹0.0162) — the cash goes back to work at the next Friday screen
2021-11-22  SHOPERSTOP  SELL ₹24.18 at stop ₹335.82 (+3.0%, charges ₹0.0251) — the cash goes back to work at the next Friday screen
2021-11-26  TATAINVEST  SELL ₹22.12 at stop ₹1,436.49 (+9.8%, charges ₹0.0229) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹21.45 at stop ₹10,070.05 (-8.8%, charges ₹0.0223) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹23.91 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.0283)
2021-11-29  RAYMOND     BUY ₹23.67 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0280)
2021-11-29  RSYSTEMS    BUY ₹23.80 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0282)
2021-11-29  SOMANYCERA  SELL ₹17.90 at stop ₹755.11 (+26.9%, charges ₹0.0186) — the cash goes back to work at the next Friday screen
2021-11-30  MAHLOG      SELL ₹19.70 at stop ₹654.55 (+32.0%, charges ₹0.0204) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹23.65 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0280)
2021-12-06  DIAMONDYD   BUY ₹23.60 at ₹800.00 (fresh Friday signal — BUY: 4.19× weekly, month 1.42×, ladder rising; stop ₹652.65; charges ₹0.0280)
2021-12-16  RSYSTEMS    SELL ₹21.29 at stop ₹291.18 (-10.4%, charges ₹0.0221) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹23.43 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0278)
2021-12-21  TCIEXP      SELL ₹23.04 at stop ₹2,039.74 (+11.4%, charges ₹0.0239) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹23.24 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0275)
2022-01-21  LTTS        SELL ₹31.25 at stop ₹4,856.88 (+178.3%, charges ₹0.0324) — the cash goes back to work at the next Friday screen
2022-01-24  JSWISPL     BUY ₹24.97 at ₹37.50 (fresh Friday signal — BUY: 5.58× weekly, month 4.04×, ladder rising; stop ₹27.79; charges ₹0.0296)
2022-01-25  SWANENERGY  SELL ₹25.16 at stop ₹162.64 (+8.5%, charges ₹0.0261) — the cash goes back to work at the next Friday screen
2022-01-31  DIAMONDYD   SELL ₹24.04 at stop ₹817.00 (+2.1%, charges ₹0.0249) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹25.28 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0299)
2022-02-07  CCL         BUY ₹25.62 at ₹503.55 (fresh Friday signal — BUY: 4.07× weekly, month 1.58×, ladder rising; stop ₹408.60; charges ₹0.0304)
2022-02-11  SHARDACROP  SELL ₹23.44 at stop ₹545.30 (-7.1%, charges ₹0.0243) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹21.78 at stop ₹424.65 (-8.7%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹24.15 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0286)
2022-02-15  RAYMOND     SELL ₹26.92 at stop ₹679.35 (+14.0%, charges ₹0.0279) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹23.67 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0280)
2022-02-21  LAXMIMACH   BUY ₹23.63 at ₹10,118.80 (fresh Friday signal — BUY: surged 2.17× weekly on 2022-01-21 (month 1.69×), ladder rising NOW — promoted from the ladder watch; stop ₹10,169.75; charges ₹0.0280)
2022-02-22  GREENLAM    SELL ₹20.17 at stop ₹313.67 (-13.7%, charges ₹0.0209) — the cash goes back to work at the next Friday screen
2022-02-22  LAXMIMACH   SELL ₹23.69 at stop ₹10,169.75 (+0.5%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2022-02-24  CCL         SELL ₹22.42 at stop ₹441.75 (-12.3%, charges ₹0.0233) — the cash goes back to work at the next Friday screen
2022-02-24  JSWISPL     SELL ₹20.10 at stop ₹30.25 (-19.3%, charges ₹0.0208) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹23.55 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0279)
2022-02-28  SHANTIGEAR  BUY ₹23.66 at ₹185.30 (fresh Friday signal — BUY: surged 3.40× weekly on 2022-02-11 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹170.29; charges ₹0.0280)
2022-03-07  GTLINFRA    BUY ₹23.84 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0282)
2022-03-07  RAJMET      BUY ₹20.63 at ₹278.00 (fresh Friday signal — BUY: surged 6.93× weekly on 2022-02-18 (month 4.62×), ladder rising NOW — promoted from the ladder watch; stop ₹226.96; charges ₹0.0244)
2022-03-21  BSE         SELL ₹20.41 at stop ₹1,634.39 (-13.5%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2022-03-28  RAJRATAN    SELL ₹18.56 at stop ₹1,553.82 (+103.4%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹9.1647 paid (STCG ₹27.39 @20%, LTCG ₹29.49 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  RCF         BUY ₹23.20 at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.0275)
2022-04-29  GTLINFRA    SELL ₹19.73 at stop ₹1.41 (-17.1%, charges ₹0.0205) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹25.89 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.0307)
2022-05-04  RCF         SELL ₹22.37 at stop ₹93.15 (-3.4%, charges ₹0.0232) — the cash goes back to work at the next Friday screen
2022-05-09  MOL         BUY ₹22.81 at ₹129.80 (fresh Friday signal — BUY: 6.75× weekly, month 2.56×, ladder rising; stop ₹113.62; charges ₹0.0270)
2022-05-11  MFL         SELL ₹22.14 at stop ₹1,225.50 (-14.3%, charges ₹0.0230) — the cash goes back to work at the next Friday screen
2022-05-11  MOL         SELL ₹19.92 at stop ₹113.62 (-12.5%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2022-05-16  KRISHANA    BUY ₹16.70 at ₹67.96 (fresh Friday signal — ACCUMULATE: 1.67× weekly, month 1.86×, ladder rising; stop ₹54.77; charges ₹0.0198)
2022-05-16  VBL         BUY ₹25.36 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0300)
2022-06-06  VBL         SELL ₹22.58 at stop ₹196.27 (-10.8%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹22.58 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0267)
2022-06-16  KRISHANA    SELL ₹13.43 at stop ₹54.77 (-19.4%, charges ₹0.0139) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹13.43 at ₹950.15 (fresh Friday signal — BUY: surged 6.84× weekly on 2022-06-10 (month 1.49×), ladder rising NOW — promoted from the ladder watch; stop ₹706.80; charges ₹0.0159)
2022-06-20  JSWENERGY   SELL ₹30.04 at stop ₹201.99 (+146.8%, charges ₹0.0312) — the cash goes back to work at the next Friday screen
2022-07-11  3MINDIA     BUY ₹26.42 at ₹22,701.00 (fresh Friday signal — BUY: surged 1.59× weekly on 2022-07-01 (month 2.11×), ladder rising NOW — promoted from the ladder watch; stop ₹20,069.75; charges ₹0.0313)
2022-09-06  DANGEE      SELL ₹37.52 at stop ₹375.25 (+59.7%, charges ₹0.0389) — the cash goes back to work at the next Friday screen
2022-09-12  SHREECEM    BUY ₹28.39 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0336)
2022-09-15  RAJMET      SELL ₹26.60 at stop ₹359.30 (+29.2%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2022-09-19  JSWHL       BUY ₹27.95 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0331)
2022-11-03  APARINDS    SELL ₹19.16 at stop ₹1,358.50 (+43.0%, charges ₹0.0199) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹29.16 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0345)
2022-12-21  ELECON      SELL ₹37.24 at stop ₹202.49 (+65.3%, charges ₹0.0386) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹44.02 at stop ₹345.56 (+86.5%, charges ₹0.0457) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹29.06 at stop ₹139.84 (-0.1%, charges ₹0.0301) — the cash goes back to work at the next Friday screen
2022-12-26  GICRE       BUY ₹28.53 at ₹157.00 (fresh Friday signal — BUY: surged 4.73× weekly on 2022-12-02 (month 1.82×), ladder rising NOW — promoted from the ladder watch; stop ₹134.14; charges ₹0.0338)
2022-12-26  KABRAEXTRU  BUY ₹26.42 at ₹441.95 (fresh Friday signal — BUY: surged 4.67× weekly on 2022-11-25 (month 1.52×), ladder rising NOW — promoted from the ladder watch; stop ₹457.95; charges ₹0.0313)
2022-12-26  KRISHANA    BUY ₹28.32 at ₹83.60 (fresh Friday signal — BUY: 3.70× weekly, month 2.29×, ladder rising; stop ₹75.36; charges ₹0.0336)
2022-12-26  KSL         BUY ₹28.46 at ₹330.10 (fresh Friday signal — BUY: surged 5.50× weekly on 2022-12-09 (month 2.50×), ladder rising NOW — promoted from the ladder watch; stop ₹328.23; charges ₹0.0337)
2023-01-02  3MINDIA     SELL ₹25.11 at stop ₹21,626.80 (-4.7%, charges ₹0.0260) — the cash goes back to work at the next Friday screen
2023-01-09  JINDALSAW   BUY ₹25.11 at ₹55.85 (fresh Friday signal — BUY: 3.64× weekly, month 3.14×, ladder rising; stop ₹42.55; charges ₹0.0298)
2023-01-27  KSL         SELL ₹28.24 at stop ₹328.23 (-0.6%, charges ₹0.0293) — the cash goes back to work at the next Friday screen
2023-01-30  LSIL        BUY ₹28.24 at ₹23.20 (fresh Friday signal — BUY: 2.28× weekly, month 3.56×, ladder rising; stop ₹11.29; charges ₹0.0335)
2023-02-01  GICRE       SELL ₹30.41 at stop ₹167.72 (+6.8%, charges ₹0.0315) — the cash goes back to work at the next Friday screen
2023-02-06  MAHINDCIE   BUY ₹29.19 at ₹395.20 (fresh Friday signal — BUY: 1.59× weekly, month 2.05×, ladder rising; stop ₹328.94; charges ₹0.0346)
2023-02-07  LSIL        SELL ₹24.34 at stop ₹20.04 (-13.6%, charges ₹0.0252) — the cash goes back to work at the next Friday screen
2023-02-13  CIGNITITEC  BUY ₹25.57 at ₹673.00 (fresh Friday signal — BUY: 3.13× weekly, month 1.41×, ladder rising; stop ₹568.10; charges ₹0.0303)
2023-02-17  CGCL        SELL ₹27.77 at stop ₹704.95 (+17.6%, charges ₹0.0288) — the cash goes back to work at the next Friday screen
2023-02-20  TIIL        BUY ₹27.77 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0329)
2023-03-10  MAHINDCIE   SELL ₹28.86 at stop ₹391.69 (-0.9%, charges ₹0.0299) — the cash goes back to work at the next Friday screen
2023-03-13  KIRLOSIND   BUY ₹28.86 at ₹2,300.00 (fresh Friday signal — ACCUMULATE: 2.65× weekly, month 2.41×, ladder rising; stop ₹2,097.31; charges ₹0.0342)
2023-03-14  KABRAEXTRU  SELL ₹30.23 at stop ₹506.92 (+14.7%, charges ₹0.0314) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹28.87 at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.57×, ladder rising; stop ₹691.46; charges ₹0.0342)
2023-03-20  KRISHANA    SELL ₹31.91 at stop ₹94.40 (+12.9%, charges ₹0.0331) — the cash goes back to work at the next Friday screen
2023-03-27  JINDALSAW   SELL ₹30.47 at stop ₹67.92 (+21.6%, charges ₹0.0316) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹28.97 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.61×, ladder rising; stop ₹372.21; charges ₹0.0343)
2023-03-29  CIGNITITEC  SELL ₹26.73 at stop ₹705.14 (+4.8%, charges ₹0.0277) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹52.07 at stop ₹112.36 (+116.1%, charges ₹0.0540) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹27.59 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.0327)
2023-04-03  INGERRAND   BUY ₹27.54 at ₹2,690.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2023-03-10 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹2,170.84; charges ₹0.0326)
2023-04-03  NATCOPHARM  BUY ₹27.54 at ₹569.80 (fresh Friday signal — ACCUMULATE: 1.84× weekly, month 1.46×, ladder rising; stop ₹494.24; charges ₹0.0326)
2023-04-03  TAX         FY2023 settled: ₹17.4119 paid (STCG ₹58.38 @20%, LTCG ₹45.89 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-24  SHREECEM    SELL ₹27.22 at stop ₹23,636.00 (-3.9%, charges ₹0.0282) — the cash goes back to work at the next Friday screen
2023-05-02  GUJALKALI   BUY ₹29.38 at ₹688.15 (fresh Friday signal — BUY: 22.10× weekly, month 1.42×, ladder rising; stop ₹590.90; charges ₹0.0348)
2023-05-23  GUJALKALI   SELL ₹27.53 at stop ₹646.14 (-6.1%, charges ₹0.0286) — the cash goes back to work at the next Friday screen
2023-05-29  THANGAMAYL  BUY ₹30.32 at ₹1,344.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.50×, ladder rising; stop ₹1,116.30; charges ₹0.0359)
2023-07-03  ANURAS      SELL ₹38.40 at stop ₹1,007.67 (+33.3%, charges ₹0.0398) — the cash goes back to work at the next Friday screen
2023-07-10  GENUSPOWER  BUY ₹31.96 at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.48×, ladder rising; stop ₹99.51; charges ₹0.0379)
2023-07-12  KSB         SELL ₹28.20 at stop ₹407.74 (-2.4%, charges ₹0.0292) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹31.13 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0369)
2023-07-17  THANGAMAYL  SELL ₹30.26 at stop ₹1,344.25 (+0.0%, charges ₹0.0314) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹32.45 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.84×, ladder rising; stop ₹359.10; charges ₹0.0384)
2023-08-14  GANESHHOUC  SELL ₹29.65 at stop ₹418.62 (-8.4%, charges ₹0.0308) — the cash goes back to work at the next Friday screen
2023-08-21  ASTRAZEN    BUY ₹35.60 at ₹4,099.85 (fresh Friday signal — BUY: 6.03× weekly, month 2.40×, ladder rising; stop ₹3,562.50; charges ₹0.0422)
2023-09-13  INGERRAND   SELL ₹30.88 at stop ₹3,022.99 (+12.4%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹34.79 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.67×, ladder rising; stop ₹58.28; charges ₹0.0412)
2023-09-25  KIRLOSIND   SELL ₹40.10 at stop ₹3,202.97 (+39.3%, charges ₹0.0416) — the cash goes back to work at the next Friday screen
2023-10-03  PILANIINVS  BUY ₹37.47 at ₹2,380.05 (fresh Friday signal — BUY: 3.07× weekly, month 7.66×, ladder rising; stop ₹2,018.75; charges ₹0.0444)
2023-10-23  SJVN        SELL ₹30.42 at stop ₹66.03 (-12.4%, charges ₹0.0316) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹36.72 at stop ₹1,840.70 (+33.4%, charges ₹0.0381) — the cash goes back to work at the next Friday screen
2023-10-30  KKCL        BUY ₹37.05 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0439)
2023-10-30  SHAREINDIA  BUY ₹32.72 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0388)
2023-11-01  NATCOPHARM  SELL ₹37.20 at stop ₹771.40 (+35.4%, charges ₹0.0386) — the cash goes back to work at the next Friday screen
2023-11-06  SUNDARMHLD  BUY ₹37.20 at ₹144.75 (fresh Friday signal — BUY: 3.35× weekly, month 1.95×, ladder rising; stop ₹109.72; charges ₹0.0441)
2023-11-16  GENUSPOWER  SELL ₹45.83 at stop ₹234.03 (+43.7%, charges ₹0.0475) — the cash goes back to work at the next Friday screen
2023-11-20  ISMTLTD     BUY ₹39.30 at ₹94.60 (fresh Friday signal — BUY: 5.37× weekly, month 1.93×, ladder rising; stop ₹80.18; charges ₹0.0466)
2023-12-20  ISMTLTD     SELL ₹36.62 at stop ₹88.35 (-6.6%, charges ₹0.0380) — the cash goes back to work at the next Friday screen
2023-12-20  SUNDARMHLD  SELL ₹37.28 at stop ₹145.40 (+0.4%, charges ₹0.0387) — the cash goes back to work at the next Friday screen
2023-12-26  MMFL        BUY ₹42.64 at ₹1,023.60 (fresh Friday signal — BUY: 9.43× weekly, month 3.43×, ladder rising; stop ₹821.80; charges ₹0.0505)
2023-12-26  OIL         BUY ₹37.80 at ₹251.27 (fresh Friday signal — BUY: 6.09× weekly, month 3.92×, ladder rising; stop ₹186.55; charges ₹0.0448)
2024-01-17  TIIL        SELL ₹57.98 at stop ₹2,337.00 (+109.3%, charges ₹0.0601) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹42.64 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0505)
2024-01-30  MMFL        SELL ₹37.91 at stop ₹912.05 (-10.9%, charges ₹0.0393) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹46.91 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0556)
2024-02-09  ASTRAZEN    SELL ₹50.21 at stop ₹5,795.95 (+41.4%, charges ₹0.0521) — the cash goes back to work at the next Friday screen
2024-02-12  IOB         BUY ₹44.76 at ₹71.50 (fresh Friday signal — BUY: 7.81× weekly, month 2.91×, ladder rising; stop ₹38.71; charges ₹0.0530)
2024-03-06  SHAREINDIA  SELL ₹38.87 at stop ₹357.20 (+19.1%, charges ₹0.0403) — the cash goes back to work at the next Friday screen
2024-03-11  DOLLAR      BUY ₹48.72 at ₹527.95 (fresh Friday signal — BUY: 4.55× weekly, month 2.48×, ladder rising; stop ₹461.65; charges ₹0.0577)
2024-03-11  TCI         SELL ₹37.46 at stop ₹790.40 (-20.0%, charges ₹0.0389) — the cash goes back to work at the next Friday screen
2024-03-13  DOLLAR      SELL ₹42.50 at stop ₹461.65 (-12.6%, charges ₹0.0441) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹32.71 at stop ₹674.12 (-11.5%, charges ₹0.0339) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹42.74 at stop ₹666.47 (+0.5%, charges ₹0.0443) — the cash goes back to work at the next Friday screen
2024-03-15  OIL         SELL ₹51.71 at stop ₹344.53 (+37.1%, charges ₹0.0536) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹44.30 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.0525)
2024-03-18  EMUDHRA     BUY ₹32.15 at ₹583.90 (fresh Friday signal — BUY: 1.54× weekly, month 3.10×, ladder rising; stop ₹529.77; charges ₹0.0381)
2024-03-18  FORCEMOT    BUY ₹44.11 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.0523)
2024-03-18  INDIGO      BUY ₹44.22 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0524)
2024-03-18  SOLARINDS   BUY ₹44.29 at ₹8,900.05 (fresh Friday signal — BUY: 4.28× weekly, month 2.84×, ladder rising; stop ₹5,332.29; charges ₹0.0525)
2024-03-27  ANANDRATHI  SELL ₹100.85 at stop ₹862.65 (+224.7%, charges ₹0.1046) — the cash goes back to work at the next Friday screen
2024-04-01  DMART       BUY ₹26.21 at ₹4,570.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.56×, ladder rising; stop ₹3,695.50; charges ₹0.0310)
2024-04-01  SHRIRAMFIN  BUY ₹43.63 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0517)
2024-04-01  TAX         FY2024 settled: ₹31.0226 paid (STCG ₹155.11 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-09  PILANIINVS  SELL ₹58.29 at stop ₹3,710.37 (+55.9%, charges ₹0.0605) — the cash goes back to work at the next Friday screen
2024-05-13  JSWHL       SELL ₹37.26 at stop ₹6,280.45 (+33.6%, charges ₹0.0387) — the cash goes back to work at the next Friday screen
2024-05-13  JWL         BUY ₹44.77 at ₹490.00 (fresh Friday signal — BUY: 7.12× weekly, month 2.51×, ladder rising; stop ₹370.93; charges ₹0.0530)
2024-05-21  KIRLOSBROS  BUY ₹46.65 at ₹1,844.00 (fresh Friday signal — BUY: 5.41× weekly, month 1.62×, ladder rising; stop ₹1,221.51; charges ₹0.0553)
2024-05-28  FORCEMOT    SELL ₹54.16 at stop ₹8,083.64 (+23.1%, charges ₹0.0562) — the cash goes back to work at the next Friday screen
2024-05-31  DMART       SELL ₹24.73 at stop ₹4,322.83 (-5.4%, charges ₹0.0257) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹47.47 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0562)
2024-06-03  THERMAX     BUY ₹35.56 at ₹5,640.00 (fresh Friday signal — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹0.0421)
2024-06-04  BOSCHLTD    SELL ₹43.48 at stop ₹29,015.09 (-1.6%, charges ₹0.0451) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹40.55 at stop ₹441.77 (-6.8%, charges ₹0.0421) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹39.63 at stop ₹7,980.95 (-10.3%, charges ₹0.0411) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹45.28 at ₹783.00 (fresh Friday signal — BUY: 7.38× weekly, month 1.40×, ladder rising; stop ₹632.75; charges ₹0.0537)
2024-06-10  FIEMIND     BUY ₹45.43 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0538)
2024-06-10  UNOMINDA    BUY ₹32.94 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0390)
2024-07-19  UNOMINDA    SELL ₹33.27 at stop ₹981.87 (+1.2%, charges ₹0.0345) — the cash goes back to work at the next Friday screen
2024-07-22  HBLPOWER    BUY ₹33.27 at ₹585.00 (fresh Friday signal — BUY: 3.57× weekly, month 1.41×, ladder rising; stop ₹522.78; charges ₹0.0394)
2024-07-23  FIEMIND     SELL ₹43.18 at stop ₹1,257.56 (-4.7%, charges ₹0.0448) — the cash goes back to work at the next Friday screen
2024-07-29  THYROCARE   BUY ₹43.18 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0512)
2024-08-05  KIRLOSBROS  SELL ₹50.17 at stop ₹1,987.46 (+7.8%, charges ₹0.0520) — the cash goes back to work at the next Friday screen
2024-08-05  THERMAX     SELL ₹29.69 at stop ₹4,719.70 (-16.3%, charges ₹0.0308) — the cash goes back to work at the next Friday screen
2024-08-06  JWL         SELL ₹50.32 at stop ₹552.00 (+12.7%, charges ₹0.0522) — the cash goes back to work at the next Friday screen
2024-08-12  ADANIPOWER  SELL ₹36.51 at stop ₹632.75 (-19.2%, charges ₹0.0379) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹43.99 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0521)
2024-08-12  CERA        BUY ₹43.92 at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹0.0520)
2024-08-12  PCBL        BUY ₹42.27 at ₹393.00 (fresh Friday signal — BUY: 4.82× weekly, month 4.03×, ladder rising; stop ₹246.00; charges ₹0.0501)
2024-08-13  EMUDHRA     SELL ₹43.57 at stop ₹793.11 (+35.8%, charges ₹0.0452) — the cash goes back to work at the next Friday screen
2024-08-16  CAMPUS      SELL ₹45.89 at stop ₹277.07 (-3.1%, charges ₹0.0476) — the cash goes back to work at the next Friday screen
2024-08-19  POLYPLEX    BUY ₹39.32 at ₹1,298.00 (fresh Friday signal — BUY: 2.45× weekly, month 2.33×, ladder rising; stop ₹1,030.80; charges ₹0.0466)
2024-08-19  SUPRIYA     BUY ₹43.30 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0513)
2024-08-19  VGUARD      BUY ₹43.35 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.0514)
2024-09-19  CERA        SELL ₹34.22 at stop ₹8,198.93 (-21.9%, charges ₹0.0355) — the cash goes back to work at the next Friday screen
2024-09-23  ALKYLAMINE  BUY ₹34.22 at ₹2,432.85 (fresh Friday signal — BUY: 9.32× weekly, month 3.52×, ladder rising; stop ₹2,106.24; charges ₹0.0405)
2024-10-03  IOB         SELL ₹35.34 at stop ₹56.57 (-20.9%, charges ₹0.0367) — the cash goes back to work at the next Friday screen
2024-10-04  POLYPLEX    SELL ₹34.03 at stop ₹1,125.80 (-13.3%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹34.68 at stop ₹420.24 (-19.8%, charges ₹0.0360) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹42.04 at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.0498)
2024-10-07  INDIGO      SELL ₹61.85 at stop ₹4,485.14 (+40.2%, charges ₹0.0642) — the cash goes back to work at the next Friday screen
2024-10-07  ITDCEM      BUY ₹42.26 at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹0.0501)
2024-10-07  THYROCARE   SELL ₹43.70 at stop ₹796.15 (+1.4%, charges ₹0.0453) — the cash goes back to work at the next Friday screen
2024-10-14  BSE         BUY ₹41.17 at ₹4,536.00 (fresh Friday signal — BUY: 2.79× weekly, month 4.25×, ladder rising; stop ₹3,393.93; charges ₹0.0488)
2024-10-14  DBCORP      BUY ₹42.14 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0499)
2024-10-14  SKIPPER     BUY ₹41.98 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.0497)
2024-10-18  PCBL        SELL ₹51.18 at stop ₹476.85 (+21.3%, charges ₹0.0531) — the cash goes back to work at the next Friday screen
2024-10-21  MOTILALOFS  BUY ₹40.45 at ₹1,021.95 (fresh Friday signal — BUY: 7.74× weekly, month 5.64×, ladder rising; stop ₹656.59; charges ₹0.0479)
2024-10-22  ALKYLAMINE  SELL ₹29.56 at stop ₹2,106.24 (-13.4%, charges ₹0.0307) — the cash goes back to work at the next Friday screen
2024-10-22  BASF        SELL ₹45.45 at stop ₹7,611.30 (+3.6%, charges ₹0.0471) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹36.08 at stop ₹302.08 (-14.2%, charges ₹0.0374) — the cash goes back to work at the next Friday screen
2024-10-25  HBLPOWER    SELL ₹29.67 at stop ₹522.78 (-10.6%, charges ₹0.0308) — the cash goes back to work at the next Friday screen
2024-10-28  CARERATING  BUY ₹38.38 at ₹1,396.00 (fresh Friday signal — BUY: surged 3.30× weekly on 2024-10-11 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹1,066.23; charges ₹0.0455)
2024-10-28  PAYTM       BUY ₹38.46 at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.0456)
2024-11-04  AKZOINDIA   BUY ₹40.14 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.0948)
2024-11-04  KIRLPNU     BUY ₹34.51 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.0815)
2024-11-14  ASTRAZEN    SELL ₹38.59 at stop ₹6,854.77 (-7.9%, charges ₹0.0857) — the cash goes back to work at the next Friday screen
2024-11-18  JSWHL       BUY ₹38.46 at ₹19,990.00 (fresh Friday signal — BUY: 3.46× weekly, month 4.62×, ladder rising; stop ₹8,434.53; charges ₹0.0908)
2024-12-17  SUPRIYA     SELL ₹58.62 at stop ₹717.25 (+35.8%, charges ₹0.1302) — the cash goes back to work at the next Friday screen
2024-12-23  KIRLPNU     SELL ₹32.29 at stop ₹1,596.00 (-6.0%, charges ₹0.0717) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹40.39 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.0953)
2024-12-27  AKZOINDIA   SELL ₹30.28 at stop ₹3,423.18 (-24.2%, charges ₹0.0672) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹40.09 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.0946)
2024-12-30  KFINTECH    BUY ₹39.95 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.0943)
2025-01-09  KSL         SELL ₹35.73 at stop ₹1,059.30 (-11.1%, charges ₹0.0794) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹45.78 at stop ₹893.05 (+19.4%, charges ₹0.1017) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹36.11 at stop ₹477.28 (-13.7%, charges ₹0.0802) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹36.91 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0871)
2025-01-13  CARERATING  SELL ₹33.97 at stop ₹1,239.70 (-11.2%, charges ₹0.0754) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹36.81 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.0869)
2025-01-15  KFINTECH    SELL ₹30.50 at stop ₹1,159.14 (-23.3%, charges ₹0.0677) — the cash goes back to work at the next Friday screen
2025-01-17  MOTILALOFS  SELL ₹31.12 at stop ₹788.79 (-22.8%, charges ₹0.0691) — the cash goes back to work at the next Friday screen
2025-01-20  HCG         BUY ₹36.95 at ₹504.95 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 1.41×, ladder rising; stop ₹429.63; charges ₹0.0872)
2025-01-24  AEGISLOG    SELL ₹30.83 at stop ₹700.36 (-16.1%, charges ₹0.0685) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹35.71 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0843)
2025-01-28  LLOYDSME    SELL ₹31.99 at stop ₹1,258.75 (-12.7%, charges ₹0.0711) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹36.79 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.0869)
2025-02-12  JINDWORLD   SELL ₹36.63 at stop ₹374.11 (-8.2%, charges ₹0.0814) — the cash goes back to work at the next Friday screen
2025-02-24  GODFRYPHLP  BUY ₹34.84 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.0823)
2025-02-28  BSE         SELL ₹44.81 at stop ₹4,954.63 (+9.2%, charges ₹0.0995) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹33.76 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0797)
2025-03-03  ZENSARTECH  SELL ₹28.15 at stop ₹727.84 (-23.1%, charges ₹0.0625) — the cash goes back to work at the next Friday screen
2025-03-10  GRWRHITECH  BUY ₹35.09 at ₹4,219.95 (fresh Friday signal — BUY: surged 2.69× weekly on 2025-02-14 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹3,504.00; charges ₹0.0828)
2025-03-17  AVANTIFEED  BUY ₹35.47 at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹0.0837)
2025-03-24  INDIASHLTR  BUY ₹37.73 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.0891)
2025-03-24  KSCL        BUY ₹26.41 at ₹1,285.00 (fresh Friday signal — BUY: 3.75× weekly, month 1.42×, ladder rising; stop ₹978.55; charges ₹0.0623)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹27.77 / LT ₹0.00)
2025-04-03  GRWRHITECH  SELL ₹29.83 at stop ₹3,602.82 (-14.6%, charges ₹0.0662) — the cash goes back to work at the next Friday screen
2025-04-07  AVANTIFEED  SELL ₹27.19 at stop ₹648.95 (-23.0%, charges ₹0.0604) — the cash goes back to work at the next Friday screen
2025-04-07  COROMANDEL  BUY ₹29.83 at ₹1,870.00 (fresh Friday signal — BUY: surged 1.58× weekly on 2025-03-21 (month 1.48×), ladder rising NOW — promoted from the ladder watch; stop ₹1,849.08; charges ₹0.0704)
2025-04-07  INDIASHLTR  SELL ₹34.91 at stop ₹738.82 (-7.1%, charges ₹0.0775) — the cash goes back to work at the next Friday screen
2025-04-11  ITDCEM      SELL ₹33.75 at stop ₹524.92 (-19.9%, charges ₹0.0750) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹37.91 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.0895)
2025-04-15  INDIASHLTR  BUY ₹38.05 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.0898)
2025-04-28  WHIRLPOOL   BUY ₹19.90 at ₹1,153.90 (fresh Friday signal — BUY: 2.21× weekly, month 1.77×, ladder rising; stop ₹1,017.54; charges ₹0.0470)
2025-05-15  KSCL        SELL ₹27.30 at stop ₹1,334.75 (+3.9%, charges ₹0.0606) — the cash goes back to work at the next Friday screen
2025-05-19  CARERATING  BUY ₹27.30 at ₹1,527.50 (fresh Friday signal — BUY: 11.23× weekly, month 2.66×, ladder rising; stop ₹1,144.84; charges ₹0.0645)
2025-05-26  HCG         SELL ₹40.73 at stop ₹559.08 (+10.7%, charges ₹0.0905) — the cash goes back to work at the next Friday screen
2025-06-02  TECHNOE     BUY ₹39.19 at ₹1,421.00 (fresh Friday signal — BUY: 6.29× weekly, month 1.64×, ladder rising; stop ₹1,150.36; charges ₹0.0925)
2025-06-27  COROMANDEL  SELL ₹35.67 at stop ₹2,246.75 (+20.1%, charges ₹0.0792) — the cash goes back to work at the next Friday screen
2025-06-30  ALKYLAMINE  BUY ₹37.21 at ₹2,263.00 (fresh Friday signal — BUY: 7.48× weekly, month 1.62×, ladder rising; stop ₹1,832.27; charges ₹0.0878)
2025-07-24  TECHNOE     SELL ₹40.29 at stop ₹1,467.84 (+3.3%, charges ₹0.0895) — the cash goes back to work at the next Friday screen
2025-07-28  BOMDYEING   BUY ₹39.69 at ₹181.45 (fresh Friday signal — BUY: 21.87× weekly, month 4.30×, ladder rising; stop ₹148.64; charges ₹0.0937)
2025-07-31  CARERATING  SELL ₹30.31 at stop ₹1,703.35 (+11.5%, charges ₹0.0673) — the cash goes back to work at the next Friday screen
2025-08-04  JSWHL       SELL ₹36.59 at stop ₹19,106.01 (-4.4%, charges ₹0.0813) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹42.06 at stop ₹1,814.78 (+25.2%, charges ₹0.0934) — the cash goes back to work at the next Friday screen
2025-08-04  PGHL        BUY ₹30.91 at ₹6,440.00 (fresh Friday signal — BUY: 6.30× weekly, month 2.58×, ladder rising; stop ₹5,320.00; charges ₹0.0730)
2025-08-07  ALKYLAMINE  SELL ₹34.17 at stop ₹2,087.62 (-7.7%, charges ₹0.0759) — the cash goes back to work at the next Friday screen
2025-08-07  WHIRLPOOL   SELL ₹22.35 at stop ₹1,301.97 (+12.8%, charges ₹0.0496) — the cash goes back to work at the next Friday screen
2025-08-11  RAIN        BUY ₹38.30 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.0904)
2025-08-11  UPL         BUY ₹38.24 at ₹688.95 (fresh Friday signal — ACCUMULATE: 1.66× weekly, month 1.47×, ladder rising; stop ₹625.10; charges ₹0.0903)
2025-08-18  BLACKBUCK   BUY ₹38.56 at ₹553.00 (fresh Friday signal — ACCUMULATE: 3.19× weekly, month 4.96×, ladder rising; stop ₹473.20; charges ₹0.0910)
2025-08-18  THYROCARE   BUY ₹20.08 at ₹1,408.00 (fresh Friday signal — BUY: surged 5.43× weekly on 2025-07-25 (month 1.57×), ladder rising NOW — promoted from the ladder watch; stop ₹1,171.92; charges ₹0.0474)
2025-08-26  RAIN        SELL ₹34.17 at stop ₹143.64 (-10.4%, charges ₹0.0759) — the cash goes back to work at the next Friday screen
2025-09-01  RSYSTEMS    BUY ₹34.17 at ₹460.00 (fresh Friday signal — BUY: surged 17.81× weekly on 2025-08-22 (month 4.67×), ladder rising NOW — promoted from the ladder watch; stop ₹394.44; charges ₹0.0807)
2025-09-15  THYROCARE   SELL ₹16.82 at stop ₹1,184.93 (-15.8%, charges ₹0.0374) — the cash goes back to work at the next Friday screen
2025-09-16  GODFRYPHLP  SELL ₹53.81 at stop ₹8,967.50 (+55.1%, charges ₹0.1195) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹38.00 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.75× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.0897)
2025-09-22  FLUOROCHEM  BUY ₹32.63 at ₹3,820.00 (fresh Friday signal — BUY: 5.40× weekly, month 2.64×, ladder rising; stop ₹3,396.25; charges ₹0.0770)
2025-09-24  RSYSTEMS    SELL ₹31.30 at stop ₹423.23 (-8.0%, charges ₹0.0695) — the cash goes back to work at the next Friday screen
2025-09-25  BOMDYEING   SELL ₹37.60 at stop ₹172.67 (-4.8%, charges ₹0.0835) — the cash goes back to work at the next Friday screen
2025-09-25  INDIASHLTR  SELL ₹37.77 at stop ₹862.60 (-0.3%, charges ₹0.0839) — the cash goes back to work at the next Friday screen
2025-09-29  LGBBROSLTD  BUY ₹37.04 at ₹1,411.60 (fresh Friday signal — BUY: 3.53× weekly, month 1.72×, ladder rising; stop ₹1,258.75; charges ₹0.0874)
2025-09-29  NETWEB      BUY ₹32.79 at ₹3,700.00 (fresh Friday signal — BUY: 2.97× weekly, month 7.27×, ladder rising; stop ₹2,674.79; charges ₹0.0774)
2025-09-29  SUBROS      BUY ₹36.84 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0870)
2025-10-14  SUBROS      SELL ₹33.92 at stop ₹1,046.90 (-7.5%, charges ₹0.0753) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹33.92 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0801)
2025-10-20  CREDITACC   SELL ₹53.29 at stop ₹1,274.42 (+49.9%, charges ₹0.1184) — the cash goes back to work at the next Friday screen
2025-10-27  MAHABANK    BUY ₹37.02 at ₹59.00 (fresh Friday signal — ACCUMULATE: 1.84× weekly, month 1.48×, ladder rising; stop ₹53.69; charges ₹0.0874)
2025-10-28  BLACKBUCK   SELL ₹44.57 at stop ₹642.20 (+16.1%, charges ₹0.0990) — the cash goes back to work at the next Friday screen
2025-11-03  M&MFIN      BUY ₹23.13 at ₹316.55 (fresh Friday signal — BUY: 3.42× weekly, month 1.43×, ladder rising; stop ₹281.39; charges ₹0.0546)
2025-11-03  TDPOWERSYS  BUY ₹37.71 at ₹382.27 (fresh Friday signal — BUY: 4.87× weekly, month 1.95×, ladder rising; stop ₹276.78; charges ₹0.0890)
2025-11-06  FDC         SELL ₹32.90 at stop ₹425.79 (-13.0%, charges ₹0.0731) — the cash goes back to work at the next Friday screen
2025-11-06  NETWEB      SELL ₹31.01 at stop ₹3,515.95 (-5.0%, charges ₹0.0689) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹28.37 at stop ₹5,938.45 (-7.8%, charges ₹0.0630) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹37.68 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.0889)
2025-11-10  CUB         BUY ₹37.87 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.0894)
2025-11-20  ANANDRATHI  SELL ₹31.10 at stop ₹1,450.17 (-7.9%, charges ₹0.0691) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹36.08 at stop ₹976.41 (-3.8%, charges ₹0.0801) — the cash goes back to work at the next Friday screen
2025-11-24  FLUOROCHEM  SELL ₹29.01 at stop ₹3,412.02 (-10.7%, charges ₹0.0644) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹38.30 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0904)
2025-11-24  TDPOWERSYS  SELL ₹35.11 at stop ₹357.49 (-6.5%, charges ₹0.0780) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹38.01 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.33×, ladder rising; stop ₹535.37; charges ₹0.0897)
2025-12-01  GRAVITA     BUY ₹33.79 at ₹1,825.10 (fresh Friday signal — BUY: 2.31× weekly, month 1.47×, ladder rising; stop ₹1,592.29; charges ₹0.0798)
2025-12-01  SANSERA     BUY ₹37.94 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.0896)
2026-01-07  M&MFIN      SELL ₹26.24 at stop ₹360.81 (+14.0%, charges ₹0.0583) — the cash goes back to work at the next Friday screen
2026-01-08  EUREKAFORB  SELL ₹33.57 at stop ₹589.10 (-11.3%, charges ₹0.0746) — the cash goes back to work at the next Friday screen
2026-01-09  GRAVITA     SELL ₹30.94 at stop ₹1,678.56 (-8.0%, charges ₹0.0687) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹34.27 at stop ₹2,956.49 (-10.1%, charges ₹0.0761) — the cash goes back to work at the next Friday screen
2026-01-12  HINDCOPPER  BUY ₹37.40 at ₹532.00 (fresh Friday signal — BUY: surged 1.55× weekly on 2025-12-12 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹456.95; charges ₹0.0883)
2026-01-12  NATIONALUM  BUY ₹37.43 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.0884)
2026-01-19  RBA         BUY ₹37.55 at ₹67.50 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.51×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.0887)
2026-01-20  LGBBROSLTD  SELL ₹44.76 at stop ₹1,713.80 (+21.4%, charges ₹0.0994) — the cash goes back to work at the next Friday screen
2026-01-20  UPL         SELL ₹40.28 at stop ₹729.12 (+5.8%, charges ₹0.0895) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹34.53 at stop ₹748.60 (-8.5%, charges ₹0.0767) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹36.10 at stop ₹1,672.76 (-4.4%, charges ₹0.0802) — the cash goes back to work at the next Friday screen
2026-02-17  NATIONALUM  SELL ₹35.51 at stop ₹335.49 (-4.7%, charges ₹0.0789) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹36.04 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.67×, ladder rising; stop ₹5,440.18; charges ₹0.0851)
2026-02-23  ACUTAAS     BUY ₹22.88 at ₹2,123.60 (fresh Friday signal — BUY: surged 1.51× weekly on 2026-02-13 (month 1.41×), ladder rising NOW — promoted from the ladder watch; stop ₹1,905.41; charges ₹0.0540)
2026-02-23  E2E         BUY ₹36.48 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0861)
2026-02-23  HAPPYFORGE  BUY ₹35.91 at ₹1,370.00 (fresh Friday signal — BUY: surged 6.09× weekly on 2026-02-13 (month 1.85×), ladder rising NOW — promoted from the ladder watch; stop ₹1,188.64; charges ₹0.0848)
2026-02-23  TORNTPOWER  BUY ₹35.93 at ₹1,540.00 (fresh Friday signal — BUY: 1.78× weekly, month 1.47×, ladder rising; stop ₹1,315.84; charges ₹0.0848)
2026-02-23  VESUVIUS    BUY ₹36.59 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.0864)
2026-03-04  HAPPYFORGE  SELL ₹32.20 at stop ₹1,234.05 (-9.9%, charges ₹0.0715) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹37.28 at stop ₹251.43 (-1.1%, charges ₹0.0828) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹36.99 at stop ₹528.63 (-0.6%, charges ₹0.0822) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹33.83 at stop ₹61.08 (-9.5%, charges ₹0.0751) — the cash goes back to work at the next Friday screen
2026-03-16  J&KBANK     BUY ₹33.87 at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.95×, ladder rising; stop ₹103.27; charges ₹0.0800)
2026-03-16  JBCHEPHARM  BUY ₹33.93 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0801)
2026-03-23  J&KBANK     SELL ₹30.80 at stop ₹110.67 (-8.6%, charges ₹0.0684) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹31.60 at stop ₹464.31 (-13.2%, charges ₹0.0702) — the cash goes back to work at the next Friday screen
2026-03-23  VTL         BUY ₹33.03 at ₹534.00 (fresh Friday signal — BUY: surged 1.53× weekly on 2026-02-27 (month 2.21×), ladder rising NOW — promoted from the ladder watch; stop ₹485.45; charges ₹0.0780)
2026-03-30  AETHER      BUY ₹33.04 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0780)
2026-03-30  MAHABANK    SELL ₹38.13 at stop ₹61.05 (+3.5%, charges ₹0.0847) — the cash goes back to work at the next Friday screen
2026-03-30  TORNTPOWER  SELL ₹30.56 at stop ₹1,315.84 (-14.6%, charges ₹0.0679) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹44.25 / LT ₹0.00)
2026-04-06  AUROPHARMA  BUY ₹32.43 at ₹1,344.00 (fresh Friday signal — BUY: surged 1.58× weekly on 2026-03-13 (month 1.44×), ladder rising NOW — promoted from the ladder watch; stop ₹1,178.00; charges ₹0.0765)
2026-04-06  CHENNPETRO  BUY ₹32.46 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0766)
2026-04-06  INOXINDIA   BUY ₹32.56 at ₹1,253.90 (fresh Friday signal — BUY: 2.23× weekly, month 1.48×, ladder rising; stop ₹1,067.80; charges ₹0.0769)
2026-04-13  THERMAX     BUY ₹33.74 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.0797)
2026-05-13  INOXINDIA   SELL ₹35.47 at stop ₹1,372.18 (+9.4%, charges ₹0.0788) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹32.18 at stop ₹1,125.84 (-2.1%, charges ₹0.0715) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹35.41 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.0836)
2026-05-18  CAPLIPOINT  BUY ₹35.40 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.0836)
2026-06-05  E2E         SELL ₹29.04 at stop ₹2,330.72 (-20.0%, charges ₹0.0645) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹32.23 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0761)
2026-06-15  AUROPHARMA  SELL ₹33.71 at stop ₹1,403.53 (+4.4%, charges ₹0.0749) — the cash goes back to work at the next Friday screen
2026-06-22  GARFIBRES   BUY ₹33.71 at ₹796.00 (fresh Friday signal — BUY: 14.56× weekly, month 3.47×, ladder rising; stop ₹639.35; charges ₹0.0796)
2026-07-28  ACUTAAS     SELL ₹34.11 at stop ₹3,180.60 (+49.8%, charges ₹0.0758) — the cash goes back to work at the next Friday screen
2026-07-29  THERMAX     SELL ₹40.23 at stop ₹4,306.64 (+19.8%, charges ₹0.0893) — the cash goes back to work at the next Friday screen
2026-07-31  VTL         SELL ₹36.50 at stop ₹592.80 (+11.0%, charges ₹0.0811) — the cash goes back to work at the next Friday screen
2026-08-03  BLUESTONE   BUY ₹39.30 at ₹823.40 (fresh Friday signal — ACCUMULATE: 5.63× weekly, month 9.43×, ladder rising; stop ₹664.75; charges ₹0.0928)
2026-08-03  SENCO       BUY ₹32.21 at ₹408.90 (fresh Friday signal — BUY: 3.65× weekly, month 2.69×, ladder rising; stop ₹337.25; charges ₹0.0760)
2026-08-03  TMB         BUY ₹39.32 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.0928)
2026-08-12  SENCO       SELL ₹27.25 at stop ₹347.45 (-15.0%, charges ₹0.0605) — the cash goes back to work at the next Friday screen
2026-08-17  TIIL        BUY ₹27.25 at ₹3,125.00 (fresh Friday signal — BUY: 17.87× weekly, month 4.24×, ladder rising; stop ₹2,237.25; charges ₹0.0643)
2026-09-10  ALKYLAMINE  SELL ₹39.59 at stop ₹1,920.99 (+12.3%, charges ₹0.0879) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹42.16 at stop ₹7,158.25 (+17.5%, charges ₹0.0937) — the cash goes back to work at the next Friday screen
2026-09-15  SUNDRMFAST  BUY ₹39.59 at ₹1,277.30 (fresh Friday signal — BUY: 3.14× weekly, month 1.81×, ladder rising; stop ₹1,127.74; charges ₹0.0935)
2026-09-21  AVALON      BUY ₹39.92 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.0942)
```
