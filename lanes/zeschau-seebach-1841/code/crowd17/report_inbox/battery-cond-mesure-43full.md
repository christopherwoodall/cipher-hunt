# Battery verdict: cond-mesure-43full — full-distribution test of 43='condition' vs 43='mesure'

- Target: `cond-mesure-43full`
- Claim: test 'condition' vs 'mesure' across all 16 of 43's windows; the two-continuation joint test ties, so the full distribution decides
- Worker: battery worker cond-mesure-43full (86fa9d44-5d1f-4b4c-9157-d0bf51b1651a)
- Date: 2026-10-09
- Verdict: **NULL** (bar's else-branch: full-distribution survivor set recorded — it is **empty**)

## 1. Bar (verbatim from battery-queue.json)

"select iff one value parses all 16 windows with <=1 fenced residual and the other fails >=1 window at kill grade; else record the full-distribution survivor set"

Numbered clauses:
1. One value parses all 16 windows with ≤1 fenced residual.
2. The other value fails ≥1 window at kill grade.
3. Selection fires iff clauses 1 and 2 both hold; otherwise record the full-distribution survivor set.

## 2. Method

- Stream: repaired 1,847-pair parse only (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parse per code/side-keyhunt/repair_parse.py). Verified 1,847 pairs / 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched. Lock created on start, deleted on completion. 0-based @-offsets throughout.
- 43 census re-derived: n=16 at @21/@43/@244/@258/@343/@386/@439/@563/@1027/@1092/@1126/@1204/@1303/@1305/@1544/@1724 — matches the target brief.
- Standing values used (protocol §7 + red-team rounds): 11=la, 82=m, 34=i, 29=er, 40=e, 46=que, 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 59=est (prov), 77=le (prov), 06=ent, 30=pas, 86 INF-class, 80/89 verb-frames, 12=n, 48=e, 94=ne, 98='vient' (battery-grade, cont98-43-value).
- Prior batteries adopted, not re-litigated: noun-43-discriminator (KILL of 43='suite' and 43='manière'; @21 class-pull; par-43 accepted as suite-only; pour-que government reading), cont98-43-value (98='vient', continuation B non-discriminating), 43-1126-1725-joint (NULL, joint survivor set {condition, mesure}).
- Coordinated with (did not duplicate) queued `43-29-segment`: @21's class question (noun vs verb-stem/"en") is its bar; this battery uses noun-43-discriminator's established @21 finding as coordinated input.

## 3. Window-level evidence (all 16, re-derived)

Both candidates are feminine singular nouns, so most windows are symmetric. Kill-grade windows are marked.

**@21 (a1_00):** `64=qui 98 82=m [43] 29=er 47=ce 33` = "qui [98] m[43]er ce [33]".
- 43='condition': "mconditioner" — not French; no boundary placement hosts a standalone noun here (adopted: noun-43-discriminator's exhaustion, "msuiteer"/"suiteer"/"erce" family). FAIL kill-grade.
- 43='mesure': "mmesureer" — not French; same exhaustion. FAIL kill-grade.
- Symmetric, non-discriminating. Class question owned by 43-29-segment (not re-run).

**@43 (a1_01):** `24 88 [43] 81 30=pas` = "[24] [88] [43] [81] pas". 88/81/24 open. Both candidates parse identically in any reading (determiner/article absent for both equally). PASS both; non-discriminating.

**@244 (a2_02):** `56 [43] 00=pour 66` = "[56] [43] pour [66]". "condition pour"/"mesure pour" both idiomatic; 56's class open for both equally. PASS both; non-discriminating.

**@258 (a2_02):** `32 [43] 77=le 84=on` = "[32-pred] [43] le on". Predicative frame; feminine agreement identical for both. PASS both; non-discriminating.

**@343 (a2_05):** `96=par [43] 87=ce 01` = "par [43] ce [01]".
- 43='condition': "par condition" is not idiomatic 1841 French (no such adverbial; cf. "à condition que", "sous condition"). FAIL kill-grade.
- 43='mesure': bare "par mesure" is not French ("par mesure de X" needs its "de"; absent here). FAIL kill-grade.
- Symmetric, non-discriminating. (Accepted from noun-43-discriminator's par-43 frame: suite-only.)

**@386 (a2_07):** `37 [43] 91 36` = "[37-pred] [43] [91] [36]". Feminine agreement identical. PASS both; non-discriminating.

**@439 (a2_09):** `45 46=que [43] 98=vient 80` = "[45] que [43] vient [80]". Neuter "que"+noun needs a clause boundary for both equally (adopted: noun-43-discriminator). PASS both (boundary-fenced); non-discriminating.

**@563 (a3_02):** `11=la [43] 24` = "la [43] [24]". Both feminine. PASS both; non-discriminating.

**@1027 (a6_03):** `96=par [43] 87=ce 01` — byte-identical frame to @343. Both FAIL kill-grade (same analysis).

**@1092 (a6_06):** `06 [43] 07` = "[06] [43] [07]". 06='ent' (R17-007, conditional); 07 open. One-word readings ("entcondition"/"entmesure") not French; two-word readings ("[verb]-ent condition [07]"/"[verb]-ent mesure [07]") parse identically. PASS both (equally underdetermined); non-discriminating.

**@1126 (a6_07):** continuation A — adopted from 43-1126-1725-joint: "condition pour [86-inf]"/"mesure pour [86-inf]" both idiomatic. PASS both; non-discriminating.

**@1204 (a7_00):** `47=ce [43] 55 61` = "ce [43] [55] [61]". Neuter "ce"+noun needs a boundary for both equally. PASS both (boundary-fenced); non-discriminating.

**@1303/@1305 (a7_03/a7_04):** doublet `08 [43] 21 [43] 77` = "[08] [43] [21] [43] [77]". Owned by queued frame-43-21-43-doublet (not re-run); both candidates identical in the frame. PASS both (equally open); non-discriminating.

**@1544 (a8_00):** `78 [43] 00=pour 46=que 70=pre 12=n 94=ne` = "[78] [43] pour que prenne…". Under the government reading (adopted: noun-43-discriminator): "condition pour que" ✓ and "mesure pour que" ✓ — both PASS identically; the boundary alternative (queued frame-43-pour-que-1544) also treats both equally. Non-discriminating.

**@1724 (a8_07):** continuation B — adopted from 43-1126-1725-joint: "la [52] [37] condition/mesure vient à [88]" both grammatical, symmetric strain. PASS both; non-discriminating.

### Kill-grade tally

| window | condition | mesure |
|---|---|---|
| @21 (class pull) | FAIL kill-grade | FAIL kill-grade |
| @343 par-43 | FAIL kill-grade | FAIL kill-grade |
| @1027 par-43 | FAIL kill-grade | FAIL kill-grade |
| other 13 | PASS (symmetric) | PASS (symmetric) |

## 4. Per-clause pass/fail

1. **FAIL (both).** Neither value parses all 16 windows: 'condition' fails @21, @343, @1027 at kill grade; 'mesure' fails the same three at kill grade.
2. **FAIL (vacuous for selection).** Both fail ≥1 window at kill grade, so no value can be the selected one.
3. **ELSE-BRANCH FIRES.** Full-distribution survivor set: **{} (empty)** — no candidate survives all 16 windows.

## 5. Adverses answered

1. "@21's class pull — coordinate with queued 43-29-segment, do not duplicate": ANSWERED by coordination. noun-43-discriminator's @21 finding adopted as input (no French parse hosts a standalone noun for either survivor; "mener"/"emmener"/verb-stem family owns the window); the class adjudication itself is 43-29-segment's bar and was not re-run.
2. "52-37 unit open": CONFIRMED open; fenced with stated cause at @1126/@1724 (adopted from 43-1126-1725-joint — both candidates feminine, unit agrees identically under either).
3. "88 open": CONFIRMED open; fenced with stated cause at @1724 (continuation B tested under the live infinitive-88 hypothesis; no 88 value named).

## 6. Caveat

The empty survivor set kills the noun premise {condition, mesure} at battery grade. Two red-team-act escapes remain: (a) a period-corpus defense of bare "par mesure"/"par condition" as 1841 adverbials (I found none; the joint battery's F2 `venir-a-1841-corpus` covers corpus method); (b) 43-29-segment's class adjudication at @21 (if 43 is not noun-shaped there, the noun premise was already dead and par-43's kill is moot). Either escape is the red team's act, not this battery's.

## 7. Verdict: NULL

The bar's selection condition does not fire: both 'condition' and 'mesure' fail @21, @343, and @1027 at kill grade. Full-distribution survivor set: **{} — empty**. The noun hypothesis for 43 is dead at battery grade within the {condition, mesure} candidate set; no standing verdict contradicted or downgraded (suite/manière were already killed; no red-team ruling covers 43). R5005, sealed gates, and the red-team queue untouched.

## 8. Follow-up targets (null regenerates work)

F1. id: `noun43-redteam-escalate` | priority: 1
claim: "the noun premise for 43 is dead at battery grade: {condition, mesure} both fail par-43 x2 (@343/@1027) and @21 at kill grade; the empty survivor set needs red-team adjudication"
bars: "red team rules: (a) whether bare 'par mesure'/'par condition' have any 1841 corpus attestation (if yes, re-open the noun premise with the attestation); (b) reconcile with 43-29-segment's class adjudication at @21; (c) if both stand, close the noun-43 line and route 43 to the verb-stem/'en' hypothesis"
evidence: "this battery §3: par-43 x2 kill both survivors; @21 kill-grade for both under the noun hypothesis; noun-43-discriminator (suite/manière killed); 43-29-segment queued"
adverses: "43's noun legs ('la [52] [37] 43' x2, 'par 43' x2) — the very frames that now kill the survivors; protocol §7 67-sole-polyvalence"

F2 and F3 from 43-1126-1725-joint (`venir-a-1841-corpus`, `88-1727-shape`) are already queued — referenced, not duplicated.
