# Battery `58-det-gap-corpus` — verdict: PROMOTE

**Bar (verbatim, pre-registered):** "If yes, the zero-determiner-predecessor asymmetry is expected for 58's nominal subtype; if bare gerund complements are rare, the asymmetry stands as an answered residual."

Restated as numbered clauses:
- C1: corpus census of "en [V]ant" windows run on the 1841 period corpus with stated pattern and byte-verified counts.
- C2: the following-noun slot classified (determined / free-bare / frozen-collocation / proper-noun / non-nominal), with the full auto-"bare" bucket hand-audited.
- C3: the bar's decision question answered with measured rates.

## Method

- Corpus: `code/side-period/corpus` — 63 files, 31,664,431 chars (1841 diplomatic memoirs, 1841 press, revue des deux mondes). The lane's 1841 period standard.
- Pattern: `\ben\s+\w*ant\b` (case-insensitive, curly-apostrophe normalized), then the immediately following word token. Script: `code/crowd17/next-token/58-det-gap_census.py`; output: `code/crowd17/next-token/58-det-gap_census.json`; hand audit: `code/crowd17/next-token/58-det-gap_handaudit.json`.
- Auto classification: determined (article/demonstrative/possessive/elided l' lists), free-bare, frozen-collocation, proper-noun, non-nominal (adverb, pronoun, preposition, infinitive, participle, clause, frozen). The initial 574 auto-"bare" hits were heavily contaminated (adverbs "ainsi/ici/bien", clauses "qu'il", frozen "compte/possession"); expanded exclusion lists plus curly-apostrophe elision handling reduced it to 163, which I hand-audited in full (all 131 distinct forms with context).
- Determined bucket checked: 200/2278 random sample (seed 42) — 82.5% direct determiner, rest prepositional "de"/misc. Nominal direct-complement denominator = determined-direct 1879 + frozen collocations 46 + genuine free bare 13 = 1938.

## Findings

- 5,117 "en [V]ant" windows byte-counted. Auto classes: determined 2278, bare 163, proper-noun 94, frozen 46 (after hand audit), non-nominal 1541, punctuation 1152.
- Genuine free bare nouns after gerunds: **13 of 1938 nominal direct-complement slots = 0.7%**. Determined = 1879/1938 = **97.0%**. Frozen collocations = 46/1938 = 2.4% ("prendre possession", "rendre compte", "faire allusion", "donner suite", "prendre acte", "flagrant délit", …).
- The 13 genuine cases, hand-verified: "en devenant persécuteur", "en devenant instituteur communal", "en parlant anglais", "en parlant turc à son peuple", "en accordant amnistie pleine et entière" (1841 diplomatic letters), "en manifestant accord heureusement rétabli", "en demandant grâce à son Souverain", "en devenant propriétaire", "en laissant place à la critique", "en recevant communication", "en donnant communication de cette pièce", "en faisant appel à un public", "en galant homme, en ami".
- Productive bare licenses observed: **devenir + predicative noun** (3 of the 13: persécuteur, instituteur, propriétaire — the most productive genuine channel), language names (anglais, turc), diplomatic formulas (amnistie, accord, communication, acte), "faire appel à", and the "en + noun" appositional construction ("en galant homme").

## Per-clause verdicts

- **C1 PASS** — census executed: 5,117 windows, 63 files, 31,664,431 chars, byte-verified counts.
- **C2 PASS** — slot classified with stated criteria; full 163-hit bare bucket hand-audited, OCR fragments and false friends excluded.
- **C3 PASS** — free bare-noun complements of gerunds are **rare (0.7%)** against 97.0% determined. The bar's "rare" arm fires: the zero-determiner-predecessor asymmetry for 58 is NOT position-expected; it **stands as an answered residual**.

## Verdict: PROMOTE

The corpus result is delivered (per the brief, the verdict promotes the corpus result, not a 58 class). Bare gerund complements are rare in 1841 diplomatic French; 58's asymmetry stands as an answered residual.

## Caveats / scope

- Scope is 58's gerund-complement nominal subtype (the "qu'en [85] [58]" @1695 frame and its 85-predecessor siblings). 58's other windows (predecessors 19/35/02/45) are outside this test.
- If 85 names as "devenir"-shaped, the bare-58 frame is licensed by the productive devenir-predicative channel (3/13 genuine hits) — flag for the red team and for `58-value-name`: test 85's identity, not 58's noun-hood alone.
- OCR noise in the corpus was material (many auto-"bare" hits were line-break-split fragments like "tou-/tefois", "galam-/ment"); all reported rates derive from the hand-audited set, not raw auto counts.
- No standing/red-team verdict contradicted or downgraded; §7 intact; R5005, sealed gates, and the red-team adjudication queue untouched.

## Adverses

None listed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-58-det-gap-corpus.md`
- Queue: `58-det-gap-corpus` → `status: verdict`, `result: promote`, 2026-10-09
- Lock created on start, deleted on completion. Temp-file + rename used for the queue write; JSON re-validated after write.
