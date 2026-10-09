# Battery verdict: x-61-94-boundary

**Verdict: PROMOTE (boundary decision).** 61's right boundary at both 94-successor windows is a forced two-word boundary: `61 | 94` — 94 stands as an independent word ("ne", battery-promoted), not bound to 61.

## Target

- id: `x-61-94-boundary` (priority 3)
- claim: 61's right boundary is tested by its 94-successors (2/3 windows).
- evidence: distributional
- adverses: 94-87 "ne ce" hapax at W2 (fenced to ne-ce-1169); 21's value open.
- Date: 2026-10-09. Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-work). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. Lock `locks/x-61-94-boundary.lock` created on start (agent 5f08e439-e669-4412-8604-27f983f91ac6, 2026-10-09T10:45:30Z); no stale lock; deleted on completion.

## Bar (verbatim from queue brief)

"derive numbered bars from the claim before testing: (1) census 61's 94-successor windows byte-exact; (2) decide 61's right boundary with stated byte evidence; (3) fence with stated cause if undecidable."

Numbered pass/fail clauses (pre-registered before data):

- **C1:** the "61 94" successor census is byte-exact and complete.
- **C2:** 61's right boundary at the locus windows is decided with stated byte evidence.
- **C3:** if undecidable, fence with stated cause (only taken if C2 fails).

## Census (C1: PASS)

n(61) = 18. "61 94" bigram = exactly **2x** stream-wide (not 2/3 — no third window exists):

| Window | Slice | Row | 94's follower |
|---|---|---|---|
| W1 @577 | `...55 61 | 94 82 06 06 50 10...` | a3_02 | 82 ('m', banked) |
| W2 @1168 | `...55 61 | 94 87 83 21...` | a6_09 | 87 ('ce', granted A4) |

Both windows share the identical left trigram `55 61` (which itself is 3x; the third instance @1206 has follower 21, not 94 — so no unit signature). "61 94 87" = 1x (W2 only).

61's successor profile (n=18, 14 distinct followers): 96x2, 59x2, 94x2, 21x2, then 10 singletons (20, 42, 70, 88, 24, 31, 56, 12, 40, 15). 61 is a free-combining word; nothing binds it left or right.

## Boundary decision (C2: PASS — two-word boundary forced)

Three independent byte-grounded legs force `61 | 94`:

1. **94 is a battery-promoted free word ("ne").** A free word has word boundaries on both sides; no standing verdict composes 94 leftward into its predecessor at any of its 37 windows.
2. **61 is free-combining.** 14 distinct successors, heterogeneous predecessors (89, 37, 20, 49, 62, 55x3, 87, 17, 92, 01, 53, 91, 12, 93, 04) — no bound-unit signature anywhere in its profile. The one candidate locus value, 61="premier" (val-61-premier, locus-level), yields "premierne", not a French word; no other 61 letter value stands at any grade.
3. **94 varies independently rightward.** W1 has 94→82, W2 has 94→87 — 94's right side diverges while its left side ("61") is identical. A word bound to 61 would not take two unrelated right neighbors in the only two instances; 94 behaves as an independent word, not a suffix.

The composition route ("61"+"94" as one word) has zero supporting evidence: no spelling license, no unit repetition pattern, and contradicts both words' free profiles.

**Decision:** 61's right boundary is `61 | 94` at @577–578 and @1168–1169. The "ne m"-shaped reading at W1 and the fenced "ne ce" hapax at W2 (ne-ce-1169) both sit to the right of the boundary and do not disturb it.

## Adverses answered

- **94-87 "ne ce" hapax at W2 (fenced to ne-ce-1169):** adopted as premise, not re-litigated. The fence concerns 94's right side; this battery decides 94's left side only. The boundary finding is compatible with both the ne-ce fence and any future 94-87 ruling.
- **21's value open:** 21 occurs at @1162 (pre-left) and @1172 (right of 83) — never adjacent to 61. The boundary decision uses no 21 value at any window; the adverse does not bite.

## Per-clause results

1. Census byte-exact: **PASS** (2/18 windows, both `55 61 94`).
2. Boundary decided with byte evidence: **PASS** (three legs, `61 | 94` forced).
3. Fence: **MOOT** (C2 fired).

**Verdict: PROMOTE (boundary decision).** 61's right boundary at both 94-successor windows is a forced two-word boundary. Canonical-stream caveat: rows a3_02/a6_09 offsets unvalidated.

## Follow-ups proposed

No follow-ups required by §4 for a promote. Supervisor observation (not a target): the divergent right sides of 94 (82 vs 87) keep W1 and W2 as independent 94 windows; any "ne m"/"ne ce" ruling applies per-window, consistent with the ne-ce-1169 fence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-x-61-94-boundary.md` (this file).
- Queue: `x-61-94-boundary` queued → verdict/promote, 2026-10-09 (temp-file + rename, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated post-write).
- Lock `locks/x-61-94-boundary.lock`: created on start, deleted on completion.
- No standing/red-team verdict contradicted or downgraded; §7 intact; R5005, sealed gates, red-team queue untouched.
