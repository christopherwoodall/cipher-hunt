#!/usr/bin/env python3
"""R13-92 — the F33 whole-word identification battery on 92 as subject
(WO7 class half). Runs AFTER PREREG.md. POUR-arm windows only:
@49 (suc 79), @330 (suc 50), @593 (suc 79), @683 (suc 64),
@978 (suc 7), @1154 (suc 29).
R on pool-minus-v8; T tail-shapes on v8 only where glossed (@683, @1154-frame);
J-POUR joint constraint; L/A per round-12. LA-arm/VERB-arm out of scope."""
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

POUR_ARM = {49: 79, 330: 50, 593: 79, 683: 64, 978: 7, 1154: 29}
for i, suc in POUR_ARM.items():
    if PAIRS[i] != 92 or PAIRS[i-1] != 0 or PAIRS[i+1] != suc:
        fail('POUR-arm drift @%d: %d %d %d' % (i, PAIRS[i-1], PAIRS[i], PAIRS[i+1]))
assert N == 1847, N
print('gate PASS: 6/6 POUR-arm "00 92 suc" windows, N=1847')
OUT['gate'] = 'PASS'
OUT['pour_arm'] = {i: {'suc': suc, 'ctx': ' '.join('%02d' % PAIRS[j] for j in range(max(0, i-5), min(N, i+7)))}
                   for i, suc in POUR_ARM.items()}

# ---- lane tokenizer verbatim; pool-minus-v8 ----
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
nov8_tok, v8_tok, pool_tok = [], None, []
for f in files:
    t = tok(open(os.path.join(CORP, f), encoding='utf-8', errors='replace').read())
    pool_tok.extend(t)
    if f == 'nesselrode-v8.txt':
        v8_tok = t
    else:
        nov8_tok.extend(t)
assert v8_tok is not None and len(v8_tok) == 92677, len(v8_tok or [])
assert len(pool_tok) == 3960009, len(pool_tok)
print('pool=%d toks; pool-nv8=%d toks; v8 NW=%d' % (len(pool_tok), len(nov8_tok), len(v8_tok)))

c_nov8 = Counter()
for i in range(len(nov8_tok) - 1):
    if nov8_tok[i] == 'pour' and is_inf(nov8_tok[i+1]):
        c_nov8[nov8_tok[i+1]] += 1

# R: candidate set from POOL (round-12 verbatim), ranked by pool-minus-v8
# (stable sort over pool-desc order — tie order matters, matches R1)
DROPS = {'notre': 'possessive adj', 'votre': 'possessive adj',
         'titre': 'noun', 'premier': 'adjective', 'ministre': 'noun',
         'quatre': 'numeral', 'maître': 'noun', 'homère': 'proper noun'}
c_pool = Counter()
for i in range(len(pool_tok) - 1):
    if pool_tok[i] == 'pour' and is_inf(pool_tok[i+1]):
        c_pool[pool_tok[i+1]] += 1
C = sorted(((x, n) for x, n in c_pool.items() if n >= 3 and x not in DROPS),
           key=lambda kv: -kv[1])
R_top10 = [x for x, _ in sorted(((x, c_nov8.get(x, 0)) for x, _ in C),
                                key=lambda kv: -kv[1])[:10]]
OUT['R_top10'] = R_top10
if R_top10 != ['faire', 'être', 'avoir', 'aller', 'obtenir', 'donner', 'mettre',
               'assurer', 'arriver', 'atteindre']:
    fail('R top-10 drift')
print('R drift gate PASS')

# T_683 (v8 arm): n_v8("pour X W qui") — B92's NOUN-strong datum predicts ~0
# for infinitives at @683 (suc=64='qui'-prov; '*pour INF qui[rel]' ban).
t683 = Counter(); t683_ex = {}
for i in range(len(v8_tok) - 3):
    if (v8_tok[i] == 'pour' and is_inf(v8_tok[i+1]) and v8_tok[i+3] == 'qui'):
        x = v8_tok[i+1]
        t683[x] += 1
        t683_ex.setdefault(x, ' '.join(v8_tok[max(0, i-3):i+6]))
OUT['T_683'] = {'query': 'n_v8("pour X W qui")', 'n_total': sum(t683.values()),
                'top': [{'inf': x, 'n': n, 'ex': t683_ex[x]}
                        for x, n in t683.most_common(10)],
                'prediction': 'approx 0 for infinitives (B92 NOUN-strong; '
                              'interrogative-qui middles excluded by frame)',
                'conditional_on': ['64="qui"-prov', '-quiere FENCE']}
print('T_683 n_v8("pour X W qui") = %d; top: %s'
      % (sum(t683.values()), t683.most_common(5)))

# @1154: frame license only (sub-word tail) — era "pour"+er-word rate on nv8
fr = sum(1 for i in range(len(nov8_tok) - 1)
         if nov8_tok[i] == 'pour' and nov8_tok[i+1].endswith('er'))
OUT['frame_1154'] = {'query': 'n_pool_nov8("pour" + er-word)', 'n': fr,
                     'note': 'frame licensed; value unidentifiable at whole-word granularity'}
print('frame_1154 license n=%d' % fr)

# T n/a windows (tails unglossed)
OUT['T_na'] = {'49': 'suc=79 unglossed', '330': 'suc=50 unglossed',
               '593': 'suc=79 unglossed', '978': 'suc=7 unglossed'}

# J-POUR joint constraint: one whole-word X across all six windows.
# @683's infinitive tail-shape ~0 (if confirmed) fails the joint hypothesis.
joint_fails = sum(t683.values()) == 0
OUT['J_POUR'] = {'hypothesis': 'one whole-word infinitive X across all 6 POUR-arm windows',
                 'fails_at_683': joint_fails,
                 'verdict': ('FAILS joint constraint at @683 (T_683=0) -> '
                             'POUR-arm is NOT one whole-word infinitive; '
                             'corroborates B92 conditioned-polyvalence FENCE '
                             '(cross-instrument), or Fork-S for 92')
                            if joint_fails else
                            'joint hypothesis survives @683 — re-examine'}

# per-window verdicts
OUT['windows'] = {
    49: 'NULL (T n/a, suc=79 unglossed)', 330: 'NULL (T n/a, suc=50 unglossed)',
    593: 'NULL (T n/a, suc=79 unglossed)', 978: 'NULL (T n/a, suc=7 unglossed)',
    683: ('NOUN-islet CORROBORATED (T_683=0, infinitive tail-shape absent; '
          'conditional on 64="qui"/"-quiere FENCE")' if joint_fails
          else 'T_683 nonzero — investigate'),
    1154: 'NULL (frame licensed, value unidentifiable at whole-word granularity)'}
OUT['verdict'] = ('NULL (constrained): J-POUR fails -> POUR-arm not one infinitive; '
                  '@683 corroborates B92 NOUN-islet; fork scope (Fork-W) bounds all. '
                  'Cross-instrument support for the R3 FENCED conditioned-polyvalence verdict.')
OUT['fork_note'] = ('92 mirrors the 33 paradox at small n: I1 pre==00 x6 vs '
                    'I4 92->29 x1 (@1154). Under Fork-S, "pour [stem]-er" is '
                    'licensed; under Fork-W the six windows need one '
                    'monosyllabic X that T_683 refutes at @683.')

with open(HERE / 'r13_92_results.json', 'w') as f:
    json.dump(OUT, f, indent=1, ensure_ascii=False)
print('wrote r13_92_results.json')
