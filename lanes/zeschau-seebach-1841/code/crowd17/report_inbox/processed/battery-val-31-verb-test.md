# Battery report: val-31-verb-test

**Target:** `val-31-verb-test` (P3)
**Claim:** name 31's verb value (finite vs stem) at the "qui [31]" x2 + "31 29" frames.
**Verdict: NULL**

## Bar (verbatim, pre-registered)

"31's verb class (3 legs, established here) is battery-grade material for red-team ratification"

Restated as numbered pass/fail clauses:

- **C1:** The two "qui [31]" windows (@338, @1647) license finite-verb 31 with zero new assumptions under standing values.
- **C2:** The "31 29" window (@1257) licenses verb-stem 31 ("[31]er" as infinitive) with zero new assumptions under standing values.
- **C3:** The three legs jointly establish 31's verb class at battery grade, suitable as red-team ratification material, with no standing/red-team verdict contradicted.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `repair_parse.py`). Asserts held: 1,847 pairs, 96 types.
`canonical.py` never used. n(31)=8. Byte-exact census: "64 31" occurs exactly
twice (@337, @1646 — i.e. 31 at @338 and @1647); "31 29" occurs exactly once
(@1257). No row-boundary artifacts.

Standing values used: 64="qui" (granted), 29="er" (pencil GT letter cell),
40="e" (pencil GT), 46="que" (pencil GT), 45="ce" (A11), 14="en"
(battery-grade, usable per §7).

## Window-level evidence

### Leg 1 — @338, row a2_05: `45 54 88 40 03 64 31 14 45 64 96 43 87`

Reads "ce [54] [88] e [03] **qui [31]** en ce que par [43] ce".

- 64="qui" (granted) in subject-relative form requires a finite verb in its
  clause; 31 sits immediately post-"qui".
- Boundary: follower 14="en" is battery-grade as a standalone word; a
  word-internal "31-en" reading would contradict that standing value.
  Under §7, 31 is standalone here.
- "en ce que" is a licensed 1841-French construction after verbs of
  distinction; not a contradiction (grammar as test apparatus).
- **C1 leg 1: PASS** — finite-verb 31 at battery grade, zero new assumptions.

### Leg 2 — @1647, row a8_04: `12 33 98 60 03 64 31 10 03 38 82 16 01`

Reads "[12] [33] [98] [60] [03] **qui [31]** [10] [03] [38] m [16] [01]".

- Same "qui [31]" geometry: 31 = finite verb, standalone (follower 10 is
  unvalued; no standing license for word-internal "31-10").
- "[31] [10] [03] [38]" parses as finite verb + complements; no standing
  value contradicted.
- **C1 leg 2: PASS** — finite-verb 31 at battery grade, zero new assumptions.

### Leg 3 — @1257, row a7_02: `30 06 65 46 01 61 31 29 69 88 01 09 11`

Reads "[30] [06] [65] que [01] [61] **[31]er** ce [88] [01] [09] la".

- 29="er" is a pencil-GT letter cell, so "[31]er" is a word ending in "er".
- For 31 to be a verb STEM, "[31]er" must be an infinitive, which requires a
  governor: 01 is unvalued (`val-01-census` NULL, 2026-10-09 — 'en' and 'tain'
  dead at kill grade, no uniform value), and 61 is unvalued and NOT in its
  premier-licensing slot here (left neighbor 01 is not a determiner cell,
  right neighbor 31 is not noun-class — `premier-61-admit-fence` PROMOTE,
  2026-10-09). No standing license puts an infinitive after 01 or 61.
- The rival reading — "[31]er" as a noun (French nouns in -er exist) — is
  equally unforced: "que [01] [61] [N] ce [88]" has no licensed parse under
  standing values either.
- The frame therefore does not discriminate: infinitive needs an ungranted
  governor; noun needs an ungranted parse. Naming verb-stem 31 here would be
  a new assumption.
- **C2: FAIL** at battery grade — the "31 29" window does not license
  verb-stem 31 with zero new assumptions.

### Hostile sweep (other 31 windows)

- @882 (`78 17 08 31 79 68 37`, "…[08] [31] tout [68]…"): consistent with
  verb-31; no contradiction.
- @1489 (`24 87 08 31 92 39 24`): no standing license either way.
- @1516 (`81 88 11 31 11 91 67`, "la [31] la"): consistent with finite-31
  ("la" object pronoun + finite verb + "la [91]" determiner phrase), but
  requires 88 non-finite or a clause boundary after 88 here — not tested;
  left as follow-up.
- @1521 (`91 67 08 31 24 11 11`, "[31] [24-fin/modal]"): no forced reading.
- @1615 (`83 71 48 31 76 42 44`): no standing license either way.
- No window forces 31 non-verb at kill grade. The claim is NOT falsified.

## Per-clause results

- **C1: PASS** — both "qui [31]" legs license finite-verb 31, zero new assumptions.
- **C2: FAIL** — the "31 29" leg does not license verb-stem 31 without new assumptions.
- **C3: FAIL** — 2 of 3 legs is insufficient for the bar as written; the joint
  3-leg establishment of 31's verb class is not earned at battery grade.

**Verdict: NULL.** The finite-verb legs (@338, @1647) stand; the stem leg
(@1257) does not. No standing or red-team verdict is contradicted (§5.2 does
not fire); no value is named.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-31-finite-name` (P3) — name 31's finite value from the two "qui [31]"
   legs: test candidate finite verbs against @338 ("qui [31] en ce que",
   left "e [03]") and @1647 ("qui [31] [10] [03] [38] m [16] [01]").
   Bar: name iff one value parses both windows with zero new assumptions,
   else fence.
2. `val-31-1257-word` (P3) — decide the "[31]er" word at @1257: infinitive
   (name the governor) vs noun (name the word) vs word-internal-31.
   Bar: name the word with byte evidence, else fence all three arms at the locus.
3. `val-31-1516-finite` (P4) — test finite-31 at @1516
   ("[81] [88] la [31] la [91]") as a corroborating third finite leg.
   Bar: parse with zero new assumptions, else fence.

## Scope

Names nothing. The two finite-verb legs are battery-grade material for the
red team as stated in the bar; the @1257 stem leg is not. Untouched: 31's
value, 01's value, 61's value, 10's class, 88's value at @1262/@1517.
§7 intact. Canonical-stream caveat stands.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-31-verb-test.md`
- Queue: `val-31-verb-test` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  disk re-read confirms; own entry only; no downgrade)
- Lock created on start (2026-10-09T15:40:30Z), deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
  `canonical.py` never used. No follow-ups were written into battery-queue.json
  by this worker (supervisor queues per §4); own entry only.
