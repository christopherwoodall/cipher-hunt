# Battery adj-37-385-gate — verdict: NULL (fence; bar's else-branch fires)

**Target:** `adj-37-385-gate` (P3)
**Date:** 2026-10-09
**Worker:** battery protocol §1–§6 followed. Lock `locks/adj-37-385-gate.lock` created on start, deleted on completion. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

> "name 38's class from its 7 windows (@384/@826/@1113/@1343/@1469/@1650/@1828); iff 38 is determiner/adjective-shaped, @385 ('[38] 37 [43-noun]') confirms 37 in a prenominal adjective slot and re-anchors the la-vote; else record 38's class and close"

**Numbered clauses:**
- C1: name 38's class from all 7 windows.
- C2 (conditional): iff 38 is determiner/adjective-shaped, @385 ("[38] 37 [43-noun]") confirms 37 in a prenominal adjective slot and re-anchors the la-vote.
- C3 (else): record 38's class and close.

## Method

Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`. Result: 1,847 pairs / 96 types. n(38) = 7, byte-confirmed, matching the brief's window list. All @-offsets below are 0-based queue convention (brief's "@385" = 1-based; 0-based 38 sits at @384).

Standing values used as premises only (never re-litigated): 11="la", 29="er", 40="e", 46="que" (pencil GT); 87="ce", 64="qui", 96="par", 17="fois", 79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4 allophone); 59="est" provisional; 30="pas" battery-promoted. 43's nominality is red-team venue (redteam-43-polyvalence; noun-43's noun values all kill-grade dead at battery grade) — not assumed here.

## Window-level evidence (all 7 windows, byte-traced)

- **W1 @384 (a2_07, mid-row):** `16 52 | 38 | 37 43 91 36`. 38 between 52 and 37. 52 is a §7 split candidate (adverb/adjective arms live); 37 is the A1 predicative-frame cell. Neither determiner nor adjective forced — neutral/open.
- **W2 @826 (a5_06, mid-row):** `87 59 | 38 | 82 01` = "ce est [38] m[01]". Adjective-shaped: "c'est [38-adj]" is the clean predicative-adjective slot. Determiner: "c'est [38-det] m[01]" needs an m-initial noun; 01's live values ('en'/'tain'; 'ci' kill-grade dead per R17-015) give no nominal m-word at standing grade — determiner weak here, not kill-grade dead.
- **W3 @1113 (a6_07, mid-row):** `65 38 30 69` = "[65-noun] [38] pas [69]". **Determiner-38 is kill-grade dead here:** a determiner immediately followed by "pas" (30="pas" battery-promoted) with no nominal complement is ungrammatical in 1841 French. Adjective-38: "[65-noun] [38-adj] pas [69]" = postposed epithet + ne-drop negation (ne-drop is lane precedent per battery-w2-pas-nelicense) — fully grammatical. Clean adjective leg.
- **W4 @1343 (a7_05, mid-row):** `64 52 38 47 86` = "qui [52] [38] ce [86]". Relative "qui" (64 banked GT) requires a finite clause. Determiner-38: "qui [52] [38-det] ce…" — determiner before "ce" with no nominal — ungrammatical. Adjective-38: "qui [52] [38-adj] ce [86-verb]" — adjective intervening between "qui" and the subject "ce" with no byte-evidenced parenthetical — ungrammatical. Neither parses → uniform class naming blocked at this window. Fenced with stated cause (no rescue attempted with unmarked structure).
- **W5 @1469 (a7_09, mid-row):** `62 38 26 12`. 62 = règne/trône (noun/verb-stem, open); 26 positional noun/verb (R17-020 HELD). Adjective: "[62-nom] [38-adj]" epithet — compatible. Determiner: "[62] [38-det] [26]" — needs noun-26 under the positional rule; compatible, not forced.
- **W6 @1650 (a8_04, mid-row):** `03 38 82 16`. 03 = verb-stem class. Adjective after infinitive ("[03-er] [38-adj]") — unlicensed in 1841 French. Determiner ("[03-er] [38-det] m[16]") — needs nominal m-word; 16's class/value fenced (val-16-a-vs-est NULL). Neither clean — weak/undecidable.
- **W7 @1828 (a8_11, mid-row):** `29 82 38 83 24`. Sub-lexical "-erm" precedes 38. Neither determiner nor adjective forced — weak.

## Per-clause results

- **C1 — FAIL at uniform-naming grade.** Determiner-38 is kill-grade dead (W3). Adjective-38 has clean legs (W2 predicative, W3 epithet) and compatible W5, but W4 resists both determiner and adjective → no uniform class nameable at battery grade. Per the bar's else-branch, 38's class is recorded and closed: **38 = adjective-shaped at W2/W3 (locus-level); determiner arm closed; W4 fenced with stated cause; W1/W6/W7 undecidable at standing grade.**
- **C2 — does not fire.** The consequent's frame "@385 ('[38] 37 [43-noun]')" requires 38 as a DETERMINER (parallel to the la-frame Type-A: determiner + prenominal-adjective + head-noun). The determiner arm is dead, so the required parse is unavailable. With adjective-38, @385 = "16 52 | [38-adj] [37] [43]" = three stacked prenominal adjectives with no determiner — a bare NP, ungrammatical in 1841 French. Additionally the "[43-noun]" premise is battery-closed (redteam-43-polyvalence venue; cannot be assumed). **37's prenominal-adjective confirmation at @385 is NOT established; the la-vote re-anchor does not fire.**
- **C3 — FIRES.** 38's class recorded above; target closed.

## Adverses answered

- "38's class fully open" — narrowed: adjective-shaped at W2/W3 (locus-level), determiner kill-grade dead at W3, W4 fenced with cause. No longer "fully open," but not uniformly nameable.
- "'52-38-37-43' segmentation ambiguous" — answered: the Type-A parse from battery-la-frame-52-37-43-noun ("la [52-37-prenominal-adjective-unit] [43-head-noun]", adopted as premise, not re-litigated) is what makes the ambiguity resolvable only through a determiner-38; with the determiner arm dead, no live segmentation gives 37 a prenominal-adjective slot here.

## Standing-state check

No red-team verdict exists on 38; nothing contradicted or downgraded. §7 intact (no polyvalence declared — the finding is a class narrowing plus a fence, not a value). The a7_05 rival-phase note from battery-phase-likelihood-row-sweep (−0.85, weak) and the standing canonicality caveat (68 of 70 upstream offsets unvalidated) are recorded, not litigated.

## Follow-ups proposed (null → 1–3 required; all verified absent from queue)

1. `val-52-38-unit` (P3) — test "52 38" as a prenominal-adjective unit at @384/@1343 per the la-523743-adjective Type-A precedent (52's adjective arm {même/seule} is live).
2. `adj-38-w4-parse` (P3) — resolve W4's "qui 52 38 ce 86" with 38's class open; fence W4 if no parse survives.
3. `tail-385-rerun-43poly` (P2) — re-run the @385 re-anchor once redteam-43-polyvalence adjudicates 43's nominality (the "[43-noun]" premise gate).
