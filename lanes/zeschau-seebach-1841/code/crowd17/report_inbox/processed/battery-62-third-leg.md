# Battery verdict: 62-third-leg

**Verdict: NULL** — no third independent noun frame-leg for 62 at battery grade.
Two held legs re-verified; class stays open (2 legs < lane ≥3-leg standard).

## Bar (verbatim from battery-queue.json)

> promote 62=noun-class iff >=3 independent frame-legs (two held:
> subject+'ne'+verb @761/@1772/@1329, que-relative head @1482); seek a clean
> article/determiner contact or a direct-object slot; then re-test 'pas de [62]'
> @1327.

Numbered clauses (frozen before testing):
- **B1:** a third independent noun frame-leg exists — either a clean
  article/determiner contact for 62, or a direct-object slot (verb immediately
  before 62) on standing values.
- **B2:** (conditional on B1) re-test the 'pas de [62]' window @1327
  (`30 06 62 94`) with a nominal X available.

## Method

Replicated `repair_parse.py` tokenization inline (1,847 pairs; `canonical.py`
never touched; R5005, sealed gates, red-team queue untouched). Full census of
62's 35 windows with @-offsets, re-derived (not cited): left-neighbor and
right-neighbor distributions; article/determiner contact against standing set
{11=la, 77=le (provisional), 87=ce, 47=ce} plus 79=tout (A5); direct-object
search against granted/provisional verb inventory {24 finite, 31 VERBAL,
33/86 INF, 32 verb lexeme, 67 veut-positional}. Held legs re-verified, not
re-litigated. Coordination: frame-20-62-94 owns 20's noun-leg (not touched);
spell-pasent-test owns the 30-06 "passent" spelling hypothesis (not duplicated).

## Window-level evidence (@-offsets, all re-derived)

62 n=35. Predecessor distribution: 93,30,51,21(x5),36,14,10,77,03(x2),20(x4),
74(x3),40,08(x2),78(x2),04,06,34,92(x2),02,98,41.

### B1a — article/determiner contact: NOT FOUND (clean)

- Article set {11,77,87,47} as predecessor: **1/35** — @508
  `21 67 77 62 94 64 98` = "...67 le[77] [62] ne[94] qui[64]...".
  Not clean: 'le' may be the object pronoun, and the article+noun parse
  strands on "ne qui" (94='ne' STRONG LEAD requires a verb; 64='qui' granted
  is not one). A word-internal rescue ("le [62ne] qui…") would need
  62-94 re-segmented — a 94-segmentation question owned by
  redteam-94-functional-split (queued), not decidable here. Recorded, not
  promoted.
- Article set as follower: **0/35**.
- Determiner via 79='tout': **0/35** either side.

### B1b — direct-object slot: NOT FOUND

- Verb-shaped predecessor of 62 on standing values: **0/35**. None of
  {24,31,33,86,32,67} ever immediately precedes 62.
- (98='vient' is battery-level only, unratified — not a standing value;
  see follow-up 1.)

### Held legs re-verified (not re-litigated)

- Leg 1 (subject of negated finite verb), all three windows grammatical:
  @761 `29 40 20 62 94 59 39` = "[20] [62] ne[94] est[59]" ("62 n'est…",
  59='est' provisional, budgeted); @1772 `26 37 78 62 94 24 87` =
  "[62] ne[94] [24-finite-verb]" (24 granted); @1329 `56 30 06 62 94 70 52`
  = "[62] ne[94] pre[70]…" ("62 ne pre[nd]…").
- Leg 2 (que-relative head): @1482 `82 16 98 62 46 77 84` =
  "[62] que[46] le[77]…" ("the 62 that…"; 46='que' ground truth,
  77='le' provisional).

### Supporting / negative evidence (recorded, not legs)

- 'qui 62' / 'ne 62': **x0** in 35 windows (no 64/94 predecessor) —
  supporting negative evidence against verb-class, per the bar not a leg.
- '62 qui' (62 followed by 64): **x0** — asymmetric vs 65's "65 qui" x3
  (prof-65 leg). Noted for the lane.
- 62='il' remains dead per frame-20-62-94 (ungrammatical in ≥7/35 windows);
  no value named for 62. Cited, not re-run.

### B2 — @1327 re-test: NOT RUN at grade

Window @1327: `30 06 62 94` (a7_04) = "pas[30] ent[06] [62] ne[94]"
(06='ent' standing; de/ne readings of 06 settled NULL by
noun26-1560-06-value, not re-litigated). With B1 failed, X=62 cannot be
confirmed nominal — the window keeps the status the ellipsis battery left it:
open. The "passent" spelling hypothesis belongs to spell-pasent-test
(queued); not duplicated here.

## Per-clause pass/fail

- **B1: FAIL (inconclusive, not kill-grade)** — no clean article/determiner
  contact (1/35 ambiguous @508; 0/35 via 79); no direct-object slot (0/35
  verb predecessors on standing values). Nothing forces 62 non-noun; the
  evidence is insufficient, not contradictory.
- **B2: NOT RUN** — conditional on B1; deferred to follow-ups.

## Verdict: NULL

62 holds two noun frame-legs (subject+'ne'+verb x3 windows, que-relative
head), below the lane's ≥3-leg class standard. No standing verdict
contradicted or downgraded. R5005, sealed gates, red-team queue untouched.

## Adverses (answered, none ignored)

(a) "coordinate with frame-20-62-94 (do not re-litigate 20's noun-leg)":
honored — 20's class not adjudicated; 20-62-94 windows used only
positionally; 62='il' kill cited, not re-run.
(b) "62's zero verb-slot hits ('qui 62'/'ne 62' x0 in 35 windows) is
supporting, not a leg": confirmed x0 on the repaired stream (no 64/94 among
35 predecessors; no 64 among 35 followers); treated as supporting negative
evidence only.

## Follow-ups (null regenerates work)

1. **subj-62-98-affirmative** (P2): test "62 98" x5
   (@11 `93 62 98 76`, @802 `74 62 98 53`, @945 `08 62 98 96`,
   @1136 `20 62 98 00`, @1324 `08 62 98 56`) as affirmative subject frames
   ("[62] vient…") — an independent third leg — **once 98='vient' is
   red-team-ratified**. Do not run before ratification; 98 is currently
   battery-level only.
2. **det-62-508-reseg** (P3): adjudicate @508's article contact under
   word-internal 62-94 ("le [62ne] qui…", grammatical) vs two-word
   "le [62] ne[94] qui" (ungrammatical, strands). Hinges on 94-segmentation;
   coordinate with redteam-94-functional-split (queued) — do not duplicate.
3. **do-62-verb-inventory** (P3): re-run the direct-object census when the
   standing verb inventory adjacent to 62 grows (currently 0/35 verb
   predecessors on granted/provisional values). Narrowly scoped re-test, not
   a fishing expedition.
