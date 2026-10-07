#!/usr/bin/env python3
"""Round-5 MORPHOLOGIST executor: 47='ce' promotion battery, 06 stem ID, 06/86 distribution.

Canonical input: REPAIRED parse (1,847 pairs), code/side-keyhunt/repaired_offsets.json.
Era instruments: WORD-SPACE ONLY (F30). No era-syllable-conditional legs on
fragments (29/82/34/40 excluded from era-conditioning). Raw ratios like the
round-4 battery for comparability, plus Wilson 95% CIs.

Work orders:
  WO1: 47='ce' promotion battery. Must EXPLAIN C2 (29->47 x4), address the
       unigram 2.87x, resolve the @148-152 64-slot residual. >=2 independent checks.
  WO2: identify the 06 stem via the 4 infinitive frames (06->29 x4 @1096/1388/1709/1815).
  WO3: test the 06/86 complementary distribution on the repaired parse; name an
       F33-grade (falsifiable) conditioning rule.

Writes: code/crowd5/morph47_06_results.json
"""
import json, os, math, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.join(os.path.expanduser('~'),
    'workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd4'))
from repaired_parse import load_pairs_repaired
import syllabary4 as S

HERE = os.path.dirname(os.path.abspath(__file__))
pairs, _, _ = load_pairs_repaired()
N = len(pairs)
S._era_init()
U, B = S._ERA_U, S._ERA_B
NW = len(S._ERA)

GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er',
      '40': 'e', '46': 'que'}
PROV = {'87': 'ce', '64': 'qui', '96': 'par', '94': 'ne'}


def followers(g):
    c = Counter()
    for i, x in enumerate(pairs):
        if x == g and i + 1 < N:
            c[pairs[i + 1]] += 1
    return c


def predecessors(g):
    c = Counter()
    for i, x in enumerate(pairs):
        if x == g and i > 0:
            c[pairs[i - 1]] += 1
    return c


def ngram(seq):
    L = len(seq)
    return sum(1 for i in range(N - L + 1) if pairs[i:i + L] == list(seq))


def bigram_pos(a, b):
    return [i for i in range(N - 1) if pairs[i] == a and pairs[i + 1] == b]


def win(i, r=4):
    return pairs[max(0, i - r):i + r + 1]


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - m) / d, (c + m) / d)


def era_p_next_raw(w2, w1):
    t = sum(B[w1].values())
    return (B[w1][w2] / t) if t else 0.0


out = {'N_pairs': N, 'N_era_words': NW}

# =====================================================================
# WO1: 47 = 'ce' promotion battery (repaired parse)
# =====================================================================
n47 = pairs.count('47')
F47, P47 = followers('47'), predecessors('47')
w47 = {'n': n47, 'followers': dict(F47), 'predecessors': dict(P47)}
w47['windows'] = [[i, win(i, 3)] for i, g in enumerate(pairs) if g == '47']

# --- core legs (repaired) ---
c47_46 = ngram(['47', '46'])          # 'ce que'
c47_11 = ngram(['47', '11'])          # 'cela'
c96_47 = ngram(['96', '47'])          # 'par ce'
n96 = pairs.count('96')
p_que_given_47 = c47_46 / n47
era_p_que_ce = era_p_next_raw('que', 'ce')
p_96_given_47 = P47['96'] / n47
era_p_ce_par = era_p_next_raw('ce', 'par')
p47_uni = n47 / N
era_p_ce = U['ce'] / NW
w47['legs'] = {
    'B1_ce_que': {'cipher': round(p_que_given_47, 4), 'cipher_n': f'{c47_46}/{n47}',
                  'era': round(era_p_que_ce, 4),
                  'ratio': round(p_que_given_47 / era_p_que_ce, 3),
                  'wilson95': [round(v, 4) for v in wilson(c47_46, n47)]},
    'B2_cela': {'n': c47_11},
    'C1_par_ce': {'cipher': round(p_96_given_47, 4),
                  'era': round(era_p_ce_par, 4),
                  'ratio': round(p_96_given_47 / era_p_ce_par, 3) if era_p_ce_par else None},
    'A_uni': {'cipher': round(p47_uni, 5), 'era': round(era_p_ce, 5),
              'ratio': round(p47_uni / era_p_ce, 3)},
}
# C2 frames: 29 -> 47 on the repaired parse
c2pos = bigram_pos('29', '47')
w47['C2'] = {'n': len(c2pos),
             'frames': [[i, win(i, 6)] for i in c2pos]}
# NOTE on C2's old era leg: it conditioned on cipher cell 29='er' mapped to era
# 'words ending in er'. Per F30/N22 the er-rate instrument is uncalibrated
# (29 is a hyper-frequent by-ear cell, 182x over era) -- the 12.6x RATE is VOID
# as a leg. The cipher-side count (29->47 x4) is real and needs a cipher-side
# (by-ear) explanation, which is what the frames below get.

# --- frame classification: ce-frames vs fragment-frames ---
# conditioning features: follower / predecessor identity
ce_frames, frag_frames, other_frames = [], [], []
for i, g in enumerate(pairs):
    if g != '47':
        continue
    pre = pairs[i - 1] if i > 0 else None
    suc = pairs[i + 1] if i + 1 < N else None
    rec = {'pos': i, 'pre': pre, 'suc': suc, 'ctx': win(i, 4)}
    if suc in ('46', '11') or pre == '96':
        rec['class'] = 'ce-frame'
        ce_frames.append(rec)
    elif suc == '78' or pre == '29':
        rec['class'] = 'fragment-frame'
        frag_frames.append(rec)
    else:
        rec['class'] = 'other'
        other_frames.append(rec)
w47['frame_classes'] = {
    'ce_frames': ce_frames, 'frag_frames': frag_frames,
    'other_frames': other_frames,
    'n_ce': len(ce_frames), 'n_frag': len(frag_frames), 'n_other': len(other_frames)}
# F33-style conditioning rule for the fragment reading:
# fragment iff (suc==78) or (pre==29). Check coverage and purity.
frag_pres = Counter(r['pre'] for r in frag_frames)
frag_sucs = Counter(r['suc'] for r in frag_frames)
w47['fragment_conditioning'] = {
    'rule': 'fragment reading iff suc==78 or pre==29',
    'n_covered': len(frag_frames),
    'pre_dist': dict(frag_pres), 'suc_dist': dict(frag_sucs),
    # purity: do ce-frames ever show the fragment features?
    'ce_with_suc78_or_pre29': sum(1 for r in ce_frames
                                  if r['suc'] == '78' or r['pre'] == '29'),
    # do fragment frames ever show ce features (suc 46/11, pre 96)?
    'frag_with_ce_features': sum(1 for r in frag_frames
                                 if r['suc'] in ('46', '11') or r['pre'] == '96'),
}
# ce-proper unigram after removing fragment frames
n_ce_proper = n47 - len(frag_frames)
w47['ce_proper_unigram'] = {
    'n': n_ce_proper,
    'ratio_vs_era_ce': round((n_ce_proper / N) / era_p_ce, 3)}

# --- @148-152 jar: 87 64 96 47 46 (+ downstream) ---
w47['jar148'] = {'window_140_165': pairs[140:166],
                 'wide': [[i, pairs[i]] for i in range(140, 166)]}
# era word-space attestation of the candidate readings (F30-legal)
def era_seq_count(words_seq):
    L = len(words_seq)
    return sum(1 for i in range(NW - L + 1)
               if S._ERA[i:i + L] == list(words_seq))
w47['jar148']['era_attestation'] = {
    n: era_seq_count(s) for n, s in
    {'ce_qui_par_ce_que': ['ce', 'qui', 'par', 'ce', 'que'],
     'ce_qui_parce_que': ['ce', 'qui', 'parce', 'que'],
     'ce_meme_parce_que': ['ce', 'même', 'parce', 'que'],
     'ce_qui_par': ['ce', 'qui', 'par']}.items()}
# what follows the jar: is there a verb slot downstream for the verbless 'qui'?
w47['jar148']['downstream_153_175'] = pairs[153:176]
# 66 profile (needed for the 'ce même 66 parce que' alternative)
w47['g66_profile'] = {'n': pairs.count('66'),
                      'followers': dict(followers('66')),
                      'predecessors': dict(predecessors('66'))}

# --- 47->78 x5 tension: enumerate ---
w47['f47_78'] = {'pos': bigram_pos('47', '78'),
                 'frames': [[i, win(i, 6)] for i in bigram_pos('47', '78')]}

# --- rival battery on the repaired parse, F30-legal word-space legs only ---
# legs: A_uni, B1 (que|w), B2 (la|w i.e. 'cela'-analogue), C1 (w|par)
cands = ['ce', 'se', 'le', 'les', 'en', 'ne', 'me', 'même', 'y', 'de',
         'on', 'il', 'tout', 'plus', 'bien', 'dans']
bat = []
for cand in cands:
    eu = U[cand] / NW
    p_que = era_p_next_raw('que', cand)
    p_la = era_p_next_raw('la', cand)
    p_c_par = era_p_next_raw(cand, 'par')
    bat.append({
        'w': cand, 'era_n': U[cand],
        'A_uni': round(p47_uni / eu, 3) if eu else None,
        # B1: cipher P(46|47) vs era P(que|w); null when era P = 0 -> grammatical kill
        'B1_que': (round(p_que_given_47 / p_que, 3) if p_que
                   else ('KILL_zero' if U[cand] > 50 else 'weak')),
        'B2_la': (round((F47['11'] / n47) / p_la, 3) if p_la
                  else ('KILL_zero' if U[cand] > 50 else 'weak')),
        'C1_par': (round(p_96_given_47 / p_c_par, 3) if p_c_par
                   else ('KILL_zero' if U[cand] > 50 else 'weak')),
    })
w47['rival_battery'] = bat
out['WO1_47ce'] = w47

# =====================================================================
# WO2: identify the 06 stem via the 4 infinitive frames
# =====================================================================
w06 = {}
n06 = pairs.count('06')
F06, P06 = followers('06'), predecessors('06')
w06['n'] = n06
w06['followers'] = dict(F06)
w06['predecessors'] = dict(P06)

f0629 = bigram_pos('06', '29')
w06['f06_29'] = {'n': len(f0629), 'pos': f0629,
                 'frames': [[i, win(i, 8)] for i in f0629]}
assert len(f0629) == 4, f0629  # curator: old 5th @760 was an off-phase artifact

f8629 = bigram_pos('86', '29')
w06['f86_29'] = {'n': len(f8629), 'pos': f8629,
                 'frames': [[i, win(i, 8)] for i in f8629]}

# the '06 29 67 86' formula on the repaired parse
w06['formula_06_29_67_86'] = {'n': ngram(['06', '29', '67', '86']),
                              'pos': [i for i in range(N - 3)
                                      if pairs[i:i + 4] == ['06', '29', '67', '86']]}
# 67 profile (right neighbor in 2 of the 4 frames; 'veut' is provisional)
n67 = pairs.count('67')
F67, P67 = followers('67'), predecessors('67')
w06['g67_profile'] = {'n': n67, 'followers': dict(F67),
                      'predecessors': dict(P67)}

# --- 67 battery: what follows an -er infinitive in era? (word-space, F30-legal)
# infinitive approx: era words ending in 'er', len>=4, minus noun/adj stoplist
STOP_ER = {'premier', 'premiers', 'première', 'premières', 'dernier',
           'derniers', 'dernière', 'dernières', 'étranger', 'étrangers',
           'étrangère', 'étrangères', 'léger', 'légers', 'légère', 'légères',
           'amer', 'amère', 'amers', 'amères', 'fier', 'fière', 'fiers',
           'fières', 'cher', 'chère', 'chers', 'chères', 'hier', 'enfer',
           'hiver', 'hivers', 'danger', 'dangers', 'mer', 'mers', 'fer',
           'vers', 'divers', 'diverse', 'diverses', 'travers', 'univers',
           'caractères', 'mystère', 'ministère', 'cimetière', 'frère'}
INF = [w for w in set(S._ERA) if len(w) >= 4 and w.endswith('er')
       and w not in STOP_ER]
INF_SET = set(INF)
# era: distribution of the word AFTER an -er infinitive
after_inf = Counter()
n_inf_tok = 0
for a, b in zip(S._ERA, S._ERA[1:]):
    if a in INF_SET:
        after_inf[b] += 1
        n_inf_tok += 1
w06['era_after_infinitive'] = {'n_inf_tokens': n_inf_tok,
                               'top20': after_inf.most_common(20)}
cands67 = ['veut', 'est', 'et', 'en', 'y', 'tout', 'plus', 'bien', 'faire',
           'dire', 'sans', 'pour', 'avec', 'comme', 'dont']
bat67 = []
p67_after_inf = {w: after_inf[w] / n_inf_tok for w in cands67}
for cw in cands67:
    # cipher-side: P(67=cw | prev = 06 29)? unknown mapping; use P(67|06,29 frame)
    # instead score era P(cw | prev is -er infinitive) directly
    bat67.append({'w': cw, 'era_n': U[cw],
                  'era_P_after_inf': round(p67_after_inf[cw], 5),
                  'era_n_after_inf': after_inf[cw]})
# cipher-side check: in the two '06 29 67' frames, what does era say the
# infinitive is followed by? rank the candidates.
bat67.sort(key=lambda r: -r['era_P_after_inf'])
w06['battery_67'] = bat67
w06['n_06_29_67'] = ngram(['06', '29', '67'])

# --- era -er infinitive candidates scored per frame ---
# right-context constraints (known values only):
#   @1096/@1388: next = 67 (winner of battery_67)
#   @1709: next cell = 40 'e' -> next word starts with 'e' (et/est/en/elle...)
#   @1815: next = 37 (unknown)
# left-context: all unknown groups -> use unigram rate only.
# stem-rate constraint: cipher P(06)=n06/N per pair; per-word approx via F29
# mean 1.93 groups/word -> words ~= N/1.93. Era stem rate per 1000 words.
words_est = N / 1.93
w06['rate_frame'] = {'n06': n06, 'N_pairs': N,
                     'est_words': round(words_est),
                     'cipher_stem_per_1000w': round(n06 / words_est * 1000, 2)}
stem_cands = ['demand', 'command', 'parl', 'donn', 'port', 'charg', 'assur',
              'trouv', 'pass', 'pri', 'rest', 'pens', 'mont', 'montr', 'sembl',
              'tourn', 'gard', 'appel', 'port', 'compt', 'regard', 'écout',
              'cherch', 'travaill', 'march', 'jou', 'aim', 'ador', 'inform',
              'pri', 'suppli', 'mand', 'ordonn', 'défend']
seen = set()
stem_rates = []
for s in stem_cands:
    if s in seen:
        continue
    seen.add(s)
    # infinitive form = stem + 'er' must exist in era
    inf = s + 'er'
    stem_rates.append({'stem': s, 'infinitive': inf,
                       'era_inf_n': U[inf],
                       'stem_per_1000w': round(
                           sum(n for w, n in U.items() if w.startswith(s))
                           / NW * 1000, 3)})
stem_rates.sort(key=lambda r: -r['stem_per_1000w'])
w06['stem_rates'] = stem_rates

# per-frame infinitive scoring: P(next_word | inf) for the KNOWN right context
# frame A (@1096/@1388): next=67. frame B (@1709): next starts with 'e'.
# score = era P(67winner | inf) and era P(word starting 'e' | inf)
next_e_words = [w for w in set(S._ERA) if w.startswith('e') and len(w) >= 2]
frame_scores = []
for r in stem_rates:
    inf = r['infinitive']
    if r['era_inf_n'] < 3:
        continue
    tot = sum(B[inf].values())
    d = {'stem': r['stem'], 'infinitive': inf, 'era_inf_n': r['era_inf_n'],
         'stem_per_1000w': r['stem_per_1000w']}
    # P(67-candidates | inf)
    for cw in ['veut', 'est', 'et']:
        d[f'P_{cw}_after_inf'] = round(B[inf][cw] / tot, 4) if tot else 0.0
        d[f'n_{cw}_after_inf'] = B[inf][cw]
    # P(next word starts with 'e' | inf)
    ne = sum(B[inf][w] for w in next_e_words)
    d['P_estart_after_inf'] = round(ne / tot, 4) if tot else 0.0
    d['n_estart_after_inf'] = ne
    # top followers of this infinitive in era
    d['top_followers'] = [[w, c] for w, c in B[inf].most_common(6)]
    frame_scores.append(d)
frame_scores.sort(key=lambda r: -(r['P_et_after_inf'] + r['P_est_after_inf']))
w06['frame_scores'] = frame_scores

# the '...ere' noun rival for @1709 (06 29 40 = stem+'er'+'e' word-internal):
# era nouns ending in 'ère'/'ere' after unknown-12, before unknown-65
ere_nouns = [(w, U[w]) for w in set(S._ERA)
             if (w.endswith('ère') or w.endswith('ere')) and len(w) >= 5]
ere_nouns.sort(key=lambda t: -t[1])
w06['ere_noun_rival_1709'] = {'top15': ere_nouns[:15]}
# and @1709 as infinitive+'et': era P('et' | prev=inf) distribution check
w06['P_et_after_inf_dist'] = {
    r['infinitive']: r['P_et_after_inf'] for r in frame_scores[:25]}
out['WO2_06stem'] = w06

# =====================================================================
# WO3: the 06/86 complementary distribution (repaired parse)
# =====================================================================
w06086 = {}
n00, n86 = pairs.count('00'), pairs.count('86')
F00, P00 = followers('00'), predecessors('00')
F86, P86 = followers('86'), predecessors('86')
w06086['profiles'] = {
    'n00': n00, 'n86': n86, 'n06': n06,
    'F00': dict(F00), 'P00': dict(P00),
    'F86': dict(F86), 'P86': dict(P86),
    'F06': dict(F06), 'P06': dict(P06),
}
c00_86 = ngram(['00', '86'])
c00_06 = ngram(['00', '06'])
w06086['complementary'] = {'c00_86': c00_86, 'c00_06': c00_06, 'n00': n00}
# 06's finite frames vs 86 in those frames
w06086['frames_06'] = {
    'c06_11': ngram(['06', '11']), 'c06_77': ngram(['06', '77']),
    'c06_00': ngram(['06', '00']), 'c06_29': ngram(['06', '29'])}
w06086['frames_86_in_06_slots'] = {
    'c86_11': ngram(['86', '11']), 'c86_77': ngram(['86', '77']),
    'c86_00': ngram(['86', '00']), 'c86_29': ngram(['86', '29'])}
# 86's governor slot: who precedes 86?
w06086['pred_86_top'] = P86.most_common(10)
# the one 86->06 adjacency: position + wide context
p8606 = bigram_pos('86', '06')
w06086['c86_06'] = {'n': len(p8606), 'pos': p8606,
                    'frames': [[i, win(i, 8)] for i in p8606]}
# 00->86 frames wide (what is the governor slot?)
p0086 = bigram_pos('00', '86')
w06086['f00_86'] = {'pos': p0086, 'frames': [[i, win(i, 5)] for i in p0086]}
# 06->00 frames wide
p0600 = bigram_pos('06', '00')
w06086['f06_00'] = {'pos': p0600, 'frames': [[i, win(i, 5)] for i in p0600]}

# --- significance: is 00->86 concentration real? ---
# H0: 86's successor distribution after 00 = its global successor distribution.
# permutation-style: P(pre=00 | g=86) = 12/32 vs P(00) baseline among all
# bigram tokens; binomial for c00_06 = 0 given 06's global rate after governors.
p_pre00_given_86 = P86['00'] / n86
# baseline: fraction of bigram tokens whose first element is 00
p00_first = n00 / N
# binomial: P(X >= 12) with n=32, p=p00_first
def binom_sf(k, n, p):
    # P(X >= k)
    from math import comb
    return sum(comb(n, j) * p**j * (1 - p)**(n - j) for j in range(k, n + 1))
w06086['significance'] = {
    'P_pre00_given_86': round(p_pre00_given_86, 4),
    'baseline_P00_first': round(p00_first, 4),
    'enrichment': round(p_pre00_given_86 / p00_first, 2),
    'binom_P_ge12': binom_sf(12, n86, p00_first),
    # the zero: P(00->06 = 0/12+) -- compare against 06's rate after non-00
    # governors: use P(06 | pre != 00) among 06's predecessor mass
    'P06_given_pre00': 0.0,
    'n00_bigrams': n00,
}
# F33-grade rule test: does 86 EVER take a finite-frame follower, does 06 EVER
# follow 00, does 06 EVER sit in 86's governor slot (pre=00)?
w06086['falsifier_scan'] = {
    'any_00_06': c00_06,
    'any_86_11_77_00': {k: w06086['frames_86_in_06_slots'][k]
                        for k in ('c86_11', 'c86_77', 'c86_00')},
    'any_06_after_00': c00_06,
    'any_86_06': len(p8606),
}
# homophony probe: post-'er' neighbor distribution, 06->29 vs 86->29
post06 = Counter(pairs[i + 2] for i in f0629 if i + 2 < N)
post86 = Counter(pairs[i + 2] for i in f8629 if i + 2 < N)
w06086['post_er_neighbors'] = {'after_06_29': dict(post06),
                               'after_86_29': dict(post86)}
# 00 identity probe (distributional only, no promotion): top followers
w06086['g00_followers_top15'] = F00.most_common(15)
out['WO3_06086'] = w06086

# =====================================================================
# write
# =====================================================================
fn = os.path.join(HERE, 'morph47_06_results.json')
json.dump(out, open(fn, 'w'), indent=1, ensure_ascii=False)
print('wrote', fn)

# ---- console digest ----
w = out['WO1_47ce']
print('\n=== WO1: 47 = ce (repaired parse, N=1847) ===')
print('n47 =', w['n'])
L = w['legs']
print('B1 ce-que : cipher %(cipher_n)s = %(cipher)s vs era %(era)s -> %(ratio)sx  wilson=%(wilson95)s' % L['B1_ce_que'])
print('B2 cela   : n =', L['B2_cela']['n'])
print('C1 par-ce : cipher %(cipher)s vs era %(era)s -> %(ratio)sx' % L['C1_par_ce'])
print('A  unigram: cipher %(cipher)s vs era %(era)s -> %(ratio)sx' % L['A_uni'])
print('C2 29->47 : n =', w['C2']['n'])
for i, c in w['C2']['frames']:
    print('   @%d:' % i, c)
print('frame classes: ce=%d frag=%d other=%d' % (w['frame_classes']['n_ce'],
      w['frame_classes']['n_frag'], w['frame_classes']['n_other']))
print('fragment conditioning:', json.dumps(w['fragment_conditioning'], ensure_ascii=False))
print('ce-proper unigram ratio:', w['ce_proper_unigram'])
print('jar148 window 140-166:', w['jar148']['window_140_165'])
print('era attestation:', w['jar148']['era_attestation'])
print('downstream 153-175:', w['jar148']['downstream_153_175'])
print('47->78 frames:')
for i, c in w['f47_78']['frames']:
    print('   @%d:' % i, c)
print('rival battery (A/B1/B2/C1):')
for r in w['rival_battery']:
    print('  %(w)6s A=%(A_uni)s B1=%(B1_que)s B2=%(B2_la)s C1=%(C1_par)s era_n=%(era_n)d'
          % r)

w = out['WO2_06stem']
print('\n=== WO2: 06 stem (repaired) ===')
print('n06 =', w['n'], ' f06_29 n =', w['f06_29']['n'], w['f06_29']['pos'])
for i, c in w['f06_29']['frames']:
    print('   @%d:' % i, c)
print('f86_29 n =', w['f86_29']['n'], w['f86_29']['pos'])
for i, c in w['f86_29']['frames']:
    print('   @%d:' % i, c)
print('formula 06 29 67 86: n =', w['formula_06_29_67_86']['n'],
      w['formula_06_29_67_86']['pos'])
print('67 profile: n =', w['g67_profile']['n'])
print('  followers:', dict(list(w['g67_profile']['followers'].items())[:12]))
print('  predecessors:', dict(list(w['g67_profile']['predecessors'].items())[:12]))
print('67 battery (era P(w | prev = -er infinitive)):')
for r in w['battery_67'][:8]:
    print('  %(w)6s P=%(era_P_after_inf)s n=%(era_n_after_inf)d era_unigram_n=%(era_n)d' % r)
print('rate frame:', w['rate_frame'])
print('stem rates (top 12 by stem/1000w):')
for r in w['stem_rates'][:12]:
    print('  %(stem)8s inf=%(infinitive)-12s era_inf_n=%(era_inf_n)5d stem/1000w=%(stem_per_1000w)s' % r)
print('frame scores (top 12 by P(et|inf)+P(est|inf)):')
for r in w['frame_scores'][:12]:
    print('  %(stem)8s P(et|inf)=%(P_et_after_inf)s P(est|inf)=%(P_est_after_inf)s '
          'P(veut|inf)=%(P_veut_after_inf)s P(e-start|inf)=%(P_estart_after_inf)s top=%(top_followers)s' % r)
print('ere-noun rival @1709 top:', w['ere_noun_rival_1709']['top15'][:8])

w = out['WO3_06086']
print('\n=== WO3: 06/86 distribution (repaired) ===')
print('n00 =', w['profiles']['n00'], ' n86 =', w['profiles']['n86'])
print('00->86 =', w['complementary']['c00_86'], ' 00->06 =', w['complementary']['c00_06'])
print('06 frames :', w['frames_06'])
print('86 in 06-slots:', w['frames_86_in_06_slots'])
print('pred(86) top:', w['pred_86_top'])
print('86->06 :', w['c86_06'])
print('significance:', json.dumps(w['significance'], ensure_ascii=False))
print('falsifier scan:', json.dumps(w['falsifier_scan'], ensure_ascii=False))
print('post-er neighbors:', json.dumps(w['post_er_neighbors'], ensure_ascii=False))
print('00 followers top15:', w['g00_followers_top15'])
print('00->86 frames:')
for i, c in w['f00_86']['frames']:
    print('   @%d:' % i, c)
print('06->00 frames:')
for i, c in w['f06_00']['frames']:
    print('   @%d:' % i, c)
