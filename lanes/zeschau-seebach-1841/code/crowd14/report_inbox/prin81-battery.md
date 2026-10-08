# prin81 battery report — 81="prin" ("le prince"×2) adjudicated (2026-10-07)

**Battery verdict: KILL** (red-team adjudication required before merge, standing rule).
Full evidence: `code/crowd14/prin81/` (PREREG.md pre-registered bar, corpus_test.py,
corpus_results.json, ANALYSIS.md).

## What was tested
F108 drag docket item "le prince"×2 @1240/@1401 (77-81-87 → le-prin-ce),
the "la pour" post-context adverse, the F107 "cela" ambiguity, and the
F-C@1088 anchor flanks (@1086/@1095).

## Findings
1. **Windows re-derived byte-exact** from the repaired 1,847-pair stream
   (never canonical.py). Both are `67-77-81-87-11-00`; 67="et" fires via
   ISLET-4 at both; both outside the repaired region (748–772).
2. **"la pour" adverse RESOLVED against the lead.** Corpus (34 files,
   4.22M tokens, lane tokenizer): "le prince la" = 0; "la pour" = 12 hits,
   all constituency-read — 8× "là"→"la" OCR, 3× "poursuite" splits, 1×
   genuine "prenez-la pour évangile" (verb-governed pronoun frame,
   inapplicable to noun+"la pour"+inf). Bare "la"+"pour" with no governing
   verb is **era-fenced at 0**. "et le prince la pour …" is ungrammatical
   in 1840s diplomatic French.
3. **No re-reading of 11="la" (GT) or 00="pour" (STRONG LEAD) needed.**
   Both stand untouched; it is the "le prince" reading that dies. No
   conflict to escalate.
4. **F107 ambiguity adjudicated: "cela" kills "le prince" at both windows.**
   Mutually exclusive (share cell 87). "cela"=87-11 ×7 standing unit
   (crowd5, frenchman-verified); "cela pour" 25× era-attested; bonus leg:
   @1244-1245 = 00-33 = "pour [33-inf]", the round-12 F-C frame recurring.
   Recommend segmenter clear `live*`→`live` on "cela"@1242/@1403.
5. **F-C anchor: TENSION.** Under 81="prin", @1086 (55-81-00) needs a
   word ending in "-prin" — corpus: zero French words (144 tokens all
   German-OCR fragments); @1095 (55-81-06) needs "prin"+06 with 06
   unvalued (oracle needs pre==82). Not an anchor pair; second strike.
6. **No other 81 supports "prin":** 14 total 81s; only @1241/@1402 have
   the 81-87 shape. Consistent with F108 FDR≈1.4 (real 9 vs null
   13.1±5.2) — the hit is FDR-consistent noise.

## Disposition
- 81="prin" KILLED as a docket item; 81 stays UNIDENTIFIED.
- "le prince"×2 closed as chance artifact; bytes read "et le [81] cela
  pour …" with "cela" confirmed.
- Nothing else disturbed: 11="la" GT, 00="pour" STRONG LEAD, 77="le"
  provisional, 87="ce" provisional all hold.
