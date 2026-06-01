"""
Extended pattern search — v2.

Adds to the original find_patterns.py:
  - Two new signal sources: I-banking basket YoY % (from
    investment_banks_data.csv) and USD/INR year-end + YoY %
    (from usd_inr_data.csv).
  - Two new forward outcomes: 1-year I-banking basket return,
    and 1-year IPO amount (CY-shifted by 1 — does signal X
    predict the next year's IPO supply?).
  - Three-way combined signals (issuance + valuation + FX +
    I-bank flow).

Filter (same as v1): >= 80% hit rate AND n >= 4.

Usage:
    python3 find_patterns_v2.py > /tmp/patterns_v2_run.txt
"""

from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent


def normalize_pe(price: pd.Series, pe: pd.Series) -> pd.Series:
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

    # USD/INR
    fx = pd.read_csv(HERE / "usd_inr_data.csv").sort_values("calendar_year").reset_index(drop=True)
    df["usd_inr"]      = fx.set_index("calendar_year")["year_end_close_inr_per_usd"]
    df["usd_inr_yoy"]  = df["usd_inr"].pct_change() * 100

    # I-banking basket — equal-weighted YoY % across all listed companies that year
    ib = pd.read_csv(HERE / "investment_banks_data.csv").sort_values("calendar_year").reset_index(drop=True)
    company_cols = [c for c in ib.columns if c not in ("calendar_year", "year_end_date")]
    ib_yoy = pd.DataFrame({"year": ib["calendar_year"].astype(int).values})
    for c in company_cols:
        ib_yoy[c] = (ib[c].astype(float).pct_change() * 100).values
    ib_yoy = ib_yoy.set_index("year")
    df["ib_basket_yoy"] = ib_yoy.mean(axis=1, skipna=True)
    df["ib_basket_n"]   = ib_yoy.notna().sum(axis=1)

    # YoY % for headline series
    for c in ["ipo_amt", "fpor_amt", "n50", "sc", "mc"]:
        df[f"{c}_yoy"] = df[c].pct_change() * 100

    # Forward outcomes (1-year cumulative; also 2-year for indices)
    for idx in ["n50", "sc", "mc"]:
        df[f"{idx}_fwd1"] = (df[idx].shift(-1) / df[idx] - 1) * 100
        df[f"{idx}_fwd2"] = (df[idx].shift(-2) / df[idx] - 1) * 100

    # Forward I-banking basket (next-year basket YoY %)
    df["ib_fwd1"]     = df["ib_basket_yoy"].shift(-1)
    # Forward IPO amount YoY % (next year's IPO YoY)
    df["ipo_amt_fwd1_yoy"] = df["ipo_amt_yoy"].shift(-1)
    # Forward USD/INR YoY
    df["fx_fwd1_yoy"] = df["usd_inr_yoy"].shift(-1)

    return df.reset_index()


def test_signal(df: pd.DataFrame, name: str, mask: pd.Series,
                outcome_col: str, direction: str = "up") -> dict | None:
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
        "avg_outcome": float(sub[outcome_col].mean()),
        "median_outcome": float(sub[outcome_col].median()),
    }


def build_signals(df):
    """Return list of (name, mask) — 60+ candidate signals."""
    sig = []

    # --- Section A: Issuance signals (same as v1) ---
    sig += [
        ("IPO amt YoY > +100%",       df["ipo_amt_yoy"] > 100),
        ("IPO amt YoY > +150%",       df["ipo_amt_yoy"] > 150),
        ("IPO amt YoY > +200%",       df["ipo_amt_yoy"] > 200),
        ("IPO count > 150",           df["ipo_count"] > 150),
        ("IPO count > 200",           df["ipo_count"] > 200),
        ("IPO amt > Rs 50,000 cr",    df["ipo_amt"] > 50000),
        ("IPO amt > Rs 80,000 cr",    df["ipo_amt"] > 80000),
        ("IPO amt > Rs 1,00,000 cr",  df["ipo_amt"] > 100000),
        ("IPO amt YoY < -50%",        df["ipo_amt_yoy"] < -50),
        ("IPO amt YoY < -80%",        df["ipo_amt_yoy"] < -80),
    ]

    # --- Section B: Valuation signals (same as v1) ---
    sig += [
        ("Nifty 50 P/E (norm) > 25",  df["n50_pe_n"] > 25),
        ("Nifty 50 P/E (norm) > 27",  df["n50_pe_n"] > 27),
        ("Nifty 50 P/E (norm) < 17",  df["n50_pe_n"] < 17),
        ("Smallcap P/E (norm) > 35",  df["sc_pe_n"] > 35),
        ("Smallcap P/E (norm) > 40",  df["sc_pe_n"] > 40),
        ("Smallcap P/E (norm) < 25",  df["sc_pe_n"] < 25),
        ("Midcap P/E (norm) > 30",    df["mc_pe_n"] > 30),
        ("Midcap P/E (norm) > 35",    df["mc_pe_n"] > 35),
        ("Midcap P/E (norm) < 15",    df["mc_pe_n"] < 15),
    ]

    # --- Section C: USD/INR signals (NEW) ---
    sig += [
        ("INR depreciates > +5% YoY",   df["usd_inr_yoy"] > 5),
        ("INR depreciates > +10% YoY",  df["usd_inr_yoy"] > 10),
        ("INR depreciates > +15% YoY",  df["usd_inr_yoy"] > 15),
        ("INR appreciates (USD/INR YoY < 0)",  df["usd_inr_yoy"] < 0),
        ("INR appreciates > -5% YoY",   df["usd_inr_yoy"] < -5),
        ("INR stable (-3% < USD/INR YoY < +3%)",
            (df["usd_inr_yoy"] > -3) & (df["usd_inr_yoy"] < 3)),
    ]

    # --- Section D: I-banking basket signals (NEW) ---
    sig += [
        ("I-bank basket YoY > +50%",   df["ib_basket_yoy"] > 50),
        ("I-bank basket YoY > +100%",  df["ib_basket_yoy"] > 100),
        ("I-bank basket YoY > +150%",  df["ib_basket_yoy"] > 150),
        ("I-bank basket YoY < 0%",     df["ib_basket_yoy"] < 0),
        ("I-bank basket YoY < -25%",   df["ib_basket_yoy"] < -25),
        ("I-bank basket YoY < -40%",   df["ib_basket_yoy"] < -40),
    ]

    # --- Section E: Combined valuation + issuance (same as v1) ---
    sig += [
        ("Nifty 50 P/E > 25 AND IPO amt YoY > 100%",
            (df["n50_pe_n"] > 25) & (df["ipo_amt_yoy"] > 100)),
        ("Smallcap P/E > 35 AND IPO amt YoY > 100%",
            (df["sc_pe_n"] > 35) & (df["ipo_amt_yoy"] > 100)),
        ("Midcap P/E > 30 AND IPO amt YoY > 100%",
            (df["mc_pe_n"] > 30) & (df["ipo_amt_yoy"] > 100)),
        ("Any index P/E > 35 AND IPO amt > 50,000 cr",
            ((df["sc_pe_n"] > 35) | (df["mc_pe_n"] > 35)) & (df["ipo_amt"] > 50000)),
        ("Smallcap P/E - Nifty 50 P/E > 10",
            (df["sc_pe_n"] - df["n50_pe_n"]) > 10),
    ]

    # --- Section F: NEW combined signals (FX + issuance + I-bank) ---
    sig += [
        # INR weakness + supply surge
        ("INR depreciates > +5% AND IPO amt > 50,000 cr",
            (df["usd_inr_yoy"] > 5) & (df["ipo_amt"] > 50000)),
        ("INR depreciates > +10% AND IPO amt > 50,000 cr",
            (df["usd_inr_yoy"] > 10) & (df["ipo_amt"] > 50000)),
        # INR strength + cheap valuation
        ("INR appreciates AND Nifty 50 P/E < 20",
            (df["usd_inr_yoy"] < 0) & (df["n50_pe_n"] < 20)),
        # I-bank surge as forward proxy
        ("I-bank basket > +100% (boom signal)",
            df["ib_basket_yoy"] > 100),
        ("I-bank basket > +100% AND IPO amt > 50,000 cr (heat signal)",
            (df["ib_basket_yoy"] > 100) & (df["ipo_amt"] > 50000)),
        # I-bank capitulation
        ("I-bank basket < -25% (capitulation)",
            df["ib_basket_yoy"] < -25),
        ("I-bank basket < -25% AND IPO amt YoY < -50%",
            (df["ib_basket_yoy"] < -25) & (df["ipo_amt_yoy"] < -50)),
        # I-bank basket as next-year IPO supply leading indicator
        ("I-bank basket > +50% (lead for issuance)",
            df["ib_basket_yoy"] > 50),
        # FX + valuation combined
        ("INR depreciates > +5% AND Smallcap P/E > 35",
            (df["usd_inr_yoy"] > 5) & (df["sc_pe_n"] > 35)),
        # IPO drought + INR weak (post-shock pattern)
        ("IPO amt YoY < -50% AND INR weak (USD/INR YoY > 0)",
            (df["ipo_amt_yoy"] < -50) & (df["usd_inr_yoy"] > 0)),
        # Triple-signal "everything stretched"
        ("Midcap P/E > 30 AND IPO amt > 50,000 cr AND I-bank > +50%",
            (df["mc_pe_n"] > 30) & (df["ipo_amt"] > 50000) & (df["ib_basket_yoy"] > 50)),
        # Triple-signal "everything dirt cheap"
        ("Nifty 50 P/E < 17 AND IPO amt YoY < 0 AND I-bank < 0",
            (df["n50_pe_n"] < 17) & (df["ipo_amt_yoy"] < 0) & (df["ib_basket_yoy"] < 0)),
    ]

    return sig


def main():
    df = load()

    print("=== DATA SUMMARY (key columns; rows=year) ===")
    cols = ["ipo_amt", "ipo_count", "n50", "n50_pe_n", "sc_pe_n", "mc_pe_n",
            "usd_inr", "usd_inr_yoy", "ib_basket_yoy", "ib_basket_n"]
    print(df.set_index("year")[cols].round(2).to_string())

    signals = build_signals(df)
    out_cols_index = ["n50_fwd1", "mc_fwd1", "sc_fwd1", "n50_fwd2", "mc_fwd2", "sc_fwd2"]
    out_cols_other = ["ib_fwd1", "ipo_amt_fwd1_yoy", "fx_fwd1_yoy"]
    out_cols = out_cols_index + out_cols_other

    results = []
    for name, mask in signals:
        for oc in out_cols:
            for direction in ("up", "down"):
                r = test_signal(df, name, mask, oc, direction)
                if r and r["n"] >= 4:
                    results.append(r)

    # >= 80% AND n >= 4
    strong = sorted(
        [r for r in results if r["rate"] >= 0.80 and r["n"] >= 4],
        key=lambda r: (-r["rate"], -r["n"], -abs(r["avg_outcome"])),
    )

    print(f"\n\n=== SIGNALS WITH >= 80% HIT RATE (n >= 4) — {len(strong)} found ===")
    print(f"{'DIR':<5} {'OUTCOME':<18} {'HIT':<8} {'RATE':<7} {'AVG':<8} SIGNAL  |  YEARS / RETURNS")
    print("-" * 160)
    for r in strong:
        arrow = "UP" if r["direction"] == "up" else "DN"
        print(f"{arrow:<5} {r['outcome']:<18} {r['hits']}/{r['n']:<6} "
              f"{r['rate']*100:>5.0f}%  {r['avg_outcome']:>+6.1f}%  {r['name']}  | "
              f"yrs={r['years']} out={r['outcomes']}")

    # 100% signals only
    perfect = [r for r in strong if r["rate"] == 1.0]
    print(f"\n\n=== 100% PERFECT SIGNALS (n >= 4) — {len(perfect)} found ===")
    for r in perfect:
        arrow = "UP" if r["direction"] == "up" else "DN"
        print(f"{arrow:<5} {r['outcome']:<18} {r['hits']}/{r['n']:<6} "
              f"avg {r['avg_outcome']:>+6.1f}%  {r['name']}")

    # Cross-correlations (simple)
    print("\n\n=== KEY CORRELATIONS (Pearson, on overlapping years) ===")
    corr_pairs = [
        ("ib_basket_yoy", "n50_yoy"),       ("ib_basket_yoy", "mc_yoy"),
        ("ib_basket_yoy", "sc_yoy"),
        ("ib_basket_yoy", "ipo_amt_fwd1_yoy"),  # forward IPO supply
        ("usd_inr_yoy",  "n50_yoy"),        ("usd_inr_yoy", "ib_basket_yoy"),
        ("usd_inr_yoy",  "sc_yoy"),         ("ipo_amt_yoy", "ib_basket_yoy"),
        ("ipo_amt",      "usd_inr"),        ("n50", "usd_inr"),
    ]
    for a, b in corr_pairs:
        sub = df[[a, b]].dropna()
        if len(sub) < 3:
            continue
        c = sub[a].corr(sub[b])
        print(f"  corr({a:>22}, {b:>22}) = {c:+.3f}  (n={len(sub)})")

    # I-bank basket quartile -> forward Nifty 50
    print("\n\n=== I-BANK BASKET QUARTILE -> NEXT-YEAR NIFTY 50 ===")
    sub = df[["ib_basket_yoy", "n50_fwd1", "year"]].dropna()
    if len(sub) >= 8:
        sub = sub.copy()
        sub["q"] = pd.qcut(sub["ib_basket_yoy"], q=4,
                           labels=["Q1 capitulation", "Q2", "Q3", "Q4 mania"])
        grp = sub.groupby("q", observed=False).agg(
            n=("year", "count"),
            avg_fwd1=("n50_fwd1", "mean"),
            pos_rate=("n50_fwd1", lambda x: (x > 0).mean() * 100),
            sample_years=("year", lambda x: list(x.astype(int))),
        ).round(1)
        print(grp.to_string())

    # USD/INR YoY quartile -> forward Nifty 50
    print("\n\n=== USD/INR YOY QUARTILE -> NEXT-YEAR NIFTY 50 ===")
    sub = df[["usd_inr_yoy", "n50_fwd1", "year"]].dropna()
    if len(sub) >= 8:
        sub = sub.copy()
        sub["q"] = pd.qcut(sub["usd_inr_yoy"], q=4,
                           labels=["Q1 INR strong", "Q2", "Q3", "Q4 INR weak"])
        grp = sub.groupby("q", observed=False).agg(
            n=("year", "count"),
            avg_fwd1=("n50_fwd1", "mean"),
            pos_rate=("n50_fwd1", lambda x: (x > 0).mean() * 100),
            sample_years=("year", lambda x: list(x.astype(int))),
        ).round(1)
        print(grp.to_string())


if __name__ == "__main__":
    main()
