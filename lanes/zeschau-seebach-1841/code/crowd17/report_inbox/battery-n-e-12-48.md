# Battery report: n-e-12-48 — 12="n" + 48="e" (letters)

- Target: `n-e-12-48`, priority 1
- Date: 2026-10-07
- Worker: session-911ceab9 (clean restart). Predecessor lock
  (`n-e-12-48-worker-1c7e9c9c`, 2026-10-08T04:22:22Z) found stale: the prior
  worker died on a daemon restart at ~04:26 UTC with no report on disk.
  Per protocol §6 the lock was refreshed and the target re-run from scratch.

## Bar (verbatim from battery-queue.json)

> promote iff each value has >=2 GT-anchored frames + zero contradictions

Restated as numbered pass/fail clauses (frozen before testing):

1. **C1:** Value 12 has >=2 GT-anchored frames consistent with 12="n"
   (frame = immediate adjacency to a pencil-GT value whose known reading +
   "n" forms a standard French word/cluster).
2. **C2:** Value 48 has >=2 GT-anchored frames consistent with 48="e"
   (same definition, known reading + "e" or "e" + known reading).
3. **C3:** Zero contradictions: no window forces a different letter at a
   12/48 slot at kill grade; no granted red-team frame spanning a 12/48
   position conflicts with the claim; the listed adverse (48='ne'/'de'/'est'
   kills) is answered, not ignored.

"GT-anchored" = anchored on pencil banked GT (11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que). Promoted-anchored frames are reported as corroboration
only, not counted toward C1/C2.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed byte-identically to
`code/side-keyhunt/repair_parse.py` (assert 1847 pairs, crib at the two
"la premiere" positions, a8_05 ends 46). `canonical.py` not used. R5005 not
touched. Offsets below are pair indices (@N) with row ids.

## Evidence claims re-parsed (from the queue's evidence field)

- 'me' = 82-48 x4: CONFIRMED 4 — @126, @377, @398, @1229.
- 'en' = 40-12 @64: CONFIRMED — 40 at @63, 12 at @64 (row a1_01).
- 'ni' = 12-34: CONFIRMED 1 — @1740 (row a8_07).
- 'ne' = 12-48 x7: CORRECTED — **x5**, not x7, in both the repaired and the
  obsolete parse: @169, @709, @809, @1075, @1736. (Finder overcount; noted,
  does not affect the bar.)

## C1 — 12="n" frames (23 occurrences of 12 in stream)

| Frame | Reading | @-offsets | Anchor tier |
|---|---|---|---|
| 40-12 | "en" | @63 (12 @64) | pencil 40=e |
| 12-34 | "ni" | @1740 | pencil 34=i |
| 70-12 | "pren" | @347, @1118, @1547 | pencil 70=pre |

3 distinct pencil-anchored frame types, 5 anchored occurrences. **C1 PASS.**

Consistency cross-checks (94 is under separate concurrent test, so not
counted as anchors): 12-94 "nne" windows @64, @348, @1548 read as
40-12-94 "enne" (@64) and 70-12-94 "prenne" (@348, @1548) — full French
word under 12="n" + 94="ne". Consistent with the analytic/syllabic duality,
no contradiction either way.

## C2 — 48="e" frames (38 occurrences of 48 in stream)

| Frame | Reading | @-offsets | Anchor tier |
|---|---|---|---|
| 82-48 | "me" | @126, @377, @398, @1229 | pencil 82=m |
| 29-48 | "ere" | @541 | pencil 29=er |

2 distinct pencil-anchored frame types, 5 anchored occurrences. **C2 PASS.**

Promoted-anchored corroboration (not counted): 96-48 "pare" @928
(96=par promoted). Neutral (non-supporting, non-contradicting) windows:
48-29 "eer" @1229/@1589, 48-40 "ee" @1398, 48-82 "em" @928, 48-47 "ece"
@863/@1658, 48-96 "epar" @1212, 48-77 "ele" @1076/@1350 (77=le provisional),
48-00 "epour" @377/@729 (00="pour" promoted). These are analytic letter
sequences with no granted spelling constraining the neighbor slot — neutral.

## C3 — contradiction scan

- Granted frames spanning a 12/48 slot: A7-L2 "tout me [48-verb]" at
  @396–399 (79 82 48 06 11) and @1227–1230 (79 82 48 29 47). Under 48="e"
  both read "tout me e-[verb]" — verb-initial e; the frame's value was open,
  no conflict. No other granted frame (A1 37/32/42, A8 80/89, A3 85,
  A12 37-01) spans a 12 or 48 position. **No forced alternative.**
- Crib "la premiere" (11-70-82-34-29-40 x2): no 12/48 involved.
- Registry: 12 and 48 are ABSENT from table-registry.json — no standing
  assignment to contradict, no red-team verdict overwritten.
- No window yields a pencil-anchored reading that forces a letter other than
  the claim at the 12/48 slot.

**C3 PASS — zero contradictions.**

## Adverses disposition

1. *"48='ne'/'de'/'est' all KILLED — this is the letter reading, distinct"*
   — ANSWERED. The standing kills concern 48 as a whole-word/syllable value.
   The letter-tier claim 48="e" is a different analytic tier and is in fact
   *consistent* with those kills: word-readings of 48 failed because 48 is a
   letter, not a word. Kills hold; nothing in this battery disturbs them.
2. *{48,94} homophone-set kill* — ANSWERED/FENCED. 48="e" and 94="ne" are
   not claimed as homophones; the duality is analytic spelling (12-48) vs
   syllabic single-group spelling (94) of plaintext "ne" — the homophonic
   cipher's ordinary mechanism. Cross-checked: 70-12-94 "prenne" x2 and
   40-12-94 "enne" x1 read cleanly under both concurrent batteries
   (n-e-12-48 and ne-94). No contradiction found; the duality relationship is
   flagged for red-team adjudication — not unilaterally resolved here.
3. *Evidence overcount* — fenced: 'ne'=12-48 is x5 in-stream, not x7
   (re-parsed in both 1847 and 1846 parses). Corrected above.

## Verdict

**promote** — C1 PASS (3 frame types / 5 occurrences), C2 PASS (2 frame
types / 5 occurrences), C3 PASS (zero contradictions), all adverses answered
or fenced. Promotion is a battery-verdict record only; ratification is the
red team's (never done by this worker). Follow-ups, if red team wants finer
discrimination: 12-94 "prenne/enne" duality frames; 29-48 "ere" is a single
occurrence — a second "ere"-class pencil frame would harden C2.
