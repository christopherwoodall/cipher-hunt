# Battery report: rightedge-56-1745

Target: `rightedge-56-1745`. Date: 2026-10-09. Worker: eb59c2f3-befa-45b8-bf70-39638e2abc29.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`;
1,847 pairs re-verified in-worker). `canonical.py` never used. R5005, sealed
gates, red-team queue untouched. Coordinate note: leftedge-52-86-1736 runs in
parallel; this battery does not duplicate its bar (no claim made about
@1736-1741).

## Bar (verbatim, pre-registered)

"(a) 56 named from its contact profile; (b) 'que [56]e ent' parses as
conjunction + 3pl verb with zero contradiction; (c) result states the
consequence for the @1742-1744 fence (fixes the right edge, isolates the
left-edge failure)"

Numbered clauses (fixed before testing, not modified after):

1. C1 — 56 is NAMED from its contact profile (a value, not just a class).
2. C2 — "que [56]e ent" (@1744-1747) parses as conjunction + 3pl verb with
   zero contradiction against standing values.
3. C3 — the report states the consequence for the @1742-1744 fence: the
   right edge is fixed, the left-edge failure is isolated.

## Method

Byte-exact census on the repaired stream. Target window re-derived:
@1744=46, @1745=56, @1746=40, @1747=06 (row a8_07/a8_08 boundary; offsets
0-based, consistent with ni-1740-1742). Standing values used: 46="que"
(banked pencil GT), 40="e" (banked pencil GT), 06="ent" (promoted, ent-06
battery, conditional R17-007), 82="m" (banked GT), 94="ne" (battery-promoted,
conditional). 56's full contact profile censused (n=23). All "X-40-06"
trigrams and all 06-predecessors censused.

## Window-level evidence (@-offsets)

Target window (byte-confirmed):

- @1742=94, @1743=82, @1744=46, @1745=56, @1746=40, @1747=06, @1748=65,
  @1749=34. Left: @1736-1741 = 12 48 52 86 12 34 (the ni-1740-1742 fence
  window @1739-1744 = 86 12 34 94 82 46).

56's contact profile (n=23, full census):

- Verb-slot legs: "64 56" @794-795 = "qui [56]" (a5_04: "46 07 64 56 37
  44 77") — finite-verb slot after relative "qui". "46 56" @1625-1626 =
  "que [56]" (a8_03: "67 33 46 56 69 26 00").
- Nominal legs: "56 64" @132 = "[56] qui" antecedent (a1_03);
  "56 17" @836 = "[56] fois" quantifier slot (a5_06); "56 37" x2 (@795,
  @1654), "56 32" x2 (@1282, @1571), "56 42" @1793 — pre-predicative-
  adjective slots.
- Pre-"ce": "56 87" x2 (@70, @514), "56 47" x2 (@193, @1003).
- Killed-subject windows: "56 30 06" x2 (@1326, @1732) — 56 as subject of
  "passent" KILLED by pasent-subject-26-56 (2026-10-09); subject reading
  dead, verb/noun/adverb readings live.
- "46 56" occurs exactly 2x stream-wide: @1625 and @1744.

"X-40-06" frame census: "40 06" is a HAPAX — occurs exactly 1x
stream-wide, at @1746-1747. No corpus parallel for an "e"+"ent" stem
boundary. (Not a contradiction: hapax is not contradiction.)

06-predecessor census (06 n=44): 40 precedes 06 exactly 1x (this window);
the promoted ent-06 legs use other stems (82-06 x4 "ment", 42-06 x5,
30-06 x4). Nothing in the 06 census contradicts an e-final stem.

Morphology: "[X]e"+"ent" is a real French 3pl shape (the Xéent class:
créer→"créent", agréer→"agréent", suppléer→"suppléent",
recréer→"récréent", gréer→"gréent"). 56-40-06 segments cleanly as
[56-stem]+"e"(40)+"ent"(06).

## Per-clause pass/fail

- **C1 — FAIL (null grade, not kill grade).** 56 cannot be NAMED from its
  contact profile. The profile supports a verb-stem class reading
  ("qui [56]" @795 verb slot; "que [56]" @1625/@1744), but the specific
  verb is underdetermined: the Xéent class (créer/agréer/suppléer/
  recréer/gréer/maugréer...) cannot be discriminated from contact data
  alone — no valency frame in 56's windows selects one member. Worse,
  the profile is mixed-class: nominal legs ("56 64" @132 antecedent,
  "56 17" @836 "N fois", pre-predicative-adjective x5) sit beside verb
  legs, and bare-56 as finite verb (@795 "qui [56]", @1626 "que [56] 69
  26") vs stem-56 in 56-40-06 @1745 raises the stem-vs-whole question
  (A10 standard) plus a §7 sole-polyvalence question (67 et/veut is the
  only true polyvalence — a noun/verb class alternation for 56 needs
  red-team declaration). No window forces 56 ≠ verb stem, so this is
  inconclusive, not kill. The adverse "56's value open" is therefore
  FENCED with stated cause (underdetermined Xéent identity + mixed
  class profile + §7), not answered by naming.
- **C2 — PASS.** "46 56 40 06" parses as conjunction "que" + 3pl verb
  "[56]e-ent" with zero contradiction: 46="que" (banked), 56 verb-stem
  class (profile-supported, subject reading killed independently),
  40="e" (banked), 06="ent" (promoted verb ending, in-grant use). The
  Xéent 3pl shape is grammatical French. "40 06" hapax is not a
  contradiction. No standing value is violated; no window forces an
  alternative segmentation. Caveat (fenced, not ignored): the
  subordinate clause's SUBJECT is not inside the segment — it belongs
  to the fenced left edge / red-team fence, which is exactly what C3
  isolates.
- **C3 — PASS (stated).** Consequence for the @1742-1744 fence: the
  right edge is FIXED — @1745-1747 is a 3pl verb closing the "que"
  subordinate clause, so the ni-1740-1742 fence's failure is now
  isolated entirely to the left of @1744. The fenced problems are:
  (i) "94 82 46" = "ne m que" verbless strain (@1742-1744, both ni
  readings killed 2026-10-08); (ii) the missing/overt subject of the
  "que [56]ent" subordinate clause (French does not pro-drop; the
  subject must be found left of @1744 in the fenced region or right of
  @1747 — leftedge-52-86-1736 owns the left side). The fence is
  narrowed, not resolved: red-team ownership of @1742-1744 stands.

## Verdict

**NULL** — inconclusive. C2 and C3 pass; C1 fails at null grade (56's
value underdetermined, mixed class profile, §7 polyvalence question).
Not kill: no window forces the claim false — the segment parses cleanly
as "que"+3pl verb with zero standing-value contradiction. Not promote:
the bar demands 56 NAMED, and naming is not achievable from the profile.
No standing verdict contradicted or downgraded: ent-06 promote used
in-grant; pasent-subject-26-56 kill untouched (56-as-subject dead, 56-as-
verb-stem live — the two claims are compatible); ni-1740-1742 kill
affirmed and its fence narrowed; §7 untouched (no polyvalence declared).

## Follow-ups proposed (null regenerates work)

1. `name-56-verb` (P3) — discriminate the Xéent-class verb at @1745:
   test créer/agréer/suppléer/recréer/gréer valency against 56's
   verb-slot windows (@795 "qui [56] 37", @1626 "que [56] 69 26",
   @1745 "que [56]e ent"). Bar: one candidate's valency fits all three
   windows or fence the identity as underdetermined.
2. `stem-56-whole` (P2) — adjudicate bare-56 (@795, @1626) vs stem-56
   (@1745) per the A10 stem/whole standard (<=10% orphan); red-team eyes
   on whether the noun/verb class alternation needs a second-
   polyvalence declaration or resolves via substantivization/inflection.
3. `subj-1744-que` (P2) — locate the subject of "que [56]ent": test
   postverbal 65 ("que [56]ent [65]") vs subject-from-fenced-left-edge;
   bar: one grammatical subject placement with <=1 non-granted
   assumption, or confirm the subject gap as a stated cause inside the
   @1742-1744 red-team fence.

## Bookkeeping

- Report: this file.
- battery-queue.json: `rightedge-56-1745` → status `verdict`, result
  `null`, date 2026-10-09 (temp-file + rename, own entry only).
- Lock `locks/rightedge-56-1745.lock`: created on start, deleted on
  completion. No pre-existing lock was present.
