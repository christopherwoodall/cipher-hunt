# Battery report: adj-71-234-locus

**Target:** `adj-71-234-locus` — test adjective-71 as a locus-level-only reading at @234 (lane 1-based; 0-based @233): 'par [21-noun] [60-adj] [71-adj]', stacked epithets; the sole adjective-compatible window per the parent battery.

**Worker:** battery-worker-adj-71-234-locus (agent efedff0b-37e6-4b45-849a-d321c4840cd0). Date: 2026-10-09.

**Stream:** repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py` (replicated in-session; asserts: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim)

The queue entry's `bars` field is `None`; the dispatch brief's bar is used verbatim and recorded as such (no silent rewrite):

"Name the locus-level adjective reading with byte evidence or fence it."

**Numbered clauses (pre-registered before testing):**
- C1: Name 71 as epithet adjective at @233 (0-based; lane @234) with positive byte evidence for an adjective-shaped value (positional "sits after an adjective" does not count as value evidence).
- C2: The 'par [21-noun] [60-adj] [71-adj]' stacked-epithet parse is grammatical in 1841 French (corpus-supported, not merely asserted).
- C3: No standing red-team verdict contradicted; §7 intact (no second polyvalence or split declared at battery level).

## Method

1. Re-derived the repaired stream in-session; byte-verified the window.
2. Inventoried 71's 7 windows and standing class evidence (processed reports + R19-186/R20).
3. Ran a period-corpus check on bare double-postposed-adjective stacking (57 French files, German files excluded), heuristic common-adjective list, hand-verified the single candidate.

## Window-level evidence (@-offsets 0-based; lane convention is 1-based, so lane @234 = 0-based @233)

- @230=96 @231=21 @232=60 @233=71 @234=51 @235=70 @236=98, row a2_01: `96 21 60 71 51 70 98` = "par [21] [60] [71] [51] pre…".
- This is byte-identical to adj-60-2160's W4 ("96 21 60 71"), which promoted the '21 60' noun+epithet-adjective frame at this window at frame-leg finding grade.
- 71's full inventory (n=7): @233, @325 ("60 15 63 71 10 01 19"), @711 ("53 12 48 71 12 63 00"), @924 ("40 08 65 71 17 61 96" = "t 65 [71] fois", 1-based @925, forces non-nominal), @1336 ("39 83 86 71 64 60 08" = "[86-INF] [71] qui", 1-based @1337, forces nominal), @1564 ("30 06 60 71 50 29 24"), @1613 ("08 55 83 71 48 31 76").
- Standing 71 state: §7 split candidate (nominal@1337 vs non-nominal@925, R19-186 GRANT finding grade); uniform epithet-adjective KILLED at kill grade (battery-class-71-adjective: forced 71≠adjective at @925 and @1337); frequency leader "une" (determiner) per battery-un-71-det-census (no homophony exclusion fired).
- 51's class is open (n=6, no verdict); "71 51" boundary unresolved.

## Per-clause pass/fail

- **C1 — FAIL.** Zero positive byte evidence for an adjective-shaped 71 at @233. The inventory offers: nominal (forced @1336), non-nominal/quantifier-like (forced @924), determiner "une" (frequency leader). The uniform adjective arm is kill-grade dead. The only pro-adjective datum is positional (71 follows [60-adj]) — frame evidence, not value evidence; the slot also admits adverbs, quantifiers, or a word-internal onset with 51.
- **C2 — FAIL.** Corpus check: **0 genuine** bare-stacked "PREP DET N ADJ ADJ" in 57 French period files. The single regex candidate ("dans une conversation fort longue", talleyrand-memoires-v2) is adverb+adjective ("fort" = "very"), a false positive of the heuristic list. Coordinated "ADJ et ADJ": 55 attestations — the grammatical norm. The target window is stricter than the searched frame (bare 21, no determiner: "par [21] [60] [71]"). Standing battery precedent (adj-68-postnominal) treats "tout [adj] [adj]" as ungrammatical; the parent battery's contrary assertion ("stacked epithets are grammatical") cited no corpus evidence.
- **C3 — PASS as constraint.** Even setting C1/C2 aside, naming 71-adjective here would add a third class to an already split-shaped cell (nominal@1337 vs non-nominal@925) — a split declaration, which is red-team venue under §7. Recorded, not acted on.

## Verdict: NULL (fence)

The locus-level reading 'par [21-noun] [60-adj] [71-adj]' at @233 (lane @234) is **fenced**: no positive value evidence for 71-adjective (C1), and the stacked-epithet parse has zero corpus support against 55 coordinated controls (C2). Not a kill: 71's class at this window stays open (adverb/quantifier/word-internal arms untested), and any future adjective arm for 71 is red-team §7 venue.

## Scope

Fences only the stated locus reading. Untouched: 21=noun (battery grade, val-08-successor-class), 60-adjective at the four '21 60' windows (adj-60-2160, frame-leg finding grade), 71's §7 split candidacy (R19-186), the uniform-adjective kill (class-71-adjective), poly-60 fence (R20-119). No standing verdict contradicted or downgraded. §7 intact.

## Follow-ups (§4; all verified ABSENT from battery-queue.json)

1. `class-71-233-rerun` (P3) — determine 71's class at @233 (0-based) once 51's class lands or via an explicit "71 | 51" boundary test; bars: name the class with ≥1 frame-leg at battery grade, or fence the window.
2. `stacked-epithet-corpus` (P4) — widen the stacking check beyond PREP-frames with a POS-tagged 1841 corpus; bars: harden this fence to kill grade iff zero holds, else re-open.
3. `adj-71-split-venue` (P2, red-team venue, gather-only) — package: uniform adjective killed, @233 locus fenced at battery grade, 71 already split-shaped (nominal@1337 vs non-nominal@925); any adjective arm needs a §7 split declaration.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-adj-71-234-locus.md` (this file).
- Lock `code/crowd17/next-token/locks/adj-71-234-locus.lock` created on start (agent efedff0b-37e6-4b45-849a-d321c4840cd0, 2026-10-09T18:17:30Z), deleted on completion.
- Queue update: `adj-71-234-locus` → `status: verdict`, `verdict: {result: null, report, date: 2026-10-09}` via own-entry-only temp-file+rename (pre-write asserted queued/verdictless; post-write re-validated from disk; no other entries touched; no downgrade).
