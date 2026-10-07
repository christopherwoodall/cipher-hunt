#!/usr/bin/env python3
"""Round-8 patternist: WO-11 (16='i' position-conditioned test) + WO-12
(Mehemet-Ali discrimination + RdDM 293x). Pre-registered in PREREG.md
BEFORE data was touched. Standing rules: per-window nulls only, no bearing
counts on manual tilings; assert len(cells)==len(groups) on recounts.
"""
import json, math, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'inventorist'))
from repaired_parse import load_pairs_repaired
from byear import tile as byear_tile, normalize

P, _, _ = load_pairs_repaired()
OUT = os.path.join(LANE, 'code', 'crowd8', 'patternist')
os.makedirs(OUT, exist_ok=True)

# ============ T1: follower word-initial-anchor enrichment ============
WI = {'11', '70', '46', '87', '64', '94', '96', '62'}  # primary (pre-reg)
pos16 = [i for i, g in enumerate(P) if g == '16']
pos34 = [i for i, g in enumerate(P) if g == '34']
assert len(pos16) == 28 and len(pos34) == 11
fol16 = [P[i + 1] for i in pos16 if i + 1 < len(P)]
fol34 = [P[i + 1] for i in pos34 if i + 1 < len(P)]
assert len(fol16) == 28 and len(fol34) == 11


def fisher_greater(a, b, c, d):
    """One-sided Fisher exact P(X>=a) for [[a,b],[c,d]]."""
    from math import comb
    n1, n2 = a + b, c + d
    K = a + c
    N = n1 + n2
    p = 0.0
    for x in range(a, min(n1, K) + 1):
        p += comb(n1, x) * comb(n2, K - x) / comb(N, K)
    return p


def t1_run(wi_set, fol16_use, fol34_use, label):
    a = sum(1 for g in fol16_use if g in wi_set)
    b = len(fol16_use) - a
    c = sum(1 for g in fol34_use if g in wi_set)
    d = len(fol34_use) - c
    p = fisher_greater(a, b, c, d)
    OR = (a * d / (b * c)) if b * c else float('inf')
    return {'label': label, 'table': [[a, b], [c, d]], 'p_one_sided': round(p, 4),
            'odds_ratio': round(OR, 3) if OR != float('inf') else 'inf',
            'wi_hits_16': sorted([g for g in fol16_use if g in wi_set]),
            'wi_hits_34': sorted([g for g in fol34_use if g in wi_set]),
            'pass': bool(p < 0.05)}


# parmi-window sensitivity: drop the 16@1198 follower (64)
fol16_no_parmi = [P[i + 1] for i in pos16 if i + 1 < len(P) and i != 1198]
assert len(fol16_no_parmi) == 27 and P[1198] == '16' and P[1199] == '64'
t1_primary = t1_run(WI, fol16, fol34, 'primary')
t1_s1 = t1_run({'11', '70', '46'}, fol16, fol34, 'S1 GT-only WI')
t1_s2 = t1_run(WI | {'77'}, fol16, fol34, 'S2 WI+77')
t1_s3 = t1_run(WI, fol16_no_parmi, fol34, 'S3 excl parmi-window follower')
print('T1 primary:', json.dumps(t1_primary))
print('T1 S1:', t1_s1['p_one_sided'], 'S2:', t1_s2['p_one_sided'], 'S3:', t1_s3['p_one_sided'])

# ============ T2: premier/premiere minimal-pair frames ============
def count_ngram(ng):
    n = len(ng)
    return [i for i in range(len(P) - n + 1) if P[i:i + n] == ng]

A = [i for i in count_ngram(['70', '82', '34', '29']) if P[i + 4] != '40']  # masc premier
B = count_ngram(['70', '82', '16', '29'])
C5 = count_ngram(['70', '82', '16', '29', '40'])
GT5 = count_ngram(['70', '82', '34', '29', '40'])
t2 = {'masc_34_frame_70-82-34-29': A, 'nA': len(A),
      'medial_16_frame_70-82-16-29': B, 'nB': len(B),
      'fem_16_frame_70-82-16-29-40': C5, 'nC5': len(C5),
      'GT_fem_70-82-34-29-40': GT5, 'nGT': len(GT5)}
if len(B) >= 1 or len(C5) >= 1:
    t2['verdict'] = 'ADVERSE'
elif len(A) >= 1 and len(B) == 0 and len(C5) == 0:
    t2['verdict'] = 'SUPPORT'
else:
    t2['verdict'] = 'UNINFORMATIVE'
print('T2:', json.dumps({k: v for k, v in t2.items() if not isinstance(v, list)}))

# verdict (a) per pre-reg rule
if t1_primary['pass'] and t2['verdict'] != 'ADVERSE':
    va = 'SUPPORTED'
elif not t1_primary['pass'] and t2['verdict'] == 'UNINFORMATIVE':
    va = 'NOT SUPPORTED (B1 redirect fails)'
elif t2['verdict'] == 'ADVERSE':
    va = 'KILLED'
else:
    va = 'MIXED (T1 %s, T2 %s)' % ('pass' if t1_primary['pass'] else 'fail', t2['verdict'])
print('VERDICT (a):', va)

# ============ D1: the 62-tension ============
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'period_drag'))
from common import GT, PROV, LE77, ISLETS, fit_cells, load_lexicon_tilings
HARD = dict(GT); HARD.update(PROV); HARD.update(LE77)

# the claim's own tiling puts /a/ on 62:
claim_cells = ['me', 'he', 'met', 'a', 'li']
assert len(claim_cells) == len(P[8:13]) == 5
d1_claim = {'cells[3] on 62': claim_cells[3], 'conflicts_with_62=on': claim_cells[3] != 'on'}

alts = []
for w in ['mehemetali', 'mehemedali']:
    wn = normalize(w)
    for cells, _sc in byear_tile(wn, k=8):
        if len(cells) == 5 and cells[0] == 'me':
            alts.append((w, cells))
d1 = {'claim_tiling_62_cell': claim_cells[3],
      'n_alt_len5_me tilings': len(alts),
      'alts_avoiding_a_on_62': [(w, c) for w, c in alts if 'a' not in c[3]],
      'all_alts_put_a_on_62': bool(alts) and all('a' in c[3] for _, c in alts)}
d1['tension_confirmed'] = bool(d1_claim['conflicts_with_62=on'] and
                               (not alts or d1['all_alts_put_a_on_62']))
print('D1:', json.dumps({k: v for k, v in d1.items() if k != 'alts_avoiding_a_on_62'}),
      'avoiders:', d1['alts_avoiding_a_on_62'][:3])

# ============ D2: 62-cell distribution across the 33 @8 fitters ============
lex = load_lexicon_tilings()
groups8 = P[8:13]
assert groups8 == ['78', '18', '93', '62', '98'], groups8
fitters = []
for w in lex:
    for cells, _s in byear_tile(w, k=8):
        if len(cells) != len(groups8):
            continue
        assert len(cells) == len(groups8)
        ok, _ = fit_cells(cells, groups8, HARD)
        if ok:
            fitters.append((w, cells))
            break
assert len(fitters) == 33, len(fitters)  # reproduce T7 null
c62 = Counter(c[3] for _, c in fitters)
on_compat = [(w, c) for w, c in fitters if c[3] == 'on']
name_like = [(w, c) for w, c in fitters
             if re.search(r'mehemet|mehemed|mohamed|mexique|ali$', w, re.I)]
d2 = {'n_fitters': len(fitters), 'cells3_dist': dict(c62.most_common()),
      'on_compatible': [[w, c] for w, c in on_compat],
      'n_on_compatible': len(on_compat),
      'name_like_fitters': [[w, c] for w, c in name_like]}
d2['discriminator_confirmed'] = bool(len(on_compat) >= 1)
print('D2: n=%d on_compat=%d' % (len(fitters), len(on_compat)),
      'cells[3]:', dict(c62.most_common(8)))

# verdict (b) per pre-reg rule
if d1['tension_confirmed'] and d2['discriminator_confirmed']:
    vb = 'DEMOTE recommended: LEAD -> LEAD-weak (red team adjudicates)'
elif d1['tension_confirmed']:
    vb = 'HOLD (LEAD), weakened; promotion blocked on 62'
else:
    vb = 'HOLD (LEAD) unchanged'
print('VERDICT (b):', vb)

out = {'T1': {'primary': t1_primary, 'S1': t1_s1, 'S2': t1_s2, 'S3': t1_s3},
       'T2': t2, 'verdict_a': va, 'D1': d1, 'D2': d2, 'verdict_b': vb}
json.dump(out, open(os.path.join(OUT, 'round8_results.json'), 'w'), indent=1)
print('wrote', os.path.join(OUT, 'round8_results.json'))
