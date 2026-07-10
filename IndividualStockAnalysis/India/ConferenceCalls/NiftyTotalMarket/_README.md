# Conference Calls — NIFTY Total Market constituents

**Universe:** 742 cos comprising the NSE NIFTY TOTAL MARKET index
(Nifty 500 ∪ Nifty Microcap 250). Exact list in
`../../NiftyTotalMarket/niftytotalmarket_constituents.csv`.

## What's here

For each company that has hosted quarterly investor conference calls
in the last 3 years, we produce **one consolidated PDF** named
`{NSE_SYMBOL}.pdf` containing the text of every transcript in
**chronological order — oldest call first, newest last**.

Each transcript section starts with a quarter header
(e.g. `Call: May 2023`) followed by the extracted text.

## Files

- `{NSE_SYMBOL}.pdf` — 677 cos, one file each
- `_fetch_log.csv` — per-co status with counts:
  `ok:calls_listed=N:downloaded=M:text_ok=K` reports how many calls
  screener.in listed, how many PDFs downloaded successfully, and
  how many had extractable text.

## Coverage

| Status | Count |
|---|--:|
| `ok` — PDF produced | **677 / 742** |
| `no_concalls_listed` (screener has empty Concalls section — typically banks/insurance/utilities or recently-listed cos) | 57 |
| `no_recent_concalls` (concalls listed but none in last 3 yrs) | 8 |
| **Total transcripts captured** | **~6,800** |
| **Average transcripts per company** | 10.1 |

## Source chain

1. **Listing:** screener.in's `<div class="documents concalls flex-column">`
   on each company page — one `<li>` per quarter with a date label
   (`MMM YYYY`) and a "Transcript" link.
2. **PDF download:** transcript URLs point to `bseindia.com`
   (BSE's official corporate-announcement PDF host). Downloaded
   with 4-way thread concurrency, 0.4 s delay between calls per co.
3. **Text extraction:** PyPDF2's `extract_text()`. Scanned-image
   transcripts (no embedded text) are surfaced as placeholders
   inside the consolidated PDF.
4. **Re-pack:** reportlab's `SimpleDocTemplate` flowables. A4 page,
   1.5 cm margins, 9 pt body, quarter headers as Heading2, page
   break between calls.

## Reproducibility

```
python3 ../fetch_concalls.py                                # default
python3 ../fetch_concalls.py --skip-existing                # incremental
python3 ../fetch_concalls.py --only RELIANCE,TCS,HDFCBANK   # spot check
python3 ../fetch_concalls.py --years 5                      # 5-yr lookback
```

## Caveats

- Some transcript PDFs are scanned-image only; their text comes
  out empty (PyPDF2 has no built-in OCR). They still appear in
  the output PDF with a placeholder note. For OCR-quality text,
  pair with a Tesseract / pdf-OCR pass.
- BSE occasionally returns 403 / 404 for valid-looking URLs;
  those calls are silently skipped (the consolidated PDF includes
  the date header but no body for that call).
- The PDFs are text-only (no original layout / images preserved).
  This keeps them small (~350 KB / co on average) and ideal for
  downstream LLM / search workflows.
