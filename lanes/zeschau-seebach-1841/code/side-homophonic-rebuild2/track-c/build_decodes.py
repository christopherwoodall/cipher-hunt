#!/usr/bin/env python3
"""TRACK-C step 0: reconstruct the two decode strings for the boundary
experiment. DIAGNOSTIC ONLY.

Reads the SEALED 184101 planted truth exactly the way
solver/diag_rescore.py does (never in any scoring/training loop), and the
frozen morpheme-salad winner from pilot/rebuild-pilot-final/result.json.
Writes both decode strings to track-c/decodes.json with provenance
(sha256, head/tail samples), so later scoring steps read them as data.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REBUILD = os.path.join(LANE, 'code', 'side-homophonic-rebuild')
sys.path.insert(0, os.path.join(REBUILD, 'solver'))
from solver import build_solver  # noqa: E402

SEED = '184101'
INST = os.path.join(LANE, 'code', 'side-homophonic', 'control', 'instances')
PILOT = os.path.join(REBUILD, 'pilot', 'rebuild-pilot-final', 'result.json')


def load_pairs(path):
    pairs = []
    for l in open(path):
        if l.startswith('#') or not l.strip():
            continue
        pairs += l.split()
    return pairs


def fresh_solver():
    pairs = load_pairs(os.path.join(INST, f'SYNTHETIC-ct-{SEED}.pairs.txt'))
    anchors = json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{SEED}.json')))['anchors']
    cfg = json.load(open(os.path.join(REBUILD, 'solver', 'config.json')))
    solver, _, _ = build_solver(
        pairs, anchors, {}, os.path.join(REBUILD, 'solver', 'lm_ref', 'lm.json'),
        cfg, 1841, no_phase=False, no_word=False, no_poly=False,
        no_soft=True, inventory_mode='crib', init=cfg['init'], no_contact=False)
    return solver, anchors


def truth_decode():
    truth = json.load(open(os.path.join(INST, f'SYNTHETIC-key-{SEED}.json')))
    key = truth['key']
    solver, anchors = fresh_solver()
    missing = [g for g in key if g not in anchors
               and key[g]['primary'] not in solver.pv]
    assert not missing, f'D4: missing primaries {missing}'
    for g in solver.groups:
        if g in anchors:
            solver.v1[g] = anchors[g]
            solver.v2[g] = None
            solver.w2[g] = 0.0
        else:
            solver.v1[g] = key[g]['primary']
            sec = key[g].get('secondaries') or []
            if sec:
                solver.v2[g] = sec[0]
                solver.w2[g] = 0.5
            else:
                solver.v2[g] = None
                solver.w2[g] = 0.0
    solver.n_poly = sum(1 for g in solver.groups if solver.v2[g] is not None)
    solver._rebuild_conc()
    solver._full_refresh()
    return ''.join(solver.pcell)


def salad_decode():
    res = json.load(open(PILOT))
    asg = res['best']['assignment']
    solver, anchors = fresh_solver()
    for g in solver.groups:
        a = asg[g]
        assert a['v1'] in solver.pv, f'salad v1 {a["v1"]!r} missing from inventory'
        solver.v1[g] = a['v1']
        v2 = a['v2']
        assert v2 is None or v2 in solver.pv
        solver.v2[g] = v2
        solver.w2[g] = a['w2']
    solver.n_poly = sum(1 for g in solver.groups if solver.v2[g] is not None)
    solver._rebuild_conc()
    solver._full_refresh()
    return ''.join(solver.pcell)


def main():
    t = truth_decode()
    s = salad_decode()
    out = {
        'provenance': {
            'seed': SEED,
            'truth_source': 'code/side-homophonic/control/instances/SYNTHETIC-key-184101.json (sealed planted truth, diagnostic read)',
            'salad_source': 'code/side-homophonic-rebuild/pilot/rebuild-pilot-final/result.json (best.assignment)',
            'method': 'rebuild solver build_solver + assignment + _rebuild_conc + _full_refresh, decode = join(pcell)',
        },
        'truth': {
            'len': len(t),
            'sha256': hashlib.sha256(t.encode()).hexdigest(),
            'head': t[:120], 'tail': t[-120:],
        },
        'salad': {
            'len': len(s),
            'sha256': hashlib.sha256(s.encode()).hexdigest(),
            'head': s[:120], 'tail': s[-120:],
        },
    }
    with open(os.path.join(HERE, 'decodes.json'), 'w') as f:
        json.dump({'provenance': out['provenance'],
                   'truth': {**out['truth'], 'text': t},
                   'salad': {**out['salad'], 'text': s}}, f, ensure_ascii=False)
    print(json.dumps(out['truth'], ensure_ascii=False, indent=1)[:400])
    print(json.dumps(out['salad'], ensure_ascii=False, indent=1)[:400])
    # byte-exact sanity: truth decode must match the diag-logged sha prefix
    print('truth sha prefix:', out['truth']['sha256'][:16])


if __name__ == '__main__':
    main()
