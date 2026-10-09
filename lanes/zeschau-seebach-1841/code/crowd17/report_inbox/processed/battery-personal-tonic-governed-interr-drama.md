# Battery verdict: personal-tonic-governed-interr-drama

- Target: `personal-tonic-governed-interr-drama` (battery-queue.json, priority 3, status queued)
- Claim: Drama-register interrogative-force variant: test whether '?' force licenses the tonic-governed pour-infinitive shape.
- Worker: 47747c6f-7c8c-4516-9c81-1d1f16f74ac8. Date: 2026-10-09.
- Lock: `code/crowd17/next-token/locks/personal-tonic-governed-interr-drama.lock` created on start (2026-10-09T16:13:34Z, no stale lock); deleted on completion.
- Corpus: `code/side-period/corpus` drama ingest only. R5005, sealed gates, red-team adjudication queue untouched. `canonical.py` never used (corpus battery).

## Bar (verbatim, pre-registered)

"Same P1/P3 census, drama corpus, first-terminator-'?' filter."

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name arm):** >=1 genuine attestation — tonic-topic + pour/de/à-governed infinitive where the "?" plausibly terminates the infinitive phrase itself (question force on the infinitive) — names the interrogative shape in drama.
2. **C2 (closure arm):** 0 genuine closes the interrogative-force dimension in drama at battery grade.
3. **C3:** no adverses listed.

## Method

Verbatim replication of the parent's `personal-tonic-governed-excl-drama` P1/P3 taxonomy, changing ONLY the P2 termination filter (cf. the prose sibling `personal-tonic-governed-interr-prose`):
- P1: `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]` case-insens; window = pronoun through first `[?!.]`, capped at 400 chars.
- P2: first terminator must be "?".
- P3: strict `\b(?:pour|de|d'|d'|à)\s+[a-z…]{2,}(er|ir|re|oir)\b` + loose clitic-tolerant variant, tagged separately.
- Same 14-play drama set as the parent (hugo-hernani.txt excluded, one edition per play per queue gate).
- Script: `code/crowd17/next-token/personal_tonic_governed_interr_drama_census.py`; data: `code/crowd17/next-token/personal-tonic-governed-interr-drama_census.json`.

**Corpus gate:** 14 plays, 2,969,582 chars, 1,986 pronoun-comma hits — identical to the parent's counts.

**Yield:** 34 candidates (23 strict, 11 loose-only), all hand-classified with ±700-char context.

## Clause results

- **C1: PASS — 1 genuine.**
  - **[06] dumas-henri-iii @86308 — "Moi, monsieur, et pour écrire à qui ?"**
    - G1: "Moi" is the dislocated tonic topic (understood subject of "écrire").
    - G2: "pour écrire" is pour-governed.
    - G3: "?" terminates the infinitive phrase directly (force on the infinitive).
    - G4: no finite verb in the turn (the "et" is a discourse connective, not a governor); self-contained.
    - Full turn context: LA DUCHESSE DE GUISE answers "Voulez-vous bien me servir de secrétaire ?" with "Moi, monsieur, et pour écrire à qui ?" — LE DUC DE GUISE: "Que vous importe ? c'est moi qui dicterai."
- **C2: does not fire (vacuous)** — the re-open arm fired first.
- **C3: PASS** — no adverses listed.

## Non-genuine classification (33/34, stated causes)

- Finite-matrix-governed infinitives (largest class): [00] "Quel moment prenez-vous… pour faire… ?" (vous = finite subject of "prenez"); [01] "Qu'ils m'ont fait boire… Eux… pour me rendre la force?" (pour-inf inside finite "m'ont fait boire" clause); [03] "j'ai grande envie de séduire" (finite "ai"); [04] "qu'avais-je besoin de vous chercher" ("avoir besoin" finite); [05] "j'avais besoin… pour vous exposer" (finite "avais"); [08] "suffiront à payer" (finite "suffiront"); [09] "a besoin… pour empêcher" ("avoir besoin"); [11] "tu ne veuilles nous dire" + "pour promettre" governed by finite "raillez-vous"; [12] "il est doux de passer" (impersonal finite); [13] "il faut… pour aller" ("il faut"); [15] "ce serait l'homme qu'il faudrait… pour soulever" (finite "faudrait"); [18]/[19] "il n'y a pas à trembler" (impersonal finite governs "trembler"; "pour ses jours" is a noun phrase); [21] "qui vous a donné celui de prendre" (finite "a donné"); [22] "il faut de l'argent pour vivre" ("il faut"); [23] "avons-nous à craindre" (finite "avons"); [24] "Attendez-vous… pour savoir" (finite); [26] "aurais-je raison de le croire" (finite "aurais"); [27] "je suis fâchée de n'avoir pu" (finite "suis"); [28] "Seriez-vous… bien aise de l'entendre" (finite "Seriez"); [29] "rien n'est capable de vous faire hésiter" (finite "est"); [30] "vous prenez… c'est pour ne pas monter" (finite turn, purpose adjunct); [31] "qu'est-ce que cela veut dire de s'aller jeter" (finite "veut dire"); [32] "ont-ils commencé à se mouvoir" (finite "ont commencé"); [33] "Qui suis-je… pour mériter" (finite "suis-je").
- Preposition-object pronouns: [02] "entre nous" (nous = object of "entre"); [20] "à lui" (object of "à").
- Noun false positives: [14] "jusqu'à la dernière goutte" ("goutte" noun); [17] "à la première", "à son maître" (nouns; window contains no governed infinitive); [25] "de sa lettre" (noun).
- Vocative / non-topic: [07] "elle" = subject of finite "appartient" ("Votre existence… appartient-elle"); [10] "à moi" preposition object ("elle me confie à moi"); [16] "chez moi" ("à dîner" = noun "dinner").

## Scope and caveats

- **Narrow:** the genuine is INTERROGATIVE, not the '!' exclamatory shape. The parent's exclamatory fence and the prose `personal-tonic-pour-only-prose` KILL stand unrefuted; no stream tonic-dislocation route revived by this battery alone.
- Drama-register only. The prose interrogative sibling closed at 0/53; drama licenses 1 genuine.
- **Sibling note:** `personal-tonic-pour-only-drama-recall` (PROMOTE) found this exact @86308 window genuine under its own interrogative-aware reading; its 0-genuine verdict concerned the exclamatory '!' shape, which this window does not instantiate. No contradiction — different bars.
- No standing/red-team verdict contradicted or downgraded; §7 intact. No value named.

## Verdict: PROMOTE

C1 fires: the interrogative-force variant of the tonic-governed pour-infinitive shape is attested in drama ("Moi, monsieur, et pour écrire à qui ?"). Per §4 (promote), no follow-ups required.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-personal-tonic-governed-interr-drama.md`
- Script + data: `code/crowd17/next-token/personal_tonic_governed_interr_drama_census.py`, `code/crowd17/next-token/personal-tonic-governed-interr-drama_census.json`
- Queue: `personal-tonic-governed-interr-drama` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; re-validated from disk; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
