# Battery report: reinforced-head-narrative-uncapped-drama

**Verdict: NULL** (fence executed — the deep-narrative recall gap is closed; the zero holds under uncapped punctuation-aware windows).

## Bar (verbatim, pre-registered)

"punctuation-aware windows confirm the zero across narrative-heavy plays; any genuine attestation re-opens the governed pairing"

Numbered clauses:
- C1 — punctuation-aware (uncapped) windows confirm the zero across narrative-heavy plays.
- C2 — any genuine attestation re-opens the governed pairing.

## Method

Two passes over the 14-play drama corpus from `reinforced-pour-inf-drama-recall`
(`hugo-hernani-1870.txt` as the single Hernani edition; `hugo-hernani.txt`
run separately as the excluded edition):

- **Pass B (verbatim reproduction):** DEM_B separator class
  `[,;:\-—()]`, 400-char cap, window = dem hit → next `[!?.]` or cap,
  `"!"` filter, GOV_INF = `\b(pour|à|a|de|d[''])\s+(…1-6 chars…\s+){0,2}\b\w{2,}(er|ir|re|oir)\b`
  on after-separator text.
- **Pass C (the new work):** identical, except the window runs from the dem
  hit to the NEXT sentence-end `[!?.]` with no cap (5000-char safety cap;
  never hit). Every pass-B window uncapped at 400 is resolved individually.

Script: `code/crowd17/next-token/reinforced_head_narrative_uncapped_drama.py`;
data: `code/crowd17/next-token/reinforced-head-narrative-uncapped-drama_census.json`.

## Findings

- Pass B reproduces the parent's corpus exactly: **41 dem hits** across the
  14 plays (2,969,582 chars), matching the topology battery's 41/41.
- **Exactly one window uncapped at 400:** `dumas-tour-de-nesle.txt` @79885
  ("celui-ci") — the residual flagged by the parent. Pass C resolves it at
  **415 chars** (sentence end 15 chars past the cap): "celui-ci, des murs
  aussi sourds et aussi épais que ceux-ci, des murs qui étouffent les
  cris…" — a narrative récit passage; the head is followed by a noun
  phrase, the window contains **no "!" and no governed infinitive**.
- Pass-B candidate windows: 3. Pass-C candidate windows: **3 — identical,
  0 C-only**. The uncapped resolution adds nothing.
- All 3 hand-classified with full context, **0 genuine**:
  1. `hugo-ruy-blas.txt` @34184 ("à + à quatre") — regex false positive:
     "quatre" ends in "re" but is not an infinitive; the true infinitive
     "Voir" is bare, and the head "Celui-là" is its object
     ("Voir pendre à quatre clous…"), not its governor.
  2. `dumas-kean.txt` @43821 ("de + de produire") — "l'impuissance de
     produire": the infinitive is governed by the noun "impuissance"; the
     head "Ceux-là" belongs to a different clause ("Ceux-là, c'est la
     gloire de la presse…").
  3. `scribe-verre-d-eau.txt` @36952 ("de + de les accueillir") — the
     topology battery's #38: head as the infinitive's OBJECT via clitic
     "les" ("je ne suis pas libre de les accueillir"); "libre" governs,
     the head never does.
- Excluded Hernani edition: 0 dem hits, 0 candidates.

## Per-clause result

- C1 — **PASS**: the zero is confirmed under punctuation-aware uncapped
  windows across all 14 narrative-heavy plays (41/41 windows resolved, 0
  genuine; the single uncapped-at-400 window resolved at 415 chars with
  no candidate).
- C2 — **does not fire (vacuous)**: no genuine attestation, nothing re-opens.

## Scope

Closes the deep-narrative recall gap for the reinforced-head governed
pairing in drama: no attestation was hiding past the 400-char cap.
Untouched: the comedy and prose registers (no uncapped treatment there
yet); the topology battery's direction-of-government finding (heads as
infinitive objects, never governors); the sibling follow-ups already
queued (`reinforced-head-modal-inf-drama`, `gov-inf-complement-prose-recall`,
`head-government-direction-redteam`). No standing/red-team verdict
contradicted; §7 intact. Canonical-stream caveat stands (this battery
works the period corpus, not R5005).

## Follow-ups proposed (all verified ABSENT from queue)

1. `reinforced-head-uncapped-prose-recall` (P4) — same punctuation-aware
   uncapped-window method over the 27.66M-char prose corpus for the
   reinforced-head governed pairing; closes the identical recall gap in
   prose, where long narrative passages are the norm.
2. `reinforced-head-uncapped-comedy-recall` (P4) — same treatment over the
   19-file comedy corpus (2.54M chars); closes the recall gap in the
   register where dislocation is significantly rarer.

## Bookkeeping

- Queue: `reinforced-head-narrative-uncapped-drama` → `status: verdict`,
  `result: null` (pre-write assert passed — was queued/verdictless;
  temp-file + rename; disk re-read confirms verdict/null; own entry
  only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
  `canonical.py` never used. No lock staleness noted.
