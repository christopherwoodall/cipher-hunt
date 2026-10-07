# Seebach cipher lane — RED TEAM adjudication of the period-sources crib list
**Adjudicator: PERIOD-SOURCES red team · 2026-10-07 · kill authority exercised.**
Input: `code/side-period/cribs.md` v2 (121 cards: 32 P0 / 55 P1 / 34 P2).
Kill rule applied: *Zeschau in Dresden on 18 Jan 1841 must plausibly KNOW and SAY it.*

## Verdict counts
- **Survived: 31 P0 (unique; 32 rows, 1 duplicate merged) + 54 P1 + 32 P2 = 117**
- **Killed: 3** (1 P1, 2 P2) — reasons below.
- **Demoted: 0** — no rank changes beyond kills. The miner's own demotions (Kossuth off-list;
  "A la première nouvelle que…" → P2; "J'ai l'honneur de …" → P2) were re-checked and **upheld**.

## KILL LIST (with reasons)
1. **"mon cher comte" (P1, §E)** — KILL. Seebach was a **baron** in 1841 (v9: "le baron de
   Seebach"; corpus index "Seebach (comte)" is the later era). A minister does not misaddress
   his own envoy. The 53× trigram is Nesselrode→other-men register, inapplicable to this despatch.
2. **"Daignez, je vous prie, m'indiquer la conduite que je dois suivre" (P2, v2 formulae)** —
   KILL. Direction reversed: envoy→minister voice. Zeschau writes *down* the chain to Seebach;
   he does not ask his subordinate to indicate the conduct *he* must follow.
3. **"Votre Excellence vient de m'adresser…" (P2, v2 formulae)** — KILL. Same direction reversal
   ("vient de m'adresser" = the writer received from the recipient). Envoy's voice, not the minister's.

## Verification notes (the checks the task ordered)
- **Kossuth demotion VERIFIED.** `grep -i kossuth` over all four 1841 RdM quarters: **0 hits**.
  The only corpus hits are nesselrode-v9/v10 in 1849/1850s contexts ("Rappelé par Kossuth en
  Hongrie (1849)"). Kossuth is a post-1841 figure in this corpus; keeping him off the list is correct.
- **Hong Kong / Treaty of Chuenpi: confirmed absent, never proposed.** Corpus-wide grep for
  `hong kong|hongkong|chuenpi|chuenpee`: **0 hits in all 25 files**. News-lag kill stands as a
  standing rule: Britain took possession 26 Jan 1841 (per lane sources.md) — Dresden on 18 Jan
  could not know. The opium-war P2s (Elliot, Canton, La Chine) name no post-18-Jan news and survive
  as background vocabulary only.
- **Investiture firman.** The firman of investiture (hereditary Egypt) was **issued Feb 1841**
  (lane sources.md) — i.e. *after* R5005's date. What Zeschau knew on 18 Jan: the *terms* under
  negotiation (hereditary Egypt, the Porte's "unbeschränktes Verfügungsrecht" per AZ 11-Jan-1841).
  The crib is the word **"le firman"**, not the firman's content — survives P0, but the card's
  rationale ("firman of investiture due Feb 1841") is future-looking; the drag target is the
  *word*, attested in v8's 1840 firman context ("Le firman et le refus de Mehemet-Ali de l'accepter").
- **Ibrahim at Damascus VERIFIED.** AZ 11-Jan-1841 (7 days before R5005): *"Ibrahim Pascha
  befand sich am 13 Dec. noch zu Damaskus"* — plus a second item "Ibrahim wird unter dem 6 d.
  aus Damaskus gc-". ~5-week-old news via Constantinople→Vienna→Augsburg: fully plausible in
  Dresden by 18 Jan. **Damas (P1)** and **Ibrahim (P1)** survive; this is the freshest dated
  news in the corpus.
- **"première" collision CONFIRMED HANDLED.** "la première" is read at miner coords 754/1034
  (raw 0-based pair offsets **766** and **1054** — verified in `data/upstream-ct_R5005.digits.txt`:
  `11 70 82 34 29` at both). The only "première"-containing cards are P2 "A la première nouvelle
  que…" (flagged: drag with care) and background-vocab "la première fois que" (flagged adjacent).
  Neither re-proposes "première" as unknown. **New red-team flag:** the background adjective list
  (§H) contains standalone **"premier"** — STRUCK from drag consideration; pre|m|i|er is already read.
- **Mehemet-Ali spelling VERIFIED.** RdM house form "Méhémet-Ali": **293× across the four 1841
  quarters** (miner's count exact). Nesselrode: "Mehemet-Ali". AZ 11-Jan-1841 (German): "Mehemed Ali"
  8× — a live by-ear variant. Drag accentless; try all three surfaces.
- **"la Sublime Porte" P1 promotion UPHELD.** "la Sublime Porte" (French article): **157×** in
  levant-correspondence-1841-p3.txt — not just the English papers' form. Survives P1 with a
  parliamentary-paper register note.

## Register ruling (formulae)
Two registers, kept separate as the miner separated them:
- **Official** (despatch body + formal close): "Monsieur le Baron," / "Votre dépêche du …" /
  "Recevez, Monsieur, l'assurance de ma considération distinguée" (Nesselrode's signed hand,
  Levant circular, late 1840 — highest authority in the corpus). Grade note: "haute considération"
  is ambassador-grade; to a baron-envoy **"considération distinguée" outranks "haute considération"**
  — drag the Nesselrode form first.
- **Private/familiar** (Nesselrode→Meyendorff school): "mon cher baron" / "Adieu, mon cher baron" /
  "Tout à vous". Fine as P0/P1 for Zeschau→Seebach (Seebach is family-adjacent: Nesselrode's
  son-in-law per corpus), marked [private] below.

## Surviving P0 (31 unique) — with syllable-cut risk for the drag fleet
Cut-risk key: CLEAN = natural cuts likely · FUSE = encipherer may fuse units · SPLIT = over-split
risk (cf. pre|m|i|er) · LONG = ≥6 units, drag in halves.
| # | crib | syllabification | cut risk | notes |
|---|---|---|---|---|
| 1 | Nesselrode | nes-sel-ro-de | MEDIUM | double-s by-ear (Neselrode); sel\|rode vs se\|l\|rode |
| 2 | l'Empereur | em-pe-reur | LOW-MED | anpereur nasal fusion |
| 3 | Constantinople | cons-tan-ti-no-ple | MEDIUM | 6u; con\|stan\|ti\|no\|ple alt |
| 4 | le traité de Londres | trai-té-de-Lon-dres | CLEAN | Londre by-ear; alt surface #31 |
| 5 | la question orientale | ques-tion-o-rien-tale | MEDIUM | 6u; question 2u fuse risk |
| 6 | l'affaire d'Orient | af-fai-re-d'O-rient | MEDIUM | apostrophe: dOrient vs d\|Orient |
| 7 | l'affaire d'Egypte | af-fai-re-d'E-gyp-te | MED-HIGH | 7u; Ejipte/Égipte by-ear [src: v8 intro, editor voice] |
| 8 | Mehemet-Ali | me-he-met-A-li | MEDIUM | house form Méhémet-Ali (293× RdM); AZ "Mehemed Ali"; hyphen |
| 9 | le firman | fir-man | CLEAN | the word, not the Feb content (see verification) |
| 10 | la Porte | por-te | CLEAN | |
| 11 | les détroits | dé-troits | CLEAN | destroits fuse variant [src: v8 intro, editor voice] |
| 12 | la convention orientale | con-ven-tion-o-rien-tale | MED-HIGH | 7u; convension by-ear |
| 13 | Guizot | gui-zot | CLEAN | Guisot by-ear |
| 14 | Metternich | met-ter-nich | LOW-MED | Meternich/Metternik |
| 15 | Votre dépêche du … | vo-tre-dé-pê-che-du | MEDIUM | dépêche 2↔3 cut; depeche by-ear |
| 16 | mon cher baron | mon-cher-ba-ron | CLEAN | [private] |
| 17 | Monsieur le Baron | mon-sieur-le-Ba-ron | CLEAN | merges v2 duplicate "Monsieur le Baron," |
| 18 | Adieu, mon cher baron | a-dieu-mon-cher-ba-ron | LOW-MED | a\|di\|eu over-split [private] |
| 19 | Tout à vous | tout-à-vous | CLEAN | [private] |
| 20 | par le dernier courrier | par-le-der-nier-cour-rier | LOW-MED | **96=par KNOWN — sharp anchor**; cour\|ri\|er over-split |
| 21 | Sa Majesté Impériale | sa-Ma-jes-té-Im-pé-ria-le | HIGH | 8u, drag in halves; Inperiale by-ear [official] |
| 22 | le Roi | roi | SINGLE | 1 pair — confirmation-grade, not drag-grade |
| 23 | Saint-Pétersbourg | saint-Pé-ters-bourg | LOW-MED | Petersbourg/St-Pétersbourg variants |
| 24 | Londres | Lon-dres | CLEAN | |
| 25 | Paris | Pa-ris | CLEAN | |
| 26 | Berlin | Ber-lin | CLEAN | |
| 27 | Vienne | Vien-ne | CLEAN | |
| 28 | Dresde | Dres-de | CLEAN | |
| 29 | Recevez, Monsieur, l'assurance de ma considération distinguée | 15u | HIGH | drag in halves; top authority: Nesselrode's signed hand [official] |
| 30 | Agréez, Monsieur le Baron, l'assurance de ma haute considération | 15u | HIGH | drag #29's "considération distinguée" FIRST (grade note) [official] |
| 31 | le traité du 15 juillet | trai-té-du-quin-ze-juil-let | MEDIUM | 7u; "15" spelled "quinze" (chiffre risk); alt surface of #4 |

## Surviving P1 (54) — compact verdicts
**People (14, all PASS):** Palmerston · Thiers · Louis-Philippe · Brunnow · Ponsonby · Werther ·
Ibrahim (Damascus news verified, see above) · Meyendorff · le Sultan · le roi de Prusse (FW IV) ·
Liebermann · Espartero (regent since Oct 1840 — in the air Jan 1841, RdM 101×) ·
Le prince Jean de Saxe (Zeschau's close friend per ADB) · Le roi de Saxe (Friedrich August II).
**Places (14, all PASS):** la Syrie · l'Egypte · les Dardanelles · le Bosphore · Alexandrie ·
Damas (verified) · Gaza · Jaffa · le Danemark · le Schleswig / le Holstein · Francfort · la Saxe ·
la Sublime Porte (157× French-article, parliamentary-paper register).
**Titles/institutions (8, all PASS):** l'Empereur de Russie · le roi des Français ·
les cinq puissances · les puissances signataires · la cour · le cabinet ·
le ministre des affaires étrangères · la Diète / la Confédération germanique.
**Event vocabulary (19, all PASS):** l'hérédité · l'évacuation (de la Syrie — Metternich's hand) ·
le plénipotentiaire · les pleins-pouvoirs · la déclaration [v8 intro, editor voice] ·
les bâtiments de guerre [v8 intro] · toutes les nations [v8 intro] · l'acte final ·
le refus de Mehemet-Ali de l'accepter · la leçon donnée à la France [private register] ·
les lettres patentes du roi de Danemark · le maintien de la paix ·
La clôture des détroits (Metternich's second Straits formula) · Le Pachalik d'Egypte (Metternich) ·
Les fortifications de Paris (RdM Q1 31×; "observations adressées de Vienne et de Berlin" — live) ·
La soumission de Méhémet-Ali (levant-corr TOC; Nov–Dec 1840, known by 18 Jan) ·
Hâter la fin de la crise actuelle (Nesselrode's Levant note).
**Formulae (11, all PASS except kills noted):** J'ai reçu votre dépêche du … · En réponse à votre
dépêche du … · C'est là le but de ma dépêche (verbatim ministerial, 16 Dec 1840) ·
J'ai l'honneur, etc. (closing) · les hommages respectueux de votre très dévoué (closing) ·
unir … avec l'Angleterre entre dans nos vues (28 Dec 1840) · donner notre bénédiction à … [German-affairs] ·
sous l'impulsion de la Prusse · l'intéressante expédition ·
je n'ai … aucune autre observation ou information à ajouter ·
"J'ai l'honneur de transmettre à Votre Excellence" (Guizot form; envoy-grade "Excellence" OK for 1841) ·
"Monsieur le comte, les motifs que je vous exposais dans ma dépêche n° 7…" (title slot adapts to baron;
the numbered-dépêche shape is the crib).
**Background collocations (PASS):** jusqu'à présent · sans doute · sous ce rapport.

## Surviving P2 (32) — compact
People: Kisselef · Lieven · Cancrine · Bulow · Rochow · Apponyi · Sainte-Aulaire · Blome ·
Robert Peel (opposition leader Jan 1841) · Commodore Napier (levant-corr 216×; the Alexandria
convention, disavowed — live topic) · Elliot (opium-war thread; background only) · Soult ·
Molé · Lamennais · Lindenau (Zeschau's predecessor) · Don Carlos (Carlist aftermath, metternich v6 56×).
Places: Varsovie · la Grèce · Rome · Odessa · le Taurus · la Suède · Beyrouth ·
Saint-Jean-d'Acre · Canton · La Chine (background geography; no post-18-Jan news claimed).
Institutions: le grand-duc · le concert européen · Sa Hautesse (Sultan style, Nesselrode's Levant note).
Event vocab: la paix de l'Europe · la médiation · la neutralité · la garantie/les garanties ·
Des nouvelles d'Egypte de fraîche date (Metternich's phrase) · Les Représentans d'Autriche et de Prusse ·
Rétablir… la paix dans toute l'étendue de son Empire · Les avis bienveillans et désintéressés de ses Alliés.
Formulae: J'ai l'honneur de … (P2 upheld; Formula Tester H5 refutation stands — drag with care) ·
Je m'empresse de … · Permettez-moi de … · Agréez, &c. · A la première nouvelle que… (P2 upheld;
première-collision flagged) · agréez mes plus sincères … [familiar] · Dieu veuille que ….
Background vocabulary §H: PASS as drag filler, **minus standalone "premier" (struck — pre|m|i|er read)**.
KILLED: "Daignez, je vous prie…" and "Votre Excellence vient de m'adresser…" (direction reversal).

## Standing red-team notes for the main fleet
- The miner's v2 "top authority" claims check out where verifiable (Méhémet-Ali 293× exact;
  "la Sublime Porte" 157× French-article; AZ Damascus quote verbatim).
- Editor-voice caveat: the Straits-formula cribs from the v8 introduction ("les détroits",
  "la déclaration", "les bâtiments de guerre", "toutes les nations", "l'affaire d'Egypte")
  are the *editor's* summary French, not a correspondent's hand — still period French, but weight
  below Nesselrode's/Guizot's/Metternich's own words.
- No card in the list requires knowledge Dresden could not have by 18 Jan 1841, except the two
  killed direction-reversals and the already-removed Kossuth. Hong Kong/Chuenpi were never proposed.
