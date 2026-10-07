# RED-TEAM RULINGS — Seebach homophonic-solver REBUILD fleet

Reviewer: red-team subagent (kill authority over "fixed" claims; the Runner
may not declare PASS without concurrence on the numbers).
Date: 2026-10-07. Scope: `code/side-homophonic-rebuild/` (read-only review;
this file is the only write).
Code under review: `solver/solver.py` md5 `f298c8fc…`, `solver/config.json`
md5 `de2c3fccd…`, `solver/crib_inventory.py` md5 `6ee86a775…`.
NOTE (version skew): the rebuild dir did not exist when this review started
and `config.json` changed mid-review (`lambda_poly` 20.0 → 50.0 between my
first read and the grep at `solver/config.json:10`). Rulings cite the md5s
above; if the Smith edits again, re-verify.

## Independent gate re-derivation (frozen batch, seeds 184101–184106)

Recomputed from raw artifacts with my own script (`/tmp/rt_gate_rederive.py`;
no solver/harness imports): per-instance primary/secondary from
`runs/{frozen-ctl-*,run3-*}/result.json` best assignments × sealed keys ×
`planted` lists. Report-internal consistency also checked
(`per_group_primary` sums = `primary_hits`, n_nonpin=89, pins=7).

| seed | primary | secondary |
|---|---|---|
| 184101 | 0.0000 | 0.1473 |
| 184204 | 0.0112 | 0.1387 |
| others | 0.0000 | 0.1073–0.1241 |

- primary mean **0.0019** (bar 0.20), min **0.0000** (bar 0.10)
- secondary mean **0.1244** (bar 0.30), min **0.1073** (bar 0.22)
- μ+5σ: chance baselines pooled = 0.0216±0.0153 / 0.1434±0.0167 →
  floors **0.098 / 0.227** exactly as registered. All six §4 checks FAIL.
- Byte-exact match to the Runner's numbers in
  `../side-homophonic/runs/CONTROL-VERDICT.json`. Fresh-seed
  (`control/chance_baseline.json`, 184201–184206) pooled floors:
  0.0993 / 0.2266 — registered floors still valid.

## Rulings

### R1 — UPHELD: frozen CONTROL-FAIL numbers verified
The Runner's gate numbers re-derive byte-exact from raw artifacts with
independent code. CONTROL-FAIL stands on all six §4 checks. No PASS claim
exists or is registrable on the frozen method.

### R2 — KILL: the "D2 fixed" claim (new S_word does not flip the optimum)
The Smith's diagnostic proof was re-run with MY OWN code (independent
Aho-Corasick-equivalent coverage scorer, own E-step loop, own objective
assembly — `/tmp/rt_new_objective_test.py`), then confirmed against the
Smith's rebuilt machinery itself (read-only scoring of fixed assignments,
`/tmp/rt_new_objective_smithcode.py`, `/tmp/rt_planted_old.py`).
Same-instance comparison, seed 184101, under the NEW objective
(`solver/solver.py:517-541` `_cover_sum`; `solver/config.json:10`
`lambda_poly=50.0`):

| decode | S_word (new) | S_char | penalties | total |
|---|---|---|---|---|
| PLANTED truth | 676.6 | −7,592.9 | −300 (6 islets) | **−7,215.7** |
| FROZEN degenerate best | 4,888.5 | −6,245.9 | −3,230 (60 islets + conc) | **−4,585.6** |

The fully-wrong degenerate key still outscores the planted truth by
**+2,630 nats**. The fix cut the margin 4.2× (was +11,062 under the frozen
objective — itself re-verified: my −6,934.4 vs the runner's −6,959.9, 0.4%),
but did NOT flip the optimum ordering. An annealer maximizing the new
objective still prefers the degenerate basin over truth. By the brief's
criterion ("if the true decode doesn't win, the fix is cosmetic"):
the fix is insufficient — KILLED as a "fixed" claim. The residual margin
decomposes to ΔS_word +4,212 and ΔS_char +1,347 against penalties −2,930:
the char-5gram's salad preference (pilot-measured) and the per-char
`w_h/len_h` short-word bias both survive the rewrite.

### R3 — CONCERN (not gaming): S_cov mechanism is synthetic-agnostic
`solver/solver.py:39-52,517-541`. The rewrite uses no Les Mis / Tocqueville /
generator-specific tuning: same lexicon, same weights, no generator
parameters enter. `--self-test` passes on the rebuild (incremental ==
full recompute, max err 1.06e-10, 300 moves). It is a general scoring
change that transfers — but see R2: general ≠ sufficient.

### R4 — CONCERN: lambda_poly 20 → 50 unjustified
`solver/solver.py:8` ("polyvalence runaway must hurt"); `solver/config.json:10`.
No tuning curve, no principled prior, and `solver/METHOD.md` (byte-identical
to the frozen doc) still documents the old regime. A value chosen to make
exactly-6 synthetic islets affordable while 60 spurious ones hurt is
tuning to the generator's `n_poly=6`/`p_poly_use=0.5`; R5005's true
polyvalence count is unquantified ("3 established"). Demand before any PASS:
document the selection criterion and show gate-verdict insensitivity
(e.g. λ ∈ {30, 50, 70}).

### R5 — CONCERN: the 5 inventory forms are truth-selected
`solver/crib_inventory.py:44-49` adds exactly the 5 forms missing on
184101 (`vê,tÃ©,nÃ©,vres,my` — the docstring is explicit that the
selection came from the sealed-truth diagnosis). `vres` (1/6 fresh truths)
and `my` (0/6) look like 184101-memorization; `vÃª`/`tÃ©` recur (5/6 each)
and are plausible by-ear French. Mitigating: the fresh seeds' missing
sets are DIFFERENT (`vait,je,dÃ©,rÃ©,lÃ `), so this patch cannot carry a
fresh-seed pass by itself — the fresh-seed protocol neutralizes the gaming
vector. Not a KILL, but the selection method stays on the record.

### R6 — UPHELD with correction: D4 inventory-gap closure
The 5 forms ARE in the rebuilt inventory (296 items; frozen↔rebuilt
parity verified in separate processes: diff is exactly the 5 forms).
But the ceiling is NOT 1.0 on the fresh control — exact-match ceilings
vs the rebuilt inventory: 184201 **1.0000**, 184202 **0.9775**,
184203 **0.9663**, 184204 **0.9663**, 184205 **0.9551**, 184206 **0.9663**
(missing: `vait,je,dÃ©,rÃ©,lÃ `). All still far above the 0.20 bar, so D4
remains non-gating; the binding ceiling stays the phonetic ~0.53–0.60
(prior DEMOTE-2), which no inventory patch moves.

### R7 — KILL: metrologist `band_check.py` is bugged (the check, not the instances)
`metrologist/band_check.py:31-40` recomputes the "occurrence-phase" χ²
from `key[g]['phase']` — the per-GROUP nominal phase. The generator's
statistic (`control/generator.py:713-725`) uses `pclasses`, the
per-OCCURRENCE diluted cycle positions. The check recomputes 1.0–12.9
against reported 183.2–329.5 and falsely flags ALL SIX instances
OUT-OF-BAND. Its verdicts are invalid; do not cite them. Further,
`pclasses` is not persisted in the sealed keys, so no independent
recompute from sealed artifacts is possible (provenance gap — same
class of issue as the old KILL-2; the generator is deterministic, so a
rebuild reproduces it, but the artifact trail has a hole).

### R8 — CONCERN: 184205 χ²=329.5 exceeds the pre-registered band
`PHASE1-VERIFICATION.md` table: 329.5 vs band [181, 320] (+3.0%),
re-stated in the rebuild's `control/CONTROL-DESIGN.md:104` (byte-identical
to the frozen registration). Direction is solver-helpful (stronger rhythm
signal). Do NOT re-roll the seed (selection bias is the worse sin).
Acceptable only with the Runner's written concurrence and an explicit
flag on any verdict that cites the 6-instance set.

### R9 — UPHELD: no R5005 key run
All scored runs are 1846-pair synthetic (`synthetic: true` in all six
reports). The rebuild has no `runs/` dir, no `ct_loader`, no real-data
default path (`solver.py` requires `--pairs`; `--pairs` seen only with
`solver_inbox/` synthetic files), no 1847-pair artifacts. R5005 mentions
are comments plus the gate rule (`solver/solver.py:18`: "Do NOT run on
R5005 until the control passes"). R5005 untouched.

### R10 — CONCERN: doc hygiene (5 items)
1. `solver/METHOD.md` is byte-identical to the frozen doc — still
   documents the OLD overlapping Aho-Corasick S_word (`METHOD.md:121-126`)
   and "3,420 words" (lexicon is 3,546). The D2/D3 changes live only in
   code docstrings.
2. `solver/solver.py:7` says "See REBUILD.md" — no such file exists.
3. `load_inventory` docstring claims parity "asserted by
   tools/check_inventory_parity.py" — that file does not exist
   (`solver/tools/` holds only `gen_inventory_data.py`). The parity claim
   itself verifies TRUE (R6), but the cited assertion is vapor.
4. The solver.py "METHOD (one line)" docstring still says "word-salad
   bonus (Aho-Corasick over the era lexicon)" — stale.
5. `solver.py` docstring inherits the runner's "S_ac 13,510 vs ~2,500";
   the ~2,500 does not reproduce — my independent rescore gives
   778.5 (184101) / 477.3 (184102) for the true decode's word term
   (the "15×" ratio itself reproduces: 14.9× S_word on 184101).

### R11 — PASS concurrence: WITHHELD
No PASS claim exists (the Runner has not run the fresh batch). I do NOT
concur in advance with any PASS on the current rebuild code: R2 shows the
objective still ranks a fully-wrong key +2,630 nats above truth, so the
annealer is expected to re-converge to the degenerate basin and I expect
CONTROL-FAIL on 184201–184206. The Runner may run the fresh batch as a
measurement; if its numbers clear §4 anyway, escalate for re-review —
a PASS against a provably misaligned objective needs extraordinary
scrutiny, not a rubber stamp.

## Tally
**2 KILL** (R2: "D2 fixed" claim; R7: metrologist band check) /
**0 DEMOTE** / **5 CONCERN** (R3 S_cov residual bias; R4 λ_poly
justification; R5 truth-selected inventory; R8 184205 band exceedance;
R10 doc hygiene) / **3 UPHELD** (R1 gate numbers; R6 inventory parity;
R9 no R5005 run). R11 withholds PASS concurrence (not a verdict).
Corrections banked: runner's true-decode S_word "≈2,500" → 779/477
(R10.5); "ceiling now 1.0" → 0.955–1.000 per fresh seed (R6);
mid-review `lambda_poly` 20→50 edit noted (header).
