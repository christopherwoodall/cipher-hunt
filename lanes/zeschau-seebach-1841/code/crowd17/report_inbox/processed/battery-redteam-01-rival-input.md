# Battery report: redteam-01-rival-input (GATHER-ONLY evidence package)

- Target id: `redteam-01-rival-input`
- Date: 2026-10-09
- Worker: battery worker (subagent 484bb6f2-826e-4751-893c-efa7f02649a2)
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt). `canonical.py` never used.
- Mode: gather-only. Battery decides nothing; no adjudication, no value named, no split declared.
- Queue: `redteam-01-rival-input` was queued/verdictless at start (pre-write assert passed).
- Lock: code/crowd17/next-token/locks/redteam-01-rival-input.lock (created at start, deleted on completion; no stale lock).

## Bar (verbatim, pre-registered before testing)

"Package the 'ein' kill and the 'ain'/'in'/'an' fence as red-team input for the 01 docket (01 split/polyvalence). Bars: package delivered; battery decides nothing."

Numbered clauses:
- **C1:** Package the 'ein' kill with byte-level window evidence. → PASS
- **C2:** Package the 'ain'/'in'/'an' fence with stated cause. → PASS
- **C3:** No adjudication, no value named, no split declared. → PASS

## Package contents

### 1. The 'ein' kill

Source: battery-val-01-rival-sweep (2026-10-09, verdict NULL; 'ein' killed at kill grade within).

- **Kill-grade contradictions at three windows:** @195, @1255, @1462 — 01 is forced word-initial at all three; zero genuine French words begin with "ein" in 33.6M chars of 1841 French. Residual hits were German fragments ("ein" 9x, "eine" 5x) and OCR noise ("einpoisoiiiu", "eink", "eing"). → 'ein' word-initial is impossible in French.
- **Fourth supporting window:** @484 (30=pas LEAD).
- **Scope of the kill:** word-initial only. 'ein' word-INTERNAL is French-plausible ("peine" 1,554x, "reine", ...) — the kill does not touch word-internal 'ein'.

### 2. The 'ain'/'in'/'an' fence

Source: battery-val-01-rival-sweep (2026-10-09), C1/C3/C4.

- Tested against all 15 listed windows (@195/@255/@327/@409/@484/@717/@940/@1255/@1261/@1440/@1462/@1634/@1653/@1731/@1818).
- **'ain':** no kill-grade contradiction at any window. Word-initial windows admit "ainsi" (3,816x); word-internal windows admit "-ain-" freely. Not positively parsed (neighbors mostly open) → NOT NAMED, **FENCED**.
- **'in':** no kill-grade contradiction at any window. Not positively parsed → NOT NAMED, **FENCED**.
- **'an':** no kill-grade contradiction at any window. Not positively parsed → NOT NAMED, **FENCED**.
- **Fence character:** evidentiary, not terminal. Re-openable when more neighbor values are banked. No candidate met the naming bar.

### 3. Docket context for the red team

- The 01 docket (`redteam-01-split-docket`, queued) holds the conditioned-split question: 01='on' iff immediately preverbal (cf. the 67 precedent), red-team venue under §7.
- battery-redteam-01-split-input (gather-only package) and battery-on-01-84-distrib-package (NULL, gather-only) are the companion inputs.
- This package adds: the letter-cluster rival hypotheses ('ain'/'ein'/'in'/'an') are resolved — 'ein' dead at kill grade (word-initial), the other three shelved on an evidentiary fence. Any future 01 value or split decision must reckon with these closures.

## Scope

Gather-only package. No value named, no class named, no split declared; §7 intact. No standing/red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (rows a1_01/a2_08/a7_02 offsets unvalidated; pencil gloss on a5_03).

Per the gather-only precedent (R19-182; battery-redteam-tonic-fence-input), no follow-up targets proposed — all further battery work on the 01 rival question awaits the red team's adjudication of the deferred docket.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-redteam-01-rival-input.md
- Queue: `redteam-01-rival-input` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.redteam-01-rival-input.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock: created 2026-10-09T20:02:00Z (agent 484bb6f2, no stale lock), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
