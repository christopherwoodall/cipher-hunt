# PREREG — 48 successor-word anchoring (round-11, anchorer48, work order 2)

Written 2026-10-07 (before any fresh era-count computation by this executor).
This executor has read the lane record (NOTES.md through N51/F76, STATE.md
round-11 work orders, round-10 syllabicist48 PREREG + battery JSON, round-10
frenchman era_gates10.py + JSON + report note). The 48 census (windows,
predecessors, successors) is standing lane data (F64/frenchman Q3_48),
re-derived below byte-level — not a leg. All legs ask FRESH questions.

## Standing inputs (frozen — not scored legs)
- Stream: repaired 1,847-pair parse via `code/crowd7/keystruct/aliasing.load_stream()`; 0-based indices.
- n48=38; P48=0.02057.
- Six 62→48 ("on 48"): @361(suc 76), @426(suc 76), @1316(suc 98), @1350(suc 77),
  @1465(suc 21), @1570(suc 56). Successor multiset: {76×2, 98, 77, 21, 56}.
- Four 82→48 ("m" 48): @126(suc 11), @377(suc 0), @398(suc 6), @1229(suc 29).
  Successor multiset: {11, 0, 6, 29}.
- Three 48→pronoun-cell: @126(48→11=la GT, suc2=@127=grp 2), @1076(48→77=le,
  pre=12, suc2=@1077=grp 78), @1350(48→77=le, pre=62, suc2=@1351=grp 78).
- Two 48→52 ("48 pas"): @283, @1737.
- 46=que → 48 = 0/38. 48 → 46 = 0/38.
- Banked values: GT {11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que};
  provisional {87=ce, 64=qui, 96=par, 59=est}; 77="le" provisional-CONDITIONED
  (F37); 62="on" FENCED STRONG LEAD (N39); 52="pas" STRONG; 94="ne"
  provisional-strong; 78 unidentified ("me"-syllable LEAD / ver-er fork / R-c nominal).
- Candidate datum (zero discrimination from membership — F75): the 10 S-syl
  rate-band shortlist {à, et, de, a, es, il, les, te, un, com}.
- KILLED / off-limits (never re-litigated): 48="ne"-allophone (N49),
  H_verb for 48 (N50/K2), 86=que-family (N50), unconditioned 84s, the three
  mergers (N45/F56), refuge concretizations, retired WO-6 bar.
- R-c OWNS @1351–1356 («le [78] ne ment pas», N51) — settled, not re-litigated.
  Consequence pre-registered: 78 is R-c-nominal there ⟂ 78=infinitive.
- Gate-5 banked (frenchman round-9; round-10 red-team: "conditional on
  48=transitive-verb; 48 UNIDENTIFIED → banked as future-48 constraint"):
  (i) missing-"ne" veto — fires only for 48=verb/verb-stem (F76 V1 generalized
  to all uniform word-readings; escape via conditioning, not via verbhood);
  (ii) clitic-order veto — (48=transitive-verb ∧ 77="le"-pronoun) impossible
  at @1350. This executor advances NO verb reading for 48; both vetoes are
  checked as non-firing, clitic veto stays banked.
- F76: 48="de" CONDITIONAL is the only live word-reading — narrow
  pronoun+infinitive path («de le [inf]»; frenchman: 29 «de le» all
  pronoun+infinitive «de le voir/faire/mettre», 0 article; 15 «à le» likewise;
  «de» survives ONLY via 77="le"-pronoun ∧ infinitive). 48="com" NEUTRAL
  (fragment, no frame testable). {en,nous,vous} die V1 as uniform words.
- Corpus: Nesselrode v8 strict (92,594 tokens), elision-split tokenizer
  (`code/crowd9/frenchman/corpus9.tokenize_elision`). ALL era bars on v8.
  By-ear syllabifier: round-10 v1.2 rule verbatim (consecutive vowels = single
  nucleus; cut after first consonant following nucleus end; mute -e kept;
  tokens ≤3 chars containing "'" stay whole, e.g. "m'").
- Guards: no manual-tiling bearing counts (T7) — cipher-side stays byte-level
  windows; corpus-side counts are programmatic ngrams, never hand-tiled
  cipher words. No double-counting: a window is never a leg twice for the
  same question. French claims get v8 counts or a [NEEDS-FRENCHMAN] flag —
  no bare grammaticality assertions.

## PATH A — six "on 48" windows: successor census + single-syllable coherence
A0 (datum): successor census {76×2 (@361,@426 — byte-identical "on 48 76" ×2),
  98 (@1316), 77=le prov-cond (@1350), 21 (@1465), 56 (@1570)}. No bar.
A1 (fresh vs round-10 S3 which lacked the "on"): @1350-anchored coherence.
  For each S in shortlist: v8 trigram count ("on", W, "le") with by-ear
  first_syl(W)==S. (62="on"-word ⇒ 48 starts a new word ⇒ S word-initial;
  S-final parse impossible under the premise — not counted.)
  Bar: PASS iff ≥1; ADVERSE iff 0. FENCED (single window; 77="le" prov-cond;
  62="on" fenced LEAD) — never kill-grade.
A2 ("on"+S productivity): for each S: v8 bigram count ("on", W) with
  first_syl(W)==S. Bar: PASS iff ≥1; ADVERSE iff 0. FENCED (62="on" fenced).
A3 (single-S verdict): S COHERES with the "on"-frames iff A1∧A2 PASS.
  Reading-level: COHERENT iff ≥1 S coheres (report the set; ≥2 = no unique ID);
  FENCED iff 0 cohere (premises provisional/fenced — never a kill of 48).

## PATH B — four 82→48 frames under the mandated "m'"-elision premise
Premise (work-order-mandated leg, conditional): 82="m'" (elided "me") ⇒ 48
  is vowel-initial. Vowel-initial shortlist S: {à, a, es, et, il, un}.
  Consonant-initial {de, les, te, com}: INCOHERENT with the premise (recorded;
  does not kill them as 48-values — fences the premise for those S's only).
B1 (@126-anchored): v8 trigram ("m'", W, "la") with first_syl(W)==S.
  Bar: PASS iff ≥1; ADVERSE iff 0. FENCED (single window; premise conditional).
B2 (@1229-anchored): "m' S er" — two parses, either counts:
  (i) ("m'", W1, W2) with first_syl(W1)==S and first_syl(W2)=="er";
  (ii) ("m'", W) with first_syl(W)==S and by-ear second_syl(W)=="er".
  Bar: PASS iff (i)≥1 or (ii)≥1; ADVERSE iff both 0. FENCED.
B3: @377 (suc 0), @398 (suc 6) — successors unidentified: recorded, no bar.
B4 (verdict): S COHERES with the "m'"-frames iff B1∧B2 PASS. If 0 vowel-initial
  S cohere ⇒ the "m'"-premise is FENCED for 48 (banked; 82 may be
  word-final/initial "m"). Conditional verdict only — no promotion off
  single-window legs.

## PATH D — 48="de"-CONDITIONAL narrow path (pronoun+infinitive): RUN or FENCE
D0 (footprint datum): claiming windows @126 (48→11=la), @1076 (48→77=le),
  @1350 (48→77=le). suc2: @127=grp 2, @1077=grp 78, @1351=grp 78.
D1 (era construction — context leg, re-derived not cited): v8 "de le"+X and
  "de la"+X trigram X-lists, each X classified INF (infinitive-capable) /
  NOUN / OTHER by pre-registered rule: INF iff X ends in (er|ir|re|oir) and
  X ∉ NOUN-STOP (fixed list in code; hand-verify ambiguous remainder, full
  per-X list disclosed in JSON, hand-verdicts marked [FR-JUDGMENT]).
  Bar: LICENSED iff ("de le"+INF)/("de le") ≥ 0.90 AND "de la"+INF ≥ 1.
  Context only — licenses the construction, never promotes. If bar fails ⇒
  narrow path REFUTED (kill the conditional).
D2 (window fit — discriminating):
  D2a (@1350): PRE-REGISTERED EXCLUSION — R-c owns @1351–1356 (N51, settled);
    78=R-c-nominal ⟂ 78=infinitive (frenchman's narrow-path requirement).
    ⇒ @1350 ∉ narrow path. Corroborating (not load-bearing): "on de"=2/v8 —
    classify the 2 hits from ±8 context as GENUINE (standalone subject "on")
    or INVERSION/other [FR-JUDGMENT]; @1350's "on de" needs ≥1 genuine.
  D2b (@1076): "…[12] de le [@1077=inf?]". Fit needs @1077 infinitive-compatible
    AND pre=12 licensing "[verb] de le [inf]". Both cells unidentified ⇒
    if not contradicted: IN-PENDING with missing legs ML-1 (@1077 ID),
    ML-2 (pre=12 ID).
  D2c (@126): "[82=m] de la [@127=inf?]". Era check: v8 [word ending in "m"] +
    "de la" + INF count. Bar: @126 IN iff ≥1 AND @127 not anti-infinitive
    (@127=grp 2, unidentified ⇒ cannot check ⇒ IN-PENDING with ML-3 (@127 ID)
    if era licenses, else OUT).
D3 (Gate-5 sweep): record — 48="de" is not a verb ⇒ missing-"ne" veto does not
  fire; 48="de" is not a transitive verb ⇒ clitic-order veto stays banked
  (no trip). V1 ("48 pas" @283/@1737): the conditional does not claim those
  windows — escape is via conditioning (recorded, not via (a)/(b)/(c)).
D4 (promotion audit): the narrow path RUNS (recommend LEAD) iff D1 LICENSED
  AND ≥1 claiming window FITS with ≥2 INDEPENDENT checks. Available: (1) era
  construction (D1); (2) suc2=infinitive cipher-side ID — currently missing
  for every window. Expected outcome: FENCED with explicit missing legs
  [ML-1, ML-2, ML-3] unless D2 yields a surprise fit or D1 fails (refute).
  Out-of-scope note (not a leg): 48→47 ("de ce") ×2 (@863, @1658) — different
  construction ("de ce que"/"de ce + noun"), not pronoun+infinitive; recorded only.

## Verdict rules
- Per-path verdicts with numbers; no status-line language beyond recommendation.
- Promotion needs ≥2 independent checks (STATE.md standing rule) — red team
  adjudicates every status change; this package is a recommendation only.
- Fences name explicit missing legs. Nulls recorded honestly.
