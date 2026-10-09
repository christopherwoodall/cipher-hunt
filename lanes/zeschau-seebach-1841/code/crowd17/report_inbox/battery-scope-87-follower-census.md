# Battery verdict: scope-87-follower-census

- Target: `scope-87-follower-census` (battery-queue.json, priority 3, status queued)
- Claim: test whether 87 scope (free "ce" vs bound "ceci") correlates with follower class across all 32 87-windows
- Worker: b495eb70-526a-4ca1-b5b6-99149e74ceb6. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). 1,847 pairs / 96 types asserted in-session. `canonical.py` NOT used. R5005, sealed gates, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/scope-87-follower-census.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"(a) full 87 follower census with scope assignment per window; (b) state whether the W1/W2 divergence generalizes or is locus-bound; (c) fence with stated cause if the correlation is untestable"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1:** produce the byte-exact follower census of all 32 87-windows with a scope assignment (free "ce" / bound "ceci" / other composition / fenced) per window, grounded in standing red-team rulings.
2. **C2:** state whether the W1/W2 divergence (battery-par43-ce-scope) generalizes across the census or is locus-bound.
3. **C3:** if no follower-class/scope correlation is testable, fence the correlation with stated cause.

Standing values used (per protocol §7 and red-team rounds): pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77="le"); kills hold (01="ci" general value killed R17-015; "-ci" as BOUND morpheme in ce-contexts NOT killed); red-team locus grants (R19-138/R20-070: "ceci" wins at @644 via 87-61 composition; R19-142/R20-038: @1028–1031 window FENCED, @1029 infinitive route rejected; ci-bound-01: W1 @344 fenced as 06-driven residual).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired parse in-session (1,847 pairs, 96 types asserted). Enumerated all 32 87-windows byte-exact with ±2 context.
3. Recovered the W1/W2 divergence framing from battery-par43-ce-scope: W1 (0b@342, row a2_05) = "87 01 06…" — 87 scopes free "ce" + 06-residual (fenced); W2 (0b@1026, row a6_03) = "87 01 03…" — 87 scoped bound "ceci" licensed by the @1029 exclamatory-infinitive promote. Windows diverge at the FOLLOWER OF 01 (06 vs 03), one step downstream of 87.
4. Checked current red-team standing for every scope-relevant ruling (R17-015, R19-138, R19-142, R20-038, R20-070) before assigning scopes.
5. Tested follower-class × scope correlation on the census table.

## Clause results

### C1: full 32-window follower census with scope assignment — PASS

n(87)=32 confirmed byte-exact. Scope assignments:

| @ | row | fol | ±2 context | scope | standing ground |
|---|---|-----|-----------|-------|-----------------|
| 71 | a1_02 | 14 | 24 56 **87 14** 24 | free "ce" | 87=ce grant |
| 74 | a1_02 | 11 | 14 24 **87 11** 00 | "cela" fusion | granted composition (n=7) |
| 148 | a1_04 | 64 | 84 29 **87 64** 96 | free "ce" ("ce qui") | 64=qui grant |
| 163 | a1_05 | 11 | 94 24 **87 11** 24 | "cela" fusion | granted composition |
| 174 | a1_05 | 86 | 60 09 **87 86** 21 | free "ce" | 87=ce grant |
| 180 | a1_05 | 64 | 14 24 **87 64** 23 | free "ce" ("ce qui") | 64=qui grant |
| 191 | a2_00 | 98 | 66 24 **87 98** 56 | free "ce" | 87=ce grant |
| 201 | a2_00 | 11 | 67 76 **87 11** 92 | "cela" fusion | granted composition |
| 225 | a2_01 | 46 | 61 96 **87 46** 98 | free "ce" | 46=que GT |
| 344 | a2_05 | 01 | 96 43 **87 01** 06 | free "ce" + 06-residual (FENCED) | ci-bound-01; par43-ce-scope R2 fenced |
| 461 | a2_10 | 11 | 02 79 **87 11** 59 | "cela" fusion | granted composition |
| 515 | a3_00 | 77 | 88 56 **87 77** 80 | free "ce" | 77="le" provisional |
| 572 | a3_02 | 78 | 94 52 **87 78** 45 | free "ce" | R19-139: determiner parse fenced; "verdict" parse cleaner |
| 613 | a4_00 | 83 | 47 77 **87 83** 70 | free "ce" | 83 conditioned 'de' lead |
| 628 | a4_01 | 78 | 33 29 **87 78** 67 | free "ce" | 78 verb-frame A8 |
| 644 | a4_02 | 61 | 20 24 **87 61** 88 | BOUND "ceci" | R19-138 grant, confirmed R20-070 (locus-level; 61 unvalued globally) |
| 824 | a5_05 | 59 | 13 24 **87 59** 38 | free "ce" | 59="est" provisional |
| 830 | a5_06 | 11 | 01 24 **87 11** 77 | "cela" fusion | granted composition |
| 869 | a5_07 | 77 | 86 70 **87 77** 89 | free "ce" | 77="le" provisional |
| 953 | a6_00 | 46 | 86 96 **87 46** 24 | free "ce" | 46=que GT |
| 1028 | a6_03 | 01 | 96 43 **87 01** 03 | UNDETERMINED (FENCED window) | R19-142 / R20-038: @1028–1031 fenced; @1029 infinitive license rejected |
| 1170 | a6_09 | 83 | 61 94 **87 83** 21 | free "ce" | 83 conditioned 'de' lead |
| 1242 | a7_01 | 11 | 77 81 **87 11** 00 | "cela" fusion | granted composition |
| 1274 | a7_02 | 76 | 47 76 **87 76** 48 | free "ce" | 76 noun lead |
| 1403 | a7_07 | 11 | 77 81 **87 11** 00 | "cela" fusion | granted composition |
| 1426 | a7_08 | 63 | 33 29 **87 63** 91 | free "ce" | 87=ce grant |
| 1487 | a7_10 | 08 | 84 24 **87 08** 31 | free "ce" | 87=ce grant |
| 1527 | a8_00 | 46 | 48 96 **87 46** 21 | free "ce" | 46=que GT |
| 1636 | a8_03 | 74 | 01 74 **87 74** 74 | free "ce" | 87=ce grant |
| 1767 | a8_08 | 64 | 09 24 **87 64** 26 | free "ce" ("ce qui") | 64=qui grant |
| 1775 | a8_09 | 64 | 94 24 **87 64** 59 | free "ce" ("ce qui") | 64=qui grant |
| 1800 | a8_10 | 64 | 91 79 **87 64** 77 | free "ce" ("ce qui") | 64=qui grant |

Follower-class summary: 11×7, 64×5, 46×3, 01×2, 77×2, 78×2, 83×2, 14/86/98/61/59/76/63/08/74 ×1 each.

Scope tally: bound "ceci" ×1 (@644); "cela" fusion ×7; free "ce" ×22 (incl. @344 residual); undetermined/fenced ×1 (@1028).

### C2: the W1/W2 divergence is LOCUS-BOUND — PASS

1. The divergence concerned exactly the 2 "87 01" windows (@344, @1028) — 30 of 32 windows cannot take bound "ceci" scope at all (no "-ci" partner: R17-015 leaves the bound morpheme alive only in ce-contexts; @644's bound scope runs through 61, not 01).
2. The original discriminator was never 87's follower class: both W1 and W2 have follower=01; they diverged at 01's FOLLOWER (06 vs 03), one step downstream of 87.
3. Under current standing the divergence's W2 leg is gone: R20-038 REJECTED the residual-1029-infinitive promote and R19-142 keeps @1028–1031 FENCED — the bound-"ceci" license at W2 no longer exists at battery grade. W1 was already fenced (ci-bound-01). The only surviving bound-"ceci" scope for 87 is @644 (follower 61), which is orthogonal to the W1/W2 frame.
4. Therefore the divergence does not generalize: it was a 2-window phenomenon, and its premises have since been fenced on both sides.

### C3: correlation fence — FIRES

No follower-class/scope correlation is testable, with stated cause:
- Bound "ceci" scope occurs at exactly ONE granted window (@644, follower 61). A single positive cannot establish or refute a distributional correlation; the scope assignment there is a red-team locus grant, not a follower-class prediction.
- The only other bound-candidate windows (@344, @1028) are both fenced, and they share the same follower (01) — so even within the "87 01" pair, 87's follower class does not discriminate scope; the discriminator was 01's follower.
- Fenced: "87's scope correlates with 87's follower class." Scope is assigned per-window by red-team locus rulings (R19-138 @644) and standing compositions ("cela" ×7), not predicted by follower class.

## Verdict: PROMOTE

All three bar clauses pass; no adverses listed. Findings delivered: (a) the 32-window census with per-window scope assignments; (b) the W1/W2 divergence is locus-bound and its W2 leg is now fenced (R20-038); (c) the follower-class/scope correlation is fenced as untestable with stated cause.

## Scope

Scope assignments only; no value named, no class granted, no split declared. Untouched: 61's global value (unvalued per R19-138), 01's value, the @1028–1031 fence (R19-142/R20-038 not re-litigated), the "cela" grants, R17-015's bound-'-ci' survival. No standing/red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated). Per §4 (promote), no follow-ups required.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-scope-87-follower-census.md` (this file)
- Queue: `scope-87-follower-census` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade)
- Lock `code/crowd17/next-token/locks/scope-87-follower-census.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
