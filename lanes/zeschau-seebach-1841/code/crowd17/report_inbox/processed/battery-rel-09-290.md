# Battery verdict: rel-09-290

## Bar (verbatim, pre-registered)

"discriminate the 97-09 boundary and name 09's nominal value"

Task-brief numbered clauses (derived from the claim before testing):
- C1: parse @290 with 09 as 'qui'-antecedent under standing values.
- C2: name 09's value iff the antecedent role is forced with zero new assumptions.
- C3 (else-branch): fence with stated cause.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/rel-09-290.lock` on start
(deleted on completion). Re-derived the repaired stream from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(parsed per `repair_parse.py`): 1,847 pairs / 96 types verified.
`canonical.py` never touched. R5005, sealed gates, red-team adjudication
queue untouched.

Offsets below are 1-based @. Standing values used: GT 11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout,
00=pour, 84=on, 47=ce; provisional 59=est, 77=le; kills honored incl.
09/92 "-ère" (A6, not re-litigated); holds honored incl. 09~92 (A6).

## Window-level evidence (all re-derived from bytes)

**@290 (target):** row a2_03, `89 28 00 97 [09] 64 29 40 65 16 01 11`
= "…[28] pour(00) [97] [09] qui(64) [29=er][40=e] [65]…".
Wide context @280–306 confirmed; no anomaly in phase.

**Parallel frame @688:** row a5_00,
`07 00 92 64 29 40 65 94 29 60` = "…[07] pour(00) [92] qui(64) [29][40][65]…".
Same skeleton: "pour [NP] qui [29][40][65]". Antecedent NP is a single
group (92) here vs two groups (97 09) at @290.

**Verb-unit recurrence @1713:** row a8_06, `06 29 40 65 94 44 59` —
"29 40 65" occurs WITHOUT preceding 64. The verb unit is independent;
64 is a standalone word, not a syllable of a longer "quière"-type word.
This kills the word-internal rival "…[09]qui[29][40]…" at battery grade.

**97 census (n=10):** 97 and 09 are separable words — non-adjacent at @589
(`14 00 97 41 41 [09]`, row a3_02: "…pour [97] [41] [41] [09]"), and each
occurs without the other (97 at @95/@300/@526/@567/@752/@1413;
09 at its 11 other windows). So at @290 the boundary is "97 | 09".
@95 (`81 97 46 29 85` = "…[81] [97] que(46)…") forces 97 nominal
("[det] que" is ungrammatical; noun + "que"-relative is clean).

## Per-clause results

- **C1 (parse @290 with 09 as 'qui'-antecedent): PASS.** Under standing
  values the window reads "…pour [97] [09] qui [verb: 29-40-65]…" — a
  textbook relative clause; the NP "97 09" is qui's antecedent, hence
  nominal. The @688 parallel ("pour [92] qui [29][40][65]") confirms the
  construction with byte-identical verb unit. Interrogative-"qui" rival
  fenced: it demands a full sentence break inside the "pour"-PP
  ("…pour [97] [09]. Qui [V]…?") — an unmotivated fragment, required twice
  in identical shape (@290, @688). Word-internal rival ("quière")
  killed by @1713.
- **C2 (name 09's value with zero new assumptions): FAIL.** Naming needs:
  (i) 97's class — determiner ⇒ 09 is the head noun; noun ⇒ 09 is a
  post-nominal modifier (adjective/appositive) and the head is 97 —
  undetermined (@95 forces nominal only, not noun-vs-determiner);
  (ii) the verb "29 40 65" identified — 65's value is open per queue;
  (iii) any lexical evidence for 09 — none exists in standing ground
  truth. Zero-assumption naming is impossible.
- **C3 (else-branch): FIRES — fenced.** 09 is nominal at @290 (member of
  the qui-antecedent NP "97 09"), but its value and its head/modifier
  role stay open. The 97-09 boundary discriminates to two separable
  words ("97 | 09"), not one.

## Adverses

None listed.

## Standing-state check

No standing verdict contradicted or downgraded. Notable consistency (not a
claim): the parallel antecedent slots — 09 at @290, 92 at @688 — sit well
with the standing 09~92 HOLD (A6); flagged for red-team awareness only.

## Verdict: NULL (fence executed per C3)

## Follow-ups proposed (for supervisor queuing)

1. `class-97-determiner` (P3): discriminate 97's class (determiner vs noun)
   via @95 "[97] que" and @589 "pour 97 41 41 09". Decides whether 09 is
   head noun or post-nominal modifier inside the @290 antecedent NP.
2. `verb-294065-identify` (P3): identify the finite verb "29 40 65"
   recurring @294/@688/@1713 in the frame "qui [29][40][65]"; names 65's
   value via this verb slot. Unlocks the @290/@688 relative clauses.
3. `np-97-09-modifier` (P3): test 09 as post-nominal modifier — census
   "97 09" adjacency vs separation and compare post-nominal 09 windows
   (@1263 "01 09 11", @519 "80 09 70") for a modifier signature.
