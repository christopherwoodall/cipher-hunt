#!/usr/bin/env python3
"""Round-10 67-FINISHER residual scorer. Implements PREREG.md bars E3, E4, E7.

Era: Nesselrode v8, lane tokenizer vendored (identical to round-9 score67_r9.py).
Writes: code/crowd10/finisher67/results_r10.json
"""
import json, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N

# ---------- F0: byte-verify the 6 windows against the standing record ----------
r8 = json.load(open(os.path.join(LANE, 'code/crowd8/morphologist/results_r8.json')))
OPENS = ['633', '902', '1372', '1450', '1519', '1623']
F0 = {}
for k in OPENS:
    p = int(k)
    w = r8['open67'][k]
    ok = (w['pre'] == pairs[p-1] and pairs[p] == '67' and w['suc'] == pairs[p+1]
          and w['pre2'] == pairs[p-2] and w['suc2'] == pairs[p+2]
          and [f"{i}:{pairs[i]}" for i in range(p-2, p+3)] == w['win'])
    F0[k] = {'pass': ok, 'win': [f"{i}:{pairs[i]}" for i in range(p-2, p+3)]}
assert all(v['pass'] for v in F0.values()), F0

# ---------- standing classes for the contact census ----------
b7 = json.load(open('code/crowd7/morphologist/battery67_final.json'.replace('code/crowd7', os.path.join(LANE, 'code/crowd7'))))
stand = {str(r['pos']): r['class'] for r in b7['rows']}
# round-9 adjudicated overlays (not classifications): 1248/199 fenced, 630 conditional
stand['1248'] = 'NEITHER-fenced'
stand['199'] = 'NEITHER-fenced-conditional'
stand['630'] = 'et-CONDITIONAL'

def contact_census(p, side):
    """Other 67-windows sharing pre (side=-1) or suc (side=+1): {class: count}."""
    tgt = pairs[p + side]
    c = Counter()
    poss = []
    for i in range(N):
        if pairs[i] == '67' and i != p and pairs[i + side] == tgt:
            cl = stand.get(str(i), 'open')
            c[cl] += 1
            poss.append(i)
    return dict(c), sorted(poss)

census = {}
for k in OPENS:
    p = int(k)
    pre_c, pre_pos = contact_census(p, -1)
    suc_c, suc_pos = contact_census(p, +1)
    census[k] = {'pre': pairs[p-1], 'pre_contact': pre_c, 'pre_pos': pre_pos,
                 'suc': pairs[p+1], 'suc_contact': suc_c, 'suc_pos': suc_pos}

# ---------- L2 nominal contacts (GT-anchored: 11 = "la") ----------
def n_bigram(a, b):
    return sum(1 for i in range(N - 1) if pairs[i] == a and pairs[i+1] == b)

L2 = {'n_11_31': n_bigram('11', '31'),   # E3 @1519
      'n_11_98': n_bigram('11', '98'),   # E4 @1372
      'n_11_33': n_bigram('11', '33'),   # E7 @1450/@1623
      'n_11_52': n_bigram('11', '52'),   # reference (round-9 E2-L2)
      'n_11_63': n_bigram('11', '63')}   # @633 reference

# ---------- era side (vendored lane tokenizer) ----------
def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

def split_nesselrode():
    C = os.path.join(LANE, 'code', 'side-period', 'corpus')
    txt = open(os.path.join(C, 'nesselrode-v8.txt'), encoding='utf-8', errors='replace').read()
    months = 'janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre'
    pat = re.compile(r'^((?:Saint-Pétersbourg|Berlin|Paris|Londres|Vienne|Varsovie|Constantinople|Munich|Dresde)[ ,.\u00a0]*\d{1,2}\s+(?:%s)\s+184[0-6])\.?,?\s*$' % months, re.M)
    bounds = [m.start() for m in pat.finditer(txt)]
    return [txt[a:b] for a, b in zip(bounds, bounds[1:] + [len(txt)])]

W = []
for d in split_nesselrode():
    W += tok(d)
NW = len(W)
assert NW == 92123, NW

def nseq(ws):
    L = len(ws)
    return sum(1 for i in range(NW - L + 1) if W[i:i+L] == list(ws))

def ngap(a, c):
    """n(a * c): trigram with any middle word."""
    return sum(1 for i in range(NW - 2) if W[i] == a and W[i+2] == c)

era = {
    'NW': NW,
    'n_et_l': nseq(['et', 'l']),            # E3-L1 @1519
    'n_veut_l': nseq(['veut', 'l']),
    'n_et_gap_pour': ngap('et', 'pour'),    # E4-L1 @1372
    'n_veut_gap_pour': ngap('veut', 'pour'),
    'n_et_gap_que': ngap('et', 'que'),      # E7-L1 @1450/@1623
    'n_veut_gap_que': ngap('veut', 'que'),
}
# show the veut-arm middles for the record (what would the rival be?)
era['veut_gap_pour_middles'] = Counter(W[i+1] for i in range(NW-2) if W[i] == 'veut' and W[i+2] == 'pour').most_common(8)
era['veut_gap_que_middles'] = Counter(W[i+1] for i in range(NW-2) if W[i] == 'veut' and W[i+2] == 'que').most_common(8)

def L1_pass(e_et, e_veut):
    return e_et >= 20 and e_veut <= 3 and (e_veut == 0 or e_et / e_veut >= 10)

bars = {}
# E3 @1519
l1 = {'E_et': era['n_et_l'], 'E_veut': era['n_veut_l'], 'pass': L1_pass(era['n_et_l'], era['n_veut_l'])}
l2 = {'n_11_31': L2['n_11_31'], 'pass': L2['n_11_31'] >= 2}
bars['1519'] = {'bar': 'E3', 'L1': l1, 'L2': l2,
                'pass': bool(F0['1519']['pass'] and l1['pass'] and l2['pass']),
                'verdict': 'et-CONDITIONAL(C1:08=l-apos,C2:67-standalone)' if (F0['1519']['pass'] and l1['pass'] and l2['pass']) else 'open-residual'}
# E4 @1372
l1 = {'E_et': era['n_et_gap_pour'], 'E_veut': era['n_veut_gap_pour'],
      'pass': L1_pass(era['n_et_gap_pour'], era['n_veut_gap_pour'])}
l2 = {'n_11_98': L2['n_11_98'], 'pass': L2['n_11_98'] >= 2}
bars['1372'] = {'bar': 'E4', 'L1': l1, 'L2': l2,
                'pass': bool(F0['1372']['pass'] and l1['pass'] and l2['pass']),
                'verdict': 'et-CONDITIONAL(C1p:00=pour,C2:67-standalone)' if (F0['1372']['pass'] and l1['pass'] and l2['pass']) else 'open-residual'}
# E7 @1450 and @1623
for k in ('1450', '1623'):
    l1 = {'E_et': era['n_et_gap_que'], 'E_veut': era['n_veut_gap_que'],
          'pass': L1_pass(era['n_et_gap_que'], era['n_veut_gap_que'])}
    l2 = {'n_11_33': L2['n_11_33'], 'pass': L2['n_11_33'] >= 2}
    ok = bool(F0[k]['pass'] and l1['pass'] and l2['pass'])
    bars[k] = {'bar': 'E7', 'L1': l1, 'L2': l2, 'pass': ok,
               'verdict': 'et-CONDITIONAL(C2:67-standalone)' if ok else 'open-residual'}

bars['633'] = {'bar': 'none-design-null', 'verdict': 'open-residual'}
bars['902'] = {'bar': 'none-design-null', 'verdict': 'open-residual'}

out = {'F0': F0, 'era': era, 'L2_nominal': L2, 'bars': bars,
       'contact_census_unscored': census,
       'n67_tally': {'classified_et': 18, 'classified_veut': 11,
                     'fenced_neither': 2, 'conditional': 1, 'open_residual': 6}}
json.dump(out, open(os.path.join(HERE, 'results_r10.json'), 'w'), indent=1, ensure_ascii=False)
print(json.dumps({'bars': bars, 'L2_nominal': L2,
                  'era_frames': {k: v for k, v in era.items() if not k.endswith('middles')}}, indent=1))
print('veut*pour middles:', era['veut_gap_pour_middles'])
print('veut*que middles:', era['veut_gap_que_middles'])
print('WROTE results_r10.json')
