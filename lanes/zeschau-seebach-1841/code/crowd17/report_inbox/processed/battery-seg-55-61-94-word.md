# Battery verdict: seg-55-61-94-word

**Verdict: NULL** — the 78-45-13-55-61-94 formula is real (x2, byte-verified)
and the "...prenne ce..." parse at @1167–@1170 is grammatical, but the bar's
discriminating clause fails twice over: the "55-81-00 x5" parallel frame is a
finder misread (trigram 3x, bigram 6x), and 55's value ("re") does not
triangulate from any banked/promoted contact. No window forces the claim false;
the word-unit lead survives as three narrower follow-ups below.

## Bar (verbatim from battery-queue.json)

(a) triangulate 55 via the 55-81-00 x5 parallel frame and 55's 12-window
census; (b) demonstrate the full word with grammatical "...prenne ce..."
parse at @1169; (c) keep 94='ne' intact

## Numbered clauses (pre-registered before testing)

1. (a1) Census: enumerate all 12 windows of 55 on the repaired stream with
   @-offsets.
2. (a2) Parallel frame: verify the "55-81-00 x5" frame as written (byte-exact
   counts and @-offsets).
3. (a3) Triangulation: name 55's value (or class) from contact profiles against
   banked/promoted values only.
4. (b) Demonstrate the full word 55-61-94 with a grammatical "...prenne ce..."
   parse at @1169 (word-final 94 at @1169, 87=ce at @1170).
5. (c) 94='ne' (promoted) undisturbed; no second 94 value declared (§7).

## Method

Read BATTERY-PROTOCOL.md in full first; created
`locks/seg-55-61-94-word.lock` (agent 0060ab45…, 2026-10-09T02:48:33Z) on start —
no stale lock existed. Parsed the repaired 1,847-pair stream from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` with the
upstream byte-exact tokenization (`[s[i:i+2] for i in range(o, len(s)-1, 2)]`).
`canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
Every count re-derived from the stream; no prior counts trusted.

## Window-level evidence

### The two 55-61-94 windows (formula x2 confirmed)

- @576 (row a3_02): `... 87 78 45 13 | 55 61 94 | 82 06 06 50 ...`
  (87=ce promoted; 82=m pencil; 06=ent promoted)
- @1167 (row a6_09): `... 67 78 45 13 | 55 61 94 | 87 83 21 85 ...`
  (67=et/veut; 87=ce promoted; 21=NOUN class; 85 verb-stem A3)

The 6-gram `78-45-13-55-61-94` occurs exactly 2x stream-wide, with identical
left 4-gram `78-45-13-55` and differing only in 94's follower (82 @576 vs
87 @1167). Evidence "78-45-13-55-61-94 formula x2" VERIFIED.

### 55 census: n=12 (clause 1: PASS — all 12 enumerated, byte-verified)

| @ | row | context (55 centred) |
|---|---|---|
| 25 | a1_00 | 29 47 33 **55** 81 00 34 |
| 523 | a3_00 | 91 77 06 **55** 81 97 47 |
| 550 | a3_01 | 24 47 46 **55** 81 00 86 |
| 576 | a3_02 | 78 45 13 **55** 61 94 82 |
| 906 | a5_09 | 16 88 18 **55** 83 54 49 |
| 1085 | a6_05 | 89 24 02 **55** 81 00 33 |
| 1094 | a6_06 | 06 43 07 **55** 81 06 29 |
| 1167 | a6_09 | 78 45 13 **55** 61 94 87 |
| 1205 | a7_00 | 58 47 43 **55** 61 21 65 |
| 1285 | a7_03 | 56 32 98 **55** 68 00 11 |
| 1611 | a8_03 | 65 23 08 **55** 83 71 48 |
| 1671 | a8_05 | 91 11 78 **55** 81 92 60 |

Followers of 55: 81 x6, 61 x3, 83 x2, 68 x1. Predecessors: 33, 06, 46(=que),
13, 18, 02, 07, 43, 78, 98, 08, 78 — heterogeneous.

### Clause 2: FAIL — the "55-81-00 x5" frame is a finder misread (recorded, §2)

- Trigram `55-81-00`: **3x** — @25 (a1_00), @550 (a3_01), @1085 (a6_05).
- Bigram `55-81`: **6x** — adds @523 (a3_00, follower 97), @1094 (a6_06,
  follower 06), @1671 (a8_05, follower 92).
- The bar as written ("55-81-00 x5") is false on both the trigram count (3≠5)
  and the bigram count (6≠5). The intended discriminating frame is the bigram
  `55-81` x6. Not silently rewritten — recorded here as a finding.

### Clause 3: FAIL — 55 does not triangulate

Contacts against banked/promoted values only (banked pencil: 11=la, 70=pre,
82=m, 34=i, 29=er, 40=e, 46=que; promoted: 87=ce, 64=qui, 96=par, 17=fois,
79=tout, 00=pour, 84=on, 47=ce; provisional: 59=est, 77=le):

- The 6 x 55-81 windows share no banked/promoted contact beyond 55-81 itself.
  81's value is unknown (81="prin" KILLED per §7 — kills hold; the bigram
  cannot be "re-prin").
- 83 carries only a lead ('de', unpromoted); 68 and 61 are unknown; 61's own
  battery (seg-61-94-word, NULL) failed to triangulate 61.
- 55="re" (the prefix the prenne-family claim needs) is supported by nothing
  outside the claim itself — circular. Clause 3 FAILS (attempt complete,
  negative result — not ignored).

### Clause 4: FAIL — word demonstrated? No. Compatible? Yes.

- @1167–@1170: `55 61 94 | 87` = "[word] ce" with 87=ce promoted. "...prenne
  ce..." / "...reprenne ce..." is grammatical 1841 French (subjunctive + "ce"
  + complement: "pour qu'il reprenne ce chemin"). But grammaticality is
  conditional on the undemonstrated values 55="re", 61="pren" — compatible,
  not proven.
- @576: `55 61 94 | 82(m) 06(ent)` = "[word] m..." — compatible with
  "...reprenne mon..." (82=m pencil starts a following word); no forced
  falsity.
- Rival encoding (kill-grade check, not met): the fenced word `70-12-94`
  ("pre"-"n"-"ne" = "prenne") at @347 (a2_05) and @1547 (a8_00), plus `12-94`
  @64 — "prenne" already has an established encoding. A second encoding is
  possible in a homophonic cipher but needs its own demonstration, absent here.
- Polyvalence tension: 61="pren" sits uncomfortably close to pencil 70="pre"
  with no polyvalence declared (67 et/veut remains the sole one, §7). This
  needs red-team ratification before any promotion, not a worker verdict.
- Complication (not kill): @1205 (a7_00) has `55 61 21` — 55-61 WITHOUT 94,
  followed by 21=NOUN class: "... ce(47) [43] [55-61] NOUN [65]". If the word
  is 55-61-94, this window needs a separate account (bare stem "prend" +
  object? different construction?). Fenced as follow-up F3; it does not force
  the claim false.

### Clause 5: PASS — adverse answered

Adverse was "94='ne' promoted". 94's value is untouched: it contributes its
promoted 'ne' as the word-final syllable of the hypothesized word. The reuse
pattern is precedented by the fenced `70-12-94` ("pre"-"n"-"ne"), and
leftward attachment of 94 is grant-compatible per the R17-018 12/94 duality
(predecessor battery, clause 4). No second 94 value declared. Answered, not
ignored.

## Per-clause verdicts

1. (a1) 55 census — **PASS** (12/12, @-offsets, byte-verified).
2. (a2) "55-81-00 x5" frame — **FAIL** (trigram 3x @25/@550/@1085; bigram 6x;
   finder misread recorded).
3. (a3) 55 triangulation — **FAIL** (no banked/promoted contact pins 55;
   55="re" circular).
4. (b) word demonstration — **FAIL** ("...prenne ce..." compatible, not proven;
   rival fenced 70-12-94 at @347/@1547; 61="pren" vs pencil 70="pre"
   polyvalence tension).
5. (c) 94='ne' intact — **PASS** (adverse answered via fenced 70-12-94
   precedent + R17-018).

Overall: **NULL** — no window forces the claim false (not kill); the bar's
discriminating clauses are not met (not promote). The 78-45-13-55-61-94
formula x2 and the @1167 "...prenne ce..." compatibility keep the lead alive.

## Follow-ups (null regenerates work — proposed targets for the supervisor)

**F1 — seg-55-re-prefix** (narrower bar on 55's value). Test 55="re" as a
verbal prefix independent of the prenne claim. Bars: (a) census the corrected
6 x 55-81 bigram windows (@25, @523, @550, @1085, @1094, @1671) plus the 2 x
55-83 and 1 x 55-68 windows; (b) demonstrate 55 as a prefix in ≥2 distinct
stems where a "re-" reading yields a grammatical French verb and a rival
reading breaks; (c) keep 81="prin" kill intact. Adverses: 55="re" untested;
55-81-00 x5 misread corrected to bigram x6.

**F2 — seg-61-pren-polyvalence** (discriminating frame for the 61="pren" /
70="pre" tension). Bars: (a) compare the fenced 70-12-94 "prenne" windows
(@347 a2_05, @1547 a8_00) against the 2 x 55-61-94 windows on left-context
class; (b) find one 61 window where "pren" is forced or one where it is
impossible; (c) keep 67 et/veut the sole polyvalence (§7). Adverses: 70="pre"
pencil; 61="pren" undemonstrated; no polyvalence declared.

**F3 — seg-55-61-21-stem** (word-boundary discriminator at @1205). Bars:
(a) full-row parse of a7_00 around @1205: `58 47 43 55 61 21 65` =
"[58] ce [43] [55-61] NOUN [65]"; (b) decide whether 55-61 is a bare stem
("prend" + noun object) or 94's absence breaks the 55-61-94 word unit —
one grammatical parse either way; (c) keep 21=NOUN class promoted.
Adverses: 43, 58, 65 unknown; 55-61-94 word claim undemonstrated.

---
*Worker: battery agent 0060ab45 (supervisor dispatch). Lock created
2026-10-09T02:48:33Z, deleted on completion. Stream: repaired 1,847-pair parse
(repaired_offsets.json + upstream-ct_R5005.txt). canonical.py untouched; R5005
and sealed gates untouched.*
