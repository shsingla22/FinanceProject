# Business Quality Analyst — User Interface

A web UI where you ask questions in **natural language** ("analyse DIXON",
"best 10 companies", "compare TITAN and DMART", "working capital of IXIGO")
and get the **complete business-quality analysis** back — quantitative AND
qualitative — for all **742 Nifty Total Market companies**.

Every analysis runs the **`Skills/BusinessAnalysis`** skill live on the server:

1. **Quantitative module** — signals recomputed at request time from the
   repository's balance sheets, P&L, cash flow, working capital, live market
   data and management history.
2. **Qualitative module** — the skill's playbook runs over the company's
   latest conference-call transcript via Claude (your subscription through the
   Claude Code CLI, or an API key). Scores are fused with the quantitative
   ones per the skill's hybrid rule and **cached per transcript**, so each
   company's call is analysed once (~30–60s), then instant.

Parameters the call is silent on stay *not assessed* — coverage is reported
honestly next to every score, and every qualitative score carries a verbatim
quote from the call.

## Run it (GitHub Codespaces)

1. Repo page → **Code → Codespaces → Create codespace** on this branch
   (the devcontainer installs Python deps + the Claude Code CLI).
2. Authenticate Claude with your subscription (once per codespace):
   ```bash
   claude        # follow the login link, then Ctrl+C
   ```
3. Start the site:
   ```bash
   cd UserInterface && uvicorn server:app --host 0.0.0.0 --port 8000
   ```
4. Click **"Open in Browser"** (or Ports tab → globe on port 8000).

The banner should read **"⚡ Live analysis … via your Claude subscription"**.

> **Keep port 8000 private** when using subscription-backed AI — your Max
> plan must serve only you, not visitors to a shared URL. (With an
> `ANTHROPIC_API_KEY` instead, sharing is fine — you pay per call.)

Local machine: same two commands after `pip install -r requirements.txt`
(and `npm i -g @anthropic-ai/claude-code` for subscription AI).

## What you can ask

| You type | You get |
|---|---|
| `analyse DIXON` / `tell me about asian paints` / any company name | complete scorecard: quant + concall-fused scores, per-parameter rationale **with quotes**, sales/OPM/CCC trends, management, concall extract |
| `best 10 companies` / `top 5 by growth` / `worst 10 by working capital` | coverage-guarded rankings; click a row to run the full analysis |
| `select good businesses in PHARMA` | industry-filtered picks |
| `compare TITAN and DMART` | side-by-side module scorecards |
| `working capital of IXIGO` / `margins of INFY` | topic deep-dive |
| `explain the framework` / `help` | methodology / usage |

## API endpoints (the UI uses these; so can your agents)

| Endpoint | What it does |
|---|---|
| `GET /api/health` | mode, AI backend (`claude_code_cli` / `api` / null) |
| `GET /api/companies` | all 742 quant records — recomputed when CSVs change (warmed at startup) |
| `GET /api/company/{sym}` | **the complete analysis**: fresh quant + cached-or-live AI qualitative fusion (`?quick=1` skips AI) |
| `GET /api/concall/{sym}` | transcript text extracted on demand |
| `POST /api/qualitative/{sym}` | raw AI concall scores only |
| `POST /api/refresh` | drop caches after refreshing the CSVs |

## Files

| File | Purpose |
|---|---|
| `server.py` | FastAPI backend — live skill execution, concall extraction, AI fusion, caching |
| `build_data.py` | shared scoring library (imported by the server) |
| `index.html` / `app.js` / `style.css` | frontend: NL intent parsing + rendering (no build step, no dependencies) |
| `.qual_cache.json` | on-disk cache of AI concall scores (gitignored; keyed by transcript mtime) |

## Notes

- First page load on a cold server computes all 742 companies (~30–60s); the
  UI shows a warm-up status and queues your first question. The cache
  invalidates automatically when the underlying CSVs change.
- Subscription AI calls share your Claude Code usage limits — fine for
  interactive use; don't batch-run all 742.
- Research tooling over screener.in-derived data; not investment advice.
