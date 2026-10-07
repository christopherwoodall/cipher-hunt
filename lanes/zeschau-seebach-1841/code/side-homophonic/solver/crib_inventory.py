#!/usr/bin/env python3
"""Crib-derived inventory for the Seebach homophonic solver.

Built bottom-up from the cribs (cross-fleet memo 2026-10-07, F34/N32),
NOT top-down from standard French.

Tier 1 (crib-attested, highest confidence):
  - 7 pencil cribs: la(11), pre(70), m(82), i(34), er(29), e(40), que(46)
  - By-ear "personne": per|so|nne (93-52-94 @160), pers|on|ne (77-62-94 @508)
  - Polyvalence islets: 06=ent, 94=ne/en, 52=pas/so
  - "la premiere" hyper-fine: pre|m|i|er|e (already in 7 cribs)

Tier 2 (Frenchman-attested by-ear, medium confidence):
  - From phonetic_rules.md R1-R9 evidence

Tier 3 (standard French, LOW confidence, suspect per N29):
  - UNITS from data/upstream-syll.py (audited, not verbatim)
  - Top-200 encipher_split cells (standard syllabifier)

The solver's load_inventory 'crib' mode uses Tier 1 as the core with
high proposal weight, Tier 2 as extension, Tier 3 as fallback.
"""

# Tier 1: crib-attested (pencil cribs + by-ear evidence)
CRIB_CORE = [
    # 7 pencil cribs (anchors)
    'la', 'pre', 'm', 'i', 'er', 'e', 'que',
    # "personne" by-ear, spelling 1: per|so|nne (93-52-94 @160)
    'per', 'so', 'nne',
    # "personne" by-ear, spelling 2: pers|on|ne (77-62-94 @508)
    'pers', 'on', 'ne',
    # polyvalence islets
    'ent',  # 06 (-ment)
    'en',   # 94 (ne/en)
    'pas',  # 52 (pas/so)
]

# Tier 2: Frenchman-attested by-ear (from phonetic_rules.md)
BY_EAR_EXTENDED = [
    # R3: silent consonants dropped ("prend" -> "pre")
    # R5: nasal guards (vowel+n/m before consonant)
    # These are patterns, not specific chunks; the chunks below are
    # examples attested in the rules.
    'gouverne', 'ment',  # example from R11
    'prend', 'pre',      # R3 example (pre already in core)
    'deux', 'deu',       # R? example
]

def get_crib_core():
    """Return the Tier 1 crib-attested chunks (deduplicated, order-preserved)."""
    seen = set()
    out = []
    for c in CRIB_CORE:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out

def get_by_ear_extended():
    """Return Tier 2 by-ear chunks."""
    seen = set(get_crib_core())
    out = []
    for c in BY_EAR_EXTENDED:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out

if __name__ == '__main__':
    core = get_crib_core()
    ext = get_by_ear_extended()
    print(f'Tier 1 (crib core): {len(core)} chunks')
    print(' ', core)
    print(f'Tier 2 (by-ear extended): {len(ext)} chunks')
    print(' ', ext)
