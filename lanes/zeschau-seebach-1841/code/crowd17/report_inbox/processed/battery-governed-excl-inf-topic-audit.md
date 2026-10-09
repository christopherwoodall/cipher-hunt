# Battery report: governed-excl-inf-topic-audit

- Target id: `governed-excl-inf-topic-audit`
- Claim: "classify the 236 register-control 'pour/de [inf] !' hits in prose by topic shape"
- Date: 2026-10-09
- Worker: battery worker (subagent 3bb9cd61-3001-4475-83f3-15e50139f190)
- Stream: not applicable — corpus census against period French prose, per target charter. The 1,847-pair repaired parse was not used. `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "register control" = the 236 'pour/de [inf] !' strings counted by battery-disloc-governed-excl-prose-recall (2026-10-09) as proof that prose HAS governed-exclamatory infinitives (none sat under a reinforced head). "Topic shape" = what the exclamation is about: bare (no topic), dislocated NP, dislocated pronoun, vocative/addressee, finite-matrix embedding, exclaimed-NP embedding, or false-friend/artifact. "Dislocated topic" = a topic moved to the front of the clause and resumed or commented on by the infinitive phrase.

## Parentage

Follow-up of the NULL `disloc-governed-excl-prose-recall` (2026-10-09), which produced the 236-string inventory. That battery's bar only asked about reinforced heads ("celui-là, pour rire !"). This battery audits the full topic-shape map to see whether ANY dislocated topic licenses governed exclamatory infinitives in prose. Consistent with (not duplicating) `gov-excl-inf-np-boundary` PROMOTE (2026-10-09): 24 exclaimed-NP-embedded governed infinitives in prose/drama.

## Bar (verbatim, pre-registered before testing)

"a complete topic-shape map of the 236 controls sharpens the fence beyond reinforced heads"

Numbered pass/fail clauses (restated before testing, not modified after):

1. All 236 register-control 'pour/de [inf] !' hits are classified by topic shape (complete map, byte-verified source, reproducible census).
2. The map sharpens the fence beyond reinforced heads — it answers whether any dislocated topic of any class licenses governed exclamatory infinitives in prose.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/governed-excl-inf-topic-audit.lock` on start (deleted on completion).
2. Reproduced the parent battery's corpus gate byte-verbatim in `code/crowd17/next-token/gov_excl_inf_topic_audit_census.py`:
   - 18-file 1841-register prose set name-pinned from `disloc-demonstrative-reinforced_census.json` (byte-asserted 25,670,258 chars) + the 3 wider files (byte-asserted 1,987,682 chars).
   - Drift checks asserted at runtime: 27,657,940 total chars, 231 reinforced-head-comma hits (matches parent), 236 register-control distinct per-file hits (matches parent exactly).
   - CTRL pattern verbatim from the parent script: `\b(?:pour|de)\s+[a-zàâäçéèêëîïôöùûü']{2,}(?:er|ir|re|oir)\b[^!?.]{0,60}!`, case-insensitive, distinct lowercased strings per file.
3. Captured every distinct string with first byte offset + ±150-char context: 236 per-file hits = **233 distinct strings** (3 strings appear in 2 files each: "de l'angleterre!", "de l'empire ottoman!", "de l'enfer !").
4. Hand-classified all 233 strings against context into the pre-set taxonomy below. Full per-record map (match, file, offset, class, reason) saved in `code/crowd17/next-token/gov-excl-inf-topic-audit_census.json`.

Taxonomy (defined before classification):
- **F — finite-matrix embedding**: the "!" terminates a finite clause; the de/pour+infinitive is plain-governed inside it (purpose adjunct, complement, relative clause, quoted finite speech).
- **G — exclaimed-NP embedding (Cause-C family)**: an exclaimed NP (quel/que de/comme/trop/vocative NP) embedding a governed infinitive — or a plain exclaimed NP with no infinitive.
- **H — false friend / artifact**: the match is not a "de/pour + infinitive !" reading at all: noun false friends ("-re/-oir/-er" nouns like "l'affaire", "l'observatoire", "gloire"), OCR artifacts ("!i", "!21", "û!", "(agitation !"), or matches spanning punctuation where the "!" belongs to a different clause or word.

## Window-level evidence

### Summary map (233 distinct strings; 236 per-file hits)

| Class | Distinct | Share | What they are |
|---|---|---|---|
| F — finite-matrix embedding | 112 | 48.1% | "!" owns to a finite clause; infinitive plain-governed inside it |
| H — false friend / artifact | 112 | 48.1% | noun false friends, OCR, "!" belongs elsewhere |
| G — exclaimed-NP embedding | 9 | 3.9% | exclaimed NPs, 6 with governed infinitives embedded |
| Genuine governed exclamatory infinitive, any topic | **0** | 0% | none — not bare, not dislocated |

### G class in full (all 9, with file and first byte offset)

1. `de demeurer si tard en la rue à causer !` — revue-deux-mondes-1841-q2.txt @1777350 — exclamative "quelle coustume" NP embedding "de demeurer... à causer". **Genuine (infinitive embedded).**
2. `de manière!` — revue-deux-mondes-1841-q2.txt @65978 — "Quelle vulgarité de pensées et de manière!" — exclaimed NP, no infinitive.
3. `de pouvoir épargner le sang!` — nesselrode-v7.txt @350841 — "Quel bonheur de pouvoir épargner le sang!" **Genuine (infinitive embedded).**
4. `de voir des russes se complaire à dénigrer leur pays !` — nesselrode-v8.txt @333892 — "Quelle tristesse de voir des Russes..." **Genuine (infinitive embedded).**
5. `de votre jardin !` — revue-deux-mondes-1841-q4.txt @890168 — "quelle joie de me voir courir sur le sable de votre jardin !" **Genuine (infinitive embedded).**
6. `pour dire barbarie!` — revue-deux-mondes-1841-q2.txt @2479086 — "Nations! mot pompeux pour dire barbarie!" **Genuine (infinitive embedded).**
7. `pour l'angleterre devant l'europe et devant l'histoire!` — revue-deux-mondes-1841-q4.txt @2746229 — "grande responsabilité pour l'Angleterre..." exclaimed NP, no infinitive.
8. `pour aller à arras d'une traite!` — gutenberg-17489-miserables1.txt @538621 — "Un cheval pour aller à Arras d'une traite!" **Genuine (infinitive embedded).**
9. `pour cythère!` — gutenberg-17489-miserables1.txt @290999 — "Le départ pour Cythère!" exclaimed NP ("pour"+NP, no infinitive).

Every genuine case carries an **NP head**. Zero carry a bare infinitive, zero carry a dislocated topic.

### Sole fragmentary near-miss

`de signer une paix durable avec les turcs !` — nesselrode-v7.txt @237043 — an archival rubric fragment ("Souverain de signer une paix durable avec les Turcs !"), verbless and non-exclamatory in context. Topic-less either way; it does not license any topic class.

### F-family shape census (the 112 finite-matrix hits, by matrix type)

- Purpose adjuncts in finite declaratives ("pour gouverner sans en tenir compte!", "pour venir à Prague!"): the largest family.
- Infinitive complements of finite verbs ("je viens de faire!", "qu'on puisse désirer de voir!", "Dieu me garde de raviver...!").
- "que de / comme / quel danger" exclamative finite matrices owning the "!" ("Que va faire l'Angleterre pour faire sortir les Français de la Belgique!", "comme il s'arrange habilement pour mourir !").
- Quoted finite speech owning the "!" ("Tu dis que c'est pour aller chercher l'enfant de cette fille!", "pour punir leurs parents, disent souvent: je ne mangerai pas!").
- Impersonal/conditional matrices ("il vous était si aisé de faire autrement!", "Nous n'eussions pas demandé mieux que de voir un Empire grec libre et indépendant!").

### Per-file hit counts (236 total, all classified)

guizot-memoires-t1: 4 | guizot-memoires-t2: 3 | guizot-memoires-t3: 2 | guizot-memoires-t5-t6: 10 | levant-correspondence-1841-p3: 1 | metternich-papiere-v4: 13 | metternich-papiere-v6: 20 | nesselrode-v10: 2 | nesselrode-v7: 8 | nesselrode-v8: 4 | nesselrode-v9: 2 | pozzo-di-borgo: 1 | revue-deux-mondes-1841-q1: 40 | q2: 27 | q3: 25 | q4: 40 | talleyrand-memoires-v1: 8 | miserables1 (1862): 26 | tocqueville t1/t2: 0.

Notable: Nesselrode correspondence hosts 3 of the 6 genuine NP-embedded cases — consistent with the parent battery's note that the epistolary register carries the richest exclamatory texture.

## Per-clause pass/fail

1. Complete topic-shape map of the 236 controls: **PASS** — 233 distinct strings hand-classified against byte-verified context; corpus gate byte-identical to the parent (27,657,940 chars, 231 dem-comma hits, 236 control hits all reproduced); full per-record map saved in `gov-excl-inf-topic-audit_census.json`.
2. Fence sharpened beyond reinforced heads: **PASS** — zero genuine governed exclamatory infinitives with any dislocated topic (or bare) in prose. The fence generalizes from "no reinforced-head licensors" to "no dislocated-topic licensors of any class": the only genuine exclamatory uses of governed infinitives in this inventory are NP-embedded (Cause-C), and all 6 carry NP heads.

## Verdict: PROMOTE

The bar is met as written: the complete topic-shape map is delivered, and it sharpens the prose fence beyond reinforced heads. In 27.66M chars of 19th-century prose, governed exclamatory infinitives never exclaim under a dislocated topic — they exclaim only as NP complements (6 cases, all NP-headed) or sit plain-governed inside finite clauses that own the "!" (112 cases); the other 112 controls are false friends or artifacts. The licensor question the parent battery left open is answered: no dislocated topic of any class licenses this shape in prose.

No standing or red-team verdict is contradicted or downgraded; §7 intact (no polyvalence declared). Canonical-stream caveat: not applicable — corpus census, not cipher-stream work. No follow-ups proposed (promote per §4; the inventory is exhausted at the parent's scope).

## Bookkeeping

- Census script: `code/crowd17/next-token/gov_excl_inf_topic_audit_census.py`; output: `code/crowd17/next-token/gov-excl-inf-topic-audit_census.json` (per-record map with class + reason for all 233 strings).
- Report: `code/crowd17/report_inbox/battery-governed-excl-inf-topic-audit.md`.
- Queue: `governed-excl-inf-topic-audit` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion. R5005, sealed gates, red-team adjudication queue untouched.
