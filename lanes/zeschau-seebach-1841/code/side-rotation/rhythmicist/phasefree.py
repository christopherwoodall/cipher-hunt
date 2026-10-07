#!/usr/bin/env python3
"""POST-HOC (not pre-registered): phase-free test of multi-step memory.
The phase-labeled lag-3 excess could be a labeling artifact. This tests for
3-step memory directly on the raw 96-group stream, no phases involved.

Split (same as WO3): train toks[0:923], test toks[923:1847].
M1 first-order  Markov: P(g[t+1] | g[t]),            Laplace a=1.
M2 second-order Markov: P(g[t+1] | g[t], g[t-1]),    Laplace a=1.
M3 skip-3: predicts g[t+3]: P(g[t+3] | g[t+2], g[t+1]) vs
M4 skip-3+ :            P(g[t+3] | g[t+2], g[t+1], g[t]), Laplace a=1.
Metric: held-out mean loglik per predicted token on test.
M2>M1 => genuine second-order memory. M4>M3 => genuine lag-3 memory,
phase-free. Either would confirm the rhythm is not a labeling artifact.
"""
import json
import os
import sys

import numpy as np

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired


def main():
    pairs = load_pairs_repaired()[0]
    groups = sorted(set(pairs))
    g2i = {g: i for i, g in enumerate(groups)}
    O = len(groups)
    toks = np.array([g2i[g] for g in pairs])
    train, test = toks[:923], toks[923:]

    def laplace(counts, alpha=1.0):
        return (counts + alpha) / (counts.sum(axis=-1, keepdims=True) + alpha * O)

    # M1 bigram
    c1 = np.zeros((O, O))
    np.add.at(c1, (train[:-1], train[1:]), 1)
    P1 = laplace(c1)
    ll1 = float(np.log(P1[test[:-1], test[1:]]).sum() / (len(test) - 1))

    # M2 trigram
    c2 = np.zeros((O, O, O))
    np.add.at(c2, (train[:-2], train[1:-1], train[2:]), 1)
    P2 = laplace(c2)
    ll2 = float(np.log(P2[test[:-2], test[1:-1], test[2:]]).sum() / (len(test) - 2))

    # M1 also evaluated on the same positions as M2 for comparability
    ll1b = float(np.log(P1[test[1:-1], test[2:]]).sum() / (len(test) - 2))

    # M3/M4: predict g[t+3]
    # M3: P(g3 | g2, g1)  -- first-order, shifted (context = the two
    #       immediately preceding tokens)
    c3 = np.zeros((O, O, O))  # c3[prev2, prev1, target]
    np.add.at(c3, (train[:-3], train[1:-2], train[3:]), 1)
    P3 = laplace(c3)
    # M4: P(g3 | g2, g1, g0)
    c4 = np.zeros((O, O, O, O))
    np.add.at(c4, (train[:-3], train[1:-2], train[2:-1], train[3:]), 1)
    P4 = laplace(c4)
    n4 = len(test) - 3
    ll3 = float(np.log(P3[test[:-3], test[1:-2], test[3:]]).sum() / n4)
    ll4 = float(np.log(P4[test[:-3], test[1:-2], test[2:-1], test[3:]]).sum() / n4)

    print('held-out LL/pos: M1 bigram=%.4f | M2 trigram=%.4f (M1@samepos=%.4f)'
          % (ll1, ll2, ll1b))
    print('held-out LL/pos predicting g[t+3]: M3=%.4f | M4(+g[t])=%.4f '
          'delta=%+.4f' % (ll3, ll4, ll4 - ll3))
    print('M2>M1:', ll2 > ll1b, ' M4>M3:', ll4 > ll3)
    json.dump({'M1_bigram': ll1, 'M2_trigram': ll2, 'M1_samepos': ll1b,
               'M3_skip': ll3, 'M4_skip_plus': ll4,
               'M2_wins': bool(ll2 > ll1b), 'M4_wins': bool(ll4 > ll3)},
              open('phasefree_results.json', 'w'), indent=1)
    print('wrote phasefree_results.json')


if __name__ == '__main__':
    main()
