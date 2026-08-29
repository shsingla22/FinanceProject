"""
mermaidchart.py — the same line graph as a Mermaid `xychart-beta` source.

GitHub renders Mermaid fences natively (verified against its live
renderer), so this file gives a chart that draws itself when pasted into
a GitHub comment, an issue, a wiki page or any Mermaid-aware editor.

Mermaid's xychart requires every line to have exactly as many points as
the x-axis has labels, and has no notion of a missing point. Series are
therefore plotted over the fiscal years that ALL plotted series share;
when that trims years off the ends, the header comment says so rather
than padding the gap with invented numbers.
"""

from __future__ import annotations


def render(series: list[tuple[str, dict[int, float]]], title: str,
           y_label: str = "Change vs the index (%)") -> str:
    """series: [(name, {fiscal_year: value})] -> a .mmd document."""
    series = [(n, s) for n, s in series if s]
    if not series:
        return ""

    # Some companies' series cover disjoint years (a recent listing price
    # against older statements, say), so no year is shared by all of them.
    # Plot the subset that yields the most points rather than nothing,
    # preferring more lines when the point count ties.
    best: tuple[int, int, list, list] | None = None
    for mask in range(1, 1 << len(series)):
        subset = [series[i] for i in range(len(series)) if mask >> i & 1]
        common = sorted(set.intersection(*[set(s) for _n, s in subset]))
        if len(common) < 2:                 # a line needs at least two points
            continue
        score = (len(subset) * len(common), len(subset))
        if best is None or score > best[:2]:
            best = (score[0], score[1], subset, common)
    if best is None:
        return ""
    _pts, _n, subset, common = best
    excluded = [n for n, _s in series if n not in {x[0] for x in subset}]
    everything = sorted({y for _n, s in subset for y in s})
    dropped = [y for y in everything if y not in common]
    series = subset

    head = [f"%% {title}",
            "%% Lines, in order: " + ", ".join(n for n, _s in series)]
    if excluded:
        head.append("%% Left out — no fiscal years in common with the lines "
                    "above: " + ", ".join(excluded))
    if dropped:
        head.append("%% Fiscal years not shared by every line, so left out: "
                    + ", ".join(f"FY{y}" for y in dropped))
    head.append("%% Renders on GitHub and in any Mermaid-aware viewer.")

    values = [s[y] for _n, s in series for y in common]
    lo, hi = min(values + [0.0]), max(values + [0.0])
    pad = (hi - lo) * 0.1 or 1.0

    body = ["xychart-beta",
            f'    title "{title}"',
            "    x-axis [" + ", ".join(f"FY{y}" for y in common) + "]",
            f'    y-axis "{y_label}" {lo - pad:.0f} --> {hi + pad:.0f}']
    for _name, s in series:
        body.append("    line [" + ", ".join(f"{s[y]:.1f}"
                                             for y in common) + "]")
    return "\n".join(head) + "\n" + "\n".join(body) + "\n"
