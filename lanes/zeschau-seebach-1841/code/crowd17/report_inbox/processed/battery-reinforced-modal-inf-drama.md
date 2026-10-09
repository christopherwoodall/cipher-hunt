# Battery report: reinforced-modal-inf-drama

- Target id: `reinforced-modal-inf-drama`
- Claim: "census reinforced-demonstrative heads + modal/perception-governed bare exclamatory infinitive in the drama corpus ('Celui-la, - ... Voir pendre a quatre clous ... !')"
- Date: 2026-10-09
- Worker: battery worker (subagent d481439f-6ab4-40df-8bbb-127b32ba446c)
- Stream: not applicable — corpus census against period French drama, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci, ceux-ci, celle-ci, celles-ci; also çà-là/çà-ci). "Exclamatory infinitive" = an infinitive used as an exclamation ("Moi, me taire !"). "Modal/perception-governed" = the infinitive is governed by a modal, perception, or causative verb (pouvoir/vouloir/devoir/savoir/falloir, voir/entendre/regarder/écouter/sentir, faire/laisser), as in "celui-là, voir pendre à quatre clous !". "Genuine attestation" = the reinforced head actually heads the modal/perception + infinitive construction: the infinitive phrase is the exclaimed phrase, not embedded in a downstream finite clause.

## Parentage

Follow-up of the NULL `reinforced-pour-inf-drama` (2026-10-09), which found 0 genuine reinforced-head + preposition-governed (pour/à/de) exclamatory infinitives in 2.94M characters of drama (41 dem-comma heads exist; 1 candidate, classified as finite-clause near-miss). This battery asks whether the licensor class survives with a modal/perception governor instead of a preposition. Does not duplicate `disloc-demonstrative-reinforced` (reinforced heads, bare infinitive, prose), `reinforced-pour-inf-drama` (preposition governors, drama), or the in-flight `reinforced-modal-inf`-family siblings (this is the drama arm).

## Bar (verbatim, pre-registered before testing)

">=1 genuine reinforced-head + modal/perception-governed bare exclamatory infinitive in drama shows the licensor class survives with a modal/perception governor; confirmed zero fences the modal governor too"

Numbered pass/fail clauses (restated before testing, not modified after):

1. ≥1 genuine dislocated reinforced-demonstrative head (celui-là / ceux-là / celle-là / celles-là / celui-ci / ceux-ci / celle-ci / celles-ci) + modal/perception-governed bare exclamatory infinitive exists in the drama corpus. If yes: the licensor class survives with a modal/perception governor (promote).
2. If clause 1's census is a confirmed zero — every candidate window classified, false friends and OCR excluded with cause — the modal governor is fenced too (null per §4: zero is an absence, not a refutation).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock `code/crowd17/next-token/locks/reinforced-modal-inf-drama.lock` on start (agent id + UTC timestamp; no stale or fresh lock existed for this id); deleted on completion.
2. Corpus: same 14 distinct-play drama files as `reinforced-pour-inf-drama` (2,939,372 characters): dumas-mariage-louis-xv-1841.txt, vigny-chatterton-1835.txt, musset-comedies-proverbes-1850.txt, hugo-hernani.txt (one-edition-per-play; hugo-hernani-1870.txt excluded), hugo-ruy-blas.txt, hugo-burgraves.txt, dumas-antony.txt, dumas-tour-de-nesle.txt, dumas-henri-iii.txt, dumas-kean.txt, scribe-bertrand-et-raton.txt, scribe-verre-d-eau.txt, labiche-chapeau-de-paille.txt, labiche-martin-poudre-aux-yeux.txt.
3. Ran a reproducible census script: `code/crowd17/next-token/reinforced_modal_inf_drama_census.py`. P1 = same DEM_REINF inventory as the sibling batteries; P2 = window contains "!"; P3 = modal/perception/causative governor form (faire, laisser, pouvoir, vouloir, devoir, savoir, voir, regarder, entendre, écouter, sentir + conjugated forms) followed by 0–3 clitics and a bare -er/-ir/-re/-oir infinitive. Raw results in `code/crowd17/next-token/reinforced-modal-inf-drama_census.json`.

## Window-level evidence

### Census yields

- Drama register: 41 dem-comma hits across 14 files → **0 pattern candidates**.
- Excluded-edition spot-check: `hugo-hernani-1870.txt` = 0 dem-comma hits → 0 candidates. The edition choice hides nothing.
- Widened governor set (falloir forms added after the fact): 2 extra candidates — both already in the manual scan (see below).

### Manual audit of ALL 8 dem-comma + "!" windows (pattern-free, to verify the zero is not a pattern artifact)

1. musset-comedies-proverbes-1850.txt — `celle-ci, pleine de jeunes gens, de valets!` — no infinitive, no governor. Excluded.
2. musset-comedies-proverbes-1850.txt — `celui-ci : Cordiani !` — proper noun. Excluded.
3. musset-comedies-proverbes-1850.txt — `celui-là : Je peux si je veux!` — modals present but no infinitive; conditional finite frame ("si je veux"). Excluded.
4. dumas-tour-de-nesle.txt — `celui-là, il faut le sauver… Oh !` — "il faut" (modal) + "sauver" (infinitive), BUT the infinitive is embedded in a complete finite clause ("il faut le sauver"); the "!" terminates the interjection "Oh !". The head is topic of the finite clause, not of an exclamatory infinitive. Excluded with cause.
5. dumas-henri-iii.txt — `ceux-là, morbleu !` — no infinitive. Excluded.
6. scribe-bertrand-et-raton.txt — `ceux-là, et, s'il fallait les perdre ou les voir compromis… j'aimerais mieux mourir !` — "fallait" modal + "perdre" infinitive BUT finite conditional frame; "voir compromis" = perception verb + past participle (not infinitive). The "!" terminates the finite sentence. Excluded with cause.
7. scribe-verre-d-eau.txt — `ceux-là, je ne suis pas libre de les accueillir…` (the sibling battery's 1 governed-infinitive near-miss) — "de"-governed infinitive embedded in the finite negative clause "je ne suis pas libre de les accueillir"; not the exclaimed phrase. Excluded with cause (previously classified).
8. scribe-verre-d-eau.txt — `celui-là, j'en suis sûre… Et la reine jusque-là froide et sévère, a dit… qu'elle vienne !` — "vienne" is finite subjunctive. Excluded.

## Per-clause pass/fail

1. ≥1 genuine reinforced-head + modal/perception-governed bare exclamatory infinitive in the 2.94M-char drama corpus: **FAIL (confirmed zero).** 0 pattern candidates; 8/8 dem-comma + "!" windows hand-classified with cause; 0 genuine. The excluded second Hernani edition adds 0 dem-comma hits.
2. Confirmed zero → the modal governor is fenced: **EXECUTED.** With the preposition-governed zero from `reinforced-pour-inf-drama` and this modal/perception-governed zero, the reinforced-head licensor class is fenced under both governor families in the drama register. Per §4 this is a **null**, not a kill (zero is an absence).

## Adverses, answered

- None pre-registered ("Adverses: None").
- Self-check: no contradiction with the parent NULL `reinforced-pour-inf-diagnostic` (prose, preposition-governed zero) or the sibling NULL `reinforced-pour-inf-drama` (drama, preposition-governed zero). This battery completes the second governor family of the drama program.
- Self-check: no contradiction with `disloc-demonstrative-drama-dialogue` (bare tonic heads zero in drama dialogue) — different head inventory (reinforced vs bare), same fence direction.
- §5.2: no standing red-team verdict touched; R5005 untouched.

## Verdict: NULL (confirmed zero; modal/perception governor fenced in the drama register)

0 genuine dislocated reinforced-demonstrative + modal/perception-governed bare exclamatory infinitive attestations in 2,939,372 characters of 19th-century French drama. Combined with `reinforced-pour-inf-drama` (preposition-governed zero), the reinforced-head + exclamatory-infinitive pairing stays fenced under both governor families. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **reinforced-modal-inf-prose** (P3): run the SAME modal/perception P1/P2/P3 search on the 27.66M-char 19th-century prose corpus (reinforced-pour-inf-diagnostic's corpus). Bar: ≥1 genuine modal/perception-governed attestation in prose re-opens the governor class at register level; confirmed zero fences the modal governor across both registers. (Coordinates with, does not duplicate, the preposition-governed `reinforced-pour-inf-diagnostic`.)
2. **gov-modal-inf-register-drama** (P3): corpus-wide census of modal/perception-governed exclamatory infinitives in the 14-play drama corpus with ANY topic ("il faut voir !", "Voir pendre !"). Bar: if the construction is attested drama-wide with other topics, the reinforced-head gap is head-specific and the cross-register fence stands; if unattested, the zero is register-level (the construction itself is absent from drama print, so head-licensing is moot). (Coordinates with `gov-excl-inf-register-drama`, the preposition-governed register arm, if queued; does not duplicate it.)
3. **reinforced-modal-inf-drama-window-widen** (P4): re-run P1 admitting dash/parenthesis pause marks after the head ("celui-là — voir mourir !") and a 400-char window, on the same 14-play corpus. Bar: ≥1 genuine attestation in the widened windows re-opens the pairing; confirmed zero closes this battery's unsearched-window gap. (Same recall-gap closure as `reinforced-pour-inf-drama-recall` #1, for the modal governor family.)

## Bookkeeping

- Census script: `code/crowd17/next-token/reinforced_modal_inf_drama_census.py` (re-runnable; outputs reinforced-modal-inf-drama_census.json).
- Report: code/crowd17/report_inbox/battery-reinforced-modal-inf-drama.md (this file).
- Lock created on start, deleted on completion. No stale lock existed.
- R5005, sealed gates, red-team queue untouched. Every number traces to the named corpus files or the census script; no invented data.
