# Battery report — detframe-43-hunt

Date: 2026-10-09
Target: `detframe-43-hunt` (P3)
Verdict: **NULL** (fence executed — attributive-91 arm fenced across the full 43 population)
Parent: `battery-adj-91-386-43-gate.md` (NULL, follow-up #1)

## Bar (verbatim from battery-queue.json)

"Land a 'DET 43' frame that licenses postnominal-adjective 91, or fence the attributive-91 arm across the full 43 population."

Restated as numbered clauses:
- C1: a 'DET 43' frame lands that licenses postnominal-adjective 91 (byte evidence at battery grade).
- C2: else the attributive-91 arm is fenced across the full 43 population, with stated cause.

## Method

Re-derived the repaired stream in-session (1,847 pairs / 96 types, all asserts held; `canonical.py` never used). Full n(43) census byte-exact. Determiner tier from standing values only: 11='la' (GT), 47='ce' (promoted), 77='le' (provisional), 87='ce' (promoted demonstrative), 45='ce' (A11 hold).

## Findings — all 16 43-windows (0-based @, pre, post, row)

| @ | pre | post | row | det status |
|---|-----|------|-----|------------|
| 21 | 82 | 29 | a1_00 | none |
| 43 | 88 | 81 | a1_01 | none |
| 244 | 56 | 00 | a2_02 | none |
| 258 | 32 | 77 | a2_02 | none (91 is LEFT of 43 here: "91 32 43 77") |
| 343 | 96(par) | 87(ce) | a2_05 | loose "par [43] ce" only |
| 386 | 37 | 91 | a2_07 | none (predicative left edge) |
| 439 | 46 | 98 | a2_09 | none |
| 563 | 11=la | 24 | a3_02 | **strict: la [43]** |
| 1027 | 96(par) | 87(ce) | a6_03 | loose "par [43] ce" only |
| 1092 | 06 | 07 | a6_06 | none |
| 1126 | 37 | 00 | a6_07 | none |
| 1204 | 47=ce | 55 | a7_00 | **strict: ce [43]** |
| 1303 | 08 | 21 | a7_03 | none |
| 1305 | 21 | 77 | a7_04 | none |
| 1544 | 78 | 00 | a8_00 | none |
| 1724 | 37 | 98 | a8_07 | none |

Correction to the parent's search-space note: the parent claimed four det-adjacent windows @343/@563/@1027/@1204. Strict immediate-predecessor=DET holds only at **@563** ("la [43]") and **@1204** ("ce [43]"). At @343 and @1027 the predecessor is 96='par' with 87='ce' AFTER 43 ("par [43] ce" — 64 45 64 96 43 87 01 03/06). The fence holds under either reading.

Key distributional facts:
- **"43 91" is a stream hapax, only at @386** — and @386 has NO determiner (pre=37, the predicative "est"-shaped frame; post-91 is 36).
- **No 91 within 2 positions of any 43 window except @386** (scan of all 16): @258's "91 32 43" has 91 LEFT of 43 (pre-nominal position, 32 intervening) — cannot be postnominal to 43.
- At the two strict DET 43 windows (@563: post=24; @1204: post=55) and the two loose ones (@343/@1027: post=87 'ce'), no 91 anywhere nearby. An attributive postnominal 91 at these windows would have to be invented.

Related population note (for context, not decided): 91 has DET-proximity at five other windows (@15, @723, @1005, @1428, @1518), so DET-91 attributive geometry exists elsewhere in the stream — the "DET 43 91" frame specifically is what is absent.

## Per-clause results

- **C1 FAIL:** no 'DET 43' frame lands that licenses postnominal-adjective 91. The only "43 91" geometry has no determiner; the DET-adjacent 43 windows have no 91.
- **C2 FIRES:** the attributive-91 arm is fenced across the full 43 population, with cause stated above. Fence, not kill: if the red team names 43's value/class AND a new DET-43-91 geometry arrives (or 43's class turns out to admit 91 under a different reading), the arm can be re-armed — it is not falsified as a global claim, only unsupported at every live window.

## Adverses

None listed. Note the fence's second leg is partly value-independent: even if 43 were named, the "43 91" hapax has no determiner, so a determiner-supported attributive frame at that window specifically would need new evidence beyond a named 43 (echoes the gate battery's scope caveat).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `gated-91-2trigger-rearm` (P4) — re-arm the attributive-91 arm iff BOTH a battery-grade 43 value is named AND a new DET-43-91 geometry is attested at any window.
2. `postnom-91-otherhosts` (P3) — test the five DET-proximate 91 windows (@15/@723/@1005/@1428/@1518) for licensed attributive-91 geometry with named hosts; fences if no host licenses it there either.
3. `pred-37-43-91` (P3) — since the only "43 91" window sits in the predicative-37 frame, test whether 91 reads as predicative-adjective there once 37's value is named.

No standing or red-team verdict contradicted or downgraded. §7 intact (no new polyvalence). Canonical-stream caveat stands (rows a2_05/a3_02/a6_03/a7_00/a2_07 offsets unvalidated).
