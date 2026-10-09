# Battery verdict: prenne-R3-relative-341

Target: `prenne-R3-relative-341` — "'prenne' @347 as the verb of the @341 'qui'-relative, subjunctive mood licensed by antecedent @340 45 (superlative/negation/wish force)".
Worker: 804812fe-4179-4d2d-87c2-d5ef5696aca5. Date: 2026-10-08.
Lock: code/crowd17/next-token/locks/prenne-R3-relative-341.lock (created 2026-10-09T01:21:04Z, no prior lock; deleted on completion).

## Bar (verbatim, pre-registered before testing)

> resolve iff 45 (or its NP @338-340) glosses as superlative/negative/wish-force AND 'par 43 ce 01 06' parses as adverbial material with zero contradiction under standing values; else kill the R3 reading

Numbered pass/fail clauses (restated before testing, not modified after):

1. 45 (@340), or its NP @338-340 (31-14-45), glosses as superlative / negative / wish-force — a mood-licensing antecedent for the @341 'qui'-relative.
2. 'par 43 ce 01 06' (@342-346) parses as adverbial material with zero contradiction under standing values.

Resolve iff (1) AND (2). Else kill the R3 reading.

## Method

Repaired 1,847-pair stream only: code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed byte-exact like code/side-keyhunt/repair_parse.py. Never canonical.py. R5005 untouched. Red-team queue untouched. No invented data. All @-offsets are 0-based repaired-stream indices. Standing values used: banked (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); holds (45='ce' A11, 67 et/veut sole polyvalence §7). Relied-upon queue verdicts (not re-litigated): noun-43-discriminator KILL of 43="suite" (2026-10-08), ci-01-value KILL of 01='ci'/'faisant' (2026-10-08), ce-frame-45-64-96-43-87-01 NULL (conditional "par suite" only), ent-06 PROMOTE (06='ent', battery-level, unratified).

## Window-level evidence

Stream @337-351 (row a2_05/a2_06), verified byte-identical to sibling reports:

`@337 64=qui @338 31 @339 14 @340 45 @341 64=qui @342 96=par @343 43 @344 87=ce @345 01 @346 06 | @347 70=pre @348 12 @349 94 | @350 74 @351 67=et/veut`

### Clause 1: the antecedent

- @340 45: operative reading 'ce' (A11 HOLD; the ce-frame battery confirms zero 78-contact here, so the 'dict' rival has no foothold; "ce qui par [43] ce [01]" reads cleanly under 45='ce'). "ce" carries no superlative, negative, or wish force.
- NP @338-340 = 31-14-45: 31 (n=8) and 14 (n=15) are value-open. Contact profiles show no force-marked shape: 31 = "08 31" x3 (@882/@1489/@1521), "64 31" x2 (@338/@1647), followers {14, 79, 29, 92, 11, 24, 76, 10}; 14 = "66 14" x2, "82 14" x2, "79 14" x2 (@1365/@1689), "64 31 14 45" only @339. No superlative-shaped material ("seul/premier/plus"-forms absent; "ce" cannot host superlative modification: "le seul ce" is ungrammatical). No negative frame ("aucun/rien/ne"-frame absent; the 94 inside "prenne" is the word-internal syllable "ne" per prenne-70-12-94, not a negation operator). No wish-force verb in @300-347 (trigger-348 clause inventory: sole 'que' @309 saturated @311-314, 'pour' @329 governs infinitive only). 67='et/veut' @351 postdates the trigram across the forced clause boundary @349|350 and cannot license a preceding subjunctive.
- Result: neither 45 nor 31-14-45 glosses as superlative/negative/wish-force under any standing value. Clause 1 FAILS.

### Clause 2: 'par 43 ce 01 06' as adverbial material

- Head "par 43": 96='par' is granted. The ce-frame battery tested noun-43's full candidate set {suite, condition, maniere, mesure} against "par [43]": ONLY "suite" is grammatical ("par suite" = "consequently"); "par condition", "par maniere", "par mesure" are not French.
- 43="suite" is DEAD at kill grade: noun-43-discriminator (queue verdict, 2026-10-08) found @21 ("82-43-29") forces 43!="suite" — no French parse hosts "suite" under banked 82="m", 29="er", 47="ce"; the viable parses ("mener"/"emmener"-family, verb-stem) all require 43!="suite". The surviving noun set {condition, mesure} both fail "par [43]". @21 further pulls 43 toward "en"/verb-stem, which also fails under "par" ("par en" and "par [stem]" are ungrammatical).
- Word-internal rescue "parmi" (43="mi"): zero standing evidence for 43="mi" (naming it would invent a value); independently killed by @21 ("mmier" is not French).
- Tail "ce 01 06": 01='ci' and 01='faisant' KILLED as general values (ci-01-value); bound "-ci" ("ceci") is fenced to queued ci-bound-01 and "ceci"+06 yields no adverbial parse in any case; 06='ent' (battery-promoted, unratified) gives "ce [01]-ent" no grammatical adverbial reading.
- Result: no parse of "par 43 ce 01 06" as adverbial material exists with zero contradiction under standing values — the sole grammatical head value is forced false by a window. Clause 2 FAILS at kill grade.

## Per-clause pass/fail

1. Antecedent glosses superlative/negative/wish-force: **FAIL** — 45='ce' (HOLD) has no such force; 31/14 open with no force-marked profile; no negation/wish/superlative frame in the window.
2. 'par 43 ce 01 06' parses as adverbial material, zero contradiction: **FAIL at kill grade** — the only grammatical "par [43]" value ("suite") is killed by @21 (standing battery kill); all live 43 values fail "par"; the tail has no adverbial parse.

## Adverses

- "§7 sole-polyvalence": answered — no polyvalence is invoked anywhere in this analysis. 67 et/veut remains the sole true polyvalence. Not ignored.
- "the triggerless kill of prenne-trigger-348 stands while R3 is unresolved (fence/reopen condition, not a downgrade)": answered — the fence/resolve condition now RESOLVES AGAINST REOPENING. The trigger-348 kill's stated reopen condition was "if it resolves, the kill is revisited". R3 does not resolve; it is killed on both bar clauses. The triggerless kill therefore stands, now airtight: no 'que'-governed path (saturated @311-314), no que-less mood-license path (R3 dead). This battery does not modify the prenne-trigger-348 queue entry; it records that the reopen condition evaluated to "no reopen".

## Verdict: KILL

The R3 reading is killed. Both bar clauses fail; clause 2 fails at kill grade (a window, @21 via the standing noun-43-discriminator kill, forces the sole grammatical "par [43]" value false). No standing red-team verdict is contradicted: 45='ce' stays a HOLD (neither promoted nor killed here); 43's value arm stays with queued noun-43 / at21-82-43-29-adjudicate; 01's bound-"ceci" stays with ci-bound-01; 06='ent' untouched; the 12/94 duality stays fenced per prenne-70-12-94.

## Dependency note (reopen condition, not a new target)

This kill is load-bearing on noun-43-discriminator's kill of 43="suite" (battery verdict, 2026-10-08, unratified). If that verdict is ever overturned and "suite" revives, clause 2's "par suite" parse revives with it and this target re-opens. Secondary load: ci-01-value's kill (for the tail analysis). No new follow-up targets are queued: the kill is decisive on both clauses, and the only regeneration path is the stated dependency.
