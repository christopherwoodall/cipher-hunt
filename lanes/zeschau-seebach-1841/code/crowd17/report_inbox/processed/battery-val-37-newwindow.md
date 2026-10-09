# Battery report: val-37-newwindow

- Target id: `val-37-newwindow`
- Claim: lexical search for an adjective value parsing the predicative-shaped 37 windows (@913, @1179, @1797) without colliding with the forced-nominal clefts @529/@1444
- Date: 2026-10-09
- Worker: battery worker (subagent 3c09129b-fa47-4012-87b7-b2f08ea5af2f)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types, n(37)=28. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offsets below are 0-based stream indices (lane convention).

Terms (ASD-STE100): "value" = the French word a cipher number spells. "cleft" = the "est [37] qui" focus construction. "kill grade" = a window forcing the claim false under standing values. "uniform" = one value holding at every 37 window (37 has no standing split). "name" = state a value with byte evidence at battery grade.

## Bar (verbatim from queue `bars` field)

"Bar: lexical search for an adjective value parsing the predicative-shaped 37 windows (@913, @1179, @1797) without colliding with the forced-nominal clefts @529/@1444. Bar: one value parsing all three with zero kill-grade contradictions; kill iff none exists (names value, does not reopen the clefts)."

Restated as numbered pass/fail clauses before testing:

1. **C1 (search):** conduct a lexical search for an adjective value over the three predicative-shaped 37 windows (@913, @1179, @1797).
2. **C2 (uniformity):** one adjective value parses ALL THREE windows with zero kill-grade contradictions and does not collide with the forced-nominal clefts @529/@1444. The clefts are not re-opened.
3. **C3 (kill clause):** iff no such value exists, verdict is KILL.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-37-newwindow.lock` (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All asserts held (1,847 pairs, 96 types, n(37)=28).
3. Standing premises used, not re-litigated: banked pencil 11=la/70=pre/82=m/34=i/29=er/40=e/46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional 59=est, 77=le; splits hold 20~17, 23~26 (no 37 split); §7 (67 et/veut sole true polyvalence); the adopted battery premise that "est [37] qui" clefts force the nominal arm — *"c'est [adj] qui"* is ungrammatical in every period (`x-33-37-licensing`, via `sel-37-pressure`).
4. Adopted, not re-litigated: `enterre-37re-s5` KILL (uniform 37='re' dead; re-open condition 77≠'le' unfired); `sel-37-pressure` NULL (frame set not uniformly predicative; the only ever-named candidate dead).

## Window-level evidence

All five loci byte-confirmed on the re-derived stream:

- **@529** (a3_00): `97 47 44 | 59 37 | 64 26` — "…[44] est [37] qui [26]…". Forced-nominal cleft.
- **@1444** (a7_09): `01 52 68 59 | 37 64 | 77 84` — "…[68] est [37] qui le [78]…". Forced-nominal cleft.
- **@913** (a5_09): `49 64 83 59 | 37 96 | 09 02` — "…qui [83] est [37] par [09]…". Predicative-shaped.
- **@1179** (a6_10): `74 32 48 59 | 37 77 | 78 94` — "…[48] est [37] le [78]…". Predicative-shaped.
- **@1797** (a8_10): `56 42 94 59 | 37 91 | 79 87` — "…est [37] [91] tout…". Predicative-shaped.

Both clefts have the exact geometry "59 37 64" — verified: no determiner or any other cell stands between 59 and 37 at either locus.

### C1 — PASS (search conducted)

The search space is the full French adjective lexicon (bare adjectives, past-participle adjectives, and dual-class adjective/noun words), tested against the bar's two filters: (a) parses @913/@1179/@1797; (b) no collision with the forced-nominal clefts @529/@1444.

### C2 — FAIL at kill grade (the collision is structural)

Filter (b) empties the search space before any per-window lexical fitting matters:

- 37 has no standing split (splits hold: 20~17, 23~26) and §7 bars battery-grade polyvalence (67 et/veut is the sole true polyvalence). Any adjective value named for @913/@1179/@1797 is therefore the same value at @529/@1444.
- At both clefts the named value would sit in "est [37] qui". Under the adopted premise, *"c'est [adj] qui"* is ungrammatical in every period — the cleft forces the nominal arm. So EVERY adjective value collides at kill grade, at two independent windows.
- No rescue through dual-class words: a noun-capable adjective (e.g. "sage", "grand") still needs a determiner in cleft focus (*"est sage qui"* is ungrammatical), and no determiner stands between 59 and 37 at either cleft (byte-verified). Inventing one is barred by §3.
- No rescue through the 37-01 unit (A12): at the clefts 37 is followed by 64=qui, so the unit is not in play.

The kill is therefore not epistemic ("no adjective tried"): it is structural — the cleft geometry forces nominal, the bar demands an adjective, and 37 is unsplit. No adjective value can satisfy both.

Secondary per-window evidence (not needed for the kill, stated for the record): the three predicative windows each strain a bare-adjective reading independently — @913 bare adjective + "par"-complement (96=par promoted) is unlicensed for non-participle adjectives; @1179 "est [adj] le(77, provisional)" has no grammatical parse; @1797 "est [adj] [91] tout(79, granted)" has no licensed continuation. Past-participle adjectives parse @913 ("est respecté par…") but die at the clefts like every other adjective.

### C3 — FIRES

C2 fails at kill grade, so the bar's kill clause fires. No value is named. Per §4, kills regenerate no follow-ups.

## Verdict: KILL

No adjective value exists that parses the predicative-shaped 37 windows without kill-grade collision at the forced-nominal clefts @529/@1444. This verdict contradicts no standing verdict and downgrades none; §7 intact; the clefts are not re-opened. Canonical-stream caveat stands (rows a3_00/a5_09/a6_10/a7_09/a8_10 offsets unvalidated).

## Scope

Kills only the uniform-adjective-value claim for 37. Untouched: 37's class (open), the A1 predicative-frame status (red-team venue — context: REPORT.md N59 records the red-team demotion of the 37/42 predicative est-frames to HOLD; stated here, not adjudicated), nominal-37 readings, the forced-nominal clefts themselves, and 56's object slot at @795/@1658. Re-open is red-team venue (a standing 37 split, a §7 polyvalence ruling, or overturn of the cleft premise).

## Bookkeeping

- Queue: `val-37-newwindow` → status `verdict`, result `kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/val-37-newwindow.lock` created on start, deleted on completion (verified gone).
