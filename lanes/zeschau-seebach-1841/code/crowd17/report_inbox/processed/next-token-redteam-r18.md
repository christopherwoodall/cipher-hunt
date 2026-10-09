# Round-18 red-team adjudication: next-token battery verdicts

Adjudicator: red team, kill authority. Date: 2026-10-08.
Scope: 29 unprocessed battery promote verdicts in `code/crowd17/report_inbox/battery-*.md`
(i.e. every queue target with status=verdict/result=promote not adjudicated in rounds
15/16/17). Stream: repaired 1,847-pair parse. Prior rounds AUTHORITATIVE: round-15
(`code/crowd15/report_inbox/next-token-redteam.md`), round-16
(`report_inbox/processed/next-token-redteam.md`), round-17
(`code/crowd17/report_inbox/processed/next-token-redteam-r17.md`).

Method: (1) every battery's bar checked against its verdict; (2) load-bearing numbers
re-derived independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (all re-derivations below are the red team's
own; `canonical.py` never touched); (3) each promote attacked through its weakest leg
first — one reviewer reserved as a pure attacker for the round's riskiest grants;
(4) no battery verdict overwrites a standing red-team grading without new byte-level
evidence.

Ten review lanes ran in parallel (9 claim-family adjudicators + 1 pure attacker);
the undersigned is the sole conflict-resolver. Where the attacker and a family
reviewer disagreed, the final ruling below states the reconciliation.

Re-derived anchors (red team, repaired stream): 1,847 pairs / 96 types.

## A. Final rulings (adjudicator's own)

### R18-001: prof-65 — GRANT PROMOTE (65=noun, CLASS tier; CONDITIONAL; with corrections)
The family reviewer verified the bar's 3-frame minimum with independent re-derivations:
qui-relative head @1208 ("21 65 qui est 32" — verb-65 ungrammatical after "qui" at
kill grade), que-relative head @1253, post-finite-verb DO @812/@1383; verb-65 killed
independently; no window forces noun-65 false. Accepted corrections: @724 struck
("qui la pour [inf]" ungrammatical under both classes — fenced as anomaly); L4
downgraded to verb-elimination; L2/L3 marked non-discriminating; L5/L6 conditional
(98="vient" lead; 63=verb lead). The attacker's participle rival (65 as past
participle) is fenced as a recorded caveat: in "21 65 qui est 32" a participle 65
would lack a nominal head (21's value open), so it does not refute the class grant.
Conditional on 59="est" provisional (@1208's best leg). Registry: add
"65": ["noun","cls"]; value open.

### R18-002: split-86-amended-rule — GRANT FINDING (residual disposition); RULE-PROMOTE REJECTED
The family reviewer confirmed the substantive byte delta: both residuals (@553→59,
@889→06) take verb-valued followers (06="ent" granted R17-007; 59="est" provisional)
and are fenced with byte-level cause (singleton bigrams/trigrams, same-row conforming
neighbors, shared "00 86" context) rather than bare adverses. The attacker's
self-grading charge lands on the RULE: the amendment was constructed from the
falsifying data (V-life = "verb-valued followers" is near-tautological; 2 of its 6
members are the rescued violators; exceptionlessness guaranteed, not discovered).
Ruling: the FINDING (residual disposition) is GRANTED, conditional on 59/06; the
amended rule itself is RECORDED AS PROPOSAL, not promoted — it joins the §7 docket
with the positional-rule declaration (still HELD). Third-life candidacy ({59,06})
REJECTED. Re-audit hook: reseg-86-553-889.

### R18-003: inf-37-78-475 — GRANT (conditional unit/frame finding)
37-78 x4 @312/@414/@475/@1770 (re-derived); 78's followers in the four windows are
four distinct groups (45/49/74/62) — no fixed rightward bond; 78 word-final at W1
via the exclusive 24→37 frame (x2, byte-identical 84-24-37-78 @310/@473) + @475
control; no standing value forces 37/78 apart. The attacker's bar-calibration
warning is RECORDED: clause (b) passes by non-contradiction on open values, clause
(c) kills a position nobody holds, and the decisive leg is cited from unratified
w1-314-rebar. The grant is therefore a conditional FINDING, not a unit declaration;
it does not weaken the confirmed R16-005 78="ver" LEAD. Conditional on R17-009
24-class + 78="ver" LEAD.

### R18-004: noun26-1560-1733-fragment — GRANT (constructional, conditional)
New byte evidence: the @1733 parallel ("30 06 60 12 48" left-independent, no noun
crux) proves "30 06 60" is a fragment; applied to @1561, "pas" heads RIGHT of the
forced 26|30 boundary (26@1560 = noun under banked 11="la"). The attacker's
contradiction charge is ACKNOWLEDGED and resolved: R17-011's granted "'26 30' x4 =
[verb] pas" is RE-SCOPED to x3 (@655/@992/@1250), @1560 excluded — a revision of a
standing grading WITH new byte evidence, which the method permits. The
noun26-1560-pas residual is thereby RESOLVED ('pas' = head of the second pas-limb).
R17-020's positional-rule DECLARATION stays HELD under §7 (its pending condition
is now discharged, but declaring is red-team business). The battery's stale "06
contested" is corrected (06="ent" granted R17-007). The "ne [52]" / dual-spelling
"94 52" x3 vs "12 48 52" @1736 observation is consistent-with R17-018, conditional
on 52=verb. No registry value change.

### R18-005: le-par-distributional — GRANT (finding, conditional)
96 n=21 re-derived; 37-96 x1 @913 + 11-96 x1 @997; 77-96/47-96/87-96/45-96 all x0.
The @997 datum stands on banked 11="la" + promoted 96="par" with no rescue
(word-internal barred by §7 precedent; "là"/"la partie" rescues dead). The
attacker's prejudgment warning is LOGGED: the "systematic" label (n=2) must not be
read as adjudicating S5 — @913 is S5-conditional; @997 is S5-independent. If S5
falls, @997 stands alone as a banked-value contradiction for the red-team docket
(joins "la tout" @52-53). Registry: finding only.

### R18-006: le-qui-distributional — GRANT (finding, doubly conditional)
64 n=47 re-derived; 37-64 x3 @529/@1357/@1444 (S5-conditional) + 77-64 x1 @790
(conditional on provisional 77="le"); 8x "ce qui" grammatical controls; 11="la"
never precedes 64. Red-team warning: @790 cuts both ways — "le qui"
ungrammaticality is evidence AGAINST 77="le", parallel to s5-foundation's use
against 37="le". Logged as a potential adverse for the provisional 77="le" when
its promotion docket runs. Registry: finding only.

## B. Family rulings adopted without change

### R18-007: bound-ci-984-standalone — GRANT PROMOTE (frame tier, restricted, A11-conditional)
@983-986 = "45 01 24 89" parses as "ceci [24-modal] [89-inf]" on the strongest
standing stack (A11 HOLD + R17-009 + A8); ±10 sweep zero forced contradictions;
@195 leg stays fenced. Locus-restricted, explicitly conditioned — the thinness is
fenced into the scope. Wins the @984 triple-count against w3/disc (one value per
position; strongest legs). Registry: frame record only (no 01 value cell).

### R18-008: disc-01-24-ci-X — REJECT promote; GRANT LEAD + FINDINGS
The "unique survivor" proof for 24="faire" is broken: the "laisser" kill requires
41="se", which the same battery rejects globally — under its own 41=nominal
premise, "laisser" survives W1/W2/W3 and the infinitive windows. Survivor set is
{faire, laisser}. Granted instead: LEAD — 24="faire" value-candidate (conditional
on R17-009; rival "laisser" live); LEAD — 01="en" local to @40/@828 only; FINDINGS
— byte-verified profile corrections (11-24 x3, 24-82-16 x3, contact census).
Registry: _meta notes only.

### R18-009: w3-01-adjudicate — REJECT promote; 01@984="en" FENCED as adjudicated loser
The discriminator tested the wrong rival (post-nominal "-ci" instead of the live
ceci-composition, which needs zero extra assumptions beyond R2 and loads on granted
R17-009); R2 leaves 78@982 dangling (clause 1 fails on the bar's own terms); naming
01@984="en" destroys the R17-015-fenced 45-01 "ceci" frame while claiming to
preserve it. Per the battery's own bar language the loser is fenced. The attacker
independently concurred. Registry: no change.

### R18-010: clitic-44-65-discriminator — GRANT (value tier, WINDOW-LOCAL @1714; conditional)
65's 25-window contact census (re-derived exact): copular/subject frame for "l'"
(@1208 "21 65 qui est 32" + @724/@1340 qui-relative heads); "en" fenced (no
de-complement/partitive contact; the 83-near-65 contacts attach rightward).
New byte evidence over the pronoun-44-1714 null (@1208's copular content). The
"l'" antecedent is unfound — fenced as discourse-anaphoric per the bar. Conditional
on 59="est" provisional + 94="ne" STRONG LEAD + 65 noun-class. 44 NOT promoted
globally — the verdict is fenced to @1714. Registry: no change (44's cell stays
absent).

### R18-011: stem-44-1839 — GRANT (frame tier, instance-scoped; conditional)
44@1839 decided whole-word nominal head ("[44] de [21] et [78-word]"; parallel
@1617-1619 "42 44 11 84" with 11="la" banked); stem excluded (no 42-affix nameable;
elision excluded — 44 consonant-initial; rightward "44[83]" blocked by conditioned
83="de" lead); "42 44" = two-token adjacency. Battery's stale @1070 citation
corrected (gender-44 re-analyzed it as word-internal "préalable"); verdict
unaffected. Consistent with the §7-untouched poly-44 dockets. Registry: no change.

### R18-012: profile-29-left — GRANT (finding); the @146 un-fence is KILLED
45/45 census re-derived byte-exact. Word-initial 29 demonstrated on 3 genuine
windows with allowed values only: @291/@685 "64 29 40" = "qui erre" (64="qui"
promoted, 29-40="erre" per the "ière" convention + ground-truth "première" @758);
@500 "47 11 29 40" = "cela erre" (47="ce" + 11="la" composition forced). The
battery's other 7 positives struck (@147 double-consumes granted 87="ce"; @689
loads on ungranted 94; @1230 misclassified). The @146 un-fence FAILS: lon-29-146's
five failures are independent of the word-initial question — @146 stays fenced R3.
R17-014 anchors numerically identical. Registry: no change (29 stays ["er","gt"]).

### R18-013: fence-84-29-gate — GRANT (evidence package; NOT a value promotion)
Full 25-census re-derived byte-exact; 84→29 x1 @146 confirmed as the unique
"on"-resisting successor; grading honest (CLEAN 5 / NO-CONTRADICTION 17 / FENCED 3);
§7 clean. Declares nothing about 29's value. Supports A15. Registry: no change.

### R18-014: dict-313-w1-adjudicate — GRANT (fork-window adjudication)
W1 "ce qui" wins on a corrected 2-vs-3 assumption count (the battery's 1-vs-2
overstated: the CE parse's 37-78-infinitive leg consumes the ungranted 78="ver"
LEAD structurally). Installs 45="ce" at @314 — NOT 45="dict". A11 HOLD
strengthened; R16-004/R16-005 untouched.

### R18-015: w1-314-rebar — GRANT (conditional structural finding)
Valid conditional reductio under the rival's own values (78="ver" + 45="dict" →
"X-verdict" ungrammatical as modal-24 complement; bare-37 excluded
distributionally). Clause (c) corrected: CE parse assumptions = {78="ver" LEAD
(structural), 59="est" provisional}. Installs 45="ce" at @314 (conditional),
consistent with R16-004's "ce" arm. The rpos-w1-exception promote leans on this
finding with the same conditionality recorded.

### R18-016: qui37-rival-values — GRANT (ranking only)
Ranking verb > adjective > "le" > stem (excluded, p=0.0219 re-derived exact) >
noun; verb margin conditional on open 45/01 (stated honestly). A1 not decided;
no polyvalence declared; no value named for 37.

### R18-017: qui-2326-prefix — GRANT (frame level)
24-87-64-23/26-37 formula frames (@181, @1768): 24=modal (R17-009) + clause
boundary; "ce qui [23/26] [37]" verb-position; 23's value stays open
(parallelism-inferred slot). One wording correction: "A1 predicative grant" → HOLD.

### R18-018: spell-pasent-test — GRANT (kill-grade)
The battery KILLED the "pasent"-for-"passent" spelling disjunct (0 independent
supporting instances over the 44-window 06 census; "prenent" @1118 correctly
excluded as circular). "30 06" x4 hardened as genuine residuals. No collision
with 06="ent"/30="pas". Compatible with the queued ne-06-polyvalence docket.
Registry: finding only.

### R18-019: en85-gerund-reaudit — REJECT
Fatal: the bar required "banked values only" but every gerund confirmation loads
on 24="en" — never granted (A3 granted the @952 frame, not a 24 value; the
battery's "A3 ground truth 24=en" overstates the record). Worse, the four
"confirmed" windows are the same windows standing-granted as 24=finite-verb +
85=infinitive stem (R17-009) — an undeclared overwrite attempt without new byte
evidence. R17-009 stands. Valid sub-findings banked: 24-85 x5 count exact; @1439's
16 verb-shaped via m'-clitic entailment (82="m" GT); @733 fenced.

### R18-020: lever-absolute-era-gate — GRANT (gate claim, caveated)
Independently verified: Littré "lever" v.a. (transitive); three "Absolument" marks
exactly as cited (senses 2, 11 "a vieilli", 12); "rise/get up" senses all under
"Se lever, v. réfl."; Old French absolute disclosed as diachronically dead. Caveats:
no corpus-frequency count run (bar's clause (a) letter not fully executed); Acad.
6e (1835) not fetched. Neither overturns the unanimous authority record. Registry:
era finding only.

### R18-021: ne-follower-verbless-sweep — GRANT (finding)
9/28 attachable/un-attachable census reproduced exactly (R17-001's census — no
drift); @509 not sole verb-less 94; 94-64 stream-unique @509 ("ne qui"
kill-grade ungrammatical); @508 re-framed as non-particle re-segmentation
candidate (hypothesis only). R17-022 untouched (no conditioned 62="on"); R17-001
untouched; §7 clean. Registry: no change (94 stays ["ne","lead"]).

### R18-022: verb-92-subset — GRANT PROMOTE (92=verb, CLASS tier, subset-scoped, conditional)
8/8 subset windows parse with zero new forced contradictions (@1154
"pour [92]er [80] fois" the smoking gun, loading only on granted 00 + banked 29);
stem-vs-whole tension is the R17-018 duality, fenced to seg-92-354-356; @66
conditional on 94="ne" lead; subset pre-registered (no cherry-pick); prenne-92-noun
KILL confirmed. 92's global class stays HELD pending the §7 split question.
Registry: add "92": ["verb","cls"] with subset-scope note.

### R18-023: frame-share-60-68 — GRANT LEAD (census fact)
Shared free frames re-derived byte-exact (successor 06 x1/x1 @1474/@1719;
predecessor 21 x4/x1; no shared centered trigram; formula exclusions verified).
Explicitly NOT a homophone/interchangeability claim — the standing
pair-60-68-readjudicate kill and thirds-60-68-pair null are undisturbed. Registry:
_meta note only.

### R18-024: singleton-68-predecessors — GRANT (finding; negative determination)
16 controls re-derived as the exhaustive n∈[6,10] pool minus 68 (no cherry-pick);
68's all-disjoint predecessor profile (M1=1.0) is typical of thin cells, not
anomalous. Premise corrections recorded (68 n=8; pred-21 @1787/@1788 shared).
No value claim about 68. Registry: no change.

### R18-025: lela-37-51-1655 — GRANT (window-disposition)
Both 37-11 windows fenced as genuine S5-straining residuals with stated cause
(@51: article-article adjacency, all named-trigger boundary rescues dead; @1655:
robust under both 24 readings, boundary trigger downstream). Promotes no value,
kills nothing, does NOT decide S5, does NOT preempt the "la tout" docket.
Registry: no change.

### R18-026: rpos-w1-exception — GRANT (evidence package + §7-docket candidate)
W1 re-derived; 78@313 word-final; unconditioned R-pos falsified at W1
(78→45 with 45="ce" under A11 HOLD). Refined rule candidate (45="dict" iff 78
word-MEDIAL) stated with W1–W4 classified; W2 leg conditional on R16-005. No
declaration — evidence for the §7 positional-rule decision only. R16-004
preserved. Registry: no change.

### R18-027: class-36-profile — GRANT PROMOTE (36=NOUN, CLASS tier)
Nine windows re-derived exact. Elimination sound: "par ce [36]" @1215 forces
nominal (45="ce" via A11-hold, 96="par" promoted; "ce"+bare infinitive
impossible); "pour [36-ADJ]" x3 ungrammatical as adjective; "est [36]" legs
honestly marked provisional-59-dependent (not needed). Infinitive and adjective
excluded as single-class readings. Registry: add "36": ["noun","cls"].

### R18-028: frame-74-45-93 — GRANT (frame level)
45→93 x3 @261/@477/@602 re-derived; all parse as governor + "ce" + nominal head
(74/74/96 governors — never 78, so "ce" not "dict" per R16-004); 93 determiner-
governed at all three windows (noun-shaped here); the bar-(b) tripwire does not
fire — A11 HOLD untouched. Corrections: battery's "Index 9" → 10; the false
"77-governed 93" support struck (77-93 x0). Registry: frame record only.

### R18-029: adj-frame-995-solo — GRANT (frame level)
"03 60 67" @994-996 parses as "[03-N][60-adj] et[67] la[11]" — 03 nominal
independently supported (47-03 x2 granted-47; 77-03; 03-64 x4; 30-03 x3);
67="et" per the sole-polyvalence positional rule (67-11 x4 re-derived). The
60-as-verb rival fails ("pas 03 60" ungrammatical as clause); compatible with
le-par (11="la" confirmed). 60's global class reserved to poly-60-redteam.
Registry: frame record only.

## C. Battery corrections accepted into the record

- dict-313 assumption count 1-vs-2 → 2-vs-3 (R18-014).
- w1-314-rebar clause (c) → assumptions {78="ver" LEAD, 59="est" provisional} (R18-015).
- split-86 fence arithmetic 11/12 → 10/12 under original rule; "shared pred empty" superseded by 21 @1787/@1788 (R18-002/R18-023).
- 68 n=7 → 8; predecessor set corrected (R18-024).
- le-par battery's "64 precedes 96 x3" → x1 @342 (R18-005).
- frame-74-45-93: "Index 9" → 10; strike false "77-governed 93" support (R18-028).
- prof-65: @724 struck from L1; L4 → elimination-only; L2/L3 non-discriminating (R18-001).
- profile-29-left: 10 positives → 3 (@291/@685/@500); @147/@689/@1230 struck (R18-012).
- verbless-sweep span-ladder typo: 16/37, not 18 listed (R18-021).
- fragment battery's stale "06 contested" → 06="ent" granted R17-007 (R18-004).
- stem-44 battery's stale @1070 citation → gender-44's "préalable" re-analysis (R18-011).
- qui-2326-prefix wording: "A1 predicative grant" → HOLD (R18-017).

## D. Scoreboard delta (round 18)

Promotes granted (22): R18-001 (65=noun class), R18-002 (86 residual disposition
finding), R18-003 (37-78 conditional unit/frame), R18-004 (noun26 fragment
constructional), R18-005/R18-006 (le-par / le-qui calibration findings),
R18-007 (ceci @983-986 restricted frame), R18-010 (44="l'" @1714 window-local),
R18-011 (44@1839 whole-word segmentation), R18-012 (29 word-initial finding),
R18-013 (84-successor census), R18-014 (W1 "ce qui" adjudication), R18-015
(W1 conditional structural), R18-016 (37 value-race ranking), R18-017
(24-87-64 formula frames), R18-018 (pasent-spelling kill), R18-020 (lever era
gate), R18-021 (94 verbless-family census), R18-022 (92=verb class, subset),
R18-024 (68-predecessor typicality), R18-025 (37-11 disposition), R18-026
(rpos refined-rule candidate), R18-027 (36=NOUN class), R18-028 (45→93 frame),
R18-029 (@995 postnominal frame).
Leads granted (3): 24="faire" value-candidate (rival "laisser" live), 01="en"
local @40/@828, 60~68 shared free frames (census fact).
Promotes rejected (4): disc-01-24-ci-X (salvaged as leads+findings),
w3-01-adjudicate (01@984="en" fenced as loser), en85-gerund-reaudit (R17-009
overwrite attempt), frame-97-profile (INF/N underdetermined).
Registry cell additions: 65→["noun","cls"], 92→["verb","cls"] (subset-scoped),
36→["noun","cls"].
Standing revisions with new byte evidence: R17-011 "'26 30' [verb] pas" re-scoped
x4→x3 (@1560 excluded). Killed: @146 un-fence attempt (@147 parse invalid).
Docket notes (not resolved): @997 "la par" joins "la tout" @52-53 as a
banked-value contradiction; @790 as potential adverse for provisional 77="le";
the 86 amended rule and 26 positional rule declarations remain HELD under §7.

## Battery verdicts overturned (with cause)

1. disc-01-24-ci-X "promote" → REJECTED (R18-008). Cause: uniqueness proof broken
   (laisser survives on the battery's own premises); conditional convergence is
   lead-grade per R16-001.
2. w3-01-adjudicate "promote" → REJECTED (R18-009). Cause: wrong rival tested;
   clause-1 failure on the bar's own dangling-token terms; destroys the
   R17-015-fenced 45-01 ceci frame.
3. en85-gerund-reaudit "promote" → REJECTED (R18-019). Cause: undeclared overwrite
   of standing R17-009 on identical windows; bar violated ("banked values only").
4. frame-97-profile "promote" → REJECTED (R18-023). Cause: INF/N tie at the R17
   class-promote standard (rival not killed at kill grade).
5. split-86-amended-rule "promote" (of the rule) → DOWNGRADED to finding (R18-002).
   Cause: self-grading bar; the amendment was constructed from its exceptions.
6. R17-011 "'26 30' x4 [verb] pas" → RE-SCOPED x4→x3 (R18-004). Cause: new byte
   evidence (@1733 parallel) — permitted revision.
