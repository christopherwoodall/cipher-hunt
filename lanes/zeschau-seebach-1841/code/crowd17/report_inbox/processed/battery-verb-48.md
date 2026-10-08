# Battery report: verb-48 ("48 verb-stem") — 2026-10-08

Worker: 44c52f5f-52ae-4b6e-9bcc-a4fb56feb2f5. Stream: repaired 1,847-pair parse
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per
repair_parse.py). @-offsets below are the pair index of 48 itself.

## Bar (verbatim, pre-registered)

"promote-frame iff contact profile matches verb stems vs known stems; value battery only after frame holds"

## Numbered clauses

1. The contact profile of 48 (n=38, repaired stream) matches verb stems vs known
   stems. Positive controls: 85 (A3 verb-stem frame grant), 33/86 (INF class),
   80/89 (A8 verb-frames), 76/68 (verb-hood open). Negative controls: 29='er'
   (ending), 11='la', 87='ce', 40='e' (letter).
2. (Adverse) Value NOT promoted — frame only. This battery names no value for 48.
3. (Adverse) The 'est [pred] 48' frames admit the expletif/comparative (mute-'e')
   reading; none forces a verb-stem parse.

## Method

Full predecessor/successor census of all 38 windows of 48 on the repaired stream.
Three features vs controls: P(suc=29) (infinitive -er), P(suc in WORDINIT)
(word-initial cells: 11,77,87,64,79,96,00,84,46,17,70,47 — boundary after 48),
P(pre in VERBGOV) (46,00,84,94,82,77,24,62 — verb governors). Window-level parses
under standing values for every adverse and every lead leg.

## Evidence

48 predecessor census (n=38): 62 x6, 12 x5, 82 x4, 32 x4, 89 x3, 78 x2, 24 x2,
42/29/86/74/96/98/76/85/11/65/71/19 x1 each.

Feature table:

| cell | n | P(suc=29) | P(suc word-init) | P(pre verb-gov) |
|---|---|---|---|---|
| 48 | 38 | 0.053 | 0.263 | 0.316 |
| 85 (A3 stem) | 15 | 0.000 | 0.000 | 0.333 |
| 33 (INF) | 25 | 0.200 | 0.280 | 0.400 |
| 86 (INF) | 32 | 0.125 | 0.062 | 0.531 |
| 80 (A8) | 17 | 0.000 | 0.176 | 0.176 |
| 89 (A8) | 14 | 0.000 | 0.214 | 0.357 |
| 76 | 21 | 0.000 | 0.286 | 0.238 |
| 29='er' | 45 | 0.000 | 0.156 | 0.089 |
| 11='la' | 45 | 0.044 | 0.267 | 0.156 |
| 87='ce' | 32 | 0.000 | 0.531 | 0.375 |
| 40='e' | 21 | 0.048 | 0.095 | 0.000 |

Window-level findings:

- Lead legs re-derived: 82-48 x4 @126/@377/@398/@1229; 79-82-48 trigram x2
  (@398/@1229 at 48); 48-29 x2 @1229/@1589, both as 48-29-47 = "[48]er ce"
  (@1229: '64 79 82 48 29 47 33 29'; @1589: '70 64 65 48 29 47 08').
- CORRECTION to the brief's lead evidence: "elision x4" is overstated. At
  @126 (suc 11='la'), @377 (suc 00='pour'), @398 (suc 06), the successor is
  word-initial — these are "me" + word boundary, not "m'" + elision. Only
  @1229 ('82 48 29', 48 word-internal before 'er') is a live elision leg.
  Elision evidence is x1, not x4. (Vowel-initiality itself is undisputed:
  48='e' is vowel-initial under the standing battery value too.)
- 12-48 x5 @170/@710/@810/@1076/@1737 ("ne", standing battery value).
  NOTE: n-e-12-48 reported x7; the repaired stream shows x5 (offset-shift
  correction, same windows otherwise).
- 'est [pred] 48' x3: @450 ('61 59 32 48 79 17'), @1212 ('64 59 32 48 96'),
  @1779 ('64 59 19 48 74'). All three parse as predicative + mute-'e' under
  the standing 48='e': @450 "est [32]-e toutefois" (79-17 = 'toutefois' per
  the A5 syllable-inventory re-frame); @1212 "est [32]-e par ce...";
  @1779 "qui est [19]-e ...". No following 46='que' at any of the three, so
  no comparative-'que' frame is available; the expletif (mute orthographic
  'e') reading is the live one. None of the three forces a verb stem.
  (The feminine-'e' question feeds the already-queued fem-e-48.)
- 89-48 x3 @641/@872/@987 (89's top successor): reads as "[89]-e" under
  48='e' (verb+ending-shaped), consistent with A8's verb-frame for 89.
- 62-48 x6 @361/@426/@1316/@1350/@1465/@1570: verb-governor-compatible
  position; value of 62 open (collision battery: 'on' killed, 'il'
  demonstrated-not-promoted).
- @1229/@1589 ('[48]er ce' x2) are strained under 48='e' ("e"+"er"+"ce" forms
  no clean word; the frame-29-47 '[stem]erce' alternative needs a stem ending
  before 29 that 48='e' does not supply) and clean under 48=verb-stem
  ("m'[STEM]er ce", "[65] [STEM]er ce"). These two windows are the frame's
  only exclusive legs.
- 48's successors are 29 distinct types in 38 windows (near-maximal spread),
  with 10/38 word-initial (11, 77 x2, 79, 96 x2, 00, 84, 47 x2) — a
  boundary-heavy profile. The cleanest verb stem, 85, has P(suc word-init) =
  0.000: never word-final. 48 is word-final 'e' at 9/38 windows ("me" x4,
  "ne" x5) plus predicative-'e' at 3/38.

## Per-clause pass/fail

1. FAIL. 48's profile sits inside the ambiguous verb-cell middle (33/89-like)
   but does not match verb stems at the clean-stem standard: 85 never ends a
   word (P=0.000); 48 is word-final letter-'e' at 12/38 windows ("me" x4,
   "ne" x5, predicative-'e' x3) and boundary-adjacent at 10/38 successors.
   A stem is word-internal by definition; 32% of 48's windows place it
   word-final. The A7-L2 legs (7 windows) are stem-compatible but a minority,
   and the "elision x4" lead is really x1.
2. PASS. No value named; frame test only, per the bar.
3. PASS. All three 'est [pred] 48' windows admit the mute-'e' (expletif)
   reading under the standing 48='e'; none forces the stem.

## Verdict: NULL

HEADLINE (red-team escalation): this result tensions the standing red-team
A7-L2 grant ("48 = verb-stem candidate", frame). The grant's 7 legs are not
falsified — @1229/@1589 genuinely admit the stem reading and strain under
48='e' — but the full 38-window contact profile does not match verb stems:
12/38 windows are better explained as word-final letter-'e' (the standing
battery-promoted 48='e' value), and the profile's boundary rate (0.263)
matches function cells, not the clean stem 85 (0.000). The frame, if it
survives, is confined to its exclusive legs; it does not generalize to 48.
Not kill: no window forces 48≠stem (@1229/@1589 favor the stem). Per protocol
section 7, the A7-L2 grant is not overwritten here; the red team adjudicates
whether to narrow it to the exclusive legs or retire it. The 48='e' /
verb-stem tension (sole-polyvalence rule: 67 only) is now explicit and needs
a ruling.

## Follow-up targets (null regenerates work)

1. stem48-exclusive-legs — "A window requires the stem reading iff it is
   ungrammatical under the standing 48='e'. Full 38-window sweep; only
   @1229/@1589 are candidates." Bar: retire-frame iff zero windows require
   the stem; hold-frame iff >=1 requires it AND letter-'e'-required windows
   stay below 10%.
2. elision82-48-x1 — "Re-test the 'elision x4' lead: @126/@377/@398 are
   'me'+word-boundary (successors 11/00/06 word-initial); only @1229 is a
   live elision leg." Bar: confirm the x1 elision leg with a vowel-initial
   infinitive parse at @1229, or retire the elision claim.
3. w48-boundary-census — "Classify 48's boundary (word-initial / -final /
   -internal) at all 38 windows under standing values." Bar: the stem-frame
   survives as a general claim iff >=80% of windows admit stem-internal 48;
   else scope A7-L2 to its exclusive legs or retire it.
   (Note: 'est [pred] 48' x3 already feeds queued fem-e-48; 89-48 x3 is input
   for 89's value battery. Not re-queued.)
