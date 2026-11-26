# Evaluation data

- `labelled_filings.csv` — a stratified random sample of the year's management filings (seed 20261126:
  filings the mechanical read flagged, filings that mention a seat but were not flagged, filings with no
  seat at all), each read by hand and labelled: does THIS filing disclose a change at the company's own
  CEO / MD / CFO seat? Seven sampled filings whose text did not settle the question on reading (long board
  outcomes, a restated interim charge) were left out rather than guessed.
- `reviewed_exceptions.csv` — exceptions from `evaluate.py` that a person has read and explained
  (`check,symbol,note`); they are shown with the note in `MANAGEMENT_CHANGE_EVAL.md`.
