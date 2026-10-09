# Battery verdict: tail-74-78-frame

- Target: `tail-74-78-frame` (battery-queue.json, priority 3, status queued)
- Claim: "test whether the post-residual tail '74 [et] 78' (0-based @350-352) is salvageable as a fragment: 74's follower profile (n=34), 78's predecessor profile (n=31)"

## Bar (verbatim, pre-registered)

"if a licensed '74 et 78' frame exists, the W1 fence's scope narrows to @344-349; if none exists, the residual extends to @352"

Numbered clauses:
- C1: a licensed '74 et 78' frame exists → the W1 fence's scope narrows to @344-349 (PASS iff 74, 'et', and 78 compose into a grammatical fragment at battery grade)
- C2: no licensed '74 et 78' frame exists → the residual extends to @352 (FIRES iff C1 fails with stated cause)

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session via `code/side-keyhunt/repair_parse.py` + `repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. Adopted without re-litigation: battery-w1-342-tail-parse (NULL, fence executed — W1's 87-scope fenced as 06-driven residual @344-352, 67='et' at @351 by the positional rule), val-74-212 (74 verb-shaped at @212; "ne [74]" x3 forces finite verb), R16-005 (78='ver' LEAD deferred), the 67 et/veut §7 positional rule (67='veut' iff follower infinitive-shaped).

## Findings

**Locus byte-confirmed** (0-based): `@349=94('ne') @350=74 @351=67 @352=78('ver',LEAD) @353=40('e')`, row a2_05. Full W1 window: `87(ce) 01 06(ent) 70(pre) 12(n) 94(ne) 74 67 78(ver)`.

**74's follower profile** (n=34): 74 x6, 45(ce/dict) x3, 46(que) x3, 62 x3, 67 x2, 77(le) x2, 65(noun) x2, 47(ce) x2, 48(e) x1, 49 x1, 40(e) x1, 42(noun) x1, 32(verb) x1, 52 x1, 34(i) x1, 84(on) x1, 87(ce) x1, 35(noun) x1, 93(verb) x1. Heterogeneous — no dominant composition frame.

**78's predecessor profile** (n=31): 77(le) x7, 47(ce) x5, 37 x4, 67 x4, 11(la) x2, 87(ce) x2, 16 x1, 50 x1, 86(INF) x1, 80 x1, 98(verb) x1, 84(on) x1, 17(fois) x1. Determiner-heavy left edge (le/ce/la x14) — nominal-positioning, not verbal.

**The '74 67 78' trigram is a stream hapax** (@350 only). '74 67' x2 (@142, @350); '67 78' x4 (@351, @491, @1163, @1842).

**C1 tested — the frame does not compose:**
1. 67='et' at @351 is licensed (parent's positional-rule finding: 78 open → 'et' default). Adopted.
2. 74 at @350 is finite-verb-shaped ('ne' forcing). Adopted.
3. But 'et' coordinates like elements, and **78 has no licensed role after 'et' here**: 78's class is open (registry ['ver','lead'], deferred — no class grant at battery or red-team grade). The three other '67 78' windows all show 'et ver' in NOMINAL-coordination slots ("[20] et ver [42-N]" @491, "[21-N] et ver ce" @1163, "[21-N] et ver [49]" @1842) — they do not license "V-fin et ver" at @351, where the left element is a finite verb, not a noun.
4. No in-stream parallel licenses "[V-fin] et [78]": 78 is not verb-shaped at battery grade anywhere, and the determiner-heavy predecessor profile (le/ce/la x14) points away from a verbal 78, not toward one.

The licensed components (67='et', 74's verb shape) do not add up to a licensed FRAME — 78 dangles with no grammatical position. C1 FAILS.

**C2 fires:** no licensed '74 et 78' frame exists. The W1 fence's scope is not narrowed: **the residual extends to @352** (the full @344-352 window remains fenced as the 06-driven residual per battery-w1-342-tail-parse).

## Verdict: NULL (fence executed per the bar's else-branch)

The tail is not salvageable as a fragment at battery grade. Scope: extends the W1 residual's right edge to @352; nothing else moves. No standing/red-team verdict contradicted or downgraded; §7 intact (67='et' at @351 by the positional rule, unneeded for the fence). Canonical-stream caveat stands (row a2_05 offset unvalidated).

## Follow-ups (§4, all verified ABSENT from battery-queue.json)

1. `class-78-352-coord` (P4) — name 78's class at @352; a verb-shaped 78 would license the 'et' coordination and re-open the tail.
2. `et78-noun-coord` (P4) — test the noun-coordination reading of 'et 78' at @491/@1163/@1842; if 78 is nominal there, the @351 instance's non-nominal left element kills the frame there permanently.
3. `val-74-350-finite` (P4) — name 74's value at @350; a named finite verb + named 78 could re-compose the tail.

## Bookkeeping

- Queue: `tail-74-78-frame` queued → `verdict`/`null` 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.tail-74-78-frame.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock `locks/tail-74-78-frame.lock`: created on start (agent ba18bf07, 2026-10-09T19:29:10Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
