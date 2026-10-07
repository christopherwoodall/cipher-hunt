#!/usr/bin/env python3
"""Round-8 FRENCHMAN step 2: 93='l'' allophony — fresh screen, {93,8}
homophony test, H_vow kill check, 62='on' chain."""
import json, collections, math
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import util
from util import PAIRS, N, UNI, GT, followers, predecessors, window, positions

VOWEL_GT = {34, 40, 29}
CONS_GT = {11, 70, 82, 46}
DET = {11, 87, 37}  # la, ce(prov), le(MEDIUM) — determiners l' must not follow

def shape(g):
    fol = followers(g); pre = predecessors(g)
    vow = sum(c for x, c in fol.items() if x in VOWEL_GT)
    cons = sum(c for x, c in fol.items() if x in CONS_GT)
    det_pre = sum(c for x, c in pre.items() if x in DET)
    return {'n': UNI[g], 'vow': vow, 'cons': cons, 'det_pre': det_pre,
            'fol': dict(fol), 'pre': dict(pre)}

print('=== fresh l\'-cell screen (n>=8, vow>=2, cons==0) ===')
cands = []
for g in range(100):
    s = shape(g)
    if s['n'] >= 8 and s['vow'] >= 2 and s['cons'] == 0:
        cands.append((g, s))
for g, s in sorted(cands, key=lambda r: -r[1]['vow']):
    print(f"g={g:3d} n={s['n']:3d} vow={s['vow']} cons={s['cons']} det_pre={s['det_pre']} "
          f"->62={s['fol'].get(62,0)} 94->={s['pre'].get(94,0)}")
    print(f"   fol: {dict(sorted(s['fol'].items(), key=lambda x:-x[1]))}")
    print(f"   pre: {dict(sorted(s['pre'].items(), key=lambda x:-x[1]))}")

for g in (93, 8, 14):
    s = shape(g)
    print(f"\n--- g={g} full: n={s['n']} vow={s['vow']} cons={s['cons']} det_pre={s['det_pre']}")
    print(' fol:', dict(sorted(s['fol'].items(), key=lambda x: -x[1])))
    print(' pre:', dict(sorted(s['pre'].items(), key=lambda x: -x[1])))

# ---- M_hom: {93,8} joint rate vs diplo ----
import re, glob
CORP = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus')
def tok_elision(text):
    text = text.replace('-\n','').replace('-\r\n','').lower()
    text = re.sub(r"[’‘`]", "'", text)
    text = re.sub(r"\b([a-zàâäéèêëîïôöùûüçœæ]+)'([a-zàâäéèêëîïôöùûüçœæ]+)", r"\1' \2", text)
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+'?|[a-zàâäéèêëîïôöùûüçœæ]+", text)
D = []
for f in sorted(glob.glob(os.path.join(CORP, '*.txt'))):
    if os.path.basename(f) in ('PROVENANCE.md','harvest-log.txt'): continue
    D.extend(tok_elision(open(f, encoding='utf-8', errors='replace').read()))
ND = len(D)
p_l = sum(1 for t in D if t=="l'")/ND
n_hom = UNI[93]+UNI[8]
E_hom = p_l*N
print(f"\n=== M_hom: n(93)+n(8)={n_hom} vs E_diplo={E_hom:.1f} (p_l'={p_l:.5f})")
# exact binomial two-sided-ish: P(X>=n) and P(X<=n)
from math import comb
def binom_p(n_, N_, p_, k_):
    return comb(N_, k_)*(p_**k_)*((1-p_)**(N_-k_))
# normal approx with continuity + exact lower tail via log-sum
import math
def log_tail(N_, p_, k_, upper=True):
    # exact via math.fsum of log-probs
    ls = []
    rng = range(k_, N_+1) if upper else range(0, k_+1)
    for k in rng:
        ls.append(math.lgamma(N_+1)-math.lgamma(k+1)-math.lgamma(N_-k+1)+k*math.log(p_)+(N_-k)*math.log(1-p_))
    m = max(ls)
    return math.exp(m)*math.fsum(math.exp(l-m) for l in ls)
print(' P(X<=%d) = %.4g   P(X>=%d) = %.4g' % (n_hom, log_tail(N, p_l, n_hom, False), n_hom, log_tail(N, p_l, n_hom, True)))
# ratio test (scale-free): n(93+8)/n(46) vs P(l')/P(que)
r_ciph = n_hom/UNI[46]
p_que = sum(1 for t in D if t=='que')/ND
print(f' ratio: cipher {n_hom}/{UNI[46]}={r_ciph:.3f} vs diplo P(l\')/P(que)={p_l/p_que:.3f}')
# single-cell 93 rate kill under diplo (exact)
print(' 93-alone: P(X<=14|E=%.1f) = %.4g' % (p_l*N, log_tail(N, p_l, 14, False)))

# ---- H_vow kill check: 93->62 with 62='on' fenced ----
print('\n=== H_vow (93 = l\' before front vowels only) ===')
print(' 93->62 =', shape(93)['fol'].get(62,0), ' ; 62="on" is fenced STRONG LEAD (N28/N35), "on" initial = back vowel o')
print(' -> H_vow KILLED unless 62!="on" (fence stands on independent legs)')

# ---- "ne l'" frames ----
print('\n=== ne-l\' frames ===')
for g in (93, 8):
    n94 = shape(g)['pre'].get(94, 0)
    print(f' 94->({g}) = {n94}')
    for i in positions(g):
        if i>0 and PAIRS[i-1]==94:
            print('   @%d: %s' % (i, window(i,3)))

# ---- l'on grammatical asymmetry (diplo) ----
nlil = sum(1 for i in range(ND-1) if D[i]=="l'" and D[i+1]=='il')
nlon = sum(1 for i in range(ND-1) if D[i]=="l'" and D[i+1]=='on')
print(f"\n=== diplo: l'+il bigrams = {nlil} (grammatical zero expected), l'+on = {nlon}")
# 62-chain: how many X->62 with X in {93,8}?
n_l62 = sum(1 for i in range(N-1) if PAIRS[i] in (93,8) and PAIRS[i+1]==62)
print(f' cipher: (93|8)->62 = {n_l62} windows')
for i in range(N-1):
    if PAIRS[i] in (93,8) and PAIRS[i+1]==62:
        print('   @%d: %s' % (i, window(i,4)))

# ---- complementary vs free: shared predecessors/followers of 93 vs 8 ----
s93, s8 = shape(93), shape(8)
pre93, pre8 = set(s93['pre']), set(s8['pre'])
fol93, fol8 = set(s93['fol']), set(s8['fol'])
print('\n=== 93 vs 8 distribution ===')
print(' shared predecessors:', pre93 & pre8, ' shared followers:', fol93 & fol8)
# same-position test: min distance between any 93 and 8 occurrence
p93, p8 = positions(93), positions(8)
print(' n93=%d n8=%d' % (len(p93), len(p8)))
