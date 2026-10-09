# Battery `boundary-760-combine` — verdict: NULL (fence stands, both causes stated)

- Target id: `boundary-760-combine` (P2)
- Claim: combine `boundary-760-20role`'s verdict with `val-66-767-frame`'s closed "est à" frame for the final @760 boundary call.
- Date: 2026-10-09
- Worker: battery worker (subagent 605f8218-2f2a-4ea1-97c5-db20e577d87a)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: all @-offsets are 0-based pair indices. Locus @760 = 20 on row a5_03.

Terms (ASD-STE100): "fence" = a route that is neither proven nor dead; the question is parked, not answered. "Bar" = the pass/fail test the battery must run. "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

> Bar: 20 clause-initial killed AND frame closed -> boundary forced after 20; any 20 role live -> fence stands with both causes stated. NOTE: dependency has landed (boundary-760-20role verdict/kill 2026-10-09: forced-after-20 dead, 3 clause-initial 20 roles live) — proceed directly, not gated.

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 20's clause-initial roles at @760 are killed AND the 'est à' frame is closed → the boundary is forced to fall after 20.
2. **C2:** Any 20 clause-initial role at @760 is live → the fence stands, with both causes stated.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/boundary-760-combine.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Read the two dependency reports in full from `code/crowd17/report_inbox/processed/`: `battery-boundary-760-20role.md` (verdict kill, 2026-10-09) and `battery-val-66-767-frame.md` (verdict null, 2026-10-09). Adopted their findings as premises; re-litigated nothing.
3. Re-derived the repaired stream in-session and independently re-checked every byte-level fact both reports rest on (see Window evidence). All asserts held.
4. Adopted standing premises, not re-litigated: §7 banked ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional 59=est, 77=le; 98='vient' battery-promoted; 67 et/veut sole polyvalence.

## Window evidence (byte-exact, 0-based, independently re-derived)

The @760 locus window (row a5_03, @748–773), confirmed byte-exact:

```
00 64 02 97 40 67 | 11 70 82 34 29 40 | 20 | 62 94 59 39 88 | 66 98 80 10 22 94 07 06
                                     @760  @761-765                @766-768
```

- `@760 = 20` confirmed. Right context `@761–765 = 62 94 59 39 88` ("il ne est à [88]"); follower `@766 = 66`, `@767 = 98`, `@768 = 80`.
- `"20 62 94"` trigram occurs exactly 3x stream-wide: @760, @839, @1703. Confirmed.
- `"20 62"` bigram exactly 4x: @760, @839, @1135, @1703. Confirmed.
- 20 census n=15 at @280 @307 @490 @642 @668 @703 @741 @760 @839 @873 @958 @1135 @1224 @1270 @1703. Confirmed.
- @1703 window (row a8_06): `... 85 33 94 30 | 20 62 94 88 26 12 06` — the adopted 'n'importe' confinement site. Confirmed.
- @839 window (row a5_06): `... 17 98 | 20 62 94 26 12 16 00`. Confirmed.
- `"62 94 59 39 88"` occurs exactly 1x stream-wide (@761). The 'est à' frame is a hapax. Confirmed.
- X-66-98 triple: 66-positions @87/@122/@765 ("88 66 98 80" at @765–768). Confirmed.

## Dependency findings (adopted, not re-litigated)

**Dependency A — `boundary-760-20role` (verdict: KILL).** Its bar: "every clause-initial role killed → boundary must fall after 20; any role live → the forced claim is dead." Outcome: C1 FAIL, C2 FIRES. Three clause-initial roles for 20 at @760 are **live**:
1. Particle face ('mais') — confirmed at battery grade by `particle-20-760-839` ("la première ; mais il ne est à [88] [66]…").
2. Relative-adverb face ('où'/'quand') — in-stream grammatical precedent at @1703 ("n'importe où/quand il ne [88]").
3. Clause-adverb face (ainsi/donc/cependant) — fenced-compatible at @760 per `adverb-20-wide`; a fenced route is a live route.

The forced-after-20 claim is dead. 20 can head the right clause under two battery-grade roles.

**Dependency B — `val-66-767-frame` (verdict: NULL).** Clauses C1–C3 PASS, C4 FAIL:
- C1/C2: 66's role at @767 named = nominal subject of 98='vient'; rivals killed at role grain.
- C3: the 'est à' frame closes — "62 94 59 39 88" reads "[il] [ne] [est] [à] [88-inf]", syntactically complete; 66 heads the next clause ("[66] vient [80]").
- C4 (boundary re-test): FAIL at non-kill grade — fence causes (a) 66's role: REMOVED by the naming; (b) negated-shape corpus strain: STANDS ("n'est à + inf" unattested in 32.5M side-period chars); (c) 20's fenced clause-initial roles: STANDS, owned by `boundary-760-20role` (then in flight, now resolved as live). The boundary hardens relatively; it is not forced.

## Per-clause results

- **C1: FAIL.** The first conjunct fails: 20's clause-initial roles at @760 are NOT killed — three are live (particle 'mais' battery-grade, relative-adverb 'où'/'quand' precedented, clause-adverb fenced). The 'est à' frame is closed (dependency B, C3), but "killed AND closed" requires both. The forced-after-20 branch cannot fire.
- **C2: FIRES.** At least one 20 clause-initial role is live — three are. The fence stands.

## Verdict: NULL (fence stands, both causes stated)

**Cause 1 (the 20 side):** per `boundary-760-20role` KILL, 20's clause-initial roles at @760 are live. The particle face ('mais') is battery-grade confirmed; the relative-adverb face ('où'/'quand') carries in-stream grammatical precedent at @1703; the clause-adverb face is fenced-compatible. 20 can head the right clause, so the boundary cannot be forced after 20. This cause alone is dispositive against forcing.

**Cause 2 (the frame side):** per `val-66-767-frame` NULL, the 'est à' frame closes ("62 94 59 39 88" = "il ne est à [88-inf]"; 66 subjects 'vient'), which removed one fence cause (66's role), but the negated-shape idiomaticity strain stands ("n'est à + inf" zero attestations in 32.5M side-period chars) and closure alone does not force the boundary while 20 can head the right clause. The closed frame strengthens the after-20 reading relatively; it does not license it absolutely.

No standing or red-team verdict is contradicted or downgraded: the parent fence from `adv-20-760-boundary` stands narrowed, not broken; §7 intact; no polyvalence declared. Canonical-stream caveat stands (68/70 row offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `nom-ellipsis-760` (P3) — test whether the "la première" nominalization-ellipsis premise is independently licensed at @754–759. All three live 20-roles share it as a load-bearing assumption; if the ellipsis is killed, all three roles collapse together. Bar: licensed iff a byte-grounded precedent exists for bare "la première" nominalization in the stream or 1841 French; else fence.
2. `fence-760-final` (P4) — formal terminal fence for the @760 boundary: record both stated causes as closed at battery grade with no remaining battery-grade discriminator. Bar: all discriminating avenues exhausted or queued elsewhere (est-a-neg-corpus P4, poly-20-docket queued) → fence recorded terminal, re-openable only if the red team adjudicates 20's value or the 59/94/39 standing changes.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-boundary-760-combine.md` (this file).
- Queue: `boundary-760-combine` queued → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/boundary-760-combine.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
