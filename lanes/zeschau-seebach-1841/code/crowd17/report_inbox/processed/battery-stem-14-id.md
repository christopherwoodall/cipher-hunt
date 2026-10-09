# Battery report: stem-14-id — name the la-frame stem at @1122

Worker: bb253060-203f-4c12-b3f1-616f90299c7c | 2026-10-09T05:14Z (lock
`locks/stem-14-id.lock` created on start, deleted on completion; no prior
lock existed; no stale lock).

Target: `stem-14-id` (priority 3). Claim: name the la-frame stem at @1122.

## Bar (verbatim, pre-registered before testing)

"name 14's value iff its contact profile matches a verb stem with the @1122
frame parsing; else fence with stated cause"

Numbered clauses (fixed before data examination):

- C1: 14's contact profile matches a verb stem AND the @1122 frame parses
  with 14 as the stem ("[14]ent la" = verb+object) → name 14's value.
- C2 (else): fence with stated cause (no value named).

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(1,847 pairs, 96 distinct groups — re-verified this run). `canonical.py`
never used. R5005 untouched. @-offsets are 0-based pair indices (queue
convention: the queue's "@1122" = 14 at index 1121; the la-frame surface is
`14-06-11` @1121–1123, row a6_07). Every number re-derived, none trusted.
Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9), 84=on
(A15), 47=ce (A4); promoted 06=ent (ent-06), 94=ne, 30=pas, 12=n (letter);
provisional 59=est, 77=le; 24=finite-verb class (R17-009 stands; the
24-en-verb-conflict is queued for red team — 24's verb class used only as
granted). 1841 diplomatic French throughout.

Standing battery premises used as premises (not re-litigated):
- tout-slot-14 (null, 2026-10-08): 14 n=15 census; B4 @1121 fenced as
  structural anomaly; verb/infinitive rival "live but not demonstrated".
- breaker-b4-1121 (null, 2026-10-09): @1121 resolved window-locally as
  "…prennent souvent la…" with 14 word-internal in "[14]ent".
- souvent-14-06-retest (KILL, 2026-10-08): the "sou" spelling is dead —
  "souent" ≠ "souvent" under standing 06="ent" — at @84 AND at @1121.
- le-14-kill-1121 (KILL, 2026-10-09): 14='le' killed as a global value at
  @1121 at kill grade; 14~77 'le'-homophony battery MOOT; surviving 'le'
  legs (@72/@117/@178) escalated as a homophony question (red-team venue).
- prennent-70-12-06 (KILL, 2026-10-08): the subject-agreement reading of
  "11 88 70 12 06" forced false; the verb's subject stays an open
  left-edge question.

## Window-level evidence (fresh re-derivation)

14 census: n=15 @72, 84, 117, 141, 178, 339, 424, 458, 586, 623, 813, 896,
1121, 1365, 1689 — matches tout-slot-14 exactly. Predecessors: 87, 16, 67,
66 x2, 69, 31, 47, 18, 82 x2, 65, 06, 79 x2. Successors: 24 x2, 06 x2, 21,
74, 45, 62, 02, 00, 59, 29, 98, 60 x2.

The @1121–1127 surface (row a6_07): `70 12 06 | 14 | 06 11 52 37 43`
= "pre n ent [14] ent la [52] [37] [43]".

Verb-stem test of the @1122 frame (C1's first conjunct):

1. The verb+object parse ("[14]ent la") is dead at this window. It needs
   "…ent [14]ent la…" = two adjacent finite 3pl verb forms with no
   boundary marker — ungrammatical in 1841 diplomatic French, and no
   clause boundary is evidenced (mid-row a6_07 both sides; breaker-b4-1121
   C1 failed). CORRECTION (recorded, not hidden): the ent-06 battery's
   "@1122 parses ONLY as verb+object" is superseded — it predates the
   B4 resolution and the spelling kill below.
2. The rival adverbial parse ("souvent la", breaker-b4-1121 window-local)
   is spelling-killed: 14="sou" + 06="ent" = "souent" ≠ "souvent"
   (souvent-14-06-retest, kill grade, @84 and @1121). The "[14]ent"-adverb
   SHAPE is not ruled out, but no spelling of it survives.
3. 14='le' (determiner/clitic) is killed as a global value at @1121 at
   kill grade (le-14-kill-1121); "…ent le ent la…" has no grammatical
   parse.
4. Net at @1121–1123: no value parses "06-14-06-11" cleanly at battery
   grade. The frame is a segmentation residual, not a verb frame.

Verb-stem test of the wider contact profile (C1's second conjunct) —
verb-hostile windows (bare 14 where a stem would need an ending, or a
finite verb where a stem cannot stand):

- @72 `87 14 24` = "ce [14] [24-verb]" (24 finite-verb class, R17-009):
  bare 14 before a finite verb. Clean under 14='le' (A8 "ce le [verb]"
  frame); ungrammatical as a verb stem. VERB-HOSTILE.
- @178 `69 14 24 87` = "[69] [14] [24-verb]": same shape. VERB-HOSTILE.
- @623 `82 14 59` = "m [14] est" (59='est' provisional): "me [stem] est"
  ungrammatical. VERB-HOSTILE.
- @586 `18 14 00` = "[18] [14] pour": finite stem + "pour"
  ungrammatical. VERB-HOSTILE.
- @1365/@1689 `79 14 60` = "tout [14] [60]": verb killed inside the
  tout-frame (frame-62-94-79, standing premise). VERB-HOSTILE x2.
- Predecessor 67='et' @117 ("et [14] [21]"): conjunction before a bare
  stem — no verb parse; grammatical under determiner ("et le [21]").
- Successor 45='ce' @339 (`31 14 45`): no verb parse either ("[stem] ce").

Verb-leaning fragments (insufficient, accounted for):

- `14-06` x2 (@84, @1121): @1121's is the killed residual above; @84
  (`16 14 06 88` = "[16] [14]ent [88]") is unfalsified but
  undemonstrated (16/88 open) — a shape, not a parse.
- @813 `14 29` = "[14]er" (29='er' banked): infinitive-shaped, but the
  infinitive rival "fails @72, @178, B1, B4 as a verb" (tout-slot-14,
  standing) — an infinitive at @813 does not license a finite stem at
  @1122, and the @1122 finite parse is independently dead (items 1–4).

## Per-clause pass/fail

- C1 (profile matches a verb stem with the @1122 frame parsing → name the
  value): FAIL. The @1122 frame admits no verb-stem parse (verb+object
  dead, "souvent" spelling-killed, 'le' killed at this window), and 7 of
  15 windows are verb-hostile at the contact level (@72/@178/@623/@586/
  @1365/@1689, plus the 67='et' predecessor). No French word can be named
  for 14 on this evidence.
- C2 (else: fence with stated cause): TAKEN.

## Fence (stated cause)

14's value is NOT named. Cause: (a) the @1122 "la-frame" dissolves on
inspection — "14-06-11" is not "[stem]ent la" (verb+object): the finite-
verb adjacency is ungrammatical with no evidenced boundary, the
"souvent la" re-parse is spelling-dead ("souent"≠"souvent", kill grade),
and 14='le' is kill-grade dead at this window; the surface stands as a
segmentation residual. (b) The n=15 contact profile is verb-hostile at a
majority of decidable windows (listed above); the only verb-shaped
fragments are the @1121 residual itself and the undemonstrated @84
shape. (c) 14's global value stays open: the surviving 'le'-legs
(@72/@117/@178) are homophony-question evidence per le-14-kill-1121's
escalation — a red-team venue under §7 (67 et/veut sole polyvalence),
not a battery naming.

## Adverses

"14's class open" — ANSWERED, not ignored: class remains open globally;
at @1121–1123 14 is fenced as sub-word-level inside a segmentation
residual (no battery-grade value); the homophony question is escalated,
not decided here. No red-team verdict is contradicted (none touches
14); no standing verdict is downgraded (the three kills and two nulls
above are used as premises); R5005, sealed gates, and the red-team queue
untouched.

## Verdict

**null** — C1 fails; per the bar's else-branch the target fences with
the stated cause above. No value is named for 14. Work regenerates
below; none of the follow-ups duplicates a queued target
(verb-14-rival, le14-adj60-tail, clitic-14-82-breakers, det14-elsewhere,
stem-68-id, frame-62-94-79-reparse all already queued; souvent-14-06-
retest, prennent-70-12-06, le-14-kill-1121 already at verdict).

## Follow-ups (null regenerates work; 3 proposed)

1. **la-frame-52-37-43-noun** (priority 3). Claim: the byte-identical
   "11-52-37-43" tail shared by @1123 and @1721 (re-derived this run:
   `70-12-06-14-06-11-52-37-43` and `30-64-47-68-06-11-52-37-43`) is one
   noun phrase. Bars: "name the 52-37-43 phrase value iff it parses as a
   single noun phrase under 'la' identically in both windows with one
   stated segmentation; the stem slots (14/68) inherit shape constraints
   from the result; else fence the tail as formulaic." Evidence: the
   tail is byte-identical across the only two la-frames; naming it
   constrains both residual stems without re-litigating 14's class.
   Adverses: 52/37/43 values open; @1121's head is a segmentation
   residual (this report).
2. **ent14ent-residual-adjudicate** (priority 2). Claim: the "06-14-06"
   residual @1121 is resolvable. Bars: "resolve iff a single segmentation
   of @1118–1127 parses fully under standing values with ≤1 stated
   assumption naming 14's sub-word role; else confirm as an unresolvable
   segmentation residual and fence 14's @1122 value permanently."
   Evidence: verb-stem dead, "sou" spelling dead, 'le' dead at this
   window (three standing kills); the residual is now the binding
   constraint on 14's global value. Adverses: 88/16 open at the left
   edge; 52-37-43 open at the right.
3. **stem-14-84-retest** (priority 3). Claim: @84 (`16 14 06 88`) is
   14's last verb-shaped window. Bars: "name 14's class iff @80–90 parses
   as subject+verb+complement under a verb-stem 14 with 16/88
   class-consistent and ≤1 stated assumption; else fence 14's verb class
   lane-wide." Evidence: last verb-shaped 14 window standing after the
   @1122 verb parse died; 16 verb-class + 88 verb/governor-class are
   supported/standing per souvent-14-06-retest C2. Adverses: 16/88
   values open; single-window evidence only.
