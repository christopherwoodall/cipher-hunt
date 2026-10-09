# Battery verdict: seg-81-30-offset1

- Target id: `seg-81-30-offset1`
- Claim: "An offset-1 reparse of row a1_01 dissolves the fenced @44-45 ('81 30') junction."
- Date: 2026-10-09
- Worker: battery worker (subagent 8f225e99-388f-4acc-bf65-8d816ab63480)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs,
  96 types. `canonical.py` never used. R5005, sealed gates, red-team
  adjudication queue untouched. All @-offsets are 0-based global.

Terms (ASD-STE100): "junction" = the pair adjacency at one stream position.
"off0" = the repaired offset-0 parse (canonical). "off1" = the rival
offset-1 reparse (digit pairs start one digit later). "dissolve" = the
"81 30" adjacency no longer exists in the reparse, so there is nothing to
segment.

## Bar (verbatim, pre-registered before testing)

"re-derive the @44-45 junction under the rival phase (battery 04:52:59:
offset-1 reparse constraint-clean, dissolves 'la tout'); if the junction
dissolves, close this line with byte evidence; if it survives, re-test
C1/C2 under the rival phase."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (re-derive):** re-derive the @44-45 junction byte-exact under the
   offset-1 phase — same raw digit span, re-paired, with the resulting pair
   sequence stated.
2. **C2 (dissolution test):** the "81 30" adjacency survives the reparse
   (relocation) or it does not. If it dissolves — no "81" and no "30" at the
   junction span, and no "81 30" adjacency anywhere in the off1 row — the
   line closes with byte evidence. If it survives, re-test the parent fence's
   C1/C2 (word-medial "[81]pas" / word boundary "[81] pas") under the rival
   phase.

Adverse: the offset-1 phase is itself contested (rival-phase, red-team
territory). This battery tests the junction only and does NOT adjudicate
whether offset-1 is the true phase of row a1_01.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/seg-81-30-offset1.lock` on start
   (agent id + UTC timestamp); deleted on completion. No stale lock was
   present.
2. Re-derived the repaired stream in-session from
   `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
   (parse per `repair_parse.py`). Asserts: 1,847 pairs, 96 types.
3. Extracted row a1_01's raw digits and built both full-row pair parses:
   off0 = [d[i:i+2] for i in range(0, 70, 2)], off1 = [d[i:i+2] for i in
   range(1, 70, 2)].
4. Compared the junction digit span under both phases. Standing premises
   adopted, not re-litigated: the parent fence battery
   `seg-81-30-boundary` (NULL, junction fenced: C1 word-medial FAIL,
   C2 word-boundary FAIL, blockers 43's class / 62's value / 88's
   finiteness); `seg-a1_01-constraint-sweep` (PROMOTE: offset-1 is
   constraint-clean across all 35 pairs; phase adoption is red-team venue).

## Window-level evidence (byte-exact, re-derived in-session)

Row a1_01 raw digits (71 digits):
`08913964410124884381306296009279371179855835531241083429401294926913246`
Repaired offset: 0. Global stream start: 0-based @35.

Off0 (35 pairs, canonical):
`08 91 39 64 41 01 24 88 43 81 30 62 96 00 92 79 37 11 79 85 58 35 53 12 41 08 34 29 40 12 94 92 69 13 24`

- The junction: in-row pair idx 9 = '81', idx 10 = '30' = global @44, @45.
  The digit span is d[18:22] = `8130`. "81 30" is byte-exact on the
  canonical parse.

Off1 (35 pairs, rival phase):
`89 13 96 44 10 12 48 84 38 13 06 29 60 09 27 93 71 17 98 55 83 55 31 24 10 83 42 94 01 29 49 26 91 32 46`

- The same digit span d[18:22] = `8130` re-pairs as in-row idx 9 = '13',
  idx 10 = '06'. So the @44-45 junction region becomes "13 06", not "81 30".
- Neither '81' nor '30' occurs anywhere in the 35 off1 pairs.
- No "81 30" adjacency occurs anywhere in the off1 row. The junction does
  not relocate — it disappears.
- The fence's C1 ("[81]pas" word-medial) and C2 ("[81] pas" word boundary)
  are both about segmenting the "81 30" adjacency. With no "81" and no "30"
  present, neither clause has a subject: the fenced question is vacuous
  under off1. There is nothing to re-test.

## Per-clause results

- **C1 — PASS.** The junction digit span (d[18:22] = `8130`, canonical
  @44-45 = "81 30") re-derives under offset-1 as "13 06" (in-row idx 9,10).
  Byte-exact on the repaired stream's raw digits.
- **C2 — PASS (dissolution arm).** "81" and "30" are both absent from the
  entire off1 row (35/35 pairs checked); the "81 30" adjacency survives
  nowhere. The junction dissolves under the rival phase. The line closes
  with byte evidence. The re-test arm does not fire.

## Adverses answered

- **Phase contested:** answered by scoping, not ignored. This battery does
  not adopt offset-1 and does not decide row a1_01's true phase — that
  decision is red-team venue (per `seg-a1_01-constraint-sweep`). The finding
  is conditional and stated as such: *under* the offset-1 phase, the
  junction dissolves.
- **Trepas-kill tension:** recorded, not re-litigated. The
  `seg-81-30-trepas-kill` battery noted that offset-1 "would resurrect the
  1,846-pair parse that red team killed for violating gloss (i)". That is a
  constraint on phase adoption, not on this battery's conditional
  dissolution finding. No standing verdict is contradicted: the junction's
  fence on the canonical (offset-0) stream stands untouched, and the
  trepas kill (81='tre' dead as a value) is phase-independent of this test.

## Verdict: PROMOTE

The claim is verified at battery grade: under the offset-1 reparse of row
a1_01, the fenced @44-45 ("81 30") junction dissolves — the digit span
re-pairs as "13 06", and neither "81" nor "30" survives anywhere in the
reparsed row, so the parent fence's C1/C2 have no subject under the rival
phase. Per §4 (promote), no follow-ups are required.

## Scope

Promotes only the dissolution finding, conditioned on the offset-1 phase.
Untouched: the junction's fence on the canonical offset-0 stream (still
fenced under standing values); 81's value (open); 30='pas' (standing);
43's class, 62's value, 88's finiteness (the parent fence's blockers);
row a1_01's phase decision (red-team venue). No standing or red-team
verdict contradicted or downgraded. §7 intact. Canonical-stream caveat
stands (row a1_01 offset unvalidated upstream).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-81-30-offset1.md` (this file)
- Queue: `seg-81-30-offset1` → status `verdict`, result `promote`,
  2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file
  + rename; JSON re-validated from disk; own entry only; no downgrade)
- Lock `locks/seg-81-30-offset1.lock` created on start, deleted on
  completion (verified gone). R5005, sealed gates, red-team adjudication
  queue untouched.
