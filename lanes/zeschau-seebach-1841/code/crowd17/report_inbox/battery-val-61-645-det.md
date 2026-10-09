# Battery report: val-61-645-det

- Target id: `val-61-645-det`
- Claim: name 61's class at @645 under the now-promoted determiner-87 (zero-assumption NP frame: "ce [61]"); adjectival-61 advances the "ce premier" subject arm one full assumption.
- Date: 2026-10-09
- Worker: battery worker (subagent ce7b26a0-e62d-43f8-aa3e-706a4b3e2c5f)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.
- Note: no lockfile existed for this target on start; I created `code/crowd17/next-token/locks/val-61-645-det.lock` (2026-10-09T21:21:34Z) and deleted it on completion.

## Bar (verbatim, from the task brief / battery-queue.json)

"name 61's class at @645 under the now-promoted determiner-87 (zero-assumption NP frame: "ce [61]"); adjectival-61 advances the "ce premier" subject arm one full assumption."

Numbered pass/fail clauses (pre-registered before testing, not modified after):

1. **C1:** 87 functions as a determiner over a separate 61 at the @644–645 locus (the "ce [61]" NP frame) — i.e., the determiner-87 premise is granted, not the fenced arm.
2. **C2:** 61's class at @645 is named (adjectival-61 — "premier") on standing evidence.
3. **C3:** adjectival-61 advances the "ce premier" subject arm one full assumption (one fewer ungranted assumption than the fin88-646-rerun NULL).
4. **Adverses:** none stated. Standing red-team verdicts are fence conditions: a pass that contradicts them is barred (protocol §5).

Terms (ASD-STE100): "NP" = noun phrase (a noun with its determiner). "Adjectival" = a word that describes a noun. "Ungranted assumption" = a premise the lane has not approved. "Fenced" = a reading the red team has rejected for banked use.

## Method

1. Read BATTERY-PROTOCOL.md first. Checked `code/crowd17/next-token/locks/` for `val-61-645-det.lock` — absent; created it on start (2026-10-09T21:21:34Z); deleted on completion.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`. All @-offsets below are 0-based pair indices unless marked 1-based (the "1b" prefix).
3. Byte-verified the locus: 0b window @640–649 (row a4_02) = `[89][48][20][24][87][61][88][77][78][52]`, i.e. 0b@644=87, 0b@645=61 (1b@645=87, 1b@646=61).
4. Re-derived the bigram census: "87 61" occurs x1/1847 in the whole stream (only at 0b@644); n(87)=32, n(61)=18.
5. Checked standing red-team verdicts BEFORE applying the bar: R19-138 (P1), R20-070, R20-091.

## Window-level evidence with @-offsets

- 0b@643–647 (row a4_02, mid-row), byte-confirmed: `[643]24 [644]87 [645]61 [646]88 [647]77` (1b@644=24, 1b@645=87, 1b@646=61, 1b@647=88, 1b@648=77).
- "87 61" x1/1847 — the sole attestation is this locus. Byte data is neutral between the "ce [61]" frame and the "ceci" composition; the byte evidence does NOT decide C1 on its own.

## HEADLINE — the bar's premise contradicts a standing red-team verdict

The bar's load-bearing premise — C1, 87 functioning as a determiner over a separate 61 at this locus — is exactly the arm the red team fenced:

- **R19-138 (P1 RED-TEAM DECISION), `code/crowd17/report_inbox/processed/next-token-redteam-r19.md`:** "ceci WINS at @644; det-87-644-function's PROMOTE is DOWNGRADED to FENCE; seg-ceci-87-61 composition granted. 87 stays ["ce","prom"]; 61 unvalued globally."
- **R20-070** (CONFIRM R19-138, no new byte evidence): "ceci wins at @644; composition granted locus-level."
- **R20-091** (DUPLICATE / CONFIRM R19-138, FENCE stands): "R19-138 (P1) DOWNGRADED this exact promote to FENCE; seg-ceci-87-61 composition granted; 87=["ce","prom"]." With a PIPELINE-FLAG: a queue entry still showed promote against the standing FENCE.

A battery cannot lift a red-team fence (R20-038 precedent). The granted composition holds 87+61 = "ceci" at this locus, with 61 "unvalued globally". Naming 61's class under the determiner-87 frame would require the fenced reading. The bar is therefore untestable-as-written against standing law: any "pass" would contradict R19-138. Per protocol §5 ("If your result contradicts a standing red-team verdict, do NOT overwrite it — mark your result null with the contradiction as the headline and escalate to the red team"), and per the supervisor's note on this queue entry ("Re-armed target must test under the ceci-composition locus grant, not the 'ce [61]' frame").

No standing verdict was downgraded or re-litigated. The red-team adjudication target `ceci-det-644-adjudicate` (P1) is already queued; this worker's escalations complement it.

## Per-clause pass/fail

1. **C1 — FAIL (fenced).** 87-as-determiner at this locus is FENCED by R19-138 (P1), confirmed R20-070/R20-091. The locus grant is the ceci composition (87+61="ceci").
2. **C2 — UNTESTABLE under the granted frame.** 61 is "unvalued globally" per R19-138. Naming 61's class requires the fenced frame.
3. **C3 — UNTESTABLE.** No assumption count can be reduced from a fenced premise.
4. **Adverses — fenced.** The sole adverse (standing red-team law) is answered by fence, not by evidence.

## Verdict: NULL (contradiction escalation)

The bar premise is the locus-level losing arm. Escalated to the red team rather than overwritten.

## Follow-ups proposed (all verified ABSENT from battery-queue.json on 2026-10-09)

1. `det-87-644-redteam-reconcile` (P1) — Bar: adjudicate the premise contradiction: battery-fin88-646-rerun adopted "87=determiner at @644 (det-87-644-function PROMOTE, zero-assumption)" as a premise while the queue's standing verdict for det-87-644-function is FENCE (R19-138 P1, confirmed R20-091). Claim: the red team reconciles whether fin88-646-rerun's adopted premise is permitted against the standing fence; the loser is downgraded. Evidence: the fin88-646-rerun report (2026-10-09) §Method item 3 vs R19-138/R20-091. Adverses: none stated; the fence is the binding adverse.
2. `ceci-644-dissolve-test` (P3) — Bar: byte-test the granted ceci composition for dissolution: does "87 61" @644 (x1/1847) survive a dissolve attack — i.e., is 87 ever attested immediately before a nominal at the n(87)=32 census, and does 61's follower census at n(61)=18 show compositional variance? Pass = zero independent-87-before-nominal windows force the bound reading to hold; kill = a dissolve window demonstrates 87 as a free determiner adjacent to 61 at battery grade. Evidence: re-derived census (n(87)=32, n(61)=18, "87 61" x1) from the repaired 1,847-pair stream. Adverses: R19-138's ceci grant (fence; a pass does not lift the grant, only characterizes it).
3. `val-61-646-rerarmed-ceci` (P3) — Bar: under the ceci locus grant (61 "unvalued globally", R19-138), test 61's role ACROSS its 17 non-locus occurrences: is adjectival-61 licensed anywhere outside @1556 (val-61-premier locus-level promote) given val-61-contact's global-61 KILL? Pass = a second adjectival-61 locus at battery grade; kill = zero adjectival-61 windows in n(61)=18 outside @1556, confirming 61's value stays unresolved. Evidence: the locus composition grant, val-61-contact KILL, val-61-premier locus-level PROMOTE (@1556 only). Adverses: none stated; does not name 61's value globally.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-61-645-det.md` (this file).
- Queue: `val-61-645-det` queued → verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file + rename; JSON re-validated; own entry only; no downgrade; red-team verdicts untouched).
- Lock `locks/val-61-645-det.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
