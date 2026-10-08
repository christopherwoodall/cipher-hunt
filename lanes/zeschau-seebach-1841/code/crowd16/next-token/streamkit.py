#!/usr/bin/env python3
"""Round-16 next-token battery streamkit.
Canonical 1,847-pair stream via lane's own verify_baseline.load_stream.
Position convention: bigram/trigram START indices (0-based, repaired parse).
"""
import json, sys
from collections import Counter
from math import comb
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]  # .../zeschau-seebach-1841
sys.path.insert(0, str(LANE / 'code' / 'crowd6' / 'redteam'))
from verify_baseline import load_stream  # noqa: E402

P = load_stream()
assert len(P) == 1847, len(P)
G = Counter(P)
BIG = Counter(zip(P[:-1], P[1:]))
TRI = Counter(zip(P[:-2], P[1:-1], P[2:]))
QUAD = Counter(zip(P[:-3], P[1:-2], P[2:-1], P[3:]))

def starts(a, b=None, c=None, d=None):
    """Return start indices where sequence a[,b[,c[,d]]] occurs."""
    seq = tuple(x for x in (a, b, c, d) if x is not None)
    n = len(seq)
    return [i for i in range(len(P) - n + 1) if tuple(P[i:i+n]) == seq]

def pre(g):
    return sorted({P[i-1] for i in range(1, len(P)) if P[i] == g})

def suc(g):
    return sorted({P[i+1] for i in range(len(P)-1) if P[i] == g})

def suc_c(g):
    return Counter(P[i+1] for i in range(len(P)-1) if P[i] == g)

def pre_c(g):
    return Counter(P[i-1] for i in range(1, len(P)) if P[i] == g)

def ctx(i, w=4, j=4):
    lo, hi = max(0, i-w), min(len(P), i+j+1)
    return P[lo:hi]

def fisher2x2(a, b, c, d):
    """P(X>=a) one-sided hypergeometric given margins."""
    n = a + b + c + d
    p = 0.0
    for k in range(a, min(a + b, a + c) + 1):
        p += comb(a + c, k) * comb(b + d, a + b - k) / comb(n, a + b)
    return p

# Banked values (post-round-15 red team), for annotation only
BANKED = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que',
          87: 'ce', 64: 'qui', 96: 'par', 17: 'fois', 84: 'on(grant-cond)',
          47: 'ce(allophone)', 79: 'tout', 0: 'pour', 59: 'est'}
PROV = {77: 'le', 59: 'est(cond)'}
CLASSES = {31: 'VERBAL', 33: 'INF', 86: 'INF-class'}

def gloss(i):
    g = P[i]
    v = BANKED.get(g) or PROV.get(g) or CLASSES.get(g) or ''
    return f'{g}({v})' if v else str(g)

def ctx_gloss(i, w=3, j=3):
    lo, hi = max(0, i-w), min(len(P), i+j+1)
    return ' '.join(gloss(k) for k in range(lo, hi))

if __name__ == '__main__':
    # smoke
    assert G[0] == 55 and G[84] == 25 and G[17] > 0
    print('streamkit OK: n=1847, groups=96')
