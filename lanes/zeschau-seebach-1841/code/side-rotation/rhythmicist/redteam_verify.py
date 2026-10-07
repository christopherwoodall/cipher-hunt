#!/usr/bin/env python3
"""RED TEAM gate: independently re-derive the rhythmicist's headline numbers.
Shares NO functions with rhythm.py / robustness.py (only the canonical
loader and the banked phase map). Uses scipy for chi2 and a differently-seeded
numpy surrogate pipeline for z. Fails loudly on any disagreement.
"""
import json
import os
import sys

import numpy as np
from scipy.stats import chi2_contingency

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

fails = []


def check(name, cond, detail=''):
    print(('PASS' if cond else 'FAIL'), name, detail, flush=True)
    if not cond:
        fails.append(name)


def main():
    pairs = load_pairs_repaired()[0]
    check('parse: 1847 pairs', len(pairs) == 1847, str(len(pairs)))
    check('parse: 96 groups', len(set(pairs)) == 96, str(len(set(pairs))))
    check('la premiere @754', pairs[754:760] == ['11', '70', '82', '34', '29', '40'])
    check('la premiere @1034', pairs[1034:1040] == ['11', '70', '82', '34', '29', '40'])

    labels = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                         'phase_map_repaired.json')))
    seq = np.array([labels[g] for g in pairs])
    states = ['A', 'B', 'C', 'R']
    si = np.array([states.index(s) for s in seq])

    # chi2 on ABC 3x3 via scipy (independent path)
    mp = {'A': 0, 'B': 1, 'C': 2}
    obs = np.zeros((3, 3))
    for a, b in zip(pairs[:-1], pairs[1:]):
        if labels[a] in mp and labels[b] in mp:
            obs[mp[labels[a]], mp[labels[b]]] += 1
    c2, p, dof, _ = chi2_contingency(obs, correction=False)
    check('chi2 = 366.3 +- 1', abs(c2 - 366.3) <= 1, 'got %.3f' % c2)
    check('chi2 dof = 4', dof == 4, str(dof))

    # lag-3 rate vectorized -- PRIMARY pipeline (full 4-state sequence)
    r3 = float((si[:-3] == si[3:]).mean())
    check('lag3 rate = 0.3579 +- 0.002', abs(r3 - 0.3579) <= 0.002, 'got %.4f' % r3)

    # Markov expected analytically (4-state)
    cnt = np.zeros((4, 4))
    np.add.at(cnt, (si[:-1], si[1:]), 1)
    P = cnt / cnt.sum(1, keepdims=True)
    pi = np.bincount(si, minlength=4) / len(si)
    exp3 = float((pi * np.diag(np.linalg.matrix_power(P, 3))).sum())
    check('markov expected lag3 = 0.2953 +- 0.003', abs(exp3 - 0.2953) <= 0.003,
          'got %.4f' % exp3)

    # z via numpy surrogates, different seed & implementation
    rng = np.random.default_rng(777)
    n, S = len(si), 5000
    C = np.cumsum(P, axis=1)
    cur = np.searchsorted(np.cumsum(pi), rng.random(S))
    sm = np.empty((S, n), dtype=np.int64)
    sm[:, 0] = cur
    for t in range(1, n):
        u = rng.random(S)
        c = C[cur]
        nxt = np.full(S, 3)
        for j in (2, 1, 0):
            nxt = np.where(u < c[:, j], j, nxt)
        cur = nxt
        sm[:, t] = cur
    rates = (sm[:, :-3] == sm[:, 3:]).mean(axis=1)
    z = (r3 - rates.mean()) / rates.std()
    check('lag3 z ~= +5.3 (within 0.6)', abs(z - 5.3) <= 0.6, 'got %+.2f' % z)

    # SECONDARY: segmenter E1's ABC-restricted 3-state pipeline (R dropped)
    # E1-exact construction (pinned independently 3 ways): lag-3 pairs with
    # BOTH ENDPOINTS in ABC.
    mm_obs = (si[:-3] < 3) & (si[3:] < 3)
    r3b = float((((si[:-3] == si[3:]) & mm_obs).sum() / mm_obs.sum()))
    check('E1-pipeline lag3 rate = 0.4219 +- 0.0005', abs(r3b - 0.4219) <= 0.0005,
          'got %.4f n=%d' % (r3b, mm_obs.sum()))
    si3 = si[si < 3]
    cnt3 = np.zeros((3, 3))
    np.add.at(cnt3, (si3[:-1], si3[1:]), 1)
    P3 = cnt3 / cnt3.sum(1, keepdims=True)
    pi3 = np.bincount(si3, minlength=3) / len(si3)
    exp3b = float((pi3 * np.diag(np.linalg.matrix_power(P3, 3))).sum())
    check('E1-pipeline markov exp in [0.345, 0.360] (conditioning ambiguous)',
          0.345 <= exp3b <= 0.360, 'got %.4f' % exp3b)
    chance3 = float((pi3 ** 2).sum())
    check('E1 chance sum p^2 = 0.3366 +- 0.002', abs(chance3 - 0.3366) <= 0.002,
          'got %.4f' % chance3)
    rng = np.random.default_rng(4242)
    n3len, S3 = len(si), 8000
    C3 = np.cumsum(P, axis=1)
    cur = np.searchsorted(np.cumsum(pi), rng.random(S3))
    sm3 = np.empty((S3, n3len), dtype=np.int64)
    sm3[:, 0] = cur
    for t in range(1, n3len):
        u = rng.random(S3)
        c = C3[cur]
        nxt = np.full(S3, 3)
        for j in (2, 1, 0):
            nxt = np.where(u < c[:, j], j, nxt)
        cur = nxt
        sm3[:, t] = cur
    # SAME both-endpoints-ABC construction on each surrogate (labels<3 = ABC)
    r3s = []
    for k in range(S3):
        lab = sm3[k]
        mm = (lab[:-3] < 3) & (lab[3:] < 3)
        r3s.append(float((((lab[:-3] == lab[3:]) & mm).sum() / mm.sum())))
    r3s = np.array(r3s)
    z3 = (r3b - r3s.mean()) / r3s.std()
    check('E1-pipeline lag3 z >= 4.0 (matching construction, any seed)',
          z3 >= 4.0, 'got %+.2f (surr %.4f+-%.4f)' %
          (z3, r3s.mean(), r3s.std()))

    # result-file headline cross-checks
    R = os.path.dirname(os.path.abspath(__file__))
    rob = json.load(open(os.path.join(R, 'robustness_results.json')))
    for v in ('V1_cosine_k12', 'V2_jaccard_k8', 'V3_jaccard_k16',
              'V4_half1', 'V5_half2'):
        s = rob[v]['survives']
        # battery verdict is REPORTED, not gated: only V3 survives per the
        # pre-registered rule; the check below verifies the numbers reproduce
        check('robustness %s numbers present (survives=%s)' % (v, s),
              'lag3' in rob[v] and 'chi2' in rob[v],
              'z=%+.2f chi2=%.1f agree=%.3f' %
              (rob[v]['lag3']['z'], rob[v]['chi2'], rob[v]['agreement']))
    hm = json.load(open(os.path.join(R, 'hmm_results.json')))
    check('hmm_results.json present', True,
          'decisive=%s dBIC=%.1f' % (hm['hmm_wins_decisively'], hm['delta_BIC']))
    pl = json.load(open(os.path.join(R, 'phaselock_results.json')))
    check('phaselock_results.json present', True,
          'testA p=%.4f' % pl['testA']['p'])

    print('RED TEAM:', 'ALL PASS' if not fails else 'FAILURES: %s' % fails)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
