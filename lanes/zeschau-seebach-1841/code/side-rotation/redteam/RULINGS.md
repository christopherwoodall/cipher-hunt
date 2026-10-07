# RED TEAM RULINGS — Seebach rotation fleet (side-rotation)
Coordinator: rotation-fleet. Red-team word is law over every positive claim.
Governing battery: `code/side-rotation/prereg_falsification.md` (written 2026-10-07
~11:55 CDT — BEFORE any executor result merged). Rules R1–R6 therein are binding.

## Ruling R-0 — prereg-first compliance (2026-10-07)
`prereg_falsification.md` (K1–K5 falsification battery for the column-geometry
hypothesis H_col, with kill/strengthen thresholds, exact statistics, and the
DEAD decision rule) was written at 16:55 — before the Rhythmicist's PREREG
(16:56), the Phonetician's prereg (16:56), and the Geometer's prereg (16:56+).
No executor result had merged at that time. The fleet's own preregs were each
written before their computations ran (verified by timestamps + absence of
result files at prereg time). PREREG-FIRST: SATISFIED.
Correction to the Geometer's prereg cross-cutting note: it claims
"code/side-rotation/prereg_falsification.md named in the work order does not
exist" — it EXISTS (written first, above). The work order's naming was honored;
the note is stale. No claim impact; recorded for traceability.

## Ruling R-1 — Phonetician CV-structure battery: NULL, accepted (2026-10-07)
Results `code/side-rotation/phonetician/phonetician_results.json` (6 tests).
Red-team re-derivation: INDEPENDENT Freeman-Halton exact implementation
(fixed margins, Fisher probability-definition, full enumeration) — 6/6 p-values
reproduce to <1e-6 (T-Pa 0.2500, T-Pb 0.3465, T-Pc 0.7752, T-Pa2 0.024242,
T-Pa3 0.068681, T-Pc2 1.000000). Phase assignments (16 groups) verified against
`code/crowd4/phase_map_repaired.json` — all match; no R among the 16.
Pre-registration compliance: PASS — statistic/baseline/threshold pre-stated;
exact tests at small n (R3); Bonferroni α/3 rule pre-stated; power honestly
reported; the one hand-tabulation correction was caught and disclosed
pre-execution with a script assert.
Verdicts under the phonetician's own pre-registered decision rule:
- T-Pa, T-Pb, T-Pc (primaries): NULL (p=0.25/0.35/0.78). KILLED as stated.
- T-Pa2 (GT+prov, n=11): p=0.0242 — nominally <0.05 but FAILS the pre-registered
  Bonferroni bar (0.0167) and is a robustness variant, not a primary test.
  → NULL by rule, NOT a survival claim. The direction (3 closed units avoid
  phase B: 82=m in A; 29=er, 96=par in C) sits at the floor of detectability
  with n=3 closed units; the phonetician's own min-p/power framing keeps this
  honest. No promotion, no lead-grade claim.
- T-Pa3 (p=0.069), T-Pc2 (p=1.0): NULL.
Net: finer phonetic structure shows NO phase association on any subtest. This is
the n=16 partial implementation of the falsification battery's K4 (arbitrariness
leg); the full K4 (n=23, category-coherence permutation) remains the Geometer's
or a later executor's to run — or the red team's own verification pass.
Nothing positive merges from this battery.

## Ruling R-2 — Rhythmicist PREREG: compliance PASS with one required amendment
`code/side-rotation/rhythmicist/PREREG.md` (written pre-computation): T0 gate,
WO1b labeling-robustness (5 variants, conjunctive pass rule, fragility bar
0.85), WO2 phase-lock (pooled decision test A α=0.05 + descriptive B/C, both
interpretations pre-registered), WO3 HMM-vs-bigram (contiguous split, 11
restarts, ΔBIC>10 + held-out LL both required), old-vs-new reconciliation side
result. Pre-registration discipline: PASS.
REQUIRED AMENDMENT (issued pre-computation — this is what prereg-first is for):
WO2 Test A (χ² GOF, 14 phrase starts, df=3) has expected counts
A=4.68 / B=4.29 / C=3.67 / R=1.36 (re-derived from the canonical loader +
banked map token marginals 0.3346/0.3064/0.2620/0.0969) — three of four cells
below 5. Per battery rule R3 the χ² asymptotic is VOID here. Test A MUST use an
exact multinomial GOF (or Freeman-Halton 1×4) before any decision is drawn;
otherwise Test A is descriptive-only. The 14 phrase-start counts are "asserted"
in the prereg — they must reproduce from the repaired stream before Test A runs
(gate item on results).
WO3 note: the ΔBIC>10 bar is strong; split outcomes (LL wins / BIC wins) must be
reported honestly per the prereg's own rule.

## Ruling R-3 — Geometer PREREG: compliance PASS with calibration notes
`code/side-rotation/prereg_geometer.md` (written pre-computation): T0 gate
(exact phase equality + χ²=366.3±1) — VERIFIED PASSING from `t0.json`
(exact match TRUE, sizes A=32/B=27/C=17/R=20, χ²=366.35). The lag-3 method
refinement (4-state z=+5.95 → ABC-bounded E1-exact obs=0.4219/exp=0.3529/
z=+5.61) was recorded as an amendment BEFORE WO1–3 ran; the M2 bar (z≥+3.0)
is unchanged. Amendment ACCEPTED as method refinement; gate item: WO3's M2
must use the ABC-bounded variant.
WO1 (number-range): Fisher exact MC 200k + Holm over {a,b} + Cramér's V≥0.40
+ coherent-layout-story requirement for SUPPORT. Maps to battery K1: the
geometer's SUPPORT bar is stricter than K1's strengthen bar (p<0.01 + coherent
story) — consistent; the geometer's decision rule governs their test.
WO2 (homophone cycling): Fisher's-method combination over 06/52/94 + power
honesty (vacuous tests labeled "untestable", not null) + 78-vs-43 secondary
fenced as lead-only. Maps to battery K2. Compliant.
WO3 (clerk simulation): 6 pre-registered behaviors, fixed parameters, 20
replicates, median match criteria (M1≥200, M2 z≥3.0, M3<0.8) + bridge check
(adjusted-Rand ≥0.5 of derived phases vs true columns). Calibration note: these
bars are LOWER than the battery K3 DEAD-kill bars (χ²≥366.3 AND z≥4.5 jointly,
<5% of streams). WO3 is therefore a screening design: no behavior passing even
the lowered bars strengthens the K3-kill direction; a behavior passing WO3
survives screening but must still face K3's joint bars for any DEAD/SURVIVE
verdict. Also flagged: the WO3 table construction ("frequent syllables get
variants in all 3 columns; assignment balances column frequencies") is
pre-registered but will be audited on results for smuggled-in rotation; the
Tocqueville syllabifier choice is a caveat (F30-class instrument concern does
not apply to rate legs here, but the synthetic stream's repetition structure
feeds the comparison — watched, not blocked).

## Ruling R-4 — label-agreement discrepancy: RECONCILED (2026-10-07)
N37's "69/96 agreement" and N30's "61/96 change" are BOTH CORRECT — they measure
different things on the SAME two banked maps (contactor's old k=12 Jaccard
labels vs `code/crowd4/phase_map_repaired.json`), re-derived independently:
- 69/96 agree (27 change) = BEST-PERMUTATION agreement (6 ABC perms, R fixed;
  winning perm old→new {A→B, B→A, C→C, R→R} — the cycle reversal old
  A→C→B→A vs repaired A→B→C→A). This is the methodologically correct
  clustering-agreement number. N37 is right.
- 61/96 change (35 agree) = NAIVE IDENTITY agreement (no permutation). The
  contactor's label letters on the old parse sit in a different permutation
  than the repaired map's, so identity comparison mixes the permutation flip
  with genuine membership change. N30's figure is arithmetically right and
  methodologically misleading as stated.
CORRECTED FIGURE TO BANK: **69/96 agree at best permutation (27/96 = 28%
membership change)**. The run_r5005.py:68 comment ("61/96 groups change phase
under the repair") and all N30-derived prose should be corrected to the
best-permutation figure. The fragility is real but overstated by the naive
figure: 28% change at best perm, not 63.5%.
Full derivation: `code/side-rotation/redteam/agreement_reconciliation.md`.

## Kill ledger (append-only)
- 2026-10-07: Phonetician phonetic-structure hypothesis — NULL on all 6 subtests
  (T-Pa 0.25, T-Pb 0.35, T-Pc 0.78, T-Pa2 0.0242 fails pre-registered Bonferroni,
  T-Pa3 0.069, T-Pc2 1.0). No positive claim merges.
- 2026-10-07: N30 "61/96 change" figure — SUPERSEDED by 69/96 best-permutation
  (27/96 change). Naive-identity figure retired as the fragility headline.
- Pending: Geometer WO1/WO2/WO3 results; Rhythmicist WO1/WO1b/WO2/WO3 results;
  battery K4 full version (n=23 coherence permutation).
