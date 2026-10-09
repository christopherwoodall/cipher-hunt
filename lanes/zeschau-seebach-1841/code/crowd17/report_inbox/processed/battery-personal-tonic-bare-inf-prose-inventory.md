# Battery report: personal-tonic-bare-inf-prose-inventory

- Target id: `personal-tonic-bare-inf-prose-inventory`
- Claim: ranked head-class inventory of BARE exclamatory infinitives under tonic-pronoun topics in the prose corpus
- Date: 2026-10-09
- Stream: corpus census per target charter; the 1,847-pair repaired parse not applicable (no cipher data touched). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause. "Bare exclamatory infinitive" = an infinitive with no governing preposition or modal, carrying exclamatory force itself ("Moi, voler !"). "Tonic pronoun" = moi/toi/lui/elle/nous/vous/eux. "Head-class" = the valency class of the infinitive head (transitive / intransitive / pronominal / auxiliary).

## Parentage

Follow-up #1 of `personal-tonic-governed-excl-prose` (NULL 2026-10-09): the governed shape ("Moi, pour rire !") is fenced in prose, and the parent proposed this inventory because the bare shape was thought to live in prose too. Prose-register counterpart of `disloc-tonic-personal-census` (PROMOTE: 21 genuine bare exclamatory infinitives under dislocated personal tonic pronouns in 2.97M chars of drama).

## Bar (verbatim, pre-registered before testing)

"Ranked head-class inventory of BARE exclamatory infinitives under tonic-pronoun topics in the prose corpus."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **Clause 1 (deliverable):** a ranked head-class inventory of every genuine bare exclamatory infinitive under a dislocated tonic-pronoun topic in the 27.66M-char prose corpus, with each candidate classified with cause. PASS iff the full candidate set is classified with stated cause and the genuine set is inventoried by head-class with byte evidence.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/personal-tonic-bare-inf-prose-inventory.lock` on start (2026-10-09T15:00Z); no prior lock existed for this id.
2. Re-runnable script: `code/crowd17/next-token/personal_tonic_bare_inf_prose_census.py`; raw results in `code/crowd17/next-token/personal-tonic-bare-inf-prose-inventory_census.json` (66 candidates, each with a `cause` field added in-session).
3. P1/P2/P3 copied VERBATIM from the drama sibling (`disloc_tonic_personal_census.py`), not modified after seeing data:
   - P1: `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:](case-insensitive)`; window = pronoun through the next `[!?.]` (inclusive), capped at 180 chars.
   - P2: window must contain `!`.
   - P3: `\b[a-z…]{2,}(er|ir|re|oir)\b` on the window (bare-infinitive candidate; no governor required).
   All 66 candidates hand-classified against wider context using the drama taxonomy: **a** = governed infinitive (pour/de/à, participle/noun-governed — confound, excluded); **b** = modal-governed (pouvoir/vouloir/devoir/aller); **c** = finite clause (topic of a finite verb, or pronoun is inverted finite subject); **d** = nominal exclamation; **f** = pronoun governed, not a topic; **g** = no true infinitive (inf-shaped noun/adjective); **h** = imperative; **i** = vocative; **p** = purpose adjunct.
4. Corpus VERBATIM from the parent prose battery (20 files, 27,656,185 chars, computed in-session — matches exactly): 17 files in `code/side-period/corpus/`, 3 files in `data/`.

## Yield

4,495 pronoun-comma hits across 27,656,185 chars → **66 bare-inf candidates** → all hand-classified → **1 genuine**.

## The ranked prose inventory (genuine set)

Head-class scheme: valency of the infinitive head.

| Rank | Head-class | Heads (n) | Evidence |
|------|-----------|-----------|----------|
| 1 | Transitive | 1 | voler — rdm-q1 @1331887: "— Moi, voler! répond le bon Charlemagne" (indignant refusal of the angel's order "d'aller voler"; voler = "steal", transitive) |
| 2 | Intransitive | 0 | — |
| 2 | Pronominal | 0 | — |
| 2 | Auxiliary (inf. composé) | 0 | — |

## Classification of all 66 candidates (with cause)

**Governed infinitive (a, 17 incl. dual):** [00] (à épurer/fortifier governed by "tendent"); [03] ("avoir" governed by "digne d'en"); [17] ("entrer" governed by "ayant vu"); [18] ("deviner" governed by "cherchant"); [22] ("franchir" governed by "prêt"); [27] ("plaindre" governed by "ayons"); [31] ("repousser" governed by "prendre plaisir à"); [37] ("voir" governed by "quelle joie de", "courir" by "voir"); [38] ("seconder" governed by "interdit à…de"); [43] ("exciter" governed by "envoyés"); [44] ("rassurer" governed by "les moyens"); [46] ("attendre" governed by "à"); [47] ("faire/mouvoir/débrouiller/marcher" governed by "forcé"); [48] ("faire" governed by "vient de"); [51] ("voir/juger/être" governed by "manière"); [52] ("savoir" governed by "la question"); [60] ("comprendre" governed by "l'air").

**Modal-governed (b, 12 incl. dual):** [13] ("veux mourir"); [19] ("veux…suivre"); [23] ("peut…voir"); [24] ("voudraient aller"); [32] ("peut…méconnaître"); [40] ("vouloir tourner"); [41] ("sauriez croire"); [42] ("rencontrer" governed by modal "Puissiez" = pouvoir subjunctive; "vous" is the inverted optative subject, not a topic); [59] ("vais être"); [62] ("va…finir/être"); [65] ("a cru devoir", "s'élever" governed).

**Finite-clause topic (c, 15 incl. dual):** [02] ("eux" topic of "se trouve"); [04] ("Moi, j'apprendrai"); [09] (topic of "c'est par une injure"); [14] (topic of "je reconnais"); [19] ("je vous quitte"); [26] ("moi, je pleure"); [28] ("moi, ce n'est plus…"); [32]; [35] ("je me brouillerais"); [36] ("que ne ferais-je"); [48]; [57] (relative clause); [58] ("lui" topic of finite; "!" is quoted); [60]; [64] ("elle" is the inverted subject of "s'écria-t-elle", not a topic; the echo "aller chercher mon enfant!" has understood subject "je" and NP topic "Mon enfant").

**Nominal exclamation (d):** [61] ("vous, un homme respectable, un maire, un magistrat!").

**Pronoun governed, not a topic (f):** [00] ("nous" governed by "parmi"); [07] ("moi" governed by "de moi"; "Implorer" governed by "De" in the "quelle joie de…" verse enumeration); [55] ("eux" governed by "chez eux"; OCR-mangled text, "!" on "les anusemen!").

**No true infinitive (g):** [05] (votre/vôtre nouns); [06] (terre/étrangère/barbare); [12] ("nécessaire" adjective, "i!" OCR); [15] ("l'affaire"); [16] ("singulière"); [20] ("noir"); [21]; [25] ("ordinaire"); [33] ("tibre" river); [34] ("frère"); [39] ("heure"); [45] ("l'autre"); [49]/[50] ("pouvoir/l'avenir" nouns); [53] ("rupture"); [54] ("gloire/quatre"); [56] ("vizir"); [63] ("maire").

**Imperative (h):** [11] ("aidez-moi"); [20] ("ménage"); [21] ("dévore"); [29] ("laissez-moi").

**Vocative (i):** [08] (first "vous" vocative).

**Purpose adjunct (p):** [01] ("lui, pour prendre la parole"; "!" belongs to the downstream quote).

## Correction to the parent's seed window

The parent's follow-up proposal said "window [14] here shows the bare shape lives in prose too" (rdm-q4 @1248948, "vous, au bout de votre carrière, rencontrer moins d'épines…!"). On the 500-char context this window's infinitive is **modal-governed**: "Puissiez-vous … rencontrer" (pouvoir, subjunctive optative), and "vous" is the inverted finite subject, not a topic. It is class **b**, not bare. The genuine prose bare-shape evidence is [10] ("Moi, voler!"), not [14]. This corrects the parent's seed attribution; the parent's NULL verdict on the governed shape is untouched.

## Cross-register comparison (context, not re-verified)

The drama sibling's 21 genuine windows carry 25 infinitive heads, ranked by the same head-class scheme: **Transitive 15** (contrarier, baiser, tromper, refuser, quitter ×4, céder, déprécier, donner, trahir, épouser, tuer), **Intransitive 7** (mourir, pleurer, souffrir, fuir ×3, renoncer), **Pronominal 2** (s'en aller, s'éloigner), **Auxiliary 1** (avoir oublié). Prose: 1 head (transitive) in 27.66M chars vs 25 heads in 2.97M chars of drama. The bare exclamatory infinitive under tonic-pronoun topics is a drama-register construction, nearly unattested in prose.

## Per-clause pass/fail

1. **Clause 1 (deliverable): PASS.** All 66 candidates classified with stated cause; the genuine set (1 window) inventoried by head-class with byte-exact offsets and the ranked table above. No unclassified residue.

## Verdict: PROMOTE

The ranked head-class inventory is delivered at battery grade: 1 genuine bare exclamatory infinitive under a dislocated tonic-pronoun topic in 27.66M chars of prose (Transitive: voler). No standing or red-team verdict contradicted; §7 untouched. No value named, nothing adjudicated. Corpus note: metternich-papiere v4/v6 contain German-language passages; no classified candidate depended on German text.

## Follow-ups (none required per §4 — promote)

None. The inventory is complete. The register-contrast finding (prose 1 vs drama 21) is banked as evidence for the red-team frame venue.

## Adverses, answered

- None pre-registered ("Adverses: None").
- Self-check: the parent's [14]-as-bare misread corrected above (no verdict changed); drama sibling's 21 genuine untouched.

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/personal-tonic-bare-inf-prose-inventory.lock` created on start, deleted on completion.
- Census script: `code/crowd17/next-token/personal_tonic_bare_inf_prose_census.py`; raw JSON with per-candidate `cause` fields: `code/crowd17/next-token/personal-tonic-bare-inf-prose-inventory_census.json`.
- `battery-queue.json` updated via temp-file + rename (own entry only; no downgrade).
