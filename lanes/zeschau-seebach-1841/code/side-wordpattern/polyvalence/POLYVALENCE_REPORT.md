# Polyvalence stress-test — Seebach word-pattern matcher gate

**Verdict: VALID-WITH-RESTRICTIONS** (restrictions §5, precise and implementable).
Date 2026-10-07. Code: `code/side-wordpattern/polyvalence/`
(`polyvalence_test.py`, `synthetic_breakdown.py`, `results.json`,
`synthetic_breakdown.json`). All enumeration exact (no sampling noise);
Monte Carlo (2 seeds) cross-validates.

## 1. Threat formalization

The cipher's established polyvalence (NOTES.md F24/F25/F31/N23/K5), in
lexicon-phonetic terms (mute-e dropped: ne→"n", se→"s", en→"an"):

| group | readings | status | cipher evidence |
|---|---|---|---|
| 06 | /mɑ̃/ {"man","mant"} vs /ɑ̃/ {"an","ant"} | plausible, not confirmed (F25) | 06 ×46; 94-82-06 ×3 ("ent"); demand-islets (model killed N17, tension open) |
| 94 | "ne"→"n" vs "en"→"an" | ne provisional-strong; en islets LEAD | 94 ×36; 94→82 ×4; en-islets @1168 (94-87-83), @1575 (82-94-76) |
| 52 | "pas" vs "se"→"s" | pas STRONG bounded; se LEAD; K5 forces polyvalence | 52 ×27; 94→52 ×3 ("ne se"); 52 word-internal @160 |
| 59 | "se"→"s" | LEAD | 94→59 ×2 ("ne se") → se→{52,59} split, 0.6/0.4 observed |

Two distortion directions, both modeled:
- **Merge** (different syllables → same group): plaintext ABC enciphers to
  cipher AAB/ABA/ABB. Needs two *distinct* syllables sharing a poly group
  in one word (e.g. "ennemi" an-n-mi → [94,94,X] → AAB).
- **Split** (same syllable → different groups): plaintext ABA enciphers to
  ABC. Needs a repeated polyvalent syllable with ≥2 group options
  (e.g. "sérieuse" s-rieu-s → [52,X,59] → ABC).

Per-position model: a polyvalent syllable takes a poly group w.p. q
(penetration, swept 0.05–0.9 — not identified from data), else a unique
canonical placeholder. "se"→52/59 weighted 0.6/0.4 (observed 3/5 vs 2/5 in
"ne se"); "an"→06/94 uniform (no data). 1,597/11,870 lexicon words contain
a polyvalent syllable; only **52 are structurally at-risk** (distortion
possible); 8 distinct mechanisms, fully enumerated (§4).

Islet inventories spot-checked against the pair stream rebuilt from
`data/upstream-ct_R5005.txt` + `upstream-offsets.json` (1,846 pairs):
06=46 ✓, 94→82=4 @[578,1181,1352,1741] ✓, 94→52=3 ✓, 94→59=2 ✓,
94-82-06=3 ✓, 52 @160 ✓, 06→77=6/06→29=5/06→11=4 ✓.

## 2. Forward test — pattern survival (recall)

Exact P(cipher pattern == lexicon phon pattern), q=0.5 reference:

| population | n | q=0.1 | q=0.3 | q=0.5 | q=0.9 |
|---|---|---|---|---|---|
| all w/ poly syll | 1597 | 1.000 | 0.998 | **0.995** | 0.984 |
| at-risk (52) | 52 | 0.987 | 0.931 | **0.834** | 0.517 |
| repetition ∩ poly (18) | 18 | 0.979 | 0.949 | **0.931** | 0.937 |
| repetition ∩ at-risk (2) | 2 | 0.815 | 0.537 | **0.380** | 0.431 |
| islet 06-words | 893 | 1.000 | 0.997 | 0.993 | 0.979 |
| islet 94-words | 610 | 1.000 | 0.997 | 0.992 | 0.973 |
| islet 52-words | 533 | 0.999 | 0.997 | 0.994 | 0.986 |

Frequency-weighted overall: 0.998 at q=0.5. Orthographic patterns agree
(overall 0.995; orth repetition-words 1.000 — "sé"/"se" distinct in orth,
so no split risk). Control: 200 non-polyvalent words, survival exactly
1.000 at all q, both sampling seeds. MC cross-check (40 at-risk words,
20k trials): max |exact − MC| = 0.0037, seeds 7 and 99 agree.

Reading: the **naive matcher loses <1% recall** to the known islets.
Damage concentrates in 52 identifiable words (worst: the se→52/59 split
on "sérieuse"/"sérieusement", survival 0.38 at q=0.5).

## 3. Reverse test — candidate inflation (precision)

For each cipher pattern P, two expansion strategies to recover recall:

**(a) DUMB pattern-expansion** (union over the whole closure pattern
class): CATASTROPHIC. 3|ABA: 23 → 4,659 (**202x**); 3|AAB: 2 → 4,636
(**2318x**); 2|AA: 4 → 3,222 (805x); 3|ABB: 8 → 4,644 (580x).
**The matcher must never do this** — the pattern stops pruning entirely.

**(b) SMART expansion** (naive ∪ {words that can *actually* produce P},
via exact reachable-sets): MANAGEABLE. Max **6.0x** (3|AAB: 2→12, new:
ennemi/ennemis/néanmoins/passeports…); 5|ABCDA 4.3x; 3|ABA 1.13x
(23→26); all others ≤2x. Non-repetition patterns: inflation ≈1.00x.

## 4. Per-islet distortion enumeration (52 at-risk words)

- **06-merge an/mant** (13): entièrement ABCDE→ABCDA, annuellement,
  encouragement… (surv 0.88 @q=.5)
- **06-merge man/mant** (4): momentanément, commencement, amendement,
  commandement ABCD→ABCB (0.75)
- **06-merge an/man** (1): ensemencer ABCD→ABAC; **an/ant** (2):
  envisageant, envoient (0.88)
- **94-merge an/n** (22): ennemi/ennemis/ennemie ABC→AAB,
  ancienne/endorment ABC→ABA, païenne ABCD→ABCC… (0.88)
- **52-merge pas/s** (11): passe/passé AB→AA, dépassé/surpasse ABC→ABB,
  outrepassé ABCD→ABCC… (0.85)
- **52/59-split s/s** (2): sérieuse ABA→ABC, sérieusement ABAC→ABCD
  (**0.38** — the worst case)

## 5. Restrictions (the gate conditions)

1. **Use the polyvalence-expanded index, not the naive one.** File every
   lexicon word under ALL its reachable cipher patterns (exact sets in
   `results.json`; rebuild with `polyvalence_test.py`). One lookup,
   100% recall on known islets, precision cost ≤6x. (Acceptable
   alternative: naive lookup + swallow ~0.5% recall loss — but NOT on
   se-split repetition words.)
2. **Never naive pattern-expansion** (§3a: 202x–2318x inflation kills
   the instrument).
3. **Candidate generation only from repetition-bearing patterns**
   (111 words / 26 keys). Non-repetition lookups return thousands with
   or without polyvalence — use anchors/bigrams there, not patterns.
4. **Group-level consistency beats pattern-level**: when the cipher
   word contains 06/94/52/59, filter candidates to words whose
   polyvalent syllables align with those groups (§3b is the upper bound).
5. **Flag the 52 at-risk words** (§4 list): any matcher hit on one needs
   an independent check (anchor/bigram/grammar).
6. **Re-run on model change**: if 06=verb-stem (provisional F21/F25) is
   confirmed systematic, or new polyvalent groups are found, the
   reachable-sets must be rebuilt. Current model: 06/94/52/59 only.
7. **Segmentation is the larger, separate threat** (F30): (n, pattern)
   lookup assumes the segmenter's n/cuts match the lexicon's canonical
   cut; the Frenchman's inconsistent-cutting evidence breaks this
   independently of polyvalence. The matcher must tolerate n-mismatch.

## 6. Synthetic "more of the same" breakdown

Added K synthetic islets (one group covering 2 rhyme-sharing syllables,
the phonetic-merging shape of the known islets), q=0.5, 3 seeds:

| K | overall survival | repetition survival | max smart inflation |
|---|---|---|---|
| 0 | 0.995 | 0.931 | 6.0x |
| 3 | 0.995 | 0.914 | 6.0x |
| 10 | 0.994 | 0.891 | 6.0x |
| 30 | 0.994 | 0.879 | 6.0x |

Graceful degradation: even +30 islets (10x the known count) cost only
~5 points of repetition-word recall. Polyvalence is a scalpel — it only
bites where specific syllables co-occur in interacting positions.

## 7. Caveats

- q unidentified (swept); "an"→06/94 split assumed uniform; se→52/59
  0.6/0.4 rests on n=5.
- Per-position independence assumed; a fully deterministic encipherer
  makes merge distortions certain (not probabilistic) on the 52 at-risk
  words — same word list, worse rates.
- Unknown systematic polyvalence (06 verb-stem class; unidentified
  groups) is the residual risk — §5.6 covers it.
- The instrument is a candidate *generator*; every candidate still needs
  anchor/bigram/grammar confirmation. Nothing here promotes a reading.

## 8. Relation to the pattern-matcher's HONEST NULL (sibling worker)

The pattern-matcher sibling ran the instrument against the 25 segmenter
targets and returned NULL, stamped PROVISIONAL-PENDING-POLYVALENCE-VERDICT
(`report_inbox/pattern-matcher-proposals.md`). Their null is driven by an
ORTHOGONAL failure: the lexicon's syllable inventory doesn't contain the
cipher's by-ear units (standalone m/i letters; "première" tail 82-34-29-40
returns zero candidates — a 4-ground-truth-anchor word the instrument
cannot recover). That is a unit-inventory mismatch (fix: the syllabary's
own inventory, round-4 WO5 `data/upstream-syll*.py`), not a polyvalence
failure. This gate verdict covers the polyvalence dimension only:
polyvalence does not break pattern matching (with §5 restrictions), but
the inventory mismatch remains the binding constraint — the expanded
index is only useful once the matcher operates in the cipher's own unit
alphabet. The two verdicts compose: fix inventory first, then apply §5.
