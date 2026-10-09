# Battery report: disloc-comedy-bare-heads-recall

- Target id: `disloc-comedy-bare-heads-recall`
- Claim: "dash/parenthesis pause-mark variants + uncapped pass over the 6 comedy files for bare-head + bare exclamatory infinitive"
- Date: 2026-10-09
- Worker: battery worker (subagent)
- Stream: not applicable — corpus census against period French comedy, per target charter (same as the parent battery). The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, and resumed by a pronoun. "Bare head" = a tonic demonstrative without -là/-ci (ce, cela, ceci, ça). "Bare exclamatory infinitive" = an infinitive used as an exclamation with no preposition, no "que", and no governing verb between the topic and the verb.

## Parentage

Follow-up #1 of the NULL `disloc-comedy-bare-heads-extension` (2026-10-09), which found 51 demonstrative-comma hits → 10 candidates → 0 genuine in 465,531 comedy chars, with "pause-mark variants and uncapped windows unsearched". This battery runs exactly those two missing passes.

## Bar (verbatim, pre-registered before testing)

"0 genuine confirms the comedy bare-inventory zero is not a pattern-form artifact; any genuine re-opens the inventory"

Numbered pass/fail clauses (restated before testing, not modified after):

1. Any GENUINE dislocated bare demonstrative head (ce/cela/ceci/ça) + bare exclamatory infinitive surfaces under the recall passes (pause-mark variants: dash family, ellipsis, open parenthesis, !/? used as the dislocation pause; uncapped windows through the next [!?.] with no 180-char limit). If yes: the bare inventory re-opens in comedy (promote).
2. If the recall census is a confirmed zero — every candidate window classified with cause — the parent zero is confirmed not to be a pattern-form artifact (null per §4: zero is an absence, not a kill).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/disloc-comedy-bare-heads-recall.lock` on start; deleted on completion.
2. Wrote and ran `code/crowd17/next-token/disloc_comedy_bare_heads_recall_census.py` (re-runnable) over the same 6 comedy files in `code/side-period/corpus/` (465,531 chars verified): bare head regex `\b(cela|ceci|ça|cel[àa]|cec[iy])` + Pass B bare `\bce\b`, each followed by one of five pause-mark classes (comma/semicolon/colon rerun, em/en-dash or hyphen run, ellipsis, open parenthesis, clause-terminal ! or ?), then the window runs from the demonstrative through the next [!?.] in the text *after the pause* with no 180-char cap (hard cap 4000 chars), filtered for "!" and infinitive-shaped words, all classified by hand with the parent's genuine rule: (a) demonstrative in dislocated topic position set off by a pause mark, (b) BARE infinitive (no preposition, no "que", no governing verb between topic and verb), (c) exclamatory force where the "!" terminates the infinitive phrase itself.
3. Census script: `code/crowd17/next-token/disloc_comedy_bare_heads_recall_census.py`; raw results: `code/crowd17/next-token/disloc-comedy-bare-heads-recall_census.json`.

## Census yields

- **465,531 chars; 31 variant candidates** (no bare-"ce"-pause hits, no dash-pause hits, no paren-pause hits — these pause-mark classes produce zero candidates at all, which is itself recorded).
- Of the 31, **10 are the parent's already-classified comma-pause set** (same 10 candidates: all false friends, exclaimed NPs/interjections/finite clauses/preposition-governed demonstratives). The uncapped rerun of the parent's comma pass adds **no** new candidate — the 180-char cap was not hiding exclamations.
- **21 new candidates** (13 exclq-pause, 8 ellipsis-pause), all classified below with cause. **0 genuine.**

### The 21 new candidates (all excluded with cause)

1. `labiche-29-degres-ombre.txt` @19820 — "ça ! … ce n'était pas convenu !" — no infinitive; "!" terminates a finite clause. Excluded.
2. `labiche-29-degres-ombre.txt` @27099 — "Il ne manquerait plus que ça !… Renoncer à ce duel… maintenant… c'est impossible !" — regex inf_hit 'renoncer', but wider context shows the "!" terminates the finite clause "c'est impossible !"; "Renoncer à ce duel" is a suspended infinitive completed by the finite clause, not an exclamatory infinitive. Excluded: finite-clause terminator. (This was the only infinitive-bearing new candidate; verified at ±250 chars.)
3. `labiche-29-degres-ombre.txt` @30867 — "ça ! Il est enragé, celui-là !" — no infinitive. Excluded.
4. `labiche-affaire-rue-lourcine.txt` @3348 — "ça ! … il est allé se coucher à cinq heures…" — 'coucher' governed by "est allé" inside a finite clause; "!" terminates that clause. Excluded: governed infinitive in finite clause.
5. `labiche-affaire-rue-lourcine.txt` @9737 — "ça ! … il me reconnaît !" — finite. Excluded.
6. `labiche-affaire-rue-lourcine.txt` @11598 — "ça ! Deux labadens !" — exclaimed NP. Excluded.
7. `labiche-affaire-rue-lourcine.txt` @11800 — "ça ! des noyaux de cerises !" — exclaimed NP. Excluded.
8. `labiche-la-cagnotte.txt` @11468 — "ça… Allons !" — no infinitive; interjection. Excluded.
9. `labiche-la-cagnotte.txt` @44463 — "ça… je ne sais pas ce que c'est, mais j'aime assez ça !" — finite. Excluded.
10. `labiche-la-cagnotte.txt` @49568 — "ça… Nous irons tous !" — finite. Excluded.
11. `labiche-la-cagnotte.txt` @79453 — "ça… un vrai lit de plumes !" — exclaimed NP. Excluded.
12. `labiche-la-cagnotte.txt` @130918 — "ça… c'est du faux !" — finite. Excluded.
13. `labiche-la-cagnotte.txt` @119328 — "ça ! Je proteste !" — finite. Excluded.
14. `labiche-voyage-perrichon.txt` @64867 — "ça… moi et le mont Blanc… tranquille et majestueux !" — no infinitive. Excluded.
15. `labiche-voyage-perrichon.txt` @93819 — "ceci… et surtout gardez-moi le secret: … ceux qu'ils nous rendent !" — imperative + finite clauses; no bare exclamatory infinitive. Excluded.
16. `labiche-voyage-perrichon.txt` @3279 — "ça ! PERRICHON / C'est le départ qui est laborieux…" — no infinitive. Excluded.
17. `labiche-voyage-perrichon.txt` @10676 — "ça ! MAJORIN / Pardon !" — interjection. Excluded.
18. `labiche-voyage-perrichon.txt` @11534 — "ça ! MAJORIN, sèchement / Allons !" — no infinitive. Excluded.
19. `labiche-voyage-perrichon.txt` @25772 — "cela ! MADAME PERRICHON / Merci, monsieur Armand !" — vocative/interjection. Excluded.
20. `labiche-voyage-perrichon.txt` @87164 — "ça ! des excuses !" — exclaimed NP. Excluded.
21. `scribe-le-lorgnon.txt` @59205 — "cela ! J'en étais sûr, je ne m'étais pas trompé !" — finite. Excluded.

### Zero-yield pause-mark classes

- Dash family (—, –, --, -) after a bare head: **0 hits in 465,531 chars.**
- Open parenthesis after a bare head: **0 hits.**
- Bare "ce" followed by any pause mark (Pass B): **0 hits** (consistent with the parent's 0 bare-"ce"-comma result).

## Per-clause pass/fail

- Clause 1 (≥1 genuine under the recall passes): **FAIL** — 0 genuine of 31 variant candidates; every window classified with cause.
- Clause 2 (confirmed zero; parent zero not a pattern-form artifact): **PASS** — both missing passes executed; dash/paren/CE passes yield zero even as candidates. Verdict **null** per §4 (zero is an absence).

## Verdict

**NULL** — confirmed zero for the bare demonstrative + bare exclamatory infinitive inventory in the comedy register under pause-mark variants and uncapped windows. The bare inventory stays fenced in comedy. No standing verdict contradicted; no red-team verdict touched.

## Follow-ups (nulls regenerate work — proposed for the supervisor to queue)

1. **`disloc-comedy-inversion`** (P3) — inverted-order census in comedy: the postposed "[inf] !, cela" shape was fenced in drama (inversion-fullcorpus) and RDM, but never censused over the 6 comedy files. Bar: ≥1 genuine inverted-shape attestation re-opens; confirmed zero fences the inverted order in comedy too.
2. **`bare-excl-inf-head-inventory-comedy`** (P3) — positive-space complement to the zero: inventory of genuine heads of bare exclamatory infinitives in the 6 comedy files (the drama sibling `bare-excl-inf-head-inventory-drama` exists as a queue pattern), to record what CAN head the construction in comedy dialogue.

## Files

- Report: `code/crowd17/report_inbox/battery-disloc-comedy-bare-heads-recall.md` (this file)
- Census script: `code/crowd17/next-token/disloc_comedy_bare_heads_recall_census.py`
- Raw census JSON: `code/crowd17/next-token/disloc-comedy-bare-heads-recall_census.json`
- Queue: `code/crowd17/next-token/battery-queue.json` — target `disloc-comedy-bare-heads-recall` set to status `verdict`/null via temp-file + atomic rename, own entry only, pre-write assert + post-write re-validation
