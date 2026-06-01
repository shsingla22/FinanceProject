"""
Plot US IPO annual statistics — counts and proceeds across 2000-2025.

Reads us_ipo_data.csv (SEC DERA source) and renders a multi-axis line
chart with:
  - Left axis: IPO counts (total, corporate, SPAC)
  - Right axis: IPO gross proceeds in $ billions (total, corporate, SPAC)

Output: us_ipo_combined.png

Usage:
    python3 plot_us_ipo.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
OUT = HERE / "us_ipo_combined.png"


def load() -> pd.DataFrame:
    df = pd.read_csv(HERE / "us_ipo_data.csv")
    # Convert proceeds from $M to $B for chart readability
    for c in ["ipo_proceeds_total_usd_mn", "ipo_proceeds_corporate_usd_mn",
              "ipo_proceeds_spac_usd_mn", "ipo_proceeds_fund_usd_mn"]:
        df[c.replace("_mn", "_bn")] = df[c] / 1000
    return df


def plot(df: pd.DataFrame) -> None:
    fig, ax_count = plt.subplots(figsize=(20, 11))
    ax_amount = ax_count.twinx()

    x = df["calendar_year"]

    # --- Counts on left axis ---
    cnt_lines = [
        ax_count.plot(x, df["ipo_count_total"], marker="o", linewidth=2.5,
                      color="#1f77b4", label="(1) Total IPO count")[0],
        ax_count.plot(x, df["ipo_count_corporate"], marker="^", linewidth=2,
                      color="#2ca02c", label="(2) Corporate IPO count (operating cos.)")[0],
        ax_count.plot(x, df["ipo_count_spac"], marker="s", linewidth=2,
                      color="#d62728", label="(3) SPAC IPO count")[0],
        ax_count.plot(x, df["ipo_count_fund"], marker="x", linewidth=1.5,
                      color="#8c564b", label="(4) Closed-end fund / BDC IPO count")[0],
    ]

    # --- Proceeds in $ billions on right axis ---
    amt_lines = [
        ax_amount.plot(x, df["ipo_proceeds_total_usd_bn"], marker="D", linewidth=2.5,
                       color="#ff7f0e", linestyle="--",
                       label="(5) Total IPO proceeds ($ B)")[0],
        ax_amount.plot(x, df["ipo_proceeds_corporate_usd_bn"], marker="P", linewidth=2,
                       color="#17becf", linestyle="--",
                       label="(6) Corporate IPO proceeds ($ B)")[0],
        ax_amount.plot(x, df["ipo_proceeds_spac_usd_bn"], marker="*", linewidth=2,
                       color="#e377c2", linestyle="--",
                       label="(7) SPAC IPO proceeds ($ B)")[0],
    ]

    # --- Axes formatting ---
    ax_count.set_xlabel("Calendar year", fontsize=12)
    ax_count.set_ylabel("Number of IPOs", color="#1f77b4", fontsize=12)
    ax_amount.set_ylabel("Gross proceeds (US$ billions)",
                         color="#ff7f0e", fontsize=12)
    ax_count.tick_params(axis="y", labelcolor="#1f77b4")
    ax_amount.tick_params(axis="y", labelcolor="#ff7f0e")

    ax_count.set_xticks(x)
    ax_count.set_xticklabels(x, rotation=45)
    ax_count.grid(True, alpha=0.3)

    # --- Annotate the two extreme years ---
    ax_count.annotate(
        "2021: SPAC mania peak\n1,078 IPOs / $303B",
        xy=(2021, 1078), xytext=(2017.5, 950),
        fontsize=10, color="#d62728",
        arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.2),
    )
    ax_count.annotate(
        "2008: GFC freeze\n60 IPOs / $29B",
        xy=(2008, 60), xytext=(2009.5, 250),
        fontsize=10, color="#444",
        arrowprops=dict(arrowstyle="->", color="#444", lw=1.0),
    )
    ax_count.annotate(
        "2000: dotcom peak\n459 IPOs / $84B",
        xy=(2000, 459), xytext=(2001, 700),
        fontsize=10, color="#444",
        arrowprops=dict(arrowstyle="->", color="#444", lw=1.0),
    )
    ax_count.annotate(
        "2022: post-Fed-hike freeze\n202 IPOs / $22B",
        xy=(2022, 202), xytext=(2023, 450),
        fontsize=10, color="#444",
        arrowprops=dict(arrowstyle="->", color="#444", lw=1.0),
    )

    fig.suptitle(
        "U.S. IPO market — yearly counts and gross proceeds by issuer type, CY 2000-2025\n"
        "Source: U.S. SEC Division of Economic and Risk Analysis (DERA), "
        "Initial Public Offerings Statistics dataset (released March 17, 2026)\n"
        "https://www.sec.gov/data-research/statistics-data-visualizations/initial-public-offerings-ipos",
        fontsize=12, y=0.995,
    )

    lines = cnt_lines + amt_lines
    labels = [ln.get_label() for ln in lines]
    ax_count.legend(lines, labels, loc="upper left", fontsize=10,
                    framealpha=0.92, ncol=2)

    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    plot(load())
