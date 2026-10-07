# METHOD FREEZE — Seebach homophonic solver

**Frozen:** 2026-10-07 (after red-team KILLs + cross-fleet FIX A/B)
**Status:** No further code changes before the control verdict (CONCERN-2).
Any post-control patch faces FRESH instances (new seeds).

## Frozen code md5

### solver/
| file | md5 |
|---|---|
| solver.py | d30dae03f22f060348ae29cbb7fc5096 |
| phonetics.py | e85c9002fadf4526aa25b443f2191add |
| build_lm.py | a3ed8df274c6d67a3fc8987ba15657a4 |
| phase.py | 9587f494b8b20b2b8734fb4ed196d21d |
| control_harness.py | 33fe06f695e00e8c9fbae79a68e77c2b |
| ct_loader.py | bc0c9622cc9ff3fec5886c947ddf27ed |
| crib_inventory.py | f7c10dff9052d323693fd19c05ad0e29 |
| config.json | ecea1a49cd6604529e9941699f475179 |
| METHOD.md | 0b23357ef4108d16fb6d325f73b3d4cf |
| README.md | 0240c2fd8e80375ec0a5646e62867197 |

### control/
| file | md5 |
|---|---|
| generator.py | 0d1b74fdb7d18819dbbbbe1156d02231 |
| persist_planted.py | 90df55fc0a81eb496c5dced05922eff6 |
| seal_meta_leak.py | a8eb179c52248538241a4429e169f31a |

## What changed in this freeze (vs red-team ruling versions)

1. **KILL-1:** `control_harness.py` gate rewritten to §4 exactly
   (primary mean≥0.20/min≥0.10; secondary mean≥0.30/min≥0.22;
   6-instance aggregation via `--aggregate`). Old 0.50 proposal superseded.
2. **KILL-2:** `truth['planted']` persisted to all 6 sealed keys
   (bit-identical rebuild verified); SECONDARY is true decode accuracy.
3. **DEMOTE-1:** Phase claim restated (noisy detector); `--no-contact` added.
4. **DEMOTE-2:** Projection-equivalent recovery reported alongside exact.
5. **CONCERN-6:** meta/ leak sealed (polyvalent_groups+params → sealed key).
6. **FIX A:** `ct_loader.py` uses F32 repaired parse (1,847 pairs; @754/@1034).
7. **FIX B:** `crib_inventory.py` + `inventory_mode='crib'` (default);
   bottom-up from 7 cribs + by-ear personne + polyvalence islets.

## Verification run

- `solver.py --self-test`: PASS (max err 1.13e-10 over 300 moves, crib inventory)
- `ct_loader.py`: 1,847 pairs / 96 groups; landmarks @754/@1034 VERIFIED
- `persist_planted.py`: 6/6 bit-identical rebuilds; 'planted' persisted
- `seal_meta_leak.py`: 6/6 meta files sealed
- Crib inventory: 291 items; 16/16 by-ear chunks present (was 14/16)

## Runner instructions

1. Use the frozen md5s above to verify code before batch.
2. Run control batch with `inventory_mode='crib'` (default in config.json).
3. Ablation matrix: {full, --no-contact, --no-word, --no-poly,
   --inventory-mode units} × 6 instances.
4. Aggregate with `control_harness.py --aggregate` (6 reports) for §4 verdict.
5. Do NOT run on R5005 until CONTROL-PASS.
