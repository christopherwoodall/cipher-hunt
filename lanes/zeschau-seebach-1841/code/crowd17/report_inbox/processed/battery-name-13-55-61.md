# Battery report: name-13-55-61

Target: `name-13-55-61`. Claim: 13-55-61 names as one French word via
cross-window triangulation.
Date: 2026-10-08. Worker: 10b0a896-f4cd-466e-92ed-e2a889164526 (battery worker).
Lock `locks/name-13-55-61.lock` created 2026-10-09T01:52:28Z (no stale lock for
this id; no pre-existing lockfile); deleted on completion.

Parent null: `dict-frame-78-45-13-55-61` (2026-10-08, processed). This battery
does not re-litigate that null — it builds on its two clean windows and tests
only the narrowed naming bar below (§7 honored throughout).

## Bar (verbatim, pre-registered)

"(a) 13/55/61 contact profiles stated (13->24 x3, 55->81 x6, 61 scattered n=18);
(b) name X iff one French word fits both 5-gram windows + the third 55-61
window @1205; (c) W1's 'ne mentent' 3pl subject identified under the named X"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. The 13/55/61 contact profiles are stated and match the bar's figures
   (13->24 x3, 55->81 x6, 61 scattered n=18).
2. Exactly one French word X is named such that X fits the 13-55-61 trigram in
   both 5-gram windows AND the 55-61 bigram in the third window.
3. W1's "ne mentent" 3pl subject is identified under the named X.

Offset convention: @n below = 0-based pair index in the repaired 1,847-pair
stream. The bar's "@1205" for the third window is a 0-based stream index
(verified against the prior report's window dump). The two 5-grams start at
stream @575 and @1166 (0-based).

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(stride-2 pairing per row offset). Asserted 1,847 pairs / 96 types before
testing. `canonical.py` never used. R5005 untouched (read-only parse). No
sealed gates, no red-team contact. Every number below was re-derived in-session;
no number is carried over from the parent report.

Standing values used (protocol §7): banked GT 11=la, 82=m, 40=e, 46=que;
granted 87=ce, 47="ce" (allophone tier); 06="ent" granted-conditional (R17-007,
on 94="ne" STRONG LEAD); leads 78="ver" (R16-005, confirmed R17-006/R17-021),
94="ne" STRONG LEAD (R17-001), 45="ce/dict" (A11 HOLD + R16-004 lead). 67
et/veut sole true polyvalence with the positional rule.

## Window-level evidence (re-derived)

W1 — trigram @575-577 (row a3_02):
`@572:87 @573:78 @574:45 | 13 55 61 | @578:94 @579:82 @580:06 @581:06 @582:50`
= "ce(87) verdict(78-45, LEAD) [13-55-61] ne(94, STRONG LEAD) mentent(82-06-06,
conditional)".

W2 — trigram @1166-1168 (row a6_09):
`@1162:21 @1163:67 @1164:78 @1165:45 | 13 55 61 | @1169:94 @1170:87 @1171:83
@1172:21` = "… 21 et(67, positional rule) verdict [13-55-61] ne(94) ce(87) …".
94-87 is a stream-unique bigram; "ne ce" is ungrammatical under the standing
values.

W3 — 55-61 bigram @1205-1206 (row a6_11):
`@1200:29 @1201:45 @1202:58 @1203:47 @1204:43 | 55 61 | @1207:21 @1208:65
@1209:64` = "… 29 45 58 ce(47, granted) 43 [55-61] 21 65 …". Predecessor of 55
here is 43, not 13.

Contact profiles (re-derived, full):
- 13, n=12: suc {24x3, 66x2, 55x2, 93x2, 52x1, 76x1, 92x1}; pred {65x3, 69x2,
  45x2, 00x1, 97x1, 95x1, 35x1, 99x1}. 13->55 bigram occurs ONLY at @575/@1166
  (the two target windows) — verified by full-stream bigram scan.
- 55, n=12: suc {81x6, 61x3, 83x2, 68x1}; pred {13x2, 33, 06, 46, 18, 02, 07,
  43, 98, 08, 78} — 11 distinct predecessors.
- 61, n=18: suc {96x2, 59x2, 94x2, 21x2, 20, 42, 70, 88, 24, 31, 56, 12, 40,
  15} — 14 distinct successors, none above x2; pred {55x3, 62x2, 89, 37, 20,
  49, 87, 17, 92, 01, 53, 91, 12, 93, 04}.
- 13-55-61 trigram: exactly x2 (@575, @1166), zero elsewhere. 55-61 bigram:
  exactly x3 (@576, @1167, @1205).

## Triangulation attempt

Two readings of "one French word X" were tested against all three windows.

H1 — X = one word over 13-55-61 (3 pairs), with 43≡13 in W3 (43-55-61 as the
same word with a variant first syllable). REJECTED: 13 and 43 have divergent
profiles (13 suc: 24x3/66x2/55x2/93x2/52/76/92; 43 suc: 00x3/77x2/87x2/98x2/29/
81/91/24/07/55/21; overlap only 24 and 55). No allophone evidence links them,
and §7 grants no 13/43 value. A fixed 3-pair word is falsified as a stable
unit by W3's 43 onset — but at null grade only, since the whole frame is
conditional on unsettled leads (78="ver", 45="dict").

H2 — X = one word over 55-61 (2 pairs); 13 and 43 are separate preceding units
(determiner/adjective slot). Then W1 reads "ce verdict 13 X ne mentent": 13+X
could be a 3pl subject if 13 is a plural determiner and X a plural noun
("ce verdict, les X ne mentent"). REJECTED as unnameable: 13's value is open
(no battery has named it; 13 occurs 10x without 55, so it is not bound to X),
X's value (55-61) is open, and a 2-syllable French plural noun fitting "les X
ne mentent" + "et verdict les X ne ce" + "ce 43 X 21 65" is radically
underdetermined — témoins, hommes, serments, and dozens more fit the frames
equally. No candidate is forced by the data; triangulation does not converge.

Consequence: no single word can be named with evidential support. The
underdetermination is structural (open values for 13, 55, 61, 43, 21), not a
lack of effort.

## Per-clause pass/fail

1. **PASS.** Profiles stated and verified: 13->24 x3 (of 13's 12 successors),
   55->81 x6 (of 55's 12 successors), 61 n=18 with max successor count x2
   (scattered). All figures match the bar exactly.
2. **FAIL (null grade).** No French word X can be named: H1 is falsified as a
   stable 3-pair unit by W3's 43 onset (43≠13, no allophone evidence); H2
   leaves X underdetermined over an open candidate space. Not kill-grade: the
   claim is conditional on unsettled leads (78="ver" LEAD, 45="dict" lead,
   94="ne" STRONG LEAD) — per the fork-78-45-rerun precedent an unfired
   conditional is null, not kill. No cleaner rival value was demonstrated on
   the frames.
3. **FAIL (null grade).** X unnamed, so W1's "ne mentent" 3pl subject remains
   unidentified. (Separately queued as `w1-573-subject`; this battery does not
   duplicate it.)

## Adverses answered

- "W2 'ne ce' hapax": fenced with stated cause — 94-87 is a stream-unique
  bigram and ungrammatical under 94="ne" STRONG LEAD (R17-001) + 87="ce"
  (granted); the anomaly is a 94-frame problem outside this claim's scope, and
  `ne-ce-1169` already returned null on it (verdict recorded 2026-10-08). Not
  re-litigated.
- "scattered profiles": confirmed and stated as the mechanism of the null —
  61 has 14 distinct successors (max x2), 55 has 11 distinct predecessors, 13
  has 8 distinct predecessors. The scatter is what blocks naming; it is
  evidence, not an ignored adverse.

No standing red-team verdict is contradicted (R17-001/R17-006/R17-007,
R16-005, A11 scoping, §7 banked/granted/killed values all respected) — no
escalation.

## Verdict: null

Headline: clause 1 passes (profiles verified); clauses 2–3 unsatisfiable — no
French word X is nameable over 13-55-61/55-61 with evidential support, and
W1's "ne mentent" stays subjectless. The third window's 43 onset breaks the
fixed 3-pair unit reading; the 2-pair reading is underdetermined.

## Follow-up targets (null regenerates work; all ids verified absent from the queue 2026-10-08)

1. **name-55-61-core** (priority 2). Claim: X names as one French word over
   the 55-61 bigram alone, with 13/43 as a detachable preceding slot.
   Bars: (a) 55-61 bigram census stated x3 (predecessors 13,13,43;
   successors 94,94,21); (b) name X iff one French word fits all three 55-61
   windows with stated, consistent 13/43 slot values; (c) coordinate with
   w1-573-subject (merge if X is the subject); do not re-litigate
   ne-ce-1169's null. Evidence: this report. Adverses: 55's 11 distinct
   predecessors (weak unit); W2 "ne ce" hapax; 61 profile scattered.
2. **slot-13-43-compare** (priority 3). Claim: 13 and 43 occupy the same
   pre-55-61 slot (distributional test). Bars: (a) state 13's (n=12) and 43's
   (n=16) full contact profiles; (b) same-slot iff successor-set overlap
   exceeds chance under a stated test; (c) if same slot, propose the slot's
   grammatical class with stated noun-shape criteria. Never declare 13=43 a
   value without red-team declaration (§7). Evidence: this report (13 suc
   {24x3,66x2,55x2,93x2,52,76,92}; 43 suc
   {00x3,77x2,87x2,98x2,29,81,91,24,07,55,21}). Adverses: both values open;
   small samples (n=12/n=16).
3. **frame-1205-parse** (priority 3). Claim: the third window parses
   standalone. Bars: (a) state 43/21/65 contact profiles on the repaired
   stream; (b) parse "29 45 58 ce(47) 43 55 61 21 65" (@1199-1209, 0-based)
   with word boundaries stated under granted values only (47="ce"); (c) fence
   the 29/45/58 left context with stated cause. Evidence: this report.
   Adverses: 21, 43, 65 values open.

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs /
96 types asserted before testing). Analysis scripts were session-local
(/tmp/name135561.py, /tmp/name135561b.py); the window dumps and censuses above
are the record. No writes outside this report, the queue edit, and the
lockfile (deleted).
