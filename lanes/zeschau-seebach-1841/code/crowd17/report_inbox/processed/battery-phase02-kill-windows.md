# Battery `phase02-kill-windows` — verdict: PROMOTE

**Date:** 2026-10-09

## Bar (verbatim, pre-registered)

"If the "02 79"/"02 00" bigrams dissolve there, the kill narrows to the phase-solid @459/@887."

**Numbered clauses:**
- C1: re-derive @495 (a2_11) under offset-1; the "02 79" bigram dissolves at that locus.
- C2: re-derive @1152 (a6_08) under offset-1; the "02 00" bigram dissolves at that locus.
- C3: the kill therefore narrows to the phase-solid @459/@887 (conditional consequence of C1+C2).

Adverses: none.

## Method

Parsed `data/upstream-ct_R5005.txt` row-by-row against `code/side-keyhunt/repaired_offsets.json`,
byte-exact tokenization `[s[i:i+2] for i in range(o, len(s)-1, 2)]` (the same rule as
`code/side-keyhunt/repair_parse.py`). Re-derived stream: 1,847 pairs / 96 types, asserts held
(canonical @495/@1152 loci byte-confirmed before flipping). `canonical.py` never used.
Offset-1 = flip the row's phase (0→1) and re-pair that row only. For @1152 the "02 00"
bigram crosses the a6_08|a6_09 row join, so both the a6_08-only flip and the joint
a6_08+a6_09 flip were tested.

## Canonical (offset-0) census of the two bigram families

- "02 79" x2 stream-wide: @459 (row a2_10, row-internal; ctx `66 14 02 79 87`) and
  @495 (row a2_11, row-internal; ctx `42 94 02 79 88`).
- "02 00" x2 stream-wide: @887 (row a5_08, row-internal; ctx `37 03 02 00 86`) and
  @1152 (row join a6_08|a6_09; ctx `66 84 02 00 92`).

## Findings

**@495 (a2_11) under offset-1 — C1 PASS (dissolves).**
Canonical `...42 94 02 79 88...`. Re-paired row (51 digits, 25 pairs both phases):
the re-pairing absorbs the `79` span entirely — no "79" cell occurs anywhere on the
off1 a2_11 row, and no "02 79" adjacency exists on the row. The single off1 "02"
cell (global ~501) is a different digit span (a phase-shifted artifact of the
re-pairing), not a relocated "02 79" window. The bigram dissolves at this locus.

**@1152 (a6_08) under offset-1 — C2 PASS (dissolves).**
Canonical `...66 84 02 | 00 92...` (02 is a6_08's last pair, 00 is a6_09's first).
a6_08-only flip: junction becomes `...36 68 40 00 | 92 29...` — "00" persists as
a6_09's first pair but its predecessor is now "40", and no "02" cell exists at the
junction. Joint a6_08+a6_09 flip: junction becomes `...36 68 40 09 | 22 98...` —
no "02 00" adjacency either. The bigram dissolves at this locus under both
row-join treatments.

**Phase-solid survivors — C3 FIRES.**
@459 (a2_10) and @887 (a5_08) are both row-internal bigrams on rows never flipped;
their phases are untouched by the a2_11/a6_08 re-derivations. The "02"-family kill
therefore narrows to exactly @459 ("02 79") and @887 ("02 00").

## Caveats

- Flipping a6_08 drops one pair (20→19; stream 1,847→1,846), so global @-labels
  downstream of a6_08 shift by −1 under that rival phase; the @1152 finding is
  locus-local and unaffected, but any downstream citations of the off1 parse must
  account for the shift.
- The surviving stream-wide "02 79" under the a2_11 flip is the phase-solid @459
  (a2_10) — consistent, not a relocation.
- This battery does not adopt offset-1 for any row (phase decisions remain
  red-team venue); it establishes only the conditional dissolution finding.

## Verdict

**PROMOTE** — C1 and C2 pass (both bigrams dissolve at the tested loci under
offset-1); C3, the bar's stated conditional, fires. No adverses. No standing or
red-team verdict contradicted; §7 intact; canonical-stream caveat stands.

No follow-ups required per §4 (promote).
