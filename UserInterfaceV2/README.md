# Company Analyst v2 — precomputed UX

The second version of the UX. **Same functionality as `UserInterface/`, but
instant**: instead of running the analysis skills live per request (minutes
for a first-time company), every view is served from the stored, validated
Markdown reports the batch analysis already produced in
`IndividualStockAnalysis/India/Analysis/NiftyTotalMarketAnalysis/QualityAnalysis/`
(`{SYM}_analysis.md` + `{SYM}_comparison.md` + `RANKING.md`/`_ranking.csv`).

## What it does

- **Analyse a company** — the full stored analyst report renders on the left
  (every check, pattern and risk with its why, foldable section by section)
  and the stored one-year then-vs-now comparison on the right. Both download
  buttons hand you the exact stored bytes — page and file can never disagree.
- **Best / worst lists with drill-down** — "top 20 companies", "worst 10",
  "best 15 in PHARMA" come from the stored ranking; click any row to open
  that company's full reports.
- **Compare** — "compare TITAN and DMART": stored verdicts side by side.
- **Charts** — the financial quantitative numbers (sales, net profit,
  margins, ROCE/ROE, EPS, operating & free cash flow, borrowings, reserves,
  cash-conversion cycle) render as SVG bar/line charts from the same
  statement CSVs the analyses judged.
- **Explainability & Q&A** — the reports carry their own explainability
  (exact rating arithmetic, per-check rationales, management quotes). The
  Q&A box answers questions **grounded only in the two stored reports**:
  via Claude when AI is available, or by quoting the most relevant report
  passages verbatim when it is not.

## Run it

```bash
cd UserInterfaceV2
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8001
# open http://localhost:8001
```

AI for the Q&A box (optional — everything else needs no AI):

- `ANTHROPIC_API_KEY=...` → answers via the Claude API, or
- a logged-in Claude Code CLI on PATH → answers via your own subscription
  (**personal use only — keep the forwarded port Private in Codespaces**), or
- neither / `UI_DISABLE_AI=1` → extract-from-report mode (still grounded).

## Endpoints

| Endpoint | What |
|---|---|
| `GET /api/health` | mode + how many companies have stored reports |
| `GET /api/companies` | every company: rating, grade, 1-yr direction, mcap/PE |
| `GET /api/analysis/{sym}` | stored analyst report (raw MD + section map) |
| `GET /api/comparison/{sym}` | stored then-vs-now report |
| `GET /api/report/{sym}` / `GET /api/comparison_report/{sym}` | MD downloads |
| `GET /api/ranking?n=20&order=best\|worst[&industry=]` | drill-down lists |
| `GET /api/charts/{sym}` | yearly financial series for the charts |
| `POST /api/ask/{sym}` | synchronous Q&A over the stored reports |
| `POST /api/jobs/ask/{sym}` + `GET /api/jobs/ask/{id}` | proxy-proof Q&A (the UI uses this) |

## Tests

```bash
cd UserInterfaceV2
UI_DISABLE_AI=1 python3 -m pytest test_v2_ui.py -q
```

The suite checks the endpoint contract, that served reports are
byte-identical to the stored files, ranking order/drill-down, chart/series
alignment, the grounded Q&A fallback, and sweeps **every** analysed company
through analysis + comparison + charts.
