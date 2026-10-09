# Battery report — disloc-demonstrative-drama-edition-delta

**Target:** `disloc-demonstrative-drama-edition-delta`
**Date:** 2026-10-09
**Worker:** `ad46923c-cc74-4c4d-8bd5-243f74cff987`

## Bar (pre-registered, verbatim from queue)

> Hernani second edition census matches the main edition's zero genuine count; any genuine attestation in the excluded edition re-opens the register question

### Restated as numbered clauses

1. The excluded-edition census matches the main edition's zero genuine count.
2. (Conditional adverse) Any genuine attestation in the excluded edition re-opens the register question.

## Method

Ran the identical P1/P2/P3 + strict/loose cross-check taxonomy from
`disloc_demonstrative_drama_reissue_census.py` (patterns copied verbatim)
against `code/side-period/corpus/hugo-hernani.txt` (the excluded second Hernani
edition, 173,559 chars) alone. Results saved in
`code/crowd17/next-token/disloc-demonstrative-drama-edition-delta_census.json`.
The main-edition baseline is the per-file entry for `hugo-hernani-1870.txt`
in `disloc-demonstrative-drama-reissue_census.json` (203,769 chars).

## Corpus comparison

| Pattern count | hugo-hernani-1870.txt (main) | hugo-hernani.txt (excluded) |
|---|---|---|
| chars | 203,769 | 173,559 |
| dem-comma hits (P1) | 1 | 1 |
| exclamatory candidates (P2) | 1 | 1 |
| genuine | 0 | 0 |
| strict cross-check hits | 0 | 0 |
| loose cross-check hits | 1 | 1 |

## Window-level evidence

**Excluded edition, the single candidate** (@167356, dem "cela", inf_hits=[]):

> `cela, c’est assez !`

Classification: excluded with cause. No infinitive token anywhere in the
window (inf_hits empty); the demonstrative is the subject of the finite
clause "c'est assez", not a fronted topic before a bare infinitive. It is the
same verse line the main edition surfaced ("cela, c'est assez !"), so both
editions agree at the verse level — the edition delta is immaterial.

**Main edition, the single candidate** (from reissue census):

> `cela,  c'est  assez I^ \nEn  maudissant  tout  bas  le  mendiant  avide \nAuquel  il  faut  jeter  le  fond  du  verre  vide!`

Classification (reissue report): excluded with cause — demonstrative is the
subject of a finite clause; "jeter" is governed by "il faut", "verre" is a
noun; no bare exclamatory infinitive under a fronted demonstrative topic.

Both editions yield zero genuine attestations of the fenced shape.

## Per-clause pass/fail

1. **Excluded-edition census matches the main edition's zero genuine count** —
   PASS. Identical counts (1 dem-comma / 1 excl candidate / 0 genuine), and the
   single candidate in each edition is the same verse excluded with the same
   cause.
2. **Conditional: any genuine attestation in the excluded edition re-opens the
   register question** — PASS (condition not triggered; no genuine attestation).

## Verdict: PROMOTE

The exclusion of `hugo-hernani.txt` under the one-edition-per-play rule is not
load-bearing: the excluded edition contains zero genuine attestations of the
fenced demonstrative-topic + bare-infinitive shape, matching the main edition
exactly. The drama-register fence from `disloc-demonstrative-drama-reissue`
stands at 2,969,582 + 173,559 chars with no edition-dependent gap.

No follow-ups required (promote verdict). Standing recommendation for the
supervisor: the edition-delta check is now a validated pattern for any corpus
file duplicated across editions.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/disloc-demonstrative-drama-edition-delta.lock`
  created on start, no stale lock existed; deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched. No standing
  verdicts contradicted. No numbers invented — all counts trace to the census.
