# Battery report: sel-37-pressure

- Target id: `sel-37-pressure`
- Claim: "name 37's value (A1 predicative); a named 37 creates selectional pressure on 56's object slot at @795/@1658"
- Date: 2026-10-09
- Worker: battery worker (subagent 51065271-66a9-409e-baf9-3c39d63d5282)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offsets below are 0-based stream indices (lane convention).

Terms (ASD-STE100): "value" = the French word a cipher number spells. "A1" = the frame grant that 37/32/42 may stand as predicatives (value open). "iff" = if and only if. "name" = state a value with byte evidence at battery grade. "kill grade" = a window forcing the claim false under standing values. "selectional pressure" = a named value ruling out some candidates (e.g. a naval object selecting greer/degreer for 56).

## Bar (verbatim from queue `bars` field)

"name 37's value iff one value holds across the A1 predicative frames; state the selectional consequence for 56's object slot (e.g. a naval object selects greer/degreer)"

Restated as numbered pass/fail clauses before testing:

1. **C1:** one value for 37 holds across the A1 predicative frames — and is named at battery grade.
2. **C2:** the selectional consequence for 56's object slot (@795/@1658) is stated.
3. **C3 (adverse):** 37's value naming is entangled with queued `frame-37-reexam` (red-team venue) — fence, do not adjudicate.

The iff-structure: C1 fires only if a nameable value exists. C2 fires only if C1 named one.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/sel-37-pressure.lock` (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All asserts held (1,847 pairs, 96 types, n(37)=28).
3. Standing premises used, not re-litigated: banked pencil 11=la/70=pre/82=m/34=i/29=er/40=e/46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional 59=est, 77=le; A1 predicative grant for 37 (class open); §7 (67 et/veut sole true polyvalence).
4. Surveyed prior 37-value work instead of duplicating it: `enterre-37re-s5` KILL (2026-10-09), `s5-rival-five-windows` NULL (2026-10-08), `frame-37-reexam` verdict null (red-team venue), `x-33-37-licensing` PROMOTE (2026-10-09).

## Window-level evidence

The A1 predicative frames for 37 are the "est(59) 37" windows — six, byte-exact:

- **@529** (a3_00): `97 47 44 | 59 37 | 64 26` = "…ce [44] est [37] qui [26]…"
- **@625** (a4_01): `82 14 59 | 37 33 29 | 87 78` = "…[14] est [37] [33]er ce [78]" — adopted battery premise (x-33-37-licensing PROMOTE): 37 nominal, infinitive self-licensed ("Laisser ce [78]!").
- **@913** (a5_09): `64 83 59 | 37 96 | 09 02` = "…qui [83] est [37] par [09]…"
- **@1179** (a6_10): `48 59 | 37 77 | 78 94` = "…[48] est [37] le [78]…"
- **@1444** (a7_09): `52 68 59 | 37 64 | 77 84` = "…[68] est [37] qui le [78]…" — adopted: "est [37] qui" cleft forces the nominal arm (x-33-37-licensing).
- **@1797** (a8_10): `94 59 | 37 91 | 79 87` = "…est [37] [91] tout…".

### C1 — FAIL (no value nameable at battery grade)

Two independent grounds, both sufficient:

**Ground 1 — uniformity broken.** Two of the six A1 frames force the nominal arm for 37:
- @529 and @1444 are "est [37] qui" clefts. Under the adopted battery premise, *"c'est [adj] qui"* is ungrammatical in every period — the cleft forces 37 nominal. (x-33-37-licensing, adopted.)
- @625 was battery-promoted as 37-nominal ("est [37-N]" closing its clause; the infinitive is self-licensed).
- So at least 3/6 "est 37" frames do NOT admit a predicative-adjective reading. No single predicative value can "hold across the A1 predicative frames" because the frame set itself is not uniformly predicative. This is an independent distributional result, not a re-litigation of any standing verdict.

**Ground 2 — no surviving candidate.** The only ever-named value candidate for 37 is 're':
- `enterre-37re-s5` (2026-10-09) KILLED uniform 37='re' at kill grade: @676 ("64 37 77" = "qui re le ce") admits no grammatical parse under 37='re' + standing values; the sole rescue needs 77≠'le' against the provisional 77='le' standing value. The kill's re-open condition (77≠'le') has not fired.
- `s5-rival-five-windows` (2026-10-08) returned NULL: no single rival value parses all five S5 windows ("tout V", "V la" ×2, "V qui" ×3) grammatically — and its headline notes the bar itself is unachievable because @51's "la tout" bigram is kill-grade ungrammatical independent of 37's value.
- No other value for 37 exists anywhere in the lane's reports. Under the lane's naming standard (compatible-not-forced is not a name), inventing a value here would be invention under §3.

C1's iff-antecedent ("one value holds across the A1 predicative frames") is not met. C1 does not fire.

### C2 — does not fire

C2 is conditional on C1 naming a value. No value was named, so no selectional consequence for 56's object slot (@795 "qui [56] [37]", @1658 corroborating "[56] [37]") can be stated at battery grade. The claim's example consequence — a naval object selecting greer/degreer from the 56 Xéent candidate set {créer, agréer, suppléer, recréer, gréer, dégréer, procréer, maugréer} (valency-56-wide NULL, 2026-10-09) — remains a hypothetical: it would fire if 37 ever names as a naval object, but 37 is currently neither named nor class-forced at @795/@1658 (its role there is the object/predicative-complement slot, class open).

### C3 (adverse) — honored

`frame-37-reexam` holds verdict null (red-team venue). This battery does not adjudicate it: no value named, no class claimed, the A1 grant itself not re-opened (the uniformity break is a distributional observation about the six "est 37" windows, stated as fence-grade evidence, not as a verdict on the frame). The global predicative/nominal split for 37 stays §7 red-team venue. R5005, sealed gates, red-team adjudication queue untouched.

## Verdict: NULL

No value for 37 is nameable at battery grade: the frame set is not uniformly predicative (clefts force nominal at 2–3 of 6 "est 37" windows) and the only named candidate (37='re') is kill-grade dead with its re-open condition unfired. The selectional consequence for 56's object slot cannot be stated. This verdict contradicts no standing verdict and downgrades none; §7 intact. Canonical-stream caveat stands (rows a3_00/a4_01/a5_09/a6_10/a7_09/a8_10 offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `sel-37-nominal-1179` (P3) — test 37's class at @1179 ("est [37] le [78]"): does the remaining non-cleft, non-@625 "est 37" window also force nominal? Bar: name 37's class at @1179 at battery grade, or fence with stated cause.
2. `val-37-newwindow` (P3) — lexical search for an adjective value parsing the predicative-shaped 37 windows (@913, @1179, @1797) without colliding with the forced-nominal clefts @529/@1444. Bar: one value parsing all three with zero kill-grade contradictions; kill iff none exists (names value, does not reopen the clefts).
3. `sel-56-795-gated` (P4) — gated: once 37's value is named at @795/@1658 (class or value), re-run the selectional-pressure bar for 56's object slot against the 56 Xéent candidate set. Do not dispatch until the gate fires.

## Bookkeeping

- Queue: `sel-37-pressure` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/sel-37-pressure.lock` created on start, deleted on completion (verified gone).
