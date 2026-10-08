# Battery report: ver78-296-reparse

Target: ver78-296-reparse | priority 2
Claim: @296 '11 78 40 97 86' re-parses cleanly under 78='ver'
Worker: 478ccc93-d5f2-421c-a944-1d86a890f1eb | 2026-10-08

## Bar (verbatim, pre-registered)

"(a) 97 and 86 given values/frames from their own batteries; (b) 'la ver-e-[97]-[86]' reads as one French word under 78='ver' — or the residual stays fenced with the failure stated"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. 97 and 86 carry values/frames given by their own batteries.
2. The string 11-78-40-97-86 (@296..@300) reads as one French word under
   78='ver' (11='la' banked, 40='e' banked) — or the residual stays fenced
   with the failure stated.

## Method

Parsed `data/upstream-ct_R5005.txt` with
`code/side-keyhunt/repaired_offsets.json` exactly like
`code/side-keyhunt/repair_parse.py` (stride-2 pairing per row offset).
Verified: 1,847 pairs. @n = pair-index offsets. `canonical.py` not used.
R5005, sealed gates, red-team queue untouched.

## Window-level evidence (@-offsets)

@296 window (rows a2_03..a2_04):

`64 29 40 65 16 01 [11]@296 78@297 40@298 97@299 86@300 91@301 18 89 88`

So the target 5-gram is 11@296 - 78@297 - 40@298 - 97@299 - 86@300,
i.e. "la" + "ver" + "e" + [97] + [86] under 78='ver'.

### 97 census (re-derived, n=10)

All 10 windows: @2 `00 97 51`; @94 `81 97 46`; @288 `00 97 09`;
@299 `40 97 86` (target); @525 `81 97 47`; @566 `80 97 13`;
@588 `00 97 41`; @751 `02 97 40`; @1412 `16 97 69`;
@1823 `00 97 00 86 29`.

Predecessors: 00='pour' x4, 81 x2, 40/80/02/16 x1 each.
Successors: 10 distinct singletons (51, 46='que', 09, 86, 47='ce',
13, 41, 40='e', 69, 00). No 97 battery exists in any crowd inbox;
no red-team ruling names 97's value or frame. 97's only standing
signal is the pour-governed contact pattern ('pour'+97 x4, mirroring
86's 'pour'+86 x12).

### 86 census (re-derived, n=32)

Predecessors: 00='pour' x12, 77='le' x5, 67 x3, 83 x2, others x1.
Successors: 29='er' x4, 56 x4, 24/01/52/66 x2, 18 singletons.
Standing frames (not values): A9 INF-class grant (pre=00 x12,
suc=29 x4 '86-er', 33-parallel); R17-012 substantivized
infinitive/noun frame ('le 86' x5, subject-shaped before "n'est").
86's own value battery (stem-86) is QUEUED, not run — no battery has
verdict on 86's value. No `86="<value>"` claim exists in any inbox.

### 97-86 contact

The bigram 97-86 occurs exactly once in the stream: @299, the target
window. No joint-frame precedent exists to borrow.

## One-word family sweep ("la"+"ver"+"e"+[97]+[86])

With 11='la' and 40='e' banked (§7, not negotiable), the letter string
is fixed as "la"+"ver"+"e"+[97]+[86] = "lavere"+[97]+[86], or with 11
as article, "la"+"vere"+[97]+[86]. French lexicon admits exactly two
families:

1. "lavere*": only "lavèrent" (l,a,v,è,r,e,n,t — 3pl of laver).
   Requires 97='n', 86='t'. 97='n': "pour"+97 x4 becomes "pour n"
   (ungrammatical); collides with the promoted 12='n' (n-e-12-48
   battery) with no homophony test run. 86='t': "pour"+86 x12 and
   'le 86' x5 become "pour t"/"le t" (ungrammatical); contradicts the
   A9 INF-class and R17-012 substantivized-infinitive frames.
   FAIL at frame level for both groups.
2. "vere*": only "véreux"/"véreuse" (v,é,r,e,u,x / ...u,s,e).
   Requires 97+86="use"/"ux". 97='u' or 'us': "pour"+97 x4 fails as
   above. 86='s' or 'e': "pour"+86 x12 fails. FAIL at frame level.
   Additionally "la véreuse" is two words (article + adjective), not
   the one word the bar demands, and stands noun-less.

No other French word begins "lavere" or "vere" with 4th letter 'e'.
The one-word read is lexically exhausted: the only completions force
97/86 values that their own contact profiles reject at frame level.

## Per-clause pass/fail

1. **FAIL.** 97 has no value or frame from any battery (none exists;
   no red-team frame either). 86 has red-team frames (A9 INF-class;
   R17-012 substantivized infinitive/noun) but its own value battery
   (stem-86) is still queued — clause (a) asks for values/frames
   "from their own batteries", which do not exist yet for either
   group. The clause is untestable-as-satisfiable on today's board,
   not merely untested.
2. **FAIL (fenced, failure stated).** The one-word sweep above
   exhausts the lexicon: the only French completions ("lavèrent",
   "véreux/véreuse") demand 97/86 values contradicted by their
   contact profiles, and "la véreuse" is two words anyway. The
   rival 'l'ere' read (11-78-40 as "la ...ère"-shaped) is not
   displaced — it stands, exactly as the queue's adverses record.

No positional-allophone reconciliation was attempted (rejected under
lane law by R16-005; 67 et/veut remains the sole true polyvalence per
§7 — no second polyvalence declared here).

## Verdict: NULL

Not promote: neither bar clause passes. Not kill: no window forces
the claim false — @296 stays compatible with 78='ver' as a fenced
1-window residual, consistent with the standing R16-005 LEAD grading
(ratified R17-006) and the confirmed 78='er' kill (R17-014). This
result contradicts no standing red-team verdict; nothing is
downgraded.

**@296 stays fenced** as the red-team-fenced 1-window residual
(R16-005), with the failure stated: (i) 97/86 lack battery-derived
values/frames, so the re-parse has no licensed completion; (ii) the
lexical sweep shows the only French completions force 97/86 values
their own profiles reject.

## Follow-up targets (required for null)

1. **frame-97-profile** (priority 2). Claim: 97's class is named from
   its contact profile. Bars: (a) class named (infinitive? noun?
   verb?) with >=3 frame-legs from the 10-window census
   ('pour'+97 x4, 81-97 x2, 97-46 'que', 97@1823 'pour 97 pour 86er');
   (b) the 97-86 @299 contact explained or fenced with cause.
   Evidence: census in this report. Adverses: n=10 (thin); 81's
   value open; 97-86 bigram is a hapax.
2. **ver78-296-97gate** (priority 3). Claim: this re-parse re-runs
   cleanly once frame-97-profile AND stem-86 have verdict. Bars:
   (a) 97 and 86 values/frames taken from their verdict batteries;
   (b) the one-word read demonstrated, or the residual re-fenced
   with the then-current failure stated. Gate only — do not force
   before both batteries verdict.
3. **lere-296-rival** (priority 3). Claim: the standing 'l'ere'
   rival read of 11-78-40 @296 is tested directly. Bars: (a) name
   the word 78-40 completes (coordinate with noun/adjective
   batteries; "la [X]ère"-shaped candidates); (b) or kill the rival
   at kill grade with the window re-parsed under 78='ver'.
   Evidence: @296 window; 78-40 x3 (@297/@352/@819). Adverses:
   78='ver' LEAD stands (R16-005/R17-006); R16-005 fence respected.

## Reproducibility

All counts re-derived in-session from the repaired 1,847-pair stream
via `repair_parse.py` parsing (no script file written; commands
logged in worker session). No numbers invented; every @-offset
traces to the stream.
