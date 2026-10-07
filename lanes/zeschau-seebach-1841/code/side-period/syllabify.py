#!/usr/bin/env python3
"""Rough French syllabifier for crib cards (heuristic, hand-checked per entry).
Conventions: maximal-onset, obstruent+l/r and gn/ch/ph/th/qu/gu kept together,
double consonants split, nasal digraphs are single nuclei, final mute -e kept
as its own tail only where standard French does (e.g. 'livre' -> li-vre is
WRONG here; we emit 'liv-re'? no: standard is li-vre).
NOTE: the R5005 encipherer cuts finer than standard (premiere = pre|m|i|er),
so cards also carry by-ear / alternative cut notes.
"""
import re, unicodedata, sys

def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")

NASALS = {"an": "A", "en": "E", "on": "O", "in": "I", "un": "U",
          "ain": "A", "ein": "E", "oin": "W", "aim": "A", "eim": "E"}
KEEP = {"br", "bl", "cr", "cl", "dr", "gr", "gl", "pr", "pl", "tr",
        "fr", "fl", "vr", "vl", "gn", "ch", "ph", "th", "qu", "gu",
        "sc", "sm", "sn", "sp", "st", "chr"}

def syllabify(word):
    w = word.lower().replace("œ", "oe").replace("æ", "ae")
    # protect nasal digraphs before consonant/end
    chars = list(w)
    i, out = 0, []
    while i < len(chars):
        tri = "".join(chars[i:i+3])
        di = "".join(chars[i:i+2])
        nxt = chars[i+3] if i+3 < len(chars) else ""
        nxt2 = chars[i+2] if i+2 < len(chars) else ""
        if tri in NASALS and (not nxt2 or nxt2 not in "aeiouyàâäéèêëîïôöùûüÿ"):
            out.append(NASALS[tri]); i += 3
        elif di in NASALS and (not nxt or nxt not in "aeiouyàâäéèêëîïôöùûüÿ"):
            out.append(NASALS[di]); i += 2
        else:
            out.append(chars[i]); i += 1
    s = "".join(out)
    vowels = set("aeiouyàâäéèêëîïôöùûüÿAEIOUW")
    # find nuclei (vowel groups; y between vowels counts as consonant)
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
        start_next = nuclei[a+1][0]
        cons = s[end_prev:start_next]
        n = len(cons)
        if n == 0:
            cut = end_prev
        elif n == 1:
            cut = end_prev  # single consonant -> right
        else:
            if cons[-2:] in KEEP:
                cut = end_prev + n - 2
            elif cons[-1] == cons[-2]:
                cut = end_prev + n - 1
            else:
                cut = end_prev + n - 1
        bounds.append(cut)
    bounds.append(len(s))
    # restore nasals
    rev = {"A": "an", "E": "en", "O": "on", "I": "in", "U": "un", "W": "oin"}
    parts = []
    for a, b in zip(bounds, bounds[1:]):
        p = s[a:b]
        for k, v in rev.items():
            p = p.replace(k, v)
        parts.append(p)
    return [p for p in parts if p]

if __name__ == "__main__":
    for w in sys.argv[1:]:
        print(w, "->", "-".join(syllabify(w)))
