"""Entry point: build datasets and render all four charts.

Each chart is saved twice:
  * a static PNG (matplotlib) for printable / read-only viewing, and
  * an interactive HTML (plotly) where you can click legend entries to
    toggle lines and drag the range slider / quick-pick buttons to
    change the year window.
"""
import plot_inr_usd
import plot_indices
import plot_medians
import plot_combined
import plot_interactive


def main() -> None:
    print("=" * 72)
    print("Chart 1: INR vs USD")
    print("=" * 72)
    df1 = plot_inr_usd.build_dataset()
    df1.to_csv(plot_inr_usd.OUT_CSV)
    print(df1.to_string())
    plot_inr_usd.plot(df1)

    print()
    print("=" * 72)
    print("Chart 2: Nifty 50 / Midcap / Smallcap year-end levels")
    print("=" * 72)
    df2 = plot_indices.build_dataset()
    df2.to_csv(plot_indices.OUT_CSV)
    print(df2.to_string())
    plot_indices.plot(df2)

    print()
    print("=" * 72)
    print("Chart 3: Median constituent price by index")
    print("=" * 72)
    df3 = plot_medians.build_dataset()
    df3.to_csv(plot_medians.OUT_CSV)
    print(df3.to_string())
    plot_medians.plot(df3)

    print()
    print("=" * 72)
    print("Chart 4: All seven series combined")
    print("=" * 72)
    df4 = plot_combined.build_dataset()
    df4.to_csv(plot_combined.OUT_CSV)
    print(df4.to_string())
    plot_combined.plot(df4)

    print()
    print("=" * 72)
    print("Interactive HTML versions of all four charts")
    print("=" * 72)
    plot_interactive.render_all()


if __name__ == "__main__":
    main()
