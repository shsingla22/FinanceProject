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
import csv
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import charts as CH          # noqa: E402
import darvas as DV          # noqa: E402
import darvas_history as DH  # noqa: E402
import earnings as EP        # noqa: E402
import fetch_data as FD      # noqa: E402

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "DarvasAnalysis"
REPORT = OUT_DIR / "DARVAS_REPORT.md"
LEDGER = OUT_DIR / "_positions.csv"
LATEST = OUT_DIR / "darvas_latest.json"      # the run, machine-readable
LADDER_WATCH = OUT_DIR / "_ladder_watch.csv"  # surges awaiting a rising ladder
HISTORY = OUT_DIR / "history"                # one folder per run date

DEFAULT_TOP = 25


def _ai_available() -> bool:
    return shutil.which("claude") is not None


def deep_dive(sym: str, weekly, daily, signal, ai: bool) -> dict:
    box_state = DV.find_boxes(daily[sym])
    rec = DV.recommend(box_state, signal)
    rec["symbol"] = sym
    rec["last_close"] = box_state.get("last_close")
    pw = signal.get("promoted_from_watch")
    if pw:
        rec["promoted_from_watch"] = pw
        rec["why"] += (f"; PROMOTED from the ladder watch — it surged "
                       f"{float(pw['volume_multiple']):.2f}× in the week of "
                       f"{pw['surge_week']} but its ladder was not rising "
                       f"then; the boxes sealed since have made it rise")
    power = EP.earnings_power(sym)
    calls = EP.new_age_verdict(sym, allow_ai=ai)
    months = DV.monthly_volumes(daily[sym])
    mtrend = DV.monthly_trend(months)
    # Darvas demanded earnings power under the volume: a surge on falling
    # earnings is not his trade — the action is downgraded, and says so.
    if rec["action"] in ("BUY", "ACCUMULATE") and power["verdict"] == "FALLING":
        rec["action"] = "WATCH"
        rec["downgraded"] = True
        rec["why"] += ("; DOWNGRADED to WATCH — the latest statements show "
                       "falling earnings power, and Darvas required rising "
                       "earnings under the volume")
    return {"signal": signal, "box_state": box_state, "rec": rec,
            "power": power, "calls": calls,
            "months": months, "mtrend": mtrend}


WATCH_FIELDS = ["symbol", "surge_week", "watched_since", "expires",
                "volume_multiple", "month_multiple", "tier", "ladder_why",
                "last_checked", "status", "signal_json"]


def load_ladder_watch(path: Path = LADDER_WATCH) -> dict[str, dict]:
    if not path.exists():
        return {}
    with open(path) as fh:
        return {r["symbol"]: r for r in csv.DictReader(fh)}


def save_ladder_watch(rows: dict[str, dict], path: Path = LADDER_WATCH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=WATCH_FIELDS)
        w.writeheader()
        for sym in sorted(rows):
            w.writerow({k: rows[sym].get(k, "") for k in WATCH_FIELDS})


def ladder_watch_update(gated: list[dict], daily: dict, today: str,
                        path: Path = LADDER_WATCH,
                        days: int = DV.LADDER_WATCH_DAYS) -> dict:
    """The ladder watch, one run forward.

    STARTED: every stock that passed both volume gates today but failed
    the ladder joins the watch (a repeat surge restarts its month).
    Every stock already on the watch is re-judged from TODAY'S boxes:
    ladder rising and the boxes say BUY/ACCUMULATE → PROMOTED (it goes
    through the deep dive like any fully-qualified pick, carrying its
    ORIGINAL surge numbers); ladder rising but still in its box → kept,
    noted; broke down → DROPPED; past its month → EXPIRED. A stock that
    fully qualifies afresh today leaves the watch — it is a normal pick.
    Returns {"promoted": [signal…], "watching": [row…], "started",
    "expired", "dropped": [row…]} and rewrites the watch file."""
    rows = load_ladder_watch(path)
    fresh = {g["symbol"] for g in gated if g["fully_qualifies"]}
    out = {"promoted": [], "watching": [], "started": [], "expired": [],
           "dropped": []}
    started = set()
    for g in gated:
        mv, up = g.get("month_gate"), g.get("ladder_gate")
        if g["fully_qualifies"] or not mv or not mv["qualifies"] \
                or up["qualifies"]:
            continue
        sig = {k: v for k, v in g.items()
               if k not in ("month_gate", "ladder_gate", "fully_qualifies")}
        exp = (dt.date.fromisoformat(today)
               + dt.timedelta(days=days)).isoformat()
        rows[g["symbol"]] = {
            "symbol": g["symbol"], "surge_week": g["week_start"],
            "watched_since": today, "expires": exp,
            "volume_multiple": g["volume_multiple"],
            "month_multiple": mv["month_vs_year_multiple"],
            "tier": g.get("tier") or "", "ladder_why": up["why"],
            "last_checked": today, "status": "started — ladder not rising",
            "signal_json": json.dumps(sig, default=str)}
        started.add(g["symbol"])
        out["started"].append(rows[g["symbol"]])
    for sym in sorted(rows):
        r = rows[sym]
        if sym in started:
            out["watching"].append(r)
            continue
        if sym in fresh:                      # qualified afresh: a pick
            del rows[sym]
            continue
        if today > r["expires"]:
            r["status"] = f"expired {today} — no rising ladder in {days} days"
            out["expired"].append(r)
            del rows[sym]
            continue
        bars = daily.get(sym)
        if not bars:
            out["watching"].append(r)
            continue
        st = DV.find_boxes(bars)
        up = DV.box_uptrend(st["boxes"])
        r["last_checked"] = today
        r["ladder_why"] = up["why"]
        if not up["qualifies"]:
            r["status"] = "watching — ladder not rising yet"
            out["watching"].append(r)
            continue
        try:
            sig = json.loads(r.get("signal_json") or "{}")
        except json.JSONDecodeError:
            sig = {}
        sig.setdefault("symbol", sym)
        sig["qualifies"] = True
        sig["promoted_from_watch"] = {"surge_week": r["surge_week"],
                                      "watched_since": r["watched_since"],
                                      "volume_multiple": r["volume_multiple"]}
        rec = DV.recommend(st, sig)
        if rec["action"] in ("BUY", "ACCUMULATE") and "stop_loss" in rec:
            r["status"] = f"promoted {today} — ladder rising, {rec['action']}"
            out["promoted"].append(sig)
            del rows[sym]
        elif rec["action"] == "SELL" or st["state"] == "BREAKDOWN":
            r["status"] = f"dropped {today} — broke down while on watch"
            out["dropped"].append(r)
            del rows[sym]
        else:
            r["status"] = (f"watching — ladder rising, {rec['action']} "
                           f"(entry above ₹{rec.get('buy_above', 0):,.2f})"
                           if rec.get("buy_above") else
                           f"watching — ladder rising, {rec['action']}")
            out["watching"].append(r)
    save_ladder_watch(rows, path)
    return out


def carried_updates(ledger_path: Path, picked: set, daily: dict,
                    signals: dict | None = None) -> list[dict]:
    """The rhythm for EVERY held position, not only the re-flagged ones:
    each ledger symbol that is not among today's picks is re-judged
    from its CURRENT bars — a higher sealed box ratchets its stop up
    (update_ledger keeps max(old, new)), a close through the stop
    marks it SELL, and a breakdown still inside the grace stays WATCH
    with its stop standing. Rows already sold, or without bars, are
    left untouched."""
    if not ledger_path.exists():
        return []
    out = []
    with open(ledger_path) as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        sym = r["symbol"]
        if sym in picked or r.get("action") == "SELL":
            continue
        bars = daily.get(sym)
        if not bars:
            continue
        st = DV.find_boxes(bars)
        rec = DV.recommend(st, (signals or {}).get(sym, {}))
        if rec["action"] in ("BUY", "ACCUMULATE") \
                and r.get("action") not in ("BUY", "ACCUMULATE"):
            # a fresh entry needs the full three-gate screen — a watched
            # name that merely climbed out of its box is still only watched
            rec["action"] = "WATCH"
            rec["why"] += ("; stays WATCH — not re-qualified by this "
                           "week's volume screen")
        rec["symbol"] = sym
        rec["last_close"] = st.get("last_close")
        out.append(rec)
    return out


def detect_raised(old_stops: dict, ledger: list) -> list:
    """[(symbol, old, new)] for every held stop that moved UP this run."""
    out = []
    for row in ledger:
        new = row.get("stop_loss")
        old = old_stops.get(row["symbol"], "")
        try:
            if old and new and float(new) > float(old) + 1e-9:
                out.append((row["symbol"], float(old), float(new)))
        except ValueError:
            continue
    return out


def actions_data(dives: list, ledger: list, old_stops: dict,
                 today: str | None = None,
                 ladder_watch: dict | None = None) -> dict:
    """The week in FOUR verbs, as DATA — the single source both the
    report's closing section and the UIs render from, so they can never
    disagree. WATCH is the radar, not an instruction: a genuine in-box
    WATCH converts to BUY by ITSELF in a coming week if the breakout
    arrives on qualifying volume; a downgraded WATCH is a do-not-buy;
    unbought old signals expire. SELL lists only the rows that turned
    SELL in THIS run (`today`) — a stock sold last week is not sold
    again. A BUY whose ledger stop already stands higher (a holder's
    ratchet from an earlier box) carries that standing stop too."""
    buys, radar, downs = [], [], []
    standing = {}
    for row in ledger:
        try:
            standing[row["symbol"]] = float(row.get("stop_loss") or 0)
        except ValueError:
            pass
    for d in dives:
        r = d["rec"]
        if r["action"] in ("BUY", "ACCUMULATE"):
            risk = None
            if r.get("last_close") and r.get("stop_loss"):
                risk = round((r["stop_loss"] - r["last_close"])
                             / r["last_close"] * 100, 1)
            held = standing.get(r["symbol"])
            held = (held if held and r.get("stop_loss")
                    and held > r["stop_loss"] + 1e-9 else None)
            buys.append({"symbol": r["symbol"], "action": r["action"],
                         "entry": "buy at next open",
                         "stop_loss": r.get("stop_loss"),
                         "last_close": r.get("last_close"),
                         "risk_pct": risk,
                         "wide": risk is not None and risk < -25,
                         "held_stop": held})
        elif r.get("downgraded"):
            downs.append({"symbol": r["symbol"],
                          "why": "downgraded (falling earnings power): "
                                 "never a buy"})
        else:
            radar.append({"symbol": r["symbol"],
                          "buy_above": r.get("buy_above")})
    sells = [{"symbol": row["symbol"]} for row in ledger
             if row.get("action") == "SELL"
             and (today is None or row.get("updated") == today)]
    for r in (ladder_watch or {}).get("watching", []):
        radar.append({"symbol": r["symbol"], "buy_above": None,
                      "ladder_watch": f"on the ladder watch until "
                                      f"{r['expires']} — surged "
                                      f"{float(r['volume_multiple']):.2f}× "
                                      f"in the week of {r['surge_week']}; "
                                      f"{r.get('status', '')}"})
    raises = [{"symbol": s, "old": o, "new": n}
              for s, o, n in detect_raised(old_stops, ledger)]
    return {"buys": buys, "raises": raises, "sells": sells,
            "radar": radar, "downgraded": downs}


def render_actions(a: dict) -> str:
    A = ["", "---", "", "## Today's actions — plain and simple", ""]
    if a["buys"]:
        A += ["**BUY** (place the stop as a GTT order right after the "
              "fill; one equal slice each — a tenth of capital):", "",
              "| Stock | Entry | Stop loss |", "|---|---|---:|"]
        for b in a["buys"]:
            risk = ""
            if b["risk_pct"] is not None:
                risk = f" (risk {b['risk_pct']:+.1f}% from the last close"
                risk += (" — WIDE; consider a half slice or waiting for "
                         "the next box)" if b["wide"] else ")")
            if b.get("held_stop"):
                risk += (f"; already holding it? keep your standing "
                         f"₹{b['held_stop']:,.2f} — a stop never moves down")
            A.append(f"| **{b['symbol']}** | {b['entry']} | "
                     f"₹{b['stop_loss'] or 0:,.2f}{risk} |")
        A.append("")
    else:
        A += ["**BUY:** nothing today.", ""]
    if a["raises"]:
        A += ["**RAISE STOP LOSS** (replace the standing GTT — stops "
              "only ever move up; applies only if you hold it):", ""]
        A += [f"- {r['symbol']}: ₹{r['old']:,.2f} → **₹{r['new']:,.2f}**"
              for r in a["raises"]] + [""]
    else:
        A += ["**RAISE STOP LOSS:** none this run.", ""]
    if a["sells"]:
        A += ["**SELL** (closed below its box bottom — the red flag; "
              "applies only if you hold it):", ""]
        A += [f"- {s['symbol']}" for s in a["sells"]] + [""]
    else:
        A += ["**SELL:** nothing flagged.", ""]
    A += ["**NOTHING TO DO** — the radar (the skill converts these to "
          "BUY by itself in a coming week if the break comes; unbought "
          "old signals expire):", ""]
    for x in a["radar"]:
        if x.get("ladder_watch"):
            A.append(f"- {x['symbol']} — {x['ladder_watch']}")
            continue
        A.append(f"- {x['symbol']} (turns into BUY on a daily close "
                 f"above ₹{x['buy_above']:,.2f})" if x.get("buy_above")
                 else f"- {x['symbol']}")
    for x in a["downgraded"]:
        A.append(f"- {x['symbol']} — {x['why']}")
    if not a["radar"] and not a["downgraded"]:
        A += ["- (empty)"]
    A += [""]
    return "\n".join(A)


def actions_section(dives: list, ledger: list, old_stops: dict,
                    today: str | None = None) -> str:
    return render_actions(actions_data(dives, ledger, old_stops, today))


def recommendation_rows(dives: list) -> list[dict]:
    """The recommendations table, as data — one row per deep dive, the
    same fields the Markdown table prints."""
    rows = []
    for d in dives:
        r, p, c = d["rec"], d["power"], d["calls"]
        mt = d["mtrend"]["verdict"]
        if d["mtrend"].get("rising_months", 0) >= 2:
            mt += f" ({d['mtrend']['rising_months']} mo)"
        rows.append({
            "symbol": r["symbol"], "action": r["action"],
            "downgraded": bool(r.get("downgraded")),
            "box_bottom": r.get("box_bottom"), "box_top": r.get("box_top"),
            "box_range_pct": r.get("box_range_pct"),
            "stop_loss": (None if r["action"] == "SELL"
                          else r.get("stop_loss")),
            "buy_above": r.get("buy_above"),
            "last_close": r.get("last_close"),
            "volume_trend": mt, "earnings_power": p["verdict"],
            "new_age": c.get("new_age", "—"),
            "volume_multiple": d["signal"].get("volume_multiple"),
            "why": r.get("why", "")})
    return rows


def run_record(dives: list, meta: dict, actions: dict, ledger: list,
               quick: bool) -> dict:
    """Everything a UI needs to show EXACTLY what the report shows."""
    return {"run_date": meta["run_date"], "fetched_at": meta["fetched_at"],
            "trigger_week": meta["trigger_week"],
            "scanned": meta["scanned"], "fetch_ok": meta["fetch_ok"],
            "universe_sources": meta.get("universe_sources", {}),
            "fetch_failed": meta["fetch_failed"],
            "weekly_qualifiers": meta.get("weekly_qualifiers"),
            "fully_qualified": meta.get("fully_qualified"),
            "ai_used": not quick and _ai_available(),
            "recommendations": recommendation_rows(dives),
            "actions": actions,
            "ledger": [dict(row) for row in ledger]}


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


def render_ladder_watch(lw: dict) -> list[str]:
    """The ladder watch as a report section: who joined today, who is
    being watched (and how their ladder looks now), who was promoted,
    who expired or broke down."""
    A = ["### The ladder watch", "",
         f"A stock that passes both VOLUME gates but fails the ladder is "
         f"not thrown away: it is watched for {DV.LADDER_WATCH_DAYS} days "
         f"and its ladder re-tested from fresh boxes on every run. The "
         f"moment the ladder rises and the boxes say BUY or ACCUMULATE, it "
         f"is promoted into the picks below, carrying its original surge "
         f"numbers. Darvas listed a stock when the volume came, then "
         f"waited for the boxes — this is that wait, mechanised.", ""]
    def row(r, extra=""):
        return (f"| {r['symbol']} | {r['surge_week']} | "
                f"{float(r['volume_multiple']):.2f}× | "
                f"{float(r['month_multiple']):.2f}× | {r['expires']} | "
                f"{extra or r.get('status', '')} |")
    hdr = ["| Stock | Surge week | Wk multiple | Month vs yr | Watch until "
           "| Status |", "|---|---|---:|---:|---|---|"]
    prom = lw.get("promoted") or []
    if prom:
        A += ["**Promoted today** (deep-dived below):", ""] + hdr
        for s in prom:
            pw = s["promoted_from_watch"]
            A.append(f"| {s['symbol']} | {pw['surge_week']} | "
                     f"{float(pw['volume_multiple']):.2f}× | — | — | "
                     f"ladder rising now — promoted |")
        A.append("")
    watching = lw.get("watching") or []
    if watching:
        A += ["**On watch:**", ""] + hdr
        A += [row(r) for r in watching] + [""]
    else:
        A += ["**On watch:** nobody.", ""]
    gone = (lw.get("expired") or []) + (lw.get("dropped") or [])
    if gone:
        A += ["**Left the watch today:**", ""] + hdr
        A += [row(r) for r in gone] + [""]
    return A


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

    # ---- step 1: three gates
    gated = meta.get("gated") or []
    full = [g for g in gated if g["fully_qualifies"]]
    A.append("## Step 1 — The three qualification gates")
    A.append("")
    A.append(f"A stock must pass ALL THREE, in order: **(a) the weekly "
             f"trigger** — the latest week (pro-rated if running) at ≥"
             f"{DV.QUALIFY_MULTIPLE}× its {DV.BASELINE_WEEKS}-week average "
             f"volume with the price up; **(b) the month-vs-year gate** — "
             f"the last {DV.MONTH_DAYS} trading days' average daily volume "
             f"at ≥{DV.MONTH_VS_YEAR_MULTIPLE}× the average of the "
             f"~11 months before them, so one loud week in a sleepy name "
             f"cannot qualify alone; **(c) the rising ladder** — at least "
             f"{DV.UPTREND_BOXES} sealed boxes with the last "
             f"{DV.UPTREND_BOXES} midpoints stepping upward: the stock "
             f"must have CLIMBED here. "
             f"{len(q)} weekly qualifiers → **{len(full)} pass all three "
             f"gates** out of {meta['scanned']} scanned.")
    A.append("")
    A.append("| # | Stock | Wk multiple | Price wk | Month vs yr vol | "
             "Ladder (last 3 midpoints) | Verdict |")
    A.append("|---:|---|---:|---:|---:|---|---|")
    for i, g in enumerate(gated, 1):
        mv, up = g["month_gate"], g["ladder_gate"]
        mv_txt = (f"{mv['month_vs_year_multiple']:.2f}×"
                  + (" ✓" if mv["qualifies"] else " ✗")) if mv else "no data"
        mids = up["midpoints"][-DV.UPTREND_BOXES:]
        up_txt = (" → ".join(f"{m:,.0f}" for m in mids)
                  + (" ✓" if up["qualifies"] else " ✗"))
        verdict = "**QUALIFIED**" if g["fully_qualifies"] else             ("fails month gate" if mv and not mv["qualifies"]
             else "fails ladder" if not up["qualifies"] else "no data")
        star = "*" if g.get("partial_week") else ""
        A.append(f"| {i} | {g['symbol']} | "
                 f"{g['volume_multiple']:.2f}×{star} | "
                 f"{g['price_change_pct']:+.2f}% | {mv_txt} | {up_txt} | "
                 f"{verdict} |")
    A.append("")
    if any(g.get("partial_week") for g in gated):
        A.append("\* pro-rated — the latest week is still running.")
        A.append("")
    A.append(f"The top {len(dives)} fully-qualified go on to the earnings "
             f"and box steps below.")
    A.append("")
    A += render_ladder_watch(meta.get("ladder_watch") or {})

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
    A.append(f"- **Universe:** the official NiftyTotalMarket constituents "
             f"∪ the 750 largest listed companies by market capitalisation "
             f"(NSE's daily market-cap file; ETFs and funds excluded), "
             f"both re-pulled monthly — a company just outside the index "
             f"but inside the top 750 by size is screened too. "
             f"{meta.get('universe_note', '')}")
    A.append(f"- **Data:** daily bars for the last year for every "
             f"symbol in that universe, fetched fresh THIS run "
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
    # the universe first: the stored NiftyTotalMarket list is checked
    # against NSE Indices' OFFICIAL current list at most once a month,
    # and rewritten only when membership really changed — a failed
    # pull warns and the stored list stands, never blocking the screen
    import refresh_constituents as RC
    r = RC.refresh()
    if r.get("changed"):
        print(f"universe refreshed: {r['count']} members — added "
              f"{', '.join(r['added']) or '—'}; removed "
              f"{', '.join(r['removed']) or '—'}", file=sys.stderr)
    else:
        print(f"universe: {r.get('note', 'unchanged this month')}",
              file=sys.stderr)
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
    daily = DV.load_daily()
    gated = DV.full_qualifiers(scan, daily)
    q = [g for g in gated if g["fully_qualifies"]]
    run_date = dt.date.today().isoformat()
    lw = ladder_watch_update(gated, daily, run_date)
    top = q[:args.top] + lw["promoted"]
    print(f"{sum(1 for s in scan if s['qualifies'])} weekly qualifiers → "
          f"{len(q)} pass all three gates; ladder watch: "
          f"{len(lw['started'])} started, {len(lw['promoted'])} promoted, "
          f"{len(lw['watching'])} watching, {len(lw['expired'])} expired, "
          f"{len(lw['dropped'])} dropped; deep-diving {len(top)}",
          file=sys.stderr)
    ai = _ai_available() and not args.quick
    dives = []
    for s in top:
        d = deep_dive(s["symbol"], weekly, daily, s, ai)
        d["weekly_rows"] = weekly[s["symbol"]]
        dives.append(d)
        print(f"  {s['symbol']}: {d['rec']['action']} "
              f"({s['volume_multiple']:.2f}×)", file=sys.stderr)

    old_stops = {}
    if LEDGER.exists():
        with open(LEDGER) as fh:
            for r in csv.DictReader(fh):
                old_stops[r["symbol"]] = r.get("stop_loss", "")
    picked = {d["rec"]["symbol"] for d in dives}
    carried = carried_updates(LEDGER, picked, daily,
                              {s["symbol"]: s for s in scan})
    ledger = DV.update_ledger(
        LEDGER, [{**d["rec"]} for d in dives] + carried)
    fetched_at = (FD.OUT_DIR / "_fetched_at.txt").read_text().strip() \
        if (FD.OUT_DIR / "_fetched_at.txt").exists() else "unknown"
    log_rows = list((FD.OUT_DIR / "_fetch_log.csv").read_text()
                    .splitlines())[1:]
    failed = sum(1 for r in log_rows if ",failed," in r)
    meta = {
        "run_date": run_date,
        "ladder_watch": lw,
        "fetched_at": fetched_at,
        "scanned": len(scan),
        "fetch_ok": len(log_rows) - failed,
        "fetch_failed": failed,
        "trigger_week": top[0]["week_start"] if top else "—",
        "ledger": ledger,
        "gated": gated,
    }
    src = {}
    with open(FD.CONSTITUENTS) as fh:
        for r in csv.DictReader(fh):
            k = r.get("source") or "official"
            src[k] = src.get(k, 0) + 1
    meta["universe_sources"] = src
    meta["universe_note"] = (
        f"This run: {src.get('both', 0)} in both lists, "
        f"{src.get('official', 0)} only in the index, "
        f"{src.get('mcap750', 0)} only in the top 750 by size.")
    meta["weekly_qualifiers"] = sum(1 for s in scan if s["qualifies"])
    meta["fully_qualified"] = len(gated)
    actions = actions_data(dives, ledger, old_stops, meta["run_date"], lw)
    record = run_record(dives, meta, actions, ledger, args.quick)
    events = DH.full_journal(HISTORY, current=record)
    DH.save_events(events)
    md = (render_report(scan, dives, meta)
          + DH.render_trace_md(events, ledger) + render_actions(actions))
    REPORT.write_text(md)
    LATEST.write_text(json.dumps(record, indent=1, default=str))
    snap = HISTORY / meta["run_date"]
    snap.mkdir(parents=True, exist_ok=True)
    (snap / "DARVAS_REPORT.md").write_text(md)
    (snap / "run.json").write_text(json.dumps(record, indent=1,
                                              default=str))
    shutil.copy(LEDGER, snap / "_positions.csv")
    if LADDER_WATCH.exists():
        shutil.copy(LADDER_WATCH, snap / "_ladder_watch.csv")
    print(f"wrote {REPORT} ({len(md.splitlines())} lines); "
          f"{LATEST.name}; history/{meta['run_date']}/")


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
