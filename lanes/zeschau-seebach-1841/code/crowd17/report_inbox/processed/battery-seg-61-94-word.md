# Battery verdict: seg-61-94-word

**Verdict: NULL** — leftward attachment of 94 stays grant-compatible, but no French word
61-94 is demonstrated and 61's value does not triangulate. New lead: 55-61-94 may be
the true word unit (re-/com-/sur-prenne family).

## Bar (verbatim from battery-queue.json)

(a) census 61's 18 windows and triangulate 61's value via contact profiles; (b) demonstrate
a French word 61-94 that yields a grammatical '...ne ce...' parse at @1169 with stated
agreement; (c) keep 94='ne' value intact (section 7 - no second value declared).

## Numbered clauses

1. (a1) Census: enumerate all 18 windows of 61 on the repaired stream with @-offsets.
2. (a2) Triangulation: name 61's value (or class) from contact profiles with banked values.
3. (b) Demonstrate one French word 61-94 + grammatical "...ne ce..." parse at @1169
   with stated agreement.
4. (c) 94='ne' (R17-001 STRONG LEAD) undisturbed; no second 94 value declared (§7).

## Method

Read BATTERY-PROTOCOL.md first; created `locks/seg-61-94-word.lock` on start.
Parsed the repaired 1,847-pair stream from `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt` with the upstream byte-exact tokenization
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]`). `canonical.py` never touched. R5005,
sealed gates, and the red-team queue untouched. Every count re-derived; no prior
counts trusted.

## Window-level evidence

### The two 61-94 windows (clause 1: PASS — exactly 2, both byte-verified)

- @577 (row a3_02, pair-index-in-row 20):
  `... 87 78 45 13 55 | 61 94 | 82 06 06 50 10 19 ...`
  (87=ce granted; 82=m pencil; 06=ent promoted)
- @1168 (row a6_09, pair-index-in-row 16):
  `... 67 78 45 13 55 | 61 94 | 87 83 21 85 36 74 ...`
  (87=ce granted; 21=NOUN class promoted)

Both share the identical left 4-gram `78 45 13 55`. The 4-gram `78-45-13-55`
occurs exactly 2x stream-wide, both followed by `61 94` — i.e. the 6-gram
`78-45-13-55-61-94` is a fixed formula x2, differing only in 94's follower
(82 @577 vs 87 @1168).

### 61 census: n=18 (clause 1: PASS)

| @ | row | context (r=8) |
|---|---|---|
| 223 | a2_01 | 06 59 46 29 42 16 24 89 **61** 96 87 46 98 83 82 96 21 |
| 279 | a2_03 | 06 67 33 29 89 84 91 37 **61** 20 61 42 48 52 89 28 00 |
| 281 | a2_03 | 33 29 89 84 91 37 61 20 **61** 42 48 52 89 28 00 97 09 |
| 367 | a2_06 | 21 62 48 76 47 78 48 49 **61** 70 17 06 21 65 63 29 85 |
| 447 | a2_09 | 43 98 80 50 78 41 10 62 **61** 59 32 48 79 17 77 60 65 |
| 577 | a3_02 | 45 94 52 87 78 45 13 55 **61** 94 82 06 06 50 10 19 18 |
| 645 | a4_02 | 60 67 77 89 48 20 24 87 **61** 88 77 78 52 82 94 76 49 |
| 926 | a5_10 | 49 74 74 40 08 65 71 17 **61** 96 48 82 98 83 56 69 26 |
| 1168 | a6_09 | 44 83 21 67 78 45 13 55 **61** 94 87 83 21 85 36 74 32 |
| 1206 | a7_00 | 16 64 29 45 58 47 43 55 **61** 21 65 64 59 32 48 96 45 |
| 1219 | a7_01 | 32 48 96 45 36 77 83 92 **61** 24 48 30 09 20 57 64 79 |
| 1256 | a7_02 | 67 46 26 30 06 65 46 01 **61** 31 29 69 88 01 09 11 50 |
| 1281 | a7_03 | 76 87 76 48 56 85 48 53 **61** 56 32 98 55 68 00 11 17 |
| 1429 | a7_08 | 33 21 67 33 29 87 63 91 **61** 12 16 76 49 64 52 82 16 |
| 1455 | a7_09 | 84 59 36 67 33 46 92 62 **61** 21 67 86 66 79 17 01 21 |
| 1510 | a7_11 | 33 42 33 00 86 56 41 12 **61** 59 39 81 88 11 31 11 91 |
| 1556 | a8_01 | 12 94 92 45 23 99 13 93 **61** 40 17 11 26 30 06 60 71 |
| 1810 | a8_10 | 77 84 59 35 94 52 80 04 **61** 15 93 50 42 06 29 37 01 |

Predecessors: 55 x3, 62 x2, 89/37/20/49/87(=ce)/17(=fois)/92/01/53/91/12(=n)/93/04 x1.
Followers: 96(=par) x2, 59(=est prov.) x2, 94 x2, 21(=NOUN) x2, 20/42(=NOUN)/70(=pre)/
88/24(=finite verb)/31/56/12(=n)/40(=e)/15 x1.

### Triangulation attempts (clause 2)

- **"ce 61"** @644 (`24 87 61 88 77` = [finite-verb] ce 61 [88] [77]): determiner frame —
  61 is noun/adjective-shaped here.
- **"61 par"** x2 (@223 `89 61 96 87 46` = [89] 61 par ce que; @926 `17 61 96 48` =
  fois 61 par e): verb-shaped ("[V] par...") at @223 where 96-87-46 = "par ce que"
  is a real French construction; @926's "fois 61 par" resists a verb reading.
- **"61 est"** x2 (@447 `62 61 59 32`; @1510 `12 61 59 39` = n 61 est [39]):
  @1510 suggests a proclitic ("n'en est" / "n'y est" shape) rather than a verb stem.
- **"61 NOUN"** x3 (@281 `61 42`; @1206 `55 61 21`; @1455 `62 61 21`): adjective-before-noun
  or noun-noun stacking — nominal frame.
- **"61 e fois"** @1556 (`93 61 40 17`) and **"61 pre fois"** @367 (`49 61 70 17`,
  70=pre pencil, 17=fois promoted): ordinal/quantifier frame — incompatible with a
  verb-stem value like "do"/"vie"/"tie".
- **"61 12"** x1 @1429 (`91 61 12 16`): 61 precedes 12=n once; no 94 follows, so the
  prenne-family shape (stem-12-94) does not reproduce here.

**Result: 61 occupies determiner frames, verbal frames, AND an ordinal/quantifier
frame ("61 e fois" / "61 pre fois"). No single value or class is demonstrated.
Clause 2: FAIL** (attempt complete, negative result — not ignored).

### The prenne-family precedent (bears on clause 3)

The stream's established "...ne" word is `70-12-94` ("pre"-"n"-"ne" = "prenne",
fenced) at @347 and @1547, plus `12-94` @64. The family shape is **stem-12-94** —
the medial 12="n" is present. `61-94` lacks the medial 12. For 61-94 to be a
"...ne" word, 61 itself must supply the stem-final "n" (e.g. 61="pren"/"don") —
undemonstrated, and "pren" is uncomfortably close to pencil 70="pre" without
being identical (no polyvalence declared; 67 et/veut remains the sole one).

### Right-context agreement at @1169 (partial support, not demonstration)

`61 94 | 87 83 21` = "[61-94] ce [83] NOUN": "ce" + [83] + NOUN parses as
determiner-adjective-noun (cf. "ce grand homme") **if** 61-94 is a verb
(imperative/subjunctive "prenne/reprenne ce [adj] [N]"). Grammatical in 1841
French — but conditional on the undemonstrated verb value. **Clause 3: FAIL**
(no word demonstrated; agreement noted as compatible, not proven).

### New lead found during testing: 55-61-94 as the true word unit

Both 61-94 windows sit inside `13 55 61 94`. 55's followers: 81 x6, 61 x3,
83 x2, 68 x1. If 55 is a prefix ("re"/"com"/"sur"/"ap"), then `55-61-94` =
"reprenne"/"comprenne"/"surprenne"/"apprenne" — the subjunctive "...prenne"
family with 61="pren". This keeps 94 leftward-attached (claim's core insight)
but re-segments the word boundary one group left. 55="re" is untested;
`55-81-00` (x5, 00=pour) is the discriminating parallel frame. Proposed as
follow-up `seg-55-61-94-word` below. The claim as written (61-94 = the word)
is not demonstrated either way.

### Clause 4: PASS

Nothing in this battery disturbs R17-001 (94='ne' STRONG LEAD). No second 94
value declared or needed; leftward attachment is explicitly grant-compatible
with the fenced 12/94 duality (R17-018).

## Per-clause verdicts

1. (a1) census — **PASS** (18 windows, @-offsets, byte-verified).
2. (a2) triangulation — **FAIL** (heterogeneous frames; no value demonstrated).
3. (b) word demonstration — **FAIL** (no 61 value; "prenne" blocked by 70="pre";
   stem-12-94 precedent lacks the medial 12 in 61-94).
4. (c) 94='ne' intact — **PASS**.

Overall: **NULL** (not kill — no window forces the claim false; the leftward-
attachment insight survives via the 55-61-94 re-segmentation lead).

## Follow-ups proposed (null regenerates work)

1. **`seg-55-61-94-word`** (P2): test `55-61-94` as a single word
   (re-/com-/sur-/ap-prenne family). Bars: (a) triangulate 55 via the `55-81-00`
   x5 parallel frame and 55's 12-window census; (b) demonstrate the full word
   with grammatical "...prenne ce..." parse at @1169; (c) keep 94='ne' intact.
2. **`val-61-contact`** (P2): dedicated 61 value triangulation on the four
   discriminating frames: "ce 61" @644, "61 par ce que" @223, "n 61 est" @1510,
   "61 e/pre fois" @1556/@367. Bars: one value covering all four or fenced
   polyvalence escalated to red team.
3. **`leftedge-13-55`** (P3): resolve 13's and 55's classes to fix the left edge
   shared by both 61-94 windows (`78-45-13-55-61-94` formula x2); gates the
   word-boundary decision for seg-55-61-94-word.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-61-94-word.md` (this file).
- Queue: `seg-61-94-word` → status `verdict`, result `null`, date 2026-10-08
  (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict).
- Lock `locks/seg-61-94-word.lock` created on start, deleted on completion.
- Standing verdicts: none contradicted, none downgraded. R5005, sealed gates,
  red-team adjudication queue untouched.
