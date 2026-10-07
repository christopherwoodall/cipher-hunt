# TUNER — what the three contact phases mean (R5005, Zeschau/Seebach 1841)

Verdict first: **NULL.** The contactor's A/B/C phases do **not** map to word-position
classes (initial/medial/final). Phase-constrained ranking fails to beat an
unconstrained frequency baseline on the known anchors in all four test
configurations, and no A-phase anchor is modal-medial in the era corpus under
either syllabification rule. No shortlists emitted. Full numbers below; raw
tables in `tuner_results.json` (code: `tuner.py`).

## (a) Phase map and the a-priori hypothesis

Phase assignments recomputed from the pair stream against the contactor's
k=12 Jaccard cut: **exact match, 79/79 groups** (A=30, B=26, C=23; R = 17
residual groups, 133 tokens: 00 04 10 13 18 22 27 28 54 55 57 58 73 90 95 97 99).
Pair stream re-verified: 1846 pairs / 96 distinct groups (odd_lines=28, off1=32).

Rotation re-verified independently (block transitions from the pair stream):

| edge | obs | exp | ratio |
|------|-----|-----|-------|
| A→C | 268 | 194.2 | **1.38** |
| C→B | 252 | 155.1 | **1.625** |
| B→A | 243 | 177.8 | **1.367** |
| A→A / B→B / C→C | 152/74/118 | 223.0/141.5/169.7 | 0.68/0.52/0.70 (suppressed) |

chi² = 188.3 on 4 df (contactor reported 181.3; same shape, p ≪ 1e-6 either way).
The rotation is real. The question was only what it *means*.

**A-priori hypothesis** (fixed from the cycle shape + anchor contact signatures,
before touching the corpus):
- **C = word-final** — 29=er: prev A 0.77, next B 0.89 ("er" = classic French
  final syllable; C→B is the word-boundary edge).
- **B = word-initial** — 82=m (prev C 0.61, next A 0.87; elided m' is a
  proclitic onset), 87=ce? (prev C 0.78, next A 0.72; "ce" is proclitic),
  40=e (prev C 0.81, dominated by 29→40 "er-e" ×9 — i.e. preceded by a
  word-final, as a word-initial syllable like *était/école* would be).
- **A = word-medial** — 11=la (next C 0.52 = pre-final), 34=i, 70=pre, 46=que.

**Tune template:** Tocqueville T1+T2 (1835/1840, formal prose — the lane's era
reference), 221,032 words → 387,245 syllable tokens (R1) / 372,955 (R2).
Tokenization mirrors the annealer (split on whitespace/punct incl. apostrophes,
so elided l'/m'/d' become vowelless tokens). Monosyllabic words count as both
initial and final. Two documented rules:
- **R1 (maximal-onset):** the annealer's `syllabify_word` (V|CV, digraphs
  collapsed, qu→Q, final mute-e merged). Inventory: 2,653 types.
- **R2 (coda-maximal):** identical except single intervocalic consonant attaches
  LEFT (VC|V) and final mute-e kept separate (`tuner.py::syllabify_R2`).
  Inventory: 4,191 types. All 10 valued syllables present in both inventories.

## (b) Leave-one-out validation — the NULL

Hide each anchor, rank all corpus syllable types by count in the anchor's
hypothesized phase-position (phase-constrained) vs by total count (baseline).
Best-case ranks (ties favorable). Top-k hit counts:

| config | k=1 PC/BL | k=5 PC/BL | k=10 PC/BL |
|--------|-----------|-----------|------------|
| R1, GT7 (ground truth only) | 0/0 | 1/1 | 1/2 |
| R1, ALL10 (incl. prov 87/64/96) | 0/0 | 1/1 | 1/2 |
| R2, GT7 | 0/0 | 0/1 | 0/1 |
| R2, ALL10 | 0/0 | 0/1 | 0/1 |

Aggregate over 4 configs × anchors: phase-constrained 2/34 top-10 slots vs
baseline 6/34. **Phase-constrained never beats baseline in any configuration.**
Per the pre-registered decision rule, the phase labels (as word-position
classes) are wrong. NULL.

Per-anchor ranks (R1; PC = phase-constrained, BL = baseline):

| anchor | phase→pos | PC rank | BL rank | note |
|--------|-----------|---------|---------|------|
| 11=la | A→medial | 65 | **3** | 'la' is the #3 syllable marginally, #65 medially |
| 70=pre | A→medial | 53 | 59 | bad both ways |
| 82=m | B→initial | 228 | 297 | both useless — elided m' is rare in formal prose (n=250) |
| 34=i | A→medial | 315 | 143 | — |
| 29=er | C→final | 199 | 345 | PC helps but rank 199 is unusable |
| 40=e | B→initial | **5** | 14 | the ONLY anchor where PC clearly helps |
| 46=que | A→medial | 101 | **10** | baseline far better — 'que' is rarely medial |
| 87=ce (prov) | B→initial | 31 | **16** | baseline better |
| 64=qui (prov) | A→medial | 207 | **21** | baseline far better |
| 96=par (prov) | C→final | 42 | **27** | baseline better — phase constraint HURTS |

Modal word-position of each valued syllable in the tune (R1; R2 in parens):

| anchor | phase | hyp | modal (R1) | modal (R2) |
|--------|-------|-----|-----------|-----------|
| 11=la | A | medial | final (0.49) | final (0.50) — medial 0.02/0.00 |
| 70=pre | A | medial | initial (0.74) | initial/final tie (n=108, unstable) |
| 34=i | A | medial | initial (**0.93**) | initial (0.80) |
| 46=que | A | medial | final (0.62) | final (0.54) — medial 0.02/0.00 |
| 64=qui (prov) | A | medial | initial/final tie | initial/final tie — medial ~0.01 |
| 40=e | B | initial | initial (**0.97**) | **final (0.55)** ← rule flip |
| 82=m | B | initial | initial (0.50, tie) | initial (0.77) |
| 87=ce (prov) | B | initial | **final (0.66)** | **final (0.73)** |
| 29=er | C | final | final (0.73) | **medial (0.915)** ← rule flip |
| 96=par (prov) | C | final | **initial (0.67)** | **initial (0.675)** |

Findings:
- **A=medial is falsified outright:** 0 of 4 ground-truth A anchors is
  modal-medial under either rule. 'la'/'que' are final-heavy, 'pre'/'i' are
  initial-heavy. A is not a medial class.
- **C=final is half-supported, half-tense:** 29=er is modal-final under R1
  (0.73) but modal-MEDIAL under R2 (0.915) — the tune cannot even agree with
  itself on the flagship anchor. 96=par is modal-initial under both rules
  (0.67/0.675) — if C were final, 96 would be misphased (tension for the
  provisional 96=par, flagged not killed).
- **B=initial is half-supported, half-tense:** 40=e is modal-initial at 0.97
  under R1 but modal-final under R2 (0.549); 87=ce is modal-final under both
  rules — tension for provisional 87=ce's placement in an "initial" phase.
- Sensitivity: modal positions are **rule-dependent** for 3 of 10 anchors
  (er, e, pre); stable for la, i, que, qui, ce, par, m. The NULL verdict is
  robust — both rules give NULL, R2 strictly worse for phase-constrained.

## The 'er' segmentation mismatch (independent reason the tune is uncalibrated)

- Cipher: 29 = 47/1846 pairs (**2.55%**, freq rank 3).
- Corpus R1: bare-'er' = 146 final tokens / 387,245 (**0.038%**). The infinitive
  mass never yields bare 'er': parler→par|ler, donner→don|ner (3,453
  orthographic -er tokens across 546 types); bare final-'er' comes only from
  -yer/-éer verbs (créer ×48, payer ×16, foyer ×16, …).
- A 67× frequency gap between cipher-29 and corpus-'er'. Either the 1841
  syllabary segments differently than my rule (their "er" group ≠ my bare-'er'
  syllable — e.g. their group may cover the infinitive-final position my rule
  splits as ler/ner/ter), or the register differs wildly. Either way, the tune
  template's segmentation is uncalibrated against the 1841 syllabary — no
  corpus-tuned ranking can be trusted until that mismatch is resolved.

## (c) Verdict: NULL

Phase-constrained ranking does not beat the unconstrained baseline on the
known anchors (2/34 vs 6/34 top-10 slots across 4 configs; never ahead in any
single config), and the modal-position analysis falsifies A=medial while
leaving B/C mixed and rule-dependent. The contactor's rotation (chi²=188.3)
is real, but **the three phases are not word-position classes**. No shortlists
emitted per protocol. The pending shortlist table in `tuner_results.json`
(`shortlists_pending_validation`) is explicitly NOT validated — do not use
without a validated mapping.

## (d) Shortlists

None. Withheld: LOO did not validate.

## (e) Best next step

1. **Drop the word-position reading of A/B/C.** Two concrete alternatives:
   (i) the phases reflect the 1841 syllabary's own table geometry — codebook
   neighborhoods where adjacent numbers share phonetic features — not
   linguistics at all. Test: correlate phase membership with group-number
   proximity (do nearby numbers cluster in the same phase more than chance?).
   (ii) a phonotactic (not positional) alternation — e.g. open/closed syllables
   or vowel-initial vs consonant-initial. The tune tables in
   `tuner_results.json` (per-position counts for 2,653/4,191 syllable types)
   are reusable for this; hand to the phonotactician lane.
2. **Resolve the 'er' segmentation mismatch before any corpus tuning:**
   read `data/upstream-syll*.py` (Bourdeau's segmenters) to see how the 1841
   syllabary segmented infinitive finals; the pencil crib 'er' must be
   interpreted in the syllabary's own segmentation, not mine.
3. **Tensions flagged (not kills — kill authority stays with red team):**
   96=par sits in phase C but 'par' is modal-initial under both rules and the
   phase constraint hurts its LOO rank (42 vs 27) — tension for 96=par's
   placement/value, which inherits 87=ce's provisional status. 87=ce sits in
   phase B but 'ce' is modal-final under both rules. 40=e is the single anchor
   where the positional reading helps (R1 PC rank 5 vs BL 14) — the one
   surviving lead for a positional interpretation, confined to B.
4. Note for the 87=ce red-team review: nothing here confirms or kills 87=ce;
   its phase-B placement is positionally tense ('ce' modal-final), but since
   the phase→position mapping itself is falsified, this is descriptive only.

## Caveats

- Tune = one author's rule-based orthographic syllabification of Tocqueville,
  not the 1841 syllabary's segmentation (proven mismatch on 'er') and not
  diplomatic-despatch register. Both limitations cut against the method, and
  the method still returned NULL rather than a forced positive.
- LOO has only 7–10 anchors; hit-rates are coarse. The modal analysis (which
  uses no ranking) independently falsifies A=medial, so the NULL does not
  rest on the small-n ranking test alone.
- Baseline ranks use best-case tie-breaking; the comparison is fair to the
  phase hypothesis, and it still loses.
- 82=m's corpus support is thin (n=250 R1) — formal prose under-uses elided
  m'; the tune is weak for vowelless tokens generally.
