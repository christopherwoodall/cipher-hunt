#!/usr/bin/env python3
"""Round-12 work order 1: 33-INFINITIVE IDENTIFIER. Implements PREREG.md.

Battery: the 8 "pour 33" frames -> which infinitive follows "pour" at each
frame, via era "pour [inf]" rates (clean 3.96M pool minus v8) + v8 tail-shape
queries + frame-license checks. Hand-review step (check A) is done by the
executor AFTER this script, reading v8 contexts directly.
Writes: code/crowd12/identifier33/identifier33_results.json
"""
import json, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N

# ---------- verify battery frames (0-based, repaired) ----------
FRAMES = {
    'F-A': [186, 1245],   # 00 33 16 00
    'F-B': [408],          # 00 33 01 02
    'F-C': [467, 1088],    # 00 33 79 80
    'F-D': [846],          # 00 33 96 40
    'F-E': [936, 1630],    # 00 33 21 64
}
EXPECT_SUC = {'F-A': '16', 'F-B': '01', 'F-C': '79', 'F-D': '96', 'F-E': '21'}
for cl, poss in FRAMES.items():
    for i in poss:
        assert pairs[i] == '33', (cl, i, pairs[i])
        assert pairs[i - 1] == '00', (cl, i, pairs[i - 1])
        assert pairs[i + 1] == EXPECT_SUC[cl], (cl, i, pairs[i + 1])
print('frames verified: 8/8 "pour 33" windows, N=1847')

# ---------- lane tokenizer verbatim (round-11 arm1248) ----------
def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

def is_inf(w):
    return w.endswith(('er', 'ir', 're')) and len(w) > 3

CORP = os.path.join(LANE, 'code', 'side-period', 'corpus')
EXCLUDE = {'harvest-log.txt', 'adb-zeschau-heinrich-anton-von.txt'}
files = sorted(f for f in os.listdir(CORP)
               if f.endswith('.txt') and f not in EXCLUDE
               and not f.startswith('allgemeine-zeitung-'))

pool_tok, v8_tok = [], None
for f in files:
    t = tok(open(os.path.join(CORP, f), encoding='utf-8', errors='replace').read())
    pool_tok.extend(t)
    if f == 'nesselrode-v8.txt':
        v8_tok = t
assert v8_tok is not None
NW = len(v8_tok)
assert NW == 92677, NW
print('clean pool tokens=%d (target 3960009); v8 NW=%d' % (len(pool_tok), NW))
assert len(pool_tok) == 3960009, len(pool_tok)

# pool minus v8 (disjoint corpus for check R)
nov8_tok = []
for f in files:
    if f == 'nesselrode-v8.txt':
        continue
    nov8_tok.extend(tok(open(os.path.join(CORP, f), encoding='utf-8', errors='replace').read()))

def pour_counts(t):
    c = Counter()
    for i in range(len(t) - 1):
        if t[i] == 'pour' and is_inf(t[i + 1]):
            c[t[i + 1]] += 1
    return c

c_pool = pour_counts(pool_tok)
c_nov8 = pour_counts(nov8_tok)
n_pour_pool = sum(1 for i in range(len(pool_tok) - 1) if pool_tok[i] == 'pour')
print('pool: n("pour")=%d, distinct pour-inf types=%d' % (n_pour_pool, len(c_pool)))

# ---------- candidate set C (mechanical) ----------
# hand-reviewed drops (non-infinitive false positives of is_inf); run once
# with DROPS empty, inspect, then fill with reasons and re-run.
DROPS = {
    'notre': 'possessive adjective ("pour notre + noun" is grammatical; not an infinitive)',
    'votre': 'possessive adjective ("pour votre + noun"); not an infinitive',
    'titre': 'noun; "pour titre" ungrammatical as infinitive (boundary artifact)',
    'premier': 'adjective; "pour premier" ungrammatical',
    'ministre': 'noun; "pour ministre" ungrammatical as infinitive',
    'quatre': 'numeral; not an infinitive',
    'maître': 'noun; not an infinitive',
    'homère': 'proper noun (Homer); not an infinitive',
}
raw_cands = [(x, c_pool[x]) for x in c_pool if c_pool[x] >= 3]
raw_cands.sort(key=lambda kv: -kv[1])
C = [(x, n) for x, n in raw_cands if x not in DROPS]
print('raw candidates (n>=3): %d; after drops: %d' % (len(raw_cands), len(C)))
for x, n in raw_cands[:40]:
    mark = '  DROP' if x in DROPS else ''
    print('  %6d  %s%s' % (n, x, mark))

# ---------- check R: top-10 by n("pour X") on pool-minus-v8, over C only ------
rank_nov8 = sorted(((x, c_nov8.get(x, 0)) for x, _ in C),
                   key=lambda kv: -kv[1])
R_top10 = [x for x, _ in rank_nov8[:10]]
print('R top-10 (pool-v8, post-drop):', R_top10)

# ---------- check T / L: v8 tail-shape queries ----------
def n_gram_tail(pat):
    """pat: list with 'INF' slot and literals/'W' wildcards/'EWORD'."""
    out = Counter()
    L = len(pat)
    for i in range(len(v8_tok) - L + 1):
        ok = True
        inf = None
        for j, p in enumerate(pat):
            w = v8_tok[i + j]
            if p == 'INF':
                if not is_inf(w):
                    ok = False; break
                inf = w
            elif p == 'W':
                pass
            elif p == 'EWORD':
                if not (w and w[0] in 'eé'):
                    ok = False; break
            else:
                if w != p:
                    ok = False; break
        if ok:
            out[inf] += 1
    return out

T = {}
T['F-A'] = n_gram_tail(['pour', 'INF', 'W', 'pour'])
T['F-D'] = n_gram_tail(['pour', 'INF', 'par', 'EWORD'])       # cond. 96="par"
T['F-D-fallback'] = n_gram_tail(['pour', 'INF', 'W', 'W'])     # unconditional
T['F-E'] = n_gram_tail(['pour', 'INF', 'W', 'qui'])           # cond. 64="qui"
T['F-E-fallback'] = n_gram_tail(['pour', 'INF', 'W', 'W'])
T['F-BC-fallback'] = n_gram_tail(['pour', 'INF', 'W', 'W'])
# supplementary pre-context "cela pour X" for F-A@1245 / F-C@467
T['cela-pour'] = n_gram_tail(['cela', 'pour', 'INF'])

def argmax_unique(counter, thresh=2):
    if not counter:
        return None, 0, []
    top = counter.most_common(3)
    if len(top) > 1 and top[0][1] == top[1][1]:
        return None, top[0][1], [w for w, _ in top if _ == top[0][1]]
    if top[0][1] < thresh:
        return None, top[0][1], []
    return top[0][0], top[0][1], []

results = {
    'meta': {
        'N_pairs': N, 'v8_NW': NW, 'pool_tokens': len(pool_tok),
        'n_pour_pool': n_pour_pool,
        'frames': {k: {'positions': v, 'suc': EXPECT_SUC[k]} for k, v in FRAMES.items()},
        'drops': DROPS,
    },
    'candidates': [{'inf': x, 'n_pool': n, 'n_pool_nov8': c_nov8.get(x, 0)}
                   for x, n in C],
    'R_top10_pool_nov8': [{'inf': x, 'n': c_nov8[x]} for x in R_top10],
    'clusters': {},
}
for cl in ['F-A', 'F-B', 'F-C', 'F-D', 'F-E']:
    key = {'F-A': 'F-A', 'F-D': 'F-D', 'F-E': 'F-E'}.get(cl)
    entry = {'positions': FRAMES[cl], 'suc': EXPECT_SUC[cl]}
    if key:
        cnt = T[key]
        lic = sum(cnt.values())
        amax, an, ties = argmax_unique(cnt)
        entry['T'] = {'query': key, 'license_n': lic,
                      'argmax': amax, 'argmax_n': an, 'ties': ties,
                      'top5': cnt.most_common(5)}
        entry['L_pass'] = lic >= 1
    else:
        entry['T'] = None  # tail unglossed: T cannot fire
        entry['L_pass'] = None
    # R overlap: which candidates are in R top-10
    entry['R_candidates_in_top10'] = [x for x, _ in C if x in R_top10][:10]
    results['clusters'][cl] = entry

results['fallback'] = {
    'F-D-generic-pour-INF-W1W2': T['F-D-fallback'].most_common(5),
    'F-E-generic-pour-INF-W1W2': T['F-E-fallback'].most_common(5),
    'cela-pour-INF': T['cela-pour'].most_common(10),
}
# argmax of fallbacks for the record
for k in ['F-D-fallback', 'F-E-fallback', 'cela-pour']:
    amax, an, ties = argmax_unique(T[k])
    results['fallback'][k + '-argmax'] = {'argmax': amax, 'n': an, 'ties': ties}

out = os.path.join(HERE, 'identifier33_results.json')
json.dump(results, open(out, 'w'), ensure_ascii=False, indent=1)
print('wrote', out)
