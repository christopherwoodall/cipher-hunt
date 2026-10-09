# Battery verdict: redteam-gate-trigger-input

- Target: `redteam-gate-trigger-input` (battery-queue.json, priority 2, status queued)
- Claim: "evidence package recommending gate triggers require red-team ratification of the gating value, not a battery promote alone"
- Date: 2026-10-09

## Bar tested (verbatim, pre-registered)

"evidence package for red-team adjudication; gather-only, no battery decision"

→ C1 (package delivered) — see below / C2 (no adjudication) — this report makes no ruling; it packages evidence and proposes rule text for the red team to adopt or reject.

Adverses (verbatim): "red-team venue: batteries do not decide red-team docket items" — honored: no §7 declaration, no registry change, no verdict on any red-team docket item.

## Verdict: NULL (gather-only package delivered)

## Package contents: the gate-trigger rule and six evidentiary cases

### Recommended rule text (for red-team ratification, not a battery decision)

> A gated battery target fires only when the **specific event named by its bar** has occurred at the level the bar names. The trigger must be checked against the latest red-team round report, not against battery verdicts alone:
>
> 1. A battery promote that the red team rejected, downgraded, or has not ratified does **not** satisfy the trigger.
> 2. A battery NULL that names nothing does **not** satisfy "once X names a value."
> 3. Battery leg-gains that fall short of naming the gating value do **not** satisfy a value-naming trigger.
> 4. A red-team meta note describing a shape (e.g. "X is Y-shaped") is **not** the same as naming X with a Y-compatible class; the bar's named event is what must occur.
>
> The supervisor/hook must independently audit every gate suggestion before spawning, even when triage labels it "satisfied."

### Case A — ne-508-reseg-gate62 (62='il' gate; trigger can never fire)

- Hook triaged the gate "satisfied" when a battery promoted 62='il'.
- Red-team standing: 62='il' **REJECTED at R19-097/R19-106**, confirmed **killed at kill grade at R20-125** ("The conditioned 'il' lead stays REJECTED"; R20-230: "62='il' is KILLED at kill grade (R19-106)").
- The worker correctly refused; queue entry `ne-508-reseg-gate62` = verdict/null.
- Lesson: a battery promote the red team rejected does not satisfy the gate — here the trigger can never fire.

### Case B — verdict78-gate-wordbound-rearm (78='ver' gate; leg-gains ≠ value promote)

- Hook triaged "gate satisfied" on battery ver-78 leg-gains.
- The returns were leg-gains, not a value promote. 78='ver' is **DEFERRED with cause** (R20-284 carry-forward; R16-005 LEAD stands).
- The worker correctly refused; queue entry = verdict/null.
- Lesson: red-team *resolution* of the gating value is the trigger; battery leg-gains are not.

### Case C — adj-32-inflect-gate (NULL names nothing)

- Dispatched even though the parent battery `adj-32` returned NULL and named no value.
- The worker correctly refused and returned NULL (report: battery-adj-32-inflect-gate.md, C1 gate trigger recorded as unsatisfied).
- Lesson: a NULL that names nothing does not satisfy "once X names a value." The verdict's existence is not the named event.

### Case D — lon-77-le-gate-rerun (downgraded promote ≠ trigger)

- Returned NULL because R20's FENCE/provisional survival of 77='le' was neither merge nor overturn.
- Lesson: a battery promote that was downgraded (cf. det-87-644-function, Case F) does not satisfy the trigger.

### Case E — pour66-class-rerun (2026-10-09; meta note ≠ named event)

- Bar: "confirm-or-reject the 4→2 at @244 **iff 66 is named with an INF-compatible class**."
- Hook claimed the gate SATISFIED at red-team level, citing an R20 meta note that "66=infinitive-shaped."
- The note (R20, W0-frame discussion, ~line 968) lists "66=infinitive-shaped" as a *premise* of a weak leg and explicitly says "the battery names all three as **re-open conditions**" — i.e. naming 66 is the outstanding condition, not the occurred event.
- Supervisor held the target (still queued, undispatched). 66 remains un-named at battery and red-team grade.
- Lesson: a red-team meta note describing a shape is not the bar's named event. This is the same failure pattern as Cases A–D, applied to notes rather than verdicts.

### Case F — val-61-645-det (2026-10-09; downgraded promote ≠ trigger)

- Bar: "name 61's class at @645 under the **now-promoted determiner-87**."
- det-87-644-function's PROMOTE was **DOWNGRADED to FENCE by R19-138**, confirmed **R20-091** ("DUPLICATE / CONFIRM R19-138 (FENCE stands)").
- Supervisor held the target (still queued, undispatched).
- Lesson: "now-promoted" is false at the current standing; the premise does not hold.

### Pipeline flags (noted for supervisor, not acted on)

1. R20-091 carries a pipeline flag: the queue entry for `det-87-644-function` still shows result: promote against the standing R19-138 FENCE — coordinator to reconcile.
2. `ne-508-reseg-gate62` and `verdict78-gate-wordbound-rearm` are already verdict/null (correctly refused) — no regression action needed; do not re-dispatch on the same triggers.

## Scope

Gather-only. No bankable content added beyond the record. No standing or red-team verdict contradicted, downgraded, re-litigated, or declared. §7 intact. Canonical-stream caveat stands (repaired 1,847-pair / 96-type stream used throughout; `canonical.py` never used). R5005, sealed gate instances, and the red-team adjudication queue untouched.

Per the gather-only precedent (R19-182; battery-redteam-tonic-fence-input; battery-split-03-redteam-feed), no follow-up targets are proposed — all further battery work on gated targets is blocked until the red team adjudicates the rule and the deferred docket items.

## Bookkeeping

- Lock `locks/redteam-gate-trigger-input.lock`: created on start (agent 4c1579a6-b526-49e6-beaa-c7f11606e376, 2026-10-09T20:02:11Z, no stale lock), deleted on completion (verified gone).
- Queue: `redteam-gate-trigger-input` queued → verdict/null 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.redteam-gate-trigger-input.tmp` + rename; disk re-validated; own entry only; no downgrade).
