# Battery report: skeleton-1032-revise

- Target id: `skeleton-1032-revise`
- Claim: re-parse @1028–1040 without the killed bare-'ce'-topic; the imp-80-set skeleton must be revised.
- Date: 2026-10-09
- Worker: battery worker (subagent 7acc2003-3aee-490f-bd36-c2f9f0f6451c)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Re-derived in-session: 1,847 pairs confirmed. canonical.py never used.
  R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/skeleton-1032-revise.lock (created at
  start, deleted on completion; no prior lock for this id existed).

Terms (ASD-STE100): "exclamatory infinitive" = an infinitive used as an
exclamation ("Moi, me taire !" = "me, to shut up!"). "Tonic" = the stressed
form (moi, cela, ceci). "Clitic" = the unstressed form (me, ce).

## Bar (verbatim from target; bars field was empty, so numbered bars were
derived from the claim BEFORE testing, per the task brief)

Parent-mandated bar (from ce87-topic-licensing follow-up 1): "re-parse
@1028-1040 under standing values without the killed bare-'ce'-topic. Bar:
one grammatical 1841-French parse with <=1 non-granted value assumption,
or fence the residual. 87='ce' value stands; its role is the open
question."

Numbered pass/fail clauses (derived before testing, not modified after):

1. Re-parse @1028–1040 with ZERO reliance on the killed bare-'ce'-topic
   (no dislocated clitic "ce" heading an exclamatory infinitive).
2. Produce the revised imp-80-set skeleton: every group in @1028–1040
   parses under standing values (banked GT, granted/promoted,
   provisional, battery-grade class findings), with <=1 non-granted
   value assumption.
3. No window requires the dead reading at kill grade (if one does, the
   revision fails and the residual is fenced).

## Method

1. Read BATTERY-PROTOCOL.md first. Created/deleted the lock per protocol.
2. Re-derived the repaired stream in-session (1,847 pairs). Byte-verified:
   @1028–1040 = "87 01 03 29 80 77 11 70 82 34 29 40 17" (row a6_03,
   row span 1020–1045); left context @1024–1027 = "45 64 96 43";
   tail @1041–1044 = "77 82 63 11". canonical.py never used.
3. Adopted, not re-litigated: ce87-topic-licensing KILL (bare-'ce'
   dislocation dead at kill grade); poly-80-x29-frame C1 PASS
   ("[03]er [80]-le" = infinitive + imperative 80-stem with enclitic
   'le', right edge "la première fois" fully grammatical); the
   conditioned 03 split (03 = verb stem in "03 29" = [03]er);
   ci-bound-01's ce-context restriction (bound '-ci' survives in
   ce-contexts); ce01-slot-1029's candidate-C kill (clause-boundary at
   01's slot dead) and its candidate-A/B kill (both needed the dead
   bare-'ce' topic).
4. Ran a targeted corpus check in the lane's 1841-register corpus
   (code/side-period/corpus/) for demonstrative-headed exclamatory
   infinitives; used the parent battery's established counts for the
   fronted-tonic slot ("cela," x291, "ceci," x39, "ça," x5; tonic-head
   + infinitive constructions x22).

## Window-level evidence

### The window (byte-exact, repaired stream)

@1028–1040 (row a6_03): `87 01 03 29 80 77 11 70 82 34 29 40 17`

### Revised skeleton: "Ceci, [03]er! [80]-le, la première fois!"

Group-by-group under standing values:

- **@1028–1029 "87 01" = "ceci" (fused tonic demonstrative).**
  87="ce" granted; bound "-ci" restricted to ce-contexts (87 at -1 is
  the direct ce-context; ci-demonstrative-census confirms this
  classification). "ce"+"ci" as two words is ungrammatical in French,
  so the groups fuse — the same dissolution model as the granted
  "cela" = 87+11 compounds. The killed construction was a *bare
  clitic* "ce" topic; "ceci" is the *tonic* form, which is exactly the
  form the parent kill's grammar prescription demands in the
  dislocation slot (Littré: "ce" atonic; Beauzée: ceci/cela are the
  standalone forms). Zero reliance on the dead reading.
- **@1030–1031 "03 29" = "[03]er" (exclamatory infinitive).**
  29="er" banked GT; 03 is a verb stem here under the conditioned
  03 split (verb stem only in "03 29" = [03]er, battery-grade). The
  infinitive is exclamatory with unexpressed subject; "ceci" sits as
  the fronted tonic topic — the "Eux, partir !" / "Moi, me taire !"
  shape, with the demonstrative supplying the disjunctive form the
  construction requires. Corpus: fronted "ceci," x39; tonic
  demonstratives own the fronted-topic slot (x335); tonic-head +
  infinitive constructions x22 (parent battery census).
- **@1032–1033 "80 77" = "[80]-le" (imperative 80-stem + enclitic).**
  Adopted from poly-80-x29-frame C1 (PASS at this exact window):
  80 is verb-form (imperative stem, battery-grade class), 77="le"
  provisional enclitic. No new assumption.
- **@1034–1040 "11 70 82 34 29 40 17" = "la première fois".**
  11="la" GT, 70="pre" GT, 82="m" GT (letter), 34="i" GT (letter),
  29="er" GT, 40="e" GT, 17="fois" granted. This is the byte-anchored
  "la première" pencil-gloss crib + "fois". Fully granted.

Value-assumption count: the only non-granted value used is the bound
"-ci" at 01 (battery-level NULL, surviving, consistent with the
standing ce-context restriction) = exactly 1, within the parent bar's
<=1 allowance. 77="le" is provisional (standing). 03 and 80 are read
at class level (battery-grade), their values stay open.

### Why the dead reading is not needed anywhere

The killed assumption was "bare 'ce' (87) as a dislocated topic heading
the exclamatory infinitive". The revised parse has no bare "ce": 87 is
fused into tonic "ceci", and the dislocation slot holds the tonic form
— the grammar's licensed occupant. Neither the infinitive ("[03]er!")
nor the imperative ("[80]-le") nor the adverbial ("la première fois")
depends on any "ce"-topic.

### Fenced (outside the window, stated cause)

- Left edge @1024–1027 "45 64 96 43" = "ce(45, A4) qui(64) par(96)
  [43]": no finite verb under any live reading, so a sentence/clause
  boundary falls at or before @1028. The exact boundary position is
  outside this target's window and stays fenced (edge-1024-clause-
  boundary's kill was computed under the old skeleton).
- Tail @1041–1044 "77 82 63 11": outside the window, not parsed here.
- 03's and 80's verb VALUES stay open (class-level reads only); the
  schematic French gloss is "Ceci, [X]er ! [Y]-le, la première fois !"

## Per-clause pass/fail

1. Zero reliance on the killed bare-'ce'-topic: **PASS.** The parse
   uses fused tonic "ceci"; the dislocated clitic "ce" appears
   nowhere.
2. Revised skeleton, every group under standing values, <=1
   non-granted value assumption: **PASS.** "Ceci, [03]er! [80]-le,
   la première fois!" — all groups accounted for (see evidence);
   sole non-granted value is bound "-ci" at 01 (battery-surviving,
   ce-context-licensed).
3. No window requires the dead reading at kill grade: **PASS.**
   Nothing in the window forces bare-"ce" dislocation back.

## Adverses

None listed on the target. Coordinated, not duplicated: ce87-topic-
licensing KILL (charter), poly-80-x29-frame PROMOTE (C1 adopted),
ci-bound-01 NULL (ce-context restriction honored), ce01-slot-1029
NULL (candidates A/B/C status adopted). No standing or red-team
verdict contradicted or downgraded; §7 intact (no polyvalence
declared — "ceci" is one fused word, and pronoun↔determiner for 45/87
is one French word per the lane's standing doctrine).

## Verdict: PROMOTE

The imp-80-set skeleton is revised to **"Ceci, [03]er! [80]-le, la
première fois!"** at battery grade. The bare-'ce'-topic is fully
excised; the tonic demonstrative "ceci" takes the dislocation slot
the grammar requires, the exclamatory infinitive and the imperative
+ enclitic frames are unchanged from the battery-promoted
poly-80-x29-frame reading, and the "la première fois" right edge is
the byte-anchored pencil crib. Needs red-team ratification before
banked use.

## Follow-ups (promote, not null — optional next steps noted)

1. `leftedge-1024-43-governor` (P3): license or fence the verbless
   "ce qui par [43]" left chunk now that the skeleton's left edge is
   "Ceci" — name 43's class or fence the fragment.
2. `ceci-1029-ratify-feed` (P4): package this window's "ceci" read as
   input for the red-team docket once the skeleton revision is
   ratified (feeds the open 01 "-ci" value question).

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-skeleton-1032-revise.md
  (this file).
- battery-queue.json: `skeleton-1032-revise` queued -> verdict/promote
  via temp-file + rename (pre-write assert confirmed queued/verdictless;
  JSON re-validated post-write; own entry only).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion.
- Stream re-derived in-session (1,847 pairs); canonical.py never used;
  R5005, sealed gates, red-team queue untouched.
- Every number traces to the stream or the cited reports/corpus; no
  invented data.
