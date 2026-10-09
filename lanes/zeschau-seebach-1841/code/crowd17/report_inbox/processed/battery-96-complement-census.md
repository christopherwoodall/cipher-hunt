# Battery verdict: 96-complement-census — complement-typed census of all 96 windows

**Target:** 96-complement-census
**Date:** 2026-10-09. Worker: eb8eeded-ac0e-4ed6-9293-0d5c09c994f6.
**Parent:** `par-42-complement` NULL (2026-10-09), follow-up #2.

## Bar (verbatim from battery-queue.json)

`complete complement-typed census of all 96 windows with byte evidence`

## Bar restated as numbered pass/fail clauses (pre-registered)

- **C1:** every 96 occurrence in the repaired 1,847-pair stream is enumerated with 0-based @-offset, row id, and byte-exact successor. PASS iff n(96) is re-derived and all windows are listed.
- **C2:** every 96 occurrence carries a complement type from {agent-par, means-par, distributive, complement-less} with byte evidence for the complement; windows undecidable under standing values are fenced with stated cause, never left blank. PASS iff all 21 windows are typed or fenced.
- **C3:** the claim's test is answered — whether the three "96 00" windows (@47/@465/@960) are the only complement-less pars. PASS iff the complement-less set is determined and compared.

## Method

- Re-derived the full stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). Asserts re-run: **1,847 pairs, 96 types**. `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched.
- n(96) = **21**, derived independently (matches the sibling `par-96-complement-census` sweep). 12 distinct successors: 00 x3, 87 x3, 21 x3, 43 x2, 45 x2, 82 x2, 56 x1, 47 x1, 40 x1, 09 x1, 48 x1, 86 x1.
- Standing values used (§7 + battery verdicts): 96=par (granted); 00=pour (A9 class-level); 87=ce; 47=ce (A4 allophone); 46=que (pencil); 45=ce (A11 hold); 64=qui; 40=e, 48=e, 82=m, 12=n (pencil letters); 86 INF-class (A9); 36=NOUN (class-36-profile PROMOTE, value open); 93 nominal head at @602 (frame-74-45-93 PROMOTE, window-scoped); 56 whole-word, finite verb @1732 (stem-56-whole + w5-pas-verb PROMOTE; value open; other windows undecided); par-43 kill terminal (par43-adverbial-attestation PROMOTE; "par suite" escape licensed BUT 43="suite" killed per noun-43-discriminator / frame-43-pour-census); F54 conditioned islet 96-00="par le" (red-team, undisturbed).
- This is a **red-team INPUT package**: the venue questions are gathered with byte evidence, never decided. Adverses = the venue items below, each fenced with stated cause.

## Census: all 21 windows of 96 (0-based @, row, byte window, successor)

Type key: M = means-par, CL = complement-less, OPEN = successor class open at this window (fenced), F = fenced compositional/word-internal (no word-level complement slot), (a)/(b) = reading-dependent (see venue note V1).

| @ | Row | Byte window (-3..+3) | Succ | Succ standing | Type | Complement evidence |
|---|-----|----------------------|------|---------------|------|---------------------|
| 47 | a1_01 | 81 30 62 [96] 00 92 79 | 00 | pour (A9) | CL (b) / M (a) | "par pour" fenced residual (seg battery NULL); F54 islet -> "par le [92]" (A14 set-level) |
| 131 | a1_03 | 26 32 [96] 56 64 21 | 56 | whole-word; finite verb @1732 only; value open | OPEN | 56's class at @132 undecided; finite-verb reading -> CL, nominal reading -> M |
| 150 | a1_04 | 64 96 [47] 46 66 | 47 | ce (A4) | M | "par ce que" causal clausal (47-46) |
| 224 | a2_01 | 61 96 [87] 46 98 | 87 | ce | M | "par ce que" (A3 re-derived) |
| 230 | a2_01 | 82 96 [21] 60 71 | 21 | noun-class (de-frame-21-class); formula-bound | OPEN | "98 83 82 96 21 60" byte-identical x3 (@230/@1063/@1786); 96-21 nowhere else; @21 polyvalence pending |
| 342 | a2_05 | 64 96 [43] 87 01 | 43 | fem noun, value open; par-43 kill | CL | bare "par [43]" unattested (mesure/condition); "par suite" escape needs 43="suite" (killed) |
| 465 | a2_10 | 42 96 [00] 33 79 | 00 | pour (A9) | CL (b) / M (a) | same venue as @47 |
| 602 | a4_00 | 26 96 [45] 93 54 | 45 | ce (A11); 93 nominal head (window-scoped) | M | "par ce [93]" demonstrative NP (frame-74-45-93) |
| 847 | a5_06 | 33 96 [40] 62 21 | 40 | e (letter, pencil) | F | compositional "par e[62]" word-initial; no word-level complement statable |
| 914 | a5_09 | 37 96 [09] 02 24 | 09 | class open (noun-09-916 NULL) | OPEN | "est [37] par [09] [02]"; nominal-09 -> M, verb-09 (lon-09-verb) -> CL |
| 927 | a5_10 | 61 96 [48] 82 98 | 48 | e (letter) | F | compositional "par em[82]" word-initial |
| 947 | a5_10 | 98 96 [86] 01 77 | 86 | INF-class (A9); value open | M | "par [86-inf]" substantivized infinitive; 86 positional life contested (homophone-86-split NULL) |
| 952 | a6_00 | 86 96 [87] 46 24 | 87 | ce | M | "par ce que" (A3 flagship; @952->24 elision) |
| 960 | a6_00 | 67 96 [00] 86 56 | 00 | pour (A9) | CL (b) / M (a) | same venue as @47 |
| 998 | a6_02 | 11 96 [82] 33 00 | 82 | m (letter, pencil) | F | compositional "par m[33]" word-initial |
| 1026 | a6_03 | 64 96 [43] 87 01 | 43 | same as @342 | CL | same as @342 ("par [43] ce [01]"; par43-ce-scope NULL) |
| 1063 | a6_04 | 82 96 [21] 62 18 | 21 | same as @230 | OPEN | formula x3 (third = 62) |
| 1196 | a7_00 | 16 96 [82] 16 64 | 82 | m (letter); doubled frame | F | "16 96 82 16"; a7_00 offset unvalidated (canonicality caveat) |
| 1213 | a7_00 | 48 96 [45] 36 77 | 45 | ce (A11); 36=NOUN | M | "par ce [36]" demonstrative NP (class-36-profile) |
| 1526 | a8_00 | 48 96 [87] 46 21 | 87 | ce | M | "par ce que" (A3) |
| 1786 | a8_09 | 82 96 [21] 68 47 | 21 | same as @230 | OPEN | formula x3 (third = 68) |

Type totals: **means-par 7** (@150, @224, @602, @947, @952, @1213, @1526); **complement-less 5 under (b)** (@47, @342, @465, @960, @1026) / **2 under (a)** (@342, @1026); **open 5** (@131, @230, @914, @1063, @1786); **fenced 4** (@847, @927, @998, @1196). **Agent-par: 0** (no passive-participle predecessor at any window; @914 "est [37] par [09]" is the only structural candidate and 37's participle status is NULL per frame-37-reexam). **Distributive: 0** (no distributive-shaped successor). 7+5+5+4 = 21. ✓

## Red-team venue notes (gathered, NOT decided)

- **V1 — the three "96 00" windows (@47/@465/@960).** Two standing readings. (a) F54 conditioned islet: 96-00 = "par le" -> "par le [92/33/86]" + substantivized infinitive, means-par (A14 set-level grant; 33/86 strong INF-signal, 92 rides on the set). (b) Unconditioned: 96=par + 00=pour -> "par pour", complement-less, fenced systematic residual (seg battery NULL; par-42-complement adopts the fence); "par contre" rival lives at contre-00-condition-gate / redteam-contre-00 (queued). Byte shapes: @47 "62 96 00 92 79(tout)"; @465 "42 96 00 33 79"; @960 "67(et) 96 00 86 56". Deciding is red-team venue (par-pour-redteam P2 queued).
- **V2 — "96 21" x3 (@230/@1063/@1786).** Reading (i): "par [21-noun]" (de-frame-21-class noun-class PROMOTE; sibling sweep adopted). Reading (ii): "vient de me parvenir" formula (frame-vient-parvenir; 83="de" cross-checked at 2 other windows; thirds claim KILLED). Byte gap in (ii): no 48 for "me"'s "e" (82=m pencil; §7 bars a second 82 polyvalence). The @21 polyvalence adjudication is the pending decider (par-43 kill "pending only the @21 polyvalence adjudication"). Not decided here.
- **V3 — @131 "par [56]".** Correction to the sibling sweep: its "parses — 'par [56]' infinitive (56 verb-stem class)" premise is superseded by stem-56-whole PROMOTE (56 whole-word, not a stem) + w5-pas-verb PROMOTE (56 finite verb @1732). A finite verb cannot complement "par"; 56's class at @132 is explicitly undecided ("no other window is decided here"). OPEN.
- **V4 — @914 "est [37] par [09]".** 09-as-nominal-complement-of-par is open (noun-09-916 NULL); lon-09-verb NULL keeps the verb-shaped rival alive. OPEN. (Also the sole agent-par candidate if 37 ever grades participle — frame-37-reexam NULL.)
- **V5 — @947 "par [86]".** Typed M on A9's INF-class grant; 86's positional life here is contested (homophone-86-split NULL, le-86-determiner-subset NULL) — type is conditional on the INF-class reading.
- **V6 — letter-successor windows (@847/@927/@998/@1196).** Fenced as compositional word-initial ("par e[62]", "par em[82]", "par m[33]", doubled "16 96 82 16"); no word-level complement statable under standing values. @1196 carries the a7_00 canonicality caveat (offset unvalidated; offset-1 reparse is red-team territory).

## Per-clause results

- **C1: PASS** — n(96)=21 re-derived from the repaired stream (1,847 pairs / 96 types, asserts re-run); all 21 listed above with 0-based @-offsets, row ids, byte windows, successors.
- **C2: PASS** — all 21 typed (7 M, 5/2 CL reading-dependent, 5 OPEN, 4 F) with byte evidence; every undecidable window fenced with stated cause; none blank, none invented.
- **C3: PASS** — tested and answered: **NO.** Under reading (b) the complement-less set is {@47, @342, @465, @960, @1026} — five, not three. Under reading (a) the 96-00 windows are means-par ("par le [INF]"), leaving {@342, @1026} complement-less — the premise fails instead. Either way the three "96 00" windows are **not** the only complement-less pars. (Refines, does not overturn, the sibling sweep's uniqueness-in-kind finding.)

## Verdict: PROMOTE

Census package delivered: complete complement-typed census of all 96 windows with byte evidence. Adverses (V1–V6) gathered and fenced for the red-team 96/00 venues — nothing decided at battery level. No standing verdict contradicted or downgraded (§7 intact; no polyvalence declared; the V3 note supersedes a sibling *premise*, not a verdict).

## Bookkeeping

- Report: this file (`code/crowd17/report_inbox/battery-96-complement-census.md`).
- battery-queue.json: `96-complement-census` → status `verdict`, result `promote`, date 2026-10-09 (temp-file + rename; own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated from disk after write; no downgrade).
- Lock `locks/96-complement-census.lock`: supervisor-created reservation, kept for the run, deleted on completion.
