"""
Re-fetch the P&L companies that failed in the original fetch_profit_loss.py
run (due to rate limiting). Uses a much longer delay and retries on HTTP 429.

Reads _fetch_log.csv, identifies entries that don't start with "ok",
re-fetches them, updates the per-company CSVs, appends rows to
_all_profit_loss_long.csv, and updates _fetch_log.csv in place.

Usage:
  python3 _refetch_failures.py
"""

import time
import sys
from pathlib import Path

import pandas as pd

# Reuse the fetcher functions from the main script
sys.path.insert(0, str(Path(__file__).parent))
import importlib.util
spec = importlib.util.spec_from_file_location("fpl", str(Path(__file__).parent / "fetch_profit_loss.py"))
fpl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fpl)

# Override delay to be slower for re-fetch
fpl.DELAY_BETWEEN_REQUESTS = 1.2

HERE = Path(__file__).parent
LOG_CSV = HERE / "_fetch_log.csv"
LONG_CSV = HERE / "_all_profit_loss_long.csv"


def main() -> None:
    log = pd.read_csv(LOG_CSV)
    failed_mask = ~log["status"].str.startswith("ok")
    failed_syms = log.loc[failed_mask, "nse_symbol"].tolist()
    print(f"Failed in original run: {len(failed_syms)}")

    long = pd.read_csv(LONG_CSV)

    new_long_rows: list[dict] = []
    updated_count = 0
    still_failed_count = 0

    for i, sym in enumerate(failed_syms, 1):
        try:
            df, long_rows, status = fpl.fetch_company_detailed(sym)
        except Exception as e:
            df, long_rows, status = None, [], f"exception:{type(e).__name__}:{str(e)[:50]}"

        if df is not None:
            safe_name = sym.replace("&", "_AND_")
            out_path = HERE / f"{safe_name}.csv"
            df.to_csv(out_path)
            new_long_rows.extend(long_rows)
            updated_count += 1
        else:
            still_failed_count += 1

        # Update the status in the log
        log.loc[log["nse_symbol"] == sym, "status"] = status

        if i % 10 == 0 or i == len(failed_syms):
            print(f"  [{i:3d}/{len(failed_syms)}] last={sym:<14s} updated={updated_count} still_failed={still_failed_count} "
                  f"last_status={status[:70]}")
        time.sleep(fpl.DELAY_BETWEEN_REQUESTS)

    # Rewrite log
    log.to_csv(LOG_CSV, index=False)

    # Append new long rows to the long CSV
    if new_long_rows:
        long_extended = pd.concat([long, pd.DataFrame(new_long_rows)], ignore_index=True)
        long_extended.to_csv(LONG_CSV, index=False)

    print("-" * 60)
    print(f"DONE. Recovered {updated_count}/{len(failed_syms)}. Still failed: {still_failed_count}.")
    new_ok = log["status"].str.startswith("ok").sum()
    print(f"Total ok now: {new_ok}/{len(log)}")


if __name__ == "__main__":
    main()
