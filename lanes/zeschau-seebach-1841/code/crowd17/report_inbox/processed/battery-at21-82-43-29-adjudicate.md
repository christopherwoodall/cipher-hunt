# Battery report: at21-82-43-29-adjudicate

- Target: at21-82-43-29-adjudicate (priority 1)
- Claim: "82-43-29" @19-22 (row a1_00, interior) is word-internal ('mener'/'emmener'-family with 43='en') or a verb-stem slot — 43 is not a standalone noun here.
- Worker: subagent 0ef99a21-0e18-49e4-b550-00a202e8c5fd
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py (assert 1,847 passed). `canonical.py` never used. R5005 untouched. Red-team adjudication queue untouched. No data invented. @-offsets are 0-based stream indices.
- Lock: created `code/crowd17/next-token/locks/at21-82-43-29-adjudicate.lock` on start, deleted on completion.

## HEADLINE: red-team escalation

Clause (c) of the bar cannot be satisfied at battery level. @21 forces 43
word-internal ('en' in 'mener'); @343/@1027 'par [43]' forces noun-43
('par suite' the only grammatical reading). No single value covers both
windows, and declaring a second polyvalence (or a positional rule for 43)
is a red-team act under protocol §7 (67 et/veut is the sole true
polyvalence). Petition below in §6. This null contradicts no standing
red-team verdict (no ruling exists on 43's value) and downgrades no queue
verdict (noun-43 is still queued, not verdict-recorded).

## Bar (verbatim, pre-registered)

"(a) name 98 (modal/governor, or 'em') with 'qui 98 mener ce 33' parsing as one grammatical run; (b) state 43's class at @21 (noun vs verb-stem vs 'en') with the boundary analysis from this report either confirmed or overturned with cause; (c) reconcile with the 'par [43]' noun frames — one value must cover both windows, or petition the red team on the 67-sole-polyvalence rule with stated cause"

## Bar restated as numbered pass/fail clauses

1. Clause (a): 98 takes a named value (modal/governor, or 'em') such that
   "qui 98 mener ce 33" (@17-24) parses as one grammatical French run.
2. Clause (b): 43's class at @21 stated (noun vs verb-stem vs 'en'); the
   noun-43-discriminator kill report's boundary analysis confirmed or
   overturned with cause.
3. Clause (c): one 43 value covers both @21 and the 'par [43]' frames
   (@343/@1027), or a red-team petition on the 67-sole-polyvalence rule is
   filed with stated cause.

## Method

Re-derived every number from the repaired stream. Verified @21's window,
the uniqueness of the 82-43-29 trigram, all 16 windows of 43 with
immediate neighbors, all 40 windows of 98 (±4 context), the 98-83 x5
'de'-frames, the doubled-98 x3 pairs, and the 'par [43]' windows
@343/@1027. Named no open group except 98 (at lead strength, fenced
residuals stated). Used only banked/granted values (82='m', 29='er',
64='qui', 47='ce' A4, 86 INF-class A9, 00='pour' A9).

## Window-level evidence

**@21 (a1_00, row interior; row spans @0-34, length 35):**
`15:91 16:53 17:17=fois 18:64=qui 19:98 20:82 21:43 22:29=er 23:47=ce 24:33 25:55 26:81 27:00=pour`
The 82-43-29 trigram @20-22 is UNIQUE in the stream (only occurrence).
Read: "...qui [98] m-V(43)-er ce [33]".

**43 census (n=16), immediate neighbors:** @21 `82-43-29` (a1_00);
@43 `88-43-81`; @244 `56-43-00`; @258 `32-43-77`; @343 `96-43-87`
("par [43]", a2_05); @386 `37-43-91`; @439 `46-43-98`; @563 `11-43-24`
("la [43]"); @1027 `96-43-87` ("par [43]", a6_03); @1092 `06-43-07`;
@1126 `37-43-00`; @1204 `47-43-55`; @1303 `08-43-21`; @1305 `21-43-77`;
@1544 `78-43-00`; @1724 `37-43-98`. @21 is the ONLY 82-contact and the
ONLY 29-contact of 43 in the stream.

**98 census (n=40):** predecessors top 62 x5, 42 x3, 66 x3, 98 x3;
successors top 83 x5, 82 x3, 80 x3, 98 x3, 00 x3.

**98-83 x5 ('de'-frames):**
- @227: `46-98-83-82-96-21` = "que vient de me parvenir" (byte-identical
  formula member)
- @1060: `09-98-83-82-96-21` = "[09] vient de me parvenir" (formula)
- @1783: `23-98-83-82-96-21` = "[23] vient de me parvenir" (formula)
- @897: `14-98-83-86-16` = "[14] vient de [86-inf]" — second 'venir de +
  INF' frame type (86 INF-class, A9 granted)
- @930: `48-82-98-83-56` = "me vient de [56]" — awkward, fenced residual

**98-00 ('pour'-frames):** @1137 `62-98-00` = "[62] vient pour" ✓;
@1373 `67-98-00-86` = "et vient pour [86-inf]" ✓ (finite 'vient' as
follower is consistent with the 67 positional rule: 67='et' here, not
'veut'); @1139 `00-98` = "pour [98]" needs infinitive 'venir' — fenced
(inflectional alternation is a red-team act); @1601 `82-98-00` awkward,
fenced.

**Doubled 98 x3 (fenced residuals):** @1073 `42-98-98-12-48`,
@1145 `42-98-98-86`, @1660 `47-98-98-80` — "vient vient" ungrammatical in
all three; stated cause for keeping 98='vient' at LEAD, not grant.

**@702:** `12-98-20` = "n'vient" — bad elision before consonant 'v';
fenced residual.

**'par [43]' x2:** @343 `45-64-96-43-87-01` and @1027 `45-64-96-43-87-01`
(byte-identical 6-gram) = "ce qui par [43] ce [01]". "par [43]" requires
a noun; "par suite" is the only grammatical reading of the queued
candidate set (per the kill report; "par en" is ungrammatical).

**33-21 x3 (positional precedent for noun-shaped 33):** @936, @1421,
@1630 (re-derived; queue's @937/@1422/@1631 are the 21-side offsets).

## Per-clause pass/fail

1. Clause (a) — CONDITIONAL PASS. 98='vient' (finite; semi-auxiliary
   governor): 6 clean legs (@227/@1060/@1783 formula 'vient de me
   parvenir' x3 byte-identical; @897 'vient de [86-inf]' second frame
   type; @1137 '[62] vient pour'; @1373 'et vient pour [86-inf]').
   Modal rivals ('peut'/'doit'/'veut'/'sait') are all killed by the
   98-83 x5 'de'-frames ('peut de' etc. are ungrammatical; only
   'vient de' survives). The 'em' arm FAILS: "qui emmener" (relative
   pronoun 64='qui' granted + bare infinitive, no governing
   preposition at @17-24) is ungrammatical — recorded, not ignored.
   The run parses as "qui vient mener ce [33]" = "who comes to lead
   this [noun]" — CONDITIONAL on 33 taking a noun slot at @24
   ('ce' + noun, 47='ce' A4 fixed). 33-as-noun is ungranted
   (croire-33-noun21 still queued); 33-21 x3 give positional precedent
   only. Fenced residuals: doubled-98 x3, @702, @930, @1139, @1601
   (stated causes above).
2. Clause (b) — CONFIRMED. The kill report's boundary analysis stands,
   re-derived: with banked 82='m' and 29='er', the only French words
   spanning 82-43-29 are 'mener' (43='en') and 'emmener' (98='em' +
   'mener'; 'em' arm dead per clause 1). Standalone-noun placements
   ("msuiteer"/"suiteer"/"erce") are not French; no missed boundary
   ('m|en|er', 'me|ner' all fail). 43 at @21 is the word-internal
   syllable 'en' — not a standalone noun, not an independent
   verb-stem (the verb-stem reading collapses to the same 'm[en]er').
   The reading is unique to @21 (only 82/29 contact of 43 in the
   stream).
3. Clause (c) — FAIL, petition filed (§6). No single value covers both
   @21 (word-internal 'en') and @343/@1027 ('par [43]' noun: 'par en'
   ungrammatical; noun-43 candidates give 'mconditioner'/'mmesureer',
   not French). The 67-sole-polyvalence rule bars a battery-level
   declaration.

## Adverses

- "'par [43]' x2 pulls noun-ward" — answered via clause (c): the pull
  is real and irreconcilable at battery level; escalated to red team
  with stated cause (§6), not ignored.
- "98/33 open" — 98 named 'vient' at LEAD strength (6 legs, 6 fenced
  residuals); 33-as-noun at @24 left conditional and fenced (owning
  battery croire-33-noun21 still queued; its bar not re-run).
- "47='ce' (A4) fixed" — used as fixed; 'ce'+noun is the load-bearing
  parse of the run.
- "'qui [98] mener' needs 98 as modal/governor" — satisfied: 'venir' +
  bare infinitive ("viens manger", "il vient mener") is standard
  French; 98='vient' is a governor.

## Verdict: NULL

Not promote: clause (c) fails and clause (a) is conditional on an
ungranted 33 reading. Not kill: no window forces the @21 claim false —
the claim is specifically about @21, and @21's word-internal reading is
confirmed; the failure is global reconciliation, which belongs to the
red team. Escalation is the headline.

## §6 Red-team petition (stated cause)

43 needs either (i) a positional polyvalence — 'en' word-internal in
the unique 82-43-29 trigram (@21) vs noun elsewhere — declared by the
red team under an exception to the 67-sole-polyvalence rule; or
(ii) a ruling that @21 adjudicates 43's class globally, killing
noun-43 (queued) and stranding the clean 'par suite' frames at
@343/@1027, which would then need re-reading. Path (i) is the cheaper:
the word-internal reading touches exactly one window (@21, the only
82/29 contact), while the noun frames (@343/@1027 'par', @563 'la',
@1126/@1724 predicative continuations) are untouched. Battery takes no
position beyond the evidence; the red team decides.

## Follow-up targets (for the supervisor to queue)

1. id: "vient-98-name" | priority: 2
   claim: "98='vient' (finite semi-auxiliary) at battery grade"
   bars: "promote iff >=2 'vient de' frame-types hold (formula x3 +
   @897 '[14] vient de [86-inf]') with the doubled-98 x3 (@1073/@1145/
   @1660), @702 ('n'vient'), @1139 ('pour [98]'), @930 and @1601 each
   fenced or resolved with stated cause; zero board contradictions"
   evidence: "98-83 x5: @227/@1060/@1783 'vient de me parvenir' formula
   x3 byte-identical, @897 'vient de [86-inf]' (86 INF-class A9);
   98-00: @1137 '[62] vient pour', @1373 'et vient pour [86-inf]'
   (67='et' consistent with positional rule); modal rivals killed by
   'de'-frames; 'em' arm dead ('qui emmener' ungrammatical)"
   adverses: "doubled 98 x3 ungrammatical under 'vient'; @1139 needs
   infinitive 'venir' (inflectional alternation = red-team act)"

2. id: "ce33-noun-slot" | priority: 2
   claim: "33 takes a noun slot at @24 ('ce 33' = 'ce [N]')"
   bars: "resolve iff 'ce 33' @23-24 parses with 33's class stated,
   using 33-21 x3 (@936/@1421/@1630) as positional precedent;
   coordinate with queued croire-33-noun21, do not re-run its bar"
   evidence: "'qui vient mener ce [33]' needs 'ce'+noun (47='ce' A4);
   'le dire' substantivized-infinitive precedent exists"
   adverses: "33={dire,[X]er} set null; A10 stem/whole HOLD;
   33-as-noun ungranted"

3. id: "en43-wordinternal-census" | priority: 3
   claim: "@21 is the only window where 43 reads word-internal 'en'"
   bars: "confirm-or-reject per-window: for each of 43's 16 windows,
   record whether a word-internal 'en' parse exists; pass iff only
   @21 (the sole 82/29 contact) admits one"
   evidence: "43 neighbor census: @21 '82-43-29' unique; no other
   82/29 contact in 16 windows; informs the 43-polyvalence petition"
   adverses: "none new; feeds (does not pre-empt) red-team
   adjudication"
