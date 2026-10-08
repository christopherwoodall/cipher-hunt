#!/usr/bin/env python3
"""R13-31 — 31's class VERIFICATION carry (WO7 class half). Runs AFTER PREREG.md.
Independent byte-exact re-derivation of round-12's B31 census (fresh script,
same pre-registered D-rules). CONFIRM iff byte-identical + >=2 disambiguated
verbal contacts / 0 nominal. Plus the conservative-outcome audit and the
31->29 F22-granularity consistency datum (not a leg)."""
import sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
sys.path.insert(0, str(LANE / 'code/crowd8/frenchman'))
import util
from util import PAIRS, N, UNI

OUT = {'prereg': str(HERE / 'PREREG.md')}

def fail(msg):
    print('HALT:', msg); sys.exit(2)

# ---- census-fidelity gate ----
assert N == 1847, N
assert PAIRS[1517:1522] == [11, 91, 67, 8, 31], PAIRS[1517:1522]
assert PAIRS[900:905] == [16, 92, 67, 16, 88], PAIRS[900:905]
assert UNI[31] == 8 and UNI[92] == 22 and UNI[8] == 18
print('gate PASS: N=1847, n31=8 n92=22 n08=18')
OUT['gate'] = 'PASS'

# ---- D-rule census over all 08 positions (pre-registered rules) ----
D = {'D-ce': [], 'D-que': [], 'D-ne': [], 'D-qui': []}
for i in util.positions(8):
    pre = PAIRS[i-1] if i > 0 else None
    if pre == 87: D['D-ce'].append(i)
    elif pre == 46: D['D-que'].append(i)
    elif pre == 94: D['D-ne'].append(i)
    elif pre == 64: D['D-qui'].append(i)
OUT['D_census'] = D
print('D census:', {k: v for k, v in D.items()})
# expected from round-12: D-ce=[1488], rest empty
if D['D-ce'] != [1488] or any(D[k] for k in ('D-que', 'D-ne', 'D-qui')):
    fail('D-census drift vs round-12: %s' % D)
print('D-census matches round-12 byte-exact (D-ce=[1488])')

# ---- 31-window classification ----
contacts = []
for i in util.positions(31):
    pre = PAIRS[i-1] if i > 0 else None
    if pre == 64:
        contacts.append((i, 'verbal', 'qui-relative', ['64=qui provisional']))
    elif pre == 8:
        j = i - 1
        if j in D['D-ce']:
            contacts.append((i, 'verbal', 'D-ce (ce l\' -> pronoun)',
                              ['87=ce provisional', '08="l\'" lead']))
        else:
            contacts.append((i, 'ambiguous', '08 undisambiguated (pre=%s)' %
                             (PAIRS[j-1] if j > 0 else None), []))
    elif pre == 11:
        contacts.append((i, 'ambiguous', '11=la article/pronoun-ambiguous', []))
    else:
        contacts.append((i, 'ambiguous', 'pre=%s unidentified' % pre, []))
OUT['contacts'] = [{'pos': p, 'kind': k, 'rule': r, 'cond': c}
                   for p, k, r, c in contacts]
n_verbal = sum(1 for _, k, _, _ in contacts if k == 'verbal')
n_nominal = sum(1 for _, k, _, _ in contacts if k == 'nominal')
OUT['n_verbal_disamb'] = n_verbal
OUT['n_nominal_disamb'] = n_nominal
print('31 contacts: %d verbal, %d nominal' % (n_verbal, n_nominal))
for p, k, r, c in contacts:
    print('   @%-5d %-9s %s %s' % (p, k, r, c))

EXPECTED_VERBAL = {338, 1489, 1647}
got = {p for p, k, _, _ in contacts if k == 'verbal'}
if got != EXPECTED_VERBAL or n_nominal != 0:
    fail('contact drift vs round-12: got %s' % sorted(got))
print('contact set matches round-12 byte-exact (@338/@1647 qui-relative, @1489 D-ce)')

# ---- conservative audit data ----
# route (b) re-check: any new 11->31 or 46->31 in parse?
route_b_11 = [i for i in util.positions(31) if PAIRS[i-1] == 11]
route_b_46 = [i for i in util.positions(31) if PAIRS[i-1] == 46]
OUT['route_b'] = {'n_11_to_31': len(route_b_11), 'pos': route_b_11,
                  'n_46_to_31': len(route_b_46), 'pos46': route_b_46,
                  'verdict': 'STILL UNMEETABLE' if len(route_b_11) == 1 and len(route_b_46) == 0
                               else 'DRIFT — investigate'}
# the "-quiere" fence flag: count "64 29 40" windows (tensions 64='qui'-word)
q_windows = [i for i in util.positions(64)
             if i + 2 < N and PAIRS[i+1] == 29 and PAIRS[i+2] == 40]
OUT['quiere_windows'] = q_windows
print('route(b): 11->31 n=%d @%s; 46->31 n=%d' % (len(route_b_11), route_b_11, len(route_b_46)))
print('"64 29 40" (-quiere tension) windows:', q_windows)

# ---- consistency datum (NOT a leg): 31->29 under F22 granularity ----
suc29 = [i for i in util.positions(31) if i + 1 < N and PAIRS[i+1] == 29]
OUT['suc29'] = {'pos': suc29,
                'window_ctx': {i: ' '.join(str(PAIRS[j]) for j in range(max(0, i-3), min(N, i+4)))
                               for i in suc29},
                'note': ('IF 31=finite-verb stem, "31 29"=stem+"er" ending is '
                         'consistent under F22 granularity (e.g. @1489: 87,08,31,29 '
                         '= "ce l\'" + stem + "er"). Consistency datum only; '
                         'shares the hypothesis — not an independent leg.')}
print('31->29 windows:', suc29)

OUT['verdict'] = ('CONFIRM 31=VERBAL (finite) provisional-conditioned '
                  '(C1: 64=qui, 87=ce; 08="l\'" lead) — RECOMMENDATION carried; '
                  'adjudicator rules') if (n_verbal >= 2 and n_nominal == 0) else 'DRIFT'
with open(HERE / 'r13_31_results.json', 'w') as f:
    json.dump(OUT, f, indent=1, ensure_ascii=False)
print('wrote r13_31_results.json; verdict:', OUT['verdict'])
