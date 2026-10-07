#!/usr/bin/env python3
"""Self-test the repaired objective: incremental total() must equal full
recompute after every accepted move (letter + word + concentration terms),
and the word-bonus timing must be affordable."""
import os
import sys
import time

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'scorer'))
from models import get_models  # noqa: E402
from objective import (RepairedModel, verify_repaired_incremental,  # noqa: E402
                       PINS, SEED)
import random

print('[selftest] loading models...', flush=True)
M = get_models(verbose=False)
GT = M['GT']
GS = GT['stream']
BLOCK = {g: v['phase'] for g, v in GT['group_info'].items()}
HINTS = GT['hints']

print('[selftest] incremental-exactness check (200 moves, lam_conc on)...',
      flush=True)
ok, info = verify_repaired_incremental(
    GS, BLOCK, M['LP_PROJ'], PINS, HINTS, M['CELLS'], M['WEIGHTS'], M['AC'],
    seed=7, n_moves=200)
print('[selftest] incremental exactness:', 'PASS' if ok else 'FAIL', info,
      flush=True)

print('[selftest] timing _sword_full...', flush=True)
m = RepairedModel(GS, BLOCK, M['LP_PROJ'], PINS, HINTS, M['CELLS'],
                  M['WEIGHTS'], M['AC'], rng=random.Random(SEED))
m.init_key()
t0 = time.time()
for _ in range(20):
    m._sword_full()
dt = (time.time() - t0) / 20
print('[selftest] _sword_full: %.1f ms/call' % (dt * 1000), flush=True)
t0 = time.time()
for _ in range(20):
    m.total()
dt = (time.time() - t0) / 20
print('[selftest] total(): %.1f ms/call' % (dt * 1000), flush=True)
print('[selftest] est. per restart (600 sweeps x 89 groups): %.1f min' % (
    dt * 600 * 89 / 60), flush=True)
