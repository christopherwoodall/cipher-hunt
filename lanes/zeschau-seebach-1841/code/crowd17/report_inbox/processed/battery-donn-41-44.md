# Battery verdict: donn-41-44

**Bar (verbatim, pre-registered):** "name 41/44 iff each has >=2 frame-legs; if either is a vowel-letter/inflectional ending, re-open prof-53 under 53='don'-stem"

**Numbered clauses:**
- C1 (name 41 with >=2 frame-legs): FAIL — no value parses >=2 windows; class open.
- C2 (name 44 with >=2 frame-legs): FAIL — four determiner-frame noun legs exist, but a global name is blocked by @541 (verb-stem "[44]er") and @1715 (clitic-slot per battery-clitic-44-census, promote); naming would contradict that standing verdict.
- C3 (vowel-letter/inflectional-ending test): FAIL for both — the letter/ending hypothesis is KILLED. Consequence: prof-53 is NOT re-opened; its "forced contradiction" at W2/W11 stands.

**Method:** Read BATTERY-PROTOCOL.md first; lock created/deleted per protocol. Re-derived the repaired 1,847-pair / 96-type stream in-session (`repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`; 1,847 pairs / 96 types verified). `canonical.py` never used; R5005, sealed gates, red-team queue untouched.

## 41 (n=19)

Census (1-based indices): 6, 40, 60, 92, 238, 445, 490, 590, 591, 809, 965, 1017, 1049, 1112, 1473, 1500, 1509, 1536, 1760. Predecessors: 14 distinct groups; successors: 17 distinct groups across 19 windows — a word-like profile.

**Letter kill (41='e'):** "41 41" doubling at @590-591 (row a3_02/a4_00, "97 41 41 09"). No French word contains "ee" as a bare digraph; a single letter 'e' cannot double. Clause-frame contacts confirm word status: @40 "qui(64) [41] 01" (41 in finite-verb slot after granted "qui"), @1017 "faire(24) [41] 15" (causative-faire complement slot), @238 "98 [41] fois(17)" (quantifier slot in the X-fois frame), @6 "ce(47) [41] 06" (nominal-clause slot). A sub-lexical 'e' does not occupy these slots.

**Inflectional-ending test:** the only stem+41 candidate is @1049 "85 [41] 88" (85 verb-stem A3). It is followed by 88 (verb-class) — a second finite verb with no boundary is ungrammatical; and it is a single window, not >=2 legs. FAIL.

**Naming attempt:** no candidate value parses >=2 windows. "donne"-window @58 ("35 53 12 41") is the W2 forced contradiction from prof-53, not a leg. 41 stays unnamed, class open.

## 44 (n=15)

Census (1-based indices): 209, 250, 528, 541, 798, 801, 1071, 1161, 1312, 1584, 1604, 1619, 1680, 1715, 1840. Predecessors: 12 distinct; successors: 10 distinct — word-like profile.

**Letter kill (44='e'):** four determiner frames, all on standing values: @209 "le(77) [44] 50" (77 provisional le), @1071 "la(11) [44] 74", @528 "ce(47) [44] est(59)" (47 A4 granted, 59 provisional), @1680 "le(77) [44] pour(00)". A letter cannot take a determiner. Additionally @541 "12 [44] er(29)": 44 BEARS the verbal ending 29='er' (banked GT) — 44 is the stem there, the opposite of an ending.

**Inflectional-ending test:** no stem+44 unit exists anywhere; the two sub-word windows (@541 "[44]er", @1161 "m(82)[44]") show 44 as stem, not ending. FAIL.

**Naming attempt:** 44=noun (class-level) has four frame-legs (@209, @528, @1071, @1680). But a global name is blocked: @541 forces verb-stem and @1715 is clitic-slot ("ne(94) [44] est(59)", value in {'en','l''}) per the standing battery verdict battery-clitic-44-census (promote, 12 nominal / 2 stem / 1 clitic). Promoting 44=noun would contradict that verdict (§5, never downgrade). The noun legs are packaged as follow-up 1 for red-team adjudication against the §7 split (venue: poly-44-docket).

## Adverse

"41/44 word-like successor profiles" — ANSWERED, confirmed: 41 has 17 distinct successors over 19 windows; 44 has 10 over 15. This is exactly why the vowel-letter hypothesis fails for both.

## Consequence for prof-53

Neither 41 nor 44 resolves as a vowel-letter or inflectional ending, so the C3 re-open condition does NOT fire. prof-53's forced contradictions stand: W2 @57 "35 donn[41]" and W11 @1581 "24 donn[44]" remain broken words under 53="don"-stem, and the compositional 'donne' survives only at the 53-12-48 windows (@168, @708).

## Verdict: NULL

Neither group can be named at battery grade. The deliverable is the letter-kill: the 'donne' rival cannot be rescued via a letter-valued 41/44.

## Follow-ups (for supervisor queuing)

1. `noun-44-legs-package` (P3): package 44's four determiner-frame noun legs (@209 "le [44]", @528 "ce [44] est", @1071 "la [44]", @1680 "le [44] pour") for red-team adjudication against the §7 split (@541 verb-stem, @1715 clitic-slot; venue poly-44-docket).
2. `class-41-contact` (P3): name 41's class via its three standing-value contacts — "qui(64) [41]" @40, "faire(24) [41]" @1017, "[98] [41] fois(17)" @238 — verb/noun/determiner discriminator; coordinate with (do not duplicate) any queued 41-class work.
