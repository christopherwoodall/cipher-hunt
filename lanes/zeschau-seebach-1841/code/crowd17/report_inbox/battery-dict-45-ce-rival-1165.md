# Battery report: dict-45-ce-rival-1165

Target: `dict-45-ce-rival-1165`. Claim: W4 @1164-1165 re-reads under 45='ce' HOLD as two-token parse.
Date: 2026-10-08. Worker: a28e410d-55c0-474f-a37c-4d142c9a218f (battery worker).
Lock `code/crowd17/next-token/locks/dict-45-ce-rival-1165.lock` created 2026-10-09T00:57:27Z (no pre-existing lock); deleted on completion.

## Bar (verbatim, pre-registered from battery-queue.json)

> produce the best 'ce' parse with <=1 non-granted assumption, or record W4 as double-residual (ungrammatical under both two-token readings); feeds the red-team polyvalence decision

Numbered clauses (frozen before testing):

1. Produce the best two-token parse of W4 (`21 67 78 45 13 55 61`, stream @1162-1168, row a6_09) under 45='ce' with at most ONE non-granted assumption beyond the tested premise.
2. (Alternative arm) Record W4 as double-residual: ungrammatical under BOTH the 78='ver'+45='dict' two-token reading and the 78='ver'-word+45='ce' two-token reading.

Offset convention: @n below = 0-based pair index in the repaired 1,847-pair stream. The queue cites W4 at @1164-1165 (1-based); stream indices are @1164 (78) / @1165 (45).

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` (stride-2 pairing per row offset). Verified 1,847 pairs / 96 types before testing. `canonical.py` never used. R5005 untouched (read-only parse). No sealed gates, no red-team contact. Every number traces to the stream.

Standing values used (protocol §7): banked GT 11=la, 82=m, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79="tout", 00="pour", 84="on", 47="ce"; §7 holds: 45="ce" (A11), 67 et/veut sole true polyvalence with the positional rule (67="veut" iff follower infinitive-shaped). 78="ver" is LEAD (R16-005, confirmed R17-006/R17-021) — conditional, not granted.

## Window-level evidence

W4 (stream @1162-1168, row a6_09), re-derived: `44 83 | 21 67 | 78 45 13 55 61 | 94 87 83 21`.

**Left edge.** 67's follower is 78. 78 is noun-positioned: 16/31 determiner predecessors (re-derived: 77x7, 47x5, 11x2, 87x2 of 31 windows). Follower is noun-shaped, not infinitive-shaped → 67='et' by the §7 positional rule. (Consistent with dict-frame-78-45-13-55-61's clause-3 fence; the positional rule is standing protocol, not a new assumption. The "veut" reading would require 78 infinitive-shaped, which the determiner-predecessor profile rejects.)

**Clause-1 arm: best two-token 'ce' parse.** With 45='ce' (premise) and 67='et' (positional rule), the window must parse as "[21-phrase] et [78-word] ce [13-55-61] …", where 78 is a 'ver'-shaped French word (conditional on the LEAD). Exhaustive survey of 'ver'-shaped words that can grammatically precede "ce [NP]":

1. "vers" (preposition): "et vers ce [13-55-61]" = "and toward this [13-55-61]" — grammatical IFF 13-55-61 is a noun. Assumptions: (a) 78='vers' specifically (shape is LEAD, the word ungranted); (b) 13-55-61 is one noun (open — dict-frame-78-45-13-55-61 nulled its unit-naming). = **2 non-granted assumptions.**
2. "verser" (infinitive): "veut verser ce [13-55-61]" (67 flips to 'veut' by the positional rule) — grammatical IFF 13-55-61 is a noun. = 2 assumptions, AND conflicts with 78's noun-positioning at W4 (fork-battery requirement). Weaker than (1).
3. "verdit" (finite verb, passé simple of verdir): "et verdit ce [13-55-61]" — = 2 assumptions + noun-positioning conflict. Weaker.
4. "verbe"/"verre" (noun): "[N] ce [N]" — ungrammatical (two nouns, no relation).
5. "vert" (adjective): "vert ce" — ungrammatical.
6. 45='ce' as pronominal head ("ce" + relative): requires "ce que/qui"; 13-55-61 is not 46/64-shaped. No.

Best candidate is (1): "[21-phrase] et vers ce [13-55-61-noun]". It needs 2 non-granted assumptions (78='vers', 13-55-61-as-noun). Bar budget is ≤1. **Clause-1 arm FAILS — no two-token 'ce' parse exists within the assumption budget.**

Right-edge note (shared with both readings, not part of W4's 7-gram): @1169-1170 = "94 87" is stream-unique (1/1,847) and "ne ce" under 94='ne' STRONG LEAD (R17-001); owned by queued ne-ce-1169, not re-litigated here.

**Clause-2 arm: double-residual test.**

- Reading 1 (78='ver' + 45='dict' two-token → the French word "verdict"): W4 = "[21-phrase] et verdict [13-55-61] …". Bare countable noun "verdict" in argument position with no determiner. French requires a determiner for countable nouns in argument positions; no zero-determiner construction applies (not a mass noun, not a fixed idiom, not headline style in 1841 prose). **Ungrammatical at kill grade within the two-token scope.** (The dict-45 battery called this "strained" and escaped via the 5-gram unit reading; that escape belongs to dict-frame-78-45-13-55-61 — fenced as outside scope, not re-run or re-adjudicated here.)
- Reading 2 (78='ver'-word + 45='ce' two-token): shown above — no grammatical parse within ≤1 non-granted assumption; best needs 2 (78='vers' + 13-55-61 noun). Ungrammatical under the budget.

**W4 is a double-residual: ungrammatical under both two-token readings.** Bar discharged via the second arm.

## Per-clause pass/fail

1. **FAIL.** Best two-token 'ce' parse ("et vers ce [13-55-61-noun]") needs 2 non-granted assumptions (78='vers' specific word + 13-55-61 nounhood); budget is ≤1. No parse within budget.
2. **PASS (recorded).** W4 is double-residual: "et verdict [13-55-61]" (determiner gap, kill grade within two-token scope) and "et [ver-W] ce [13-55-61]" (no parse within budget) are both ungrammatical.

## Adverses answered

- **78='ver' LEAD:** answered — every reading is explicitly conditional on the LEAD (R16-005, confirmed R17-006/R17-021). The LEAD is not promotion, so the double-residual is recorded conditional on the 'ver' shape; it does not assert a granted 78 value and does not outrun the unsettled LEAD.
- **Does not duplicate dict-frame-78-45-13-55-61 (owns the 5-gram unit parse):** answered — that battery tested 13-55-61 as one French unit (nulled on naming). This battery tested only the 78/45 two-token locus and fenced the 5-gram unit escape as owned elsewhere, citing its result without re-running it.

## Verdict: NULL

- Not promote: no 'ce' parse within the assumption budget; the 78='ver' adverse stays LEAD, not resolved.
- Not kill: the bar's second arm is a record instruction, and the bar is discharged by recording the double-residual. A kill would outrun the unsettled 78='ver' LEAD (per the fork-78-45-adjudication precedent, an unfired conditional is null, not kill); the determiner-gap finding at reading 1 is kill-grade within the two-token scope but is recorded as the residual, not as a kill of the claim, pending the red-team polyvalence decision.
- No standing red-team verdict contradicted: A11 HOLD (45='ce') untouched — the finding is scoped to the 78-45 two-token locus at W4, not to 45's other 18/22 windows; the fork battery already framed the 78-45 windows as needing red-team declaration (§7). R16-005 LEAD respected.

**Headline for the red team:** W4 is ungrammatical under both two-token rival readings — neither 45='ce' nor 45='dict' explains @1164-1165 at the two-token level. The window needs (a) the fenced 5-gram unit reading, (b) a red-team-declared positional polyvalence, or (c) a third 78 value at W4. Battery cannot declare; feeding the polyvalence decision as charged.

## Follow-ups (null regenerates work; all absent from queue, verified 2026-10-08)

1. **vers-78-w4-gate** (priority 2). Claim: W4's 'ce' parse ("et vers ce [13-55-61]") re-tests clean once gates clear. Bars: (a) 13-55-61 named as noun X — cite name-13-55-61's result, do not re-run; (b) "et vers ce [X]" parses with 78='vers' as the ONLY non-granted assumption; (c) right-edge 94-87 anomaly resolved or fenced via ne-ce-1169. Evidence: this report. Adverses: 78='ver' LEAD (conditional); 67='et' via §7 positional rule.
2. **w4-dict-det-gap** (priority 3). Claim: the determiner gap at the 78-45 loci is adjudicated. Bars: (a) census all four 78-45 windows' left edges (re-derive or cite); (b) name a period-attested zero-determiner construction fitting W4's "et verdict [13-55-61]", or certify none exists (→ determiner gap is kill-grade for the two-token "verdict" reading, conditional on 78='ver' LEAD); (c) do not declare polyvalence (§7). Evidence: this report. Adverses: 5-gram unit escape owned by dict-frame-78-45-13-55-61 (fenced, not re-run).
3. **w4-21-leftedge** (priority 3). Claim: 21's value completes W4's left edge ("… 44 83 21 et vers ce …"). Bars: (a) 21 named with ≥2 frame-legs, or recorded as gate; (b) "…[21-phrase] et vers ce…" parallelism stated or the gate named. Evidence: this report; 21->67 x8 (21's top successor). Adverses: 83's value open ('de' lead held).

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs / 96 types asserted before testing): W4 = seq[1162:1170] = ['44','83','21','67','78','45','13','55','61','94'] on row a6_09; 78 n=31 with 16/31 determiner predecessors; 94-87 bigram count = 1/1,847. `canonical.py` never used. No writes outside this report, the queue edit (own entry only), and the lockfile (deleted).
