# Battery report: seg-94-82-06-f2 (NULL — slot-equivalence undecidable at n=7; word edge undecided)

**Target:** seg-94-82-06-f2 — 18 slot-equivalence at pair 736; discriminates word-edge-after-X
**Worker:** 3d51fbaa-5c54-419e-9de5-f3e47155bc39 | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; 1,847 pairs / 96 types re-verified). Never canonical.py. No R5005 touched. No sealed gates touched. No data invented. Every @-offset re-derived from the stream. Lock: locks/seg-94-82-06-f2.lock created 2026-10-09T03:16:32Z, deleted on completion.

## Bar (verbatim from battery-queue.json)

> test whether 18 occupies the same slot as 94 at pair 736's 18-82-06 variant; decide the word-edge placement

## Bar as numbered clauses (pre-registered before testing)

1. The repaired stream contains the 18-82-06 variant at pair 736 and the 94-82 reference frames at their stated positions.
2. 18's distribution matches 94's left-of-82 slot (slot-equivalence demonstrated with <=1 ungranted assumption), or a distributional test rejects equivalence at the lane's standard.
3. The word-edge placement at 736 is decided under standing values with <=1 ungranted assumption.
4. Adverses answered: 18's value stays unknown (frame B remains fenced on 18 — no value named here); 00="pour" (A9, granted) is honored in every candidate parse.

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (asserts hold: 1,847 pairs, 96 distinct groups).
2. Full census of 18 (n=7) and 94 (n=37): positions, followers, left-neighbors.
3. Slot comparison: 18->82 vs 94->82 rates (Fisher exact, two-sided), left-of-82 context profiles, shared-follower windows compared pair-by-pair.
4. Word-edge candidates at 736 tested under standing values only: [18]|[82-06], [18-82]|[06], [18]|[82]|[06], [18-82-06] one word. Standing gloss key: 82="m" (banked), 06="ent" iff pre=82 (F61 islet — pre-06 here IS 82, so covered), 00="pour" (A9 granted), 76=noun-class (battery-promoted masculine noun), 79="tout" (promoted), 70="pre" (banked).

## Window-level evidence (0-based pair indices)

**18 census (n=7):** @9 [a1_00], @302 [a2_04], @585 [a3_02], @736 [a5_02], @905 [a5_09], @1009 [a6_02], @1066 [a6_04].
- Followers: 93, 89, 14, 82, 55, 79, 70 — all x1, no repeats.
- Left-neighbors: 78, 91, 19, 76, 88, 35, 62 — all x1, no repeats.
- 18 has NO distributional profile: every follower and every left-neighbor is a singleton.

**94 census (n=37):** 94->82 at @578, @1182, @1353 (->06) and @1742 (->46). CORRECTION to parent battery: the parent recorded "94-82-06 x3"; the bigram 94-82 is x4 — @1742 [a8_07] `86 12 34 94 82 46 56` continues to 46="que", not 06. The 06-continuation is not fixed.
- 94 followers: 82 x4, 74 x3, 59 x3, 52 x3, 92 x2, 24 x2, 76 x2, 79 x2, 93 x1, 65 x1, 06 x1, 02 x1, 64 x1, 29 x1, 60 x1.
- 94 left-neighbors at the four left-of-82 slots: 61 (@578), 78 (@1182), 78 (@1353), 12 (@1742). 18's left neighbor at 736: 76. No match.

**Shared-follower windows compared pair-by-pair (superficial overlap only):**
- 18->93 @9 [a1_00]: `78 18 93 62` vs 94->93 @101 [a1_02]: `62 94 93 59` — different left and right context.
- 18->79 @1009 [a6_02]: `35 18 79(tout) 80` vs 94->79 x2 @1363 [a7_06] / @1687 [a8_05]: both `62 94 79 14 60` (identical doubled context) — different from 18's.
- 18->82 @736 [a5_02]: `76(noun) 18 82(m) 06(ent) 00(pour) 36` — the variant frame.
- 62->18 @1066 [a6_04]: `62 18 70(pre) 39` vs 62->94 x9 (8 rows). Same left group (62), different right slot.

**Rate test:** 18->82 = 1/7 (14%); 94->82 = 4/37 (11%). Fisher exact two-sided p = 1.0 — rates compatible, probative of nothing at these counts.

**Word-edge candidates at 736** (`76 18 82 06 00 36`, 00="pour" granted):
- [18]|[82-06] = "X | ment pour [36]": "ment" standalone is non-lexical UNLESS read as mentir 3sg — "76 [18] ment pour [36]" = "[76] ne ment pour [36]" ("[76] does not lie for [36]") requires 18="ne"-class (ungranted #1) + 36 = pour's complement (ungranted #2). Conditional only.
- [18-82-06] one word = "Xment pour": adverb with 18 as stem — requires 18's value (ungranted).
- [18-82]|[06] ("18m|ent") and [18]|[82]|[06] ("X|m|ent") — EXCLUDED: "m" and "ent" are not standalone French words.

## Per-clause pass/fail

1. **Frames exist — PASS WITH CORRECTION.** 18-82-06 @736 verified; 94-82-06 @578/@1182/@1353 verified; 94-82 bigram is x4, not x3 (the @1742 ->46 continuation is new vs the parent census).
2. **Slot-equivalence — UNDECIDED (neither demonstrated nor rejected).** 18's n=7 all-singleton distribution has no profile to match against 94's left-of-82 slot; the single co-occurrence is rate-compatible (Fisher p=1.0) but context-mismatched (76 vs 61/78/78/12; shared followers sit in different windows). The bar's "distribution matches" criterion cannot be met at this n, and no window forces 18 out of the slot either.
3. **Word-edge decided — FAIL (undecided).** Every surviving edge placement needs 18's value: the mentir-3sg conditional parse needs 2 ungranted assumptions; the one-word "Xment" needs 18's value. The two sub-lexical edges are excluded.
4. **Adverses answered — PASS.** 18's value not named (frame B stays fenced on 18, as briefed). 00="pour" honored in every candidate parse ("ment pour [36]" / "Xment pour [36]").

## Verdict

**NULL.** 18's distribution (n=7, no repeats anywhere) is too thin for the bar's slot-equivalence test in either direction, and the 736 word-edge placement is downstream of 18's value, which remains unknown. The parent's "X variable supports edge-after-X" observation stands but is not advanced: a pure edge-after-X parse yields non-lexical standalone "ment", so the viable readings are the conditional "ne ment pour" (mentir 3sg) or one-word "Xment", both gated on naming 18. No standing verdict contradicted or downgraded. R5005, sealed gates, and the red-team queue untouched.

## Follow-up targets for the supervisor queue (null regeneration)

**F2a. id: "val-18-seven" | priority: 2**
claim: "name 18's value across its 7 windows (@9/@302/@585/@736/@905/@1009/@1066)"
bars: "one value parses >=6/7 windows with <=1 ungranted assumption; kill iff no value does; 'ne'-class tested at @9/@736, stem/determiner readings at the rest"
evidence: "seg-94-82-06-f2 null (2026-10-09): 18 has no distributional profile (all-singleton followers/neighbors); frame B and the 736 word-edge are gated on its value"
adverses: "18->79 @1009 ('X tout') constrains 'ne'-class readings; do not re-run the slot-equivalence test"

**F2b. id: "islet-94-82-1742" | priority: 2**
claim: "94-82-46 @1742 decides whether 94-82 is a fixed islet or 94 is left-free"
bars: "parse '12 34 94 82 46 56' @1742 under standing values; name the 94-82 relation iff one parse covers it with <=1 ungranted assumption"
evidence: "seg-94-82-06-f2 null (2026-10-09): 4th 94-82 instance found, continuation 46='que' not 06 — the 06-continuation is not fixed"
adverses: "F61 islet (06='ent' iff pre=82) unchanged; 46='que' banked"

**F2c. id: "edge-736-rerun" | priority: 3**
claim: "re-test the 736 word-edge once 18's value is named"
bars: "gated on val-18-seven resolving; decide [18]|[82-06] vs [18-82-06] under the named value with <=1 ungranted assumption"
evidence: "seg-94-82-06-f2 null (2026-10-09): conditional parses identified ('ne ment pour' mentir-3sg; one-word 'Xment')"
adverses: "sub-lexical edges ([18-82]|[06], [18]|[82]|[06]) already excluded — do not re-test"
