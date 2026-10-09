# Battery report: reseg-367-4961-bound

- Target id: `reseg-367-4961-bound`
- Claim: "Resolve the 49/61/70 boundary at @367."
- Date: 2026-10-09
- Worker: battery worker (subagent 5603e488-8d7b-4817-bcc4-c9705d322c7c)
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` per `repair_parse.py` (asserts held: 1847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "boundary" = where one word ends and the next begins in the group stream. "Stranded" = a group with no licensed word-host in either direction. "GT" = ground truth (pencil-banked).

## Parentage

Follow-up #2 of the PROMOTE `val-61-premier` (2026-10-09, locus-level): "61 40 17" @1556 = "première fois", 61 = "premier" at that locus only. That report fenced @367 ("49 61 70 17") out of scope because "premier"+"pre"+"fois" is ungrammatical — the sharpest anti-leg against any 61 extension. This battery resolves the 49/61/70 boundary itself.

## Bar (derived from the claim before testing; queue `bars` field was null)

1. **C1:** Re-derive the @367 window from the repaired stream byte-exact.
2. **C2:** Decide the 49/61/70 boundary with stated byte evidence and standing values.
3. **C3:** State the resulting parse with assumption count.
4. **C4:** Fence honestly if unresolvable at battery grade.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/reseg-367-4961-bound.lock` on start; deleted on completion.
2. Re-derived the stream in-session; all offsets below are 0-based pair indices.
3. Standing values held fixed: 70="pre" (pencil GT), 17="fois" (granted), 40="e" (pencil GT), 64="qui", 47="ce", 11="la" (granted/GT). 61="premier" adopted as locus-level @1556 only (not re-litigated, not extended). 49's value open.

## Window-level evidence

### C1 — the locus, byte-exact

@366–369 (row a2_06): `49 61 70 17`. Wider clause @355–375:
`98 92 47(ce) 11(la) 21 62 48 76 47(ce) 78 48 49 61 70(pre) 17(fois) 06 21 65 63 29(er) 85`.

Distributional facts (re-derived):
- "49 61" is a stream hapax (1/1,847). "61 70" is a stream hapax. "70 17" is a stream hapax. "49 61 70" trigram: 1×. The locus has zero repetition leverage.
- n(49)=12; dominant follower 74 ×5 (@416, @815, @860, @918, @1844); @367 is 49's sole "49 61" window.
- n(61)=18; followers varied (96×2, 59×2, 94×2, 21×2, 20, 42, 88, 24, 31, 56, 12, 40, 15, 70×1); no dominant follower, no suffix-like profile.
- n(70)=15; "70 64" (@1586, blocked rightward by granted "qui") and "36 70" are stream hapax (per stem48-qui-65-hapax).

### C2 — boundary arms, each tested

- **Arm A — "49 | 61 | pre | fois" (four free words):** requires "pre" as a free French word. The pencil gloss writes "la pre m i er e" = "la pre-mi-er-e" — "pre" is glossed as a *syllable* of "première", never as a free word. "pre" alone is unlicensed in 1841 diplomatic French. **Fenced.**
- **Arm B — "49 | [61]pre | fois":** needs a French word ending in "-pre" composed with 61. Only candidates "âpre" (61="â") and "pourpre" (61="pour"); both then require "[49] âpre/pourpre fois" — a qualitative adjective prenominal before "fois" is ungrammatical ("fois" takes première/dernière/seconde/chaque, never "âpre/pourpre"). **Fenced.**
- **Arm C — "49 | 61 | prefois":** "prefois" is not a French word. **Killed.**
- **Arm D — "[49][61] | pre | fois":** same free-"pre" defect as Arm A. **Fenced.**
- **Arm E — "[49][61]pre | fois":** needs 49+61 to compose "â"/"pour" before "pre"; no license for either composition, and "pourpre/âpre fois" fails selection as in Arm B. **Fenced.**
- **Arm F — 61="premier" extension:** "premier pre fois" is ungrammatical under standing values; this is val-61-premier's own standing anti-leg, adopted not re-litigated. **Blocked.**
- **Structural arm — 70 is stranded:** rightward continuation is 17="fois" (granted word), blocking "pre"+"fois" as one word — the same rightward block as stem48-qui-65-hapax's "70 64" (@1586, blocked by granted "qui"). Leftward, "[61]pre" is unlicensed (Arms B/E). So at @367, 70="pre" has no licensed host in either direction — the stranded-pre geometry recurs.
- **Rival arm (out of scope, noted not pre-empted):** 61="la" + 70 as manuscript abbreviation of "première" → "[49] la première fois". This needs 49's value and is the queued target `frame-367-4961-la-pre`'s venue; this battery makes no declaration on it.

C2: no boundary parse is licensable at battery grade.

### C3 — parse with assumption count

No parse survives. Assumption count is moot; every arm needs ≥1 unlicensed step.

### C4 — fence

**The 49/61/70 boundary at @367 is fenced as unresolvable at battery grade.** Stated cause: the locus is a quadruple hapax ("49 61", "61 70", "70 17" each 1/1,847), 70="pre" is stranded between granted "fois" and unvalued 61/49, and every segmentation arm (four-word, "[61]pre", "prefois", "[49][61]pre", 61="premier" extension) fails on byte-grounded French-grammar grounds. The standing anti-leg ("premier pre fois") is untouched; no standing or red-team verdict contradicted; §7 intact. Canonical-stream caveat: row a2_06 offset unvalidated.

Orthographic observation (not a finding, not a re-litigation): the parent locus promote reads "61"+"40"("e") as "première", but letter-wise "premier"+"e" = "premiere" ≠ "première" (è vs e). Noted for the red team; the locus verdict stands un-downgraded.

## Verdict: NULL (fence executed)

## Follow-ups proposed (nulls regenerate work; all verified absent from battery-queue.json)

1. `val-49-74-frame` (P3) — name 49 via its dominant "49 74" ×5 frame (@416/@815/@860/@918/@1844). 49's value is the keyhole for both this boundary and the queued `frame-367-la-pre`. Bar: name 49's value iff ≥2 of the five windows parse under one value with zero new assumptions; else fence.
2. `bound-70-abbrev-premiere` (P3) — test 70 as manuscript abbreviation of "première": the pencil gloss "la pre m i er e" writes "pre" as the head syllable; check 1841 manuscript abbreviation practice for "pre" = "première". Discriminates the la-première rival arm without pre-empting `frame-367-la-pre`.
3. `seg-61pre-lettertier` (P4) — letter-tier composition test of "61"+"pre" once the 29/40/33 syllabary resolves 61's letters. Gated on the syllabary.

## Bookkeeping

- Queue: `reseg-367-4961-bound` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
