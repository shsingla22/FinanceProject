# Company Analyst — User Interface

A web UI where you ask questions in **natural language** ("analyse DIXON",
"rate CRISIL", "best 10 companies", "risks of TATASTEEL") and get the
**complete company analysis** back for all **742 Nifty Total Market
companies** — one explainable rating out of 100 built from three engines
that all run live on the server:

1. **Business quality (45%)** — the `Skills/BusinessAnalysis` 34-check
   framework: quantitative signals recomputed at request time, fused with
   the qualitative playbook over the company's conference-call history.
2. **Multibagger fit (30%)** — the `Skills/MultibaggerPattern` skill: which
   of the 11 patterns long-term winners share does it fit, and why.
3. **Risk safety (25%)** — the `Skills/QualityRisks` skill: which of the 8
   ways quality companies fail is it exposed to, at what severity.

The quality judge for all three engines is **Opus 5** (`claude-opus-5`),
via your Claude subscription (Claude Code CLI) or an API key. Judge
verdicts are **cached per transcript+model**, so a company's first
analysis takes several minutes (three deep reads of its call history) and
is instant afterwards. Every verdict states *why* it landed where it did;
anything the evidence can't answer stays *not assessed* — never guessed —
and every qualitative judgement carries a verbatim quote from the calls.

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
| `analyse DIXON` / `rate CRISIL` / any company name | the full workup: **rating card with point-by-point build-up**, quality scorecard with per-check rationale **and quotes**, the multibagger patterns it fits, the risk check with silver linings, trends, management, concall extract, downloadable report, and an "Ask about this analysis" box |
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
| `GET /api/company/{sym}` | quality-framework analysis only (`?quick=1` skips AI) |
| `GET /api/rating/{sym}` | **the complete analysis**: all three engines + the combined rating with full derivations (`?quick=1` = numbers only) |
| `GET /api/patterns/{sym}` | MultibaggerPattern record alone |
| `GET /api/risks/{sym}` | QualityRisks record alone |
| `GET /api/report/{sym}` | the downloadable Complete Company Analysis (Markdown) |
| `POST /api/ask/{sym}` | Q&A grounded in all three stored records + the rating |
| `GET /api/concall/{sym}` | transcript text extracted on demand |
| `POST /api/qualitative/{sym}` | raw AI concall scores only |
| `POST /api/refresh` | drop caches after refreshing the CSVs |

## Files

| File | Purpose |
|---|---|
| `server.py` | FastAPI backend — live skill execution, concall extraction, AI fusion, caching |
| `rating.py` | loads MultibaggerPattern + QualityRisks, computes the 3-pillar rating with derivations |
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
