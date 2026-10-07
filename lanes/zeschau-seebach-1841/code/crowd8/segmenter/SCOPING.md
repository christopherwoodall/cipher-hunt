# SCOPING — the columns refuge, round 8 (WO-13)

Segmenter · 2026-10-07 · Lane: zeschau-seebach-1841.
Pre-registration: `PREREG8.md`. Battery: `recoverability.py` → `recoverability.json`.

## The refuge, precisely stated

Post-fleet form (FLEET-SYNTHESIS.md): the killed form is COLUMNS-ARBITRARY
(the key-maker's table had linguistically-arbitrary columns; the Geometer
killed it four ways, including the structural result that the lane's contact-
clustering instrument is blind to arbitrary columns, ARI≈0). The surviving
refuge is COLUMNS-CLASS: the table's columns were an UNTESTED LINGUISTIC
CLASS X of syllables (e.g. onset/coda phonotactics — not the same as the
Phonetician's CV-shape test).

The refuge decomposes into two separable claims:
- (i) LINGUISTIC: some syllable class X carries the observed signature
  (period-3 contact rhythm, z≈+5.6 label-free; directed-cycle momentum
  r1=0.6327 vs r0=0.4856, z=+4.77) in French prose.
- (ii) ARRANGEMENT: the key's table was physically arranged with columns = X.

## Testable WITHOUT key recovery (claim i only)

- T1 — corpus signature. For any concrete X: the plaintext X-class stream
  must show lag-3 excess (z>2) AND momentum (r1>r0, one-sided p<0.05) on
  era prose (Tocqueville T1+T2; Les Mis register check). A miss kills X as
  the rhythm's source. Precedent: C0 coda-sonority died here (momentum z=-65).
  Caveats (pre-registered, conservative): orthographic syllabification ≠
  encipherer's cuts (R2: inconsistent cutting solid — attenuates real
  effects); register proxy (diplomatic French unobtainable).
- T2 — instrument-recoverability (new this round). X must be recoverable by
  the lane's own contact-clustering pipeline (Jaccard top-10 contact sets,
  average linkage, k=3 cut) from a plaintext syllable stream, at ARI ≥ 95th
  percentile of 200 size-matched random partitions. Inverts the Geometer's
  result: a class the instrument cannot recover cannot be what the cipher's
  clustering found. No-aliasing simulation is the best case (F49: real
  aliasing is contact-coherent, only degrades) — failure kills X, and the
  kill direction is conservative.
- T3 — valued-group phase×X association (n=16, Fisher): consistency ONLY.
  Gated by N43(c) (~0.5 mapping purity): can neither promote nor kill.
- T4 — register check (Les Mis): bounds the register caveat; never
  bar-driving.

## NOT testable without key recovery

- U1 — per-group phase↔X ground truth (N43(c): mapping ~0.5 purity; no
  per-group phase argument is licensed without independent support).
- U2 — the encipherer's actual syllable cut points (R2). All corpus tests
  are conservative proxies.
- U3 — claim (ii) itself: deliberate column arrangement vs emergent contact
  classes. Even a perfect X-signature plus perfect group association is
  compatible with "syllabary ordered by contact similarity, no columns".
  Distinguishing needs the key's physical layout.
- U4 — the true plaintext register (diplomatic French, 1841). Corpus proxies
  only; phonotactics is less register-sensitive than lexicon, but the gap
  is uncloseable without parallel text.
- U5 — homophone-dealing policy detail. F49 (contact-coherent aliasing) is
  a positive key-structure clue, but which cells / how many homophones per
  syllable needs the key. (Key-structure's lane; not duplicated here.)
- U6 — the bare "untested class" schema with no concretization: logically
  open, zero positive evidence, unkillable without key (standing).

## Battery verdict (Thread T)

Pre-registered candidates, Tocqueville primary (417,943 syllables, 1,526
distinct). Signature = C1 construction (lag-3 z>2 AND momentum r1>r0,
one-sided p<0.05). Recoverability = ARI(k-cut clustering, X) vs 200
size-matched random partitions. Full numbers: `recoverability.json`,
`diag_k12_top96.json`.

| X | lag-3 z (toc) | momentum z (toc) | momentum (lesmis) | ARI vs X | verdict |
|---|---|---|---|---|---|
| X1 coda3 (calibration) | +11.90 | −64.91 (anti) | −49.92 (anti) | −0.050, p_emp=0.94 | DEAD |
| X2 onset manner | +2.39 | +8.60 (r1−r0=+0.016) | −7.03 (anti) | +0.008, p_emp=0.22 | DEAD |
| X3 nucleus quality | −2.63 | −111.71 (anti) | −90.28 (anti) | −0.037, p_emp=0.80 | DEAD |
| X4 shape | +5.57 | −100.18 (anti) | −64.16 (anti) | +0.013, p_emp=0.21 | DEAD |

Notes:
- The k=3 cut degenerates at both scales (full inventory: 1524/1/1;
  top-96: 93/2/1) — the same labeling-degeneracy the Rhythmicist
  documented. The ARI leg was therefore re-run post-hoc (diagnostic,
  labeled as such) with the lane-faithful pipeline: top-96 syllables
  (75.3% token coverage), k=12 cut (non-degenerate: 54/13/10/…), top-3
  clusters + nearest-assignment. All four X score ARI≈0, below every
  random-partition p95: the instrument, working as designed, does not see
  any of these classes.
- X2 is the only non-degenerate signature: lag-3 z=+2.39 clears the bar and
  momentum is significant (p≈0) — but the effect is +0.016 vs the cipher's
  +0.147, it REVERSES on Les Mis (z=−7.03), and it fails recoverability.
  Register-fragile, tiny, multiplicity-exposed (4 candidates): not a live
  concretization.
- S2 (secondary, supporting-only): X2/X4 transition-matrix cosines beat
  their random nulls (X2 0.9349 vs p95 0.8869; X4 0.8744 vs p95 0.7426) —
  gross transition geometry is compatible, not discriminating; does not
  override the primary kills.

## Bottom line

Every concretization of the refuge attempted so far dies: C0 coda-sonority
(round 7, momentum z=−65) and now X1–X4 (three with strongly ANTI momentum,
z=−65…−112; the fourth register-fragile at +0.016 effect). None of the four
is recoverable by the lane's own contact-clustering (ARI≈0 vs random nulls)
— so none of them can be what the cipher's clustering found, either.

The refuge is now scoped to exactly this: the "untested linguistic class"
schema survives ONLY while unconcretized. Every concrete class dies on the
signature leg, the recoverability leg, or both. What remains untestable
without key recovery is U1–U6 above — in particular U3 (deliberate column
arrangement vs emergent contact classes) and the bare schema U6. Full kill
needs key recovery: standing, unchanged.
