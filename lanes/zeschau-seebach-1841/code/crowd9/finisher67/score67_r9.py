#!/usr/bin/env python3
"""Round-9 67-FINISHER scorer. Implements prereg.md bars N1 and E2.

Era: Nesselrode v8, lane tokenizer vendored (no ratemodel import -> no
module-level side effects). Corpus split: 97 dateline docs (same regex as
code/crowd8/ratemodel/ratemodel.py::split_nesselrode).
Writes: code/crowd9/finisher67/results_r9.json
"""
import json, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

# ---------- cipher side ----------
pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N

OPENS = [199, 630, 633, 902, 1248, 1372, 1450, 1519, 1623]
r8 = json.load(open(os.path.join(LANE, 'code/crowd8/morphologist/results_r8.json')))
for p in OPENS:
    w = r8['open67'][str(p)]
    assert w['pre'] == pairs[p-1] and pairs[p] == '67' and w['suc'] == pairs[p+1], p
    assert [f"{i}:{pairs[i]}" for i in range(p-2, p+3)] == w['win'], p

def fires_standing(p):
    pre, suc = pairs[p-1], pairs[p+1]
    pre2 = pairs[p-2] if p >= 2 else None
    et, veut = [], []
    if pre in ('06', '86'): et.append('R_et1')
    if suc == '64': et.append('R_et2')
    if pre2 in ('06', '86') and pre == '29': et.append('R_et3')
    if suc == '11': et.append('R_et4')
    if suc == '77' and pre not in ('21', '11'): et.append('R_et5')
    if suc == '96': et.append('R_et6')
    if pre == '21': veut.append('R_veut1')
    if suc == '78': veut.append('R_veut2')
    if pre == '11': veut.append('R_veut3')
    return et, veut

standing = {p: fires_standing(p) for p in OPENS}
assert all(e == [] and v == [] for e, v in standing.values()), standing

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

def nseq(ws):
    L = len(ws)
    return sum(1 for i in range(NW - L + 1) if W[i:i+L] == list(ws))

era = {
    'NW': NW,
    'n_pour_et_que': nseq(['pour', 'et', 'que']),
    'n_pour_veut_que': nseq(['pour', 'veut', 'que']),
    'n_pour_ce_que': nseq(['pour', 'ce', 'que']),
    'n_l_et': nseq(['l', 'et']),
    'n_l_veut': nseq(['l', 'veut']),
    'n_et_l': nseq(['et', 'l']),
    'n_veut_l': nseq(['veut', 'l']),
    'n_ce_me_et': nseq(['ce', 'me', 'et']),
    'n_ce_me_veut': nseq(['ce', 'me', 'veut']),
}

# new-arm census for @1248: "pour * que" middles
mid = Counter(W[i+1] for i in range(NW - 2) if W[i] == 'pour' and W[i+2] == 'que')
era['pour_star_que_middles'] = mid.most_common(12)

# ---------- Bar N1 ----------
n1_1248 = {'F1_parse_ok': True,
           'F2_both_zero': era['n_pour_et_que'] == 0 and era['n_pour_veut_que'] == 0,
           'F3_no_new_arm': not any(c >= 2 and len(w) <= 3 for w, c in mid.most_common(12))}
n1_1248['pass'] = all(n1_1248.values())
n1_199 = {'F1_parse_ok': True,
          'F2_both_zero': era['n_l_et'] == 0 and era['n_l_veut'] == 0,
          'F3_no_new_arm': True}
n1_199['pass'] = all(n1_199.values())

# ---------- Bar E2 (@630) ----------
E_et, E_veut = era['n_et_l'], era['n_veut_l']
n_11_52 = sum(1 for i, x in enumerate(pairs) if x == '52' and i > 0 and pairs[i-1] == '11')
e2 = {'L1': {'E_et': E_et, 'E_veut': E_veut,
             'pass': E_et >= 20 and E_veut <= 3 and (E_veut == 0 or E_et / E_veut >= 10)},
      'L2': {'n_11_52': n_11_52, 'pass': n_11_52 >= 2}}
e2['pass'] = e2['L1']['pass'] and e2['L2']['pass']

out = {
    'era': era,
    'standing_recheck': {str(p): {'et': e, 'veut': v} for p, (e, v) in standing.items()},
    'bar_N1': {'1248': n1_1248, '199': n1_199},
    'bar_E2_630': e2,
    'classification': {
        '1248': 'NEITHER-fence' if n1_1248['pass'] else 'open',
        '199': 'NEITHER-fence-conditional-on-08=l-apostrophe' if n1_199['pass'] else 'open',
        '630': 'et-CONDITIONAL(C1:08=l-apos,C2:67-standalone-word)' if e2['pass'] else 'open',
        '633': 'open', '902': 'open', '1372': 'open',
        '1450': 'open', '1519': 'open', '1623': 'open',
    },
    'unscored_leans': {
        '1519': "et-lean: L1-only 63:1 ('et l' vs 'veut l' frame); 31 class contradictory",
        '1450': "et-lean: suc==33 3/3 et on classifieds, all R_et1-confounded",
        '1623': "et-lean: suc==33 3/3 et on classifieds, all R_et1-confounded",
        '1372': "observation: shares '16 91 67' frame with @1519",
    },
}
json.dump(out, open(os.path.join(HERE, 'results_r9.json'), 'w'), indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False)[:2000])
print('WROTE results_r9.json')
