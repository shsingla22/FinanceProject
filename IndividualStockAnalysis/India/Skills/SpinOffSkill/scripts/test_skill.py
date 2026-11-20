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
    monkeypatch.setattr(SO, "_EQUITY", ({}, {}))


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


def test_probable_table_puts_demergers_first_and_links_its_sources():
    def sit(sym, kind, conf, score, heads):
        return {"symbol": sym, "kind": kind, "confidence": (conf, "why"), "verdict": {"score": score},
                "family": AZ.SO.family_of(kind), "stage": "announced", "listing": {"short": "NOT YET"}, "headlines": heads}
    heads = [{"date": "2026-01-10", "category": "Outcome of Board Meeting", "kind": "demerger",
              "headline": "x", "attachment": "https://nsearchives.nseindia.com/a.pdf"},
             {"date": "2026-03-01", "category": "Updates", "kind": "demerger", "headline": "y",
              "attachment": "https://nsearchives.nseindia.com/b.pdf"},
             {"date": "2026-04-30", "category": "Earnings call Apr 2026", "kind": "demerger", "headline": "q",
              "attachment": "https://www.bseindia.com/t.pdf"},
             {"date": "2026-02-02", "category": "Record Date (corporate-actions register)", "kind": "demerger",
              "headline": "r", "attachment": ""},
             {"date": "2026-02-03", "category": "Updates", "kind": "merger", "headline": "m",
              "attachment": "https://nsearchives.nseindia.com/b.pdf"}]          # same url, not repeated
    links = AZ.source_links(sit("A", "demerger", "probable", 5, heads))
    assert links.startswith("[2026-04 call transcript](https://www.bseindia.com/t.pdf)")
    assert "[2026-03-01 Updates](https://nsearchives.nseindia.com/b.pdf)" in links
    assert "[2026-02-02 NSE register](https://www.nseindia.com/get-quotes/equity?symbol=A)" in links
    assert links.count("](") == 4 and "more" not in links
    assert AZ.source_links(sit("B", "demerger", "probable", 5, [])) == "—"
    rows = [sit("S", "scheme_other", "probable", 9, []), sit("I", "demerger", "indicated", 9, []),
            sit("L", "subsidiary_listing", "probable", 8, []), sit("D1", "demerger", "probable", 4, []),
            sit("D2", "demerger", "probable", 7, [])]
    assert [r["symbol"] for r in sorted(rows, key=AZ.probable_order)] == ["D2", "D1", "I", "L", "S"]


def test_as_of_never_hears_later_calls_or_later_record_dates(tmp_path, monkeypatch):
    text = ("Call: Jan 2025\nwe are evaluating a demerger of the hotels business\n"
            "Call: Jun 2025\nthe demerger is now complete\n")
    as_of = dt.date(2025, 3, 31)
    assert [m["call"] for m in SO.concall_mentions(text, as_of)] == ["Jan 2025"]
    monkeypatch.setattr(SO, "concall_text", lambda sym: text)
    monkeypatch.setattr(FN, "doc_links", lambda sym: {"calls": {}})
    assert "Jun 2025" not in AZ.calls_text_for("X", 12, as_of) and "Jan 2025" in AZ.calls_text_for("X", 12, as_of)
    gt = tmp_path / "gt.csv"
    gt.write_text("date,symbol,company,purpose,source,detail,isin,register_symbol,in_universe\n"
                  "2025-01-10,A,A Ltd,Demerger,bc,,,A,yes\n2025-06-10,A,A Ltd,Demerger,api,,,A,yes\n"
                  "2025-02-01,B,B Ltd,Demerger,bc,,,B,yes\n")
    reg = SO.set_register(gt, as_of)
    assert reg == {"A": ["2025-01-10"], "B": ["2025-02-01"]}
    # the validator windows the register the same way
    import validate_demergers as VD
    rows = VD.load_ground_truth(gt)
    assert set(VD.register_demergers(rows, ("2024-04-01", "2025-03-31"))) == {"A", "B"}
    assert VD.register_demergers(rows, ("2025-05-01", "2025-12-31"))["A"]["dates"] == {"2025-06-10"}


def test_judge_cache_keeps_several_readings_per_key(tmp_path, monkeypatch):
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    calls = []
    def runner(p):
        calls.append(p)
        return json.dumps({"what_is_spun": f"reading {len(calls)}"})
    assert AZ._ask("K", "stamp-today", "p", True, runner=runner)["what_is_spun"] == "reading 1"
    assert AZ._ask("K", "stamp-backtest", "p", True, runner=runner)["what_is_spun"] == "reading 2"
    # both stay cached: switching between them asks nothing more
    assert AZ._ask("K", "stamp-today", "p", True, runner=runner)["status"] == "cached"
    assert AZ._ask("K", "stamp-backtest", "p", True, runner=runner)["status"] == "cached"
    assert len(calls) == 2
    # a legacy single-stamp entry is still read
    (tmp_path / "cache.json").write_text(json.dumps({"L": {"stamp": "s1", "verdict": {"what_is_spun": "old"}}}))
    assert AZ._ask("L", "s1", "p", True, runner=runner)["what_is_spun"] == "old" and len(calls) == 2


def test_extra_members_join_the_universe_and_its_isins(tmp_path, monkeypatch):
    import demerger_ground_truth as GT
    extra = tmp_path / "_extra_members.csv"
    extra.write_text("symbol,company,isin,why\nRAYMOND,Raymond Ltd.,INE301A01014,parent of a member\n")
    monkeypatch.setattr(FA, "EXTRA_MEMBERS", extra)
    m = FA.universe()
    assert m["RAYMOND"] == "Raymond Ltd." and len(m) >= 750
    assert GT.universe_isins()["INE301A01014"] == "RAYMOND"
    monkeypatch.setattr(FA, "EXTRA_MEMBERS", tmp_path / "missing.csv")
    assert "RAYMOND" not in FA.universe()


def test_corporate_actions_file_with_a_ragged_row_still_parses(tmp_path):
    import zipfile
    import demerger_ground_truth as GT
    z = tmp_path / "PR020424.zip"
    bc = ("SERIES,SYMBOL,SECURITY,RECORD_DT,BC_STRT_DT,BC_END_DT,EX_DT,ND_STRT_DT,ND_END_DT,PURPOSE\n"
          "EQ,RAYMOND,Raymond Ltd,11-JUL-2024,,,11-JUL-2024,,,DEMERGER\n"
          "EQ,ODDCO,\"Odd, Co Ltd\",,,,12-APR-2024,,,DEMERGER,extra,fields\n"      # ragged: overflow columns
          "EQ,XYZ,XYZ Ltd,15-APR-2024,,,15-APR-2024,,,DIVIDEND\n")
    with zipfile.ZipFile(z, "w") as zz:
        zz.writestr("bc02042024.csv", bc)
    rows = GT.parse_bc(z)
    assert [(r["symbol"], r["date"]) for r in rows] == [("RAYMOND", "2024-07-11"), ("ODDCO", "2024-04-12")]


def test_register_rows_are_put_under_the_universe_symbol_by_isin_or_twin():
    import demerger_ground_truth as GT
    members = {"TMPV": "Tata Motors Passenger Vehicles Ltd.", "HEGAM": "HEG Advanced Materials Ltd.", "VEDL": "Vedanta Ltd."}
    isins = {"INE155A01022": "TMPV", "INE545A01016": "HEGAM"}
    rows = [{"date": "2025-10-14", "symbol": "TATAMOTORS", "company": "Tata Motors Limited", "purpose": "DEMERGER", "source": "bc", "detail": ""},
            {"date": "2025-10-14", "symbol": "TMPV", "company": "Tata Motors Passenger Vehicles Limited", "purpose": "Demerger",
             "source": "api", "detail": "", "isin": "INE155A01022"},
            {"date": "2026-09-07", "symbol": "HEG", "company": "HEG Ltd", "purpose": "DEMERGER", "source": "bc", "detail": ""},
            {"date": "2026-09-07", "symbol": "HEG", "company": "HEG Limited", "purpose": "Demerger", "source": "api", "detail": "", "isin": "INE545A01016"},
            {"date": "2026-09-07", "symbol": "DALMIASUG", "company": "Dalmia Bharat Sugar", "purpose": "DEMERGER", "source": "bc", "detail": ""}]
    out = {(r["source"], r["register_symbol"]): r for r in GT.canonicalise(rows, members, isins)}
    assert out[("api", "HEG")]["symbol"] == "HEGAM" and out[("api", "HEG")]["in_universe"] == "yes"      # by ISIN
    assert out[("bc", "TATAMOTORS")]["symbol"] == "TMPV" and out[("bc", "TATAMOTORS")]["in_universe"] == "yes"   # by its API twin
    assert out[("bc", "HEG")]["symbol"] == "HEGAM"
    assert out[("bc", "DALMIASUG")]["symbol"] == "DALMIASUG" and out[("bc", "DALMIASUG")]["in_universe"] == ""   # same date, other company


def test_restructuring_rows_follow_the_deep_store_after_a_rule_change():
    store = {"a1": {"read_status": "read", "tags": ""},                 # read, nothing left after the rule change
             "a2": {"read_status": "read", "tags": "merger|rights_issue"},
             "a3": {"read_status": "", "tags": ""}}                     # not read: headline tag stands
    rows = [{"source": "NSE", "ann_id": "a1", "kind": "demerger", "tags": "demerger|merger"},
            {"source": "NSE", "ann_id": "a2", "kind": "demerger", "tags": "demerger"},
            {"source": "NSE", "ann_id": "a3", "kind": "demerger", "tags": "demerger"},
            {"source": "NSE-BM", "ann_id": "a1", "kind": "demerger", "tags": "demerger"},   # other source: untouched
            {"source": "CALLS", "ann_id": "c1", "kind": "demerger", "tags": "demerger"}]
    out, retagged, dropped = FA.reconcile_with_store(rows, store)
    assert dropped == 1 and retagged == 1
    assert [(r["source"], r["ann_id"], r["kind"]) for r in out] == [
        ("NSE", "a2", "merger"), ("NSE", "a3", "demerger"), ("NSE-BM", "a1", "demerger"), ("CALLS", "c1", "demerger")]
    assert out[0]["tags"] == "merger|rights_issue"


def test_esop_boilerplate_does_not_make_a_demerger():
    esop = ("RESOLVED FURTHER THAT in case of any corporate action(s) such as rights issue, bonus issue, "
            "merger/demerger, spin-off, consolidation, amalgamation, the outstanding options granted under the "
            "ESOP Plan 2024 shall be suitably adjusted. RESOLVED FURTHER THAT the Board be authorised.")
    stripped = FA.strip_boilerplate(esop)
    assert len(stripped) == len(esop) and "demerger" not in stripped and "authorised" in stripped
    assert DR.classify_text(esop) == []
    assert SO.evidence_in(esop, "demerger") == []
    real = esop + " The Board approved the demerger of the Sugar Business into Piccadily Sugar Limited, the Resulting Company."
    assert DR.classify_text(real) == ["demerger"]
    ev = SO.evidence_in(real, "demerger")
    assert ev[0]["keyword"] == "demerger" and "Sugar Business" in ev[0]["sentence"]
    row = {"kind": "scheme_other"}
    assert SO.refine_kind(row, esop * 3) == "scheme_other"


def test_evidence_quotes_the_keyword_line_and_sentence(tmp_path, monkeypatch):
    text = ("Sub: Outcome of Board Meeting\n\nThe Board at its meeting held today approved the Scheme of Arrangement. "
            "It provides for the demerger of the Sugar Business into Piccadily Sugar Limited (the Resulting Company).\n"
            "Other matters were also considered.\n")
    ev = SO.evidence_in(text, "demerger", 2)
    assert ev[0]["keyword"] == "demerger" and ev[0]["line"] == 3 and "Sugar Business" in ev[0]["sentence"]
    assert ev[1]["keyword"].lower().startswith("resulting compan")
    assert SO.evidence_in(text, "subsidiary_listing") == [] and SO.evidence_in("", "demerger") == []
    assert SO.evidence_in("DRHP filed for the IPO of the subsidiary", "subsidiary_listing")[0]["keyword"] == "DRHP"
    # the cell: link · keyword · stored text file with line · sentence, from the filings index
    monkeypatch.setattr(SO, "ANN_DIR", tmp_path)
    (tmp_path / "text").mkdir()
    (tmp_path / "text" / "P_a1.txt").write_text(text)
    row = {"symbol": "P", "date": "2026-03-02", "headline": "Outcome of Board Meeting", "ann_id": "a1",
           "text_file": "text/P_a1.txt", "attachment": "https://nsearchives.nseindia.com/p.pdf"}
    idx = AZ.rows_index([row])
    s = {"symbol": "P", "kind": "demerger", "headlines": [
        {"date": "2026-03-02", "category": "Outcome of Board Meeting", "kind": "demerger", "headline": "Outcome of Board Meeting",
         "attachment": "https://nsearchives.nseindia.com/p.pdf"},                       # no ann_id: a saved run
        {"date": "2026-04-30", "category": "Earnings call Apr 2026", "kind": "demerger",
         "headline": "we expect the demerger to complete next year", "attachment": "https://www.bseindia.com/t.pdf"},
        {"date": "2026-01-05", "category": "Updates", "kind": "demerger", "headline": "Intimation of demerger update",
         "attachment": "https://nsearchives.nseindia.com/u.pdf"}]}                       # no text on file → headline
    cell = AZ.sources_and_evidence(s, idx)
    parts = cell.split("<br>")
    assert parts[0].startswith("[2026-04 call transcript](https://www.bseindia.com/t.pdf) · **demerger** · P.pdf · “we expect")
    assert "[2026-03-02 Outcome of Board Meeting](https://nsearchives.nseindia.com/p.pdf) · **demerger** · [text line 3](" in parts[1]
    assert "text/P_a1.txt#L3" in parts[1] and "Sugar Business" in parts[1]
    assert parts[2].startswith("[2026-01-05 Updates](https://nsearchives.nseindia.com/u.pdf) · **demerger** · headline ·")
    assert AZ.sources_and_evidence({"symbol": "Q", "kind": "demerger", "headlines": []}, idx) == "—"


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


def test_backtest_runs_list_only_as_of_a_date_into_its_own_folder(tmp_path, monkeypatch):
    import backtest as BT
    rows = _rows()
    texts = {"3": SCHEME}
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    monkeypatch.setattr(SO, "load_filings", lambda path=None: rows)
    monkeypatch.setattr(SO, "load_text", lambda r: texts.get(r["ann_id"], ""))
    monkeypatch.setattr(SO, "concall_text", lambda sym: CALLS if sym == "ALPHA" else "")
    monkeypatch.setattr(FA, "universe", lambda: {"ALPHA": "Alpha Industries Ltd.", "BETA": "Beta"})
    monkeypatch.setattr(AZ, "_ai_available", lambda: False)
    for name in ("OUT_DIR", "REPORT", "LATEST", "SITUATIONS", "MENTIONS", "HISTORY", "COVERAGE", "OFFERINGS"):
        monkeypatch.setattr(AZ, name, tmp_path / "prod" / name)        # the production paths must stay untouched
    monkeypatch.setattr(FN, "PNL", tmp_path / "pnl")
    monkeypatch.setattr(FN, "CASH", tmp_path / "cash")
    monkeypatch.setattr(FN, "PPT_DIR", tmp_path / "ppt")
    monkeypatch.setattr(FN, "AR_DIR", tmp_path / "ar")
    monkeypatch.setattr(FN, "LINKS", tmp_path / "ppt" / "_concall_links.csv")
    monkeypatch.setattr(FN, "CONCALLS", tmp_path / "cc")
    gt = tmp_path / "gt.csv"
    gt.write_text("date,symbol,company,purpose,source,detail,isin,register_symbol,in_universe\n"
                  "2026-09-15,ALPHA,Alpha Industries Ltd.,Demerger,bc,,,ALPHA,yes\n"
                  "2026-11-20,ZETA,Zeta Ltd,Demerger,bc,,,ZETA,yes\n")                  # after the as-of date: unseen
    monkeypatch.setattr(BT, "GT", gt)
    monkeypatch.setattr(BT, "BACKTESTS", tmp_path / "bt")
    r = BT.run_backtest(dt.date(2026, 1, 1), TODAY, "TEST", workers=2, quick=True)
    folder = tmp_path / "bt" / "TEST"
    assert r["folder"] == str(folder)
    assert (folder / "SPINOFF_REPORT.md").exists() and (folder / "spinoff_latest.json").exists()
    assert (folder / "SPINOFF_GROUND_TRUTH_CHECK.md").exists() and (folder / "BACKTEST_SUMMARY.md").exists()
    assert not (tmp_path / "prod").exists()
    sits = r["record"]["situations"]
    assert sits[0]["symbol"] == "ALPHA" and "parent_financials" not in sits[0]   # list-only: no numbers
    md = (folder / "SPINOFF_REPORT.md").read_text()
    assert "## Confirmed demergers" in md and "### The parent, last three fiscal years" not in md
    s = r["check"]["summary"]
    assert s["register_demergers"] == 1 and s["captured"] == 1 and s["false_positives"] == 0   # ZETA is after the as-of date
    summ = (folder / "BACKTEST_SUMMARY.md").read_text()
    assert "# Backtest TEST" in summ and "| **ALPHA** |" in summ and "- none" in summ


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
    assert kind == "other" and ("slump sale" in why or "answered no" in why)
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


def test_company_name_must_end_where_the_name_ends():
    assert SO.demerger_direction("demerger of NISP from NMDC Limited into NMDC Steel Limited", "NMDC Ltd.")[0] == ""
    assert SO.demerger_direction("Amalgamation of UPL SAS with and into UPL 1 (“Merger 1”); Demerger of the Demerged Undertaking", "UPL Ltd.")[0] == ""
    assert SO.demerger_direction("to demerge its Driver Information business into Pricol Electronics Limited", "Pricol Ltd.")[0] == ""
    assert SO.demerger_direction("NMDC Limited (Demerged Company) and NMDC Steel Limited (Resulting Company)", "NMDC Ltd.")[0] == "outbound"
    # equality, not containment, when the judge names the receiving company
    assert not SO._same_company("Siemens Energy India Limited", "Siemens Ltd.")
    assert not SO._same_company("Astral Chemie", "Astral Ltd.")
    assert SO._same_company("Gabriel India Limited", "Gabriel India Ltd.")
    j = {"status": "judged", "what_is_spun": "The Energy business of Siemens Limited, transferred to Siemens Energy India Limited under a Scheme",
         "parent_or_spin": "parent", "selling_pressure": "likely", "reason": "focus"}
    assert SO.judge_override({"kind": "demerger", "company": "Siemens Ltd.", "facts": {}, "headlines": []}, j)[0] is None


def test_the_spin_off_itself_is_recognised_from_the_scheme_or_the_judge(monkeypatch):
    monkeypatch.setattr(SO, "_EQUITY", ({"ABLBL": "2025-06-23", "TMCV": "2025-11-12", "BELRISE": "2025-05-28",
                                         "AARTIPHARM": "2023-01-30", "ABFRL": "2008-01-01", "TMPV": "1998-07-22"},
                                        {SO._norm_name("Aditya Birla Fashion and Retail Limited"): "ABFRL",
                                         SO._norm_name("Tata Motors Limited"): "TMPV"}))
    today = dt.date(2026, 11, 8)
    text = ("Scheme of Arrangement between Aditya Birla Fashion and Retail Limited ('Demerged Company') and "
            "Aditya Birla Lifestyle Brands Limited ('Resulting Company') for the demerger of the Madura business.")
    assert SO.demerged_company_in(text) == "Aditya Birla Fashion and Retail Limited"
    rows = [{"date": "2026-01-10", "symbol": "ABLBL", "company": "Aditya Birla Lifestyle Brands Limited", "source": "NSE",
             "category": "Updates", "kind": "demerger", "tags": "demerger", "headline": "Update on the Scheme",
             "attachment": "x.pdf", "ann_id": "a1", "file_size": "", "text_file": ""}]
    s = SO.build_situations(rows, {"a1": text}, today=today)[0]
    assert s["facts"]["direction"] == "inbound" and s["facts"]["demerged_company"] == "Aditya Birla Fashion and Retail Limited"
    # by the scheme text: the demerged company is listed, ABLBL listed 17 months ago → the spin-off, second year
    assert SO.spin_identity(s, {}, today)
    assert s["stage"] == "listed" and s["listed_on"] == "2025-06-23" and s["facts"]["parent_symbol"] == "ABFRL"
    assert s["confidence"][0] == "confirmed" and "second year" in s["confidence"][1]
    assert SO.judge_override(s, {"status": "judged", "what_is_spun": "Madura business into Aditya Birla Lifestyle Brands Limited",
                                 "parent_or_spin": "parent", "selling_pressure": "likely", "reason": "x"})[0] is None
    assert SO.listing_status(s, {}, today)["short"].startswith("THIS IS THE SPIN-OFF")
    assert SO.confidence(s)[0] == "confirmed"
    # by the judge: renamed resulting company (TML Commercial Vehicles → Tata Motors Limited), no text direction
    t = {"symbol": "TMCV", "company": "Tata Motors Limited", "kind": "demerger", "stage": "announced", "facts": {},
         "stage_dates": {}, "listed_on": None, "days_since_listing": None, "headlines": []}
    jt = {"status": "judged", "what_is_spun": "Tata Motors' commercial vehicle business, demerged into TML Commercial Vehicles Limited, now renamed",
          "parent_or_spin": "spin", "selling_pressure": "likely", "reason": "focus",
          "listing_timeline": "the Company's equity shares were listed on November 12, 2025"}
    assert SO.spin_identity(t, jt, today) and t["stage"] == "listed" and t["listed_on"] == "2025-11-12"
    assert t["confidence"][0] == "confirmed" and "first year" in t["confidence"][1]
    # a recent IPO receiving a private company by merger is NOT the spin-off
    b = {"symbol": "BELRISE", "company": "Belrise Industries Limited", "kind": "demerger", "stage": "exchange_noc",
         "facts": {"direction": "inbound", "demerged_company": "H-One India Private Limited"}, "stage_dates": {}, "headlines": []}
    assert not SO.spin_identity(b, {"status": "judged", "parent_or_spin": "parent", "listing_timeline": "not stated"}, today)
    # a resulting company listed more than three years ago is a mature parent now
    a = {"symbol": "AARTIPHARM", "company": "Aarti Pharmalabs Limited", "kind": "demerger", "stage": "announced",
         "facts": {"direction": "inbound", "demerged_company": "Aarti Industries Limited"}, "stage_dates": {}, "headlines": []}
    assert not SO.spin_identity(a, {}, today)
    # an old listed company named as resulting company stays an inbound demerger
    g = {"symbol": "TMPV", "company": "Tata Motors Passenger Vehicles Limited", "kind": "demerger", "stage": "listed",
         "facts": {"direction": "inbound", "demerged_company": "Aditya Birla Fashion and Retail Limited"}, "stage_dates": {}, "headlines": []}
    assert not SO.spin_identity(g, {}, today)


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

def test_sebi_listing_disclosure_aliases_and_renames_from_the_fy25_backtest():
    # SEBI's 'whether listing would be sought' line, as companies answer it
    assert SO.listing_sought_in("7. Whether listing would be sought for the resulting entity. No. The shares issued by JKTTL would not be listed")[0] == "no"
    assert SO.listing_sought_in("Whether listing would be sought for the resulting entity Not Applicable ANNEXURE A2")[0] == "no"
    assert SO.listing_sought_in("Whether listing would be sought for the resulting entity: Yes, on BSE and NSE")[0] == "yes"
    assert SO.listing_sought_in("Whether listing would be sought for the resulting entity The equity shares of the Resulting Company are already listed on BSE")[0] == "already"
    assert SO.listing_sought_in("nothing of the kind") == ("", "")
    # an alias inside the parenthesis, or 'being the', still names the role
    kitex = ("Scheme between Kitex Childrenswear Limited (“KCL” or “Demerged Company”) and Kitex Garments Limited "
             "(“KGL” or “Resulting Company”) for the demerger of the Textile Business into Kitex Garments Limited (being the Resulting Company).")
    assert SO.demerger_direction(kitex, "Kitex Garments Ltd.")[0] == "inbound"
    # a renamed company: the filings' name is an alias of today's
    awl = "Scheme between Adani Enterprises Limited (Demerged Company) and Adani Wilmar Limited (Resulting Company)."
    assert SO.demerger_direction(awl, "AWL Agri Business Ltd.")[0] == ""
    assert SO.demerger_direction(awl, ["AWL Agri Business Ltd.", "Adani Wilmar Limited"])[0] == "inbound"
    rows = [{"date": "2024-08-01", "symbol": "AWL", "company": "Adani Wilmar Limited", "source": "NSE", "category": "Demerger",
             "kind": "demerger", "tags": "demerger", "headline": "Demerger", "attachment": "", "ann_id": "w1", "file_size": "", "text_file": ""},
            {"date": "2024-10-29", "symbol": "AWL", "company": "AWL Agri Business Ltd.", "source": "NSE", "category": "Updates",
             "kind": "demerger", "tags": "demerger", "headline": "Update on the Scheme", "attachment": "", "ann_id": "w2", "file_size": "", "text_file": ""}]
    s = SO.build_situations(rows, {"w1": awl, "w2": "Whether listing would be sought for the resulting entity: No."}, today=dt.date(2025, 3, 31))[0]
    assert s["facts"]["direction"] == "inbound"
    assert s["facts"]["listing_sought"] == {"no": 1} and s["facts"]["no_listing_sought"]
    kind, why = SO.judge_override(s, {"status": "judged", "what_is_spun": "Food FMCG division", "parent_or_spin": "spin"})
    assert kind == "other" and "SEBI disclosure" in why
    # a 'yes' anywhere keeps the demerger: Raymond's May 2024 'No' was about another scheme
    s2 = SO.build_situations(rows, {"w1": "Whether listing would be sought for the resulting entity: Yes.",
                                    "w2": "Whether listing would be sought for the resulting entity: No."}, today=dt.date(2025, 3, 31))[0]
    assert s2["facts"]["listing_sought"] == {"yes": 1, "no": 1} and not s2["facts"].get("no_listing_sought")
    # the judge's own words: slump sale to a wholly-owned subsidiary, 'no spin-off', a dated past separation
    base = {"symbol": "X", "company": "X Ltd", "kind": "demerger", "stage": "announced", "facts": {}, "headlines": [], "first_filing": "2024-07-10"}
    j = {"status": "judged", "parent_or_spin": "parent", "selling_pressure": "unclear", "reason": "x", "listing_timeline": "not stated"}
    assert SO.judge_override(base, {**j, "what_is_spun": "new edge digital services business, hived off to wholly-owned subsidiary Novamesh Limited on slump-sale basis"})[0] == "other"
    assert SO.judge_override(base, {**j, "what_is_spun": "Three SEZ undertakings of DLF Assets, vested into DCCDL; no listed-shareholder spin-off"})[0] == "other"
    assert SO.judge_override(base, {**j, "what_is_spun": "Non-Airport business demerged into GMR Power (January 2022); these filings describe an inbound merger"})[0] == "other"
    assert SO.judge_override(base, {**j, "what_is_spun": "Hotels business demerged into ITC Hotels (January 2025), listed"})[0] is None
    # a news-verification headline that says 'demerge' is not a scheme on the record
    heads = [{"date": "2024-12-24", "category": "News Verification", "kind": "demerger", "headline": "clarification on news: Amber looking to demerge electronics", "attachment": ""}]
    assert not SO.scheme_named(heads)
    assert SO.confidence({"kind": "demerger", "stage": "announced", "facts": {}, "headlines": heads})[0] == "probable"
    # 'moving into listed Kitex Garments' names this company as the receiver
    jk = {**j, "what_is_spun": "Kitex Childrenswear's Textile Business Division moving into listed Kitex Garments"}
    assert SO.judge_override({**base, "company": "Kitex Garments Ltd."}, jk)[0] == "other"


def _listing_sit(sym="HDFCBANK", company="HDFC Bank Ltd."):
    return {"symbol": sym, "company": company, "kind": "subsidiary_listing", "stage": "announced", "facts": {},
            "confidence": ("probable", "a subsidiary's listing is in motion"), "family": "partial spin-off / listing",
            "first_filing": "2026-01-17", "latest_filing": "2026-01-17", "listed_on": None, "days_since_listing": None,
            "stage_dates": {}, "headlines": [], "n_filings": 2, "sources": ["NSE"]}


def test_subsidiary_listing_is_resolved_into_partial_spin_off_or_dropped(monkeypatch):
    today = dt.date(2026, 11, 16)
    monkeypatch.setattr(SO, "_EQUITY", ({"HDBFS": "2025-07-02", "OLDCO": "2021-03-01"},
                                        {SO._norm_name("HDB Financial Services Limited"): "HDBFS",
                                         SO._norm_name("Old Subsidiary Limited"): "OLDCO"}))
    ok = {"status": "judged"}
    # already listed: the date comes from NSE's equity list, not the judge
    s = _listing_sit()
    r = SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_already_listed", "subsidiary": "HDB Financial Services Limited",
                                          "relation": "subsidiary", "parent_stake_before": "94.3%", "parent_stake_after": "74.2%",
                                          "ipo_stage": "listed", "listing_date": "2025-06-30", "quote": "HDBFS launched its IPO"}, today)
    assert r == "partial" and s["confidence"][0] == "confirmed" and s["stage"] == "listed"
    assert s["listed_on"] == "2025-07-02" and s["facts"]["subsidiary_listing_source"] == "NSE equity list"
    assert s["facts"]["subsidiary_symbol"] == "HDBFS" and s["family"] == "partial spin-off (subsidiary IPO)"
    assert SO.verdict(s, [])["label"].startswith("PARTIAL SPIN-OFF, LISTED 1–2Y")
    st = SO.listing_status(s, {}, today)
    assert st["state"] == "listed" and "HDB Financial Services" in st["text"] and "74.2%" in st["text"]
    # announced: confirmed, IPO in motion, nothing listed
    s = _listing_sit("AMBER", "Amber Enterprises India Ltd.")
    r = SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_ipo_announced", "subsidiary": "IL JIN Electronics (India) Limited",
                                          "ipo_stage": "DRHP filed", "timeline": "DRHP dated 6 November 2026 filed with SEBI",
                                          "listing_date": "not stated", "quote": "IL JIN filed the DRHP"}, today)
    assert r == "partial" and s["confidence"][0] == "confirmed" and s["stage"] == "announced" and s["listed_on"] is None
    assert SO.verdict(s, [])["label"].startswith("PARTIAL SPIN-OFF, IPO IN MOTION")
    assert SO.listing_status(s, {}, today)["short"].startswith("IPO DRHP filed — IL JIN")
    # an offer-for-sale 'record date' in the filings is not a listing date for an IPO in motion
    s = {**_listing_sit("NLCINDIA", "NLC India Ltd."), "stage": "record_date", "listed_on": "2026-11-04", "days_since_listing": 12}
    SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_ipo_announced", "subsidiary": "NLC India Renewables Limited (NIRL)",
                                      "ipo_stage": "board approval", "quote": "q"}, today)
    assert s["stage"] == "announced" and s["listed_on"] is None and s["facts"]["subsidiary"] == "NLC India Renewables Limited"
    # listed per the filings when NSE's list does not carry the name (a foreign listing)
    s = _listing_sit("KPIL", "Kalpataru Projects International Ltd.")
    SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_already_listed", "subsidiary": "Linjemontage i Grastorp AB",
                                      "listing_date": "2026-09-28", "quote": "listed on Nasdaq Stockholm"}, today)
    assert s["listed_on"] == "2026-09-28" and s["facts"]["subsidiary_listing_source"] == "per the filings"
    # an as-of run must not know a later listing
    s = _listing_sit()
    SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_ipo_announced", "subsidiary": "HDB Financial Services Limited",
                                      "ipo_stage": "DRHP filed", "quote": "q"}, dt.date(2025, 3, 31))
    assert s["stage"] == "announced" and s["listed_on"] is None and s["confidence"][0] == "confirmed"
    # the noise: each leaves both lists with its reason
    for what, word in (("stake_sale_in_other_ipo", "another company's IPO"), ("sale_or_transfer", "sale"), ("merger", "merger"),
                       ("own_ipo", "own IPO"), ("no_event", "no subsidiary listing"), ("something_else", "no subsidiary listing")):
        s = _listing_sit("X", "X Ltd")
        assert SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": what, "subsidiary": "not stated", "quote": "the quote"}, today) == "not"
        assert s["confidence"][0] == "other" and word in s["confidence"][1] and s["family"].startswith("not a subsidiary listing")
    # 'yes' without a named subsidiary is not a yes
    s = _listing_sit("X", "X Ltd")
    assert SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_ipo_announced", "subsidiary": "not stated"}, today) == "not"
    # listed more than two years ago: past the notes' window, out of the list
    s = _listing_sit("X", "X Ltd")
    assert SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_already_listed", "subsidiary": "Old Subsidiary Limited"}, today) == "not"
    assert s["confidence"][0] == "other" and "two years" in s["confidence"][1]
    # bracketed abbreviations and former names do not break the name or the exchange lookup
    assert SO.clean_entity("Mahanadi Coalfields Limited (MCL)") == "Mahanadi Coalfields Limited"
    assert SO.clean_entity("IL JIN Electronics (India) Limited (formerly known as IL JIN Electronics (India) Private Limited)") == "IL JIN Electronics (India) Limited"
    assert SO.clean_entity("Linjemontage i Grästorp AB (publ)") == "Linjemontage i Grästorp AB"
    s = _listing_sit()
    SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_already_listed", "subsidiary": "HDB Financial Services Limited (HDBFS)",
                                      "ipo_stage": "listed", "other_subsidiaries": ["Second Sub Limited (SSL)", "not stated"], "quote": "q"}, today)
    assert s["facts"]["subsidiary"] == "HDB Financial Services Limited" and s["listed_on"] == "2025-07-02"
    assert s["facts"]["other_subsidiaries"] == ["Second Sub Limited"]
    # 'already listed' with the offer still open and no date anywhere is an IPO in motion
    s = _listing_sit("SBIN", "State Bank of India")
    SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_already_listed", "subsidiary": "SBI Funds Management Limited",
                                      "ipo_stage": "offer open", "listing_date": "not stated", "quote": "q"}, today)
    assert s["confidence"][0] == "confirmed" and s["stage"] == "announced" and s["listed_on"] is None
    # an already-listed company that was acquired is not a partial spin-off
    s = _listing_sit("BAJAJ-AUTO", "Bajaj Auto Ltd.")
    assert SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "listed_entity_acquired_or_long_listed",
                                             "subsidiary": "Bajaj Mobility AG", "quote": "q"}, today) == "not"
    assert "acquired already listed" in s["confidence"][1]
    # withdrawn; and no judge answer leaves it probable
    s = _listing_sit("X", "X Ltd")
    assert SO.resolve_subsidiary_listing(s, {**ok, "what_it_is": "subsidiary_ipo_withdrawn", "subsidiary": "Sub Ltd", "quote": "DRHP withdrawn"}, today) == "withdrawn"
    assert s["confidence"][0] == "indicated" and s["stage"] == "withdrawn"
    s = _listing_sit("X", "X Ltd")
    assert SO.resolve_subsidiary_listing(s, {"status": "not assessed"}, today) == "unresolved" and s["confidence"][0] == "probable"


def test_report_puts_partial_spin_offs_below_the_demergers_and_drops_the_noise(tmp_path, monkeypatch):
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    monkeypatch.setattr(SO, "_EQUITY", ({"HDBFS": "2025-07-02"}, {SO._norm_name("HDB Financial Services Limited"): "HDBFS"}))
    today = dt.date(2026, 11, 16)
    docs = "HDFC Bank informs the Exchange that its subsidiary HDB Financial Services Limited has completed its IPO. " * 10
    asked = []
    def runner(prompt):
        asked.append(prompt)
        if "possible LISTING OF A SUBSIDIARY" in prompt:
            if "Bank of Noise" in prompt:
                return json.dumps({"what_it_is": "stake_sale_in_other_ipo", "subsidiary": "not stated", "quote": "sold NSE shares"})
            return json.dumps({"what_it_is": "subsidiary_already_listed", "subsidiary": "HDB Financial Services Limited",
                               "relation": "subsidiary", "parent_stake_after": "74.2%", "ipo_stage": "listed",
                               "listing_date": "2025-07-02", "quote": "HDBFS completed its IPO"})
        return json.dumps({"what_is_spun": "HDB Financial Services", "parent_or_spin": "parent", "selling_pressure": "unclear"})
    monkeypatch.setattr(AZ, "scheme_text_for", lambda s, rows, budget=AZ.FILINGS_CHARS: docs)
    monkeypatch.setattr(AZ, "calls_text_for", lambda sym, months, today, budget=AZ.CALLS_CHARS: "")
    good, noise = _listing_sit(), _listing_sit("NOISE", "Bank of Noise")
    for s in (good, noise):
        s.update({"checklist": [], "verdict": {"label": "x", "score": 3.0}, "reasons": [], "concall_mentions": []})
        AZ.enrich(s, [], True, today, {}, runner=runner, list_only=True)
    assert good["confidence"][0] == "confirmed" and good["facts"]["partial_spin"] and good["listed_on"] == "2025-07-02"
    assert noise["confidence"][0] == "other" and "another company's IPO" in noise["confidence"][1]
    assert sum("possible LISTING OF A SUBSIDIARY" in p for p in asked) == 2
    record = {"meta": {"run_date": "2026-11-16", "window_from": "2025-10-12", "window_to": "2026-11-15", "filings": 2,
                       "companies": 2, "universe": 750, "judge": "test"}, "situations": [good, noise], "call_only": []}
    md = AZ.render_report(record)
    assert "0 confirmed demergers, 1 partial spin-offs (subsidiary IPOs), 0 completed demergers, 0 probable" in md
    top = md.split("## Probable and indicated")[0]
    assert top.index("## Confirmed demergers") < top.index("### Partial spin-offs") < top.index("| **HDFCBANK** | HDB Financial Services Limited |")
    assert "2025-07-02 (NSE)" in top and "PARTIAL SPIN-OFF, LISTED 1–2Y" in top
    prob = md.split("## Probable and indicated")[1].split("<details>")[0]
    assert "HDFCBANK" not in prob and "NOISE" not in prob                 # neither is in the probable list
    assert "**NOISE**" not in top                                         # and the noise is not in the confirmed list
    assert "| NOISE | not a subsidiary listing (stake sale in other ipo) |" in md      # kept, with its reason, among the others
    assert "# Partial spin-offs (subsidiary IPOs) — in full" in md and "**The partial spin-off:** **HDB Financial Services Limited**" in md


def test_a_subsidiary_ipo_hidden_behind_a_demerger_situation_is_found(tmp_path, monkeypatch):
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    monkeypatch.setattr(SO, "_EQUITY", ({"HDBFS": "2025-07-02"}, {SO._norm_name("HDB Financial Services Limited"): "HDBFS"}))
    today = dt.date(2026, 11, 16)
    def runner(prompt):
        if "possible LISTING OF A SUBSIDIARY" in prompt:
            return json.dumps({"what_it_is": "subsidiary_already_listed", "subsidiary": "HDB Financial Services Limited",
                               "ipo_stage": "listed", "quote": "HDBFS completed its IPO"})
        return json.dumps({"what_is_spun": "the ice cream business", "parent_or_spin": "parent", "selling_pressure": "likely"})
    monkeypatch.setattr(AZ, "scheme_text_for", lambda s, rows, budget=AZ.FILINGS_CHARS: "filings " * 100)
    monkeypatch.setattr(AZ, "calls_text_for", lambda sym, months, today, budget=AZ.CALLS_CHARS: "")
    heads = [{"date": "2025-07-03", "category": "Updates", "kind": "subsidiary_listing", "headline": "IPO of subsidiary", "attachment": ""},
             {"date": "2025-10-18", "category": "Outcome of Board Meeting", "kind": "demerger", "headline": "financial results", "attachment": ""}]
    def base(conf_facts):
        return {**_listing_sit(), "kind": "demerger", "family": "spin-off", "headlines": heads, "checklist": [],
                "verdict": {"label": "x", "score": 3.0}, "reasons": [], "concall_mentions": [], **conf_facts}
    # a text-only (probable) demerger: the company becomes the partial spin-off it really is
    s = base({})
    monkeypatch.setattr(SO, "confidence", lambda sit: ("probable", "text-only"))
    AZ.enrich(s, [], True, today, {}, runner=runner, list_only=True)
    assert s["kind"] == "subsidiary_listing" and s["confidence"][0] == "confirmed" and s["listed_on"] == "2025-07-02"
    assert s["facts"]["previously_held_as"] == "demerger / probable" and "also_partial" not in s
    # a demerger the register records stays a demerger, and is ALSO shown as a partial spin-off
    s = base({"facts": {"record_date": "2025-12-05", "record_date_source": "NSE corporate-actions register"}})
    monkeypatch.setattr(SO, "confidence", lambda sit: ("confirmed", "a demerger scheme is on the exchange record"))
    AZ.enrich(s, [], True, today, {}, runner=runner, list_only=True)
    assert s["kind"] == "demerger" and s["confidence"][0] == "confirmed"
    assert s["also_partial"]["facts"]["subsidiary"] == "HDB Financial Services Limited" and s["also_partial"]["stage"] == "listed"
    record = {"meta": {"run_date": "2026-11-16", "window_from": "a", "window_to": "b", "filings": 1, "companies": 1,
                       "universe": 750, "judge": "t"}, "situations": [s], "call_only": []}
    md = AZ.render_report(record)
    assert "1 confirmed demergers, 1 partial spin-offs" in md and "*(the company also has a demerger on file)*" in md
    # no subsidiary-listing filing among the headlines: the question is not asked
    asked = []
    s = base({"headlines": heads[1:]})
    AZ.enrich(s, [], True, today, {}, runner=lambda p: asked.append(p) or runner(p), list_only=True)
    assert not any("possible LISTING OF A SUBSIDIARY" in p for p in asked) and s["kind"] == "demerger"


def _prob_sit(sym="REFEX", company="Refex Industries Ltd.", kind="demerger", conf="probable", stage="announced"):
    return {"symbol": sym, "company": company, "kind": kind, "stage": stage, "facts": {},
            "confidence": (conf, "a filing's text names a demerger"), "family": SO.family_of(kind),
            "first_filing": "2026-03-17", "latest_filing": "2026-10-28", "listed_on": None, "days_since_listing": None,
            "stage_dates": {}, "headlines": [], "n_filings": 3, "sources": ["NSE"]}


def test_probable_rows_are_resolved_in_progress_completed_indicated_or_discarded(monkeypatch):
    today = dt.date(2026, 11, 17)
    monkeypatch.setattr(SO, "_EQUITY", ({"NSLNISP": "2023-02-20", "SCILAL": "2024-03-19", "TRITURBINE": "2011-10-28"},
                                        {SO._norm_name("Shipping Corporation of India Land and Assets Limited"): "SCILAL"}))
    monkeypatch.setattr(SO, "_REGISTER", {"SANOFI": ["2024-06-13"]})
    ok = {"status": "judged"}
    # a real demerger in progress: confirmed, marked as read from the text, stage from the judge
    s = _prob_sit()
    r = SO.resolve_probable(s, {**ok, "what_it_is": "demerger_in_progress", "business": "Green Mobility Business Undertaking",
                                "resulting_company": "Refex Mobility Limited (RML)", "role": "demerged company", "stage": "NCLT sanction",
                                "timeline": "NCLT hearing on 28 October 2026", "quote": "NCLT hearings are underway under the proposed demerger scheme"}, today)
    assert r == "in_progress" and s["kind"] == "demerger" and s["confidence"][0] == "confirmed"
    assert s["facts"]["resolved_from_text"] and s["facts"]["resulting_company"] == "Refex Mobility Limited" and s["stage"] == "nclt_sanction"
    assert SO.verdict(s, [])["label"].startswith("PRE-SPIN")
    # a 'scheme, nature unclear' row found to be a demerger becomes one; the judge cannot push it to a record date
    s = _prob_sit("X", "X Ltd", kind="scheme_other")
    SO.resolve_probable(s, {**ok, "what_it_is": "demerger_in_progress", "business": "the cement business", "stage": "record date", "quote": "q"}, today)
    assert s["kind"] == "demerger" and s["family"] == "spin-off" and s["stage"] == "announced"
    # completed, this company the RESULTING company: its own NSE listing date
    s = _prob_sit("NSLNISP", "NMDC Steel Ltd.")
    r = SO.resolve_probable(s, {**ok, "what_it_is": "demerger_completed", "business": "Nagarnar iron and steel plant", "role": "resulting company",
                                "resulting_company": "NMDC Limited", "completed_date": "2022", "quote": "pre-demerger period"}, today)
    assert r == "completed" and s["confidence"][0] == "completed" and s["facts"]["completed_date"] == "2023-02-20"
    assert s["facts"]["completed_date_source"].startswith("NSE equity list (this company")
    assert SO.listing_status(s, {}, today)["state"] == "completed" and SO.verdict(s, [])["label"].startswith("COMPLETED DEMERGER")
    # completed, this company the DEMERGED company: the resulting company's NSE listing date
    s = _prob_sit("SCI", "Shipping Corporation of India Ltd.")
    SO.resolve_probable(s, {**ok, "what_it_is": "demerger_completed", "business": "non-core land assets", "role": "demerged company",
                            "resulting_company": "Shipping Corporation of India Land and Assets Limited", "completed_date": "FY 2023-24", "quote": "q"}, today)
    assert s["facts"]["completed_date"] == "2024-03-19" and "SCILAL listed" in s["facts"]["completed_date_source"]
    # completed long ago: the exchange date is not forced onto a different year; the filings' date stands
    s = _prob_sit("TRITURBINE", "Triveni Turbine Ltd.")
    SO.resolve_probable(s, {**ok, "what_it_is": "demerger_completed", "business": "steam turbine business", "role": "resulting company",
                            "resulting_company": "Triveni Engineering and Industries Limited", "completed_date": "2010", "quote": "demerged in 2010"}, today)
    assert s["facts"]["completed_date"] == "2011-10-28"                     # within a year of what the filing says: the listing date
    s = _prob_sit("EMBDL", "Embassy Developments Ltd.")
    SO.resolve_probable(s, {**ok, "what_it_is": "demerger_completed", "business": "power business", "role": "demerged company",
                            "resulting_company": "not stated", "completed_date": "FY 2010-11", "quote": "q"}, today)
    assert s["facts"]["completed_date"] == "FY 2010-11" and s["facts"]["completed_date_source"] == "per the filings"
    # the register's record date outranks every other date
    s = _prob_sit("SANOFI", "Sanofi India Ltd.")
    SO.resolve_probable(s, {**ok, "what_it_is": "demerger_completed", "business": "consumer healthcare", "completed_date": "2024", "quote": "q"}, today)
    assert s["facts"]["completed_date"] == "2024-06-13" and s["facts"]["completed_date_source"].startswith("NSE register")
    # management's own indication stays indicated; a withdrawal is recorded
    s = _prob_sit("ZEEL", "Zee", conf="indicated", stage="indicated_on_calls")
    assert SO.resolve_probable(s, {**ok, "what_it_is": "management_indication", "business": "music business", "quote": "we are evaluating a demerger"}, today) == "indicated"
    assert s["confidence"][0] == "indicated" and "management itself" in s["confidence"][1] and s["stage"] == "indicated_on_calls"
    s = _prob_sit()
    assert SO.resolve_probable(s, {**ok, "what_it_is": "withdrawn", "business": "x", "quote": "scheme withdrawn"}, today) == "withdrawn" and s["stage"] == "withdrawn"
    # everything else is discarded, with its reason
    for what, word in (("other_companys_demerger", "another company's"), ("internal_reorganisation", "internal reorganisation"),
                       ("merger_or_acquisition", "merger"), ("no_event", "no demerger event"), ("news_report_only", "press speculation"),
                       ("gibberish", "no demerger event")):
        s = _prob_sit("X", "X Ltd")
        assert SO.resolve_probable(s, {**ok, "what_it_is": what, "business": "not stated", "quote": "the quote"}, today) == "discarded"
        assert s["confidence"][0] == "other" and word in s["confidence"][1] and s["family"].startswith("discarded on reading")
    # 'in progress' without a named business is not accepted; no judge answer leaves the row alone
    s = _prob_sit("X", "X Ltd")
    assert SO.resolve_probable(s, {**ok, "what_it_is": "demerger_in_progress", "business": "not stated"}, today) == "discarded"
    s = _prob_sit("X", "X Ltd")
    assert SO.resolve_probable(s, {"status": "not assessed"}, today) == "unresolved" and s["confidence"][0] == "probable"
    assert SO.resolve_probable({**_prob_sit(), "kind": "merger"}, {**ok, "what_it_is": "no_event"}, today) == "unresolved"


def test_report_places_resolved_demergers_completed_list_and_drops_the_rest(tmp_path, monkeypatch):
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    monkeypatch.setattr(SO, "_EQUITY", ({"NSLNISP": "2023-02-20"}, {}))
    today = dt.date(2026, 11, 17)
    answers = {"Refex": {"what_it_is": "demerger_in_progress", "business": "Green Mobility Business Undertaking",
                         "resulting_company": "Refex Mobility Limited", "stage": "NCLT sanction", "quote": "proposed demerger scheme"},
               "NMDC Steel": {"what_it_is": "demerger_completed", "business": "Nagarnar steel plant", "role": "resulting company",
                              "resulting_company": "NMDC Limited", "completed_date": "2022", "quote": "pre-demerger period"},
               "Tata Tech": {"what_it_is": "other_companys_demerger", "business": "not stated", "quote": "Tata Motors, the Holding Company"},
               "Zee": {"what_it_is": "management_indication", "business": "music business", "quote": "we are evaluating a demerger"}}
    asked = []
    def runner(prompt):
        if "no filing settles what it is" in prompt:
            asked.append(prompt)
            return json.dumps(next(v for k, v in answers.items() if f"of {k}" in prompt))
        return json.dumps({"what_is_spun": "a business", "parent_or_spin": "parent", "selling_pressure": "unclear"})
    monkeypatch.setattr(AZ, "scheme_text_for", lambda s, rows, budget=AZ.FILINGS_CHARS: "filings " * 100)
    monkeypatch.setattr(AZ, "calls_text_for", lambda sym, months, today, budget=AZ.CALLS_CHARS: "")
    monkeypatch.setattr(SO, "confidence", lambda sit: sit["confidence"])
    extra = {"checklist": [], "verdict": {"label": "x", "score": 3.0}, "reasons": [], "concall_mentions": []}
    scheme = {**_prob_sit("ALPHA", "Alpha Ltd.", conf="confirmed"), **extra, "facts": {"resulting_company": "Alpha Energy Limited"}}
    refex = {**_prob_sit(), **extra}
    nsl = {**_prob_sit("NSLNISP", "NMDC Steel Ltd."), **extra}
    tata = {**_prob_sit("TATATECH", "Tata Tech Ltd."), **extra}
    zee = {**_prob_sit("ZEEL", "Zee Ltd.", conf="indicated", stage="indicated_on_calls"), **extra}
    gone = {**_prob_sit("PRESTIGE", "Prestige Ltd.", conf="indicated", stage="withdrawn"), **extra}
    sits = [refex, scheme, nsl, tata, zee, gone]                    # refex first: the report must still list it last
    for s in sits:
        AZ.enrich(s, [], True, today, {}, runner=runner, list_only=True)
    assert len(asked) == 4                                           # not the confirmed one, not the withdrawn one
    assert (refex["confidence"][0], nsl["confidence"][0], tata["confidence"][0], zee["confidence"][0]) == ("confirmed", "completed", "other", "indicated")
    record = {"meta": {"run_date": "2026-11-17", "window_from": "a", "window_to": "b", "filings": 6, "companies": 6,
                       "universe": 750, "judge": "t"}, "situations": sits, "call_only": []}
    md = AZ.render_report(record)
    assert "2 confirmed demergers, 0 partial spin-offs (subsidiary IPOs), 1 completed demergers, 0 probable, 2 indicated" in md
    top = md.split("## Probable and indicated")[0]
    assert top.index("| **ALPHA** |") < top.index("| **REFEX** † |")            # read-from-text demergers go last
    assert "† *A demerger in progress, confirmed by reading the complete filings" in top
    assert top.index("### Partial spin-offs") < top.index("### Completed demergers") < top.index("| **NSLNISP** | resulting company |")
    assert "2023-02-20 | NSE equity list (this company's listing)" in top
    rest = md.split("## Probable and indicated")[1].split("<details>")[0]
    assert "**ZEEL**" in rest and "**PRESTIGE**" in rest and "TATATECH" not in rest and "REFEX" not in rest and "NSLNISP" not in rest
    assert "| TATATECH | discarded on reading (other companys demerger) |" in md
    # the register check counts a completed demerger as captured
    import validate_demergers as VD
    gt = [{"date": "2023-01-10", "symbol": "NSLNISP", "company": "NMDC Steel", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""}]
    res = VD.check(sits, gt, today, equities=[], days=2000)
    assert res["recall"][0]["verdict"] == "captured" and res["summary"]["false_positives"] == 0


def test_rules_from_the_long_backtests_unverified_list(monkeypatch):
    base = {"symbol": "X", "company": "X Ltd", "kind": "demerger", "stage": "announced", "facts": {}, "headlines": [],
            "first_filing": "2024-06-26", "confidence": ("confirmed", "")}
    j = {"status": "judged", "parent_or_spin": "parent", "selling_pressure": "unclear", "reason": "x", "listing_timeline": "not stated"}
    # Viyash: 'Not stated — documents describe an amalgamation … into Sequent', whatever it calls the company
    assert SO.judge_override(base, {**j, "what_is_spun": "Not stated — documents describe an amalgamation of Viyash Life Sciences and subsidiaries into Sequent"})[0] == "merger"
    # Adani Enterprises today: 'not stated; … no Food FMCG demerger'
    assert SO.judge_override(base, {**j, "what_is_spun": "not stated; filings show amalgamations under the Composite Scheme and a cash sale of the AWL stake, no Food FMCG demerger",
                                    "parent_or_spin": "unclear"})[0] == "other"
    # GMR: the judge answers the listing question with no; 'No listing date stated' is silence, not a no
    assert SO.judge_override(base, {**j, "what_is_spun": "GIL's non-airport business, demerged into GMR Power", "listing_timeline": "No new listing: GIL will continue as the listed entity"})[0] == "other"
    assert SO.judge_override(base, {**j, "what_is_spun": "Platform Business Undertaking demerged into Odigma", "listing_timeline": "No listing date stated. On November 14, 2026 the company said Rediff filed the UDRHP"})[0] is None
    # and the exchange's register outranks every reading: a company with a demerger record date is never demoted
    reg = {**base, "facts": {"record_date": "2024-09-11", "record_date_source": "NSE corporate-actions register", "direction": "inbound"}}
    assert SO.judge_override(reg, {**j, "what_is_spun": "Not stated — documents describe an amalgamation", "listing_timeline": "No new listing."})[0] is None
    # Cello today: into a NAMED wholly-owned subsidiary; Adani today: an amalgamation described as the 'spin'
    assert SO.judge_override(base, {**j, "what_is_spun": "Wim Plast's Manufacturing Business demerged into Cello Consumer Products Private Limited, a wholly owned subsidiary of Cello World",
                                    "listing_timeline": "not stated — no listing of the demerged entity is described"})[0] == "other"
    assert SO.judge_override(base, {**j, "what_is_spun": "Adani Tradecom Limited amalgamated into Adani New Industries Limited; documents give no business description"})[0] == "merger"
    assert SO.judge_override(base, {**j, "what_is_spun": "Hotels business, demerged into ITC Hotels", "reason": "after the amalgamation of a subsidiary into the parent, focus"})[0] is None
    # Tata Communications: to a wholly-owned subsidiary, nothing about listing; Natco: to a WOS that WILL list
    assert SO.judge_override(base, {**j, "what_is_spun": "new edge digital services business, hived off to wholly-owned subsidiary Novamesh Limited"})[0] == "other"
    natco = {**base, "facts": {"listing_sought": {"yes": 2}}}
    assert SO.judge_override(natco, {**j, "what_is_spun": "Crop Health Sciences division demerged into a wholly owned subsidiary"})[0] is None
    assert SO.judge_override(base, {**j, "what_is_spun": "Crop Health Sciences division demerged into a wholly owned subsidiary",
                                    "listing_timeline": "the equity shares of NCHSL shall be listed on BSE and NSE after the scheme"})[0] is None
    # SCI: the resulting company already listed before these filings, and nothing expected
    monkeypatch.setattr(SO, "_EQUITY", ({"SCILAL": "2024-03-01", "AWL": "2022-02-08"},
                                        {SO._norm_name("Shipping Corporation of India Land and Assets Limited"): "SCILAL",
                                         SO._norm_name("Adani Wilmar Limited"): "AWL"}))
    sci = {**base, "symbol": "SCI", "facts": {"resulting_company": "Shipping Corporation of India Land and Assets Limited"}}
    assert SO.judge_override(sci, {**j, "what_is_spun": "192 land assets transferred to a separate land-holding company"})[0] == "other"
    # …but Adani Enterprises' holders receiving listed Adani Wilmar shares, with a listing expected, is a spin-off
    ael = {**base, "symbol": "ADANIENT", "facts": {"resulting_company": "Adani Wilmar Limited"}}
    assert SO.judge_override(ael, {**j, "what_is_spun": "Food FMCG division demerged into Adani Wilmar",
                                   "listing_timeline": "the Resulting Company New Equity Shares shall be listed on BSE"})[0] is None
    # Astral: the judge read the withdrawal no headline carried
    conf, stage = SO.judge_adjust(base, {**j, "what_is_spun": "Chemicals undertaking into subsidiary Astral Chemie Limited; scheme later withdrawn"})
    assert conf[0] == "indicated" and stage == "withdrawn"
    assert SO.judge_adjust({**base, "stage": "listed"}, {**j, "what_is_spun": "x; scheme later withdrawn"}) == (None, None)


def test_a_filing_speaking_of_the_company_and_the_headline_name_settle_direction():
    cello = ("The Scheme provides for (a) the demerger, transfer and vesting of the Manufacturing Business of WPL into CCPPL "
             "and issue of equity shares by the Company to the shareholders of WPL in consideration thereof; and (b) the "
             "amalgamation of WPL with the Company. The equity shares issued by the Company as consideration for the demerger will be listed.")
    assert SO.demerger_direction(cello, "Cello World Ltd.")[0] == "inbound"
    out = ("The Scheme provides for the demerger of the Hotels Business of the Company into ITC Hotels Limited; the shareholders "
           "of the Company shall receive one share of ITC Hotels for every ten held.")
    assert SO.demerger_direction(out, "ITC Ltd.")[0] == "outbound"
    # the headline carries the name the company filed under; the store carries today's
    rows = [{"date": "2024-08-01", "symbol": "AWL", "company": "AWL Agri Business Ltd.", "source": "NSE", "category": "Demerger",
             "kind": "demerger", "tags": "demerger", "headline": "Adani Wilmar Limited has informed the Exchange about Demerger",
             "attachment": "", "ann_id": "w1", "file_size": "", "text_file": ""}]
    awl = "Scheme between Adani Enterprises Limited (Demerged Company) and Adani Wilmar Limited (Resulting Company)."
    s = SO.build_situations(rows, {"w1": awl}, today=dt.date(2025, 3, 31))[0]
    assert s["facts"]["direction"] == "inbound"


def test_register_record_date_overrides_the_filings_date_and_looks_a_little_ahead(monkeypatch):
    # ITC: the filings' words gave a June 2024 'record date' (the dividend's); the register says 2025-01-06
    row = {"date": "2024-06-01", "symbol": "ITC", "company": "ITC Ltd.", "source": "NSE", "category": "Demerger",
           "kind": "demerger", "tags": "demerger", "headline": "Scheme of Arrangement — demerger of the Hotels business",
           "attachment": "", "ann_id": "i1", "file_size": "", "text_file": ""}
    text = "The Board fixed Tuesday, 4 June 2024 as the record date. The demerger of the Hotels Business into ITC Hotels Limited."
    monkeypatch.setattr(SO, "_REGISTER", {"ITC": ["2025-01-06"]})
    s = SO.build_situations([row], {"i1": text}, today=dt.date(2025, 3, 31))[0]
    assert s["stage"] == "record_date" and s["listed_on"] == "2025-01-06" and s["facts"]["record_date"] == "2025-01-06"
    assert s["facts"]["record_date_source"].startswith("NSE")
    # an upcoming record date in the file: stage record_date, nothing listed yet
    monkeypatch.setattr(SO, "_REGISTER", {"ITC": ["2025-04-07"]})
    s = SO.build_situations([row], {"i1": text}, today=dt.date(2025, 3, 31))[0]
    assert s["stage"] == "record_date" and s["listed_on"] is None and s["facts"]["record_date"] == "2025-04-07"
    assert SO.listing_status(s, {}, dt.date(2025, 3, 31))["state"] == "pending_record_date_set"
    # set_register keeps the announced weeks ahead, not months
    import tempfile
    p = Path(tempfile.mkdtemp()) / "gt.csv"
    p.write_text("date,symbol,company,purpose,source,detail,isin,register_symbol,in_universe\n"
                 "2025-04-07,SIEMENS,Siemens,Demerger,bc,,,SIEMENS,yes\n2025-09-01,LATE,Late,Demerger,bc,,,LATE,yes\n")
    assert SO.set_register(p, dt.date(2025, 3, 31)) == {"SIEMENS": ["2025-04-07"]}


def test_completed_demergers_older_than_two_years_are_mature_and_still_verified(monkeypatch):
    row = {"date": "2026-10-01", "symbol": "SANOFI", "company": "Sanofi India Ltd.", "source": "NSE", "category": "Updates",
           "kind": "demerger", "tags": "demerger", "headline": "Update on the demerger", "attachment": "", "ann_id": "s1",
           "file_size": "", "text_file": ""}
    monkeypatch.setattr(SO, "_REGISTER", {"SANOFI": ["2024-06-13"]})
    s = SO.build_situations([row], {"s1": "the demerger of the consumer healthcare business"}, today=dt.date(2026, 11, 16))[0]
    assert s["facts"]["mature"] and s["listed_on"] == "2024-06-13" and s["stage"] == "record_date"
    assert SO.confidence(s)[0] == "other" and "two years" in SO.confidence(s)[1]
    # the check: a record date older than the recall window still verifies; a mature one is captured, not missed
    import validate_demergers as VD
    gt = [{"date": "2024-06-13", "symbol": "SANOFI", "company": "Sanofi", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""},
          {"date": "2026-05-01", "symbol": "VEDL", "company": "Vedanta", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""}]
    sits = [{"symbol": "ITC", "company": "ITC", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "record_date",
             "listed_on": "2025-01-06", "facts": {"record_date": "2025-01-06"}, "judge": {"what_is_spun": "hotels"}},
            {"symbol": "VEDL", "company": "Vedanta", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "record_date",
             "listed_on": "2026-05-01", "facts": {}, "judge": {"what_is_spun": "power"}},
            {**s, "confidence": ("other", "mature"), "judge": {"what_is_spun": "consumer healthcare"}}]
    gt.append({"date": "2025-01-06", "symbol": "ITC", "company": "ITC", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""})
    res = VD.check(sits, gt, dt.date(2026, 11, 16), equities=[], days=400)
    assert set(res["register"]) == {"VEDL"}                                   # recall window: 400 days
    byp = {r["symbol"]: r["verdict"] for r in res["precision"]}
    assert byp["ITC"] == "verified by the register" and byp["VEDL"] == "verified by the register"   # ITC: older than the window, still verified
    assert res["summary"]["false_positives"] == 0
    res2 = VD.check(sits, gt, dt.date(2026, 11, 16), equities=[], days=960)
    byv = {r["symbol"]: r["verdict"] for r in res2["recall"]}
    assert byv["SANOFI"].startswith("captured (mature") and byv["ITC"] == "captured" and byv["VEDL"] == "captured"
    assert res2["summary"]["missed"] == 0 and res2["summary"]["captured"] == 3


def test_register_check_verifies_later_record_dates_in_a_backtest():
    import validate_demergers as VD
    gt = [{"date": "2025-04-07", "symbol": "SIEMENS", "company": "Siemens", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""},
          {"date": "2025-12-05", "symbol": "HINDUNILVR", "company": "HUL", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""},
          {"date": "2025-01-06", "symbol": "ITC", "company": "ITC", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""}]
    sits = [{"symbol": "SIEMENS", "company": "Siemens", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "record_date",
             "listed_on": None, "facts": {"record_date": "2025-04-07"}, "judge": {"what_is_spun": "energy business"}},
            {"symbol": "HINDUNILVR", "company": "HUL", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "announced",
             "listed_on": None, "facts": {}, "judge": {"what_is_spun": "ice cream"}},
            {"symbol": "ITC", "company": "ITC", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "record_date",
             "listed_on": "2025-01-06", "facts": {}, "judge": {"what_is_spun": "hotels"}},
            {"symbol": "NEVER", "company": "Never", "kind": "demerger", "confidence": ("confirmed", ""), "stage": "announced",
             "listed_on": None, "facts": {}, "judge": {"what_is_spun": "a unit"}}]
    res = VD.check(sits, gt, dt.date(2025, 3, 31), equities=[], days=365)
    assert set(res["register"]) == {"ITC"}                                   # recall: the window only
    byp = {r["symbol"]: r["verdict"] for r in res["precision"]}
    assert byp["SIEMENS"] == "verified by the register"                     # announced ahead, in the file already
    assert byp["HINDUNILVR"] == "verified by a later record date (2025-12-05)"
    assert byp["ITC"] == "verified by the register" and byp["NEVER"].startswith("pending")
    s = res["summary"]
    assert (s["verified"], s["verified_later"], s["pending"], s["false_positives"]) == (3, 1, 1, 0)


def test_register_check_finds_misses_and_false_positives():
    import validate_demergers as VD
    gt = [{"date": "2026-05-01", "symbol": "VEDL", "company": "Vedanta", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""},
          {"date": "2026-05-01", "symbol": "VEDL", "company": "Vedanta", "purpose": "Demerger", "source": "api", "in_universe": "yes", "detail": ""},
          {"date": "2026-07-22", "symbol": "TRIVENI", "company": "Triveni", "purpose": "Demerger", "source": "bc", "in_universe": "yes", "detail": ""},
          {"date": "2026-06-10", "symbol": "OUTSIDE", "company": "X", "purpose": "Demerger", "source": "bc", "in_universe": "", "detail": ""},
          {"date": "2026-04-01", "symbol": "ANYCO", "company": "", "purpose": "Dividend", "source": "bc", "in_universe": "yes", "detail": ""}]
    # NSE's equity list stands in for the arrival check: the resulting company's own listing date
    equities = [{"symbol": "TSPL", "name": "Talwandi Sabo Power Limited", "listing_date": "2026-05-20"},
                {"symbol": "RANDOMIPO", "name": "Random Foods Limited", "listing_date": "2026-05-21"},
                {"symbol": "VEDLOLD", "name": "Vedanta Aluminium Limited", "listing_date": "2026-09-01"}]   # too late
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
    res = VD.check(sits, gt, dt.date(2026, 10, 12), equities=equities)
    assert set(res["register"]) == {"VEDL", "TRIVENI"}                      # universe demergers only
    byv = {r["symbol"]: r["verdict"] for r in res["recall"]}
    assert byv["VEDL"] == "captured" and byv["TRIVENI"] == "held as other restructuring only"
    assert [r["symbol"] for r in res["misses"]] == ["TRIVENI"]
    arrived = next(r for r in res["recall"] if r["symbol"] == "VEDL")["resulting_company_listed"]
    assert arrived == "TSPL (2026-05-20)"                                  # named like the read, in the window; the IPO is not
    byp = {r["symbol"]: r["verdict"] for r in res["precision"]}
    assert byp["VEDL"].startswith("verified") and byp["UPL"].startswith("pending")
    assert byp["DABUR"].startswith("FALSE POSITIVE (judge") and byp["GHOST"].startswith("FALSE POSITIVE (record date")
    s = res["summary"]
    assert (s["register_demergers"], s["captured"], s["missed"], s["false_positives"], s["pending"]) == (2, 1, 1, 2, 1)
    md = VD.render(res, "2026-10-12")
    assert "| …MISSED | 1 |" in md and "**TRIVENI**" in md and "FALSE POSITIVE" in md
