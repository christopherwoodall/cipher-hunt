# Battery report: prof-53 — 53 single-parse profile (decides 2/5 'ne' windows)

Worker: worker-prof-53-eea364f5. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
Lock: created locks/prof-53.lock 2026-10-08T12:36:32Z; no prior lock existed.

## Bar (verbatim from battery-queue.json)

"resolve iff single parse covers all 11 of 53's windows"

## Bar as numbered clauses (pre-registered before testing)

1. **Scope.** All 11 windows of 53 enumerated fresh on the repaired stream.
2. **Coverage.** ONE parse (a single value/segmentation for 53) parses all 11
   windows with zero forced contradiction — no window may require a second
   value, a positional rule, or an undeclared polyvalence.
3. **Decision.** The parse decides the 2 of 5 'ne' windows (@169, @709):
   12-48 reads either "ne" (negation) or "donne" (word-internal), consistent
   with the single parse.

## Method

Replicated repair_parse.py's tokenizer byte-exact
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]` per row with repaired offsets).
Enumerated all 53 occurrences (fresh counts; queue glosses not trusted).
Enumerated all 12-48 bigrams (fresh count). Tested three candidate parses
per window: (P-A) 'donne' compositional 53="don" + 12="n" + 48="e";
(P-B) 'donne' whole-word (pair 53 = "donne"); (P-C) 'ne' reading
(53 = standalone X, 12-48 = "ne" negation). Checked for any further
single-value candidate from window evidence. Standing values used:
11=la, 34=i, 82=m, 87=ce, 64=qui, 00=pour, 84=on, 47=ce, 17=fois,
12="n", 48="e" (promoted letters), 94="ne" (promoted), 59=est (provisional).
§7 obeyed: 67 is the sole true polyvalence; no second polyvalence declared.

## Window-level evidence (all 11 windows, @-offsets are pair indices)

- W1 @16 (a1_00): `98 76 45 91 [53] 17 64 98 82` — "91 [53] fois(17) qui(64)".
- W2 @57 (a1_01): `79 85 58 35 [53] 12 41 08 34` — "35 [53] n(12) [41]".
- W3 @168 (a1_05): `11 24 82 84 [53] 12 48 21 60` — "on(84) [53] n(12) e(48) 21".
- W4 @403 (a2_08): `06 11 45 88 [53] 34 69 26 00` — "88 [53] i(34)".
- W5 @411 (a2_08): `00 33 01 02 [53] 84 51 37 78` — "02 [53] on(84)".
- W6 @708 (a5_01): `12 66 21 35 [53] 12 48 71 12` — "35 [53] n(12) e(48) 71".
- W7 @804 (a5_05): `44 74 62 98 [53] 69 24 24 41` — "98 [53] 69".
- W8 @1020 (a6_03): `41 15 66 91 [53] 84 92 64 45` — "91 [53] on(84)".
- W9 @1280 (a7_03): `48 56 85 48 [53] 61 56 32 98` — "e(48) [53] 61".
- W10 @1473 (a7_10): `38 26 12 41 [53] 60 06 67 33` — "41 [53] 60".
- W11 @1581 (a8_02): `76 47 98 24 [53] 12 44 00 36` — "24 [53] n(12) [44]".

Contact profile (fresh): 53 n=11; predecessors 91x2, 35x2, 84, 88, 02, 98,
48, 41, 24; followers 12x4, 84x2, 17, 34, 69, 61, 60. Top follower 12 (4/11)
confirmed.

12-48 bigrams (fresh): x5 at @169 (pre 53), @709 (pre 53), @809 (pre 41),
@1075 (pre 98), @1736 (pre 60). The 2 disputed 'ne' windows are @169/@709.

41 profile: n=19; successors 12, 15, 06, 01, 08, 98 (word-like).
44 profile: n=15; successors 00x3, 59x2, 74, 83 (word-like).
Neither 41 nor 44 is in the spelling-letter band; neither can complete a
"donnV" word.

## Per-window parse tests

P-A ('donne' compositional, 53="don" + 12="n" + 48="e"):
- W3 @168 "on donne 21": CLEAN. W6 @708 "35 donne 71": CLEAN.
- W2 @57 "35 donn[41]": 41 is word-valued (n=19), cannot be the final "e" of
  "donne"; "donn"+"[41]" is a broken word. FORCED CONTRADICTION.
- W11 @1581 "24 donn[44]": same, 44 word-valued (n=15). FORCED CONTRADICTION.
- The same 53-12 contact would have to be word-internal "n" at W3/W6 and
  word-boundary "n" at W2/W11: a positional polyvalence for 53, barred by §7
  (67 is the sole true polyvalence; only the red team may declare another).
- W1, W4, W5, W7, W8, W9, W10: "don" as noun/stem leaves "91 don fois",
  "88 don i", "02 don on", "98 don 69", "91 don on", "e don 61",
  "41 don 60" — none parse cleanly; at best fenced with unstated causes.

P-B ('donne' whole-word, pair 53 = "donne"):
- W2 @57 "35 donne n 41" = "donnen [41]": broken. KILLED at W2.
- W11 @1581 "24 donne n 44": broken. KILLED at W11 independently.

P-C ('ne' reading, 53 = standalone X, 12-48 = "ne"):
- W3 @168 "on X ne 21": no grammatical X exists between subject "on" and
  negation "ne" (clitics and adverbs do not occupy that slot). Ungrammatical
  for every candidate X. KILLED at W3.
- W6 @708 "35 X ne 71": "35" would need to be a subject taking "X ne";
  same empty slot. KILLED at W6.

Further candidates from window evidence: 53 as adjective before "fois"
(W1: "91 [53] fois" — "dernière/seule/prochaine" slot) fails at W3/W5/W8;
53 as noun "don" fails at W1/W4/W7/W9/W10; 53 as verb fails at W1/W4/W5/W8.
No single value covers all 11 windows.

## Per-clause pass/fail

1. Scope: PASS. n=11 confirmed on the repaired stream at @16, @57, @168,
   @403, @411, @708, @804, @1020, @1280, @1473, @1581.
2. Coverage: FAIL. P-A is clean at 2 windows but forced false at W2/W11
   (53-12-41, 53-12-44) and unparseable at 7 others; P-B killed at W2/W11;
   P-C killed at W3/W6; no further single parse found.
3. Decision: FAIL. The 2 of 5 'ne' windows (@169, @709) remain undecided:
   the 'donne' reading is grammatical there but cannot be the single parse;
   the 'ne' reading is ungrammatical there for any X.

## Verdict: null

No single parse covers all 11 of 53's windows. The queue gloss's 'donne'
alternative is real at @168/@708 ("on donne 21", "35 donne 71" both clean)
but 53-12-41 (@57) and 53-12-44 (@1581) break it as a single parse, exactly
as the gloss suspected — now demonstrated on fresh counts: 41/44 are
word-valued, not word-final letters, so the 53-12 contact cannot be
word-internal "n" everywhere.

Consequence for the 2/5 'ne' windows: @169/@709 stay disputed. The 3
undisputed 'ne' windows (@809, @1075, @1736) are unaffected; ne-le-1075
("98 ne le 77") does not touch 53. The negation-'ne' census via 12-48 is
3 clean + 2 disputed, pending the follow-ups below.

Worker corrections (no verdict contradicted): queue gloss @-offsets were
off by one (53 sits at @168/@708; the 12s at @169/@709; 53-12-41 at
@57-59; 53-12-44 at @1581-83). The n-e-12-48 battery's "'ne'=12-48 x7"
gloss re-derives as x5 on the repaired stream (its promotion rests on
GT-anchored legs, not the count; noted for downstream citations).

No standing red-team verdict on 53 exists; nothing contradicted, nothing
overwritten. Sealed gates and the adjudication queue untouched.

## Follow-ups (null regenerates work)

1. **donne-168-708-leg** (priority 2): 2-window leg battery. Bar: "on donne 21"
   (@168) and "35 donne 71" (@708) parse with 21/71 named; 53-12-41/44
   explicitly out of scope (fenced to donn-41-44). Adverses: leg does not
   decide 53's profile; 21/71 unnamed.
2. **donn-41-44** (priority 3): name 41 and 44 (word-valued, n=19/n=15).
   Bar: 41/44 named with >=2 frame-legs each; if either resolves as a
   vowel-letter or inflectional ending, re-open prof-53 under 53="don"-stem.
   Adverses: 41/44 word-like successor profiles.
3. **ne-census-1248** (priority 3): re-derive the 12-48 census on the repaired
   stream (x5, not x7) and restate negation-'ne' as 3 clean + 2 disputed
   (@169/@709 pending donne-168-708-leg). Correct downstream citations of
   the x7 gloss. Adverses: none; bookkeeping.
