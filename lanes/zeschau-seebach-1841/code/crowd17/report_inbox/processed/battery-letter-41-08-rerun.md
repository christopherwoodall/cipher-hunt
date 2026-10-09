# Battery `letter-41-08-rerun` — verdict: NULL (fence executed; dependency unmet)

## Bar (verbatim, pre-registered)

> "pass iff the banked 08 value admits exactly one French word over 41,08,i,er(,e) with a forced segmentation, else keep 41 outside the letter tier"

Numbered clauses:

- **C1** — 08's letter value is banked (the claim's precondition: "once 08's letter value is banked").
- **C2** — the banked 08 value admits exactly one French word over 41,08,i,er(,e) with a forced segmentation → PASS (re-test of W1 @59 can run).
- **C3** — else (dependency unmet or the uniqueness/segmentation test fails) → fence: keep 41 outside the letter tier at this locus.

Per the dispatch caveat: evaluate the dependency in the bar and fence if unmet.

## Findings

Tested against the repaired stream only: 1,847 pairs, 96 types, derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` with the byte-exact tokenization of `repair_parse.py`. `canonical.py` was never used. All asserts of the repair pass hold.

### Locus byte-confirmed (0-based)

Row a1_01, 0-based @59–63:

- @59 = 41, @60 = 08, @61 = 34, @62 = 29, @63 = 40, @64 = 12, @65 = 94

i.e. `41 08 34('i') 29('er') 40('e')` — the exact `41,08,i,er(,e)` frame the bar names. This matches the parent battery's frame (battery-letter-41-dist2-tri NULL: 'priere' (41=p) is the unique common-word @59–63 reading **iff** 08=r; the @59–62 vs @59–63 segmentation is underdetermined, 6 rivals in the shorter).

### C1 FAILS — the dependency is unmet

- The standing letter tier (§7 protocol): 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que. **08 is not banked at any tier.**
- `code/table-grid/table-registry.json` (50 cells) has **no '08' key at all**.
- R20's ruling on the 08 letter question (R20-100, 08-letter-geometry) is **GRANT (signature-level)** — the report states "No value named"; 08's letter-tier value stayed open. Registry: none.
- The post-R20 battery package (08='t', four independent lines, seven spelling legs, h/f/b rivals killed) is **battery-level evidence awaiting red-team ratification**. Battery workers do not adjudicate red-team docket items; a battery promote that the red team has not ratified does not satisfy the "banked" precondition (gate-trigger rule, standing lesson 2026-10-09).
- No R21 red-team report exists yet (checked `report_inbox/` and `report_inbox/processed/` on 2026-10-09 ~21:04 UTC).

C1 fails. The claim is conditional ("once 08's letter value is banked"); the condition has not fired. C2 cannot be tested — testing it now would require provisionally adopting an unratified value, which the bar's "banked" requirement forbids.

### C3 FIRES — fence with stated cause

The re-test of W1 (@59) is **premature**: fence this re-arm until a red-team round banks 08's letter-tier value. Cause: the banked-08 precondition is the entire discrimination power of the bar — the uniqueness/segmentation test over 41,08,i,er(,e) is only meaningful once 08 is fixed, since each candidate 08 letter yields a different word inventory (cf. parent NULL: 08=r selects 'priere'; other 08 letters select other inventories, all untested here).

## Scope

Locus-level (W1 @59) only. No change to 41's standing status (split package fed, not decided, R20-108; 41 outside the letter tier at this locus stays the standing position). No change to 08's status (letter-tier value open; signature-level grant stands; the 't' value package untouched). No standing or red-team verdict contradicted, downgraded, or re-litigated. §7 intact. R5005, sealed gate instances, and the red-team adjudication queue untouched. Canonical-stream caveat stands.

## Follow-ups (all verified ABSENT from battery-queue.json on 2026-10-09 ~21:04 UTC)

1. **`letter-41-08-rerun-rearm`** (P3, conditional): re-arm this exact test once a red-team round banks 08's letter-tier value (the gate-trigger rule: battery-level 08='t' evidence does not fire it). Same bar verbatim.
2. **`letter-41-08-candidate-sweep`** (P4, gather-only): pre-compute the W1 @59–63 French-word legs for each surviving 08 letter candidate, so the rerun fires instantly once 08 banks. Evidence feed only; no value adopted.
3. **`w1-59-segmentation-audit`** (P4): resolve the @59–62 vs @59–63 segmentation underdetermination (6 rivals in the shorter) the parent NULL recorded, independent of 08's value — a forced segmentation there narrows the rerun's C2 test.

## Bookkeeping

- Verdict: NULL (fence executed; conditional dependency unmet — battery-grade conditional logic per dispatch caveat).
- Queue entry `letter-41-08-rerun` → `status: verdict`, `result: null`, 2026-10-09. Pre-write assert passed (was queued/verdictless). Written through target-id-unique temp `battery-queue.json.letter-41-08-rerun.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover.
- Lock `letter-41-08-rerun.lock` created 2026-10-09T21:04:14Z (agent f962a3ac-d884-4e18-b9df-52b3b7bb97e2, no stale lock), deleted on completion (verified gone).
