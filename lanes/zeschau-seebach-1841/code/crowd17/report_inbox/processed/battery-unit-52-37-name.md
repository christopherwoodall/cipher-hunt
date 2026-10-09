# Battery report: unit-52-37-name (NULL — split candidacy to red team)

**Target:** unit-52-37-name — one name for the 52-37 unit across three context types, or split
**Worker:** 1e84068c-3e24-4e2a-958e-e92c14df1fca | **Date:** 2026-10-08
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Never canonical.py. No R5005 touched. No data invented. Every @-offset re-derived from the stream.

## Bar (verbatim from battery-queue.json)

> name the unit iff one value parses all three context types with <=10% orphan; else state the split candidacy (52~52) with per-window parses for red-team adjudication — do not declare polyvalence at battery level

## Bar as numbered clauses

1. One value V names the 52-37 unit iff V parses all three context types — Type A 'la 52-37 43' x2 (@1124, @1722), Type B '86 52-37 86' x1 (@1129), Type C '94-82-06 52-37 qui 35' x1 (@1356) — with <=10% orphan windows (4 windows × 10% = 0.4 → effectively all four must parse).
2. If clause 1 fails: state the split candidacy (52~52) with per-window parses for red-team adjudication.
3. Do not declare polyvalence at battery level (protocol §7: 67 et/veut is the sole true polyvalence).

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (1,847 pairs; asserts hold).
2. Re-derived all 52-37 bigrams by exact match: x4 at @1124, @1129, @1356, @1722 (52-37 @-offsets index the 52; the la-523743 battery indexes the preceding 11 at @1123/@1721 — same windows).
3. Full 52 census (n=27) with ±3 contexts; full 37 census cross-checked against the la-523743-adjective battery (2026-10-08), whose Type-A parse ("[verb-ent] la [52-37-adj-unit] [43-head-noun] pour [86]") is adopted as verified and not re-litigated.
4. Verified every evidence n-gram in the target brief: '94-52-30' trigram x0; byte-identical 6-gram '84-59-35-94-52-80' @1290/@1803; '52-37-86' hapax @1129; '86-52' x2 (@1099, @1128); '11-52' x3 (@1006/@1123/@1721).
5. Tested the four strongest single-value candidates for the unit (même, seule, dite/ladite, telle) against all three context types under standing values only (11=la, 00=pour, 64=qui, 94=ne, 06=ent, 82=m banked/promoted; 59=est, 77=le provisional; 43 = head noun per frame-43 battery; 86 = INF class / "le" determiner-life).

## Window-level evidence

**Type A — '11 52 37 43' x2 (adjectival, firm):**
- @1124 [a6_07]: `06 14 06 [11 52 37 43] 00 86 52 37 86` → "ent la [52-37] [43] pour [86] …"
- @1722 [a8_07]: `68 06 [11 52 37 43] 98 39 88` → "…ent la [52-37] [43] [98] …"
- Per la-523743-adjective (verified): 52-37 is a prenominal adjective unit; 43 is the head noun (condition/mesure-type, feminine — agrees with "la"). Candidate values all parse: "la même [43]", "la seule [43]", "la dite [43]" (= ladite, peak diplomatic register), "la telle [43]" (marginal).
- 52 is adjective-shaped here, window-locally. 52's global profile pulls three ways (nominal 'la 52' x3; clitic '94-52-80' x2; '52-82' x5) — the adjective reading does not generalize.

**Type B — '86 52 37 86' x1 @1129 [a6_07] (segmentation open):**
- Full clause: `… 06 [11 52 37 43] 00 [86] [52 37] [86] 24 77 [86] …` → "[43] pour [86] [52-37] [86] [24] le [86]" — five pairs downstream of the Type-A window, same clause.
- Under 86=INF: "pour [inf] X [inf]" with X adjectival — ungrammatical for every Type-A candidate ("pour faire même faire", "pour faire seule faire", etc.).
- Under 86="le" (determiner-life, strong in 'pour' frames: '00-86' x12): "pour le X le [24]" — ungrammatical for every candidate ("pour le même le [verb]", "pour le seule le [verb]").
- The '52-37-86' trigram is a hapax; 37-86 occurs nowhere else (37's 28-window census). Segmentation "86 [52-37] 86" assumed; "[86-52] [37] [86]" and "[86] [52] [37-86]" have no independent support. No standing 86-value rescues an adjectival X here.

**Type C — '94 82 06 52 37 64 35' x1 @1356 [a7_05] (nominal position):**
- Wide: `34 62 48 77 78 [94 82 06] [52 37] 64 35` → "[i] [62] [e] le [78] ne(94) m(82) ent(06) [52-37] qui(64) [35]".
- The "94-82-06" trigram is fixed stream-wide x4 (@579, @737, @1183, @1356; @737 lacks 94: '18 82 06'). With 94=ne (R17-001 STRONG LEAD), 82=m, 06=ent, no grammatical French parse of "ne m ent" exists at battery grade — left edge fenced, not parsed.
- 52-37 sits as bare antecedent of "qui": "même qui", "seule qui", "dite qui", "telle qui" are all ungrammatical without a determiner in 1841 French. The only rescues re-segment (antecedent larger than 52-37, or 37 pairing rightward as "37-64" = "ce qui", cf. '59-37-64' x2 @529/@1444) — each abandons the single-unit claim.
- The la-523743 battery recorded this as "the 52-37 unit as nominal antecedent of 'qui' — a positional split, recorded not declared."

**Orphan count:** Type A parses 2/4 windows under the best single value; Types B and C parse 0/4. Orphan rate 50% ≫ 10% bar.

## Per-clause pass/fail

1. **Single value for all three types — FAIL.** No candidate ("même", "seule", "dite", "telle", and by extension any feminine prenominal adjective) parses Types B and C. Type A forces adjectival; Type C forces nominal-ish; Type B parses under no standing value. 50% orphan vs the 10% bar.
2. **Split candidacy with per-window parses — PASS (stated below).**
3. **No polyvalence declared — PASS.** The split is a candidacy for red-team adjudication, not a battery-level declaration.

## Split candidacy (52~52) for the red team

- **Windows @1124/@1722 (Type A):** 52-37 = prenominal adjective unit, "la [X] [43-noun]". 52 adjective-shaped (window-local). X ∈ {même, seule, dite} at lead grade; 37's sub-lexical value inside the unit unresolved — S5 (37="le") owns 37 and is already escalated to s5-foundation; this battery does not touch it.
- **Window @1356 (Type C):** 52-37 in nominal/antecedent position before "qui". 52's role here is irreconcilable with the Type-A adjective reading under one value. Left edge "94-82-06" unfenced-parseable at battery grade.
- **Window @1129 (Type B):** "[86] [52-37] [86]" hapax; neither the adjectival nor a nominal reading parses under standing 86-values; segmentation open.
- **Red-team question:** is 52 split (adjective-internal "52" vs nominal "52" — cf. NOTES.md F31/F33: 52="pas" STRONG but bounded to negation frames, rival 52="se" LEAD, K5 forces 52 polyvalence), or is 37 split, or is one context type mis-segmented? Battery-level evidence cannot decide; no second polyvalence declared here per §7.

## Adverses answered

- **Protocol §7 (67 sole true polyvalence):** respected — no polyvalence declared; the 52~52 split is referred to the red team as a candidacy with per-window parses, exactly as the bar requires.
- **@1129 hapax segmentation:** confirmed '52-37-86' hapax on the repaired stream; "86 [52-37] 86" retained as the working segmentation with stated cause (no support for "[86-52] [37] [86]" or "[86] [52] [37-86]"); left open via follow-up F3 rather than forced.

## Verdict

**NULL.** No single value names the 52-37 unit across the three context types (50% orphan vs the 10% bar). The Type-A adjectival reading ("la [X] [43]") is firm but window-local; Types B and C do not admit it. Split candidacy (52~52) stated above for red-team adjudication. No standing verdict contradicted or downgraded; R5005, sealed gates, and the red-team queue untouched.

## Follow-up targets for the supervisor queue (null regeneration)

**F1. id: "adj-52-37-value" | priority: 2**
claim: "The Type-A 52-37 adjective is named (même vs seule vs dite discriminated)"
bars: "decide among {même, seule, dite} using 43's resolved noun value and wider prenominal-adjective frames; name iff one candidate parses both @1124/@1722 with <=1 ungranted assumption"
evidence: "unit-52-37-name null (2026-10-08): Type A firm 'la [X] [43-noun]', X ∈ {même, seule, dite}; 43 = head noun (frame-43 battery)"
adverses: "37's sub-lexical value owned by S5/s5-foundation — do not decide 37; name the unit only"

**F2. id: "seg-94-82-06" | priority: 2**
claim: "The '94-82-06' trigram left edge resolves (ne+ment vs alternatives)"
bars: "parse '94-82-06' x4 (@579/@737/@1183/@1356) under standing values; name the segmentation iff one parse covers all four with <=1 ungranted assumption, else fence with stated cause"
evidence: "unit-52-37-name null (2026-10-08): '94-82-06' x4 fixed trigram, 'ne m ent' ungrammatical as parsed; blocks 52-37's slot assignment in Type C"
adverses: "94='ne' STRONG LEAD (R17-001) — do not overturn; re-segmentation only"

**F3. id: "seg-86-52-37-86" | priority: 3**
claim: "@1129 segmentation decided among '86 [52-37] 86' vs '[86-52] 37 86' vs '86 52 [37-86]'"
bars: "adjudicate using 86's resolved value(s) and 86-52 x2 (@1099/@1128); decide iff one segmentation parses the full clause '…43 pour 86 52 37 86 24 77 86…' grammatically"
evidence: "unit-52-37-name null (2026-10-08): '52-37-86' hapax @1129; '86-52' x2; clause continues the Type-A window five pairs downstream"
adverses: "86=INF class granted (A9) with determiner-life — both lives must be honored or fenced"

---
Lock: locks/unit-52-37-name.lock created 2026-10-09T02:16:46Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No promotions made. No red-team verdicts modified.
