# Battery verb-93: 93 verb-shaped discriminator

## Bar (verbatim)
"resolve iff 93 takes infinitive/valency markers with contact profile verb-shaped"

## Bar restated (numbered clauses)
- C1: 93 takes infinitive/valency markers (29='er' contact, 06='ent' contact, que-subjunctive valency, noun objects).
- C2: 93's contact profile is verb-shaped (distributional discriminator vs reference verb/noun groups; zero forced non-verb windows).

## Method
Read BATTERY-PROTOCOL.md first. Re-derived the stream independently from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
via `code/side-keyhunt/repair_parse.py`: 1,847 pairs / 96 types confirmed.
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Lock created on start, deleted on completion.

## Census (93, n=14)
@10 "18 93 62 98" | @102 "62 94 93 59 45" | @111 "67 93 29 89" |
@159 "35 93 52 94" | @263 "45 93 52 33" | @479 "45 93 00 13" |
@604 "45 93 54 64" | @734 "85 93 76 18" | @1540 "62 93 88" |
@1555 "13 93 61 40 17" | @1685 "13 93 62 94 79" | @1761 "15 93 06 77" |
@1812 "15 93 50 42" | @1846 "74 93" (stream-final).

Predecessors: 45 x3, 13 x2, 15 x2, 18/94/67/35/85/62/74 x1.
Followers: 62 x2, 52 x2, 59/29/00/54/76/88/61/06/50 x1.

## Discriminator (vs reference groups, same stream)
P(45='que' immediately before): 93 = 0.21 (3/14); 24/32/98/21/26/76/42 = 0.00.
P(29 after): 93 = 0.07; all references 0.00.
P(06 after): 93 = 0.07; all references 0.00 (42=0.25 is 06-before, different test).
93 is the only group in the reference set that ever follows 45='que'.

## Per-clause results
- **C1 PASS.** Infinitive/valency markers, all byte-traced:
  - @111 "67 93 29": 93 takes 29='er' (banked GT); "93"+"er" is infinitive-shaped,
    and fires the standing 67 positional rule (67='veut' iff follower
    infinitive-shaped): "que la [21] veut [93]er [89]" is a clean
    modal+infinitive frame.
  - @1761 "15 93 06": 93 takes 06='ent' (promoted); "[93]ent" is 3pl
    finite-shaped; right side "77 84" = "l'on" (77-84 x7 pattern).
  - Valency: "45 93" que-subjunctive x3 (@263/@479/@604) with complements
    (52 x2, "pour" 00, 54); noun objects 52 x2, 76 (promoted masculine noun);
    "94 93" ne-frame @102; modal-stem frame @734 ("85 93 76" = modal-stem +
    infinitive + object, parallel to @111).
- **C2 PASS.** The contact profile is verb-shaped: unique que-selection,
  ne-frame, finite/infinitive endings, object valency. Window parses:
  @10 "[18] [93] | [62] vient [76]" (two clauses); @159 "[35] [93] [52] |
  ne [24]" (literary ne); @1555 "[13] [93] [61]e fois" ("[61]e fois" =
  ordinal+'e'+'fois', cf. "la première fois" @1035-1041); @1685 "[13] [93] |
  [62] ne tout [14]" (62-94 is the known x9 bigram); @1812/@1761 finite frames.

## Adverses
- "profile currently inconclusive" — ANSWERED. The discriminator plus marker
  contacts make the profile conclusive at class level.
- Residual 1 (fenced, stated cause): @102 "62 94 93 59" ("ne [93] est") is
  ungrammatical under the verb reading, but the judgment is conditional on
  three unratified values: 94='ne' (STRONG LEAD, ungranted), 59='est'
  (provisional), 62 (open). Re-segmentation "94 [93-59]" noted, not decided.
- Residual 2 (fenced, stated cause): @1846 is the stream-final pair; a bare
  group at the stream edge has uncertain segmentation. Positional residual.

## Verdict: PROMOTE (verb class)
93 = verb (class-level; value open). No standing red-team verdict on 93
exists, so nothing is contradicted or downgraded. No new polyvalence
declared (§7 intact: 67 et/veut remains the sole true polyvalence).

## Follow-ups
None required for a promote. Suggested (optional): `verb-93-value` (P3) —
name 93's value once 13/15/18 resolve as subject candidates; gated on
red-team ratification of this class promote.
