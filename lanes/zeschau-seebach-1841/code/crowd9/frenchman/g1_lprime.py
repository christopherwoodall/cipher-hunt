#!/usr/bin/env python3
"""GATE 1: {93,8}='l'' — 'ne l'est' @101-103 frame + B1 shape + joint rate."""
import json, sys, collections
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import corpus9
sys.path.insert(0, str(corpus9.LANE / 'code/crowd8/frenchman'))
from util import PAIRS, N, GT, positions, followers, window

out = {}
t = corpus9.load('primary')
eu, eb, et = corpus9.counters('primary')
out['primary_tokens'] = len(t)

# 1a. 'ne l'est' frame era counts
out['ne_l_est'] = corpus9.ngram_count('primary', 'ne', "l'", 'est')
out['ne_l_est_pas'] = corpus9.ngram_count('primary', 'ne', "l'", 'est', 'pas')
out['ne_l_est_guere'] = corpus9.ngram_count('primary', 'ne', "l'", 'est', 'guère')
out['l_est'] = corpus9.ngram_count('primary', "l'", 'est')
out['ne_l'] = eb[('ne', "l'")]
out['l_prime_total'] = eu["l'"]
# P(l') for rate bar
out['P_lprime'] = eu["l'"] / len(t)
out['E_93_8'] = out['P_lprime'] * 1847
out['n_93_8'] = len(positions(93)) + len(positions(8))
# scale-free ratio test n(93+8)/n(46) vs P(l')/P(que)
out['n46'] = sum(1 for p in PAIRS if p == 46)
out['ratio_cipher'] = out['n_93_8'] / out['n46']
out['ratio_era'] = out['P_lprime'] / (eu['que'] / len(t))

# 1b. B1 shape: followers of 93 and 8 — all vowel-initial or 62?
# vowel-initial GT: 34=i, 40=e, 29=er. consonant-initial GT: 11=la,70=pre,82=m,46=que
VOW = {34, 40, 29}
CONS = {11, 70, 82, 46}
for g in (93, 8):
    fol = followers(g)
    bad = {k: v for k, v in fol.items() if k in CONS}
    vow = {k: v for k, v in fol.items() if k in VOW}
    other = {k: v for k, v in fol.items() if k not in VOW and k not in CONS}
    out[f'shape_{g}'] = {
        'n': sum(fol.values()), 'vowel_GT': vow, 'consonant_GT_BAD': bad,
        'other_unknown': other, 'to_62': fol.get(62, 0)}
    out[f'windows_{g}'] = [(i, window(i, 2)) for i in positions(g)]

# 1c. kwic of 'ne l' est' for the report
out['kwic_ne_l_est'] = corpus9.kwic('primary', "l'", width=5, limit=0)  # placeholder
kw = []
tt = corpus9.load('primary')
for i in range(len(tt)-3):
    if tt[i] == 'ne' and tt[i+1] == "l'" and tt[i+2] == 'est' and len(kw) < 12:
        kw.append(' '.join(tt[max(0,i-4):i+5]))
out['kwic_ne_l_est'] = kw

json.dump(out, open('g1_out.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in out.items() if not k.startswith('windows') and k != 'kwic_ne_l_est'}, ensure_ascii=False, indent=1))
print('\nkwic ne/l\'/est:')
for k in kw: print('  ', k)
