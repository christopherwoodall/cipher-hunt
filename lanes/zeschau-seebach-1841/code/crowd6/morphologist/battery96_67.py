#!/usr/bin/env python3
"""Round-6 MORPHOLOGIST executor: WO-A 96 conditioned-verb battery in
"ce qui __ ce que"; WO-B 67 classification + et/veut fork + 43="me" pressure.

Canonical: REPAIRED parse, 1,847 pairs (code/side-keyhunt/repaired_offsets.json
via code/crowd4/repaired_parse.py). Era: Tocqueville WORD-SPACE ONLY (F30) via
code/crowd4/syllabary4.py. No era-syllable-conditional legs on fragments.
Provisional vs GT marked everywhere.

Writes: code/crowd6/morphologist/battery96_67_results.json
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
assert N == 1847 and len(set(pairs)) == 96
S._era_init()
ERA = S._ERA
U, B = S._ERA_U, S._ERA_B
NW = len(ERA)

GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er',
      '40': 'e', '46': 'que'}
PROV = {'87': 'ce', '64': 'qui', '96': 'par', '94': 'ne', '77': 'le'}

out = {'N': N, 'n_groups': len(set(pairs))}


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


def ngram_pos(seq):
    L = len(seq)
    return [i for i in range(N - L + 1) if pairs[i:i + L] == list(seq)]


def ngram(seq):
    return len(ngram_pos(seq))


def win(i, r=5):
    return pairs[max(0, i - r):i + r + 1]


def val(g):
    if g in GT:
        return '%s=GT:%s' % (g, GT[g])
    if g in PROV:
        return '%s=prov:%s' % (g, PROV[g])
    return g


def era_bigram(a, b):
    """word-space P(b|a), Tocqueville."""
    t = sum(B[a].values())
    return (B[a][b] / t) if t else 0.0


def era_seq_count(words):
    L = len(words)
    return sum(1 for i in range(NW - L + 1) if ERA[i:i + L] == list(words))


# =====================================================================
# WO-A: 96 conditioned-verb battery in "ce qui __ ce que"
# =====================================================================
woa = {}

# A0: key numbers re-derived (F41 red-team corrections)
n47 = pairs.count('47')
woa['key_numbers'] = {
    'n47': n47,
    '47->46': ngram(['47', '46']),
    '47->64': ngram(['47', '64']),
    '47->11': ngram(['47', '11']),
    '87->64': ngram(['87', '64']),
    '87->46': ngram(['87', '46']),
    'n96': pairs.count('96'),
}
assert n47 == 28, n47

# A1: frame census — every "ce qui __ ce que" = 87 64 X 47 46
frames = ngram_pos(['87', '64'])
frame5 = []
for i in frames:
    x = pairs[i + 2] if i + 2 < N else None
    tail = pairs[i + 3:i + 5] if i + 4 < N else []
    frame5.append({'pos': i, 'X': x, 'tail': tail,
                   'is_ce_que': tail == ['47', '46'],
                   'win': [val(g) for g in win(i, 5)]})
woa['A1_frame_census'] = {
    'n_87_64': len(frames),
    'frames': frame5,
}
# controls: 47 64 X 47 46 (expect empty per Q1), 87 64 X 87 46 (expect empty)
woa['A1_controls'] = {
    'n_47_64': ngram(['47', '64']),
    'n_87_64_96': ngram(['87', '64', '96']),
    'pos_87_64_96': ngram_pos(['87', '64', '96']),
    'n_96_47_46_parce_que': ngram(['96', '47', '46']),
    'pos_96_47_46': ngram_pos(['96', '47', '46']),
    'n_96_87_46_parce_que': ngram(['96', '87', '46']),
    'pos_96_87_46': ngram_pos(['96', '87', '46']),
}
# what precedes "ce que" (47 46)?
woa['A1_pre_ce_que'] = dict(predecessors('47') and Counter(
    pairs[i - 1] for i in ngram_pos(['47', '46']) if i > 0))
# all "ce qui __" continuations: 87 64 X distribution
woa['A1_ce_qui_continuations'] = dict(followers('64') and Counter(
    pairs[i + 2] for i in frames if i + 2 < N))

# A2: 96's full profile — is @150 the only verb-slot 96?
F96, P96 = followers('96'), predecessors('96')
ctx96 = []
for i in range(N):
    if pairs[i] != '96':
        continue
    pre = pairs[i - 1] if i > 0 else None
    suc = pairs[i + 1] if i + 1 < N else None
    suc2 = pairs[i + 2] if i + 2 < N else None
    frame = None
    if suc == '87' and suc2 == '46':
        frame = 'parce_que_87'
    elif suc == '47' and suc2 == '46':
        frame = 'parce_que_47'
    elif suc == '47':
        frame = 'par_ce'
    elif suc == '43':
        frame = 'par_43'
    elif pre == '64':
        frame = 'qui_PAR_SLOT'
    ctx96.append({'pos': i, 'pre': pre, 'suc': suc, 'frame': frame,
                  'win': [val(g) for g in win(i, 3)]})
woa['A2_96_profile'] = {'n': len(ctx96), 'followers': dict(F96),
                        'predecessors': dict(P96), 'contexts': ctx96}
woa['A2_96_par_frames'] = Counter(c['frame'] for c in ctx96)

# A3: era word-space checks (F30-legal)
woa['A3_era'] = {
    'ce_qui_parce_que_4gram': era_seq_count(['ce', 'qui', 'parce', 'que']),
    'ce_qui_par_ce_que_5gram': era_seq_count(['ce', 'qui', 'par', 'ce', 'que']),
    'ce_qui_par_3gram': era_seq_count(['ce', 'qui', 'par']),
    'n_ce_qui': era_seq_count(['ce', 'qui']),
}
# era fillers of "ce qui __ ce que": ce qui at i, then "ce que" within 1-3 words
fillers = Counter()
cequi_verb_gap = 0
for i in range(NW - 5):
    if ERA[i:i + 2] == ['ce', 'qui']:
        for d in (1, 2, 3):
            if ERA[i + 2 + d:i + 4 + d] == ['ce', 'que']:
                fill = tuple(ERA[i + 2:i + 2 + d])
                fillers[fill] += 1
                break
woa['A3_era']['ce_qui_gap_fillers_ce_que'] = {
    ' '.join(k): v for k, v in fillers.most_common(25)}
woa['A3_era']['n_ce_qui___ce_que'] = sum(fillers.values())
# immediate word after "ce qui" in era (top 20)
woa['A3_era']['top_after_ce_qui'] = B['ce'] and None or None
after_cequi = Counter()
for i in range(NW - 2):
    if ERA[i:i + 2] == ['ce', 'qui']:
        after_cequi[ERA[i + 2]] += 1
woa['A3_era']['top_after_ce_qui'] = after_cequi.most_common(20)
woa['A3_era']['P_parce_after_ce_qui'] = (
    after_cequi['parce'] / sum(after_cequi.values()) if after_cequi else 0.0)

# A4: the @148-152 residual window, verbatim
woa['A4_residual'] = {
    'window_144_160': [{'pos': i, 'g': pairs[i], 'val': val(pairs[i])}
                       for i in range(144, 161)],
}
# era attestation of the four candidate readings (round-5 set, re-derived)
woa['A4_era_readings'] = {
    'ce_qui_par_ce_que': era_seq_count(['ce', 'qui', 'par', 'ce', 'que']),
    'ce_qui_parce_que': era_seq_count(['ce', 'qui', 'parce', 'que']),
    'ce_meme_parce_que': era_seq_count(['ce', 'même', 'parce', 'que']),
    'ce_qui_par': era_seq_count(['ce', 'qui', 'par']),
}

# A5: 96-as-verb verdict inputs — 96 in verb frames elsewhere?
# a verb reading needs a verb-shaped profile: check 96's successors that are
# GT/prov verb-adjacent (29=er, 46=que) vs par-adjacent
woa['A5'] = {
    'n_96_total': len(ctx96),
    'n_96_qui_slot': sum(1 for c in ctx96 if c['frame'] == 'qui_PAR_SLOT'),
    'n_96_parce_que': sum(1 for c in ctx96
                          if c['frame'] in ('parce_que_87', 'parce_que_47')),
    'n_96_par_ce': sum(1 for c in ctx96 if c['frame'] == 'par_ce'),
}

out['WOA'] = woa

# =====================================================================
# WO-B: 67 classification, et/veut fork, "la veut" pin, 43="me" pressure
# =====================================================================
wob = {}
n67 = pairs.count('67')
wob['n67'] = n67
assert n67 == 38, n67
F67, P67 = followers('67'), predecessors('67')
wob['g67_profile'] = {'followers': dict(F67), 'predecessors': dict(P67)}

# B1: full 67 context table
ctx67 = []
for i in range(N):
    if pairs[i] != '67':
        continue
    ctx67.append({
        'pos': i,
        'pre2': pairs[i - 2] if i > 1 else None,
        'pre': pairs[i - 1] if i > 0 else None,
        'suc': pairs[i + 1] if i + 1 < N else None,
        'suc2': pairs[i + 2] if i + 2 < N else None,
        'win': [val(g) for g in win(i, 4)],
    })
wob['B1_contexts'] = ctx67

# B2: et/veut fork — era P(word | prev = -er infinitive), method mirrors round-5
STOP_ER = {'premier', 'premiers', 'première', 'premières', 'dernier',
           'derniers', 'dernière', 'dernières', 'étranger', 'étrangers',
           'étrangère', 'étrangères', 'léger', 'légers', 'légère', 'légères',
           'amer', 'amère', 'amers', 'amères', 'fier', 'fière', 'fiers',
           'fières', 'cher', 'chère', 'chers', 'chères', 'hier', 'enfer',
           'hiver', 'hivers', 'danger', 'dangers', 'mer', 'mers', 'fer',
           'vers', 'divers', 'diverse', 'diverses', 'travers', 'univers',
           'caractères', 'mystère', 'ministère', 'cimetière', 'frère'}
INF_SET = set(w for w in set(ERA) if len(w) >= 4 and w.endswith('er')
              and w not in STOP_ER)
after_inf = Counter()
n_inf_tok = 0
for a, b in zip(ERA, ERA[1:]):
    if a in INF_SET:
        after_inf[b] += 1
        n_inf_tok += 1
p_et = after_inf['et'] / n_inf_tok
p_veut = after_inf['veut'] / n_inf_tok if after_inf['veut'] else 0.0
wob['B2_fork'] = {
    'n_inf_tokens': n_inf_tok,
    'P_et_after_inf': p_et, 'n_et_after_inf': after_inf['et'],
    'P_veut_after_inf': p_veut, 'n_veut_after_inf': after_inf['veut'],
    'ratio_et_veut': (p_et / p_veut) if p_veut else float('inf'),
}

# B3: cipher-side grammatical kills for the fork
wob['B3_grammatical'] = {
    # 67->78 x4: "et me" vs "veut me" in era word-space
    'n_67_78': ngram(['67', '78']),
    'pos_67_78': ngram_pos(['67', '78']),
    'era_et_me': era_seq_count(['et', 'me']),
    'era_veut_me': era_seq_count(['veut', 'me']),
    'era_n_et': U['et'], 'era_n_veut': U['veut'],
    # 67->64 x2: "et qui" vs "veut qui"
    'n_67_64': ngram(['67', '64']),
    'pos_67_64': ngram_pos(['67', '64']),
    'era_et_qui': era_seq_count(['et', 'qui']),
    'era_veut_qui': era_seq_count(['veut', 'qui']),
    # 06 29 67 x2 formula: era after-infinitive ranking already in B2
    'n_06_29_67': ngram(['06', '29', '67']),
    'pos_06_29_67': ngram_pos(['06', '29', '67']),
    'n_86_29_67': ngram(['86', '29', '67']),
    'pos_86_29_67': ngram_pos(['86', '29', '67']),
    # 21 67 86 @1457
    'n_21_67': ngram(['21', '67']),
    'pos_21_67': ngram_pos(['21', '67']),
    'era_me_veut': era_seq_count(['me', 'veut']),
    'era_me_et': era_seq_count(['me', 'et']),
    # 11 67 "la veut" @1044 and 67 11 "veut la"
    'n_11_67': ngram(['11', '67']),
    'pos_11_67': ngram_pos(['11', '67']),
    'n_67_11': ngram(['67', '11']),
    'pos_67_11': ngram_pos(['67', '11']),
    'era_la_veut': era_seq_count(['la', 'veut']),
    'era_la_et': era_seq_count(['la', 'et']),
    'era_veut_la': era_seq_count(['veut', 'la']),
    'era_et_la': era_seq_count(['et', 'la']),
}

# B4: classify each 67 into et-condition / veut-condition / open
# et-conditions (round-5): pre in {06,86} stem frames or 06-29-67 formula,
#   suc=64 (qui); veut-conditions: suc=78 (me), pre=21, pre=11 (la)
def classify_67(c):
    pre, suc = c['pre'], c['suc']
    et = (pre in ('06', '86')) or (suc == '64') or (
        c['pre2'] == '06' and pre == '29') or (c['pre2'] == '86' and pre == '29')
    veut = (suc == '78') or (pre == '21') or (pre == '11')
    if et and veut:
        return 'BOTH'
    if et:
        return 'et'
    if veut:
        return 'veut'
    return 'open'

for c in ctx67:
    c['class'] = classify_67(c)
tally = Counter(c['class'] for c in ctx67)
wob['B4_classification'] = dict(tally)
wob['B4_by_class'] = {k: [c['pos'] for c in ctx67 if c['class'] == k]
                      for k in tally}

# B5: "la veut" @1044-1045 pin test
wob['B5_la_veut'] = {
    'window_1040_1052': [{'pos': i, 'g': pairs[i], 'val': val(pairs[i])}
                         for i in range(1040, 1053)],
    'era_la_veut': era_seq_count(['la', 'veut']),
    'era_la_et': era_seq_count(['la', 'et']),
    # 67@1045's own context
    'ctx_1045': next(c for c in ctx67 if c['pos'] == 1045),
}

# B6: 43="me" pressure — "par 43" x2
n43 = pairs.count('43')
pos_96_43 = ngram_pos(['96', '43'])
F43, P43 = followers('43'), predecessors('43')
wob['B6_43'] = {
    'n43': n43,
    'n_96_43': len(pos_96_43),
    'pos_96_43': pos_96_43,
    'win_96_43': [[{'pos': j, 'g': pairs[j], 'val': val(pairs[j])}
                   for j in range(p - 4, p + 6)] for p in pos_96_43],
    'era_par_me': era_seq_count(['par', 'me']),
    'era_par_moi': era_seq_count(['par', 'moi']),
    'followers_43': dict(F43),
    'predecessors_43': dict(P43),
    # 43's lead context: "il me [v]" @43 (MEDIUM lead basis) — show it
    'win_40_50': [{'pos': i, 'g': pairs[i], 'val': val(pairs[i])}
                  for i in range(38, 52)],
}

# B7: 06/86 M1 compliance spot-check for 67's post-"er" frames; n06 verify
n06 = pairs.count('06')
n86 = pairs.count('86')
wob['B7_M1'] = {
    'n06': n06, 'n86': n86,
    'n_00_86': ngram(['00', '86']), 'n_00_06': ngram(['00', '06']),
    'n_06_29_67': ngram(['06', '29', '67']),
    'n_86_29_67': ngram(['86', '29', '67']),
    # 67 as right neighbor of 29 in stem frames: M1 says 06/86 are stem
    # allomorphs; 67's fork is orthogonal — just verify no 00->06 violation
    # appears in 67's neighborhood
    'note': 'single-stem-for-all-06 KILLED (N38, 17.1x) — not re-proposed; '
            'M1 allomorph frame (F40) is the working frame',
}

out['WOB'] = wob

with open(os.path.join(HERE, 'battery96_67_results.json'), 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print('WOA A1 frames:', len(frames))
print('WOA A1 87-64-96 positions:', woa['A1_controls']['pos_87_64_96'])
print('WOA A2 96 frames:', dict(woa['A2_96_par_frames']))
print('WOB n67:', n67, 'classes:', dict(tally))
print('WOB fork ratio et/veut:', wob['B2_fork']['ratio_et_veut'])
print('WOB n_96_43:', len(pos_96_43), pos_96_43)
print('WOB n06/n86:', n06, n86)
print('wrote battery96_67_results.json')
