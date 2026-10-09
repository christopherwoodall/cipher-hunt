# Battery report: hier-arm-94-nonneg

- Target id: `hier-arm-94-nonneg`
- Claim: re-test arm A dropping the 94=negation premise: ne-94-right-context established non-negator functions for 94 (6 word-final '-ne' syllable, 5 non-particle)
- Date: 2026-10-09
- Worker: battery worker (subagent 67592383-798d-4a82-889c-f291a0c95b42)
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
  (parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs,
  96 types). `canonical.py` never used. R5005, sealed gate instances, and the
  red-team adjudication queue untouched. Offsets below are 0-based repaired-stream @.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"parse "hier en [94-X] [92-verb]" iff a licensed non-negation function of 94
fits @65 with <=1 new assumption; else fence"

Adverses (verbatim): none listed. Parent-dispatch adverse (honored):
"94 split was rejected/closed in round 19 — do not declare a second 94 value;
only test whether a licensed non-negation function fits within existing §7
standing."

## Numbered pass/fail clauses (fixed before testing, bar not modified after data)

- **C1:** a licensed non-negation function of 94 (current standing, post-R19)
  fits @65 with <=1 new assumption → "hier en [94-X] [92-verb]" parses.
- **C2 (else):** fence the re-open with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/hier-arm-94-nonneg.lock` on start (agent id
   + UTC timestamp); no stale lock pre-existed. Deleted on completion.
2. Re-derived the repaired stream in-session; verified 1,847 pairs / 96 types.
3. Adopted (never re-litigated): banked GT 34='i', 29='er', 40='e'; 12='n'
   promoted; 94=["ne","lead"] (registry, unchanged by R19); 92 verb class-level
   (registry ["verb","cls"]); 69=["noun","cls"] (R19-ADD).
4. Binding red-team law (R19-167, R19-168):
   - R19-167: 94's value is the single syllabic spelling "ne". Word-final
     "-ne" is the SAME spelling word-internally — a SEGMENTATION distinction,
     not a second value. The split question is CLOSED. 67 et/veut remains the
     sole true polyvalence (§7).
   - R19-168: the 6 non-particle windows are FENCED as a red-team-tracked
     item, resolving via per-window W-naming, never via a value declaration.
5. Tested every licensed non-negator function against @65 byte-exactly.

## Window-level evidence

0b@60-67, row a1_01 (byte-exact, re-derived):

| @ | group | standing value |
|---|-------|----------------|
| 60 | 08 | open (word-internal, value unnamed) |
| 61 | 34 | 'i' (GT) |
| 62 | 29 | 'er' (GT) |
| 63 | 40 | 'e' (GT) |
| 64 | 12 | 'n' (promoted spelling letter) |
| 65 | 94 | 'ne' (battery lead) |
| 66 | 92 | verb (class-level) |
| 67 | 69 | noun (class-level) |

Right context at @65: 92 (verb class). ne-94-right-context's own census
lists this window under "Verbal-negator function — clean":
`40 94 92 69` = "e ne [92-V] [69]" — ne + verb-class 92 immediate.

## Function tests (C1)

### F1 — word-final "-ne" syllable (word-internal segmentation)

Per R19-167 this is a segmentation option, not a value: 94 must be the final
syllable of a French word ending at @65. Byte-exact candidates:

- @64-65: 12 94 = 'n' + 'ne' → "nne" — not a word.
- @63-65: 40 12 94 = 'e','n','ne' → "enne" — not a French word.
- @62-65: 29 40 12 94 → "erenne" — not a word.
- @61-65: 34 29 40 12 94 → "ierenne" — parent-killed family (enne-word-64:
  no French word contains "ierenne"), kill grade.
- @60-65: 08 + "ierenne" — killed family regardless of 08's value.

F1: FAIL. No host word exists; the segmentation is byte-blocked at this
window. (At the six R19-168 windows the word-final reading lived on [W]ne
nouns; @65 has no such W.)

### F2 — the five non-particle windows as transferable function

The five non-particle windows (@250, @318, @688, @1169, @1664) are fenced as
a red-team-tracked item resolving via per-window W-naming, "never via a value
declaration" (R19-168). They are not a licensed transferable function. In
addition, all five have verb-less right contexts; @65's right neighbor is 92
(verb class) — the geometry does not match any of them. Invoking one here
would declare a second 94 value, barred by R19-167 and §7 (adverse).

F2: FAIL.

### F3 — 94 as word-initial "ne" of the following verb ([94 92] one word)

No battery or red-team verdict licenses 94 as a word-INITIAL syllable; the
licensed syllable reading is word-final only. Naming 92 as "ne…"-initial to
make this parse would invent 92's value (§3 bars invention) and is not a
licensed function under the bar.

F3: FAIL (unlicensed; not a candidate the bar's budget can buy).

### Budget check

Even spending the bar's ≤1 new assumption, no licensed non-negator function
exists to spend it on. The budget is moot.

## Per-clause results

- **C1: FAIL** — F1 dead at kill grade (non-word hosts), F2 barred
  (red-team-fenced, non-transferable), F3 unlicensed.
- **C2: EXECUTED** — fence the re-open with stated cause.

## Verdict: NULL

The bar's else-arm is the designed outcome. Arm A's "hier en [94-X] [92-verb]"
has no licensed non-negator X at @65 under current red-team standing. No
standing or red-team verdict contradicted or downgraded: R19-167/R19-168 used
as premises; ne-94-right-context's PROMOTE stands (its @65 listing was
verbal-negator-clean, consistent with this result); seg-08-ier-61's NULL
fence stands (extended, not disturbed); §7 intact — no polyvalence declared,
no second 94 value. Canonical-stream caveat: row a1_01 offset unvalidated
(68 of 70 per §7).

## Fence (stated cause)

0b@65's 94 cannot be revived as a non-negator within existing §7 standing:
(a) word-final "-ne" segmentation forces non-words at this window
("enne"/"erenne"/"ierenne", kill grade); (b) the five non-particle readings
are red-team-fenced per-window items, not transferable functions, and their
geometries do not match @65's verb-class right neighbor; (c) R19-167 closed
the 94 split, so no second value may be declared. The "hier"+"en" arm stays
dead: with 94 as negator it dies on the "en ne" clitic-order kill
(seg-08-ier-61 C2), and without a negator it has no licensed X.

## Follow-ups proposed (nulls regenerate work; all verified absent from battery-queue.json)

1. `hier-94-nonneg-rearm` (P4) — gated re-fire of this bar iff the red team
   re-opens the 94 functional split (R19-167 reversal) or names a non-negator
   94 function covering @65. Not dispatchable now.
2. `enne-65-lexicon-tighten` (P3) — corpus-verify "enne"/"erenne"/"ierenne"
   as zero word forms in period French (31.6M-char side-period corpus,
   byte-counted). Bar: confirmed zero hardens the @65 word-final fence;
   any genuine form re-opens F1.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-hier-arm-94-nonneg.md` (this file).
- Queue: `hier-arm-94-nonneg` queued → verdict/null via temp-file + rename,
  own entry only; pre-write assert confirmed no prior verdict; JSON
  re-validated; all 1,204 entries checked, only this entry changed.
- Lock `code/crowd17/next-token/locks/hier-arm-94-nonneg.lock`: created on
  start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
