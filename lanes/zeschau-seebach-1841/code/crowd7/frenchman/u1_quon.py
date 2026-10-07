#!/usr/bin/env python3
"""U1: hunt the "qu'on" whole-word cell (ranked unblocker #1 for 62="on").

Rescue hypothesis (N39 Leg-1 caveat iv): a dedicated whole-word "qu'on" cell X
in the mixed table explains 46->62=0 under 62="on" (and under 62="il" as "qu'il").
Screen: rare groups (2<=n<=8; era expects n~3.3 for qu'on, ~4.4 for qu'il)
with complementizer-shaped predecessor profile (like 46=que [GT]) and
verb-shaped follower profile ("qu'on"+V). Manual by-ear inspection of top hits.
"""
import json, math, collections
import util
from util import PAIRS, N, UNI, GT, followers, predecessors, window

VERBSET = {59, 67, 6}          # 59=verb structural; 67 verb-cand; 06 verb-stem class
eu, eb = util.era_counters()

# reference: 46=que profiles
pre46 = predecessors(46); fol46 = followers(46)
print('46=que n=', UNI[46])
print('  top predecessors:', pre46.most_common(8))
print('  top followers   :', fol46.most_common(8))
print('  frac pre in VERBSET:', sum(c for g, c in pre46.items() if g in VERBSET) / sum(pre46.values()))
print('  frac fol in VERBSET:', sum(c for g, c in fol46.items() if g in VERBSET) / sum(fol46.values()))

# era qu'on profile (unit tokens via raw regex positions -> use split-token approx)
# predecessors of "on" that are "qu'": complement verbs before qu'on
pre_quon = collections.Counter(a for (a, b) in eb if b == 'on' and a == "qu'")
comp_verbs = collections.Counter()
for (a, b), c in eb.items():
    if b == "qu'" and a not in ("qu'",):
        comp_verbs[a] += c
print('\nera complement verbs before qu\' (top):', comp_verbs.most_common(12))
fol_quon = collections.Counter(b for (a, b) in eb if a == "qu'" )
# followers of qu'+on specifically
fol_quon_on = collections.Counter()
t = util.toks()
for i in range(len(t)-2):
    if t[i] == "qu'" and t[i+1] == 'on':
        fol_quon_on[t[i+2]] += 1
print('era followers of qu\'on (top):', fol_quon_on.most_common(12))

def cos(a, b):
    keys = set(a) | set(b)
    na = sum(a.values()); nb = sum(b.values())
    if na == 0 or nb == 0: return 0.0
    return sum(a.get(k, 0)/na * b.get(k, 0)/nb for k in keys) / math.sqrt(
        sum((a.get(k,0)/na)**2 for k in keys) * sum((b.get(k,0)/nb)**2 for k in keys) or 1)

rows = []
for g in range(100):
    n = UNI[g]
    if n < 2 or n > 8:
        continue
    pre = predecessors(g); fol = followers(g)
    sim_pre = cos(pre, pre46)                      # complementizer-likeness
    fverb = sum(c for x, c in fol.items() if x in VERBSET) / max(1, sum(fol.values()))
    fverb_pre = sum(c for x, c in pre.items() if x in VERBSET) / max(1, sum(pre.values()))
    fol62 = fol.get(62, 0); pre46c = pre.get(46, 0)
    rows.append((g, n, sim_pre, fverb, fverb_pre, fol62, pre46c,
                 sorted(pre.items(), key=lambda x: -x[1])[:3],
                 sorted(fol.items(), key=lambda x: -x[1])[:3]))
rows.sort(key=lambda r: -(r[2] + r[3]))
print('\nTop candidates (g, n, cos_pre_vs_46, f_fol_verb, f_pre_verb, fol62, pre46, top_pre, top_fol):')
for r in rows[:15]:
    print(f"  62? g={r[0]:2d} n={r[1]} cos_pre={r[2]:.3f} fverb_fol={r[3]:.2f} fverb_pre={r[4]:.2f} ->62={r[5]} 46->={r[6]} pre={r[7]} fol={r[8]}")

# also: groups that follow complement-verb-ish contexts AND precede verb-ish, regardless of n
print('\n--- wider net: n<=12, require >=1 verb predecessor and >=1 verb follower ---')
wide = []
for g in range(100):
    n = UNI[g]
    if n < 2 or n > 12: continue
    pre = predecessors(g); fol = followers(g)
    vp = sum(c for x, c in pre.items() if x in VERBSET)
    vf = sum(c for x, c in fol.items() if x in VERBSET)
    if vp >= 1 and vf >= 1:
        wide.append((g, n, vp, vf, cos(pre, pre46)))
wide.sort(key=lambda r: -(r[4]))
for g, n, vp, vf, c in wide[:15]:
    print(f'  g={g:2d} n={n} verb_pre={vp} verb_fol={vf} cos_pre46={c:.3f}')

json.dump({'candidates': [r[:7] for r in rows[:15]]},
          open('u1_quon.json', 'w'), indent=1)
print('\nwrote u1_quon.json')
