---
name: spinoff-skill
description: >
  Special-situation investing in spin-offs and demergers, mechanised over
  the NiftyTotalMarket universe: pulls the last year of NSE and BSE
  filings, keeps every scheme of arrangement, demerger, subsidiary
  listing, slump sale, merger, rights offering and capital action, reads
  the attachments and the last twelve months of conference calls, and
  judges each situation against the spin-off checklist in the source
  notes (Greenblatt) — why the spin, who sells, who gains, what is
  revealed, the parent as the trade, partial spin-offs and the stub,
  rights offerings and oversubscription, and the first-year / second-year
  timing. Use when asked for announced or indicated spin-offs,
  demergers, value-unlocking schemes, or a Greenblatt-style read of one.
license: internal
---

# SpinOffSkill — spin-offs and demergers, mechanised

## The idea, from the notes

Spin-offs are where bargains form for reasons that have nothing to do
with investment merit. The new stock lands in the hands of holders who
never chose it — index funds, mandates with size or industry limits,
analysts who do not cover it — and they sell for about a year. The
parent is often the better buy before the split, and institutions buy
the clean parent afterwards. Insiders tell you what they think through
the stock and options they take in the new entity, and the date those
options are priced is worth knowing. A pro-forma statement and the peer
P/E of the piece's own industry price what the market is ignoring;
leverage in the spun entity turns a small asset move into a doubled
stock (Host Marriott). Partial spin-offs price the parent's stub once the
listed piece trades (Sears). Rights offerings with an oversubscription
clause, and insiders declaring they will oversubscribe, are the tell. The
largest gains came not in the first year but in the second.

## What the skill does

1. **Pulls the filings** — `Announcements/fetch_announcements.py` reads
   NSE's corporate-announcements feed month by month for the last year
   (the whole exchange, ~180k filings) and keeps the rows of the 750
   official NiftyTotalMarket constituents that classify as restructuring
   — `demerger`, `subsidiary_listing`, `slump_sale`, `merger`,
   `capital_reduction`, `rights_issue`, `scheme_other` — by category
   and headline. BSE's announcement API refuses this environment (Akamai),
   so BSE is covered honestly by its daily RSS feed (snapshotted every
   run and accumulated) and the BSE-sourced per-company lists on
   screener.in; BSE attachment PDFs download normally. Every attachment
   is reduced to text. Stored in
   `IndividualStockAnalysis/India/Announcements/NiftyTotalMarket/`,
   beside `BalanceSheet/`, `ProfitStatement/` and `ConferenceCalls/`.
2. **Builds situations** (`scripts/spinoff.py`) — one per company per
   kind family. A bare "Scheme of Arrangement" is re-classified from its
   attachment text (a scheme that demerges is a demerger; one that only
   amalgamates is a merger). Stages are walked from the filings' words:
   announced → exchange NOC → meetings → NCLT sanction → effective →
   record date → listed. Facts are extracted by pattern with the quote:
   entitlement ratio, resulting company, demerged undertaking, record and
   appointed dates, pro-forma mention, option-pricing language, promoter
   continuity, size of the piece. Stated reasons are classified into the
   notes' five (unrelated businesses, value unlocking, a weak or
   capital-heavy business carved away, a regulatory / strategic knot,
   attracting different investors).
3. **Reads the calls** — the stored consolidated transcripts, last twelve
   months, scanned for demerger / spin-off / hive-off / separate-listing
   / value-unlocking language with verbatim snippets; companies whose
   management talks this way with no filing yet are listed as
   *indicated, not yet filed* — the earliest signal.
4. **Pulls the numbers** — borrowings (stored balance sheets), net
   profit and sales (stored P&L), market cap / price / P/E (the live
   Nifty 500 market file, date stated), the industry median P/E from the
   same file; `stub_value()` and `leverage_doubling()` carry the Sears
   and Host Marriott arithmetic for when the pieces trade.
5. **Answers the checklist**, item by item, each with status
   (yes / partly / no / unknown), evidence and — when unknown — what to
   read next. A verdict line places the situation in the cycle:
   PRE-SPIN (study the parent) → SPINNING (record date set) → LISTED <1Y
   (the selling-pressure window) → LISTED 1–2Y (the second-year window)
   → MATURE. The score (0–10) is the share of checklist items the
   documents answer; it measures visibility of the pattern, not quality.
6. **The judge** (`claude -p`, model `SPINOFF_JUDGE_MODEL` →
   `ANALYST_MODEL` → `claude-opus-5`) reads each spin-off's scheme text
   and call excerpts and fills what a pattern cannot — the real reason,
   who gains, what is hidden or revealed, the option-pricing date, what
   to read next — strictly from the documents, with a verbatim quote,
   cached per document hash (`.judge_cache.json`). `--quick` skips it;
   the mechanical read stands alone and says so.

## Run it

```bash
cd IndividualStockAnalysis/India/Skills/SpinOffSkill
python3 ../../Announcements/fetch_announcements.py          # the last year of filings
python3 scripts/analyze.py run                              # report, with the judge
python3 scripts/analyze.py run --quick                      # no AI
python3 scripts/analyze.py run --refresh                    # re-pull, then report
python3 scripts/analyze.py company TMPV                     # one company, JSON
python3 -m pytest scripts/test_skill.py -q                  # 21 tests, offline
```

## Outputs

| Where | What |
|---|---|
| `Analysis/NiftyTotalMarketAnalysis/SpinOffAnalysis/SPINOFF_REPORT.md` | the report: situations table, each spin-off with stages, facts, the judge's read, the checklist, the numbers, the calls, the filings; other restructurings folded; call-only indications; method |
| `…/spinoff_latest.json` | the run, machine-readable |
| `…/_situations.csv`, `…/_concall_mentions.csv` | one row per situation; every call mention with its quote |
| `…/history/<run_date>/` | snapshot per run |
| `Announcements/NiftyTotalMarket/_announcements_restructuring.csv` | every matched filing (NSE, BSE-RSS, BSE-screener), with `kind`, `tags`, attachment and text file |
| `Announcements/NiftyTotalMarket/text/` | attachment texts |
| `Announcements/NiftyTotalMarket/_bse_codes.csv`, `_bse_rss_snapshots.csv`, `_fetch_log.csv`, `_README.md` | BSE codes, the accumulating BSE RSS store, the run log |

## Limits, stated

- BSE's historical announcement list cannot be pulled from this
  environment; the NSE feed is the complete one-year record for these
  dual-listed companies, and the BSE RSS store only grows forward from
  the first run.
- Market cap and P/E exist for the Nifty 500 members only (the live
  market file); for the other 250 the numbers section says so.
- Pattern extraction reads what a filing states; a scheme whose
  attachment is a scanned image yields no text and the checklist says
  "unknown" with what to read. The judge never fills a gap from memory.
- The score counts answered items; a high score means the documents
  show the pattern clearly, not that the stock is cheap.
