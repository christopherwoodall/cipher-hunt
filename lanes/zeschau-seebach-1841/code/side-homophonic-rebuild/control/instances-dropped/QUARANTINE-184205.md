# QUARANTINE NOTE — seed 184205 (dropped from the rebuild-fleet batch, 2026-10-07)

**DO NOT SCORE.** These files are OUT OF THE REGISTRABLE BATCH.

**Reason for drop (Metrologist adjudication, binding, 2026-10-07):**
`metrologist/FINDINGS.md` Task 1 / Ruling. Occurrence-phase χ² = 329.5,
+9.5 above the pre-registered band ceiling of 320 (CONTROL-DESIGN.md §3).
The batch's own builder flagged it FAIL at build time. Replacement
protocol: first in-band draw in seed order → 184207 @ 242.3 (mid-band),
adopted at the same slice slot (idx 4, Les Mis slice [16000, 20000]).
Final batch: 184201, 184202, 184203, 184204, 184207, 184206.

**Why kept (not deleted):** R8 sensitivity provision — 184205 may serve
as a NON-REGISTRABLE sensitivity diagnostic alongside the final 6
(score and report whether the §4 verdict changes with/without it).
Never enters the scored set.

**Dropped-entry record (removed from scorable state):**
- chance_baseline.json entry "184205" (chance_primary 0.0232±0.0159,
  chance_secondary 0.1395±0.0178, oracle 0.9653) — removed from the
  live chance_baseline.json; this note is the record.
- build_checkpoint.json / build_summary.json "184205" summary row removed
  (occurrence_chi2 329.5, unsupervised 13.1, keep 45.54%, T_eff 52,
  crib@pair 187, crib offsets tried [400]).

**File hashes (moved 2026-10-07, bytes unchanged):**
- SYNTHETIC-ct-184205.pairs.txt   e64ad597fec63c68935f2e7cbf2bafd909947c8ed66f80efc680325bfeacf52d
- SYNTHETIC-key-184205.json        a44f25716d37089096f569630336401c453f8bb3fb44d34b60d7dd367143ba26
- SYNTHETIC-crib-184205.json       06b1bf6a26fa5ae1ffdf3061e73abdbb41fd696b16dcc6bc5415796c5e5896eb
- SYNTHETIC-meta-184205.json       d01bc5adf8fbd1cc2e6483f515843489413c8709c023e9b2bdfce432215d9b60

Build params: q_cycle=0.5 (certified), T=56, slice idx 4 [16000, 20000].
Generator: code/side-homophonic-rebuild/control/generator.py.
