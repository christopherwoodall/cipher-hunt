# Battery report: vient-98-511-relative (@510-517 relative-clause test)

Worker: e4476b7b-d81f-4ea9-a5b1-f326cf4c9b6a. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005 never touched. No invented numbers.
Anchor convention: @-indices are 0-based pair indices in the repaired stream.
Lock: code/crowd17/next-token/locks/vient-98-511-relative.lock (created
2026-10-09T02:19Z, deleted on completion).
Sibling coordination: ne-508-reseg (queued, no lockfile at run time) works the
@507-511 syllabic re-segmentation; this battery works the @510-517 grammatical
parse only. No duplication.

## Bar (verbatim, pre-registered)

"state whether the relative clause parses with <=1 ungranted assumption; if yes, the right side is clean and the residual belongs purely to 'ne'"

Numbered clauses (stated BEFORE testing, unchanged after data):

1. The span @510-517 parses as the relative clause
   "qui vient [65] [88] [56] ce le [80-frame]" under 98='vient' (test premise)
   with at most ONE ungranted assumption. Standing grants (64='qui', 87='ce'),
   provisionals (77='le'), class-level promotions (65=NOUN per battery-prof-65,
   88=governor/verb-class, 80=verb-frame per A8), and the test premise
   98='vient' (battery-promoted, pending red-team) do not consume the budget.
2. IF clause 1 passes: the right side @510-517 is clean (no independent
   strain) and the verb-gap residual belongs purely to the 'ne' reading of 94
   at @509.

## Method

Fresh byte-exact re-parse of the repaired stream in-work; no prior counts
trusted. Window @508-519 re-derived: 508=62 509=94 510=64 511=98 512=65 513=88
514=56 515=87 516=77 517=80 518=09 519=70 (row a3_00). Census of 98 (n=40),
65 (n=25), 88 (n=23), 56 (n=23) followers/predecessors re-derived in-work.
Tested the most charitable grammatical assembly of
"qui / vient / 65 / 88 / 56 / ce / le / [80-verb]" against French grammar,
counting each ungranted assumption independently.

## Window-level evidence (@-offsets, repaired stream)

- @510='64' ('qui', granted), @511='98' ('vient', test premise; 64-98 'qui
  vient' bigram x2 stream-wide: @19, @511).
- @512='65' (NOUN class, promoted battery-prof-65; value open). 98-65 occurs
  x1 stream-wide (this window); 65-88 occurs x1 stream-wide (@512). The
  "98 65 88" contact is entirely singleton.
- @513='88' (governor/verb-class, class-level only; value open). 88-77 x3
  (@86, @646, @1541); 88-77-78 x2 (@646-648, @1541-1543).
- @514='56' (open). 56-87 x2 (@70, @514).
- @515='87' ('ce', granted), @516='77' ('le', provisional), @517='80'
  (verb-frame, A8). The frame "87 77 [verb-frame]" occurs x2 stream-wide:
  @515-517 ('87 77 80') and @869-871 ('87 77 89').
- 98's other followers (n=40): 83 x5 ('de'-lead frames), 82 x3, 80 x3, 98 x3,
  00 x3 ('pour'), 56 x2, 20 x2, then singletons incl. 65 x1. No 98+[noun]
  window besides @511 shows a bare-noun complement.
- 65's standing frames (battery-prof-65): relative-head x3 ('65 qui'),
  object-relative head x1 ('65 que'), post-finite-verb direct object x2,
  post-"-ere" slot x3, post-verb x1 (@511, supporting only). None temporal or
  locative.

## Per-clause pass/fail

1. Relative clause parses with <=1 ungranted assumption — **FAIL**.
   The most charitable grammatical assembly
   "qui vient [65=time] [88=inf] [56], ce le [80]" needs THREE independent
   ungranted assumptions, each verified against the stream:
   - (a) "vient [65]": 65 is NOUN-class with relative-head / direct-object /
     post-"-ere" frames — none temporal or locative. A bare-NP complement of
     "venir" is ungrammatical; the parse needs "65 denotes a time expression
     used adverbially" (cf. "il vient lundi") or an elided preposition.
     Ungranted #1. No stream evidence for a temporal 65.
   - (b) "[88]": 88's class is governor/verb-class at class level only. For
     the single clause to survive, 88 must be non-finite — the purpose
     infinitive ("vient [lundi] [88-inf] [56]", cf. "il vient demain
     chercher X" is grammatical). The infinitive inflection is ungranted #2;
     the preposition reading ("88 le 78" x2 supports prep-88) is likewise
     ungranted and queued separately.
   - (c) "ce le [80]": the preverbal "ce"+"le" clitic stack is unlicensed in
     French of any period ("ce" demonstrative cannot stack with an object
     clitic before a finite verb). Rescue needs a clause boundary plus
     dislocation ("..., ce, le [80]") or 77 != 'le' at this window (77='le'
     is provisional). Ungranted #3. The frame "87 77 [verb-frame]" recurs x2
     (@515-517, @869-871), so the strain is systematic — but systematicity is
     not a license; it is a live residual for the 77/87 line, not a grant.
   Even collapsing (a)+(b) via an elided "de" ("vient de 65"), the count
   stays >= 2. Budget is 1. FAIL.
2. Right side clean; residual purely 'ne' — **NOT AFFIRMED** (conditional on
   clause 1). The right side is not clean: independent strain at @512-517
   (the 65-complement problem, the 88-role problem, the ce-le-80 stack
   problem) persists regardless of how 94 at @509 reads. The verb-gap
   residual therefore does NOT belong purely to 'ne' — this window carries
   its own complement-side strain. This bounds, but does not re-litigate,
   the verb-gap-ne-508 null.

## Adverse answered

- "98-65 is a stream singleton (this window), so the fit is local" —
  **CONFIRMED and fenced with stated cause.** Re-derived: 98-65 x1
  stream-wide (@511); 65-88 x1 (@512). The whole "98 65 88" contact is
  singleton, so this window can neither confirm nor kill 98='vient'
  distributionally. The null below is therefore local-fit only and touches
  no standing verdict: 98='vient' (battery-promote, vient-98-name) rests on
  the 'vient de' / 'vient pour' frames at other windows and is untouched;
  64='qui' untouched; the red-team 12/94 duality untouched.

## Verdict

**NULL** — inconclusive for the battery-promote. The span does not parse as a
clean relative clause within the assumption budget (clause 1 fails at 3
ungranted assumptions vs budget 1), and the failure does not force
98 != 'vient' (strain localizes to the open-value complements
65/88/56/87/77/80, not to 98). No standing red-team verdict contradicted;
nothing downgraded.

## Null follow-ups (per §4 — work regenerates, never ends)

1. `ce-le-verb-frame` (P2): "87 77 [80/89]" x2 (@515-517, @869-871). Bar:
   give a grammatical account of the preverbal ce+le stack with period
   evidence, or demonstrate a rival value for 77 at these windows; else fence
   as a 77-value residual. Discriminates the @510-517 tail and the @869
   window together.
2. `vient-65-complement` (P2): "98 65" is a singleton; 98's other followers
   are 83/82/80/00/98/56/20-class. Bar: state whether any 98+[noun-class]
   window admits a grammatical "venir" complement (time / locative / purpose
   with stated frame evidence), or fence 98-65 as a complement-class
   residual. Decides whether @511's strain touches 98 at all.
3. `88-prep-rival` (P3): "88 77 78" x2 (@646-648, @1541-1543) reads clean as
   "[prep] le [78-noun]"; 88's class is governor/verb-class at class level
   only. Bar: >=2 frame-legs deciding preposition vs verb for 88. A prep-88
   reframes "qui vient [65] [88=prep] [56]" and the @513 slot.

## Provenance

R5005, sealed gate instances, and the red-team adjudication queue untouched.
No invented data. All counts re-derived in-work from the repaired 1,847-pair
parse. Lock created on start, deleted on completion.
