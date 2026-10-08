# VALUE-52 hunter report — round 14 WO5 (2026-10-07)

Executor: value52 battery. Scope: `code/crowd14/value52/`.
Stream: repaired 1,847-pair parse, re-implemented here from
`code/side-keyhunt/repaired_offsets.json` (asserts: 1,847 pairs, 96 groups,
"la première" @754 and @1034). Corpus: clean-diplo pool verbatim
(FRENCH_CLEAN + lane tokenizer; N=3,618,487 here).

## T1 — 52 census, re-derived (n=27, positions match round-13 exactly)

pos | pre→52→suc | est-frame verdict
--- | --- | ---
160 | 93→52→94 | STRAINED (r13: 93="l'" needs "ne" before; "ne" follows)
264 | 93→52→33 | FAIL ("l'est"+infinitive)
284 | 48→52→89 | UNTESTED
383 | 16→52→38 | UNTESTED
482 | 13→52→30 | UNTESTED
571 | 94→52→87 | FAIL ("n'est-ce" needs "pas")
632 | 8→52→67 | UNTESTED
649 | 78→52→82 | STRAINED ("le [78] 52 m ne", W3 opaque)
1007 | 11→52→35 | **IMPOSSIBLE** ("la est"=0)
1081 | 6→52→89 | IMPOSSIBLE-COND (pre=Vstem-class; cond. on prov. 06)
1100 | 86→52→82 | IMPOSSIBLE-COND (pre=Vstem2; cond. on prov. 86)
1124 | 11→52→37 | **IMPOSSIBLE** ("la est"=0)
1129 | 86→52→37 | IMPOSSIBLE-COND (pre=Vstem2)
1294 | 94→52→80 | AMBIGUOUS ("n'est 80" vs "ne pas 80")
1308 | 74→52→30 | UNTESTED
1332 | 70→52→39 | UNTESTED
1342 | 64→52→38 | **CLEAN** ("qui est", era 904)
1356 | 6→52→37 | IMPOSSIBLE-COND (pre=Vstem-class)
1385 | 68→52→82 | UNTESTED
1409 | 46→52→42 | **IMPOSSIBLE** ("que est" unelided=0; elision caveat noted)
1416 | 34→52→32 | UNTESTED (word-internal "i|est" not excludable)
1435 | 64→52→82 | STRAINED ("qui est m[16]" needs 82-led word)
1441 | 1→52→68 | UNTESTED
1574 | 28→52→82 | UNTESTED
1722 | 11→52→37 | **IMPOSSIBLE** ("la est"=0)
1738 | 48→52→86 | UNTESTED
1807 | 94→52→80 | AMBIGUOUS (same 5-gram as @1294)

Tally: CLEAN 1, AMBIGUOUS 2, STRAINED 3, FAIL 2, IMPOSSIBLE 8 (3×"la",
1×"que", 4×Vstem-conditional), UNTESTED 11. The 7 EST-LICENSED grades
reproduce round-13 VERDICT.md (positions re-derived identical).

## T2 — "la 52"×3 verdict: FENCED, no viable candidate

- Re-derived from the repaired stream: @1007 (47 91 **11 52** 35 18 79),
  @1124 (14 6 **11 52** 37 43 0), @1722 (68 6 **11 52** 37 43 98). Exactly 3.
- "la est"=0 re-verified on the clean pool (n("la")=91,558; "la est" 0×).
- **New:** @1124 and @1722 share the identical 5-gram **6 11 52 37 43** ×2
  (@1122–1126 / @1720–1726) — the la-arm is formulaic, n_eff=2 types.
- Corpus inversion, pre-registered bar (LEAD iff era P(W|"la") within
  factor-2 of cipher P(52|"la")=3/45=0.0667): the ONLY in-band word is
  **"france"** (0.0430, ratio 0.65). Next-best "chambre" is 4.6× under.
- "france"-as-word is **KILLED**: era P("france")=0.0016 vs cipher
  P(52)=0.0146 = **9.1× gap**. Whole-word reading dead; "fra"-syllable
  reading has no F30-legal legs (not proposed, not killed).
- Missing legs (named): IDs of 37/43 (the ×2 formula's tail) and 35;
  or a second in-band era "la W" phrase surviving all three windows.
- Verdict: **FENCED**. "la 52" is a conditioned non-est arm (pre==11),
  value unidentified. (F33-grade conditioning would need the value;
  not claimed.)

## T3 — positional-allophone test: STRENGTHENED

- **0 shared (pre,suc) frames** across all 54 windows of {52,59}.
  For all 9 shared predecessors the successor sets are disjoint
  (e.g. pre=94: 52→{80,87}, 59→{30,37,39}; pre=11: 52→{35,37}, 59→{42};
  pre=64: 52→{38,82}, 59→{19,32}; full table in `value52_deep.json`).
- Monte Carlo (20k label-shuffles, H0=free homophony): P(0 shared)=**0.059**
  — marginal, same neighborhood as the -este Fisher p=0.0555. Two
  independent marginal signals, same direction: corroborating, not decisive.
- -este arm re-derived: pre=84 → 59 ×4 (@1190/@1291/@1448/@1804), 52 ×0.
- The 3 ±3 co-occurrences (@1294: 59@1291 pre=84 vs 52@1294 pre=94;
  @1807: 59@1804 pre=84 vs 52@1807 pre=94; @1441: 52 pre=1 vs 59@1444
  pre=68) are all in **different frames** — proximity, not same-environment.
  Allophony is about environments, not proximity: no kill.
- **New datum:** 11→59 ×1 @463 ("ce la 59 42") — 59 also occurs after "la"
  ("la est"=0 kills est there too), with suc=42 vs 52's suc∈{35,37}.
  Same-pre/different-suc is exactly the allophone prediction.
- Verdict: the F103 split is **corroborated, not re-litigated** (per WO:
  the split stands). Do not merge 52/59 windows in the solver.

## T4 — F106 P1c fence: respected

No est-class value is proposed for 52. The est-arm lead rests on a single
clean frame (@1342) — below the ≥2-leg bar, and the P1c anti-promotion
fence is not addressed by any new leg. Fence holds.

## 52's status after this round: UNIDENTIFIED (ranked)

1. **est-arm only (pre∈{64,94,93}), WEAK** — 1/7 clean frames; fence holds.
   Adverse: 52 runs 1.9× hotter than era "est" (0.0146 vs 0.0076).
2. **la-arm conditioned value (pre==11), FENCED** — missing legs named above.
3. **Vstem-arm (pre∈{6,86} ×4: @1081/@1100/@1129/@1356), OPEN residual** —
   est ruled out conditional on provisional 06/86; inflection/clitic arm
   unidentified; needs its own battery (referred, not run here).
4. **"france"-word: REJECTED** (unigram 9.1× kill).
5. **"pas" (K5/N29): not revived** ("la pas 37" etc. still fail).

## Files
- `code/crowd14/value52/value52.py` — census + era pass
- `code/crowd14/value52/value52_deep.py` — la-candidacy, frame splits
- `code/crowd14/value52/value52_stats.py` — MC test, unigrams, 5-gram verify
- `code/crowd14/value52/value52_results.json`, `value52_deep.json`,
  `value52_stats.json`
