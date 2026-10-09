# Battery verdict: et-regne-wider-register

**Verdict: PROMOTE** — the head-frame contest is re-opened. Six genuine
19th-century prose attestations of "et le règne" found (lane corpus +
Wikisource + web). **No word value is promoted by this verdict**; the
standing battery-grade `w508-noun-ne` "trône" promote is untouched
(§5 honored — never downgraded, never re-litigated). This re-opens the
head slot for the red team, which now has règne-side prose evidence to
weigh against the trône 3×.

**Target:** `et-regne-wider-register` (P3)
**Claim:** Wider 19th-century French search (beyond the lane corpus) for "et le regne".
**Date:** 2026-10-09
**Worker:** 6be36034-ec84-414a-b616-193771139e9b
**Parent:** battery-62-regne-trone-final (NULL, 2026-10-09) — "et le trone" ×3 vs "et le regne" ×0 on the lane corpus alone.
**Stream:** repaired 1,847-pair / 96-type parse untouched this battery (corpus battery, not stream battery). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"re-open the head-frame contest iff >=1 genuine attestation; confirmed zero across a larger base hardens trone's head-slot advantage"

Numbered clauses (restated before testing; not modified after):

- **C1**: ≥1 genuine attestation of "et le règne" in 19th-century French prose → the head-frame contest re-opens.
- **C2**: confirmed zero across a larger base → trône's head-slot advantage hardens.

(Disjunctive bar: C1 and C2 are alternative outcomes. "Genuine" = hand-checked 19th-century prose token of the "et le [W]" head frame; regex counts, title/index metadata, and "et il"-type misparses do not count.)

## Method

1. Lock `locks/et-regne-wider-register.lock` created on start (agent id + 2026-10-09T19:47:43Z); no stale lock present.
2. Lane corpus (`code/side-period/corpus/`, **98 files, 59,197,732 chars**, 1841-register French): accent-insensitive (NFD strip) regex `et\s+le\s+regne\b` with flexible whitespace (double-space OCR artifacts caught). Every raw hit hand-checked in context.
3. French Wikisource full-text via `insource:"et le règne"` and `insource:"et le regne"` (MediaWiki API): 12 raw hits, every one hand-checked in snippet context.
4. Four targeted exact-phrase web queries (accented, unaccented, year-scoped, "et le règne de").
5. Lexicographic check: Littré "règne" entry citation base for an "et le règne" collocation.
6. Exact-frame spot checks in the lane corpus: "et le règne qui", "le règne qui vient", "le règne qui".
7. Untapped and fenced (not claimed): Gallica full-text (SRU endpoint Cloudflare-blocked for curl, HTTP 403) and Open Library inside-search (endpoint returned non-JSON). → follow-ups below.

## Evidence

### Lane corpus: 8 raw hits → 6 genuine prose attestations

Exhaustive scan, 59.2M chars, all hand-checked:

**Genuine (6):**

1. `metternich-papiere-v6.txt` — "Une minorité et le règne d'un jeune Prince qui la suit, sont des régimes difficiles à supporter pour un État solidement établi" (Metternich papers/correspondence, 19th c.).
2. `pozzo-di-borgo-correspondance-v1.txt` — "et ces horreurs ont nécessité et rendu puissant le despotisme militaire et le règne de Bonaparte" (Pozzo di Borgo correspondence, 19th c.).
3. `revue-deux-mondes-1840-q3.txt` — "d'indiquer en traits rapides le caractère politique et le règne de Frédéric-Guillaume" (Revue des Deux Mondes, 1840).
4. `revue-deux-mondes-1841-q1.txt` — "la déposition de Marie, la chute définitive du catholicisme, et le règne de Murray, protestant, sous le nom de l'impuissant Darnley" (RDDM, 1841).
5. `revue-deux-mondes-1841-q2.txt` — "il opéra la transition entre l'époque des controverses théologiques et le règne de la philosophie" (RDDM, 1841).
6. `revue-deux-mondes-1841-q4.txt` — "le triomphe de l'homœopathie et le règne de l'égalité" (RDDM, 1841).

**Excluded with cause (2):**

- `chateaubriand-outre-tombe-t4.txt` — editorial footnote quoting a book title ("…la Restauration et le règne de Louis-Philippe Ier, par la duchesse d'Abrantès, tome VII, 1838"): bibliographic title string, not a prose head-frame token.
- `revue-deux-mondes-1840-q3.txt` — "il admet le règne de l'apparence et il [fait] trôner l'illusion": the "et" joins "il", a misparse, not an "et le règne" token.

**Distributional fact (all six):** every genuine attestation takes a "de X" complement ("d'un jeune Prince", "de Bonaparte", "de Frédéric-Guillaume", "de Murray", "de la philosophie", "de l'égalité"). The parent's trône 3× are bare/PP-headed ("soutenir l'autel et le trone"; "et le trone comme la charte, la paix interieure"; "et le trone avec eux"). Exact frame "et le règne qui" / "le règne qui vient" / "le règne qui": **0/0/0** in the lane corpus — the parent's exact-frame zero holds.

### Wikisource: 12 raw hits → 0 genuine

All twelve are the title convention "…et le règne de X" in periodical tables of contents (Revue des Deux Mondes index pages: "Les États-Généraux de 1484 et le règne de Louis XI", "…et le règne de Louis XII", "Les institutions et le règne d'Akbar", "Le Journal de l'abbé de Veri et le règne de Louis XV", "La Conquête et le Règne") or a PDF filename embedded in a transclusion ("…la Restauration et le règne de Louis-Philippe Ier. Tome 1.pdf"). Headline/index metadata, not prose tokens. Unaccented variant `insource:"et le regne"`: 0 hits.

### Web search: 0 genuine

Four exact-phrase queries surfaced no 19th-century prose token — only bookstore metadata and more instances of the "…et le règne de X" title convention (e.g. Histoire des salons de Paris subtitle "…la Restauration et le règne de Louis-Philippe Ier", éd. 1837–1838). One Google Books hit (Laquièze, Les origines du régime parlementaire) matched on query-adjacent metadata only.

### Lexicographic: Littré "règne" — 0

Littré's citation base for "règne" (senses 1–3: Rotrou, Sacy/Bible, Racine, Fénelon, Montesquieu, Voltaire, Saint-Simon, Bossuet, D'Alembert) shows collocations "votre règne", "son règne", "un mauvais règne", "le règne du feu roi", "leur trop long règne" — no "et le règne" collocation.

### Adverses (coordination with `trone-vient-register`, verdicted NULL 2026-10-09)

No duplication: the sibling battery searched 'trône' as subject of lexical 'venir' (its lane-corpus exhaustive search + Littré + web: zero genuine; Littré "venir" sense 19 licenses the échoir construction type, so the zero is a usage zero, not a grammaticality zero). This battery searched only the "et le [W]" head frame. The two results compose without conflict: the selectional-asymmetry question (sibling: tie unresolved) and the head-frame question (this battery: contest re-opened) are independent evidence strands for the red team. Nothing here contradicts or downgrades the standing battery-grade `w508-noun-ne` "trône" promote.

## Per-clause verdict

- **C1** (≥1 genuine attestation): **PASS** — 6 genuine 19th-century prose attestations (listed above, hand-checked). → the head-frame contest re-opens.
- **C2** (confirmed zero): **FAIL** — zero not confirmed (moot given C1).

## Verdict: PROMOTE

The bar is met on C1: the head-frame contest re-opens. Fence, explicitly: this promotes no word value and names nothing at @508. The standing battery-grade `w508-noun-ne` "trône" promote stands untouched; what changes is the evidence balance the red team must weigh — head slot is no longer 3-vs-0. Note for the red team: règne's six attestations are uniformly "et le règne de X"; the cipher locus "et le [62]ne qui vient" has no "de X" before "qui", while the exact "et le règne qui" frame is 0/0 in the 59.2M-char base. Whether the bare head "et le règne qui" is licensed is a separate selectional question.

## Follow-ups proposed (verdict is promote, so §4's null obligation does not apply; the two below are pipeline gaps worth queuing at the supervisor's discretion — both verified ABSENT from battery-queue.json by target id)

1. `et-regne-gallica` (P4) — Gallica full-text search for "et le règne" in 1800–1900 French books; the one 19th-c book base this battery could not tap (SRU Cloudflare-blocked for curl; needs a live-browser or alternate route).
2. `et-regne-barehead` (P4) — targeted search for bare-headed "et le règne" (no "de X" complement) and the exact "et le règne qui" frame in a larger book corpus; tests whether règne's 6/6 "de X" pattern is a real distributional restriction against the cipher locus.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-et-regne-wider-register.md` (this file)
- Queue: `et-regne-wider-register` queued → `status: verdict`, `verdict: {"result": "promote", "report": "code/crowd17/report_inbox/battery-et-regne-wider-register.md", "date": "2026-10-09"}` (pre-write assert: was queued/verdictless; target-id-unique tmp `battery-queue.json.et-regne-wider-register.tmp` + rename; JSON re-validated post-write; own entry only; no standing verdict touched)
- Lock `locks/et-regne-wider-register.lock`: created on start (2026-10-09T19:47:43Z, no stale lock), deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched. No standing/red-team verdict contradicted or downgraded. §7 intact. Canonical-stream caveat stands.
