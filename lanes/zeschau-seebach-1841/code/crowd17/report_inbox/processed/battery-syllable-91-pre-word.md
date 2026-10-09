# Battery verdict: syllable-91-pre-word

- Target: `syllable-91-pre-word` (battery-queue.json, priority 3, status queued)
- Claim: "state 91's syllable/stem role in the '70 91' hapax at @520 with byte evidence, or fence the word-internal arm"
- Worker: 380a54c4-e2db-4728-8ceb-0b36707641e9, 2026-10-09

## Bar tested (verbatim, pre-registered)

"name 91's syllable/stem content iff it composes a French word with 'pre' under standing licenses; else fence"

Numbered clauses:
- C1: name 91's syllable/stem content — it composes a French word with 'pre' (70='pre', pencil GT) under standing licenses → PASS names the content
- C2 (else): fence the word-internal arm → FIRES

## Verdict: NULL (fence executed)

## Findings

Repaired 1,847-pair / 96-type stream re-derived in-session (asserts held; `canonical.py` never used).

**Locus byte-confirmed:** the '70 91' bigram is exactly 1x stream-wide at @519–520. Full window @515–524:
`87(ce) 77(le) 80(?) 09(?) 70(pre) 91(?) 77(le) 06(ent) 55(?) 81(?)`
= "ce le [80] [09] pre [91] le ent [55] [81]".

**Word-internal hypothesis test:** for C1, a candidate 91 content must (a) form a real French word with 'pre', and (b) parse in the frame "[pre-91-word] le(77) ent(06)" — i.e. "[word] le [verb-3pl]" (06='ent' promoted, 77='le' provisional). Exhaustion over "pre-" words:

| 91 content | word | frame parse | result |
|---|---|---|---|
| 'mier' | premier | "premier le [V]ent" — adjective/noun + "le" + 3pl verb | dead |
| 'ndre' | prendre | "prendre le [V]ent" — two finite/inf verbs in sequence | dead |
| 'sent' | présent | "présent le [V]ent" | dead |
| 'parer' | préparer | "préparer le [V]ent" | dead |
| 's' | près | "près" requires "de", not "le" | dead |
| 'sse' | presse | "presse le [V]ent" — person/sequence | dead |
| 'uve' | preuve | "preuve le [V]ent" | dead |
| 'sque' | presque | "presque le [V]ent" — adverb cannot sit between subject and object pronoun | dead |
| 'nnent' | prennent | not a licensable syllable | dead on form |
| 'nne' | prenne | "prenne le [V]ent" | dead |

**Corpus check:** 0 hits for "presque le [verb]ent" / "premier le [verb]ent" in the 98-file 1841 corpus — the grammatical argument is usage-confirmed.

**Adverse answered:** the left context "87 77" ("ce le") is itself a standing residual (ce-le-verb-frame NULL); no rescue for the word-internal arm comes from the left. 77='le' is provisional, but no alternative 77 value composes a "pre[91][77]" word either ("prendre" via 91='nd'/77='re' still strands "prendre [V]ent").

**Fence (stated cause):** no "pre"+X composition yields a grammatical window parse under standing licenses. The word-internal arm for the '70 91' hapax is fenced at battery grade. 91's syllable/stem role at @520 is unnameable — the window is a segmentation residual (consistent with the "ce le" residual immediately left).

## Scope

Fences only the word-internal "pre[91]" arm at @519–520. Untouched: 91's locus-level promotes (val-91-pp-adj past-participle @537/@1370; adj-91-723-03-gate adjective @723), 70='pre' pencil GT, 06='ent' promote, 77='le' provisional, §7. No standing/red-team verdict contradicted or downgraded; no §7 split declared. Canonical-stream caveat stands.

## Follow-ups proposed (§4, all verified ABSENT from battery-queue.json)

1. `seg-520-residual` (P4) — package the @519–524 window (this fence + ce-le-verb-frame NULL) as a segmentation residual; test whether any multi-cell resegmentation licenses the "ce le [80] [09] pre [91]" stretch.
2. `val-09-519-subj` (P4) — name 09's class at @518; a nominal 09 supplies the missing subject for "le [V]ent" and re-opens the window right of the fenced arm.
3. `word-70-standalone` (P4) — test 70='pré' (meadow) as a standalone word at @519; the pencil gloss is "pre" but a "pré [91]" two-word parse was never tested.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-syllable-91-pre-word.md`
- Queue: `syllable-91-pre-word` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.syllable-91-pre-word.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/syllable-91-pre-word.lock`: created on start (2026-10-09T19:50:00Z approx, no stale lock), deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched
