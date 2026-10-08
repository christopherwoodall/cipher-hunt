#!/usr/bin/env python3
"""Round-13 islet audit: 4-part compositional battery.

Re-derives every count from the repaired 1,847-pair stream. Era checks on the
clean diplomatic pool (no nesselrode-v8 for phrases, no AZ German).
Writes results.json. Recommendations only — adjudicator rules.
"""
import json, os, sys
from collections import Counter
from scipy.stats import chi2

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stream import load_pairs, windows, ctx
from era import era_words, counts

OUT = {}
pairs = load_pairs()
OUT['stream'] = {'n_pairs': len(pairs), 'n_groups': len(set(pairs))}

W = era_words()
N, wu, bi = counts(W)
tri = Counter(zip(W, W[1:], W[2:]))
quad = Counter(zip(W, W[1:], W[2:], W[3:]))
quin = Counter(zip(W, W[1:], W[2:], W[3:], W[4:]))
OUT['era'] = {'pool_files': 16, 'N_words': N}

def chi2_2way(c1, c2):
    """Uniformity of two categorical distributions; pooled expected."""
    cats = sorted(set(c1) | set(c2))
    n1, n2 = sum(c1.values()), sum(c2.values())
    stat, dof = 0.0, 0
    for c in cats:
        o1, o2 = c1.get(c, 0), c2.get(c, 0)
        e1 = (o1 + o2) * n1 / (n1 + n2)
        e2 = (o1 + o2) * n2 / (n1 + n2)
        if e1 >= 1 and e2 >= 1:
            stat += (o1 - e1) ** 2 / e1 + (o2 - e2) ** 2 / e2
            dof += 1
    dof = max(dof - 1, 1)
    return {'chi2': round(stat, 3), 'dof': dof,
            'p': round(float(chi2.sf(stat, dof)), 4), 'n1': n1, 'n2': n2}

def prec(g):
    return Counter(p for _, p, _ in windows(pairs, g) if p)
def succ(g):
    return Counter(s for _, _, s in windows(pairs, g) if s)

# confirmed multi-cell words (byte-verified this lane)
WORDS = {
    'm_en': ('82', '84'), 'ment': ('82', '06'), 'par_le': ('96', '00'),
    'en_ce': ('24', '87'), 'c_est': ('87', '01'),
    'la_premiere': ('11', '70', '82', '34', '29', '40'),
}
def in_word(i):
    """positions i-1/i inside any confirmed word n-gram?"""
    for name, w in WORDS.items():
        L = len(w)
        for j in range(max(0, i - L + 1), i + 1):
            if pairs[j:j + L] == list(w) and j <= i < j + L:
                return name
    return None

# =====================================================================
# ISLET 4 — 67 et/veut fork
# =====================================================================
w67 = windows(pairs, '67')
OUT['islet4'] = {'n67': len(w67)}
def et_rules(i, pre, pre2, suc):
    r = []
    if pre in ('06', '86'): r.append('R_et1')
    if suc == '64': r.append('R_et2')
    if pre == '29' and pre2 in ('06', '86'): r.append('R_et3')
    if suc == '11': r.append('R_et4')
    if suc == '77' and pre not in ('21', '11'): r.append('R_et5')
    if suc == '96': r.append('R_et6')
    return r
def veut_rules(i, pre, suc):
    r = []
    if pre == '21': r.append('R_veut1')
    if suc == '78': r.append('R_veut2')
    if pre == '11': r.append('R_veut3')
    return r
rows, tally = [], Counter()
for i, pre, suc in w67:
    pre2 = pairs[i - 2] if i >= 2 else None
    er, vr = et_rules(i, pre, pre2, suc), veut_rules(i, pre, suc)
    if er and vr: cls = 'BOTH'
    elif er: cls = 'et'
    elif vr: cls = 'veut'
    else: cls = 'open'
    tally[cls] += 1
    rows.append({'pos': i, 'pre': pre, 'suc': suc, 'class': cls,
                 'et': er, 'veut': vr})
OUT['islet4']['tally'] = dict(tally)
OUT['islet4']['open_positions'] = [r['pos'] for r in rows if r['class'] == 'open']
OUT['islet4']['both_positions'] = [r['pos'] for r in rows if r['class'] == 'BOTH']
w506 = [r for r in rows if r['pos'] == 506]
w1248 = [r for r in rows if r['pos'] == 1248]
OUT['islet4']['w506'] = w506
OUT['islet4']['w1248'] = w1248
# compositional overlap: 67-windows inside confirmed words
ov = [(r['pos'], in_word(r['pos'])) for r in rows if in_word(r['pos'])]
OUT['islet4']['word_overlap'] = {'n': len(ov), 'frac': round(len(ov) / len(rows), 3),
                                 'windows': ov}
# era legs
OUT['islet4']['era'] = {
    'et_la': bi[('et', 'la')], 'veut_la': bi[('veut', 'la')],
    'et_le': bi[('et', 'le')], 'veut_le': bi[('veut', 'le')],
    'et_par': bi[('et', 'par')], 'veut_par': bi[('veut', 'par')],
    'et_qui': bi[('et', 'qui')], 'veut_qui': bi[('veut', 'qui')],
}

# =====================================================================
# ISLET 5 — 96=verb-stem iff pre==64 & suc==47
# =====================================================================
w96 = windows(pairs, '96')
OUT['islet5'] = {'n96': len(w96)}
f = [(i, pre, suc) for i, pre, suc in w96 if pre == '64' and suc == '47']
OUT['islet5']['frame_windows'] = f
OUT['islet5']['frame_ctx'] = [ctx(pairs, i) for i, _, _ in f]
OUT['islet5']['n96_00'] = sum(1 for _, _, s in w96 if s == '00')  # par le
OUT['islet5']['suc47_other_pre'] = [(i, pre) for i, pre, suc in w96
                                    if suc == '47' and pre != '64']
OUT['islet5']['pre_counter'] = dict(prec('96').most_common())
# era: «ce qui X ce que» frames, all verb-led?
frames = [(a, b, c, d, e) for a, b, c, d, e in
          zip(W, W[1:], W[2:], W[3:], W[4:])
          if a == 'ce' and b == 'qui' and d == 'ce' and e == 'que']
OUT['islet5']['era_ce_qui_X_ce_que'] = {'n': len(frames),
                                       'fillers': [x[2] for x in frames][:10]}
par_ce_que = sum(1 for a, b, c in zip(W, W[1:], W[2:])
                 if a == 'ce' and b == 'qui' and c == 'par')
OUT['islet5']['era_ce_qui_par_ce_que'] = par_ce_que

# =====================================================================
# ISLET 6 — 66 class
# =====================================================================
w66 = windows(pairs, '66')
OUT['islet6'] = {'n66': len(w66)}
OUT['islet6']['windows'] = [{'pos': i, 'pre': pre, 'suc': suc,
                             'ctx': ctx(pairs, i)} for i, pre, suc in w66]
OUT['islet6']['pour66'] = sum(1 for _, pre, _ in w66 if pre == '00')
OUT['islet6']['pre_counter'] = dict(prec('66').most_common(8))
# subject-pronoun forcing: pre==00 (pour) + subject-only pronouns is 0;
# check 66 windows where a subject pronoun would be forced — none expected
# era: «pour» + subject pronouns
OUT['islet6']['era_pour_subjpron'] = {p: bi[('pour', p)] for p in
                                     ['il', 'on', 'ils', 'je', 'tu']}
OUT['islet6']['era_pour_nous_vous'] = {'nous': bi[('pour', 'nous')],
                                      'vous': bi[('pour', 'vous')]}
ov66 = [(i, in_word(i)) for i, _, _ in w66 if in_word(i)]
OUT['islet6']['word_overlap'] = {'n': len(ov66), 'windows': ov66}

# =====================================================================
# ISLET 7 — 89 noun-class
# =====================================================================
w89 = windows(pairs, '89')
OUT['islet7'] = {'n89': len(w89)}
OUT['islet7']['windows'] = [{'pos': i, 'pre': pre, 'suc': suc,
                             'ctx': ctx(pairs, i)} for i, pre, suc in w89]
OUT['islet7']['legs'] = {
    '77_89': sum(1 for _, pre, _ in w89 if pre == '77'),
    '29_89': sum(1 for _, pre, _ in w89 if pre == '29'),
    '89_48': sum(1 for _, _, suc in w89 if suc == '48'),
    '24_89': sum(1 for _, pre, _ in w89 if pre == '24'),
    '52_89': sum(1 for _, pre, _ in w89 if pre == '52'),
    '29_89_84': sum(1 for i, pre, _ in w89
                    if pre == '29' and pairs[i + 1] == '84'),
}
# compositional check: 29-89 as «[stem]er»+89 — is 29-89 a word boundary?
# check whether prepre of 29-89 windows completes «premier» (11-70-82-34)
pr29 = []
for i, pre, suc in w89:
    if pre == '29' and i >= 5:
        pr29.append((i, pairs[i - 5:i]))
OUT['islet7']['pre29_5mer'] = pr29
ov89 = [(i, in_word(i)) for i, _, _ in w89 if in_word(i)]
OUT['islet7']['word_overlap'] = {'n': len(ov89), 'windows': ov89}

# =====================================================================
# ISLET 8 — 64-77-84-59 ×2
# =====================================================================
hits8 = [i for i in range(len(pairs) - 3)
         if pairs[i:i + 4] == ['64', '77', '84', '59']]
OUT['islet8'] = {'n_frames': len(hits8), 'positions': hits8,
                 'ctx': [ctx(pairs, i, 4) for i in hits8]}
# era: «qui le X est» and «qui le X Y» verb dominance
qlxe = sum(1 for a, b, c, d in zip(W, W[1:], W[2:], W[3:])
           if a == 'qui' and b == 'le' and d == 'est')
qly = [(c, d) for a, b, c, d in zip(W, W[1:], W[2:], W[3:])
       if a == 'qui' and b == 'le']
OUT['islet8']['era_qui_le_X_est'] = qlxe
OUT['islet8']['era_qui_le_n'] = len(qly)
OUT['islet8']['era_qui_le_sample'] = qly[:12]
# -este verb inventory
OUT['islet8']['era_este_verbs'] = {v: wu[v] for v in
    ['manifeste', 'atteste', 'proteste', 'conteste', 'déteste', 'reste']}

# =====================================================================
# ISLET 9 — 86 identity
# =====================================================================
w86 = windows(pairs, '86')
OUT['islet9'] = {'n86': len(w86)}
OUT['islet9']['n00_86'] = sum(1 for _, pre, _ in w86 if pre == '00')
n00 = sum(1 for p in pairs if p == '00')
OUT['islet9']['n00'] = n00
OUT['islet9']['suc_counter'] = dict(succ('86').most_common(10))
OUT['islet9']['suc_consonant_kill'] = {
    '86_70': sum(1 for _, _, s in w86 if s == '70'),
    '86_52': sum(1 for _, _, s in w86 if s == '52'),
    '86_56': sum(1 for _, _, s in w86 if s == '56'),
}
OUT['islet9']['n77_86'] = sum(1 for _, pre, _ in w86 if pre == '77')
OUT['islet9']['w77_86'] = [(i, pairs[i + 1]) for i, pre, _ in w86 if pre == '77']
npour = wu['pour']
OUT['islet9']['era'] = {
    'P_que_given_pour': round(bi[('pour', 'que')] / npour, 5) if npour else 0,
    'n_pour_que': bi[('pour', 'que')],
    'P_qu_given_pour': round(bi[('pour', 'qu')] / npour, 5) if npour else 0,
    'n_pour_qu': bi[('pour', 'qu')],
    'n_pour': npour,
    'cipher_00_86_frac': round(OUT['islet9']['n00_86'] / n00, 4) if n00 else 0,
    'n_le_que': bi[('le', 'que')], 'n_le_qu': bi[('le', 'qu')],
    'n_le': wu['le'],
}
# part 4: {33,86} uniformity; {66,86} contact sanity
OUT['islet9']['homophone_33_86'] = chi2_2way(prec('33'), prec('86'))
OUT['islet9']['homophone_33_86_suc'] = chi2_2way(succ('33'), succ('86'))
pre66, pre86 = prec('66'), prec('86')
jacc = len(set(pre66) & set(pre86)) / max(len(set(pre66) | set(pre86)), 1)
OUT['islet9']['set_66_86'] = {'pre_jaccard': round(jacc, 3),
                              'n66': len(windows(pairs, '66'))}
# F40 M1: 06/86 complementary distribution spot-check
OUT['islet9']['suc86_29'] = sum(1 for _, _, s in w86 if s == '29')  # [86]er

# =====================================================================
# ISLET 10 — 59 est / -este
# =====================================================================
w59 = windows(pairs, '59')
OUT['islet10'] = {'n59': len(w59)}
def arm59(pre):
    if pre in ('64', '94', '93'): return 'est'
    if pre == '84': return 'este'
    if pre in ('06', '61', '44', '86'): return 'subtier'
    return 'leftover'
rows59, tally59 = [], Counter()
for i, pre, suc in w59:
    a = arm59(pre)
    tally59[a] += 1
    rows59.append({'pos': i, 'pre': pre, 'suc': suc, 'arm': a,
                   'ctx': ctx(pairs, i)})
OUT['islet10']['tally'] = dict(tally59)
OUT['islet10']['est_windows'] = [r for r in rows59 if r['arm'] == 'est']
OUT['islet10']['este_windows'] = [r for r in rows59 if r['arm'] == 'este']
OUT['islet10']['subtier_windows'] = [r for r in rows59 if r['arm'] == 'subtier']
OUT['islet10']['leftover_windows'] = [r for r in rows59 if r['arm'] == 'leftover']
# era legs: qui/l/n + est
OUT['islet10']['era'] = {
    'n_qui_est': bi[('qui', 'est')], 'n_qui': wu['qui'],
    'n_l_est': bi[('l', 'est')], 'n_l': wu['l'],
    'n_n_est': bi[('n', 'est')], 'n_n': wu['n'],
    'n_est': wu['est'],
    'P_59': round(len(w59) / len(pairs), 5),
}
# part 4: {52,59} uniformity
OUT['islet10']['homophone_52_59'] = chi2_2way(prec('52'), prec('59'))
OUT['islet10']['homophone_52_59_suc'] = chi2_2way(succ('52'), succ('59'))
# est frames with successors (fused-word check: pre=93/94 elided single words)
OUT['islet10']['est_pre93_94_ctx'] = [
    (r['pos'], r['ctx']) for r in rows59 if r['pre'] in ('93', '94')]

# =====================================================================
# SANITY — the three dissolved islets
# =====================================================================
OUT['sanity'] = {}
# ISLET 3: 06="ent" iff pre=82 → W06 06-positions [580,738,1184,1355]
w06 = windows(pairs, '06')
w06_82 = [(i, pre, suc) for i, pre, suc in w06 if pre == '82']
OUT['sanity']['islet3'] = {
    'n06': len(w06),
    'pre82_06_positions': [i for i, _, _ in w06_82],
    'expect': [580, 738, 1184, 1355],
    'ctx': [ctx(pairs, i, 4) for i, _, _ in w06_82],
}
# ISLET 2: 00="le" iff pre=96
w00 = windows(pairs, '00')
w00_96 = [(i, pre, suc) for i, pre, suc in w00 if pre == '96']
OUT['sanity']['islet2'] = {
    'n00': len(w00),
    'pre96_positions': [i for i, _, _ in w00_96],
    'expect': [48, 466, 961],
    'ctx': [ctx(pairs, i, 3) for i, _, _ in w00_96],
}
# ISLET 1: 84="en" iff pre∈{82,66,89}
w84 = windows(pairs, '84')
arms = [(i, pre, suc) for i, pre, suc in w84 if pre in ('82', '66', '89')]
OUT['sanity']['islet1'] = {
    'n84': len(w84),
    'arm_windows': [(i, pre, suc, ctx(pairs, i, 3)) for i, pre, suc in arms],
    'residual_n': len(w84) - len(arms),
}
# 24-87 compositional (87="ce" after 24)
OUT['sanity']['en_ce'] = sum(1 for i in range(len(pairs) - 1)
                             if pairs[i] == '24' and pairs[i + 1] == '87')
OUT['sanity']['era_en_ce'] = bi[('en', 'ce')]
# @1351 ment check: 78-94-82-06 + successor
i1351 = 1351
OUT['sanity']['ment_1351'] = {'seq': pairs[1351:1358]}

json.dump(OUT, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'results.json'), 'w'), indent=1)
print('n67 =', OUT['islet4']['n67'], 'tally =', dict(tally))
print('n96 =', OUT['islet5']['n96'], 'frame =', len(f))
print('n66 =', OUT['islet6']['n66'], 'n89 =', OUT['islet7']['n89'])
print('n86 =', OUT['islet9']['n86'], 'n00_86 =', OUT['islet9']['n00_86'])
print('n59 =', OUT['islet10']['n59'], 'tally59 =', dict(tally59))
print('era N =', N)
print('OK — results.json written')
