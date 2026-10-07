# Metrologist findings — Seebach homophonic-solver rebuild fleet

**Role:** metrologist (instrumentation verification for the rebuild control).
**Date:** 2026-10-07. **Scope:** `code/side-homophonic-rebuild/`
(read-only on the frozen `code/side-homophonic/`).
**Status:** Tasks 1–4 COMPLETE. R7 KILL accepted and fixed; 184205
adjudication recorded (binding). Pending: Runner executes the 184205→184207
swap + quarantine (then metrologist re-verifies); Smith re-delivers the
rebuilt solver (R2 kill); Runner runs the post-freeze fresh-vs-ablation
comparison per the pre-registered criterion.

Reference docs: `../control/CONTROL-DESIGN.md` (pre-registered band §3),
`../control/calibration.json`, `../control/build_summary.json`.

---

## Task 1 — Fresh-instance band check: COMPLETE (R7-fixed)

The Runner built 6 fresh instances (seeds 184201–184206) with the rebuild
control's generator (byte-identical to the frozen generator except the seed
list — verified by diff; only `PARAMS['seeds']` differs).

**R7 KILL — accepted and fixed (2026-10-07).** The Red Team correctly
killed the first version of `metrologist/band_check.py`: it recomputed χ²
from the per-GROUP label phase (`key[g]['phase']`, the round-robin alias
deal) — the wrong quantity, reading 12.9 on 184201 vs the true 195.1
(demonstrated; matches the Red Team's "1–13" range). The calibrated
quantity per CONTROL-DESIGN.md §3 is the **occurrence-phase** χ²,
`occurrence_chi2(inst['pclasses'])`, where `pclasses` is the per-position
diluted-cycle phase sequence. The fixed tool re-derives `pclasses` by
**deterministic rebuild** (same generator code, certified q_cycle=0.5,
T=56 — the generator is seeded/deterministic, so this reproduces `pclasses`
exactly) and checks the recomputed χ² against both the meta file
(persistence/determinism check) and the pre-registered band [181, 320].

**Re-run results (fixed tool):** all 6 recomputed values match the reported
meta values exactly; structural invariants hold (1846 pairs, 96 groups,
crib exactly once each).

| seed | occ χ² (recomputed = reported) | in band [181, 320]? | unsup χ² | keep | oracle |
|------|-------------------------------:|---------------------|---------:|------|-------:|
| 184201 | 195.1 | YES | 9.0 | 42.36% | 0.926 |
| 184202 | 222.9 | YES | 336.4 | 47.01% | 0.901 |
| 184203 | 183.2 | YES | 211.0 | 44.71% | 0.903 |
| 184204 | 245.3 | YES | 5.1 | 47.33% | 0.907 |
| 184205 | **329.5** | **NO (+9.5 / +3.0% over ceiling)** | 13.1 | 45.54% | 0.965 |
| 184206 | 285.3 | YES | 48.4 | 47.11% | 0.903 |

The rebuild fleet's own builder independently flagged 184205 OUTOFBAND
(`control/build_rebuild_instances.log`: "VERIFICATION: FAILURES PRESENT").

**Provenance gap closed (R7 note):** `pclasses` was build-time-only. It is
now persisted sealed via `metrologist/persist_pclasses.py` →
`metrologist/sealed-pclasses.json` (sha256 `d7799c2c4cb63f52…`; SEALED —
planted truth, never show to the solver). The Runner re-runs
`persist_pclasses.py` after the 184205→184207 swap to cover the final 6.

### RULING (metrologist adjudication, 2026-10-07, BINDING): REPLACE 184205 with 184207 — option (b)

**Verdict: option (b).** 184205 is dropped from the batch; the Runner builds
184207 in its place (same slice slot, idx 4); the batch becomes
184201–184204, 184206, 184207. This ruling weighs the Red Team's R8 CONCERN
(accept-with-flag, no re-roll) against the coordinator's lean and finds for
replacement, for the reasons below. R8's transparency goals are preserved
via the logging/quarantine/sensitivity provisions.

**Why (b) over R8's (a):**
1. **Pre-registration.** The band [181, 320] was fixed before any solver saw
   the instances, and the fleet's own builder implements it as a per-unit
   acceptance gate — it flagged 184205 FAIL. Accepting post-hoc because
   "+3% is close" unties the exact hands pre-registration was meant to tie.
   If 329.5 is acceptable, there is no principled line left at 320.
2. **Bias direction.** The miss is solver-helpful (stronger rhythm than the
   "unrealistically clean" threshold, on the phase-machinery axis the
   rebuild touches). (b) removes an easier instance — it is the
   bias-against-interest, conservative choice. (a) would make any future
   PASS easier to challenge ("you kept an out-of-spec instance that helped
   the solver").
3. **Not cherry-picking.** The re-roll selects on a pre-registered,
   solver-independent instrument reading, made while no frozen rebuilt
   solver exists (R2 killed the Smith's central fix; re-delivery pending).
   It is acceptance sampling per the instrument's own gate, fully logged
   and deterministic — the anti-cherry-picking conditions are: fixed
   criterion, solver-blind timing, seed-order walk, complete draw log.
4. **R8's substance, honored differently.** R8 wants transparency, not the
   violation per se. Preserved via: (i) the complete draw-walk log below;
   (ii) 184205 quarantined, not deleted (`control/instances-dropped/`
   with a note); (iii) OPTIONAL sensitivity diagnostic — the Runner may
   score 184205 non-registrably alongside the final 6 and report whether
   the verdict changes with/without it. If the verdict is insensitive,
   the adjudication is moot in practice and clean in principle.
5. **No time pressure.** The batch is on hold pending the Smith's
   re-delivery — the swap costs one deterministic build.

**Draw walk** (deterministic, at certified q_cycle=0.5, idx 4 / slice 4,
seed order; Runner to verify by re-running):

| seed | occ χ² | verdict |
|------|------:|---------|
| 184207 | 242.3 | IN-BAND → **ADOPTED** (first in-band draw in seed order) |

184207 @ 242.3 sits mid-band (band midpoint 250.5), near the original-6
mean of 236 and the fresh-5 mean of 227. Predicted slice [16000, 20000]
(same slot 184205 vacated), T_eff=56. No further draws needed.
(Exploratory probes beyond the walk: 184208 @ 175.6 OUT on the low side —
confirming the band is a genuine two-sided filter, ~1-in-6 draws fall out
on either side; 184209 @ 291.8 in-band.)

**Runner instructions:**
1. Verify the walk (re-run the one-liner; expect 184207 @ 242.3), then
   build 184207 fully with `control/build_rebuild_instances.py` mechanics:
   swap 184205 → 184207 in the seeds list **at index 4** (same slice slot;
   do NOT append — list index determines the plaintext slice), certified
   q_cycle=0.5, T=56; compute its chance baseline; seal the key. Runner
   concurrence required — if the Runner disagrees with this ruling,
   escalate to the coordinator before building.
2. **Quarantine 184205**: move `SYNTHETIC-{ct,key,crib,meta}-184205.*` to
   `control/instances-dropped/` with a note; remove/annotate its
   `chance_baseline.json` entry; update `build_summary.json` /
   `build_checkpoint.json` to the final 6 seeds.
3. Re-run `metrologist/persist_pclasses.py` for the final 6
   (184201–184204, 184206, 184207) to refresh the sealed pclasses record.
4. Do not score the rebuilt solver until the metrologist re-verifies the
   built 184207 with the fixed `band_check.py`.
5. Optional (R8 sensitivity): score quarantined 184205 non-registrably
   alongside the final batch; report whether the §4 verdict changes
   with/without it.

**Self-caught probe error (recorded for the log):** my first replacement
probes ran at q_cycle=0.55 (the raw, uncertified `PARAMS` default) and
falsely suggested slices run hot (means ~340). Analytic check
(E[χ²] = n·2q⁴: 231 @ q=0.5 vs 338 @ q=0.55) exposed the error; re-running
at the certified q_cycle=0.5 gave the walk above. **Instrumentation
caution:** raw `PARAMS['q_cycle']=0.55` is NOT the certified config —
the certified 0.5 lives in `build_checkpoint.json`/`calibration.json`.
Anyone probing the generator must override q_cycle explicitly.

---

## Task 2 — q_cycle=0 ablation (phase-rhythm scrub): COMPLETE (set built; solver comparison pending Smith re-delivery)

**Rationale:** the phase rhythm is a synthetic control device ("not a
linguistic claim about the real cipher's phases — mechanism unknown",
CONTROL-DESIGN.md §2.3). A rebuilt solver that needs the rhythm to beat
the §4 bar is leaning on a synthetic crutch.

**Ablation set: BUILT and scrub-verified** (`metrologist/ablation-q0/`,
`build_ablation_q0.py`): 6 instances, seeds 184213–184218 (fresh; no prior
references), same generator code, same 6 slices, T=56, **q_cycle=0**.
Full instance files (keys SEALED) + `ablation-chance-baseline.json` +
`ablation-build-summary.json` with sha256.

| seed | occ χ² | unsup χ² | keep | oracle | scrubbed? |
|------|------:|---------:|------|-------:|:---------:|
| 184213 | 6.4 | 18.6 | 42.21% | 0.904 | YES |
| 184214 | 0.8 | 8.6 | 47.01% | 0.929 | YES |
| 184215 | 8.8 | 12.9 | 44.34% | 0.914 | YES |
| 184216 | 1.3 | 222.5 | 47.10% | 0.911 | YES |
| 184217 | 2.6 | 35.6 | 45.91% | 0.919 | YES |
| 184218 | 3.8 | 26.6 | 46.61% | 0.919 | YES |

Occurrence-phase χ² at the noise floor (df=4, E≈4) on all 6 — the rhythm
is scrubbed; structure intact (1846 pairs, 96 groups, crib exactly once).
Note 184216's unsupervised χ² reads 222.5 while its occurrence χ² is 1.3 —
a live demonstration of the noisy detector (R7-adjacent): the contactor's
number is not the rotation.

**Pre-registered ablation criterion** (for the Runner, post-freeze):
score the FROZEN rebuilt solver on BOTH the fresh set (q=0.5) and the
ablation set (q=0). The crutch verdict is the COMPARISON:
- rebuilt solver clears §4 on fresh AND its primary/secondary do not
  materially degrade on the scrubbed set → phase machinery is not
  exploiting the synthetic rhythm. PASS on this axis.
- rebuilt solver clears §4 on fresh but collapses on the scrubbed set
  (toward chance) → the rhythm is load-bearing. FAIL on this axis:
  report, do not silently pass; the Smith repairs the phase machinery,
  not the bar.

**Frozen-family reference** (from Task 3's `phase_ref_184101`): the frozen
184101 degenerate optimum re-scored with phase machinery disabled —
default total 3933.4; `no_phase` (gate→0, S_potts 1.74→0.00) total 3931.7;
`no_contact` (proposal-only flag) no change to a fixed assignment, as
designed. **The frozen exploit moves <2 nats out of 3933 when the phase
gate is killed — it is S_word-driven and phase-independent**, as D2
claims. This is the baseline: if the REBUILT solver's decode collapses
without the rhythm, that is new, rebuild-specific crutch behavior.

**Status note:** the Smith's central fix was killed under R2; the rebuilt
solver is not frozen. No full-strength rebuilt-solver runs until
re-delivery; the comparison above is the post-freeze protocol. A cheap
objective-level probe (planted-key decomposition under the rebuilt
objective, fresh-184201 vs scrubbed-184213, isolating S_potts/S_conc) is
queued for when the ablation set is adopted.

---

## Task 3 — D2 consistency across the original 6: COMPLETE

**Question:** is the CONTROL-FAIL verdict instance-lottery (the noisy
χ² detector reading 0.4–787 across instances) or solver-signal? The
verdict is robust iff the D2 failure mode — S_word-dominance, the
Aho-Corasick scoring-function exploit — holds on ALL 6 instances.

**Method** (`metrologist/d2_consistency.py`): per original instance
(184101–184106), re-derived under the FROZEN solver (md5-verified
`d30dae03…`; no annealing — install assignment + `_full_refresh`, exact):
- (A) the batch's ANNEALED best assignment — more precisely, the best
  restart's FINAL assignment (re-derivation reproduces `best['final']`
  to <1.5 nats; the recorded `best['best']` is the best total OBSERVED
  mid-trajectory, a few hundred nats higher — both are reported);
- (P) the PLANTED truth key (sealed; scoring/diagnosis only).
D2 holds iff (i) total(P) << total(A) (gap < −1000 nats) and
(ii) S_ac(A)/S_ac(P) > 5. D3 bonus: n_poly(A) >> 6.

**Results** (full decompositions in `d2_consistency_results.json`):

| seed | total(P) | total(A final) | total(A best-obs) | gap | S_ac(P) | S_ac(A) | S_ac ratio | n_poly(A) | D2 |
|------|---------:|---------------:|------------------:|----:|--------:|--------:|----------:|----------:|:--:|
| 184101 | −6960 | 3933 | 4127 | −10893 | 768 | 13357 | 17.4× | 60 | ✓ |
| 184102 | −6751 | 4142 | 4348 | −10893 | 477 | 12791 | 26.8× | 60 | ✓ |
| 184103 | −6630 | 4613 | 4815 | −11243 | 588 | 13740 | 23.4× | 59 | ✓ |
| 184104 | −7112 | 4430 | 4444 | −11542 | 514 | 13867 | 26.9× | 61 | ✓ |
| 184105 | −6934 | 3815 | 4460 | −10749 | 588 | 12441 | 21.1× | 60 | ✓ |
| 184106 | −6848 | 4661 | 4773 | −11509 | 475 | 13263 | 27.9× | 59 | ✓ |

**D2 holds on all 6.** The failure mode is consistent: planted truth
scores ~11,000 nats worse than the degenerate optimum under the solver's
own objective (misalignment, criterion i), while the Aho-Corasick term
rewards degenerate repetition 17–28× above real French (criterion ii),
and polyvalence runs away to 59–61 islets vs 6 planted (D3, also
consistent). The S_ac ratios dwarf the noisy-detector spread: the
unsupervised χ² lottery (0.4–787) does not touch this verdict —
**the CONTROL-FAIL is solver-signal, not instance-lottery.**
Method note for the record: re-derivation targets `best['final']`
(the saved assignment), not `best['best']` (best observed mid-run).

---

## Task 4 — Fresh-seed hygiene: COMPLETE

- Fresh seeds 184201–184206 appear ONLY in the rebuild control's build
  tooling (`control/generator.py` seed list, `seal_meta_leak.py`,
  `build_rebuild_instances.py`/log) — never in solver code, configs,
  or diagnostics. Lane-wide re-grep (2026-10-07, final): zero `1842xx`
  references outside `code/side-homophonic-rebuild/`, and zero
  references to fresh/ablation seeds anywhere under
  `code/side-homophonic-rebuild/solver/`.
- The Smith's diagnostic rescoring (`solver/diag_rescore.py`,
  `solver/tools/anatomy.py`) is hardcoded to the ORIGINAL seed 184101
  and reads the ORIGINAL control instances — the fresh sealed keys
  have never been opened by the Smith's tooling.
- The rebuilt `solver/solver.py` + `config.json` contain no seed
  references and no `SYNTHETIC-key` reads.
- Ablation seeds 184213–184218: fresh; no prior references anywhere.
- Metrologist's own probes: in-memory only for the walk/ablation
  planning; keys persisted to disk only for the ablation set, under
  `metrologist/ablation-q0/` (sealed, Runner-scoring-only), plus the
  sealed `metrologist/sealed-pclasses.json` (planted truth, same
  handling as keys).

---

## Instrumentation caveats for the final verdict

1. **The χ² band is a genuine two-sided filter**, not a formality:
   draws fall outside on BOTH sides (184205 high @ 329.5; walk probe
   184208 low @ 175.6). Expect ~1-in-6 draws to need replacement;
   the replacement protocol (first in-band draw in seed order, logged)
   is part of the instrument.
2. **The contactor's unsupervised χ² remains a noisy detector**
   (fresh set: 5.1–336.4; originals: 0.4–787.3). It is NOT the
   calibrated quantity and must not gate anything — the calibrated
   quantity is the occurrence-phase χ², verified by independent
   re-derivation in Task 1.
3. **Raw `PARAMS['q_cycle']=0.55` is uncertified** (see ruling section):
   the certified 0.5 lives in the checkpoint/calibration files.
4. **Real R5005's 181.3 sits at the band floor** — per the Control
   Designer's bonus finding, it may itself be lucky clustering. The
   control tests solvers against rhythms in [181, 320]; transfer to a
   weaker real rhythm is an open question the q_cycle=0 ablation
   bounds from below.
5. **Plaintext-slice reuse**: the fresh set reuses the original 6 Les Mis
   slices (idx 0–5; the generator maps seed-list position → slice). The
   failed control's solver saw these slices' cts — but never the fresh
   keys/planted assignments, and the rebuild is a new objective. Noted,
   not blocking.
6. **184205 quarantine**: its files/chance entry must be moved out of
   the scorable set before the Runner scores (see Runner instructions).
   An out-of-band instance left in the directory is a scoring hazard.
