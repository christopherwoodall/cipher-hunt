#!/usr/bin/env python3
"""WO2 salvage -- POST-HOC (not pre-registered). The pre-registered Tests A/B/C
are VOID: phase is a deterministic function of group, and exact-repeat phrases
share their start group, so "all occurrences start on the same phase" holds
with probability 1 by construction. This script asks the surviving honest
question: do the 6 DISTINCT formula-initial groups concentrate on phases B/C
beyond what their frequency predicts?

Start groups: 11->B, 96->C, 24->C, 77->C, 64->B, 56->C  (6/6 in {B,C}).
Nulls:
  H1: 6 iid draws uniform over the 96 groups.
  H2: 6 iid draws from token phase marginals.
  H3: frequency-matched permutation -- for each start group draw a random
      group with |rank diff| <= 5; 10k draws; one-sided p for 6/6 in {B,C}.
Also: phase distribution of the top-10/20 frequent groups (frequency
explanation check).
"""
import json
import os
import sys
from collections import Counter

import numpy as np

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

START_GROUPS = ['11', '96', '24', '77', '64', '56']


def main():
    pairs = load_pairs_repaired()[0]
    labels = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                         'phase_map_repaired.json')))
    groups = sorted(set(pairs))
    freq = Counter(pairs)
    ranked = sorted(groups, key=lambda g: (-freq[g], g))
    rank = {g: i for i, g in enumerate(ranked)}

    start_ph = [labels[g] for g in START_GROUPS]
    print('start groups:', list(zip(START_GROUPS, start_ph,
                                    [freq[g] for g in START_GROUPS])))
    k_bc = sum(1 for p in start_ph if p in 'BC')
    print('distinct starts in {B,C}: %d/6' % k_bc)

    # H1: uniform over groups
    nBC_groups = sum(1 for g in groups if labels[g] in 'BC')
    p1 = (nBC_groups / len(groups)) ** 6
    print('H1 uniform-group: P(6/6 in {B,C}) = (%.3f)^6 = %.4f'
          % (nBC_groups / len(groups), p1))

    # H2: token marginals
    seq = [labels[g] for g in pairs]
    pBC_tok = sum(1 for s in seq if s in 'BC') / len(seq)
    p2 = pBC_tok ** 6
    print('H2 token-marginal: P(6/6 in {B,C}) = (%.4f)^6 = %.4f'
          % (pBC_tok, p2))

    # H3: frequency-matched permutation
    rng = np.random.default_rng(20261007)
    cands = {g: [h for h in groups if abs(rank[h] - rank[g]) <= 5]
             for g in START_GROUPS}
    hits = 0
    N = 10000
    for _ in range(N):
        draw = [rng.choice(cands[g]) for g in START_GROUPS]
        if all(labels[h] in 'BC' for h in draw):
            hits += 1
    print('H3 freq-matched: %d/10000 draws all in {B,C} -> p=%.4f'
          % (hits, hits / N))

    # frequency explanation: top-k phase distribution
    for k in (10, 20):
        top = ranked[:k]
        d = Counter(labels[g] for g in top)
        print('top-%d phase distribution:' % k, dict(d))

    json.dump({'start_groups': START_GROUPS, 'start_phases': start_ph,
               'H1_p': p1, 'H2_p': p2, 'H3_p': hits / N,
               'top10': dict(Counter(labels[g] for g in ranked[:10])),
               'top20': dict(Counter(labels[g] for g in ranked[:20]))},
              open('phaselock_posthoc.json', 'w'), indent=1)
    print('wrote phaselock_posthoc.json')


if __name__ == '__main__':
    main()
