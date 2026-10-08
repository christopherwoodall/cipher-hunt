# PREREG — followup48 (round-12, 48-followup executor, STATE.md WO5.5)

Written 2026-10-07 BEFORE any fresh era-count computation by this executor.
Executor has read: NOTES.md N52/F77–F83, STATE.md round-12 WOs,
`code/crowd11/anchorer48/PREREG.md` + `anchor48_results.json` (F83).
Positions are repaired 1,847-pair 0-based per `code/crowd4/REINDEX.md`.

## Standing inputs (frozen — not scored legs)
- Stream: `code/crowd7/keystruct/aliasing.load_stream()`; N=1847 asserted at runtime.
- Claim window: @1075=12, @1076=48, @1077=77, @1078=78, @1079=64, @1080=6 (byte-verified).
  **Prose-label discrepancy flagged:** F83/D4 prose says "ML-1: @1077 infinitive-ID"
  and "@1077 (grp 78 here)". Byte-exact: 77="le"-prov sits at @1077; the
  infinitive-slot cell 78 sits at @1078. This package works byte-exact
  (@1078 = infinitive candidate cell) and flags the prose off-by-one.
- Banked values: GT {11=la,70=pre,82=m,34=i,29=er,40=e,46=que};
  provisional {87=ce,64=qui,96=par,59=est}, 77="le" provisional-CONDITIONED (F37);
  62="on" FENCED STRONG LEAD (N39); 52="pas" STRONG; 94="ne" provisional-strong;
  33=infinitive-class (F79); 78 polyvalent (F33: me/ver coexistence; R-c owns
  @1351–1356 ⇒ 78=R-c-nominal there, N51 settled).
- F83 fences stand: Path A (A1 0/10 real zero), Path B, Path D fenced with
  missing legs ML-1 (@1078 infinitive-ID), ML-2 (pre=12 licensor-ID),
  ML-3 (@127, not in scope). @1350 OUT (R-c exclusion + "on de" 0/2 genuine).
  @126 OUT (left context unlicensed). @863/@1658 "de ce"-frames: follow-up
  pointer, out of the narrow path.
- Corpus: Nesselrode v8 strict (92,594 tokens), elision-split tokenizer
  (`code/crowd9/frenchman/corpus9.tokenize_elision`). All era bars on v8;
  levant-correspondence-1841-p3 as sensitivity note only. By-ear syllabifier
  v1.2 verbatim (round-10 rule: consecutive vowels = single nucleus; cut after
  first consonant following nucleus end; mute -e kept; tokens ≤3 chars with
  "'" stay whole).
- Case law: F77 — Nesselrode v8 OCR word-splits VOID as French (phrase counts
  fine); the clean diplomatic corpus corroborates. No manual-tiling bearing
  counts (T7). Cipher-side stays byte-level windows; corpus-side counts are
  programmatic ngrams. French claims get v8 counts or a [NEEDS-FRENCHMAN] flag.
- Never re-litigated: 48="ne"-allophone (N49), H_verb for 48 (N50/K2),
  86=que-family, unconditioned 84s, the three mergers, refuge concretizations,
  retired WO-6 bar, settled round-11 fences.

## ML-1 — identify the infinitive cell after "de le" (@1078=78)
Frame per F83: 48="de"-word, 77="le"-pronoun ⇒ @1078 must be an infinitive
(1 cell: faire/voir/croire-class; or first cell of a 2+-cell infinitive).
Two candidate readings: (a) 78 = monosyllabic infinitive, @1079=64 ("qui" prov)
starts the next word; (b) 78 = inf-initial cell, @1079=64 = inf-second cell.

- ML-1a (era context, "de [article] [INF]" rates — per WO wording): v8
  ("de","le")+X, ("de","la")+X, ("de","l'")+X, ("de","les")+X with X an
  infinitive (classification rule: X ends in (er|ir|re|oir) and X ∉ NOUN-STOP
  fixed list; hand-verify ambiguous remainder, [FR-JUDGMENT], full X-lists
  disclosed). For each: n, top-X, and share of X with by-ear cell-count == 1.
  Bar: CONTEXT ONLY — report rates; licenses reading (a) iff monosyllabic
  share is non-trivial (report, no threshold) AND "faire/voir/croire"-class
  is attested after "de le" specifically.
- ML-1b (era, reading (b) licensor): v8 infinitives (same classification rule)
  whose by-ear syllabification has second_syl == "qui". Bar: PASS-for-(b) iff
  ≥1 genuine token in v8 (note fragility if n=1); ADVERSE-for-(b) iff 0.
- ML-1c (era, reading (a) licensor): v8 ("de","le",W,"qui") with W a
  monosyllabic infinitive per ML-1a's attested list. Bar: PASS-for-(a) iff ≥1;
  ADVERSE-for-(a) iff 0. (Reads: "[12] de le [inf] qui [verb=6@1080]".)
- ML-1d (cipher): 78's profile against infinitive-cell readings. (i) 78→29
  ("er" GT): datum only, no bar (by-ear inf-second cells are rarely bare "er";
  0/31 expected-weak either way — reported, not scored). (ii) 78 after 47 ×5
  and the @364 window (47-78-48): reported as context, no bar. (iii) The
  seven 77→78 windows: classify each window's compatibility with 78=inf-cell
  vs 78="me"-syllable-LEAD (F38) — report, no bar (polyvalence already banked).
  Verdict rule: ML-1 IDENTIFIED only if (a) or (b) gets its era PASS AND no
  cipher-side contradiction in (d); else ML-1 stays OPEN with the surviving
  reading named.

## ML-2 — identify the pre=12 licensor's class (adj / noun / participle / verb)
F83/D2b framed the licensor as "verb/verb-final" only. This leg tests the full
era L1 class set of "de le"+INF.

- ML-2a (era): L1 of v8 ("de","le")+INF tokens (INF per ML-1a rule), hand-
  classified [FR-JUDGMENT] into {verb(-final), adjective, noun, participle,
  other}; full L1 list disclosed with counts. Bar: CONTEXT — report shares.
  The decisive output: whether adjective/noun/participle L1s are a substantial
  share (if yes, D2b's verb-only framing was too narrow — recorded as a
  prereg-scope correction, not a kill).
- ML-2b (era, L2 support for @1073–1074=98,98): for the adjective/noun/
  participle L1s from ML-2a, the L2 distribution (L2,L1,"de","le",INF);
  check whether article-like L2s (le/la/les/un/ce/cette) dominate. Bar:
  CONTEXT — report top L2s. (98 unidentified; this leg only constrains what
  98 would need to be under each class reading.)
- ML-2c (cipher): 12's class probes, byte-level: (i) 12 after 70 ("pré-"
  prefix GT) ×3 (@348,@1119,@1548) ⇒ 12 is word-initial stem cell — reported,
  compatible with all four classes; (ii) 12→48 ×5: the four non-@1075 windows
  (@169,@709,@809,@1736) — do any have era-licensed "[class] de" left frames?
  era check per window class-hypothesis, report; (iii) 12→33 @1642
  (33=infinitive-class, F79): "12 [inf]" — era: which classes take a bare
  infinitive complement (verbs: "veut faire"; adjectives/nouns/participles:
  report v8 counts of (adj|noun|part, INF) bigrams for the ML-2a L1 word set).
  Bar: ML-2 IDENTIFIED iff 12's cipher profile is compatible with ≥1 era-
  licensed class AND incompatible with the others on ≥1 independent cipher
  datum; else OPEN with the surviving class set. Honest null allowed: if 12
  is compatible with multiple classes, say so.

## @863 — second de-frame: re-open or pointer-only?
@862=74, @863=48, @864=47, @865=46. F83: 48-47-46 reads "de ce que" (10× v8).

- 863-a (era): re-derive ("de","ce","que") in v8 (expect 10; report exact);
  KWIC ±6 for all hits — classify each as "de ce que"+clause vs "de ce"+noun
  [FR-JUDGMENT]; report L1 distribution of the hits. Also v8 ("de","ce",NOUN)
  count for the @1658 window (48-47-98: "de ce"+X; X=98 unidentified).
- 863-b (cipher): @862=74 — 74's profile (n, pre/suc) reported; does any
  banked anchor touch @862 or the frame? Report. (74 unidentified expected.)
- 863-c (accounting): all 38 of 48's windows classified {era-licensed-de,
  anti-de, neutral} with the license cited (fences from F83 reused, not
  re-scored). Pre-registered verdict rule: recommend RE-OPEN of a broader
  48="de" hypothesis iff ≥2 INDEPENDENT licensed de-frames beyond the narrow
  path exist AND no anti-frame contradicts under banked (non-fenced) premises;
  else POINTER-ONLY. Separately scored: a conditioned-syllable lead
  (48 = "de"-cell in 48→47 frames, cf. F33 conditioned polyvalence) —
  recommend BANK-AS-LEAD iff 863-a passes with n≥2 genuine "de ce que".
- Explicit non-goals: does NOT re-run Paths A/B/D; does NOT re-litigate
  "48 pas" @283/@1737 (conditioning escape recorded in D3); the @863 verdict
  cannot by itself promote 48="de" (needs ≥2 independent checks per standing
  rule; red team adjudicates).

## Verdict rules
- Per-leg PASS/ADVERSE/OPEN with numbers; recommendation language only
  (LEAD / FENCED / BANK-AS-LEAD / POINTER-ONLY / OPEN).
- Promotion needs ≥2 independent checks (STATE.md standing rule) — red team
  adjudicates every status change; this package is a recommendation only.
- Fences name explicit missing legs. Nulls recorded honestly. Byte-exact
  positions; the @1077/@1078 prose off-by-one is flagged, not silently fixed.
