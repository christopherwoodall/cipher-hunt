#!/usr/bin/env python3
"""Round-9 conditioner: window census on the repaired canonical stream."""
import collections, json, os, sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'redteam'))
from verify_baseline import load_stream

pairs = load_stream()
N = len(pairs)
assert N == 1847
cf = collections.Counter(pairs)
OUT = {}

def windows_of(g):
    return [i for i, v in enumerate(pairs) if v == g]

def ctx(i, w=3):
    lo, hi = max(0, i - w), min(N, i + w + 1)
    seg = []
    for j in range(lo, hi):
        s = '%02d' % pairs[j]
        seg.append('[%s]' % s if j == i else s)
    return '-'.join(seg)

def find_seq(seq):
    L = len(seq)
    return [i for i in range(N - L + 1) if pairs[i:i + L] == seq]

OUT['n'] = {g: cf[g] for g in [84, 86, 66, 89, 59, 0, 6, 67, 96, 64, 43, 1, 77, 78, 94, 82]}

# ---- 84 windows ----
w84 = windows_of(84)
OUT['84'] = {'n': len(w84),
             'windows': [{'pos': i, 'pre': pairs[i-1], 'suc': pairs[i+1],
                          'ctx3': ctx(i)} for i in w84]}
# round-8 banked sets
EN_EXT = [154, 1151, 276, 1378]   # F62-granted 66/89 extensions
EN_GT = [167]                      # F62-granted @167
EN_FENCED = [1665]                 # fenced adverse
RESID9 = [391, 788, 412, 1021, 857, 1501, 1189, 1290, 1418]
WITHDRAWN = [310, 473]             # F62 qu'en refuted
other = [i for i in w84 if i not in EN_EXT + EN_GT + EN_FENCED + RESID9 + WITHDRAWN]
OUT['84']['other_unaccounted'] = [{'pos': i, 'pre': pairs[i-1], 'suc': pairs[i+1], 'ctx3': ctx(i)} for i in other]

# ---- qui-96-43 formula ----
OUT['formula_64_96_43_87_01'] = find_seq([64, 96, 43, 87, 1])
OUT['formula_ctx'] = {i: ctx(i, 5) for i in OUT['formula_64_96_43_87_01']}
# wider: full 64..01 neighborhood ±8
OUT['formula_ctx8'] = {i: ctx(i, 8) for i in OUT['formula_64_96_43_87_01']}
# 43's other windows
w43 = windows_of(43)
OUT['43'] = {'n': len(w43), 'pre_counter': dict(collections.Counter(pairs[i-1] for i in w43).most_common()),
             'suc_counter': dict(collections.Counter(pairs[i+1] for i in w43).most_common())}

# ---- 64-77-84-59 ----
OUT['seq_64_77_84_59'] = find_seq([64, 77, 84, 59])
OUT['seq_64_77_84_59_ctx5'] = {i: ctx(i, 5) for i in OUT['seq_64_77_84_59']}

# ---- 86 windows ----
w86 = windows_of(86)
OUT['86'] = {'n': len(w86),
             'windows': [{'pos': i, 'pre': pairs[i-1], 'suc': pairs[i+1],
                          'ctx3': ctx(i)} for i in w86],
             'pre_counter': dict(collections.Counter(pairs[i-1] for i in w86).most_common()),
             'suc_counter': dict(collections.Counter(pairs[i+1] for i in w86).most_common())}
OUT['00_86'] = [i for i in w86 if pairs[i-1] == 0]
OUT['00_46'] = [i for i in windows_of(46) if pairs[i-1] == 0]

# ---- 66 windows ----
w66 = windows_of(66)
OUT['66'] = {'n': len(w66),
             'pre_counter': dict(collections.Counter(pairs[i-1] for i in w66).most_common(12)),
             'suc_counter': dict(collections.Counter(pairs[i+1] for i in w66).most_common(12)),
             'pour66': [i for i in w66 if pairs[i-1] == 0],
             'win66_84': [i for i in w66 if i + 1 < N and pairs[i+1] == 84]}

# ---- 89 windows ----
w89 = windows_of(89)
OUT['89'] = {'n': len(w89),
             'pre_counter': dict(collections.Counter(pairs[i-1] for i in w89).most_common(12)),
             'suc_counter': dict(collections.Counter(pairs[i+1] for i in w89).most_common(12)),
             'w77_89': [i for i in w89 if pairs[i-1] == 77],
             'w29_89': [i for i in w89 if pairs[i-1] == 29],
             'w89_48': [i for i in w89 if i + 1 < N and pairs[i+1] == 48],
             'w89_84': [i for i in w89 if i + 1 < N and pairs[i+1] == 84]}

# ---- 59 windows (for 59-word vs 59-syllable split) ----
w59 = windows_of(59)
OUT['59'] = {'n': len(w59),
             'pre_counter': dict(collections.Counter(pairs[i-1] for i in w59).most_common(15)),
             'suc_counter': dict(collections.Counter(pairs[i+1] for i in w59).most_common(15))}

# ---- 00 windows (registry) ----
w00 = windows_of(0)
OUT['00'] = {'n': len(w00),
             'pre_counter': dict(collections.Counter(pairs[i-1] for i in w00).most_common(12)),
             'suc_counter': dict(collections.Counter(pairs[i+1] for i in w00).most_common(12)),
             'w96_00': [i for i in w00 if pairs[i-1] == 96]}

# ---- 06 windows (registry: 06="ent" iff pre=82) ----
w06 = windows_of(6)
OUT['06'] = {'n': len(w06),
             'pre82': [i for i in w06 if pairs[i-1] == 82],
             'pre_counter': dict(collections.Counter(pairs[i-1] for i in w06).most_common(10))}

# ---- 67 windows (registry bookkeeping) ----
w67 = windows_of(67)
OUT['67'] = {'n': len(w67)}

# ---- 96 windows ----
w96 = windows_of(96)
OUT['96'] = {'n': len(w96),
             'w64_96_47': [i for i in w96 if pairs[i-1] == 64 and i + 1 < N and pairs[i+1] == 47]}

# ---- 77-78-94-82-06 5-mer (gouvernement frame) ----
OUT['gouv_5mer'] = find_seq([77, 78, 94, 82, 6])

json.dump(OUT, open(os.path.join(os.path.dirname(__file__), 'census_results.json'), 'w'),
          indent=1)
print('n pairs:', N)
print('formula 64-96-43-87-01 at:', OUT['formula_64_96_43_87_01'])
print('64-77-84-59 at:', OUT['seq_64_77_84_59'])
print('gouv 5-mer at:', OUT['gouv_5mer'])
print('n86=%d 00->86 x%d, 00->46 x%d' % (OUT['86']['n'], len(OUT['00_86']), len(OUT['00_46'])))
print('n66=%d pour66 x%d' % (OUT['66']['n'], len(OUT['66']['pour66'])))
print('n89=%d 77-89 x%d 29-89 x%d 89-48 x%d 89-84 x%d' % (
    OUT['89']['n'], len(OUT['89']['w77_89']), len(OUT['89']['w29_89']),
    len(OUT['89']['w89_48']), len(OUT['89']['w89_84'])))
print('n59=%d n00=%d 96-00 x%d' % (OUT['59']['n'], OUT['00']['n'], len(OUT['00']['w96_00'])))
print('n06=%d pre82 x%d' % (OUT['06']['n'], len(OUT['06']['pre82'])))
print('n67=%d' % OUT['67']['n'])
print('84 other_unaccounted:', [(w['pos'], w['pre'], w['suc']) for w in OUT['84']['other_unaccounted']])
