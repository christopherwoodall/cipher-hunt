# Battery report: noun26-89-class

- Target id: `noun26-89-class`
- Claim: "adjudicate 89's class (noun vs infinitive vs word-internal); unblocks @1753"
- Date: 2026-10-09
- Worker: battery worker (subagent c69eb0cb-8178-4540-9164-e4832c36d2bb)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets are 0-based repaired-stream indices.
  `canonical.py` never used. R5005 not touched.
- Lock: code/crowd17/next-token/locks/noun26-89-class.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"state 89's class (n=14) by adjudicating noun ('77 89' x2 @639/@870, load-bearing on provisional 77='le') vs infinitive ('24 89' x3 @222/@986/@1498, load-bearing on promoted 24=modal) vs word-internal ('[X]er [89]' x3 @275/@1377/@1393) — stated class or fenced split"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) One uniform class is named only if all 14 windows parse under it with
   <=10% orphan (the lane's standard for naming).
2. (C2) Failing C1, the split is fenced: each arm's windows are enumerated with
   their conditions, and any irreducible arm-vs-arm collision is stated.
3. (C3) No polyvalence is declared at battery level (§7: 67 et/veut remains the
   sole true polyvalence); the fence is evidence for the red-team docket only.

## Method

1. Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types.
   Never used canonical.py. R5005 not touched.
2. Census: n(89) = 14, 0-based indices
   [113, 222, 275, 285, 303, 640, 781, 871, 986, 1082, 1377, 1393, 1498, 1752].
3. Tested noun / infinitive / word-internal at each window against standing
   values: 29='er' (banked), 24=finite modal (promoted class), 77='le'
   (provisional), 64='qui' (granted), 87='ce' (granted).

## Window-level evidence

### Arm A — noun ('77 89' x2, conditional on provisional 77='le')

- @640 (a4_01): `60 67 77 89 48 20 24` — "le [89] e [20] [24]" = "le [89]e",
  determiner + noun with -e ending. Noun forced here (an infinitive after an
  article is ungrammatical in 1841 French). Conditional on provisional 77='le'.
- @871 (a5_07): `70 87 77 89 48 20 74` — "le [89] e [20]" — same shape, noun
  forced, same condition.
- @1752 (a8_08): `34 07 28 89 26 24 85` — "28 [89] [26] [24-modal]"; 89 as
  subject of the finite modal. Conditional noun leg #3 (the @1753 residual
  "89 26 24" parses under noun-89; cf. noun26-residual-adjud NULL).

### Arm B — infinitive ('24 89' x3, load-bearing on promoted 24=modal)

- @222 (a2_01): `42 16 24 89 61 96 87` — "[24-modal] [89]" = modal + infinitive.
  Clean; a noun here would need to be a direct object of a modal (ungrammatical).
- @986 (a6_01): `45 01 24 89 48 01 76` — "[24-modal] [89] e"; 89 as infinitive
  with word-internal 89-48 = "[89]e" (-re-shaped infinitive). Clean.
- @1498 (a7_11): `15 59 24 89 41 74 84` — "[24-modal] [89]"; modal + infinitive.
  Clean.

### Arm C — word-internal ('[X]er [89]')

- @275 (a2_03): `67 33 29 89 84 91 37` — "[33]er [89]"; 89 as governed
  infinitive (French permits infinitive-on-infinitive government,
  "aller faire"-shaped) OR word-internal composition.
- @1377 (a7_06): `00 86 29 89 84 92 69` — "[86]er [89]"; same duality.
- @1393 (a7_07): `67 86 29 89 16 76 47` — "[86]er [89]"; same duality.
- @113 (a1_03): `67 93 29 89 68 21 67` — "[93]er [89]"; same duality.
- @781 (a5_04): `37 08 29 89 11 24 42` — "[08]er [89]"; 08 open, same duality.
- Word-internal vs governed-infinitive at these 5 windows is not decidable
  at battery grade: no window forces one, no syllabary-uniformity test was
  run. Fenced as a sub-question (follow-up 2).

### Open windows (arm-neutral)

- @285 (a2_03): `42 48 52 89 28` — "52 [89]"; 52/28 open, no forcing evidence.
- @303 (a2_04): `86 91 18 89 88` — "18 [89] 88"; 18/88 open, no forcing evidence.
- @1082 (a6_05): `64 06 52 89 24` — "52 [89] [24-modal]"; compatible with both
  arms (infinitive + modal frame needs 52's class; noun + modal frame ungrammatical
  without a boundary).

## Per-clause pass/fail

1. **C1 FAIL** — no uniform class. Uniform-infinitive is killed at the 2 noun
   windows (an infinitive after "le" is ungrammatical; both kill-grade under
   provisional 77='le'). Uniform-noun is killed at @222 (a noun cannot be the
   direct object of the promoted finite modal 24). Uniform word-internal was
   not demonstrated at any window.
2. **C2 PASS** — split fenced with conditions stated:
   - noun: @640, @871 (forced), @1752 (conditional leg) — all conditional on
     provisional 77='le'; if 77 is not 'le', Arm A dies (follow-up 1).
   - infinitive: @222, @986, @1498 (forced), plus @275/@1377/@1393/@113/@781
     as governed-infinitive-or-word-internal (sub-question fenced).
   - The arm-vs-arm collision is irreducible on current grants: noun-arm needs
     77='le' + 24=modal to both hold in different windows — a conditioned
     two-way split, not a uniform class.
3. **C3 PASS** — no polyvalence declared. This fence is battery-grade evidence
   for the red-team docket; §7's sole-polyvalence standing (67 et/veut) is
   untouched.

## Verdict: PROMOTE (finding grade — fenced split recorded; battery-grade, needs red-team ratification)

89 takes a **conditioned split**: noun at the '77 89' windows, infinitive at
the '24 89' windows (with the '[X]er 89' family fenced between
governed-infinitive and word-internal). The noun arm is conditional on
provisional 77='le'; the infinitive arm is load-bearing on the promoted
24=modal class. No uniform class is nameable; no value was named or
re-litigated.

## Adverses answered

- "89's value open (not re-litigated)" — no value was named anywhere in this
  battery; the adjudication is class-level only.
- "77='le' provisional" — stated as the explicit load-bearing condition on
  Arm A, not hidden.
- "do not declare polyvalence (§7)" — none declared; the fence is evidence
  for red-team adjudication, not a polyvalence claim.

## Follow-up targets (for supervisor queuing)

1. **89-noun-locus-rerun** (priority 3): re-test Arm A iff 77's value ever
   resolves non-'le' or 77='le' promotes; kill the noun arm iff "le [89]e"
   fails under the new value.
2. **er89-wordinternal-govern** (priority 3): adjudicate word-internal vs
   governed-infinitive at @275/@1377/@1393/@113/@781 with a syllabary
   uniformity test; kill one fork.
3. **poly-89-redteam-package** (priority 3): structured evidence package for
   the red-team poly-89 docket (this fence + value-open 89), with the
   conditioning hypotheses and their load-bearing grants.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-noun26-89-class.md
- Queue: `battery-queue.json` → `noun26-89-class` status `verdict`,
  result `promote`, date 2026-10-09 (pre-write assert passed —
  was `queued`/verdictless; temp-file + rename; JSON re-validated; only
  this entry touched).
- Lock created on start, deleted on completion (verified gone).
- No standing or red-team verdict contradicted or downgraded; §7 intact;
  R5005, sealed gates, red-team adjudication queue untouched.
