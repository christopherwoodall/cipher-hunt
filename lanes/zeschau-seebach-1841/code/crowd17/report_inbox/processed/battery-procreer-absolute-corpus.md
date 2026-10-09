# Battery report: procreer-absolute-corpus — verdict: NULL (fence executed)

## Bar (verbatim, pre-registered)
"resolve iff procreer's absolute use is attested in period diplomatic French (corpus hit with stated source) or fenced with a stated literature search; new work beyond the parent's form census"

Numbered clauses:
- C1 — corpus attestation arm: ≥1 absolute (objectless) use of procréer in the period corpus, with stated source. PASS iff found; FAIL iff the exhaustive census finds zero.
- C2 — fence arm: if C1 fails, fence with a stated literature search (what was searched, what it returned).

## Method
Exhaustive stem census over `code/side-period/corpus` (77 files, ~34.5M chars): case-insensitive regex `[Pp]rocr[ée][a-zéèêëàâîïôöùûç]*` across every .txt file, then hand-classified the transitivity of every verb-form hit. This is new work beyond the parent's (`procreer-56-semantic`) form census: the parent counted forms; this battery classified object government. Stream untouched (corpus-only battery); `canonical.py` never used.

## Findings
Total stem hits in the entire corpus: **5 tokens in 4 files**.
- `levant-correspondence-1841-p3.txt`: "procreation", "procréation" — nouns, irrelevant to the verb.
- `revue-deux-mondes-1841-q3.txt`: "les avait **procréés** en révolte contre Dieu" — transitive, direct object "les".
- `metternich-papiere-v6.txt` (Aus Metternich's nachgelassenen Papieren, vol. 6; coverage 1835–43, French despatch text; archive.org `ausmetternichsna06mettuoft`): "…de ce que le temps seul sait **procreer** et completer." Hand-parse: "ce" (the relative-pronoun antecedent of "ce que") is the direct object of both infinitives — transitive, NOT absolute. The apparent absolute reading dies on the object gap.
- `nesselrode-v10.txt`: "qui n'en **procréait** pas d'autres dans son haras" — transitive, objects "en"/"d'autres".

**Relevant verb tokens: 3/3 transitive. Absolute (objectless) uses: 0.**

Stated literature search (fence arm):
- Period corpus (34.5M chars, 77 files, provenance in `code/side-period/corpus/PROVENANCE.md`): 0 absolute uses, exhaustive.
- Littré: the parent's evidence notes Littré records an absolute use of procréer — a dictionary record, not a period diplomatic attestation; its citations are undated by the parent. No period diplomatic source found.

C1: FAIL (0/3). C2: FIRES — fenced with the stated search above.

## Verdict
**NULL** — fence executed per lane convention for "attest X or fence" bars. The absolute-use question is closed at the period-corpus level: procréer's absolute use is unattested in 34.5M chars of period French including diplomatic correspondence. This removes the Littré-absolute gradient-fit advantage cited in the parent's `procreer-56-semantic` NULL — the 8-way Xéent tie at @1745 should be re-scored without it.

## Scope
Corpus-only; no stream claims. No standing or red-team verdict contradicted; §7 intact. The fence covers the period corpus as constituted; it does not rule on the drama register or on Littré's citation dates (see follow-ups).

## Follow-ups (all verified ABSENT from battery-queue.json)
1. `procreer-littre-absolute-date` (P4) — date Littré's absolute-use citations for procréer; a pre-1841 diplomatic citation re-opens, otherwise the register question closes.
2. `procreer-absolute-drama-corpus` (P4) — same transitivity census on the 14-play drama corpus; a different register may hold the absolute use.
3. `procreer-56-semantic-reweight` (P3) — re-score the 8-way Xéent tie at @1745 with the Littré-absolute advantage removed per this fence.

## Bookkeeping
- Lock `code/crowd17/next-token/locks/procreer-absolute-corpus.lock` created 2026-10-09T15:24:30Z, deleted on completion.
- Queue: `procreer-absolute-corpus` → status verdict, result null, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
