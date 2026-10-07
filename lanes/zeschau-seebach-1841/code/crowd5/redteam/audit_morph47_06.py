#!/usr/bin/env python3
"""RED TEAM audit of Morphologist's round-5 WO1/WO2/WO3 (47=ce, 06 stem, 06/86)."""
import json, math, sys
from pathlib import Path
from collections import Counter
from math import comb

LANE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(LANE / 'code' / 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
seq = [int(g) for g in pairs]; n = len(seq)
assert n == 1847
big = Counter(zip(seq[:-1], seq[1:]))
cf = Counter(seq)

print('=== WO1: 47=ce ===')
n47 = cf[47]
print('n47 =', n47)
# Q2 partition: check ALL 28 frames for feature overlap
pos47 = [i for i,g in enumerate(seq) if g==47]
ce_feat = frag_feat = 0
overlap = []
for i in pos47:
    pre = seq[i-1] if i>0 else None
    suc = seq[i+1] if i+1<n else None
    has_ce = (suc in (46,11)) or (pre==96)
    has_frag = (suc==78) or (pre==29)
    if has_ce: ce_feat += 1
    if has_frag: frag_feat += 1
    if has_ce and has_frag: overlap.append(i)
print(f'frames with ce-features: {ce_feat}, with frag-features: {frag_feat}, overlap: {overlap}')
print('(worker: 6 ce, 9 frag, 0 overlap)')
# Q1: 47->64, 87->64, 87->46 by pre
print('47->64 =', big[(47,64)], '| 87->64 =', big[(87,64)], '| 87->46 =', big[(87,46)])
p87_46_pre96 = sum(1 for i in range(n-2) if seq[i]==96 and seq[i+1]==87 and seq[i+2]==46)
print('96-87-46 =', p87_46_pre96, '(all 87->46 have pre=96:', p87_46_pre96==big[(87,46)], ')')
p47_46 = [i for i in range(n-1) if seq[i]==47 and seq[i+1]==46]
print('47->46 @', p47_46, 'pres:', [seq[i-1] for i in p47_46])
# Fisher for [[5,0],[0,2]]
p_fisher = comb(5,5)*comb(2,0)/comb(7,5)
print(f'Fisher one-sided [[5,0],[0,2]] = {p_fisher:.4f} (claim 0.0476)')
# binomial 47->64=0/28 vs era P(qui|ce)=0.188
print(f'binom P(0/28 | p=0.188) = {(1-0.188)**28:.4f} (claim 0.0029)')
print(f'binom P(0/28 | p=5/32) = {(1-5/32)**28:.4f} (claim 0.0086)')
# C2: 29->47 positions
c2 = [i for i in range(n-1) if seq[i]==29 and seq[i+1]==47]
print('29->47 @', c2, '(= Q2 pre==29 frames:', all(seq[i+1]==47 and seq[i]==29 for i in c2), ')')
c29_87 = [i for i in range(n-1) if seq[i]==29 and seq[i+1]==87]
print('29->87 @', c29_87, 'n =', len(c29_87), '(claim 3)')
# unigram: .md says 4.11x / 2.79x; JSON says 2.13 / 1.446
print('P(47) =', round(n47/n,5))

print('\n=== WO2: 06 stem ===')
print('n06 =', cf[6])
f0629 = [i for i in range(n-1) if seq[i]==6 and seq[i+1]==29]
f8629 = [i for i in range(n-1) if seq[i]==86 and seq[i+1]==29]
print('06->29 @', f0629, '| 86->29 @', f8629)
print('rate: 44/957*1000 =', round(44/957*1000,2), '/1000w (claim 45.98)')

print('\n=== WO3: 06/86 ===')
print('00->86 =', big[(0,86)], '| 00->06 =', big[(0,6)])
print('06->11 =', big[(6,11)], '| 06->77 =', big[(6,77)], '| 06->00 =', big[(6,0)])
print('86->11 =', big[(86,11)], '| 86->77 =', big[(86,77)], '| 86->00 =', big[(86,0)])
p86 = Counter(seq[i-1] for i in range(1,n) if seq[i]==86)
p06 = Counter(seq[i-1] for i in range(1,n) if seq[i]==6)
print('P86[00] =', p86[0], '| 00 in P06:', 0 in p06)
# Fisher [[0,12],[44,20]]
num = comb(12,0)*comb(64,44)/comb(76,44)  # one-sided, a=0
# two-sided via hypergeometric sum of <= P(obs)
from math import comb as C
def hyper(a):
    return C(12,a)*C(64,44-a)/C(76,44)
p_obs = hyper(0)
p_two = sum(hyper(a) for a in range(0,13) if hyper(a) <= p_obs+1e-18)
print(f'Fisher [[0,12],[44,20]] one-sided = {p_obs:.3e} (claim 7.3e-06)')
# binomial P(>=12/32) at p=55/1847
p0 = 55/1847
sf = sum(C(32,j)*p0**j*(1-p0)**(32-j) for j in range(12,33))
print(f'binom P(>=12/32 | p={p0:.4f}) = {sf:.3e} (claim 6.3e-11)')
print('enrichment:', round((12/32)/p0,2))
