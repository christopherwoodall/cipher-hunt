# PRE-REGISTER — 48=verb/verb-stem battery (round-9, 48-successor)

Written 2026-10-07 BEFORE any 48-window stream access by this executor.
All cipher-side numbers below are derived fresh afterward against the
repaired 1,847-pair parse (`code/crowd7/keystruct/aliasing.load_stream()`).
Era comparator: Nesselrode v8 (`code/side-period/corpus/nesselrode-v8.txt`),
tokenized with `code/crowd7/closer/diplomatic_rates.tokenize`.

## Claim under test
F60 residual (round-8 homophonist battery, 48="ne"-allophone KILLED):
48 as VERB/verb-stem. Two sub-hypotheses:
- **H_verb**: 48 is a conjugated verb FORM (single lexical cell, word-level),
  e.g. the "dit"/"fait"/"peut" class.
- **H_stem**: 48 is a verb STEM cell (syllabic, cf. 96=verb-stem LEAD n_eff=1).

## Motivating datums (NOT scored legs)
"on 48" ×6 (62→48=6, adjudicator re-derived; 62="on" fenced STRONG LEAD),
"48 pas" ×2 (48→52=2; 52="pas" STRONG, rival 52="se" LEAD noted),
flat followers (19 distinct/38, "syllable-like"). These motivated the
hypothesis. The battery's legs must ask FRESH questions of these windows —
re-counting them is circular and is barred.

## Independence (from the F60 kill — binding)
The F60 kill legs are NOT positive legs here:
- H2 (merged (94+48) unigram 4.78× vs "ne") — not reused.
- H5 ("ne ce que" @863 / "en ne ce" @1657–1660) — not reused.
- H6 (predecessor era-fit −0.585 nats vs "ne") — not reused.
The lane-standard >3× rate-kill bar (B1 precedent) is reused as a BAR with a
FRESH comparator (verb forms), not the "ne" datum. The H3 "pas"-frame datum
(48→52 ×2 compatible with 94's rate) is not a leg; V2 asks a different
question of the same windows (ne-LICENSING, not rate-compatibility).

## Banked values used (frozen for this battery)
- GT: 11="la", 70="pre", 82="m", 34="i", 29="er", 40="e", 46="que".
- 62="on" fenced STRONG LEAD (R7c, +2 non-ear legs).
- 52="pas" STRONG, bounded (F31; rival 52="se" stays LEAD; K5 polyvalence).
- 94="ne" provisional-strong. 24="en" STRONG lead. 64="qui" provisional.
  87="ce" provisional. 59="est" provisional. 01="est" MEDIUM.
- 96=verb-stem LEAD n_eff=1 (single 64-96-47 window @149–151, 0-based).
- 93/8="l'" LEAD (homophone set).

## Legs (promotion needs ≥2 of V1–V4)

**V1 — verb-form rate band (fresh comparator).**
n48 expected 38 → 38/1847 = 0.02057. Comparator: top-20 most frequent
unambiguous VERB FORMS in Nesselrode v8 (word-level; classifier: standard
French lexicon; full top-40 table with classifications dumped to results
JSON for audit). Register caveat recorded: word-rate ≈ pair-rate only for
word-sized groups; a syllabic 48 breaks the comparator (favors H_stem).
- PASS: 0.02057 ∈ [0.5×min20, 2×max20] (in-band with frequent verb forms).
- ADVERSE (kill-grade): >3× max20 (lane-standard kill bar, B1 precedent).
- Else NULL.

**V2 — "48 pas" ne-licensing (fresh question).**
Under H_verb, adjacent "VERB pas" is licensed ONLY as "ne VERBE pas"
(era French; infinitival "ne pas V" does not apply — 48 precedes pas).
For each of the 2 "48→52" windows: scan pair positions i−4..i−1 for
94="ne" (provisional-strong). A window LICENSES iff a 94 occurs in that
span AND no GT word-break cell (11="la"; 93/8="l'") intervenes between
the 94 and the 48.
- PASS: ≥1/2 windows licensed.
- ADVERSE: 0/2 licensed. Diagnostic (recorded, NOT scored): test the
  52="se" rival reading of the 2 windows ("48 se" = VERB+se reflexive? —
  "se" follows the verb only infinitivally/postposed; record fit only).

**V3 — predecessor verb-licensing profile (fresh).**
All 38 predecessors classified under banked values (frozen sets):
- LICENSING: {62="on" (subject pronoun), 94="ne" (negation),
  64="qui" (relative pronoun), 46="que" (subordinator), 24="en"
  (adverbial pronoun), 82="m" (GT syllable; m'-elision before verb —
  syllable caveat flagged, counted but footnoted)}.
- HARD-INCOMPATIBLE: {11="la" (GT article — cannot directly precede a
  finite verb)}.
- All other predecessors: UNCLASSIFIED (recorded, not scored).
- PASS: ≥60% (≥23/38) in LICENSING.
- ADVERSE: ≥3 in HARD-INCOMPATIBLE.
- Else NULL.

**V4 — "on 48" successor verb-compatibility (fresh question).**
The 6 "on 48" windows: each successor must be post-verb-compatible.
Frozen HARD-INCOMPATIBLE successor set: {62="on", 64="qui", 94="ne"}
(none can directly follow a finite verb in era French). All other
successors recorded with banked values but not pre-scored (syllabic
system — a stem reading rescues odd successors; over-scoring here would
beg the H_verb/H_stem question).
- PASS (weak leg, recorded as such): 0/6 hard-incompatible.
- ADVERSE: ≥2/6 hard-incompatible.
- 1/6: NULL.

**V5 — 96 same-stem-family test (H_stem ONLY; exploratory).**
n96 derived from repaired stream. (a) predecessor cosine(48,96) vs the
0.60 bar (homophonist's bar); floor = median cosine vs all n≥20 groups.
(b) Fisher exact on shared top follower cells (2×2 overlap table).
- PASS (one H_stem leg): (a) AND (b) both pass.
- Else NULL — explicitly NOT adverse (n96 underpowers the test).
H_stem second leg (stem-signature): top-3 followers of 48 ≥40% of 38
(stems take a limited inflectional-suffix inventory) → PASS; else NULL.

**V6 — follower-concentration diagnostic (NOT scored, T7).**
HHI/top-5 share of 48's followers vs the same statistic for banked
verb-adjacent cells. Recorded only; never a promotion/demotion input
(T7: never score manual-tiling bearing counts; this stays diagnostic).

## Kill conditions (any one kills the corresponding hypothesis as LEAD)
- K1: V1 ADVERSE (>3× max top-20 verb-form rate) → H_verb dead as a
  single FORM (H_stem may survive as rescue).
- K2: V2 ADVERSE **and** V3 licensing <40% → no licensed verbal
  environment anywhere → H_verb dead.
- K3: any of the 8 frame windows ungrammatical under EVERY banked-value
  reading including the syllabic rescue → flagged for red team; I do not
  adjudicate, but an unflagged K3 is required for any promotion.
- K4: a GT/provisional-strong cell forces a NON-verb reading of 48 at ≥3
  of the 38 windows → H_verb dead (record the forcing windows).

## Verdict rules
- **LEAD recommendation (H_verb):** ≥2 of V1–V4 PASS, zero kill
  conditions, zero un-fenced adverses, K3 clean.
- **LEAD-weak:** exactly 1 of V1–V4 PASS, rest NULL, zero kills.
- **H_stem LEAD:** V5 PASS + stem-signature PASS + no K2/K3/K4
  (V1 may be ADVERSE — that is the stem rescue's predicted signature).
- **HONEST NULL:** everything else. Deliverable = full census (38 windows:
  index, pre, suc) + alternatives enumeration (below) + what red team
  must rule on.

## If null: alternatives enumeration (census-grounded, no batteries)
Adverb ("plus"/"bien"/"tout"/"aussi"/"encore" class — rate vs Nesselrode v8
top adverbs); preposition ("de"/"à"/"en"/"dans"/"pour"/"sur" — 38/1847 =
2.06% noted against preposition word-rates); pronoun; conjunction;
bare syllable cell (homophonist's "syllable-like followers" reading).
One paragraph each, census-grounded, no promotion claims. By-ear
readings flagged F34/F44.

## Guards
- No double-counting: motivating counts are not legs; V2/V4 ask new
  questions of old windows; H3's pas-datum is not a leg.
- F60 kill legs (H2/H5/H6) are not positive legs. The >3× bar is a
  lane-standard instrument with a fresh comparator.
- T7: no manual-tiling bearing counts scored. V6 diagnostic only.
- By-ear syllabification flagged F34/F44; never a gate.
- Recommendation PACKAGE only — red team adjudicates. No status-line
  language ("LEAD") except inside the recommendation field.
- All @-citations 0-based pair indices (REINDEX.md convention).
