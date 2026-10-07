# RED TEAM — Round 5 rulings

Date: 2026-10-07. Kill authority over every promotion.

## Docket status: EMPTY — NULL ROUND

No round-5 executor claims have landed. `code/crowd5/` and `report_inbox/`
contain no Frenchman, Morphologist, Bigram Closer, Closer, Segmenter, or
Inventorist outputs as of this review. **Zero rulings issued; zero promotions;
zero kills; net promotion count = 0.**

This file records (a) the armed baseline every future round-5 claim will be
judged against, and (b) the standing kill conditions per expected claim, so
that adjudication, when claims land, is mechanical and traceable.

## Armed baseline (recomputed against the repaired 1,847-pair stream)

`verify_baseline.py` builds the canonical stream from
`code/side-keyhunt/repair_parse.py` + `repaired_offsets.json` and re-derives
every load-bearing number named in the round-5 work orders. **29/29 checks
PASS** (canonical: 1,847 pairs, 96 distinct groups, "la première" @754/@1034).

Corrections the instrument forced on my own expectations (documented, not hidden):
- `47->64` — I had written want=2 from memory; recomputed **0**. The "ce qui"
  route goes via 87, never 47. (Noted as evidence, not as a number I carried.)
- `n06` = **44** on the repaired parse, not 46 — the 46 was the OLD-parse count
  (N28's P(77|06)=6/46). The exact old-parse staleness failure this brief warns
  about, caught live. P(77|06) recomputed 6/44=0.1364.
- `n78` = **31** — I had no banked number; recorded from the stream.
- `94->82` positions = [578, 1182, 1353, 1742] — old-parse [578,1181,1352,1741]
  + REINDEX rule (old n≥773 → n+1), verified byte-level.

N31 spot-check (independent): the round-4 rulings' "values identical for
n≥773" assertion holds — every re-derived count matches its banked value;
only indices shifted, per REINDEX.md. N31 stands.

## Standing kill conditions for the expected round-5 claims

### 1. Frenchman — 62="on" third leg (instrument-independent)
- Current legs: ear lock + 62→94 = 9/35=0.2571 (2.18× era, recomputed — a 9th
  "on ne" @761 from the repaired a5_03 region) + fresh-window subject
  triangulation @845–853 ("…par écrit, on me [dit]…", zero counterexamples in
  26 fresh windows, /ɔ̃/ rivals killed).
- PROMOTION REQUIRES: a leg from an instrument independent of the ear —
  statistical/structural only. Legs 1&3 share the ear instrument (N28); a
  restated ear reading, a bigger fresh-window sample, or any 62-count
  re-derivation does NOT qualify. N22 calibration exclusions enforced (no
  29/82/34 in rate legs); F30 (no era-syllable-conditionals on fragments).
- KILL CONDITION: if the "independent" leg divides by a wrong marginal (the
  N20 B-78b failure mode — verify the denominator), cites 62→94 on the old
  8/34 count, or leans on 87/64/96-provisional anchors without support.
- Status without the leg: STRONG LEAD, unchanged.

### 2. Morphologist — 47="ce" promotion battery
- Current: "ce que" 3/28=0.1071 vs era 0.1076 → 1.00× exact; "par ce" 2.85×;
  47→11 ×3 "cela". Blockers (N29): C2 "..er→ce" 12.6× unexplained, unigram
  2.87×, @148–150 jar bounded (@150–152 "par ce que" ✓), the verbless 64 slot.
- PROMOTION REQUIRES: C2 explained AND the 64-slot residual resolved, or an
  equivalent second independent leg. "Ce que" 1.00× is one leg, not two.
- ECHO WARNING: 87/64/96-provisional are live in every 47 context ("par ce
  que" = 96-47-46). A candidate that "reads" only through provisional anchors
  gets FENCED, not promoted. 47->64=0 (recomputed) — "ce qui" never via 47;
  that's tension for uniform "ce", not a kill, but the battery must address it.
- F33 GUARD: a claim of unconditioned 47=ce∥47=me polyvalence breaks F33 —
  the battery must name the conditioning rule or be denied.

### 3. Morphologist — 06 stem identification
- Current: 06→29 ×4 (repaired; the old 5th was an off-phase artifact), 06→77 ×6,
  06→11 ×4, 06→00 ×4; 00→86 ×12 vs 00→06 ×0 (06/86 complementary distribution);
  n06=44 (repaired). 06="ent" general REFUTED; /mɑ̃/ KILLED (N17); class
  PROVISIONAL; specific stem bounded, NOT identified.
- PROMOTION REQUIRES: ≥2 independent checks on a SPECIFIC stem reading —
  the class already holds provisional. The 66× "demand*" rate gap is the
  baseline any specific-stem claim must clear.
- F30: no era-syllable-conditional legs (06 is a morphological fragment;
  -er-strip legs uncalibrated). F33: 06/86 distribution is complementary
  conditioning — fine as-is; a second free reading without a rule kills F33.

### 4. Bigram Closer — 77="le" / 78="me" vs 78="ver"
- Current: 77→86 ×5 verified @430/798/877/950/1133 ("le"+verb-stem frame);
  77→78 ×7 adverse frames under 78="me" ("pas me" era-0 — kill-grade against
  the frame); 2/7 inside the "gouvernement" trigram → 78="ver" word-internal
  open; 77="pas"/77="que" DISFAVORED.
- PROMOTION (77="le") REQUIRES: the object-pronoun frame + L1 as independent
  legs; the 77→78 ×7 adverse frames must be ADJUDICATED, not waved — either
  killed as frame-adverse (fatal) or absorbed by 78="ver" conditioning (F33).
  If 78="ver" is claimed word-internal, its conditioning rule must be stated.
- 78="me" PROMOTION STAYS DENIED until the 77→78 ×7 frames are resolved
  (N25 — the closer's own finding). "pas me" era-0 is a grammatical kill,
  not a rate anomaly.

### 5. Closer — 87=ce new angles
- Current: provisional-strengthened (F27); cela leg DEAD (N27 — register-matched
  reporter-voice subset fails the pre-stated bar); 87-64-77-84 @1800–1803 =
  «ce qui [verbe] 84» corroboration (not promotion).
- PROMOTION REQUIRES: a non-circular anchor or a non-circular leg.
  The N3 "parce que" frame was admitted CIRCULAR (conditions on 96="par");
  the R1 recycled the dead 24="est" number (VOID). Any claim reusing these
  without disclosure is a traceability violation, not a leg.
- 24-inversion stays empty under era, Les Mis, AND the union model (F27) —
  "24 is not a plain function word" is a legitimate finding, but it is not a
  leg for 87=ce. The F30 instrument restriction still stands.

### 6. Segmenter — rotation claims
- Current: recomputed chi²=366.3 (N30) under repaired phases; cluster
  assignments fragile (61/96 groups change phase); tuner NULL stands
  (phases ≠ word-position classes, N15).
- PROMOTION REQUIRES: a falsifiable positive claim of what the rotation IS,
  not "consistent with X". A rotation-break drag that only reproduces the
  chi² is a re-derivation, not a claim. Any claim using phase→position
  mapping is VOID per N15 (tuner-falsified instrument).
- The 06/86 split and conditioned polyvalence (F33) are the model the rotation
  must coexist with — a claim contradicting F33's falsifiable form
  (1 group → 2 sounds, unconditioned) is itself a claim to adjudicate:
  verify it against the conditioning rules, or kill it with extra care.

### 7. Inventorist — inventory claims
- Current: side-wordpattern fleet adjudicated (redteam/ADJUDICATION.md, F34);
  26 proposals killed; crib-derived inventory is the only legal base for
  fragment hypotheses (F30). The K≥3 synthetic numbers from the tester §6 do
  NOT reproduce — regenerate, never cite.
- Any round-5 inventory claim is judged against R1–R8 (red-team-amended).
  Echo warning: an "inventory" that re-derives the pencil cribs plus the
  provisional anchors is a re-statement, not an instrument.

## Methodology flags carried into round 5

- N22 calibration exclusions enforced in every rate leg (29/82/34 excluded;
  40-conditionals excluded; my own baseline complies).
- F30: rigid syllabification DEAD — no era-syllable-conditional legs on
  morphological fragments; era word-space legs survive.
- Round-3 traceability violation (N20/N26: .md ratios not reproducing from
  archived code) must not recur — every executor number must reproduce from
  shipped code+JSON on the repaired stream; prose ratios are not evidence.
- Instrument independence is audited per claim, not per check count: two checks
  from the same ear/rate are ONE check (the 62="on" legs-1&3 precedent).
- Any number computed on the 1,846-pair parse is VOID unless re-derived
  (REINDEX.md: old n≥773 → n+1). My baseline caught an old-parse count (n06=46)
  in my own first draft — the staleness rule is live.

## Kill ledger — round 5

| Claim | Ruling | Reason |
|---|---|---|
| *(none landed)* | — | Docket empty; session persistent, rulings follow claims as they arrive |

- Promotions: **0** · Demotions: **0** · Kills: **0** · Fenced leads: **0** · Nulls: **1 (the round's docket itself)**
- Net promotion count: **0** — the bar holds for a fifth straight round,
  trivially: nothing cleared it because nothing was brought.

## For the record

The round-4 ledger stands unmodified: kills 47="me" (uniform word),
94="re"→disfavored, 64="même"→disfavored (bounded), 77="le" LEAD-weak→LEAD
(fenced), 62="on" STRONG LEAD (third leg pending), 94="en" co-value DENIED.
Nothing in the armed baseline moves any of those.
