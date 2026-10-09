# Battery verdict: val-80-1596-3sg

- Target: `val-80-1596-3sg` (battery-queue.json, priority 3, status queued)
- Claim: Name 80's value at @1596.
- Date: 2026-10-09
- Worker: battery worker (subagent db0154b1-b504-47b9-845c-0ed5dac80adf)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`; re-derived in-session: **1,847 pairs, 96 types**). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"name 80's value at @1596; a 3sg finite form licenses the infinitive-subject reading under '[03]er [80-fin]'; else fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 80's value is NAMED at @1596 — one specific lexeme selected over rivals at battery grade (≥2 independent selective legs).
2. **C2:** The named value is a 3sg finite form that licenses the infinitive-subject reading under the "[03]er [80-fin]" frame.
3. **C3 (else-arm):** If C1 cannot be met, fence the value-naming claim at @1596 with stated cause.

Adverse listed: 80's imperative/determiner split is red-team venue (poly-80-docket).

## Parentage

Follow-up #3 of the NULL `imp-80-finite-rival-1156-1596` (2026-10-09). That battery fenced the bare-verb imperative readings and found the finite-80 rival at @1596 unlicensed but not killed: "a named 3sg-finite 80 revives the infinitive-subject reading, so it stays fenced, not dead." This battery tests the revival path — naming the value. Adopted (not re-litigated): 03=verb-stem class (R19) + 29='er' pencil GT → "[03]er" is an infinitive; 67='et' at @1597 (positional rule — follower 77 is not infinitive-shaped); 77='le' provisional; 98='vient' LEAD; the right-edge coordination blocker ("[80-fin] et le [81]…" leaves "et le [81]" verb-less).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-80-1596-3sg.lock` on start (agent id + 2026-10-09T20:17:08Z); no stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Byte-confirmed the locus (0-based): `@1593=81 @1594=03 @1595=29 @1596=80 @1597=67 @1598=77 @1599=81 @1600=82 @1601=98` (row a8_02) = "…[81] [03]er [80] et le [81] m vient…".
4. Census of 80: n=17 (loci 441, 469, 517, 565, 663, 673, 720, 768, 1011, 1032, 1090, 1156, 1295, 1322, 1596, 1662, 1808). The `03 29 80` trigram is exactly 3× stream-wide (@1032/@1322/@1596).
5. Adopted standing findings: 80's value OPEN, absent from registry, zero promoted values queue-wide (80-value-host-w2); infinitive value fenced as locus-bound (val-80-768-inf); seven naming routes failed at @1322 (80-value-host-w2 NULL).

## Window-level evidence

### C1 — name the value: FAIL

Tested whether any 3sg finite candidate is SELECTED (not merely parsed) by the @1596 frame under standing values. Candidates: est, dit, peut, doit, veut, vaut, semble, reste.

- The frame "[03]er [80] et le [81] m vient" supplies zero selectional pressure: no agreement controller beyond 3sg, no object, no complement, no tense adverbial. Every candidate parses the frame identically. Per the val-03-value-census precedent (adopted by stem-85-value-rerun): **parsing ≠ naming**. Zero selective legs for any candidate.
- The two sibling `03 29 80` windows (@1032 "@1032 [03]er [80] le la pre", @1322 "[03]er [80] t [62] vient") are equally nondiscriminating — and @1322's seven-route naming attempt already failed (80-value-host-w2 NULL).
- Corpus-frequency reasoning ("est" is the commonest infinitive-subject predicate) cannot name at battery grade: 1690-frequency uniformity is necessary but insufficient, and 80's registry is null with zero promoted values.
- **C1: FAIL.** 80's value is unnameable at @1596 at battery grade.

### C2 — 3sg finite licenses the reading: MOOT

Without a named value there is nothing to license. Recorded for completeness: the parent battery's right-edge blocker stands — "[80-fin] et le [81]…" leaves "et le [81]" verb-less with no coordination license. A named finite value would still need that blocker resolved.

### C3 — fence: FIRES

80's value-naming at @1596 is **fenced**: the frame admits every 3sg finite candidate identically, and no independent standing constraint selects one. This is a battery-grade fence (evidentiary, re-openable when 03's value, 81's class, or a second selective leg is banked), not a kill — the finite-80 revival path itself stays fenced per the parent battery.

## Scope

- Fences only the value-naming claim at @1596. Untouched: the parent battery's fenced finite-80 reading (revival-possible), 80's A8 verb-frame, the imperative arm (R19-120 W1, conditional on provisional 77='le'), the determiner arm (R19-120 W2 "[80] fois" @1156), the poly-80-docket split question (red-team venue — the listed adverse), §7. No standing or red-team verdict contradicted or downgraded.
- Canonical-stream caveat stands (row a8_02 offsets unvalidated).

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json, 2026-10-09)

Not duplicated: `val-80-469-stem`, `80-inf-transfer-1322`, `wordint-80-08-unit` (all already queued via 80-value-host-w2).

1. **`imp-80-1596-coord`** (P4) — resolve the right-edge coordination blocker for finite-80 at @1596: name 81's class at @1599 ("et le [81] m vient") or fence the coordination rescue terminally; a licensed "et" re-opens the finite-80 revival path. Evidence: this report (C2). Adverses: 81 class-open.
2. **`val-03-1594-frame`** (P4) — name 03's value at @1594; the infinitive-subject's identity selectionally constrains the finite predicate (e.g. "vouloir" vs "dire" subjects admit different 3sg predicates). Evidence: this report (C1 nondiscrimination). Adverses: none.
3. **`kill-80-finite-cands`** (P4) — corpus census of bare-infinitive-subject + 3sg finite verb constructions in 1841 French; kills candidates with zero attestations in the construction. Frequency cannot name, but absence can kill. Evidence: this report (candidate set). Adverses: none.

## Verdict: NULL (fence executed)

C1 fails (no selective legs — parsing ≠ naming), C2 moot, C3 fires. 80's value is unnameable at @1596 at battery grade; the finite-80 revival path remains fenced, not killed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-80-1596-3sg.md`
- Queue: `val-80-1596-3sg` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-80-1596-3sg.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/val-80-1596-3sg.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
