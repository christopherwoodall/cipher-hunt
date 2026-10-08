# Battery report: split-92-redteam-evidence — re-derived evidence package for red-team adjudication

- Target: `split-92-redteam-evidence` (claim: "carry the re-derived 92 tripartite-governor evidence package to red-team adjudication (evidence only, no split decision)")
- Worker: subagent f614fe1a-3cad-484c-a12b-5a330d195b8a
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`; canonical.py NOT used, R5005 NOT touched)
- Lock: `code/crowd17/next-token/locks/split-92-redteam-evidence.lock` (created 2026-10-08T12:36:34Z; no prior/stale lock on this target)

## Bar (verbatim, pre-registered before testing)

"package the re-derived window table + @1154/@1550/@1022 parses for red-team adjudication; no class named, no split declared"

Restated as numbered pass/fail clauses:

- **C1**: re-derive the 22-window 92 table (offsets + governor census + follower census) independently on the repaired stream — use battery-class-92.md and battery-split-92-adjudication.md as coordination context only, not as source.
- **C2**: re-derive the hinge windows @1154 ('02 00 92 29 80' = 'pour [92]er' verbal forcing), @1550 ('pour que prenne [92] ce' — inverted postposed subject vs direct object, both live), @1022 (fenced as residual R-class92-1022, anomalous under all classes).
- **C3**: verify the '94→92 x2' correction (only @65-66 is a true ne-governor; @1549's 94 is word-internal to 'prenne') and the @683 A6 fence, without re-litigating A6 or the killed '-ère' value.
- **C4**: package evidence only — no class named, no split declared, no polyvalence assigned (§7: 67 sole true polyvalence; battery-level split is forbidden); nothing written to the red-team adjudication queue; coordinate with (do not duplicate) queued prenne-92-noun's noun-value arm.

## Method

Parsed the repaired stream from scratch (repair_parse.py logic: `repaired_offsets.json` + `../data/upstream-ct_R5005.txt`; 1,847 pairs asserted). Scanned for all '92' tokens, dumped predecessor/follower for each, ran a global governor census and follower census. Cross-checked byte-level contexts at the hinge windows (@1154, @1550, @1022, @683, @66) against the coordination context. Every offset below is a repaired-stream @-offset; every count is re-derived, none copied.

## Window-level evidence — independently re-derived

**n(92) = 22**, offsets: @49, @66, @203, @321, @330, @354, @356, @593, @683, @901, @978, @1022, @1154, @1218, @1310, @1361, @1379, @1453, @1490, @1550, @1607, @1673 — identical to the coordination context, byte for byte.

**Governor census (re-derived, sums to 22):** 00x6 (@49, @330, @593, @683, @978, @1154), 11x3 (@203, @321, @1607), 84x2 (@1022, @1379), 94x2 (@66, @1550), singletons: 40 (@354), 98 (@356), 16 (@901), 83 (@1218), 30 (@1310), 13 (@1361), 46 (@1453), 31 (@1490), 81 (@1673). Tripartite governor profile confirmed as stated.

**Group {00x6} → verbal (00='pour', A9 granted):**
- @1154: `02 00 92 29 80` = "pour [92]er ..." — 92 takes the -er infinitive ending directly (A10 stem composition). Verdict-grade verbal forcing at this locus; "pour"+noun-reader impossible here. Single strongest window in the profile. CONFIRMED.
- @683: `07 00 92 64 29 40 65` — the A6 frame ([09/92]-qui-er-e-65). Fenced per A6; value killed, not re-litigated. CONFIRMED.
- @49/@593: `00 92 79` x2 — 'pour [92]' with the same follower 79; @330: `00 92 50`; @978: `00 92 07`. CONFIRMED.

**Group {11x3} → nominal-or-clitic+verb (11='la', banked):**
- @203: `87 11 92 63`, @321: `06 11 92 60`, @1607: `39 11 92 65`. Article-'la [92]': grammatical as article+noun/adjective or object-clitic+finite-verb; ungrammatical as article+whole-word-infinitive. CONFIRMED, all three identical to context.

**Group {84x2} → finite-verbal (84='on', A15 unconditioned per collision-62-84 battery 2026-10-08):**
- @1379: `89 84 92 69` = "[89] on [92] [69]" — clean under VFIN/clitic; "on"+noun ungrammatical with 84 unconditioned. CONFIRMED.
- @1022: `53 84 92 64 45 64 96` = "[53] on [92] qui ce qui [96]..." — see fencing below. CONFIRMED.

**Group {@1550} → prenne clause:**
- Byte context re-derived: `@1545:00 @1546:46 @1547:70 @1548:12 @1549:94 @1550:92 @1551:45` = "pour que prenne [92] ce...". @1549's 94 is word-internal to "prenne" (70-12-94 immediately precedes 92). The '94→92 x2' closed-set claim is thereby CORRECTED: only @65-66 is a true ne-governor. CONFIRMED.
- @1550's two live parses (both handed intact to the red team and queued prenne-92-noun): (a) inverted postposed subject — "pour que prenne [92-S]" (literary inversion); (b) direct object — "pour que [S] prenne 92" with the subject slot open. Choosing is the red team's act; neither decided here.
- @66 re-derived: `40 12 94 92 69` = "[...] n ne [92]" — 'ne [92]' parses under VERB (ne-explétif/literary), ungrammatical under NOUN. The only true ne-governed 92. CONFIRMED.

**@1022 fenced as residual (re-derived):** `53 84 92 64 45 64 96` — "on [92] qui ce qui [96]". Under NOUN: "on"+noun ungrammatical at the governor. Under VFIN: "[92-verb] qui" ungrammatical; "on [92-clitic]" leaves 'qui ce qui' unparseable. Under whole-word INF: 'on'+infinitive ungrammatical. Under ADJ: 'on'+adjective ungrammatical. Anomalous under ALL classes. Fenced as residual **R-class92-1022**; red-team eyes. CONFIRMED.

**Singletons (re-derived predecessor/follower):** @354 `40 92 98`, @356 `98 92 47` (adjacent `40 92 98 92 47` — two 92s two apart), @901 `16 92 67`, @1218 `83 92 61`, @1310 `30 92 44`, @1361 `13 92 62`, @1453 `46 92 62` ("que [92]"), @1490 `31 92 39`, @1673 `81 92 60`. None contradicts the tripartite profile; none resolves it.

**FOLLOWER CENSUS — PACKAGE CORRECTION (re-derived, contradicts the coordination context):**
The split-92-adjudication report states "max 2x clusters are 92→64 ('qui', @683 + @1022) and no other repeated follower pair". On the re-derived stream there are FIVE repeated 2x follower pairs, not one:
- 92→79 x2 @49, @593
- 92→69 x2 @66, @1379
- 92→60 x2 @321, @1673
- 92→64 x2 @683, @1022
- 92→62 x2 @1361, @1453
All other followers are singletons. Assessment: the scatter remains neutral — no follower dominates (max 2/22 = 9%) — but the package's follower-scatter line is factually wrong and must be corrected before red-team adjudication. Follow-up F1 below. Nothing in the tripartite evidence turns on follower scatter, so the package itself stands with this correction applied.

## Coordination with queued prenne-92-noun (no duplication)

This battery tested NOTHING about 92's value — the noun-value arm (incl. the 'la 92' x3 + '92 qui' x2 feminine-noun lead) belongs entirely to prenne-92-noun. @1550's byte string verified and both parses handed over. Adverses documented for that target's runner: @1154 ("pour [92]er" — verbal forcing) and the {84x2} 'on 92' group remain fenced here.

## Standing constraints observed

Did not touch R5005, sealed gate instances, or the red-team adjudication queue. Nothing promoted, killed, split, or re-valued. The killed '-ère' value was NOT re-litigated. A14's set-level INF-signal and the 09~92 HOLD are untouched and consistent with this evidence. No contradiction with any standing red-team verdict; no downgrade of anything.

## Per-clause results

| clause | result |
|---|---|
| C1 — 22-window table re-derived | **PASS** — all 22 offsets + governor census byte-identical to coordination context |
| C2 — @1154/@1550/@1022 re-derived | **PASS** — @1154 verbal forcing, @1550 both parses live, @1022 fenced R-class92-1022; all anomalous/parse statements independently confirmed |
| C3 — '94→92 x2' correction + @683 A6 fence | **PASS** — @1549's 94 word-internal to 'prenne' (only @65-66 true ne-governor); @683 fenced under A6, not re-litigated |
| C4 — decide nothing; package held | **PASS** — no class named, no split declared, nothing written to the red-team queue |

## Verdict: NULL (evidence-package null, per bars)

The bar is red-team-adjudication-only, so this battery cannot return promote or kill: the split-vs-polyvalence-vs-governor-misread question is undecidable at battery level under §7 (67 sole true polyvalence). The tripartite governor profile is real on the repaired stream and independently verified. The re-derivation did not fail — it succeeded with ONE package correction (follower scatter: five 2x pairs, not one). The corrected package is carried to red-team adjudication.

## Follow-up for the supervisor (null regeneration)

### F1 — id "split-92-followers-amend" (priority 2)
- claim: "the follower-scatter line in battery-split-92-adjudication.md is factually wrong and must be amended before red-team adjudication"
- evidence: "re-derived on the repaired stream (this report): 92→79 x2 (@49/@593), 92→69 x2 (@66/@1379), 92→60 x2 (@321/@1673), 92→64 x2 (@683/@1022), 92→62 x2 (@1361/@1453) — FIVE repeated 2x pairs, not '92→64 x2 only'. Scatter still neutral (max 2/22); the tripartite governor evidence does not turn on follower scatter."
- adverses: "battery-split-92-adjudication.md states 'no other repeated follower pair' — amend the line in place (editorial, not a new battery)."
- bars: "resolve iff battery-split-92-adjudication.md's follower-scatter statement matches the re-derived census above; check that no battery-level inference leaned on 'only 64 x2'."
