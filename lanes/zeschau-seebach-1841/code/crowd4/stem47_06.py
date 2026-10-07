"""Round-4 STEM HUNTER: (a) resolve 47, (b) identify the 06 stem.

All counts re-derived from data/upstream-ct_R5005.txt + offsets (R5005 only).
Era: Tocqueville t1+t2, WORD-SPACE legs only (F30).
"""
import json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from syllabary4 import (load_pairs, followers, predecessors, windows,
                        ngram_count, era_unigram, era_p_next, era_bigram_n,
                        era_p_after)

pairs = load_pairs()
N = len(pairs)
F47 = followers(pairs, '47'); P47 = predecessors(pairs, '47')
n47 = pairs.count('47')
print(f'n47={n47} N={N} f47={n47/N:.5f}')

# ---- the 802x number, recomputed --------------------------------------
n96 = pairs.count('96')
c96_21 = ngram_count(pairs, ['96', '21'])
c96_47 = ngram_count(pairs, ['96', '47'])
e_me_given_par = era_p_next('me', 'par')
print(f'96->21 x{c96_21}: cipher P={c96_21/n96:.4f} vs era P(me|par)={e_me_given_par:.6f} ratio={(c96_21/n96)/e_me_given_par:.1f}x')
print(f'96->47 x{c96_47}: cipher P={c96_47/n96:.4f} vs era P(me|par)={e_me_given_par:.6f} ratio={(c96_47/n96)/e_me_given_par:.1f}x')
print('era n(par,me)=', era_bigram_n('par', 'me'))
print('era n(par,ce)=', era_bigram_n('par', 'ce'))

# ---- candidate battery for 47 (word-space, F30-legal) ------------------
# legs: A unigram | B1 P(que|w) vs 47->46 x3 | B2 P(la|w) vs 47->11 x3
#       B3 P(me|w) vs 47->78 x5 (78=me LEAD) | C1 P(w|par) vs 96->47 x1
#       C2 P(w|prev-ends-er) vs 29->47 x4
cands = ['me', 'mes', 'met', 'mais', 'ce', 'le', 'les', 'en', 'ne', 'se',
         'même', 'dans', 'plus', 'bien', 'tout', 'on', 'il', 'elle', 'nous',
         'vous', 'lui', 'leur', 'y', 'mon', 'ma', 'son', 'sa', 'quel',
         'cette', 'ces', 'des', 'du', 'de', 'est', 'sont', 'ont', 'fait',
         'dit', 'peu', 'point', 'pas', 'mêmes', 'tel', 'telle', 'mien']
print(f"\n{'w':8} {'A:uni':>7} {'B1:que':>8} {'B2:la':>8} {'B3:me':>8} {'C1:w|par':>9} {'C2:w|..er':>9}")
rows = []
for w in cands:
    A = (n47 / N) / era_unigram(w) if era_unigram(w) > 0 else float('inf')
    B1 = (F47['46'] / n47) / era_p_next('que', w)
    B2 = (F47['11'] / n47) / era_p_next('la', w)
    B3 = (F47['78'] / n47) / era_p_next('me', w)
    C1 = (P47['96'] / n47) / era_p_next(w, 'par')
    C2 = (P47['29'] / n47) / era_p_after(w, 'er')
    rows.append((w, A, B1, B2, B3, C1, C2))
    print(f'{w:8} {A:7.2f} {B1:8.2f} {B2:8.2f} {B3:8.2f} {C1:9.2f} {C2:9.2f}')

json.dump({'n47': n47, 'N': N, 'followers47': dict(F47), 'pred47': dict(P47),
           'c96_21': c96_21, 'c96_47': c96_47, 'n96': n96,
           'battery': [dict(zip(['w','A','B1','B2','B3','C1','C2'], r)) for r in rows]},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'stem47_battery.json'), 'w'), indent=1)
