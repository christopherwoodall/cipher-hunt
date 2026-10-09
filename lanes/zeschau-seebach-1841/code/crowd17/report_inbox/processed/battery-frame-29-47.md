# Battery frame-29-47 — "29-47" x4 cluster: word boundary vs word-internal "erce"

Date: 2026-10-09. Worker: battery. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
re-derived in-worker; `canonical.py` never used). Offsets 1-based.

## Bar (verbatim from queue)

"resolve iff boundary real (contact profiles) with frame split tested"

Numbered clauses:
- C1: the "29 47" contact is a real word boundary ("er | ce"), established
  from 29's and 47's contact profiles.
- C2: the frame split across the four windows is tested (systematic frame vs
  singletons), and the boundary holds across the split.

Standing values used: 29="er" (ground truth), 47="ce" (A4, allophone tier,
granted), 64="qui", 82="m", 48="e", 70="pre", 46="que".

## Method

Re-derived the full stream (1,847 pairs, 96 types). Census of the "29 47"
contact, 29's follower profile (n=45), 47's predecessor profile (n=28) and
follower profile (n=28). Frame-split test on the four windows.

## Windows (1-based, ±5)

- @23: `17 64 98 82 43 | 29 47 33 | 55 81 00 34`
  ("qui vient m[43] er ce [33] ...")
- @423: `74 74 46 49 36 | 29 47 14 | 62 48 76 42`
- @1231: `57 64 79 82 48 | 29 47 33 | 29 85 56 10`
  ("qui tout m e er ce [33] ...")
- @1591: `36 70 64 65 48 | 29 47 08 | 81 03 29 80`
  ("pre qui [65] e er ce [08] ...")

"29 47" occurs exactly 4x stream-wide (the cluster is exhaustive).
"29 47 33" occurs exactly 2x, both inside the cluster; 47->33 occurs only there.

## Contact profiles

- 29's followers (n=45): 40="e" x9, 89 x5, 47 x4, 80 x4, 42 x3, 85 x3, 87 x3,
  82 x3, then singletons. Dominant contact is word-internal "ere" (29->40).
  29->47 is 8.9%, third-ranked.
- 47's predecessors (n=28): 29 x4, 76 x4, 56/58/74/48/64 x2, then singletons.
  29 is the tied-top left neighbor of 47 (14.3%).
- 47's followers at the cluster: 33 x2, 14 x1, 08 x1.

## Frame split

- Frame A (@23, @1231): identical trigram "29 47 33" with parallel left shape
  "qui ... [m][X] er ce [33]". Systematic.
- Frame B (@423): "29 47 14" singleton.
- Frame C (@1591): "29 47 08" singleton.

## Per-clause results

- C1 (boundary real via contact profiles): FAIL. The profiles do not
  independently establish a word boundary: 29's dominant life is
  word-internal ("ere" x9), and 29 being 47's tied-top predecessor is
  equally compatible with a word-internal "erce" syllable contact. Decisive
  test comes from the right context instead (see C2).
- C2 (frame split tested, boundary holds): FAIL at the systematic frame.
  Frame A reads "...er ce [33]" under the boundary model, with 33 in
  verbal/INF position. Standing battery kill ce-inf-1841 (2026-10-08):
  "'ce' + infinitive nominalization is ungrammatical in 1841 French", and
  the @23 window itself was FENCED: "ce can be neither determiner of a
  nominalized infinitive nor bare object pronoun under 33=verb".
  The boundary reading is therefore dead at @23, and by the identical
  trigram + parallel frame at @1231. Frames B and C are untestable at
  battery grade (14's and 08's values are open), so no global kill of the
  boundary is available either.

## Verdict: NULL

The boundary is not real: it is killed at the only systematic frame (2 of 4
windows) by standing verdicts, and merely possible-but-untestable at the two
singletons. Frame A ("29 47 33" x2) is fenced as non-boundary — the
"[stem]erce" word-internal reading (exercer/commerce/percer family) survives
there unrefuted, though no stem value is named at battery grade (left groups
43/36/48/48 unvalued; "meerce"-shaped strings at @1231/@1591 resist a single
stem, so the internal word is not identified either).

No standing verdict contradicted or downgraded. R5005, sealed gates, and the
red-team adjudication queue untouched.

## Follow-ups (for supervisor queuing)

1. `erce-14-singleton` (P3): test "29 47 14" @423 once 14's value resolves —
   boundary ("er | ce [14]") vs internal ("[49][36]erce").
2. `erce-08-singleton` (P3): test "29 47 08" @1591 once 08's value resolves.
3. `erce-stem-fenceA` (P3): word-internal "erce" stem test at Frame A once
   the left groups (43/36/48) resolve; kill the internal reading iff no
   French "[stem]erce" word fits.
