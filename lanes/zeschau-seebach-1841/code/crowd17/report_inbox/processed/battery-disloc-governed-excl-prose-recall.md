# Battery report: disloc-governed-excl-prose-recall

- Target id: `disloc-governed-excl-prose-recall`
- Claim: "run the governed-exclamatory P3 search against the prose battery's 231 reinforced-head-comma hits"
- Date: 2026-10-09
- Worker: battery worker (subagent 4a677e3c-51ea-402a-a436-5a11e557d3ec)
- Stream: not applicable — corpus census against period French prose, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, and resumed by a pronoun. "Reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, celle-ci). "Governed exclamatory infinitive" = an infinitive led by a preposition (pour, de, à) that carries exclamatory force on its own ("celui-là, pour rire !" = "that one — what a laugh!") — not a plain governed infinitive inside a finite clause.

## Parentage

Follow-up of the NULL `disloc-reinforced-prep-inf-drama` (2026-10-09): its drama zero is confirmed (2,969,582 chars, 193 "pour/de [inf] !" positive controls, 0 under reinforced heads; clitic-tolerant re-run caught exactly 1 escapee, excluded with cause). The prose battery `disloc-demonstrative-reinforced` (231 reinforced-head-comma hits → 7 exclamatory candidates → 0 genuine) never ran the narrowed governed-exclamatory P3. This battery runs it. Does not duplicate `gov-excl-inf-recall` (different inventory: that battery searched ANY topic, this one reinforced heads).

## Gate

Corpus pinned by name to the parent battery's exact file set (byte-identity asserted at runtime, not by filename alone):

- 1841-register prose: 18 files, 25,670,258 characters — identical to the parent battery (guizot-memoires t1/t2/t3/t5-t6, nesselrode v7/v8/v9/v10, revue-deux-mondes-1841 q1/q2/q3/q4, metternich-papiere v4/v6, talleyrand-memoires-v1, pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3, plus harvest-log.txt at 1,755 chars — a non-literary file present in the parent's pinned set, carried for byte-identity; 0 hits).
- Wider 19th-century register: 3 files, 1,987,682 characters — data/gutenberg-17489-miserables1.txt (1862), data/gutenberg-30513-tocqueville-t1.txt (1835), data/gutenberg-30514-tocqueville-t2.txt (1840).
- Total: 21 files, 27,657,940 characters. Drama files in the same directory were EXCLUDED (only the parent's pinned names were read).

**Corpus-note (not hidden):** the dispatch charter describes the corpus as "the byte-identical 18-file set used by battery-disloc-demonstrative-reinforced", but the claim's 231 reinforced-head-comma hits span the parent battery's full 21-file corpus (206 in the 18-file 1841 set + 25 in the wider set). The 18-file byte-identity was still asserted separately (25,670,258 chars == parent), and the census ran against the full 21-file battery corpus so that the 231 hits reproduce exactly. The bar is not rewritten — the corpus gate is satisfied at the claim's full scope.

## Bar (verbatim, pre-registered before testing)

">=1 genuine governed exclamatory infinitive under a reinforced head in prose re-opens the shape arm; confirmed zero hardens the prose fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE governed exclamatory infinitive ("pour/de/à + infinitive" with exclamatory illocutionary force on its own, not a plain governed infinitive inside a finite or conditional clause) under a dislocated reinforced demonstrative head exists in the prose corpus. If yes: the shape arm re-opens (promote).
2. If clause 1's census is a confirmed zero — every candidate window classified, false friends excluded with cause — the prose fence hardens (null per §4: zero is an absence, not a refutation).

## Method

1. Read BATTERY-PROTOCOL.md first. A supervisor dispatch lock already existed at `code/crowd17/next-token/locks/disloc-governed-excl-prose-recall.lock`; per the dispatch brief it was OVERWRITTEN on start with this worker's agent id + UTC timestamp (not treated as stale), and deleted on completion.
2. Ran a reproducible census script: `code/crowd17/next-token/disloc_governed_excl_prose_recall_census.py` (same P1/P2 taxonomy as the prose parent census; P3 = the narrowed governed-exclamatory search adapted from `disloc_reinforced_prep_inf_drama_census.py`). Raw results in `code/crowd17/next-token/disloc-governed-excl-prose-recall_census.json`.
3. Search patterns (verbatim, from the script):
   - P1 (dislocation): `DEM_REINF\s*[,;:]` where DEM_REINF = `((?:celui|ceux|celle|celles)[-–— ]?(?:l[àa]|ci)|ça[-–— ]?(?:l[àa]|ci))`, case-insensitive. Window = demonstrative through the next `[!?.]` (inclusive), capped at 180 chars.
   - P2 (exclamatory filter): the window must contain "!" before its end.
   - P3 (governed-infinitive, strict): `\b(?:pour|de|d'|d’|à)\s+[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`, case-insensitive.
   - P3b (clitic-tolerant re-run): `(?:pour|de|d'|d’|à)\s+(?:short word\s+){0,2}[infinitive-shaped]`, catching shapes like "à en donner", "de faire penser".
   - All 4 candidates classified by hand with ±300-char context (regex cannot judge exclamatory illocutionary force).
   - Register positive control: counted bare "pour/de [inf] !" (up to 60 chars before "!") occurrences across the corpus.

## Window-level evidence

### Census yields

- 231 reinforced-head-comma hits across the 21 files (206 + 25 — identical to the parent battery, taxonomy consistent) → strict + clitic-tolerant P3 candidates: **4**.
- **0 genuine.** All four classified with cause:

**Candidate 1 — nesselrode-v10.txt @494889 ("celle-ci"):** "celle-ci, je me suis convaincu qu'il n'y a aucun inconvénient à en donner lecture in extenso ; qu'il y a même nécessité à le faire, puisqu'il en es! fait mention…" — the demonstrative is anaphoric to the dispatch ("en relisant celle-ci") inside a finite declarative matrix ("je me suis convaincu que…"). The infinitives "donner lecture"/"faire" are plain governed by "inconvénient à"/"nécessité à". The window's "!" is OCR noise ("en es! fait mention" — "est" misread). **Excluded with cause: finite declarative matrix; no exclamatory infinitive; "!" is an OCR artifact.**

**Candidates 2+3 — nesselrode-v8.txt @165979 ("celle-ci") and @165994 ("celle-là"), same window:** "…comme on critique l'intimité de celle-ci, de celle-là, et comme on a vite fait de faire penser hommes et femmes sur toute chose!" — the two demonstrative heads sit inside a finite exclamatory "comme…" matrix; "de faire penser" is governed by the idiom "vite fait de". **Excluded with cause: finite "comme"-matrix exclamation; infinitive plain-governed by "vite fait de", not itself exclamatory.**

**Candidate 4 — revue-deux-mondes-1841-q1.txt @2467062 ("celle-ci"):** "…je n'ai jamais mieux senti le néant des mots… que dans ces heures de contemplation… ; mais il ne m'arrivait pas d'autre formule d'enthousiasme que celle-ci : Bon Dieu, béni sois-tu pour m'avoir donné de bons yeux!" — "celle-ci" is cataphoric to the quoted optative outburst; "pour m'avoir donné de bons yeux" is a causal adjunct to the finite optative clause "béni sois-tu", and the "!" terminates that finite clause. **Excluded with cause: finite optative matrix; infinitive governed by purpose "pour", not an exclamatory infinitive.**

- Register positive control: 236 "pour/de [inf] !" hits in the register (RDM 1841 q1/q4 40+40, q2 27, q3 25, Metternich v6 20, v4 13, Guizot t5-t6 10, Misérables 26, etc.) — prose HAS governed-exclamatory infinitives; none sits under a reinforced head.

### Per-clause pass/fail

1. ≥1 genuine governed exclamatory infinitive under a reinforced head in prose: **FAIL** — confirmed zero. All 4 candidates excluded with cause (2 finite-matrix embeddings, 1 anaphoric-inside-declarative + OCR-noise "!", 1 finite-optative with purpose adjunct).
2. Confirmed zero hardens the prose fence: **PASS (executed)**.

## Verdict: NULL

The prose fence hardens: "celui-là, pour rire !" is unattested in 27.66M chars of 19th-century prose on top of the drama null (2.97M chars). Combined with the parent battery: zero genuine in 30.6M chars. Null per §4 — zero is an absence, not a refutation. No standing verdict contradicted; no red-team verdict touched.

Notable pattern: the two near-misses are both Nesselrode private correspondence. The epistolary register is where the exclamatory texture runs richest in this corpus — a targeted follow-up on correspondence may be the last live hunting ground for this shape in prose.

## Follow-ups proposed (nulls regenerate work)

1. `disloc-reinforced-pausemark-prose-recall` (P3) — run the dash/parenthesis pause-mark variant of the governed search on the same 21-file prose corpus. The drama-side pause-mark search found zero new hits; the prose side never ran it. Bar: ≥1 genuine re-opens; confirmed zero confirms the zero is not a separator artifact.
2. `disloc-governed-excl-epistolary` (P2) — targeted census of the correspondence sub-corpus (Nesselrode, Pozzo, Talleyrand, Guizot, Metternich) with the clitic-tolerant pattern. Bar: ≥1 genuine re-opens the shape in prose; confirmed zero closes the epistolary hunting ground.
3. `governed-excl-inf-topic-audit` (P3) — classify the 236 register-control "pour/de [inf] !" hits by topic shape (any topic class) to see whether any dislocated topic licenses governed exclamatory infinitives in prose, sharpening the fence beyond reinforced heads. Bar: any genuine with a dislocated topic of any class re-opens the licensor question; confirmed zero generalizes the fence.
