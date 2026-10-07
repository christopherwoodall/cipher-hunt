#!/bin/bash
# Control runs for the 6 synthetic instances (2 parallel streams).
# Run from code/side-homophonic/solver. Per-run wall-clock recorded.
# Chance analytic values from control/chance_baseline.json (primary.analytic).
cd "$(dirname "$0")" || exit 1
declare -A CHANCE=(
  [184101]=0.022093170054286074
  [184102]=0.021588183310188108
  [184103]=0.022093170054286074
  [184104]=0.020830703194041157
  [184105]=0.021588183310188108
  [184106]=0.021335689938139123
)
SEEDS="184101 184102 184103 184104 184105 184106"
RUNLOG="../runs/control_batch.log"
mkdir -p ../runs
run_one() {
  local seed=$1
  local t0=$(date +%s)
  echo "[batch] START seed=$seed $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$RUNLOG"
  python3 control_harness.py \
    --ct ../control/instances/SYNTHETIC-ct-${seed}.pairs.txt \
    --truth ../control/instances/SYNTHETIC-key-${seed}.json \
    --crib ../control/instances/SYNTHETIC-crib-${seed}.json \
    --chance ${CHANCE[$seed]} \
    --lm lm_ref/lm.json \
    --out ../runs/ctl-${seed} \
    > ../runs/ctl-${seed}.stdout.log 2>&1
  local rc=$?
  local t1=$(date +%s)
  echo "[batch] DONE seed=$seed rc=$rc wall=$((t1-t0))s $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$RUNLOG"
}
for s in $SEEDS; do
  run_one "$s" &
  # cap at 2 concurrent
  while [ "$(jobs -r | wc -l)" -ge 2 ]; do sleep 30; done
done
wait
echo "[batch] ALL DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$RUNLOG"
