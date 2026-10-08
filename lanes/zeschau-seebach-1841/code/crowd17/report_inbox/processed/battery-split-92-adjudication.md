# Battery report: split-92-adjudication — evidence package for red-team adjudication of 92's tripartite governor profile

- Target: `split-92-adjudication` (claim: "red team adjudicates 92's tripartite governor profile: split/polyvalence declaration vs governor misread")
- Worker: subagent 45849a5b-6b7d-4552-b0bd-ec640703c717
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`; canonical.py NOT used, R5005 NOT touched)
- Lock: `code/crowd17/next-token/locks/split-92-adjudication.lock` (created 2026-10-08T11:51:00Z; no prior/stale lock on this target)

## Bar (verbatim, pre-registered before testing)

"red-team adjudication only — battery may gather windows, never decide the split"

Restated as numbered pass/fail clauses:

- **C1**: re-derive the tripartite window table on the repaired stream — governor census, the four governor groups, and the hinge windows (@1154 stem, @1022 residual, @1550 prenne-clause) — independently of battery-class-92.md.
- **C2**: confirm/fence @1022: either it parses under a candidate class, or it is fenced as anomalous under all classes with the byte-level window stated.
- **C3**: gather coordination evidence for queued prenne-92-noun without duplicating its bar (noun-value arm belongs to that target; this battery tests nothing about 92's value).
- **C4**: decide nothing. No class named, no split declared, no polyvalence assigned — §7 sole-polyvalence (67 et/veut) blocks any battery-level split decision. Package evidence for red-team adjudication only; contradict no standing verdict (A14 set-level INF-signal, A6 '-ère' value kill, 09~92 HOLD).

## Method

Loaded the repaired stream per repair_parse.py (1,847 pairs asserted; offsets independent re-read, not copied from the class-92 report). Located all 92 tokens by stream scan, dumped predecessor/follower windows for each, and ran a global contact census (00→92, 11→92, 84→92, 94→92, 92→64). Every offset below is a repaired-stream @-offset; every count is a re-derived number.

## Window-level evidence (@-offsets) — re-derived

**Global census (re-derived, not inherited):** n(92) = 22 at @49, @66, @203, @321, @330, @354, @356, @593, @683, @901, @978, @1022, @1154, @1218, @1310, @1361, @1379, @1453, @1490, @1550, @1607, @1673 — the same 22 offsets as battery-class-92.md. Governor census re-derived: 00→92 x6 (@49, @330, @593, @978, @683, @1154), 11→92 x3 (@203, @321, @1607), 84→92 x2 (@1022, @1379), 94→92 x2 (@66, @1550), singletons 40 (@354), 98 (@356), 16 (@901), 83 (@1218), 30 (@1310), 13 (@1361), 46 (@1453), 31 (@1490), 81 (@1673). Counts sum to 22. Followers: five repeated 2x clusters — 92→79 (@49, @593), 92→69 (@66, @1379), 92→60 (@321, @1673), 92→64 ('qui', @683 + @1022), 92→62 (@1361, @1453); all other followers x1. Scatter still neutral (max 2/22). [AMENDED 2026-10-08, supervisor: original stated '92→64 x2 only' — factually wrong; the neutral-scatter inference did not lean on the single-pair claim and stands.]

**Group 1 — {00x6} → verbal (00='pour', A9 granted):**
- @1154: `02 00 92 29 80` = "pour [92]er ..." — 92 takes the -er infinitive ending directly (A10 compositional stem). Verdict-grade forcing window for the verbal reading at THIS locus; "pour [N]er" impossible. This is the single strongest window in the profile.
- @683: `00 92 64 29 40 65` = the A6 frame ([09/92]-qui-er-e-65), predecessor 00 here (07 before it). Fenced per A6: value killed, never re-litigated; class-parse marginal under every candidate.
- @49/@330/@593/@978: `00 92 79` x2 (@49, @593), `00 92 50` (@330), `00 92 07` (@978) — 'pour [92]' frames, verbal class cleanest (INF/whole/stem); "pour"+finite-verb ruled out.

**Group 2 — {11x3} → nominal-or-clitic+verb (11='la', banked):**
- @203: `87 11 92 63`, @321: `06 11 92 60`, @1607: `39 11 92 65`. Article+'la [92] [X]': grammatical as article+noun/adjective or object-clitic+finite-verb ("la [V]"); ungrammatical as article+whole-word-infinitive (substantivized infinitive is masculine). 3 windows, all consistent with nominal, none consistent with whole-word INF.

**Group 3 — {84x2} → finite-verbal (84='on', A15 unconditioned per collision-62-84 battery 2026-10-08):**
- @1379: `89 84 92 69` = "[89] on [92] [69]" — clean under VFIN/clitic; "on"+noun ungrammatical (84 holds unconditioned).
- @1022: `53 84 92 64 45 64 96` = "[53] on [92] qui ce qui [96]..." — see C2 fencing below.

**Group 4 — {@1550} → nominal-subject (prenne clause):**
- Byte-level context re-derived: `@1545:00 @1546:46 @1547:70 @1548:12 @1549:94 @1550:92 @1551:45` = "pour que prenne [92] ce..." — the full "prenne" (70-12-94) stands immediately before 92, and @1545=00 ('pour') opens the clause: "pour que prenne [92]". @1549's 94 is word-internal to "prenne" (verified: 1547=70, 1548=12, 1549=94), so the '94→92 closed set x2' is corrected as class-92 stated — only @65-66 is a true ne-governor.
- @66 re-derived: `08 34 29 40 12 94 92` = "[08] i er e n ne [92]" — 'ne [92]' parses as ne-explétif/literary under VERB, ungrammatical under NOUN. This is the only true 'ne'-governed 92.
- @1550's two candidate parses (both recorded, neither decided): (a) inverted postposed subject — "pour que prenne [92-S]" (literary inversion pattern "que vienne le jour"); (b) direct object — "pour que [S] prenne 92" with the subject slot still open. Parse (a) is the class-92 battery's recommendation; parse (b) is prenne-92-noun's standing bar framing. Both are live; choosing is the red team's act.

**Singletons (re-derived predecessor/follower):** @354 `40 92 98` (40='e' banked letter — segmentation open, fenced for a segmentation battery, not counted as contradiction); @356 `98 92 47`; @901 `16 92 67`; @1218 `83 92 61` (83 fenced blocker per le83-window battery); @1310 `30 92 44` ("pas [92]", parses under ADJ, strained elsewhere); @1361 `13 92 62`; @1453 `46 92 62` ("que [92]" — clean under V-subjunctive); @1490 `31 92 39`; @1673 `81 92 60` (81's noun-81 lead open). None contradicts the tripartite picture; none resolves it.

## C2 — @1022 fenced as residual

`@1022: 53 84 92 64 45 64 96` — "on [92] qui ce qui [96]". Under NOUN: "on"+noun ungrammatical at the governor. Under VFIN: "[92-verb] qui" ungrammatical as a direct verb+relative sequence; "on [92-clitic]" leaves 'qui ce qui' unparseable. Under whole-word INF: 'on'+infinitive ungrammatical. Under ADJ: 'on'+adjective ungrammatical. Anomalous under ALL classes — confirmed independently on the repaired stream. Fenced as residual **R-class92-1022**; red-team eyes. (Note: '92 qui' is also the @683 follower pair, but @683's anomaly is fenced under A6, not re-litigated.)

## Coordination output for queued prenne-92-noun (no bar duplication)

- prenne-92-noun tests 92's noun-value arm and carries the 'la 92' x3 + '92 qui' x2 feminine-noun lead; this battery tested NOTHING about 92's value — no duplication. Its window @1550 is byte-verified as "pour que prenne [92] ce" with 94 word-internal to "prenne"; the inverted-subject vs direct-object framing choice is handed to the red team intact, with both readings recorded above. The '94 92' closed-set correction (only @65-66 a true ne-governor) is confirmed byte-level.
- Coordination note for prenne-92-noun's runner: @1154 ("pour [92]er" — verbal forcing) and the 'on 92' x2 group remain this battery's documented adverses for any noun arm; do not re-derive them, they are fenced here.

## Standing constraints observed

Did not touch R5005, sealed gate instances, or the red-team adjudication queue. Nothing promoted, killed, split, or re-valued by this battery. The killed '-ère' value was NOT re-litigated (@683 fenced under A6). No numbers invented: every offset and count traces to the repaired 1,847-pair stream. A14's set-level INF-signal, the 09~92 HOLD, and the §7 sole-polyvalence rule are untouched — and they are consistent with this evidence (92 rides the set per A14: "92 weakest (genuinely ambiguous)"). No contradiction with any standing red-team verdict; nothing to downgrade.

## Per-clause results

| clause | result |
|---|---|
| C1 — table re-derived | **PASS** — 22 windows, 4 governor groups, all census counts match class-92.md independently |
| C2 — @1022 confirmed/fenced | **PASS** — anomalous under all classes; fenced R-class92-1022 |
| C3 — prenne-92-noun coordination, no duplication | **PASS** — noun-value arm untouched; @1550 bytes verified, both parses handed over |
| C4 — decide nothing | **PASS** — no class named, no split declared, no polyvalence assigned; split/polyvalence-vs-misread question is entirely the red team's |

## Verdict: NULL (evidence-package null, per bars)

The bar is red-team-adjudication-only, so this battery cannot return promote or kill: the question — split vs second polyvalence declaration vs governor misread — is undecidable at battery level under §7. The tripartite profile is real on the repaired stream, independently verified.

## Follow-up for the supervisor (null regeneration)

### F1 — id "split-92-redteam-evidence" (priority 1)
- claim: "red team adjudicates 92's tripartite governor profile: split / second-polyvalence declaration / governor misread, on the re-derived evidence package (this report)"
- evidence: "re-derived 22-window table on the repaired stream: {00x6}->verbal with @1154 'pour [92]er' stem forcing (smoking gun); {11x3}->nominal-or-clitic; {84x2}->finite-verbal (84='on' unconditioned per collision battery); {@1550}->'pour que prenne [92]' nominal (inverted-subject vs direct-object both live); @1022 fenced residual R-class92-1022 (anomalous under all classes); '94 92' closed set corrected (@1549's 94 word-internal to 'prenne'; only @65-66 a true ne-governor); @683 fenced under A6. §7 sole-polyvalence (67) blocks battery-level split declaration — this is why the evidence comes to the red team. A14 set-level INF-signal and 09~92 HOLD untouched."
- adverses: "A14 set-level INF-signal (92 'genuinely ambiguous', rides the set — consistent, not contradictory); 92's killed '-ère' value stays killed (NOT re-litigated); prenne-92-noun (noun-value arm, coordinate — do not duplicate)."
- bars: "red-team adjudication only — declare 92 split/polyvalent/misread or return with a discriminating-frame commission; the battery record holds all four live readings with byte offsets."
