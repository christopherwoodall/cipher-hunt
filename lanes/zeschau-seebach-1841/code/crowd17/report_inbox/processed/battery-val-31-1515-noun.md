# Battery report: val-31-1515-noun

- Target id: `val-31-1515-noun`
- Claim: "name 31's class at @1515"
- Date: 2026-10-09
- Worker: battery worker (subagent 8ff3dff8-88d0-472b-a9e4-b07b10dcc31a)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: all @-offsets are 0-based repaired-stream pair indices (queue convention). The 'la [31]' bigram is @1515–1516 (0-based); the bar's "@1514" names the "88 11" locus of the parent battery, and its "@1515" names the bigram's start. Substance unaffected.

Terms (ASD-STE100): "battery grade" = the evidence standard of this pipeline. "Kill grade" = a window or distributional test forces the claim false at the lane's standard.

## Bar (verbatim, pre-registered before testing)

"noun-31 makes 'la [31]' a battery-grade [art+noun] object at @1514; non-noun kills the object reading there"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (noun arm):** 31 is nominal at the @1515–1516 locus → 'la [31]' parses as a battery-grade [art+noun] object of governor-88 at @1514 → the noun-31 hypothesis stands.
2. **C2 (non-noun arm):** 31 is non-noun at the locus → the [art+noun] object reading at @1514 is killed at kill grade.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-31-1515-noun.lock` on start (agent id + 2026-10-09T19:10:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Ran a window-complete census of all 31 occurrences (n(31)=8, see below).
4. Adopted, never re-litigated: 11='la' pencil GT (§7); 31=["VERBAL","cls"] registry class-level; val-08-successor-class PROMOTE (2026-10-09): 31 = SPLIT (finite VERB / word-internal SYLLABLE) at battery grade — 3 verb legs ("qui [31]" @338/@1647, "[31]er" stem @1257), 3 syllable legs ("t[31]" @882/@1489/@1521); val-31-1257-word NULL (2026-10-09): the noun arm for 31 fenced — "a noun value for 31 would collide with its battery-grade finite-verb legs (@338, @1647): verb/noun polyvalence, red-team venue"; 88=["gov","cls"] (governor class); parent inf88-object-census NULL (2026-10-09): "88 11" x2 @730/@1514, 88's finiteness open at @1514.

## Window-level evidence

### The test locus @1514–1517 (row a7_11), byte-exact

`... 61 59 39 81 | 88 11 31 11 | 91 67 08 31 24 ...`
- @1514=88 (governor class), @1515=11='la' (pencil GT), @1516=31, @1517=11='la', @1518=91.
- The candidate object NP is "11 31" = "la [31]" at @1515–1516, governed (if at all) by 88 at @1514.

### Complete 31 census (n=31)=8, all byte-exact

| @ | row | context (`pre |31| post`) | established arm |
|---|---|---|---|
| 338 | a2_05 | `40 03 64 \|31\| 14 45 64` | finite VERB ("qui [31]", battery grade) |
| 882 | a5_08 | `78 17 08 \|31\| 79 68 37` | SYLLABLE ("t[31]", battery grade) |
| 1257 | a7_02 | `46 01 61 \|31\| 29 69 88` | VERB stem ("[31]er", battery grade); noun arm FENCED (val-31-1257-word NULL) |
| 1489 | a7_10 | `24 87 08 \|31\| 92 39 24` | SYLLABLE ("t[31]", battery grade) |
| 1516 | a7_11 | `81 88 11 \|31\| 11 91 67` | **test locus** — no independent arm |
| 1521 | a7_11 | `91 67 08 \|31\| 24 11 11` | SYLLABLE ("t[31]", battery grade) |
| 1615 | a8_03 | `83 71 48 \|31\| 76 42 44` | non-nominal (48='e' letter tier left; no determiner governs 31; no nominal frame) |
| 1647 | a8_04 | `60 03 64 \|31\| 10 03 38` | finite VERB ("qui [31]", battery grade) |

Nominal-leg count for 31 across all 8 windows: **zero**. No window shows 31 determiner-governed, as a verb subject, or in any other nominal frame.

### Why the noun arm cannot reach battery grade

1. **Six non-nominal legs vs zero nominal legs.** 31's class is battery-PROMOTEd as verb/syllable split (3 verb + 3 syllable legs). The remaining two windows (@1257 verb-stem, @1615 non-nominal) add no nominal support.
2. **Precedent fence.** val-31-1257-word NULL (2026-10-09) already fenced the noun arm for 31 on exactly these grounds: a noun value collides with the battery-grade finite-verb legs (@338, @1647) → verb/noun polyvalence → §7 red-team venue. A nominal 31 at @1516 would be a third class arm needing the same red-team declaration. Battery cannot license it.
3. **No locus-level rescue.** At @1516, the syllable arm has no leg (the "t[31]" legs all need letter-08 left; here left is word-level 11='la'), and no "11 31" wordhood license exists in standing record. The trailing @1517=11 ('la') is additionally hostile to a bare [art+noun] object NP ("la [31-noun] la" with no intervening verb), though @1517 may open a new clause — recorded as hostile, not as the kill basis.

## Per-clause pass/fail

- **C1 (noun arm): FAIL.** Zero nominal legs for 31 in 8 windows; the noun arm was already fenced at @1257 on verb/noun-polyvalence (§7) grounds; no battery-grade path to a nominal 31 at @1515–1516 exists. 'la [31]' cannot be a battery-grade [art+noun] object.
- **C2 (non-noun arm): FIRES.** 31 is non-noun at battery grade (3 verb legs + 3 syllable legs, zero nominal legs; §7 bars the third arm). Per the bar, the [art+noun] object reading at @1514 is killed at kill grade.

## Verdict: KILL

The noun-31 hypothesis at the @1515–1516 locus is killed at kill grade: "88 11 31" at @1514 cannot be [governor] + [art+noun] object. 31 at @1516 is non-noun (verb/syllable per the standing split promote).

## Scope (stated, not hidden)

- Kills only the [art+noun] object reading of "88 11 31" at @1514. 31's class globally is untouched (verb/syllable split stands; registry ["VERBAL","cls"] stands).
- The object-pronoun rival ("[88] la" = verb + feminine clitic, parent battery) is NOT adjudicated here — it is owned by the queued target `objpron-88-77-11`; recorded, not ignored.
- 88's finiteness at @1514 stays open (adopted from parent). No standing/red-team verdict contradicted or downgraded; §7 intact (no new polyvalence declared).
- No follow-ups required (kill, not null); the surviving open question (object-pronoun rival) is already queued.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-31-1515-noun.md` (this file).
- Queue: `val-31-1515-noun` queued → `verdict`/`kill`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-31-1515-noun.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
