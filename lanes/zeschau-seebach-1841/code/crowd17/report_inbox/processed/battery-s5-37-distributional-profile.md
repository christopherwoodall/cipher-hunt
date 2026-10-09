# Battery report — s5-37-distributional-profile

- Target: `s5-37-distributional-profile` (priority 3)
- Worker: a321c883-f33a-480c-98e6-e43cc20a18dd
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  verified: 1,847 pairs, 96 groups, n(37)=28). `canonical.py` never used.
  R5005 untouched.
- Lock: `code/crowd17/next-token/locks/s5-37-distributional-profile.lock`
  created on start, deleted on completion. No stale lock existed.

## Bar (verbatim, pre-registered)

> pass = complete, stream-traced neighbor table for all 28 occurrences plus
> a representativeness judgment for the five S5 windows; no value declared
> at battery level.

## Bar restated as numbered pass/fail clauses (fixed before testing, unmodified after)

- **C1.** A complete, stream-traced neighbor table covering all 28
  occurrences of 37 is published.
- **C2.** A representativeness judgment for the five S5 windows
  (@51/@1655 37-11; @529/@1357/@1444 37-64 in s5-rival-five-windows offsets)
  is stated.
- **C3.** No value for 37 is declared at battery level.

## Offset convention

Lane reports mix 0-based and 1-based "@". The s5-rival-five-windows report
used 0-based stream indices for its "@" offsets and position list. This
report gives **1-based** offsets as primary (lane convention per
w1-573-subject) with the prior report's 0-based index in parentheses for
byte-traceability. Byte-identity verified: prior "@51" (a1_01, "92 79 [37]
11 79 85") = my @52 (0-based index 51); all 28 occurrences byte-match the
prior positions list +1.

## Method

Re-derived the repaired stream in-session from
`data/upstream-ct_R5005.txt` + `repaired_offsets.json` per
`repair_parse.py`. Enumerated every occurrence of group "37" with row id,
predecessor, successor, and ±3 context. Built predecessor/successor censuses
independently. Checked the 37-01 closed set and the five S5 windows against
the byte stream.

## C1 — full 37 neighbor table (all 28, 1-based @; 0-based in parens)

| @ (1b) | 0b | row | −3 −2 −1 **[37]** +1 +2 +3 |
|--------|----|-----|---------------------------|
| 52 | (51) | a1_01 | 00 92 79 **[37]** 11 79 85 |
| 184 | (183) | a1_05 | 87 64 23 **[37]** 06 00 33 |
| 279 | (278) | a2_03 | 89 84 91 **[37]** 61 20 61 |
| 313 | (312) | a2_04 | 46 84 24 **[37]** 78 45 64 |
| 386 | (385) | a2_07 | 16 52 38 **[37]** 43 91 36 |
| 415 | (414) | a2_08 | 53 84 51 **[37]** 78 49 74 |
| 476 | (475) | a2_10 | 46 84 24 **[37]** 78 74 45 |
| 530 | (529) | a3_00 | 47 44 59 **[37]** 64 26 32 |
| 621 | (620) | a4_01 | 10 29 88 **[37]** 76 82 14 |
| 626 | (625) | a4_01 | 82 14 59 **[37]** 33 29 87 |
| 677 | (676) | a5_00 | 80 03 64 **[37]** 77 45 23 |
| 779 | (778) | a5_04 | 15 33 73 **[37]** 08 29 89 |
| 797 | (796) | a5_04 | 07 64 56 **[37]** 44 77 86 |
| 886 | (885) | a5_08 | 31 79 68 **[37]** 03 02 00 |
| 914 | (913) | a5_09 | 64 83 59 **[37]** 96 09 02 |
| 940 | (939) | a5_10 | 33 21 64 **[37]** 01 07 50 |
| 1126 | (1125) | a6_07 | 06 11 52 **[37]** 43 00 86 |
| 1131 | (1130) | a6_07 | 00 86 52 **[37]** 86 24 77 |
| 1180 | (1179) | a6_10 | 32 48 59 **[37]** 77 78 94 |
| 1302 | (1301) | a7_03 | 16 02 70 **[37]** 08 43 21 |
| 1358 | (1357) | a7_05 | 82 06 52 **[37]** 64 35 13 |
| 1445 | (1444) | a7_09 | 52 68 59 **[37]** 64 77 84 |
| 1634 | (1633) | a8_03 | 33 21 64 **[37]** 01 74 87 |
| 1656 | (1655) | a8_04 | 16 01 56 **[37]** 11 24 48 |
| 1724 | (1723) | a8_07 | 06 11 52 **[37]** 43 98 39 |
| 1771 | (1770) | a8_08 | 87 64 26 **[37]** 78 62 94 |
| 1798 | (1797) | a8_10 | 42 94 59 **[37]** 91 79 87 |
| 1818 | (1817) | a8_10 | 42 06 29 **[37]** 01 02 09 |

Predecessor census: 59×6, 52×4, 64×3, 24×2, 56×2, 79/23/91/38/51/88/73/68/70/26/29 ×1 each (11 singles). Sums to 28 exactly.

Successor census: 78×4, 43×3, 64×3, 01×3, 11×2, 77×2, 08×2, 06/61/76/33/44/03/96/86/91 ×1 each (9 singles). Sums to 28 exactly.

Both censuses byte-match the F3 summary in battery-s5-rival-five-windows
(except that report's "+13 singles" predecessor shorthand; byte-derived
count is 11 singles, summing to exactly 28).

**37-01 bigram closed set:** exactly three — @940 (a5_10), @1634 (a8_03),
@1818 (a8_10). @940 and @1634 share the byte-identical 3-pair left context
"33 21 64". No other 37→01 contact exists in the stream.

## C2 — representativeness judgment for the five S5 windows

The five S5 windows (1-based: @52/@1656 with 37-11, @530/@1358/@1445 with
37-64) are 5/28 = 17.9% of 37's distribution.

1. **Frequency rank: middle band, not tail, not dominant.** 64 and 43 and 01
   are tied-second followers (×3); 11 and 77 and 08 are tied-third (×2).
   The dominant follower 78 (×4) is unrepresented in the S5 set.
2. **Predecessors drawn from dominant classes.** The five predecessors are
   79, 59, 52, 59, 56 — 59 is the top predecessor (6/28), 52 the second
   (4/28). The S5 windows are not left-side outliers.
3. **Epistemically privileged, not behaviorally typical.** The S5 set is the
   only 37 subset closed under a bigram criterion whose right neighbors
   carry granted/banked values (11=la banked, 64=qui granted). That is why
   rival-value batteries targeted it — testability, not typicality. Note
   @914 (37-96, 96='par' granted) is a granted-follower window NOT in the
   S5 set, so the set is bigram-criterion-defined, not value-criterion-defined.
4. **Bulk unrepresented.** 23/28 windows (78×4, 43×3, 01×3, 77×2, 08×2,
   9 singles) have open-valued neighbors; no S5 window samples them.

Judgment: the S5 windows are a legitimately chosen, epistemically
privileged test set — drawn from dominant predecessor classes and
mid-ranked follower classes, hence not distribution outliers. But they are
not representative of the bulk either, because the bulk's dominant
followers (78×4, 43×3, 01×3) carry open values. Any rival value promoted
on the five S5 windows must still clear the other 23 — which the
s5-rival-five-windows family screen (F2) already showed no lexical family
does jointly. The five-window bar is a necessary but far-from-sufficient
filter.

## Adverses (all answered/coordinated)

- **1690 frequency uniformity necessary-not-sufficient (§7):** acknowledged.
  n(37)=28 is moderate; this battery runs no uniformity test and declares
  no value.
- **Distributional evidence never promotes alone:** honored. Verdict is a
  profile publication (promote = table delivered per the bar's own
  definition), not a value promote. No lead re-graded.
- **37-01 bigrams vs the A12 unit grant:** coordinated. The three 37-01
  windows are consistent with the A12 grant ("37-01 as a unit, not a value";
  01 valueless inside the unit — see battery-ci-bound-01's 24-window sweep,
  which found 01 valueless in all non-ce windows including these three).
  No window forces a token value on 01 inside the unit. The queued
  `wordinternal-37-01` battery tests "-faisant" vs "-ci"/"-tain" endings —
  not decided here, no duplication, no contradiction.

## Per-clause pass/fail

- **C1 (complete neighbor table, all 28): PASS** — table above, all counts
  stream-traced, predecessor/successor censuses sum to 28 exactly.
- **C2 (representativeness judgment for the five S5 windows): PASS** —
  stated above: epistemically privileged test set, not distribution
  outliers, not representative of the bulk.
- **C3 (no value declared at battery level): PASS** — no value named; §7
  intact (37's sub-lexical value remains S5-owned).

## Verdict: PROMOTE (profile grade)

The full 28-occurrence neighbor profile of 37 is published to bound the
rival-value search space, per the bar. No value declared; no standing
verdict contradicted or downgraded; §7 intact.
