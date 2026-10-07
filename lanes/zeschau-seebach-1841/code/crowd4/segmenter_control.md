# SEGMENTER round 4 — PRE-REGISTERED control spec (written BEFORE any control run)

Lane: zeschau-seebach-1841. Instrument under test: crowd3/segmenter.py STRUCT path
(semi-Markov forward-backward, unsupervised EM-fit boundary rates, rotation-break
assumption only). Scorer lesson N16: no instrument touches R5005 before validating
on a control.

## 1. Control construction (fully synthetic, zero target data)

Source text: Tocqueville 1835/1840 (data/gutenberg-30513-tocqueville-t1.txt,
data/gutenberg-30514-tocqueville-t2.txt) — era corpus only, not target-derived.
The control slice is EXCLUDED from the era word-length prior used in the control
run (prior rebuilt from corpus-minus-slice; the R5005 run's prior is untouched).

1. Take ~1,100 consecutive words from t1 (words 50000–51100), lowercase, strip
   punctuation. Syllabify each word with crowd/anneal.py `syllabify_word`
   (R1 maximal-onset) — the same routine as the R5005 prior.
2. Syllabary: the 96 most frequent synthetic-slice syllables each get a 2-digit
   code. Words containing any out-of-top-96 syllable are dropped from the slice
   (keeps the inventory closed; mirrors R5005's 96-group inventory).
3. Rotation model (the hypothesis under test): each syllable has 4 homophone
   variants, one per track A/B/C/R. Within a word the encipherer advances the
   track along the cycle A→C→B→A (matches R5005's within-favoring edges
   A->C, C->B, B->A, which carry negative s in the real STRUCT model).
   - At each true word boundary: with prob q_break=0.70 the track BREAKS
     (jumps to the R "reset" variant); with prob 0.30 it continues the cycle
     (inconsistent encipherer).
   - Mid-word spurious break with prob q_mid=0.04 per syllable (jump to R
     variant once, resume cycle afterwards).
4. Ear-cutting noise (round-3 enlightenment: encipherer spells by ear, cuts
   inconsistently — « personne » two spellings):
   - p_merge=0.08: two adjacent syllables within a word merge into one group
     (merged-syllable code, e.g. "per-son-ne" → "per-sonne").
   - p_split=0.04: one syllable splits into two groups (fragment codes).
   - p_alt=0.06: alternate spelling of the syllable (final-e drop etc.).
   Ground truth is recorded at the GROUP level after all noise is applied.
5. Stream: ~1,100 words → ~1,900 groups, comparable to R5005's 1,846 pairs.
   Random seed fixed (rng=20261007) for reproducibility.

Phase map for the control run: the synthetic track labels (A/B/C/R) directly.
KNOWN GAP (stated, not hidden): this tests segmentation *given correct phases*;
the R5005 phase map came from the contactor's unsupervised k=12 clustering,
which the control does not re-test.

## 2. Instrument run on the control

Exact copy of the segmenter.py STRUCT procedure, no target data anywhere:
  - M = control stream's own block-transition matrix (Laplace-smoothed per row)
  - Pb = control stream's column marginals ("boundary resets the phase")
  - EM-fit per-row boundary rates π_a (damped, 20 iters max), init from
    control-era mean word length
  - w(e)=log(Pw(e)/M(e)), s(e)=log(Pb(e)/Pw(e)); semi-Markov forward-backward
    with KMAX=12 and the control-era word-length prior
  - boundary confidence conf[p] at every inter-group position p

## 3. Pre-registered PASS/FAIL threshold

Compared against the synthetic ground-truth word boundaries (group level):
  - (M1) Boundary RECALL at conf ≥ 0.5: **≥ 0.60**
  - (M2) Internal positions with conf < 0.5: **≥ 0.70**
  - (M3) mean(boundary conf) − mean(internal conf): **≥ 0.10**
PASS = all three hold. FAIL = any one fails → STOP: no drag, null reported,
targets untouched. No post-hoc threshold movement.

Sanity side-note (not pass/fail): the control's fitted s-values are reported
for qualitative comparison against the real STRUCT s-values
(R->C +12.62, B->B +12.53, R->B +4.12, …), to check the control's signal sits
in the same ballpark rather than being trivially easy.

## 4. Drag protocol for the 25 crib-drag targets (runs ONLY if control PASSES)

Priority: @1110-1112 [41 65 38] first, @81-83 [51 62 16] second, then the
remaining 23 in STRUCT-score order from
code/crowd3/segmenter_results.json['crib_drag_targets_STRUCT'].

Current values usable as hard constraints:
  ground truth: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que
  provisional: 87=ce (strengthened), 64=qui, 96=par (CONFIRMED 4/4)
  lead-grade: 62=on (promotion candidate; readings leaning on it are marked
  lead-conditional, inheriting provisional×provisional uncertainty)
Targets by construction contain no ground-truth/provisional groups EXCEPT 62
(@81-83 [51 62 16], @1703-1705 [62 94 88], @507-509 [77 62 94],
@1538-1540 [62 93 88]).

Lane rule F30: rigid syllabification DEAD — no era-syllable-conditional legs on
morphological fragments; era word-space (whole-word) legs survive.
Round-3 enlightenment: the encipherer cuts inconsistently, so a target's group
count may be ±1 vs a candidate word's clean syllable count; any reading that
uses the ±1 slack is marked cut-tolerant (weaker).

Per target:
  1. Pull MAP span geometry from segmenter_results.json (flank conf, inner max,
     phases, score).
  2. Enumerate candidate French words from the Tocqueville corpus (era
     register) with syllable count == group count (±1 with cut-tolerant flag),
     using `syllabify_word`; syllable slot must match known values where a
     group has one.
  3. A proposed reading needs ≥2 INDEPENDENT checks from this menu:
       (G) geometry: flank conf ≥ 0.90 both sides AND max inner conf < 0.35
           (STRUCT MAP, already computed round 3)
       (L) era-lexical: candidate word occurs in Tocqueville corpus ≥ 3×
       (F) frequency-rank: the target groups' stream-frequency ranks sit
           within a factor-3 band of the candidate syllables' era
           syllable-frequency ranks (counts only — independent of geometry)
       (X) cross-occurrence: ≥1 group of the target recurs in another
           dragged target (or a cribbed span) at a syllable slot consistent
           with the proposed reading (shared-syllable consistency)
       (I) independent instrument: another lane instrument's output
           (bigram_closer legs, stem_hunter, attempt3 phonotactician values,
           tuner) independently supports ≥1 proposed syllable
  4. Verdicts: PROPOSED (reading + ≥2 checks, checks named) | LEAD-held
     (<2 checks; best candidate named if any) | KILLED (a check contradicts a
     ground-truth value, or forces one group to two different syllables).
     A reading leaning on 62=on stays lead-conditional even with 2 checks.

Nulls are first-class. No ciphertext invented; every number traces to a lane
file. No GitHub push. R5005 only.
