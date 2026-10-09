# Battery `ent-er-residual` — resolve "06 29 67" @1097/@1389 and "06 29 37" @1816

## Bar (verbatim, pre-registered)

`test 06≠"-ent" at these windows vs an "er…"-word whose second syllable is 67/37`

Restated as numbered pass/fail clauses:
1. At @1097/@1389 ("06 29 67", rows a6_06/a7_07): either 06≠"-ent" parses, or an "er"-word with second syllable 67 parses — else the residual stands fenced.
2. At @1816 ("06 29 37", row a8_10): either 06≠"-ent" parses, or an "er"-word with second syllable 37 parses — else the residual stands fenced.
3. No standing verdict contradicted or downgraded; 67's sole-polyvalence standing and 37's S5 ownership respected (no value named for 37, no polyvalence declared).

## Method

Read BATTERY-PROTOCOL.md first; created/deleted `locks/ent-er-residual.lock` per protocol. Re-derived the full stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (1,847 pairs / 96 types verified; `canonical.py` never touched; R5005, sealed gates, red-team queue untouched). The trigram "06 29 67" occurs exactly twice (0-based @1096/@1388 = 1-based @1097/@1389); "06 29 37" exactly once (0-based @1815 = 1-based @1816). Standing values used: 06='ent' (promoted), 29='er' (ground truth), 67='et'/'veut' (sole polyvalence, §7), 37 open (S5-owned), 86=INF class, 42=noun class. 1841 diplomatic French throughout.

Windows (0-based @, ±8):
- @1096 (a6_06): `33 79 80 06 43 07 55 81 | 06 29 67 | 86 52 82 94 74 47`
- @1388 (a7_07): `69 13 24 65 68 52 82 16 | 06 29 67 | 86 29 89 16 76 47`
- @1815 (a8_10): `52 80 04 61 15 93 50 42 | 06 29 37 | 01 02 09 19 00 97`

## Clause 1 — @1097/@1389 ("06 29 67"): NEITHER ARM PARSES — residual stands

**Arm B ("er"-word, second syllable 67): KILLED at lexical grade.** 67's standing values are 'et'/'veut'. "er"+"et" = "eret" and "er"+"veut" = "erveut" are not French words. No other value for 67 is available at battery level (§7: 67 et/veut is the sole true polyvalence; re-valuing 67 is a red-team act).

**Arm A (06≠"-ent"):** no grammatical parse found under any tested variant:
- 06='ent' word-internal: "…[81]enter[et]" / "…[16]enter[et]" — no French word ends in "-enter" or "-enteret", for any stem (81/16 values open but the ending is impossible regardless).
- 06='en' (preposition): "…[81] en er[et]" — still requires "eret"/"erveut" ✗ (same lexical kill).
- 67='veut' (follower 86 is INF-class, positional rule may fire): "…[81]enter veut [86]" — "veut [infinitive]" is grammatical ("veut voir"), but the left edge "…[81]enter" still fails ✗.
- 29 word-final ("…[81]-ent-er"): "[81]enter" ✗ (same ending impossibility).

Exhaustive segmentation check (06/29/67 = 'ent'/'er'/'et'-family): every boundary placement leaves a non-word ("ent", "er", "eret", "enter", "enteret"). **The @1097/@1389 residual is genuine and stays fenced.** Its only escapes are a red-team re-valuation of 67 or of 06 — neither available at battery level.

## Clause 2 — @1816 ("06 29 37"): ARM A VIABLE (CONDITIONAL) — "enterre" lead

**Arm A (06≠"-ent"-suffix) parses conditionally:** `…[42] | 06 29 37 | [01]…` = "…[42] **enterre** [01]…" — 3sg present of *enterrer* ("the [42] buries [01]").
- Spelling is byte-exact: 06('ent') + 29('er') + 37('re') = "enterre" ✓.
- 06 keeps its promoted value 'ent' but is word-internal, NOT the 3pl suffix — satisfying "06≠'-ent'" in the suffix sense the residual assumed.
- Precedent: @1710 "12 06 29 40" = "n'enterre" (profile-29-left), where 06='ent'+29='er' likewise sit word-internally; here 37='re' spells the ending more cleanly than that battery's 40='e'.
- Conditions (ungranted): (i) 37='re' — 37's value is S5-owned and open, NOT decided here; (ii) 42 is a complete word (42=noun class, value open); (iii) 01 is a grammatical object (open).
- Note the tension for S5/red team: 37='re' must cohere with "37 78" x4 (promoted infinitive unit, 78 word-final) and "59 37" x6 / "64 37" x3 — "est re…"/"qui re…" do not work word-initially there, so 37='re' would need positional conditioning or lose. This is S5's call.

**Arm B ("er"-word, second syllable 37):** also conditionally viable — "erreur" (37='reur'), "erre"/"errer" (37='re'/'rer') are all real words — BUT it requires 06='en' (preposition, re-valuing promoted 06='ent') for 29 to be word-initial ("…[42] en erreur…"), a strictly stronger claim than Arm A's. Arm A wins on parsimony.

## Clause 3 — standing untouched: PASS

No standing verdict contradicted or downgraded. 67's polyvalence intact (Arm B's kill uses it, does not revise it). No value named for 37. No polyvalence declared (§7). No escalation of a standing red-team grading.

## Verdict: NULL (fence + conditional lead)

- @1097/@1389: Arm B killed at lexical grade ("eret"/"erveut" not French); Arm A yields no parse. Residual stands fenced — a hard residual requiring red-team re-valuation of 67 or 06 to dissolve.
- @1816: Arm A yields the only grammatical parse ("…[42] enterre [01]…", 3sg *enterrer*), conditional on 37='re' (S5-owned, open). Lead, not promotion — recorded for S5/red-team adjudication, not banked here.

## Follow-ups proposed (for supervisor queuing)

1. `enterre-37re-s5` (P2): test 37='re' — coherence across @1815 ("enterre"), "59 37" x6, "64 37" x3, "37 78" x4 (infinitive unit). Coordinate with S5; 37's value is S5/red-team's to decide. If 37='re' holds, @1816 resolves and Arm A (06≠'-ent'-suffix) promotes at this window.
2. `resid-1097-1389-escalate` (P2): escalate the @1097/@1389 hard residual to the red team — exhaustive segmentation under standing values yields no parse; dissolution needs 67 or 06 re-valuation.
3. `67-internal-sweep` (P3): stream-wide distributional test — is 67 EVER word-internal (67's left neighbors: 21 x8, 06 x3, 20 x3, 40 x3, …)? Decides Arm B ("er"-word with 67 as second syllable) globally rather than per-window.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ent-er-residual.md`
- `battery-queue.json`: `ent-er-residual` queued → verdict/null (temp-file + rename, own entry only, pre-write assert confirmed no prior verdict, JSON re-validated).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- Prior worker note: a previous worker for this target died in a runtime restart before producing anything; its lock was cleared before this clean re-run. No partial state was inherited.
