"""
Build the inlined JSON data payload used by all_series_interactive.html.

Reads the five per-series CSV files in this folder, aligns them to a
single year index (2000-2025), computes YoY % changes, and a normalized
P/E ratio (with the EPS-collapse adjustment), then prints a JSON object
that gets pasted inline into the HTML <script> block as `const DATA = ...`.

Usage:
    python3 build_interactive_data.py > /tmp/all_series_data.json
    # then update the DATA = {...} block in all_series_interactive.html

Why the JSON is inlined into the HTML instead of fetched at runtime:
- file:// URLs in Safari + Chrome block fetch() from disk for security.
- An inlined payload means the HTML works equally well opened directly
  from disk (no web server needed) and served from any origin.

The normalization rule applied here matches the one documented in
patterns_high_probability.md and the *_data_sources.md files:
  if implicit_EPS(year y) < 0.5 * implicit_EPS(prior valid year):
      pe_norm[y] = price[y] / prior_eps
  else:
      pe_norm[y] = pe[y]
This catches COVID-style earnings collapses (Midcap 2020 = 419 -> 30)
without flattening true valuation extremes.
"""

import json
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent


def load_aligned() -> pd.DataFrame:
    ipo = pd.read_csv(HERE / "ipo_data.csv").rename(columns={"year_label": "year"})
    fpo = pd.read_csv(HERE / "fpo_rights_data.csv").rename(columns={"year_label": "year"})
    n50 = pd.read_csv(HERE / "nifty50_data.csv").rename(columns={"calendar_year": "year"})
    nsm = pd.read_csv(HERE / "nifty_smallcap100_data.csv").rename(columns={"calendar_year": "year"})
    nmd = pd.read_csv(HERE / "nifty_midcap100_data.csv").rename(columns={"calendar_year": "year"})

    years = list(range(2000, 2026))
    df = pd.DataFrame({"year": years}).set_index("year")
    df["ipo_count"]   = ipo.set_index("year")["ipo_count_total"]
    df["ipo_amount"]  = ipo.set_index("year")["ipo_amount_cr_total"]
    df["fpor_count"]  = fpo.set_index("year")["fpo_rights_count"]
    df["fpor_amount"] = fpo.set_index("year")["fpo_rights_amount_cr"]
    df["nifty50"]     = n50.set_index("year")["year_end_close"]
    df["smallcap"]    = nsm.set_index("year")["year_end_close"]
    df["midcap"]      = nmd.set_index("year")["year_end_close"]
    df["nifty50_pe"]  = n50.set_index("year")["pe_ratio"]
    df["smallcap_pe"] = nsm.set_index("year")["pe_ratio"]
    df["midcap_pe"]   = nmd.set_index("year")["pe_ratio"]
    return df


def load_ibanks() -> pd.DataFrame:
    """Read investment_banks_data.csv, compute per-company YoY % and basket avg.

    Returns a DataFrame indexed by `year` (2000-2025) with one column per
    company holding YoY % change, plus an 'ibank_basket_yoy' column with
    the equal-weighted average across companies that have a value that year.
    """
    src = HERE / "investment_banks_data.csv"
    raw = pd.read_csv(src).sort_values("calendar_year").reset_index(drop=True)
    company_cols = [c for c in raw.columns if c not in ("calendar_year", "year_end_date")]

    years = list(range(2000, 2026))
    out = pd.DataFrame({"year": years}).set_index("year")

    yoy_only = pd.DataFrame({"year": raw["calendar_year"].astype(int).values})
    for c in company_cols:
        # Short name for the trace (strip the "(Yahoo XXX, INR)" suffix)
        short = c.split(" (")[0]
        yoy_only[short] = (raw[c].astype(float).pct_change() * 100).values
    yoy_only = yoy_only.set_index("year")

    company_short_cols = list(yoy_only.columns)
    out = out.join(yoy_only, how="left")
    out["ibank_basket_yoy"] = out[company_short_cols].mean(axis=1, skipna=True)
    out["ibank_basket_n"]   = out[company_short_cols].notna().sum(axis=1)
    return out


def normalize_pe(price: pd.Series, pe: pd.Series):
    """Return (normalized_pe, flag, note) Series aligned to price's index."""
    out_pe, out_flag, out_note = [], [], []
    last_eps, last_year = None, None
    for y in price.index:
        p, r = price[y], pe[y]
        if pd.isna(p) or pd.isna(r) or r <= 0:
            out_pe.append(None); out_flag.append(False); out_note.append("")
            continue
        eps_now = p / r
        if last_eps is not None and eps_now < 0.5 * last_eps:
            out_pe.append(round(p / last_eps, 2))
            out_flag.append(True)
            out_note.append(
                f"Normalized using {last_year} EPS "
                f"(raw P/E={r:.1f}, raw EPS={eps_now:.1f}, prior EPS={last_eps:.1f})"
            )
        else:
            out_pe.append(round(r, 2))
            out_flag.append(False)
            out_note.append("")
            last_eps, last_year = eps_now, y
    return out_pe, out_flag, out_note


def main() -> None:
    df = load_aligned()
    for c in ["ipo_amount", "fpor_amount", "nifty50", "smallcap", "midcap"]:
        df[f"{c}_yoy"] = (df[c].pct_change() * 100).round(2)

    n50_norm, n50_flag, n50_note = normalize_pe(df["nifty50"],  df["nifty50_pe"])
    sc_norm,  sc_flag,  sc_note  = normalize_pe(df["smallcap"], df["smallcap_pe"])
    mc_norm,  mc_flag,  mc_note  = normalize_pe(df["midcap"],   df["midcap_pe"])

    ibanks = load_ibanks()
    ibank_company_cols = [c for c in ibanks.columns if c not in ("ibank_basket_yoy", "ibank_basket_n")]
    df = df.join(ibanks, how="left")

    df = df.reset_index()
    col = lambda name: [None if pd.isna(v) else float(v) for v in df[name].tolist()]

    payload = {
        "years": df["year"].astype(int).tolist(),
        "ipo_count":      col("ipo_count"),
        "ipo_amount":     col("ipo_amount"),
        "fpor_count":     col("fpor_count"),
        "fpor_amount":    col("fpor_amount"),
        "nifty50":        col("nifty50"),
        "smallcap":       col("smallcap"),
        "midcap":         col("midcap"),
        "ipo_amount_yoy": col("ipo_amount_yoy"),
        "fpor_amount_yoy":col("fpor_amount_yoy"),
        "nifty50_yoy":    col("nifty50_yoy"),
        "smallcap_yoy":   col("smallcap_yoy"),
        "midcap_yoy":     col("midcap_yoy"),
        "nifty50_pe_raw":   col("nifty50_pe"),
        "smallcap_pe_raw":  col("smallcap_pe"),
        "midcap_pe_raw":    col("midcap_pe"),
        "nifty50_pe_norm":  n50_norm,
        "smallcap_pe_norm": sc_norm,
        "midcap_pe_norm":   mc_norm,
        "nifty50_pe_norm_flag":  n50_flag,
        "smallcap_pe_norm_flag": sc_flag,
        "midcap_pe_norm_flag":   mc_flag,
        "nifty50_pe_norm_note":  n50_note,
        "smallcap_pe_norm_note": sc_note,
        "midcap_pe_norm_note":   mc_note,
        "ibank_basket_yoy":      [None if pd.isna(v) else round(float(v), 2) for v in df["ibank_basket_yoy"].tolist()],
        "ibank_basket_n":        [None if pd.isna(v) else int(v) for v in df["ibank_basket_n"].tolist()],
        "ibank_companies":       ibank_company_cols,
        "ibank_company_yoy":     {c: [None if pd.isna(v) else round(float(v), 2) for v in df[c].tolist()] for c in ibank_company_cols},
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
