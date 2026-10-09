# Battery verdict: det-14-locus-117

- Target: `det-14-locus-117` (battery-queue.json, priority 4, status queued)
- Claim: "Stress-test the @117 determiner leg against the offset-1 re-phase of row a1_03 (cf. seg-a1_01 for a1_01): does '67 14 21' survive as a contact under the rival phase?"
- Date: 2026-10-09. Worker: battery worker (agent 61ae8004-1aa0-4ad9-b0bc-fecc6170d5b8). Lock `code/crowd17/next-token/locks/det-14-locus-117.lock` created 2026-10-09T20:49:47Z; no prior/stale lock; deleted on completion.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py` (`load_rows` + `parse`). 1,847 pairs / 96 groups re-derived; asserts held. R5005 untouched. `canonical.py` never used. No invented data.

## Bar

The queue entry's `bars` field is null. Per BATTERY-PROTOCOL.md §2 the bar is
stated explicitly here rather than silently rewritten: it is derived from the
claim and the parent's brief ("decide at battery grade or fence").

**Bar (stated, not pre-registered):** "The '67 14 21' contact survives the
offset-1 re-phase of row a1_03 as a contact at battery grade."

Numbered clauses:

1. C1: Under the offset-1 re-phase of row a1_03, the triple '67 14 21'
   occurs as a contact somewhere in the row (same or relocated position).
2. C2: If C1 fails, the @117 determiner leg is phase-conditional: record
   whether the leg's evidence dissolves entirely or only relocates.

## Method

Re-derived the repaired stream in-session via `repair_parse.py`. Row a1_03
(raw digits `935945280046112167932989682167142160901958669882481102263296566`,
63 digits; repaired offset 0, 31 pairs) starts at global pair index 102.
Computed the rival phase per the lane's standard tokenization
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]` with o=1): 31 pairs.
Scanned the full off1 row for '67', '14', '21', the bigram '67 14', and the
trigram '67 14 21'. Counted stream-wide contacts on the repaired stream.

## Window-level evidence

- Repaired (offset 0) global @111–125 (row a1_03, in-row idx 9–23):
  `93 29 89 68 21 67 14 21 60 90 19 58 66 98 82`.
  The contact: @116–118 = `67 14 21` = "et [14] [21-noun]" (67='et' by the
  positional rule; 21 noun-class). This is the det-14-census @117
  determiner leg's entire contact.
- The '67 14 21' trigram is a **stream-wide hapax**: exactly 1× in 1,847
  pairs. The '67 14' bigram is likewise exactly 1×. The leg's evidence lives
  entirely on this row under offset 0.
- Rival phase (offset 1) full-row parse (31 pairs, in-row order):
  `35 94 52 80 04 61 12 16 79 32 98 96 82 16 71 42 16 09 01 95 86 69 88 24 81 10 22 63 29 65 66`
- Under offset 1: **'67' occurs 0×, '14' occurs 0×, '21' occurs 0×** in the
  row. The contact does not relocate — it is annihilated. No determiner-slot
  evidence for 14 exists anywhere in the row under the rival phase.
- Row containment: both phases yield 31 pairs (off0 drops the last digit,
  off1 drops the first), so the re-phase shifts no global index downstream
  of a1_03.
- Context (not adjudication): banked-value density is 5 banked tokens under
  off0 (46, 11×2, 29, 82) vs 2 under off1 (82, 29); granted tokens tie 2–2
  (off0: 00, 96; off1: 96, 79). The rival phase is distributionally poorer,
  but the rival phase itself is not decided here.

## Per-clause pass/fail

1. C1 — **FAIL at kill grade.** The trigram '67 14 21' occurs 0× under the
   offset-1 re-phase; moreover none of its three members occurs in the row
   at all. The contact cannot be said to survive in any sense.
2. C2 — **dissolves entirely.** The @117 determiner leg's evidence is not
   relocated, it evaporates: with no 14 in the re-phased row, there is no
   locus for any determiner-shaped reading.

## Verdict

**KILL (of the robustness claim).** The '67 14 21' contact does not survive
the offset-1 re-phase of row a1_03 — it is annihilated, not relocated. The
@117 determiner leg is **phase-conditional**: it exists only under offset 0.

## Scope

- This kills only the survival claim. It does NOT overturn det-14-census's
  PROMOTE of the @117 determiner leg: offset 0 remains the standing repaired
  parse for a1_03, and the rival phase has no independent adjudication in
  this battery (a full row-grade test in the seg-a1_01-offset1-test style
  would be a separate target).
- Untouched: 14's open global status, le-14-kill-1121 (global 'le' kill),
  stem-14 fences, 67's positional rule, 21's noun class, §7, all
  standing/red-team verdicts. Canonical-stream caveat stands.

## Follow-ups (verdict is kill, so none required; one note)

- If the red team ever re-opens a1_03's phase, the @117 leg must be
  re-derived from scratch — it has zero content under offset 1. No new
  battery target is proposed here; the row-phase question belongs to the
  offset-adjudication track (cf. seg-a1_01-offset1-test), not to 14.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-det-14-locus-117.md`
- Queue: `det-14-locus-117` queued → `verdict`/`kill`, 2026-10-09 (pre-write
  assert passed — was queued/verdictless; target-id-unique tmp
  `battery-queue.json.det-14-locus-117.tmp` + atomic rename; disk
  re-validated; own entry only; no downgrade)
- Lock `locks/det-14-locus-117.lock`: created on start, deleted on
  completion (verified gone). R5005, sealed gates, red-team adjudication
  queue untouched.
