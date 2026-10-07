#!/usr/bin/env python3
"""Round-7 KEY-STRUCTURE analyst: contact-coherent aliasing inversion.

Proposes homophone sets via phase-conditioned contact profiles and tests
candidate mergers under F33 conditioned-polyvalence rules.

Pipeline:
  1. Load repaired 1,847-pair parse.
  2. Group-level phase labels via the contactor's Jaccard clustering
     (replicated; NOISY instrument per N43(c) -- flagged, never sole basis).
  3. Phase-conditioned contact profiles per group.
  4. Synthetic calibration: own generator-built instances (known key) to
     determine which statistics discriminate true alias pairs from
     spurious pairs, and the direction of merger effects.
  5. Candidate battery on R5005 + F33 tests + ranking.

Work order 6; red team holds kill authority over any merger claim.
"""
import json, math, os, random, sys
from collections import Counter, defaultdict
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(LANE / 'code' / 'side-keyhunt'))
sys.path.insert(0, str(LANE / 'code' / 'side-homophonic' / 'control'))
from repair_parse import load_rows, parse  # noqa: E402

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)


def load_stream():
    rows = load_rows()
    off = json.loads((LANE / 'code/side-keyhunt/repaired_offsets.json').read_text())
    pairs = [int(g) for g, _ in parse(rows, off)]
    assert len(pairs) == 1847, len(pairs)
    return pairs


# ---------------- phase labels (contactor replication, k=3) ----------------
def phase_labels(pairs, k_cut=12, K=10):
    """Jaccard top-K contact sets -> agglomerative avg-linkage -> k_cut cut ->
    3 largest clusters as phases A/B/C, rest R. Returns dict group->phase and
    the block-transition 3x3 chi2 (noisy detector, N43(b): do not lean)."""
    groups = sorted(set(pairs))
    N = len(pairs)
    pred = defaultdict(Counter); foll = defaultdict(Counter)
    for a, b in zip(pairs[:-1], pairs[1:]):
        foll[a][b] += 1; pred[b][a] += 1
    top = {g: (set(h for h, _ in foll[g].most_common(K)) |
               set(h for h, _ in pred[g].most_common(K))) for g in groups}

    def jac(a, b):
        sa, sb = top[a], top[b]
        u = sa | sb
        return len(sa & sb) / len(u) if u else 0.0

    clusters = [{g} for g in groups]
    merges = []

    def avg(c1, c2):
        return sum(jac(a, b) for a in c1 for b in c2) / (len(c1) * len(c2))

    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                s = avg(clusters[i], clusters[j])
                if s > best:
                    best, bi, bj = s, i, j
        merges.append((sorted(clusters[bi]), sorted(clusters[bj])))
        new = clusters[bi] | clusters[bj]
        clusters = [c for k, c in enumerate(clusters) if k not in (bi, bj)] + [new]
    cs = [{g} for g in groups]
    for c1l, c2l in merges:
        if len(cs) <= k_cut:
            break
        c1, c2 = set(c1l), set(c2l)
        cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
    cs = sorted(cs, key=len, reverse=True)
    block = {}
    for x, lbl in zip(cs[:3], 'ABC'):
        for g in x:
            block[g] = lbl
    rest = set().union(*cs[3:]) if len(cs) > 3 else set()
    for g in rest:
        block[g] = 'R'
    trans = Counter()
    for a, b in zip(pairs[:-1], pairs[1:]):
        trans[(block[a], block[b])] += 1
    cnt = {(r, c): trans[(r, c)] for r in 'ABC' for c in 'ABC'}
    r3 = {r: sum(cnt[(r, c)] for c in 'ABC') for r in 'ABC'}
    c3 = {c: sum(cnt[(r, c)] for r in 'ABC') for c in 'ABC'}
    n3 = sum(cnt.values())
    chi2 = sum((cnt[(r, c)] - r3[r] * c3[c] / n3) ** 2 / (r3[r] * c3[c] / n3)
               for r in 'ABC' for c in 'ABC' if r3[r] * c3[c] > 0)
    return block, round(chi2, 1), {'n3': n3, 'cnt': {f'{r}{c}': v for (r, c), v in cnt.items()},
                                  'sizes': {l: sum(1 for g in block.values() if g == l) for l in 'ABCR'}}


def contact_profiles(pairs, block):
    """Per group: succ/pred counters + phase-marginals of contacts."""
    succ = defaultdict(Counter); pred = defaultdict(Counter)
    for a, b in zip(pairs[:-1], pairs[1:]):
        succ[a][b] += 1; pred[b][a] += 1
    prof = {}
    for g in set(pairs):
        s, p = succ[g], pred[g]
        ns, np_ = sum(s.values()), sum(p.values())
        prof[g] = {
            'n': pairs.count(g),
            'succ': dict(s), 'pred': dict(p),
            'succ_phase': {l: sum(c for h, c in s.items() if block.get(h) == l) / ns
                           for l in 'ABCR'} if ns else {},
            'pred_phase': {l: sum(c for h, c in p.items() if block.get(h) == l) / np_
                           for l in 'ABCR'} if np_ else {},
            'phase': block.get(g, 'R'),
        }
    return prof


if __name__ == '__main__' and '--selftest' in sys.argv:
    pairs = load_stream()
    block, chi2, info = phase_labels(pairs)
    print('block chi2 =', chi2, '(noisy; not leaned on)')
    print('cluster sizes:', info['sizes'])
    print('counts:', info['cnt'])
    prof = contact_profiles(pairs, block)
    for g in [87, 47, 77, 0, 45, 78, 29, 1, 59, 37, 16, 34, 43, 21, 6, 86]:
        pr = prof[g]
        print(f"g={g:3d} n={pr['n']:3d} phase={pr['phase']} "
              f"succ_phase={ {l: round(v,2) for l,v in pr['succ_phase'].items() if v>0.01} } "
              f"pred_phase={ {l: round(v,2) for l,v in pr['pred_phase'].items() if v>0.01} }")
