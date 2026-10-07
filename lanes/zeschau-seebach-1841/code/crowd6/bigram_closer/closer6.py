#!/usr/bin/env python3
"""Round 6 — BIGRAM CLOSER executor (77="le" exploitation).

Three threads on the REPAIRED canonical 1,847-pair parse:
 (a) Identify 84 — the «ce qui [verbe] 84» slot (87-64-77-84 @1800-1803;
     84="fait" killed 6.7x).
 (b) Test the "le me"x7 dependency — 77->78 x7 vs 78="me"-syllable-LEAD
     dissolution (F38); classify every instance on the repaired stream.
 (c) Drag 78-windows — test 45="me" (78->45 x4).

F30: no era-syllable-conditional legs on morphological fragments; era
word-space legs survive. N22 exclusions enforced (29/82/34 all legs;
40 conditionals). Kill rule: cipher n>=3 AND era count 0. Band 0.5-2.0
UNCALIBRATED (context only).

Writes: closer6.json, closer6.md
"""
import sys, os, json, re, math, collections

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(HERE, '..', '..')
LANE = os.path.join(CODE, '..')
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, os.path.join(CODE, 'crowd4'))
from repaired_parse import load_pairs_repaired

EXCLUDED_ALL = {'29', '82', '34'}
EXCLUDED_COND = {'40'}

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N
CF = collections.Counter(pairs)
CBI = collections.Counter(zip(pairs, pairs[1:]))

def positions_bigram(a, b):
    return [i for i in range(N - 1) if pairs[i] == a and pairs[i + 1] == b]

def positions_seq(seq):
    L = len(seq)
    return [i for i in range(N - L + 1) if pairs[i:i + L] == seq]

def window(i, r=3):
    return pairs[max(0, i - r):i + r + 1]

def fol(g):
    return collections.Counter(pairs[i + 1] for i in range(N - 1) if pairs[i] == g)

def pre(g):
    return collections.Counter(pairs[i - 1] for i in range(1, N) if pairs[i] == g)

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - m) / d, (c + m) / d)

def binom_le(k, n, p):
    if p <= 0: return 1.0 if k >= 0 else 0.0
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i)
               for i in range(0, k + 1))

# ---------------- era word-space model (Tocqueville t1+t2, elision-split) ------
def load_era_words():
    words = []
    for fn in ('gutenberg-30513-tocqueville-t1.txt',
               'gutenberg-30514-tocqueville-t2.txt'):
        txt = open(os.path.join(DATA, fn), encoding='utf-8').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', txt)
        words += re.findall(r'[a-z\u00e0-\u00ff]+', txt)
    return words

W = load_era_words()
RAW = W
WU = collections.Counter(W)
WB = collections.Counter(zip(W, W[1:]))
WT = collections.Counter(zip(W, W[1:], W[2:]))
WN = len(W)

def inband(r):
    return r is not None and 0.5 <= r <= 2.0

out = {'npairs': N, 'legs': {}}

# ============ baseline extension: re-derived key numbers =====================
base = out['baseline_rederive'] = {}
for g in ('77', '78', '84', '45', '59', '64', '87', '94', '82', '86', '46', '06', '67', '96'):
    base[f'n{g}'] = CF[g]
base['77->78'] = len(positions_bigram('77', '78'))
base['78->45'] = len(positions_bigram('78', '45'))
base['94->82'] = len(positions_bigram('94', '82'))
base['77->86'] = len(positions_bigram('77', '86'))
base['84->59'] = len(positions_bigram('84', '59'))
base['64->77'] = len(positions_bigram('64', '77'))
base['77->84'] = len(positions_bigram('77', '84'))
base['78->94'] = len(positions_bigram('78', '94'))
base['59->46'] = len(positions_bigram('59', '46'))
base['46->59'] = len(positions_bigram('46', '59'))
base['pos_77->86'] = positions_bigram('77', '86')
base['pos_94->82'] = positions_bigram('94', '82')
base['pos_64-77-84'] = positions_seq(['64', '77', '84'])
base['pos_87-64-77-84'] = positions_seq(['87', '64', '77', '84'])
base['pos_64-77-84-59'] = positions_seq(['64', '77', '84', '59'])
base['pos_77-78-94-82-06'] = positions_seq(['77', '78', '94', '82', '06'])
base['pos_78->45'] = positions_bigram('78', '45')

# ============ THREAD (a): identify 84 ========================================
a = out['legs']['a_identify_84'] = {}
a['n84'] = CF['84']
a['rank84'] = sorted(CF.values(), reverse=True).index(CF['84']) + 1
a['pos84'] = [i for i, p in enumerate(pairs) if p == '84']
a['followers84'] = dict(fol('84').most_common())
a['predecessors84'] = dict(pre('84').most_common())
a['windows84_r2'] = {str(i): window(i, 2) for i in a['pos84']}

# A1: era inversion — what follows "qui le" in word space?
# cipher: 87-64-77 = ce-qui-le, so 84 = W in era "ce qui le W" / "qui le W"
tri_qil = collections.Counter()
for (w1, w2, w3) in zip(RAW, RAW[1:], RAW[2:]):
    if w1 == 'qui' and w2 == 'le':
        tri_qil[w3] += 1
tri_cqil = collections.Counter()
for (w1, w2, w3) in WT:
    if w1 == 'ce' and w2 == 'qui' and False:
        pass
# "ce qui le W" needs a 4-gram
WQ = collections.Counter(zip(W, W[1:], W[2:], W[3:]))
cqil = collections.Counter()
for (w1, w2, w3, w4) in zip(W, W[1:], W[2:], W[3:]):
    if (w1, w2, w3) == ('ce', 'qui', 'le'):
        cqil[w4] += 1
a['A1_era_qui_le_followers'] = tri_qil.most_common(25)
a['A1_era_ce_qui_le_followers'] = cqil.most_common(15)
# unigram test for the top candidates vs P(84)
p84 = CF['84'] / N
a1u = a['A1_unigram_band'] = {}
for w, _ in tri_qil.most_common(12):
    pw = WU[w] / WN
    a1u[w] = {'era_n': WU[w], 'era_p': pw, 'ratio_cipher_over_era': p84 / pw,
              'inband': inband(p84 / pw)}
# A2: 84's own follower 59 x2 — cipher-side: what is 59 doing?
# 59->46 "que" x2 (verb taking que); check era for 84-candidate -> 59-candidate
a['A2_59_profile'] = {'n59': CF['59'], 'followers59': dict(fol('59').most_common()),
                      'predecessors59': dict(pre('59').most_common())}
a['A2_era_que_after'] = {w: WB.get(('que', w), 0) for w in []}
# era verbs that take "que" most often (for the 59="verb+que" reading)
que_takers = collections.Counter()
for (w1, w2) in zip(RAW, RAW[1:]):
    if w2 == 'que':
        que_takers[w1] += 1
a['A2_era_top_que_takers'] = que_takers.most_common(15)
# A3: alternative parse — 84 as complement after a verb (77=verb reading).
# cipher-side: 84's predecessor set minus the trigram; 84's followers diversity.
a['A3_84_predecessor_diversity'] = len(pre('84'))
a['A3_84_follower_diversity'] = len(fol('84'))
# era: words that can follow a verb+object — check "X le W" where W is a verb:
# (second parse of the trigram) 77=verb, 84 = post-verbal. Rank era (V, W) for
# fixed trigram-internal V unknown — instead test: is 84's follower profile
# (59 x2, rest diverse) compatible with a VERB? era: top followers of common
# verbs vs cipher followers of 84. Use word-space: followers of "faire"/"dire".
for v in ('faire', 'dire', 'voir', 'savoir'):
    fv = collections.Counter(w2 for (w1, w2) in zip(RAW, RAW[1:]) if w1 == v)
    a[f'A3_era_followers_{v}'] = fv.most_common(10)
# A4: the 84->59 x2 + 59->46 x2 chain in era: find era (W, V, 'que') chains
# with W in the A1 candidate set — a joint consistency test.
a4 = a['A4_joint_chain'] = {}
cands = [w for w, _ in tri_qil.most_common(12)]
for w in cands:
    n_w_v_que = sum(1 for (a1, a2, a3, a4g) in zip(W, W[1:], W[2:], W[3:])
                    if a1 == w and a3 == 'que')
    a4[w] = {'n_w_X_que_4gram': n_w_v_que}
# how many era "qui le W" continuations then take a que-clause soon?
a['A4_note'] = 'chain test: era 4-gram (W, X, que) counts for candidate W'

# ============ THREAD (b): the "le me" x7 dependency ===========================
b = out['legs']['b_leme_x7'] = {}
b77_78 = positions_bigram('77', '78')
b['pos_77->78'] = b77_78
b['n_77->78'] = len(b77_78)
b['n77'] = CF['77']
b['n78'] = CF['78']
b['P78_given77'] = len(b77_78) / CF['77']
b['P78_base'] = CF['78'] / N
b['enrichment'] = b['P78_given77'] / b['P78_base']
# classify each of the 7 by the 78's follower (F38 rules)
cls = b['classification'] = {}
for i in b77_78:
    f78 = pairs[i + 2] if i + 2 < N else None
    p77 = pairs[i - 1] if i > 0 else None
    cls[str(i)] = {'pre77': p77, 'win_r2': window(i, 2),
                   'fol78': f78,
                   'is_ver_islet': f78 == '94',
                   'is_5mer': pairs[i:i + 5] == ['77', '78', '94', '82', '06']}
b['n_islet_in_x7'] = sum(1 for v in cls.values() if v['is_ver_islet'])
b['n_5mer_in_x7'] = sum(1 for v in cls.values() if v['is_5mer'])
# B1: dissolution check — do the non-islet 5 read as me-syllable frames?
# follower-of-78 distribution inside x7 vs outside x7 (cipher-side).
all78 = [i for i, p in enumerate(pairs) if p == '78']
fol_in = collections.Counter(pairs[i + 2] for i in b77_78 if i + 2 < N)
fol_out = collections.Counter(pairs[i + 1] for i in all78
                              if i + 1 < N and i not in b77_78)
b['B1_fol78_inside_x7'] = dict(fol_in)
b['B1_fol78_outside_x7'] = dict(fol_out.most_common())
# B2: era word-bigram "le me" — the dissolved adverse, re-derived.
b['B2_era_le_me'] = WB.get(('le', 'me'), 0)
b['B2_era_le_n'] = WU['le']
# B3: adversarial — any of the 7 where 77 MUST be word-"le" AND 78 MUST be
# word-"me" simultaneously? i.e. 78's follower forces a word boundary after
# "me" while 77's frame forces word-"le" before. Follower 45 (if 45="me"-word)
# would be "me me" era-0 — flag.
b['B3_flag_78fol45_in_x7'] = [int(i) for i in b77_78
                              if i + 2 < N and pairs[i + 2] == '45']
b['B3_era_me_me'] = WB.get(('me', 'me'), 0)
# B4: the other 78-predecessors — is 77 special? P(78|77) vs P(78|47), P(78|37)
for g in ('47', '37', '11'):
    n = len(positions_bigram(g, '78'))
    b[f'B4_P78_given_{g}'] = n / CF[g] if CF[g] else 0.0
    b[f'B4_n_{g}->78'] = n

# ============ THREAD (c): 45="me" test ========================================
c = out['legs']['c_test_45_me'] = {}
c['n45'] = CF['45']
c['rank45'] = sorted(CF.values(), reverse=True).index(CF['45']) + 1
c['pos78->45'] = positions_bigram('78', '45')
c['windows78->45_r2'] = {str(i): window(i, 2) for i in c['pos78->45']}
c['followers45'] = dict(fol('45').most_common())
c['predecessors45'] = dict(pre('45').most_common())
# overlap: are the four 78->45 instances among the 77->78 x7? among ver islets?
s775 = set(b77_78)
c['overlap_78->45_with_77->78'] = [i for i in c['pos78->45'] if i in s775]
c['overlap_78->45_ver_islet'] = [i for i in c['pos78->45']
                                 if i + 2 < N and pairs[i + 2] == '94']
# C1: unigram word-space test P(45) vs P("me")
p45 = CF['45'] / N
pme = WU['me'] / WN
c['C1'] = {'cipher_P45': p45, 'era_Pme': pme, 'era_n_me': WU['me'],
           'ratio': p45 / pme, 'inband': inband(p45 / pme)}
# C2: the "me me" joint tension — under 78="me"-syllable, 78->45 with 45="me"
# is era-0 ("me me"). Check era ("me","me") and the status of the 4 host 78s.
c['C2_era_me_me'] = WB.get(('me', 'me'), 0)
c['C2_era_me_n'] = WU['me']
# are the four 78s in the me-syllable population or the ver-islet population?
# ver islet = next==94; none of the four have next==94 (checked above) so all
# four 78s are in the me-syllable population under F38's partition.
c['C2_host78_reading'] = 'all four host 78s are non-islet => me-syllable under F38'
# C3: predecessor test — era words most often before "me" vs cipher pre(45)
me_pres = collections.Counter()
for (w1, w2) in zip(RAW, RAW[1:]):
    if w2 == 'me':
        me_pres[w1] += 1
c['C3_era_top_pre_me'] = me_pres.most_common(15)
c['C3_cipher_pre45'] = dict(pre('45').most_common())
# which cipher predecessors of 45 are attested before "me" in era?
c['C3_match'] = {p: me_pres.get(p, 0) for p in pre('45')}
# C4: alternative — 45's followers vs era followers of "me"
me_fols = collections.Counter()
for (w1, w2) in zip(RAW, RAW[1:]):
    if w1 == 'me':
        me_fols[w2] += 1
c['C4_era_top_fol_me'] = me_fols.most_common(15)
c['C4_cipher_fol45'] = dict(fol('45').most_common())

json.dump(out, open(os.path.join(HERE, 'closer6.json'), 'w'),
          indent=1, ensure_ascii=False)
print('wrote closer6.json')

# ---------------- console digest ---------------------------------------------
print('== baseline ==')
for k in ('n77', 'n78', 'n84', 'n45', 'n59', 'n64', 'n87', 'n94'):
    print(' ', k, base[k])
print('  77->78', base['77->78'], base['pos_77->78'] if 'pos_77->78' in base else positions_bigram('77','78'))
print('  78->45', base['78->45'], base['pos_78->45'])
print('  94->82', base['94->82'], base['pos_94->82'])
print('  77->86', base['77->86'], base['pos_77->86'])
print('  84->59', base['84->59'], positions_bigram('84', '59'))
print('  64-77-84', base['pos_64-77-84'])
print('  87-64-77-84', base['pos_87-64-77-84'])
print('  64-77-84-59', base['pos_64-77-84-59'])
print('  77-78-94-82-06', base['pos_77-78-94-82-06'])
print('== (a) 84 ==')
print('  pos84', a['pos84'])
print('  pre84', a['predecessors84'])
print('  fol84', a['followers84'])
print('  qui le top:', a['A1_era_qui_le_followers'][:12])
print('  ce qui le top:', a['A1_era_ce_qui_le_followers'][:8])
print('== (b) x7 ==')
for i, v in cls.items():
    print(' ', i, v['win_r2'], 'pre77=', v['pre77'], 'fol78=', v['fol78'],
          'islet' if v['is_ver_islet'] else '', '5mer' if v['is_5mer'] else '')
print('  P(78|77)=%.4f base=%.4f enrich=%.2f' %
      (b['P78_given77'], b['P78_base'], b['enrichment']))
print('  fol78 inside x7:', dict(fol_in))
print('  era (le,me):', b['B2_era_le_me'], '/', b['B2_era_le_n'])
print('== (c) 45 ==')
print('  n45', c['n45'], 'rank', c['rank45'])
print('  pre45', c['predecessors45'])
print('  fol45', c['followers45'])
print('  C1 ratio', round(c['C1']['ratio'], 3), 'inband', c['C1']['inband'])
print('  overlap x7:', c['overlap_78->45_with_77->78'])
