# Battery A1 — predicative-adjective frame battery over {37, 32, 42, 19}

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Sources: finder P2/P3 (next-token-findings-qui.md), finder §3
(next-token-findings-parle-and-rest.md), parent queue P3 (32) / P4 (19).

## Pre-registered bar (written BEFORE touching data)

For each X in {37, 32, 42, 19}, test the reading "X = predicative adjective
(or past participle) after 'est'".

- **PROMOTE** X as predicative iff ALL hold: (a) ≥2 independent "est X"
  windows (est=59 conditioned frame; independent = non-overlapping positions,
  not the same window viewed twice); (b) X's successor slots are
  adjective-compatible in ≥2 windows (followed by 48/94-class clitic/prep
  slot, a verb, or an infinitive frame like @624's 37-33-29); (c) ZERO
  windows requiring a non-adjective reading of X in the "est X" frame
  (e.g. X clearly nominal with article force, or verbal with subject).
- **HOLD** if single-leg, or legs are mixed/neutral with no contradiction.
- **KILL** if any "est X" window requires a non-adjective parse, or the
  frame count drops below claimed (phantom legs).
- **SAME-OR-DISTINCT** for any X/Y pair: no merge without the
  {33,86}-precedent standard (joint frames + distribution test). A shared
  successor alone is NOT a merge leg.
- **Frame-vs-value discipline:** this battery constrains the *frame*
  (what syntactic slot X occupies), not X's plaintext value. Promoting the
  frame ≠ promoting a value; values need their own ≥2 independent legs.
- Kill-grade check on 19's leg count: parent's "follows est ×2" vs the
  finder's CORRECTION that @1774/@1776 are one physical window — re-derive
  19's est-leg count from the stream myself.

## Data

### Leg counts (re-derived from the stream, not the finders)

| X | est→X bigram positions | n | est-frame legs |
|---|---|---|---|
| 37 | 528, 624, 912, 1178, 1443, 1796 | 6 | 6 + "n'est 37" @1795 (negated arm) |
| 32 | 316, 448, 1210 | 3 | 3 |
| 42 | 463, 1186 | 2 | 2 |
| 19 | 1777 | 1 | **1** — finder's CORRECTION confirmed: @1774/@1776 are one physical window ("en ce qui" view vs "qui" view). Parent's "×2" is retired. |

### Window audits

**37 (n=28 corpus-wide; est-pre 6/28, top predecessor):**
- @528: est 37 64 26 — "est [37] qui [26]" (adj + relative, grammatical)
- @624: est 37 33 29 — "est [adj] [inf]er" (adj + infinitive: "est nécessaire de [faire]"-shaped; 33=INF class)
- @912: est 37 96 09 — "est [37] par [09]"
- @1178: est 37 77 78 — "est [37] le [78]"
- @1443: est 37 64 77 — "est [37] qui le [77]"
- @1796: est 37 91 79 — "est [37] 91 79"
- @1795: 42-94-59-37 — "n'est [37]" (negated est-arm; banked un-fenced in contexts.json)
Successors of 37 globally: 78×4, 43×3, 64×3, 01×3, 11×2, 77×2, 08×2 — all
verb/infinitive/que-class/pronoun slots; zero noun-requiring frames.
No "est 37" window requires a non-predicative parse.
**Compositional note (not a kill):** @179's 23-37-06 ("en ce qui [23]-37-06")
re-uses 37 in a verb-shaped word. If 37 is a "cer/cern" syllable, the
adjective frame ("certain") and the verb frame ("concerne(nt)") interlock
naturally — syllable polyvalence, not homophony. Flagged as a value-battery
lead, not litigated here.

**32 (n=13; est-pre 3/13, top predecessor):**
- @316: 64-59-32-94-06 — "qui est [32] ne…" ("est 32 94": 94=ne-class)
- @448: 61-59-32-48-79 — "est [32] [48]…"
- @1210: 64-59-32-48-96 — "qui est [32] [48] par…"
32→48 ×4 globally (top successor). The 94/48 post-predicate slot is shared
with 19 (@1777: 19-48) — class-level sharing, not merge-level.
@1209's "48-par" tension (48="à" rival) noted in the finder — held, not resolved.

**42 (n=20; est-pre 2/20):**
- @463: 79-87-11-59-42-96 — "tout cela est [42]…" (P1's strongest window extended)
- @1186: 06-06-59-42-06-84 — "est [42]…" (42→06 ×5 globally — compositional candidate "42-ent"?)
Meets the ≥2-leg bar exactly; no contradictions.

**19 (n=9; est-pre 1/9):**
- @1777: 24-87-64-59-19-48-74 — "en ce qui est [19] [48]…"
Single leg. 19's other 8 windows have diverse predecessors (01×2, 98, 90, 88, 10, 41, 09) —
no second predicative frame found.

### Corpus census (register check, code/side-period/corpus/)
"est [adj]" predicative frames in the 1841 diplomatic corpus: vrai 49,
nécessaire 19, possible 18, certain 15, évident 14, difficile 10,
important 6, juste 3; "il est évident/possible/nécessaire" ×7 each.
The predicative-adjective slot after "est" is register-typical — the frame
claim is plausible French, not a cipher artifact.

### F71 est-arm reconciliation (supplement to ANOMALIES.md)
94→59 bigrams re-derived: @558, @762, @1795 (all three banked as "n'est" in
contexts.json, none fenced). est-arm = **7** (64-59×3 + 94-59×3 + 93-59×1),
not F71's 6/6. All three 94-59 windows are frame-compatible ("n'est [30/39/37]").
F71's count is corrected; no re-litigation of 59's conditioned value.

## Verdicts

- **37: PROMOTE frame** — predicative slot after "est", 6 independent legs
  (+1 negated leg @1795). Strongest adjective-frame group in the lane.
  Value NOT promoted (the "cer/cern" interlock is a lead for a value battery).
- **32: PROMOTE frame** — predicative slot after "est", 3 independent legs.
  Value NOT promoted.
- **42: PROMOTE frame** — predicative slot after "est", 2 independent legs
  (bar met exactly). Value NOT promoted. Weakest of the three promotes —
  named as such for the red team.
- **19: HOLD** — single est-leg; predicative frame plausible but unconfirmed.
  Needs a second independent "est 19" (or "n'est 19") window to promote.
- **Same-or-distinct:** NO merges. 32/19 share the 48-successor slot
  (class-level); 37 never takes 48 directly in the est frame. The
  {33,86}-precedent standard is not met for any pair — all stay distinct.
- **F71 supplement:** est-arm = 7; the miscount is corrected with evidence.

## New leads queued
- L1: 37's syllable value ("cer/cern" interlock: "certain" × adjective frame,
  "concerne(nt)" × verb frame @179). Value battery target.
- L2: 42→06 ×5 compositional ("42-ent"?).
- L3: @1209 "32-48-par" tension for the 48 battery.
