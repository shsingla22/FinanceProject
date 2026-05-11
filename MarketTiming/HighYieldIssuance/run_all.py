"""Entry point: build datasets and render both charts.

The default window is 25 years. Pass an integer to plot_usa.build_dataset /
plot_india.build_dataset to override.
"""
import plot_usa
import plot_india


def main() -> None:
    print("=" * 70)
    print("Building USA dataset and chart...")
    print("=" * 70)
    df_usa = plot_usa.build_dataset(years_back=plot_usa.YEARS_BACK)
    df_usa.to_csv(plot_usa.OUT_CSV)
    print(df_usa.to_string())
    plot_usa.plot(df_usa)

    print()
    print("=" * 70)
    print("Building India dataset and chart...")
    print("=" * 70)
    df_in = plot_india.build_dataset(years_back=plot_india.YEARS_BACK)
    df_in.to_csv(plot_india.OUT_CSV)
    print(df_in.to_string())
    plot_india.plot(df_in)


if __name__ == "__main__":
    main()
