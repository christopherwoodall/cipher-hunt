# Battery report: split-13-secondleft

Target: `split-13-secondleft`. Claim: "the -2 slot ({23,40,79,92} arm A vs
{60,64,78,80,91,93} arm B, value-disjoint, n=12) carries the positional
separator this battery could not read".
Date: 2026-10-09. Worker: 47533f98-5f14-414a-9291-2e3b5826c5fb (battery worker).
Lock `locks/split-13-secondleft.lock` created 2026-10-09T15:47:33Z (no
pre-existing lock for this id); deleted on completion.

Parent: battery-split-13-det-pron (NULL, 2026-10-09) follow-up #2. Its arms:
Arm A = verb-follower windows of 13 (n=5: @68/@822/@1381/@1554/@1684);
Arm B = non-verb-follower windows (n=7:
@139/@456/@481/@567/@575/@1166/@1360). No positional separator found on any
tested candidate except the value-disjoint -2 slot, recorded as a lead.

Offset convention: @n = 0-based pair index in the repaired 1,847-pair stream.

## Bar (verbatim, pre-registered)

"(a) adjudicate those values' classes under standing values; (b) a
class-level -2 separator promotes to red-team rule candidacy, else dissolve
as coincidence"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. **C1:** each of the ten -2 slot values is adjudicated to a class under
   standing values (protocol section 7 + standing battery promotes/leads;
   class-open values marked, not invented).
2. **C2:** a class-level separator between the arms' -2 slots is stated and
   promotes to red-team rule candidacy; absent that, the disjointness is
   dissolved as coincidence and the claim dies.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair stream
independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed exactly per
`code/side-keyhunt/repair_parse.py` (asserted 1,847 pairs / 96 types before
testing). `canonical.py` never used. R5005, sealed gates, red-team queue
untouched. Every number traces to the stream.

The 12 windows and their -2 slots were re-derived byte-exact and match the
parent's loci exactly:

| window | arm | -2 | context |
|---|---|---|---|
| @68 | A | 92 | `94 92 69 [13] 24 56` |
| @822 | A | 40 | `78 40 95 [13] 24 87` |
| @1381 | A | 92 | `84 92 69 [13] 24 65` |
| @1554 | A | 23 | `45 23 99 [13] 93 61` |
| @1684 | A | 79 | `46 79 65 [13] 93 62` |
| @139 | B | 91 | `23 91 65 [13] 66 14` |
| @456 | B | 60 | `77 60 65 [13] 66 14` |
| @481 | B | 93 | `45 93 00 [13] 52 30` |
| @567 | B | 80 | `24 80 97 [13] 76 45` |
| @575 | B | 78 | `87 78 45 [13] 55 61` |
| @1166 | B | 78 | `67 78 45 [13] 55 61` |
| @1360 | B | 64 | `37 64 35 [13] 92 62` |

## C1 — class adjudication under standing values

Arm A -2 slot ({23, 40, 79, 92}):
- **23** — class OPEN (23~26 split holds; no granted value).
- **40** — GT letter cell ("e", pencil). At @822 (`78 40 95`) the
  letter-tier reading is unforced: 40 is word-edge-capable but may stand
  alone; no standing license fixes it word-internal here.
- **79** — "tout" granted as a whole word (A5).
- **92** — class OPEN (09~92 hold; the 09/92 "-ere" value is killed).

Arm B -2 slot ({60, 64, 78, 80, 91, 93}):
- **60** — class OPEN.
- **64** — "qui" granted (whole word; relative/interrogative pronoun).
- **78** — "ver" LEAD (R16-005), not granted; stem-tier in ver-words.
- **80** — verb-frame A8 (class-level), value open.
- **91** — class OPEN (past-participle 91 is locus-scoped to the 16-91
  windows per R19-164; 91 verb-shaped at @277 per noun-91-nondet;
  globally open).
- **93** — verb class promoted (verb-93).

**No class-level partition exists.** Both arms contain granted whole
words (79="tout" in A vs 64="qui" in B); both contain class-open cells
(23, 92 in A vs 60, 91 in B). The only tier-unique items are single data
points — 40 (letter-tier, unforced at its locus) in A and 93 (verb
class) in B — and one data point cannot carry a class-level rule.
Standing values give the arms no disjoint class reading at the -2 slot.

## C2 — coincidence test

Exact permutation test (C(12,5) = 792 labelings; statistic = number of
shared -2 values between the 5-window and 7-window arms): the observed
disjointness (0 shared values) occurs in **22.2%** of random labelings.
p = 0.222 — the disjointness is not significant at any lane standard.
With n=12 and 96 types, disjoint -2 slots are a common coincidence.

Per the bar's else-arm: the claim dissolves as coincidence.

## Adverses answered

- **small n (12): ANSWERED.** The exact permutation test (p=0.222) is the
  small-n control; the disjointness fails it outright.
- **classes open: ANSWERED.** Six of ten values are class-open; the four
  class-known values (40, 79, 64, 93) plus the two class-level frames
  (80, 78-lead) form no partition. The class arm was given its best
  chance and found nothing.

## Verdict: KILL

The -2 slot does not carry a positional separator: no class-level
partition exists under standing values, and the value-disjointness that
motivated the lead is a 22%-likely coincidence (exact permutation test,
p=0.222). The claim dies at battery grade.

Scope: kills only the -2-slot separator claim. Untouched: the parent's
5/7 distributional split (observed fact), its red-team
second-polyvalence package (bar c), and the arm-A re-segmentation venue
(reseg-13-armA, queued). No standing/red-team verdict contradicted;
protocol section 7 intact (67 et/veut remains the sole true
polyvalence). Canonical-stream caveat stands (68 of 70 row offsets
unvalidated).

Per protocol section 4 (kill), no follow-ups are required. Natural next
questions (not queued): none — the parent's remaining leads
(reseg-13-armA, pronoun-13-les) already own the surviving venues.

## Bookkeeping

- `battery-queue.json`: `split-13-secondleft` queued -> verdict/kill
  (temp-file + rename, own entry only; pre-write assert confirmed no
  prior verdict; JSON re-validated from disk; no downgrade).
- Lock `locks/split-13-secondleft.lock`: created on start, deleted on
  completion.
- R5005, sealed gates, red-team adjudication queue untouched.
