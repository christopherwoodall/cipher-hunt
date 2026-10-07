# Round-5 MORPHOLOGIST: 47="ce" battery, 06 stem ID, 06/86 distribution

Executor: morphologist (round 5). Canonical: repaired parse, 1,847 pairs
(`code/side-keyhunt/repaired_offsets.json`). Era: Tocqueville word-space ONLY (F30).
Code: `code/crowd5/morph47_06.py`. Numbers: `code/crowd5/morph47_06_results.json`.
Mid-round inputs folded in: Closer A2 (87/47 homology bound, `code/crowd5/closer87_angles.json`);
overwatch memo (`code/crossfleet/memo-round5-briefing.md`: petit-chiffre word-family
packing → 06/86 as stem allomorphs; 1690 royal order on mandated homophones; no nulls).

## WO1 — 47="ce" promotion battery → verdict: LEAD (strengthened), NOT promoted

### Repaired-parse legs (all re-derived)
| leg | cipher | era | ratio |
|---|---|---|---|
| B1 "ce que" 47→46 | 3/28 = 0.1071, Wilson 95% [0.037, 0.272] | P(que\|ce) = 0.1076 | **0.996×** |
| B2 "cela" 47→11 | ×3 | — | — |
| C1 "par ce" P(96\|47) | 1/28 = 0.0357 | P(ce\|par) = 0.0125 | 2.85× |
| A unigram (naive) | 28/1847 = 0.01516 | P("ce") = 0.00528 | 2.87× |

### New independent check 1 — Q2 fragment conditioning (F33-grade, positional instrument)
All 28 frames classified. **Fragment reading iff suc==78 or pre==29**: covers 9/9
fragment frames (suc==78 ×5 with pre∈{76×3, 74×2}; pre==29 ×4 with suc∈{33×2, 14, 08});
**0/6** ce-frames show fragment features; **0/9** fragment-frames show ce-features
(suc∈{46,11}, pre==96). Clean partition, zero cross-contamination — F33-form
(positional conditioning, falsifiable: one cross-contaminated frame breaks it).
The 1690 royal order (mandated sparse homophones on frequent syllables) is the
historical prior for exactly this kind of conditioned double. Fragment sound
unidentified ("même"-fragment survives from N29 as the only named candidate;
"même" as uniform word is dead: B1 5.8×, C1 kill).

### New independent check 2 — Q1 qui/que complementarity (folds in Closer A2)
A2's bound: P(64|47)=0/28 vs era P(qui|ce)=0.188, binom p=0.0030. Verified on the
repaired parse, sharpened:
- 47→64 = **0/28** (binom p=0.0029 vs era; p=0.0086 vs cipher P(64|87)=5/32).
- 87→64 = 5/32 (pres: 24×3 ["en ce qui" if 24="en"], 29×1 [the @148 jar], 79×1).
- Relative "ce que": 47→46 with pre≠96 ×2 (@548 pre=24, @864 pre=48); **87→relative-que = 0/32**.
- Fused "parce que" (pre=96) takes either cell: 87×3 (@225/@953/@1527), 47×1 (@151).
- "cela" takes either: 87→11 ×7, 47→11 ×3. "c'est" (A1) takes either: 87→01 ×2, 47→01 ×1.
- Fisher exact for the qui/rel-que split (table [87: 5, 0; 47: 0, 2]): **p=0.0476**.

**Rule Q1 (F33-style, falsifiable):** the relative-pronoun complement after "ce" is
cell-conditioned — 87 before "qui" (5/5), 47 before relative "que" (2/2); fused
"parce que"/"cela"/"c'est" are homophonic overlap (2 groups→1 sound = the F33-allowed
direction, not the falsifier). Falsifiers: one 47→64; one 87→46 with pre≠96.
Mechanism unfenced (candidate: "ce qui"/"en ce qui" as 87's table-level formula unit).

### C2 explained (the "..er→ce" 12.6×)
1. **Rate dissolved (methodological):** the 12.6× conditioned on cipher cell 29="er"
   mapped to era "words ending in er" — F30-void per N22 (29 is a hyper-frequent
   by-ear cell, 182× over era; er-rate instrument uncalibrated). Same class as the
   red team's N22 self-kill.
2. **Cipher-side bounded:** the 4 frames (@22/@422/@1230/@1590, repaired 29-positions)
   are exactly Q2's pre==29 fragment context (two sub-patterns: "48/43 er [frag] 33" ×2,
   "36/48 er [frag] 14/08" ×2).
3. **Cross-allophone (new):** the phenomenon is "ce"-level, not 47-level — 29→87 ×3
   as well (@147 the jar, @627, @1425). Both "ce" cells show it, as conditioned
   polyvalence predicts.

### Unigram addressed
The naive 2.87× is miscalibrated (pair-rate vs word-rate). Elision-corrected
(era "c'est" counted under U['c']=395, cipher writes the ce-cell): 47 = **4.11×**;
ce-proper (19/28, fragment frames removed) = **2.79×**. Residual = register +
polyvalence (no diplomatic corpus in lane to close it; the Meisel 1826 corpus from
F15 is not in `data/`). Rival ranking unaffected (same 1.93 factor for all).

### Rival battery (16 candidates, repaired parse, F30-legal legs A/B1/B2/C1)
"ce" uniquely survives. Killed on B1 (era P(que|w)=0 with era_n>50): se, le, les,
ne, me, tout, y, dans, bien. Out-of-band: en (B1 145×), de (979×), on (28×),
il (100×), même (B1 5.8× + C1 kill), plus (B1 5.4×, C1 37×).

### Blockers for promotion (why LEAD, not provisional)
1. **The @148–152 64-slot residual is unresolved** (explicit WO requirement).
   Window @147–156: `29 87(ce) 64(qui) 96(par) 47(ce) 46(que) 66 84 26 35`.
   Era attestation: "ce qui par ce que" = 0, "ce qui parce que" = 0,
   "ce même parce que" = 0, "ce qui par" = 0 (Tocqueville, word-space).
   Three live alternatives: (a) parenthetical verb downstream
   ("ce qui, par ce que 66 84, [V]" — "94(ne) 24" @161–163 is a verb slot, but
   "52 94 24" order is wrong for "ne…pas"); (b) 96 = conditioned verb stem in the
   "ce qui __ ce que" frame ("ce qui [verb] ce que" is grammatical — the context
   miner independently flagged this window: "wants a verb, not par/de", F19);
   (c) 64/47 fragment substitution here. Best next step: 96 conditioned-verb battery.
2. Q1's mechanism unfenced; fragment sound unidentified; unigram residual open.

Net: the best-supported LEAD in the lane (7 legs, two new F33-grade conditions),
but the WO's explicit bar (resolve the 64-slot) is not met. **Do not promote.**

## WO2 — identify the 06 stem → verdict: NULL (not identified)

### Frames verified (repaired parse)
06→29 ×4 @[1096, 1388, 1709, 1815] (curator's correction holds: old @760 was the
a5_03 off-phase artifact). Wide contexts in JSON.
86→29 ×4 @[431, 1375, 1391, 1825]; @1391 overlaps @1388
("82 16 06 29 67 86 29" 5-gram) → **7 independent infinitive events**.
Formula "06 29 67 86" ×2 @[1096, 1388].

### 67 fork (right neighbor in 2/4 frames; "veut" is provisional)
Era P(w | prev = -er infinitive): **et 0.02851 (n=113)** vs veut 0.00025 (n=1) —
**114:1**. Cipher-side: "06 et"✓/"06 veut"✗ (no subject); "et qui"✓/"veut qui"✗
(67→64 ×2); but "veut me"✓/"et me"✗ (67→78 ×4 @351/@491/@1163/@1842) and
"21 veut [inf]"✓/"21 et [inf]"✗ (@1457 "21 67 86"). → conditioned-polyvalence
hypothesis for 67 (et after verb-stems/infinitives; veut before 78/with subject-21),
8/38 classified, **unpromoted** — needs a full 67 battery (round-6 work).

### The rate kills
- Single-stem-for-all-06: **KILLED**. 44 tokens / ~957 words = 46.0/1000w vs best
  era -er stem "pri*" 2.685/1000w = **17× gap**.
- One-stem-in-7-events (memo's allomorph framing): no Tocqueville -er infinitive
  reaches the needed rate (best "donner", expected 957×82/214861 = **0.37** vs 7
  observed = **19×**) → the infinitive is a diplomatic-register verb,
  Tocqueville-blind. Conditional-best (one-stem ∧ 16="en" ∧ 00="pour" ∧ 77="le" ∧
  12="de" ∧ 67="et"): **"donner"** — the only candidate taking all four governors
  in era (le:1, pour:1, de:15, en:1) — but needs 19× register inflation: UNVERIFIED.
- Allomorph rate tension (T1): (44+32)/957 = **79.4/1000w** for the stem family vs
  ~40/1000w max for any French verb → the pure one-stem-allomorph reading is
  challenged (class cells with slot-conditioning stay live).
- Self-coordination tension (T2): @1388 "82 16 06 29 67 86 29" = "[inf-A] et [inf-B]"
  with A=B under one-stem ("donner et donner" — odd).
- @1709 "manière"-rival: cut-consistent with the crib ("première" → i|er|e, so
  "manière" → man(i)|er|e), but requires 06="man" (unattested elsewhere) → fenced/disfavored.

**Verdict: NULL.** The stem is not identified; the frames constrain it to a
diplomatic-register -er infinitive invisible to Tocqueville. "donner"/"prier"
lead conditionally, both unverified.

## WO3 — 06/86 complementary distribution → verdict: RULE M1 ACCEPTED (F33-grade)

### Holds on the repaired parse
00→86 ×12 vs 00→06 ×0. 06's finite frames: 06→11 ×4, 06→77 ×6, 06→00 ×4.
86 in 06's slots: 86→11/77/00 = **0/0/0**. 86→29 ×4 (shared infinitive slot).
The single 86→06 @889 ("00 86 06 77") fenced as clause-boundary (00 86 | 06 77).

### M1 (allomorph framing, memo-directed)
Petit-chiffre word-family packing → 06/86 as **stem allomorphs** (same stem,
mood-conditioned: 06 = finite/imperative, 86 = infinitive-complement), adopted as
the working interpretation (historical prior for F33's 4th conditioned case):
> After governor 00, the verb-stem cell is 86 (12/12 stem-takes), never 06 (0/55).
> In finite/imperative frames (stem→11 ×4, stem→77 ×6, stem→00 ×4) the stem cell
> is 06, never 86 (0/14). The →29 infinitive slot is shared (06→29 ×4, 86→29 ×4;
> allomorph conditioning there unfenced).
> Falsifiers: one 00→06; one 86→{11,77,00}; one 06 with pre=00.

### Significance
- 00→86 enrichment: P(pre=00|86) = 12/32 = 0.375 vs baseline 55/1847 = 0.0298 →
  **12.6×, binomial P(≥12/32) = 6.3e-11**.
- Asymmetry (00 selects 86 over 06 | stem-take): Fisher exact **p = 7.3e-06**
  (table [00: 0, 12; ¬00: 44, 20]).
- Honest caveat: 00→06 = 0/55 alone is n.s. (expected 1.35 under baseline); the
  joint (enrichment + asymmetry) carries the claim.
- Post-"er" neighbors disjoint ({67,40,37} vs {82,89}) but n=4+4: non-probative,
  noted.

### Leads & compliance
- **00="pour" lead** (out of scope, needs its own battery): explains 00→86
  ("pour [inf]" ✓), 00→46 ×4 ("pour que" ✓), 06→00 ("[V] pour [inf/que]" ✓ —
  @544 "42 06 00 46" = "[V] pour que" ✓ grammatical). Closer refuted 00's
  "de/a/le", not "pour".
- **No nulls posited** in any reading (petit-chiffre reference has none; lane's
  null-digit negative stands).

## Best next steps (ranked)
1. **96 conditioned-verb battery** in the "ce qui __ ce que" frame → resolves the
   @148–152 residual blocking 47="ce" promotion (context miner's independent flag).
2. **Full 67 classification** (38 occurrences) → promote/kill the et/veut
   conditioned polyvalence; gates WO2's right-context.
3. **00="pour" battery** (unigram, "pour que" ×4, "pour [inf]" ×12, "pour la" ×4).
4. **Diplomatic-register corpus** (Meisel 1826 from F15 is not in `data/`) → closes
   the "ce" unigram and infinitive rate residuals honestly.
5. **16="en" test** → unlocks "m'en [inf]" frames (@1388/@1391/@431) for WO2.
6. **21="me" re-check**: 96→21 ×3 ("par 21") vs N29's "par me" era-n=0 hardening —
   adverse for the open 21="me" lead (flagged, out of scope).
