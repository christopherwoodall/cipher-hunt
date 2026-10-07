#!/usr/bin/env python3
"""T7 anchored recount: only tilings that ENGAGE the anchor cell count.

A fit is anchor-bearing iff the anchor group sits in the window under the
anchor cell. Vacuous (anchor-free) placements are reported separately.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PAIRS as P, GT, PROV, fit_cells, null_rate, load_lexicon_tilings

HARD = dict(GT)
HARD.update(PROV)
lex = load_lexicon_tilings()

# (name, anchor_group, anchor_cell, cell_offset, k, manual_tilings_with_anchor)
DRAGS = [
    ('Metternich', '29', 'er', 2, 4,
     [['met', 't', 'er', 'nich'], ['me', 'tt', 'er', 'nich'],
      ['m', 'et', 't', 'er', 'nich']][:2]),
    ('Nesselrode', '94', 'ne', 0, 4,
     [['ne', 'ssel', 'ro', 'de']]),
    ('Nesselrode', '94', 'ne', 0, 5,
     [['ne', 'se', 'l', 'ro', 'de']]),
    ('Ibrahim', '34', 'i', 0, 3,
     [['i', 'bra', 'him']]),
    ('Ibrahim', '34', 'i', 0, 4,
     [['i', 'b', 'ra', 'him']]),
    ('Saxe', '40', 'e', 1, 2,
     [['sax', 'e']]),
    ('Mehemet-Ali', '78', 'me', 0, 5,
     [['me', 'he', 'met', 'a', 'li'], ['me', 'h', 'me', 't', 'a', 'li']]),
]

out = {}
for name, g0, c0, k0, k, tilings in DRAGS:
    bearing = []
    for s in range(len(P) - k + 1):
        if P[s + k0] != g0:
            continue
        groups = P[s:s + k]
        for cells in tilings:
            ok, notes = fit_cells(cells, groups, HARD)
            if ok:
                bearing.append({'start': s, 'cells': cells,
                                'groups': groups})
                break
    key = f'{name}[{g0}={c0}@{k0}]'
    entry = {'n_bearing': len(bearing),
             'positions': [b['start'] for b in bearing][:15]}
    if bearing:
        s = bearing[0]['start']
        n, N, sample = null_rate(P[s:s + k], HARD, lex)
        entry['null_at_first'] = [n, N]
        entry['null_sample'] = sample[:8]
        entry['first_groups'] = bearing[0]['groups']
        entry['first_cells'] = bearing[0]['cells']
    out[key] = entry
    print(key, 'bearing:', len(bearing), entry.get('positions', []),
          'null:', entry.get('null_at_first'))

json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                't7_anchored.json'), 'w'), indent=1)
print('wrote t7_anchored.json')
