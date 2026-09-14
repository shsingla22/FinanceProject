"""
darvas.py — the Darvas method's mechanical core.

Three pieces, each deterministic and testable on synthetic series:

  1. THE VOLUME TRIGGER (step 1). A stock qualifies when its last
     COMPLETED week traded a multiple of its normal weekly volume AND the
     price appreciated that week — volume without price appreciation is
     distribution, price without volume is drift; Darvas required both.
     Ranked by the volume multiple, numbers attached.

  2. BOX DETECTION (step 3). Nicolas Darvas's own definition: a top is a
     high that stands unbroken for the next three sessions; once the top
     stands, the bottom is the subsequent low that stands undercut-free
     for three sessions. Top + bottom seal a box. A close above the top
     is an upward break (the stock "reaches for the higher box"); a close
     below the bottom is a breakdown — the red flag. Every stock gets its
     OWN box height from its own prices; nothing is assumed about range.

  3. STOP LOSSES (step 5). stop = bottom − 0.3 × box height. This is the
     rule the worked examples imply: a 50–55 box stops out around 48
     (50 − 0.3×5 = 48.5) and a 70–85 box around 65 (70 − 0.3×15 = 65.5).
     Stops only ever RATCHET UP: when a stock seals a new, higher box —
     which by construction takes three quiet sessions on each edge, so
     "decisively" is built into the definition — the stop moves up with
     it; a computed stop below the standing one is ignored.
"""

from __future__ import annotations

import csv
import datetime as dt
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
UNIVERSE = "NiftyTotalMarket"
DATA_DIR = INDIA / "VolumeAndPricing" / UNIVERSE

# volume trigger tuning — deliberately explicit so the report can cite it
BASELINE_WEEKS = 12          # up to 12 prior completed weeks form "normal"
MIN_BASELINE_WEEKS = 6       # fewer than this and the stock is not judged
QUALIFY_MULTIPLE = 1.5       # last week must be at least 1.5x normal
TIERS = [(3.0, "multifold"), (2.0, "strong"), (1.5, "elevated")]

CONFIRM_DAYS = 3             # Darvas's three quiet sessions seal an edge
STOP_FRACTION = 0.3          # stop sits 0.3 box-heights below the bottom …
STOP_MIN_BELOW = 0.05        # … and NEVER less than 5% below it: room to
                             # stabilise inside the box instead of churning

# step 1b — the month-vs-year volume gate: the last month of trading must
# run significantly above the stock's one-year norm, so a single loud week
# in a sleepy name cannot qualify on its own
MONTH_DAYS = 21              # ~ one month of trading days
YEAR_BASELINE_DAYS = 231     # ~ the eleven months before that month
MIN_BASELINE_DAYS = 120      # fewer prior days than this and it's not judged
MONTH_VS_YEAR_MULTIPLE = 1.5

# step 1c — the ladder gate: the stock must have CLIMBED here — at least
# three sealed boxes with rising midpoints, the general trend up
UPTREND_BOXES = 3


# ---------------------------------------------------------------- loading

def load_weekly(path: Path | None = None) -> dict[str, list[dict]]:
    """{symbol: [week rows, oldest first]} — ALL weeks, the running
    (partial) one included and flagged, so the trigger always sees the
    LATEST volume and price rather than stopping a week behind."""
    path = path or DATA_DIR / "_all_weekly_long.csv"
    out: dict[str, list[dict]] = {}
    with open(path) as fh:
        for r in csv.DictReader(fh):
            out.setdefault(r["symbol"], []).append({
                "week_start": r["week_start"],
                "open": float(r["open"]), "high": float(r["high"]),
                "low": float(r["low"]), "close": float(r["close"]),
                "volume": int(r["volume"]),
                "days": int(r["days"]) if r.get("days") else 5,
                "complete": r["complete"] == "True",
            })
    for rows in out.values():
        rows.sort(key=lambda w: w["week_start"])
    return out


def load_daily(path: Path | None = None) -> dict[str, list[dict]]:
    path = path or DATA_DIR / "_all_daily_long.csv"
    out: dict[str, list[dict]] = {}
    with open(path) as fh:
        for r in csv.DictReader(fh):
            out.setdefault(r["symbol"], []).append({
                "date": r["date"],
                "high": float(r["high"]) if r["high"] else None,
                "low": float(r["low"]) if r["low"] else None,
                "close": float(r["close"]),
                "volume": int(r["volume"]),
            })
    for rows in out.values():
        rows.sort(key=lambda d: d["date"])
    return out


# ---------------------------------------------------------- volume trigger

def volume_signal(weeks: list[dict]) -> dict | None:
    """The step-1 numbers for one stock, or None when history is too thin.

    The week under test is the LATEST week in the data — the running
    (partial) week when there is one, so a surge is caught the day it
    happens, not a week later. A partial week's multiple is pro-rated to
    a full five-day week (volume ÷ (average × days÷5)) and labelled so
    the report can say exactly what was compared. Baseline = mean weekly
    volume of up to BASELINE_WEEKS COMPLETED weeks before the test week."""
    if not weeks:
        return None
    test = weeks[-1]
    prior = [w for w in weeks[:-1] if w.get("complete", True)]
    if len(prior) < MIN_BASELINE_WEEKS:
        return None
    base = [w["volume"] for w in prior[-BASELINE_WEEKS:]]
    avg = sum(base) / len(base)
    if avg <= 0:
        return None
    partial = not test.get("complete", True)
    days = min(5, test.get("days") or 5)
    fraction = (days / 5) if partial else 1.0
    if fraction <= 0:
        return None
    prev_close = prior[-1]["close"]
    price_pct = (test["close"] - prev_close) / prev_close * 100
    raw_multiple = test["volume"] / avg
    multiple = raw_multiple / fraction
    tier = next((name for cut, name in TIERS if multiple >= cut), None)
    recent = [{"week_start": w["week_start"], "volume": w["volume"],
               "close": w["close"], "complete": w.get("complete", True),
               "days": w.get("days", 5)} for w in weeks[-4:]]
    return {
        "week_start": test["week_start"],
        "partial_week": partial,
        "days_traded": days if partial else 5,
        "last_week_volume": test["volume"],
        "baseline_weeks": len(base),
        "baseline_avg_volume": round(avg),
        "volume_multiple": round(multiple, 2),
        "raw_volume_multiple": round(raw_multiple, 2),
        "recent_weeks": recent,
        "price_change_pct": round(price_pct, 2),
        "close": test["close"],
        "tier": tier,
        "qualifies": multiple >= QUALIFY_MULTIPLE and price_pct > 0,
    }


def scan_universe(weekly: dict[str, list[dict]]) -> list[dict]:
    """Every stock's signal; qualifiers first, highest multiple first —
    'the best stocks with highest volume reactions … in the same order'."""
    out = []
    for sym, weeks in weekly.items():
        sig = volume_signal(weeks)
        if sig is not None:
            out.append({"symbol": sym, **sig})
    out.sort(key=lambda s: (-s["qualifies"], -s["volume_multiple"]))
    return out


# -------------------------------------------------------------- box theory

def find_boxes(daily: list[dict]) -> dict:
    """Darvas boxes over one stock's daily bars.

    Returns {"boxes": [...], "state": "IN_BOX"|"BREAKOUT"|"BREAKDOWN"|
    "FORMING", "current": <last sealed box or None>}. Each box carries
    top, bottom, the dates its edges were set, range_pct (the stock's own
    box height), and how it resolved: "up", "down" or "open"."""
    highs = [d["high"] for d in daily]
    lows = [d["low"] for d in daily]
    closes = [d["close"] for d in daily]
    dates = [d["date"] for d in daily]
    n = len(daily)
    boxes: list[dict] = []
    state = "FORMING"
    i = 0
    top = bottom = None
    top_i = None
    while i < n:
        if top is None:
            # seek a top: a high unbroken for the next CONFIRM_DAYS
            cand, cand_i = highs[i], i
            j = i + 1
            while j < n and j - cand_i <= CONFIRM_DAYS:
                if highs[j] is not None and highs[j] > cand:
                    cand, cand_i = highs[j], j
                    j = cand_i + 1
                    continue
                j += 1
            if j - cand_i <= CONFIRM_DAYS:      # ran out of data unconfirmed
                # a break that JUST happened stays a break — the next box
                # simply has not had its three quiet sessions yet
                if state not in ("BREAKOUT", "BREAKDOWN"):
                    state = "FORMING"
                break
            top, top_i = cand, cand_i
            i = cand_i + 1
            bottom = None
            continue
        if bottom is None:
            # seek a bottom after the top: a low undercut-free for 3 days
            cand, cand_i = lows[top_i + 1] if top_i + 1 < n else None, top_i + 1
            if cand is None:
                state = "FORMING"
                break
            j = cand_i + 1
            while j < n and j - cand_i <= CONFIRM_DAYS:
                if lows[j] is not None and lows[j] < cand:
                    cand, cand_i = lows[j], j
                    j = cand_i + 1
                    continue
                j += 1
            if j - cand_i <= CONFIRM_DAYS:
                if state not in ("BREAKOUT", "BREAKDOWN"):
                    state = "FORMING"
                break
            bottom = cand
            boxes.append({
                "top": top, "bottom": bottom,
                "top_date": dates[top_i], "bottom_date": dates[cand_i],
                "range_pct": round((top - bottom) / bottom * 100, 2),
                "outcome": "open",
            })
            state = "IN_BOX"
            i = cand_i + 1
            continue
        # a sealed box: watch the closes for a break of either edge
        c = closes[i]
        if c > top:
            boxes[-1]["outcome"] = "up"
            boxes[-1]["break_date"] = dates[i]
            top = bottom = None                  # reach for the higher box
            state = "BREAKOUT"
            continue                             # re-seek from this same day
        if c < bottom:
            boxes[-1]["outcome"] = "down"
            boxes[-1]["break_date"] = dates[i]
            top = bottom = None
            state = "BREAKDOWN"
            i += 1
            # after a breakdown, box-seeking starts fresh below
            continue
        i += 1
    current = boxes[-1] if boxes else None
    if boxes and boxes[-1]["outcome"] == "open":
        state = "IN_BOX"
    # a breakdown is only the standing verdict while the price honours it:
    # a later CLOSE back above the broken box's TOP is a recovery — the
    # stock is reaching upward again, but with no sealed box there is no
    # honest stop yet, so it is watched, not bought and not sold
    if (state == "BREAKDOWN" and boxes and closes
            and closes[-1] > boxes[-1]["top"]):
        state = "RECOVERY"
    return {"boxes": boxes, "state": state, "current": current,
            "last_close": closes[-1] if closes else None,
            "last_date": dates[-1] if dates else None}


def stop_loss(box: dict) -> float:
    """stop = bottom − max(STOP_FRACTION × height, STOP_MIN_BELOW × bottom):
    the stock's own range sets the distance, but the stop always sits AT
    LEAST 5% below the box bottom — a shallow box must not put the stop a
    rupee under the floor and churn the position on ordinary noise."""
    height = box["top"] - box["bottom"]
    gap = max(STOP_FRACTION * height, STOP_MIN_BELOW * box["bottom"])
    return round(box["bottom"] - gap, 2)


def recommend(box_state: dict, signal: dict) -> dict:
    """Steps 4-5: what to do, from the boxes + the volume trigger.

    BUY        broke above its box on the trigger volume — Darvas's entry
    ACCUMULATE sealed a HIGHER box after an upward break and is holding it
    WATCH      in a box; the entry is a close above the box top
    SELL       closed below its box bottom — the red flag, exit
    """
    state = box_state["state"]
    cur = box_state["current"]
    if state == "RECOVERY":
        action, why = "WATCH", (
            "broke down through its box but has since CLOSED back above "
            "the old box top on the trigger volume — a recovery, not a "
            "standing breakdown; with no new box sealed there is no "
            "honest stop yet, so wait for the next box before buying")
    elif state == "BREAKDOWN":
        graced = (cur is not None and box_state.get("last_close") is not None
                  and box_state["last_close"] > stop_loss(cur))
        if graced:
            action, why = "WATCH", (
                "closed below its box bottom — a red flag, but still inside "
                "the stabilisation grace (above the stop, which sits at "
                "least 5% below the bottom); give it time rather than "
                "churn, and sell only if the stop is taken out")
        else:
            action, why = "SELL", (
                "closed below its box bottom AND through the stop — "
                "Darvas's red flag confirmed; a stock dropping to a lower "
                "box is sold, not averaged")
    elif state == "BREAKOUT":
        action, why = "BUY", ("closed above its box top on trigger volume — "
                              "reaching for the higher box; buy the break")
    elif state == "IN_BOX" and cur is not None and _prior_break_up(box_state):
        action, why = "ACCUMULATE", ("sealed a higher box after an upward "
                                     "break and is holding it — add while "
                                     "it stabilises in the higher box")
    elif state == "IN_BOX":
        action, why = "WATCH", ("moving inside its box on trigger volume — "
                                "the entry is a close above the box top")
    else:
        action, why = "WATCH", ("box still forming — too few quiet sessions "
                                "to seal both edges yet")
    out = {"action": action, "why": why, "state": state}
    if state == "RECOVERY":
        return out          # the broken box's edges are history, not levels
    if cur is not None:
        out["box_top"] = cur["top"]
        out["box_bottom"] = cur["bottom"]
        out["box_range_pct"] = cur["range_pct"]
        out["stop_loss"] = stop_loss(cur)
        if action == "WATCH":
            out["buy_above"] = cur["top"]
    return out


def _prior_break_up(box_state: dict) -> bool:
    boxes = box_state["boxes"]
    return len(boxes) >= 2 and boxes[-2]["outcome"] == "up"


# ------------------------------------------------------------- the ledger

LEDGER_FIELDS = ["symbol", "first_flagged", "action", "box_bottom",
                 "box_top", "stop_loss", "last_close", "updated"]


def update_ledger(path: Path, picks: list[dict],
                  today: str | None = None) -> list[dict]:
    """The stop-loss rhythm (step 5): the ledger is re-read on every run —
    the rhythm IS the run, weekly after Friday's close — and each held
    symbol's stop is recomputed from its CURRENT box. The new stop is
    kept only if it is HIGHER: max(old, new). A SELL wipes the stop and
    marks the row; a symbol newly flagged is added with its first stop."""
    today = today or dt.date.today().isoformat()
    rows: dict[str, dict] = {}
    if path.exists():
        with open(path) as fh:
            for r in csv.DictReader(fh):
                rows[r["symbol"]] = r
    for p in picks:
        sym = p["symbol"]
        old = rows.get(sym)
        stop = p.get("stop_loss")
        if old and old.get("stop_loss") not in (None, "", "None") \
                and stop is not None:
            stop = max(float(old["stop_loss"]), float(stop))
        rows[sym] = {
            "symbol": sym,
            "first_flagged": (old or {}).get("first_flagged") or today,
            "action": p["action"],
            "box_bottom": p.get("box_bottom", ""),
            "box_top": p.get("box_top", ""),
            "stop_loss": "" if p["action"] == "SELL" else
                         ("" if stop is None else stop),
            "last_close": p.get("last_close", ""),
            "updated": today,
        }
    ordered = sorted(rows.values(), key=lambda r: r["symbol"])
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=LEDGER_FIELDS)
        w.writeheader()
        for r in ordered:
            w.writerow({k: r.get(k, "") for k in LEDGER_FIELDS})
    return ordered


# ------------------------------------------------------- monthly volumes

def monthly_volumes(daily: list[dict],
                    running_month: str | None = None) -> list[dict]:
    """Calendar-month volume totals from daily bars, oldest first.
    The running month (default: the month of the last bar) is flagged
    partial so no trend conclusion ever leans on an unfinished month."""
    if not daily:
        return []
    running_month = running_month or daily[-1]["date"][:7]
    by_m: dict[str, dict] = {}
    for r in daily:
        m = r["date"][:7]
        e = by_m.setdefault(m, {"month": m, "volume": 0, "days": 0,
                                "close": r["close"]})
        e["volume"] += r["volume"]
        e["days"] += 1
        e["close"] = r["close"]
    out = [by_m[m] for m in sorted(by_m)]
    for e in out:
        e["complete"] = e["month"] != running_month
    return out


def monthly_trend(months: list[dict]) -> dict:
    """Is the volume BUILDING month over month, or was the trigger a
    one-week event? Judged on COMPLETE months only — the running month
    is shown but never argued from."""
    comp = [m for m in months if m["complete"]]
    if len(comp) < 3:
        return {"verdict": "TOO SHORT", "rising_months": 0,
                "why": "fewer than three complete months of data"}
    streak = 0
    for i in range(len(comp) - 1, 0, -1):
        if comp[i]["volume"] > comp[i - 1]["volume"]:
            streak += 1
        else:
            break
    if streak >= 2:
        return {"verdict": "BUILDING", "rising_months": streak,
                "why": f"volume has risen month over month for the last "
                       f"{streak} complete months — buying pressure has "
                       f"been building, not arriving in one week"}
    prior = [m["volume"] for m in comp[:-1]]
    last = comp[-1]["volume"]
    if prior and last > 1.5 * (sum(prior) / len(prior)):
        return {"verdict": "STEPPED UP", "rising_months": streak,
                "why": "the last complete month traded well above the "
                       "months before it"}
    return {"verdict": "SPIKE ONLY", "rising_months": streak,
            "why": "monthly volumes were flat before the trigger — the "
                   "surge is a one-week event so far, not a building trend"}


# ------------------------------- step 1b: month vs year volume gate

def month_vs_year(daily: list[dict]) -> dict | None:
    """Is the LAST MONTH of trading significantly louder than the stock's
    one-year norm? recent = the last MONTH_DAYS trading days' average daily
    volume; baseline = the average of the up-to-YEAR_BASELINE_DAYS days
    before them (at least MIN_BASELINE_DAYS, else not judged)."""
    if len(daily) < MONTH_DAYS + MIN_BASELINE_DAYS:
        return None
    recent = [d["volume"] for d in daily[-MONTH_DAYS:]]
    prior = [d["volume"] for d in
             daily[-(MONTH_DAYS + YEAR_BASELINE_DAYS):-MONTH_DAYS]]
    base = sum(prior) / len(prior)
    if base <= 0:
        return None
    mult = (sum(recent) / len(recent)) / base
    return {"month_avg_daily": round(sum(recent) / len(recent)),
            "year_avg_daily": round(base),
            "baseline_days": len(prior),
            "month_vs_year_multiple": round(mult, 2),
            "qualifies": mult >= MONTH_VS_YEAR_MULTIPLE}


# ------------------------------------ step 1c: the rising-ladder gate

def box_uptrend(boxes: list[dict]) -> dict:
    """Has the stock CLIMBED here? At least UPTREND_BOXES sealed boxes,
    with the midpoints of the last UPTREND_BOXES strictly rising — the
    general trend up, box over box."""
    mids = [round((b["top"] + b["bottom"]) / 2, 2) for b in boxes]
    if len(boxes) < UPTREND_BOXES:
        return {"qualifies": False, "boxes": len(boxes), "midpoints": mids,
                "why": f"only {len(boxes)} sealed box"
                       f"{'es' if len(boxes) != 1 else ''} — the ladder is "
                       f"too short to call a trend"}
    last = mids[-UPTREND_BOXES:]
    rising = all(last[i] < last[i + 1] for i in range(len(last) - 1))
    return {"qualifies": rising, "boxes": len(boxes), "midpoints": mids,
            "why": (f"the last {UPTREND_BOXES} boxes step upward "
                    f"({' → '.join(f'₹{m:,.1f}' for m in last)})" if rising
                    else f"the last {UPTREND_BOXES} box midpoints do not "
                         f"step upward ({' → '.join(f'₹{m:,.1f}' for m in last)})")}


def full_qualifiers(scan: list[dict],
                    daily: dict[str, list[dict]]) -> list[dict]:
    """All three gates together, order preserved from the weekly scan:
    weekly trigger AND month-vs-year volume AND the rising ladder. Each
    row keeps every gate's numbers so the report can show WHY a stock
    passed or fell out."""
    out = []
    for s in scan:
        if not s["qualifies"]:
            continue
        bars = daily.get(s["symbol"])
        if not bars:
            continue
        mv = month_vs_year(bars)
        up = box_uptrend(find_boxes(bars)["boxes"])
        out.append({**s,
                    "month_gate": mv,
                    "ladder_gate": up,
                    "fully_qualifies": bool(mv and mv["qualifies"]
                                            and up["qualifies"])})
    return out
