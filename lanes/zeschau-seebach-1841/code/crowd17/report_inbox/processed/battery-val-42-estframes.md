# Battery report: val-42-estframes — verdict: NULL (value underdetermined)

Target: `val-42-estframes` — name 42's value at the 59-42 bigram (@463/@1186).
Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types
re-derived in-session, asserts held). `canonical.py` never used. R5005,
sealed gate instances, red-team adjudication queue untouched. Lock
`code/crowd17/next-token/locks/val-42-estframes.lock` created on start
(2026-10-09T10:45:08Z); no prior/stale lock existed; deleted on completion.

@-offsets below are 0-based pair indices (the brief's @463/@1186 are the 59
positions; 42 sits at 464/1187).

## Bar (verbatim, pre-registered)

"one value for 42 parsing both 'cela est [42]' @463 and 'est [42]' @1186 as
predicate nouns with <=1 ungranted assumption; kill iff no value does"

Numbered clauses (fixed BEFORE the window census, not modified after):

- **C1:** One specific French value for 42 is named that parses "cela est
  [42]" @463 as a predicate-noun construction with <=1 ungranted assumption.
- **C2:** The same value parses "est [42]" @1186 as a predicate-noun
  construction with <=1 ungranted assumption.
- **C3 (kill arm):** Kill iff NO value parses both frames as predicate nouns
  within the assumption budget.

## Method

1. Re-derived the repaired stream byte-exact per `repair_parse.py`.
2. Located the "59 42" bigram: exactly 2x stream-wide, @463 and @1186
   (0-based 59 positions). Full ±6 windows re-derived below.
3. Adopted (never re-litigated) standing values: pencil 11=la, 29=er, 40=e,
   46=que; granted 87=ce, 96=par, 00=pour (A9), 47=ce (A4); provisional
   59=est; battery 94=ne, 12=n, 48=e, 06=ent.
4. Adopted 42's class NOUN from `val-42-nominal` (PROMOTE, 2026-10-08) per the
   adverse; class not re-opened. A1 predicative-frame grant used as frame
   only.
5. Tested whether any single value is DETERMINED by the two windows (the
   lane's naming standard: a value is named when evidence selects it, not
   when it is merely compatible — cf. §3, never invent data).

## Window-level evidence (@-offsets, 0-based)

**W1 @463 (row a2_10):** `... 02 79 87 11 | 59 42 | 96 00 33 79 80 06 ...`
= "tout(79) ce(87) la(11) est(59) [42] par(96) pour(00) [33] ..." —
"tout cela est [42] par pour [33]". The local frame "cela est [42]" is a
clean predicate-noun slot (1 ungranted assumption: provisional 59=est).
Downstream caveat (outside 42's frame, recorded not decided): "96 00" =
"par pour" is ungrammatical as written — no agent NP follows "par". This
constrains the full-window parse, not the "est [42]" frame.

**W2 @1186 (row a6_10):** `... 82 06 06 | 59 42 | 06 84 59 46 ...`
= "ne(94) m(82) ent(06) ent(06) est(59) [42] ent(06) on(84) est(59) que(46)"
— "est [42]" with the 06 contact. The 06 contact is fenced in standings
(`battery-stem-42-verb`: adjectival "-ent" or clause-boundary — adopted, not
re-litigated). Under the clause-boundary arm ("est [42]. Ent...") the local
"est [42]" frame is a clean predicate-noun slot (1 ungranted assumption:
provisional 59=est). Note: `subject-1186-est42` (PROMOTE, 2026-10-09) fenced
this clause as a subjectless-'est' residual — adopted; the residual is the
clause's, not 42's value.

**42's wider profile (n=20, re-derived):** subject slots before "ne [verb]"
(@784 "[24] [42] ne [74]", @1794 "[56] [42] ne est [37]" — nominal-consistent);
"29->42" x3 (@79 "la er [42]", @219 "que [X]er [42]"); "76->42" x3; "42->06"
x5 (the verb-stem contact — `stem-42-verb` found genuine "42ent" 3pl-verb
legs at @206 "[42]ent le [44]" transitive and @544 "[42]ent pour que"; the
noun/verb-stem polyvalence is ESCALATED to the red team per §7, not decided
here); "33 42" x2 (@267/@1504, possibly word-internal); "61 42 48" @282
(48='e' may compose a feminine "[42]e").

## Per-clause results

- **C1: FAIL.** No value is determined. The "est [42]" frame accepts ANY
  French noun ("cela est fait/vrai/bien/droit..."), so the windows select
  noun-ness (already promoted) but no specific value. Naming any one of
  them — "fait", "vrai", "bien" — would be invention under §3, not a finding.
  No window in 42's 20-window profile determines the value either: the
  subject slots (@784/@1794) and infinitive-object slots (@219) are
  class-level only; the "33 42" and "61 42 48" composition leads are
  untested at battery grade.
- **C2: MOOT** (no value named in C1).
- **C3: does NOT fire.** Values exist that parse both local frames within
  the budget (any French noun in the "est [N]" slot; 1 ungranted assumption
  each, the provisional 59=est). No window forces every value false: W1's
  "par pour" awkwardness is downstream of 42's frame, and W2's
  subjectless-'est' fence is the clause's, already fenced by standing
  battery.

## Verdict: NULL

Not kill-grade: the kill arm's condition ("no value parses") is false — the
local "est [42]" frames are satisfiable. Not promotable: no value is
determined, and naming one would invent data. 42's value stays open; its
NOUN class (val-42-nominal PROMOTE) stands untouched.

## Adverses answered

- "42's class is battery-promoted - class standing is not re-opened, value
  only": ANSWERED. NOUN adopted as premise throughout; no class claim made
  or disturbed. A1's predicative-frame grant used as frame only.
- The 42-06 verb-stem contact (stem-42-verb) and its §7 polyvalence
  escalation: noted, not re-litigated, not decided — red-team venue.

## Follow-ups proposed (for supervisor queuing)

1. `val-42-lettertier` (P3) — letter-tier composition test: "33 42" x2
   (@267/@1504) as one word, and 42 against the 29/40/33 syllabary. A
   composed 42 names its syllable value directly. Bar: name 42's syllable
   iff one composition parses with zero new assumptions.
2. `frame-464-fullparse` (P3) — full-window parse of @464's "59 42 96 00"
   ("est [42] par pour"). Resolving the "par pour" sequence constrains 42's
   right edge (passive participle? "42-96" one word?) and may determine the
   value. Bar: one grammatical full-window parse with <=1 ungranted
   assumption, or fence @464 as a 96/00-driven residual.
3. `val-42-282-fem` (P3) — test "61 42 48" @282 as "[61] [42]e" with 48='e'
   composing a feminine noun/adjective. A clean feminine word narrows 42's
   value to the feminine-noun inventory. Bar: name the value iff "[42]e" is
   a licensed French feminine word parsing the window.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-42-estframes.md` (this file).
- Queue: `val-42-estframes` queued -> verdict/null via temp-file + rename,
  own entry only; pre-write assert confirmed no prior verdict; JSON
  re-validated post-write.
- Lock `val-42-estframes.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
