# Battery report: wordbound-63-29-373 — decide the word boundary at @373|374

- Worker: battery worker wordbound-63-29-373, agent abc1347b-5c22-43c6-97fa-98a49bc78e31
- Date: 2026-10-09 (lock created 2026-10-09T20:30:00Z; no prior lock, fresh run)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Re-derived in-session: 1,847 pairs / 96 types verified; asserts held. canonical.py NOT used. R5005, sealed gates, and the red-team adjudication queue untouched. All @-offsets are 0-based repaired-stream pair indices.

## Epistemic status (up front)

NULL / fence both arms. The fused boundary ("[63]er" one word) dies on the governor arm — locus-368-fullparse killed "bare infinitive after a noun" at kill grade, and 63=[verb,cls] has no licensed stem-tier reading for infinitive composition. The split boundary ("[63] | er...") dies on the strand arm — er85-word-census fenced the "29 85" → "er[85]" composition as exhausted (0/3), and "er" standalone is not a French word. Battery-grade; no standing/red-team verdict contradicted or downgraded.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"name one boundary with byte evidence or fence both"

Numbered clauses (frozen, not modified after testing):
1. C1: Name the fused boundary ("[63]er" as one word) with byte evidence.
2. C2: Name the split boundary ("[63] | er...") with byte evidence.
3. C3: Else fence both with stated cause.

Adverses: none listed.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/wordbound-63-29-373.lock` on start; deleted on completion.
2. Re-derived the repaired stream in-session. Byte-confirmed the locus: @372=65, @373=63, @374=29, @375=85 on row a2_06 (`...21 65 63 29 85 | 82 48 00 11...`, row join at 375|376).
3. Censused the three contact families byte-exact: "63 29" exactly 1x stream-wide (@373); "65 63" exactly 4x (@251, @372, @1106, @1530); "29 85" exactly 3x (@96, @374, @1233).
4. Adopted, never re-litigated: 63=[verb,cls] (R19-102), 65=[noun,cls] (R18-001), 21=[noun,cls] (F122), 29='er' pencil GT, 85 verb-stem frame (A3, value open), 67 sole polyvalence (§7), the verb-63-frames PROMOTE report (Leg A), the fin63-373-rerun NULL report (this target's parent), the er85-word-census PROMOTE report, the stem-85-value-rerun NULL report, the locus-368-fullparse NULL report (route-7 kill).

## Window-level evidence

### The locus

Row a2_06 tail: `...70(pre) 17(fois) 06(ent) 21 65 63 29 85 | 82(m) 48(e) 00(pour) 11(la)`. The question is only the boundary between @373=63 and @374=29.

### C1 — fused boundary ("[63]er" one word): FAIL, fenced

For "[63]er" to be one word it must be an infinitive: no French finite paradigm ends in plain "-er" (adopted from fin63-373-rerun). That reading fails on two independent grounds:

- F1 — no governor. The infinitive would sit after 65=[noun,cls] with 21=[noun,cls] further left. Locus-368-fullparse killed route 7 ("bare infinitive after a noun is ungrammatical") at kill grade. No preposition or governing verb is available in the window (00='pour' is two pairs right of 85 and does not govern retroactively).
- F2 — stem-tier shift ungranted. Infinitive composition in the lane runs stem+'er' (03-29 precedent, R19-178). 03 is verb-STEM class; 63 is verb class (R19-102), not stem class. Reading the finite-verb-class cell 63 as a bare stem for "er"-composition is an ungranted tier shift at battery grade.
- F3 — value-open. Even a governor plus a tier license would still need 63's value to name the infinitive "Xer"; 63's value is open, and naming it invents a value (§3 barred).

Fenced with stated cause (F1 at kill grade via locus-368-fullparse route 7).

### C2 — split boundary ("[63] | er..."): FAIL, fenced

A boundary between 63 and 29 forces 29 to begin the next word: "er" + 85.

- S1 — the "er[85]" composition is fenced exhausted. er85-word-census (PROMOTE, battery grade): "29 85" occurs exactly 3x stream-wide (@96, @374, @1233) and zero windows compose as a word under standing values; the route is fenced as exhausted (C3 fired there).
- S2 — 85's value is unnameable via word formation. stem-85-value-rerun (NULL): 29='er' is 0x after 85 across all 15 windows, so a stem with no completion neighbor can never surface as a complete word; 'laisser' locus-killed at @1699; zero selective legs for any rival stem.
- S3 — "er" standalone is a non-word. 29='er' is pencil ground truth at letter/ending tier; the lane's only licensed 'er'-initial word is "29 40"='erre' (R18-012), not "29 85".
- Note: the "65 63" Leg-A subject-verb shape IS licensed here (three of the four "65 63" windows parse as "[65-subj] [63-fin] pour [66]"; @372 is the fourth). The finite-63 head is shape-consistent — the parse dies only on the "er" strand, which is exactly this boundary question (adopted from fin63-373-rerun NULL: "the residual is now localized to exactly two open slots — the @373|374 word boundary and 85's value at @375").

Fenced with stated cause: the split boundary strands a non-word under all standing values.

### C3 — fence both: FIRES

Neither boundary is nameable with byte evidence under standing values. Both arms are fenced at battery grade with independent stated causes.

## Verdict: NULL

The @373|374 boundary is unfenceable-open: fused dies on the governor kill (F1), split dies on the "er"-strand (S1–S3). The fence is evidentiary, not terminal — re-openable when 63's value is banked (re-opens fused) or 85's value/completion is banked (re-opens split).

## Scope

Boundary decision only at @373|374. Untouched: 63's verb class (R19-102), 65's noun class (R18-001), the Leg-A "65 63 00 66" frames, 29='er' pencil GT, A3, the er85-word-census PROMOTE, the fin63-373-rerun NULL, the stem-85-value-rerun NULL, the locus-368-fullparse route-7 kill, §7 (67 sole polyvalence). No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a2_06 offsets unvalidated).

## Follow-ups (all verified ABSENT from battery-queue.json; for supervisor queuing)

1. `val-63-373-value` (P3) — name 63's value at @373; a named -er infinitive stem re-opens the fused arm (governor still required).
2. `gov-21-371-inf` (P4) — test whether 21 (noun-class, F122) or a clause boundary left of 65 can govern an infinitive at @373; a licensed governor re-opens the fused arm without naming 63.
3. `val-85-375-completion` (P4) — name 85's value/completion at @375 (row-final uncompleted stem); a named "er[85]" word re-opens the split arm.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-wordbound-63-29-373.md`
- Queue: `wordbound-63-29-373` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.wordbound-63-29-373.tmp` + rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/wordbound-63-29-373.lock`: created on start (agent abc1347b-5c22-43c6-97fa-98a49bc78e31, 2026-10-09T20:30:00Z), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
