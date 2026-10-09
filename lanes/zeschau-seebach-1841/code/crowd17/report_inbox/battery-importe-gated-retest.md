# Battery report: importe-gated-retest — re-run of the pas/importe adversarial sweep on the four gated windows

- Target: `importe-gated-retest` (battery-queue.json, priority 2, status queued)
- Claim: GATE SATISFIED — 30='pas' is PROMOTE at red-team level (R17-004 / R20-009 DUPLICATE). Re-run the pas/importe adversarial sweep's bars on @1251/@1561/@1327/@1309 — the only windows where a granted subject could ever make 'importe' parse.
- Worker: bee45124-438b-4ceb-b6f5-2d103ba7d838
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`, re-derived in-session: 1,847 pairs / 96 types confirmed). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/importe-gated-retest.lock` created 2026-10-09T18:10:00Z; no stale lock present.

## Gate verification (before testing)

- 30='pas' is red-team PROMOTE (R17-004; R20-009 DUPLICATE, "conditional on 94-LEAD and 59-provisional") — the target's gate trigger is SATISFIED.
- Per-window sub-gate audit:
  - @1251/@1561 (noun-26): `noun-26` returned NULL (2026-10-08). `qui-fol-23-26-value` (2026-10-09): 26 carries 8 independent verb/copula legs, zero noun legs. 26 nominal is NOT granted; the gate has not cleared in the noun direction.
  - @1327 (62): 62='il' killed at red-team grade (R19-106/R20-125). `class-62-16-windows` PROMOTE (62 non-pronominal at the 62-16 windows); `val-52-630-frame` PROMOTE (2026-10-09: 62 nominal at @944/@1324, "et [62] vient"). 62's value is NOT named; the subject slot's class (56, class open; 98='vient' is LEAD, not granted) is unresolved. Gate NOT cleared.
  - @1309 (74/52): `val-74-212` and `val-74-letter` both queued (74's value open); `val-52-630-frame` PROMOTE (52 split-shaped: verb-tier / adverb-tier / sub-lexical by locus). No granted subject. Gate NOT cleared.

## Bar (verbatim, pre-registered)

"re-run this sweep's bars on @1251/@1561/@1327/@1309 once their gates clear: these are the only windows where a granted subject could ever make 'importe' parse. Bar: re-open 30's value iff >=1 then discriminates; else re-confirm confinement."

Numbered clauses (frozen before testing):
1. >=1 of the 4 windows FAILS under 30='pas' AND parses under 30='importe' → re-open 30's value.
2. Else: re-confirm confinement — 'importe' stays @1702-word-formation-confined; the rivalry is settled at battery level.

## Method

Byte-verified all four windows against the in-session re-derived stream (all match the parent sweep's readings). Adversarial re-test: for each window, first re-confirmed 'pas' parses under standing values (banked pencil + granted + provisional per §7; 94='ne' battery-promoted with ratification caveat), then tested whether 'importe' parses with a GRANTED subject. A discriminator needs FAIL('pas') + PARSE('importe').

## Window-level evidence

1. @1251 (a7_02) `00 67 46 26 | 30 06 65 46 01` — byte-match confirmed.
   - 'pas': "que 26 pas 06 65 que" parses. NOT failed.
   - 'importe': "que [26] importe" is grammatical ONLY if 26 is nominal. noun-26 is NULL; 26's 8 independent legs are verb/copula. No granted nominal subject. NOT discriminating.
2. @1561 (a8_01) `40 17 11 26 | 30 06 60 71 50` — byte-match confirmed.
   - 'pas': "fois la [26] pas" parses. NOT failed.
   - 'importe': "la [26] importe" needs 26 nominal — ungranted (same as @1251). NOT discriminating.
3. @1327 (a7_04) `08 62 98 56 | 30 06 62 94 70` — byte-match confirmed.
   - 'pas': "pas 06 62 ne pre" parses (parent's judgment, re-confirmed). NOT failed.
   - 'importe': "et [62] vient [56] importe" needs a granted subject for "importe". 56's class is open; 98='vient' is LEAD, not granted; 62's value unnamed. No granted subject. NOT discriminating.
4. @1309 (a7_04) `43 77 74 52 | 30 92 44 00 36` — byte-match confirmed.
   - 'pas': "le [74] [52] pas" parses. NOT failed.
   - 'importe': subject needs 74/52 named. 74's value is open (val-74-212, val-74-letter queued); 52 is split-shaped with no granted determiner/nominal tier at this locus. No granted subject. NOT discriminating.

Result: 0/4 windows discriminate.

## Adverses (answered, not ignored)

- **"pas-30 stands promoted — adversarial re-test, not a re-vote; no downgrade":** respected. This battery re-tests the re-open condition only; 30='pas' PROMOTE (R17-004) is not re-voted, not downgraded, not touched.
- **"No granted-subject 'importe' vehicle found (confirms importe-30-subject-sweep)":** CONFIRMED again — 0/4 here, matching the parent's 0/19.
- **"The @1702 adverse fence from battery-pas-30 stands exactly as fenced":** untouched. Re-verified: 94-30 adjacency is stream-unique to @1702 (0-based); 'n'importe' remains the sole elision-licensed frame.
- **"No elision-forced consonantal window (77='le' never directly precedes 30)":** re-verified on the stream — zero occurrences of 77 immediately before 30.
- §7 intact: no polyvalence declared, no kill/split/hold touched, no red-team verdict re-litigated. A10 HOLD respected.

## Per-clause results

1. >=1 discriminating window: FAIL — 0/4 (and the parent's 0/19 stands).
2. Else-branch: APPLIES — confinement re-confirmed. 'importe' stays @1702-word-formation-confined; the pas/importe rivalry is settled at battery level.

## Verdict

**null** — re-confinement confirmed. The four gated windows still offer no granted-subject 'importe' parse, and none fails under 30='pas'. Note: the per-window sub-gates themselves have not cleared (noun-26 NULL; 62's value unnamed; 74's value open), so a future re-run remains legitimate if any of noun-26 / 62-value / 74-value lands at grant grade — but today's re-run changes nothing. Not a kill: @1702's 'n'importe' parse remains clean and bracket-legitimate, so 'importe' stays a confined word-formation reading rather than a dead value.

## Follow-ups (null regenerates work; supervisor to queue)

1. `importe-gated-retest-2` (P4) — third re-run of this sweep's bars, gated on ANY of: noun-26 granted, 62's value named at red-team grade, 74's value named. Bar: re-open 30's value iff >=1 then discriminates; else re-confirm confinement. Evidence: this report's four windows.
2. `importe-1702-singleton-sweep` (P3) — sweep all 37 @94 windows for a second elision-licensed 94-30 adjacency under standing values; if none, record @1702 as a terminal singleton (strengthens confinement permanently). (Duplicates the parent's follow-up-2 if already queued — merge, do not duplicate.)
3. `neque-94lead-gate` (P4, already proposed by verb-slot-62-1686-neque) — noted for coordination: 30='pas' PROMOTE is conditional on 94-LEAD; if 94='ne' ever ratifies, the conditional lifts and this whole family re-opens at higher grade.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-importe-gated-retest.md`
- Queue: `importe-gated-retest` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; disk re-validated; own entry only; no downgrade)
- Lock created on start (2026-10-09T18:10:00Z, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
