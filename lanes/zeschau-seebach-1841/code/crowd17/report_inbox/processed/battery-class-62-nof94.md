# Battery verdict: class-62-nof94

**Verdict: NULL** — no word-class parses all 26 non-94 windows of 62 on the repaired stream, and the @46 block cannot be re-derived with a grammatical segmentation under standing values. The blocker is structural: the "96 00" ("par pour") collocation is ungrammatical at all 3 of its stream occurrences, and @46 sits inside one of them.

## Bar (verbatim, pre-registered)

> one class parsing all 26 non-94 windows, or the same @46 block re-derived

Numbered clauses (fixed before testing):
1. One word-class parses all 26 non-94 windows: 62 takes a single word-class under which every non-94 window is grammatical using only standing (pencil / granted / promoted / provisional) values; no window forces the class false.
2. (Alternative) The @46 block ("81 30 62 96 00", row a1_01) is re-derived: one grammatical segmentation of @44–48 with 62 word-medial, removing the universal blocker.

## Method

Read BATTERY-PROTOCOL.md in full first; lock `locks/class-62-nof94.lock` created on start (agent id + UTC), no stale lock present. Re-derived the 62 census from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`). `canonical.py` never touched. Confirmed 26 non-94 windows = the fullcensus 35 minus the nine 62-94 windows (@100, @508, @761, @840, @1329, @1362, @1686, @1704, @1772). The nine 62-94 windows were not re-litigated (excluded by design; R17-018). R5005, sealed gates, red-team queue untouched. No standing verdict contradicted.

Value key used (standing only): 11=la, 46=que, 87=ce, 64=qui, 96=par, 00=pour, 79=tout, 84=on, 47=ce, 17=fois, 40=e, 34=i, 29=er, 59=est*, 77=le*, 21=<N>, 18=pre, 70=pre, 82=m, 30=pas?, 06=ent?, 14=ce? (* provisional, ? battery-promoted).

## 26-window evidence (re-derived, @-offsets)

| # | @ | row | prev-62-next | wide context (glossed) |
|---|---|-----|--------------|------------------------|
| 1 | 11 | a1_00 | 93-62-98 | 78 18 93 62 98 76 45 |
| 2 | 46 | a1_01 | 30-62-96 | 81 pas? 62 par pour 92 |
| 3 | 82 | a1_02 | 51-62-16 | 98 51 62 16 ce? ent? |
| 4 | 360 | a2_06 | 21-62-48 | ce la <N> 62 48 76 ce |
| 5 | 389 | a2_07 | 36-62-91 | 43 91 36 62 91 on 73 |
| 6 | 425 | a2_09 | 14-62-48 | er ce ce? 62 48 76 42 |
| 7 | 446 | a2_09 | 10-62-61 | 78 41 10 62 61 est* 32 |
| 8 | 658 | a4_02 | 03-62-16 | 26 pas? 03 62 16 pour 86 |
| 9 | 665 | a4_02 | 03-62-06 | 50 80 03 62 ent? pour 20 |
| 10 | 802 | a5_05 | 74-62-98 | 86 44 74 62 98 53 69 |
| 11 | 849 | a5_06 | 40-62-21 | 33 par e 62 <N> 67 91 |
| 12 | 945 | a5_10 | 08-62-98 | 50 e 08 62 98 par 86 |
| 13 | 1065 | a6_04 | 21-62-18 | m par <N> 62 pre pre 39 |
| 14 | 1136 | a6_08 | 20-62-98 | le* 86 20 62 98 pour 98 |
| 15 | 1141 | a6_08 | 78-62-16 | pour 98 78 62 16 er 42 |
| 16 | 1297 | a7_03 | 04-62-16 | 52 80 04 62 16 02 pre |
| 17 | 1315 | a7_04 | 74-62-48 | pour 36 74 62 48 98 15 |
| 18 | 1324 | a7_04 | 08-62-98 | er 80 08 62 98 56 pas? |
| 19 | 1349 | a7_05 | 34-62-48 | 66 73 i 62 48 le* 78 |
| 20 | 1454 | a7_09 | 92-62-61 | 33 que 92 62 61 <N> 67 |
| 21 | 1464 | a7_09 | 21-62-48 | fois 01 <N> 62 48 <N> 02 |
| 22 | 1468 | a7_09 | 02-62-38 | 48 <N> 02 62 38 26 12 |
| 23 | 1482 | a7_10 | 98-62-46 | m 16 98 62 que le* on |
| 24 | 1536 | a8_00 | 41-62-06 | 66 73 41 62 ent? <N> 62 |
| 25 | 1539 | a8_00 | 21-62-93 | 62 ent? <N> 62 93 88 le* |
| 26 | 1569 | a8_01 | 74-62-48 | er 24 74 62 48 56 32 |

Follower distribution (26): 48 x6, 98 x5, 16 x4, 06 x2, 61 x2, 96/91/21/18/38/46/93 x1.

## Clause 1 test: one class for all 26 — FAIL

@46 ("81 pas? 62 par pour", row a1_01) is inside the 26 and defeats every candidate word-class under standing values (30=pas, 96=par promoted):

- subject pronoun: "pas il par" — no.
- finite verb: "pas [V] par" with no "ne" — no.
- noun / adjective / adverb / preposition / determiner: all fail "pas _ par" (carried from battery-class-62-fullcensus; the exclusion of the 62-94 windows does not touch @46).
- infinitive: "pas [INF] par" needs "ne" — no.
- past participle: "pas [PP] par" needs "ne" — no.
- conjunction / relative pronoun: "pas [CONJ/REL] par" — no.
- 'il' rival: already kill-grade dead globally (fullcensus); not revived.
- 'on': collision-62-84 KILL honored, not re-litigated.

No remaining candidate class survives @46, so no single class parses all 26. Clause 1 **FAIL**.

## Clause 2 test: re-derive the @46 block — FAIL

Target segmentation: @44–48 = "81 30 62 96 00" with 62 word-medial, grammatical under standing values. Enumerated segmentations, all fail:

1. "81 | 30-62 | 96 | 00" ("30-62" = "passe"/"passé"): "81 passe par pour [92-inf]" — "par" has no complement and "par pour" is ungrammatical.
2. "81 | 30 | 62-96 | 00" ("62-96" = verb in -par: "préparer"/"réparer"/"séparer"): "pas [INF] pour [inf]" needs "ne"; 81 cannot be "ne" ("77 81" = "le 81" occurs 4x: @745, @1241, @1402, @1599).
3. "81-30 | 62-96 | 00" ("81-30" = "repas"/"trépas"/"appas"): leaves 62 an independent word and keeps "par pour" ungrammatical.
4. "81 | 30-62-96 | 00" ("30-62-96" = "passe-parole"): needs 00="ole", contradicting the 00="pour" promotion (A9).
5. "81 | 30 | 62 | 96-00" ("96-00" one word): no French word "parpour".
6. "81-30-62 | 96 | 00" ("impasse"/"trépasse"): keeps "par pour" ungrammatical.

Structural finding: "96 00" ("par pour") occurs 3x in the stream — @47 ("81 30 62 96 00 92"), @465 ("59 42 96 00 33": "est* 42 par pour 33"), @960 ("67 96 00 86": "67 par pour 86") — and is ungrammatical under standing values at all three. The blocker is the collocation itself, not just @46: "par" never takes a complement in this collocation. Clause 2 **FAIL**.

## Per-clause verdict

- Clause 1: **FAIL** — @46 defeats every candidate class; no class parses all 26.
- Clause 2: **FAIL** — no grammatical word-medial segmentation of the @46 block under standing values; "par pour" x3 is the deeper blocker.

## Adverses

None stated for this target (`adverses: null`). Standing constraints honored: collision-62-84 KILL (62='on' unconditioned) not re-litigated; 62='il' kill-grade dead (fullcensus) not revived; R17-018 62-94 exclusion respected; no red-team verdict contradicted (redteam-62-conditioned still queued, untouched).

## Verdict: NULL

Neither bar clause passes. The negative results are recorded at their proper grades: @46 remains the universal blocker, and the "96 00" collocation is now flagged as independently ungrammatical (3x) — a new lead, not a re-litigation.

## Follow-ups (null regenerates work)

1. `seg-par-pour-96-00` (P2): the "96 00" collocation ("par pour") is ungrammatical under standing values at all 3 occurrences (@47, @465, @960). Bars: produce one grammatical reading of the collocation (one-word hypothesis, value re-check of 00 inside this collocation, or ellipsis fence with byte evidence). Unlocks @46 and the 62 class question.
2. `class-62-25` (P2): name 62's class on the 25 non-94, non-46 windows, with @46 fenced as segmentation-open pending seg-par-pour-96-00. Bars: one class parsing all 25.
3. `stem-62-ent-665-1536` (P3): test 62 as verb-stem-final group in the "62-06" windows @665 ("03 62 ent? pour") and @1536 ("41 62 ent? <N>"), where 06="ent?" reads as a 3pl ending. Bars: parse both as "[stem]-62-ent" 3pl verbs with stated stems, or kill the stem hypothesis.

## Bookkeeping

- Lock `locks/class-62-nof94.lock` created on start (agent id + UTC 2026-10-09T02:48:28Z); no stale lock present; deleted on completion.
- `battery-queue.json`: target `class-62-nof94` queued → verdict/null (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict).
- R5005, sealed gates, red-team adjudication queue untouched. No standing verdict contradicted or downgraded.
