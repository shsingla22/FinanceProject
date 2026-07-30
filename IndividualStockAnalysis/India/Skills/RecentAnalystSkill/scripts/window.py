"""
window.py — the one-year lens over the AnalystSkill.

This skill IS the AnalystSkill — same three sibling skills, same engines,
same composer, same explainability contract — with exactly one difference:
every piece of evidence is restricted to the LAST ONE YEAR:

  - financial statements: only the latest fiscal year, plus the
    immediately-prior year kept solely as the comparison baseline (you
    cannot say "improved vs last year" without the baseline);
  - conference calls: only the last four quarterly calls (~12 months);
  - the judges are explicitly instructed to judge the CURRENT state of
    the business, not the multi-year trajectory.

The window is applied at the DATA layer — the engines themselves are the
AnalystSkill's, untouched — so every check, ladder, derivation and report
behaves identically, and checks that genuinely need longer history say so
honestly instead of silently computing on data the lens excludes. All AI
caches live in THIS folder, fully separate from the full-history skill's.

NOTE: this module windows the loaded engine instances, so it must run in
its own process (the CLI below guarantees that). Do not import it next to
the full-history AnalystSkill in one process.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # .../scripts
RECENT = HERE.parent                            # .../RecentAnalystSkill
SKILLS = RECENT.parent

WINDOW_YEARS = 2      # latest FY + baseline year
WINDOW_CALLS = 4      # ~12 months of quarterly calls

sys.path.insert(0, str(SKILLS / "AnalystSkill" / "scripts"))
import registry as AR       # noqa: E402  (loads all three sibling skills)
import composer as AC       # noqa: E402

# ----------------------------------------------------- 1. window the frames
def _filter_frame(df):
    """Keep, per company, only its WINDOW_YEARS most recent fiscal years."""
    if df is None or getattr(df, "empty", True):
        return df
    if "year" not in df.columns or "nse_symbol" not in df.columns:
        return df
    d = df.copy()
    d["_yk"] = d["year"].map(AR.MB_QE._year_key)

    def cutoff(s):
        u = sorted(set(s), reverse=True)
        return u[min(WINDOW_YEARS, len(u)) - 1]

    d = d[d["_yk"] >= d.groupby("nse_symbol")["_yk"].transform(cutoff)]
    return d.drop(columns=["_yk"])


_orig_mb_load = AR.MB_QE._load
_orig_qr_load = AR.QR_QE._load


def _mb_load(base, universe):
    return {k: _filter_frame(v) for k, v in _orig_mb_load(base, universe).items()}


def _qr_load(base, universe):
    return {k: _filter_frame(v) for k, v in _orig_qr_load(base, universe).items()}


AR.MB_QE._load = _mb_load
AR.QR_QE._load = _qr_load
AR.MB_QE._frames = {}
AR.QR_QE._frames = {}

# BusinessAnalysis reads through Q.load_statement (already wrapped by the
# shared build_data cache) — layer the window on top and clear that cache.
_orig_q_load = AR.Q.load_statement
AR.Q.load_statement = lambda *a, **k: _filter_frame(_orig_q_load(*a, **k))
try:
    AR.BD._load_cache.clear()
except Exception:
    pass

# --------------------------------------------- 2. window the concall reads
LENS_NOTE = (
    "IMPORTANT — ONE-YEAR LENS: this analysis deliberately covers ONLY the "
    "last 12 months. The call excerpts below are the company's most recent "
    "quarterly calls only. Judge the CURRENT state of the business as these "
    "recent calls show it — recent delivery, recent pricing, recent risks. "
    "Where a judgement truly needs multi-year evidence you do not have, "
    "return null rather than inferring a long-term trajectory.")


def _windowed_timeline(sym: str, budget: int = 45000):
    full = AR.MB_AZ._concall_text(sym)
    if not full:
        return "", 0, ""
    parts = AR.MB_AZ.CALL_HEADER_RE.split(full)
    calls = [(parts[i], parts[i + 1].strip())
             for i in range(1, len(parts) - 1, 2)]
    calls = [(d, t) for d, t in calls if len(t) > 800][-WINDOW_CALLS:]
    if not calls:
        return full[-budget:], 1, "the most recent call text"
    per = budget // len(calls)
    ex = "\n\n".join(
        f"===== CALL {i + 1} of {len(calls)} in the last-12-months window "
        f"({d}) =====\n{t[:per]}"
        for i, (d, t) in enumerate(calls))
    return ex, len(calls), f"{calls[0][0]} to {calls[-1][0]} (last 12 months)"


AR.MB_AZ._timeline_excerpt = _windowed_timeline
AR.QR_AZ._timeline_excerpt = _windowed_timeline

_orig_mb_prompt = AR.MB_AZ._qual_prompt
_orig_qr_prompt = AR.QR_AZ._qual_prompt
_orig_ba_prompt = AR._ba_qual_prompt


def _wrap_prompt(orig):
    def wrapped(*a, **k):
        p = orig(*a, **k)
        return None if p is None else LENS_NOTE + "\n\n" + p
    return wrapped


AR.MB_AZ._qual_prompt = _wrap_prompt(_orig_mb_prompt)
AR.QR_AZ._qual_prompt = _wrap_prompt(_orig_qr_prompt)
AR._ba_qual_prompt = _wrap_prompt(_orig_ba_prompt)

# ------------------------------------- 3. this skill's own, separate caches
AR.BA_CACHE = RECENT / ".ba_qual_cache.json"
AR.MB_AZ.CACHE = RECENT / ".mb_qual_cache.json"
AR.QR_AZ.CACHE = RECENT / ".qr_qual_cache.json"
AC.SYNTH_CACHE = RECENT / ".synth_cache.json"
AC.OVERVIEW_CACHE = RECENT / ".overview_cache.json"

# ------------------------- 4. window-aware explanations (explainability)
WINDOW_EXPL = (" (One-year lens: this view only sees the latest two "
               "financial years, so longer-trend checks are out of scope "
               "by design.)")


def _annotate(checks: dict, flag_key: str) -> dict:
    for c in checks.values():
        if c.get(flag_key) is None and c.get("explanation") \
                and WINDOW_EXPL not in c["explanation"]:
            c["explanation"] = c["explanation"].rstrip() + WINDOW_EXPL
    return checks


_orig_mb_checks = AR.MB_QE.compute_checks
_orig_qr_checks = AR.QR_QE.compute_checks
AR.MB_QE.compute_checks = lambda *a, **k: _annotate(_orig_mb_checks(*a, **k),
                                                    "passed")
AR.QR_QE.compute_checks = lambda *a, **k: _annotate(_orig_qr_checks(*a, **k),
                                                    "flagged")

# --------------------------------------------- 5. the lens on the report
LENS_BANNER = (
    "**The one-year lens:** this is the SAME analysis the full AnalystSkill "
    "runs — the 34-check quality framework, the 11 multibagger patterns and "
    "the 8 risk channels — deliberately restricted to the last fiscal year "
    "(the prior year is kept only as the comparison baseline) and the last "
    "12 months of earnings calls. It answers \"what does the business look "
    "like RIGHT NOW?\" — checks that genuinely need longer history say so "
    "honestly instead of guessing. For the long-view verdict, use the "
    "full-history AnalystSkill report alongside this one.")

_orig_render = AC.render


def _windowed_render(*args, **kwargs) -> str:
    md = _orig_render(*args, **kwargs)
    lines = md.splitlines()
    lines[0] = lines[0].replace("— The Analyst's Report",
                                "— The Analyst's Report · Last One Year")
    lines.insert(1, "")
    lines.insert(2, LENS_BANNER)
    out = "\n".join(lines)
    return out.replace(
        "stored data (financial statements, working capital, conference-call "
        "transcripts, management history):",
        "stored data, RESTRICTED TO THE LAST ONE YEAR (latest fiscal year "
        "plus the prior year as baseline; last 12 months of calls):")


AC.render = _windowed_render
