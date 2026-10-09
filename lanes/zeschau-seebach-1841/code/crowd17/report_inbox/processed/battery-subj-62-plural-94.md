# Battery report: subj-62-plural-94 — verdict: KILL

**Target:** `subj-62-plural-94` — "Test 62 as plural subject across the 62-94 x9 windows."
**Worker:** subagent b66affad-1308-4ae7-a5c1-5ac79c5e8fb3. **Date:** 2026-10-09.
**Stream:** repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs verified in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched. Lock created on start (agent id + UTC timestamp); deleted on completion.

## Bar (verbatim, pre-registered before testing)

"Kill iff any window forces singular."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** All nine "62 94" windows identified byte-exact on the repaired stream.
2. **C2:** KILL iff ≥1 window forces 62 singular — i.e. the only grammatical parse under standing values has 62 as a singular nominal (3sg agreement with 62 as subject or as relative antecedent).
3. **C3:** Listed adverses answered (adverses: null; the evidence-field tension — "62-98 x5 needs 62 singular-compatible (98='vient' 3sg)" — is addressed below).

## Standing premises used (not re-litigated)

- 94="ne" (battery-promoted); 64="qui" (granted); 98="vient" 3sg (battery-PROMOTED, vient-98-name — pending red team, usable at battery grade); 59="est" (provisional, 3sg); 56 finite verb, bare-56 = 3sg per the promoted stem-56-whole inflection model; 86 INF-class (A9).
- 62="il" kill-grade dead globally (class-62-fullcensus; sel-62-48-94 KILL); 62="on" unconditioned killed (collision-62-84). 62's value/class otherwise open.
- French grammar: a relative "qui" takes the nearest compatible nominal antecedent in unmarked construction and agrees with it in number; "ils … qui vient" (3sg) is ungrammatical in every period.

## Window-level evidence (0-based @-offsets, repaired stream)

C1 PASS: n(62-94) = 9, byte-exact: @100, @508, @761, @840, @1329, @1362, @1686, @1704, @1772.

- **W1 @100** (a1_02): `21 62 94 93 59 45 28 00` — "…[21] 62 ne [93] est(59) [45]…pour(00)". 93 fully open; a 3pl 93 ("ils ne [93-pl]") is conceivable and 59's "est" is provisional. No kill-grade force. → compatible.
- **W2 @508** (a3_00): `…68 21 67(et) 77(m') 62 94(ne) 64(qui) 98(vient) 65 88 56…` — **FORCES SINGULAR.** The relative "qui" (granted) needs a nominal antecedent; the nearest preceding nominal is 62 (77 is a clitic, 67 is "et"). "vient" is promoted 3sg, so the antecedent must be 3sg → 62 is singular here. Under the claim (62 = "ils"), "ils … qui vient" is ungrammatical. Escape via antecedent = 21/68 across the intervening nominal 62 violates unmarked relative attachment (no comma, no marking). Second independent leg: the matrix finite verb 56@514 is bare → 3sg-shaped per the promoted inflection model; a plural "ils" cannot govern it. → **kill-grade force.**
- **W3 @761** (a5_03): `20 62 94 59 39 88 66` — "62 ne est(59) à(39) [88] [66]". Under 62="ils" + provisional 59="est": "ils ne est" is ungrammatical → singular-leaning (provisional-dependent, supporting only).
- **W4 @840** (a5_06): `20 62 94 26 12 16 00` — no finite verb available for 62; no force. → compatible.
- **W5 @1329** (a7_04): `06 62 94 70 52 39 83 86` — 86 INF-class; no finite verb for 62. → compatible.
- **W6 @1362** (a7_06): `92 62 94 79 14 60 03 30` — 60 finite but its form at this window is unnamed. → compatible.
- **W7 @1686** (a8_05): `93 62 94 79 14 60 27 46` — same shape as W6. → compatible.
- **W8 @1704** (a8_06): `20 62 94 88 26 12 06` — the finite-88-ne locus: the unique grammatical parse is the fused 3pl "[88-26]nent" ("[62] ne [88-26]-nent"), which NEEDS a plural subject. → supports plural here. **Tension noted:** @1704 wants plural 62 while @508 forces singular 62 — no uniform number holds across the nine windows; that is a conditioned-split question, red-team venue (redteam-62-conditioned still queued; §7 bars a battery-level polyvalence declaration).
- **W9 @1772** (a8_09): `78 62 94 24 87 64 59 19` — "62 ne [24] ce(87) qui(64) est(59)": "est" agrees with "ce", not 62; 62's own verb absent. → compatible.

**C2 FIRES** — W2 @508 forces singular at kill grade. **C3** — the evidence-field tension (62-98 x5 vs plural) is out of this target's scope (those are 62-98 windows, not 62-94), and is consistent with the @508 finding rather than contradicted by it.

## Verdict: KILL

The uniform "62 = plural subject" claim across the 62-94 windows is false: @508 forces 62 singular ("…[62] ne qui(64) vient(98-3sg)…" — 3sg relative agreement with 62 as nearest antecedent). The @1704/@508 number tension further shows no uniform number reading survives; naming 62's conditioned behavior is red-team venue (redteam-62-conditioned queued, untouched). No standing/red-team verdict contradicted or downgraded (98="vient" promote used as premise, not re-decided); §7 intact. Canonical-stream caveat stands (row offsets unvalidated).

Per §4, kills regenerate no follow-ups. Flag for red team: the @1704 (plural-forcing) vs @508 (singular-forcing) pair is input to the queued redteam-62-conditioned decision.

## Bookkeeping

- Queue: `subj-62-plural-94` → status `verdict`, result `kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/subj-62-plural-94.lock` created on start, deleted on completion (verified gone).
