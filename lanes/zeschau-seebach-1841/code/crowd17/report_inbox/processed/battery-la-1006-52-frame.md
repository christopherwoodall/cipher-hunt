# Battery verdict: la-1006-52-frame

- Target: `la-1006-52-frame`
- Claim: Control: test 52's adjective shape at the third 'la 52' window (@1006, '11 52 35 18 79 80'); sharpens whether the adjective arm is tail-specific.
- Parent: la-frame-52-37-43-noun (NULL, 2026-10-09)
- Worker: cb9c8d23-cae3-4cda-bba9-997b6fca5b85
- Date: 2026-10-09
- Verdict: **PROMOTE** (window-level class naming; locus-level only)

## 1. Bar (verbatim from battery-queue.json)

1. "Stream-only test at @1006 (11 52 35 18 79 80): is 52 adjective-shaped there?"
2. "Compare against the tail-window adjective evidence; sharpen whether the adjective arm is tail-specific."
3. "Coordinate with queued adj-52-37-value-rerun ({même, seule} tie-break) — do not duplicate it."

Numbered clauses (pre-registered before testing):
- **C1:** PASS iff 52 is adjective-shaped at @1006 under standing values with the rival class arms decided at battery grade.
- **C2:** PASS iff the comparison with the tail windows (@1123/@1721) sharpens whether the adjective arm is tail-specific.
- **C3:** PASS iff adj-52-37-value-rerun's {même, seule} tie-break is untouched (no value named, no duplication).

## 2. Method

- Read BATTERY-PROTOCOL.md first. Lock `locks/la-1006-52-frame.lock` created on start (agent id + UTC timestamp), deleted on completion.
- Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: **1,847 pairs / 96 types verified**. `canonical.py` never touched.
- 0-based @-offsets throughout (queue convention).
- Adopted as premises (not re-litigated): la-frame-52-37-43-noun NULL (Type-A parse "la [52-37-adj-unit] [43-head-noun]", 43 red-team-gated); la-523743-adjective NULL (52 adjective-shaped at the tails; @1006 left undetermined); 52 determiner arm killed stream-wide; split-52-redteam-input PROMOTE (gather-only package, explicitly not a class decision); ne52inf-adverb's 52 adjective-arm finding. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## 3. Window-level evidence (all byte-traced)

- **Locus byte-confirmed** (row a6_02, fully mid-row): `@1006=11 @1007=52 @1008=35 @1009=18 @1010=79 @1011=80` = "la [52] [35] [18] tout [80]". Left context `@1003=56 @1004=47 @1005=91`; right context `@1012=78 @1013=47 @1014=03 @1015=24`.
- **"11 52" exactly 3× stream-wide** (@1006, @1123, @1721) — census confirms exhaustiveness; no other 11→52 bigram.
- **"35 18" is a stream-wide hapax** (@1008). No standing reading on the contact.
- **Standing delta since la-523743-adjective's @1006 analysis (2026-10-08):** 35 = ["noun","cls"] granted at **R19-050** (registry). That report left @1006 "undetermined" because "la 52 [35]" then admitted both "la [52-noun] [35-adj]" and "la [52-adj] [35-noun]". The registry grant kills the first alternative at battery grade (35 adjective-shaped would be polyvalence = red-team venue).

## 4. Per-clause pass/fail

- **C1 — PASS (window-level).** Arm elimination at @1006 under standing values:
  - **Adjective: "la [52-adj] [35-noun]"** — grammatical French, zero ungranted assumptions (11=la banked GT; 35 noun-class granted). Unique survivor.
  - Noun: "la [52-noun] [35-noun]" needs an unlicensed noun-noun composition; the old "la [52-noun] [35-adj]" variant is dead via 35's noun grant. Dead at battery grade.
  - Finite verb ("a"): "la" + finite verb is ungrammatical. Dead.
  - Determiner: 52's determiner arm is killed stream-wide. Dead.
  - Sub-lexical: 35 is word-level noun-class, not letter-tier; no licensed 52-35 composition is statable. Not a battery-grade arm.
- **C2 — PASS.** The adjective arm is **NOT tail-specific**: it fires at all three "la 52" windows. At the tails (@1123/@1721) 52 is adjective-shaped *unit-internally* — "la [52-37-adj-unit] [43-head-noun]" (Type-A, itself NULL because 43's nominality is red-team-gated). At @1006 52 is adjective-shaped *standalone prenominal* — "la [52-adj] [35-noun]" — with a granted head noun, so @1006 is the cleanest locus of the three: no dependency on 43's gated nominality.
- **C3 — PASS.** No 52 value named; the {même, seule} tie-break untouched — it remains owned by queued `adj-52-37-value-rerun` (still queued/verdictless, not duplicated).

## 5. Adverses answered

- **"52's value open"** — ANSWERED: no value named; class-level naming only.
- **"52=`a` conditioned split"** — ANSWERED: "a" (finite verb) is ungrammatical after "la" at all three windows; the split-52 package already tiers these windows separately from the "a" tier. Consistent, no contradiction.
- **split-52 Tier-3 "adverb ('la plus')" label** — ANSWERED: that report is explicitly gather-only ("not a class claim... the docket item is NOT decided at battery level"). My result is a class-level frame finding at one locus, not a value claim and not a split declaration. The labeling tension (adverb-shaped vs adjective-shaped at "la [52]") is recorded as a note for the red team, not adjudicated here.
- **"18 tout 80" continuation** — ANSWERED as out of scope: the NP "la [52] [35]" is left-complete; the continuation is a separate window question and does not disturb the internal parse.
- **52-37 unit structure** — ANSWERED: @1006 has no 37; the standalone adjective reading does not touch the unit. Coordination bar satisfied.

## 6. Verdict: PROMOTE

52 is adjective-shaped at @1006 (window-level class naming, locus-level only): "la [52-adj] [35-noun]" is the unique surviving frame-level reading, and the R19-050 grant of 35=["noun","cls"] removes the alternative that previously kept @1006 undetermined. The adjective arm is not tail-specific — it fires at all three "la 52" windows, and @1006 is the cleanest locus (no 43 dependency). Feeds the split-52 venue; no value named; no polyvalence declared. No standing or red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands (row a6_02 offset unvalidated).

## 7. Scope

Locus-level only (@1006–1008). Untouched: 52's global class/value, the split-52 docket, 37/43/18/79/80, adj-52-37-value-rerun's {même, seule} tie-break, the "18 tout 80" continuation parse. R5005, sealed gates, red-team adjudication queue untouched.

## 8. Bookkeeping

- Report: `code/crowd17/report_inbox/battery-la-1006-52-frame.md`
- Queue: `la-1006-52-frame` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.la-1006-52-frame.tmp` + atomic rename, no leftover; disk re-validated; own entry only; no downgrade).
- Lock created on start (no stale lock), deleted on completion (verified gone).
- Per §4 (promote), no follow-ups required.
