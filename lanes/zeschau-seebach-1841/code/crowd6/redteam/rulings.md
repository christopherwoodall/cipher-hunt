# RED TEAM — Round 6 rulings

Date: 2026-10-07. Kill authority over every round-6 promotion claim.

Session docket: Frenchman, Morphologist, Bigram Closer, Scorer Smith,
Segmenter, Closer, Inventorist — claim packages expected in
`code/crowd6/` (executor-local dirs) plus report-inbox notes per REPORTING.md.

## Armed baseline

`code/crowd6/redteam/verify_baseline.py` — extends the round-5 instrument
(`code/crowd5/redteam/verify_baseline.py`, 30/30 PASS, left untouched):
30 inherited checks + 19 round-6 additions. **49/49 PASS** on this machine
against the canonical repaired 1,847-pair stream
(`code/side-keyhunt/repair_parse.py` + `repaired_offsets.json`).

Corrections armed (memo 2026-10-07, re-verified): n62=35 (sidepath's 34
superseded; N28 carries 9/35), n24=52 (unmoved), n52=27 (unmoved),
n06=44 (repaired; old-parse 46), n78=31, 47→64=0.

Round-6 additions (all verified against the stream): 59→46 ×2 @[216, 1190]
(n59=27); 46→62=0 (double-duty datum, N35); full 62 follower/predecessor
profiles (both sum to 35=n62 — complete accounting); 64-77-84 trigram
×3 @[144, 1445, 1801] (n_eff=1 — N27); 64-77-84-59 quad ×2 @[1445, 1801]
(F42 refinement); 87→01 ×2 @[344, 1028] + 47→01 @[194] (F42 A1 "c'est");
87→11 ×7 (A5 structural); 78→45 ×4 @[313, 573, 982, 1164] (45="me" drag
targets); n45=22; 00→46 ×4 @[106, 545, 1545, 1680] ("pour que", F40);
67→11 ×4 @[561, 669, 753, 996] / 11→67 @[1044] (F42 chiasmus);
n67=38, n84=25, n43=16; 96→43 ×2 @[342, 1026] («par 43» ×2).

## Standing bars (non-negotiable)

- ≥2 independent checks per promotion. Instrument independence audited per
  claim, not per check count: two checks from the same instrument are ONE
  check (N28; the 62="on" legs-1&3 precedent).
- N28: ear-contaminated legs fail. The N35 ruling is the case law: subject-
  battery framing with an undisclosed ear premise, an asserted by-ear merger
  asymmetry inside a "non-ear" leg, χ² with 3/4 cells exp<5 (overstated
  precision — exact-test it), recycled datums re-entered without independence
  accounting, provisional/LEAD-anchor leaning unfenced.
- F33-grade conditioning for any polyvalence claim: falsifiable positional/
  lexical rules, zero free polyvalence. A single verified unconditioned
  1-group→2-sounds case breaks F33.
- Traceability: every .md number must reproduce from archived code on the
  repaired stream (round-3's trust-JSON-over-md lesson; F26-11).
- No double-counted data (N35's 46→62 lesson: one datum, two uses — the
  discriminative use must be independently licensed).
- No recycled cells across legs (the Check-C ne-cell failure: exact p=0.045
  full → 0.0675 minus the recycled datum).
- Anchor-preserving controls on all drags (N34: shuffling de-anchors windows;
  controls must preserve anchor positions).
- Provisional vs GT status marked on every claim; provisional anchors
  propagate their status to everything built on them (round-3 precedent).
- F30: rigid syllabification is DEAD — no era-syllable-conditional legs on
  morphological fragments (29/82/34 excluded; 40-conditionals excluded);
  era word-space legs survive; fragment hypotheses test against the
  crib-learned unit inventory (F44), never `data/upstream-syll*.py`.
- N22 calibration exclusions enforced in every rate leg; the factor-2 band is
  UNCALIBRATED (F20) — not a kill-or-pass instrument.
- No null groups (cross-fleet standing constraint; petit-chiffre has none).

## Standing kill conditions per docket

### 1. Frenchman — 62="on" non-ear discrimination; follow 59
Current: STRONG LEAD on ear lock + 62→94=9/35=0.2571 (2.18× era, repaired;
9th @761) + fresh-window subject triangulation (26 windows, zero
counterexamples, /ɔ̃/ rivals killed). Promotion needs a NON-EAR leg:
follower/predecessor profile with n≫2 in the INDEPENDENT cells (baseline
arms both profiles), or a word-space grammatical on-vs-il asymmetry, or an
independent "qu'il"-merger calibration from the cipher's own elision/merger
habits. KILL the leg if: ear-contaminated (N35 case law applies by name);
recycles 62→94; divides by a wrong marginal (N20 failure mode); uses 46→62
as the independent leg (one datum, two uses); leans on 87/64/96-provisional
unfenced (64="qui" blocking "qui" is a provisional-anchor dependency).
Adverse standing: unigram favors "il" 1.50× over "on" 2.59×.
59→46 ×2 @[216, 1190] is a verb-candidate lead, not a 62 leg.

### 2. Morphologist — 96 conditioned-verb battery ("ce qui __ ce que"); Q2
fragment sound; 06 stem
47="ce" promotion is BLOCKED on the @148–152 64-slot residual (F41 —
worker's own call, upheld). The battery unblocks only if it resolves the
residual or delivers an equivalent independent leg; the ranked #1 unblocker
(96 conditioned-verb in "ce qui __ ce que") is the lane's most-wanted leg.
F33-grade conditioning required for any polyvalence claim; no unconditioned
47=ce∥47=me. The cela-tension (B2=121.5) must be addressed, not waved
(F26-13). No recycled cells across legs (Check-C precedent). Q2's fragment
sound is UNIDENTIFIED — any claim identifying it needs ≥2 independent legs.
06 stem: single-stem-for-all-06 is KILLED (17.1×); the 66× "demand*" rate gap
is the baseline any specific-stem claim must clear; F30 bars era-syllable-
conditional legs on 06 (morphological fragment).

### 3. Bigram Closer — 77="le" exploit (identify 84; "le me"×7 dissolution
dependency; 78-window drag incl. 45="me"); 00="pour" battery
77="le" is provisional-CONDITIONED (F37 — the lane's only promotion):
the "gou"@1180/@1351 exception is FENCED (trigger unconfirmed, n_eff=1);
the "le me"×7 dissolution is conditional on 78="me"-syllable-LEAD — IF that
LEAD falls, a kill-grade adverse revives (dependency recorded on the
promotion). 78 COEXIST stands (F38): me-WORD disfavored-strong, me-SYLLABLE
LEAD, "ver" islet LEAD n_eff=1; no category errors (the N25 dissolution is
conditional on the syllable LEAD, not general). 84 is unresolved (84="fait"
killed 6.7×); identifying it needs ≥2 independent legs — the 64-77-84-59
quad ×2 refinement and the 87-64-77-84 @1800 frame are armed. All drags:
anchor-preserving controls (N34); no hand-computed-in-no-code legs (N21
precedent). 00="pour" (F40: 00→46 ×4, 06→00 ×4) needs its own ≥2-check
battery — NOT adjudicated until then.

### 4. Scorer Smith — objective repair per N36, then re-run the control
N36 is an ORDER, not a suggestion: fix lam_poly scale (truth beats annealed
only at lam_poly < 0.09; configured 10) + import side fleet's phonetic
projection + spanning word bonus + concentration penalty (ordered list in
`code/crowd5/scorer_identifiability.md` §4–5). Then re-run the CONTROL; then
re-judge search vs identifiability. Gate holds until a control passes —
NO R5005 run (N30's basin test: no basin around truth; the landscape slopes
away). Control-first rule (N5/N12/N16): a failed control voids real-data
claims. Any claim positing null groups is pre-voided (standing constraint).

### 5. Segmenter — rotation follow-ups
Work orders: (1) labeling-robustness battery (cosine metric, k=8/16,
half-stream clustering); (2) 3-state HMM vs 96-group bigram model, held-out
BIC; (3) reconcile the label-agreement discrepancy (69/96 here vs N30's
"61/96 change"). KILL conditions: any phase→position mapping claim is VOID
per N15 (tuner-falsified instrument); a rotation-break drag that only
reproduces the chi² is a re-derivation, not a claim — falsifiable positive
claims only ("consistent with X" does not promote); must coexist with F33
(verified conditioning rules, not free polyvalence). The period-3 rhythm
(F43: lag-3 z=+5.6, p≈1e-8; leading hypothesis = enciphering-process column
geometry) is discovery-grade, not identification.

### 6. Closer — resolve 84 or another non-circular anchor; 67
classification; 43="me" pressure; "la veut" @1044–1045
87=ce promotion requires a non-circular anchor or leg: N3's "parce que"
frame was admitted CIRCULAR (conditions on 96="par"); R1 recycled the dead
24="est" number (VOID). Reuse without disclosure is a traceability
violation, not a leg. The 24-inversion (empty under era, Les Mis, AND the
union model — F27) is a legitimate finding but NOT a leg for 87=ce.
64-77-84 trigram is n_eff=1 (N27) — no triple-counting the byte-identical
phrase. 67: 30/38 unclassified; et/veut fork (114:1 era) unpromoted;
"la veut" @1044–1045 is the pin-lead for 67="veut" (provisional);
the 67→11/11→67 chiasmus (@753/@1044 adjacent to the cribs) is armed with
full distributions. 43="me" is pressured by «par 43» ×2 @[342, 1026] (era
"par me" n=0 — F42): the claim must answer it, not ignore it.

### 7. Inventorist — re-drive the pattern matcher on the crib-learned unit
alphabet (F44); apply POLYVALENCE_REPORT §8 (fix inventory first, then R1–R8)
R1–R8 (N33, red-team-amended) govern: smart expansion only (naive whole-
closure expansion 202×–2318× is an instrument-killer); expanded index
unconditional (R1 strengthened); R7 fenced non-implementable. Inventory must
be crib-learned (F44: 24 units, Tier 0–3) — the upstream 180-unit inventory
is NOT the encipherer's table (ruled out, F44). ECHO WARNING (N32): an
"inventory" that re-derives the pencil cribs plus provisional anchors is a
re-statement; proposals must beat their provisional-anchor echo (the
"quiconque" ×7 caution). Traceability: the tester's §6 K≥3 synthetic
numbers did NOT reproduce — regenerate, never cite.

## Ruling ledger

| # | Claim | Ruling | Decisive reason |
|---|---|---|---|
| | *(no claim packages have landed in `code/crowd6/` as of this writing — all seven dockets open)* | | |

- Promotions: 0 · Demotions: 0 · Kills: 0 · Fenced leads: 0

## Methodology flags banked (F26-N+)

- **F26-14:** the F42 chiasmus is stated on the ADJACENT instances —
  67→11 @753 immediately before the @754 crib; 11→67 @1044 immediately after
  the @1034 crib. The full 67→11 distribution is @[561, 669, 753, 996]:
  @996 is post-@754, pre-@1034 — not "before the crib" in general. Any
  chiasmus leg must scope which instances it claims; a count of 4 ≠ a claim
  of 2 adjacent pairs.
- **F26-15:** 62 follower/predecessor profiles armed as literal dicts, both
  summing to 35=n62 (complete accounting — no truncation). Predecessor sum
  =35 confirms no 62 leads the stream; follower sum =35 confirms no 62
  closes it. Any on-vs-il profile battery re-uses these cells — the N35
  independence accounting (no recycled cells, exact tests, no ear-premise
  leakage) applies per use, not just per claim.
