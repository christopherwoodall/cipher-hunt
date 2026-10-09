# Battery `41-808-role` — verdict: PROMOTE

Worker: 4cf62875-34ff-4980-9840-5112955e2212 · 2026-10-09T16:59:38Z start
Target: `41-808-role` (P3) — null-regenerating follow-up #2 of
`battery-val-41-word-census` NULL. Decides 41's tier at @808:
standalone-word vs word-internal.

## Bar (verbatim, pre-registered before testing)

> "41 at @808 is STANDALONE-word iff (B1) the @804..812 frame is
> byte-exact 53 69 24 24 41 12 48 24 65 on row a5_05; (B2) 24@807 is
> finite/modal — stream-verified follower 41 (not 85) per the standing
> R24 logic, forcing a word boundary immediately before 41; (B3) 12's
> attachment at @809 is rightward, not leftward — the bigram '12 48'
> recurs in the stream independently of @808 while '41 12' has no
> independent recurrence beyond the letter-tier @1508 window
> (independent rightward recurrences outnumber independent leftward
> recurrences); (B4) the @1508 letter-tier '41 12' does not transfer to
> @808 — the two frames differ in the boundary-forcing left neighbor of
> 41 (24-finite at @808 vs 56 at @1508) and in 12's rightward
> collocation ('12 48' 5x vs '12 61' hapax at @1509). Promote requires
> B1∧B2∧B3∧B4 with >=2 independent legs; any clause failing at kill
> grade kills the standalone claim; ambiguity on B3/B4 is null."

Restated as numbered pass/fail clauses (fixed before the census run):
- B1: @804..812 reads exactly `53 69 24 24 41 12 48 24 65`, row a5_05,
  41 at @808. PASS/FAIL on exact bytes.
- B2: 24@807's follower is 41 (≠ 85); per standing R24, 24 parses as
  finite/modal here and forces a word boundary before 41. PASS/FAIL.
- B3: 12 attaches rightward at @809: count independent (non-@808)
  '12 48' bigrams vs independent (non-@808) '41 12' bigrams;
  PASS iff rightward independents > leftward independents.
- B4: @1508 frame (`86 56 41 12 61 59`, a7_11) differs from @808 in the
  left-boundary evidence for 41 and in 12's rightward collocation
  ('12 61' count vs '12 48' count); PASS iff the letter-tier reading
  at @1508 is frame-local and does not transfer.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like
`code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
96 types; 0-based @-offsets). `canonical.py` never used. R5005,
sealed gates, red-team adjudication queue untouched. No invented
numbers: every count below is from the stream.

Adopted premises (not re-litigated): §7 standings; `val-41-word-census`
NULL (its @808/@1016 "'en [41]'" premise rejected: both windows read
"[24-fin] [41]"); 24 finite/modal per R24; @1508 '41 12' letter-tier
per the parent census; 41's split candidacy is red-team venue
(`split-41-redteam`), untouched here.

Lock: `locks/41-808-role.lock` created at start (agent id + UTC
timestamp); no stale lock present. Deleted on completion per §6.

## Window-level evidence (byte-exact, 0-based)

Stream totals: n(41)=19, n(12)=23, n(24)=52, n(48)=38.

**@808 window (row a5_05):**
`@802..814 = 62 98 53 69 24 24 41 12 48 24 65 14 29`
— @806=24, @807=24, @808=41, @809=12, @810=48. (B1 frame confirmed.)

**24-follower census (B2):** 24@807 is followed by 41, not 85.
Stream-wide 24-followers: 87×10, 85×5, 82×4, 30×3, 89×3, 37×2,
80×2, 26×2, 41×2, 65×2, 49×2, 48×2, plus 13 singletons.
The two '24 41' bigrams are @807 (@808 window) and @1015 (@1016
window: `79 80 78 47 03 24 41 15 66 91 53`, a6_02) — both windows the
parent census forces as standalone-word 41.

**12-attachment census (B3):** all 23 occurrences of 12 with neighbors:
- '12 48' bigram: 5× — @169 (a1_05: `53 12 48`), @709 (a5_01:
  `53 12 48`), @809 (a5_05, test window), @1075 (a6_05: `98 12 48`),
  @1736 (a8_07: `60 12 48`). Independent of @808: 4×, with left
  neighbors 53, 53, 98, 60 (never 41).
- '41 12' bigram: 2× — @808 (test window) and @1508 (a7_11:
  `56 41 12 61`, letter-tier per parent census). Independent of @808:
  1×.
- '12 41' bigram: 2× — @58 (a1_01: `53 12 41`), @1471 (a7_10:
  `26 12 41`); both letter-tier per parent census.
- Other 12 neighbors are letter-tier-adjacent: @64 `40 12 94`
  (40='e', banked letter), @1740 `86 12 34` (34='i', banked letter),
  @348/@1548 `70 12 94` (70='pre', bound prefix). 12 never anchors a
  forced word-tier window in 23 occurrences — consistent with the
  'n'-pending letter-tier hypothesis, and compatible with 12 opening
  the next word at @809 ("n…" + 48…).

**@1508 non-transfer (B4):** @1502..1514 (a7_11) =
`33 42 33 00 86 56 41 12 61 59 39 81 88`.
41's left neighbor is 56 (no forced word boundary — cf. @808 where it
is finite 24). 12's rightward option at @1509 is '12 61', a hapax
(61's 18 occurrences never otherwise neighbor 12), while '12 48' is
5×. So at @1508 the leftward letter-tier parse wins on both legs, and
at @808 the rightward parse wins on both legs — the frames genuinely
discriminate; the letter-tier reading does not transfer.

**Supporting leg — 41's standalone capability:** the parent census
forces standalone-word 41 at 7 other windows (@5, @39, @91, @237,
@964, @1016, @1048) with followers 06, 01, 98, 17, 19, 15, 88. A
standalone 41 followed by another token is the stream-normal parse;
nothing about @808 requires demoting 41 to letter-tier.

## Per-clause results

- **B1: PASS.** @804..812 = `53 69 24 24 41 12 48 24 65`, row a5_05,
  41 at @808 — byte-exact.
- **B2: PASS.** 24@807's follower is 41, not 85; standing R24 parses
  24 as finite/modal here, forcing a word boundary before 41. (The
  5× '24 85' bigrams are fenced under Adverses; they do not touch
  this window's follower test.)
- **B3: PASS.** Independent '12 48': 4× (@169, @709, @1075, @1736);
  independent '41 12': 1× (@1508). 4 > 1 — 12 attaches rightward at
  @809, leaving 41 as its own word.
- **B4: PASS.** @1508 differs in the discriminating features (left
  neighbor 56, no forced boundary; rightward '12 61' hapax vs '12 48'
  5×). The letter-tier reading is frame-local to @1508.

## Adverses

- A1 ('24 85' 5×: @732, @955, @1438, @1693, @1754): fenced with
  cause. A finite/modal 24 followed by verb-stem 85 parses as
  modal + infinitive (the same positional pattern §7 grants 67);
  these windows do not alter the follower test at @807 (41 ≠ 85).
  24's class outside @807 is out of scope.
- A2 ('24 24' doubling at @806/@807): noted, stream-real, byte-exact.
  B2 tests 24@807 only; 24@806's class is out of scope and does not
  affect the boundary before 41.
- A3 (12 'n'-pending, 48 tier open): fenced. The bar tests 12's
  attachment direction, not its value; 48's tier does not discriminate
  parses (a) vs (b) and is left open.
- A4 (41 letter-tier at @59/@1472/@1508 per parent census): answered
  by B4 — frame asymmetry (no forced left boundary there) keeps those
  windows from transferring; 41's split/tier adjudication remains
  red-team venue, untouched.
- A5 (§7 polyvalence): untouched. No new polyvalence claimed — the
  verdict is that 41 is word-tier at @808, consistent with its 7 other
  forced-standalone windows.

No standing or red-team verdict contradicted, downgraded, or
overwritten.

## Verdict: PROMOTE

41 is standalone-word at @808. Three independent legs converge:
(1) finite-verb 24@807 forces a word boundary before 41 (B2);
(2) 12 attaches rightward — '12 48' recurs 4× independently vs 1× for
'41 12' (B3); (3) the rival letter-tier frame @1508 is
distinguishable on both discriminating features and does not transfer
(B4). The word-internal rival is fenced with stated cause. No
follow-ups required (promote).

## Scope

Decides 41's tier at @808 only. Untouched: all §7 standings,
`val-41-word-census` NULL, `val-41-det-windows` PROMOTE,
`val-41-1016` NULL, `41-doubling-audit` PROMOTE,
`41-1016-det-incompatibility` PROMOTE, `split-41-redteam` (queued),
`41-verb-arm-package` (queued), `41-05-class` (in flight),
the val-24 targets, R5005, sealed gates, red-team adjudication queue.
