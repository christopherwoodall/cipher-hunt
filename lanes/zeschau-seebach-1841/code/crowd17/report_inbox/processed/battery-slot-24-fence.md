# Battery verdict: slot-24-fence

## Bar (verbatim from battery-queue.json)

"if ce-inf-1841 validates, re-test the noun-slot formulation with 33 = nominalized verb; if it fails, fence @23-24 as a 'ce' + verb contact residual and record it against 47's A4 allophone tier"

Restated as numbered clauses (pre-registered before testing):

1. IF ce-inf-1841 validates THEN re-test the noun-slot formulation with 33 = nominalized verb (conditional arm).
2. IF it fails THEN fence @23-24 as a 'ce' + verb contact residual (fail arm).
3. Record the residual against 47's A4 allophone tier.

## Method

Re-derived on the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json`
+ `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
pair count verified 1847 in-session). `canonical.py` never touched. R5005, sealed
gates, and the red-team adjudication queue untouched. Standing grants used:
47='ce' (A4, allophone tier), 33 = verb-class (ce33-noun-slot, NULL 2026-10-08),
A10 (33+29 stem/whole HOLD). The ce-inf-1841 verdict (KILL, 2026-10-09) and the
ce33-noun-slot verdict (NULL, 2026-10-08) are adopted as premises, not re-litigated.

## Evidence

**Byte-exact locus (re-derived in-session):**
- '47 33' occurs exactly x2 on the repaired stream (complete population):
  0-based @23 (row a1_00) and 0-based @1231 (row a7_01).
- @23-24 window: `53 17 64(qui) 98 82(m) 43 29(er) 47(ce) 33 55 81 00(pour) 34(i) 24 ...`
  Row a1_00, offset 0. The @23-24 in this target's bar is the 0-based pair
  index of the '47 33' contact (47@23, 33@24).
- @1231 window: `20 57 64(qui) 79(tout) 82(m) 48(e) 29(er) 47(ce) 33 29(er) 85 56 10 03 ...`
  Row a7_01. Out of this target's scope (mirrored by the already-queued
  slot-1232-fence follow-up from ce-inf-1841).

**Gate status (verified in queue):**
- `ce-inf-1841` → status verdict, result **kill**, 2026-10-09. The conditional
  arm's precondition (validation) is false. The kill report positively
  establishes: 'ce' + infinitive nominalization is ungrammatical in 1841 French
  (Littré: the substantivized infinitive takes "le"; grammars: pronoun "ce" is
  never immediately followed by a noun; demonstrative + infinitive is Old French
  only). Zero period attestations of "ce" + infinitive.
- The fail arm is therefore live, exactly as the supervisor's dispatch brief
  stated.

## Per-clause results

1. **Conditional arm (ce-inf-1841 validates → re-test noun-slot) — DOES NOT FIRE.**
   Precondition false: ce-inf-1841 returned KILL. No re-test of the noun-slot
   formulation is possible or required under the bar.
2. **Fail arm (fence @23-24 as 'ce' + verb contact residual) — FIRES / EXECUTED.**
   Under 33 = verb (standing), neither the (a) "ce [infinitif substantivé]"
   parse nor the (b) bare-pronoun-object parse is grammatical (adopted from
   ce-inf-1841's kill-grade findings). The window is unparseable via any
   'ce'-headed nominal. @23-24 is hereby fenced as a 'ce' + verb contact
   residual: the '47 33' contact is two adjacent words ('ce' + verb-class 33)
   with no licensed syntactic relation, recorded as unparsed rather than
   forced into a grammar the period does not have.
3. **Record against 47's A4 allophone tier — RECORDED.** The residual is logged
   here: at @23-24, 47's A4 'ce' value produces a word-boundary contact with
   a verb-class cell (33) that admits no grammatical 'ce'-headed nominal. The
   A4 allophone-tier grant for 47 is unaffected (the value stands); the
   residual is a contact-level annotation, not a value challenge.

## Adverses

- **"GATED on ce-inf-1841 validating - do not run before" — ANSWERED.**
  The gate is the resolution of ce-inf-1841, not its success. ce-inf-1841
  reached verdict/kill on 2026-10-09; the gate's "do not run before" condition
  is satisfied, and the fail arm (the bar's explicit consequence of the gate
  failing) is now live and executed.

## Verdict: PROMOTE

Headline: the bar's fail arm is fully executed at battery grade. ce-inf-1841
KILLED the nominalization route, so the noun-slot re-test never fires; @23-24
is fenced as a 'ce' + verb contact residual with the residual recorded against
47's A4 allophone tier. All three bar clauses pass (C1 vacuous by failed
precondition, C2 executed, C3 recorded). No new class, value, split, or
polyvalence is named or challenged. No standing or red-team verdict is
contradicted or downgraded (33 = verb-class stands; 47 = 'ce' A4 stands; A10
stands). §7 intact. Canonical-stream caveat stands. Per §4 (promote), no
follow-ups required. Re-open is red-team venue only (e.g. a future re-analysis
of '47 33' contact segmentation).

## Bookkeeping

- Lock `locks/slot-24-fence.lock` created on start (agent id + UTC), deleted on
  completion (verified gone).
- `battery-queue.json`: target `slot-24-fence` queued -> verdict/promote (own
  entry only, temp-file + rename; pre-write assert confirmed prior status was
  `queued` with no verdict — no downgrade).
- R5005, sealed gate instances, and the red-team adjudication queue untouched.
