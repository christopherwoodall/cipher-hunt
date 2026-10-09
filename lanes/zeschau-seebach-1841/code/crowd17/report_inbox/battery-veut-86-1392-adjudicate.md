# Battery verdict: veut-86-1392-adjudicate

## Bar (verbatim, pre-registered)

"if 67='et' there, C1 passes and the strict bar holds"

## Restated clauses (fixed before testing, not modified after)

- **C1:** "et [86]er" parses grammatically at the @1392 locus (67 @1390,
  0-based, repaired stream) under standing values, with no new polyvalence
  declared and ≤1 non-granted value assumption.
- **C2:** If C1 holds, the stem-class-split C1 (governor-set disjointness
  for 33 vs 86) passes under value-resolved governors: 33's 67-governors
  read "veut", 86's @1390 67-governor reads "et" — sets disjoint.
- **Verdict rule (pre-registered):** promote iff C1 and C2 pass AND the
  adverse (the §7 positional rule) is answered without contradicting any
  standing rule; kill iff the window forces the et-reading false;
  null iff inconclusive or a standing-rule contradiction blocks decision —
  then escalate with the contradiction as headline.

## Method

Read BATTERY-PROTOCOL.md first. Created
`locks/veut-86-1392-adjudicate.lock` on start (agent id + UTC timestamp;
no pre-existing lock). Re-derived the 1,847-pair / 96-type stream from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed per `repair_parse.py` (upstream tokenization
`[s[i:i+2] for i in range(o, len(s)-1, 2)]`; 1847 pairs, 96 types
verified). `canonical.py` never touched. R5005, sealed gates, and the
red-team adjudication queue untouched.

Offset note: the stem-class-split census labels stem cells by the 29's
offset ("@1392" = the 29). On the re-derived stream the tokens are:
67 @1390, 86 @1391, 29 @1392, 89 @1393 (row a7_07, @1387–@1414).
All @-offsets below are 0-based token offsets on the repaired stream.

## Window-level evidence

### The locus

Row a7_07 @1387–@1396: `16 06 29 67 86 29 89 16 76 47`
(@1387=16, @1388=06, @1389=29, **@1390=67**, @1391=86, @1392=29,
@1393=89, @1394=16, @1395=76, @1396=47).

Standing values in play: 29='er' (GT), 06='ent' verb ending (promoted),
86=INF-class (A9, pour-taking infinitive), 47='ce' (A4), 77='le'
(provisional), 87='ce', 11='la', 00='pour', 46='que'; 16/76/89 open.

### 67 census (re-derived, n=38)

67='veut' under the §7 positional rule (follower infinitive-shaped)
fires at exactly 5 windows: @110 ("21 67 93 29"), @272 ("06 67 33 29"),
@1423 ("21 67 33 29"), @1476 ("06 67 33 29"), **@1390 ("29 67 86 29")**.
@1390 is the ONLY 67 whose infinitive-shaped follower is 86. The other
33 windows resolve "et" (follower not infinitive-shaped), including
@1098 ("29 67 86 52" — same "06 29 67 86" formula as @1390, but 86
followed by 52, not 29).

### The conflict (headline finding)

Two standing rule systems classify @1390 oppositely, byte-exact:

- **System A — `code/crowd7/morphologist/battery67_final.json`** (red-team
  graded, rounds 7–9; n=38 tally et=18/veut=11/open=9; positions match the
  repaired stream exactly). **R_et3**: "pre2 in {06,86} and pre == 29
  (infinitive formula)". At @1390: pre=@1389=29 ✓, pre2=@1388=06 ✓ →
  **fires → 67="et"**. Row entry verified: pos=1390, class=et,
  et_rules=[R_et3]. The crowd13 islet-audit re-verified:
  "@1098/@1390 «[06]er et»" with "no counterdatum".
- **System B — §7 positional rule** (BATTERY-PROTOCOL.md, crowd17
  pipeline): "67='veut' iff follower infinitive-shaped". At @1390:
  suc=@1391=86, suc2=@1392=29 → follower infinitive-shaped →
  **67="veut"**.

The same conflict holds at @272 and @1476 (R_et1 "pre in {06,86}" →
et, vs positional rule → veut). No lane document retires R_et1/R_et3 or
scopes the positional rule against them. Both systems are standing.

### Grammaticality of "et [86]er" (C1)

FOR (et available): R_et3 is red-team-graded with era word-space legs
("infinitive formula"); the crowd13 islet-audit re-verified the
"[06]er et" reading at @1098/@1390; the stem-class-split null (2026-10-09)
independently asserted "'et [86]er' is grammatical". Three prior lane
passes converge on availability.

AGAINST / residual: the infinitive coordination "[06]er et [86]er" has no
overt licensor. The only candidate is 16 (open). Corpus check: "16 X 29"
occurs 2× stream-wide (@1198 "16 64 29", @1387 "16 06 29"); 16's profile
(n=28; top follower 00 ×4, top predecessor 82 ×11 "m[16]") shows no
infinitive-licensor shape. This weakens but does not kill the et-reading:
R_et3's era legs carry the grammaticality, and the residual is fenced
here, not resolved.

The "veut" reading ("veut [86]er") is a clean modal+infinitive core;
its subject slot is open, but the lane already tolerates this at
@272/@1476 ("06 veut [33]er"), so subject-ellipsis does not discriminate.

## Per-clause results

- **C1: PASS.** "et [86]er" is grammatical/available at @1390: the
  standing R_et3 classification (red-team-graded, era legs) plus the
  crowd13 islet-audit re-verification ("[06]er et", no counterdatum)
  establish availability under standing values with no new polyvalence.
  The 16-licensor residual is fenced with cause above.
- **C2: PASS (conditional).** Under value-resolved governors, 33's
  67-governors (@272/@1423/@1476) read "veut" via the positional rule and
  86's @1390 67-governor reads "et" via R_et3 → governor sets
  {veut, 37, ce} vs {le, pour, et} are disjoint → the stem-class-split
  strict bar's C1 would hold.
- **Adverse ("67 positional rule, 67 sole true polyvalence"): BLOCKED.**
  Promoting the et-reading at @1390 would contradict the granted §7
  positional rule, which fires "veut" on the same window. No new
  polyvalence is declared (§7 intact); the block is a conflict between
  two standing systems, not a worker-grade call.

## Verdict: NULL — escalate to red team

**Headline: standing-rule contradiction at @1390.** The red-team-graded
`battery67_final.json` R_et3 classifies 67 @1390 as "et" (re-verified by
the crowd13 islet-audit); the granted §7 positional rule classifies the
same window as "veut". A battery cannot retire or scope either system.
The et-reading IS available (C1 passes), so the stem-class-split strict
bar is one red-team ruling away from holding — but that ruling is not
mine to make.

No standing verdict downgraded or contradicted by this battery beyond
surfacing the pre-existing R_et3-vs-positional-rule conflict. No
polyvalence declared.

## Follow-ups proposed (for supervisor queuing)

1. `r-et3-vs-positional-redteam` (P1) — Red-team adjudication: does R_et3
   (battery67_final.json, "pre2 in {06,86} and pre == 29") survive the §7
   positional rule, or is it retired/scoped? Same question for R_et1 at
   @272/@1476. Until ruled, 67 @1390 is indeterminate and stem-class-split
   C1 stays failed. This is the blocking question; the other two are
   independent of its answer.
2. `et86er-licensor-16` (P3) — If R_et3 survives: what licenses the
   "[06]er et [86]er" infinitive coordination? Census "16 X 29" (2×:
   @1198, @1387), the "06 29 67 86" formula's two instances (@1098
   et-rule vs @1390 contested), and 16's full contact profile (n=28).
   Bar: name the licensor with ≥2 frame-legs or fence 16 as the blocker.
3. `veut67-subject-census` (P3) — Census the subject slot of all five
   positional-rule veut-67s (@110 pre=21, @272 pre=06, @1390 pre=29,
   @1423 pre=21, @1476 pre=06). If "veut" systematically lacks an overt
   subject, the positional rule's "if" direction weakens and the
   veut-reading at @1390 loses its cleanliness edge.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-veut-86-1392-adjudicate.md`
  (this file).
- Queue: `battery-queue.json` `veut-86-1392-adjudicate` → status
  `verdict`, result `null`, date 2026-10-09 (re-read before write;
  temp-file + rename; only this entry modified; JSON re-validated).
- Lock: created on start with agent id + UTC timestamp (no pre-existing
  lock); deleted on completion.
