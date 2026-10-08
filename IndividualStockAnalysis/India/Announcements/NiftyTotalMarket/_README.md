# NiftyTotalMarket — restructuring filings (spin-offs, demergers, schemes)

**Generated:** 2026-10-08 04:59 UTC
**Window:** the 365 days to 2026-10-08 · **Universe:** 750 official
NiftyTotalMarket constituents · **Rows:** 1023 filings across 256 companies

## What is here
- `_announcements_restructuring.csv` — one row per exchange filing that
  classifies as a restructuring event: `date, symbol, company, source
  (NSE | BSE-RSS | BSE-screener), category, kind, tags, headline,
  attachment, ann_id, file_size, text_file`.
- `text/` — the attachment's extracted text, `{SYMBOL}_{ann_id}.txt`.
- `_bse_codes.csv` — symbol → BSE scrip code and screener id.
- `_bse_rss_snapshots.csv` — BSE's daily RSS, accumulated run over run.
- `_fetch_log.csv` — what each run did.

## Kinds (first matching tag wins; all tags kept in `tags`)
- `merger`: 371
- `scheme_other`: 286
- `capital_reduction`: 133
- `rights_issue`: 122
- `demerger`: 71
- `slump_sale`: 35
- `subsidiary_listing`: 5

## Sources, honestly
NSE's corporate-announcements API is read month by month for the whole
exchange and filtered to the universe — this is the complete one-year
record, since every member is NSE-listed and Regulation 30 disclosures
go to both exchanges. BSE's announcement API refuses this environment
(Akamai), so BSE is covered by its daily RSS feed (accumulating forward
from the first run) and by the BSE-sourced per-company lists on
screener.in; BSE attachment PDFs download normally.

Re-run: `python3 ../fetch_announcements.py` (adds, never duplicates).
