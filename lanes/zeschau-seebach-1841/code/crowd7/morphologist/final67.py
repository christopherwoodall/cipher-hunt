#!/usr/bin/env python3
"""Round-7 MORPHOLOGIST: bank the final 67 classification with rules + fences.
Writes battery67_final.json."""
import json, os, sys
from collections import Counter

sys.path.insert(0, os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd4'))
from repaired_parse import load_pairs_repaired

HERE = os.path.dirname(os.path.abspath(__file__))
pairs, _, _ = load_pairs_repaired()
N = len(pairs)
prev = json.load(open(os.path.expanduser(
    '~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd6/morphologist/battery96_67_results.json')))
ctx = {c['pos']: c for c in prev['WOB']['B1_contexts']}
positions = [i for i in range(N) if pairs[i] == '67']
assert len(positions) == 38

RULES = {
    'R_et1': 'pre in {06,86} (M1 stem frames)',
    'R_et2': 'suc == 64 (qui) — "et qui" era 99 vs "veut qui" 0',
    'R_et3': 'pre2 in {06,86} and pre == 29 (infinitive formula)',
    'R_et4': 'suc == 11 (la) — era "et la"=196 vs "veut la"=0; trigrams clean',
    'R_et5': 'suc == 77 (le) — era "et le"=185 vs "veut le"=2 (both non-clitic); FENCED: not when pre in {21,11}',
    'R_et6': 'suc == 96 (par) — era "et par"=38 vs "veut par"=1 (instrumental, unfitting); n=1',
    'R_veut1': 'pre == 21 — rests on 21="le/les" lead; era "le veut"=2 vs "le et"=0',
    'R_veut2': 'suc == 78 — "veut me"-syllable frames (round-5/6)',
    'R_veut3': 'pre == 11 (la) — "la veut" era-attested; "la et"=0',
}

def classify(i):
    c = ctx[i]
    pre, suc = c['pre'], c['suc']
    et_reasons = []
    if pre in ('06', '86'):
        et_reasons.append('R_et1')
    if suc == '64':
        et_reasons.append('R_et2')
    if c['pre2'] in ('06', '86') and pre == '29':
        et_reasons.append('R_et3')
    if suc == '11':
        et_reasons.append('R_et4')
    if suc == '77' and pre not in ('21', '11'):
        et_reasons.append('R_et5')
    if suc == '96':
        et_reasons.append('R_et6')
    veut_reasons = []
    if pre == '21':
        veut_reasons.append('R_veut1')
    if suc == '78':
        veut_reasons.append('R_veut2')
    if pre == '11':
        veut_reasons.append('R_veut3')
    return et_reasons, veut_reasons

rows = []
for i in positions:
    er, vr = classify(i)
    if er and vr:
        cls = 'COLLISION'
    elif er:
        cls = 'et'
    elif vr:
        cls = 'veut'
    else:
        cls = 'open'
    rows.append({'pos': i, 'class': cls, 'et_rules': er, 'veut_rules': vr,
                 'pre': ctx[i]['pre'], 'suc': ctx[i]['suc']})

tally = Counter(r['class'] for r in rows)
out = {'rules': RULES, 'n': 38, 'tally': dict(tally), 'rows': rows,
       'fences': {
           'R_et5_fence': 'does not fire when pre in {21,11} (veut pre-markers); collision @506 -> OPEN (fork-ambiguous)',
           '506': 'pre=21 AND suc=77: era joint "le et le"=0, "le veut le"=1 (boundary-mediated), "les"-forms 0; '
                  'grammaticality turns on unresolved 21 (subject vs clitic). 1/38 collision bounds the conditioning; does not falsify the fork.',
       },
       'era_legs': {
           'et_la': [196, 0], 'et_le': [185, 2], 'et_par': [38, 1],
           'la_et': [0, 0], 'la_veut': [0, 1],
           'le_veut': [2, 0], 'le_et': [0, 0],
           'et_la_premiere_tri': [1, 0], 'et_la_INF_tri': [1, 0],
       }}
with open(os.path.join(HERE, 'battery67_final.json'), 'w') as f:
    json.dump(out, f, indent=1)

print('tally:', dict(tally))
print('et:', sorted(r['pos'] for r in rows if r['class'] == 'et'))
print('veut:', sorted(r['pos'] for r in rows if r['class'] == 'veut'))
print('open:', sorted(r['pos'] for r in rows if r['class'] == 'open'))
print('collision:', sorted(r['pos'] for r in rows if r['class'] == 'COLLISION'))
print('wrote battery67_final.json')
