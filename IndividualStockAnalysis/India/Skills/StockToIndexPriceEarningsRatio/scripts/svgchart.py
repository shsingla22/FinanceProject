"""
svgchart.py — the same line graph as a standalone SVG.

The Markdown report carries a text chart because GitHub strips inline
images, but a vector file is still useful on its own: it opens in any
browser, scales cleanly and can be dropped into a deck. One file per
company sits beside the report.

Colours follow the project's dataviz palette: series-1 blue for the
price ratio, green for PAT, amber for operating profit, with ink-toned
text and a neutral zero line. Values are printed at every point.
"""

from __future__ import annotations

COLORS = ["#2a78d6", "#1a9e5c", "#e07b00"]
W, H = 980, 460
L, R, T, B = 78, 26, 54, 96          # margins


def _bounds(values: list[float]) -> tuple[float, float]:
    lo, hi = min(values + [0.0]), max(values + [0.0])
    if hi == lo:
        return lo - 1, hi + 1
    pad = (hi - lo) * 0.10
    return lo - pad, hi + pad


def render(series: list[tuple[str, dict[int, float]]], title: str,
           subtitle: str = "", unit: str = "%") -> str:
    """series: [(name, {fiscal_year: value})] -> a complete SVG document."""
    years = sorted({y for _, s in series for y in s})
    if not years:
        return ""
    values = [v for _, s in series for v in s.values()]
    lo, hi = _bounds(values)
    span = hi - lo

    def x(year: int) -> float:
        if len(years) == 1:
            return L + (W - L - R) / 2
        return L + years.index(year) * (W - L - R) / (len(years) - 1)

    def y(v: float) -> float:
        return T + (hi - v) * (H - T - B) / span

    p: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" font-family="Helvetica,Arial,sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
        f'<text x="{W/2:.0f}" y="26" text-anchor="middle" font-size="17" '
        f'font-weight="700" fill="#0b0b0b">{_esc(title)}</text>',
    ]
    if subtitle:
        p.append(f'<text x="{W/2:.0f}" y="44" text-anchor="middle" '
                 f'font-size="12" fill="#52514e">{_esc(subtitle)}</text>')

    # horizontal gridlines + y labels
    for k in range(5):
        v = hi - span * k / 4
        yy = y(v)
        p.append(f'<line x1="{L}" y1="{yy:.1f}" x2="{W-R}" y2="{yy:.1f}" '
                 f'stroke="#e4e3df" stroke-width="1"/>')
        p.append(f'<text x="{L-10}" y="{yy+4:.1f}" text-anchor="end" '
                 f'font-size="12" fill="#52514e">{v:+,.0f}{unit}</text>')
    # zero line
    if lo < 0 < hi:
        p.append(f'<line x1="{L}" y1="{y(0):.1f}" x2="{W-R}" y2="{y(0):.1f}" '
                 f'stroke="#9b9a94" stroke-width="1.5" stroke-dasharray="6 4"/>')
    # x axis
    p.append(f'<line x1="{L}" y1="{H-B:.1f}" x2="{W-R}" y2="{H-B:.1f}" '
             f'stroke="#52514e" stroke-width="1"/>')
    for yr in years:
        p.append(f'<line x1="{x(yr):.1f}" y1="{H-B:.1f}" x2="{x(yr):.1f}" '
                 f'y2="{H-B+5:.1f}" stroke="#52514e" stroke-width="1"/>')
        p.append(f'<text x="{x(yr):.1f}" y="{H-B+20:.0f}" text-anchor="middle" '
                 f'font-size="12" fill="#52514e">FY{yr}</text>')

    # series
    for i, (name, s) in enumerate(series):
        color = COLORS[i % len(COLORS)]
        pts = [(x(yr), y(s[yr])) for yr in years if yr in s]
        if len(pts) > 1:
            path = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
            p.append(f'<polyline points="{path}" fill="none" stroke="{color}" '
                     f'stroke-width="2.6" stroke-linejoin="round" '
                     f'stroke-linecap="round"/>')
        for yr in years:
            if yr not in s:
                continue
            px, py = x(yr), y(s[yr])
            p.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" '
                     f'fill="#ffffff" stroke="{color}" stroke-width="2.4"/>')
            # value label, nudged above or below to avoid the line
            above = i % 2 == 0
            dy = -11 if above else 17
            p.append(f'<text x="{px:.1f}" y="{py+dy:.1f}" text-anchor="middle" '
                     f'font-size="10.5" fill="{color}">{s[yr]:+.1f}</text>')

    # legend
    lx = L
    for i, (name, _s) in enumerate(series):
        color = COLORS[i % len(COLORS)]
        p.append(f'<rect x="{lx}" y="{H-34}" width="13" height="13" rx="3" '
                 f'fill="{color}"/>')
        p.append(f'<text x="{lx+19}" y="{H-23}" font-size="12.5" '
                 f'fill="#0b0b0b">{_esc(name)}</text>')
        lx += 30 + int(7.1 * len(name))
    p.append("</svg>")
    return "\n".join(p) + "\n"


def _esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
