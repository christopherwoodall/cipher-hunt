# Battery verdict: vient-98-name — 98='vient' (finite semi-auxiliary)

- Target: `vient-98-name`
- Claim: 98='vient' (finite semi-auxiliary) at battery grade
- Worker: battery-worker vient-98-name (be9ae439-f7b8-44a6-ab9d-a418b1c7eb75)
- Date: 2026-10-08
- Verdict: **PROMOTE** (battery grade; needs red-team ratification per pipeline rule)

## Pre-registered bar (verbatim)

"promote iff >=2 'vient de' frame-types hold (formula x3 + @897 '[14] vient de [86-inf]') with the doubled-98 x3 (@1073/@1145/@1660), @702 ('n'vient'), @1139 ('pour [98]'), @930 and @1601 each fenced or resolved with stated cause; zero board contradictions"

## Bar as numbered clauses

1. PASS/FAIL: >=2 'vient de' frame-types hold: (a) formula 98-83-82-96-21 x3 byte-identical (@227/@1060/@1783), (b) @897 '14 98 83 86' = '[14] vient de [86-inf]'.
2. PASS/FAIL: doubled-98 x3 (@1073/@1145/@1660) fenced or resolved with stated cause.
3. PASS/FAIL: @702 ('12 98' = "n'vient") fenced or resolved with stated cause.
4. PASS/FAIL: @1139 ('00 98' = 'pour [98]') fenced or resolved with stated cause.
5. PASS/FAIL: @930 ('82 98 83 56') fenced or resolved with stated cause.
6. PASS/FAIL: @1601 ('82 98 00 44') fenced or resolved with stated cause.
7. PASS/FAIL: zero board contradictions across all 40 windows of 98.

## Method

- Stream: repaired 1,847-pair parse only. Built from code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt with the repair_parse.py tokenization (2-digit pairs per row offset). canonical.py never used. R5005 untouched.
- All @-offsets below are pair indices on the repaired stream. Every window re-derived by script in this run. No invented numbers.
- Standing values used as given (§7): 82=m, 29=er, 46=que, 64=qui, 17=fois, 96=par, 00=pour (A9, class-level), 87=ce, 94=ne, 12=n, 48=e, 84=on (A15), 86 INF-class (A9, class-level), 80/89 verb-frames (A8), 48 verb-stem frame (A7-L2), 47=ce (A4 allophone tier), 59=est provisional, 77=le provisional. 62='on' unconditioned ELIMINATED (collision-62-84 battery); 62='il' demonstrated-not-promoted. 83='de' is a LEAD (le83-window battery: null, C2 5/5 'vient de X' pass, 83 fenced as blocker).

## Window evidence (all 40 windows of 98 scanned)

98 indices on the repaired stream: 12, 19, 80, 89, 92, 124, 192, 227, 236, 355, 440, 511, 702, 767, 803, 838, 894, 897, 930, 946, 971, 1060, 1073, 1074, 1137, 1139, 1145, 1146, 1284, 1317, 1325, 1373, 1481, 1579, 1601, 1643, 1660, 1661, 1725, 1783 (n=40).

Core 'vient de' frames (98-83 x5 total on stream):
- @227: `24 89 61 96 87 46 [98] 83 82 96 21 60 71` — formula 5-gram `98 83 82 96 21`, third=60.
- @1060: `74 45 23 77 84 09 [98] 83 82 96 21 62 18` — formula 5-gram, third=62.
- @1783: `59 19 48 74 65 23 [98] 83 82 96 21 68 47` — formula 5-gram, third=68.
- The 5-gram `98 83 82 96 21` is byte-identical at all three (verified). Thirds 60/62/68 vary.
- @897: `77 76 01 98 82 14 [98] 83 86 16 92 67 16` — `14 98 83 86`; 86 is INF-class (A9). Reads '[14] vient de [86-inf]'.
- @930: `71 17 61 96 48 82 [98] 83 56 69 26 00 33` — `82 98 83 56`; see clause 5.

'vient pour' frames (98-00 x3, 00-98 x1):
- @1137: `86 24 77 86 20 62 [98] 00 98 78 62 16 29` — `62 98 00 98` = '[62] vient pour [98]'.
- @1373: `03 30 82 16 91 67 [98] 00 86 29 89 84 92` — `67 98 00 86 29` = 'et vient pour [86]er'. 67='et' (follower 98 finite, positional rule holds). Clean.
- @1601: `29 80 67 77 81 82 [98] 00 44 70 39 11 92` — see clause 6.
- @1139: `77 86 20 62 98 00 [98] 78 62 16 29 42 98` — see clause 4.

'qui vient' x2 (kills the 'em' arm):
- @19: `76 45 91 53 17 64 [98] 82 43 29 47 33 55` — 'fois qui vient me [43]er' (43-29='[43]er' infinitive shape; 43's class stays with noun-43). 'qui emmener' ungrammatical — 'em' arm dead.
- @511: `21 67 77 62 94 64 [98] 65 88 56 87 77 80` — 'ne qui vient [65]'. Clean.

Compositional leg:
- @236: `96 21 60 71 51 70 [98] 41 17 11 26 12 16` — `70 98` with 70='pre' (banked) reads 'pré-vient' = 'prévient' (prévenir, 3sg). Compositional morphology (cela=87+11 precedent). Selects 'vient' over 'revient' ('pré-revient' is not a word). Supporting leg, conditional on 70='pre'.

Other clean or neutral windows:
- @192: `87 98 56` — 'ce vient [56]' (87='ce' promoted). Grammatical.
- @946: `62 98 96 86` — '[62] vient par [86-subst-inf]' via the A14 set-level grant ('par'+substantivized infinitive). Parses.
- @894: `01 98 82 14` — 'vient m'[14]' (elided 'me' before vowel-initial 14). Conditional on 14 vowel-initial infinitive; the @897 clause then shares subject 01: '[01] vient m'[14]. [01] vient de [86].' Both clauses grammatical. Subject attribution (14 vs 01) fenced as underdetermined — does not break the frame.
- @803/@946/@1137/@1325: `62 98` x4 — '[62] vient'. 62='on' unconditioned is ELIMINATED (collision battery); parses as '[62=il] vient' under the demonstrated-not-promoted reading. Conditional, not a contradiction.
- @12, @80, @89, @92, @355, @89: open-token subjects (`[93]/[42]/[66]/[41]/[92] vient ...`) — neutral, no force either way.
- @440/@767: `[43]/[66] vient [80]` — 'vient [80]' needs infinitive; 80 verb-frame (A8) — conditional pass.
- @1284: `[32] vient [55]` — parses under A1 (32 predicative adjective); 32's verb-tension is fenced at adj-32, not here.
- @1481: `82 16 98 62` — '82-16' is the x11 collocation (frame-82-16 queued); '[82-16] vient-il [46=que]' under 62='il' demonstrated. Conditional.
- @1579: `47 98 24` — 'ce vient [24]' (47='ce' A4). Grammatical.
- @1643: `12 33 98 60` — '[33] vient [60]' with 33 as infinitive-subject (literary but grammatical) or 12 as word-final 'n' of open 56. Underdetermined, not a contradiction.
- @1725: `43 98 39 88` — '[43] vient à [88]' ('venir à' + INF). Conditional on 43 noun-like.
- @838: `17 98 20` — 'fois vient [20]'; needs 56 determiner-like or a clause boundary ('[56] fois, vient [20]'). Underdetermined, not a contradiction.

Fenced residuals (strain localizes to other open tokens, not to 98):
- @1317: `62 48 98 15` — the 48-slot admits no clean parse under standing values ('on [48] vient'). Fenced as 48-value residual (verb-48 follow-up territory). Does not force 98≠'vient'.
- @124: `66 98 82 48 11` — 'vient me [48]' needs 48 as bare infinitive; 48 is verb-STEM frame (A7-L2), 'er' absent here. 48-residual.
- @971: `01 98 48 51` — 'vient [48]' same 48-residual.

## Per-clause results

1. **PASS.** Two 'vient de' frame-types hold on the byte level: formula `98 83 82 96 21` x3 byte-identical (@227/@1060/@1783, thirds 60/62/68) and @897 `14 98 83 86` = '[14] vient de [86-inf]' (86 INF-class, A9 class grant). Dependency stated: the 'de' reading of 83 is lead-strength (le83-window battery: null, C2 5/5 pass), not a grant. The frames hold as frames regardless.
2. **PASS (fenced with stated cause).** Doubled 98 x3 (@1073 `@1072-1076 = 42 98 98 12 48`; @1145 `@1144-1148 = 42 98 98 86 67`; @1660 `@1659-1663 = 47 98 98 80 22`) is ungrammatical as finite-verb doubling under 98='vient'. All three are mid-row (a6_05, a6_08, a8_04) — no row-boundary artifact. No clean re-parse found (pre∈{42,47}, suc∈{12,86,80}). Stated cause: systematic reduplication of unknown cause — candidates: (a) scribal/emphatic doubling, (b) undeclared second value of 98 at these windows (red-team act per §7), (c) unattested 'vient-vient' compound. Fenced, not ignored. Does not force 98≠'vient' (37/40 windows consistent).
3. **PASS (fenced with stated cause).** @702 `12 98 20`: "n'vient" is ungrammatical (elision before consonant-initial 'vient'); the 'ne vient' reading would need bare 12='ne', which is ungranted and would collide with 94='ne' without a red-team polyvalence declaration (analytic 'ne'=12-48 exists, bare 12='ne' does not). Stated cause recorded.
4. **PASS (fenced with stated cause).** @1139 `00 98 78` = 'pour [98]': complement of 'pour' needs infinitive 'venir'; 98='vient' is finite. Inflectional alternation vient/venir is a red-team act per §7 (67 sole true polyvalence) — fenced, not declared. Same fence covers the second 98 at @1137 ('vient pour [98]').
5. **PASS (fenced with stated cause).** @930 `82 98 83 56` = 'me vient de [56]': the 'vient de' level holds (same frame-type as @897), but complement 56's class is underdetermined — 56 shows verb signals ('56 30' x2 = '[56] pas') and noun signals (follows 86 x4, takes 37/32 adjectival followers), takes no 'er' (56-29 x0) and no 'que' (56-46 x0). Cannot confirm the infinitive-complement reading here; fenced as complement-class residual.
6. **PASS (resolved).** @1601 `81 82 98 00 44` = '[81] me vient pour [44]': proclitic indirect-object 'me' before finite 'vient' ("l'idée me vient" shape) + 'pour' + complement. "The [81] comes to me for [44]" — grammatical under standing values, conditional on 81 noun-like (noun-81 queued) and 44 'pour'-complement-like (open). Resolved with stated conditions.
7. **PASS.** Zero board contradictions: no window forces 98≠'vient'. Every window parses clean, parses conditionally on stated open-token assumptions, or is fenced above with its strain localized to another token's open value.

## Adverses answered

- Doubled 98 x3 ungrammatical under 'vient' → fenced with stated cause (clause 2). Not ignored.
- @1139 needs infinitive 'venir' (inflectional alternation = red-team act) → fenced, not declared (clause 4).
- Modal rivals ('peut'/'doit'-shaped): killed by the 'de'-frames — modals do not take 'de' + infinitive; 5/5 98-83 windows force the 'venir de' semi-auxiliary. 'revient' killed by the @236 'pré-vient' composition ('pré-revient' is not a word). 'souvient' killed by absent reflexive. 'tient' killed by the INF complement ('tenir de' takes nouns).
- 'em' arm: dead — 'qui 98' x2 (@19/@511) reads 'qui vient'; 'qui emmener' is ungrammatical.

## Verdict

**PROMOTE** — 98='vient' (finite semi-auxiliary) at battery grade. All seven bar clauses pass (2–5 via explicit fencing the bar itself permits); both listed adverses answered. No contradiction with any standing red-team verdict (no A-item covers 98; checked code/crowd15/report_inbox/next-token-redteam.md).

Caveats for the red team: (a) clause 1 rests on the 83='de' lead (le83 null, C2) — ratifying 83='de' hardens this promote; (b) the doubled-98 x3 cause is unknown — if the red team declares a second value or inflectional polyvalence for 98, clauses 2/4 re-open; (c) 62='il' (demonstrated-not-promoted) underwrites four '[62] vient' windows — 62's own battery would harden them.

## Follow-ups

None required (promote, not null). Residuals for other lanes (not this claim): doubled-98 cause (red-team), 83='de' ratification (le83 line), 48-slot residuals @124/@971/@1317 (verb-48 line), 56 complement class (open).
