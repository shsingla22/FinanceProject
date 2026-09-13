"""
analyze.py — run the Darvas method end to end and write the report.

    python3 analyze.py run                      # fetch fresh data + report
    python3 analyze.py run --no-fetch           # reuse the stored fetch
    python3 analyze.py run --top 15             # deep-dive the top 15
    python3 analyze.py run --quick              # no AI call for step 2

THE RHYTHM (step 5): run this once a week, after Friday's close. Each run
re-fetches the data (a volume surge is only visible in current data),
re-ranks the universe, re-seals every pick's boxes and RE-COMPUTES every
held stop from the current box — ratcheting stops up, never down. The
ledger in the analysis folder carries the held positions between runs.

Output:
    Analysis/NiftyTotalMarketAnalysis/DarvasAnalysis/DARVAS_REPORT.md
    Analysis/NiftyTotalMarketAnalysis/DarvasAnalysis/_positions.csv
"""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import charts as CH          # noqa: E402
import darvas as DV          # noqa: E402
import earnings as EP        # noqa: E402
import fetch_data as FD      # noqa: E402

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "DarvasAnalysis"
REPORT = OUT_DIR / "DARVAS_REPORT.md"
LEDGER = OUT_DIR / "_positions.csv"

DEFAULT_TOP = 25


def _ai_available() -> bool:
    return shutil.which("claude") is not None


def deep_dive(sym: str, weekly, daily, signal, ai: bool) -> dict:
    box_state = DV.find_boxes(daily[sym])
    rec = DV.recommend(box_state, signal)
    rec["symbol"] = sym
    rec["last_close"] = box_state.get("last_close")
    power = EP.earnings_power(sym)
    calls = EP.new_age_verdict(sym, allow_ai=ai)
    months = DV.monthly_volumes(daily[sym])
    mtrend = DV.monthly_trend(months)
    # Darvas demanded earnings power under the volume: a surge on falling
    # earnings is not his trade — the action is downgraded, and says so.
    if rec["action"] in ("BUY", "ACCUMULATE") and power["verdict"] == "FALLING":
        rec["action"] = "WATCH"
        rec["why"] += ("; DOWNGRADED to WATCH — the latest statements show "
                       "falling earnings power, and Darvas required rising "
                       "earnings under the volume")
    return {"signal": signal, "box_state": box_state, "rec": rec,
            "power": power, "calls": calls,
            "months": months, "mtrend": mtrend}


# --------------------------------------------------------------- rendering

def _md_money(v) -> str:
    return "—" if v is None else f"₹{v:,.2f}"


def _power_table(p: dict) -> str:
    if not p.get("ebitda") and not p.get("pat"):
        return f"*{p['why']}.*"
    years = [y for y, _ in (p.get("pat") or p.get("ebitda"))]
    label = "Financing profit" if p.get("lender_lines") else "EBITDA"
    rows = {label: dict(p.get("ebitda") or []),
            f"{label} margin %": dict(p.get("ebitda_margin_pct") or []),
            "PAT": dict(p.get("pat") or []),
            "PAT margin %": dict(p.get("pat_margin_pct") or [])}
    out = ["| Measure | " + " | ".join(years) + " |",
           "|---|" + "---|" * len(years)]
    for name, by_year in rows.items():
        cells = [f"{by_year[y]:,.1f}" if y in by_year else "—"
                 for y in years]
        out.append(f"| {name} | " + " | ".join(cells) + " |")
    return "\n".join(out)


def render_report(scan, dives, meta) -> str:
    A = []
    q = [s for s in scan if s["qualifies"]]
    A.append("# The Darvas Screen — NiftyTotalMarket")
    A.append("")
    A.append(f"*Run {meta['run_date']} on data fetched "
             f"{meta['fetched_at']} · {meta['scanned']} stocks scanned "
             f"({meta['fetch_ok']} fetched, {meta['fetch_failed']} "
             f"unavailable) · trigger week beginning "
             f"{meta['trigger_week']}.*")
    A.append("")
    A.append("**The method, in one line:** a surge in weekly volume with "
             "the price appreciating is the trigger; rising earnings power "
             "(ideally in a new-age industry) is the confirmation; the "
             "stock's own boxes give the buy point, the add point and the "
             "stop; a drop to a lower box is the exit.")
    A.append("")

    # ---- step 1
    A.append("## Step 1 — The volume trigger")
    A.append("")
    A.append(f"A stock qualifies when its LATEST week — the running "
             f"(partial) week when there is one, pro-rated to five days — "
             f"traded at least {DV.QUALIFY_MULTIPLE}× its average weekly "
             f"volume of the prior {DV.BASELINE_WEEKS} completed weeks AND "
             f"the price rose. {len(q)} of {meta['scanned']} qualified; "
             f"every qualifier, best volume reaction first, with the last "
             f"four weeks of volume shown:")
    A.append("")
    A.append("| # | Stock | Vol W−3 | Vol W−2 | Vol W−1 | Vol latest wk | "
             "12-wk avg | Multiple | Price latest wk | Close |")
    A.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for i, s in enumerate(q, 1):
        rw = s.get("recent_weeks", [])
        cells = ["—"] * (4 - len(rw)) + [f"{w['volume']:,}" for w in rw]
        star = "*" if s.get("partial_week") else ""
        A.append(f"| {i} | {s['symbol']} | {cells[0]} | {cells[1]} | "
                 f"{cells[2]} | {cells[3]}{star} | "
                 f"{s['baseline_avg_volume']:,} | "
                 f"**{s['volume_multiple']:.2f}×**{star} | "
                 f"{s['price_change_pct']:+.2f}% | ₹{s['close']:,.1f} |")
    A.append("")
    if any(s.get("partial_week") for s in q):
        A.append("\* the latest week is still running — its multiple is "
                 "pro-rated to a full five-day week (volume ÷ (average × "
                 "days traded ÷ 5)); the raw volume shown is what has "
                 "actually traded so far.")
        A.append("")
    A.append(f"The top {len(dives)} go on to the earnings and box steps "
             f"below.")
    A.append("")

    # ---- summary of recommendations
    A.append("## The recommendations")
    A.append("")
    A.append("| Stock | Action | Box (₹) | Own box height | Stop loss | "
             "Volume trend | Earnings power | New-age |")
    A.append("|---|---|---|---:|---:|---|---|---|")
    for d in dives:
        r, p, c = d["rec"], d["power"], d["calls"]
        mt = d["mtrend"]["verdict"]
        if d["mtrend"].get("rising_months", 0) >= 2:
            mt += f" ({d['mtrend']['rising_months']} mo)"
        box = (f"{r['box_bottom']:,.1f}–{r['box_top']:,.1f}"
               if r.get("box_top") else "forming")
        rng = (f"{r['box_range_pct']:.1f}%" if r.get("box_range_pct")
               else "—")
        stop = _md_money(r.get("stop_loss")) if r["action"] != "SELL" \
            else "exit"
        A.append(f"| {r['symbol']} | **{r['action']}** | {box} | {rng} | "
                 f"{stop} | {mt} | {p['verdict']} | "
                 f"{c.get('new_age', '—')} |")
    A.append("")

    # ---- per-stock deep dives
    for d in dives:
        s, r, p, c = d["signal"], d["rec"], d["power"], d["calls"]
        sym = r["symbol"]
        A.append(f"## {sym} — {r['action']}")
        A.append("")
        A.append(f"**Why:** {r['why']}.")
        A.append("")
        part = (f" in {s['days_traded']} trading day"
                f"{'s' if s['days_traded'] > 1 else ''} of a week still "
                f"running — {s['raw_volume_multiple']:.2f}× the weekly "
                f"average already, {s['volume_multiple']:.2f}× pro-rated "
                f"to five days" if s.get("partial_week") else
                f" — **{s['volume_multiple']:.2f}× normal**")
        A.append(f"**The trigger numbers:** {s['last_week_volume']:,} "
                 f"shares traded in the week of {s['week_start']} against "
                 f"a {s['baseline_weeks']}-week average of "
                 f"{s['baseline_avg_volume']:,}{part} "
                 f"({s['tier'] or 'below tier'}), with the price "
                 f"{s['price_change_pct']:+.2f}% on the week.")
        A.append("")
        A.append("### Price and volume together, week by week")
        A.append("")
        A.append(CH.price_volume_chart(d["weekly_rows"]))
        A.append("")
        A.append("### Is the volume building, or a one-week event?")
        A.append("")
        A.append(f"**{d['mtrend']['verdict']}** — {d['mtrend']['why']}.")
        A.append("")
        A.append(CH.monthly_volume_table(d["months"]))
        A.append("")
        A.append("### The boxes")
        A.append("")
        A.append(CH.box_picture(d["box_state"], r))
        A.append("")
        if r.get("box_range_pct"):
            A.append(f"This stock's own box height is "
                     f"**{r['box_range_pct']:.1f}%** — box edges are taken "
                     f"from its actual highs and lows (an edge stands only "
                     f"after {DV.CONFIRM_DAYS} sessions fail to better it), "
                     f"never from a fixed percentage.")
            A.append("")
        A.append("### Earnings power (step 2)")
        A.append("")
        A.append(f"**{p['verdict']}** — {p['why']}.")
        A.append("")
        A.append(_power_table(p))
        A.append("")
        na = c.get("new_age", "not assessed")
        if c.get("status") == "with_calls":
            A.append(f"**New-age industry:** {na}"
                     + (f" ({c.get('theme')})" if c.get("theme") else "")
                     + (f" — {c.get('rationale')}" if c.get("rationale")
                        else ""))
            if c.get("quote"):
                A.append(f"> \"{c['quote']}\"")
        else:
            A.append(f"**New-age industry:** not assessed "
                     f"({c.get('status', 'no evidence')}) — stated "
                     f"honestly rather than guessed.")
        A.append("")

    # ---- the ledger
    A.append("## The stop-loss ledger")
    A.append("")
    A.append("Positions carried between runs. The rhythm: this skill runs "
             "weekly after Friday's close; every held stop is recomputed "
             "from the stock's CURRENT box (stop = box bottom − 0.3 × box "
             "height) and only ever moves UP — a stock seals a higher box "
             "only after three quiet sessions on each edge, so the ratchet "
             "is decisive by construction. A SELL row means the stock "
             "closed below its box bottom — the red flag.")
    A.append("")
    A.append("| Stock | First flagged | Action | Box (₹) | Stop | Updated |")
    A.append("|---|---|---|---|---:|---|")
    for row in meta["ledger"]:
        box = (f"{float(row['box_bottom']):,.1f}–"
               f"{float(row['box_top']):,.1f}"
               if row.get("box_top") not in ("", None) else "—")
        stop = (f"₹{float(row['stop_loss']):,.2f}"
                if row.get("stop_loss") not in ("", None) else "exit")
        A.append(f"| {row['symbol']} | {row['first_flagged']} | "
                 f"{row['action']} | {box} | {stop} | {row['updated']} |")
    A.append("")

    A.append("## How this screen was built")
    A.append("")
    A.append(f"- **Data:** daily bars for the last six months for every "
             f"NiftyTotalMarket symbol, fetched fresh THIS run "
             f"({meta['fetched_at']}) from Yahoo Finance into "
             f"`IndividualStockAnalysis/India/VolumeAndPricing/"
             f"{FD.UNIVERSE}/`, aggregated into completed Monday-Friday "
             f"weeks. {meta['fetch_failed']} symbols were unavailable and "
             f"are listed in `_fetch_log.csv`, never silently skipped.")
    A.append(f"- **Trigger:** last completed week's volume ÷ mean of up "
             f"to {DV.BASELINE_WEEKS} prior completed weeks (minimum "
             f"{DV.MIN_BASELINE_WEEKS}); qualification needs ≥"
             f"{DV.QUALIFY_MULTIPLE}× AND a positive week. Tiers: ≥3× "
             f"multifold, ≥2× strong, ≥1.5× elevated.")
    A.append(f"- **Boxes:** Darvas's own rule — a top stands after "
             f"{DV.CONFIRM_DAYS} sessions fail to exceed it, then a bottom "
             f"stands after {DV.CONFIRM_DAYS} sessions fail to undercut "
             f"it; a close above the top reaches for the higher box, a "
             f"close below the bottom is the red flag.")
    A.append(f"- **Stops:** bottom − {DV.STOP_FRACTION} × box height, "
             f"ratcheted up only (a 50–55 box stops near 48.5, a 70–85 "
             f"box near 65.5 — the worked examples of the method).")
    A.append("- **Volume trend:** month-wise totals from the same daily "
             "bars; BUILDING = volume rose month over month for at least "
             "the last two complete months; the running month is shown "
             "but never argued from.")
    A.append("- **Earnings power:** EBITDA, EBITDA margin, PAT and PAT "
             "margin from the stored statements; the new-age read comes "
             "from the conference calls via the judge model and is "
             "cached per transcript. Anything unassessable is marked, "
             "never guessed.")
    A.append("- Research tooling — not investment advice.")
    A.append("")
    return "\n".join(A)


# --------------------------------------------------------------------- CLI

def cmd_run(args) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if args.no_fetch and (FD.OUT_DIR / "_all_weekly_long.csv").exists():
        print("using the stored fetch (--no-fetch)", file=sys.stderr)
    else:
        print("fetching fresh volume + price data for the universe…",
              file=sys.stderr)
        summary = FD.fetch_universe()
        print(f"fetched {summary['ok']} ok, {summary['failed']} failed "
              f"in {summary['seconds']}s", file=sys.stderr)

    weekly = DV.load_weekly()
    scan = DV.scan_universe(weekly)
    q = [s for s in scan if s["qualifies"]]
    top = q[:args.top]
    print(f"{len(q)} qualifiers; deep-diving the top {len(top)}",
          file=sys.stderr)

    daily = DV.load_daily()
    ai = _ai_available() and not args.quick
    dives = []
    for s in top:
        d = deep_dive(s["symbol"], weekly, daily, s, ai)
        d["weekly_rows"] = weekly[s["symbol"]]
        dives.append(d)
        print(f"  {s['symbol']}: {d['rec']['action']} "
              f"({s['volume_multiple']:.2f}×)", file=sys.stderr)

    ledger = DV.update_ledger(
        LEDGER, [{**d["rec"]} for d in dives])
    fetched_at = (FD.OUT_DIR / "_fetched_at.txt").read_text().strip() \
        if (FD.OUT_DIR / "_fetched_at.txt").exists() else "unknown"
    log_rows = list((FD.OUT_DIR / "_fetch_log.csv").read_text()
                    .splitlines())[1:]
    failed = sum(1 for r in log_rows if ",failed," in r)
    meta = {
        "run_date": dt.date.today().isoformat(),
        "fetched_at": fetched_at,
        "scanned": len(scan),
        "fetch_ok": len(log_rows) - failed,
        "fetch_failed": failed,
        "trigger_week": top[0]["week_start"] if top else "—",
        "ledger": ledger,
    }
    md = render_report(scan, dives, meta)
    REPORT.write_text(md)
    print(f"wrote {REPORT} ({len(md.splitlines())} lines)")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--top", type=int, default=DEFAULT_TOP,
                   help="how many qualifiers get the full deep dive")
    r.add_argument("--no-fetch", action="store_true",
                   help="reuse the stored fetch instead of refetching")
    r.add_argument("--quick", action="store_true",
                   help="skip the AI call-read for step 2")
    args = ap.parse_args()
    {"run": cmd_run}[args.cmd](args)


if __name__ == "__main__":
    main()
