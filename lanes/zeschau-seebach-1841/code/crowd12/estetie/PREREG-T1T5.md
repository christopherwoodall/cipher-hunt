# PREREG — Round 12 WO7: ESTE-VERB TIE-BREAKERS T1–T5

Executor: este-tiebreaker (round 12, work order 7).
**Pre-registered 2026-10-07 ~16:30 CDT — BEFORE any new data query for this
work order.** Standing published results read for battery design (NOTES N52,
F80; crowd11/este_verb/PREREG.md + este_verb_results.json; ISLET registry
1/3/10; crowd11 red-team RULINGS-ROUND11 R4); no new stream census, window
extraction, or era count run before this file.

## Standing input (not re-litigated)
- H0 (F80, GRANT): -este verb set-valued {manifeste, atteste, proteste,
  conteste, déteste}. a3-monovalence banked as data: stem@1447 ∉
  by-ear mid-options@1189 ⇒ 84 polyvalent across windows OR @1190's verb ≠
  @1448/@1804's. a3 case law: a stem/frame mismatch is recorded as
  "polyvalent here OR different verb", NEVER a candidate kill.
- ISLET 10 (LEAD): 59=verb-final «-este» iff pre(59)=84 — firm
  @1190/@1448/@1804, fenced @1291. 59="est" provisional elsewhere.
- ISLET 3 (LEAD, conditioned): 06="ent" iff pre(82). ISLET 1: 84="en" iff
  pre∈{82}∪{66,89} (noun identity rescoped/NULL).
- Values: 7 pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que);
  provisional: 87=ce, 64=qui, 96=par, 59=est; 77="le"
  provisional-CONDITIONED.
- Killed/rescoped, not re-litigated: unconditioned-59, unconditioned 84s,
  86=que-family, three mergers, 48="ne", H_verb, refuge concretizations,
  retired WO-6 bar.
- Conditional discriminator (F80, fenced): under @1291 verb-parse +
  [35]=ne-clause-subject, {manifeste, proteste} survive; {atteste,
  conteste, déteste} excluded. Does NOT fire unless @1291 un-fences.

## Canonical parse & positions
Repaired 1,847-pair stream (`code/crowd6/redteam/verify_baseline.load_stream`);
positions 0-based per `code/crowd4/REINDEX.md`. Este windows: p59 ∈
{1190 (06-84-59), 1448, 1804, 1291 fenced}; p84 = p59−1.

## Era reference (pre-registered corpus split)
- **clean-diplo (French, phrase queries + rates):** guizot-memoires-t1,
  t2, t3, t5-t6; metternich-papiere-v4, v6; pozzo-di-borgo-correspondance-v1;
  levant-correspondence-1841-p3; talleyrand-memoires-v1;
  revue-deux-mondes-1841-q1..q4. (1841 diplomatic/literary French —
  register-matched to the despatch; "conter"-class literary verbs flagged
  for register, not counted as diplomatic.)
- **nesselrode-v7/v8/v9/v10:** unigram rates DESCRIPTIVE ONLY; phrase
  zeros VOID (archive.org OCR word-splits per F77 — v8 phrase zeros are
  not French). Never used to kill or license a phrase frame.
- **Excluded:** allgemeine-zeitung-1841-* (German), adb-zeschau (German),
  harvest-log.txt, PROVENANCE.md.
- Tokenizer: round-11 este_verb.py's (NFC, lower, ’-normalized).

## T1 — 84 stem ID outside este frames
Q: does the required stem reading (manif/att/prot/cont/dét) survive where
-este frames don't constrain it?
- (T1a) Census all 25 84-tokens; este-framed = {1189 (middle of 06-84-59),
  1290, 1447, 1803} (59-followed). Free = remaining 21. Full ±3 window
  table with known-value glosses, from code.
- (T1b) Anchored free windows per candidate (stem+neighbor must form
  French): @146 «64(qui) 77(le) 84 29(er)» → stem+"er": conteste→"conter"
  (real word — then test «qui le conter» grammaticality/era); the other
  four → non-words ("manifer","atter","proter","déter" — recorded as
  polyvalence-data per a3 case law, NOT kills).
- (T1c) Era: n("conter"), n("qui le conter"), n("conte") in clean-diplo;
  v8 unigram descriptive. Register flag: "conter" is literary, rare in
  diplomatic prose.
- (T1d) Other anchored free windows recorded: @1501 «74 84 33»
  (33 infinitive-class), @1620 «11(la) 84 78», @1665 «94 84 64(qui)»,
  @1485/@1058/@1764 «77 84 X», @788 «65 84 06».
- **Bar (independent stem-ID leg):** the same stem value required at
  @1447/@1803 must be licensed at a free window by ≥2 INDEPENDENT
  considerations (contact-frame + era-attested word/grammar). EXPECTATION:
  not met — will report honestly.

## T2 — «le» antecedents at @1448/@1804
Q: what does «le» (77, prov-cond) refer to; does the antecedent break the tie?
- (T2a) Wide windows pairs[1420:1470] (@1448) and pairs[1775:1825]
  (@1804), glossed with all banked values.
- (T2b) Enumerate masculine-noun antecedent candidates in left context;
  test each candidate's contact profile for noun-hood (article-adjacency,
  verb-government). Note the structural fact: 37 immediately precedes
  «qui» @1448 and sits 3-back @1804 («37 91 79 ce qui le V»).
- **Bar (antecedent ID):** masculine noun pinned by ≥2 independent legs;
  breaks the tie only if exactly one verb's selectional frame fits it.
  EXPECTATION: inconclusive — will report honestly.

## T3 — 06's ID at @1190 (06="pro" ⇒ proteste)
Q: test the "pro" reading directly.
- (T3a) Local compatibility: pre(06@1188)=42 ∉ {82} → ISLET-3 "ent"
  conditional does NOT fire (no contradiction); by-ear cut 06-84-59 =
  pro|t|este ∈ proteste's banked options; suc(59@1190)=46="que" GT →
  «proteste que» (leg C attested).
- (T3b) Independent "pro"-witness hunt over all 44 06-windows: live
  candidate @346 «1 06 70(="pre" GT) 12» = "pro"+"pre" (missing final -e —
  caveat vs crib-writes-mute-e N17; graded WEAK at best); era-check
  «propre» + left context «87(ce) 1».
- (T3c) Global-06 screen (scoping only): 06→77 ×6, 06→59 ×2, 06→0 ×3,
  06→29 ×4, 06→67 ×3 — recorded as polyvalence scoping (06 polyvalent is
  live lane-wide), NOT a window-local kill.
- **Bar:** 06="pro"@1188 graded LEAD iff (a) passes AND (b) ≥1
  corroborating window (even weak). Does NOT promote proteste alone —
  the este-verb PROMOTE bar (≥2 independent legs + stem-ID leg) is the
  red team's, not T3's. EXPECTATION: COMPATIBLE-UNCONFIRMED.

## T4 — 17/35 for @1291
Q: can 17 and 35 resolve (≥2 legs each) to un-fence @1291?
- (T4a) 17 census (n=15) + full contact table. Test 17="fois"-WEAK:
  era «la fois» + finite verb WITHOUT «que» (expect 0 — ungrammatical);
  supporting: 17→46 ×1 @308 («17 que»); tension: 17→64 @17
  («17 qui» — noun+relative signature).
- (T4b) 35 census (n=10) + full contact table. Test 35=ne-clause subject:
  profile (pre: 59 ×3, 58 ×2, 64/52/74/21/26; suc: 94 ×2, 56 ×2, 53 ×2,
  58/93/18/13); tension: 64→35 @1359 («qui 35» — verb-slot signature vs
  subject role); positional parallel «59 35 94» ×2 (@1292, @1805).
- **Bar (un-fence @1291):** 17 AND 35 EACH resolved with ≥2 independent
  legs. EXPECTATION: stays fenced; conditional discriminator stays
  conditional.

## T5 — a second «qui le [84-59]» token
Q: is there another 64-77-84-59 beyond @1448/@1804?
- Byte-exact census: 64-77-84-59 n-grams; also 77-84-59 and 64-77-84
  (near-miss @144: 64-77-84-29). All from code.
- **Bar:** a third 64-77-84-59 token with discriminating context = new
  leg; else CLEAN NEGATIVE (known: exactly 2×).

## Anti-gaming & method
- No manual-tiling bearing counts (F59) — every count from scripts.
- No re-litigation of settled kills (listed above).
- Red team adjudicates any status change; nothing self-promoted.
- Era/register discipline: 1841 diplomatic French throughout; literary
  verbs flagged, not smuggled.
- Outputs: `estetie_results.json` + `PREREG-T1T5.md` (this file) in
  `code/crowd12/estetie/`; report note at
  `code/crowd12/report_inbox/estetie-t1t5.md`.
