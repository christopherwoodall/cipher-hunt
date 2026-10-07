#!/usr/bin/env python3
"""U2: identify the l'-cell (ranked unblocker #2 for 62="on").

l' elides obligatorily before vowels (and h-muet). Cipher screen:
  X's GT-identified followers all vowel-initial {34=i,40=e,29=er} (>=2 such),
  X never before consonant-initial GT {11=la,70=pre,82=m,46=que}.
Era: n(l')=5333/221059 -> E[n(X)]~45. Discrimination payoff:
  P(pre=l' | w="on")=0.0619 -> E[X->62]=2.17; P(pre=l' | w="il")=0 (grammatical zero).
  Any X->62 >= 1 kills "il" (modulo X's identification); 0 is weak-adverse to "on".
"""
import json, collections
import util
from util import PAIRS, N, UNI, GT, followers, predecessors, window, positions

VOWEL_GT = {34, 40, 29}
CONS_GT = {11, 70, 82, 46}
eu, eb = util.era_counters()

print('era P(pre=l\'|il) =', round(eb[("l'", 'il')] / eu['il'], 5), '(expect 0)')
print('era P(pre=l\'|on) =', round(eb[("l'", 'on')] / eu['on'], 5))
print('era E[n(l\'-cell)] =', round(eu["l'"] / len(util.toks()) * N, 1))

cands = []
for g in range(100):
    n = UNI[g]
    if n < 8:  # l' is frequent; skip rare groups
        continue
    fol = followers(g); pre = predecessors(g)
    vow = sum(c for x, c in fol.items() if x in VOWEL_GT)
    cons = sum(c for x, c in fol.items() if x in CONS_GT)
    gt_id = vow + cons
    if vow >= 2 and cons == 0 and gt_id >= 2:
        # predecessor diversity (l' follows verbs/preps/nouns, not determiners)
        cands.append((g, n, vow, dict(sorted(fol.items(), key=lambda x: -x[1])[:6]),
                      dict(sorted(pre.items(), key=lambda x: -x[1])[:6]),
                      fol.get(62, 0)))
cands.sort(key=lambda r: -r[2])
print(f'\n{len(cands)} candidates:')
res = []
for g, n, vow, fol6, pre6, to62 in cands:
    # full vowel-fraction estimate: followers that are plausibly vowel-initial
    # (use GT only; rest unknown) -> report vow share among GT-identified
    print(f'g={g:3d} n={n:3d} ->VOWEL_GT={vow} ->62={to62}')
    print(f'   fol: {fol6}')
    print(f'   pre: {pre6}')
    res.append({'g': g, 'n': n, 'vow': vow, 'to62': to62,
                'fol': fol6, 'pre': pre6})

# discrimination test for each candidate
print('\n--- discrimination test X->62 ---')
for r in res:
    g, n, to62 = r['g'], r['n'], r['to62']
    # under "on": X->62 ~ Binomial(n62pos=35, 0.0619) but conditioned on X identified;
    # simpler: E = 35*0.0619 = 2.17 ; under "il": exactly 0
    print(f'g={g}: X->62 = {to62}  (E|on=2.17, E|il=0)')

json.dump(res, open('u2_lcell.json', 'w'), indent=1)
print('\nwrote u2_lcell.json')
