# Battery `word89e-right-bound` — verdict: PROMOTE (48 word-final confirmed at all three windows)

**Target:** mirror test of `inf89-letter-interior` (NULL, 2026-10-09): the
"[89]e" right boundary — is 48 word-final, or does the word extend past 48
("e[20]"-shaped)?

## Bar (verbatim, pre-registered)

> "test the '[89]e' right boundary at @640/@871/@986: confirm 48 word-final
> vs word-extending ('e[20]'-shaped)."

Restated as numbered pass/fail clauses (verbatim decomposition, committed
before verdict; no clause added, dropped, or reworded after numbers were seen):

- **C1** — at @640 (window "67 77 89 48 20"), 48 is word-final: "[89]e" does
  NOT extend past 48 into 20.
- **C2** — at @871 (window "87 77 89 48 20"), same as C1.
- **C3** — at @986 (window "01 24 89 48 01"), 48 is word-final: "[89]e" does
  NOT extend past 48 into 01.

Adverses: none listed.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
96 types). `canonical.py` never used. R5005 untouched. Adopted standing
premises (§7): 48='e' word-final of "[89]e" (battery-grade locus @641,
`conj-20-642-subordinator` NULL: "…77(le) 89 48(e) 20…"); 20's class at @642
is post-nominal adjective; 67 et/veut is the sole true polyvalence; 89 has
no polyvalence declaration.

## Window-level evidence (@-offsets, byte-exact, row-validated)

| @ | row | context (pre2 pre1 89 48 post1) |
|---|-----|---------------------------------|
| 640 | a4_01 | 67 77 **89 48** 20 |
| 871 | a5_07 | 87 77 **89 48** 20 |
| 986 | a6_01 | 01 24 **89 48** 01 |

- "89 48" bigram: exactly **3×** stream-wide (no more, no fewer).
- "48 20" bigram: exactly **2×** stream-wide — @641 and @872, i.e. only in
  the two "[89]e" windows. No other word's final-48 ever precedes 20.
- **20 distribution: 15 windows, 13 distinct predecessors**
  (61, 88, 41, 48, 00, 98, 36, 40, 04, 86, 09, 30 — some ×2). 20 is a free
  word stream-wide, not a bound morpheme of "[89]e".
- **Direct parallel at @759–760 (row a5_03): "70 82 34 29 40 20 62".**
  Banked pencil gloss (§7): 70=pre, 82=m, 34=i, 29=er, 40=e ⇒ "première".
  Here 40 is a banked word-final 'e' followed by 20 as a separate word.
  The "48(e) 20" sequence at @641/@872 reads the identical way:
  word-final-e + 20 as two words. No fusion license needed, and none exists.
- **20's class at @642 is post-nominal adjective** (`conj-20-642` finding).
  A post-nominal adjective is a free-word position by definition; making 20
  word-interior to an "e[20]"-fused form would invert that class with no
  granting frame.
- The one conceivable counter-read — "20 is bound *only* in the 89-context,
  free elsewhere" — would make 20 polyvalent (bound suffix vs free word).
  §7 stands: 67 et/veut is the sole true polyvalence; 20 has no polyvalence
  declaration. The counter-read is fenced with stated cause, not ignored.
- **@986 successor 01: 28 windows, 21 distinct predecessors, 20 distinct
  successors** — a free word by any distributional bar. "…89 48(e) 01…"
  is final-e + free word; no extending license exists.
- No row straddling at any of the three windows (48 and its successor sit
  in the same row each time).

## Per-clause results

- **C1 — PASS.** @640: 48 word-final. 20 is a free word (15 windows / 13
  predecessors); the "première" parallel at @759–760 shows word-final-e + 20
  as two words; 20's post-nominal-adjective class at @642 forbids
  word-interior placement; the bound-only-in-89-context counter-read is
  §7-barred (67 sole polyvalence).
- **C2 — PASS.** @871: identical structure to C1 (same "77 89 48 20"
  sequence, same 20, same class and distribution evidence).
- **C3 — PASS.** @986: 48 word-final. Successor 01 is a free word
  (28 windows / 21 pre / 20 post); no word-extending frame exists for
  "[89]e01".

## Verdict rationale

All three bar clauses pass and every listed adverse (none) is answered; the
one natural counter-read is fenced with stated cause. 48's word-finality at
the "[89]e" right boundary is confirmed from the right side, hardening the
48-interior kill arm of `inf89-letter-interior` exactly as designed. §7
intact; no standing or red-team verdict contradicted or downgraded;
canonical-stream caveat stands.

**Verdict: promote.**

## Follow-ups

None — a promote verdict regenerates no work. (The sibling follow-up
`inf89-er89-boundary`, already queued from the parent report, sharpens the
left boundary independently.)

## Bookkeeping

- Stream: repaired 1,847-pair parse, asserts held; `canonical.py` never used.
- Lock: created on start (2026-10-09T13:30:06Z), deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
