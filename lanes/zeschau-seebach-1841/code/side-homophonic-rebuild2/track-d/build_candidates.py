#!/usr/bin/env python3
"""TRACK-D pilot step 0: build the 18 pilot candidates. PILOT ONLY (R7 GO).

Decode plumbing via the track-c build_decodes.py pattern (reviewed, R3).
- truth_<seed>: planted truth from sealed keys 184101-184106. NO new seal:
  all six keys were opened in round-1 forensics
  (verifier/CLOSING-VERIFICATION.md:8,139).
- salad_<seed>: frozen salad-class decode = best.assignment from
  code/side-homophonic/runs/frozen-ctl-<seed>/result.json, taken AS-IS.

Paraphrases (para_<seed>) are written by the operator AFTER this script
runs, frozen into candidates.json with sha256 BEFORE any judge scoring.

Outputs:
  candidates.json  - label -> {text, sha256, len, class, seed, provenance}
                    labels are random 8-hex; class/instance hidden from judge
  label_map.json   - label -> {seed, class}; SEALED until all 54 queries logged
"""
import hashlib
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REBUILD = os.path.join(LANE, 'code', 'side-homophonic-rebuild')
sys.path.insert(0, os.path.join(REBUILD, 'solver'))
from solver import build_solver  # noqa: E402
from phonetics import project  # noqa: E402

SEEDS = ['184101', '184102', '184103', '184104', '184105', '184106']

# Salad source per seed. frozen-ctl-184105/184106 result.json were never saved
# (dirs empty; only stdout logs remain). Substitutes: run3-184105/run3-184106
# = the SAME frozen instrument (side-homophonic/solver.py, lambda_poly=20,
# 12 restarts) on the same seeds — verified degenerate-class (npoly 59/60,
# 28-37 distinct v1 tiling 96 groups). Documented, not cherry-picked.
SALAD_SRC = {
    '184101': 'frozen-ctl-184101',
    '184102': 'frozen-ctl-184102',
    '184103': 'frozen-ctl-184103',
    '184104': 'frozen-ctl-184104',
    '184105': 'run3-184105',  # SUBSTITUTE for missing frozen-ctl-184105/result.json
    '184106': 'run3-184106',  # SUBSTITUTE for missing frozen-ctl-184106/result.json
}
INST = os.path.join(LANE, 'code', 'side-homophonic', 'control', 'instances')
FROZEN_RUNS = os.path.join(LANE, 'code', 'side-homophonic', 'runs')
LM = os.path.join(REBUILD, 'solver', 'lm_ref', 'lm.json')
CFG = json.load(open(os.path.join(REBUILD, 'solver', 'config.json')))


def load_pairs(path):
    pairs = []
    for l in open(path):
        if l.startswith('#') or not l.strip():
            continue
        pairs += l.split()
    return pairs


def fresh_solver(seed):
    pairs = load_pairs(os.path.join(INST, f'SYNTHETIC-ct-{seed}.pairs.txt'))
    anchors = json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{seed}.json')))['anchors']
    solver, _, _ = build_solver(
        pairs, anchors, {}, LM, CFG, 1841, no_phase=False, no_word=False,
        no_poly=False, no_soft=True, inventory_mode='crib',
        init=CFG['init'], no_contact=False)
    return solver, anchors


def apply_key(solver, anchors, key):
    repairs = []
    for g in solver.groups:
        if g in anchors:
            solver.v1[g] = anchors[g]
            solver.v2[g] = None
            solver.w2[g] = 0.0
        else:
            cells = [key[g]['primary']] + (key[g].get('secondaries') or [])
            for c in cells:
                if c not in solver.pv:
                    # D4-miss repair (decode plumbing ONLY): the planted cell
                    # is not in the 296-item Tier-1 inventory. Add it locally
                    # so the truth string can be reconstructed; inventory
                    # weights are unused on the decode path (choose() only
                    # needs pv[]). No scoring happens here.
                    solver.pv[c] = project(c)
                    solver.inv.append(c)
                    repairs.append((g, c))
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
    return ''.join(solver.pcell), repairs


def apply_assignment(solver, anchors, asg):
    for g in solver.groups:
        a = asg[g]
        assert a['v1'] in solver.pv, f'salad v1 {a["v1"]!r} missing'
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
    rng = random.Random(20261007)  # label shuffle only; not a result seed
    cands = {}
    prov = {}
    for seed in SEEDS:
        solver, anchors = fresh_solver(seed)
        # truth (sealed key, forensics-class read)
        truth = json.load(open(os.path.join(INST, f'SYNTHETIC-key-{seed}.json')))
        key = truth['key']
        t, repairs = apply_key(solver, anchors, key)
        if repairs:
            print(f'  D4 repairs ({seed}):', repairs)
        # salad (frozen control best; see SALAD_SRC for the 184105/184106 substitute)
        sdir = SALAD_SRC[seed]
        res = json.load(open(os.path.join(FROZEN_RUNS, sdir, 'result.json')))
        s = apply_assignment(solver, anchors, res['best']['assignment'])
        prov[seed] = {
            'truth_source': f'code/side-homophonic/control/instances/SYNTHETIC-key-{seed}.json (sealed planted truth, forensics-class read; opened round-1)',
            'salad_source': f'code/side-homophonic/runs/{SALAD_SRC[seed]}/result.json best.assignment (frozen solver, lambda_poly=20)' + (' — SUBSTITUTE for missing frozen-ctl-%s/result.json' % seed if SALAD_SRC[seed].startswith('run3') else ''),
            'method': 'rebuild solver build_solver + key/assignment + _rebuild_conc + _full_refresh, decode=join(pcell)',
            'd4_repairs': repairs,
        }
        cands[(seed, 'truth')] = t
        cands[(seed, 'salad')] = s

    labels = {}
    used = set()
    for (seed, cls) in sorted(cands):
        while True:
            lab = '%08x' % rng.randrange(2**32)
            if lab not in used:
                used.add(lab)
                break
        labels[(seed, cls)] = lab

    out = {}
    lmap = {}
    for (seed, cls), lab in labels.items():
        text = cands[(seed, cls)]
        out[lab] = {
            'text': text,
            'sha256': hashlib.sha256(text.encode()).hexdigest(),
            'len': len(text),
        }
        lmap[lab] = {'seed': seed, 'class': cls}
    meta = {
        'provenance': prov,
        'n_candidates': len(out),
        'label_rng_seed': 20261007,
        'note': 'paraphrases (para_<seed>) added by operator post-GO, frozen with sha256 BEFORE any judge scoring; see candidates.json update log',
    }
    json.dump({'meta': meta, 'candidates': out}, open(os.path.join(HERE, 'candidates.json'), 'w'), ensure_ascii=False)
    json.dump(lmap, open(os.path.join(HERE, 'label_map.json'), 'w'), indent=1)
    for (seed, cls) in sorted(cands):
        lab = labels[(seed, cls)]
        print(seed, cls, lab, len(cands[(seed, cls)]),
              hashlib.sha256(cands[(seed, cls)].encode()).hexdigest()[:16])


if __name__ == '__main__':
    main()
