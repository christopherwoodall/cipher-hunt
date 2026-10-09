# Battery report: syl79-wordname

**Target:** `syl79-wordname` (P2)
**Date:** 2026-10-09
**Worker:** battery worker (subagent 8c729cc0-64df-4aaa-aa66-1961aadf35eb)
**Verdict:** PROMOTE (naming achieved where neighbor values resolve; 2/4 windows named, 2/4 fenced pending)

## Bar (verbatim from battery-queue.json)

> Name the words as neighbor values resolve.

Numbered pass/fail clauses (restated before testing, not modified after):

1. @451: name the multi-group word containing 79.
2. @1460: name the multi-group word containing 79.
3. @53: name the multi-group word containing 79 iff the neighbor values (85, 58) resolve; otherwise fence with stated cause.
4. @1419: name the multi-group word containing 79 iff the neighbor value (15) resolves; otherwise fence with stated cause.

Adverse (must be answered, not ignored): Progressive target — runs as neighbor values resolve; S-growth strengthens, W-growth weakens the 79 split (red-team declaration pending).

## Method

Read BATTERY-PROTOCOL.md first; created `code/crowd17/next-token/locks/syl79-wordname.lock` on start. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types); `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. All @-offsets are 0-based repaired-stream indices. 1841 diplomatic French throughout.

Adopted as premises (not re-litigated): 79="tout" (A5 banked); 17="fois" (banked GT); REPORT.md's recorded position that @451/@1460 read "toutefois" with "Inflection ≠ polyvalence"; the homophone-79-split S-family partition (@53, @451, @1419, @1460).

## Window-level evidence

**"79 17" census (byte-exact):** the bigram occurs exactly 2× stream-wide — @451 and @1460. These are the whole population of the "tout fois" shape.

### C1 — @451 (row a2_10): PASS — "toutefois" named

Bytes @449–454: `32 48 79 17 77 60` = "[32]e toutefois le [60]".
- 48='e' inflectional (granted) → "[32]e" predicative (A1 frame: 32 predicative).
- 79+17 = **"toutefois"** ("however"): 17="fois" banked; 79='toute', the feminine allomorph of banked 79="tout" (REPORT-sanctioned: inflection ≠ polyvalence, 67-sole-polyvalence law undisturbed).
- Right edge: 77='le' provisional + 60 open → "toutefois le [60]" = "however, the [60]…" — grammatical.
- Period-corpus attestation: "toutefois" occurs 318× in the lane's 1841 corpus (22× in RDM 1841-q1 alone) — a common diplomatic-prose adverb, not an invention.
- Word named: **toutefois** = 79+17.

### C2 — @1460 (row a7_09): PASS — "toutefois" named

Bytes @1458–1463: `86 66 79 17 01 21` = "[86] [66] toutefois [01] [21]".
- 79+17 = **"toutefois"** — same composition as @451.
- 86, 66 open; 01 is bound-only/dead as a whole word — 01 is a separate residual, not part of the named word and not re-litigated here.
- Word named: **toutefois** = 79+17.

### C3 — @53 (row a1_01): FENCE — neighbors unresolved

Bytes @51–56: `37 11 79 85 58 35` = "[37] la tout [85] [58] [35]".
- Candidate multi-group words containing 79 exhausted:
  - "toutefois"-type: requires 17 after 79 — absent. No.
  - 79+85: 85's value is open (A3 verb-stem frame granted, no value named by any battery). No French word nameable.
  - 79='toute': "la toute [85]" admits no grammatical parse (s5-la-tout-adjudicate's kill-grade "la tout" analysis extends; no 1841 precedent for the ellipsis rescue).
- 85 and 58 are both value-open; per the bar's own gate, no word can be named. Fenced with stated cause. (For reference: at @595, "79 85 01 29" reads "tout entière" with 79 standalone — the 79+85 contact does not force a single word.)

### C4 — @1419 (row a7_08): FENCE — neighbor unresolved

Bytes @1417–1422: `32 84 79 15 33 21` = "[32] on tout [15] [33]".
- 84="on" (A15). 79+15: 15's value is open (predecessors 41×2/60/94/98/79/66/58/30; no battery has named it). No French word nameable for "tout"+[15] or "toute"+[15].
- Fenced with stated cause per the bar's own gate.

## Per-clause results

1. **PASS.** @451 = "toutefois" (79+17).
2. **PASS.** @1460 = "toutefois" (79+17).
3. **FENCE (bar's conditional path).** @53 unnameable: 85/58 open.
4. **FENCE (bar's conditional path).** @1419 unnameable: 15 open.

## Adverse answered

Progressive target executed as designed: 2/4 windows named, 2/4 fenced pending neighbor resolution. The 79-split declaration remains red-team venue — `redteam-79-split-docket` is still queued and was not touched; nothing declared here. §7 honored: no polyvalence declared ("toutefois" = inflectional allomorphy of the banked lemma, the REPORT's standing position, not a second lexeme).

## Observation for the red-team 79 docket (not a finding)

Naming "toutefois" at @451/@1460 resolves two of the four S-windows via the 'toute' value-variant route (not the syllabic route): the unexplained S-set shrinks to @53 and @1419. The parent battery's bimodal W/S partition is otherwise undisturbed.

## Follow-ups (progressive re-runs; both verified absent from queue)

1. `syl79-53-rerun` (P3): name the @53 word once 85's and/or 58's values resolve.
2. `syl79-1419-rerun` (P3): name the @1419 word once 15's value resolves.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/syl79-wordname.lock` created on start, deleted on completion.
- `battery-queue.json`: `syl79-wordname` queued → verdict/promote (temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated; only this entry touched).
- R5005, sealed gate instances, red-team adjudication queue untouched.
- Canonicality caveat: rows a2_10/a7_09/a1_01/a7_08 carry unvalidated upstream offsets; verdict holds on the canonical stream per protocol.
- Scratch: `code/crowd17/next-token/work/syl79-wordname/stream.json` (re-derived stream, disposable).
