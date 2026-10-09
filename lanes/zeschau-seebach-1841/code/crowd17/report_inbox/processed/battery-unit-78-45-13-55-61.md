# Battery verdict: unit-78-45-13-55-61

**Verdict: KILL** — 61 is not word-internal to a longer unit at either locus
(@577/@1168). The only named word-internal candidate (55-61-94
"prenne"-family, 61="pren") is forced false by standing verdicts, and no
alternative named word admits 61 as an internal syllable. The cleaner rival
— 61 as an independent group with a clean 61|94 word boundary — is
demonstrated on the same frames.

## Target

- id: `unit-78-45-13-55-61` (priority 2)
- claim: "test whether 61 is word-internal to a longer unit at the
  byte-identical 5-gram x2 (@573/@1164)"
- evidence: "battery-duality-61-7034-pattern null (2026-10-09):
  byte-identical 5-gram x2 (@573/@1164) with divergent right edges
  ('ne mentent' vs 'ne ce [83]')."
- adverses: none listed.

## Bar (verbatim from battery-queue.json)

"test whether 61 is word-internal to a longer unit (55-61-94 'prenne'-family
lead from seg-61-94-word vs independent group); discriminates the dict-frame
locus and the @577/@1168 resistance"

## Numbered pass/fail clauses (stated from the bar BEFORE testing; bar not modified after data)

1. **Clause 1 (prenne-family arm):** 55-61-94 is a French word with 61 as an
   internal syllable ("pren") at both @577 and @1168, compatible with all
   standing verdicts (§7 sole-polyvalence rule, banked pencil 70="pre",
   val-61-premier PROMOTE @1556).
2. **Clause 2 (independent-group arm):** 61 parses as an independent group
   (not word-internal to any longer unit) at both windows — a clean word
   boundary at 61|94, and no named longer unit admitting 61 as an internal
   syllable.
3. **Clause 3 (discrimination):** the surviving arm discriminates the
   dict-frame locus (the 5-gram 78-45-13-55-61 is not one word) and accounts
   for @577/@1168's "premier"-resistance.

Verdict rule: KILL if a bar clause fails at kill grade (a window forces the
claim false, or a cleaner rival value is demonstrated on the same frames);
§4. §5.2 noted: no standing red-team verdict is contradicted below, so no
escalation is triggered.

## Method

Read BATTERY-PROTOCOL.md in full before testing. Created
`code/crowd17/next-token/locks/unit-78-45-13-55-61.lock` on start (agent id
1668c062-bfbc-4f1f-bedc-e67f53aa4fa9 + 2026-10-09T08:20:55Z); no stale lock
present. Parsed the repaired 1,847-pair / 96-type stream from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
with the upstream byte-exact tokenization
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]`, same as
`code/side-keyhunt/repair_parse.py`). `canonical.py` never touched. R5005,
sealed gate instances, and the red-team adjudication queue untouched. Every
count below re-derived in-session; no prior counts trusted. Sibling context
read before testing: battery-duality-61-7034-pattern (NULL, follow-up #1 is
this target), battery-dict-frame-78-45-13-55-61 (NULL), battery-seg-61-94-word
(NULL), battery-seg-61-94-word-adjudicate (KILL, 2026-10-09). Standing values
held fixed per §7.

Re-derived census (byte-verified, stream 0-based @):
- "78-45-13-55-61": exactly 2x (@573, @1164), byte-identical.
- "61-94": exactly 2x (@577, @1168) — the whole 61-94 population.
- "55-61-94": exactly 2x (@576, @1167). "55-61": 3x (@576, @1167, @1205).
- The stream's "...ne" word-family shape is stem-12-94: "70-12-94" x2 (@347,
  @1547), "12-94" x3 (@64, @348, @1548). 61-94 lacks the medial 12.
- "61-40": 1x (@1556) — the val-61-premier locus. 61: n=18, scattered
  successors {96x2, 59x2, 94x2, 21x2, 20, 42, 70, 88, 24, 31, 56, 12, 40, 15}
  and predecessors {55x3, 62x2, 89, 37, 20, 49, 87, 17, 92, 01, 53, 91, 12,
  93, 04} — no dominant class.
- 55: n=12, successors {81x6, 61x3, 83x2, 68x1}.
- 13: n=12, successors {24x3, 66x2, 55x2, 93x2, 52x1, 76x1, 92x1};
  13->55 occurs ONLY inside the two 5-grams.

## Window-level evidence

W1 — @573 (row a3_02), target 61 @577:
`80 97 13 76 45 94 52 87 | 78 45 13 55 61 | 94 82 06 06 50 10 19 18`
= "…78-45 [13-55-61] 94-82-06-06…" (queue's 1-based @574).

W2 — @1164 (row a6_09), target 61 @1168:
`80 17 77 82 44 83 21 67 | 78 45 13 55 61 | 94 87 83 21 85 36 74 32`
= "…78-45 [13-55-61] 94-87-83-21…" (queue's 1-based @1165).

Right edges diverge: @577-581 "94 82 06 06" = "ne mentent" (94='ne' STRONG
LEAD, 82='m' banked, 06='ent' R17-007); @1169-1171 "94 87 83" = "ne ce [83]"
(stream-unique 94-87 bigram, "ne ce" hapax — dict-frame battery's residual,
queued follow-up ne-ce-1169).

## Per-clause pass/fail

1. **Clause 1: FAIL at kill grade.** The prenne-family arm forces 61="pren"
   (the family's stream shape is stem-12-94; 61-94 has no medial 12). 61="pren"
   is forced false at two windows with banked neighbors: @1556
   ("93 61 40 17" with banked 40="e" pencil + promoted 17="fois" gives "prene
   fois" — not a French word) and @367 ("49 61 70 17" with banked 70="pre"
   pencil + promoted 17="fois" gives "prenpre" — unreadable). It also
   collides with banked pencil 70="pre" (near-identical "pre"/"pren" pair)
   and with standing val-61-premier PROMOTE (@1556 reads 61 "premier"-shaped).
   A frame-restricted rescue (61="pren" only at @577/@1168) is a second
   polyvalence, forbidden by §7 (67 et/veut is the sole true polyvalence).
   This corroborates — without re-litigating — the standing
   battery-seg-61-pren-polyvalence KILL and the 2026-10-09
   battery-seg-61-94-word-adjudicate KILL, which closed the 55-61-94 family
   candidacy on the same grounds.
2. **Clause 2: PASS.** 61|94 is a clean word boundary at both windows:
   94='ne' is a STRONG LEAD (R17-001) and heads the rightward negation word
   ("ne mentent" @578-581, R17-007); 94 is word-external to 61, so no unit
   containing 61 can extend rightward through 94. Leftward, the only named
   candidate (55-61-94) is killed in clause 1; 13-55-61 is unnameable
   (dict-frame battery NULL, not re-litigated); 55-61 itself parses as a
   complete word at @1205 (seg-55-61-21-stem PROMOTE, "prend" + noun object)
   — consistent with 61 word-final or standalone, never internal to a longer
   unit. Naming any other longer unit now would invent data (protocol §3).
   61's scattered contact profile (no dominant class, val-61-contact KILL of
   any global value) fits an independent group with an unnameable value, not
   a hidden syllable.
3. **Clause 3: PASS.** The independent-group arm discriminates the dict-frame
   locus: the 5-gram "78-45-13-55-61" is not one word — 61 sits at its right
   edge as an independent group. The @577/@1168 "premier"-resistance stands
   as found by the duality battery (agreement failure @577; "ne ce" hapax
   @1168): this battery closes the last word-internal escape route for
   re-parsing either locus, and leaves the residuals with their already-queued
   follow-ups (ne-ce-1169, w1-573-subject).

## Verdict: KILL

The word-internal claim fails at kill grade: its only named candidate is
forced false by standing verdicts (§7 + val-61-premier + seg-61-pren-
polyvalence KILL), no alternative named word admits 61 as a syllable, and
the cleaner rival — 61 as an independent group with a clean 61|94 boundary —
is demonstrated on the same frames. No standing red-team verdict is
contradicted; the duality-null's red-team escalation question (is 61
word-internal inside 78-45-13-55-61(-94)?) is answered at battery grade: no.
61 is word-final or standalone at both loci.

## Follow-ups

None required: §4 mandates follow-ups for nulls, not kills. The live
residuals from these windows already have queued targets (ne-ce-1169,
w1-573-subject, name-13-55-61 from the dict-frame battery; premier-61-admit-
fence, premier-61-residual5 from the duality battery). No duplicates created.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-unit-78-45-13-55-61.md` (this file).
- Lock created on start, deleted on completion. No stale lock was present.
- R5005, sealed gate instances, red-team adjudication queue untouched.
  `canonical.py` never touched.
