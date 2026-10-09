# Battery report: lon-94-64-rightedge (@509-510 'ne qui' right edge)

Worker: 8bfb8ca3-cd47-4c2e-bc36-45a5ea02991f. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005 never touched.
Anchor convention: @-indices are 0-based pair indices in the repaired stream,
matching battery-lon-ne-77-62-94.md (verified: its window table and
"@509->@510" both reproduce exactly under this convention).
Lock: code/crowd17/next-token/locks/lon-94-64-rightedge.lock (created
2026-10-09T00:20:18Z, deleted on completion).

## Bar (verbatim, pre-registered)

"resolve iff a clause boundary intervenes between @509 and @510 with the
parse stated, or the 64='qui' assumption fails here with stated cause; else
fence with stated cause"

Numbered clauses (stated BEFORE testing, unchanged after data):

1. A clause boundary intervenes between @509 and @510, with the parse stated
   on both sides: the left clause ending at @509 is complete and grammatical
   under standing values, and the right clause beginning at @510 is complete
   and grammatical.
2. OR the 64='qui' assumption fails at @510 with a stated cause (a rival
   value or structural reason local to this window; the 64='qui' grant
   itself is not downgraded).
3. If neither clause 1 nor clause 2 holds, fence with stated cause
   (null-grade outcome, not a kill of any grant).

Adverse: 64='qui' promoted — answered below by window-level fencing with
cause; the grant is not touched.

## Method

Fresh parse of the repaired stream; no prior counts trusted. Re-derived the
@505-517 window, the full 94-follower and 64-predecessor censuses (37 and 47
windows), and the neighboring '64-98' and '98-83' frames. Tested the clause-
boundary arm against standing values (banked GT; 67 et/veut positional rule;
77='le' provisional; 62='il' vs conditioned-'on' unresolved at battery level;
94='ne' battery-promoted pending ratification; 64='qui' granted; §7 sole-
polyvalence law). Left-context (@505-509) taken as analyzed in
battery-lon-ne-77-62-94.md and not duplicated; this battery decides only the
@509-510 right edge.

## Window-level evidence (@-offsets, repaired stream)

Singleton re-derived: '94-64' occurs x1 stream-wide (@509->@510, row a3_00;
no row boundary between the pairs). 94 n=37 with 24 distinct followers —
'64' is its sole 'qui' follower (x1). 64 n=47 with 29 distinct predecessors
— '94' is its sole 'ne' predecessor (x1). The anomaly is symmetric: it
isolates to this single contact, not to either value's profile.

Window (0-based), row a3_00:
@505='21', @506='67' (et: positional rule, follower 77 not infinitive-shaped),
@507='77' (le? provisional), @508='62' (il? / conditioned-on? — open),
@509='94' (ne*), @510='64' (qui, granted), @511='98' (open, n=40),
@512='65', @513='88', @514='56', @515='87' (ce), @516='77' (le?),
@517='80'.

Full 94-follower census (37 windows): 82 x4, 74 x3, 59 x3, 52 x3, 92 x2,
24 x2, 76 x2, 79 x2, 93/65/06/02/64/29/60/07/15/26/87/70/84/30/88/44 x1.
Full 64-predecessor census (47 windows): 87 x5, 03 x4, 45/37/65 x3,
39/67/92/49/21 x2, 56/09/19/94/54/00/77/07/51/78/16/57/20/71/70/84/30/69 x1.

Right-neighbor check: '64-98' occurs x2 stream-wide (@18-19: "17-64-98-82-43"
= "fois qui [98] m [43]...", and this window @510-511). 98's value is open;
the @18-19 window does not discriminate 64='qui' either way, so 'qui 98' is
not itself anomalous — the anomaly is strictly the 'ne'-before-'qui' contact.
98's top predecessors are 62 x5, 42/66/98 x3, 64 x2; 98-83 x5 is the
'vient de' formula family (frame-vient-parvenir, queued) — not this window.

## Per-clause pass/fail

1. Clause boundary between @509 and @510 with parse stated — FAIL.
   (a) Left side: @505-509 = "21 et [77] [62] ne". Under the 'il' rival the
   trigram is already dead ("et le il ne", per lon-ne-77-62-94). Under the
   'l'on' rival the clause reads "...et l'on ne" — and 'ne' is a bound
   preverbal clitic: it must be followed by a finite verb (bare 'ne' with
   cesser/oser/pouvoir/savoir, expletive 'ne', 'ne...que', 'n'importe' —
   every licensed form has 'ne' immediately before a verb). No verb stands
   in @505-509, and none can intervene between @509 and @510 by hypothesis.
   Ending the left clause on 'ne' leaves it dangling: ungrammatical.
   (b) 'ne' cannot attach to the right clause either: 'ne' never begins a
   French clause ("ne qui..." is ungrammatical; no licensed form puts 'ne'
   before 'qui').
   (c) Right side: @510+ = "qui [98] [65] [88] [56]..." — a 'qui'-headed
   relative clause with no grammatical matrix on either rival reading
   (the matrix clause is broken in (a)).
   No placement of the boundary yields a stated grammatical parse. FAIL.
2. 64='qui' fails at @510 with stated cause — FAIL (no cause statable at
   battery level). No rival value for 64 is in evidence at this window:
   "nequi" is not a French word-form (word-internal read excluded), pair
   tokenization is fixed by the repaired parse, and the 'qui'-as-relative
   reading is not refuted by its right neighbor ('qui 98' recurs cleanly
   at @18-19). Declaring a second, window-local value for 64 would be a
   positional-polyvalence act, which §7 reserves to the red team (67
   et/veut is the sole true polyvalence). The anomaly being symmetric
   (94's only 'qui', 64's only 'ne') gives no directional cause. FAIL.
3. Fence with stated cause — TAKEN.

## Verdict

**NULL — fenced with stated cause.** The 'ne qui' singleton at @509-510 is a
genuine 1-window residual: no clause boundary can intervene between the
pairs ('ne' dangles on both rival readings and cannot open the next clause),
and no window-local cause exists for 64='qui' to fail here. The contact is
symmetric (94's sole 'qui' of 37; 64's sole 'ne' of 47), so the residual
localizes to the contact itself, not to either value's profile. Per the
task brief, this window-level fence is a null-grade outcome: the 64='qui'
grant is NOT downgraded, the 94='ne' promotion-track is NOT re-litigated,
and no standing verdict is modified. Red-team-owned questions (12/94
duality, conditioned 62='on', §7 polyvalence) are not decided.

## Adverses (answered or fenced, never ignored)

- 64='qui' promoted: fenced at window level with the cause stated above;
  grant untouched. The bar's second arm was tested and failed for lack of a
  statable cause, not skipped.

## Null follow-ups (per §4 — work regenerates, never ends)

1. verb-gap-ne-508: the 'ne' @509 has no verb in its clause on either rival
   reading. Test the downstream span @510-525 for a finite-verb candidate
   that completes the 'ne' clause under a re-parse keeping 64='qui' (e.g.
   98 verb-shaped with the clause boundary placed AFTER @510, or a
   matrix verb further right). Bar: state the full parse with the verb
   named and every pair @505-520 assigned; else confirm the verb gap as a
   second window residual.
2. ne-follower-verbless-sweep: classify all 37 windows of 94 by whether a
   verb follows within the clause (full follower census in this report:
   82 x4, 74 x3, 59 x3, 52 x3, 92/24/76/79 x2, 16 singletons incl. 64).
   Bar: if @509 is the sole verb-less 'ne', the residual stands alone; if
   a verb-less family exists, re-frame the @508 window inside it.
3. qui-94-syllabic-rival: gather window-level evidence for the red-team-owned
   12/94 duality AT THIS WINDOW ONLY — test a word-internal syllabic parse
   covering @507-511 ('77-62-94-64') with each pair's syllable role stated
   (cf. 'prenne' = 70-12-94 precedent). Bar: one coherent word-internal
   parse with all five pairs assigned; else fence to the red-team duality
   adjudication without deciding it.
