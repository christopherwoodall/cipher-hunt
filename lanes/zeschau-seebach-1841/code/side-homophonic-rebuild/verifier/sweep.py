#!/usr/bin/env python3
"""Goodhart sweep: search reweightings of the CURRENT term family for one
that flips truth > salad on the 184101 pilot while keeping truth > the
frozen degenerate (viability). Static check only -- see CLOSING-VERIFICATION.md
for the evadability analysis (why static flips don't make truth the argmax).

J = a*S_char + b*S_cov - c*S_single + S_potts - d*n_poly - e*S_conc(cap)
(parts measured independently by rescore.py; conc recomputed per cap)
"""
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, 'parts.json')))
# parts.json holds full dicts incl. decode; extract the scalars
T = {k: P['truth'][k] for k in ('S_char', 'S_cov', 'S_single', 'S_potts', 'n_poly')}
S = {k: P['salad'][k] for k in ('S_char', 'S_cov', 'S_single', 'S_potts', 'n_poly')}
D = {k: P['degen6'][k] for k in ('S_char', 'S_cov', 'S_single', 'S_potts', 'n_poly')}
CONC = {'truth': {6: 0, 4: 9, 2: 50},
        'salad': {6: 10, 4: 74, 2: 223},
        'degen': {6: 46, 4: 139, 2: 311}}
print('truth parts:', {k: round(T[k], 1) for k in T})
print('salad parts:', {k: round(S[k], 1) for k in S})
print('degen parts:', {k: round(D[k], 1) for k in D})


def J(X, key, a, b, c, d, e, cap):
    return (a * X['S_char'] + b * X['S_cov'] - c * X['S_single'] + X['S_potts']
            - d * X['n_poly'] - e * CONC[key][cap])


print()
print(f'{"a":>4} {"b":>4} {"c":>4} {"d":>5} {"e":>5} {"cap":>3} | '
      f'{"M1 t-s":>9} {"M2 t-d":>9}  verdict')
n_flip = 0
examples = []
for a, b, c, d, e, cap in itertools.product(
        (1.0, 0.5, 0.2, 0.0), (1.0, 0.5, 0.2, 0.0), (1, 2, 4, 8),
        (50, 200), (5, 20, 100), (6, 4, 2)):
    jt = J(T, 'truth', a, b, c, d, e, cap)
    js = J(S, 'salad', a, b, c, d, e, cap)
    jd = J(D, 'degen', a, b, c, d, e, cap)
    m1, m2 = jt - js, jt - jd
    if m1 > 0 and m2 > 0:
        n_flip += 1
        if len(examples) < 8:
            examples.append((a, b, c, d, e, cap, m1, m2, jt, js, jd))
        print(f'{a:>4} {b:>4} {c:>4} {d:>5} {e:>5} {cap:>3} | '
              f'{m1:>+9.1f} {m2:>+9.1f}  FLIP (truth wins, viable)')
print(f'\n{n_flip} / {4*4*4*2*3*3} grid points flip the pilot with truth viable')
print('\nExample flips (a,b,c,d,e,cap | M1 truth-salad | M2 truth-degen | totals t/s/d):')
for ex in examples:
    print('   a=%s b=%s c=%s d=%s e=%s cap=%s | M1=%+.1f M2=%+.1f | %.1f / %.1f / %.1f' % ex)

# The shipped config for reference
jt0 = J(T, 'truth', 1, 1, 1, 50, 5, 6)
js0 = J(S, 'salad', 1, 1, 1, 50, 5, 6)
print(f'\nshipped (1,1,1,50,5,6): truth={jt0:.1f} salad={js0:.1f} M1={jt0-js0:+.1f}')
