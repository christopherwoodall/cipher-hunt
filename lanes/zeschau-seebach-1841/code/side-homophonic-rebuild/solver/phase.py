#!/usr/bin/env python3
"""Unsupervised contact-structure analysis for the Seebach solver.

Method (copied from the lane's contactor, code/crowd/contactor.py, and the
control generator's unsupervised_chi2 -- same instrument the control is
calibrated against):
  1. For each group: top-10 predecessors | top-10 followers (raw counts).
  2. Jaccard similarity on those contact sets (PRIMARY similarity; no
     smoothing, so rare groups are not inflated toward each other).
  3. Agglomerative average-linkage clustering, cut at k=12 clusters.
  4. The 3 largest clusters -> phases A/B/C; the rest -> R.
  5. 3x3 block-transition chi-square vs independence (df=4).

The rotation A->C->B->A on R5005 measures chi2=181.3 (df=4, p << 1e-6;
code/crowd/contactor_results.md). The synthetic control is calibrated to
chi2 in [181, 320] by the same unsupervised pipeline.

WHAT THE PHASES MEAN (and do not mean)
--------------------------------------
The rotation is real structure, but the tuner (code/crowd3/tuner_results.md)
KILLED the word-position interpretation (phases != initial/medial/final;
red-team M1 VOID, phonetic_rules.md FORBIDDEN #2). This module therefore
makes NO linguistic claim about the phases. It provides two things:
  (a) a data-driven group-similarity graph (Jaccard adjacency): groups with
      interchangeable contact profiles are the natural homophone pool --
      under uniform homophone emission, homophones of one cell have
      statistically identical contacts. This is a claim about TABLE
      STRUCTURE, not about word positions.
  (b) a rotation-strength gate on chi2: the Potts prior weight scales with
      measured rotation strength, so on streams without the rhythm (random-
      mapping controls) the prior shuts itself off.

Recomputed from the INPUT stream every run -- never banked from R5005, so it
works identically on synthetic controls.
"""

import collections
import math


def contact_sets(pairs, k=10):
    groups = sorted(set(pairs))
    pred = collections.defaultdict(collections.Counter)
    foll = collections.defaultdict(collections.Counter)
    for i in range(len(pairs) - 1):
        a, b = pairs[i], pairs[i + 1]
        foll[a][b] += 1
        pred[b][a] += 1
    top = {}
    for g in groups:
        s = set(h for h, _ in foll[g].most_common(k))
        s |= set(h for h, _ in pred[g].most_common(k))
        top[g] = s
    return top


def jaccard_matrix(top):
    groups = sorted(top)
    J = {}
    for i, a in enumerate(groups):
        for b in groups[i + 1:]:
            sa, sb = top[a], top[b]
            u = sa | sb
            j = len(sa & sb) / len(u) if u else 0.0
            if j > 0:
                J[(a, b)] = j
    return J


def reference_chi2(pairs):
    """VERBATIM copy of the control generator's unsupervised_chi2
    (code/side-homophonic/control/generator.py), which itself copies
    code/crowd/contactor.py. The synthetic control is CALIBRATED against this
    exact function (chi2 in [181, 320]), so the solver's gate must use the
    identical instrument. Any 'improvement' here would decouple the gate
    from the calibration. Do not refactor."""
    groups = sorted(set(pairs))
    N = len(pairs)
    freq = collections.Counter(pairs)
    pred = collections.defaultdict(collections.Counter)
    foll = collections.defaultdict(collections.Counter)
    for i in range(N - 1):
        a, b = pairs[i], pairs[i + 1]
        foll[a][b] += 1
        pred[b][a] += 1
    K = 10
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
        if len(cs) <= 12:
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
    trans = collections.Counter()
    for i in range(N - 1):
        trans[(block[pairs[i]], block[pairs[i + 1]])] += 1
    cnt = {(r, c): trans[(r, c)] for r in 'ABC' for c in 'ABC'}
    r3 = {r: sum(cnt[(r, c)] for c in 'ABC') for r in 'ABC'}
    c3 = {c: sum(cnt[(r, c)] for r in 'ABC') for c in 'ABC'}
    n3 = sum(cnt.values())
    chi2 = sum((cnt[(r, c)] - r3[r] * c3[c] / n3) ** 2 / (r3[r] * c3[c] / n3)
               for r in 'ABC' for c in 'ABC' if r3[r] * c3[c] > 0)
    return round(chi2, 1), block


def gate_of(chi2):
    """Rotation-strength switch. Calibrated: uniform-random null streams
    (1846-4000 pairs, 60-96 groups) measure chi2 in [2, 33]; R5005 measures
    181.3 and the synthetic control is calibrated to [181, 320] by the same
    instrument. Midpoint 80, softness 12: null -> <0.02, signal -> >0.999."""
    return 1.0 / (1.0 + math.exp(-(chi2 - 80.0) / 12.0))


def analyze_stream(pairs, jaccard_floor=0.1):
    """Full unsupervised analysis. Returns dict with:
    block: {group: 'A'/'B'/'C'/'R'}, chi2 (reference instrument), gate,
    adj: {group: [(neighbor, jaccard)]} (homophone-pool graph)."""
    groups = sorted(set(pairs))
    chi2, block = reference_chi2(pairs)
    top = contact_sets(pairs)
    J = jaccard_matrix(top)
    adj = collections.defaultdict(list)
    for (a, b), j in J.items():
        if j >= jaccard_floor:
            adj[a].append((b, j))
            adj[b].append((a, j))
    for g in groups:
        adj[g].sort(key=lambda t: -t[1])
    return {
        'block': block,
        'chi2': chi2,
        'gate': round(gate_of(chi2), 4),
        'adj': {g: adj[g] for g in groups},
        'n_groups': len(groups),
    }


if __name__ == '__main__':
    # Smoke tests (mechanics only -- methodology is the control's job):
    #  1. gate math: chi2=181 -> ~1, chi2=25 -> 0.5, chi2=0 -> ~0.04.
    #  2. adjacency: two groups with identical contacts get high Jaccard.
    #  3. the reference chi2 runs end-to-end on a realistic-size stream.
    import random
    assert gate_of(181.3) > 0.999, gate_of(181.3)
    assert gate_of(320.0) > 0.999, gate_of(320.0)
    assert gate_of(33.0) < 0.03, gate_of(33.0)   # null max (measured)
    assert gate_of(0.0) < 0.01, gate_of(0.0)
    print('gate math ok: g(181)=%.4f g(33)=%.4f g(0)=%.4f' %
          (gate_of(181.3), gate_of(33.0), gate_of(0.0)))

    rng = random.Random(7)
    # 96 groups; gA/gB are twins (identical contact distribution by
    # construction: they always appear in the same contexts).
    gs = ['%02d' % i for i in range(96)]
    pairs = []
    for _ in range(4000):
        r = rng.random()
        if r < 0.3:
            pairs.append(rng.choice(['gA', 'gB']))
            pairs.append(rng.choice(gs[:40]))
        else:
            pairs.append(rng.choice(gs))
    pairs = [p if p not in ('gA', 'gB') else p for p in pairs]
    # note: 'gA'/'gB' are extra labels beyond the 96; keep them, they are
    # just two more groups for the contact analysis
    r = analyze_stream(pairs)
    ja = dict(r['adj']['gA'])
    top1 = r['adj']['gA'][0] if r['adj']['gA'] else (None, 0.0)
    print('twin gA: top Jaccard neighbor %s=%.3f (adj size %d), chi2=%s' %
          (top1[0], top1[1], len(r['adj']['gA']), r['chi2']))
    assert top1[0] == 'gB', 'twin should be the top contact neighbor'
    # pure null: uniform random stream -> gate ~0
    pairs0 = [rng.choice(gs) for _ in range(4000)]
    r0 = analyze_stream(pairs0)
    print('null: chi2=%s gate=%s' % (r0['chi2'], r0['gate']))
    assert r0['gate'] < 0.10, 'gate leaks on null stream'
    print('phase smoke test ok')
