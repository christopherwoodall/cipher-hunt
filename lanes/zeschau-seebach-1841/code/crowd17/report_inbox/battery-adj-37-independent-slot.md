# Battery report: adj-37-independent-slot

**Target id:** `adj-37-independent-slot`
**Verdict:** NULL (fence executed — the supply arm fails on count)
**Date:** 2026-10-09
**Worker:** b2eb0e76-5d03-40d7-9fab-8c9a842f0bcc

## Bar (verbatim from queue)

"supply the missing independent adjective-slot leg for 37"

Numbered clauses:
- C1 (supply arm): name ≥2 independent "37 [granted-noun-head]" prenominal windows outside the 43 family, each supporting 37 in a prenominal adjective slot.
- C2 (fence arm): if C1 fails, fence the independent-adjective-slot claim with stated cause.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed per `repair_parse.py`; asserts held: 1,847 pairs, 96 types).
`canonical.py` never used. Censused all 28 windows of group 37 with ±3
context; tabulated followers; checked each follower against the granted
noun roster (43=[noun,cls] R19-064/R20-117; 65 noun R20-047; 68=[noun,cls]
R19-107; 69 noun R19-109; 76 noun R19-111, confirmed by val-76-class-census
2026-10-09).

## Findings

**n(37) = 28.** Follower distribution:
78×4, 43×3, 64×3, 01×3, 11×2, 77×2, 08×2, 06×1, 61×1, 76×1, 33×1, 44×1,
03×1, 96×1, 86×1, 91×1.

**"37 [granted-noun]" windows:** the 43-family ("37 43" ×3 at @385, @1125,
@1723) is excluded by the target. Of the remaining followers, the only
granted noun is **76 ×1 at @620** (row a4_01):
`29('er') 88 [37] 76 82('m') 14` — i.e. `[88] [37] [76-noun-masc] m…`.
No "37 65", "37 68", or "37 69" window exists anywhere in the stream.

**@620 assessment:** the adjective reading "[37-ADJ] [76-N]" is
structurally possible (76 is a granted masculine noun), but it is held
hostage by the target's own adverse: 37="le" (S5) is **live at MEDIUM**
(R17-era rating, never killed), and under S5 the same bigram reads
"le [76]" — determiner + noun — which is mutually exclusive with the
adjective slot. With S5 unadjudicated, @620 cannot count as a clean
independent adjective-slot leg.

**C1 — FAIL.** Exactly one non-43 "37 [granted-noun]" window exists (@620),
and it is contaminated by the live S5 rival. The bar needs ≥2 independent
legs; the stream cannot supply them.
**C2 — PASS (fence fires).** The independent-adjective-slot claim for 37 is
fenced: no second prenominal "37 [granted-noun]" window exists outside the
43 family, and the sole candidate is undecidable while S5 stands.

No standing or red-team verdict contradicted. 37's noun class grant
(R17-003/R17-008), the A12 "37 01" unit, and the 43-family windows are all
untouched. §7 intact.

## Scope

Fences only the *independent* (non-43-family) prenominal adjective-slot
claim. Does not touch 37's class, the 43-family adjective question, or S5.

## Follow-ups proposed (§4)

1. `adj-37-76-rerun` (P3) — re-test @620's adjective reading once S5
   (37="le") is adjudicated via the already-queued `s5-37-385-adjudicate`;
   the single leg is currently undecidable, not dead.
2. `adj-37-nounwatch` (P4) — re-run this census if/when any new noun grant
   lands; check whether the newly-granted noun's windows ever follow 37.
   (Both IDs verified ABSENT from battery-queue.json.)

## Bookkeeping

- Lock `locks/adj-37-independent-slot.lock` created on start (agent id +
  UTC timestamp), deleted on completion.
- Queue: `adj-37-independent-slot` → `status: verdict`, `result: null`
  (pre-write assert: was queued/verdictless; temp-file + rename; own entry
  only; no downgrade).
- R5005, sealed gate instances, and the red-team adjudication queue
  untouched. No numbers invented; every @-offset traces to the repaired
  stream.
