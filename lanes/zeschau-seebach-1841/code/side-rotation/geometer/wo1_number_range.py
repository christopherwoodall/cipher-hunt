#!/usr/bin/env python3
"""GEOMETER WO1 — number-range test (table-geometry smoking gun).

Pre-registered in code/side-rotation/prereg_geometer.md BEFORE running.
WO1a: phase(A/B/C) x number-tertile, Fisher exact MC (200k), alpha=0.05.
WO1b: phase(A/B/C) x (number mod 3), same. Holm over the two.
Robustness: runs test on phase sequence ordered by group number (4 categories).
Decision rule in prereg. Writes wo1.json.
"""
import json, os, sys, math, random, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

random.seed(20261007)
OUT = {}

pairs, _, _ = load_pairs_repaired()
block = json.load(open(os.path.join(LANE, 'code', 'crowd4', 'phase_map_repaired.json')))
groups = sorted(set(pairs), key=int)
assert len(groups) == 96
nums = sorted(int(g) for g in groups)

# tertile cuts from ALL 96 group numbers
c1 = nums[len(nums) // 3]
c2 = nums[2 * len(nums) // 3]
OUT['tertile_cuts'] = [c1, c2]

def tertile(g):
    n = int(g)
    return 0 if n < c1 else (1 if n < c2 else 2)

abc = [g for g in groups if block[g] in 'ABC']
assert len(abc) == 76

def chi2_stat(rows, cols, data):
    # data: list of (r, c); rows/cols: category lists
    tab = collections.Counter(data)
    n = len(data)
    rm = collections.Counter(r for r, c in data)
    cm = collections.Counter(c for r, c in data)
    x2 = 0.0
    for r in rows:
        for c in cols:
            o = tab[(r, c)]
            e = rm[r] * cm[c] / n
            if e > 0:
                x2 += (o - e) ** 2 / e
    return x2

def cramers_v(rows, cols, data):
    x2 = chi2_stat(rows, cols, data)
    n = len(data)
    return math.sqrt(x2 / (n * (min(len(rows), len(cols)) - 1)))

def mc_fisher(rows, cols, data, reps=200000):
    """Monte-Carlo Fisher exact: permute row labels over fixed column slots
    (both margins fixed exactly). Statistic: chi2."""
    obs = chi2_stat(rows, cols, data)
    rlabels = [r for r, c in data]
    cslots = [c for r, c in data]
    ge = 0
    for _ in range(reps):
        rl = rlabels[:]
        random.shuffle(rl)
        if chi2_stat(rows, cols, list(zip(rl, cslots))) >= obs:
            ge += 1
    return (ge + 1) / (reps + 1), obs

def show_table(rows, cols, data):
    tab = collections.Counter(data)
    return [[tab[(r, c)] for c in cols] for r in rows]

# WO1a
data_a = [(block[g], tertile(g)) for g in abc]
p_a, x2_a = mc_fisher(list('ABC'), [0, 1, 2], data_a)
v_a = cramers_v(list('ABC'), [0, 1, 2], data_a)
OUT['WO1a'] = {'p': round(p_a, 5), 'chi2': round(x2_a, 3), 'cramers_v': round(v_a, 4),
               'table': show_table(list('ABC'), [0, 1, 2], data_a),
               'table_note': 'rows A/B/C, cols tertile 0/1/2 (cuts %s)' % OUT['tertile_cuts']}
print('WO1a phase x tertile: p=%.5f chi2=%.2f V=%.3f' % (p_a, x2_a, v_a))
for r, row in zip('ABC', OUT['WO1a']['table']):
    print('  %s: %s' % (r, row))

# WO1b
data_b = [(block[g], int(g) % 3) for g in abc]
p_b, x2_b = mc_fisher(list('ABC'), [0, 1, 2], data_b)
v_b = cramers_v(list('ABC'), [0, 1, 2], data_b)
OUT['WO1b'] = {'p': round(p_b, 5), 'chi2': round(x2_b, 3), 'cramers_v': round(v_b, 4),
               'table': show_table(list('ABC'), [0, 1, 2], data_b),
               'table_note': 'rows A/B/C, cols n-mod-3 = 0/1/2'}
print('WO1b phase x n-mod-3: p=%.5f chi2=%.2f V=%.3f' % (p_b, x2_b, v_b))
for r, row in zip('ABC', OUT['WO1b']['table']):
    print('  %s: %s' % (r, row))

# Holm over {WO1a, WO1b}
ps = sorted([(p_a, 'WO1a'), (p_b, 'WO1b')])
holm = []
m = 2
for rank, (p, name) in enumerate(ps, 1):
    holm.append({'test': name, 'p': round(p, 5),
                 'holm_threshold': round(0.05 / (m - rank + 1), 5),
                 'reject': bool(p < 0.05 / (m - rank + 1))})
OUT['holm'] = holm
print('Holm:', holm)

# Runs robustness: all 96 groups ordered by number, 4 phase categories
seq = [block[g] for g in groups]
runs = 1 + sum(1 for i in range(1, len(seq)) if seq[i] != seq[i - 1])
def n_runs(s):
    return 1 + sum(1 for i in range(1, len(s)) if s[i] != s[i - 1])
labs = seq[:]
le = 0
for _ in range(10000):
    random.shuffle(labs)
    if n_runs(labs) <= runs:
        le += 1
p_runs = (le + 1) / 10001
OUT['runs'] = {'observed_runs': runs, 'p_fewer_or_equal': round(p_runs, 4)}
print('runs test: observed runs=%d p=%.4f' % (runs, p_runs))

# Decision per pre-registered rule
def support(p, v):
    return p < 0.05 and v >= 0.40
OUT['verdict_WO1a'] = 'SUPPORT-candidate' if support(p_a, v_a) else ('weak' if p_a < 0.05 else 'NULL')
OUT['verdict_WO1b'] = 'SUPPORT-candidate' if support(p_b, v_b) else ('weak' if p_b < 0.05 else 'NULL')

json.dump(OUT, open(os.path.join(HERE, 'wo1.json'), 'w'), indent=1)
print('verdicts:', OUT['verdict_WO1a'], '/', OUT['verdict_WO1b'])
