# Battery verdict: det-20-value — **NULL**

**Target:** `det-20-value` (priority 2)
**Date:** 2026-10-08 (CDT)
**Worker:** ef5c0a43-a820-4273-a20f-9328441778cd
**Lock:** `code/crowd17/next-token/locks/det-20-value.lock` created on start (agent id + UTC 2026-10-09T02:48:43Z); no stale lock present.

## Pre-registered bar (verbatim from battery-queue.json)

> CLAIM: name 20's determiner/adjective value at @307.
> BARS: test the corpus's top "fois que" predecessors (chaque, cette, dernière, plusieurs, une, deux) against 20's full 15-window distribution; a determiner value that also explains @280's 91-adjacency wins.
> ADVERSES: 20's det/adj leg (@307) vs the noun legs.
> EVIDENCE: battery-noun-20-value.md follow-up #1.

**Numbered clauses (pre-registered before testing):**
- (c1) Each of the six corpus predecessors {chaque, cette, dernière, plusieurs, une, deux} is tested as 20's monovalent value at @307 (`88 02 88 [20] 17 46 84` = "[preds] [X] fois que on …", 17='fois' banked, 46='que' pencil GT, 84='on' promoted). A candidate passes c1 iff "[X] fois que" is grammatical 1841 French in this frame.
- (c2) Every c1-passing candidate is tested against 20's full 15-window distribution (@280, @307, @490, @642, @668, @703, @741, @760, @839, @873, @958, @1135, @1224, @1270, @1703). A candidate passes c2 iff it yields a grammatical parse in ALL 15 windows — no re-segmentation, no second polyvalence (§7 sole-polyvalence law; 67 et/veut is the only one).
- (c3) Winner rule: the named value is a c1∩c2-passing determiner that additionally parses @280's window (`91 37 61 [20] 61 42 48`, the 91-adjacent window — 91@277 is the only 91 within ±8 of 20@280). If no candidate passes c2, there is no winner: verdict null per §4.

## Method

Read BATTERY-PROTOCOL.md in full first. All counts re-derived from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never touched. R5005, sealed gates, and the red-team adjudication queue untouched. Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); banked/promoted (17=fois, 30=pas, 59=est provisional, 87=ce, 64=qui, 79=tout, 00=pour, 84=on, 47=ce); leads (94='ne' strong, 62='il' battery lead, 98='vient' battery promote). Kills honored: 20='fois' (§7) — not re-litigated. The noun-20-value battery (2026-10-08, NULL) is not re-litigated; this battery names only the det/adj leg.

**20 census re-derived (n=15), verified identical to battery-noun-20-value:**
@280 `91 37 61 20 61 42 48` · @307 `91 18 89 88 02 88 20 17 46 84 24 37` ·
@490 `76 42 41 20 67 78 42` · @642 `77 89 48 20 24 87 61` · @668 `62 06 00 20 67 11 86` ·
@703 `60 12 98 20 12 66 21` · @741 `06 00 36 20 30 67 77` ·
@760 `11 70 82 34 29 40 20 62 94 59 39 88` · @839 `76 59 35 56 17 98 20 62 94 26 12 16` ·
@873 `77 89 48 20 74 49 16` · @958 `24 85 04 20 67 96 00` · @1135 `24 77 86 20 62 98 00` ·
@1224 `48 30 09 20 57 64 79` · @1270 `88 24 30 20 64 47 76` · @1703 `23 91 85 33 94 30 20 62 94 88 26 12`

**91 census re-derived (n=21):** 91 falls within ±8 of a 20-window exactly three times: @277→@280 (dist 3), @301→@307 (dist 6), @1698→@1703 (dist 5). @280's window opens with the 91 (`91 37 61 20 …`); it is the window the bar's "91-adjacency" clause identifies. 91's own value is unnamed (no standing hypothesis); top followers 53/65/32/11/67 give no determiner read.

## Window-level evidence: the six candidates

### (c1) @307 — "[X] fois que" grammaticality

| X | "[X] fois que" @307 | c1 |
|---|---|---|
| chaque | "chaque fois que on …" — canonical ("each time that") | **PASS** |
| une | "une fois que on …" — canonical ("once / when") | **PASS** |
| cette | "cette fois que" — ungrammatical; "cette fois" requires -ci/-là and never takes "que" | FAIL |
| plusieurs | "plusieurs fois que" — ungrammatical; "plusieurs fois" never takes "que" ("les fois que" / "chaque fois que" do) | FAIL |
| deux | "deux fois que" — ungrammatical without article ("les deux fois que") | FAIL |
| dernière | "dernière fois que" — ungrammatical without article; would need 88/02 = article ("[88] [02] [88] dernière fois que"), unevidenced | FAIL |

Note: the round-14 fois corpus attests cette/plusieurs/deux/dernière as "X" in "X fois" bigrams, but as *standalone* values in 20's @307 slot only chaque and une are grammatical. (c1) survivors: **chaque, une**.

### (c2) Full 15-window distribution for the survivors

**20 = "chaque":**
- @280 `91 37 61 chaque 61 42 48` — FAIL. "chaque" is pre-nominal: "61 chaque 61" = "W chaque W" with the same group 61 on both sides; no French W parses ("fois chaque fois" is not a phrase; "chaque" cannot follow its own noun).
- @741 `06 00 36 chaque 30 67 77` — FAIL. "chaque pas" ungrammatical.
- @760 `la premiere chaque 62 94 59` — FAIL at kill grade for the determiner reading. After "la" + "première" only a noun (or nominal ellipsis) can follow; a second determiner is ungrammatical in French.
- @839 `… 98 vient chaque 62 94 …` — FAIL. "vient chaque" needs a noun after "chaque"; follower is 62='il', not a noun.
- @1270 `88 24 30 pas chaque 64 …` — FAIL. "pas chaque" ungrammatical ("pas à chaque fois" needs "à").
- @1703 `… 94 30 pas chaque 62 94 …` — FAIL. "ne pas chaque" ungrammatical.
- @668 `62 06 00 pour chaque 67 11 86` — "pour chaque [67]" possible only if 67 is a singular noun; 67 is et/veut (§7), neither a noun. FAIL.
- Remaining windows (@490, @642, @703, @873, @958, @1135, @1224, @307) do not individually kill "chaque", but the six failures above are fatal.

**20 = "une":**
- @280 `91 37 61 une 61 42 48` — FAIL. Same sandwich: "W une W" ungrammatical for any W.
- @741 `06 00 36 une 30 67 77` — FAIL. "une pas" ungrammatical.
- @760 `la premiere une 62 94 59` — FAIL at kill grade, same as "chaque": no determiner follows "la première".
- @839 `… 98 vient une 62 94 …` — FAIL. "vient une" needs a feminine noun after "une"; follower is 62='il'.
- @1270 `88 24 30 pas une 64 47` — FAIL. "pas une" (= "not one") needs its noun; "pas une qui ce" is broken.
- @1703 `… 94 30 pas une 62 94 …` — FAIL. "ne pas une il ne" broken.
- Remaining windows do not individually kill "une", but the six failures are fatal.

**(c2) result: no candidate passes.** Both c1 survivors die on at least six windows each, including @760 at kill grade (determiner-after-"la-première" is categorically ungrammatical) and @280 (the bar's named window).

### (c3) Winner rule

No c1∩c2-passing candidate exists; the winner rule cannot fire. In particular, **no determiner value explains @280's 91-adjacent window**: the only grammatical @307 values ("chaque", "une") both fail @280's "61 [X] 61" sandwich, and the other four fail @307 outright.

## Per-clause pass/fail

- **(c1) @307 grammaticality — PARTIAL.** "chaque" and "une" pass; "cette", "plusieurs", "deux", "dernière" fail as standalone values.
- **(c2) Full 15-window distribution — FAIL.** "chaque" fails @280/@668/@741/@760/@839/@1270/@1703; "une" fails @280/@741/@760/@839/@1270/@1703. @760 is kill-grade for every determiner candidate.
- **(c3) Winner rule — NO WINNER.** Nothing to name.

## Adverses

**"20's det/adj leg (@307) vs the noun legs" — ANSWERED by fencing, not by resolution.** The det/adj leg is confirmed real and exclusive: @307 is the stream's only 20–17 adjacency ("[20] fois que"), and the fois-corpus result (91 "X fois que" bigrams, predecessors exclusively determiners/adjectives, zero nouns) still stands. But no monovalent determiner value from the corpus inventory covers the other 14 windows — the noun legs (@760 "la premiere __", @839, @1703) demand a disjoint category, exactly as battery-noun-20-value found from the other side. The paradox is therefore structural under monovalence, not an artifact of an untested candidate list. Resolution remains where the pipeline already put it: `poly-20-docket` (P1, red-team venue — conditioned-polyvalence candidacy, n=1 caveat on the det/adj leg) and `ellipsis-760` (P2) are both already queued; neither is re-litigated here. No standing verdict contradicted or downgraded. R5005, sealed gates, and the red-team adjudication queue untouched.

## Verdict: **NULL**

Two corpus predecessors ("chaque", "une") parse @307's "[X] fois que" cleanly, but every one of the six fails 20's full 15-window distribution — @760 ("la premiere [DET]") is kill-grade for all determiner values, and none parses @280's 91-adjacent "61 [X] 61" sandwich. The bar's winner rule cannot fire. The det/adj leg stays fenced at n=1 (@307); the monovalent naming this battery was asked for does not exist on the repaired stream.

## Follow-ups proposed (null regenerates work; none duplicate already-queued targets)

1. `det-20-307-fenced` (P2): name the @307 value with the other 14 windows explicitly OUT of scope. Bar: for X in {chaque, une} (the two c1 survivors), produce a grammatical "[X] fois que on [24]" parse of the full @307 window `91 18 89 88 02 88 20 17 46 84 24 37`, fenced as the n=1 det/adj leg; discriminate "chaque" vs "une" on the @307 continuation (verb agreement/mood at 24/37). If 88/02 get named first (lever-88 line), re-admit {dernière, deux} under explicit article-supply.
2. `61-20-61-frame` (P3): @280 is the unique "61 20 61" sandwich in all 1,847 pairs (only 61–20 and 20–61 adjacencies in the stream) and the window the det-20-value bar named but could not clear. Bar: name 61 (n=18; top followers 96/59/94/21, top predecessors 55/62/89) and test whether ANY determiner/adjective value for 20 parses `91 37 61 [20] 61 42 48`; kill-grade if the sandwich forces 20 non-determiner.
3. `fois-corpus-article-audit` (P3): audit the round-14 fois corpus X-inventory for article-completeness. Bar: for each X in {cette, plusieurs, deux, dernière}, record from the 91 "X fois que" bigrams whether the attestation carries a preceding article (i.e. "[art] X fois que") — settles which corpus predecessors are standalone determiners (admissible at @307's bare slot) vs article-dependent (needing 88/02 to supply the article), and sharpens follow-up #1's candidate set.
