# Battery report: val-98-subject

- Target id: `val-98-subject`
- Claim: name 98's value/class. If 98 names as subject-shaped or verb-shaped, the "98 83 [56-fin]" frame at @932 re-opens for 83 value-naming with the host granted.
- Date: 2026-10-09
- Worker: battery worker (subagent 11222fca-eb3d-442c-a430-746945a98b93)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs, 96 types, n(98)=40 all re-derived in-session). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Terms (ASD-STE100): "GT" = banked ground truth (pencil). "verb-shaped" = a finite clause-head verb. "kill grade" = evidence strong enough to close a reading.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"Bar: name 98's value/class. If 98 names as subject-shaped or verb-shaped, the "98 83 [56-fin]" frame at @932 re-opens for 83 value-naming with the host granted. Bar: 98's class named at battery grade with ≤1 stated assumption; fence if undecidable."

Adverses listed in queue entry: none.

Numbered pass/fail clauses (fixed before testing, not modified after):

1. **C1:** 98's class is named at battery grade with ≤1 stated assumption. Pass iff a class is forced by banked values + byte-exact windows with at most one stated assumption.
2. **C2:** else-arm — fence if the class is undecidable (state the cause).

Resolve-arm: C1 passes → verdict promote. Else-arm: C2 fires → verdict null.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-98-subject.lock` (agent id + 2026-10-09T11:47:14Z) on start. No fresh lock was present. Deleted on completion.
2. Re-derived the repaired stream byte-exact in-session. All @-offsets are 0-based pair indices.
3. Sibling reports read first and adopted, not re-litigated: prof-98 (PROMOTE 2026-10-09: 98 = finite verb), boundary-98-839 (PROMOTE 2026-10-09: distributional function = finite clause-head verb), vient-98-name (PROMOTE 2026-10-08: 98='vient', pending red-team ratification), de83-932-gate (NULL 2026-10-09: 83≠'de' at @932 at kill grade; this target is its proposed follow-up 1).
4. Standing premises used, not re-litigated: pencil GT (64='qui', 82='m'); promoted/granted (84='on', 00='pour'); §7 (67 et/veut sole true polyvalence; no second value declared at battery grade). 98='vient' is battery-promoted, used as gloss shorthand only; the class finding below stands on banked GT alone.

## Window-level evidence

98 census re-derived (n=40): @12, 19, 80, 89, 92, 124, 192, 227, 236, 355, 440, 511, 702, 767, 803, 838, 894, 897, 930, 946, 971, 1060, 1073, 1074, 1137, 1139, 1145, 1146, 1284, 1317, 1325, 1373, 1481, 1579, 1601, 1643, 1660, 1661, 1725, 1783. Followers: 83 x5, 82 x3, 80 x3, 98 x3, 00 x3, 56 x2, 20 x2 + singletons. Matches the cited census exactly.

### C1 leg A — "qui 98" x2 (zero ungranted assumptions)

- @19 (row a1_00): `53 17 64 98 82 43` = "...fois qui [98] me [43]..." (17='fois', 64='qui' both banked GT).
- @511 (row a3_00): `62 94 64 98 65 88` = "...ne qui [98] [65]..." (64='qui' banked GT).
- 'qui' requires a finite verb in French of every period. No other word class can follow 'qui' in these positions. The class of 98 is forced: finite verb. Zero ungranted assumptions — the force comes from banked pencil ground truth only.

### C1 leg B — "m' 98" x2 (zero ungranted assumptions)

- @930 (row a5_10): `96 48 82 98 83 56` = "...par [48] m(e) [98] [83] [56-fin]..." (82='m' banked GT).
- @1601 (row a8_02): `77 81 82 98 00 44` = "...[81] m(e) [98] pour [44]..." (82='m' banked GT).
- The clitic 'me' procliticizes only to a finite verb. Independent of leg A. Zero ungranted assumptions.

### Kill-grade audit — does any window force 98 ≠ finite-verb?

- Doubled 98 x3 (@1073/@1145/@1660: "98 98") do not parse as two finite verbs. They are fenced as formula/residual with stated cause by standing battery verdicts (prof-98 §4; vient-98-name clause 2). A second value of 98 is a red-team act under §7; this battery adopts the standing fence and declares nothing.
- 'pour 98' (@1137/@1139) is fenced as complement-class residual by vient-98-name (inflectional alternation = red-team act). Does not force a different class.
- All other 33 windows are consistent with a finite clause-head verb (subject slot left: 62 x5, 64 x2, 82 x2, 87 x1, 47 x2; complement inventory right: 83 x5, 00 x3, 82 x3).
- No window forces the claim false at kill grade. No standing or red-team verdict is contradicted.

### Value note (not load-bearing for the verdict)

- 98='vient' is battery-promoted (vient-98-name, 2026-10-08) and pending red-team ratification; used as gloss shorthand only. The class verdict above does not depend on it.

## Per-clause pass/fail

- **C1: PASS** — 98's class is named: finite clause-head verb (verb-shaped). Forced by two independent banked-GT legs ('qui' x2, 'me' x2) with zero ungranted assumptions (limit was ≤1). Kill-grade audit clean; 33/40 windows consistent, 7 fenced under standing battery verdicts.
- **C2:** else-arm does not fire.

## Verdict: PROMOTE

98 names as verb-shaped at battery grade with zero ungranted assumptions. Per the claim, the "98 83 [56-fin]" frame at @932 (`82 98 83 56 69`, row a5_10, 0-based @930–933) re-opens for 83 value-naming with the host granted: 98 is a finite verb and 56 is finite, so 83 sits between a finite verb and its complement. The 'de' arm at @932 stays closed — de83-932-gate owns kill-grade 83≠'de' there ("*de crée" ungrammatical); the re-open covers the remaining value candidates (pronominal y/en, adverbial, nominal), which belong to the already-queued `adv-83-932` target. No promotion beyond this battery's bar is claimed; red-team ratification still applies per pipeline rule. §7 intact — no polyvalence declared.

## Bookkeeping

- Queue: `val-98-subject` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade; no standing red-team verdict covers 98).
- Lock deleted on completion.
