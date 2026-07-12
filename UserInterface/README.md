# Business Quality Analyst — User Interface

A static, dependency-free web UI where you ask questions in **natural language**
("analyse DIXON", "best 10 companies", "compare TITAN and DMART", "working
capital of IXIGO") and get explainable business-quality analysis back.

Behind the scenes it runs the **`Skills/BusinessAnalysis`** skill — the
34-parameter quality-investing framework — over the repository's dataset
(balance sheets, P&L, cash flow, working capital, live market data, management
history, concall availability) for all **742 Nifty Total Market companies**.

## How it works

```
IndividualStockAnalysis/India/            UserInterface/
  BalanceSheet / ProfitStatement /   →    build_data.py  (runs the skill's quant
  CashFlow / WorkingCapital /             engine + scoring at BUILD time)
  StockInfo / ManagementInfo /                 ↓
  ConferenceCalls                         data/companies.json  (742 records, ~1 MB)
  Skills/BusinessAnalysis  ───────────→   data/framework.json  (34 parameters)
                                               ↓
                                          index.html + app.js  (static site:
                                          NL intent parsing + rendering only)
```

GitHub Pages hosts static files only, so all skill computation happens at build
time in `build_data.py`; the browser parses your question (company detection,
intent, topic) and renders the precomputed, evidence-backed scores.

**Honesty by design:** only ~7 of the 34 parameters are computable from the
financial statements alone. The other 27 require qualitative judgement over
concalls/annual reports (the skill's qualitative playbook), which a static site
cannot run — so every score is shown **with its coverage**, and unassessed
parameters are listed explicitly, never guessed.

## Two modes

| | **Dynamic (recommended)** | Static |
|---|---|---|
| What runs | `server.py` (FastAPI) executes the skill **live per request** | precomputed `data/*.json` snapshot |
| Freshness | edit a CSV → `POST /api/refresh` → answers change | frozen until `build_data.py` re-run |
| Concall text | extracted from the PDFs **on demand** | not available |
| AI qualitative scoring | ✅ with `ANTHROPIC_API_KEY` (Claude runs the playbook over the concall) | ❌ |
| Hosting | GitHub **Codespaces** / any Python host | GitHub **Pages** |

The same frontend serves both: `app.js` probes `/api/health` at load — if the
server is there it switches to live endpoints, otherwise it falls back to the
static JSON.

## Dynamic hosting via GitHub Codespaces (runs the skill live)

1. On the repo page: **Code → Codespaces → Create codespace** on this branch
   (the `.devcontainer/` config installs everything automatically).
2. In the codespace terminal:
   ```bash
   cd UserInterface && uvicorn server:app --host 0.0.0.0 --port 8000
   ```
3. Codespaces auto-forwards port 8000 and opens the browser — you're live.
   Make the port **Public** (right-click the port → Port Visibility) to share
   the URL with others.
4. Optional AI mode — two ways to enable the "🤖 Run AI qualitative analysis"
   button (scores the 30 text-based parameters live from the concall):

   | | **A. Claude subscription (Pro/Max)** | B. API key |
   |---|---|---|
   | Setup | `claude` in the terminal once → follow the login link | `export ANTHROPIC_API_KEY=sk-ant-...` |
   | Billing | included in your subscription | pay-as-you-go credits |
   | How it runs | server shells out to headless `claude -p` | direct Claude API call |
   | Sharing the URL | **❌ keep the port private** — your subscription must not serve third parties | ok (you pay per call) |

   The devcontainer pre-installs the Claude Code CLI, so for (A) you only run
   `claude` once to authenticate, then start the server — `/api/health` will
   show `"ai_backend": "claude_code_cli"`. The server prefers the API key if
   both are present.

Dynamic locally is the same two commands. Other dynamic hosts that work
unchanged: Render / Railway / Fly.io / Hugging Face Spaces (Docker) — start
command `uvicorn server:app --host 0.0.0.0 --port $PORT` from `UserInterface/`.

### Dynamic API endpoints

| Endpoint | What it does |
|---|---|
| `GET /api/health` | mode, framework version, whether AI is enabled |
| `GET /api/companies` | all 742 records — recomputed when CSVs change (mtime-stamped cache) |
| `GET /api/company/{sym}` | **one record recomputed fresh right now** + latest-concall excerpt |
| `GET /api/concall/{sym}` | transcript text extracted on demand from the merged PDF |
| `POST /api/qualitative/{sym}` | Claude scores the qualitative parameters from the call (needs API key) |
| `POST /api/refresh` | drop caches after refreshing the underlying CSVs |

## Static hosting on GitHub Pages (one-time setup)

1. Go to the repo's **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Push to this branch (or run the *"Deploy Business Analysis UI to GitHub
   Pages"* workflow manually from the **Actions** tab).
4. The site goes live at **`https://<owner>.github.io/FinanceProject/`**.

The workflow (`.github/workflows/deploy-pages.yml`) publishes the
`UserInterface/` folder on every push that touches it, on this branch or main.

## Running locally

```bash
cd UserInterface
python3 -m http.server 8000
# open http://localhost:8000
```

(A server is needed because the app fetches the JSON data files; opening
`index.html` directly via file:// will be blocked by CORS.)

## Refreshing the data

Whenever the underlying CSVs are refreshed (new fiscal year, new constituents):

```bash
python3 UserInterface/build_data.py   # re-runs the skill over all 742 cos
```

then commit the regenerated `data/*.json`.

## What you can ask

| You type | You get |
|---|---|
| `analyse DIXON` / `tell me about Titan` / just a company name | full explainable scorecard: overall + module scores, per-parameter rationale, sales/OPM/CCC trends, current management, concall count |
| `best 10 companies` / `top 5 by growth` / `worst 10 by working capital` | ranked table (score, coverage, mcap, P/E); click any row to drill in |
| `select good businesses in PHARMA` | industry-filtered ranking |
| `compare TITAN and DMART` | side-by-side module scorecards |
| `working capital of IXIGO` / `margins of INFY` / `management of HDFCBANK` | topic deep-dive for that company |
| `explain the framework` / `explain return on capital` | the methodology, parameter by parameter |

## Files

| File | Purpose |
|---|---|
| `index.html` / `style.css` / `app.js` | the static site (vanilla JS, no dependencies) |
| `build_data.py` | build-time generator — imports the skill's `quant_signals.py` + `scoring.py` |
| `data/companies.json` | precomputed per-company analysis records |
| `data/framework.json` | the 34-parameter taxonomy from the skill |

## Notes & limits

- Scores are **quantitative-only** (CROCI proxy, asset turns, margin level &
  stability, cash-conversion cycle, growth persistence, gross-margin proxy,
  pricing-rationality proxy). Qualitative parameters are surfaced with their
  judgement questions but not scored.
- Not investment advice; research tooling over screener.in-derived data.
