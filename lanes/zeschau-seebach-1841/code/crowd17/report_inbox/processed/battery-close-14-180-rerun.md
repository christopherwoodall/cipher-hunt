# Battery report: close-14-180-rerun

- Target: `close-14-180-rerun`
- Verdict: **PROMOTE**
- Date: 2026-10-09
- Parent: battery-ce-qui-left-closure (NULL, fence executed) — follow-up #1
- Stream: repaired 1,847-pair / 96-type parse from `data/upstream-ct_R5005.txt`
  + `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs, 96 types).
  `canonical.py` never used. R5005 never touched. 1841 diplomatic French.

## Bar (verbatim, pre-registered)

> '69 [14] [24]' closes with zero new assumptions iff 14's granted role
> composes (e.g., 14='en' -> '69 en [24]'); else fence W2 permanently.

Restated as numbered pass/fail clauses before testing:

- **C1:** 14 has a granted role (the trigger condition is met).
- **C2:** the granted role composes at the W2 locus ("69 14 24", 0b@177–179).
- **C3:** the closure uses zero new assumptions (all premises standing or
  battery-grade; nothing invented, nothing ungranted).
- **Else-arm:** if any of C1–C3 fails, fence W2 permanently instead.

## Method

Re-derived the repaired stream in-session and verified the five "87 64"
adjacencies byte-exact (148, 180, 1767, 1775, 1800 — matches the parent
census). Re-examined the trigger condition first: is 14's class/value now
granted? Then tested the "69 14 24" locus under that granted role.

## C1: the trigger is met

14's role is battery-grade granted since the parent null:

- `en14-value-tighten` (PROMOTE, 2026-10-09): global 14='en' survived a
  kill-grade tighten over all 15 windows (15/15 pass, 0 forced
  contradictions), with four positive legs (@624 "m'en est", @897 "m'en",
  @1366/@1690 "tout en [60]").
- `en14-three-window` (PROMOTE, 2026-10-09): second promote.

Epistemic note: red-team ratification of 14=`en` is still pending; the
granted role is battery-grade. The bar's trigger phrase "14's granted role"
is read at battery grade — the same reading under which the supervisor
dispatched this re-run ("(14='en' promoted)" in the target brief). No
standing verdict contradicts the role: the standing 14 kills are all
verb-stem kills (uniform 14 verb stem; verb-14-rival KILL) and the lane-wide
14-verb NULL fence — 14='en' is a clitic, not a verb stem.

**C1 PASS.**

## C2: the role composes at W2

Locus byte-exact (row a1_05, 0-based): @177=69, @178=14, @179=24, @180=87.
Left context of "87 64" is "… 86 21 | 69 14 24".

Adopted premises (all standing or battery-grade, adopted by the parent
report itself):

- 69 nominal class (class-69-nominal battery PROMOTE, adopted).
- 14 = 'en' (clitic), battery-grade promote (C1).
- 24 finite/modal verb class (R17-009, red-team; R24 ratified Round 19:
  24="en" iff follower is 85 — the follower here is 87="ce" granted, so
  24 is finite/modal).

Composition: "[69-nom] en [24-fin]" — nominal subject + adverbial-pronoun
clitic "en" + finite verb. This is the licensed "il en veut" shape the
parent itself cited as the re-open criterion. "en" before a finite verb is
canonical 1841 French ("il en parle", "il en veut"); the corpus legs of the
grant (@624 "m'en est", @897 "m'en") corroborate the clitic cluster geometry.

**C2 PASS.**

## C3: zero new assumptions

The closure "69 en [24-fin]" uses exactly:

1. 69 nominal — battery PROMOTE, adopted (not new).
2. 14='en' clitic — battery PROMOTE, the bar's trigger condition (not new).
3. 24 finite/modal — red-team class grant + R24 (not new).
4. "en + finite verb" grammar — the construction is licensed French; the
   parent's own bar supplied the "il en veut" control (not new).

Nothing invented. No window-local value naming. The elsewhere-open
14-verb-stem question and 24's value are untouched — composition does not
depend on them.

**C3 PASS.**

## Verdict: PROMOTE

"69 en [24-fin]" closes W2's left with zero new assumptions once the
battery-granted 14='en' role is adopted. The else-arm (permanent fence)
does not fire.

## Scope

- Lifts the parent's W2 fence only, conditionally: the closure is licensed
  iff 14='en' holds. If the red team later rejects 14=`en`, this closure
  lapses with it — the parent fence's re-open criterion said exactly this.
- Untouched: W1/W3/W5 fences from the parent (09, 91, and W1's
  "l'on+er" problem are independent of 14); 14's value ratification
  (red-team venue); 24's value; 69's value; §7.
- No standing/red-team verdict contradicted or downgraded.

## Adverses

None listed.

## Bookkeeping

- Queue: `close-14-180-rerun` → status `verdict`, result `promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated from disk after write; own entry only; no
  downgrade).
- Lock `locks/close-14-180-rerun.lock` created on start, deleted on
  completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
