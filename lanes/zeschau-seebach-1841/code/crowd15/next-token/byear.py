#!/usr/bin/env python3
"""By-ear (clerk-style) fine-cut segmentation for the Seebach R5005 predictor.

The R5005 encipherer cuts finer than standard French syllabification and
spells partly by ear. Ground-truth evidence (all SOLID per
code/sidepath/phonetic_rules.md):

  R9  letter-level cutting:  "la première" = 11-70-82-34-29-40
                              = la|pre|m|i|er|e   (82="m", 34="i", 40="e")
  R4  final -re cut as er|e:  "qui erre" x2 = ...29(er)+40(e); "première" ends er|e
  R1  mute final -e may be its own cell (40="e")
  R3  silent consonants dropped: "prend" written "pre" (silent -d- dropped)
  R8  orthographic doubles spelled once: "erre" -> "er"+"e" (single r sound)
  R2  inconsistent cutting is SOLID -- the clerk is not deterministic.
      This module therefore implements ONE deterministic canonical fine cut,
      not a simulation of the clerk's inconsistency. The standard
      syllabifier (code/side-period/syllabify.py) remains the other mode;
      the applier should query both.

byear_cut(word) pipeline (all steps deterministic, documented):
  1. lowercase, strip accents (model vocabulary is accentless, matching the
     cipher's cell inventory: 70="pre" covers "pré", etc.)
  2. R8 (conservative): collapse "rr"->"r", "nn"->"n" only.
     ("ss"->"s" is NOT collapsed: between vowels it would corrupt [s]->[z].)
  3. R3 (conservative): drop silent word-final -d/-t after a nasal digraph:
     "prend"->"pren", "vient"->"vien", "sont"->"son", "ont"->"on".
     (The frenchman's ear reads "prend" as "pre"; we emit "pren" and record
     the divergence -- see CALIBRATION.md. Never applied to the banked cell
     "est", which the clerk demonstrably wrote with its -t.)
     Final -s/-x/-p dropping (R11) is SPECULATIVE: not applied.
  3b. Word-final -ment -> "m"|"ent" (attested: "ment"=82-06; the three
     ...nement trigrams, e.g. "gouvernement" -> gou|ver|ne|m|ent). Applied
     before R3 so the silent-t drop does not eat it. The stem's final -re
     is [Er] with no schwa -> plain "er", not er|e.
  3c. Word-final -erre -> "er"|"e" (R4/R8: "qui erre" x2 = 29+40).
  4. standard-syllabify the phonetic spelling, then fine-cut transforms:
     a. R4: word-final syllable "re" (word ends in -re) -> ["er","e"].
     b. glide-nucleus split (from "miè"->"m"|"i"): a syllable of shape
        <single consonant> + ("ie"|"iè"|"ia"|"io") -> [C, "i"].
        Single-consonant onsets only: qu/gu/ch/gn/ph/th digraphs never split
        (they are one sound by ear). Not applied to word-initial syllables
        of polysyllabic words? -- no: applied everywhere it matches, e.g.
        "miel" -> m|i|el. Monosyllabic banked cells ("la","le","que","ce",
        "qui","par","est") never match this shape, so they stay whole.
  5. Final -ne / -me splits (R1 + "personne" attestation): word-final -ne ->
     stem + "ne" as one cell ("personne" -> per|so|nne, attested); word-final
     -me -> stem_with_m + "e" ("dame" -> dam|e, per R1's "-me" example).
     This also sidesteps the lane syllabifier's di-nasal lookahead quirk,
     which over-nasalizes these ("persone"->per|sone, "miene"->["miene"]).
     R1 (mute -e as own cell) is NOT applied to other -Ce finals (-le, -se,
     -te, ...): no attestation; conservative.

Returns a list of cell strings. Inverse of nothing: this is a heuristic.
"""
import re
import sys
import unicodedata

sys.path.insert(0, "/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period")
from syllabify import syllabify as _syllabify  # noqa: E402


def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


NASAL_INNER = r"an|en|on|in|un|ain|ein|oin"
NASAL = r"(?:" + NASAL_INNER + r")"
_SINGLE_C = r"[bcdfgjklmnpqrstvwxz]"   # single-letter onsets; no h, no digraphs
_GLIDE_NUC = r"(?:ie|iè|ia|io)"
_BANKED_KEEP = {"est"}                # never phonetically rewrite banked cells


def phonetic_spelling(w):
    """R8 + R3 (conservative). Input/output: accentless lowercase."""
    w = w.replace("rr", "r").replace("nn", "n")          # R8 conservative
    if w not in _BANKED_KEEP:
        # R3: silent final -d/-t after a nasal: prend->pren, vient->vien.
        # (group 1 must be the nasal: NASAL itself is non-capturing.)
        w = re.sub(r"(" + NASAL_INNER + r")[dt]$", r"\1", w)
    return w


def _split_final_ne_me(w):
    """Word-final -ne / -me splits (R1 + "personne" attestation).

    Evidence:
      - "personne" is attested per|so|nne AND pers|on|ne: final "nne"->"ne"
        stays ONE cell (94="ne"). So word-final -ne -> stem + "ne".
      - R1 licenses mute final -e as its own cell with the -me example
        "-me" -> ...+40("e"): the m stays with the stem, the e splits off.
        So word-final -me -> stem_with_m + "e" ("dame" -> dam|e).
    The lane syllabifier over-nasalizes these ("persone"->per|sone,
    "miene"->["miene"]) because of its di-nasal lookahead quirk, so we
    split before syllabifying. Fine-cut philosophy throughout (R9).
    Returns (stem, tail) or (w, None).
    """
    if len(w) > 3:
        m = re.fullmatch(r"(.+)(ne)", w)
        if m:
            return m.group(1), "ne"
    m = re.fullmatch(r"(.+m)(e)", w)
    if m:
        return m.group(1), "e"
    return w, None


def byear_cut(word, _allow_final_re=True):
    w = strip_acc(word.lower().replace("œ", "oe").replace("æ", "ae"))
    if not w:
        return []
    # -ment -> m|ent (attested: "ment"=82-06; 06="-ent" survives in the
    # three ...nement trigrams, e.g. "gouvernement"). Split before the
    # phonetic spelling so R3's silent-t drop does not eat it. The stem's
    # final -re is [Er] with no schwa ("premièrement"=[pr@mjer.mA]),
    # so R4's er|e does NOT fire on the stem (plain "er" instead).
    ment_tail = None
    if w.endswith("ment") and len(w) > 4:
        w, ment_tail = w[:-4], ["m", "ent"]
        _allow_final_re = False
    # -erre -> er|e (R4/R8: "qui erre" x2 = 29(er)+40(e); the double-r
    # collapses to the single heard [R]). Split before phonetic_spelling
    # so the rr-collapse does not eat it.
    erre_tail = None
    if w.endswith("erre") and len(w) >= 4:
        w, erre_tail = w[:-4], ["er", "e"]
    w = phonetic_spelling(w)
    tail = None
    w, tail = _split_final_ne_me(w)
    syls = _syllabify(w)
    out = []
    for i, s in enumerate(syls):
        last = (i == len(syls) - 1) and tail is None
        s = strip_acc(s)
        # R4: word-final -re -> er|e (not for the lone word "re" itself).
        # On a -ment stem the -re is [Er] with no schwa ("premièrement"):
        # emit the clerk's [Er] cell "er" alone (29="er" in "qui erre").
        if last and s == "re" and w.endswith("re") and len(w) > 2:
            out += ["er", "e"] if _allow_final_re else ["er"]
            continue
        # glide-nucleus split: "miè" -> m|i
        m = re.fullmatch(_SINGLE_C + r"(" + _GLIDE_NUC + r")", s)
        if m:
            out += [s[0], "i"]
            continue
        out.append(s)
    if tail:
        out.append(tail)
    if erre_tail:
        out += erre_tail
    if ment_tail:
        out += ment_tail
    return [p for p in out if p]


if __name__ == "__main__":
    for w in sys.argv[1:]:
        std = [strip_acc(p) for p in _syllabify(w)]
        print(f"{w}: std={'-'.join(std)}  byear={'-'.join(byear_cut(w))}")
