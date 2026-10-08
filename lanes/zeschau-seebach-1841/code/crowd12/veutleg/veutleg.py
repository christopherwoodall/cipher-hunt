#!/usr/bin/env python3
"""VEUT-ARM SUBJECT BAR — round 12, WO-2 (VEUT-SECOND-LEG executor).

Implements code/crowd12/veutleg/PREREG.md literally. Pre-registered
2026-10-07 21:24 UTC, before any round-12 computation on this question.

Question: does an era "veut" frame license the 36/66 predecessor of the
decider 67s (@1450: 59-36-67-33-46 ; @1623: 78-66-67-33-46)?
Bar: 36/66 must be subject-compatible (nominal) from OTHER windows for the
veut-arm to survive; verbal 36/66 kills it at that window.
"""
import json
import math
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.expanduser(
    '~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code'), 'crowd4'))
from repaired_parse import load_pairs_repaired

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N
freq = Counter(pairs)

# ---------- byte-exact window verification (standing record) ----------
assert pairs[1448:1453] == ['59', '36', '67', '33', '46'], pairs[1448:1453]
assert pairs[1621:1626] == ['78', '66', '67', '33', '46'], pairs[1621:1626]

# ---------- alternative-(b) negative: all 33-positions with suc==46 ----------
pos33_suc46 = [i for i, p in enumerate(pairs)
               if p == '33' and i + 1 < N and pairs[i + 1] == '46']

# ---------- cipher-side: 36/66 class census (decider windows excluded) ----------
# Pre-registered licensor sets
NOM_PRE = {'11', '08', '77', '96', '87', '47'}   # 08/77 WEAK (F82 caveat)
NOM_SUC = {'64'}                                 # suc=qui follows nominals
VRB_PRE = {'64'}                                 # pre=qui -> P finite-verbal
VRB_SUC = {'29'}                                 # suc=er -> P verb stem (F22)
AMBIGUOUS = {'00', '06', '86', '46', '59'}       # +67v handled below

DECIDER_POS = {'36': 1449, '66': 1622}
WINDOWS = {1450: '36', 1623: '66'}

def binom_p_ge(n, p, k):
    if k <= 0:
        return 1.0
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j)
               for j in range(k, n + 1))

def census(P):
    """Full pre/suc census of P, excluding its decider position."""
    excl = DECIDER_POS[P]
    pos = [i for i, p in enumerate(pairs) if p == P and i != excl]
    rows = []
    for i in pos:
        pre = pairs[i - 1] if i > 0 else None
        suc = pairs[i + 1] if i + 1 < N else None
        rows.append({'pos': i, 'pre': pre, 'suc': suc})
    nom, vrb = {}, {}
    amb = []
    for r in rows:
        i, pre, suc = r['pos'], r['pre'], r['suc']
        if pre in NOM_PRE:
            nom.setdefault('pre=' + pre, []).append(i)
        if suc in NOM_SUC:
            nom.setdefault('suc=' + suc, []).append(i)
        if pre in VRB_PRE:
            vrb.setdefault('pre=' + pre, []).append(i)
        if suc in VRB_SUC:
            vrb.setdefault('suc=' + suc, []).append(i)
        if pre in AMBIGUOUS or pre == '67':
            amb.append({'pos': i, 'cell': 'pre=' + str(pre)})
        if suc in AMBIGUOUS or suc == '67':
            amb.append({'pos': i, 'cell': 'suc=' + str(suc)})
    # binomial nulls per fired licensor
    nulls = {}
    for leg, hits in list(nom.items()) + list(vrb.items()):
        grp = leg.split('=')[1]
        p = freq[grp] / N
        k = len(hits)
        nulls[leg] = {'k': k, 'n': len(pos),
                      'E': round(len(pos) * p, 3),
                      'p_ge_k': round(binom_p_ge(len(pos), p, k), 4)}
    n_nom, n_vrb = len(nom), len(vrb)
    if n_nom >= 2 and n_vrb <= 1:
        cls = 'NOMINAL'
    elif n_vrb >= 2 and n_nom <= 1:
        cls = 'VERBAL'
    elif n_nom >= 2 and n_vrb >= 2:
        cls = 'UNRESOLVED-CONTRADICTORY'
    else:
        cls = 'UNRESOLVED'
    return {'P': P, 'n_total': freq[P], 'n_census': len(pos),
            'excluded_decider': excl, 'rows': rows,
            'nom_licensors': {k: v for k, v in nom.items()},
            'vrb_licensors': {k: v for k, v in vrb.items()},
            'ambiguous_datums': amb, 'nulls': nulls, 'CLASS': cls}

c36 = census('36')
c66 = census('66')

# ---------- era side: E1 predecessor distribution of "veut" (Nesselrode v8) ----------
def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

def split_nesselrode():
    C = os.path.join(LANE, 'code', 'side-period', 'corpus')
    txt = open(os.path.join(C, 'nesselrode-v8.txt'),
               encoding='utf-8', errors='replace').read()
    months = ('janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|'
              'septembre|octobre|novembre|décembre|decembre')
    pat = re.compile(r'^((?:Saint-Pétersbourg|Berlin|Paris|Londres|Vienne|'
                     r'Varsovie|Constantinople|Munich|Dresde)[ ,.\u00a0]*'
                     r'\d{1,2}\s+(?:%s)\s+184[0-6])\.?,?\s*$' % months, re.M)
    bounds = [m.start() for m in pat.finditer(txt)]
    return [txt[a:b] for a, b in zip(bounds, bounds[1:] + [len(txt)])]

W = []
for d in split_nesselrode():
    W += tok(d)
NW = len(W)
assert NW == 92123, NW

SUBJPRO = {'il', 'elle', 'ils', 'elles', 'on', 'cela', 'qui', 'je', 'tu',
           'nous', 'vous'}
pre_veut = Counter()
n_veut = 0
for i in range(1, NW):
    if W[i] == 'veut':
        n_veut += 1
        pre_veut[W[i - 1]] += 1
n_subjpro = sum(c for w, c in pre_veut.items() if w in SUBJPRO)
e1_ratio = n_subjpro / n_veut if n_veut else 0.0
E1_PASS = e1_ratio >= 0.50  # pre-registered bar

# ---------- verdicts (pre-registered rules) ----------
def window_verdict(P, c):
    cls = c['CLASS']
    vrb_only_64 = (set(c['vrb_licensors'].keys()) == {'pre=64'})
    if cls == 'NOMINAL' and E1_PASS:
        return 'SUPPORTS'
    if cls == 'VERBAL':
        # pre-registered sensitivity: 64-only verbal -> downgrade to NULL
        if vrb_only_64:
            return 'NULL (64-only verbal, qui-provisional caveat fenced)'
        return 'KILLS'
    return 'NULL'

v1450 = window_verdict('36', c36)
v1623 = window_verdict('66', c66)

if 'KILLS' in (v1450, v1623):
    joint = 'NULL (kill at >=1 window; per-window recommendation below)'
elif v1450 == 'SUPPORTS' and v1623 == 'SUPPORTS':
    joint = 'CONFIRMED'
elif 'SUPPORTS' in (v1450, v1623):
    joint = 'FENCED (partial)'
else:
    joint = 'NULL'

out = {
    'prereg': 'code/crowd12/veutleg/PREREG.md (2026-10-07 21:24 UTC)',
    'parse': 'repaired 1,847-pair',
    'windows_verified': {'1450': pairs[1448:1453], '1623': pairs[1621:1626]},
    'alt_b_negative': {
        '33_with_suc46': pos33_suc46,
        'only_decider_pair': pos33_suc46 == [1451, 1624],
    },
    'census_36': c36,
    'census_66': c66,
    'era_E1': {
        'corpus': 'nesselrode-v8.txt', 'NW': NW,
        'n_veut': n_veut,
        'top25_predecessors': pre_veut.most_common(25),
        'n_subjpro_pre': n_subjpro,
        'subjpro_ratio': round(e1_ratio, 4),
        'bar': '>= 0.50',
        'E1_PASS': bool(E1_PASS),
    },
    'era_E2': 'STANDING (cited, not re-counted): "il veut prouver que" '
              '(census33, v8) licenses "veut [inf] que" compositionally.',
    'per_window': {'1450 (P=36)': v1450, '1623 (P=66)': v1623},
    'joint_recommendation': joint,
}

outp = os.path.join(LANE, 'code', 'crowd12', 'veutleg', 'veutleg_results.json')
with open(outp, 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print('wrote', outp)
print('33 suc==46 positions:', pos33_suc46)
print('CLASS(36) =', c36['CLASS'], '| nom:', sorted(c36['nom_licensors']),
      '| vrb:', sorted(c36['vrb_licensors']))
print('CLASS(66) =', c66['CLASS'], '| nom:', sorted(c66['nom_licensors']),
      '| vrb:', sorted(c66['vrb_licensors']))
print('E1: n_veut =', n_veut, '| subjpro ratio =', round(e1_ratio, 4),
      '| PASS =', E1_PASS)
print('@1450:', v1450, '| @1623:', v1623, '| JOINT:', joint)
