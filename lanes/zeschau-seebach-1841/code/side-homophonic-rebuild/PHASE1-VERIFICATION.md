# PHASE-1 VERIFICATION — rebuild-fleet fresh synthetic controls (2026-10-07)

> **PHASE-1b addendum (2026-10-07):** per the Metrologist's binding
> adjudication (`metrologist/FINDINGS.md`, Ruling), 184205 was REPLACED by
> 184207 (first in-band draw in seed order @ occ χ²=242.3, mid-band; the
> Runner's independent in-memory walk rebuild reproduced 242.3 exactly at
> slice idx 4 = [16000, 20000], the slot 184205 vacated). The final
> registrable batch is **184201, 184202, 184203, 184204, 184207, 184206**.
> 184205 is QUARANTINED in `control/instances-dropped/` (with
> `QUARANTINE-184205.md`; non-registrable sensitivity diagnostic only —
> never scored). Its chance-baseline/checkpoint/summary entries were
> removed from live state. `generator.py` / `seal_meta_leak.py` /
> `band_check.py` seed lists updated to the final 6. `persist_pclasses.py`
> re-run for the final 6 → `metrologist/sealed-pclasses.json`
> (sha256 1024427db1d30701…). `band_check.py` (R7-fixed) re-run on the
> final 6: reported == recomputed on all, ALL IN BAND.
>
> Final batch table:
>
> | seed | pairs | groups | crib `11-70-82-34-29-40` | occ χ² | in [181,320] | chance_primary | chance_secondary | oracle |
> |------|-------|--------|---------------------------|--------|--------------|----------------|------------------|--------|
> | 184201 | 1846 | 96 | 1× @305 | 195.1 | yes | 0.0216±0.0154 | 0.1687±0.0174 | 0.9258 |
> | 184202 | 1846 | 96 | 1× @194 | 222.9 | yes | 0.0218±0.0151 | 0.1428±0.0171 | 0.9014 |
> | 184203 | 1846 | 96 | 1× @229 | 183.2 | yes | 0.0228±0.0160 | 0.1335±0.0172 | 0.9030 |
> | 184204 | 1846 | 96 | 1× @190 | 245.3 | yes | 0.0208±0.0150 | 0.1405±0.0152 | 0.9068 |
> | 184207 | 1846 | 96 | 1× @184 | 242.3 | yes | 0.0209±0.0150 | 0.1338±0.0168 | 0.9252 |
> | 184206 | 1846 | 96 | 1× @44 | 285.3 | yes | 0.0213±0.0154 | 0.1234±0.0175 | 0.9025 |
>
> 184207 ct sha256:
> `c559d0ed9f9f833e0335fcda848a678851cfac7dbf8afe0de0cd7dc9d4cef709`
> All six sealed; solver inbox holds only ct+crib for the final 6.
>
> --- original Phase-1 record follows ---

Builder: `control/build_rebuild_instances.py` (resumable driver over
`control/generator.py` semantics; seeds 184201–184206; deterministic).
Launched detached via `control/launch_build.sh` (setsid+nohup, per-seed
checkpoints in `control/build_checkpoint.json`).
Calibration: q_cycle sweep on seed[0] pilot → q=0.4:102.6 / q=0.5:195.1 /
q=0.6:517.6; certified q_cycle=0.5, T=56 (same as frozen batch).

## Verification table

| seed | pairs | groups | crib `11-70-82-34-29-40` | occ χ² | band [181,320] | sealed | verdict |
|------|-------|--------|---------------------------|--------|----------------|--------|---------|
| 184201 | 1846 | 96 | 1× @pair 305 | 195.1 | in | yes | OK |
| 184202 | 1846 | 96 | 1× @pair 194 | 222.9 | in | yes | OK |
| 184203 | 1846 | 96 | 1× @pair 229 | 183.2 | in | yes | OK |
| 184204 | 1846 | 96 | 1× @pair 190 | 245.3 | in | yes | OK |
| 184205 | 1846 | 96 | 1× @pair 187 | 329.5 | **OUT (+9.5 / +3.0%)** | yes | **FAIL** |
| 184206 | 1846 | 96 | 1× @pair 44 | 285.3 | in | yes | OK |

(All: coverage repair 0 pairs; T_eff 52–55; keep 42.4–47.3%; islets 6/6.
Chance baselines computed per instance, `control/chance_baseline.json`.)

## Anomaly: seed 184205 occurrence χ² = 329.5, above band ceiling 320

- The χ² band is a per-instance acceptance criterion (task spec) and the
  frozen batch had all six in-band (181.2–272.1). This instance is 3.0%
  above the ceiling.
- No legitimate in-semantics fix exists: the build is fully deterministic
  (seed × offset × params); re-running reproduces 329.5 exactly. Any
  parameter nudge (q_cycle, crib offset order) would break `--build-all`
  semantics and comparability with the frozen batch.
- Direction of the miss: HIGHER χ² = stronger phase-cycle signal, which is
  the solver-helpful direction on that axis (band floor 181 brackets the
  real R5005's χ²=181.3). The instance remains ≥-real on every other axis
  (length 1846, 96 groups, 7 pins, 6 islets vs real 3, ear noise on,
  register gap kept). The certified pilot (184201) is in-band at 195.1.
- DECISION NEEDED (coordinator): accept 184205 as-is with this flag
  (recommended — marginal, solver-helpful direction, deterministic
  integrity intact), or re-certify a different parameter set.

## Sealing status

- `seal_meta_leak.py` re-run: all six "already sealed". Open meta files
  contain NO `polyvalent_groups` and NO `params`; key files carry
  `sealed_meta` {params, polyvalent_groups} + per-position `planted` (for
  SECONDARY scoring) and are Runner-only.
- Solver-facing inbox `solver_inbox/` holds ONLY ct + crib files
  (12 files). Keys never leave `control/instances/`.

## Provenance

- sha256 of ct streams (SYNTHETIC-ct-<seed>.pairs.txt):
  - 184201 ba72e2b62b12766e37a3c4532178fad021b075a62caf0b461cb1f81c28d57fb5
  - 184202 3abef81bad9e97097a2fbbc3da51be70d04bd48485e0b4eb48a27a7aefce762c
  - 184203 60dd9c194ed4a1abd3b8d3bcedb16b4e1e3ebe656141e9a6157afb99ea1202ce
  - 184204 2d83206df7a32356d9da2a919c13cbed1ee88afb6c89f8ff8d3ead8d355cacfe
  - 184205 e64ad597fec63c68935f2e7cbf2bafd909947c80efc680325bfeacf52d
  - 184206 5004051c9d2f3af5378a611d04732e60836887d2bc563ccdb581e8dcdfc3f63a
- Full numbers: `control/build_summary.json`, `control/calibration.json`,
  `control/chance_baseline.json`, `control/build_rebuild_instances.log`.
