# Battery report: frame-76-tension — 76 "gender tension"

- Target id: `frame-76-tension`
- Worker: subagent 02d9d14d-b528-4435-b9c6-5963d2bd8877
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  canonical.py NOT used. R5005 NOT touched. All @-offsets are global pair indices
  on the repaired stream.

## Bar (verbatim, pre-registered)

> "resolve iff one class with positional rule, or second polyvalence declared by red team only"

### Numbered clauses

1. 76 is resolved to ONE class, with a stated positional rule covering all 21
   windows on the repaired stream — including the "la" tension window.
2. OR a second polyvalence is declared for 76 by the red team (battery may not
   declare it; per §7, 67 et/veut is the sole true polyvalence).

## Method

Re-parsed the repaired stream; censused all 21 windows of 76 (n=21) with
predecessor/successor contact profiles; re-derived each element of the
finder's evidence verbatim; tested class coherence against standing ground
truth (11=la pencil, 77="le" provisional per le-77 NULL, 67="et/veut"
polyvalence with positional rule per §7, 94="ne" promoted, 47="ce" A4,
06="ent" promoted).

## Window-level evidence (@-offsets on the repaired stream)

76's 21 windows (pre-4 shown): @13 a1_00 (62 98 76 45), @200 a2_00
(08 67 76 87 11 92), @362 a2_06 (48 76 47 78), @427 a2_09 (48 76 42 63 77),
@487 a2_11 (64 76 42 41 20), @568 a3_02 (13 76 45 94 52), @621 a4_01
(37 76 82 14 59), @652 a4_02 (52 82 94 76 49 24 26 30), @735 a5_02
(93 76 18 82 06), @833 a5_06 (87 11 77 76 59 35 56), @892 a5_08
(06 77 76 01 98 82 14), @969 a6_00 (06 77 76 01 98 48 51), @980 a6_01
(07 76 47 78 45), @989 a6_01 (01 76 49 24 26), @1046 a6_04
(11 67 76 85 41 88), @1273/@1275 a7_02 (47 76 87 76 48), @1395 a7_07
(16 76 47 78 48), @1432 a7_08 (16 76 49 64 52), @1577 a8_01
(52 82 94 76 47 98 24 53), @1616 a8_03 (31 76 42 44 11).

Finder-evidence re-derivation:
- "'le [76]' x3" — CONFIRMED: 77-76 @833, @892, @969 (5-gram
  06-77-76-01-98 x2 sits inside @892/@969, starting @890/@967).
- "'la [76]' x1" — NOT FOUND: 11-76 x0 on the repaired stream.
  Closest la-contact: @1046 ('11 67 76', i.e. la before 67, not before 76),
  @833 ('87 11 77 76', 11 two left of 76 under intervening 77), @1616
  ('…76 42 44 11', 11 three RIGHT of 76). None is a "la [76]" bigram. The
  finder's tension bigram exists on neither the repaired parse nor, as far as
  this worker can verify, any documented variant; the discrepancy is
  recorded, not hand-waved. NOTE: canonicality caveat (§7) stands — 68 of 70
  upstream row offsets unvalidated — but the worker tests the repaired
  stream only, per §3.
- Emergent (not in finder evidence): noun-vs-verb contact tension. Noun-side:
  77-76 x3; 76-47 x4; 76-42 x3; 76-87 x2; 76-01 x2. Verb-side: 94-76 x2
  (@652, @1577: "…82 94 76…" under 94="ne" = "ne [76]"); 67-76 x2
  (@200, @1046: "67 76" = "et/veut [76]", verb-shaped iff 67="veut");
  48-76 x2 (@362, @427; 48 vowel-initial per verb-48 elision frames).
  Predecessor census: 77 x3, 67 x2, 48 x2, 94 x2, 16 x2, singletons
  (98, 64, 13, 37, 93, 07, 01, 47, 87, 31).

## Per-clause pass/fail

- Clause 1 (one class + positional rule): FAIL. No one-class parse covers all
  21 windows. 76=noun fails at 94-76 x2 ("ne [76]" ungrammatical without a
  verbal head; the clitic-order anomaly "82 94" = 'me ne' at @652/@1577
  suggests the sub-word parse needs work but does not fence either window
  cleanly). 76=verb fails at 77-76 x3 ("le [verb]" ungrammatical under
  77="le" provisional; downgrading 77 would collide with le-77's own null
  verdict and load-bearing A8/A13/A15 frames). No positional rule candidate
  is grounded: any "verb iff pre in {94,67,48}, noun iff pre=77" formulation
  would be a battery-level second-polyvalence declaration, forbidden by §7
  (67 et/veut is the sole true polyvalence).
- Clause 2 (red-team-declared second polyvalence): FAIL — not declared. Red
  team has not adjudicated 76; red-team eyes were on this tension per finder
  evidence, but no declaration exists in code/crowd15/report_inbox/
  next-token-redteam.md or §7. Battery may not declare it.

## Verdict: null

Rationale: inconclusive, not kill. No window forces the one-class claim
false at kill grade — each rival parse admits a live alternative ("82 94"
clitic-order anomaly blocks the clean "ne [76]" verb read; 77="le" is
provisional, so the "le [76]" noun read is itself conditional; @1046
'11 67 76' parses as "la et [76]" noun-coordination, leaving only
@200/@1046's 67-reading ambiguous under 67's own granted positional rule).
The bar's premise is also partly unfounded: the 'la [76]' bigram does not
exist on the repaired stream, so the gender tension as stated dissolves
into a null-evidence state rather than resolving. This contradicts no
standing red-team verdict (76 has no adjudicated value or class), so no
escalated-null is required — but the 76 class question is referred to red
team as an open fork in follow-up F3.

Adverses: none listed. All numbers above trace to the repaired stream.

## Follow-ups (null mandates 1–3; nulls regenerate work)

1. frame-76-ne-94 — "ne [76]" x2 (@652, @1577): decide verb-read vs sub-word
   re-parse under the ne-distributed duality (94="ne" vs 48="e"); audit the
   "82 94" clitic-order anomaly at both windows.
2. frame-76-67 — 67-76 x2 (@200, @1046): adjudicate against 67's standing
   positional rule (67="veut" iff follower infinitive-shaped) — is 76
   infinitive-shaped? Discriminates 76-as-infinitive from 76-as-noun-after-"et".
3. noun-76-candidates — test 'meme/premier-type' noun candidates under
   one-class noun agreement (le/la agreement, not polyvalence), with full
   contact-profile census; gated on le-77 ratification (77="le" is provisional).
