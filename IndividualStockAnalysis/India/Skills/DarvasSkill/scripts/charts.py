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
        mark = "  ◀ trigger week" if i == len(rows) - 1 else ""
        out.append(f"{w['week_start']}  {bar:<{width + 2}}"
                   f"{_fmt_vol(w['volume']):>9}  "
                   f"₹{w['close']:>9,.1f}  {chg:>8}{mark}")
        prev = w
    out.append("```")
    return "\n".join(out)


def box_picture(box_state: dict, rec: dict) -> str:
    """The sealed boxes as a ladder, most recent at the top."""
    boxes = box_state["boxes"][-4:]
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
