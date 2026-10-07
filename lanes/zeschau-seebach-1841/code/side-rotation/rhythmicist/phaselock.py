#!/usr/bin/env python3
"""WO2 -- phase-lock test. Do anchor formulaic phrases lock to the period-3
rhythm? Fresh code; uses the verified canonical phase map (T0 gate must pass
first -- this script asserts it).

Phrases (pre-registered):
  L1 la premiere : 11 70 82 34 29 40 x2
  L2             : 96 87 46 x3
  L3             : 24 87 64 x3
  L4             : 77 78 94 82 06 x2
  L5             : 64 96 43 87 01 x2
  L6 9-mer       : 56 69 26 00 33 21 64 37 01 x2

Tests (pre-registered, alpha=0.05):
  A: pooled 14 starts, chi2 GOF vs token phase marginals (df=3).
  B: per-set P(all n starts same phase) = sum_i p_i^n (descriptive).
  C: L1 exact 6-sequence lock; chance = (sum_i p_i^2)^6.
"""
import json
import math
import os
import sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

PHRASES = {
    'L1_la_premiere': ['11', '70', '82', '34', '29', '40'],
    'L2_96_87_46': ['96', '87', '46'],
    'L3_24_87_64': ['24', '87', '64'],
    'L4_77_78_94_82_06': ['77', '78', '94', '82', '06'],
    'L5_64_96_43_87_01': ['64', '96', '43', '87', '01'],
    'L6_9mer': ['56', '69', '26', '00', '33', '21', '64', '37', '01'],
}


def find_all(pairs, pat):
    n, m = len(pairs), len(pat)
    return [i for i in range(n - m + 1) if pairs[i:i + m] == pat]


def main():
    pairs = load_pairs_repaired()[0]
    labels = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                         'phase_map_repaired.json')))
    seq = [labels[g] for g in pairs]
    states = ['A', 'B', 'C', 'R']
    pi = {s: seq.count(s) / len(seq) for s in states}
    print('phase token marginals:', {s: round(pi[s], 4) for s in states})
    p_same_start = sum(pi[s] ** 2 for s in states)
    print('P(two draws same phase) = sum p_i^2 = %.4f' % p_same_start)

    occ = {}
    for name, pat in PHRASES.items():
        pos = find_all(pairs, pat)
        occ[name] = pos
        starts = [seq[i] for i in pos]
        phstr = [seq[i:i + len(pat)] for i in pos]
        allsame = len(set(starts)) == 1
        p_allsame = sum(pi[s] ** len(pos) for s in states)
        print('%s x%d @%s starts=%s all-same=%s P(all-same|H0)=%.4f'
              % (name, len(pos), pos, starts, allsame, p_allsame))
        for k, (p_, hs) in enumerate(zip(pos, phstr)):
            print('    occ%d @%d: %s' % (k, p_, ''.join(hs)))

    # Test A: pooled chi2 GOF
    starts_all = [seq[i] for pos in occ.values() for i in pos]
    n = len(starts_all)
    assert n == 14, n
    obs = [starts_all.count(s) for s in states]
    chi2 = sum((o - n * pi[s]) ** 2 / (n * pi[s]) for o, s in zip(obs, states))
    from scipy.stats import chi2 as chi2_dist
    p = float(chi2_dist.sf(chi2, 3))
    print('Test A pooled: obs=%s chi2=%.3f df=3 p=%.4f -> %s'
          % (obs, chi2, p, 'LOCK' if p < 0.05 else 'no lock (null)'))

    # Test C: L1 exact 6-sequence lock
    l1 = occ['L1_la_premiere']
    assert len(l1) == 2 and l1 == [754, 1034], l1
    s1 = seq[l1[0]:l1[0] + 6]
    s2 = seq[l1[1]:l1[1] + 6]
    exact = (s1 == s2)
    p_exact = p_same_start ** 6
    print('Test C L1 exact 6-phase lock: %s vs %s identical=%s '
          'P(identical|H0)=%.2e' % (''.join(s1), ''.join(s2), exact, p_exact))

    json.dump({'marginals': pi, 'p_same_start': p_same_start,
               'occurrences': {k: v for k, v in occ.items()},
               'starts': {k: [seq[i] for i in v] for k, v in occ.items()},
               'phase_strings': {k: [''.join(seq[i:i + len(PHRASES[k])])
                                     for i in v]
                                 for k, v in occ.items()},
               'testA': {'obs': obs, 'chi2': chi2, 'p': p},
               'testC': {'s1': ''.join(s1), 's2': ''.join(s2),
                         'identical': exact, 'p_chance': p_exact}},
              open('phaselock_results.json', 'w'), indent=1)
    print('wrote phaselock_results.json')


if __name__ == '__main__':
    main()
