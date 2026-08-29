# Anup Engineering (ANUP) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: LAGGED the index: the ratio fell -22% from FY2020 to FY2026.**

```
FY2020  █████████████████████████  0.016%
FY2021  ██████████████████████████ 0.016%  ▲ +4.4% vs prior year
FY2022  ████████████████████       0.013%  ▼ -23.1% vs prior year
FY2023  ██████████████             0.009%  ▼ -29.1% vs prior year
FY2025  ████████████████████████   0.015%  ▲ +66.9% vs prior year
FY2026  ███████████████████        0.012%  ▼ -18.1% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2020 |
| last 10 years | FY2016 | FY2026 | n/a — data starts FY2020 |
| last 5 years | FY2021 | FY2026 | -25% |
| last 3 years | FY2023 | FY2026 | +37% |
| last 1 year | FY2025 | FY2026 | -18% |


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: GAINED on the index: the ratio rose +13% from FY2020 to FY2026.**

```
FY2020  ███████████████████████    0.014%
FY2021  █████████████████████      0.013%  ▼ -9.4% vs prior year
FY2022  ████████████████           0.010%  ▼ -24.7% vs prior year
FY2023  ███████████████            0.009%  ▼ -2.9% vs prior year
FY2025  █████████████████████████  0.016%  ▲ +66.6% vs prior year
FY2026  ██████████████████████████ 0.016%  ▲ +2.0% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2020 |
| last 10 years | FY2016 | FY2026 | n/a — data starts FY2020 |
| last 5 years | FY2021 | FY2026 | +24% |
| last 3 years | FY2023 | FY2026 | +70% |
| last 1 year | FY2025 | FY2026 | +2% |


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

    +7% ┤
        │◆┓
        │ ┗┓                   ╔═■
        │┈┈┃┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╔══╝┈┈┈┈
    -3% ┤  ┗┓            ■══╝
        │   ┗┓          ╔╝
        │■╗  ┗┓        ╔╝
   -12% ┤ ╚═╗ ┗┓      ╔╝
        │   ╚═╗┗┓   ╔═╝
        │     ╚╗┃  ╔╝            ◆
   -22% ┤      ╚═╗╔╝          ┏━━┛
        │        ■╝┓         ┏┛
        │          ┗━━━━┓ ┏━━┛
        │               ┗◆┛
   -32% ┤
        └┬───────┬───────┬───────┬──
       FY21    FY22    FY23    FY26

◆      +4.4    -23.1   -29.1   -18.1
■      -9.4    -24.7   -2.9    +2.0

◆ PAT ratio   ■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

Each line again on its own, for a closer read:

```
PAT RATIO — yearly change against the Nifty 50 (%)

    +7% ┤
        │◆┓
        │ ┗┓
        │┈┈┃┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
    -3% ┤  ┗┓
        │   ┗┓
        │    ┗┓
   -12% ┤     ┗┓
        │      ┗┓
        │       ┃                ◆
   -22% ┤       ┗┓            ┏━━┛
        │        ◆━┓         ┏┛
        │          ┗━━━━┓ ┏━━┛
        │               ┗◆┛
   -32% ┤
        └┬───────┬───────┬───────┬──
       FY21    FY22    FY23    FY26

◆      +4.4    -23.1   -29.1   -18.1

◆ PAT ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

```
OPERATING-PROFIT RATIO — yearly change against the Nifty 50 (%)

    +4% ┤
        │                       ╔■
        │┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╔════╝┈┈┈
        │                ■═╝
    -4% ┤               ╔╝
        │               ║
        │■╗            ╔╝
   -11% ┤ ╚╗          ╔╝
        │  ╚╗        ╔╝
        │   ╚╗      ╔╝
        │    ╚═╗   ╔╝
   -19% ┤      ╚╗  ║
        │       ╚╗╔╝
        │        ■╝
   -27% ┤
        └┬───────┬───────┬───────┬──
       FY21    FY22    FY23    FY26

■      -9.4    -24.7   -2.9    +2.0

■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```


**The value at every point of the graph** (also printed under each point above):

| Fiscal year | PAT ratio | Operating-profit ratio |
|---|---|---|
| FY2021 | +4.4% | -9.4% |
| FY2022 | -23.1% | -24.7% |
| FY2023 | -29.1% | -2.9% |
| FY2026 | -18.1% | +2.0% |


The same graph in two other formats sits beside this file: [`ANUP_stock_to_index.svg`](ANUP_stock_to_index.svg) — a vector chart that opens in any browser — and [`ANUP_stock_to_index.mmd`](ANUP_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


## 5. The raw yearly values behind every ratio

Company prices in rupees; profits in Rs crore. The index close is the March close unless the company closes its books in another month (shown in brackets). '—' = not in the stored data.

| Fiscal year | Company price (Rs) | Nifty 50 close | Company PAT (Rs cr) | Index PAT (Rs cr) | Company OP (Rs cr) | Index OP (Rs cr) |
|---|---|---|---|---|---|---|
| FY2015 | — | — | — | 239,976 | — | 362,356 |
| FY2016 | — | — | — | 252,916 | — | 381,103 |
| FY2017 | — | — | — | 268,287 | — | 384,170 |
| FY2018 | — | — | — | 260,991 | — | 381,288 |
| FY2019 | — | — | — | 281,855 | — | 476,374 |
| FY2020 | — | — | 43 | 275,997 | 70 | 491,207 |
| FY2021 | — | — | 54 | 331,853 | 70 | 542,357 |
| FY2022 | — | — | 62 | 495,232 | 71 | 730,487 |
| FY2023 | — | — | 51 | 574,328 | 84 | 890,079 |
| FY2024 | — | — | — | 721,343 | — | 1,008,599 |
| FY2025 | — | — | 118 | 796,066 | 168 | 1,068,504 |
| FY2026 | — | — | 110 | 905,734 | 174 | 1,084,854 |


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
