# Battery report: form-56-1627

- Target id: `form-56-1627`
- Claim: "decide 56 form (3sg -ee vs 3pl -eent vs infinitive) at @933/@1627 via spelling/shape constraints; a landed finite-56 forces the subject search and collapses H4"
- Date: 2026-10-09
- Worker: battery worker (subagent 541514d1-5353-44a5-9878-66bd711258fa)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: the brief uses 1-based @933/@1627. This report uses the queue convention, 0-based: @932 and @1626. Same loci.

Terms (ASD-STE100): "form" = which verb shape 56 takes. "3sg" = third-person singular, "il crée". "3pl" = third-person plural, "ils créent". "infinitive" = the base verb form, "créer". "bare-56" = 56 with no ending numbers after it. "spelled ending" = the cipher writes the ending with letter-tier numbers (40='e', 06='ent'). "battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"form named with byte evidence at battery grade"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** The infinitive (-éer) is excluded at @932/@1627 by spelling/shape constraints.
2. **C2:** The 3pl (-éent) is excluded at @932/@1626 by spelling/shape constraints.
3. **C3:** The 3sg (-ée) is confirmed at @932/@1626 with byte evidence.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/form-56-1627.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based.
3. Full 56 census re-derived (n=23; indices match stem-56-whole exactly): followers, predecessors, and adjacency tests for 29 ('er'), 40 ('e'), 06 ('ent').
4. Standing premises used, not re-litigated: 29='er', 40='e', 46='que' (pencil GT); 06='ent' (promoted, ent-06); stem-56-whole PROMOTE (56 whole-word; bare X = 3sg "il X"; X+e+ent = 3pl "ils Xent"); w5-pas-verb PROMOTE (56 finite verb @1732); le83-window NULL (83 fenced as blocker; 83='de' not standing); frame-vient-parvenir KILL (the source of the 83='de' lead); §7 (67 et/veut is the sole true polyvalence).

## Window-level evidence

The two loci (byte-confirmed):

- **W1 0b@932 (row a5_10):** `[929]82 [930]98 [931]83 [932]56 [933]69 [934]26 [935]00(pour)`. 56 is bare. Follower = 69. Predecessor = 83.
- **W2 0b@1626 (row a8_03):** `[1623]67 [1624]33 [1625]46(que) [1626]56 [1627]69 [1628]26 [1629]00(pour)`. 56 is bare. Follower = 69. Predecessor = 46='que'.

Formula identity: the 8-gram `56 69 26 00 33 21 64 37` is byte-identical at @932 and @1626, and occurs exactly 2x stream-wide. One number in byte-identical contexts carries one form (§7).

Ending-adjacency census over all 23 windows of 56:

- **56-29 ('er'):** 0/23. The spelled infinitive shape never occurs. (29 occurs within ±2 of 56 only at @502 and @1235, both two positions left and attached to neighbor words per stem-56-whole — never adjacent.)
- **56-40 ('e'):** 1/23 — only @1745, the 56-40-06 3pl spelling (the single A10-budgeted orphan).
- **56-06 ('ent'):** 0/23 direct. The cipher's 3pl shape always spells the ending (06 census: 82-06 x4, 42-06 x5, 30-06 x4; 40-06 hapax at @1746-1747).
- **"46 56" ('que'+56):** exactly 2x stream-wide (@1625, @1744).
- Followers of bare 56 include 69 x2 (@932, @1626), 37 x2, 32 x2, 30 x2, 87 x2, 47 x2, 41 x2 — no ending tier.

## Per-clause pass/fail

- **C1 — PASS (infinitive excluded).** (a) The cipher's infinitive shape for -éer verbs is [stem]+'er' = 56-29 (29='er' banked GT). 56-29 occurs 0/23 — the shape never occurs anywhere in 56's profile. (b) At @1626, "46 56" = "que [56]": "que" + infinitive is ungrammatical in French (parse-1626-clause H4 is blocked on exactly this). (c) At @932, the only infinitive license would be 83='de' ("de [56]"), but 83='de' is not standing: le83-window NULL fenced 83 as the blocker, and the 'de' lead came from the KILLED frame-vient-parvenir. (d) §7: the 8-gram is byte-identical at both loci, so one form holds; an infinitive at @932 beside a finite 56 at @1626 would be an undeclared class alternation.
- **C2 — PASS (3pl excluded).** (a) The cipher's only attested 3pl-56 shape is 56-40-06 with an overt spelled ending (@1745, the A10 orphan). Bare 56 at @932/@1626 carries no ending, and the cipher's 3pl shape elsewhere always spells -ent (06 census). (b) Promoted inflection model (stem-56-whole C2): bare X = 3sg "il X"; X+e+ent = 3pl "ils Xent". Bare-56 falls on the 3sg side. (c) Subject agreement: a 3pl verb needs a plural subject; neither window shows one — the only adjacent nominal is 69, battery-promoted 'ce' (singular demonstrative).
- **C3 — PASS (3sg confirmed).** (a) Bare-56 = 3sg finite is the lane's established shape: stem-56-whole PROMOTE (whole-word, 22/23); @795 "qui [56]" (a relative "qui" requires a finite verb; read "crée"-shaped 3sg by name-56-verb); @1732 "[56] pas" (w5-pas-verb PROMOTE: finite verb). (b) @1626 "que [56]" is a forced finite-verb slot. (c) With infinitive (C1) and 3pl (C2) excluded by spelling/shape, 3sg is the remaining form at both loci.

## Verdict: PROMOTE

56's form at @932/@1626 (brief's @933/@1627) is **3sg (-ée)** — "crée"-shaped, finite. All three bar clauses pass on byte evidence; no adverses were listed. No standing or red-team verdict is contradicted: the result agrees with stem-56-whole's promoted inflection model (bare X = 3sg at @795/@1626/@1732). §7 intact — no polyvalence declared.

Claim consequence fires: 56 is finite at both formula windows, so **H4 collapses** (parse-1626-clause H4: "56 non-finite, clause verb = 33" — dead). The subject search is now forced: H1 (69 inverted subject) vs H6 (69 subject, 26 object) vs a leftward subject.

## Caveats (stated, not hidden)

- The 3sg conclusion builds on lane-standing premises: stem-56-whole's inflection model, 83 fenced (not killed) as the @932 infinitive gate, and 69='ce' (battery-promoted, pending ratification) for the agreement leg.
- The "crée" = two spoken syllables in one cipher number is lane-settled (name-56-verb, stem-56-whole); not re-litigated here.

## Follow-ups proposed (promote needs none; these continue the claim's forced next steps — both verified absent from battery-queue.json)

1. `subj-56-1626` (P3) — locate the subject of finite 56 at @1626 ("que [56] [69] [26]"): test H1 (69 inverted subject) vs H6 (69 subject, 26 object) vs leftward subject. Bar: one grammatical subject placement with <=1 non-granted assumption, or fence with stated cause. Coordinates with queued `class-69-nominal`; does not duplicate it.
2. `de83-932-gate` (P3) — decide 83's value at @932 ("98 83 [56]"): if 83='de', the W1 infinitive residual re-opens under red-team eyes; else the W1/W2 form-identity stands closed. Gated on 83, not on 56.

## Bookkeeping

- Queue: `form-56-1627` → status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/form-56-1627.lock` created on start, deleted on completion (verified gone).
