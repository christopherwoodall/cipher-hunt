# Battery verdict: objpron-77-89 — **KILL** (object-pronoun-77 closes at battery grade)

- Target: `objpron-77-89` (battery-queue.json, priority 3, status queued)
- Claim: "discriminating clitic frame for 77 at the two '77 89' windows; fail -> object-pronoun-77 closes at battery grade"
- Evidence lineage: follow-up #1 of the NULL verdict on `val-77-722-det` (battery-val-77-722-det.md, processed)
- Worker: agent 8392d92b (session 46ccea03-5adc-43fe-822f-75f84b1e0759). Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held in-session: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gate instances, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/objpron-77-89.lock` created on start (no prior/stale lock present); deleted on completion.

## Bar (verbatim, pre-registered from the task brief)

"Discriminate the clitic frame with byte evidence at battery grade; close object-pronoun-77 if no discriminating frame exists."

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (PROMOTE clitic-77):** name clitic-77 iff BOTH '77 89' windows (@639, @870) parse as [object-pronoun 77] + [verb 89], with 89's verb reading held at both windows, and no determiner or word-internal rival surviving at either window; every listed adverse answered.
2. **C2 (CLOSE):** if C1 fails — no discriminating clitic frame exists at battery grade — object-pronoun-77 closes at battery grade (KILL; red-team ratification required like all battery verdicts).

Standing values used (protocol §7 + ratified rounds): pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 47=ce, 84=on, 00=pour); provisional (77="le", 59=est); 67 et/veut sole polyvalence with positional rule; **R19-161: 89=noun LEAD ratified, infinitive/verb rival KILLED globally**; R20-130: finite-89 unlicensed; R20-131: the three "ce"+77 windows (@515/@611/@869) fenced as 77-value residuals, 77="le" provisional survives; R20-092: "le [89]e" NP at @639–642 GRANTed agreement-admissible.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session (asserts held). Located both '77 89' windows and re-derived 89's census (n=14) independently.
3. Tested C1 against standing red-team rulings and prior battery verdicts on these exact windows — no prior counts trusted without re-derivation of the loci.

## Window-level evidence (re-derived, byte-exact)

- **@639** (row a4_01): @633–645 = `67 63 74 46 60 67 | 77 89 | 48 20 | 24 87 61`. Predecessor @638=67: "et" (67="veut" iff follower infinitive-shaped; 77 is not infinitive-shaped → "et"). Followers: @641=48, @642=20.
- **@870** (row a5_07): @864–876 = `47 46 00 86 70 87 | 77 89 | 48 20 | 74 49 16`. Predecessor @869=87 ("ce", granted).
- **'77 89 48 20' tetrogram x2**, byte-identical at @639 and @870 — the only two occurrences. '89 48 20' occurs exactly twice stream-wide, both at @640 and @871, i.e. only ever preceded by 77.
- n(89)=14 re-derived: positions [113, 222, 275, 285, 303, 640, 781, 871, 986, 1082, 1377, 1393, 1498, 1752].

## Clause results

- **C1 at @639: FAIL.** 89's verb reading is not held — it is unavailable: R19-161 ratified **89=noun LEAD** and **KILLED the infinitive/verb rival globally**; R20-130 confirms finite-89 is unlicensed. The clitic parse "et le [89-verb]" therefore cannot be constructed at battery grade. Worse for C1, a determiner rival stands on the same bytes with red-team backing: `subj-20-642` PROMOTE (battery-grade) reads @639–641 = "77 89 48" as a **closed NP "le [89]e" with noun forced (arm A)**, and R20-092 GRANTed the "le [89]e" NP agreement-admissible, explicitly strengthened by R19-161's 89=noun LEAD. A granted rival geometry on identical bytes defeats "discriminating".
- **C1 at @870: FAIL at kill grade.** The clitic parse "87(ce) 77(le) 89(verb)" was already demonstrated **ungrammatical at battery grade**: `battery-ce-le-verb-frame` NULL tested "ce le [verb]" as clitic stack and failed it with 1841 period evidence (Littré: demonstrative "ce" cannot head a lexical verb and cannot stack with object clitic "le" before any verb — "both windows ungrammatical as parsed"). R20-131 FENCEs @869 as a 77-value residual. 89=noun LEAD (R19-161) independently blocks the verb reading. The window forces the clitic parse false.
- **C2: FIRES.** No discriminating clitic frame exists at battery grade: the two '77 89' windows — the strongest clitic-compatible legs on record (parent battery val-77-722-det) — both reject the [clitic le]+[verb] parse, one at kill grade.

## Adverses

- **Byte-identical '77 89 48 20' x2 (formulaic repetition):** answered — the repetition is consistent with the NP reading ("le [89]e [20-adj]" per subj-20-642 PROMOTE) and does not discriminate for the clitic parse; repetition of a frame is not evidence of its geometry.
- **A8 "80/89 verb-frames" frame grant:** NOT overturned. R20-084 confirms it as frame-level (not a split), conditional on 77='le' provisional. The bar required 89's verb reading HELD at these windows; the later ratified 89=noun LEAD (R19-161, verb rival killed globally) governs the window reading. No contradiction created.
- **Determiner rival at @870 ("*ce le [noun]"):** also ungrammatical per ce-le-verb-frame candidate 2 — but that failure does not rescue the clitic parse; the window stays fenced (R20-131).
- **Word-internal rivals ("87 77" = "ceci"/"celle" fusions):** tested and failed/fenced elsewhere (ce-le-verb-frame candidates 5, 7; R20-130 FENCE; celle-7780-fusion-515-869 KILL). No letter-tier hypothesis for 89 exists on record. Answered.
- **'l'on' x7 (A15):** settled alternative geometry for 77, untouched by this battery; not present at these windows.
- **Provisional 77="le" value:** untouched. R20-131 keeps 77=["le","prov"]. This close is geometry-level (object-pronoun), not value-level.
- **§5.2 contradiction check:** no standing red-team verdict grants clitic/object-pronoun-77 geometry. The KILL is recorded at battery grade; red-team ratification required.

## Verdict: KILL (battery grade)

Object-pronoun-77 closes at battery grade. The two '77 89' windows — the strongest clitic-compatible legs for 77 on record — cannot supply a discriminating clitic frame: @870 rejects the clitic parse at kill grade (ungrammatical, fenced residual), and @639's clitic parse is blocked by ratified 89=noun LEAD with a granted determiner-NP rival standing on the same bytes.

## Scope

This close is scoped to the '77 89' legs and the object-pronoun geometry claim. It does not touch: 77="le" provisional (value); the 'l'on' x7 grant (A15); the '77 86' x5 "le + nominalized infinitive" legs, which are clitic-compatible but outside this battery's scope — their venue is the queued `det-77-86-substantivized` follow-up (parent NULL follow-up #2). If the red team declines to ratify, the close lapses to a fence at @639/@870.

## Bookkeeping

- `battery-queue.json`: `objpron-77-89` queued → verdict/kill (temp-file + rename, own entry only; pre-write assert confirmed status "queued" with no prior verdict; JSON re-validated from disk; no downgrade; no other entries touched).
- Lock `locks/objpron-77-89.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched. No invented data.
