# Battery report: en43-wordinternal-census

- Target: `en43-wordinternal-census` (priority 3)
- Claim: "@21 is the only window where 43 reads word-internal 'en'"
- Worker: battery-worker ad6af51f-fb69-4a13-aace-6a96e70525de
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`, upstream tokenization `[s[i:i+2] for i in range(o, len(s)-1, 2)]`; 1,847 pairs / 96 types asserted). `canonical.py` never used. R5005 untouched. Red-team adjudication queue untouched. Sealed gates untouched. No data invented. @-offsets are 0-based stream indices.
- Lock: created `code/crowd17/next-token/locks/en43-wordinternal-census.lock` on start (no prior fresh lock existed for this target); deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"confirm-or-reject per-window: for each of 43's 16 windows, record whether a word-internal 'en' parse exists; pass iff only @21 (the sole 82/29 contact) admits one"

## Bar restated as numbered pass/fail clauses (mechanical restatement, unchanged by data)

1. For each of the 16 windows of 43 in the repaired stream, a word-internal
   'en' parse classification (exists / does not exist) is recorded with stated
   cause.
2. @21 admits a word-internal 'en' parse.
3. No window of 43 other than @21 admits a word-internal 'en' parse.

## Method

1. Re-derived the full 43 census from the repaired stream: all 16 windows of
   43 with immediate predecessors, successors, and upstream row labels.
2. Word-internal 'en' parse defined: a French word in which 43 occupies the
   syllable 'en' between letter-valued flanks (the battery's confirmed
   instance is 82-43-29 = 'm-en-er' = "mener", banked 82='m', 29='er').
   Tested per window against protocol §7 banked ground truth (82=m, 29=er,
   34=i, 40=e, 70=pre, 11=la, 46=que) and granted values (96=par, 87=ce,
   00=pour, 47=ce, 98='vient' lead). Flanks that are whole-word groups or
   unvalued cannot carry a word-internal syllable; recorded, not assumed.
3. Cross-checked against standing queue verdicts (see §6 below).

## Census evidence (re-derived from the repaired stream)

- 82-43-29 trigram: exactly one occurrence in the stream (starts @20; 43 at
  @21). @21 is the ONLY 82-contact and the ONLY 29-contact of 43 (n=16).
- Letter-valued flanks available anywhere in the 43 census: 82 and 29, both
  only at @21. No 43 window has 34 ('i'), 40 ('e'), or 70 ('pre') as a flank.
- Note: 81="prin" is a killed hypothesis (§7), so 81 is unvalued; @43's
  trigram has no valued letters at all.

### Per-window classification table

| # | @ | row | prev | next | flank values | word-internal 'en' parse? | cause |
|---|---|-----|------|------|--------------|---------------------------|-------|
| 1 | 21 | a1_00 | 82 | 29 | m (banked), er (banked) | **YES** | 'm-en-er' = "mener" (French). Confirmed in at21 clause (b); re-derived here. |
| 2 | 43 | a1_01 | 88 | 81 | none (88 unvalued; 81 unvalued — "prin" killed) | NO | no valued letters; no French word constructible |
| 3 | 244 | a2_02 | 56 | 00 | 'pour' (00, word-valued) | NO | 'pour' is a standalone word; "56-en-pour" is not one word |
| 4 | 258 | a2_02 | 32 | 77 | 'le' (77 provisional, word) | NO | flanks unvalued/word; no interior-syllable word |
| 5 | 343 | a2_05 | 96 | 87 | 'par' (granted), 'ce' (granted) | NO | "par en" ungrammatical (at21 report, clause c); both flanks are words |
| 6 | 386 | a2_07 | 37 | 91 | none (37 open, 91 unvalued) | NO | no valued letters; no French word constructible |
| 7 | 439 | a2_09 | 46 | 98 | 'que' (banked, word), 'vient' (lead, word) | NO | both flanks standalone words |
| 8 | 563 | a3_02 | 11 | 24 | 'la' (banked, word) | NO | "la en" is two tokens, not a word-internal syllable |
| 9 | 1027 | a6_03 | 96 | 87 | 'par' (granted), 'ce' (granted) | NO | same as @343; byte-identical window |
| 10 | 1092 | a6_06 | 06 | 07 | none (both open) | NO | no valued letters |
| 11 | 1126 | a6_07 | 37 | 00 | 'pour' (word) | NO | "37-en-pour" not one word |
| 12 | 1204 | a7_00 | 47 | 55 | 'ce' (granted, word) | NO | 'ce' is a word; 43 is standalone here, not word-internal |
| 13 | 1303 | a7_03 | 08 | 21 | none (both open) | NO | no valued letters |
| 14 | 1305 | a7_04 | 21 | 77 | 'le' (provisional, word) | NO | no interior-syllable word |
| 15 | 1544 | a8_00 | 78 | 00 | 'pour' (word) | NO | "78-en-pour" not one word |
| 16 | 1724 | a8_07 | 37 | 98 | 'vient' (lead, word) | NO | "37-en-vient" not a French word |

Summary: 1 YES (@21), 15 NO.

## Per-clause pass/fail

1. **PASS.** All 16 windows classified above with stated cause, every number
   re-derived from the repaired stream.
2. **PASS.** @21: 'm-en-er' = "mener" with banked 82='m' and 29='er'; the
   82-43-29 trigram is unique in the stream; @21 is 43's sole 82-contact and
   sole 29-contact.
3. **PASS.** The other 15 windows admit no word-internal 'en' parse: in 11 of
   them the flanks are whole-word groups ('par', 'ce', 'la', 'pour', 'que',
   'vient', 'le') that cannot host an interior syllable, and in the other 4
   (@43, @386, @1092, @1303) no flank carries a value at all. No window has
   any other letter-valued flank (no 34/40/70 adjacency anywhere in the
   16-window census).

## Adverses

- "none new; feeds (does not pre-empt) red-team adjudication" — answered:
  this report names no global value for 43, declares no second polyvalence,
  and re-names nothing at battery level. It is a window-local census whose
  result feeds the red team's pending 43-polyvalence petition (at21 §6):
  the word-internal reading is confirmed to touch exactly one window, while
  the noun frames are untouched.

## Consistency with standing queue verdicts (no contradictions)

- `at21-82-43-29-adjudicate` (null, 2026-10-08): clause (b) CONFIRMED the
  @21 word-internal 'en' reading and the 16-window neighbor census, which
  this battery re-derived byte-identically. This report is the follow-up
  target that null's §6 proposed (follow-up #3), completed.
- `43-29-segment` (promote, 2026-10-09): "Boundary killed; word-internal
  stands" at @21; "29 x1 (@21) is the sole verbal-ending adjacency in 16
  windows". Fully consistent — this census independently re-derives the
  same isolation of @21.
- `noun-43` (null), `noun-43-discriminator` (kill), `par43-adverbial-attestation`
  (promote), all other 43-related verdicts: none contradicted; none of them
  posit a word-internal 'en' reading outside @21, and the noun legs of the
  other 15 windows are not challenged here.

## Verdict: PROMOTE

All three bar clauses pass and the sole adverse note is answered (honored,
not ignored). The claim is promoted at battery grade: @21 is the only
window of 43 in the repaired 1,847-pair stream that admits a word-internal
'en' parse. Promotion scope is strictly window-local: no global 43 value is
named, and the 67-sole-polyvalence rule and the red team's 43 adjudication
are not pre-empted.

## Follow-ups (nulls only)

None required — verdict is promote. The pending red-team 43-polyvalence
petition (at21 §6) is the standing escalation for the global question and
is left untouched.
