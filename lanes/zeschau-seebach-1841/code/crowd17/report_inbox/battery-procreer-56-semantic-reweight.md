# Battery report: procreer-56-semantic-reweight — verdict: PROMOTE

- Target id: `procreer-56-semantic-reweight` (P3)
- Claim: "Re-score the 8-way Xéent tie at @1745 with the Littré-absolute advantage removed per this fence."
- Date: 2026-10-09
- Worker: battery worker (subagent 5d686d70-54ba-454e-9e2f-9cb74845fa3a; clean re-dispatch — prior worker died on daemon restart with no report and no queue change)
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/procreer-56-semantic-reweight.lock` created on start (agent id + UTC timestamp), deleted on completion.

## Bar (verbatim, pre-registered)

"Re-score the 8-way Xéent tie at @1745 with the Littré-absolute advantage removed per this fence."

Numbered clauses (frozen before testing, not modified after):

1. C1 — re-score all 8 Xéent candidates against the @1745 objectless frame ("que Xéent [65]") with procréer's Littré-absolute advantage removed (its absolute use is unattested in the period corpus per the fence; score it as the v.a. it is).
2. C2 — state the resulting tie structure: does the tie break, restructure, or stand as before?

## Method

1. Read BATTERY-PROTOCOL.md in full before testing; created lock on start.
2. Re-derived @1745 byte-exact on the repaired stream (0-based): `...94 82 46 |56| 40 06 65...` (row a8_08) = "ne m que [56]e-ent [65]" — matches the parent's locus exactly.
3. Adopted as premises (not re-litigated): the 9-verb closed inventory and réer kill from `xeent-register-tiebreak` (2026-10-09); the Littré register/valency table (créer/agréer/suppléer/recréer v.a., gréer/dégréer v.a. "Terme de marine", procréer v.a. "Engendrer" + "Absolument", maugréer v.n.); the 3pl-form corpus counts (créent 9–10, suppléent 5, agréent 1, all others 0 in ~32M chars); the fence from `procreer-absolute-corpus` (2026-10-09): **5 stem tokens in 4 files of the 77-file / ~34.5M-char period corpus — 2 nouns, 3 verb forms, all 3 transitive; 0 absolute (objectless) uses.**
4. Re-scored on valency-fit at the objectless frame only (the advantage's locus). No new corpus work; no value named.

## Findings — the re-scored table

The parent's `procreer-56-semantic` C2 gave procréer a gradient-fit advantage on the objectless frame: Littré's "Absolument" licensed "que procréent [65]" better than the strictly-transitive rivals (créer, recréer, gréer, dégréer) — "a gradient advantage, not a discrimination (shared with maugréer/agréer/suppléer)". The fence removes it: procréer is now scored as a plain v.a. in an objectless frame, with no absolute-use license live in the period register.

| Candidate | Littré | Objectless-frame capacity (post-fence) | 3pl corpus form | Tier |
|---|---|---|---|---|
| maugréer | v.n. | natural (intransitive) — unchanged | 0 | A |
| agréer | v.a. (+intr. use) | licensed — unchanged | 1 | A |
| suppléer | v.a. (+ "suppléer à") | licensed — unchanged | 5 | A |
| créer | v.a. | unlicensed absolute; objectless = ellipsed-object strain | 9–10 | B |
| procréer | v.a. ("Absolument" in Littré) | **absolute fenced 0/34.5M — DEMOTED to tier B** | 0 | B |
| recréer | v.a. | unlicensed absolute; ellipsed-object strain | 0 | B |
| gréer | v.a., Terme de marine | same strain + nautical strain | 0 | B |
| dégréer | v.a., Terme de marine | same strain + nautical strain | 0 | B |

- C1: PASS — re-score complete. Procréer drops from tier A to tier B. It is now no better than créer on the @1745 frame — and strictly worse on attestation (créer "créent" ×9–10 vs procréer 0).
- C2: PASS — the tie does NOT break (no candidate separates uniquely), but it restructures from 8-flat to **3-vs-5 tiered**: {maugréer, agréer, suppléer} retain objectless capacity; {créer, procréer, recréer, gréer, dégréer} all carry the same objectless strain for a v.a. verb. Within tier B, créer leads on form attestation; procréer/recréer/gréer/dégréer are unattested; gréer/dégréer keep the nautical strain.

## Scope

Re-scoring only; no kill, no value named, no polyvalence declared. The demotion is valency-fit at the @1745 objectless frame — it does not touch @795 ("qui [56] [37]" is a transitive frame; the absolute fence is irrelevant there) or @1626 (parse-1626-clause's venue). maugréer's v.n. standing is the `valency-56-wide` / `valency-maugreer-56` venue, not re-litigated. No standing/red-team verdict contradicted; §7 intact. No follow-ups per §4 (promote).

## Bookkeeping

- Queue: `procreer-56-semantic-reweight` → status `verdict`, result `promote`, date 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/procreer-56-semantic-reweight.lock`: created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched. No numbers invented: @1745 byte-derived in-session; all corpus/Littré figures cited from the named parent batteries.
