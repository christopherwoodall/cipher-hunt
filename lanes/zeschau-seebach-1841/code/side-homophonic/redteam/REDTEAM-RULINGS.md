# RED TEAM RULINGS — Seebach homophonic-solver side fleet

**Red team:** kill authority over the control design, the solver's feature
choices, and any claimed recovery.
**Date:** 2026-10-07. **Status of the lane at ruling time:** the control
batch is IN FLIGHT (launched 2026-10-07T15:20:29Z, 2/6 instances running);
no recovery has been claimed yet. The solver code was being edited DURING
this review (solver.py 15:24:46Z and 15:29:49Z; METHOD.md 15:22:55Z;
config.json 15:26:12Z) — rulings cite the versions below.
**Supplement:** two cross-fleet memos folded in 2026-10-07 ~10:45 CDT
(KILL-3, CONCERN-9/10/11, UPHELD-12 at the end).

## Version manifest (what was ruled on)

| file | mtime (UTC) | md5 |
|---|---|---|
| control/generator.py | 15:11:45 | (stable; rebuilt 184101 bit-identical) |
| control/CONTROL-DESIGN.md | 15:13:13 | — |
| control/chance_baseline.json, build_summary.json, calibration.json | 15:13:51 | — |
| control/instances/* | 15:13:51 | — |
| solver/solver.py | **15:29:49** | `37fcdd0e9f963a6d2022a6eb0754603b` |
| solver/METHOD.md | **15:22:55** | `2de6557c43f983dd0ef7f7358433f2ce` |
| solver/config.json | **15:26:12** | `93045d00153d3cc2ed6d55bbbc774bbb` |
| solver/control_harness.py | 15:09:06 | (stable) |
| solver/phase.py | 15:00:34 | (stable) |
| solver/phonetics.py | 15:13:22 | (stable) |
| solver/build_lm.py | 14:58:12 | (stable) |

An earlier solver.py (read ~15:17Z) lacked the S_conc machinery; an
intermediate (15:24:46Z) had S_conc bookkeeping not yet wired to
`total()`/`DEFAULTS`. The current code's `--self-test` PASSES
(max err 2.2e-11 over 300 random moves). Sealed keys were read ONLY for
verification (ceiling/rank/purity/determinism quantification); nothing was
fed back to the solver.

---

## KILLS

### KILL-1 — The harness gate enforces the wrong bar (both directions)

`solver/control_harness.py:49-56` (`BARS`) and `:163` gate on the Smith's
**superseded proposal** — pins 7/7; PRIMARY ≥ 0.50; PRIMARY ≥ chance+0.30;
islets ≥ 4/6; best−random20 ≥ 200 nats; MRR ≥ 0.60 — not the Designer's
**registered** bar (`control/CONTROL-DESIGN.md` §4: "this document is the
registration"): PRIMARY mean ≥ 0.20 / min ≥ 0.10; SECONDARY mean ≥ 0.30 /
min ≥ 0.22; both means ≥ μ_chance+5σ. METHOD.md §7 admits
"CONTROL-DESIGN.md finalizes", but the harness was never updated.

Mechanism of failure, both directions:
- **False negative:** a solver with primary mean 0.30 FAILS the harness
  (0.30 < 0.50) but PASSES the registration (0.30 > 0.20).
- **False positive:** the harness checks NO secondary metric at all, does no
  6-instance aggregation (mean/min), and never evaluates the μ+5σ
  conditions. A solver with primary 0.55 and secondary 0.15 would read
  CONTROL-PASS from the harness and FAIL from the registration.

The in-flight batch (`solver/run_all_controls.sh`, launched 15:20:29Z) scores
through this gate: its CONTROL-PASS/BROKEN-ON-CONTROL labels will be wrong
even if its per-instance numbers are right.

**Resurrect:** rewrite `gate()` to implement §4 exactly, plus a 6-instance
aggregation (means/mins); keep islets/MRR/margin as diagnostics, not gates.
The batch's per-instance metrics remain usable for re-derivation.

### KILL-2 — The registered SECONDARY metric cannot be computed

CONTROL-DESIGN.md §4 defines SECONDARY as "decode accuracy, all 1846 pairs
(anchors given, auto-correct)"; §4's justification derives the 0.30 bar from
it (0.143 + 0.20×0.857 ≈ 0.314). §2.4/:92 promises "per-position ground
truth (planted cell recorded)". But `control/generator.py::write_instance`
persists `'key'` + `'group_phase_diagnostic'` to the sealed key file and
**drops `'planted'`** (it exists in memory — `generator.py:483` — and feeds
the chance baseline at `:587`, but is never written).

`control_harness.py:15` admits the fallback: SECONDARY is a *proxy* —
"frequency-weighted primary agreement per position (proxy: per-position
planted cells are not persisted by the generator)". `score_assignment`
computes it as `hit += prim_hit[g]` per position: a **deterministic reweight
of PRIMARY**, carrying zero independent information and never exercising the
v2/E-step polyvalence machinery — the only thing the registered secondary
tests beyond primary.

**Resurrect:** deterministic rebuild (verified: rebuilt seed 184101 from
`generator.py` → pairs bit-identical to the shipped file), append
`'planted'` per position to the six sealed key files, score true decode
accuracy. Until then, **no PASS verdict is registrable** — the §4
conjunction cannot be evaluated as written.

---

## DEMOTIONS

### DEMOTE-1 — Phase calibration is generator-internal, not solver-observable

CONTROL-DESIGN.md §3 certifies `q_cycle=0.5` by **occurrence-phase** χ² ∈
[181,320] (per-instance 181.2–272.1; `calibration.json` in_band=True —
verified). But the only phase quantity the solver observes —
`solver/phase.py::reference_chi2`, a verbatim copy of the generator's
`unsupervised_chi2` and the exact function driving the Potts gate — reads
**36.6, 0.4, 787.3, 375.5, 6.2, 2.9** (`build_summary.json`): in-band on
**0/6** instances. Gate = σ((χ²−80)/12) ≤ 0.026 on 4/6 → the Potts prior is
OFF on most instances; the 2 instances where it is on (184103: 787,
184104: 375) over-read *above* the calibration band.

The Designer handed me the ammunition (`report_inbox/
control-designer-control.md`): the pipeline is a noisy detector (0.4–787 on
synthetic with true rotation at 181–272). I verified the deeper claim
independently: planted-phase Jaccard purity is **0.62–0.66 (non-anchor) on
all six instances regardless of the χ² reading** — the underlying contact
coherence is constant; the coin-flip lives in the clustering step.

Demoted: the difficulty table's "phase rhythm ≥" row and METHOD.md §5's
"R5005 and the control → gate ≈ 1" (false for the control on 4/6). What the
control actually certifies: contact-coherent aliasing at fixed strength,
which the solver's Jaccard proposal machinery faces on all 6 instances.
What it does NOT certify: the Potts prior's weight/gating — untestable here
on 4/6 instances.

Fix: (a) restate the claim as above; (b) note `--no-phase` only zeroes the
gate, not the contact proposals (`solver.py::build_solver`: `phase_info =
dict(phase_info, gate=0.0)`; adjacency still drives the 20% homophone-pool
proposals and block moves) — add `--no-contact` to isolate the Jaccard
machinery; (c) if the Potts weight must be validated pre-R5005, build a
phase-coherent variant with unsupervised χ² in-band (hard per the
Designer's documented attempts).

### DEMOTE-2 — The primary metric's ceiling is ~0.55, not ~1.0

The §4 justification ("0.20 primary = 9.3× chance") implicitly assumes
exact-string recovery is achievable to 1.0. Measured on the sealed keys:
- **29–34 of 54–55** planted distinct cells per instance share a projected
  form with another inventory value (the solver's S_char/S_word are blind
  to these distinctions *by design* — e.g. 'té'→'te' vs 'te', 'pas'→'pa' vs
  'pa');
- **3–7 of 89** groups per instance have planted cells entirely absent from
  the 288-item inventory (184101: vê×2, té, né, vres, my — Les Mis /
  ear-noise forms missing from the Tocqueville-derived top-200).

Expected primary under PERFECT phonetic inference: **0.526–0.601**
(1/K per colliding group, 0 for missing, 1.0 for unique-projection).
The Smith independently flagged this ("25/67 pilot truth cells share a
projected form" — `report_inbox/solver-smith-method.md` Caveats).

The 0.20 bar is therefore ~36% of the solver's achievable ceiling — a
stiffer gate than advertised, but still valid (far above chance, below
ceiling). **The bar is UPHELD; the interpretation is demoted.**
Require the Runner to report projection-equivalent recovery alongside
exact-string (diagnostic), so correct phonetic recoveries aren't misread as
failures.

### DEMOTE-3 — "Covers the Designer's planted inventory" → ~94% of planted groups

METHOD.md §1(c)/§6. Measured: 3–5 distinct planted cells per instance
(3–7/89 groups) are NOT in the extended inventory. The misses are
register-gap artifacts (Les Mis / noise-form cells absent from the
Tocqueville top-200) — **conservative** (harder control), not an easiness.
Hygiene: UNITS carries 2 duplicate entries ('que','qui'; 180→178 distinct),
inherited by the solver inventory (288→286), doubling those values'
proposal weight. Demote the claim; keep the inventory.

### DEMOTE-4 — "0.22 min = 1.5× chance" is 1.30× on the hardest instance

`control/chance_baseline.json`: per-instance secondary chance reaches
0.1687±0.0166 (184101; anchor coverage 14.7%). z(0.22)=3.09,
P(one null draw ≥ 0.22) ≈ 1.0e-3. The Designer's "1.5×" uses the average
chance (0.1434). The secondary-min bar is the softest of the four
inequalities — though non-binding in practice (any solver clearing primary
0.20 has expected secondary ≈ 0.143+0.20×0.857 ≈ 0.31).

---

## CONCERNS (mechanism + settling experiment)

### CONCERN-1 — Anchor coverage 14.7% on 184101 (+32% vs real 11.1%)

Measured per-instance anchor coverage: 0.147, 0.124, 0.107, 0.123, 0.120,
0.109 (real: 204/1846 = 0.111, `SYNTHETIC-meta-*.json`
`anchor_freqs_real_R5005`). Mechanism: anchors are hard pins; each anchor
occurrence is known-plaintext context for the char LM. +32% more anchor
context on 184101 is a material easiness axis the difficulty table doesn't
discount (it counts anchors, not coverage).
**Settle:** mask random anchor occurrences to 11.1% coverage on 184101 and
re-run; if primary drops > 0.05, harden the control (resample the slice).

### CONCERN-2 — Pilot-tuning / adaptive overfitting; method never above chance

The Smith's three patches — empty-projection guard; spanning-only S_word
(after 0/89 pilot); S_conc (after 2/89 pilot) — were tuned against the
Smith's own Les Mis pilot (`report_inbox/solver-smith-method.md`: "my own
labelled synthetic, Les Mis plaintext, 96 groups, 7 pins"). Pilot recovery:
0/89 → 2/89 (≈ chance 0.022). **The method has never demonstrated
above-chance recovery on any synthetic instance.** The pilot's disjointness
from the 6 control instances is unverifiable from lane files; if the pilot
≈ the control distribution, the control is not an independent validation.
**Settle/require:** (a) Smith attests pilot seeds/slices are disjoint from
the 6 control instances; (b) FREEZE the method now — no more pilot-driven
patches before the control verdict; (c) single-use control: any
post-control patch faces FRESH instances (new seeds; the generator is
deterministic), or the bar is being tuned to the test.

### CONCERN-3 — Version skew: the running batch tests a superseded artifact [LIVE]

Batch launched 2026-10-07T15:20:29Z (`runs/control_batch.log`);
solver.py/METHOD.md/config.json modified 15:22–15:29Z (S_conc wired into
`total()`/`DEFAULTS`/snapshot/self-test at 15:29:49Z; `+conc_cap`/
`+lambda_conc` in config.json at 15:26:12Z). The in-flight batch does not
test the current method. (An intermediate 15:24:46Z solver.py had S_conc
bookkeeping not yet wired to `total()`/`DEFAULTS` — a run against it would
have crashed or tested the wrong objective; the current code's self-test
passes.)
**Settle:** record the tested code's md5 with every batch; re-run the batch
on the frozen current code if the method changed materially; treat the
in-flight batch as a pilot result, not the registered verdict.

### CONCERN-4 — `--no-phase` doesn't ablate the contact proposals

`build_solver`: `if no_phase: phase_info = dict(phase_info, gate=0.0)` —
only β is zeroed; the Jaccard adjacency still drives the 20%
homophone-pool proposals and block moves. The ablation matrix cannot
isolate the contact graph's contribution.
**Settle:** add `--no-contact` (uniform proposals, no block moves) to the
Runner's ablation matrix.

### CONCERN-5 — The bar's validity is conditional on the register gap

Frequency-rank-match with Tocqueville cell frequencies: **0.000–0.034**
(≤ chance) — the gap neutralizes the shortcut. But oracle rank-match with
the slice's own frequencies: **0.079–0.191** (184105: 0.191 ≈ the 0.20
bar). The generator's frequency-weighted dealing plants a real rank signal;
only the register gap keeps it from the solver. If the reference corpus is
ever improved toward the plaintext register, the bar must be re-baselined.
Containment holds: the harness asserts Tocqueville-only LM (`'mis' not in
corpus`). Keep it.

### CONCERN-6 — Sealed-adjacent metadata in the open

`SYNTHETIC-meta-<seed>.json` contains `'polyvalent_groups'` — the 6 islet
group labels (184101: 26, 52, 84, 85, 95, 99) — plus full generator PARAMS:
genuine key-adjacent material in a file the Runner protocol doesn't
explicitly seal (CONTROL-DESIGN.md §8 excludes it by "ONLY", but its
"diagnostics" purpose invites sharing). The harness never reads meta/
(verified) — no active leak.
**Settle:** move `polyvalent_groups` + `params` into sealed storage, or
explicitly seal `meta/` in the Runner protocol. (The sealed key file's
`group_phase_diagnostic` is properly sealed with the key.)

### CONCERN-7 — Hyperparameter provenance unverifiable

METHOD.md §8.4: "defaults from a toy pilot, not tuned on the control". No
pilot artifact in the lane; unverifiable from files. Ties to CONCERN-2.

### CONCERN-8 — Literary vs diplomatic register (residual)

The control tests register-gapped *literary* French (Les Mis 1862); the
target is register-gapped *diplomatic* French (1841 despatch). The gap
direction relative to Tocqueville is unmeasured. No experiment available
without a period diplomatic corpus. Noted, not blocking.

---

## UPHELD

- **U1 — The 6-instance luck math.** Primary mean ≥ 0.20 is ~28σ above the
  random-permutation null (SE of the 6-instance mean ≈ 0.0063, from
  `chance_baseline.json` per-instance sds); min ≥ 0.10 is ~5.1σ per
  instance (P ≈ 1.7e-7 each). The §4 conjunction's false-pass rate under the
  null is negligible (dominated by min-primary: ~1e-42 under normality).
  The §4 floors 0.098/0.227 recompute exactly as μ+5σ. **6 instances
  suffice** — the residual risk is null misspecification, not n (the
  rank-match channel was tested and refuted: 0.000–0.034).
- **U2 — Les Mis as the hardness choice.** Tocqueville-rank-match scores at
  or below chance, so the register gap is real and load-bearing; the
  round-3 failure mode (in-distribution Tocqueville-t2 control) is not
  repeated. The Designer's F10-motivated choice is corroborated by
  measurement, not just argued.
- **U3 — SA as the method choice.** Round-1's z=+17.7 confident-wrong
  convergence (`code/crowd/annealer_results.md`) proves the sampler
  explored and the objective failed — "the failure was the objective, not
  the sampler" is evidenced, and the scorer-smith's N12 diagnosis
  (consistent-but-not-distinctive) is the right target. The new objective —
  char-5-gram on phoneticized decode + spanning word bonus + contact Potts
  + polyvalence E-step — is genuinely new machinery addressing the
  diagnosed gap (letters were inexpressible; bigram contexts
  underdetermined), not the round-1 annealer with new paint. Many-to-one
  collapse is blocked structurally (periodic decodes have no French
  5-grams; S_conc penalizes concentration over projected values).
- **U4 — Phonetic classes.** Evidence-graded (SOLID/PROVISIONAL per the
  `phonetic_rules.md` legend), applied identically to corpus/lexicon/
  inventory/decode, 42 anchored self-test cases pass (`python3
  phonetics.py`), and the two found attractors (empty projection → vowel
  guard + never-empty belt-and-braces) were fixed principledly.
- **U5 — Soft priors.** Forced off on controls (`control_harness.run` →
  `no_soft=True`); the R5005 with/without robustness check is
  pre-specified (METHOD.md §2). No double-counting in the control verdict.
- **U6 — Negative control.** The round-1 syllable-bigram annealer scores
  0.034–0.045 (mean 0.041, ≈chance) on the 6 new instances
  (`runs/negative-control/negctrl_results.json`, verdict
  NEGATIVE-CONTROL-OK) — the control kills the old method as intended;
  "harder than R1's control" holds where it matters (bar 0.20 vs old
  method 0.04).
- **U7 — Generator determinism.** Rebuilt seed 184101 from
  `control/generator.py` → pairs bit-identical to the shipped file. The
  "deterministic (seeded)" claim verifies — and this is the KILL-2 fix
  path (regenerate `'planted'` per position).
- **U8 — Chance baselines.** Analytic + 2000-draw MC values trace:
  primary 0.0216±0.0153, secondary 0.1434±0.0167 per instance in
  `chance_baseline.json`; the Designer's summary numbers are exact
  averages.
- **U9 — No-syllabifier-in-scorer (F30).** The scorer never syllabifies the
  decode; the rule syllabifier builds only the candidate inventory (a word
  list, never a conditional model). The i/e letter-rate fidelity gap is the
  documented F30 mirror and conservative.
- **U10 — Bookkeeping.** `solver.py --self-test` PASSES on the current code
  (max err 2.2e-11 over 300 random moves): the incremental objective
  (S_char, S_ac, S_single, S_conc, S_potts) is exact, including the new
  spanning-only and concentration terms.
- **U11 — The noisy-detector enlightenment, independently verified.**
  Planted-phase Jaccard purity 0.62–0.66 (non-anchor) on all six instances
  while the unsupervised χ² reads 0.4–787: the χ² coin-flip is a
  clustering artifact, and the contact structure the solver's proposal
  machinery uses is equally strong on all six. This corroborates the
  control's contact-coherence axis even as DEMOTE-1 demotes the gate.

---

## ATTACK 3 — claimed recovery: NONE YET

No `result.json`/`control_report.json` exists; the batch is in flight (2/6
started ~15:20Z). When it lands (or on re-run), the verification protocol:

1. **Re-derive scoring independently.** Re-open the sealed keys; recompute
   PRIMARY (exact, 89 non-anchor groups) and projection-equivalent recovery
   per instance from the batch's `result.json` assignments; check the
   harness's arithmetic.
2. **Apply the REGISTERED §4 bars** with 6-instance aggregation
   (mean ≥ 0.20 / min ≥ 0.10; mean ≥ 0.30 / min ≥ 0.22; means ≥ μ+5σ) —
   never the harness's `gate()`.
3. **Leakage audit.** `result.json` meta must show the 7 pinned anchors,
   `no_soft`, Tocqueville-only LM; the solver must not have read key/meta
   files (the harness code path is clean: `load_synthetic` skips `#`
   comments; truth enters only in `score()`; only `['anchors']` is taken
   from the crib file — the disclosed `crib_pair_offset` is unused by the
   solver). The Smith's inventory choice (encipher_split cells) is method
   knowledge from the Designer's notes, not instance leakage — the
   inventory is built from the reference corpus, never from control data.
4. **KILL-2 blocks any PASS**: the secondary bar is unverifiable until
   `'planted'` is persisted. A "PASS" before that is unregistrable.
5. **Version check**: confirm the tested code's md5 matches the frozen
   method (CONCERN-3) — the in-flight batch predates the S_conc wiring.

## Resurrection summary

| ruling | fix |
|---|---|
| KILL-1 (wrong gate) | rewrite `gate()` to §4 + 6-instance aggregation; re-derive |
| KILL-2 (secondary uncomputable) | deterministic rebuild → persist `'planted'` → true decode accuracy |
| KILL-3 (inventory circularity) | crib-derived inventory core + re-run; or explicit scope limitation on PASS |
| DEMOTE-1 (phase calibration) | restate claim (contact coherence certified; gate not validated); add `--no-contact` ablation |
| DEMOTE-2 (ceiling ~0.55) | keep the bar; report projection-equivalent recovery alongside |
| DEMOTE-3 (inventory ~94%) | documentation fix |
| DEMOTE-4 (1.5× → 1.30×) | documentation fix |
| CONCERN-1 (anchor coverage) | masking experiment on 184101 |
| CONCERN-2/7 (pilot-tuning) | freeze + disjointness attestation + single-use control |
| CONCERN-3 (version skew) | md5-tagged batches; re-run on frozen code |
| CONCERN-4 | `--no-contact` ablation flag |
| CONCERN-5 | keep LM Tocqueville-only; re-baseline on any reference change |
| CONCERN-6 | seal `meta/` or move `polyvalent_groups`+`params` to sealed storage |
| CONCERN-8 | noted residual; no action available |
| CONCERN-9 (stale parse docs) | update RUN-PROTOCOL.md + runner-results.md to record completed verification |
| CONCERN-10 (crib_attack landmine) | pin the label source or repoint with rebuild-and-verify |
| CONCERN-11 (χ² anchor superseded) | cross-fleet: crowd re-runs contactor on repaired parse; Designer re-anchors or disclaims |

---

## SUPPLEMENT — cross-fleet memos (folded 2026-10-07 ~10:45 CDT)

Memos: `code/crossfleet/memo-crib-inventory-to-homophonic.md` (inventory
circularity), `code/crossfleet/memo-parse-repair-to-homophonic.md` (parse
repair). Each attacked below; the Smith's fixes are assessed against the
precondition standard (a fix that doesn't fully close the surface is named
as such).

### KILL-3 — Inventory circularity: a control PASS is not registrable as R5005-readiness on the inventory axis

The solver's value inventory (`solver/solver.py::load_inventory`: UNITS
verbatim + top-200 `encipher_split` cells from Tocqueville) and the
control's planted units (`control/generator.py`: top-T `encipher_split`
cells from the Les Mis slice + parametric ear noise) derive from the SAME
rule syllabifier (`code/crowd2/scorer_smith.py`). The control therefore
**assumes the inventory family it would need to test** — a pass validates
inference *conditional on* inventory adequacy, never the adequacy itself.

This is not hypothetical: the word-pattern fleet's F34/N32 is direct
real-cipher evidence the family is wrong — the known "première" tail
@1035–1038 (82-34-29-40, four pencil-crib anchors, 'm' standalone, which is
phonotactically impossible in French but real here) returns ZERO candidates
in a standard-French syllabified lexicon. N29 (word-pattern red team)
independently suspects `data/upstream-syll*.py` is not the encipherer's
table ("all three annealers failed on it"): the inventory must be learned
from cribs, not adopted upstream.

Audit of the generator (memo Action 1) — measured on the sealed keys:
- The generator DOES plant letter-tier by-ear-style chunks: **9–11 distinct
  standalone single letters per instance** as non-anchor primaries
  (a,c,d,l,n,t,u,s,o,r,j,y,à,é) via `encipher_split` (p_letter_split=0.03),
  and the solver's inventory covers them. The 'm'-standalone *shape* is
  represented; the control is not circular on the letter tier.
- What it cannot plant is the real encipherer's *systematic* by-ear
  chunking: the generator's "by-ear" is parametric noise (mute-e 0.15,
  merge 0.10, split 0.05, alt 0.08) on rule-syllabified units. The solver's
  tolerance (phonetic projection) is validated only against the generator's
  noise guess, not the real habit. (The F34/N32 falsification targeted a
  syllabified-lexicon instrument; the solver's character-stream scorer with
  a letter tier is a different instrument — but the value-inventory family
  is shared, and that is what the control cannot test.)

The Smith's fixes do **not** close this — stated explicitly: METHOD.md §6
and the `--inventory-mode units` ablation vary the inventory WITHIN the
standard-French family; no ablation can detect family-level inadequacy.

**Preconditions for a registrable PASS** (memo Actions 2+3): (a) build the
crib-derived inventory core (7 pencil cribs' attested chunks —
pre|m|i|er|e, la, que — plus the frenchman by-ear evidence) and re-run the
control with the solver using it; or, minimum, (b) carry the explicit scope
limitation on any PASS verdict: *"validates inference conditional on
inventory adequacy; inventory adequacy for the real by-ear chunking is
untested and independently doubted (F34/N32, N29)."*

### CONCERN-9 — Stale parse docs still forbid the verified adapter

`runs/RUN-PROTOCOL.md` ("Loader gate (HARD)") and
`report_inbox/runner-results.md:13` still declare `solver/ct_loader.py`
STALE (reads `data/upstream-offsets.json`, asserts 1846) and forbid running
it. Both statements are now false and operationally blocking.
**Fix:** update both docs to record the completed repointing and the
byte-level verification below.

### CONCERN-10 — `crib_attack.py` still feeds the control generator old-parse labels

`code/crib_attack.py:38` uses `data/upstream-offsets.json`;
`control/generator.py::real_group_labels` imports it and asserts
(1846, 96). Measured: the 96 label SETS are identical old-vs-new (31 groups
shift frequency ±1–2; +1 pair total) — no live corruption. But if key-hunt
updates `crib_attack` to the repaired parse, the control rebuild breaks
(the assert fires): a landmine with a loud trigger.
**Fix:** pin the label source (comment + label-set assert) or repoint with
rebuild-and-verify.
Fidelity note: the control's "crib reads EXACTLY ONCE" invariant was modeled
on the old "exactly once @1033" belief; the repaired parse has "la première"
twice (@754, @1034). Synthetic design choice, immaterial to validity.

### CONCERN-11 (cross-fleet) — the phase calibration anchor is superseded

Measured with the verbatim instrument (`solver/phase.py::reference_chi2`)
on the repaired-parse stream: R5005 unsupervised χ² = **366.3** (blocks
A32/B27/R20/C17), vs 181.3 on the old parse
(`code/crowd/contactor_results.json`). The control's band [181, 320] was
justified as "[real, 1.8× real]" from 181.3 — it does not contain the
current measurement, and the difficulty table's "1.3× real" is stale.
Given DEMOTE-1 (a one-pair flip + rephasing moves this instrument 2× — it
is a coin flip, not a ruler), the correct response is NOT "recalibrate to
366" but to disclaim the unsupervised anchor: the occurrence-χ²
calibration stands mechanically, but its claimed relationship to reality
is void until the crowd fleet re-runs the contactor on the repaired parse.
**Fix (cross-fleet):** crowd re-runs contactor on the repaired parse; the
Designer re-anchors the band or explicitly disclaims it.

### UPHELD-12 — Parse-repair repointing, verified byte-level

The memo's gap is **closed**. `solver/ct_loader.py` reads
`code/side-keyhunt/repaired_offsets.json`, asserts `a5_03 == 0`, expects
1847 pairs / 96 groups, and verifies both crib landmarks. Executed just
now: `R5005: 1847 pairs, 96 groups → landmarks 11-70-82-34-29-40 @754 and
@1034: VERIFIED`. `repaired_offsets.json` md5
`40521e174deaa2bfbc179443283c615e` matches the protocol's pinned md5.
The 1846-pair synthetics remain self-consistent (the memo agrees); the
1-pair delta is immaterial to control difficulty. No solver/harness code
path assumes 1846 for real data (`solver.py` builds groups dynamically;
the harness's 1846 asserts apply to synthetics only; the Runner's post-gate
path is `ct_loader → write_pairs_json → solver --pairs`, all 1847-clean).
The Smith's fix fully closes the functional precondition; CONCERN-9/10 are
documentation residue.

**Tally after supplement: 3 KILL / 4 DEMOTE / 11 CONCERN / 12 UPHELD.**
