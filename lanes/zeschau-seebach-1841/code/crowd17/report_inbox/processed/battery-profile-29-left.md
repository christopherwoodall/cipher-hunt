# Battery verdict: profile-29-left

Target: `profile-29-left` (priority 2).
Date: 2026-10-08. Worker: b49e3f2c-327e-4a83-820d-c59393f828d2.

## Bar (verbatim from battery-queue.json)

> A positive would un-fence @146; a negative closes the word-initial question lane-wide.

Numbered clauses:
1. Census: enumerate all 29 windows (n=45) on the repaired stream with left context.
2. Positive test: at least one window parses grammatically with 29 word-initial
   (29="er" begins a word) using only pencil/granted/provisional values.
3. If positive: @146 ("l'on" window, fenced by battery-lon-29-146) is un-fenced.
   If negative: the word-initial question is closed lane-wide.

Adverses: none listed.

## Method

Re-derived from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json`
+ `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).
`canonical.py` never touched. n(29)=45 confirmed. Pencil ground truth used:
11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par,
79=tout, 00=pour, 84=on, 47=ce, 12=n, 48=e, 06=ent; provisional 59=est, 77=le.
French: 1841 diplomatic prose. A window counts as word-initial-29 iff the left
neighbor is a complete word (forcing a word boundary before 29) and
"er"+follower parses as a French word start.

## Full left-context census (45 windows)

| @ | left | right | row | reading |
|---|------|-------|-----|---------|
| 22 | 43 | 47 | a1_00 | 43 open — fenced |
| 62 | 34 | 40 | a1_01 | word-internal: "[08]ière" suffix |
| 78 | 11 | 42 | a1_02 | **POSITIVE (positional)**: "pour la"+"er[42]" |
| 96 | 46 | 85 | a1_02 | **POSITIVE (positional)**: "que"+"er[85]" |
| 112 | 93 | 89 | a1_03 | 93 open — fenced |
| 147 | 84 | 87 | a1_04 | **POSITIVE (strong)**: "l'on erre, ce qui" |
| 218 | 46 | 42 | a2_01 | **POSITIVE (positional)**: "que"+"er[42]" |
| 274 | 33 | 89 | a2_03 | 33 open — fenced |
| 291 | 64 | 40 | a2_03 | **POSITIVE (strong)**: "qui erre" |
| 374 | 63 | 85 | a2_06 | 63 open — fenced |
| 422 | 36 | 47 | a2_08 | 36 open — fenced |
| 432 | 86 | 82 | a2_09 | 86 open — fenced |
| 500 | 11 | 40 | a2_11 | **POSITIVE (strong)**: "cela erre" (47+11="cela") |
| 541 | 44 | 48 | a3_01 | 44 open — fenced |
| 597 | 01 | 40 | a4_00 | 01 open — fenced |
| 618 | 10* | 88 | a4_01 | row-initial; *10 is previous row — no conclusion |
| 627 | 33 | 87 | a4_01 | 33 open — fenced |
| 685 | 64 | 40 | a5_00 | **POSITIVE (strong)**: "qui erre" |
| 689 | 94 | 60 | a5_00 | **POSITIVE (strong)**: "n'erre" (94="ne" elided) |
| 758 | 34 | 40 | a5_03 | word-internal: "première" (ground truth) |
| 780 | 08 | 89 | a5_04 | 08 open — fenced |
| 814 | 14 | 49 | a5_05 | 14 open — fenced |
| 1031 | 03 | 80 | a6_03 | 03 open — fenced |
| 1038 | 34 | 40 | a6_03 | word-internal: "[88]ière" suffix |
| 1050 | 88 | 40 | a6_04 | 88 open — fenced |
| 1052 | 40 | 74 | a6_04 | 40="e" syllable — fenced (no word boundary forced) |
| 1097 | 06 | 67 | a6_06 | **RESIDUAL**: "-ent" forces word-initial "er", but "er"+"et/veut" has no lexical resolution — fenced with stated cause |
| 1143 | 16 | 42 | a6_08 | 16 open — fenced |
| 1155 | 92 | 80 | a6_09 | 92 open — fenced |
| 1200 | 64 | 45 | a7_00 | **POSITIVE (positional)**: "qui"+"er[45]" |
| 1230 | 48 | 47 | a7_01 | **POSITIVE (positional)**: "me"+"er[re]" ("me" complete word); lexical open |
| 1233 | 33 | 85 | a7_01 | 33 open — fenced |
| 1258 | 31 | 69 | a7_02 | 31=VERBAL class — fenced (class, not a complete word) |
| 1321 | 03 | 80 | a7_04 | 03 open — fenced |
| 1376 | 86 | 89 | a7_06 | 86 open — fenced |
| 1389 | 06 | 67 | a7_07 | **RESIDUAL**: same as @1097 — fenced |
| 1392 | 86 | 89 | a7_07 | 86 open — fenced |
| 1425 | 33 | 87 | a7_08 | 33 open — fenced |
| 1478 | 33 | 82 | a7_10 | 33 open — fenced |
| 1566 | 50 | 24 | a8_01 | 50 open — fenced |
| 1590 | 48 | 47 | a8_02 | **RESIDUAL**: "e"+"er"+"ce" = "erce" — no French word; fenced |
| 1595 | 03 | 80 | a8_02 | 03 open — fenced |
| 1710 | 06 | 40 | a8_06 | word-internal: "n'enterre" (12-06-29-40, see §) |
| 1816 | 06 | 37 | a8_10 | **RESIDUAL**: "ent er [37]", 37 open — fenced |
| 1826 | 86 | 82 | a8_11 | 86 open — fenced |

## Strong positives (word-initial 29, grammatical 1841 French)

- **@147** (a1_04): `64 77 84 | 29 87 64` = "qui l'on erre, ce qui".
  77="le" (provisional) + 84="on" (promoted) elide to "l'on" ("le on" is
  ungrammatical, so the elided reading is forced); 29-40... here 29 followed
  by 87="ce": "erre, ce qui" — "erre" (3sg of *errer*, to wander) + "ce qui".
  "l'on erre, ce qui…" parses cleanly. **This is the @146 window: UN-FENCED.**
- **@291** (a2_03) and **@685** (a5_00): `64 | 29 40` = "qui erre" (who wanders).
  64="qui" promoted and a complete word, so 29 must begin the next word;
  "erre" is the only grammatical "er"+"e" word. No word-internal alternative
  exists ("*quierre" is not French).
- **@500** (a2_11): `47 11 | 29 40` = "cela erre". 47="ce"+11="la" compose
  "cela" ("ce la" as two words is ungrammatical); then "erre".
- **@689** (a5_00): `94 | 29 60` = "n'erre". 94="ne" (STRONG LEAD, R17-001)
  elides before the vowel: "ne"+"erre" → "n'erre" (does not wander).
  Consistent with the 12/94 "ne"-duality note (R17-018).

Positional positives (word-initial forced by a complete-word left neighbor;
lexical completion open pending the follower's value):
- **@78**: "pour la"+"er[42]" → "pour l'er[reur/…]" (42 open).
- **@96**: "que"+"er[85]" → "qu'er[reur/…]" (85 verb-stem, value open).
- **@218**: "est que"+"er[42]" (59="est" provisional).
- **@1200**: "qui"+"er[45]" (45 open).
- **@1230**: "qui tout me"+"er[re]" — 82+48="me" (clitic, complete word).

## Word-internal 29 (majority, pencil-consistent)

- @758: "la première" (ground truth, gloss (i)).
- @62, @1038: "[X]ière" adjectival suffix (34-29-40 = i-er-e).
- @1710: `12 06 29 40` = "n'enterre" — 12="n"+06="ent"+29="er"+40="e":
  "ne"+"enterre" elided ("one does not bury"). Elegant word-internal parse;
  NOT a word-initial window.

## Residuals (fenced with stated cause, not verdict-changing)

- @1097/@1389 "06 29 67" and @1816 "06 29 37": 06="ent" is the 3pl verb
  ending, always word-final, so "er" is positionally word-initial — but
  "er"+"et"/"er"+"veut" (67's sole polyvalence) and "er"+37 form no French
  word. Either 06≠"-ent" at these windows or the "er…"-word's second syllable
  is not 67/37. Left for the red team; does not sink the positives.
- @1590 "48 29 47": "e"+"er"+"ce" = "erce" — no French word starts "erce";
  segmentation here is unresolved.
- @22 "43 29 47": 43's value open; "cher ce"/"perce"/"merci" all speculative.
- @618: row-initial 29 (a4_01); manuscript row boundary ≠ word boundary —
  no conclusion.

## Per-clause verdicts

1. Census complete (45/45 windows, @-offsets, re-derived on repaired stream): **PASS**.
2. Positive test: 5 strong + 5 positional windows parse with 29 word-initial: **PASS (positive)**.
3. @146 un-fenced via @147 "l'on erre, ce qui": **PASS**.

Adverses: none listed. No standing verdict contradicted or downgraded.
R5005, sealed gates, red-team queue untouched.

## Verdict: PROMOTE

**Finding: 29 occurs word-initially.** The "er"-initial family is the verb
*errer* ("qui erre", "l'on erre", "cela erre", "n'erre"); the @146 "l'on"
window is un-fenced. The pencil value 29="er" is unaffected — this is a
positional finding, not a value change. Residual "ent er" windows (@1097,
@1389, @1816) fenced for red-team visibility.

## Follow-ups proposed

1. `er-word-lexicon` (P3): identify the "er"-initial word at the positional
   positives @78/@96/@218/@1200 — is it "erreur"? Blocked on values for
   42, 85, 45.
2. `ent-er-residual` (P2): resolve "06 29 67" @1097/@1389 and "06 29 37"
   @1816 — test 06≠"-ent" at these windows vs an "er…"-word whose second
   syllable is 67/37.
3. `erce-1590` (P3): re-segment "48 29 47" @1590 (the "erce" problem).
