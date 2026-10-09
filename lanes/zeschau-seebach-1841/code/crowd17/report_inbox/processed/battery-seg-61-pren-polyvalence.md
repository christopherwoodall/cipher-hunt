# Battery verdict: seg-61-pren-polyvalence

**Verdict: KILL** — 61="pren" is impossible as a global value. Window @1556
(a8_01) reads `93 61 40 17` = "…93 prene fois…": 61="pren" + 40="e" (pencil)
gives "prene", and 17="fois" (promoted) follows. No French word is "prene".
No French word ends in "pren". No French word starts with "prene" as a full
word ("preneur"/"preneuse" need more letters, but 17="fois" is banked and
starts a new word). The window cannot be read with banked neighbors under a
single 61="pren" value. Corroboration at @367 (a2_06): `49 61 70 17` =
"…49 prenpre fois…" with 70="pre" (pencil) and 17="fois" (promoted):
"prenpre" is also not readable French. A rescue that limits 61="pren" to the
55-61-94 frame only would be a polyvalence. That is forbidden by §7 and by
clause 3 below. The 70="pre" pencil side of the tension stands. 61 stays
undemonstrated.

## Bar (verbatim from battery-queue.json)

(a) compare the fenced 70-12-94 "prenne" windows (@347, @1547) against the 2 x
55-61-94 windows on left-context class; (b) find one 61 window where "pren"
is forced or one where it is impossible; (c) keep 67 et/veut the sole
polyvalence (§7)

## Numbered clauses (pre-registered before testing)

1. (a) Left-context-class comparison: list the left 3 tokens and the right
   follower for each of the four windows (70-12-94 @347 and @1547; 55-61-94
   @576 and @1167) on the repaired stream, with @-offsets and row ids; state
   the discriminating difference or record its absence.
2. (b) Name one 61 window where "pren" is forced, or one where "pren" is
   impossible. Only banked (§7) neighbor values may ground the call.
3. (c) No polyvalence is declared at battery level. 67 et/veut stays the sole
   polyvalence.

## Method

Read BATTERY-PROTOCOL.md in full first. Created
`locks/seg-61-pren-polyvalence.lock` (agent edd4c9aa-0b83-48a9-97ec-5b6b53b6662b,
2026-10-09T03:17:19Z) on start. No stale lock existed. Parsed the repaired
1,847-pair stream from `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt` with the upstream byte-exact tokenization
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]`), the same form as
`code/side-keyhunt/repair_parse.py`. `canonical.py` never touched. R5005,
sealed gate instances, and the red-team adjudication queue never touched. All
counts re-derived from the stream. No prior counts trusted. No values
redacted.

## Window-level evidence

### Clause 1: the four windows

70-12-94, trigram start @347 (row a2_05):
`… 87 01 06 | 70 12 94 | 74 67 78 …`
Left-3 of 70: 87=ce (promoted), 01, 06. Right follower of 94: 74.

70-12-94, trigram start @1547 (row a8_00):
`… 43 00 46 | 70 12 94 | 92 45 23 …`
Left-3 of 70: 43, 00=pour (promoted), 46=que (pencil). Right follower of 94:
92. This is a clean "pour que ___" subjunctive frame with 70 word-initial.
The "prenne" fence on the 70 side is anchored by banked values (00, 46, 70)
alone. It does not need 61.

55-61-94, trigram start @576 (row a3_02):
`… 87 78 45 13 | 55 61 94 | 82 06 06 …`
Left-4 of 55: 87=ce (promoted), 78, 45, 13. Right follower of 94: 82=m
(pencil).

55-61-94, trigram start @1167 (row a6_09):
`… 83 21 67 78 45 13 | 55 61 94 | 87 83 21 …`
Left of 55: 83, 21, 67=et/veut (§7 polyvalence, untouched), then 78, 45, 13.
Right follower of 94: 87=ce (promoted).

Left-context class result: the two 55-61-94 windows share an identical left
trigram 78-45-13 (one fixed 6-gram formula, 78-45-13-55-61-94, x2 stream-wide).
The two 70-12-94 windows share no left bigram (01-06 vs 00-46). The 70 frame
is verb-licensed ("pour que prenne" @1547) with 70 word-initial. The 55 frame
is a fixed collocation with fully unknown left material, so 55 is not shown
word-initial and the "re-" prefix parse is unanchored. The 55-61-94 frame
cannot inherit the "prenne" fence from 70-12-94. Clause 1: PASS.

### Clause 2: the 61 census (n=18) against "pren"

Full census with banked neighbors (pencil: 11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que; promoted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout,
00=pour, 84=on, 47=ce; provisional: 59=est, 77=le):

| 61@ | row | left nb | right nb | note under 61="pren" |
|---|---|---|---|---|
| 223 | a2_01 | 89 | 96=par | "pren par" — no force |
| 279 | a2_03 | 37 | 20 | no banked contact |
| 281 | a2_03 | 20 | 42 | no banked contact |
| 367 | a2_06 | 49 | 70=pre | "prenpre fois" — IMPOSSIBLE (see below) |
| 447 | a2_09 | 62 | 59=est | "pren est" — no force |
| 577 | a3_02 | 55 | 94 | the 55-61-94 frame |
| 645 | a4_02 | 87=ce | 88 | "ce pren ?" — no force |
| 926 | a5_10 | 17=fois | 96=par | "fois pren par" — no force |
| 1168 | a6_09 | 55 | 94 | the 55-61-94 frame |
| 1206 | a7_00 | 55 | 21 | third 55-61 window (follower 21) |
| 1219 | a7_01 | 92 | 24 | no banked contact |
| 1256 | a7_02 | 01 | 31 | no banked contact |
| 1281 | a7_03 | 53 | 56 | no banked contact |
| 1429 | a7_08 | 91 | 12 | "pren ?" — 12 unknown |
| 1455 | a7_09 | 62 | 21 | no banked contact |
| 1510 | a7_11 | 12 | 59=est | "? pren est" — 12 unknown |
| 1556 | a8_01 | 93 | 40=e | "prene fois" — IMPOSSIBLE (see below) |
| 1810 | a8_10 | 04 | 15 | no banked contact |

No window forces "pren". Not one of the 18 windows has banked neighbors
that form an unambiguous "pren…" word.

Impossible window 1 — @1556 (a8_01), byte-verified:
`… 23@1552 99@1553 13@1554 93@1555 61@1556 40@1557 17@1558 11@1559 …`
61="pren" + 40="e" (pencil) = "prene", then 17="fois" (promoted), then
11="la" (pencil): "…93 prene fois la…". "prene" is not a French word. No
French word ends in "pren". "preneur"/"preneuse" start with "prene" but need
more letters, and 17="fois" is banked, so it starts a new word. Every
boundary placement fails with banked neighbors.

Impossible window 2 — @367 (a2_06), byte-verified:
`… 47@363 78@364 48@365 49@366 61@367 70@368 17@369 06@370 …`
61="pren" + 70="pre" (pencil) + 17="fois" (promoted) = "…49 prenpre fois…".
"prenpre" is not readable French under any boundary placement with banked
neighbors.

Clause 2: PASS via the "impossible" disjunct. The substantive result is that
61="pren" is forced false as a global value.

### Clause 3: polyvalence

No polyvalence declared. 67 et/veut not touched (it appears only as
left-context at the @1167 window, four tokens before 55). Clause 3: PASS.

## Per-clause pass/fail

1. (a) Left-context comparison with @-offsets and discriminating difference
   stated — PASS.
2. (b) One 61 window where "pren" is impossible, banked-grounded (@1556;
   corroborated @367); no window forces "pren" — PASS as written. The
   finding forces the claim false at kill grade.
3. (c) 67 et/veut the sole polyvalence; none declared — PASS.

## Adverses

- 70="pre" pencil: ANSWERED and re-confirmed. @1547 sits in "pour que
  70-12-94" (00=pour promoted, 46=que pencil, 70=pre pencil). The "prenne"
  fence on the 70 side holds without 61.
- 61="pren" undemonstrated: ANSWERED by exclusion. It is now positively
  excluded as a global value (@1556, @367).
- No polyvalence declared: holds. Clause 3 passes.

## Verdict: KILL

Two independent windows (@1556, @367) force 61="pren" false with banked
neighbors. A frame-restricted rescue (61="pren" only after 55) would be a
polyvalence, forbidden by §7 and clause 3. The 61="pren" / 70="pre" tension
resolves against 61. 70="pre" pencil stands. 61 keeps no value from this
battery.

Re-open condition: the kill falls only if the red team fences @1556 (for
example a proper noun or non-French token at 93-61-40) with a stated cause.
That is a red-team call, not a battery call. No standing red-team verdict on
61 was contradicted: the earlier seg-61-94-word battery returned null, and
no verdict for 61="pren" exists.
