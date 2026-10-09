# Battery verdict: qui-41-01-boundary

**Verdict: NULL** (fence executed — the boundary is not forceable at battery grade).

- Target id: `qui-41-01-boundary`
- Claim: "A forced byte-level word boundary between 41 and 01 proves 41's verb value 01-independent at @40."
- Date: 2026-10-09
- Worker: battery worker (subagent 7422d575-3ad6-4f2c-b0e5-ee98bdaec4f3)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs / 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/qui-41-01-boundary.lock` created on start, deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered)

"Byte-level word-boundary test between 41 and 01; a forced boundary proves 41's verb value 01-independent."

Restated as numbered pass/fail clauses (fixed before testing, not modified after):

- **C1:** A byte-level word boundary between 41 and 01 at @39–40 is forced — i.e. the "41|01" segmentation survives every standing-grade byte test (phase stability, composition exclusion, repetition).
- **C2:** The forced boundary proves 41's verb value 01-independent at @40 (no 01-dependent reading of 41 survives).
- **Resolve-arm:** C1 AND C2 pass → promote. **Else-arm:** fence with stated cause → null.

Adverses listed in queue: "No composition or boundary evidence exists at battery grade yet; the battery found 41's finite value fully unconstrained by the window." — answered below (confirmed, not ignored).

## Method

1. Read BATTERY-PROTOCOL.md first. Lock created/deleted as above.
2. Re-derived the repaired stream in-session; byte-verified the @39–40 locus on row a1_01.
3. Three byte tests: (a) phase stability of the "41|01" pairing under rival row-phase; (b) composition evidence for/against "41"+"01" as one word; (c) repetition leverage ("41 01" census) plus 41's distributional profile (n=19).
4. Standing values held fixed per §7 (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que pencil; 87=ce, 64=qui, 96=par, 17=fois, 79=tout A5, 00=pour A9, 84=on A15, 47=ce A4; provisional 59=est, 77=le). Kills, splits, and the §7 sole-polyvalence rule honored.

## Window-level evidence (all byte-verified)

### The locus

0-based @39–40, row a1_01, mid-row:

`... 91 39 | 64(qui) 41 [39] 01 [40] 24 88 43 81 ...`

Raw digits at the locus: `9139644101248843` — the "41|01" span is raw `4101`.

### Test (a): phase stability — FAILS the forcing bar

Row a1_01's repaired offset is **0** (unvalidated; 68 of 70 upstream row offsets are unvalidated per the canonicality caveat). Under the rival phase (offset 1), the same raw span re-pairs as:

`... 13 96 | 44 10 12 ...`

— the "41" and "01" groups **dissolve entirely**. The "41|01" boundary exists only under the unvalidated offset=0 choice. A boundary that vanishes under the live rival phase cannot be called *forced* at battery grade. Adjudicating the phase is red-team venue.

### Test (b): composition — no evidence either way

- No letter values exist for 41 or 01 at any grade, so no "41"+"01" word can be composed or excluded on spelling grounds. (Contrast stem48-qui-65-hapax, which fenced the "quière" family *against* the 64 grant — here there is no value to fence against.)
- 41's letter-tier contacts show free-word behavior, not composition: @237 (`70(pre) 98 41 17(fois) 11(la)`, row a2_01) flanks 41 with pencil-valued groups on both sides; @59 (`53 12 41 08 34(i)`, row a1_01) stands 41 before letter groups without merging. Neither window shows 41 composing sub-lexically.
- 01's class is itself unresolved (verb-ness at @1256 vs nominal arms; 01-verbclass-probe NULL, red-team venue), so no 01-side composition premise exists either.

### Test (c): repetition — no leverage

- "41 01" occurs exactly **1×** stream-wide (@39–40) — a stream hapax.
- n(41)=19: predecessors {47:1, 64:1, 12:2, 19:1, 98:1, 78:2, 42:1, 97:1, 41:1, 24:2, 56:2, 85:1, 73:2, 89:1} — 14 distinct, max count 2. Followers {06,01,08,98,17,10,20,41,09,12×2,19,15×2,88,65,53,74,62} — 17 distinct, max count 2. Zero distributional repetition to anchor a boundary claim.
- n(01)=28. No 01-window forces a "41 01"-shaped unit anywhere else.

### Adverse answered

The queue's adverse is **confirmed and extended**: not only is 41's finite value fully unconstrained by the @40 window, but the byte-level boundary the claim needs cannot be forced — it is phase-contingent (test a), composition-untestable (test b), and repetition-free (test c).

## Per-clause results

- **C1: FAIL.** The "41|01" boundary is not forced: it dissolves under the rival a1_01 phase, has no composition evidence either way, and no repetition leverage. This is a fence, not a refutation — the rival phase is itself unvalidated, so the boundary is not forced *false* either (kill grade not met).
- **C2: MOOT.** With C1 failed, no boundary exists to prove 41's 01-independence. (Independent of this bar: 41's class remains the three-arm split pending red-team adjudication; fin-41-le stays closed; the @35–39 antecedent NP remains unrecoverable per antec-08-91-39 NULL.)
- **Resolve-arm: not met. Else-arm: TAKEN — fence with stated cause.**

## Verdict: NULL

Not kill-grade: no window forces the boundary false (the rival phase is unvalidated, not established). No standing or red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stated (row a1_01 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `a101-phase-rival-40` (P4) — re-run this bar under the rival a1_01 phase once row offsets are validated; if the phase adjudicates to offset 1, the boundary question dissolves and fin-41's @40 leg is re-audited.
2. `wordinternal-41-census` (P3) — census 41's 19 windows for sub-lexical composition evidence; letter-tier leads are @59 ("41 08 34") and @237 ("70 98 41 17 11").
3. `val-41-40-independent` (P3) — name 41's value at @40 via its qui-leg ("qui [41]" frame) independent of 01 — 01-independence by licensing, not by boundary.

## Bookkeeping

- `battery-queue.json`: `qui-41-01-boundary` queued → verdict/null (temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated).
- Lock created on start, deleted on completion. No standing verdict contradicted or downgraded. R5005, sealed gates, red-team queue untouched.
