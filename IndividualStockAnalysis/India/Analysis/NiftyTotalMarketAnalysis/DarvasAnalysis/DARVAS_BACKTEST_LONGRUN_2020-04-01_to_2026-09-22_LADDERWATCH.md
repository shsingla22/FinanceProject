# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 1388 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹200.80** | **+11.38% a year** |
| The same system before costs and taxes | ₹242.92 | +14.70% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹289.64 | +17.87% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹200.80** (+11.38% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 506 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹14.85** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹30.92**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹9.43 | ₹0.00 | ₹1.8870 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹4.06 | ₹51.97 | ₹7.3076 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹46.79 | ₹0.00 | ₹9.3581 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹61.85 | ₹0.00 | ₹12.3695 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹10.41 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹47.08 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹40.76 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 126.90 | +26.9% | +27.5% | +70.1% |
| 2021 (2021-12-31) | 179.72 | +41.6% | +44.0% | +26.2% |
| 2022 (2022-12-30) | 211.84 | +17.9% | +24.4% | +4.3% |
| 2023 (2023-12-29) | 275.38 | +30.0% | +33.2% | +20.0% |
| 2024 (2024-12-27) | 267.17 | -3.0% | +3.5% | +9.6% |
| 2025 (2025-12-26) | 217.15 | -18.7% | -17.5% | +9.4% |
| 2026 (2026-09-22) | 200.80 | -7.5% | -6.5% | -10.1% |

## What it took to earn it

- **Maximum drawdown: -42.8%** (peak 2024-02-23 → trough 2026-04-02, on weekly closes).
- **235 closed trades**: 86 winners (37%), average winner +29.3%, average loser -9.4%.
- Best closed trade KIRLFER +354.1%; worst ZENSARTECH -23.1%.
- Median holding period 56 days.
- Cash share of equity averaged 10% across all weeks (median 3%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.38 | 49.96 | 5 |
| 2020-05-29 | 100.25 | 8.82 | 9 |
| 2020-06-26 | 117.95 | 0.00 | 10 |
| 2020-07-31 | 126.61 | 0.00 | 10 |
| 2020-08-28 | 131.61 | 0.00 | 10 |
| 2020-09-25 | 121.16 | 55.88 | 5 |
| 2020-10-30 | 114.49 | 8.55 | 9 |
| 2020-11-27 | 123.17 | 0.00 | 10 |
| 2020-12-24 | 126.90 | 47.55 | 6 |
| 2021-01-29 | 138.01 | 24.84 | 8 |
| 2021-02-26 | 145.09 | 12.84 | 9 |
| 2021-03-26 | 142.71 | 1.40 | 9 |
| 2021-04-30 | 149.25 | 20.17 | 8 |
| 2021-05-28 | 159.83 | 5.08 | 9 |
| 2021-06-25 | 174.79 | 5.08 | 9 |
| 2021-07-30 | 193.92 | 5.08 | 9 |
| 2021-08-27 | 174.86 | 30.14 | 8 |
| 2021-09-24 | 180.93 | 16.78 | 9 |
| 2021-10-29 | 182.66 | 16.19 | 9 |
| 2021-11-26 | 183.94 | 57.01 | 7 |
| 2021-12-31 | 179.72 | 5.43 | 10 |
| 2022-01-28 | 184.16 | 19.89 | 9 |
| 2022-02-25 | 163.75 | 80.06 | 5 |
| 2022-03-25 | 180.65 | 15.42 | 9 |
| 2022-04-29 | 196.91 | 11.20 | 9 |
| 2022-05-27 | 184.93 | 26.08 | 8 |
| 2022-06-24 | 188.13 | 4.75 | 9 |
| 2022-07-29 | 203.64 | 4.75 | 9 |
| 2022-08-26 | 215.66 | 9.98 | 9 |
| 2022-09-30 | 203.79 | 20.63 | 9 |
| 2022-10-28 | 216.19 | 0.20 | 10 |
| 2022-11-25 | 209.29 | 62.02 | 7 |
| 2022-12-30 | 211.84 | 9.87 | 10 |
| 2023-01-27 | 206.84 | 50.50 | 8 |
| 2023-02-24 | 200.70 | 23.64 | 9 |
| 2023-03-31 | 200.48 | 19.74 | 10 |
| 2023-04-28 | 205.95 | 13.40 | 10 |
| 2023-05-26 | 204.42 | 36.73 | 9 |
| 2023-06-30 | 217.97 | 0.00 | 11 |
| 2023-07-28 | 228.20 | 7.67 | 10 |
| 2023-08-25 | 238.15 | 5.01 | 10 |
| 2023-09-29 | 245.72 | 0.00 | 10 |
| 2023-10-27 | 244.55 | 62.75 | 7 |
| 2023-11-24 | 252.65 | 0.00 | 10 |
| 2023-12-29 | 275.38 | 0.00 | 10 |
| 2024-01-25 | 295.25 | 0.00 | 11 |
| 2024-02-23 | 314.46 | 13.24 | 10 |
| 2024-03-28 | 279.54 | 0.00 | 10 |
| 2024-04-26 | 283.41 | 0.00 | 10 |
| 2024-05-31 | 278.35 | 0.00 | 10 |
| 2024-06-28 | 294.84 | 25.88 | 9 |
| 2024-07-26 | 288.38 | 78.03 | 7 |
| 2024-08-30 | 298.76 | 0.00 | 10 |
| 2024-09-27 | 301.91 | 0.00 | 10 |
| 2024-10-25 | 272.58 | 24.96 | 10 |
| 2024-11-29 | 286.90 | 0.00 | 11 |
| 2024-12-27 | 267.17 | 21.29 | 10 |
| 2025-01-31 | 251.22 | 122.22 | 5 |
| 2025-02-28 | 227.42 | 121.41 | 5 |
| 2025-03-27 | 239.96 | 0.00 | 10 |
| 2025-04-25 | 240.26 | 9.40 | 9 |
| 2025-05-30 | 247.50 | 4.25 | 9 |
| 2025-06-27 | 250.75 | 25.74 | 8 |
| 2025-07-25 | 237.23 | 22.74 | 8 |
| 2025-08-29 | 247.08 | 21.07 | 8 |
| 2025-09-26 | 234.61 | 40.84 | 8 |
| 2025-10-31 | 223.12 | 27.64 | 10 |
| 2025-11-28 | 220.79 | 58.76 | 8 |
| 2025-12-26 | 217.15 | 0.00 | 11 |
| 2026-01-30 | 210.50 | 104.77 | 5 |
| 2026-02-27 | 200.39 | 0.85 | 10 |
| 2026-03-27 | 183.72 | 35.88 | 8 |
| 2026-04-30 | 197.65 | 0.23 | 10 |
| 2026-05-29 | 209.72 | 0.00 | 10 |
| 2026-06-25 | 203.95 | 0.00 | 10 |
| 2026-07-31 | 208.42 | 43.19 | 8 |
| 2026-08-28 | 209.54 | 0.89 | 10 |
| 2026-09-22 | 200.80 | 1.13 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,392.00 | 1,242.60 | +40.7% |
| GODREJAGRO | 2026-09-07 | 648.15 | 653.90 | 606.77 | +0.9% |
| INOXINDIA | 2026-09-21 | 2,098.80 | 2,133.70 | 1,972.58 | +1.7% |
| IPCALAB | 2026-09-21 | 2,012.00 | 1,992.40 | 1,833.31 | -1.0% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| LTFOODS | 2026-09-15 | 439.90 | 421.35 | 408.07 | -4.2% |
| MEGH | 2021-04-19 | 116.15 | 138.25 | 107.93 | +19.0% |
| METROPOLIS | 2026-05-18 | 522.50 | 592.40 | 539.60 | +13.4% |
| NAVINFLUOR | 2026-09-07 | 8,557.50 | 8,438.00 | 7,704.50 | -1.4% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| GREENPLY | 2020-05-04 | 100.05 | 2020-05-08 | 89.49 | -10.6% |
| JKPAPER | 2020-05-11 | 96.95 | 2020-05-26 | 87.25 | -10.0% |
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| PANACEABIO | 2020-06-01 | 153.00 | 2020-08-20 | 184.01 | +20.3% |
| NESTLEIND | 2020-04-27 | 879.25 | 2020-09-01 | 793.25 | -9.8% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| BALAJITELE | 2020-05-04 | 61.40 | 2020-09-09 | 74.07 | +20.6% |
| SIYSIL | 2020-09-07 | 150.70 | 2020-09-21 | 136.36 | -9.5% |
| BBL | 2020-09-07 | 400.00 | 2020-09-21 | 370.31 | -7.4% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| DEEPAKFERT | 2020-05-11 | 101.00 | 2020-09-22 | 154.26 | +52.7% |
| MOREPENLAB | 2020-05-11 | 17.05 | 2020-09-24 | 22.56 | +32.3% |
| GUJALKALI | 2020-09-14 | 342.45 | 2020-10-13 | 317.35 | -7.3% |
| SASKEN | 2020-10-19 | 735.00 | 2020-10-26 | 651.70 | -11.3% |
| VINATIORGA | 2020-09-28 | 1,294.60 | 2020-11-06 | 1,114.87 | -13.9% |
| OAL | 2020-11-09 | 485.00 | 2020-12-21 | 510.34 | +5.2% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| DPSCLTD | 2020-08-24 | 11.80 | 2020-12-22 | 9.82 | -16.8% |
| FINEORG | 2020-09-14 | 2,900.00 | 2020-12-23 | 2,342.46 | -19.2% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| J&KBANK | 2020-12-28 | 23.85 | 2021-01-28 | 26.36 | +10.5% |
| CESC | 2021-02-01 | 61.51 | 2021-02-02 | 63.66 | +3.5% |
| INOXLEISUR | 2021-02-08 | 333.15 | 2021-02-23 | 296.40 | -11.0% |
| PUNJABCHEM | 2020-09-28 | 630.20 | 2021-03-18 | 868.82 | +37.9% |
| RUBYMILLS | 2020-12-28 | 192.25 | 2021-03-18 | 171.43 | -10.8% |
| PCJEWELLER | 2020-12-28 | 2.52 | 2021-03-19 | 2.66 | +5.6% |
| ZOTA | 2021-02-01 | 155.60 | 2021-03-30 | 142.03 | -8.7% |
| CENTRUM | 2020-09-28 | 15.95 | 2021-04-12 | 24.89 | +56.1% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| TCNSBRANDS | 2021-03-22 | 510.15 | 2021-04-12 | 471.72 | -7.5% |
| IOB | 2021-03-22 | 15.85 | 2021-04-28 | 14.82 | -6.5% |
| KIRLFER | 2020-06-15 | 61.55 | 2021-08-10 | 279.49 | +354.1% |
| KESORAMIND | 2020-11-02 | 40.35 | 2021-08-10 | 85.78 | +112.6% |
| CENTRALBK | 2021-03-01 | 20.00 | 2021-08-10 | 21.09 | +5.4% |
| BODALCHEM | 2021-04-19 | 87.00 | 2021-08-10 | 107.92 | +24.0% |
| MARKSANS | 2021-05-03 | 70.95 | 2021-08-10 | 77.14 | +8.7% |
| IFGLEXPOR | 2021-04-05 | 326.10 | 2021-08-23 | 314.39 | -3.6% |
| BBL | 2021-08-16 | 704.80 | 2021-08-23 | 634.17 | -10.0% |
| SHANTIGEAR | 2021-08-16 | 182.10 | 2021-09-21 | 164.87 | -9.5% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| INDOCO | 2021-08-16 | 484.30 | 2021-11-12 | 412.30 | -14.9% |
| KKCL | 2021-11-01 | 1,227.00 | 2021-11-15 | 1,130.50 | -7.9% |
| EMAMIPAP | 2021-04-19 | 125.00 | 2021-11-22 | 141.55 | +13.2% |
| HATSUN | 2021-08-30 | 1,055.00 | 2021-11-22 | 1,255.19 | +19.0% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| ALLCARGO | 2020-09-28 | 131.30 | 2021-11-29 | 310.33 | +136.4% |
| SHANKARA | 2021-08-16 | 593.00 | 2021-11-29 | 489.25 | -17.5% |
| MAHLOG | 2021-08-30 | 805.00 | 2021-11-30 | 654.55 | -18.7% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| ESABINDIA | 2021-09-27 | 2,187.65 | 2021-12-20 | 2,698.00 | +23.3% |
| TVTODAY | 2021-11-22 | 320.24 | 2022-01-24 | 311.68 | -2.7% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| ONMOBILE | 2022-02-14 | 126.10 | 2022-02-15 | 129.75 | +2.9% |
| RVNL | 2021-11-15 | 38.00 | 2022-02-18 | 32.77 | -13.8% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| CHAMBLFERT | 2021-12-06 | 407.45 | 2022-02-24 | 353.85 | -13.2% |
| RAJESHEXPO | 2021-12-06 | 751.80 | 2022-02-24 | 748.32 | -0.5% |
| MAHLIFE | 2022-02-21 | 305.00 | 2022-02-24 | 286.85 | -6.0% |
| PSPPROJECT | 2022-02-21 | 538.00 | 2022-02-24 | 482.13 | -10.4% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| AVTNPL | 2022-03-07 | 89.95 | 2022-05-05 | 105.99 | +17.8% |
| GAEL | 2022-02-21 | 93.58 | 2022-05-09 | 145.28 | +55.3% |
| GODFRYPHLP | 2022-05-02 | 1,219.00 | 2022-05-09 | 1,130.50 | -7.3% |
| EVEREADY | 2022-03-28 | 344.00 | 2022-05-11 | 310.46 | -9.8% |
| MOL | 2022-05-09 | 129.80 | 2022-05-11 | 113.62 | -12.5% |
| RIIL | 2021-12-27 | 845.00 | 2022-05-26 | 863.73 | +2.2% |
| HUHTAMAKI | 2022-05-16 | 178.20 | 2022-05-26 | 161.50 | -9.4% |
| GEPIL | 2022-05-16 | 176.10 | 2022-05-31 | 163.45 | -7.2% |
| RAJRATAN | 2022-06-06 | 714.95 | 2022-06-14 | 653.60 | -8.6% |
| JKIL | 2022-05-16 | 222.90 | 2022-08-05 | 308.80 | +38.5% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| RAJMET | 2022-02-28 | 265.00 | 2022-09-15 | 359.30 | +35.6% |
| NAVNETEDUL | 2022-08-08 | 130.50 | 2022-09-26 | 127.30 | -2.5% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| TIMETECHNO | 2022-05-16 | 91.25 | 2022-11-21 | 95.09 | +4.2% |
| MIDHANI | 2022-10-03 | 204.40 | 2022-11-21 | 224.20 | +9.7% |
| GODREJAGRO | 2022-05-30 | 526.00 | 2022-11-23 | 456.63 | -13.2% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| SAFARI | 2022-09-12 | 765.00 | 2022-12-22 | 796.58 | +4.1% |
| IRCON | 2022-11-28 | 61.40 | 2022-12-22 | 56.81 | -7.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| IRFC | 2022-11-28 | 32.00 | 2022-12-23 | 28.20 | -11.9% |
| KSL | 2022-12-26 | 330.10 | 2023-01-27 | 328.23 | -0.6% |
| WABAG | 2022-12-26 | 304.45 | 2023-01-27 | 308.85 | +1.4% |
| GICRE | 2022-12-26 | 157.00 | 2023-02-01 | 167.72 | +6.8% |
| JBMA | 2023-01-30 | 263.32 | 2023-02-07 | 246.34 | -6.5% |
| TRIL | 2023-02-06 | 70.90 | 2023-02-14 | 62.10 | -12.4% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| USHAMART | 2023-01-30 | 179.95 | 2023-02-22 | 166.25 | -7.6% |
| KABRAEXTRU | 2022-12-26 | 441.95 | 2023-03-14 | 506.92 | +14.7% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| CIGNITITEC | 2023-02-20 | 731.95 | 2023-03-29 | 705.14 | -3.7% |
| ROUTE | 2023-02-27 | 1,338.25 | 2023-04-11 | 1,231.11 | -8.0% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| ACCELYA | 2023-05-02 | 1,404.95 | 2023-05-05 | 1,294.61 | -7.9% |
| DCAL | 2023-03-20 | 134.50 | 2023-05-24 | 115.42 | -14.2% |
| VSSL | 2023-02-13 | 345.70 | 2023-05-26 | 324.52 | -6.1% |
| MAHABANK | 2022-11-28 | 27.60 | 2023-06-15 | 27.79 | +0.7% |
| KSB | 2023-03-27 | 417.98 | 2023-07-12 | 407.74 | -2.4% |
| THANGAMAYL | 2023-05-29 | 1,344.00 | 2023-07-17 | 1,344.25 | +0.0% |
| GANESHHOUC | 2023-07-24 | 457.00 | 2023-08-14 | 418.62 | -8.4% |
| INGERRAND | 2023-04-03 | 2,690.00 | 2023-09-13 | 3,022.99 | +12.4% |
| SIS | 2023-05-08 | 384.35 | 2023-09-21 | 424.60 | +10.5% |
| OLECTRA | 2023-03-27 | 634.90 | 2023-10-19 | 1,121.00 | +76.6% |
| VSTTILLERS | 2023-06-19 | 2,812.30 | 2023-10-23 | 3,516.05 | +25.0% |
| GHCL | 2023-09-18 | 648.00 | 2023-10-23 | 582.83 | -10.1% |
| IOB | 2023-09-25 | 44.40 | 2023-10-23 | 39.62 | -10.8% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| SWARAJENG | 2023-05-29 | 1,809.90 | 2024-01-29 | 2,210.32 | +22.1% |
| 3MINDIA | 2024-01-23 | 34,850.00 | 2024-02-13 | 31,629.68 | -9.2% |
| GLS | 2023-04-17 | 418.00 | 2024-03-05 | 779.48 | +86.5% |
| IIFLSEC | 2023-10-30 | 100.40 | 2024-03-05 | 132.05 | +31.5% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| TCI | 2024-02-05 | 987.60 | 2024-03-11 | 790.40 | -20.0% |
| TIPSINDLTD | 2023-10-23 | 358.00 | 2024-03-13 | 453.39 | +26.6% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| JINDWORLD | 2024-03-18 | 331.00 | 2024-03-19 | 341.71 | +3.2% |
| PILANIINVS | 2024-03-11 | 3,893.90 | 2024-05-09 | 3,710.37 | -4.7% |
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| PSB | 2024-03-11 | 64.10 | 2024-05-13 | 54.09 | -15.6% |
| SOLARINDS | 2024-03-18 | 8,900.05 | 2024-06-04 | 7,980.95 | -10.3% |
| ICICIGI | 2024-03-18 | 1,646.00 | 2024-06-04 | 1,543.84 | -6.2% |
| VIJAYA | 2024-05-21 | 803.00 | 2024-06-25 | 730.50 | -9.0% |
| TEJASNET | 2024-05-13 | 1,124.95 | 2024-07-10 | 1,313.90 | +16.8% |
| SUDARSCHEM | 2024-05-21 | 832.00 | 2024-07-10 | 859.23 | +3.3% |
| BHARATRAS | 2024-06-10 | 2,646.25 | 2024-07-10 | 2,743.14 | +3.7% |
| ELECON | 2024-07-15 | 650.48 | 2024-07-18 | 603.25 | -7.3% |
| TRENT | 2024-03-11 | 2,654.67 | 2024-07-22 | 3,464.36 | +30.5% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| ROUTE | 2024-07-01 | 1,814.45 | 2024-07-26 | 1,663.69 | -8.3% |
| POLYMED | 2024-07-15 | 2,100.00 | 2024-08-01 | 1,861.67 | -11.3% |
| AVANTIFEED | 2024-07-29 | 697.65 | 2024-09-09 | 650.13 | -6.8% |
| KIOCL | 2023-08-21 | 223.00 | 2024-10-07 | 352.88 | +58.2% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| SAREGAMA | 2024-10-14 | 589.85 | 2024-10-15 | 541.54 | -8.2% |
| PCBL | 2024-08-05 | 364.05 | 2024-10-18 | 476.85 | +31.0% |
| IIFL | 2024-10-21 | 452.35 | 2024-10-24 | 391.93 | -13.4% |
| CMSINFO | 2024-03-26 | 384.65 | 2024-10-28 | 545.68 | +41.9% |
| ASTRAZEN | 2024-10-14 | 7,800.00 | 2024-11-14 | 6,854.77 | -12.1% |
| BOROLTD | 2024-07-22 | 351.05 | 2024-11-18 | 411.49 | +17.2% |
| INDIGOPNTS | 2024-07-29 | 1,496.95 | 2024-11-18 | 1,460.72 | -2.4% |
| UNICHEMLAB | 2024-11-04 | 874.35 | 2024-12-20 | 711.49 | -18.6% |
| PRSMJOHNSN | 2024-09-16 | 214.51 | 2024-12-26 | 170.55 | -20.5% |
| GARFIBRES | 2024-10-14 | 805.75 | 2025-01-09 | 829.35 | +2.9% |
| UTIAMC | 2024-11-25 | 1,338.75 | 2025-01-09 | 1,191.16 | -11.0% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| CARERATING | 2024-10-28 | 1,396.00 | 2025-01-13 | 1,239.70 | -11.2% |
| MOTILALOFS | 2024-10-21 | 1,021.95 | 2025-01-17 | 788.79 | -22.8% |
| PTCIL | 2025-01-20 | 16,420.00 | 2025-01-21 | 15,417.55 | -6.1% |
| VARROC | 2025-01-13 | 590.00 | 2025-01-22 | 563.49 | -4.5% |
| STYLAMIND | 2024-07-15 | 2,019.00 | 2025-01-23 | 1,967.22 | -2.6% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| CONCORDBIO | 2024-10-21 | 2,018.05 | 2025-01-27 | 1,971.77 | -2.3% |
| PRIVISCL | 2024-11-25 | 1,829.50 | 2025-01-28 | 1,643.12 | -10.2% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| GANESHHOUC | 2024-11-18 | 1,059.00 | 2025-02-28 | 1,090.38 | +3.0% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| CASTROLIND | 2025-03-17 | 233.90 | 2025-03-20 | 215.90 | -7.7% |
| GRWRHITECH | 2025-03-10 | 4,219.95 | 2025-04-03 | 3,602.82 | -14.6% |
| SUVENPHAR | 2025-03-10 | 1,166.00 | 2025-04-07 | 1,038.10 | -11.0% |
| AARTIPHARM | 2025-03-10 | 744.90 | 2025-04-07 | 640.24 | -14.1% |
| AVANTIFEED | 2025-03-17 | 842.55 | 2025-04-07 | 648.95 | -23.0% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| TEJASNET | 2025-04-15 | 859.00 | 2025-05-09 | 679.16 | -20.9% |
| THYROCARE | 2025-05-12 | 965.00 | 2025-06-06 | 901.60 | -6.6% |
| SPARC | 2025-04-15 | 146.90 | 2025-06-19 | 150.81 | +2.7% |
| FINEORG | 2025-04-07 | 3,600.15 | 2025-06-23 | 4,498.25 | +24.9% |
| GODREJIND | 2025-04-15 | 1,144.00 | 2025-07-02 | 1,179.90 | +3.1% |
| SUBROS | 2025-06-30 | 944.90 | 2025-07-25 | 848.42 | -10.2% |
| OPTIEMUS | 2025-06-23 | 659.90 | 2025-07-28 | 564.30 | -14.5% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| KSL | 2025-07-07 | 959.55 | 2025-08-11 | 855.00 | -10.9% |
| DCMSHRIRAM | 2025-08-04 | 1,386.00 | 2025-08-18 | 1,266.35 | -8.6% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| RSYSTEMS | 2025-09-01 | 460.00 | 2025-09-24 | 423.23 | -8.0% |
| BOMDYEING | 2025-07-28 | 181.45 | 2025-09-25 | 172.67 | -4.8% |
| DMART | 2025-01-20 | 3,624.00 | 2025-10-03 | 4,404.96 | +21.5% |
| HEMIPROP | 2025-09-22 | 171.25 | 2025-10-06 | 159.33 | -7.0% |
| JTEKTINDIA | 2025-09-29 | 168.40 | 2025-10-09 | 154.34 | -8.3% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| BLACKBUCK | 2025-08-18 | 553.00 | 2025-10-28 | 642.20 | +16.1% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| VMART | 2025-10-27 | 858.00 | 2025-11-07 | 806.50 | -6.0% |
| INFIBEAM | 2025-10-27 | 18.94 | 2025-11-11 | 17.40 | -8.1% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| CCL | 2025-06-09 | 878.00 | 2025-11-24 | 976.41 | +11.2% |
| KIOCL | 2025-08-25 | 434.45 | 2025-11-24 | 376.46 | -13.3% |
| TDPOWERSYS | 2025-11-10 | 389.50 | 2025-11-24 | 357.49 | -8.2% |
| RAMKY | 2025-10-13 | 622.35 | 2025-12-01 | 578.17 | -7.1% |
| PGIL | 2025-11-17 | 844.05 | 2025-12-09 | 765.71 | -9.3% |
| SHAILY | 2025-10-13 | 2,434.00 | 2025-12-15 | 2,340.80 | -3.8% |
| HATSUN | 2025-11-24 | 1,046.40 | 2026-01-08 | 946.43 | -9.6% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| TATACOMM | 2025-11-03 | 1,875.40 | 2026-01-09 | 1,750.94 | -6.6% |
| ESABINDIA | 2025-12-08 | 5,750.00 | 2026-01-12 | 5,605.00 | -2.5% |
| KIRLOSENG | 2025-12-22 | 1,258.30 | 2026-01-12 | 1,140.95 | -9.3% |
| MINDACORP | 2025-10-06 | 590.90 | 2026-01-19 | 537.94 | -9.0% |
| PRICOLLTD | 2025-12-01 | 624.05 | 2026-01-19 | 587.20 | -5.9% |
| NATCOPHARM | 2025-12-15 | 905.65 | 2026-01-20 | 825.79 | -8.8% |
| JBMA | 2026-01-19 | 592.05 | 2026-01-20 | 556.03 | -6.1% |
| RAIN | 2026-01-19 | 139.49 | 2026-01-20 | 131.45 | -5.8% |
| GPPL | 2025-12-01 | 178.98 | 2026-01-21 | 169.62 | -5.2% |
| TATAELXSI | 2026-02-02 | 5,448.00 | 2026-02-12 | 5,016.48 | -7.9% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| CEIGALL | 2026-02-02 | 274.95 | 2026-03-04 | 266.33 | -3.1% |
| HAPPYFORGE | 2026-02-23 | 1,370.00 | 2026-03-04 | 1,234.05 | -9.9% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| HINDCOPPER | 2026-01-12 | 532.00 | 2026-03-12 | 528.63 | -0.6% |
| RBA | 2026-01-19 | 67.50 | 2026-03-12 | 61.08 | -9.5% |
| SANSERA | 2026-03-09 | 2,125.10 | 2026-03-13 | 2,033.00 | -4.3% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-16 | 121.14 | 2026-03-23 | 110.67 | -8.6% |
| MAHABANK | 2026-02-02 | 60.48 | 2026-03-30 | 61.05 | +0.9% |
| ABSLAMC | 2026-03-23 | 937.90 | 2026-03-30 | 876.18 | -6.6% |
| INOXINDIA | 2026-04-13 | 1,299.10 | 2026-05-13 | 1,372.18 | +5.6% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| E2E | 2026-02-23 | 2,914.00 | 2026-06-05 | 2,330.72 | -20.0% |
| THERMAX | 2026-04-13 | 3,596.00 | 2026-07-29 | 4,306.64 | +19.8% |
| VTL | 2026-03-09 | 532.95 | 2026-07-31 | 592.80 | +11.2% |
| SAREGAMA | 2026-06-08 | 465.55 | 2026-08-31 | 483.79 | +3.9% |
| ITDC | 2026-08-03 | 707.00 | 2026-08-31 | 653.65 | -7.5% |
| BHARATFORG | 2026-03-23 | 1,700.00 | 2026-09-04 | 1,953.29 | +14.9% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-02-23 | 6,090.00 | 2026-09-15 | 7,158.25 | +17.5% |
| KARURVYSYA | 2026-08-03 | 343.50 | 2026-09-15 | 327.23 | -4.7% |
| KENNAMET | 2026-09-07 | 4,717.00 | 2026-09-16 | 4,134.40 | -12.4% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_LADDERWATCH.csv` beside this report (19571 events in all).*

```
2020-04-13  DEEPAKNTR   BUY ₹10.00 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 2.47×, ladder rising; stop ₹240.25; charges ₹0.0118)
2020-04-27  CADILAHC    BUY ₹10.01 at ₹330.30 (fresh Friday signal — ACCUMULATE: surged 10.60× weekly on 2020-04-09 (month 3.50×), ladder rising NOW — promoted from the ladder watch; stop ₹310.03; charges ₹0.0119)
2020-04-27  NESTLEIND   BUY ₹9.99 at ₹879.25 (fresh Friday signal — ACCUMULATE: surged 2.03× weekly on 2020-04-09 (month 2.43×), ladder rising NOW — promoted from the ladder watch; stop ₹793.25; charges ₹0.0118)
2020-04-27  SYNGENE     BUY ₹10.02 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.94×, ladder rising; stop ₹285.95; charges ₹0.0119)
2020-04-27  TAJGVK      BUY ₹10.02 at ₹133.40 (fresh Friday signal — BUY: 6.65× weekly, month 2.23×, ladder rising; stop ₹106.49; charges ₹0.0119)
2020-05-04  BALAJITELE  BUY ₹9.93 at ₹61.40 (fresh Friday signal — BUY: surged 4.19× weekly on 2020-04-24 (month 2.47×), ladder rising NOW — promoted from the ladder watch; stop ₹48.55; charges ₹0.0118)
2020-05-04  GREENPLY    BUY ₹9.86 at ₹100.05 (fresh Friday signal — ACCUMULATE: surged 3.61× weekly on 2020-04-24 (month 1.51×), ladder rising NOW — promoted from the ladder watch; stop ₹89.49; charges ₹0.0117)
2020-05-08  GREENPLY    SELL ₹8.80 at stop ₹89.49 (-10.6%, charges ₹0.0091) — the cash goes back to work at the next Friday screen
2020-05-11  APLLTD      BUY ₹9.82 at ₹774.70 (fresh Friday signal — ACCUMULATE: surged 5.92× weekly on 2020-04-24 (month 3.96×), ladder rising NOW — promoted from the ladder watch; stop ₹694.45; charges ₹0.0116)
2020-05-11  DEEPAKFERT  BUY ₹9.81 at ₹101.00 (fresh Friday signal — ACCUMULATE: surged 4.08× weekly on 2020-04-30 (month 3.79×), ladder rising NOW — promoted from the ladder watch; stop ₹91.29; charges ₹0.0116)
2020-05-11  JKPAPER     BUY ₹9.82 at ₹96.95 (fresh Friday signal — ACCUMULATE: surged 4.21× weekly on 2020-04-30 (month 1.95×), ladder rising NOW — promoted from the ladder watch; stop ₹87.25; charges ₹0.0116)
2020-05-11  MOREPENLAB  BUY ₹9.52 at ₹17.05 (fresh Friday signal — ACCUMULATE: surged 3.57× weekly on 2020-04-24 (month 3.20×), ladder rising NOW — promoted from the ladder watch; stop ₹15.48; charges ₹0.0113)
2020-05-26  JKPAPER     SELL ₹8.82 at stop ₹87.25 (-10.0%, charges ₹0.0091) — the cash goes back to work at the next Friday screen
2020-06-01  PANACEABIO  BUY ₹8.82 at ₹153.00 (fresh Friday signal — ACCUMULATE: surged 27.86× weekly on 2020-04-30 (month 7.39×), ladder rising NOW — promoted from the ladder watch; stop ₹114.11; charges ₹0.0104)
2020-06-12  DEEPAKNTR   SELL ₹9.97 at stop ₹474.05 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-06-15  KIRLFER     BUY ₹9.97 at ₹61.55 (fresh Friday signal — BUY: 8.70× weekly, month 2.09×, ladder rising; stop ₹48.49; charges ₹0.0118)
2020-08-20  PANACEABIO  SELL ₹10.58 at stop ₹184.01 (+20.3%, charges ₹0.0110) — the cash goes back to work at the next Friday screen
2020-08-24  DPSCLTD     BUY ₹10.58 at ₹11.80 (fresh Friday signal — ACCUMULATE: surged 18.55× weekly on 2020-07-31 (month 4.81×), ladder rising NOW — promoted from the ladder watch; stop ₹9.82; charges ₹0.0125)
2020-09-01  APLLTD      SELL ₹11.74 at stop ₹928.62 (+19.9%, charges ₹0.0122) — the cash goes back to work at the next Friday screen
2020-09-01  NESTLEIND   SELL ₹8.99 at stop ₹793.25 (-9.8%, charges ₹0.0093) — the cash goes back to work at the next Friday screen
2020-09-07  BBL         BUY ₹8.23 at ₹400.00 (fresh Friday signal — ACCUMULATE: surged 12.29× weekly on 2020-08-14 (month 4.63×), ladder rising NOW — promoted from the ladder watch; stop ₹370.31; charges ₹0.0098)
2020-09-07  SIYSIL      BUY ₹12.50 at ₹150.70 (fresh Friday signal — ACCUMULATE: surged 16.86× weekly on 2020-08-07 (month 8.12×), ladder rising NOW — promoted from the ladder watch; stop ₹136.36; charges ₹0.0148)
2020-09-08  CADILAHC    SELL ₹11.04 at stop ₹364.99 (+10.5%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2020-09-09  BALAJITELE  SELL ₹11.95 at stop ₹74.07 (+20.6%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-14  FINEORG     BUY ₹12.54 at ₹2,900.00 (fresh Friday signal — ACCUMULATE: surged 9.10× weekly on 2020-08-28 (month 4.32×), ladder rising NOW — promoted from the ladder watch; stop ₹2,208.64; charges ₹0.0149)
2020-09-14  GUJALKALI   BUY ₹10.45 at ₹342.45 (fresh Friday signal — ACCUMULATE: surged 6.65× weekly on 2020-08-28 (month 5.24×), ladder rising NOW — promoted from the ladder watch; stop ₹317.35; charges ₹0.0124)
2020-09-21  BBL         SELL ₹7.61 at stop ₹370.31 (-7.4%, charges ₹0.0079) — the cash goes back to work at the next Friday screen
2020-09-21  SIYSIL      SELL ₹11.29 at stop ₹136.36 (-9.5%, charges ₹0.0117) — the cash goes back to work at the next Friday screen
2020-09-22  DEEPAKFERT  SELL ₹14.94 at stop ₹154.26 (+52.7%, charges ₹0.0155) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹9.48 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-24  MOREPENLAB  SELL ₹12.57 at stop ₹22.56 (+32.3%, charges ₹0.0130) — the cash goes back to work at the next Friday screen
2020-09-28  ALLCARGO    BUY ₹12.28 at ₹131.30 (fresh Friday signal — ACCUMULATE: surged 10.41× weekly on 2020-08-28 (month 3.25×), ladder rising NOW — promoted from the ladder watch; stop ₹102.98; charges ₹0.0145)
2020-09-28  CENTRUM     BUY ₹12.23 at ₹15.95 (fresh Friday signal — ACCUMULATE: surged 5.71× weekly on 2020-08-28 (month 3.97×), ladder rising NOW — promoted from the ladder watch; stop ₹13.49; charges ₹0.0145)
2020-09-28  PUNJABCHEM  BUY ₹6.89 at ₹630.20 (fresh Friday signal — ACCUMULATE: surged 5.01× weekly on 2020-08-28 (month 9.82×), ladder rising NOW — promoted from the ladder watch; stop ₹472.24; charges ₹0.0082)
2020-09-28  SAKSOFT     BUY ₹12.26 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.0145)
2020-09-28  VINATIORGA  BUY ₹12.22 at ₹1,294.60 (fresh Friday signal — ACCUMULATE: surged 5.20× weekly on 2020-09-18 (month 5.20×), ladder rising NOW — promoted from the ladder watch; stop ₹1,088.50; charges ₹0.0145)
2020-10-13  GUJALKALI   SELL ₹9.67 at stop ₹317.35 (-7.3%, charges ₹0.0100) — the cash goes back to work at the next Friday screen
2020-10-19  SASKEN      BUY ₹9.67 at ₹735.00 (fresh Friday signal — BUY: surged 7.12× weekly on 2020-09-25 (month 4.35×), ladder rising NOW — promoted from the ladder watch; stop ₹651.70; charges ₹0.0115)
2020-10-26  SASKEN      SELL ₹8.55 at stop ₹651.70 (-11.3%, charges ₹0.0089) — the cash goes back to work at the next Friday screen
2020-11-02  KESORAMIND  BUY ₹8.55 at ₹40.35 (fresh Friday signal — ACCUMULATE: surged 5.63× weekly on 2020-10-09 (month 1.81×), ladder rising NOW — promoted from the ladder watch; stop ₹36.61; charges ₹0.0101)
2020-11-06  VINATIORGA  SELL ₹10.50 at stop ₹1,114.87 (-13.9%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2020-11-09  OAL         BUY ₹10.50 at ₹485.00 (fresh Friday signal — ACCUMULATE: surged 8.03× weekly on 2020-10-23 (month 4.04×), ladder rising NOW — promoted from the ladder watch; stop ₹407.43; charges ₹0.0124)
2020-12-21  OAL         SELL ₹11.03 at stop ₹510.34 (+5.2%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2020-12-22  DPSCLTD     SELL ₹8.79 at stop ₹9.82 (-16.8%, charges ₹0.0091) — the cash goes back to work at the next Friday screen
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-23  FINEORG     SELL ₹10.10 at stop ₹2,342.46 (-19.2%, charges ₹0.0105) — the cash goes back to work at the next Friday screen
2020-12-28  J&KBANK     BUY ₹13.04 at ₹23.85 (fresh Friday signal — ACCUMULATE: surged 12.58× weekly on 2020-11-27 (month 3.32×), ladder rising NOW — promoted from the ladder watch; stop ₹19.59; charges ₹0.0154)
2020-12-28  PAISALO     BUY ₹12.88 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0153)
2020-12-28  PCJEWELLER  BUY ₹8.63 at ₹2.52 (fresh Friday signal — ACCUMULATE: surged 10.32× weekly on 2020-12-11 (month 1.59×), ladder rising NOW — promoted from the ladder watch; stop ₹2.03; charges ₹0.0102)
2020-12-28  RUBYMILLS   BUY ₹13.00 at ₹192.25 (fresh Friday signal — BUY: surged 14.77× weekly on 2020-11-27 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹171.43; charges ₹0.0154)
2021-01-25  SAKSOFT     SELL ₹10.47 at stop ₹341.10 (-14.4%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2021-01-28  J&KBANK     SELL ₹14.38 at stop ₹26.36 (+10.5%, charges ₹0.0149) — the cash goes back to work at the next Friday screen
2021-02-01  CESC        BUY ₹14.00 at ₹61.51 (fresh Friday signal — BUY: surged 9.11× weekly on 2021-01-15 (month 2.06×), ladder rising NOW — promoted from the ladder watch; stop ₹63.66; charges ₹0.0166)
2021-02-01  ZOTA        BUY ₹10.84 at ₹155.60 (fresh Friday signal — ACCUMULATE: surged 7.41× weekly on 2021-01-01 (month 3.19×), ladder rising NOW — promoted from the ladder watch; stop ₹141.20; charges ₹0.0128)
2021-02-02  CESC        SELL ₹14.46 at stop ₹63.66 (+3.5%, charges ₹0.0150) — the cash goes back to work at the next Friday screen
2021-02-08  INOXLEISUR  BUY ₹14.34 at ₹333.15 (fresh Friday signal — ACCUMULATE: surged 5.38× weekly on 2021-01-08 (month 2.12×), ladder rising NOW — promoted from the ladder watch; stop ₹296.40; charges ₹0.0170)
2021-02-23  INOXLEISUR  SELL ₹12.73 at stop ₹296.40 (-11.0%, charges ₹0.0132) — the cash goes back to work at the next Friday screen
2021-03-01  CENTRALBK   BUY ₹12.84 at ₹20.00 (fresh Friday signal — ACCUMULATE: surged 17.35× weekly on 2021-02-19 (month 12.20×), ladder rising NOW — promoted from the ladder watch; stop ₹15.16; charges ₹0.0152)
2021-03-18  PUNJABCHEM  SELL ₹9.48 at stop ₹868.82 (+37.9%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2021-03-18  RUBYMILLS   SELL ₹11.57 at stop ₹171.43 (-10.8%, charges ₹0.0120) — the cash goes back to work at the next Friday screen
2021-03-19  PCJEWELLER  SELL ₹9.09 at stop ₹2.66 (+5.6%, charges ₹0.0094) — the cash goes back to work at the next Friday screen
2021-03-22  IOB         BUY ₹14.38 at ₹15.85 (fresh Friday signal — ACCUMULATE: surged 16.79× weekly on 2021-02-19 (month 7.35×), ladder rising NOW — promoted from the ladder watch; stop ₹13.70; charges ₹0.0170)
2021-03-22  TCNSBRANDS  BUY ₹14.35 at ₹510.15 (fresh Friday signal — BUY: surged 26.51× weekly on 2021-02-19 (month 9.22×), ladder rising NOW — promoted from the ladder watch; stop ₹414.06; charges ₹0.0170)
2021-03-30  ZOTA        SELL ₹9.88 at stop ₹142.03 (-8.7%, charges ₹0.0102) — the cash goes back to work at the next Friday screen
2021-04-01  TAX         FY2021 settled: ₹1.8870 paid (STCG ₹9.43 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-05  IFGLEXPOR   BUY ₹9.39 at ₹326.10 (fresh Friday signal — ACCUMULATE: surged 10.84× weekly on 2021-03-19 (month 11.93×), ladder rising NOW — promoted from the ladder watch; stop ₹281.72; charges ₹0.0111)
2021-04-12  CENTRUM     SELL ₹19.05 at stop ₹24.89 (+56.1%, charges ₹0.0198) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹16.33 at stop ₹72.41 (+27.1%, charges ₹0.0169) — the cash goes back to work at the next Friday screen
2021-04-12  TCNSBRANDS  SELL ₹13.24 at stop ₹471.72 (-7.5%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2021-04-19  BODALCHEM   BUY ₹13.98 at ₹87.00 (fresh Friday signal — ACCUMULATE: surged 4.65× weekly on 2021-03-19 (month 3.27×), ladder rising NOW — promoted from the ladder watch; stop ₹79.02; charges ₹0.0166)
2021-04-19  EMAMIPAP    BUY ₹13.91 at ₹125.00 (fresh Friday signal — ACCUMULATE: surged 37.60× weekly on 2021-03-19 (month 15.67×), ladder rising NOW — promoted from the ladder watch; stop ₹81.22; charges ₹0.0165)
2021-04-19  MEGH        BUY ₹13.99 at ₹116.15 (fresh Friday signal — ACCUMULATE: surged 7.86× weekly on 2021-03-19 (month 3.51×), ladder rising NOW — promoted from the ladder watch; stop ₹107.93; charges ₹0.0166)
2021-04-28  IOB         SELL ₹13.42 at stop ₹14.82 (-6.5%, charges ₹0.0139) — the cash goes back to work at the next Friday screen
2021-05-03  MARKSANS    BUY ₹15.09 at ₹70.95 (fresh Friday signal — ACCUMULATE: surged 10.80× weekly on 2021-04-23 (month 2.96×), ladder rising NOW — promoted from the ladder watch; stop ₹64.12; charges ₹0.0179)
2021-08-10  BODALCHEM   SELL ₹17.30 at stop ₹107.92 (+24.0%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2021-08-10  CENTRALBK   SELL ₹13.51 at stop ₹21.09 (+5.4%, charges ₹0.0140) — the cash goes back to work at the next Friday screen
2021-08-10  KESORAMIND  SELL ₹18.14 at stop ₹85.78 (+112.6%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2021-08-10  KIRLFER     SELL ₹45.16 at stop ₹279.49 (+354.1%, charges ₹0.0468) — the cash goes back to work at the next Friday screen
2021-08-10  MARKSANS    SELL ₹16.37 at stop ₹77.14 (+8.7%, charges ₹0.0170) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹18.54 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.0220)
2021-08-16  BBL         BUY ₹18.44 at ₹704.80 (fresh Friday signal — ACCUMULATE: surged 4.57× weekly on 2021-07-16 (month 1.71×), ladder rising NOW — promoted from the ladder watch; stop ₹634.17; charges ₹0.0218)
2021-08-16  INDOCO      BUY ₹18.45 at ₹484.30 (fresh Friday signal — BUY: 4.80× weekly, month 2.73×, ladder rising; stop ₹412.30; charges ₹0.0219)
2021-08-16  SHANKARA    BUY ₹18.48 at ₹593.00 (fresh Friday signal — BUY: surged 6.32× weekly on 2021-07-16 (month 2.82×), ladder rising NOW — promoted from the ladder watch; stop ₹489.25; charges ₹0.0219)
2021-08-16  SHANTIGEAR  BUY ₹18.58 at ₹182.10 (fresh Friday signal — ACCUMULATE: surged 18.60× weekly on 2021-07-30 (month 3.71×), ladder rising NOW — promoted from the ladder watch; stop ₹149.80; charges ₹0.0220)
2021-08-16  TATAINVEST  BUY ₹18.52 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0219)
2021-08-23  BBL         SELL ₹16.56 at stop ₹634.17 (-10.0%, charges ₹0.0172) — the cash goes back to work at the next Friday screen
2021-08-23  IFGLEXPOR   SELL ₹9.03 at stop ₹314.39 (-3.6%, charges ₹0.0094) — the cash goes back to work at the next Friday screen
2021-08-30  HATSUN      BUY ₹17.69 at ₹1,055.00 (fresh Friday signal — BUY: 8.05× weekly, month 2.62×, ladder rising; stop ₹874.48; charges ₹0.0210)
2021-08-30  MAHLOG      BUY ₹12.45 at ₹805.00 (fresh Friday signal — ACCUMULATE: surged 7.46× weekly on 2021-07-30 (month 3.08×), ladder rising NOW — promoted from the ladder watch; stop ₹588.04; charges ₹0.0147)
2021-09-21  SHANTIGEAR  SELL ₹16.78 at stop ₹164.87 (-9.5%, charges ₹0.0174) — the cash goes back to work at the next Friday screen
2021-09-27  ESABINDIA   BUY ₹16.78 at ₹2,187.65 (fresh Friday signal — ACCUMULATE: surged 12.28× weekly on 2021-08-27 (month 2.38×), ladder rising NOW — promoted from the ladder watch; stop ₹1,979.18; charges ₹0.0199)
2021-10-25  BASF        SELL ₹16.19 at stop ₹3,220.59 (-12.5%, charges ₹0.0168) — the cash goes back to work at the next Friday screen
2021-11-01  KKCL        BUY ₹16.19 at ₹1,227.00 (fresh Friday signal — ACCUMULATE: surged 18.21× weekly on 2021-10-08 (month 12.18×), ladder rising NOW — promoted from the ladder watch; stop ₹915.66; charges ₹0.0192)
2021-11-12  INDOCO      SELL ₹15.67 at stop ₹412.30 (-14.9%, charges ₹0.0163) — the cash goes back to work at the next Friday screen
2021-11-15  KKCL        SELL ₹14.88 at stop ₹1,130.50 (-7.9%, charges ₹0.0154) — the cash goes back to work at the next Friday screen
2021-11-15  RVNL        BUY ₹15.67 at ₹38.00 (fresh Friday signal — ACCUMULATE: surged 17.72× weekly on 2021-10-22 (month 2.26×), ladder rising NOW — promoted from the ladder watch; stop ₹30.11; charges ₹0.0186)
2021-11-22  EMAMIPAP    SELL ₹15.71 at stop ₹141.55 (+13.2%, charges ₹0.0163) — the cash goes back to work at the next Friday screen
2021-11-22  HATSUN      SELL ₹21.00 at stop ₹1,255.19 (+19.0%, charges ₹0.0218) — the cash goes back to work at the next Friday screen
2021-11-22  TVTODAY     BUY ₹14.88 at ₹320.24 (fresh Friday signal — BUY: 15.58× weekly, month 3.55×, ladder rising; stop ₹253.08; charges ₹0.0176)
2021-11-26  TATAINVEST  SELL ₹20.30 at stop ₹1,436.49 (+9.8%, charges ₹0.0211) — the cash goes back to work at the next Friday screen
2021-11-29  ALLCARGO    SELL ₹28.95 at stop ₹310.33 (+136.4%, charges ₹0.0300) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹18.01 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.0213)
2021-11-29  RAYMOND     BUY ₹17.83 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0211)
2021-11-29  RSYSTEMS    BUY ₹17.93 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0212)
2021-11-29  SHANKARA    SELL ₹15.22 at stop ₹489.25 (-17.5%, charges ₹0.0158) — the cash goes back to work at the next Friday screen
2021-11-30  MAHLOG      SELL ₹10.10 at stop ₹654.55 (-18.7%, charges ₹0.0105) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹17.87 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0212)
2021-12-06  CHAMBLFERT  BUY ₹17.83 at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹0.0211)
2021-12-06  RAJESHEXPO  BUY ₹17.77 at ₹751.80 (fresh Friday signal — BUY: 2.81× weekly, month 2.30×, ladder rising; stop ₹662.77; charges ₹0.0211)
2021-12-16  RSYSTEMS    SELL ₹16.03 at stop ₹291.18 (-10.4%, charges ₹0.0166) — the cash goes back to work at the next Friday screen
2021-12-20  ESABINDIA   SELL ₹20.65 at stop ₹2,698.00 (+23.3%, charges ₹0.0214) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹17.62 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0209)
2021-12-27  RIIL        BUY ₹17.65 at ₹845.00 (fresh Friday signal — ACCUMULATE: surged 9.24× weekly on 2021-12-10 (month 3.25×), ladder rising NOW — promoted from the ladder watch; stop ₹552.18; charges ₹0.0209)
2022-01-24  TVTODAY     SELL ₹14.45 at stop ₹311.68 (-2.7%, charges ₹0.0150) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹18.60 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0220)
2022-02-11  SHARDACROP  SELL ₹17.25 at stop ₹545.30 (-7.1%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹16.41 at stop ₹424.65 (-8.7%, charges ₹0.0170) — the cash goes back to work at the next Friday screen
2022-02-14  ONMOBILE    BUY ₹17.54 at ₹126.10 (fresh Friday signal — BUY: surged 15.93× weekly on 2022-01-21 (month 2.33×), ladder rising NOW — promoted from the ladder watch; stop ₹129.75; charges ₹0.0208)
2022-02-15  ONMOBILE    SELL ₹18.01 at stop ₹129.75 (+2.9%, charges ₹0.0187) — the cash goes back to work at the next Friday screen
2022-02-15  RAYMOND     SELL ₹20.28 at stop ₹679.35 (+14.0%, charges ₹0.0210) — the cash goes back to work at the next Friday screen
2022-02-18  RVNL        SELL ₹13.49 at stop ₹32.77 (-13.8%, charges ₹0.0140) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹17.22 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0204)
2022-02-21  GAEL        BUY ₹17.28 at ₹93.58 (fresh Friday signal — ACCUMULATE: surged 6.33× weekly on 2022-01-28 (month 1.94×), ladder rising NOW — promoted from the ladder watch; stop ₹80.97; charges ₹0.0205)
2022-02-21  MAHLIFE     BUY ₹17.25 at ₹305.00 (fresh Friday signal — ACCUMULATE: surged 6.66× weekly on 2022-02-11 (month 2.51×), ladder rising NOW — promoted from the ladder watch; stop ₹286.85; charges ₹0.0204)
2022-02-21  PSPPROJECT  BUY ₹17.19 at ₹538.00 (fresh Friday signal — ACCUMULATE: surged 3.55× weekly on 2022-02-04 (month 2.31×), ladder rising NOW — promoted from the ladder watch; stop ₹482.13; charges ₹0.0204)
2022-02-22  GREENLAM    SELL ₹15.17 at stop ₹313.67 (-13.7%, charges ₹0.0157) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹15.45 at stop ₹353.85 (-13.2%, charges ₹0.0160) — the cash goes back to work at the next Friday screen
2022-02-24  MAHLIFE     SELL ₹16.19 at stop ₹286.85 (-6.0%, charges ₹0.0168) — the cash goes back to work at the next Friday screen
2022-02-24  PSPPROJECT  SELL ₹15.37 at stop ₹482.13 (-10.4%, charges ₹0.0159) — the cash goes back to work at the next Friday screen
2022-02-24  RAJESHEXPO  SELL ₹17.65 at stop ₹748.32 (-0.5%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹16.58 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0196)
2022-02-28  RAJMET      BUY ₹16.47 at ₹265.00 (fresh Friday signal — ACCUMULATE: surged 6.93× weekly on 2022-02-18 (month 4.62×), ladder rising NOW — promoted from the ladder watch; stop ₹226.96; charges ₹0.0195)
2022-02-28  SHANTIGEAR  BUY ₹16.57 at ₹185.30 (fresh Friday signal — BUY: surged 3.40× weekly on 2022-02-11 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹170.29; charges ₹0.0196)
2022-03-07  AVTNPL      BUY ₹16.37 at ₹89.95 (fresh Friday signal — ACCUMULATE: surged 9.20× weekly on 2022-02-11 (month 2.02×), ladder rising NOW — promoted from the ladder watch; stop ₹72.36; charges ₹0.0194)
2022-03-07  GTLINFRA    BUY ₹14.08 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0167)
2022-03-21  BSE         SELL ₹15.42 at stop ₹1,634.39 (-13.5%, charges ₹0.0160) — the cash goes back to work at the next Friday screen
2022-03-28  EVEREADY    BUY ₹15.42 at ₹344.00 (fresh Friday signal — ACCUMULATE: surged 3.19× weekly on 2022-03-04 (month 2.42×), ladder rising NOW — promoted from the ladder watch; stop ₹310.46; charges ₹0.0183)
2022-04-01  AVTNPL      TRIM 3.9% (₹0.93 at ₹131.40) to pay the tax bill
2022-04-01  CGCL        TRIM 3.9% (₹0.69 at ₹614.95) to pay the tax bill
2022-04-01  DANGEE      TRIM 3.9% (₹0.85 at ₹310.25) to pay the tax bill
2022-04-01  EVEREADY    TRIM 3.9% (₹0.59 at ₹338.95) to pay the tax bill
2022-04-01  GAEL        TRIM 3.9% (₹0.95 at ₹132.03) to pay the tax bill
2022-04-01  GTLINFRA    TRIM 3.9% (₹0.50 at ₹1.55) to pay the tax bill
2022-04-01  MEGH        TRIM 3.9% (₹0.65 at ₹138.25) to pay the tax bill
2022-04-01  RAJMET      TRIM 3.9% (₹0.85 at ₹349.70) to pay the tax bill
2022-04-01  RIIL        TRIM 3.9% (₹0.65 at ₹804.40) to pay the tax bill
2022-04-01  SHANTIGEAR  TRIM 3.9% (₹0.64 at ₹183.85) to pay the tax bill
2022-04-01  TAX         FY2022 settled: ₹7.3076 paid (STCG ₹4.06 @20%, LTCG ₹51.97 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-29  GTLINFRA    SELL ₹11.20 at stop ₹1.41 (-17.1%, charges ₹0.0116) — the cash goes back to work at the next Friday screen
2022-05-02  GODFRYPHLP  BUY ₹11.20 at ₹1,219.00 (fresh Friday signal — ACCUMULATE: surged 36.00× weekly on 2022-04-13 (month 1.67×), ladder rising NOW — promoted from the ladder watch; stop ₹1,130.50; charges ₹0.0133)
2022-05-05  AVTNPL      SELL ₹18.49 at stop ₹105.99 (+17.8%, charges ₹0.0192) — the cash goes back to work at the next Friday screen
2022-05-09  GAEL        SELL ₹25.73 at stop ₹145.28 (+55.3%, charges ₹0.0267) — the cash goes back to work at the next Friday screen
2022-05-09  GODFRYPHLP  SELL ₹10.36 at stop ₹1,130.50 (-7.3%, charges ₹0.0107) — the cash goes back to work at the next Friday screen
2022-05-09  MOL         BUY ₹18.49 at ₹129.80 (fresh Friday signal — BUY: 6.75× weekly, month 2.56×, ladder rising; stop ₹113.62; charges ₹0.0219)
2022-05-11  EVEREADY    SELL ₹13.35 at stop ₹310.46 (-9.8%, charges ₹0.0138) — the cash goes back to work at the next Friday screen
2022-05-11  MOL         SELL ₹16.15 at stop ₹113.62 (-12.5%, charges ₹0.0168) — the cash goes back to work at the next Friday screen
2022-05-16  GEPIL       BUY ₹18.63 at ₹176.10 (fresh Friday signal — ACCUMULATE: surged 5.38× weekly on 2022-04-22 (month 2.38×), ladder rising NOW — promoted from the ladder watch; stop ₹163.45; charges ₹0.0221)
2022-05-16  HUHTAMAKI   BUY ₹9.71 at ₹178.20 (fresh Friday signal — BUY: surged 3.11× weekly on 2022-04-13 (month 2.75×), ladder rising NOW — promoted from the ladder watch; stop ₹161.50; charges ₹0.0115)
2022-05-16  JKIL        BUY ₹18.58 at ₹222.90 (fresh Friday signal — BUY: surged 4.42× weekly on 2022-04-22 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹192.28; charges ₹0.0220)
2022-05-16  TIMETECHNO  BUY ₹18.66 at ₹91.25 (fresh Friday signal — BUY: surged 5.09× weekly on 2022-04-22 (month 3.01×), ladder rising NOW — promoted from the ladder watch; stop ₹86.50; charges ₹0.0221)
2022-05-26  HUHTAMAKI   SELL ₹8.78 at stop ₹161.50 (-9.4%, charges ₹0.0091) — the cash goes back to work at the next Friday screen
2022-05-26  RIIL        SELL ₹17.30 at stop ₹863.73 (+2.2%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2022-05-30  GODREJAGRO  BUY ₹18.84 at ₹526.00 (fresh Friday signal — ACCUMULATE: surged 13.85× weekly on 2022-04-29 (month 4.66×), ladder rising NOW — promoted from the ladder watch; stop ₹456.63; charges ₹0.0223)
2022-05-31  GEPIL       SELL ₹17.26 at stop ₹163.45 (-7.2%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2022-06-06  RAJRATAN    BUY ₹19.02 at ₹714.95 (fresh Friday signal — ACCUMULATE: surged 2.40× weekly on 2022-05-27 (month 2.70×), ladder rising NOW — promoted from the ladder watch; stop ₹653.60; charges ₹0.0225)
2022-06-14  RAJRATAN    SELL ₹17.35 at stop ₹653.60 (-8.6%, charges ₹0.0180) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹18.08 at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹0.0214)
2022-08-05  JKIL        SELL ₹25.68 at stop ₹308.80 (+38.5%, charges ₹0.0266) — the cash goes back to work at the next Friday screen
2022-08-08  NAVNETEDUL  BUY ₹20.45 at ₹130.50 (fresh Friday signal — BUY: 14.73× weekly, month 3.84×, ladder rising; stop ₹88.40; charges ₹0.0242)
2022-09-06  DANGEE      SELL ₹25.38 at stop ₹375.25 (+59.7%, charges ₹0.0263) — the cash goes back to work at the next Friday screen
2022-09-12  SAFARI      BUY ₹21.39 at ₹765.00 (fresh Friday signal — ACCUMULATE: surged 7.66× weekly on 2022-08-12 (month 2.19×), ladder rising NOW — promoted from the ladder watch; stop ₹679.25; charges ₹0.0253)
2022-09-12  SHREECEM    BUY ₹13.98 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0166)
2022-09-15  RAJMET      SELL ₹21.41 at stop ₹359.30 (+35.6%, charges ₹0.0222) — the cash goes back to work at the next Friday screen
2022-09-19  JSWHL       BUY ₹20.68 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0245)
2022-09-26  NAVNETEDUL  SELL ₹19.90 at stop ₹127.30 (-2.5%, charges ₹0.0206) — the cash goes back to work at the next Friday screen
2022-10-03  MIDHANI     BUY ₹20.43 at ₹204.40 (fresh Friday signal — ACCUMULATE: surged 11.84× weekly on 2022-09-16 (month 2.33×), ladder rising NOW — promoted from the ladder watch; stop ₹184.94; charges ₹0.0242)
2022-11-03  APARINDS    SELL ₹25.80 at stop ₹1,358.50 (+43.0%, charges ₹0.0268) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹22.06 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0261)
2022-11-21  MIDHANI     SELL ₹22.36 at stop ₹224.20 (+9.7%, charges ₹0.0232) — the cash goes back to work at the next Friday screen
2022-11-21  TIMETECHNO  SELL ₹19.40 at stop ₹95.09 (+4.2%, charges ₹0.0201) — the cash goes back to work at the next Friday screen
2022-11-23  GODREJAGRO  SELL ₹16.32 at stop ₹456.63 (-13.2%, charges ₹0.0169) — the cash goes back to work at the next Friday screen
2022-11-28  IRCON       BUY ₹20.84 at ₹61.40 (fresh Friday signal — ACCUMULATE: surged 9.66× weekly on 2022-11-18 (month 9.92×), ladder rising NOW — promoted from the ladder watch; stop ₹52.53; charges ₹0.0247)
2022-11-28  IRFC        BUY ₹20.85 at ₹32.00 (fresh Friday signal — BUY: 6.87× weekly, month 11.74×, ladder rising; stop ₹23.09; charges ₹0.0247)
2022-11-28  MAHABANK    BUY ₹20.33 at ₹27.60 (fresh Friday signal — BUY: 6.28× weekly, month 7.28×, ladder rising; stop ₹21.47; charges ₹0.0241)
2022-12-22  IRCON       SELL ₹19.24 at stop ₹56.81 (-7.5%, charges ₹0.0200) — the cash goes back to work at the next Friday screen
2022-12-22  SAFARI      SELL ₹22.22 at stop ₹796.58 (+4.1%, charges ₹0.0230) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹29.62 at stop ₹345.56 (+86.5%, charges ₹0.0307) — the cash goes back to work at the next Friday screen
2022-12-23  IRFC        SELL ₹18.33 at stop ₹28.20 (-11.9%, charges ₹0.0190) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹21.98 at stop ₹139.84 (-0.1%, charges ₹0.0228) — the cash goes back to work at the next Friday screen
2022-12-26  GICRE       BUY ₹20.19 at ₹157.00 (fresh Friday signal — BUY: surged 4.73× weekly on 2022-12-02 (month 1.82×), ladder rising NOW — promoted from the ladder watch; stop ₹134.14; charges ₹0.0239)
2022-12-26  KABRAEXTRU  BUY ₹20.30 at ₹441.95 (fresh Friday signal — BUY: surged 4.67× weekly on 2022-11-25 (month 1.52×), ladder rising NOW — promoted from the ladder watch; stop ₹457.95; charges ₹0.0241)
2022-12-26  KRISHANA    BUY ₹20.49 at ₹83.60 (fresh Friday signal — BUY: 3.70× weekly, month 2.29×, ladder rising; stop ₹75.36; charges ₹0.0243)
2022-12-26  KSL         BUY ₹20.14 at ₹330.10 (fresh Friday signal — BUY: surged 5.50× weekly on 2022-12-09 (month 2.50×), ladder rising NOW — promoted from the ladder watch; stop ₹328.23; charges ₹0.0239)
2022-12-26  WABAG       BUY ₹20.41 at ₹304.45 (fresh Friday signal — BUY: surged 3.91× weekly on 2022-12-02 (month 2.10×), ladder rising NOW — promoted from the ladder watch; stop ₹308.85; charges ₹0.0242)
2023-01-27  KSL         SELL ₹19.98 at stop ₹328.23 (-0.6%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2023-01-27  WABAG       SELL ₹20.66 at stop ₹308.85 (+1.4%, charges ₹0.0214) — the cash goes back to work at the next Friday screen
2023-01-30  JBMA        BUY ₹20.99 at ₹263.32 (fresh Friday signal — BUY: surged 2.74× weekly on 2023-01-06 (month 5.32×), ladder rising NOW — promoted from the ladder watch; stop ₹246.34; charges ₹0.0249)
2023-01-30  USHAMART    BUY ₹20.97 at ₹179.95 (fresh Friday signal — BUY: surged 2.55× weekly on 2023-01-06 (month 2.92×), ladder rising NOW — promoted from the ladder watch; stop ₹166.25; charges ₹0.0248)
2023-02-01  GICRE       SELL ₹21.52 at stop ₹167.72 (+6.8%, charges ₹0.0223) — the cash goes back to work at the next Friday screen
2023-02-06  TRIL        BUY ₹21.03 at ₹70.90 (fresh Friday signal — ACCUMULATE: surged 3.71× weekly on 2023-01-20 (month 2.79×), ladder rising NOW — promoted from the ladder watch; stop ₹62.10; charges ₹0.0249)
2023-02-07  JBMA        SELL ₹19.59 at stop ₹246.34 (-6.5%, charges ₹0.0203) — the cash goes back to work at the next Friday screen
2023-02-13  VSSL        BUY ₹20.91 at ₹345.70 (fresh Friday signal — ACCUMULATE: surged 2.11× weekly on 2023-01-20 (month 2.73×), ladder rising NOW — promoted from the ladder watch; stop ₹286.40; charges ₹0.0248)
2023-02-14  TRIL        SELL ₹18.38 at stop ₹62.10 (-12.4%, charges ₹0.0191) — the cash goes back to work at the next Friday screen
2023-02-17  CGCL        SELL ₹19.42 at stop ₹704.95 (+17.6%, charges ₹0.0201) — the cash goes back to work at the next Friday screen
2023-02-20  CIGNITITEC  BUY ₹20.54 at ₹731.95 (fresh Friday signal — BUY: 2.05× weekly, month 1.77×, ladder rising; stop ₹568.10; charges ₹0.0243)
2023-02-20  TIIL        BUY ₹20.66 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0245)
2023-02-22  USHAMART    SELL ₹19.33 at stop ₹166.25 (-7.6%, charges ₹0.0200) — the cash goes back to work at the next Friday screen
2023-02-27  ROUTE       BUY ₹19.94 at ₹1,338.25 (fresh Friday signal — BUY: surged 18.55× weekly on 2023-01-27 (month 1.57×), ladder rising NOW — promoted from the ladder watch; stop ₹1,099.48; charges ₹0.0236)
2023-03-14  KABRAEXTRU  SELL ₹23.23 at stop ₹506.92 (+14.7%, charges ₹0.0241) — the cash goes back to work at the next Friday screen
2023-03-20  DCAL        BUY ₹20.03 at ₹134.50 (fresh Friday signal — ACCUMULATE: surged 6.76× weekly on 2023-02-24 (month 4.70×), ladder rising NOW — promoted from the ladder watch; stop ₹114.43; charges ₹0.0237)
2023-03-20  KRISHANA    SELL ₹23.09 at stop ₹94.40 (+12.9%, charges ₹0.0240) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹10.32 at ₹417.98 (fresh Friday signal — ACCUMULATE: surged 4.48× weekly on 2023-03-10 (month 1.97×), ladder rising NOW — promoted from the ladder watch; stop ₹372.21; charges ₹0.0122)
2023-03-27  OLECTRA     BUY ₹19.68 at ₹634.90 (fresh Friday signal — ACCUMULATE: surged 5.11× weekly on 2023-03-10 (month 12.52×), ladder rising NOW — promoted from the ladder watch; stop ₹534.05; charges ₹0.0233)
2023-03-29  CIGNITITEC  SELL ₹19.74 at stop ₹705.14 (-3.7%, charges ₹0.0205) — the cash goes back to work at the next Friday screen
2023-04-03  INGERRAND   BUY ₹10.38 at ₹2,690.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2023-03-10 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹2,170.84; charges ₹0.0123)
2023-04-03  TAX         FY2023 settled: ₹9.3581 paid (STCG ₹46.79 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-11  ROUTE       SELL ₹18.30 at stop ₹1,231.11 (-8.0%, charges ₹0.0190) — the cash goes back to work at the next Friday screen
2023-04-17  GLS         BUY ₹18.30 at ₹418.00 (fresh Friday signal — ACCUMULATE: surged 3.47× weekly on 2023-03-17 (month 1.63×), ladder rising NOW — promoted from the ladder watch; stop ₹351.50; charges ₹0.0217)
2023-04-24  SHREECEM    SELL ₹13.40 at stop ₹23,636.00 (-3.9%, charges ₹0.0139) — the cash goes back to work at the next Friday screen
2023-05-02  ACCELYA     BUY ₹13.40 at ₹1,404.95 (fresh Friday signal — ACCUMULATE: surged 5.15× weekly on 2023-04-21 (month 2.33×), ladder rising NOW — promoted from the ladder watch; stop ₹1,294.61; charges ₹0.0159)
2023-05-05  ACCELYA     SELL ₹12.32 at stop ₹1,294.61 (-7.9%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2023-05-08  SIS         BUY ₹12.32 at ₹384.35 (fresh Friday signal — ACCUMULATE: surged 8.42× weekly on 2023-04-13 (month 2.36×), ladder rising NOW — promoted from the ladder watch; stop ₹356.54; charges ₹0.0146)
2023-05-24  DCAL        SELL ₹17.15 at stop ₹115.42 (-14.2%, charges ₹0.0178) — the cash goes back to work at the next Friday screen
2023-05-26  VSSL        SELL ₹19.58 at stop ₹324.52 (-6.1%, charges ₹0.0203) — the cash goes back to work at the next Friday screen
2023-05-29  SWARAJENG   BUY ₹16.27 at ₹1,809.90 (fresh Friday signal — ACCUMULATE: surged 14.22× weekly on 2023-04-28 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹1,683.40; charges ₹0.0193)
2023-05-29  THANGAMAYL  BUY ₹20.46 at ₹1,344.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.50×, ladder rising; stop ₹1,116.30; charges ₹0.0242)
2023-06-15  MAHABANK    SELL ₹20.42 at stop ₹27.79 (+0.7%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2023-06-19  VSTTILLERS  BUY ₹20.42 at ₹2,812.30 (fresh Friday signal — ACCUMULATE: surged 11.83× weekly on 2023-05-19 (month 2.73×), ladder rising NOW — promoted from the ladder watch; stop ₹2,482.68; charges ₹0.0242)
2023-07-12  KSB         SELL ₹10.05 at stop ₹407.74 (-2.4%, charges ₹0.0104) — the cash goes back to work at the next Friday screen
2023-07-17  THANGAMAYL  SELL ₹20.42 at stop ₹1,344.25 (+0.0%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2023-07-24  GANESHHOUC  BUY ₹22.80 at ₹457.00 (fresh Friday signal — BUY: 23.66× weekly, month 7.84×, ladder rising; stop ₹359.10; charges ₹0.0270)
2023-08-14  GANESHHOUC  SELL ₹20.84 at stop ₹418.62 (-8.4%, charges ₹0.0216) — the cash goes back to work at the next Friday screen
2023-08-21  KIOCL       BUY ₹23.49 at ₹223.00 (fresh Friday signal — ACCUMULATE: surged 21.95× weekly on 2023-08-04 (month 3.62×), ladder rising NOW — promoted from the ladder watch; stop ₹199.78; charges ₹0.0278)
2023-09-13  INGERRAND   SELL ₹11.64 at stop ₹3,022.99 (+12.4%, charges ₹0.0121) — the cash goes back to work at the next Friday screen
2023-09-18  GHCL        BUY ₹16.66 at ₹648.00 (fresh Friday signal — BUY: surged 5.59× weekly on 2023-09-01 (month 2.23×), ladder rising NOW — promoted from the ladder watch; stop ₹568.10; charges ₹0.0197)
2023-09-21  SIS         SELL ₹13.58 at stop ₹424.60 (+10.5%, charges ₹0.0141) — the cash goes back to work at the next Friday screen
2023-09-25  IOB         BUY ₹13.58 at ₹44.40 (fresh Friday signal — BUY: 7.60× weekly, month 2.94×, ladder rising; stop ₹28.26; charges ₹0.0161)
2023-10-19  OLECTRA     SELL ₹34.66 at stop ₹1,121.00 (+76.6%, charges ₹0.0360) — the cash goes back to work at the next Friday screen
2023-10-23  GHCL        SELL ₹14.95 at stop ₹582.83 (-10.1%, charges ₹0.0155) — the cash goes back to work at the next Friday screen
2023-10-23  IOB         SELL ₹12.09 at stop ₹39.62 (-10.8%, charges ₹0.0125) — the cash goes back to work at the next Friday screen
2023-10-23  TIPSINDLTD  BUY ₹24.44 at ₹358.00 (fresh Friday signal — BUY: 4.52× weekly, month 1.76×, ladder rising; stop ₹270.23; charges ₹0.0290)
2023-10-23  VSTTILLERS  SELL ₹25.48 at stop ₹3,516.05 (+25.0%, charges ₹0.0264) — the cash goes back to work at the next Friday screen
2023-10-30  IIFLSEC     BUY ₹24.35 at ₹100.40 (fresh Friday signal — ACCUMULATE: surged 7.44× weekly on 2023-10-20 (month 4.56×), ladder rising NOW — promoted from the ladder watch; stop ₹87.69; charges ₹0.0288)
2023-10-30  KKCL        BUY ₹24.37 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0289)
2023-10-30  SHAREINDIA  BUY ₹14.03 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0166)
2024-01-17  TIIL        SELL ₹43.15 at stop ₹2,337.00 (+109.3%, charges ₹0.0448) — the cash goes back to work at the next Friday screen
2024-01-23  3MINDIA     BUY ₹14.62 at ₹34,850.00 (fresh Friday signal — ACCUMULATE: surged 14.46× weekly on 2023-12-29 (month 2.55×), ladder rising NOW — promoted from the ladder watch; stop ₹31,629.68; charges ₹0.0173)
2024-01-23  GANESHHOUC  BUY ₹28.52 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0338)
2024-01-29  SWARAJENG   SELL ₹19.83 at stop ₹2,210.32 (+22.1%, charges ₹0.0206) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹19.83 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0235)
2024-02-13  3MINDIA     SELL ₹13.24 at stop ₹31,629.68 (-9.2%, charges ₹0.0137) — the cash goes back to work at the next Friday screen
2024-03-05  GLS         SELL ₹34.05 at stop ₹779.48 (+86.5%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2024-03-05  IIFLSEC     SELL ₹31.95 at stop ₹132.05 (+31.5%, charges ₹0.0331) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹16.67 at stop ₹357.20 (+19.1%, charges ₹0.0173) — the cash goes back to work at the next Friday screen
2024-03-11  PILANIINVS  BUY ₹29.28 at ₹3,893.90 (fresh Friday signal — BUY: surged 7.04× weekly on 2024-03-01 (month 2.60×), ladder rising NOW — promoted from the ladder watch; stop ₹3,091.63; charges ₹0.0347)
2024-03-11  PSB         BUY ₹29.09 at ₹64.10 (fresh Friday signal — ACCUMULATE: surged 5.07× weekly on 2024-02-09 (month 3.12×), ladder rising NOW — promoted from the ladder watch; stop ₹51.89; charges ₹0.0345)
2024-03-11  TCI         SELL ₹15.84 at stop ₹790.40 (-20.0%, charges ₹0.0164) — the cash goes back to work at the next Friday screen
2024-03-11  TRENT       BUY ₹29.08 at ₹2,654.67 (fresh Friday signal — ACCUMULATE: surged 5.91× weekly on 2024-02-09 (month 2.06×), ladder rising NOW — promoted from the ladder watch; stop ₹2,395.27; charges ₹0.0345)
2024-03-13  KKCL        SELL ₹21.52 at stop ₹674.12 (-11.5%, charges ₹0.0223) — the cash goes back to work at the next Friday screen
2024-03-13  TIPSINDLTD  SELL ₹30.88 at stop ₹453.39 (+26.6%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹28.59 at stop ₹666.47 (+0.5%, charges ₹0.0297) — the cash goes back to work at the next Friday screen
2024-03-18  ICICIGI     BUY ₹27.16 at ₹1,646.00 (fresh Friday signal — ACCUMULATE: surged 3.64× weekly on 2024-03-01 (month 1.55×), ladder rising NOW — promoted from the ladder watch; stop ₹1,543.84; charges ₹0.0322)
2024-03-18  INDIGO      BUY ₹27.23 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0323)
2024-03-18  JINDWORLD   BUY ₹23.63 at ₹331.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2024-02-23 (month 4.51×), ladder rising NOW — promoted from the ladder watch; stop ₹341.71; charges ₹0.0280)
2024-03-18  SOLARINDS   BUY ₹27.27 at ₹8,900.05 (fresh Friday signal — BUY: 4.28× weekly, month 2.84×, ladder rising; stop ₹5,332.29; charges ₹0.0323)
2024-03-19  JINDWORLD   SELL ₹24.34 at stop ₹341.71 (+3.2%, charges ₹0.0252) — the cash goes back to work at the next Friday screen
2024-03-26  CMSINFO     BUY ₹24.34 at ₹384.65 (fresh Friday signal — ACCUMULATE: surged 11.05× weekly on 2024-03-01 (month 2.35×), ladder rising NOW — promoted from the ladder watch; stop ₹357.20; charges ₹0.0288)
2024-04-01  CMSINFO     TRIM 4.4% (₹1.07 at ₹389.10) to pay the tax bill
2024-04-01  ICICIGI     TRIM 4.4% (₹1.22 at ₹1,697.85) to pay the tax bill
2024-04-01  INDIGO      TRIM 4.4% (₹1.32 at ₹3,548.95) to pay the tax bill
2024-04-01  JSWHL       TRIM 4.4% (₹1.39 at ₹7,225.05) to pay the tax bill
2024-04-01  KIOCL       TRIM 4.4% (₹1.89 at ₹411.25) to pay the tax bill
2024-04-01  MEGH        TRIM 4.4% (₹0.70 at ₹138.25) to pay the tax bill
2024-04-01  PILANIINVS  TRIM 4.4% (₹1.13 at ₹3,439.80) to pay the tax bill
2024-04-01  PSB         TRIM 4.4% (₹1.26 at ₹63.50) to pay the tax bill
2024-04-01  SOLARINDS   TRIM 4.4% (₹1.17 at ₹8,726.05) to pay the tax bill
2024-04-01  TAX         FY2024 settled: ₹12.3695 paid (STCG ₹61.85 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-01  TRENT       TRIM 4.4% (₹1.24 at ₹2,591.20) to pay the tax bill
2024-05-09  PILANIINVS  SELL ₹26.62 at stop ₹3,710.37 (-4.7%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2024-05-13  JSWHL       SELL ₹26.37 at stop ₹6,280.45 (+33.6%, charges ₹0.0274) — the cash goes back to work at the next Friday screen
2024-05-13  PSB         SELL ₹23.42 at stop ₹54.09 (-15.6%, charges ₹0.0243) — the cash goes back to work at the next Friday screen
2024-05-13  TEJASNET    BUY ₹26.62 at ₹1,124.95 (fresh Friday signal — ACCUMULATE: surged 11.31× weekly on 2024-04-26 (month 2.75×), ladder rising NOW — promoted from the ladder watch; stop ₹982.30; charges ₹0.0315)
2024-05-21  SUDARSCHEM  BUY ₹21.28 at ₹832.00 (fresh Friday signal — ACCUMULATE: surged 7.51× weekly on 2024-04-26 (month 3.09×), ladder rising NOW — promoted from the ladder watch; stop ₹672.36; charges ₹0.0252)
2024-05-21  VIJAYA      BUY ₹28.52 at ₹803.00 (fresh Friday signal — BUY: surged 19.81× weekly on 2024-05-10 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹621.82; charges ₹0.0338)
2024-06-04  ICICIGI     SELL ₹24.30 at stop ₹1,543.84 (-6.2%, charges ₹0.0252) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹23.33 at stop ₹7,980.95 (-10.3%, charges ₹0.0242) — the cash goes back to work at the next Friday screen
2024-06-10  BHARATRAS   BUY ₹28.55 at ₹2,646.25 (fresh Friday signal — ACCUMULATE: surged 14.67× weekly on 2024-05-31 (month 4.36×), ladder rising NOW — promoted from the ladder watch; stop ₹2,171.27; charges ₹0.0338)
2024-06-10  FIEMIND     BUY ₹19.09 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0226)
2024-06-25  VIJAYA      SELL ₹25.88 at stop ₹730.50 (-9.0%, charges ₹0.0268) — the cash goes back to work at the next Friday screen
2024-07-01  ROUTE       BUY ₹25.88 at ₹1,814.45 (fresh Friday signal — BUY: 31.30× weekly, month 3.19×, ladder rising; stop ₹1,425.00; charges ₹0.0307)
2024-07-10  BHARATRAS   SELL ₹29.53 at stop ₹2,743.14 (+3.7%, charges ₹0.0306) — the cash goes back to work at the next Friday screen
2024-07-10  SUDARSCHEM  SELL ₹21.93 at stop ₹859.23 (+3.3%, charges ₹0.0227) — the cash goes back to work at the next Friday screen
2024-07-10  TEJASNET    SELL ₹31.02 at stop ₹1,313.90 (+16.8%, charges ₹0.0322) — the cash goes back to work at the next Friday screen
2024-07-15  ELECON      BUY ₹29.76 at ₹650.48 (fresh Friday signal — BUY: surged 6.79× weekly on 2024-06-14 (month 1.65×), ladder rising NOW — promoted from the ladder watch; stop ₹603.25; charges ₹0.0353)
2024-07-15  POLYMED     BUY ₹29.74 at ₹2,100.00 (fresh Friday signal — BUY: surged 7.26× weekly on 2024-06-21 (month 1.56×), ladder rising NOW — promoted from the ladder watch; stop ₹1,826.80; charges ₹0.0352)
2024-07-15  STYLAMIND   BUY ₹22.97 at ₹2,019.00 (fresh Friday signal — BUY: surged 6.44× weekly on 2024-06-28 (month 2.13×), ladder rising NOW — promoted from the ladder watch; stop ₹1,803.38; charges ₹0.0272)
2024-07-18  ELECON      SELL ₹27.54 at stop ₹603.25 (-7.3%, charges ₹0.0286) — the cash goes back to work at the next Friday screen
2024-07-22  BOROLTD     BUY ₹27.54 at ₹351.05 (fresh Friday signal — ACCUMULATE: surged 5.77× weekly on 2024-07-05 (month 3.23×), ladder rising NOW — promoted from the ladder watch; stop ₹331.93; charges ₹0.0326)
2024-07-22  TRENT       SELL ₹36.21 at stop ₹3,464.36 (+30.5%, charges ₹0.0376) — the cash goes back to work at the next Friday screen
2024-07-23  FIEMIND     SELL ₹18.15 at stop ₹1,257.56 (-4.7%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2024-07-26  ROUTE       SELL ₹23.68 at stop ₹1,663.69 (-8.3%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹28.89 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0342)
2024-07-29  INDIGOPNTS  BUY ₹20.22 at ₹1,496.95 (fresh Friday signal — ACCUMULATE: surged 9.66× weekly on 2024-07-12 (month 1.82×), ladder rising NOW — promoted from the ladder watch; stop ₹1,357.74; charges ₹0.0240)
2024-07-29  THYROCARE   BUY ₹28.92 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0343)
2024-08-01  POLYMED     SELL ₹26.31 at stop ₹1,861.67 (-11.3%, charges ₹0.0273) — the cash goes back to work at the next Friday screen
2024-08-05  PCBL        BUY ₹26.31 at ₹364.05 (fresh Friday signal — BUY: 10.04× weekly, month 2.68×, ladder rising; stop ₹246.00; charges ₹0.0312)
2024-09-09  AVANTIFEED  SELL ₹26.86 at stop ₹650.13 (-6.8%, charges ₹0.0279) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹26.86 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0318)
2024-10-07  INDIGO      SELL ₹36.42 at stop ₹4,485.14 (+40.2%, charges ₹0.0378) — the cash goes back to work at the next Friday screen
2024-10-07  KIOCL       SELL ₹35.47 at stop ₹352.88 (+58.2%, charges ₹0.0368) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹29.26 at stop ₹796.15 (+1.4%, charges ₹0.0304) — the cash goes back to work at the next Friday screen
2024-10-14  ASTRAZEN    BUY ₹29.20 at ₹7,800.00 (fresh Friday signal — ACCUMULATE: surged 13.24× weekly on 2024-09-27 (month 4.07×), ladder rising NOW — promoted from the ladder watch; stop ₹6,768.80; charges ₹0.0346)
2024-10-14  GARFIBRES   BUY ₹29.16 at ₹805.75 (fresh Friday signal — ACCUMULATE: surged 10.91× weekly on 2024-09-20 (month 2.71×), ladder rising NOW — promoted from the ladder watch; stop ₹704.32; charges ₹0.0346)
2024-10-14  SAREGAMA    BUY ₹29.15 at ₹589.85 (fresh Friday signal — ACCUMULATE: surged 9.45× weekly on 2024-10-04 (month 4.55×), ladder rising NOW — promoted from the ladder watch; stop ₹541.54; charges ₹0.0345)
2024-10-15  SAREGAMA    SELL ₹26.71 at stop ₹541.54 (-8.2%, charges ₹0.0277) — the cash goes back to work at the next Friday screen
2024-10-18  PCBL        SELL ₹34.39 at stop ₹476.85 (+31.0%, charges ₹0.0357) — the cash goes back to work at the next Friday screen
2024-10-21  CONCORDBIO  BUY ₹16.81 at ₹2,018.05 (fresh Friday signal — ACCUMULATE: surged 6.49× weekly on 2024-09-20 (month 3.37×), ladder rising NOW — promoted from the ladder watch; stop ₹1,566.80; charges ₹0.0199)
2024-10-21  IIFL        BUY ₹28.87 at ₹452.35 (fresh Friday signal — ACCUMULATE: surged 6.67× weekly on 2024-09-20 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹391.93; charges ₹0.0342)
2024-10-21  MOTILALOFS  BUY ₹29.04 at ₹1,021.95 (fresh Friday signal — BUY: 7.74× weekly, month 5.64×, ladder rising; stop ₹656.59; charges ₹0.0344)
2024-10-24  IIFL        SELL ₹24.96 at stop ₹391.93 (-13.4%, charges ₹0.0259) — the cash goes back to work at the next Friday screen
2024-10-28  CARERATING  BUY ₹24.96 at ₹1,396.00 (fresh Friday signal — BUY: surged 3.30× weekly on 2024-10-11 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹1,066.23; charges ₹0.0296)
2024-10-28  CMSINFO     SELL ₹32.95 at stop ₹545.68 (+41.9%, charges ₹0.0342) — the cash goes back to work at the next Friday screen
2024-11-04  UNICHEMLAB  BUY ₹28.21 at ₹874.35 (fresh Friday signal — ACCUMULATE: surged 9.84× weekly on 2024-10-25 (month 3.48×), ladder rising NOW — promoted from the ladder watch; stop ₹711.49; charges ₹0.0666)
2024-11-14  ASTRAZEN    SELL ₹25.58 at stop ₹6,854.77 (-12.1%, charges ₹0.0568) — the cash goes back to work at the next Friday screen
2024-11-18  BOROLTD     SELL ₹32.17 at stop ₹411.49 (+17.2%, charges ₹0.0715) — the cash goes back to work at the next Friday screen
2024-11-18  GANESHHOUC  BUY ₹27.46 at ₹1,059.00 (fresh Friday signal — BUY: surged 4.01× weekly on 2024-10-18 (month 1.75×), ladder rising NOW — promoted from the ladder watch; stop ₹867.10; charges ₹0.0648)
2024-11-18  INDIGOPNTS  SELL ₹19.67 at stop ₹1,460.72 (-2.4%, charges ₹0.0437) — the cash goes back to work at the next Friday screen
2024-11-25  PRIVISCL    BUY ₹28.26 at ₹1,829.50 (fresh Friday signal — ACCUMULATE: surged 2.78× weekly on 2024-11-08 (month 2.77×), ladder rising NOW — promoted from the ladder watch; stop ₹1,643.12; charges ₹0.0667)
2024-11-25  UTIAMC      BUY ₹26.45 at ₹1,338.75 (fresh Friday signal — ACCUMULATE: surged 1.86× weekly on 2024-11-01 (month 2.10×), ladder rising NOW — promoted from the ladder watch; stop ₹1,191.16; charges ₹0.0624)
2024-12-20  UNICHEMLAB  SELL ₹22.85 at stop ₹711.49 (-18.6%, charges ₹0.0507) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹22.85 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.0539)
2024-12-26  PRSMJOHNSN  SELL ₹21.29 at stop ₹170.55 (-20.5%, charges ₹0.0473) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹21.29 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.0502)
2025-01-09  GARFIBRES   SELL ₹29.91 at stop ₹829.35 (+2.9%, charges ₹0.0664) — the cash goes back to work at the next Friday screen
2025-01-09  KSL         SELL ₹20.21 at stop ₹1,059.30 (-11.1%, charges ₹0.0449) — the cash goes back to work at the next Friday screen
2025-01-09  UTIAMC      SELL ₹23.42 at stop ₹1,191.16 (-11.0%, charges ₹0.0520) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹25.32 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0598)
2025-01-13  CARERATING  SELL ₹22.09 at stop ₹1,239.70 (-11.2%, charges ₹0.0491) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹22.98 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.0543)
2025-01-13  VARROC      BUY ₹25.25 at ₹590.00 (fresh Friday signal — ACCUMULATE: surged 1.67× weekly on 2025-01-03 (month 2.95×), ladder rising NOW — promoted from the ladder watch; stop ₹563.49; charges ₹0.0596)
2025-01-17  MOTILALOFS  SELL ₹22.34 at stop ₹788.79 (-22.8%, charges ₹0.0496) — the cash goes back to work at the next Friday screen
2025-01-20  DMART       BUY ₹25.84 at ₹3,624.00 (fresh Friday signal — ACCUMULATE: surged 3.63× weekly on 2025-01-03 (month 2.27×), ladder rising NOW — promoted from the ladder watch; stop ₹3,226.13; charges ₹0.0610)
2025-01-20  PTCIL       BUY ₹18.59 at ₹16,420.00 (fresh Friday signal — ACCUMULATE: surged 3.56× weekly on 2025-01-10 (month 2.38×), ladder rising NOW — promoted from the ladder watch; stop ₹15,417.55; charges ₹0.0439)
2025-01-21  PTCIL       SELL ₹17.37 at stop ₹15,417.55 (-6.1%, charges ₹0.0386) — the cash goes back to work at the next Friday screen
2025-01-22  VARROC      SELL ₹24.00 at stop ₹563.49 (-4.5%, charges ₹0.0533) — the cash goes back to work at the next Friday screen
2025-01-23  STYLAMIND   SELL ₹22.31 at stop ₹1,967.22 (-2.6%, charges ₹0.0495) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹21.15 at stop ₹700.36 (-16.1%, charges ₹0.0470) — the cash goes back to work at the next Friday screen
2025-01-27  CONCORDBIO  SELL ₹16.37 at stop ₹1,971.77 (-2.3%, charges ₹0.0364) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹24.21 at ₹850.00 (fresh Friday signal — ACCUMULATE: surged 9.13× weekly on 2025-01-10 (month 6.49×), ladder rising NOW — promoted from the ladder watch; stop ₹825.52; charges ₹0.0572)
2025-01-28  LLOYDSME    SELL ₹19.97 at stop ₹1,258.75 (-12.7%, charges ₹0.0444) — the cash goes back to work at the next Friday screen
2025-01-28  PRIVISCL    SELL ₹25.27 at stop ₹1,643.12 (-10.2%, charges ₹0.0561) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹25.10 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.0593)
2025-02-12  JINDWORLD   SELL ₹19.44 at stop ₹374.11 (-8.2%, charges ₹0.0432) — the cash goes back to work at the next Friday screen
2025-02-24  GODFRYPHLP  BUY ₹23.29 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.0550)
2025-02-28  GANESHHOUC  SELL ₹28.14 at stop ₹1,090.38 (+3.0%, charges ₹0.0625) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹22.58 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0533)
2025-03-03  ZENSARTECH  SELL ₹19.20 at stop ₹727.84 (-23.1%, charges ₹0.0427) — the cash goes back to work at the next Friday screen
2025-03-10  AARTIPHARM  BUY ₹22.97 at ₹744.90 (fresh Friday signal — ACCUMULATE: surged 1.58× weekly on 2025-02-21 (month 4.42×), ladder rising NOW — promoted from the ladder watch; stop ₹640.24; charges ₹0.0542)
2025-03-10  GRWRHITECH  BUY ₹23.05 at ₹4,219.95 (fresh Friday signal — BUY: surged 2.69× weekly on 2025-02-14 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹3,504.00; charges ₹0.0544)
2025-03-10  SUVENPHAR   BUY ₹23.07 at ₹1,166.00 (fresh Friday signal — ACCUMULATE: surged 4.03× weekly on 2025-02-21 (month 1.56×), ladder rising NOW — promoted from the ladder watch; stop ₹1,038.10; charges ₹0.0545)
2025-03-17  AVANTIFEED  BUY ₹23.41 at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹0.0553)
2025-03-17  CASTROLIND  BUY ₹23.39 at ₹233.90 (fresh Friday signal — ACCUMULATE: surged 4.16× weekly on 2025-03-07 (month 2.15×), ladder rising NOW — promoted from the ladder watch; stop ₹215.90; charges ₹0.0552)
2025-03-20  CASTROLIND  SELL ₹21.49 at stop ₹215.90 (-7.7%, charges ₹0.0477) — the cash goes back to work at the next Friday screen
2025-03-24  INDIASHLTR  BUY ₹23.63 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.0558)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹10.41 / LT ₹0.00)
2025-04-03  GRWRHITECH  SELL ₹19.59 at stop ₹3,602.82 (-14.6%, charges ₹0.0435) — the cash goes back to work at the next Friday screen
2025-04-07  AARTIPHARM  SELL ₹19.66 at stop ₹640.24 (-14.1%, charges ₹0.0437) — the cash goes back to work at the next Friday screen
2025-04-07  AVANTIFEED  SELL ₹17.95 at stop ₹648.95 (-23.0%, charges ₹0.0399) — the cash goes back to work at the next Friday screen
2025-04-07  FINEORG     BUY ₹19.59 at ₹3,600.15 (fresh Friday signal — ACCUMULATE: surged 2.90× weekly on 2025-03-27 (month 1.61×), ladder rising NOW — promoted from the ladder watch; stop ₹3,791.55; charges ₹0.0462)
2025-04-07  INDIASHLTR  SELL ₹21.86 at stop ₹738.82 (-7.1%, charges ₹0.0486) — the cash goes back to work at the next Friday screen
2025-04-07  SUVENPHAR   SELL ₹20.45 at stop ₹1,038.10 (-11.0%, charges ₹0.0454) — the cash goes back to work at the next Friday screen
2025-04-15  GODREJIND   BUY ₹23.51 at ₹1,144.00 (fresh Friday signal — ACCUMULATE: surged 2.24× weekly on 2025-03-13 (month 6.73×), ladder rising NOW — promoted from the ladder watch; stop ₹954.30; charges ₹0.0555)
2025-04-15  SPARC       BUY ₹23.50 at ₹146.90 (fresh Friday signal — ACCUMULATE: surged 2.67× weekly on 2025-03-27 (month 3.93×), ladder rising NOW — promoted from the ladder watch; stop ₹134.04; charges ₹0.0555)
2025-04-15  TEJASNET    BUY ₹23.50 at ₹859.00 (fresh Friday signal — ACCUMULATE: surged 5.18× weekly on 2025-04-04 (month 4.12×), ladder rising NOW — promoted from the ladder watch; stop ₹679.16; charges ₹0.0555)
2025-05-09  TEJASNET    SELL ₹18.49 at stop ₹679.16 (-20.9%, charges ₹0.0411) — the cash goes back to work at the next Friday screen
2025-05-12  THYROCARE   BUY ₹23.65 at ₹965.00 (fresh Friday signal — BUY: surged 25.39× weekly on 2025-04-25 (month 2.07×), ladder rising NOW — promoted from the ladder watch; stop ₹824.60; charges ₹0.0558)
2025-06-06  THYROCARE   SELL ₹22.00 at stop ₹901.60 (-6.6%, charges ₹0.0489) — the cash goes back to work at the next Friday screen
2025-06-09  CCL         BUY ₹24.73 at ₹878.00 (fresh Friday signal — BUY: surged 52.15× weekly on 2025-05-09 (month 6.55×), ladder rising NOW — promoted from the ladder watch; stop ₹755.63; charges ₹0.0584)
2025-06-19  SPARC       SELL ₹24.01 at stop ₹150.81 (+2.7%, charges ₹0.0533) — the cash goes back to work at the next Friday screen
2025-06-23  FINEORG     SELL ₹24.36 at stop ₹4,498.25 (+24.9%, charges ₹0.0541) — the cash goes back to work at the next Friday screen
2025-06-23  OPTIEMUS    BUY ₹24.15 at ₹659.90 (fresh Friday signal — BUY: 15.64× weekly, month 2.48×, ladder rising; stop ₹559.36; charges ₹0.0570)
2025-06-30  SUBROS      BUY ₹24.88 at ₹944.90 (fresh Friday signal — ACCUMULATE: surged 20.53× weekly on 2025-06-20 (month 8.07×), ladder rising NOW — promoted from the ladder watch; stop ₹848.42; charges ₹0.0587)
2025-07-02  GODREJIND   SELL ₹24.14 at stop ₹1,179.90 (+3.1%, charges ₹0.0536) — the cash goes back to work at the next Friday screen
2025-07-07  KSL         BUY ₹24.49 at ₹959.55 (fresh Friday signal — BUY: surged 13.70× weekly on 2025-06-20 (month 2.70×), ladder rising NOW — promoted from the ladder watch; stop ₹813.20; charges ₹0.0578)
2025-07-25  SUBROS      SELL ₹22.24 at stop ₹848.42 (-10.2%, charges ₹0.0494) — the cash goes back to work at the next Friday screen
2025-07-28  BOMDYEING   BUY ₹22.74 at ₹181.45 (fresh Friday signal — BUY: 21.87× weekly, month 4.30×, ladder rising; stop ₹148.64; charges ₹0.0537)
2025-07-28  OPTIEMUS    SELL ₹20.56 at stop ₹564.30 (-14.5%, charges ₹0.0457) — the cash goes back to work at the next Friday screen
2025-08-04  DCMSHRIRAM  BUY ₹20.56 at ₹1,386.00 (fresh Friday signal — ACCUMULATE: surged 18.98× weekly on 2025-07-04 (month 4.95×), ladder rising NOW — promoted from the ladder watch; stop ₹1,266.35; charges ₹0.0485)
2025-08-04  NH          SELL ₹28.14 at stop ₹1,814.78 (+25.2%, charges ₹0.0625) — the cash goes back to work at the next Friday screen
2025-08-11  KSL         SELL ₹21.73 at stop ₹855.00 (-10.9%, charges ₹0.0483) — the cash goes back to work at the next Friday screen
2025-08-11  RAIN        BUY ₹23.61 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.0557)
2025-08-18  BLACKBUCK   BUY ₹23.91 at ₹553.00 (fresh Friday signal — ACCUMULATE: surged 9.73× weekly on 2025-08-08 (month 3.62×), ladder rising NOW — promoted from the ladder watch; stop ₹473.20; charges ₹0.0564)
2025-08-18  DCMSHRIRAM  SELL ₹18.70 at stop ₹1,266.35 (-8.6%, charges ₹0.0415) — the cash goes back to work at the next Friday screen
2025-08-25  KIOCL       BUY ₹21.04 at ₹434.45 (fresh Friday signal — BUY: surged 9.67× weekly on 2025-08-01 (month 9.01×), ladder rising NOW — promoted from the ladder watch; stop ₹301.02; charges ₹0.0497)
2025-08-26  RAIN        SELL ₹21.07 at stop ₹143.64 (-10.4%, charges ₹0.0468) — the cash goes back to work at the next Friday screen
2025-09-01  RSYSTEMS    BUY ₹21.07 at ₹460.00 (fresh Friday signal — BUY: surged 17.81× weekly on 2025-08-22 (month 4.67×), ladder rising NOW — promoted from the ladder watch; stop ₹394.44; charges ₹0.0497)
2025-09-16  GODFRYPHLP  SELL ₹35.97 at stop ₹8,967.50 (+55.1%, charges ₹0.0799) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹12.32 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.75× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.0291)
2025-09-22  HEMIPROP    BUY ₹23.66 at ₹171.25 (fresh Friday signal — ACCUMULATE: surged 14.83× weekly on 2025-09-05 (month 2.96×), ladder rising NOW — promoted from the ladder watch; stop ₹159.33; charges ₹0.0558)
2025-09-24  RSYSTEMS    SELL ₹19.30 at stop ₹423.23 (-8.0%, charges ₹0.0429) — the cash goes back to work at the next Friday screen
2025-09-25  BOMDYEING   SELL ₹21.54 at stop ₹172.67 (-4.8%, charges ₹0.0478) — the cash goes back to work at the next Friday screen
2025-09-29  JTEKTINDIA  BUY ₹17.52 at ₹168.40 (fresh Friday signal — ACCUMULATE: surged 5.42× weekly on 2025-09-12 (month 13.89×), ladder rising NOW — promoted from the ladder watch; stop ₹154.34; charges ₹0.0413)
2025-09-29  SUBROS      BUY ₹23.32 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0551)
2025-10-03  DMART       SELL ₹31.26 at stop ₹4,404.96 (+21.5%, charges ₹0.0694) — the cash goes back to work at the next Friday screen
2025-10-06  HEMIPROP    SELL ₹21.91 at stop ₹159.33 (-7.0%, charges ₹0.0487) — the cash goes back to work at the next Friday screen
2025-10-06  MINDACORP   BUY ₹23.83 at ₹590.90 (fresh Friday signal — ACCUMULATE: surged 18.19× weekly on 2025-09-26 (month 3.44×), ladder rising NOW — promoted from the ladder watch; stop ₹536.85; charges ₹0.0563)
2025-10-09  JTEKTINDIA  SELL ₹15.98 at stop ₹154.34 (-8.3%, charges ₹0.0355) — the cash goes back to work at the next Friday screen
2025-10-13  RAMKY       BUY ₹23.48 at ₹622.35 (fresh Friday signal — BUY: 20.34× weekly, month 6.75×, ladder rising; stop ₹529.58; charges ₹0.0554)
2025-10-13  SHAILY      BUY ₹21.84 at ₹2,434.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 1.66×, ladder rising; stop ₹1,942.00; charges ₹0.0516)
2025-10-14  SUBROS      SELL ₹21.47 at stop ₹1,046.90 (-7.5%, charges ₹0.0477) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹21.47 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0507)
2025-10-20  CREDITACC   SELL ₹36.14 at stop ₹1,274.42 (+49.9%, charges ₹0.0803) — the cash goes back to work at the next Friday screen
2025-10-27  INFIBEAM    BUY ₹13.36 at ₹18.94 (fresh Friday signal — ACCUMULATE: surged 4.46× weekly on 2025-10-10 (month 1.58×), ladder rising NOW — promoted from the ladder watch; stop ₹17.40; charges ₹0.0315)
2025-10-27  VMART       BUY ₹22.77 at ₹858.00 (fresh Friday signal — ACCUMULATE: surged 13.79× weekly on 2025-10-03 (month 3.80×), ladder rising NOW — promoted from the ladder watch; stop ₹806.50; charges ₹0.0538)
2025-10-28  BLACKBUCK   SELL ₹27.64 at stop ₹642.20 (+16.1%, charges ₹0.0614) — the cash goes back to work at the next Friday screen
2025-11-03  TATACOMM    BUY ₹22.46 at ₹1,875.40 (fresh Friday signal — ACCUMULATE: surged 4.92× weekly on 2025-10-17 (month 3.69×), ladder rising NOW — promoted from the ladder watch; stop ₹1,750.94; charges ₹0.0530)
2025-11-06  FDC         SELL ₹10.66 at stop ₹425.79 (-13.0%, charges ₹0.0237) — the cash goes back to work at the next Friday screen
2025-11-07  VMART       SELL ₹21.31 at stop ₹806.50 (-6.0%, charges ₹0.0473) — the cash goes back to work at the next Friday screen
2025-11-10  CUB         BUY ₹22.66 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.0535)
2025-11-10  TDPOWERSYS  BUY ₹14.49 at ₹389.50 (fresh Friday signal — BUY: 3.09× weekly, month 2.39×, ladder rising; stop ₹276.78; charges ₹0.0342)
2025-11-11  INFIBEAM    SELL ₹12.22 at stop ₹17.40 (-8.1%, charges ₹0.0271) — the cash goes back to work at the next Friday screen
2025-11-17  PGIL        BUY ₹12.22 at ₹844.05 (fresh Friday signal — BUY: 19.68× weekly, month 3.53×, ladder rising; stop ₹612.56; charges ₹0.0289)
2025-11-20  ANANDRATHI  SELL ₹19.68 at stop ₹1,450.17 (-7.9%, charges ₹0.0437) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹27.37 at stop ₹976.41 (+11.2%, charges ₹0.0608) — the cash goes back to work at the next Friday screen
2025-11-24  HATSUN      BUY ₹19.68 at ₹1,046.40 (fresh Friday signal — ACCUMULATE: surged 15.41× weekly on 2025-10-31 (month 4.59×), ladder rising NOW — promoted from the ladder watch; stop ₹946.43; charges ₹0.0465)
2025-11-24  KIOCL       SELL ₹18.14 at stop ₹376.46 (-13.3%, charges ₹0.0403) — the cash goes back to work at the next Friday screen
2025-11-24  TDPOWERSYS  SELL ₹13.24 at stop ₹357.49 (-8.2%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹22.10 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.33×, ladder rising; stop ₹535.37; charges ₹0.0522)
2025-12-01  GPPL        BUY ₹14.54 at ₹178.98 (fresh Friday signal — ACCUMULATE: surged 5.65× weekly on 2025-11-07 (month 2.18×), ladder rising NOW — promoted from the ladder watch; stop ₹163.50; charges ₹0.0343)
2025-12-01  PRICOLLTD   BUY ₹22.11 at ₹624.05 (fresh Friday signal — BUY: surged 9.29× weekly on 2025-11-07 (month 2.30×), ladder rising NOW — promoted from the ladder watch; stop ₹549.67; charges ₹0.0522)
2025-12-01  RAMKY       SELL ₹21.71 at stop ₹578.17 (-7.1%, charges ₹0.0482) — the cash goes back to work at the next Friday screen
2025-12-08  ESABINDIA   BUY ₹21.49 at ₹5,750.00 (fresh Friday signal — ACCUMULATE: surged 27.55× weekly on 2025-11-14 (month 4.46×), ladder rising NOW — promoted from the ladder watch; stop ₹5,247.99; charges ₹0.0507)
2025-12-09  PGIL        SELL ₹11.04 at stop ₹765.71 (-9.3%, charges ₹0.0245) — the cash goes back to work at the next Friday screen
2025-12-15  NATCOPHARM  BUY ₹11.26 at ₹905.65 (fresh Friday signal — BUY: surged 9.02× weekly on 2025-11-28 (month 2.43×), ladder rising NOW — promoted from the ladder watch; stop ₹825.79; charges ₹0.0266)
2025-12-15  SHAILY      SELL ₹20.91 at stop ₹2,340.80 (-3.8%, charges ₹0.0464) — the cash goes back to work at the next Friday screen
2025-12-22  KIRLOSENG   BUY ₹20.91 at ₹1,258.30 (fresh Friday signal — BUY: 4.09× weekly, month 1.67×, ladder rising; stop ₹1,014.88; charges ₹0.0494)
2026-01-08  EUREKAFORB  SELL ₹19.52 at stop ₹589.10 (-11.3%, charges ₹0.0434) — the cash goes back to work at the next Friday screen
2026-01-08  HATSUN      SELL ₹17.72 at stop ₹946.43 (-9.6%, charges ₹0.0394) — the cash goes back to work at the next Friday screen
2026-01-09  TATACOMM    SELL ₹20.87 at stop ₹1,750.94 (-6.6%, charges ₹0.0464) — the cash goes back to work at the next Friday screen
2026-01-12  ESABINDIA   SELL ₹20.85 at stop ₹5,605.00 (-2.5%, charges ₹0.0463) — the cash goes back to work at the next Friday screen
2026-01-12  HINDCOPPER  BUY ₹20.75 at ₹532.00 (fresh Friday signal — BUY: surged 1.55× weekly on 2025-12-12 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹456.95; charges ₹0.0490)
2026-01-12  KIRLOSENG   SELL ₹18.87 at stop ₹1,140.95 (-9.3%, charges ₹0.0419) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹20.76 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.0490)
2026-01-19  JBMA        BUY ₹20.57 at ₹592.05 (fresh Friday signal — ACCUMULATE: surged 4.93× weekly on 2026-01-02 (month 2.87×), ladder rising NOW — promoted from the ladder watch; stop ₹556.03; charges ₹0.0486)
2026-01-19  MINDACORP   SELL ₹21.60 at stop ₹537.94 (-9.0%, charges ₹0.0480) — the cash goes back to work at the next Friday screen
2026-01-19  PRICOLLTD   SELL ₹20.71 at stop ₹587.20 (-5.9%, charges ₹0.0460) — the cash goes back to work at the next Friday screen
2026-01-19  RAIN        BUY ₹20.55 at ₹139.49 (fresh Friday signal — ACCUMULATE: surged 2.72× weekly on 2026-01-02 (month 3.48×), ladder rising NOW — promoted from the ladder watch; stop ₹131.45; charges ₹0.0485)
2026-01-19  RBA         BUY ₹15.20 at ₹67.50 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.51×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.0359)
2026-01-20  JBMA        SELL ₹19.23 at stop ₹556.03 (-6.1%, charges ₹0.0427) — the cash goes back to work at the next Friday screen
2026-01-20  NATCOPHARM  SELL ₹10.22 at stop ₹825.79 (-8.8%, charges ₹0.0227) — the cash goes back to work at the next Friday screen
2026-01-20  RAIN        SELL ₹19.28 at stop ₹131.45 (-5.8%, charges ₹0.0428) — the cash goes back to work at the next Friday screen
2026-01-21  GPPL        SELL ₹13.72 at stop ₹169.62 (-5.2%, charges ₹0.0305) — the cash goes back to work at the next Friday screen
2026-02-02  CEIGALL     BUY ₹20.52 at ₹274.95 (fresh Friday signal — ACCUMULATE: surged 4.16× weekly on 2026-01-02 (month 1.71×), ladder rising NOW — promoted from the ladder watch; stop ₹253.32; charges ₹0.0484)
2026-02-02  MAHABANK    BUY ₹20.47 at ₹60.48 (fresh Friday signal — ACCUMULATE: surged 1.87× weekly on 2026-01-16 (month 1.60×), ladder rising NOW — promoted from the ladder watch; stop ₹59.76; charges ₹0.0483)
2026-02-02  TATAELXSI   BUY ₹20.48 at ₹5,448.00 (fresh Friday signal — ACCUMULATE: surged 3.74× weekly on 2026-01-09 (month 1.70×), ladder rising NOW — promoted from the ladder watch; stop ₹5,016.48; charges ₹0.0483)
2026-02-12  TATAELXSI   SELL ₹18.77 at stop ₹5,016.48 (-7.9%, charges ₹0.0417) — the cash goes back to work at the next Friday screen
2026-02-17  NATIONALUM  SELL ₹19.70 at stop ₹335.49 (-4.7%, charges ₹0.0438) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹20.04 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.67×, ladder rising; stop ₹5,440.18; charges ₹0.0473)
2026-02-23  E2E         BUY ₹20.35 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0480)
2026-02-23  HAPPYFORGE  BUY ₹20.11 at ₹1,370.00 (fresh Friday signal — BUY: surged 6.09× weekly on 2026-02-13 (month 1.85×), ladder rising NOW — promoted from the ladder watch; stop ₹1,188.64; charges ₹0.0475)
2026-02-23  VESUVIUS    BUY ₹20.42 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.0482)
2026-03-04  CEIGALL     SELL ₹19.78 at stop ₹266.33 (-3.1%, charges ₹0.0439) — the cash goes back to work at the next Friday screen
2026-03-04  HAPPYFORGE  SELL ₹18.03 at stop ₹1,234.05 (-9.9%, charges ₹0.0400) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹22.31 at stop ₹251.43 (-1.1%, charges ₹0.0496) — the cash goes back to work at the next Friday screen
2026-03-09  SANSERA     BUY ₹18.94 at ₹2,125.10 (fresh Friday signal — ACCUMULATE: surged 4.58× weekly on 2026-02-13 (month 2.89×), ladder rising NOW — promoted from the ladder watch; stop ₹2,033.00; charges ₹0.0447)
2026-03-09  VTL         BUY ₹18.91 at ₹532.95 (fresh Friday signal — ACCUMULATE: surged 1.53× weekly on 2026-02-27 (month 2.21×), ladder rising NOW — promoted from the ladder watch; stop ₹485.45; charges ₹0.0446)
2026-03-12  HINDCOPPER  SELL ₹20.52 at stop ₹528.63 (-0.6%, charges ₹0.0456) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹13.69 at stop ₹61.08 (-9.5%, charges ₹0.0304) — the cash goes back to work at the next Friday screen
2026-03-13  SANSERA     SELL ₹18.04 at stop ₹2,033.00 (-4.3%, charges ₹0.0401) — the cash goes back to work at the next Friday screen
2026-03-16  J&KBANK     BUY ₹18.76 at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.95×, ladder rising; stop ₹103.27; charges ₹0.0443)
2026-03-16  JBCHEPHARM  BUY ₹18.79 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0444)
2026-03-23  ABSLAMC     BUY ₹18.36 at ₹937.90 (fresh Friday signal — ACCUMULATE: surged 4.88× weekly on 2026-03-13 (month 2.34×), ladder rising NOW — promoted from the ladder watch; stop ₹876.18; charges ₹0.0434)
2026-03-23  BHARATFORG  BUY ₹18.26 at ₹1,700.00 (fresh Friday signal — ACCUMULATE: surged 1.59× weekly on 2026-02-27 (month 1.77×), ladder rising NOW — promoted from the ladder watch; stop ₹1,564.35; charges ₹0.0431)
2026-03-23  J&KBANK     SELL ₹17.06 at stop ₹110.67 (-8.6%, charges ₹0.0379) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹17.63 at stop ₹464.31 (-13.2%, charges ₹0.0392) — the cash goes back to work at the next Friday screen
2026-03-30  ABSLAMC     SELL ₹17.08 at stop ₹876.18 (-6.6%, charges ₹0.0379) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹18.10 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0427)
2026-03-30  MAHABANK    SELL ₹20.57 at stop ₹61.05 (+0.9%, charges ₹0.0457) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹47.08 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹18.03 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0426)
2026-04-13  INOXINDIA   BUY ₹18.51 at ₹1,299.10 (fresh Friday signal — BUY: 4.08× weekly, month 2.14×, ladder rising; stop ₹1,091.46; charges ₹0.0437)
2026-04-13  THERMAX     BUY ₹18.66 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.0441)
2026-05-13  INOXINDIA   SELL ₹19.46 at stop ₹1,372.18 (+5.6%, charges ₹0.0432) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹17.64 at stop ₹1,125.84 (-2.1%, charges ₹0.0392) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹18.09 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.0427)
2026-05-18  METROPOLIS  BUY ₹19.23 at ₹522.50 (fresh Friday signal — ACCUMULATE: surged 10.71× weekly on 2026-05-08 (month 1.72×), ladder rising NOW — promoted from the ladder watch; stop ₹489.25; charges ₹0.0454)
2026-06-05  E2E         SELL ₹16.21 at stop ₹2,330.72 (-20.0%, charges ₹0.0360) — the cash goes back to work at the next Friday screen
2026-06-08  SAREGAMA    BUY ₹16.21 at ₹465.55 (fresh Friday signal — BUY: surged 75.04× weekly on 2026-05-15 (month 13.54×), ladder rising NOW — promoted from the ladder watch; stop ₹364.42; charges ₹0.0383)
2026-07-29  THERMAX     SELL ₹22.25 at stop ₹4,306.64 (+19.8%, charges ₹0.0494) — the cash goes back to work at the next Friday screen
2026-07-31  VTL         SELL ₹20.94 at stop ₹592.80 (+11.2%, charges ₹0.0465) — the cash goes back to work at the next Friday screen
2026-08-03  ITDC        BUY ₹21.14 at ₹707.00 (fresh Friday signal — BUY: surged 16.08× weekly on 2026-07-10 (month 6.72×), ladder rising NOW — promoted from the ladder watch; stop ₹646.14; charges ₹0.0499)
2026-08-03  KARURVYSYA  BUY ₹21.16 at ₹343.50 (fresh Friday signal — ACCUMULATE: surged 8.37× weekly on 2026-07-24 (month 2.58×), ladder rising NOW — promoted from the ladder watch; stop ₹314.74; charges ₹0.0499)
2026-08-31  ITDC        SELL ₹19.45 at stop ₹653.65 (-7.5%, charges ₹0.0432) — the cash goes back to work at the next Friday screen
2026-08-31  SAREGAMA    SELL ₹16.76 at stop ₹483.79 (+3.9%, charges ₹0.0372) — the cash goes back to work at the next Friday screen
2026-09-04  BHARATFORG  SELL ₹20.89 at stop ₹1,953.29 (+14.9%, charges ₹0.0464) — the cash goes back to work at the next Friday screen
2026-09-07  GODREJAGRO  BUY ₹16.39 at ₹648.15 (fresh Friday signal — BUY: surged 7.19× weekly on 2026-08-28 (month 1.81×), ladder rising NOW — promoted from the ladder watch; stop ₹573.80; charges ₹0.0387)
2026-09-07  KENNAMET    BUY ₹20.81 at ₹4,717.00 (fresh Friday signal — ACCUMULATE: surged 7.35× weekly on 2026-08-14 (month 2.41×), ladder rising NOW — promoted from the ladder watch; stop ₹4,134.40; charges ₹0.0491)
2026-09-07  NAVINFLUOR  BUY ₹20.80 at ₹8,557.50 (fresh Friday signal — ACCUMULATE: surged 7.38× weekly on 2026-08-07 (month 1.57×), ladder rising NOW — promoted from the ladder watch; stop ₹7,704.50; charges ₹0.0491)
2026-09-10  ALKYLAMINE  SELL ₹20.23 at stop ₹1,920.99 (+12.3%, charges ₹0.0449) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹23.45 at stop ₹7,158.25 (+17.5%, charges ₹0.0521) — the cash goes back to work at the next Friday screen
2026-09-15  KARURVYSYA  SELL ₹20.06 at stop ₹327.23 (-4.7%, charges ₹0.0446) — the cash goes back to work at the next Friday screen
2026-09-15  LTFOODS     BUY ₹20.23 at ₹439.90 (fresh Friday signal — ACCUMULATE: surged 14.35× weekly on 2026-08-28 (month 2.26×), ladder rising NOW — promoted from the ladder watch; stop ₹408.07; charges ₹0.0478)
2026-09-16  KENNAMET    SELL ₹18.15 at stop ₹4,134.40 (-12.4%, charges ₹0.0403) — the cash goes back to work at the next Friday screen
2026-09-21  AVALON      BUY ₹20.17 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.0476)
2026-09-21  INOXINDIA   BUY ₹20.18 at ₹2,098.80 (fresh Friday signal — BUY: surged 2.84× weekly on 2026-08-28 (month 2.01×), ladder rising NOW — promoted from the ladder watch; stop ₹1,972.58; charges ₹0.0476)
2026-09-21  IPCALAB     BUY ₹20.19 at ₹2,012.00 (fresh Friday signal — BUY: surged 6.62× weekly on 2026-08-21 (month 2.62×), ladder rising NOW — promoted from the ladder watch; stop ₹1,833.31; charges ₹0.0477)
```
