#!/usr/bin/env python3
"""KE2 Part B — @1034 polyvalence audit. Implements PREREG.md (locked 2026-10-07).

B1: registry trigger check at @1034 for each crib group.
B2: F33 conditioned-vs-free battery with each crib group as subject:
    census all occurrences with (pre,suc); split-hunt over {pre=x, suc=y}
    with n>=2 for systematic free-reading failures.
Writes ke2b_results.json (B1 + census + candidate triggers; grammaticality
judgments on candidates done by hand and recorded in the JSON by a follow-up).
"""
import json, os, sys
from collections import Counter, defaultdict

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847

CRIB = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er', '40': 'e'}
CRIB_POS = {'11': 1034, '70': 1035, '82': 1036, '34': 1037, '29': 1038, '40': 1039}
# verify crib placement
assert pairs[1034:1040] == ['11', '70', '82', '34', '29', '40']
assert pairs[754:760] == ['11', '70', '82', '34', '29', '40']

def ctx(i):
    pre = pairs[i - 1] if i > 0 else None
    suc = pairs[i + 1] if i < N - 1 else None
    return pre, suc

# ---------------- B1: contexts at @1034 and @754 ----------------
b1 = {}
for g, pos in CRIB_POS.items():
    pre, suc = ctx(pos)
    pre754, suc754 = ctx(754 + (pos - 1034))
    b1[g] = {'pos1034': pos, 'pre1034': pre, 'suc1034': suc,
             'pre754': pre754, 'suc754': suc754}

# Registry triggers: (group, trigger-desc, fires(pre,suc)->bool)
REGISTRY = [
    ('84', "pre in {82,66,89} -> 'en'", lambda p, s: p in {'82', '66', '89'}),
    ('00', "pre == 96 -> 'le' (not 'pour')", lambda p, s: p == '96'),
    ('06', "pre == 82 -> 'ent'", lambda p, s: p == '82'),
    ('96', "pre == 64 and suc == 47 -> verb-stem", lambda p, s: p == '64' and s == '47'),
    ('59', "pre in {64,94,93} -> word-'est'", lambda p, s: p in {'64', '94', '93'}),
    ('59', "pre == 84 -> verb-final '-este'", lambda p, s: p == '84'),
    ('52', "pre in {94,70} -> 'pas'", lambda p, s: p in {'94', '70'}),
    ('94', "pre == 82 -> 'en'", lambda p, s: p == '82'),
    ('94', "suc == 87 -> 'en'", lambda p, s: s == '87'),
]
b1_triggered = {}
b1_pattern_only = {}
for g in CRIB:
    pre, suc = b1[g]['pre1034'], b1[g]['suc1034']
    own = [t for t in REGISTRY if t[0] == g and t[2](pre, suc)]
    other = [(t[0], t[1]) for t in REGISTRY if t[0] != g and t[2](pre, suc)]
    b1_triggered[g] = [{'rule_group': t[0], 'rule': t[1]} for t in own]
    b1_pattern_only[g] = [{'rule_group': rg, 'rule': rl} for rg, rl in other]

# ---------------- B2: census + split-hunt ----------------
b2 = {}
for g, v in CRIB.items():
    occ = [(i, pairs[i - 1] if i > 0 else None, pairs[i + 1] if i < N - 1 else None)
           for i in range(N) if pairs[i] == g]
    by_pre = defaultdict(list); by_suc = defaultdict(list)
    for i, p, s in occ:
        by_pre[p].append(i); by_suc[s].append(i)
    cand = []
    for p, idxs in sorted(by_pre.items()):
        if p is not None and len(idxs) >= 2:
            cand.append({'trigger': 'pre=%s' % p, 'n': len(idxs), 'positions': idxs})
    for s, idxs in sorted(by_suc.items()):
        if s is not None and len(idxs) >= 2:
            cand.append({'trigger': 'suc=%s' % s, 'n': len(idxs), 'positions': idxs})
    b2[g] = {'value': v, 'n': len(occ),
             'positions': [i for i, _, _ in occ],
             'candidate_triggers': cand}

out = {'crib_contexts': b1,
       'B1_triggered_own_rule': b1_triggered,
       'B1_pattern_only_other_groups': b1_pattern_only,
       'B2_census': b2}
json.dump(out, open(os.path.join(HERE, 'ke2b_results.json'), 'w'), indent=1)
print('B1 @1034 contexts:')
for g in CRIB:
    print(' ', g, '=', CRIB[g], '@1034: pre=%s suc=%s | @754: pre=%s suc=%s' % (
        b1[g]['pre1034'], b1[g]['suc1034'], b1[g]['pre754'], b1[g]['suc754']))
print('B1 own-rule TRIGGERED:', {g: b1_triggered[g] for g in CRIB if b1_triggered[g]})
print('B1 pattern-only (other groups):')
for g in CRIB:
    if b1_pattern_only[g]:
        print(' ', g, b1_pattern_only[g])
print('B2 census n:', {g: b2[g]['n'] for g in CRIB})
