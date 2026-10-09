# Battery `ne-1330-bare-corpus` — corpus check: bare "ne" + finite verb in 1841 main clauses

- Target id: `ne-1330-bare-corpus` (priority 3)
- Date: 2026-10-09
- Worker session: 98f1b96f-169c-45c9-a78c-2f8a1be52873
- Lock: `code/crowd17/next-token/locks/ne-1330-bare-corpus.lock` (created 2026-10-09T12:57Z, deleted on completion)
- Stream/corpus: this is a corpus battery, not a stream battery. Corpus = the lane's
  period corpus `code/side-period/corpus` (71 files, 32,895,030 chars read).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "bare ne" = the word "ne" with no negation partner
("pas", "point", "que", "ni", "jamais", "plus", "rien", "personne", "aucun",
"guère", "mie", "goutte") in its clause. "main clause" = a clause that is not
a subordinate clause (expletive-"ne" subordinates like "craindre que ... ne",
"empêcher que ... ne", "à moins que ... ne", comparatives "moins ... que ... ne"
are excluded). "genuine" = a real 1841 main clause, not an OCR fragment or a
sentence-split artifact.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"Bar: corpus check: bare "ne" + finite verb with no "pas"/"que"/"point" partner
in 1841 main clauses — attested or absent? Bar: ≥1 genuine main-clause
attestation keeps the finite-verb reading unstrained; confirmed zero across the
lane's period corpora kills the finite-verb arm at @1334 (all three candidates
die together; the word-internal-39 reading dies with them). 3.
**`subj-62-1329-agree`** (P3) — name 62 at @1329 (the "ne pre[52]a" subject
slot). Bar: if 62 names plural, all three 3sg candidates die by agreement
(fence, not kill, pending 62's own standing); if 62='il' (battery-promoted)
holds, the 3sg agreement leg is banked for the surviving subset."

Numbered pass/fail clauses (restated before testing, not modified after; the
`subj-62-1329-agree` text is the parent's follow-up 3, a separate queued
target — not this battery's bar):

1. **C1:** ≥1 genuine main-clause attestation of bare "ne" + finite verb in the
   lane's period corpora → the finite-verb arm at @1334 stays unstrained
   (PROMOTE).
2. **C2:** confirmed zero across the lane's period corpora → the finite-verb
   arm at @1334 dies at kill grade, all three candidates together (KILL).

Parent context (adopted, not re-litigated): `syll-52-locus-1334` NULL
(2026-10-09) — the @1334 locus reads "…[62] ne pre[52]a de [86-INF] …" with
three finite candidates ("ne prescrira / préserva / prévoira de [INF]") and a
partnerless "ne" at 0-based @1330 (nearest 30='pas' @1368 belongs to the local
"[60] [03] pas" clause). R19-167 adopted: 94 = single syllabic "ne" (split
CLOSED); the @1330 "ne" is the particle.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/ne-1330-bare-corpus.lock` on
   start; deleted on completion.
2. Census script `code/crowd17/next-token/ne1330_bare_corpus_census.py`:
   - Sentence split on `[.!?…;:]` after normalizing single newlines to spaces
     (prose line-wrap). Paragraph breaks kept. **Methodology fix:** an early
     run split on raw newlines and produced 6,096 "bare" candidates; the
     hand-audit caught the artifact class ("elle ne servira / qu'à démontrer"
     — restrictive "que" on the next line, nesselrode-v7.txt). After the fix:
     **2,229 strict candidates**. This follows the R19 standing rule that
     corpus zeros require whitespace-normalized search.
   - Candidate = a sentence with a standalone "ne" (or elided "n'") whose
     nearest verb-shaped head (0–3 clitics skipped: le/la/les/lui/leur/me/te/se/
     nous/vous/en/y/m'/t'/s'/l'/d'/qu') matches finite-verb morphology
     (common-finite lexicon + distinctive finite endings), and the sentence
     contains NO strict-tier partner. Strict tier =
     {pas, point, que, ni, jamais, plus, rien, personne, aucun, aucune, guère,
     mie, goutte}; restrictive "que/qu'" must FOLLOW the "ne" to count
     (fused "qu'il"/"qu'une" tokens handled; "parce/puisque/lorsque/quoique +
     qu'" conjunctions excluded). A literal tier (partners = pas/point/que
     only, the bar's wording) is recorded for comparison.
   - 34,863 standalone "ne" hits + 26,072 elided "n'" hits scanned.
   - All candidates hand-audited for main-clause status and genuineness.
     Known generator holes, all closed on audit: expletive-"ne" subordinates,
     comparatives, "nullement"/"nulle part" (negative adverbials, not in the
     token partner set), fused "d'aucune" (partner missed by token check),
     OCR fragments.

## Window-level evidence (genuine main-clause bare-"ne" attestations)

**C1 passes many times over.** A sample of the genuine attestations (all
1841-period sources, all main clauses, all partnerless):

- "on ne peut le surprendre avec certains argumens" (revue-deux-mondes-1841-q4)
- "nulle ne peut dominer et imposer ses décisions" (revue-deux-mondes-1841-q4)
- "je ne sais si le bruit est fondé" (nesselrode-v7 — epistolary/diplomatic,
  the cipher's own register)
- "ne saurait être trop soutenue et trop encouragée" (revue-deux-mondes-1841-q1)
- "Delessert ne pouvait être soupçonné de malveillance" (guizot-memoires-t2)
- "ces sophismes ... qui veut se satisfaire et n'ose s'avouer"
  (guizot-memoires-t2)
- "Je n'ose demander à qui." (hugo-ruy-blas)
- "je ne cesse de rapprocher tout le monde" (pozzo-di-borgo-correspondance)
- "Il ne cesse de discourir et tient des propos incohérents." (nesselrode-v8)
- "une conversation à fond ne put avoir lieu entre nous"
  (metternich-papiere-v4 — passé simple)
- "Je ne saurais l'accepter." (revue-deux-mondes-1841-q4)
- "Un pair ne pourra réunir sur sa tête plusieurs de ces majorats."
  (guizot-memoires-t1 — future)
- "La nuit tu ne pourras tourner les yeux, ô roi." (hugo-hernani — future)
- "Nul ne le sait." (revue-deux-mondes-1841-q1)
- "N'importe, l'Opéra vient de donner signe de vie" (revue-deux-mondes-1841-q2)

The licensed bare-"ne" class in 1841: **pouvoir, savoir, oser, cesser, falloir,
vouloir, devoir** (1,307/2,229 strict candidates), plus the "nul/nulle"-subject
construction, the "n'importe" idiom, and conditional forms ("n'eût été").
Critically for the cipher arm, the **exact constructional shape is attested**:
"ne [finite] de [INF]" — "je ne cesse de rapprocher tout le monde",
"Il ne cesse de discourir".

**Sharpening (stated, not hidden):** the genuine class is lexically bounded.
Targeted corpus-wide search for "ne/n'" directly governing
prescrire/préserver/prévoir (any tense): **zero** in 32.9M chars. The only two
"ne prescrivent" hits both carry partners ("ne prescrivent que les moyens",
"ne prescrivent non plus aucune autre manière" — levant-correspondence-1841-p3).
The three cipher candidates' verbs sit outside the licensed bare-"ne" class;
their strain is lexical, not constructional. The bar as written asks only for
the constructional question, which passes — the lexical question is proposed
as a continuation below.

Excluded on audit (not genuine): expletive-"ne" subordinates ("je crains
qu'il ne se soit fait", "prendre garde qu'on ne me donne",
"Sa visière empêcha qu'on ne vît"), comparatives ("moins ... qu'on ne le
dit"), restrictive "ne...que" missed by the first run's line-break split
("elle ne servira qu'à démontrer"), "nullement"/"nulle part" adverbials,
fused "d'aucune"/"qu'aucune" partners, OCR fragments.

## Per-clause pass/fail

- **C1 — PASS.** ≥1 genuine main-clause attestation of bare "ne" + finite verb
  is confirmed many times over, in 1841-period sources, including the cipher's
  own diplomatic register (Nesselrode, Guizot, Metternich correspondence) and
  including the exact "ne [finite] de [INF]" shape ("ne cesse de rapprocher").
- **C2 — antecedent false.** No confirmed zero; does not fire.

## Verdict: PROMOTE

The finite-verb arm at @1334 stays unstrained: bare "ne" + finite verb is a
live 1841 main-clause construction, and the exact "ne [finite] de [INF]"
shape the locus needs is attested ("ne cesse de rapprocher", "ne cesse de
discourir"). All three candidates ("ne prescrira / préserva / prévoira de
[INF]") survive this battery together; the word-internal-39 reading is not
re-opened by this result.

Scope: construction-level only. This battery does not name 52's value, does
not touch the 52="a" uniformity tension (unif-52a-1334-orphan venue), and does
not re-litigate R19-167 (94 = single "ne"). No standing/red-team verdict
contradicted or downgraded; §7 intact (67 sole polyvalence). No polyvalence
declared.

One optional continuation proposed (promote needs none per §4):
`ne-1330-lexical-trio` (P3) — the sharpening above: test whether
prescrire/préserver/prévoir specifically license bare-"ne" government in a
wider (or modern-control) corpus, or accept the construction-level license as
sufficient. Bar: ≥1 genuine bare-ne + prescrire/préserver/prévoir attestation,
or a verb-lexicon sample showing the licensed class is closed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ne-1330-bare-corpus.md`
- Census: `code/crowd17/next-token/ne1330_bare_corpus_census.py`;
  `ne1330_bare_corpus_candidates.json` (2,229 strict);
  `ne1330_bare_corpus_literal_extra.json` (5,329 literal-tier-only);
  `ne1330_bare_corpus_meta.json`
- Queue: `ne-1330-bare-corpus` → `status: verdict`, `result: promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated from disk; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone). R5005, sealed
  gates, red-team adjudication queue untouched.
