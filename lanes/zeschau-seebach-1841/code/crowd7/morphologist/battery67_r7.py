#!/usr/bin/env python3
"""Round-7 MORPHOLOGIST: 67 classification completion (work order 12).

Extends round-6 B4 with new F33-grade conditioning legs. Era: Tocqueville
word-space ONLY (F30). Canonical: repaired 1,847-pair parse.
Writes: code/crowd7/morphologist/battery67_r7.json
"""
import json, os, sys
from collections import Counter

sys.path.insert(0, os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd4'))
from repaired_parse import load_pairs_repaired
import syllabary4 as S

HERE = os.path.dirname(os.path.abspath(__file__))
pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847
S._era_init()
ERA = S._ERA
U, B = S._ERA_U, S._ERA_B
NW = len(ERA)

out = {}

def ngram_pos(seq):
    L = len(seq)
    return [i for i in range(N - L + 1) if pairs[i:i + L] == list(seq)]

def eseq(words):
    L = len(words)
    return sum(1 for i in range(NW - L + 1) if ERA[i:i + L] == list(words))

def ebigram(a, b):
    t = sum(B[a].values())
    return (B[a][b] / t) if t else 0.0

# ---- era discrimination table for (et|veut) in open-67 frames ----
STOP_ER = {'premier', 'premiers', 'première', 'premières', 'dernier',
           'derniers', 'dernière', 'dernières', 'étranger', 'étrangers',
           'étrangère', 'étrangères', 'léger', 'légers', 'légère', 'légères',
           'amer', 'amère', 'amers', 'amères', 'fier', 'fière', 'fiers',
           'fières', 'cher', 'chère', 'chers', 'chères', 'hier', 'enfer',
           'hiver', 'hivers', 'danger', 'dangers', 'mer', 'mers', 'fer',
           'vers', 'divers', 'diverse', 'diverses', 'travers', 'univers',
           'caractères', 'mystère', 'ministère', 'cimetière', 'frère'}
INF = set(w for w in set(ERA) if len(w) >= 4 and w.endswith('er') and w not in STOP_ER)

def trigram_et_veut(w1, w2, third_in_inf=False):
    """n('et w1 w2...') vs n('veut w1 w2...') in era; optionally third word must be infinitive."""
    n_et = n_veut = 0
    n_et_inf = n_veut_inf = 0
    for i in range(NW - 2):
        if ERA[i+1] == w1 and ERA[i+2] == w2:
            if ERA[i] == 'et':
                n_et += 1
                if i + 3 < NW and ERA[i+3] in INF:
                    n_et_inf += 1
            elif ERA[i] == 'veut':
                n_veut += 1
                if i + 3 < NW and ERA[i+3] in INF:
                    n_veut_inf += 1
    return {'et': n_et, 'veut': n_veut, 'et_inf3': n_et_inf, 'veut_inf3': n_veut_inf}

legs = {}
legs['et_la'] = {'bigram': (eseq(['et', 'la']), eseq(['veut', 'la']))}
legs['et_la_trigram'] = trigram_et_veut('x', 'y')  # placeholder replaced below
legs['et_la'] = {'et': eseq(['et', 'la']), 'veut': eseq(['veut', 'la'])}
legs['et_le'] = {'et': eseq(['et', 'le']), 'veut': eseq(['veut', 'le'])}
legs['et_par'] = {'et': eseq(['et', 'par']), 'veut': eseq(['veut', 'par'])}
legs['et_que'] = {'et': eseq(['et', 'que']), 'veut': eseq(['veut', 'que'])}
legs['la_et'] = {'et': eseq(['la', 'et']), 'veut': eseq(['la', 'veut'])}
legs['le_veut'] = {'le_veut': eseq(['le', 'veut']), 'les_veut': eseq(['les', 'veut']),
                   'le_et': eseq(['le', 'et']), 'les_et': eseq(['les', 'et'])}
# trigram detail for the 4 suc=11 frames
legs['tri_et_la'] = trigram_et_veut('la', None)  # computed properly below
out['era_legs'] = legs

# proper trigram counts: ('et'|'veut', 'la', w3) for the observed w3 values
tri = {}
for w3 in ['première', 'par', 'INF']:
    n_et = n_veut = 0
    for i in range(NW - 3):
        if ERA[i+1] == 'la' and ((w3 == 'INF' and ERA[i+2] in INF) or ERA[i+2] == w3):
            if ERA[i] == 'et':
                n_et += 1
            elif ERA[i] == 'veut':
                n_veut += 1
    tri[w3] = {'et': n_et, 'veut': n_veut}
out['era_legs']['tri_la_w3'] = tri
# ('et'|'veut','le',w3)
tri2 = {}
for w3 in ['INF']:
    n_et = n_veut = 0
    for i in range(NW - 3):
        if ERA[i+1] == 'le' and ERA[i+2] in INF:
            if ERA[i] == 'et':
                n_et += 1
            elif ERA[i] == 'veut':
                n_veut += 1
    tri2[w3] = {'et': n_et, 'veut': n_veut}
out['era_legs']['tri_le_w3'] = tri2

# ---- 08 profile (round-2 lead 08="ni"; two open 67s have suc=08) ----
F08, P08 = Counter(), Counter()
for i, x in enumerate(pairs):
    if x == '08':
        if i + 1 < N:
            F08[pairs[i+1]] += 1
        if i > 0:
            P08[pairs[i-1]] += 1
out['g08'] = {'n': pairs.count('08'), 'followers': dict(F08), 'predecessors': dict(P08)}
# era "ni" test: P(follower of ni is X)
ni_f = Counter()
for a, b in zip(ERA, ERA[1:]):
    if a == 'ni':
        ni_f[b] += 1
out['era_ni'] = {'n': sum(ni_f.values()), 'top_followers': ni_f.most_common(15)}
# cipher 08-08 doubling?
out['g08']['n_08_08'] = len(ngram_pos(['08', '08']))

# ---- audit existing classes: dump contexts ----
def ctx(i, r=4):
    return pairs[max(0, i-r):i+5]
prev = json.load(open(os.path.expanduser(
    '~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd6/morphologist/battery96_67_results.json')))
b4 = prev['WOB']['B4_by_class']
out['prev_classes'] = b4
open_ctx = {}
for i in range(N):
    if pairs[i] == '67':
        pre = pairs[i-1] if i > 0 else None
        suc = pairs[i+1] if i+1 < N else None
        open_ctx[i] = {'pre': pre, 'suc': suc, 'suc2': pairs[i+2] if i+2 < N else None,
                       'win': ctx(i)}
out['open_contexts'] = {str(k): v for k, v in open_ctx.items() if k in b4['open']}

with open(os.path.join(HERE, 'battery67_r7.json'), 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)

print('era legs:')
for k, v in legs.items():
    if k not in ('et_la_trigram', 'tri_et_la'):
        print(' ', k, v)
print('tri_la_w3:', tri)
print('tri_le_w3:', tri2)
print('08:', out['g08']['n'], 'foll:', dict(F08), 'pred:', dict(P08))
print('era ni:', out['era_ni']['n'], out['era_ni']['top_followers'][:8])
print('wrote battery67_r7.json')
