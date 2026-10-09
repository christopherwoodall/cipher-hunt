# Battery report: subj-42-qui — 'qui' @531 as 3pl subject of '[42]ent'

Target: `subj-42-qui`. Claim: 'qui' (64 @531) is the 3pl subject of '[42]ent'
with the relative clause spanning @531-544. Date: 2026-10-09.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed like `code/side-keyhunt/repair_parse.py`.
Never used `canonical.py`. R5005 untouched. No invented data.
@-offsets are 1-based. Lock `locks/subj-42-qui.lock` held for this run only.

Dependency: subj-42-w3 null (2026-10-08) follow-up #3. The w3 battery fenced
@544's left junction and left the "qui @531 as subject" rival untested. This
battery tests that rival only; it does not re-litigate w3's 44-29-48 bar.

## Bar (verbatim, pre-registered before testing)

"parse @528-550 as one grammatical period with 'qui' as subject, or fence"

Numbered clauses (fixed before testing):

1. The span @528-550 parses as one grammatical period under standing values.
2. Within that parse, 'qui' (64 @531) is the subject of '[42]ent' (@544-545),
   heading a relative clause spanning @531-544.
3. (Adverse) The relative-clause span @531-544 parses as one period: every
   token @532-543 is licit clause-interior material between a subject
   relative pronoun and its verb.
4. Scope: this battery tests only the qui rival; it does not duplicate
   subj-42-w3's 44-29-48 bar.

## Method

Re-derived @518-556 from the repaired stream (script, not w3's transcription).
Full census of 64 ('qui', granted value): n=47 with +-3 context each.
Identified every clean qui-subject frame licensed by granted/banked values
and measured qui-to-verb distance. Re-verified 44's determiner contacts
(77-44, 11-44) and scanned @532-543 for any finite-verb material.
Standing values used: granted 64=qui, 00=pour, 46=que, 47=ce, 82=m(letter),
84=on; banked 11=la, 29=er, 34=i, 40=e, 70=pre; provisional 59=est, 77=le;
battery-promoted (pending ratification) 12=n, 48=e, 06=ent.

## Window-level evidence (@-offsets, 1-based)

**Target span @528-550** (verified from stream):
`@528 44 @529 59 @530 37 @531 64 @532 26 @533 32 @534 16 @535 08 @536 24
@537 82 @538 16 @539 91 @540 12 @541 44 @542 29 @543 48 @544 42 @545 06
@546 00 @547 46 @548 24 @549 47 @550 46`
= "[44] est[59] [37] qui[64] [26] [32] [16] [08] [24] m[82] [16] [91] n[12]
[44] er[29] e[48] [42] ent[06] pour[00] que[46] [24] ce[47] que[46]"

The claim's parse would read: "[44] est [37], qui [26] [32] [16] [08] [24]
m [16] [91] n [44]ere [42]ent, pour que [24] ce que ..." with 'qui' the
subject of the 3pl verb '[42]ent' across a 12-token gap (@532-543).

**Block A — subject-verb adjacency (distributional, lane standard).**
Clean qui-subject frames licensed by standing values, with qui-to-verb
distance d (all verified in the census above):
- "qui est [32]" @316, @1210; "qui est [19]" @1777: d=1 (x3)
- "qui l'on est" @1446, @1802 (A13 frame): d=3, intervening 77+84 clitics (x2)
- "qui l'on [er]" @145: d=3, clitics (x1)
- "en ce qui [26] [37]" @1769; "qui [23] [37]" @182 (formula frames): d=1 (x2)
- "qui [32]" @33, @855 (32 verb-shaped per adj-32 battery): d=1 (x2)
Stream maximum for qui-as-subject-of-overt-verb: d=3, and d in {2,3} occurs
only with clitic material (77/84) between. The claim requires d=13
(@531 -> @544) with twelve tokens of lexical material between, including a
full noun phrase @541-543 = 44-29-48 ("[44]ere"; 44 is noun-class: 'le 44'
x2 @208/@1679, 'la 44' x1 @1070, '44 pour' x3). A bare NP between a subject
relative pronoun and its verb has no grammatical role in French (not an
object: SOV is ungrammatical; not appositive to 'qui'). No qui-window in
the 47-window census licenses anything comparable.

**Block B — number agreement.**
'qui' as subject inherits its antecedent's number. The antecedent is the
nearest nominal, @530=37 (matrix "@528-530 = [44] est [37]"). Both
candidates are singular-marked: 44 takes singular determiners (11='la'
banked @1070; 77='le' provisional @208/@1679); 59='est' is 3sg
(provisional, standing lane-wide); predicative 37 agrees with the singular
matrix subject. A 3pl verb '[42]ent' (06='ent' battery-promoted, pending
ratification) cannot agree with a singular 'qui'. Even setting the 'ent'
reading aside, Block A alone is fatal.

**No rescue parse.** (i) If @532-543 contained qui's true verb (e.g. 26 on
its verb arm, 'concerne'-shaped per noun-26), the relative clause would
close before @544 and 'qui' would not be the subject of '[42]ent' — the
claim still fails. (ii) Interrogative 'qui' as subject is equally
verb-adjacent. (iii) A 12-token parenthetical between 'qui' and its verb is
not grammatical French. (iv) No finite-verb material exists in @532-543
(scan: zero 59, zero 06 in @532-544), so the span cannot be re-cut into two
clauses that keep 'qui' as subject of '[42]ent'.

**Adverse answered (not ignored):** the bar's adverse — "relative-clause
span @531-544 must parse as one period" — is shown to be a misread with
stated cause: the span cannot be one relative clause headed by subject
'qui' (Blocks A and B). The 44-29-48 material is clause-interior only in
the loose sense; it cannot sit inside a qui-headed relative clause at all.

## Per-clause pass/fail

- Clause 1 (one grammatical period @528-550 with 'qui' as subject): FAIL.
  The required sub-parse (@531-544 as a qui-headed relative clause) is
  ungrammatical under standing values; no alternative single-period parse
  keeps 'qui' as subject of '[42]ent'.
- Clause 2 ('qui' @531 is the subject of '[42]ent'): FAIL AT KILL GRADE.
  The window forces the claim false: (A) distributional rejection —
  qui-to-verb d=13 vs stream max d=3 (10 clean frames, clitics-only beyond
  d=1); (B) agreement — singular antecedent vs 3pl verb. Either block alone
  is fatal; both hold on granted/banked values plus standing provisionals.
- Clause 3 (adverse: @531-544 parses as one period): FAIL — answered as a
  misread with cause (see above), not ignored.
- Clause 4 (scope, no w3 duplication): PASS by construction.

## Verdict

**kill** — A window forces the claim false. 'qui' (64 @531) cannot be the
subject of '[42]ent' (@544): a subject relative pronoun does not sit 12
lexical tokens from its verb (stream max is 3, clitics only), and a 3pl
verb cannot agree with the singular antecedent the relative clause
requires. No standing red-team verdict is contradicted (64='qui' granted
and used; 42's value stays open; A1/A13 untouched). Nothing to escalate.

Note for the pipeline: the live rivals for @544's subject remain w3's
fenced 44-29-48 hypothesis (follow-ups det-pl-544, gender-44 already
queued) and the "qui [26]" short-clause cut (conditional on the open
26=verb question, noun-26 null — red-team territory). This kill does not
decide between them.
