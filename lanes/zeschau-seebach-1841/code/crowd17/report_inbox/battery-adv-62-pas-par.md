# Battery verdict: adv-62-pas-par

## Bar (verbatim, pre-registered)

> parse @44–48 as "pas [62-adv] par" with stated adverb candidate; fence if no candidate parses

Numbered clauses (pre-registered before testing):
1. (Parse arm) One stated adverb candidate X makes "pas X par" parse grammatically at @44–48.
2. (Fence arm) If no candidate parses, fence @46 as adverb-incompatible with stated cause.

Origin: null follow-up #3 of battery-seg-30-62-96 (the pas-30 battery's "...pas par... ('not by ...')" gloss at @45 skipped 62; a named adverb would close the gap with 62 as an independent word).

## Method

Read BATTERY-PROTOCOL.md first; lock `locks/adv-62-pas-par.lock` created on start (agent id + UTC), no stale lock present; deleted on completion. Re-derived the window from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` — same tokenization, re-run inline). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.

Standing values honored and not re-litigated: 30="pas" (battery-promoted), 96="par" (granted), 00="pour" (A9 granted).

## Window-level evidence (@-offsets, repaired stream)

Re-parse of row a1_01 (byte-exact, 0-based @):

| @ | pair | row | standing value |
|---|------|-----|----------------|
| 44 | 81 | a1_01 | — (open; seg-81-30-boundary queued owns the left edge) |
| 45 | 30 | a1_01 | **pas** |
| 46 | 62 | a1_01 | — (target) |
| 47 | 96 | a1_01 | **par** |
| 48 | 00 | a1_01 | **pour** |
| 49 | 92 | a1_01 | — |

Window @44–48 = "81 30 62 96 00" = "[81] pas [62] par pour". Matches seg-30-62-96's byte-exact re-parse.

## Census (repaired stream, re-derived)

- "30 62 96" occurs **exactly once** stream-wide: @45 (the target window). No second "pas [62] par" frame exists.
- 62's full successor distribution (n=38): 94 x9, 48 x6, 98 x5, 16 x4, 61 x2, 06 x2, **96 x1**, 91 x1, 21 x1, 18 x1, 38 x1, 46 x1, 93 x1. 62 never precedes 00 or 39 — no "pas [62] pour/à" frames exist anywhere.
- 30's successor distribution: 06 x4, 03 x3, 67 x2, 20 x2, 62 x1, 01 x1, 69 x1, 09 x1, 92 x1, 82 x1, 64 x1, 15 x1.

## Clause 1 test (Parse arm): candidate sweep — FAIL

Tested candidates in the frame "pas X par pour [92]" (@45–48):

- **"même"** ("pas même par" = "not even by") — the idiomatic candidate. Dies at the right edge: @47=96 ("par") is immediately followed by @48=00 ("pour"), and "par" requires a nominal complement that "pour" cannot supply. "par pour" is ungrammatical in French at any period. Additionally "même" is incompatible with 62's other contacts: 62-06 x2 reads "donnent"/"mènent" (3pl, nn-final stem per battery-sel-62-48-94) — "mèment" is not French.
- **"seulement"** ("pas seulement par" = "not only by") — same right-edge death: "par pour" ungrammatical.
- **"encore"** — "pas encore par" is ungrammatical (encore needs its own complement; "pas encore" = "not yet", cannot license a following "par").
- **"tout"** — "pas tout par" ungrammatical.
- **"plus" / "moins"** — "pas plus/moins par" ungrammatical as standalone adverb + "par".
- **"si" / "tant" / "davantage"** — none licenses a following bare "par" without its complement.

No clause-boundary escape: there is no byte evidence for punctuation or a boundary between @47 and @48 (mid-row a1_01), and "par" cannot end a clause hanging without its complement in 1841 French.

**Clause 1: FAIL.** No adverb candidate parses at @44–48.

## Clause 2 test (Fence arm): fence with stated cause — FIRES

@46 is fenced as adverb-incompatible. Causes, all byte-grounded:

1. **Right-edge impossibility:** under granted 96="par" + 00="pour", the window's right edge is forced "par pour", which no French adverb salvages (C1 sweep).
2. **Frame uniqueness:** "30 62 96" is a hapax (n=1, @45). The parent battery's stricter naming bar (≥2 independent "pas [adv] par/pour/à" frames) is unreachable — no second frame exists, and 62 never precedes 00/39, so the adverb hypothesis has exactly one testable window, and it fails.
3. **Distributional incompatibility:** 62-06 x2 forces an nn-final stem ("donnent"/"mènent"), incompatible with any adverb candidate that could occupy the "pas X par" slot.

This fence is window-local (adverb-62 at @44–48), not a global class verdict on 62. 62's class remains open (class-62-nof94 returned null on the non-94 windows).

## Standing-state check

- No contradiction: battery-lex-passepartout-48 (kill, 2026-10-09) already closed the compound-word route at @44–48; seg-81-30-boundary (queued) owns the 81–30 left edge; class-62-nof94 (null) leaves 62's class open.
- No standing red-team verdict touched. §7 honored — no polyvalence declared.

## Verdict: NULL (fence executed)

The adverb hypothesis for 62 at @44–48 is fenced with stated cause. Nothing is named.

## Follow-ups (null regenerates work)

1. `part-62-46-slot` (P3): test 62 as past-participle/participial at @46 — "pas [62-part] par" is the last open word-class between "pas" and "par" under granted values; fence iff no participial candidate parses. Coordinates with (does not duplicate) queued seg-81-30-boundary (left edge) and class-62-nof94's null (class still open).
2. `bound-96-00-clause` (P3): test a clause boundary between @47 and @48 with byte evidence — if "par" can strand with an elided complement (ungrammatical in 1841 French, but state the evidence), the adverb arm revives; fence iff no boundary evidence exists.
3. `pasX-adverb-census` (P3): census all "30 X" (pas+X) bigrams stream-wide for adverb-shaped X with a complement-bearing right edge — if some other group parses as an adverb after "pas", compare its contact profile to 62's to bound the adverb hypothesis distributionally.

## Bookkeeping

- Lock `locks/adv-62-pas-par.lock` created on start, deleted on completion.
- `battery-queue.json`: target `adv-62-pas-par` queued → verdict/null (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated post-write).
- R5005, sealed gate instances, red-team adjudication queue untouched. `canonical.py` never used.
