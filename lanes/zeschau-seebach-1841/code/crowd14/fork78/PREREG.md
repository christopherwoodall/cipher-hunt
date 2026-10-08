# PREREG — FORK-78 resolver (round 14, WO6)

Written 2026-10-07 BEFORE the position×frame contingency table is computed.
(Raw 78/76 window lists seen; no table computed yet.)

## Hypothesis

**H1 (positional polyvalence):** 78 = "ver" when word-INITIAL; 78 = "er" when
word-NON-INITIAL (medial/final). The work order states "er-FINAL"; the test
distinguishes INITIAL vs NON-INITIAL because zero word-final 78s are
identifiable a priori — the FINAL sub-claim is graded separately.

**H0-ver:** 78 = "ver" uniformly. **H0-er:** 78 = "er" uniformly.

## Position rules (neighbor-based, tiered by anchor strength)

- INITIAL: pre78 is a complete-word cell → the word containing 78 starts at 78.
  Tiers: {11=la, 46=que} GT; {87=ce, 64=qui, 96=par} provisional;
  {37=le} MEDIUM; {77} provisional-conditioned.
- FINAL: suc78 is a complete-word cell (same sets). Expected ~zero a priori.
- SOLO: both (excluded from the 2×2, reported).
- 5-mer special cases: @1181 → MEDIAL (gouv|er|ne|m|ent LEAD; 78 not
  word-initial under any live reading). @1352 → CONTESTED: R-c granted
  («le [78] ne ment pas» → solo word) vs killed R-b (→ medial). EXCLUDED from
  the primary table; sensitivity S1 only.
- UNCERTAIN: everything else. F107's 32 segments are checked first (expected
  zero coverage — verified in-script, not assumed).

## Frame rules (reading evidence, neighbor-based, independent of position tiers)

- ver-frame: pre78 ∈ {37, 11, 87} — "le/la/ce ver[…]", mirroring 76's
  "le ver[…]" @833/@892/@969 (F103). Caveat: 37="le" is MEDIUM, 87=ce prov.
- er-frame: suc78 = 94 — 94="ne" provisional-strong; the h3a er|ne boundary
  diagnostic (er|ne 52 tokens/22 types vs ver|ne zero genuine common words,
  Fisher p=3.2e-11).
- other: everything else.
- EXCLUDED from the fork table: the four 78-45 windows (@313/@573/@982/@1164)
  — contested third reading (78-45="même" LEAD, F50); they support neither
  fork-tine. Sensitivity S4 re-includes them adversarially.

## Primary table

Rows {INITIAL, NON-INITIAL} × cols {ver-frame, er-frame}.
H1 predicts diagonal concentration (INITIAL↔ver-frame, NON-INITIAL↔er-frame).
Fisher exact, one-sided, pre-registered bar **p < 0.05**.
Expected: underpowered (small n) — a directional check, not the sole leg.

## Sensitivity analyses (pre-registered)

- S1: @1352 included as INITIAL + er-frame.
- S2: GT-only position tier (pre ∈ {11, 46}).
- S3: drop pre=77 (prov-cond) INITIAL windows.
- S4: même-windows included as ver-frame (adversarial).

## Legs (fork needs ≥2 independent legs; the table is one)

- **Leg 1** — the contingency table above (cipher instrument).
- **Leg 2** — H0-er kill via GT-anchored initial frames: "la 78" @297/@1670
  (pre=11=la GT → 78 word-initial, certain). "la er" is ungrammatical —
  French lexicon has ~zero er-initial words (verified on nesselrode-v8
  in-script). Each is an independent contradiction of H0-er. Instrument:
  French grammar + GT anchor. Independent of Leg 1's provisional tiers.
- **Leg 3** — H0-ver vs the er|ne diagnostic: 78-94 ×2 (@1181, @1352). Under
  H0-ver these read "ver|ne" — zero genuine common words in French (h3a).
  Graded WEAK per h3a's own PREREG ("language stat ≠ encipherer cut; cannot
  kill a tine alone"). Instrument: era-corpus boundary survey. Independent
  of Legs 1–2.
- **Leg 4** — the 76 contrast (different cell, different data): 76's 21
  windows classified by the same position rules; er-frames counted
  (suc=94). H1 predicts: 76 INITIAL-or-uncertain only, zero FINAL, zero
  er-frames — the er-arm is licensed only non-initially, and 76 never
  occurs non-initially. Precedent: {52,59} positional-allophone split (F103).
  Banked constraint honored: 76 and 78 treated as separate cells throughout;
  NO 76↔78 homophone tie; no window merging.
- **Leg 5 (Frenchman, required)** — era-corpus phonotactics on
  code/side-period/corpus/nesselrode-v8.txt: (a) ver-initial vs ver-final
  token counts; (b) er-initial token count (~zero); (c) er|ne vs ver|ne
  boundary re-derivation (h3a cross-check); (d) ear-checks on
  @297/@1670/@1181/@1352. Instrument: lexicon/corpus + ear. Independent.

## Verdict rules

- **CONFIRMED:** both uniform alternatives contradicted (Legs 2+3) AND the
  table directionally perfect AND ≥2 independent legs AND Frenchman concurs
  AND the {76,78} tension addressed (Leg 4).
- **WEAKENED:** direction right but a leg fails or is missing, no contradiction.
- **KILLED:** table significantly anti-diagonal; or a word-initial 78-94;
  or 76 with FINAL/er-frame occurrences; or Frenchman veto.

## Verification

5 random 78 windows (seed 1407) re-derived byte-exact from the repaired
stream in-script.

## Standing inputs (not re-litigated)

94="ne" provisional-strong; 87=ce / 64=qui / 96=par provisional; 37="le"
MEDIUM; 77="le" provisional-conditioned; F103 {76,78} split; F70 @1351 R-c
granted; h3a er|ne diagnostic; F50 même-LEAD (fenced confound).
