#!/bin/bash
# Frozen-code control batch: 6 synthetic instances, 2 parallel streams.
# Run from code/side-homophonic/solver. Uses frozen config.json defaults
# (inventory_mode='crib', restarts=12, iters=40000, seed=1841).
# Outputs tagged with frozen md5s (see ../runs/BATCH-TAG-frozen.md5.json).
cd "$(dirname "$0")" || exit 1
SEEDS="184101 184102 184103 184104 184105 184106"
RUNLOG="../runs/frozen_batch.log"
mkdir -p ../runs
run_one() {
  local seed=$1
  local t0=$(date +%s)
  echo "[frozen-batch] START seed=$seed $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$RUNLOG"
  python3 control_harness.py \
    --ct ../control/instances/SYNTHETIC-ct-${seed}.pairs.txt \
    --truth ../control/instances/SYNTHETIC-key-${seed}.json \
    --crib ../control/instances/SYNTHETIC-crib-${seed}.json \
    --lm lm_ref/lm.json \
    --out ../runs/frozen-ctl-${seed} \
    > ../runs/frozen-ctl-${seed}.stdout.log 2>&1
  local rc=$?
  local t1=$(date +%s)
  echo "[frozen-batch] DONE seed=$seed rc=$rc wall=$((t1-t0))s $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$RUNLOG"
}
for s in $SEEDS; do
  run_one "$s" &
  while [ "$(jobs -r | wc -l)" -ge 2 ]; do sleep 30; done
done
wait
echo "[frozen-batch] ALL DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$RUNLOG"
