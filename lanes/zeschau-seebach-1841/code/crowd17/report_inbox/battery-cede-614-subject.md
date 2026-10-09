# Battery `cede-614-subject` — verdict: NULL (fenced with stated cause)

Target: name 58's class at @610; if noun-class, test '[58] ... cède' against the
'celle' fusion; decides @614's subject.
Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types
re-derived in-work). `canonical.py` never used. R5005, sealed gate instances,
red-team adjudication queue untouched. Lock
`code/crowd17/next-token/locks/cede-614-subject.lock` created on start
(agent-session ca91cfb2-552e-495f-82fb-58cb235b4a3f, 2026-10-09T04:46:02Z);
no prior/stale lock existed; deleted on completion.

Indexing: @-offsets are 0-based pair indices (the brief's @610 = 58's position,
@614 = 83's position). Row a4_00.

## Bar (verbatim, pre-registered)

"resolve iff 58's class decides @614's subject; else fence with stated cause"

Numbered clauses (fixed BEFORE the stream census, not modified after):

- **C1:** 58's class is named at battery grade (≥2 independent frame-legs or a
  distributional determination).
- **C2:** If 58 is noun-class, '[58] ... cède' is tested against the 'celle'
  (47-77) fusion, and the test decides @614's subject.
- **Resolve-arm:** C1 met AND 58's class decides @614's subject → resolve.
  **Else-arm:** fence @614's subject with stated cause.

## Method

1. Re-derived the repaired stream byte-exact per `repair_parse.py`.
2. Full census of 58 (n=7, re-derived): positions
   [55, 122, 157, 610, 1202, 1695, 1756]; predecessors {85:3, 19:1, 35:1,
   02:1, 45:1}; successors {35:2, 47:2, 66:1, 15:1, 17:1}.
3. Distributional comparison of 58 against known nouns (21 noun-class n=30,
   81 masc-abstract-noun n=14, 26 fem-noun n=17).
4. Tested the two subject candidates for 'cède' at @614 against standing
   values and battery-grade findings (no new assumptions).

Standing values used: pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9), 84=on (A15),
47=ce (A4 allophone tier); provisional 77=le, 59=est; A3 85 verb-stem (frame);
ne-24-profile 24=finite verb, modal-shaped (class-level promote, 2026-10-08);
A11 45=ce HOLD (R18-strengthened); §7 sole polyvalence (67 et/veut).
NOT decided here: 58's value/class, 02's class, 35's class, 83's value,
the 24='en'-vs-24=verb conflict (see §Fence).

## Window-level evidence (@-offsets, 0-based)

The @614 locus (brief's window, re-derived @606-614):
`64 39 64 02 58 47 77 87 83` = "qui(64) a/à(39) qui(64) [02] [58] ce(47)
le(77) ce(87) de(83)/cède(87-83)". Tail @615-620: `70 88 10 29 88 37`.

58's seven windows (±4):
- @55 (a1_01): `37 11 79 85 58 35 53` — "la(11) tout(79) [85] [58] [35]".
- @122 (a1_03): `90 19 58 66 98 82` — "[90] [19] [58] [66] vient(98)".
- @157 (a1_04): `84 26 35 58 35 93` — "on(84) [26] [35] [58] [35]".
- @610 (a4_00): `64 39 64 02 58 47 77` — the locus.
- @1202 (a7_00): `64 29 45 58 47 43` — "qui(64) er(29) ce(45) [58] ce(47) [43]".
- @1695 (a8_06): `46 24 85 58 15 23` — "que(46) [24] [85] [58] [15]".
- @1756 (a8_08): `26 24 85 58 17 78` — "[26] [24] [85] [58] fois(17)".

Distributional noun comparison (re-derived):
- 21 (noun): predecessors include 11='la' ×2, 96='par' ×3.
- 26 (fem noun): predecessors include 11='la' ×2, 64='qui' ×2.
- 81 (masc noun): predecessors include 77='le' ×4, 55 ×6.
- 58: predecessors {85:3, 19:1, 35:1, 02:1, 45:1} — **zero determiner or
  preposition predecessors** (no 11, 77, 96, 00). Distributionally unlike
  every known noun in the stream.

## C1: 58's class — NOT NAMEABLE at battery grade

- **Noun-class: weak.** The distributional strike above (zero determiner
  predecessors vs 11/77 for 21/26/81) counts against garden-variety
  noun-hood. Compatibility pockets exist (@1202 'ce [58]' as demonstrative +
  noun with a phrase boundary before 47; @1756 '[58] fois' as
  determiner-shaped; @122 '[19] [58]'), but none is a clean frame-leg, and
  @1695/@1756 ('[24-modal] [85-stem] [58]') leave 85 a bare stem after a
  modal under A3 + ne-24-profile if 58 is an independent noun — ungrammatical.
- **Verb-class: blocked.** Bound verbal ending KILLED at kill grade by
  ant-58-ending (2026-10-09): @1202 forces 58 non-verbal ("ce"+"ant" =
  "ceant", non-word, under A11 45='ce' + A4 47='ce'). Free-verb readings
  fare no better ('ce [58-verb] ce' @1202 ungrammatical — 'ce' cannot
  subject a lexical verb).
- **The '24-85-58' windows (@1695/@1756) are uninterpretable at battery
  grade** because of an unresolved standings conflict: ne-24-profile
  (2026-10-08, promote) made 24 a finite modal verb, but en85-gerund-reaudit
  (2026-10-08, promote) and ant-58-ending (2026-10-09, kill) both used
  24='en' (A3 GT) for the same bigrams. Under §7 (67 sole polyvalence) both
  cannot hold. This conflict is escalated as follow-up 1; it blocks 58's
  classification at its two most informative windows.
- **C1: FAIL.** No class reaches battery grade.

## C2: the subject test — both candidates fail independently

**Candidate A: the 'celle' (47-77) fusion as subject.**
47='ce' (A4) + 77='le' (provisional) read as one word 'celle', subject of
'cède' (87-83). FAIL at battery grade: the ce-le-verb-frame battery (2026-10-08)
graded the 'celle' fusion FAIL because "celle" requires a following relative
("celle qui/que/de") — and at @611 the follower of 47-77 is 87-83, not a
relative (re-derived: no 64='qui' or 46='que' in @613-620). Under the 'cède'
rival the parse is "celle cède" — bare demonstrative pronoun as subject of a
lexical verb, ungrammatical in French of any period. The fusion is dead at
@611; this extends (does not contradict) ce-le-verb-frame's fencing of @611
as a 77-value residual.

**Candidate B: '[58] ... cède' (58 as subject).**
FAIL independently of 58's class: the intervening '...' is 47-77 = 'ce le',
fenced as a 77-value residual by ce-le-verb-frame (2026-10-08, battery grade;
@611 one of three fenced windows). No re-segmentation parses with standing
values ('celle' fusion → double subject '[58] celle cède'; rival 77-values
all killed by ce-le-verb-frame; 47='ce' granted). Even a confirmed nominal
58 could not supply a grammatical subject here.

**C2: FAIL** (antecedent unconfirmed AND both consequent parses ungrammatical).

## Per-clause results

- **C1: FAIL** — 58's class not nameable (noun weak, verb-ending killed,
  24-conflict blocks the decisive windows).
- **C2: FAIL** — 'celle' fusion ungrammatical at @611 (relative-requirement);
  '[58] ... cède' ungrammatical ('ce le' fenced residual).
- **Resolve-arm: not met.** 58's class does not decide @614's subject — no
  class assignment yields a grammatical subject.
- **Else-arm: TAKEN — @614's subject FENCED with stated cause** (below).

## Verdict: NULL

Not kill-grade: no window forces a falsehood about 58's class (the class is
open, not refuted), and the bar's else-arm (fence) is the designed outcome
for exactly this state. No standing verdict contradicted or downgraded:
frame-87-83-cede's NULL is CONFIRMED (@614 underdetermined — this battery
shows the underdetermination is structural, not just epistemic);
de-83-sweep's open adverse at @614 stands; ant-58-ending's kill untouched;
ce-le-verb-frame's fenced @611 residual extended, not disturbed.

## Fence (stated cause)

@614's subject is UNRESOLVABLE at battery grade:
(a) 58's class is open — distributionally un-noun-like (zero determiner
predecessors), verb-ending killed at @1202, and the two most informative
windows (@1695/@1756 '24-85-58') are uninterpretable pending adjudication of
the 24='en' (A3 GT) vs 24=finite-verb (ne-24-profile promote) standings
conflict;
(b) the 'celle' (47-77) fusion fails the relative-requirement (ce-le-verb-frame,
battery grade) — 87-83 follows at @611, not a relative;
(c) '[58] ... cède' fails on the intervening 'ce le', a fenced 77-residual
(ce-le-verb-frame, battery grade), with no grammatical re-segmentation under
standing values.
@614 remains an open adverse (de-83-sweep) against the 83='de' lead and an
undecided locus for the 'cède' rival (frame-87-83-cede).

## Adverses

- "coordinate with frame-87-83-cede / de-83-sweep; do not duplicate": honored.
  frame-87-83-cede's 'cède'-rival frames were not re-litigated; its NULL is
  confirmed and its @614 underdetermination given a structural cause.
  de-83-sweep's 83 census was not re-run; its open adverse at @614 is
  preserved as open. This battery answers only the delegated question
  (58's class → @614's subject).

## Follow-ups proposed (for supervisor queuing)

1. `24-en-verb-conflict` (P2) — adjudicate the standings conflict blocking
   58's classification: ne-24-profile (2026-10-08, promote: 24 = finite
   modal verb) vs en85-gerund-reaudit (2026-10-08, promote: "24-85" gerund
   frames with 24='en', A3 GT) and ant-58-ending's use of 24='en'. Bars:
   determine whether 24='en' survives at any window or 24=verb wins globally
   (§7: 67 sole polyvalence bars both); state the consequence for the five
   24-85 windows and for 58 at @1695/@1756. Red-team venue likely.
2. `02-class-609` (P3) — name 02's class at @609 ('64 39 64 02 58 47 77').
   02 follows 'qui' (64) ×2 (@609, @750), a verb-selecting slot; if 02 is a
   finite verb, 'qui [02] [58]' constrains 58 (object/complement → nominal
   signal) at the @614 locus itself. Bars: 02's class named with ≥2
   frame-legs; 58's class constrained as stated consequence. Do not
   duplicate slot-24-fence.
3. `58-noun-adjudicate` (P3) — fair distributional test of 58's noun-class
   once follow-up 1 resolves: weigh the pro-noun windows (@1202 'ce [58]',
   @1756 '[58] fois', @122 '[19] [58]') against the anti-noun evidence (zero
   determiner predecessors stream-wide; @1695/@1756 under A3 + ne-24-profile).
   Bars: promote noun-class iff 58 matches known-noun (21/26/81) distribution
   in ≥2 independent determiner/demonstrative slots with the 24-conflict
   adjudicated; kill noun-class iff any window forces non-nominal under the
   adjudicated standings.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-cede-614-subject.md` (this file).
- Queue: `cede-614-subject` queued → verdict/null via temp-file + rename,
  own entry only; pre-write assert confirmed no prior verdict; JSON
  re-validated post-write.
- Lock `cede-614-subject.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
