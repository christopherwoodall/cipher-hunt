#!/usr/bin/env python3
"""GEOMETER WO2 — homophone-cycling test.

Pre-registered in code/side-rotation/prereg_geometer.md BEFORE running.
For F33 islets 06/52/94: reading-class (F33 verified rules, re-derived from
the stream) x (stream position mod 3), Fisher exact MC (200k); combined via
Fisher's method, alpha=0.05. Best-case p per group = power ceiling.
Secondary: 78 vs 43 ('me' candidate homophone pair) choice x mod 3.
Writes wo2.json.
"""
import json, os, sys, math, random, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

random.seed(20261007)
OUT = {}

pairs, _, _ = load_pairs_repaired()
N = len(pairs)

def idxs(g):
    return [i for i, p in enumerate(pairs) if p == g]

# ---- F33 reading rules, re-derived from the stream ----
# 06: trigram-internal 'ent' iff pairs[i-4:i+1] == 77 78 94 82 06
i06 = idxs('06')
cls06 = {}
for i in i06:
    tri = (i >= 4 and pairs[i - 4:i + 1] == ['77', '78', '94', '82', '06'])
    cls06[i] = 'ent' if tri else 'stem'
n_ent = sum(1 for v in cls06.values() if v == 'ent')
OUT['r06'] = {'n': len(i06), 'n_ent': n_ent,
              'ent_positions': sorted(i for i, v in cls06.items() if v == 'ent')}
print('06: n=%d ent=%d @%s' % (len(i06), n_ent, OUT['r06']['ent_positions']))

# 94: 'en'-islet iff prev==82 or next==87
i94 = idxs('94')
cls94 = {}
for i in i94:
    isl = (i > 0 and pairs[i - 1] == '82') or (i + 1 < N and pairs[i + 1] == '87')
    cls94[i] = 'en' if isl else 'ne'
n_en = sum(1 for v in cls94.values() if v == 'en')
OUT['r94'] = {'n': len(i94), 'n_en': n_en,
              'en_positions': sorted(i for i, v in cls94.items() if v == 'en')}
print('94: n=%d en=%d @%s' % (len(i94), n_en, OUT['r94']['en_positions']))

# 52: 'pas'-candidate iff a 94 in window [i-6, i-1]
i52 = idxs('52')
cls52 = {}
for i in i52:
    neg = '94' in pairs[max(0, i - 6):i]
    cls52[i] = 'pas' if neg else 'other'
n_pas = sum(1 for v in cls52.values() if v == 'pas')
OUT['r52'] = {'n': len(i52), 'n_pas': n_pas,
              'pas_positions': sorted(i for i, v in cls52.items() if v == 'pas')}
print('52: n=%d pas=%d @%s' % (len(i52), n_pas, OUT['r52']['pas_positions']))

def chi2_2x3(data):
    tab = collections.Counter(data)
    n = len(data)
    rm = collections.Counter(r for r, c in data)
    cm = collections.Counter(c for r, c in data)
    x2 = 0.0
    for r in rm:
        for c in cm:
            o = tab[(r, c)]
            e = rm[r] * cm[c] / n
            if e > 0:
                x2 += (o - e) ** 2 / e
    return x2

def mc_fisher_2x3(data, reps=200000):
    obs = chi2_2x3(data)
    rlabels = [r for r, c in data]
    cslots = [c for r, c in data]
    ge = 0
    for _ in range(reps):
        rl = rlabels[:]
        random.shuffle(rl)
        if chi2_2x3(list(zip(rl, cslots))) >= obs:
            ge += 1
    return (ge + 1) / (reps + 1), obs

def best_case_p(data, minority_label, reps=200000):
    """Power ceiling: all minority-class occurrences in a single mod bin
    (the bin maximizing the statistic), majority distribution unchanged."""
    maj = [(r, c) for r, c in data if r != minority_label]
    nmin = sum(1 for r, c in data if r == minority_label)
    best = None
    for b in (0, 1, 2):
        d2 = maj + [(minority_label, b)] * nmin
        p, x2 = mc_fisher_2x3(d2, reps=reps)
        if best is None or x2 > best[1]:
            best = (p, x2, b)
    return best

results = {}
for name, cls, minlabel in [('06', cls06, 'ent'), ('94', cls94, 'en'), ('52', cls52, 'pas')]:
    data = [(v, i % 3) for i, v in cls.items()]
    p, x2 = mc_fisher_2x3(data)
    bp, bx2, bb = best_case_p(data, minlabel)
    tab = collections.Counter(data)
    results[name] = {
        'p': round(p, 5), 'chi2': round(x2, 3),
        'table': {str((r, c)): tab[(r, c)] for r in sorted(set(r for r, c in data)) for c in (0, 1, 2)},
        'best_case_p': round(bp, 5), 'best_case_bin': bb,
        'vacuous': bool(bp >= 0.05),
    }
    print('%s: p=%.5f chi2=%.2f best-case p=%.5f (bin %d) %s' %
          (name, p, x2, bp, bb, 'VACUOUS' if bp >= 0.05 else ''))
OUT['primary'] = results

# Fisher's method combine (only non-vacuous groups contribute meaningfully;
# combine all three as pre-registered, report both)
ps = [results[g]['p'] for g in ('06', '94', '52')]
X = -2.0 * sum(math.log(p) for p in ps)
# chi2 sf with 6 df
def chi2_sf(x, df):
    # regularized upper gamma via series/continued fraction (Numerical Recipes)
    if x <= 0:
        return 1.0
    a = df / 2.0
    if x < a + 1.0:
        # series for P(a,x), return 1-P
        ap = a
        s = 1.0 / a
        d = s
        for _ in range(500):
            ap += 1
            d *= x / ap
            s += d
            if abs(d) < abs(s) * 1e-12:
                break
        return 1.0 - s * math.exp(-x + a * math.log(x) - math.lgamma(a))
    else:
        # continued fraction for Q(a,x)
        b = x + 1.0 - a
        c = 1e300
        d = 1.0 / b
        h = d
        for i in range(1, 500):
            an = -i * (i - a)
            b += 2.0
            d = an * d + b
            if abs(d) < 1e-300:
                d = 1e-300
            c = b + an / c
            if abs(c) < 1e-300:
                c = 1e-300
            d = 1.0 / d
            dl = d * c
            h *= dl
            if abs(dl - 1.0) < 1e-12:
                break
        return h * math.exp(-x + a * math.log(x) - math.lgamma(a))
p_comb = chi2_sf(X, 6)
OUT['fisher_combined'] = {'X': round(X, 3), 'df': 6, 'p': round(p_comb, 5)}
print('Fisher combined: X=%.2f p=%.5f' % (X, p_comb))

# ---- secondary: 78 vs 43 'me' homophone-pair choice x mod 3 ----
i78 = idxs('78')
i43 = idxs('43')
data_me = [('78', i % 3) for i in i78] + [('43', i % 3) for i in i43]
p_me, x2_me = mc_fisher_2x3(data_me)
OUT['secondary_78_43'] = {'n78': len(i78), 'n43': len(i43),
                          'p': round(p_me, 5), 'chi2': round(x2_me, 3),
                          'caveat': '43=me is MED-grade; positive = lead only, null = weak'}
print('78/43 choice x mod3: n78=%d n43=%d p=%.5f' % (len(i78), len(i43), p_me))

json.dump(OUT, open(os.path.join(HERE, 'wo2.json'), 'w'), indent=1)
print('combined verdict:', 'SUPPORT' if p_comb < 0.05 else 'NULL')
