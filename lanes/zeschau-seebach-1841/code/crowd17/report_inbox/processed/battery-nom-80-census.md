# Battery `nom-80-census` — verdict: NULL

## Bar (verbatim, pre-registered)

> "name a nominal 80 leg with <=1 unstated assumption; a pronoun-like or determined leg re-opens @1596 within the x29-80-1596-nominal budget"

Restated as numbered clauses (before testing):
- **C1:** at least one 80-window yields a nominal-shaped (noun / pronoun / determined) reading of 80 with ≤1 unstated assumption → name the leg (PROMOTE).
- **C2:** else, fence the nominal-80 route at battery grade (NULL), with per-window stated cause.
- **C3 (conditional consequence):** if C1's leg is pronoun-like or determined, re-open @1596 within the x29-80-1596-nominal budget.

No adverses listed on the queue target.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py`. `canonical.py` never used.
All 80-windows censused byte-exact (0-based offsets, row-validated); n(80)=17,
matching the `inf-97-567-adjudicate` census. Priority frames verified:
"03 29 80" exactly 3× (@1032/@1322/@1596), "21 80 77" at @720.

Standing premises: protocol §7 + R19 rulings R19-120 (80 global class stays
verb-frame A8; no second class declared), R19-122 (GRANT, reading-level:
@1156 "[80] fois" determiner arm unique survivor; @1011 compatible-but-unforced;
no value named), R19-191/R24 (24='en' iff follower=85; finite/modal elsewhere),
R19-192 (67 positional rule exceptionless).

## Census (±3 tokens, 0-based @)

| @ | row | window | nominal-route test | result |
|---|---|--------|-------------------|--------|
| 441 | a2_09 | 46 43 98 80 50 78 41 | "vient [80-noun]" | FAIL — "venir" takes no bare noun (killed in `frame66-vient-80`); "98 80" is the ×3 infinitive cluster |
| 469 | a2_10 | 00 33 79 80 06 67 46 | "tout [80-noun]" | FAIL — needs 80=noun (1) + "tout"+bare-noun construction license, unlicensed in lane 1841 model (2). Over budget. (Same trigram "79 80 06" at @1090.) |
| 517 | a3_00 | 56 87 77 80 09 70 91 | "le [80-noun]" (77 prov) | FAIL — "87 77" = "ce le" is ungrammatical under the article reading, killing the DET+N frame; pronoun reading needs a verb. Dead, not merely over-budget. |
| 565 | a3_02 | 11 43 24 80 97 13 76 | "[24] [80-noun]" | FAIL — R24: follower=80 → 24 finite/modal; "[modal] [80-noun]" unlicensed; needs 24=transitive (1) + 80=noun (2). Over budget. |
| 663 | a4_02 | 00 86 50 80 03 62 06 | "[50-det] [80-noun]" | FAIL — 50 unvalued; needs 50=det (1) + 80=noun (2). Over budget. |
| 673 | a5_00 | 11 86 24 80 03 64 37 | "[24] [80-noun]" | FAIL — same as @565 (R24 modal); 03's verb-stem class is scoped to "03 29"×3, and here 03 is followed by 64. Over budget. |
| 720 | a5_01 | 01 02 21 80 77 03 91 | "[21-noun] [80-noun/adj]" | FAIL — bare noun-noun apposition ungrammatical; 80=adj needs class (1) + agreement (2). Closest miss on the priority frame; see follow-up 2. |
| 768 | a5_03 | 88 66 98 80 10 22 94 | "vient [80-noun]" | FAIL — "[66-subj] vient [80-inf]" promoted (`frame66-vient-80`, six rivals killed, incl. noun). Dead. |
| 1011 | a6_02 | 35 18 79 80 78 47 03 | "tout [80-noun]" | FAIL — R19-122: compatible-but-unforced, NOT granted; needs 80=noun (1) + "tout"+bare-noun license (2). Over budget. |
| 1032 | a6_03 | 01 03 29 80 77 11 70 | "[03]er [80-noun]" | FAIL — "77 11" = "le la" ungrammatical under any reading, killing DET+N and stranding the nominal; needs 80=noun (1) + "le la" rescue (2+). Dead. |
| 1090 | a6_05 | 00 33 79 80 06 43 07 | "tout [80-noun]" | FAIL — same as @469. Over budget. |
| 1156 | a6_09 | 00 92 29 80 17 77 82 | "[80-det] fois" | RED-TEAM GRANTED (R19-122, locus-scoped). Sole nominal-shaped locus; out of battery scope — this battery cannot re-name it. |
| 1295 | a7_03 | 35 94 52 80 04 62 16 | "[52-det] [80-noun]" | FAIL — 52 unvalued; needs 52=det (1) + 80=noun (2). Over budget. (×2 with @1808.) |
| 1322 | a7_04 | 24 03 29 80 08 62 98 | "[03]er [80-noun/det]" | FAIL — determiner route fenced (`x29-80-1322-det` fence, consistent with `ce-08-31-frame`); nominal needs 80=noun (1) + clause-boundary/exclamative structure (2). Over budget. |
| 1596 | a8_02 | 81 03 29 80 67 77 81 | "[03]er [80-noun]" | FAIL — 67='et' by exceptionless positional rule (R19-192); nominal needs 80=noun (1) + coordination/punctuation structure + 81 named (2+). Over budget. C3 does not fire. |
| 1662 | a8_04 | 47 98 98 80 22 94 84 | "vient [80-noun]" | FAIL — "venir" takes no bare noun (same kill as @441/@768). Dead. |
| 1808 | a8_10 | 35 94 52 80 04 61 15 | "[52-det] [80-noun]" | FAIL — same as @1295. Over budget. |

## Per-clause verdicts

- **C1 FAIL:** no NEW nominal-shaped 80 leg is nameable with ≤1 unstated
  assumption. The census is complete (17/17); the sole nominal-shaped locus,
  @1156 "[80] fois", is a red-team reading-level grant (R19-122), not a
  battery-grade naming — re-promoting it here would duplicate a standing
  red-team ruling.
- **C2 FIRES:** the nominal-80 route is fenced at battery grade with the
  per-window causes above. Fence, not kill: @517 re-opens iff 77 resolves as
  article (R20 open call); @720's adjective arm is untested.
- **C3 does not fire:** no pronoun-like or determined leg was named, so
  @1596's nominal budget is unchanged (its determiner route stays fenced per
  `x29-80-1322-det`).

No standing/red-team verdict contradicted or downgraded (R19-120, R19-122,
R24, R19-192, A8, `frame66-vient-80` all adopted as premises); §7 intact;
80 absent from registry (unchanged); canonical-stream caveat stands
(rows a2_09/a2_10/a3_00/a3_02/a4_02/a5_00/a5_01/a5_03/a6_02/a6_03/a6_05/a6_09/
a7_03/a7_04/a8_02/a8_04/a8_10 offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `nom80-517-77gate` (P4) — gated re-test of @517's "le [80-noun]" DET+N
   frame iff the red team resolves 77='le' as article (R20 open call; the
   "87 77" blocker is the thing to re-examine).
2. `nom80-720-adj` (P3) — test 80 as post-nominal adjective at @720
   ("[21-noun] [80-adj]"); the census's closest miss on a priority frame.
3. `nom80-1596-reopen-gated` (P4) — gated re-fire of this target's C3:
   re-open @1596's nominal budget iff a pronoun-like or determined 80 leg
   is named anywhere at battery grade or above.

## Bookkeeping

- Queue: `nom-80-census` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated from disk; own entry only; no downgrade).
- Lock created on start (2026-10-09T12:41:50Z), deleted on completion
  (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
