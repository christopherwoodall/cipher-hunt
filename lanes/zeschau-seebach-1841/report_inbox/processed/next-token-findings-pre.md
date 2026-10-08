# Next-token findings: followers of 70="pre" (15 windows)

Beat: all 70 occurrences + 3 followers each, clustered by follower pattern first.
Stream: repaired 1,847-pair canonical parse. Method: French-first prediction, cipher-tested.

## Cluster inventory

| # | Pattern | Windows | Reading |
|---|---------|---------|---------|
| A | 70-82-34-29-40 | @755, @1035 (both pred 11) | "première" — the pencil crib itself, GT |
| B | 70-39-11 | @1067 (→44), @1604 (→92) | "pré-a-la" — see P4/P8 |
| C | 70-12-94 | @347 (→74), @1547 (→92) | "prenne" (subj.) — see P3 |
| D | 70-12-06 | @1119 (→14) | "prennent" (3pl) — see P3 |
| E | 70-98-41-17 | @235 | "première fois" — see P5 |
| F | 70-91-77-06 | @519 | "prévalent" — see P6 |
| G | 70-88-10-29 | @615 | "presser" — see P7 |
| H | 70-87-77-89 | @868 | "[X]pre" + "ce le [89]" — see P8 |
| I | 70-37-08-43 | @1300 | unresolved singleton |
| J | 70-52-39-83 | @1331 | unresolved singleton |
| K | 70-17-06-21 | @368 | anomaly — see P9 |
| L | 70-64-65-48 | @1586 | boundary "[X]pre" + "qui" — see P10 |

## Ranked predictions

### P1 (PROMOTE): 94="ne" — 6 independent frames
- 62-94 ×9: "[verb stem]-ne" (prenne/vienne/donne-shaped)
- 94-82 ×4: "ne m'" — @578, @1182, @1353 ("ne m'[verb]", object pronoun, 82="m" GT)
- 94-59 ×3: "n'est" — @558, @762, @1795 (ne+est elision, 59="est" provisional)
- 70-12-94 ×2: "prenne" (subjunctive, see P3)
- 12-48 ×5 (analytic "n"+"e") vs 94 (syllabic "ne") — dual spelling, same architecture as P5
- Converges with the qui finder's "ne-distributed 94/48 pair": 94="ne", 48="e". "qui est 32-94" = "qui est [adj], ne…" (clause boundary, ne…pas/ne…que); "qui est 32-48" = "qui est [adj]e" (feminine)
- Zero contradictions across 37 occurrences. **Recommend PROMOTE.**

### P2 (HIGH): 12="n" (letter) + 48="e" (letter) — cross-checked against GT letters
- 12-48 ×7 = "ne" (negation particle; explains 12's high frequency n=23)
- 82-48 ×4 = "me" (object pronoun; 82="m" GT) — independent confirmation of 48="e"
- 40-12 = "en" @64 (preposition; 40="e" GT) — independent confirmation of 12="n"
- 12-34 = "ni" (34="i" GT) — "ni" (neither/nor)
- 70-12-94 = "pre-n-ne" = "prenne"; 70-12-06 = "pre-n-ent" = "prennent"
- 48="e" is a homophone of 40="e" (expected in a homophonic table; cf. 29="er"/94="ne" analytic-vs-syllabic pairs)
- **Recommend PROMOTE for both** (each has ≥3 frames, two anchored on GT letters).

### P3 (HIGH): "prendre" forms — 70-12-94="prenne" ×2, 70-12-06="prennent" ×1
Falls out of P1+P2 compositionally:
- @1547: "00-46-70-12-94-92" = "pour que prenne [92]" — pour que + subjunctive, perfect French. (00="pour?" lead supported.)
- @347: "06-70-12-94-74" = "[ent?] prenne [74]" — same byte-identical trigram, subjunctive trigger leftward unresolved (01/87="ce" context).
- @1119: "88-70-12-06-14" = "[88] prennent [14]" — 3pl indicative. (If 88 ends the prior word; "apprennent" alternative if 88="ap" — 88="s" in P7 favors the boundary reading: "[noun]s prennent".)

### P4 (HIGH): 39="a/à" — 4 frames
- 64-39 = "qui a" (avoir; 64="qui" promoted)
- 59-39 ×2 = "est à" ("est à même/craindre"-shaped; 59 provisional)
- 03-39 ×3
- 70-39-11 ×2 = "pré-a-la" (see P8) — 11="la" banked
- Single value covers "a"/"à" (same sound; homophonic table expected to merge).

### P5 (MEDIUM-HIGH): 70-98-41-17="première fois" (@235) — word HIGH, cells MEDIUM
- "51-70-98-41-17-11" = "[51] première fois la [26]". "pre-?-?-fois" admits exactly one French word: "première". 51="une" fits ("une première fois") but 51 is n=6, single frame — LOW.
- 98-41 is a hapax bigram (only @236): 98-41="mière" (98="mi", 41="ère") — single-leg values, need more windows.
- **Architectural finding:** dual spelling of "première" — analytic 70-82-34-29-40 (pre-m-i-er-e, the crib ×2) vs syllabic 70-98-41 (pre-mi-ère, here). Same stem, two granularities. Expect this elsewhere (cf. 12-48="ne" analytic vs 94="ne" syllabic).

### P6 (MEDIUM): 70-91-77-06="prévalent" (@519) → 91="va"
- "09-pré-va-le-ent": "prévalent" (pré-va-lent, "lent"→"le"+"ent" per the table's analytic splitting; 06="ent" supported, 77="le" provisional).
- Cross-check: 91-11 ×2 = "va la" ("il va la…"-shaped). 91 n=21, plausible for "va" (aller 3sg) homophone cell.
- "prévalent" is solid diplomatic French ("l'opinion prévalente").

### P7 (MEDIUM): 70-88-10-29="presser" (@615) → 88="s", 10="s"
- "pre-s-s-er": 88="s" (letter), 10="s", 29="er" GT.
- 88 as word-final "s" fits its boundaries: 88-77 ×3 = "[noun]s le", 88-11 ×2 = "[noun]s la" (plural noun + article).
- Alternative: "présenter" (88="sen", 10="t"). Discriminator: does 88 pattern as letter-"s" (plural/article boundaries) or syllable-"sen"? Current evidence favors "s".
- Note: @1119's "88-70" then reads "[noun]s prennent" — consistent.

### P8 (MEDIUM): 70-39-11-44="préalable" (@1067) → 44="bl(e)"
- "pré-a-la-ble": 44="ble" word-final (nexts 00/59/74/83 = word boundaries).
- Cross-check: 77-44 ×2 (@207, @1678) = "le [bl-word]" ("le blâme/blesse"-shaped) — same cell word-initial. Positional flexibility is normal.
- Caveat: @1604's 70-39-11-**92** cannot be "préalable" — 92 patterns as a standalone noun (00-92 ×6 "pour [92]", 11-92 ×3 "la [92]"), not "ble". So "préalable" is claimed for @1067 only; @1604's 70-39-11 shares the "pré-a-la" trigram but its 92 needs independent resolution. The trigram identity (×2 byte-identical) vs divergent 4th groups is flagged, not forced.

### P9 (FLAG, do not force): @368 "61-70-17-06" = "[61]-pre-fois-ent"
- "pre-fois" with no "mière" between — anomalous. 17="fois" is solid (4 legs), so this is real, not a misread.
- Possible: word boundary ("[X]pre" + "fois"), encipherer elision, or 70 covering a non-prefix "pre". Null preferred over invention.

### P10 (LOW): @1586 "36-70-64-65-48" = "[36]-pre-qui-[65]-e"
- Boundary: word ending in "-pre" + "qui [65]e" (48="e" verbal ending; "qui [verb]e"-shaped). The "-pre" word unresolved ("propre"?). No prediction.

### P11 (LOW): @1300 "02-70-37-08-43", @1331 "94-70-52-39-83"
- Singletons, no cluster. @1331 has 94="ne" + 70 + 52-39("a")-83: "ne pre-[52]-a-[83]". @1300: "pre-[37]-…" with 37 the hot verb/adjective cell — worth re-examining once 37 resolves. No forced reading.

## Battery queue (priority order)
1. 94="ne" — PROMOTE battery (6 frames, zero contradictions)
2. 12="n" + 48="e" — PROMOTE battery (GT-letter cross-checks: "me", "en", "ni")
3. "prenne"/"prennent" — compositional verification of P1+P2 at @347/@1547/@1119
4. 39="a/à" — value battery (4 frames: "qui a", "est à", 03-39, "pré-a-la")
5. 98-41="mière" — needs more windows (hapax bigram; search for 98-41 elsewhere as lane grows)
6. 91="va" ("prévalent" + "va la" ×2)
7. 88="s"/10="s" ("presser" vs "présenter" discriminator)
8. 44="bl(e)" ("préalable"@1067 + "le blâme"@207/@1678); resolve @1604's 92 independently

## Nulls / non-findings
- No "premier" (masc.) spelled 70-82-34-29: masculine "premier" never uses the analytic spelling in-text; the syllabic candidate 70-12-94 resolved to "prenne", not "premier".
- 70 never takes 29 directly ("pre-er" unattested) — consistent with 29="er" being verb/noun-final, not prefixal.
- @368 anomaly recorded, not solved.
