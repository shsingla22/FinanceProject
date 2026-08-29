# StockToIndexPriceEarningsRatio skill

Compares one company against the **Nifty 50 index** on three measures,
one data point per fiscal year, up to the last 15 fiscal years:

1. **Price ratio** — company share price at its fiscal-year end ÷ the
   Nifty 50 close of the same month (shown ×1000 for readability).
2. **PAT ratio** — company Net Profit ÷ the summed Net Profit of the
   Nifty 50 constituents, as % of the index.
3. **Operating-profit ratio** — company Operating Profit (Financing
   Profit for lenders) ÷ the summed Operating Profit of the index, as %.

A **rising** ratio means the company outgrew the index on that measure;
a **falling** ratio means it lagged. Each chart carries a one-line
verdict (GAINED / LAGGED / MOVED WITH the index), year-by-year moves,
and a **window table** with the ratio's change over the last 15, 10, 5,
3 and 1 fiscal years (n/a rows state where the data starts instead of
guessing). A fourth section draws a **line graph inside the same Markdown file**:
all three ratios in one grid for comparison, then each ratio again on
its own for a closer read, with the value of every point printed under
its own column and repeated in a table. Series without enough points
are dropped and the legend says which lines remain. A fifth
section tables the **raw yearly values** every ratio is built from —
company price, Nifty 50 close, company and index PAT, company and index
operating profit. Years either side cannot cover are listed, never
guessed.

## Data

- **Company side** (stored, no network): share prices per fiscal year
  from `StockInfo/Nifty500/{SYM}.csv`; Net Profit and Operating Profit
  from `ProfitStatement/NiftyTotalMarket/_all_profit_loss_long.csv`.
- **Index side** (fetched once, saved under `data/`):
  - `nifty50_price_monthly.csv` / `nifty50_price_yearly.csv` — real
    ^NSEI closes (Yahoo Finance), 15 fiscal years of March closes
    (Mar 2012..Mar 2026) plus the monthly series so companies with
    Jun/Dec year-ends divide by the matching month.
  - `nifty50_constituents.csv` — current 50 constituents (screener.in
    mirror; the official NSE archive blocks scripts).
  - `nifty50_earnings_yearly.csv` — per fiscal year, the summed PAT and
    summed Operating Profit of the current constituents aggregated from
    the stored Nifty 500 statements (Mar 2015..Mar 2026). NSE publishes
    no such series, so this is the honest constructible one; it uses
    today's membership, so older years carry a survivorship caveat.

## Usage (from `scripts/`)

```bash
python3 fetch_index_data.py            # refresh the index series
python3 analyze.py report SYM out.md   # one company's report
python3 run_all.py                     # every company in the universe
python3 run_all.py --force             # rebuild even what already exists
python3 -m pytest test_skill.py -q     # the skill's test suite
```

`run_all.py` covers all 742 NiftyTotalMarket companies in about half a
minute — the skill reads only stored data, so there are no AI calls and
no network. It is resumable (a company whose files all exist is skipped)
and never aborts on one bad company; every outcome lands in
`_stock_to_index_log.csv`.

## Where the output goes

Beside each company's other stored analysis, in
`Analysis/NiftyTotalMarketAnalysis/QualityAnalysis/`:

| File | What it is |
|---|---|
| `{SYM}_stock_to_index.md` | the report — self-contained, text charts |
| `{SYM}_stock_to_index.svg` | the same line graph as a vector chart |
| `{SYM}_stock_to_index.mmd` | the same line graph as Mermaid source |

A company with fewer than two comparable fiscal years has no
year-on-year change to draw, so it gets the report and no chart files
rather than an empty chart.

## Known limits

- The stored statements span FY2015..FY2026, so the two earnings charts
  cover ~12 fiscal years even though the price chart covers 15.
- A company whose stored statements are stale (e.g. COLPAL's P&L stops
  at FY2010) gets a price chart plus an explicit "could not cover" list
  instead of guessed earnings ratios.

## Why the chart is drawn in text

Tested against GitHub's real Markdown renderer (a probe file pushed and
the rendered HTML read back), every inline image is stripped:

| Embedding | GitHub |
|---|---|
| `![](data:image/png;base64,...)` | removed |
| `<img src="data:image/png;base64,...">` | removed |
| `![](data:image/svg+xml;base64,...)` | removed |
| raw `<svg>...</svg>` | removed |
| ```mermaid `xychart-beta` | kept |
| `![](chart.png)` relative file | kept |

Mermaid survives on GitHub but does not render in every Markdown viewer,
and a relative image file is not self-contained. Box-drawing characters
render identically everywhere, so the chart is drawn with real strokes
(`linechart.py`): a light line with `●` points for the price ratio, a
heavy line with `◆` for PAT and a double line with `■` for operating
profit. Those pairings are pinned per measure, so `◆` means PAT in every
report even when another measure has no line to draw.


## Feeding the AnalystSkill

`analyst_interface.py` plugs this skill into the AnalystSkill through its
extensibility contract, contributing:

- a **pillar**, "Relative to the index", worth **10%** of the combined
  rating (`scripts/index_pillar.py` does the scoring),
- a **report section** with the verdict, the 10 / 5 / 3 / 1-year window
  table and the line graph,
- **facts** for the analyst's written summary.

Scoring, on the same −2..+2 scale the 34-check framework uses: a ratio
up 25%+ over the window scores +2, up 10–25% +1, within ±10% 0, down
10–25% −1, down 25%+ −2. Every measure × window pair the stored data can
answer is one cell; the pillar is their mean mapped onto 0–100, with
coverage reported. A ratio that crosses zero has no honest percentage
change, so that pair is left out rather than guessed.
