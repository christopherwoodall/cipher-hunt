# PREREG — carry-rest (round 13, council work order 7 second half)

Carry-forward executor for Seebach round 13. **Written 2026-10-07 ~18:10 CDT —
BEFORE any new data query by this worker.** Round-12 partials read (not re-run):
`code/crowd12/followup48/{PREREG.md,followup48_results.json}`,
`code/crowd12/rerun1248/{PREREG.md,rerun1248_results.json}`,
`code/crowd12/estetie/{PREREG-T1T5.md,estetie_results.json,estetie_era_followup.json}`.
Positions 0-based on the repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`,
`code/crowd7/keystruct/aliasing.load_stream()`, N=1847 asserted at runtime).

## Standing inputs (frozen, not scored legs)
- GT {11=la,70=pre,82=m,34=i,29=er,40=e,46=que}; provisional {87=ce,64=qui,96=par,59=est},
  77="le" provisional-CONDITIONED; 62="on" FENCED STRONG LEAD; 52="pas" STRONG;
  94="ne" provisional-strong; 33=infinitive-class; 78 polyvalent.
- ISLET 10: 59=verb-final «-este» iff pre(59)=84 — firm @1190/@1448/@1804, fenced @1291.
  H0: -este verb set-valued {manifeste, atteste, proteste, conteste, déteste}.
- ISLET 3: 06="ent" iff pre(82). @471: pre(06)=80 ⇒ ISLET-3 does NOT cover @471.
- 48 fences stand: Path A, Path B, Path D fenced (F83); @1350 OUT; @126 OUT;
  @863/@1658 "de ce"-frames are follow-up pointers, not legs.
- 48="de"-unconditioned KILLED (kill-grade, french-blitz 11 windows) — NOT re-litigated.
  48="ne" KILLED (N49), H_verb for 48 KILLED (N50/K2) — NOT re-litigated.
  H_stem (48 = verb-STEM syllable cell) is a DIFFERENT hypothesis — in scope per WO.
- @1248 NEITHER-fence STANDS. Round-12 PC-1 PASS (craindre-peu-que, new lemma) and
  DP-1 FAIL (~22MB double-pour zero) are recommendations awaiting red-team ruling.
- Corpus: clean-diplo pool (guizot t1/t2/t3/t5-t6, metternich v4/v6, pozzo-di-borgo v1,
  levant-correspondence-1841-p3, talleyrand v1, rdm-1841 q1–q4). v8 phrase counts VOID (F77).
  Tokenizer: round-11 este_verb.py's (NFC, lower, '-normalized, elision kept on stem).
  No manual-tiling bearing counts. All counts from scripts.

## A — 74-class battery (does 74 license "de ce que"? promotes/kills the @863 islet)
Frame: @862=74, @863=48, @864=47, @865=46. followup48 863-a: v8 "de ce que" n=10,
L1 ∈ {piqué, heureux, courant, quart, contente, compte, contraire, opposé, fâchés, paris→satisfait}.
- **Leg A1 (era):** classify the 10 L1s into {adjective, noun, participle, verb-phrase}
  [FR-JUDGMENT]; also classify clean-diplo "de ce que" L1s (exhaustive, same classes).
  Bar: PROMOTE-side iff ONE class covers ≥70% of pooled genuine L1s → 74 must be that
  class. KILL-side iff "de ce que" is unlicensed after every class (expect: not met —
  report honestly). Split shares → CLASS-AMBIGUOUS (no kill, no promote).
- **Leg A2 (cipher):** 74's full contact profile (n=34; pre/suc ±1, ±2 windows) against
  class-discriminating predictions on banked/provisional values:
  (i) verb-hypothesis: 74→77 ("le") ×2 = verb + postposed object pronoun → ungrammatical
  in French ⇒ verb class ADVERSE; (ii) participle-hypothesis: check auxiliary adjacency
  (pre(74) ∈ auxiliary set {52? no — "pas"; use provisional 59="est"} — report, no bar);
  (iii) adjective/noun: report article/determiner adjacency (pre ∈ {11,87}).
  Bar: A2 KILLS the islet iff 74's profile contradicts EVERY licensor class on ≥1
  banked/provisional datum. A2 PROMOTES iff 74 fits exactly ONE class on ≥2 independent
  data AND that class licenses "de ce que" per A1. Else OPEN.
- Verdict rule: islet PROMOTED-to-word-lead iff A1 dominant-class AND A2 single-class-fit
  agree; KILLED iff A2 kills; else the conditioned-syllable LEAD (followup48 863-c)
  stands as recommended.

## B — H_stem battery (48-er×2 / 48-e×1: verb stem + inflection as 48's natural habitat)
Cipher datum (followup48 accounting): 48→29 ("er" GT) at @1229 (pre=82="m") and @1589
(pre=65); 48→40 ("e" GT) at @1398 (pre=78). H_stem: 48 is a vowel-initial verb-stem cell.
- **Leg B1 (cipher):** gloss all 3 windows ±3 with banked values; compatibility checks:
  @1229 "m 48-er": 82="m" elides only before vowel ⇒ stem must be vowel-initial
  (consistent with round-12 "48 vowel-initial lead", 82-precedes-48 ×4); grammaticality
  of "m'[stem]er" (object pronoun + infinitive) per era. @1589, @1398: pre-context
  verb-licensing (auxiliary/modal adjacency) reported.
  Bar: B1 PASS iff all 3 windows compatible with stem-reading on banked values
  (no contradiction); FAIL (kill-grade datum) iff any window contradicts on a GT value.
- **Leg B2 (era):** by-ear v1.2 syllabification (verbatim round-10 rule) of clean-diplo
  -er infinitives: share whose parse is exactly [stem-cell]["er"] (second cell bare "er").
  Bar: LICENSES the two-cell "48-er" split iff share ≥5% (non-trivial); ~0% ⇒ H_stem's
  cell-split unlicensed (kill-grade datum). Report exact share + n.
- Verdict rule: H_stem GAINS a leg iff B1 PASS AND B2 licenses; H_stem KILLED iff
  B1 contradiction on GT OR B2 ~0; else OPEN. (Does NOT promote 48=anything — leg only.)

## C — second "48-47-46" hunt
- **Leg C1 (cipher, byte-exact):** census 48-47-46 trigrams over the repaired stream
  (expect @863 only; verify @1658 = 48-47-98, not 48-47-46); near-miss census
  48-47-X (X≠46) and 48-X-46. For each hit: ±4 window glossed.
  Bar: PROMOTE the islet (second token) iff a second 48-47-46 exists with licensable
  left context; KILL iff a second token exists with anti-"de ce que" context under
  banked values; else CLEAN NEGATIVE (only @863).
- C1 is confirmatory: followup48 863-c already recommends the conditioned-syllable
  LEAD on n≥2 genuine "de ce que"; a clean negative here changes nothing by itself.

## D — @1248 verdict consolidation
- **Leg D1 (independent re-check, mine):** re-run strict DP patterns
  ("pour W1 W2 pour peu que" / "pour W1 W2 pour INF que", lane is_inf) on RDM-1841-q1
  + Guizot-DIP fresh in this worker (independent of round-12's scan); constituency-read
  any hit. Bar: CONFIRMS-FENCE iff 0 genuine; RE-OPENS iff ≥1 genuine.
- Verdict rule: recommend GRANT of PC-1 (peu 4/8→5/9, craindre-peu-que attestation
  leg, OCR-running-head caveat recorded) iff round-12's PC-1 adjudication re-verifies
  on the raw JSON (spot-check the craindre context); recommend DP-1 PERMANENT FENCE
  (both arms, frame-unattested in ~22MB) iff D1 confirms zero. @1248 NEITHER-fence
  stands regardless (WO6 single-work-order bar).

## E — -este tie-breakers (adjudicate estetie T1–T5 + Frenchman transitivity battery)
- **Leg E-trans (era + Frenchman, mine):** for each of {manifeste, atteste, proteste,
  conteste, déteste} + reste: clean-diplo counts of ("le", V3sg), ("qui","le",V3sg),
  (V3sg, "que"); Frenchman transitivity judgment [FR-JUDGMENT]: which verbs govern a
  direct object «le» in diplomatic register. Bar: TRANSITIVITY-LICENSED iff
  n("le",V3sg)≥1 genuine; reste EXCLUDED iff intransitive (Frenchman kill-grade if
  "reste" is in the candidate space).
- T1–T5 adjudication (recommendations only, from estetie partial):
  T1: no tie-break (conter≠contester lexeme; "qui le conter" 0/3.6M) → NULL.
  T2: antecedent inconclusive → NULL.
  T3: 06="pro" COMPATIBLE-UNCONFIRMED ("proteste que" 2/3.6M; @346 weak witness with
  mute-e caveat) → stays LEAD-WEAK, no promote.
  T4: @1291 stays FENCED (bar was ≥2 legs each for 17/35 — not met) → NULL.
  T5: second «qui le [84-59]» CLEAN NEGATIVE (exactly 2×) → NULL (as expected).
- Verdict rule: a verb is TIE-BROKEN only on ≥2 independent legs; E-trans alone is
  one leg (transitivity), combinable with T3's "pro" lead.

## Outputs
- `code/crowd13/carry-rest/{PREREG.md,a74.py,hstem.py,frame2.py,dp_verify.py,frenchman_este.py,carry_results.json}`
- Report-inbox notes at lane `report_inbox/carry13-<topic>.md` per REPORTING.md.
- Final report to coordinator: per-item verdicts or honest nulls; recommendations only.
