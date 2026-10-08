#!/usr/bin/env python3
"""Tokenizer: raw corpus text -> syllable-cell streams (standard and by-ear).

Pipeline per document:
  1. lowercase (accents KEPT for the syllabifier, stripped from cells after).
  2. word regex: [a-z + French accented letters]+ ; internal apostrophes
     (', U+2019) and hyphens split the token:
       - elisions: "l'homme" -> ["l","homme"], "qu'il" -> ["qu","il"],
         "c'est" -> ["c","est"], "m'en" -> ["m","en"], "d'un" -> ["d","un"],
         "s'est" -> ["s","est"], "n'a" -> ["n","a"], "j'ai" -> ["j","ai"].
         The left particle is emitted bare ("l","d","qu","c","m","s","n",
         "j","t","y") -- matching the clerk's cells: "m'en" = 82-84 =
         "m"|"en", "l'est" = 93-59 = "l"|"est".
       - hyphenated compounds split: "arc-en-ciel" -> arc|en|ciel.
  3. dropped: tokens containing digits (years, page numbers), tokens
     longer than 30 chars (OCR garbage), empty tokens.
  4. segmentation per mode:
       standard: lane syllabify.py, then accent-strip each cell.
       byear:    byear.by ear_cut (already accentless).
  5. the stream is a flat list of cells across word boundaries -- the
     cipher is a continuous pair stream, so NO word-boundary markers and
     NO sentence markers are emitted.

Both modes share steps 1-3; only step 4 differs.
"""
import re
import sys
import unicodedata

sys.path.insert(0, "/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period")
sys.path.insert(0, "/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd15/next-token")
from syllabify import syllabify as _syllabify  # noqa: E402
from byear import byear_cut, strip_acc  # noqa: E402

_WORD = re.compile(r"[a-zàâäéèêëîïôöùûüÿçœæ]+")
_APOS = re.compile(r"['\u2019]")
_HYPH = re.compile(r"[-\u2010-\u2015]")


def word_pieces(raw):
    """Split one raw word into encipherable pieces (elisions, hyphens)."""
    pieces = []
    for h in _HYPH.split(raw):
        parts = _APOS.split(h)
        if len(parts) == 2 and parts[0] and parts[1]:
            # elision: "l'homme" -> l | homme. Left particle emitted bare.
            pieces.append(parts[0])
            pieces.append(parts[1])
        elif len(parts) > 2:
            # "l'"+"..." chains or quoted fragments: keep non-empty alphas
            pieces.extend(p for p in parts if p)
        else:
            pieces.append(h)
    return [p for p in pieces if p]


def iter_words(text):
    """Yield cleaned word-pieces from raw text."""
    for m in _WORD.finditer(text.lower()):
        w = m.group(0)
        if any(c.isdigit() for c in w):
            continue
        if len(w) > 30:
            continue
        for p in word_pieces(w):
            if len(p) > 30 or not p:
                continue
            yield p


def segment_stream(text, mode="standard"):
    """Full text -> list of syllable cells. mode: 'standard' | 'byear'."""
    out = []
    for w in iter_words(text):
        if mode == "standard":
            cells = [strip_acc(c) for c in _syllabify(w)]
        elif mode == "byear":
            cells = byear_cut(w)
        else:
            raise ValueError(mode)
        out.extend(c for c in cells if c)
    return out


if __name__ == "__main__":
    demo = "La première dépêche du baron ne prend pas fin. C'est l'homme qu'il m'envoie."
    for mode in ("standard", "byear"):
        print(mode, "->", segment_stream(demo, mode))
