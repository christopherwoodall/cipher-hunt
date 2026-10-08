#!/usr/bin/env python3
"""B31 — 31's class via 08-disambiguation (route a). Runs AFTER PREREG.md.
Census-fidelity gate first; HALT on drift."""
import sys, json, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd8/frenchman'))
import util
from util import PAIRS, N, UNI, GT
import era

OUT = {}
def fail(msg):
    print('HALT:', msg); sys.exit(2)

# ---- census-fidelity gate ----
print('=== gate ===')
assert N == 1847, N
assert PAIRS[1517:1522] == [11, 91, 67, 8, 31], PAIRS[1517:1522]
assert PAIRS[900:905] == [16, 92, 67, 16, 88], PAIRS[900:905]
assert UNI[31] == 8 and UNI[92] == 22 and UNI[8] == 18, (UNI[31], UNI[92], UNI[8])
print('gate PASS: N=1847, @1519/[11,91,67,8,31], @902/[16,92,67,16,88], n31=8 n92=22 n08=18')
OUT['gate'] = 'PASS'

# ---- D-rule census over all 08 positions ----
# D-ce: pre=87(ce-prov,C1) | D-que: pre=46(que-GT) | D-ne: pre=94(ne-prov-strong,C1) | D-qui: pre=64(qui-prov,C1)
p08 = util.positions(8)
D = {'D-ce': [], 'D-que': [], 'D-ne': [], 'D-qui': []}
for i in p08:
    pre = PAIRS[i - 1] if i > 0 else None
    if pre == 87: D['D-ce'].append(i)
    elif pre == 46: D['D-que'].append(i)
    elif pre == 94: D['D-ne'].append(i)
    elif pre == 64: D['D-qui'].append(i)
print('\n=== D-rule census (n08=18) ===')
for k, v in D.items():
    print(f'{k}: {len(v)} windows {v}')
    for i in v:
        print('   @%d:' % i, ' '.join(str(PAIRS[j]) for j in range(max(0, i - 2), min(N, i + 4))))
OUT['D_census'] = {k: v for k, v in D.items()}

# ---- 31-window classification ----
p31 = util.positions(31)
print('\n=== 31 windows (n=8) ===')
contacts = []  # (pos, kind, rule/anchor, conditionals)
for i in p31:
    pre = PAIRS[i - 1] if i > 0 else None
    suc = PAIRS[i + 1] if i + 1 < N else None
    kind, rule, cond = 'ambiguous', None, []
    if pre == 64:
        kind, rule, cond = 'verbal', 'qui-relative', ['64=qui provisional']
    elif pre == 8:
        # 08's role disambiguated only if a D-rule fired at i-1
        if (i - 1) in D['D-ce']:
            kind, rule, cond = 'verbal', 'D-ce (ce l\' -> pronoun)', ['87=ce provisional', '08="l\'" lead']
        elif (i - 1) in D['D-que']:
            kind, rule, cond = 'verbal', 'D-que', ['08="l\'" lead']
        elif (i - 1) in D['D-ne']:
            kind, rule, cond = 'verbal', 'D-ne', ['94=ne provisional-strong', '08="l\'" lead']
        elif (i - 1) in D['D-qui']:
            kind, rule, cond = 'verbal', 'D-qui', ['64=qui provisional', '08="l\'" lead']
        else:
            kind, rule = 'ambiguous', '08 undisambiguated (pre=%s)' % pre
    elif pre == 11:
        kind, rule = 'ambiguous', '11=la article/pronoun-ambiguous (standing flaw)'
    else:
        kind, rule = 'ambiguous', 'pre=%s unidentified' % pre
    contacts.append((i, kind, rule, cond))
    ctx = ' '.join(str(PAIRS[j]) for j in range(max(0, i - 2), min(N, i + 3)))
    print(f'@{i}: [{ctx}] -> {kind} | {rule} | cond={cond}')
OUT['contacts_31'] = [{'pos': i, 'kind': k, 'rule': r, 'cond': c} for i, k, r, c in contacts]

verbal = [c for c in contacts if c[1] == 'verbal']
nominal = [c for c in contacts if c[1] == 'nominal']
print(f'\ndisambiguated verbal contacts: {len(verbal)} {[c[0] for c in verbal]}')
print(f'disambiguated nominal contacts: {len(nominal)} {[c[0] for c in nominal]}')
OUT['n_verbal_disamb'] = len(verbal)
OUT['n_nominal_disamb'] = len(nominal)

# route (b) pre-check: second GT-anchored nominal contact?
gt_nom = [i for i in p31 if (PAIRS[i - 1] in (11, 46))]
print(f'GT-anchored 31 windows (pre in {{11,46}}): {gt_nom} (route b needs >=2 with nominal force)')
OUT['route_b_windows'] = gt_nom

# ---- era leg E31-1: n('ce','l'') attestation ----
n_ce_l = era.bigram('ce', "l'")
print(f'\n=== E31-1: n((ce, l\')) in French pool = {n_ce_l} (pool {len(era.toks())} tokens) ===')
OUT['E31_1_n_ce_l'] = n_ce_l
if n_ce_l:
    t = era.toks()
    ex = []
    for j in range(len(t) - 3):
        if t[j] == 'ce' and t[j + 1] == "l'":
            ex.append(' '.join(t[j:j + 4]))
            if len(ex) == 3:
                break
    print('examples:', ex)
    OUT['E31_1_examples'] = ex

# ---- verdict ----
if len(verbal) >= 2 and len(nominal) >= 2:
    verdict = 'CONTRADICTION (both bars met — escalate)'
elif len(verbal) >= 2:
    verdict = '31=VERBAL (provisional-conditioned; RECOMMENDATION for red-team)'
elif len(nominal) >= 2:
    verdict = '31=NOMINAL (RECOMMENDATION for red-team)'
else:
    verdict = 'NULL (contested)'
print('\nB31 VERDICT:', verdict)
OUT['verdict'] = verdict
OUT['recommendation'] = ('31=VERBAL provisional-conditioned (C1: 64=qui, 87=ce; 08="l\'" lead)'
                         if verdict.startswith('31=VERBAL') else None)

json.dump(OUT, open(HERE / 'b31_results.json', 'w'), indent=1)
print('\nwrote b31_results.json')
