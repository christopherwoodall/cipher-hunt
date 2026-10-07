# KEY-STRUCTURE analyst report — contact-coherent aliasing (Round 7, work order 6)

Date: 2026-10-07 · Analyst: keystruct (crowd7) · Work dir: `code/crowd7/keystruct/`
Red team holds kill authority over any merger claim. No R5005 key search run;
no annealing. This is a key-maker constraint study.

## 1. What was asked, what was built

F49/N43: uniform-random homophone aliasing kills the rotation (χ²=3.9);
phase-coherent dealing preserves it ⇒ the key-maker dealt aliases
contact-coherently. Work order: INVERT — propose homophone sets via
phase-conditioned contact profiles; test mergers under F33 rules.

**N43 noisy-detector flag applied throughout:**
(a) rhythm existence confirmed (label-free lag-3, not re-litigated);
(b) exact χ² magnitudes (181.3/366.3) never leaned on — my phase-clustering
replication reads χ²=366.3 and I use it only as a replication check;
(c) phase mapping ~0.5 purity — **no merger argument rests on a per-group
phase label alone**; every candidate needs independent (label-free) support.

**Key modeling decision.** The generator deals aliases round-robin across
phases, but the work order asks "which groups share contact profiles *within*
a phase?" — and contact-coherence does not imply round-robin. I treat two
dealing models: (i) **same-phase dealing** (aliases share a phase; directly
testable — contact profiles live in the same group space, no alias-map
circularity); (ii) **cross-phase dealing** (generator-style; profiles not
directly comparable — only rate + complementarity evidence available, graded
weaker). Five of nine case-law candidates are same-phase; four are cross-phase.

## 2. Instruments

**Primary — within-phase contact similarity** (`within_phase2.py`). Phase
labels via the contactor's Jaccard clustering replicated exactly on the
repaired 1,847-pair parse (agglomerative avg-linkage, k=12 cut, 3 largest
clusters → A/B/C; replication check: block χ²=366.3 ✓). For every same-phase
pair: Jaccard similarity on top-10 contact sets (succ∪pred) + cosine on raw
count vectors (α=0.1). Null per phase over pairs with n≥12 (sparse groups
cluster spuriously). Candidates scored regardless of n.

**Secondary — cross-phase battery** (`battery.py`): E1 phase separation, E2
individual coherence, E3 label-free follower/pred Jaccard, E4 merged-vs-single
era cross-entropy fit (Tocqueville full follower/pred distributions, word-space),
E5 phase-explained split (Fisher 2×2 + falsifier rate), E6 merged unigram vs era
(syllable-space primary; word-space secondary), E7 raw top contacts.

**Era rates** (`era.py`, `era_syl.json`): Tocqueville T1+T2, 215,246 words /
394,016 lane-syllabified syllables. F30 respected: NO era-syllable legs for
morphological fragments (er/i/e/m) — M4/M7 get no rate leg.

## 3. Calibration (honest nulls included)

**(a) Same-phase dealing simulator** (`sim_samephase.py`, 3 seeds, 53 true
alias pairs, oracle phase labels): within-phase Jaccard at z>2.8 —
sensitivity 0.04 (2/53), false-positive rate ~0.005, enrichment ~14× over the
2% base rate. **The instrument is weak but informative at the top end**:
a z≈2.8 pair is ~14× likelier to be a true alias pair than a random pair,
but with ~325 null pairs/phase, ~1–2 false positives at that level are
expected. Nothing promotes on similarity alone — the lane's ≥2-checks rule
is load-bearing, not ceremonial.

**(b) Round-robin calibration — VOID.** Two lane-generator instances (own
seeds 184201/184202) failed to materialize rotation (unsupervised χ²=18.8 /
0.6, no detectable cycle) — outside the calibrated band, so no power
conclusions are drawn from them. Recorded as a null, not hidden.

**(c) Specificity control — M9 (06/86).** The F40-RULE-M1 ACCEPTED allomorph
pair (grammatical conditioning, NOT phase aliasing) scores within-phase
Jaccard z=+1.19 — below every serious candidate. The instrument does not
fire strongly on merely-related pairs.

## 4. Candidate results (F33 adjudication)

F33 bar for mergers (adapted from the 06/52/94/78 standard):
**B1** reading-identity (same live sound, no conflicting live reading) ·
**B2** contact-coherence (N43/F49 positive clue) ·
**B3** rate consistency, merged budget vs era (band uncalibrated — soft) ·
**B4** falsifiability (stated rule or explicit free-variation null; no
smuggled unconditioned polyvalence) ·
**B5** ≥2 independent checks. Promotion-grade = all five.

Phases (my labeling; A=32/B=27/C=17/R=20 groups): 87:A, 47:A, 77:C, 00:C,
45:A, 78:C, 29:C, 01:B, 59:C, 37:A, 16:B, 34:B, 43:B, 21:C, 06:B, 86:B.

### M1 {87,47} = "ce" — STRONGEST; conditioned-LEAD, NOT promotion-grade
- B1 ✓: 87="ce" provisional-strengthened; 47="ce" LEAD (F41). Same sound.
- B2 ✓: same phase (A); within-phase Jaccard 0.379, **z=+2.81** (rank 3/325
  in phase A; cosine z=+2.56). Confirms F42's follower-Jaccard 0.435/97th pct
  with an independent metric and a calibrated null. Shared followers:
  11, 46, 77, 78, 86 (+1, 8, 14, 76, 98); both precede 11 ("cela" frames:
  87→11 ×7, 47→11 ×3).
- B3 ⚠: merged 60/1847 = 3.25% vs era ce-syllable 1.10% → **2.96× over**
  (each single in-band: 1.58×/1.38×). Sensitivity: under /sə/={ce,se}
  (0.0110+0.0096=2.06%) the merged rate is 1.58× — in-band. The rate leg
  hinges on whether the cell is spelled "ce" or the sound /sə/ (unestablished).
- B4: **A2 REFUTES the unconditioned merger, sharpened by phase.**
  φ(64)=B=next(A): under same-phase interchangeable aliasing,
  P(64|47) should ≈ P(64|87)=5/32=0.156; observed 0/28,
  binomial p=0.0086. The qui-divergence is incompatible with free
  interchange (this dissolves F42's "not the same ce" into "not the same
  UNCONDITIONED ce"). The surviving form is F41's CONDITIONED aliasing
  (Q1 qui/que-complementarity + Q2 fragment rule) — but Q1 is thin
  (Fisher 0.0476) and 13/28 of 47's frames are unclassified = free cases.
  Fails F33 zero-free-cases.
- B5: only ONE independent check for the merger (similarity; rate is
  adverse-literal). Not met.
- **Verdict: unconditioned {87,47} merger REFUTED (A2 + phase-sharpening,
  p=0.0086). Conditioned homophone set ("ce", Q1/Q2-conditioned) stays
  LEAD-grade — inherits 87-prov + 47-LEAD, sharpened, NOT promotion-grade.**
  Phase contribution: same-phase dealing (not round-robin); the alias
  choice, if real, is lexically conditioned, not phase-dealt.

### M2 {77,00} = "le" — REFUTED as merger
- B1 ✓-ish (77 prov-cond, 00 "le" LEAD) but 00="pour" is STRONG LEAD and owns
  00's mass. B2 ✗: same phase (C) yet similarity **z=−0.56 (null)** —
  no contact support. B3 ✗: merged 2.60× over era le-syllable; each single
  in-band (1.16×/1.44×). The shared top follower 86 (77→86 ×5, 00→86 ×12)
  is explained by 86's stem polyvalence (F40), not aliasing.
- **Verdict: REFUTED.** (00's "le"-islet remains a WO-2 conditioned-polyvalence
  question, not a homophone merger.)

### M3 {78,45} = "me"-syllable — INSUFFICIENT
- Cross-phase (C/A): no within-phase test. B3 ✗: merged 3.78× over era
  me-syllable (singles 2.21×/1.57×). Only leg: F50's "même" word reading
  (LEAD, stands on its own) + weak complementarity (E5 Fisher p=0.0057,
  falsifier rate 0.53 — the round-robin rule does not describe this pair).
- **Verdict: INSUFFICIENT** — one weak leg; 78's polyvalence (me/ver, F33)
  must be respected by any future claim (M3 uses 78-as-me only).

### M4 {29,78} = "er" — INSUFFICIENT
- Same phase (C), similarity z=+1.35 (weak). B1 ⚠: 29 GT, but 78's
  "er"-reading is a 2-window islet (n_eff=1, LEAD fork ver/er per T4 ruling).
  B3 barred (F30). **Verdict: INSUFFICIENT** — the islet needs the T4 ruling's
  independent support (second non-byte-identical window, or 78="er" evidence
  outside T4) before any merger claim.

### M5 {01,59} = "est" — INSUFFICIENT
- Cross-phase (B/C): no similarity test. B3 ✗: merged 2.76× over era
  word-"est" (each single in-band: 1.35×/1.40×). S4 adverse (59→46 "est que"
  5.4×) and the 01-interaction still block 59's promotion (F45).
- **Verdict: INSUFFICIENT.**

### M6 {37,77} = "le" — INSUFFICIENT (one weak leg)
- Cross-phase (A/C): no similarity test. B3: merged 1.89× — **in-band, the
  only candidate whose merged budget fits** (singles 0.74×/1.16×). But rate
  consistency is also satisfied by 77-alone; 37="le" is only MEDIUM;
  77 is contact-messy (coh 0.443). Exactly one weak leg.
- **Verdict: INSUFFICIENT.** Discovery note: (37,87) scores z=+3.0
  within-phase — reading-incompatible (le vs ce), i.e. functional
  (determiner) similarity, a standing confound for this instrument.

### M7 {16,34} = "i" — CONDITIONAL (hold for WO-4)
- Same phase (B), similarity z=+1.83 (moderate; 34 n=11 below null floor).
  B1 ✗: 16="i" UNCONFIRMED (battery pending, work order 4). B3 barred (F30).
- **Verdict: CONDITIONAL** — rerun the day 16="i" confirms; then M7 enters
  as a LEAD-grade candidate (phase-B + z=1.83 + GT 34).

### M8 {43,21} = "me" — REFUTED
- Cross-phase (B/C). B3 ✗✗: merged 3.28× over era me-syllable (32.9× over
  word-"me"); zero shared followers (j_s=0.000). 43="me" is WEAK.
- **Verdict: REFUTED.**

### M9 {06,86} stem-allomorphs — CONTROL (not a merger candidate)
- F40 RULE M1 ACCEPTED (grammatical conditioning, not phase aliasing).
  Within-phase z=+1.19: correctly weak — specificity control passed.

## 5. Ranked proposals

| rank | set | reading | grade | decisive evidence |
|---|---|---|---|---|
| 1 | {87,47} | "ce" (conditioned) | LEAD (not promotion-grade) | z=+2.81 similarity; A2 refutes unconditioned form (p=0.0086) |
| 2 | {16,34} | "i" | CONDITIONAL on WO-4 | z=+1.83; 16="i" unconfirmed |
| 3 | {29,78} | "er" | INSUFFICIENT | z=+1.35; islet n_eff=1 |
| 4 | {37,77} | "le" | INSUFFICIENT | merged rate 1.89× in-band only |
| 5 | {78,45} | "me" | INSUFFICIENT | F50 word-LEAD only |
| 6 | {01,59} | "est" | INSUFFICIENT | rate 2.76× over |
| 7 | {77,00} | "le" | REFUTED | similarity null; rate over |
| 8 | {43,21} | "me" | REFUTED | rate 3.28×+ over; j_s=0 |

**Promotion-grade: NONE.** No candidate meets B1–B5. The strongest result is
negative-and-precise: M1's unconditioned form is refuted, its conditioned
form sharpened — a key-maker constraint (same-phase, lexically-conditioned
aliasing for "ce"), not a solver input.

## 6. Key-maker constraints established (for the lane)

1. **Same-phase dealing is live in this key**: M1's pair shares a phase AND
   38% of top contacts. The generator's round-robin is not the whole story;
   the key-maker used same-phase coherent aliasing at least for "ce".
2. **Interchangeability is falsifiable per pair**: the phase model turns
   A2-style divergences into sharp tests (M1: p=0.0086 vs interchangeability).
   Future alias claims must survive this test, not just show similarity.
3. **Functional similarity is the standing confound**: top discovery pairs
   (37,87) z=3.0, (46,86) z=3.03, (29,52) z=2.68 are reading-incompatible —
   high within-phase similarity alone never licenses a merger. B1
   (reading-identity) screens first, always.
4. **Rate-additivity pattern**: for M1/M2/M5/M8 each single alias already
   fills its syllable's era budget — mergers double-count without a register
   effect or a /sə/-style sound-cell hypothesis. M6 is the exception
   (neither single fills "le" alone).

## 7. Caveats & open threads

- Phase labels ~0.5 purity (N43c): the similarity z-scores use labels only to
  define the comparison set; the Jaccard itself is label-free. Cross-phase
  candidates (M3/M5/M6/M8) have no similarity instrument — their grades are
  weaker by construction, not by evidence.
- Era band uncalibrated (red team): B3 ratios are reported, never dispositive
  alone. The /sə/ sensitivity for M1 is flagged, not adopted.
- E4 (merged-vs-single era fit) was INCONCLUSIVE on real data (known
  follower sets 17–35 tokens, word-space/syllable-space mismatch) — graded
  as such, not as adverse.
- Discovery pairs (42,49) z=2.84 and (76,78) z=2.33 are reading-less/
  reading-partial — noted for future reading work, not proposed as sets.
- The (37,87) z=3.0 determiner-similarity may matter for 37's readers;
  left as an observation.

## 8. Files

- `code/crowd7/keystruct/aliasing.py` — loader, phase labels, profiles
- `code/crowd7/keystruct/calibrate.py` — voided round-robin calibration
  (+ `calibration_pairs.json`)
- `code/crowd7/keystruct/sim_samephase.py` — power/specificity sim
  (+ `samephase_power.json`: sens 0.04 @z>2.8, fp~0.005, ~14× enrichment)
- `code/crowd7/keystruct/era.py` — Tocqueville word rates
  (+ `era_rates.json`, `era_syl.json`)
- `code/crowd7/keystruct/battery.py` — cross-phase battery (+ `battery.json`)
- `code/crowd7/keystruct/within_phase.py`, `within_phase2.py` — similarity
  (+ `within_phase_sim2.json`, `phase_cache.json`)
- This report: `code/crowd7/report_inbox/keystruct-aliasing.md`
