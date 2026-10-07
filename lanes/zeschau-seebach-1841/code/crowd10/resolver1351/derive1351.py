#!/usr/bin/env python3
"""D1: byte-exact re-derivation of @1349-1362 + D2ii 94-scan + era checks."""
import json, os, sys, re, collections

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

PAIRS, _, _ = load_pairs_repaired()
out = {}

# D1: the window
seg = PAIRS[1349:1363]
out['window_1349_1362'] = {str(1349 + k): v for k, v in enumerate(seg)}
out['D1_assert_1351_1355'] = PAIRS[1351:1356] == ['77', '78', '94', '82', '06']
out['D1_assert_1356'] = PAIRS[1356] == '52'
out['D1_assert_pre1351'] = (PAIRS[1349], PAIRS[1350])  # expect 62, 48
out['D1_assert_suc1356'] = (PAIRS[1357], PAIRS[1358], PAIRS[1359])  # expect 37,64,35
out['D1_full'] = out['D1_assert_1351_1355'] and out['D1_assert_1356'] == True

# D2ii: any other 94 in @1340-1370 that could license 52="pas" under R-b?
scan = [(i, PAIRS[i]) for i in range(1340, 1371) if PAIRS[i] == '94']
out['other_94_in_1340_1370'] = scan

# context: predecessors/successors of the key cells
out['pre_94_1353'] = PAIRS[1351:1353]   # 77,78
out['suc_06_1355'] = PAIRS[1356:1358]   # 52,37

# W06 cross-check (islet positional membership of @1355)
w06 = [i for i in range(len(PAIRS) - 1) if PAIRS[i] == '82' and PAIRS[i + 1] == '06']
out['W06_82pos'] = w06  # expect [579,737,1183,1354] (82-positions)
out['W06_06pos'] = [i + 1 for i in w06]  # expect [580,738,1184,1355]

# Era checks on Nesselrode v8 strict, elision-split tokenizer
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd9', 'frenchman'))
import corpus9
v8t = corpus9.tokenize_elision(
    open(os.path.join(LANE, 'code', 'side-period', 'corpus', 'nesselrode-v8.txt'),
         encoding='utf-8', errors='replace').read())
N = len(v8t)
out['v8_tokens'] = N
gouv_idx = [i for i, w in enumerate(v8t) if w == 'gouvernement']
out['n_gouvernement_v8'] = len(gouv_idx)
out['gouvernement_followed_by_pas'] = sum(
    1 for i in gouv_idx if i + 1 < N and v8t[i + 1] == 'pas')
out['ne_ment_pas_v8'] = sum(
    1 for i in range(N - 2)
    if tuple(v8t[i:i + 3]) == ('ne', 'ment', 'pas'))
out['ne_ment_v8'] = sum(
    1 for i in range(N - 1) if tuple(v8t[i:i + 2]) == ('ne', 'ment'))
# "pas" without ne/n' in 6-back (frenchman Gate 5 figure, re-derived)
bare = sum(1 for i in range(6, N)
           if v8t[i] == 'pas' and 'ne' not in v8t[i - 6:i]
           and "n'" not in v8t[i - 6:i])
out['pas_without_ne_6back_v8'] = bare
out['pas_total_v8'] = v8t.count('pas')
# "on" within L1..L2 of "gouvernement" (H1c figure, re-derived)
out['on_in_L1L2_of_gouvernement_v8'] = sum(
    1 for i in gouv_idx if (i > 0 and v8t[i - 1] == 'on')
    or (i > 1 and v8t[i - 2] == 'on'))
# "le qui" bigram (H1d figure, re-derived)
out['le_qui_bigram_v8'] = sum(
    1 for i in range(N - 1) if v8t[i] == 'le' and v8t[i + 1] == 'qui')

json.dump(out, open('derive1351.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
