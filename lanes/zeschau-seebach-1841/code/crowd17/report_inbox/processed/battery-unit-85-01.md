# Battery report: unit-85-01

- Target id: `unit-85-01`
- Claim: "85-01 x2 (@595/@1439) is a two-group word/unit ('[stem]-ci' demonstrative postfix, parallel to the A12 37-01 unit)"
- Date: 2026-10-09
- Worker: battery worker (subagent cb38decc-9930-42b2-a19e-151b0bb56c51)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; n=1847 asserted, 96 groups asserted).
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/unit-85-01.lock` (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"promote unit iff ONE French word-formation reading (e.g. '[stem]-ci' demonstrative postfix, parallel to the A12 37-01 unit) covers both windows with stated boundary evidence; kill iff the two windows force different segmentations. (Resolves battery-stem-85 Adverse 1's frame either way.)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1, promote) ONE French word-formation reading of the two-group "85-01"
   parses grammatically at BOTH @595 and @1439, with the word boundary after
   01 stated and evidenced at each window.
2. (C2, kill) The two windows force DIFFERENT segmentations of the "85-01"
   bigram (the claimed uniform boundary-after-01 cannot hold at both).
3. (C3) Adverses answered: (a) "01='ci' ungranted (nominal parse of @595
   conditional only)"; (b) "@984 '45-01-24' is the A11-HOLD-dependent
   counterpoint — coordinate with bound-ci-984-standalone."

## Method

1. Re-derived the repaired parse in-session (1,847 pairs, 96 types asserted).
2. Located both "85-01" bigrams byte-exact: @595 (row a4_00) and @1439
   (row a7_08); confirmed the bigram occurs exactly 2x stream-wide.
3. Tested the bar's example reading ("[stem]-ci" demonstrative postfix) and
   every other nameable 'ci'-final word ("merci", "voici", "ceci"-family)
   against both windows under standing grants only.
4. Adopted as premises (not re-litigated): 79='tout' PROMOTED (A5) forcing a
   nominal function after "tout" (stem-85 Adverse 2); 29='er' banked GT;
   85 = verb-stem frame grant (A3); ci-01-value KILL of general 01='ci'
   (2026-10-08); bound-ci-984-standalone PROMOTE (bound-'ci' licensed in
   ce-contexts).

## Window-level evidence

### W1 @595 (row a4_00, 0-based)

Full row: `41 09 00 92 79 85 01 29 40 03 39 26 96 45 93 54 64 39 64 02 58 47 77 87 83 70 88 10`
= "…[41][09] pour(00) [92] tout(79) [85][01] er(29) e(40) [03] [39] [26]
par(96) ce(45) [93] [54] qui(64) …"

- "tout" (79, A5-granted) forces a nominal word after it.
- Unit reading (i): "[85]-ci" + new word "29 40" = "er e" ("ère", era).
  Full: "pour [92] tout [85]-ci ère [03]…". DEAD twice over: (a) the
  demonstrative postfix -ci requires a demonstrative determiner
  (ce/cet/celui); "tout X-ci" is ungrammatical in 1841 French;
  (b) bare "ère" without an article is ungrammatical. No other French
  word "ere…" fits the two groups. Word-final-'ci' at W1 is kill-grade
  dead.
- Reading (ii): "85-01-29" = "[85]cier" (the -cier nominal suffix:
  mercier/épicier/sourcier/financier family; 29='er' is banked GT, so
  "01-29"='cier' needs only word-internal "ci", which ci-01-value
  explicitly left open). "tout [85]cier" = "tout [noun-masc]" —
  grammatical shape; 40='e' then opens the next word ("e[03]…").
  LIVE — and it makes 01 word-INTERNAL, i.e. NO boundary after 01.
- Reading (iii): "85-01-29-40" = "[85]cière" (feminine): "tout [85]cière"
  — gender clash with masculine "tout" → dead.
- Forced segmentation at W1: 01 groups RIGHTWARD with 29 (the -cier
  continuation is the unique live parse; every word-final-'ci' parse is
  kill-grade dead). Boundary after 29, not after 01.

### W2 @1439 (row a7_08/a7_09 boundary)

Context: `…64(qui) 52 82(m) 16 24 85 01 52 | 68 59 37 64(qui) 77…`
(row a7_08 ends @1441 = 52; a7_09 begins @1442 = 68)
= "…qui [52] m(82) [16] [24] [85][01] [52] | [68] [59] [37] qui…"

- Unit reading (i): "[24] [85]-ci [52]". Under 24=finite-verb
  (class-level battery promote): bare "X-ci" NP without a determiner in
  post-verbal position is ungrammatical (French requires "ce X-ci" /
  "cet X-ci"); as subject of est-59, "X-ci est [37]" is equally
  unlicensed. Under 24='en' (A3 GT): "en X-ci" is ungrammatical.
  Robust to the standing 24 conflict — dead either way, kill grade.
- "merci" (85='mer'): W1 already kills it globally ("tout merci" +
  stranded "er e" ungrammatical); 85='mer' also contradicts the A3
  verb-stem grant. Dead.
- "voici" (85='voi'): W1 kills it globally ("tout voici"
  ungrammatical). Dead as a uniform word.
- "ceci" (85='ce'): contradicts A3 (85 = verb-stem frame); 'ce' is a
  determiner. Dead.
- No rightward grouping available at W2 (successor is 52, not 29; 52's
  value open; no -cier continuation). No licensed word-final-01 reading
  exists. The claimed boundary-after-01 is kill-grade dead here for a
  DIFFERENT reason than at W1 (licensing/position, not following bytes).

### The 'ci' license question (adverse a)

General 01='ci' is kill-grade dead (ci-01-value, W1@40/W2@828/W3@984).
Bound-'ci' is licensed ONLY in ce-contexts — confirmed by
bound-ci-984-standalone PROMOTE (@984 '45-01', A11-HOLD-dependent).
Neither W1 ("tout [85]-01") nor W2 ("[24] [85]-01") is a ce-context,
so the "[stem]-ci" unit reading has no licensed 01 value at either
window. The ci-bound-01 null does not extend the license (ce-contexts
only). Adverse (a) answered: the "@595 nominal parse conditional on
01='ci'" is now CLOSED, not merely unforced — "tout [85]-ci" is
kill-grade dead at W1.

## Per-clause pass/fail

1. (C1, promote) **FAIL.** No ONE French word-formation reading covers
   both windows. The bar's example ("[stem]-ci" demonstrative postfix)
   is kill-grade dead at W2 (no licensed bare "X-ci" post-verbally
   without a determiner, under either 24 reading) and kill-grade dead
   at W1 ("tout X-ci" ungrammatical; "29-40" stranded). "merci",
   "voici", "ceci" each die globally (W1 kills all three) or
   contradict standing grants (A3). No other reading is nameable
   (85's value open; stem-85 null).
2. (C2, kill) **PASS.** The windows force different segmentations:
   W1 forces 01 word-INTERNAL, grouped rightward with 29 (the -cier
   continuation is the unique live parse; boundary after 29, not 01).
   W2 admits no rightward grouping (successor 52, no -cier) and no
   licensed word-final-01 reading — the claimed uniform
   boundary-after-01 is dead at both windows, in incompatible ways.
   No single segmentation of "85-01" survives both windows.
3. (C3) **PASS.** Adverse (a) answered above. Adverse (b) answered:
   bound-ci-984-standalone PROMOTE is adopted as a premise — the
   @984 '45-01' "ceci" reading stands UNDER A11 HOLD in its ce-context
   and is consistent with this kill (the bound-'ci' license is
   ce-context-restricted; @595/@1439 are not ce-contexts). No
   contradiction.

## Verdict: KILL

The two-group word/unit "85-01" is dead at battery grade. The claimed
uniform boundary after 01 holds at neither window, and the windows
force incompatible segmentations (W1: 01 word-internal via the -cier
continuation; W2: no licensed 'ci'-final word in post-verbal position).

### Resolution of battery-stem-85 Adverse 1 (per the bar)

Adverse 1 fenced the @595 window as: verbal-signal reading unforced,
nominal "tout [85]-ci" parse available-but-conditional on ungranted
01='ci'. This kill removes the nominal rescue THROUGH "-ci": the
"tout [85]-ci" parse is now dead, not merely conditional. The window's
only live parse is the word-internal "-cier" one ("tout [85]cier"),
which is CONSISTENT with the nominal frames (F2 under 79='tout'
PROMOTED) — so the "verbal signal" reading of Adverse 1 remains
unestablished, and the nominal side no longer runs through a
demonstrative postfix. The F1 (verb-stem) vs F2 (nominal) tension for
85 stands as recorded for the red team; this kill does not name 85's
value and does not touch the A3 frame grant.

## Standing state

- A12's 37-01 unit grant untouched (different bigram).
- ci-01-value KILL strengthened (general-'ci' dead; this kill closes
  the last 'ci'-postfix-shaped nominal rescue outside ce-contexts).
- bound-ci-984-standalone PROMOTE untouched (ce-context license
  confirmed and scoped).
- stem-85 NULL untouched; its Adverse 1 frame resolved as above.
- No red-team verdict contradicted or downgraded. §7 intact (no
  polyvalence declared). Canonicality caveat stands (verdict holds on
  the canonical stream per protocol).

## Follow-ups proposed (optional; kill regenerates work)

1. `cier-85-595-name` (P3): the surviving W1 parse is "tout [85]cier"
   + "e[03]…" — test the -cier nominal family (mercier/épicier/
   sourcier/financier) against 85's contact profile; name 85's value
   iff one family member's stem fits 85's other windows. (Would feed
   the F2 nominal side of the 85 question, not the verbal side.)

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-unit-85-01.md`
- Queue: `battery-queue.json` → `unit-85-01` status `verdict`, result
  `kill`, date 2026-10-09 (temp-file + rename; pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write; only
  this entry touched).
- Lock created at start, deleted on completion.
