# Battery report: spell-single-consonant

Target: `spell-single-consonant`. Claim: clerk single-consonant spelling explains
'prenent'/'pasent'. Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed
like `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-verified).
Never used `canonical.py`. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered)

"confirm iff a stated single-consonant spelling rule covers all 5 windows with
zero contradiction; else re-parse each with stated cause"

Numbered clauses:

1. C1 — a single-consonant spelling rule is stated in general form.
2. C2 — the rule covers all 5 windows: each window's letter-string maps via the
   rule to a grammatical French word in its context.
3. C3 — zero contradiction: no standing byte-exact evidence contradicts the rule.
4. Else-branch — if confirmation fails, re-parse each of the 5 windows with
   stated cause.

Offset convention: 0-based token indices (the target evidence's convention);
1-based equivalents in parentheses.

## Target windows (byte-confirmed)

- W1 "prenent": 70-12-06, 70 at 0-based @1118 (1-based @1119-1121), row a6_07.
  Census: the ONLY 70-12-06 trigram stream-wide.
- W2 "pasent": 30-06, 30 at 0-based @1251 (1-based @1252-1253), row a7_02.
- W3 "pasent": 30-06, 30 at 0-based @1327 (1-based @1328-1329), row a7_04.
- W4 "pasent": 30-06, 30 at 0-based @1561 (1-based @1562-1563), row a8_01.
- W5 "pasent": 30-06, 30 at 0-based @1733 (1-based @1734-1735), row a8_07.
  Census: exactly 4 stream-wide 30-06 bigrams — matches the evidence's "x4".

Standing values used: 70='pre', 12='n' (GT/letter); 06='ent' (promoted,
R17-007); 30="pas" (promoted, conditional); 94='ne' (STRONG LEAD R17-001,
battery-promoted).

## Per-clause results

**C1 — stated.** General form: "The clerk writes a single consonant where
standard 1841 French orthography doubles it (nn→n, ss→s)." Under it,
70-12-06 = "pre"+"n"+"ent" → "prennent" (3pl of prendre); 30-06 =
"pas"+"ent" → "passent" (3pl of passer).

**C2 — FAIL.** No window yields a clean instance:

- W1, row a6_07 (1-based): `73 41 65 38 30 69 11 88 | 70 12 06 | 14 06 11 52 37 43`.
  "prennent" needs 88 as 3pl subject — no subject reading for 88 exists under
  standing values (governor/verb-class at class level only; infinitive-shaped
  at the @1727 locus). Worse, "prennent" is immediately followed by "14-06"
  = "[14]ent", stacking two finite verbs with no clause boundary (mid-row, no
  byte evidence for one). The ent-06 battery already graded @1118-1121 "not a
  clean frame". Not an instance of the rule.
- W2, row a7_02: `16 00 67 46 26 | 30 06 | 65 46 01 61 31 29` = "que [26]
  pasent [65] que". "passent" needs 26 = 3pl subject; 26's class is open
  (red-team item: noun vs word-internal). Conditional only — not covered.
- W3, row a7_04: `80 08 62 98 56 | 30 06 | 62 94 70 52 39 83` = "[98] [56]
  pasent [62] [94]". Needs 56 = 3pl subject (open). Conditional only.
- W4, row a8_01: `61 40 17 11 26 | 30 06 | 60 71 50 29 24 74` = "[61]e fois la
  [26] pasent [60]…". "la [26] passent" is ungrammatical — the determiner is
  stranded before the subject, and French does not pro-drop a 3pl subject.
  The target word is grammatically EXCLUDED here. Not an instance of the rule.
- W5, row a8_07: `24 30 15 01 56 | 30 06 | 60 12 48 52 86 12` = "[01] [56]
  pasent [60]…". Needs 56 = 3pl subject (open). Conditional only.

**C3 — FAIL (kill-grade for the general form).** "prenne" = 70-12-94 at
0-based @347-349 (1-based @348-350), row a2_05 (`87 01 06 70 12 94 74 …`),
and at 0-based @1547-1549 (1-based @1548-1550), row a8_00 — battery-confirmed
by enne-family-12-94 (PROMOTE, 2026-10-09): 12='n' + 94='ne' compose as
letters inside one word. The SAME clerk writes the doubled n of "prenne" in
full. The general rule predicts "prene". Direct contradiction at the lane's
byte standard.

**Narrow rescue considered and rejected.** "Single consonant only before
06='ent'" avoids the "prenne" contradiction but is ad hoc — no orthographic
or phonetic principle distinguishes -ent from -ne (both "prennent" and
"prenne" are pronounced with a single /n/). The compositional account
explains the strings with no clerk habit at all: 94='ne' as letters (n-e)
contributes its own initial n, so "pre"+n+"ne" = "prenne" emerges; 06='ent'
as letters (e-n-t) contributes no initial consonant, so "pre"+n+"ent" =
"prenent" emerges; the inventory has no 'ss'/'nent' groups. The "missing"
consonant is an inventory fact, not a scribal choice. The narrow rule is
unproven and unprovable on current evidence — not confirmed.

**Adverse ("re-parse rival (not spelling)") — answered** via the re-parses
below.

## Verdict

**NULL** — the spelling rule cannot be confirmed (general form contradicted by
standing byte evidence; narrow form ad hoc and instance-less). Per the bar's
else-branch, each window re-parsed with stated cause:

1. W1 @1118 (row a6_07): "88 70 12 06 14 06". "prenent" is not a French word;
   "prennent" is unavailable (88 has no 3pl-subject reading under standing
   values; "prennent [14]ent" stacks finite verbs with no boundary). Fenced as
   unparsed pending 88's value and 14's class. Cause: grammar fails
   independently of spelling.
2. W2 @1251 (row a7_02): "46 26 30 06 65 46". Byte-level reading is "pas"+"ent":
   promoted "pas" + promoted 'ent' with no stem — "pasent" is not a French
   word, and "passent" needs 26 = 3pl subject (open). Fenced pending 26's class.
3. W3 @1327 (row a7_04): "98 56 30 06 62 94". Same; "passent" needs 56 = 3pl
   subject (open). Fenced.
4. W4 @1561 (row a8_01): "61 40 17 11 26 30 06 60 71". "la [26] passent" is
   ungrammatical (stranded determiner, no pro-drop). The "passent" reading is
   excluded — this window cannot be an instance of the rule under any
   spelling. Fenced with cause.
5. W5 @1733 (row a8_07): "01 56 30 06 60 12". Same as W2/W3; needs 56 = 3pl
   subject (open). Fenced.

Not kill-grade for the narrow claim: the failures are epistemic (open
subjects/values, ungranted boundaries), not forced falsehoods. No standing
verdict contradicted or downgraded (06='ent', 30="pas", 12='n', 70='pre' all
consistent with the re-parses). §7 intact — no polyvalence declared.

## Follow-ups proposed (all verified absent from battery-queue.json)

1. `pasent-subject-26-56` (P2) — decide 26/56 as 3pl subjects at the four
   30-06 windows (@1251/@1327/@1561/@1733 0-based). If neither can be 3pl,
   the "passent" reading dies grammatically and 30-06 must re-segment.
2. `reseg-1118-88-14` (P3) — re-segment "88 70 12 06 14 06" once 88's value
   and 14's class resolve; test 12-06-14 "n-ent-[14]" vs word-internal
   readings.
3. `inventory-doubling-contrast` (P3) — package the "prenne"-doubled vs
   "prenent"/"pasent"-single contrast for the red team: standing
   falsification of any general single-consonant habit; venue for the
   compositional (group-inventory) account.

## Bookkeeping

- Report: this file.
- battery-queue.json: `spell-single-consonant` → status `verdict`, result
  `null`, date 2026-10-09 (temp-file + rename, own entry only; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write).
- Lock `locks/spell-single-consonant.lock`: created on start, deleted on
  completion.
