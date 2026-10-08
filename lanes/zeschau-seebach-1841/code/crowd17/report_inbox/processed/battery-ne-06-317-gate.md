# Battery report: ne-06-317-gate — @317's '94 06' hapax

Target: `ne-06-317-gate`. Claim: resolve @317's '94 06' hapax once ent-06 names 06.
Date: 2026-10-08. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`),
parsed like `code/side-keyhunt/repair_parse.py` (re-implemented inline; parse
asserted n=1847). Never used `canonical.py`. R5005, sealed gates, red-team
adjudication queue untouched. No data invented.
Lock: `code/crowd17/next-token/locks/ne-06-317-gate.lock` created
2026-10-08T11:06:34Z; no prior lockfile (no stale-lock note needed).

## Bar (verbatim, pre-registered from battery-queue.json, BEFORE testing)

"discriminate bare-ne + finite 06 vs elided \"n'[06]\" vs adverb-06 readings;
input bar for any future 32-value promotion (clause 2 of adj-32 battery)"

Numbered clauses:

1. Discriminate reading (a): bare-ne + finite 06 — "ne [06]" parses as
   literary bare-ne with 06 as a finite verb.
2. Discriminate reading (b): elided "n'[06]" — 94 elides to n' before
   vowel-initial 06 and the frame parses.
3. Discriminate reading (c): adverb-06 — 06 reads as "-ment" adverb here.
4. The outcome supplies the input bar for any future 32-value promotion
   (clause 2 of the adj-32 battery).

Gate status: OPEN. ent-06 promoted 06="ent" (verb ending; "-ment" = 82+06
compositional) on 2026-10-08
(`code/crowd17/report_inbox/processed/battery-ent-06.md`).

## Method

Re-derived the @317 window and the 94/06 censuses from the repaired stream.
Tested each reading against standing values: banked GT (11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois,
79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); battery
promotions (94=ne, 12=n, 48=e, 06=ent, 30=pas). Elision precedent checked
against 94-59 'n'est' x3. Finite-verb slots checked against 62/84->06
windows. No red-team verdict on 94-06 exists; none is contradicted.

## Window-level evidence (@-offsets)

- **@317**: `[314]45 [315]64 [316]59 [317]32 [318]94 [319]06 [320]11 [321]92`
  = "…ce(45) qui(64) est(59) 32 ne(94) [06] la(11) [92]…".
  Wider: `@310-316` "84-24-37-78-45-64-59" = "on(84) en(24) [37] [78] ce(45)
  qui(64) est(59)". @-offsets are 0-based stream indices of the 32 cell
  (matches adj-32's indexing; A1's battery indexed the 59 cell).
- **94 census (n=37, re-derived)**: followers 82x4, 74x3, 59x3, 52x3,
  92x2, 24x2, 76x2, 79x2, then 20 singles incl. 06x1. 94-06 occurs exactly
  once: @318-320. Hapax confirmed (1 of 37).
- **06 census (n=44, re-derived)**: predecessors 42x5, 82x4, 30x4, 14x2,
  80x2, 06x2, 62x2, 64x2, 12x2, singles incl. 94x1 (@318), 48x1, 84x1.
  Followers 77x6, 00x4, 11x4, 29x4, 67x3, rest <=2.
- **Elision precedent**: 94-59 x3 @558/@762/@1795 = "n'est" (est-59-frames
  battery). Elision before vowel-initial 59 is established on the stream.
  Other 94 + vowel-initial-follower windows: @318 (06), @1169 (87='ce',
  "n'ce" ungrammatical), @1363/@1687 (79='tout', "n'tout" ungrammatical),
  @1664 (84='on', "n'on" ungrammatical). 94-59 is the ONLY successful
  elision frame.

### Reading (a): bare-ne + finite 06 — FAIL

"ne(94) [06]" needs 06 finite. With 06="ent" promoted (verb-ending
syllable), 06 is an ending, not a finite verb. Direct window evidence:
- 62->06 x2 @666/@1537 ("il"+"ent" — no parse; 62='il' rival stood up in
  collision-62-84 battery) and 84->06 @789 ("on"+"ent" — no parse, ent-06
  battery fenced). 06 never occupies a finite-verb slot anywhere on the
  stream: its article followers (77x6 'le', 11x4 'la') sit after
  non-finite/prepositional contexts ("pour"+"ent" x4, "pas"+"ent" x4,
  "le"+"ent" @522).
- The literary bare-ne license needs a savoir/pouvoir/oser/cesser/être-class
  finite verb. 06="ent" matches none.
At @317 specifically: "ne ent la" = ending without a stem — ungrammatical.
Window forces (a) false.

### Reading (b): elided "n'[06]" — FAIL

Phonologically applicable: 06="ent" is vowel-initial, so elision applies
exactly as in the 94-59 "n'est" precedent. Lexically void: "n'ent" is not
a French word. There is no French verb or noun "ent"; "n'ent la" has no
parse. The elision precedent shows the frame only succeeds when the
vowel-initial follower is a real verb (59='est'); every other 94 +
vowel-initial-follower window on the stream fails (@318, @1169, @1363,
@1664, @1687 — all ungrammatical under elision). @317 joins that failing
set. Window forces (b) false.

### Reading (c): adverb-06 — FAIL

ent-06 promoted "-ment" = 82+06 compositional; an adverb-06 reading here
needs an adjective stem before 06. At @317 the predecessor is 94='ne', a
promoted word, not a stem — the ent-06 battery already fenced @318-320 as
"stem slot filled by non-stem". Additionally adverb+"la" is ungrammatical
(@320 = 11='la'). Zero windows on the stream parse 06 as a standalone
adverb; the sole -ment-adverb candidate (@736-739) is 82+06 compositional
and conditional on open 18. Window forces (c) false.

## Per-clause pass/fail

1. Reading (a) discriminated: **FAIL** (kill grade — window forces it false).
2. Reading (b) discriminated: **FAIL** (kill grade — window forces it false).
3. Reading (c) discriminated: **FAIL** (kill grade — window forces it false).
4. Input for 32-value promotion: **NEGATIVE INPUT** — none of the three
   readings parses, so clause 2 of the adj-32 battery stays unmet; a future
   32-value promotion must route around @317's fenced 94, not through it.

## Adverses (from queue; answered, none ignored)

- "gated on ent-06 (do not force)": NOT FORCED. Gate opened legitimately:
  ent-06 promoted 06="ent" on 2026-10-08 via its own battery; this worker
  used the promotion, did not manufacture it.
- "conditional on provisional 59='est' and battery-level 94='ne', 48='e',
  30='pas'": all three readings fail independently of 59 (only @316-317
  context), and the failures are lexical/structural ("ent" is an ending,
  "n'ent" is not a word, adverb needs a stem), not conditional on the
  provisional values. 94='ne' and 06="ent" are the load-bearing values;
  both are battery-promoted, not provisional.
- No standing red-team verdict contradicted. adj-32's null (with @317
  fenced) is upheld, not re-litigated.

## Verdict

**kill** — the gate's claim is falsified at the window: naming 06 ("ent")
did NOT resolve the hapax. All three pre-registered readings fail at kill
grade on @317-320 ("ne ent la" — ending without stem; "n'ent" not a word;
no stem for the adverb). @317's '94 06' stands as a fenced residual, not
as a resolved frame. This does not downgrade adj-32 (its null already
records @317 fenced); it closes the gate and retires the follow-up.

## Follow-up directions (for the supervisor; not queued by this worker)

1. **ne-317-wide-parse** — re-parse the full @314-325 clause ("45-64-59-32-
   94-06-11-92-60-15-63-71") under all standing values with alternate
   word-boundary hypotheses (e.g. 06 composing forward/backward across the
   fenced boundary). Bar: one grammatical parse with <=1 new-value
   assumption; else confirm the fence.
2. **hapax-94-06-rerun** — re-test @317 if verb-32 or a 32-value promotion
   lands (a named 32 re-parses the whole @314-325 clause and may un-fence
   94-06 from the left). Bar: the new 32 value must change the parse of
   "94-06-11" vs the current fence; gated, not forced.
