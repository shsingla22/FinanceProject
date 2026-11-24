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

1. **Pulls the filings and READS them** — `Announcements/fetch_announcements.py`
   reads NSE's corporate-announcements feed month by month for the last
   year and keeps every row of the 750 official NiftyTotalMarket
   constituents in `_all_filings.csv.gz` (about 84,000 a year). Then
   `Announcements/deep_read.py` streams the attachment of every filing in
   a category that could carry a corporate action (everything except the
   routine-compliance categories: DP certificates, trading windows,
   newspaper copies, ESOP grants, appointments, credit ratings and the
   like), keeps the text of its first six pages under `text/first/`,
   discards the PDF, and classifies from headline AND text together.
   Classification is MULTI-LABEL: `demerger`, `subsidiary_listing`,
   `slump_sale`, `merger`, `capital_reduction`, `rights_issue`,
   `preferential_issue`, `scheme_other` — one filing (and one company)
   can carry several tags; a kind read from the body needs a strong
   phrase or repeated mention so boilerplate does not count. Files over
   8 MB keep a headline-only classification and are marked. The
   board-meeting purposes feed is a further source. BSE's API refuses
   this environment, so BSE is covered by its daily RSS (accumulated) and
   the BSE-sourced per-company lists on screener.in. Every tagged
   filing's full text is stored. NSE's own corporate-actions REGISTER
   is a further source (`Announcements/demerger_ground_truth.py`): the
   daily bhavcopy bundle's `bc` file and the corporate-actions API list
   every record date with its purpose, so a universe company with a
   "Demerger" record date joins the store as a `NSE-register` row even
   when no announcement headline said so.
1b. **The calls are a SOURCE too** — the last twelve months of every
   stored transcript are scanned for special-situation language; each
   forward-looking mention (planning, evaluating, will, timeline — not a
   demerger already done, not a denial) becomes a filing-shaped row
   (`source` CALLS, the transcript as its attachment) so the initial list
   is never built from filings alone. A company with call mentions and no
   filing is a situation at the `indicated_on_calls` stage.
2. **Builds situations** (`scripts/spinoff.py`) — one per company per
   kind family, and a filing joins EVERY family its tags cover (a
   composite scheme that demerges one business and amalgamates another is
   in both). A bare "Scheme of Arrangement" is re-classified from its
   attachment text. Stages (announced → exchange NOC → meetings → NCLT
   sanction → effective → record date → listed) come from the filing
   headline when it names one, otherwise from the DOCUMENT read for
   EVENTS — "has sanctioned", "record date has been fixed as", "listed
   and admitted to dealings" — never from promises ("shall be listed",
   "proposed to be"); a match preceded by a promissory word does not
   count. Call mentions never set a stage. A record date "for the
   purpose of dividend / interest / buy-back / bonus" is not the scheme's
   record date, and "allotment of equity shares of the Company" is the
   company issuing its own shares, not the spin-off listing. NSE's
   register is then consulted: a demerger whose filings seem to report a
   record date or listing more than 30 days old that the register does
   not know falls back to its last real stage, with the reason kept.
   Facts are extracted by pattern with the quote: entitlement ratio,
   resulting company, demerged undertaking, record and appointed dates,
   pro-forma mention, option-pricing language, promoter continuity, size
   of the piece, and the DIRECTION of the demerger (the company's role in
   the scheme: Demerged / Transferor = outbound, Resulting / Transferee =
   inbound). Stated reasons are classified into the notes' five.
3. **Confidence and order** — `confirmed` when a demerger scheme is on
   the exchange record: an exchange filing in a scheme category
   (Demerger, Scheme of Arrangement, Amalgamation/Merger, a register
   record date) or a demerger-tagged filing whose headline names the
   scheme — a results filing or dividend notice whose body mentions a
   demerger in passing is not; `probable` for a demerger named only in a
   filing's text, a subsidiary listing in motion, or a scheme whose
   nature the documents do not settle; `indicated` for news verification,
   denial or calls alone. The judge's read of the COMPLETE record then
   moves it: a text-only demerger whose separated business the judge
   names becomes `confirmed`; a demerger the judge cannot find in the
   filed scheme and that is named only on the calls goes back to
   `indicated on calls` (Adani Enterprises: a composite scheme on file,
   the demergers management talks about not filed). The judge can also
   DEMOTE: a read opening "nothing is separated", an explicit
   amalgamation / liquidation / insolvency matter, becomes `merger`; an
   acquisition or stake purchase, or a business demerged INTO the listed
   company (inbound by the scheme's own words, or by the judge's; its own
   holders receive no new listing), becomes `other`. A subsidiary listing
   is never demoted. Each demotion is shown with its reason among the
   other restructurings. THE SPIN-OFF ITSELF is recognised too: a company
   the scheme names as the Resulting company whose Demerged company is
   itself NSE-listed, or one the judge calls the spin and says is listed,
   and that NSE's equity list (`_nse_equity_list.csv`, listing dates)
   shows listed within the last three years, is the spun entity in its
   first or second year — Tata Motors (the former TML Commercial
   Vehicles), SKF India (Industrial), Aditya Birla Lifestyle Brands. It is
   `confirmed`, stage LISTED from the exchange's own listing date, with
   the parent named; past two years it is marked mature. The report puts
   confirmed demergers first and gives them the full treatment.
3b. **Subsidiary listings are resolved, not left probable.** A filing that
   pairs IPO / DRHP / listing with a subsidiary is asked one pointed,
   forced-choice question of the complete documents
   (`analyze.judge_listing`): is a subsidiary, associate or joint venture
   of this company being listed by IPO (`subsidiary_ipo_announced`), has
   it already listed (`subsidiary_already_listed`), was the IPO
   withdrawn — or is it something that only looked like one: the company
   selling shares it holds in another company's IPO, a sale or slump
   sale, a merger, the company's own IPO, or no event at all. The first
   two are PARTIAL SPIN-OFFS (the notes' Sears case): `confirmed`, shown
   in the confirmed list directly BELOW the demergers with the
   subsidiary, the parent's stake before and after, the IPO stage, and
   the listing date — from NSE's equity list when the subsidiary is found
   there, else the date the filings give — and a verbatim quote. Listed
   first, then IPOs in motion; one listed more than two years ago is
   past the window and dropped. Everything else leaves BOTH the confirmed
   and the probable lists and is kept, with its reason, among the other
   restructurings. Without a judge answer the row stays probable. The
   question is also asked of a demerger or scheme situation that carries
   subsidiary-listing filings (a company is one spin situation, and a
   demerger tag outranks a listing tag): a partial spin-off found there
   replaces a text-only demerger, and is shown BESIDE a confirmed or
   register-recorded demerger, which stays a demerger.
3c. **Probable and indicated rows are settled the same way.** Every
   demerger or scheme row left `probable` (a demerger named only in a
   filing's text; a scheme whose nature is unclear) or `indicated` (calls
   or news only) is asked one forced-choice question of the complete
   documents (`analyze.judge_resolution`): is it a `demerger_in_progress`
   (a business of THIS company, under a board-approved scheme, its
   holders to receive shares, not yet complete), a `demerger_completed`
   (and when, and in which role), another company's demerger, an internal
   reorganisation, a merger or acquisition, a subsidiary IPO,
   management's own indication, a withdrawal, press speculation, or no
   event. A demerger in progress becomes a `confirmed` demerger, marked †
   and listed LAST in the demerger table (it is confirmed by reading the
   text; no scheme-category filing names it). A completed one goes to
   **Completed demergers**, a dated list below the partial spin-offs,
   which also carries the demergers NSE's register recorded more than two
   years before the run; the date is the register's record date, else the
   resulting company's listing date from NSE's equity list, else the date
   the filings give. Management's own indication stays `indicated`, as do
   withdrawals. Everything else is discarded: it leaves every list and is
   kept, with its reason and quote, among the other restructurings. The
   judge may not move a row to a record date or a listing; only the
   exchange's record does that. Without a judge answer the row is left as
   it was.
3d. **Every separated entity, and a nine-part write-up.** One company can
   separate several businesses (Quess: Digitide and Bluspring; Vedanta:
   each of its demerged companies). The DEAL SHEET
   (`analyze.judge_deal`) names EVERY resulting company or listed
   subsidiary from the complete documents, with — per entity — its
   business, share swap, stated turnover and share of the parent, and who
   runs it; and for the whole deal the promoters' holding before and
   after, what a public shareholder receives, management incentives,
   every dated event, and the documents' own statements of how the
   businesses differ. Three rules keep the entity list complete and
   clean. (a) THE WHOLE HISTORY IS READ: `analyze.deal_text_for` takes
   every filing tagged demerger / scheme / subsidiary listing in the
   store; when they exceed the budget every filing contributes its opening
   pages first (the Regulation 30 disclosure), then whole documents
   shortest first — so a newer scheme never crowds out an older one
   (Vedanta's four demerged companies behind its later real-estate
   scheme). (b) EVERY ENTITY HAS A ROLE: resulting, listed_subsidiary,
   parent, former_parent, merged_in, unrelated, other — with its scheme
   and status. Only resulting companies and listed subsidiaries are shown
   as separated (TVS Motor: Harita ARC, not TVS Motor Services which is
   merged in); `analyze.settle_roles` holds the role to the situation: a
   resulting company listed more than a year before the record date is an
   earlier separation (Triveni Turbine, 2011), a subsidiary listed years
   ago is not a partial spin-off now (Hindustan Zinc), a dropped unit is
   marked dropped (Vedanta Base Metals). (c) THE EXCHANGE CROSS-CHECKS:
   `deal.arrivals` lists companies NSE shows listed in the 150 days after
   a record date that carry the parent's name or are named in the filings;
   they are put to the judge, which says from the documents which the
   scheme created (a resulting company is often renamed: Talwandi Sabo
   Power → Vedanta Power), and any left unaccounted for is flagged in the
   write-up. `scripts/deal.py` adds the mechanical parts: each
   entity's NSE symbol and listing date (equity list), the shareholding
   pattern (screener, stored under `ShareholdingPattern/`), market caps
   from the newest bhavcopy bundle, and the call transcripts split into
   speaker turns. Each company is then written in nine parts:
   (1) company and category; (2) stages and dates — every stage with its
   filing, the documents' stated dates, NSE's record date, each entity's
   listing; (3) size of each separated entity beside the WHOLE (the parent
   plus every separated entity) — market-cap share, the documents' stated
   share (turnover, or the cost-of-acquisition split read by entity name),
   segment revenue share — and the reading for institutional selling,
   entity by entity, from the first of those that exists (under 10% very
   likely, under 25% likely, under 50% possible); for a subsidiary IPO no
   shares are distributed, so the section sizes the listed piece beside
   the parent for the stub instead; (4) insider ownership — swap ratio per
   entity, promoters' holding, management incentives; (5) why, point by
   point; (6) the calls VERBATIM — every question about the separation
   with every answer to it, uncut, oldest first, plus the complete
   sentences about it from prepared remarks; an exchange counts when it
   uses a separation term or names a separated entity ('Vedanta
   Aluminium', 'Digitide') — never on an ordinary word of the business
   ('aluminium', 'power'), which would pull in every operating question; (7) the parent's statements;
   (8) each separated business's statements — its own reported numbers
   once listed and on file, else one segment table per business, with
   segment assets, liabilities, capital employed and capex when the pages
   give them; (9) other financial differences — margins, growth,
   working-capital days, ROCE, debt, side by side. The main report shows
   part 6 as a table of calls; `companies/<SYMBOL>.md` carries all nine
   parts with every exchange in full.
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
   `ANALYST_MODEL` → `claude-opus-5`) is handed the COMPLETE record for
   each spin-off: every filing of the company in full text (newest
   first) and the complete transcripts of the last twelve months of
   calls for the checklist read, thirty-six months for the rationale —
   whole documents, not snippets. Budgets of 320k characters of filings
   and 360k of calls keep the prompt inside the model's context; over
   budget, the oldest documents are dropped whole and the prompt says how
   many. It reads only what it is shown, must quote, writes "not stated"
   rather than fill a gap, and is cached per document hash
   (`.judge_cache.json`). `--quick` skips it.
11. **Coverage** — `_coverage.csv` records, per confirmed / probable
    company, whether the parent P&L, cash flow, P/E, annual reports,
    presentations, segment numbers and rationale were found.
12. **The register check** (`scripts/validate_demergers.py`) — the
    demerger list is tested against NSE's own record, built by
    `Announcements/demerger_ground_truth.py` from the year's bhavcopy
    bundles' corporate-actions file (record dates with purpose
    "Demerger"), the corporate-actions API (the same register, with
    ISINs, so a renamed company is keyed to the universe), and NSE's
    equity list (listing dates, for the resulting company's arrival).
    RECALL: every universe company with a demerger record
    date must be in the list as a confirmed or probable demerger — held
    as merger or other is a classification miss, absent is a capture
    miss. PRECISION: every confirmed demerger at record date or listed
    must have a register row, and a confirmed demerger whose judge read
    says nothing is separated is a false positive; confirmed demergers
    still before their record date are "pending, not yet verifiable".
    ARRIVAL: a company in NSE's equity list that LISTED within 75 days of
    the record date, named like the parent or the company the scheme
    names; a company that IS the resulting company is verified by its
    own listing date. It writes `SPINOFF_GROUND_TRUTH_CHECK.md` and exits 1
    on any miss or false positive, so a run that fails the register is
    not shared.
13. **Backtests** (`scripts/backtest.py`) — the skill run AS OF a past
    date over a past window, list-only (judge classification and listing
    status; no rationale, numbers, documents or offerings), checked
    against the register for that window, everything under
    `Analysis/NiftyTotalMarketAnalysis/SpinOffBacktest/<label>/`. An
    as-of run sees only filings dated inside its window, calls up to its
    month, register record dates up to its date, and the equity list;
    nothing later. The store and the register must first be extended
    back (`fetch_announcements.py --days N`, `demerger_ground_truth.py
    --days N`). The judge cache keeps several readings per company, so a
    backtest and today's run do not evict each other.

## Run it

```bash
cd IndividualStockAnalysis/India/Skills/SpinOffSkill
python3 ../../Announcements/fetch_announcements.py                 # the last year of filings
python3 ../../InvestorPresentations/fetch_presentations.py --only THOMASCOOK,UPL
python3 scripts/analyze.py run                                     # report, with the judge
python3 scripts/analyze.py run --fetch-docs                        # pull reports for highlighted companies first
python3 scripts/analyze.py run --quick                             # no AI
python3 scripts/analyze.py company THOMASCOOK                      # one company, JSON
python3 scripts/analyze.py render                                  # re-render the report from the saved run, no judge
python3 ../../Announcements/demerger_ground_truth.py --days 400    # NSE's register from the bhavcopy bundles
python3 scripts/validate_demergers.py                              # the list against the register; exit 1 on a miss
python3 ../../Announcements/fetch_announcements.py --days 960      # extend the store back (for a backtest)
python3 scripts/backtest.py --from 2024-04-01 --to 2025-03-31 --label FY2024-25   # the skill as of a past date, list-only, own folder
python3 scripts/backtest.py --from 2024-04-01 --label 2024-04_to_today
python3 -m pytest scripts/test_skill.py -q                         # 77 tests, offline
```

## Outputs

| Where | What |
|---|---|
| `Analysis/NiftyTotalMarketAnalysis/SpinOffAnalysis/SPINOFF_REPORT.md` | confirmed demergers table (entity, stage, listing, score), probable / indicated table — demergers first, each row with its SOURCES AND EVIDENCE: the filing or transcript link, the keyword that made it a spin-off / demerger / listing / scheme, the stored text file with line number, and the sentence around it — other restructurings; per confirmed company: listing callout, stages, facts, the judge's read, the rationale from three years of calls with transcript links, the parent's three years with charts, P/E and cash flows, the separated business's own numbers with page citations, checklist, calls, filings |
| `…/companies/<SYMBOL>.md` | one file per company: the complete nine-part analysis with every management-call question and answer in full |
| `…/spinoff_latest.json`, `…/_situations.csv`, `…/_coverage.csv`, `…/_offerings.csv`, `…/_concall_mentions.csv`, `…/history/<run_date>/` | the run, machine-readable; one row per situation; what was found for whom; every call mention with tone and quote; snapshots |
| `…/SPINOFF_GROUND_TRUTH_CHECK.md`, `…/_ground_truth_check.csv` | the register check: recall row per register demerger, precision row per confirmed demerger, verdicts |
| `Announcements/NiftyTotalMarket/` | every matched filing with kind, tags, attachment and text; `_all_filings.csv.gz` (every universe filing); `text/first/` (first six pages of every read attachment); `_demerger_ground_truth.csv` (NSE's register); BSE codes; BSE RSS store; log; README |
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
