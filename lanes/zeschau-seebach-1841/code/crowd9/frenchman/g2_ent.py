#!/usr/bin/env python3
"""GATE 2: 06='ent' by-ear at the 4 W06 windows (F34/F44 + over-splitting lens).
06 cells at 580, 738, 1184, 1355 (pre=82 in all four)."""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corpus9
sys.path.insert(0, str(corpus9.LANE / 'code/crowd8/frenchman'))
from util import PAIRS, N, GT, positions, window

out = {}
W06 = [580, 738, 1184, 1355]
GT.update({87: 'ce', 64: 'qui', 96: 'par', 59: 'est', 94: 'ne', 52: 'pas',
           62: 'on/il', 00: 'pour?'})
out['windows'] = {}
for i in W06:
    out['windows'][i] = {
        'str': window(i, 5),
        'pre': PAIRS[i-1], 'pre2': PAIRS[i-2], 'pre3': PAIRS[i-3],
        'suc': PAIRS[i+1], 'suc2': PAIRS[i+2]}

# era legs (strict v8 first, then primary)
def C(*w):
    return {'v8': corpus9.ngram_count('v8file', *w)}
# corpus9 'primary' = v8+levant; do v8-only via direct file
import re
v8t = corpus9.tokenize_elision(open(corpus9.CORP / 'nesselrode-v8.txt', encoding='utf-8', errors='replace').read())
def cv8(*w):
    n = len(w); return sum(1 for i in range(len(v8t)-n+1) if tuple(v8t[i:i+n]) == tuple(w))
out['era_v8'] = {
    'ne_ment_pas': cv8('ne', 'ment', 'pas'),
    'ne_ment': cv8('ne', 'ment'),
    'ment': v8t.count('ment'),
    'ne_mentent': cv8('ne', 'mentent'),
    'mentent': v8t.count('mentent'),
    'm_entendent': sum(1 for i in range(len(v8t)-1) if v8t[i] == "m'" and v8t[i+1] == 'entendent'),
    'ne_m_entendent': sum(1 for i in range(len(v8t)-2) if v8t[i] == 'ne' and v8t[i+1] == "m'" and v8t[i+2] == 'entendent'),
    'entendent': v8t.count('entendent'),
    'ne_m_entendent_pas': sum(1 for i in range(len(v8t)-3) if tuple(v8t[i:i+4]) == ('ne', "m'", 'entendent', 'pas')),
}
out['era_primary'] = {
    'ne_ment_pas': corpus9.ngram_count('primary', 'ne', 'ment', 'pas'),
    'ne_mentent': corpus9.ngram_count('primary', 'ne', 'mentent'),
    'ne_m_entendent': sum(1 for i in range(len(corpus9.load('primary'))-2)
                           if tuple(corpus9.load('primary')[i:i+3]) == ('ne', "m'", 'entendent')),
}
# -ment adverbs before 'pour' (for @738 '[stem]ment pour')
out['ment_pour_v8'] = cv8('seulement', 'pour') + 0  # placeholder replaced below
mp = {}
for i in range(len(v8t)-1):
    if v8t[i].endswith('ment') and len(v8t[i]) > 4 and v8t[i+1] == 'pour':
        mp[v8t[i]] = mp.get(v8t[i], 0) + 1
out['mentX_pour_v8'] = {'total': sum(mp.values()), 'top': sorted(mp.items(), key=lambda x: -x[1])[:10]}
out['v8_tokens'] = len(v8t)
json.dump(out, open('g2_out.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
