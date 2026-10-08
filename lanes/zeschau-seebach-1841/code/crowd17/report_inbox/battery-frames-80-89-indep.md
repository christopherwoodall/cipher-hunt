# Battery report: frames-80-89-indep

- Target id: `frames-80-89-indep`
- Claim: "80/89 verb-frames hold with 77 unfixed (independent of 77='le')"
- Date: 2026-10-08
- Worker: subagent-a573ee26
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`).
  1,847 pairs confirmed. Never used `canonical.py`. R5005 untouched. No invented data.

## Bar (verbatim, pre-registered before testing)

"promote (independence confirmed) iff >=2 verb legs per cell parse with 77 held
unfixed (treat 77 as unknown, never as 'le') and zero contradictions; kill iff
the frames collapse without 77='le' (no verb leg survives unfixed); else null
with 1-3 follow-up targets. Do not overwrite A8's grant - this tests its
condition, not its content."

Numbered pass/fail clauses (restated, not modified):

1. PROMOTE iff (a) >=2 verb legs per cell (80 and 89) parse with 77 held
   unfixed (77 treated as unknown, never as 'le'), AND (b) zero contradictions
   (no window forces a non-verb reading of 80 or 89).
2. KILL iff the frames collapse without 77='le', i.e. no verb leg survives
   with 77 unfixed.
3. Else NULL, with 1-3 follow-up targets.
4. CONSTRAINT: do not overwrite A8's grant (test its condition, not its
   content); do not overwrite any standing red-team verdict (round-15
   `code/crowd15/report_inbox/next-token-redteam.md`, round-16
   `report_inbox/processed/next-token-redteam.md`). A result that contradicts
   one is recorded as null with the contradiction as headline, escalated.

Terms. A "leg" is one window that supports the frame. A "frame" is a recurring
construction. "Fenced" means set aside with stated cause. A "contradiction" is
a window that forces a non-verb reading (not merely an unparsed window).

## Method

1. Parsed the repaired stream exactly per the brief. Indexing convention:
   @-offsets are 0-indexed pair indices into the 1,847-pair parse; each @ cites
   the FIRST pair of the named frame (this matches prior reports: "87-77-80
   @515" has 87 at 515). The target cell's own index is one or two higher and
   is given in each transcription.
2. 77 discipline: 77 is treated as UNKNOWN in every window. No parse below
   assumes 77='le'. Windows that need 77 are fenced, not used as legs.
3. Values used (standing only): banked GT 11=la, 70=pre, 82=m, 34=i, 29=er,
   40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
   84=on (A15, R16-002 weakened), 47=ce; battery-promoted 24=modal
   (ne-24-profile, 2026-10-08), 06='ent' (ent-06, 2026-10-08), 48='e' (letter),
   94='ne'; provisional 59=est. 67='et'/'veut' positional rule (sole
   polyvalence) applied throughout.
4. Re-derived every count below from the stream. Census check: 80 n=17,
   89 n=14. Key bigrams re-derived: 24->85 x5, 24->89 x3 (@221/@985/@1497),
   24->80 x2 (@564/@672), 79->80 x3 (@468/@1010/@1089), 29->80 x4,
   29->89 x5, 89->48 x3, 89->84 x2, 80->06 x2 (@469/@1090), 87->77 x2
   (@515/@869), 00->86 x12, 86->29 x4.

## Window-level evidence

### A. Verb legs with 77 unfixed (all 77-absent)

The ne-24-profile battery (verdict: promote, 2026-10-08, standing) classes 24
as a finite verb, infinitive-taking (modal-shaped), and explicitly lists
24->80 x2 and 24->89 x3 as infinitive-frame complements. That classification
rests on 24->85 x5 (85=verb-stem, A3, independent of 80/89), so using it here
is not circular. The slot "[24-modal] ___" is verb-selecting; 80/89 in it are
verb-class (infinitive-slot). Residual noted: vouloir/savoir-shaped modals can
also take nouns, so the legs are frame-grade, not deductive; the battery's
"infinitive-taking" verdict is not re-litigated here.

Cell 80 (2 legs):

- @564: `67 11 43 24 80 97` (80 at 565). 67='et' (follower 11='la', not
  infinitive-shaped). Parse: "et la [43] [24-modal] [80-infinitive] [97]" =
  "and the [43] can [80] [97]". Subject NP "la [43]" present, modal +
  infinitive, object slot [97]. CLEAN. 77 absent.
- @672: `67 11 86 24 80 03 64` (80 at 673). Parse: "et la [86] [24-modal]
  [80-infinitive] [03] qui [37] [77]" = "and the [86] can [80] [03] which...".
  CLEAN. The trailing 77 sits inside the relative clause and does not touch
  the leg.

Cell 89 (2 solid + 1 weak):

- @221: `16 24 89 61` (89 at 222), wider `29 42 16 24 89 61 96 87 46`.
  Parse: "[42] [16] [24-modal] [89-infinitive] [61] par ce que". The
  modal+infinitive core is forced (a modal takes an infinitive, not a noun).
  Subject NP "42 16" fenced as open but slotted. LEG.
- @985: `01 24 89 48 01` (89 at 986). Parse: "[01] [24-modal]
  [89-infinitive] [48] [01]". The 48-junction is fenced: 48='e' (letter) cannot
  attach left ("[89]e" would unmake the infinitive under the modal), so it
  attaches right ("e[01]", 01 open, cause stated). LEG with fenced follower.
- @1497: `59 24 89 41` (89 at 1498), wider `66 15 59 24 89 41 74 84 33`.
  The "[24] [89]" core is modal+infinitive, but the left junction "59 24"
  ("est [24]") is broken under provisional 59='est'. WEAK: leg conditional on
  59's value here (fenced, 59 provisional).

Result: >=2 verb legs per cell, all with 77 unfixed. Clause 1(a): PASS.

### B. Contradictions (force non-verb readings)

- @1155: `00 92 29 80 17 77` (80 at 1156), wider
  `02 00 92 29 80 17 77 82 44`. Parse: "[02] pour [92]er [80] fois [77] [m]".
  The "[80] fois" slot forces 80 to be a determiner ('une fois', 'toutefois'
  as toute|fois) or preposition ('parfois' as par|fois). Every verb reading
  fails: finite verb + bare 'fois' is ungrammatical ("*[verb] fois"); "[92]er
  [80-infinitive] fois" is "[inf] [inf] fois", ungrammatical; imperative +
  'fois' fails. HARD contradiction for 80. (This confirms R16-001's "CLEAN
  determiner leg"; re-derived, not overwritten. 77 follows 'fois' and does not
  touch 80's slot.)
- @1376: `00 86 29 89 84` (89 at 1377), wider
  `98 00 86 29 89 84 92 69 13`. Parse: "[98] pour [86]er [89] on [92]...".
  00='pour' + 86 (INF-class, A9 red-team grant; 00->86 x12, 86->29 x4) gives
  "pour [infinitive]". After "pour [inf]", 89 must be a noun (direct object:
  "pour [faire] [X]") or adverb ("pour [parler] [bien]"). Every verb reading
  fails: "[inf] [89-finite] on" ungrammatical; "[inf] [89-infinitive] on"
  ungrammatical; "[89]-on" inversion cannot open a clause; 89-84 as one word
  ("[89]on") is still non-verb-89. HARD contradiction for 89. This hardens
  R16-001's "29-89 x5 tensions" at this window from tension to forced
  non-verb (new derivation; uses A9, not 77).
- @468: `00 33 79 80 06 67` (80 at 469), wider
  `96 00 33 79 80 06 67 46 84`. CONDITIONAL on 06='ent' (battery-promoted,
  2026-10-08). 67='et' (follower 46='que'). 06 cannot be word-initial before
  'et' (no French word begins "entet"), and 'ent' is not a standalone word,
  so 06 attaches left: 80-06 = "[80]ent", one word. "[80]ent" as 3pl verb
  fails subject agreement (*"tout [verb]ent", 'tout' is singular, no plural
  subject available). As adjective it parses: "pour [33-inf] tout [80]ent-adj
  et qu'on..." = "pour [rendre]-shaped [inf] tout [différent]-shaped, et
  qu'on..." ('to [X] everything [adj], and that one...'; 79='tout' as object,
  [80]ent as object complement, standard French). So 80 is adjective-forming
  here, not a verb. CONDITIONAL contradiction (falls back to fenced if
  06='ent' is overturned; 33-transitivity is compatible, unproven).

Result: 2 hard contradictions + 1 conditional. Clause 1(b) ("zero
contradictions"): FAIL.

### C. Fenced windows (cause stated)

- @515 (87-77-80) and @869 (87-77-89): the A8 C3 windows. With 77 unknown,
  "ce [77] [80/89]" cannot serve as a verb leg. Under the section-A
  infinitive-slot finding, "ce [77] [80/89-infinitive]" is ungrammatical, so a
  verb reading would need 77=clitic + finite 80/89 -- unassumed. FENCED:
  unresolvable without 77; consistent with verb-80/89 only under an unmade
  assumption. Neither confirms nor kills.
- @720 and @1032 (80-77 x2): the imp-80-set "imperative + enclitic 'le'"
  reading needs 77='le'. Unfixed: "21 [80] [77] 03" and "29 [80] [77] 11"
  admit no 77-independent verb parse. FENCED (need 77; @1032's dedicated
  battery went null).
- @1010 (79-80-78): 'tout [80] [78]'. Pronoun+verb ("tout [verb]") vs
  adverb+adjective ("tout [adj]") both grammatical; 78's value is open
  (ver-78 LEAD, not granted). FENCED: needs 78.
- @1089 (79-80-06): same 5-gram '00-33-79-80-06' as @468, but 06's follower
  is 43 (open). The "entre" rival (06-43 = "ent"+"re", 80 as finite verb:
  "tout [80] entre [07]...") cannot be excluded while 43 is open. FENCED:
  needs 43. (If 43 resolves against 're', @1089 joins @468.)
- 29-80 x2 (@1321, @1595): "[X]er [80]" with no clause boundary; ungrammatical
  under finite-80 and infinitive-80 alike. TENSION, fenced (no forced rival).
  (@1031 fenced under 77 above; @1155 is the section-B contradiction.)
- 29-89 x4 (@112, @274, @780, @1392): same tension. @274 has a conditional
  noun rival ("[67=veut] dire [89-noun]", conditional on 33='dire' lead);
  the rest have no forced rival. TENSION, fenced. (@1376 is the section-B
  contradiction.)
- 52-windows (@1294/@1807 for 80; @284/@1081 for 89): 52's class is open
  (value52 report: est-arm fenced, no value). FENCED.
- 98-windows (@441/@768/@1662 for 80): 98 open. Not legs, no contradiction.
- @663 (50-80-03), @565-side windows: 50 open. Not legs.

### D. Corrections to A8's cited evidence (record, not grant-overwrite)

1. "post-'er' x4" (80) does not reproduce: zero windows have 80 followed by
   29 (adjacent or within +3). It double-counts the same four windows as
   "pre 29x4". Correction for the record.
2. "'tout [80]' x3 pronoun+verb re-read CONFIRMED" does not survive
   re-derivation: @468/@1089 re-parse as adjective-shaped (conditional on
   06='ent', which postdates A8); @1010 is ambiguous (fenced on 78). The
   re-read predates the 06='ent' battery verdict; under current standing
   values it is at best unconfirmed.
3. 89 "suc 48x3/84x2": under 48='e' (letter battery), 89->48 is "[89]e"
   (stem + letter), not a verb frame; 89->84 as "[verb]-on" inversion is
   strained (clause-initial inversion ungrammatical), and as "[89]on" one
   word is non-verb-89. Not verb-frame evidence as stated.

A8's conditional GRANT itself is not overturned (see clause 4; R16-001 already
moved its foundation). The 80-vs-89 DISTINCT grant is untouched by this
battery.

## Adverses answered

1. C3 windows (@515/@869) with 77 unknown: FENCED with cause (section C).
   They become indeterminate "ce [77=?] [80/89]" trigrams. They cannot serve
   as verb legs unfixed, and nothing is silently assumed. Note: under the
   section-A infinitive-slot finding, "ce [77] [80/89-infinitive]" would be
   ungrammatical, so these windows cannot be verb legs even if 77 later
   resolves to a clitic without a finiteness change -- flagged for R16-001's
   docket.
2. 80's determiner leg @1155: re-parse attempted, verb readings all fail;
   CONCEDED as a hard contradiction (section B). It stands as red-team-noted
   (R16-001); this battery confirms it on the repaired stream.
3. 89's class / val-89-mirror (queued separately): interaction noted, bar not
   duplicated. Inputs for val-89-mirror from this battery: (i) infinitive-slot
   legs @221/@985 (+@1497 weak) = verb-class evidence; (ii) @1376
   ("pour [86] [89-noun/adv]") = hard non-verb window; (iii) the resulting
   class conflict (infinitive vs noun) implicates the 67-sole-polyvalence law
   and belongs to red-team adjudication.

## Per-clause pass/fail

1. (a) >=2 verb legs per cell, 77 unfixed: PASS (80: @564, @672; 89: @221,
   @985, +@1497 weak; all 77-absent). (b) zero contradictions: FAIL (hard:
   @1155 for 80, @1376 for 89; conditional: @468 for 80). Clause: FAIL.
2. Kill (no verb leg survives unfixed): FAIL -- five infinitive-slot legs
   survive without any 77 assumption.
3. Else null: APPLIES.
4. Constraint: HONORED. A8's conditional grant is not overwritten (its cited
   frames are corrected/supplemented, the grant verdict stands). No standing
   red-team verdict is overturned: R16-001's demotion of 77='le' is coherent
   with these findings (the C3 condition is load-bearing and unmet unfixed);
   le-77's null is untouched (this battery does not promote 77).

## Verdict: NULL

Headline: 77-independent verb legs EXIST for both cells (infinitive-slot via
24-modal: 80 @564/@672, 89 @221/@985), so the frames do not fully collapse
without 77='le' -- but hard non-verb contradictions BLOCK independence
(@1155: 80=determiner, "pour [92]er [80] fois"; @1376: 89=noun/adverb,
"pour [86-inf] [89], on..."; plus @468 adjective-shaped for 80 conditional on
06='ent'). A8's condition (77='le') remains load-bearing for A8's cited
frames (C3 fenced unfixed; 'tout [80]' re-parsed; 29-frames tense), while the
new infinitive-slot legs do not need 77 at all.

Escalation to red team: 80 shows infinitive-slot verb-class AND determiner
(@1155) AND adjective (@468, conditional) windows; 89 shows infinitive-slot
verb-class AND noun/adverb (@1376) windows. Under the 67-sole-polyvalence
law this class conflict needs red-team adjudication -- battery level cannot
declare polyvalence or retract A8's conditional grant. The infinitive (not
finite) shape of the surviving legs is also material to R16-001's docket:
"ce le [80/89]" would need finite verbs, which the surviving legs do not
support.

## Follow-up targets (null regenerates work)

1. **inf-80-89-ratify.** Re-derive the infinitive-slot legs once ne-24-profile
   is red-team-ratified (currently battery-grade, load-bearing for all five
   legs). Bar: iff 24=modal ratified, @564/@672 promote 80 and @221/@985
   promote 89 to infinitive-slot verb-class (value open); resolve @985's
   48-junction ("e[01]") and @1497's 59-junction inside the same pass.
2. **noun-89-1377-adjudicate.** Adjudicate @1376 ("pour [86-inf] [89-noun/adv],
   on...") against the infinitive legs. Bar: either produce a verb-89 parse
   of @1376 (killing the noun/adverb reading) or confirm the class conflict
   and escalate for polyvalence adjudication. Feed @1376 + @221/@985 into
   queued val-89-mirror; do not duplicate its bar.
3. **det-adj-80-adjudicate.** Adjudicate 80's non-verb windows (@1155
   determiner HARD; @468 adjective conditional on 06='ent'; @1089 gated on
   43) against the infinitive legs. Bar: confirm or fence each non-verb
   parse; if >=1 hard non-verb window stands with the infinitive legs,
   escalate for polyvalence adjudication (67-sole-polyvalence law).
