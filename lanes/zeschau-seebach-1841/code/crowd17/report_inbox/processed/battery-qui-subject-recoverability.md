# Battery report: qui-subject-recoverability

- Target id: `qui-subject-recoverability`
- Claim: "census antecedent recoverability across all 47 qui-windows; methodology check on the agreement-lexicon route."
- Date: 2026-10-09
- Worker: battery worker (subagent 3c405bff-3bda-4258-89a7-794065df095f)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "antecedent" = the noun phrase the relative "qui" refers to. "Recoverable" = the antecedent is named by a standing value or granted frame with zero new assumptions. "Left-adjacent" = the token directly before "qui". "Cleft" = "c'est X qui" shape. All @-offsets 0-based.

## Bar (verbatim, pre-registered before testing)

"record the recoverability rate with byte evidence; does not decide any 41 value."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** n(64)=47 verified byte-exact on the repaired stream, every window censused with left/right context.
2. **C2:** each window classified RECOVERABLE / PARTIAL / BLOCKED with byte evidence, and the recoverability rate recorded.
3. **C3:** the methodology implication for the agreement-lexicon route is stated; no 41 value is decided.

Adverses listed: "methodology battery - records the rate even if low; does not decide any 41 value."

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/qui-subject-recoverability.lock` (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. n(64)=47 confirmed byte-exact.
3. Standing premises used, not re-litigated: pencil GT (11=la, 82=m, 34=i, 29=er, 40=e, 46=que, 70=pre); granted 64=qui, 87=ce, 47=ce (A4), 17=fois, 96=par, 79=tout (A5), 00=pour (A9), 84=on (A15); provisional 59=est, 77=le; registry class 65=noun (R18); battery-promoted 69 nominal-class (class-69-nominal), 78 nominal-class (x-33-37-licensing distributional leg); A1 predicative frames 37/32/42; cleft finding "est 37 qui forces 37 nominal at @529/@1444" (x-33-37-licensing); §7 (67 sole polyvalence).
4. Classification rule (battery grade, 0 new assumptions):
   - RECOVERABLE: left-adjacent token is a standing nominal (87=ce pronoun, 17=fois noun, 65 noun-class, 69 nominal-class, 78 nominal-class), or the window is a licensed cleft "est [37-nominal] qui".
   - PARTIAL: left-adjacent token has a granted class whose nominal arm is unvalued (37 predicative A1 outside a cleft).
   - BLOCKED: left context is verb/particle/preposition/conjunction with no licensed nominal, or the only nearby nominal cannot head a relative (e.g. 77=le pronoun, 84=on indefinite — "*le qui", "*on qui" ungrammatical).
   - Two corrections were made during review (not hidden): @791 "06 77 64" and @1666 "94 84 64" were first auto-flagged RECOVERABLE by left-adjacent nominal but downgraded to BLOCKED, because "le" and "on" cannot head a relative clause.

## Window census (all 47, 0-based)

RECOVERABLE (13):
- @18 (a1_00): "17 64" = "fois qui" — 17=fois noun antecedent.
- @149 (a1_04): "87 64" = "ce qui" — demonstrative-pronoun antecedent.
- @181 (a1_05): "87 64" = "ce qui".
- @1768 (a8_08): "87 64" = "ce qui".
- @1776 (a8_09): "87 64" = "ce qui".
- @1801 (a8_10): "87 64" = "ce qui". (Matches the "ce qui" x5 count of 87-left-attach-census.)
- @530 (a3_00): "59 37 64" — cleft, 37 nominal arm forced (x-33-37-licensing).
- @1445 (a7_09): "59 37 64" — same cleft shape.
- @725 (a5_02): "65 64" — 65 noun-class (R18 registry).
- @1209 (a7_00): "65 64" — same.
- @1341 (a7_05): "65 64" — same.
- @1079 (a6_05): "77 78 64" = "le [78] qui" — 78 nominal-class (x-33-37 battery leg).
- @1836 (a8_11): "69 64" — 69 nominal-class (class-69-nominal PROMOTE); "ce [69]" NP head.

PARTIAL (1):
- @1358 (a7_05): "52 37 64" — 37 predicative (A1) but not a cleft; nominal arm unvalued.

BLOCKED (33):
- Verb-adjacent: @32/@337/@675/@1646 ("03 64", verb-stem); @133 ("56 64"); @684/@1023 ("92 64", verb); @684-note; @144/@395 ("67 64"); @938/@1632 ("21 64"); @794 ("07 64"); @1337 ("71 64", split candidate).
- Particle/preposition: @510 ("94 64" = "ne qui"); @749 ("00 64" = "pour qui" — prepositional qui, no relative antecedent exists); @38/@608 ("39 64" = "à qui" — antecedent beyond window, fenced); @315/@341/@1025 ("45 64", 45="ce" is A11 HOLD — not a standing value at battery grade).
- Ungrammatical-nominal neighbor: @791 ("77 64", "*le qui"); @1666 ("84 64", "*on qui").
- Open classes: @290 ("09 64"), @486 ("19 64", 19 HOLD), @606 ("54 64"), @854 ("51 64"), @910 ("49 64"), @1199 ("16 64"), @1226 ("57 64"), @1271 ("20 64"), @1434 ("49 64"), @1587 ("70 64"), @1717 ("30 64").

## Per-clause pass/fail

- **C1 PASS.** n(64)=47 byte-exact; all 47 windows censused ±4 context above.
- **C2 PASS.** Rate recorded: **13/47 = 27.7% RECOVERABLE** at battery grade (all values standing or battery-promoted). Strict §7-standing-only rate (excluding 65/69/78 battery-grade items): **8/47 = 17.0%**. Loose rate including the single PARTIAL: **14/47 = 29.8%**.
- **C3 PASS.** Methodology implication: antecedent recoverability is LOW. The agreement-lexicon route cannot lean on most qui-windows — only the "ce qui" family (5), the two clefts, and the noun-adjacent windows (65 x3, 78, 69) carry licensed antecedents. 33/47 windows are blocked, most because "qui" sits next to a verb, particle, preposition, or open-class token. No 41 value decided; no standing/red-team verdict contradicted or downgraded; §7 intact.

Adverse answered: the rate is recorded even though low — that was the adverse, and it is honored, not evaded.

## Verdict: PROMOTE (methodology/census-level)

The census is complete and the rate is recorded with byte evidence. This promote is methodology-level only: it names no value and changes no class.

## Follow-ups proposed (promote needs none; the finding opens two narrow continuations — both verified absent from battery-queue.json)

1. `qui-38-608-aqui` (P3) — resolve the "à qui" windows (@38/@608): name the leftward antecedent or fence the frame.
2. `qui-45-hold-rerun-gated` (P4) — re-run the "45 64" windows (@315/@341/@1025) once the red team adjudicates the A11 "45=ce" hold.

## Bookkeeping

- Queue: `qui-subject-recoverability` -> status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/qui-subject-recoverability.lock` created on start, deleted on completion (verified gone).
