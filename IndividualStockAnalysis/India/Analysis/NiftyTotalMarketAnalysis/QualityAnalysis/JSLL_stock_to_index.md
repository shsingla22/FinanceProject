# Jeena Sikho Life (JSLL) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: GAINED on the index: the ratio rose +1003% from FY2022 to FY2026.**

```
FY2022  ██                         0.002%
FY2023  ██████                     0.006%  ▲ +166.5% vs prior year
FY2025  ███████████                0.010%  ▲ +69.8% vs prior year
FY2026  ██████████████████████████ 0.025%  ▲ +143.9% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2022 |
| last 10 years | FY2016 | FY2026 | n/a — data starts FY2022 |
| last 5 years | FY2021 | FY2026 | n/a — data starts FY2022 |
| last 3 years | FY2023 | FY2026 | +314% |
| last 1 year | FY2025 | FY2026 | +144% |


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: GAINED on the index: the ratio rose +1206% from FY2022 to FY2026.**

```
FY2022  ██                         0.002%
FY2023  ████                       0.005%  ▲ +109.7% vs prior year
FY2025  ███████████                0.013%  ▲ +155.3% vs prior year
FY2026  ██████████████████████████ 0.032%  ▲ +143.8% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2022 |
| last 10 years | FY2016 | FY2026 | n/a — data starts FY2022 |
| last 5 years | FY2021 | FY2026 | n/a — data starts FY2022 |
| last 3 years | FY2023 | FY2026 | +522% |
| last 1 year | FY2025 | FY2026 | +144% |


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

  +180% ┤
        │◆━┓
        │  ┗━━━━┓
  +132% ┤       ╔■
        │  ╔════╝
        │■═╝
        │
   +83% ┤
        │
        │
   +35% ┤
        │
        │
        │┈┈┈┈┈┈┈┈┈┈┈
   -13% ┤
        └┬───────┬──
       FY23    FY26

◆     +166.5  +143.9
■     +109.7  +143.8

◆ PAT ratio   ■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

Each line again on its own, for a closer read:

```
PAT RATIO — yearly change against the Nifty 50 (%)

  +180% ┤
        │◆━┓
        │  ┗━━━━┓
  +132% ┤       ┗◆
        │
        │
        │
   +83% ┤
        │
        │
   +35% ┤
        │
        │
        │┈┈┈┈┈┈┈┈┈┈┈
   -13% ┤
        └┬───────┬──
       FY23    FY26

◆     +166.5  +143.9

◆ PAT ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

```
OPERATING-PROFIT RATIO — yearly change against the Nifty 50 (%)

  +155% ┤
        │       ╔■
        │    ╔══╝
        │  ╔═╝
  +114% ┤■═╝
        │
        │
   +72% ┤
        │
        │
   +30% ┤
        │
        │
        │┈┈┈┈┈┈┈┈┈┈┈
   -12% ┤
        └┬───────┬──
       FY23    FY26

■     +109.7  +143.8

■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```


**The value at every point of the graph** (also printed under each point above):

| Fiscal year | PAT ratio | Operating-profit ratio |
|---|---|---|
| FY2023 | +166.5% | +109.7% |
| FY2026 | +143.9% | +143.8% |


The same graph in two other formats sits beside this file: [`JSLL_stock_to_index.svg`](JSLL_stock_to_index.svg) — a vector chart that opens in any browser — and [`JSLL_stock_to_index.mmd`](JSLL_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


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
| FY2022 | — | — | 11 | 495,232 | 18 | 730,487 |
| FY2023 | — | — | 34 | 574,328 | 46 | 890,079 |
| FY2024 | — | — | — | 721,343 | — | 1,008,599 |
| FY2025 | — | — | 80 | 796,066 | 141 | 1,068,504 |
| FY2026 | — | — | 222 | 905,734 | 349 | 1,084,854 |


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
