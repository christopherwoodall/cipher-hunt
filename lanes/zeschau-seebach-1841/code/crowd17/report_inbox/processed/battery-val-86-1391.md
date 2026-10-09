# Battery verdict: val-86-1391

- Target id: `val-86-1391`
- Claim: "name 86 value at the @1391-1392 \"[86]er\" locus; its value constrains whether \"[86]er\" can license 89 slot at all"
- Date: 2026-10-09
- Worker: battery worker (subagent 71f70d81-d4ef-4f4c-8fdb-716e5f570f92)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. @-offsets are 0-based token offsets.

Terms (ASD-STE100): "leg" = one byte-verified window where the named value parses under a licensed frame with zero new assumptions. "Tier" = the level of the unit (whole word vs stem/syllable vs letter). "Licensor" = the word that grammatically governs a slot.

## Bar (verbatim, pre-registered before testing)

"value named with >=2 independent legs"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** one specific value for 86 is named at the @1391-1392 "[86]er" locus.
2. **C2:** the name rests on >=2 independent legs (byte-verified windows with licensed frames, zero new assumptions).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-86-1391.lock` on start (agent id + 2026-10-09T18:28:00Z); no prior/stale lock; to be deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Read the standing 86 record before testing (adopted, never re-litigated):
   - 86 = INF-class, A9 leg-1 class-level; red-team R20-087 re-confirmed "values not named".
   - noun-86-dlife-name KILL (2026-10-09): no single noun value covers the determiner windows (pencil "la" @671 forces feminine vs granted "ce" @175/@1345 forces masculine).
   - val-86-inf-locus NULL (2026-10-09): same bar ("value named with >=2 independent legs"); "voi"/"voir" candidacy has zero byte-forced legs ("86 29" = "voier" orthographic gap; "pourvoient" §5.2-blocked).
   - veut-86-1392-adjudicate NULL: 67 @1390 contested — R_et3 ("et", red-team-graded) vs §7 positional rule ("veut"); red-team venue, unruled.
   - et86er-licensor-16 NULL: 16 fenced as blocker (0/27 non-locus windows license a bare infinitive).
   - ce86-le86-parity PROMOTE (2026-10-09): ce-pair + le-quadruple merge as one masculine-noun hypothesis (value unnamed).
   - split-86-amended-rule PROMOTE (battery): determiner-life vs stem-life split declaration is red-team venue per §7.
4. 1841 diplomatic French throughout.

## Window-level evidence (byte-exact)

### The locus

Row a7_07 @1387-1396: `16 06 29 67 86 29 89 16 76 47`
(@1390=67 contested, @1391=86, @1392=29='er' pencil GT, @1393=89 A8 verb-frame, @1394=16).

### The "86 29" family (byte-exact, stream-wide, exactly 4x)

- @431 (a2_09): `76 42 63 77 86 29 82 16 78 63` — "77 86 29 82 16" = "[le~] [86]er m[16]"
- @1375 (a7_06): `91 67 98 00 86 29 89 84 92 69` — "00 86 29 89 84" = "pour [86]er [89] on(84=on GRANTED)"
- @1391 (a7_07): `16 06 29 67 86 29 89 16 76 47` — "67 [86]er [89] 16" (locus)
- @1825 (a8_11): `19 00 97 00 86 29 82 38 83 24` — "00 86 29 82 38" = "pour [86]er m[38]"

Two subfamilies: "86 29 82" x2 (@431, @1825) and "86 29 89" x2 (@1375, @1391).

### The "00 86 56" collocation (byte-exact, exactly 4x; "86 56" never occurs without preceding 00)

- @961: `20 67 96 00 86 56 41 19 24 06`
- @1001: `96 82 33 00 86 56 47 91 11 52`
- @1505: `33 42 33 00 86 56 41 12 61 59`
- @1791: `68 47 03 00 86 56 42 94 59 37`

56's value is open; the collocation is stem-consistent but names nothing.

### "86 70" (1x) and "77 86" (5x)

- @867: `48 47 46 00 86 70 87 77 89 48` — "pour [86]pre ce" (70='pre' pencil GT; admits comprendre/apprendre/surprendre/reprendre/entreprendre — five candidates, none forced).
- "77 86" x5: @430 ("77 86 29" — determiner + "[86]er", nominalized-infinitive shape), @798, @877, @950, @1133.

### The "X-er 89" control set (89's predecessors: {29: 5, 24: 3, 52: 2, 77: 2, 18: 1, 28: 1})

- @113: `11 21 67 93 29 89 68` — "93 29 89"
- @275: `11 06 67 33 29 89 84` — "33 29 89" (33+29 = A10 hold)
- @781: `33 73 37 08 29 89 11` — "08 29 89" (08='t' battery PROMOTE)
- @1377: `67 98 00 86 29 89 84` — "86 29 89" (same as locus subfamily)
- @1393: `06 29 67 86 29 89 16` — "86 29 89" (locus)

## Findings

### 1. No stem value reaches the bar (C1 FAIL, C2 FAIL)

Every -er stem parses all four "86 29" windows with zero friction (donner, parler, manger, penser, trouver, demander...): the bigram is shape-consistent with the whole -er infinitive class and discriminates none of them. The only multi-leg candidacy on record ("voi"/"voir") is dead per val-86-inf-locus (orthographic "voier" gap; "pourvoient" §5.2-blocked). The "00 86 56" x4 collocation and the "86 70" @867 window each admit multiple stems (56 open; five -prendre candidates). **Zero byte-forced legs for any specific value.** The bar is unmet.

### 2. Tier determination (fresh, battery grade): "[86]er" is a spelled -er infinitive, not a noun

- At @1391 there is no determiner anchor (pre=67, contested et/veut, never a determiner).
- 29='er' is pencil ground truth, a bound morpheme: treating it as a standalone word after a noun ("[86-noun] er") is unevidenced anywhere on the stream.
- Under the lane's compositional morphology (85 verb-stem A3; 33+29 A10 hold), "86 29" x4 is stem + 'er' — the same shape as the "08 29" control @781, where 08='t' (battery PROMOTE) makes a spelled word ("ter") impossible and forces the same compositional reading.
- Consistent with the noun-86-dlife-name KILL (no uniform noun value) and with split-86-amended-rule's stem-life arm.

**Consequence for the 89 slot:** "[86]er" can license 89's slot only as an infinitive (subject or governed infinitive), never as a lexical noun. The noun-subject arm for the 89 slot is dead at this locus. Note the "86 29 89" shape is not unique to @1391 (also @1375: "pour [86]er [89] on"), so the licensor question generalizes beyond this locus — but with 86's stem value open and 67 @1390 contested, no licensor determination is possible at battery grade.

### 3. Jurisdictional blocks (independent of the bar)

- The 67 @1390 "et" vs "veut" conflict (R_et3 vs §7 positional rule) is red-team venue, unruled — the governor of "[86]er" is indeterminate.
- The stem-life vs determiner-life split declaration is red-team venue per split-86-amended-rule (§7). The tier finding above stays battery-grade and declares no split.

## Per-clause results

- **C1: FAIL.** No value for 86 is forced by the stream at battery grade.
- **C2: FAIL** (moot — no value named).

## Verdict: NULL

86's value at the @1391-1392 "[86]er" locus remains unnamed: the bar's >=2-independent-legs standard is unmet (Finding 1). Battery-grade tier result: "[86]er" is a spelled -er infinitive (stem 86 + 'er'), so the 89 slot can only be licensed infinitive-shaped, never by a lexical noun (Finding 2). No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands (row a7_07 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json; supervisor to queue)

1. `stem-86-29-value` (P3) — name the -er stem across the four "86 29" windows; bar: one stem parses all four with a contact discriminator (via the "00 86 56" x4 collocation or the "86 70" @867 -prendre constraint), else fence as unnameable at battery grade.
2. `x-er-89-frame` (P3) — census the five "X-er 89" windows (@113, @275, @781, @1377, @1393); bar: one licensor frame for 89 parses all five at battery grade, else fence the 89-slot question.
3. `det-86-29-431` (P4) — test "77 86 29" @431 under provisional 77="le" as nominalized infinitive ("le [86]er"); bar: promote the nominalized-infinitive tier iff "82 16" parses as the "m[16-verb]" complement with zero new assumptions.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-86-1391.md` (this file).
- Queue: `val-86-1391` queued -> `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-86-1391.lock` created on start, to be deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
