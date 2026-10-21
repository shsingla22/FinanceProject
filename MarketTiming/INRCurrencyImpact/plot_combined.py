"""Chart 4: ALL series from Charts 1-3 plus net total FII equity inflow.

Eight lines on a single chart:
  - INR per 1 USD                                       (1 line, solid)
  - Index year-end close: Nifty 50, Midcap 100, Smallcap (3 lines, solid)
  - Median constituent year-end close: Nifty 50, Midcap, Smallcap (3 lines, dashed)
  - Net FII equity inflow — TOTAL Indian equity        (1 line, dotted)

Four y-axes are used to handle the very different scales:
  - Left y-axis        : INR per 1 USD                       (~40-95)
  - Right y-axis #1    : Median constituent close            (~5-1,500)
  - Right y-axis #2    : Index level                         (2K-65K)
  - Right y-axis #3    : Net FII inflow (USD mn)             (-18K to +37K)

Per-Nifty-index FII flow series are intentionally NOT plotted here:
CDSL/NSDL/SEBI/NSE do not publish net FII flow broken down by index,
so any per-index series would need to be derived from per-stock data
rather than read from a single published source.

Sources:
  - Prices (INR/USD, indices, constituents):  Yahoo Finance via yfinance
  - Total FII inflow:                          CDSL FPI/FII Investment
                                              Details (Financial Year),
                                              USD via FRED DEXINUS yearly
                                              average. See fii_inflows.py.
"""

from __future__ import annotations
import os

import matplotlib.pyplot as plt
import pandas as pd

from plot_inr_usd import build_dataset as build_inr
from plot_indices import build_dataset as build_indices
from plot_medians import build_dataset as build_medians
from fii_inflows import build_fii_inflows_df

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(HERE, "combined_all.png")
OUT_CSV = os.path.join(HERE, "combined_all.csv")
YEARS_BACK = 25


def build_dataset(years_back: int = YEARS_BACK) -> pd.DataFrame:
    inr = build_inr(years_back)
    idx = build_indices(years_back)
    med = build_medians(years_back)
    fii = build_fii_inflows_df()[["fii_total_usd_mn"]]
    df = inr.join([idx, med, fii], how="outer").sort_index()
    df.index.name = "year"
    from datetime import datetime
    end_year = datetime.today().year
    start_year = end_year - years_back
    df = df[(df.index >= start_year) & (df.index <= end_year)]
    return df


def plot(df: pd.DataFrame, out_path: str = OUT_PNG) -> None:
    fig, ax_inr = plt.subplots(figsize=(18, 9.5))

    # Axis 1 (left): INR per USD
    c_inr = "#d62728"
    L_inr = ax_inr.plot(
        df.index, df["inr_per_usd"],
        color=c_inr, marker="o", linewidth=2.4,
        label="INR per 1 USD",
    )
    ax_inr.set_xlabel("Year")
    ax_inr.set_ylabel("INR per 1 USD", color=c_inr)
    ax_inr.tick_params(axis="y", labelcolor=c_inr)

    # Axis 2 (right): median constituent close
    ax_med = ax_inr.twinx()
    L_med_50 = ax_med.plot(
        df.index, df["nifty50_median"],
        color="#1f77b4", marker="o", linewidth=1.6, linestyle="--",
        label="Nifty 50 — median constituent close",
    )
    L_med_mid = ax_med.plot(
        df.index, df["midcap_median"],
        color="#2ca02c", marker="s", linewidth=1.6, linestyle="--",
        label="Nifty Midcap 100 — median constituent close",
    )
    L_med_sm = ax_med.plot(
        df.index, df["smallcap_median"],
        color="#ff7f0e", marker="^", linewidth=1.6, linestyle="--",
        label="Nifty Smallcap 100 — median constituent close",
    )
    ax_med.set_ylabel("Median constituent close (INR, dashed lines)",
                      color="#444444")
    ax_med.tick_params(axis="y", labelcolor="#444444")

    # Axis 3 (right, offset): index level
    ax_idx = ax_inr.twinx()
    ax_idx.spines["right"].set_position(("axes", 1.08))
    L_idx_50 = ax_idx.plot(
        df.index, df["nifty50"],
        color="#1f77b4", marker="o", linewidth=2.2,
        label="Nifty 50 — year-end close",
    )
    L_idx_mid = ax_idx.plot(
        df.index, df["nifty_midcap"],
        color="#2ca02c", marker="s", linewidth=2.2,
        label="Nifty Midcap 100 — year-end close",
    )
    L_idx_sm = ax_idx.plot(
        df.index, df["nifty_smallcap"],
        color="#ff7f0e", marker="^", linewidth=2.2,
        label="Nifty/BSE Smallcap — year-end close",
    )
    ax_idx.set_ylabel("Index level (year-end close, solid lines)",
                      color="#222222")
    ax_idx.tick_params(axis="y", labelcolor="#222222")

    # Axis 4 (right, further offset): total FII inflow (USD mn)
    ax_fii = ax_inr.twinx()
    ax_fii.spines["right"].set_position(("axes", 1.16))
    L_fii_tot = ax_fii.plot(
        df.index, df["fii_total_usd_mn"],
        color="#8c564b", marker="P", linewidth=2.4, linestyle=":",
        label="Net FII inflow — total Indian equity (USD mn, CDSL)",
    )
    ax_fii.axhline(0, color="#999999", linewidth=0.8)
    ax_fii.set_ylabel("Net FII inflow (USD millions, dotted line)",
                      color="#8c564b")
    ax_fii.tick_params(axis="y", labelcolor="#8c564b")

    lines = (L_inr + L_idx_50 + L_idx_mid + L_idx_sm
             + L_med_50 + L_med_mid + L_med_sm
             + L_fii_tot)
    labels = [ln.get_label() for ln in lines]
    ax_inr.legend(lines, labels, loc="upper left", framealpha=0.92,
                  fontsize=9)

    plt.title(
        f"INR/USD · Nifty 50 / Midcap / Smallcap index levels · median "
        f"constituent prices · net FII equity inflow — last {YEARS_BACK} years"
    )
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
