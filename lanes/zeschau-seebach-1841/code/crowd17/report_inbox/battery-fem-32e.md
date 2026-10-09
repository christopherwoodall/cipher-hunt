# Battery verdict: fem-32e

## Bar (verbatim, pre-registered)

"(1) all 4 windows parse with '32e' as feminine predicative adjective; (2) copula frames @449/@1176/@1211 ('est 32e' x2, '32e est') are clean; (3) closed set verified: exactly 4 '32 48' bigrams, zero '48 32'"

Restated as numbered clauses:
- C1: all 4 '32 48' windows parse with '32e' as feminine predicative adjective.
- C2: the copula frames @449 ('est 32e'), @1176 ('32e est'), @1211 ('est 32e') are clean.
- C3: closed set — exactly 4 '32 48' bigrams stream-wide, zero '48 32'.

Adverses: (a) @855 'qui 32e on' needs a clause boundary or re-parse ('qui'+adjective without copula is ungrammatical); (b) @449's tail 'tout fois' ('79 17') vs A5 'tout' class-level grant (fence to A5, do not re-litigate). Inflection follow-up to queued adj-32, not a rival.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/fem-32e.lock` on start. Re-derived the
full stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(parsed per `repair_parse.py`): 1,847 pairs, 96 types verified. `canonical.py` never
touched. R5005, sealed gates, red-team adjudication queue untouched.

Offset convention: @-offsets below are 0-based indices of the '32' token, matching the
brief's numbering (verified: brief @449/@855/@1176/@1211 = my 0-based '32 48' bigram
positions exactly).

Standing values used: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (GT pencil);
87=ce, 64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9), 84="on" (A15,
re-derived unconditioned by collision-62-84), 47="ce" (A4); 59=est, 77="le"
(provisional); 32 predicative frame (A1, value open); **48="e" R17-003 GRANT PROMOTE
(letter tier)**; 78="ver" LEAD (R16-005). 1841 diplomatic French throughout.

## Window-level evidence

**@449** (row a2_09): `62 61 [59] 32 48 79 17 77 60 65 13`
- "est 32e" — copula frame clean under 59='est' (provisional). Subject slot = 61
  (0-based 447; value open globally — locus-level "premier" @1556 only, not extended here).
- Tail "79 17" = "tout fois": fenced to A5 per brief instruction (79="tout"
  class-level grant; the analytic "tout fois" vs syllabic "toutefois" duality is
  A5's venue — not re-litigated).

**@1211** (row a7_00): `65 [64] [59] 32 48 [96] 45 36`
- "qui est 32e par [45]" — 64=qui granted, 59='est' provisional, 96=par granted.
  Clean copula frame, and the "par" continuation yields the canonical passive shape
  "est [feminine pp] par [agent]" — the strongest leg for the feminine reading.
  (45 under HOLD A11; agent value not needed for the frame.)

**@1176** (row a6_10): `74 32 48 [59] 37 [77] 78 94 82`
- "32e est" — subject "32e" (nominalized feminine) + copula + "le ver":
  77='le' (provisional) + 78='ver' (LEAD) give "le ver" = "the worm".
  Grammatical: "[the] 32e is the worm". Residual noted: subject determination is
  open — 74 (0-based 1175) precedes and may supply determination or belong to the
  previous clause; bare nominalized feminine adjectives are strained but the frame
  parses. Clean at battery grade.

**@855** (row a5_07): `51 [64] 32 48 [84] 02 24 49 74 74`
- "qui 32e on [02]…" — 64=qui granted, 84=on (A15, unconditioned), 48='e'
  (R17-granted letter tier). The relative "qui" has no finite verb: verbless
  "qui + adjective" is ungrammatical in French at any period, including 1841.
- Clause-boundary search: none byte-evidenced. The window is mid-row a5_07
  (row starts 0-based 850; continuous digit stream, no row edge). Boundary after
  "qui" gives "32e on…" (unparseable); after "32e" gives verbless "qui 32e"
  (ungrammatical); after "32" gives "e on" (no French).
- Re-parse search: 64=qui cannot bend (granted); 84=on cannot bend (A15
  unconditioned); 48='e' cannot bend (R17 letter-tier grant). "32e" as feminine
  noun in apposition to "qui" is ungrammatical; "32e" modifying "on" is
  impossible ("on" masculine singular); interrogative/exclamative "qui 32e"
  has no 1841 precedent; scribal-error appeals ("dropped est") are not
  battery-grade. 02-as-verb is killed (ne-alone-02-74); "on y [24]" ("on y
  fait…", 24='faire' battery-promoted) fixes only the right side, not "qui 32e".
- FENCED with stated cause as a 32e-residual: morphology "32e" intact
  (32 + R17-granted 'e'), syntactic integration unachievable under standing values.

## Per-clause results

- **C1: FAIL (epistemic).** 3 of 4 windows parse with '32e' as feminine predicative
  adjective (@449, @1176, @1211). @855 does not parse that way under any standing
  values and no clause boundary or re-parse was found. The failure is epistemic,
  not kill-grade: no window forces the morphological claim false (the "32e"
  reading — 32 + granted 'e' — is intact at @855), and no cleaner rival value is
  demonstrated on these frames.
- **C2: PASS.** @449 "est 32e" clean; @1211 "qui est 32e par" clean (passive-shaped,
  strongest leg); @1176 "32e est le ver" clean (subject-determination residual noted).
- **C3: PASS.** Exactly 4 '32 48' bigrams stream-wide (0-based 449/855/1176/1211),
  zero '48 32' — byte-verified on the repaired stream.

Adverses: (a) @855 — fenced with stated cause above (no boundary or re-parse found;
the brief's requested positive resolution is not achieved); (b) @449 tail "79 17" —
fenced to A5 per instruction, not re-litigated.

## Verdict: NULL

C1 as written ("all 4 windows parse") is not met; the @855 failure is epistemic
(one unparseable window, morphology intact, 3/4 frames clean including a
passive-shaped "est 32e par"). Not kill-grade: nothing forces the claim false and
no rival is demonstrated. The three clean copula frames and the verified closed
set are recorded as findings for the red team.

## Follow-ups (for supervisor queuing)

1. `adj-32-inflect-gate` (P2) — re-test @855 once adj-32 names 32's value: a
   feminine past-participle 32 would make "qui 32e" a candidate reduced-relative /
   passive remnant. Coordinate with queued adj-32 (verdict/null); do not duplicate
   its bar. (Brief notes this as the inflection follow-up, not a rival.)
2. `qui32e-855-reseg` (P3) — re-segmentation sweep at @855: test 48='e'
   positionality at this window and exhaust byte-evidenced clause boundaries;
   either kill the residual or promote the fence.
3. `fem32e-subject-gender` (P3) — gender census of the three copula-frame subjects
   (61 @447, 65 @1208, 74 @1175): feminine agreement wants feminine (or
   gender-unmarked) subjects; a forced masculine subject would condition the claim.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-fem-32e.md` (this file).
- `battery-queue.json`: `fem-32e` → status `verdict`, result `null` (temp-file +
  rename, own entry only; pre-write assert confirmed queued/verdictless; JSON
  re-validated post-write).
- Lock `locks/fem-32e.lock`: deleted on completion.
- No standing verdict contradicted or downgraded. No polyvalence declared (§7
  intact). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
