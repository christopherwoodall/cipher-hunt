# Battery report: seg-92-354-356 — @354/@356 '40 92 98 92' segmentation

- Target id: seg-92-354-356
- Worker: battery-worker-seg-92-354-356 (session d6edcf6c-3347-48d3-b96e-48d356da5ec8)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs verified in-worker). `canonical.py` not used. R5005 not touched.

## Bar (verbatim, pre-registered from battery-queue.json before testing)

"resolve iff one segmentation parses both windows with <=1 non-granted value assumption; else fence"

Numbered pass/fail clauses:

1. **(C1)** There exists a segmentation S of the run @353–356 ("40 92 98 92") —
   word-internal (no inner word boundary) or two-word (at least one inner word
   boundary) — such that BOTH windows (@354 and @356) parse as grammatical
   French under S, using granted/banked values freely plus at most ONE
   non-granted value assumption in total across both windows. PASS = claim
   resolves (promote).
2. **(C2)** If C1 fails, the target is fenced: the fence is recorded with the
   blocking cause (which values are open, which segmentations were tried and
   why each fails). PASS = fence recorded (verdict null).

"Granted" = §7 standing values (banked pencil, red-team A-series grants,
provisional 59/77, battery-promoted values where noted). The killed 09/92
'-ere' value is NOT used or re-litigated (per adverses).

## Method

1. Rebuilt the repaired stream in Python per `repair_parse.py`; asserted 1,847 pairs.
2. Located the run: @353=40, @354=92, @355=98, @356=92, all on row a2_06.
   Left context @349–352: 94 74 67 78. Right context @357–365:
   47('ce') 11('la') 21 62('il') 48('e'-letter) 76 47 78 48.
3. Enumerated all 8 inner-boundary placements over @353–356 (S0–S7, §Evidence).
4. Tested each placement twice: (a) strict §7 reading (98 value-open, per the
   target's pre-registered adverses); (b) granting battery-grade 98='vient'
   (vient-98-name, promoted 2026-10-08) to check whether the fence survives it.
5. Counted non-granted value assumptions per placement; checked French
   grammaticality of each resulting word string.

## Window-level evidence (@-offsets)

- @354 = 92 (row a2_06). Predecessor @353 = 40 ('e', banked letter).
  Successor @355 = 98. Bigram "40 92" occurs exactly 1x in the stream (here).
- @356 = 92 (row a2_06). Predecessor @355 = 98. Successor @357 = 47 ('ce',
  A4 allophone tier), @358 = 11 ('la'). "47 11" occurs 3x (@269, @357, @498)
  and reads "cela" via allophony (cf. granted "cela" = 87-11, x7). The word
  boundary before @357 is common ground for all segmentations.
- "92 98" x1, "98 92" x1, "92 47" x1 — all hapaxes, all inside this run.
  The 4-gram "40 92 98 92" occurs exactly 1x. 92-92 adjacency: x0.
- This run is 92's ONLY contact with 98 in the whole stream (98's sole
  92-predecessor is @355; 98's sole 92-follower is @356). It is also 98's only
  92-contact (n(98) = 40; predecessors 62x5, 42x3, 66x3, 98x3, …; followers
  83x5, 82x3, 80x3, 98x3, 00x3, …).
- 92: '-ere' value KILLED (A6, hold-09-92); tripartite governor profile
  (verbal/nominal/finite) under red-team adjudication (split-92-adjudication,
  null 2026-10-08); verb-92-subset promoted as CLASS only (00-governor
  subset). 92 has no granted VALUE.
- 98: battery-grade 98='vient' (finite semi-auxiliary, vient-98-name, promoted
  2026-10-08) with fenced adverses (doubled-98 x3, @1139 infinitive 'venir');
  prof-98 promoted 2026-10-09 (verb-frame class). Not a §7 grant.
- 40 ('e' letter): n=21; "29 40" x9 = "er"+"e" analytic "-ere" spelling
  (control: letters glue word-internally). 40's followers take granted values
  8/21 — no clean word-final prior (see follow-up 3).

Segmentation placements over [40, 92, 98, 92] (outer boundaries fixed:
after @352, before @357):

- S0 word-internal: [40 92 98 92] one word.
- S1: [40] [92 98 92] · S2: [40 92] [98 92] · S3: [40 92 98] [92]
- S4: [40] [92] [98 92] · S5: [40] [92 98] [92]
- S6: [40 92] [98] [92] · S7: [40] [92] [98] [92]

## Per-placement results

Reading (a) — strict §7 (92 value-open, 98 value-open):
every placement needs a value for 92 AND a value for 98 (the two pairs are
distinct; no granted value exists for either) = at least 2 non-granted value
assumptions, over the ≤1 budget. C1 fails on budget alone.

Reading (b) — granting battery-grade 98='vient' (the stronger test, since the
target's adverses predate/ignore that promotion):
- S0: "e-[92]-vient-[92]" — one word with a finite verb inside it. Ungrammatical.
- S1: "e" alone is not a French word; "[92]-vient-[92]" has a finite verb inside. Fail.
- S2: "e[92] vient[92] cela" — 'vient' is intransitive; trailing "[92]" has no
  grammatical slot (would need 92 = adverb, unsupported by 92's profile, and a
  second role for 92). Fail.
- S3: "e-[92]-vient" — word ending in a finite verb. Ungrammatical.
- S4: "e" alone fails (as S1).
- S5: "e" alone fails; "[92]-vient" ends in a finite verb. Fail.
- S6: "e[92] vient [92] cela" — "vient [92]" needs 92 as a standalone adverb
  word (non-granted, profile-inconsistent), while W1 needs 92 word-final after
  'e' — two inconsistent roles for one value, over budget. Fail.
- S7: "e" alone fails (as S1).

No placement parses within budget under either reading.

## Per-clause pass/fail

- **C1: FAIL.** Under strict §7 the budget is unsatisfiable in principle
  (two value-open pairs, budget of one). Even granting battery-grade
  98='vient', all 8 placements fail — four strand a finite verb inside a word
  (S0, S1, S3, S5), three need the standalone letter "e" as a word (S1, S4,
  S5, S7), and the two survivors (S2, S6) die on 'vient' intransitivity plus
  budget/role inconsistency.
- **C2: PASS.** Fenced with cause: (1) 92's value is open (tripartite
  adjudication pending; '-ere' killed and not re-litigated); (2) 98's value is
  open under §7 (battery-grade 'vient' does not rescue any placement);
  (3) the "92 vient 92" sandwich admits no grammatical segmentation at
  battery level.

## Verdict

**null (fence)** — the segmentation does not resolve at battery level. Not a
kill: no window forces the disjunctive claim false; the word-internal
alternative dies only conditional on battery-grade 98='vient' (not §7), and
the two-word alternative is underdetermined, not refuted. Untouched: A6
(09/92 '-ere' kill), split-92-adjudication (red-team queue), vient-98-name
(battery promote stands), 47='ce' (A4), 87-11 'cela' compositional grant.
No standing red-team verdict is contradicted, so no null-escalation triggers.

Adverses answered (none ignored):
- 92's killed '-ere' value NOT re-litigated: no placement uses or tests it;
  the fence never depends on it.
- 98 open: tested under both readings (open per §7; 'vient' per battery
  promotion). The fence holds under both, so the adverse is answered, not
  sidestepped.

## Follow-up targets (null regenerates work)

1. **seg-92-354-356-retest** (gate: red-team adjudication of
   split-92-adjudication). Re-run this bar once 92's value is named: with 92
   granted, the budget covers 98 alone and placements S2 ("e[92] vient[92]")
   and S6 ("e[92] vient [92] cela") become the discriminating frames. Bar:
   "resolve iff one segmentation parses both windows with <=1 non-granted
   value assumption (92's adjudicated value granted); else fence."
2. **vient-98-355-transitivity.** @355 is the stream's only "92 98 92"
   sandwich — the hardest window for battery-grade 98='vient': an
   intransitive verb flanked by two unknowns. Census 98's nominal-subject
   windows elsewhere (n(98)=40; predecessors 62x5, 42x3, 66x3…); if 'vient'
   never takes nominal subjects, @355 is kill-grade adverse material against
   vient-98-name — escalate to the red team.
3. **boundary-40-letter-census.** Classify all 21 of 40's windows as
   word-final-letter vs word-internal-letter using granted-value neighbours
   ("29 40" x9 analytic "-ere" as the word-internal control). Yields a prior
   for 40|92 boundary placement, reusable for other segmentation targets.

## Worker notes

- Lock `code/crowd17/next-token/locks/seg-92-354-356.lock` created on start,
  deleted on completion (this report).
- No numbers invented: every count re-derived from the repaired 1,847-pair
  stream in-worker. 98's profile (n=40, predecessor/follower censuses) and
  40's profile (n=21) computed fresh, not copied from finder reports.
