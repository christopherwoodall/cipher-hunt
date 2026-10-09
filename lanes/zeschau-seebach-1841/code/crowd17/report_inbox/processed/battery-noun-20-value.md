# Battery verdict: noun-20-value — **NULL**

**Target:** `noun-20-value` (priority 2)
**Date:** 2026-10-08 (CDT)
**Worker:** 9162005f-4884-97f1-ebd33d5f2888

## Pre-registered bar (verbatim from battery-queue.json)

> CLAIM: name 20's noun-leg value resolving the determiner/adjective paradox.
> BARS: a feminine noun value for 20 parsing @760 ('la premiere [20] il n'est'), @839 ('vient [20] il ne'), @1703 ('pas [20] il ne') AND surviving the @307 determiner-leg adverse ('88 20 fois que') — or show the paradox resolves via conditioned polyvalence (red-team act; this battery may only state the candidacy, never declare).
> ADVERSES: 20's determiner/adjective leg (@307 'fois que' with det/adj predecessors 91/91) unresolved — paradox stands; 20='fois' KILLED (§7).
> EVIDENCE: battery-frame-20-62-94 null (2026-10-08): three '20 62 94' windows share no uniform noun-leg parse (@1703 'pas 20' selects infinitive); @307 untouched by the battery.

**Numbered clauses:**
- (a1) A feminine noun value for 20 parses @760 under the 62='il' / 94='ne' / 59='est' reading ("la première [20] il n'est [39]").
- (a2) The same value parses @839 ("[56] fois vient [20] il ne [26]").
- (a3) The same value parses @1703 ("[33] ne pas [20] il ne [88]").
- (a4) The same value survives @307 ("88 02 88 [20] fois que on") — the determiner/adjective-leg adverse.
- (b) ALTERNATIVE: the paradox resolves via conditioned polyvalence (candidacy stated only; declaration is a red-team act per §7 sole-polyvalence law).

## Method

Read BATTERY-PROTOCOL.md first; created `locks/noun-20-value.lock` on start. All counts re-derived from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never touched. R5005, sealed gates, and the red-team adjudication queue untouched. Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), banked (17=fois, 30=pas, 59=est provisional, 87=ce, 64=qui), leads (94='ne' STRONG LEAD R17-001, 62='il' battery lead, 98='vient' battery promote). Kill holds honored: 20='fois' (§7).

## Window-level evidence (re-derived, @-offsets on repaired stream)

**20 census: n=15.** Full distribution:
@280 `91 37 61 20 61 42 48` · @307 `91 18 89 88 02 88 20 17 46 84 24 37` ·
@490 `76 42 41 20 67 78 42` · @642 `77 89 48 20 24 87 61` · @668 `62 06 00 20 67 11 86` ·
@703 `60 12 98 20 12 66 21` · @741 `06 00 36 20 30 67 77` ·
@760 `11 70 82 34 29 40 20 62 94 59 39 88` · @839 `76 59 35 56 17 98 20 62 94 26 12 16` ·
@873 `77 89 48 20 74 49 16` · @958 `24 85 04 20 67 96 00` · @1135 `24 77 86 20 62 98 00` ·
@1224 `48 30 09 20 57 64 79` · @1270 `88 24 30 20 64 47 76` · @1703 `23 91 85 33 94 30 20 62 94 88 26 12`

**Structural facts (verified this session):**
1. The "la première" crib (`11 70 82 34 29 40`, all GT) occurs exactly **twice** in the stream: crib@754 → follower **20**@760; crib@1034 → follower **17**@1040 (17='fois' banked). 20 occupies at W1 the exact slot 'fois' occupies at W2 → the W1 slot is nominal.
2. **Exactly one** 20–17 adjacency exists in all 1,847 pairs: **@307** (`88 20 17 46` = "[20] fois que", 46=que GT). Zero 17–20 adjacencies.
3. 20's successor distribution: 62 ×4 (@760, @839, @1135, @1703), 67 ×3, {12, 30, 74, 57, 64, 61} ×1 each, 17 ×1 (@307 only).

## Per-clause results

**(a1) @760 — FAIL (strained at best; fatal in combination with a4).** `11 70 82 34 29 40 20 62 94 59 39 88` = "la première [20] il n'est [39] 88" (62='il' lead, 94='ne' lead, 59='est' provisional). A feminine noun (lettre/dépêche/place…) requires asyndeton — "la première lettre, il n'est [39]…" with "il" = unestablished masculine referent. Grammatically tolerable only with a comma intonation the bytes do not mark. No noun parses *cleanly*.

**(a2) @839 — FAIL.** `76 59 35 56 17 98 20 62 94 26 12 16` = "…56 fois vient [20] il ne [26]…". "vient [noun]" (inverted subject, "vient la lettre") followed by asyndetic "il ne [26]" is doubly strained; no feminine noun yields a natural parse.

**(a3) @1703 — FAIL at kill grade for the noun reading.** `23 91 85 33 94 30 20 62 94 88 26 12` = "…33 ne pas [20] il ne [88]…". "ne pas" selects an infinitive, never a bare noun — **"ne pas [noun]" is ungrammatical in 1841 French**. The noun-leg framing itself breaks here; this window has a verbal flavor ("ne pas [20-62…]") that the bar's gloss does not survive. (Not pursued: re-segmentation is unevidenced and outside this bar.)

**(a4) @307 — FAIL, categorically.** `91 18 89 88 02 88 20 17 46 84 24 37` = "…88 02 88 [20] fois que on…". The fois-battery (2026-10-07, round-14) corpus result stands: 91 bigrams of "X fois que" in 1840–42 diplomatic French, predecessors **exclusively determiners/adjectives** (les, première, chaque, une, dernière, plusieurs, la, deux, cette…), **zero nouns**. "[noun] fois que" is ungrammatical; the tested runner-ups (place, lettre) die here. No re-segmentation rescues it: 20–17 as one word contradicts banked 17='fois' segmentation; "fois que" cannot begin a clause; 88–20 as one word is unevidenced.

**Net of (a):** the @307 slot (determiner/adjective-exclusive) and the @760 slot (nominal, crib-parallel to W2's "la première fois") demand **disjoint grammatical categories**. No monovalent cell satisfies both. 20='fois' kill (§7) holds and is not re-litigated.

**(b) Conditioned-polyvalence candidacy — STATED, not declared.** The distributional condition is real: 20 is followed by 17 ("fois") exactly once (@307, the det/adj window) and by {62, 67, 12, 30, 74, 57, 64, 61} in all 14 other windows. Candidacy: 20 = DET/ADJ value iff follower is 17; 20 = NOUN value otherwise. **Caveats (why this stays a candidacy):** the det/adj leg rests on a single window (n=1 — stipulative, not demonstrated); no French word is independently known to split noun/determiner this way; and the lane dissolved the polyvalence program — 67 et/veut is the sole true polyvalence and any new polyvalence is a **red-team act** per §7. This battery does not declare it.

## Verdict: **NULL**

No feminine noun value for 20 parses @760/@839/@1703 while surviving @307; (a3) actively refutes the noun reading at @1703 and (a4) categorically excludes nouns at @307. The determiner/adjective paradox is confirmed structural on the repaired stream. The conditioned-polyvalence resolution is stated as a candidacy for the red team, not declared. No standing verdict contradicted or downgraded. R5005, sealed gates, and the red-team adjudication queue untouched.

## Follow-ups proposed (null regenerates work)

1. `det-20-value` (P2): name 20's determiner/adjective value at @307 — test the corpus's top "fois que" predecessors (chaque, cette, dernière, plusieurs, une, deux) against 20's full 15-window distribution; a determiner value that also explains @280's 91-adjacency wins.
2. `ellipsis-760` (P2): re-examine W1 (@760) under the ellipsis hypothesis — "la première" nominalized ("the first one"), 20 clause-initial; test 20 as clause-initial particle against @760/@839/@1703 with @307 fenced as the det/adj leg.
3. `poly-20-docket` (P1, red-team venue): escalate the conditioned-polyvalence candidacy (20 = NOUN in "la première __" frames vs DET/ADJ in the unique "__ fois que" frame @307) for adjudication under the §7 sole-polyvalence law (67 et/veut precedent); include the n=1 caveat on the det/adj leg.
