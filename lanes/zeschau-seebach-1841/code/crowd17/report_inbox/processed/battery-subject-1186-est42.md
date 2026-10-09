# Battery report: subject-1186-est42 — PROMOTE (finding grade): 1186 fenced as subjectless-'est' residual

**Target:** subject-1186-est42 — name the subject of 'est [42]' at pair 1186, or fence the 1186 clause as subjectless.
**Worker:** e933789b-5ee9-4fe5-9f28-b32da81db56e | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed byte-exactly per code/side-keyhunt/repair_parse.py; 1,847 pairs / 96 types re-verified). Never canonical.py. No R5005 touched. No sealed gates touched. No data invented. Every @-offset re-derived from the stream. Lock: locks/subject-1186-est42.lock created 2026-10-09T06:46:18Z, deleted on completion.

## Bar (verbatim from battery-queue.json)

> one grammatical subject left of 59@1186 (ellipsis/subject-recovery with stated frame evidence, or 'est-il' inversion under 42's class) with <=1 ungranted assumption; else fence 1186 as a subjectless-'est' residual with stated cause

## Bar as numbered clauses (pre-registered before testing)

1. A grammatical subject left of 59@1186 is named via ellipsis/subject-recovery with stated frame evidence, using <=1 ungranted assumption.
2. 'est-il' inversion parses under 42's noun class with <=1 ungranted assumption.
3. Else: 1186 is fenced as a subjectless-'est' residual with stated cause.

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (asserts hold: 1,847 pairs, 96 distinct groups).
2. Verified frame C at 0-based 1182 [a6_10]: `78(1181) 94(1182) 82(1183) 06(1184) 06(1185) 59(1186) 42(1187) 06(1188) 84(1189) 59(1190) 46(1191)`.
3. Took seg-94-82-06-f1's decided points as given per the adverse — 59@1186 = 'est'-as-word (0 ungranted assumptions), the "mentent est" contact ungrammatical, all verb-unit alternatives dead. Not re-tested.
4. Inventoried every subject candidate left of 1186 against standing values; ran the 27-window 59-census for ellipsis precedent; checked the negated VP's own subject status against subj-w1-573-reroute (W1's "ne mentent" confirmed subjectless, PROMOTE finding grade).

## Window-level evidence (0-based pair indices)

**Frame C verified [a6_10]:** @1181 `78`, @1182 `94`, @1183 `82`, @1184 `06`, @1185 `06`, @1186 `59`, @1187 `42`, @1188 `06`, @1189 `84`, @1190 `59`, @1191 `46`.

**Wider left context [a6_10]:** @1177 `48`, @1178 `59` ("[48] est [37]" — 48 is that clause's subject), @1179 `37`, @1180 `77` ('le' provisional), @1181 `78` ('ver' LEAD, value open).

**The negated VP:** 94-82-06-06 @1182-1185 = "ne mentent", 3rd person plural (94='ne' battery-promoted; 06='ent' verb-ending battery-promoted; ent-06 lists @1182-1185 as one of the two 'ne mentent' legs). Its covert subject would be 3pl ('ils/elles'). W1's parallel leg @578-581 was CONFIRMED subjectless by subj-w1-573-reroute (PROMOTE, finding grade) — the negated VP's own subject is unfound, so there is no recovered subject to share.

**The agreement kill (hard fact, 0 ungranted assumptions):** 'mentent' is 3pl; 'est' is 3sg. A shared covert subject across "ne mentent … est [42]" is number-incompatible regardless of ellipsis theory. The only recoverable subject left of 59 cannot be its subject.

**59-census (n=27) for ellipsis precedent:** every other 'est' window carries an overt left subject ('n'est' x3, "c'est" @825, "cela est" @463, 'qui est' x3, 'on est' x3, 'ne l'est' @1715, "[76] est" @834, etc.) or a flagged caveat (@216 "[78] [06] est que"). @1186's left-3 = `82 06 06` — the only 'est' in the corpus whose immediate left is a finite negated VP. No battery-grade precedent exists for subject ellipsis before 'est'.

**Candidate arms, each tested:**
- (a) Ellipsis/subject-recovery from "ne mentent"'s covert subject: KILLED on number agreement (3pl vs 3sg), from promoted standings alone. Kill grade on this arm.
- (b) "le [78]" @1180-1181 as subject: needs (i) 78's value named as a noun — ungranted ('ver' LEAD is syllable-level, red-team-fenced per R16-005) — AND (ii) the finite clause "ne mentent" interpolated between subject and verb — ungrammatical in 1841 French, no lane precedent. >=2 ungranted assumptions. FAIL.
- (c) 48@1177 (subject of @1178's 'est') shared across "le [78] ne mentent": asyndetic subject-sharing across two finite clauses — ungrammatical; >=2 assumptions. FAIL.
- (d) 'est-il' inversion under 42's class ("est-il [42-noun]" = "is he a [42]?"): grammatical in the abstract, but the adverse reserves 'il'-readings to red-team authority, and interrogative mood is ungranted. Not decidable at battery grade — recorded as the fence-lift condition, not decided here. FAIL at battery grade.

## Per-clause pass/fail

1. **Subject via ellipsis/subject-recovery, <=1 ungranted assumption — FAIL.** Every candidate needs >=2 ungranted assumptions; the recovery arm is additionally killed on number agreement.
2. **'est-il' inversion under 42's class, <=1 ungranted assumption — FAIL at battery grade.** Adverse-gated: 'il'-readings need red-team authority; interrogative mood ungranted.
3. **Fence 1186 as subjectless-'est' residual with stated cause — PASS.** Cause: the only left material is the negated VP "ne mentent" (itself a confirmed-subjectless clause; its covert 3pl subject is agreement-incompatible with 3sg 'est'), plus "le [78]" (78 value-open, finite-clause interpolation ungrammatical); 'est' cannot open a declarative clause (seg-f1, decided); the sole surviving arm ('est-il' inversion) is red-team-reserved.

## Adverses answered

- 42 noun-class (battery) honored: no 'il' claimed from 42; the inversion arm is fenced to the red team, not decided.
- The 'mentent est' contact not re-tested: seg-f1's decisions (59@1186='est'-as-word; contact ungrammatical; verb-unit alternatives dead) taken as given.
- 59='est' stays provisional: no global promotion claimed; this report names no value and promotes no value.

## Verdict: PROMOTE (finding grade)

1186 is fenced as a subjectless-'est' residual with stated cause, per the bar's else-clause (lane precedent: prenne-subject-S1545, subj-w1-573-reroute — "find the subject or confirm subjectless" claims promote on the confirmed-residual arm). The subject hunt at 1186 is closed at battery level.

Scope limits (explicit): names no value; re-grades no lead; declares no polyvalence (§7 intact); does not touch seg-94-82-06-f1's null, the ver-78 LEAD, R16-005, or any red-team verdict. No standing battery verdict contradicted or downgraded.

## Fence-lift conditions (for supervisor / red-team routing)

1. **Red-team 'il'-reading at 1186** (the adverse-reserved arm): a declared 'est-il [42]?' inversion (interrogative mood + 'il' subject) would lift the fence and re-read the clause as a question. This is the only live subject arm; it needs red-team authority, not a battery.
2. **78's value settling** (ver-78 follow-ups already queued: ver-78-rebar, ver78-ce78-open-succ, ver78-296-reparse): if 78 names a noun, re-test the "le [78] … est [42]" long-subject parse — currently blocked on interpolated-finite-clause grammar, so a weak gate.
3. **@216 "[78] [06] est que"** — the only other subjectless-shaped 'est' (caveat window): a joint subjectless-'est' census could test whether 1186 belongs to a residual class rather than standing alone.

---
Lock: locks/subject-1186-est42.lock created 2026-10-09T06:46:18Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No promotions of values made. No red-team verdicts modified or downgraded.
