# Static website (GitHub Pages)

The GitHub Pages build of the Investment Company website — the same UI as
the live version one folder up, with all data pre-exported so it runs with
no server at all.

## How it stays in sync

- **One frontend**: `build_static.py` copies `../index.html`, `../app.js`
  and `../style.css` at build time (flagging `window.STATIC_MODE`), so any
  UI improvement automatically reaches both versions.
- **One data source**: the generator imports the live server's own
  functions to export `data/companies.json`, `data/ranking.json`,
  `data/charts/{SYM}.json` and copies the stored report files — the two
  versions can never disagree.
- **Auto-deploy**: `.github/workflows/pages.yml` rebuilds and republishes
  the site on every push to `main` that touches the reports, the data or
  the UI. No manual step.

## Build & preview locally

```bash
python3 UserInterfaceV2/StaticWebsite/build_static.py
cd UserInterfaceV2/StaticWebsite/site && python3 -m http.server 8002
# open http://localhost:8002
```

## One-time GitHub setup

1. Repo **Settings → Pages → Source: GitHub Actions**.
2. (Custom domain) Enter your domain in the same Pages settings, then add
   DNS at your registrar: CNAME `www` → `shsingla22.github.io`, and A
   records for the apex → 185.199.108.153 / .109.153 / .110.153 / .111.153.
   Tick **Enforce HTTPS**.

Differences from the live version: the Q&A box always answers by quoting
the most relevant report passages (no server = no AI call); everything
else — search, rankings, drill-down, verdicts, charts, downloads — is
identical.
