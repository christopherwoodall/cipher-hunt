# Next-token findings: followers of 17="fois" (15 windows)

Beat: all 17-windows, clustered by follower pattern first. Stream: repaired 1,847-pair parse.

## The 15 windows (idx | left3 | 17 | right3)
- @17: 45 91 53 | 17 | 64 98 82 ("…fois qui 98 m…")
- @238: 70 98 41 | 17 | 11 26 12 ("…fois la 26 [12]…")
- @308: 02 88 20 | 17 | 46 84 24 ("[20] fois que 84 24…")
- @369: 49 61 70 | 17 | 06 21 65 ("…pre fois 06…" — ANOMALY, sole "pre+fois" junction)
- @452: 32 48 79 | 17 | 77 60 65 ("toutefois le 60 65…")
- @556: 86 59 34 | 17 | 86 94 59 ("…86…" echo both sides)
- @837: 59 35 56 | 17 | 98 20 62 ("…fois 98 20 62")
- @880: 77 86 78 | 17 | 08 31 79 ("…fois 08 [VERBAL] 79…")
- @925: 08 65 71 | 17 | 61 96 48 ("…fois 61 par 48")
- @1040: 34 29 40 | 17 | 77 82 63 ("la première fois le m[63] la…")
- @1157: 92 29 80 | 17 | 77 82 44 ("…fois le m[44] 83…")
- @1289: 68 00 11 | 17 | 84 59 35 ("la fois 84 est 35…")
- @1461: 86 66 79 | 17 | 01 21 62 ("toutefois 01 21 62…")
- @1558: 93 61 40 | 17 | 11 26 30 ("…fois la 26 [30]…")
- @1757: 24 85 58 | 17 | 78 41 15 ("…fois 78…")

Structural note: the crib "la première" occurs twice (@754, @1034) but only @1034 is followed by 17. @754 goes "la première **20** 62 94" — feeds P3.

## P1 (HIGH). The absolute construction: "[une] fois le/la [NOUN] [PARTICIPLE]"
Two clusters, one frame:
- **Cluster B** "17 11 26 [12/30]" ×2 (@238→12, @1558→30). Globally "26 12"×4 + "26 30"×3 = **7-window 12~30 same-slot pair** — homophone battery input, ready-made.
- **Cluster A** "17 77 82 [44/63]" ×2 (@1040→63, @1157→44). **Frozen trigram**: "77 82" occurs exactly 2×, both as "17 77 82" — never without "fois".
- 44~63 share **5 followers** {00,29,77,74,11} (44→00×3, 63→00×3); both sit in the "le m" slot. Same-class, permutation-test-ready (cf. the 20~17 split method).
- 82's "m"+44 and "m"+63 junctions are **hapaxes** (82 never otherwise precedes 44/63) → 44/63 are independent words, NOT word-continuations. Kills the "m+44=moment" one-word reading.
- Reading: "une fois la [dépêche] reçue", "une fois le [moment] venu" — the absolute construction, peak diplomatic French. 12/30 and 44/63 = participles/adjectives in the predicate slot.
- The "le m[44/63]" sub-question: leading hypothesis "le même [44/63]" ("the same [noun]") — fits "44 est"×2 (@527, @1714) and the shared noun-like distribution. **Caveat**: requires 82="même" as a word vs pencil "m" as a letter — polyvalence tension, red-team call, do not assume. Alternatives: sentence boundary ("…fois. Le m…"), "M. [surname]" (no polyvalence, but "le M." unidiomatic).
- Testable: (1) 12~30 homophone battery; (2) 44~63 same-class battery; (3) 26's noun frames; (4) hunt the "une" — "98 41"@238 / "61 40"@1558 leftovers ("u-ne" split?).

## P2 (MEDIUM-HIGH). "20 62 94" trigram ×3 — the 20-paradox sharpens
- @760 "la première 20 62 94", @839 "fois 98 20 62 94", @1703 "…30 20 62 94". (4th "20 62" @1135 →98.)
- 20 across 15 windows sits in **determiner slot** (@307 "88 20 fois") AND **noun slot** (@760 "la première 20", feminine). The paradox is now two clean minimal pairs, not a hunch.
- Cross-cutting: feeds the 20-paradox work order. My windows add @839 ("fois 98 20") and the trigram's positional stability.

## P3 (MEDIUM). "toutefois" followers: 60 = masculine noun, 01 = subject pronoun
- @452: "toutefois, le [60] [65]…" — 60 hapax after "le"; test noun frames ("un 60", "du 60").
- @1461: "toutefois, [01] [21] [62]…" — **01→24 ("il/on en") ×3** → subject pronoun ("il"/"on"). Test 01's subject frames ("que 01", "01 [verb]").

## P4 (MEDIUM). @308 — the only "fois que" in the stream
- "17 46" occurs exactly 1×: "[20] fois que 84 [24] [37]".
- If 24="en" (from "en cela"): "…fois que [84] en [37-verb]" — clitic chain ("les fois qu'on en [parle]"). Unlocks if 24="en" confirms. 84's pronoun profile already with the que/ce battery.

## P5 (MEDIUM-LOW). @925 "…71 fois 61 par 48"
- "61 96" ×2 (other @223: "61 par ce que"!). 61 = word taking "par"-phrases (participle? "frappé/instruit par").
- "96 48" is a **hapax** → "par ailleurs/conséquent" downgraded to weak. Null-leaning; 61's contact profile is the testable residue.

## P6 (FLAG/ANOMALY). @369 "49 61 pre(70) fois 06…" — do not force
- Sole "70 17" junction in 70's whole distribution ("pre" otherwise continues words: 12×3, 82×2, 39×2…).
- Tantalizing near-miss: "parfois"/"quelquefois" ("sometimes") fits the meaning slot perfectly ("…[61] parfois [verb-ent]…"), but 70="pre" ≠ "parf".
- Three options, ranked: (a) undiscovered idiom with "pre…fois" boundary; (b) 70-polyvalence (AGAINST lane law — red-team call only); (c) nearby cell misassignment. Battery: test (a) via "49 61" frame search; escalate (b) to red team, do not assume.

## P7 (LOW). Relativizer frames: @17 "…53 fois qui 98…" / @880 "…fois 08 [VERBAL] 79…"
- Both are "fois + relativizer + verb". 98: →82×3, →20×2 — verb candidate. 08: "que"/pronoun candidate before 31=VERBAL.
- @880's "08 31 79": if 08=subject ("il/on"), "[il] [verb] tout" — "…fois qu'il [verb] tout…". Test 08's subject-slot distribution.

## P8 (LOW). @1757 "en(24?) 85 58 fois 78…"
- "en … fois" frame ("en deux fois", "en plusieurs fois") — weak support for 24="en". 78 = ver/er fork; thin.

## Honest nulls
- @556's "86…86" echo: no fois-reading forced. (Cross-cutting: "00 86"×12 — "pour [86]" with "00 86 56"×4 / "00 86 29"×2 — 86 = verb stem, upgrades 00="pour" toward promotion. Not my beat; handing off.)
- @837 "fois 98 20 62": folds into P2 (trigram) + P7 (98-verb).
- @1289 "la fois 84 est": 84 already with the que/ce battery; no independent fois-prediction.

## Battery queue (ranked)
1. 12~30 homophone battery (7 windows: "26 12"×4, "26 30"×3) — permutation test on successor distributions.
2. 44~63 same-class battery (5 shared followers; "44 est"×2 as noun evidence).
3. 26 noun-frame battery ("la 26" exclusive to "fois la 26" — frozen trigram).
4. "le même [44/63]" vs boundary vs "M." — adjudicate after (2); 82-polyvalence question to red team.
5. 01 pronoun battery ("01 24"×3 = "il/on en").
6. 60 noun battery ("toutefois, le [60]").
7. @369 anomaly: "49 61" frame search; 70-polyvalence escalation to red team.
8. 20-paradox feed: @839 + trigram stability to the 20 work order.
