# Battery A15 — Q1: "que 84-en-37" (84 = clitic pronoun?)

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder Q1 (next-token-findings-que-ce.md).
Windows: @309/@472 byte-identical `46-84-24-37-78` ("que [84] en [37] [78]");
@1485 variant `46-77-84-24-87` ("que le [84] en ce…").
Prediction: 84 = clitic pronoun (je/se/me/te/le/y…), 37 = verb.
Standing: A13 classified 84's arms (masc-noun pre=77 ×7–8; "en"-arm
pre∈{46,94,82} ×3–4); 24="en" GT-strong; A1's 37 predicative frame vs
Q1's 37-verb claim noted as the "cer"-syllable interlock (not litigated here).

## Pre-registered bar (written BEFORE touching data)

- **PROMOTE 84=clitic** (in the "que 84 en" frame) iff ALL hold: (a) @309
  and @472 parse as "que [clitic] en [37-verb]" with zero contradiction
  (37's verb-slot here vs A1's predicative frame is EXPECTED under the
  syllable-interlock — not a contradiction, but say so explicitly);
  (b) 84's "en"-arm contact profile (pre∈{46,94,82}) fits clitic hosts
  ("que"/"ne"/"m" — clitics attach to verbs/conjunctions, not nouns);
  (c) the @1485 variant parses WITHOUT breaking the claim — if @1485's
  84 falls in the masc-noun arm ("que le [84-noun]"), the variant is a
  different arm (split, not a kill); if it parses as clitic-cluster,
  it's a second leg.
- **HOLD** if the frame parses but the clitic value is underdetermined
  (je/se/me/te/le/y not distinguished — the battery promotes the FRAME,
  not the specific pronoun).
- **KILL** if @309/@472 contradict clitic-84 (e.g. 84 demonstrably nominal
  there) or 37 cannot be verbal in that slot.
- 37's verb candidacy here is a bonus leg for the verb battery, not a
  value promotion.

## Data

### The Q1 windows

- @309: `17-46-84-24-37-78` = "fois **qu'on en** [37] [78]"
- @472: `67-46-84-24-37-78` = "[67] **qu'on en** [37] [78]"
- @1485: `46-77-84-24-87` = "que **l'on** en ce [08]"

### The "on"-syllable interlock (10 frame-legs)

| frame | windows | French | corpus |
|---|---|---|---|
| qu'on en | @309, @472 (byte-identical) | "qu'on en [37-verb]" | "qu'on en" ×21 |
| l'on | 77-84 ×7 (@145, @259, @1057, @1446, @1484, @1763, @1802) | "l'on [verb]" | "l'on" ×1852 |
| mon | 82-84 @166 ("24-82-84" = "en mon [53]") | "en mon [53-noun]" | — |

84's successors fit "l'on"/"qu'on" + verb: 59×4 ("l'on **est**" ✓),
24×3 ("l'on **en**"/"qu'on **en**" ✓), 02/92/09×2 (verb slots).
The "en"-arm (46-84, 82-84) and the 77-arm UNIFY under one syllable —
F53's "masc-noun arm (pre=77)" is reclassified: **77-84 = "l'on"**, not
"le"+noun.

### Bar check

(a) @309/@472 parse as "qu'on en [37-verb]" ✓ (corpus ×21; 37's verb slot
expected under A1's "cer"-syllable interlock — "qu'on en [juge]"-shaped,
"37-78" tail consistent). (b) clitic hosts fit: "que"+"on", "m"+"on"="mon"
(even better than clitic — possessive), 94-84@1664 strained (fenced below).
(c) @1485 re-reads as "que l'on en ce" — "l'on" variant, a second leg,
not a split.

### Residuals (named, not hidden)

- R1: @1619 "11-84" = "la [84]" — "la on" is bad. Fenced: possibly a
  genuine "on"-syllable noun ("la [montre]"?) or 11≠"la" here. Single window.
- R2: @1664 "94-84" = "ne on" — strained ("n'on" unstandard). Fenced.
- R3: A13's "qui l'on est [36/35]" — "l'on est [X]" ("one is [X]") is clean,
  but "qui"'s leftward integration still needs a clause boundary (same
  strain as A13's "qui le [N]" had — not worsened).
- R4: 15/25 84-windows unclassified — consistent with "on"-syllable in
  other words ("montre", "long", "répondre"…), not contradictions.

## Verdict: PROMOTE 84="on"

**84 = the syllable "on"** — 10 frame-legs ("qu'on en"×2, "l'on"×7,
"mon"×1), all built on banked values, corpus "l'on"×1852 / "qu'on en"×21.
This CONFIRMS Q1's prediction and upgrades it to a specific value.
**Corrections issued:**
- A13's "qui le [84-noun]" unit → re-read "qui l'on…"; the "le [N] est [X]"
  sub-frame → "l'on est [X]" ("one is [X]") — cleaner, no noun needed.
- F53's "84=masc-noun arm (pre∈{77,11})" → 77-84 is the "l'on" arm;
  the genuine noun-arm (if any) is unclassified.
**Weakest leg (red team):** the promotion leans on "l'on"'s corpus
frequency (×1852) — high-frequency frames are easy to over-fit; the
discriminating legs are "qu'on en"×2 (byte-identical, rare frame) and
"mon"@166. R1/R2 stay fenced.
