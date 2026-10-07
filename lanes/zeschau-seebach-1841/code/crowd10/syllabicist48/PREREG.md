# PRE-REGISTER — 48 syllable-cell battery (round-10, syllabicist48)

Written 2026-10-07T20:38:55Z (15:38 CDT), BEFORE any fresh 48-window inspection
by this executor. This executor has read the lane record (NOTES.md N1–N50,
F1–F68, STATE.md round-10 work orders, code/crowd9/successor48/) — the 48
census (F60/F64) is standing lane data, not a leg. All legs below ask FRESH
questions of that census.

## Standing inputs (lane record, frozen — not scored legs)
- n48=38; P48 = 38/1847 = 0.02057 (F64; curator re-derived).
- Predecessors (F64 census): 62×6, 12×5, 82×4 (m GT), 32×4, 89×3, 78×2,
  24×2 (en STRONG lead), 11×1 (la GT), 96×1, 98×1, 86×1, 74×1, 76×1, 85×1,
  65×1, 71×1, 19×1, 42×1, 29×1. Note: 46=que → 48 = 0.
- Successors (F64 census): 29 distinct / 38; top 2s: 21, 52 (pas STRONG),
  76, 20, 47 (ce-frag LEAD), 77 (le prov-cond), 96, 29 (er GT), 56; singles
  incl 11 (la GT), 40 (e GT), 59 (est prov), 6, 0, 30, 31, 74, 88, 98, 82,
  84, 24, 42, 49, 51, 53, 71, 1, 79. Note: 48 → 46 (que) = 0; 48 → 29 (er)
  = 2; 48 → 40 (e) = 1.
- 48 ↔ 94 = 0 (N49). "on 48" ×6 association real (E=0.72, p=7.6e-05) but no
  verbal signature; "48 pas" ×2 statistically null alone (E=0.555, p=0.106) (F64).
- Windows (0-based, F64 census @): 126, 170, 283, 361, 365, 377, 398, 426,
  450, 542, 641, 710, 729, 810, 856, 863, 872, 928, 972, 987, 1076, 1177,
  1212, 1221, 1229, 1276, 1279, 1316, 1350, 1398, 1465, 1525, 1570, 1589,
  1614, 1658, 1737, 1779.
- KILLED / off-limits (never re-litigated): 48="ne" (F60), H_verb for 48
  (F64, K2 fired), 86=que-family (F65), unconditioned 84s, the three mergers,
  refuge concretizations, retired WO-6 bar.
- Banked values (frozen for licensing checks): GT {11=la, 70=pre, 82=m,
  34=i, 29=er, 40=e, 46=que}; provisional {87=ce, 64=qui, 96=par, 59=est};
  77="le" provisional-conditioned; 62="on" fenced STRONG LEAD; 52="pas"
  STRONG; 94="ne" provisional-strong; 24="en" STRONG lead; 78="me"-syllable
  LEAD; 00="pour" STRONG lead; 00="le" LEAD; 47="ce" LEAD; 96=verb-stem LEAD
  n_eff=1; 93/8="l'" LEAD.

## Claim under test
48 is a FREQUENT SYLLABLE CELL — not a conjugated verb (H_verb killed),
not "ne". Two classes:
- **S-word**: 48 = a whole word (adverb / preposition / conjunction /
  pronoun / particle class).
- **S-syl**: 48 = a syllable cell — a spoken syllable, word-internal or
  boundary-crossing, per the lane's mixed table (F44 R4).

## H_stem placement — TESTED SEPARATELY
H_stem (48 as a 96-family verb stem) is a contact-profile identity claim,
best served by its own cosine/signature battery. It is NOT folded into the
syllable legs: the 48–96 contact datums are consumed by S6 only, never by
S1–S5. (Decision: separate — cleaner instrument, no double-counting.)

## Candidate shortlist — pre-registered SELECTION RULE
1. Build by-ear syllable unigram rates from Nesselrode v8 with a DOCUMENTED
   fixed tokenizer (lowercase, elision-split per
   `code/crowd7/closer/diplomatic_rates.tokenize`, then word → syllables by a
   fixed maximal-onset/CV rule; mute -e kept written per F44-R3; final -er
   NOT pre-split — recorded approximation, flagged F30/F22).
2. Take top-40 by-ear syllables by rate.
3. EXCLUDE unconditionally: GT {la, pre, m, i, er, e, que}; provisional
   {ce, qui, par, ne, est}; banked {on (62), le (77-conditioned), me
   (78-syllable), pour (00), en (24), pas (52), ent (06-restricted),
   l' (93/8), ce-frag (47), même (64-disfavored)}; killed 48 readings
   {ne, verb-form class}.
4. Of the remainder, battery the top-10 by rate-band proximity
   (|log(rate_S / 0.02057)|), min 6, max 12.
5. Word-class (S-word) candidates: top-3 corpus word unigrams by the same
   proximity rule (same exclusions) PLUS hand-seeded a-priori candidates
   (marked SEEDED): {de, à, se, les, des, plus, tout, bien, sur, sans, dans,
   encore, aussi, leur, son, mais, car, donc, ni, y, point}. Seededs are
   battery members, not favorites — the legs decide.
6. PREREG v1.1 (2026-10-07T20:38:55Z+2m, before any run): noun seeds added
   to the S-word class — {lettre, dépêche, gouvernement, majesté, affaire,
   cour, ministre} (a frequent-noun whole-word cell is a legitimate S-word
   subclass; the function-word seeds would miss it). Same legs apply.

## Legs (per candidate S; class determines which apply)

### S1 — rate band (context leg; kill only at >5×)
- S-word: 0.02057 vs era WORD rate of S in Nesselrode v8.
- S-syl: 0.02057 vs era by-ear SYLLABLE rate of S.
- PASS: ratio r in [1/3, 3]. ADVERSE-KILL: r > 5 or r < 1/10.
  Else NULL (context only).
- Pre-stated limitation: F30 (rigid syllabification dead as an instrument)
  and F20 (factor band uncalibrated) apply — S1 NEVER promotes alone.

### S2 — "la 48" frame @1525 (GT predecessor; FRESH question, never asked)
- S-word: S must be grammatical directly after "la" (article). Era bigram
  check in v8: PASS iff n("la", S) >= 1; ADVERSE-KILL iff n("la", S) = 0
  in 86,636 tokens (grammatical zero — e.g. "la de").
- S-syl: neutral (any "la X…" word admits S as a non-initial syllable);
  recorded, not scored.

### S3 — "on 48" ×6 frames (FRESH question — F64's V4 asked the successor
  side; this asks the pre-side and the frame grammar)
Windows: @361 (suc 76), @426 (suc 76), @1316 (suc 98), @1350 (suc 77="le"),
@1465 (suc 21), @1570 (suc 56).
- S-word: all six "on S" frames must be grammatical. PASS iff era
  n("on", S) >= 1 AND no frame is a grammatical zero; ADVERSE-KILL iff any
  frame is era-zero in v8.
- S-syl: successor-continuation check. For each window, the successor cell
  must be a plausible continuation of a word beginning with S under "on":
  @1350 (suc 77="le") → PASS iff era attests >= 1 word ending in S
  followed by "le"; else recorded adverse (NOT kill — successors 76/98/21/56
  are unidentified; single-datum checks stay fenced).
- S-word also: "que 48" = 0/38 — for S-word, "que S" must be attested
  (PASS iff n("que",S) >= 1; kill iff zero). S-syl: neutral.

### S4 — "48 pas" ×2 frames @283, @1737 (FRESH question for S-word;
  F60's H3 pas-datum is not reused as a leg)
- S-word: "S pas" must be grammatical: PASS iff era n(S, "pas") >= 1;
  ADVERSE-KILL iff zero.
- S-syl: neutral (word boundary before "pas").

### S5 — successor-profile class signature (DIAGNOSTIC ONLY — T7)
Record: 48→{29(er),40(e)} = 3/38; 48→ word-boundary-anchored cells
{11=la ×1, 77=le ×2, 46=que ×0}; 48→ unidentified {96, 47, 56, 21, 20, 76,
98, …}. Compare qualitatively to candidate class (stems take
inflectional-suffix followers; words take word-initial followers). No bar,
never a verdict input.

### S6 — H_stem battery (SEPARATE instrument, same package)
- (a) predecessor cosine(48, 96) re-derived on the repaired stream; bar 0.60
  (homophonist's); floor = median cosine of 48 vs all n>=20 groups.
- (b) Fisher exact on shared top-follower cells (2×2 overlap table).
- (c) stem-signature: top-3 followers of 48 >= 40% of 38 (crowd9 prereg).
- Verdict: LEAD iff ((a) OR (b) passes) AND (c) passes, with no fresh
  adverses. Failure = NULL, explicitly never adverse (underpowered, n96=21
  — F64).
- The 48–96 contact datums are consumed HERE ONLY.

## Verdict rules (recommendation to red team ONLY)
- **LEAD (recommend):** >= 2 of S1–S4 PASS (S1 counts), zero kill-grade
  adverses, zero unfenced adverses, S5/S6 consistent.
- **LEAD-weak:** exactly 1 of S1–S4 PASS, rest NULL, zero kills.
- **HONEST NULL:** everything else.
- 48 stays UNIDENTIFIED unless the bar is met. No status-line language
  outside the recommendation field.

## Guards
- F64's legs (V1–V4) are not reused as positive legs. The motivating datums
  ("on 48"×6, "48 pas"×2) are re-examined under FRESH questions only.
- No double-counting: the same window is never a leg twice for the same
  question (pre-side vs suc-side differ).
- T7: no manual-tiling bearing counts scored; S5 diagnostic only.
- F30: no era-syllable-conditional legs on morphological fragments; S1-syl
  uses whole-syllable by-ear unigrams with the limitation flagged; fragments
  (er/m/i/e — N22) never enter rate legs.
- All @-citations 0-based pair indices (REINDEX.md).
- Recommendation package only — red team adjudicates every status change.

## v1.2 (2026-10-07T20:44Z, instrument repair — before any S-syl result is interpreted)
The v1.0 by-ear rule split VV sequences ("puis"→"pu|is", "que"→"qu|e"),
and the resulting fragments ("qu","is","it","ur","us","u") dominated the
S-syl shortlist — non-syllables, instrument artifact. Repaired rule:
consecutive vowels form a SINGLE nucleus (no VV split), consistent with the
lane's by-ear premise ("qu'on"=/kɔ̃/ one spoken syllable, F44). Everything
else unchanged. The v1.0 S-word battery is unaffected (word-space legs only)
and stands as run.
