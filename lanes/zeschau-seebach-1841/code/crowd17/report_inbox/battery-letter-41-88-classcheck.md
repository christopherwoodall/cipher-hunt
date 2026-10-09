# Battery report — letter-41-88-classcheck

- Target id: `letter-41-88-classcheck` (priority 3)
- Claim: W2's letter arm requires 88 as a letter, but 88 stands as verb-stem (A3 frame).
- Date: 2026-10-09
- Worker: subagent letter-41-88-classcheck (session ed2acd13-befd-4a7e-9b87-c8b9fe3628e5)
- Parent evidence: battery-letter-41-dist2-tri NULL (2026-10-09): W2 @1048 fenced; 88 stands as verb-stem (A3 frame), class-incompatible with letter use.

## Bar (verbatim, from battery-queue.json)

"pass iff 88's verb-stem frame is scoped/downgraded away from @1049 AND exactly one of {frere, biere, fiere, opere, avere, acere} survives, else keep the W2 arm fenced"

## Numbered pass/fail clauses (pre-registered before testing, not modified after)

- **C1:** 88's verb-stem frame (A3) is scoped or downgraded away from @1049 by a standing verdict.
- **C2:** Exactly one of {frère, bière, fière, opère, avère, acère} survives as the @1048–1051 letter-arm word (41 word-internal).
- **C3 (else arm):** If either clause fails, keep the W2 arm fenced (fence outcome = NULL, evidentiary not terminal, per val-01-rival-sweep precedent).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing. Created
   `code/crowd17/next-token/locks/letter-41-88-classcheck.lock` on start
   (agent id + 2026-10-09T20:43:58Z); no stale lock for this target existed.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`
   (`[s[i:i+2] for i in range(o, len(s)-1, 2)]`, offsets from
   `code/side-keyhunt/repaired_offsets.json`, rows from `data/upstream-ct_R5005.txt`).
   Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005,
   sealed gate instances, and the red-team adjudication queue untouched.
3. Adopted, never re-litigated: protocol §7 standings (88 verb-stem A3;
   banked pencil GT 29="er", 40="e", 46="que"); the adverse on this target
   ("88 verb-stem frame (A3) stands; do not re-litigate at battery level");
   seg-88er-1049 PROMOTE (2026-10-09, segmentation at @1049–@1052);
   the parent battery's belt-and-suspenders rival exhaustion (adopted).

## Window-level evidence (@-offsets 0-based pair indices, byte-verified)

W2 locus: @1048=41, @1049=88, @1050=29, @1051=40, @1052=29, @1053=74, @1054=74
(row a6_04; window @1043–1056 = `63 11 67 76 85 41 88 29 40 29 74 74 45 23`).

### C1 — 88's A3 frame at @1049: FAIL (not scoped away)

The only @1049-specific standing verdict is seg-88er-1049 (PROMOTE,
2026-10-09), and it does the opposite of scoping the verb-stem frame away:

- It resolved the segmentation at @1049–@1052 as **[88 29 40] | [29 74 74]**
  (Option B): "[88]ere" is one word, forced by the banked letter values and
  the "29 40 29" trigram geometry (Option A "[88]er"+"e…" killed at kill grade
  — it forces an "eer"-initial word, unattested in 34.5M chars of period French).
- Its consistency note: "[88]ere" is consistent with finite present-tense
  shapes such as "préfère"/"adhère"/"suggère" (stem + "ère"). "The
  '88-infinitive' naming the parent anticipated is constrained AGAINST at
  this window: 88 cannot be '[88]er'-infinitive here; it is '[88]ere'."
- 88's value is not named, but 88 at @1049 remains verb-frame
  (finite-verb stem position) — the A3 frame is REINFORCED, not
  scoped/downgraded away.

A queue-wide search found no other standing verdict scoping or downgrading
88's A3 frame at @1049 (the "downgrade…88"/"A3…downgrade" report hits are
about unrelated loci). The target's adverse ("88 verb-stem frame (A3)
stands; do not re-litigate at battery level") independently bars me from
re-litigating this. C1 fails determinately.

### C2 — exactly one rival survives: FAIL

The letter arm reads @1048–1051 as `41 88 er e` = ??ère. Even hypothetically
(treating 88 as a single letter, which C1 already forbids), the parent
battery's exhaustion found six rivals: frère, bière, fière, opère, avère,
acère — and "guère" (g-u-è-r-e) is a seventh. The bar requires EXACTLY ONE
survivor; seven fail uniqueness. Adopted from the parent's
belt-and-suspenders exhaustion (not re-litigated); the guère addition is a
sanity check that changes nothing about the verdict.

Additional kill-grade block on the letter arm's segmentation: the letter arm
needs @1048–1051 as ONE word, but seg-88er-1049's forced boundary is
@1051|@1052 with [88 29 40] one word and 41 word-external at @1048. The two
segmentations are mutually exclusive; the battery-promoted one wins. C2
fails on two independent grounds.

## Per-clause pass/fail

- **C1: FAIL** — no standing verdict scopes/downgrades 88's A3 frame away
  from @1049; seg-88er-1049 PROMOTE reinforces the verb frame there.
- **C2: FAIL** — seven ??ère rivals survive (uniqueness fails); the letter
  arm's segmentation contradicts the promoted boundary.
- **C3 (else arm): FIRES** — keep the W2 arm fenced.

## Verdict

**NULL** — fence outcome per pre-registered bar (C3). The W2 letter arm
stays fenced with stated cause: (a) 88's verb-stem frame stands at @1049
(reinforced by seg-88er-1049's "[88]ere" segmentation), (b) the ??ère word
space has ≥7 rivals (uniqueness unmet), (c) the letter arm's segmentation
contradicts a battery-promoted boundary. The fence is evidentiary, not
terminal — re-openable if a future standing verdict names 88's stem value
at @1049 in a way compatible with a letter reading, or re-segments
@1048–1051. No standing or red-team verdict contradicted, downgraded, or
re-litigated. §7 intact.

## Follow-ups (per §4; all verified ABSENT from battery-queue.json — for the supervisor to queue)

1. `letter-41-1048-reseg` (P4) — Under seg-88er-1049's forced segmentation
   ([88 29 40] | [29 74 74] @1049–1054), test whether 41 at @1048 is a
   licensed standalone word immediately before the "[88]ere" verb. Bar:
   "name 41's class at @1048 with standing values and zero ungranted
   assumptions, else fence the @1048 locus as a segmentation residual."
   Rationale: decides whether the W2 locus has any licensed parse without
   the (now doubly fenced) letter arm.
2. `word-88ere-value` (P4) — Name 88's stem value in the "[88]ere" word at
   @1049–1051 (finite present-tense stem+"ère" shape, e.g. préfère/adhère/
   suggère family). Bar: "name the stem with ≤1 ungranted assumption; a
   named stem constrains the locus and feeds 88-value work." Rationale: a
   named stem would close the loop on the seg-88er-1049 segmentation.

## Scope

W2 (@1048–1051) only. 41's global tier, 88's global value/class, 74's value,
seg-88er-1049 PROMOTE, the parent NULL, the "prière" W1 lead, §7 — all
untouched. Canonical-stream caveat stands (row a6_04 offsets unvalidated).

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/letter-41-88-classcheck.lock`
  created on start (agent id + 2026-10-09T20:43:58Z), deleted on completion.
- Report: `code/crowd17/report_inbox/battery-letter-41-88-classcheck.md`
  (this file).
- Queue: target `letter-41-88-classcheck` set to status `verdict`
  (result `null`) — pre-write assert queued/verdictless, target-id-unique
  temp file `battery-queue.json.letter-41-88-classcheck.tmp` + atomic rename,
  disk re-validated, own entry only, no downgrade.
