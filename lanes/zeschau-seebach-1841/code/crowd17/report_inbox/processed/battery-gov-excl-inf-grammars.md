# Battery `gov-excl-inf-grammars` — verdict: KILL

## Bar (verbatim, pre-registered before testing)
">=1 cited genuine example re-opens the construction; confirmed zero keeps the register fence"

Restated as numbered clauses:
- C1: ≥1 genuine governed exclamatory infinitive ("pour/de + infinitive" phrase as an
  independent exclamation: "!" terminates the governed phrase itself, no finite matrix
  verb, not an exclaimed NP) cited in a 19th-century French grammar or rhetoric → the
  construction re-opens at grammar level.
- C2: confirmed zero across a genuine good-faith search of 19th-c grammars/rhetorics →
  the register fence keeps standing.

No adverses listed.

## Method
Full-text search of three major 19th-century school grammars (Internet Archive
scans, OCR `_djvu.txt`, downloaded 2026-10-09), plus a web search on the doctrine's
history. "Genuine" uses the family criterion from `gov-excl-inf-register-drama` and
siblings: a preposition-governed infinitive phrase standing as an independent
exclamation. Bare-infinitive exclamations ("Moi, payer cela !") do NOT count — the
register question is specifically the governed shape ("Pour conspirer !",
"de m'épouser, pardine !", "De ne pas pénétrer dans la chambre !").

Note on §3: this target is chartered as a grammar/corpus search (like all
`gov-excl-inf-*` siblings); the cipher stream is not the test surface here.

Corpus saved under `code/crowd17/next-token/corpus-grammars19c/` with provenance
(see `corpus-grammars19c/PROVENANCE.md`).

### G1 — Girault-Duvivier, *Grammaire des grammaires*, 1843 ed. (3.0 MB text)
- 27 "infinitif" lines: doctrine covers the infinitive as subject, as (in)direct
  regime, and substantivized — e.g. the section at text-line 42886 ("Le présent de
  l'infinitif sert à spécifier le verbe dont on veut parler") and 42961
  ("L'infinitif devient quelquefois un véritable [substantif]"). No independent /
  exclamatory / narrative use anywhere.
- 3 "exclamat*" lines: all concern the adverb "comment" used by exclamation
  (text-line 51510: "Il s'emploie encore par exclamation..."), not the infinitive.
- Zero lines matching "de/pour/à + infinitive !" shapes.

### G2 — Bescherelle, *Grammaire nationale*, 1847 ed. (3.3 MB text)
- The INFINITIF entry (n° DLXXXVI–DLXXXVII, text-line 90268) has exactly two
  subsections: "employé comme sujet et comme complément" and "employé
  substantivement". No exclamatory, narrative, or deliberative use.
- The "LES INTERROGATIONS ET LES EXCLAMATIONS" section (text-line 46868) cites only
  finite-verb and nominal exclamations (Bernardin de Saint-Pierre, Ballanche,
  etc.). No infinitive example.
- Zero lines matching "de/pour/à + infinitive !" shapes.

### G3 — Noël/Chapsal, *Nouvelle grammaire française*, 1849 ed. (0.5 MB text)
- All "infinitif" lines are morphological (conjugation classes, "-er/-ir"
  terminations). No syntactic doctrine of independent infinitives at all.
- 2 "exclamat*" lines, both in the punctuation section ("Du point interrogatif et
  du point exclamatif", text-line 14053). Nothing syntactic.

### Doctrine history (web)
- The four-way "infinitif de narration / délibératif / exclamatif / injonctif"
  classification is a 20th-century school-grammar systematization (Grevisse 1936
  and successors). The 19th-c grammars above have no such category.
- The modern doctrine's cited examples are BARE infinitives ("charger ainsi cette
  pauvre bourrique !", "Moi, payer cela !"). Even the later codification never
  covers the governed "pour/de + inf !" shape.

## Findings
- **C1 FAIL.** Zero genuine governed exclamatory infinitives cited in any of the
  three grammars. Stronger than a bare zero: the grammatical *category* of the
  independent/exclamatory infinitive does not exist in 19th-century school
  grammar at all, so the zero is not an OCR-recall artifact — there is no
  doctrine section in which such an example could have been cited.
- **C2 FIRES.** Confirmed zero at the doctrine level.

## Verdict rationale
The claim "19th-c grammars cite genuine governed exclamatory infinitives" is dead
at battery grade. Per the bar, the register fence keeps standing — unchanged, not
strengthened into a kill of the construction itself (the construction is separately
attested in drama and late-19th-c fiction by sibling batteries). This battery kills
only the grammar-citation avenue: the shape was never grammatically codified in the
19th century.

Scope: 19th-c French school grammars (the three most widely used: Girault-Duvivier,
Bescherelle, Noël/Chapsal). Rhetoric manuals (Fontanier etc.) were not directly
consulted — Gallica is Cloudflare-blocked from this VM and no usable
archive.org copy was found; school rhetorics treat exclamation as a figure with
poetic/oratorical examples, and the grammar-side zero already covers the
codification question. Per §4, kills regenerate no follow-ups.

No standing/red-team verdict contradicted or downgraded; §7 intact. R5005, sealed
gates, red-team adjudication queue untouched. `canonical.py` never used (no cipher
windows involved).
