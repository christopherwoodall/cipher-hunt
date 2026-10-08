# SYSTEMATIC DRAG — run report (2026-10-07)

Plan: `code/council/systematic-drag.md` (pre-registered). Implementation:
`code/council/drag/` — `common.py` (stream/oracle/syllabifier),
`build_inventory.py`, `run_drag.py`. All runs seeded, byte-rederivable.

## Tractability (actual)
- Inventory build: 66 s (3.45M pool tokens → 45,060 candidates → 37,418
  after subsumption → top 500 n-grams + 55 seeds = 555 phrases, 1,127 variants)
- Main drag: 4.4 s (555 phrases × ≤3 variants × 1,847 positions)
- Shuffle null (20 replicates, 2 workers): 88 s
- Decoy null (122 phrases): <1 s
- **Total: ~95 s.** Well under the plan's ~2 h estimate.

## Positive control: PASS
"par ce que" reproduced at @224, @952, @1526 exactly (par=96✓ ce=87✓ que=46✓).
Implementation verified correct before the main run.

## Main drag: 9 primary hits, 0 veto-sensitive
(3 are the positive control; 6 are new)

| pos | phrase | var | k | m | rank | alignment |
|---|---|---|---|---|---|---|
| 1240 | le prince | V0 | 3 | 2 | 13.11 | le=77(le✓) prin=81(?) ce=87(ce✓) |
| 1401 | le prince | V0 | 3 | 2 | 13.11 | le=77(le✓) prin=81(?) ce=87(ce✓) |
| 179 | tout ce qui | V0 | 3 | 2 | 12.34 | tout=24(?) ce=87(ce✓) qui=64(qui✓) |
| 1766 | tout ce qui | V0 | 3 | 2 | 12.34 | tout=24(?) ce=87(ce✓) qui=64(qui✓) |
| 1774 | tout ce qui | V0 | 3 | 2 | 12.34 | tout=24(?) ce=87(ce✓) qui=64(qui✓) |
| 1799 | tout ce qui | V0 | 3 | 2 | 12.34 | tout=79(?) ce=87(ce✓) qui=64(qui✓) |
| 224 | par ce que | V0 | 3 | 3 | 5.84 | (positive control) |
| 952 | par ce que | V0 | 3 | 3 | 5.84 | (positive control) |
| 1526 | par ce que | V0 | 3 | 3 | 5.84 | (positive control) |

0 veto-sensitive → no provisional is vetoing a would-be hit (no board-risk flags).

## Nulls
- **Shuffle null (20 seeded replicates):** hits per replicate
  [17,24,13,7,18,9,5,14,10,10,15,14,13,7,12,14,15,19,14,4],
  mean 13.1, std 5.2. Real = 9. **Real does NOT beat all 20 shuffles**
  (pre-registered bar not met; real is 0.8σ below the null mean).
- **Decoy null (122 anachronistic phrases):** 0 hits. The bar is tight;
  the 9 real hits are not looseness artifacts.
- **FDR estimate:** 13.1 / 9 ≈ 1.4 → the 6 new hits are consistent with
  chance. Treat as LEAD-grade docket items, not discoveries.

Note on the shuffle null: oracle-active positions are 400/1847 (real)
vs mean 361/1847 (shuffles), so the null is not confounded by oracle
coverage — the real stream simply isn't enriched for these phrases
vs chance (plan §4.3, third bullet: the remaining plaintext avoids the
top-500 formulaic phrases, which constrains register/topic).

## Board tensions from the 6 new hits
- **"tout ce qui" ×3 (tout→24) vs 24="en" (STRONG lead, F31):**
  incompatible — if 24="en" holds, @179/@1766/@1774 are dead.
  The @1799 hit (tout→79) is clean of this tension.
- **"le prince" ×2:** no tension (prin→81 unknown; ce→87="ce"
  consistent with the provisional). 81="prin" would be a new lead.
- No hit contradicts any GT, provisional, or islet value
  (0 contra by construction of the primary bar).

## Files
- `drag_hits.json` — all 9 hits with per-syllable alignment tables
- `null_report.json` — shuffle counts, seeds, FDR, decoy hits (0)
- `inventory.json` — 555 phrases, variants, frequencies
- `board oracle` — `common.build_oracle()` (frozen logic; per-stream)
