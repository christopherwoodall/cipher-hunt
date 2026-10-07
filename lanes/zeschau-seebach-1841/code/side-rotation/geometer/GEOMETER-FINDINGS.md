# GEOMETER findings — rotation-fleet, Seebach lane (2026-10-07)

Executor: GEOMETER. Scope: `code/side-rotation/geometer/`.
Pre-registration: `code/side-rotation/prereg_geometer.md` (written BEFORE any
test ran; one calibration amendment recorded before derived-phase results).
Gate: T0 re-derived Jaccard-k12 phases EXACTLY (= banked map), chi²=366.35,
lag-3 z=+5.61 via the E1-exact ABC-bounded reconstruction (0.4219 vs 0.3529 —
matches rotation_mystery.md). All inputs: repaired 1,847-pair stream, banked
phase map. Nothing invented.

## WO1 — number-range test: NULL
- WO1a phase×tertile (76 ABC groups): Fisher exact MC p=0.569, chi²=3.05,
  Cramér's V=0.142. Table: A=[12,12,8], B=[8,11,8], C=[5,4,8] — flat.
- WO1b phase×(n mod 3): p=0.883, V=0.089. Flat.
- Runs test (96 groups by number): 74 runs, p=0.76.
- Verdict: NULL. Kills the naive printed-table layouts (column-contiguous
  numbering, row-major numbering). A table numbered in a non-obvious order
  survives this test, but the "3 columns = 3 number ranges" story is dead.
- Evidence: `geometer/wo1.json`, `geometer/wo1_number_range.py`.

## WO2 — homophone-cycling test: NULL
Reading classes re-derived byte-exact from the stream (F33 rules):
- 06: n=44; trigram-"ent" n=2 @[1184,1355] (strict 77-78-94-82-06 rule).
  Note: the repaired stream's @578 94-82-06 trigram LACKS the 77-78 prefix —
  T2a's n=3 was old-parse/looser-rule. Sensitivity with the loose prev-pair
  rule (n=3 @[580,1184,1355]): same conclusion.
- 94: n=37; "en"-islet n=4 @[651,1102,1169,1576] (matches T2d).
- 52: n=27; "pas"-frame n=5 @[571,1294,1332,1356,1807].
- Reading × position-mod-3, Fisher exact MC:
  06 p=0.194 (VACUOUS — best-case p=0.178 even under perfect cycling; loose
  rule: p=0.510, best-case 0.098 — still vacuous),
  94 p=0.809 (POWERED — best-case p=0.011, a real cycle was detectable),
  52 p=0.219 (POWERED — best-case p=0.0022).
- Secondary 78/43 "me"-pair choice × mod-3: p=0.924 (n78=31, n43=16).
- Combined: literal pre-registered 3-way Fisher p=0.036 — NOT CLAIMED. It is
  manufactured by the vacuous 06 component, fails the pre-registered direction
  check (minority readings spread across mod classes: 94 → mods 0,1,2,1;
  52 → 1,1,0,0,1), and the non-vacuous combination (94+52) gives p≈0.48
  (loose-rule 3-way: p=0.14).
- Verdict: NULL. No evidence the clerk cycles homophone/reading choice with
  stream position. 06 is untestable at this n under either rule.
- Evidence: `geometer/wo2.json`, `geometer/wo2_homophone_cycling.py`.

## WO3 — simulate the clerk: NO behavior reaches observed strength
Toy 3-column table (~90 groups; 45 top Tocqueville syllables, frequent ones
with a variant in each column), T=1847 syllable streams, 20 replicates per
behavior, lane's Jaccard-k12 pipeline run on every simulated stream
(derived-phase measurements — apples-to-apples with observed 366.3/+5.6).

Median derived-phase measurements (bars: M1≥200, z≥+3.0, M3<0.8, ARI≥0.5):

| behavior | derived M1 | derived z | derived M3 | ARI | true-col z |
|---|---|---|---|---|---|
| B0 null | 6.5 | -0.38 | 0.989 | 0.005 | 0.30 |
| B1 per-unit cycling | 30.8 | -0.47 | 0.876 | -0.007 | -0.25 |
| B2 stream soft rotation | 16.0 | -0.28 | 0.999 | -0.000 | 0.78 |
| B3 taboo-2 memory | 30.6 | 0.55 | 0.971 | 0.009 | **+8.34** |
| B4 row-major scan | 0.8 | -0.25 | 1.000 | 0.187 | -0.88 |
| B5 hand drift | 15.9 | 0.05 | 0.991 | 0.003 | 0.37 |
| **observed** | **366.3** | **+5.61** | **0.51–0.74** | — | — |

Post-hoc boundary (B6 deterministic column rotation; B7 strong-soft
p_same=0.05/p_next=0.80): ARI_med = 0.000 / 0.043; derived z = -0.51 / +1.00
(deterministic seeds). Even PERFECT column alternation is invisible to contact
clustering.

Verdict: no tested clerk behavior reproduces the package — the process
hypothesis in its column-geometry form is in trouble. Two sharp sub-results:
1. A taboo-2 "don't reuse a column used in the last 2 steps" memory DOES
   generate lag-3 z≈+8-class rhythm at the process level (B3 true columns,
   rep0 z=+8.34; earlier seed schedule gave +6.61 — robust).
   Pure first-order column rotation does NOT (B2 true z≈0.3–0.8) — the observed
   z=+5.6 needs ≥2nd-order memory IF it is a column process at all.
2. Structural mismatch: Jaccard-k12 contact clustering NEVER recovers
   linguistically-arbitrary columns (ARI≈0 from null through deterministic),
   because a group's contact profile is dominated by its syllable's linguistic
   neighbors, not its column. The observed phases WERE found by contact
   clustering (chi²=366.3) — so they cannot be arbitrary table columns.
   Combined with T1–T4 (no linguistic mapping), WO1 (no number structure),
   and WO2 (no cycled choice), the column-geometry hypothesis is cornered into
   an impossible conjunction: contact-recoverable AND linguistically incoherent
   AND number-unstructured AND period-3-rhythmic. No tested mechanism produces it.
- Surviving refuge (narrow, testable): columns = a linguistic class T1–T4 did
  not test (not morphology/polyvalence/cell-size/syntactic-function — e.g.
  onset/coda phonotactics). T4c's fragment scatter argues against it, but no
  direct test exists. Needs key recovery.
- New lead (speculative): the rhythm has 3-step AVOIDANCE memory (B3-style).
  What process avoids reusing a state used in the last 2 steps, has
  contact-clusterable states, and no linguistic mapping? Not answered here.
- Caveats: toy uses 45 syllables, random column assignment, column process
  independent of plaintext; crude syllabifier. The ARI≈0 result rests on
  linguistic bigram structure dominating contact profiles — expected to hold
  for any natural-language-like stream, but it is a toy result, not a theorem.
- Evidence: `geometer/wo3.json`, `geometer/wo3_clerk_sim.py`,
  `geometer/wo3_exploratory.json`, `geometer/wo3_exploratory.py`.
  Seeds deterministic (behavior-index based); Red Team can re-derive exactly.

## Bottom line for the fleet
Three falsification legs, all pre-registered, all executed:
1. Phases are not number-structured (WO1).
2. Homophone/reading choice is not position-cycled (WO2).
3. No column-geometry clerk process reproduces the observed package, and
   contact clustering structurally cannot recover arbitrary columns (WO3).
The rotation is real (z=+5.6, global, distributed) and still unexplained.
The "soft column-rotation through a multi-column table" leading hypothesis
should be demoted: it now needs independent evidence, not just fit.
