# Battery verdict: prenne-trigger-348

Target: `prenne-trigger-348` — "the subjunctive trigger for @347-349 is located via clause-boundary analysis @300-347".
Worker: ab274a53-ae16-4cbf-81c4-0c1caf694cef. Date: 2026-10-08.
Lock: created 2026-10-09T00:57:46Z, no prior lock (no stale-lock note needed).

## Bar (verbatim, pre-registered before testing)

> resolve iff a trigger+subject parse is found, else confirm triggerless with stated cause

Numbered clauses:
1. Resolve: a trigger+subject parse for the subjunctive @347-349 is found under standing values with zero contradiction.
2. Else: the window @300-347 is confirmed triggerless, with a stated cause.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). Never `canonical.py`. No invented data. Offsets below are 0-indexed pair positions; this battery anchors at the trigram's first pair, so @347 = trigram @347-349 = 70-12-94 ("pre"+"n"+"ne"). Standing values used: 46=que, 84=on, 64=qui, 00=pour, 96=par, 87=ce, 11=la, 17=fois (banked); 59=est, 77=le (provisional); 37/32/42 predicative frames, 67 et/veut sole polyvalence (granted).

## Window-level evidence

Glossed stream @300-351 (row a2_04/a2_05/a2_06):

`@300 86 @301 91 @302 18 @303 89 @304 88 @305 02 @306 88 @307 20 @308 17=fois @309 46=que @310 84=on @311 24 @312 37 @313 78 @314 45 @315 64=qui @316 59=est @317 32 @318 94 @319 06 @320 11=la @321 92 @322 60 @323 15 @324 63 @325 71 @326 10 @327 01 @328 19 @329 00=pour @330 92 @331 50 @332 45 @333 54 @334 88 @335 40=e @336 03 @337 64=qui @338 31 @339 14 @340 45 @341 64=qui @342 96=par @343 43 @344 87=ce @345 01 @346 06 | @347 70=pre @348 12 @349 94 | @350 74 @351 67`

Clause inventory of @300-347:
- Sole 46='que' in @280-347 is @309 (verified by scan; previous 'que' is @226, 83 pairs back). Distance @309→@347 = 38 pairs.
- @310 84='on' (banked subject pronoun) opens the 'que'-clause; a subject pronoun forces a finite verb in @311-314. @312 37 is a granted predicative frame (A1) — a finite copular verb sits in @311-313. The 'que' is saturated by its own clause here.
- 'qui'-relatives at @315 (verb 'est' @316, provisional), @337, @341 — each carries its own finite verb. A 'que' governs the finite verb of its own clause; it cannot skip its own verb plus three relative-clause verbs to govern @347.
- @329 00='pour' + @330 92: 'pour' governs an infinitive, never a subjunctive. (92's class is the sibling battery's target; not needed here — 'pour' is not a subjunctive frame regardless.)
- @342 96='par', @344 87='ce': neither is a subjunctive frame. No negation frame is visible in the window.
- The "qu'on … prenne" single-clause rescue (subject 'on' @310, verb "prenne" @347) fails by dilemma on 01-06 @345-346:
  - If 01-06 is finite ("[01]-ent"), the @341 'qui'-relative is saturated and "prenne" @347 opens a new verb-initial clause with no introducer — triggerless.
  - If 01-06 is non-finite, the @341 'qui' is left verbless and the single-clause parse is ungrammatical — so "prenne" cannot be the 'que'-clause's verb; the 'que' stays saturated at @311-314 and "prenne" is the @341 relative's verb (subject = 'qui' @341).
  - Either horn: @309's 'que' does not govern @347.
- Right edge (adverse test): 74 is verb-shaped, verified independently from the repaired stream — n=34; predecessors {74 x6, 49 x5, 94 x3}; followers {74 x6, 45 x3, 46 x3, 62 x3, 67 x2, 77 x2}; '74 77' ("74 le", 77='le' provisional) @212 and @1677; '74 46' ("74 que") @418, @635, @693; self-doubled x6. "prenne 74" as V+V is ungrammatical in French, so a clause boundary is forced at @349|350: the trigram is clause-final. The 'prennent' re-parse (70-12-94-74 = pre-n-ne-nt with 74='nt') is blocked by 74's verb contact profile and the sole-true-polyvalence rule (67 et/veut only).
- Pre-verbal slot @346 06 ('ent'/'-ment' lead): n=44; predecessors {42 x5, 82 x4 ('m' banked), 30 x4}; followers {77 x6 ('le'), 11 x4 ('la'), 00 x4, 29 x4, 67 x3}; sample windows show 06 trailing stems and preceding objects ("41 06 77", "42 06 77", "94 06 11 92", "78 06 59"). '06 70' occurs exactly 1x stream-wide — here, at the trigram's left edge. No subject-shaped reading under standing values ('06 59' x2 is ambiguous and rare, 2/44; not a subject-verb junction under any granted value).

## Per-clause verdicts

1. Trigger+subject parse found: **FAIL** — no parse under standing values yields both a subjunctive trigger and a subject for @347-349 with zero contradiction. The only 'que' (@309) is saturated by its own clause; no other introducer exists in @300-347.
2. Triggerless confirmed with stated cause: **PASS** — stated cause: (a) sole 'que' @309 saturated @311-314 ('on' + predicative-frame verb), unreachable across three 'qui'-relatives; (b) the single-clause rescue fails by the 01-06 dilemma either way; (c) 'pour'/'par'/'ce' are not subjunctive frames and no negation frame is visible; (d) '74 = verb' forces a clause edge at @349|350, making the trigram clause-final; (e) the pre-verbal slot @346 06 is not subject-shaped. The trigger is not located because there is none in the window.

## Adverses

- "triggerless window is the rival" — the rival WINS. The window is confirmed triggerless with the five-point stated cause above. Not ignored; it is the verdict.
- "'74 = verb' reading's consequence (forces re-parse of the trigram's right edge)" — tested and answered: 74's verb profile re-verified from the repaired stream (numbers above); consequence confirmed — a clause boundary is forced at @349|350, the trigram is clause-final, and the 74='nt' ("prennent") re-parse is blocked by the contact profile plus the sole-polyvalence rule. Not ignored.

## Verdict: KILL

The claim is false: clause-boundary analysis @300-347 locates no subjunctive trigger for @347-349 — it confirms the window is triggerless, with the stated cause above. No standing red-team verdict is contradicted (checked `code/side-homophonic/report_inbox/red-team-rulings.md`: it covers the homophonic solver only; the sibling `battery-prenne-70-12-94` null fenced the 12/94 duality on a different bar, which this battery does not touch). The 12/94 duality stays fenced for the red team per the sibling verdict; neither the ne-94 nor the n-e-12-48 promote is downgraded by this kill (scoped to the trigger bar only).

## Follow-up (fence / reopen condition)

1. **prenne-R3-relative-341** (priority 2): test the surviving horn — "prenne" @347 as the verb of the @341 'qui'-relative (subject = 'qui' @341), subjunctive mood licensed by the antecedent @340 45 carrying superlative / negation / wish force. Bar: resolve iff 45 (or its NP @338-340) glosses as superlative/negative/wish-force AND "par 43 ce 01 06" parses as adverbial material with zero contradiction under standing values; else kill the R3 reading. Rationale: this is the only 'que'-less mood-license path the window leaves open. If it dies, the triggerless kill is airtight; if it resolves, this kill is revisited.
