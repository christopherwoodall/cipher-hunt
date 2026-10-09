# Battery `ordinal-particle-boost` — report

Target: ordinal-particle-boost (P3). Follow-up from `particle-20-value-rivals` NULL (2026-10-09).

## Bar (verbatim, pre-registered)

"separation declared iff 'mais' stays exclusive at n>=20 with rivals at zero; else the frame is abandoned as a discriminator"

## Bar restated as numbered clauses

- C1: 'mais' remains exclusive in the ordinal-ellipsis-final frame at n>=20.
- C2: rivals (or/donc/cependant) stay at zero in the same frame.
- C3: else the frame is abandoned as a discriminator.

## Method

- Stream: repaired 1,847-pair parse re-derived in-session per repair_parse.py; asserts held (1,847 pairs, 96 types). `canonical.py` never used.
- Corpus: lane period corpus `code/side-period/corpus`, 76 .txt files (~35M chars). 1841 diplomatic French register.
- Census script: `code/crowd17/next-token/ordinal_particle_boost_census.py` → `ordinal_particle_boost.json`.
- Frame: clause-initial particle (mais/or/donc/cependant) whose immediately preceding clause ends with a nominalized ordinal. Expanded beyond the parent battery's regex: added possessive determiners (sa/son/ses/ma/mon/tes/notre/votre/leur), indefinite articles (un/une/des), demonstratives (ce/cette/cet/ces), ordinal stems quatrièmes/cinquièmes/sixièmes/ultimes, all unaccented spelling variants. Particles matched accent-insensitively.
- All hits hand-audited in full context.

## Findings

Census result over 76 files: mais=6, or=0, donc=0, cependant=1. All 7 hits hand-audited genuine:

| # | file | particle | ordinal span | judgment |
|---|------|----------|--------------|----------|
| 1 | raw-thtredecasim01dela-djvu.txt | mais | le premier | genuine — "J'en conviens le premier. Mais c'est une faiblesse..." |
| 2 | revue-deux-mondes-1841-q1.txt | mais | le cinquième | genuine — "...le pathétique de tout le cinquième. Mais, pour rester bon juge..." |
| 3 | revue-deux-mondes-1841-q1.txt | mais | la première | genuine — "...par-dessus la première. Mais voici bien autre chose." |
| 4 | revue-deux-mondes-1841-q1.txt | mais | la première | genuine — "...plutôt que la première. Mais il serait tout aussi juste d'ajouter..." |
| 5 | revue-deux-mondes-1841-q3.txt | **cependant** | une troisième | **GENUINE RIVAL** — "...toute envie d'en organiser une troisième. Cependant la petite flotte avait encore rencontré..." |
| 6 | revue-deux-mondes-1841-q3.txt | mais | la première | genuine — "...cette nouvelle polémique à la première. mais plus la chose était imprudente..." |
| 7 | revue-deux-mondes-1841-q4.txt | mais | les premiers | genuine — "...vous n'avez qu'à tirer les premiers. mais vous pourrez bien vous en repentir." |

Hit 5 is a positive, genuine counterexample: "cependant" follows a clause ending in a nominalized ordinal ("une troisième") in clean diplomatic-period prose. No amount of additional powering can un-find it.

## Per-clause verdicts

- C1: FAIL — n(mais)=6 < 20.
- C2: FAIL — cependant=1, a genuine rival attestation.
- C3: FIRES — the frame is abandoned as a discriminator.

## Verdict: KILL

The ordinal-ellipsis-final frame cannot separate 'mais' from its rivals at the cipher window @760. The 5-0-0-0 observation was an underpowered artifact; with expanded variants and the full corpus, 'cependant' attests in the same frame. This finding stands alongside the parent battery's F2/F3 results: neither the ordinal frame nor the fois frame separates 'mais' from its rivals. The parent's 'mais' naming at @760 stands unrefuted by this test (no value proposed or killed here); only the discriminator route is dead.

## Adverses

None listed. No standing or red-team verdict contradicted or downgraded. §7 intact. R5005 untouched. Canonical-stream caveat stands.

## Scope

Kills only the ordinal-frame discriminator claim for 20='mais'-vs-rivals. Untouched: 20's open value, the poly-20-docket, 'donc'-needs-premise results (already dead in the parent), fois-final frame results.

## Follow-ups

Per §4, kills regenerate no follow-ups — none proposed.
