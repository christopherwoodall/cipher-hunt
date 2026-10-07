#!/usr/bin/env python3
"""REAL-DATA ADAPTER -- R5005 pair loader.

*** NOT FOR CONTROL USE. Not imported by solver.py or control_harness.py. ***
Exists so the Runner can feed the real R5005 transcription to the solver AFTER
the control gate passes, without the solver core ever touching real data.

Logic replicates code/crib_attack.py load_pairs() (the verified loader):
per-line offsets from data/upstream-offsets.json choose the pair phase;
a stray edge digit is dropped. Yields (pairs, n_groups).
"""

import json
import os
import re

LANE = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', '..'))
DATA = os.path.join(LANE, 'data')


def load_r5005():
    """Returns (pairs, odd_lines, off1). 1846 pairs / 96 groups expected."""
    offsets = json.load(open(os.path.join(DATA, 'upstream-offsets.json')))
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


def write_pairs_json(path):
    pairs, odd, off1 = load_r5005()
    with open(path, 'w') as f:
        json.dump({'pairs': pairs,
                   'meta': {'source': 'R5005 (real)',
                            'n_pairs': len(pairs),
                            'n_groups': len(set(pairs)),
                            'odd_lines': odd, 'off1_lines': off1,
                            'synthetic': False}}, f)
    return pairs


if __name__ == '__main__':
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp/r5005.pairs.json'
    pairs = write_pairs_json(out)
    print(f'R5005: {len(pairs)} pairs, {len(set(pairs))} groups -> {out}')
    assert len(pairs) == 1846 and len(set(pairs)) == 96
