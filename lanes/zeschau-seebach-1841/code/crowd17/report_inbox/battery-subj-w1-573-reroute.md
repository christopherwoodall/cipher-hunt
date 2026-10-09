# Battery report: subj-w1-573-reroute

Target: `subj-w1-573-reroute`. Claim: W1's 'ne mentent' 3pl subject is found
via a non-13 route.
Date: 2026-10-09. Worker: 31c3b65b-4f33-4661-a8de-602bff9382b6 (battery worker).
Lock `locks/subj-w1-573-reroute.lock` created 2026-10-09T04:56:42Z (no
pre-existing lock for this id); deleted on completion.

Offset convention: @n below = 1-based pair index in the repaired 1,847-pair
stream.

## Bar (verbatim, pre-registered)

"(a) parse 'ce verdict [13] [55-61] ne mentent' with 13's value held open
(neither determiner nor pronoun); (b) coordinate with subj-55-61-word's kill
(55-61 verb-shaped) and the pronoun-13-les kill - no duplication; (c) name
the 3pl subject with the clause boundary stated, or confirm W1 subjectless
as a fenced residual"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. The frame 'ce verdict [13] [55-61] ne mentent' parses with 13's value held
   open (neither plural-determiner nor object-pronoun).
2. Coordination with subj-55-61-word's kill (55-61 verb-shaped) and
   pronoun-13-les's kill is honored — both adopted as premises, not
   re-litigated, not duplicated.
3. Either the 3pl subject of "ne mentent" is NAMED with the clause boundary
   stated, or W1 is CONFIRMED subjectless as a fenced residual with stated
   cause.

## Method

Read BATTERY-PROTOCOL.md first. Created/deleted the lock per protocol.
Re-derived the repaired 1,847-pair / 96-type stream from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed per `code/side-keyhunt/repair_parse.py` (asserted 1,847 pairs /
96 types before testing). `canonical.py` never used. R5005, sealed gates,
red-team queue untouched. Every number traces to the stream (analysis
script `/tmp/reroute_parse.py`, session-local).

Standing values used (protocol section 7 + battery verdicts): banked GT
11=la, 82=m, 29=er, 40=e, 46=que; granted 87=ce, 47="ce" (A4), 00="pour"
(A9), 84="on" (A15); promoted 94="ne" (STRONG LEAD R17-001), 06="ent"
(R17-007 conditional), 30="pas", 65=noun-class, 76=noun masculine;
provisional 59="est", 77="le"; leads 78="ver" (R16-005), 45="ce/dict"
(A11 HOLD); kills: plural-determiner-13 (subj-13-value, kill grade),
'les'-pronoun-13 (pronoun-13-les, kill grade at @567), plural-noun-55-61
(subj-55-61-word, kill grade); promotes: 55-61 verb-shaped "prend"
(seg-55-61-21-stem), 45="dict" sole host "verdict"
(dict-45-host-inventory); 67 et/veut sole true polyvalence.

## Window-level evidence (re-derived)

W1 — row a3_02, 1-based @559-590 (32 pairs):
`94 59 30 67 11 43 24 80 97 13 76 45 94 52 | 87 78 45 13 55 61 | 94 82 06 06 |
50 10 19 18 14 00 97 41`
= "ne(94) est(59) pas(30) et(67) la(11) [43] [24-verb] [80] [97] [13]
[76-noun] [45] ne(94) [52] (fragment, verb never arrives) | ce(87)
verdict(78-45, LEAD, certified sole host) [13: OPEN] [55-61: verb-shaped] |
ne(94) mentent(82-06-06, 3pl per conditional R17-007 grant) | [50] [10]
[19] [18] [14] pour(00) [97] [41]"

Key token positions (1-based): 87@573, 78@574, 45@575, 13@576, 55@577,
61@578, 94@579, 82@580, 06@581, 06@582, 50@583.

Censuses re-derived: '78 45 13 55 61' exactly x2 (@574, @1165);
'94 82 06 06' exactly x2 (@579, @1183); '55 61' exactly x3 (@577, @1168,
@1206); 50 n=11.

50's profile (re-derived): pre {44, 92, 11x2, 80, 06, 86, 02, 07, 71, 93};
suc {88, 45x2, 82, 78, 10, 80, 40, 46, 29, 42}. Heterogeneous — no
pronoun-shaped contact.

W2 cross-check — row a6_09 (1-based @1154-1173):
`00 92 29 80 17 77 82 44 83 21 67 78 45 13 55 61 94 87 83 21`
= "…verdict(78-45) [13] [55-61] ne(94) ce(87) [83]…" — the '94 87' hapax at
@1170-1171 (see Adverses). Row a6_10 (1-based @1174-1191):
`85 36 74 32 48 59 37 77 78 94 82 06 06 59 …`
= "…le(77) ver[78] | ne(94) mentent(82-06-06) | est(59)…" — @1181-1182
"le ver" (singular), @1183-1186 "ne mentent", @1187 "est".

## The parse (bar clause 1)

"ce(87, granted) verdict(78-45, LEAD) [13: value open — plural-determiner
killed (subj-13-value), object-pronoun killed (pronoun-13-les)] [55-61:
verb-shaped, finite 'prend'-type, 3sg agreeing with 'ce verdict', per
subj-55-61-word kill + seg-55-61-21-stem promote under the section 7
one-value rule] ne(94, STRONG LEAD) mentent(82-06-06, 3pl per conditional
R17-007 grant) [50] …"

Reading: "this verdict, [13] takes; they do not lie …" — two finite verbs
with incompatible agreement (3sg vs 3pl) cannot share one clause or one
subject. The "ne mentent" clause (@579+) is structurally separate from the
"ce verdict [13] prend" clause (@573-578).

## Subject-slot exhaustion (bar clause 3, first arm)

Every grammatically possible 3pl-subject slot for W1's "ne mentent",
tested against standing values:

1. "ce verdict" (@573-575): singular. "verdict" is the certified sole host
   of 45="dict" (dict-45-host-inventory); 87="ce" is granted singular. A
   singular subject with a 3pl verb is ungrammatical in French at any
   period. CLOSED.
2. [13-55-61] as 3pl NP: triply closed. (i) 13's plural-determiner arm
   killed at kill grade (subj-13-value: 13->24 x3 / 13->93 x2 force any
   plural determiner false). (ii) 13's object-pronoun arm killed at kill
   grade (pronoun-13-les: @567 "97 les [76-noun]" forces 'les' false;
   section 7 one-value). (iii) 55-61 verb-shaped at kill grade
   (subj-55-61-word: W3 forces "prend"; section 7 one-value extends to
   W1) — a verb cannot head a subject NP. CLOSED.
3. [13] alone as 3pl subject: the bar holds 13 open as neither determiner
   nor pronoun; no remaining lone-13 value is 3pl-subject-capable (@567's
   76=noun wall stands; a bare common-noun 13 would violate French
   determiner requirements). CLOSED.
4. Post-verbal 50 as inverted subject ("ne mentent-ils?"): 50's
   re-derived profile (n=11) shows no pronoun-shaped contact (successors
   heterogeneous: 88/45/82/78/10/80/40/46/29/42); and W2's "ne mentent"
   is followed by 59="est" ("ne mentent est"), which kills inversion as
   the general account of the x2 frame. FENCED with stated cause
   (not kill-grade: 50's value stays open).
5. Pro-drop / implicit 3pl subject: ungrammatical in French. CLOSED.
6. Cross-row subject: a3_01's tail ("47 46 55 81 00 86 59 34 17 86") and
   a4_00's head ("41 09 00 92 79 85 01 29 40 03 39 26") contain no 3pl NP;
   declarative subjects precede their verb. CHECKED, absent.
7. Shared subject with the @559-561 "n'est pas" clause: that clause is
   itself subjectless ("ne est pas" with no "ce"/"il"). No 3pl NP.
   CHECKED, absent.
8. The @570-572 "[45] ne [52]" fragment: the verb never arrives; no 3pl
   NP in the fragment. CHECKED, absent.
9. W2 cross-check (@1183-1186): the only available subject is "le(77)
   ver[78]" (singular) — the identical gap. The subjectlessness is
   systematic across both "ne mentent" windows, not W1-local. CHECKED.

Result: no 3pl subject exists for W1's "ne mentent" under any standing
value. The first arm of clause 3 cannot fire.

## Clause boundary (stated per bar clause 3)

- Left: @573 (87="ce", granted) opens the nominal clause, following the
  "[45] ne [52]" fragment (@570-572) and the subjectless "n'est pas"
  clause (@559-561).
- Internal: the agreement mismatch forces a clause boundary between @578
  (61, "prend" 3sg agreeing with "ce verdict") and @579 (94, "ne
  mentent" 3pl). Two finite verbs with incompatible agreement cannot
  share a subject.
- Right: the "ne mentent" clause runs @579-582 through @583-590 ("[50]
  [10] [19] [18] [14] pour [97] [41]") past row end into row a4_00
  (@591: "41 09 00 92 …"); no sentence terminator is visible — right
  boundary indeterminate at battery grade.

## Adverses

1. "94='ne' STRONG-LEAD caveats (R17-001)": HONORED. 94="ne" is used as
   the particle throughout. Recorded caveat: both "ne mentent" windows
   are PARTICLE-STRAINED per battery-ne-particle-ungrammatical-sweep
   ("ne m'ent-ent", doubled 06, no stem); R17-007's conditional "ne
   mentent" grant is not re-litigated. The strained status is the red
   team's venue (94-duality adjudication), not a battery finding.
2. "'94 87' hapax at W2": ANSWERED. W2 a6_09 @1170-1171 "ne(94) ce(87)"
   is ungrammatical as particle+demonstrative — a 94-duality problem
   (94 possibly syllabic/word-internal at W2), fenced to the red-team
   94-duality adjudication with stated cause. It does not disturb W1:
   @579-580 "94 82" ("ne"+"m…") is clean particle position. The hapax
   adds strain to the frame but changes nothing in the subject analysis.

## Per-clause pass/fail

1. PASS. The frame parses with 13 held open (neither determiner nor
   pronoun): "ce verdict [13-open] [55-61-verb] ne mentent".
2. PASS. Coordination honored: subj-55-61-word's kill (55-61 verb-shaped),
   pronoun-13-les's kill (13 is not 'les'-pronoun), and subj-13-value's
   kill (13 is not a plural determiner) adopted as premises; nothing
   re-litigated, nothing duplicated. Consequence stated: the
   "les [55-61]" 3pl-subject-NP route is triply closed.
3. PASS via the second arm. The 3pl subject cannot be named — the slot
   space is exhausted (9 positions checked: 4 closed by grammar or
   standing kills, 1 fenced with cause, 4 checked absent) — so W1 is
   CONFIRMED subjectless as a fenced residual: "ne mentent" (3pl per the
   conditional R17-007 grant) with no overt 3pl subject under any
   standing value; the gap is systematic (W2 identical); both windows
   particle-STRAINED. Packaged for the red-team 94-duality / R17-007
   adjudication.

## Verdict: PROMOTE (finding grade)

W1's "ne mentent" clause is confirmed subjectless as a fenced residual at
battery grade. The non-13 route space is exhausted: "ce verdict" is
singular, [13-55-61] is triply closed as a subject NP, inversion /
pro-drop / cross-row / shared-subject routes all fail, and W2 shows the
identical gap. This closes the subject hunt at battery level; the frame's
strained status belongs to the red-team 94-duality adjudication.

Scope limits (explicit): names no value; re-grades no lead; declares no
polyvalence (section 7 intact); does not touch R17-007's conditional "ne
mentent" grant, R17-001, or any red-team verdict. No standing battery
verdict contradicted or downgraded (subj-13-value, pronoun-13-les,
subj-55-61-word, seg-55-61-21-stem, w1-573-subject all upheld — this
finding narrows w1-573-subject's null to a confirmed residual).

## Observations for the supervisor (not follow-up targets)

- The red-team 94-duality adjudication is now the live owner of the "ne
  mentent" frame: two subjectless clauses, both particle-STRAINED.
- value-13-third-arm (queued, P2) still owns 13's remaining value space,
  but it is now irrelevant to the W1 subject hunt (the subject is
  confirmed absent regardless of 13's value).

## Bookkeeping

- Report: this file.
- `battery-queue.json`: `subj-w1-573-reroute` queued -> verdict/promote
  (finding grade) via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write). Own entry only.
- Lock created on start (agent id + UTC), deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
