# Battery report: slot-60-at-197

- Target id: `slot-60-at-197`
- Claim: "name 60's slot at the free (non-formula) 21-60 window @196–197"
- Date: 2026-10-09
- Worker: battery worker (subagent 576796bd-7663-4e1e-b096-320d8e0e676f)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py;
  1,847 pairs / 96 types asserted in-work. `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched. @-offsets are
  1-based repaired-stream pair indices (queue convention).
- Lock: code/crowd17/next-token/locks/slot-60-at-197.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"resolve iff exactly one of verb/adjective/infinitive parses @194-200 with 21
nominal and <=1 unstated assumption; coordinate with verb-60 and
poly-60-redteam without duplicating their bars; if polyvalence-gated, fence
with stated cause"

Numbered pass/fail clauses (fixed before data examination):

1. (C1) Exactly one of {60=finite verb, 60=adjective, 60=infinitive} parses
   the window @194–200 (1-based) with 21 nominal and ≤1 unstated assumption;
   the other two arms fail at kill grade or exceed the assumption gate.
2. (C2) Coordination: verb-60's and poly-60-redteam's conclusions are adopted
   as premises; neither bar is duplicated (verb-60 covered only its six
   windows; poly-60-redteam stays queued, untouched).
3. (C3) Polyvalence gate: no polyvalence is declared at battery level per §7;
   if the window forces a polyvalent reading, fence with stated cause instead
   of resolving.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types; asserts
   held); never touched canonical.py/R5005.
2. Extracted @194–200 (1-based) byte-exact: `56 47 01 21 60 08 67`
   (row a2_00; ±8 context: `24 87 98 | 56 47 01 21 60 08 67 | 76 87 11 92 63 42`).
3. Censused all four "21 60" bigrams stream-wide (@119, @172, @197, @232)
   for consistency only — the bar scopes to @197.
4. Tested the three arms against standing values (grants/promotes from
   BATTERY-PROTOCOL §7 plus battery-verdict premises listed below), counting
   every class/value not covered by a verdict as an unstated assumption.

## Standing premises (adopted, not re-litigated)

- 47='ce' granted (A4 allophone tier); 21 noun-CLASS battery-promoted
  (de-frame-21-class); 76 noun-class battery-promoted (noun-76).
- 98='vient', finite clause-head verb, clause-terminal at @193: 98's selected
  complements are {83, 00, 82} (battery-boundary-98-839 PROMOTE, 2026-10-09);
  follower @194=56 ∉ inventory → clause break 98→56. New clause starts at 56.
- 67 positional rule (§7): 67='veut' iff follower infinitive-shaped;
  follower @201=76 is nominal → 67='et'.
- 60 verbal class forced at verb-60's V1 ('qui 60 08' @1338), V2 ('ne 60 12'
  @700), V4 ('53 60 06' @1474); noun-60 killed; adj-60's uniform-adjective
  claim killed. verb-60's own note: @197 ('21 60 08 67') is "same verb+08
  frame" as V1, value unnamed.
- 56 is whole-word (stem-56-whole PROMOTE, 2026-10-09); its noun/verb class
  split is red-team venue — no class selected here.
- 01's class is open (no class verdict; 01 modal-verb killed only at the
  @1028–1031 locus per ce01-slot-1029-infinitive-avenue; 01='-ci' fusion
  killed there too — not used here).
- 08's class open (stem-08 NULL); 08 is not verb-shaped ('08 31' x3,
  per stem-08 evidence cited in verb-60) — 08=verb is contradicted.

## Window-level evidence

Window (1-based): @194=56 @195=47 @196=01 @197=21 @198=60 @199=08 @200=67.

### Arm (a): 60 = finite verb — PARSES (the unique survivor)

Parse: new clause `[56] ce [01] [21-N] [60-V] [08] et [76-N]`.

- Subject NP "ce [01] [21]": 47='ce' granted; 21 nominal is the bar's own
  premise (class promoted); 01 must be determiner/adjective class to complete
  the NP — **the single unstated assumption** (1 of ≤1). It is the ONLY
  01-window stream-wide with the det-01-noun shape (censused n(01)=28), so it
  is a hapax slot: no distributional support, but no standing verdict kills
  it either (01's class genuinely open; no det/adj-01 kill exists).
- 60-V: subject present (21-N); geometry is byte-identical to verb-60's V1
  ('qui 60 08' → '[21-N] 60 08'), the verb+08 frame verb-60 itself flagged as
  the @197 twin. Right edge 08 = fenced complement (08 open, not assumed);
  "et [76]" = clean conjunction + nominal per the §7 positional rule and
  noun-76.
- Zero kill-grade contradictions: 21-as-subject is class-licensed; 60-verbal
  is class-forced elsewhere and uncontradicted here; "ce [01] [21] [60]"
  needs no archaism, no word-order violation, no clause-boundary invention.
- 56: fenced as a clause-initial residual with stated cause (whole-word
  status promoted; noun/verb split red-team venue; selecting a class would be
  a second unstated assumption). The residual is at the clause edge, not
  inside the "ce [01] [21] [60]" core.

Assumption count: **1** (01 = determiner/adjective). Within the bar's gate.

### Arm (b): 60 = postnominal adjective — FAILS the assumption gate

"ce [01] [21-N] [60-adj]" is a grammatical NP only if some OTHER group is
the clause's finite verb. Candidates:

- 56 as verb: needs 56=verb (assumption 1 — 56's noun/verb split is
  red-team venue; the w5-pas-verb window verdict at @1732 does not license
  a class selection at @194) AND 01=det/adj (assumption 2) = 2 assumptions.
- 08 as verb: contradicted at battery grade (08 not verb-shaped); also needs
  56 nominal + 01 det/adj = ≥2 assumptions.
- No other finite-verb candidate exists in the window.

**2+ unstated assumptions required → exceeds the ≤1 gate → arm (b) fails.**
(Consistent with adj-60's kill of the uniform-adjective claim; this window
is not an adjective refuge.)

### Arm (c): 60 = infinitive — FAILS (no governor)

An infinitive needs a preposition/modal governor. Left edge is
"ce [01] [21]" (no preposition/modal); selecting 56 as a modal/preposition
is assumption 1 plus 01=det/adj assumption 2, and 56 has no
modal/preposition profile anywhere. Alternatively "ce" governing an
infinitive is ungrammatical. **Fails at kill grade (governorless); the
rescued form needs 2 assumptions anyway.**

### Consistency (not a claim)

The other three "21 60" bigrams do not contradict 60=verb: @172
('12 48 21 60 09' = "e [21-N] [60-V] [09]") parses verb-clean; @119
('14 21 60 90') and @232 ('21 60 71', the vient-parvenir formula window,
owned by queued frame-vient-parvenir) are class-compatible.

## Per-clause pass/fail

- C1: **PASS.** Exactly one arm — 60=finite verb — parses @194–200 with 21
  nominal and ≤1 unstated assumption (01 = determiner/adjective). The
  adjective arm needs 2 assumptions; the infinitive arm is governorless.
- C2: **PASS.** verb-60's verdicts adopted as premises (V1/V2/V4 verb
  forcing; the @197 twin note CONFIRMED at battery grade by this result);
  verb-60's six-window bar not re-run. poly-60-redteam (queued pri 1)
  untouched — this result feeds it a 7th bare-verb window; no duplication.
- C3: **PASS.** No polyvalence declared or needed (§7 intact); the window
  resolves on a single class, so the fence branch does not fire.

## Adverses answered

- "polyvalence is red-team-only per §7": honored — the resolution is
  single-class (verb); the noun/verb split on 56 is left for the red team
  (56 fenced, not classed).
- "coordinate with verb-60 and poly-60-redteam without duplicating their
  bars": done — verb-60's frame adopted, poly-60-redteam's docket untouched.

## Caveats

1. Row a2_00's upstream offset is one of the 68 unvalidated offsets
   (canonicality caveat): under a rival row phase this window could
   re-segment, dissolving the result. Canonical-stream verdict per protocol.
2. The single assumption (01 = determiner/adjective) is a hapax slot with no
   distributional support; it is unstated but not contradicted.
3. 56 is a fenced clause-initial residual, not parsed.
4. 60's VALUE is unnamed (consistent with verb-60's null: V1–V4 value-open);
   this is a slot verdict, not a value verdict. Pending red-team ratification.

## Follow-ups

None required (promote, not null). Suggested for the supervisor's
consideration: `det-01-slot` (P3) — test the determiner/adjective arm for 01
across its 28 windows now that @196 is the sole det-01-noun slot.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-slot-60-at-197.md (this file)
- Queue: `slot-60-at-197` → status `verdict`, result `promote`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion.
- `canonical.py` never used; R5005, sealed gates, red-team adjudication
  queue untouched; no standing or red-team verdict contradicted or
  downgraded; §7 intact.
