# Battery verdict: verdict-arm-819-strengthen

- Target: `verdict-arm-819-strengthen` (battery-queue.json, priority 3, status queued)
- Claim: test whether the R20-banked @819 'ce verre' leg composes with the W2-W4 one-word reads — does 'verdict' gain a second independent composition leg outside @573?
- Worker: ef5809f9-6252-454e-893b-8a858f998abd
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; re-derived in-session).
- `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"name the composition with byte evidence at battery grade, or fence the cross-window composition arm"

Numbered pass/fail clauses (frozen before testing):

1. C1 — Name a "verdict" composition (78='ver' + 45='dict' as one French word) at a window outside @573, with byte evidence at battery grade.
2. C2 — (alternative) Fence the cross-window composition arm with stated cause.

Adverses: "legs only — no global 78='ver' promote from this battery; R16-005 LEAD grading."

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types); all @-offsets below are 0-based pair indices of the 78 token (matching the lane's "78-position" convention; byte-identical to older reports' labeling).
2. Re-verified the four standing premises on bytes:
   - @819 leg (R20-035 GRANT): "47 78 40" = "ce verre".
   - W2-W4 one-word 78-45 boundaries (verdict-w2-574-gate PROMOTE; verdict78-gate-wordbound-rearm: "W2-W4 one-word boundary: STANDS", ver-78-independent).
   - W1–W4 classification (battery-verdict45-value NULL): W1 @313 two-word exception (45="ce", R18-014); W2 @573 conditional positive; W3 @982 fenced NEUTRAL (w3-ceci circularity); W4 @1164 fenced residual.
   - 45='dict' status: LEAD, unratified (R20 DEFER: "45 stays ['ce/dict','lead']"; R17-006 settle condition (1) NOT met).
3. Tested each 78-45 window outside @573 for an independent "verdict" composition under the @819-augmented standing set.

## Window-level evidence (byte-exact, re-derived)

### @819 — the independent "ver" half (adopted, re-verified)

`14@813 29@814 49@815 74@816 74@817 47@818 78@819 40@820 95@821 13@822 24@823 87@824 59@825` (row a5_05).

- "47 78 40" = "ce verre": 47='ce' (A4 allophone tier), 78='ver' (tested value), 40='e' (pencil GT). Grammatical French NP on banked/granted values only.
- Full row a5_05 spans @800–824; **zero 45 tokens in the row** (re-verified) — the leg is fully 45-independent, breaking the 78↔45 mutual conditionality from the 78 side (R20-035). Adopted, not re-litigated.

### 78-45 inventory (closed)

Exactly 4 "78 45" windows stream-wide (78-positions): @313 (W1), @573 (W2), @982 (W3), @1164 (W4). Byte-confirmed, matches dict-45-host-inventory.

### W3 @982 — "47 78 45" (does NOT yield an independent second leg)

`01@976 00@977 92@978 07@979 76@980 47@981 78@982 45@983 01@984 24@985 89@986 48@987 01@988` (row a6_01).

- Byte-level, "ce verdict" is available here exactly as at @573. The @819 leg upgrades the epistemic status of the "ver" half (no longer mutually conditional with 45).
- But the composition's "dict" half (45='dict') gains **zero** new support from @819: at W3, 45='dict' is still evidenced only via 78 being word-medial "ver" — the w3-ceci circularity stands. A composition whose second half is unratified is not an *independent* leg; it is a second conditional instance with the identical dependency structure as W2.
- Standing fence respected: battery-verdict45-value fenced W3 NEUTRAL with stated cause (w3-ceci circularity); this battery does not re-litigate it. The @819 leg does not supply the missing "dict"-half support, so it cannot un-fence W3.

### W4 @1164 — "67 78 45" (does NOT yield a leg)

`77@1158 82@1159 44@1160 83@1161 21@1162 67@1163 78@1164 45@1165 13@1166 55@1167 61@1168 94@1169 87@1170` (row a6_09).

- Fenced as residual: "neither two-token reading parses at battery level" (verdict45-value follow-up; dict-45-w4-adjudicate queued). The @819 leg is about 78's value, not about W4's unparseable frame — it does not touch the residual.

### W1 @313 — excluded by standing verdict

45="ce" at W1 (R18-014); the two-word exception stands. Not a composition candidate.

## Per-clause pass/fail

1. C1 (name an independent second "verdict" composition): **FAIL** — no window outside @573 yields one. W3's composition is byte-available but epistemically identical to W2's (both halves lead-grade; "dict" half unratified); it is not independent. W4 is residual; W1 is excluded by standing verdict.
2. C2 (fence the cross-window composition arm): **FIRES** — fenced with stated cause: the @819 leg composes with the W2-W4 one-word reads only at the "ver"-half level. The full "verdict" composition bottlenecks on 45='dict', which is unratified (R17-006 condition (1) unmet, R20 DEFER). No new window composes the full word independently.

Adverse "legs only — no global 78='ver' promote": honored — no value promoted, no lead re-graded; R16-005 LEAD stands untouched.

## Verdict: NULL (fence executed)

The cross-window composition arm is fenced, not killed: no window forces the claim false, and a future 45='dict' ratification re-opens the composition at W2/W3 (W3's neutrality is explicitly conditional on the missing "dict"-half support). The @819 leg's contribution is real but half-scoped — it strengthens the "ver" half of the existing W2 conditional leg; it does not create a second independent "verdict" leg.

## Scope

Window-level composition question only. Untouched: R20-035's @819 GRANT, the W2 one-word boundary PROMOTE, W3's NEUTRAL fence, W4's residual fence, A11 HOLD, 45's ["ce/dict","lead"] status, R16-005 LEAD, §7 (no polyvalence declared). No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a5_05 offset unvalidated; pencil gloss on a5_03).

## Follow-ups (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `verdict-w3-unfence` (P3): re-test W3 @982's neutral status once 45='dict' gains any independent leg — the @819 "ver"-half license plus the standing one-word boundary may promote W3 to conditional-positive.
2. `dict-45-independent-leg` (P3): hunt a 45='dict' leg independent of 78-adjacency — the missing half of the composition; its discovery re-opens the full "verdict" composition arm.
3. `ver78-45-window-census` (P4): re-census the closed 4-window "78 45" inventory after any new 78 or 45 value evidence; W4's residual is the likeliest mover.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-verdict-arm-819-strengthen.md`
- Queue: `verdict-arm-819-strengthen` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.verdict-arm-819-strengthen.tmp` + atomic rename per protocol §5.2; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/verdict-arm-819-strengthen.lock`: created on start (agent ef5809f9-6252-454e-893b-8a858f998abd, 2026-10-09T19:42Z), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
