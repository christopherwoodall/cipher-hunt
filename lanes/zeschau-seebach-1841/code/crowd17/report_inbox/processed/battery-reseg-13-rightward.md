# Battery verdict: reseg-13-rightward

- Target: `reseg-13-rightward` (battery-queue.json, priority 3, status queued)
- Claim: test rightward attachment of 13 at @481/@575/@1166 ('pour [13-52]', 'ce [13-55]').
- Worker: 4b4b9a01-8ccb-4c04-aaaf-022c1327b378. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/reseg-13-rightward.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"name the rightward attachment with standing values and zero new assumptions at >=2 windows; else fence rightward-13 at those loci"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name arm):** name the rightward attachment (the French word or word-part "13-52" / "13-55") at >=2 of the three windows using standing values and zero new assumptions.
2. **C2 (fence arm):** if C1 cannot be met, fence rightward-13 at the three loci.

Standing values used (per protocol §7): pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour A9, 84=on A15, 47=ce A4); provisional (59=est, 77=le); 45=ce (A11). Kills: 13='les' object pronoun killed at kill grade (pronoun-13-les); 13='que' §7-blocked (46='que' banked); 62='il' killed at kill grade (R19-106, R20-125).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed the three loci.
3. Tested whether any rightward attachment can be stated with standing values alone.

## Window-level evidence (byte-confirmed, in-session)

- **@481 (row a2_11):** `[477]74 [478]45 [479]93 [480]00 [481]13 [482]52 [483]30 [484]01 [485]19` — "…[45] [93] pour [13] [52] [30]…". 00=pour (A9 preposition) is the left neighbor; 13 at @481; 52 at @482.
- **@575 (row a3_02):** `[571]52 [572]87 [573]78 [574]45 [575]13 [576]55 [577]61 [578]94 [579]82` — "…[87] [78] ce [13] [55] [61]…". 45=ce (A11 determiner) is the left neighbor; 13 at @575; 55 at @576.
- **@1166 (row a6_09):** `[1162]21 [1163]67 [1164]78 [1165]45 [1166]13 [1167]55 [1168]61 [1169]94 [1170]87` — "…[21] [67] [78] ce [13] [55] [61]…". 45=ce is the left neighbor; 13 at @1166; 55 at @1167.

The parent battery (reseg-13-armB, KILL, 2026-10-09) killed the LEFTWARD account (13 as suffix of a preceding nominal) at these three windows: a preposition (00) and a determiner (45) cannot host a nominal suffix. The remaining options per window are: (a) 13 attaches rightward to 52/55 ("[13-52]", "[13-55]" as word-internal prefix/syllable or part of a word unit); (b) 13 stands alone as a word between "pour"/"ce" and the following cell; (c) some other segmentation.

## Clause results

- **C1: FAIL (deterministic, not value-specific).** Naming the attachment means stating a French word or word-part for "13-52" / "13-55" with standing values and zero new assumptions. The inventory of standing 13-content is empty: 13='les' is killed at kill grade (pronoun-13-les), 13='que' is §7-blocked (46='que' banked), and the adverses record 13's gloss as open with 52/55 class-open. Every concrete French candidate requires naming 13's letter content AND 52's or 55's content — each a new assumption, and the bar allows zero. Even the class-tier route ("13 as prefix-syllable of a nominal 52/55") needs 52/55 nominal, which is ungranted. No window admits a named attachment; the structural blocker is identical at all three.
- **Adverses answered:** 52/55 class-open confirmed against the report archive — the only standing-adjacent hypotheses (52="pas" in negation frames, 55="re", 52="a" as a letter in the "52 82 94" word-unit) are battery-grade, locus-scoped, and none is standing at red-team level; none transfers to these windows without new assumptions. 13's gloss open confirmed (kills above). The leftward account's kill (reseg-13-armB) is adopted, not re-litigated.
- **C2: FIRES.** Rightward-13 is fenced at @481, @575, and @1166: the attachment cannot be named with standing values, so it cannot be established at battery grade.

## Verdict: NULL (fence executed)

The three loci are now double-fenced: leftward attachment killed by the parent (reseg-13-armB), rightward attachment unfenceable-until-named by this battery. Neither kill nor naming is forced — the fence records the state, not a refutation. No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-13-letter` (P3) — census 13's 12 windows for a uniform letter value with byte evidence; a named letter-13 re-opens the rightward attachment at all three loci (removes 1 of the 2 missing assumptions).
2. `val-52-55-class` (P3) — test 52/55 class at @482/@576/@1167 specifically (nominal vs letter vs stem); a granted nominal-52/55 plus a named letter-13 unlocks C1.
3. `standalone-13-481` (P4) — test 13 as a standalone word between "pour"/"ce" and the following cell (e.g. particle reading); name with standing values or fence the standalone arm.

## Bookkeeping

- `battery-queue.json`: `reseg-13-rightward` queued → verdict/null (temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated; no downgrade).
- Lock `locks/reseg-13-rightward.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
