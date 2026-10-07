#!/usr/bin/env python3
"""@1248 non-finite arm-builder (round 10, WO4). Implements PREREG.md bars.

Candidates (Gate-4 compliant): C1 cela / C2 peu / C3 infinitive / C4 mediatrice-class.
Legs: L1 era frame rate (n_v8>=2) / L2 era constituency (read hits) /
      L3 cipher-side contact / L4 window coherence.
Plus: 62-WO3 blocker check (62 in @1248+-6?).
Writes: arm1248_results.json
"""
import json, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

# ---------- cipher side ----------
pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N

P = 1248
assert pairs[P] == '67' and pairs[P-1] == '00' and pairs[P+1] == '46', \
    (pairs[P-2:P+3],)
win = [(i, pairs[i]) for i in range(P-8, P+9)]

# board values (GT + provisional; mark status)
BOARD = {'11': ('la','GT'), '70': ('pre','GT'), '82': ('m','GT'),
         '34': ('i','GT'), '29': ('er','GT'), '40': ('e','GT'),
         '46': ('que','GT'), '87': ('ce','prov'), '64': ('qui','prov'),
         '96': ('par','prov'), '59': ('est','prov'), '77': ('le','prov-cond')}
def val(g):
    return '%s=%s' % (g, BOARD[g][0]) if g in BOARD else g
win_sub = [(i, val(pairs[i])) for i in range(P-8, P+9)]

# 67 full profile
fol = Counter(pairs[i+1] for i in range(N-1) if pairs[i] == '67')
pre = Counter(pairs[i-1] for i in range(1, N) if pairs[i] == '67')
pos67 = [i for i in range(N) if pairs[i] == '67']
n67 = len(pos67)
n67_to_46 = sum(1 for i in pos67 if i + 1 < N and pairs[i+1] == '46')

# 00->67 frames (F54 pour-islet licensing check for @1247)
pos00_67 = [i for i in range(1, N) if pairs[i] == '67' and pairs[i-1] == '00']

# ---------- 62-WO3 blocker ----------
win62 = [(i, pairs[i]) for i in range(P-6, P+7) if pairs[i] == '62']

# ---------- era side (vendored lane tokenizer + split) ----------
def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

def split_nesselrode():
    C = os.path.join(LANE, 'code', 'side-period', 'corpus')
    txt = open(os.path.join(C, 'nesselrode-v8.txt'), encoding='utf-8', errors='replace').read()
    months = 'janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre'
    pat = re.compile(r'^((?:Saint-Pétersbourg|Berlin|Paris|Londres|Vienne|Varsovie|Constantinople|Munich|Dresde)[ ,\.\u00a0]*\d{1,2}\s+(?:%s)\s+184[0-6])\.?,?\s*$' % months, re.M)
    bounds = [m.start() for m in pat.finditer(txt)]
    return [txt[a:b] for a, b in zip(bounds, bounds[1:] + [len(txt)])]

C = os.path.join(LANE, 'code', 'side-period', 'corpus')
v8_docs = split_nesselrode()
assert len(v8_docs) == 97, len(v8_docs)
levant = open(os.path.join(C, 'levant-correspondence-1841-p3.txt'),
              encoding='utf-8', errors='replace').read()
v8 = [tok(d) for d in v8_docs]
primary = v8 + [tok(levant)]
NW_v8 = sum(len(t) for t in v8)

def pour_star_que(docs):
    c = Counter()
    for t in docs:
        for i in range(len(t) - 2):
            if t[i] == 'pour' and t[i+2] == 'que':
                c[t[i+1]] += 1
    return c

middles_v8 = pour_star_que(v8)
middles_primary = pour_star_que(primary)

# infinitive-class: middles ending in -er/-ir/-re (heuristic) with n>=1
def is_inf(w):
    return w.endswith(('er', 'ir', 're')) and len(w) > 3
inf_v8 = {w: n for w, n in middles_v8.items() if is_inf(w)}
inf_primary = {w: n for w, n in middles_primary.items() if is_inf(w)}

# hit contexts for L2 constituency (word window +-12 around "pour X que")
def hits(docs, X, half=12):
    out = []
    for di, t in enumerate(docs):
        for i in range(len(t) - 2):
            if t[i] == 'pour' and t[i+1] == X and t[i+2] == 'que':
                lo, hi = max(0, i-half), i+3+half
                out.append(('doc%d' % di, ' '.join(t[lo:hi])))
    return out

hit_cela_v8 = hits(v8, 'cela')
hit_empecher_v8 = hits(v8, 'empêcher')
hit_peu_primary = hits(primary, 'peu')
hit_mediat_primary = hits(primary, 'médiatrice')

# cela contact class in v8 (for L3 no-contradiction)
cela_fol = Counter()
cela_pre = Counter()
for t in v8:
    for i, w in enumerate(t):
        if w == 'cela':
            if i + 1 < len(t): cela_fol[t[i+1]] += 1
            if i - 1 >= 0: cela_pre[t[i-1]] += 1
peu_fol = Counter(); peu_pre = Counter()
for t in v8:
    for i, w in enumerate(t):
        if w == 'peu':
            if i + 1 < len(t): peu_fol[t[i+1]] += 1
            if i - 1 >= 0: peu_pre[t[i-1]] += 1

# L1 bars
L1 = {
    'cela': middles_v8.get('cela', 0) >= 2,
    'peu': middles_v8.get('peu', 0) >= 2,
    'infinitive-class': sum(inf_v8.values()) >= 2,
    'mediatrice-class': middles_v8.get('médiatrice', 0) >= 2,
}

out = {
    'parse': {'N': N, 'window_P1248': ['%d:%s' % (i, g) for i, g in win],
              'window_sub': ['%d:%s' % (i, g) for i, g in win_sub]},
    'profile67': {'n67': n67, 'followers': dict(fol), 'predecessors': dict(pre),
                  'positions': pos67, 'n67_to_46': n67_to_46,
                  'pos00_67': pos00_67},
    'blocker62': {'window62': ['%d:%s' % (i, g) for i, g in win62]},
    'era': {'NW_v8': NW_v8, 'n_docs_v8': len(v8_docs),
            'middles_v8': dict(middles_v8),
            'middles_primary': dict(middles_primary),
            'inf_v8': inf_v8, 'inf_primary': inf_primary,
            'L1': L1,
            'n_cela_v8': middles_v8.get('cela', 0),
            'n_empecher_v8': middles_v8.get('empêcher', 0),
            'n_peu_v8': middles_v8.get('peu', 0),
            'n_peu_primary': middles_primary.get('peu', 0),
            'n_mediat_primary': middles_primary.get('médiatrice', 0),
            'cela_contact': {'followers': dict(cela_fol), 'predecessors': dict(cela_pre),
                             'n': sum(cela_fol.values())},
            'peu_contact': {'followers': dict(peu_fol), 'predecessors': dict(peu_pre),
                            'n': sum(peu_fol.values())}},
    'L2_hits': {'cela_v8': hit_cela_v8, 'empecher_v8': hit_empecher_v8,
                'peu_primary': hit_peu_primary, 'mediat_primary': hit_mediat_primary},
}
json.dump(out, open(os.path.join(HERE, 'arm1248_results.json'), 'w'), indent=1,
          ensure_ascii=False)
print('window:', ' '.join('%d:%s' % (i, g) for i, g in win_sub))
print('n67 =', n67, '| 67->46 elsewhere =', n67_to_46, '| 00->67 positions =', pos00_67)
print('62 in +-6:', win62)
print('middles_v8:', dict(middles_v8))
print('middles_primary:', dict(middles_primary))
print('inf_v8:', inf_v8, 'inf_primary:', inf_primary)
print('L1:', L1)
