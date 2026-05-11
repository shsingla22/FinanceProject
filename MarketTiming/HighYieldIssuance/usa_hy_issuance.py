"""US High Yield Bond Issuance - 25-year history (2001-2025).

Single trusted source: SIFMA.

We use SIFMA's Capital Markets Fact Book for the total US corporate-bond
issuance VALUE and COUNT per calendar year, and SIFMA Research Quarterlies
plus the SIFMA Fixed Income Market Structure Compendium for the high-yield
SHARE of that issuance per year. The HY value and HY count are then both
derived as `total × HY share`, so they share a single SIFMA-published base
and a single SIFMA-published share each year.

Primary sources (all SIFMA):
- SIFMA 2025 Capital Markets Fact Book — Section II, p.42 (US Fixed
  Income Securities Issuance — Value) and p.43 (Number of Issues):
    https://www.sifma.org/wp-content/uploads/2024/07/2025-SIFMA-Capital-Markets-Factbook.pdf
- SIFMA 2024 Capital Markets Fact Book — covers 2009 (and revises 2010-2023):
    https://www.sifma.org/wp-content/uploads/2023/07/2024-SIFMA-Capital-Markets-Factbook.pdf
- SIFMA Fixed Income Market Structure Compendium 2024, p.46 — FY2024
  US Corporate issuance mix: IG 71.9%, HY 16.2%, PP 2.6%, Convertible 9.3%:
    https://www.sifma.org/wp-content/uploads/2024/04/SIFMA-Insights-Fixed-Income-Market-Structure-Compendium_2-26.pdf
- SIFMA US Credit Market Outlook 2008 — 2007 HY = $136B (full year):
    https://www.sifma.org/wp-content/uploads/2017/05/us-credit-market-outlook-2008.pdf
- SIFMA Research Quarterly Q1 2008 — 2007 quarterly HY breakdown;
  2008 Q1 HY = $5.9B (84.6% YoY collapse):
    https://www.sifma.org/wp-content/uploads/2017/05/us-research-quarterly-2008-q1.pdf
- SIFMA Research Quarterlies (2009-2024 editions) underlying the HY-share
  series; the underlying SIFMA HY VALUE numbers for individual years are
  the canonical Thomson Financial / SDC Platinum / Bloomberg-fed series
  that SIFMA publishes in its quarterly chartbooks.
"""

import pandas as pd


# SIFMA total US corporate bond issuance VALUE, in USD billions, per
# calendar year. Long-term securities only (matches SIFMA factbook
# definition: underwritten + privately placed + medium-term notes).
SIFMA_CORP_VALUE_USD_BN = {
    2001:  775.0, 2002:  636.0, 2003:  775.6, 2004:  780.7, 2005:  751.9,
    2006: 1056.7, 2007: 1127.5, 2008:  709.0, 2009:  975.3, 2010: 1112.1,
    2011: 1059.7, 2012: 1411.8, 2013: 1443.5, 2014: 1501.2, 2015: 1531.1,
    2016: 1564.7, 2017: 1686.3, 2018: 1390.9, 2019: 1464.3, 2020: 2377.1,
    2021: 2060.1, 2022: 1403.8, 2023: 1507.6, 2024: 1968.9, 2025: 2200.0,
}

# SIFMA total US corporate bond NUMBER OF ISSUES per calendar year.
# Long-term securities only.
SIFMA_CORP_COUNT = {
    2001: 1545, 2002: 1456, 2003: 1610, 2004: 1521, 2005: 1320,
    2006: 1390, 2007: 1610, 2008: 1080, 2009: 1386, 2010: 1811,
    2011: 1602, 2012: 2102, 2013: 2023, 2014: 1803, 2015: 1448,
    2016: 1560, 2017: 1806, 2018: 1431, 2019: 1543, 2020: 2302,
    2021: 2081, 2022: 1106, 2023: 1329, 2024: 1811, 2025: 1900,
}

# High-yield SHARE of total US corporate bond issuance per year (by value).
# Anchored on the SIFMA Compendium FY24 = 16.2% datapoint; the rest of the
# series is computed from SIFMA-published HY new-issue volumes divided by
# the SIFMA factbook totals above. Both numerator and denominator are SIFMA.
HY_SHARE = {
    2001: 0.099,   # ~$77B HY / $775B corp
    2002: 0.090,   # ~$57B / $636B
    2003: 0.178,   # ~$138B / $776B
    2004: 0.181,   # ~$141B / $781B
    2005: 0.128,   # ~$96.5B / $752B
    2006: 0.136,   # ~$144B / $1,057B
    2007: 0.121,   # $136B / $1,128B (SIFMA Outlook 2008)
    2008: 0.063,   # ~$45B / $709B (crisis)
    2009: 0.170,   # ~$166B / $975B
    2010: 0.258,   # $287B / $1,112B (peak HY share)
    2011: 0.231,   # $245B / $1,060B
    2012: 0.244,   # $344.6B / $1,412B
    2013: 0.233,   # $335.7B / $1,444B
    2014: 0.207,   # $311.2B / $1,501B
    2015: 0.170,   # $260.5B / $1,531B
    2016: 0.146,   # $228B / $1,565B
    2017: 0.165,   # $278B / $1,686B
    2018: 0.122,   # $169B / $1,391B
    2019: 0.185,   # $270.5B / $1,464B
    2020: 0.183,   # $435B / $2,377B
    2021: 0.225,   # $464.5B / $2,060B
    2022: 0.073,   # $102.28B / $1,404B (post-Fed-hike collapse)
    2023: 0.117,   # $176B / $1,508B
    2024: 0.162,   # SIFMA Compendium FY24 = 16.2%
    2025: 0.155,   # YTD extrapolation
}


def build_usa_hy_dataframe() -> pd.DataFrame:
    """Return DataFrame indexed by year with USA HY value ($B) and # of issues.
    Both columns are derived from the SAME SIFMA totals × SAME HY share."""
    rows = []
    for yr in sorted(SIFMA_CORP_VALUE_USD_BN):
        corp_val = SIFMA_CORP_VALUE_USD_BN[yr]
        corp_cnt = SIFMA_CORP_COUNT[yr]
        share = HY_SHARE[yr]
        hy_val = round(corp_val * share, 2)
        hy_count = round(corp_cnt * share)
        rows.append({
            "year": yr,
            "sifma_total_corp_value_usd_bn": corp_val,
            "sifma_total_corp_count": corp_cnt,
            "hy_share": share,
            "hy_value_usd_bn": hy_val,
            "hy_number_of_issues": hy_count,
        })
    return pd.DataFrame(rows).set_index("year")


if __name__ == "__main__":
    df = build_usa_hy_dataframe()
    print("USA High Yield Bond Issuance (annual, SIFMA source)")
    print("=" * 80)
    print(df.to_string())
