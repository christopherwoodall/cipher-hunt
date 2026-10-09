# Battery report: residual-345-06

- Target id: `residual-345-06`
- Claim: "@345 '87 01 06 70 12 94' resolves with 'ceci' intact or fences as 06-driven residual"
- Date: 2026-10-09
- Worker: battery worker (subagent 6a0fb8af-fc36-4525-87a2-b9dc61eb9ff9)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  1,847 pairs / 96 types re-derived in-session. All @-offsets 1-based.
  `canonical.py` never used. R5005, sealed gates, red-team adjudication
  queue untouched.
- Lock: code/crowd17/next-token/locks/residual-345-06.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"produce a full-context parse of 'ce [01] entreprenne [74]...' (is
'entreprenne' the verb with an elided 'que'? can 'ceci'/'ce' serve as its
subject?); if the window parses with 'ceci' intact, re-test ci-bound-01's
clause 1; else fence @345 as a 06-driven residual with stated cause (not a
-ci residual)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: produce a full-context parse of "ce [01] entreprenne [74]..." with
   'ceci' intact — 'entreprenne' as the verb, testing (a) an elided-"que"
   governor and (b) 'ceci'/'ce' as its subject.
2. C2: if C1 passes, re-test ci-bound-01's clause 1 with @345 as a clean
   "ceci [verb]" window.
3. C3 (else-branch): fence @345 as a 06-driven residual with stated cause,
   explicitly NOT a -ci residual.
4. Adverse: the analysis is load-bearing on ent-06's PROMOTE — the fence
   must state the dependency.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs verified).
2. Extracted the full row context: row a2_05 = 1-based @325–351 =
   `63 71 10 01 19 00 92 50 45 54 88 40 03 64 31 14 45 64 96 43 87 01 06 70
   12 94 74`; row a2_06 begins @352 (`67 78 40 92 98 92 47 11 21 62 48 76
   47 78 48 49 61 70 17 06 21 65 63 29`).
3. Tested the 'ceci'-intact parse against standing values: 87=ce (granted),
   45=ce (A11 hold), 64=qui (GT), 96=par (promoted), 70=pre (GT), 12='n'
   (promoted letter), 94='ne' (promoted), 06='ent' (PROMOTE) + the
   06-attachment rule (06 = -ent finite 3pl ending iff left neighbor is a
   verb stem; else syllabic).
4. Swept ±20 pairs around @345 for any 46='que' (banked GT) or other
   subjunctive governor; checked the left edge @338–344 against
   edge-340-31-14's standing kill.
5. Adopted (not re-litigated): 01='faisant' general killed (ci-01-value),
   01='ci' general killed (ci-01-value), "ceci" bound-morpheme reading fenced
   not killed (ci-bound-01 NULL), 31=verb class (edge-340-31-14), 14's verb
   candidacy fenced lane-wide.

## Window-level evidence

Core window (1-based): @343 96(par) @344 43 @345 87(ce) @346 01 @347 06
@348 70(pre) @349 12(n) @350 94(ne) @351 74 | a2_05 ends | a2_06: @352 67
(et/veut) @353 78 @354 40(e) @355 92 @356 98 ...

**Attempt A — "par [43] ceci entreprenne [74]" with 'ceci' intact:**
- "par ceci" is grammatical ("by this"). The verb "entreprenne" is 3sg
  subjunctive of entreprendre (standing ent-06 F3 leg). A subjunctive
  requires a "que"-governor (or optative context, absent here).
- Elided-"que" rescue: FAIL. Verified byte-exact: zero 46='que' cells in
  @320–370. French elision ("qu'") still requires the word "que" present;
  there is no que-cell anywhere in reach.
- 'ceci'/'ce' as subject of a bare subjunctive in declarative 1841 prose:
  ungrammatical. No optative/wish frame in context.
- Result: FAIL.

**Attempt B — left edge rescue ("ce qui par [43] ceci ..."):**
- @341–343 = 45(ce) 64(qui) 96(par) = "ce qui par". Kill-grade dead per
  standing edge-340-31-14: "ce qui" needs a finite verb and a preposition
  cannot serve. All 8 clause-boundary placements in that battery failed.
- Result: FAIL (adopted kill, not re-litigated).

**Attempt C — 06 as syllabic instead of verb ending:**
- 06's left neighbor @346 (01) is open, not a verb stem, so per the
  06-attachment rule 06 cannot be the -ent finite ending here. As syllabic
  "ent", 06-70-12-94 = "ent"+"pre"+"n"+"ne" = "entprenne" — not a French
  word. The only word-reading is the standing "entreprenne" gloss, which
  itself fails Attempts A/B.
- Result: FAIL.

**Value-independence check (the "not a -ci residual" clause):** the
breakage is identical under every 01 reading — 'ceci', 'ce', or fully open:
the subjunctive-without-que failure and the "ce qui par" left-edge kill do
not involve 01's value. The residual is 06-driven (bare/stemless 'ent'
before a pre-n-ne complex with no governor), not -ci-driven. Confirmed.

**Independent caveat (new finding, not hidden):** the standing
"entreprenne" gloss has a spelling hole. 06('ent') + 70('pre') + 12('n') +
94('ne') concatenates to "entprenne" (9 letters), not "entreprenne"
(e-n-t-r-e-p-r-e-n-n-e, 11 letters). The gloss as written requires 06 =
'entre' (unpromoted; contradicts 06='ent') or an unaccounted "re". The
ent-06 F3 and ent-06-host-census both state the "entreprenne" equation
without bridging the "re". This weakens the verb-ID leg itself; the fence
above does not depend on it (Attempts A/B kill independently of how the
verb is spelled). Flagged for follow-up, not adjudicated here.

## Per-clause pass/fail

1. C1 ("ceci"-intact full-context parse): FAIL — Attempts A, B, C all fail
   at kill grade (subjunctive without governor, dead left edge, no
   syllabic alternative).
2. C2 (re-test ci-bound-01 clause 1): MOOT — C1 failed; no re-test
   triggered. ci-bound-01's clause-1 score stands (1 clean @984,
   1 provisional @195, 2 fenced residuals @345/@1029).
3. C3 (fence as 06-driven residual): FIRES — @345 fenced as a 06-driven
   residual, explicitly not a -ci residual. Cause: stemless 'ent' + "pre" +
   "n" + "ne" complex with no "que"-governor in ±20 and a kill-grade-dead
   "ce qui par" left edge; failure is 01-value-independent.
4. Adverse (load-bearing on ent-06's PROMOTE): ANSWERED — the fence uses
   06='ent' and the 06-attachment rule throughout. If ent-06's grant is
   ever overturned, @345 re-opens (same dependency as ci-bound-01's).

Phase caveat (stated, not hidden): row a2_05's offset is unvalidated
(canonicality caveat). The fence holds on the canonical stream per
protocol; a2_05 is phase-uncertain soil (edge-340-31-14: −3.35 nats), and
under offset-1 the whole run dissolves — same mechanism class as the
a1_01/a7_10 findings.

No standing red-team verdict contradicted or downgraded. §7 intact
(67="veut" iff follower infinitive-shaped; 78 open → 67='et' default at
@352, unneeded for the fence).

## Verdict: NULL (fence executed per the bar's else-branch)

## Follow-up targets (nulls regenerate work)

1. **phase02-a2_05-reseg** (priority 3): constraint sweep of row a2_05 under
   offset-1; hardens the @345 fence or dissolves it (the edge-340-31-14
   kill dissolves under the same re-phase).
2. **spell-06-entre** (priority 3): resolve the "entreprenne" spelling hole
   — census 06-initial words for an "entre" value vs 06='ent'; if no
   "entre" license exists, kill the @346–349 verb-ID leg (ent-06 F3's
   "value evidence, not ending evidence" claim falls with it).
