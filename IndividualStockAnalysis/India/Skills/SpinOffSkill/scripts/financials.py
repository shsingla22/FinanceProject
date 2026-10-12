"""
financials.py — the numbers and the documents behind each spin-off.

  parent_financials(sym)   sales, operating profit, PAT with growth and
                           margins for the last three fiscal years, from
                           the stored P&L
  cash_flows(sym)          CFO / CFI / CFF / net / free cash flow, three
                           years, from the stored cash-flow statements
  pe_ratio(sym, live)      the P/E — live market file when the company is
                           in it, else latest stored close ÷ latest EPS,
                           method and date stated
  mermaid_chart(...)       a Mermaid xychart (renders on GitHub) of the
                           three-year series
  rationale_excerpts(sym)  every demerger / spin-off passage in the last
                           36 months of calls, each with the transcript's
                           source link
  segment_excerpts(sym, names)
                           the segment-reporting pages of the stored
                           annual reports and the pages of the quarterly
                           presentations that name the business, each
                           with document and page
  doc_links(sym)           the source URLs of every stored report

Nothing is computed from a number that is not on file; every value says
which statement and year it came from.
"""

from __future__ import annotations

import csv
import datetime as dt
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
PNL = INDIA / "ProfitStatement" / "NiftyTotalMarket"
CASH = INDIA / "CashFlow" / "NiftyTotalMarket"
DAILY = INDIA / "VolumeAndPricing" / "NiftyTotalMarket" / "_all_daily_long.csv"
CONCALLS = INDIA / "ConferenceCalls" / "NiftyTotalMarket"
PPT_DIR = INDIA / "InvestorPresentations" / "NiftyTotalMarket"
AR_DIR = INDIA / "AnnualReports" / "NiftyTotalMarket"
LINKS = PPT_DIR / "_concall_links.csv"

YEARS = 3
_MONTHS = {m: i + 1 for i, m in enumerate(
    "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


# ------------------------------------------------------------ statements

def _table(path: Path) -> tuple[list[str], dict[str, list[float | None]]]:
    """(year labels, {line item: values}) from a stored statement CSV."""
    if not path.exists():
        return [], {}
    with open(path) as fh:
        rows = list(csv.reader(fh))
    if not rows:
        return [], {}
    years = rows[0][2:]
    out = {}
    for r in rows[1:]:
        if not r:
            continue
        vals = []
        for v in r[2:]:
            try:
                vals.append(float(v))
            except ValueError:
                vals.append(None)
        out[r[0]] = vals
    return years, out


def _last_years(years: list[str], series: dict, n: int = YEARS) -> list[int]:
    """Indexes of the last n year columns that carry a Sales (or first
    item) value — statements sometimes end with an empty column."""
    key = "Sales" if "Sales" in series else next(iter(series), None)
    if key is None:
        return []
    idx = [i for i, v in enumerate(series[key]) if v is not None]
    return idx[-(n + 1):]          # one extra for the first year's growth


def _growth(cur, prev):
    if cur is None or prev is None or prev == 0:
        return None
    return round((cur - prev) / abs(prev) * 100, 1)


def _margin(num, den):
    if num is None or den in (None, 0):
        return None
    return round(num / den * 100, 1)


def parent_financials(symbol: str, n: int = YEARS) -> dict:
    """Three fiscal years of the parent's consolidated P&L, with growth
    and margins computed here (never read from a model)."""
    years, s = _table(PNL / f"{symbol}.csv")
    idx = _last_years(years, s, n)
    if len(idx) < 2:
        return {"available": False, "source": str(PNL / f"{symbol}.csv")}
    show = idx[1:] if len(idx) > n else idx
    g = lambda item, i: (s.get(item) or [None] * len(years))[i]      # noqa: E731
    rows = []
    labels = [years[i] for i in show]
    def series(item):
        return [g(item, i) for i in show]
    def growth(item):
        out = []
        for k, i in enumerate(show):
            prev = idx[idx.index(i) - 1] if idx.index(i) > 0 else None
            out.append(_growth(g(item, i), g(item, prev) if prev is not None else None))
        return out
    sales, op, pat = series("Sales"), series("Operating Profit"), series("Net Profit")
    rows = [
        {"metric": "Sales (₹ cr)", "values": sales},
        {"metric": "Sales growth (%)", "values": growth("Sales")},
        {"metric": "Operating profit (₹ cr)", "values": op},
        {"metric": "Operating profit growth (%)", "values": growth("Operating Profit")},
        {"metric": "Operating margin (%)", "values": [_margin(o, sl) for o, sl in zip(op, sales)]},
        {"metric": "PAT (₹ cr)", "values": pat},
        {"metric": "PAT growth (%)", "values": growth("Net Profit")},
        {"metric": "PAT margin (%)", "values": [_margin(p, sl) for p, sl in zip(pat, sales)]},
        {"metric": "EPS (₹)", "values": series("EPS in Rs")},
    ]
    return {"available": True, "years": labels, "rows": rows,
            "source": f"ProfitStatement/NiftyTotalMarket/{symbol}.csv (consolidated, screener.in)"}


def cash_flows(symbol: str, n: int = YEARS) -> dict:
    years, s = _table(CASH / f"{symbol}.csv")
    key = "Cash from Operating Activity"
    if key not in s:
        return {"available": False}
    idx = [i for i, v in enumerate(s[key]) if v is not None][-n:]
    if not idx:
        return {"available": False}
    items = [("Cash from operations (₹ cr)", key),
             ("Cash from investing (₹ cr)", "Cash from Investing Activity"),
             ("Cash from financing (₹ cr)", "Cash from Financing Activity"),
             ("Net cash flow (₹ cr)", "Net Cash Flow"),
             ("Free cash flow (₹ cr)", "Free Cash Flow")]
    rows = [{"metric": m, "values": [(s.get(k) or [None] * len(years))[i] for i in idx]}
            for m, k in items if k in s]
    return {"available": True, "years": [years[i] for i in idx], "rows": rows,
            "source": f"CashFlow/NiftyTotalMarket/{symbol}.csv (consolidated, screener.in)"}


_CLOSE_CACHE: dict[str, tuple[str, float]] | None = None


def latest_closes() -> dict[str, tuple[str, float]]:
    """{symbol: (date, close)} from the stored daily bars, read once."""
    global _CLOSE_CACHE
    if _CLOSE_CACHE is None:
        _CLOSE_CACHE = {}
        if DAILY.exists():
            with open(DAILY) as fh:
                rd = csv.DictReader(fh)
                for r in rd:
                    sym, d = r.get("symbol"), r.get("date")
                    try:
                        c = float(r.get("close") or "")
                    except ValueError:
                        continue
                    if sym and (sym not in _CLOSE_CACHE or d > _CLOSE_CACHE[sym][0]):
                        _CLOSE_CACHE[sym] = (d, c)
    return _CLOSE_CACHE


def pe_ratio(symbol: str, live: dict | None = None) -> dict:
    """The parent's P/E with its method: the live market file (Nifty 500
    members) or latest stored close ÷ latest fiscal-year EPS."""
    lm = (live or {}).get(symbol)
    if lm and lm.get("stock_pe") not in (None, "", "nan"):
        try:
            return {"pe": float(lm["stock_pe"]), "price": float(lm["current_price_rs"]),
                    "as_of": (lm.get("fetched_at") or "")[:10],
                    "method": "live market file (screener.in), trailing"}
        except ValueError:
            pass
    years, s = _table(PNL / f"{symbol}.csv")
    eps = s.get("EPS in Rs") or []
    idx = [i for i, v in enumerate(eps) if v is not None]
    close = latest_closes().get(symbol)
    if not idx or not close:
        return {"pe": None, "method": "no price or EPS on file"}
    e = eps[idx[-1]]
    if e <= 0:
        return {"pe": None, "price": close[1], "as_of": close[0],
                "method": f"EPS {e} for {years[idx[-1]]} is not positive"}
    return {"pe": round(close[1] / e, 1), "price": close[1], "as_of": close[0],
            "method": f"close {close[0]} ÷ EPS {e} ({years[idx[-1]]})"}


# ----------------------------------------------------------------- charts

def mermaid_chart(title: str, years: list[str], series: dict[str, list],
                  y_label: str, kind: str = "bar") -> str:
    """A Mermaid xychart-beta fenced block. Every series must have a value
    for every year (Mermaid cannot skip a point); series with a gap are
    left out and named in a comment line."""
    xs = [f'"{y}"' for y in years]
    lines = ["```mermaid", "xychart-beta", f'    title "{title}"',
             f"    x-axis [{', '.join(xs)}]", f'    y-axis "{y_label}"']
    plotted, skipped = [], []
    for name, vals in series.items():
        if any(v is None for v in vals) or len(vals) != len(years):
            skipped.append(name)
            continue
        lines.append(f"    {kind} [{', '.join(f'{v:g}' for v in vals)}]")
        plotted.append(name)
    if not plotted:
        return ""
    lines.append("```")
    legend = ", ".join(plotted)
    note = f"*Series in order: {legend}.*" + (f" *Not plotted (gap in the data): {', '.join(skipped)}.*"
                                            if skipped else "")
    return "\n".join(lines) + "\n" + note


def charts_for(fin: dict) -> list[str]:
    """The two charts the report shows: the ₹ crore lines and the margins."""
    if not fin.get("available"):
        return []
    rows = {r["metric"]: r["values"] for r in fin["rows"]}
    out = []
    c1 = mermaid_chart("Sales, operating profit and PAT (₹ cr)", fin["years"],
                       {"Sales": rows["Sales (₹ cr)"], "Operating profit": rows["Operating profit (₹ cr)"],
                        "PAT": rows["PAT (₹ cr)"]}, "₹ crore")
    c2 = mermaid_chart("Margins (%)", fin["years"],
                       {"Operating margin": rows["Operating margin (%)"],
                        "PAT margin": rows["PAT margin (%)"]}, "%", kind="line")
    return [c for c in (c1, c2) if c]


# -------------------------------------------------------------- documents

def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path) as fh:
        return list(csv.DictReader(fh))


def doc_links(symbol: str) -> dict:
    """{'annual_reports': [(label, url, text_path)], 'presentations':
    [...], 'calls': {label: transcript_url}}."""
    ar = [(r["label"], r["url"], AR_DIR / symbol / r["text_file"])
          for r in _read(AR_DIR / symbol / "_index.csv") if r.get("text_file")]
    ppt = [(r["label"], r["url"], PPT_DIR / symbol / r["text_file"])
           for r in _read(PPT_DIR / symbol / "_index.csv") if r.get("text_file")]
    calls = {r["label"]: r["transcript_url"] for r in _read(LINKS)
             if r["symbol"] == symbol and r.get("transcript_url")}
    return {"annual_reports": ar, "presentations": ppt, "calls": calls}


def pages_of(text: str) -> list[tuple[int, str]]:
    """[(page number, page text)] from a page-marked text file."""
    parts = re.split(r"\n=== page (\d+) ===\n", text)
    out = []
    for i in range(1, len(parts) - 1, 2):
        out.append((int(parts[i]), parts[i + 1]))
    return out


GENERIC_WORDS = {"limited", "private", "business", "company", "demerged", "undertaking",
                 "resulting", "transferee", "transferor", "india", "indian", "group", "division",
                 "segment", "entity", "management", "services", "solutions", "products", "scheme"}


AR_PAGE_CHARS = 12_000       # a segment note's tables are dense; do not cut them


def segment_excerpts(symbol: str, names: list[str], cap: int = 110_000) -> list[dict]:
    """The pages that carry the piece's own numbers: annual-report pages
    with segment reporting that name the business, then presentation
    pages that name it. Each excerpt carries document, label and page."""
    names = [n for n in names if n and len(n) > 2]
    if not names:
        return []
    # the business's own words: whole names, plus their distinctive tokens
    # (the segment table may say "Leisure Hospitality and Resorts" where
    # the scheme says "Sterling Holiday Resorts Limited")
    tokens = set()
    for n in names:
        for w in re.findall(r"[A-Za-z]{5,}", n):
            if w.lower() not in GENERIC_WORDS:
                tokens.add(w)
    name_rx = re.compile("|".join(re.escape(x) for x in sorted(set(names) | tokens, key=len, reverse=True)), re.I)
    seg_rx = re.compile(r"segment (revenue|result|information|reporting|wise)|"
                        r"operating segments?|business segments?|reportable segments?", re.I)
    links = doc_links(symbol)
    cands = []
    for label, url, path in links["annual_reports"]:
        if not path.exists():
            continue
        pages = pages_of(path.read_text(errors="replace"))
        by_page = dict(pages)
        picked = set()
        for page, txt in pages:
            nums = len(re.findall(r"\d[\d,]{2,}", txt))
            segs = len(seg_rx.findall(txt))
            named = bool(name_rx.search(txt))
            if segs and (named or nums >= 25):
                # a segment TABLE is dense with numbers; prose pages are not.
                # The segment-reporting note itself (all segments, no brand
                # name) is always wanted — the judge picks the column — and
                # its tables run onto the next page, so that page comes too.
                score = nums + 20 * segs + (15 if named else 0)
                for pg, bonus in ((page, 0), (page + 1, -5)):
                    if pg in by_page and pg not in picked:
                        picked.add(pg)
                        cands.append((score + bonus, label, url, pg,
                                      re.sub(r"[ \t]+", " ", by_page[pg]).strip()[:AR_PAGE_CHARS]))
    for label, url, path in links["presentations"][:6]:
        if not path.exists():
            continue
        for page, txt in pages_of(path.read_text(errors="replace")):
            if (name_rx.search(txt) or seg_rx.search(txt)) and re.search(r"\d{2,}", txt):
                score = len(re.findall(r"\d[\d,]{2,}", txt)) + (10 if name_rx.search(txt) else 0)
                cands.append((score, f"Presentation {label}", url, page,
                              re.sub(r"[ \t]+", " ", txt).strip()[:3_000]))
    cands.sort(key=lambda c: -c[0])
    # budget: annual-report pages may take 70% of the cap; presentation
    # pages keep the rest, so the latest quarter is never crowded out
    out, used_ar, used_ppt = [], 0, 0
    for score, label, url, page, snippet in cands:
        is_ppt = label.startswith("Presentation")
        if is_ppt and used_ppt + len(snippet) > cap * 0.3:
            continue
        if not is_ppt and used_ar + len(snippet) > cap * 0.7:
            continue
        out.append({"doc": label, "url": url, "page": page, "text": snippet, "numbers": score})
        if is_ppt:
            used_ppt += len(snippet)
        else:
            used_ar += len(snippet)
    out.sort(key=lambda e: (not e["doc"].startswith("Annual"), e["doc"], e["page"]))
    return out


MENTION_RX = re.compile(
    r"\bde-?merg\w*|spin[\s-]?offs?|hiv(e|ing)[\s-]?off|carve[\s-]?out|"
    r"(separate|independent) listing|list(ing)? (of )?(the |our |its )?(subsidiar|arm|business)|"
    r"value[\s-]?unlock\w*|scheme of arrangement|restructur\w* (of|the) (business|group|company)", re.I)


def rationale_excerpts(symbol: str, months: int = 36, today: dt.date | None = None,
                       pad: int = 700, per_call: int = 5, cap: int = 40_000) -> list[dict]:
    """Every passage in the last `months` of calls where management or an
    analyst spoke about the separation — wide windows so the WHY survives
    — each with the call's label and its transcript link."""
    today = today or dt.date.today()
    path = CONCALLS / f"{symbol}.pdf"
    if not path.exists():
        return []
    try:
        import PyPDF2                                  # noqa: PLC0415
        text = "\n".join((pg.extract_text() or "") for pg in
                         PyPDF2.PdfReader(str(path), strict=False).pages)
    except Exception:                                  # noqa: BLE001
        return []
    cutoff = dt.date(today.year, today.month, 1) - dt.timedelta(days=months * 31)
    links = doc_links(symbol)["calls"]
    parts = re.split(r"(Call: \w{3} \d{4})", text)
    out, used = [], 0
    for i in range(1, len(parts) - 1, 2):
        label = parts[i].replace("Call: ", "")
        m = re.match(r"(\w{3}) (\d{4})", label)
        if not m or m.group(1) not in _MONTHS:
            continue
        if dt.date(int(m.group(2)), _MONTHS[m.group(1)], 1) < cutoff:
            continue
        body = parts[i + 1]
        last_end, n = -1, 0
        for hit in MENTION_RX.finditer(body):
            if hit.start() < last_end:
                continue
            a, b = max(0, hit.start() - pad), min(len(body), hit.end() + pad)
            q = re.sub(r"\s+", " ", body[a:b]).strip()
            out.append({"call": label, "url": links.get(label, ""), "quote": q})
            used += len(q)
            last_end = b
            n += 1
            if n >= per_call or used > cap:
                break
        if used > cap:
            break
    return out
