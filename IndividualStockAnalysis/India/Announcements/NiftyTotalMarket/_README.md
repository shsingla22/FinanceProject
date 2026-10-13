# NiftyTotalMarket — restructuring filings (spin-offs, demergers, schemes)

**Generated:** 2026-10-13 03:45 UTC
**Window:** the 370 days to 2026-10-13 · **Universe:** 750 official
NiftyTotalMarket constituents · **Rows:** 1494 filings across 343 companies

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
- `merger`: 426
- `scheme_other`: 295
- `preferential_issue`: 241
- `rights_issue`: 191
- `capital_reduction`: 184
- `demerger`: 87
- `slump_sale`: 59
- `subsidiary_listing`: 11

## Sources, honestly
NSE's corporate-announcements API is read month by month for the whole
exchange and filtered to the universe — this is the complete one-year
record, since every member is NSE-listed and Regulation 30 disclosures
go to both exchanges. Two more NSE sources close the headline blind spot:
the board-meeting PURPOSES feed (`source` NSE-BM — "to consider a scheme
of arrangement (demerger)" is often the first word), and a DEEP SCAN of
every bare "Outcome of Board Meeting" filing (`source` NSE-deep): its
first pages are read and the filing kept when they describe a
restructuring. BSE's announcement API refuses this environment
(Akamai), so BSE is covered by its daily RSS feed (accumulating forward
from the first run) and by the BSE-sourced per-company lists on
screener.in; BSE attachment PDFs download normally.

Re-run: `python3 ../fetch_announcements.py` (adds, never duplicates).
