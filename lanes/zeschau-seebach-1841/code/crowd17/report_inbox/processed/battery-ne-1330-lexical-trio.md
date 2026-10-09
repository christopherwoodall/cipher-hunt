# Battery `ne-1330-lexical-trio` — do prescrire/préserver/prévoir license bare-'ne'?

- Target id: `ne-1330-lexical-trio` (priority 3)
- Date: 2026-10-09
- Worker session: a3461ac0-9a6c-4ab8-b52d-58aec6dc50cf
- Lock: `code/crowd17/next-token/locks/ne-1330-lexical-trio.lock` (created 2026-10-09T13:44Z, deleted on completion)
- Stream/corpus: corpus battery. Two corpora: (1) the lane's 1841 period corpus
  `code/side-period/corpus` (75 files, 34,525,238 chars read); (2) a new modern
  formal-register control — Europarl French (Helsinki-NLP/europarl, en-fr
  train-00000-of-00002.parquet, French column only: 1,025,507 sentences,
  172,572,549 chars; sha256 dca560a6...6dff; retrieved 2026-10-09 via curl).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "bare ne" = the word "ne" (or elided "n'") with no negation
partner ("pas", "point", "que", "ni", "jamais", "plus", "rien", "personne",
"aucun", "guère", "mot", "nulle part", "aucunement") in its clause.
"genuine" = a real main-clause attestation, not an OCR fragment, subordinate
clause, expletive-"ne", imperative, or transcription defect.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

">=1 genuine bare-ne + prescrire/préserver/prévoir attestation, or a
verb-lexicon sample showing the licensed class is closed."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** ≥1 genuine bare-"ne" + prescrire/préserver/prévoir attestation in the
   wider (1841 + modern-control) corpora → the trio verbs specifically license
   bare-'ne' government (PROMOTE on the specific-license arm).
2. **C2:** else, a verb-lexicon sample showing the licensed class is closed →
   accept the construction-level license as sufficient, i.e. as the final word
   on this question (PROMOTE on the closure arm).

Parent context (adopted, not re-litigated): `ne-1330-bare-corpus` PROMOTE
(2026-10-09) — bare "ne" + finite verb is a live 1841 main-clause construction,
including the exact "ne [finite] de [INF]" shape; the genuine class is lexically
bounded to pouvoir, savoir, oser, cesser, falloir, vouloir, devoir (+ idioms);
targeted search for bare-"ne" + trio verbs returned zero in 32.9M chars.
R19-167 adopted: 94 = single syllabic "ne" (split CLOSED).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/ne-1330-lexical-trio.lock` on
   start; deleted on completion.
2. Census script `code/crowd17/next-token/ne1330_lexical_trio_census.py`:
   - All conjugated forms of prescrire/préserver/prévoir (every tense and mood,
     accented and unaccented spellings).
   - Pattern: "ne"/"n'" + 0–3 clitics + trio-verb form; sentence partner check.
   - Whitespace-normalized search per the lane's standing corpus-zero rule.
   - Methodology fixes applied after a first run: curly apostrophes (U+2019)
     normalized before tokenizing (the first run missed "ne ... qu'" partners
     written with curly quotes); "ne"/"n'" detected on accent-preserving
     lowercase so the participle "né" is not read as the particle; partners
     extended with "mot" ("ne ... mot"), "aucunement", and the "nulle part"
     bigram. (Note: "n'" never elides before these three verbs — no form starts
     with a vowel — so zero "n'" hits is expected, not a bug.)
3. Lexicon script `code/crowd17/next-token/ne1330_lexclass_census.py` (C2 arm):
   independent extraction of every "ne"/"n'" + 0–3 clitics + head-word instance
   in the modern control; bare (partnerless) candidates auto-classified against
   comprehensive form sets for the 7 licensed verbs + idiom buckets
   ("n'importe", "n'eût", "ne fût-ce"); the full "other" bucket hand-audited by
   head form; a random 60 of the auto-licensed hand-audited for validation.

## Evidence

### C1 — trio-verb census (0 genuine in 207.1M chars)

- 1841 corpus: 28 "ne" + trio-verb hits, **0 bare**. All 28 carry partners
  ("ne prévoit pas", "ne prévoient que", "ne prescrivent que",
  "ne prescrivent non plus aucune" — the two "ne prescrivent" hits are both in
  levant-correspondence-1841-p3.txt, independently reproducing the parent's
  finding verbatim).
- Modern Europarl control: 406 "ne" + trio-verb hits, **0 bare**. Top forms:
  "prévoit" ×281, "prévoient" ×43, "prévoie" ×21 — every one partnered
  ("ne prévoit pas/plus/aucune", "que ne le prévoit").
- Combined: **434 hits, 0 genuine bare-"ne" + prescrire/préserver/prévoir**
  across 207,097,787 chars of 1841 diplomatic/literary French and modern formal
  French. **C1 FAILS.**

### C2 — verb-lexicon sample (licensed class is closed)

Modern Europarl control, independent extraction: 162,756 "ne"/"n'" instances →
5,435 bare strict candidates.

- 5,032 (92.6%) auto-classify to the 7 licensed verbs
  (pouvoir, savoir, oser, cesser, falloir, vouloir, devoir).
- 12 idiom ("n'importe", "n'eût", "ne fût-ce", "il n'empêche",
  "ne vous en déplaise", "si je ne m'abuse / me trompe", "n'avoir cure").
- Random 60 of the auto-licensed hand-audited: **60/60 genuine main-clause
  bare-"ne", all licensed verbs** (pouvoir ×50, cesser ×5, savoir ×5), including
  "je ne puis" (the "puis" form the first classifier missed — fixed).
- The full "other" bucket (140 distinct heads, 391 instances) hand-audited by
  head form. It dissolves completely:
  - partnered via fused/adverbial partners the token check misses
    ("d'aucun/d'aucune", "aucunement", "ne ... mot", "ne ... guère",
    "nulle part", "nulle trace"): disposer ×80, faire ×24, jouir ×9,
    bénéficier ×14, être/avoir ×~40, etc.;
  - "pas" mis-OCRed as "par": parler, sembler, confondre, réglementer,
    remplir, désavouer, dénoncer, faire;
  - expletive-"ne" / subordinate clauses ("craindre qu'il ne soit",
    relatives, "si"-protases, indirect questions);
  - non-finite heads ("de ne pouvoir", "ne pouvant", "à ne cesser");
  - artifacts (Latin "ne bis in idem", proper noun "Ne Win", paren "(ne)",
    participle "né", "ne série" = "une série");
  - negative-subject licensed pattern ("Nul ne connaît", "aucun collègue ne
    souhaite", "Aucunes ressources ... n'ont été intégrées");
  - auxiliary + past participle of licensed verbs ("n'a cessé", "n'ont pu",
    "n'avons cessé");
  - imperatives ("Ne vous faites d'illusions").
- Residual: 13 doubtful instances (0.2%) — e.g. "Je ne compte sur la
  Commission", "l'administration ne semble pouvoir trouver",
  "Il ne s'agit de remettre en question", "le résultat final ne manque
  d'allure", "je ne m'aventurerais à faire" — most plausibly "pas"-drops in
  transcribed parliamentary speech — plus 3 rhetorical-question "Qui ne ...?"
  ("Qui ne lui serait reconnaissant ?"). **None involves prescrire, préserver,
  or prévoir.** No productive new class is established.

The licensed bare-"ne" class is closed: the 7 verbs (+ idioms + the
negative-subject and auxiliary-of-licensed-verb patterns). The trio verbs sit
outside it. **C2's condition is met.**

## Per-clause pass/fail

- **C1 — FAIL.** Zero genuine bare-"ne" + prescrire/préserver/prévoir in
  207.1M chars (1841 + modern formal French). The trio verbs do not license
  bare-'ne' government.
- **C2 — PASS.** The verb-lexicon sample shows the licensed class is closed
  (5,032/5,435 = 92.6% in the 7 verbs; 60/60 hand-audit clean; the 391
  "other" fully accounted for; 0.2% doubtful residue, none trio-related).

## Verdict: PROMOTE (lexical question closed — negatively)

Read this verdict exactly as written: it does **not** license the trio verbs.
It banks the negative result and accepts the construction-level license as the
final word on this question:

- prescrire/préserver/prévoir do **not** specifically license bare-'ne'
  government (definitive 207M-char zero, 1841 + modern control).
- The bare-"ne" licensed class is closed to
  {pouvoir, savoir, oser, cesser, falloir, vouloir, devoir} + idioms.
- Consequence for the @1334 arm ("ne prescrira/préserva/prévoira de [INF]"):
  it stays exactly where `ne-1330-bare-corpus` left it — constructionally
  licensed (the "ne [finite] de [INF]" shape is real), **lexically strained**
  (its verbs sit outside the closed licensed class). The strain is now
  quantified, not lifted. No further lexical batteries are needed on this
  question.

Scope: corpus-lexical only. No stream window re-parsed; no value named for 52;
no standing/red-team verdict contradicted or downgraded (R19-167, A8, §7
intact; 67 sole polyvalence). No polyvalence declared. Canonical-stream caveat
stands. Per §4, promote requires no follow-ups; none are queued (the
rhetorical-question "Qui ne ...?" sub-pattern is noted as an observation, not
a work order — it does not touch the trio question or any declarative window).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ne-1330-lexical-trio.md`
- Census: `code/crowd17/next-token/ne1330_lexical_trio_census.py`,
  `code/crowd17/next-token/ne1330_lexclass_census.py`;
  `ne1330_trio_1841.json` (28 hits, 0 bare),
  `ne1330_trio_modern.json` (406 hits, 0 bare),
  `ne1330_lexclass_modern.json` (5,435 candidates; 140-head "other" audit +
  60-sample validation)
- Modern control provenance: Europarl French v8, Helsinki-NLP/europarl,
  en-fr/train-00000-of-00002.parquet, French column extracted
  (1,025,507 sentences, 172,572,549 chars, sha256
  dca560a6909fd22331c125b53cd59a67b9c69954d45a0425b3818d6d89856dff),
  retrieved 2026-10-09 via curl (HuggingFace Hub direct download; the
  `huggingface_hub` python client is broken on this VM per TOOLS.md).
- Queue: `ne-1330-lexical-trio` → `status: verdict`, `result: promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated from disk; own entry only; no downgrade)
- Lock created on start (2026-10-09T13:44Z), deleted on completion (verified
  gone). R5005, sealed gates, red-team adjudication queue untouched.
