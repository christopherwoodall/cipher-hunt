# PREREG8 — Segmenter round 8: scoping the columns refuge (WO-13)

Worker: segmenter (round 8) · 2026-10-07 · Lane: zeschau-seebach-1841.
Work order: STATE.md round-8 WO-13 — scope what's testable WITHOUT key
recovery re: the columns refuge; state honestly what isn't. Do not duplicate
the Smith's objective work or key-structure work. Standing: full kill needs
key recovery; the coda-sonority concretization (C0) is dead (N48).

Base documents: `code/side-rotation/FLEET-SYNTHESIS.md` (refuge definition),
N43 (noisy-detector flag), N48 (round-7 flag application).
Canonical parse: repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`
via `code/crowd4/repaired_parse.py`); banked phases
`code/crowd4/phase_map_repaired.json`. Corpus: Tocqueville T1+T2 primary
(`data/gutenberg-30513-tocqueville-t1.txt`, `...-t2.txt`); Les Mis T1
register check. Syllabifier: orthographic, copied from
`code/crowd/phonotactician.py` (mute-e kept as own syllable — matches the
encipherer's attested practice; R2 inconsistent cutting is a STATED
conservative caveat, same as C1).

## Thread S — scoping statement (analytic; no data)

Decompose the refuge into two separable claims:
- (i) LINGUISTIC: some syllable class X carries the period-3 + momentum
  signature in French prose (the rhythm is linguistic, not process).
- (ii) ARRANGEMENT: the key's table was physically arranged with columns = X.

Testable WITHOUT key recovery (claim i):
- T1 corpus signature: for any concrete X, the plaintext X-class stream must
  show lag-3 excess (z>2, excess direction) AND momentum (r1>r0, one-sided
  p<0.05) on Tocqueville. Kills X as the rhythm's source if absent
  (C0 died here: momentum z=-65).
- T2 instrument-recoverability (NEW this round): X must be recoverable by the
  lane's own contact-clustering pipeline (Jaccard top-10 contact sets,
  average linkage, k=3 cut) from a plaintext syllable stream. The Geometer
  proved the instrument is blind to arbitrary columns (ARI~0); inverting it,
  a class the instrument CANNOT recover cannot be what the cipher's
  clustering found. No-aliasing simulation = best case (F49: real aliasing
  is contact-coherent, only degrades); failure here kills X.
- T3 valued-group phase×X association (n=16 Fisher): consistency ONLY —
  gated by N43(c) (~0.5 mapping purity): can neither promote nor kill.
- T4 register check (Les Mis): bounds the register caveat, never bar-driving.

NOT testable without key recovery:
- U1 per-group phase↔X ground truth (N43(c)).
- U2 the encipherer's actual syllable cut points (R2 solid) — all corpus
  tests conservative.
- U3 claim (ii) itself: deliberate column arrangement vs emergent contact
  classes. Even a perfect X-signature + perfect group association is
  compatible with "syllabary ordered by contact similarity, no columns".
  The physical layout needs the key.
- U4 the true plaintext register (diplomatic French 1841) — corpus proxies
  only.
- U5 homophone-dealing policy detail (F49 positive clue stands; mechanism
  needs the key).
- U6 the bare "untested class" schema with no concretization — logically
  open, no positive evidence, unkillable without key (standing).

## Thread T — new concretization battery (cluster-recoverability + signature)

Candidate classes X (pre-registered, syllable-level, 3-class, all computable
from orthographic syllables; token = orthographic syllable incl. lone-C):

- X1 CODA3 = {OPEN, SON, OBS} — coda_class verbatim from round-7
  `columns_refuge.py` (coda after last vowel; SON iff ends in n/m/l/r).
  CALIBRATION: C1 signature known-dead (momentum z=-65); recoverability
  expected HIGH (contact-relevant). A recoverable-but-signaturless X1
  validates the battery's dissociation power.
- X2 ONSET (manner): onset = consonant tokens before first vowel.
  {VINIT: no onset} / {VLESS: onset[0] in {p,t,k,qu,c,ch,ph,f,s,x}} /
  {VOICED: else (b,d,g,j,v,z,l,m,n,r,gn,h)}. Lone-C syllable: classed by
  its first token under the same map.
- X3 NUCLEUS (vowel quality): nasal digraph in nucleus+coda not followed
  by vowel/n/m in-syllable ("anne" correctly oral via double-n) → NASAL;
  elif nucleus contains ou/au/eau/oi or 'o' or 'u' → ROUNDED; else FRONT.
  Lone-C → FRONT. (Orthographic approximation — stated noise, conservative.)
- X4 SHAPE: {V: no onset and no coda} / {CV: onset, no coda} /
  {CX: has coda, or no vowel (lone-C)}.

Per X, on Tocqueville (primary):
1. SIGNATURE (C1 construction, copied verbatim: e1_3 lag-3 vs 3-state Markov
   expectation; momentum_3 dominant-directed-3-cycle r1 vs r0 one-sided z).
2. RECOVERABILITY: inventory = distinct syllables (n≈1526); contact sets =
   top-10 predecessors ∪ top-10 successors by raw count (mirror
   `rotation_r6.contact_sets`); Jaccard similarity; scipy average-linkage;
   cut k=3; ARI vs true X. Null: 200 size-matched random 3-partitions →
   ARI null; report percentile + empirical p.
3. S2 (secondary, supporting only): cipher A/B/C 3×3 row-normed transition
   matrix (banked phases, repaired stream, R-tokens dropped —
   population-level, no per-group claim; SURVIVES*-grade under N43(c)) vs
   corpus X 3×3 matrix; best-permutation cosine; calibrated against the same
   200 random partitions (percentile reported).

BAR (pre-registered, per X, Tocqueville):
- LIVE refuge candidate iff ARI(X) ≥ 95th pct of random AND lag-3 z>2 AND
  momentum one-sided p<0.05 with r1>r0.
  Pre-run smoke fixes (no data seen): X3 nasal check moved to nucleus+coda;
  momentum_k guards n1==0 or n0==0 (returns degenerate, p=1).
- DEAD as refuge iff it fails recoverability (instrument-blind ⇒ cannot be
  the found phases) OR fails signature (cannot explain the rhythm).
- Les Mis: reported, not bar-driving. Multiplicity: 4 candidates; raw
  numbers reported; any LIVE call carries a Bonferroni-noted caveat.

Pre-registered expectations (to be confirmed or corrected):
- X1: recoverable, signature dead (C1) → DEAD, battery validated.
- X2/X3/X4: unknown; honest run.

Conservativeness notes (pre-registered): orthographic syllabification ≠
encipherer's cuts (attenuates real effects); register proxy (Tocqueville
formal prose vs diplomatic French — phonotactics less register-sensitive
than lexicon); no-aliasing simulation is best-case for recoverability
(kill direction conservative); N43(b): no argument leans on exact χ²
magnitudes; N43(c): no per-group phase claim anywhere in this battery.

## Outputs
- `recoverability.py` → `recoverability.json` (Thread T)
- `SCOPING.md` — the scoping statement (Thread S) + battery verdict
- Report note: `code/crowd8/report_inbox/segmenter-refuge-scope.md`
