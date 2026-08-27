"""
test_skill.py — tests for the StockToIndexPriceEarningsRatio skill.

Covers the saved index series (shape, spans, sanity of magnitudes), the
fiscal-year mapping, ratio arithmetic against hand-computed values, and
full report generation for the ten companies the skill is run on —
including the degraded-but-honest path for a company with stale
statements (COLPAL).

Run from this folder:  python3 -m pytest test_skill.py -q
"""

from pathlib import Path

import pandas as pd
import pytest

import analyze

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"

TOP10 = ["COLPAL", "APOLLOHOSP", "PIDILITIND", "CAPLIPOINT", "TRITURBINE",
         "VIJAYA", "CAMS", "LALPATHLAB", "THELEELA", "GILLETTE"]
FULL_CHART_SYMS = [s for s in TOP10 if s != "COLPAL"]


# ------------------------------------------------------------ index data

def test_price_yearly_has_15_fiscal_years():
    df = pd.read_csv(DATA / "nifty50_price_yearly.csv")
    assert len(df) == 15
    assert df.fy.iloc[0] == "Mar 2012" and df.fy.iloc[-1] == "Mar 2026"
    # index levels must be plausible and strictly positive
    assert (df.close > 1000).all() and (df.close < 100000).all()


def test_price_monthly_covers_every_fiscal_march():
    m = pd.read_csv(DATA / "nifty50_price_monthly.csv")
    marches = m[m.month_num == 3].year.tolist()
    for y in range(2012, 2027):
        assert y in marches, f"no March close for {y}"


def test_constituents_are_a_plausible_nifty50():
    c = pd.read_csv(DATA / "nifty50_constituents.csv")
    assert 45 <= len(c) <= 50
    for anchor in ("RELIANCE", "HDFCBANK", "TCS", "INFY", "ITC"):
        assert anchor in set(c.nse_symbol), f"{anchor} missing"


def test_earnings_yearly_span_and_magnitude():
    e = pd.read_csv(DATA / "nifty50_earnings_yearly.csv")
    assert e.fy.iloc[0] == "Mar 2015" and e.fy.iloc[-1] == "Mar 2026"
    assert (e.pat_companies >= 40).all()
    # Nifty 50 aggregate PAT is lakhs of crores, growing over the window
    assert e.index_pat.iloc[0] > 100000
    assert e.index_pat.iloc[-1] > e.index_pat.iloc[0]
    assert (e.index_op >= e.index_pat * 0.8).all()  # OP >= ~PAT in aggregate


# ------------------------------------------------------- fiscal-year map

@pytest.mark.parametrize("label,fy", [
    ("Mar 2024", "Mar 2024"),
    ("Jun 2024", "Mar 2025"),
    ("Dec 2024", "Mar 2025"),
    ("Sep 2015", "Mar 2016"),
    ("Jan 2020", "Mar 2020"),
])
def test_fy_mapping(label, fy):
    assert analyze.fy_of(label) == fy


# ------------------------------------------------------ ratio arithmetic

def test_price_ratio_matches_hand_computation():
    prices = analyze.company_prices("PIDILITIND")
    label, px = prices["Mar 2026"]
    assert label == "Mar 2026"
    monthly = pd.read_csv(DATA / "nifty50_price_monthly.csv")
    idx = analyze.index_close_for(monthly, "Mar 2026")
    report = analyze.build_report("PIDILITIND")
    expected = f"{px / idx * 1000:.3f}"
    assert expected in report


def test_pat_ratio_matches_hand_computation():
    earn = analyze.company_earnings("PIDILITIND")
    e = pd.read_csv(DATA / "nifty50_earnings_yearly.csv").set_index("fy")
    expected = earn["Mar 2026"]["pat"] / e.loc["Mar 2026", "index_pat"] * 100
    assert f"{expected:.3f}%" in analyze.build_report("PIDILITIND")


def test_gillette_june_book_close_maps_into_fiscal_years():
    # GILLETTE closes its books in June: its stored P&L year "Jun 2015"
    # must land in fiscal year "Mar 2016", and the earnings ratios must
    # therefore exist for FY2016 even though no "Mar 2016" statement exists
    earn = analyze.company_earnings("GILLETTE")
    assert "Mar 2016" in earn and "pat" in earn["Mar 2016"]
    # and the monthly index series can serve non-March labels too
    monthly = pd.read_csv(DATA / "nifty50_price_monthly.csv")
    assert analyze.index_close_for(monthly, "Jun 2024") is not None


# ------------------------------------------------------- report contract

@pytest.mark.parametrize("sym", TOP10)
def test_report_generates_without_error(tmp_path, sym):
    out = tmp_path / f"{sym}.md"
    out.write_text(analyze.build_report(sym))
    md = out.read_text()
    assert "Stock vs Nifty 50" in md
    assert "## 1. Price ratio" in md
    assert "## 2. PAT ratio" in md
    assert "## 3. Operating-profit ratio" in md


@pytest.mark.parametrize("sym", FULL_CHART_SYMS)
def test_full_data_companies_get_all_three_charts(sym):
    md = analyze.build_report(sym)
    # every section must contain a real chart (a bar row), not the
    # no-data placeholder
    for section in ("## 1.", "## 2.", "## 3."):
        chunk = md.split(section, 1)[1].split("## ", 1)[0]
        assert "█" in chunk, f"{sym}: no chart bars under {section}"
    assert "no overlapping years" not in md


def test_colpal_degrades_honestly():
    md = analyze.build_report("COLPAL")
    # price data exists (FY2015..FY2026) -> price chart present
    price_chunk = md.split("## 1.", 1)[1].split("## 2.", 1)[0]
    assert "█" in price_chunk
    # stored P&L stops at FY2010 -> earnings charts must say so, not guess
    pat_chunk = md.split("## 2.", 1)[1].split("## 3.", 1)[0]
    assert "no overlapping years" in pat_chunk
    assert "could not cover" in md


def test_trend_windows_table_and_arithmetic():
    rows = [(f"Mar {y}", float(v)) for y, v in
            zip(range(2011, 2027), range(10, 26))]      # FY2011..FY2026
    table = analyze.trend_windows(rows)
    # 15y: 10 -> 25 = +150% ; 1y: 24 -> 25 = +4%
    assert "| last 15 years | FY2011 | FY2026 | +150% |" in table
    assert "| last 1 year | FY2025 | FY2026 | +4% |" in table
    for w in (15, 10, 5, 3, 1):
        assert f"last {w} year" in table


def test_trend_windows_reports_na_when_data_starts_late():
    md = analyze.build_report("PIDILITIND")
    assert "| last 15 years | FY2011 | FY2026 | n/a — data starts FY2015 |" in md
    assert "| last 10 years | FY2016 | FY2026 |" in md


def test_trend_windows_handles_sign_flip():
    rows = [("Mar 2025", -1.0), ("Mar 2026", 2.0)]
    assert "turned from loss to profit share" in analyze.trend_windows(rows)


def test_yoy_series_matches_hand_computation():
    rows = [("Mar 2024", 2.0), ("Mar 2025", 3.0), ("Mar 2026", 1.5)]
    s = analyze.yoy_series(rows)
    assert s == {2025: pytest.approx(50.0), 2026: pytest.approx(-50.0)}


@pytest.mark.parametrize("sym", FULL_CHART_SYMS)
def test_line_graph_in_file_with_point_values(sym):
    md = analyze.build_report(sym)
    assert "## 4. Yearly change of all three ratios" in md
    sec4 = md.split("## 4.", 1)[1].split("## 5.", 1)[0]
    # the graph lives inside the SAME md file, in a code fence
    graph = sec4.split("```", 2)[1]
    # THELEELA listed in FY2026, so it has a single price point and no
    # price YoY line — its graph honestly carries the two earnings lines
    expected = ["T = PAT ratio", "O = Operating-profit ratio"]
    if sym != "THELEELA":
        expected.insert(0, "P = Price ratio")
    for leg in expected:
        assert leg in graph, f"{sym}: legend missing {leg}"
    # every graph must carry the value-at-every-point table, and each
    # tabled value must equal the hand-computed YoY change
    assert "The value at every point of the graph" in sec4
    pat_yoy = analyze.yoy_series(
        _ratio_rows_for(sym, "pat"))
    for year, v in pat_yoy.items():
        assert f"| FY{year} |" in sec4
        assert f"{v:+.1f}%" in sec4


def _ratio_rows_for(sym: str, kind: str):
    """Recompute a ratio series exactly as the report does."""
    earn = analyze.company_earnings(sym)
    idx = pd.read_csv(DATA / "nifty50_earnings_yearly.csv").set_index("fy")
    rows = []
    for fy in idx.index:
        e = earn.get(fy, {})
        if kind in e and idx.loc[fy, f"index_{kind}"]:
            rows.append((fy, e[kind] / idx.loc[fy, f"index_{kind}"] * 100))
    return rows


def test_line_graph_degrades_for_colpal():
    # COLPAL has no earnings overlap; the price-only series still has
    # years, so the graph must include exactly the price line
    md = analyze.build_report("COLPAL")
    sec4 = md.split("## 4.", 1)[1].split("## 5.", 1)[0]
    graph = sec4.split("```", 2)[1]
    assert "P = Price ratio" in graph
    assert "T = PAT ratio" not in graph


# ------------------------------------------------------- raw value table

def test_raw_values_table_matches_source_csvs():
    md = analyze.build_report("PIDILITIND")
    assert "## 5. The raw yearly values behind every ratio" in md
    sec5 = md.split("## 5.", 1)[1]
    # company price straight from StockInfo
    info = pd.read_csv(analyze.STOCKINFO / "PIDILITIND.csv")
    px = float(info[info.metric == "Stock Price (Rs)"].iloc[0]["Mar 2026"])
    # index close straight from the saved yearly file
    idx_px = float(pd.read_csv(DATA / "nifty50_price_yearly.csv")
                   .set_index("fy").loc["Mar 2026", "close"])
    # company PAT/OP straight from the long profit-and-loss
    pl = pd.read_csv(analyze.PL_LONG)
    pl = pl[(pl.nse_symbol == "PIDILITIND") & (pl.year == "Mar 2026")]
    pat = float(pl[pl.line_item == "Net Profit"].value.iloc[0])
    op = float(pl[pl.line_item == "Operating Profit"].value.iloc[0])
    # index PAT/OP straight from the saved earnings file
    ie = pd.read_csv(DATA / "nifty50_earnings_yearly.csv").set_index("fy")
    row = [l for l in sec5.splitlines() if l.startswith("| FY2026 ")][0]
    for expected in (f"{px:,.2f}", f"{idx_px:,.2f}", f"{pat:,.0f}",
                     f"{op:,.0f}", f"{ie.loc['Mar 2026', 'index_pat']:,.0f}",
                     f"{ie.loc['Mar 2026', 'index_op']:,.0f}"):
        assert expected in row, f"{expected} not in FY2026 raw row: {row}"


def test_raw_values_table_marks_missing_as_dash():
    md = analyze.build_report("COLPAL")
    sec5 = md.split("## 5.", 1)[1]
    row = [l for l in sec5.splitlines() if l.startswith("| FY2026 ")][0]
    # price, index close and index profits present; the two COMPANY
    # profit cells (P&L stale after FY2010) are honest dashes
    assert row.count("—") == 2
    assert "1,788.70" in row and "23,997.55" in row


def test_raw_values_table_notes_non_march_book_close():
    md = analyze.build_report("GILLETTE")
    sec5 = md.split("## 5.", 1)[1]
    assert "(Jun" not in sec5.split("\n")[0]  # header clean
    # GILLETTE prices are March snapshots, so no bracket needed there;
    # every data row must have 7 columns
    for l in sec5.splitlines():
        if l.startswith("| FY"):
            assert l.count("|") == 8


def test_chart_never_exceeds_15_points():
    for sym in TOP10:
        md = analyze.build_report(sym)
        for chunk in md.split("```")[1::2]:      # inside code fences
            rows = [l for l in chunk.splitlines() if l.startswith("FY")]
            assert len(rows) <= 15
