# Battery report: contredire-85-33-vehicle — 85-33 'contredire' compound lead (evidence only)

- Target: `contredire-85-33-vehicle` (battery-queue.json, priority 2, status queued)
- Claim: test the 85-33 'contredire' compound lead as the vehicle for the 'n'importe' parse (evidence only)
- Worker: 1d5436a1-4d7f-4bd8-9557-6843aebfd9e5
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/contredire-85-33-vehicle.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"gather 85-33 contact profile + compound plausibility evidence for red-team; never declare a second polyvalence"

Numbered clauses (frozen before testing):
1. The full 85-window census and the 85-33 / 33-85 adjacency census are re-derived from the stream with @-offsets.
2. Compound plausibility evidence is recorded with stated strengths and limits (French word-formation, cipher-scheme precedent, boundary evidence), without endorsing or killing the compound.
3. No value is named for 85, no value promoted for 33, and no polyvalence declared; the polyvalence question and the consequences for the croire/dire tie and the 'n'importe' parse are escalated to red team as stated questions.

## Method

Re-parsed the repaired stream (assert 1,847 pairs). Re-derived: all 15 85-windows with ±3 context, 85's full predecessor/successor census, the 85→33 and 33→85 bigram censuses, and 33's full contact census (n=25). Standing values used: banked pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); battery-promoted 94='ne' (ratification pending); provisional 59='est'; §7 sole polyvalence (67 et/veut). NOT assumed: 33='dire' or 33='croire' (tied, both null per dire-33-set / croire-33-tiebreak), 85's value (open; A3 verb-stem frame grant only).

## Window-level evidence

### Clause 1: 85's contact profile (all 15 windows, ±3 context)

| @ | row | pre → 85 → suc | notes |
|---|-----|---------------|-------|
| 54 | a1_01 | 37 11 79 **85** 58 35 53 | 79-85 #1 ('tout [85]') |
| 97 | a1_02 | 97 46 29 **85** 08 21 62 | 29-85 #1 (post-"er") |
| 375 | a2_06 | 65 63 29 **85** 82 48 00 | 29-85 #2 |
| 595 | a4_00 | 00 92 79 **85** 01 29 40 | 79-85 #2 |
| 733 | a5_02 | 88 11 24 **85** 93 76 18 | 24-85 #1 ('en [85]') |
| 746 | a5_02 | 67 77 81 **85** 28 00 64 | 81-85 |
| 956 | a6_00 | 87 46 24 **85** 04 20 67 | 24-85 #2 |
| 1047 | a6_04 | 11 67 76 **85** 41 88 29 | 76-85 |
| 1173 | a6_10 | 87 83 21 **85** 36 74 32 | 21-85 |
| 1234 | a7_01 | 47 33 29 **85** 56 10 03 | 29-85 #3 (stem frame "[X]er [85]") |
| 1278 | a7_03 | 76 48 56 **85** 48 53 61 | 56-85 |
| 1439 | a7_08 | 82 16 24 **85** 01 52 68 | 24-85 #3 |
| 1694 | a8_06 | 27 46 24 **85** 58 15 23 | 24-85 #4 |
| **1699** | a8_06 | 15 23 91 **85** 33 94 30 | sole 85→33; flagged window |
| 1755 | a8_08 | 89 26 24 **85** 58 17 78 | 24-85 #5 |

- Predecessor census: 24 x5, 29 x3, 79 x2, 81/76/21/56/91 x1.
- Successor census: 58 x3, 01 x2, 08/82/93/28/04/41/36/56/48/33 x1 (12 distinct followers).
- **85→33: exactly 1 instance (@1699). 33→85: 0 instances.** The 'contredire' bigram is a hapax — no recurring-bigram support either way.
- Wide window @1693-1704 (row a8_06): `24 85 58 15 23 91 85 33 94 30 20 62`. Note @1694=24-85-58 and @1699=91-85-33 are both on row a8_06.

### Clause 2: compound plausibility evidence

(a) **French word-formation: SUPPORTS plausibility.** "contredire" (to contradict) is a real compound: "contre-" + "dire". "contrecroire" is not a French word — so IF the compound reading is adopted, it is a dire-only compound (relevant to the croire/dire tie, §consequence).

(b) **Cipher-scheme precedent: SUPPORTS plausibility.** Compositional multi-group words are established lane devices: 87+11 = "cela" (A-series grant), 70+12+94 = "prenne" as "pre"+"n"+"ne" (battery-tested, null 2026-10-08). A 85+33 compositional word is scheme-plausible, not exotic.

(c) **Boundary evidence at @1699: NEUTRAL-to-weak.** Predecessor @1698=91 is an open value; no internal-boundary marker and no second instance to test byte-identical repetition against. The bigram is self-contained: **33→94 @1700 is ALSO the stream's sole 33-94 bigram** — so 85-33-94 is a fully unique chain: a unique two-group unit followed by 94='ne'. Consistent with (not proof of) a one-word + negation segmentation: "… [85-33] ne [30] …".

(d) **Limits: STRONG.** Both halves of the compound are open values: 85's value is unpromoted (A3 frame grant only; stem-85 queued) and 33 is tied dire/croire (unpromoted, both null). The compound hypothesis therefore has zero granted legs — it is conditional on two future promotions, exactly the gate the target's evidence field flagged ("if 85 must carry 'contre' as a second function…").

(e) **No kill-grade evidence found.** No window forces 85-33 to be two words; no cleaner rival compound is demonstrated; 33's 12-class successor diversity (including 33→29 x5 stems and 33→46 x2 'que'-frames) does not exclude a bound "dire" stem at @1700.

### 85's standing function load (for red-team polyvalence adjudication)

If 85='contre' were ever adopted, red team would need to reconcile it with the already-recorded functions — stated here, not decided:

- F1: verb-stem in 'en [85]' x5 (@733/@956/@1439/@1694/@1755; A3 frame grant, standing).
- F2: noun-shaped in 'tout [85]' x2 (@54/@595) under 79='tout' PROMOTED — contradiction already recorded by the x-33-laisser-test battery (2026-10-08).
- F3: bound "contre-" prefix inside "contredire" @1699 (this target's question).
- F4: post-"er" complement in 29-85 x3 (class-neutral per x-33-laisser-test).

F3 is a bound-morpheme function distinct from F1/F2. Whether a bound prefix plus a free-stem reading counts as a second polyvalence, or as stem/allomorphy under one value, is a §7 question for the red team — this battery declares neither.

## Consequences (stated, not decided)

1. **croire/dire tie:** if red team ever adopts "contredire" at @1699, it discriminates dire over croire ("contrecroire" is non-French) — a dire-shaped leg at exactly the flagged window. Without 85's value, the tie is untouched: no leg is added by this report.
2. **'n'importe' parse (ne-30-1700, null 2026-10-08):** the compound is the clause-level vehicle the ne-30-1700 report flagged as missing. Under 85-33='contredire', the window reads "… [91] contredire n'importe [20] il ne …". Honest limit: even with the compound granted, the clause stalls at @1703=20 — "n'importe [20]" needs a 'quel'-shaped complement, and 20's value is open (noun-profile, frame-20-62-94 queued). The vehicle supplies the verb for the "n'importe" adjunct but does not close the complement question. pas-30's promotion is untouched (its re-open caveat requires 30='importe' at clause level, not reached here).

## Per-clause results

1. Full 85-window census (n=15) and 85-33/33-85 adjacency census re-derived with @-offsets: **PASS** — 85→33 x1 (@1699), 33→85 x0, all counts trace to the stream.
2. Compound plausibility evidence gathered with stated strengths/limits: **PASS** — French word-formation and cipher-scheme precedent support plausibility; hapax status and both-half-open values are recorded as the governing limits; no kill-grade evidence found.
3. No value named, nothing promoted, no polyvalence declared: **PASS** — the polyvalence question (F1/F2/F3 load on 85) and the two consequences are escalated to red team as stated questions. §7 sole-polyvalence untouched.

## Adverses (answered, not ignored)

- **"§7 sole-polyvalence: battery gathers only, never declares"** — answered by compliance: this report names no value for 85, promotes nothing for 33, and frames the polyvalence question as red-team-only.
- **No standing verdict contradicted.** A3's 85 frame grant, 79='tout' (A5), pas-30's promote, ne-30-1700's null/fence, the dire-33-set and croire-33-tiebreak nulls, and the x-33-laisser-test null are all left standing.

## Verdict

**PROMOTE — evidence-gathering bar only.** All three bar clauses pass: the 85-33 contact profile is fully censused (85→33 hapax @1699; 33→85 x0; 85 n=15 with pre/suc censuses above), compound plausibility evidence is recorded with its real limits (scheme-plausible and French-plausible; both halves unpromoted; hapax), and no value was named or polyvalence declared. **This verdict promotes NOTHING about 85's value or the 'contredire' compound itself** — the compound, the polyvalence question, and the tie/n'importe consequences are referred to the red team with the evidence package above.

No follow-ups are queued by this battery: the battery's bar was gathering, not resolution. Open red-team questions (not queued work): (1) whether F1/F2/F3 on 85 is one value, stem/allomorphy, or a second polyvalence; (2) whether the @1699 compound, if adopted, breaks the croire/dire tie; (3) whether a named 85 closes the @1700 complement at 20 (coordinate with stem-85 and frame-20-62-94, both queued).
