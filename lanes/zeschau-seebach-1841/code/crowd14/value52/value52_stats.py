#!/usr/bin/env python3
"""value52 stats: Monte-Carlo allophone test, unigram kills, 5-gram repeat verify."""
import json, os, re, random
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
OUTDIR = os.path.join(LANE, 'code', 'crowd14', 'value52')

def load_stream():
    offsets = json.load(open(os.path.join(LANE, 'code', 'side-keyhunt', 'repaired_offsets.json')))
    pairs = []
    for line in open(os.path.join(LANE, 'data', 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line: continue
        lid, digits = line.split()
        digits = re.sub(r'\D', '', digits)
        d = digits[offsets.get(lid, 0):]
        for i in range(0, len(d) - 1, 2):
            pairs.append(int(d[i:i + 2]))
    assert len(pairs) == 1847
    return pairs

s = load_stream()
frames = []  # (pre, suc) for each 52/59 window
for i, v in enumerate(s):
    if v in (52, 59):
        frames.append((v, s[i-1] if i > 0 else None, s[i+1] if i < len(s)-1 else None))

def n_shared(fr):
    seen = {}
    for v, p, q in fr:
        seen.setdefault((p, q), set()).add(v)
    return sum(1 for vs in seen.values() if len(vs) == 2)

obs = n_shared(frames)
print('observed shared (pre,suc) frames:', obs)

random.seed(20261007)
labels = [v for v, _, _ in frames]
ctx = [(p, q) for _, p, q in frames]
N = 20000
ge = 0
for _ in range(N):
    lab = labels[:]
    random.shuffle(lab)
    if n_shared([(lab[k], ctx[k][0], ctx[k][1]) for k in range(len(lab))]) <= obs:
        ge += 1
print('MC P(n_shared <= %d | free-homophone label shuffle) = %.4f  (N=%d)' % (obs, ge/N, N))

# 5-gram repeat verify: 6 11 52 37 43
hits = [i for i in range(len(s)-4) if s[i:i+5] == [6, 11, 52, 37, 43]]
print('5-gram [6,11,52,37,43] hits:', hits)

# unigram rate checks (cipher) vs era word candidates
import unicodedata
FRENCH_CLEAN = ['guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
                'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
                'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
                'pozzo-di-borgo-correspondance-v1.txt',
                'levant-correspondence-1841-p3.txt', 'talleyrand-memoires-v1.txt',
                'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
                'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt']
WORD = re.compile(r"[a-z\xe0\xe2\xe4\xe9\xe8\xea\xeb\xee\xef\xf4\xf6\xf9\xfb\xfc\xff\xe7\u0153\xe6]+(?:'[a-z\xe0\xe2\xe4\xe9\xe8\xea\xeb\xee\xef\xf4\xf6\xf9\xfb\xfc\xff\xe7\u0153\xe6]+)*")
def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('\u2019', "'").replace('\u2018', "'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p: continue
            toks.append(p + "'" if i < len(parts) - 1 else p)
    return toks
toks = []
for f in FRENCH_CLEAN:
    toks += tokenize(open(os.path.join(LANE, 'code', 'side-period', 'corpus', f), encoding='utf-8', errors='replace').read())
Ntok = len(toks)
uni = Counter(toks)
for w in ['france', 'est', 'même', 'plus', 'que', 'pas', 'la']:
    print('era P(%s) = %.4f  (n=%d)' % (w, uni[w]/Ntok, uni[w]))
print('cipher P(52) = %.4f  (n=27/1847)' % (27/1847))
print('cipher P(59) = %.4f' % (27/1847))
# "la france" successors in era (for the 5-gram formula idea)
fol = Counter()
for i, t in enumerate(toks):
    if t == 'la' and i+2 < len(toks) and toks[i+1] == 'france':
        fol[toks[i+2]] += 1
print('era "la france X":', fol.most_common(10))

res = {'mc_p_le_obs': ge/N, 'mc_N': N, 'obs_shared': obs,
       'fivegram_hits': hits,
       'era_unigrams': {w: (uni[w], uni[w]/Ntok) for w in ['france', 'est', 'même', 'plus', 'que', 'pas', 'la']},
       'era_N': Ntok, 'era_la_france_suc': fol.most_common(10)}
json.dump(res, open(os.path.join(OUTDIR, 'value52_stats.json'), 'w'), indent=1)
print('wrote value52_stats.json')
