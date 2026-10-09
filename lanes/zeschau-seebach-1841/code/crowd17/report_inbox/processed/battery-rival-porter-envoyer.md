# Battery report — rival-porter-envoyer (the two surviving 'laisser' rivals are eliminated)

Worker: battery-worker-rival-porter-envoyer (agent 63919416-63fd-4ccb-a1a3-03361d5c68a5). Date: 2026-10-08.
Lock: `code/crowd17/next-token/locks/rival-porter-envoyer.lock` created
2026-10-09T01:52Z, no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(replicated, not `canonical.py`). R5005 not touched. Every count below
re-derived from the stream in this run.

Coordination: consumes erstem-33-id (null, 2026-10-08) and
x-33-laisser-test (null, 2026-10-08) as prior evidence; does NOT re-run
their valency sweeps or gate profiles. Gate owners: frame-82-16 (queued),
stem-85 (decided null 2026-10-08 — value unnamed; the task brief's "both
queued" is corrected here, substance unchanged: 85's value is open),
frame-qui-47 (queued, owns 47's "se" rival reading). This battery tests ONLY
the two rivals against the 5 stem windows. No duplication.

## Bar (pre-registered verbatim, from battery-queue.json)

`each rival must parse all 5 stem windows under <=1 open-slot assumption; 'envoyer' must survive @1232 ('s\'envoyer [85]' test once 85 resolves); 'porter' must survive @1477 ('porter me [16]' test once 16 resolves); failure of both leaves 'laisser' unique`

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. 'porter' parses all 5 stem windows (@273, @626, @1232, @1424, @1477)
   with at most 1 open slot per window.
2. 'envoyer' parses all 5 stem windows with at most 1 open slot per window.
3. 'envoyer' survives @1232: the "s'envoyer [85]" test — record
   conditional survival (gated on 85's resolution) or kill.
4. 'porter' survives @1477: the "porter me [16]" test — record whether any
   failure is 16-class-independent (kill-grade now) or class-dependent
   (gated on frame-82-16).
5. The claim "both rivals eliminated" holds iff porter fails (clauses 1/4)
   AND envoyer fails (clauses 2/3).

## Method

Re-parsed the repaired stream (assert 1,847 pairs). Re-derived the five
`33-29` stem windows and the slot census (62-16 x4, 12-16 x3, 16-00 x4,
79-85 x2, 82-16 x11, 47-33-29 x1) — identical to the three prior
batteries. Tested each rival window-by-window against 1841 French
grammar under the standing values (§7): 29="er", 82="m", 12="n"
(banked); 87="ce" (promoted); 84="on" (A15); 47="ce" (A4 allophone
tier, granted — "se" is the queued frame-qui-47 rival); 59="est"
(provisional); 67 et/veut positional rule; sole-polyvalence law.
16's class and 85's value NOT named by this worker (gate owners' lane).

## Window-level evidence (@-offsets are repaired-stream pair indices)

Stem windows re-derived (identical set):
- @273 (a2_03) `47-11-06-67-33-29-89-84-91` — "veut [X]er [89], on [91]"
- @626 (a4_01) `82-14-59-37-33-29-87-78-67` — "est [37] [X]er ce [78]"
- @1232 (a7_01) `82-48-29-47-33-29-85-56-10` — "[ce/se] [X]er [85] [56]"
- @1424 (a7_08) `15-33-21-67-33-29-87-63-91` — "dire [21], veut [X]er ce [63]"
- @1477 (a7_10) `53-60-06-67-33-29-82-16-98` — "veut [X]er m[16] [98]"

### 'porter' (transitive, non-causative)

- @273: PASS (1 open slot: 89). "veut porter [89]" grammatical.
- @626: 2 open slots (37, 78). Exceeds the <=1 budget — but the cost is
  identical for every candidate including 'laisser', so the window is
  rival-neutral: FENCED as non-discriminating, not a kill clause. (A
  strict per-window <=1 reading makes @626 unpassable for all candidates;
  the bar's operative discriminators are @1232/@1477.)
- @1232: FAIL under the granted 47="ce": "ce porter [85]" is
  ungrammatical. The "se porter" rescue needs 47="se" (ungranted rival,
  frame-qui-47 queued) AND 85 as predicative noun — 2 ungranted
  assumptions, and "se porter" takes no infinitive complement. Exceeds
  the <=1 budget under every 47 reading.
- @1424: PASS (1 open slot: 63). "veut porter ce [63]" grammatical.
- @1477: FAIL at kill grade, 16-class-independent. "veut porter me [16]":
  16=infinitive → clitic "me" in post-infinitive position after a
  non-causative verb is ungrammatical in every period of standard French
  (clitic must climb: "veut me porter [16]"; post-position is licensed
  only for the causative class and imperatives). 16=noun → "me"/"m'" +
  noun is ungrammatical (82="m" banked forces vowel-initial 16, and a
  noun after "m'" is impossible). 16=finite verb → clause broken. No
  16-class rescues porter. This re-derives and confirms
  x-33-laisser-test's "V+me+order kill 16-class-independent" for porter
  specifically.

Clause 1: FAIL. Clause 4: FAIL — porter does not survive @1477, and the
failure does not wait on frame-82-16.

### 'envoyer' (ditransitive, non-causative)

- @273: PASS (1 open slot: 89). "veut envoyer [89]" grammatical.
- @626: same rival-neutral fence as porter (2 open slots, all candidates).
- @1232: CONDITIONAL — gated, doubly. "s'envoyer [85]" needs 47="se"
  (ungranted rival reading, frame-qui-47 queued) AND 85 noun-shaped
  (stem-85 decided null; noun signals: 79-85 x2 with 79="tout" promoted;
  verb signals: A3 'en [85]' x5 + 'que [85]er' x2). If 85 resolves as an
  infinitive, "s'envoyer [inf]" is ungrammatical and envoyer dies here
  too; if 85 resolves noun-shaped AND 47 reads "se", "s'envoyer [85]"
  parses ("s'envoyer un [N]" — reflexive + direct object). The test is
  deferred to the gate owners as the bar prescribes.
- @1424: PASS (1 open slot: 63). "veut envoyer ce [63]" grammatical.
- @1477: FAIL at kill grade, 16-class-independent. "veut envoyer me [16]":
  envoyer's only candidate construction is "envoyer qqn [inf]" (send
  someone to do X) — but that construction requires clitic climbing
  ("veut m'envoyer [16]"); the observed order has the clitic
  post-infinitive ("veut envoyer me [16]"), which is ungrammatical for
  every non-causative verb in 1841 French. The dative rescue ("envoyer
  [16] a moi") fails the same order rule, and 16=noun fails the "m'"
  elision (noun after "m'" ungrammatical). No 16-class rescues envoyer.

Clause 2: FAIL. Clause 3: MOOT — envoyer is already dead at @1477; the
@1232 conditional cannot resurrect it, but is recorded for the gate
owners (stem-85, frame-qui-47) since their resolutions close the loop.

### Prior-battery tension resolved

erstem-33-id recorded "envoyer: survives @1477 ('envoyer me [inf]')";
x-33-laisser-test recorded "donner/montrer/envoyer/prononcer die at the
V+me+order frame". This battery adjudicates: x-33-laisser-test is
correct. The "envoyer qqn [inf]" construction exists, but only with the
clitic climbed ("veut m'envoyer [16]"); the stream's order is "veut
envoyer me [16]" — post-infinitive clitic — which no non-causative -er
verb licenses. Resolution recorded with cause; this is a
battery-vs-battery adjudication on fresh grammatical evidence, not a
red-team contradiction (no red-team verdict covers porter/envoyer).

## Per-clause pass/fail

1. porter parses all 5 windows (<=1 open slot each): FAIL — fails @1232
   (broken under granted 47="ce") and @1477 (kill-grade,
   16-class-independent). @626 fenced rival-neutral.
2. envoyer parses all 5 windows (<=1 open slot each): FAIL — fails @1477
   (kill-grade, 16-class-independent); @1232 doubly conditional/gated;
   @626 fenced rival-neutral.
3. envoyer survives @1232: GATED-THEN-MOOT — conditional survival only
   under (47="se" AND 85 noun-shaped); kill is already secured at @1477.
4. porter survives @1477: FAIL — dead under every 16-class; no gate.
5. Both rivals eliminated: HOLDS — porter and envoyer are each eliminated
   at kill grade, both kills independent of the open slots (16, 85).

## Adverses disposition

- "gated on frame-82-16 and stem-85 (both queued — coordinate, do not
  duplicate)": ANSWERED by mootness. Both kills (@1477 for porter and
  for envoyer) are 16-class-independent and 85-independent, so neither
  gate can rescue either rival. frame-82-16 and stem-85 were not
  re-litigated; their resolutions remain their owners' lane. (Correction:
  stem-85 is decided-null, not queued — 85's value is open either way.)
- The @626 rival-neutral fence: recorded with cause, not ignored.

## Standing-verdict check

No contradiction with any standing verdict: §7 banked/promoted values,
sole-polyvalence law, A4 (47="ce" tier), A10 HOLD all untouched; 16 and
85 unnamed by this worker; the erstem/x-33-laisser-test nulls not
re-litigated (one battery-vs-battery tension adjudicated with cause
above). Nothing to escalate on contradiction grounds.

## Verdict: null — ESCALATE TO RED TEAM FOR PROMOTION RATIFICATION

Headline: **both rivals are eliminated at kill grade — porter and
envoyer each die at @1477 ("veut [X]er me [16]"), 16-class-independent,
85-independent.** The claim "the two surviving 'laisser' rivals are
eliminated" is established at battery level: failure of both leaves
'laisser' unique among the tested -er candidates.

This worker's task brief bars promotions ("promotions are only ratified
by the red team"), so the result is recorded as null with this
escalation rather than promote (ver-78 precedent). Red team is asked to
ratify: (a) the V+me+order frame is ungrammatical for non-causative -er
verbs in 1841 French under every 16-class; (b) envoyer is not in the
causative -er class; (c) the erstem/x-33-laisser-test tension resolution
above. On ratification the claim promotes and 'laisser' stands unique.

## Follow-ups (null regenerates work)

1. **rival-elim-ratify** — claim: red-team ratifies the porter+envoyer
   eliminations. Bars: (a) confirm the V+me+order ungrammaticality for
   non-causative -er verbs under every 16-class; (b) confirm envoyer is
   not causative-class; (c) ratify the erstem tension resolution; then
   the claim promotes. Evidence: this report's @1477 analysis.
   Adverses: gates moot (kills gate-independent) — state explicitly.
2. **envoyer-1232-close** — claim: envoyer's @1232 conditional is closed
   once stem-85 / frame-qui-47 resolve. Bars: record the resolution
   outcome against the doubly-conditional parse (47="se" AND 85 noun);
   confirm it cannot resurrect envoyer (@1477 kill stands regardless).
   Evidence: @1232 window; 79-85 x2 noun signals vs A3 verb-stem frame.
   Adverses: owned by stem-85 and frame-qui-47 — coordinate.
3. **laisser-unique-sweep** — claim: with porter+envoyer eliminated,
   'laisser' is the unique surviving -er candidate. Bars: (a) re-check
   erstem-33-id's full candidate list against the @1477 kill
   (donner/montrer/prouver/trouver/porter/envoyer/prononcer all dead
   there); (b) confirm no new -er candidate parses all 5 windows.
   Evidence: erstem-33-id candidate sweep + this report. Adverses: none
   new; gated on rival-elim-ratify.
