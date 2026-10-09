# Battery verdict: audit-adv62-count

## Bar (verbatim, pre-registered)

> "recount from the repaired stream and correct that report's contact table; the fence's right-edge argument stands"

Numbered clauses (pre-registered before testing):
1. (Recount arm) Re-derive 62's successor distribution from the repaired 1,847-pair stream and publish the corrected contact table for `battery-adv-62-pas-par.md`.
2. (Fence arm) State whether the fence's right-edge argument still stands under the corrected numbers.

Origin: reconciliation battery — `adv-62-pas-par`'s successor-distribution headline (n=38) disagrees with re-derived counts (repaired n=35, old-parse n=34). Note: the internal table rows of `adv-62-pas-par` were never themselves verified; the headline was.

## Method

Read BATTERY-PROTOCOL.md first; lock `locks/audit-adv62-count.lock` created on start (agent id + UTC), no stale lock present; deleted on completion. Re-derived counts inline from the repaired stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, tokenized per `code/side-keyhunt/repair_parse.py`: byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). `canonical.py` never touched. R5005, sealed gate instances, red-team adjudication queue untouched. Old-parse counts re-derived the same way with `data/upstream-offsets.json` (a5_03=1) for comparison — not via `canonical.py`. §7 honored; no standing verdict re-litigated (the prior report is a battery null, not a red-team verdict; this audit agrees with its fence, so no escalation).

## Window-level evidence (@-offsets, repaired stream)

- Stream: 1,847 pairs. 62 occurs 35 times; none at stream-final position, so successor n = 35.
- Target window (confirmed byte-exact): @44=81, @45=30, @46=62, @47=96, @48=00, @49=92, all row a1_01 — matches the prior report's re-parse.
- All 62 windows with successors:

| @ | row | successor | @ | row | successor |
|---|-----|-----------|---|-----|-----------|
| 11 | a1_00 | 98 | 1065 | a6_04 | 18 |
| 46 | a1_01 | 96 | 1136 | a6_08 | 98 |
| 82 | a1_02 | 16 | 1141 | a6_08 | 16 |
| 100 | a1_02 | 94 | 1297 | a7_03 | 16 |
| 360 | a2_06 | 48 | 1315 | a7_04 | 48 |
| 389 | a2_07 | 91 | 1324 | a7_04 | 98 |
| 425 | a2_09 | 48 | 1329 | a7_04 | 94 |
| 446 | a2_09 | 61 | 1349 | a7_05 | 48 |
| 508 | a3_00 | 94 | 1362 | a7_06 | 94 |
| 658 | a4_02 | 16 | 1454 | a7_09 | 61 |
| 665 | a4_02 | 06 | 1464 | a7_09 | 48 |
| 761 | a5_03 | 94 | 1468 | a7_09 | 38 |
| 802 | a5_05 | 98 | 1482 | a7_10 | 46 |
| 840 | a5_06 | 94 | 1536 | a8_00 | 06 |
| 849 | a5_06 | 21 | 1539 | a8_00 | 93 |
| 945 | a5_10 | 98 | 1569 | a8_01 | 48 |
| — | — | — | 1686 | a8_05 | 94 |
| — | — | — | 1704 | a8_06 | 94 |
| — | — | — | 1772 | a8_09 | 94 |

- "30 62 96" occurs exactly once stream-wide: @45 (the target window). Hapax confirmed.
- 62 never precedes 00 or 39: zero windows ("62->00 or 62->39" search returns []). The "no 'pas [62] pour/a' frames anywhere" statement holds.
- Old-parse (upstream offsets) recount: 1,846 pairs; 62 occurs 34 times; distribution 94 x8, 48 x6, 98 x5, 16 x4, 61 x2, 06 x2, plus the seven singletons (18, 21, 38, 46, 91, 93, 96) — n=34. The +1 repaired occurrence is the a5_03 re-pairing delta (one extra 94-successor at @761).

## Corrected contact table (replaces the prior report's)

62 successor distribution, repaired stream, n=35:

94 x9, 48 x6, 98 x5, 16 x4, 61 x2, 06 x2, 18 x1, 21 x1, 38 x1, 46 x1, 91 x1, 93 x1, 96 x1. Sum: 35. All 35 windows accounted; 13 distinct successor types.

Cross-check vs the prior report: its listed rows were 94 x9, 48 x6, 98 x5, 16 x4, 61 x2, 06 x2, 96 x1, 91 x1, 21 x1, 18 x1, 38 x1, 46 x1, 93 x1 — category-for-category identical to the re-derived table. The table's rows sum to 35, so the error is localized to the headline: **n=38 was wrong** (unaccounted +3 against the repaired stream, +4 against the old parse n=34). The prior report's own table rows needed no numerical correction — only the headline did.

Corrections recorded (delta, what was wrong):
- Headline "n=38" → n=35 (repaired) / n=34 (old parse). No evidence for any 38-count on either parse.
- The prior report's "62 never precedes 00 or 39" — CONFIRMED (re-derived, zero windows).
- The prior report's "30 62 96 exactly once stream-wide" — CONFIRMED (@45).
- The prior report's 30-successor table (n=19: 06 x4, 03 x3, 67 x2, 20 x2, 62 x1, 01 x1, 69 x1, 09 x1, 92 x1, 82 x1, 64 x1, 15 x1) — CONFIRMED verbatim (re-derived n=19, identical).

## Clause tests

**Clause 1 (Recount arm): PASS.** Successor distribution re-derived from the repaired stream: n=35 with the corrected contact table above; headline n=38 corrected to n=35. The table is fully traceable (35 windows, 35 successors, 13 types, every window @-offsetted).

**Clause 2 (Fence arm): PASS — the fence's right-edge argument stands.** The fence's three byte-grounded causes re-derive cleanly under corrected numbers:
1. Right-edge impossibility: unchanged — @46–48 = "62 96 00" is the granted "par pour", which no French adverb salvages. Independent of n.
2. Frame uniqueness: "30 62 96" is a hapax (n=1, @45); 62 never precedes 00 or 39 (zero windows). Both CONFIRMED on the repaired stream. The adverb hypothesis still has exactly one testable window, and it fails there.
3. Distributional incompatibility: 62-06 x2 confirmed (@665, @1536) — nn-final stem, incompatible with the adverb slot.

The n=38→35 correction touches none of the three causes; the fence stands on the same byte evidence.

## Verdict: PROMOTE

Both bar clauses pass; no adverses listed; no standing verdict contradicted (the prior report was a battery null and this audit agrees with its fence — the correction is numerical, not inferential). This is an audit battery: "promote" = the corrected numbers and the fence both stand. No follow-ups required (not a null).

## Bookkeeping

- Lock `locks/audit-adv62-count.lock` created on start, deleted on completion.
- `battery-queue.json`: target `audit-adv62-count` queued → verdict/promote (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated post-write).
- R5005, sealed gate instances, red-team adjudication queue untouched. `canonical.py` never used. No invented numbers — every figure traces to the stream.
