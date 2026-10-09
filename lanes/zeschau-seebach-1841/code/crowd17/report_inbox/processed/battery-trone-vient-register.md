# Battery verdict: trone-vient-register

- Target: `trone-vient-register` (battery-queue.json, priority 3, status queued)
- Claim: "Wider 19th-century French search (beyond the lane corpus) for 'trône' as subject of lexical 'venir' (arrive/come; exclude 'venir de' + infinitive and passive auxiliaries)."
- Date: 2026-10-09
- Worker: b416466e-195d-4da5-bed4-23b3c99c31e4

## Bar (verbatim, pre-registered)

"Battery-grade search: >=1 genuine attestation closes the selectional asymmetry (tie stands); confirmed zero leaves the tie unresolved."

Numbered clauses:
- C1: >=1 genuine attestation of 'trône' as subject of lexical 'venir' in 19th-century French → closes the selectional asymmetry (tie stands).
- C2: confirmed zero → the tie stays unresolved.

No kill clause is defined by this bar; the outcomes are attest-or-null.

## Method

1. Exhaustive regex search of the lane corpus (`code/side-period/corpus/`, 99 files, ~59M chars, 19th-century French): all `trône/trônes` occurrences co-occurring with any 'venir' form (vient/viennent/vint/vînmes/vinrent/viendra/viendrait/venu/venue/venir/venait/venions/vienne/subjunctive forms), then tightened to subject-position patterns (`le trône vient/vint/viendra`, `vient le trône`, `trône ... vint ... à/de/lui` échoir patterns). Every candidate hand-checked.
2. Lexicographic check: Littré "venir" entry (littre.org), full text searched for 'trône'.
3. Web searches (multiple targeted queries): `"le trône vint"`, `"le trône vient"`, `"trône lui vint"`, `"trône lui est venu"`, `"le trône vint à"`, author-scoped (Chateaubriand/Hugo/Balzac), Wikisource-scoped, succession-context queries.
4. Baseline check: same corpus searched for 'règne' + 'venir' to establish the rival side of the asymmetry.

Stream context (repaired 1,847-pair / 96-type parse; `canonical.py` never used): 62~98 adjacencies are 6× stream-wide (@11, @802, @945, @1136, @1324 '62 98'; @1481 '98 62'). 98='vient' is LEAD (unratified); 62 is unvalued with the 'règne' vs 'trône' tie unresolved. The question is whether 'trône' can be the subject of lexical 'venir' at these windows.

## Findings

### Lane corpus: confirmed zero (exhaustive)

217 raw `trône`+`venir` co-occurrence chunks reduced to 2 subject-adjacent candidates, both excluded with cause:

1. **pozzo-di-borgo-correspondance-v1.txt**: "au cas que le trône vienne à vaquer par la mort du roi" — 'venir à' + infinitive, the fortuit semi-auxiliary (Littré "venir" sense 39: "marque quelque chose d'inattendu, de fortuit"). Not lexical 'venir' (arrive/come). Excluded.
2. **thiers-consulat-empire-v2.txt**: "quand le trône de France venait de s'écrouler" — 'venir de' + infinitive, recent-past auxiliary. Explicitly excluded by the bar.

All other co-occurrences have a different subject for the 'venir' form (e.g. "les rois viennent baiser" — subject 'rois'; "l'Europe entière interviendrait" — hyphenated word).

### Lexicographic evidence

- Littré "venir" **sense 19**: "Venir par succession, échoir, **avec un nom de choses pour sujet**. Après la mort du père, les biens viennent aux enfants." — the construction TYPE (thing-noun subject + 'venir' in the échoir/succession sense) is grammatical French. This means the corpus zero is a usage zero, not a grammaticality zero: 'trône' is not selectionally barred from the échoir construction, it is merely unattested.
- Littré "venir" full text contains exactly one 'trône' citation: "Ce roi vint jeune au trône" — subject is 'roi', not 'trône'. No 'trône'-subject citation.

### Web search: zero genuine attestations (best-effort)

Multiple targeted queries (exact-phrase, author-scoped, Wikisource-scoped, succession-context) returned no genuine 19th-century attestation of 'trône' as subject of lexical 'venir'. Notable: the famous rival-side attestation "que ton règne vienne" (Matthew 6:10, "Adveniat regnum tuum") is liturgical/biblical French — 'règne' has a universally known 'venir'-subject attestation; 'trône' has nothing comparable in the sources searched.

### Baseline: 'règne' + 'venir' in the lane corpus

5 chunks; none is lexical 'venir' with 'règne' as subject ("Un nouveau regne vient de commencer" = 'venir de' auxiliary; others have different subjects). The asymmetry rests on the liturgical "que ton règne vienne", not on corpus evidence.

## Per-clause verdict

- C1 (≥1 genuine attestation): **FAIL** — zero genuine attestations found in the lane corpus (exhaustive), in Littré's citation base, and in best-effort wider web search.
- C2 (confirmed zero): **HOLDS at lane-corpus level** (exhaustive 59M-char search); best-effort at the wider-web level (web search is not exhaustive).

## Verdict: NULL

Per the bar's own terms, confirmed zero leaves the tie unresolved. 'Trône' is not grammatically barred from the échoir construction (Littré sense 19 licenses thing-noun subjects), but no 19th-century attestation of 'trône' as subject of lexical 'venir' was found. The 'règne' vs 'trône' tie for 62 is unmoved.

Scope: this fences only the selectional-asymmetry question. 98='vient' LEAD, 62's value, and the 'règne'/'trône' tie are all untouched. §7 intact. No standing/red-team verdict contradicted or downgraded. Canonical-stream caveat stands.

## Follow-ups proposed (§4, all verified ABSENT from battery-queue.json)

1. `trone-venir-gallica` (P4) — Gallica full-text search for "le trône vint/vienne/viendra" in 19th-century books; the one wider 19th-century source not yet tapped by this battery.
2. `regne-venir-liturgical` (P4) — document the 'règne' side of the asymmetry precisely (liturgical "que ton règne vienne" and its 19th-century currency); pins down what a 'trône' attestation would need to match.
3. `trone-echoir-corpus` (P4) — targeted search for the échoir construction "le trône vint/est venu à [personne]" (Littré sense 19) in a larger book corpus; tests the one construction where a 'trône' subject is most plausible.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-trone-vient-register.md` (this file)
- Queue: `trone-vient-register` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.trone-vient-register.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/trone-vient-register.lock`: created on start (2026-10-09T19:29:15Z, no stale lock), deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched
