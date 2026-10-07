#!/usr/bin/env python3
"""One-shot parity check (rebuild 2026-10-07): the rebuild solver's
load_inventory() must produce EXACTLY the frozen solver's inventory plus the
5 accented by-ear Tier-1 forms (D4 fix) -- same order, same weights --
for all three modes. Any other difference is a rebuild bug.
"""
import json
import os
import sys

REBUILD = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LANE = os.path.abspath(os.path.join(REBUILD, '..', '..', '..'))
FROZEN = os.path.join(LANE, 'code', 'side-homophonic', 'solver')

# frozen pipeline first (needs the crowd2 chain on sys.path, like the Runner)
sys.path.insert(0, os.path.join(LANE, 'code'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd2'))
sys.path.insert(0, FROZEN)
import solver as frozen_solver  # noqa: E402

lm_data = json.load(open(os.path.join(FROZEN, 'lm_ref', 'lm.json')))
lex_wt = {e['w']: e['wt'] for e in lm_data['lexicon']}
pins = {"11": "la", "70": "pre", "82": "m", "34": "i", "29": "er",
        "40": "e", "46": "que"}

frozen_inv = {}
for mode in ('crib', 'extended', 'units'):
    inv, w = frozen_solver.load_inventory(mode, pins, {}, lex_wt)
    frozen_inv[mode] = (inv, w)
    print(f'frozen {mode}: {len(inv)} items')

# now the rebuild (fresh interpreter state for its crib_inventory)
for mod in [m for m in list(sys.modules) if m in ('solver', 'crib_inventory',
                                                  'phonetics', 'phase')]:
    del sys.modules[mod]
sys.path.insert(0, REBUILD)
import importlib.util
spec = importlib.util.spec_from_file_location(
    'rebuild_solver', os.path.join(REBUILD, 'solver.py'))
rebuild_solver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rebuild_solver)

NEW_FORMS = ['vê', 'té', 'né', 'vres', 'my']
ok = True
for mode in ('crib', 'extended', 'units'):
    inv, w = rebuild_solver.load_inventory(mode, pins, {}, lex_wt)
    finv, fw = frozen_inv[mode]
    print(f'rebuild {mode}: {len(inv)} items')
    if mode == 'crib':
        # rebuild == frozen with the 5 new Tier-1 forms spliced after 'pas'
        # (end of the old crib core, index 16)
        assert finv[:16] == inv[:16], f'{mode}: tier1 head diverged'
        assert inv[16:21] == NEW_FORMS, f'{mode}: new forms misplaced: {inv[16:21]}'
        assert finv[16:] == inv[21:], f'{mode}: tail diverged'
        # weights: same formula; check the tail weights match exactly
        assert fw[16:] == w[21:], f'{mode}: tail weights diverged'
        # new forms get tier-1 weight 3.0 + lex_wt
        from phonetics import project as _p  # noqa
        for v, wv in zip(inv[16:21], w[16:21]):
            assert abs(wv - (3.0 + lex_wt.get(_p(v), 0.0))) < 1e-12, v
        print(f'  {mode}: OK (frozen + 5 accented Tier-1 forms, weights match)')
    else:
        assert inv == finv, f'{mode}: inventory diverged'
        assert w == fw, f'{mode}: weights diverged'
        print(f'  {mode}: OK (byte-identical to frozen)')
print('PARITY PASS')
