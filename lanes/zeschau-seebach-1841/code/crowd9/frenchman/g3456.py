#!/usr/bin/env python3
"""GATES 3-6: 84 en-islet predecessors; 67@1248 'pour X que'; 48 verb vetoes;
'gouvernement' collocations. Era: Nesselrode v8 strict (+ primary where noted)."""
import json, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corpus9
sys.path.insert(0, str(corpus9.LANE / 'code/crowd8/frenchman'))
from util import PAIRS, N, GT, positions, window

out = {}
v8t = corpus9.tokenize_elision(open(corpus9.CORP / 'nesselrode-v8.txt', encoding='utf-8', errors='replace').read())
V8N = len(v8t)
out['v8_tokens'] = V8N
prim = corpus9.load('primary')

# ---------- GATE 3: 84 en-islet predecessors ----------
g3 = {}
# 'm'en' era
g3['m_en_v8'] = sum(1 for i in range(V8N-1) if v8t[i] == "m'" and v8t[i+1] == 'en')
g3['m_en_primary'] = sum(1 for i in range(len(prim)-1) if prim[i] == "m'" and prim[i+1] == 'en')
# 'en' predecessor class distribution in v8 (top 25)
pre_en = collections.Counter(v8t[i-1] for i in range(1, V8N) if v8t[i] == 'en')
g3['en_predecessors_top25_v8'] = pre_en.most_common(25)
g3['n_en_v8'] = v8t.count('en')
# 'qu'en' specifically (sans doubling) and the killed 'qu'en en'
g3['qu_en_v8'] = sum(1 for i in range(V8N-1) if v8t[i] == "qu'" and v8t[i+1] == 'en')
g3['qu_en_en_v8'] = sum(1 for i in range(V8N-2) if v8t[i] == "qu'" and v8t[i+1] == 'en' and v8t[i+2] == 'en')
# noun-before-en frames: 'que [noun] en [verb]' shape — sample kwic
kw = [i for i in range(1, V8N-1) if v8t[i] == 'en' and v8t[i-1] not in
      ("qu'", "l'", "d'", "s'", "n'", "m'", "t'", "c'", "j'", 'ne', 'en', 'que', 'qui', 'pas')]
g3['en_after_nonclitic_sample'] = [' '.join(v8t[max(0,i-4):i+3]) for i in kw[:10]]
g3['en_after_nonclitic_n'] = len(kw)
out['gate3'] = g3

# ---------- GATE 4: 67@1248 'pour X que' ----------
g4 = {}
# all X in 'pour X que' in v8
pxq = collections.Counter()
for i in range(V8N-2):
    if v8t[i] == 'pour' and v8t[i+2] == 'que':
        pxq[v8t[i+1]] += 1
g4['pour_X_que_v8'] = pxq.most_common(30)
g4['pour_X_que_total_v8'] = sum(pxq.values())
for cand in ['autant', 'peu', 'tout', 'ce', 'et', 'veut']:
    g4[f'pour_{cand}_que_v8'] = pxq.get(cand, 0)
# same in primary
pxqp = collections.Counter()
for i in range(len(prim)-2):
    if prim[i] == 'pour' and prim[i+2] == 'que':
        pxqp[prim[i+1]] += 1
g4['pour_X_que_primary_top15'] = pxqp.most_common(15)
out['gate4'] = g4

# ---------- GATE 5: 48 verb/verb-stem vetoes ----------
g5 = {}
# verbs after 'on' in v8 (top 30)
on_fol = collections.Counter(v8t[i+1] for i in range(V8N-1) if v8t[i] == 'on')
g5['after_on_top30_v8'] = on_fol.most_common(30)
# words before 'pas' in v8 (top 30) — the verb slot
pre_pas = collections.Counter(v8t[i-1] for i in range(1, V8N) if v8t[i] == 'pas')
g5['before_pas_top30_v8'] = pre_pas.most_common(30)
# 'V pas' WITHOUT preceding 'ne' (within 2 back): should be ~0 in formal prose
bare = collections.Counter()
for i in range(2, V8N):
    if v8t[i] == 'pas' and v8t[i-2] != 'ne' and v8t[i-1] != "n'":
        # check v8t[i-2] is not ne either (ne X pas / ne pas X)
        bare[v8t[i-1]] += 1
g5['pas_without_ne_top15_v8'] = bare.most_common(15)
g5['pas_without_ne_total'] = sum(bare.values())
g5['pas_total_v8'] = v8t.count('pas')
# anachronism watchlist: verbs/senses post-1841 — sample checks of candidates
# that a successor might propose; report era counts (0 = veto-grade)
watch = ['fout', 'foutre', 'kiffer', 'bosser', 'choper', 'piger', 'rigoler',
         'délirer', 'assurer', 'gérer', 'acter', 'impacter', 'solutionner',
         'finaliser', 'initier', 'positionner', 'cadrer', 'briefer', 'débriefer']
g5['watchlist_v8'] = {w: v8t.count(w) for w in watch}
out['gate5'] = g5

# ---------- GATE 6: 'gouvernement' collocations ----------
g6 = {}
idx = [i for i, w in enumerate(v8t) if w == 'gouvernement']
g6['n_gouvernement_v8'] = len(idx)
g6['predecessors'] = collections.Counter(v8t[i-1] for i in idx if i > 0).most_common(15)
g6['successors'] = collections.Counter(v8t[i+1] for i in idx if i+1 < V8N).most_common(15)
g6['pre2_le'] = sum(1 for i in idx if i > 0 and v8t[i-1] == 'le')
g6['kwic'] = [' '.join(v8t[max(0,i-5):i+6]) for i in idx[:14]]
# 'gouverne' verb forms for the fork (a) gou|ver reading
g6['n_gouverne_v8'] = v8t.count('gouverne')
g6['n_gouvernent_v8'] = v8t.count('gouvernent')
out['gate6'] = g6

json.dump(out, open('g3456_out.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1)[:6000])
