#!/usr/bin/env python3
"""01-CLOSER battery (round-8 work order 3): 01="est" allophony vs mutual exclusivity.

Pre-registered at code/crowd8/closer01/PRE-REGISTER.md BEFORE this script ran.
Canonical parse: repaired 1,847-pair stream. Comparator: Nesselrode v8 only.
"""
import json, math, os, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd5', 'redteam'))
from verify_baseline import load_stream
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd7', 'closer'))
from diplomatic_rates import tokenize

OUT = {}

def chi2_p(table):
    """table: list of rows, each a list of counts. Returns (chi2, dof, p)."""
    rows = len(table); cols = len(table[0])
    rtot = [sum(r) for r in table]
    ctot = [sum(table[r][c] for r in range(rows)) for c in range(cols)]
    n = sum(rtot)
    chi2 = 0.0
    for r in range(rows):
        for c in range(cols):
            e = rtot[r] * ctot[c] / n
            if e > 0:
                chi2 += (table[r][c] - e) ** 2 / e
    dof = (rows - 1) * (cols - 1)
    # upper-tail of chi2 via regularized gamma: p = gammainc(dof/2, 0, chi2/2)... use gammaincc
    p = math.gamma(dof / 2) and _gammaincc(dof / 2, chi2 / 2)
    return chi2, dof, p

def _gammaincc(a, x):
    # regularized upper incomplete gamma Q(a,x) via continued fraction / series
    if x <= 0:
        return 1.0
    if x < a + 1:
        # series for P, then Q = 1 - P
        ap, s, d = a, 1.0 / a, 1.0 / a
        n = 1
        while True:
            ap += 1; d *= x / ap; s += d
            if abs(d) < abs(s) * 1e-12 or n > 1000:
                break
            n += 1
        return 1.0 - s * math.exp(-x + a * math.log(x) - math.lgamma(a))
    else:
        b, c, d, h = x + 1 - a, 1e300, 1.0 / (x + 1 - a), 1.0 / (x + 1 - a)
        i = 1
        while True:
            an = -i * (i - a); b += 2
            d = 1.0 / (an * d + b); c = b + an / c
            cd = c * d; h *= cd
            if abs(cd - 1.0) < 1e-12 or i > 1000:
                break
            i += 1
        return h * math.exp(-x + a * math.log(x) - math.lgamma(a))

def fisher_2x2(a, b, c, d):
    """Two-sided Fisher exact via hypergeometric enumeration."""
    n = a + b + c + d
    from math import comb
    def hg(x):
        return comb(a + b, x) * comb(c + d, a + c - x) / comb(n, a + c)
    p_obs = hg(a)
    lo = max(0, (a + c) - (c + d)); hi = min(a + b, a + c)
    return sum(hg(x) for x in range(lo, hi + 1) if hg(x) <= p_obs + 1e-15)

def binom_tail_le(k, n, p):
    return sum(math.comb(n, i) * p**i * (1 - p)**(n - i) for i in range(0, k + 1))

def binom_tail_ge(k, n, p):
    return sum(math.comb(n, i) * p**i * (1 - p)**(n - i) for i in range(k, n + 1))

pairs = load_stream()
assert len(pairs) == 1847
N = len(pairs)
pos01 = [i for i, g in enumerate(pairs) if g == 1]
pos59 = [i for i, g in enumerate(pairs) if g == 59]
n01, n59 = len(pos01), len(pos59)
OUT['n01'], OUT['n59'], OUT['N'] = n01, n59, N

def pre(i):
    return pairs[i - 1] if i > 0 else None

def suc(i):
    return pairs[i + 1] if i < N - 1 else None

# ---------- shared contexts (banked facts re-derived) ----------
pre01 = Counter(pre(i) for i in pos01)
pre59 = Counter(pre(i) for i in pos59)
suc01 = Counter(suc(i) for i in pos01)
suc59 = Counter(suc(i) for i in pos59)
shared_pre = sorted(set(pre01) & set(pre59) - {None})
shared_suc = sorted(set(suc01) & set(suc59) - {None})
OUT['shared_pre'] = shared_pre
OUT['shared_suc'] = shared_suc
OUT['n_shared_pre'], OUT['n_shared_suc'] = len(shared_pre), len(shared_suc)

# ---------- banked value classes ----------
GT = {70, 82, 34, 29, 40}
def pre_class(g):
    if g is None: return 'none'
    if g == 64: return 'qui'
    if g == 94: return 'ne'
    if g == 87: return 'ce'
    if g == 46: return 'que'
    if g == 77: return 'le-prov'
    if g == 11: return 'la'
    if g in GT: return 'GT-letter'
    return 'other'
def suc_class(g):
    if g is None: return 'none'
    if g == 46: return 'que'
    if g == 11: return 'la'
    if g == 77: return 'le-prov'
    if g == 19: return 'g19'
    if g == 24: return 'g24'
    return 'other'

phase_map = json.load(open(os.path.join(LANE, 'code', 'crowd4', 'phase_map_repaired.json')))
def phase_of(g):
    return phase_map.get(f"{g:02d}", 'other') if g is not None else 'none'

# formula spans by content search
def find_spans(pat):
    L = len(pat)
    return [i for i in range(N - L + 1) if pairs[i:i + L] == pat]
formulas = {
    '64-96-43-87-01': find_spans([64, 96, 43, 87, 1]),
    '24-87-64': find_spans([24, 87, 64]),
    '77-78-94-82-06': find_spans([77, 78, 94, 82, 6]),
}
formula_pos = set()
for name, starts in formulas.items():
    L = len(name.split('-'))
    for s in starts:
        formula_pos.update(range(s, s + L))
OUT['formula_starts'] = {k: v for k, v in formulas.items()}

# ---------- C1: six conditioning families ----------
def family_table(level_fn):
    levels = sorted(set(level_fn(i) for i in pos01 + pos59))
    li = {l: k for k, l in enumerate(levels)}
    t01 = [0] * len(levels); t59 = [0] * len(levels)
    for i in pos01: t01[li[level_fn(i)]] += 1
    for i in pos59: t59[li[level_fn(i)]] += 1
    return levels, [t01, t59]

def best_split_accuracy(levels, table):
    # assign each level to 01-side or 59-side by majority; token accuracy per glyph
    t01, t59 = table
    c01 = c59 = 0
    for k in range(len(levels)):
        if t01[k] >= t59[k]:
            c01 += t01[k]
        else:
            c59 += t59[k]
    return c01 / n01, c59 / n59

families = {
    'F1_pre_identity': lambda i: pre(i),
    'F2_pre_class': lambda i: pre_class(pre(i)),
    'F3_suc_class': lambda i: suc_class(suc(i)),
    'F4_pre_phase': lambda i: phase_of(pre(i)),
    'F5_qui_ne_rule': lambda i: 'after_qui_ne' if pre(i) in (64, 94) else 'elsewhere',
    'F6_formula': lambda i: 'in_formula' if i in formula_pos else 'outside',
}
C1 = {}
M = len(families)
for fname, fn in families.items():
    levels, table = family_table(fn)
    # drop all-zero columns
    keep = [k for k in range(len(levels)) if table[0][k] + table[1][k] > 0]
    levels = [levels[k] for k in keep]
    table = [[table[0][k] for k in keep], [table[1][k] for k in keep]]
    if len(levels) < 2:
        C1[fname] = {'note': 'degenerate', 'levels': levels}
        continue
    chi2, dof, p = chi2_p(table)
    p_corr = min(1.0, p * M)
    acc01, acc59 = best_split_accuracy(levels, table)
    # Fisher on the best 2x2 collapse: collapse levels by majority side
    side01 = [k for k in range(len(levels)) if table[0][k] >= table[1][k]]
    a = sum(table[0][k] for k in side01); b = sum(table[1][k] for k in side01)
    c = sum(table[0][k] for k in range(len(levels)) if k not in side01)
    d = sum(table[1][k] for k in range(len(levels)) if k not in side01)
    pf = fisher_2x2(a, b, c, d)
    qualifies = (p_corr < 0.05) and (acc01 >= 0.90) and (acc59 >= 0.90)
    C1[fname] = {
        'levels': levels, 'table_01': table[0], 'table_59': table[1],
        'chi2': round(chi2, 3), 'dof': dof, 'p': p, 'p_bonferroni_m6': p_corr,
        'fisher_best_split_p': pf, 'best_split': [a, b, c, d],
        'acc_01': round(acc01, 4), 'acc_59': round(acc59, 4),
        'qualifies': qualifies,
    }
    # successor-phase diagnostic for F4
    if fname == 'F4_pre_phase':
        lv2, tb2 = family_table(lambda i: phase_of(suc(i)))
        keep2 = [k for k in range(len(lv2)) if tb2[0][k] + tb2[1][k] > 0]
        lv2 = [lv2[k] for k in keep2]; tb2 = [[tb2[0][k] for k in keep2], [tb2[1][k] for k in keep2]]
        if len(lv2) >= 2:
            ch2, df2, p2 = chi2_p(tb2)
            C1[fname]['suc_phase_diagnostic'] = {'levels': lv2, 'table_01': tb2[0],
                'table_59': tb2[1], 'p': p2}
OUT['C1'] = C1
OUT['C1_verdict'] = 'PASS' if any(v.get('qualifies') for v in C1.values()) else 'FAIL'

# ---------- C2: forced est-frames ----------
forced = [(i, pre(i)) for i in pos01 + pos59 if pre(i) in (64, 94)]
n_forced = len(forced)
k01_forced = sum(1 for i, _ in forced if pairs[i] == 1)
k59_forced = n_forced - k01_forced
p59_null = n59 / (n01 + n59)
p_le = binom_tail_le(k01_forced, n_forced, 1 - p59_null)  # P(01-count <= observed)
# fresh-data condition: any NEW forced slot to 01? banked 6/6 all to 59; list positions
OUT['C2'] = {
    'n_forced': n_forced, 'to_01': k01_forced, 'to_59': k59_forced,
    'forced_positions': sorted(i for i, _ in forced),
    'null_p59': round(p59_null, 4),
    'binom_p_01_le_observed': p_le,
    'D2_fires': bool(p_le < 0.05 and k01_forced == 0),
}
# counter-leg: c'est frame
c_est_01 = sum(1 for i in pos01 if pre(i) == 87)
c_est_59 = sum(1 for i in pos59 if pre(i) == 87)
n_ce = c_est_01 + c_est_59
p_ce_01dir = binom_tail_ge(c_est_01, n_ce, n01 / (n01 + n59)) if n_ce else 1.0
OUT['C2_counter_cest'] = {'to_01': c_est_01, 'to_59': c_est_59,
    'binom_p_01_ge_observed': p_ce_01dir,
    'wash': bool(p_ce_01dir >= 0.05)}

# ---------- C3: rival screen on Nesselrode v8 ----------
dr = json.load(open(os.path.join(LANE, 'code', 'crowd7', 'closer', 'diplomatic_rates.json')))
n8 = dr['nesselrode_v8_only']
P_est = n8['P_est']
corpus = open(os.path.join(LANE, 'code', 'side-period', 'corpus', 'nesselrode-v8.txt'),
              encoding='utf-8', errors='replace').read()
toks = tokenize(corpus)
tc = Counter(toks); nt = len(toks)
rivals = {}
for w in ['doute', 'dit', 'fait', 'veut', 'peut', 'ait', 'sont', 'ont']:
    pw = tc[w] / nt
    ratio = (n01 / N) / pw if pw else float('inf')
    rivals[w] = {'n': tc[w], 'P': pw, 'ratio_vs_P01': ratio,
                 'survives_5x': bool(ratio < 5)}
OUT['C3'] = {
    'P01': n01 / N, 'P_est_n8': P_est,
    'est_ratio_vs_P01': (n01 / N) / P_est,
    'rivals': rivals,
    'est_unique_survivor': all(not r['survives_5x'] for r in rivals.values()),
}
# ait-frame interaction
OUT['C3']['frames_46_to_01'] = sum(1 for i in pos01 if pre(i) == 46)
OUT['C3']['frames_64_to_01'] = sum(1 for i in pos01 if pre(i) == 64)

# ---------- C4: joint unigram discipline ----------
joint = (n01 + n59) / N
OUT['C4'] = {
    'joint': joint, 'P_est_n8': P_est,
    'joint_over_n8': joint / P_est,
    'I1_bar_3x_fires': bool(joint / P_est > 3),
    'P01_over_n8': (n01 / N) / P_est,
}

# ---------- C5: @295 founding window ----------
w295 = [i for i in range(N - 4) if pairs[i:i + 5] == [65, 16, 1, 11, 78]]
OUT['C5'] = {'window_positions': w295}
for s in w295:
    OUT['C5'][f'context_{s}'] = pairs[max(0, s - 6):s + 11]

# ---------- C6: 59's legs re-verified ----------
P59 = n59 / N
n64 = sum(1 for g in pairs if g == 64)
n94 = sum(1 for g in pairs if g == 94)
s2 = sum(1 for i in pos59 if pre(i) == 64) / n64
s3 = sum(1 for i in pos59 if pre(i) == 94) / n94
rival59 = {}
for w, key in [('doute', 'P_doute'), ('dit', 'P_dit'), ('fait', 'P_fait'),
               ('veut', 'P_veut'), ('peut', 'P_peut')]:
    pw = n8[key]
    r = P59 / pw if pw else float('inf')
    rival59[w] = {'ratio': r, 'kill_holds_5x': bool(r >= 5)}
OUT['C6'] = {
    'S1_ratio': P59 / P_est,
    'S2_cipher': s2, 'S2_n8': n8['P_est_given_qui'], 'S2_ratio': s2 / n8['P_est_given_qui'],
    'S3_cipher': s3, 'S3_n8': n8['P_est_given_n'], 'S3_ratio': s3 / n8['P_est_given_n'],
    'L5_rivals': rival59,
    'all_hold': bool(P59 / P_est < 2 and s2 / n8['P_est_given_qui'] < 3
                     and s3 / n8['P_est_given_n'] < 2
                     and all(v['kill_holds_5x'] for v in rival59.values())),
}

# ---------- verdict ----------
D1 = OUT['C1_verdict'] == 'FAIL'
D2 = OUT['C2']['D2_fires']
D3 = OUT['C6']['all_hold']
C1pass = OUT['C1_verdict'] == 'PASS'
C3uniq = OUT['C3']['est_unique_survivor']
C5pass = None  # qualitative; set in report
if C1pass and C3uniq:
    verdict = 'PROMOTE-candidate (pending C5 + c\'est consistency + red team)'
elif D1 and D2 and D3:
    verdict = 'DEMOTE 01 MEDIUM->WEAK'
else:
    verdict = 'CONFIRM MEDIUM'
OUT['verdict_rule_inputs'] = {'D1_no_conditioning': D1, 'D2_exclusivity': D2,
                              'D3_59_legs_hold': D3, 'C1_pass': C1pass,
                              'C3_unique_survivor': C3uniq}
OUT['verdict'] = verdict

with open(os.path.join(HERE, 'results.json'), 'w') as f:
    json.dump(OUT, f, indent=1, default=str)
print(json.dumps({k: v for k, v in OUT.items()
                  if k in ('n01', 'n59', 'C1_verdict', 'verdict')}, indent=1))
print('C1 families:')
for k, v in C1.items():
    if 'p_bonferroni_m6' in v:
        print(f"  {k}: p_corr={v['p_bonferroni_m6']:.4g} acc01={v['acc_01']} acc59={v['acc_59']} qualifies={v['qualifies']}")
print('C2:', json.dumps(OUT['C2'], default=str))
print('C3 unique survivor:', C3uniq, {w: round(r['ratio_vs_P01'], 2) for w, r in rivals.items()})
print('C4 joint/N8:', round(joint / P_est, 3), 'bar fires:', OUT['C4']['I1_bar_3x_fires'])
print('C5 windows:', w295)
print('C6 all hold:', D3)
