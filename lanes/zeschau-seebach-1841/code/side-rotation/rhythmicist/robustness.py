#!/usr/bin/env python3
"""WO1b -- labeling-robustness battery. Same T0 method, matrix-vectorized
agglomeration (identical tie-breaking: first best pair in cluster-list order
wins) + numpy Markov-surrogate z. Variants:
  V1 cosine metric (contactor-style smoothed 192-dim contact vectors), k=12
  V2 Jaccard, k=8
  V3 Jaccard, k=16
  V4 Jaccard k=12 on pairs[0:923]      (zero-count groups -> R)
  V5 Jaccard k=12 on pairs[923:1847]   (zero-count groups -> R)
Per variant: chi2 on ABC 3x3, lag-3 rate + Markov z (same pipeline as T0).
Survival: chi2 > 30 (df=4) AND z_lag3 >= 3.0 with obs > expected.
"""
import collections
import itertools
import json
import os
import re
import sys

import numpy as np

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired  # canonical loader only


def stream_mats(pairs):
    groups = sorted(set(pairs))
    idx = {g: i for i, g in enumerate(groups)}
    G = len(groups)
    foll = np.zeros((G, G), dtype=float)
    pred = np.zeros((G, G), dtype=float)
    for a, b in zip(pairs[:-1], pairs[1:]):
        foll[idx[a], idx[b]] += 1
        pred[idx[b], idx[a]] += 1
    return groups, idx, foll, pred


def jaccard_sim_matrix(pairs, k=10):
    """TOP[g] = top-k followers UNION top-k predecessors by raw count,
    ties broken by first-occurrence order (Counter.most_common semantics)."""
    foll = collections.defaultdict(collections.Counter)
    pred = collections.defaultdict(collections.Counter)
    for a, b in zip(pairs[:-1], pairs[1:]):
        foll[a][b] += 1
        pred[b][a] += 1
    groups = sorted(set(pairs))
    tops = []
    for g in groups:
        s = set(h for h, _ in foll[g].most_common(k))
        s |= set(h for h, _ in pred[g].most_common(k))
        tops.append(s)
    G = len(groups)
    S = np.zeros((G, G))
    for i in range(G):
        ti = tops[i]
        for j in range(i, G):
            u = ti | tops[j]
            v = len(ti & tops[j]) / len(u) if u else 0.0
            S[i, j] = S[j, i] = v
    return S, groups


def cosine_sim_matrix(pairs):
    """Contactor-style smoothed contact vectors, L2-normalized."""
    groups, idx, foll, pred = stream_mats(pairs)
    G = len(groups)
    V = np.zeros((G, 2 * G))
    for g in range(G):
        v = np.concatenate([(pred[g] + 1) / (pred[g].sum() + G),
                            (foll[g] + 1) / (foll[g].sum() + G)])
        V[g] = v / np.linalg.norm(v)
    return V @ V.T, groups


def agglomerate_matrix(S):
    """Average-linkage on index clusters; first best pair in list order wins."""
    n = S.shape[0]
    clusters = [[i] for i in range(n)]
    merges = []
    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            ci = clusters[i]
            for j in range(i + 1, len(clusters)):
                cj = clusters[j]
                s = S[np.ix_(ci, cj)].mean()
                if s > best:
                    best, bi, bj = s, i, j
        merges.append((sorted(clusters[bi]), sorted(clusters[bj])))
        new = clusters[bi] + clusters[bj]
        clusters = [c for t, c in enumerate(clusters) if t not in (bi, bj)] + [new]
    return merges


def cut_matrix(n, merges, k):
    cs = [[i] for i in range(n)]
    for c1l, c2l in merges:
        if len(cs) <= k:
            break
        s1, s2 = set(c1l), set(c2l)
        cs = [c for c in cs if set(c) != s1 and set(c) != s2] + [c1l + c2l]
    return sorted(cs, key=len, reverse=True)


def labels_from_cut(groups, cs):
    lab = {}
    for name, cl in zip('ABC', cs[:3]):
        for i in cl:
            lab[groups[i]] = name
    for cl in cs[3:]:
        for i in cl:
            lab[groups[i]] = 'R'
    return lab

def chi2_3x3(pairs, labels):
    obs = np.zeros((3, 3))
    mp = {'A': 0, 'B': 1, 'C': 2}
    for a, b in zip(pairs[:-1], pairs[1:]):
        la, lb = labels[a], labels[b]
        if la in mp and lb in mp:
            obs[mp[la], mp[lb]] += 1
    n = obs.sum()
    row, col = obs.sum(1), obs.sum(0)
    exp = np.outer(row, col) / n
    chi2 = ((obs - exp) ** 2 / exp).sum()
    return float(chi2), int(n), obs.tolist()


def markov_z(seq, states, k, n_surrogate=10000, seed=20261007):
    rng = np.random.default_rng(seed)
    idx = {s: i for i, s in enumerate(states)}
    m = len(states)
    cnt = np.zeros((m, m))
    si = np.array([idx[s] for s in seq])
    np.add.at(cnt, (si[:-1], si[1:]), 1)
    P = cnt / cnt.sum(1, keepdims=True)
    pi = np.bincount(si, minlength=m) / len(si)
    Pk = np.linalg.matrix_power(P, k)
    exp = float((pi * np.diag(Pk)).sum())
    n = len(si)
    obs = float((si[:-k] == si[k:]).mean())
    C = np.cumsum(P, axis=1)
    cur = np.searchsorted(np.cumsum(pi), rng.random(n_surrogate))
    sm = np.empty((n_surrogate, n), dtype=np.int64)
    sm[:, 0] = cur
    for t in range(1, n):
        u = rng.random(n_surrogate)
        c = C[cur]
        nxt = np.full(n_surrogate, m - 1)
        for j in range(m - 2, -1, -1):
            nxt = np.where(u < c[:, j], j, nxt)
        cur = nxt
        sm[:, t] = cur
    rates = (sm[:, :-k] == sm[:, k:]).mean(axis=1)
    mean, sd = float(rates.mean()), float(rates.std())
    return {'obs': obs, 'markov_expected': exp, 'surr_mean': mean,
            'surr_sd': sd, 'z': (obs - mean) / sd if sd else 0.0}


def best_perm_agreement(lab_a, lab_b, groups):
    best = 0.0
    for perm in itertools.permutations('ABC'):
        mp = dict(zip(perm, 'ABC'))
        ag = sum(1 for g in groups
                 if (mp[lab_b[g]] if lab_b[g] in 'ABC' else 'R') == lab_a[g]) \
            / len(groups)
        best = max(best, ag)
    return best


def main():
    pairs = load_pairs_repaired()[0]
    canon = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                        'phase_map_repaired.json')))
    groups_all = sorted(set(pairs))
    states = ['A', 'B', 'C', 'R']

    def evaluate(labels, tag):
        seq = [labels[g] for g in pairs]
        seq3 = [s for s in seq if s in 'ABC']
        chi2, n3, tab = chi2_3x3(pairs, labels)
        z3 = markov_z(seq, states, 3)
        z2 = markov_z(seq, states, 2)
        z3b = markov_z(seq3, list('ABC'), 3)  # segmenter E1 pipeline
        ag = best_perm_agreement(canon, labels, groups_all)
        surv = chi2 > 30 and z3['z'] >= 3.0 and z3['obs'] > z3['markov_expected']
        surv_e1 = z3b['z'] >= 3.0 and z3b['obs'] > z3b['markov_expected']
        print('%s: chi2=%.1f (n=%d) lag3 obs=%.4f exp=%.4f z=%+.2f | '
              'E1pipe lag3 obs=%.4f exp=%.4f z=%+.2f | '
              'lag2 z=%+.2f | agree=%.3f | SURVIVE=%s/E1=%s'
              % (tag, chi2, n3, z3['obs'], z3['markov_expected'], z3['z'],
                 z3b['obs'], z3b['markov_expected'], z3b['z'],
                 z2['z'], ag, surv, surv_e1), flush=True)
        return {'chi2': chi2, 'n3': n3, 'tab3x3': tab,
                'lag3': z3, 'lag3_E1pipeline': z3b, 'lag2_z': z2['z'],
                'agreement': ag, 'survives': bool(surv),
                'survives_E1pipeline': bool(surv_e1)}

    results = {}
    S, groups = jaccard_sim_matrix(pairs)
    assert groups == groups_all
    merges = agglomerate_matrix(S)
    cs = cut_matrix(len(groups), merges, 12)
    lab0 = labels_from_cut(groups, cs)
    exact = all(lab0[g] == canon[g] for g in groups)
    print('matrix-pipeline reproduces canonical map exactly:', exact, flush=True)

    Sc, _ = cosine_sim_matrix(pairs)
    lab = labels_from_cut(groups, cut_matrix(len(groups),
                                             agglomerate_matrix(Sc), 12))
    results['V1_cosine_k12'] = evaluate(lab, 'V1 cosine k=12')

    lab = labels_from_cut(groups, cut_matrix(len(groups), merges, 8))
    results['V2_jaccard_k8'] = evaluate(lab, 'V2 jaccard k=8')

    lab = labels_from_cut(groups, cut_matrix(len(groups), merges, 16))
    results['V3_jaccard_k16'] = evaluate(lab, 'V3 jaccard k=16')

    for tag, half in (('V4_half1', pairs[:923]), ('V5_half2', pairs[923:])):
        Sh, gh = jaccard_sim_matrix(half)
        mh = agglomerate_matrix(Sh)
        lab = labels_from_cut(gh, cut_matrix(len(gh), mh, 12))
        present = set(half)
        full_lab = {g: (lab[g] if g in present and g in lab else 'R')
                    for g in groups_all}
        results[tag] = evaluate(full_lab, tag + ' (half n=%d)' % len(half))

    DATA = os.path.join(LANE, 'data')
    old_offsets = json.load(open(os.path.join(DATA, 'upstream-offsets.json')))
    opairs = []
    for line in open(os.path.join(DATA, 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = re.sub(r'\D', '', digits)
        d = digits[old_offsets.get(lid, 0):]
        for i in range(0, len(d) - 1, 2):
            opairs.append(d[i:i + 2])
    print('old-parse pairs:', len(opairs), flush=True)
    So, go = jaccard_sim_matrix(opairs)
    lab_old = labels_from_cut(go, cut_matrix(len(go), agglomerate_matrix(So), 12))
    ag_old = best_perm_agreement(canon, lab_old, groups_all)
    print('old-vs-new label agreement (best perm): %.4f -> %d/96 agree'
          % (ag_old, round(ag_old * 96)), flush=True)
    results['old_vs_new_agreement'] = ag_old

    json.dump(results, open('robustness_results.json', 'w'), indent=1)
    print('wrote robustness_results.json', flush=True)


if __name__ == '__main__':
    main()
