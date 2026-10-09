# Battery report — w2-16-class (16's class with >=3 frame-legs; left-edge close test)

Worker: b5a8f263-7d62-44e0-be50-bda75439c633. Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/w2-16-class.lock` created 2026-10-09T09:08:57Z;
no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(replicated in-worker, not `canonical.py`). R5005, sealed gates, red-team queue
untouched. Every count below re-derived from the stream in this run.

Parent: reseg-3006-w2 (null, 2026-10-09) follow-up #2.

## Bar (pre-registered verbatim, from battery-queue.json)

"assign 16's class with >=3 frame-legs; then test whether 'cela pour [33] [16]'
closes the left edge so '00 67 46' can be fenced as clause-initial"

Numbered clauses (restated from the bar verbatim before testing, not modified
after):

1. C1 — 16's class is assigned with >=3 frame-legs (independent grammatical
   frames parsing under one class with stated standing values).
2. C2 — "cela pour [33] [16]" (@1242-1246) closes the left edge (parses as a
   complete clause), so that "00 67 46" (@1247-1249) can be fenced as
   clause-initial.

Adverses (queue): none.

## Method

Re-derived the repaired stream (assert 1,847 pairs; assert 96 types).
Censused all 28 windows of 16 with ±4 context and row IDs. Adopted as
premises (not re-litigated): 16=infinitive is a standing battery PROMOTE
(gate-satisfiability-16-85, 2026-10-08; §5 forbids overwriting); 62 is
non-pronominal at the four 62-16 windows (class-62-16-windows, promote,
2026-10-09); the doubled frame @1195-1198 is a universal killer, fenced
(laisser-gate-16, null); @1142 is a fenced universal residual
(gate-satisfiability-16-85). Standing values used: pencil GT 11=la, 82=m,
29=er, 40=e, 46=que, 70=pre, 34=i; granted 87=ce, 64=qui, 96=par, 17=fois,
79=tout (A5), 00=pour (A9), 84=on (A15), 47=ce (A4); provisional 59=est,
77=le; battery 24=finite verb modal-shaped, 98=finite verb, 88=VERB;
§7 sole polyvalence 67=et/veut (67='et' iff follower not infinitive-shaped).
1841 diplomatic French only.

## Window-level evidence (@-offsets are 0-based repaired-stream pair indices)

n(16)=28 confirmed. Anchors from the claim verified byte-exact:
@659=16, @660=00, @661=86 ("16 00 86"); @844=16, @845=00, @846=33
("16 00 33").

Predecessor census: 82 x11, 62 x4, 12 x3, 33 x2, 42 x2, 65/32/49/86/67/89 x1.
Successor census: 00 x4 (@187, @659, @844, @1246), 24 x2, 01 x2, 91 x2,
76 x2, singletons 14/56/52/78/08/77/92/88/29/96/64/02/06/97/98/59.

W2 left edge (verified): @1240=77, @1241=81, @1242=87, @1243=11, @1244=00,
@1245=33, @1246=16, @1247=00, @1248=67, @1249=46, @1250=26. Row a7_01 ends
at @1247; row a7_02 starts at @1248. "00 33 16 00" occurs exactly 2x
stream-wide: @185 and @1244 (0-based 00 positions). Row a7_01 full:
@1219-1247 = "61 24 48 30 09 20 57 64 79 82 48 29 47 33 29 85 56 10 03 40
67 77 81 87 11 00 33 16 00" (finite verb 24 at @1220).

### C1 frame-legs for 16=infinitive (standing assignment, confirmed)

- Leg 1 — "82-m' [16-inf]" x11 (banked 82='m'). Elided clitic + vowel-initial
  infinitive is grammatical ("pour m'aider" pattern). Four INF-clean windows
  per the standing gate battery, spot-confirmed on bytes: @434
  ("77 86 29 82 16": "le pouvoir me [inf]"), @1370 ("60 03 30 82 16":
  "ne...pas me [inf]" frame, 30='pas' promoted), @1480 left edge
  ("67 33 29 82 16": "veut [X]er me [inf]" causative shape), @1832
  ("38 83 24 82 16": "de me [inf]" pattern).
- Leg 2 — "12-n' [16-inf]" x3 (@242, @844, @1431; banked 12='n'). "n'" +
  infinitive is grammatical ("n'avoir pas", "n'être pas" literary); 12
  carries the promoted syllabic duality as second reading.
- Leg 3 — "[16-inf] 00-pour [86/33]" x2 (@659 "16 00 86", @844 "16 00 33").
  Purpose chain "[inf] pour [inf]" ("partir pour ne plus revenir");
  conditional on 86/33 infinitive (86 class disputed, 33 class open).

Three frame-legs exhibited; a fourth ("67-veut [16-inf]" @903) is supportive
but circular (67's positional value assumes 16's shape) and not counted.

Standing dispute headlined, not hidden: laisser-gate-16 (null, 2026-10-09)
carries a finite-verb lead fitting 24/28 windows and a CONTRADICTION
HEADLINE against the standing 16=infinitive promote (escalated to red team,
not resolved here); val-16-a-vs-est (null) fenced the 'a'/'est' refinement
(both forced-false at @1143 and @1481); the doubled frame @1195-1198
("m'[16] par m'[16] qui") is a universal killer, fenced. @1480's right edge
("16 98", 98=finite verb per prof-98) is strained under the infinitive
assignment (needs an unevidenced clause boundary); recorded as residual,
consistent with laisser-gate-16 C3.

### C2 — "cela pour [33] [16]" close test

Segment @1242-1246 = "87 11 00 33 16" = "ce la pour [33] [16-inf]"
(87=ce promoted, 11=la GT, 00=pour A9, 16=infinitive standing).

Close attempts, all fail:
- (a) "cela" (subject) + "pour [33] [16-inf]" (predicate): no finite verb
  in the segment; 16 is infinitive by standing promote. Not a clause.
- (b) 33 as finite verb: "pour [33-finite]" is ungrammatical in 1841
  French; 33's open arms are infinitive/nominal (lane notes), neither
  supplies a finite verb here.
- (c) 33=infinitive: "pour [33-inf] [16-inf]" (two bare infinitives) is
  ungrammatical.
- (d) 33=nominal: "cela pour [33-noun] [16-inf]" is a purpose fragment
  ("that, for [noun], to [do]"), not a closed clause.
- (e) Under the finite-verb lead (16='a'/'est'): "cela pour [33] a/est"
  still lacks its complement ("a/est pour et que" is ungrammatical), so
  the segment does not close under the rival class either.
- (f) The row's finite verb is 24 at @1220 ("[61] [24-verb] e pas..."),
  so "cela pour [33] [16] pour" is the main clause's tail (purpose
  adjuncts), not a closed clause.

The parallel "00 33 16 00" window at @185 ("...00 33 16 00 66 24...") shows
the same unclosed shape ("pour [33] [16] pour [66] [24-verb]"), confirming
the pattern is a mid-clause purpose chain, not a clause boundary.

Therefore the left edge does NOT close at @1246, and "00 67 46"
(@1247-1249, spanning the a7_01/a7_02 row boundary) cannot be fenced as
clause-initial on the basis of a closed left edge. It remains the fenced
mid-clause residual per reseg-3006-w2 C4 ("pour et que": 67='et' forced
positionally since follower 46='que' is not infinitive-shaped;
coordination implausible at 57 tokens; "veut" ungrammatical after "pour").

## Per-clause pass/fail

1. C1 — PASS (confirming). 16=infinitive, the standing battery assignment,
   is exhibited with 3 frame-legs ("82-m' [16-inf]" x11, "12-n' [16-inf]"
   x3, "[16-inf] pour [86/33]" x2). The finite-verb lead contradiction and
   the fenced residuals are standing battery findings, adopted not
   re-litigated; no standing verdict overwritten (§5).
2. C2 — FAIL. "cela pour [33] [16]" does not parse as a complete clause
   under standing values (no finite verb; attempts (a)-(f) exhausted), so
   "00 67 46" cannot be fenced as clause-initial on that basis.

## Verdict: NULL

C1 passes, C2 fails; the bar as a whole is not satisfied. C2's failure is
a negative test outcome (the left-edge-closing hypothesis is rejected),
not a kill-grade failure of the target's claim. No standing or red-team
verdict contradicted or downgraded; §7 intact.

## Follow-ups proposed (null regenerates work; all verified absent from queue)

1. `val-33-adv-test` (P3) — test 33 as adverb at the "00 33 16 00" x2
   windows (@185, @1244). Bar: "pour [33-adv] [16-inf]" parses as a
   grammatical purpose phrase ("pour bien faire") at both windows with
   zero contradiction; if 33=adverb holds, re-test C2's left-edge closing.
2. `knot-0067-rowboundary` (P3) — test a clause boundary between @1247
   (00, last pair of row a7_01) and @1248 (67, first pair of row a7_02).
   Bar: exhibit byte-evidenced boundary or kill it; if it holds,
   "67 46 26..." is clause-initial and the stranded "pour" @1247 is
   re-fenced as an incomplete purpose clause.
3. `pour33-16-185-parallel` (P3) — fully parse the parallel "00 33 16 00"
   window at @185 ("...00 33 16 00 66 24..."). Bar: if @185's window parses
   with a closed left edge, apply the same structure to @1244; else fence
   both as pattern residuals.

## Bookkeeping

- Report: this file.
- battery-queue.json: `w2-16-class` → status `verdict`, result `null`,
  date 2026-10-09 (temp-file + rename, own entry only; pre-write assert
  passed: was queued/verdictless).
- Lock `locks/w2-16-class.lock`: created on start, deleted on completion.
  No pre-existing lock was present.
