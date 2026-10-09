# Battery report — tense-24-307 — VERDICT: NULL (fenced; §5 escalation candidate)

Worker: subagent session 045ea3a7 (seebach battery).
Date: 2026-10-09. Target: `tense-24-307` (priority 2).

## Claim

"Name 24's tense/form at @311."

## Bar (verbatim)

"une fois que" requires a completed-tense subordinate verb; "chaque fois que"
requires a habitual one. The @307 discriminator is untestable until 24 resolves.

## Bar restated as numbered clauses

- **c1:** If 24 at @311 names a completed-tense verb, then @307 (`20 17 46`) reads
  "une fois que" (or equivalent completed-tense licensing reading).
- **c2:** If 24 at @311 names a habitual-tense verb, then @307 reads
  "chaque fois que" (or equivalent habitual licensing reading).
- **c3:** 24's value (tense/form) is RESOLVED at standing grade, so the
  discriminator above is actually testable. This is the bar's own gating clause.

## Method

1. Read the bar before seeing data (copied above verbatim from
   `code/crowd17/next-token/battery-queue.json`, target `tense-24-307`).
2. Read @311 on the repaired stream
   (`code/side-keyhunt/repaired_offsets.json`; 1,847-pair parse; never
   `canonical.py`).
3. Checked battery-grade 24 values (REPORT.md finding list) and standing
   red-team verdicts on 24 (Round 18 adjudication file
   `code/crowd17/report_inbox/processed/next-token-redteam-r18.md`, controlling
   since 2026-10-09 03:13:01 UTC).

## Window-level evidence (bytes, repaired stream)

@307–@318 (row a2_04): `20 17 46 84 24 37 78 45 64 59 32`
@473–@480 (row a2_10, twin window): `06 67 46 84 24 37 78 74`

- @307 = 20 (determiner slot; 20="fois" KILLED, split 20~17 holds).
- @308 = 17 ("fois", promoted). @309 = 46 ("que", banked ground truth).
- @310 = 84 ("on", granted A15; C1–C3 conditions not independently audited here —
  fenced, not assumed).
- @311 = 24, the target. Follower: @312 = 37 (predicative frame, A1 granted).
- Byte-identical `84 24 37 78` contacts occur exactly twice: @310 and @473.
- A third `84 24` contact at @1485 (`84 24 87 08`) has a different follower —
  fenced out of the frame family, not treated as evidence.

So 24 at @311 sits in `[84=on] [24] [37=predicative]` — it is the clause's verb
candidate (subject "on" forces finiteness IF 24 is the verb), OR a non-verbal
filler (24="en" arm) that leaves the "on"-clause without any verb at all.

## Per-clause results

- **c1 — UNTESTABLE (fenced):** 24's tense/form at @311 is not named at standing
  grade. Nothing completes.
- **c2 — UNTESTABLE (fenced):** same cause.
- **c3 — FAILED AT STANDING GRADE (honest fence, not kill):** 24 is not resolved.
  Evidence:
  1. **Round 18 R18-008 (controlling):** the battery-PROMOTE of 24="faire"
     (F124, battery-disc-01-24-ci-X) was **REJECTED as a promote** and granted
     only LEAD + FINDINGS: the "unique survivor" proof is broken — the
     "laisser" kill requires a contact profile that leaves {faire, laisser}
     open. Granted instead: "24='faire' value-candidate (conditional)".
     A LEAD is not a resolved value, and it never named a tense/form at @311.
  2. **R17-009 stands:** 24=finite-verb (modal-class) is the standing red-team
     frame verdict — class-level, VALUE OPEN, tense/form un-named.
  3. **24="en" — never granted:** the "A3 ground truth 24=en" claim overstates
     the record (R18, §7 review): "A3 granted the @952 frame, not a 24 value";
     the four "confirmed" windows are the same windows standing-granted as
     24=finite-verb + R17-009. The 24="en" arm survives only as a conditioned
     lead on specific windows.
  4. **Battery grade is worse, not better:** the strongest battery-grade claim
     (F124, 24="faire") lists three live forms — finite "fait", infinitive
     "faire", participle "fait" — decided across @40/@828/@984, **never at
     @311**. Naming "24 = the verb lexeme faire" says nothing about tense or
     finiteness at @311. F127 (24=finite modal verb, class-level) is likewise
     scoped to the "qui [23/26] 37" frames (@181/@1768), not @311.
  5. Therefore c1/c2's discriminator is exactly what the bar says it is:
     untestable until 24 resolves. 24 has not resolved.

No adverse listed (adverses: null).

## Verdict

**NULL** — the bar's own gating clause fails: 24 is unresolved at standing
grade (controlling red-team state: 24="faire" promote REJECTED at R18-008,
demoted to conditional LEAD; 24=finite-verb class standing via R17-009 with
value open; 24="en" never granted). Naming a tense/form at @311 from any of
these would overstate the record; per §5 this is an honest fence with stated
cause, not a silent rewrite of the bar.

Note per protocol §5: this result does not contradict a standing red-team
verdict — it agrees with R18-008's demotion of the 24="faire" promote. No
never-downgrade conflict arises: target had no prior verdict (status queued,
verdict null).

## Follow-up targets (nulls regenerate work — 3 proposed)

1. **`tense-24-311-formclass`** (priority 2): decide FORM CLASS of 24 at @311/@473
   from the `84 24 37 78` twin windows, byte-identical. 84="on" (granted A15) is
   a subject pronoun; if 24 is the clause's verb it is forced FINITE (killing
   the infinitive/participle arms of F124 at these windows); if the 24="en" arm
   is live, the "on"-clause has no verb — test whether 1841 diplomatic French
   licenses verb-less "on en [37-predicative]" (kill-grade framing for the en
   arm at @311). Bar: 24 at @311 is finite-verb OR the en-arm dies at these
   windows; no tense named.
2. **`faire-tense-311`** (priority 3, CONDITIONAL on 24="faire" LEAD):
   if 24="faire" survives, decide between finite "fait" (which tense: present,
   passé composé, imparfait?) at @311/@473 via contact profile: @312=37 is the
   A1 predicative frame, @313=78 verb-stem-class — test whether finite "fait"
   governs `[37-predicative] [78]` ("on fait [predicative] ..."?), whether
   infinitive "faire" is licensed under subject "on", and whether participle
   "fait" has an auxiliary anywhere in the clause. 1841 diplomatic French only.
3. **`en24-311-killpack`** (priority 3): kill-grade pack for the residual
   24="en" arm AT @311: "on en [37-predicative]" with no verb in the "on"-clause
   violates French syntax (pronominal "en" requires a verb) unless a zero-verb
   reading is licensed — bar: produce a licensed parse or fence the en-arm at
   @311 kill grade. Must reckon with R17-009's standing finite-verb frame at
   the byte-identical @473 twin window.
