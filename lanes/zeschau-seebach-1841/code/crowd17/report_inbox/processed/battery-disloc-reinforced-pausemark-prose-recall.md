# Battery report: disloc-reinforced-pausemark-prose-recall

- Target id: `disloc-reinforced-pausemark-prose-recall`
- Claim: "dash/parenthesis pause-mark variant of the governed-exclamatory search on the prose corpus"
- Date: 2026-10-09
- Worker: battery worker (subagent a436b1ba-0254-4faf-9275-b8cedd4f64b1)
- Stream: not applicable — corpus census against period French prose, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, and resumed by a pronoun. "Reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, celle-ci). "Governed exclamatory infinitive" = an infinitive led by a preposition (pour, de, à) that carries exclamatory force on its own ("celui-là, pour rire !" = "that one — what a laugh!") — not a plain governed infinitive inside a finite clause.

## Parentage

Follow-up of the NULL `disloc-governed-excl-prose-recall` (2026-10-09): 231 reinforced-head-comma hits → 4 candidates → 0 genuine in 27,657,940 chars of 19th-century prose. Its P1 covered only comma/semicolon/colon separators. The French "—" (tiret cadratin) is the classic 19th-century prose dislocation mark ("Celui-là — pour rire !"), so this battery asks whether the parent's zero is a separator artifact.

## Bar (verbatim, pre-registered before testing)

"0 genuine confirms the prose zero is not a separator artifact; any genuine re-opens the shape arm"

Numbered pass/fail clauses (restated before testing, not modified after):

1. If ≥1 GENUINE governed exclamatory infinitive ("pour/de/à + infinitive" with exclamatory illocutionary force on its own, not a plain governed infinitive inside a finite or conditional clause) under a dislocated reinforced demonstrative head set off by a dash-family mark, ellipsis, or open parenthesis exists in the prose corpus, the shape arm re-opens.
2. If the census is a confirmed zero — every pause-mark hit accounted for, every candidate classified — the prose zero is not a separator artifact (null per §4: zero is an absence, not a refutation).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/disloc-reinforced-pausemark-prose-recall.lock` on start with this worker's agent id + UTC timestamp; deleted on completion.
2. Ran a reproducible census script: `code/crowd17/next-token/disloc_reinforced_pausemark_prose_recall_census.py`. Raw results in `code/crowd17/next-token/disloc-reinforced-pausemark-prose-recall_census.json`.
3. Corpus gate: name-pinned to the parent battery's exact 21-file set — 18 files from `code/side-period/corpus/` (byte-identity asserted at runtime: 25,670,258 chars == parent) + 3 wider files from `data/` (gutenberg-17489-miserables1.txt, gutenberg-30513-tocqueville-t1.txt, gutenberg-30514-tocqueville-t2.txt; 1,987,682 chars == parent). Total 27,657,940 chars.
4. Search patterns:
   - P1 (dislocation, variant): `DEM_REINF\s*(?:—|–|-|\.\.\.|…|\()\s*` where DEM_REINF = `\b((?:celui|ceux|celle|celles)[-–— ]?(?:l[àa]|ci)|ça[-–— ]?(?:l[àa]|ci))`, case-insensitive. Comma/semicolon/colon deliberately EXCLUDED — the parent battery covers them; this battery is the separator-artifact test.
   - P2 (exclamatory filter): window must contain "!" before its end. Window = demonstrative through the next `[!?.]` (inclusive), capped at 180 chars — same as parent.
   - P3 (governed-infinitive, strict): `\b(?:pour|de|d'|d’|à)\s+[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`, case-insensitive — verbatim from the parent.
   - P3b (clitic-tolerant re-run): up to 2 intervening short words between the preposition and the infinitive-shaped word — verbatim from the parent.

## Window-level evidence

### Census yields

- **1 dem-pausemark hit in 27,657,940 chars** (revue-deux-mondes-1841-q3.txt; 0 in all other 20 files).
- The single hit: `…ceux-ci \n\n\n(1)  De l'État des ouvriers et de son amélioration par V organisation du travail, par Adolphe Boyer, compositeur typographe.` — the open parenthesis is a **footnote marker** "(1)" followed by a bibliographic title, not a dislocation pause mark. No "!" and no infinitive in its window → fails P2/P3 → not a candidate.
- Sanity check on the regex (revue-deux-mondes-1841-q3.txt, n=145 reinforced heads): top followers are continuations (" n'", " se", " ne", ",  ", " : ") — 19th-century prose simply does not set off reinforced demonstrative heads with dashes/ellipses/parentheses in this register. The sparsity is real, not a pattern bug.
- Governed-excl candidates through P2+P3/P3b: **0**. 0 genuine.
- Register comparison (parent batteries): the "—" mark IS the productive dislocator for bare demonstratives in prose ("Moi, voler !" analogues aside, the disloc-drama program found the inverted forms). But under *reinforced* heads in prose, dash-mark dislocation is unattested.

### Per-clause pass/fail

1. ≥1 genuine re-opens the shape arm: **FAIL** — confirmed zero. No genuine, no candidates.
2. Confirmed zero → not a separator artifact: **PASS (executed)**. Dash/ellipsis/parenthesis marks produce essentially no reinforced-head dislocations at all in the prose corpus (1 footnote artifact in 27.7M chars), so the parent battery's comma-colon zero cannot be hiding behind a different separator.

## Verdict: NULL

Per §4 (zero is an absence, not a refutation), consistent with the sibling recall battery `disloc-comedy-bare-heads-recall` (NULL). The prose fence hardens one more way: the reinforced-head + governed exclamatory infinitive pairing is unattested under every pause-mark class the corpus contains — comma, semicolon, colon, em/en dash, hyphen, ellipsis, open parenthesis — across 27,657,940 chars. No standing verdict contradicted; §7 intact; no red-team verdict touched.

## Follow-ups proposed (nulls regenerate work)

1. `disloc-reinforced-pausemark-epistolary` (P3) — the two near-misses of the parent prose battery were both Nesselrode private correspondence; run the dash/parenthesis variant on the epistolary sub-corpus. Bar: ≥1 genuine re-opens; confirmed zero closes the register's separators.
2. `disloc-reinforced-bare-inf-heads-prose` (P3) — the parent census's P1 was reinforced-head-only; run the dash/parenthesis separator variant with *any* demonstrative head (bare ce/ça/ceci/cela included) on the same 21-file corpus, since bare heads dislocate more freely with dashes in prose. Bar: ≥1 genuine with a dislocated topic re-opens the licensor question; confirmed zero generalizes the separator finding.
3. `disloc-reinforced-pausemark-drama` (P4) — the prose register is comma-dominant; drama dialogue is dash-dominant ("—" dialogues). Test the variant where dashes actually live. Bar: ≥1 genuine re-opens the register question; confirmed zero fences the variant in drama too.
