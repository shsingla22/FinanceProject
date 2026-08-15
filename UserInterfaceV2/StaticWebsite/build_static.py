"""
build_static.py — generate the GitHub Pages build of the Investment
Company website into ./site, from the SAME sources the live UI serves:

  frontend        ../index.html + ../app.js + ../style.css copied as-is
                  (index gets window.STATIC_MODE=true injected) — one UI,
                  two backends, so UI improvements flow to both versions
  data/           companies.json, ranking.json, charts/{SYM}.json —
                  produced by the live server's OWN functions (imported),
                  so the two versions can never disagree
  reports/        the stored {SYM}_analysis.md / {SYM}_comparison.md

Re-run after any report refresh (or let the GitHub Actions workflow in
.github/workflows/pages.yml do it automatically on every push):

    python3 UserInterfaceV2/StaticWebsite/build_static.py
"""

from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path

os.environ.setdefault("UI_DISABLE_AI", "1")

HERE = Path(__file__).resolve().parent            # UserInterfaceV2/StaticWebsite
UIV2 = HERE.parent
sys.path.insert(0, str(UIV2))

import server as S                                # noqa: E402  (the live UI)

SITE = HERE / "site"


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "data" / "charts").mkdir(parents=True)
    (SITE / "reports").mkdir(parents=True)

    syms = S.analysed_symbols()

    # inventory — exactly what /api/companies serves
    (SITE / "data" / "companies.json").write_text(json.dumps(S.companies()))

    # full ranking, enriched like /api/ranking rows (client slices best/worst)
    live = S._live_map()
    rows = []
    for r in S._ranking_rows():
        lv = live.get(r["symbol"], {})
        rows.append({**r,
                     "industry": S._const_map.get(r["symbol"], {}).get("industry", ""),
                     "mcap": S._clean(lv.get("market_cap_rs_cr")),
                     "pe": S._clean(lv.get("stock_pe"))})
    (SITE / "data" / "ranking.json").write_text(json.dumps(rows))

    # per-company: chart series (server logic) + the stored reports
    for sym in syms:
        data = S._charts_for(sym)
        charts = [dict(m) for m in S.CHART_META
                  if sum(v is not None for v in data["series"].get(m["key"], [])) >= 3]
        (SITE / "data" / "charts" / f"{sym}.json").write_text(
            json.dumps({**data, "charts": charts}))
        a, c = S._report_paths(sym)
        shutil.copy2(a, SITE / "reports" / a.name)
        shutil.copy2(c, SITE / "reports" / c.name)

    # the one shared frontend, flagged into static mode
    shutil.copy2(UIV2 / "style.css", SITE / "style.css")
    shutil.copy2(UIV2 / "app.js", SITE / "app.js")
    html = (UIV2 / "index.html").read_text().replace(
        '<script src="app.js"></script>',
        '<script>window.STATIC_MODE = true;</script>\n<script src="app.js"></script>')
    assert "STATIC_MODE" in html, "index.html no longer references app.js?"
    (SITE / "index.html").write_text(html)
    (SITE / ".nojekyll").write_text("")            # serve files starting with _

    n_files = sum(1 for _ in SITE.rglob("*") if _.is_file())
    print(f"site built: {len(syms)} companies, {len(rows)} ranked, "
          f"{n_files} files -> {SITE}")


if __name__ == "__main__":
    main()
