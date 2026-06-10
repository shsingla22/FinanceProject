# Management Info — NIFTY Total Market constituents

**Universe:** 742 cos comprising the NSE NIFTY TOTAL MARKET index.
Exact list in `../../NiftyTotalMarket/niftytotalmarket_constituents.csv`.

## What's here

For each company, a CSV summarizing the **Chairman / Managing Director /
CEO / CFO** named in the last 5 fiscal years of annual reports, with
5-year change tracking:

| Column | Meaning |
|---|---|
| `role` | Chairman, Managing Director, CEO, or CFO |
| `name` | Person's name as printed in the AR |
| `qualification` | Best-effort degree snippet (e.g. "holds a B.Tech from IIT…") — often empty |
| `experience` | Best-effort "X years of experience" snippet — often empty |
| `years_present` | FY range the person appears in (e.g. `FY2022–FY2026`), or comma list if non-contiguous |
| `status` | `current` if present in the latest AR, `exited` otherwise |
| `first_seen_in_ar` | URL of the earliest AR where the person was found |

People appearing in multiple years are listed **once** with their year
range — per the original spec. A change of personnel shows up as one
`exited` row + one `current` row with adjoining year ranges.

## Coverage

| | Count |
|---|--:|
| Cos with a management CSV | **658 / 742** (89%) |
| Cos with no extractable people | 84 |
| Total (role, person) rows | 4,437 |
| — Chairman | 2,122 |
| — Managing Director | 1,436 |
| — CFO | 657 |
| — CEO | 222 |

The 84 misses are mostly PSU banks / insurance cos whose ARs are
scanned-image PDFs (no embedded text layer; no OCR in this pipeline)
or recent IPOs with no AR yet.

## Method & caveats (IMPORTANT)

- Source: each company's last 5 annual-report PDFs (listed on
  screener.in, hosted on bseindia.com). Only the **first 80 pages**
  of each AR are parsed (board profiles virtually always live there).
- Extraction is **regex-based**, matching tight patterns like
  "Mr. <Name>, Managing Director" / "Chairman: Shri <Name>".
  Names + designations are fairly reliable; **qualification and
  experience fields are best-effort** and empty for most rows —
  AR prose is too varied for regex. For high-quality bios, an
  LLM-extraction pass over the same cached PDFs is the upgrade path.
- Chairman rows over-count: ARs mention committee chairpersons and
  guest names near the "Chairman" keyword; the tight patterns reduce
  but don't eliminate this. Treat `Chairman` rows with more
  scepticism than `CFO`/`MD` rows.
- The downloaded AR PDFs (~10 GB) are cached to `/tmp/mgmt_ar_cache/`
  during the run and deleted afterwards — they are NOT in git.

## Reproducibility

```
python3 ../fetch_management_info.py                       # full run
python3 ../fetch_management_info.py --skip-existing       # resume
python3 ../fetch_management_info.py --only RELIANCE,TCS   # spot check
python3 ../fetch_management_info.py --keep-cache          # keep AR PDFs
```
