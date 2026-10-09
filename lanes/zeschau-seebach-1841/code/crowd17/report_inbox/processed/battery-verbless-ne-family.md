# Battery verdict: verbless-ne-family

**Target:** `verbless-ne-family` (P3)
**Date:** 2026-10-09
**Worker:** battery worker (subagent 10170d8e-975c-4766-9996-94c0a92476af)
**Claim:** "if a verb-less 'ne' family exists across 94's 37 windows, re-frame @508 inside it instead of as an isolated residual"
**Stream:** repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py`; asserts 1847 pairs / 96 types held).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim from battery-queue.json)

"coordinate with ne-follower-verbless-sweep (promote) - classify; if a
verb-less family exists, re-frame @508 inside it"

## Numbered clauses (restated before testing)

1. C1 — Coordinate with ne-follower-verbless-sweep (verdict PROMOTE, processed
   report): adopt its census (do NOT duplicate per the adverse), re-derive the
   repaired stream in-session, and confirm all 37 94-windows at the parent's
   @-offsets byte-exact.
2. C2 — Spot-verify the D3 verb-presence classification on the bytes (5
   attachable + 5 un-attachable windows, using the parent's verb-class set
   V={24,31,32,33,86,88} and blocker set {87,47,46,64,96,17,79,00,84,59}).
3. C3 — If a verb-less family exists, confirm the @508 re-frame inside it on
   the verified bytes (0-based @508 = the 62 of the 62-94 contact whose 94 is
   at 0-based @509).

## Method

1. Read BATTERY-PROTOCOL.md first; created `locks/verbless-ne-family.lock`
   on start (2026-10-09T07:14:01Z), deleted on completion.
2. Re-derived the repaired stream independently; asserted 1,847 pairs, 96 types.
3. Compared my 94-window census against ne-follower-verbless-sweep's list.
4. Spot-verified 10 D3 assignments with the parent's exact method
   (nearest forward verb-class group within +1..+8, no granted non-clitic
   intervener; 11/77 excluded from blockers).
5. Verified the 62-94 x9 bigram count, the 94-64 stream-unique bigram, and the
   target window bytes on row a3_00.
6. Checked the queue for the parent's proposed follow-ups
   (seg-62-94-wordfinal, ne-attachable-paradigm) to avoid duplication.

## Window-level evidence

### C1: stream and census verification

- Repaired stream: 1,847 pairs, 96 types — asserts held.
- My 37 94-window enumeration matched the parent's offset list byte-exact
  (0-based @: 65 101 161 250 318 349 494 509 558 570 578 651 688 699 762 771
  774 785 841 1102 1169 1182 1293 1330 1353 1363 1549 1576 1664 1687 1701 1705
  1713 1742 1773 1795 1806).
- 62-94 bigram: exactly x9 on the stream (0-based 94 positions 101 509 762
  841 1330 1363 1687 1705 1773) — matches the parent's list byte-exact.
- 94-64 bigram: exactly x1 stream-wide (94 at 0-based @509, 64 at @510) —
  stream-unique, matches the parent.
- Target window bytes (0-based @506–511, all row a3_00):
  `67 77 62 94 64 98` — matches the parent's "39 68 21 67 77 62 94 64 98 65
  88 56 87" left/right profile.
- n(77) = 44 — matches the parent.

### C2: D3 spot-verification (10/10 assignments match)

| 0-based @ | D3 result | Parent assignment | Match |
|---|---|---|---|
| @64 | attachable (24@+5) | attachable | YES |
| @160 | attachable (24@+2) | attachable | YES |
| @770 | attachable (33@+6) | attachable | YES |
| @1329 | attachable (86@+6) | attachable | YES |
| @1772 | attachable (24@+2) | attachable | YES |
| @508 | un-attachable (64 blocker @+1) | un-attachable | YES |
| @100 | un-attachable | un-attachable | YES |
| @348 | un-attachable | un-attachable | YES |
| @577 | un-attachable | un-attachable | YES |
| @1181 | un-attachable | un-attachable | YES |

### C3: the @508 re-frame on verified bytes

- The 94 at 0-based @509 is D3-un-attachable: its +1 follower is 64='qui'
  (granted), a hard blocker — particle-'ne' attachment fails at kill grade
  at this window ("ne" never directly precedes "qui" in 1841 French).
- Left profile matches the family's modal pattern: 62-94 x9, of which 6/9
  are D3-un-attachable (@101, @509, @762, @841, @1363, @1687).
- The re-frame (adopted from the parent battery, confirmed on the verified
  bytes): the @508 window belongs to the un-attachable 94-family; its 94 is
  a non-particle re-segmentation candidate (62-94 word-final "ne" syllable,
  or a distinct 94 value per the R17-018 duality). No second 94 value is
  DECLARED here (§7: red-team declaration required); the re-frame is a
  segmentation hypothesis, not a value claim.

### Annotation correction (minor; assignments unaffected)

The parent's forward-position annotations skip the duplicate-94 intervener
in two windows (e.g. @64: parent "24@+4 [92 69 13]", mine 24@+5 because a
second 94 sits at +1; @770: parent "33@+5 [07 06 94 15]", mine 33@+6 with
two intervening 94s). The bytes are identical; only the annotation
convention differs. Recorded for the record; it does not change any
assignment.

## Per-clause pass/fail

1. C1: PASS — stream and all 37 windows verified byte-exact against the
   parent census.
2. C2: PASS — 10/10 D3 spot-verifications match (adverse honored: adopted,
   not duplicated).
3. C3: PASS — the verb-less family exists (the parent's 28-member
   un-attachable family; the target 94 is verified un-attachable via the
   64='qui' blocker), and the @508 re-frame inside it is confirmed on the
   verified bytes.

## Adverses answered

- "coordinate with ne-follower-verbless-sweep, do not duplicate" —
  answered: the parent's census was adopted as evidence and spot-verified,
  never re-run. No battery result was duplicated.

## Standing verdicts

- R17-001 (94='ne' STRONG LEAD): UNTOUCHED — the re-frame is a
  segmentation hypothesis, not a value claim; the lead's domain stays as
  the parent battery delimited it.
- No standing or red-team verdict contradicted or downgraded. No
  polyvalence declared (§7 intact).

## Verdict: PROMOTE

The bar's conditional is confirmed at battery grade on independently
verified bytes: the verb-less 94 family exists (@509's 94 is not the sole
verb-less 'ne' — spot-verified 9 other un-attachable windows alongside 5
attachable ones), and the @508 window is re-framed inside it as a
non-particle re-segmentation candidate with the specific blocker
(64='qui' at +1) and the family profile (62-94 modal pattern) named.

## Follow-up proposed (optional, verified absent from queue)

1. `seg-62-94-wordfinal` (P2) — test the surviving 62-94 x9 as word-final
   "ne" syllable (paradigm: 70-12-94 "prenne", 61-94 candidate); the
   re-frame's segmentation hypothesis is the natural next test. (The
   parent's `ne-attachable-paradigm` (P3) is likewise absent; the
   supervisor may queue either.)

## Bookkeeping

- Lock `code/crowd17/next-token/locks/verbless-ne-family.lock` created on
  start (agent id + UTC), deleted on completion (verified gone).
- `battery-queue.json`: `verbless-ne-family` status `queued` -> `verdict`,
  `verdict: {"result": "promote", "report":
  "code/crowd17/report_inbox/battery-verbless-ne-family.md", "date":
  "2026-10-09"}` (temp-file + rename; pre-write assert confirmed
  queued/verdictless — no downgrade; JSON re-validated; only this entry
  touched).
- R5005, sealed gates, red-team adjudication queue untouched.
