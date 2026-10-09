# Battery report: framecensus-60-redteam-pack

Worker: battery worker (session 8c1f1c3c-5329-4250-9f9e-288a99df735d).
Date: 2026-10-09.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`), parsed per
`code/side-keyhunt/repair_parse.py` (re-implemented in-session; 1,847 pairs
and 96 types asserted). `canonical.py` never used. R5005, sealed gate
instances, and the red-team adjudication queue untouched.
@i = 0-based pair index; 1-based @ = i+1 (matching the ledit-60-corrob census
offsets verbatim).
Lock: `code/crowd17/next-token/locks/framecensus-60-redteam-pack.lock` created
at start with agent id + UTC timestamp, deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"package iff every 60 window (census offsets from ledit-60-corrob) is classified
with standing values and cited, with no new claim beyond the census"

Numbered clauses (fixed before data examination):

1. (C1) Every 60 window (the 18 census offsets from ledit-60-corrob) is
   classified.
2. (C2) Every classification uses only standing values (banked, granted,
   promoted, provisional) and fences open neighbors with stated cause.
3. (C3) Every classification is cited to a standing battery report.
4. (C4) The package contains no new claim beyond the census: no value named
   for 60, no class declared for 60, no polyvalence declared at battery level.

## Method

1. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types.
2. Located all 60 windows: 18, offsets
   [119, 172, 197, 232, 322, 454, 637, 690, 700, 995, 1338, 1366, 1474, 1563,
   1644, 1674, 1690, 1735] — byte-identical to ledit-60-corrob's census.
3. For each window, extracted the 5-left/5-right context and adopted the
   classification from the standing battery verdicts listed below. Where two
   batteries disagree, both are presented without adjudication — adjudication
   is the red-team docket's job.

## 18-window frame census

Class keys: V = verbal (bare-60 or ent-60 per split-60-verbs),
A = adjectival NP frame, N = neutral/fenced. Citations are standing verdicts.

| @ | row | local frame | slot | licensing frame / evidence |
|---|-----|-------------|------|---------------------------|
| 119 | a1_03 | `21 60 90` | N | vient-parvenir formula third; 21 open; fenced to queued frame-vient-parvenir (adj-60 scan) |
| 172 | a1_05 | `21 60 09` | N | same family; 09 open; fenced (adj-60 scan) |
| 197 | a2_00 | `21 60 08 67` | V | `[56] ce [01] [21-N] [60-V] [08] et [76-N]`; geometry byte-identical to V1's `qui 60 08`; 7th bare-verb window — battery-slot-60-at-197 PROMOTE 2026-10-09 |
| 232 | a2_01 | `21 60 71` | N | formula third; `60 71` twin of V5 but owned by queued frame-vient-parvenir; not touched by verb-60 — fenced |
| 322 | a2_04 | `92 60 15` | N | 92 and 15 open; no participial frame (ledit-60-corrob C3) — fenced |
| 454 | a2_10 | `77 60 65` | A | flagship NP frame `le [60-adj] [65-N]`; only determiner-left + noun-right 60 window stream-wide; participial value 60="dit" kill-grade dead (dit-60-syncretic); adjective single-value claim killed — battery-adj-60 W1, ledit-60-corrob C2 |
| 637 | a4_01 | `46 60 67 77` | N | `que [60] et[67] le [89]...`; verb-coord-637 KILL (@637 coordination dead); strained under both readings — fenced; queued adj-frames-995-637 may harden |
| 690 | a5_00 | `29 60 03` | A | `[60-adj] [03-N]` with 03 nominal (independently supported anchors) — battery-adj-60 W2 |
| 700 | a5_01 | `94 60 12 98` | V | `ne [60] n [98]`; "ne" must be followed by a verb (94='ne' battery-promoted, 12='n' letter); bare-60 V2 — battery-verb-60 V2 |
| 995 | a6_01 | `03 60 67 11` | V/A | AMBIGUOUS: verbal `[03-N] [60-V] et` (battery-verb-60 V3, verb-compatible; right edge fenced residual) AND postnominal adjective `[03-N] [60-adj] et la` (adj-60 supporting note) — live evidence on BOTH arms |
| 1338 | a7_05 | `64 60 08 65` | V | `qui [60] [08]`; subject-relative "qui" (64 granted) must be followed by a finite verb; bare-60 V1 — battery-verb-60 V1; present-participle reading killed here (participle-60 V1) |
| 1366 | a7_06 | `14 60 03` | N | determiner-left like @454, but 03 is verb-stem (stem-03 battery-PROMOTED); "ledit"-shaped participle frame impossible — ledit-60-corrob C3; battery-npframe-60-1366 NULL |
| 1474 | a7_10 | `53 60 06 67` | V | `[53] [60-stem]ent veut [33-29]`; ent suffix on stem-60; right edge clean modal `veut [X]er`; bare-60 V4 — battery-verb-60 V4 |
| 1563 | a8_01 | `06 60 71` | V | ent-prefix `ent[60]` word-initial (backward attach blocked by 30='pas' battery-promoted); ent-60 V5 — battery-verb-60 V5 |
| 1644 | a8_04 | `98 60 03` | A | `[60-adj] [03-N]` — battery-adj-60 W3 |
| 1674 | a8_05 | `92 60 03` | A | `[60-adj] [03-N]` — battery-adj-60 W4 |
| 1690 | a8_05 | `14 60 27` | N | determiner-left like @1366, but 27's class is open; queued npframe-60-detleft-closeout will fence iff 27 non-nominal — ledit-60-corrob follow-up |
| 1735 | a8_07 | `06 60 12 48` | V | ent-prefix `ent[60]ne` (one word; "ne"-after-verb ungrammatical); the 'de' arm of the left edge killed — battery-leftedge-60-value KILL 2026-10-09; ent-60 V6 — battery-verb-60 V6, battery-split-60-verbs PROMOTE |

Tally: 18/18 classified. 7 verbal windows (6 from battery-verb-60 plus @197
from battery-slot-60-at-197; @995 belongs to both arms). 4 adjectival NP
frames (@454, @690, @1644, @1674 — battery-adj-60 W1–W4; note @454's
participial value is dead, its adjective single-value claim killed).
7 neutral/fenced (119, 172, 232, 322, 637, 1366, 1690).

## Standing evidence the red-team docket must weigh

- Verbal arm: V1 @1338 (granted 64='qui' forces finite verb — kill-grade
  forcing), V2 @700 (battery-promoted 94='ne' + letter 12='n'), V3 @995
  (class-ambiguous, verb-compatible), V4 @1474 (`[60]ent`), V5 @1563
  (ent-prefix), V6 @1735 (ent-prefix), @197 (7th verb window, battery
  slot-60-at-197 PROMOTE). Noun single-value claim killed (noun-60);
  adjective single-value claim killed (adj-60, kill-grade at @1338 and
  @700 under §7 — a single value cannot span the adjective frames and
  the verb-forcing windows).
- Verbal-arm split (battery-split-60-verbs PROMOTE, finding grade):
  bare-60 verb (V1–V4) and ent-60 verb (V5–V6) are TWO items sharing the
  syllable 60 — predecessor sets disjoint, successor overlap exactly {12},
  `06 60 06` x0, no French verb with both `[X]ent` and `ent[X]` forms.
  The naming follow-ups (verb-60-bare, verb-60-ent) both returned null —
  no value is nameable for either arm.
- Adjective arm: four NP frames (@454/@690/@1644/@1674, anchors
  independently supported per adj-60) plus @995 postnominal support;
  @454's participial leg ("dit") is kill-grade dead (dit-60-syncretic),
  and the det-left closeout (npframe-60-detleft-closeout) is queued.

## Open dependencies (flagged, not resolved)

1. Canonicality: rows a7_05 (V1 @1338) and a7_10 (V4 @1474) are among the
   68 unvalidated upstream offsets; both windows dissolve under offset-1
   re-pairing (battery-split-60-verbs phase-stress check). Row a2_00
   (@197) likewise unvalidated. Verdicts here are canonical-stream per
   protocol.
2. Load-bearing provisional/battery-level values: 77='le' at @454;
   94='ne' + 12='n' at @700; 30='pas' (06 forward-attachment) at
   @1563/@1735; 84='on' grant (excludes 60='on' at V6); 98='vient'
   battery-level at @197's clause start.
3. 03's verb-stem promote (stem-03) closes @1366's "ledit" frame but
   sits in tension with the @454/@690/@1644/@1674 adjective frames'
   need for nominal 03 — 03 is before the red team on its own docket.
4. Open neighbors fence windows, never decide them: 21 (@119/@172/@232 —
   owned by queued frame-vient-parvenir), 92/15 (@322), 89 (@637),
   27 (@1690 — closeout queued), 08 (stem-08 queued), 53 (prof-53 null).
5. The NP-frame adjective question vs the verbal windows is already
   before the red team as poly-60-redteam (priority 1); this package adds
   the bare/ent verbal split, which that docket must take into account.

## Per-clause pass/fail

- C1: PASS — 18/18 windows classified (see table).
- C2: PASS — every classification uses only standing values
  (banked/granted/promoted/provisional per §7); open neighbors fenced
  with stated cause.
- C3: PASS — every row cites a standing battery report.
- C4: PASS — no value named for 60, no class declared for 60, no
  polyvalence declared at battery level; the adjudication stays with
  poly-60-redteam.

## Adverses

"feeds the poly-60-redteam docket; no battery-level decision" — answered:
this package makes no battery-level decision. It presents both arms'
evidence side by side (including the ambiguous @995 window that reads
under both classes) and flags open dependencies.

## Verdict: PROMOTE (ruling-ready input package grade)

All bar clauses pass. The package is delivered to the poly-60-redteam
docket without any battery-level declaration on 60's class or
polyvalence. This does not bank, promote, or downgrade any value: the
adj-60 kill (single-value adjective) and the split-60-verbs promote
(verbal-arm split, finding grade) stand unmodified.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/framecensus-60-redteam-pack.lock`
  created on start (agent id + UTC timestamp), deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry
  only; pre-write assert confirmed `queued`/verdictless; JSON re-validated
  after write.
- R5005, sealed gate instances, and the red-team adjudication queue
  untouched. No standing verdict contradicted or downgraded. §7 intact.
