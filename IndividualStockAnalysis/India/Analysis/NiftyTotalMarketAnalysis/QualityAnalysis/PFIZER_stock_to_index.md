# Pfizer Ltd. (PFIZER) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: LAGGED the index: the ratio fell -28% from FY2015 to FY2026.**

```
FY2015  █████████████████          272.584
FY2016  ███████████████            228.458  ▼ -16.2% vs prior year
FY2017  █████████████              205.851  ▼ -9.9% vs prior year
FY2018  █████████████              203.476  ▼ -1.2% vs prior year
FY2019  ██████████████████         280.065  ▲ +37.6% vs prior year
FY2020  ██████████████████████████ 408.016  ▲ +45.7% vs prior year
FY2021  ████████████████████       309.266  ▼ -24.2% vs prior year
FY2022  ████████████████           254.240  ▼ -17.8% vs prior year
FY2023  ████████████               191.926  ▼ -24.5% vs prior year
FY2024  ████████████               185.577  ▼ -3.3% vs prior year
FY2025  ██████████                 164.563  ▼ -11.3% vs prior year
FY2026  █████████████              196.708  ▲ +19.5% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2015 |
| last 10 years | FY2016 | FY2026 | -14% |
| last 5 years | FY2021 | FY2026 | -36% |
| last 3 years | FY2023 | FY2026 | +2% |
| last 1 year | FY2025 | FY2026 | +20% |


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

   +51% ┤
        │                             ╭──●╮
        │                        ●────╯   ╰╮
        │                       ╭╯         │
   +31% ┤                      ╭╯          ╰╮
        │                     ╭╯            │                                            ●
        │                   ╭─╯             ╰╮                                         ╭─╯
   +11% ┤                  ╭╯                ╰╮                                       ╭╯
        │                 ╭╯                  ╰╮                                     ╭╯
        │┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╭●╯┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈│┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈●─╮┈┈┈┈┈┈┈┈╭╯┈┈┈┈┈┈
   -10% ┤          ╭────╯                      ╰╮                     ╭──╯ ╰────╮ ╭─╯
        │     ╭──●─╯                            │                    ╭╯         ╰●╯
        │●────╯                                 ╰╮   ╭───●────╮   ╭──╯
        │                                        ●───╯        ╰──●╯
   -30% ┤
        └┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20    FY21    FY22    FY23    FY24    FY25    FY26

●      -16.2   -9.9    -1.2    +37.6   +45.7   -24.2   -17.8   -24.5   -3.3    -11.3   +19.5

● Price ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

**The value at every point of the graph** (also printed under each point above):

| Fiscal year | Price ratio |
|---|---|
| FY2016 | -16.2% |
| FY2017 | -9.9% |
| FY2018 | -1.2% |
| FY2019 | +37.6% |
| FY2020 | +45.7% |
| FY2021 | -24.2% |
| FY2022 | -17.8% |
| FY2023 | -24.5% |
| FY2024 | -3.3% |
| FY2025 | -11.3% |
| FY2026 | +19.5% |


The same graph in two other formats sits beside this file: [`PFIZER_stock_to_index.svg`](PFIZER_stock_to_index.svg) — a vector chart that opens in any browser — and [`PFIZER_stock_to_index.mmd`](PFIZER_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


## 5. The raw yearly values behind every ratio

Company prices in rupees; profits in Rs crore. The index close is the March close unless the company closes its books in another month (shown in brackets). '—' = not in the stored data.

| Fiscal year | Company price (Rs) | Nifty 50 close | Company PAT (Rs cr) | Index PAT (Rs cr) | Company OP (Rs cr) | Index OP (Rs cr) |
|---|---|---|---|---|---|---|
| FY2007 | — | — | 106 | — | 127 | — |
| FY2008 | — | — | 340 | — | -139 | — |
| FY2009 | — | — | 300 | — | -82 | — |
| FY2015 | 2,230.15 | 8,181.50 | — | 239,976 | — | 362,356 |
| FY2016 | 1,793.35 | 7,849.80 | — | 252,916 | — | 381,103 |
| FY2017 | 1,915.25 | 9,304.05 | — | 268,287 | — | 384,170 |
| FY2018 | 2,185.20 | 10,739.35 | — | 260,991 | — | 381,288 |
| FY2019 | 3,290.25 | 11,748.15 | — | 281,855 | — | 476,374 |
| FY2020 | 4,023.00 | 9,859.90 | — | 275,997 | — | 491,207 |
| FY2021 | 4,524.90 | 14,631.10 | — | 331,853 | — | 542,357 |
| FY2022 | 4,348.15 | 17,102.55 | — | 495,232 | — | 730,487 |
| FY2023 | 3,467.15 | 18,065.00 | — | 574,328 | — | 890,079 |
| FY2024 | 4,194.95 | 22,604.85 | — | 721,343 | — | 1,008,599 |
| FY2025 | 4,004.50 | 24,334.20 | — | 796,066 | — | 1,068,504 |
| FY2026 | 4,720.50 | 23,997.55 | — | 905,734 | — | 1,084,854 |


## Years the stored data could not cover

- Mar 2015: company Net Profit not in stored data
- Mar 2016: company Net Profit not in stored data
- Mar 2017: company Net Profit not in stored data
- Mar 2018: company Net Profit not in stored data
- Mar 2019: company Net Profit not in stored data
- Mar 2020: company Net Profit not in stored data
- Mar 2021: company Net Profit not in stored data
- Mar 2022: company Net Profit not in stored data
- Mar 2023: company Net Profit not in stored data
- Mar 2024: company Net Profit not in stored data
- Mar 2025: company Net Profit not in stored data
- Mar 2026: company Net Profit not in stored data


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
