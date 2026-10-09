# Battery report: f61-06-scope-precise

- Target id: `f61-06-scope-precise`
- Claim: byte-precise the F61 islet's scope — census all 44 06-windows for the pre=82 conditioning; confirm or fence which 06 positions the islet actually covers.
- Date: 2026-10-09
- Worker: battery worker (subagent b2cd33a8-943c-4cb9-8f00-b479328d3eed)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "islet" = a conditioned value claim that covers only some windows of a cell. "F61" = the conditioned lead "06 = 'ent' iff pre = 82". "pre" = the pair immediately left of the window. "fol" = the pair immediately right. "battery grade" = the evidence standard of this pipeline. All @-offsets are 0-based pair indices.

## Bar (verbatim, pre-registered before testing)

"Bar: byte-precise the F61 islet's scope: census all 44 06-windows for the pre=82 conditioning; confirm or fence which 06 positions the islet actually covers. Bar: conditioning rule stated with byte evidence at battery grade, or the islet fenced as underdetermined."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** n(06) = 44 confirmed on the repaired stream; all 44 windows censused byte-exact (position, pre, fol, row).
2. **C2:** the pre=82 06-positions are exactly [580, 738, 1184, 1355]; "82 06" bigram occurs exactly 4x stream-wide; each covered position is row-internal (no row-boundary artifact).
3. **C3:** 'ent' is a licensed reading at each of the 4 covered positions — no covered window forces a non-'ent' reading; per-window license stated with byte context.
4. **C4:** the 40 non-covered positions (pre != 82) are outside the islet's conditioning scope — stated, not decided; the doubling-second positions (@581, @1185; pre=06) explicitly outside.
5. **C5:** adverses answered (none listed).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/f61-06-scope-precise.lock` on start (agent id + UTC timestamp); deleted on completion.
2. Re-derived the repaired stream in-session per `repair_parse.py` (byte-exact tokenizer `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). Asserts held: 1,847 pairs, 96 types.
3. Standing premises used, not re-litigated: 82 = 'm' (banked GT letter), 06 = 'ent' global promoted (ent-06), 94 = 'ne' (battery-promoted), F61 conditioned lead as the charter under test, §7 (67 et/veut sole polyvalence).
4. Read the parent/grandparent batteries `seg-94-82-06` (NULL), `seg-94-82-06-f3` (NULL), `second-06-nonent` (NULL) for window readings; re-derived the full 06 census independently (did not copy their numbers).

## Census — all 44 06-windows, byte-exact

Columns: 0-based pair index of the 06 | pre (pair left) | fol (pair right) | row of the 06.

| idx | pre | fol | row | idx | pre | fol | row |
|-----|-----|-----|-----|-----|-----|-----|-----|
| 6 | 41 | 77 | a1_00 | 1184 | 82 | 06 | a6_10 |
| 85 | 14 | 88 | a1_02 | 1185 | 06 | 59 | a6_10 |
| 184 | 37 | 00 | a1_05 | 1188 | 42 | 84 | a6_10 |
| 206 | 42 | 77 | a2_00 | 1252 | 30 | 65 | a7_02 |
| 215 | 78 | 59 | a2_00 | 1328 | 30 | 62 | a7_04 |
| 267 | 42 | 73 | a2_02 | 1355 | 82 | 52 | a7_05 |
| 271 | 11 | 67 | a2_03 | 1388 | 16 | 29 | a7_07 |
| 319 | 94 | 11 | a2_04 | 1475 | 60 | 67 | a7_10 |
| 346 | 01 | 70 | a2_05 | 1537 | 62 | 21 | a8_00 |
| 370 | 17 | 21 | a2_06 | 1562 | 30 | 60 | a8_01 |
| 399 | 48 | 11 | a2_08 | 1667 | 64 | 91 | a8_05 |
| 470 | 80 | 67 | a2_10 | 1709 | 12 | 29 | a8_06 |
| 522 | 77 | 55 | a3_00 | 1720 | 68 | 11 | a8_07 |
| 544 | 42 | 00 | a3_01 | 1734 | 30 | 60 | a8_07 |
| 580 | 82 | 06 | a3_02 | 1747 | 40 | 65 | a8_08 |
| 581 | 06 | 50 | a3_02 | 1762 | 93 | 77 | a8_08 |
| 666 | 62 | 00 | a4_02 | 1815 | 42 | 29 | a8_10 |
| 738 | 82 | 00 | a5_02 | | | | |
| 773 | 07 | 94 | a5_04 | | | | |
| 789 | 84 | 77 | a5_04 | | | | |
| 890 | 86 | 77 | a5_08 | | | | |
| 967 | 24 | 77 | a6_00 | | | | |
| 1080 | 64 | 52 | a6_05 | | | | |
| 1091 | 80 | 43 | a6_06 | | | | |
| 1096 | 81 | 29 | a6_06 | | | | |
| 1120 | 12 | 14 | a6_07 | | | | |
| 1122 | 14 | 11 | a6_07 | | | | |

Predecessor distribution (44 windows): 42 x5, 82 x4, 30 x4, 14 x2, 80 x2, 06 x2, 62 x2, 64 x2, 12 x2, and 41, 37, 78, 11, 94, 01, 17, 48, 77, 07, 84, 86, 24, 81, 16, 60, 68, 40, 93 x1 each. (5+4+4+2+2+2+2+2+2+19 = 44.)

Row-boundary notes: @271 (pre a2_02, 06 a2_03), @399 (pre a2_07, 06 a2_08), @773 (pre a5_03, 06 a5_04), @1091 (pre a6_05, 06 a6_06) straddle row joins. None of the four pre=82 positions does — all are row-internal.

## The four covered positions — byte context (±5, 0-based)

- **@580** (a3_02, row-internal): `13 55 61 [94 82 06] 06 50 10 19 18` → "…55 61 ne m'ent ent [50]…". Left trigram 94-82-06. License: "82 06" = "m"+"ent" = "ment…"; no window-level force against 'ent' (the second-06 question at @581 is a separate, already-fenced battery).
- **@738** (a5_02, row-internal): `85 93 76 [18 82 06] 00 36 20 30 67` → "…76 [18] m'ent pour [36]…". Left trigram 18-82-06 (the 94-variant; the left-slot value does not touch the pre=82 conditioning). License: "ment pour".
- **@1184** (a6_10, row-internal): `37 77 78 [94 82 06] 06 59 42 06 84` → "…78 ne m'ent ent est [42]…". Left trigram 94-82-06. License: "ment…".
- **@1355** (a7_05, row-internal; ±5 window reaches a7_06 but the trigram + follower are all a7_05): `48 77 78 [94 82 06] 52 37 64 35 13` → "…78 ne m'ent [52] [37]…". Left trigram 94-82-06. License: "ne ment"-family (parent battery: frame D clean).

"82 06" bigram: exactly 4x stream-wide (the four positions above). "06 06" doubling: exactly 2x (left indices 580, 1184); the second 06s (@581, @1185) have pre=06 and sit outside the islet.

## Per-clause pass/fail

- **C1 — PASS.** n(06) = 44 confirmed; full table above, every window byte-exact with row labels.
- **C2 — PASS.** pre=82 06-positions are exactly [580, 738, 1184, 1355]; "82 06" bigram x4 stream-wide (no fifth instance); all four row-internal — no row-boundary artifact inflates or deflates the set.
- **C3 — PASS.** 'ent' is licensed at each covered position via the "m"+"ent" = "ment" composition under the standing 82='m' bank; no covered window forces a non-'ent' reading. Per-window licenses stated above.
- **C4 — PASS.** The other 40 positions carry pre != 82 and are therefore outside the conditioning's scope. The doubling seconds @581/@1185 (pre=06) are explicitly outside — consistent with `seg-94-82-06-f3`'s standing note "F61's scope is unchanged (first 06 covered; second outside scope)". Nothing about the other 40 positions' values is decided here.
- **C5 — PASS.** No adverses were listed.

## Verdict: PROMOTE

The F61 islet's scope is byte-precise. **Conditioning rule (battery grade): 06 reads 'ent' under the F61 conditioning at exactly those 06-positions whose immediate predecessor is 82 ('m') — 0-based @580, @738, @1184, @1355 — four positions, all row-internal, 'ent' licensed at each with no forcing counter-evidence.** The other 40 06-windows (pre != 82) are outside the islet's scope. The charter's "iff" is confirmed as a coverage statement: the islet covers exactly the pre=82 set — no more, no fewer.

## Scope notes (not decided, not re-litigated)

- Whether non-covered 06 positions also read 'ent' is 06's global promoted value (ent-06), a separate standing premise — not this battery's bar.
- The reverse direction of the biconditional (pre != 82 → 06 != 'ent') was not tested; the bar scoped this battery to coverage only.
- The second-06 doubling values (@581, @1185) stay fenced under `second-06-nonent` / `seg-94-82-06-f3`; this battery neither opens nor closes them.
- Canonical-stream caveat stands (rows a3_02/a5_02/a6_10/a7_05 offsets unvalidated; 68/70 upstream row offsets unvalidated per protocol §7).

No standing or red-team verdict contradicted or downgraded; §7 intact (no polyvalence declared — homophony not at issue); R5005, sealed gates, red-team adjudication queue untouched.

## Follow-ups proposed

Promote needs none (§4: only nulls regenerate). No follow-ups proposed.

## Bookkeeping

- Queue: `f61-06-scope-precise` → status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/f61-06-scope-precise.lock`: created on start (agent id + UTC timestamp), deleted on completion (verified gone).
