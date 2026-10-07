# PRE-REGISTRATION — GEOMETER (rotation-fleet), Seebach lane
Date: 2026-10-07. Executor: GEOMETER. Lane: zeschau-seebach-1841.
Scope: code/side-rotation/geometer/ (+ this file at code/side-rotation/prereg_geometer.md).

## Canonical inputs (fixed before any test)
- Pair stream: code/side-keyhunt/repaired_offsets.json → 1,847 pairs, 96 groups
  (loader: code/crowd4/repaired_parse.py::load_pairs_repaired).
- Phase map: code/crowd4/phase_map_repaired.json (Jaccard-k12; A=32, B=27, C=17, R=20).
- T0 gate (runs first, in code): re-derive Jaccard-k12 phases independently and
  require exact equality with the banked map AND chi²(3×3 ABC)=366.3±1.
  If T0 fails, stop — instrument unreproduced (do not run WO1–3).
- Lag-3 reference (E1, RECOVERED EXACTLY in T0): the E1-exact method is ABC-bounded —
  lag-k same-phase rate over position pairs with BOTH endpoints in {A,B,C},
  vs a 3-state chain fitted on ABC-bounded transitions (π = row marginals):
  lag-3 obs=0.4219, exp=0.3529, z=+5.61 (matches the md's 0.4219/0.3530/+5.6).
  My first 4-state reconstruction gave z=+5.95 with different absolute rates;
  the ABC-bounded variant is the exact E1 method and is what WO3's M2 uses.
  (Amendment recorded 2026-10-07 before WO1–3 ran: method refinement, not a
  statistic change — the pre-registered bar M2 z≥+3.0 is unchanged.)

## WO1 — NUMBER-RANGE TEST (table-geometry smoking gun)
Hypothesis under test: phases = physical columns (or column blocks) of a printed
multi-column table. A 3-column printed table numbers cells either
(a) column-contiguously (col1=low numbers, col2=mid, col3=high), or
(b) row-major across columns (column = n mod 3).
Both layouts predict group NUMBER ↔ phase association. Both are tested; a
positive claim requires a COHERENT layout story, not just a small p.

- WO1a (primary): 3×3 contingency phase∈{A,B,C} × number-tertile.
  Tertile cut points from ALL 96 group numbers (33rd/67th percentiles);
  contingency on the 76 ABC groups (R excluded — the rotation is ABC).
  Statistic: Fisher's exact test, Monte Carlo 200,000 replicates, α=0.05.
  Effect size: Cramér's V.
- WO1b (secondary): 3×3 contingency phase∈{A,B,C} × (group number mod 3),
  same exact test, α=0.05.
- Multiple testing: Holm over {WO1a, WO1b}.
- Robustness variant (secondary): runs test — phase sequence ordered by group
  number (all 96, R kept as 4th category); statistic = number of runs;
  baseline = 10,000 permutations of phase labels over numbers; one-sided p
  (fewer runs than expected = clustering).
- Decision rule (pre-registered): SUPPORT for table geometry iff (WO1a or WO1b
  significant after Holm) AND Cramér's V ≥ 0.40 AND the winning table shows a
  coherent layout (each phase concentrated in one tertile / one mod-class —
  the (a)/(b) story). p<0.05 with V<0.30 = "weak number structure, suggestive
  only", NOT support. p≥0.05 on both = NULL (one leg of the falsification
  battery against the column-geometry hypothesis).

## WO2 — HOMOPHONE-CYCLING TEST
Mechanism under test: "the clerk cycles through homophone variants in rhythm
with the stream". Observable with current key knowledge: for groups whose
readings are classified by F33's verified conditioning rules, does the READING
choice depend on stream position mod 3?
F33 rules (re-derived in code from the stream, not copied from prose):
- 06: "trigram-internal ent" iff pairs[i-4:i+1]==[77,78,94,82,06] (else verb-stem).
- 94: "en"-islet iff prev-group==82 OR next-group==87 (else "ne").
- 52: "pas"-candidate iff a 94 occurs in window [i-6, i-1] (else "se"/"so"-class).
- 78: single live reading ("me" LEAD) — NO reading-contrast test possible.
  Secondary mechanism test instead: candidate homophone pair for "me": 78 (LEAD)
  vs 43 ("me" MED). Test: among 78∪43 occurrences, P(chosen=43) vs position mod 3
  (Fisher exact). Pre-registered as SECONDARY with the caveat that 43="me" is
  MED-grade — a null here is weak, a positive is a lead not a verdict.
- Statistic (primary): per group, Fisher's exact test (Monte Carlo 200,000) on
  reading-class × (position mod 3). Combined across 06/52/94 via Fisher's method
  on the three p-values; α=0.05 on the combined p. Per-group p's reported.
- Power honesty (pre-registered): for each group report the BEST-CASE p — the
  Monte-Carlo p when all minority-class occurrences sit in a single mod bin
  (perfect cycling). If best-case p ≥ 0.05 for a group, the test is VACUOUS for
  that group: reported as "untestable at this n", not as a null.
- Decision rule: combined p<0.05 → SUPPORT for position-cycled choice (direction
  checked: minority readings concentrated in one mod class). Else NULL.

## WO3 — SIMULATE THE CLERK (generative verification)
Build a toy 3-column printed table (~100 groups), syllabify era French
(data/gutenberg-30513-tocqueville-t1.txt, body text only — strip Gutenberg
header/footer), assign each distinct syllable 2–4 homophone groups spread across
the 3 columns (frequent syllables get variants in all 3 columns; assignment
balances column frequencies), and encipher the syllable stream under each
pre-registered clerk behavior. 20 replicates per behavior (fresh table +
fresh behavior noise each replicate; fixed seed schedule recorded in code).

Clerk behaviors (pre-registered; column chosen first, then uniform among the
needed syllable's variants in that column, falling back to nearest column with
a variant):
- B0 NULL: uniform random variant choice (no column bias).
- B1 PER-UNIT CYCLING: per-syllable counter; successive occurrences of the same
  syllable cycle its variants across the 3 columns in fixed order.
- B2 STREAM SOFT ROTATION: column drawn from a first-order Markov chain fitted
  to the observed ABC transition profile (p_same≈0.20, p_next≈0.55, p_off≈0.25).
- B3 TABOO-2 MEMORY: column weights penalize columns used at t−1 and t−2:
  w(c) ∝ exp(−β·(1[c used at t−1] + γ·1[c used at t−2])), β=2.0, γ=0.7
  (genuine 3-step memory; β pre-registered, not tuned to the target).
- B4 ROW-MAJOR SCAN: clerk scans the printed table row-major from the last
  chosen cell and takes the first variant of the needed syllable.
- B5 HAND DRIFT: hand position h_t ∈ {0,1,2} random-walks (P(stay)=0.5,
  P(±1)=0.25 each, reflecting); variant chosen = the needed syllable's variant
  nearest h_t.

Measurements per replicate (on TRUE column labels — no clustering):
- M1: chi² of the 3×3 column-transition table vs independence (df=4).
- M2: lag-3 same-column rate and z vs fitted first-order Markov expectation
  (my T0 reconstruction of the E1 method).
- M3: self-transition suppression factor = P(same)/Σ p_i².
Match criteria (pre-registered): a behavior REACHES OBSERVED STRENGTH iff the
MEDIAN over 20 replicates satisfies ALL of: M1 ≥ 200 (observed 366.3; bar set
below observed to allow for derivation noise), M2 z ≥ +3.0 (observed +5.6),
M3 < 0.8 (observed 0.51–0.74×). Failing any one = does not reach.
Bridge check (pre-registered, for behaviors passing the median criteria): run
the lane's Jaccard-k12 clustering on the simulated group stream and require
adjusted-Rand(derived phases, true columns) ≥ 0.5 — i.e. the behavior must also
produce CLUSTERABLE phases, or the analogy to the observed pipeline breaks.
Decision rule: if NO behavior reaches observed strength → report plainly that
the process hypothesis is in trouble (no tested clerk mechanism reproduces the
package). If one does, name it with parameters.
- CALIBRATION AMENDMENT (recorded 2026-10-07, before any derived-phase results
  were seen): the observed headline numbers (chi²=366.3, z=+5.6) are
  POST-CLUSTERING quantities (Jaccard-k12 derived phases). True-column sim
  measurements are therefore NOT the comparison basis — early true-column
  medians (B2 M1≈45–54, B3 M1≈51) already show clustering amplifies chi², so a
  true-column bar would be miscalibrated. The match criteria (M1≥200, z≥+3.0,
  M3<0.8) apply to the DERIVED-PHASE measurements: for every replicate, run the
  lane's Jaccard-k12 pipeline on the simulated group stream and compute M1/M2/M3
  on the derived phases exactly as for the observed stream. True-column
  measurements are kept as diagnostics. The bridge ARI≥0.5 requirement stands:
  without it a passing behavior could be passing for the wrong reason.

## Cross-cutting rules
- Never invent ciphertext or keys. All inputs are the repaired stream + banked
  phase map + Gutenberg text + toy tables built in code.
- The Red Team gates positive claims: any SUPPORT verdict above goes to
  code/side-rotation/redteam/ for independent re-derivation before it is final.
  (Note: code/side-rotation/prereg_falsification.md named in the work order does
  not exist; this file serves as the pre-registration record.)
- Report-inbox note per REPORTING.md on completion: code/side-rotation/geometer/
  holds code + prereg note; inbox note named geometer-<topic>.md entries.
