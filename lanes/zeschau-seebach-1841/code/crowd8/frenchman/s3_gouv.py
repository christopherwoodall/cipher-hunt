#!/usr/bin/env python3
"""Round-8 FRENCHMAN step 3: 77='gouv'/78='er' independent support + fork resolution."""
import json, re, glob, os, collections
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import util
from util import PAIRS, N, UNI, GT, followers, predecessors, window, positions

print('=== exact T4 windows (wide) ===')
for i in (1180, 1351):
    print(' @%d: %s' % (i-1, window(i-1, 6)))
    print('       labels:', [(PAIRS[j], GT.get(PAIRS[j], '?')) for j in range(i-1, i+7)])

print('\n=== 82->06 bigrams (all) ===')
for i in range(N-1):
    if PAIRS[i]==82 and PAIRS[i+1]==6:
        print(' @%d: %s' % (i, window(i, 4)))

print('\n=== 77->78 non-T4 windows (wide) ===')
for i in (7, 213, 647, 1077, 1542):
    print(' @%d: %s' % (i, window(i, 5)))

# diplo gouvernement family rates
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
DU = collections.Counter(D)
fam = {w: DU[w] for w in DU if w.startswith('gouvern')}
print('\n=== diplo gouvernement family ===')
for w, c in sorted(fam.items(), key=lambda x: -x[1])[:15]:
    print(f'  {w}: {c}  (P={c/ND:.2e})')
n_gouv = DU['gouvernement']
# despatch word count estimate: pairs->words scale via crib? use 1847 pairs, ~1.3 pairs/word (over-split) -> ~1420 words
for scale in (1.0, 1.3, 1.6):
    W = N/scale
    E = n_gouv/ND*W
    print(f'  scale {scale}: despatch ~{W:.0f} words, E[gouvernement]={E:.2f}')
# left collocates of gouvernement in diplo
pre = collections.Counter(D[i-1] for i in range(1,ND) if D[i]=='gouvernement')
print(' top left collocates:', pre.most_common(10))
fol = collections.Counter(D[i+1] for i in range(ND-1) if D[i]=='gouvernement')
print(' top right collocates:', fol.most_common(10))

# 37 profile (the @1180 left context)
print('\n=== 37 profile (n=%d) ===' % UNI[37])
print(' fol37:', dict(sorted(followers(37).items(), key=lambda x:-x[1])[:10]))
print(' pre37:', dict(sorted(predecessors(37).items(), key=lambda x:-x[1])[:10]))
# 37->77 ?
print(' 37->77 =', sum(1 for i in range(N-1) if PAIRS[i]==37 and PAIRS[i+1]==77))
# 48 profile (the @1351 left context)
print('\n=== 48 profile (n=%d): fol->77=%d ===' % (UNI[48], sum(1 for i in range(N-1) if PAIRS[i]==48 and PAIRS[i+1]==77)))
print(' fol48:', dict(sorted(followers(48).items(), key=lambda x:-x[1])[:12]))
# 52 after 06 @1351: 06->52 count
print('\n06->52 =', sum(1 for i in range(N-1) if PAIRS[i]==6 and PAIRS[i+1]==52),
      '| 06->06 =', sum(1 for i in range(N-1) if PAIRS[i]==6 and PAIRS[i+1]==6))
# unit inventory cutting rules
inv = json.load(open(os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd5/unit_inventory.json')))
print('\n=== unit inventory keys ===')
print(list(inv.keys())[:20] if isinstance(inv, dict) else type(inv))
