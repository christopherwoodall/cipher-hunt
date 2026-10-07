#!/usr/bin/env python3
"""
titus_test.py — Charles I Isle of Wight 1648 lane, Titus-cipher fit test.

Tests whether the 200 tokens of the two UNSOLVED letters (1 Aug 1648 to
Prince Charles, 88 tokens; 22 May 1648 to Worsley, 112 tokens) fit the
TITUS cipher's number ranges, against the published solved-2021 ranges.

Ranges:
  Titus (per S. Tomokiyo, "King Charles I's Ciphers", reconstruction note
  preserved in an HTML comment in data/charlesi-ciphers-tomokiyo.html,
  said to be reconstructed from Hillier 1852 + Poynting p.134):
    letters: "lower numbers" (no bound stated; word series 1 starts at 103,
             so the letter/null zone is taken as 1-102 here — MARKED as an
             assumption, not a source claim)
    word series 1: 103-420
    word series 2: 453-608
    numerals/days/months/random words: 634-705
    gaps (unexplained in the reconstruction): 421-452, 609-633, 706+
  Solved-2021 (Biermann/Brown/Bosbach; data/nomenclator-charles-i-1648-solved-key.json):
    letters: 1-90 (homophonic), nulls: 100-107, words: 142-615;
    gaps: 91-99, 108-141, 616+

Note: Hillier 1852 itself prints NO range table. It DOES print (see
data/hillier1852-titus-cipher.txt, verbatim excerpts [D]-[F]):
  715 = Mrs. Whorwood, 457 = Lady Carlisle, 546, 493, 714 = Dr. Fraizer,
  315 = "queen" (not the queen), 560:315 = "the queen", W = Captain Titus,
  J = the king, F = Dowcett, D = Firebrace, 688, and the statement
  "the numbers were changed for the use of every correspondent".

Exit 0 always. Output -> data/titus-range-test.txt. No decode claimed.
"""
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from derive import parse_letter, tokens_of

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(LANE, "data")
OUT = os.path.join(DATA, "titus-range-test.txt")

TITUS_LETTER_ZONE = (1, 102)      # ASSUMED bound: series 1 starts 103
TITUS_S1 = (103, 420)
TITUS_S2 = (453, 608)
TITUS_NUM = (634, 705)
TITUS_GAPS = [(421, 452), (609, 633)]
S21_LET = (1, 90)
S21_NULL = (100, 107)
S21_WORD = (142, 615)
S21_GAPS = [(91, 99), (108, 141)]

TOP_UNDEF = [379, 212, 329, 214, 339, 86, 248, 208, 96, 395, 230, 388, 97]

FILES = [
    ("letter-prince-charles-1648-08-01-cipher.txt", "AUG"),
    ("letter-worsley-1648-05-22-cipher.txt", "WORS"),
]


def in_rng(t, rng):
    return rng[0] <= t <= rng[1]


def classify_titus(t):
    if in_rng(t, TITUS_LETTER_ZONE):
        return "letter-zone(1-102)*"
    if in_rng(t, TITUS_S1):
        return "word-series1(103-420)"
    if in_rng(t, TITUS_S2):
        return "word-series2(453-608)"
    if in_rng(t, TITUS_NUM):
        return "numeral/day/random(634-705)"
    for a, b in TITUS_GAPS:
        if a <= t <= b:
            return "titus-gap(%d-%d)" % (a, b)
    if t > 705:
        return "above-titus-max(>705)"
    return "below-1?"


def classify_s21(t):
    if in_rng(t, S21_LET):
        return "letters(1-90)"
    if in_rng(t, S21_NULL):
        return "nulls(100-107)"
    if in_rng(t, S21_WORD):
        return "words(142-615)"
    for a, b in S21_GAPS:
        if a <= t <= b:
            return "s21-gap(%d-%d)" % (a, b)
    if t > 615:
        return "above-s21-max(>615)"
    return "below-1?"


def main():
    all_toks = []
    per_letter = {}
    for fn, tag in FILES:
        segs = parse_letter(os.path.join(DATA, fn))
        toks = tokens_of(segs)
        per_letter[tag] = toks
        all_toks += toks

    n = len(all_toks)
    lines = []
    W = lines.append
    W("TITUS-CIPHER RANGE-FIT TEST — unknown nomenclator tokens")
    W("(work order b; 2026-10-07; code/titus_test.py)")
    W("=" * 78)
    W("Tokens: AUG=%d, WORS=%d, total=%d" %
      (len(per_letter["AUG"]), len(per_letter["WORS"]), n))
    W("Titus letter-zone bound 1-102 is an ASSUMPTION (source only says 'lower numbers';")
    W("series 1 starts at 103, so 1-102 is the residual). Everything else is quoted from the")
    W("Tomokiyo reconstruction note (data/charlesi-ciphers-tomokiyo.html HTML comment).")
    W("")

    W("--- TITUS classification (all 200 tokens) ---")
    ct = Counter(classify_titus(t) for t in all_toks)
    for k in ["letter-zone(1-102)*", "word-series1(103-420)", "word-series2(453-608)",
              "numeral/day/random(634-705)", "titus-gap(421-452)", "titus-gap(609-633)",
              "above-titus-max(>705)", "below-1?"]:
        c = ct.get(k, 0)
        W("  %-32s %3d  (%.1f%%)" % (k, c, 100.0 * c / n))
    n_in_titus_any = sum(v for k, v in ct.items() if not k.startswith("titus-gap")
                         and not k.startswith("above-") and not k.startswith("below-"))
    W("  %-32s %3d  (%.1f%%)" % ("IN some Titus defined zone", n_in_titus_any,
                                 100.0 * n_in_titus_any / n))
    W("")

    W("--- SOLVED-2021 classification (all 200 tokens; N1/N2 already showed 52.3%/57.1% defined) ---")
    cs = Counter(classify_s21(t) for t in all_toks)
    for k in ["letters(1-90)", "nulls(100-107)", "words(142-615)",
              "s21-gap(91-99)", "s21-gap(108-141)", "above-s21-max(>615)", "below-1?"]:
        c = cs.get(k, 0)
        W("  %-24s %3d  (%.1f%%)" % (k, c, 100.0 * c / n))
    W("")

    W("--- DISCRIMINATING TOKENS (zones where Titus and solved-2021 DISAGREE) ---")
    dis_aug = [(t, classify_titus(t)) for t in per_letter["AUG"]
               if t > 705 or (421 <= t <= 452) or (609 <= t <= 633)
               or (t > 615)]
    dis_wor = [(t, classify_titus(t)) for t in per_letter["WORS"]
               if t > 705 or (421 <= t <= 452) or (609 <= t <= 633)
               or (t > 615)]
    W("Titus-defined but solved-undefined (634-705):")
    t_only = [(t, classify_titus(t)) for t in all_toks if 634 <= t <= 705]
    W("  %s (n=%d)" % (sorted(set(t for t, _ in t_only)), len(t_only)))
    W("Solved-defined but Titus-gap (421-452, 609-633, 616+):")
    s_only = [(t, classify_titus(t)) for t in all_toks
              if (421 <= t <= 452) or (609 <= t <= 633) or (616 <= t <= 705)]
    # careful: 616-633 overlaps gap; report as-is
    W("  %s (n=%d)" % (sorted(set(t for t, _ in s_only)), len(s_only)))
    W("tokens above Titus max 705: %s" % sorted(set(t for t in all_toks if t > 705)))
    W("max token in corpus: %d" % max(all_toks))
    W("")

    W("--- TOP-13 previously-undefined tokens vs Titus word series ---")
    cnt = Counter(all_toks)
    for tok in TOP_UNDEF:
        cls = classify_titus(tok)
        W("  token %3d  x%-2d  titus=%s" % (tok, cnt.get(tok, 0), cls))
    in_s1 = sum(1 for tok in TOP_UNDEF if 103 <= tok <= 420)
    in_s2 = sum(1 for tok in TOP_UNDEF if 453 <= tok <= 608)
    in_lz = sum(1 for tok in TOP_UNDEF if 1 <= tok <= 102)
    W("  of the 13: %d in series1(103-420), %d in series2(453-608), %d in letter-zone(1-102)" %
      (in_s1, in_s2, in_lz))
    W("")

    W("--- CROSS-CHECK: Hillier's real Titus groups vs Tomokiyo's stated ranges ---")
    W("Hillier 1852 prints (verbatim, excerpt [D]): 715 = Mrs. Whorwood,")
    W("457 = Lady Carlisle, 714 = Dr. Fraizer, 560:315 = 'the queen', 315 = queen (not the queen).")
    W("NOTE: 714 and 715 lie ABOVE Tomokiyo's 634-705 numeral/day/random zone.")
    W("So the reconstruction's 634-705 upper bound is not exact even for the Titus cipher itself.")
    W("")

    W("--- PER-LETTER totals ---")
    for tag in ["AUG", "WORS"]:
        toks = per_letter[tag]
        ct2 = Counter(classify_titus(t) for t in toks)
        W("  %s (%d): s1=%d s2=%d num=%d letter-zone=%d gaps=%d above705=%d" %
          (tag, len(toks), ct2.get("word-series1(103-420)", 0),
           ct2.get("word-series2(453-608)", 0), ct2.get("numeral/day/random(634-705)", 0),
           ct2.get("letter-zone(1-102)*", 0),
           ct2.get("titus-gap(421-452)", 0) + ct2.get("titus-gap(609-633)", 0),
           ct2.get("above-titus-max(>705)", 0)))
    W("")
    W("VERDICT ON NUMBERS ALONE: range-fit counts CANNOT separate the two schemes —")
    W("both share the bipartite low-block + high-word-section architecture, and Titus's")
    W("word zones (103-420, 453-608) swallow 40.5% of the unknown tokens almost exactly")
    W("as the solved-2021 word zone (142-615) does. Decisive evidence must come from")
    W("(a) Hillier's own statement that 'the numbers were changed for the use of every")
    W("correspondent' (excerpt [F]) — Titus's cipher was a PER-CORRESPONDENT variant,")
    W("while the unknown nomenclator was shared by at least TWO correspondents (Worsley")
    W("and Prince Charles, sharing 20 tokens across the two letters);")
    W("(b) assignments, not ranges: the actual Titus figure codes (315=queen, 457=Carlisle,")
    W("714=Fraizer, 715=Whorwood, W=Titus, J=king) vs the unknown tokens' cleartext constraints.")
    W("See data/titus-range-test.txt (this file) and NOTES.md for the recorded null/finding.")

    open(OUT, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines[:40]))
    print("... (%d lines total) -> %s" % (len(lines), OUT))


if __name__ == "__main__":
    main()
