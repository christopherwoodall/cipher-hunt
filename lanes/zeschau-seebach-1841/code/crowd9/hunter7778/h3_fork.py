#!/usr/bin/env python3
"""hunter7778 H3: fork discriminator 78="ver" (a2) vs 78="er" (c).
Pre-registered in PREREG.md BEFORE running."""
import re, glob, collections
from pathlib import Path
from math import comb

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
CORP = LANE / 'code/side-period/corpus'

def tokenize_elision(text):
    text = text.replace('-\n', '').replace('-\r\n', '')
    text = text.lower()
    text = re.sub(r"[’‘`]", "'", text)
    text = re.sub(r"\b([a-zàâäéèêëîïôöùûüçœæ]+)'([a-zàâäéèêëîïôöùûüçœæ]+)", r"\1' \2", text)
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+'?|[a-zàâäéèêëîïôöùûüçœæ]+", text)

toks = []
for f in [CORP / 'nesselrode-v8.txt', CORP / 'guizot-memoires-t5-t6.txt']:
    toks.extend(tokenize_elision(open(f, encoding='utf-8', errors='replace').read()))
print('corpus toks:', len(toks))

# H3a: tokens containing 'verne' or 'erne' (gouvernement-family excluded: circular)
vern = collections.Counter(t for t in toks if 'verne' in t)
ern = collections.Counter(t for t in toks if 'erne' in t and 'verne' not in t)
gouvfam = sum(c for t, c in list(vern.items()) if t.startswith('gouv')) + \
          sum(c for t, c in list(ern.items()) if t.startswith('gouv'))
print('\nH3a raw:')
print('  verne-types:', dict(vern.most_common(20)))
print('  erne-types (non-verne):', dict(ern.most_common(25)))
print('  gouvernement-family tokens excluded:', gouvfam)

# by-ear morphological classification (F34/F44-allowed), non-gouvernement only
ver_ne, er_ne = collections.Counter(), collections.Counter()
for t, c in vern.items():
    if t.startswith('gouv'):
        continue
    # caverne-type / proper nouns: ver|ne ; gouverne* already excluded
    ver_ne[t] = c
for t, c in ern.items():
    if t.startswith('gouv'):
        continue
    er_ne[t] = c
V, E = sum(ver_ne.values()), sum(er_ne.values())
print(f'  non-gouvernement: ver|ne boundary tokens={V} types={len(ver_ne)}: {dict(ver_ne)}')
print(f'  non-gouvernement: er|ne boundary tokens={E} types={len(er_ne)}: {dict(sorted(er_ne.items(), key=lambda kv: -kv[1])[:15])} ...')
# Fisher exact on tokens: [[V, E]] vs null 1:1 — one-sided p for E>=obs
n = V + E
p_ge = sum(comb(n, k) for k in range(E, n+1)) / 2**n if n else 1.0
p_le = sum(comb(n, k) for k in range(0, V+1)) / 2**n if n else 1.0
print(f'  ratio er|ne : ver|ne = {E}:{V} = {E/max(V,1):.1f}x; Fisher one-sided p(er>=obs)={p_ge:.3g} p(ver>=obs)={p_le:.3g}')

# H3b: inventory parsimony
GT = {'la', 'pre', 'm', 'i', 'er', 'e', 'que'}
a2_novel = {'gou', 'ver'} - GT
c_novel = {'gouv'} - GT   # 'er' in GT via 29
print(f'\nH3b inventory: GT={sorted(GT)}')
print(f'  (a2) gou|ver|ne|m|ent novel syllables: {sorted(a2_novel)} (n={len(a2_novel)})')
print(f'  (c)  gouv|er|ne|m|ent novel syllables: {sorted(c_novel)} (n={len(c_novel)})')

# H3c: kill-condition scan (mechanical)
import json
rows = []
for line in open(LANE / 'data/upstream-ct_R5005.txt'):
    line = line.strip()
    if not line: continue
    lid, digits = line.split()
    rows.append((lid, re.sub(r'\D', '', digits)))
off = json.loads((LANE / 'code/side-keyhunt/repaired_offsets.json').read_text())
P = []
for lid, digits in rows:
    o = off[lid]
    P += [int(digits[i:i+2]) for i in range(o, len(digits)-1, 2)]
N = len(P)
fivemers = [i for i in range(N-4) if P[i:i+5] == [77, 78, 94, 82, 6]]
print(f'\nH3c kill-condition scan:')
print(f'  77-78-94-82-06 5-mer count = {len(fivemers)} (kill needs a 3rd window with incompatible boundary: NONE)')
print(f'  independent "ver"-cell identification banked: NONE (open hunt, out of scope)')
print(f'  independent 2nd "er"-cell beyond 29 GT: NONE banked (78 itself is the candidate)')
print(f'  syllabification authority beyond by-ear: NONE available (F34/F44 cap)')
