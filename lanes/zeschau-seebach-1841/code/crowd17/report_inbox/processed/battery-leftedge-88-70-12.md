# Battery verdict: leftedge-88-70-12 — name 88's class at the left edge

- Target: `leftedge-88-70-12` (priority 4)
- Claim: "Name 88's class at @1118 ('11 88 70 12 06') now that the 'prennent' reading is dead — closes the left edge of the fenced residual."
- Worker: battery-worker leftedge-88-70-12 (agent b309e85c-2eb5-4b24-8d9f-ba20e1e4b232)
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization; 1,847 pairs / 96 types re-verified in-session). `canonical.py` never used. R5005 untouched. Sealed gates untouched. Red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/leftedge-88-70-12.lock` created on start (no pre-existing lock; nothing stale to note); deleted on completion.

## 1. Bar (pre-registered BEFORE testing)

The queue entry's `bars` field is null, so the bar is constructed from the claim text (fixed before any window analysis; not modified after seeing data):

- C1: 88's class is NAMED at battery grade — a single class parses the locus with standing values and zero ungranted assumptions, is consistent with 88's global profile (no conditioned split, §7 clean), and every rival class is eliminated on closed grounds.
- C2 (else): the class question is FENCED with stated cause.

Offset note: the claim's "@1118" is 1-based. 0-based: @1116=11, **@1117=88**, @1118=70, @1119=12, @1120=06 (row a6_07). The window '11 88 70 12 06' = 0-based @1116–1120. The class target is 0-based @1117.

## 2. Method

Re-derived the repaired stream in-session (1,847 pairs / 96 types verified). Byte-confirmed the locus and 88's full 23-window census. Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 45=ce A4); promoted letters (12=n, 48=e, 06=ent); provisional (59=est, 77=le); red-team R19-108 GRANT (locus-level): "69 11"="cela" at 0-based @1115–1116. Battery-level items cited with status labels, never as standing. 1841 diplomatic French throughout.

## 3. Window-level evidence

**Locus** (0-based, row a6_07): `@1114=30 @1115=69 @1116=11 @1117=88 @1118=70 @1119=12 @1120=06 @1121=14 @1122=06 @1123=11`
= `pas cela [88] pre-n-ent [14]-ent la` (with the R19-108 cela grant; 14='le' killed globally at @1121 by battery-le-14-kill-1121).

**88's census** (n=23, re-derived): @42/@86/@210/@304/@306/@334/@402/@497/@513/@616/@619/@646/@730/@765/@904/@1049/@1117/@1260/@1267/@1514/@1541/@1706/@1727. Verb-shaped legs: @1049 "[88]ere" one word (battery-seg-88er-1049 PROMOTE — finite present stem+"ère" shape, préfère/adhère/suggère); @1706 "62 94 [88] 26 12" = "[88-26]nent" 3pl verb (R20-114 GRANT-WITH-CORRECTIONS); "88 77" x3 (@86/@646/@1541, verb+object-clitic frame). Nominal legs: "79 88" @496 ("tout [88]"), "59 39 88" @765 ("est à [88]"), "45 88" @402 ("ce [88]"). 88's class stands as governor/verb-class (battery-88-prep-rival: "Verb-class stands, now with word-level frame-legs"; registry ["gov","cls"]).

## 4. Class elimination at @1117 (0-based)

Frame under standing values: `pas cela [88] pre-n-ent …` ("cela" granted as one word at @1115–1116, so 88 stands alone after it).

1. **Finite verb — LIVE.** "cela [88-fin]" = subject + finite verb: grammatical French ("cela est", "cela veut"). Zero ungranted assumptions (cela granted R19-108; 88's verb-class standing). Consistent with 88's global verb legs (@1049 finite shape, @1706 3pl, "88 77" x3) — no conditioned split, §7 clean.
2. **Noun — DEAD.** "cela [88-N]" is ungrammatical (demonstrative + bare noun, no apposition). The "la [88]" noun frame is dissolved by the cela grant (11 word-internal); the noun-88-det NULL's class forcing was conditional on that frame. The plural-noun-subject arm is independently killed (battery-noun-88-subject, verdict/kill).
3. **Pronoun — DEAD.** Killed at kill grade (battery-prennent-88-subject: "tout [88]" @496-497 forces 88 ≠ plural pronoun under §7 monovalence).
4. **Infinitive — DEAD.** "cela [88-INF]" ungrammatical (demonstrative subject cannot take a bare infinitive).
5. **Determiner / adjective / adverb / preposition — DEAD.** All ungrammatical after standalone "cela" ("cela [det/adj/adv/prep]" parses in no French frame at battery grade). The determiner frames are independently dead (battery-noun-88-epicene-rescope, verdict/kill: "both determiner frames dead").
6. **Sub-lexical / letter tier — DEAD.** "cela"+"ver" and "ver"+"pre" are non-words; no licensed composition under standing values.

Only the finite-verb class survives. The elimination uses only standing grants (R19-108, registry), battery kills (prennent-88-subject, noun-88-subject, noun-88-epicene-rescope, le-14-kill-1121), and closed French grammar — no open-value load, no invented values.

## 5. Per-clause pass/fail

- C1 (name 88's class at battery grade): **PASS.** 88 = **finite verb (verb-class)** at 0-based @1117 (claim's 1-based @1118). Single class, zero ungranted assumptions, globally consistent with 88's standing verb-class (registry ["gov","cls"]; battery-88-prep-rival "Verb-class stands"). No §7 declaration — this is a locus-level naming consistent with the registered class, not a split.
- C2 (fence arm): moot.

## 6. Verdict: PROMOTE

88's class at @1117 is **finite verb**. This closes the left edge of the fenced residual: with (a) the cela grant dissolving "la [88]", (b) the pronoun arm killed, (c) the plural-noun-subject arm killed, and (d) both determiner frames killed, the left edge resolves to `pas cela [88-fin] …`. The residual's right edge ("pre-n-ent [14]-ent la …") stays fenced — out of this bar's scope. No value named for 88 (value stays open); no standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact.

## 7. Scope

Locus-level class naming only (0-based @1117). Untouched: 88's open value, the 'ver' LEAD deferral (78, not 88), the fenced right-edge residual, the cela grant's locus scope, all standing/red-team verdicts. Canonical-stream caveat stands (row a6_07 offsets unvalidated).

No follow-ups required (promote, not null).

## 8. Bookkeeping

- Report: `code/crowd17/report_inbox/battery-leftedge-88-70-12.md`
- Queue: `leftedge-88-70-12` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.leftedge-88-70-12.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/leftedge-88-70-12.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
