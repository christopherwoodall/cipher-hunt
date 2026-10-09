# Battery verdict: verb-91-277-frame

- Target: `verb-91-277-frame` (battery-queue.json, priority 3, status queued)
- Claim: name 91's class at the @277 'on [91]' window (finite-verb vs adverb test).
- Evidence (queue): optional follow-up of ant-91-36-noun KILL (2026-10-09): @277 (a2_03)
  '33 29 89 84 91 37 61 20 61' puts 91 directly after granted 'on' (84, A15) -
  'on' + bare noun is ungrammatical, a kill-grade contradiction capping the
  noun-class claim.

## Bar (verbatim)

"91's class named at battery grade with finite-verb vs adverb decided; else fence
with stated cause."

## Bar restated (numbered, pre-registered)

- C1. 91's class is NAMED at battery grade at the @277 'on [91]' window.
- C2. The finite-verb vs adverb fork is DECIDED: one arm licensed, the other
  fenced with stated cause.
- C3. Else-arm: if C1 or C2 fails, fence the locus with stated cause. (moot if
  C1 and C2 pass)

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/verb-91-277-frame.lock` on
   start (agent d1c77618-a292-476e-9a2d-0e6c721206d0, 2026-10-09T20:17:00Z).
2. Re-derived the repaired stream in-session from
   `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
   via `repair_parse.py` logic: 1,847 pairs, 96 types; asserts held.
   `canonical.py` never used.
3. Byte-confirmed the locus (0-based @277, row a2_03):
   @273=33 @274=29('er', pencil GT) @275=89 @276=84('on', A15 granted)
   @277=91 @278=37 @279=61 @280=20 @281=61 @282=42 @283=48('e', letter tier).
4. "84 91" bigram is exactly 1x stream-wide (@276-277).
5. Adopted (not re-litigated):
   - 84='on' A15 GRANT (round-15 A15; weakened round-16 on the 'on est' legs;
     conditional per R20-003). Conditions: C1 (77='le' provisional, the 'le 84'
     legs) — @276 is preceded by 89, not 77, so C1 is irrelevant here;
     C2 (62/84 'on' collision) — resolved: 84='on' holds unconditioned
     (battery-collision-62-84; 62='on' unconditioned killed); C3 (fenced
     residuals @1619 'la on', @1664 'ne on') — @277 is neither.
   - ant-91-36-noun KILL: 91 is not noun-class at battery grade; 'on' + bare
     noun is ungrammatical at kill grade.
   - val-91-pp-adj PROMOTE (locus-level): 91 = past participle at the two
     16-91 windows (0-based @537-538, @1370-1371), R19-164. Verified in-session:
     '16 91' bigram is exactly 2x stream-wide.
   - 91's adjective reading fenced lane-wide for lack of a second independent
     leg (adj-91-723-second-leg fence; @723 leg stands conditional).

## Findings

### C1 — finite-verb class named: PASS

The frame 'on [91]' is structurally verb-forcing at battery grade. 84='on' is
the subject pronoun (A15 grant; all three conditions hold/clear at @277 as
shown above). French grammar requires a finite verb after a subject pronoun.
The frame therefore licenses 91 as FINITE VERB at battery grade with ZERO
ungranted assumptions. Class named (class-level, value open): no single verb
value is selectable — any finite verb parses identically here, and naming one
would be arbitrary (precedent: masc-noun-86-name, stem-86-29-value,
stem-26-nent-verb).

### C2 — adverb arm fenced with stated cause: PASS

The adverb reading of 91 at @277 fails at battery grade:

- F1 (ungrammatical as written): 'on' + bare adverb is ungrammatical French.
  An adverb cannot host a subject pronoun. This is the same kill-grade
  mechanism as the adopted noun-capping ('on' + bare noun).
- F2 (the only rescue needs two ungranted assumptions): 'on [91-adv]
  [37-verb]' would require BOTH 91=adverb (class-open, ungranted) AND
  37=finite verb (37 is a predicative-frame cell, value open per A1;
  class-open per val-24-1132). A forced zero-assumption structural license
  (C1) beats a possible two-assumption composition at battery grade.
  The rescue stays a conditional future, not a battery-grade finding.

The finite-verb vs adverb fork is decided: finite-verb arm licensed,
adverb arm fenced.

### F3 — the past-participle tension (scope, not a contradiction)

val-91-pp-adj's promote is LOCUS-LEVEL at @538/@1371 (16-91 windows) and does
not contradict a locus-level finite-verb naming at @277. But the two readings
are mutually exclusive under single-form uniformity: 91 = past participle
(non-finite) at the 16-91 windows vs 91 = finite verb at @277. This is the
classic section-7 conditioned-split shape (parallel to the 74 verb/noun
package and the 86 stem/prefix package). Recorded here as red-team input;
no split is declared by this battery.

## Verdict: PROMOTE

- C1 PASS: 91 = finite-verb class at @277 (locus-level), value open.
- C2 PASS: the adverb arm is fenced (F1 ungrammatical-as-written; F2 rescue
  needs two ungranted assumptions).
- C3 moot.
- The 16-91 past-participle vs @277 finite-verb split shape is packaged in
  this report for the section-7 red-team venue.

## Scope

- Names only the class at @277. No value named; no polyvalence declared;
  section 7 intact.
- Untouched: val-91-pp-adj's locus-level PP at @538/@1371; adj-91-723-03-gate's
  conditional @723 leg; ant-91-36-noun's lane-wide noun KILL; the A15 grant
  and its conditions; all standing/red-team verdicts (no contradiction,
  no downgrade).
- Out of scope: the @1668 '06 91' window ('qui ent [91] la le …') — a different
  frame, not tested here.
- Canonical-stream caveat stands (row a2_03 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-verb-91-277-frame.md`
- Queue: `verb-91-277-frame` queued -> `verdict`/`promote`, 2026-10-09
  (pre-write assert passed - was queued/verdictless; target-id-unique tmp
  `battery-queue.json.verb-91-277-frame.tmp` + atomic rename; disk
  re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/verb-91-277-frame.lock`: created on start, deleted on completion
  (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
