# Battery verdict: uniform-55-verb-w2w6

- Target: `uniform-55-verb-w2w6` (battery-queue.json, priority 3, status queued)
- Claim: Test whether any uniform verb-class reading covers W2 @523 and W6 @1671 (the two windows blocking option (C)).
- Date: 2026-10-09. Worker: battery subagent 31097421-825d-4628-945c-d29e40e7270d.
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types asserted in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Offset convention: @n = 0-based pair index in the repaired stream.
- Lock: `code/crowd17/next-token/locks/uniform-55-verb-w2w6.lock` created 2026-10-09T20:33:29Z (no pre-existing lock); deleted on completion.

## Bar (verbatim, pre-registered BEFORE testing)

"Kill-grade block at either window fences option (C); cover both with one reading or fence"

## Numbered clauses (fixed before testing, not modified after)

1. C1: a kill-grade block at W2 @523 (some verb-class reading structurally impossible there under standing values) fences option (C).
2. C2: a kill-grade block at W6 @1671 fences option (C).
3. C3: if no kill-grade block at either window, either one uniform verb-class reading covers both windows, or fence with stated cause.

Note on "kill-grade block": a window forces every verb-class reading false for structural reasons (missing subject/governor/auxiliary) under standing values only — value-independent, so no future lexeme choice re-opens it.

## Method

Read BATTERY-PROTOCOL.md first; created the lock on start. Re-derived the repaired stream in-session; every count and window below re-derived from the stream, not trusted from prior reports. Prior reports read for standing values only (not re-litigated, not downgraded): R19-077 (55 verb-class battery-grade), R20-034 (red-team grant of ver78-1670-5581, recording the W2/W6 blocks), R17-007 (06='ent' conditional), the battery 06-attachment rule (06 is '-ent' iff left neighbor is a verb stem; else syllabic), 77='le' provisional, 47='ce' granted (A4), 59='est' provisional, 64='qui' granted, 94='ne' STRONG LEAD, 84='on' granted (A15), 98='vient' LEAD, 11='la' pencil GT. 78's value is OPEN ('ver' LEAD deferred, R16-005); 81's class is OPEN; 91/09/97/44/44/22/80/60/03/39 open. Tested all six verb-class readings — finite, infinitive, imperative, past participle, gerund/present participle, subjunctive — at each window under standing values only.

## Window-level evidence

### W2 @523 (0-based; row a3_00) — byte-confirmed in-session

`@518=09 @519=70 @520=91 @521=77 @522=06 @523=55 @524=81 @525=97 @526=47 @527=44 @528=59`
= "[09] pre(70) [91] le(77) [06] [55] [81] [97] ce(47) [44] est(59)"

- 06 at @522: left neighbor @521=77='le' (provisional), not a verb stem → 06 is syllabic here per the 06-attachment rule, not '-ent'. The string left of 55 is "…le ent [55]".
- Finite: no licensed subject. "le" (77) is article/object-pronoun provisional — not a subject pronoun. 91/09 open; "pre" (70) is a syllable. No postverbal-subject trigger for 81. BLOCKED.
- Infinitive: no governor. No preposition or modal left of 55 ("le"+INF ungrammatical; 70='pre' is a syllable, not the preposition "pré"/"pour"). BLOCKED.
- Imperative: "le [55-IMP]" — positive imperative requires enclisis ("prends-le"); preverbal "le" marks indicative/subjunctive, not imperative. No "ne…pas" for the negative. BLOCKED.
- Past participle: no auxiliary ("avoir"/"être") anywhere left. BLOCKED.
- Gerund/present participle: no "en". BLOCKED.
- Subjunctive: needs "que" + subject; neither present. BLOCKED.
- Rescue considered and rejected: "[55-INF] [81] [97], ce [44] est" as infinitive-subject cleft — 97 dangles unaccounted, "ce [44] est" is not "c'est" (44 intervenes), needs ungranted 97-value. Not battery grade. The infinitive still fails W6 independently (see below), so no uniform reading survives regardless.
- The blocks are structural (missing subject/governor/auxiliary) and value-independent: no choice of verb lexeme for 55 repairs any of them.

**C1: kill-grade block at W2 CONFIRMED.** Every verb-class reading fails structurally under standing values.

### W6 @1671 (0-based; row a8_05) — byte-confirmed in-session

`@1661=98 @1662=80 @1663=22 @1664=94 @1665=84 @1666=64 @1667=06 @1668=91 @1669=11 @1670=78 @1671=55 @1672=81 @1673=92 @1674=60 @1675=03 @1676=39`
= "vient(98) [80] [22] ne(94) on(84) qui(64) [06] [91] la(11) [78] [55] [81] [92-verb] [60] [03] [39]"

- 06 at @1667: left neighbor @1666=64='qui' (granted), not a verb stem → 06 syllabic here.
- Finite: no licensed subject at battery grade. "qui" (@1666) cannot govern 55 — "06 91 la ver" intervenes between relative pronoun and verb (only clitics may intervene). "on" (@1665) cannot reach 55 across "qui". The "la [78]"-as-subject rescue needs 78 nominal (UNGRANTED — 78 'ver' LEAD deferred, R16-005) plus a byte-evidenced clause boundary for the dangling "qui 06 91" — two ungranted assumptions. BLOCKED at battery grade.
- Infinitive: "la [78] [55-INF]" — bare infinitive directly after a determiner-led NP with no preposition is ungrammatical. BLOCKED.
- Imperative: no addressee frame; "la ver" would dangle; preverbal NP incompatible. BLOCKED.
- Past participle: no auxiliary. The "la [78] [55-PP]" NP+participle shape ("la lettre écrite") needs ungranted 78-nominal and strands 81. BLOCKED at battery grade.
- Gerund/present participle: no "en". BLOCKED.
- Compound-tense rescue considered and rejected: "vient … [55-PP]" — "venir" takes no past participle (only "venir de" + infinitive; no "de" present). BLOCKED.
- The blocks are structural and value-independent.

**C2: kill-grade block at W6 CONFIRMED.** Every verb-class reading fails structurally under standing values.

### Uniformity intersection

No verb class covers W2; no verb class covers W6. A fortiori no single uniform verb-class reading covers both. The "verb stem + completion" variant is not a uniform verb-class reading: it would make 55 sub-lexical at the 55-81 windows but whole-word ("prend", seg-55-61-21-stem PROMOTE) at the 55-61 windows — that is the positional rule (option B), not option (C).

**C3: moot — kill-grade blocks fired at both windows.**

## Per-clause pass/fail

1. C1 (kill-grade block at W2): **FIRES** — all six verb classes structurally blocked.
2. C2 (kill-grade block at W6): **FIRES** — all six verb classes structurally blocked.
3. C3 (cover-or-fence tail): **moot** — blocks fired.

## Verdict: NULL (fence executed)

Per the bar, the kill-grade blocks at W2 and W6 fence option (C) — the "one class (uniform verb) covering all 12 windows" resolution for 55. The fence is input to the red-team docket (redteam-55-polyvalence venue); the battery does not kill the red-team venue option, and the red team may still declare option (C) or a variant at §7.

## Scope

- Fences ONLY option (C) (uniform verb-class 55 across all 12 windows). Untouched: R19-077 (55 verb-class battery-grade at the 55-61 windows and conditionally at W1/W3/W4), seg-55-61-21-stem PROMOTE ("prend" @1205), seg-55-61-94-letters PROMOTE ("prend" + 94='ne' particle @576/@1167), options (A) and (B) of the redteam-55-polyvalence package, the 06-attachment rule, 77='le' provisional, 78's deferred LEAD, §7. No standing or red-team verdict contradicted, downgraded, or re-litigated — this finding is consistent with R20-034, which already recorded both blocks. Canonical-stream caveat stands (a3_00/a8_05 offsets unvalidated).
- Re-open conditions (recorded, not tested): (a) a newly banked value licensing a subject/governor/auxiliary for 55 at W2; (b) 78 named nominal by the red team plus byte-evidenced clause-boundary at W6; (c) revision of the 06-attachment rule.

## Follow-ups (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `w2-523-subject-search` (P4) — if 77/91/09/97 bank new values, re-test whether a subject or governor for 55 emerges at W2; re-fires this bar's C1.
2. `w6-1671-78-nominal` (P4) — if the red team names 78 nominal, re-test the "la [78] [55-fin]" subject parse at W6 (still needs clause-boundary evidence for "qui 06 91"); re-fires this bar's C2.
3. `uniform-55-verb-rerun` (P4) — re-run this uniform-cover test if the 06-attachment rule is revised or standing values at the window edges change.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-uniform-55-verb-w2w6.md`
- Queue: `uniform-55-verb-w2w6` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.uniform-55-verb-w2w6.tmp` + rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/uniform-55-verb-w2w6.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
