# battery-personal-tonic-pour-inf-drama-corpus — report

Follow-up #1 from NULL battery-personal-tonic-pour-inf-drama (2026-10-09):
the intended tonic-pronoun + pour-governed exclamatory infinitive test, run
in the true venue — the plaintext drama corpus.

## Bar (verbatim, pre-registered)

">=1 genuine locates the governor in the true drama venue; a confirmed zero hardens the fence at the governor class where the bar is actually testable."

## Numbered clauses

1. **Clause 1 (attest arm):** ≥1 genuine personal tonic pronoun topic + pour-governed
   exclamatory infinitive in the drama register locates the governor in the true
   drama venue.
2. **Clause 2 (fence arm):** a confirmed zero (every candidate classified with
   cause) hardens the fence at the governor class — the pour-only governor —
   where the bar is actually testable.

## Method

- Venue: the plaintext drama corpus `code/side-period/corpus/` — the sibling's
  pinned 14-play set (one edition per play; `hugo-hernani.txt` Hetzel 1889
  duplicate excluded by gate).
- Re-runnable script: `code/crowd17/next-token/personal_tonic_pour_inf_drama_census.py`
  (sibling taxonomy from `personal_tonic_governed_excl_drama_census.py`,
  P3 restricted to the pour-only governor). Raw census JSON alongside.
- P1 (dislocation): `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]` (case-insensitive).
- Window: from the pronoun through the next `[!?.]` (inclusive), capped at 180 chars.
- P2 (exclamatory filter): window must contain `!`.
- P3 (pour-governed-infinitive candidate):
  strict — `\bpour\s+[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`;
  loose (clitic-tolerant, tagged separately) — `\bpour\s+(?:[a-zàâäçéèêëîïôöùûü']{1,4}\s+){1,2}[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`.
- Manual classification of all candidates (regex cannot judge exclamatory
  illocutionary force or topic status).

## Corpus gate (verified on disk before testing)

- 14 unique plays, 2,969,582 chars total, 1,986 pronoun-comma hits — matches
  the sibling battery's census exactly. `hugo-hernani.txt` present-but-excluded
  as expected. Gate: PASS.

## Yield

- 1,986 pronoun-comma hits over 2,969,582 chars.
- **5 pour-governed-exclamatory candidates** (2 strict, 3 loose-only), all
  hand-classified. **0 genuine.**

## Classification (all 5, with cause)

No-true-infinitive false positives (2):
- [01] dumas-antony.txt @58307 — "moi, pour la vie entière, je serai loin… Ah !"
  loose-only ("pour la vie entière"): "la vie" is a noun phrase, not an
  infinitive; "entière" (-re ending) tripped the loose pattern.
- [02] dumas-tour-de-nesle.txt @62103 — "je serais si heureuse de mourir
  pour mon chevalier !" loose-only ("pour mon chevalier"): noun phrase, not
  an infinitive.

Purpose adjuncts of finite clauses (2):
- [00] hugo-hernani-1870.txt @44016 — "Moi, pour vouloir si peu je ne suis pas
  si fou !" strict ("pour vouloir"): purpose adjunct of the finite matrix
  "je ne suis pas si fou"; the "!" terminates the finite clause, not the
  infinitive phrase.
- [04] musset-comedies-proverbes-1850.txt @187096 — "nous, dans ces palais
  somptueux, nous attendons qu'on nous insulte pour tirer nos épées !"
  strict ("pour \ntirer"): purpose adjunct of the finite matrix
  "nous attendons qu'on nous insulte"; the tonic "nous" is the resumed subject
  of the finite clause.

Finite-matrix-governed (1):
- [03] scribe-bertrand-et-raton.txt @161965 — "c'est pour moi, pour me sauver
  qu'il marcherait à la mort !…" loose-only ("pour me sauver"): the infinitive
  is governed by the finite conditional "marcherait"; the "!" terminates the
  finite clause.

Nearest near-miss note: [03] is a tonic topic followed by a pour-governed
infinitive — but governed by a finite conditional, failing the
exclamatory-force-on-the-infinitive gate (same classification as the sibling
battery's [19]).

## Per-clause pass/fail

1. **Clause 1 (attest arm): FAIL — antecedent false.** Zero genuine tonic-topic
   + pour-governed exclamatory infinitive windows in 5 candidates over
   2,969,582 chars. The "Moi, pour rire !" shape is unattested with the
   pour-only governor at battery level in drama.
2. **Clause 2 (fence arm): PASS.** The zero survives manual classification of
   the full candidate set: 2 regex false positives (noun phrases), 2 purpose
   adjuncts of finite clauses, 1 finite-matrix-governed. No unclassified
   residue. The fence hardens at the pour-governor class in the drama register:
   even with the dominant "de/à" finite-matrix confounds removed (the confound
   class that carried the sibling's all-governor zero), no tonic-pronoun topic
   licenses a pour-governed exclamatory infinitive.

## Adverse

"prior NULL was a venue mismatch, not a refutation of the claim" — ANSWERED.
This battery ran in the correct venue (plaintext drama corpus, sibling's pinned
14-play set); the confirmed zero is now a genuine corpus finding, not a venue
artifact. Nothing in this run contradicts a standing red-team verdict; no
verdict was downgraded; no data invented; the sibling's all-governor NULL
(battery-personal-tonic-governed-excl-drama) is corroborated, not re-litigated.

## Verdict

**NULL** — confirmed zero, not a refutation (§4: zero is an absence, not a
kill; sibling precedent battery-personal-tonic-governed-excl-drama). The
fence at the pour-governor class is hardened at drama-register level: tonic
pronouns do not license the pour-governed exclamatory infinitive even under
the cleanest possible search (pour-only, the canonical governed-exclamatory
governor). This supports the reinforced-head fence family and does not revive
any stream tonic-dislocation route.

## Follow-ups proposed (nulls regenerate work)

1. **personal-tonic-pour-only-drama-recall (P3)** — pour-only net with the
   sibling's recall widening (400-char window + "?" termination):
   recall-gap closure specific to the pour governor. Distinct from the
   already-queued all-governor `personal-tonic-governed-excl-recall`
   (different net, different bar). Verified absent from battery-queue.json.
2. (Coverage already queued — not re-proposed:) `personal-tonic-pour-only-prose`
   (queued) runs the pour-only net on the prose corpus — the register-bound
   check; `tonic-pronoun-stream-locate` (queued) is the stream-side tonic-group
   prerequisite.

## Standing items

- R5005: never touched. Sealed gate instances, red-team adjudication queue: untouched.
- Standing §7 values: untouched, none contradicted.
- No numbers invented: every count traces to the census script output above
  (`personal-tonic-pour-inf-drama_census.json`).
- Lock: created on start (881ac421-1166-426d-8ad4-3d6523e2dd85, 2026-10-09T15:00:39Z),
  deleted on completion.
