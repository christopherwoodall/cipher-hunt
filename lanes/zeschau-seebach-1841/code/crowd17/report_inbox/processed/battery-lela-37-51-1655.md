# Battery report: lela-37-51-1655 (PROMOTE — both windows fenced as genuine S5-straining residuals; S5 not decided)

**Target:** lela-37-51-1655 — the two "37-11" windows parse or fence under standing values
**Worker:** fd20b036-9a36-434f-b602-e37cf9549e57 | **Date:** 2026-10-08
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; asserts 1847 pairs / 96 unique re-verified). Never canonical.py. No R5005 touched. No data invented. Every @-offset re-derived from the stream, not taken on trust.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

> each window parses under standing values with <=1 non-granted assumption, or is confirmed as a genuine S5-straining residual with stated cause; clause-boundary readings must name the boundary trigger

## Bar as numbered clauses (fixed before testing)

1. Window @51 ("79-37-11-79-85"): parses under standing values with <=1 non-granted assumption, OR is confirmed as a genuine S5-straining residual with stated cause. Any clause-boundary reading must name its boundary trigger.
2. Window @1655 ("56-37-11-24"): same disjunction, same trigger requirement.

## Method

1. Re-derived 37-11 by exact bigram scan of the repaired stream: exactly x2, @51 and @1655. No other occurrences.
2. Window 1 re-derived: @50–54 = 79-37-11-79-85, row a1_01 (byte-exact). Wider @41–61: `24 88 43 81 30 62 96 00 92 79 37 11 79 85 58 35 53 12 41 08 34`.
3. Window 2 re-derived: @1654–58 = 56-37-11-24-48, row a8_04 (byte-exact). Wider @1645–65: `03 64 31 10 03 38 82 16 01 56 37 11 24 48 47 98 98 80 22 94 84`.
4. Standing anchors used: banked 11=la, 34=i, 82=m; promoted 79="tout" (A5), 96="par", 64="qui", 47="ce" (A4); S5 fence 37="le" (MEDIUM, round-7) taken as the standing value under test — NOT decided here.
5. Compound check: 87-11="cela" is the only granted *-11 compound (n=7); 88-11 (n=2) / 89-11 (n=1) untested per ne-24-profile; no granted compound dissolves 37-11.
6. Hapax check: 79-37 n=1, 11-79 n=1 stream-wide (window-1's 5-gram is hapax — no recurrent standing construction is being misread). Other 56-37 @795 = "56-37-44-77", not 37-11 — no confound.
7. Boundary-rescue sweep: every inter-token seam in/around both windows tested for a named-trigger clause-boundary parse (triggers must be standing: "pour"-infinitive, "ce"-opener per ne-24's 24->87 x10 mechanism, etc.).
8. Cross-checked against standing batteries: s5-foundation (r1) and s5-foundation-r2 (both 2026-10-08, both verdict null, both escalated to red team) already confirmed these exact windows ungrammatical under 37="le"; ne-24-profile (verdict recorded) classes 24 as finite verb, infinitive-taking, and fences @1657's "11-24" with "'la' as previous clause's object pronoun available". Nothing below contradicts any standing verdict.

## Window-level evidence

### Clause 1 — @51 (row a1_01): `92 79 37 11 79 85`

Under standing values (79="tout" A5, 11="la" banked, 37="le" per S5): `…[92] tout le la tout [85]`.

**Parse attempt (disjunct 1):** the 37-11 boundary is article+article ("le la"). French has no article-article parse. Exhausting the seams:
- Boundary between @51 and @52: no token exists at the seam to serve as a trigger (the bar requires a NAMED trigger); the fragments would be "…[92] tout le" (tout+article with no noun — incomplete NP) and "la tout [85]" (article+"tout" in non-adjectival order; "tout"-as-noun is masculine "le tout"; "tout"+infinitive needs a subject/modal). Ungrammatical on both sides, trigger unnamed — fails the bar twice over.
- Boundary between @50 and @51: right fragment "le la tout [85]" still article-article. Dead.
- Boundary between @52 and @53: left fragment "…tout le la" still article-article. Dead.
- Boundary before @50 / after @54: the 5-gram stays intact. Dead.
- "pour" @48 as infinitive-clause opener: "par pour [92] tout le la tout [85]" keeps "le la" inside the pour-clause; the trigger does not touch the 37-11 adjacency. Dead.
- 92's value (open, "pour 92" x6) cannot repair the boundary: whether 92 is verb or noun, the violation sits two tokens right at 37-11. 85's value (open, verb-stem frame A3) sits two tokens right of 11 and cannot repair an article-article adjacency upstream of it.
- Word-internal rescue: would need 79 or 11 sub-lexical; 79="tout" is granted as a full word (A5) and 11="la" is banked — no standing word-internal role for either here (contrast 87-11="cela", the granted dissolution model, which does not apply to 37-11).

Disjunct 1 fails: no parse under standing values with <=1 non-granted assumption. Every rescue needs >=2 non-granted assumptions, contradicts a granted/banked value, or invokes an unnamed trigger.

**Fence (disjunct 2): confirmed as a genuine S5-straining residual.** Stated cause: under the standing S5 value (37="le"), the window presents "tout le la tout [85]" — an article-article adjacency at the 37-11 boundary with no grammatical rescue under standing values: "tout le" requires a following noun (the next token is banked article "la", not a noun), and no named-trigger clause boundary anywhere in the window removes the adjacency (enumerated above). The residual is genuine, not an artifact: byte-exact on the repaired stream, hapax frame (79-37 n=1, 11-79 n=1), no granted compound dissolves 37-11, and the flanking material (79="tout", 11="la") is independently clean — the strain localizes exactly to 37's slot. **Clause 1: PASS via the bar's fence disjunct.**

### Clause 2 — @1655 (row a8_04): `56 37 11 24 48 47`

Under standing values (11="la" banked, 47="ce" A4, 37="le" per S5): `[56] le la [24] [48] ce`.

**Parse attempt (disjunct 1):**
- Under the article reading of "la": "le la" is article-article. Dead (same as clause 1).
- Under ne-24-profile's class finding (24 = finite verb, infinitive-taking): "11-24" = "la"+finite verb forces "la" into its object-pronoun role ("[subject] la [verb]" — clean). Then 37="le" before "la" has no grammatical slot: not a subject ("le" is never a subject pronoun), not an article (no noun follows — "la" is pronominal here), not a second object pronoun ("le la" double direct object is impossible). Dead.
- So the residual is robust under BOTH readings of 24 — it does not depend on ne-24's standing, and ne-24's own fence of @1657 ("'la' as previous clause's object pronoun is available") is consistent with this.
- Boundary sweep with named triggers: the only standing trigger candidate is 47="ce" @1659 (clause opener per ne-24's 24->87 x10 mechanism: 24 clause-final, "ce" opens the next clause). Boundary after @1658: clause 1 = "[56] le la [24] [48]" — the "le la" adjacency sits inside clause 1, unrescued. Dead.
- Boundary between @1655 and @1656: no trigger token at the seam; left fragment "[56] le" would need 56=imperative verb (non-granted #1 — "verb-le" postverbal pronoun is imperative-only) and right fragment "la [24] [48]" would need a subject (non-granted #2; French is not pro-drop) — 2 non-granted assumptions plus an unnamed trigger. Fails the bar.
- Boundary between @1654 and @1655: right fragment "le la [24]…" still article-article. Dead.
- 56's value (open; n=23; pre 86 x4 / suc 87 x2, 47 x2, 37 x2): enumerated — as subject, noun, or verb, 56 cannot repair the 37-11 adjacency to its right ("[56-subject] le la" still strands "le la"; "[56-verb] le la" still article-article). 56 is inert to the violation.

Disjunct 1 fails: no parse under standing values with <=1 non-granted assumption.

**Fence (disjunct 2): confirmed as a genuine S5-straining residual.** Stated cause: under S5 (37="le"), "56-le-la-[24]" presents an article-article adjacency at the 37-11 boundary that survives every named-trigger clause boundary (the only standing trigger, "ce" @1659, places the boundary downstream of the adjacency) and survives both readings of 24 (article+noun and ne-24's pronoun+verb — under the latter, "le" occupies an impossible slot between the putative subject zone and the object pronoun "la"). Genuine, not artifact: byte-exact re-derivation, 37-11 exactly x2 stream-wide, no granted compound dissolves it, strain localized to 37's slot. **Clause 2: PASS via the bar's fence disjunct.**

### Kill-grade check

- No window forces the claim false: both windows satisfy the bar's fence disjunct with stated cause.
- No cleaner rival value demonstrated on these frames at battery level: the la-finder's adjective vote does not parse them cleanly either ("tout [37-adj] la tout [85]" still strands "la tout [85]"; "[56] [37-adj] la [24]" is ungrammatical). The rival search is owned by queued s5-rival-five-windows — not preempted here.
- Not kill.

## Per-clause pass/fail

1. **Window @51 — PASS** (fence disjunct: genuine S5-straining residual, stated cause; no parse under standing values with <=1 non-granted assumption; all boundary rescues enumerated, none with a named trigger).
2. **Window @1655 — PASS** (fence disjunct: genuine S5-straining residual, stated cause; robust under both readings of 24; 56 inert; named-trigger boundaries enumerated, none rescue the 37-11 adjacency).

## Adverses answered

- **S5 standing fence (37="le" MEDIUM, round-7) — NOT decided at battery level.** Both windows are fenced as residuals with stated cause; the fence itself is untouched. This is consistent with s5-foundation (r1) and s5-foundation-r2, which already confirmed these exact windows as S5-contradicting evidence (both verdict null) and escalated to the red team — no standing verdict is contradicted or overwritten here.
- **Feed s5-foundation:** these two windows are confirmed data for s5-foundation / s5-foundation-r2 and for queued s5-rival-five-windows (the designated rival-search venue). No duplicate target proposed.
- **56/85 values open:** answered — the analysis does not depend on either. Window 1's violation is at the 37-11 boundary, two tokens left of 85 and unreachable by it; window 2's 56 was enumerated as subject/noun/verb and is inert to the adjacency (shown above). Both windows fence with zero assumptions about 56 or 85.

## Verdict: PROMOTE

Both bar clauses pass via the bar's explicit fence disjunct (each window confirmed as a genuine S5-straining residual with stated cause; clause-boundary readings held to the named-trigger requirement and found wanting), and all three adverses are answered. This promotes the WINDOW-DISPOSITION claim only: the two "37-11" windows are fenced, not parsed. **No cipher value is promoted, no value is killed, and S5 (37="le") is not decided here** — the S5 question remains with the red team via the r1/r2 escalations. No new follow-up targets are needed: the windows are fenced and fed to already-queued s5-rival-five-windows.

---
Lock: locks/lela-37-51-1655.lock created 2026-10-09T01:20:34Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No red-team verdicts modified. No other queue entry touched.
