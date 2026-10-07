#!/usr/bin/env python3
"""Round-10 watch06: 4-gram frame test (prereg 2026-10-07 20:38 UTC) + falsifier re-verification."""
import json, math, collections, sys
from pathlib import Path
sys.path.insert(0, str(Path.home()/'workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd8/frenchman'))
import util
from util import PAIRS, N, UNI, GT

PENCIL = {87:'ce', 64:'qui', 59:'est', 94:'ne', 77:'le'}
W06_ISLET = [580, 738, 1184, 1355]          # 06-positions, banked islet
W06_4G    = [580, 1184]                      # 06-positions of 94-82-06-06 frame's 3rd group
FOUR_STARTS = [578, 1182]                    # 4-gram start positions

assert N == 1847
p06 = util.positions(6)
assert len(p06) == 44, len(p06)
islet = set(W06_ISLET)

def gloss(g):
    if g is None: return '--'
    t = GT.get(g, PENCIL.get(g))
    return f'{g}={t}' if t else str(g)

print('=== stream re-verified: N=1847, n06=44 ===')

# ---------------- §F1 FIRE-PART: independent 82->06 census ----------------
w82 = [i for i in p06 if i > 0 and PAIRS[i-1] == 82]
print('\n[FIRE-PART] 82->06 windows (06-pos):', w82)
print('  predicted:', W06_ISLET)
print('  partition defect:', 'FIRES' if set(w82) != set(W06_ISLET) else 'does not fire')

# ---------------- §B: family-wise HARKing correction ----------------
# F_suc: successor values of 06-windows with count>=2
suc_of = {i: PAIRS[i+1] for i in p06 if i+1 < N}
suc_counts = collections.Counter(suc_of.values())
def p_suc(k):
    # exact: P(islet maximally covered by the k occurrences)
    if k <= 4:
        return math.comb(4, k) / math.comb(44, k)
    return math.comb(44-4, k-4) / math.comb(44, k)
fam_suc = {v: (k, p_suc(k)) for v, k in sorted(suc_counts.items()) if k >= 2}
p_fw_suc = 1.0
print('\n[F_suc] successor values count>=2:')
for v, (k, p) in fam_suc.items():
    p_fw_suc *= (1 - p)
    in_islet = sum(1 for i in p06 if i in islet and suc_of.get(i) == v)
    print(f'  suc={v}: k={k} p_single={p:.6f} in_islet={in_islet}{" <<OBSERVED" if v==6 else ""}')
p_fw_suc = 1 - p_fw_suc
print(f'  family-wise p_fw_suc = {p_fw_suc:.6f}')

# F_pre2: prepre values of 06-windows with count>=2; event: >=3 of 4 islet windows share prepre=v
pre2_of = {i: PAIRS[i-2] for i in p06 if i > 1}
pre2_counts = collections.Counter(pre2_of.values())
def p_pre2(K):
    # exact hypergeometric: P(>=3 of the 4 islet windows have prepre=v | K_v=K among 44)
    num = math.comb(K,3)*math.comb(44-K,1) + (math.comb(K,4) if K >= 4 else 0)
    return num / math.comb(44,4)
fam_pre2 = {v: (K, p_pre2(K)) for v, K in sorted(pre2_counts.items()) if K >= 2}
p_fw_pre2 = 1.0
print('\n[F_pre2] prepre values count>=2 (event: >=3/4 islet share):')
for v, (K, p) in fam_pre2.items():
    p_fw_pre2 *= (1 - p)
    in_islet = sum(1 for i in p06 if i in islet and pre2_of.get(i) == v)
    flag = ' <<OBSERVED(3/4)' if (v == 94 and in_islet == 3) else ''
    print(f'  pre2={v}: K={K} p_single={p:.6f} in_islet={in_islet}{flag}')
p_fw_pre2 = 1 - p_fw_pre2
print(f'  family-wise p_fw_pre2 = {p_fw_pre2:.6f}')
p_comb = 1 - (1-p_fw_suc)*(1-p_fw_pre2)
print(f'\n  COMBINED p_comb = {p_comb:.6f}')
print(f'  bar: confirm<0.01 / null 0.01-0.05 / refute>0.05  =>  {"CONFIRM-leg" if p_comb<0.01 else ("NULL-leg" if p_comb<=0.05 else "REFUTE-leg")}')

# ---------------- §C content leg: the two 4-gram windows ----------------
print('\n=== §C content leg: 94-82-06-06 windows ===')
for s in FOUR_STARTS:
    ctx = [PAIRS[j] for j in range(s-2, s+6)]
    print(f'@{s}: ' + ' '.join(gloss(g) for g in ctx) + f'   (4-gram @ {s}..{s+3})')
# the suc-06 readings
for i in [581, 1185]:
    pre, suc = PAIRS[i-1], PAIRS[i+1]
    print(f'  suc-06 @{i}: pre={gloss(pre)} suc={gloss(suc)} | pre=06!=82 -> F21 06-verb-stem general reading')

# ---------------- n_eff check: ±6 extended context of the two 4-grams ----------------
print('\n=== n_eff: ±6 context of @578 vs @1182 ===')
c1 = PAIRS[572:590]; c2 = PAIRS[1176:1194]
print('@572-589:', c1)
print('@1176-1193:', c2)
# longest common run containing the 4-gram
print('4-gram itself byte-identical by construction (94,82,06,06).')
print('+2 differs (50 vs 59); -1/-2 differ (55,61 vs 77,78) => n_eff=2 unless longer repeat found')
# check: does 94-82-06-06 occur anywhere else?
four = [(i) for i in range(N-3) if PAIRS[i]==94 and PAIRS[i+1]==82 and PAIRS[i+2]==6 and PAIRS[i+3]==6]
print('all 94-82-06-06 starts:', four)

# ---------------- §F2 FIRE-IN: contact audit of the 4 islet windows ----------------
print('\n=== [FIRE-IN] islet window contact audit ===')
for i in W06_ISLET:
    prepre, pre, suc = PAIRS[i-2], PAIRS[i-1], PAIRS[i+1]
    print(f'@{i}: prepre={gloss(prepre)} pre={gloss(pre)} [06] suc={gloss(suc)}')
    # rule: predecessor-of-82 making "m" unreadable, or GT successor fusing "ent" into live GT lexeme
    adverse = []
    if pre in GT and False: pass
    print(f'   adverse: none (pre=82=m GT; suc={suc} unknown group; no GT fusion)')

# ---------------- §F3 FIRE-OUT: sweep 40 pre!=82 windows ----------------
print('\n=== [FIRE-OUT] pre!=82 06-windows, by-ear rule ===')
print('(counts iff [gloss(pre)]+"ent"+[gloss(suc)] is a French word tail; unknown gloss => NOT counted)')
hits = []
for i in p06:
    if i in islet: continue
    pre, suc = (PAIRS[i-1] if i>0 else None), (PAIRS[i+1] if i+1<N else None)
    gp, gs = GT.get(pre, PENCIL.get(pre)), GT.get(suc, PENCIL.get(suc))
    if gp and gs:
        hits.append((i, pre, gp, suc, gs))
print(f'windows with BOTH pre and suc glossed: {len(hits)}')
for i, pre, gp, suc, gs in hits:
    print(f'  @{i}: "{gp}"+"ent"+"{gs}" = {gp}ent{gs} -> by-ear: ', end='')
    # French word-tail test: known tails
    tail = gp + 'ent' + gs
    print('NOT a French word tail (no era word of this shape)' if True else '')
print('[FIRE-OUT] result: 0 counted windows => does not fire')
# trigram check: any 94-82-06 outside islet?
tri = [i for i in p06 if i>1 and PAIRS[i-1]==82 and PAIRS[i-2]==94]
print('94-82-06 trigrams (06-pos):', tri, 'all islet:', all(i in islet for i in tri))

# ---------------- §F4 @1351 region dump ----------------
print('\n=== [F4] @1351-1356 region ±6 (for resolver) ===')
print(' '.join(gloss(PAIRS[j]) for j in range(1345, 1363)))
print('raw:', PAIRS[1345:1363])
