#!/usr/bin/env python3
"""GEOMETER T0 — independent re-derivation gate.

Re-derives Jaccard-k12 phases from scratch (no import of crowd5 instrument),
requires exact equality with code/crowd4/phase_map_repaired.json and
chi2(3x3 ABC) = 366.3 +- 1. Also reconstructs the E1 lag-3 statistic.
Writes t0.json. Exits nonzero if the gate fails.
"""
import json, os, sys, math, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

OUT = {}

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847 and len(set(pairs)) == 96

# ---- Jaccard-k12 agglomerative, from scratch ----
groups = sorted(set(pairs))
foll = collections.defaultdict(collections.Counter)
pred = collections.defaultdict(collections.Counter)
for a, b in zip(pairs, pairs[1:]):
    foll[a][b] += 1
    pred[b][a] += 1
K = 10
TOP = {g: (set(h for h, _ in foll[g].most_common(K)) |
           set(h for h, _ in pred[g].most_common(K))) for g in groups}

def jac(a, b):
    sa, sb = TOP[a], TOP[b]
    u = sa | sb
    return len(sa & sb) / len(u) if u else 0.0

clusters = [{g} for g in groups]
merges = []
while len(clusters) > 1:
    best, bi, bj = -1.0, None, None
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            c1, c2 = clusters[i], clusters[j]
            s = sum(jac(a, b) for a in c1 for b in c2) / (len(c1) * len(c2))
            if s > best:
                best, bi, bj = s, i, j
    merges.append((sorted(clusters[bi]), sorted(clusters[bj])))
    new = clusters[bi] | clusters[bj]
    clusters = [c for k, c in enumerate(clusters) if k not in (bi, bj)] + [new]
cs = [{g} for g in groups]
for c1l, c2l in merges:
    if len(cs) <= 12:
        break
    c1, c2 = set(c1l), set(c2l)
    cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
cs = sorted(cs, key=len, reverse=True)
block = {}
for x, lbl in ((cs[0], 'A'), (cs[1], 'B'), (cs[2], 'C')):
    for g in x:
        block[g] = lbl
for c in cs[3:]:
    for g in c:
        block[g] = 'R'

banked = json.load(open(os.path.join(LANE, 'code', 'crowd4', 'phase_map_repaired.json')))
exact = (block == banked)
OUT['t0_phase_exact_match'] = exact
OUT['t0_phase_sizes'] = {l: sum(1 for g in block.values() if g == l) for l in 'ABCR'}
print('phase exact match:', exact, OUT['t0_phase_sizes'])

# ---- chi2 on 3x3 ABC transitions ----
trans = collections.Counter()
for a, b in zip(pairs, pairs[1:]):
    la, lb = block[a], block[b]
    if la in 'ABC' and lb in 'ABC':
        trans[(la, lb)] += 1
nT = sum(trans.values())
row = collections.Counter(); col = collections.Counter()
for (a, b), c in trans.items():
    row[a] += c; col[b] += c
chi2 = 0.0
for a in 'ABC':
    for b in 'ABC':
        o = trans[(a, b)]
        e = row[a] * col[b] / nT
        chi2 += (o - e) ** 2 / e
OUT['t0_chi2_3x3'] = round(chi2, 2)
OUT['t0_n_trans'] = nT
print('chi2_3x3 =', round(chi2, 2), 'n_trans =', nT)

# ---- E1 reconstruction: lag-k same-phase on 4-state stream ----
lab = [block[p] for p in pairs]
states = 'ABCR'
pi = collections.Counter(lab)
P = {s: collections.Counter() for s in states}
for a, b in zip(lab, lab[1:]):
    P[a][b] += 1
Pm = {s: {t: P[s][t] / pi[s] for t in states} for s in states}
# P^k via dict matmul
def matmul(M1, M2):
    return {s: {t: sum(M1[s][u] * M2[u][t] for u in states) for t in states} for s in states}
Pk = {s: {t: (1.0 if s == t else 0.0) for t in states} for s in states}
lagres = {}
for k in (1, 2, 3, 4, 5, 6):
    Pk = matmul(Pk, Pm)
    exp = sum(pi[s] / N * Pk[s][s] for s in states)
    obs = sum(1 for i in range(N - k) if lab[i] == lab[i + k]) / (N - k)
    se = math.sqrt(exp * (1 - exp) / (N - k))
    z = (obs - exp) / se
    lagres[k] = {'obs': round(obs, 4), 'exp': round(exp, 4), 'z': round(z, 2)}
OUT['t0_lag'] = lagres
for k, r in lagres.items():
    print(f'lag{k}: obs={r["obs"]} exp={r["exp"]} z={r["z"]}')

json.dump(OUT, open(os.path.join(HERE, 't0.json'), 'w'), indent=1)
ok = exact and abs(chi2 - 366.3) <= 1.0
print('T0 GATE:', 'PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
