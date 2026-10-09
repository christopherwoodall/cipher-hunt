# Battery report: noun-03-gender-test

Worker: c89793cc-6f4a-4b04-a994-2989e3cbdf6f. Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/noun-03-gender-test.lock` created 2026-10-09T16:33:18Z; no prior lock present (no collision).
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed byte-exact per `code/side-keyhunt/repair_parse.py`
(`parse`: `[digits[i:i+2] for i in range(off[lid], len(digits)-1, 2)]`).
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
`@i` = 0-based pair index in the repaired stream (matches the battery-queue brief;
R20 uses 1-based elsewhere — noted to avoid confusion).
Asserts held: 1,847 pairs; 03 occurs 20x; all three briefed windows byte-verified.

## Bar (verbatim, pre-registered before testing)

"name the gender iff it holds across all forced-nominal windows with zero kill-grade contradictions"

Numbered clauses:
- C1 — every forced-nominal window (03 headed by an article/demonstrative) forces the same gender.
- C2 — zero kill-grade contradictions: no window forces the opposite gender, and no distributional rejection of the named gender.

Parent follow-up (battery-val-03-noun, 2026-10-09) noted 47="ce" as "epicene"; that wording is
corrected here under standing values: 47="ce" is GRANTED at A4 (allophone tier), and French
"ce" before a consonant-initial noun is masculine (feminine would require "cette"). The
queue brief's claim (masculine uniformity) is therefore the tested reading; the parent's
loose gloss is battery-grade wording, not a red-team verdict, and this correction contradicts
no standing finding.

## Method

1. Re-derived the repaired stream in-session; located all 20 occurrences of 03 (0-based @31, @336,
   @599, @657, @664, @674, @691, @722, @886, @994, @1014, @1030, @1237, @1320, @1367, @1594,
   @1645, @1649, @1675, @1790).
2. Tabulated the immediate left neighbor of every 03 (the determiner position).
3. Re-parsed the three determiner-headed windows byte-exact with ±6 context.
4. Checked all 20 windows for any feminine-forcing element under §7 standing values.
5. Swept the red-team rounds (esp. R20-131 on 77, R20-038 on 03) for standing verdicts this
   result could contradict.

## Findings

### Window-level evidence (forced-nominal windows)

03-predecessor census (all 20 windows): 60 x4, 30 x3, 40 x2, 80 x2, 47 x2, 10 x2, 77 x1,
37 x1, 01 x1, 24 x1, 81 x1. The only article/demonstrative-headed windows are the three
below (standing nominal values per §7: 77="le" provisional, 47="ce" granted A4).

- @722 (row a5_02, raw offset 2): `86 01 02 21 80 77 [03] 91 65 64 11 00 86`
  → "le [03-N]". Determiner 77="le" (provisional) is masculine. Forced gender: masculine.
- @1014 (row a6_02, raw offset 37): `35 18 79 80 78 47 [03] 24 41 15 66 91 53`
  → "ce [03-N]". Determiner 47="ce" (GRANTED, A4) is masculine before consonant-initial noun.
  Forced gender: masculine.
- @1790 (row a8_09, raw offset 38): `83 82 96 21 68 47 [03] 00 86 56 42 94 59`
  → "ce [03-N]". Same: masculine.

All three forced-nominal windows force masculine. Unanimous.

### C1: PASS

Every forced-nominal window (3/3: @722, @1014, @1790) forces masculine under standing values.

### C2: PASS — zero kill-grade contradictions

- The only feminine determiner in the standing inventory is 11="la" (banked ground truth,
  45x in stream). 11 precedes 03 in 0 of 20 windows.
- No other 03 predecessor is a feminine forcer (30="pas", 40="e", 80=verb-frame A8,
  37=predicative A1, 60/10/01/24/81 carry no feminine value under §7).
- 81 is KILLED ("prin") and follows no determiner logic here regardless.
- No distributional rejection: 03's 20 windows remain noun-compatible per the standing
  noun-03 frame inventory (R19-180 GRANT, val-03-noun null with frames intact); none of the
  17 non-determiner windows forces a gender at all.

### Adverse answered

Adverse: 77='le' provisional (the @722 leg depends on it).

Answered by FENCE with stated cause (per §4, "fenced with stated cause" = answered):
the @722 masculine leg is conditional on the provisional 77="le" gloss, which the red team
has FENCED, not ratified (R20-131: "77='le' provisional SURVIVES" — provisional status
explicitly preserved, ratification pending). The other two legs (@1014, @1790) stand on the
granted 47="ce" (A4) and carry the finding independently: dropping @722 entirely leaves
2/2 determiner-headed windows forcing masculine with zero contradictions. The fence is
carried honestly; no leg of the promote depends on treating 77="le" as banked.

Standing-verdict check: no contradiction of any red-team verdict. R20-038 GRANTed 03's
class resolution as findings (removing the conditioned-split hedge at @1030); this result
(03 masculine-uniform) is compatible with and anticipated by it. 77's fence (R20-131) is
preserved, not lifted. §7 intact. No settled kill re-litigated (62='il' kill irrelevant here).

Canonicality caveat stands (pencil gloss on row a5_03; 68 of 70 upstream row offsets unvalidated).

## Verdict: PROMOTE (battery grade; red-team ratification pending)

Bar met: masculine holds across all forced-nominal windows with zero kill-grade contradictions.
Named gender: **noun-03 is masculine-uniform**.

This verdict narrows the future noun-03 lexeme candidate space to masculine nouns, as the
parent follow-up intended. Promote is a battery-grade finding only — per standing practice,
the red team ratifies.

## Follow-ups

None required by §4: a promote verdict proposes no follow-ups. (If the red team rejects the
promote, the natural regeneration is `noun-03-gender-rearm`: re-test gender uniformity on the
A/B-frame windows per R20-038's carry-forward, or against any new 03 determiner windows from
future finder beats.)

## Bookkeeping

- Queue: `noun-03-gender-test` → `status: verdict`, `result: promote` (pre-write assert passed —
  was queued/verdictless; temp-file + rename; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/noun-03-gender-test.lock` deleted on completion.
