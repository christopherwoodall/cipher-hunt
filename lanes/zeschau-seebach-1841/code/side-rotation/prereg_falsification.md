# Pre-registered falsification battery — column-geometry hypothesis (Seebach rotation fleet)
2026-10-07. Red team, rotation fleet. Written BEFORE the Geometer, Rhythmicist,
and Phonetician run — the others' results merge only against this battery.

## 0. The hypothesis, stated before testing (H_col)
The 3-phase rotation (repaired-parse χ²=366.3, cycle A→B→C→A; T0-verified exact
against `code/crowd4/phase_map_repaired.json`) and the lag-3 excess (z=+5.6,
p≈1e-8 vs fitted first-order Markov — beyond what the block transition matrix
explains) arise from **enciphering-process geometry**: the clerk selecting groups
from a **multi-column syllabary table** with a soft column-rotation habit —
suppressing same-column repeats (self-transitions 0.51–0.74×), preferring column
cycling (cycle edges 1.35–1.52× over independence), with a 3-step process memory
(lag-3 excess). Table columns are **linguistically arbitrary** (laid out for the
clerk's convenience, not by grammar), which predicts the observed package: real
rotation + fragile cluster assignment + all linguistic mappings killed
(word-position N15, morphological T1, polyvalence-conditioner T2, unit-size T3,
syntactic T4-null) + tail-distributed signal (T5a distributed, not hub-driven).

Scope: this battery tests H_col, the column-geometry mechanism. It does NOT
re-test "the rotation is real" (established: T0 + E1–E3).

Canonical inputs: pair stream `code/side-keyhunt/repaired_offsets.json` (1,847
pairs, 96 groups); phases `code/crowd4/phase_map_repaired.json` (Jaccard-k12).

Pre-existing ADVERSE evidence (banked, not re-litigated):
- T2: phase conditions NONE of the three conditioned polyvalent readings
  (06 p=0.4399; 94 p=1.0000; 52 p=1.0000 — KILLED). If column selection
  conditioned homophone choice, phase would condition readings. It does not.
- T2c: naked adjacency of the two 06 readings in identical phase environments
  — same conditioner value, different readings. Direct contradiction of any
  phase-as-conditioner reading.

## 1. Falsification tests (statistic, baseline, threshold — all stated first)

### K1 — phase ↔ number-range association (the column-partition leg)
H_col prediction (strong form): phases = physical table columns; if columns are
numeric blocks, phase labels correlate with group-number range.
Pre-registered partition set (2 schemes; NO data-dredging beyond):
  S1: numeric tertiles of group ID — low 32 / mid 32 / high 32 (96 groups).
  S2: group ID mod 3.
Statistic: χ² association of phase (A/B/C/R) × range (3 classes). Significance by
EXACT permutation (10,000 shuffles of phase labels over the 96 groups), two-sided,
Bonferroni over 2 tests → per-test α=0.025.
Kill condition: p≥0.025 on BOTH schemes → the "numeric-block columns" variant is
foreclosed (record as a variant-kill, not a general kill of H_col — columns could
be non-numeric).
Strengthen condition: p<0.01 on either scheme WITH a coherent column story (the
enriched cells must form a readable one-to-one column layout, e.g. tertile↔phase)
→ STRENGTHENS H_col.

### K2 — homophone-variant cycling by position mod 3
H_col prediction: the clerk's soft rotation habit acts on column selections; the
choice among conditioned homophone variants should show residual mod-3 structure.
Pre-registered design: for each conditioned polyvalent group (06, 52, 94, 78 —
F33 + F38 islets), classify every occurrence into its F33 reading-class
(06: trigram-internal "ent" vs stem; 52: negation-frame "pas" vs other;
94: "en"-islet iff pre=82/suc=87 vs "ne"; 78: "ver" iff next=94 vs "me"-syllable).
Statistic per group: χ²(reading-class × occurrence-index-mod-3); exact permutation
p (10,000), one-sided (excess cycling), α=0.05 per group; combine the four with
FISHER'S METHOD as the pre-registered combiner, combined α=0.05. Report per-group
p as context only.
Kill condition: combined p≥0.05 AND no individual p<0.05 → no mod-3 cycling in
variant choice. (Note: reading-class labels inherit F33 lexical conditioning; a
lexical confound can only FALSE-positive this test, so a null is clean.)
Strengthen condition: combined p<0.05 with the cycling aligned to the A→B→C→A
order (variant choice must cycle through phases in the observed cycle direction —
stated to block "any periodicity counts" goalpost-moving).

### K3 — generative clerk simulation (mechanism adequacy; the hard gate)
H_col prediction: a generative model implementing the stated mechanism must be
ABLE to produce the observed package.
Pre-registered model: 3-column Markov column-choice chain (columns = phases),
parameters fitted from the observed ABC transition matrix: cycle-boost β =
P(on-cycle edge)/independence, self-suppression γ = P(self)/independence.
Within-column group selection = empirical within-phase unigram (linguistically
blind). Simulate 10,000 streams of 1,847 pairs; on each, re-run the Jaccard-k12
phase derivation + χ²(3×3 ABC) + lag-3 z (vs fitted first-order Markov).
Kill condition: <5% of simulated streams reach χ²≥366.3 AND z≥4.5
SIMULTANEOUSLY → the stated mechanism cannot generate the observed package →
H_col DEAD as a mechanism. (Joint package only: χ² alone is fitted by
construction; the joint package is the falsifier.)
Survival condition: ≥5% joint adequacy in BOTH variants — (i) empirical
within-phase unigram, (ii) uniform within-column (removes the fitted-unigram
crutch) → mechanism adequate; H_col survives K3. Adequacy ≠ confirmation.
Strengthen condition: passes both variants AND the fitted (β,γ) sit in a
clerk-plausible soft-habit range (γ∈[0.3,0.9], β∈[1.1,2.0]) — a hard
deterministic rotation (β≫2) would be the wrong mechanism for a "habit".

### K4 — phase-internal linguistic coherence (the arbitrariness leg; STRONGEST)
H_col prediction: columns are linguistically arbitrary; same-phase groups'
plaintext values should be linguistically INCOHERENT. This is the hypothesis's
core prediction, hence the strongest falsifier.
Pre-registered category assignment (fixed NOW, before running; status-marked
readings only — GT, provisional, strong leads; NO fragment readings):
  function-word: 11=la, 46=que, 87=ce, 64=qui, 96=par, 94=ne, 62=on, 77=le, 47=ce, 52=pas
  verb-stem: 06=verb-stem-class, 67=veut
  content/fragments: 70=pre, 82=m, 34=i, 29=er, 40=e, 78=me-syllable
  n=23 groups; R-phase groups excluded (matches the 3×3 χ² construction).
Statistic: coherence = fraction of A∪B∪C groups whose category equals their
phase's modal category. Baseline: 10,000 permutations of categories over the 23
groups, one-sided α=0.05.
Kill condition: p<0.05 in the coherence direction (same-phase groups ARE
linguistically coherent) → H_col DEAD (columns are linguistic slots, not
arbitrary columns).
Support condition: p≥0.05 → consistent with arbitrariness (a null, not evidence).
Anti-gaming note: categories were assigned from lane status marks, not from the
phase map; anyone re-running may not re-assign categories after seeing phases.

### K5 — boundary-rotation independence (DEFERRED until boundary ground truth)
H_col prediction: cycle-edge placement is INDEPENDENT of word boundaries
(clerk-side rhythm, not language-side).
Deferred until boundary ground truth accumulates (segmenter + cribs). Pre-registered
NOW: at known boundaries (formula-internal + GT-word boundaries), exact test of
on-cycle × boundary, two-sided α=0.05.
Kill/redirect condition: if on-cycle edges are boundary-ENRICHED at p<0.05, H_col
weakens toward a boundary-rhythm alternative (best-answer template (e)); if
boundary-DEPLETED at p<0.05, template (e) wins outright and H_col in the
table-geometry form is DEAD.
Existing constraint: T1b's formula-edge test (38 edges, exact binomial p=0.25
null) already weakly constrains this; K5 fires when real boundary data arrives.

## 2. Decision rule (the DEAD condition)
H_col is **DEAD** if ANY of:
  (i) K3 kill — the stated mechanism cannot generate the observed package, OR
  (ii) K4 kill — phases are linguistically coherent (the arbitrariness core breaks).
H_col is **WEAKENED** (not dead) if K1 fails on both schemes AND K2 fails AND K5
(when fireable) shows boundary dependence — the mechanism survives but has no
positive support beyond the package it was built to explain.
H_col is **STRENGTHENED** if K1 shows p<0.01 with a coherent column story, OR K2
shows mod-3 cycling at combined p<0.05 in the A→B→C→A order, OR K3 passes both
variants with clerk-plausible (β,γ).
H_col is **never CONFIRMED** by these alone. Confirmation additionally requires:
the labeling-robustness battery (round-6 WO item 1: cosine metric, k=8/16 cuts,
half-stream clustering — the lag-3 excess must persist in ALL variants) AND the
HMM-vs-bigram held-out BIC (WO item 2 — the 3-state HMM must win) AND K4-null
AND K3-pass. Until the key speaks, the ceiling verdict is "surviving, mechanism
adequate, unexplained" — best-answer template (g) "still unknown" stays on the
table.

## 3. Pre-registration compliance rules for the fleet (BINDING on Geometer, Rhythmicist, Phonetician)
R1. Statistic, baseline, and threshold stated BEFORE running. Any claim whose
    statistic was chosen after seeing the numbers is EXPLORATORY by default —
    fenced as such, never a verdict.
R2. Multiple-testing discipline: any battery running >1 test names its correction
    (Bonferroni / Fisher's / permutation-combined) IN ADVANCE. Uncorrected
    p-hacking = claim VOID.
R3. Small-n exactness: n<20 in any cell or expected<5 → exact/permutation tests
    only. χ² asymptotics are void there (the N35 lesson).
R4. Status propagation: any leg conditioning on provisional readings (87=ce,
    64=qui, 96=par, 94=ne, 06-class, 67=veut, 62=on, 77=le, 47=ce, 78-me/ver)
    inherits provisional. No provisional-conditioned leg reaches CONFIRMED.
R5. Traceability: headline ratios must reproduce from archived .json. .md-only
    numbers are VOID (the F26-6 / F26-11 lesson).
R6. Every positive claim merges only with a red-team ruling. Rulings live in
    `code/side-rotation/redteam/`.

## 4. Kill ledger (append-only)
- (empty — no claims have landed as of 2026-10-07 ~11:55 CDT)
