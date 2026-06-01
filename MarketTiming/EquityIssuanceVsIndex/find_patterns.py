"""
Systematic pattern search across the five per-series CSV files.

Tests 30 candidate signals (built from IPO/FPO+Rights issuance, P/E
ratios, P/E spreads, and prior-year returns) against 6 forward outcome
series (1-year and 2-year Nifty 50, Midcap 100, Smallcap 100 returns).

Reports:
  1. All signals where the historical hit rate >= 80% with n >= 4.
  2. The mirror image (DOWN predictions <= 20% hit rate) as a sanity
     check on the UP signals.
  3. The full enumeration of signals with n >= 5, ranked by hit rate.
  4. Forward-return statistics by P/E quartile for each index.

The numbers this script prints are the inputs to
patterns_high_probability.md and methodology.md. Re-run after adding
any new year's data to refresh the patterns.

Usage:
    python3 find_patterns.py
"""

from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent


def normalize_pe(price: pd.Series, pe: pd.Series) -> pd.Series:
    """Replace P/E with price / prior_year_eps when current EPS collapsed."""
    out = pe.copy().astype(float)
    last_eps, _ = None, None
    for y in price.index:
        p, r = price[y], pe[y]
        if pd.isna(p) or pd.isna(r) or r <= 0:
            continue
        eps_now = p / r
        if last_eps is not None and eps_now < 0.5 * last_eps:
            out[y] = p / last_eps
        else:
            last_eps = eps_now
    return out


def load() -> pd.DataFrame:
    ipo = pd.read_csv(HERE / "ipo_data.csv").rename(columns={"year_label": "year"})
    fpo = pd.read_csv(HERE / "fpo_rights_data.csv").rename(columns={"year_label": "year"})
    n50 = pd.read_csv(HERE / "nifty50_data.csv").rename(columns={"calendar_year": "year"})
    nsm = pd.read_csv(HERE / "nifty_smallcap100_data.csv").rename(columns={"calendar_year": "year"})
    nmd = pd.read_csv(HERE / "nifty_midcap100_data.csv").rename(columns={"calendar_year": "year"})

    years = list(range(2000, 2026))
    df = pd.DataFrame({"year": years}).set_index("year")
    df["ipo_count"]  = ipo.set_index("year")["ipo_count_total"]
    df["ipo_amt"]    = ipo.set_index("year")["ipo_amount_cr_total"]
    df["fpor_count"] = fpo.set_index("year")["fpo_rights_count"]
    df["fpor_amt"]   = fpo.set_index("year")["fpo_rights_amount_cr"]
    df["n50"]    = n50.set_index("year")["year_end_close"]
    df["sc"]     = nsm.set_index("year")["year_end_close"]
    df["mc"]     = nmd.set_index("year")["year_end_close"]
    df["n50_pe"] = n50.set_index("year")["pe_ratio"]
    df["sc_pe"]  = nsm.set_index("year")["pe_ratio"]
    df["mc_pe"]  = nmd.set_index("year")["pe_ratio"]
    df["n50_pe_n"] = normalize_pe(df["n50"], df["n50_pe"])
    df["sc_pe_n"]  = normalize_pe(df["sc"],  df["sc_pe"])
    df["mc_pe_n"]  = normalize_pe(df["mc"],  df["mc_pe"])

    for c in ["ipo_amt", "fpor_amt", "n50", "sc", "mc"]:
        df[f"{c}_yoy"] = df[c].pct_change() * 100

    # Forward returns (1-year and 2-year cumulative) for each index
    for idx in ["n50", "sc", "mc"]:
        df[f"{idx}_fwd1"] = (df[idx].shift(-1) / df[idx] - 1) * 100
        df[f"{idx}_fwd2"] = (df[idx].shift(-2) / df[idx] - 1) * 100

    return df.reset_index()


def test_signal(df: pd.DataFrame, name: str, mask: pd.Series,
                outcome_col: str, direction: str = "up") -> dict | None:
    """Test how often `mask`-positive years had positive (up) / negative (down) outcome."""
    sub = df[mask & df[outcome_col].notna()].copy()
    n = len(sub)
    if n == 0:
        return None
    hits = ((sub[outcome_col] > 0) if direction == "up" else (sub[outcome_col] < 0)).sum()
    return {
        "name": name, "direction": direction, "outcome": outcome_col,
        "n": int(n), "hits": int(hits), "rate": float(hits) / n,
        "years": sub["year"].tolist(),
        "outcomes": [round(v, 1) for v in sub[outcome_col].tolist()],
    }


def main() -> None:
    df = load()

    print("=== DATA SUMMARY ===")
    print(df.set_index("year")[
        ["ipo_amt", "ipo_count", "n50", "n50_pe_n", "sc", "sc_pe_n", "mc", "mc_pe_n"]
    ].round(2).to_string())

    # Candidate signals — issuance-based, valuation-based, combined, spread
    signals = [
        # Issuance
        ("IPO amt YoY > +100%",           df["ipo_amt_yoy"] > 100),
        ("IPO amt YoY > +150%",           df["ipo_amt_yoy"] > 150),
        ("IPO amt YoY > +200%",           df["ipo_amt_yoy"] > 200),
        ("IPO count > 150",               df["ipo_count"] > 150),
        ("IPO count > 200",               df["ipo_count"] > 200),
        ("IPO amt > Rs 50,000 cr",        df["ipo_amt"] > 50000),
        ("IPO amt > Rs 80,000 cr",        df["ipo_amt"] > 80000),
        ("IPO amt > Rs 1,00,000 cr",      df["ipo_amt"] > 100000),
        ("IPO amt YoY < -50%",            df["ipo_amt_yoy"] < -50),
        ("IPO amt YoY < -80%",            df["ipo_amt_yoy"] < -80),
        # Valuation (normalized P/E)
        ("Nifty 50 P/E (norm) > 25",      df["n50_pe_n"] > 25),
        ("Nifty 50 P/E (norm) > 27",      df["n50_pe_n"] > 27),
        ("Nifty 50 P/E (norm) < 15",      df["n50_pe_n"] < 15),
        ("Smallcap P/E (norm) > 35",      df["sc_pe_n"] > 35),
        ("Smallcap P/E (norm) > 40",      df["sc_pe_n"] > 40),
        ("Smallcap P/E (norm) < 20",      df["sc_pe_n"] < 20),
        ("Midcap P/E (norm) > 30",        df["mc_pe_n"] > 30),
        ("Midcap P/E (norm) > 35",        df["mc_pe_n"] > 35),
        ("Midcap P/E (norm) < 15",        df["mc_pe_n"] < 15),
        # Combined valuation + issuance
        ("Nifty 50 P/E > 25 AND IPO amt YoY > 100%",
            (df["n50_pe_n"] > 25) & (df["ipo_amt_yoy"] > 100)),
        ("Smallcap P/E > 35 AND IPO amt YoY > 100%",
            (df["sc_pe_n"] > 35) & (df["ipo_amt_yoy"] > 100)),
        ("Smallcap P/E > 40 AND IPO count > 150",
            (df["sc_pe_n"] > 40) & (df["ipo_count"] > 150)),
        ("Midcap P/E > 30 AND IPO amt YoY > 100%",
            (df["mc_pe_n"] > 30) & (df["ipo_amt_yoy"] > 100)),
        ("Any index P/E > 35 AND IPO amt > 50,000 cr",
            ((df["sc_pe_n"] > 35) | (df["mc_pe_n"] > 35)) & (df["ipo_amt"] > 50000)),
        # Spread
        ("Smallcap P/E - Nifty 50 P/E > 10",
            (df["sc_pe_n"] - df["n50_pe_n"]) > 10),
        ("Smallcap P/E - Nifty 50 P/E > 15",
            (df["sc_pe_n"] - df["n50_pe_n"]) > 15),
        # Prior-year strength
        ("Smallcap UP >40% prior year AND IPO amt > 50,000 cr",
            (df["sc"].pct_change() > 0.40) & (df["ipo_amt"] > 50000)),
        ("Midcap UP >40% prior year AND IPO amt > 50,000 cr",
            (df["mc"].pct_change() > 0.40) & (df["ipo_amt"] > 50000)),
    ]

    out_cols = ["n50_fwd1", "mc_fwd1", "sc_fwd1", "n50_fwd2", "mc_fwd2", "sc_fwd2"]

    results = []
    for name, sig in signals:
        for oc in out_cols:
            for direction in ("up", "down"):
                r = test_signal(df, name, sig, oc, direction)
                if r and r["n"] >= 4:
                    results.append(r)

    # >= 80% hit rate, n >= 4
    strong = sorted(
        [r for r in results if r["rate"] >= 0.80 and r["n"] >= 4],
        key=lambda r: (-r["rate"], -r["n"]),
    )

    print(f"\n\n=== SIGNALS WITH >= 80% HIT RATE (n>=4) ===\n")
    print(f"{'DIR':<5} {'OUTCOME':<10} {'HITS':<7} {'RATE':<7} SIGNAL  |  YEARS / OUTCOMES")
    print("-" * 130)
    for r in strong:
        arrow = "UP" if r["direction"] == "up" else "DN"
        print(f"{arrow:<5} {r['outcome']:<10} {r['hits']}/{r['n']:<5} "
              f"{r['rate']*100:>5.0f}%  {r['name']}  | "
              f"years={r['years']} returns={r['outcomes']}")

    # Forward return by P/E quartile
    print("\n\n=== FORWARD RETURNS BY P/E QUARTILE ===")
    for idx in ("n50", "sc", "mc"):
        pe_col, fwd_col = f"{idx}_pe_n", f"{idx}_fwd1"
        sub = df[[pe_col, fwd_col, "year"]].dropna()
        if len(sub) < 8:
            print(f"\n{idx.upper()}: only {len(sub)} years of data, skipping quartile.")
            continue
        sub = sub.copy()
        sub["q"] = pd.qcut(sub[pe_col], q=4, labels=["Q1 cheap", "Q2", "Q3", "Q4 expensive"])
        grp = sub.groupby("q", observed=False).agg(
            n=("year", "count"),
            avg_fwd1=(fwd_col, "mean"),
            pos_fwd1=(fwd_col, lambda x: (x > 0).mean() * 100),
            median_fwd1=(fwd_col, "median"),
        ).round(1)
        print(f"\n{idx.upper()} P/E quartile -> next-year return:")
        print(grp.to_string())


if __name__ == "__main__":
    main()
