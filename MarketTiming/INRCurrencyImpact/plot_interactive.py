"""Interactive HTML versions of Charts 1-4 (built with Plotly).

Two interactive features:

1. Enable/disable lines on the chart
   Click any legend entry to hide/show that line. Double-click an entry
   to isolate it (hide all others). This is Plotly's built-in legend
   behaviour and works for every chart in this module.

2. Adjust the time/yearly view to a custom range
   Each chart has:
     - a range-slider strip below the main plot that you can drag to
       narrow the x-axis,
     - quick-pick buttons (Last 5y / 10y / 15y / 25y / All), and
     - native click-drag zoom on the plot itself; double-click to reset.

Plotly.js is inlined into every HTML file (via `include_plotlyjs=True`)
so the page works fully offline and when opened via the `file://`
protocol in Safari / Chrome / Firefox. The trade-off is that each
HTML is ~3-4 MB instead of ~20 KB — necessary because Safari blocks
external CDN scripts on `file://` pages.

The existing static PNG charts are kept untouched — this module only
adds *_interactive.html files next to them.
"""

from __future__ import annotations
import os

import pandas as pd
import plotly.graph_objects as go

from plot_inr_usd import build_dataset as build_inr
from plot_indices import build_dataset as build_indices
from plot_medians import build_dataset as build_medians
from plot_combined import build_dataset as build_combined

HERE = os.path.dirname(os.path.abspath(__file__))
YEARS_BACK = 25

# Standard colour scheme reused from the matplotlib charts
C_INR  = "#d62728"
C_50   = "#1f77b4"
C_MID  = "#2ca02c"
C_SM   = "#ff7f0e"
C_FII  = "#8c564b"


def _add_year_controls(fig: go.Figure) -> None:
    """Attach an x-axis range slider, year-window quick-pick buttons,
    and double-click-to-reset behaviour to a year-indexed chart."""
    fig.update_xaxes(
        rangeslider=dict(visible=True, thickness=0.06),
        rangeselector=dict(
            buttons=[
                dict(count=5,  label="Last 5y",  step="year",
                     stepmode="backward"),
                dict(count=10, label="Last 10y", step="year",
                     stepmode="backward"),
                dict(count=15, label="Last 15y", step="year",
                     stepmode="backward"),
                dict(count=25, label="Last 25y", step="year",
                     stepmode="backward"),
                dict(label="All", step="all"),
            ],
            x=0.0, y=1.12, xanchor="left", yanchor="top",
        ),
        tickmode="linear", dtick=1, tickangle=-45,
    )
    fig.update_layout(
        legend=dict(
            itemclick="toggle",
            itemdoubleclick="toggleothers",
            x=0.0, y=1.0, bgcolor="rgba(255,255,255,0.85)",
        ),
        hovermode="x unified",
        margin=dict(l=70, r=70, t=110, b=70),
    )


def _years_as_dates(idx: pd.Index) -> pd.Index:
    """Plotly's range-slider works on datetimes; map year ints -> Dec-31
    of each year so the slider gives one tick per year."""
    return pd.to_datetime([f"{int(y)}-12-31" for y in idx])


# -- Chart 1: INR vs USD ----------------------------------------------------
def render_inr_usd(out: str | None = None) -> str:
    out = out or os.path.join(HERE, "inr_vs_usd_interactive.html")
    df = build_inr(YEARS_BACK)
    x = _years_as_dates(df.index)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=df["inr_per_usd"],
        mode="lines+markers",
        line=dict(color=C_INR, width=2.4),
        marker=dict(size=7),
        name="INR per 1 USD (year-end)",
    ))
    fig.update_layout(
        title=f"Indian Rupee vs US Dollar (last {YEARS_BACK} years, "
              f"year-end close)",
        xaxis_title="Year",
        yaxis_title="INR per 1 USD",
        height=560,
    )
    _add_year_controls(fig)
    fig.write_html(out, include_plotlyjs=True, full_html=True)
    print(f"Saved: {out}")
    return out


# -- Chart 2: 3 Nifty indices on one chart ---------------------------------
def render_indices(out: str | None = None) -> str:
    out = out or os.path.join(HERE, "nifty_indices_interactive.html")
    df = build_indices(YEARS_BACK)
    x = _years_as_dates(df.index)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=df["nifty50"],
        mode="lines+markers",
        line=dict(color=C_50, width=2.2),
        marker=dict(size=7, symbol="circle"),
        name="Nifty 50",
    ))
    fig.add_trace(go.Scatter(
        x=x, y=df["nifty_midcap"],
        mode="lines+markers",
        line=dict(color=C_MID, width=2.2),
        marker=dict(size=7, symbol="square"),
        name="Nifty Midcap 100",
    ))
    fig.add_trace(go.Scatter(
        x=x, y=df["nifty_smallcap"],
        mode="lines+markers",
        line=dict(color=C_SM, width=2.2),
        marker=dict(size=7, symbol="triangle-up"),
        name="Nifty/BSE Smallcap",
    ))
    fig.update_layout(
        title=f"Nifty 50 / Midcap 100 / Smallcap Yearly Close "
              f"(last {YEARS_BACK} years)",
        xaxis_title="Year",
        yaxis_title="Index level (year-end close)",
        height=640,
    )
    _add_year_controls(fig)
    fig.write_html(out, include_plotlyjs=True, full_html=True)
    print(f"Saved: {out}")
    return out


# -- Chart 3: median constituent close --------------------------------------
def render_medians(out: str | None = None) -> str:
    out = out or os.path.join(HERE, "constituent_medians_interactive.html")
    df = build_medians(YEARS_BACK)
    x = _years_as_dates(df.index)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=df["nifty50_median"],
        mode="lines+markers",
        line=dict(color=C_50, width=2.0),
        marker=dict(size=7, symbol="circle"),
        name="Nifty 50 — median constituent close",
    ))
    fig.add_trace(go.Scatter(
        x=x, y=df["midcap_median"],
        mode="lines+markers",
        line=dict(color=C_MID, width=2.0),
        marker=dict(size=7, symbol="square"),
        name="Nifty Midcap 100 — median constituent close",
    ))
    fig.add_trace(go.Scatter(
        x=x, y=df["smallcap_median"],
        mode="lines+markers",
        line=dict(color=C_SM, width=2.0),
        marker=dict(size=7, symbol="triangle-up"),
        name="Nifty Smallcap 100 — median constituent close",
    ))
    fig.update_layout(
        title=f"Median Year-End Constituent Price: Nifty 50 / Midcap / "
              f"Smallcap (last {YEARS_BACK} years)",
        xaxis_title="Year",
        yaxis_title="Median constituent close (INR)",
        height=640,
    )
    _add_year_controls(fig)
    fig.write_html(out, include_plotlyjs=True, full_html=True)
    print(f"Saved: {out}")
    return out


# -- Chart 4: all 8 series on a single chart with four y-axes ---------------
def render_combined(out: str | None = None) -> str:
    out = out or os.path.join(HERE, "combined_all_interactive.html")
    df = build_combined(YEARS_BACK)
    x = _years_as_dates(df.index)

    fig = go.Figure()

    # y-axis 1 (left): INR per USD
    fig.add_trace(go.Scatter(
        x=x, y=df["inr_per_usd"], yaxis="y1",
        mode="lines+markers",
        line=dict(color=C_INR, width=2.6),
        marker=dict(size=8, symbol="circle"),
        name="INR per 1 USD",
    ))

    # y-axis 2: median constituent close
    fig.add_trace(go.Scatter(
        x=x, y=df["nifty50_median"], yaxis="y2",
        mode="lines+markers",
        line=dict(color=C_50, width=1.7, dash="dash"),
        marker=dict(size=6, symbol="circle"),
        name="Nifty 50 — median constituent close",
    ))
    fig.add_trace(go.Scatter(
        x=x, y=df["midcap_median"], yaxis="y2",
        mode="lines+markers",
        line=dict(color=C_MID, width=1.7, dash="dash"),
        marker=dict(size=6, symbol="square"),
        name="Nifty Midcap 100 — median constituent close",
    ))
    fig.add_trace(go.Scatter(
        x=x, y=df["smallcap_median"], yaxis="y2",
        mode="lines+markers",
        line=dict(color=C_SM, width=1.7, dash="dash"),
        marker=dict(size=6, symbol="triangle-up"),
        name="Nifty Smallcap 100 — median constituent close",
    ))

    # y-axis 3: index level
    fig.add_trace(go.Scatter(
        x=x, y=df["nifty50"], yaxis="y3",
        mode="lines+markers",
        line=dict(color=C_50, width=2.4),
        marker=dict(size=7, symbol="circle"),
        name="Nifty 50 — year-end close",
    ))
    fig.add_trace(go.Scatter(
        x=x, y=df["nifty_midcap"], yaxis="y3",
        mode="lines+markers",
        line=dict(color=C_MID, width=2.4),
        marker=dict(size=7, symbol="square"),
        name="Nifty Midcap 100 — year-end close",
    ))
    fig.add_trace(go.Scatter(
        x=x, y=df["nifty_smallcap"], yaxis="y3",
        mode="lines+markers",
        line=dict(color=C_SM, width=2.4),
        marker=dict(size=7, symbol="triangle-up"),
        name="Nifty/BSE Smallcap — year-end close",
    ))

    # y-axis 4: total FII inflow (USD mn)
    fig.add_trace(go.Scatter(
        x=x, y=df["fii_total_usd_mn"], yaxis="y4",
        mode="lines+markers",
        line=dict(color=C_FII, width=2.4, dash="dot"),
        marker=dict(size=8, symbol="cross"),
        name="Net FII inflow — total Indian equity (USD mn, CDSL)",
    ))
    # zero reference line for FII flow
    fig.add_hline(y=0, line=dict(color="#999999", width=1), yref="y4")

    fig.update_layout(
        title=f"INR/USD · Nifty 50 / Midcap / Smallcap index levels · median "
              f"constituent prices · net FII equity inflow — last "
              f"{YEARS_BACK} years",
        height=780,
        xaxis=dict(
            domain=[0.06, 0.86],
            title="Year",
        ),
        yaxis=dict(
            title=dict(text="INR per 1 USD", font=dict(color=C_INR)),
            tickfont=dict(color=C_INR),
            anchor="x", side="left",
        ),
        yaxis2=dict(
            title=dict(text="Median constituent close (INR)",
                        font=dict(color="#444444")),
            tickfont=dict(color="#444444"),
            anchor="x", overlaying="y", side="right",
            position=0.86,
        ),
        yaxis3=dict(
            title=dict(text="Index level (year-end close)",
                        font=dict(color="#222222")),
            tickfont=dict(color="#222222"),
            anchor="free", overlaying="y", side="right",
            position=0.93,
        ),
        yaxis4=dict(
            title=dict(text="Net FII inflow (USD mn)",
                        font=dict(color=C_FII)),
            tickfont=dict(color=C_FII),
            anchor="free", overlaying="y", side="right",
            position=1.00,
        ),
    )
    _add_year_controls(fig)
    fig.write_html(out, include_plotlyjs=True, full_html=True)
    print(f"Saved: {out}")
    return out


def render_all() -> None:
    render_inr_usd()
    render_indices()
    render_medians()
    render_combined()


if __name__ == "__main__":
    render_all()
