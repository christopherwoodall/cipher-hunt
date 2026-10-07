#!/usr/bin/env python3
"""One-shot analysis (rebuild 2026-10-07): WHERE does the degenerate key's
S_cov come from? Dumps hit-level and value-level anatomy for the degenerate
vs truth decodes under the new per-char best-hit scorer.
"""
import collections
import json
import os
import sys

REBUILD = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LANE = os.path.abspath(os.path.join(REBUILD, '..', '..', '..'))
sys.path.insert(0, REBUILD)
from solver import build_solver, AhoCorasick  # noqa: E402
from phonetics import project as _proj  # noqa: E402

SEED = '184101'
INST = os.path.join(LANE, 'code', 'side-homophonic', 'control', 'instances')
RUNS = os.path.join(LANE, 'code', 'side-homophonic', 'runs')


def load_pairs(path):
    pairs = []
    for l in open(path):
        if l.startswith('#') or not l.strip():
            continue
        pairs += l.split()
    return pairs


def install(solver, asg):
    for g in solver.groups:
        a = asg[g]
        solver.v1[g] = a['v1']
        solver.v2[g] = a['v2']
        solver.w2[g] = a['w2']
    solver._rebuild_conc()
    solver._full_refresh()


def hit_anatomy(solver, name, mingate=0):
    s = ''.join(solver.pcell)
    # all hits with positions
    contrib = collections.Counter()   # word -> total w credited via per-char best
    cnt = collections.Counter()
    # per-char best attribution: for each char, which hit won (gated)
    lo_hits = list(solver.ac.scan_hits(s))
    n = len(s)
    bestv = [0.0] * n
    bestw = [None] * n
    for a, b, w in lo_hits:
        if b - a < mingate:
            continue
        v = w / (b - a)
        for c in range(a, b):
            if v > bestv[c]:
                bestv[c] = v
                bestw[c] = s[a:b]
    for c in range(n):
        if bestw[c]:
            contrib[bestw[c]] += bestv[c]
            cnt[bestw[c]] += 1
    tot = sum(contrib.values())
    print(f'--- {name} (mingate={mingate}): S_cov~{tot:.1f} '
          f'chars={n} distinct_winning_words={len(contrib)}')
    print(f'    top 25 winning words by attributed weight:')
    for w_, tw in contrib.most_common(25):
        print(f'      {w_!r:20s} len={len(w_):2d} attr_w={tw:8.1f} '
              f'char_hits={cnt[w_]:5d}')
    # value anatomy
    vc = collections.Counter(solver.v1[g] for g in solver.groups)
    print(f'    top 15 values by #groups:')
    for v, k in vc.most_common(15):
        print(f'      {v!r:12s} proj={solver.pv[v]!r:12s} groups={k}')
    # how much of S_cov comes from hits of each length
    bylen = collections.Counter()
    for w_, tw in contrib.items():
        bylen[len(w_)] += tw
    print(f'    attributed weight by hit length: {dict(sorted(bylen.items()))}')


def main():
    pairs = load_pairs(os.path.join(INST, f'SYNTHETIC-ct-{SEED}.pairs.txt'))
    anchors = json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{SEED}.json')))['anchors']
    truth = json.load(open(os.path.join(INST, f'SYNTHETIC-key-{SEED}.json')))
    cfg = json.load(open(os.path.join(REBUILD, 'config.json')))
    solver, lm_data, phase_info = build_solver(
        pairs, anchors, {}, os.path.join(REBUILD, 'lm_ref', 'lm.json'),
        cfg, 1841, no_phase=False, no_word=False, no_poly=False,
        no_soft=True, inventory_mode='crib', init=cfg['init'],
        no_contact=False)
    # degenerate
    res = json.load(open(os.path.join(RUNS, 'run2-184101', 'result.json')))
    install(solver, res['best']['assignment'])
    hit_anatomy(solver, 'DEGENERATE', mingate=6)
    # truth
    key = truth['key']
    asg = {}
    for g in solver.groups:
        if g in anchors:
            asg[g] = {'v1': anchors[g], 'v2': None, 'w2': 0.0}
        else:
            sec = key[g].get('secondaries') or []
            asg[g] = {'v1': key[g]['primary'],
                      'v2': sec[0] if sec else None,
                      'w2': 0.5 if sec else 0.0}
    install(solver, asg)
    hit_anatomy(solver, 'TRUTH')


if __name__ == '__main__':
    main()
