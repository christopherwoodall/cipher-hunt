# Battery report: qui-02-750-parse

## Bar (verbatim from battery-queue.json)

"if qui-legs drop to one, anti-verb side wins outright"

## Bar restated as numbered pass/fail clauses

- C1: The verb requirement on 02 at the second "qui [02]" window (0-based @750, row a5_03) dissolves under a deep parse (97's class or a word-boundary rescue), dropping 02's qui-legs from two to one.
- C2 (conditional on C1): The anti-verb side wins outright for 02's class.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed
per `repair_parse.py`: 1,847 pairs / 96 types, byte-exact. `canonical.py` never
touched. R5005, sealed gates, and the red-team adjudication queue untouched.
All @-offsets below are 0-based stream indices (queue convention); the target
label "@750" is 02's 0-based position (1-based @751).

Standing premises adopted (not re-litigated): 64="qui" banked GT;
11="la" banked GT; 40="e" banked GT; 67 et/veut positional rule
(67="veut" iff follower infinitive-shaped); 94="ne" STRONG LEAD;
{48,94} homophone-set kill; 02-class-609's split signature (verb-selecting
"qui [02]" at @609/@750; verb-excluding @305 "88 02 88" and @858
"on [02] faire").

## Window-level evidence

Target window (byte-confirmed): 0b@746-753, row a5_03 mid-row
(row a5_03 starts at 0b@748):

    85 28 | 00 64 02 97 40 67 | 11 70 82 34 29 40 ...
         "[85] [28] pour qui [02] [97] e et la pre m i er e ..."

- a5_03's repaired offset is **0** and is **pencil-gloss-anchored** (gloss i,
  the "la pre m i er e" crib at 0b@754-759). This window sits on one of the
  two gloss-anchored rows, so it is immune to the offset-1 resegmentation
  rescues that dissolved the a1_01 ("la tout") and a7_10 (@1481) frames.
- 64 at 0b@749 and 02 at 0b@750 are on the **same row** (a5_03); no row
  boundary, no punctuation, no formula marker, no gloss marker at the contact.
- "02 97" is a **stream hapax** (only 0b@750). "64 02" occurs exactly 2x
  stream-wide (0b@608, 0b@749) - the two qui-windows.
- 97: n=10, value open. Windows: "00 97 51" (@3), "81 97 46" (@95),
  "00 97 09" (@289), "40 97 86" (@300), "81 97 47" (@526),
  "80 97 13" (@567), "00 97 41" (@589), "02 97 40" (@752),
  "16 97 69" (@1413), "00 97 00" (@1824).
- First qui-window (for comparison): 0b@607-613, row a4_00:
  "64 39 64 02 58 47" = "qui [39] qui [02] [58] ce(47)".
- 67's follower here is 11="la" (not infinitive-shaped), so 67="et" by the
  positional rule: the frame's right edge reads "[97]e et la premiere".

## Dissolve routes tested

**Route A - 97 as the finite verb, 02 as intervenor ("qui [02] [97-fin]").**
97 has genuine verb legs ("97 46" = [97] + "que"-complement at 1b@95;
"97 47" = [97] + "ce"-object at 1b@526; "00 97" x4 infinitive-compatible),
but 97's class is OPEN - none of these legs is forced, and "80 97 13"
@567 is awkward for a finite 97. More decisively, 02 as the intervenor
between "qui" and a finite verb needs a forced non-verb class: negation
"ne" is blocked (94="ne" STRONG LEAD, no homophony evidence for 02);
clitic/adverb values for 02 have zero battery-grade evidence. The parse
"qui [02-?] [97-fin]e" is COMPATIBLE, not FORCED - and battery grade needs
FORCED (stem-03-value precedent). Route A does not dissolve the leg at
battery grade.

**Route B - clause/word boundary between 64 and 02 ("pour qui | [02] ...").**
No byte evidence: mid-row a5_03, same row on both sides, no punctuation,
no formula marker, no crib/gloss marker at the contact. Fenced with stated
cause.

**Route C - sub-lexical "02 97" as one word.**
"02 97" is a hapax; 02 has no established letter-tier neighbors; no
composition evidence. Even if composed, the unit would still occupy the
verb slot after "qui" - the rescue has no battery-grade premise. Fenced.

**Route D - interrogative "pour qui?" reading.**
Interrogative "qui" still requires a finite verb ("pour qui [verbe]?").
The verb requirement does not dissolve under this reading.

**Standing parse survives:** "pour qui [02-verb] [97]e et la premiere..."
- 02 as finite verb, "[97]e" as feminine noun/adjective object
(40="e" composing leftward), "et la" continuing the coordination - fully
grammatical, zero forced contradiction.

## Per-clause pass/fail

- **C1: FAIL (antecedent not met).** No dissolve route survives at battery
  grade. The second qui-window remains verb-selecting for 02.
- **C2: not reached.** The anti-verb side does not win outright.

The strengthened-anchoring finding: because the @750 window sits on the
gloss-anchored row a5_03, its qui-leg is phase-solid - the offset-1
mechanism that dissolved other forced frames cannot touch it.

## Verdict

**NULL.** The bar's antecedent is not met: 02's qui-legs stand at two
(@609, @750). 02 remains a §7 split candidate - verb-selecting at the two
qui-windows vs verb-excluding at @305 ("88 02 88", three-finite-verb
strain) and @858 ("on [02] faire"). No polyvalence declared at battery
level. No standing verdict contradicted or downgraded; §7 intact.

## Follow-ups proposed (1-3, per protocol §4)

1. `val-97-verb-test` (P3) - name 97's class from its 10 windows
   ("97 46" que-complement, "97 47" ce-object verb legs vs "00 97" x4
   infinitive frames and "80 97 13" @567); a forced verb-97 re-opens
   Route A with 02 as the intervenor to test.
2. `val-02-clitic` (P3) - test 02 as negation/clitic/adverb in the
   "qui [02] [97]" slot; a forced non-verb 02 at @750 drops the qui-leg.
3. `qui-02-609-parse` (P3) - deep parse the FIRST qui-window
   ("64 39 64 02 58 47", 0b@607-613, row a4_00); if its verb requirement
   dissolves there, qui-legs drop to one from the other side.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/qui-02-750-parse.lock` created on
  start, deleted on completion.
- `battery-queue.json` `qui-02-750-parse` -> status `verdict`,
  result `null`, date 2026-10-09 (temp-file + rename, own entry only,
  pre-write assert confirmed queued/verdictless, JSON re-validated).
- Adverses: none listed on this target.
