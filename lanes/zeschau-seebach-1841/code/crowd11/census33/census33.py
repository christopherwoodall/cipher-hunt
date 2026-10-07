#!/usr/bin/env python3
"""Round-11 work order 3: 33-CLASS CENSUS. Implements code/crowd11/census33/PREREG.md.

Censuses group 33's contact profile on the repaired 1,847-pair stream,
fires the pre-registered class signatures, applies bars C1/C2/C3, then the
F74 decider for @1450/@1623. Era legs on Nesselrode v8 only.
Writes: code/crowd11/census33/census33_results.json
"""
import json, os, re, math, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N

# ---------- standing classes ----------
b7 = json.load(open(os.path.join(LANE, 'code/crowd7/morphologist/battery67_final.json')))
stand67 = {r['pos']: r['class'] for r in b7['rows']}
stand67[1248] = 'NEITHER-fenced'
stand67[199] = 'NEITHER-fenced-conditional'
stand67[630] = 'et-CONDITIONAL'
VEUT67 = {p for p, c in stand67.items() if c == 'veut'}

GOUV_FENCED = {1180, 1351}  # 77="gou" exception positions (F70)

def n_bigram(a, b):
    return sum(1 for i in range(N - 1) if pairs[i] == a and pairs[i + 1] == b)

INF_GOV = {'00'}            # I1 pre set
VEUT_PRE = 'veut67'         # I2 marker
STEM_PRE = {'06', '86'}     # I3 pre set
NOM_PRE = {'11', '77', '87', '47', '96'}  # N1..N4/N6 pre set

pos33 = [i for i, g in enumerate(pairs) if g == '33']
assert len(pos33) == 25
DECIDER_33 = {1451, 1624}   # 33s after 67@1450 / 67@1623 — excluded from census

def fire(i):
    """Return (inf_kinds:set, nom_kinds:set, notes:list) per PREREG."""
    pre, suc = pairs[i - 1], pairs[i + 1]
    inf, nom, notes = set(), set(), []
    # I1
    if pre == '00':
        inf.add('I1'); notes.append('I1 pre=00(pour-lead)')
    # I2
    if pre == '67' and (i - 1) in VEUT67:
        inf.add('I2'); notes.append('I2 pre=67-veut@%d' % (i - 1))
    elif pre == '67':
        notes.append('pre=67@%d class=%s (not veut)' % (i - 1, stand67.get(i - 1, 'open')))
    # I3
    if pre in STEM_PRE:
        inf.add('I3'); notes.append('I3 pre=%s(stem-class)' % pre)
    # I4
    if suc == '29':
        inf.add('I4'); notes.append('I4 suc=29(er): stem+er')
    # N1
    if pre == '11':
        nom.add('N1'); notes.append('N1 pre=11(la-GT)')
    # N2 (fenced at gouv positions)
    if pre == '77':
        if i - 1 in GOUV_FENCED or i in GOUV_FENCED:
            notes.append('N2 BLOCKED: gouv-fenced window')
        else:
            nom.add('N2'); notes.append('N2 pre=77(le-cond)')
    # N3/N6 (one kind: ce-governor)
    if pre in {'87', '47'}:
        nom.add('N3/N6'); notes.append('N3/N6 pre=%s(ce-%s)' % (pre, 'prov' if pre == '87' else 'lead'))
    # N4
    if pre == '96':
        nom.add('N4'); notes.append('N4 pre=96(par-prov)')
    # suc==46 disambiguation (I5/N5)
    if suc == '46':
        if pre in INF_GOV or (pre == '67' and (i - 1) in VEUT67) or pre in STEM_PRE:
            inf.add('I5'); notes.append('I5 suc=46(que): inf-licensed')
        elif pre in NOM_PRE:
            nom.add('N5'); notes.append('N5 suc=46(que): nominal+rel-que')
        else:
            notes.append('suc=46(que): AMBIGUOUS pre=%s, unscored' % pre)
    # V1
    if pre == '64':
        notes.append('V1 pre=64(qui-prov): finite-verb bucket')
    if pre == '59':
        notes.append('pre=59(est-islet): recorded, unscored')
    return inf, nom, notes

rows = []
for i in pos33:
    pre, suc = pairs[i - 1], pairs[i + 1]
    inf, nom, notes = fire(i)
    rows.append({'pos': i, 'pre': pre, 'suc': suc,
                 'excluded_decider': i in DECIDER_33,
                 'inf_kinds': sorted(inf), 'nom_kinds': sorted(nom),
                 'notes': notes})

census_rows = [r for r in rows if not r['excluded_decider']]
inf_kinds_all = Counter(k for r in census_rows for k in r['inf_kinds'])
nom_kinds_all = Counter(k for r in census_rows for k in r['nom_kinds'])
n1_hits = sum(1 for r in census_rows if 'N1' in r['nom_kinds'])
n5_hits = sum(1 for r in census_rows if 'N5' in r['nom_kinds'])

# C1 / C2 / C3 on the census (excluded decider windows)
c1 = len(inf_kinds_all) >= 2 and n1_hits == 0 and n5_hits == 0
c2 = (len(nom_kinds_all) >= 2 and (n1_hits >= 1 or sum(1 for k in nom_kinds_all if k != 'N1') >= 2)
      and sum(inf_kinds_all.values()) == 0)
verdict = 'C1-infinitive' if c1 else ('C2-nominal' if c2 else 'C3-unclassified')

# per-window nulls (binomial, base rates) for fired signatures
freq = Counter(pairs)
def binom_p(n, p, k):
    return sum(math.comb(n, j) * p**j * (1 - p)**(n - j) for j in range(k, n + 1))
nulls = {}
for sig, grp, cond in [('I1', '00', 'pre'), ('I4', '29', 'suc'), ('N1', '11', 'pre'),
                       ('N2', '77', 'pre'), ('N3/N6', None, 'pre'), ('N4', '96', 'pre')]:
    k = inf_kinds_all.get(sig, 0) or nom_kinds_all.get(sig, 0)
    if grp:
        p = freq[grp] / N
        nulls[sig] = {'k': k, 'n': len(census_rows), 'E': len(census_rows) * p,
                      'p_ge_k': round(binom_p(len(census_rows), p, k), 4) if k else 1.0}
    else:
        p = (freq['87'] + freq['47']) / N
        nulls[sig] = {'k': k, 'n': len(census_rows), 'E': len(census_rows) * p,
                      'p_ge_k': round(binom_p(len(census_rows), p, k), 4) if k else 1.0}

# ---------- era side: class-matched frames on Nesselrode v8 ----------
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

def gap_middles(a, c):
    return Counter(W[i + 1] for i in range(NW - 2) if W[i] == a and W[i + 2] == c)

et_que_mid = gap_middles('et', 'que')
veut_que_mid = gap_middles('veut', 'que')
era = {'NW': NW,
       'n_et_gap_que': sum(et_que_mid.values()),
       'n_veut_gap_que': sum(veut_que_mid.values()),
       'et_que_middles': et_que_mid.most_common(),
       'veut_que_middles': veut_que_mid.most_common()}

# decider windows' own signatures (sensitivity, not census)
dec = [{'pos': r['pos'], 'pre': r['pre'], 'suc': r['suc'],
        'inf_kinds': r['inf_kinds'], 'nom_kinds': r['nom_kinds'], 'notes': r['notes']}
       for r in rows if r['excluded_decider']]
for d in dec:
    d['67pos'] = d['pos'] - 1
    d['67win'] = [pairs[d['pos'] - 3], pairs[d['pos'] - 2], '67', '33', '46']

out = {'n33': len(pos33), 'census_n': len(census_rows),
       'freq33': round(len(pos33) / N, 5),
       'rows': rows,
       'inf_kinds_all': dict(inf_kinds_all), 'nom_kinds_all': dict(nom_kinds_all),
       'n1_hits': n1_hits, 'n5_hits': n5_hits,
       'C1': bool(c1), 'C2': bool(c2), 'verdict': verdict,
       'nulls': nulls, 'era': era, 'decider_windows': dec,
       'stand67_veut': sorted(VEUT67)}
json.dump(out, open(os.path.join(HERE, 'census33_results.json'), 'w'), indent=1, ensure_ascii=False)
print('verdict:', verdict)
print('inf_kinds:', dict(inf_kinds_all), 'nom_kinds:', dict(nom_kinds_all))
print('era et*que:', era['n_et_gap_que'], 'veut*que:', era['n_veut_gap_que'])
print('veut middles:', era['veut_que_middles'])
print('et middles:', era['et_que_middles'])
