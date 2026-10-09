# Battery report: adj-groundwork-refollower (NULL — no adjective value namable at battery grade)

**Target:** adj-groundwork-refollower (priority 2). Worker: b7802f27-4cf6-4435-9e0f-b8f080b54966 (supervisor-dispatched). Date: 2026-10-08.
**Stream:** repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`; 1,847 pairs, 96 groups, asserts hold). `canonical.py` never used. R5005 untouched. Sealed gates untouched. Red-team adjudication queue untouched. No data invented. @-offsets 0-indexed on the repaired stream.
**Lock:** `code/crowd17/next-token/locks/adj-groundwork-refollower.lock` created on start (no stale lock existed; no prior lock for this id), deleted on completion.

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"name >=1 adjective value with >=2 independent legs (e.g. test whether est-59-frames' predicative 30/39/37 extend to postnominal attributive use, or via det-adj-80), then re-test the adjective-follower prong of the ellipsis battery's bars."

## Bar as numbered pass/fail clauses (frozen before testing; not modified after seeing data)

1. **C1:** >=1 adjective value/class is named with >=2 independent legs on the repaired stream, via a route that does not re-litigate est-59-frames, does not duplicate det-adj-80 / adj-80-469-ratify, and invents no values (adverses).
2. **C2:** the followers of 65/62/60 are re-censused for adjective followers against the C1 value/class (i.e. the adjective-follower prong of the ellipsis battery's bars is re-tested).

Note on the bar's two examples: (a) the est-59-frames extension (predicative 30/39/37 -> postnominal attributive) is barred by the adverses ("predicative != attributive - do not re-litigate est-59-frames"); (b) the det-adj-80 route is barred by the adverses ("coordinate with queued adj-80-469-ratify / det-adj-80 verdicts, do not duplicate") and is gated on 06='ent' ratification + 43's value. Both example routes were therefore treated as unavailable; the bar was tested via original distributional work below.

## Method

1. Read BATTERY-PROTOCOL.md in full. Read the standing adjective-state reports: battery-ellipsis-65-62-60-profile (null; prong untestable), processed/battery-adj-frame-995-solo (promote, frame-level), battery-det-adj-80-adjudicate (null; @469/@1090 conditional, @1156 hard determiner), processed/battery-est-59-frames (promote, frames; predicative only), battery-adj-52-37-value (null; {même,seule,dite} tie), battery-unit-52-37-name (null; split candidacy), battery-dite-52-37-anaphora (kill "dite" -> {même,seule} tie), battery-adj-frames-995-637 (null).
2. Built an original adjective-frame survey on the repaired stream, using standing values only (protocol §7): banked 11=la,70=pre,82=m,34=i,29=er,40=e,46=que; granted 87=ce,64=qui,96=par,17=fois,79=tout,00=pour,84=on,47=ce; provisional 59=est,77=le; battery-promoted 94=ne,12=n,48=e,06=ent,30=pas,39=/a/.
3. Frame detectors (all adjective-shaped, none touching 59-copular or 80 windows):
   - **F-tout:** "tout[79] X" followers (tout + adjective intensifier frame).
   - **F-pre:** DET(11/77/87/47) + X + N, N in nominal-supported {03,43,17}.
   - **F-post:** [DET N] X postnominal via DET(11/47/87/77) + N(03/43/17) + X, plus bare N-X bigrams.
   - **F-detqui:** DET X 64 (qui) trigrams.
4. Full censuses for every adjective-shaped candidate found (14, 91, 55, 78, 85) to test >=2 independent legs.

## Window-level evidence (@-offsets, all re-derived)

### F-tout: "tout[79] X" followers (n=19 windows)

80 x3 (gated — det-adj-80 territory, not touched); 85 x2; 82 x2 (82=m banked, pronoun); 17 x2 (17=fois, "toutes les fois"-shaped, count-noun not adjective); 87 x2 (87=ce, "tout ce"); 14 x2; 37 x1 (A1 predicative, S5-owned, barred); 88 x1; 68 x1; 15 x1; 65 x1 (@1683 "que tout [65]" — already read determiner-shaped by the ellipsis battery).

- **14 x2:** @1364 (a7_06) `13 92 62 94 79 14 60 03 30 82 16 91` and @1688 (a8_05) `13 93 62 94 79 14 60 27 46 24 85 58`. Both = "…62 ne[94] tout[79] [14] [60] …" — same "tout 14 60" trigram twice. Adjective-shaped ("tout [adj] [X]") BUT the head X=60 is red-team-gated: noun-60 KILL, adj-60 KILL (single-value), verb-60 NULL, poly-60-redteam queued. Naming 14=adjective via contested 60 exceeds battery grade (would preempt the red team; protocol §5.2).
- **85 x2:** @53 (a1_01) `92 79 37 11 79 85 58 35 53 12 41 08` and @594 (a4_00) `41 09 00 92 79 85 01 29 40 03 39 26`. 85's verb-stem frames are GRANTED (A3, §7). Making 85 an adjective contradicts a standing grant — not available.
- **88/68/15/65 x1:** singletons, no second leg anywhere in the survey.

### F-pre: DET + X + N (prenominal)

Only 2 hits stream-wide:
- @1028 (a6_03): `87 01 03` = "ce[87] [01] [03]" — 01 unvalued, single leg.
- @1542 (a8_00): `93 88 77 78 43 00 46` = "…le[77,provisional] [78] [43]…" — 78 adjective-shaped prenominal, single leg.

### F-post: [DET N] X postnominal

- @721 (a5_02): `01 02 21 80 77 03 91 65` = "…le[77] [03] [91] [65]…" — 91 postnominal-adjective-shaped, single leg.
- @1203 (a7_00): `64 29 45 58 47 43 55 61` = "…ce[47] [43] [55]…" — 55 postnominal-shaped, single leg.
- Others are clause edges, not adjective slots: @562 "la 43 24" (24 = finite verb, granted); @1013 "ce 03 24" (verb); @1288 "la fois 84" (84=on, clause); @1789 "ce 03 00" (00=pour, clause).
- Bare N-X bigrams: ('03','60') x1 = @995 frame (promoted frame-level; 60's value unnamed, red-team-gated); ('03','91') x1 = @721; no other N+adjective-shaped bigram recurs.

### F-detqui: DET X qui

Only ('77','78') x1 = @1078 "le[77] [78] qui[64]" — 78 nominal-before-qui, not adjectival (relative-head = nominal slot).

### Full censuses of adjective-shaped candidates

- **91 (n=21):** @15 `98 76 45 91 53 17 64`; @36 `32 01 08 91 39 64 41`; @137 `21 65 23 91 65 13 66`; @247 `43 00 66 91 32 44 94`; @256 `00 66 01 91 32 43 77`; @277 `29 89 84 91 37 61 20`; @301 `40 97 86 91 18 89 88`; @387 `38 37 43 91 36 62 91`; @390 `91 36 62 91 84 73 34`; @520 `80 09 70 91 77 06 55`; @538 `24 82 16 91 12 44 29`; @723 `80 77 03 91 65 64 11` (the single postnominal leg); @852 `62 21 67 91 51 64 32`; @1005 `86 56 47 91 11 52 35`; @1019 `41 15 66 91 53 84 92`; @1371 `30 82 16 91 67 98 00`; @1428 `29 87 63 91 61 12 16`; @1518 `11 31 11 91 67 08 31`; @1668 `84 64 06 91 11 78 55`; @1698 `58 15 23 91 85 33 94`; @1798 `94 59 37 91 79 87 64` ("n'est [37] [91]" — predicative-59 territory, barred). Verdict on survey: exactly ONE adjective-shaped window (@723). No second leg.
- **55 (n=12):** dominant collocations "13 55 61" x2 (@576/@1167) and "55 81" x4 (@25,@523,@1085,@1094); 81="prin" KILLED (§7). "ce 43 55" @1205 is the single postnominal-shaped window. Verdict: one leg, and the main collocate's value is killed.
- **78 (n=33):** dominant frames are '37 78 X' (@313 `84 24 37 78 45 64 59`, @476 `84 24 37 78 74 45 93`, @352 `67 78 40 92 98` — 37 is S5-owned, barred) and '47 78 X' x5+ (@364, @819, @982, @1105, @1397) — pronominal/nominal-shaped, not adjectival. "le 78 43" @1542 is the single prenominal leg; "le 78 qui" @1078 is nominal. Verdict: one leg, dominant frames non-adjectival.
- **14 (n=2):** both windows are "tout 14 60" (@1364/@1688); head 60 red-team-gated. Verdict: two windows but one pattern, and unusable until poly-60-redteam rules.

### Standing-state check (adopted, not re-litigated)

- est-59-frames PROMOTE (frames): 30/39/37 predicative after "n'est" only. 30='pas' promoted (negation); 39=/a/ preposition at @762; 37 A1-predicative (S5-owned, frame-37-reexam queued). Per adverses, predicative != attributive — none serves the follower prong, and re-litigation is barred.
- adj-frame-995-solo PROMOTE (frame-level): "[03-N] [60-adj] et la" @995; 60's VALUE unnamed; noun-60 KILL and adj-60 KILL stand; poly-60-redteam queued. Not a named adjective value; preempting the red team is forbidden (§5.2).
- 52-37 Type-A: "dite" KILLED (dite-52-37-anaphora, 2026-10-09); {même, seule} tie owned by adj-52-37-value-rerun (gated on noun-43). Not named.
- det-adj-80-adjudicate NULL: @469/@1090 adjective legs CONDITIONAL on 06='ent' ratification (adj-80-469-ratify queued, gated); @1156 is a HARD determiner, not adjective. Not available.

### Follower re-census against standing values (C2 dependency)

65's followers {63,23,13,64,94,16,88,84,14,71,38,46,68,48,34}, 62's {94,48,98,16,61,06,96,91,21,18,38,46,93}, 60's {03,08,71,67,12,90,09,15,65,06,27} — none carries a standing adjective value (per the ellipsis battery's census, re-verified against this report's survey). The survey above finds no NEW adjective value to test them against, so the re-census has no operand: on standing values the adjective-follower prong remains empty, exactly as the ellipsis battery recorded.

## Per-clause pass/fail

- **C1 (name >=1 adjective value with >=2 independent legs): FAIL (inconclusive, not kill-grade).** The survey's best candidates each fall short: 14 has 2 windows but one pattern and a red-team-gated head (60); 91/55/78 have exactly one adjective-shaped window each with dominant non-adjectival collocations; 85 contradicts a standing verb-stem grant. Every other route to an adjective value is fenced: est-59-frames (predicative-only, re-litigation barred), det-adj-80 (gated/duplication barred), 52-37 Type-A ({même,seule} tie, gated), 60@995 (value unnamed, red-team-gated). This is absence of a promotable value at battery grade, not a forced-false — the value may exist behind pending rulings (06='ent' ratification, noun-43, poly-60-redteam).
- **C2 (re-census 65/62/60 followers): BLOCKED by C1.** With no C1 value, the re-census has no operand; on standing values alone the adjective-follower prong is empty (re-verified follower sets contain no standing adjective value). The ellipsis battery's §2 finding stands unrevised.
- **Kill-grade check:** not kill — no window forces the groundwork claim false, and no distributional test rejects at the lane's standard. The failure is the unavailability of a namable value under the adverses' constraints, i.e. inconclusive.

## Adverses (answered, none ignored)

- "predicative != attributive - do not re-litigate est-59-frames": honored. est-59-frames' 30/39/37 were adopted as standing (predicative only) and never re-tested; no predicative->attributive extension was attempted.
- "do not invent values": honored. No value was named on the basis of the single-leg windows (@723, @1205, @1542); single legs are recorded as legs, not values.
- "coordinate with queued adj-80-469-ratify / det-adj-80 verdicts, do not duplicate": honored. 80's "tout 80" x3 windows were counted in the census and fenced as gated territory; @469/@1090 were not re-tested.

## Verdict: NULL

Headline: no adjective value/class can be named with >=2 independent legs at battery grade under the adverses' constraints. The bar's two example routes are both barred (est-59-frames re-litigation; det-adj-80 duplication/gating), and original distributional work on the repaired stream finds only single-leg adjective-shaped candidates (91 @723 "le 03 91"; 55 @1205 "ce 43 55"; 78 @1542 "le 78 43") plus the gated "tout 14 60" x2 (@1364/@1688, head 60 red-team-gated) and the grant-contradicting 85. The adjective-follower prong of the ellipsis battery therefore remains untestable: on standing values, 65/62/60 have zero adjective followers. No standing verdict contradicted or downgraded; R5005, sealed gates, and the red-team queue untouched.

## Follow-up targets (null regeneration; for the supervisor to queue)

1. **adj-14-tout-gate** (priority 2): once the red team rules on poly-60-redteam, test "tout [14] [60]" @1364/@1688 as adjective legs for 14. Bar: name 14=adjective iff both windows parse as "tout [adj] [60-ruled]" with <=1 ungranted assumption under 60's ruled value; fence otherwise. Adverses: do not preempt the red team — gated on poly-60-redteam's verdict; do not touch verb-60. Evidence: this report's tout-X census (14 x2, byte-parallel "62 ne tout 14 60" at both windows).
2. **adj-91-723-second-leg** (priority 3): "le 03 91" @723 is one postnominal leg for 91; seek a second independent adjective leg for 91 among its 21 windows or fence the adjective reading. Bar: name 91=adjective iff >=2 independent adjective-shaped windows stand; fence iff the @723 window stands alone. Adverses: @1798 "n'est 37 91" is predicative-59 territory — excluded; do not re-litigate est-59-frames. Evidence: this report's 91 census (n=21, exactly one adjective-shaped window).
3. **adj-78-fence** (priority 3): fence or leg the adjective reading of 78. Its dominant collocations ('37 78 X' x3+, '47 78 X' x5+) are nominal/pronominal-shaped; "le 78 43" @1542 is the sole prenominal leg. Bar: fence 78-adjective iff no adjective-shaped frame besides @1542 stands; name 78=adjective iff a second independent leg is found. Adverses: 37's sub-lexical value owned by S5 — do not decide 37; '37 78' windows are nominal-context evidence only. Evidence: this report's 78 census (n=33).

## Standing constraints observed

- §7: standing values only; 67 sole-polyvalence untouched; prof-65, noun-60, adj-60, frame-20-62-94, pas-30, A3-85 verb-stem, and all cited verdicts respected, none downgraded; no second polyvalence declared.
- No invented numbers: every count re-derived above on the repaired 1,847-pair parse.

---
Lock: `locks/adj-groundwork-refollower.lock` created 2026-10-09T03:17Z, deleted on completion of this report.
