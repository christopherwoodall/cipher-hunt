# Battery report: reinforced-modal-inf-prose — verdict: NULL

**Target id:** `reinforced-modal-inf-prose`
**Date:** 2026-10-09
**Verdict:** NULL (fence-hardening deliverable produced; no attestation)

## Bar (verbatim from queue)

> run the SAME modal/perception P1/P2/P3 search on the 27.66M-char 19th-century
> prose corpus (the reinforced-pour-inf-diagnostic corpus); >=1 genuine
> attestation re-opens; confirmed zero hardens the fence.

Numbered clauses:
- **C1 (re-open arm):** ≥1 genuine modal/perception-governed bare exclamatory
  infinitive under a reinforced-demonstrative head re-opens the pairing → FAIL
  (0 genuine).
- **C2 (fence arm):** confirmed zero hardens the fence → PASS (vacuous:
  0 genuine over 27,656,185 chars).
- **Adverses:** "coordinates with, does not duplicate, the preposition-governed
  reinforced-pour-inf-diagnostic battery" → ANSWERED: this census uses only
  modal/perception/causative governors (faire, laisser, pouvoir, vouloir,
  devoir, savoir, voir, regarder, entendre, écouter, sentir); the pour/de/à
  preposition set is untouched. No duplication.

## Method

Script: `code/crowd17/next-token/reinforced_modal_inf_prose_census.py`
(re-runnable; output `reinforced-modal-inf-prose_census.json`).
P1/P2/P3 copied verbatim from `reinforced_modal_inf_drama_census.py`:
P1 = reinforced demonstrative head (celui/celle/ceux/celles)-là/-ci (+çà-là/çà-ci)
followed by [,;:]; window = demonstrative through next [!?.], capped at 180 chars.
P2 = window must contain "!". P3 = modal/perception/causative verb form +
0–3 clitics + bare infinitive (er/ir/re/oir), applied after the comma.

Corpus gate: 20 prose files (guizot-memoires t1/t2/t3/t5-t6, nesselrode v7–v10,
revue-deux-mondes 1841 q1–q4, metternich-papiere v4/v6, talleyrand-memoires v1,
pozzo-di-borgo v1, levant-correspondence-1841-p3, miserables1, tocqueville t1/t2)
= **27,656,185 chars — exact match with the parent corpus counts.**

## Findings

- 231 reinforced-demonstrative-comma hits → **2 modal/perception-inf candidates**,
  both hand-read with ±450-char context → **0 genuine**.
- Both candidates are the same nesselrode-v8 passage (@165979 "celle-ci",
  @165994 "celle-là" — the second is the regex re-matching inside the first
  window):
  > "…comme on critique l'intimité **de celle-ci, de celle-là**, et comme on a
  > vite **fait de faire penser** hommes et femmes sur toute chose!"
- Kill causes (both windows):
  1. "celle-ci"/"celle-là" are **objects of "l'intimité de"** (contrastive
     pair), not dislocated topics — the head never licenses anything.
  2. "penser" is governed by causative "faire" under the **finite** "on a
     (vite) fait" — the "!" force falls on a finite clause, not on a bare
     exclamatory infinitive under the head.
- Cross-register: the drama parent (`reinforced-modal-inf-drama`) found
  **0 candidates in 2,939,372 chars**. Combined modal-governed yield:
  2 candidates / 30.6M chars / 0 genuine.

## Verdict rationale

C1 fails (no attestation), C2 passes (confirmed zero hardens the fence).
Per §4 and the sibling zero-yield convention (e.g. personal-tonic-governed-excl-
prose-recall), a confirmed zero is an absence, not a kill: the existential
claim fails, but the fence-hardening deliverable is what the bar's second arm
asks for. **NULL.**

## Scope

Closes the modal/perception/causative-governed arm of the reinforced-head
pairing in prose at battery grade. Untouched: the preposition-governed
(reinforced-pour-inf-diagnostic) family, the drama register (already zero),
the interrogative-force variant, bare (ungoverned) shapes. §7 intact;
no standing/red-team verdict contradicted. R5005, sealed gates, red-team
adjudication queue untouched. `canonical.py` never used.

## Follow-ups proposed (all verified ABSENT from queue)

1. `reinforced-modal-inf-prose-interr` (P4) — same modal/perception search
   with '?' termination admitted ('celui-là, pour croire ?' pattern); the
   sibling prose recalls found '?' variants productive.
2. `reinforced-modal-inf-drama-compare` (P4) — formalize the cross-register
   comparison: drama 0/2.94M vs prose 0 genuine/27.66M; test whether the
   modal-governed fence extends across registers at a stated significance.
3. `reinforced-causative-inf-prose` (P4) — split the causative sub-arm: both
   prose candidates were "faire"-causative; dedicated causative-only census
   with wider clitic/infinitive patterns to close the sub-arm properly.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-reinforced-modal-inf-prose.md`
- Script + data: `code/crowd17/next-token/reinforced_modal_inf_prose_census.py`,
  `code/crowd17/next-token/reinforced-modal-inf-prose_census.json`
- Queue: `reinforced-modal-inf-prose` → `status: verdict`, `result: null`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; disk re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion.
