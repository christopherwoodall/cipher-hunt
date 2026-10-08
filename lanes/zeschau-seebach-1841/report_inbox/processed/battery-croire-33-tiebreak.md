# Battery report — croire-33-tiebreak (33="croire" rival to "dire")

Worker: subagent da6545e4-14b8-4618-a764-015f54eb7681. Date: 2026-10-08.
Lock: `locks/croire-33-tiebreak.lock` created 2026-10-08T05:07:01Z, deleted on
completion. No prior lock existed (supervisor-checked).

## Bar (verbatim, from battery-queue.json)

`promote-33='croire' iff a discriminating frame is found (parses under croire, fails under dire) or vice versa; else record the tie`

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. C1 — a frame exists among 33's 25 windows that parses grammatically under
   33="croire" and fails under 33="dire" (whole-infinitive windows only; the
   five 33-29 stem windows are out of scope per the A10 stem/whole HOLD).
2. C2 — (vice versa) a frame exists that parses under 33="dire" and fails
   under 33="croire".
3. C3 — every listed adverse is answered: (a) 21's value open — the `33-21`
   x3 noun test is gated, not forced; (b) stem windows kill both equally —
   confirmed symmetric, not assumed; (c) the @1700 `85-33-94-30` contredire
   lead is tested, not forced.

Verdict rule: promote iff (C1 xor C2) passes with C3 answered; kill iff a
cleaner rival is demonstrated on the same frames (not applicable — neither
candidate is cleaner); else null with the tie recorded.

## Method

Parsed per `code/side-keyhunt/repair_parse.py`: `repaired_offsets.json` +
`data/upstream-ct_R5005.txt` = 1,847 pairs. `canonical.py` not used. R5005
not touched. No invented numbers: every count below was re-derived from the
stream in this run.

33 occurs in 25 windows. Census re-derived (matches battery-dire-33
exactly): predecessors 00 x8, 67 x6, 47 x2, 15 x2, 52/37/82/84/42/12/85 x1;
successors 29 x5, 21 x3, 46/16/79/42/00 x2, 55/01/73/96/66/98/94 x1.

Standing values used: 29="er", 82="m" (banked GT); 87="ce", 64="qui",
96="par", 46="que", 79="tout", 00="pour", 47="ce" (A4, allophone tier),
84="on" (A15, conditional), 94="ne", 12="n" (letter). 67 positional rule
applied throughout (67="veut" iff follower infinitive-shaped — 33 is
infinitive-shaped under both candidates, so 67="veut" at all six `67-33`
windows). A10 respected: 33+29 stem/whole HOLD (stem windows excluded from
the whole-frame test); the red-team note ("'dire' leading partial,
unpromoted", next-token-redteam.md) is consistent with this battery —
nothing here contradicts a standing red-team verdict, so no escalation.

## Evidence (window-level, @-offsets are repaired-stream pair indices)

Stem windows — kill both equally, excluded from C1/C2 per A10 HOLD:
@273 `67-33-29-89-84`, @626 `37-33-29-87-78`, @1232 `47-33-29-85-56`,
@1424 `67-33-29-87-63`, @1477 `67-33-29-82-16`. 33-29 x5 needs an -er stem
X; "dire" and "croire" are both -re verbs, so neither can be the stem
member. Symmetric kill confirmed by re-derivation (C3b answered).

Whole-window sweep (20 windows), each tested under croire and under dire:

- `00-33` x8 (@186 `00-33-16`, @408 `00-33-01`, @467 `00-33-79`,
  @846 `00-33-96`, @936 `00-33-21`, @1088 `00-33-79`, @1245 `00-33-16`,
  @1630 `00-33-21`): "pour dire"/"pour croire" both clean at all 8. Tie.
- `67-33-46` x2 (@1451 `67-33-46-92`, @1624 `67-33-46-56`): "veut dire
  que"/"veut croire que" both clean. F1 inherited: "veut savoir que" is
  ungrammatical, so savoir stays killed — but savoir is not this battery's
  rival. Tie.
- `47-33` whole x1 (@24 `47-33-55`): "se/ce dire"/"se/ce croire" both
  clean. Tie. (@1232 is a stem window.)
- `33-21` x3 (@937 `00-33-21-64`, @1422 `15-33-21-67`, @1631
  `00-33-21-64`): "pour [33] [21] qui..." — 21's value is open (n=30;
  successors 67 x8, 62 x5, 60 x4, 65 x4, 64 x2; "[21] qui" x2 is
  noun-shaped but unnamed). Both verbs take noun objects, so no asymmetry
  is available now. Gated, not forced (C3a answered; follow-up 2).
- `33-79` x2 (@467, @1088): "dire tout"/"croire tout". Tie.
- `33-42` x2 (@265 `52-33-42`; @1502-04 chain): 42 open (A1 predicative);
  symmetric under both.
- `33-16` x2 (@186, @1245): "dire [16]"/"croire [16]". Tie.
- `33-00` x2 (@1000 `82-33-00-86`, @1504 `42-33-00-86`): "[33] pour
  [86]er" — equally strained under both.
- Singletons, all symmetric: @24 `47-33-55`, @265 `52-33-42`,
  @776 `15-33-73`, @846 `00-33-96`, @1149 `67-33-66`, @1421 `15-33-21`
  (open neighbors, or equal strain under both hypotheses).

@1700 contredire lead — TESTED, fenced with cause (C3c answered):
@1700 ctx `15-23-91-85-33-94-30-20-62`. 85's contact profile re-derived:
n=15; predecessors 24 x5, 29 x3, 79 x2, 81/76/21/56/91 x1; successors
58 x3, 01 x2, 08/82/93/28/04/41/36/56/48/33 x1. A3 grants 85 a VERB-STEM
frame ("en [85]" x5, "que [85]er" x2). Reading `85-33` as "contre-dire"
needs 85="contre" (a preposition/noun, not a verb stem) at @1699 while 85
is verb-stem-shaped at its other 14 windows — a polyvalence only the red
team can declare (§7: 67 is the sole true polyvalence). The lead is therefore
fenced with stated cause, not merely "untested". Re-test is gated on
stem-85 naming a compound-compatible stem (mé-/re-/contre-class) AND pas-30
resolving 30 (94="ne" is granted; 30="pas" is still queued) — follow-up 1.
Note the honest cost: as written, `85-33-94-30` = "[85][33] ne [30]" also
needs an infinitive-negation or clause-boundary reading for the word order.

Shared residuals — fail under BOTH hypotheses, implicate neighbors, do NOT
discriminate (follow-up 3):
- @1502 `89-41-74-84-33-42-33-00-86`: "on"+infinitive is ungrammatical
  under both. 84="on" is conditional (A15 C1–C3; the 62/84 collision
  battery is queued) — the residual may belong to 84, not 33.
- @1642 `74-35-56-12-33-98-60-03-64`: "n'" elides only before vowels;
  12="n" is granted as a letter, and "dire"/"croire" are consonant-initial,
  so "n'dire"/"n'croire" break under both. The residual may belong to 12's
  segmentation, not 33.

## Per-clause pass/fail

1. C1: FAIL. No frame among the 25 windows parses under croire and fails
   under dire. All 20 whole-windows are grammatically symmetric.
2. C2: FAIL. No dire-only frame is usable under current standing values.
   The single candidate (@1700 compound verb) is fenced on open 85 with
   cause — it cannot promote dire now.
3. C3: PASS. (a) 21 open — `33-21` x3 gated, not forced. (b) Stem-window
   symmetry confirmed by re-derivation: 33-29 x5 kills both equally.
   (c) @1700 tested and fenced with stated cause (A3 verb-stem frame vs
   "contre"; polyvalence bar per §7).

## Verdict: null — the tie is recorded

"croire" ties "dire" on every testable whole-frame: `pour [inf]` x8,
`veut [inf] que` x2, `se/ce [inf]`. No discriminating frame exists under
current standing values, in either direction. This is not a kill: neither
value is demonstrated cleaner than the other, and killing either would
contradict clean windows. Consistent with A10 ("'dire' leading partial,
unpromoted") — no red-team contradiction, no escalation. 33's value stays
open; the live hypotheses remain dire-33-set (33 = {dire, X-er}) and
erstem-33-id (name X). The two shared residuals (@1502, @1642) are fenced
to 84/12, not charged to either candidate.

## Follow-ups (null regenerates work)

1. **croire-33-compound85** — claim: @1700 `85-33-94-30` discriminates via
   dire-only compound verbs (contredire/médire/redire/dédire have no croire
   counterparts). Bars: promote-33="dire" iff stem-85 names 85's value AND
   `85-33` forms a grammatical dire-compound with no croire reading AND
   `94-30` parses (gated on pas-30); kill the lead iff 85's named value
   compounds with neither. Evidence: @1700 ctx
   `15-23-91-85-33-94-30-20-62`; 94="ne" granted; 30="pas" queued
   (pas-30); 85 n=15 with A3 verb-stem frame ("en [85]" x5, "que [85]er"
   x2). Adverses: "contre" fights the A3 verb-stem frame (needs mé-/re-/
   contre-class stem, not the preposition); word order "[85-33] ne [30]"
   needs an infinitive-negation or clause-boundary reading; polyvalence
   bar per §7 if 85 must be two things.
2. **croire-33-noun21** — claim: `33-21` x3 (@937/@1422/@1631) re-tested
   once 21's value resolves; "dire" substantivizes ("le dire") and the two
   verbs may diverge on 21's specific value. Bars: break the tie iff 21's
   named value yields a frame grammatical under exactly one of
   {dire, croire} across the 3 windows. Evidence: `00-33-21-64-37-01` x2
   byte-identical (@937/@1631) + `15-33-21-67-33-29` (@1422); 21 n=30,
   "[21] qui" x2 (64="qui"), 21-67 x8. Adverses: 21's value open; 15's
   value open (@1422); the "noun-shaped" reading is unverified; both verbs
   take noun objects, so the asymmetry must come from 21's specific value.
3. **croire-33-residuals** — claim: the two windows ungrammatical under
   BOTH hypotheses resolve without moving 33's value (via 84/12 re-reads)
   or force a joint revision. Bars: resolve iff each window parses under
   standing values with <=1 stated new assumption, or is fenced with cause
   implicating 84 (A15-C2 collision battery queued) or 12. Evidence:
   @1502 `89-41-74-84-33-42-33-00-86` ("on"+infinitive); @1642
   `74-35-56-12-33-98-60-03-64` ("n'"+consonant-initial infinitive);
   84="on" conditional; 12="n" letter grant (elision needs a vowel).
   Adverses: symmetric failure now — resolution may not discriminate; do
   not force a winner.
