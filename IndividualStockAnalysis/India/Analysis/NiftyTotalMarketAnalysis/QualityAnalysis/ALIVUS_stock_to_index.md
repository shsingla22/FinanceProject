# Alivus Life Sciences (ALIVUS) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: GAINED on the index: the ratio rose +53% from FY2019 to FY2021.**

```
FY2019  ████████████████           0.070%
FY2020  ██████████████████████████ 0.113%  ▲ +63.1% vs prior year
FY2021  ████████████████████████   0.106%  ▼ -6.5% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2006 | FY2021 | n/a — data starts FY2019 |
| last 10 years | FY2011 | FY2021 | n/a — data starts FY2019 |
| last 5 years | FY2016 | FY2021 | n/a — data starts FY2019 |
| last 3 years | FY2018 | FY2021 | n/a — data starts FY2019 |
| last 1 year | FY2020 | FY2021 | -6% |


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: GAINED on the index: the ratio rose +109% from FY2019 to FY2021.**

```
FY2019  ████████████               0.052%
FY2020  ███████████████████████    0.096%  ▲ +84.6% vs prior year
FY2021  ██████████████████████████ 0.109%  ▲ +13.4% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2006 | FY2021 | n/a — data starts FY2019 |
| last 10 years | FY2011 | FY2021 | n/a — data starts FY2019 |
| last 5 years | FY2016 | FY2021 | n/a — data starts FY2019 |
| last 3 years | FY2018 | FY2021 | n/a — data starts FY2019 |
| last 1 year | FY2020 | FY2021 | +13% |


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

   +92% ┤
        │■╗
        │ ╚╗
        │  ╚╗
   +65% ┤◆┓ ╚╗
        │ ┗┓ ║
        │  ┗┓╚╗
   +39% ┤   ┗┓╚╗
        │    ┗┓╚╗
        │     ┃ ╚╗
   +13% ┤     ┗┓ ■
        │      ┗┓
        │┈┈┈┈┈┈┈┗┓┈┈
        │        ◆
   -14% ┤
        └┬───────┬──
       FY20    FY21

◆      +63.1   -6.5
■      +84.6   +13.4

◆ PAT ratio   ■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

Each line again on its own, for a closer read:

```
PAT RATIO — yearly change against the Nifty 50 (%)

   +69% ┤
        │◆┓
        │ ┗┓
   +48% ┤  ┃
        │  ┗┓
        │   ┃
        │   ┗┓
   +28% ┤    ┗┓
        │     ┗┓
        │      ┃
    +8% ┤      ┗┓
        │       ┃
        │┈┈┈┈┈┈┈┗┓┈┈
        │        ◆
   -12% ┤
        └┬───────┬──
       FY20    FY21

◆      +63.1   -6.5

◆ PAT ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

```
OPERATING-PROFIT RATIO — yearly change against the Nifty 50 (%)

   +91% ┤
        │■╗
        │ ╚╗
        │  ║
   +67% ┤  ╚╗
        │   ╚╗
        │    ╚╗
   +42% ┤     ╚╗
        │      ╚╗
        │       ║
   +18% ┤       ╚╗
        │        ■
        │
        │┈┈┈┈┈┈┈┈┈┈┈
    -7% ┤
        └┬───────┬──
       FY20    FY21

■      +84.6   +13.4

■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```


**The value at every point of the graph** (also printed under each point above):

| Fiscal year | PAT ratio | Operating-profit ratio |
|---|---|---|
| FY2020 | +63.1% | +84.6% |
| FY2021 | -6.5% | +13.4% |


The same graph in two other formats sits beside this file: [`ALIVUS_stock_to_index.svg`](ALIVUS_stock_to_index.svg) — a vector chart that opens in any browser — and [`ALIVUS_stock_to_index.mmd`](ALIVUS_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


## 5. The raw yearly values behind every ratio

Company prices in rupees; profits in Rs crore. The index close is the March close unless the company closes its books in another month (shown in brackets). '—' = not in the stored data.

| Fiscal year | Company price (Rs) | Nifty 50 close | Company PAT (Rs cr) | Index PAT (Rs cr) | Company OP (Rs cr) | Index OP (Rs cr) |
|---|---|---|---|---|---|---|
| FY2015 | — | — | — | 239,976 | — | 362,356 |
| FY2016 | — | — | — | 252,916 | — | 381,103 |
| FY2017 | — | — | — | 268,287 | — | 384,170 |
| FY2018 | — | — | — | 260,991 | — | 381,288 |
| FY2019 | — | — | 196 | 281,855 | 248 | 476,374 |
| FY2020 | — | — | 313 | 275,997 | 472 | 491,207 |
| FY2021 | — | — | 352 | 331,853 | 591 | 542,357 |
| FY2022 | — | — | — | 495,232 | — | 730,487 |
| FY2023 | — | — | — | 574,328 | — | 890,079 |
| FY2024 | — | — | — | 721,343 | — | 1,008,599 |
| FY2025 | — | — | — | 796,066 | — | 1,068,504 |
| FY2026 | — | — | — | 905,734 | — | 1,084,854 |


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
