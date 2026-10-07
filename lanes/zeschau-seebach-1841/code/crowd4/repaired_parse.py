#!/usr/bin/env python3
"""Repaired canonical parse loader — round 4, WO8 parse update (2026-10-07).

The lane's canonical parse was repaired (key-hunt side fleet, red-team
verified): offsets['a5_03'] flipped 1 -> 0. New canonical: 1,847 pairs
(not 1,846). Canonical offsets: code/side-keyhunt/repaired_offsets.json
(supersedes data/upstream-offsets.json).

This module provides load_pairs_repaired() which applies the REPAIRED
offsets. crib_attack.load_pairs() still uses the old offsets; do not use
it for R5005 work going forward.

Re-indexing (0-based, old -> new):
- old n < 748 -> new n (unchanged)
- 748 <= old n <= 772 -> REPAIRED REGION (row a5_03 re-paired; values changed)
- old n >= 773 -> new n+1 (values identical, index shifted)

New canonical facts:
- 11 70 82 34 29 40 ("la première") at pairs 754 AND 1034 (0-based).
"""

import json
import os
import re

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
DATA = os.path.join(LANE, 'data')
REPAIRED_OFFSETS = os.path.join(LANE, 'code', 'side-keyhunt',
                                'repaired_offsets.json')


def load_pairs_repaired():
    """Load the repaired canonical 1,847-pair stream.

    Returns (pairs, odd_lines, off1) like crib_attack.load_pairs.
    """
    offsets = json.load(open(REPAIRED_OFFSETS))
    pairs, odd_lines, off1 = [], 0, 0
    for line in open(os.path.join(DATA, 'upstream-ct_R5005.txt')):
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
    assert len(pairs) == 1847, len(pairs)
    assert len(set(pairs)) == 96, len(set(pairs))
    # canonical anchor: "la première" twice
    assert pairs[754:760] == ['11', '70', '82', '34', '29', '40'], pairs[754:760]
    assert pairs[1034:1040] == ['11', '70', '82', '34', '29', '40'], pairs[1034:1040]
    return pairs, odd_lines, off1


def reindex(old_n):
    """Map an old-parse 0-based pair index to the repaired parse."""
    if old_n < 748:
        return old_n
    if old_n <= 772:
        return None  # repaired region: values changed, do not shift
    return old_n + 1
