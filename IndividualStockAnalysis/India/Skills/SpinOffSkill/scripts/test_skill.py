"""
SpinOffSkill tests.

  cd IndividualStockAnalysis/India/Skills/SpinOffSkill
  python3 -m pytest scripts/test_skill.py -q

Every test is offline: the fetcher's parsers run on captured fixtures,
the analysis on synthetic filings and texts, the CLI on a temporary
output folder with the judge stubbed. The arithmetic of the notes
(Sears' stub, Host Marriott's leverage) is checked against the notes'
own numbers.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent.parent / "Announcements"))

import fetch_announcements as FA     # noqa: E402
import spinoff as SO                 # noqa: E402
import analyze as AZ                 # noqa: E402
import financials as FN              # noqa: E402
import deep_read as DR               # noqa: E402

sys.path.insert(0, str(HERE.parent.parent.parent / "InvestorPresentations"))
import fetch_presentations as FP     # noqa: E402

TODAY = dt.date(2026, 10, 8)


@pytest.fixture(autouse=True)
def _no_register_on_disk(monkeypatch):
    """Tests build their own register (or none): the real
    _demerger_ground_truth.csv must not reach into them."""
    monkeypatch.setattr(SO, "_REGISTER", {})


def test_presentation_index_survives_a_torn_line_and_writes_atomically(tmp_path):
    assert FP.label_date("Mar 2026") == dt.date(2026, 3, 1)
    assert FP.label_date(None) == dt.date.min and FP.label_date("n.aspx?Pname=x.pdf") == dt.date.min
    rows = [{"symbol": "A", "label": "Mar 2026", "transcript_url": "t", "presentation_url": "p"},
            {"symbol": "n.aspx?Pname=7d07.pdf", "label": None, "transcript_url": None, "presentation_url": None},
            {"symbol": "", "label": "Jan 2026", "transcript_url": "", "presentation_url": ""}]
    good = FP._well_formed(rows)
    assert [r["symbol"] for r in good] == ["A"]
    out = tmp_path / "links.csv"
    FP._write(out, good, ["symbol", "label", "transcript_url", "presentation_url"])
    assert FP._read(out) == good and not list(tmp_path.glob("*.tmp"))


# ================================================================ fetcher

def test_classify_reads_category_and_headline():
    assert FA.classify("Scheme of Arrangement", "Approval of Composite Scheme by NCLT") \
        == ("scheme_other", ["scheme_other"])
    k, tags = FA.classify("Updates", "Demerger of Commercial Vehicles business of Tata Motors")
    assert k == "demerger" and "demerger" in tags
    k, tags = FA.classify("Amalgamation/Merger", "Scheme of Amalgamation of a WOS")
    assert k == "merger" and "merger" in tags
    # a scheme that demerges is a demerger even if it also merges parts
    k, _ = FA.classify("Scheme of Arrangement",
                       "Composite scheme: demerger of the energy business and amalgamation of X")
    assert k == "demerger"
    assert FA.classify("Rights Issue", "Letter of offer") == ("rights_issue", ["rights_issue"])
    k, _ = FA.classify("Updates", "Board approved the IPO of its material subsidiary")
    assert k == "subsidiary_listing"
    k, _ = FA.classify("Updates", "Slump sale of the motors business to Innomotics")
    assert k == "slump_sale"
    assert FA.classify("Updates", "Appointment of CFO") == ("", [])
    assert FA.classify("Demerger", "anything") == ("demerger", ["demerger"])


def test_classify_ignores_noise_categories_whatever_they_say():
    noisy = "Certificate under SEBI (Depositories and Participants) Regulations, 2018"
    assert FA.classify(noisy, "demerged shares credited") == ("", [])
    assert FA.classify("Issue of Duplicate Share Certificate(s)", "pursuant to merger") == ("", [])
    assert FA.classify("Copy of Newspaper Publication", "notice of demerger meeting") == ("", [])


def test_nse_rows_keep_only_universe_restructuring_filings():
    feed = [
        {"symbol": "TMPV", "an_dt": "03-Oct-2025 18:02:11", "desc": "Updates",
         "attchmntText": "Demerger of Commercial Vehicles business", "seq_id": "1",
         "attchmntFile": "https://nsearchives.nseindia.com/corporate/a.pdf", "attFileSize": "1.2 MB"},
        {"symbol": "TMPV", "an_dt": "03-Oct-2025 18:02:12", "desc": "Appointment",
         "attchmntText": "Appointment of director", "seq_id": "2", "attchmntFile": ""},
        {"symbol": "NOTINIDX", "an_dt": "03-Oct-2025 18:02:13", "desc": "Demerger",
         "attchmntText": "Demerger", "seq_id": "3", "attchmntFile": ""},
    ]
    rows = FA.nse_rows(feed, {"TMPV": "Tata Motors Passenger Vehicles Ltd."})
    assert [r["ann_id"] for r in rows] == ["1"]
    r = rows[0]
    assert r["date"] == "2025-10-03" and r["source"] == "NSE" and r["kind"] == "demerger"
    assert r["company"].startswith("Tata Motors") and r["file_size"] == "1.2 MB"
    assert set(r) == set(FA.FIELDS)


def test_month_windows_cover_the_lookback_in_month_sized_pieces():
    w = FA.month_windows(dt.date(2026, 10, 8), 365)
    assert w[0][0] == dt.date(2025, 10, 8) and w[-1][1] == dt.date(2026, 10, 8)
    for (a, b), (c, _) in zip(w, w[1:]):
        assert c == b + dt.timedelta(days=1) and (b - a).days <= 31
        assert a.month == b.month


def test_bse_rss_parses_items_with_scrip_codes_and_dates():
    xml = """<rss><channel><item><title>Persistent Systems Ltd (533179)</title>
    <link>https://www.bseindia.com/xml-data/corpfiling/AttachLive/779e.pdf</link>
    <scripcode>533179</scripcode><description>Intimation of   demerger</description>
    <pubDate>08-Oct-2026 09:50:18</pubDate></item></channel></rss>"""
    rows = FA.parse_bse_rss(xml)
    assert rows == [{"bse_code": "533179", "company": "Persistent Systems Ltd",
                     "headline": "Intimation of demerger",
                     "link": "https://www.bseindia.com/xml-data/corpfiling/AttachLive/779e.pdf",
                     "date": "2026-10-08"}]


def test_screener_company_page_yields_ids_and_announcements_parse():
    html = ('<div data-company-id="3245"></div> <a href="https://www.bseindia.com/'
            'stock-share-price/sun-pharmaceutical-industries-ltd/sunpharma/524715/">BSE</a>')
    assert FA.parse_screener_company(html) == {"screener_id": "3245", "bse_code": "524715"}
    li = ('<ul><li><a href="https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=abc.pdf">'
          ' Scheme of Arrangement <div class="ink-600 smaller"><time datetime="2026-10-07T20:39:11'
          '+05:30">7 Oct</time> - Approval of demerger by NCLT &amp; listing</div></a></li>'
          '<li><a href="https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=def.pdf">'
          ' Newspaper Publication <span><time>12 Oct 2025</time></span></a></li></ul>')
    rows = FA.parse_screener_announcements(li, 2026)
    assert rows[0]["date"] == "2026-10-07" and rows[0]["headline"].startswith("Scheme of Arrangement")
    assert "demerger by NCLT & listing" in rows[0]["note"]
    assert rows[1]["date"] == "2025-10-12"
    assert FA.bse_pdf_url(rows[0]["link"]).endswith("/AttachLive/abc.pdf")


def test_merge_rows_adds_never_duplicates_and_keeps_text_files():
    old = [{"source": "NSE", "ann_id": "1", "date": "2026-01-01", "symbol": "A", "text_file": "text/A_1.txt"}]
    new = [{"source": "NSE", "ann_id": "1", "date": "2026-01-01", "symbol": "A", "text_file": ""},
           {"source": "NSE", "ann_id": "2", "date": "2026-01-02", "symbol": "A", "text_file": ""}]
    m = FA.merge_rows(old, new)
    assert [r["ann_id"] for r in m] == ["1", "2"]
    assert m[0]["text_file"] == "text/A_1.txt"


def test_universe_is_the_official_index_list_only():
    u = FA.universe()
    assert 700 <= len(u) <= 800, len(u)
    assert "SUNPHARMA" in u and "RELIANCE" in u


# =============================================================== analysis

SCHEME = """
SCHEME OF ARRANGEMENT between Alpha Industries Limited ("Demerged Company") and
Alpha Energy Limited ("Resulting Company") and their respective shareholders.
RATIONALE: The demerger will unlock value for shareholders and allow focused
management of two distinct businesses with different risk profiles, each
attracting a distinct set of investors. The Energy business is capital intensive.
"Demerged Undertaking" means the Energy business of the Demerged Company
comprising all assets and liabilities pertaining to the energy segment.
The Energy business contributed 18% of the consolidated revenue in FY25.
Share Entitlement Ratio: 1 (One) fully paid-up equity share of Rs. 2 each of the
Resulting Company for every 1 (One) fully paid-up equity share of Rs. 2 each held
in the Demerged Company. Appointed Date: 1st April 2025. Record Date for the
purpose of the Scheme shall be 15th September 2026.
Pro forma financial statements of the Resulting Company are annexed.
The promoters shall continue to hold the same percentage shareholding in the
Resulting Company. Stock options granted under the ESOP 2020 shall be adjusted
and the exercise price determined on the record date.
"""


def test_facts_in_reads_ratio_entities_dates_and_incentives():
    f = SO.facts_in(SCHEME)
    assert f["entitlement_ratio"] == "1 for every 1"
    assert f["resulting_company"] == "Alpha Energy Limited"
    assert f["demerged_undertaking"].startswith("the Energy business")
    assert f["record_date"] == "2026-09-15" and f["appointed_date"] == "2025-04-01"
    assert f["pro_forma"] is True
    assert "exercise price" in f["esop_pricing"]
    assert "promoters shall continue" in f["insider_continuity"]
    assert f["small_share"] == "18% of revenue"
    # the other drafting order is read too
    g = SO.facts_in('between X Ltd ("Demerged Company") and the Resulting Company, i.e. Beta Power Limited')
    assert g["resulting_company"] == "Beta Power Limited"


def test_reasons_are_classified_into_the_notes_five_with_quotes():
    rs = {r["reason"]: r["quote"] for r in SO.reasons_in(SCHEME)}
    assert "unrelated businesses separated" in rs
    assert "value unlocking for shareholders" in rs
    assert "a weak or capital-heavy business carved away" in rs
    assert "attracting different investors / capital" in rs
    assert "unlock value" in rs["value unlocking for shareholders"]
    # Regulation 30 boilerplate is not a regulatory reason
    assert SO.reasons_in("Disclosure pursuant to Regulation 30 of SEBI (Listing Obligations "
                         "and Disclosure Requirements) Regulations, 2015") == []


def test_stage_of_reaches_the_furthest_stage_named():
    assert SO.stage_of("Board approved the proposed demerger") == "announced"
    assert SO.stage_of("Receipt of No Objection letter from the exchange") == "exchange_noc"
    assert SO.stage_of("NCLT convened meeting of equity shareholders") == "meetings"
    assert SO.stage_of("Approval of Composite Scheme of Arrangement by NCLT") == "nclt_sanction"
    assert SO.stage_of("Record date for the purpose of the scheme") == "record_date"
    assert SO.stage_of("Listing and commencement of trading of equity shares of the "
                       "resulting company") == "listed"
    assert SO.stage_of("Appointment of director") is None


def test_refine_kind_reads_the_scheme_text():
    row = {"kind": "scheme_other"}
    assert SO.refine_kind(row, SCHEME + " demerger demerger") == "demerger"
    assert SO.refine_kind(row, "amalgamation of the WOS; merger; amalgamation; amalgamation") == "merger"
    assert SO.refine_kind(row, "") == "scheme_other"
    assert SO.refine_kind({"kind": "rights_issue"}, SCHEME) == "rights_issue"


def _rows():
    mk = lambda i, d, cat, head, kind, tags=None: {        # noqa: E731
        "date": d, "symbol": "ALPHA", "company": "Alpha Industries Ltd.", "source": "NSE",
        "category": cat, "kind": kind, "tags": tags or kind, "headline": head,
        "attachment": f"https://x/{i}.pdf", "ann_id": str(i), "file_size": "1 MB", "text_file": ""}
    return [
        mk(1, "2026-01-10", "Outcome of Board Meeting", "Board approved the proposed demerger of the Energy business", "demerger"),
        mk(2, "2026-03-02", "Scheme of Arrangement", "Receipt of No Objection letter from NSE on the Scheme", "scheme_other"),
        mk(3, "2026-06-20", "Scheme of Arrangement", "Approval of the Scheme of Arrangement by NCLT", "scheme_other"),
        mk(4, "2026-09-01", "Record Date", "Record date for the demerger fixed as 15 September 2026", "demerger"),
        mk(5, "2026-02-01", "Amalgamation/Merger", "Amalgamation of a wholly owned subsidiary", "merger"),
    ]


def test_build_situations_groups_walks_stages_and_gathers_facts():
    texts = {"3": SCHEME}
    sits = SO.build_situations(_rows(), texts, TODAY)
    assert [s["kind"] for s in sits] == ["demerger", "merger"]      # spin-offs first
    s = sits[0]
    assert s["n_filings"] == 4 and s["first_filing"] == "2026-01-10"
    assert list(s["stage_dates"]) == ["announced", "exchange_noc", "nclt_sanction", "record_date"]
    assert s["stage"] == "record_date" and s["listed_on"] == "2026-09-15"   # the record date itself
    assert s["facts"]["resulting_company"] == "Alpha Energy Limited"
    assert s["facts"]["entitlement_ratio"] == "1 for every 1"
    assert {r["reason"] for r in s["reasons"]} >= {"value unlocking for shareholders"}
    assert s["days_since_first"] == (TODAY - dt.date(2026, 1, 10)).days
    # the bare 'Scheme of Arrangement' row was re-read as a demerger from its text
    assert [h["kind"] for h in s["headlines"] if h["date"] == "2026-06-20"] == ["demerger"]


def test_checklist_and_verdict_follow_the_notes():
    sits = SO.build_situations(_rows(), {"3": SCHEME}, TODAY)
    s = sits[0]
    fin = {"industry": "Capital Goods", "borrowings_cr": 500.0, "borrowings_year": "Mar 2026",
           "market_cap_cr": 10000.0, "debt_to_market_cap": 0.05, "net_profit_cr": 1000.0,
           "net_profit_cr_year": "Mar 2026", "pe_on_latest_profit": 10.0,
           "industry_median_pe": 30.0, "industry_peers": 20}
    mentions = [{"call": "May 2026", "term": "demerger", "quote": "the demerger is on track"}]
    items = {i["item"]: i for i in SO.checklist(s, fin, mentions, TODAY)}
    assert items["Why the spin-off"]["status"] == "yes"
    assert items["Institutional selling likely (small / different business)"]["status"] == "yes"
    assert items["Insider ownership and incentives aligned"]["status"] == "partly"
    assert items["A hidden value revealed (pro-forma, leverage, comparables)"]["status"] == "yes"
    assert items["Parent before the spin (clean parent, takeover prelude)"]["status"] == "no"
    assert items["Timing (first year sells, second year gains)"]["status"] == "partly"
    assert items["Management discussing it on the calls"]["status"] == "yes"
    v = SO.verdict(s, list(items.values()))
    assert v["label"].startswith("SPINNING") and 7 <= v["score"] <= 10   # record date 23 days ago
    later = dt.date(2026, 11, 1)
    s2 = SO.build_situations(_rows(), {"3": SCHEME}, later)[0]
    assert SO.verdict(s2, SO.checklist(s2, fin, mentions, later))["label"].startswith("LISTED <1Y")
    # a pre-spin situation points at the parent
    pre = SO.build_situations(_rows()[:2], {}, TODAY)[0]
    assert pre["stage"] == "exchange_noc"
    assert SO.verdict(pre, SO.checklist(pre, {}, [], TODAY))["label"].startswith("PRE-SPIN")
    # a merger is named for what it is
    m = sits[1]
    assert SO.verdict(m, SO.checklist(m, {}, [], TODAY))["label"].startswith("MERGER")


def test_timing_moves_from_first_year_to_second_year_to_mature():
    rows = _rows()[:4]
    for today, expect in ((dt.date(2026, 12, 1), "LISTED <1Y"), (dt.date(2027, 12, 1), "LISTED 1–2Y"),
                          (dt.date(2029, 1, 1), "MATURE")):
        s = SO.build_situations(rows, {}, today)[0]
        assert SO.verdict(s, SO.checklist(s, {}, [], today))["label"].startswith(expect)


def test_sears_stub_and_host_marriott_leverage_match_the_notes():
    # Sears $54; Dean Witter 136m sh at $37 → $15; Allstate 340m at $29 → $29; stub ≈ $10
    r = SO.stub_value(54, 340e6, [(37, 136e6), (29, 340e6)])
    assert r["stake_values_per_parent_share"] == pytest.approx([14.8, 29.0], abs=0.05)
    assert r["stub_per_share"] == pytest.approx(10.2, abs=0.05)
    # Host: stock $3–5, debt ~$25/share: a ~15% rise in assets doubles the stock
    h = SO.leverage_doubling(4, 25)
    assert h["asset_rise_to_double_equity_pct"] == pytest.approx(13.8, abs=0.1)
    assert SO.leverage_doubling(0, 25) == {}


CALLS = """Alpha Industries Ltd. (ALPHA)
Conference call transcripts, oldest-first.
Call: Feb 2025
We have no plans to restructure. Demerger is not on the table.
Call: Nov 2025
On the demerger of the energy business: the scheme has been filed with the exchanges,
and we expect value unlocking for shareholders.
Call: May 2026
The spin-off is on track; record date will be announced. Separate listing targeted for Q3.
"""


def test_concall_mentions_window_the_last_twelve_months_with_quotes():
    secs = SO.concall_sections(CALLS)
    assert [l for l, _ in secs] == ["Call: Feb 2025", "Call: Nov 2025", "Call: May 2026"]
    ms = SO.concall_mentions(CALLS, today=TODAY)
    calls = {m["call"] for m in ms}
    assert calls == {"Nov 2025", "May 2026"}                 # Feb 2025 is outside the year
    terms = {m["term"].lower() for m in ms}
    assert "demerger" in terms and "spin-off" in terms and "separate listing" in terms
    assert all(m["quote"] for m in ms)
    assert SO.concall_mentions("no sections here", today=TODAY) == []


def test_financial_picture_reads_the_stored_statements_and_market_file():
    live = {"X": {"market_cap_rs_cr": "1000", "current_price_rs": "100", "stock_pe": "20", "fetched_at": "2026-08-02"},
            "P1": {"stock_pe": "30"}, "P2": {"stock_pe": "10"}, "P3": {"stock_pe": "40"}}
    ind = {"X": "Tools", "P1": "Tools", "P2": "Tools", "P3": "Tools"}
    f = SO.financial_picture("X", live, ind)
    assert f["market_cap_cr"] == 1000 and f["industry_median_pe"] == 30 and f["industry_peers"] == 3
    # a real company on file: numbers carry their year and source
    g = SO.financial_picture("SIEMENS")
    assert g["industry"] and g.get("borrowings_year") and g.get("net_profit_cr_year")


# ==================================================================== CLI

def test_judge_is_cached_by_document_and_abstains_without_a_runner(tmp_path, monkeypatch):
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    sit = {"symbol": "ALPHA", "company": "Alpha", "kind": "demerger", "stage": "listed",
           "first_filing": "2026-01-10", "facts": {}}
    calls = []
    def runner(prompt):
        calls.append(prompt)
        assert "Alpha" in prompt and "STRICT JSON" in prompt
        return 'preamble {"what_is_spun": "Energy", "reason": "focus", "reason_class": "unrelated", "quote": "q"} tail'
    j = AZ.judge(sit, SCHEME, "", allow_ai=True, runner=runner)
    assert j["status"] == "judged" and j["what_is_spun"] == "Energy"
    assert "FILINGS, COMPLETE" in calls[0] and "EARNINGS CALLS, COMPLETE" in calls[0]
    j2 = AZ.judge(sit, SCHEME, "", allow_ai=True, runner=runner)
    assert j2["status"] == "cached" and len(calls) == 1
    # a changed document re-judges; --quick abstains honestly
    AZ.judge(sit, SCHEME + " changed", "", allow_ai=True, runner=runner)
    assert len(calls) == 2
    assert AZ.judge({**sit, "symbol": "BETA"}, SCHEME, "", allow_ai=False)["status"] == "not assessed"
    assert AZ.judge({**sit, "symbol": "BETA"}, SCHEME, "", runner=lambda p: "garbage")["status"].startswith("judge failed")


def test_judge_answer_parsing_tolerates_fences_prose_and_retries_once(tmp_path, monkeypatch):
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    # fenced, with prose around it and a trailing comma — still read
    fenced = 'Here is the read:\n```json\n{"what_is_spun": "Energy", "n": [1, 2,],}\n```\nDone.'
    assert AZ._parse_json(fenced) == {"what_is_spun": "Energy", "n": [1, 2]}
    # a brace inside prose before the object does not derail the scan
    assert AZ._parse_json("note {not json} then {\"a\": 1}") == {"a": 1}
    assert AZ._parse_json("no object here") is None
    # a malformed first answer is asked again, once, with the JSON reminder
    asks = []
    def flaky(p):
        asks.append(p)
        return '{"what_is_spun": "Energy", "reason": "unterminated' if len(asks) == 1 else '{"what_is_spun": "Energy"}'
    j = AZ._ask("k1", "s1", "prompt", True, runner=flaky)
    assert j["status"] == "judged" and j["what_is_spun"] == "Energy"
    assert len(asks) == 2 and "not valid JSON" in asks[1] and asks[1].startswith("prompt")
    # two malformed answers fail honestly, and nothing is cached
    j2 = AZ._ask("k2", "s1", "prompt", True, runner=lambda p: "{broken")
    assert j2["status"] == "judge failed: bad json"
    assert "k2" not in AZ._cache() and "k1" in AZ._cache()


def test_run_writes_report_record_csvs_and_snapshot(tmp_path, monkeypatch):
    rows = _rows()
    texts = {"3": SCHEME}
    out = tmp_path / "out"
    monkeypatch.setattr(AZ, "OUT_DIR", out)
    monkeypatch.setattr(AZ, "REPORT", out / "SPINOFF_REPORT.md")
    monkeypatch.setattr(AZ, "LATEST", out / "spinoff_latest.json")
    monkeypatch.setattr(AZ, "SITUATIONS", out / "_situations.csv")
    monkeypatch.setattr(AZ, "MENTIONS", out / "_concall_mentions.csv")
    monkeypatch.setattr(AZ, "HISTORY", out / "history")
    monkeypatch.setattr(AZ, "COVERAGE", out / "_coverage.csv")
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    monkeypatch.setattr(SO, "load_filings", lambda path=None: rows)
    monkeypatch.setattr(SO, "load_text", lambda r: texts.get(r["ann_id"], ""))
    monkeypatch.setattr(SO, "concall_text", lambda sym: CALLS if sym == "ALPHA" else "")
    monkeypatch.setattr(FA, "universe", lambda: {"ALPHA": "Alpha Industries Ltd.", "BETA": "Beta"})
    monkeypatch.setattr(AZ, "_ai_available", lambda: False)

    monkeypatch.setattr(FN, "PNL", tmp_path / "pnl")
    monkeypatch.setattr(FN, "CASH", tmp_path / "cash")
    monkeypatch.setattr(FN, "PPT_DIR", tmp_path / "ppt")
    monkeypatch.setattr(FN, "AR_DIR", tmp_path / "ar")
    monkeypatch.setattr(FN, "LINKS", tmp_path / "ppt" / "_concall_links.csv")
    monkeypatch.setattr(FN, "CONCALLS", tmp_path / "cc")
    _write_pnl(tmp_path / "pnl" / "ALPHA.csv")

    class A:
        refresh = False; days = 365; no_bse = True; quick = True; no_calls = False; only = ""
        fetch_docs = False; as_of = TODAY.isoformat(); workers = 2
    AZ.cmd_run(A())
    md = (out / "SPINOFF_REPORT.md").read_text()
    assert "# Spin-offs and demergers" in md
    assert "## Confirmed demergers" in md and "| **ALPHA** | Alpha Energy Limited | record_date | RECORD DATE 2026-09-15" in md
    assert "> **Listing:** RECORD DATE 2026-09-15; Alpha Energy Limited not yet listed" in md
    assert "### The parent, last three fiscal years" in md and "| Sales (₹ cr) | 100 | 120 | 150 |" in md
    assert "| Sales growth (%) | +25.0% | +20.0% | +25.0% |" in md and "```mermaid" in md
    assert "**P/E:**" in md and "### The business being separated" in md
    assert "Alpha Energy Limited" in md and "1 for every 1" in md
    assert "SPINNING" in md and "On the calls" in md
    assert "Other restructurings on file" in md and "| ALPHA | merger |" in md
    assert "mechanical read only" in md
    rec = json.loads((out / "spinoff_latest.json").read_text())
    # the two filing-only CALLS mentions of ALPHA joined its spin situation as rows
    assert rec["meta"]["filings"] >= 5 and rec["situations"][0]["judge"]["status"] == "not assessed"
    assert "CALLS" in rec["situations"][0]["sources"]
    assert rec["situations"][0]["confidence"][0] == "confirmed"
    sits = list(csv.DictReader(open(out / "_situations.csv")))
    assert [s["kind"] for s in sits] == ["demerger", "merger"]
    assert sits[0]["resulting_company"] == "Alpha Energy Limited" and sits[0]["listing"] == "pending_record_date_set"
    cov = list(csv.DictReader(open(out / "_coverage.csv")))
    assert cov[0]["symbol"] == "ALPHA" and cov[0]["parent_pnl"] == "yes" and cov[0]["cash_flow"] == "no"
    ms = list(csv.DictReader(open(out / "_concall_mentions.csv")))
    assert {m["symbol"] for m in ms} == {"ALPHA"} and all(m["quote"] for m in ms)
    snap = out / "history" / TODAY.isoformat()
    assert (snap / "run.json").exists() and (snap / "SPINOFF_REPORT.md").exists()


def test_call_only_scan_finds_indications_without_filings(monkeypatch):
    monkeypatch.setattr(SO, "concall_text", lambda sym: CALLS if sym == "GAMMA" else "")
    c = AZ.call_only_scan(["GAMMA", "DELTA"], exclude=set(), today=TODAY)
    assert [x["symbol"] for x in c] == ["GAMMA"] and c[0]["n"] >= 2
    assert c[0]["latest"] == "May 2026" and c[0]["example"] and c[0]["forward"] >= 1
    assert AZ.call_only_scan(["GAMMA"], exclude={"GAMMA"}, today=TODAY) == []
    # a company only describing a past demerger, or denying one, is not an indication
    past = "Call: May 2026\nOne year post our demerger we completed the integration. We have no plan to demerge further."
    monkeypatch.setattr(SO, "concall_text", lambda sym: past)
    assert AZ.call_only_scan(["OLD"], exclude=set(), today=TODAY) == []


def test_tone_separates_plans_from_history_and_denials():
    assert SO.tone("we are evaluating a demerger of the energy business; the board will consider it next quarter") == "forward"
    assert SO.tone("one year post our demerger, the integration was completed") == "backward"
    assert SO.tone("there is no plan to demerge, as you said, at the moment") == "backward"
    ms = SO.concall_mentions(CALLS, today=TODAY)
    assert all("tone" in m for m in ms) and any(m["tone"] == "forward" for m in ms)


def test_boilerplate_does_not_read_as_stages_facts_or_reasons():
    boiler = ("Disclosure under Regulation 30 of SEBI (Listing Obligations and Disclosure "
              "Requirements) Regulations, 2015 — Listing Regulations. The scheme is subject to "
              "receipt of regulatory approvals. Details of pending actions against the Company, "
              "its promoters: nil. Pursuant to the above, equity shares were credited. Announcement.")
    assert SO.stage_of(boiler) is None
    f = SO.facts_in(boiler)
    assert "esop_pricing" not in f and "insider_continuity" not in f
    assert "insider_oversubscribe" not in SO.facts_in(boiler, rights=False)
    assert SO.reasons_in(boiler) == []
    assert SO.stage_of("Listing and commencement of trading of the equity shares of SKF "
                       "Industrial Limited (resulting company)") == "listed"
    assert SO.stage_of("Board approved the Scheme of Arrangement for demerger") == "announced"
    # a scheme's text that PROMISES a listing is not a listing event: stages come from headlines
    row = {"date": "2026-02-20", "symbol": "U", "company": "U", "source": "NSE", "category": "Scheme of Arrangement",
           "kind": "demerger", "tags": "demerger", "headline": "UPL has informed the Exchange about Scheme of Arrangement",
           "attachment": "", "ann_id": "77", "file_size": "", "text_file": ""}
    s = SO.build_situations([row], {"77": "the equity shares of the Resulting Company shall be listed on the stock exchanges"}, TODAY)[0]
    assert s["stage"] == "announced" and "listed" not in s["stage_dates"]
    g = SO.facts_in('between Alpha Ltd and JSW Energy Limited ("Resulting Company")')
    assert g["resulting_company"] == "JSW Energy Limited"
    assert "demerged_undertaking" not in SO.facts_in('"Demerged Undertaking" as defined in the Scheme;')


def test_news_only_filings_are_a_rumoured_situation():
    rows = [{"date": "2026-09-30", "symbol": "SUNTV", "company": "Sun TV", "source": "NSE",
             "category": "News Verification", "kind": "demerger", "tags": "demerger",
             "headline": "The Exchange has sought clarification w.r.t. news item captioned "
                         "Possible sports division demerger", "attachment": "", "ann_id": "9",
             "file_size": "", "text_file": ""},
            {**{"date": "2026-09-30", "symbol": "SUNTV", "company": "Sun TV", "source": "NSE",
                "category": "Clarification", "kind": "demerger", "tags": "demerger",
                "headline": "Sun TV denies CNBC-TV18 rumor of possible sports division demerger",
                "attachment": "", "ann_id": "10", "file_size": "", "text_file": ""}}]
    s = SO.build_situations(rows, {}, TODAY)[0]
    assert s["stage"] == "rumoured" and s["facts"].get("news_only") is True
    assert SO.verdict(s, SO.checklist(s, {}, [], TODAY))["label"].startswith("RUMOURED")



# ============================================================= financials

def _write_pnl(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(",parent_line_item,Mar 2023,Mar 2024,Mar 2025,Mar 2026\n"
                    "Sales,,80,100,120,150\nOperating Profit,,8,12,18,30\nOPM %,,10,12,15,20\n"
                    "Net Profit,,4,5,9,15\nEPS in Rs,,2,2.5,4.5,7.5\n")


def test_parent_financials_three_years_with_growth_and_margins(tmp_path, monkeypatch):
    monkeypatch.setattr(FN, "PNL", tmp_path)
    _write_pnl(tmp_path / "X.csv")
    f = FN.parent_financials("X")
    assert f["available"] and f["years"] == ["Mar 2024", "Mar 2025", "Mar 2026"]
    rows = {r["metric"]: r["values"] for r in f["rows"]}
    assert rows["Sales (₹ cr)"] == [100, 120, 150]
    assert rows["Sales growth (%)"] == [25.0, 20.0, 25.0]          # 80→100 uses the fourth year
    assert rows["Operating margin (%)"] == [12.0, 15.0, 20.0]
    assert rows["PAT growth (%)"] == [25.0, 80.0, 66.7] and rows["PAT margin (%)"] == [5.0, 7.5, 10.0]
    assert not FN.parent_financials("NOPE")["available"]
    charts = FN.charts_for(f)
    assert len(charts) == 2 and 'x-axis ["Mar 2024", "Mar 2025", "Mar 2026"]' in charts[0]
    assert "bar [100, 120, 150]" in charts[0] and "line [12, 15, 20]" in charts[1]


def test_mermaid_chart_leaves_out_series_with_gaps():
    c = FN.mermaid_chart("t", ["a", "b"], {"ok": [1, 2], "gap": [1, None]}, "y")
    assert "bar [1, 2]" in c and "gap" in c and "Not plotted" in c
    assert FN.mermaid_chart("t", ["a", "b"], {"gap": [1, None]}, "y") == ""


def test_cash_flows_and_pe_fallback(tmp_path, monkeypatch):
    monkeypatch.setattr(FN, "CASH", tmp_path)
    (tmp_path / "X.csv").write_text(",parent_line_item,Mar 2024,Mar 2025,Mar 2026\n"
                                    "Cash from Operating Activity,,10,20,30\nFree Cash Flow,,5,8,12\n")
    cf = FN.cash_flows("X")
    assert cf["available"] and cf["years"] == ["Mar 2024", "Mar 2025", "Mar 2026"]
    assert {r["metric"]: r["values"] for r in cf["rows"]}["Free cash flow (₹ cr)"] == [5, 8, 12]
    # P/E: live file first, else close ÷ EPS with the method stated
    assert FN.pe_ratio("X", {"X": {"stock_pe": "22.5", "current_price_rs": "100", "fetched_at": "2026-08-02"}})["pe"] == 22.5
    monkeypatch.setattr(FN, "PNL", tmp_path)
    _write_pnl(tmp_path / "X.csv")
    monkeypatch.setattr(FN, "_CLOSE_CACHE", {"X": ("2026-10-01", 150.0)})
    pe = FN.pe_ratio("X", {})
    assert pe["pe"] == 20.0 and "EPS 7.5" in pe["method"] and pe["as_of"] == "2026-10-01"
    assert FN.pe_ratio("NONE", {})["pe"] is None


def test_segment_excerpts_pick_number_dense_pages_with_the_business_name(tmp_path, monkeypatch):
    monkeypatch.setattr(FN, "AR_DIR", tmp_path / "ar")
    monkeypatch.setattr(FN, "PPT_DIR", tmp_path / "ppt")
    monkeypatch.setattr(FN, "LINKS", tmp_path / "ppt" / "_concall_links.csv")
    d = tmp_path / "ar" / "X"; d.mkdir(parents=True)
    (d / "_index.csv").write_text("symbol,kind,label,url,file,text_file,pages,status,fetched\n"
                                  "X,annual_report,Annual Report 2026,https://b/ar.pdf,a.pdf,a.txt,3,ok,2026-10-12\n")
    (d / "a.txt").write_text("\n=== page 1 ===\nSterling is our hospitality arm. Segment information follows later.\n"
                             "\n=== page 2 ===\nSegment revenue: Travel 5,000 Sterling 450 Forex 1,200; Segment results Sterling 85\n"
                             "\n=== page 3 ===\nNothing here\n")
    ex = FN.segment_excerpts("X", ["Sterling Holiday Resorts Limited"])
    # page 3 rides along as the continuation of the segment table on page 2
    assert [e["page"] for e in ex] == [1, 2, 3] and ex[1]["numbers"] > ex[0]["numbers"]
    # the segment note is wanted even when it never names the brand
    (d / "a.txt").write_text("\n=== page 1 ===\nSegment revenue " + " ".join(f"{i*113:,}" for i in range(30)) + "\n")
    assert [e["page"] for e in FN.segment_excerpts("X", ["Sterling"])] == [1]
    assert ex[0]["doc"] == "Annual Report 2026" and ex[0]["url"] == "https://b/ar.pdf"
    assert FN.pages_of("\n=== page 7 ===\nabc") == [(7, "abc")]
    assert FN.segment_excerpts("X", []) == []


def test_segment_table_computes_growth_from_extracted_numbers():
    seg = {"unit": "₹ crore", "years": [
        {"fy": "FY2024", "revenue": 400, "operating_profit": 80, "pat": None, "source": "AR 2024 — page 150"},
        {"fy": "FY2025", "revenue": 450, "operating_profit": 90, "pat": 40, "source": "AR 2025 — page 161"},
        {"fy": "FY2026", "revenue": 540, "operating_profit": 99, "pat": 50, "source": "AR 2026 — page 170"}]}
    st = AZ.segment_table(seg)
    rows = {r["metric"]: r["values"] for r in st["rows"]}
    assert st["available"] and st["years"] == ["FY2024", "FY2025", "FY2026"]
    assert rows["Revenue growth (%)"] == [None, 12.5, 20.0] and rows["Operating margin (%)"] == [20.0, 20.0, 18.3]
    assert rows["PAT growth (%)"] == [None, None, 25.0] and st["found_numbers"] == 8
    assert not AZ.segment_table({"years": []})["available"]


def test_confidence_and_listing_status_follow_the_record():
    sits = SO.build_situations(_rows(), {"3": SCHEME}, TODAY)
    s = sits[0]
    assert SO.confidence(s) == ("confirmed", "a demerger scheme is on the exchange record")
    L = SO.listing_status(s, {}, TODAY)
    assert L["state"] == "pending_record_date_set" and "RECORD DATE 2026-09-15" in L["text"]
    later = SO.build_situations(_rows(), {"3": SCHEME}, dt.date(2026, 11, 20))[0]
    assert SO.listing_status(later, {}, dt.date(2026, 11, 20))["state"] == "listed"
    pre = SO.build_situations(_rows()[:2], {}, TODAY)[0]
    L = SO.listing_status(pre, {"listing_timeline": "listing expected by Q4 FY27 (Feb 2026 call)"}, TODAY)
    assert L["state"] == "not_yet" and "Q4 FY27" in L["text"]
    assert SO.listing_status(sits[1], {}, TODAY)["state"] == "not_a_spin"
    rum = {**pre, "stage": "rumoured", "facts": {"news_only": True}, "headlines": []}
    assert SO.confidence(rum)[0] == "indicated" and SO.listing_status(rum, {}, TODAY)["state"] == "no_scheme"
    ipo = {**pre, "kind": "subsidiary_listing"}
    assert SO.confidence(ipo)[0] == "probable" and SO.listing_status(ipo, {}, TODAY)["state"] == "subsidiary_ipo"



def test_resulting_company_never_the_parent_and_listing_has_a_short_form():
    rows = _rows()[:1]
    s = SO.build_situations(rows, {"1": 'Alpha Industries Limited ("Resulting Company")'}, TODAY)[0]
    assert "resulting_company" not in s["facts"]                     # the parent itself
    s = SO.build_situations(rows, {"1": 'In the case of Alpha Energy Limited ("Resulting Company")'}, TODAY)[0]
    assert s["facts"]["resulting_company"] == "Alpha Energy Limited"
    L = SO.listing_status(s, {}, TODAY)
    assert L["short"].startswith("NOT YET (announced)")
    full = SO.build_situations(_rows()[:4], {"3": SCHEME}, TODAY)[0]
    assert SO.listing_status(full, {}, TODAY)["short"] == "RECORD DATE 2026-09-15; listing pending"
    assert AZ.entity_cell({"facts": {}, "judge": {"what_is_spun": "the ice-cream business"}}) == "the ice-cream business"
    assert AZ.entity_cell({"facts": {}, "judge": {"what_is_spun": "not stated"}}) == "—"



def test_an_amalgamation_order_is_not_a_demerger_and_the_judge_can_demote():
    # a composite scheme that demerges AND amalgamates is a demerger (Cello);
    # an amalgamation order that mentions "demerger" in passing is left to the judge
    assert SO.refine_kind({"kind": "scheme_other"}, "demerger " * 15 + "amalgamation " * 16) == "demerger"
    assert SO.refine_kind({"kind": "merger"}, "amalgamation " * 12 + "demerger " * 3) == "merger"
    assert SO.refine_kind({"kind": "scheme_other"}, "demerger " * 6 + "amalgamation " * 2) == "demerger"
    sit = {"kind": "demerger", "stage": "exchange_noc", "facts": {}, "days_since_first": 10,
           "listed_on": None, "days_since_listing": None, "reasons": [], "headlines": []}
    j = {"status": "judged", "what_is_spun": "Nothing; documents describe amalgamation of Sesa Care "
         "Private Limited into Dabur India, not a demerger", "parent_or_spin": "neither",
         "selling_pressure": "unlikely", "reason": "brand acquisition"}
    assert SO.judge_override(sit, j)[0] == "merger"
    j2 = {"status": "judged", "what_is_spun": "Ice cream business demerged into Kwality Wall's",
          "parent_or_spin": "spin", "selling_pressure": "likely", "reason": "focus"}
    assert SO.judge_override({**sit, "company": "Hindustan Unilever Ltd."}, j2)[0] is None
    # Eris: acquisitions dressed as a scheme; Gabriel: a business demerged INTO the listed company
    je = {"status": "judged", "what_is_spun": "not stated — the documents describe acquisitions (Swiss Parenterals 30% stake)",
          "parent_or_spin": "neither", "selling_pressure": "unclear", "reason": "stake purchases"}
    assert SO.judge_override({**sit, "company": "Eris Lifesciences Ltd."}, je)[0] == "other"
    jg = {"status": "judged", "what_is_spun": "Automotive Undertaking of Asia Investments Private Limited demerged into Gabriel India Limited",
          "parent_or_spin": "neither", "selling_pressure": "unclear", "reason": "consolidation"}
    kind, why = SO.judge_override({**sit, "company": "Gabriel India Ltd."}, jg)
    assert kind == "other" and "inbound" in why
    # …and when the judge itself calls the company the 'spin', the DIRECTION
    # read from the scheme text still demotes it, with no judge at all
    jg2 = {**jg, "what_is_spun": "Automotive Undertaking of Asia Investments: drivetrain, forgings", "parent_or_spin": "spin"}
    assert SO.judge_override({**sit, "company": "Gabriel India Ltd."}, jg2)[0] is None
    inbound = {**sit, "company": "Gabriel India Ltd.",
               "facts": {"direction": "inbound", "direction_quote": "Gabriel India Limited (the “Resulting Company”)"}}
    kind, why = SO.judge_override(inbound, jg2)
    assert kind == "other" and "Resulting Company" in why
    assert SO.judge_override(inbound, {"status": "not assessed"})[0] == "other"
    # Prestige: a subsidiary IPO whose DRHP was withdrawn is NOT an amalgamation
    j3 = {"status": "judged", "what_is_spun": "Subsidiary Prestige Hospitality Ventures via IPO; DRHP now withdrawn",
          "parent_or_spin": "unclear", "selling_pressure": "unclear",
          "reason": "Not stated for the separation itself; the DRHP was withdrawn"}
    assert SO.judge_override({**sit, "kind": "subsidiary_listing"}, j3)[0] is None
    assert SO.judge_override(sit, j3)[0] is None
    j4 = {"status": "judged", "what_is_spun": "not stated — documents concern a Section 9 insolvency petition",
          "parent_or_spin": "neither", "selling_pressure": "unclear", "reason": "n/a"}
    assert SO.judge_override(sit, j4)[0] == "merger"
    assert "demerged_undertaking" not in SO.facts_in('"Demerged Undertaking" means with the total revenue and net.')


def test_dividend_record_dates_and_own_share_allotments_are_not_scheme_stages():
    assert SO.stage_of("Record Date | Record date for the purpose of Dividend is 16-Jan-2026") is None
    assert SO.stage_of("Record date for the purpose of Interim Dividend is 16-Feb-2026") is None
    assert SO.stage_of("Record date for the purpose of Scheme of Arrangement (demerger) is 10-Jan-2026") == "record_date"
    # the company allotting ITS OWN shares under a scheme is a merger / inbound allotment, not the spin-off listing
    assert SO.stage_of("Record date for the purpose of Allotment of equity shares of the Company in accordance with the Scheme") == "record_date"
    assert SO.stage_of("Allotment of equity shares by the Resulting Company pursuant to the Scheme") == "listed"
    # SEBI boilerplate is not a listing event; a dividend record date fixed in a body is not the scheme's
    assert SO.stage_from_text("on all the stock exchanges where the equity shares of the listed entity are/were listed.") is None
    assert SO.stage_from_text("The equity shares of the Resulting Company were listed and admitted to dealings on NSE.") == "listed"
    assert SO.stage_from_text("The record date has been fixed as 16 January 2026 for the purpose of the interim dividend.") is None
    assert SO.stage_from_text("The record date has been fixed as 16 January 2026 for the demerger.") == "record_date"


def test_register_guard_drops_a_record_date_the_exchange_does_not_know(monkeypatch):
    row = {"date": "2026-01-10", "symbol": "HCL", "company": "HCL Tech Ltd", "source": "NSE",
           "category": "Record Date", "kind": "demerger", "tags": "demerger",
           "headline": "Record date for the purpose of Scheme of Arrangement is 10-Jan-2026", "attachment": "",
           "ann_id": "r1", "file_size": "", "text_file": ""}
    monkeypatch.setattr(SO, "_REGISTER", {"HINDUNILVR": ["2025-12-05"]})
    s = SO.build_situations([row], {"r1": ""}, today=dt.date(2026, 6, 1))[0]
    assert s["stage"] == "announced" and s["listed_on"] is None and "register" in s["facts"]["register_note"]
    # with the exchange's own record date, the claim stands
    monkeypatch.setattr(SO, "_REGISTER", {"HCL": ["2026-01-10"]})
    s = SO.build_situations([row], {"r1": ""}, today=dt.date(2026, 6, 1))[0]
    assert s["stage"] == "record_date" and s["listed_on"] == "2026-01-10"
    # too recent to be in the register yet: not touched; no register at all: not touched
    monkeypatch.setattr(SO, "_REGISTER", {"HINDUNILVR": ["2025-12-05"]})
    assert SO.build_situations([row], {"r1": ""}, today=dt.date(2026, 1, 20))[0]["stage"] == "record_date"
    monkeypatch.setattr(SO, "_REGISTER", {})
    assert SO.build_situations([row], {"r1": ""}, today=dt.date(2026, 6, 1))[0]["stage"] == "record_date"


def test_confirmed_needs_a_scheme_named_on_the_exchange_record_and_the_judge_moves_it():
    base = {"symbol": "X", "company": "X Ltd", "kind": "demerger", "stage": "announced", "facts": {}}
    results = [{"date": "2026-01-12", "category": "Outcome of Board Meeting", "kind": "demerger",
                "headline": "X Ltd has submitted the financial results for the quarter", "attachment": ""}]
    named = [{"date": "2026-01-12", "category": "Outcome of Board Meeting", "kind": "demerger",
              "headline": "Board approved the Scheme of Arrangement for demerger of the cement business", "attachment": ""}]
    call = [{"date": "2026-04-30", "category": "Earnings call Apr 2026", "kind": "demerger",
             "headline": "…we plan to demerge the airports business…", "attachment": ""}]
    assert not SO.scheme_named(results) and SO.scheme_named(named) and not SO.scheme_named(call)
    assert SO.confidence({**base, "headlines": results})[0] == "probable"
    assert SO.confidence({**base, "headlines": named})[0] == "confirmed"
    assert SO.confidence({**base, "headlines": [{"date": "2026-01-01", "category": "Demerger", "kind": "demerger",
                                                 "headline": "Intimation", "attachment": ""}]})[0] == "confirmed"
    # the judge: 'nothing separated' demotes even when it calls the company the parent
    j_nothing = {"status": "judged", "what_is_spun": "Nothing is separated; two wholly-owned subsidiaries are merged into the listed parent",
                 "parent_or_spin": "parent", "selling_pressure": "unlikely", "reason": "amalgamation rationale"}
    assert SO.judge_override({**base, "headlines": named}, j_nothing)[0] == "merger"
    j_none = {**j_nothing, "what_is_spun": "Nothing is spun off; a stake was bought", "reason": "stake"}
    assert SO.judge_override({**base, "headlines": named}, j_none)[0] == "other"
    # a demerger only on the calls, which the judge cannot find in the filed scheme → indicated on calls
    j_no = {"status": "judged", "what_is_spun": "No ANIL demerger scheme in documents; management plans demergers of Airports, Roads",
            "parent_or_spin": "parent", "selling_pressure": "unclear", "reason": "plans"}
    sit = {**base, "headlines": call + [{"date": "2026-04-01", "category": "Scheme of Arrangement", "kind": "scheme_other",
                                        "headline": "Effective Date of the Composite Scheme", "attachment": ""}],
           "confidence": ("confirmed", "")}
    conf, stage = SO.judge_adjust(sit, j_no)
    assert conf[0] == "indicated" and stage == "indicated_on_calls"
    # a text-only (probable) demerger is NOT promoted on the judge's word: results notes describe
    # completed demergers (SCI's land company), inbound ones (UltraTech taking Kesoram's cement)
    j_yes = {"status": "judged", "what_is_spun": "192 non-core assets transferred to a separate asset company, 185 leased back",
             "parent_or_spin": "parent", "selling_pressure": "likely", "reason": "focus"}
    assert SO.judge_adjust({**base, "headlines": results, "confidence": ("probable", "")}, j_yes) == (None, None)
    assert SO.judge_adjust({**base, "headlines": named, "confidence": ("confirmed", "")}, j_yes) == (None, None)
    assert SO.judge_adjust({**base, "kind": "subsidiary_listing", "headlines": named, "confidence": ("probable", "")}, j_yes) == (None, None)
    # inbound by the judge's words: "vested in <this company>"
    j_in = {"status": "judged", "what_is_spun": "Kesoram Industries' Cement Business Division, transferred out of Kesoram and vested in UltraTech as a going concern",
            "parent_or_spin": "parent", "selling_pressure": "unlikely", "reason": "consolidation"}
    kind, why = SO.judge_override({**base, "company": "UltraTech Cement Limited", "headlines": results}, j_in)
    assert kind == "other" and "inbound" in why
    # a slump sale: the business leaves for cash; nothing is listed for the holders
    j_sale = {"status": "judged", "what_is_spun": "The Robotics Business — a sales channel with maintenance support — sold on slump sale basis to ABB Robotics India",
              "parent_or_spin": "parent", "selling_pressure": "unclear", "reason": "portfolio",
              "listing_timeline": "No listing: the postal ballot notice says size, nature and scale did not warrant creation of a separate entity"}
    kind, why = SO.judge_override({**base, "company": "ABB India Limited", "headlines": results}, j_sale)
    assert kind == "other" and "slump sale" in why
    j_bosch = {**j_sale, "what_is_spun": "No demerger stated; documents describe sale of the Video solutions business", "listing_timeline": "not stated"}
    assert SO.judge_override({**base, "company": "Bosch Limited", "headlines": results}, j_bosch)[0] == "other"
    # …but a demerger whose rationale mentions a past sale is left alone
    j_real = {"status": "judged", "what_is_spun": "The ice cream business, demerged into a separately listed company",
              "parent_or_spin": "parent", "selling_pressure": "likely", "reason": "after the sale of the water business, focus", "listing_timeline": "not stated"}
    assert SO.judge_override({**base, "company": "HUL", "headlines": named}, j_real)[0] is None


def test_demerger_direction_reads_resulting_and_demerged_roles():
    gabriel = ("Scheme of Arrangement between Asia Investments Private Limited (the “Demerged Company”) and "
               "Gabriel India Limited (the “Resulting Company”) providing for the demerger of the Automotive "
               "Undertaking of Asia Investments Private Limited into Gabriel India Limited.")
    d, q = SO.demerger_direction(gabriel, "Gabriel India Limited")
    assert d == "inbound" and "Resulting Compan" in q
    hul = ("Scheme of Arrangement amongst Hindustan Unilever Limited (Demerged Company) and Kwality Wall's "
           "(India) Limited (Resulting Company) for the demerger of the Ice Cream Business of Hindustan "
           "Unilever Limited into Kwality Wall's (India) Limited.")
    assert SO.demerger_direction(hul, "Hindustan Unilever Ltd.")[0] == "outbound"
    # 'Ltd.' in the filing, 'Limited' in the universe name; abbreviations too
    assert SO.demerger_direction("Vedanta Ltd. (“Demerged Company”) and Vedanta Aluminium Metal Limited", "Vedanta Limited")[0] == "outbound"
    assert SO.demerger_direction("nothing about roles here", "Gabriel India Limited") == ("", "")
    # both roles named for the same company (a composite scheme) settles nothing
    both = gabriel + " Gabriel India Limited (the “Demerged Company” for Part D)."
    assert SO.demerger_direction(both, "Gabriel India Limited")[0] == ""


def test_inbound_demerger_is_marked_in_the_situation(monkeypatch):
    rows = [{"date": "2026-01-10", "symbol": "GAB", "company": "Gabriel India Limited", "source": "NSE",
             "category": "Demerger", "kind": "demerger", "tags": "demerger",
             "headline": "Scheme of Arrangement — demerger", "attachment": "x.pdf", "ann_id": "g1",
             "file_size": "", "text_file": ""}]
    texts = {"g1": "Asia Investments Private Limited (the “Demerged Company”) and Gabriel India Limited "
                   "(the “Resulting Company”): demerger of the Automotive Undertaking into Gabriel India Limited."}
    sits = SO.build_situations(rows, texts, today=dt.date(2026, 6, 1))
    assert sits[0]["kind"] == "demerger" and sits[0]["facts"]["direction"] == "inbound"
    hul_rows = [{**rows[0], "symbol": "HUL", "company": "Hindustan Unilever Limited", "ann_id": "h1"}]
    hul_texts = {"h1": "Hindustan Unilever Limited (Demerged Company) and Kwality Wall's (India) Limited (Resulting Company)"}
    assert SO.build_situations(hul_rows, hul_texts, today=dt.date(2026, 6, 1))[0]["facts"]["direction"] == "outbound"



def test_resulting_company_must_look_like_a_company_name():
    good = 'the Resulting Company, i.e. Talwandi Sabo Power Limited'
    assert SO.facts_in(good)["resulting_company"] == "Talwandi Sabo Power Limited"
    assert SO.facts_in('Sriam Labs Private Limited ("Resulting Company")')["resulting_company"] == "Sriam Labs Private Limited"
    for bad in ('No. 1 is a public limited ("Resulting Company")', 'Essentials Limited ("Resulting Company")',
                'the Resulting Company, i.e. Public Limited', 'Investments Limited ("Resulting Company")'):
        assert "resulting_company" not in SO.facts_in(bad), bad



def test_withdrawn_proposals_are_marked_and_bare_nclt_is_not_a_scheme():
    rows = [{"date": "2026-03-31", "symbol": "P", "company": "P Ltd", "source": "NSE", "category": "Updates",
             "kind": "subsidiary_listing", "tags": "subsidiary_listing", "headline": "Filing of DRHP by subsidiary",
             "attachment": "", "ann_id": "1", "file_size": "", "text_file": ""},
            {"date": "2026-09-25", "symbol": "P", "company": "P Ltd", "source": "NSE", "category": "General Updates",
             "kind": "subsidiary_listing", "tags": "subsidiary_listing", "headline": "Withdrawal of DRHP by Subsidiary",
             "attachment": "", "ann_id": "2", "file_size": "", "text_file": ""}]
    s = SO.build_situations(rows, {}, TODAY)[0]
    assert s["stage"] == "withdrawn" and s["facts"]["withdrawn_on"] == "2026-09-25"
    assert SO.confidence(s)[0] == "indicated" and SO.listing_status(s, {}, TODAY)["state"] == "withdrawn"
    assert SO.verdict(s, SO.checklist(s, {}, [], TODAY))["label"].startswith("WITHDRAWN")
    assert FA.classify("Updates", "copy of the order passed by NCLT on the insolvency petition") == ("", [])
    assert FA.classify("Updates", "NCLT sanctioned the Scheme of Arrangement")[0] == "scheme_other"



def test_board_meeting_purposes_and_bare_outcomes_feed_the_classifier():
    members = {"NATCOPHARM": "Natco Pharma Ltd.", "COALINDIA": "Coal India Ltd."}
    bm = [{"bm_symbol": "NATCOPHARM", "bm_date": "24-Mar-2026", "bm_purpose": "Scheme of arrangement",
           "bm_desc": "To consider Scheme of arrangement (demerger)", "bm_timestamp": "24-Mar-2026 09:00:00",
           "attachment": "https://x/n.pdf", "attFileSize": "1 MB"},
          {"bm_symbol": "NATCOPHARM", "bm_date": "20-May-2026", "bm_purpose": "Financial Results",
           "bm_desc": "To consider audited results", "bm_timestamp": "20-May-2026 09:00:00"},
          {"bm_symbol": "OTHER", "bm_date": "24-Mar-2026", "bm_desc": "demerger", "bm_timestamp": "x"}]
    rows = FA.board_meeting_rows(bm, members)
    assert len(rows) == 1 and rows[0]["kind"] == "demerger" and rows[0]["source"] == "NSE-BM"
    assert rows[0]["date"] == "2026-03-24" and rows[0]["ann_id"].startswith("bm")
    assert FA.classify("General Updates", "In-principle approval of Listing of South Eastern Coalfields "
                       "Limited (SECL), a Wholly owned subsidiary")[0] == "subsidiary_listing"
    assert FA.classify("Record Date", "Record date fixed in consultation with the Resulting Company "
                       "i.e. HEG Graphite Limited")[0] == "demerger"
    assert FA.is_bare_outcome("Outcome of Board Meeting", "X Ltd has informed the Exchange about Outcome of Board Meeting")
    assert FA.is_bare_outcome("Outcome of Board Meeting", "Outcome of Board Meeting held on 12 May 2026")
    assert not FA.is_bare_outcome("Outcome of Board Meeting", "Outcome of Board Meeting - approval of the demerger of X")
    assert not FA.is_bare_outcome("Updates", "Outcome of Board Meeting")



def test_preferential_issues_are_captured_and_who_is_buying_is_rendered(monkeypatch):
    assert FA.classify("Updates", "Affle 3i Limited has informed the Exchange regarding 'allotment of warrants '.") \
        == ("preferential_issue", ["preferential_issue"])
    assert FA.classify("Allotment of Securities", "allotment of 6058394 securities pursuant to Preferential Issue")[0] == "preferential_issue"
    assert FA.classify("Monitoring Agency Report", "utilisation of preferential issue proceeds") == ("", [])
    f = SO.offering_facts("allotment of 36,00,000 convertible warrants at an issue price of Rs. 1,650 per warrant "
                          "aggregating to Rs. 594 crores to persons belonging to the promoter group on a preferential basis")
    assert f["instrument"] == "warrants" and f["securities"] == "36,00,000" and f["issue_price"] == "1,650"
    assert f["amount"] == "₹594 crores" and f["promoters_buying"] is True
    rows = [{"date": "2026-06-18", "symbol": "AFFLE", "company": "Affle 3i Ltd.", "source": "NSE", "category": "Updates",
             "kind": "preferential_issue", "tags": "preferential_issue", "headline": "allotment of warrants",
             "attachment": "https://x/w.pdf", "ann_id": "77", "file_size": "1 MB", "text_file": ""}]
    s = SO.build_situations(rows, {"77": "allotment of 36,00,000 warrants at an issue price of Rs. 1,650 to the promoter group"}, TODAY)[0]
    assert s["kind"] == "preferential_issue" and s["facts"]["instrument"] == "warrants"
    assert SO.verdict(s, SO.checklist(s, {}, [], TODAY))["label"].startswith("PREFERENTIAL ISSUE")
    s["offering"] = {"status": "judged", "instrument": "warrants", "total_amount": "₹594 crore", "issue_price": "₹1,650",
                     "allottees": [{"name": "Anuj Khanna Sohum", "category": "promoter", "securities": "20,00,000", "amount": "₹330 cr"},
                                   {"name": "Malabar India Fund", "category": "institution", "securities": "16,00,000", "amount": "₹264 cr"}],
                     "promoter_share_of_issue": "56%", "promoter_intent": "not stated", "upfront_paid": "25% upfront, 18 months",
                     "purpose": "growth capital", "stage": "allotted", "quote": "allotted to Anuj Khanna Sohum, promoter"}
    md = "\n".join(AZ.render_offerings([s]))
    assert "who is buying" in md and "| **AFFLE** | warrants | ₹594 crore | ₹1,650 |" in md
    assert "**Anuj Khanna Sohum** (promoter)" in md and "Malabar India Fund (institution)" in md and "yes (56%)" in md
    assert AZ.offering_rows([s])[0]["promoters_buying"] == "yes"
    assert AZ.render_offerings([])[-2] == "- (none on file)"



# ============================================ reading the documents, not headlines

def test_classify_all_is_multi_label_from_headline_and_first_pages():
    kind, tags = DR.classify_all("Outcome of Board Meeting", "Outcome of Board Meeting",
                                 "The Board approved the Scheme of Arrangement providing for the demerger of the "
                                 "Energy business into the Resulting Company, and the amalgamation of Alpha Power into "
                                 "Alpha Energy; a further amalgamation of two subsidiaries is proposed.")
    assert kind == "demerger" and tags == ["demerger", "merger", "scheme_other"]
    # a single passing word in a body is not enough for the heavy kinds
    assert DR.classify_text("the demerger of 2019 is referred to once") == []
    assert DR.classify_text("rights issue of equity shares; letter of offer") == ["rights_issue"]
    # the headline still counts on its own, text or no text
    assert DR.classify_all("Updates", "allotment of warrants", "")[1] == ["preferential_issue"]
    assert DR.eligible({"category": "Dividend", "attachment": "https://x/a.pdf", "file_size": "1 MB"}) == "noise-category"
    assert DR.eligible({"category": "Updates", "attachment": "https://x/a.pdf", "file_size": "12 MB"}).startswith("skipped:size")
    assert DR.eligible({"category": "Updates", "attachment": "https://x/a.pdf", "file_size": "3 MB"}) == ""


def test_stage_from_text_reads_events_and_ignores_promises():
    assert SO.stage_from_text("the Resulting Company is proposed to be listed; the scheme shall become effective upon approval") is None
    assert SO.stage_from_text("the Hon'ble NCLT, Mumbai Bench has sanctioned the Scheme vide order dated 24 September 2026") == "nclt_sanction"
    assert SO.stage_from_text("the record date has been fixed as Friday, 15 September 2026") == "record_date"
    assert SO.stage_from_text("the equity shares were listed and admitted to dealings on NSE") == "listed"
    assert SO.stage_from_text("received observation letter with no adverse observations from BSE") == "exchange_noc"
    assert SO.stage_from_text("the Board has approved the Scheme of Arrangement for the demerger") == "announced"
    # a bare-headline filing takes its stage from its document
    row = {"date": "2026-06-20", "symbol": "ALPHA", "company": "Alpha", "source": "NSE", "category": "Outcome of Board Meeting",
           "kind": "demerger", "tags": "demerger", "headline": "Outcome of Board Meeting", "attachment": "",
           "ann_id": "5", "file_size": "", "text_file": ""}
    s = SO.build_situations([row], {"5": "The Hon'ble NCLT has sanctioned the Scheme of Arrangement for the demerger today."}, TODAY)[0]
    assert s["stage"] == "nclt_sanction"


def test_a_filing_joins_every_family_its_tags_cover():
    row = {"date": "2026-05-15", "symbol": "CELLO", "company": "Cello", "source": "NSE", "category": "Scheme of Arrangement",
           "kind": "demerger", "tags": "demerger|merger", "headline": "Composite Scheme of Arrangement",
           "attachment": "", "ann_id": "9", "file_size": "", "text_file": ""}
    sits = SO.build_situations([row], {}, TODAY)
    assert sorted(s["kind"] for s in sits) == ["demerger", "merger"]
    assert all(s["n_filings"] == 1 for s in sits)


def test_calls_are_a_source_of_situations():
    members = {"GAMMA": "Gamma Ltd.", "DELTA": "Delta Ltd."}
    texts = {"GAMMA": CALLS, "DELTA": "Call: May 2026\nOne year post our demerger the integration is complete; no plan to demerge."}
    rows = SO.concall_candidates(["GAMMA", "DELTA"], members, TODAY, links={"GAMMA": {"May 2026": "https://t/x.pdf"}},
                                 text_of=lambda s: texts.get(s, ""))
    assert {r["symbol"] for r in rows} == {"GAMMA"}                 # DELTA's mentions are backward-looking
    assert all(r["source"] == "CALLS" and r["kind"] in ("demerger", "scheme_other", "subsidiary_listing") for r in rows)
    assert any(r["attachment"] == "https://t/x.pdf" for r in rows if r["category"].endswith("May 2026"))
    s = SO.build_situations(rows, {}, TODAY)[0]
    assert s["sources"] == ["CALLS"] and s["stage"] == "indicated_on_calls"
    assert SO.confidence(s)[0] == "indicated" and SO.listing_status(s, {}, TODAY)["state"] == "no_filing"


def test_complete_documents_are_assembled_within_budget(tmp_path, monkeypatch):
    rows = [{"symbol": "X", "date": f"2026-0{i}-01", "category": "Updates", "headline": f"filing {i}", "ann_id": str(i),
             "source": "NSE", "text_file": "", "kind": "demerger", "tags": "demerger"} for i in range(1, 5)]
    texts = {"1": "a" * 1000, "2": "b" * 1000, "3": "c" * 1000, "4": "d" * 1000}
    monkeypatch.setattr(SO, "load_text", lambda r: texts.get(r["ann_id"], ""))
    monkeypatch.setattr(SO, "load_first_pages", lambda r: "")
    full = AZ.scheme_text_for({"symbol": "X"}, rows, budget=10_000)
    assert full.startswith("[4 filings in full]") and full.index("filing 4") < full.index("filing 1")   # newest first
    cut = AZ.scheme_text_for({"symbol": "X"}, rows, budget=2_300)
    assert "2 older filings omitted" in cut and "dddd" in cut and "aaaa" not in cut
    monkeypatch.setattr(SO, "concall_text", lambda sym: CALLS)
    monkeypatch.setattr(FN, "doc_links", lambda sym: {"calls": {"May 2026": "https://t/may.pdf"}, "annual_reports": [], "presentations": []})
    c = AZ.calls_text_for("X", 12, TODAY)
    assert c.startswith("[2 calls in full]") and "### CALL May 2026 · https://t/may.pdf" in c and "Feb 2025" not in c
    assert "spin-off is on track" in c                                  # the whole section, not a snippet



def test_pdf_text_with_lone_surrogates_is_still_written():
    bad = "Scheme of Arrangement \ud83d demerger of the Energy business"
    assert "\ud83d" not in DR.clean_text(bad) and "demerger" in DR.clean_text(bad)
    DR.clean_text(bad).encode("utf-8")              # must not raise

    assert DR.first_pages(b"not a pdf at all") == ""
    assert DR.first_pages(b"%PDF-1.4 garbage") == ""
    monkeypatch = None


# ============================================= the register check (validate_demergers)

def test_register_check_finds_misses_and_false_positives():
    import validate_demergers as VD
    gt = [{"date": "2026-05-01", "symbol": "VEDL", "company": "Vedanta", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""},
          {"date": "2026-05-01", "symbol": "VEDL", "company": "Vedanta", "purpose": "Demerger", "source": "api", "in_universe": "yes", "detail": ""},
          {"date": "2026-07-22", "symbol": "TRIVENI", "company": "Triveni", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""},
          {"date": "2026-06-10", "symbol": "OUTSIDE", "company": "X", "purpose": "Demerger", "source": "bc", "in_universe": "", "detail": ""},
          {"date": "2026-05-20", "symbol": "TSPL", "company": "", "purpose": "first appearance in the price file", "source": "newlist", "in_universe": "", "detail": ""},
          {"date": "2026-04-01", "symbol": "ANYCO", "company": "", "purpose": "Dividend", "source": "bc", "in_universe": "yes", "detail": ""}]
    sits = [{"symbol": "VEDL", "company": "Vedanta", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "listed",
             "listed_on": "2026-05-01", "facts": {"resulting_company": "Talwandi Sabo Power Limited"},
             "judge": {"what_is_spun": "power business into TSPL"}},
            {"symbol": "TRIVENI", "company": "Triveni", "kind": "merger", "confidence": ("other", ""), "stage": "announced",
             "listed_on": None, "facts": {}, "judge": {}},
            {"symbol": "DABUR", "company": "Dabur", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "exchange_noc",
             "listed_on": None, "facts": {}, "judge": {"what_is_spun": "Nothing is separated; amalgamation of Sesa into Dabur"}},
            {"symbol": "GHOST", "company": "Ghost", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "listed",
             "listed_on": "2026-03-01", "facts": {}, "judge": {"what_is_spun": "a unit"}},
            {"symbol": "UPL", "company": "UPL", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "exchange_noc",
             "listed_on": None, "facts": {}, "judge": {"what_is_spun": "crop protection into UPL 2"}}]
    res = VD.check(sits, gt, dt.date(2026, 10, 12))
    assert set(res["register"]) == {"VEDL", "TRIVENI"}                      # universe demergers only
    byv = {r["symbol"]: r["verdict"] for r in res["recall"]}
    assert byv["VEDL"] == "captured" and byv["TRIVENI"] == "held as other restructuring only"
    assert [r["symbol"] for r in res["misses"]] == ["TRIVENI"]
    assert "TSPL" in next(r for r in res["recall"] if r["symbol"] == "VEDL")["new_symbols_near_record_date"]
    byp = {r["symbol"]: r["verdict"] for r in res["precision"]}
    assert byp["VEDL"].startswith("verified") and byp["UPL"].startswith("pending")
    assert byp["DABUR"].startswith("FALSE POSITIVE (judge") and byp["GHOST"].startswith("FALSE POSITIVE (record date")
    s = res["summary"]
    assert (s["register_demergers"], s["captured"], s["missed"], s["false_positives"], s["pending"]) == (2, 1, 1, 2, 1)
    md = VD.render(res, "2026-10-12")
    assert "| …MISSED | 1 |" in md and "**TRIVENI**" in md and "FALSE POSITIVE" in md
