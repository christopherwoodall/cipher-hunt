# Round-20 red-team adjudication: next-token battery verdicts

Adjudicator: red-team coordinator (sole conflict-resolver). Date: 2026-10-09.
Scope: 108 unruled battery promotes (every queue target with
status=verdict/result=promote not adjudicated in R15–R19) + 28
priority-1 RED-TEAM DECISION targets. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`;
`canonical.py` never touched). Prior rounds AUTHORITATIVE: R15
(`code/crowd15/report_inbox/next-token-redteam.md`), R16
(`report_inbox/processed/next-token-redteam.md`), R17
(`code/crowd17/report_inbox/processed/next-token-redteam-r17.md`), R18
(`code/crowd17/report_inbox/processed/next-token-redteam-r18.md`), R19
(`code/crowd17/report_inbox/processed/next-token-redteam-r19.md`).

Method: (1) every battery's bar checked against its verdict; (2) load-bearing
numbers re-derived independently from the repaired stream (all re-derivations
are the adjudicators' own, fresh Python, no verifier code imported);
(3) each promote attacked through its weakest leg first — one lane reserved
as a pure attacker for the round's riskiest grants, plus a follow-up
attack-recovery on formula-76-49-24; (4) no standing red-team grading
overwritten without NEW byte-level evidence (revisions with new evidence are
marked as such).

Thirteen lanes ran in parallel (11 claim-family adjudicators + 1 pure
attacker + 1 attack-recovery); the undersigned is the sole
conflict-resolver. Where the attacker and a family adjudicator disagreed,
the final ruling below states the reconciliation and the winning evidence.

Re-derived anchors (coordinator): 1,847 pairs / 96 types.

Standing revisions this round: exactly ONE — R20-116 lifts the @889
clause-boundary fence (new byte evidence: the one-word "pourvoient" parse).
Every other standing R15–R19 grading is confirmed, none overwritten.

Coordinator override: FAM-G's formula-76-49-24 GRANT is overridden to FENCE
(see R20-080): the attack-recovery proved the N-ADJ-Vfin license vacuous
after adj-49-420-366 killed adjective-49 at kill grade.

## A. Final rulings

### FAM-A: core value batteries (R20-001–019)

Fourteen of nineteen are byte-identical re-filings of already-ruled
reports — marked DUPLICATE with the earlier ruling, not re-adjudicated.
Five are new.

### R20-001: fois-17 — DUPLICATE (standing: 17="fois" PROMOTED)
R17 banks 17="fois". No new byte evidence. Registry: none.

### R20-002: cela-87-11 — DUPLICATE (R15-P1 PROMOTE CONFIRMED, compositional)
R15-P1: "cela"=87+11. 87=["ce","prom"]. Registry: none.

### R20-003: on-84 — DUPLICATE (R15-A15 GRANT-WITH-CONDITIONS, weakened by R16-002)
84=["on","prom"], conditional. Registry: none.

### R20-004: ce-47 — DUPLICATE (R15-A4 GRANT, allophone tier)
47=["ce","prom"]. Registry: none.

### R20-005: tout-79 — DUPLICATE (R15-A5 GRANT)
79=["tout","prom"]. Registry: none.

### R20-006: pour-00 — DUPLICATE (R15-A9 GRANT, leg-(1) downgrade)
00=["pour","prom"]. Registry: none.

### R20-007: ne-94 — DUPLICATE (R17-001 REJECT promote; 94="ne" STRONG LEAD)
Confirmed by R19-167. 94=["ne","lead"]. FLAG: the queue's "promote" verdict
is battery-level only; not ratified. Registry: none.

### R20-008: n-e-12-48 — DUPLICATE (R17-002 + R17-003 GRANT PROMOTE, letter tier)
12="n", 48="e" letter tier. Registry: none.

### R20-009: pas-30 — DUPLICATE (R17-004 GRANT PROMOTE, conditional)
30="pas", conditional on 94-LEAD and 59-provisional. Registry: none.

### R20-010: a-39 — DUPLICATE (R17-005 GRANT LEAD, allophone tier — NOT full promote)
Standing is LEAD (/a/ allophone). FLAG: do not upgrade on the queue's
"promote" wording. Registry: none.

### R20-011: ent-06 — DUPLICATE (R17-007 GRANT PROMOTE, conditional)
06=["ent","prom"]. Registry: none.

### R20-012: o79-adjudicate — GRANT (adjudication delivered; split stays red-team venue)
Bar met 5/5 with stated causes: @496 O-remains (gated on queued
subj-42-ne-frame); @883 W-conditional (68 masculine); @1010 W-conditional
(80 non-finite); @1364 S ("ne tout" ungrammatical all functions);
@1688 S (systematic "94 79" x2). New tally: W=11 (9+2 conditional), S=6,
O=1. Weakest leg: the W-classifications are conditional; the S-growth is the
firm leg (byte-identical 2x repetition rules out hapax rescue). No
declaration — split stays red-team venue per §7. Registry: none.

### R20-013: syl79-wordname — GRANT (naming delivered: 2 named, 2 fenced)
"79 17" x2 @451/@1460 named "toutefois" (lexicalized /tut.fwa/ —
inflection, not polyvalence, §7 intact); @53 and @1419 fenced (85/58 and 15
open). No value declared beyond banked 79="tout" / 17="fois". Registry: none.

### R20-014: trigram-79-82-48 — DUPLICATE (R15-A7: L2 frame GRANT; 48 value NOT promoted)
L1 "est" killed; L2 "tout me [48-verb]" frame stands. Registry: none.

### R20-015: par-le-set — DUPLICATE (R15-A14 GRANT, set-level)
"par le"+substantivized infinitive for X in {92,33,86}; values not named.
Registry: none.

### R20-016: disc-01-24-ci-X — DUPLICATE (R18-008 REJECT promote; GRANT LEAD {faire} + 01="en" local LEAD + FINDINGS)
Survivor set {faire, laisser} stands. Registry: none.

### R20-017: par43-suite-adverbial — GRANT (corpus-side attestation leg; no value named)
Bare "par suite" as sentential "consequently" attested (Littré §27); the
escape is structurally licensed but valuationally moot (43="suite" killed,
R19-046/063). FLAG: do not cite as a 43-value lead. Registry: none.

### R20-018: par-43-class — GRANT (support-leg confirmation of R19-045; no value promoted)
6-gram '45 64 96 43 87 01' byte-identical x2 (@340-345, @1024-1029);
43 in a licensed nominal slot after 'par'; all 16 windows censused with
zero contradiction; firmest leg @563 "la [43] [24-fin]" (DET+noun+finite
verb). Supports R19-045's 43=["noun","cls"]; no new class, no value named.
Registry: none.

### R20-019: 96-complement-census — GRANT (census finding; refines R19-011)
n(96)=21, all offsets byte-exact; 7 means-par, 5/2 complement-less,
5 open, 4 fenced compositional; successor multiset re-derived byte-exact.
Refines R19-011's "par pour x3 unique in kind" (kind-uniqueness holds; the
count claim narrows). Adverses gathered for the red-team 96/00 venues;
nothing decided at battery level. Registry: none.

### FAM-B: ne/negation batteries (R20-020–031)

### R20-020: ne-census-1248 — GRANT
12→48 x5 re-derived byte-exact @169/@709/@809/@1075/@1736. Registry: none.

### R20-021: ne-follower-census-84 — GRANT-WITH-CORRECTIONS
25 84-windows byte-exact; 84→94/48/12 all x0; the lon discriminator is not
weakened. Correction: "94='ne' battery promote" is a tier mislabel —
R17-001 rejected the promote; 94='ne' is STRONG LEAD. Registry: none.

### R20-022: verbless-ne-family — GRANT-WITH-CORRECTIONS
37 94-windows byte-exact; 62-94 x9; D3 partition 9 attachable / 28
un-attachable re-derived; @508 re-frame stands as a segmentation
hypothesis (§7-clean). Correction: the C2 table's @-labels are one less
than the true 94 positions — labeling slip, no assignment changes.
Registry: none.

### R20-023: ne-particle-ungrammatical-sweep — GRANT (evidence package)
All 37 follower frames re-derived byte-exact; 8/9/4/16 partition delivered;
residuals @1363/@1687 ("ne tout") and @1664 ("ne on") honestly fenced.
Registry: none.

### R20-024: neque-tail-24-85-clause — GRANT
Locus bytes verified; "24 85" bigram x5; R24 legitimately adopted as a
premise. Registry: none.

### R20-025: neque-15slot-fence — GRANT
16 distinct-46 brackets re-derived byte-exact; all 15 non-W3 slots
confirmed empty of a finite verb under standing law; W03 (24, finite/modal
per R24) the exception. Registry: none.

### R20-026: ne-attachable-paradigm — GRANT-WITH-CORRECTIONS
Deliverable stands: three disqualifications real (@651 contradicts the
parent D3 census's own definition; @771/@1701 carry second-94
interveners). Correction: the "6 clean" core overstates — honest core is
4 clean (@65, @161, @1705, @1773) + 2 conditional (@1330, @774) +
3 disqualified. NOTE for the record: the @651 parent-D3 inconsistency
should be marked against the ne-follower-verbless-sweep census.
Registry: none.

### R20-027: ne-1331-70-52-parse — REJECT the promote; FENCE
The bar ("resolve iff @1331 parses under one arm with stated values; else
fence") is NOT met. Arm A loads on 52's prendre-family verb role, which is
NOT a stated standing value (the three-way tie comes from NULL batteries;
52 is UNIDENTIFIED in the registry). Arm B's kill is sound (sel-62-48-94
KILL closed; §3 bars inventing a 62 value). FENCE: arm A live-conditional
on 52's prendre-family resolution; arm B dead. The battery's claimed
resolution is withdrawn. Registry: none.

### R20-028: ne-W6-pas-verb — REJECT the promote; FENCE
The bar's C2 should have fired. The elimination chain's load-bearing
premise, particle-'ne' at 94@1363, is not granted: the promoted sweep
battery classifies the same window as B-group residual ("ne tout"
ungrammatical). The "no ungranted assumption" claim is false. Attacker
concurs (ATTACK-SUCCESS). FENCE: 03 finite at @1367 only conditional on the
particle reading of 94@1363; W6 C1 does NOT re-open; the battery's claimed
consequence is withdrawn. Registry: none.

### R20-029: ne-1330-bare-corpus — GRANT-WITH-CORRECTIONS (construction-level)
Bare-"ne" + finite verb attested many times over in 1841 sources,
including the diplomatic register; the exact "ne [finite] de [INF]" shape
attested ("je ne cesse de rapprocher tout le monde",
"Il ne cesse de discourir", "Je ne sais si le bruit est fondé" — all
verified in the cited files). Methodology verified (2,229 candidates,
whitespace-normalized split, conservative partner tier). Corrections:
(a) the 2,229-candidate hand-audit has no recorded decision trail beyond
the 15-example sample — not byte-reproducible from artifacts;
(b) "n'importe" is a fused lexical item, not bare "ne" + finite verb;
(c) the verdict's "unstrained" reads construction-level only;
(d) corpus subset unexplained (71 of 76 txt files). The constructional
PROMOTE stands. Registry: none.

### R20-030: ne-1330-lexical-trio — GRANT
Bar met on the closure arm: 0 genuine bare-"ne" + prescrire/préserver/
prévoir in 207.1M chars (28/0 in the 1841 corpus, 406/0 in the Europarl
control); the 7-verb licensed class closed (5,032 of 5,435 bare candidates
in the 7 verbs; the 391 "other" dissolved; 13 doubtful, none trio-related).
The apostrophe-normalization fix verified live in the detection paths
(load-bearing: 45,289 U+2019 chars). Diachronic caveat: C2's closure sample
is modern-French; 1841 closure rests on the parent's census shape.
Registry: none.

### R20-031: syll-94-508-verify — GRANT-WITH-CORRECTIONS
The negative half is unconditional and kill-grade: particle-94 dead at
@509 (successor 64='qui' banked GT; "ne qui" ungrammatical). Corrections:
(a) the positive half (syllabic specifically) is conditional on provisional
77="le" AND on 62 naming a 'ne'-final word — the latter condition is
missing (62's value open; "trône" lead-grade, not demonstrated);
(b) the sibling-window contrast loads on killed 62 values ('il' killed
R19-106; 'on' killed by collision-62-84) — struck as stale.
Registry: none.

### FAM-C: ver-78 family (R20-032–038)

### R20-032: ver78-ce78-census — GRANT
Bar 4/4 pass on re-derived bytes: 7/7 'ce [78]' windows re-read under
standing values; @364/@1397/@819 killed completions re-derived;
@1105 correctly left open on 65's unvalued status; @573/@982 under standing
45="ce" (A11 HOLD) or the dict lead — determiner-profile either way. The
successor-completion formulation retires. No value promoted; no lead
re-graded. Registry: none.

### R20-033: ver78-flagship-1181-1352 — GRANT-WITH-CORRECTIONS
Both flagship strings parse under standing values at the two and only two
5-gram sites (@1181 'le ver | ne mentent'; @1352 'le ver | ne ment',
[52] strain fenced with cause). Finding grade only. Corrections:
(a) 94='ne' is STRONG LEAD (R17-001), not "battery-promoted";
(b) 62='il' is KILLED at kill grade (R19-106) — the clause-4 left-edge
'il e' wording is STRUCK; (c) 59='est' is provisional, not
"battery-promoted". Registry: none.

### R20-034: ver78-1670-5581 — GRANT
The bar's disjunctive fence disjunct fired legitimately: n(55)=12,
'55 81' x6 re-derived exact; 55=verb battery-grade (R19-077) explains
W1/W3/W4 conditionally but is blocked at W2 (06-rule) and W6 (no licensed
post-"la ver" verb frame); adjective arm dead (zero legs, no §7 split
declarable at battery level); @1670 fenced with stated cause and stated
re-open conditions. Registry: none.

### R20-035: ver78-non45-positive-leg — GRANT (legs only)
@819 '47 78 40' = "ce verre" parses as a grammatical French NP on
banked/granted values only (47='ce' A4, 78='ver' the tested value, 40='e'
pencil GT); zero hard contradictions; the consistency scan holds (zero
windows force 78='ver' false); no 45 in the window or row a5_05
(independently verified) — the 78↔45 mutual conditionality breaks from the
78 side. The @364/@1397 '76-47-78-48' x2 second leg family banked with its
stated dependency (battery-promoted 48='e'). The battery correctly declined
global promotion; R16-005 LEAD stands. Registry: none.

### R20-036: boundary-value-census — GRANT (census finding, promotes no value)
31/31 windows re-derived; the four 'ver'-shaped loci are exactly the four
78-45 windows; only @574 parses 'ver'-shaped as a leg ("ce verdict",
conditional — R19-187-gated); @314 resolved A11 'ce'; @983 fenced NEUTRAL;
@1165 double-residual. The >=2 iff fails — the value arm gains no new leg;
the "four 78-45 windows = four legs" notion retires at battery grade.
Registry: none.

### R20-037: lever-lement-rival — GRANT-WITH-CORRECTIONS
The '…levement' rival at @1180/@1351 stays undemonstrated; the '…lement'
word-composition is closed at battery grade. 5-gram x2 and trigram x3
re-derived exact; the trigram's standing parses are "ne mentent" x2 clean.
Correction (material): 62='il' is KILLED at kill grade (R19-106), not a
standing value — clause 1's no-host outcome stands a fortiori; the
independent byte anchor is the intervening-token structure.
Registry: none.

### R20-038: residual-1029-infinitive — REJECT the promote; GRANT the new findings as findings
(a) The queue's RE-BRIEF is authoritative: the '@1029 ceci [03]er [80]-le'
premise is STALE and the target was to be worked against the A/B frame —
the battery worked the ceci premise and never tested the A/B race.
(b) The promoted reading is exactly the reading R19-142 FENCED ("do not
ratify for banked use"); a battery cannot lift a red-team fence (R19-100
precedent), and the fence's load-bearing legs are untouched by the new
evidence. New findings GRANTED as findings: 03's class resolution removes
the conditioned-split hedge at @1030 (within R19-178's conditioned scope);
'01 03' hapax census @1029 x1/1847 re-derived exact; the 7-level
register-fence restatement. The @1028–1031 window stays FENCED per R19-142;
re-work against the A/B frame stays queued. Registry: none.

Carry-forward item: 78='ver' — DEFER with cause. R17-006's settle condition:
(1) 45='dict' resolved — NOT met (45 stays ["ce/dict","lead"],
unratified); (2) a new positive leg on banked/granted values — MET AT
BATTERY GRADE by the @819 "ce verre" leg (R20-035), pending red-team
ratification. The legs are positive legs for a value, not a value proof —
none of the seven batteries independently names 78='ver' at red-team grade;
the 'verdict' value (R19-187) stays conditional on the unsettled LEAD.
R16-005 LEAD stands; the @819 leg is banked for the red-team settle
decision; R19-194's re-arm stays queued (trigger unfired).

### FAM-D: 98/vient + 97 + 65 (R20-039–047)

### R20-039: venir-a-1841-corpus — CONFIRM R19 (no new delta)
R19 already confirmed. Registry: none.

### R20-040: frame66-vient-80 — GRANT-WITH-CORRECTIONS (window-level)
Bar met: 80 infinitive-shaped at @768 (locus byte-verified); six rivals
killed at grammar level; two complete clauses @760–768. Corrections:
(a) the adopted premise "98='vient' (vient-98-name PROMOTE)" is
tier-misstated — R19-172 REJECTED the value promote; operative premises
are 98=finite-verb class (granted R19-171/176) + 'vient' value-LEAD;
(b) the 66-subject premise is adopted from the NULL parent
val-66-767-frame (window-level) — honestly flagged, battery-grade adoption.
Scope @768 only; poly-80-docket untouched. Registry: none.

### R20-041: vient-complement-inventory-ratify — GRANT (packaging grade; red-team input)
Bar met: C1–C3 ('de' 4/5 clean + @930 broken at kill grade; 'pour' no
break; elided clitic no break), C4 (consequence rule applied as package
statement, not adjudication), C5 (no adjudication performed).
Correction: premise tier "98='vient' (battery PROMOTE)" → LEAD per
R19-172. The @930 break is doubly conditional on two battery-level
verdicts — if either falls, the break dissolves; the package's red-team
framing of the three options is the correct §7 posture. The 98-76 and 98-65
re-open is packaged as a docket item, not decided here. Registry: none.

### R20-042: vient-98-355-transitivity — GRANT (census finding)
Bar met: all 40 windows censused with stated grounds; predecessor
distribution and sandwich uniqueness byte-verified; C2's adverse antecedent
is FALSE — three nominal-subject windows @80/@440/@1725 under standing
noun-class grants (42 R19-055; 43 R19-045), so @355 is NOT kill-grade
adverse material on the nominal-subject ground. Weakest leg: the
"nominal" subjects are class-level and @838 honestly left underdetermined
— the census discharges the adverse but adds no non-circular positive
value leg for 'vient'. Census-level only. Registry: none.

### R20-043: 98-237-frame — GRANT (battery-grade, window-local)
98='vient' named at @236 via compositional 'pré-vient' (70='pre' banked
pencil GT; 'prévient' a French word); finite-verb class + grammatical
"prévient [41] fois la [26]" parse; the 98='par' rival closed via §7.
Correction: premise "vient-98-name PROMOTE" → LEAD tier per R19-172.
Weakest leg: the same compositional singleton R19-172 graded thin — meets
the battery bar but does not move the global value grade. Scope: @236 only.
Registry: none.

### R20-044: frame-97-profile — NO NEW DELTA (R19 closed; no re-adjudication)
R19 ruled: CONFIRM R18 REJECTION, CLOSE (no new byte evidence). Registry: none.

### R20-045: nom-97-526-adverb — GRANT (window-level)
Bar met: 81's class at @524 named NOMINAL at battery grade (collocation
uniformity "55 81" x6 + 10/14 determiner-predecessor population + zero
stream-wide adverbial license; all censuses byte-verified); adverbial-81
dead at @524 → INF-topic revival condition fails → NOM-97 hardened at
@526. Weakest leg: the determiner reading loads on unvalued 55 — the
battery rests on the collocation and fences this honestly; the hostile
@1096 "[81]ent" window stays fenced, not resolved. Consistent with R19-123.
No polyvalence; §7 intact. Registry: none.

### R20-046: redteam-97-tie-adjudication — GRANT (packaging grade; tie stays red-team venue)
Bar met: no class decision in the report; all four components byte-exact
(leg tally 6 INF / 4 NOM, @525 clean NOM parse, pour-window discriminator,
@566 13-blocker status). Correction: the package's premise "frame-97-profile
(97 infinitive-class, class-level PROMOTE — standing, not downgraded)" is
stale — R18-023 rejected it, R19 closed it. No battery-grade class decision
is possible — the tie is genuine at battery grade (INF/N underdetermined is
the standing state); the deciding venues are live and queued. The tie
survives at the four 'pour [97]' windows (INF-97@525 killed via R20-045).
Registry: none.

### R20-047: enne-65-lexicon-tighten — GRANT (finding)
Bar met: genuine-0 confirmed for all three forms (independent re-run on the
drifted-larger corpus reproduces 14/0/0 raw and genuine 0). The @65
word-final fence hardens. Registry: none (65 stays ["noun","cls"]).

Carry-forward decisions. "Values for 98" — DECISION: KEEP AT LEAD; DO NOT
GRANT. Attack question answered: 'vient' is NOT uniquely forced. The
windows survive under unvalued neighbors; 'revient' remains the live rival;
nominal-subject windows don't discriminate verbs. The strengthened
post-R19 evidence is net-mixed: the transitivity adverse is discharged
(R20-042, defensive), but the inventory ratify broke the 'de' member at
kill grade @930 (R20-041), the compositional leg remains a singleton, and
R19-172's three rejection reasons stand (circularity with the conditioned
83='de' lead; thin positives; unresolved anomalies: doubled-98 x3,
@702 'n'vient', @1139 'pour [98]'). Grant conditions (R19-172's R20 calls):
83='de' ratification or doubled-98 cause resolution. Registry: none.
"Values for 93" — DEFER WITH CAUSE: no new byte evidence in this round's
docket touches 93's value; R19-166's class grant stands; no 93-value target
exists in battery-queue.json. "65 gender" — DEFER WITH CAUSE: R20-047
hardens the @65 word-final fence but names no gender; 65 stays
["noun","cls"]; gender ownership remains with the 32-duality docket.

### FAM-E: governed-exclamatory-infinitive corpus (R20-048–058)

All eleven corpus batteries GRANT (corpus construction findings; no value
named; no registry cell touched). Orphan sweep 11/11.

R20-048: gov-excl-inf-np-boundary — GRANT (corpus finding). 24
hand-classified Cause-C windows (de=9, à=11, pour=4); all three governors
license NP-embedded governed infinitives (falsifies the "only à, never
pour" asymmetry); scoped to the 1841 print register.

R20-049: gov-excl-inf-recall-drama — GRANT. ≥1 genuine in drama (Labiche,
"Oh ! non… pour ne pas la montrer !…", dist=1); independently re-run,
same window, two passes.

R20-050: gov-excl-inf-drama-n2 — GRANT. 6 genuine (1 Scribe, 5 Labiche),
4 non-Scribe plays → drama-wide. Report headline arithmetic corrected
(window list authoritative).

R20-051: gov-excl-inf-drama-recall — GRANT. Sibling confirmation of the
R20-049 window (counted once in the inventory).

R20-052: gov-modal-inf-register-drama — GRANT. 5 genuine across 5 plays
(modal/perception/causative governor family, distinct from prepositional;
correctly scoped).

R20-053: gov-excl-inf-diachronic-bracket — GRANT. 6 genuine in
Zola/Maupassant 1877–1888; emergence window narrows to [1841, 1877];
near-misses honestly excluded.

R20-054: governed-excl-inf-topic-audit — GRANT. 233 distinct strings
hand-classified (F=112 finite-matrix, H=112 false-friend/artifact, G=9
exclaimed-NP, 6 embed genuine infinitives); 0 genuine with any dislocated
topic; corpus gate byte-identical to the parent.

R20-055: gov-excl-inf-drama-comedy-skew — GRANT. 4 genuine in drames
(Hugo Le Roi s'amuse ×2, Hugo Lucrèce Borgia ×1, Dumas fils Dame aux
camélias ×1) → drama-wide. Comedy count corrected to 8.

R20-056: gov-excl-inf-drama-n3 — GRANT (verification finding).
Cumulative inventory verified at n=12 (2 Scribe, 6 Labiche, 3 Hugo,
1 Dumas fils; 8 comedy / 4 drame); candidate set reproduces exactly;
genuine list byte-verified independently.

R20-057: gov-excl-inf-tragedy-n2 — GRANT. 1 genuine (Delavigne, "Ou plutôt
à revoir !"); the softest of the inventory (frozen-form tension adjudicated:
constructed corrective self-repair, not the fixed idiom). Correct
cumulative: 13 (comedy 8 / drame 4 / tragédie 1).

R20-058: gov-excl-inf-drama-grade — GRANT. Audit of all 12 standing cases:
11/12 are dialogue-elliptical fragments; Hugo's *Lucrèce Borgia* case is
standalone (byte-verified in context: "À mon tour maintenant, à moi de
parler haut et de vous écraser la tête du talon !" — explicit "moi"
subject, self-contained, no finite matrix). The fragment-theory break
HOLDS. The fragment-grade grammar does not cover the construction.

Family-level: inventory genuineness scrutinized, 13/13 genuine; no
cherry-picking (all batteries share the parent exclusion taxonomy and
report per-cause counts including the zero arms); these license a
construction, not a value. Registry: none.

### FAM-F: noun-26 / 06 / ent / 60 (R20-059–068)

### R20-059: noun26-pas-frames — GRANT (frame-level; positional-rule referral recorded)
Bar (a)–(e) all pass on re-derived bytes: four '26 30' windows byte-exact;
noun-parse ungrammatical @654/@991/@1249, boundary fenced with stated
cause @1559; ne-audit per window recorded; bare-'pas' tension flagged.
The §7 cost (second positional polyvalence) is referred, not declared, per
the bar's own escape clause. 26 stays ["noun","lead"]; no value named.
Registry: none.

### R20-060: noun26-encequi-triple — GRANT (finding grade)
Triple re-derived byte-exact; @1768 parses with 26 as verb; 37's slot
honestly NOT decided (fenced to queued frame-37-reexam); 23~26 split
respected; subject-reading rival excluded via 59='est' in the identical
slot. Weakest leg: class-by-uniformity with n=1 for 26 itself, leaning on
provisional 59='est' — honestly stated. Registry: none.

### R20-061: noun26-gov-frames — GRANT-WITH-CORRECTIONS
All four governor windows byte-exact and the verb-forcing parses stand.
Correction (R19-106 blast radius): the battery cites "62='il'
demonstrated" — 'il' is KILLED at kill grade, permanent. The parses survive
with 62's value OPEN (subject-shaped slot; R19-099's noun-62 windows
support a noun subject; 'ne' must precede a verb). The "62='il'" citation
is struck; nothing else moves. Registry: none.

### R20-062: noun26-la-frames — GRANT-WITH-CORRECTIONS
Bar met: @239 absolute "une fois la [N]" byte-exact; @1559's 'pas'
resolved as a boundary fence with stated cause; @128 byte-exact; @530
decided as verb-slot under the positional rule; '26n' at @239 tested and
live-but-unexcludable. The refined positional rule records its §7
polyvalence cost for the red team; no polyvalence declared. Corrections:
tier-staleness — 30='pas' is PROMOTE (R17-004), 12='n' is PROMOTE
letter-tier (R17-002), 94='ne' is STRONG LEAD (R17-001 rejected the
promote), 06='ent' is PROMOTE (R17-007). All corrections strengthen.
26 stays ["noun","lead"]. Registry: none.

### R20-063: noun26-69-pour-dire — GRANT (finding grade)
Trigram '26 00 33' x3 re-derived byte-exact; 69's 12-window profile supports
the noun naming (10/12 nominal, 1 verbal @1115 honestly packaged as a §7
split candidate, not declared); the 33 word-vs-stem fork fenced out of
26's class decision. Consistent with registry 69=["noun","cls"] (R19-109):
consistent confirmation. Registry: none.

### R20-064: 06-forces-84 — GRANT (consistent confirmation; no escalation)
06's class as 'ent' consistent with the standing R17-007 red-team grant;
@1188 parses with the required word boundary, so the feared 'en on est'
contradiction never fires; the NULL/escalation branch (06='en') is closed —
consistent with R19-105's rejection of the 'ne' co-value. Read as
consistent confirmation of the standing grant, not a battery-level
re-promote. 06=["ent","prom"], 84=["on","prom"]. Registry: none.

### R20-065: prenne-subject-S1545 — GRANT (subjectless confirmed via second disjunct)
Bytes byte-exact: '00 46 70 12 94 92 45 23' — the slot between 'que' (46)
and the prenne composition (70 12 94) is EMPTY; no postposed-subject
reading is licensed in an 1841 'que'-subjunctive clause. The battery takes
the bar's second disjunct honestly: subjectless confirmed with stated
cause. Registry: none.

### R20-066: nest-subject-86-62-42 — GRANT-WITH-CORRECTIONS
The three 'X 94 59' loci re-derived as the stream's only three
(@558/86, @762/62, @1795/42; '12 59' = 0x). 86's and 42's subject parses
are unforced and contradiction-free. Correction (R19-106 blast radius):
the battery's 62 leg reads "il n'est à [88]..." under the "demonstrated
62='il' rival" — 'il' is now KILLED at kill grade. The subject-SHAPE bar
still passes for 62 with the value OPEN, but the "il n'est" reading is
struck. Further tier corrections: 30='pas' standing PROMOTE (R17-004);
94='ne' STRONG LEAD (R17-001). All three windows remain conditional on
provisional 59='est' (stated). Registry: none.

### R20-067: ent-06-host-214 — GRANT (census deliverable; @215 fenced as residual)
44/44 06-windows classified byte-exact (n(06)=44 confirmed). C1: licensed
hosts are the F61 94-82 "ment" frame (4 windows, re-verified); the licensed
verbal-stem host class is honestly EMPTY at battery grade (0 windows;
§3 bars inventing a stem). C2 fires the designed else-arm: @215 ("le ver
ent est que") fenced as a genuine residual with stated cause — fenced, not
killed, so a red-team 78-naming can re-open it. 06=["ent","prom"].
Registry: none.

### R20-068: gerund-60-1688 — GRANT (finding grade; EVIDENCE INPUT to poly-60-redteam)
Bar met: @1688 = '62 94 79 14 60 27 46 24 85' parses as "…ne tout en
[60-stem]…" (79='tout' PROMOTE R19-119; 14='en' battery promote,
R19-023/024 confirmed; 60 verb-class at battery grade; -ant unspelled per
en85-gerund-reaudit; 58='ant' KILLED so no spelled ending expected).
H-14 re-opens with 27 as sole open (27 hapax, already queued). Weakest leg:
every leg is battery-grade, honestly conditioned — the bar explicitly
licenses battery-grade promote; the reading strengthens the verb arm
without touching R19-090's fence (no polyvalence declared;
present-participle is inflection of the verb item, not a new item). Per the
carry-forward note this is evidence input; the "poly-60 item-hood" P1
decision stays with poly-60-redteam (FENCED, R20-118). Registry: none
(60 absent).

Cross-cutting: (1) 62='il' kill blast radius (R19-106): two batteries cited
"62='il' demonstrated" — both verdicts survive with value-open corrections
above; any other processed report citing the 'il' rival is now a live
staleness defect. (2) Tier-staleness pattern: several batteries described
30='pas'/94='ne'/12='n'/06='ent' as "battery-promoted, pending
ratification" — standing: 30='pas' PROMOTE (R17-004), 12='n' PROMOTE
letter-tier (R17-002), 06='ent' PROMOTE (R17-007); only 94='ne' is
sub-promote (STRONG LEAD, R17-001). All corrections strengthen. (3) Noun-26
war: 16/17 windows decided or fenced; the positional rule recorded twice
with its §7 cost stated; declaration remains a red-team act. Remaining
orphan window: 0b1470.

### FAM-G: boundaries, segmentation, census (R20-069–082)

### R20-069: seg-a1_01-constraint-sweep — CONFIRM R19-048 (no new byte evidence)
R19-048's GRANT (sweep finding) stands. Re-derivation confirms the bytes:
offset-1 row = 35 pairs, byte-identical; canonical @52–53 = '11 79'
("la tout"); all 35 offset-1 pairs are 96-type members. Adoption of
offset-1 remains a red-team act. Registry: none.

### R20-070: seg-ceci-87-61 — CONFIRM R19-138 (no new byte evidence)
R19-138's ruling stands: ceci wins at @644; composition granted
locus-level; 87=["ce","prom"]; 61 unvalued globally. Re-derived:
"87 61" x1 @644; "87 11" x7. Weakest leg (E3's "faire ceci" parallel loads
on 24=finite-modal): survives R24 — 24@643 is followed by 87, not 85.
Registry: none.

### R20-071: seg-528294-word — GRANT-WITH-CORRECTIONS (word-unit promote stands)
Bar met: "52 82 94" x3 re-derived byte-exact @649/@1100/@1574; n(52)=27;
"amnestier"/"amnestie" enumerated with 52="a" as the single new
assumption; all 24 non-trigram windows fit with zero forced contradictions.
Weakest leg (the lexicon enumeration is lexicon knowledge, not a period
corpus): the "-e-" spelling's period attestation is UNCITED — lead-grade,
not established; the bar's C1 is satisfied by the amnistie/amnestier
family regardless. A1 (94's status at the trigram windows) fenced for the
red team per §7; the word-unit is conditional on that ruling. Registry:
none (word-unit scope only; 52="a" recorded in _meta as the composition's
letter premise).

### R20-072: seg-81-30-offset1 — GRANT (conditional dissolution finding)
Byte-exact: row a1_01 d[18:22] = '8130' = canonical @44–45 "81 30";
under offset-1 the span re-pairs as "13 06", and neither "81" nor "30"
occurs anywhere in the 35 off1 pairs. The dissolution arm fires; the
re-test arm does not. Weakest leg (the offset-1 phase is contested):
the battery scopes honestly — conditional finding only, canonical-stream
fence untouched. Registry: none.

### R20-073: inventory-doubling-contrast — GRANT (evidence package)
C1: "12 94" x3 @64/@348/@1548 re-derived, all three carry the doubled n —
the general single-consonant habit falsified at byte standard. C2:
compositional account packaged — "70 12 06" x1, "30 06" x4, "12 06" x2,
"70 12" x3 (all re-derived byte-exact); 94 contributes its own n
("prenne"/"enne"), 06 contributes none. C3 honored: evidence only, no
class/value/split declared; R19-167 adopted as premise (94 = single
syllabic spelling "ne"). Registry: none.

### R20-074: er85-word-census — GRANT (census; rescue route fenced)
"29 85" x3 @96/@374/@1233 re-derived exact. Zero windows compose an
'er[85]' word under standing values: 85's value is open (A3 frame grant
only); naming any 'er…'-word would invent a value, barred by §3. The
finite-63 strand at @373 receives no rescue from this route. The '[63]er'
boundary rival honestly left open (needs 63's value; fin63-373-rerun
venue) — the fence is route-scoped, not a global kill. Registry: none.

### R20-075: bound-40-boundary-resolve — GRANT (finding: 40='e' is a FREE letter)
Bar met with distributional byte evidence. Kill-grade leg verified: the
gloss-anchored "premiere" crib over "11 70 82 34 29 40" places 40
word-final ("82 34 29 40" re-derived at [756, 1036], i.e. 40 at 0-based
@759/@1039 = 1-based @760/@1040) — a bound letter (never at a word edge)
cannot be word-final: the BOUND hypothesis is dead at kill grade.
Supporting: n(40)=21; "40 08" x2 @921/@943; "29 40" x9; the second crib
(@1040) places 40 before 17='fois' (promoted word). Window-12 row-label
correction verified: a5_06 spans 1-based 826–850, so 0b848 is a5_06-internal
(B classification retained on the standing free-word rule). Downstream
stated honestly: free permits but does not force the 40|08 boundary; the
parent battery's 08|62 fence stands. Registry: none (40 stays ["e","gt"];
free-letter status to _meta).

### R20-076: 62-boundary-census — GRANT (evidence package for redteam-62-split; decides nothing)
All 35 62-windows censused byte-identical to the independent re-derivation
(35/35 positions match). Anchors: "62 94" x9; "94 62" x0; "08 62" x2.
Boundary claims: 1 forced boundary (@46 right, fol=96='par'), 1 forced
no-boundary (@1349 left, via bound-letter 34='i'), 68/70 sides
UNDETERMINED with stated cause. New observations verified: @1349 (sole
standing-decided left boundary), @1482's fol=46='que' gap (banked GT but
not in the licensing set — honestly recorded), @849's 62|21 adjacency
crossing the a5_06|a5_07 row join. Weakest leg (does R20's 40=FREE flip
@849's undetermined left?): no — a free letter is not a free word; no
standing rule forces a boundary at a free letter's side. §7 honored
throughout. Registry: none.

### R20-077: kernel-6926-frame — GRANT ("69 26 00 33" = "ce [26] pour [33-INF]")
"69 26 00 33" x3 @405/@933/@1627 re-derived. C1: parses with exactly 1 new
assumption — 69's standing 'ce' value-lead (R19-110) as parse premise;
"ce"+26-noun = licensed DP, "pour"+33-INF = licensed purpose infinitive;
uniform across all three windows. C2: no licensed zero-assumption rival
(the attack's "two bare nouns" candidate is not a LICENSED parse).
Using a value-lead as a parse premise is not a value declaration (§7
intact). Registry: none.

### R20-078: f61-06-scope-precise — GRANT (conditioning rule, battery grade)
n(06)=44 confirmed; predecessor distribution sums to 44. "82 06" x4,
all row-internal, no fifth instance. 'ent' licensed at each covered
position via "m"+"ent" under banked 82='m'; no covered window forces a
non-'ent' reading. Weakest leg (the charter's "iff"): the battery honestly
tests only coverage, not the reverse direction — correctly scoped, and the
untested direction is recorded, not smuggled. Registry: none
(06=["ent","prom"]).

### R20-079: 1696-reparse-adverb — GRANT (B-frame collapse confirmed; surviving parse delivered)
Window table @1692–1707 re-derived byte-exact. (a) fenced with cause:
post-58 clause has no nameable subject (23, 91 unvalued; §3) and no
securely finite verb. (b) fails as specified: the bar's pre-R24 24-premise
is superseded — standing R24 declares 24@1693='en' ("24 85" bigram x5
re-derived); "que en [85-inf]" is ungrammatical, and no in-budget rescue
preserves both the infinitive shape and 58-as-object. Surviving parse
delivered with its single stated assumption: inversion "qu'en [85-fin]
[58-subj-noun] [15-adv]". (c) answered: "ne pas" reads forward to
88@1706 at conditional grade. Frame B's numeral-58 case collapses to
frame A alone; frame A @1756 untouched. Registry: none.

### R20-080: formula-76-49-24 — FENCE (coordinator override; FAM-G's GRANT rejected)
The attack-recovery (independent re-derivation, ATTACK-SUCCESS) proves the
N-ADJ-Vfin license vacuous under current knowledge:
(1) the promote's C1 licensed one specific geometry, NOUN + ADJECTIVE +
FINITE VERB (the census searched an ADJECTIVE slot; all 66 matches are
N-ADJ-Vfin triples);
(2) the promote's own Scope tied the license to the adjective-49 leg
("consistent with adjective-49 … venue: adj-49-420-366");
(3) adj-49-420-366 KILLED adjective-49 at kill grade — its scope is
explicit: the frame "can no longer be read as 'N [49-adj] [V-fin]' on the
adjective leg" and "the '76 49 24' formula needs a new class";
(4) 49's surviving classes are adverb (strained) and noun (strained); verb,
determiner, and relative/interrogative pronoun are kill-grade dead.
Neither surviving class instantiates the licensed geometry: N-ADV-Vfin and
N-NOUN-Vfin have zero census attestations (the census was ADJ-only) and
are ungrammatical in that slot.
(5) the kill report's rescue note ("the frame license stands; what is now
open is the slot-filler class X=49") quietly generalizes the license from
N-ADJ-Vfin to N-[X]-Vfin — the census never licensed that generalization,
and French grammar refutes it for every surviving X.
Supporting flaws: census #64 is a genuine false positive ("gouvernement
provisoire sont" — "sont" agrees with "travaux", not the matched noun;
65/66 clean — damages evidence quality but not C1 alone); the @652 window
is ungrammatical under standing values (@651=94="ne" + @652=76 promoted
noun — "ne" is strictly preverbal; the battery listed "no adverses"
despite battery-lever-77-78 having fenced the "82 94 76" tail as an
"m'+'ne' inversion strain"); cross-verdict conflict: battery-pas-30
(PROMOTE) counted @651→656 ("ne 76 49 24 26 pas") as a valid 'ne…pas'
frame, which a promoted noun between "ne" and the verb makes
ungrammatical — the two promotes cannot both parse @651–656 correctly.
Re-running the battery's own bar with current facts: C1 has 0 attestations
for any geometry the frame can actually instantiate, so the C2 fence arm
fires ("confirmed zero … fences it as an unparsed repeat"). The verdict's
own Scope condition (adj-49-420-366 venue) returned KILL. The condition
failed.
Ruling: FENCE. The x2 byte-identity is real and unexplained; 49's class is
still open; the census (65/66 clean) remains a valid linguistic resource.
If 49's class ever resolves to something licensable, re-run the license
with a new census for the actual geometry. Until then, per the battery's
own C2, the frame is an unparsed repeat. The fence records: (a) strike
census #64; (b) the @651–656 "ne"+N conflict between pas-30 and this
verdict needs a dedicated target; (c) the lever-77-78 "m'ne" strain adverse
must be disclosed by any future re-battery of this frame. Registry: none.

### R20-081: val-42-det-gap — GRANT-WITH-CORRECTIONS (§5 escalation handled correctly)
C1 passes: 0/20 immediate-left determiners (re-derived with the standing
determiner set {11,47,77,79,87}); all 20 positions byte-identical; the 8
position-artifact exclusions honestly classified; the 5 argument windows
(@1794 subject — "[42] ne est [37]" verified; @205/@1410/@1503/@493)
determiner-less under all standing-compatible parses. Correction: the
"@1794 subject leg" tier language — 94 is STRONG LEAD (R17-001), not
"promoted"; re-grade @1794 as conditional on 94-lead + 59-provisional
(the leg survives). C2 fires with the proper-noun leg ADOPTED
(R19-055-compatible: proper nouns are nouns); the pronoun-class
'rien'-family leg is ESCALATED per §5, not adopted. The escalation stands
for the R20 42 venue. Registry: none.

### R20-082: 41-doubling-audit — GRANT (doubling confirmed stream-real)
"41 41" x1 stream-wide @589 (re-derived; @588–591 = '97 41 41 09');
present identically in the upstream 1,846-pair parse; the two 41s occupy
distinct raw digit positions (a3_02 tail / a4_00 head), both rows
even-length at offset 0, zero digits dropped or duplicated. Weakest leg
(phase-dependence: any single-row flip removes the doubling): answered —
a flip has no positive byte evidence, no gloss covers a3_02/a4_00, and
choosing it would be result-driven. C3 fires — the W_C fence from
val-41-1016 stands; 41 naming does not re-open. Registry: none.

### FAM-H: frames, syntax, misc (R20-083–101)

### R20-083: frames-predicative — DUPLICATE / CONFIRM STANDING (R15-A1)
R15-A1 GRANT (37/32/42 predicative frames; 42 weakest, bar met exactly;
19 HOLD). Conditions carry: 37's value unnamed; 59='est' provisional; R24
scopes 24's verb arm. Registry: none.

### R20-084: frames-80-89 — DUPLICATE / CONFIRM STANDING (R15-A8)
R15-A8 GRANT (conditional on 77='le' provisional); 80-vs-89 DISTINCT
granted. R19-120 fenced the poly-80 declaration — consistent (A8 was
frame-level, not a split). Registry: none.

### R20-085: unit-37-01 — DUPLICATE / CONFIRM STANDING (R15-A12)
R15-A12 GRANT (unit, not value). Registry: none.

### R20-086: frame-qui-77-84 — DUPLICATE / CONFIRM STANDING (R15-A13)
R15-A13 GRANT (re-valued "qui l'on est"; F53's masc-noun 84 arm killed).
Registry: none.

### R20-087: infclass-86 — DUPLICATE / CONFIRM STANDING (R15-A9)
R15-A9 GRANT (86 INF-class, class-level). R19-133–137 enriched without
overturning. Registry: none.

### R20-088: frame-37-43-1204 — GRANT (window-local finding)
Bar met: "47 43" = 'ce' + noun-class = DET+N on standing values alone
(47='ce' A4 allophone tier explicitly determiner-capable; 43=["noun","cls"]
per R19-045, @1204 inside scope). Census re-derived byte-exact (16/16).
Weakest leg (47's allophone tier) attacked: A4's grant carries determiner
function, so the tier weakness does no work here. Zero new assumptions;
§7 intact. Feeds: 43-value venue; attributive-91 host question.
Registry: none.

### R20-089: nom-ellipsis-760 — GRANT (premise license)
Bar disjunction honestly resolved: C1 FAIL (no in-stream bare precedent —
@1034 = "la première fois" with head noun), C2 PASS — 30 hand-classified
bare "la première" nominalizations in the 1841 diplomatic corpus.
Weakest leg (hand classification): the bar's existential quantifier is
satisfied even at a fraction of the claimed 30. Licenses only the
grammatical premise; 20's role at @760 untouched. Feeds: the three live
20-roles at @760. Registry: none.

### R20-090: ce-08-31-frame — GRANT-WITH-CORRECTIONS (reading-level)
C1/C2 pass; all numbers byte-exact ("87 08 31" x1 @1487; "08 31" x3;
n(08)=18). Correction (stale citation): C1 cites "det-87-644-function
PROMOTE" as a parallel determiner-arm license — that promote was
DOWNGRADED to FENCE by R19-138; strike the citation. The determiner arm
stands on 87='ce' + standard 1841 grammar + R19-139's @628 "ce [78]"
reading. Verdict holds: @1487–1489 = "ce" + [08][31]-word, 08
word-initial letter. Feeds: 08 word-family. Registry: none.

### R20-091: det-87-644-function — DUPLICATE / CONFIRM R19-138 (FENCE stands)
R19-138 (P1) DOWNGRADED this exact promote to FENCE; seg-ceci-87-61
composition granted; 87=["ce","prom"]. No new byte evidence. PIPELINE
FLAG: the queue entry still shows result: promote against the standing
R19-138 FENCE — coordinator to reconcile (battery-queue.json not touched
per brief). Registry: none.

### R20-092: agr-89-642-adj — GRANT (agreement-admissibility check)
Bar met: no forced gender/number mismatch under standing values (77='le'
provisional; 48='e' inflectional per R19-071, not forced feminine).
Numbers byte-exact (@639–642 = 77 89 48 20; n(89)=14). Weakest leg (parent
subj-20-642 battery-grade; 77 provisional): the verdict is a negative
check, so the conditionality is carried honestly. Strengthening since the
battery ran: R19-161 ratified 89=noun LEAD — the "le [89]e" NP premise is
now stronger. Feeds: 89-value venue. Registry: none.

### R20-093: adv-1135-leftward — REJECT the promote; FENCE (conditional)
The weakest leg breaks. C1.4 licensed "boundary after 20" on the premise
"62='il' (battery promote)". R19-106 KILLED 'il' at kill grade —
permanent. With 62's class open ('il' dead), the right-edge clause-start
at @1136 costs one ungranted assumption (62 must be subject-capable,
unlicensed). Per the bar's own verdict rule (C1 fails → C2 fires), the
promote cannot stand. But the frame is not dead: C1.1–C1.3 survive (modal
clause complete at @1134 under R17-009 + R24's verb arm; manner-adverb
licensed; 20 unconstrained). Ruling: FENCE — the clause-final-adverb frame
("…[24] [77] [86-inf] [20-adv]. 62 …") survives only conditional on 62
resolving to a subject-capable reading. With the sibling boundary-adverb
arm already fenced (adverb-20-wide NULL), 20 at @1135 is now genuinely open
on both rivals. Feeds: poly-20-docket. Registry: none.

### R20-094: 58-det-gap-corpus — GRANT (corpus deliverable)
Bar met in full: census executed (5,117 "en [V]ant" windows; script +
census JSON present), slot classified with full hand audit of the 163-hit
bare bucket, decision question answered — the "rare" arm fires (13 genuine
free-bare of 1,938 nominal complements = 0.7% vs 97.0% determined). The
verdict promotes the corpus result only, not a 58 class. The
devenir-predicative-channel caveat (3/13 hits) is the honest live escape
for 58-value-name. Feeds: the 58 conflict package (answered-residual arm).
Registry: none.

### R20-095: 58-a11-hold-test — GRANT (frame-C finding; fence hardened)
C1–C4 pass; "45 58" hapax @1201–1202, n(45)=22, n(58)=7 all byte-exact.
Weakest leg (rival set closed to {'dict'}): honestly stated; 'dict' fails
on every documented mechanic; the A11 HOLD is not promoted — 45='ce' stays
ungranted (red-team venue). Strengthening: R19-185 ratified 58=["nominal",
"cls"]. Feeds: the 58 conflict package (frame-C side). Registry: none
(58 already ["nominal","cls"]).

### R20-096: 58-det-numeral-tension — GRANT (red-team input package delivered)
Bar (gather/package/no-decide) met in full: frame A (@1756 "85 58 17",
unique trigram), frame B (@1695 "que [24] [85] [58] [15]"), frame C
recorded, numeral/determiner coherence stated without deciding, standing
adverse fenced. R24 update for the red-team docket (not a verdict change):
@1693=24's follower is 85 → under R24 (declared), 24='en' there is
DECLARED, so frame B reads "qu'en [85] [58] [15]" — the 58-slot geometry
is unchanged, but the package's "modal parse dead" premise is now a
declared-'en' parse; weigh the coherence claim under R24. Feeds: the 58
conflict package (this IS its core input). Registry: none.

### R20-097: word-class-08-31-3frames — GRANT (joint class finding)
C1 pass: W nominal (noun/adjective) jointly across @881/@1488/@1520;
numbers byte-exact ("08 31" x3; standalone-31 x8). Weakest leg attacked —
the @1520 modus-tollens ("la"@1517=article forced by joint constraint):
holds under §7 (no W-polyvalence; the adjacent @1515–1516 "la 31"
pronoun+verb is a separate byte-exact token). 31's banked VERBAL class
stands, unrescoped, untouched. Finer noun-vs-adjective split honestly
deferred (bar forbids value naming). Feeds: 08 word-family. Registry: none.

### R20-098: word89e-right-bound — GRANT (boundary finding)
C1–C3 pass; "89 48" x3, "48 20" x2, the @759–760 "40(e) 20" parallel all
byte-exact. Weakest leg (20's post-nominal-adjective class at @642 is
battery-grade): the distributional legs stand independently. The §7 bar on
the bound-only-in-89-context counter-read correctly applied. Strengthening:
R19-161 (89=noun LEAD ratified). Hardens inf89-letter-interior's kill arm.
Feeds: 89-value venue. Registry: none.

### R20-099: 08-position-profile — GRANT (census deliverable)
C1/C2 pass: 18/18 windows censused byte-exact (positions match the
independent census exactly). Headline (initial-skewed, non-uniform:
5 forced initial, 3 initial-or-internal, 3 boundary/conditional,
6 undetermined) is robust. Weakest cell noted (@198 "word-final" —
left-fusion into [60 08] inferential); re-classing it undetermined does
not flip the headline. No value named; §7 intact. Feeds: 08 family.
Registry: none.

### R20-100: 08-letter-geometry — GRANT (signature-level)
C1/C2 pass: neighbor census byte-exact (pre {40='e' x2}, post {34='i' x1,
29='er' x1}, 82='m' zero contacts, 36/36 slots classed). The adverse
(spelling-vs-clitic) answered: both pulls are positional flavors of the
landed letter reading; the clitic pull has zero positive legs (62-08 x0
vs 62-94 x9, standalone-08 kill-grade dead). No value named; stem-08 NULL
untouched. Feeds: val-08-31-letter. Registry: none.

### R20-101: close-14-180-rerun — GRANT-WITH-CONDITIONS (conditional closure)
Bar met at battery grade: C1 trigger (14='en' battery promote —
en14-value-tighten; red-team ratification pending, honestly stated);
C2 composes ("69 en [24-fin]" — under R24, @179=24's follower 87='ce' ≠
85 → verb arm, R24-consistent); C3 zero new assumptions. Locus byte-exact
(@177–180 = 69 14 24 87; "87 64" x5). Weakest leg (trigger is
battery-grade, not red-team): the verdict is explicitly conditional — the
W2 closure lapses if the red team rejects 14='en'. Conditional promote
stands. Feeds: the 14 venue (14's value ratification). Registry: none.

Carry-forward feeds: 03 / 71 §7 splits — no direct feed from this family
(R19-186's 71 split-candidate and R19-178's stem-03 stand on their own
dockets). 58 conflict package — fed directly by R20-094 (answered-residual
corpus arm), R20-095 (frame-C hardening), R20-096 (core input package —
weigh under R24 per the note above). Doubled-consonant package — no direct
feed (inventory-doubling-contrast is its own docket, R20-073).

### FAM-I: 24/modal leftovers + misc (R20-102–108)

### R20-102: parce-quen-952 — CONFIRM (R15 A3 stands; no re-litigation)
Queue verdict points to the R15 red-team doc, where A3 ruled: frame
CONFIRM + 85 verb-stem candidate GRANT (value open). "96 87 46"
@224/@952/@1526 byte-exact; 85 predecessors 24x5, 29x3 (n(85)=15) —
matches R15's numbers exactly. Weakest leg (R24 interaction, new since
R15): 24@953's follower is 85 → 24='en' there, so "parce qu'en" reads
cleaner now, not worse. Registry: none (85 value-open; frame value-free).

### R20-103: valency-33 — CONFIRM (R15 A10 stands; no re-litigation)
A10 ruled que-valency CONFIRM + 33/29 composition HOLD. n(33)=25; "33 46"
x2; "33 29" x5; pre=00 x8/25 — byte-exact match to R15. Post-R15
developments consistent, not adverse (R19-053 closed poly-33 as a
polyvalence question; 33=["INF","cls"], R17-018 spelling duality).
Registry: none.

### R20-104: fois-corpus-article-audit — GRANT (census deliverable; formalizes R19's FAM-A confirmation)
Bar = "re-audit the corpus 'fois que' predecessor inventory for
article-completeness" — both clauses pass with full contexts read.
R19 already confirmed it as a finding ("sharpens det-20's candidate set;
does not revive killed 20='fois'"); this ruling formalizes it at R20.
Re-derived (spot-check): absolute corpus counts are method-sensitive, so
the verdict-critical within-class statuses were tested instead — "la
dernière fois que" all carry "la" (article-dependent); "chaque fois que"
bare in all samples; "cette/plusieurs/deux fois que [clause]" zero genuine
subordinator attestations (the battery's hits are comparative/adverbial
lookalikes). The 100%-within-class structure survives tokenization
differences. Registry: none.

### R20-105: nementent-W2-subject — GRANT (evidence package; R19-167/168-closed disposition)
Bar = (C1) DECIDE one subject account vs re-segmentation; (C2) PACKAGE for
the red-team 94-duality adjudication, no §7 violation. Both pass: C1
decides one account (both windows = [singular nominal clause] + "ne
mentent" + no licensed 3pl subject); C2 delivers the package with the
disposition that R19-167/168 CLOSED the 94 split, so no new red-team act is
requested. Re-derived: "94 82 06 06" x2 @578/@1182 stream-wide; W2 context
byte-exact ("le ver[78]" singular left; "est [42]" predicative right;
24@~1193 follower=82 ≠ 85 → R24 verb arm). Weakest leg: the "no licensed
re-segmentation" claim — "ne m'entent" is not French; word-internal "mne"
closed by R19-167; "on" (84) is 3sg and cannot subject a 3pl verb. The
battery honestly loads on conditional R17-007 (06='ent') and lead-grade
94='ne'. Bookkeeping flag (non-verdict-flipping): the queue entry's
"report" path is doubled
(`code/crowd17/code/crowd17/report_inbox/processed/processed/battery-nementent-W2-subject.md`);
the real file is at
`code/crowd17/report_inbox/processed/battery-nementent-W2-subject.md`.
Registry: none.

### R20-106: reseg-13-armA — CONFIRM R19-170 GRANT; R24 discharges the 24-conditionality caveat
R19-170 already GRANTed this (conditional segmentation). The battery's
bar — (a) state the boundary per window, (b) falsifier "any window admits
no boundary" — passes; no standing grading needs revision. Re-derived:
all five windows byte-exact (@68/@822/@1381/@1554/@1684); n(13)=12;
exactly the five arm-A windows carry verb-class successors (24 x3, 93 x2),
the seven arm-B windows carry non-verb successors. The three 24-right-legs'
24 followers are 56, 87, 65 — none is 85, so R19-170's caveat ("if 24='en',
three right legs fall") does NOT fire under declared R24. The
conditionality is discharged in favor of the grant. Registry: none
(13 not in registry; segmentation only, per R19-170).

### R20-107: ratify-24-modal-input — GRANT (input package delivered; decision stays red-team venue)
Bar = "input package for the red team" (C1 five legs consolidated
byte-exact; C2 queue adverse stated + answered; C3 package delivered, no
adjudication). All pass; the package honestly records that the queue's own
adverse ("24=modal is battery-grade… load-bearing for all five legs") is
now empirically false — the legs survive on R17-009 alone. Re-derived:
"24 85" x5; "24 89" x3; "24 80" x2; all five leg contexts byte-exact.
Weakest leg: the five legs survive on R17-009's class-level "finite verb,
modal-shaped, infinitive-taking complements" license; the label did no
unique work. The open question — whether class-level R17-009 counts as
"ratified" for the rerun gate — is explicitly NOT decided here, per the
task's "package, do not decide" instruction. Registry: none.

### R20-108: 41-1016-det-incompatibility — GRANT (input package for the split-41-redteam docket)
Bar = "deliver the per-value incompatibility evidence to the
split-41-redteam docket at battery grade" (C1 all four det values tested;
C2 clause-boundary rescue audit; C3 per-value pass/fail delivered). All
pass: une/chaque/deux/plusieurs all FAIL the W0 frame on stated corpus
grounds; B1/B2 boundary placements both fail; all four fail → split-forced
evidence packaged. Re-derived: W0 byte-exact (@1012..1023 =
'78 47 03 24 41 15 66 91 53 84 92 64', row break @1019/1020);
"41 15 66" hapax @1016; n(41)=19; 24@1015 follower=41 (≠85 → R24 verb arm).
Weakest leg: the W0 frame's premises — 24=finite/modal @1015 (holds under
R24, re-derived), 15=adverb-class, 66=infinitive-shaped; the battery names
all three as re-open conditions. The corpus zeros' directionality checked:
Pattern B ("[V-fin] DET plus" 0/34.5M) and Pattern A ("DET plus [INF]"
0/88) are one-directional zeros; Pattern A's positive controls internally
consistent. No contradiction with R19-054's D1 determiner-arm grant — the
D1/@1016 tension is exactly what the split docket exists to resolve. §7
honored. Registry: none.

### FAM-J: P1 decisions — values and frames (R20-109–117)

### R20-109: escalate-83-de-kill — GRANT (confirm R19-128)
Decision on the bar ("execute the kill of unconditioned 83='de' or state
the conditioning rule"): both stand as ruled in R19-128. 83='de' is DEAD
at kill grade except in the conditioned windows; conditioned 83='de' lives
as LEAD in the 11-window scope. Re-derived: n(83)=15; positions byte-exact;
conditioned scope {228,898,907,931,1061,1161,1334,1612,1784,1829,1840} +
{911 kill-grade, 614 adverse, 1171 'cède' rival, 1217 fenced}. No new 83
verdicts since R19-128 (de-83-sweep NULL, de83-932-gate NULL; inf-83-fork
KILL and re83-gar-test KILL remove rival values, strengthening the lead's
exclusivity but adding no positive legs). Carry-forward: the "positive legs
for 83='de'" item remains open — the 4-leg restock (1 clean @898 +
formula x3 + compatibilities, R19-126 corrected) is unchanged; no new
positive legs found. 83=["de","lead"]. Registry: none.

### R20-110: escalate-44-deframe — REJECT (confirm R19-066)
Decision ("declare a second polyvalence / revisit the noun-44 kill / rule
stem-level"): no polyvalence declared (§7 DOA); the noun-44 kill is not
revisited; @1714 = clitic slot, value undetermined at red-team grade.
Re-derived: n(44)=15; '94 44' x1 stream-wide (@1713→1714). New since
R19-066: clitic-44-65-discriminator PROMOTE discriminated @1714 to 44='l''
window-local ("ne l'est pas"), fencing 'en' on three stated causes.
Why this does not overturn R19-066: (a) 'y' ("n'y est pas") and 'se'
("ne s'est pas") were never tested — the live set {'l'' (battery-promoted
window-local), 'y', 'se'} is still undetermined; (b) l''s predicative
antecedent is unidentified (fenced discourse-anaphoric); (c) the
discriminator is battery-grade, and window-local values are not
registry-grade (R19-059 precedent). The discriminator strengthens the 'l''
lead but R19-066's narrowing ("clitic-undetermined") stands — a
refinement, not an overturn. 44's cell stays absent. Registry: none.

### R20-111: escalate-1714-ne44 — REJECT (confirm R19-065)
Decision ("admit the '65ne' word-final + 30-predicative re-parse, or rule
the clitic forcing stands"): re-parse not admitted; the clitic forcing at
@1714 stands. Re-derived: @1712–1716 = "65 94 44 59 30". The re-parse
needs two ad-hoc re-valuations with zero positive legs (94 as word-final
"ne" syllable — R15-A15-C3 forbade 94 as letter-'n', no "65ne" word
evidenced; 30 as predicative — no named value, no legs) against the
standing grammatical "65 ne l'est pas" (zero re-valuations). Consequences
stand: noun-44 kill's clause-3 basis intact; pas-30's clause-2 leg not
re-opened; ne-94 not conditioned. Registry: none.

### R20-112: arm-a-fence-ratify — GRANT (confirm R19-144)
Decision ("ratify the arm-(a) fence of ce87-1028-role as standing"):
ratification confirmed; the fence stands. No new byte evidence since
R19-144 (the queue's evidence field cites the disloc-demonstrative NULLs,
which were R19-144's basis). skeleton-1032-revise stays battery-grade; the
ratification sets its bar (resolve 01='-ci' + the demonstrative+bare-inf
gap) without killing it, per R19-144's scope. Registry: none.

### R20-113: ci-984-reading-adjudicate — GRANT (reading (i) wins)
Decision ("rule among (i) A11 'ce(47) [78] ceci(45-01) fait(24)'; (ii)
ver-78+dict-45 'ce(47) verdict(78-45) -ci(01) fait(24)'; (iii) 01='en'
'ce(45) en(01) fait(24)'"): reading (i) WINS at @984, conditional on the
A11 HOLD, locus-restricted to @983–986. Readings (ii) and (iii) rejected
with cause. Re-derived: @981–986 = "47 78 45 01 24 89"; 45-01 bigram
stream-unique (x1 @983); 24-89 contacts x3; 24-85 bigrams x5 — @985's
follower is 89, so R24 gives 24 = finite/modal verb here (not 'en').
(i): bound-ci-984-standalone PROMOTE (restricted; A11-conditional; ±10
contradiction sweep clean) + ceci-984-195-pair NULL. "fait(24)": 24's
class is modal-verb (R17-009, R24-scoped); 'faire' is a live
value-candidate here. (ii) REJECTED: the two-token "verdict" reading killed
at kill grade (dict-45-ce-rival-1165); ver-78 is LEAD only (promote
rejected R16-005/R17); dict-45 NULL; standalone '-ci' is not a French
word; 01 valueless outside ce-contexts. (iii) REJECTED: 01='en' has zero
battery support; 01='faisant' killed (ci-01-value KILL); "ce en fait"
ungrammatical. 45=["ce/dict","lead"]; 01's value unnamed; no 78 value
named. Registry: none.

### R20-114: fuse-88-26-redteam — GRANT-WITH-CORRECTIONS (package granted; §7 declarations HELD)
Decision: the fused-3pl package is GRANTED as the unique grammatical locus
parse at @1706 ("62 ne [88-26]nent" = 3pl verb + 'ne'). The two §7
conditioned claims — 26 word-internal (vs noun lead) and 62
plural-subject (vs 62-98 3sg) — are HELD/fenced, not declared (kill-grade
bar for a §7 act not met). Precedent: R19-134 (package granted;
declaration held). Re-derived: @1704–1709 = "62 94 88 26 12 06" (row
a8_06); 26-12-06 hapax stream-wide; 12-06 = "nent" 3pl-ending byte-exact
parallel with "prennent" (70-12-06); segmentation forces 26 word-internal
*if* the parse holds. Corrections / new constraining kills: verb88-26-stem
KILL — the uniform vient-family stem is dead 16/23 windows, so the fused
form's lexical value is unnameable via a global stem (C1 cannot be
satisfied; the @1706 fused read "remains a valid locus-level parse but
does not generalize"); subj-62-plural-94 KILL — uniform plural-62 dead
(@508 "62 ne qui vient" forces 62 singular at kill grade; @1704 needs
plural; no uniform number survives; the @1704/@508 tension is a conditioned
question). 26 word-internal: single window + loads on 94='ne' STRONG LEAD
(not granted) → not kill-grade; R19-178 conditioned-class precedent
required ≥2 frames. HELD. 62 plural-subject: conditional on fusion +
94='ne' lead; 62's value/class open; R19-106's 'il' kill stands. HELD.
26=["noun","lead"]; 62's cell absent; 88's value open; §7 intact — 67
et/veut remains the sole true polyvalence, R24 the sole declared
exception. Carry-forward (values for 88): @1706 constrains 88 to compose a
3pl "-nent" verb with word-internal 26 (locus parse); the uniform
vient-family stem is KILLED, so 88's value cannot be a global vient-family
stem; 88's value remains open. Registry: none.

### R20-115: resid-1097-1389-escalate — FENCE (confirm R19-129)
Decision: the @1097/@1389 ("06 29 67") hard residual is genuine; fenced
with stated cause (confirm R19-129's fence). Dissolution requires red-team
re-valuation of 67 or 06 — not taken today. Re-derived: 0-based @1096–1098
and @1388–1390 = "06 29 67"; the trigram occurs exactly x2. Arm B
("eret"/"erveut") killed at lexical grade (67 = 'et'/'veut', sole
polyvalence — re-valuing 67 is a red-team act); Arm A (06≠'-ent') yields no
parse under any variant; exhaustive segmentation leaves non-words at every
boundary. enterre-37re-s5 KILL closes the 37='re' escape for the sibling
@1816 window. Carry-forward (values for 88): no direct 88 constraint; the
fenced "06 29" region bounds 86's left context (@1099/@1391 "86 29"),
which matters for 86's value. Registry: none.

### R20-116: redteam-889-pourvoient — GRANT (mechanism: one word; STANDING REVISION)
Decision ("adjudicate mechanism — one word vs clause boundary; state which
mechanism the bytes support"): the bytes support ONE WORD: "pourvoient"
(00+86+06). The standing red-team clause-boundary fence ("00 86 | 06 77",
crowd5 rulings) is LIFTED at @889 — revision with new byte-level evidence.
M1's falsifier-exclusion is preserved, strengthened: under "pourvoient"
no "86→06" word-bigram exists at all. Re-derived: @886–892 =
"03 02 00 86 06 77 76" → "[03] [02] pourvoient le [76]" (subject + 3pl
finite verb + direct object; "pourvoir" vt. = to provide/supply —
diplomatic register, "pourvoir un poste"). Spelling byte-exact: 00='pour'
(A9 granted) + 86='voi' + 06='ent' (R17-007 promoted) = p-o-u-r-v-o-i-e-n-t.
86='voi' independently grounded: 86→29 x4 re-derived (@431 "77 86 29" =
"le voir"; @1375/@1825 "00 86 29" = "pour voir"; @1391 "67 86 29" =
"veut voir", 67='veut' positional) — two independent compositions, one
stem. 86→06 hapax @889 re-derived (confirms the red-team observation;
explained: no bigram exists). "00 86" x12 re-derived; @889 the sole
"00 86 06". Clause-boundary rival dead: "pour [86] | [06] [77]" =
"pour voir ent le" — "pour"+finite ungrammatical; elision rescue
contradicted by 77='le'. Precedent for granted-group word-internal prefix:
70='pre' in "première" (pencil gloss). The queued val-86-728-entr ('entr'
hypothesis) is untested and does not contradict the demonstrated local
'voi' composition; 86's global value stays open (redteam-86-split-docket
queued). Note: R19-135's terse "GRANT" did not answer the mechanism — this
ruling closes the docket bar's question. 86=["INF","cls"]; "pourvoient" is
word-internal composition, not a value promotion. Registry: none.

### R20-117: redteam-43-polyvalence — REJECT (confirm R19-064)
Decision ("(a) noun legs confirmed or overturned on bytes; (b) the @21
'[43]er' infinitive accepted as a second 43 value or re-segmented
grammatically"): (a) the 15 noun legs stand (R19-045's class grant
unchallenged); (b) the @21 infinitive is NOT accepted as a second value —
no polyvalence declared (§7 DOA); @21 stays fenced ('en' word-internal vs
verb-stem "me [43-stem]er", both live, neither declared). Re-derived:
@20–22 = "82 43 29"; 82-43-29 trigram x1 stream-wide; n(43)=16. No new 43
verdicts since R19-064 — every 2026-10-08/09 43 verdict was adjudicated in
R19-045/046/047/184. The attacker's byte kill stands unrebutted ('mener'
not forced; frame leans on unratified 98='vient'; verb-stem rival live;
'en'@21 circular). §7 intact. 43=["noun","cls"]; @21 excluded per _meta.
Registry: none.

### FAM-K: P1 decisions — classes, splits, polyvalence (R20-118–136)

### R20-118: ne-06-polyvalence-question — REJECT (confirm R19-105)
New post-R19 evidence strengthens the rejection: pas-ent-shift-survey KILL
— 06's stranding is consistent across all four "30 06" windows; the
word-placement discriminator is rejected at battery grade. No window exists
where 'ent' fails AND 'ne' uniquely succeeds (§7 bar); @1327 ("30 06 62
94", re-derived) hard-fences 'ne' at kill grade. 06 keeps single value
'ent' (R17-007 intact); "30 06" x4 stay fenced genuine residuals; 06→77 x6
windows stay under single-value 'ent'. Registry: none.

### R20-119: poly-60-redteam — FENCE (confirm R19-090)
No new post-R19 evidence on 60's item-hood (no item-hood battery landed).
The bar is unmet at kill grade: adjective arm still has zero unconditional
legs (@454 loads on provisional 77; @690/@1644/@1674 load on 03-nominal,
contradicted by R19-178; @995 verb-ambiguous); verb arm's one unconditional
forcing window (@1338) stands; @197 contested (R19-086 vs R19-087); the
verbal side is ≥3 ways per R19-088 (binary misdescribes). Declaration
conditions unchanged: (1) homophony route killed or item-hood test run;
(2) @700 re-based on granted premises or @1338 phase contest resolved;
(3) positional rule covering all 18 windows across three arms.
Registry: none.

### R20-120: redteam-94-functional-split — REJECT/CLOSED (confirm R19-167)
New post-R19 evidence enters the closed record as consistent support, none
of it re-opens: nementent-W2-subject PROMOTE (both "94 82 06 06" windows
share one subject account — subjectless; package explicitly requests no new
red-team act); mentent-w2-killseek KILL ("ne mentent" one-word rival dead
at W2 @1182–1187, 12 rescue routes exhausted); mentent-580-rival W1 kill
stands. 94's value is the single syllabic spelling "ne" (STRONG LEAD);
word-final "-ne" is segmentation, not value. 67 et/veut remains the SOLE
true polyvalence. The split question stays CLOSED. 94=["ne","lead"].
Registry: none.

### R20-121: poly-80-docket — FENCE (confirm R19-120) + RATIFY modal-80 kill
New post-R19 evidence ratified: modal-80-license KILL at battery grade —
17-window census re-derived exact; zero infinitive-shaped followers of 80
stream-wide; the sole near-candidate @565 fails on the adjacent-finite
conflict ("24 80" under R24). RATIFIED as a standing kill: the modal-80 arm
is dead; per inf-97-567-adjudicate's consequence clause the INF reading at
@567 ("80 97" under modal-80) is now KILLED, not strained. Also ratified:
80-value-host-w2 NULL (80's value unnameable at @1322 across 7 routes) and
80-inf-transfer-1322 KILL (no uniform infinitive transfer across the three
"03 29 80" windows; frame66-vient-80 @768-scoped PROMOTE untouched). The
declaration bar is still unmet: no kill-grade byte evidence for a second
80 class; the word-internal-80 rival unfalsified; W1's imperative reading
stays conditional (provisional-77 + unlicensed boundary); W2's determiner
reading stays locus-conditioned on offset PROBABLE-WEAK a6_09. 80's global
class stays verb-frame per A8. 80 absent from registry. Registry: none.

### R20-122: adjudicate-1560-fence — CONFIRM R19-193
No new evidence. R18-004's promote stays downgraded to findings+fence:
the "ne [52]" dual-spelling frame and "30 06 60" left-independence stand
as findings; the "pas [06]" interior stays fenced; Clause 2b is @1733-local.
Registry: none.

### R20-123: redteam-86-split-docket — FENCE (confirm R19-134: package granted, declaration held)
New: clitic-86-77-windows KILL (86=object-clitic dead at @951 on granted
96='par' — pre-R19, consistent with the package). The segregation table,
uniformity results, and the homophone-set candidacy rejection per the
{33,86} criterion stand as packaged. No declaration-grade evidence
(positional split vs polyvalence vs homophone set) has landed. Declaration
conditions: kill-grade byte evidence for two 86 values, or a positional
rule covering the partition. 86=["INF","cls"]. Registry: none.

### R20-124: redteam-la-tout-fence — FENCE (confirm R19-189)
"11 79" @52-53 re-derived byte-exact; kill-grade ungrammatical under
banked 11='la' + 79='tout'. New: la-400-residual NULL (@400 'la' fenced as
canonical-offset object) — unlocks no exit. The three exits stand: (a)
banking revision inconceivable (11='la' crib-backed); (b) a1_01
segmentation — seg-a1_01-offset1-test (P2) still queued, must beat +6.49
LOO; (c) accepted hapax stays open. @997 "la par" remains in the
banked-value contradiction docket with it. Registry: none.

### R20-125: redteam-62-conditioned — REJECT (confirm R19-106)
New: ne-scope-62-indet NULL — 0/5 '62 94' windows' finite verbs nameable at
battery grade; the distributional-only fence on '62 94' = subject+'ne'
HARDENS. The conditioned 'il' lead stays REJECTED (§7-DOA per R17-022;
@508 unclean); 'il' stays KILLED at kill grade, permanent. 62's cell stays
absent. Registry: none.

### R20-126: poly-20-docket — FENCE (confirm R19-036)
New: particle-20-value-rivals NULL — no battery-grade left-context frame
separates 'mais' from 'or'/'donc'/'cependant' at @760/@839 (the exact
ordinal-ellipsis frame favors 'mais' 5-0-0-0 but is underpowered at
P≈0.48; the 'donc'-needs-premise shortcut died on genuine counterexamples).
'mais' remains the routed candidate; the value is unnamed. R24 noted as
context (24=finite/modal outside the five 'en' windows) — no impact on the
20 docket. Candidacy recorded; polyvalence NOT declared; T1/T2/T3 triggers
for R21. 20 has no cell. Registry: none.

### R20-127: poly-33-redteam — CLOSED (confirm R19-053)
No new evidence. The attacker's R19 kill stands: whole-word and stem faces
of val-33-verb have non-empty intersection — one lexeme covers all 25
windows (R17-018 spelling duality); 'penser' is lead exemplar, not unique.
No polyvalence, no homophone split. 33=["INF","cls"]. Registry: none.

### R20-128: r-et3-vs-positional-redteam — CONFIRM R19-192
No new evidence. R_et3 RETIRED; §7 positional rule ("veut" iff follower
infinitive-shaped) exceptionless 5/33; @1390="veut". R_et1 at @272/@1476
still not ruled (separate item). Registry: none.

### R20-129: 24-redteam-adjudication — CONFIRM R19-191 (R24 declared)
New: neque-tail-24-85-clause PROMOTE is consistent with R24 (85 licenses a
verb-stem parse with [24] as licensed 'en'-clitic dependent). Re-derived:
24-85 bigrams x5 @732/@955/@1438/@1693/@1754. No contradicting evidence.
R24 stands: 24='en' iff follower=85; 24=finite/modal verb elsewhere;
R17-009 scoped; R18-008 narrowed. 24=["verb","cls"]; R24 in _meta/protocol.
Registry: none.

### R20-130: ceci-77-redteam — FENCE
The "ceci" hypothesis (77="ci" at the three "ce"+77 contacts) requires a §7
polyvalence declaration. "87 77" x2 @515/@869 and @611 "47 77 87"
re-derived byte-exact. New: celle-7780-fusion-515-869 KILL removes the
"celle" fusion rival (different composition — does not kill "ceci" but
narrows the field). The "ceci [80/89]" subject parse needs finite-80/89 —
both unlicensed (80's value open per R20-121's ratifications; 89 is
noun-LEAD with the infinitive rival killed, R19-161). No kill-grade byte
evidence for "ci" as a value exists. The le/ci split is NOT declared.
Declaration conditions: (a) battery-grade finite-80/89 naming making
"ceci [80/89]" the unique parse, or (b) kill-grade proof that "ce le" is
ungrammatical with no other rescue. 77=["le","prov"]. Registry: none.

### R20-131: le-77-residual-adjudicate — FENCE
77="le" provisional SURVIVES; the three "ce"+77 windows (@515/@611/@869)
stay fenced as residuals. The "ce le" windows do NOT force a conditioned
split at kill grade (a conditioned split = a second polyvalence; the
ungrammaticality is fenced, not forcing, while the "ceci" reading and
word-internal alternatives are live-but-unproven). Neither merge nor split
is declared now. Merge condition: the queued 80/89-verb battery (F104
docket linkage). Split condition: kill-grade "ci" evidence per R20-130.
77=["le","prov"]. Registry: none.

### R20-132: par-pour-redteam — CONFIRM R19-190 (split ruling stands)
New: pour-prefix-00-census KILL — rescue 2c dead at kill grade (00 as
syllabic prefix "pour-" killed stream-wide), which hardens R19-190 by
closing the prefix rescue of "96 00". Standing: global 00='contre' kill
ratified; A9 00='pour' stands ("pour que" x4); "96 00" positional ("par
contre" @47/@465/@960) stays FENCED as live conditional — grammatical with
Littré 1873 attestation, "par pour" ungrammatical under A9; NOT declared
as a second polyvalence (x3, other-preposition space untested, §7 bar
unmet). Registry: none.

### R20-133: redteam-79-split-docket — FENCE (confirm R19-119, evidence strengthened)
New: o79-adjudicate PROMOTE ratified — the 5 O-windows adjudicate as
2 W-conditional / 2 S / 1 O-remains: @883 W (conditional on 68 masculine),
@1010 W (conditional on 80 non-finite), @1364/@1688 S (new systematic "ne
tout" S-shape; "94 79" x2 re-derived byte-exact), @496 O-remains (gated on
queued subj-42-ne-frame). New tally: W=11 (9+2 conditional), S=6 (4+2),
O=1. The split hypothesis survives and gains a second systematic S-shape
alongside "tout fois", but the declaration bar — a demonstrated
syllabic-79 second life at kill grade (syl79-wordname still pending) — is
unmet. Monovalent word-'tout' still covers 11/18. The "toutefois"
composition (79="toute"+17="fois") at @451/@1460 stands as granted
window-local compositional allomorphy, not a §7 polyvalence. 79="tout"
banked value STANDS. 79=["tout","prom"]. Registry: none.

### R20-134: split-13-redteam — FENCE
New: letter-13-verdicts KILL ratified — 13 as word-final "s"
("verdicts") killed at kill grade by the forced "ce verdicts"
determiner-number mismatch at @573 ("78 45 13 55 61" x2 re-derived
byte-exact; 87='ce' forced determiner; 78-45="verdict" promoted).
R19-170 (reseg-13-armA, conditional segmentation) stands. The §7 split
candidacy (verb-window values vs @568 nominal contact) is packaged with
this new evidence, but the declaration bar — kill-grade byte evidence for
TWO 13 values — is unmet: the sub-lexical word-final arm is dead,
word-internal/initial arms live, no values named. Declaration conditions:
(a) two named 13 values each with kill-grade window evidence, or
(b) reseg-13-armB landing. 13 absent from registry. Registry: none.

### R20-135: split-69-adjudicate — FENCE
The @1115 modal-inf leg is the sole verbal-69 window and is contested: the
cela locus parse (R19-108, GRANT locus-level: "69 11"="cela" @1115-1116,
clause boundary before 88) is the standing disposition, and the modal-inf
reading ("pas [69-modal-inf] la [88-inf]") has not displaced it. @1115
context re-derived: "38 30 69 11 88". The 97-tie evidence
(redteam-97-tie-adjudication PROMOTE package: INF 6 legs / NOM 4 windows,
tie genuine, class decision red-team venue) supplies NO second verbal-69
window — the tie leaves @1412 unresolved in both directions, not verbal.
No kill-grade evidence for a second 69 value; even a conditioned
subset-scoped split is unwarranted on one contested window (R18-022
precedent required 8). 69=["noun","cls"] with 'ce' value-lead
(R19-109/110). Declaration conditions: (a) battery-grade refutation of
the cela parse at @1115, or (b) a second independent verbal-69 window.
Registry: none.

### R20-136: redteam-62-split — FENCE (split candidacy rejected as framed; strain evidence banked)
New post-R19 package: scope-62-verb-noun NULL (35 windows classified:
2 forced stem-verbal @665/@1536 via the 06 decision rule, 1 lean,
8 nominal, 21 ambiguous/strained, 2 residual twins @1362/@1686; 8/9 of
the 62-94 family strained under {règn-,trôn-}) and 62-boundary-census
PROMOTE (35-window boundary census: 1 forced boundary @46-right, 1 forced
no-boundary @1349-left via bound-letter 34='i', 68/70 sides undetermined
with stated cause; '62 94' x9 re-derived byte-exact). The candidacy AS
FRAMED ('il' vs {règn-,trôn-}) is dead on arrival: 62='il' was KILLED at
kill grade in R19-106 (permanent — no future 'il' claim without new byte
evidence overturning the kill), and the scope battery's
"demonstrated-but-unpromoted 'il'" framing predates that kill. No second
value is nameable; §7 bars the declaration. The 62-94-79 twins
(@1362/@1686, "62 94 79 14 60" x2 re-derived byte-exact) are genuine
residuals; the 62-94 family's strain is banked as live docket evidence.
FENCE, not close: a future split candidacy needs a named rival other than
'il' (e.g. ne-scope-62-indet's follow-ups: ne-W6-pas-verb,
ne-W8-06-word, ne-scope-62-W7-residual). 62's cell stays absent.
Registry: none.

§7 standing: 67 et/veut remains the sole true polyvalence; R24 the sole
declared exception.

## B. Carry-forward disposition

| Item | Disposition |
|---|---|
| @197 full-clause call | DEFER — no new byte evidence in this round's docket; the @197 contest (R19-086 vs R19-087) is unresolved; needs a dedicated target. |
| poly-60 item-hood | FENCE (R20-119) — confirm R19-090; declaration bar unmet. |
| 42 polyvalence venue | DEFER — the venue is a queued red-team target, not in this docket. New evidence banked: val-42-det-gap restricts 42's value inventory to bare-capable nouns (proper nouns adopted; pronoun-class 'rien'-family escalated per §5, R20-081). |
| 03 and 71 §7 splits | DEFER — no docket item owned them; R19-178 (stem-03) and R19-186 (71 split-candidate) stand on their own dockets. |
| load-bearing 77="le" | FENCE (R20-130, R20-131) — provisional SURVIVES; "ce"+77 windows stay fenced residuals; neither merge nor split declared. |
| provisional 59="est" | UNCHANGED — no new evidence in this round's target set; stays provisional. |
| 78="ver" | DEFER with cause (R20-032–038) — R16-005 LEAD stands; the @819 "ce verre" leg banked for the red-team settle decision; settle conditions: 45='dict' resolved or R19-172's grant conditions met. |
| 65 gender / 32 duality | DEFER with cause (R20-039–047) — @65 word-final fence hardens (R20-047); gender unnamed; ownership with the 32-duality docket. |
| "la tout" exits | FENCE (R20-124) — confirm R19-189; three exits stand. |
| positive legs for 83="de" | OPEN (R20-109) — conditioned LEAD stands; the 4-leg restock unchanged; no new positive legs found. |
| values for 88 | OPEN — @1706 constrains 88 to compose a 3pl "-nent" verb with word-internal 26 (locus parse, R20-114); the uniform vient-family stem is KILLED; 88's value remains open. |
| values for 93 | DEFER with cause (R20-039–047) — no new byte evidence; R19-166's class grant stands. |
| values for 98 | KEEP AT LEAD; DO NOT GRANT (R20-039–047) — 'vient' not uniquely forced; R19-172's rejection reasons stand; grant conditions: 83='de' ratification or doubled-98 cause resolution. |
| reseg-1481-98 | DEFER — queued battery venue (no docket item owned it); no evidence in this round. |
| 62 split package | FENCE (R20-136) — candidacy as framed dead on arrival ('il' killed); strain evidence banked; future candidacy needs a named rival other than 'il'. |
| 58 conflict package | FED, not decided — R20-094 (corpus arm), R20-095 (frame-C hardening), R20-096 (core input package, weigh under R24); 58=["nominal","cls"] stands; value decision open. |
| doubled-consonant package | FED (R20-073) — compositional account packaged; evidence only. |
| 41 split package | FED, not decided — R20-108 (per-value incompatibility package), R20-082 (doubling confirmed stream-real); split decision is the queued split-41-redteam target. |
| 79 W/S evidence | FENCE (R20-133) — confirm R19-119, evidence strengthened (W=11/9+2c, S=6/4+2, O=1); split declaration bar unmet. |
| 97 INF/NOM tie | SURVIVES at the four 'pour [97]' windows (R20-039–047) — INF-97@525 killed (R20-045); the tie is genuine at battery grade; deciding venues live and queued. |
| post-R19 modal-80 kill | RATIFIED (R20-121) — modal-80 arm dead at kill grade; @567 INF reading KILLED. |
| post-R19 "ne mentent" kill | RATIFIED (R20-120, R20-105) — "ne mentent" one-word rival dead at both windows; 94-split stays CLOSED. |

## C. Registry deltas

None. Zero cell changes this round: no value named, no class changed,
no split declared, no polyvalence granted. Cells stand at 50/96 per R19's
accounting. The sole standing revision is the @889 mechanism ruling
(R20-116): the clause-boundary fence is lifted in favor of the one-word
"pourvoient" parse — a locus parse, not a registry entry.

_meta notes: 40 = free letter, word-final-dominant (R20-075); 52="a" =
the seg-528294-word composition's letter premise, word-unit scope only
(R20-071); val-42-det-gap's pronoun-class 'rien'-family leg escalated to
the R20 42 venue per §5 (R20-081); 62-boundary-census new observations
(@1349 forced no-boundary, @1482's 46-gap, @849 row join) feed any future
62-split candidacy (R20-076); R24 declared protocol (R20-129).

## D. Orphan sweep

108/108 promotes covered: FAM-A 19 + FAM-B 12 + FAM-C 7 + FAM-D 9 +
FAM-E 11 + FAM-F 10 + FAM-G 14 + FAM-H 19 + FAM-I 7 = 108. 0 orphans.
28/28 P1 red-team decisions covered: FAM-J 9 + FAM-K 19 = 28. 0 orphans.

## E. Ruling tally

136 rulings: GRANT 65 · GRANT-WITH-CORRECTIONS 16 ·
DUPLICATE/CONFIRM/NO-NEW-DELTA 31 (standing rulings) · REJECT 10 ·
FENCE 13 · CLOSED 1. Sum: 65+16+31+10+13+1 = 136. 0 orphans.
0 registry changes.

## E. Ruling tally

136 rulings: GRANT 65 · GRANT-WITH-CORRECTIONS 16 ·
DUPLICATE/CONFIRM/NO-NEW-DELTA 31 (standing rulings) · REJECT 10 ·
FENCE 13 · CLOSED 1. Sum: 65+16+31+10+13+1 = 136. 0 orphans.
0 registry changes.

Composition: promotes confirmed (GRANT/GWC) 81; standing confirmations
31; fresh REJECTs of promotes 4 (R20-027, R20-028, R20-038, R20-093);
fresh FENCE of a promote 1 (R20-080). P1 decisions: 5 GRANT-family
(R20-109, 112, 113, 114, 116), 6 REJECT (R20-110, 111, 117, 118, 120,
125), 1 CLOSED (R20-127), 12 FENCE (R20-115, 119, 121, 123, 124, 126,
130, 131, 133, 134, 135, 136), 4 CONFIRM (R20-122, 128, 129, 132).
Carry-forward DEFERs: 7 (78='ver', 93 value, 65 gender, @197, 42 venue,
03/71 splits, reseg-1481-98).

## F. Pipeline flags for the supervisor

1. det-87-644-function's queue entry still reads result: promote against
the standing R19-138 FENCE (R20-091). Same class of anomaly as R19-028's
pre-banked verdict note.
2. a-39's queue verdict reads "promote"; red-team standing is R17-005
LEAD (allophone tier) — do not upgrade (R20-010).
3. ne-94's queue verdict reads "promote"; standing is R17-001 REJECT
(STRONG LEAD, confirmed R19-167) — not ratified (R20-007).
4. ne-1331-70-52-parse's REJECT (R20-027) withdraws the @1331 resolution
claim; the window is fenced with arm A conditional on 52's
prendre-family resolution — feeds the queued 52-value work
(adj-52-37-value-rerun), not this round.
5. ne-W6-pas-verb's REJECT (R20-028) withdraws the W6 C1 re-open
consequence; ne-scope-62-indet's C1 stays as it was.
6. Queue report-path metadata: doubled `code/crowd17/code/crowd17/`
prefixes on comedy-skew/drama-n3/drama-grade entries and a doubled
`code/crowd17/code/crowd17/report_inbox/processed/processed/` path on
nementent-W2-subject — harmless path metadata, worth a one-line repair.
7. The queue holds a byte-identical sibling pair seg-81-30-trepas-kill /
seg-81-30-trépas-kill (é vs e), both verdict/kill — consider merging to
prevent re-dispatch.
8. No standing R15–R19 verdict is contradicted or downgraded by any
ruling in this round. §7 intact: 67 et/veut remains the sole true
polyvalence; R24 the sole declared exception.
