#!/usr/bin/env python3
"""REAL-DATA ADAPTER -- R5005 pair loader.

*** NOT FOR CONTROL USE. Not imported by solver.py or control_harness.py. ***
Exists so the Runner can feed the real R5005 transcription to the solver AFTER
the control gate passes, without the solver core ever touching real data.

CANONICAL PARSE (2026-10-07, key-hunt red-team F32, supersedes
data/upstream-offsets.json):
  offsets = code/side-keyhunt/repaired_offsets.json (a5_03: 1 -> 0)
  1,847 pairs / 96 groups expected (not 1,846)
  "la premiere" (11 70 82 34 29 40) at pairs 754 AND 1034 (0-based)
Full remap: code/crowd4/REINDEX.md. Repair code: code/side-keyhunt/repair_parse.py.

Logic replicates code/crib_attack.py load_pairs() (the verified loader):
per-line offsets choose the pair phase; a stray edge digit is dropped.
Yields (pairs, n_groups).
"""

import json
import os
import re

LANE = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', '..'))
DATA = os.path.join(LANE, 'data')
# CANONICAL (F32 repair). Do NOT use data/upstream-offsets.json.
OFFSETS = os.path.join(LANE, 'code', 'side-keyhunt', 'repaired_offsets.json')

CRIB = ['11', '70', '82', '34', '29', '40']
CRIB_AT = (754, 1034)  # 0-based pair indices, REINDEX.md


def load_r5005():
    """Returns (pairs, odd_lines, off1). 1847 pairs / 96 groups expected."""
    offsets = json.load(open(OFFSETS))
    assert offsets.get('a5_03') == 0, \
        'not the repaired offsets (a5_03 must be 0)'
    pairs, odd_lines, off1 = [], 0, 0
    with open(os.path.join(DATA, 'upstream-ct_R5005.txt')) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lid, digits = line.split()
            digits = re.sub(r'\D', '', digits)
            if len(digits) % 2 == 1:
                odd_lines += 1
            off = offsets.get(lid, 0)
            if off == 1:
                off1 += 1
            d = digits[off:]
            for i in range(0, len(d) - 1, 2):
                pairs.append(d[i:i + 2])
    return pairs, odd_lines, off1


def verify_landmarks(pairs):
    """Byte-level check of the F32 anchor landmarks."""
    assert len(pairs) == 1847, f'expected 1847 pairs, got {len(pairs)}'
    assert len(set(pairs)) == 96, \
        f"expected 96 groups, got {len(set(pairs))}"
    for at in CRIB_AT:
        got = pairs[at:at + 6]
        assert got == CRIB, \
            f'crib landmark @{at}: expected {CRIB}, got {got}'
    return True


def write_pairs_json(path):
    pairs, odd, off1 = load_r5005()
    verify_landmarks(pairs)
    with open(path, 'w') as f:
        json.dump({'pairs': pairs,
                   'meta': {'source': 'R5005 (real)',
                            'parse': 'repaired_offsets.json (F32)',
                            'n_pairs': len(pairs),
                            'n_groups': len(set(pairs)),
                            'odd_lines': odd, 'off1_lines': off1,
                            'crib_landmarks': list(CRIB_AT),
                            'synthetic': False}}, f)
    return pairs


if __name__ == '__main__':
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp/r5005.pairs.json'
    pairs = write_pairs_json(out)
    print(f'R5005: {len(pairs)} pairs, {len(set(pairs))} groups -> {out}')
    print(f'landmarks 11-70-82-34-29-40 @754 and @1034: VERIFIED')
