#!/usr/bin/env bash
# resume_batch.sh — idempotent watchdog step for the QualityAnalysis batch.
#
#   bash resume_batch.sh START COUNT
#
# Safe to run any time, from any fresh container:
#   - already running          -> prints status, does nothing
#   - batch incomplete + dead  -> syncs branch state, relaunches the batch
#                                 and the 30-min checkpoint-commit loop
#   - batch complete           -> says so (final validation is the
#                                 operator's step — it needs judgement)
set -u
START="${1:?usage: resume_batch.sh START COUNT}"
COUNT="${2:?usage: resume_batch.sh START COUNT}"
REPO=/home/user/FinanceProject
QA="$REPO/IndividualStockAnalysis/India/Analysis/NiftyTotalMarketAnalysis/QualityAnalysis"
BRANCH=claude/quality-analysis-batch
LOG=/tmp/qa_batch_${START}_${COUNT}.log

cd "$REPO"

if pgrep -f "python3 analyze_batch[.]py run" >/dev/null; then
  echo "ALREADY RUNNING: $(grep -cE '^\[' "$LOG" 2>/dev/null || echo '?') companies logged so far"
  exit 0
fi

# fresh container? make sure we're on the batch branch with latest work
git fetch -q origin "$BRANCH" || true
if [ "$(git branch --show-current)" != "$BRANCH" ]; then
  git checkout -q "$BRANCH" 2>/dev/null || git checkout -qb "$BRANCH" "origin/$BRANCH"
fi
git merge -q --ff-only "origin/$BRANCH" 2>/dev/null || true
python3 -c "import pandas, PyPDF2" 2>/dev/null || pip install -q pandas PyPDF2

# done already?
expected=$(python3 - "$START" "$COUNT" <<'EOF'
import csv, sys
from pathlib import Path
start, count = int(sys.argv[1]), int(sys.argv[2])
qa = Path("IndividualStockAnalysis/India/Analysis/NiftyTotalMarketAnalysis/QualityAnalysis")
rows = list(csv.DictReader(open(
    "IndividualStockAnalysis/India/NiftyTotalMarket/niftytotalmarket_constituents.csv")))
syms = [r["nse_symbol"] for r in rows[start:start + count]]
missing = [s for s in syms if not ((qa / f"{s}_analysis.md").exists()
                                   and (qa / f"{s}_comparison.md").exists())]
print(len(missing))
EOF
)
if [ "$expected" = "0" ]; then
  echo "COMPLETE: all $COUNT companies of batch start=$START have both reports"
  exit 0
fi

echo "RESUMING: $expected companies still to do (start=$START count=$COUNT)"
cd "$QA"
nohup python3 analyze_batch.py run --start "$START" --count "$COUNT" \
  > "$LOG" 2>&1 &
echo "batch pid $!"

nohup bash -c '
cd '"$REPO"'
QA='"$QA"'
while pgrep -f "python3 analyze_batch[.]py run" >/dev/null; do
  sleep 1800
  cd "$QA"
  for a in *_analysis.md; do
    s="${a%_analysis.md}"
    [ -f "${s}_comparison.md" ] && git add "$a" "${s}_comparison.md" 2>/dev/null
  done
  cd '"$REPO"'
  git add IndividualStockAnalysis/India/Skills/*/.*cache*.json 2>/dev/null
  if ! git diff --cached --quiet; then
    git commit -q -m "QualityAnalysis: checkpoint — completed report pairs + judge caches

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0129m7453TBvAqwTs5dfy4AF" \
      && git push -q origin '"$BRANCH"'
  fi
done' > /tmp/qa_checkpoint.log 2>&1 &
echo "checkpoint loop pid $!"
