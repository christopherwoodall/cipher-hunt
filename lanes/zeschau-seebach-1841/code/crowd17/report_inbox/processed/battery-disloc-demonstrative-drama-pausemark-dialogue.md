# Battery report: disloc-demonstrative-drama-pausemark-dialogue

- Target id: `disloc-demonstrative-drama-pausemark-dialogue`
- Claim: "the pausemark census extends to dialogue-scoped drama text (speaker-header/stage-direction stripped)"
- Date: 2026-10-09
- Worker: battery worker (subagent 3a0b8d0c)
- Stream: not applicable — corpus census against period French drama, per target charter. The 1,847-pair repaired parse was not used. `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "demonstrative" = cela, ceci, ça (tonic demonstratives). "Pausemark" = a pause mark that is not a comma: `!`, `?`, `--` / em-dash, `...` / ellipsis, `:`, `;`. "Bare exclamatory infinitive" = an infinitive used as an exclamation with no preposition (de, pour), no "que", no resumptive clitic. "Dialogue" = the spoken speech of the plays, after front matter (preface, title page, cast list), ALL-CAPS speaker headers, and whole-line stage directions are removed.

## Bar (verbatim, pre-registered before testing)

"Same pausemark census on dialogue-scoped drama text; >=1 genuine re-opens at dialogue level; confirmed zero closes the dialogue level too"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated-demonstrative (cela/ceci/ça) + NON-COMMA separator + [bare infinitive] ! attestation exists in dialogue-scoped drama text. If yes: arm (a) of ce87-1028-role re-opens at dialogue level.
2. If clause 1's census is a confirmed zero — every candidate classified, false friends excluded with cause — the dialogue level is closed too (null per §4: zero is an absence).

## Parentage

Fires follow-up #1 of the battery-level NULL `disloc-demonstrative-drama-pausemark-recall` (2026-10-09): 307 demonstrative+pausemark hits → 120 with `!` in the 70-char window → 0 genuine over the FULL drama text (2,939,372 chars, 14 files, one Hernani edition). This battery asks whether stripping speaker headers and stage directions surfaces any new candidate the full-text census missed.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/disloc-demonstrative-drama-pausemark-dialogue.lock` on start; deleted on completion (see Bookkeeping).
2. Dialogue scoping per file: dropped front matter before the first play-body line (per-file ACTE/PARTIE cut line, verified by hand: dumas-antony 131, dumas-henri-iii 50, dumas-kean 1, dumas-mariage-louis-xv-1841 100, dumas-tour-de-nesle 48, hugo-burgraves 117, hugo-hernani 104, hugo-ruy-blas 130, labiche-chapeau-de-paille 120, labiche-martin-poudre-aux-yeux 48, musset-comedies-proverbes-1850 148, scribe-bertrand-et-raton 54, scribe-verre-d-eau 23, vigny-chatterton-1835 918). Dropped whole-line ALL-CAPS headers (≥70% uppercase letters, ≤80 chars) and whole-line parenthetical stage directions. Kept lines: 2,539,841 chars total over 14 files.
3. Ran the parent's patterns VERBATIM on scoped text: `\b(cela|ceci|ça|ca)\s*(?:[!?…:;]|—+|--+|\.{2,})`, 70-char window must contain `!`, first infinitive-shaped word (er/ir/re ending) after the head before sentence end. Re-runnable script: `code/crowd17/next-token/disloc_demonstrative_drama_pausemark_dialogue_census.py`; raw results: `code/crowd17/next-token/disloc-demonstrative-drama-pausemark-dialogue_census.json`.
4. Mapped each scoped candidate back to its original file offset and checked overlap (±40 chars) against the parent's 120 hand-classified candidates. Every candidate already in the parent set carries the parent's 0-genuine classification. Only the 9 NOT in the parent set were hand-classified (dialogue status verified in original context).

## Results

- **128 candidates** in dialogue-scoped text. 119 overlap the parent's hand-classified set (0 genuine, carried over). **9 are new** (stripping changed adjacencies) — all hand-classified below with original-file offsets:
  1. dumas-mariage-louis-xv-1841 @100405 — "comment cela?" — finite interrogative ("et comment cela?"). Excluded.
  2. dumas-mariage-louis-xv-1841 @148572 — "il a dit cela?" — interrogative with finite verb. Excluded.
  3. dumas-mariage-louis-xv-1841 @157210 — "n'est-ce point cela?" — finite interrogative. Excluded.
  4. dumas-tour-de-nesle @113710 — "Qui t'a dit cela?" — interrogative with finite verb. Excluded.
  5. dumas-tour-de-nesle @128934 — "où cela?" — interrogative, no verb. Excluded.
  6. labiche-chapeau-de-paille @51383 — "Après ça…" — ellipsis continuation of a sentence, no infinitive, no "!". Excluded.
  7. musset-comedies-proverbes-1850 @80006 — "Comment cela?" — interrogative; the infinitive-shaped "voir" in window belongs to "je viens de la voir" (finite clause); the "!" belongs to "Que Lucrèce partait!". Excluded.
  8. musset-comedies-proverbes-1850 @254977 — "tu sauras cela?" — finite interrogative; "colère" is a noun false hit. Excluded.
  9. vigny-chatterton-1835 @141845 — "pourquoi cela?" — finite interrogative. Excluded.

- **0 genuine.** Dialogue-scoped taxonomy matches the parent's: interrogative "cela?"/"ça?" with finite verbs, exclamations over finite clauses, governed/determined demonstratives — never a dislocated topic + bare exclamatory infinitive.

## Per-clause pass/fail

1. ≥1 genuine demonstrative + non-comma separator + [bare infinitive] ! in dialogue-scoped drama: **FAIL (confirmed zero).** 128/128 candidates accounted for (119 carried from the parent's 0-genuine classification; 9 new, all excluded with cause above).
2. Confirmed zero → dialogue level closed: **EXECUTED.** Per §4 this is a **null**, not a kill.

## Adverses, answered

- None pre-registered.
- Self-check: consistent with the dialogue-scoped comma census NULL (`disloc-demonstrative-drama-dialogue`, 0 genuine), the drama full-text NULLs, and the parent pausemark-recall NULL. Arm (a) of ce87-1028-role is now fenced at SEVEN levels: RDM full corpus, RDM quoted dialogue, RDM inversion, drama full text (both Hernani editions), drama dialogue (comma heads), drama full text (non-comma separators), drama dialogue (non-comma separators). No standing or red-team verdict contradicted; §7 intact.

## Verdict: NULL (clause 2 executed)

Confirmed zero: no dislocated-demonstrative + bare-exclamatory-infinitive attestation behind non-comma separators in dialogue-scoped 19th-century French drama (14 files, 2,539,841 scoped characters). Arm (a) stays fenced.

## Follow-ups (nulls regenerate work — all verified absent from the queue)

1. **disloc-demonstrative-inversion-drama-dialogue** (P3): run the postposed-demonstrative census ("[bare inf] !, cela/ceci/ça") on the same dialogue-scoped text; closes the inverted order at dialogue level too.
2. **bare-excl-inf-head-inventory-drama-dialogue** (P3): positive-space complement on the same scoped text — inventory genuine heads of bare exclamatory infinitives in drama dialogue (what CAN head them, if not demonstratives).
3. **arm-a-fence-ratify** (red team, already queued): arm (a) is now fenced at seven levels. Package the fencing reports for red-team ratification.

## Bookkeeping

- Census script: `code/crowd17/next-token/disloc_demonstrative_drama_pausemark_dialogue_census.py` (re-runnable)
- Raw results: `code/crowd17/next-token/disloc-demonstrative-drama-pausemark-dialogue_census.json`
- Report: `code/crowd17/report_inbox/battery-disloc-demonstrative-drama-pausemark-dialogue.md` (this file)
- battery-queue.json: `disloc-demonstrative-drama-pausemark-dialogue` queued → verdict/null via temp-file + rename (pre-write assert queued/verdictless; JSON re-validated post-write; own entry only; claim/bars/evidence/adverses preserved)
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- R5005, sealed gates, red-team queue untouched. Every number traces to the named corpus files or the census script; no invented data.
