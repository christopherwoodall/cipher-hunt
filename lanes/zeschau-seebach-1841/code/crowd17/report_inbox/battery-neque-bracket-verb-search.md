# Battery report — neque-bracket-verb-search (instance-B 'ne...que' bracket, verb-slot hunt)

- Target id: neque-bracket-verb-search (priority 3)
- Worker: be1c1fd7-2208-4e99-8b51-b8e3f85f0271
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). canonical.py never touched.
- Lock: locks/neque-bracket-verb-search.lock created on start (no stale lock present; no prior lockfile found).
- Parent: battery-npframe-60-detleft-closeout (NULL, 2026-10-09) — the complement's 60 NP-frame hypothesis was already closed out NULL.

## Bar (verbatim, frozen BEFORE testing)

> resolve iff a licensed verb parses at the bracket's verb slot under standing values with the complement parsing; if no verb is licensable under any battery-available class, fence the window as a permanent residual with stated cause

## Bar restated as numbered pass/fail clauses (frozen BEFORE testing)

1. **Clause 1 (resolve):** A licensed verb parses at the bracket's verb slot — the position between 94@1687 ('ne') and 79@1688 ('tout') — under standing values, AND the complement 'tout [14] [60] [27]' parses under standing values.
2. **Clause 2 (fence):** If no verb is licensable at the slot under any battery-available class, fence the window as a permanent residual with stated cause.

Battery-available verb classes per §7: 80/89 verb-frames (A8), 85 verb-stem (A3), "tout me [48-verb]" frame (A7-L2), 37/32/42 predicative (A1).

## Method

1. Built the 1,847-pair stream exactly per repair_parse.py (offsets from repaired_offsets.json; 1,847 pairs confirmed).
2. Located the target window: indices 1686–1694 = `62 94 79 14 60 27 46 24 85` (row a8_05/a8_06 boundary; 46@1692 closes the bracket, 85@1694 is the next group).
3. Checked the verb slot: the pair(s) standing between 94@1687 and 79@1688.
4. Swept the whole stream for all 94…46 windows to compare slot occupancy (discriminating context, same frames).

## Window-level evidence (@-offsets, 0-based pair indices)

- @1686: 62 (glossed 'il' in the claim; note: 62 is a live "il" rival vs 84 per finder-beats 84-adjudication — the rival does not affect the verb-slot test)
- @1687: 94 ('ne', battery-promoted, pending ratification — used as given)
- @1688: 79 ('tout', granted A5) — **directly adjacent to 94; zero pairs stand between them**
- @1689: 14 (unresolved; 15/1,847)
- @1690: 60 (unresolved; NP-frame closed out NULL by parent battery-npframe-60-detleft-closeout)
- @1691: 27 (unresolved; **stream-wide hapax, 1/1,847**)
- @1692: 46 ('que', banked)
- @1693: 24 (unresolved; 52/1,847)
- @1694: 85 (verb-stem frame A3, granted — but it stands AFTER the bracket, not in the slot)

Verb-slot inventory at @1687–@1688: **empty — no pair exists between 94 and 79.**

Stream-wide 94…46 comparison (pair between 94 and 46, slot occupancy):
- @101:  [93 59 45 28 00] — 5 pairs
- @688:  [29 60 03 39 74] — 5 pairs
- @785:  [74 65 84 06 77 64] — 6 pairs
- @1182: [82 06 06 59 42 06 84 59] — 8 pairs
- @1687: [79 14 60 27] — **79 immediately after 94; verb slot (between 94 and 79) empty**
- @1742: [82] — 1 pair

The @1687 window is the ONLY one stream-wide where 79 directly follows 94, and the only one whose verb slot is a structural zero.

## Per-clause pass/fail

- **Clause 1: FAIL.** The verb slot contains zero pairs. None of the battery-available verb classes (80/89 A8, 85 A3, 48-verb A7-L2, 37/32/42 predicative A1) has any pair present at the slot to license; 79='tout' (granted A5) cannot head the slot. Licensing any verb would require inventing a pair — forbidden. Additionally, the complement does not parse under standing values: 60's NP-frame is NULL (parent), 27 is a hapax, 14 and 24 are unresolved. Clause 1's conjunction fails on both halves.
- **Clause 2: PASS (applies).** No verb is licensable under any battery-available class. The window is fenced as a permanent residual with stated cause (below).

Adverses answered: (a) "fence is a result — do not force a verb" — honored; no verb was forced, the window is fenced. (b) 79='tout' granted and 94='ne' battery-promoted pending ratification — both used as given; no claim is made about 94's ratification status and nothing is promoted. (c) '[27] que [24]' cannot open a new clause — consistent with the fence; the tail stays unresolved (see follow-up 2).

## Verdict: NULL (fence = permanent residual, not a resolution)

The instance-B 'ne…que' bracket's verb slot is a structural zero: 94 ('ne') is directly followed by 79 ('tout') at @1687–@1688 with no intervening pair, and no battery-available verb class is present at that position. Under standing values no licensed verb can parse there without inventing data. Fenced as a permanent residual.

**Stated cause of the residual:** adjacency anomaly — 94→79 with an empty verb slot, unique among the six stream-wide 94…46 windows — combined with an unresolvable complement (60 NP-frame NULL, 27 hapax). The residual is structural (missing pair), not a value dispute: no value assignment can fill a slot that contains no pair.

This result does not contradict any standing red-team verdict; it refines the parent NULL with a distributional uniqueness finding.

## Follow-up targets (null MUST propose 1–3)

1. **complement-14-60-27-head** (priority 3, battery): license a head for the complement 'tout [14] [60] [27]' under standing values. Narrower bar: resolve iff a single licensed head value parses for [14], [60], or [27] with the other two parsing as its dependents; fence as residual if 27's hapax status blocks every frame. (Rationale: the complement is the only parsable surface left in the window; the parent NULL killed only the 60-detleft frame, not all heads.)
2. **neque-tail-24-85-clause** (priority 3, battery): test whether 85 (verb-stem frame A3, granted) at @1694 opens a licensed verb clause in the tail '[27] que [24] [85]'. Narrower bar: promote iff 85 licenses a verb-stem parse with [24] as a licensed dependent under A3 conditions; kill iff the tail forces 85 into a non-verb reading; null iff A3's conditions are untestable on this frame.
3. **neque-instance-sweep** (priority 4, finder): classify all six 94…46 windows stream-wide (verb-slot occupancy, 79-adjacency, slot length distribution). Discriminating frame: establish whether the @1687 empty-slot anomaly is a singleton or part of a wider 94→79 adjacency pattern, and whether slot-length predicts which battery-available class fills it. Report to code/crowd17/report_inbox/next-token-findings-neque-instance-sweep.md.
