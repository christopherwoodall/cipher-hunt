# Battery verdict: det-14-clitic-178

- Target: `det-14-clitic-178` (battery-queue.json, priority 4, status queued)
- Claim: "Name the subject of '69 le [24-verb]' at @178 — is 69 the subject, or does the clause 'ce 86 21 69' absorb it?"
- Date: 2026-10-09. Worker: battery worker (agent ba08c7da-e04a-4422-ac84-34b86d31f14d). Lock `code/crowd17/next-token/locks/det-14-clitic-178.lock` created on start; deleted on completion after queue confirm.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`. 1,847 pairs / 96 types re-derived in-session. R5005 untouched. `canonical.py` never used. No invented data.
- Parent: `det-14-census` PROMOTE (2026-10-09), whose follow-up #2 is this target.

## Bar (verbatim, from battery-queue.json)

The queue entry's `bars` field is null. Per BATTERY-PROTOCOL.md §2, the claim itself supplies the testable bar; no modification after seeing data. Restated as numbered clauses:

C1. Name the subject of the "69 le [24-verb]" window at @178 with battery-grade evidence (69 as subject, or the "ce 86 21 69" absorption).
C2. If neither arm is nameable at battery grade, fence the locus with stated cause.

Offset note: the claim's "@178" is 1-based (0-based @177 = the 69 pair); the parent battery's "@178" was 0-based citing the 14 pair itself (0-based @178 = 14). Same window. All offsets below are 0-based pair indices into the repaired stream.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start, deleted on completion.
2. Re-derived the repaired stream in-session; byte-confirmed the locus on row a1_05 (offsets unvalidated per the canonicality caveat).
3. Tested the two arms against standing values only. Adverses: none listed; standing verdicts adopted, not re-litigated.

## Window-level evidence (@-offsets, repaired stream)

Row a1_05 (0-based @161–189):

`94 24 87 11 24 82 84 53 12 48 21 60 09 87 86 21 69 14 24 87 64 23 37 06 00 33 16 00 66`

Locus (0-based): `@174=87 @175=86 @176=21 @177=69 @178=14 @179=24 @180=87 @181=64` = "ce [86] [21] [69] [14] [24-verb] ce qui …".

Standing values (none decided here): 87='ce' (granted, A4 allophone tier), 86=INF class (R15-A9 GRANT, confirmed R20-087), 21=NOUN class (battery-promote), 69=NOUN class (registry, R19-109), 14=locus-level clitic 'le' (parent det-14-census PROMOTE; global 14='le' kill-grade dead per le-14-kill-1121 — consistent, locus-level readings are not the global value), 24=finite verb class, modal-shaped (R17-009 class-level GRANT; value open — savoir/vouloir narrowed, neither named), 64='qui' (granted).

### Arm A — 69 is the subject: PASS

"[69-noun] le [24-verb]" parses with standing values only: nominal subject (69, registry noun class) + object clitic "le" (14, locus-level per the parent) + finite verb (24, class-level GRANT). "L'homme le sait"-shaped. Zero ungranted assumptions. The subject is **named: 69**.

### Arm B — "ce 86 21 69" absorbs 69: FENCED with stated cause

For 69 to be absorbed, "ce 86 21 69" must form a complete grammatical unit under standing values. It cannot:

- F1: 87='ce' + 86=INF-class — "ce" cannot subject an infinitive in 1841 French; no French frame "ce [INF] …" exists as a standalone clause. (86's INF class is a standing grant; the @867 prefix-tier finding is locus-level and does not transfer here.)
- F2: the 21/69 noun-noun contact has no licensed composition under standing values (both noun-class; no granted compound frame).
- F3: even hypothetically absorbed, [24-verb] would strand subjectless — 14 is the clitic, and the only other leftward nouns (21, 53, 48) would strand a double-subject "[21] [69] le [24]" or sit too far left. Absorption does not rescue the window; it kills it.

No licensed rescue exists for Arm B. The window parses **only** under Arm A.

## Per-clause pass/fail

1. Subject named at battery grade — **PASS**: 69 (Arm A, standing values only, zero ungranted assumptions).
2. Fence arm — moot (C1 passed).

## Verdict: PROMOTE

The subject of the "69 le [24-verb]" window at @178 is **69**. The "ce 86 21 69" absorption arm is fenced: no licensed parse under standing values (F1–F3).

## Scope

- Locus-level only (0-based @174–179). Names a subject, not a value: 69's value, 14's value beyond locus-level 'le', 24's value, and 86's tier all untouched.
- Untouched: le-14-kill-1121 (global 'le' kill stands — this finding is locus-level, consistent), 24's open value (savoir/vouloir), 86's tier-split §7 candidacy, the parent det-14-census PROMOTE, §7 (no split or polyvalence declared).
- No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a1_05 offsets unvalidated).

## Follow-ups

None required (promote, not null).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-det-14-clitic-178.md`
- Queue: `det-14-clitic-178` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.det-14-clitic-178.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/det-14-clitic-178.lock`: created on start (agent ba08c7da-e04a-4422-ac84-34b86d31f14d), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
