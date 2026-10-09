# Battery verdict: pour1544-post-adjudication-rerun

Target: `pour1544-post-adjudication-rerun` (battery-queue.json, priority 3, status queued).
Worker: cf95c777-7995-4a35-ae0c-85f2ee5351d3. Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/pour1544-post-adjudication-rerun.lock` created on start (no prior lock, no stale-lock note needed).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

> "record the adjudicated @1544 survivor set and the census's terminal claim verdict (promote/kill) with no new grammaticality litigation."

Numbered clauses:
1. C1 — record the adjudicated @1544 survivor set (from frame-43-pour-que-1544's verdict).
2. C2 — record the census's terminal claim verdict: promote or kill. No new grammaticality litigation.

## Method

Adoption only, per protocol §5 (never downgrade an existing verdict) and the bar's "no new grammaticality litigation" constraint. This re-run performs no fresh window tests: it applies the adjudication report's verdict to the census's C2. Byte anchor re-verified in-session on the repaired 1,847-pair / 96-type stream (asserts held; `canonical.py` never used):

`@1543 78 | @1544 43 | @1545 00 | @1546 46 | @1547 70 | @1548 12 | @1549 94 | @1550 92`

Matches frame-43-pour-que-1544's corrected anchor exactly ("43 pour que [70-prenne]" spans @1544..1549).

## Findings

**The adjudication (adopted wholesale, not re-litigated):** `battery-frame-43-pour-que-1544` (2026-10-09, verdict NULL — "the frame is a dead discriminator at battery level"):

- Clause (a) 43 named: FAIL. The discriminator's positive set within French feminine nouns is {condition, mesure} (suite/manière already killed: noun-43-discriminator KILL). Both members dead at battery grade on independent windows: cond-mesure-43full (NULL, survivor set EMPTY — condition and mesure fail par-43 x2 @343/@1027 and @21 at kill grade) + par43-adverbial-attestation (PROMOTE on negative arm — bare "par mesure"/"par condition" unattested as 1841 adverbials; terminal closure pending only the @21 polyvalence ruling, red-team docket).
- Clause (b) 78's slot: ANSWERED (determiner-headed nominal, not verb-like). 78's slot is nominal under any ver-shaped value; the "verb like faire" reading excluded by shape.
- Clause (c) prenne-battery consistency: CONSISTENT. The clause is genuinely subjectless (prenne-subject-S1545 PROMOTE), anomalous not conventional.
- Adverse 1 sharpened: the government reading has ZERO constructional support stream-wide — no "pour que" window is noun-governed (@106 left=28 unknown, @545 left=06 verb-ending, @1680 left=44 unknown).

**Adjudicated @1544 survivor set (C1 of this re-run's bar):**

- Government reading ("[43] pour que [subj]"): frame-local {condition, mesure} — both globally dead at battery grade on independent windows (cond-mesure-43full kill grade + par43-adverbial-attestation terminal closure). Effective survivor set: **{}**.
- Boundary reading ("...78 43. Pour que prenne 92..."): frame-local {suite, condition, maniere, mesure} — suite/maniere globally killed (noun-43-discriminator KILL) → {condition, mesure} → both globally dead → effective **{}**.

Under EITHER reading, @1544's survivor set is empty at battery grade. The 4 -> 2 discrimination the census's C2 recorded is moot: the "2" do not survive anywhere, so there is no positive set left for the window to discriminate.

**The census's terminal claim verdict (C2 of this re-run's bar): KILL.**

The census's C2 claim — "the discrimination reads 4 -> 2 under the government reading" — is falsified at battery grade. The surviving pair is dead on independent windows, so @1544 cannot serve as the pour-frame discriminator. Per the follow-up spec ("if boundary, @1544 drops out of the census permanently"), @1544 drops out of the census permanently — and here on stronger grounds than the boundary case alone: the window is a dead discriminator under BOTH readings.

**Census terminal state after this re-run:**

- @1126: 4 -> 2 (frame-local, C1 PASS — stands).
- @1544: DROPPED from the census permanently (this verdict).
- @244: fenced, pending pour66-class-rerun (C3 fence stands; the gate "iff 66 is named with an INF-compatible class" is UNFIRED — 66 not named at battery or red-team grade; no re-run triggered by this report).
- @439: 4 -> 4, non-discriminating (C4 recorded — stands).

No standing or red-team verdict contradicted or downgraded: noun-43-discriminator's kills stand; cond-mesure-43full's empty global survivor set stands; par43-adverbial-attestation's promote stands; the @21 polyvalence caveat stays red-team venue. §7 intact. R5005, sealed gates, red-team adjudication queue untouched.

## Verdict: KILL

The @1544 discrimination arm of the frame-43-pour-census is dead at battery grade: the adjudicated survivor set is empty under both the government and boundary readings. @1544 is permanently out of the census. (Kill, not null — no follow-ups required; the @244 arm already has its queued re-run target pour66-class-rerun.)

## Bookkeeping

- Queue: `pour1544-post-adjudication-rerun` queued → `verdict`/`kill` 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.pour1544-post-adjudication-rerun.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
- Canonical-stream caveat stands (rows a8_00 offsets unvalidated; pencil gloss on a5_03).
