# Battery report: qui-38-608-aqui — resolve the "à qui" windows (@38/@608)

- Worker session: 14ccdfcb-409c-4337-9245-ed3a0050cc40
- Date: 2026-10-09 (UTC 12:45 start)
- Lock: created `code/crowd17/next-token/locks/qui-38-608-aqui.lock` on start, deleted on completion.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`).
  `canonical.py` never used. R5005 never touched. Sealed gates untouched.
  Red-team adjudication queue untouched.

## Bar (verbatim from battery-queue.json)

"Bar: resolve the \"à qui\" windows (@38/@608): name the leftward antecedent or fence the frame."

Numbered clauses (pre-registered before testing):

1. C1 — the leftward antecedent of 'qui' at @38 is named with battery-grade evidence.
2. C2 — the leftward antecedent of 'qui' at @608 is named with battery-grade evidence.
3. C3 — if C1/C2 cannot be met, the frame is fenced with stated cause.

Claim-framing note (not a bar rewrite): the queue title calls both "à qui" windows.
Byte-exact check shows @608 is really "qui à qui" (@606=64 @607=39 @608=64);
the parent battery a-39 already fenced that window as adverse A1 ("neither
'qui a qui' nor 'qui à qui' is French"). The bar as written — name the leftward
antecedent of 'qui' at both windows — is testable as written, and was tested.

## Method

Re-derived the repaired stream in-session (1,847 pairs / 96 types; asserts held).
Loci byte-confirmed: @37=39 @38=64 (row a1_01); @606=64 @607=39 @608=64 (row a4_00).
Adopted standing premises (not re-litigated): 39="/a/" allophone tier, lead
(a-39 PROMOTE; "à qui" @37 clean as value-shape); 64='qui' prom; 67 et/veut sole
polyvalence (§7); R24 (24='en' iff follower=85, else finite/modal verb);
R19-192 (67 positional rule exceptionless); registry standings as of 2026-10-09
(50/96 banked; 62='il' removed; 38=[verb,lead]).

## Window-level evidence

### W1 — @38 (row a1_01): "…[91] à qui …"

0-based layout:
```
@26=81(?) @27=00(pour) @28=34(i) @29=24 @30=30(pas) @31=03(verb-stem) @32=64(qui)
@33=32(verb) @34=01(?) @35=08(?) @36=91(?) @37=39(à) @38=64(qui)
@39=41(?) @40=01(?) @41=24 @42=88(gov) @43=43(noun) @44=81(?) @45=30(pas)
```
(? = unvalued cell, no battery/red-team standing.)

- Right side: predicate-complete. @41=24 is finite/modal under R24 (follower
  @42=88, not 85). "à qui [41] [01] [24-fin] [88-gov] [43-noun]" has a verb.
- Left side: antecedent search. A relative "à qui" needs a nominal antecedent
  immediately left of "à" (@37). The full left span @26–@36 contains NO
  noun-class cell at battery grade: 81/01/08/91 unvalued; 32=[verb,cls];
  24=[R24 verb]; 03=[verb-stem,cls]; 30='pas'; 00='pour'; 34='i'. Naming
  91/08/01 as the antecedent noun would invent a value (§3).
- The first qui @32 cannot serve as antecedent of "à qui" — a relative pronoun
  is ungrammatical as the antecedent of a following prepositional relative.
- 39-as-verb-"a" (avoir) route: killed by a-39 ("Zero windows parse 39 as the
  verb 'a'"). Adopted, not re-litigated.
- **C1 FAIL → fence:** the "à qui" sequence shape is grammatical, but its
  antecedent is unnameable at battery grade. Fence cause: no noun-class or
  named-nominal cell in the entire leftward span @26–@36; nearest verb @33=32.

### W2 — @608 (row a4_00): "qui à qui …"

0-based layout:
```
@596=01(?) @597=29(er) @598=40(e) @599=03(verb-stem) @600=39(à) @601=26(noun,lead)
@602=96(par) @603=45(ce,A11) @604=93(verb) @605=54(?) @606=64(qui)
@607=39(à) @608=64(qui)
@609=02(?) @610=58(nominal) @611=47(ce) @612=77(le*) @613=87(ce) @614=83(de)
@615=70(pre) @616=88(gov) @617=10(?)
```
- Adopted premise: a-39 adverse A1 fenced "64 39 64" at @606–608 ("neither 'qui
  a qui' nor 'qui à qui' is French"; 39 possibly word-internal; boundary
  underdetermined). Not re-litigated.
- Antecedent of the second qui @608: immediately left is @606=64=qui —
  ungrammatical as a relative antecedent. Next candidates: @605=54 unvalued
  (naming it invents a value); @604=93 verb-class; @603=45='ce' is 4 pairs
  left across "93 [54] qui" and licenses no "ce … à qui" frame at battery grade;
  @601=26=[noun,lead] is 6 pairs left with "par ce [93-verb] [54] qui"
  intervening — not a licensable antecedent position.
- Right side: no finite verb in the plausible relative span @609–@617
  (02?, 58-nominal, 47=ce, 77=le*, 87=ce, 83=de, 70=pre, 88=gov, 10?). The
  relative clause lacks a predicate under standing values as well.
- **C2 FAIL → fence:** no licensed parse; antecedent unnameable; predicate
  absent. Fence cause stated above. Re-open is red-team/battery venue only
  (naming 54, a 39 word-boundary ruling at @607).

## Per-clause results

- C1: FAIL — @38 antecedent unnameable (no noun-class cell @26–@36).
- C2: FAIL — @608 antecedent unnameable (left neighbor is another qui;
  a-39 A1 fence adopted; no predicate @609–@617).
- C3: FIRES — both frames fenced with stated cause.

## Verdict: NULL

The resolve arm fails at both windows. Not kill: no window forces the "à qui"
value/frame false at kill grade — the sequence shapes are grammatical French,
and naming acts (91/54/08/01 as nouns; 39's word-boundary at @607) re-open the
question at battery or red-team grade. No standing/red-team verdict
contradicted or downgraded (§7 intact; 67 remains sole polyvalence;
canonical-stream caveat stands: rows a1_01/a4_00 offsets unvalidated).

## Follow-ups proposed (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `ant-91-36-noun` (P3) — name 91's class at @36; a noun-91 licenses
   "…[91] à qui…" as the antecedent frame for qui @38. Bar: promote iff a
   noun-class 91 parses the antecedent slot with zero new assumptions.
2. `ant-54-605-noun` (P3) — name 54's class at @605; a noun-54 licenses the
   first qui @606's antecedent and re-opens the "à qui" test at @608. Bar:
   promote iff noun-54 parses both qui frames with zero new assumptions.
3. `wordbound-39-607` (P4) — decide 39's word-boundary status at @607
   (preposition "à" vs word-internal 'a'); if word-internal, qui @608 becomes
   a subject relative with a different antecedent search space. Bar: preposition
   iff a licensed "qui à"-frame parses; else fence as word-internal.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-qui-38-608-aqui.md`
- Queue: `qui-38-608-aqui` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone).
