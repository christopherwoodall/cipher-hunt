# Battery report: ce-le-verb-frame (preverbal ce+le stack)

- Target id: `ce-le-verb-frame`
- Claim: "grammatical account of preverbal ce+le stack at '87 77 [80/89]' x2"
- Date: 2026-10-08
- Worker: battery worker (agent 48d9bd42-ed6d-4c5e-a712-e4d1e6dbc0dd). Lock
  `code/crowd17/next-token/locks/ce-le-verb-frame.lock` created
  2026-10-09T02:47:17Z; no prior/stale lock existed; deleted on completion
  after queue confirm.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
  (`load_rows` + `parse`). 1,847 pairs / 96 groups re-derived. R5005 untouched.
  `canonical.py` never used. No invented data.
- Coordinates with (not duplicating): vient-98-511-relative null (2026-10-08),
  which fenced the "87 77 [verb-frame]" x2 frame as a live residual for the
  77/87 line.

Indexing convention: @-offsets are 0-indexed pair indices into the repaired
stream, citing the FIRST pair of the named frame.

## Bar (pre-registered verbatim, from battery-queue.json)

"give a grammatical account of the preverbal ce+le stack with period evidence,
or demonstrate a rival value for 77 at these windows; else fence as a 77-value
residual. Discriminates the @510-517 tail and the @869 window together"

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. A grammatical account of the preverbal "ce"+"le" stack (87/47="ce" +
   77="le") is given with period-French (1841 diplomatic) evidence, covering
   BOTH @515 ("87 77 80") and @869 ("87 77 89").
2. OR a rival value for 77 is demonstrated at these windows (parses both
   windows, distributionally compatible with 77's stream profile).
3. ELSE the stack is fenced as a 77-value residual with stated cause.

## Method

Fresh byte-exact re-parse of the repaired stream in-work; no prior counts
trusted. Re-derived the full "ce"+77 population: "87 77" x2 (@515, @869) plus
one "47 77" window the brief did not name (@611: "47 77 87", 47="ce"
promoted, allophone tier). Census of 77 (n=44), 87 (n=32), 47 (n=28), 80
(n=17), 89 (n=14) re-derived in-work. Tested candidate grammatical accounts
against 1841 French grammar (Littré 1872-1877 distribution of demonstrative
"ce": licensed before "être" — c'est, ce sont, ce fut — and before relatives
— ce qui, ce que, ce dont; never as bare subject of a lexical verb, never
stacked with an object clitic). Tested rival values for 77 against its
follower/leader profile.

Standing values used (none decided here): banked GT 11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 00=pour (A9),
84=on (A15), 47=ce (allophone tier); provisional 77="le", 59=est; class-level
65=NOUN, 88=governor/verb-class, 86=INF-class; A8 80/89 verb-frames; 89=noun
lead (registry). §7 respected: no polyvalence declared.

## Window-level evidence (@-offsets, repaired stream)

- @515-517 (row a3_00): wider @505-525 =
  `21 67 77 62 94 64 98 65 88 56 | 87 77 80 | 09 70 91 77 06 55 81 97`.
  The stack: 87="ce" (granted), 77="le" (provisional), 80=verb-frame (A8).
  This is the @510-517 tail of the vient-98-511-relative window.
- @869-871 (row a5_07): wider @860-880 =
  `49 74 74 48 47 46 00 86 70 | 87 77 89 | 48 20 74 49 16 77 86 78 17`.
  The stack: 87="ce", 77="le", 89=noun-lead / infinitive-conflict (89's class
  is with the red team per class-89-adjudicate; registry shows noun lead).
- @611-613 (row a3_04, bonus window found in-work): wider @600-625 =
  `39 26 96 45 93 54 64 39 64 02 58 | 47 77 87 83 | 70 88 10 29 88 37 76 82 14 59 37`.
  The stack: 47="ce" (granted), 77="le", 87="ce". A third "ce le" contact —
  the strain is systematic, not a two-window accident.
- 77's pro-"le" legs (re-derived, untouched by this battery): 77->84 x7 =
  "l'on" with textbook distribution — @1484 `46 77 84` = "que l'on" (46=que
  granted), @145/@1446/@1802 `64 77 84` = "qui l'on" (64=qui granted);
  77->86 x5 = "l'/le + nominalized infinitive" (86 INF-class; cf. Littré
  "Le boire est un infinitif employé comme substantif"); 67->77 x6 =
  "veut/et le". 77="le" is strong GLOBALLY; only the "ce"+77 contact fails.
- 87's licensed "ce" frames (re-derived): 87->64 x5 = "ce qui", 87->46 x3 =
  "ce que", 87->11 x7 ("cela"-shaped). The demonstrative-pronoun value is
  solid; the anomaly is strictly the 77 follower.
- 47's licensed "ce" frames: 47->46 x3 = "ce que", 47->11 x3 ("cela"-shaped),
  47->78 x5. Same conclusion: "ce" is fine, "ce le" is not.

## Candidate accounts tested (all fail at battery grade)

1. "ce le [verb]" as clitic stack — FAIL. Demonstrative "ce" cannot head a
   lexical verb (bare "ce" subject requires "être": c'est/ce sont/ce fut, or a
   relative: ce qui/ce que) and cannot stack with object clitic "le" before
   any verb, in French of any period. Both windows ungrammatical as parsed.
2. "ce le [noun]" (89=noun lead at @869) — FAIL. "*ce le [noun]" is
   ungrammatical; the determiner "ce" and article "le" cannot co-occur.
3. Clause boundary + dislocation ("..., ce, le [80]") — FAIL. "le [80]" as a
   clause needs a subject (none on either side); as an infinitive phrase
   ("le [80-inf]" = "to V it") it leaves "ce" dangling with no governor at
   either window ("56 ce" @515, "pre ce" @869 — neither is a phrase).
4. Re-segmentation "87 | 77 80" = "ce" + "le [80-inf]" (infinitive phrase
   "to V it") — FAIL at battery grade. Needs 80/89 infinitive-shaped at
   these windows (ungranted) AND a governor for the stranded "ce" (ungranted):
   2+ ungranted assumptions per window. Kept as follow-up, not a finding.
5. "87 77" = "celle" (one word, syllabic cel-le) — FAIL. "celle" requires a
   following relative ("celle qui/que/de"); 80/89 is not a relative at
   either window (64=qui, 46=que are the relatives).
6. 77="ne" ("ce ne [80/89]") — FAIL. Bare "ce" cannot subject even a negated
   lexical verb; and 77="ne" is killed distributionally by "46 77 84" =
   "que l'on" (@1484, perfect) and "64 77 84" x3 = "qui l'on".
7. 77="ci" ("87 77" = "ceci", full pronoun subject: "ceci [verb]" IS
   grammatical) — FAIL at battery grade: attractive at @515 ("ceci [80]"
   with 80 finite-verb-shaped) but "77 84" = "ci on" is ungrammatical x7 and
   "que l'on" @1484 forbids it globally; needs 77=le/ci polyvalence, which
   §7 bars at battery level (67 et/veut sole true polyvalence). Escalated as
   a red-team hypothesis (follow-up 1), not demonstrated.
8. 77="y"/"en"/"se"/"lui"/"les"/"la"/"est" — all FAIL: none makes
   "ce X [verb]" grammatical with bare "ce", and each contradicts 77's
   "l'on" / "le + nominalized infinitive" legs.
9. 87="se" ("se le [verb]" — grammatical clitic cluster!) — NOT TESTED as a
   finding: contradicts the granted 87=ce. Recorded as a red-team escalation
   note only; battery cannot overturn a grant.

## Per-clause pass/fail

1. Grammatical account with period evidence covering both windows — **FAIL**.
   Nine candidate accounts tested; none parses both windows within the
   assumption budget. The closest (re-segmentation "ce | le [inf]") needs 2+
   ungranted assumptions per window.
2. Rival value for 77 demonstrated — **FAIL**. "ne", "ci", "y", "en", "se",
   "lui", "les", "la", "est" each tested; each is either ungrammatical in
   the "ce X [verb]" frame or distributionally killed ("que l'on" @1484).
3. Fence as 77-value residual — **TAKEN**. The stack "87 77 [80/89]" x2 plus
   "47 77 87" @611 is fenced: 87/47="ce" granted and clean elsewhere; 77="le"
   provisional with strong global legs ("que l'on", "qui l'on", "le +
   nominalized infinitive") that this battery does NOT disturb; the
   "ce"+"le" contact itself is ungrammatical in 1841 French and unexplained.
   These three windows are held OUT of 77="le"'s support and held as a
   residual for the 77-line / red team. No standing verdict contradicted or
   downgraded: 77="le" stays provisional, 87=ce and 47=ce stay granted,
   98="vient" (battery-promote) untouched, A8 untouched.

## Verdict

**NULL** — inconclusive, with the bar's else-branch executed: the preverbal
ce+le stack is **fenced as a 77-value residual**. No grammatical account
survives battery-grade testing (clause 1 fails); no rival 77-value is
demonstrated (clause 2 fails); the three windows (@515, @611, @869) are
recorded as a systematic residual against provisional 77="le", which is
neither confirmed nor killed here. Per §4, nulls regenerate work — follow-ups
below; the supervisor queues them.

## Follow-ups proposed (for supervisor queuing)

1. `ceci-77-redteam` (P2) — test 77="ci" at the three "ce"+77 contacts only
   ("87 77" x2, "47 77" x1) as the word "ceci": bar = "ceci" parses @515 and
   @869 as subject ("ceci [80/89]" with 80/89 finite-verb-shaped) and @611
   ("47 77 87 83") is given a "ceci"-compatible parse, with the 77=le/ci
   polyvalence cost stated for the red team; else the "ceci" hypothesis is
   killed. Note: needs red-team authority (§7, 67 sole polyvalence).
2. `inf-7780-reseg` (P3) — test the re-segmentation "87 | 77 [80/89-inf]" =
   "ce" + "le [inf]" (infinitive phrase "to V it"): bar = 80/89 shown
   infinitive-shaped at @515/@869 AND "87"="ce" given a left-context governor
   ("56 ce" / "70 ce" parsed as phrases) with <=1 ungranted assumption total;
   else the re-segmentation is fenced.
3. `le-77-residual-adjudicate` (P2) — package the three fenced windows
   (@515 "87 77 80", @611 "47 77 87", @869 "87 77 89") together with the
   pro-77="le" legs ("que l'on" @1484, "qui l'on" x3, "le + nominalized
   infinitive" x5) for red-team adjudication: does 77="le" survive with a
   fenced residual, or do the "ce le" windows force a conditioned split?
   Coordinate with (do not duplicate) the queued lon-77-le-gate target.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ce-le-verb-frame.md` (this file).
- `battery-queue.json`: `ce-le-verb-frame` queued -> verdict/null via
  temp-file + rename, own entry only; pre-write assert confirmed no prior
  verdict; queue JSON re-validated after write.
- Lock `code/crowd17/next-token/locks/ce-le-verb-frame.lock` deleted on
  completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
  No standing verdict contradicted or downgraded.
