#!/usr/bin/env python3
"""Round-6 CLOSER: WO-A (84 from the 87-side) + WO-B (00="pour" battery).

WO-A: given 87=ce / 64=qui / 77=le (provisional), what does the
87-64-77-84 window (@1800-1803, plus 64-77-84 x3) demand of 84?
WO-B: full >=2-check battery for 00="pour" (F40 lead, not adjudicated).

Cipher: repaired 1,847-pair parse (code/crowd4/repaired_parse.py).
Era: Tocqueville t1+t2, elision-split word model (round-5 convention).
F30-legal: word-space legs only; no syllable-conditional legs on fragments.
All cipher numbers re-derived here; nothing invented.
"""

import collections, json, math, os, re, sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847
cf = collections.Counter(pairs)
cbi = collections.Counter(zip(pairs, pairs[1:]))
cpre = collections.defaultdict(collections.Counter)  # followers: cpre[a][b]
csuc = collections.defaultdict(collections.Counter)  # predecessors: csuc[b][a]
for a, b in zip(pairs, pairs[1:]):
    cpre[a][b] += 1
    csuc[b][a] += 1
rank = {g: r + 1 for r, (g, _) in enumerate(cf.most_common())}

def occ(g):
    return [i for i, x in enumerate(pairs) if x == g]

def window(i, w=4):
    lo, hi = max(0, i - w), min(N, i + w + 1)
    return [(j, pairs[j]) for j in range(lo, hi)]

# ---------------- era: elision-split word model ----------------
def load_era_words():
    words = []
    for fn in ('gutenberg-30513-tocqueville-t1.txt',
               'gutenberg-30514-tocqueville-t2.txt'):
        txt = open(os.path.join(DATA, fn), encoding='utf-8').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', txt)
        words += re.findall(r'[a-z\u00e0-\u00ff]+', txt)
    return words

words = load_era_words()
wu = collections.Counter(words)
wb = collections.Counter(zip(words, words[1:]))
wN = len(words)
we = collections.defaultdict(collections.Counter)  # followers we[a][b]
for a, b in zip(words, words[1:]):
    we[a][b] += 1

# infinitive heuristic for the B2 candidate-set analysis
INF_STOP = {'mer', 'hier', 'cher', 'fer', 'amer', 'enfer', 'cuiller', 'cuill\u00e8re',
            'b\u00e9lier', 'atelier', 'escalier', 'grenier', 'panier', 'papier',
            'premier', 'dernier', 'entier', 'fier', 'altier', 'grossier',
            'léger', 'leger', 'étranger', 'etranger', 'passager', 'messager',
            'boulanger', 'fromager', 'berger', 'verger', 'danger', 'manger',
            'songer', 'longer', 'ranger', 'venger', 'plonger', 'allonger'}
def is_inf(tok):
    return (re.search(r'(er|ir|oir|re|dre|tre)$', tok) is not None
            and tok not in INF_STOP and len(tok) > 3)

R = {'work_orders': {}}

# =====================================================================
# WO-A: 84 from the 87-side
# =====================================================================
A = {}
n84 = cf['84']
A['n84'] = n84
A['rank84'] = rank['84']
A['P84'] = n84 / N
A['P84_given_77'] = cbi[('77', '84')] / cf['77']
A['pos_77_84'] = [i for i in range(N - 1) if pairs[i] == '77' and pairs[i+1] == '84']
A['followers84'] = dict(cpre['84'].most_common())
A['predecessors84'] = dict(csuc['84'].most_common())
A['n_84_59'] = cbi[('84', '59')]
A['n_46_84'] = cbi[('46', '84')]
A['pos_46_84'] = [i for i in range(N - 1) if pairs[i] == '46' and pairs[i+1] == '84']
A['n_84_29'] = cbi[('84', '29')]
# 64-77-84 trigrams
A['pos_647784'] = [i for i in range(N - 2)
                   if pairs[i] == '64' and pairs[i+1] == '77' and pairs[i+2] == '84']
A['pos_64778459'] = [i for i in range(N - 3)
                     if pairs[i:i+4] == ['64', '77', '84', '59']]
A['windows84'] = {i: window(i) for i in occ('84')}

# --- Leg A1: era inventory of X in "qui le X" (word-space grammar) ---
# Given 87=ce ^ 64=qui ^ 77=le: the frame is "ce qui le X". What fills X in era?
inv = collections.Counter()
inv_ce = collections.Counter()
for i in range(len(words) - 2):
    if words[i] == 'qui' and words[i+1] == 'le':
        inv[words[i+2]] += 1
        if i > 0 and words[i-1] == 'ce':
            inv_ce[words[i+2]] += 1
A['era_qui_le_n'] = sum(inv.values())
A['era_qui_le_top'] = inv.most_common(25)
A['era_ce_qui_le_n'] = sum(inv_ce.values())
A['era_ce_qui_le_top'] = inv_ce.most_common(25)
# verb test: heuristic - 3sg present verb forms are the grammatical filler.
# Use a POS-free proxy: X is "verb-like" if it also occurs as words[i] with
# prev in {il, elle, on, ce, qui} ... simpler: report the raw inventory and
# hand-grade the top items in the .md. Also count how many distinct X.
A['era_qui_le_distinct'] = len(inv)

# --- Leg A2: conditional kills of the A4 inversion candidates in the frame ---
cands = ['plus', 'm\u00eame', 'leur', 'sur']
A['era_qui_le_cand'] = {c: inv.get(c, 0) for c in cands}
A['era_n_qui'] = wu['qui']
A['era_n_le'] = wu['le']

# --- Leg A3: GT-anchored "que 84" check: era inventory after "que" ---
qinv = collections.Counter()
for i in range(len(words) - 1):
    if words[i] == 'que':
        qinv[words[i+1]] += 1
A['era_que_n'] = sum(qinv.values())
A['era_que_top'] = qinv.most_common(20)
A['era_que_distinct'] = len(qinv)
# verb-proxy after "que": X in {soit} or X tagged by infinitive heuristic or
# X in a small 3sg-verb probe list
probe_verbs = ['soit', 'vienne', 'fasse', 'dise', 'prenne', 'veuille', 'puisse',
               'doive', 'sache', 'aille', 'concerne', 'touche', 'regarde']
A['era_que_probe'] = {v: qinv.get(v, 0) for v in probe_verbs}
A['era_n_que'] = wu['que']

# 59 profile (for the 84->59 x4 frame; secondary)
A['n59'] = cf['59']
A['rank59'] = rank['59']
A['followers59'] = dict(cpre['59'].most_common(12))
A['predecessors59'] = dict(csuc['59'].most_common(12))
A['n_59_46'] = cbi[('59', '46')]
A['pos_59'] = occ('59')
R['work_orders']['WO-A_84'] = A

# =====================================================================
# WO-B: 00="pour" battery
# =====================================================================
B = {}
n00 = cf['00']
B['n00'] = n00
B['rank00'] = rank['00']
B['P00'] = n00 / N
B['n_00_46'] = cbi[('00', '46')]
B['pos_00_46'] = [i for i in range(N - 1) if pairs[i] == '00' and pairs[i+1] == '46']
B['P46_given_00'] = B['n_00_46'] / n00
B['n_00_86'] = cbi[('00', '86')]
B['n_00_06'] = cbi[('00', '06')]
B['n_06_00'] = cbi[('06', '00')]
B['pos_06_00'] = [i for i in range(N - 1) if pairs[i] == '06' and pairs[i+1] == '00']
B['followers00'] = dict(cpre['00'].most_common(15))
B['predecessors00'] = dict(csuc['00'].most_common(15))
# 87-11-00 frame (A5 structural datum)
B['pos_8711'] = [i for i in range(N - 1) if pairs[i] == '87' and pairs[i+1] == '11']
B['n_8711_00'] = sum(1 for i in B['pos_8711'] if i + 2 < N and pairs[i+2] == '00')
B['pos_8711_00'] = [i for i in B['pos_8711'] if i + 2 < N and pairs[i+2] == '00']
B['P00_given_8711'] = B['n_8711_00'] / len(B['pos_8711'])
B['n_00_11'] = cbi[('00', '11')]
B['n_00_77'] = cbi[('00', '77')]
B['n_00_01'] = cbi[('00', '01')]
B['windows_00_46'] = {i: window(i) for i in B['pos_00_46']}
B['windows_06_00'] = {i: window(i) for i in B['pos_06_00']}

# --- Leg B1: rate ---
B['era_P_pour'] = wu['pour'] / wN
B['era_n_pour'] = wu['pour']
B['era_rank_pour'] = None
erank = {w: r + 1 for r, (w, _) in enumerate(wu.most_common())}
B['era_rank_pour'] = erank['pour']
B['ratio_P00_vs_pour'] = B['P00'] / B['era_P_pour']
B['era_P_sans'] = wu['sans'] / wN
B['era_P_apres'] = wu['apr\u00e8s'] / wN
B['ratio_P00_vs_sans'] = B['P00'] / B['era_P_sans']
B['ratio_P00_vs_apres'] = B['P00'] / B['era_P_apres']

# --- Leg B2: the governor frame. Era candidate set: words taking "que" AND bare infinitive ---
cand = {}
for w0, n0 in wu.most_common():
    if n0 < 30:
        break
    q = we[w0].get('que', 0)
    inf = sum(c for t2, c in we[w0].items() if is_inf(t2))
    if q >= 3 and inf >= 3:
        cand[w0] = {'n': n0, 'n_que': q, 'n_inf': inf,
                    'Pque': q / n0, 'Pinf': inf / n0}
B['era_que_inf_candidates'] = cand
# spot-check the actual infinitive followers for the top candidates
B['era_inf_followers'] = {}
for w0 in ('pour', 'sans', 'apr\u00e8s', 'avant', 'afin'):
    fl = [(t2, c) for t2, c in we[w0].most_common(40) if is_inf(t2)]
    B['era_inf_followers'][w0] = fl[:12]

# --- Leg B3: "pour que" bigram ---
B['era_n_pour_que'] = wb[('pour', 'que')]
B['era_Pque_given_pour'] = B['era_n_pour_que'] / wu['pour']
B['ratio_P46g00_vs_era'] = B['P46_given_00'] / B['era_Pque_given_pour']

# --- Leg B4: rival grammatical kills (era-0 bigram checks) ---
rivals = ['\u00e0', 'a', 'de', 'en', 'par', 'sans', 'apr\u00e8s', 'avant',
          'afin', 'pendant', 'dans', 'sur', 'avec', 'd\u00e8s']
rkill = {}
for r0 in rivals:
    nq = wb.get((r0, 'que'), 0)
    ninf = sum(c for t2, c in we[r0].items() if is_inf(t2))
    rkill[r0] = {'era_n': wu[r0], 'era_n_que': nq, 'era_n_inf': ninf}
B['rival_grammatical'] = rkill

# --- Adverse: "cela pour" frame ---
B['era_n_cela_pour'] = wb[('cela', 'pour')]
B['era_n_cela'] = wu['cela']
B['era_Ppour_given_cela'] = B['era_n_cela_pour'] / wu['cela'] if wu['cela'] else 0
B['ratio_P00g8711_vs_era'] = (B['P00_given_8711'] / B['era_Ppour_given_cela']
                              if B['era_Ppour_given_cela'] else None)

# 00 predecessor verb-profile (conditional on 06=verb-stem provisional): list preds
B['pred00_full'] = dict(csuc['00'].most_common())

R['work_orders']['WO-B_00pour'] = B
R['meta'] = {
    'parse': 'repaired 1847 pairs',
    'era': 'Tocqueville t1+t2 elision-split word model',
    'era_words': wN,
    'note': 'F30-legal word-space legs only; band 0.5-2.0 UNCALIBRATED per F20',
}

with open(os.path.join(LANE, 'code', 'crowd6', 'closer',
                       'closer87_00_results.json'), 'w') as f:
    json.dump(R, f, indent=1, ensure_ascii=False)
print('wrote JSON')

# ---------- console digest ----------
print('--- WO-A ---')
print('n84=%d rank=%d P=%.4f P(84|77)=%.4f n77_84=%d' % (
    A['n84'], A['rank84'], A['P84'], A['P84_given_77'], len(A['pos_77_84'])))
print('64-77-84 @', A['pos_647784'])
print('64-77-84-59 @', A['pos_64778459'])
print('84->59 x%d  46->84 x%d @%s  84->29 x%d' % (
    A['n_84_59'], A['n_46_84'], A['pos_46_84'], A['n_84_29']))
print('era "qui le X": n=%d distinct=%d' % (A['era_qui_le_n'], A['era_qui_le_distinct']))
print('top:', A['era_qui_le_top'][:12])
print('"ce qui le X": n=%d top:' % A['era_ce_qui_le_n'], A['era_ce_qui_le_top'][:12])
print('inversion cands in frame:', A['era_qui_le_cand'])
print('era "que"->X: n=%d distinct=%d top:' % (A['era_que_n'], A['era_que_distinct']),
      A['era_que_top'][:10])
print('probe verbs after que:', A['era_que_probe'])
print('n59=%d rank=%d 59->46 x%d preds:' % (A['n59'], A['rank59'], A['n_59_46']),
      A['predecessors59'])
print('--- WO-B ---')
print('n00=%d rank=%d P=%.4f' % (B['n00'], B['rank00'], B['P00']))
print('00->46 x%d P=%.4f | 00->86 x%d 00->06 x%d | 06->00 x%d @%s' % (
    B['n_00_46'], B['P46_given_00'], B['n_00_86'], B['n_00_06'],
    B['n_06_00'], B['pos_06_00']))
print('era P(pour)=%.4f (n=%d rank=%d) ratio=%.2f' % (
    B['era_P_pour'], B['era_n_pour'], B['era_rank_pour'], B['ratio_P00_vs_pour']))
print('ratio vs sans=%.1f vs apres=%.1f' % (B['ratio_P00_vs_sans'], B['ratio_P00_vs_apres']))
print('que+inf candidates:', {k: (v['n'], v['n_que'], v['n_inf']) for k, v in cand.items()})
print('P(que|pour) era=%.4f cipher P(46|00)=%.4f ratio=%.2f' % (
    B['era_Pque_given_pour'], B['P46_given_00'], B['ratio_P46g00_vs_era']))
print('rivals:', {k: (v['era_n'], v['era_n_que'], v['era_n_inf']) for k, v in rkill.items()})
print('87-11-00 x%d/%d P=%.3f | era P(pour|cela)=%.4f ratio=%s' % (
    B['n_8711_00'], len(B['pos_8711']), B['P00_given_8711'],
    B['era_Ppour_given_cela'], B['ratio_P00g8711_vs_era']))
print('00 followers:', B['followers00'])
print('00 preds:', B['predecessors00'])
