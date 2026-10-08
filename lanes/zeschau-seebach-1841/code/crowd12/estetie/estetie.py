#!/usr/bin/env python3
"""Round 12 WO7: este-verb tie-breakers T1-T5. Pre-registered in PREREG-T1T5.md.

Reads the repaired 1,847-pair stream and the clean-diplo era corpus.
Writes estetie_results.json. No manual tiling: all counts from code.
"""
import json, re, sys, unicodedata
from collections import Counter
from pathlib import Path

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
sys.path.insert(0, str(LANE / 'code/crowd6/redteam'))
from verify_baseline import load_stream  # noqa: E402

OUT = {}
s = load_stream()
assert len(s) == 1847, len(s)

# banked glosses
GLOSS = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que',
         87: 'ce?', 64: 'qui?', 96: 'par?', 59: 'est/-este?', 77: 'le?',
         94: 'ne?', 52: 'pas~'}

def gloss(i):
    g = s[i]
    return '%d%s' % (g, '=%s' % GLOSS[g] if g in GLOSS else '')

def window(i, r=3):
    return [s[j] for j in range(max(0, i - r), min(len(s), i + r + 1))]

# ================= era corpus =================
CORP = LANE / 'code' / 'side-period' / 'corpus'
FRENCH_CLEAN = ['guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
                'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
                'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
                'pozzo-di-borgo-correspondance-v1.txt',
                'levant-correspondence-1841-p3.txt', 'talleyrand-memoires-v1.txt',
                'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
                'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt']
WORD = re.compile(r"[a-zàâäéèêëîïôöùûüÿçœæ]+(?:'[a-zàâäéèêëîïôöùûüÿçœæ]+)*")

def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('’', "'").replace('‘', "'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p:
                continue
            toks.append(p + "'" if i < len(parts) - 1 else p)
    return toks

ctoks = []
for f in FRENCH_CLEAN:
    ctoks += tokenize((CORP / f).read_text(encoding='utf-8', errors='replace'))
cuni = Counter(ctoks)
cbi = Counter(zip(ctoks[:-1], ctoks[1:]))
ctri = Counter(zip(ctoks[:-1], ctoks[1:], ctoks[2:]))
OUT['era'] = {'files': FRENCH_CLEAN, 'N': len(ctoks)}
print('era clean-diplo N =', len(ctoks))

# v8 unigrams descriptive only
vtoks = tokenize((CORP / 'nesselrode-v8.txt').read_text(encoding='utf-8', errors='replace'))
vuni = Counter(vtoks)
OUT['era']['v8_N'] = len(vtoks)

# ================= T1 =================
t1 = {}
pos84 = [i for i, g in enumerate(s) if g == 84]
este84 = {1189, 1290, 1447, 1803}
free84 = [i for i in pos84 if i not in este84]
t1['n84'] = len(pos84)
t1['este_framed'] = sorted(este84)
t1['free'] = len(free84)
t1['free_windows'] = {i: {'pre': s[i-1], 'suc': s[i+1], 'ctx': window(i, 3),
                          'gloss': [gloss(j) for j in range(i-3, i+4)]} for i in free84}
stems = {'manifeste': 'manif', 'atteste': 'att', 'proteste': 'prot',
         'conteste': 'cont', 'déteste': 'dét'}
# @146 qui-le-84-er test: stem + 'er' word?
t1['w146'] = {'ctx': window(146, 4), 'gloss': [gloss(j) for j in range(142, 151)],
              'stem_plus_er': {v: st + 'er' for v, st in stems.items()}}
# era checks
t1['era'] = {
    'conter': cuni.get('conter', 0),
    'qui_le_conter': ctri.get(('qui', 'le', 'conter'), 0),
    'conte_noun_verb': cuni.get('conte', 0),
    'manifer': cuni.get('manifer', 0), 'atter': cuni.get('atter', 0),
    'proter': cuni.get('proter', 0),
    'v8_conter': vuni.get('conter', 0),
}
for v, st in stems.items():
    w = st + 'er'
    t1['era']['clean_%s' % w] = cuni.get(w, 0)
print('T1: n84=%d free=%d; era conter=%d qui_le_conter=%d' %
      (t1['n84'], t1['free'], t1['era']['conter'], t1['era']['qui_le_conter']))
OUT['T1'] = t1

# ================= T2 =================
t2 = {}
for name, c, r in [('w1448', 1448, 25), ('w1804', 1804, 25)]:
    lo, hi = c - r, c + r + 1
    t2[name] = {'center': c, 'gloss': [gloss(j) for j in range(lo, hi)]}
# left-context unknown groups (antecedent candidates): list distinct groups
# in the 25-left window that are not banked values
banked = set(GLOSS)
for name, c in [('w1448', 1448), ('w1804', 1804)]:
    left = s[c-25:c-2]  # up to but excluding qui/le region
    t2[name]['left_unbanked'] = sorted(set(g for g in left if g not in banked))
print('T2 windows extracted')
OUT['T2'] = t2

# ================= T3 =================
t3 = {}
pos06 = [i for i, g in enumerate(s) if g == 6]
t3['n06'] = len(pos06)
t3['w1188'] = {'pre06': s[1187], 'suc84': s[1189], 'ctx': window(1188, 6),
               'gloss': [gloss(j) for j in range(1182, 1195)],
               'islet3_fires': s[1187] == 82}
# 06->70 window (@346)
t3['w346'] = {'ctx': window(346, 4), 'gloss': [gloss(j) for j in range(342, 351)],
              'suc70': s[347], 'suc2': s[348]}
# all 06 windows: successor profile
suc06 = Counter(s[i+1] for i in pos06)
pre06 = Counter(s[i-1] for i in pos06 if i > 0)
t3['suc_profile'] = dict(sorted(suc06.items()))
t3['pre_profile'] = dict(sorted(pre06.items()))
# pro-witness hunt: 06 windows where suc is a GT syllable or 06-70
t3['pro_witnesses'] = [{'pos': i, 'pre': s[i-1], 'suc': s[i+1],
                       'gloss': [gloss(j) for j in range(i-2, i+3)]}
                      for i in pos06 if s[i+1] in (70, 29, 40, 34, 82)]
# era: propre rates, proteste+que
t3['era'] = {'propre': cuni.get('propre', 0),
             'proteste_que': cbi.get(('proteste', 'que'), 0),
             'proteste': cuni.get('proteste', 0)}
print('T3: n06=%d islet3@1188 fires=%s; 06->70 windows=%d' %
      (t3['n06'], t3['w1188']['islet3_fires'],
       sum(1 for i in pos06 if s[i+1] == 70)))
OUT['T3'] = t3

# ================= T4 =================
t4 = {}
for gval, nm in [(17, 'g17'), (35, 'g35')]:
    pos = [i for i, x in enumerate(s) if x == gval]
    t4[nm] = {'n': len(pos),
              'windows': [{'pos': i, 'pre': s[i-1] if i > 0 else None,
                           'suc': s[i+1],
                           'gloss': [gloss(j) for j in range(i-2, i+3)]}
                          for i in pos],
              'pre_profile': dict(sorted(Counter(s[i-1] for i in pos if i > 0).items())),
              'suc_profile': dict(sorted(Counter(s[i+1] for i in pos).items()))}
# era: 'la fois' + finite verb without 'que' — approximate: 'la fois' bigrams
# followed by a non-que token that is a verb form; simpler: count 'la fois'
# then 'la fois que' vs 'la fois <other>'
la_fois = cbi.get(('la', 'fois'), 0)
la_fois_que = ctri.get(('la', 'fois', 'que'), 0)
t4['era'] = {'la_fois': la_fois, 'la_fois_que': la_fois_que,
             'fois': cuni.get('fois', 0),
             'v8_fois': vuni.get('fois', 0)}
# '59 35 94' positional parallel
t4['g35']['mer_59_35_94'] = [i for i in range(len(s)-2)
                             if s[i:i+3] == [59, 35, 94]]
t4['g35']['mer_35_94_52'] = [i for i in range(len(s)-2)
                             if s[i:i+3] == [35, 94, 52]]
print('T4: n17=%d n35=%d; era la_fois=%d la_fois_que=%d' %
      (t4['g17']['n'], t4['g35']['n'], la_fois, la_fois_que))
OUT['T4'] = t4

# ================= T5 =================
t5 = {}
t5['ngram_64_77_84_59'] = [i for i in range(len(s)-3) if s[i:i+4] == [64, 77, 84, 59]]
t5['ngram_77_84_59'] = [i for i in range(len(s)-2) if s[i:i+3] == [77, 84, 59]]
t5['ngram_64_77_84'] = [i for i in range(len(s)-2) if s[i:i+3] == [64, 77, 84]]
# successors of 64-77-84
t5['qui_le_84_successors'] = {i: s[i+3] for i in t5['ngram_64_77_84']}
print('T5: 64-77-84-59 at', t5['ngram_64_77_84_59'])
OUT['T5'] = t5

json.dump(OUT, open(LANE / 'code/crowd12/estetie/estetie_results.json', 'w'),
          indent=1, ensure_ascii=False)
print('wrote estetie_results.json')
