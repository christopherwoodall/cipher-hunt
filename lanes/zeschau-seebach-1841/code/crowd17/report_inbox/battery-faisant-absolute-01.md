# Battery report: faisant-absolute-01

- Target id: `faisant-absolute-01`
- Claim: re-test 'faisant' only as absolute 'ce faisant' at the three ce-windows with subject recovery
- Date: 2026-10-09
- Worker: battery worker (subagent 97b4b98c-7a86-49cb-be47-97dabb4a55fc)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  1,847 pairs / 96 types re-derived in-session. All @-offsets are 1-based
  repaired-stream pair positions (@N = pairs[N-1]).
- Lock: code/crowd17/next-token/locks/faisant-absolute-01.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"re-test 'faisant' at 87-01/47-01/45-01 windows with a recovered subject for
each; promote-feed iff >=2 windows parse with the subject stated"

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: At each ce-window (87-01 x2 @345/@1029, 47-01 @195, 45-01 @984),
   attempt the absolute "ce faisant" parse (01 = 'faisant', 87/47/45 = 'ce')
   with a stated recovered subject for the governing main clause.
2. C2 (promote-feed): >=2 windows parse as complete "ce faisant,
   [subject] [verb]" clauses with the subject stated -> verdict
   promote-feed. Per the proposing battery (ci-01-value, KILL
   2026-10-08): kill the absolute reading iff none does.

Adverse (pre-registered): "24 is a finite verb (ne-24-profile promoted) --
subject recovery required."

## Method

1. Read BATTERY-PROTOCOL.md first; created/deleted the lock per protocol.
   Never used canonical.py. R5005, sealed gates, red-team queue untouched.
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types verified).
3. Located all ce-bigrams: 87-01 x2 (@345-346 a2_05, @1029-1030 a6_03),
   47-01 x1 (@195-196 a2_00), 45-01 x1 (@984-985 a6_01).
4. For each, attempted the absolute "ce faisant" + main-clause parse with
   an explicitly stated recovered subject, under standing values only.
5. Standing values used as premises (never re-litigated): 11=la, 70=pre,
   82=m, 34=i, 29=er, 40=e, 46=que (GT); 87=ce, 64=qui, 96=par, 17=fois,
   79=tout, 00=pour, 84=on, 47=ce (granted); 45=ce (A11 HOLD); 94=ne
   (STRONG LEAD); 06=ent (promoted); 24=finite modal verb (ne-24-profile,
   promoted); 30=pas (promoted); 12=n, 48=e (letters); 67=et/veut
   (sole polyvalence; "veut" iff follower infinitive-shaped); 03=verb
   stem class with 03-29=[03]er infinitive (stem-03); 98=finite verb
   class (prof-98); 88=verb class; 21=noun class; 65=noun class (R18-001).

## Window-level evidence

### W-A: 87-01 @345-346 (row a2_05, mid-row)

Full row a2_05: `63 71 10 01 19 00 92 50 45 54 88 40 03 64 31 14 45 64 96 43 87 01 06 70 12 94 74`

Target span @341-352: `45 64 96 43 87 01 06 70 12 94 74`
= "ce(45) qui(64) par(96) [43] ce(87) faisant(01) [06] pre(70) n(12) ne(94) [74]"

- "06 70 12 94" = "entreprenne": 06="ent" as word-initial syllable
  (ent-06-host-census decision rule: 06 is a finite ending iff left
  neighbor is a verb stem; 01='faisant' is a participle, not a stem,
  so 06 is syllabic here -- the census explicitly lists @347 as
  "entreprenne" word-initial), then "70 12 94" = "prenne" (12='n' +
  94='ne' word-internal, per the prenne battery). "entreprenne" is
  3sg present SUBJUNCTIVE of "entreprendre" (indicative 3sg would be
  "entreprend").
- Attempted parse: "[Ce qui par [43]], ce faisant, entreprenne [74]."
  Subject recovered and stated: "ce qui par [43]" (neuter relative,
  3sg, @341-344).
- FAILURE at kill grade: the main-clause verb "entreprenne" is
  subjunctive with no governor. No "que"/"pour que" in the row; "qui"
  does not license subjunctive here (no superlative, no negation,
  no "qui que"); the independent/optative subjunctive without "que"
  is restricted to fixed formulae ("vive", "ainsi soit-il") and does
  not extend to "entreprenne". An ungoverned subjunctive is
  ungrammatical in 1841 French. The subject is recoverable but the
  clause is not complete/grammatical.

### W-B: 87-01 @1029-1030 (row a6_03, mid-row)

Full row a6_03: `53 84 92 64 45 64 96 43 87 01 03 29 80 77 11 70 82 34 29 40 17 77 82 63 11`

Target span @1024-1040: `45 64 96 43 87 01 03 29 80 77 11 70 82 34 29 40 17`
= "ce(45) qui(64) par(96) [43] ce(87) faisant(01) [03]er(03-29) [80] [77] la(11) pre(70) m(82) i(34) er(29) e(40) fois(17)"

- "70 82 34 29 40" = "premiere" (pencil-crib anchored).
- "03 29" = "[03]er" infinitive (stem-03 battery: one of the three
  canonical "[03]er" infinitives @1030/@1320/@1594).
- Attempted parse: "[Ce qui par [43]], ce faisant, [03]er [80]..."
- FAILURE at kill grade: the infinitive "[03]er" directly follows "ce
  faisant" and no finite verb follows. An infinitive cannot head the
  main clause of an absolute construction. The infinitive-as-subject
  rescue ("[03]er [80]..." = "to-[03] [80]s...") is strained and
  additionally blocked by "77 11" ("le la", ungrammatical under
  provisional 77='le'). No complete "ce faisant, [subject] [verb]"
  clause is statable.

### W-C: 47-01 @195-196 (row a2_00, mid-row)

Full row a2_00: `24 87 98 56 47 01 21 60 08 67 76 87 11 92 63 42 06 77 44 50 88 19 74 77 78 06 59`

Target span @191-202: `24 87 98 56 47 01 21 60 08 67 76 87`
= "[24] ce(87) [98-finite] [56] ce(47) faisant(01) [21-noun] [60] [08] et(67) [76-noun] ce(87)"

- "21 60" @197-198 is one of the four '21 60' windows tested by
  battery-adj-60-2160 (PROMOTE 2026-10-09): 60 = postposed adjective
  ("[21-noun] [60-adj]"). 60 is adjective-grade here, not verbal.
- 67's follower is 76 (noun), so 67="et" per the positional rule.
- Attempted parse: "ce faisant, [21-noun] [60-adj] [08] et [76]..."
- FAILURE at kill grade: no finite verb follows "ce faisant". 60 is
  adjective-grade (not a verb); 08's class is open and a lone 08
  cannot head a finite clause. The absolute has no main clause.
  (The pre-"ce faisant" material "[24] ce [98] [56]" does not supply
  one either: 24 is modal/infinitive-taking but 98 is finite-verb
  class, so no modal+infinitive parse.)

### W-D: 45-01 @984-985 (row a6_01, mid-row)

Full row a6_01: `48 51 45 08 01 00 92 07 76 47 78 45 01 24 89 48 01 76 49 24 26 30 03 60` (offset 1)

Target span @980-990: `07 76 47 78 45 01 24 89 48 01 76`
= "[07] [76-noun] ce(47) [78] ce(45) faisant(01) [24-faire] [89] e(48) [01] [76-noun]"

- "45 01 24" @984-986 is one of the three '01 24' windows where
  ci-01-value (KILL) already forced unconditioned 01='faisant' false:
  "absolute 'ce faisant' + finite verb with no subject."
- Attempted subject recovery for 24 (finite modal, ne-24-profile):
  candidates are (i) "ce(47) [78]" @982-983 -- requires 78 nominal,
  but 78's class is open (ver78 docket; red-team venue), so this is
  an ungranted assumption, not a recovery; (ii) "[76-noun]" @981 in
  dislocation -- "[76], ce [78], ce faisant, [24]..." is strained
  beyond battery grade; (iii) the absolute's own "ce" -- "ce
  faisant, ce [24]" is unidiomatic (the "ce" is already the agent of
  "faisant").
- FAILURE at kill grade: no subject is recoverable under standing
  values. This confirms ci-01-value's W3 kill; the "ceci [24]" rival
  ("ceci peut...") parses cleanly at this window but that is the
  bound-"-ci" hypothesis (fenced, not tested here).

## Per-clause pass/fail

- C1 (attempt absolute + recovered subject at each window): attempted
  at all four ce-windows (W-A @345, W-B @1029, W-C @195, W-D @984).
  A subject could be STATED only at W-A ("ce qui par [43]"), but the
  clause fails on the ungoverned subjunctive.
- C2 (promote-feed iff >=2 parse): 0 of 4 windows parse as complete
  "ce faisant, [subject] [verb]" clauses. The threshold is not met.
  Per the proposing battery's bar ("kill the absolute reading iff
  none does"): the absolute reading is killed.

## Verdict: KILL

The absolute "ce faisant" reading of 01 is killed at battery grade.
All four ce-windows force it false:
- W-A @345: recoverable subject but ungoverned subjunctive
  ("entreprenne") -- no complete clause.
- W-B @1029: infinitive "[03]er" blocks any finite main clause.
- W-C @195: adjective-grade 60 blocks any finite main clause.
- W-D @984: no recoverable subject for finite 24 (confirms
  ci-01-value's kill).

No cleaner rival is named here (the bound-"-ci"/"ceci" hypothesis is
fenced per ci-01-value and untouched by this kill). This kill covers
only the ABSOLUTE frame shape; word-internal 01 readings (37-01
"-faisant" compounds, 01-29 "-cier") are untested here.

## Adverses

- "24 is a finite verb -- subject recovery required": ANSWERED. The
  one window where 24 follows the absolute (W-D @984) was subjected
  to full subject-recovery analysis; every candidate fails under
  standing values (78's nominality ungranted; dislocation strained;
  "ce"-reuse unidiomatic). The adverse is satisfied by the attempt,
  not ignored.

## Standing state

- Consistent with ci-01-value (KILL 2026-10-08): this battery is its
  follow-up #3 and confirms the absolute frame -- the "only surviving
  frame shape" per that report -- does not survive subject recovery.
- No standing red-team verdict contradicted or downgraded. No values
  named. Section 7 intact (no polyvalence declared).
- Note for the red team: W-A's "entreprenne" subjunctive and W-B's
  "[03]er [80]" sequence remain unexplained residuals under all live
  01 readings; they are fenced, not resolved.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-faisant-absolute-01.md
- battery-queue.json: `faisant-absolute-01` -> status `verdict`,
  result `kill`, date 2026-10-09 (temp-file + rename; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write).
- Lock created on start, deleted on completion.
- Stream re-derived in-session (1,847 pairs / 96 types); canonical.py
  never used; R5005, sealed gates, red-team queue untouched.

No follow-ups proposed (kill ends the absolute line; the surviving
bound-"-ci" and word-internal hypotheses are owned by ci-bound-01
and wordinternal-37-01, already queued).
