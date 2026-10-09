# Battery report: personal-tonic-pour-only-prose

- Target id: `personal-tonic-pour-only-prose`
- Claim: restrict the governor to 'pour' only (the canonical governed-exclamatory governor) to cut finite-matrix confounds
- Date: 2026-10-09
- Stream: corpus census per target charter; the 1,847-pair repaired parse not applicable (no cipher data touched). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, resumed by a pronoun. "Governed exclamatory infinitive" = an infinitive led by a preposition and carrying the exclamatory force itself ("Moi, pour rire !"). "Tonic pronoun" = moi/toi/lui/elle/nous/vous/eux.

## Parentage

Follow-up #2 of `personal-tonic-governed-excl-prose` (NULL 2026-10-09): that battery's 26 candidates / 0 genuine zero was carried mostly by finite-matrix confounds (10 finite-matrix-governed, 4 noun-governed). This run restricts the governor to "pour" only — the canonical governed-exclamatory governor — to cut those confounds.

## Bar (verbatim, pre-registered before testing)

"Restrict the governor to 'pour' only; >=1 genuine under pour-only re-opens; confirmed zero fences"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **Clause 1 (restrict):** run the tonic-pronoun + pour-governed exclamatory-infinitive census on the same 27.66M-char prose corpus → the pour-only restriction executes.
2. **Clause 2 (re-open):** ≥1 genuine personal-tonic-pronoun topic + pour-governed exclamatory infinitive → the arm re-opens.
3. **Clause 3 (fence):** a confirmed zero (every pour-only candidate classified with cause) → the pour-only arm is fenced.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/personal-tonic-pour-only-prose.lock` on start (2026-10-09T15:11Z); no prior lock existed for this id.
2. Re-runnable script: `code/crowd17/next-token/personal_tonic_pour_only_prose_census.py`; raw results in `code/crowd17/next-token/personal-tonic-pour-only-prose_census.json`.
3. P1/P2 copied VERBATIM from the parent (`personal_tonic_governed_excl_prose_census.py`); P3 restricted as the bar requires:
   - P1: `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]` case-insensitive; window = text from the pronoun through the next `[!?.]`, capped at 180 chars.
   - P2: the window must contain "!" before its end.
   - P3 (pour-only): strict `\bpour\s+[a-z…]{2,}(er|ir|re|oir)\b`; loose (clitic-tolerant, tagged separately) = same with up to 2 intervening short words. All candidates hand-classified (regex cannot judge exclamatory illocutionary force or topic status).
4. Corpus VERBATIM from the parent (20 files, 27,656,185 chars, computed in-session — matches exactly):
   - 1841-register prose, 17 files, `code/side-period/corpus/`: guizot-memoires t1/t2/t3/t5-t6, nesselrode v7/v8/v9/v10, revue-deux-mondes-1841 q1/q2/q3/q4, metternich-papiere v4/v6, talleyrand-memoires-v1, pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3.
   - Wider 19th century, 3 files, `data/`: gutenberg-17489-miserables1.txt, gutenberg-30513-tocqueville-t1.txt, gutenberg-30514-tocqueville-t2.txt.

## Yield

4,495 pronoun-comma hits across 27,656,185 chars → **3 pour-only candidates** (2 strict, 1 loose-only), all hand-classified with 300/350-char wider context. **0 genuine.**

The restriction worked as designed: it cut the candidate set from 26 to 3 (an 88% reduction), eliminating all de-/à-governed windows. The finite-matrix confound class is not fully gone — 2 of the 3 remaining are still finite-matrix-governed — but the confound carrier set is now exhaustively classified.

## Classification (all 3, with cause)

Finite-matrix-governed (2):
- guizot-t2 @282484 — "lui, pour prendre la parole: «Ici, d'Argout!»"; "pour prendre" is a purpose adjunct of the finite matrix ("il l'envoyait… Je l'ai entendu s'écrier"); "!" belongs to the downstream quote, not the infinitive. (Parent's [01].)
- rdm-q4 @1633288 — "eux; …envoyés dans le Liban pour exciter la révolte!"; "pour exciter" governed by the participle "envoyés" (finite matrix); "!" terminates the finite clause. (Parent's [15].)

False positive, noun phrase (1):
- rdm-q1 @112215 — "pour ceci votre" (loose); "pour ceci" is prepositional, "votre tête" is a noun phrase, not an infinitive; finite "j'aurai"; "!" terminates the finite clause. (Parent's [03].)

No unclassified residue. All three are the same items the parent already classified (01, 03, 15) — no new windows surfaced under pour-only.

## Per-clause pass/fail

1. **Clause 1 (restrict): PASS.** The pour-only census ran clean on the full 27.66M-char corpus: 4,495 pronoun-comma hits → 3 pour-only candidates, all hand-classified.
2. **Clause 2 (re-open): FAIL at kill grade.** Zero genuine tonic-pronoun topic + pour-governed exclamatory infinitive windows. The distributional test rejects at the lane's standard (full candidate classification, zero genuine, same corpus as the parent).
3. **Clause 3 (fence): FIRES.** The confirmed zero fences the pour-only governed-exclamatory arm in prose.

## Verdict: KILL

The pour-only route for the governed exclamatory infinitive under a personal-tonic-pronoun topic is fenced at battery grade in 1841 prose. The restriction executed as designed (88% candidate reduction), and the remaining confounds classify cleanly — the arm has no surviving leg.

## Scope

Kills only the pour-only governed-exclamatory arm in prose. Untouched: the 12 genuine governed-exclamatory cases in drama (different register, drama-wide), the bare-shape tonic-pronoun findings, the @1029 clitic/tonic-dislocation routes (already dead), the parent's NULL verdict (not contradicted — this battery was its proposed follow-up), and all standing/red-team verdicts. No value named, nothing adjudicated. §7 intact. Per §4 (kill), no follow-ups.

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/personal-tonic-pour-only-prose.lock` created on start, deleted on completion.
- Census script: `code/crowd17/next-token/personal_tonic_pour_only_prose_census.py`; raw JSON: `code/crowd17/next-token/personal-tonic-pour-only-prose_census.json`.
- `battery-queue.json` updated via temp-file + rename (own entry only; no downgrade).
