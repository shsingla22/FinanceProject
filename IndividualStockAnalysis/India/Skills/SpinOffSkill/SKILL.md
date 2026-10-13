---
name: spinoff-skill
description: >
  Special-situation investing in spin-offs and demergers, mechanised over
  the NiftyTotalMarket universe: pulls the last year of NSE and BSE
  filings, keeps every scheme of arrangement, demerger, subsidiary
  listing, slump sale, merger, rights offering and capital action, reads
  the attachments, three years of conference calls, annual reports and
  quarterly presentations, and judges each situation against the
  spin-off checklist in the source notes (Greenblatt) — why the spin,
  who sells, who gains, what is revealed, the parent as the trade,
  partial spin-offs and the stub, rights offerings, and first-year /
  second-year timing — with the demerged entity's listing status, the
  parent's three-year financials, P/E and cash flows, and the separated
  business's own numbers, page-cited. Use when asked for announced or
  indicated spin-offs, demergers, value-unlocking schemes, or a
  Greenblatt-style read of one.
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
   and keeps the rows of the 750 official NiftyTotalMarket constituents
   that classify as restructuring — `demerger`, `subsidiary_listing`,
   `slump_sale`, `merger`, `capital_reduction`, `rights_issue`,
   `preferential_issue`, `scheme_other`. Two more NSE sources close the
   headline blind spot: the board-meeting PURPOSES feed ("to consider a
   scheme of arrangement (demerger)") and a DEEP SCAN of every bare
   "Outcome of Board Meeting" filing, whose first pages are read and the
   filing kept when they describe a restructuring. BSE's announcement API refuses this environment
   (Akamai), so BSE is covered by its daily RSS feed (snapshotted and
   accumulated) and the BSE-sourced per-company lists on screener.in;
   BSE attachment PDFs download normally. Every attachment is reduced to
   text. Stored in `IndividualStockAnalysis/India/Announcements/`.
2. **Builds situations** (`scripts/spinoff.py`) — one per company per
   kind family. A bare "Scheme of Arrangement" is re-classified from its
   attachment text. Stages are walked from the filing HEADLINES
   (announced → exchange NOC → meetings → NCLT sanction → effective →
   record date → listed); a scheme body that merely promises a listing
   is not a listing event. Facts are extracted by pattern with the
   quote: entitlement ratio, resulting company, demerged undertaking,
   record and appointed dates, pro-forma mention, option-pricing
   language, promoter continuity, size of the piece. Stated reasons are
   classified into the notes' five.
3. **Confidence and order** — `confirmed` when a demerger scheme is on
   the exchange record (a Demerger / Scheme filing or a scheme text that
   demerges); `probable` for a subsidiary listing in motion or a scheme
   whose nature the documents do not settle; `indicated` for news
   verification, denial or calls alone. The report puts confirmed
   demergers first and gives them the full treatment.
4. **Listing status** — for every spin-off: LISTED since (record date),
   RECORD DATE set and listing pending (with the typical 4–10 week gap
   stated as typical, not forecast), NOT YET with the timeline the
   filings or calls state, subsidiary IPO in motion, or no scheme filed.
5. **Rationale from three years of calls** — every passage in the last
   36 months of the stored transcripts where the separation was
   discussed (wide windows), plus the scheme's rationale section, read
   by the judge into a detailed account: the reasoning with the
   specifics management gave, how the idea evolved call by call, what
   management expects for each entity, what the calls did not explain —
   point by point, each linked to its transcript
   (`InvestorPresentations/NiftyTotalMarket/_concall_links.csv`).
6. **The parent's numbers** (`scripts/financials.py`) — sales, operating
   profit, PAT with growth and margins, and EPS, for the last three
   fiscal years from the stored P&L; two Mermaid charts (₹ crore lines
   and margins; they render on GitHub); P/E from the live Nifty 500
   market file or latest stored close ÷ latest fiscal-year EPS, method
   stated; three years of cash flows (operating, investing, financing,
   net, free) from the stored cash-flow statements. Growth and margins
   are computed here, never by a model.
7. **The separated business's own numbers** —
   `InvestorPresentations/fetch_presentations.py` pulls, per
   highlighted company, the last three annual reports (to
   `AnnualReports/NiftyTotalMarket/{SYMBOL}/`) and twelve quarterly
   presentations (to `InvestorPresentations/NiftyTotalMarket/{SYMBOL}/`)
   from the BSE links screener lists, as PDFs on disk plus page-marked
   text and an index with source URLs. The segment-reporting pages
   (always the note itself, plus pages naming the business or its
   words) go to the judge, which returns revenue, operating profit and
   PAT per fiscal year with document and page for every number, the
   latest quarter from the presentations, what the profit line is, and
   what the pages do not carry. Growth and margins are computed here.
8. **Rights and preferential offerings — who is buying.** Rights issues
   and preferential issues of equity or warrants (`rights_issue`,
   `preferential_issue`; conversions of warrants included) are kept as
   their own situations. The filing text is read for the instrument,
   count, price and aggregate amount, and the judge names the buyers:
   every allottee with its category (promoter, promoter group,
   non-promoter, institution, public), the promoters' share of the
   issue, for rights the promoters' stated intent to subscribe, renounce
   or oversubscribe, for warrants the upfront payment and tenure, the
   purpose and the stage. The report's "who is buying" table puts
   offerings with promoters among the buyers first — the notes' tell —
   and `_offerings.csv` carries every row.
9. **Checklist, verdict, score** — the notes' questions answered item by
   item with evidence and what to read next; the verdict places the
   situation in the cycle (RUMOURED → PRE-SPIN → SPINNING → LISTED <1Y →
   LISTED 1–2Y → MATURE); the score is the share of items the documents
   answer.
10. **The judge** (`claude -p`, model `SPINOFF_JUDGE_MODEL` →
   `ANALYST_MODEL` → `claude-opus-5`) reads only the documents shown to
   it, must quote, writes "not stated" rather than fill a gap, and is
   cached per document hash (`.judge_cache.json`). `--quick` skips it.
11. **Coverage** — `_coverage.csv` records, per confirmed / probable
    company, whether the parent P&L, cash flow, P/E, annual reports,
    presentations, segment numbers and rationale were found.

## Run it

```bash
cd IndividualStockAnalysis/India/Skills/SpinOffSkill
python3 ../../Announcements/fetch_announcements.py                 # the last year of filings
python3 ../../InvestorPresentations/fetch_presentations.py --only THOMASCOOK,UPL
python3 scripts/analyze.py run                                     # report, with the judge
python3 scripts/analyze.py run --fetch-docs                        # pull reports for highlighted companies first
python3 scripts/analyze.py run --quick                             # no AI
python3 scripts/analyze.py company THOMASCOOK                      # one company, JSON
python3 -m pytest scripts/test_skill.py -q                         # 36 tests, offline
```

## Outputs

| Where | What |
|---|---|
| `Analysis/NiftyTotalMarketAnalysis/SpinOffAnalysis/SPINOFF_REPORT.md` | confirmed demergers table (entity, stage, listing, score), probable / indicated table, other restructurings; per confirmed company: listing callout, stages, facts, the judge's read, the rationale from three years of calls with transcript links, the parent's three years with charts, P/E and cash flows, the separated business's own numbers with page citations, checklist, calls, filings |
| `…/spinoff_latest.json`, `…/_situations.csv`, `…/_coverage.csv`, `…/_offerings.csv`, `…/_concall_mentions.csv`, `…/history/<run_date>/` | the run, machine-readable; one row per situation; what was found for whom; every call mention with tone and quote; snapshots |
| `Announcements/NiftyTotalMarket/` | every matched filing with kind, tags, attachment and text; BSE codes; BSE RSS store; log; README |
| `AnnualReports/NiftyTotalMarket/{SYMBOL}/`, `InvestorPresentations/NiftyTotalMarket/{SYMBOL}/` | annual reports and presentations: PDFs on disk (git-ignored), page-marked `.txt`, `_index.csv` with source URLs; `_concall_links.csv` maps every call to its transcript and presentation |

## Limits, stated

- BSE's historical announcement list cannot be pulled from this
  environment; the NSE feed is the complete one-year record for these
  dual-listed companies, and the BSE RSS store only grows forward.
- Market cap and trailing P/E from the live file exist for the Nifty 500
  members; others get close ÷ EPS, with the method stated.
- Segment numbers come from what the annual reports and presentations
  print. Where a business is not a reportable segment, or the pages are
  scanned images, the report says what was searched and what was not
  found rather than estimating.
- The score counts answered items; a high score means the documents
  show the pattern clearly, not that the stock is cheap.
