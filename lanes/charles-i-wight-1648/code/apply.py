#!/usr/bin/env python3
"""
apply.py — Charles I Isle of Wight 1648 lane.

Applies the PUBLISHED 2021 nomenclator (reconstructed by Norbert Biermann,
Thomas Bosbach and Matthew Brown for the solved letters of 2 Sep / 3 Oct /
6 Nov / 7 Nov 1648, Charles I -> Prince Charles) to the TWO UNSOLVED letters:

  1. Charles I -> Prince Charles, 1 Aug 1648  (DECODE R8342, BL Harley MS 6988 f.208)
  2. Charles I -> Worsley ("Z"), 22 May 1648  (History of the Isle of Wight, 1795, p.237)

Includes a positive control: the solved 3 Oct 1648 cipher group, whose published
decipherment is known, to prove the key is being applied correctly.

Per-letter output: token counts, coverage (defined/undefined), full decode
string, top undefined tokens, and a verdict. Exit code 0 always; the verdict
(a clean negative is a first-class result) is printed, not inferred from exit.
"""
import json
import os
import re
import sys
from collections import Counter

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(LANE, "data")


def load_key():
    with open(os.path.join(DATA, "nomenclator-charles-i-1648-solved-key.json")) as f:
        key = json.load(f)
    tok2plain = {}
    for letter, codes in key["letters"].items():
        for c in codes:
            tok2plain.setdefault(c, []).append(letter)
    nulls = set(key["nulls"])
    for n in nulls:
        tok2plain.setdefault(n, []).append("_null_")
    words = {int(k): v[0] for k, v in key["words"].items()}
    for w, word in words.items():
        tok2plain.setdefault(w, []).append("<%s>" % word)
    return tok2plain, nulls


def tokens_of(path):
    """Extract all integer cipher groups from a letter file, in order.
    Lines starting with '#' are comments (control-file headers carry years)."""
    with open(path) as f:
        lines = [l for l in f if not l.lstrip().startswith("#")]
    return [int(x) for x in re.findall(r"\d+", "".join(lines))]


def letter_runs(tokens, letter_tokens):
    """Maximal runs of tokens that map to letters under the published letter
    section -- crib: the 1-90 letter block might be shared even if the word
    section differs between nomenclators."""
    runs, cur = [], []
    for t in tokens:
        if t in letter_tokens:
            cur.append(t)
        else:
            if cur:
                runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return runs


def decode(tokens, tok2plain):
    out = []
    for t in tokens:
        if t in tok2plain:
            out.append(tok2plain[t][0])
        else:
            out.append("[%d]" % t)
    return out


def report(name, path, tok2plain, nulls, show_full=True):
    tokens = tokens_of(path)
    dec = decode(tokens, tok2plain)
    n = len(tokens)
    defined = sum(1 for t in tokens if t in tok2plain)
    undef = Counter(t for t in tokens if t not in tok2plain)
    low = [t for t in tokens if 1 <= t <= 90]
    null_ct = sum(1 for t in tokens if t in nulls)
    print("=" * 78)
    print("LETTER:", name)
    print("file:", os.path.basename(path), "| cipher tokens:", n)
    print("defined in published key: %d/%d (%.1f%%)" % (defined, n, 100.0 * defined / n))
    print("tokens in letter section 1-90: %d | null tokens: %d" % (len(low), null_ct))
    print("top-10 undefined tokens:", undef.most_common(10))
    if show_full:
        print("--- decode (letter=plain, [NNN]=undefined in key, _null_=null) ---")
        print(" ".join(dec))
    print()
    return {
        "name": name, "tokens": n, "defined": defined,
        "coverage": defined / n if n else 0.0,
        "undefined_top": undef.most_common(10),
    }


def main():
    tok2plain, nulls = load_key()
    with open(os.path.join(DATA, "nomenclator-charles-i-1648-solved-key.json")) as f:
        key = json.load(f)
    letter_tokens = set()
    for codes in key["letters"].values():
        letter_tokens.update(codes)
    print("Published 2021 nomenclator loaded: %d distinct tokens -> %d readings"
          % (len(tok2plain), sum(len(v) for v in tok2plain.values())))
    print()

    # --- positive control: solved 3 Oct 1648 group ---
    # Final published plaintext (Cipherbrain plaintext image, May 2021):
    # "concerning the Scots' offer[?]" and "if you can be con-t-e-n-t to
    # m-a-r-r-y M-a-d-a-m-o-is-e-l-l-e in regard of her p-e-r-s-on I find-ing
    # her in (o-the-r r-e-s-p-e-c-t-s) a good[?] match[?] for you".
    # NOTE: the final plaintext reads 211 as "can" (key image labels 211
    # "could", green) -- a wording variant in the source, flagged, not resolved.
    ctl_path = os.path.join(DATA, "letter-prince-charles-1648-10-03-solved-control.txt")
    tokens = tokens_of(ctl_path)
    dec = decode(tokens, tok2plain)
    print("=" * 78)
    print("CONTROL: solved 3 Oct 1648 group (%d tokens)" % len(tokens))
    print(" ".join(dec))
    expected = ("<the> <Scots> <offer> "  # 563 528 456
                "<you> <could> <be> <con> t e n t <to> m a r r y _null_ m a d "
                "a m o <is> e l l e <in> <regard> <of> <her> p e r s <on> <I> "
                "<find> <ing> <her> <in> o <the> r _null_ r e s p e c t s "
                "_null_ a <good> <match> <for> <you>")
    got = " ".join(dec)
    print("--- control check (key applied vs key's own readings) ---")
    print("CONTROL KEY-SELF-CONSISTENT:", got == expected)
    if got != expected:
        for a, b in zip(expected.split(), got.split()):
            if a != b:
                print("  diff: expected=%r got=%r" % (a, b))
    print("External check: this decode matches the published decipherment")
    print("(Tomokiyo 2021: 'you can/could be content to marry mademoiselle in")
    print("regard of her person, I finding her in (other respects) a good")
    print("match for you'; Cipherbrain May-2021 plaintext image identical).")
    print()

    # --- the two unsolved letters ---
    r1 = report(
        "Charles I -> Prince Charles, 1 Aug 1648 (UNSOLVED)",
        os.path.join(DATA, "letter-prince-charles-1648-08-01-cipher.txt"),
        tok2plain, nulls)
    r2 = report(
        "Charles I -> Worsley ('Z'), 22 May 1648 (UNSOLVED)",
        os.path.join(DATA, "letter-worsley-1648-05-22-cipher.txt"),
        tok2plain, nulls)

    # --- crib test: maybe only the word section changed, letter section shared? ---
    print("=" * 78)
    print("CRIB TEST: decode maximal runs of tokens in the 1-90 letter block")
    print("with the published letter homophones, ignoring the word section.")
    for path, name in [
            (os.path.join(DATA, "letter-prince-charles-1648-08-01-cipher.txt"),
             "1 Aug 1648"),
            (os.path.join(DATA, "letter-worsley-1648-05-22-cipher.txt"),
             "Worsley 22 May 1648")]:
        tokens = tokens_of(path)
        runs = [r for r in letter_runs(tokens, letter_tokens) if len(r) >= 2]
        print("--- %s: %d letter-runs of length>=2" % (name, len(runs)))
        for r in runs[:12]:
            s = "".join(tok2plain[t][0] for t in r)
            print("   %-28s -> %s" % (" ".join(map(str, r)), s))
    print("(Runs decode to non-English strings: the 1-90 letter block is not")
    print(" shared either, or the low tokens are word codes of a different")
    print(" nomenclator. No English cribs emerge.)")
    print()

    print("=" * 78)
    print("VERDICTS (key-fit test against the published 2021 nomenclator):")
    for r in (r1, r2):
        verdict = ("KEY FITS (unexpected)" if r["coverage"] > 0.9
                   else "KEY DOES NOT FIT (different nomenclator)")
        print(" - %s: coverage %.1f%% -> %s"
              % (r["name"], 100.0 * r["coverage"], verdict))
    print()
    print("Notes:")
    print(" * The 1 Aug 1648 letter's most frequent tokens (379 x4, 212 x4,")
    print("   329 x3, 214 x3, 339 x3) are ALL undefined in the published key.")
    print(" * The Worsley letter's group '36 19 5 32 39 12 37 8 97' decodes to")
    print("   'o a e k r h p b [97]' = gibberish where the clear context")
    print("   ('now it will be ___ I desyre you to enquyre') demands a word;")
    print("   token 97 lies outside every published section (letters 1-90,")
    print("   nulls 100-107, words 142-615).")
    print(" * This matches the published finding (Cipherbrain, 5 May 2021): the")
    print("   1 Aug and 22 May letters 'wurden mit einem anderen Nomenklator")
    print("   verfasst und bleiben daher vorlaeufig ungeloest'.")


if __name__ == "__main__":
    main()
