#!/usr/bin/env python3
"""HOMOPHONE-SET BATTERY (sets A/B), round 13 council work order 2.
Part 1: cipher-side statistics — uniformity chi2, Wald-Wolfowitz runs,
predecessor/successor divergence. Per PREREG.md bars.
Stream: repaired 1847-pair via code/council/drag/common.py::load_stream.
"""
import sys, os, json, math
from collections import Counter

LANE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code', 'council', 'drag'))
from common import load_stream

OUT = os.path.join(os.path.dirname(__file__), 'battery_results.json')
p = load_stream()
N = len(p)
assert N == 1847

def chi2_uniform(counts):
    k = len(counts); tot = sum(counts); e = tot / k
    x2 = sum((c - e) ** 2 / e for c in counts)
    # p-value for df = k-1 via regularized gamma
    df = k - 1
    # use math.erfc for df=1, else incomplete gamma approximation
    from math import exp, lgamma
    def gammaincc(a, x):
        # continued fraction for upper incomplete gamma Q(a,x)
        if x <= 0: return 1.0
        if x < a + 1:
            # series for P, then Q = 1-P
            n = 1; ap = a; s = 1.0 / a; d = s
            while abs(d) > 1e-12 * abs(s) and n < 1000:
                ap += 1; d *= x / ap; s += d; n += 1
            P = s * exp(-x + a * math.log(x) - lgamma(a))
            return 1.0 - P
        else:
            b = x + 1 - a; c = 1e300; d = 1.0 / b; h = d; i = 1
            while True:
                an = -i * (i - a); b += 2; d = an * d + b
                if abs(d) < 1e-300: d = 1e-300
                c = b + an / c
                if abs(c) < 1e-300: c = 1e-300
                d = 1.0 / d; delta = d * c; h *= delta
                if abs(delta - 1.0) < 1e-12 or i > 1000: break
                i += 1
            return h * exp(-x + a * math.log(x) - lgamma(a))
    pv = gammaincc(df / 2, x2 / 2)
    return x2, pv

def runs_test(labels):
    """Wald-Wolfowitz. labels: list of 0/1 in order. Returns (R, E, SD, z)."""
    n1 = sum(labels); n2 = len(labels) - n1
    R = 1 + sum(1 for a, b in zip(labels, labels[1:]) if a != b)
    E = 2 * n1 * n2 / (n1 + n2) + 1
    nn = n1 + n2
    var = (2 * n1 * n2 * (2 * n1 * n2 - nn)) / (nn ** 2 * (nn - 1))
    sd = math.sqrt(var)
    z = (R - E) / sd
    return R, E, sd, z, n1, n2

def membership_seq(g1, g2):
    seq = []
    for i, x in enumerate(p):
        if x == g1: seq.append((i, 0))
        elif x == g2: seq.append((i, 1))
    return seq

def divergence(g1, g2, side='pre', min_exp=1.0):
    """Chi-square on P(side|g1) vs P(side|g2). Pools rare categories."""
    pos1 = [i for i, x in enumerate(p) if x == g1]
    pos2 = [i for i, x in enumerate(p) if x == g2]
    def ctx(i):
        if side == 'pre': return p[i - 1] if i > 0 else None
        return p[i + 1] if i < N - 1 else None
    c1 = Counter(ctx(i) for i in pos1)
    c2 = Counter(ctx(i) for i in pos2)
    cats = set(c1) | set(c2)
    # pool categories with small expected counts
    n1, n2 = len(pos1), len(pos2)
    rows = []
    pool1 = pool2 = 0
    for c in cats:
        e1 = (c1[c] + c2[c]) * n1 / (n1 + n2)
        e2 = (c1[c] + c2[c]) * n2 / (n1 + n2)
        if min(e1, e2) < min_exp:
            pool1 += c1[c]; pool2 += c2[c]
        else:
            rows.append((c1[c], c2[c]))
    rows.append((pool1, pool2))
    # chi-square test of homogeneity
    tot1 = sum(r[0] for r in rows); tot2 = sum(r[1] for r in rows)
    x2 = 0.0
    for a, b in rows:
        t = a + b
        if t == 0: continue
        e1 = t * tot1 / (tot1 + tot2); e2 = t * tot2 / (tot1 + tot2)
        if e1 > 0: x2 += (a - e1) ** 2 / e1
        if e2 > 0: x2 += (b - e2) ** 2 / e2
    df = len(rows) - 1
    from math import exp, lgamma
    # reuse gammaincc via chi2_uniform machinery: compute p directly
    def gammaincc(a, x):
        if x <= 0: return 1.0
        if x < a + 1:
            n = 1; ap = a; s = 1.0 / a; d = s
            while abs(d) > 1e-12 * abs(s) and n < 1000:
                ap += 1; d *= x / ap; s += d; n += 1
            P = s * exp(-x + a * math.log(x) - lgamma(a))
            return 1.0 - P
        else:
            b = x + 1 - a; c = 1e300; d = 1.0 / b; h = d; i = 1
            while True:
                an = -i * (i - a); b += 2; d = an * d + b
                if abs(d) < 1e-300: d = 1e-300
                c = b + an / c
                if abs(c) < 1e-300: c = 1e-300
                d = 1.0 / d; delta = d * c; h *= delta
                if abs(delta - 1.0) < 1e-12 or i > 1000: break
                i += 1
            return h * exp(-x + a * math.log(x) - lgamma(a))
    pv = gammaincc(df / 2, x2 / 2)
    return x2, df, pv, dict(c1.most_common()), dict(c2.most_common())

res = {'N': N}
for g1, g2, name in [('33', '86', 'setA'), ('48', '94', 'setB')]:
    c1 = sum(1 for x in p if x == g1); c2 = sum(1 for x in p if x == g2)
    x2u, pu = chi2_uniform([c1, c2])
    seq = membership_seq(g1, g2)
    labels = [s for _, s in seq]
    R, E, sd, z, n1, n2 = runs_test(labels)
    x2pre, dfpre, ppre, pre1, pre2 = divergence(g1, g2, 'pre')
    x2suc, dfsuc, psuc, suc1, suc2 = divergence(g1, g2, 'suc')
    res[name] = {
        'g1': g1, 'n1': c1, 'g2': g2, 'n2': c2,
        'uniformity': {'chi2': round(x2u, 4), 'df': 1, 'p': round(pu, 4)},
        'runs': {'R': R, 'E': round(E, 2), 'sd': round(sd, 2), 'z': round(z, 3),
                 'n1': n1, 'n2': n2, 'positions_g1': [i for i, s in seq if s == 0],
                 'positions_g2': [i for i, s in seq if s == 1]},
        'pre_divergence': {'chi2': round(x2pre, 3), 'df': dfpre, 'p': round(ppre, 5),
                           'dist_g1': pre1, 'dist_g2': pre2},
        'suc_divergence': {'chi2': round(x2suc, 3), 'df': dfsuc, 'p': round(psuc, 5),
                           'dist_g1': suc1, 'dist_g2': suc2},
    }
    print(f"=== {name} {{{g1},{g2}}} n=({c1},{c2})")
    print(f"  uniformity: chi2={x2u:.4f} p={pu:.4f}")
    print(f"  runs: R={R} E={E:.2f} sd={sd:.2f} z={z:.3f}")
    print(f"  pre-divergence: chi2={x2pre:.3f} df={dfpre} p={ppre:.5f}")
    print(f"  suc-divergence: chi2={x2suc:.3f} df={dfsuc} p={psuc:.5f}")

json.dump(res, open(OUT, 'w'), indent=1)
print('wrote', OUT)
