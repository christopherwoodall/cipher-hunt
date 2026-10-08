#!/usr/bin/env python3
"""EXPERIMENT 0 (basin probe) — council solver-architecture §2, Track-D v2 revision.

Question: under the rebuilt objective J, is the planted truth a LOCAL OPTIMUM?

Protocol (per ORIGINAL control instance 184101-184106 — all keys already
opened in round-1 forensics; NO fresh-seal contact):
  - build the frozen rebuild solver with the Track-D §5 gate configuration
    (config.json, no_contact=False, inventory_mode='crib', no_soft=True)
  - install the sealed truth key directly (forensics-class read)
  - run the anneal loop for 40k iters STARTING AT THE TRUTH KEY
    (init_key() skipped; everything else identical to Solver.anneal)

Classification (pre-registered here, before seeing results):
  STAY : final key within Hamming distance <= 5 of truth in group space
  SLIDE: final J > J(truth) + 500 nats AND primary recovery < 0.10
  else : DRIFT (report-only; number, not classified)

Output: experiment0.json with per-instance numbers.
Deterministic: build seed 9091+i per instance, logged.
"""
import hashlib
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REBUILD = os.path.join(LANE, 'code', 'side-homophonic-rebuild')
sys.path.insert(0, os.path.join(REBUILD, 'solver'))
from solver import build_solver  # noqa: E402
from phonetics import project  # noqa: E402

SEEDS = ['184101', '184102', '184103', '184104', '184105', '184106']
INST = os.path.join(LANE, 'code', 'side-homophonic', 'control', 'instances')
LM = os.path.join(REBUILD, 'solver', 'lm_ref', 'lm.json')
CFG = json.load(open(os.path.join(REBUILD, 'solver', 'config.json')))
ITERS = 40000


def load_pairs(path):
    pairs = []
    for l in open(path):
        if l.startswith('#') or not l.strip():
            continue
        pairs += l.split()
    return pairs


def apply_truth(solver, anchors, key):
    """Install the sealed truth key exactly as track-d build_candidates.py."""
    for g in solver.groups:
        if g in anchors:
            solver.v1[g] = anchors[g]
            solver.v2[g] = None
            solver.w2[g] = 0.0
        else:
            cells = [key[g]['primary']] + (key[g].get('secondaries') or [])
            for c in cells:
                if c not in solver.pv:
                    solver.pv[c] = project(c)
                    solver.inv.append(c)
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


def anneal_from_current(solver, iters, t0, tmin):
    """Solver.anneal() with init_key() SKIPPED: search starts at the truth key.

    Everything else (move set, cooling schedule, accept rule, best-state
    tracking) is byte-for-byte the same logic.
    """
    cur = solver.total()
    best = cur
    best_state = (dict(solver.v1), dict(solver.v2), dict(solver.w2))
    cool = (tmin / t0) ** (1.0 / iters)
    T, acc, moves = t0, 0, 0
    for it in range(iters):
        g = solver.rng.choice(solver.nonpin)
        delta, snap = solver.propose_move(g)
        if snap is None:
            continue
        moves += 1
        if delta >= 0 or solver.rng.random() < math.exp(delta / T):
            cur += delta
            acc += 1
            if cur > best:
                best = cur
                best_state = (dict(solver.v1), dict(solver.v2),
                              dict(solver.w2))
        else:
            solver.revert(snap)
        T *= cool
    solver.v1, solver.v2, solver.w2 = best_state
    solver._full_refresh()
    return {'best': best, 'acc_rate': acc / max(moves, 1), 'final': solver.total()}


def main():
    out = {'meta': {
        'date': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'config': {k: CFG[k] for k in ('iters', 't0', 'tmin', 'lambda_word',
                                       'lambda_poly', 'lambda_conc', 'beta0',
                                       'conc_cap', 'init', 'inventory_mode')},
        'no_contact': False,
        'seal_note': 'original instances 184101-184106 only; truth keys opened '
                     'in round-1 forensics (CLOSING-VERIFICATION.md:8,139). '
                     'Fresh batch NEVER read; R5005 untouched.',
        'rule': 'STAY: hamming(96 groups) <= 5. SLIDE: final_J > J_truth+500 '
                'AND primary_recovery < 0.10. else DRIFT (report-only).',
    }, 'instances': {}}
    for i, seed in enumerate(SEEDS):
        bseed = 9091 + i  # deterministic, logged
        pairs = load_pairs(os.path.join(INST, f'SYNTHETIC-ct-{seed}.pairs.txt'))
        anchors = json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{seed}.json')))['anchors']
        solver, _, _ = build_solver(
            pairs, anchors, {}, LM, CFG, bseed, no_phase=False, no_word=False,
            no_poly=False, no_soft=True, inventory_mode='crib',
            init=CFG['init'], no_contact=False)
        truth = json.load(open(os.path.join(INST, f'SYNTHETIC-key-{seed}.json')))
        key = truth['key']
        apply_truth(solver, anchors, key)
        J_truth = solver.total()
        truth_primary = {g: key[g]['primary'] for g in solver.groups}
        truth_v1 = dict(solver.v1)

        t0 = time.time()
        a = anneal_from_current(solver, ITERS, CFG['t0'], CFG['tmin'])
        wall = round(time.time() - t0, 1)

        hamming = sum(1 for g in solver.groups if solver.v1[g] != truth_primary[g])
        hamming_nonpin = sum(1 for g in solver.groups
                             if g not in anchors and solver.v1[g] != truth_primary[g])
        n_nonpin = sum(1 for g in solver.groups if g not in anchors)
        primary_recovery = sum(1 for g in solver.groups
                               if g not in anchors and solver.v1[g] == truth_primary[g]) / n_nonpin
        final_J = a['best']
        delta_J = final_J - J_truth

        if hamming <= 5:
            verdict = 'STAY'
        elif delta_J > 500 and primary_recovery < 0.10:
            verdict = 'SLIDE'
        else:
            verdict = 'DRIFT'

        out['instances'][seed] = {
            'build_seed': bseed,
            'J_truth': round(J_truth, 2),
            'final_J': round(final_J, 2),
            'delta_J': round(delta_J, 2),
            'hamming_groups': hamming,
            'hamming_nonpin': hamming_nonpin,
            'n_nonpin': n_nonpin,
            'primary_recovery': round(primary_recovery, 4),
            'acc_rate': round(a['acc_rate'], 4),
            'wall_s': wall,
            'verdict': verdict,
        }
        print(f'{seed}: J_truth={J_truth:.1f} final_J={final_J:.1f} '
              f'dJ={delta_J:+.1f} hamming={hamming}({hamming_nonpin}np) '
              f'rec={primary_recovery:.3f} -> {verdict} ({wall}s)', flush=True)

    path = os.path.join(HERE, 'experiment0.json')
    json.dump(out, open(path, 'w'), indent=1)
    print('wrote', path)


if __name__ == '__main__':
    main()
