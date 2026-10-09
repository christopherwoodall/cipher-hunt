# Battery verdict: cela-87-11-reseg

- Target: `cela-87-11-reseg` (battery-queue.json, priority 4, status queued)
- Claim: Test 87+11 = "cela" word composition at @163/@830: does "ne [24] cela" / "[24] cela" parse the closure windows without the A1 transitivity assumption?
- Parent: null-mandated follow-up from `battery-trans-24-ce-corpus` KILL (2026-10-09). That battery killed the corpus-discharge route for A1 (0 bare "savoir/vouloir + ce" in 61M chars, 22 hits for "V + cela") and proposed this target: a "cela" composition (87=ce granted + 11=la pencil) would give a grammatical bare-demonstrative-DO route for 24 without the corpus-rejected A1 assumption.

## Bar (verbatim, pre-registered)

> promote iff 87+11 segments as the single word "cela" at >=2 of the three closure loci (@163/@824/@830) with no byte-level contradiction and the "ne [24] cela" / "[24] cela" surface parses grammatical under 24's narrowed rivals (savoir/vouloir)

Restated as numbered pass/fail clauses before testing:

- **C1:** 87+11 is present and segments as the single word "cela" at >=2 of @163/@824/@830 (1-based pair indices of the 24 group: @163=24, @824=24, @830=24).
- **C2:** No byte-level contradiction — the raw digit runs at the loci parse as the stated pairs in the repaired stream.
- **C3:** The "ne [24] cela" surface (@163: "52 94 24 87 11") parses grammatical as one clause under 24 = savoir/vouloir.
- **C4:** The "[24] cela" surface (@830: "01 24 87 11") parses grammatical under 24 = savoir/vouloir.

## Method

1. Read BATTERY-PROTOCOL.md fully. Checked `locks/cela-87-11-reseg.lock` — absent, no other worker owned the target. Created the lock on start (agent e525d86e-6a23-4817-ae39-9143821e05e4, 2026-10-09T21:21:32Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py` logic: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
3. Loci re-confirmed in the repaired parse (1-based): @163 = pairs 161-165 "52 94 24 87 11" (row a1_05); @824 = pairs 823-826 "13 24 87 59" (row a5_05); @830 = pairs 829-832 "01 24 87 11" (row a5_06). The @ index names the 24 group.
4. Corpus checks ran against `code/side-period/corpus/` (the same 61M-char 1841 corpus as the parent battery).

## Findings

**Stream census:** "87 11" bigram occurs n=7 stream-wide at 1-based 87-positions @75, @164, @202, @462, @831, @1243, @1404 (rows a1_02, a1_05, a2_00, a2_10, a5_06, a7_01, a7_07) — matches the n=7 recorded in battery-cela-69-11-word (87-11 = "cela" granted compound at battery grade).

**Byte-level:**
- @163: row a1_05, offset 1, 87-11 at pair-index 2, raw digit run "87112482" = pairs 87, 11, 24, 82. Byte-exact.
- @830: row a5_06, offset 1, 87-11 at pair-index 5, raw digit run "87117776" = pairs 87, 11, 77, 76. Byte-exact.
- @824: row a5_05, offset 1, raw digit run "879" = pairs 87, 59, 38. 87 is followed by 59 ("est", provisional), NOT 11. The adverse is confirmed in the bytes.

**Grammaticality:**
- "[24] cela" (@830): grammatical under both rivals — "sait cela" / "veut cela". Corpus: 22 bare "V + cela" hits (parent's positive control, e.g. "Voltaire savait cela", "Vous savez cela aussi bien que moi").
- "ne [24] cela" (@163): UNGRAMMATICAL. The surface is 94("ne", provisional-strong) + 24 + "cela" with NO "pas" (30, promoted) anywhere within +/-15 pairs. In 1841 French, negated savoir/vouloir requires "ne ... pas": corpus check finds **0** hits for "ne V cela" (lone ne) across 61M chars vs **3** hits for "ne V pas cela" ("ne savez pas cela" x2, "ne sais pas cela" x1). Red-team R19-191 already ruled on this exact window (@162 lone-"ne"): "'ne fait'/'ne laisse' without 'pas' ungrammatical in 1841 French" — the structural objection (lone-ne without pas) is value-independent and transfers to "ne sait/veut cela".
- Cleaner rival parse on the same frame: battery-ne-24-profile reads @162-165 as "ne [24]. Cela [24] m ..." — a clause boundary after 24 (absolute-modal "ne [24]" clause, lone-ne = author's norm 34/37), with "cela" as the SUBJECT of the next clause, not 24's direct object. This rival is battery-established and absorbs the window without the closure DO parse.

## Per-clause pass/fail

- **C1: PASS.** 87+11 segments at @163 (pairs 164-165) and @830 (pairs 831-832) = 2 of 3 loci. @824 hosts 87+59 instead.
- **C2: PASS.** Raw digit runs confirm byte-exact "87 11" at both loci; no contradiction. 87=ce granted, 11=la pencil ground truth, 87-11="cela" compound granted at battery grade.
- **C3: FAIL at kill grade.** "ne sait/veut cela" without "pas" is ungrammatical in 1841 French: red-team R19-191 ruled lone-ne ungrammatical on this exact @162 window; corpus 0/61M "ne V cela" with positive "ne V pas cela" control (3 hits); no 30 within +/-15. A window forces the "ne [24] cela" closure parse false, and a cleaner rival parse (clause boundary, "cela" = next-clause subject) is demonstrated on the same frame.
- **C4: PASS (in isolation).** "[24] cela" is grammatical ("sait/veut cela", 22 corpus hits) — but the bar is conjunctive; C3's kill-grade failure kills the promote.

## Adverses

- **A1 (@824 has 87 followed by 59, not 11):** ANSWERED — re-parsed cleanly. 87+59 = "ce est" = "c'est" (cf. battery-ne-24-profile). The bar's ">=2 of the three" threshold explicitly accommodates this; the composition holds at @163 and @830.
- **A2 (87+11 composition may not hold at all three loci):** ANSWERED/FENCED — holds byte-exact at @163/@830 (2 of 3, satisfying the bar); fenced at @824 with stated cause ("c'est" parse, not "cela").

## Verdict: KILL

The "cela" composition is real (C1, C2 pass; 87-11="cela" remains granted) but it does NOT re-open the closure parse: the @163 "ne [24] cela" surface is ungrammatical at kill grade (lone-ne without pas, red-team R19-191, corpus 0/61M with positive control), and the @163 window is already absorbed by the cleaner clause-boundary rival ("ne [24]. Cela [24] m..."). The closure-reopening claim is dead; nothing here downgrades 87+11="cela" as a compound, 87=ce, 11=la, or the 22 "V + cela" corpus facts. No standing red-team verdict is contradicted (R19-191 supports this kill).

## Follow-ups proposed (kill verdict; optional, verified ABSENT from battery-queue.json, left for supervisor)

1. `cela-830-solo` (P4) — the @830 "[01] [24] cela" surface IS grammatical in isolation ("sait/veut cela", 22 corpus hits). Name 01's value iff it yields a grammatical clause with standing values and zero new assumptions at @830; else fence @830 as cela-subject-of-next-clause vs 24-DO.
2. `cela-163-clause-boundary` (P4) — directly test battery-ne-24-profile's rival at @161-168 ("35 93 52 94 [24] | 87 11 [24] 82 84"): does a clause boundary before 87-11 hold with stated values and zero new assumptions, or does the tail ("cela [24] m on") force a re-read?

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-cela-87-11-reseg.md` (this file).
- Queue: `cela-87-11-reseg` -> `status: verdict`, `result: kill`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.cela-87-11-reseg.tmp` + atomic rename; JSON re-validated after rename; own entry only; no downgrade; no tmp leftover).
- Lock created 2026-10-09T21:21:32Z (no stale lock present), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
