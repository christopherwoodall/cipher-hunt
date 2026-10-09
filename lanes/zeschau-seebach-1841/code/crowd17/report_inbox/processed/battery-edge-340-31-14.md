# Battery report: edge-340-31-14

Target: edge-340-31-14
Claim: '…03 qui 31 14 ce qui…' resolves once 31/14 are named
Worker: subagent fe1879b6-82dd-450a-a289-df75d95e2728
Date: 2026-10-09
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered)

"(a) 31 and 14 each named with contact profiles; (b) the 'qui 31 14 ce qui par suite ce [01]' sequence parses as one grammatical run or is fenced to a clause boundary with stated cause; (c) 14's other 14 windows show no contradiction with the chosen parse"

## Bar restated as numbered pass/fail clauses

1. Clause (a): 31 and 14 each named (class-level or better) with byte-exact contact profiles.
2. Clause (b): the sequence 'qui 31 14 ce qui par [43] ce [01]' (0-based @337–345, row a2_05) parses as one grammatical run under standing values, OR is fenced to a clause boundary with stated cause.
3. Clause (c): 14's other 14 windows show no contradiction with the parse chosen in (b).

## Method

Re-derived the stream in-session (1,847 pairs / 96 types verified). Byte-located the target: 1-based @338–345 = 0-based @337–344 `64 31 14 45 64 96 43 87` + @345 `01`, mid-row a2_05. Built full contact censuses for 31 (n=8) and 14 (n=15). Tested every 14-role hypothesis at @339 against 1841 French grammar under standing values; enumerated all 8 clause-boundary placements. Adopted as premises (not re-litigated): 64='qui' banked GT, 45='ce' HOLD (A11), 96='par' promoted, 87='ce' promoted, 14's verb class fenced lane-wide (stem-14-84-retest, NULL 2026-10-09), 14='le' kill-grade dead at @1121 (le-14-kill-1121), ce-frame-45-64-96-43-87-01's fence of this edge (NULL 2026-10-08), noun-43's noun-value kills ({suite, maniere, condition, mesure} all kill-grade dead — la-frame-52-37-43-noun 2026-10-09).

## Window-level evidence

Target window, 0-based @336–345 (row a2_05, mid-row): `03 64 31 14 45 64 96 43 87 01`.

**31 contact profile (n=8, byte-exact):**
- Predecessors: 64 x2 (@337, @1646), 08 x2 (@881, @1488), 61 (@1256), 79 (@882), 83 (@1614), 48 (@1614→1615: 48 31 76)
- Successors: 14 (@339), 79 (@883), 29 (@1258), 92 (@1490), 11 x2 (@1517, @1523), 24 (@1522), 76 (@1616), 10 (@1648)
- **Naming: VERB class.** Three frame-legs: (1) "qui [31]" x2 (@338, @1647 — relative "qui" selects a finite verb); (2) "31 29" @1257 = "[31]er" word-internal infinitive (A10 pattern, cf. 43-29, 03-29); (3) "48 [31] 76" @1615 = "e [31-verb] [76-noun]" verb+object. Value open — no value declared (§7 honored).

**14 contact profile (n=15, byte-exact):** predecessors {87, 62, 21, 66, 69, 64, 47, 13, 19, 82, 24, 98, 06, 79 x2}; successors {24 x2, 06 x2, 21, 74, 45, 62, 02, 00, 59, 29, 98, 60 x2}. Profile is split: determiner-shaped @117 ("et [14] [21-noun]"), noun-compatible @72 ("ce [14-noun] [24-verb]") and @424 ("ce [14] [62]"), adjective-compatible @178 ("[69-noun] [14-adj] [24-verb]"); verb class fenced; 14='le' killed at @1121; @1121 residual fenced.

**Clause (b), arm 1 — one grammatical run: FAILS under every 14-role.**
The irreducible break is downstream of 31/14: 0-based @340–342 = `45 64 96` = "ce qui par". Under standing values (45='ce' HOLD — the {13,01} exclusivity partition keeps "dict" away from this window, neighbors 14/64; 64='qui' banked GT; 96='par' promoted), "ce qui" requires a finite verb and a preposition cannot serve. Role-by-role at @339:
- 14 = finite verb: fenced lane-wide (stem-14-84-retest).
- 14 = determiner ('le'-shaped): "qui [31] le ce(45)…" — "le ce" ungrammatical.
- 14 = noun: "qui [31-fin] [14-noun] ce(45) qui(64) par(96)…" — "ce qui par" ungrammatical.
- 14 = adjective/adverb/pronoun: all strand on "ce qui par" identically.
No 14-role repairs the downstream break. The ce-frame battery's conditional rescue ("par suite" adverbial via 43="suite") is voided: suite is kill-grade dead as a noun value, and even as an adverbial it does not supply "qui" with a verb.

**Clause (b), arm 2 — fence to a clause boundary: FAILS at all 8 placements.**
- After @337 ("…qui | [31]…"): right piece opens "[31] [14] ce qui par…" — dead.
- After @338: right piece "[14] ce qui par…" — dead for every 14-role.
- After @339: right piece "ce(45) qui(64) par(96)…" — "ce qui par" dead.
- After @340: right piece "qui(64) par(96)…" — "qui par" dead.
- After @341: left piece "…ce(45) qui(64)" verbless — dead.
- After @342: left piece "…qui(64) par(96)" — dead.
- After @343/@344: fragments; left pieces lack "qui"+verb.
No placement yields two grammatical pieces. The ungrammaticality is structural, not a matter of 31/14's openness.

**Clause (c):** moot — no parse was chosen in (b). 14's other windows were censused (above); the "no resolving role" conclusion is consistent with 14's split profile and does not contradict any standing verdict.

## Per-clause pass/fail

1. Clause (a) — PARTIAL PASS: 31 named (verb class, 3 frame-legs, value open); 14's profile stated, no resolving role exists.
2. Clause (b) — **FAIL at kill grade**: the sequence parses as no grammatical run under any 14-role, and no clause-boundary placement rescues it. The claim's premise — that naming 31/14 resolves the edge — is forced false by the downstream "ce qui par" break, which is independent of 31/14's values.
3. Clause (c) — moot (no parse chosen); no contradiction introduced.

## Adverses

- "31's and 14's values open": answered — 31 is named at class level only (value stays open, §7 honored); 14's value stays open; the kill does not depend on naming values. The ce-frame battery's "open values, not a contradiction" fence is superseded by new evidence (suite's kill-grade death voids its conditional rescue), not contradicted.

## Phase caveat (stated, not hidden)

Row a2_05's offset (0) is unvalidated — one of the 68 unvalidated upstream offsets. Under offset-1 the "64 31 14 45 64 96" digit run dissolves entirely (re-pairs to "36 43 11 44 56 49 64 38"), and a2_05 sits in the phase-uncertainty list (rival phase favored by 3.35 nats, phase-likelihood-row-sweep). **This kill holds on the canonical repaired stream per protocol; it dissolves if a2_05 re-phases** — same mechanism class as seg-a1_01 ("la tout") and reseg-1481-98.

## Verdict: KILL

The claim "'…03 qui 31 14 ce qui…' resolves once 31/14 are named" is kill-grade dead on the canonical stream: the window forces it false. Naming 31 (verb class, established here) and exhausting 14's roles cannot resolve the edge, because the break — "ce qui par" under banked/promoted values — lies downstream of both cells and admits no clause-boundary rescue. This upgrades ce-frame-45-64-96-43-87-01's fence to a kill, superseding it with the post-suite-kill evidence. No standing red-team verdict contradicted; §7 intact; no values named.

## Follow-up targets (for supervisor queuing; det-14-census already queued, not duplicated)

1. phase02-a2_05-reseg (P3) — run the seg-a1_01-style constraint sweep on row a2_05 under offset-1; if constraint-clean, this kill dissolves and the edge re-opens under the new phase; if violations appear, the kill hardens to phase-independent.
2. val-31-verb-test (P3) — name 31's verb value (finite vs stem) at the "qui [31]" x2 + "31 29" frames; 31's verb class (3 legs, established here) is battery-grade material for red-team ratification.
