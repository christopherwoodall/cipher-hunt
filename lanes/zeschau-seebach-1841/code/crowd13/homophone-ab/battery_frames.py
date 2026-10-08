#!/usr/bin/env python3
"""HOMOPHONE-SET BATTERY (sets A/B) — Part 2: joint (pre,suc) frame analysis.
Re-derives: joint-frame overlap, characteristic-frame interchangeability
(binomial), Fisher asymmetries, pour-frame successor disjointness.
Per PREREG.md. Stream: repaired 1847-pair.
"""
import sys, os, json
from math import comb
from collections import Counter

LANE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code', 'council', 'drag'))
from common import load_stream

p = load_stream()
N = len(p)
OUT = os.path.join(os.path.dirname(__file__), 'battery_frames.json')

def jframes(g):
    pos = [i for i, x in enumerate(p) if x == g]
    d = Counter()
    for i in pos:
        pre = p[i - 1] if i > 0 else None
        suc = p[i + 1] if i < N - 1 else None
        d[(pre, suc)] += 1
    return pos, d

def binom_cdf_le(k, n, pr):
    return sum(comb(n, x) * (pr ** x) * ((1 - pr) ** (n - x)) for x in range(0, k + 1))

def fisher_depleted(a, b, c, d):
    """table [[a,b],[c,d]]; one-sided p that row1 is depleted in col1."""
    n1 = a + b; n2 = c + d; k = a + c; n = n1 + n2
    return sum(comb(k, x) * comb(n - k, n1 - x) / comb(n, n1) for x in range(0, a + 1))

res = {}
for g1, g2, name in [('33', '86', 'setA'), ('48', '94', 'setB')]:
    pos1, f1 = jframes(g1); pos2, f2 = jframes(g2)
    n1, n2 = len(pos1), len(pos2)
    s1, s2 = set(f1), set(f2)
    shared = s1 & s2
    # characteristic frames: count>=2 in either
    char1 = {k: v for k, v in f1.items() if v >= 2}
    char2 = {k: v for k, v in f2.items() if v >= 2}
    # g2 in g1's char frames
    g2_in_c1 = sum(f2.get(k, 0) for k in char1)
    tot_c1 = sum(char1.values())
    p_g2_in_c1 = binom_cdf_le(g2_in_c1, tot_c1, n2 / (n1 + n2))
    # g1 in g2's char frames
    g1_in_c2 = sum(f1.get(k, 0) for k in char2)
    tot_c2 = sum(char2.values())
    p_g1_in_c2 = binom_cdf_le(g1_in_c2, tot_c2, n1 / (n1 + n2))
    entry = {
        'n1': n1, 'n2': n2,
        'distinct_frames_g1': len(s1), 'distinct_frames_g2': len(s2),
        'shared_frames': [[list(k), f1[k], f2[k]] for k in shared],
        'n_shared': len(shared),
        'frac_disjoint': round(1 - len(shared) / len(s1 | s2), 4),
        'char_frames_g1': {str(k): v for k, v in char1.items()},
        'char_frames_g2': {str(k): v for k, v in char2.items()},
        'g2_in_g1_char': [g2_in_c1, tot_c1, round(p_g2_in_c1, 5)],
        'g1_in_g2_char': [g1_in_c2, tot_c2, round(p_g1_in_c2, 5)],
    }
    # pour-frame (pre==00) successor analysis
    pour_suc1 = Counter(p[i + 1] for i in pos1 if p[i - 1] == '00')
    pour_suc2 = Counter(p[i + 1] for i in pos2 if p[i - 1] == '00')
    entry['pour_successors_g1'] = dict(pour_suc1)
    entry['pour_successors_g2'] = dict(pour_suc2)
    entry['pour_suc_overlap'] = sorted(set(pour_suc1) & set(pour_suc2))
    # 29-completion frames
    c29_1 = [(p[i-1], i) for i in pos1 if p[i+1] == '29']
    c29_2 = [(p[i-1], i) for i in pos2 if p[i+1] == '29']
    entry['completion29_g1'] = c29_1
    entry['completion29_g2'] = c29_2
    res[name] = entry
    print(f"=== {name} {{{g1},{g2}}}")
    print(f"  distinct joint frames: {len(s1)} vs {len(s2)}, shared: {len(shared)} "
          f"({[tuple(k) for k in shared]}), disjoint frac: {entry['frac_disjoint']}")
    print(f"  {g2} in {g1}-char-frames: {g2_in_c1}/{tot_c1} p={p_g2_in_c1:.5f}")
    print(f"  {g1} in {g2}-char-frames: {g1_in_c2}/{tot_c2} p={p_g1_in_c2:.5f}")
    print(f"  pour-suc {g1}: {dict(pour_suc1)}")
    print(f"  pour-suc {g2}: {dict(pour_suc2)}")

# targeted Fisher asymmetries for setA
pos33, _ = jframes('33'); pos86, _ = jframes('86')
n77_33 = sum(1 for i in pos33 if p[i-1] == '77')
n77_86 = sum(1 for i in pos86 if p[i-1] == '77')
res['setA']['fisher_77_33depleted'] = round(fisher_depleted(n77_33, 25-n77_33, n77_86, 32-n77_86), 5)
# pour-suc in {16,79,21}: is 86 depleted?
ps1 = Counter(p[i+1] for i in pos33 if p[i-1]=='00')
ps2 = Counter(p[i+1] for i in pos86 if p[i-1]=='00')
a = sum(ps2.get(s,0) for s in ['16','79','21']); b = 12 - a
c = sum(ps1.get(s,0) for s in ['16','79','21']); d = 8 - c
res['setA']['fisher_poursuc167921_86depleted'] = round(fisher_depleted(a,b,c,d), 5)
print('setA Fisher 77 (33 depleted):', res['setA']['fisher_77_33depleted'])
print('setA Fisher pour-suc{16,79,21} (86 depleted):', res['setA']['fisher_poursuc167921_86depleted'])

json.dump(res, open(OUT, 'w'), indent=1)
print('wrote', OUT)
