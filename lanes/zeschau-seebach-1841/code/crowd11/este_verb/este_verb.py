#!/usr/bin/env python3
"""Round 11 WO1: este-verb identifier. Pre-registered checks (a/b/c).

Reads the repaired 1,847-pair stream and nesselrode-v8.txt (standing rate
reference). Writes este_verb_results.json. No manual tiling: all counts
from code.
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

# ---------- window verification ----------
windows = {}
for p59, name in [(1190, 'w1190'), (1448, 'w1448'), (1804, 'w1804'), (1291, 'w1291')]:
    assert s[p59] == 59, (name, s[p59])
    assert s[p59 - 1] == 84, (name, s[p59 - 1])
    windows[name] = {
        'p59': p59, 'p84': p59 - 1,
        'ctx12': s[p59 - 12:p59 + 13],
        'pre84': s[p59 - 2],
    }
OUT['windows'] = windows
for name, w in windows.items():
    print(name, 'p59=%d p84=%d pre84=%d' % (w['p59'], w['p84'], w['pre84']))
    print('   ctx12:', w['ctx12'])

# ---------- (a1) 84 predecessor profile ----------
pos84 = [i for i, g in enumerate(s) if g == 84]
OUT['n84'] = len(pos84)
pre_profile = Counter(s[i - 1] for i in pos84)
OUT['pre84_profile'] = dict(sorted(pre_profile.items()))
print('\n(a1) n84 =', len(pos84))
print('pre(84) profile:', dict(sorted(pre_profile.items())))
en_arm = {82, 66, 89}
OUT['en_arm_positions'] = [i for i in pos84 if s[i - 1] in en_arm]
OUT['este_84_positions'] = [w['p84'] for w in windows.values()]
OUT['este_84_pre_in_en_arm'] = [s[w['p84'] - 1] in en_arm for w in windows.values()]
print('84 positions with pre in en-arm {82,66,89}:', OUT['en_arm_positions'])
print('este-window 84 pres in en-arm:', OUT['este_84_pre_in_en_arm'])

# ---------- (a3) by-ear 3-cell cuts for @1190 (06-84-59) ----------
# 59 = "este" (banked). 06+84 must cover the stem. Candidate stems:
stems = {'manifeste': 'manif', 'atteste': 'att', 'proteste': 'prot',
         'conteste': 'cont', 'déteste': 'dét'}
# plausible by-ear 2-way splits of each stem (06=first part, 84=second part)
cuts = {
    'manifeste': [('man', 'if'), ('ma', 'nif'), ('mani', 'f')],
    'atteste': [('a', 'tt'), ('at', 't')],
    'proteste': [('pro', 't'), ('pr', 'ot'), ('p', 'rot')],
    'conteste': [('con', 't'), ('co', 'nt'), ('c', 'ont')],
    'déteste': [('dé', 't'), ('d', 'ét')],
}
OUT['a3'] = {}
for v, stem in stems.items():
    need_first = stem  # 84's required value at @1447/@1803 (first syllable)
    mid_options = [c[1] for c in cuts[v]]
    monovalent_ok = need_first in mid_options
    OUT['a3'][v] = {'stem_first': need_first, 'mid_options_1190': mid_options,
                    'monovalent_compatible': monovalent_ok}
    print('(a3) %-10s stem=%-6s @1190 mid-options=%s monovalent=%s'
          % (v, stem, mid_options, monovalent_ok))

# ---------- (b) v8 era rates ----------
CORP = LANE / 'code' / 'side-period' / 'corpus'
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

toks = tokenize((CORP / 'nesselrode-v8.txt').read_text(encoding='utf-8', errors='replace'))
N = len(toks)
uni = Counter(toks)
bi = Counter(zip(toks[:-1], toks[1:]))
tri = Counter(zip(toks[:-1], toks[1:], toks[2:]))
OUT['v8'] = {'N': N, 'per_candidate': {}}
print('\n(b) v8 N =', N)
for v in stems:
    d = {'n': uni.get(v, 0),
         'qui_le_V': tri.get(('qui', 'le', v), 0),
         'le_V': bi.get(('le', v), 0),
         'V_le': bi.get((v, 'le'), 0),
         'V_que': bi.get((v, 'que'), 0),
         'ne_V_pas': sum(1 for i in range(N - 3)
                         if toks[i] in ('ne', "n'") and toks[i + 1] == v and toks[i + 2] == 'pas')}
    OUT['v8']['per_candidate'][v] = d
    print('  %-10s %s' % (v, d))
# (a2) "manif" as standalone word in v8 + diplo inventory presence
OUT['a2'] = {'manif_standalone_v8': uni.get('manif', 0)}
print('(a2) standalone "manif" in v8:', uni.get('manif', 0))

json.dump(OUT, open(LANE / 'code/crowd11/este_verb/este_verb_results.json', 'w'),
          indent=1, ensure_ascii=False)
print('\nwrote este_verb_results.json')
