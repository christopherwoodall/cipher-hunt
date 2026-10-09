# Battery `frame-367-la-pre` — verdict: KILL

## Bar (verbatim, pre-registered)

`test 61="la" with 70 as abbreviation of "première" ("70 17" unique stream-wide); needs 49's value`

Numbered clauses:
- C1: "70 17" is unique stream-wide (the claim's distributional premise).
- C2: 70 can carry "première" as a manuscript abbreviation at @368 — i.e. the reading "70 17" = "première fois" is licensed.
- C3: 61="la" fits the @367 window inside the joint reading.
- Adverse: 49's value is open.

## Method

Repaired 1,847-pair / 96-type stream re-derived in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types; `canonical.py` never used).
Tested C1/C2 byte-exact against the stream and the banked manuscript gloss crib.

## Window-level evidence (@-offsets, 0-based)

- Locus: @366 = 49, @367 = 61, @368 = 70, @369 = 17 (row a2_06); left @364/365 = 78/48, right @370/371 = 06/21.
- "49 61 70 17" 4-gram: exactly 1× stream-wide (@366).
- "70 17" bigram: exactly 1× stream-wide (@368). **C1 PASSES** — the uniqueness premise is byte-exact.
- Banked gloss (i) crib, byte-confirmed twice: "11 70 82 34 29 40" = "la première" at @754 (row a5_03, the gloss line itself) and @1034 (row a6_03).
- At @1034 (a6_03) the crib is followed by 17: "11 70 82 34 29 40 17" = "la première fois" **spelled in full**.
  At @754 (a5_03, the gloss line) the crib is followed by 20 62 94 59 — the same 5-cell spelling, different right context.

## Per-clause pass/fail

- C1: PASS — "70 17" is unique (@368).
- C2: **FAILS AT KILL GRADE.** The manuscript's own banked gloss proves "première" is spelled with five cells,
  70 82 34 29 40, at both crib loci — 70 carries only the syllable "pre-". A reading of bare 70 as the whole word
  "première" contradicts the banked crib segmentation; the miè-re cells (82 34 29 40) cannot be absorbed into 70.
  The a6_03 locus further proves "la première fois" is written in full ("11 70 82 34 29 40 17"), so an abbreviated
  "70 17" = "première fois" is impossible under standing ground truth. No rescue is available at battery grade:
  re-segmenting would require downgrading the banked gloss crib, which is out of battery scope (§5.2).
- C3: moot — not tested; secondary cause recorded: 61="la" would homophone-collide with banked ground truth
  11="la", with no licensed split or homophony precedent for "la" in the standing splits (20~17, 23~26 are
  different values; 09~92, 19 are holds, not "la").
- Adverse (49's value open): **answered** — the C2 kill rests on the banked crib and is independent of 49's value.
  No naming of 49 can rescue a dead abbreviation arm.

## Verdict

**KILL.** The joint claim "61='la' + 70-as-'première'-abbreviation" is dead: its 70 arm is forced false by the
banked manuscript gloss. Scope: kills only the abbreviation reading and the joint @367 claim; untouched are
pencil 70=pre, promoted 17=fois, GT 11=la, 61's open value, 49's open value, and the sibling `locus-368-fullparse`
fence (its surviving routes rest on 49/61/85 naming, none of which this kill forecloses).

No standing/red-team verdict contradicted or downgraded; §7 intact (67 sole polyvalence); no split or polyvalence
declared; canonical-stream caveat stands (row a2_06 unvalidated).

## Follow-ups

Per §4, kills regenerate no follow-ups. Re-open is red-team venue only (a naming act overturning the banked
gloss crib — out of battery scope).

## Bookkeeping

- Queue: `frame-367-la-pre` → `status: verdict`, `result: kill`, 2026-10-09 (pre-write assert: queued/verdictless;
  temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `frame-367-la-pre.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
