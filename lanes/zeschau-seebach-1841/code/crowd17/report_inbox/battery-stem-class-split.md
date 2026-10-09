# Battery verdict: stem-class-split

## Bar (verbatim, pre-registered)

"census governors and post-29 complements across all stem cells (33 x5, 86 x4, 06 x4, 34/64/03 x3, 11/46/48 x2); the split holds iff the governor sets are disjoint and complement sets overlap only at [89]/m[16]"

## Restated clauses

- **C1:** The governor sets of 33 and 86 are disjoint.
- **C2:** The complement (post-29) sets of 33 and 86 overlap only at 89 and at m[16].
- **C3 (implicit):** The full census across all listed stem cells is byte-exact on the repaired stream.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/stem-class-split.lock` on start
(agent id + UTC timestamp). Re-derived the 1,847-pair / 96-type stream from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed per `repair_parse.py` (upstream tokenization `[s[i:i+2] for i in
range(o, len(s)-1, 2)]`). `canonical.py` never touched. R5005, sealed gates,
and the red-team adjudication queue untouched.

"Stem cell" = a group immediately preceding 29='er' (banked GT), i.e. the
"[X]er" infinitive shape. For each window "pre X 29 post", the GOVERNOR is
`pre` and the COMPLEMENT is `post`. Offsets below are 0-based stream indices.

Standing values used for reading (not re-litigated): 11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que (GT); 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5),
00=pour (A9), 84=on (A15), 47=ce (A4); 59=est, 77=le (provisional);
67=et/veut with the positional rule (67="veut" iff follower infinitive-shaped).

## Census (all bar cells, byte-exact)

### 33 (n=5)

| @ (0-based) | row   | governor (pre) | complement (post) | post+1 |
|-------------|-------|----------------|-------------------|--------|
| 274         | a2_03 | 67 (veut)      | 89                | 84     |
| 627         | a4_01 | 37 (open)      | 87 (ce)           | 78     |
| 1233        | a7_01 | 47 (ce)        | 85 (verb-stem)    | 56     |
| 1425        | a7_08 | 67 (veut)      | 87 (ce)           | 63     |
| 1478        | a7_10 | 67 (veut)      | 82 (m)            | 16     |

- Governors: {67, 37, 47}. 67="veut" x3 by the positional rule (each followed
  by "33 29", infinitive-shaped).
- Complements: {89, 87, 85, 82}. Takes 'ce' (87) x2. The 82-complement is
  followed by 16, i.e. the "m[16]" configuration.

### 86 (n=4)

| @ (0-based) | row   | governor (pre) | complement (post) | post+1 |
|-------------|-------|----------------|-------------------|--------|
| 432         | a2_09 | 77 (le, prov.) | 82 (m)            | 16     |
| 1376        | a7_06 | 00 (pour)      | 89                | 84     |
| 1392        | a7_07 | 67 (veut)      | 89                | 16     |
| 1826        | a8_11 | 00 (pour)      | 82 (m)            | 38     |

- Governors: {77, 00, 67}. 00="pour" x2 (granted A9); 77="le" x1
  (provisional); 67="veut" x1 by the positional rule ("86 29" is
  infinitive-shaped, so the rule fires at @1392).
- Complements: {82, 89}. The 82 at @432 is followed by 16 ("m[16]"); the 82
  at @1826 is followed by 38 ("m[38]", 86-specific, not shared).
- **86 never takes a 'ce' complement** (no 87, 47, or 45 in 0/4 windows).

### 06 (n=4) — the adverse's "unexamined" cell, now examined

| @ (0-based) | row   | governor | complement | post+1 |
|-------------|-------|----------|------------|--------|
| 1097        | a6_06 | 81       | 67         | 86     |
| 1389        | a7_07 | 16       | 67         | 86     |
| 1710        | a8_06 | 12       | 40         | 65     |
| 1816        | a8_10 | 42       | 37         | 01     |

- Governors: {81, 16, 12, 42}. Complements: {67, 40, 37}.
- 06 is a distinct profile: never veut-governed, never pour-governed, takes
  67/40/37 complements. It patterns with neither 33 nor 86. The "06-29
  unexamined" adverse is now answered.

### Remaining bar cells (context)

- **34 (n=3):** governors {08, 82, 82}; complements {40 x3}. Uniform "m [34]er e" / "[08] [34]er e" shape.
- **64 (n=3):** governors {09, 92, 16}; complements {40, 40, 45}. Note @1200:
  "64 29 45" — 45 is the 'ce'/'dict' group (A11 HOLD).
- **03 (n=3):** governors {01, 24, 81}; complements {80 x3}. Uniform "[X] [03]er [80]" shape; cf. battery-imp-80-set and battery-stem-03-value.
- **11 (n=2):** governors {00, 47}; complements {42, 40}. @78: "pour [11]er [42]".
- **46 (n=2):** governors {97, 59}; complements {85, 42}.
- **48 (n=2):** governors {82, 65}; complements {47 x2} — 48 takes 'ce' (47)
  x2, a 'ce'-complement profile like 33's but via 47 rather than 87.

## Clause results

### C1 (governor sets disjoint): FAIL

- 33 governors: {67, 37, 47}
- 86 governors: {77, 00, 67}
- Intersection: **{67}**. 67="veut" (positional rule) governs 33 at
  @274/@1425/@1478 and governs 86 at @1392 ("67 86 29", row a7_07:
  "06 29 | 67 86 29 89 | 16 76 47").
- The overlap is a single group type, manifesting in 1 of 86's 4 windows.
  It is real under the standing positional rule, not a misread: "et [86]er"
  is grammatical, but the rule ("67='veut' iff follower infinitive-shaped")
  stands and fires here.

### C2 (complement overlap only at [89]/m[16]): PASS (careful reading)

- 33 complement groups: {89, 87, 85, 82}
- 86 complement groups: {89, 82}
- Group-level intersection: {89, 82}.
- 89 is explicitly allowed. For 82: 33's 82 (@1478) is followed by 16 and
  86's 82 (@432) is followed by 16 — the shared configuration is exactly
  "m[16]". 86's additional 82 (@1826, followed by 38, "m[38]") is
  86-specific and creates no additional overlap.
- The overlap is therefore confined to 89 and m[16], as the bar allows.

### C3 (census byte-exact): PASS

All counts match the bar's stated n (33 x5, 86 x4, 06 x4, 34/64/03 x3,
11/46/48 x2); every window re-derived from the repaired stream.

## Adverses

1. **"06-29 unexamined": ANSWERED.** 06's 4 windows are censused above; 06
   has a third profile (governors 81/16/12/42; complements 67/40/37) and
   does not disturb the 33-vs-86 comparison.
2. **"37/47/77 open": PARTLY STALE, REST FENCED.**
   - 47="ce" is GRANTED (A4 allophone tier), not open; it governs 33 at
     @1233 without issue.
   - 77="le" is PROVISIONAL (governor of 86 at @432); the pour/le arm of
     the claim rests partly on a provisional value — noted, not a failure.
   - 37 is OPEN (governor of 33 at @627); no interpretation in this report
     depends on 37's value.

## Verdict: NULL

The strict bar fails on C1 (governor sets share 67="veut" via @1392), so
this is not a promote. It is not kill-grade: the failure is a single shared
governor, not a systematic refutation. The substantive valency distinction
is supported by the data:

- 33 takes 'ce' complements (87 x2, @627/@1425); 86 never takes any 'ce'
  (0/4 across 87/47/45 — clean).
- 33 is veut-heavy (3/5 governors); 86 is pour/le-heavy (3/4 governors).
- Complement profiles differ (33: ce/89/85/m[16]; 86: 89/m[16]/m[38]).

"Valency-distinct" holds as a gradient/distributional claim; the bar's
strict disjointness operationalization is what fails, on one window. This
needs red-team adjudication on whether the bar should be refined or the
@1392 "veut" reading revisited.

No standing verdict contradicted or downgraded. No polyvalence declared
(§7 intact). The 67="veut" reading at @1392 follows the standing positional
rule; no rival segmentation is asserted here.

## Follow-ups proposed (for supervisor queuing)

1. `veut-86-1392-adjudicate` (P2) — The sole governor overlap is @1392.
   The positional rule forces 67="veut", but "et [86]er" is grammatical.
   Adjudicate whether the rule definitively resolves @1392 or a re-read is
   available; if 67="et" there, C1 passes and the strict bar holds.
2. `stem-valency-gradient` (P3) — Reframe as a distributional test:
   compute governor/complement distribution divergence (33 vs 86) across
   the full census instead of strict set disjointness.
3. `ce-complement-86-negative` (P3) — Sweep ALL 86 windows (n(86)
   stream-wide, not just the 4 stem-29 cells) for any 'ce'-group complement
   (87/47/45). A clean negative hardens the "86 never 'ce'" arm, which is
   the sharpest part of the distinction.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-stem-class-split.md` (this file).
- Queue: `battery-queue.json` `stem-class-split` → status `verdict`, result
  `null`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write).
- Lock: created on start with agent id + UTC timestamp; deleted on
  completion.
