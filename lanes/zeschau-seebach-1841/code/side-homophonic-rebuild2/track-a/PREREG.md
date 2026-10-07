# PREREG — Track A: register-gap hypothesis test (2026-10-07)

**Question (fleet charter):** is the rebuilt solver's failure caused by the
register gap (Tocqueville-trained LM scoring 1862 literary French synthetic
plaintext) or by the language-model family itself?

**Status:** PREREG + step-2 reference build only. NO scored comparison has
run. `rescore_reg.py` is written but NOT executed; it runs only after the
red team signs off in `redteam/RULINGS.md`.

## 1. Hypotheses (binding)

- **H0 (register gap is the blocker):** the Tocqueville→Les-Mis register gap
  makes the LM prefer adversarial morpheme-salad over register-gapped truth.
  Prediction: under a register-matched (diplomatic-corpus) reference, the
  planted 184101 truth decode beats the frozen pilot-salad decode by
  **≥ +500 nats**, while salad wins under the Tocqueville reference.
- **H1 (LM family is the blocker):** the 5-gram + lexicon family cannot
  separate real French from adversarial salad at any training register.
  Prediction: the frozen salad still beats truth by **≥ +500 nats** under
  the register-matched reference.
- **Inconclusive:** diagnostic margin in (−500, +500) → neither hypothesis
  supported → NO pilot anneal without a new PREREG (re-registration).
  (Red-team criterion: "diagnostic positive" ≡ H0 margin ≥ +500 exactly;
  charter: anneal "ONLY if diagnostic positive".)

The ±500 band is ~19% of the measured 2,601-nat Tocqueville margin — an
honest acknowledgment that register may explain part, not all, of the gap.

## 2. Diagnostic rescoring protocol (step 3, post sign-off)

- **Decodes:** planted 184101 truth vs frozen pilot salad (restart 199939,
  npoly=0), on the 184101 cipher stream (1,846 pairs, 96 groups).
  Key construction mirrors `verifier/verify.py` exactly (anchors → anchor
  values; non-anchors → planted primary; secondaries → sec[0] with w2=0.5
  init; salad w2 from the pilot artifact).
- **Instrument:** `track-a/rescore_reg.py` — the INDEPENDENT verifier rescorer
  (`verifier/rescore.py`) with a single documented deviation: the `lm.json`
  path is overridable. All scoring code (CharLM, E-step, phonetics, phase,
  `_cover_sum`, `score()`) is the verifier's, untouched.
- **(a) Tocqueville reference** (`solver/lm_ref/lm.json`) — SANITY: the
  margin (salad − truth) must reproduce the verifier's **+2,601.0 nats to
  ≤ 1 nat**, else STOP (instrument broken).
- **(b) Register-matched reference** (`track-a/lm_ref_diplo/lm.json`,
  §4) — DIAGNOSTIC.
- **Config:** shipped `solver/config.json` (word_minlen=6, λ_poly=50,
  λ_conc=5, conc_cap=6, λ_word=1.0, β0=2.0). The phase gate is computed from
  the cipher stream itself, hence identical across (a)/(b); S_potts is
  reference-invariant.
- **Report:** full part-by-part tables for both decodes under both
  references (S_char, S_cov, S_single, S_word, S_potts, S_conc, n_poly,
  total, decode_len, per-pair rate) plus per-part (b)−(a) deltas for truth
  and salad separately. Artifact: `track-a/results/rescore.json`.

## 3. Decision rule (verbatim, pre-registered)

Let `M_d = total_salad − total_truth` under the register-matched reference.
- `M_d ≤ −500` AND sanity (a) reproduced → **H0 supported** (diagnostic
  positive).
- `M_d ≥ +500` AND sanity (a) reproduced → **H1 supported**.
- `M_d ∈ (−500, +500)` → **INCONCLUSIVE** → no pilot anneal without
  re-registration.
- If sanity (a) fails → no verdict; diagnose the instrument.

## 4. Register-matched reference (BUILT — step 2, this PREREG)

Builder: `track-a/build_ref.py`. Construction is VERBATIM the frozen
Tocqueville pipeline (`code/side-homophonic/solver/build_lm.py`): token
regex, projection, spaceless char stream, char 1..5-gram nested counts,
lexicon rule (freq ≥ 3, projected len ≥ 4, dedup freq-summed, top 40,000,
wt = log1p(freq)), held-out perplexity (first-90% train / last-10% test,
order-5, α=0.5). The rebuild solver's `phonetics.py` is BYTE-IDENTICAL to
the frozen one (verified by empty `diff`), so the projection matches the
Tocqueville `lm_ref` build exactly.

### 4.1 Corpus composition (all under `code/side-period/corpus/`)

| file | sha256 | words |
|---|---|---|
| guizot-memoires-t5-t6.txt | 3b6f4c1eb5bff6f1a4a30c4c14b3c323ec4a0a36ebaf015d749d6ff0a904a871 | 298,616 |
| nesselrode-v7.txt | 6879f818054f0b14a1d7d9efac9696319a1a6bd02e46ab784617d31ca14b8a53 | 78,958 |
| nesselrode-v8.txt | 699d5afab3656f0341a5475099841c34e4d402c486ebf4d4a803276a8a3301ca | 92,594 |
| nesselrode-v9.txt | 078a771c456abf8db17cdf83c483c4eccb3b1d5fd19978a3158571a3364de5ed | 85,248 |
| nesselrode-v10.txt | 74dc194f1f857d6b4909e737f87ebcad4e62b997ef9a049c807eced1a5bd51ec | 82,436 |
| revue-deux-mondes-1841-q1.txt | 6bb18f457a9f2152d1b3d85a4211be612fdb7526ecbc9ab149272d6bb3b34f86 | 458,783 |
| revue-deux-mondes-1841-q2.txt | 8f2b8c935986d80a75fed4d0cc438622eb5229cd9f898445c45a5fe9ea1f0b1e | 449,302 |
| revue-deux-mondes-1841-q3.txt | 14b46d9d1c2415ea294a94b8c9473829e7eb44a32bf4176f6ccc9275e9806ea2 | 462,825 |
| revue-deux-mondes-1841-q4.txt | b7204a2c1b51a253ea958003e4ce009c9dfa3271d34a45c72d46c4267d0dc09e | 477,912 |

Guizot t5–t6 = his 1840–42 despatches (best register match to the 1841
task); Nesselrode v7–v10 (v8 = full 1841 run); Revue des Deux Mondes 1841
all four quarters. Total ≈ 2.49M words.

### 4.2 Les-Mis-free proof (leakage rule)

**Rule:** word-20-gram overlap scan against
`data/gutenberg-17489-miserables1.txt` — the sealed-truth plaintext source
itself, so "0 on truth-slice content" is directly tested.
**Result: 0 shared word-20-grams across all 9 files** (per-file counts all
0; 119,485 distinct Les-Mis 20-grams tested). The reference cannot have
memorized the sealed truth. (Scan script ran 2026-10-07; deterministic.)

### 4.3 Exclusions + subsample (pre-registered, executed)

- Guizot word offsets **[100000, 104000)** and **[200000, 204000)** were
  REMOVED before any other step — reserved as Track-A instance truth
  plaintext (§5). The reference never sees them.
- Deterministic shuffle (`random.Random(184101)`) of the concatenated,
  span-excluded word list; first **215,000** words kept — size-matched to
  Tocqueville's 214,861 so the test isolates REGISTER, not corpus size.

### 4.4 Built artifact

`track-a/lm_ref_diplo/lm.json`
sha256=`5018f44c1bcf0d1d0bb8e02b72a6e6f142df973fa20b077cc11f4c650a8c147b`
(+ `lm_stats.md`; build 2026-10-07T19:22:10Z, wall 21.3s, seed 184101).

| stat | Tocqueville ref | diplomatic ref |
|---|---|---|
| words | 214,861 (distinct 11,870) | 215,000 (distinct 23,961) |
| projected chars | 775,949 | 756,241 |
| alphabet | 30 | 30 (identical set) |
| distinct 5-grams | 134,855 | 233,156 |
| held-out per-char logp / ppl | −1.8594 / 6.42 | −2.6133 / 13.64 |
| lexicon size | 3,546 | 4,776 |

**Documented caveat (not hidden):** held-out perplexity 13.64 > 6.42. The
9-source, deterministically shuffled corpus is more heterogeneous than
single-author Tocqueville (genre mix + OCR noise). The H0/H1 test is
comparative (truth vs salad under the SAME reference), so the inference
stands, but the reference is a noisier French model than Tocqueville's.
Top lexicon forms are diplomatic-register (`avec, cete, meme, come, leur,
tute, otre, etre, …, guvernemA, politike, …`) — the intended register.

## 5. Step-4 pilot pre-registration (ONLY if diagnostic positive)

### 5.1 Two register-matched synthetic instances

- **Seeds:** 184301, 184302 — new (not in 184101–184106, not in
  184201–184204/184206/184207, not in 184213–184218).
- **Plaintext:** guizot-memoires-t5-t6.txt word spans [100000,104000)
  (→ 184301) and [200000,204000) (→ 184302) — the §4.3 excluded spans.
- **Builder:** `track-a/build_instances.py` (written only after a positive
  diagnostic), importing `build_instance` / `write_instance` from
  `side-homophonic-rebuild/control/generator.py` with `tokens` = the
  4,000-word slice (idx-0 scheme) and `p` = PARAMS verbatim except
  `seeds=[<seed>]` and `q_cycle=0.5` fixed (already calibrated; no
  recalibration). `T` nominal 56. Output to `track-a/instances-reg/`
  (NOT the lane `instances/` dir — no confusion with sealed batches).
  Keys held by Track A; they are Track A's own control, not the lane gate.
- **Deviations from CONTROL-DESIGN.md (complete list):** plaintext source
  (diplomatic slices instead of Les Mis); seeds; output directory. As a
  consequence the instance is register-MATCHED to the reference — this is
  the test (the original control was deliberately register-gapped).
  Everything else identical: cell pipeline (syllabify → p_er_free=0.8 →
  p_letter_split=0.03 → ear noise p_mute_e=0.15 / p_merge=0.10 /
  p_split=0.05 / p_alt=0.08), 96 R5005 group labels, 7 anchors pinned,
  6 polyvalent islets, phase q_cycle=0.5, 1846-pair covering window,
  "la première" scrub + planted crib (force-cut pre|m|i|er|e).
- **Per-instance sanity (reported, not a bar):** 1846 pairs / 96 groups;
  crib `11-70-82-34-29-40` reads exactly once; occurrence-phase χ² in the
  calibrated band [181, 320].

### 5.2 Short pilot anneal

Per instance (current rebuilt method, register-matched reference):

```
python3 side-homophonic-rebuild/solver/solver.py \
  --pairs track-a/instances-reg/SYNTHETIC-ct-184301.pairs.txt \
  --lm track-a/lm_ref_diplo/lm.json \
  --out track-a/pilot-reg/184301 \
  --anchors-file track-a/instances-reg/SYNTHETIC-crib-184301.json \
  --no-soft --seed 184301 --restarts 3 --iters 40000
```

(same for 184302). 3 restarts × 40k = 120k total anneal iters per instance
= 1/4 of the frozen 12×40k = 480k batch. `--no-soft`: soft priors are
R5005-specific. Anneal seed = instance seed; restart seeds derive
deterministically as `seed + 7919·r` (solver.py). Shipped `config.json`
otherwise (T0=60, refine on, inventory `crib`).

### 5.3 Pilot bar (pre-registered)

**PRIMARY recovery ≥ 0.10 on BOTH instances = H0 confirmed behaviorally**
(the 0.10 per-instance floor is the control's registered bar,
CONTROL-DESIGN.md §4). SECONDARY reported (no bar). Anything else → the
numbers are reported honestly with no claim beyond them. Metrics per
CONTROL-DESIGN.md §4 definitions (PRIMARY: exact planted primary, 89
non-anchor groups; SECONDARY: decode accuracy over 1,846 pairs), computed
against Track-A-held keys.

### 5.4 Cross-track contamination

Track B must exclude guizot spans [100000,104000) and [200000,204000) from
any training manifest (red-team R-B leakage rule). Track A's reference
already excludes them (§4.3).

## 6. Standing constraints (acknowledged)

1. NO R5005 contact. Control/diagnostic only.
2. The sealed 184101 truth read is forensics-class (opened in round 1 per
   CLOSING-VERIFICATION §caveats): used ONLY for the diagnostic rescore,
   never for training, lexicon construction, or solver priors. Labeled as
   such in the report; it is NOT a control pass.
3. Deterministic; all seeds logged (§4.3: 184101; §5.1: 184301/184302;
   §5.2: anneal seeds = instance seeds, restarts `seed+7919·r`). Results
   must reproduce from these seeds.
4. No scored comparison before red-team sign-off in `redteam/RULINGS.md`.
5. Repair-direction implications (for the report, not the verdict):
   H0 → the LM training register was load-bearing; repair = register-matched
   reference + fresh-batch gate decision. H1 → the 5-gram+lexicon family
   cannot separate real French from adversarial salad at any register;
   repair must change the model family (word-level / boundary / neural),
   not the training text. Inconclusive → re-register before any anneal.

---
Track A subagent, 2026-10-07. Awaiting red-team review.
