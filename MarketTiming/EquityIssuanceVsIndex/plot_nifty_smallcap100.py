"""
Line graph of Nifty Smallcap 100 year-end closing values plus yearly
percentage change, sourced only from nifty_smallcap100_data.csv.

Covers calendar years 2012-2025. The percentage-change series starts
from 2013 because 2011 isn't in the source data (NSE bhavcopy archives
only go back to 2012).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
CSV = HERE / "nifty_smallcap100_data.csv"
OUT = HERE / "nifty_smallcap100_close_vs_yoy.png"


def plot() -> None:
    df = pd.read_csv(CSV).sort_values("calendar_year").reset_index(drop=True)
    df["yoy_pct"] = df["year_end_close"].pct_change() * 100

    fig, ax_close = plt.subplots(figsize=(15, 8))
    ax_pct = ax_close.twinx()

    x = df["calendar_year"]

    line_close = ax_close.plot(
        x, df["year_end_close"], marker="o", linewidth=2.5,
        color="#1f77b4", label="Nifty Smallcap 100 (year-end close)",
    )[0]
    line_pct = ax_pct.plot(
        x, df["yoy_pct"], marker="s", linewidth=2, linestyle="--",
        color="#d62728", label="YoY % change",
    )[0]
    ax_pct.axhline(0, color="#d62728", linewidth=0.5, alpha=0.3)

    ax_close.set_xlabel("Calendar year")
    ax_close.set_ylabel("Year-end closing value", color="#1f77b4")
    ax_pct.set_ylabel("YoY % change", color="#d62728")
    ax_close.tick_params(axis="y", labelcolor="#1f77b4")
    ax_pct.tick_params(axis="y", labelcolor="#d62728")

    ax_close.set_xticks(x)
    ax_close.set_xticklabels(x, rotation=0)
    ax_close.grid(True, alpha=0.3)

    ax_close.set_title(
        "Nifty Smallcap 100 — year-end close and YoY % change (CY 2012-2025)\n"
        "Source: NSE archives end-of-day index bhavcopy files",
        fontsize=12,
    )

    ax_close.legend(
        [line_close, line_pct],
        [line_close.get_label(), line_pct.get_label()],
        loc="upper left", fontsize=10, framealpha=0.95,
    )

    for xv, yv in zip(x, df["yoy_pct"]):
        if pd.notna(yv):
            ax_pct.annotate(
                f"{yv:+.1f}%", xy=(xv, yv),
                xytext=(0, 8 if yv >= 0 else -14),
                textcoords="offset points",
                ha="center", fontsize=8, color="#d62728",
            )

    fig.tight_layout()
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    plot()
