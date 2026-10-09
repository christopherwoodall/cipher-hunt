# Battery verdict: seg-par-pour-96-00 — "par pour" (96 00) collocation

Date: 2026-10-09. Worker: a7373be3-da9e-449c-ae85-fc92fa1415be.

## Bar (verbatim from battery-queue.json)

produce one grammatical reading of "par pour" at @47/@465/@960 under standing values (ungrammatical at all three now); else fence the collocation with stated cause

## Bar restated as numbered clauses

- C1: produce ONE grammatical reading of the bare "par pour" sequence covering @47, @465, and @960 under standing values (96="par" granted; 00="pour" A9 leg-1 class-level; all other standing values per BATTERY-PROTOCOL §7). PASS iff a reading parses all three windows with zero ungranted assumptions.
- C2 (else-branch): fence the collocation with stated cause — distributional + grammatical grounds, windows fenced as a systematic residual, no value downgraded.

## Method

Re-derived the full 1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parse per `code/side-keyhunt/repair_parse.py`; asserts re-run: 1,847 pairs, 96 types). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched. Lock created on start with agent id + UTC timestamp.

## Census (byte-exact)

"96 00" occurs exactly 3× stream-wide, all within-row (no row-boundary artifact):

- @47 (row a1_01): `43 81 30 62 96 00 92 79 37 11` → "…pas [62] **par pour** [92] tout [37] la"
- @465 (row a2_10): `87 11 59 42 96 00 33 79 80 06` → "…ce-la est? [42] **par pour** [33=INF] tout [80]…"
- @960 (row a6_00): `85 04 20 67 96 00 86 56 41 19` → "…[20] et **par pour** [86=INF] [56]…"

(67="et" at @959 by the positional rule: 67="veut" iff follower infinitive-shaped; 96="par" is not.)

96 occurs 21× with 12 distinct followers; 00 is its joint-top follower (×3, with 87 ×3, 21 ×3). 00 occurs 55× with 25 distinct leaders. No "00 96" anywhere.

## C1 tested — no grammatical reading (FAIL)

"par" and "pour" are both prepositions requiring complements in French of every period (Littré: "par" governs a nominal/infinitival regime; a bare preposition-preposition sequence is ungrammatical). Candidate rescues, each tested against the three windows:

1. **Ellipsis of par's complement** ("par [X] pour …"): no elidable nominal is supplied by any left context (@47 "pas [62]", @465 "cela est [42]", @960 "[20] et"). Ellipsis is ungranted at battery grade — rejected.
2. **"par" as passive agent attaching left** ("…[participle] par … pour …"): the left elements are not passive participles (62 class-open, 42 noun-class, 67="et") — rejected.
3. **"pour" as the noun "le pour"** (as in "le pour et le contre"): requires article ellipsis, ungrammatical — rejected.
4. **Clause boundary between 96 and 00** ("…par | pour…"): "par" is still complement-less on its left — rejected.
5. **Re-segmentation**: groups are fixed by the repaired parse — rejected.

## Fence (C2 — TAKEN)

The collocation is fenced as a systematic residual with stated cause:

- **96="par" is independently healthy**: it takes complements in 6 other windows — "par ce que" ×3 (@224, @952, @1526; 87="ce" granted, 46="que" ground truth; "par ce que" + clause is fully grammatical 19th-c. French) and "par [21-noun]" ×3 (@230, @1063, @1786). The anomaly is therefore local to the "96 00" trigram, not a second value of 96 (§7: no polyvalence declared at battery level).
- **00="pour" keeps its A9 class-level grant** outside the fenced trigram.
- **The three windows share one shape**: complement-less "par" + "pour" + verbal element (92 / 33=INF / 86=INF). Fenced as one systematic residual, not three independent problems.
- **@46 ("pas 62 par") stays fenced as segmentation-open** per class-62-nof94: this verdict does not unlock it — the collocation blocker stands.

## Coordination

Sibling battery `par-pour-962-adjudicate` (verdict null, report in inbox) fenced the @960 adjacency alone and proposed follow-ups `poly-96-par-adj` and `pour-prefix-00-census`; neither is in the queue (supervisor had not ingested that report at check time). My follow-ups subsume the polyvalence-adjudication proposal with new control evidence; they are written to be queued instead of duplicates.

## Verdict: NULL (fence executed per the bar's else-arm)

No standing verdict contradicted or downgraded. 96 polyvalence NOT declared.

## Follow-up targets (null regenerates work)

1. `par-pour-redteam` (P2): red-team adjudication package — the three fenced "96 00" windows (@47/@465/@960) plus the control legs ("par ce que" ×3 @224/@952/@1526; "par [21]" ×3 @230/@1063/@1786) establishing 96="par" as complement-taking. Subsumes the sibling's `poly-96-par-adj` proposal — queue this one, not both.
2. `contre-00-three-windows` (P2): test 00="contre" at @47/@465/@960 — "par contre" is grammatical 19th-c. French and would dissolve all three windows at once. Promote iff all three parse with zero contradiction on banked neighbors. 00="pour" is A9 class-level, so no battery-level contradiction; escalate to red team if positive.
3. `par-ellipsis-period` (P3): period-diplomatic corpus test for complement-less "par" immediately before "pour" (ellipsis of par's complement). Kill the ellipsis rescue iff no 17th–19th c. parallel exists; if a parallel exists, re-open the collocation under the ellipsis reading.

## Bookkeeping

- Report: this file.
- battery-queue.json: `seg-par-pour-96-00` → status `verdict`, result `null`, date 2026-10-09 (temp-file + rename; own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated after write).
- Lock `locks/seg-par-pour-96-00.lock`: created on start, deleted on completion.
