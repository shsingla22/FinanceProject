"""Chart 4: ALL seven series from Charts 1-3 on a single chart.

Because the seven series have very different scales (INR per USD is
~40-95, index levels are 2,000-65,000, median constituent prices are
~5-1,500), three y-axes are used:

  - Left y-axis        : INR per 1 USD                       (1 line)
  - Right y-axis #1    : Median constituent year-end close   (3 lines)
  - Right y-axis #2    : Index year-end close                (3 lines)

All seven series are sourced from Yahoo Finance via yfinance
(see data_fetcher.py).
"""

from __future__ import annotations
import os

import matplotlib.pyplot as plt
import pandas as pd

from plot_inr_usd import build_dataset as build_inr
from plot_indices import build_dataset as build_indices
from plot_medians import build_dataset as build_medians

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(HERE, "combined_all.png")
OUT_CSV = os.path.join(HERE, "combined_all.csv")
YEARS_BACK = 25


def build_dataset(years_back: int = YEARS_BACK) -> pd.DataFrame:
    inr = build_inr(years_back)               # 1 col:  inr_per_usd
    idx = build_indices(years_back)           # 3 cols: nifty50, nifty_midcap, nifty_smallcap
    med = build_medians(years_back)           # 3 cols: *_median
    df = inr.join([idx, med], how="outer").sort_index()
    df.index.name = "year"
    return df


def plot(df: pd.DataFrame, out_path: str = OUT_PNG) -> None:
    fig, ax_inr = plt.subplots(figsize=(17, 9))

    # Left axis: INR per USD
    color_inr = "#d62728"
    line_inr = ax_inr.plot(
        df.index, df["inr_per_usd"],
        color=color_inr, marker="o", linewidth=2.4,
        label="INR per 1 USD",
    )
    ax_inr.set_xlabel("Year")
    ax_inr.set_ylabel("INR per 1 USD", color=color_inr)
    ax_inr.tick_params(axis="y", labelcolor=color_inr)

    # Right axis #1: median constituent close
    ax_med = ax_inr.twinx()
    l_med_50 = ax_med.plot(
        df.index, df["nifty50_median"],
        color="#1f77b4", marker="o", linewidth=1.8, linestyle="--",
        label="Nifty 50 — median constituent close",
    )
    l_med_mid = ax_med.plot(
        df.index, df["midcap_median"],
        color="#2ca02c", marker="s", linewidth=1.8, linestyle="--",
        label="Nifty Midcap 100 — median constituent close",
    )
    l_med_sm = ax_med.plot(
        df.index, df["smallcap_median"],
        color="#ff7f0e", marker="^", linewidth=1.8, linestyle="--",
        label="Nifty Smallcap 100 — median constituent close",
    )
    ax_med.set_ylabel("Median constituent close (INR, dashed lines)",
                      color="#444444")
    ax_med.tick_params(axis="y", labelcolor="#444444")

    # Right axis #2: index level
    ax_idx = ax_inr.twinx()
    ax_idx.spines["right"].set_position(("axes", 1.08))
    l_idx_50 = ax_idx.plot(
        df.index, df["nifty50"],
        color="#1f77b4", marker="o", linewidth=2.2,
        label="Nifty 50 — year-end close",
    )
    l_idx_mid = ax_idx.plot(
        df.index, df["nifty_midcap"],
        color="#2ca02c", marker="s", linewidth=2.2,
        label="Nifty Midcap 100 — year-end close",
    )
    l_idx_sm = ax_idx.plot(
        df.index, df["nifty_smallcap"],
        color="#ff7f0e", marker="^", linewidth=2.2,
        label="Nifty/BSE Smallcap — year-end close",
    )
    ax_idx.set_ylabel("Index level (year-end close, solid lines)",
                      color="#222222")
    ax_idx.tick_params(axis="y", labelcolor="#222222")

    lines = (line_inr + l_idx_50 + l_idx_mid + l_idx_sm
             + l_med_50 + l_med_mid + l_med_sm)
    labels = [ln.get_label() for ln in lines]
    ax_inr.legend(lines, labels, loc="upper left", framealpha=0.9,
                  fontsize=9)

    plt.title(f"INR vs USD, Nifty 50 / Midcap / Smallcap index levels, "
              f"and median constituent prices — last {YEARS_BACK} years")
    ax_inr.grid(True, alpha=0.3)
    ax_inr.set_xticks(df.index)
    ax_inr.set_xticklabels([str(y) for y in df.index], rotation=45)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140)
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    df = build_dataset()
    df.to_csv(OUT_CSV)
    print(df.to_string())
    plot(df)
