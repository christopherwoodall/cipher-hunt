# Battery report: gov-excl-inf-modern

- Target id: `gov-excl-inf-modern`
- Claim: "governed exclamatory-infinitive census in a modern French corpus"
- Date: 2026-10-09
- Stream: not applicable — corpus census against modern French, per target charter.
  The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and
  the red-team adjudication queue were not touched.

Terms: "governed exclamatory infinitive" = a preposition-governed infinitive
phrase (pour / à / de + infinitive) that IS itself the exclaimed element
("pour rire !"). "Genuine attestation" = the "!" terminates the governed
infinitive phrase itself; the infinitive is not embedded in a finite matrix
clause whose "!" belongs to the matrix, and not embedded in an exclaimed
noun phrase. "Modern French" = early-20th-century French fiction, 1902–1913
(the diachronic control; limitations in §Limitations).

## Parentage

The register battery (`gov-excl-inf-register`, 2026-10-09) found 0 genuine
governed exclamatory infinitives in 27.66M chars of 1841 French print, and the
recall battery (`gov-excl-inf-recall`) closed its three search gaps at the same
zero. The standing fence is that the construction is register-absent from 1841
French print. This battery tests whether that zero is period-bound: does the
construction attest in later French?

## Bar (verbatim, pre-registered before testing)

">=1 genuine in modern French re-opens the diachronic question; confirmed
zero suggests the fence is not period-bound."

Numbered pass/fail clauses (restated before testing, not modified after):

1. If >=1 genuine attestation of the governed exclamatory infinitive is found
   in the modern French corpus, the diachronic question is re-opened (the
   zero is period-bound, an 1841-register gap).
2. If the census confirms zero genuine attestations in modern French, the
   fence is not period-bound (the construction is absent from modern French
   print too, at this register).

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/gov-excl-inf-modern.lock` on start
   (worker id + UTC timestamp 2026-10-09T11:21:26Z; no stale lock for this id
   existed); deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/gov_excl_inf_modern_census.py` — the register
   battery's P1 candidate design verbatim: for every "!" in the corpus, take
   the 120 chars before it; run GOV_INF =
   `\b(pour|à|a|de|d['’])\s+(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`
   (case-insensitive) on that segment; keep the closest match whose tail to
   the "!" contains no [.;]. Raw results in
   `code/crowd17/next-token/gov-excl-inf-modern_census.json` (per-file sizes,
   "!" counts, all 259 candidate windows with prep/infinitive/dist fields).
3. Corpus (byte counts recomputed in-session; provenance in
   `code/crowd17/next-token/corpus-modern/PROVENANCE.md`):
   - PG 13765: Gaston Leroux, "Le mystère de la chambre jaune" (1907),
     520,058 chars, 1,111 "!".
   - PG 62100: Marcel Proust, "Un amour de Swann" (1913), 473,135 chars,
     326 "!".
   - PG 13525: Louis Hémon, "Maria Chapdelaine" (1913), 292,052 chars,
     156 "!".
   - PG 73058: André Gide, "L'immoraliste" (1902), 246,774 chars, 199 "!".
   - Total: 4 files, 1,532,019 characters, 1,792 "!". All four verified
     French (gutenberg.org ebook-page inLanguage=fr) before download.
   - First-attempted source (fr-Wikipedia 20220301 parquet shards) was
     abandoned: shard downloads timed out through the egress proxy and the
     background fetch hit a runtime confirmation gate.
4. Classification. Tight band (dist<=40, 171 candidates) fully hand-classified
   in one pass, using the register battery's cause legend:
   A (never-infinitive word), B (finite-matrix embedding), C (exclaimed-NP
   embedding), D (terminator belongs to following quotation/interjection),
   E (interrogative matrix), F (pattern false friend). Classification record
   in `code/crowd17/next-token/gov-excl-inf-modern_classification.json`.
   Wide band (dist>40, 88 candidates) scanned in full, the parent battery's
   "scanned" treatment.
5. Recall-gap due diligence (the recall battery's G1 gap): ran the same P1
   pattern against "?" terminators on the modern corpus — 107 tight
   candidates, scanned.

## Findings

C1 FIRES. C2 does not fire.

### The genuine attestation (1)

- **Tight candidate #89**, pg13765.txt (Leroux, 1907), dist=16:
  "...elle prie le père Jacques de ne pas se déranger! **De ne pas pénétrer
  dans la chambre!**"
  The second sentence is an independent sentence whose only content is the
  "de"-governed infinitive phrase; the "!" terminates that phrase itself.
  There is no finite matrix in the sentence. The exclaimed element IS the
  governed infinitive phrase ("de ne pas pénétrer dans la chambre"). This
  meets the genuine-attestation definition verbatim. It is an elliptical
  restatement of the preceding sentence's request ("elle prie ... de ne pas
  se déranger"), which is exactly how a governed infinitive comes to stand
  alone as an exclamation.

### Fenced near-miss (1)

- **Tight candidate #55**, pg13765.txt: «Eh! s'écria M. de Marquet, encore
  une fois, assez de piailler comme ça!» — the exclaimed head is the degree
  adverb "assez"; the "de"-infinitive is its complement. Per the bar's
  definition the infinitive phrase is not itself the exclaimed element
  (cause-C-adjacent embedding); fenced, not counted.

### Tight-band tally (171, hand-classified)

- B (finite-matrix embedding): 114
- D (terminator belongs to following quotation/interjection): 30
- C (exclaimed-NP embedding): 11
- E (interrogative matrix): 11
- A (never-infinitive word, e.g. "terre", "fenêtre", "cela"): 2
- F (pattern false friend — bare infinitive "connaître le silence de cette
  chambre!", where "de" governs "silence" not the infinitive): 1
- NEARMISS (fenced, see above): 1
- GENUINE: 1 (candidate #89)

### Wide band (88 candidates, scanned)

- 0 genuine. All scan as B/C/D/E. Nothing in the wide band undercuts the
  tight-band result.

### "?"-terminated gap (107 candidates, scanned)

- 0 genuine. All 107 are interrogative matrices (cause E): the "?" marks a
  genuine question ("Ai-je le droit de tuer l'assassin de Mlle Stangerson?"),
  never exclamatory incredulity at an infinitive phrase.

## Verdict rationale

C1 fired: one genuine governed exclamatory infinitive attests in the modern
French corpus (Leroux, 1907, "De ne pas pénétrer dans la chambre!"). The
diachronic question is therefore re-opened: the 1841-register zero (0 genuine
in 27.66M chars) is **period-bound** — the construction is absent from the
1841 print register but alive in early-20th-century French fiction. This does
not contradict the register battery's zero (different register, different
century); it brackets it. No standing/red-team verdict contradicted or
downgraded; §7 intact. Adverses: none listed.

Promote is census-grade only: it attests the construction's existence in
1902–1913 French fiction, and says nothing about 1841 French or about any
cipher value.

## Limitations (stated, not hidden)

- The control corpus is early-20th-century literary fiction (dialogue-rich),
  not present-day French and not 1841 diplomatic print. It tests
  period-boundedness, not modernity in the strict sense.
- The corpus is 1.53M chars / 1,792 "!" — smaller than the register battery's
  27.66M / 5,896, but the "!" density is comparable and the single genuine
  hit is a positive attestation, not an absence claim.
- The genuine hit is one window (n=1); the construction is rare even in this
  register. The 1841 zero remains the standing register fact.

## Optional regenerations (promote, not null — these are notes, not mandated
follow-ups)

1. `gov-excl-inf-diachronic-bracket` (P3) — census a late-19th-century French
   fiction corpus (e.g. Zola, Maupassant) to bracket the construction's
   emergence: absent 1841, present 1907 — when does it appear?
2. `gov-excl-inf-ellipsis-frame` (P4) — study the genuine hit's frame: is the
   stand-alone governed infinitive in 1907 French licensed only as an
   elliptical restatement of a request ("prie ... de"), or does it occur
   ungoverned-by-context too?

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-gov-excl-inf-modern.md` (this file)
- Queue: `gov-excl-inf-modern` → `verdict`/`promote`, 2026-10-09 (pre-write
  assert passed — was queued/verdictless; temp-file + rename; JSON
  re-validated; own entry only; no downgrade)
- Census JSON: `code/crowd17/next-token/gov-excl-inf-modern_census.json`
- Classification JSON:
  `code/crowd17/next-token/gov-excl-inf-modern_classification.json`
- Census script: `code/crowd17/next-token/gov_excl_inf_modern_census.py`
- Corpus: `code/crowd17/next-token/corpus-modern/` (texts + PROVENANCE.md)
- Lock created on start, deleted on completion. R5005, sealed gates,
  red-team adjudication queue untouched.
