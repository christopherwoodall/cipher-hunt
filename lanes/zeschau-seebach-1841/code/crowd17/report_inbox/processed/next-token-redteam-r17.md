# Round-17 red-team adjudication: next-token battery verdicts

Adjudicator: red team, kill authority. Date: 2026-10-08.
Scope: 20 battery reports in `code/crowd17/report_inbox/processed/battery-*.md`
plus 5 in `report_inbox/processed/battery-*.md` (ne-94, n-e-12-48, dire-33,
le-77, lon-ne-77-62-94). Stream: repaired 1,847-pair parse.
Prior rounds are AUTHORITATIVE: round-15
(`code/crowd15/report_inbox/next-token-redteam.md`, A1-A16, P1) and round-16
(`report_inbox/processed/next-token-redteam.md`, R16-001-R16-032).

Method: (1) every battery's bar checked against its verdict; (2) load-bearing
numbers re-derived independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (all re-derivations below are the
red team's own); (3) each promote attacked through its weakest leg first;
(4) no battery verdict overwrites a standing red-team grading without new
byte-level evidence.

Re-derived anchors (red team, repaired stream): 1,847 pairs / 96 types.
94-59 x3 @558/@762/@1795. 94-59-30 x1 @558 ("86 94 59 30 67 11").
12-48 x5 @169/@709/@809/@1075/@1736. 94-82-06-06 x2 @578/@1182
("61 94 82 06 06 50"). 06-70-12-94 x1 @346 ("87 01 06 70 12 94 74").
78: n=31, det-pred 16/31, pred-33 0/31. 29: n=45, det-pred 2/45, pred-33 5/45.
OR = 22.93. 62->94 x9 @100/@508/@761/@840/@1329/@1362/@1686/@1704/@1772.
84->59 x4 @1189/@1290/@1447/@1803. 62->59 x0, 84->94 x0. 77-84 x7
@145/@259/@1057/@1446/@1484/@1763/@1802. 01-24 x3 @40/@828/@984.
26-30 x4 @655/@992/@1250/@1560. 87-78-45 @573 ("52 87 78 45 13 55").
42-94-59-37 @1794-1797 ("56 42 94 59 37 91"). 34-29-40-12-94 x1 @61.
70-12-94 x2 @347/@1547. 24-87 x10. 32 n=13.

## A. Battery promotes

**R17-001: 94="ne" promote — REJECT; R16-006 CONFIRMED (STRONG LEAD).**
The battery re-derives real frames (94-59 x3, 94-82 x4, 62-94 x9, 70-12-94
x2; 37-window scan, zero hard contradictions). But it presents no new byte
evidence beyond what R16-006 weighed. R16-006 declined the promote on the
record: three conditional legs converging + one independent-strained leg =
STRONG LEAD, not promotion, under the R16-001 standard (conditional
convergence is lead-grade). The n'est legs load on provisional 59; the
62-94 legs load on 62; the prenne legs load on 12; the ne-me legs are
strained (doubled 06, verbless "ne me que"). Nothing overturns R16-006.
94="ne" stays STRONG LEAD. All downstream verdicts conditional on 94 keep
their stated caveats.

**R17-002: 12="n" — GRANT PROMOTE (letter tier).**
Three pencil-anchored frame types: 40-12 "en" @64 (40="e" GT), 12-34 "ni"
@1740 (34="i" GT), 70-12 "pren" @347/@1118/@1547 (70="pre" GT). Zero
contradictions in the 23-window census. Upgrades R16-010 LEAD. The
12-48 x5 correction (not x7) is accepted and recorded.

**R17-003: 48="e" — GRANT PROMOTE (letter tier).**
The letter reading is demonstrated across the 38-window sweep:
"ne" x5 (12-48), "me la" @126 (82="m" GT), feminine/mute-"e" x5
(@283/@450/@1212/@1779/@1177), "[89]-e" verb+ending x3 (@641/@872/@987).
R16-007's decline is overtaken by this evidence. Caveat: the battery's
"me" x4 includes @1229 (stem-required, see R17-024) and two doubtful
windows — the grant rests on the sweep, not on that count. 48="e" is the
general value; the A7-L2 verb-stem frame is narrowed to its exclusive
legs (R17-024). No second polyvalence: the frame is conditioned, not a
second value.

**R17-004: 30="pas" — GRANT PROMOTE (conditional).**
Bar met: @558 "n'est pas" canonical (re-derived "86 94 59 30 67 11"),
@1713 "ne [44] est pas", two more independent ne-frames (@651, @1363),
19/19 windows with zero forced contradictions. The @1702 'n'importe'
rival is fenced to ne-30-1700 with stated cause. Conditional on 94="ne"
STRONG LEAD (R17-001) and 59="est" provisional. Upgrades R16-009 LEAD.

**R17-005: 39="/a/" — GRANT LEAD (allophone tier).**
Upgrades R16-011 HYPOTHESIS. Three /a/ frames: "91 [39] 64" @37,
"59 [39]" @764 and @1512. Correction to the battery: "a qui" is NOT
ungrammatical — "a qui" is good French — so window #1 does not pick "a"
over "a". The claim survives as the /a/ PHONEME (one phoneme; "a" vs "a"
is not cipher-testable), realized as "a"/"a"/word-internal 'a', per the
47="ce" allophone-tier precedent. Not full PROMOTE: two of three clean
frames lean on provisional 59. Zero forced contradictions; frequency band
fits a single letter.

**R17-006: 78="ver" — REJECT promote; R16-005 CONFIRMED (LEAD).**
The ver-78-rebar battery correctly NULLed: promoting would contradict the
standing R16-005 LEAD grading. The re-bar is verified (7/7 'ce [78]'
re-derived at the exact R16-005 offsets; OR=22.93 re-derived; @296 fenced
as residual), but it adds no unconditional positive leg. The two 'verdict'
reads (@573, @982) load on the 45="dict" lead (R16-004), ungranted.
Settle condition for a future promote: 45="dict" resolved, or a new
positive leg on banked/granted values. The NULL is ratified as correct
battery discipline.

**R17-007: 06="ent" — GRANT PROMOTE (conditional).**
"ne mentent" x2 @578/@1182 (re-derived "61 94 82 06 06 50" and the
@1182 repeat; 82="m" GT), "entreprenne" @346 (re-derived
"87 01 06 70 12 94 74"). The -ment adverb fork has zero clean windows;
verb stems take 06 (80 x2, "ment-" x2). "-ment" = 82+06 compositional.
Upgrades R16-012 LEAD. Conditional on 94="ne" STRONG LEAD. The battery's
queue corrections are accepted: "prennent" (70-12-06) refuted as stated;
"concernent" unverified; 06->77 recount x7 (not x6).

**R17-008: 32 = one verb lexeme — GRANT PROMOTE (class level).**
All 13 windows parse under one lexeme: finite 3sg (@33 "qui 32", @855
"qui [32]e"; 6/13 strong), past participle (@317/@449/@1211 "est [32](e)";
@130/@532/@1176/@1283/@1572 participle-modifier/passive). The participle
analysis dissolves the adjective/verb tension with no second lexeme and
no polyvalence. Value unnamed — class-level grant, lane-precedented
(31=VERBAL). Consistent with the granted 37/32/42 predicative frames.

**R17-009: 24 = finite verb, modal-shaped — GRANT PROMOTE (class level).**
Six subordinate finite slots ("que 24" x3 @547/@955/@1693; "qu'on 24" x2
@311/@474; "que l'on 24" x1 @1486), infinitive-taking complements
(24->85 x5, 24->89 x3, 24->80 x2), postverbal "pas" x3. The preposition
arm is KILLED at kill grade: eight windows ungrammatical as preposition
("que"/"on"/"ne" + preposition). Value ("peut"/"sait"/"doit") unnamed —
class-level grant.

**R17-010: 59 "n'est" frames — GRANT PROMOTE (frame level, conditional).**
@1795 "[42] n'est [37]" clean copular (re-derived "56 42 94 59 37 91";
A1-predicative 37); @762 "[62] n'est a [88]" predicative-PP (soft leg,
88 open); @558 fenced as the ne...pas negation frame (30="pas"
promoted). Promotes the FRAMES, not the 59="est" value (stays
provisional). Conditional on A1 surviving frame-37-reexam.

**R17-011: noun-26 — frame claims GRANTED; unconditioned value REJECTED.**
GRANT: '26 30' x4 = "[verb] pas" (@655/@992/@1250/@1560 re-derived);
26 = verb in the 'en ce qui' formula slot (triple uniformity, see
battery). REJECT: 26=verb-class unconditioned — three windows (@129,
@240, @1560) force noun under banked 11="la". The positional rule (noun
in '11 (02)? 26', verb elsewhere) is recorded as a GRANTED FINDING but
its declaration as polyvalence is HELD (R17-020).

**R17-012: nest-subject-86-62-42 — GRANT PROMOTE (frame level).**
The three X-94-59 trigrams (@558, @762, @1795 — the stream's only three)
each take a subject parse with zero forced contradiction: 86
(substantivized infinitive/noun; 'le 86' x5), 62 ("il n'est a...",
under the demonstrated 'il' rival), 42 ("[42] n'est [37]"). Conditional
on provisional 59="est". No standing verdict contradicted.

**R17-013: prenne-subject-S1545 — GRANT (finding).**
The bar resolved via its second disjunct: the clause is genuinely
subjectless with stated cause (slot empty pair-adjacent @1546/@1547;
'pour que' + subjunctive mandates an overt subject; the '00 46' control
shows the slot normally filled). This is a finding, not a value promote.
It strengthens the prenne-70-12-94 fence; the 12/94 duality keeps its
statuses.

## B. Battery kills

**R17-014: 78="er" — KILL CONFIRMED (R16-005 stands).**
Re-derived: 78 16/31 det-pred vs 29 2/45; 78 0/31 pred-33 vs 29 5/45;
OR = 22.93. @296 stays the fenced 1-window residual.

**R17-015: 01="ci" and 01="faisant" — KILL CONFIRMED (general values).**
'01 24' x3 @40/@828/@984: "ci" before the granted finite verb 24 is
ungrammatical (W1, W2 force 'ci' false); "faisant" + finite verb with no
subject is ungrammatical (W1, W2, W3 force 'faisant' false). Load-bearing
on R17-009 (24=finite verb); if that grant ever falls, re-open. NOT
killed: "-ci" as a BOUND morpheme in "ceci" (87-01 x2, 47-01, 45-01);
word-internal 37-01 readings. A12's 37-01 unit grant untouched.

**R17-016: "enne" one-word composition — KILL CONFIRMED.**
34-29-40-12-94 occurs once (@61); the forced letter string "ierenne"
admits no French word (family sweep verified in method). The kill is
scoped to the composition only: 94="ne" and 12="n" are NOT downgraded.

**R17-017: 62="on" unconditioned — KILL CONFIRMED.**
62->94 x9 vs 84->59 x4, zero crossover (re-derived). Against the A15
84="on" grant, §7 (67 sole polyvalence) forbids a second unconditioned
"on". 62="il" stays demonstrated-not-promoted.

**R17-025: ne-06-317-gate — KILL CONFIRMED (gate closed).**
Naming 06 did not resolve the @317 hapax: all three readings fail at kill
grade ("ne ent la", "n'ent" not a word, no adverb stem). @317 stays a
fenced residual.

## C. Escalations

**R17-018: 12/94 "ne" duality — FENCED as compatible mechanism.**
The analytic (12-48) vs syllabic (94) spellings of "ne" are the
homophonic cipher's ordinary mechanism, not a contradiction. Neither
12="n" (R17-002) nor 94="ne" (R17-001) is downgraded. The subjectless
@1545 (R17-013) is a genuine fenced residual.

**R17-019: frame-37-reexam scope — A1 STANDS on 6 windows.**
A1 granted 59->37 x6 (@528/@624/@912/@1178/@1443/@1796). The "7th window"
claim is corrected to 6; no window is added or removed. The est-finder
VOID claim does not overturn A1 without kill-grade evidence against
these six.

**R17-020: noun-26 positional rule — GRANTED as finding; declaration HELD.**
The rule (noun in '11 (02)? 26' @129/@240/@1560; verb-class elsewhere,
14 windows) accounts for 16/17 windows cleanly. Declaring it would be the
lane's second polyvalence (§7: 67 only). HELD pending noun26-1560-pas
(the @1560 'pas' residual). §7 is not violated by a finding.

**R17-021: ver-78-rebar vs R16-005 — R16-005 CONFIRMED.**
The battery's NULL was correct discipline. 78="ver" stays LEAD.

**R17-022: lon-ne-77-62-94 vs collision kill — COLLISION KILL CONFIRMED.**
@508 reads "l'on ne" cleanly at trigram level, but installing a
conditioned 62="on" there would be a second polyvalence. REJECTED under
§7. @508 is FENCED as a 1-window residual (like @296). The 'ne qui'
right edge (@509-@510, singleton) is an independent fenced anomaly.

## D. 77="le"

**R17-023: 77="le" stays PROVISIONAL UNCONDITIONED.**
No new evidence. battery-le-77 NULLed (no clean re-parse of the adverse
windows). R16-001 stands in full. The promotion docket is unchanged:
76-noun battery + 80/89-verb battery must resolve favorably, then two of
@832/@516/@870/@1042 upgrade to clean legs.

## E. Scope ruling

**R17-024: A7-L2 NARROWED to its exclusive legs.**
The A7-L2 "48 = verb-stem candidate" frame (round-15 grant) is in tension
with the granted 48="e" letter value (R17-003). The 38-window sweep shows
exactly two windows require the stem (@1229, @1589: "[48]er ce",
ungrammatical under 48="e") while fourteen require the letter. The frame
is NARROWED to @1229/@1589 as a conditioned frame — lane-precedented
(allophony/conditioned frames, cf. 47/87). It is not a second polyvalence.
The general value of 48 is "e".

## Battery corrections accepted into the record

- 12-48 x5 (not x7): both batteries agree; the finder overcount is corrected.
- 06->77 x7 (not x6): ent-06 recount accepted.
- "prennent" (70-12-06) refuted as stated; "concernent" unverified.
- 94-24-87 @161/@1773 (battery said @162/@1774; same frames).
- @508 anchor (62's offset; was @507 in queue evidence).

## Scoreboard delta (round 17)

Promotions granted: 12="n" (letter), 48="e" (letter), 30="pas"
(conditional), 06="ent" (conditional), 32=verb-lexeme (class),
24=finite-verb (class), 59-frames (frame), nest-subject (frame),
noun26 frames (frame-level x2). Leads granted: 39="/a/" (allophone).
Findings granted: prenne-subjectless, noun-26 positional rule (held
from declaration), 12/94 duality (compatible).
Promotes rejected: 94="ne" (stays STRONG LEAD), 78="ver" (stays LEAD),
26=verb-class unconditioned.
Kills confirmed: 78="er", 01="ci", 01="faisant", "enne"-word,
62="on" (unconditioned), ne-06-317 gate.
Scopes narrowed: A7-L2 to @1229/@1589.
77="le": provisional unconditioned (unchanged).

## Updated promotion list (post-R17)

Ground truth (pencil): 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
Banked/granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
47="ce" (allophone), 84="on" (conditional, weakened).
Newly promoted: 12="n" (letter), 48="e" (letter), 30="pas",
06="ent", 32=verb-lexeme (class), 24=finite-verb (class).
Frame-level: 59 "n'est" frames, nest-subject-86-62-42, noun26
"[verb] pas" x4, noun26 'en ce qui' slot.
Leads: 94="ne" (strong), 78="ver", 39="/a/" (allophone), 33="dire",
45="ce/dict", 73="lu", 20/43/81 noun leads, 65 (queued).
Provisional: 59="est", 77="le" (unconditioned).
Killed: 78="er", 84="fait", 01="ci", 01="faisant", "enne"-word,
62="on" (unconditioned), ne-06-317 gate claim.
Held: 37/42 predicative frames, 45="ce", 26 positional rule
(declaration), 76 gender, 83 value, 92 class.

## Battery verdicts overturned (with cause)

1. ne-94 "promote" → REJECTED (R17-001). Cause: no new byte evidence
   beyond R16-006; legs remain conditional; R16-001 standard binds.
2. ver-78-rebar implicit promote → DECLINED (R17-006). Cause: would
   contradict R16-005; no unconditional positive leg; the battery itself
   correctly NULLed.
3. noun26 unconditioned verb-class → REJECTED (R17-011). Cause: three
   windows force noun under banked 11="la".
4. lon-ne-77-62-94 conditioned 62="on" → REJECTED (R17-022). Cause:
   second polyvalence barred by §7.
5. 48="e" decline (R16-007) → OVERTURNED (R17-003). Cause: new
   38-window sweep evidence; R16-007's "no independent legs" no longer
   holds.
6. 39 HYPOTHESIS (R16-011) → upgraded to LEAD (R17-005). Cause: three
   /a/ frames with zero forced contradictions (with the "a qui"
   French correction noted).
