# Battery verdict: cont98-43-value — naming 98 and re-testing @1725

- Target: `cont98-43-value`
- Claim: Naming 98 (copula-like vs other) decides condition vs mesure via continuation B (43-98-39)
- Worker: battery-worker cont98-43-value (65ef220a-e4b7-4a3e-ace6-4ed4dbeb0801)
- Date: 2026-10-08
- Verdict: **NULL**

## 1. Bar (verbatim from battery-queue.json)

"name 98 iff >=2 independent frames parse under one value with zero contradictions across its 40 windows; then re-test @1725 under 43 = condition vs 43 = mesure and record which value continuation B selects"

Numbered clauses:
1. 98 takes one named value, supported by >=2 independent frames that parse under that value, with zero contradictions (no window forces 98≠value) across all 40 windows of 98.
2. Re-test @1725 (43-98-39) under 43='condition' vs 43='mesure'; record which value continuation B selects.

## 2. Method

- Stream: repaired 1,847-pair parse only (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization). canonical.py never used. R5005 untouched. No invented numbers.
- 98 census re-derived: n=40 at @12, 19, 80, 89, 92, 124, 192, 227, 236, 355, 440, 511, 702, 767, 803, 838, 894, 897, 930, 946, 971, 1060, 1073, 1074, 1137, 1139, 1145, 1146, 1284, 1317, 1325, 1373, 1481, 1579, 1601, 1643, 1660, 1661, 1725, 1783. Successors: 83 x5, 82 x3, 80 x3, 98 x3, 00 x3 (matches brief).
- Standing values used as given (protocol §7): 11=la, 82=m, 46=que, 64=qui, 96=par, 17=fois, 00=pour, 87=ce, 94=ne, 12=n, 48=e, 84=on, 47=ce, 59=est (prov), 77=le (prov), 06=ent, 30=pas, 86 INF-class, 80/89 verb-frames.
- The vient-98-name battery (processed/, verdict PROMOTE battery-grade 2026-10-08) is NOT re-litigated wholesale; its window calls were spot-verified against the stream below and its fenced residuals adopted where the strain localizes to other tokens. No standing red-team verdict covers 98.

## 3. Window-level evidence

### Clause-1 frames for 98='vient' (re-derived, byte-exact)

Frame V1 — 'venir de' + INF (83='de' lead):
- Formula `98 83 82 96 21` byte-identical x3: @227 (`98 83 82 96 21 60`), @1060 (`98 83 82 96 21 62`), @1783 (`98 83 82 96 21 68`). Thirds 60/62/68 vary; 5-gram identical.
- @897: `14 98 83 86` = '[14] vient de [86-inf]' (86 INF-class, A9 grant).

Frame V2 — 'venir pour' + complement:
- @1373: `67 98 00 86 29` = 'et vient pour [86]er' (67='et': follower 98 finite, positional rule holds; 86-29 infinitive shape). Clean.
- @1601: `82 98 00 44` = '[81] me vient pour [44]' ("l'idée me vient" shape; conditional on 81 noun-like, 44 pour-complement-like).

Frame V3 — 'qui vient' relatives (kills the 'em' arm):
- @19: `64 98 82 43 29` = 'qui vient me [43]er'. 'qui emmener' ungrammatical.
- @511: `64 98 65` = 'qui vient [65]' (65=noun, promoted 2026-10-08).

Frame V4 — demonstrative subjects:
- @192: `87 98 56` = 'ce vient [56]' (87='ce' granted).
- @1579: `47 98 24` = 'ce vient [24]' (47='ce' A4).

Supporting legs: @236 `70 98` = 'pré-vient' ('prévient'; kills 'revient': 'pré-revient' is not a word); @946 `62 98 96` = '[62] vient par [86]' (A14); @894/@803/@1325/@1137 `[62] vient` x4 (conditional on 62='il', demonstrated-not-promoted).

### Contradiction audit (all 40 windows)

Zero windows force 98≠'vient'. Non-parsing windows, all fenced with strain localized to other tokens (adopting vient-98-name's fences after spot-verification):
- @702 `12 98 20` ("n'vient", ungrammatical): strain on 12 ('ne' vs word-final 'n'); does not force 98≠'vient'.
- Doubled 98 x3 pairs @1073/@1074 (`42 98 98 12`), @1145/@1146 (`42 98 98 86`), @1660/@1661 (`47 98 98 80`): "vient vient" ungrammatical; candidates are scribal doubling or undeclared second value (red-team act per §7). Fenced, cause unknown; does not force 98≠'vient' globally.
- @1139 `00 98 78` ('pour vient'): complement of 'pour' needs infinitive 'venir'; inflectional alternation is a red-team act. Fenced, not declared. Same fence covers the second 98 at @1137 (`62 98 00 98 78`).
- @124/@971/@1317 (`66 98 82 48`, `01 98 48`, `62 48 98 15`): 48-slot residuals (verb-48 territory); strain on 48, not 98.
- @930 `82 98 83 56` ('me vient de [56]'): 'vient de' frame holds; 56's complement class underdetermined. Fenced as complement-class residual.
- @838 (`17 98 20`), @1643 (`33 98 60`): underdetermined (boundary or open-token assumptions); not contradictions.

Modal rivals ('peut'/'doit'-shaped) are killed by the 5/5 'vient de' frames (modals do not take 'de' + infinitive); 'revient' killed by @236; 'souvient' killed by absent reflexive; 'tient' killed by INF complements. (Per vient-98-name; not re-run.)

### Clause-2 re-test: @1725 under 43='condition' vs 43='mesure'

@1725 context (row a8_07, re-derived): `06 11 52 37 43 98 39 88 24 30 15 01 56`
= "[06-ent] la [52] [37] [43] vient à [88] [24] pas …"

With 98='vient' (clause 1), continuation B reads "[43] vient à [88]":
- 39 must be 'à' (preposition): 39='a' (avoir) after finite 'vient' is ungrammatical. Forced.
- 88's class is open (governor/verb-class); "à [88]" admits infinitive ("venir à + inf", transition: 'to come to do') or noun ("venir à" + goal).
- 43 is the subject NP head ("la [52] [37] [43]", feminine per 11='la').

Test:
- 43='condition': "la [52] [37] condition vient à [88]". Grammatical as a frame (subject-verb-preposition), but 'condition' (a static requirement) is not a natural subject of "venir à" (transition/process verb); no idiomatic "condition + venir à" collocation exists in 1841 French.
- 43='mesure': "la [52] [37] mesure vient à [88]". Same frame-grammar; 'mesure' (a step taken) is equally unnatural as a "venir à" subject; no idiomatic "mesure + venir à" collocation exists.

Neither value is forced or ruled out by the construction. "Venir à" selects for subjects capable of process/transition; both 'condition' and 'mesure' are equally (un)suitable, and 88's open value prevents resolving the infinitive-vs-noun reading that might discriminate. The copula readings ('être à'/'rester à' + inf) that the frame-43 battery called "live" are now DEAD (98='vient', not copula-like) — but their death does not select between the survivors either, since both were compatible under copula and both remain compatible under 'vient'.

Second 43-98 window @439 (`45 46 43 98 80` = '…que [43] vient [80]'): "[43] vient [80]" needs 80 infinitive-compatible (A8 verb-frame; bare infinitive after 'venir' is strained — conditional pass per vient-98-name). Does not discriminate condition/mesure.

## 4. Per-clause pass/fail

1. **PASS.** 98='vient': 4 independent frame-types (V1 'venir de', V2 'venir pour', V3 'qui vient', V4 demonstrative-subject) parse under one value; zero contradictions across all 40 windows (8 non-parsing windows fenced with strain localized to other tokens or unknown-cause reduplication; none forces 98≠'vient').
2. **INCONCLUSIVE (recorded).** Continuation B under 98='vient' is "[43] vient à [88]". It is compatible with both 43='condition' and 43='mesure' and selects NEITHER: no grammatical or collocational feature of "venir à" discriminates the two. The copula-based readings are dead (98 is not copula-like), but their removal does not break the tie.

## 5. Adverses answered

1. "98-98 doubled x3 pairs" → FENCED with stated cause (§3: unknown-cause reduplication; red-team act if second value; does not force 98≠'vient').
2. "98-83 x5 ('de'-follower) tensions a copula reading" → ANSWERED: the copula reading is dead (98='vient'); "vient de" is the core SUPPORTING frame (5/5), not a tension.
3. "frame-vient-parvenir's French for 98 is unconfirmed" → FENCED with stated cause: the full formula's French ("vient de me parvenir") is owned by the queued frame-vient-parvenir target and is not needed for 98='vient', which stands on four independent frame-types.

## 6. Verdict: NULL

Clause 1 passes: 98='vient' is (re-)named at battery grade with zero contradictions. Clause 2 does not deliver the decision: continuation B, under 98='vient', is "[43] vient à [88]" — grammatical but non-discriminating between 'condition' and 'mesure'. The claim's "decides" mechanism therefore does not fire. This is inconclusive on 43's value, not a refutation of either candidate: both survive, and the 43 question stays open for the dedicated noun-43 line. No standing verdict contradicted; R5005, sealed gates, and the red-team queue untouched.

## 7. Follow-up targets (null regenerates work)

F1. id: `name-88-value` | priority: 2
claim: "88 takes one value across its 23 windows, deciding the 'à [88]' complement at @1725"
bars: "name 88 iff one value (infinitive vs noun) parses >=80% of its 23 windows with the '39 88' x3 ('à [88]': @765 'est à [88]', @1514 'à [81] [88]', @1727 'vient à [88]') and the article followers ('88 77' x3, '88 11' x2) resolved; then re-test '43 vient à [88]'"
evidence: "88 n=23; pre 39 x2/69 x2; suc 77 x3/11 x2/24 x2; 88='governor/verb-class' (class-level only)"
adverses: "88's article followers tension a pure verb reading; 88's verb-class grant"

F2. id: `43-1126-1725-joint` | priority: 2
claim: "The byte-identical NP 'la [52] [37] [43]' (@1122/@1720, 5-gram '06-11-52-37-43' x2) takes 'pour [86-inf]' (@1126) and 'vient à [88]' (@1725); the JOINT continuations discriminate condition vs mesure where B alone cannot"
bars: "test 'condition' vs 'mesure' against both continuations jointly; select iff one value parses both and the other fails at least one at kill grade; else record the joint survivor set"
evidence: "shared 5-gram x2 byte-identical; @1126 '43 pour [86-inf]'; @1725 '43 vient à [88]'; frame-43 battery narrowed 4->2 via continuation A alone"
adverses: "52-37 unit value open; 88 value open; coordinates with (does not duplicate) noun-43-discriminator"

F3. id: `43-29-segment` | priority: 3
claim: "@21 'qui vient me [43]er' segments as word-internal '[43]er' infinitive, which would make 43 verb-stem-shaped and re-open the noun hypothesis"
bars: "decide the 43-29 boundary at @21 (word-internal vs word boundary) using 43's other 15 windows and 29's distribution; if word-internal, escalate the noun-43 hypothesis to the red team; do not re-name 43 at battery level"
evidence: "@21 '64 98 82 43 29' = 'qui vient me [43]er'; 43 n=16; vient-98-name noted the infinitive shape but kept noun-43"
adverses: "43's noun legs ('la [52] [37] 43' x2, 'par 43' x2); protocol §7 67-sole-polyvalence (a verb-stem 43 alongside noun-43 would need red-team act)"
