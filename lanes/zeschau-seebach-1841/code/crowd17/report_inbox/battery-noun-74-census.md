# Battery report: noun-74-census

- Target: `noun-74-census`
- Claim: "74 has a namable class, which would rescue @141's 'le [74]' as a determiner leg."
- Date: 2026-10-09
- Worker: battery worker (subagent b6588fbd-752c-4bed-9215-eb622b063eaa)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched.
- Lock: `code/crowd17/next-token/locks/noun-74-census.lock` (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"name 74's class iff a single class covers >=2/3 of its 34 windows with zero
contradictions; else fence 74 as class-open and @141 stays headless."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1** — enumerate all 34 windows of 74 byte-exact on the repaired stream.
2. **C2** — name 74's class iff ONE class covers >=23/34 windows (>=2/3) with
   ZERO contradictions (a window forces 74 != the class at kill grade).
3. **C3** — else fence 74 as class-open; @141's 'le [74]' stays headless
   (the bar's explicit else-branch = fence, i.e. null, not kill).
4. **C4** — adverse answered: "74's distribution is diffuse; the unit reading
   may win" — tested, not ignored.

## Method

1. Re-derived the repaired parse in-session (1,847 pairs / 96 types asserted).
   Never used `canonical.py`. R5005 untouched.
2. Full census of 74: n(74) = 34, byte-exact. Predecessors: 74 x6, 49 x5,
   94 x3, 39 x2, 44 x2, 36 x2, 14/19/84/78/63/20/29/77/69/41/24/01/87/48 x1.
   Successors: 74 x6, 45 x3, 46 x3, 62 x3, 67 x2, 77 x2, 65 x2, 47 x2,
   48/49/40/42/32/52/34/84/87/35/93 x1.
3. Adopted as premises (not re-litigated): `ne-alone-02-74` KILL (2026-10-09)
   — verb-74 rejected at the lane's distributional standard (zero verb-frame
   contact across all 34 windows; '74 74' self-loop x6 resists verb-shape);
   `det14-elsewhere` NULL/fence (2026-10-09) — 14's determiner value fenced to
   the frame-tail windows @1365/@1689; `det-14-census` PROMOTE (locus-level,
   2026-10-09) — 14 determiner-shaped only at @117.
4. Scored every window under noun-74 (the only surviving whole-word candidate
   after verb-74's kill) against standing values: banked GT (11=la, 70=pre,
   82=m, 34=i, 29=er, 40=e, 46=que), promoted (87=ce, 64=qui, 96=par, 17=fois,
   79=tout, 00=pour, 84=on A15, 47=ce A4), provisional (59=est, 77=le),
   red-team R17-001 (94=ne STRONG LEAD), R18 (65=noun, 36=noun class).

## Window-level evidence (0-based @; ±3 context; row)

Doubling family — '74 74' bigram x6 (12 windows):
- @417 (a2_08): `49 74 74 46` — "49 [74] [74] que(46)"
- @418 (a2_08): `74 74 46 49` — "[74] [74] que(46) [49]"
- @816 (a5_05): `49 74 74 47` — "49 [74] [74] ce(47)"
- @817 (a5_05): `74 74 47 78` — "[74] [74] ce(47) [78]"
- @861 (a5_07): `49 74 74 48` — "49 [74] [74] [48]"
- @862 (a5_07): `74 74 48 47` — "[74] [74] [48] ce(47)"
- @919 (a5_09): `49 74 74 40` — "49 [74] [74] e(40)"
- @920 (a5_09): `74 74 40 08` — "[74] [74] e(40) [08]"
- @1053 (a6_04): `29 74 74 45` — "er(29) [74] [74] ce(45)"
- @1054 (a6_04): `74 74 45 23` — "[74] [74] ce(45) [23]"
- @1637 (a8_03): `87 74 74 35` — "ce(87) [74] [74] [35]"
- @1638 (a8_04): `74 74 35 56` — "[74] [74] [35] [56]" (straddles a8_03/a8_04
  row boundary; the adjacency is stream-continuous)

Non-doubling windows (22):
- @142 (a1_04): `14 74 67 64` — "[14] [74] et/veut(67) qui(64)"
- @212 (a2_00): `19 74 77 78` — "[19-verb] [74] le(77) [78]"
- @261 (a2_02): `84 74 45 93` — "on(84) [74] ce(45) [93]"
- @350 (a2_05): `94 74 67 78` — "ne(94) [74] et(67) [78]"
- @477 (a2_11): `78 74 45 93` — "[78] [74] ce(45) [93]"
- @635 (a4_01): `63 74 46 60` — "[63-verb] [74] que(46) [60]"
- @693 (a5_00): `39 74 46 02` — "[39-a/a] [74] que(46) [02]"
- @786 (a5_04): `94 74 65 84` — "ne(94) [74] [65-noun] on(84)"
- @801 (a5_05): `44 74 62 98` — "[44] [74] [62] [98]"
- @874 (a5_08): `20 74 49 16` — "[20-split] [74] [49] [16]"
- @1071 (a6_05): `44 74 42 98` — "[44] [74] [42] [98]"
- @1103 (a6_06): `94 74 47 78` — "ne(94) [74] ce(47) [78]"
- @1175 (a6_10): `36 74 32 48` — "[36-noun] [74] [32] [48]"
- @1307 (a7_04): `77 74 52 30` — "le(77) [74] [52] pas(30)"
- @1314 (a7_04): `36 74 62 48` — "[36-noun] [74] [62] [48]"
- @1414 (a7_07): `69 74 34 52` — "[69-noun] [74] i(34) [52]"
- @1500 (a7_11): `41 74 84 33` — "[41] [74] on(84) [33]"
- @1568 (a8_01): `24 74 62 48` — "[24-modal] [74] [62] [48]"
- @1635 (a8_03): `01 74 87 74` — "[01] [74] ce(87) [74]"
- @1677 (a8_05): `39 74 77 44` — "[39-a/a] [74] le(77) [44]"
- @1780 (a8_09): `48 74 65 23` — "[48-e] [74] [65-noun] [23]"
- @1845 (a8_11): `49 74 93` — "[49] [74] [93]" (row-final)

## Noun-74 scoring (the only surviving whole-word candidate)

CONTRADICTS noun at kill grade (22):
- All 12 doubling windows: two identical adjacent content words ("[74] [74]")
  are ungrammatical in French prose — no noun, verb, adjective, pronoun, or
  adverb doubles adjacently (six occurrences, varied contexts). Each forces
  74 != any whole-word class.
- @261 "on [74] ce": "on"(A15) + bare noun + "ce" — ungrammatical; 74 != noun
  (caveat: A15's conditions C1-C3 could in principle exclude this window, but
  no battery has done so).
- @350 "ne [74] et": "ne"(R17-001 STRONG LEAD) + bare noun — ungrammatical.
- @786 "ne [74] [65-noun]": "ne" + noun + noun — ungrammatical.
- @1103 "ne [74] ce": "ne" + noun — ungrammatical.
- @1175 "[36-noun] [74] [32]": bare "N N" juxtaposition — ungrammatical
  without punctuation (74-as-subject per queued `fem32e-subject-gender` does
  not license the "36 74" contact).
- @1314 "[36-noun] [74] [62]": same juxtaposition failure.
- @1414 "[69-noun] [74] i": same juxtaposition failure.
- @1500 "[41] [74] on": "[N] on" — subject pronoun after a bare noun,
  ungrammatical.
- @1568 "[24-modal] [74] [62]": modal + bare noun — ungrammatical
  (conditional on battery-promoted 24=modal; `24-en-verb-conflict` is a live
  red-team docket).
- @1780 "[48-e] [74] [65-noun]": "N N" juxtaposition — ungrammatical.

COVERED cleanly (3, all conditional on licensed provisional/promoted values):
- @212 "[19-verb] [74] le(77-prov) [78]": V + object-N + new NP "le [78]" —
  covered.
- @635 "[63-verb] [74] que(46) [60]": "[N] que [V]" relative — covered,
  conditional on verbal-60.
- @1307 "le(77-prov) [74] [52]": "le [N] [52]" — covered.

CONDITIONAL / UNDECIDABLE (9): @142 (14's determiner fenced here — see below),
@477 (78 open; "vert" word-internal rival live), @693, @801, @874, @1071,
@1635, @1677, @1845 (open neighbors, no forcing evidence either way).

Noun-74 coverage: 3/34 clean (8.8%), 22 kill-grade contradictions. The bar
needs >=23/34 with ZERO contradictions. The doubling family alone caps every
whole-word class at 22/34 = 64.7% < 66.7%.

Verb-74: dead by adoption — `ne-alone-02-74` KILL (2026-10-09) rejected it at
the lane's distributional standard (zero verb-frame contact across all 34
windows; self-loop x6 resists verb-shape). The doubling family independently
contradicts verb at all 12 windows.

Adjective/pronoun/adverb/determiner-74: each contradicted at kill grade by the
12 doubling windows (no such class doubles adjacently in French).

## The @141 rescue is doubly dead

1. Noun-74 fails the bar above — no nominal class to rescue with.
2. Independently: `det14-elsewhere` (NULL/fence, 2026-10-09) fenced 14's
   determiner value to the frame-tail windows @1365/@1689 (0/4 legs
   elsewhere); `det-14-census` (PROMOTE locus-level) licenses determiner-14
   only at @117. @141's "14 74" is not a licensed 'le [74]' window at battery
   grade. Even a nominal 74 would not license the determiner leg here.

## Per-clause pass/fail

1. **C1 PASS** — 34 windows enumerated byte-exact (n(74)=34 confirmed;
   predecessor/successor censuses match `ne-alone-02-74` independently).
2. **C2 FAIL** — no single class covers >=23/34 with zero contradictions.
   Best whole-word candidate (noun): 3 clean covers, 22 kill-grade
   contradictions. Verb: dead by adopted kill + 12 doubling contradictions.
3. **C3 FIRES** — fence 74 as class-open; @141's 'le [74]' stays headless
   (bar's explicit else-branch).
4. **C4 PASS** — adverse answered: the unit reading ("49 74 74" as a
   formula/word unit with sub-lexical 74, e.g. doubled consonant) is
   consistent with the doubling family and is the leading hypothesis — but it
   is not a namable word-class, so the bar's fence path fires. It is tested
   directly by follow-up 2 below, not ignored.

## Verdict: NULL (fence executed per the bar's else-branch)

74 stays class-open. @141's 'le [74]' stays headless as a determiner leg
(and is independently unlicensable per `det14-elsewhere`).

Canonicality caveat (stated, not hidden): all doubling windows sit on
offset-0 rows with unvalidated upstream offsets; the fence holds on the
canonical repaired stream per protocol. A row re-phase that dissolves a
doubling bigram would re-open that window only, not the class question
(10+ contradictions would remain).

No standing or red-team verdict contradicted or downgraded. No polyvalence
declared (§7 intact: 67 et/veut remains the sole true polyvalence).

## Follow-up targets (nulls regenerate work; all three verified ABSENT from
battery-queue.json)

1. `noun-74-formula` (P3): test 74 as a nominal/formula head in the
   '49 74 74 [46/47/48/40]' chains x4 (49-prev x5, self-loop x6). Bar:
   promote iff a French nominal/formula frame parses all four chains with
   stated boundary evidence; kill iff 74 shows verb-frame contact or no
   nominal frame parses. (Proposed by `ne-alone-02-74` but never queued.)
2. `unit-49-74-74` (P3): test "49 74 74" as a single word/unit with 74 as a
   letter/syllable (e.g. doubled consonant "-tt-"/"-ss-"). Bar: name the host
   word via 49's contact profile; the four chains parse with <=10% orphan;
   kill iff no French word-formation covers all four.
3. `det-74-141-rerun` (P4): re-test @141's 'le [74]' iff the red-team 14/77
   homophony docket ever extends 14's determiner value beyond the frame tail
   (@1365/@1689) and @117.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-noun-74-census.md` (this file).
- Queue: `battery-queue.json` — `noun-74-census` status `queued` -> `verdict`,
  result `null`, date 2026-10-09 (temp-file + rename; pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write; only this
  entry's keys touched).
- Lock created at start, deleted on completion.
