# Battery report: bound-40-boundary-resolve — resolve 40='e' bound/free status stream-wide

Worker: subagent e1af5d16-2e64-43a7-87d8-4b51cc4640ff, 2026-10-09.
Lock: supervisor-created reservation `locks/bound-40-boundary-resolve.lock`
(2026-10-09T14:20:45Z, fresh); kept during work, deleted on completion.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed like code/side-keyhunt/repair_parse.py
(replicated inline; asserts held: 1,847 pairs, 96 types). canonical.py never
touched. R5005, sealed gate instances, and the red-team adjudication queue
never touched. All numbers trace to the stream. @-offsets 0-based.

Provenance: follow-up #2 of battery-08-62-boundary-adjudication NULL
(2026-10-09; code/crowd17/report_inbox/processed/battery-08-62-boundary-adjudication.md).
That battery fenced the 08|62 boundary at both windows partly because 08's
right side is boundary-dependent on the unresolved 40|08 question, and 40='e'
(a pencil GT cell) had no standing bound/free ruling. This target resolves it.

## Bar (verbatim, pre-registered)

"state 40's status with distributional byte evidence at battery grade; else fence"

## Bar restated as numbered clauses (fixed before testing)

- C1: state 40's bound/free status (BOUND = attaches within words; FREE =
  standalone word) with distributional byte evidence at battery grade, on
  standing-licensed grounds.
- C2 (else): fence with stated cause.

Adverses: none listed.

Standing premises adopted (§7; battery premises, never re-litigated):
29='er' and 34='i' are banked pencil-GT bound letters (must sit inside a
word); 11=la, 64=qui, 96=par, 17=fois, 47=ce, 79="tout", 00="pour", 84="on",
67=et/veut, 87=ce are free words forcing a boundary on any adjacent side;
08 is letter-tier, value OPEN. No standing ruling on 40's bound/free status
prior to this report.

## Method

Re-derived the repaired stream in-session byte-exact per repair_parse.py.
Full 21-window census of 40 (±1 context, boundary status per standing rules
only). Tested the FREE reading for forced contradictions: FREE-40 forces a
boundary on both sides of 40 at every window; where a bound letter 29 stands
immediately before 40 behind a forced boundary, FREE strands 29 as a
standalone word — impossible for a banked bound letter. Tested the BOUND
reading for compatibility across all 21 windows. Checked both crib loci and
the '40 08' bigram census against the parent report's figures.

## Window-level evidence (@-offsets, 0-based, repaired stream)

n(40) = 21. Predecessor distribution: 29 x9, 78 x3, rest x1 (88, 97, 96,
74, 50, 03, 48, 61, 56). Follower distribution: 65 x3, 67 x3, 08 x2, 17 x2,
03 x2, rest x1 (12, 97, 92, 56, 20, 95, 62, 29, 06).

Full census (b = boundary status per standing rules only):

| @ | row | pre [40] fol | left | right |
|---|---|---|---|---|
| 63 | a1_01 | 29 [40] 12 | NO (pre bound) | undet |
| 292 | a2_03 | 29 [40] 65 | NO (pre bound) | undet |
| 298 | a2_04 | 78 [40] 97 | undet | undet |
| 335 | a2_05 | 88 [40] 03 | undet | undet |
| 353 | a2_06 | 78 [40] 92 | undet | undet |
| 501 | a2_11 | 29 [40] 56 | NO (pre bound) | undet |
| 598 | a4_00 | 29 [40] 03 | NO (pre bound) | undet |
| 686 | a5_00 | 29 [40] 65 | NO (pre bound) | undet |
| 752 | a5_03 | 97 [40] 67 | undet | FORCED (fol free) |
| 759 | a5_03 | 29 [40] 20 | NO (pre bound) | undet |
| 820 | a5_05 | 78 [40] 95 | undet | undet |
| 848 | a5_06 | 96 [40] 62 | FORCED (pre free) | undet |
| 921 | a5_09 | 74 [40] 08 | undet | undet |
| 943 | a5_10 | 50 [40] 08 | undet | undet |
| 1039 | a6_03 | 29 [40] 17 | NO (pre bound) | FORCED (fol free) |
| 1051 | a6_04 | 29 [40] 29 | NO (pre bound) | NO (fol bound) |
| 1238 | a7_01 | 03 [40] 67 | undet | FORCED (fol free) |
| 1399 | a7_07 | 48 [40] 67 | undet | FORCED (fol free) |
| 1557 | a8_01 | 61 [40] 17 | undet | FORCED (fol free) |
| 1711 | a8_06 | 29 [40] 65 | undet-left? NO (pre bound) | undet |
| 1746 | a8_08 | 56 [40] 06 | undet | undet |

(@1711 left = NO: pre 29 is a bound letter.)

### Kill-grade test of FREE: three stranding windows

Under FREE-40, a boundary is forced on both sides of 40 at every window.
At these three windows the cell before 29 is a free word, forcing a
boundary between it and 29 — so 29 stands between two forced boundaries:

- @292 (a2_03), row-internal [290..293]: `64 | [29] | [40] 65`
  (64='qui' forces boundary before 29; FREE-40 forces boundary after 29)
- @501 (a2_11), row-internal [499..501]: `11 | [29] | [40] 56`
  (11='la' forces boundary before 29; FREE-40 forces boundary after 29)
- @686 (a5_00), row-internal [684..686]: `64 | [29] | [40] 65`
  (64='qui' forces boundary before 29; FREE-40 forces boundary after 29)

At each window FREE-40 makes 29='er' a standalone word. 29 is a banked
pencil-GT bound letter (§7) — a bound letter cannot constitute a word.
No escape: 29 cannot fuse leftward (forced boundary before it) and cannot
fuse rightward into 40 (that would make it internal to 40's word,
contradicting FREE-40). Each window independently kills the FREE reading
at kill grade.

### Distributional signature (BOUND-positive)

- 9/21 (43%) of 40's occurrences immediately follow the bound letter 29
  (the dominant neighbor by far: next is 78 x3).
- 0/21 windows show 40 isolated as a standalone word (never flanked by
  free words on both sides; never flanked by forced boundaries on both
  sides under any standing ground).
- 6/21 windows sit at a word edge next to a free word — all
  BOUND-compatible: word-final x5 (@752, @1039, @1238, @1399, @1557:
  "…40 | et/veut / fois") and word-initial x1 (@848: "par | 40…").
- Both crib windows (@759 a5_03, gloss line; @1039 a6_03) read
  `11 70 82 34 29 [40]` = "la pre m i er e" with 40 word-final — the
  pencil gloss itself shows 40 as a bound, word-final letter.
- @1051 (a6_04): `29 [40] 29` — 40 fully internal between two bound
  letters; BOUND-compatible (under FREE-40 this window is merely
  non-decisive, not contradictory).

### '40 08' bigram check

Exactly x2 stream-wide: 08 at @922 (a5_09; 40 at @921) and 08 at @944
(a5_10; 40 at @943). Matches the parent report's figures. Note: the
queue brief's "@922/@944" are the 08 positions; the 40 positions are
@921/@943.

## Per-clause pass/fail

- C1: PASS at battery grade. 40='e' is a BOUND letter (attaches within
  words; never a standalone word). FREE is rejected at kill grade by
  three independent stranding windows (@292, @501, @686), each forcing
  the banked bound letter 29='er' into a standalone word under the FREE
  reading. The positive distributional signature (9/21 post-bound-29,
  0/21 standalone, 6/21 word-edge placements all bound-compatible, crib
  word-final) corroborates BOUND. Grounds are standing-licensed only:
  banked 29=er bound (§7), the free-word forced-boundary rule, and
  byte-exact stream positions.
- C2: not reached.

Consequence for the parent question (stated, not re-decided): the claim's
mechanism — "a forced 40|08 boundary makes 08 word-initial at @944 (and
@922)" — is dead. With 40 bound and 08 letter-tier, no standing rule
forces a boundary at 40|08 (@921|@922, @943|@944). The 40|08 boundary
itself remains undetermined on standing grounds (nothing forces it,
nothing forbids it); this ruling removes only the forcing route. The
parent's fence on 08|62 is untouched — no standing or red-team verdict
contradicted or downgraded; §7 intact; canonical-stream caveat stands
(rows a5_09/a5_10/a2_03/a2_11/a5_00 unvalidated).

## Verdict

**promote** — 40='e' is a BOUND letter at battery grade (kill-grade
rejection of FREE + corroborating distributional signature). Adverses:
none listed. No follow-ups required (promote, not null).

## Bookkeeping

- Lock `locks/bound-40-boundary-resolve.lock` (supervisor reservation,
  fresh at 2026-10-09T14:20:45Z) kept during work, deleted on completion
  (verified below).
- Queue: `bound-40-boundary-resolve` -> `status: verdict`,
  `result: promote`, `2026-10-09` (pre-write assert: was
  `queued`/verdictless; temp-file + rename; JSON re-validated from disk;
  own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
