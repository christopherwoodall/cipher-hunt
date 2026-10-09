# Battery report: reinforced-pour-inf-adjacent-excl

- Target id: `reinforced-pour-inf-adjacent-excl`
- Claim: "rule out next-sentence exclamation on the 16 declarative zero-pause reinforced-governed-infinitive windows (±500-char frame)"
- Date: 2026-10-09
- Stream: not applicable — corpus census against period French, per target charter. R5005, sealed gate instances, and the red-team adjudication queue were not touched.
- Parentage: follow-up #3 (P3) of the NULL `reinforced-pour-inf-zeropause` (2026-10-09), which found 16 declarative zero-pause reinforced-head + preposition + infinitive windows, all non-exclamatory.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked with -là or -ci. "Genuine adjacent exclamation" = an exclamatory clause ("!") within the ±500-char frame that SHARES the reinforced head (i.e. the head governs or belongs to the exclamatory clause). An ambient "!" or "?" in a separate sentence/clause does not count.

## Bar (verbatim, pre-registered before testing)

"0 genuine adjacent exclamation confirms the zero is not a window-boundary artifact; any genuine re-opens the pairing"

Numbered pass/fail clauses (restated before testing, not modified after):

1. Re-derive the declarative zero-pause head+preposition+infinitive windows byte-exact and re-examine each with a ±500-char frame.
2. Confirm 0 GENUINE adjacent exclamations (head-sharing exclamatory clause) across all windows — this confirms the parent's zero is not a window-boundary artifact. Any genuine attestation re-opens the pairing.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/reinforced-pour-inf-adjacent-excl.lock` on start (2026-10-09); deleted on completion.
2. Wrote `code/crowd17/next-token/reinforced_pour_inf_adjacent_excl_census.py`: re-derives the zero-pause reinforced-head + preposition + infinitive shape over the parent's byte-identical 21-file corpus (18 French files in code/side-period/corpus + 3 wider files in data/), allowing up to 2 intervening particles (ne/se) between preposition and infinitive, and dumps ±500-char frames for manual classification. Raw results: `code/crowd17/next-token/reinforced-pour-inf-adjacent-excl_census.json`.
3. Hand-vetted every candidate window for genuineness (head + governed infinitive), then hand-classified every "!" and "?" in-frame by clause ownership.

## Window-level evidence

### Census yield

- Raw candidate hits (head + prep (+≤2 particles) + infinitive-shaped word): 24.
- Hand-vetted false positives (2): guizot-memoires-t1 @593899 "celle-ci à votre image" ("votre" is a possessive, not an infinitive); revue-deux-mondes-1841-q3 @1984663 "celle-ci point de mire un système" ("mire" is the noun in "point de mire", not an infinitive). Both excluded with cause.
- **Genuine declarative zero-pause head+prep+inf windows: 22** — a superset of the parent's 16 (the parent's strict "directly followed" rule; mine additionally admits ne/se particles, all hand-verified genuine).

The 22 genuine windows (file @ offset, head, shape): guizot-memoires-t1 @466086 "celle-ci pour conquérir"; @466120 "celle-là pour retenir"; metternich-papiere-v4 @73090 "celles-ci de ne point rencontrer"; @756543 "celle-ci de jamais se prêter"; @872506 "celles-ci de devenir"; metternich-papiere-v6 @1167534 "celui-ci de faire"; @1682373 "celle-ci de faire ressortir"; nesselrode-v10 @11048 "celle-ci de rompre"; @57549 "celui-ci de se mettre"; @214428 "celle-ci pour se ménager"; nesselrode-v8 @348133 "celui-ci à se rendre"; pozzo-di-borgo-correspondance-v1 @624602 "celui-ci de participer"; revue-deux-mondes-1841-q1 @168528 "ceux-ci pour moudre"; @168563 "ceux-là pour scier"; revue-deux-mondes-1841-q2 @650108 "ceux-ci à attaquer"; revue-deux-mondes-1841-q3 @2475974 "ceux-là à jouer"; revue-deux-mondes-1841-q4 @1326152 "ceux-ci de les porter"; @1326196 "ceux-là de leur faire subir"; @2673373 "celui-ci à se soumettre"; talleyrand-memoires-v1 @211457 "celle-ci de faire"; gutenberg-30514-tocqueville-t2 @68783 "ceux-ci à s'éloigner"; @233703 "ceux-là de déplorer".

### Ambient marks in frame (5 windows with "!" or "?" in ±500 chars)

1. metternich-papiere-v4 @872506 "celles-ci de devenir journellement le jouet...": the "?" belongs to "Quels sont ces lois et ces usages ?" in the FOLLOWING sentence (about civil liberty). Separate sentence, no head-sharing clause. Not genuine.
2. metternich-papiere-v6 @1167534 "c'est à celui-ci de faire une demande en grâce.": the "?" belongs to "Lequel des deux partis prendra le Sultan ?" in a later sentence. Separate sentence, no head-sharing clause. Not genuine.
3. revue-deux-mondes-1841-q1 @168528 "ceux-ci pour moudre le grain...": the "!" belongs to "une entreprise que l'on pourrait croire impossible!" — a separate later sentence about the Hollandais, ~300 chars after the head. Different sentence, no head-sharing clause. Not genuine.
4. revue-deux-mondes-1841-q1 @168563 "ceux-là pour scier les planches...": same "!" as (3). Not genuine.
5. revue-deux-mondes-1841-q2 @650108 "pour exciter ceux-ci à attaquer les Anglais...": the "?" belongs to the PRECEDING section heading "...en particulier ?" Separate clause, no head sharing. Not genuine.

**Genuine adjacent exclamations: 0/22.** No head-sharing exclamatory clause exists within ±500 chars of any declarative zero-pause head+governed-infinitive window.

## Per-clause pass/fail

1. Windows re-derived byte-exact with ±500-char frames: **PASS.** 22 genuine windows (superset of the parent's 16, both false positives excluded with cause).
2. 0 genuine adjacent exclamations → zero is not a window-boundary artifact: **PASS.** The 5 ambient marks are all "?" or belong to separate sentences with no head-sharing clause. No genuine attestation re-opens the pairing.

## Adverses, answered

- None pre-registered ("Adverses: null").
- Self-check: does this confirm contradict the parent NULL (reinforced-pour-inf-zeropause)? No — it closes its chartered follow-up #3 exactly as directed. The reinforced head + governed exclamatory infinitive now stands fenced with the next-sentence recall gap ruled out.
- Note: "?" marks were classified anyway; the bar's pairing is exclamatory ("!"), and no "?" marked a head-sharing clause either.

## Verdict: PROMOTE

The parent's zero is not a window-boundary artifact: across 22 genuine declarative zero-pause reinforced-head + governed-infinitive windows, no adjacent exclamatory clause shares the head. The fence against the reinforced-head + governed exclamatory infinitive pairing is hardened.

## Bookkeeping

- Census script: code/crowd17/next-token/reinforced_pour_inf_adjacent_excl_census.py; raw results: code/crowd17/next-token/reinforced-pour-inf-adjacent-excl_census.json (22 genuine windows + frames).
- Report: code/crowd17/report_inbox/battery-reinforced-pour-inf-adjacent-excl.md (this file).
- battery-queue.json: `reinforced-pour-inf-adjacent-excl` queued -> verdict/promote via temp-file + rename (own entry only; claim/bars/evidence/adverses preserved).
- Lock created on start, deleted on completion. R5005, sealed gates, red-team queue untouched. Every number traces to the named corpus files or the census script; no invented data.
