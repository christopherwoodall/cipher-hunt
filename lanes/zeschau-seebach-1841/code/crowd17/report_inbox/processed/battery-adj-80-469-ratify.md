# Battery verdict: adj-80-469-ratify

- Target: `adj-80-469-ratify` (priority 2)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`); `canonical.py` not used.
- Worker: 67823faf-b4a6-4e89-bde6-44b8de6fb3c2

## Bar (verbatim, from queue)

"GATED on 06='ent' ratification (ent-06 battery-promoted 2026-10-08, pending red-team ratification) - do not run before. Then: resolve the 'et que' right edge at @469 and the 43 gate at @1090; fence or promote the adjective leg for 80."

## Bar restated as numbered clauses

1. Gate: 06='ent' ratified at red-team level before running.
2. Resolve the "et que" right edge at @469.
3. Handle the 43 gate at @1090 (fence or resolve).
4. Decide the adjective leg for 80 at @469 with >=2 independent legs under the 06='ent' grant, else fence.

## Gate check (clause 1): PASS

06='ent' is a standing red-team grant: R17-007 GRANT PROMOTE, re-confirmed
R20-011 (DUPLICATE) and R20-064 (GRANT, consistent confirmation).
Registry: none (value-level grant, no class declared). Gate satisfied —
the target runs.

## Method

Re-derived the @469 window byte-exact on the repaired stream (1,847 pairs
verified). Tested the adjective parse against 1841 diplomatic French grammar
with granted values only (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que,
87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 06=ent;
provisional 59=est, 77=le). Census of 06's distribution (44 occurrences)
and of the "79 80 06" / "80 06" frames stream-wide. Wider-window re-parse
@420-480 for the right edge.

## Window-level evidence

### @469 (row a2_10), byte-exact

Pairs @463-476: `59 42 96 00 33 79 [80] 06 67 46 84 24 37`

With grants: `[est?] [42] par pour [33] tout [80] ent et que on [24] [37]`
(59=est provisional, 96=par, 00=pour, 79=tout, 06=ent, 46=que, 84=on;
67=et by the 67 positional rule — follower 46=que is not infinitive-shaped).

### Clause 4, leg 1 — "tout [X]ent" frame grammar: PASS

79=tout is granted as a whole word (A5; R20-013 confirms "79 17" lexicalized
"toutefois" at @451/@1460 but that does not touch the @469 locus, where 79
is followed by 80, not 17). Immediately left-adjacent to 80, "tout" opens
the core French intensifier frame "tout + adjective" (tout entier, tout
différent, tout puissant shapes). Immediately right-adjacent, granted
06='ent' closes the word: "80ent". French -ent adjectives are productive
(apparent, différent, violent, prudent, présent, récent, diligent,
négligent). Distributional corroboration: the byte-identical 4-gram
"33 79 80 06" recurs at @1089 — the frame shape is not a hapax.

### Clause 4, leg 2 — verb-rival exclusion at the locus: PASS

80's only granted verb shape is the infinitive (A8 verb-frames; note R20-121
has since killed the modal-24 arm, leaving the vient-98 arm). At @469, 80 is
immediately followed by granted 06='ent'. Three attachment sub-cases:

(a) Word boundary 80|06: "ent" is not a standalone French word. Dead.
(b) Right-attachment 06+67: "ent"+"et"/"ent"+"veut" forms no French word
    (67's granted values are "et"/"veut", fixed). Dead.
(c) Left-attachment: "80ent" is one orthographic word, 80 its stem, -ent its
    ending. This is DEMONSTRATED (a+b eliminate the alternatives), not
    assumed — it answers fence point (i) of battery-det-adj-80-adjudicate.

On (c): a French infinitive never ends in -ent (endings -er/-ir/-re/-oir),
so the infinitive read — 80's only granted verb shape — dies
morphologically at this locus. A 3pl finite-verb read ("-ent") dies
syntactically: "*tout [3pl-verb]" is ungrammatical ("tout" as subject takes
3rd singular; as adverb/determiner it cannot precede a finite verb). A bare
noun read dies: "*tout [noun]" without determiner is ungrammatical. The only
surviving class in the "tout __" slot is the modifier class
(adjective/adverb). Verb readings are excluded at kill grade at this locus.

Subclass caveat (stated, not hidden): adjective vs adverb cannot be
discriminated at battery level — "tout + adverbe" (tout doucement shape) is
as grammatical here as "tout + adjectif", and -ent closes both adjectives
and -ment adverbs. Discriminating needs 33's value (if 33 names the
"pour"-governed infinitive, the adverbial-agreement test applies) — queued
as follow-up 1 below. The leg promoted is the modifier-class leg; the
adjective subclass is the live hypothesis, adverb the open rival.

### Clause 2 — "et que" right edge: RESOLVED

Wider window @420-480 shows 46=que at @438, opening a subordinate clause
("que [43] [98] [80] [50] …"). The "et que" at @471-472 coordinates with it:
"que … et que …" — the standard two-clause coordination license. The right
edge is not "awkward after an adjective"; it is licensed by the earlier
"que", independent of the adjective phrase. Fence point (ii) of
battery-det-adj-80-adjudicate is answered by the wider-window re-parse.

### Clause 3 — @1090 43 gate: FENCED (per dispatch brief)

Pairs @1083-1096: `02 55 81 00 33 79 [80] 06 43 07 55 81 06` — the same
"33 79 80 06" frame as @469, with 43 immediately right of 06. 43's value is
open (red-team venue; cf. queued noun-43 work). The adjective read at @1090
stays CONDITIONAL on a 43 value compatible with adjective continuation.
Fenced with stated cause; not run, not claimed. Follow-up 2 below re-arms
it when 43 lands.

## Per-clause pass/fail

1. Gate (06='ent' ratified): PASS — R17-007 grant, R20-011/R20-064 re-confirm.
2. "et que" right edge at @469: PASS — resolved ("que" @438 licenses
   "et que" @471-472; 67=et by positional rule).
3. @1090 43 gate: FENCED — 43's value open; re-arm queued as follow-up.
4. Adjective leg at @469 with >=2 independent legs: PASS — leg 1 (frame
   grammar) and leg 2 (verb-rival exclusion) are independent (left-neighbor
   frame evidence vs right-neighbor morphological/syntactic evidence).

## Adverses answered

- Gate adverse ("do not run before ratification"): answered — ratification
  verified in the R20 report before any testing.
- @1090 adverse ("gated on 43's value"): answered — fenced with stated cause,
  not ignored, re-arm proposed.
- @469 conditionals from det-adj-80-adjudicate: (i) 80|06 boundary —
  demonstrated word-internal by elimination (a+b dead above); (ii) "et que"
  right edge — resolved via "que" @438.
- 67-sole-polyvalence law / R20-121: NOT contradicted. This verdict promotes
  a locus-level leg only; it declares no second polyvalence and no global
  class change for 80 (80's global class stays verb-frame per A8/R20-121).
  The @469 hard non-verb window is docket feed for the red-team poly-80
  venue, which R20-121 kept fenced — no standing verdict is overwritten or
  downgraded.

## Verdict: PROMOTE — the @469 adjective leg for 80

@469 is a HARD non-verb window for 80: "tout [80]ent", modifier class
(adjective live hypothesis, adverb open rival), with 80-06 word-internal
demonstrated, verb rivals killed at the locus, and the right edge licensed.
@1090 stays fenced on 43. No registry change proposed (value-level grant
06='ent' already banked; 80's class declaration is red-team venue).

## Follow-ups (supervisor to queue)

1. `adjadv-80-469-subclass` (P2): discriminate adjective vs adverb at @469
   once 33's value lands — if 33 names the "pour"-governed infinitive, run
   the adverbial-agreement test on "tout [80ent]"; if 33 names a noun, run
   the adjective-agreement test. Bar: name the subclass with <=1 ungranted
   assumption, else fence the subclass question.
2. `adj-80-1090-unfence` (P2, GATED on 43's value): re-test @1090 as a hard
   adjective leg once 43 is valued — resolve whether 43 continues the
   adjective phrase nominally; fence or promote. Do not run before the gate.
3. (No third: `val-80-469-stem` already queued — naming 80's stem under the
   "80ent" word-internal reading; do not duplicate.)

## Scope

Single-locus adjudication (@469, row a2_10) plus the @1090 fence. No claim
about 80's other 15 windows, no claim about 06's class, no polyvalence
declaration. R5005, sealed gate instances, and the red-team adjudication
queue untouched.

## Bookkeeping

- Lock `locks/adj-80-469-ratify.lock` created 2026-10-09T17:06:38Z, deleted on
  completion.
- `battery-queue.json`: target `adj-80-469-ratify` queued → verdict/promote,
  own entry only (temp-file + rename; pre-write assert queued/verdictless
  passed), no downgrade (no prior verdict existed).
