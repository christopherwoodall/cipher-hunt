# Battery verdict: on-01-893-970-corpus

- Target: `on-01-893-970-corpus` (battery-queue.json, priority 3, status queued)
- Claim: "Corpus frame leg for the preverbal-'on' shape ('le [N] on vient' / preverbal pronoun + finite verb) in 1841 French, as red-team input for redteam-01-split-docket"
- Date: 2026-10-09

## Bar (verbatim, pre-registered)

">=1 genuine frame attestation or fence the shape as stream-coincidence."

Numbered clauses:
- **C1**: >=1 genuine frame attestation of the single-clause shape "le [N] on [V-fin]" (noun directly followed by preverbal "on" + finite verb, same clause) in 1841 French.
- **C2**: fence the shape as stream-coincidence (if no genuine attestation exists).

## Method

1. Byte-confirmed the stream loci on the repaired 1,847-pair / 96-type parse (asserts held; `canonical.py` never used):
   - @893 (row a5_08): `00 86 06 77(le) 76(noun) 01(?) 98(verb) 82(m) 14 98 83`
   - @970 (row a6_00): `19 24 06 77(le) 76(noun) 01(?) 98(verb) 48(e) 51 45 08`
   - The shape under test: `77 76 01 98` = "le [N] on vient" as ONE clause (per battery-redteam-01-split-input, Clause 2).
2. Corpus: `code/side-period/corpus/` — 97 files, 61,065,841 bytes (the lane's widened 1841 French corpus; includes drama texts, a superset of the prose census — if the shape were genuine it would appear in drama too).
3. Regex census: `\b(le|la|les|un|une|des|du|au|aux)\s+\w{2,}\s+on\s+\w{2,}` (case-insensitive, multiline) → **250 raw hits**. Every hit's context (±120 chars) hand-checked for whether the noun and "on" belong to the SAME clause.

## Findings

- **C1: FAIL.** Of 250 raw candidates, **zero** are a genuine single-clause "le [N] on V". Every hit falls into one of:
  1. **Fronted temporal adverbial + new clause** (~40%): "Le lendemain on monta", "Un jour on le trouva", "tous les jours on se félicite", "à la fin on saisira", "dès la veille on avait".
  2. **Fronted locative PP + new clause** (~30%): "dans les ateliers on avait", "aux Italiens on fait", "dans le monde on s'en rapporte", "à la cour on croie", "sur le bassin on lit".
  3. **Fronted manner/adverbial PP + new clause**: "du moins on croyait", "au fond on juge", "de la sorte on ralliait", "à la vérité on ne voulait".
  4. **Gerundive/purpose/subordinate clause + new main clause**: "si en la donnant on n'a compromis", "pour les contenir on eût", "qu'en repoussant la loi on prouverait", "lorsqu'une fois on aura décidé".
  5. **Enumerations**: "des chefs on passa aux officiers", "des cris on passa aux...".
  6. **Sentence boundaries / headings / stage directions**: "LA GUERRE. On l'a dit", "un fauteuil. On entend des coups".
  7. **OCR garbage**: "un poème on quatre chants" (= en), "la oü on" (= où), "une fiqile on pave", "un démenti on un reproche" (= ou).
- The nearest misses ("la société on verra résulter", "du corps on veut représenter", "la Saxe on pouvait") all have the "article + word" INSIDE a larger NP/relative clause, with "on" opening the main clause — clause boundaries, not the tested shape.
- **C2: FIRES.** The single-clause "le [N] on vient" shape is unattested across ~61M chars of 1841 French (250 candidates, all excluded in context).

## Verdict: NULL (fence executed)

The "on" reading of 01 at @893/@970 cannot be licensed by a corpus frame: the preverbal-'on' shape "le [N] on vient" as one clause is a stream-coincidence at the lane's corpus-grammaticality standard. This is red-team input, not a value claim: it bears on redteam-01-split-docket's Clause-2 "on" readings. The "en" readings at the same windows ("en vient", per battery-redteam-01-split-input) are untouched by this fence — "le [N] en V" (en as clitic) is a different shape and was not tested. 01's value stays open; 98='vient' LEAD untouched; §7 intact. No standing/red-team verdict contradicted or downgraded.

## Follow-ups proposed (all verified ABSENT from battery-queue.json; left for supervisor)

1. `en-01-893-970-corpus` (P4) — corpus leg for the rival "en" reading at @893/@970: is single-clause "le [N] en [V-fin]" (en as preverbal clitic) attested in 1841 French? Directly serves redteam-01-split-docket.
2. `on-01-40-corpus` (P4) — the third "on"-reading window @40 ("[41] on [24-fin]") has a different shape; corpus-leg it separately.
3. `boundary-76-01-893` (P4) — test the sentence-boundary parse "…le [N] | on vient…" at @893/@970: does the left context (ending at 76) license a complete clause, making "on" a new-clause subject (the shape the corpus DOES attest)?

## Scope

Corpus-leg only. No value named, no class named, no registry change. Canonical-stream caveat stands (rows a5_08/a6_00 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-on-01-893-970-corpus.md`
- Queue: `on-01-893-970-corpus` queued → `verdict`/`null` 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.on-01-893-970-corpus.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/on-01-893-970-corpus.lock`: created on start (agent 44eb2eeb-2422-4d83-b085-b1b474cd5412, 2026-10-09T19:18:00Z, no stale lock), deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched
