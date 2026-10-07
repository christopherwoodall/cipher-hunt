#!/usr/bin/env python3
"""By-ear tiler for the Seebach word-pattern re-drive (crowd6/inventorist).

Re-syllabifies the 11,870-word era lexicon under the F44 24-unit crib-learned
inventory, replacing the standard-French syllabification that killed the old
instrument (N32: 'm' as a syllable in 1/11,870 entries; ground-truth
"premiere" = pre|m|i|er|e unmatchable).

Inventory unit strings (F44):
  Tier 0 (GT): la pre m i er e que
  Tier 1 (inferred): ce qui par ne veut on me le        (06=verb-stem-class: no string)
  Tier 2 (polyvalence islets): ent pas so se en
Cutting rules honored: R1 (1-4 letters, 1-letter cells exist), R2 (by-ear,
inconsistent -> generate the SET of tilings, top-K), R3 (mute -e written),
R4 (mixed table). Accents stripped: the inventory attests only unaccented
unit strings (pre, er, e), so cells are compared unaccented (disclosed).

Scoring (calibrated on attested cuts — see CALIBRATION below):
  cell known in inventory      +6.0  (+1.0 onset-cluster bonus, CCV/CCCV)
  cell len 1 (not known)      +2.5   (R1: single letters are proven cells)
  cell len 2 (not known)      +1.2
  cell len 3 (not known)      +0.6
  cell len 4 (not known)      +0.3
  tiling penalty               -3.0 per cell  (the encipherer does not maximally
      split: 'pre' stays together while 'mi' splits -> penalty must exceed 2.6;
      3.0 chosen, calibrated)

CALIBRATION (ground-truth, disclosed):
  "premiere" -> top-1 [pre,m,i,er,e]  (pencil crib, 11-70-82-34-29-40)
  "personne" -> [pers,on,ne] and [per,so,nne] in top-K  (frenchman, @159/@507)
  "cela"     -> top-1 [ce,la]          (87-11 x7)
Single-letter function words (la/ne/pas/par/qui/le/on/me/que) -> top-1 [self].

Stdlib only. Deterministic.
"""
import json
import os
import re
import unicodedata

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
LEXD = os.path.join(LANE, 'code', 'side-wordpattern', 'lexicon')

# F44 inventory unit strings (06=verb-stem-class excluded: not a cell string)
KNOWN = frozenset([
    # Tier 0 - pencil-crib PROOF
    'la', 'pre', 'm', 'i', 'er', 'e', 'que',
    # Tier 1 - lane-inferred (status-marked; strings as attested)
    'ce', 'qui', 'par', 'ne', 'veut', 'on', 'me', 'le',
    # Tier 2 - conditioned polyvalence islets
    'ent', 'pas', 'so', 'se', 'en',
])

VOWELS = set('aeiouy')
CONS = set('bcdfghjklmnpqrstvwxz')
_ONSET2 = re.compile(r'^[bcdfghjklmnpqrstvwxz]{2}[aeiouy]')
_ONSET3 = re.compile(r'^[bcdfghjklmnpqrstvwxz]{3}[aeiouy]')


def normalize(word):
    """Lowercase, strip diacritics (inventory is unaccented)."""
    w = word.lower()
    w = unicodedata.normalize('NFD', w)
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    w = w.replace('ç', 'c').replace('œ', 'oe').replace('æ', 'ae')
    # keep only a-z (drop apostrophes/hyphens: "l'" handled by lexicon tokenization)
    w = re.sub(r'[^a-z]', '', w)
    return w


def cell_score(cell):
    if cell in KNOWN:
        s = 6.0
    elif len(cell) == 1:
        s = 2.5
    elif len(cell) == 2:
        s = 1.2
    elif len(cell) == 3:
        s = 0.6
    else:
        s = 0.3
    if len(cell) <= 4 and (_ONSET3.match(cell) or _ONSET2.match(cell)):
        s += 1.0
    return s


CELL_PENALTY = 3.0
BEAM = 500


def tile(word, k=8):
    """Top-k by-ear tilings of `word` (normalized). Returns [(cells, score)]."""
    w = normalize(word)
    n = len(w)
    if n == 0:
        return []
    # beam: list of (pos, cells_tuple, score)
    beam = [(0, (), 0.0)]
    done = []
    while beam:
        nxt = []
        for pos, cells, score in beam:
            for L in (1, 2, 3, 4):
                if pos + L > n:
                    continue
                c = w[pos:pos + L]
                ns = score + cell_score(c) - CELL_PENALTY
                ncells = cells + (c,)
                if pos + L == n:
                    done.append((ncells, ns))
                else:
                    nxt.append((pos + L, ncells, ns))
        # prune beam by score
        nxt.sort(key=lambda t: -t[2])
        # dedupe by cells (keep best score)
        seen = {}
        pruned = []
        for pos, cells, score in nxt:
            if cells not in seen:
                seen[cells] = True
                pruned.append((pos, cells, score))
        beam = pruned[:BEAM]
    # dedupe done, keep best score per tiling, sort, take k
    best = {}
    for cells, score in done:
        if cells not in best or score > best[cells]:
            best[cells] = score
    ranked = sorted(best.items(), key=lambda kv: -kv[1])
    return [(list(c), s) for c, s in ranked[:k]]


def load_lexicon():
    lex = []
    with open(os.path.join(LEXD, 'lexicon.jsonl')) as f:
        for line in f:
            e = json.loads(line)
            lex.append(e)
    return lex


if __name__ == '__main__':
    # calibration checks
    checks = [
        ('première', ['pre', 'm', 'i', 'er', 'e'], 1),
        ('personne', ['pers', 'on', 'ne'], 8),
        ('personne', ['per', 'so', 'nne'], 8),
        ('cela', ['ce', 'la'], 1),
        ('lumière', ['lu', 'm', 'i', 'er', 'e'], 8),
    ]
    ok = True
    for word, want, topk in checks:
        tilings = tile(word, k=8)
        found = [i + 1 for i, (c, s) in enumerate(tilings) if c == want]
        status = 'OK ' if (found and found[0] <= topk) else 'FAIL'
        if status == 'FAIL':
            ok = False
        print(f"[{status}] {word} -> want {want}: rank "
              f"{found[0] if found else 'ABSENT'}; top3 = "
              f"{[c for c, s in tilings[:3]]}")
    print('CALIBRATION', 'PASS' if ok else 'FAIL')
