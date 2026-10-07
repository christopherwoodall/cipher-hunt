#!/usr/bin/env python3
"""Verify a frozen-ctl-* control_report.json by re-scoring its result.json
with the FROZEN control_harness.score_assignment (sealed truth opened for
scoring only, as the Runner protocol allows). Prints match/mismatch."""
import json, os, sys

SH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(SH, 'solver'))
from control_harness import load_synthetic, score_assignment, _load_truth_robust  # noqa: E402

INST = os.path.join(SH, 'control', 'instances')

for seed in sys.argv[1:]:
    d = os.path.join(SH, 'runs', f'frozen-ctl-{seed}')
    result = json.load(open(os.path.join(d, 'result.json')))
    report = json.load(open(os.path.join(d, 'control_report.json')))
    pairs, meta = load_synthetic(os.path.join(INST, f'SYNTHETIC-ct-{seed}.pairs.txt'))
    anchors = json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{seed}.json')))['anchors']
    truth = _load_truth_robust(os.path.join(INST, f'SYNTHETIC-key-{seed}.json'))
    m = score_assignment(result, truth, pairs, anchors)
    rep = report['metrics']
    keys = ['primary', 'primary_hits', 'proj_equiv', 'secondary', 'mrr',
            'pins_intact', 'n_islets', 'islets_ok', 'n_nonpin']
    ok = all(m[k] == rep[k] for k in keys)
    print(f'seed {seed}: rescore-match={ok}')
    if not ok:
        for k in keys:
            if m[k] != rep[k]:
                print(f'  DIFF {k}: rescore={m[k]} report={rep[k]}')
    print(f'  primary={m["primary"]} secondary={m["secondary"]} proj_equiv={m["proj_equiv"]} mrr={m["mrr"]}')
