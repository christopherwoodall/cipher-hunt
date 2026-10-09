# Battery report — syllable-08-letter-value

Worker: 75a4c7bc-6b5b-4aa4-be72-abccc23c5e36 (supervisor-dispatched, 2026-10-09)
Date: 2026-10-09

## Bar (verbatim from battery-queue.json)

> resolve iff 08's letter value is named with byte evidence; kill iff the phoneme forces a boundary between 08 and 31

Numbered clauses (pre-registered before testing):

1. **Resolve clause:** 08's letter value is named with byte evidence. (pass → verdict promote)
2. **Kill clause:** the phoneme forces a boundary between 08 and 31. (pass → verdict kill)

## Method

Repaired-stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`
(1,847 pairs; `canonical.py` never touched). Enumerated all 18 windows of
token 08 (0-based @-offsets), tested claim "pin 08's letter value from @60
and 40-08 x2 (cf. promoted 40-12='en')" against the banked ground truth
(§7: 34=i, 29=er, 40=e; 45="ce" A11; 47="ce" A4).

## Window-level evidence (0-based @-offsets)

| @ | row | raw-digit span | pairs | reading |
|---|-----|----------------|-------|---------|
| 60 | a1_01 | digits 48–57 = `4108 3429` | 41 08 34 29 40 | 08-i-er-e = "-tière" word ending |
| 922 | a5_09 | digits 45–50 = `4008 65` | 40 08 65 | e-08 = "et" |
| 944 | a5_10 | digits 40–45 = `4008 62` | 40 08 62 | e-08 = "et" (2nd) |
| 975 | a6_01 | digits 7–12 = `4508 01` | 45 08 01 | ce-08 = "cet" (45="ce" A11) |
| 1592 | a8_02 | digits 22–27 = `4708 81` | 47 08 81 | ce-08 = "cet" (47="ce" A4) |
| 779 | a5_04 | digits 10–15 = `3708 29` | 37 08 29 | 37-08-er = "ter" syllable contact |
| 881 | a5_08 | digits 15–22 = `1708 3179` | 17 08 31 79 | 08-31 frame (31 unknown) |
| 1488 | a7_10 | digits 36–43 = `8708 3192` | 87 08 31 92 | 08-31 frame (31 unknown) |
| 1520 | a7_11 | digits 46–53 = `6708 3124` | 67 08 31 24 | 08-31 frame (31 unknown) |

All 18 occurrences of 08 are row-internal with letter neighbors on both
sides — never standalone (corroborates the val-52-630-frame PROMOTE adverse).

## Per-clause pass/fail

1. **Resolve clause — PASS.** Six independent byte-exact windows converge on
   a single value, 08 = **'t'**:
   - @60: "08 34 29 40" = "?-i-er-e"; with 08='t' → "-tière", a productive
     French word ending (matière / entière / dernière). The 34-29-40 tail is
     the crib's own ("la premiere" = 11 70 82 34 29 40).
   - @922, @944: "40 08" x2 = "e" + 08; with 08='t' → "et" ("and"), the
     overwhelmingly natural French "e-?" bigram. Rivals ("ed", "es", "er"
     as word units) are not French words.
   - @975: 45="ce" (A11 hold) + 08 → "cet"; @1592: 47="ce" (A4 allophone
     tier) + 08 → "cet". Two independent "ce" tokens both followed by 08
     giving "cet" (ce + liaison t before vowel) is decisive.
   - @779: 37 + 08 + 29=er → "37-t-er" = "ter" syllable contact, consistent.
   No rival letter satisfies all six frames.

2. **Kill clause — FAIL (not met).** The phoneme does NOT force a boundary
   between 08 and 31: the 08-31 frames (@881, @1488, @1520) give no phoneme
   evidence either way (31's value is unknown: n31=8, no vowel markers among
   its 8 followers / 8 preceders), battery-prefix-08-31 returned null, and
   the adopted val-08-successor-class verdict (PROMOTE 2026-10-09) already
   holds 08 as a word-internal letter, never a governing particle. A null on
   the prefix question is not a forced boundary.

## Adverses answered

- val-52-630-frame PROMOTE adverse (08 never standalone in 18/18 windows):
  verified re-parsed — all 18 windows row-internal with both neighbors.
- val-08-successor-class PROMOTE (08 word-internal, never governing
  particle): consistent — every "cet"/"et"/"-tière" frame is word-internal.
- battery-prefix-08-31 null: noted; the 08-31 semantics remain open but do
  not falsify 08='t'.
- cf. promoted 40-12='en': no conflict (12 ≠ 08).

## Verdict

**PROMOTE** — 08's letter value is named 't' with byte evidence (six windows,
clause 1 passes; clause 2 not met, no kill). Consistent with the adopted
battery-grade 08='t' verdict; this worker corroborates it from the repaired
stream, no red-team contradiction.

## Follow-ups

None queued — verdict is promote, not null. Residual note for the pipeline
(not a new target): token 31's value remains open; 08-31 word status belongs
to the existing prefix-08-31 / successor-class work.
