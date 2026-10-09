# Battery report: class-71-233-rerun

**Target:** `class-71-233-rerun` — determine 71's class at @233 (0-based) once 51's class lands or via an explicit '71 | 51' boundary test.

**Worker:** battery-worker-class-71-233-rerun (agent 5d10f0ab-072f-47cd-a61e-d6284458c2f). Date: 2026-10-09.

**Stream:** repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py` (replicated in-session; asserts: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

**Protocol:** read BATTERY-PROTOCOL.md in full before testing. Lock `code/crowd17/next-token/locks/class-71-233-rerun.lock` created on start (agent id + UTC 2026-10-09T20:22:05Z); pre-run re-read of battery-queue.json confirmed status `queued`, no verdict, no fresh lock — target was clear to take.

## Bar (verbatim from battery-queue.json)

"Name the class with >=1 frame-leg at battery grade, or fence the window"

**Numbered clauses (pre-registered before testing):**
- C1: Name 71's class at 0-based @233 (lane @234) with ≥1 frame-leg at battery grade (distributional or grammatical evidence tying 71 to a granted frame at this window).
- C2: Run the explicit '71 | 51' boundary test: same word vs adjacent tokens, resolved on byte evidence (collocation strength, row-boundary structure, typographic marks in the upstream CT).
- C3: No standing red-team verdict contradicted; §7 intact (no split or second polyvalence declared at battery level).

## Method

1. Re-derived the repaired stream in-session; byte-verified the window.
2. Full inventory of code 71 (n=7) and code 51 (n=6): predecessors, successors, bigram counts, row structure.
3. Tested each standing candidate class for 71 at @233 (adjective, locus-adjective, determiner/quantifier, nominal, sub-lexical) against the bar.
4. Checked the raw upstream CT line for typographic word-boundary marks.

## Window-level evidence (0-based @-offsets; lane convention 1-based)

- @230=96 @231=21 @232=60 @233=71 @234=51 @235=70 @236=98, row a2_01 (all mid-row, in-row 12–18; no row boundary anywhere in the ±6 window): `96 21 60 71 51 70 98` = "par [21-noun] [60] [71] [51] pre [98]".
- '71 51' bigram: exactly 1x stream-wide (n=1847).
- 71 (n=7): preds {60 x2, 63, 48, 65, 86, 83}; succs {51, 10, 12, 17, 64, 50, 48} — all x1. Every successor distinct; every predecessor-but-60 distinct.
- 51 (n=6): preds {97, 98, 71, 84, 91, 48} — all x1; succs {47, 62, 70, 37, 64, 45} — all x1. Fully dispersed on both sides.
- Raw CT line a2_01 is digit soup with no separators: `94629421624896196874698838296216071517098411711261216563` — no typographic word-boundary marks exist in the byte record.

## Per-clause pass/fail

**C1 — FAIL on the naming arm; the fencing arm is taken.**
Candidate arms exhausted at this window:
- Adjective (uniform): dead at kill grade (battery-class-71-adjective: 71≠adjective forced at @925 and @1337). Adopted as premise, not re-litigated.
- Adjective (locus-level, stacked epithets): fenced by the parent battery (battery-adj-71-234-locus, null): zero value evidence, zero corpus support (0 genuine bare stacks vs 55 coordinated controls).
- Determiner "une" (frequency leader, battery-un-71-det-census): 'par [21-noun] [60-adj] une [51]…' is grammatical ONLY if 51 is a nominal head — 51's class is open (no queue target names it; verified absent), so no frame-leg exists at battery grade. The leg is conditional on an unlanded premise.
- Quantifier-like (the @925 non-nominal arm): 'par [21] [60] [quant] [51]…' has no head for the quantifier — the post-adjectival quantifier shape is ungrammatical in a PP; no leg.
- Nominal: 'par [21-noun] [60-noun] [71-noun]…' is bare N-N-N adjacency — ungrammatical per battery-pre-71-60-class (C1 fail at @233: bare noun-noun adjacency needs apposition/compound/proper-name evidence, none exists).
- Sub-lexical (71 as letter-group fusing with 51): no collocation support — '71 51' is 1x/1847 with fully dispersed pairings on both sides; the only supported sub-lexical locus for 71 is '48 71 12' at @712, not this window.
No class carries ≥1 frame-leg at battery grade. Fencing arm taken.

**C2 — INCONCLUSIVE; fenced with the window.**
The explicit boundary test is unresolvable on the byte record: the upstream CT carries zero word-boundary marks (digit soup), and the distributional evidence is negative-only — '71 51' at 1/1847 with all-distinct pairings on both sides rules out a fixed fused unit, but is fully compatible with both "same word" and "adjacent tokens" readings. Same-row adjacency (a2_01 in-row 16/17) adds no boundary evidence either way. 51's class has not landed (no `class-51-*` target exists in battery-queue.json), so the rerun's first clause ("once 51's class lands") cannot fire. Test does not discriminate: fenced, not forced.

**C3 — PASS as constraint.**
Standing verdicts preserved: uniform-adjective kill (class-71-adjective), @233 locus fence (adj-71-234-locus), split-candidacy gathering (val-71-quant-nominal PROMOTE at finding grade, R19-186), poly-60 fence (R20-119 — '60 71' 2x noted, both mid-row, no polyvalence declared). No split, no second polyvalence, no value named. §7 intact.

## Verdict: NULL (fence)

Neither rerun clause fires: 51's class is unlanded, and the explicit '71 | 51' boundary test is byte-unresolvable (distributional evidence is negative-only; the CT has no word-boundary marks). No class for 71 at @233 carries a frame-leg at battery grade (adjective killed, locus-adjective fenced, determiner/quantifier legs blocked on 51's open class, nominal ungrammatical, sub-lexical unevidenced at this window). The window is fenced; 71's class at @233 stays open.

## Adverses answered

- "Adjective arm for 71 needs a section-7 split declaration": adjective arm not pursued — uniform arm is kill-grade dead, locus arm fenced by the parent battery; no split declared (gather-only).
- "uniform adjective killed (class-71-adjective)": adopted as premise.
- "poly-60 fence (R20-119)": 60's standing untouched; '60 71' 2x recorded, no polyvalence declaration.

## Scope

Fences only the stated window and the two rerun clauses. Untouched: 21=noun, 60's standing, 71's §7 split candidacy (R19-186 / val-71-quant-nominal), 51's open class (n=6), poly-60 fence (R20-119). No standing verdict contradicted or downgraded.

## Follow-ups (§4; all three verified ABSENT from battery-queue.json)

1. `class-51-census` (P3) — census code 51's 6 windows (0b@3/81/234/413/853/973); bars: name 51's class with ≥1 frame-leg at battery grade, or fence it. Unblocks this rerun's first clause.
2. `class-71-233-r3` (P3) — re-run once 51's class lands: test the 'une/ch + [51-noun]' determiner/quantifier leg at @233; bars: name the class with ≥1 frame-leg at battery grade, or fence the window permanently.
3. `unit-60-71` (P4) — rival-arm test: '60 71' occurs 2x (@232/@1563, both mid-row); bars: positive byte/distributional evidence that '60-71' reads as one word at @233 (both windows parse under one value), or fence the unit arm.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-class-71-233-rerun.md` (this file).
- Lock `code/crowd17/next-token/locks/class-71-233-rerun.lock` created on start (agent 5d10f0ab-072f-47cd-a61e-d6284458c2f, 2026-10-09T20:22:05Z), deleted on completion.
- Queue update: `class-71-233-rerun` → `status: verdict`, `verdict: {result: null, report, date: 2026-10-09}` via `battery-queue.json.class-71-233-rerun.tmp` + atomic rename (pre-write re-read asserted queued/verdictless; post-write re-validated from disk; own entry only; no downgrade).
