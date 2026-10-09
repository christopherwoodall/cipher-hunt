# Battery report: val-14-determiner-test (14='le' determiner legs @72/@117/@178)

- Target id: `val-14-determiner-test`
- Claim: "Test 14='le' (determiner) at the surviving legs @72/@117/@178 under the A8
  'ce le [verb]' frame; decides whether the homophony question has battery-grade legs
  before red-team escalation."
- Date: 2026-10-09. Worker: battery worker (agent b3412f9d-ac3a-4a3f-baff-9cf2359340f1).
  Lock `code/crowd17/next-token/locks/val-14-determiner-test.lock` created
  2026-10-09T21:36Z; no prior/stale lock existed; deleted on completion after queue confirm.
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
  (`load_rows` + `parse`). Asserts re-derived in-session: 1,847 pairs, 96 types.
  `canonical.py` never used. R5005 untouched. No invented data.
- Coordinates with (not duplicating): det-14-census (parent PROMOTE, locus-level
  determiner-shape at @117), det-14-locus-117 (KILL of the @117 robustness claim),
  det-14-clitic-178 (PROMOTE: 69 is the subject at @178), le-14-kill-1121 (KILL:
  global 14='le' dead), ce-le-verb-frame (NULL/fence: "ce le [verb]" ungrammatical),
  en14-value-tighten (PROMOTE battery-grade: 14='en' survives tighten, ratification
  pending), stem-14-id (verb-stem-14 fenced lane-wide).

Indexing convention: @-offsets are 0-indexed pair indices into the repaired stream,
citing the 14 pair itself.

## Bar (derived from claim per §2 — queue `bars` field was null; fixed BEFORE testing)

"Test 14='le' determiner at @72/@117/@178 under the A8 'ce le [verb]' frame with
stated values, or fence."

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. Test 14='le' (determiner) at @72 under the "ce le [verb]" frame with stated
   values — the leg survives or dies with stated cause.
2. Test 14='le' (determiner) at @117 ("et [14] [21-noun]") with stated values —
   the leg survives or dies with stated cause.
3. Test 14='le' (determiner) at @178 ("[69-noun] [14] [24-verb]") with stated
   values — the leg survives or dies with stated cause.
4. Decide whether the 14-homophony question (locus-level 14='le' vs 14≠'le'
   elsewhere; §7 red-team venue) has battery-grade legs before red-team
   escalation: PASS iff ≥1 determiner-'le' leg survives at battery grade.

## Method

Fresh byte-exact re-parse of the repaired stream in-work; no prior counts trusted.
All three windows re-read at ±8 pairs with standing values. Standing values used
(none decided here): banked ground truth 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9),
84=on (A15), 47=ce (A4 allophone tier); provisional 59=est, 77="le"; registry
21=["noun","cls"], 24=["verb","cls"], 69=["noun","cls"]; §7 positional rule
(67="veut" iff follower infinitive-shaped). §7 respected: no polyvalence declared.

## Window-level evidence (@-offsets, repaired stream)

- @72 (row a1_02): @64–80 =
  `12 94 92 69 13 24 56 87 14 24 87 11 00 11 29 42 98`.
  The contact: `87 14 24` = "ce [14] [24-verb]" (hapax "87 14").
  - Determiner-'le' dies on two independent grounds: (1) "ce le" stacks two
    determiners — ungrammatical in 1841 French; (2) determiner "le" needs a
    nominal head, but 24 is finite-verb class (registry 24=["verb","cls"],
    R17-009).
  - The claim's A8 "ce le [verb]" frame premise is itself dead: ce-le-verb-frame
    (battery, 2026-10-08/09) found "ce le [verb]" ungrammatical at battery grade
    (bare "ce" cannot subject a lexical verb; cannot stack with an object clitic).
    Adopted as premise, not re-litigated.
  - No rescue: "87 14" has no standing composition ("cele" is no French word);
    a clause boundary "ce le | [24]" leaves an ungrammatical fragment.
  - **LEG DEAD as determiner-'le'.**

- @117 (row a1_03): @109–125 =
  `21 67 93 29 89 68 21 67 14 21 60 90 19 58 66 98 82`.
  The contact: `67 14 21` = "et [14] [21-noun]" (hapaxes "67 14", "14 21").
  - 67='et' by the §7 positional rule (follower 14 is not infinitive-shaped);
    21=NOUN (registry ["noun","cls"]). "et le [21]" = conjunction + determiner +
    noun: clean and grammatical, zero ungranted assumptions.
  - Determiner-shaped: **PASS at class level**. Value 'le': leading, not forced
    (consistent with provisional 77='le' and the 14~77 homophony note).
  - The 'en' rival (14='en' battery promote, en14-value-tighten) is dead at this
    locus: preposition "en" + bare noun is ungrammatical in French.
  - **Caveat (phase-conditionality):** det-14-locus-117 (KILL, 2026-10-09) showed
    the "67 14 21" contact is annihilated under the offset-1 re-phase of row
    a1_03 (67/14/21 all 0×). The leg holds under the standing offset-0 parse
    only. Canonicality caveat stands (row a1_03 offset unvalidated).
  - **LEG SURVIVES as determiner-'le' (class-level, 'le' leading), phase-conditional.**

- @178 (row a1_05): @170–186 =
  `48 21 60 09 87 86 21 69 14 24 87 64 23 37 06 00 33`.
  The contact: `69 14 24` = "[69-noun] [14] [24-verb]" (hapax "69 14").
  - Determiner-'le' dies: determiner "le" needs a nominal head; 24 is
    finite-verb class (registry 24=["verb","cls"]).
  - The clitic-'le' reading is live and separately promoted (det-14-clitic-178:
    69 is the subject; "[69-noun] le [24-verb]" = "l'homme le sait"-shaped) —
    but that is clitic-'le', not determiner-'le'.
  - **LEG DEAD as determiner-'le' (clitic arm live, out of this bar's scope).**

## Per-clause pass/fail

1. @72 tested — **PASS** (determiner-'le' leg dead on two independent grounds;
   A8 frame premise dead, adopted).
2. @117 tested — **PASS** (determiner-'le' leg survives at class level, 'le'
   leading; phase-conditional per det-14-locus-117).
3. @178 tested — **PASS** (determiner arm dead; clitic arm live, adopted).
4. Battery-grade legs for the homophony question — **PASS**: exactly one
   battery-grade determiner-'le' leg survives (@117, with the stated
   phase-conditionality). The escalation is not empty.

## Adverses answered

- le-14-kill-1121 (global 14='le' KILL): consistent — this battery tests
  locus-level only; no contradiction.
- det-14-locus-117 (robustness KILL): recorded as the @117 phase-conditionality
  caveat; the leg stands under the standing offset-0 parse.
- det-14-clitic-178 (PROMOTE): consistent — @178 is clitic, not determiner.
- ce-le-verb-frame ("ce le [verb]" fence): adopted as premise; the claim's A8
  framing is noted as stale (the frame is dead, the locus test proceeds anyway).
- en14-value-tighten (14='en' battery promote, ratification pending): unratified;
  dead at @117 ("en" + bare noun ungrammatical); no contradiction.
- No standing or red-team verdict contradicted, downgraded, or re-litigated.
  §7 intact: battery declares no polyvalence — it packages the question.

## Verdict

**PROMOTE (finding grade):** the 14-homophony question has battery-grade legs
for red-team escalation — one determiner-'le' leg at @117 ("et le [21-noun]",
class-level, 'le' leading), phase-conditional on the standing offset-0 parse
of row a1_03. @72 is dead as determiner-'le' (double-determiner + no nominal
head; A8 frame dead). @178 is clitic-'le', not determiner-'le'.

## Follow-ups

None required (promote, §4). Optional note for the supervisor: the @117 leg's
only remaining vulnerability is the row-a1_03 phase question (det-14-locus-117);
no new target is proposed here because `w3-composition-joint-gate`-style phase
work already covers offset disputes.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-14-determiner-test.md`
- Queue: `val-14-determiner-test` → `status: verdict`, `result: promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique
  tmp `battery-queue.json.val-14-determiner-test.tmp` + atomic rename; disk
  re-validated; own entry only; no downgrade; no tmp leftover).
- Lock: created 2026-10-09T21:36Z (no stale lock), deleted on completion
  (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
- Canonical-stream caveat stands (rows a1_02/a1_03/a1_05 offsets unvalidated).
