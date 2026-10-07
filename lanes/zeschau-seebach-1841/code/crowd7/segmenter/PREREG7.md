# PREREG7 — Segmenter round 7: flag application + label-free momentum + columns refuge

Worker: segmenter (round 7) · 2026-10-07 · Lane: zeschau-seebach-1841.
Work order: STATE.md round-7 WO-11. Red-team rulings applied: N41 UPHELD, N43 UPHELD
(`code/crowd7/redteam/RULINGS.md`). Deconfliction: side-rotation fleet owns
rhythmicist/geometer; this package owns the falsification battery + flag application —
their results are CITED, not re-derived.

Canonical stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`
via `code/crowd4/repaired_parse.py`), positions per `code/crowd4/REINDEX.md`.
All randomized steps: seed 20261007 (matches round 6). Cipher-internal only
(F30-legal); no invented values. No argument below leans on the exact χ²
magnitudes (181.3 / 366.3) — N43(b). Per-group phase claims are flagged unless
independently supported — N43(c).

## Thread A — flag application to the round-6 package (N41)

Re-derive the two load-bearing numbers fresh (A1 gate E1, A2 P2a momentum);
audit T1/T2/T3/P2b/P2c against the red-team-verified `code/crowd6/segmenter/rotation_r6.json`
(N41 UPHELD — no need to re-run the slow HMM/clustering code; the audit is the work).

Per-conclusion verdict scale (applied analytically, stated before running):
- SURVIVES — no dependence on exact χ² or per-group phases.
- SURVIVES* — population-level / instrument-consistency claim; does not name
  any group's phase; mapping-purity caveat recorded.
- DOWNGRADED — verdict overstates what the instrument licenses under the flag.
- FENCED — leans on a per-group phase argument without independent support.

Pre-registered expectations (to be confirmed or corrected by the run):
- A1 gate E1 (lag-3 z≈+5.8): SURVIVES — flag (a) explicitly confirms.
- A2 T1 labeling-robustness FRAGILE: SURVIVES* — failure mode is labeling
  degeneracy (mega-clusters), never excess-death; 91/96 k=16 agreement is
  instrument-consistency, not mapping truth.
- A3 T2 HMM-vs-bigram (ΔtestLL 0.028, bigram wins; cyclic A): SURVIVES — no χ²,
  no labels in the fit; the unsupervised cyclic A is label-free corroboration.
- A4 T3 69/96-vs-61/96 reconciliation: SURVIVES* — definitional metrology
  (naive vs best-permutation); neither number measures mapping truth.
- A5 P2a momentum (z=+4.77): SURVIVES* PENDING Thread B — population-level
  (not per-group, not χ²); circularity caveat (labels fit on the same stream).
- A6 P2b memory-2 null: SURVIVES — null on the label stream; power caveat under (c).
- A7 P2c fixed-column-order FALSIFIED: DOWNGRADED → INCONCLUSIVE — variant
  direction flips are computed on degenerate partitions (V_cos C=1 group,
  V_half B=4/C=5); under (c) they cannot falsify "one column order". The
  halves-consistency (fwd/fwd on the reference instrument) survives as an
  observation.

## Thread B — label-free momentum test (NEW)

Question: does the P2a momentum signal (r1=0.6327 vs r0=0.4856, z=+4.77)
survive WITHOUT the fragile banked labels?

Instrument: 3-state HMM, Baum-Welch, code copied verbatim from round-6
`hmm_test.py` (fwd_bwd / baum_welch / viterbi), seed 20261007, 10 restarts ×
150 iters, MAP-EM eps=1e-4. NO banked labels used at any step.

- Gate B0 (instrument reproduction): re-fit A must match round-6 A within
  1e-3 per entry. Else STOP — instrument not reproduced.
- Guard B1 (cycle definability): frozen A's dominant directed 3-cycle must
  satisfy fwd_mass/rev_mass ≥ 2.0. Else UNTESTABLE (no definable cycle).
- Decode: Viterbi on the TEST split only (pairs[1231:], held-out — never in
  the fit). Cycle direction from the frozen A (not from banked labels).
- Statistic (P2a analog): r1 = P(S_{t+1}=cyc(S_t) | (S_{t-1},S_t) a cycle step),
  r0 = P(S_{t+1}=cyc(S_t) | (S_{t-1},S_t) a non-cycle non-self step);
  self-transitions excluded from both conditioning sets (mirrors P2a).
- Guard B2 (power): n1 ≥ 100 and n0 ≥ 50, else INCONCLUSIVE (underpowered —
  not a falsification).
- BAR (pre-registered): one-sided two-proportion z, α=0.05. SURVIVES iff
  p < 0.05 AND r1 > r0. Else DOES NOT SURVIVE (label-dependent).
- Secondary: 2,000 permutations of the decoded test order → empirical p for
  (r1−r0); reported alongside (validates the z-approximation, guards against
  Viterbi artifacts).
- Reference (not verdict-driving): labeled P2a recomputed on the test split
  only, for comparability.

Conservativeness note (pre-registered): Viterbi decoding noise creates
spurious non-cycle transitions followed by re-sync cycle steps, which
INFLATES r0 — the test is conservative for r1>r0.

## Thread C — the columns refuge: concrete or killed

Standing: arbitrary-column form KILLED (side-rotation fleet instrument-validity
proof: contact clustering never recovers arbitrary columns, ARI≈0; no clerk
simulation reaches χ²-class strength — cited, not re-derived). Surviving refuge:
columns = an untested linguistic class.

Concretization C0 (STATED BEFORE TESTING — this is the model under test):
- Table: 96 cells = 3 columns × ~32 rows. Columns = CODA-SONORITY class:
  OPEN (vowel-final syllable) / SON-CLOSED (final sonorant n,m,l,r) /
  OBS-CLOSED (final obstruent). Rows ≈ onset (linguistically inert for the
  rhythm question).
- Mechanism: French prose syllable streams alternate function-word opens
  (le/la/de/à/ce/que/qui/ne/se…) with content-word codas; the coda-class
  sequence carries a period-3-ish rhythm + chaining momentum. Contact-coherent
  homophonic aliasing (F49) preserves the class sequence at the group level,
  which is what Jaccard clustering recovers (at ~0.5 purity — N43(c)).
- Predictions: (P-a) the plaintext coda-class stream shows lag-3 excess
  (z>2) AND momentum (r1>r0, p<0.05); (P-b) valued groups' banked phases
  associate with coda class.

C1 corpus test (decisive for C0): syllabify Tocqueville T1+T2
(`code/crowd/phonotactician.py::syllabify`, orthographic, mute-e kept as its
own syllable per R1 — matches the encipherer's attested practice), map each
syllable to {OPEN, SON, OBS} by its orthographic coda; E1 lag-3 (obs/exp/z,
3-state Markov expectation, all positions) + P2a-analog momentum (dominant
directed 3-cycle from the data).
- Secondary: Les Mis T1 (register robustness — F10).
- Caveats (pre-registered): orthographic syllabification ≠ encipherer's cuts
  (R2 inconsistent cutting is SOLID) → the test is CONSERVATIVE (attenuates
  real effects; a null weakens, a positive is strong). Register gap
  (diplomatic vs literary French) — phonotactics less register-sensitive
  than lexicon, but noted.
- BAR: CONCRETE iff primary (Tocqueville) hits z>2 (excess direction) AND
  momentum p<0.05 with r1>r0. WEAKENED iff |z|≤2 AND momentum p≥0.05.
  Mixed → INCONCLUSIVE. (Full KILL needs key recovery: phase ⊥ coda-class
  at n≫.)

C2 anchor probe (consistency only, never verdict-driving): 16 valued groups →
orthographic coda class → phase × class Fisher exact MC (10k).
Pre-registered list: 11=la OPEN, 70=pre OPEN, 82=m SON (lone-consonant edge),
34=i OPEN, 29=er SON, 40=e OPEN, 46=que OPEN, 87=ce OPEN, 64=qui OPEN,
96=par SON, 77=le OPEN (conditioned), 59=est OBS, 00=pour SON, 16=i OPEN,
78=me-syllable OPEN (F51-conditional), 62=on SON (ear-only). Excluded: 84
(conflict), 45 (disfavored), 47 (blocked), 43 (weak), 67 (fork).
BAR: p<0.05 AND interpretable pattern → consistent-with (weak support);
else inconclusive.

## Outputs
- `flag_audit.py` → `flag_audit.json` (Thread A)
- `momentum_labelfree.py` → `momentum_labelfree.json` (Thread B)
- `columns_refuge.py` → `columns_refuge.json` (Thread C)
- Report note: `code/crowd7/report_inbox/segmenter-rotation.md`
