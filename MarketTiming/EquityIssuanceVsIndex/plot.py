"""
Equity issuance vs index — Indian market, last 25 years.

Reads data.csv and renders all requested series on a single figure with
three y-axes. Missing values (NaN) are drawn as gaps in the lines rather
than imputed, so the chart is faithful to the underlying data provenance
documented in sources.md.

Series plotted (all on the same chart, one shared x-axis = year):
  Issuance amounts (left y-axis, INR crore)
    1. IPO amount raised
    2. FPO amount raised
    3. Total capital raised in equity primary market (IPO+FPO+Rights+QIP+Pref)
  Issue counts (right y-axis, count)
    4. Number of IPOs
    5. Number of FPOs
  Index levels (far-right y-axis)
    6. Nifty 50 year-end close
    7. Nifty Midcap 100 year-end close
    8. Nifty Smallcap 100 year-end close
    9. Median of Nifty Smallcap 100 constituent year-end prices
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
CSV = HERE / "data.csv"
OUT = HERE / "equity_issuance_vs_index.png"


def load() -> pd.DataFrame:
    return pd.read_csv(CSV).sort_values("year").reset_index(drop=True)


def plot(df: pd.DataFrame) -> None:
    fig, ax_amt = plt.subplots(figsize=(18, 10))
    ax_cnt = ax_amt.twinx()
    ax_idx = ax_amt.twinx()
    ax_idx.spines["right"].set_position(("outward", 80))

    x = df["year"]

    amt_lines = [
        ax_amt.plot(x, df["ipo_amount_cr"], marker="o", linewidth=2,
                    color="#1f77b4", label="IPO amount raised (INR cr)")[0],
        ax_amt.plot(x, df["fpo_amount_cr"], marker="s", linewidth=2,
                    color="#17becf", label="FPO amount raised (INR cr)")[0],
        ax_amt.plot(x, df["total_capital_raised_cr"], marker="h", linewidth=2.5,
                    color="#000000",
                    label="Total equity capital raised — primary market (INR cr)")[0],
    ]

    cnt_lines = [
        ax_cnt.plot(x, df["ipo_count"], marker="^", linewidth=2, linestyle="--",
                    color="#ff7f0e", label="Number of IPOs")[0],
        ax_cnt.plot(x, df["fpo_count"], marker="v", linewidth=2, linestyle="--",
                    color="#d62728", label="Number of FPOs")[0],
    ]

    idx_lines = [
        ax_idx.plot(x, df["nifty50_close"], marker="D", linewidth=2,
                    color="#2ca02c", label="Nifty 50 (year-end close)")[0],
        ax_idx.plot(x, df["nifty_midcap100_close"], marker="P", linewidth=2,
                    color="#9467bd",
                    label="Nifty Midcap 100 (year-end close)")[0],
        ax_idx.plot(x, df["nifty_smallcap100_close"], marker="X", linewidth=2,
                    color="#8c564b",
                    label="Nifty Smallcap 100 (year-end close)")[0],
        ax_idx.plot(x, df["nifty_smallcap100_constituent_median"],
                    marker="*", linewidth=2, color="#e377c2",
                    label="Nifty Smallcap 100 constituent median price")[0],
    ]

    ax_amt.set_xlabel("Year (FY ending Mar for 2001-2020; CY Jan-Dec for 2021-2025)")
    ax_amt.set_ylabel("Capital raised (INR crore)", color="#1f77b4")
    ax_cnt.set_ylabel("Number of issues", color="#ff7f0e")
    ax_idx.set_ylabel("Index / price level", color="#2ca02c")

    ax_amt.tick_params(axis="y", labelcolor="#1f77b4")
    ax_cnt.tick_params(axis="y", labelcolor="#ff7f0e")
    ax_idx.tick_params(axis="y", labelcolor="#2ca02c")

    ax_amt.set_xticks(x)
    ax_amt.set_xticklabels(x, rotation=45)
    ax_amt.grid(True, alpha=0.3)

    ax_amt.set_title(
        "Equity issuance vs broad-market indices — India, 2001–2025\n"
        "Sources: SEBI Handbooks of Statistics; SEBI Bulletin (Oct 2025); "
        "PRIME Database via Business Standard/KPMG; NSE Nifty year-end closes",
        fontsize=12,
    )

    lines = amt_lines + cnt_lines + idx_lines
    labels = [ln.get_label() for ln in lines]
    ax_amt.legend(lines, labels, loc="upper left", fontsize=9, framealpha=0.9)

    fig.tight_layout()
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    plot(load())
