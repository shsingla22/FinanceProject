"""
source_override.py — run the AnalystSkill over a SUPPLIED document.

Normally the qualitative side of every analysis reads the company's
conference-call archive from the repository. This module lets a run use a
DIFFERENT evidence source — a PDF, a Markdown file, or plain text that the
user supplies — while everything downstream stays the AnalystSkill
unchanged (the same judges, the same honesty rules, the same composer).

    python3 analyze.py report SYM out.md --source /path/to/document.pdf
    python3 analyze.py report ACME out.md --source notes.md --name "Acme Ltd"

How it works (the same lens pattern RecentAnalystSkill uses):

  * every skill reads its evidence through ONE seam — `_transcript_path()`
    in the MultibaggerPattern and QualityRisks modules (the analyst's own
    judge and the overview go through the former). `activate()` repoints
    that seam at the supplied file, so text extraction, the existence
    gates and the content-hash cache stamps all follow automatically.
  * judgements of supplied documents are cached in SEPARATE files
    (.source_*_cache.json, gitignored), keyed by the document's content
    hash — they never mix with the concall archive's committed verdicts,
    and re-running the same document is free.
  * the QUANTITATIVE side is untouched: a symbol in the universe keeps its
    statements, trends and index comparison; an unknown company honestly
    has none, and the rating re-normalises over what could be scored —
    the never-guess rule carries the whole report.

`deactivate()` restores everything, so one process can serve both modes.
"""

from __future__ import annotations

from pathlib import Path

import composer as C
import registry as REG

HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent

TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".text"}

_state: dict = {"active": False, "saved": {}, "doc": None, "text": ""}


class SourceError(ValueError):
    """The supplied document cannot serve as an evidence source."""


def _extract_text(doc: Path) -> str:
    if doc.suffix.lower() == ".pdf" or doc.suffix.lower() in TEXT_SUFFIXES:
        return REG.MB_AZ._read_doc(doc)
    raise SourceError(
        f"unsupported document type '{doc.suffix}' — supply a .pdf, .md or "
        f".txt file")


def active() -> bool:
    return _state["active"]


def describe() -> dict | None:
    """What the current run's evidence is — used for provenance."""
    if not _state["active"]:
        return None
    doc = _state["doc"]
    return {"path": str(doc), "name": doc.name,
            "kind": "pdf" if doc.suffix.lower() == ".pdf" else "text",
            "chars": len(_state["text"]),
            "hash": REG.pdf_content_stamp(doc)}


def activate(doc: str | Path, name: str | None = None) -> dict:
    """Point every qualitative read at `doc`. Idempotent per document;
    activating a second document deactivates the first."""
    if _state["active"]:
        deactivate()
    doc = Path(doc).expanduser().resolve()
    if not doc.exists():
        raise SourceError(f"document not found: {doc}")
    text = _extract_text(doc)
    if len(text.strip()) < 200:
        raise SourceError(
            f"no usable text in {doc.name} — extraction produced "
            f"{len(text.strip())} characters (a scanned/image PDF cannot "
            f"be read; supply a text PDF or a Markdown file)")

    saved = _state["saved"] = {}

    # 1. the evidence seam: both judge skills (the analyst's own judge and
    #    the overview read through MB's) now resolve to the supplied file
    saved["mb_path"] = REG.MB_AZ._transcript_path
    saved["qr_path"] = REG.QR_AZ._transcript_path
    REG.MB_AZ._transcript_path = lambda sym: doc
    REG.QR_AZ._transcript_path = lambda sym: doc

    # 2. excerpting: a concall archive is sampled across its timeline; a
    #    generic document is taken from the TOP (its tail is appendices).
    #    A document that carries the archive's own "Call: Mon YYYY"
    #    headers still gets the timeline treatment.
    def _doc_excerpt(orig, header_re):
        def wrapped(sym: str, budget: int = 90000):
            if header_re.search(text):
                return orig(sym, budget)
            return text[:budget], 1, "supplied document"
        return wrapped

    saved["mb_excerpt"] = REG.MB_AZ._timeline_excerpt
    saved["qr_excerpt"] = REG.QR_AZ._timeline_excerpt
    REG.MB_AZ._timeline_excerpt = _doc_excerpt(
        saved["mb_excerpt"], REG.MB_AZ.CALL_HEADER_RE)
    REG.QR_AZ._timeline_excerpt = _doc_excerpt(
        saved["qr_excerpt"], REG.QR_AZ.CALL_HEADER_RE)

    # 3. separate caches: supplied-document judgements never mix with the
    #    concall archive's committed verdicts. Stamps stay content-derived
    #    (they hash whatever _transcript_path returns — now the document),
    #    so the same document re-analysed is a cache hit and an edited
    #    document is honestly a miss.
    saved["ba_cache"] = REG.BA_CACHE
    saved["mb_cache"] = REG.MB_AZ.CACHE
    saved["qr_cache"] = REG.QR_AZ.CACHE
    saved["ov_cache"] = C.OVERVIEW_CACHE
    saved["sy_cache"] = C.SYNTH_CACHE
    REG.BA_CACHE = SKILL_DIR / ".source_ba_cache.json"
    REG.MB_AZ.CACHE = SKILL_DIR / ".source_mb_cache.json"
    REG.QR_AZ.CACHE = SKILL_DIR / ".source_qr_cache.json"
    C.OVERVIEW_CACHE = SKILL_DIR / ".source_overview_cache.json"
    C.SYNTH_CACHE = SKILL_DIR / ".source_synth_cache.json"

    # 4. a company outside the universe keeps the supplied display name
    if name:
        saved["meta"] = REG.company_meta
        base_meta = saved["meta"]

        def named_meta(sym: str) -> dict:
            meta = base_meta(sym)
            if meta["name"] == sym:          # not in the constituents file
                meta = {**meta, "name": name}
            return meta
        REG.company_meta = named_meta

    _state.update(active=True, doc=doc, text=text)
    return describe()


def deactivate() -> None:
    if not _state["active"]:
        return
    saved = _state["saved"]
    REG.MB_AZ._transcript_path = saved["mb_path"]
    REG.QR_AZ._transcript_path = saved["qr_path"]
    REG.MB_AZ._timeline_excerpt = saved["mb_excerpt"]
    REG.QR_AZ._timeline_excerpt = saved["qr_excerpt"]
    REG.BA_CACHE = saved["ba_cache"]
    REG.MB_AZ.CACHE = saved["mb_cache"]
    REG.QR_AZ.CACHE = saved["qr_cache"]
    C.OVERVIEW_CACHE = saved["ov_cache"]
    C.SYNTH_CACHE = saved["sy_cache"]
    if "meta" in saved:
        REG.company_meta = saved["meta"]
    _state.update(active=False, saved={}, doc=None, text="")


PROVENANCE_HEAD = "## How this report was built"


def annotate_md(md: str) -> str:
    """State the evidence source in the report itself — a reader of the
    file alone must know this analysis did NOT use the concall archive."""
    d = describe()
    if d is None or PROVENANCE_HEAD not in md:
        return md
    bullet = (f"\n\n- **Evidence source:** the supplied document "
              f"`{d['name']}` ({d['kind']}, {d['chars']:,} characters, "
              f"md5 {d['hash'][:12]}…). The conference-call archive was "
              f"NOT used for qualitative judgement in this run; the "
              f"quantitative statements are the repository's stored data "
              f"where the company has them.")
    head, tail = md.split(PROVENANCE_HEAD, 1)
    md = head + PROVENANCE_HEAD + bullet + tail
    # the no-overview placeholder blames missing transcripts; in a source
    # run the document was there — it just was not summarised without AI
    return md.replace(
        "*No conference-call transcripts were available to describe the "
        "business in management's own words — run the full analysis, or "
        "see the evidence sections below.*",
        "*The supplied document was not summarised into a business "
        "overview for this run — the evidence sections below are where "
        "its content is judged.*")
