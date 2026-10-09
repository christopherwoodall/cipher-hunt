# Battery report: reinforced-head-frequency-comedy

- Target id: `reinforced-head-frequency-comedy`
- Claim: "test whether dislocated reinforced heads are genuinely rarer in comedy over a larger comedy sample (syntactic vs lexical locus of the fence)"
- Date: 2026-10-09
- Worker: battery worker (subagent c5aebcd1-8ca7-47a9-abb8-80f47c3e9f4c)
- Stream: not applicable — corpus frequency comparison against period French theatre, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause ("Celui-là, je le sauverai"). "Reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, ceux-ci), as opposed to bare tonic heads (cela, ceci, ça). "Bare exclamatory infinitive" = an infinitive used as an exclamation with no governor ("Moi, voler !"). "Syntactic locus" = the fence sits in constructional choice (heads do not dislocate). "Lexical locus" = the fence sits in licensing (heads dislocate but never license infinitives).

## Parentage

Follows the disloc-reinforced family: `disloc-demonstrative-drama-reinforced` (NULL, 41 reinforced-head-comma hits → 8 exclamatory candidates → 0 genuine in 2,969,582 chars of mixed drama) and `disloc-reinforced-comedy-extension` (NULL, 2 hits → 0 candidates in 465,531 chars of new Scribe/Labiche comedy). Both fenced the reinforced-head + bare-exclamatory-infinitive pairing at register level but left the locus open: is the comedy gap syntactic (heads do not dislocate) or lexical (heads dislocate but never license infinitives)? This battery runs the frequency comparison on a larger comedy sample against a clean drama sample.

## Bar (verbatim, pre-registered before testing)

"a frequency comparison locates the fence: syntactic (heads don't dislocate) vs lexical (heads dislocate but never license infinitives)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. Run the same P1/P2/P3 taxonomy as the parent census on a larger comedy sample and a clean drama sample; report dislocation rates (P1 hits per 100k chars), dislocation propensity (P1 per reinforced head), and genuine bare-exclamatory-infinitive counts in each register.
2. If the dislocation rate is significantly lower in comedy (exact binomial two-sided test, α=0.05) → the fence has a syntactic locus component (heads dislocate less in comedy).
3. If dislocation rates are statistically indistinguishable but the bare-exclamatory-infinitive shape is absent in both registers → the fence is lexical (heads dislocate but never license infinitives), register-independent.
4. The comparison must decompose the rate difference (head base rate vs dislocation propensity) so the locus is not misattributed.

## Method

1. Read BATTERY-PROTOCOL.md first. Created lock `code/crowd17/next-token/locks/reinforced-head-frequency-comedy.lock` on start (agent id + UTC timestamp, no stale lock existed); deleted on completion.
2. Genre sets (period French theatre only, one edition per play; duplicate `hugo-hernani.txt` excluded per the parent gate note):
   - COMEDY (19 files): labiche-* ×13, scribe-* ×5 (bertrand-et-raton, charlatanisme, le-lorgnon, le-savant, verre-d-eau), musset-comedies-proverbes-1850 ×1.
   - DRAMA (19 files): delavigne-* ×3, dumas père ×6 (antony, dame-camelias, henri-iii, kean, mariage-louis-xv-1841, tour-de-nesle), hugo ×7 (angelo, burgraves, hernani-1870, lucrece-borgia, marie-tudor, roi-samuse, ruy-blas), vigny-chatterton-1835, musset-lorenzaccio, ponsard-lucrece.
3. Ran `code/crowd17/next-token/reinforced_head_frequency_comedy_census.py` — same P1/P2/P3 taxonomy as the parent: P1 `DEM_REINF\s*[,;:]` (window through next [!?.], cap 180 chars); P2 window must contain "!"; P3 infinitive-ending regex with MANUAL classification. Also counted raw reinforced heads (no comma) per file for the propensity metric. Raw JSON: `code/crowd17/next-token/reinforced-head-frequency-comedy_census.json`.
4. Exact two-sided binomial test on counts with exposure-proportional null (implemented from scratch, verified against the closed form).

## Window-level evidence

### Census yields

| register | chars | reinforced heads | P1 (dislocated) | P2 (exclamatory cand.) | genuine |
|---|---|---|---|---|---|
| COMEDY | 2,538,042 | 134 | 23 | 8 | 0 |
| DRAMA | 2,990,590 | 166 | 46 | 7 | 0 |
| TOTAL | 5,528,632 | 300 | 69 | 15 | 0 |

Dislocation rate: comedy 0.906/100k chars vs drama 1.538/100k chars. Exact binomial two-sided p = **0.0398** (23/69 hits on 45.9% of exposure) → significant at α=0.05.

Dislocation propensity (P1 per head): comedy 17.2% vs drama 27.7%. Exact binomial two-sided p = **0.0688** → not significant at α=0.05 (marginal).

Head base rate: comedy 5.28/100k vs drama 5.55/100k — essentially identical. The dislocation deficit is NOT a head-frequency artifact.

### Comedy P2 candidates — all 8 classified with cause (0 genuine)

1. `labiche-baron-fourchevif.txt` @43030 — "ceux-là, on ne les coupe jamais !" Finite clause ("on ne les coupe jamais"), no infinitive. Excluded.
2. `labiche-misanthrope-auvergnat.txt` @1374 — "celui-là, il vit tout seul, dans des endroits noirs, comme un colimaçon !" Finite. Excluded.
3. `scribe-bertrand-et-raton.txt` @110103 — "ceux-là, et, s'il fallait les perdre ou les voir compromis… j'aimerais mieux mourir !" Infinitives present but all governed: perdre/voir governed by conditional "fallait", mourir governed by "aimerais mieux"; "!" terminates the conditional clause, not a bare infinitive. Excluded.
4. `scribe-verre-d-eau.txt` @36952 — "ceux-là, je ne suis pas libre de les accueillir… je ne puis le voir sans exciter la défiance et les plaintes des nouveaux !" accueillir governed by "libre de", voir by "puis", exciter by "sans". All preposition/modal-governed. Excluded.
5. `scribe-verre-d-eau.txt` @124330 — "celui-là, j'en suis sûre…" Finite. Excluded.
6. `musset-comedies-proverbes-1850.txt` @2635 — "celle-ci, pleine de jeunes gens, de valets!" Nominal appositive, no verb. Excluded.
7. `musset-comedies-proverbes-1850.txt` @54850 — "celui-ci : Cordiani !" Vocative name. Excluded.
8. `musset-comedies-proverbes-1850.txt` @248302 — "celui-là : Je peux si je veux!" Finite. Excluded.

### Drama P2 candidates — all 7 classified with cause (0 genuine)

1. `dumas-henri-iii.txt` @33211 — "ceux-là, morbleu !" Interjection, no infinitive. Excluded.
2. `dumas-tour-de-nesle.txt` @20203 — "celui-là, il faut le sauver… Oh !" sauver governed by "il faut"; "!" is on "Oh". Excluded.
3. `hugo-marie-tudor.txt` @22918 — "celui-là, — et l'autre !" No verb. Excluded.
4. `hugo-marie-tudor.txt` @114547 — "ceux-ci, comme vous avez exterminé Tom Wyat…" Finite. Excluded.
5. `hugo-marie-tudor.txt` @135892 — "ceux-là, voyez-vous !" Finite. Excluded.
6. `musset-lorenzaccio.txt` @5819 — "celle-là ; et cependant Dieu sait si leur damnée de musique me donne envie de danser !" danser governed by "donne envie de". Excluded.
7. `musset-lorenzaccio.txt` @134263 — "celui-là : Je peux si je veux !" Finite. Excluded.

Near-miss profile is symmetric across registers: the only infinitive-containing windows in both registers carry governed infinitives (falloir / aimer mieux / libre de / pouvoir / sans / il faut / donner envie de) — no register asymmetry in infinitive richness.

## Per-clause pass/fail

1. Comparison run on 19 comedy + 19 drama files (5,528,632 chars), same taxonomy, all candidates hand-classified: PASS.
2. Dislocation rate significantly lower in comedy (0.906 vs 1.538 per 100k, p=0.0398): PASS — syntactic locus component confirmed. The bar's "heads don't dislocate" is too strong as stated (23 comedy hits exist), but the register-level syntactic deficit is real and significant.
3. Indistinguishable rates: does NOT hold (p=0.0398) — the pure-lexical arm as stated is rejected; however the "never license infinitives" leg IS register-independent (0 genuine in both registers over 5.53M chars). The fence is therefore two-legged: syntactic rarity in comedy + register-independent licensing ban.
4. Decomposition done: head base rates equal (5.28 vs 5.55/100k); the deficit sits in dislocation propensity (17.2% vs 27.7%, marginal p=0.0688), i.e. comedy playwrights use the heads but put them in topic position less often. PASS.

## Verdict: PROMOTE

The frequency comparison locates the fence. Dislocated reinforced heads are genuinely rarer in comedy (per-char rate 0.906 vs 1.538, p=0.0398) while reinforced heads themselves occur at equal rates in both registers (5.28 vs 5.55/100k) — a syntactic-register deficit in the dislocation construction, not a head-frequency artifact. The bare-exclamatory-infinitive shape is absent in both registers (0/5,528,632 chars), so the "never license infinitives" leg is register-independent. Caveat recorded: the propensity-given-head difference is marginal (p=0.0688); the comedy P1 sample (n=23) is small, so the exact locus share between constructional choice and chance remains open.

No value named; no registry change; §7 intact; no standing/red-team verdict contradicted.

## Bookkeeping

- Census script: `code/crowd17/next-token/reinforced_head_frequency_comedy_census.py`; raw JSON: `code/crowd17/next-token/reinforced-head-frequency-comedy_census.json`.
- Report: `code/crowd17/report_inbox/battery-reinforced-head-frequency-comedy.md`.
- Queue: `reinforced-head-frequency-comedy` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock created on start (agent id + timestamp), deleted on completion. R5005, sealed gates, red-team adjudication queue untouched. No follow-ups required per §4 (promote).
