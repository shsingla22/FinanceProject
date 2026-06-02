"""
Systematic pattern search across US IPO, index, and DXY data (2000-2025).

Reads the five CSV files in this folder and tests candidate signals
against forward outcomes. Reports patterns with hit rate >= 80%, n >= 4.

Outcomes scored: 1y / 2y forward S&P 500, S&P 400, Russell 2000 returns,
plus 1y forward IPO proceeds YoY % and 1y forward DXY YoY %.

Usage:
    python3 find_patterns_us.py > /tmp/us_patterns.txt
"""

from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent


def load():
    ipo = pd.read_csv(HERE / "us_ipo_data.csv")
    sp500 = pd.read_csv(HERE / "sp500_data.csv")[
        ["calendar_year", "year_end_close", "pe_ratio_trailing"]
    ].rename(columns={"year_end_close": "sp500", "pe_ratio_trailing": "sp500_pe"})
    sp400 = pd.read_csv(HERE / "sp_midcap400_data.csv")[
        ["calendar_year", "year_end_close"]
    ].rename(columns={"year_end_close": "sp400"})
    rut = pd.read_csv(HERE / "russell2000_data.csv")[
        ["calendar_year", "year_end_close"]
    ].rename(columns={"year_end_close": "rut"})
    dxy = pd.read_csv(HERE / "usd_index_data.csv")[
        ["calendar_year", "dxy_close", "dxy_yoy_pct"]
    ].rename(columns={"dxy_close": "dxy", "dxy_yoy_pct": "dxy_yoy"})

    df = (ipo.merge(sp500, on="calendar_year")
              .merge(sp400, on="calendar_year")
              .merge(rut,   on="calendar_year")
              .merge(dxy,   on="calendar_year"))
    df = df.sort_values("calendar_year").reset_index(drop=True)
    df = df.set_index("calendar_year")

    # YoY % for index levels and IPO proceeds
    df["sp500_yoy"]    = df["sp500"].pct_change() * 100
    df["sp400_yoy"]    = df["sp400"].pct_change() * 100
    df["rut_yoy"]      = df["rut"].pct_change() * 100
    df["proceeds_yoy"] = df["ipo_proceeds_total_usd_mn"].pct_change() * 100
    df["corp_proceeds_yoy"] = df["ipo_proceeds_corporate_usd_mn"].pct_change() * 100

    # Forward outcomes
    for col in ["sp500", "sp400", "rut"]:
        df[f"{col}_fwd1"] = (df[col].shift(-1) / df[col] - 1) * 100
        df[f"{col}_fwd2"] = (df[col].shift(-2) / df[col] - 1) * 100

    df["proceeds_fwd1_yoy"] = df["proceeds_yoy"].shift(-1)
    df["dxy_fwd1_yoy"]      = df["dxy_yoy"].shift(-1)

    return df.reset_index()


def test_signal(df, name, mask, outcome_col, direction="up"):
    sub = df[mask & df[outcome_col].notna()]
    n = len(sub)
    if n == 0:
        return None
    hits = ((sub[outcome_col] > 0) if direction == "up" else (sub[outcome_col] < 0)).sum()
    return dict(
        name=name, direction=direction, outcome=outcome_col,
        n=int(n), hits=int(hits), rate=float(hits) / n,
        avg=float(sub[outcome_col].mean()),
        years=sub["calendar_year"].tolist(),
        outs=[round(v, 1) for v in sub[outcome_col].tolist()],
    )


def build_signals(df):
    sig = []

    # --- A: Issuance signals ---
    sig += [
        ("IPO total count > 300",            df["ipo_count_total"] > 300),
        ("IPO total count > 400",            df["ipo_count_total"] > 400),
        ("IPO total count < 150",            df["ipo_count_total"] < 150),
        ("IPO corporate count > 200",        df["ipo_count_corporate"] > 200),
        ("IPO corporate count < 100",        df["ipo_count_corporate"] < 100),
        ("IPO total proceeds > $80B",        df["ipo_proceeds_total_usd_mn"] > 80000),
        ("IPO total proceeds > $100B",       df["ipo_proceeds_total_usd_mn"] > 100000),
        ("IPO total proceeds > $200B",       df["ipo_proceeds_total_usd_mn"] > 200000),
        ("IPO total proceeds < $30B",        df["ipo_proceeds_total_usd_mn"] < 30000),
        ("IPO proceeds YoY > +100%",         df["proceeds_yoy"] > 100),
        ("IPO proceeds YoY > +200%",         df["proceeds_yoy"] > 200),
        ("IPO proceeds YoY < -50%",          df["proceeds_yoy"] < -50),
        ("IPO proceeds YoY < -80%",          df["proceeds_yoy"] < -80),
    ]

    # --- B: SPAC-specific signals ---
    sig += [
        ("SPAC count > 100",                 df["ipo_count_spac"] > 100),
        ("SPAC count > 200 (mania)",         df["ipo_count_spac"] > 200),
        ("SPAC count > 500 (extreme mania)", df["ipo_count_spac"] > 500),
        ("SPAC proceeds > $50B",             df["ipo_proceeds_spac_usd_mn"] > 50000),
        ("SPAC count = 0 (pre-SPAC era)",    df["ipo_count_spac"] == 0),
    ]

    # --- C: S&P 500 valuation signals (full coverage) ---
    sig += [
        ("S&P 500 P/E < 17 (cheap)",         df["sp500_pe"] < 17),
        ("S&P 500 P/E < 20",                 df["sp500_pe"] < 20),
        ("S&P 500 P/E > 25 (stretched)",     df["sp500_pe"] > 25),
        ("S&P 500 P/E > 30 (very stretched)",df["sp500_pe"] > 30),
        ("S&P 500 P/E > 40 (earnings collapse era)", df["sp500_pe"] > 40),
    ]

    # --- D: Index momentum signals ---
    sig += [
        ("S&P 500 YoY > +20% (big rally)",   df["sp500_yoy"] > 20),
        ("S&P 500 YoY > +25%",               df["sp500_yoy"] > 25),
        ("S&P 500 YoY < -10% (drawdown)",    df["sp500_yoy"] < -10),
        ("S&P 500 YoY < -20% (bear market)", df["sp500_yoy"] < -20),
        ("S&P 400 YoY > +25%",               df["sp400_yoy"] > 25),
        ("S&P 400 YoY < -15%",               df["sp400_yoy"] < -15),
        ("Russell 2000 YoY > +25%",          df["rut_yoy"] > 25),
        ("Russell 2000 YoY < -20%",          df["rut_yoy"] < -20),
        ("Russell 2000 beats S&P 500 by >5pp",
            (df["rut_yoy"] - df["sp500_yoy"]) > 5),
        ("Russell 2000 lags S&P 500 by >5pp",
            (df["sp500_yoy"] - df["rut_yoy"]) > 5),
    ]

    # --- E: DXY (US Dollar Index) signals ---
    sig += [
        ("DXY YoY > +10% (USD strong shock)",  df["dxy_yoy"] > 10),
        ("DXY YoY > +5% (USD strong)",         df["dxy_yoy"] > 5),
        ("DXY YoY < -10% (USD weak shock)",    df["dxy_yoy"] < -10),
        ("DXY YoY < -5% (USD weak)",           df["dxy_yoy"] < -5),
        ("DXY YoY < 0% (USD weakens)",         df["dxy_yoy"] < 0),
        ("DXY YoY stable (-3% to +3%)",
            (df["dxy_yoy"] > -3) & (df["dxy_yoy"] < 3)),
        ("DXY level > 100 (strong USD regime)", df["dxy"] > 100),
        ("DXY level < 80 (weak USD regime)",    df["dxy"] < 80),
    ]

    # --- F: Combined cross-asset signals ---
    sig += [
        ("IPO proceeds > $100B AND DXY YoY < 0",
            (df["ipo_proceeds_total_usd_mn"] > 100000) & (df["dxy_yoy"] < 0)),
        ("SPAC count > 100 AND DXY YoY < 0",
            (df["ipo_count_spac"] > 100) & (df["dxy_yoy"] < 0)),
        ("S&P 500 P/E > 25 AND DXY YoY > 0",
            (df["sp500_pe"] > 25) & (df["dxy_yoy"] > 0)),
        ("S&P 500 P/E < 17 AND IPO proceeds YoY < 0",
            (df["sp500_pe"] < 17) & (df["proceeds_yoy"] < 0)),
        ("Russell 2000 YoY < -15% AND IPO proceeds YoY < -50%",
            (df["rut_yoy"] < -15) & (df["proceeds_yoy"] < -50)),
        ("DXY YoY > +5% AND IPO proceeds YoY < -50%",
            (df["dxy_yoy"] > 5) & (df["proceeds_yoy"] < -50)),
        ("S&P 500 YoY > +25% AND IPO proceeds > $80B",
            (df["sp500_yoy"] > 25) & (df["ipo_proceeds_total_usd_mn"] > 80000)),
        ("All three indices DOWN in same year",
            (df["sp500_yoy"] < 0) & (df["sp400_yoy"] < 0) & (df["rut_yoy"] < 0)),
        ("All three indices UP > +20% (boom)",
            (df["sp500_yoy"] > 20) & (df["sp400_yoy"] > 20) & (df["rut_yoy"] > 20)),
        ("Smallcaps lead AND IPO proceeds > $80B",
            ((df["rut_yoy"] - df["sp500_yoy"]) > 5) & (df["ipo_proceeds_total_usd_mn"] > 80000)),
    ]

    return sig


def main():
    df = load()

    print("=== DATA SUMMARY (key cols) ===")
    cols = ["ipo_count_total", "ipo_count_corporate", "ipo_count_spac",
            "ipo_proceeds_total_usd_mn", "sp500", "sp500_pe", "sp400", "rut",
            "dxy", "dxy_yoy"]
    print(df.set_index("calendar_year")[cols].round(2).to_string())

    signals = build_signals(df)
    out_cols = [
        "sp500_fwd1", "sp400_fwd1", "rut_fwd1",
        "sp500_fwd2", "sp400_fwd2", "rut_fwd2",
        "proceeds_fwd1_yoy", "dxy_fwd1_yoy",
    ]

    results = []
    for name, mask in signals:
        for oc in out_cols:
            for direction in ("up", "down"):
                r = test_signal(df, name, mask, oc, direction)
                if r and r["n"] >= 4:
                    results.append(r)

    strong = sorted(
        [r for r in results if r["rate"] >= 0.80 and r["n"] >= 4],
        key=lambda r: (-r["rate"], -r["n"], -abs(r["avg"])),
    )

    print(f"\n\n=== >= 80% HIT RATE, n >= 4 — {len(strong)} found ===")
    print(f"{'DIR':<4} {'OUTCOME':<20} {'HIT':<8} {'RATE':<6} {'AVG':<8}  SIGNAL")
    print("-" * 160)
    for r in strong:
        arrow = "UP" if r["direction"] == "up" else "DN"
        print(f"{arrow:<4} {r['outcome']:<20} {r['hits']}/{r['n']:<6} "
              f"{r['rate']*100:>4.0f}% {r['avg']:>+7.1f}%  {r['name']}  | yrs={r['years']} out={r['outs']}")

    perfect = [r for r in strong if r["rate"] == 1.0]
    print(f"\n\n=== PERFECT 100% (n >= 4) — {len(perfect)} found ===")
    for r in perfect:
        arrow = "UP" if r["direction"] == "up" else "DN"
        print(f"{arrow:<4} {r['outcome']:<20} {r['hits']}/{r['n']:<6} avg {r['avg']:>+7.1f}%  {r['name']}")

    # Correlations
    print("\n\n=== KEY CORRELATIONS ===")
    pairs = [
        ("sp500_yoy", "sp400_yoy"), ("sp500_yoy", "rut_yoy"), ("sp400_yoy", "rut_yoy"),
        ("dxy_yoy", "sp500_yoy"), ("dxy_yoy", "rut_yoy"),
        ("proceeds_yoy", "sp500_yoy"), ("proceeds_yoy", "rut_yoy"),
        ("ipo_count_spac", "sp500_yoy"),
        ("sp500_pe", "sp500_fwd1"), ("sp500_pe", "sp500_fwd2"),
        ("dxy_yoy", "proceeds_fwd1_yoy"),
        ("sp500_yoy", "proceeds_fwd1_yoy"),
    ]
    for a, b in pairs:
        sub = df[[a, b]].dropna()
        if len(sub) < 3:
            continue
        c = sub[a].corr(sub[b])
        print(f"  corr({a:>22}, {b:>22}) = {c:+.3f}  (n={len(sub)})")

    # Quartile views
    print("\n\n=== S&P 500 P/E QUARTILE -> NEXT-YEAR S&P 500 RETURN ===")
    sub = df[["sp500_pe", "sp500_fwd1", "calendar_year"]].dropna()
    if len(sub) >= 8:
        sub = sub.copy()
        sub["q"] = pd.qcut(sub["sp500_pe"], q=4, labels=["Q1 cheap", "Q2", "Q3", "Q4 expensive"])
        grp = sub.groupby("q", observed=False).agg(
            n=("calendar_year", "count"),
            avg=("sp500_fwd1", "mean"),
            pos_rate=("sp500_fwd1", lambda x: (x > 0).mean() * 100),
            years=("calendar_year", lambda x: list(x.astype(int))),
        ).round(1)
        print(grp.to_string())

    print("\n\n=== DXY YOY QUARTILE -> NEXT-YEAR S&P 500 RETURN ===")
    sub = df[["dxy_yoy", "sp500_fwd1", "calendar_year"]].dropna()
    if len(sub) >= 8:
        sub = sub.copy()
        sub["q"] = pd.qcut(sub["dxy_yoy"], q=4, labels=["Q1 USD weak", "Q2", "Q3", "Q4 USD strong"])
        grp = sub.groupby("q", observed=False).agg(
            n=("calendar_year", "count"),
            avg=("sp500_fwd1", "mean"),
            pos_rate=("sp500_fwd1", lambda x: (x > 0).mean() * 100),
            years=("calendar_year", lambda x: list(x.astype(int))),
        ).round(1)
        print(grp.to_string())

    print("\n\n=== DXY YOY QUARTILE -> NEXT-YEAR RUSSELL 2000 RETURN ===")
    sub = df[["dxy_yoy", "rut_fwd1", "calendar_year"]].dropna()
    if len(sub) >= 8:
        sub = sub.copy()
        sub["q"] = pd.qcut(sub["dxy_yoy"], q=4, labels=["Q1 USD weak", "Q2", "Q3", "Q4 USD strong"])
        grp = sub.groupby("q", observed=False).agg(
            n=("calendar_year", "count"),
            avg=("rut_fwd1", "mean"),
            pos_rate=("rut_fwd1", lambda x: (x > 0).mean() * 100),
            years=("calendar_year", lambda x: list(x.astype(int))),
        ).round(1)
        print(grp.to_string())

    print("\n\n=== IPO PROCEEDS QUARTILE -> NEXT-YEAR S&P 500 ===")
    sub = df[["ipo_proceeds_total_usd_mn", "sp500_fwd1", "calendar_year"]].dropna()
    if len(sub) >= 8:
        sub = sub.copy()
        sub["q"] = pd.qcut(sub["ipo_proceeds_total_usd_mn"], q=4, labels=["Q1 low", "Q2", "Q3", "Q4 high"])
        grp = sub.groupby("q", observed=False).agg(
            n=("calendar_year", "count"),
            avg=("sp500_fwd1", "mean"),
            pos_rate=("sp500_fwd1", lambda x: (x > 0).mean() * 100),
            years=("calendar_year", lambda x: list(x.astype(int))),
        ).round(1)
        print(grp.to_string())


if __name__ == "__main__":
    main()
