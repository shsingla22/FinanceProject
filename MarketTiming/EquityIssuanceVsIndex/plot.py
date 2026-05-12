"""
Equity issuance vs index — Indian market, last 25 years.

Reads data.csv and renders all eight requested series on a single figure
with multiple y-axes. Missing values (NaN) are drawn as gaps in the lines
rather than imputed, so the chart is faithful to the underlying data
provenance documented in sources.md.

Series plotted (all on the same chart, one shared x-axis = year):
  1. Yearly cumulative amount of fresh capital raised through IPOs (INR cr)
  2. Yearly number of IPOs
  3. Yearly cumulative amount raised through FPOs (INR cr)
  4. Yearly number of FPOs
  5. Yearly value of Nifty 50 (year-end close)
  6. Yearly value of Nifty Smallcap 100 (year-end close)
  7. Yearly value of Nifty Midcap 100 (year-end close)
  8. Yearly median of Nifty Smallcap 100 constituent year-end closing prices
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
CSV = HERE / "data.csv"
OUT = HERE / "equity_issuance_vs_index.png"


def load() -> pd.DataFrame:
    df = pd.read_csv(CSV)
    df = df.sort_values("year").reset_index(drop=True)
    return df


def plot(df: pd.DataFrame) -> None:
    fig, ax_amount = plt.subplots(figsize=(16, 9))
    ax_count = ax_amount.twinx()
    ax_index = ax_amount.twinx()
    ax_index.spines["right"].set_position(("outward", 70))

    x = df["year"]

    amt_lines = [
        ax_amount.plot(
            x, df["ipo_amount_cr"], marker="o", linewidth=2,
            color="#1f77b4", label="IPO amount raised (INR cr)",
        )[0],
        ax_amount.plot(
            x, df["fpo_amount_cr"], marker="s", linewidth=2,
            color="#17becf", label="FPO amount raised (INR cr)",
        )[0],
    ]

    cnt_lines = [
        ax_count.plot(
            x, df["ipo_count"], marker="^", linewidth=2, linestyle="--",
            color="#ff7f0e", label="Number of IPOs",
        )[0],
        ax_count.plot(
            x, df["fpo_count"], marker="v", linewidth=2, linestyle="--",
            color="#d62728", label="Number of FPOs",
        )[0],
    ]

    idx_lines = [
        ax_index.plot(
            x, df["nifty50_close"], marker="D", linewidth=2,
            color="#2ca02c", label="Nifty 50 (year-end close)",
        )[0],
        ax_index.plot(
            x, df["nifty_midcap100_close"], marker="P", linewidth=2,
            color="#9467bd", label="Nifty Midcap 100 (year-end close)",
        )[0],
        ax_index.plot(
            x, df["nifty_smallcap100_close"], marker="X", linewidth=2,
            color="#8c564b", label="Nifty Smallcap 100 (year-end close)",
        )[0],
        ax_index.plot(
            x, df["nifty_smallcap100_constituent_median"],
            marker="*", linewidth=2, color="#e377c2",
            label="Nifty Smallcap 100 constituent median (year-end)",
        )[0],
    ]

    ax_amount.set_xlabel("Year")
    ax_amount.set_ylabel("Amount raised (INR crore)", color="#1f77b4")
    ax_count.set_ylabel("Number of issues", color="#ff7f0e")
    ax_index.set_ylabel("Index / price level", color="#2ca02c")

    ax_amount.tick_params(axis="y", labelcolor="#1f77b4")
    ax_count.tick_params(axis="y", labelcolor="#ff7f0e")
    ax_index.tick_params(axis="y", labelcolor="#2ca02c")

    ax_amount.set_xticks(x)
    ax_amount.set_xticklabels(x, rotation=45)
    ax_amount.grid(True, alpha=0.3)

    ax_amount.set_title(
        "Equity issuance vs broad-market indices — India, 2001–2025\n"
        "(Year-end closes; mainboard+SME IPO/FPO issuance; gaps = unverified)",
        fontsize=13,
    )

    lines = amt_lines + cnt_lines + idx_lines
    labels = [ln.get_label() for ln in lines]
    ax_amount.legend(
        lines, labels, loc="upper left", fontsize=9, framealpha=0.9,
    )

    fig.tight_layout()
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    plot(load())
