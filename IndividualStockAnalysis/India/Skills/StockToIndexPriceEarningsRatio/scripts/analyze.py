"""
analyze.py — StockToIndexPriceEarningsRatio reports.

For one company, writes a Markdown report with three charts, one data
point per fiscal year, up to the last 15 fiscal years:

  1. Price ratio      company share price at fiscal-year end
                      ÷ Nifty 50 close of the same month
  2. PAT ratio        company Net Profit for the fiscal year
                      ÷ summed Net Profit of the Nifty 50 constituents
  3. Operating ratio  company Operating Profit (Financing Profit for
                      lenders) ÷ summed Operating Profit of the index

A RISING line means the company outgrew the index on that measure; a
FALLING line means it lagged the index. Years where either side of a
ratio is missing in the stored data are listed, never guessed.

Usage (from this folder):
  python3 analyze.py report SYMBOL out.md
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
INDIA = HERE.parent.parent.parent          # .../IndividualStockAnalysis/India
STOCKINFO = INDIA / "StockInfo" / "Nifty500"
PL_LONG = INDIA / "ProfitStatement" / "NiftyTotalMarket" / "_all_profit_loss_long.csv"
CONST = INDIA / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"

MAX_YEARS = 15
BAR_WIDTH = 26


# ---------------------------------------------------------------- inputs

def fy_of(label: str) -> str:
    """Map a statement column like 'Jun 2024' to its fiscal year 'Mar 2025'
    (Apr..Dec YYYY -> Mar YYYY+1; Jan..Mar YYYY -> Mar YYYY)."""
    mon, yr = label.split()
    m = datetime.strptime(mon, "%b").month
    return f"Mar {int(yr) + 1}" if m >= 4 else f"Mar {yr}"


def load_index() -> tuple[pd.DataFrame, pd.DataFrame]:
    monthly = pd.read_csv(DATA / "nifty50_price_monthly.csv")
    earnings = pd.read_csv(DATA / "nifty50_earnings_yearly.csv")
    return monthly, earnings


def company_prices(sym: str) -> dict[str, tuple[str, float]]:
    """fy -> (statement column label, share price at that fiscal-year end)."""
    f = STOCKINFO / f"{sym}.csv"
    if not f.exists():
        return {}
    df = pd.read_csv(f)
    row = df[df.metric == "Stock Price (Rs)"]
    if row.empty:
        return {}
    out: dict[str, tuple[str, float]] = {}
    for col in df.columns[1:]:
        if col == "Live":
            continue
        v = row.iloc[0][col]
        if pd.notna(v):
            out[fy_of(col)] = (col, float(v))
    return out


def company_earnings(sym: str) -> dict[str, dict[str, float]]:
    """fy -> {'pat': .., 'op': ..} from the stored long profit-and-loss."""
    pl = pd.read_csv(PL_LONG)
    pl = pl[pl.nse_symbol == sym]
    out: dict[str, dict[str, float]] = {}
    for _, r in pl.iterrows():
        fy = fy_of(r.year)
        d = out.setdefault(fy, {})
        if r.line_item == "Net Profit" and pd.notna(r.value):
            d["pat"] = float(r.value)
        # lenders report Financing Profit instead of Operating Profit;
        # prefer Operating Profit when both appear
        if r.line_item == "Operating Profit" and pd.notna(r.value):
            d["op"] = float(r.value)
        if r.line_item == "Financing Profit" and pd.notna(r.value) \
                and "op" not in d:
            d["op"] = float(r.value)
    return out


def index_close_for(monthly: pd.DataFrame, label: str) -> float | None:
    """Index close of the company's fiscal-year-end month (e.g. 'Jun 2024')."""
    mon, yr = label.split()
    m = datetime.strptime(mon, "%b").month
    hit = monthly[(monthly.year == int(yr)) & (monthly.month_num == m)]
    return float(hit.close.iloc[0]) if not hit.empty else None


# ---------------------------------------------------------------- charts

def chart(rows: list[tuple[str, float]], unit: str) -> str:
    """ASCII bar chart, one row per fiscal year: FY, bar, value, YoY move."""
    if not rows:
        return "*(no overlapping years in the stored data)*\n"
    peak = max(abs(v) for _, v in rows) or 1.0
    lines = ["```"]
    prev = None
    for fy, v in rows:
        n = max(1, round(abs(v) / peak * BAR_WIDTH)) if v else 0
        bar = ("█" if v >= 0 else "▒") * n
        move = ""
        if prev not in (None, 0):
            pct = (v - prev) / abs(prev) * 100
            arrow = "▲" if pct > 0.5 else ("▼" if pct < -0.5 else "▬")
            move = f"  {arrow} {pct:+.1f}% vs prior year"
        lines.append(f"FY{fy.split()[1]}  {bar:<{BAR_WIDTH}} {v:.3f}{unit}{move}")
        prev = v
    lines.append("```")
    return "\n".join(lines) + "\n"


WINDOWS = [15, 10, 5, 3, 1]                # trend windows, in fiscal years


def _pct_change(a: float, b: float) -> str:
    """Change from a to b, worded safely across sign flips."""
    if a == 0:
        return "n/a (base year is zero)"
    if a < 0 <= b:
        return "turned from loss to profit share"
    if b < 0 <= a:
        return "fell from profit to loss share"
    return f"{(b - a) / abs(a) * 100:+.0f}%"


def trend_windows(rows: list[tuple[str, float]]) -> str:
    """Markdown table: change of the ratio over the last 15/10/5/3/1 FYs."""
    if len(rows) < 2:
        return "*(too little data for window trends)*\n"
    by_year = {int(fy.split()[1]): v for fy, v in rows}
    latest_year = max(by_year)
    lines = ["| Window | From | To | Ratio change |",
             "|---|---|---|---|"]
    for w in WINDOWS:
        base_year = latest_year - w
        if base_year in by_year:
            lines.append(
                f"| last {w} year{'s' if w > 1 else ''} | FY{base_year} "
                f"| FY{latest_year} "
                f"| {_pct_change(by_year[base_year], by_year[latest_year])} |")
        else:
            first = min(by_year)
            lines.append(
                f"| last {w} year{'s' if w > 1 else ''} | FY{base_year} "
                f"| FY{latest_year} | n/a — data starts FY{first} |")
    return "\n".join(lines) + "\n"


def yoy_series(rows: list[tuple[str, float]]) -> dict[int, float]:
    """FY year -> % change of the ratio vs the prior fiscal year."""
    by_year = {int(fy.split()[1]): v for fy, v in rows}
    out: dict[int, float] = {}
    for y, v in by_year.items():
        prev = by_year.get(y - 1)
        if prev not in (None, 0):
            out[y] = (v - prev) / abs(prev) * 100
    return out


def ascii_line_graph(series: list[tuple[str, str, dict[int, float]]]) -> str:
    """Kept for backwards compatibility; the report now uses linechart."""
    import linechart
    return linechart.render([(n, s) for n, _l, s in series],
                            "Yearly change of each ratio (%)")


def point_values_table(series: list[tuple[str, str, dict[int, float]]]) -> str:
    """The exact value at every point of the line graph."""
    years = sorted({y for _, _, s in series for y in s})
    head = "| Fiscal year | " + " | ".join(name for name, _, _ in series) + " |"
    sep = "|---" * (len(series) + 1) + "|"
    rows = [head, sep]
    for y in years:
        cells = [f"{s[y]:+.1f}%" if y in s else "—" for _, _, s in series]
        rows.append(f"| FY{y} | " + " | ".join(cells) + " |")
    return "\n".join(rows) + "\n"


def yoy_line_graph(price_rows, pat_rows, op_rows) -> str:
    """A proper line graph of the yearly change of the three ratios: all
    three together for comparison, then each on its own for a close read.
    Drawn with box-drawing strokes so it renders identically in GitHub,
    plain Markdown viewers and any editor — GitHub strips inline images."""
    import linechart
    # the style index is pinned per measure, so ● always means price,
    # ◆ always PAT and ■ always operating profit in every report
    series = [("Price ratio", yoy_series(price_rows), 0),
              ("PAT ratio", yoy_series(pat_rows), 1),
              ("Operating-profit ratio", yoy_series(op_rows), 2)]
    series = [(n, s, i) for n, s, i in series if s]
    if not series:
        return "*(no overlapping years in the stored data)*\n"

    out = linechart.render(
        series, "ALL THREE RATIOS — yearly change against the Nifty 50 (%)")
    if len(series) > 1:
        out += "\nEach line again on its own, for a closer read:\n\n"
        for name, s, i in series:
            out += linechart.render(
                [(name, s, i)],
                f"{name.upper()} — yearly change against the Nifty 50 (%)")
            out += "\n"
    out += ("\n**The value at every point of the graph** (also printed under "
            "each point above):\n\n")
    out += point_values_table([(n, "", s) for n, s, _i in series])
    return out


def raw_values_table(sym: str, prices, earn, idx_earn, monthly,
                     fys: list[str]) -> str:
    """Every underlying number the three ratios are built from, per year."""
    head = ("| Fiscal year | Company price (Rs) | Nifty 50 close "
            "| Company PAT (Rs cr) | Index PAT (Rs cr) "
            "| Company OP (Rs cr) | Index OP (Rs cr) |")
    rows = [head, "|---|---|---|---|---|---|---|"]
    for fy in fys:
        px = idx_px = pat = op = ipat = iop = "—"
        if fy in prices:
            label, v = prices[fy]
            px = f"{v:,.2f}"
            ic = index_close_for(monthly, label)
            if ic:
                idx_px = f"{ic:,.2f}"
                if label != fy:
                    idx_px += f" ({label})"
        e = earn.get(fy, {})
        if "pat" in e:
            pat = f"{e['pat']:,.0f}"
        if "op" in e:
            op = f"{e['op']:,.0f}"
        if fy in idx_earn.index:
            ipat = f"{idx_earn.loc[fy, 'index_pat']:,.0f}"
            iop = f"{idx_earn.loc[fy, 'index_op']:,.0f}"
        if {px, idx_px, pat, op, ipat, iop} == {"—"}:
            continue
        rows.append(f"| FY{fy.split()[1]} | {px} | {idx_px} | {pat} "
                    f"| {ipat} | {op} | {iop} |")
    return "\n".join(rows) + "\n"


def trend_word(rows: list[tuple[str, float]]) -> str:
    if len(rows) < 2 or rows[0][1] == 0:
        return "too little overlapping data to call a trend"
    if rows[0][1] < 0 <= rows[-1][1]:
        return (f"TURNED AROUND against the index: from a loss in "
                f"FY{rows[0][0].split()[1]} to a positive share of the "
                f"index by FY{rows[-1][0].split()[1]}")
    if rows[-1][1] < 0 <= rows[0][1]:
        return (f"FELL INTO LOSS: positive in FY{rows[0][0].split()[1]}, "
                f"negative by FY{rows[-1][0].split()[1]}")
    total = (rows[-1][1] - rows[0][1]) / abs(rows[0][1]) * 100
    if total > 10:
        return (f"GAINED on the index: the ratio rose {total:+.0f}% from "
                f"FY{rows[0][0].split()[1]} to FY{rows[-1][0].split()[1]}")
    if total < -10:
        return (f"LAGGED the index: the ratio fell {total:+.0f}% from "
                f"FY{rows[0][0].split()[1]} to FY{rows[-1][0].split()[1]}")
    return (f"MOVED WITH the index: the ratio changed only {total:+.0f}% "
            f"across the window")


# ---------------------------------------------------------------- report

def build_report(sym: str) -> str:
    monthly, idx_earn = load_index()
    prices = company_prices(sym)
    earn = company_earnings(sym)
    names = {r["nse_symbol"]: r["company_name"]
             for _, r in pd.read_csv(CONST).iterrows()}
    name = names.get(sym, sym)

    idx_earn = idx_earn.set_index("fy")
    fys_all = sorted(set(prices) | set(earn) | set(idx_earn.index),
                     key=lambda s: int(s.split()[1]))[-MAX_YEARS:]

    price_rows, pat_rows, op_rows = [], [], []
    missing: list[str] = []
    for fy in fys_all:
        # price ratio — company FY-end price vs index close of that month
        if fy in prices:
            label, px = prices[fy]
            ic = index_close_for(monthly, label)
            if ic:
                price_rows.append((fy, px / ic * 1000))
            else:
                missing.append(f"{fy}: no index close for {label}")
        # earnings ratios — company vs summed index, same fiscal year
        if fy in idx_earn.index:
            e = earn.get(fy, {})
            if "pat" in e and idx_earn.loc[fy, "index_pat"]:
                pat_rows.append((fy, e["pat"] / idx_earn.loc[fy, "index_pat"] * 100))
            elif fy in prices or fy in earn:
                if "pat" not in e:
                    missing.append(f"{fy}: company Net Profit not in stored data")
            if "op" in e and idx_earn.loc[fy, "index_op"]:
                op_rows.append((fy, e["op"] / idx_earn.loc[fy, "index_op"] * 100))

    idx_span = (f"{idx_earn.index[0]}..{idx_earn.index[-1]}"
                if len(idx_earn) else "none")
    md = [f"# {name} ({sym}) — Stock vs Nifty 50: price and earnings ratios\n"]
    md.append(
        f"Every chart divides the company by the **Nifty 50** index, one "
        f"point per fiscal year, up to the last {MAX_YEARS} fiscal years. "
        f"A **rising** line means the company outgrew the index on that "
        f"measure; a **falling** line means it lagged. Index prices are "
        f"real ^NSEI closes; index PAT and operating profit are the summed "
        f"figures of the current 50 constituents from the stored "
        f"statements ({idx_span}) — today's membership, so older years "
        f"carry a survivorship caveat.\n")

    md.append("## 1. Price ratio — company share price ÷ Nifty 50 "
              "(×1000 for readability)\n")
    md.append(f"**Verdict: {trend_word(price_rows)}.**\n")
    md.append(chart(price_rows, ""))
    md.append("\n**Change over the standard windows**\n")
    md.append(trend_windows(price_rows))

    md.append("\n## 2. PAT ratio — company net profit ÷ index net profit "
              "(% of index)\n")
    md.append(f"**Verdict: {trend_word(pat_rows)}.**\n")
    md.append(chart(pat_rows, "%"))
    md.append("\n**Change over the standard windows**\n")
    md.append(trend_windows(pat_rows))

    md.append("\n## 3. Operating-profit ratio — company operating profit ÷ "
              "index operating profit (% of index)\n")
    md.append(f"**Verdict: {trend_word(op_rows)}.**\n")
    md.append(chart(op_rows, "%"))
    md.append("\n**Change over the standard windows**\n")
    md.append(trend_windows(op_rows))

    md.append("\n## 4. Yearly change of all three ratios — line graph\n")
    md.append("One line per ratio, one point per fiscal year: how much the "
              "company gained (+) or lost (−) on the index that year.\n")
    md.append(yoy_line_graph(price_rows, pat_rows, op_rows))

    md.append("\n## 5. The raw yearly values behind every ratio\n")
    md.append("Company prices in rupees; profits in Rs crore. The index "
              "close is the March close unless the company closes its "
              "books in another month (shown in brackets). '—' = not in "
              "the stored data.\n")
    md.append(raw_values_table(sym, prices, earn, idx_earn, monthly, fys_all))

    if missing:
        md.append("\n## Years the stored data could not cover\n")
        for m in missing:
            md.append(f"- {m}")
        md.append("")

    md.append("\n---\n*Generated by the StockToIndexPriceEarningsRatio "
              "skill. Research tooling — not investment advice.*\n")
    return "\n".join(md)


def main() -> None:
    if len(sys.argv) != 4 or sys.argv[1] != "report":
        print("usage: python3 analyze.py report SYMBOL out.md")
        sys.exit(2)
    sym, out = sys.argv[2].upper(), Path(sys.argv[3])
    out.write_text(build_report(sym))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
