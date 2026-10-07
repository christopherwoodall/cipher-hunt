#!/usr/bin/env python3
"""watch06 census: every 06 window with contact, 82->06 census, coincidence stats."""
import json, collections, sys, math
from pathlib import Path
sys.path.insert(0, str(Path.home()/'workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd8/frenchman'))
import util
from util import PAIRS, N, UNI, GT

PENCIL = {87:'ce', 64:'qui', 59:'est', 94:'ne', 77:'le'}
W06 = [579, 737, 1183, 1354]

p06 = util.positions(6)
print('N =', N)
print('n06 =', len(p06), '(expect 44)')
n82 = UNI[82]
print('n82 =', n82, 'P82 =', n82/N)

# full census: (i, pre, suc, prepre, sucsuc)
rows = []
for i in p06:
    pre = PAIRS[i-1] if i > 0 else None
    suc = PAIRS[i+1] if i+1 < N else None
    prepre = PAIRS[i-2] if i > 1 else None
    sucsuc = PAIRS[i+2] if i+2 < N else None
    rows.append((i, prepre, pre, suc, sucsuc))

def gloss(g):
    if g is None: return '--'
    t = GT.get(g, PENCIL.get(g))
    return f'{g}={t}' if t else str(g)

print('\n=== all 44 06-windows (i, prepre, pre, suc, sucsuc) ===')
for i, pp, pre, suc, ss in rows:
    mark = '  <<ISLET' if i in W06 else ''
    print(f'@{i}: {gloss(pp)} {gloss(pre)} [6] {gloss(suc)} {gloss(ss)}{mark}')

# 82->06 census (FIRE-PART check)
w82 = [i for i in p06 if i > 0 and PAIRS[i-1] == 82]
print('\n=== 82->06 windows:', w82, 'n =', len(w82))
extra = [i for i in w82 if i not in W06]
print('NOT on predicted W06 (partition defect):', extra)

# trigram 94-82-06 census
tri = [i for i in w82 if i > 1 and PAIRS[i-2] == 94]
print('94-82-06 trigrams (06 positions):', tri)

# pre/suc profiles
pre_c = collections.Counter(r[2] for r in rows)
suc_c = collections.Counter(r[3] for r in rows)
print('\npre profile:', dict(sorted(pre_c.items())))
print('suc profile:', dict(sorted(suc_c.items())))
print('\npre profile (glossed):', {gloss(k): v for k, v in sorted(pre_c.items())})
print('suc profile (glossed):', {gloss(k): v for k, v in sorted(suc_c.items())})

# coincidence: exact binomial P(X>=4) with p=n82/N, trials=n06
p = n82 / N
n = len(p06)
obs = len(w82)
pmf = sum(math.comb(n, k) * p**k * (1-p)**(n-k) for k in range(obs, n+1))
E = n * p
print(f'\n=== coincidence probe ===')
print(f'E[82->06] under independence = {E:.2f}; obs = {obs}; enrichment = {obs/E:.2f}x; exact P(X>={obs}) = {pmf:.4f}')

# successor profile: islet-4 vs other-40 (exact Fisher-ish: just report tables)
islet_suc = collections.Counter(PAIRS[i+1] for i in W06 if i+1 < N)
other_suc = collections.Counter(PAIRS[i+1] for i in p06 if i not in W06 and i+1 < N)
print('\nislet-4 suc profile:', {gloss(k): v for k, v in sorted(islet_suc.items())})
print('other-40 suc profile:', {gloss(k): v for k, v in sorted(other_suc.items())})
# Fisher exact on suc==82? trivial. Compare: proportion of suc in islet's suc-set
iset = set(islet_suc)
k_islet = 4
k_other = sum(v for k, v in other_suc.items() if k in iset)
print(f'other-40 windows sharing an islet successor group: {k_other}/40')

# islet windows: full ±4 context with glosses
print('\n=== islet window contexts (±4) ===')
for i in W06:
    print(f'@{i}:', util.window(i, w=4))

# @737 lone-82: what precedes 82@736?
print('\n=== @737 lone-82-06: extended contact ===')
print('pairs @730-742:', ' '.join(gloss(PAIRS[j]) for j in range(730, 743)))
