# NIFTY Total Market — constituents

**Generated:** 2026-06-04 05:36:52 UTC

**Universe:** the ~750 cos that comprise the NSE NIFTY TOTAL MARKET index (Nifty 500 ∪ Nifty Microcap 250).

## Files
- `niftytotalmarket_constituents.csv` — `nse_symbol, company_name, industry, series, isin`
- `_fetch_log.csv` — provenance of ISIN & name per company
- `fetch_constituents.py` — re-runnable fetcher

## Data source chain
Because NSE's own index CSVs (niftyindices.com / nseindia.com archives) are WAF-blocked from headless clients, the script uses:

1. **screener.in** `/company/NFTYTOTMKT/` (paginated) for the constituent universe (NSE symbols).
2. **Groww** instruments master (`growwapi-assets.groww.in/instruments/instrument.csv`) for the ISIN and canonical company name. Groww's CSV is publicly downloadable and updated daily by Groww.
3. **Local Nifty500 master** (`../Nifty500/nifty500_constituents.csv`) for the longer proper-cased company names and industry tags (used preferentially where present).

## Reproducibility
`python3 fetch_constituents.py`
