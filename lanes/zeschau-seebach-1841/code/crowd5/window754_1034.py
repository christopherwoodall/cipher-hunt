#!/usr/bin/env python3
"""CLOSER round 5 — window mining: "la première" @754 (row a5_03, NEVER mined)
vs @1034 (row a6_03). Mine +/-15 pairs around each.

All positions on the repaired 1,847-pair stream (code/crowd4/repaired_parse.py).
Annotations mark ground-truth vs provisional vs lead; nothing invented.

Outputs:
  code/crowd5/window754_1034.md   — human-readable window tables + comparison
  code/crowd5/window754_1034.json — machine numbers
"""
import json, os, sys, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, '..', '..'))
CODE = os.path.join(LANE, 'code')
sys.path.insert(0, os.path.join(CODE, 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, odd_lines, off1 = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N
FREQ = collections.Counter(pairs)

# ---------- annotations (ground truth / provisional / lead) ----------
GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er',
      '40': 'e', '46': 'que'}
PROV = {'87': 'ce', '64': 'qui', '96': 'par', '94': 'ne',
        '47': 'ce', '06': 'stem', '67': 'veut'}
LEAD = {'62': 'on', '77': 'le', '78': 'me', '52': 'pas', '24': 'en',
        '01': 'est', '43': 'me', '37': 'le', '56': 'plus', '74': 'te',
        '21': 'me'}

def annot(g):
    if g in GT:   return GT[g] + ' [GT]'
    if g in PROV: return PROV[g] + ' [prov]'
    if g in LEAD: return LEAD[g] + ' [lead]'
    return ''

# ---------- phases (per-group cluster, repaired) ----------
PHASE = json.load(open(os.path.join(CODE, 'crowd4', 'phase_map_repaired.json')))

# ---------- row mapping ----------
offsets = json.load(open(os.path.join(CODE, 'side-keyhunt',
                                      'repaired_offsets.json')))
ROW_OF = {}   # pair idx -> (row id, offset-in-row)
acc = 0
for line in open(os.path.join(LANE, 'data', 'upstream-ct_R5005.txt')):
    line = line.strip()
    if not line: continue
    lid, digits = line.split()
    digits = re.sub(r'\D', '', digits)
    d = digits[offsets.get(lid, 0):]
    for j in range(len(d) // 2):
        ROW_OF[acc + j] = (lid, j)
    acc += len(d) // 2
assert acc == 1847

out = {'npairs': N, 'windows': {}, 'comparison': {}}

def window(c, r=15):
    rows = []
    for i in range(c - r, c + r + 1):
        lid, off = ROW_OF[i]
        rows.append({'idx': i, 'group': pairs[i], 'row': lid,
                     'rowoff': off, 'phase': PHASE.get(pairs[i], '?'),
                     'annot': annot(pairs[i]),
                     'freq': FREQ[pairs[i]]})
    return rows

for c in (754, 1034):
    # verify crib
    assert pairs[c:c + 6] == ['11', '70', '82', '34', '29', '40'], pairs[c:c+6]
    w = window(c)
    out['windows'][str(c)] = w

# ---------- comparison metrics ----------
w754 = out['windows']['754']; w1034 = out['windows']['1034']
g754 = [r['group'] for r in w754]; g1034 = [r['group'] for r in w1034]
ph754 = ''.join(r['phase'] for r in w754); ph1034 = ''.join(r['phase'] for r in w1034)

cmpd = out['comparison']
# 1. multiset overlap (Jaccard on types, ignoring the shared 6-gram crib)
s754 = set(g754) - {'11','70','82','34','29','40'}
s1034 = set(g1034) - {'11','70','82','34','29','40'}
cmpd['type_jaccard_excl_crib'] = len(s754 & s1034) / len(s754 | s1034)
cmpd['shared_types_excl_crib'] = sorted(s754 & s1034)
# 2. phase-string identity
cmpd['phase_seq_754'] = ph754
cmpd['phase_seq_1034'] = ph1034
cmpd['phase_seq_match_positions'] = sum(a == b for a, b in zip(ph754, ph1034))
# 3. function-word skeleton: groups with a GT/PROV/LEAD annotation
def skeleton(w):
    return [(r['idx'], r['group'], r['annot']) for r in w if r['annot']]
cmpd['skeleton_754'] = skeleton(w754)
cmpd['skeleton_1034'] = skeleton(w1034)
# 4. exact 31-pair identity?
cmpd['windows_identical'] = g754 == g1034
# 5. immediate frames: predecessor triple and successor triple
cmpd['frame_754'] = {'pre': g754[12:15], 'crib': g754[15:21], 'post': g754[21:24]}
cmpd['frame_1034'] = {'pre': g1034[12:15], 'crib': g1034[15:21], 'post': g1034[21:24]}
# 6. anchors inside windows: GT-anchored runs
def anchored_runs(w):
    runs, cur = [], []
    for r in w:
        if r['group'] in GT:
            cur.append(r)
        else:
            if len(cur) >= 2: runs.append(cur)
            cur = []
    if len(cur) >= 2: runs.append(cur)
    return [[(x['idx'], x['group'], GT[x['group']]) for x in run] for run in runs]
cmpd['anchored_runs_754'] = anchored_runs(w754)
cmpd['anchored_runs_1034'] = anchored_runs(w1034)
# 7. provisional function-word frames touching the crib
def touching_frames(w):
    fr = []
    for r in w:
        if r['group'] in PROV or r['group'] in LEAD:
            rel = r['idx'] - (754 if w is w754 else 1034)
            fr.append((rel, r['group'], r['annot']))
    return fr
cmpd['provlead_frames_754'] = touching_frames(w754)
cmpd['provlead_frames_1034'] = touching_frames(w1034)
# 8. rows spanned
cmpd['rows_754'] = sorted({r['row'] for r in w754})
cmpd['rows_1034'] = sorted({r['row'] for r in w1034})

json.dump(out, open(os.path.join(HERE, 'window754_1034.json'), 'w'),
          indent=1, ensure_ascii=False)

# ---------- markdown ----------
md = []
md.append('# Window mining: "la première" @754 vs @1034 (repaired 1,847-pair stream)')
md.append('')
md.append('Crib `11 70 82 34 29 40` byte-verified at both positions. ±15 pairs = 31-pair windows.')
md.append('Annotations: [GT]=pencil ground truth, [prov]=provisional, [lead]=lead. Phases per-group (repaired).')
md.append('')
for c in (754, 1034):
    md.append(f'## Window @ {c}')
    md.append('')
    md.append('| rel | idx | grp | phase | annot |')
    md.append('|-----|-----|-----|-------|-------|')
    for r in out['windows'][str(c)]:
        rel = r['idx'] - c
        mark = ' **>>CRIB<<**' if 0 <= rel <= 5 else ''
        md.append(f"| {rel:+d} | {r['idx']} | {r['group']} | {r['phase']} | {r['annot']}{mark} | row {r['row']}:{r['rowoff']}")
    md.append('')
md.append('## Comparison')
md.append('')
md.append(f"- 31-pair windows byte-identical: **{cmpd['windows_identical']}**")
md.append(f"- Type Jaccard (excl. shared crib 6-gram): {cmpd['type_jaccard_excl_crib']:.3f}")
md.append(f"- Shared types excl. crib: {', '.join(cmpd['shared_types_excl_crib'])}")
md.append(f"- Phase-sequence match positions: {cmpd['phase_seq_match_positions']}/31")
md.append(f"- phase @754 : `{cmpd['phase_seq_754']}`")
md.append(f"- phase @1034: `{cmpd['phase_seq_1034']}`")
md.append(f"- Immediate frame @754 : pre={cmpd['frame_754']['pre']} crib post={cmpd['frame_754']['post']}")
md.append(f"- Immediate frame @1034: pre={cmpd['frame_1034']['pre']} crib post={cmpd['frame_1034']['post']}")
md.append(f"- GT-anchored runs @754: {cmpd['anchored_runs_754']}")
md.append(f"- GT-anchored runs @1034: {cmpd['anchored_runs_1034']}")
md.append(f"- prov/lead frames @754: {cmpd['provlead_frames_754']}")
md.append(f"- prov/lead frames @1034: {cmpd['provlead_frames_1034']}")
md.append(f"- rows spanned @754: {cmpd['rows_754']}")
md.append(f"- rows spanned @1034: {cmpd['rows_1034']}")
open(os.path.join(HERE, 'window754_1034.md'), 'w').write('\n'.join(md) + '\n')
print('wrote window754_1034.{md,json}')
print('identical:', cmpd['windows_identical'],
      'jaccard:', round(cmpd['type_jaccard_excl_crib'], 3),
      'phase_match:', cmpd['phase_seq_match_positions'], '/31')
