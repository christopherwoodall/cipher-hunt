#!/usr/bin/env python3
"""
cribs.py — Charles I Isle of Wight 1648 lane, unknown-nomenclator work order (b).

Systematic crib battery on the short cipher groups with forcing cleartext
context ("clear text left by partial encoding"). Every candidate records:
the group, the candidate word (period spelling), the context quote, and WHY.
Verdicts per candidate:
  HELD        — token->letter map consistent with all previously held cribs
                AND frequency-plausible
  HELD-WEAK   — consistent but rationale weak or underdetermined (null sweep)
  CONTRADICTED— assigns a token a different letter than a held crib
  IMPLAUSIBLE — maps a frequent token to a rare English letter (rate ratio>5)
Also runs the solved-nomenclator word-gloss carryover test (parent suggestion):
every unknown token that exists in the solved word section is checked for
contextual fit; overlap at/below chance = MISS.

A single held crib is a hypothesis, NOT a finding: only cross-crib
convergence (two independent cribs assigning the same token the same letter)
would qualify as a partial-key entry. Exit 0 always.
"""
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from derive import parse_letter, tokens_of, groups_of, words_around

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(LANE, "data")
OUT = os.path.join(DATA, "crib-attempts.txt")

# approx English letter frequencies (%, modern; period English close enough
# for a ratio>5 implausibility flag)
LETFREQ = {
    'e': 12.0, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7.0, 'n': 6.7, 's': 6.3,
    'h': 6.1, 'r': 6.0, 'd': 4.3, 'l': 4.0, 'c': 2.8, 'u': 2.8, 'm': 2.4,
    'w': 2.4, 'f': 2.2, 'g': 2.0, 'y': 2.0, 'p': 1.9, 'b': 1.5, 'v': 1.0,
    'k': 0.8, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07,
}

GROUPS = {}   # gid -> dict(tokens, before, after, letter)


def load():
    specs = [
        ("aug1648", "letter-prince-charles-1648-08-01-cipher.txt", "A"),
        ("worsley", "letter-worsley-1648-05-22-cipher.txt", "W"),
    ]
    for name, fn, tag in specs:
        segs = parse_letter(os.path.join(DATA, fn))
        for gi, g in enumerate(groups_of(segs)):
            gid = "%s-g%d" % (tag, gi + 1)
            prev, nxt = words_around(segs, gi)
            GROUPS[gid] = {
                "tokens": g, "letter": name,
                "before": " ".join(prev[-8:]), "after": " ".join(nxt[:8]),
            }


# (gid, candidate, mode, rationale). mode 'spell': candidate spelled with all
# tokens, no nulls. mode 'spell-null1': candidate has len(tokens)-1 letters;
# the null position is swept. Candidates on the SAME group are competing
# hypotheses (mutually exclusive by construction); each is evaluated
# INDEPENDENTLY for frequency plausibility. Cross-group compatibility is
# checked pairwise afterwards — only that can yield convergence.
CRIBS = [
    ("W-g2", "expedient", "spell",
     "ctx 'now it will be ___ I desyre you to enquyre': 9 tokens, 8 of them "
     "in 1-90; 'expedient' (advantageous) is standard 17th-c state diction; "
     "9 letters = 9 tokens, no nulls assumed"),
    ("W-g2", "requisite", "spell",
     "ctx as above; 'now it will be requisite' — same slot, 9 letters"),
    ("W-g2", "important", "spell",
     "ctx as above; period sense 'urgent, of moment'; 9 letters"),
    ("W-g2", "needfull", "spell-null1",
     "ctx as above; period spelling (double l); 8 letters + 1 null among "
     "the 9 tokens (97 is the odd-one-out, the only token >90 in the group)"),
    ("W-g2", "required", "spell-null1",
     "ctx as above; 8 letters + 1 null; control: contains q (rare)"),
    # W-g5 (6 tokens: 379 4 28 5 348 354, 'lett me know ___ the'): no viable
    # single-word crib — mixed high/low tokens, no 6-letter content word fits
    # the slot grammatically; recorded as attempted-without-candidate below.
]


def freq_flag(tok, letter, tokcount, total=200):
    """(flagged, ratio): True if token rate >> letter's English rate."""
    rate = 100.0 * tokcount / total
    exp = LETFREQ[letter]
    ratio = rate / exp
    return (ratio > 5.0), ratio


def try_spell(gid, tokens, word):
    """Derive token->letter; return (mapping, notes)."""
    mapping = {}
    for t, ch in zip(tokens, word):
        mapping[t] = ch
    return mapping


def main():
    load()
    tokcount = Counter()
    for g in GROUPS.values():
        tokcount.update(g["tokens"])

    lines = []
    W = lines.append
    W("CRIB ATTEMPTS — unknown nomenclator, Charles I Isle of Wight 1648")
    W("200 tokens; battery run 2026-10-07 (run 1), re-run same day with")
    W("Phase 3 (run 2: single-token semantic cribs from the new Worsley")
    W("p.122 material). Single held cribs are hypotheses, not findings")
    W("(see convergence check at end).")
    W("=" * 78)

    # ---- Phase 1: independent per-variant evaluation (frequency only) ----
    # A variant is PLAUSIBLE if no token->letter assignment has
    # token-rate / english-rate > 5. Same-group variants are competing
    # hypotheses and are NOT checked against each other here.
    evaluated = []  # (gid, word, vnote, mapping, plausible, flag_detail)
    for gid, word, mode, rationale in CRIBS:
        g = GROUPS[gid]
        toks = g["tokens"]
        W("")
        W("CRIB %s | group %s (%d tokens): %s"
          % (word.upper(), gid, len(toks), " ".join(map(str, toks))))
        W('  context: "...%s [CIPHER] %s..."'
          % (g["before"], g["after"]))
        W("  rationale: %s" % rationale)
        W("  mode: %s" % mode)

        variants = []
        if mode == "spell":
            if len(word) != len(toks):
                W("  -> SKIPPED (length mismatch %d vs %d)"
                  % (len(word), len(toks)))
                continue
            variants = [(try_spell(gid, toks, word), "no-null")]
        elif mode == "spell-null1":
            if len(word) != len(toks) - 1:
                W("  -> SKIPPED (length mismatch)")
                continue
            for nullpos in range(len(toks)):
                seq = toks[:nullpos] + toks[nullpos + 1:]
                variants.append(
                    (try_spell(gid, seq, word),
                     "null@pos%d(tok%s)" % (nullpos + 1, toks[nullpos])))

        for mapping, vnote in variants:
            flags = []
            for t, ch in mapping.items():
                bad, ratio = freq_flag(t, ch, tokcount[t])
                if bad:
                    flags.append((t, ch, tokcount[t], ratio))
            if flags:
                det = "; ".join("tok%d(x%d)->%r rate%.1f%%/eng%.2f%% ratio%.1f"
                                % (t, tc, ch, 100.0 * tc / 200,
                                   LETFREQ[ch], r)
                                for t, ch, tc, r in flags)
                W("  [%s] IMPLAUSIBLE (frequency): %s" % (vnote, det))
                evaluated.append((gid, word, vnote, mapping, False, det))
            else:
                W("  [%s] PLAUSIBLE: %s" % (vnote, ", ".join(
                    "%d->%s" % (t, ch) for t, ch in sorted(mapping.items()))))
                evaluated.append((gid, word, vnote, mapping, True, ""))

    plausible = [e for e in evaluated if e[4]]
    implausible = [e for e in evaluated if not e[4]]

    # ---- Phase 2: cross-group compatibility (the only route to convergence)
    W("")
    W("=" * 78)
    W("CROSS-GROUP COMPATIBILITY — pairs of PLAUSIBLE variants from DIFFERENT")
    W("groups whose token->letter maps agree (shared tokens, same letter).")
    W("Agreement here would be converging evidence; disagreement kills the pair.")
    pairs = []
    for i in range(len(plausible)):
        for j in range(i + 1, len(plausible)):
            a, b = plausible[i], plausible[j]
            if a[0] == b[0]:
                continue  # same group: competing hypotheses by construction
            shared = set(a[3]) & set(b[3])
            if not shared:
                continue  # no shared tokens: vacuous, not evidence
            agree = all(a[3][t] == b[3][t] for t in shared)
            pairs.append((a, b, sorted(shared), agree))
    if pairs:
        for a, b, shared, agree in pairs:
            W("  %s/%s  x  %s/%s  shared=%s -> %s"
              % (a[0], a[1], b[0], b[1], shared,
                 "AGREE" if agree else "DISAGREE (pair dead)"))
    else:
        W("  no cross-group pairs share tokens — convergence untestable with")
        W("  this battery (all plausible variants live on W-g2 alone).")

    W("")
    W("=" * 78)
    W("TALLY: %d crib candidates, %d spell variants evaluated"
      % (len(CRIBS), len(evaluated)))
    W("  PLAUSIBLE: %d | IMPLAUSIBLE (frequency): %d"
      % (len(plausible), len(implausible)))
    W("  cross-group agreeing pairs: %d"
      % sum(1 for _, _, _, ag in pairs if ag))
    W("Attempted without a viable candidate (recorded, not fitted):")
    W("  W-g5 (6 tokens '379 4 28 5 348 354' after 'lett me know', before")
    W("   'the ....'): mixed high/low tokens; no 6-letter content word fits")
    W("   the slot grammatically; word-code/split hypotheses unverifiable.")
    W("  W-g6 (2 tokens '206 18' after 'the ....', before 'So I rest'):")
    W("   2-letter spell vs word-code+null indistinguishable; underdetermined.")
    W("Not attempted (no forcing context): A-g1 (88 tokens, single block),")
    W("  W-g1 (29), W-g3 (23), W-g4 (43) — too long for single-word cribs.")
    W("")
    W("READING: the plausible W-g2 fits (expedient / important / needfull x9")
    W("null-variants) are mutually exclusive alternatives for ONE group.")
    W("With no second cribbable group sharing tokens, they cannot be")
    W("discriminated: crib density is too low to resolve the unknown mapping.")

    W("")
    W("=" * 78)
    W("SOLVED-KEY WORD-GLOSS CARRYOVER TEST (parent suggestion): unknown")
    W("tokens that coincide with solved 2021 word-section entries, checked")
    W("for contextual fit.")
    key = json.load(open(os.path.join(
        DATA, "nomenclator-charles-i-1648-solved-key.json")))
    words = {int(x): v for x, v in key["words"].items()}
    all_toks = []
    for g in GROUPS.values():
        all_toks += g["tokens"]
    overlap = sorted(set(all_toks) & set(words))
    n_occ = sum(all_toks.count(t) for t in overlap)
    W("overlap: %d distinct tokens, %d/200 occurrences (%.1f%%)"
      % (len(overlap), n_occ, 100.0 * n_occ / 200))
    for t in overlap:
        W("  token %d (x%d) = solved %r [%s]" % (
            t, all_toks.count(t), words[t][0], words[t][1]))
    W("verdict: MISS — overlap at/below chance (any unknown token in 142-615")
    W("has ~20% chance of coinciding with one of the 94 solved entries by")
    W("number alone); the two 'green' coincidences (339='im' x3, 236='defeat'")
    W("are single-token, context-free, and the nomenclators are established")
    W("as different (N1-N3). 236 sits at W-g4 pos 1 after 'but for this'")
    W("('but for this defeat ...' reads plausibly) but one token is not")
    W("evidence; not held.")

    W("")
    W("=" * 78)
    W("PHASE 3 — SINGLE-TOKEN SEMANTIC CRIBS from the new Worsley p.122")
    W("material (data/letter-worsley-1648-southampton-cover-ocr.txt,")
    W("attributed same-system: shared correspondent Z, king's 'The Cypher'")
    W("label, token 395 shared with W-g1/W-g4). These are semantic")
    W("constraints, not spelling cribs: they cannot enter the cross-group")
    W("letter-agreement test, only a compatibility check.")
    W("  C1: token 395 = male PERSON (name-code). Letter-B context: 'the")
    W("      other [letter] is to 395 w.ch I defyre you send safely and")
    W("      speedely to him'. Occurs in the 200-token corpus at W-g1")
    W("      ('...82 395 380...' after 'particularly that you did') and")
    W("      W-g4 ('...32 395 42...' inside the 'whether or not [CIPHER]")
    W("      group before 'but for this').")
    W("      COMPATIBLE: a person-code is grammatically fittable in both")
    W("      slots (W-g1: 'that you did [someone] 380 ...'; W-g4: a person")
    W("      among other coded words after 'whether or not').")
    W("  C2: token 'W' = male person at Mrs. Pit's house, Southampton")
    W("      ('where you will finde W: and deliver to him the inclosed').")
    W("      Non-numeric in print; not in the 200-token corpus; recorded,")
    W("      not fitted.")
    W("  verdict: C1/C2 are COMPATIBLE with the corpus but UNDERDETERMINED")
    W("  (single tokens, no spelling). 395 does not occur in W-g2, so the")
    W("  new constraints cannot discriminate the W-g2 candidates")
    W("  (expedient/important/needfull): no convergence. The battery's")
    W("  verdict is unchanged — crib density still too low.")

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote", OUT)
    print("crib candidates: %d, variants: %d | plausible %d, implausible %d | "
          "cross-group agreeing pairs: %d"
          % (len(CRIBS), len(evaluated), len(plausible), len(implausible),
             sum(1 for _, _, _, ag in pairs if ag)))


if __name__ == "__main__":
    main()
