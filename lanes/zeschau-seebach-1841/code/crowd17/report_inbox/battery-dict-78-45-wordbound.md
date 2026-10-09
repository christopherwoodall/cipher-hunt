# Battery report: dict-78-45-wordbound

- Target: `dict-78-45-wordbound` (priority 2, status queued)
- Claim: 78-45 is one word ('verdict') iff the boundary holds
- Worker: da68f154-8e9e-4e6f-ba8b-a5f32ff734c3
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005, sealed gates, and the red-team queue untouched.
- Prior work read and built on (not duplicated): `report_inbox/processed/battery-fork-78-45-adjudication.md` (null; follow-up #2 = this target) and `code/crowd17/report_inbox/processed/battery-dict-45-contact-update.md` (PROMOTE verdict, contact-profile boundary, Fisher p=0.002).

## Bar (verbatim, pre-registered)

"(a) decide by contact profile: 45's post-78 followers {64, 13, 01} plus byte-identical 78-45-13-55-61 x2 vs standalone-45 followers {93x3, 23x3, 28x2, 64x2, 91, 54, 88, 46, 94}; (b) adjudicate W1's shared 45-64 follower adverse - if the boundary holds at W2-W4 but W1 parses two-word, record W1 as exception with stated cause"

## Bar restated as numbered pass/fail clauses (frozen before testing)

1. Clause (a) — decide by contact profile: 45's post-78 followers equal {64, 13, 01}, the 5-gram 78-45-13-55-61 occurs exactly twice and is byte-identical, and the standalone-45 follower set matches the bar's stated set; the boundary is decided on the comparison.
2. Clause (b) — adjudicate W1's shared 45-64 follower: IF the boundary holds at W2-W4 AND W1 parses two-word, THEN record W1 as an exception with stated cause (do not silently demote it and do not silently promote it).

## Method

Re-derived the full 45 census on the repaired stream (no values assumed for 78 or 45; only token adjacency). Split all 22 occurrences of 45 by predecessor = 78 vs predecessor != 78. Re-checked the 5-gram loci, the 45-64 windows, and W1's wider context (305-322). Checked 13/01's global predecessors and whether 13-55-61 occurs anywhere else. Compared every count against the bar's stated sets before judging.

## Window-level evidence (@-offsets are pair indices in the repaired stream)

- 78-45 bigrams: 78@313, 78@573, 78@982, 78@1164 (45@314, @574, @983, @1165). Count = 4.
- Post-78 45 followers: @314 -> 64; @574 -> 13 (575=55, 576=61); @983 -> 01; @1165 -> 13 (1166=55, 1167=61). Set = {64, 13, 01} exactly as the bar states.
- 5-gram 78-45-13-55-61: x2, at 78@573 and 78@1164, byte-identical (both rows a3_02 / a6_09 verified; both continue 94 after 61). 13-55-61 occurs NOWHERE else in the stream (global scan: zero).
- Standalone 45 (n=18): followers = {93x3 (@262, @478, @603), 23x3 (@678, @1055, @1551), 28x2 (@104, @697), 64x2 (@340, @1024), 91 (@14), 54 (@332), 88 (@401), 46 (@437), 94 (@569), 08 (@974), 58 (@1201), 36 (@1214)}.
- 45-64 windows: @314 (pre=78, W1), @340 (pre=14), @1024 (pre=64) — re-derived.
- Discriminating core: {13, 01} follow 45 ONLY post-78 (3/3 vs 0/18 standalone). 13 has 10/12 non-45 predecessors globally (65x3, 69x2, 00, 97, 95, 35, 99); 01 has n=28 with 22 distinct predecessors — both are ordinary tokens globally; the exclusivity is 45-specific.
- W1 wide context (@305-322, row a2_04): `02 88 | 20 17 46 84 24 37 | 78 45 | 64 59 32 94 06 11 92 60`.

## Finding (pre-test data check)

The bar's stated standalone follower set sums to 15, not 18. The bar missed three standalone-45 windows: @974 (follower 08), @1201 (follower 58), @1214 (follower 36). The bar's set is a confirmed subset of the true set; the missed followers all occur standalone, never post-78, so the boundary decision is unaffected. Recorded as a stale-census caveat, not a bar rewrite.

## Per-window parses under the boundary claim

- W1 @313 (`84 24 37 | 78 45 | 64 59 32`): two-word parse — "...on [24] [37] ce qui est [32]..." (45='ce', 64='qui' promoted, 59='est' provisional, 32 predicative granted A1) — clean. One-word parse — "...[37] verdict qui est [32]..." — also clean (78='ver' is LEAD only, so the value arm is unsettled). W1 is AMBIGUOUS; its follower 64 is profile-neutral (shared with standalone @340/@1024; 64='qui' promoted, 3/22 = highest-frequency function word in 45's contact set). The contact profile is silent on W1.
- W2 @573 (`...87 | 78 45 | 13 55 61 94 82 06 06...`): one-word — "ce verdict [13-55-61] ne m'[06][06]..." (94='ne', 82='m' banked; elision frame x4 per A7-L2) — clean. Two-word — "ce [78] ce [13-55-61]..." — strained (78 unvalued). Favors the boundary.
- W3 @982 (`...47 | 78 45 | 01 24 89 48 01...`): one-word — "ce verdict [01]..." — clean. Two-word — "ce [78] ce [01]..." — strained. Favors the boundary.
- W4 @1164 (`...67 | 78 45 | 13 55 61 94 87 83...`): one-word — "et verdict [13-55-61] ne ce [83]..." (67='et', follower not infinitive-shaped) — clean given the boundary. Two-word needs 78 noun-valued without the boundary. Favors the boundary.

## Per-clause pass/fail

1. Clause (a): PASS. The contact profile decides: post-78 followers {13x2, 64, 01} = the bar's {64, 13, 01} exactly; the 5-gram occurs x2, byte-identical, at 78@573/78@1164; the standalone set is confirmed (bar's subset + {08, 58, 36} stale-census finding); the discriminating core {13, 01} is 3/3 exclusive to post-78 vs 0/18 standalone. The sister contact-update battery PROMOTED this boundary (Fisher p=0.002, ver-78-independent). The boundary holds.
2. Clause (b): PASS. The boundary holds at W2-W4 (exclusive {13, 01} followers + byte-identical 5-gram x2, both with clean one-word parses). W1 parses two-word cleanly ('ce qui est [32]') and also one-word; its follower 64 is shared and profile-neutral, so the contact profile cannot decide W1. Per the bar's conditional, W1 is recorded as an EXCEPTION with stated cause: at W1, 45-64 reads as two words ('ce qui'), because (i) 64 is shared with standalone 45-64 @340/@1024 and carries no boundary signal, (ii) the boundary's discriminating followers {13, 01} are absent at W1, and (iii) W1's 45-64-59-32 is the A11 mirror leg whose two-word parse is fully grammatical under standing values.

## Adverses answered

- "W1's 45-64-59-32 = A11 mirror leg shared with @340/@1024; demoting it costs A11 one leg" — ANSWERED by fencing, not demoting: the W1 exception keeps @314 as 'ce qui' (two-word), so A11 retains all three mirror legs (@314, @340, @1024). No demotion occurs. The boundary applies at W2-W4 only.
- 64-sharing across classes — ANSWERED: re-derived and fenced as profile-neutral filler (64='qui' promoted; 3/22), consistent with the contact-update verdict. It does not break the boundary because the load-bearing signal is {13, 01} exclusivity plus the 5-gram, not 64.

## Verdict: null

Headline: the boundary holds at W2-W4 with W1 fenced as a two-word exception, but the claim cannot promote — the value arm ('verdict') and the positional declaration both need red-team action, so this escalates.

Why not promote, although both clauses pass:

1. The claim names the word 'verdict'. That value arm is unsettled: ver-78 returned null (2026-10-08); red-team R16-005 graded 78='ver' LEAD, not settled, with @296 a red-team-fenced residual. Promoting 78-45='verdict' would jump ahead of R16-005's grading. Per protocol §5, a result contradicting a standing red-team grading is marked null and escalated.
2. Adopting "78-45 is one word at W2-W4, two words at W1 and the other 18 windows" is a positional assignment for 45. Protocol §7 names 67 et/veut as the sole true polyvalence; positional rules are red-team declarations only. The fork battery already escalated the equivalent positional rule (R-pos) without adopting it. This battery does not declare it either.
3. The value-arm and declaration blockers are independent: even with the boundary promoted (it is, by the sister battery), the word-level claim 'verdict' waits on ver-78, and the positional form waits on the red team.

Not kill: no window forces the claim false. W1's ambiguity is fenced as a stated exception, not a contradiction. The boundary's contact profile (promoted, ver-78-independent) survives at W2-W4.

Escalation for the red team: (i) declare or reject the positional reading of 45 (one word after 78, 'ce' elsewhere); (ii) when ver-78 resolves, confirm whether the W2-W4 boundary reads 'verdict' and whether W1's two-word exception survives.

## Follow-up targets (null regenerates work)

1. verdict78-gate-wordbound (priority 1). Claim: re-test this bar once ver-78 resolves. Bars: (a) if 78='ver' promotes, check whether the W2-W4 one-word reads become 'verdict' and whether W1's two-word exception stands or flips (record A11 @314's fate explicitly); (b) if ver-78 kills, the 'verdict' value arm dies — record the boundary as an unvalued word-unit. Evidence: this report (per-window parses, 5-gram loci @573/@1164, W1 exception). Adverses: R16-005 LEAD grading; A11 HOLD; fork-78-45-rerun already verdict/null (that one covers 45='ce' kill scope — coordinate, do not duplicate).
2. unit-13-55-61-contact (priority 2). Claim: 13-55-61 is a real unit riding the boundary, not a coincidence. Bars: census all 13, 55, 61 contacts on the repaired stream; the unit is real iff 55-61 binds to 13 more tightly than chance (55-61 after non-13 tokens) and the 5-gram tail parses with the unit named. Evidence: 13-55-61 occurs nowhere else globally (verified); 13 has 10/12 non-45 predecessors; the 5-gram is byte-identical x2 at 78@573/@1164. Adverses: dict-frame-78-45-13-55-61 returned null on the unit-naming bar — build on its two clean windows, do not re-run them.
3. boundary-45-exclusivity-sensitivity (priority 3). Claim: the {13, 01}-exclusivity survives leave-one-out. Bars: recompute the Fisher table dropping each post-78 window in turn (contact-update's one-window-sensitivity caveat); the boundary is robust iff exclusivity holds (p<0.05) in all four leave-one-out tables; also test 13/01 against other word-final positions to rule out a global frequency artifact. Evidence: n=4 post-78 (contact-update census); 01 is globally common (n=28, 22 distinct predecessors); 13 is n=12. Adverses: small-n caveat stated, not ignored.

## Non-duplication note

w1-314-ambig is queued (fork battery follow-up #3) — its 37-78 left-context test was not re-run here. The 5-gram windows were used only as positional confirmation of the stated counts; dict-frame-78-45-13-55-61's unit-naming bar was not re-run.
