#!/usr/bin/env python3
"""diag_k12_top96.py — POST-HOC diagnostic (not pre-registered; not verdict-driving
unless clean). The k=3 cut on 1526 corpus syllables degenerated (1524/1/1) —
the same labeling-degeneracy the Rhythmicist documented. This diagnostic asks
whether the FAITHFUL cipher analog (96 items, k=12 cut, top-3 clusters) gives a
non-degenerate partition on corpus syllables, and if so re-runs ARI vs X.
If it degenerates too, T2 is reported INCONCLUSIVE (instrument limitation)."""
import json, os, sys, collections
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
DATA = os.path.join(LANE, 'data')
rng = __import__('random').Random(20261007)
np.random.seed(20261007)

# reuse defs from recoverability.py without executing its main body
src = open(os.path.join(HERE, 'recoverability.py')).read()
head = src.split("# ---------------- corpus load ----------------")[0]
head = head.replace("HERE = os.path.dirname(os.path.abspath(__file__))", "HERE='.'")
head = head.replace("LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))",
                    "LANE=r'%s'" % LANE)
ns = {}
exec(head, ns)
syllabify, ACC = ns['syllabify'], ns['ACC']
ari = ns['ari']
CANDIDATES = ns['CANDIDATES']

TOC = [os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
       os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')]
words, syls = ns['load_syllables'](TOC)
cnt = collections.Counter(syls)
top96 = [s for s, _ in cnt.most_common(96)]
print("top96 token coverage: %.4f" % (sum(cnt[s] for s in top96) / len(syls)))
inv = top96
n = 96
si = {s: i for i, s in enumerate(inv)}
foll = [collections.Counter() for _ in range(n)]
pred = [collections.Counter() for _ in range(n)]
for a, b in zip(syls, syls[1:]):
    if a in si and b in si:  # contacts restricted to top-96 inventory
        foll[si[a]][si[b]] += 1
        pred[si[b]][si[a]] += 1
TOP = [set(h for h, _ in foll[i].most_common(10)) |
       set(h for h, _ in pred[i].most_common(10)) for i in range(n)]
B = np.zeros((n, n), dtype=np.uint8)
for i, s in enumerate(TOP):
    for j in s:
        if j < n:
            B[i, j] = 1
Bi = B.astype(np.int32)
inter = Bi @ Bi.T
rs = Bi.sum(axis=1).astype(np.int32)
union = rs[:, None] + rs[None, :] - inter
with np.errstate(divide='ignore', invalid='ignore'):
    sim = np.where(union > 0, inter / union, 0.0)
np.fill_diagonal(sim, 1.0)
dist = 1.0 - sim
Z = linkage(squareform(dist, checks=False), method='average')
for kcut in (12, 16, 3):
    cl = fcluster(Z, kcut, criterion='maxclust') - 1
    sizes = sorted(collections.Counter(cl).values(), reverse=True)
    print("k=%d: %d clusters, top sizes %s" % (kcut, len(set(cl)), sizes[:8]))

# ARI diagnostic at k=12: lane analog = top-3 clusters by size -> 3 labels;
# remaining 9 clusters' members assigned to nearest of the 3 by Jaccard sim
# (documented approximation; diagnostic only)
cl12 = fcluster(Z, 12, criterion='maxclust') - 1
by_size = [c for c, _ in collections.Counter(cl12).most_common(3)]
lab = np.full(n, -1)
for i in range(n):
    if cl12[i] in by_size:
        lab[i] = by_size.index(cl12[i])
# assign the rest to nearest top-3 cluster (mean Jaccard sim)
members = {c: [i for i in range(n) if cl12[i] == c] for c in set(cl12)}
for i in range(n):
    if lab[i] == -1:
        best, bj = -1, 0
        for j, c in enumerate(by_size):
            s = np.mean([sim[i, m] for m in members[c]])
            if s > best:
                best, bj = s, j
        lab[i] = bj
print("top-3 cluster sizes:", [int((lab == j).sum()) for j in range(3)])
OUT = {}
for xname, (xfn, states) in CANDIDATES.items():
    true_lab = np.array([states.index(xfn(s)) for s in inv])
    a = ari(true_lab, lab)
    sizes = [int((true_lab == i).sum()) for i in range(3)]
    nulls = []
    for rep in range(200):
        perm = rng.sample(range(n), n)
        rl = np.zeros(n, dtype=int)
        pos = 0
        for ci, sz in enumerate(sizes):
            rl[perm[pos:pos + sz]] = ci
            pos += sz
        nulls.append(ari(rl, lab))
    nulls = np.array(nulls)
    print("%s: ARI=%.4f null_p95=%.4f p_emp=%.4f" %
          (xname, a, np.percentile(nulls, 95), (nulls >= a).mean()))
    OUT[xname] = {'ari_k12': round(float(a), 4),
                  'null_p95': round(float(np.percentile(nulls, 95)), 4),
                  'p_emp': round(float((nulls >= a).mean()), 4)}
json.dump(OUT, open(os.path.join(HERE, 'diag_k12_top96.json'), 'w'), indent=1)
print("wrote diag_k12_top96.json")
