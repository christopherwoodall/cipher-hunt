#!/usr/bin/env python3
"""
derive.py — Charles I Isle of Wight 1648 lane, unknown-nomenclator work order (a)-(b).

Parses the two UNSOLVED letters (1 Aug 1648 to Prince Charles, 88 tokens;
22 May 1648 to Worsley, 112 tokens; 200 total) and produces:

  1. token frequency tables per letter and combined (data/freq-analysis.txt)
  2. token-range distribution vs the solved 2021 nomenclator's structure
     (letter block 1-90 homophonic, nulls 100-107, word section 142-615)
     -> hypothesis about the unknown system's ranges
  3. a crib table: every cipher group with its adjacent cleartext
     (the "clear text left by partial encoding" attack surface)

Exit 0 always. All output goes to data/freq-analysis.txt; nothing here
claims a decode — this is evidence preparation.
"""
import json
import os
import re
from collections import Counter

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(LANE, "data")
OUT = os.path.join(DATA, "freq-analysis.txt")


def parse_letter(path):
    """Ordered segments: ('clear', text) or ('cipher', [int, ...]).
    A cipher group = a maximal run of integers separated ONLY by whitespace
    (numbers may wrap across lines; cleartext words/punctuation end a group)."""
    with open(path) as f:
        text = f.read()
    nums = list(re.finditer(r"\d+", text))
    segs = []            # list of ('clear', str) / ('cipher', [ints])
    cur = []             # tokens of the cipher group being built
    cur_first = None     # start offset of first number in cur
    last_end = 0         # end offset of the last finalized segment
    prev_end = 0         # end offset of the previous number match

    def flush_clear(upto):
        nonlocal last_end
        chunk = text[last_end:upto].strip()
        if chunk:
            segs.append(("clear", chunk))
        last_end = upto

    for m in nums:
        gap = text[prev_end:m.start()]
        if cur and re.fullmatch(r"\s*", gap):
            cur.append(int(m.group(0)))
        else:
            if cur:
                flush_clear(cur_first)      # cleartext before this group
                segs.append(("cipher", cur))
                last_end = prev_end         # end of the cipher group
            cur = [int(m.group(0))]
            cur_first = m.start()
        prev_end = m.end()
    if cur:
        flush_clear(cur_first)
        segs.append(("cipher", cur))
        last_end = prev_end
    flush_clear(len(text))
    return segs


def tokens_of(segs):
    return [t for kind, v in segs for t in (v if kind == "cipher" else [])]


def groups_of(segs):
    return [v for kind, v in segs if kind == "cipher"]


def words_around(segs, gi, before=10, after=10):
    """Cleartext words adjacent to cipher group #gi (within same letter)."""
    groups = [idx for idx, (k, _) in enumerate(segs) if k == "cipher"]
    gi_pos = groups[gi]
    prev_words, next_words = [], []
    for idx in range(gi_pos - 1, -1, -1):
        if segs[idx][0] == "clear":
            prev_words = re.findall(r"[A-Za-z&']+", segs[idx][1])
            break
    for idx in range(gi_pos + 1, len(segs)):
        if segs[idx][0] == "clear":
            next_words = re.findall(r"[A-Za-z&']+", segs[idx][1])
            break
    return prev_words[-before:], next_words[:after]


def range_histogram(tokens):
    buckets = {"1-90": 0, "91-99": 0, "100-107": 0, "108-141": 0,
               "142-615": 0, "616+": 0}
    for t in tokens:
        if 1 <= t <= 90:
            buckets["1-90"] += 1
        elif 91 <= t <= 99:
            buckets["91-99"] += 1
        elif 100 <= t <= 107:
            buckets["100-107"] += 1
        elif 108 <= t <= 141:
            buckets["108-141"] += 1
        elif 142 <= t <= 615:
            buckets["142-615"] += 1
        else:
            buckets["616+"] += 1
    return buckets


def repeated_ngrams(tokens, n=2, min_occ=2):
    c = Counter()
    for i in range(len(tokens) - n + 1):
        c[tuple(tokens[i:i + n])] += 1
    return sorted(((g, k) for g, k in c.items() if k >= min_occ),
                  key=lambda x: (-x[1], x[0]))


def main():
    L = {}
    for name, fn in [("aug1648", "letter-prince-charles-1648-08-01-cipher.txt"),
                     ("worsley", "letter-worsley-1648-05-22-cipher.txt")]:
        L[name] = parse_letter(os.path.join(DATA, fn))

    lines = []
    W = lines.append
    W("FREQUENCY ANALYSIS — Charles I Isle of Wight 1648 unsolved letters")
    W("(unknown nomenclator; published 2021 key shown NOT to fit — N1-N3)")
    W("=" * 78)

    all_tokens = []
    for name, segs in L.items():
        toks = tokens_of(segs)
        all_tokens += toks
        grps = groups_of(segs)
        W("")
        W("LETTER: %s  (%d cipher groups, %d tokens)" % (name, len(grps), len(toks)))
        W("group lengths: %s" % [len(g) for g in grps])
        W("token range: min=%d max=%d distinct=%d"
          % (min(toks), max(toks), len(set(toks))))
        W("")
        W("top-25 tokens:")
        for tok, ct in Counter(toks).most_common(25):
            W("  %4d x%-3d" % (tok, ct))
        W("")
        W("range histogram (solved-2021 section boundaries for comparison):")
        for rng, ct in range_histogram(toks).items():
            W("  %-8s %3d  (%.1f%%)" % (rng, ct, 100.0 * ct / len(toks)))
        W("")
        W("repeated bigrams (>=2x):")
        for g, k in repeated_ngrams(toks, 2)[:12]:
            W("  %s x%d" % (" ".join(map(str, g)), k))
        W("repeated trigrams (>=2x):")
        for g, k in repeated_ngrams(toks, 3)[:12]:
            W("  %s x%d" % (" ".join(map(str, g)), k))

    W("")
    W("=" * 78)
    W("COMBINED (200 tokens)")
    c = Counter(all_tokens)
    W("distinct tokens: %d" % len(c))
    W("top-30 combined:")
    for tok, ct in c.most_common(30):
        W("  %4d x%-3d" % (tok, ct))
    W("")
    W("combined range histogram:")
    for rng, ct in range_histogram(all_tokens).items():
        W("  %-8s %3d  (%.1f%%)" % (rng, ct, 100.0 * ct / len(all_tokens)))
    W("")
    shared = set(tokens_of(L["aug1648"])) & set(tokens_of(L["worsley"]))
    W("tokens shared between the two letters (%d):" % len(shared))
    W("  %s" % sorted(shared))

    W("")
    W("=" * 78)
    W("STRUCTURE HYPOTHESIS (unknown nomenclator ranges)")
    W("Solved-2021 reference: letters 1-90 (homophonic, 24 letters),")
    W("nulls 1/10/58/68/69/78 + 100-107, word section 142-615 (94 entries).")
    low = sum(1 for t in all_tokens if 1 <= t <= 90)
    mid = sum(1 for t in all_tokens if 91 <= t <= 141)
    word = sum(1 for t in all_tokens if 142 <= t <= 615)
    hi = sum(1 for t in all_tokens if t > 615)
    W("- low block 1-90:      %3d/200 (%.1f%%)" % (low, 100.0 * low / 200))
    W("- gap 91-141:          %3d/200 (%.1f%%)" % (mid, 100.0 * mid / 200))
    W("- word zone 142-615:   %3d/200 (%.1f%%)" % (word, 100.0 * word / 200))
    W("- above 615:           %3d/200 (%.1f%%)" % (hi, 100.0 * hi / 200))
    W("Calibration: the KNOWN-key solved 3 Oct 1648 group (67 tokens, 10 groups)")
    W("shows 61.2% low-block / 35.8% word-zone / 3.0% above 615 — the same")
    W("bipartite split. HYPOTHESIS (unverified): the unknown nomenclator shares")
    W("the ARCHITECTURE (homophonic low letter block + high word-code section)")
    W("with different code assignments. Supporting: (i) the split matches;")
    W("(ii) no tokens above 615 in either unknown letter (solved key tops at")
    W("615); (iii) the 91-141 gap is nearly empty in both systems (solved:")
    W("words start at 142). Caution: N3 already showed low-token runs do NOT")
    W("decode with the solved homophones, so the letter-block numbering")
    W("differs; the hypothesis is structural only.")
    W("Notable: token 5 is the most frequent low token (x6) in the unknown")
    W("letters AND the most frequent low token (x3) in the solved control,")
    W("where the solved key reads 5='e'. Consistent with 5='e' in the unknown")
    W("system too — but a different nomenclator makes this coincidence-level;")
    W("recorded as an observation, not evidence.")

    W("")
    W("=" * 78)
    W("CRIB TABLE — cipher groups with adjacent cleartext")
    W("(candidate fits use period spelling; see NOTES.md for attempts/hits)")
    for name, segs in L.items():
        grps = groups_of(segs)
        W("")
        W("--- %s ---" % name)
        for gi, g in enumerate(grps):
            prev, nxt = words_around(segs, gi)
            W("group %d (%d tokens):" % (gi + 1, len(g)))
            W("  BEFORE: ... %s" % " ".join(prev))
            W("  CIPHER: %s" % " ".join(map(str, g)))
            W("  AFTER:  %s ..." % " ".join(nxt))

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote", OUT)
    print("letters parsed:", {k: (len(groups_of(v)), len(tokens_of(v)))
                              for k, v in L.items()})


if __name__ == "__main__":
    main()
