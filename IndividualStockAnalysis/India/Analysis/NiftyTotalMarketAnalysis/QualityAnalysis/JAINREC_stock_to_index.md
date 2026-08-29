# Jain Resource (JAINREC) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: too little overlapping data to call a trend.**

```
FY2026  ██████████████████████████ 19.023
```


**Change over the standard windows**

*(too little data for window trends)*


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: GAINED on the index: the ratio rose +139% from FY2023 to FY2026.**

```
FY2023  ███████████                0.016%
FY2024  ███████████████            0.023%  ▲ +41.9% vs prior year
FY2025  ███████████████████        0.028%  ▲ +23.2% vs prior year
FY2026  ██████████████████████████ 0.038%  ▲ +36.8% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2023 |
| last 10 years | FY2016 | FY2026 | n/a — data starts FY2023 |
| last 5 years | FY2021 | FY2026 | n/a — data starts FY2023 |
| last 3 years | FY2023 | FY2026 | +139% |
| last 1 year | FY2025 | FY2026 | +37% |


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: GAINED on the index: the ratio rose +260% from FY2023 to FY2026.**

```
FY2023  ███████                    0.014%
FY2024  ████████████               0.023%  ▲ +60.5% vs prior year
FY2025  ██████████████████         0.035%  ▲ +53.2% vs prior year
FY2026  ██████████████████████████ 0.051%  ▲ +46.6% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2023 |
| last 10 years | FY2016 | FY2026 | n/a — data starts FY2023 |
| last 5 years | FY2021 | FY2026 | n/a — data starts FY2023 |
| last 3 years | FY2023 | FY2026 | +260% |
| last 1 year | FY2025 | FY2026 | +47% |


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

   +65% ┤
        │■═══╗
        │    ╚═══■══╗
        │           ╚══╗
   +48% ┤              ╚═■
        │◆━┓
        │  ┗━━┓        ┏━◆
   +30% ┤     ┗━┓   ┏━━┛
        │       ┗◆━━┛
        │
   +13% ┤
        │
        │
        │┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
    -5% ┤
        └┬───────┬───────┬──
       FY24    FY25    FY26

◆      +41.9   +23.2   +36.8
■      +60.5   +53.2   +46.6

◆ PAT ratio   ■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

Each line again on its own, for a closer read:

```
PAT RATIO — yearly change against the Nifty 50 (%)

   +45% ┤
        │◆┓
        │ ┗━┓           ┏◆
   +33% ┤   ┗┓         ┏┛
        │    ┗━┓    ┏━━┛
        │      ┗━┓ ┏┛
        │        ◆━┛
   +21% ┤
        │
        │
    +9% ┤
        │
        │
        │┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
    -3% ┤
        └┬───────┬───────┬──
       FY24    FY25    FY26

◆      +41.9   +23.2   +36.8

◆ PAT ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

```
OPERATING-PROFIT RATIO — yearly change against the Nifty 50 (%)

   +65% ┤
        │■═══╗
        │    ╚═══■══╗
        │           ╚══╗
   +48% ┤              ╚═■
        │
        │
   +30% ┤
        │
        │
   +13% ┤
        │
        │
        │┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
    -5% ┤
        └┬───────┬───────┬──
       FY24    FY25    FY26

■      +60.5   +53.2   +46.6

■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```


**The value at every point of the graph** (also printed under each point above):

| Fiscal year | PAT ratio | Operating-profit ratio |
|---|---|---|
| FY2024 | +41.9% | +60.5% |
| FY2025 | +23.2% | +53.2% |
| FY2026 | +36.8% | +46.6% |


The same graph in two other formats sits beside this file: [`JAINREC_stock_to_index.svg`](JAINREC_stock_to_index.svg) — a vector chart that opens in any browser — and [`JAINREC_stock_to_index.mmd`](JAINREC_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


## 5. The raw yearly values behind every ratio

Company prices in rupees; profits in Rs crore. The index close is the March close unless the company closes its books in another month (shown in brackets). '—' = not in the stored data.

| Fiscal year | Company price (Rs) | Nifty 50 close | Company PAT (Rs cr) | Index PAT (Rs cr) | Company OP (Rs cr) | Index OP (Rs cr) |
|---|---|---|---|---|---|---|
| FY2015 | — | — | — | 239,976 | — | 362,356 |
| FY2016 | — | — | — | 252,916 | — | 381,103 |
| FY2017 | — | — | — | 268,287 | — | 384,170 |
| FY2018 | — | — | — | 260,991 | — | 381,288 |
| FY2019 | — | — | — | 281,855 | — | 476,374 |
| FY2020 | — | — | — | 275,997 | — | 491,207 |
| FY2021 | — | — | — | 331,853 | — | 542,357 |
| FY2022 | — | — | — | 495,232 | — | 730,487 |
| FY2023 | — | — | 92 | 574,328 | 127 | 890,079 |
| FY2024 | — | — | 164 | 721,343 | 231 | 1,008,599 |
| FY2025 | — | — | 223 | 796,066 | 375 | 1,068,504 |
| FY2026 | 456.50 | 23,997.55 | 347 | 905,734 | 558 | 1,084,854 |


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
