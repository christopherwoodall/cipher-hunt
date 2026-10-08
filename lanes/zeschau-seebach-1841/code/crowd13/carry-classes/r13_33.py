#!/usr/bin/env python3
"""R13-33 — 33's specific infinitive (council carry, WO7 class half).
Runs AFTER PREREG.md. Whole-word battery (Fork-W scope); checks R, T2
(pool-nv8 'pour X ce qui', F-E @936/@1630 with 21='ce' banked), T-D pool
fence re-check, J-C joint replication constraint for F-C.
"""
import sys, os, re, json
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
sys.path.insert(0, str(LANE / 'code/crowd8/frenchman'))
import util
from util import PAIRS, N

OUT = {'prereg': str(HERE / 'PREREG.md')}

def fail(msg):
    print('HALT:', msg); sys.exit(2)

# ---- byte-verify gate ----
pairs = ['%02d' % p for p in PAIRS]
FRAMES = {'F-A': [186, 1245], 'F-B': [408], 'F-C': [467, 1088], 'F-D': [846],
          'F-E': [936, 1630]}
EXPECT_SUC = {'F-A': '16', 'F-B': '01', 'F-C': '79', 'F-D': '96', 'F-E': '21'}
for cl, poss in FRAMES.items():
    for i in poss:
        if pairs[i] != '33' or pairs[i-1] != '00' or pairs[i+1] != EXPECT_SUC[cl]:
            fail('frame drift %s @%d: %s %s %s' % (cl, i, pairs[i-1], pairs[i], pairs[i+1]))
assert N == 1847, N
print('gate PASS: 8/8 "pour 33" frames verified, N=1847')
OUT['gate'] = 'PASS'

# ---- lane tokenizer verbatim (round-11 arm1248 / identifier33) ----
def tok(text):
    text = text.lower().replace('’', "'").replace('‘', "'")
    text = re.sub(r"([a-zà-ÿ])'([a-zà-ÿ])", r'\1 \2', text)
    return re.findall(r'[a-zà-ÿ]+', text)

def is_inf(w):
    return w.endswith(('er', 'ir', 're')) and len(w) > 3

CORP = str(LANE / 'code/side-period/corpus')
EXCLUDE = {'harvest-log.txt', 'adb-zeschau-heinrich-anton-von.txt'}
files = sorted(f for f in os.listdir(CORP)
               if f.endswith('.txt') and f not in EXCLUDE
               and not f.startswith('allgemeine-zeitung-'))
nov8_tok = []
pool_tok = []
for f in files:
    t = tok(open(os.path.join(CORP, f), encoding='utf-8', errors='replace').read())
    pool_tok.extend(t)
    if f == 'nesselrode-v8.txt':
        continue
    nov8_tok.extend(t)
assert len(pool_tok) == 3960009, len(pool_tok)
assert len(nov8_tok) > 3000000, len(nov8_tok)
print('pool tokens=%d; pool-minus-v8 tokens=%d' % (len(pool_tok), len(nov8_tok)))
OUT['pool_tokens'] = len(pool_tok)
OUT['pool_nov8_tokens'] = len(nov8_tok)

def pour_counts(t):
    c = Counter()
    for i in range(len(t) - 1):
        if t[i] == 'pour' and is_inf(t[i + 1]):
            c[t[i + 1]] += 1
    return c

c_pool = pour_counts(pool_tok)
c_nov8 = pour_counts(nov8_tok)
DROPS = {'notre': 'possessive adj', 'votre': 'possessive adj',
         'titre': 'noun', 'premier': 'adjective', 'ministre': 'noun',
         'quatre': 'numeral', 'maître': 'noun', 'homère': 'proper noun'}
raw = sorted(((x, c_pool[x]) for x in c_pool if c_pool[x] >= 3),
             key=lambda kv: -kv[1])
C = [(x, n) for x, n in raw if x not in DROPS]
assert len(C) == 461, len(C)  # round-12 JSON: 461 post-drop (469 raw, 8 drops)
OUT['n_candidates'] = len(C)

# ---- check R: top-10 by n("pour X") on pool-minus-v8, over C only ------
rank = sorted(((x, c_nov8.get(x, 0)) for x, _ in C), key=lambda kv: -kv[1])
R_top10 = [x for x, _ in rank[:10]]
EXPECTED = ['faire', 'être', 'avoir', 'aller', 'obtenir', 'donner', 'mettre',
            'assurer', 'arriver', 'atteindre']
OUT['R_top10'] = [{'inf': x, 'n': n} for x, n in rank[:10]]
if R_top10 != EXPECTED:
    fail('R top-10 drift: %s' % R_top10)
print('R drift gate PASS: top-10 identical to round-12')

# ---- check T2: n("pour X ce qui") on pool-minus-v8 (F-E arm) ----
t2 = Counter()
wins = {}
for i in range(len(nov8_tok) - 3):
    if (nov8_tok[i] == 'pour' and nov8_tok[i+2] == 'ce'
            and nov8_tok[i+3] == 'qui' and is_inf(nov8_tok[i+1])):
        x = nov8_tok[i+1]
        t2[x] += 1
        wins.setdefault(x, []).append(
            ' '.join(nov8_tok[max(0, i-4):i+7]))
t2_top = t2.most_common(12)
OUT['T2'] = {'query': 'n_pool_nov8("pour X ce qui")', 'n_total': sum(t2.values()),
             'top': [{'inf': x, 'n': n} for x, n in t2_top],
             'bar': 'unique argmax, n>=2'}
print('T2 total n("pour X ce qui") = %d' % sum(t2.values()))
for x, n in t2_top:
    print('   %5d  %s' % (n, x))
OUT['T2']['examples_argmax'] = (wins[t2_top[0][0]][:3] if t2_top else [])

# ---- check T-D: pool fence re-check "pour X par" + e-initial ----
td = 0
td_ex = []
for i in range(len(nov8_tok) - 3):
    if (nov8_tok[i] == 'pour' and is_inf(nov8_tok[i+1])
            and nov8_tok[i+2] == 'par' and nov8_tok[i+3][0] in 'eéèêë'):
        td += 1
        if len(td_ex) < 3:
            td_ex.append(' '.join(nov8_tok[i-3:i+5]))
OUT['T_D'] = {'query': 'n_pool_nov8("pour X par [e-word]")', 'n': td,
              'examples': td_ex, 'bar': 'expect 0 (fence re-check)'}
print('T-D n("pour X par [e-word]") pool-nv8 = %d' % td)

# ---- J-C: joint replication constraint datum ----
# Both F-C frames share one unknown infinitive (R1). Testable joint
# constraint with unglossed tails: candidate R-membership + supplementary
# anchors (@467: 96='par'-prov two pairs before 00; @1088: 29='er'-GT after 06).
OUT['J_C'] = {
    'frames': [467, 1088],
    'window_467_ctx': ' '.join(pairs[460:476]),
    'window_1088_ctx': ' '.join(pairs[1082:1102]),
    'note': ('tails (79,80,06) unglossed: no tail discriminates X. '
             'Joint constraint = one shared X across both frames (R1 '
             'replication datum); R-membership is the only mechanical filter. '
             'Anchor compat: @467 pre-context holds 96(=par-prov) two pairs '
             'before 00; @1088 post-context holds 29(=er-GT) after 06.')}
print('J-C contexts printed to JSON')

# ---- per-frame verdict table ----
# F-A: FENCED (R1/F81) — gate only. F-B/F-C: T n/a. F-D: fence re-check.
# F-E: T2 arm. A (hand-read anchor confirmation) is done by the executor,
# not the script; the script emits the windows for hand-read.
frames_tab = {}
for cl, poss in FRAMES.items():
    frames_tab[cl] = {'positions': poss,
                      'ctx': {i: ' '.join(pairs[max(0, i-6):i+8]) for i in poss}}
frames_tab['F-A']['verdict'] = 'FENCED (R1/F81 — not re-argued)'
frames_tab['F-B']['verdict'] = 'NULL (T n/a, tails unglossed)'
frames_tab['F-C']['verdict'] = 'NULL (T n/a; J-C replication datum holds)'
frames_tab['F-D']['verdict'] = ('FENCED-strong RE-CONFIRMED on pool-nv8' if td == 0
                                else 'FENCE BROKEN — %d hits' % td)
# F-E: T2 bar — unique argmax with n>=2?
if t2_top and (len(t2_top) == 1 or t2_top[0][1] > t2_top[1][1]) and t2_top[0][1] >= 2:
    frames_tab['F-E']['verdict'] = 'T2 FIRES for %s (n=%d); LEAN bar needs A + fork-compat' % t2_top[0]
    OUT['T2_fires'] = {'inf': t2_top[0][0], 'n': t2_top[0][1]}
else:
    frames_tab['F-E']['verdict'] = 'NULL (T2 no unique argmax with n>=2)'
    OUT['T2_fires'] = None
OUT['frames'] = frames_tab

with open(HERE / 'r13_33_results.json', 'w') as f:
    json.dump(OUT, f, indent=1, ensure_ascii=False)
print('wrote r13_33_results.json')
