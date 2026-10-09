# Battery report: contre-00-global-census

- Target id: `contre-00-global-census`
- Claim: "A full 55-window census under 00='contre' decides whether a global promote stands ('contre que' x4 and 'contre [33]' x8 as kill legs) or the claim fences to the '96 00' positional reading."
- Date: 2026-10-09
- Worker: battery worker (subagent 1e547d44-d65d-4b23-962f-888ea54ee71c)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). All @-offsets are 0-based repaired-stream indices. n(00) = 55 (verified byte-exact in-session).
- Lock: code/crowd17/next-token/locks/contre-00-global-census.lock (created at start, deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"Full 55-window census under 00='contre'; 'contre que' x4 and 'contre [33]' x8 as the kill legs; promote global iff zero hard contradictions, else fence to the '96 00' positional reading."

Numbered pass/fail clauses (restated before testing, not modified after):

1. Census all 55 windows of 00 under the value 'contre'; classify each window as grammatical, conditional, or hard contradiction.
2. 'Contre que' x4: each of the four 00->46 windows must be shown grammatical or contradiction-grade under banked 46='que'.
3. 'Contre [33]' x8: evaluate the eight 00->33 windows as kill legs (conditional on 33's open value — see adverse).
4. Promote the global 00='contre' value iff zero hard contradictions across all 55 windows; else fence to the '96 00' positional reading. Do NOT downgrade the A9 00='pour' class-level grant in either case.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types; `canonical.py` never used). R5005 not touched.
2. Enumerated all 55 windows of 00 with ±4 context; predecessor and successor censuses.
3. Applied 1841 diplomatic French grammar: "contre" governs nouns, infinitives, and (in "par contre") functions as a post-par connective — it NEVER introduces a "que" clause.
4. Checked every kill leg byte-exactly; checked the '96 00' positional windows for grammaticality under "par contre".

## Window-level evidence

### Kill legs: 'contre que' (00 -> 46, banked GT 46='que') x4 — ALL FOUR HARD CONTRADICTIONS

- W1 @106 (row a1_03): `93 59 45 28 00 46 11 21 67` = "[93] est(59) ce(45) [28] contre que la(11) [21] [67]". "Contre" cannot introduce a "que" clause in French. Kill grade.
- W2 @545 (row a3_01): `29 48 42 06 00 46 24 47 46` = "er(29) [48] [42] [06] contre que [24-verb] ce(47) que(46)". Same failure. Kill grade.
- W3 @1545 (row a8_00): `88 77 78 43 00 46 70 12 94` = "[88] le(77) [78] [43] contre que pre(70) n(12) ne(94)". Same failure. Kill grade.
- W4 @1680 (row a8_05): `39 74 77 44 00 46 79 65 13` = "[39] [74] le(77) [44] contre que tout(79) [65] [13]". Same failure. Kill grade.

No rescue available: "contre" has no "contre que" construction in any register of 1841 French; no alternative parse licenses a preposition before a "que" clause. Four independent rows (a1_03, a3_01, a8_00, a8_05).

### Supporting kill leg: 'contre' + finite verb

- @1138 (row a6_08): `86 20 62 98 00 98 78 62 16` = "[86] [20] [62] vient(98) contre vient(98)". 98 is promoted finite-verb class (prof-98 PROMOTE, vient-98-name battery-promote). "Contre" + finite verb is ungrammatical. Fifth hard contradiction (battery-grade).

### 'Contre [33]' x8 — NOT kill-grade, conditional (adverse answered)

@185, @407, @466, @845, @935, @1087, @1244, @1629. Per the adverse, 33 has a penser/pens- segmentation duality and its value/class is red-team's call. "Contre" + [33] is grammatical iff 33 is noun/infinitive-shaped — untestable at battery grade without 33's class. These are fenced as conditional, not contradictions.

### Grammatical windows under 'contre' (partial census — successor set)

- 00 -> 86 x12 ("contre [INF]", 86 INF-class): grammatical.
- 00 -> 66 x7 ("contre [INF]", 66 infinitive-shaped): grammatical.
- 00 -> 92 x6 ("contre [92-verb]", 92 verb class): grammatical.
- 00 -> 11 x4 ("contre la..."): grammatical.
- 00 -> 97 x4: conditional (97 value open).
- 00 -> 36 x3 ("contre [36-noun]", 36 ratified noun class R18): grammatical.
- 00 -> 34 x1, 00 -> 13 x1, 00 -> 20 x1, 00 -> 64 x1 ("contre qui"): conditional/grammatical.
- 00 -> 67 x1 (@1247, "contre et/veut"): conditional.
- 00 -> 44 x1 (@1602): conditional.
- Predecessor census: 00 is preceded by 11 x4, 06 x4, 16 x4, 63 x4, 96 x3, 81 x3, 28 x3, 43 x3, 26 x3, 98 x3, 44 x3, 09 x2, 19 x2, 02 x2, 33 x2, 48/93/14/07/46/01/68/24/03/97 x1. No predecessor forces a global value.

### The '96 00' positional windows x3 — "par contre" grammatical

- @48 (a1_01): `30 62 96 00 92 79 37` = "[30] [62] par(96) contre [92] tout(79) [37]". "Par contre [92-verb]" grammatical.
- @466 (a2_10): `59 42 96 00 33 79 80` = "[59] [42] par(96) contre [33] tout(79) [80]". Grammatical under 33 noun/infinitive shape.
- @961 (a6_00): `20 67 96 00 86 56 41` = "[20] [67] par(96) contre [86-INF]". Grammatical.

## Per-clause pass/fail

1. 55-window census: DONE (n(00)=55 verified; full predecessor/successor censuses above). PASS.
2. 'Contre que' x4: all four are hard contradictions under banked 46='que'. PASS (as kill legs).
3. 'Contre [33]' x8: evaluated — conditional only, not kill-grade (adverse answered: 33's class is red-team's call). PASS.
4. Global promote iff zero hard contradictions: FIVE hard contradictions found ("contre que" x4 + "contre [98-vient]" x1). Global 00='contre' promote is KILLED. The '96 00' positional reading ("par contre") is FENCED as a live conditional at the three byte-exact windows. The A9 00='pour' class-level grant is NOT downgraded.

## Verdict: KILL (of the global 00='contre' promote)

The global value claim is dead at kill grade: four byte-exact "contre que" windows force 00 != 'contre' globally under the banked 46='que' GT, with a fifth battery-grade contradiction at @1138 ("vient contre vient").

Per the adverse, the '96 00' positional ("par contre") is FENCED as a conditional reading at the three positional windows (@48, @466, @961) — it is NOT declared a polyvalence: per §7, 67 et/veut is the sole true polyvalence, and declaring a second is a red-team act. The fenced positional lead is packaged for the red team (par/pour anomaly docket).

## Adverses answered

1. "00='pour' is A9 class-level granted — real resistance": honored. The A9 grant is not downgraded; it remains the controlling global account ("pour que" x4 all grammatical under it).
2. "'contre [33]' x8 strained (33 has penser/pens- duality, red-team's call)": answered — treated as conditional, not kill legs.
3. "A positional (post-96) alternative would be a second polyvalence — red-team's act": answered — the positional is fenced, not declared.

## Caveats

- Canonicality caveat stands: all rows' upstream offsets are unvalidated except a5_03. The five contradictions hold on the canonical stream per protocol; a rival phase that dissolves a bigram would need its own constraint sweep (no such sweep is pending for a1_03, a3_01, a8_00, a8_05, a6_08).
- The fenced positional reading is conditional on 96='par' (promoted) and "par contre" being acceptable 1841 French (it is attested, though less frequent than later).

## Follow-ups

None required (verdict is kill, not null — the bar's fence branch is satisfied). Optional for the supervisor: a `par-contre-1841` corpus check (P4) confirming "par contre" attestation in 1841 diplomatic French would strengthen the fenced positional for the red team.

No standing red-team verdict is contradicted or downgraded. No battery verdict downgraded. R5005, sealed gates, and the red-team adjudication queue untouched. §7 intact.
