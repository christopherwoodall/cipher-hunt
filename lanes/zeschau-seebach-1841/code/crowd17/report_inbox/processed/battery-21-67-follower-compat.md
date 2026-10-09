# Battery report — 21-67-follower-compat

- Target: `21-67-follower-compat` (priority 3)
- Verdict: **null**
- Date: 2026-10-09
- Worker agent id: worker-21-67-follower-compat-subagent

## Bar (verbatim from battery-queue.json)

> Test each of the eight 21-67 windows under the named 21 value; an incompatible frame must fail at battery grade (parse contradiction), not stylistic judgment.

## Bar restated as numbered clauses

1. A named value for token 21 exists in the lane's standing record (banked ground
   truth, promoted/granted, provisional, or a red-team-ratified assignment).
2. Each of the eight `21 67` windows (followers 93/14/77/91/78/33/86/78) is parsed
   as `[21] et <follower>` under that named value.
3. Any incompatible frame fails at battery grade — a parse contradiction
   (structural impossibility), not a stylistic judgment.

## Finding: the bar is untestable as written (clause 1 fails)

The bar's gating precondition — "the named 21 value" — is not satisfied. No named
value for 21 exists in the standing record:

- Banked ground truth (pencil), promoted/granted, provisional (§7 of the battery
  protocol): 21 appears in none of the lists. Provisional covers only 59=est and
  77="le".
- Red team: `crowd3/red_team_results.md` line 202 treats **21="les"** as an
  "unconfirmed bonus lead", and notes that worker's own admission that
  "21→67→33→29 is ungrammatical under 21='les'".
- Battery record on 21: `battery-name-21-obj.md` tested 21="suite" → **null**;
  `battery-rival-21-feminine.md` → **null** ("21='suite' is a LEAD only");
  `battery-suite-21-qui-que.md` → **kill** (the "suite" hypothesis killed at that
  frame); `battery-de-frame-21-class.md` → **promote** only for "21 = noun class"
  (a class assignment, not a value). `suite-21-residuals` remains queued.

Per protocol §2, a genuinely untestable bar is recorded as a finding and counts
as a **null** — the bar is not silently rewritten to test under a mere LEAD.

## Method

Repaired-stream parse only: `code/side-keyhunt/repaired_offsets.json` applied to
`data/upstream-ct_R5005.txt` with byte-exact upstream tokenization
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]`, same as
`code/side-keyhunt/repair_parse.py`). 1,847 pairs confirmed. `canonical.py` was
not used. R5005 was not touched.

## Window-level evidence (all eight windows located in the repaired stream)

| @offset | row   | context (pairs)                    | follower | next-after |
|---------|-------|------------------------------------|----------|------------|
| @109    | a1_03 | 00 46 11 **21 67** 93 29 89        | 93       | 29         |
| @115    | a1_03 | 29 89 68 **21 67** 14 21 60        | 14       | 21         |
| @505    | a3_00 | 56 39 68 **21 67** 77 62 94        | 77       | 62         |
| @850    | a5_07 | 96 40 62 **21 67** 91 51 64        | 91       | 51         |
| @1162   | a6_09 | 82 44 83 **21 67** 78 45 13        | 78       | 45         |
| @1422   | a7_08 | 79 15 33 **21 67** 33 29 87        | 33       | 29         |
| @1456   | a7_09 | 92 62 61 **21 67** 86 66 79        | 86       | 66         |
| @1841   | a8_11 | 42 44 83 **21 67** 78 49 74        | 78       | 49         |

Follower set matches the target brief exactly: 93/14/77/91/78/33/86/78 (8 windows,
78 twice). The windows are real; the gate is what fails.

Standing knowledge on the followers (from the battery queue, no new claims made
here):

- 93: verb frame battery-**promoted** (`verb-93`).
- 91: verb frame battery-**promoted** (`verb-91-277-frame`).
- 77: provisional "le".
- 86: `homophone-86-split` null, `le-86-determiner-subset` null.
- 67: sole true polyvalence — 67="veut" iff follower infinitive-shaped, else
  67="et" (positional resolution rule, standing §7).

Noteworthy without a named 21 value: if the 67 positional rule resolves 67="veut"
in the @109 (follower 93, verb) and @850 (follower 91, verb) windows, the
"[21] et <verb>" reading the claim contemplates does not even apply there — the
compat test must branch on the 67 resolution per window, not assume 67="et"
uniformly. This is why the null regenerates sharper work rather than ending.

## Per-clause pass/fail

1. Named 21 value exists — **FAIL** (no named value; untestable as written).
2. Eight windows parse as [21] et \<follower\> under named value — **UNTESTABLE**
   (depends on clause 1; windows themselves located and listed above).
3. Incompatible frames fail at battery grade — **UNTESTABLE** (depends on
   clause 1; stylistic judgment would be the only substitute — excluded by bar).

## Verdict

**null** — bar untestable as written (clause 1 fails: 21's value is not named).
Nulls regenerate work; they never end it.

## Follow-ups (verified absent from battery-queue.json)

1. **`21-67-follower-compat-rearm`** (P3): re-dispatch this exact target once a
   21 value is named — gated on any verdict promoting a 21 value (e.g.
   `suite-21-residuals` promote, or a future `val-21-*` promote). Carry over the
   eight @-offsets above; they are verified against the repaired stream.
2. **`21-67-verb-followers-67pos`** (P3): test @109 and @850 under the standing
   67 positional rule — determine whether followers 93/91 are infinitive-shaped
   (→ 67="veut", compatibility question moot) or not (→ 67="et", run the
   parse-contradiction test on "[21] et <verb>" once 21 is named). Bars: for each
   window, state the 67 resolution and cite the infinitive-shape evidence.
3. **`21-les-1422-falsifier`** (P3): battery-grade test of the red team's bonus
   lead 21="les" on the discriminating window @1422 (21 67 33 → 29) — a parse
   contradiction there would kill "les" outright; a clean parse fences it as a
   standing candidate. The red team already flagged this window as
   "ungrammatical under 21='les'"; this turns that observation into a verdict.

## Anomalies

None observed in the stream or pipeline. Lock was absent (no predecessor
attempt). No red-team contradiction encountered — nothing to overwrite; standing
record left untouched.
