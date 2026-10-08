"""
Tests for source_override — running the AnalystSkill over a SUPPLIED
document (PDF / Markdown / text) instead of the conference-call archive.

  python3 -m pytest tests/test_source_override.py -q   (from AnalystSkill/)

No AI is invoked anywhere here. The judged path is exercised by SEEDING
the source caches with entries keyed exactly as the judge would key them
(the document's content hash) and asserting the pipeline serves them —
which proves the stamps, cache files and seams all line up.
"""

import json
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))

import registry as REG            # noqa: E402
import composer as C              # noqa: E402
import source_override as SO      # noqa: E402

INDIA = REG.INDIA
A_PDF = INDIA / "ConferenceCalls" / "NiftyTotalMarket" / "IXIGO.pdf"

DOC_TEXT = """# Sample Co — investor note

Sample Co sells industrial adhesives across India through 40 depots.
Management has run the company debt-free for a decade and says plainly:
"we grow only as fast as our cash allows". Gross margins held near 40%
for six years; a single customer is a quarter of revenue, and the CFO
resigned this March. The new Gujarat plant doubles capacity on a bet the
defence offset programme materialises within two years.
""" * 3          # comfortably past the 200-char floor


@pytest.fixture()
def doc(tmp_path):
    p = tmp_path / "note.md"
    p.write_text(DOC_TEXT)
    yield p
    SO.deactivate()


@pytest.fixture()
def clean_source_caches():
    files = [SO.SKILL_DIR / n for n in
             (".source_ba_cache.json", ".source_mb_cache.json",
              ".source_qr_cache.json", ".source_overview_cache.json",
              ".source_synth_cache.json")]
    for f in files:
        if f.exists():
            f.unlink()
    yield files
    for f in files:
        if f.exists():
            f.unlink()


# ------------------------------------------------------------- activation

def test_activation_repoints_the_evidence_seam(doc):
    d = SO.activate(doc)
    assert d["kind"] == "text" and d["chars"] > 600
    # every skill now resolves its evidence to the supplied file
    assert REG.MB_AZ._transcript_path("ANYSYM") == doc
    assert REG.QR_AZ._transcript_path("ANYSYM") == doc
    # the excerpt is the document's own text, labelled honestly
    ex, n, rng = REG.MB_AZ._timeline_excerpt("ANYSYM")
    assert "industrial adhesives" in ex
    assert rng == "supplied document"
    # caches moved to the source-specific files
    assert REG.BA_CACHE.name == ".source_ba_cache.json"
    assert REG.MB_AZ.CACHE.name == ".source_mb_cache.json"
    assert C.OVERVIEW_CACHE.name == ".source_overview_cache.json"


def test_deactivation_restores_everything(doc):
    before = (REG.MB_AZ._transcript_path, REG.BA_CACHE,
              REG.MB_AZ._timeline_excerpt, C.OVERVIEW_CACHE)
    SO.activate(doc)
    SO.deactivate()
    after = (REG.MB_AZ._transcript_path, REG.BA_CACHE,
             REG.MB_AZ._timeline_excerpt, C.OVERVIEW_CACHE)
    assert before == after
    # and the archive path is back to the real concall archive
    p = REG.MB_AZ._transcript_path("IXIGO")
    assert p.name == "IXIGO.pdf" and "ConferenceCalls" in str(p)


def test_a_pdf_is_a_valid_source():
    """Any text PDF works as a source — here, one from the repo itself."""
    if not A_PDF.exists():
        pytest.skip("no sample PDF in this checkout")
    try:
        d = SO.activate(A_PDF)
        assert d["kind"] == "pdf" and d["chars"] > 5000
        ex, _n, _rng = REG.MB_AZ._timeline_excerpt("WHATEVER")
        assert len(ex) > 2000
    finally:
        SO.deactivate()


def test_unusable_documents_are_refused(tmp_path):
    with pytest.raises(SO.SourceError):
        SO.activate(tmp_path / "missing.md")
    empty = tmp_path / "empty.md"
    empty.write_text("too short")
    with pytest.raises(SO.SourceError):
        SO.activate(empty)
    binary = tmp_path / "data.xlsx"
    binary.write_text("x" * 500)
    with pytest.raises(SO.SourceError):
        SO.activate(binary)
    assert not SO.active()


def test_unknown_company_takes_the_supplied_name(doc):
    SO.activate(doc, name="Sample Co Ltd")
    assert REG.company_meta("SAMPLECO")["name"] == "Sample Co Ltd"
    # a real constituent keeps its real name
    assert REG.company_meta("PIDILITIND")["name"] != "SAMPLECO"
    SO.deactivate()
    assert REG.company_meta("SAMPLECO")["name"] == "SAMPLECO"


# ------------------------------------------------- the pipeline, end to end

def test_known_company_keeps_its_numbers_and_reads_the_document(doc):
    """A universe symbol analysed over a supplied document: quantitative
    pillars intact from the stored statements, qualitative judged ONLY
    against the document (here unjudged: no AI, empty source caches)."""
    SO.activate(doc)
    ba, s1 = REG.run_business("PIDILITIND", ai=False)
    assert ba["overall"] is not None, "quant must survive a source run"
    assert s1 == "numbers_only", \
        "concall-archive judgements must NOT leak into a source run"
    assert ba["qualitative_included"] is False


def test_unknown_company_composes_an_honest_report(doc, tmp_path):
    SO.activate(doc, name="Sample Co Ltd")
    ba, _ = REG.run_business("SAMPLECO", ai=False)
    mb, _ = REG.run_patterns("SAMPLECO", ai=False)
    qr, _ = REG.run_risks("SAMPLECO", ai=False)
    exts = REG.run_extensions("SAMPLECO", ai=False)
    rt = C.compute_rating(ba, mb, qr, extensions=exts)
    assert rt["grade"] == "Not rated", \
        "no statements + no judged evidence must never produce a score"
    md = C.render("SAMPLECO", "Sample Co Ltd", ba, mb, qr, rt, None,
                  {"business": "numbers_only", "patterns": "numbers_only",
                   "risks": "numbers_only"}, extensions=exts)
    md = SO.annotate_md(md)
    assert "Sample Co Ltd" in md
    assert "**Evidence source:** the supplied document `note.md`" in md
    assert "conference-call archive was NOT used" in md


def test_seeded_source_cache_serves_the_judgement_without_ai(
        doc, clean_source_caches):
    """Seed the source caches EXACTLY as the judge would write them —
    stamps derived from the document's content hash — and the no-AI
    pipeline must serve the judgement. This proves the seam, the cache
    files and the stamp scheme line up end to end."""
    SO.activate(doc)
    h = REG.pdf_content_stamp(doc)
    sym = "SAMPLECO"
    ba_scores = [{"id": "MGT.candor", "score": 2,
                  "rationale": "states growth is capped by cash",
                  "quote": "we grow only as fast as our cash allows"}]
    (SO.SKILL_DIR / ".source_ba_cache.json").write_text(json.dumps(
        {sym: {"stamp": f"{h}:ba1:{REG.MODEL}", "scores": ba_scores}}))
    by_pattern = {"pricing_power": {
        "fit": "partial", "rationale": "margins held near 40% for years",
        "quote": ""}}
    (SO.SKILL_DIR / ".source_mb_cache.json").write_text(json.dumps(
        {sym: {"stamp": f"{h}:v1:{REG.MB_AZ.JUDGE_MODEL}",
               "by_pattern": by_pattern}}))
    by_risk = {"stakeholder_concentration": {
        "exposure": "high", "rationale": "one customer is a quarter of "
        "revenue and the CFO just left", "quote": "", "mitigant": ""}}
    (SO.SKILL_DIR / ".source_qr_cache.json").write_text(json.dumps(
        {sym: {"stamp": f"{h}:v1:{REG.QR_AZ.JUDGE_MODEL}",
               "by_risk": by_risk}}))

    ba, s1 = REG.run_business(sym, ai=False)
    assert s1 == "with_calls", "seeded source judgement must serve"
    assert ba["qualitative_included"] is True
    qual_mb = REG.MB_AZ.qual_judge(sym, REG.MB_PE.load_taxonomy(),
                                   allow_ai=False)
    assert qual_mb and "pricing_power" in qual_mb
    qual_qr = REG.QR_AZ.qual_judge(sym, REG.QR_RE.load_taxonomy(),
                                   allow_ai=False)
    assert qual_qr and "stakeholder_concentration" in qual_qr


def test_source_judgements_never_touch_the_archive_caches(
        doc, clean_source_caches):
    """The committed concall caches must be byte-identical across a
    source-mode run — supplied documents get their own files."""
    archive_caches = [SO.SKILL_DIR / ".qual_cache.json",
                      REG.SKILLS / "MultibaggerPattern" / ".qual_cache.json",
                      REG.SKILLS / "QualityRisks" / ".qual_cache.json"]
    before = [p.read_bytes() for p in archive_caches]
    SO.activate(doc)
    REG.run_business("PIDILITIND", ai=False)
    REG.run_patterns("PIDILITIND", ai=False)
    REG.run_risks("PIDILITIND", ai=False)
    after = [p.read_bytes() for p in archive_caches]
    assert before == after


def test_editing_the_document_is_honestly_a_cache_miss(
        doc, clean_source_caches):
    SO.activate(doc)
    h1 = REG.pdf_content_stamp(REG.MB_AZ._transcript_path("X"))
    doc.write_text(DOC_TEXT + "\nOne more paragraph of evidence.")
    REG._PDF_HASH_MEMO.clear()
    h2 = REG.pdf_content_stamp(REG.MB_AZ._transcript_path("X"))
    assert h1 != h2, "an edited document must not reuse old judgement"


def test_normal_mode_is_untouched_after_a_source_run(doc):
    """The concall pipeline must behave identically before and after a
    source-mode activation — no leakage between the modes."""
    ba0, s0 = REG.run_business("IXIGO", ai=False)
    SO.activate(doc)
    REG.run_business("IXIGO", ai=False)
    SO.deactivate()
    ba1, s1 = REG.run_business("IXIGO", ai=False)
    assert (s0, ba0["overall"], ba0["coverage"]) == \
           (s1, ba1["overall"], ba1["coverage"])


def test_long_documents_are_sampled_across_not_head_sliced(tmp_path):
    """A 450-page prospectus's first 90k chars are its cover page and
    definitions; the judges must see the middle chapters too."""
    long_doc = tmp_path / "prospectus.md"
    body = "".join(f"<<MARK {i}>> " + ("filler words " * 40) + "\n"
                   for i in range(4000))
    long_doc.write_text(body)
    try:
        SO.activate(long_doc)
        ex, _n, rng = REG.MB_AZ._timeline_excerpt("X", budget=90000)
        assert "sampled at spread offsets" in rng
        marks = [int(m) for m in
                 __import__("re").findall(r"<<MARK (\d+)>>", ex)]
        assert marks, "no content sampled"
        spread = (max(marks) - min(marks)) / 4000
        assert spread > 0.7, f"samples cover only {spread:.0%} of the doc"
        assert len(ex) <= 91000
    finally:
        SO.deactivate()
