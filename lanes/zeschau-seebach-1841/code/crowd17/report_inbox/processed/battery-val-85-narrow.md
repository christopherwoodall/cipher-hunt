# Battery verdict: val-85-narrow

- Target id: `val-85-narrow`
- Claim: narrower naming battery for 85 value — re-test only surviving stem candidates from the stem-85 report against the 6 surviving A3 frame legs.
- Date: 2026-10-09
- Worker: 8a9b7069-df3c-47bd-9062-7d82696908ad
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`; asserts re-derived in-session: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/val-85-narrow.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"promote iff a value names with >=2 independent verb-stem frames; kill iff the candidate set empties"

Numbered clauses (frozen before testing):
1. (Promote) A specific French verb-stem VALUE for 85 is named, with >=2 independent verb-stem frames (distinct positions, non-overlapping windows) parsing cleanly under that named value.
2. (Kill) The candidate set empties — every surviving stem candidate is contradicted at kill grade.

Standing values used (protocol §7): pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout A5, 00=pour A9, 84=on A15, 47=ce A4); provisional (59=est, 77=le); frames (A3 85 verb-stem class, value open; 24=en A3 GT). 1841 diplomatic French throughout.

## The 6 legs, re-derived byte-exact in-session

n(85)=15. The A3 frame legs (per battery-stem-85 as corrected by battery-en85-gerund-reaudit, verdict PROMOTE):

| # | @ (85-pos) | row | frame | status |
|---|-----------|-----|-------|--------|
| L1 | @956 | a6_00 | `46-24-85` = "qu'en [85]" | clean gerund |
| L2 | @1694 | a8_06 | `46-24-85` = "qu'en [85] [58]" | clean gerund |
| L3 | @1755 | a8_08 | `26-24-85` = "[26] en [85] [58]" | clean gerund |
| L4 | @1439 | a7_08 | `16-24-85` = "m'[16] en [85]" | clean gerund (16 verb-shaped by clitic entailment) |
| L5 | @733 | a5_02 | `11-24-85` = "la en [85]" → "l'en" | FENCED (gerund vs pronoun-cluster + finite-85 rival) |
| L6 | @97 | a1_02 | `46-29-85` = "que er [85]" | profile leg only (verb-selecting environment, not a word) |

Verified in-session: exactly 5 "24-85" bigrams (24 at @732/@955/@1438/@1693/@1754) and exactly 1 "46-29-85" trigram (46 at @95). No 46-85 bigram exists stream-wide.

## The surviving candidate set

From battery-stem-85 (NULL, 2026-10-08) and its follow-ups:
- **C1 'laisser'** — causative -er verb, LEAD strength (battery-x-33-laisser-test, NULL), gated on 16's class and 33's dire/croire tie. Not killed.
- **C2 'contredire' compound** — 85-33 hapax @1699 (battery-contredire-85-33-vehicle, evidence-gathering PROMOTE); red-team venue for the compound/polyvalence question. Not killed.
- Dead since: 58='ant' (battery-ant-58-ending, KILL); 85-01 unit (battery-unit-85-01, KILL); -cier family (battery-cier-85-595-name, KILL — @97 kills every -cier stem at kill grade).

## Candidate-by-leg test

### C1 'laisser' vs the 6 legs
- L1–L4: "en laissant" is a grammatical gerund in all four clean legs. COMPATIBLE — but non-discriminating: any -er stem fits these frames identically. The legs select the -er class, not 'laisser' specifically.
- L5: fenced; the finite-85 rival parse does not contradict the 'laisser' VALUE (a finite "laisse" is consistent with the stem), and the leg is excluded from naming use by the fence.
- L6: profile leg — 'laisser' is verb-shaped, sits compatibly in the verb-selecting environment. Class-level only.
- 'laisser's actual support comes from the 33/16 gates (x-33-laisser-test), which lie OUTSIDE these 6 legs. **0 of 6 legs name 'laisser'; 0 of 6 kill it.**

### C2 'contredire' compound vs the 6 legs
- The compound's evidence locus is @1699 ("85 33 94 30"), which is NOT one of the 6 legs. None of the 6 legs involves 33.
- L1–L4 under a GLOBAL 85='contre' reading: "en contre" is ungrammatical — "contre" is a prefix/preposition, not a verb stem, and no gerund "en contre" exists in 1841 French. The 4 clean gerund legs therefore kill GLOBAL-'contre' at kill grade.
- BUT no standing claim is global-'contre': battery-contredire-85-33-vehicle explicitly frames the compound as locus-scoped and refers the F1/F2/F3 scope question to the red team, promoting nothing about 85's value. Per protocol §7 and §5.2, this battery does not decide red-team venue. The locus-scoped compound is untouched by the 6 legs.
- **0 of 6 legs name the compound; the legs kill global-'contre' but that claim is not live. The live locus-compound survives.**

## Per-clause results

1. Promote (a value names with >=2 independent verb-stem frames): **FAIL** — neither 'laisser' nor the 'contredire' compound is determined by any of the 6 legs. All legs are value-open: the four clean gerunds admit any -er stem, L5 is fenced, L6 is class-level. 'laisser's support lives in the 33/16 gates; the compound's lives at @1699. This is the same data limit battery-stem-85 Finding 4 recorded: the frames do not supply a value.
2. Kill (candidate set empties): **FAIL** — 'laisser' survives at LEAD (gated, no kill-grade contradiction from any leg); the locus-scoped 'contredire' compound survives as red-team venue. Global-'contre' dies on L1–L4 but was never the live claim. Set = 2, not empty.

No standing/red-team verdict contradicted or downgraded; §7 intact (the 79='tout' F2 nominal tension is red-team venue, not re-litigated). Adverses: none listed.

## Verdict: NULL

The narrow re-test confirms the parent's Finding 4 at the candidate level: the 6 surviving A3 legs are value-open and cannot name 'laisser' or 'contredire' — and neither candidate is killed by them. The candidate set does not empty.

## Follow-ups (null regenerates work; all verified ABSENT from battery-queue.json)

1. **laisser-85-gate-status** (P3) — check whether the 'laisser' lead's gates have moved (16's class via frame-82-16; 33's dire/croire tie). If both resolve favorably, re-run the naming bar with 'laisser' against all 15 windows of 85, not just the 6 legs.
2. **laisser-85-15window** (P3) — score 'laisser' against ALL 15 windows of 85: the 9 non-leg windows, especially the "tout [85]" ×2 nominal frames (@54/@595) under granted 79='tout' (A5), are the real threat to a global 'laisser'. Bars: promote 'laisser' iff >=2 non-leg windows independently support it with zero kill-grade contradictions; kill iff any window forces 85 non--er-stem.
3. **en85-successor-constraint** (P4) — 85's successor census (58 ×3, 01 ×2, 93/04/08/82/28/41/36/56/48/33 ×1): test whether any successor forces a non-stem reading of 85, further constraining the -er inventory beyond the gerund frames.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-85-narrow.md` (this file).
- Queue: `val-85-narrow` → `status: verdict`, `result: null` (temp-file + rename; pre-write assert passed — was queued/verdictless; JSON re-validated from disk; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-85-narrow.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched. `canonical.py` never used.
