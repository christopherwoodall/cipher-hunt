# Battery `58-complement-1695` — verdict: PROMOTE (58 = nominal, noun-class)

Target: name 58's class from the @1695 gerund-complement datum.
Date: 2026-10-09. Worker: agent 645a58b5-2455-438e-898d-e80523b2c30e.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived
in-work; n(58) = 7 re-derived). `canonical.py` never used. R5005, sealed
gate instances, red-team adjudication queue untouched. Lock
`code/crowd17/next-token/locks/58-complement-1695.lock` created on start
(2026-10-09T07:20:00Z); no prior/stale lock existed; deleted on completion.

Indexing: @-offsets are 0-based pair indices of **58** (cede-614-subject /
ant-58-ending convention).

## Bar (verbatim, pre-registered BEFORE testing)

"name 58's class with the @1695 window parsing ('qu'en [85] [58]' gerund-complement position) and >=2 more windows under one class with zero forced contradiction; else fence"

Numbered clauses (fixed BEFORE the stream census, not modified after):

- **C1:** The @1695 window parses as 'qu'en [85] [58]' with 58 in
  gerund-complement (nominal) position.
- **C2:** 58's class is named as ONE class consistent with C1.
- **C3:** >=2 more windows parse under that class with zero forced
  contradiction.
- **Else-arm:** if any clause fails, fence with stated cause (records a null).

## Method

1. Re-derived the repaired stream byte-exact per `repair_parse.py`.
   58 census: positions (0-based) [55, 122, 157, 610, 1202, 1695, 1756];
   predecessors {85:3, 19:1, 35:1, 02:1, 45:1}; successors {35:2, 66:1,
   47:2, 15:1, 17:1} — exact match to cede-614-subject's re-derived census.
2. For each window, tested the nominal (noun-class) hypothesis plus rival
   classes (bound verbal ending — standing-killed by ant-58-ending;
   free verb; object pronoun; preposition; adverb) under standing values:
   pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce,
   64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9, leg-1
   class-level), 84="on" (A15), 47="ce" (A4 allophone tier); provisional
   77=le, 59=est; frames 85 verb-stem (A3), 37/32/42 predicative (A1);
   HOLD 45="ce" (A11, R18-strengthened); 67 sole true polyvalence (§7).
   1841 diplomatic French throughout.
3. A "forced contradiction" at kill grade = a clean standing-values frame
   in which every non-nominal parse survives and every nominal parse is
   ungrammatical. Distributional asymmetry is NOT forced contradiction.

## Window-level evidence (@-offsets, 0-based)

- **@1695 (a8_06): `60 27 46 24 85 [58] 15 23 91 85 33`** — FLAGSHIP.
  "…27 46[que] 24 85 58 15…" Per the 24-en-verb-conflict null (2026-10-09,
  newer than cede-614-subject), the modal parse is dead here (C2 of that
  battery: no subject after "que"); the 'ant'-ending rival is dead by
  ant-58-ending (kill). SOLE surviving parse: "qu'en [85] [58]" — gerund
  + complement. 58 sits in complement (nominal) position. Dissolves
  cede-614-subject's anti-noun leg at this window ("modal + bare stem +
  noun ungrammatical"): the modal reading is no longer live. ✔ nominal leg.
- **@1756 (a8_08): `28 89 26 24 85 [58] 17 78 41 15 93`** — LEG.
  The 24-conflict battery records all THREE parses surviving at the
  @1754-56 pair: (a) gerund "[26] en [85] [58]"; (b) modal "[26-subj]
  [24] [85-inf] [58]" iff 26 nominal; (c) pronoun+finite "[26-subj] en
  [85-finite] [58]" iff 26 nominal. Under ALL THREE, 58 follows [85] as
  its complement/object — nominal position, independent of 26's class.
  No duplication of 26-class-1754's bar (26's class is taken only as a
  boundary: the claim about 58 holds on every branch). Bonus: successor
  17="fois" (granted) gives "[58] fois" — "X fois" is noun-shaped
  ("une fois"-shaped). ✔ nominal leg.
- **@1202 (a7_00): `82 16 64 29 45 [58] 47 43 55 61 21`** — LEG.
  "…er(29) ce(45) [58] ce(47) [43]…" Parses as "ce [58-noun]" (demonstrative
  + noun) with a clause boundary before 47 ("…er ce [N] | ce [43]…").
  Kill-grade facts that live here: ant-58-ending forced 58 NON-VERBAL
  ("ceant" non-word under A11 45='ce' + A4 47='ce'); "ce [58-verb] ce" is
  ungrammatical ('ce' cannot subject a lexical verb — cede-614-subject);
  pronoun ("ce le ce"-shaped) and preposition ("ce [prep] ce") fail here
  too. The only surviving class at this window is nominal. ✔ nominal leg
  (and the rival-class discriminator).
- **@610 (a4_00): `54 64 39 64 02 [58] 47 77 87 83 70`** — COMPATIBLE.
  "qui(64) a/à(39) qui(64) [02] [58] ce(47) le(77)…" Nominal parse:
  "[02-verb] [58-N]" as verb + direct object ("…qui [V] [N] ce…"); the
  right edge "47 77" = 'ce le' is the standing fenced residual
  (ce-le-verb-frame, battery grade) and is NOT re-litigated. Conditional on
  02 verb-shaped (02's class is open; ne-alone-02-74's kill was of 02 as
  the *negated* verb in a different frame, not of 02=verb generally). No
  forced contradiction at 58's slot. Recorded as compatible-with-condition,
  not a clean leg.
- **@122 (a1_03): `14 21 60 90 19 [58] 66 98 82 48 11`** — COMPATIBLE.
  "[19] [58] [66] vient(98)…". 19, 66 open; "[19-adj?] [58-noun]" parses
  without any standing-value strain. No forced contradiction.
- **@157 (a1_04): `46 66 84 26 35 [58] 35 93 52 94 24`** — COMPATIBLE.
  "on(84) [26] [35] [58] [35]…". 35 unknown both sides; no frame forces
  58's class either way. No forced contradiction.
- **@55 (a1_01): `79 37 11 79 85 [58] 35 53 12 41 08`** — FENCED, not
  contradicted. The left edge carries the banked "11 79" = "la tout"
  contradiction (round 18, standing record): the window has no clean
  grammatical frame under standing values, so it cannot kill-test 58's
  class at battery grade (a forced contradiction needs a clean frame that
  excludes nouns; none exists here). Fenced with stated cause: upstream
  contradiction, window uninterpretable at battery grade.

Distributional note (cede-614-subject, standing): 58's predecessors are
{85:3, 19:1, 35:1, 02:1, 45:1} — zero determiner/preposition predecessors
vs 11/77/96-attested nouns 21/26/81. This is distributional asymmetry,
not a forced contradiction: gerund complements are routinely bare
("en prenant froid"-shaped), and the bar's standard is zero *forced*
contradiction, which holds. Recorded as the standing caveat.

## Per-clause results

- **C1: PASS** — @1695 re-derived byte-exact; sole surviving parse
  "qu'en [85] [58]", 58 in gerund-complement (nominal) position.
- **C2: PASS** — 58's class named: **nominal (noun-class)**. The @1202
  kill-grade discriminator leaves nominal as the only class surviving all
  windows; the rival classes (verb-ending — standing kill; free verb;
  pronoun; preposition) each fail at @1202.
- **C3: PASS** — @1756 and @1202 parse as clean nominal legs; @610, @122,
  @157 compatible with zero forced contradiction; @55 fenced with stated
  cause (not a forced contradiction).
- **Else-arm: not triggered.**

## Adverses

- "58's class open": ANSWERED — named as nominal (noun-class) with four
  parsing windows and a kill-grade rival-class discriminator.
- "@1756 stays 3-way ambiguous pending 26's class (coordinate with
  26-class-1754)": ANSWERED as a boundary, not duplicated. All three
  surviving @1754-56 parses (24-conflict null, 2026-10-09) place 58 in
  complement position; the 58 claim holds under 26-nominal and
  26-non-nominal alike. No claim made about 26's class; 26-class-1754's
  bar untouched.

## Standing-state check

No standing verdict contradicted or downgraded. ant-58-ending's kill
(58='ant') is untouched — noun-class ≠ 'ant' ending. cede-614-subject's
null is refined, not contradicted: its blocker (the 24-conflict) is now
resolved in 58's favor at @1695 by the newer 24-en-verb-conflict null,
and its distributional caveat is carried forward here as a caveat.
The queued `58-noun-adjudicate` target (P3, stricter distributional bar)
is NOT preempted — this battery's verdict stands on its own pre-registered
bar; that target's bar remains live work for a future worker. R5005,
sealed gate instances, red-team adjudication queue untouched.

## Verdict: PROMOTE

58 = nominal (noun-class). All bar clauses pass; all listed adverses
answered; no standing verdict contradicted. Caveats standing: zero
determiner predecessors (distributional, not forced); @55 fenced on the
banked "la tout" contradiction; exact noun value unnamed (beyond battery
grade here).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-58-complement-1695.md` (this file).
- Queue: `58-complement-1695` queued → verdict/promote via temp-file + rename,
  own entry only; pre-write assert confirmed no prior verdict (was JSON
  null); JSON re-validated post-write; evidence/adverses text preserved,
  new evidence appended.
- Lock `58-complement-1695.lock`: created on start, deleted on completion.
