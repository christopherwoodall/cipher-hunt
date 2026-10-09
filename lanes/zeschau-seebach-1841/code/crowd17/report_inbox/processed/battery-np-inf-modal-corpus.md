# Battery report — np-inf-modal-corpus

Target: `np-inf-modal-corpus`. Date: 2026-10-09. Worker: worker-34708111.

## Bar (verbatim, pre-registered)

Bar: corpus verdict in 1841 diplomatic French: does any modal verb license "modal + NP + infinitive"? Confirmed zero kills the non-finite-88 arm here permanently; any attestation revives it.

## Numbered clauses

1. Search the lane's 1841 period corpus for modal + NP + infinitive.
2. Classify every hit as genuine attestation or licensed/noise.
3. If zero genuine attestations: verdict kill (non-finite-88 arm dead here).
4. If any genuine attestation: verdict null, arm revives, attestation is the headline.

## Method

- Corpus: `code/side-period/corpus/` — 62 text files, 4,692,620 tokens, 36,724 modal tokens (pouvoir, devoir, vouloir, savoir, falloir, all tenses). Mostly 1841 French (diplomatic correspondence, memoirs, press, theatre); a few German newspaper files.
- Three-pass regex scan (Python). Pass 1: modal + up to 8 tokens + infinitive-like word with non-clitic material between (6,652 raw hits). Pass 2: tightened to NP head directly after modal (1,718). Pass 3: removed licensed classes automatically — clitic pronouns (5,478), interrogative inversion subjects (1,762), "puis" as stage-direction adverb in plays (247), adverb/negation/parenthetical interveners, savoir + indirect question, falloir/devoir/vouloir as full lexical verbs + NP, infinitive-shaped nouns (éclair, chambre, octobre, affaire...), OCR/German noise. 155 candidates left for manual review.
- I read all 155 with context. Each one fell into a licensed or noise class (details below).

## Classified hits

Zero genuine attestations. The 155 manual-review candidates break down as:

- Adverbial/parenthetical interveners (licensed): ~60. Examples: "pouvait un jour désirer", "devrait un peu songer", "pourrait ce me semble déterminer", "devrai ce me semble me montrer", "voulait un instant réfléchir" (temporal adjunct, not an argument NP), "put cette fois échapper".
- Clitic pronouns between modal and infinitive (licensed): e.g. "saurais monsieur vous accorder" (vocative + clitic), "doit des lors nous importer", "peut tout aussi bien y faire entrer".
- Inverted subjects in questions (licensed): "que peut cette main généreuse t'offrir", "que pouvaient ces démonstrations contre les pouvoirs", "que pourrait un ministre".
- Full lexical verb + NP, infinitive belongs to another clause (not modal use): "voulait une garantie contre", "fallait un souverain temporaire", "doit son élévation" (owe), "savait cela", "veut une réception solennelle", "voulait du bien" (vouloir du bien à).
- OCR / non-French noise: ~40. Examples: "sus cz ykowski's neuester" (German), "devraient wlettevni nad get fasere", "peux mondes passager" (header "revue des deux mondes" OCR), "voulait lord palmer ston me" (sentence boundary + hyphen-split "Pal-merston"), "puis des afhires étrangères novembre" (puis = then), "sus dernlfebe mit pendre" (German).
- Infinitive-shaped non-verbs: "quatre", "encore", "contre", "octobre", "alexandre", "voltaire", "métier", "histoire", "j'espère", "montre", "prépare", "déclare".
- "puis" as adverb "then" in plays and prose: "puis une petite porte se rouvre", "puis son présent littéraire", "puis flmperatrice ira passer".

## Per-clause pass/fail

1. PASS — corpus searched (62 files, 4.69M tokens, 36.7k modals).
2. PASS — all 155 candidates classified; none genuine.
3. PASS — confirmed zero.
4. N/A — no attestation found.

## Verdict

**kill** — confirmed zero attestations of "modal + NP + infinitive" across the 1841 period corpus. The non-finite-88 arm is dead in this lane.

No lock conflicts. No R5005 contact. No invented data.
