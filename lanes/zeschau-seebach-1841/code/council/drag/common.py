#!/usr/bin/env python3
"""Shared machinery for the systematic crib-drag (code/council/systematic-drag.md).

Stream: rebuilt fresh from code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt. NEVER canonical.py (loads the obsolete
1,846-pair parse — known lane bug, cf. 59-frame mapper finding).

Oracle: (group, predecessor, pre2, successor) -> value | None, from
  7 pencil GT (unconditioned) +
  5 provisional (87=ce, 64=qui, 96=par, 59 refined by ISLET 10, 77=le) +
  10 conditioned islets with EXACT rules (islet_registry.md).
A class (96=verb-stem, 66-class, 89-class) is not a value -> None.
"""
import json
import os
import re
import sys
import unicodedata

LANE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
DATA = os.path.join(LANE, 'data')
CORPUS = os.path.join(LANE, 'code', 'side-period', 'corpus')

# ---------------------------------------------------------------- stream
def load_stream():
    offsets = json.load(open(os.path.join(LANE, 'code', 'side-keyhunt',
                                          'repaired_offsets.json')))
    assert offsets.get('a5_03') == 0, 'not the repaired offsets (a5_03 must be 0)'
    pairs = []
    with open(os.path.join(DATA, 'upstream-ct_R5005.txt')) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lid, digits = line.split()
            digits = re.sub(r'\D', '', digits)
            d = digits[offsets.get(lid, 0):]
            for i in range(0, len(d) - 1, 2):
                pairs.append(d[i:i + 2])
    assert len(pairs) == 1847, f'expected 1847 pairs, got {len(pairs)}'
    assert len(set(pairs)) == 96, f'expected 96 groups, got {len(set(pairs))}'
    assert pairs[754:760] == ['11', '70', '82', '34', '29', '40']
    assert pairs[1034:1040] == ['11', '70', '82', '34', '29', '40']
    return pairs

# ------------------------------------------------------- normalization
def strip_acc(s):
    s = s.replace('œ', 'oe').replace('æ', 'ae')
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def norm(s):
    return strip_acc(s).lower()

# ------------------------------------------------------------- tokenizer
def tok_elision(text):
    text = text.replace('-\n', '').replace('-\r\n', '').lower()
    text = re.sub(r"[’‘`]", "'", text)
    text = re.sub(r"\b([a-zàâäéèêëîïôöùûüçœæ]+)'([a-zàâäéèêëîïôöùûüçœæ]+)",
                  r"\1' \2", text)
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+'?|[a-zàâäéèêëîïôöùûüçœæ]+", text)

# ----------------------------------------------------------- syllabifier
# Frozen: code/side-period/syllabify.py (verbatim copy of its core).
NASALS = {"an": "A", "en": "E", "on": "O", "in": "I", "un": "U",
          "ain": "A", "ein": "E", "oin": "W", "aim": "A", "eim": "E"}
KEEP = {"br", "bl", "cr", "cl", "dr", "gr", "gl", "pr", "pl", "tr",
        "fr", "fl", "vr", "vl", "gn", "ch", "ph", "th", "qu", "gu",
        "sc", "sm", "sn", "sp", "st", "chr"}

def syllabify(word):
    w = word.lower().replace("œ", "oe").replace("æ", "ae")
    chars = list(w)
    i, out = 0, []
    while i < len(chars):
        tri = "".join(chars[i:i + 3])
        di = "".join(chars[i:i + 2])
        nxt = chars[i + 3] if i + 3 < len(chars) else ""
        nxt2 = chars[i + 2] if i + 2 < len(chars) else ""
        if tri in NASALS and (not nxt2 or nxt2 not in "aeiouyàâäéèêëîïôöùûüÿ"):
            out.append(NASALS[tri]); i += 3
        elif di in NASALS and (not nxt or nxt not in "aeiouyàâäéèêëîïôöùûüÿ"):
            out.append(NASALS[di]); i += 2
        else:
            out.append(chars[i]); i += 1
    s = "".join(out)
    vowels = set("aeiouyàâäéèêëîïôöùûüÿAEIOUW")
    nuclei = []
    j = 0
    while j < len(s):
        if s[j] in vowels:
            k = j
            while k < len(s) and s[k] in vowels:
                k += 1
            nuclei.append((j, k)); j = k
        else:
            j += 1
    if not nuclei:
        return [word]
    bounds = [0]
    for a in range(len(nuclei) - 1):
        end_prev = nuclei[a][1]
        start_next = nuclei[a + 1][0]
        cons = s[end_prev:start_next]
        n = len(cons)
        if n == 0:
            cut = end_prev
        elif n == 1:
            cut = end_prev
        else:
            if cons[-2:] in KEEP:
                cut = end_prev + n - 2
            elif cons[-1] == cons[-2]:
                cut = end_prev + n - 1
            else:
                cut = end_prev + n - 1
        bounds.append(cut)
    bounds.append(len(s))
    rev = {"A": "an", "E": "en", "O": "on", "I": "in", "U": "un", "W": "oin"}
    parts = []
    for a, b in zip(bounds, bounds[1:]):
        p = s[a:b]
        for k_, v_ in rev.items():
            p = p.replace(k_, v_)
        parts.append(p)
    return [p for p in parts if p]

# ------------------------------------------------------- phrase variants
# V0: plain by-ear (syllabify.py per token).
# V1: consonant-onset splits (clerk over-splitting, GT precedent pre|m|i|er):
#     each V0 syllable C+rest (C single consonant) -> C | rest.
# V2: elision-joined phonetic units (lane by-ear convention: j'ai -> zhay).
VOWELS_NORM = set('aeiouy')

def _v0(tokens):
    out = []
    for t in tokens:
        out.extend(syllabify(t))
    return [norm(s) for s in out if norm(s)]

def _v1(tokens):
    out = []
    for s in _v0(tokens):
        if len(s) >= 2 and s[0] not in VOWELS_NORM and s[1] in VOWELS_NORM:
            out.append(s[0])
            out.append(s[1:])
        else:
            out.append(s)
    return out

_ELIDE_JOIN = {
    "j'ai": 'zhay', "j’ ai": 'zhay',
    "l'est": 'lest', "c'est": 'cest', "n'est": 'nest', "s'est": 'sest',
    "d'est": 'dest', "qu'est": 'kest', "m'est": 'mest', "t'est": 'test',
}

def _v2(tokens):
    # re-join elided token pairs: ["l'", "est"] -> ["l'est"] etc.
    joined = []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.endswith("'") and i + 1 < len(tokens):
            u = t + tokens[i + 1]
            joined.append(u)
            i += 2
        else:
            joined.append(t)
            i += 1
    out = []
    for w in joined:
        wl = w.lower()
        if wl in _ELIDE_JOIN:
            out.append(_ELIDE_JOIN[wl])
        else:
            out.extend(syllabify(w))
    return [norm(s) for s in out if norm(s)]

def phrase_variants(tokens):
    """Return up to 3 variants: [('V0', [...]), ('V1', [...]), ('V2', [...])],
    deduplicated (a variant identical to an earlier one is dropped)."""
    cands = [('V0', _v0(tokens)), ('V1', _v1(tokens)), ('V2', _v2(tokens))]
    seen, out = set(), []
    for name, syls in cands:
        key = tuple(syls)
        if key and key not in seen:
            seen.add(key)
            out.append((name, list(syls)))
    return out

# ---------------------------------------------------------------- oracle
GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er',
      '40': 'e', '46': 'que'}
PROVISIONAL_GROUPS = {'87', '64', '96', '59', '77'}  # anchor-grade

def oracle_value(g, pre, pre2, suc):
    """Exact-rule board oracle. Returns normalized value or None (neutral)."""
    if g in GT:
        return GT[g]
    if g == '87':
        return 'ce'
    if g == '64':
        return 'qui'
    if g == '96':
        # ISLET 5: 96=verb-stem iff pre==64 & suc==47 -> class, not a value
        if pre == '64' and suc == '47':
            return None
        return 'par'
    if g == '59':
        # ISLET 10 refines the provisional: est iff pre in {64,94,93};
        # verb-final -este iff pre==84; else unclassified.
        if pre in ('64', '94', '93'):
            return 'est'
        if pre == '84':
            return 'este'
        return None
    if g == '77':
        return 'le'  # provisional-conditioned, conditioned default
    if g == '84':
        # ISLET 1: 84="en" iff pre in {82,66,89}
        return 'en' if pre in ('82', '66', '89') else None
    if g == '00':
        # ISLET 2: 00="le" iff pre==96
        return 'le' if pre == '96' else None
    if g == '06':
        # ISLET 3: 06="ent" iff pre==82
        return 'ent' if pre == '82' else None
    if g == '67':
        # ISLET 4 fork, exact standing rules (score67_r9.fires_standing)
        et = (pre in ('06', '86') or suc == '64'
              or (pre2 in ('06', '86') and pre == '29')
              or suc == '11'
              or (suc == '77' and pre not in ('21', '11'))
              or suc == '96')
        veut = (pre == '21' or suc == '78' or pre == '11')
        if et and not veut:
            return 'et'
        if veut and not et:
            return 'veut'
        return None
    # ISLET 6/7 (classes), ISLET 8 (frame), ISLET 9 (86 NULL): no values.
    return None

def build_oracle(stream):
    """Oracle array aligned to stream positions; needs full context."""
    n = len(stream)
    arr = []
    for p in range(n):
        g = stream[p]
        pre = stream[p - 1] if p > 0 else None
        pre2 = stream[p - 2] if p > 1 else None
        suc = stream[p + 1] if p < n - 1 else None
        arr.append(oracle_value(g, pre, pre2, suc))
    return arr

def is_anchor_group(g):
    return g in GT or g in PROVISIONAL_GROUPS
