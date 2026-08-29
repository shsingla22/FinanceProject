"""
linechart.py — a proper multi-series line chart drawn in text.

Why text: GitHub's Markdown sanitiser strips every inline image (tested:
data-URI PNG, data-URI SVG and raw <svg> are all removed), while plain
image files break the "everything in one file" requirement and Mermaid
does not render in every Markdown viewer. Characters render identically
in all of them, so the chart is drawn with real box-drawing strokes.

Each series gets its own stroke weight so three lines stay readable in
one grid:

    Price ratio             light   ─ │ ╭ ╮ ╰ ╯   points marked ●
    PAT ratio               heavy   ━ ┃ ┏ ┓ ┗ ┛   points marked ◆
    Operating-profit ratio  double  ═ ║ ╔ ╗ ╚ ╝   points marked ■

The value of every data point is printed underneath its own column, so
each point on the graph carries its number.
"""

from __future__ import annotations

# horizontal, vertical, top-left, top-right, bottom-left, bottom-right, marker
STROKES = [
    ("─", "│", "╭", "╮", "╰", "╯", "●"),   # light
    ("━", "┃", "┏", "┓", "┗", "┛", "◆"),   # heavy
    ("═", "║", "╔", "╗", "╚", "╝", "■"),   # double
]
MARKERS = [s[6] for s in STROKES]

HEIGHT = 15          # plot rows
STEP = 8             # columns between two fiscal years
GUTTER = 9           # width of the y-axis label column


def _nice_bounds(lo: float, hi: float) -> tuple[float, float]:
    """Pad the value range a little so the line never touches the frame."""
    if hi == lo:
        return lo - 1, hi + 1
    pad = (hi - lo) * 0.08
    return lo - pad, hi + pad


def render(series, title: str, unit: str = "%") -> str:
    """series: [(name, {fiscal_year: value})] or [(name, values, style_index)].

    Passing an explicit style index keeps a measure's stroke and marker the
    same in every report, even when another measure has no data to plot.
    Returns a fenced code block.
    """
    series = [(s[0], s[1], s[2] if len(s) > 2 else i)
              for i, s in enumerate(series)]
    years = sorted({y for _, s, _i in series for y in s})
    if not years:
        return "*(no data to plot)*\n"
    values = [v for _, s, _i in series for v in s.values()]
    lo, hi = _nice_bounds(min(values + [0.0]), max(values + [0.0]))
    span = hi - lo

    width = GUTTER + (len(years) - 1) * STEP + 3
    grid = [[" "] * width for _ in range(HEIGHT)]

    def row_of(v: float) -> int:
        return int(round((hi - v) / span * (HEIGHT - 1)))

    def col_of(year: int) -> int:
        return GUTTER + years.index(year) * STEP

    # zero line first, so the series draw over it
    zero_row = row_of(0.0) if lo <= 0 <= hi else None
    if zero_row is not None:
        for c in range(GUTTER, width):
            grid[zero_row][c] = "┈"

    # one pass for the strokes, a second for the point markers, so a later
    # series can never bury an earlier series' data points
    for _name, s, idx in series:
        h, v, tl, tr, bl, br, _m = STROKES[idx % len(STROKES)]
        pts = [(col_of(y), row_of(s[y])) for y in years if y in s]
        for (c0, r0), (c1, r1) in zip(pts, pts[1:]):
            prev = r0
            for c in range(c0 + 1, c1 + 1):
                r = int(round(r0 + (r1 - r0) * (c - c0) / (c1 - c0)))
                if r == prev:
                    grid[r][c] = h
                    continue
                step = 1 if r > prev else -1
                for rr in range(prev + step, r, step):
                    grid[rr][c] = v
                if r > prev:                    # value falling
                    grid[prev][c], grid[r][c] = tr, bl
                else:                           # value rising
                    grid[prev][c], grid[r][c] = br, tl
                prev = r

    for _name, s, idx in series:
        marker = MARKERS[idx % len(MARKERS)]
        for y in years:
            if y in s:
                grid[row_of(s[y])][col_of(y)] = marker

    # y-axis labels on five evenly spaced levels
    for k in range(5):
        val = hi - span * k / 4
        r = row_of(val)
        label = f"{val:+,.0f}{unit}".rjust(GUTTER - 2)
        for j, ch in enumerate(label):
            grid[r][j] = ch
        grid[r][GUTTER - 1] = "┼" if r == zero_row else "┤"
    for r in range(HEIGHT):
        if grid[r][GUTTER - 1] == " ":
            grid[r][GUTTER - 1] = "│"

    out = [f"{title}", ""]
    out += ["".join(r).rstrip() for r in grid]

    # x-axis with a tick under every fiscal year
    axis = [" "] * width
    axis[GUTTER - 1] = "└"
    for c in range(GUTTER, width):
        axis[c] = "─"
    for y in years:
        axis[col_of(y)] = "┬"
    out.append("".join(axis).rstrip())

    def label_row(prefix: str, text_of) -> str:
        row = [" "] * width
        for j, ch in enumerate(prefix):        # marker sits at the left edge
            row[j] = ch
        for y in years:
            t = text_of(y)
            if t is None:
                continue
            # centre the text on the year's column; the gutter is blank on
            # these rows, so the first label may start inside it
            start = max(0, min(col_of(y) - len(t) // 2, width - len(t)))
            for j, ch in enumerate(t):
                row[start + j] = ch
        return "".join(row).rstrip()

    out.append(label_row("", lambda y: f"FY{str(y)[2:]}"))
    out.append("")
    # the value of every point, under its own column
    for name, s, idx in series:
        marker = MARKERS[idx % len(MARKERS)]
        out.append(label_row(f"{marker} ",
                             lambda y, s=s: (f"{s[y]:+.1f}" if y in s else "·")))
    out.append("")
    legend = "   ".join(f"{MARKERS[i % len(MARKERS)]} {name}"
                        for name, _s, i in series)
    out.append(legend)
    if zero_row is not None:
        out.append("┈ the 0% line — above it the company gained on the index "
                   "that year, below it the company lagged")
    return "```\n" + "\n".join(out) + "\n```\n"
