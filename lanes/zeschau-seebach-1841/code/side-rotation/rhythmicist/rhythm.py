#!/usr/bin/env python3
"""RHYTHMICIST core: fresh re-implementation of the contactor's phase-clustering
method + chi2 + lag-k autocorrelation. Written from the published method
description (NOTES.md / rotation_mystery.md spec); shares no code with
code/crowd5/rotation_mystery.py or code/crowd/contactor.py.

Spec implemented (contactor, old parse):
  TOP[g] = top-10 followers (raw count) UNION top-10 predecessors (raw count)
  sim(g,h) = Jaccard(TOP[g], TOP[h])
  agglomerative average-linkage: each round merge the pair of clusters with
    strictly greatest average pairwise similarity (first such pair wins ties);
    merged cluster appended at end of the list.
  cut: replay the recorded merges until exactly k clusters remain.
  labels: 3 largest clusters -> A, B, C (size order); remainder -> R.
"""
import collections
import json
import math
import os
import sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired  # canonical loader only


def load_stream():
    pairs, odd_lines, off1 = load_pairs_repaired()
    return pairs


def contact_maps(pairs):
    foll = collections.defaultdict(collections.Counter)
    pred = collections.defaultdict(collections.Counter)
    for a, b in zip(pairs[:-1], pairs[1:]):
        foll[a][b] += 1
        pred[b][a] += 1
    return foll, pred


def top_sets(pairs, k=10):
    """TOP[g]: top-k followers UNION top-k predecessors by raw count."""
    foll, pred = contact_maps(pairs)
    groups = sorted(set(pairs))
    top = {}
    for g in groups:
        s = set(h for h, _ in foll[g].most_common(k))
        s |= set(h for h, _ in pred[g].most_common(k))
        top[g] = s
    return top, groups


def jaccard(a, b):
    u = a | b
    return len(a & b) / len(u) if u else 0.0


def agglomerate(groups, sim):
    """Average-linkage agglomeration. Returns recorded merge list."""
    clusters = [{g} for g in groups]
    merges = []
    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                c1, c2 = clusters[i], clusters[j]
                s = 0.0
                for a in c1:
                    for b in c2:
                        s += sim(a, b)
                s /= (len(c1) * len(c2))
                if s > best:
                    best, bi, bj = s, i, j
        c1l, c2l = sorted(clusters[bi]), sorted(clusters[bj])
        merges.append((c1l, c2l))
        new = clusters[bi] | clusters[bj]
        clusters = [c for t, c in enumerate(clusters) if t not in (bi, bj)] + [new]
    return merges


def cut_at(groups, merges, k):
    cs = [{g} for g in groups]
    for c1l, c2l in merges:
        if len(cs) <= k:
            break
        c1, c2 = set(c1l), set(c2l)
        cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
    return sorted(cs, key=len, reverse=True)


def derive_phases(pairs, k=12):
    """Jaccard-k12 phase map: {group: 'A'|'B'|'C'|'R'}."""
    top, groups = top_sets(pairs)
    sim = lambda a, b: jaccard(top[a], top[b])
    merges = agglomerate(groups, sim)
    cs = cut_at(groups, merges, k)
    labels = {}
    for name, cl in zip('ABC', cs[:3]):
        for g in cl:
            labels[g] = name
    for cl in cs[3:]:
        for g in cl:
            labels[g] = 'R'
    return labels


def chi2_3x3(pairs, labels):
    """chi2 of independence on the ABC 3x3 consecutive-phase table."""
    obs = [[0] * 3 for _ in range(3)]
    for a, b in zip(pairs[:-1], pairs[1:]):
        la, lb = labels[a], labels[b]
        if la in 'ABC' and lb in 'ABC':
            obs['ABC'.index(la)]['ABC'.index(lb)] += 1
    n = sum(sum(r) for r in obs)
    row = [sum(r) for r in obs]
    col = [sum(obs[r][c] for r in range(3)) for c in range(3)]
    chi2 = 0.0
    for r in range(3):
        for c in range(3):
            e = row[r] * col[c] / n
            chi2 += (obs[r][c] - e) ** 2 / e
    return chi2, obs, n


def phase_sequence(pairs, labels):
    return [labels[g] for g in pairs]


def lag_rates(seq, ks):
    n = len(seq)
    out = {}
    for k in ks:
        same = sum(1 for i in range(n - k) if seq[i] == seq[i + k])
        out[k] = same / (n - k)
    return out


def fit_markov(seq, states):
    """First-order Markov fit over `states`. Returns (P, pi)."""
    idx = {s: i for i, s in enumerate(states)}
    m = len(states)
    cnt = [[0] * m for _ in range(m)]
    for a, b in zip(seq[:-1], seq[1:]):
        cnt[idx[a]][idx[b]] += 1
    P = [[c / sum(row) if sum(row) else 0.0 for c in row] for row in cnt]
    pi = [seq.count(s) / len(seq) for s in states]
    return P, pi


def mat_pow(P, k):
    m = len(P)
    R = [[1.0 if i == j else 0.0 for j in range(m)] for i in range(m)]
    for _ in range(k):
        R = [[sum(R[i][t] * P[t][j] for t in range(m)) for j in range(m)]
             for i in range(m)]
    return R


def markov_lagk_expected(P, pi, k):
    Pk = mat_pow(P, k)
    return sum(pi[i] * Pk[i][i] for i in range(len(P)))


def lag_z(seq, states, k, n_surrogate=10000, seed=20261007):
    """z of observed lag-k same-phase rate vs Markov-null surrogates."""
    import random
    rng = random.Random(seed)
    P, pi = fit_markov(seq, states)
    exp = markov_lagk_expected(P, pi, k)
    obs = lag_rates(seq, [k])[k]
    # cumulative probs for fast sampling
    cum = []
    for row in P:
        c, acc = [], 0.0
        for p in row:
            acc += p
            c.append(acc)
        cum.append(c)
    cum_pi, acc = [], 0.0
    for p in pi:
        acc += p
        cum_pi.append(acc)
    n = len(seq)
    rates = []
    for _ in range(n_surrogate):
        u = rng.random()
        s = next(i for i, c in enumerate(cum_pi) if u <= c)
        seq_s = [s]
        for _ in range(n - 1):
            u = rng.random()
            s = next(i for i, c in enumerate(cum[s]) if u <= c)
            seq_s.append(s)
        same = sum(1 for i in range(n - k) if seq_s[i] == seq_s[i + k])
        rates.append(same / (n - k))
    mean = sum(rates) / len(rates)
    sd = math.sqrt(sum((r - mean) ** 2 for r in rates) / len(rates))
    z = (obs - mean) / sd if sd else 0.0
    return {'obs': obs, 'markov_expected': exp if exp is not None else mean,
            'surr_mean': mean, 'surr_sd': sd, 'z': z}


def main():
    pairs = load_stream()
    assert len(pairs) == 1847 and len(set(pairs)) == 96
    labels = derive_phases(pairs)
    banked = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                         'phase_map_repaired.json')))
    exact = all(labels[g] == banked[g] for g in banked)
    print('phase-map exact match:', exact)
    if not exact:
        diff = [g for g in banked if labels[g] != banked[g]]
        print('diff groups:', diff)
    chi2, obs, n3 = chi2_3x3(pairs, labels)
    print('chi2 ABC 3x3 = %.4f (n=%d)' % (chi2, n3))
    for r in obs:
        print('  ', r)
    seq = phase_sequence(pairs, labels)
    states = ['A', 'B', 'C', 'R']
    pi = [seq.count(s) / len(seq) for s in states]
    print('token marginals:', dict(zip(states, [round(p, 4) for p in pi])))
    print('chance sum p^2 = %.4f' % sum(p * p for p in pi))
    rates = lag_rates(seq, [1, 2, 3, 4, 5, 6])
    print('lag rates:', {k: round(v, 4) for k, v in rates.items()})
    for k in (2, 3):
        r = lag_z(seq, states, k)
        print('lag%d: obs=%.4f markov_exp=%.4f surr=%.4f±%.4f z=%+.2f'
              % (k, r['obs'], r['markov_expected'], r['surr_mean'],
                 r['surr_sd'], r['z']))
    # secondary: segmenter E1's ABC-restricted 3-state pipeline
    seq3 = [s for s in seq if s in 'ABC']
    pi3 = [seq3.count(s) / len(seq3) for s in 'ABC']
    print('ABC-restricted: n=%d chance sum p^2=%.4f'
          % (len(seq3), sum(p * p for p in pi3)))
    for k in (2, 3):
        r = lag_z(seq3, list('ABC'), k)
        print('ABC lag%d: obs=%.4f markov_exp=%.4f surr=%.4f±%.4f z=%+.2f'
              % (k, r['obs'], r['markov_expected'], r['surr_mean'],
                 r['surr_sd'], r['z']))


if __name__ == '__main__':
    main()
