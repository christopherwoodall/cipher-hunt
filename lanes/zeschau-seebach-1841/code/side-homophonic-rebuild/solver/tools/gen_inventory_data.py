#!/usr/bin/env python3
"""One-shot generator for inventory_data.json (rebuild, 2026-10-07).

Reproduces the FROZEN solver's Tier-3 / 'units' inventory inputs using the
frozen pipeline, then freezes the OUTPUT as data so the rebuild solver never
imports the fragile crowd2 chain (scorer_smith -> crib_attack) at runtime.

Frozen inputs reproduced verbatim:
  UNITS:  data/upstream-syll.py  via regex  UNITS = list('...') + '''...'''.split()
  top-200 encipher_split cells: scorer_smith.syllabify/encipher_split over
            build_lm.load_words() (Tocqueville corpus), Counter.most_common(200)

The rebuild's load_inventory() must produce EXACTLY the frozen 'crib'
inventory plus the 5 accented by-ear forms (vê/té/né/vres/my); verified by
tools/check_inventory_parity.py (not shipped; run once here).
"""
import collections
import hashlib
import json
import os
import re
import sys

LANE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code'))          # crib_attack
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd2'))  # scorer_smith
sys.path.insert(0, os.path.join(LANE, 'code', 'side-homophonic', 'solver'))  # build_lm

from scorer_smith import syllabify, encipher_split  # noqa: E402
from build_lm import load_words  # noqa: E402


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def main():
    # --- UNITS (frozen regex, verbatim) ---
    up = os.path.join(LANE, 'data', 'upstream-syll.py')
    src = open(up).read()
    m = re.search(r"UNITS = list\('([^']+)'\) \+ '''(.*?)'''\.split\(\)", src, re.S)
    units = list(m.group(1)) + m.group(2).split()

    # --- top-200 encipher_split cells (frozen computation, verbatim) ---
    cnt = collections.Counter()
    for w in load_words():
        for c in encipher_split(syllabify(w)):
            cnt[c] += 1
    top200 = [c for c, _ in cnt.most_common(200)]

    out = {
        'provenance': {
            'generated': '2026-10-07',
            'by': 'code/side-homophonic-rebuild/solver/tools/gen_inventory_data.py',
            'units_source': 'data/upstream-syll.py',
            'units_sha256': sha(up),
            'top200_pipeline': ('scorer_smith.syllabify/encipher_split over '
                                'build_lm.load_words(), most_common(200)'),
            'scorer_smith_sha256': sha(os.path.join(LANE, 'code', 'crowd2', 'scorer_smith.py')),
            'build_lm_sha256': sha(os.path.join(LANE, 'code', 'side-homophonic', 'solver', 'build_lm.py')),
            'n_units': len(units),
            'n_top200': len(top200),
        },
        'units': units,
        'tier3_top200': top200,
    }
    dest = os.path.join(os.path.dirname(__file__), '..', 'inventory_data.json')
    json.dump(out, open(dest, 'w'), ensure_ascii=False, indent=1)
    print(f'wrote {dest}: {len(units)} units, {len(top200)} top200')


if __name__ == '__main__':
    main()
