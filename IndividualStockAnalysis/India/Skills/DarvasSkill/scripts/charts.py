"""
charts.py — the pictorial side of the report, drawn as text.

GitHub strips inline SVG and data-URI images from rendered Markdown (the
repository established this empirically in the StockToIndexPriceEarnings-
Ratio work), so the report's pictures are text-drawn: they survive every
renderer, including GitHub itself. Two pictures per recommended stock:

  * the WEEKLY VOLUME + PRICE chart — one row per completed week, the
    volume as a scaled bar with its exact number, the close and the
    week-on-week move beside it, and the trigger week marked; and
  * the BOX picture — the sealed boxes as ranges on a price ladder, the
    current box, the buy point and the stop, each with its exact price.
"""

from __future__ import annotations

BAR = "█"
HALF = "▌"


def _fmt_vol(v: float) -> str:
    if v >= 1e7:
        return f"{v / 1e7:.2f} Cr"
    if v >= 1e5:
        return f"{v / 1e5:.2f} L"
    return f"{v:,.0f}"


def weekly_chart(weeks: list[dict], max_weeks: int = 13,
                 width: int = 26) -> str:
    """Volume bars with the price beside them, latest week last."""
    rows = weeks[-max_weeks:]
    if not rows:
        return ""
    peak = max(w["volume"] for w in rows) or 1
    out = ["```",
           "Week of      volume" + " " * (width - 4) + "close     w/w"]
    prev = None
    for i, w in enumerate(rows):
        n = max(1, round(w["volume"] / peak * width))
        bar = BAR * n
        chg = ""
        if prev:
            pct = (w["close"] - prev["close"]) / prev["close"] * 100
            arrow = "▲" if pct > 0.2 else "▼" if pct < -0.2 else "▬"
            chg = f"{arrow} {pct:+.1f}%"
        mark = ""
        if i == len(rows) - 1:
            mark = "  ◀ trigger week"
            if not w.get("complete", True):
                mark += f" (partial: {w.get('days', '?')} days so far)"
        out.append(f"{w['week_start']}  {bar:<{width + 2}}"
                   f"{_fmt_vol(w['volume']):>9}  "
                   f"₹{w['close']:>9,.1f}  {chg:>8}{mark}")
        prev = w
    out.append("```")
    return "\n".join(out)


def box_picture(box_state: dict, rec: dict) -> str:
    """The sealed boxes as a ladder, most recent at the top."""
    boxes = box_state["boxes"]          # the FULL six-month ladder
    if not boxes:
        return "*(no box sealed yet — too few quiet sessions on each edge)*"
    out = ["```"]
    last_close = box_state.get("last_close")
    for b in reversed(boxes):
        tag = {"open": "  ◀ current box", "up": "  broke UP",
               "down": "  broke DOWN — red flag"}[b["outcome"]]
        out.append(f"┌ ₹{b['top']:>9,.2f} ─ top    ({b['top_date']})")
        inside = ""
        if b["outcome"] == "open" and last_close is not None:
            inside = f"   close ₹{last_close:,.2f} inside"
        out.append(f"│   box height {b['range_pct']:.1f}%{inside}")
        out.append(f"└ ₹{b['bottom']:>9,.2f} ─ bottom ({b['bottom_date']})"
                   + tag)
    if rec.get("stop_loss") is not None:
        out.append(f"  ✂ ₹{rec['stop_loss']:>9,.2f} ─ stop loss "
                   f"(bottom − 0.3 × box height)")
    if rec.get("buy_above") is not None:
        out.append(f"  ▲ ₹{rec['buy_above']:>9,.2f} ─ buy on a close above "
                   f"the box top")
    out.append("```")
    return "\n".join(out)


# ------------------------- price line + volume bars, one shared picture

PRICE_ROWS = 9
VOL_ROWS = 4
COL_W = 3           # one week = one 3-character column, both panels


def price_volume_chart(weeks: list[dict], max_weeks: int = 13) -> str:
    """The Darvas picture: the weekly close as a line, the weekly volume
    as bars UNDER it on the same week axis — a genuine surge shows as the
    price stepping up exactly where a volume bar towers."""
    rows = weeks[-max_weeks:]
    if len(rows) < 2:
        return ""
    closes = [w["close"] for w in rows]
    vols = [w["volume"] for w in rows]
    n = len(rows)
    lo, hi = min(closes), max(closes)
    pad = (hi - lo) * 0.08 or max(lo * 0.01, 1)
    lo -= pad
    hi += pad

    def level(c):
        return round((hi - c) / (hi - lo) * (PRICE_ROWS - 1))

    grid = [[" "] * (n * COL_W) for _ in range(PRICE_ROWS)]
    for i, c in enumerate(closes):
        x = i * COL_W + 1
        grid[level(c)][x] = "●"
        if i:
            a, b = level(closes[i - 1]), level(c)
            step = 1 if b > a else -1
            for r in range(a + step, b, step):
                grid[r][x - 1 if step > 0 else x - 1] = \
                    "╲" if step > 0 else "╱"

    margin = 10
    out = ["```"]
    top_lab = f"₹{max(closes):,.0f}"
    bot_lab = f"₹{min(closes):,.0f}"
    for r in range(PRICE_ROWS):
        lab = top_lab if r == level(max(closes)) else \
              bot_lab if r == level(min(closes)) else ""
        out.append(f"{lab:>{margin - 2}} │ " + "".join(grid[r]).rstrip())
    out.append(" " * (margin - 2) + " ┼" + "─" * (n * COL_W))

    peak = max(vols) or 1
    peak_lab = _fmt_vol(peak)
    for r in range(VOL_ROWS, 0, -1):
        line = []
        for v in vols:
            h = v / peak * VOL_ROWS
            line.append(" █ " if h >= r - 0.5 else "   ")
        lab = peak_lab if r == VOL_ROWS else ""
        out.append(f"{lab:>{margin - 2}} │ " + "".join(line).rstrip())
    out.append(" " * (margin - 2) + " └" + "─" * (n * COL_W))

    # week labels centred under their own columns, every second week;
    # the grid starts at text column margin+1, markers sit at +1 inside it
    lab_row = [" "] * (margin + 1 + n * COL_W + 6)
    for i, w in enumerate(rows):
        if i % 2 == (n - 1) % 2:          # latest week always labelled
            text = w["week_start"][5:]
            x = margin + 1 + i * COL_W + 1 - 2      # centre minus half label
            for j, ch in enumerate(text):
                if 0 <= x + j < len(lab_row):
                    lab_row[x + j] = ch
    out.append("".join(lab_row).rstrip())

    last = rows[-1]
    partial = "" if last.get("complete", True) else \
        f" (partial: {last.get('days', '?')} days so far)"
    out.append(f"{'':>{margin - 2}}   latest week{partial}: "
               f"volume {_fmt_vol(last['volume'])}, "
               f"close ₹{last['close']:,.1f}")
    out.append("```")
    return "\n".join(out)


def monthly_volume_table(months: list[dict]) -> str:
    """Month-wise volume with the change against the prior month — the
    running month flagged, never argued from."""
    if not months:
        return ""
    out = ["| Month | Volume | vs prior month | |",
           "|---|---:|---:|---|"]
    prev = None
    for m in months:
        chg = ""
        if prev and prev > 0:
            pct = (m["volume"] - prev) / prev * 100
            chg = f"{'▲' if pct > 5 else '▼' if pct < -5 else '▬'} {pct:+.0f}%"
        note = "" if m["complete"] else f"partial — {m['days']} days"
        out.append(f"| {m['month']} | {m['volume']:,} | {chg} | {note} |")
        prev = m["volume"] if m["complete"] else prev
    return "\n".join(out)
