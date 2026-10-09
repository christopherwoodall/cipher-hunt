# Battery report: subj-42-ne-frame

- Target: `subj-42-ne-frame` (P2)
- Verdict: **NULL** (frame fenced; follow-ups proposed below)
- Date: 2026-10-09
- Worker: battery worker, agent 10c4ac79-f58e-4062-8f86-14926db9f421
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Offsets: 0-based repaired-stream indices. The brief's @493/@784/@1794 are the '42' positions of the three '42 94 X' windows; the X slots sit at @495 (02), @786 (74), @1796 (59).

## Bar (pre-registered BEFORE testing)

**Finding (protocol §2): the queue's `bars` field was null for this target — no bar was pre-registered upstream.** The bar below was stated by the worker before any window was examined (per the supervisor brief's suggested shape: resolve iff each of {02,74,59} takes a stated class with all three windows parsing under one frame statement, else fence the failing slot). It was not modified after seeing data.

Verbatim bar: "(1) @1794 control: '42 94 59 37' parses as '[42] n'est [37-predicative]' with 59 in the copular class (94-59 = 'n'est' per R17-001; 37 = predicative per A1); (2) @493: 02 takes a stated nominal class under one negative-nominal frame statement for '42 94 02' — the window '42 94 02 79 88 47 11 29 40' parses as a negative-nominal clause with 02 as nominal head (verbal already killed at distributional grade by ne-alone-02-74); (3) @786: 74 takes a stated nominal class under the same frame statement — '42 94 74 65 84 06 77 64 46' parses with 74 as nominal head; (4) one '42 94 X' frame statement covers all three windows; failing slots are fenced with stated cause. Verdict: promote iff all clauses pass with each X named to a nominal/copular class; kill iff a window forces the frame non-nominal; null otherwise."

Numbered clauses (frozen before testing):
- **B1**: control @1794–1797 '42 94 59 37' = "[42] n'est [37-pred]"; 59 is copular-shaped.
- **B2**: 02 is nominal-shaped at @495; the @493 window parses under a negative-nominal frame statement.
- **B3**: 74 is nominal-shaped at @786; the @784 window parses under the same frame statement.
- **B4**: one '42 94 X' frame statement covers all three windows.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/subj-42-ne-frame.lock` on start (no prior lock existed).
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types asserted).
3. Verified the closed '42 94 X' set byte-exact: exactly three windows — @493→02, @784→74, @1794→59. No other '42 94' adjacency exists.
4. Adopted as premises (completed battery verdicts, not re-litigated): `ne-alone-02-74` KILL (2026-10-09) — the verbal arm ("02/74 are the negated verbs in '42 ne 02'/'42 ne 74'") is dead at the lane's distributional standard (51 windows, zero verb-frame contact); `noun-74-census` NULL (2026-10-09) — 74 is class-open, noun-74 contradicted at kill grade (22 contradictions); `02-class-609` NULL (2026-10-09) — 02's class split/unnamable ("qui [02]" x2 verb-selecting vs non-finite forced at @305/@858).
5. Standing values used (never re-litigated): GT (11=la, 29=er, 40=e, 46=que, 64=qui); granted (47=ce A4, 79=tout A5, 84=on A15); provisional (59=est, 77=le); R17-001 (94-59 x3 = 'n'est', STRONG LEAD); A1 (37/32/42 predicative frames, value open).

## Window-level evidence

**Control — @1794–1797** (straddles a8_09/a8_10 row boundary; a8_09 ends at @1795):
`... 86 56 | 42 94 | 59 37 | 91 79 87 64 77`
= "[86] [56] | [42] n'est [37-pred] | [91] tout ce qui le".
'94 59' is R17-001's 'n'est' (x3 globally: @558, @762, @1795). 59's follower census: 37 x6, 32 x3, 35 x3 — predicative-frame followers, copular-shaped. 37 = predicative (A1 grant). The window parses cleanly as "[42] n'est [37-pred]".
Row-boundary note: 2 of the 3 '94 59' legs straddle upstream row boundaries (@558: a3_01/a3_02; @1795: a8_09/a8_10); stream-continuous adjacency holds (precedent: @1638 in noun-74-census). Not an anomaly; the control is undisturbed.

**@493–495** (row a2_11, mid-row):
`... 67 78 | 42 94 02 | 79 88 47 11 29 40`
= "et/veut [78] | [42] ne [02] tout [88-V] ce la er e".
79='tout' (A5), 88=verb (battery-promoted, class-level), 47='ce' (A4), 11='la', 29='er', 40='e'. The in-row verb 88 follows 'tout': the surface order is "ne [02] tout [V]".

**@784–786** (row a5_04, mid-row):
`... 11 24 | 42 94 74 | 65 84 06 77 64 46 | 07 64 56 37 44 77 86`
= "la [24] | [42] ne [74] [65] on [06] le qui que | [07] qui [56] [37] [44] le [86]".
84='on' (A15), 77='le' (provisional), 64='qui', 46='que'. 65 = noun-class (per noun-74-census: 65 takes 'qui' x3).

## Per-clause pass/fail

- **B1: PASS.** The control parses as "[42] n'est [37-pred]" under standing values (R17-001 + A1). 59 is copular-shaped ('59 37' x6, '59 32' x3, '59 35' x3). The copular arm of the frame is anchored.
- **B2: FAIL → FENCED.** 02 takes no stated nominal class at @495. 02's global profile is split and unnamable at battery grade (02-class-609 NULL, adopted): "qui [02]" x2 is verb-selecting, but @305 ("[88-V] [02] [88-V]") and @858 ("on [02] faire") force 02 non-finite; nominal legs ("la [02]" @128) exist but no class commands ≥2 consistent legs. At @493 specifically, no nominal frame parses the window: "ne [02] tout [88-V]" is ungrammatical for every candidate class of 02 — as nominal, 'ne' + bare noun is ungrammatical; as clitic, 'tout' cannot intervene between clitic and verb; as verb, killed at distributional grade (adopted). No clause-boundary placement inside the window is byte-evidenced (mid-row, continuous). The slot is fenced, not named.
- **B3: FAIL → FENCED.** 74 takes no stated nominal class at @786. 74 is class-open (noun-74-census NULL, adopted): noun-74 is contradicted at kill grade at this very window — "ne [74] [65-noun]" ('ne' + bare noun + noun) is ungrammatical — and the '74 74' x6 doubling family contradicts every whole-word class globally. No other nominal class parses "ne [74] [65] on...". The slot is fenced, not named.
- **B4: FAIL.** No one frame statement covers all three windows: the control is copular via an overt copula ('est'), while the @493 and @786 windows admit no stated nominal parse. The "one frame statement" requirement is not met.

## Verdict: NULL

The nominal arm does not resolve: X is not nominal-shaped in all three windows (B2 and B3 fenced). The verbal arm is already dead (adopted ne-alone-02-74 KILL). The '42 94' frame is therefore **fenced** — neither named copular/negative-nominal nor verbal. This is not a kill: no window forces the frame non-nominal (the untested leftward-composition account, "[42]ne", and 42's open value leave the frame genuinely unresolved rather than refuted). No standing red-team verdict is contradicted or downgraded: R17-001 ('n'est') stands untouched, the A1 predicative grant on 42 holds, and the @1794 control is undisturbed.

## Follow-up targets (nulls regenerate work; all three verified ABSENT from battery-queue.json)

1. `frame-42-94-leftward` (P3) — Test '42 94' as leftward composition "[42]ne" (word-final 'ne' syllable). Precedent: syll-94-508-verify's conditional "[62]ne" @508 (PROMOTE, conditional); 94's predecessor census shows leftward composition is live for 94 (62 x9, 42 x3, 82 x3, 12 x3). Re-parse all three windows: "[42ne] [59=est] [37]" (@1794), "[42ne] [02] tout [88]..." (@493), "[42ne] [74] [65] on..." (@786). Bar: promote iff "[42ne]" takes ONE stated word-class parsing all three windows with the X-slots resolved or fenced; kill iff it contradicts R17-001's 'n'est' legs (@558 '86 94 59 30', @762 '62 94 59 39' — neither 42-preceded) or requires §7 polyvalence on 94 (escalate to the red team; a battery declares no polyvalence).
2. `subj-42-class` (P3) — Name 42's class (n=20; followers: 06 x5, 98 x3, 94 x3, 16 x2, 44 x2; predecessors: 29 x3, 76 x3, 33 x2, 59 x2). Test the '42 06' x5 legs under the ent-06-host-census decision rule (06 is finite "-ent" 3pl iff its left neighbor is a verb stem — is 42 verb-stem-shaped?). A1 grants only the predicative FRAME; the value is open, and the '42 94 X' frame question turns on 42's class. Bar: name 42's class with ≥2 frame-legs; re-state the '42 94 X' frame under the named 42.
3. `est-59-frame-census` (P3) — Harden the control: full census of 59 (n=27). '59 37' x6, '59 32' x3, '59 35' x3 are predicative followers; test the remaining 15 windows. Bar: harden iff ≥80% of 59's windows parse as copular ('est' + predicative/nominal complement) with residuals fenced. This secures the frame's copular arm for future work.

## Adverses

Queue `adverses` field was null. Fenced (not ignored):
- Leftward composition ("[42]ne"): a live alternative parse of '42 94' with a promoted conditional precedent (@508 "[62]ne"); deciding it implicates 94's function and is §7-adjacent → follow-up 1, not decided here.
- 42's own class: '42 06' x5 may be verb-stem-shaped under the 06 decision rule, which would re-frame '42 94' entirely; out of scope → follow-up 2.
- Upstream '30' at @483 (same row a2_11, 10 tokens before the @493 window): belongs to an earlier clause ('30 01' = "pas [01]"); ne-alone-02-74's "no 30 downstream in the row" finding stands undisturbed.
- Row-boundary straddle at @1795–1796 ('42 94 | 59 37'): noted above; normal for '94 59' legs, stream-continuous, not an anomaly.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/subj-42-ne-frame.lock` created on start (no prior lock existed), deleted on completion.
- `battery-queue.json`: `subj-42-ne-frame` → status `verdict`, result `null` (temp-file + rename, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated post-write).
- Report: `code/crowd17/report_inbox/battery-subj-42-ne-frame.md` (this file).
