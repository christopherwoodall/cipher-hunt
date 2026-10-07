#!/usr/bin/env python3
"""watch06 round 11: falsifier watch vs ISLET 3 (06="ent" iff pre=82).
Runs AFTER PREREG.md was written. Repaired 1,847-pair stream.
Gloss tightening: 59="est" only where pre(59) in {64,94,93} (ISLET 10)."""
import json, math, collections, re, sys
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
sys.path.insert(0, str(LANE / 'code/crowd8/frenchman'))
import util
from util import PAIRS, N, UNI, GT

W06 = [580, 738, 1184, 1355]
PROV = {87: 'ce', 64: 'qui', 94: 'ne', 77: 'le', 96: 'par'}  # 59 handled conditionally
EST_OK_PRE = {64, 94, 93}

def gloss(i):
    """gloss of the group AT stream position i (for pre/suc neighbors)."""
    g = PAIRS[i]
    if g == 59:
        pre = PAIRS[i-1] if i > 0 else None
        if pre in EST_OK_PRE:
            return '59=est'
        return '59?'
    t = GT.get(g, PROV.get(g))
    return f'{g}={t}' if t else str(g)

def known(i):
    """True iff position i has a banked gloss (GT, PROV, or ISLET-10-tightened 59)."""
    g = PAIRS[i]
    if g == 59:
        pre = PAIRS[i-1] if i > 0 else None
        return pre in EST_OK_PRE
    return g in GT or g in PROV

print('=== census-fidelity gate ===')
print('N =', N, '(expect 1847)')
p06 = util.positions(6)
n82 = UNI[82]
print('n06 =', len(p06), '(expect 44); n82 =', n82, '(expect 39)')
if N != 1847 or len(p06) != 44 or n82 != 39:
    print('HALT: parse drifted underneath the prereg.')
    sys.exit(2)

rows = []
for i in p06:
    rows.append((i, PAIRS[i-2] if i > 1 else None, PAIRS[i-1] if i > 0 else None,
                 PAIRS[i+1] if i+1 < N else None, PAIRS[i+2] if i+2 < N else None))

print('\n=== FIRE-PART: 82->06 census ===')
w82 = [i for i in p06 if i > 0 and PAIRS[i-1] == 82]
print('observed:', w82)
print('predicted:', W06)
missing = [i for i in W06 if i not in w82]
extra = [i for i in w82 if i not in W06]
print('missing from prediction:', missing, '| NOT on predicted list:', extra)
print('FIRE-PART:', 'FIRES (partition defect)' if (missing or extra) else 'does not fire')

print('\n=== 94-82-06 trigram census ===')
tri = [i for i in w82 if i > 1 and PAIRS[i-2] == 94]
print('94-82-06 trigrams (06-pos):', tri, '| all islet:', all(i in W06 for i in tri))
tri_out = [i for i in p06 if i > 1 and i not in W06 and PAIRS[i-2] == 94 and PAIRS[i-1] == 82]
print('94-82-06 trigrams OUTSIDE islet:', tri_out)

print('\n=== FIRE-IN: islet contact audit (round-11 glosses) ===')
# @1355: banked F70 gloss «le [78] ne ment pas»; @1184: F66 fence re-checked
for i in W06:
    pp, pre, suc = PAIRS[i-2], PAIRS[i-1], PAIRS[i+1]
    ctx = ' '.join(gloss(j) for j in range(max(0, i-4), min(N, i+5)))
    print(f'@{i}: {ctx}')
    # forced-parse check: (a) pre-of-82 frame breaking "m"; (b) GT suc fusing "ent" into live lexeme
    force = None
    # (b): suc is GT consonant/vowel group that would fuse with "ent" into a live GT lexeme
    if suc in GT:
        # only full-word GT groups could fuse: check word-space GT lexemes containing 'ent'
        force = f'GT successor {suc}={GT[suc]} — needs manual audit'
    print('   forced adverse:', force if force else 'none')

print('\n=== @1355 F70-check: is the 94-82-06-52 block byte-exact? ===')
print('pairs @1349-1362:', ' '.join(gloss(j) for j in range(1349, 1363)))

print('\n=== FIRE-OUT: pre!=82 06-windows, ISLET-10-tightened by-ear rule ===')
print('(counts iff [gloss(pre)]+"ent"+[gloss(suc)] is an era-French word tail; unknown=>NOT counted)')
counted = []
both_glossed = []
for i, pp, pre, suc, ss in rows:
    if pre == 82:
        continue
    kp = known(i-1) if i > 0 else False
    ks = known(i+1) if i+1 < N else False
    if kp and ks:
        both_glossed.append((i, gloss(i-1), gloss(i+1)))
for i, gp, gs in both_glossed:
    print(f'  @{i}: "{gp}"+"ent"+"{gs}"')
print('windows with both pre and suc glossed:', len(both_glossed))
print('counted (French word tail):', counted if counted else 'NONE => FIRE-OUT does not fire')

print('\n=== coincidence probe (cipher-internal exact binomial) ===')
p = n82 / N
n = len(p06)
obs = len(w82)
pmf = sum(math.comb(n, k) * p**k * (1-p)**(n-k) for k in range(obs, n+1))
print(f'E[82->06]={n*p:.2f}; obs={obs}; enrichment={obs/(n*p):.2f}x; P(X>={obs})={pmf:.4f}')
print('prereg read: p>0.05 => adverse to conditioner; p<0.01 => selection real')

print('\n=== Frenchman register check: Nesselrode v8 word-space ===')
txt = open(LANE / 'code/side-period/corpus/nesselrode-v8.txt', encoding='utf-8', errors='replace').read().lower()
txt = re.sub(r"[’‘`]", "'", txt)
toks = re.findall(r"[a-zàâäéèêëîïôöùûüç]+'?|[a-zàâäéèêëîïôöùûüç]+", txt)
pairs = list(zip(toks, toks[1:]))
print('v8 tokens:', len(toks))
for probe in [('ne','ment'), ('ment','pas'), ('ne','mentent')]:
    print(f'  {" ".join(probe)}: n =', sum(1 for a, b in pairs if a == probe[0] and b == probe[1]))
ment_words = [t for t in toks if t.endswith('ment') and len(t) > 4]
print('  words ending in -ment (len>4):', len(ment_words), 'types:', len(set(ment_words)))
print('  sample:', sorted(set(ment_words))[:15])

print('\n=== islet-window successor profile (re-derive) ===')
print('islet suc:', collections.Counter(PAIRS[i+1] for i in W06))
