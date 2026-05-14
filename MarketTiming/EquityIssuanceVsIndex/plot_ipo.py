"""
Line graph of yearly IPO count and yearly IPO amount raised, sourced
exclusively from ipo_data.csv (SEBI Handbooks + SEBI monthly bulletins).

Covers FY 2001-02 through FY 2024-25, no gaps.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
CSV = HERE / "ipo_data.csv"
OUT = HERE / "ipo_count_vs_amount.png"


def plot() -> None:
    df = pd.read_csv(CSV).sort_values("fiscal_year").reset_index(drop=True)

    fig, ax_count = plt.subplots(figsize=(16, 8))
    ax_amount = ax_count.twinx()

    x = df["fiscal_year"]

    line_count = ax_count.plot(
        x, df["ipo_count_total"], marker="o", linewidth=2,
        color="#ff7f0e", label="Number of IPOs (mainboard + SME)",
    )[0]
    line_amount = ax_amount.plot(
        x, df["ipo_amount_cr_total"], marker="s", linewidth=2,
        color="#1f77b4", label="IPO amount raised (INR crore)",
    )[0]

    ax_count.set_xlabel("Fiscal year")
    ax_count.set_ylabel("Number of IPOs", color="#ff7f0e")
    ax_amount.set_ylabel("Amount raised (INR crore)", color="#1f77b4")
    ax_count.tick_params(axis="y", labelcolor="#ff7f0e")
    ax_amount.tick_params(axis="y", labelcolor="#1f77b4")

    ax_count.set_xticks(range(len(x)))
    ax_count.set_xticklabels(x, rotation=45)
    ax_count.grid(True, alpha=0.3)

    ax_count.set_title(
        "Indian IPO market — yearly count and amount raised, FY 2001-02 to FY 2024-25\n"
        "Source: SEBI Handbooks of Statistics + SEBI Monthly Bulletin Annexure Tables",
        fontsize=12,
    )

    ax_count.legend(
        [line_count, line_amount],
        [line_count.get_label(), line_amount.get_label()],
        loc="upper left", fontsize=10, framealpha=0.95,
    )

    fig.tight_layout()
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    plot()
