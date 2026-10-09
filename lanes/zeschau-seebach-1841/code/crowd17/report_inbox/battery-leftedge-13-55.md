# Battery report: leftedge-13-55

Target: `leftedge-13-55`. Claim: "resolve 13's and 55's classes to fix the left
edge shared by both 61-94 windows (78-45-13-55-61-94 formula x2)".
Date: 2026-10-09. Worker: battery worker (supervisor dispatch).
Lock `locks/leftedge-13-55.lock` created 2026-10-09T06:16:36Z (no pre-existing
lock); deleted on completion.

Offset convention: @n = 0-based pair index in the repaired 1,847-pair stream
(matches battery-seg-55-61-21-stem, battery-class-55-det, battery-value-13-third-arm).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve 13's and 55's classes; gates the word-boundary decision for seg-55-61-94-word"

Numbered clauses (frozen; not modified after seeing data):

1. 55's class resolved (word-internal syllable vs separate word), verified at
   the two formula windows.
2. 13's class resolved (or narrowed with stated open questions and ownership).
3. The word-boundary decision for seg-55-61-94-word stated as a gated
   consequence (the [55-61][94] vs [55-61-94] segmentation at both windows).

Adverses: none stated.

## Method

Read BATTERY-PROTOCOL.md and battery-queue.json first. Re-derived the repaired
1,847-pair stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (byte-exact stride-2 pairing per row
offset); asserted 1,847 pairs before testing. `canonical.py` never used.
R5005, sealed gates, red-team queue untouched. Every count below re-derived
in-session; no prior counts trusted.

## Standing state (used as premises, not re-litigated)

Four verdicts landed 2026-10-09, after this target was queued, and they decide
most of the bar:

- `seg-55-61-21-stem` PROMOTE: 55-61 = "prend" (bare finite stem) at W3
  (@1205, `43 55 61 21`); "the UNIT (55-61-94 as a 'prenne'-family word where
  94 occurs) survives"; indicative/subjunctive alternation prend/prenne.
- `class-55-det` KILL: 55 is not a separate determiner word (W3 forces
  word-internal "prend"; §7 sole-polyvalence bars a separate-at-11 /
  word-internal-at-1 split). Non-determiner separate-word classes also fail
  (this report: 55='sans' fails at 55-61 x3 since 61 is finite "prend" there;
  55='de'/'à'/'en' fail at "que [55]" @550).
- `subj-13-value` KILL + `pronoun-13-les` KILL: both French "les" arms for 13
  dead (determiner, object pronoun; the latter killed at the @567 wall: 76 is
  a battery-promoted noun that can never host a preverbal clitic).
- `value-13-third-arm` KILL (2026-10-09): no UNIFORM word-level non-'les' value
  exists for 13 (15 candidates tested, all fail; the @567/568 wall kills 9).
  Surviving space: sub-lexical 13 or a §7 split — both red-team territory.

## Window-level evidence

### The formula x2 (byte-verified)

`78-45-13-55-61-94` starts at 0-based @573 (row a3_02) and @1164 (row a6_09).
Exactly 2 occurrences stream-wide. Differing only in 94's follower
(82 @578 vs 87 @1169).

- W1 @573: `94 52 87 | 78 45 13 55 61 94 | 82 06 06 50`
  = "[52] ce(87) [78-45] [13] [55-61] [94] m(82) ent(06) ent(06) [50]"
- W2 @1164: `83 21 67 | 78 45 13 55 61 94 | 87 83 21 85`
  = "[83] [21] [67] [78-45] [13] [55-61] [94] ce(87) [83] [21] [85]"

### 55: word-internal (clause 1)

- Bigram `55-61`: exactly 3x stream-wide — @576 (W1), @1167 (W2), @1205 (W3,
  promoted "prend"). Followers: 94, 94, 21. 55 never pairs with 61 outside
  the prendre family; 61 never takes 55 outside it either (61's other 15
  windows have 14 distinct predecessors, 55 x3 the max).
- At both formula windows 55-61 sits in the prendre context (followed by 94,
  the "prenne"-family position per seg-55-61-21-stem clause 2). No
  formula-window evidence contradicts word-internal 55: a separate-word 55
  would need 13 to license it ("[13] [55-det] [61]"), and 13's value is open
  with both determiner-licensing arms ('les') killed.
- Per §7 uniformity (class-55-det KILL), W3's promoted one-word "prend"
  fixes 55 as word-internal at all 12 windows. 55's class = RESOLVED:
  word-internal syllable, the prendre-stem initial ('pre'-part; the internal
  letter split re-pren-ne vs pre-nd is the standing red-team residual from
  seg-55-61-21-stem, not re-opened here).

### 94-boundary: follower-determined (clause 3, new)

- W1 @578-581: `94 82 06 06` = "ne(94) mentent(82-06-06)" — "ne mentent" is a
  clean negation frame (w1-573-subject's "ne mentent" 3pl; 94='ne'
  battery-promoted). The rival join [55-61-94]="prenne" gives "prenne
  mentent" (subjunctive 3sg + indicative 3pl, two verbs) — ungrammatical.
  W1 boundary: [55-61][94='ne']. FIRM.
- W2 @1169: `94 87` = "ne ce" — ungrammatical (negation proclitic "ne" can
  never be followed by demonstrative "ce"; 87='ce' granted via cela-87-11).
  `94-87` occurs exactly ONCE stream-wide (@1169): no corpus rescue.
  Therefore 94 != 'ne' at W2. Live options: (i) [55-61-94] joined as
  "prenne" (subjunctive; "...prenne ce..." grammatical per
  seg-55-61-94-word, but the trigger is open — 13='que' is §7-blocked since
  46='que' is banked, and no other trigger is byte-evidenced); (ii) 94 = a
  non-'ne' value X ("[55-61=prend] [94=X] ce..."). The "87-83 = cède" rescue
  fails (two-verb pile-up either way: "prend ne cède" / "prenne cède").
  W2 boundary: [55-61-94] joined, "prenne"-reading leads with trigger open.

So the formula has NO single 94-boundary: W1 splits ([55-61][94='ne']),
W2 joins ([55-61-94]="prenne"). The variation is inflectional (prend + ne
vs prenne — same lexeme, mood-conditioned segmentation per
seg-55-61-21-stem's alternation note), not a 55-class split: the [55-61]
unit holds at both windows. Formal declaration is red-team venue (§7);
recorded here as window-level fact.

### 13: narrowed, not resolved (clause 2)

- Re-derived profile: n=12. Followers: 24 (finite verb, promoted) x3,
  93 (verb-shaped, promoted) x2, 66 x2, 55 (word-internal → prendre-verb)
  x2, 76 (noun, promoted) x1, 52 x1, 92 x1. Predecessors: 65 (noun-class)
  x3, 69 x2, 45 x2, 00/97/95/35/99 x1.
- 13 is preverbal in 7/12 windows (24x3, 93x2, 55x2). The @567 wall
  (`97 13 76`, 76 = promoted noun) fences every preverbal-only candidate.
- Standing kill (value-13-third-arm, today): no uniform word-level value
  exists; sub-lexical 13 or §7 split — red-team territory. This battery
  does not re-litigate it. 13's class = OPEN at battery level.
- Left-edge note (not a decision): `78-45` x4 stream-wide (@313, @573, @982,
  @1164); 78 is noun-shaped ("le [78]" x7 via provisional 77='le').
  "ce(87) [78-45]" @573 and "[21] et(67) [78-45]" @1164 read naturally as
  "ce verdict" / "et verdict" under the 45='dict' rival (78='ver' LEAD).
  The 45='ce'-HOLD vs 'dict'-rival fork is owned by
  fork-78-45-adjudication (NULL) — the [78-45]|[13] boundary is not decided
  here, and 13's sub-lexical-vs-split question sits with the red team.

## Per-clause pass/fail

1. 55's class resolved — **PASS**. Word-internal prendre-stem syllable;
   standing PROMOTE (seg-55-61-21-stem) + KILL (class-55-det) + §7
   uniformity; verified at both formula windows with no contradiction.
2. 13's class resolved — **FAIL** (attempt complete, negative result, not
   ignored). Narrowed to preverbal particle (7/12) with the @567 noun-wall
   fenced; no uniform word-level value exists per today's standing kill
   (value-13-third-arm); sub-lexical or §7-split = red-team territory.
3. Word-boundary decision gated — **PASS**. [55-61] is one word uniformly
   (the [55][61] split is dead — gates seg-55-61-94-word's core question);
   the 94-boundary is follower-determined per window: W1 [55-61][94='ne']
   ("ne mentent" firm), W2 [55-61-94] joined ("ne ce" ungrammatical forces
   94 != 'ne'; "prenne"-join leads, trigger open).

## Verdict: NULL

Clause 2 is not resolvable at battery level (13's uniform-value question was
closed today by a standing kill; the surviving space is red-team venue), so
the bar's conjunction does not fully pass. Not kill: no window forces the
bar's claim false — 55 resolved cleanly and the boundary decision is
delivered. No standing verdict contradicted, none downgraded, none
re-litigated (all 2026-10-09 kills/window-reads used as premises only).

## Follow-ups proposed (null regenerates work; ids verified absent from queue)

1. **`w2-1167-prenne-trigger`** (P3): resolve the subjunctive trigger for
   W2's joined "prenne" (`78 45 13 55 61 94 87 83 21` @1164-1172). Bars:
   (a) one grammatical "...[13] prenne ce [83] [21]..." parse with the
   trigger stated; (b) the trigger may not be 13='que' (§7; 46='que'
   banked) — name it or fence the "prenne" reading; (c) if no trigger,
   route to val-94-w2.
2. **`val-94-w2`** (P3): test 94 = non-'ne' value at W2 (@1169 — the sole
   "94-87" window stream-wide; "ne ce" ungrammatical). Bars: name X with
   >=2 independent windows where 94=X parses, or kill (then the
   "prenne"-join stands as the only grammatical option).
3. 13's class: owned by value-13-third-arm's proposed follow-ups
   (`letter-13-verdicts`, `split-13-redteam`, `noun-97-568` — proposed in
   that report for supervisor queuing, not yet in the queue); not
   re-proposed here to avoid duplication.

## Bookkeeping

- Report: this file (`code/crowd17/report_inbox/battery-leftedge-13-55.md`).
- `battery-queue.json`: `leftedge-13-55` queued -> verdict/null via
  temp-file + rename (pre-write assert confirmed queued/verdictless; JSON
  re-validated post-write). Own entry only.
- Lock `locks/leftedge-13-55.lock` created on start, deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Standing §7 constraints respected throughout; 67 et/veut remains the sole
  polyvalence (no new value declared — "prenne"/"prend" is one lexeme).
