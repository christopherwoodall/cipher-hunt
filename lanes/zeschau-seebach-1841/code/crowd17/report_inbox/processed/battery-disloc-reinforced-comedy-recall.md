# Battery report: disloc-reinforced-comedy-recall

- Target id: `disloc-reinforced-comedy-recall`
- Claim: "run pause-mark variants (dash/parenthesis) + an uncapped pass over the 6 new comedy files to confirm the comedy zero is not a pattern-form artifact"
- Date: 2026-10-09
- Worker: battery worker (subagent e24d4fa0-feca-4f91-926f-45232bb7f0ba)
- Stream: not applicable — corpus census against new period French comedy, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, and resumed by a pronoun. "Reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, ceux-ci), as opposed to the bare tonic heads (cela, ceci, ça). "Bare exclamatory infinitive" = an infinitive used as an exclamation with no preposition, no "que", and no governing verb between the topic and the verb ("Moi, voler !" = "me, steal !").

## Parentage

Recall check on the NULL `disloc-reinforced-comedy-extension` (2026-10-09), which found 2 reinforced-head-comma hits → 0 exclamatory candidates in 465,531 chars of new Scribe/Labiche comedy. Its parentage: follow-up #1 of that report, chartered to confirm the comedy zero is not a separator-class or window-truncation artifact.

## Gate / corpus

All 6 comedy files verified on disk in `code/side-period/corpus/` (Scribe *Le Savant*, *Le Lorgnon*; Labiche & Martin *Le Voyage de monsieur Perrichon*; Labiche & Delacour *La Cagnotte*; Labiche *29 degrés à l'ombre*; Labiche/Monnier/Martin *L'Affaire de la rue de Lourcine*). 465,531 chars total — same byte-identical set as the parent battery. Gate not rewritten.

## Bar (verbatim, pre-registered before testing)

"0 genuine confirms the comedy zero is not a pattern-form artifact; any genuine re-opens the family"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated reinforced-demonstrative head (celui-là / ceux-là / celle-là / celles-là / celui-ci / ceux-ci / celle-ci / celles-ci) + bare exclamatory infinitive exists in the 6 comedy files under the EXTENDED separator class (comma + em-dash + en-dash + hyphen + parenthesis) or in the uncapped-window pass. If yes: the pairing re-opens.
2. If clause 1's recall census is a confirmed zero — every candidate classified, false friends excluded with cause — the comedy zero is confirmed as not a pattern-form artifact (null per §4: inconclusive as a kill, since zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Overwrote the supervisor dispatch lock `code/crowd17/next-token/locks/disloc-reinforced-comedy-recall.lock` on start (adopted, not stale); deleted on completion.
2. Wrote and ran `code/crowd17/next-token/disloc_reinforced_comedy_recall_census.py` (re-runnable): P1-recall = DEM_REINF followed by one of `[,;:—–\-()]`; window = demonstrative + 400 chars NOT truncated at the first sentence mark (uncapped pass); P2 = window must contain "!" anywhere; P3 = -er/-ir/-re/-oir token regex for candidates. Raw results in `code/crowd17/next-token/disloc-reinforced-comedy-recall_census.json`.
3. Raw reinforced-head inventory per file for the non-blindness record (see evidence).

## Window-level evidence

### Separator-class coverage

Only comma separators are attested after reinforced heads in the 6 comedy files: `scribe-le-savant.txt` 1, `scribe-le-lorgnon.txt` 1. Dash/paren/hyphen variants: **zero attested**. Raw reinforced-head inventory: 26 heads across the 6 files (Savant 4, Lorgnon 8, Perrichon 3, Cagnotte 6, 29 degrés 1, Lourcine 4) — the regex is not blind; heads exist but almost never dislocate.

### Census yield: 1 recall candidate, 0 genuine

- **1 candidate** in 465,531 chars: `scribe-le-lorgnon.txt` @5398, sep=`,`, window closed within 180 chars = True.
  - Window (verbatim start): "Celui-là, fidèle et sensible, / Ne me vole pas, j'en suis sûr." — the SAME vaudeville couplet already excluded by the parent battery ("Air du Piège": appositive adjective phrase in verse + finite negative clause).
  - Why the uncapped pass caught it: the window contains "!" at distance ("Je le défie, hélas ! de me rien prendre…") and infinitive-shaped tokens "prendre", "rendre", "voler" — but those belong to a DIFFERENT speaker's later verse ("Je le défie, hélas ! de me rien prendre… / Pour me voler quelque chose, il faudrait / Qu'il commençât par me le rendre"). The head's own clause has no infinitive and no exclamation.
  - Excluded with cause: cross-speaker window bleed; head's clause = appositive + finite negative clause; infinitives governed by a later speaker's modal construction, not an exclamatory infinitive under the head.

No uncapped-only candidate exists. No separator-variant candidate exists. The parent battery's two comma hits remain the complete hit inventory (the second, `scribe-le-savant.txt` @44460 "celui-là, j'espère, ne sera pas exigeant sur la dot", is finite-clause, no "!" even in 400 chars).

## Per-clause pass/fail

- Clause 1 (≥1 genuine under extended separators / uncapped windows): FAIL — 0 genuine of 1 candidate in 465,531 chars; the single candidate is a cross-speaker bleed excluded with cause. The comedy zero stands under the full separator class.
- Clause 2 (confirmed zero = not a pattern-form artifact): PASS — executed per the pre-registered recall census; every candidate classified; separator coverage measured (only commas attested, so dash/paren variants add nothing). Verdict **null** per §4.

## Verdict

**NULL** — the comedy-register zero is not a separator-class or window-truncation artifact; no standing verdict contradicted; no red-team verdict touched.

## Follow-ups (nulls regenerate work — proposed for the supervisor to queue)

1. **`disloc-reinforced-comedy-widercorpus`** (P2) — raise coverage beyond the 6 files (more Scribe/Labiche vaudevilles and comedies on fr.wikisource/Gallica): 465,531 chars is a thin base for a register-level fence; ≥1 genuine re-opens; confirmed zero hardens. Bar: 0 genuine in ≥1M added chars confirms; any genuine re-opens.
2. **`disloc-reinforced-verse-vs-prose-comedy`** (P3) — the only hits come from vaudeville verse couplets; test whether the reinforced-head census behaves differently in sung verse vs spoken dialogue windows within the comedy register. Bar: ≥1 genuine in either verse or prose windows re-opens that sub-register; confirmed zero in both fences the whole comedy register.

## Files

- Report: `code/crowd17/report_inbox/battery-disloc-reinforced-comedy-recall.md` (this file)
- Census script: `code/crowd17/next-token/disloc_reinforced_comedy_recall_census.py`
- Raw census JSON: `code/crowd17/next-token/disloc-reinforced-comedy-recall_census.json`
- Corpus: `code/side-period/corpus/{scribe-le-savant,scribe-le-lorgnon,labiche-voyage-perrichon,labiche-la-cagnotte,labiche-29-degres-ombre,labiche-affaire-rue-lourcine}.txt`
- Queue: `code/crowd17/next-token/battery-queue.json` — target `disloc-reinforced-comedy-recall` set to status `verdict`/null via temp-file + atomic rename, own entry only, pre-write assert + post-write re-validation
