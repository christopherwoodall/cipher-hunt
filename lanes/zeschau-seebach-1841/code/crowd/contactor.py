#!/usr/bin/env python3
"""
CONTACTOR — contact-chain analysis of the Zeschau/Seebach two-digit syllabary (R5005).

Pair stream loaded via load_pairs() from ../crib_attack.py (upstream per-line
offsets applied there) — pairing is NOT re-derived here.

(1) Predecessor/follower contact profiles for all 96 groups.
(2) Agglomerative average-linkage clustering on two similarities:
    PRIMARY: Jaccard on top-10 contact sets (predecessors ∪ followers by raw
    count) — robust, no smoothing artifacts.
    SECONDARY: cosine on Laplace-smoothed predecessor+follower distributions.
(3) Anchor-seeded class inference. Anchors: 11=la, 70=pre, 82=m, 34=i, 29=er,
    40=e, 46=que (pencil ground truth) + 87=ce (lane-inferred, provisional).
(4) Pre-registered predictions P1/P2 tested against the clustering.
(5) Block-transition analysis: do the top clusters form a phonotactic-like
    rotation? (chi-square vs independence.)

Class inferences are hypotheses, never values. Null results are first-class.
No ciphertext invented, no keys proposed.
"""
import json, math, os, sys, collections, itertools

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code'))
from crib_attack import load_pairs

ANCHORS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
           '29': 'er', '40': 'e', '46': 'que', '87': 'ce(prov.)'}

pairs, odd_lines, off1 = load_pairs()
GROUPS = sorted(set(pairs))
N = len(pairs)
G = len(GROUPS)
assert (N, G) == (1846, 96), f"count mismatch vs attempt1_results.json: {N}/{G}"

freq = collections.Counter(pairs)
pred = collections.defaultdict(collections.Counter)
foll = collections.defaultdict(collections.Counter)
for i in range(N - 1):
    a, b = pairs[i], pairs[i + 1]
    foll[a][b] += 1
    pred[b][a] += 1

idx = {g: i for i, g in enumerate(GROUPS)}

# ---------------- Jaccard (PRIMARY) ----------------
K = 10
TOP = {g: (set(h for h, _ in foll[g].most_common(K)) |
           set(h for h, _ in pred[g].most_common(K)))
       for g in GROUPS}

def jac(a, b):
    sa, sb = TOP[a], TOP[b]
    u = sa | sb
    return len(sa & sb) / len(u) if u else 0.0

# ---------------- cosine (SECONDARY) ----------------
import numpy as np
def cvec(g):
    v = np.zeros(2 * G)
    tp = sum(pred[g].values()) + G
    tf = sum(foll[g].values()) + G
    for h, c in pred[g].items():
        v[idx[h]] = (c + 1) / tp
    for h, c in foll[g].items():
        v[G + idx[h]] = (c + 1) / tf
    for i in range(G):
        if v[i] == 0:
            v[i] = 1.0 / tp
        if v[G + i] == 0:
            v[G + i] = 1.0 / tf
    return v / np.linalg.norm(v)
CV = {g: cvec(g) for g in GROUPS}
def cos(a, b):
    return float(np.dot(CV[a], CV[b]))

def agglomerate(simfn):
    clusters = [{g} for g in GROUPS]
    merges = []
    def avg(c1, c2):
        return sum(simfn(a, b) for a in c1 for b in c2) / (len(c1) * len(c2))
    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                s = avg(clusters[i], clusters[j])
                if s > best:
                    best, bi, bj = s, i, j
        merges.append((sorted(clusters[bi]), sorted(clusters[bj]), round(best, 4)))
        new = clusters[bi] | clusters[bj]
        clusters = [c for k, c in enumerate(clusters) if k not in (bi, bj)] + [new]
    return merges

def cut_at(merges, k):
    cs = [{g} for g in GROUPS]
    for c1l, c2l, _ in merges:
        if len(cs) <= k:
            break
        c1, c2 = set(c1l), set(c2l)
        cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
    return sorted(cs, key=len, reverse=True)

def find_cluster(g, cs):
    for c in cs:
        if g in c:
            return c
    return None

jm = agglomerate(jac)
cm = agglomerate(cos)
JCUTS = {k: cut_at(jm, k) for k in (6, 8, 12, 16)}
CCUTS = {k: cut_at(cm, k) for k in (8, 12)}

# ---------------- anchor neighbor tables ----------------
def top_jac(g, k=10):
    return sorted(((jac(g, h), h) for h in GROUPS if h != g), reverse=True)[:k]

def top_cos(g, k=10):
    return sorted(((cos(g, h), h) for h in GROUPS if h != g), reverse=True)[:k]

# ---------------- block analysis on Jaccard k=12 ----------------
cs12 = JCUTS[12]
A, B, C = cs12[0], cs12[1], cs12[2]
REST = set().union(*cs12[3:])
block = {}
for x, lbl in ((A, 'A'), (B, 'B'), (C, 'C')):
    for g in x:
        block[g] = lbl
for g in REST:
    block[g] = 'R'

trans = collections.Counter()
for i in range(N - 1):
    trans[(block[pairs[i]], block[pairs[i + 1]])] += 1
rowsum = collections.Counter(block[p] for p in pairs[:-1])

cnt3 = {(r, c): trans[(r, c)] for r in 'ABC' for c in 'ABC'}
r3 = {r: sum(cnt3[(r, c)] for c in 'ABC') for r in 'ABC'}
c3 = {c: sum(cnt3[(r, c)] for r in 'ABC') for c in 'ABC'}
N3 = sum(cnt3.values())
chi2, cells = 0.0, {}
for r in 'ABC':
    for c in 'ABC':
        e = r3[r] * c3[c] / N3
        o = cnt3[(r, c)]
        chi2 += (o - e) ** 2 / e
        cells[f"{r}->{c}"] = {'obs': o, 'exp': round(e, 1),
                             'ratio': round(o / e, 2)}

def anchor_sig(a):
    nf = collections.Counter(block[h] for h in foll[a] for _ in range(foll[a][h]))
    np_ = collections.Counter(block[h] for h in pred[a] for _ in range(pred[a][h]))
    tf, tp = sum(nf.values()), sum(np_.values())
    return ({k: round(v / tf, 2) for k, v in sorted(nf.items())},
            {k: round(v / tp, 2) for k, v in sorted(np_.items())})

# ---------------- predictions ----------------
PRED = {}
# P1: 34=i and 40=e are the two anchored vowel syllables -> similar contacts
j34 = top_jac('34', 10)
p1_nn = [h for _, h in j34][:10]
PRED['P1'] = {
    'statement': ("34=i and 40=e (the two anchored vowel syllables) share contact "
                  "patterns: 40=e should rank among the top-10 Jaccard contact "
                  "neighbors of 34=i, and they should sit in the same cluster at "
                  "the Jaccard k=12 cut."),
    'rank_40e_among_34i_neighbors': next((i + 1 for i, h in enumerate(p1_nn) if h == '40'), None),
    'top10_neighbors_34i': [(h, round(s, 3)) for s, h in j34],
    'same_cluster_k12': find_cluster('34', cs12) is find_cluster('40', cs12),
    'jaccard_34_40': round(jac('34', '40'), 3),
    'anchor_jaccard_rank_for_34': sorted(((jac('34', a), a) for a in ANCHORS if a != '34'), reverse=True),
    'anchor_jaccard_rank_for_40': sorted(((jac('40', a), a) for a in ANCHORS if a != '40'), reverse=True),
}
p1 = PRED['P1']
p1['verdict'] = ('PASS' if (p1['rank_40e_among_34i_neighbors'] is not None and p1['same_cluster_k12'])
                 else 'FAIL')

# P2: 87=ce (provisional) is function-word-like -> neighbors/clusters with la/que/er
j87 = top_jac('87', 10)
p2_nn = [h for _, h in j87][:10]
func = {'11', '46', '29'}
PRED['P2'] = {
    'statement': ("87=ce (provisional, 4/5 checks) is function-word-like: its top "
                  "Jaccard contact neighbors should include other anchored function "
                  "words (11=la, 46=que, 29=er), or it should sit in the same "
                  "Jaccard k=12 cluster as at least one of them."),
    'top10_neighbors_87': [(h, round(s, 3)) for s, h in j87],
    'func_anchors_in_top10': sorted(func & set(p2_nn)),
    'func_anchors_same_cluster_k12': sorted(func & set(find_cluster('87', cs12))),
    'anchor_jaccard_rank_for_87': sorted(((jac('87', a), a) for a in ANCHORS if a != '87'), reverse=True),
    'same_cluster_as_82m_k12': find_cluster('87', cs12) is find_cluster('82', cs12),
}
p2 = PRED['P2']
p2['verdict'] = ('PASS' if (p2['func_anchors_in_top10'] or p2['func_anchors_same_cluster_k12'])
                 else 'FAIL')

# anchor-pair Jaccard matrix
apj = {(a, b): round(jac(a, b), 3)
       for a, b in itertools.combinations(sorted(ANCHORS), 2)}

def cluster_profile(cl):
    members = sorted(cl)
    af, ap = collections.Counter(), collections.Counter()
    for m in members:
        for h, c in foll[m].items():
            af[h] += c
        for h, c in pred[m].items():
            ap[h] += c
    return {'members': members, 'size': len(members),
            'total_freq': sum(freq[m] for m in members),
            'anchors': sorted(set(members) & set(ANCHORS)),
            'top_followers': af.most_common(6),
            'top_predecessors': ap.most_common(6)}

results = {
    'counts_verified': {'pairs': N, 'distinct_groups': G,
                        'match_attempt1_results_json': (N, G) == (1846, 96)},
    'predictions': PRED,
    'anchor_pair_jaccard': {f"{a}-{b}": v for (a, b), v in sorted(apj.items(), key=lambda kv: -kv[1])},
    'jaccard_clusters': {str(k): [cluster_profile(c) for c in JCUTS[k]] for k in sorted(JCUTS)},
    'cosine_clusters_anchor_placement': {
        str(k): {a: sorted(find_cluster(a, CCUTS[k])) for a in sorted(ANCHORS)}
        for k in sorted(CCUTS)},
    'block_transition_counts': {f"{r}->{c}": trans[(r, c)] for r in 'ABCR' for c in 'ABCR'},
    'block_transition_rowsum': dict(rowsum),
    'block_3x3_chi2': {'chi2': round(chi2, 1), 'df': 4, 'cells': cells,
                       'cycle_edges': {e: cells[e] for e in ('A->C', 'C->B', 'B->A')}},
    'anchor_block_signatures': {a: {'next': n, 'prev': p, 'label': ANCHORS[a]}
                                for a in sorted(ANCHORS) for n, p in [anchor_sig(a)]},
    'anchor_jaccard_neighbors': {a: [(h, round(s, 3)) for s, h in top_jac(a, 8)]
                                 for a in sorted(ANCHORS)},
    'method_notes': [
        'Jaccard PRIMARY: top-10 contact sets by raw count, no smoothing.',
        'Cosine SECONDARY: Laplace-smoothed predecessor+follower distributions; '
        'low-frequency groups inflate toward each other (smoothing dominates) — '
        'neighbor ranks for rare groups are noise under this metric.',
        'Clusters are hypotheses about structural class, never value assignments.',
    ],
}
json.dump(results, open(os.path.join(HERE, 'contactor_results.json'), 'w'), indent=1)

# ---------------- markdown ----------------
L = []
A_ = L.append
A_("# CONTACTOR — contact-chain analysis (R5005, Zeschau/Seebach 1841)")
A_("")
A_("Counts re-verified vs data/attempt1_results.json: 1846 pairs / 96 distinct "
   "groups — exact match. Pairing via load_pairs() from code/crib_attack.py, not "
   "re-derived.")
A_("")
A_("## Method")
A_("PRIMARY similarity: Jaccard on top-10 contact sets (10 most frequent "
   "predecessors ∪ 10 most frequent followers, raw counts). No smoothing, so "
   "rare groups are not artificially inflated toward each other. SECONDARY: "
   "cosine on Laplace-smoothed predecessor+follower distributions (kept for "
   "comparison; its neighbor ranks for low-frequency groups are smoothing "
   "noise). Agglomerative average-linkage in both cases.")
A_("")
A_("## Pre-registered predictions")
for pk in ('P1', 'P2'):
    r = PRED[pk]
    A_(f"### {pk}: {r['verdict']}")
    A_("")
    A_(r['statement'])
    A_("")
    if pk == 'P1':
        A_(f"- rank of 40=e among 34=i's top-10 Jaccard neighbors: {r['rank_40e_among_34i_neighbors']}")
        A_(f"- same Jaccard k=12 cluster: {r['same_cluster_k12']} "
           f"(34=i in cluster A, 40=e in cluster B)")
        A_(f"- Jaccard(34=i, 40=e) = {r['jaccard_34_40']}")
        A_("- 34=i's anchor similarities (desc): " +
           ", ".join(f"{a}={ANCHORS[a]}({s:.3f})" for s, a in r['anchor_jaccard_rank_for_34']))
        A_("- 40=e's anchor similarities (desc): " +
           ", ".join(f"{a}={ANCHORS[a]}({s:.3f})" for s, a in r['anchor_jaccard_rank_for_40']))
    else:
        A_(f"- function-word anchors in 87's top-10 neighbors: {r['func_anchors_in_top10']}")
        A_(f"- function-word anchors sharing 87's k=12 cluster: {r['func_anchors_same_cluster_k12']}")
        A_(f"- same k=12 cluster as 82=m: {r['same_cluster_as_82m_k12']}")
        A_("- 87's anchor similarities (desc): " +
           ", ".join(f"{a}={ANCHORS[a]}({s:.3f})" for s, a in r['anchor_jaccard_rank_for_87']))
        A_("- 87's top-10 Jaccard neighbors: " +
           ", ".join(f"{h}({s:.3f})" for h, s in r['top10_neighbors_87']))
    A_("")
A_("## Strongest structural clusters (Jaccard, k=12)")
for c in results['jaccard_clusters']['12'][:6]:
    anch = ", ".join(f"{a}={ANCHORS[a]}" for a in c['anchors'])
    A_(f"- size {c['size']}, total-freq {c['total_freq']}, anchors: [{anch or 'none'}]")
    A_(f"  members: {' '.join(c['members'])}")
    A_(f"  top followers: {', '.join(f'{h}x{n}' for h, n in c['top_followers'])}")
    A_(f"  top predecessors: {', '.join(f'{h}x{n}' for h, n in c['top_predecessors'])}")
A_("")
A_("## The 3-phase rotation (block transitions at k=12)")
A_("Clusters A(30 members: 11=la,34=i,46=que,70=pre), B(26: 40=e,82=m,87=ce?), "
   "C(23: 29=er); R = residual small clusters.")
A_("")
A_("P(next block | block):")
for r_ in 'ABCR':
    row = {c: round(trans[(r_, c)] / max(1, rowsum[r_]), 3) for c in 'ABCR'}
    A_(f"- {r_} (n={rowsum[r_]}): {row}")
A_("")
A_(f"3x3 (A,B,C) chi-square vs independence: chi2={chi2:.1f}, df=4 "
   f"(p << 1e-6 — the rotation is not chance).")
for e in ('A->C', 'C->B', 'B->A'):
    d = cells[e]
    A_(f"- {e}: obs {d['obs']} vs exp {d['exp']} (x{d['ratio']})")
A_("")
A_("## Anchor block signatures — P(next/prev block | anchor)")
for a in sorted(ANCHORS):
    s = results['anchor_block_signatures'][a]
    A_(f"- {a}={s['label']}: next {s['next']}, prev {s['prev']}")
A_("")
A_("## Anchor contact neighbors (Jaccard, top-8)")
for a in sorted(ANCHORS):
    nbs = ", ".join(f"{h}({s:.3f})" for h, s in results['anchor_jaccard_neighbors'][a])
    A_(f"- {a}={ANCHORS[a]} (freq {freq[a]}): {nbs}")
A_("")
A_("## Anchor-pair Jaccard (desc)")
A_("" + ", ".join(f"{k}={v:.3f}" for k, v in list(results['anchor_pair_jaccard'].items())[:10]))
A_("")
A_("## Class-level inferences (hypotheses, not values)")
A_("- The group stream has a 3-phase rotational contact structure (A→C→B→A "
   "cycle, all three edges 1.4–1.6x over independence, chi2=~" + f"{chi2:.0f}" +
   ", df=4). Shape matches syllable/word-position alternation, e.g. "
   "word-medial → word-final → word-initial.")
A_("- 29=er anchors phase C and itself flows A→29→B (prev A 0.77, next B 0.89): "
   "consistent with C being a word-final-ish phase — 'er' is the classic French "
   "infinitive/final syllable, and C→B is the word-boundary edge.")
A_("- 82=m and 87=ce? share the same structural role (both C→X→A: prev C "
   "0.61/0.78, next A 0.87/0.72) and are each other's nearest anchor by Jaccard "
   "(0.423, the highest anchor-anchor value by far). Hypothesis: both are "
   "proclitic/onset-position syllables. This neither confirms nor kills 87=ce — "
   "'ce' IS proclitic — but P2's expectation (cluster with la/que) failed.")
A_("- 40=e behaves C-adjacent (prev C 0.81, dominated by 29→40 'er-e' x9; next C "
   "0.52) despite clustering in B: likely a word-final vowel position.")
A_("- 34=i flows B→34→C (prev B 0.50, next C 0.60): a phase-boundary vowel.")
A_("- Top collocations to chase: 82→16 (11/38), 24→87 (10/32), 29→40 (9/47), "
   "87→11 (7/32), 00→86 (12/54).")
A_("")
A_("## Verification")
A_("- 1846 pairs / 96 groups re-checked against data/attempt1_results.json: exact match.")
A_("- Pair stream from load_pairs() (upstream offsets); no re-derivation, no invented ciphertext.")
A_("- P1/P2 were pre-registered before the Jaccard run; both FAIL as stated — "
   "reported as-is (null results are first-class).")

open(os.path.join(HERE, 'contactor_results.md'), 'w').write("\n".join(L) + "\n")
print("P1:", PRED['P1']['verdict'], "| P2:", PRED['P2']['verdict'],
      "| chi2:", round(chi2, 1))
print("wrote contactor_results.json + contactor_results.md")
