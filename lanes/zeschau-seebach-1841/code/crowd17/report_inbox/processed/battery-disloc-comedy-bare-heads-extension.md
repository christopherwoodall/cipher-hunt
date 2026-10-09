# Battery report: disloc-comedy-bare-heads-extension

- Target id: `disloc-comedy-bare-heads-extension`
- Claim: "run the bare-head (ce/cela/ça) demonstrative census over the 6 newly ingested comedy files"
- Date: 2026-10-09
- Worker: battery worker (subagent e8481a42-e906-4885-a80e-a87d4cf2d385)
- Stream: not applicable — corpus census against new period French comedy, per target charter (same as parent battery). The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, and resumed by a pronoun ("Cela, je le crois" = "that, I believe it"). "Bare head" = a tonic demonstrative without -là/-ci (ce, cela, ceci, ça), as opposed to the reinforced compounds (celui-là, ceux-ci). "Bare exclamatory infinitive" = an infinitive used as an exclamation with no preposition (de, pour, à), no "que", and no governing verb between the topic and the verb ("Moi, voler !" = "me, steal !").

## Parentage

Follow-up #2 of the NULL `disloc-reinforced-comedy-extension` (2026-10-09), which fenced the reinforced-head inventory at the comedy-register level (2 reinforced-head-comma hits → 0 exclamatory candidates in 465,531 chars, 0 genuine). The comedy register was never censused for the BARE demonstrative inventory — this battery closes that gap.

## Corpus

The 6 comedy-extension files in `code/side-period/corpus/` (sizes verified in-session; total 465,531 chars, exact match with the parent report):

| file | chars |
|---|---|
| `scribe-le-savant.txt` | 88,949 |
| `scribe-le-lorgnon.txt` | 67,028 |
| `labiche-voyage-perrichon.txt` | 97,395 |
| `labiche-la-cagnotte.txt` | 134,353 |
| `labiche-29-degres-ombre.txt` | 34,634 |
| `labiche-affaire-rue-lourcine.txt` | 43,172 |
| **Total** | **465,531** |

## Bar (verbatim, pre-registered before testing)

">=1 genuine bare-head + bare exclamatory infinitive in comedy re-opens the bare inventory; confirmed zero fences the bare inventory in the comedy register too"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated bare demonstrative head (ce/cela/ceci/ça) + bare exclamatory infinitive exists in the 6 comedy texts. If yes: the bare inventory re-opens in comedy (promote).
2. If clause 1's census is a confirmed zero — every candidate window classified, false friends excluded with cause — the bare inventory stays fenced at the comedy-register level too (null per §4: inconclusive as a kill, since zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. A supervisor dispatch lock existed at `code/crowd17/next-token/locks/disloc-comedy-bare-heads-extension.lock`; overwrote it on start with worker id + UTC timestamp (not treated as stale); will delete on completion.
2. Ran `code/crowd17/next-token/disloc_comedy_bare_heads_extension_census.py` (re-runnable) — the P1/P2/P3 taxonomy copied verbatim from `disloc_demonstrative_drama_reissue_census.py`:
   - P1 (dislocation): `\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]` case-insensitive; window = text from the demonstrative through the next `[!?.]` (inclusive), capped at 180 chars.
   - P2 (exclamatory filter): window must contain "!" before its end.
   - P3 (infinitive candidate): `\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b` on the window; all candidates classified by hand (regex cannot separate -er infinitives from nouns/adjectives).
3. Pass B (bare "ce", per the target's "(ce/cela/ça)" wording): `\bce\b\s*[,;:]` case-insensitive, same windowing + P2 + P3. "ce" is excluded from the standard DEM inventory because it is overwhelmingly the determiner; Pass B runs it separately.
4. Cross-check (from the ingest battery): STRICT (`\b(cela|ceci|ça)\b\s*[,;:…]\s*(?:\S+\s+)?[word](er|ir|re)\s*!` within 50 chars) and LOOSE (`\b(cela|ceci|ça)\b.{0,35}?[inf].{0,35}!` within 35 chars); all loose hits printed with ±90-char context and classified by hand.
5. Classification rule (same as sibling batteries): a genuine window needs (a) a demonstrative in dislocated topic position set off by a pause mark, (b) a BARE infinitive (no preposition, no "que", no governing verb between topic and verb), and (c) exclamatory force where the "!" terminates the infinitive phrase itself.

## Window-level evidence

### Census yields

- **51 demonstrative-comma hits, 0 bare-"ce"-comma hits, → 10 exclamatory candidates, 0 strict, 12 loose cross hits → 0 genuine in 465,531 chars.**

### The 10 P1/P2 candidates (verbatim, all classified with cause)

1. `labiche-29-degres-ombre.txt` @14572 — "ça, non !" — no infinitive; exclaimed negation. Excluded.
2. `labiche-29-degres-ombre.txt` @19628 — "Ça, un amant !" — no infinitive; exclaimed NP ("un amant"). Excluded.
3. `labiche-affaire-rue-lourcine.txt` @11304 — "ça, un prix de vers latins !" — no infinitive; exclaimed NP. Excluded.
4. `labiche-affaire-rue-lourcine.txt` @20260 — "cela, point d'embarras, / La conscience, ami, ça n'se voit pas !" — no infinitive; exclaimed NP ("point d'embarras"), "ça" = subject of the finite "ça n'se voit pas". Excluded.
5. `labiche-affaire-rue-lourcine.txt` @37381 — "ça, il n'y a plus de témoins !" — no infinitive; "ça" = subject of the finite clause. Excluded.
6. `labiche-la-cagnotte.txt` @92375 — "cela, elle ne peut pas m'entraîner bien loin !" — regex inf_hit 'entraîner', but wider context reads "Après **cela**, elle ne peut pas m'entraîner bien loin !…": "cela" is the complement of the preposition "après" (not a dislocated topic), and "entraîner" is governed by the modal "peut" inside a finite clause that the "!" terminates. Not bare, not exclamatory-infinitive. Excluded: preposition-governed demonstrative + modal-governed infinitive.
7. `labiche-voyage-perrichon.txt` @5311 — "ça, chaque fois qu'elle n'a pas pris son café !" — no infinitive; clause-initial "ça" before an elliptical clause. Excluded.
8. `labiche-voyage-perrichon.txt` @11511 — "ça, mon ami !" — no infinitive; exclaimed interjection/vocative. Excluded.
9. `scribe-le-lorgnon.txt` @8652 — "cela ; et si monsieur le baron et madame / la baronne… justement la voici !" — no infinitive; demonstrative + semicolon before a conditional clause. Excluded.
10. `scribe-le-savant.txt` @43400 — "ça, / Que de maris seraient sans place !" — no infinitive; exclamative "que"-clause (finite). Excluded.

### The 12 loose cross hits (verbatim, all classified with cause)

1. `labiche-29-degres-ombre.txt` @6654 — "ça va faire une diversion au tonneau !" — "ça" = subject of the finite modal "va faire" (going to). Not dislocated. Excluded.
2. `labiche-affaire-rue-lourcine.txt` @27896 — "ça coûte cher !" — "ça" = subject of finite "coûte". Excluded.
3. `labiche-affaire-rue-lourcine.txt` @38090 — "Ceci fera l'affaire !" — "ceci" = subject of finite "fera". Not dislocated; exclamatory finite clause. Excluded.
4. `labiche-la-cagnotte.txt` @45466 — "Mâtin ! que ça doit être bon !" — "ça" = subject of the modal "doit être" inside a finite "que"-clause. Excluded: finite-matrix.
5. `labiche-la-cagnotte.txt` @53384 — "Se partager tout ça ?… c'est bizarre. (On sonne.) Voilà ! voilà !" — the "!" terminates "Voilà !"; "ça" sits inside "tout ça". Excluded: interjection terminator.
6. `labiche-la-cagnotte.txt` @92375 — same window as candidate 6 above ("Après cela, elle ne peut pas m'entraîner bien loin !"). Excluded with the same cause.
7. `labiche-la-cagnotte.txt` @119301 — "ça ne peut pas durer comme ça ! Je proteste !" — "ça" = subject of finite modal clause. Excluded.
8. `labiche-voyage-perrichon.txt` @11671 — "et ça va en Suisse !" — "ça" = subject of finite "va" (movement). Excluded.
9. `labiche-voyage-perrichon.txt` @60429 — "ça lui apprendra à ne pas acquitter les droits !" — "ça" = subject of finite "apprendra"; "acquitter" is governed by the preposition "à". Not a bare infinitive. Excluded.
10. `labiche-voyage-perrichon.txt` @73544 — "ça m'a échappé, ton père se bat !" — "ça" = subject of finite "a échappé". Excluded.
11. `labiche-voyage-perrichon.txt` @87164 — "C'est ça ! des excuses ! encore des excuses !" — "ça" inside "c'est ça"; the "!" terminates exclaimed NPs. Excluded.
12. `scribe-le-savant.txt` @4840 — "Voyez où cela le mène : à être malade, à se tuer !" — "cela" = subject of the finite "mène"; the infinitives "être/se tuer" are governed by the preposition "à". NOT bare infinitives (the bar requires no preposition between topic and verb). Excluded with cause: preposition-governed infinitives. (Notable near-miss: this is the comedy register's closest approach to an exclamatory infinitive — the infinitives are preposition-governed, so it feeds follow-up 2 below rather than the bar.)

### Pass B note

0 bare-"ce"-comma hits in 465,531 chars — bare "ce" never appears as a dislocated topic with a pause mark in this comedy sample (consistent with "ce" being the determiner/clitic elsewhere).

## Per-clause pass/fail

- Clause 1 (≥1 genuine bare-head + bare exclamatory infinitive in comedy): FAIL — 0 genuine of 10 candidates + 12 loose cross hits in 465,531 chars; every window classified with cause.
- Clause 2 (confirmed zero fences the bare inventory in the comedy register too): PASS — census executed per the pre-registered taxonomy; nothing left unclassified. Verdict **null** per §4 (zero is an absence — fencing, not kill).

Combined with the prose null (0 genuine in 27.66M chars) and the drama nulls (0/35 bare-head candidates in 2.97M chars; 0/8 reinforced-head candidates), the bare demonstrative + bare exclamatory infinitive pairing is now fenced in prose, drama, and comedy registers.

## Verdict

**NULL** — confirmed zero for the bare demonstrative inventory in the comedy register; no standing verdict contradicted; no red-team verdict touched. Pass B recorded no dislocated bare "ce" at all.

## Follow-ups (nulls regenerate work — proposed for the supervisor to queue)

1. **`disloc-comedy-bare-heads-recall`** (P2) — recall repair for THIS census: dash/parenthesis pause-mark variants after the bare head + an uncapped pass over the 6 comedy files, to confirm the zero is not a pattern-form artifact. Bar: 0 genuine with variants confirms; any genuine re-opens.
2. **`disloc-comedy-governed-inf`** (P2) — governed-shape census in comedy: the nearest near-miss (Le Savant @4840, "à être malade, à se tuer !") shows preposition-governed exclamatory infinitives may exist in the comedy register. Test whether the governed shape (vs the now-fenced bare shape) attests genuinely in comedy, mirroring `gov-excl-inf-register-drama`'s register-boundary logic. Bar: ≥1 genuine governed exclamatory infinitive in comedy pins the fence exactly at BARE; confirmed zero fences the whole exclamatory-infinitive family in comedy.

## Files

- Report: `code/crowd17/report_inbox/battery-disloc-comedy-bare-heads-extension.md` (this file)
- Census script: `code/crowd17/next-token/disloc_comedy_bare_heads_extension_census.py`
- Raw census JSON: `code/crowd17/next-token/disloc-comedy-bare-heads-extension_census.json`
- Queue: `code/crowd17/next-token/battery-queue.json` — target `disloc-comedy-bare-heads-extension` set to status `verdict`/null via temp-file + atomic rename, own entry only, pre-write assert + post-write re-validation
