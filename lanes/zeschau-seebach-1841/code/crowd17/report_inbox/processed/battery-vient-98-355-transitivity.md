# Battery report: vient-98-355-transitivity — nominal-subject census of 98-as-'vient'

- Target id: vient-98-355-transitivity
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  asserts 1,847 pairs / 96 types held in-worker). `canonical.py` not used.
  R5005 not touched.
- Follow-up of seg-92-354-356 (NULL fence, 2026-10-09).

## Bar (verbatim, pre-registered from battery-queue.json before testing)

"census 98's nominal-subject windows elsewhere (n(98)=40; predecessors 62x5, 42x3, 66x3); if 'vient' never takes nominal subjects, @355 is kill-grade adverse material against vient-98-name — escalate to the red team"

Numbered pass/fail clauses:

1. **(C1)** Complete census of all 40 windows of 98: predecessor distribution
   stated, and each window's subject under the battery-grade 98='vient' reading
   classified (nominal / pronoun / relative / open / implicit / fenced / n-a)
   with stated grounds. PASS = census complete with stated grounds.
2. **(C2)** Conditional: IF 'vient' takes no nominal subjects elsewhere, THEN
   @355 is kill-grade adverse material against vient-98-name and the worker
   escalates to the red team (no battery verdict against vient-98-name is
   declared). PASS = condition evaluated and the correct branch taken.

## Method

1. Rebuilt the repaired stream in-worker per `repair_parse.py`; asserted
   1,847 pairs / 96 types. Index list of 98 byte-exact: 12, 19, 80, 89, 92,
   124, 192, 227, 236, 355, 440, 511, 702, 767, 803, 838, 894, 897, 930, 946,
   971, 1060, 1073, 1074, 1137, 1139, 1145, 1146, 1284, 1317, 1325, 1373,
   1481, 1579, 1601, 1643, 1660, 1661, 1725, 1783 (n=40, matches
   vient-98-name's list exactly).
2. Verified the sandwich claim: the 3-gram '92 98 92' occurs exactly once
   stream-wide (@354, row a2_06). 98's sole 92-predecessor and sole 92-follower
   are both @355. The claim's uniqueness premise is byte-exact.
3. For each window, adopted the window-level parses from vient-98-name
   (PROMOTE, battery-grade, 2026-10-09) and seg-92-354-356 (NULL, 2026-10-09) —
   not re-litigated — and classified 98's subject under the 98='vient'
   hypothesis. "Nominal subject" = subject cell carrying a standing noun
   class/value (42 noun-class R19-055; 43 noun-class R19-045; 76 masc noun;
   17='fois' promoted). Pronouns (47/87='ce'), relatives (64='qui', 46='que'),
   and open cells do not count.
4. 98's value was NOT re-named and no clause of vient-98-name's bar was
   re-tested (per adverses: coordinate, do not duplicate).

## Window-level evidence (@-offsets; subject = subject of 98-as-'vient')

Predecessor census (byte-exact): 62x5, 42x3, 66x3, 98x3, 64x2, 43x2, 01x2,
82x2, 47x2, and 41/87/46/70/92/12/17/14/09/00/32/48/67/16/33/23 x1 each —
matches the bar's stated distribution (62x5, 42x3, 66x3).

| @ | context (pre [98] fol) | subject of vient | class |
|---|---|---|---|
| 12 | 62 [98] 76 | 62 (open; 'il' demonstrated-not-promoted) | open |
| 19 | 64 [98] 82 | 64='qui' | relative |
| 80 | 42 [98] 51 | 42 (noun cls, R19-055) | **NOMINAL** |
| 89 | 66 [98] 19 | 66 | open |
| 92 | 41 [98] 81 | 41 | open |
| 124 | 66 [98] 82 | 66 | open |
| 192 | 87 [98] 56 | 87='ce' | pronoun |
| 227 | 46 [98] 83 | 46='que' | relative |
| 236 | 70 [98] 41 | word-internal ('pre'+98 = 'previent', compositional) | n/a |
| 355 | 92 [98] 92 | sandwich (under study) | excluded from elsewhere census |
| 440 | 43 [98] 80 | 43 (noun cls, R19-045) | **NOMINAL** |
| 511 | 64 [98] 65 | 64='qui' | relative |
| 702 | 12 [98] 20 | fenced ('n'vient', clause 3) | fenced |
| 767 | 66 [98] 80 | 66 | open |
| 803 | 62 [98] 53 | 62 | open |
| 838 | 17 [98] 20 | 17='fois' — subject attribution underdetermined ('fois vient [20]' vs '[56] fois, vient [20]') | underdetermined |
| 894 | 01 [98] 82 | 01 | open |
| 897 | 14 [98] 83 | 14 | open |
| 930 | 82 [98] 83 | 'me' proclitic; subject implicit | implicit |
| 946 | 62 [98] 96 | 62 | open |
| 971 | 01 [98] 48 | 01 | open |
| 1060 | 09 [98] 83 | 09 | open |
| 1073 | 42 [98] 98 | fenced (doubled-98, clause 2) | fenced |
| 1074 | 98 [98] 12 | n/a (second of doublet, non-subject position) | n/a |
| 1137 | 62 [98] 00 | 62 | open |
| 1139 | 00 [98] 78 | 'pour [98]' — infinitive 'venir' (clause 4) | non-finite |
| 1145 | 42 [98] 98 | fenced (doubled-98, clause 2) | fenced |
| 1146 | 98 [98] 86 | n/a (second of doublet) | n/a |
| 1284 | 32 [98] 55 | 32 (A1 predicative — not a nominal subject) | not-nominal |
| 1317 | 48 [98] 15 | fenced (48-residual) | fenced |
| 1325 | 62 [98] 56 | 62 | open |
| 1373 | 67 [98] 00 | 'et vient' — subject implicit (coordinated) | implicit |
| 1481 | 16 [98] 62 | 16 | open |
| 1579 | 47 [98] 24 | 47='ce' | pronoun |
| 1601 | 82 [98] 00 | '[81] me vient' — subject 81 (open; noun-81 queued) | open |
| 1643 | 33 [98] 60 | 33 (infinitive-subject, underdetermined) | open |
| 1660 | 47 [98] 98 | fenced (doubled-98, clause 2) | fenced |
| 1661 | 98 [98] 80 | n/a (second of doublet) | n/a |
| 1725 | 43 [98] 39 | 43 (noun cls, R19-045) | **NOMINAL** |
| 1783 | 23 [98] 83 | 23 | open |

The three nominal-subject windows, byte-exact:

- **@80** (row a1_02): `11 29 42 [98] 51 62 16` = '[42] vient [51]'. 42 carries
  the noun class (R19-055, class-level grant). Clean subject-verb frame;
  vient-98-name left it neutral ("[42] vient ... no force either way") — no
  fence, no contradiction. The subject is nominal at class level.
- **@440** (row a2_09): `45 46 43 [98] 80 50 78` = '[43] vient [80]'. 43 carries
  the noun class (R19-045, class-level grant). Adopted conditional pass from
  vient-98-name ('vient [80]' needs infinitive; 80 verb-frame A8). Subject
  nominal at class level.
- **@1725** (row a8_07): `52 37 43 [98] 39 88 24` = '[43] vient a [88]'
  ('venir a' + INF frame). 43 noun class (R19-045); vient-98-name's "43
  noun-like" condition is met at class level. Clean nominal-subject window.

Fences adopted without re-litigation: doubled-98 x3 (@1073/@1145/@1660,
clause 2), @702 'n'vient' (clause 3), @1139 infinitive (clause 4), 48-residuals
(@124/@971/@1317). @838 kept underdetermined (not counted). @236 is
word-internal, not a subject-verb window.

## Per-clause pass/fail

- **C1: PASS.** All 40 windows censused with stated grounds; predecessor
  distribution matches the bar's stated (62x5, 42x3, 66x3); sandwich uniqueness
  verified ('92 98 92' x1 stream-wide). Three nominal-subject windows found:
  @80, @440, @1725 (subjects 42, 43, 43 — all noun-class standing).
- **C2: PASS.** The antecedent ('vient' never takes nominal subjects) is FALSE:
  three windows take nominal subjects at class-level standing. Therefore @355
  is NOT kill-grade adverse material against vient-98-name on this ground and
  NO red-team escalation is triggered by this census. (The parent
  seg-92-354-356 fence on the sandwich's segmentation stands on its own
  grounds; this battery only discharged the transitivity bar.)

## Verdict

**PROMOTE** — the census is complete and the bar's adverse-material condition
does not obtain: 'vient' takes nominal subjects at three windows
(@80, @440, @1725) under standing class grants, so @355's sandwich is not
kill-grade adverse material against vient-98-name on the nominal-subject
ground.

## Adverses answered

- 98='vient' battery-grade, not red-team-ratified: no ratification claimed,
  requested, or assumed. The census runs strictly under the battery-grade
  hypothesis as the bar requires; nothing here upgrades vient-98-name.
- Coordinate with vient-98-name, do not duplicate its bar: every window parse
  adopted from vient-98-name (PROMOTE, 7 clauses) and seg-92-354-356 (NULL)
  without re-testing; 98's value not re-named; no overlap with vient-98-name's
  seven clauses.

## Scope

Census-level only. @355 itself is not parsed here (the parent fence stands).
92's value/class is untouched. 62's, 66's, 41's, 01's, 33's values stay open.
No standing or red-team verdict contradicted or downgraded; section 7 intact;
canonical-stream caveat stands. No follow-ups required per section 4
(promote). Re-open condition: a red-team value for 62, 66, 41, or 01 that
converts an open-subject window to nominal, or a value for 92.
