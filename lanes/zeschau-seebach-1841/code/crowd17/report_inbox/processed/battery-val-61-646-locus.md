# Battery report: val-61-646-locus

- Target id: `val-61-646-locus`
- Claim: test 61='premier' at @645 by the val-61-premier locus method; removes fin-88-645 assumption (1)
- Date: 2026-10-09
- Worker: battery worker (subagent 509edbb3-05aa-4a12-a514-7d9988325e76)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Bar (verbatim, from battery-queue.json)

"name 61='premier' at @645 under the val-61-premier locus method with zero ungranted assumptions; fence if the locus method fails here"

## Terms used here

- **Locus method** (from battery-val-61-premier.md): the test that named 61='premier' at @1556. It has two parts. Part A (substitution): 61 substitutes the four groups "70 82 34 29" ("premier") in crib-grade structural parallel to the flagship "la premiere fois" ("11 70 82 34 29 40 17"), anchored by the byte-exact "61 40" bigram and the "40 17" ("e fois") right edge. Part B (fence): all other 61 windows are fenced with a stated cause.
- **Granted**: a value in BATTERY-PROTOCOL.md §7 (banked ground truth, promoted, provisional).
- **Ungranted assumption**: any premise that is not granted and not a standing verdict.

## Numbered pass/fail clauses (pre-registered before testing, not modified after)

1. **C1:** the locus method names 61='premier' at @645 — 61 substitutes "70 82 34 29" in crib-grade structural parallel to the flagship, byte-exact.
2. **C2:** the naming uses zero ungranted assumptions.
3. **Verdict rule:** promote iff C1 and C2 both pass; kill iff a window forces 61='premier' false under standing values; else NULL (fence executed) with 1–3 follow-ups.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing. Created `code/crowd17/next-token/locks/val-61-646-locus.lock` on start (agent id + 2026-10-09T11:15:49Z); no stale lock present. Deleted on completion.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`. All @-offsets below are 0-based pair indices.
3. Adopted, never re-litigated: 87='ce' (granted), 77='le' (provisional), 29='er' (banked GT), 40='e' (pencil), 17='fois' (promoted), 88=VERB class (battery PROMOTE 2026-10-09, pending red-team ratification), val-61-premier (PROMOTE, locus-level @1556 only), val-61-contact (KILL of any global 61 value, stands).

## Window-level evidence (all byte-verified on the repaired stream)

### The locus — @645 (row a4_02)

`... [643]24 [644]87(ce) [645]61 [646]88 [647]77(le) [648]78 ...`
Wide clause (@630–660): `67 08 52 67 63 74 46 60 67 77 89 48 20 24 87 61 88 77 78 52 82 94 76 49 24 26 30 03 62 16 00`.

### C1 test — does the locus method name 61='premier' at @645?

It does not, on three independent byte-level counts:

1. **The byte anchor is absent.** The locus method's substitution part is anchored by the "61 40" bigram and the "40 17" right edge. Census: "61 40" occurs exactly once stream-wide (@1556); "40 17" occurs exactly twice (@1039 flagship, @1556). At @645, 61's neighbors are 87 (left) and 88 (right) — zero valued letter-groups adjacent. No spelling composition exists at this window to test.
2. **The structural frame does not match.** The flagship frame is a noun phrase ("la premier-e fois"); @1556 kept the noun-phrase frame ("61 40 17"). The @645 frame is `[87=ce] [61] [88=verb-class] [77=le] [78]` — a "ce"-slot followed by a verb, not a noun phrase. Naming 61="premier" here needs 61 to act as an adjective, but no noun follows (88 is verb-class, battery-promoted). The compositional reading "ce premier" has one support window stream-wide ("87 61" bigram = 1×) — zero repetition leverage, so no distributional crib exists.
3. **The full 61 census confirms @1556 is the sole spelling-composed window.** n(61)=18. Windows where 61 touches a valued letter-group: @367 ("61 70(pre) 17(fois)" — already fenced in battery-val-61-premier as ungrammatical), @926 ("17(fois) 61 96", no word shape), @1429 ("61 12(n) 16", no vowel), @1510 ("12(n) 61 59" — fenced by val-61-contact's clitic-class KILL), @1556 ("61 40(e) 17(fois)" — the promoted locus). @645 has no letter neighbors at all.

**C1: FAIL.** The locus method fails here.

### C2

Not reached — the naming did not complete. Moot.

### Kill check — is 61='premier' at @645 forced false?

No. Under standing values, `[87=ce] [61] [88=verb-class] [77=le]` parses without contradiction; no granted value forces 61='premier' false at this window. The "ce premier" composition was flagged unlicensed in battery-fin-88-645, but that was a premise against the finite-88 reading, not a forced-false for 61='premier'. val-61-contact's global KILL is not re-litigated (this target sought a locus naming only, the same category as val-61-premier's locus promote). **Not kill-grade.**

## Verdict: NULL (fence executed)

Per the bar's own fence clause: the val-61-premier locus method fails at @645, so the locus-level extension is fenced. val-61-premier's @1556 locus-level PROMOTE stands unchanged; no 61 extension beyond @1556 is licensed by this battery. No standing or red-team verdict contradicted or downgraded; §7 intact; the canonical-stream caveat stands (row a4_02 offset unvalidated). Adverses: none were listed.

Note on fin-88-645: this null does NOT remove that report's assumption (1). The @645 window stays a 61/88 residual, still downstream of 61's value at @645 and 24's form at @643.

## Follow-ups proposed (all verified ABSENT from battery-queue.json, 2026-10-09)

1. `det-87-644-function` (P3) — decide 87's syntactic function at @644 (determiner vs pronominal "ce") by the 87-follower census. Determiner-87 licenses a "ce premier [noun]" adjective reading only if a noun follows (none does — 88 is verb-class); pronominal-87 kills the "ce premier" composition outright. This decides which 61 arm is even licensed at @645.
2. `val-61-646-secondleg-sweep` (P3) — 61-as-adjective needs >=2 legs. "87 61" is 1× stream-wide; sweep all 18 windows of 61 for "[det] 61 [noun]"-shaped frames. If @645 stays the sole adjective candidate, fence 61-as-adjective as a one-window residual.
3. `spell-61-anchor-census` (P3) — full spelling-composition census of all 18 61 windows against valued letter-groups. This run's quick census shows @1556 as the sole complete spelling anchor; a full battery confirms it and permanently fences any 61 extension that needs a spelling anchor, or re-opens the question if a second anchor is found.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-61-646-locus.md` (this file).
- Queue: `val-61-646-locus` queued → verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/val-61-646-locus.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
