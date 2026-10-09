# Battery verdict: seg-a1_01-extrinsic-phase

## Bar (verbatim, pre-registered BEFORE testing)

"digit-count parity, row-boundary formulas with a1_00/a1_02, or manuscript/transcription facts that discriminate a1_01's phase"

Restated as numbered pass/fail clauses:

1. (C1) Digit-count parity: some parity fact of the digit strings discriminates
   whether a1_01 drops its leading digit (offset 1) or its trailing digit
   (offset 0).
2. (C2) Row-boundary formulas with a1_00/a1_02: some structural relation between
   a1_01's phase and its neighbor rows' phases discriminates the choice.
3. (C3) Manuscript/transcription facts: some record about the manuscript or the
   transcription (as opposed to the statistical parse) discriminates a1_01's
   phase.

Adverses: none listed.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/seg-a1_01-extrinsic-phase.lock`
on start. Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed like `code/side-keyhunt/repair_parse.py` (1,847 pairs / 96 types
asserted). `canonical.py` never used. R5005, sealed gates, red-team adjudication
queue untouched. No red-team verdict on a1_01's phase exists.

Standing context (cited, not re-run): battery-seg-a1_01-constraint-sweep
(PROMOTE) already showed offset-1 is constraint-clean across all 35 pairs of
a1_01 and dissolves the "la tout" banked contradiction. That is
constraint/statistical evidence. This battery tests only EXTRINSIC evidence —
evidence from outside the statistical parse.

## Findings

Row a1_01: 71 digits, canonical offset 0, spans 1-based stream @36–@70.
Offset-0 drops the trailing digit ("6"); offset-1 drops the leading digit
("0"). Both phases yield 35 pairs, all within the 96-type inventory
(seg-a1_01-constraint-sweep: zero novel groups under offset-1).

### C1 — Digit-count parity: FAIL (no discrimination)

- Odd-length rows are the norm, not an anomaly: 28 of 70 rows have odd digit
  counts (a1_01, a1_02, a1_03, a1_05, a2_00, a2_06, a2_10, a2_11, a3_01, a4_02,
  a5_00, a5_01, a5_08, a5_10, a6_04, a6_07, a6_09, a7_02, a7_04, a7_05, a7_06,
  a7_09, a7_10, a8_01, a8_03, a8_04, a8_05, a8_11).
- Total digit count is 3,764 (even) either way; the row length does not change.
- A 71-digit row drops exactly one digit under either phase. Nothing about the
  parity of 71 favors the leading drop over the trailing drop (or vice versa).

### C2 — Row-boundary formulas with a1_00/a1_02: FAIL (no such relation exists)

- The tokenization is row-local by construction: repair_parse.py parses each
  row independently from its own offset
  (`pairs += [(s[i:i+2], lid) for i in range(o, len(s)-1, 2)]` per row).
- Verified in-session: flipping a1_00's offset leaves a1_01's AND a1_02's pair
  sequences byte-identical. No cross-row phase relation exists in the parse.
- The only cross-row objects are boundary contacts (a1_00-final/a1_01-initial,
  a1_01-final/a1_02-initial). Contact comparisons ("01|08" vs "01|89",
  "24|56" vs "46|56") are marginal/statistical evidence, not extrinsic
  evidence — and the lane's standing guardrail (all-70-row phase sweep, 2026-10-09)
  is explicit that likelihood cannot override byte evidence (gloss-anchored a5_03
  prefers the wrong phase). So the boundary angle is closed twice over:
  structurally (row-local parse) and doctrinally (no likelihood override).

### C3 — Manuscript/transcription facts: FAIL (none bear on a1_01)

- No full-size manuscript scans are held. `data/manuscript/PROVENANCE.md`
  records that full-size scans (IMG_R5005_I28858_P1..P6.jpg) require DECODE
  authentication (not pursued); the cached thumbnails (TH_P1..TH_P6.jpg) cannot
  resolve digit-level pairing.
- PROVENANCE.md contains no a1_01-specific note.
- The transcription line is clean: `a1_01 089139...913246` (71 digits, no
  formatting artifact, no leading/trailing whitespace anomaly) — nothing about
  the transcription bears on which end of the row is spurious.
- The only byte-pinned manuscript anchors are the erased pencil glosses:
  "la pre m i er e" over row a5_03 and "que" over row a8_05 (repair_parse.py
  header). Neither touches a1_01.

## Per-clause pass/fail

1. C1 digit-parity: FAIL — no discriminating parity fact.
2. C2 row-boundary formulas: FAIL — no cross-row phase relation exists; boundary
   contacts are statistical, excluded by the standing guardrail.
3. C3 manuscript/transcription facts: FAIL — no scans, no a1_01 note, clean
   transcription line, glosses elsewhere.

## Verdict: NULL

No extrinsic evidence discriminates a1_01's phase from outside the statistical
parse. The phase question for a1_01 stands where the battery lane left it:
offset-1 is the constraint-clean rival (seg-a1_01-constraint-sweep PROMOTE),
adoption is a red-team act. This null does not touch that finding and does not
contradict any standing or red-team verdict. §7 intact.

## Follow-ups proposed (for supervisor queuing)

1. `scan-verify-a1_01` (P4) — IF full-size DECODE scans arrive (lane's external
   acquisition rule applies; no email/purchase/scans order authorized), verify
   a1_01's 71-digit string against the manuscript image line. A mis-transcribed
   leading or trailing digit would discriminate the phase directly.
2. `offset-drop-census` (P4) — census all 28 odd-length rows: does the EM's
   drop-end choice (first vs last digit) correlate with row-label order or page
   runs? A transcription-process pattern (e.g. leading-digit drops clustering at
   line starts) would supply an extrinsic process prior for a1_01's phase. Not
   duplicated: queued seg-a1_01-hybrid-phase owns the transcription-error
   rival itself; this is the process-level complement.
3. No third follow-up: seg-a1_01-hybrid-phase (already queued) covers the
   remaining intrinsic rival; nothing else is proposed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-a1_01-extrinsic-phase.md`
- Queue: `seg-a1_01-extrinsic-phase` status `queued`→`verdict`, result `null`,
  date 2026-10-09 (temp-file + rename; pre-write assert passed; JSON
  re-validated; only this entry touched).
- Lock created on start, deleted on completion.
