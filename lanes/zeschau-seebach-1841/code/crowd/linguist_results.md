# LINGUIST — era+register priors for the 1841 French diplomatic syllabary
Lane: `zeschau-seebach-1841` · R5005, 18 Jan 1841, Dresden→St Petersburg, French diplomatic despatch
Author role: THE LINGUIST (crowd) · 2026-10-07
Status marks: **[OBS]** = observed/quoted from source · **[DER]** = computed by me, method given · **[INF]** = inference, do not treat as fact

## Verdict: the biggest traps

1. **Register mismatch dwarfs era mismatch.** Les Misérables (1862) is a novel: third-person narration, dialogue, argot. A diplomatic despatch is first-person formulaic administrative French ("J'ai l'honneur de…", "Agréez… l'assurance de ma haute considération"). Bigram/trigram rates from Les Mis actively steer a solver toward novel-shaped transitions (dialogue tags, "dit-il", "ça") and away from despatch-shaped ones. This is the most likely mechanism behind Bourdeau's "fluent nonsense" solver drift.
2. **Orthography is era-consistent but treacherous in the opposite direction:** 1841 chancery French is *post-1835, pre-1878*: "collége" (not collège), "poëte" (diaeresis, not poète), "rhythme"/"aphthe" (restored Greek digraphs, not rythme/aphte), "asyle" (not asile), but "français"/"était"/"enfants" (1835 reform done). Cribs must use these spellings, not modern ones. German (Saxon) chancery hands add irregular accentuation (cf. Daschkoff 1809: "réspéctueux", "vôtre").
3. **"cela"≫"ça" (47:1 in print, 1835–1850).** In diplomatic register "ça" is effectively absent. The attempt-2 "cela"-rate match for 87=ce is consistent but weak evidence (cela is era-standard in every register, not diagnostic of Les Mis).
4. **Single-letter groups are real and frequent.** Anchors 82=m, 34=i, 40=e fit: in my syllabification of 98k words of 1826 diplomatic French, single letters l/d/s/m/i/y/e/é/a/à are all top-60 syllables — elided forms (l', d', s', m', j', n') are the mechanism.

---

## 1. 1841 French orthography (post-1835, pre-1878)

**[OBS]** The 1835 reform (6th ed. of the Dictionnaire de l'Académie) made two big changes, in force by 1841: (a) plurals of -nt words restored the t: "enfans"→"enfants", "parens"→"parents"; (b) oi pronounced [ɛ] → ai: "j'avois"→"j'avais", "il faisoit"→"il faisait", "françois"→"français", "étoit"→"était". Source: fr.wikipedia.org, "Réforme de l'orthographe française de 1835". A 1841 despatch writes "français", "était", "enfants" — pre-1835 spellings would flag a different/older hand.

**[OBS]** The same 1835 edition restored etymological Greek digraphs and old -y spellings, in force 1835–1878: "rhythme" (not rythme), "aphthe" (not aphte), "asyle" (not asile), "anévrysme", "abyme" (source: fr.wikipedia 1835-reform article). **And the diaeresis spellings "poëte"/"poëme" (not poète/poème) and the -é- spellings "collége", "Liége", "siége", "avénement" (not collège/Liège/siège/avènement) were standard until the 1878 reform** (source: fr.wikipedia.org, "Réforme de l'orthographe française de 1878"). Expect "collége" in an 1841 despatch.

**[OBS]** Dateline month capitalization: two official French letters of the era write "Paris, (Place Vendôme No 12) / Le 27 Mai 1839" and "Paris, / le 12 Octobre 1840" — months capitalized ("Mai", "Octobre"). Source: Fox Talbot Correspondence Project, docs 3884 and 04143 (foxtalbot.dmu.ac.uk). Expect "Dresde, le 18 Janvier 1841" rather than modern lowercase.

**[OBS]** Chancery abbreviations in the period: "&c." (et cetera, seen in the 1839 Talbot letter: "&c, &c, &c"), "V. Exe." (Votre Excellence), "S. M." (Sa Majesté), "S. A." (Son Altesse), "M.r"/"Mr" (Monsieur) — seen in Meisel, *Cours de style diplomatique* (1826), e.g. "Je renouvelle à V. Exe. l'assurance de ma considération distinguée". If the cipher text contains clear abbreviations, they sit outside the syllabary.

**[INF]** German-chancery accent noise: the Saxon foreign office wrote French as a second language; Daschkoff's 1809 Russian-chancery French shows "réspéctueux", "vôtre", "jouisser" (founders.archives.gov, Jefferson Papers). Expect possible é/è/ê instability and treat "é"/"è"/"e" as potentially conflated in the key.

---

## 2. Syllable inventory with frequency tiers

Two sources. (a) **[OBS]** Chetail & Mathey (2010), *J. Psycholinguist. Res.* 39:485–504, InfoSyll analysis of written French: top-10 orthographic syllables = **ment, a, dé, té, tion, ter, é, ti, ma, ca**; CV is the dominant structure (26.4% of orthographic syllables), then CVC (15.4%). (b) **[DER]** My syllabification of 98,229 words of Meisel, *Cours de style diplomatique* (Paris, 1826; public domain, OCR'd via archive.org, noise flagged) — 178,188 syllable tokens, 3,286 types. My vowel-unit list missed the "ui" diphthong (so "qui"→"qu"+"i" there) and double-consonant clusters syllabify as coda+onset ("pren-dre"); treat counts as ±10% estimates, not exact. Qualitative overlap with Chetail-Mathey is good (a, dé, té, tion, ter, é, ti all in my top 35).

### Tier 0 — >1.5% of syllable tokens (expect every one to have a group; highest-frequency crib targets)
de 3.48 · re 2.58 · le 2.13 · et 1.89 · les 1.86 · i 1.77 · la 1.76 · a 1.55 · qu 1.32 · que 1.19 · ce 1.14 · à 1.12 · des 1.12 · é 1.12 · e 1.08 · en 1.07

### Tier 1 — 0.35–1.0% (the productive middle of the syllabary)
res · te · té · l · se · ent · un · d · ti · par · con · tion · li · ra · au · si · me · ré · du · pour · dé · ces · ri · s · il · ne · dans · es · tes · in · y · m · is · com · nous · pa · di · ci · su · sa · né · tions · est

### Tier 2 — 0.08–0.35% (still likely keyed; formula-relevant)
ter · on · vous · tout · sur · plus · pas · est · son · ma · mon · je · sont · fait · bien · ant · an · aux · point · dont · sans · sous · ment · ait · er · ur · ais · hon · oi

### Single-letter inventory **[DER/INF]**
The key demonstrably uses single letters (82=m, 34=i, 40=e). My table shows these single letters all in the top 60: **l** 0.86%, **d** 0.75%, **s** 0.51%, **m** 0.40%, **y** 0.42% (from "y" in "il y a"), **i** 1.77%, **e** 1.08%, **é** 1.12%, **a** 1.55%, **à** 1.12%. Mechanism: elision (l', d', s', m', j', n', qu') + word-final silent -e/-es. Expect also **n** (n'), **j** (j'ai), **t** (t-on, t-il in inversions — rare in despatches), **c** (c'). A 96-group key ≈ all of Tier 0+1 (~55 units) + Tier 2 + single letters + a tail of rarer syllables.

### Top syllable bigrams **[DER]** (same Meisel corpus; useful for drag-ordering, register-appropriate)
qu+i · un+e · el+le · pu+is · a+vec · not+re · mê+me · lu+i · cet+te · com+me · è+re · êt+re · gé+né · lem+ent · é+té · fai+re · ent+re · min+ist(re) · se+ra · é+tats · tou+tes · li+té · fran+ce · sou+ve · se+ront · aut+res · i+i · ra+tion · vot+re · con+ven · lett+res · gou+ver · pré+sen · déc+la · aus+si · é+tat
(Note: "qu+i" = "qui/qu'il"; "i+i" is an OCR/syllabifier artifact of "ii" sequences — discount it.)

---

## 3. 1840s diplomatic formulae — with syllable segmentations

Segmentation uses standard orthographic syllabification (diphthongs kept: qui, eau; double consonants split: hon-neur, con-si-dé-ra-tion; elided consonant = its own unit: l', d', j'). Status per formula.

### Openings
- **[OBS]** "Monsieur," → **mon-sieur** (2) — the standard despatch salutation; seen in Talbot 1839 letter ("Monsieur,"). Variant with title: "Monsieur le Baron," → **mon-sieur-le-ba-ron** (5) — attested as a form in 19th-c. epistolary manuals (Ducret 1829–1909, via puc.hypotheses.org).
- **[OBS]** "Dresde, le 18 Janvier 1841." → **dres-de-le-18-jan-vier-1841** — dateline shape from Talbot docs 3884/04143 ("Le 27 Mai 1839"; "le 12 Octobre 1840"); month capitalized **[OBS]**, city French-spelled **[INF]**.
- **[OBS]** "J'ai l'honneur de vous informer que" → **j'ai-l'-hon-neur-de-vous-in-for-mer-que** (10) — attested in a model letter in Meisel (1826), p.465: "j'ai l'honneur de vous informer que depuis…".
- **[INF]** "J'ai l'honneur de vous transmettre" → **j'ai-l'-hon-neur-de-vous-trans-mett-re** — genre-standard variant, unverified verbatim.

### Reference / administrative formulae (the despatch's connective tissue)
- **[INF]** "Par ma dépêche du [date]" → **par-ma-dé-pê-che-du-…** — genre-standard self-reference; unverified verbatim for Saxon 1841.
- **[INF]** "En réponse à la dépêche de Votre Excellence du [date]" → **en-ré-pon-se-à-la-dé-pê-che-de-vo-tre-ex-cel-len-ce-du-…** — genre-standard; unverified verbatim.
- **[INF]** "J'ai l'honneur d'accuser à Votre Excellence réception de sa dépêche du" → **j'ai-l'-hon-neur-d'ac-cu-ser-à-vo-tre-ex-cel-len-ce-ré-ce-ption-de-sa-dé-pê-che-du** — the standard acknowledgement formula of the period; unverified verbatim for this correspondence.

### Closings (highest-value crib zone — every despatch ends with one)
- **[OBS]** "Agréez, Monsieur, l'assurance de ma haute considération." → **a-gré-ez-mon-sieur-l'-as-su-ran-ce-de-ma-hau-te-con-si-dé-ra-tion** (16) — verbatim in the 12 Oct 1840 official letter (Talbot doc 04143: "Agréez, Monsieur, l'assurance de ma haute considération.").
- **[OBS]** "J'ai l'honneur d'être avec la plus haute considération, Monsieur, Votre très humble et obéissant serviteur" → **j'ai-l'-hon-neur-d'ê-tre-a-vec-la-plus-hau-te-con-si-dé-ra-tion-mon-sieur-vo-tre-très-hum-ble-et-o-béis-sant-ser-vi-teur** — verbatim in the 27 May 1839 letter (Talbot doc 3884: "J'ai l'honneur d'être avec la plus haute considération, Monsieur, Votre très humble et obéissant serviteur").
- **[OBS]** "J'ai l'honneur d'être avec la considération la plus parfaite, etc." → **j'ai-l'-hon-neur-d'ê-tre-a-vec-la-con-si-dé-ra-tion-la-plus-par-fai-te-etc.** — in Meisel (1826), Grenville letter.
- **[OBS]** "Je renouvelle à V. Exe. l'assurance de ma considération distinguée" → **je-re-nou-vel-le-à-v-exe-l'-as-su-ran-ce-de-ma-con-si-dé-ra-tion-dis-tin-guée** — in Meisel (1826).

**[INF — high-value crib hypothesis for the repeat lanes]:** the ×5 repeat `7778948206` is 5 pairs = 5 syllable units. "J'ai l'honneur de" = **j'ai · l' · hon · neur · de** = exactly 5 units, and it is *the* despatch opening formula, plausibly repeated once per subject paragraph in a 70-line despatch. Test: does the pair in the l'-position behave like a single-letter consonant (l/d/s/m), and does the hon–neur adjacency hold? Do not assert without positional checks.

---

## 4. Function-word expectations: epistolary French vs novel French

**[DER]** Era-correct baseline (Google Books French ngrams 2012 corpus, mean 1835–1850, % of tokens):
de 4.37 · la 2.41 · et 2.16 · les 1.72 · le 1.62 · des 1.27 · que 1.11 · en 0.90 · qui 0.86 · du 0.84 · dans 0.79 · un 0.74 · une 0.68 · par 0.63 · pour 0.56 · il 0.55 · ne 0.52 · est 0.49 · se 0.45 · plus 0.45 · ce 0.44 · au 0.43 · sur 0.40 · pas 0.39 · on 0.32 · nous 0.29 · son 0.28 · avec 0.27 · cette 0.27 · ces 0.22 · leur 0.22 · ses 0.22 · comme 0.21 · sa 0.20 · je 0.16 · vous 0.15 · roi 0.063 · gouvernement 0.034 · ministre 0.017 · honneur 0.015 · majesté 0.0052 · considération 0.0051 · assurance 0.0022 · dépêche 0.0011

**[DER]** "cela" 0.0357% vs "ça" 0.00076% — **cela is 47× more frequent** in print 1835–1850. In diplomatic register, ça ≈ 0 (never write "ça" in a despatch).

**[INF]** Epistolary adjustments vs the book-average baseline (directional, for drag weighting):
- **je / vous / Monsieur / honneur / considération / dépêche / Excellence**: expect 5–20× their book rates. "J'ai l'honneur de" alone injects je+l'+honneur+de per occurrence; closings inject considération/assurance/Monsieur. These words are the *cheapest* high-confidence cribs in the genre.
- **il / elle / ils / dit / répondit**: expect well BELOW novel rates. A despatch reports ("on assure que", "il paraît que") but does not narrate; dialogue tags are absent.
- **nous**: the envoy writes as an individual ("j'ai l'honneur"), so **je > nous** in despatches — unlike novels where "nous" is common in dialogue, and unlike royal "nous". **[INF]**
- **Negation**: "ne…pas" standard; "ne…point" still live in formal 1840s prose (my Meisel corpus: point 0.08% of syllables) — expect occasional "ne…point" where a novel-trained model expects "pas".
- **Subjunctive triggers**: "veuillez", "je vous prie de", "il est à désirer que" — formulaic, novel-rare.

---

## 5. Where Les Misérables (1862) misleads — the trap list

1. **Person system.** Les Mis: third-person narration + dialogue ("il", "elle", "ils", "dit-il", "s'écria-t-il"). Despatch: first-person reporter + second-person addressee ("je", "vous"). Any n-gram model trained on Les Mis will overweight *il*-initial and dialogue bigrams and underweight *je/vous*-formula bigrams. **[INF from genre contrast]**
2. **"ça" vs "cela".** Les Mis dialogue uses "ça"; the despatch register forbids it. Attempt-2's "cela"×7 confirmation is real (87=ce stands on "ce que"×3 + positional evidence), but the *rate-match* against Les Mis proves little — cela dominates in every register (47:1). **[DER+INF]**
3. **Argot and neologism.** Hugo's vocabulary includes argot, Spanish/Italian inserts, and coinages with syllables rare or absent in chancery French. Syllable priors from Les Mis will contain junk the 1841 key never used. **[INF]**
4. **Orthography is the *least* mismatched axis** (both pre-1878: poëte, collége), so don't "correct" for era there — correct for it in the *other* direction: cribs must use poëte/collége/rhythme/asyle spellings, not modern ones. **[OBS]**
5. **Sentence rhythm.** Les Mis favors short dramatic sentences and exclamations; despatches favor long periodic sentences with semicolons and nested subordinate clauses ("...dont j'ai l'honneur de..."). Quadgram/5-gram models from Les Mis learn the wrong cadence. **[INF]**
6. **Formula density.** "J'ai l'honneur", "assurance de ma haute considération", "Votre Excellence" occur ~0× in Les Mis and dozens of times per despatch. A Les-Mis-trained solver treats these as improbable sequences — exactly backwards. **[INF]**

## What the attackers should change

1. **Replace the n-gram reference, don't patch it.** The attempt-3 era corpus is the right move; until it lands, weight *function-word + formula* cribs (this document) over Les-Mis bigram rates. Treat all Les-Mis-derived rates as suspect.
2. **Crib the genre, not the language.** Priority drag targets: "j'ai l'honneur de" (5 units — test against the ×5 repeat `7778948206`), "monsieur", "considération", "assurance", "dépêche", "excellence", "agréez". These have known syllable segmentations (§3) and 5–20× expected rates.
3. **Use 1835/1878 spellings in every crib:** collége, poëte, rhythme, asyle, français, était, enfants. A modern-spelled crib that fails may be failing on one letter.
4. **Single letters are first-class groups:** l, d, s, m, n, j, t, c, i, e, é, a, y — the elision system. The key's 96 groups almost certainly include all of these.
5. **"cela", never "ça".** If a candidate reading produces "ça", kill it.
6. **je > nous; vous is everywhere; il narrates nothing.** Rebalance any person-sensitive scoring accordingly.

## Provenance of sources used
- Meisel, H. *Cours de style diplomatique*, Tome I, Paris: Aillaud, 1826 (M DCCC XXVI). Public domain scan via archive.org (`coursdestyledip01meisgoog_text.pdf`); OCR noise present, formulae verified by context. — genre formulae, address rules.
- Fox Talbot Correspondence Project (De Montfort Univ.): doc 3884, Société Française de Statistique → Talbot, 27 May 1839; doc 04143, Académie Royale des Sciences → Talbot, 12 Oct 1840. Transcriptions + translations. — era formulae, dateline capitalization.
- André Daschkoff → Thomas Jefferson, 5 July 1809 (founders.archives.gov, Jefferson Papers). — chancery French accent/orthography noise.
- Chetail & Mathey (2010), "Into the syllable" / InfoSyll analysis, *J. Psycholinguist. Res.* 39:485–504 (fchetail.ulb.ac.be PDF). — published syllable frequency/structure stats.
- Google Books Ngram Viewer, French 2012 corpus (corpus=19), JSON API, queried 2026-10-07. — era function-word rates, cela/ça ratio.
- fr.wikipedia.org: "Réforme de l'orthographe française de 1835", "Réforme de l'orthographe française de 1878", "Réforme de l'orthographe française", "Orthographe du français" (accessed 2026-10-07). — orthography facts.
- Epistolary-manual scholarship: puc.hypotheses.org (Ducret "Monsieur le Baron" commencement forms); elon.io formal-correspondence (closing-formula anatomy, modern but structurally continuous).

## Open questions (for the era-corpus worker / curator)
- Did the Saxon chancery write "Dresde" (French) in datelines? Assumed yes — unverified.
- Are "é/è/e" (and "à/a") distinct groups in the key or merged? The anchors give 40=e; no è/é anchor exists. Chancery accent noise makes this a live question.
- Salutation: "Monsieur," vs "Monsieur le Baron," — Seebach's rank (envoy) suggests the former between minister and envoy, but unverified.
- The ×5 repeat hypothesis ("j'ai l'honneur de") needs positional/bigram checks by the drag lanes — offered as a crib, not a claim.
