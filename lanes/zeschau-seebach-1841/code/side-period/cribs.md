# Seebach cipher lane — ranked crib list (PERIOD-SOURCES fleet, crib miner)
**Status: v2 + v3 delta** (v1 = Nesselrode *Lettres et papiers* v7–v10; v2 adds RdM 1841 Q1–Q4,
Guizot *Mémoires* t5–t6, Metternich *Papiere* v4+v6, Levant Correspondence 1841 P3,
AZ Augsburg 11-Jan-1841, ADB Zeschau, Pozzo di Borgo v1 — see v2 delta below;
v3 delta appends cards from Talleyrand v1, Guizot t1–t3, AZ 12–25 Jan-1841 — see v3 delta at end).
Miner: `code/side-period/miner.py` · syllabifier: `code/side-period/syllabify.py`
(heuristic; every card hand-checked). Durable mining output:
`code/side-period/work/mine-nesselrode/mine.json`,
`code/side-period/work/mine-rdm/mine.json`, `code/side-period/work/mine-v3/mine.json`.
Corpus: `code/side-period/corpus/`
(Nesselrode files renamed `nesselrode-v7..v10.txt`; v1 cards cite them as v7/v8/v9/v10).

## Cipher context (for the drag fleet)
R5005: 18 Jan 1841, Zeschau (Saxon foreign minister, Dresden) → Seebach (Saxon envoy,
St Petersburg). Two-digit French **syllabary**, 96 groups, 1,896 pairs.
Known values: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que, 87=ce, 64=qui,
96=par, 77=le. "La première" reads at pairs 754 and 1034 ("la première … que").
The encipherer cuts **finer than natural syllables** ("première" = pre|m|i|er) and
**spells by ear** with inconsistent cuts (personne/persone-style variants) —
so every card carries by-ear variants and alternative-cut notes.
Unassigned top groups by pair count: 06(49), 24(48), 00(46), 94(41), 98(38),
47(37), 62(37), 78(33), 67(33), 16(31), 42(30), 48(30), 21(28), 60(28) —
prime suspects for de / les / des / et / en / un / à / ne / se / re / on / tion…

## Rank key
- **P0** — name/date/formula highly likely in a mid-Jan-1841 Zeschau despatch to St Petersburg.
- **P1** — plausible (named in the period corpus, topic-adjacent).
- **P2** — background chancellery vocabulary.
- Red Team owns anachronism review; nothing proposed here is visibly post-1841.

## TOP-15 cribs (drag these first)
1. **Nesselrode** (P0 name) — Russian chancellor AND Seebach's father-in-law; 1,474× in corpus. nes-sel-ro-de; by-ear: Neselrode, Nesselrod.
2. **l'Empereur / Sa Majesté Impériale** (P0 title) — Nicholas I; "l'empereur" 754×. em-pe-reur; by-ear: anpereur, l'Empereur.
3. **Constantinople** (P0 place) — Levant crisis hub; 80× in v8 alone. cons-tan-ti-no-ple.
4. **le traité de Londres** (P0 collocation) — the operative 15-Jul-1840 treaty; 8× in v8. trai-té-de-Lon-dres.
5. **la question orientale / l'affaire d'Orient** (P0 collocation) — the frame of the whole despatch. ques-tion-o-rien-tale.
6. **Mehemet-Ali** (P0 name) — "le vice-roi d'Egypte"; firman of investiture due Feb 1841. me-he-met-A-li; by-ear: Mehmet-Ali, Méhémet-Ali, Mehmed-Ali.
7. **le firman** (P0 collocation) — "Le firman et le refus de Mehemet-Ali de l'accepter"; "l'affaire du firman". fir-man; by-ear: firmanne.
8. **la Porte** (P0 institution) — "La Porte modifiera son firman"; 80× in v8. por-te.
9. **les détroits / les Dardanelles** (P0 place/collocation) — Straits settlement under negotiation; "les détroits restent fermés aux bâtiments de guerre de toutes les nations". dé-troits / dar-da-nel-les; by-ear: destroits.
10. **la convention orientale** (P0 collocation) — "les pleins-pouvoirs pour signer la convention orientale" (the coming Straits Convention). con-ven-tion-o-rien-tale.
11. **Guizot** (P0 name) — French foreign minister since Oct 1840; 57× in v8. gui-zot; by-ear: Guizo, Guisot.
12. **Metternich** (P0 name) — Austrian chancellor, co-manager of the crisis; 61× in v8. met-ter-nich; by-ear: Meternich, Metternik.
13. **Votre dépêche du …** (P0 formula) — the standard despatch-reference opener. vo-tre-dé-pê-che-du.
14. **mon cher baron / Monsieur le Baron** (P0 formula) — Seebach was a baron in 1841; "mon cher baron" trigram 178× in corpus. mon-cher-ba-ron; by-ear: baron stable.
15. **Adieu, mon cher baron / Tout à vous** (P0 formula) — the two standard closings, dozens of attestations each. a-dieu-mon-cher-ba-ron / tout-à-vous.

---

## A. People (proper names)
| rank | crib | source | rationale | syllabification | by-ear variants |
|---|---|---|---|---|---|
| P0 | Nesselrode | v7/v8/v9/v10 (1,474×) | Russian chancellor; Seebach's father-in-law — personal + official register both demand the name | nes-sel-ro-de | Neselrode, Nesselrod |
| P0 | Guizot | v8 (57×) | French foreign minister Oct 1840–; "l'attitude de Guizot"; "faire asseoir M. Guizot à la table ronde" | gui-zot | Guizo, Guisot |
| P0 | Metternich | v8 (61×) | Austrian chancellor; "les longues dépêches de Metternich au comte Apponyi" | met-ter-nich | Meternich, Metternik |
| P0 | Mehemet-Ali | v8 (Mehemet 21×, Ali 23×) | "le vice-roi d'Egypte, Mehemet-Ali"; his submission + firman is the live crisis | me-he-met-A-li | Mehmet-Ali, Méhémet-Ali, Mehmed-Ali, Mehmet Ali |
| P1 | Palmerston | v8 (43×) | British foreign secretary; "la politique de lord Palmerston" | pal-mer-ston | Palmerstonne |
| P1 | Thiers | v8 (52×) | ex-premier (fell Oct 1840); "les manœuvres de Thiers" | thiers (1 unit) | Tier, Tièr |
| P1 | Louis-Philippe | v8 (49× "Louis Philippe") | "une entrevue avec Louis-Philippe"; "le roi des Français" | lou-is-Phi-lip-pe | Loui-Filippe, Louis Philippe |
| P1 | Brunnow | v8 (60×) | Russian ambassador in London; carries the pleins-pouvoirs for the convention | brun-nov | Brunnov, Bruno |
| P1 | Ponsonby | v8 (4×) | British ambassador at the Porte; "les nouvelles instructions données à Ponsonby"; "Lord Ponsonby sera le seul à n'être pas d'accord avec nous" | pon-son-by | Ponsonbi |
| P1 | Werther | v8 (28×) | Prussian ambassador in Paris; "notre bon Werther se sera réconcilié avec le traité de Londres" | wer-ther | Werther stable |
| P1 | Ibrahim | v8 (4×) | Mehemet-Ali's son/general; "les forces d'Ibrahim"; Syria evacuation | i-bra-him | Ibraim |
| P1 | Meyendorff | v8 (78×) | Russian ambassador in Berlin; Nesselrode's main correspondent (v8 core) | mey-en-dorff | Meiendorf, Meyendorf |
| P1 | le Sultan | v8 (36× "Sultan") | "le sultan avait refusé l'hérédité"; the Porte's master | sul-tan | Soultan |
| P1 | le roi de Prusse | v8 (16×) | Friedrich Wilhelm IV; "le roi de Prusse irait en Angleterre" | roi-de-Prus-se | le roi de Pruse |
| P1 | Liebermann | v8 (29×) | Prussian envoy at St Petersburg; Zollverein dépêche reader | lie-ber-mann | Libermann |
| P2 | Espartero | sources.md seed | Spanish regent — "in the air" Jan 1841; not yet mined in corpus | es-par-te-ro | Espartero |
| P2 | Kisselef | v8 (27×) | Russian diplomat (Paris) | kis-se-lef | Kisseleff |
| P2 | Lieven | v8 (23×) | Princess Lieven, London circle | lie-ven | Liéven |
| P2 | Cancrine | v8 (22×) | Russian finance minister | can-cri-ne | Cancrin |
| P2 | Bulow | v8 (21×) | Prussian diplomat | bu-lov | Bulov, Bülow |
| P2 | Rochow | v8 (21×) | Prussian diplomat | ro-chov | Rochov |
| P2 | Apponyi | v8 (5×) | Austrian ambassador in Paris; Metternich's dépêche channel | a-ppo-nyi | Apponi |
| P2 | Sainte-Aulaire | v8 (1×) | French ambassador in Vienna ("fait partir subitement M. de Sainte-Aulaire pour Vienne") | sain-te-Au-lai-re | Saint-Aulaire |
| P2 | Blome | v8 (comte Blome) | "ancien ministre de Danemark à Pétersbourg" — Danish-patents thread | blo-me | Blom |

Note: **Seebach** (the recipient, "le baron de Seebach" per v9) is NOT proposed as a
plaintext crib — a minister does not name his addressee mid-despatch. **Zeschau**
(self, 0 hits in corpus) likewise excluded.

## B. Places
| rank | crib | source | rationale | syllabification | by-ear variants |
|---|---|---|---|---|---|
| P0 | Constantinople | v8 (31×; 80 incl. variants) | crisis hub; "défense de Constantinople"; Ibrahim's target | cons-tan-ti-no-ple | Constantinople stable |
| P0 | Saint-Pétersbourg | v8 (158×) | Seebach's posting; letter dateline form | saint-Pé-ters-bourg | Petersbourg, St-Pétersbourg, Saint-Petersbourg |
| P0 | Londres | v8 (82×) | "la nouvelle que le roi de Prusse irait en Angleterre"; treaty/conference city | Lon-dres | Londre |
| P0 | Paris | v8 (91×) | Guizot's capital; French resentment theater | Pa-ris | Paris stable |
| P0 | Berlin | v8 (117×) | Prussian capital; "unir les deux grandes cours allemandes avec l'Angleterre" | Ber-lin | Berlin stable |
| P0 | Vienne | v8 (69×) | Metternich's capital | Vien-ne | Vienne stable |
| P0 | Dresde | v8 (5×) | Zeschau's own capital; "J'ai été témoin, à Dresde, d'une espèce de congrès" (6 Sep 1840) | Dres-de | Dresd |
| P1 | la Syrie | v8 (22×) | "retirer ses forces de la Syrie" — the evacuation theater, Jan–Feb 1841 | Sy-rie | Sirie; cut sy-ri-e? |
| P1 | l'Egypte | v8 (topic) | "l'affaire d'Egypte est terminée"; "la révolte du vice-roi d'Egypte" | E-gyp-te | Ejipte, Égipte |
| P1 | les Dardanelles | v8 (3×) | Straits; "le blocus des Dardanelles" | dar-da-nel-les | Dardanelles stable |
| P1 | le Bosphore | v8 (1×) | Straits pair of Dardanelles | Bos-pho-re | Bosfore |
| P1 | Alexandrie | v8 (3×) | "la dernière dépêche que j'ai reçue d'Alexandrie"; "bombarder Alexandrie" | a-le-xan-drie | Alexandrie stable |
| P1 | le Danemark | v8 (9×) | Sound tolls + "les lettres patentes du roi de Danemark" — live Jan-1841 thread for a German minister | Da-ne-mark | Dannemark |
| P1 | le Schleswig / le Holstein | v8 (3×/6×) | "parfaitement dans son droit quant au Schleswig" — the Danish-patents substance | Schles-wig / Hol-stein | Slesvig, Sleswick |
| P1 | Francfort | v8 (3×) | Federal Diet seat | Franc-fort | Francfort stable |
| P1 | la Saxe | v8 (2×) | Zeschau's own state (rare in Nesselrode, but a Saxon minister names his master) | Sa-xe | Saxe stable |
| P2 | Varsovie | v8 (22×) | Polish theater; "aller par Varsovie et Dresde" | Var-so-vie | Varsovie stable |
| P2 | la Grèce | v8 (28×) | background Levant geography | Grè-ce | Grece |
| P2 | Rome | v8 (23×) | diplomatic geography | Ro-me | Rome stable |
| P2 | Odessa | v8 | "un mot au préfet d'Odessa" | O-des-sa | Odessa stable |
| P2 | le Taurus | v8 (1×) | "Ibrahim ne passera pas le Taurus" | Tau-rus | Taurus stable |
| P2 | la Suède | v8 (3×) | northern geography | Su-è-de | Suede |

## C. Titles, institutions, collective nouns
| rank | crib | source | rationale | syllabification | by-ear variants |
|---|---|---|---|---|---|
| P0 | l'Empereur | all vols (754× "l'empereur") | Nicholas I in a St-Petersburg despatch; "l'Empereur de Russie" 6× | em-pe-reur | anpereur, l'Empereur |
| P0 | Sa Majesté Impériale | v8 (6× "sa majesté…") | formal style; "j'ai l'honneur de faire à Sa Majesté Impériale la communication…" | sa-Ma-jes-té-Im-pé-ria-le | sa Majesté Inperiale |
| P0 | la Porte | v8 (80× "Porte"; 18× "la porte") | the Ottoman government as actor; "La Porte modifiera son firman" | por-te | Porte stable |
| P0 | le Roi | v8 (132×) | generic sovereign reference; "S. M. le Roi" | roi | roi stable |
| P1 | l'Empereur de Russie | v8 (6×) | disambiguating title | em-pe-reur-de-Rus-sie | — |
| P1 | le roi des Français | v8 (1×) | Louis-Philippe's style; "tout amoureux du roi des Français" | roi-des-Fran-çais | le roi des Francais |
| P1 | les cinq puissances | v8 (2×) | the Concert; "une déclaration que la Porte adresserait aux cinq puissances" | cinq-puis-san-ces | sinque puisances |
| P1 | les puissances signataires | v8 (traité de Londres ctx) | "proposer aux puissances signataires du traité de Londres un traité d'alliance…" | puis-san-ces-si-gna-tai-res | — |
| P1 | la cour | v8 ("cour de Berlin", "cour de Vienne") | "unir les deux grandes cours allemandes avec l'Angleterre" | cour | court |
| P1 | le cabinet | v8 (6× "cabinet de") | "le cabinet de …" ministry metonym | ca-bi-net | cabine |
| P1 | le ministre des affaires étrangères | v8 (13× "ministre des affaires"; trigram 33×) | office vocabulary | mi-nis-tre-des-af-fai-res-é-tran-gè-res | — |
| P1 | la Diète / la Confédération germanique | v8 (3×/5×) | German Confederation business — squarely a Saxon minister's lane | Di-è-te / Con-fé-dé-ra-tion-ger-ma-ni-que | Diete |
| P2 | le grand-duc | v8 (29×) | German princely vocabulary | grand-duc | grand duc |
| P2 | le concert européen | v8 (1×) | Concert-of-Europe vocabulary | con-cert-eu-ro-pé-en | — |
| P2 | la Sublime Porte | — (style) | formal variant of la Porte (not attested in v8; keep P2) | su-bli-me-Por-te | — |

## D. Levant / Straits event vocabulary (the despatch's likely substance)
| rank | crib | source | rationale | syllabification | by-ear variants |
|---|---|---|---|---|---|
| P0 | le traité de Londres | v8 (8×) | THE treaty; "exécuter le traité de Londres"; "réconcilié avec le traité de Londres" | trai-té-de-Lon-dres | le traité de Londre |
| P0 | la question orientale | v8 (2×) | "sur la question orientale. Nous sommes à attendre l'effet qu'aura produit…" | ques-tion-o-rien-tale | — |
| P0 | l'affaire d'Orient | v8 (2×) | "l'état actuel de l'affaire d'Orient"; "une nouvelle perturbation dans l'affaire d'Orient" | af-fai-re-d'O-rient | — |
| P0 | l'affaire d'Egypte | v8 intro (1×) | "l'affaire d'Egypte est terminée" | af-fai-re-d'E-gyp-te | — |
| P0 | le firman | v8 (4×) | "Le firman et le refus de Mehemet-Ali de l'accepter"; "l'affaire du firman"; investiture firman due Feb 1841 | fir-man | firmanne |
| P0 | les détroits | v8 (1×, intro) | "les détroits restent fermés aux bâtiments de guerre de toutes les nations" — the Straits formula | dé-troits | destroits |
| P0 | la convention orientale | v8 (1×) | "les pleins-pouvoirs pour signer la convention orientale" | con-ven-tion-o-rien-tale | convension |
| P1 | l'hérédité | v8 (7× "heredite") | "le sultan avait refusé l'hérédité"; the firman's substance (hereditary Egypt) | hé-ré-di-té | heredité, eredité |
| P1 | l'évacuation | v8 (1×) | "l'évacuation des Français" (form model); Jan–Feb 1841 = evacuation of Syria | é-va-cua-tion | evacuation, évacuasion |
| P1 | le plénipotentiaire | v8 (many) | "envoyer un plénipotentiaire à Constantinople"; "ministre plénipotentiaire" | plé-ni-po-ten-tiai-re | plénipotensiaire |
| P1 | les pleins-pouvoirs | v8 (2×) | "les pleins-pouvoirs pour signer la convention orientale" | pleins-pou-voirs | — |
| P1 | la déclaration | v8 intro | "une déclaration que la Porte adresserait aux cinq puissances" | dé-cla-ra-tion | declarasion |
| P1 | les bâtiments de guerre | v8 intro | "…fermés aux bâtiments de guerre de toutes les nations" | bâ-ti-ments-de-guer-re | batiments |
| P1 | toutes les nations | v8 intro | tail of the Straits formula | tou-tes-les-na-tions | — |
| P1 | l'acte final | v8 | "la France signera l'acte final plus tard" | ac-te-fi-nal | — |
| P1 | le refus de Mehemet-Ali de l'accepter | v8 | "Le firman et le refus de Mehemet-Ali de l'accepter vont jeter une nouvelle perturbation…" | re-fus-de-me-he-met-A-li-de-l'ac-cep-ter | — |
| P1 | la leçon donnée à la France | v8 (16 Dec 1840 letter) | "la leçon que nous avons donnée à la France a été bonne" — the 1840 humiliation, still live | le-çon-don-née-à-la-Fran-ce | — |
| P1 | les lettres patentes du roi de Danemark | v8 (2×) | "Notre opinion est qu'il est parfaitement dans son droit quant au Schleswig" | let-tres-pa-ten-tes-du-roi-de-Da-ne-mark | — |
| P1 | le maintien de la paix | v8 (2×) | Concert vocabulary | main-tien-de-la-paix | — |
| P2 | la paix de l'Europe | style | Concert vocabulary (model) | paix-de-l'Eu-ro-pe | pai |
| P2 | la médiation | style | crisis vocabulary | mé-dia-tion | mediation |
| P2 | la neutralité | style | crisis vocabulary | neu-tra-li-té | neutralité |
| P2 | la garantie / les garanties | style | treaty vocabulary | ga-ran-tie | garantee |

iation |
| P2 | la neutralité | style | crisis vocabulary | neu-tra-li-té | neutralité |
| P2 | la garantie / les garanties | style | treaty vocabulary | ga-ran-tie | garantee |

## E. Formulae — salutations & openings
| rank | crib | source | rationale | syllabification | by-ear variants |
|---|---|---|---|---|---|
| P0 | mon cher baron | corpus (trigram 178× "mon cher baron"; 324× "cher baron") | Nesselrode→Meyendorff standard; Seebach was a baron — Zeschau's most likely salutation shape | mon-cher-ba-ron | — |
| P0 | Monsieur le Baron | v8 ("monsieur le…" pattern; address register) | formal address variant for an envoy | mon-sieur-le-Ba-ron | — |
| P0 | Votre dépêche du … | v8 | "Votre dépêche du 17 octobre"; "votre dépêche du 5 août 1835" — the despatch-reference opener | vo-tre-dé-pê-che-du | depeche, dépèche |
| P1 | J'ai reçu votre dépêche du … | v8 (12× "j'ai reçu") | "j'ai reçu avant-hier l'intéressante expédition…"; "j'ai reçu par la poste votre dépêche du 1er mai" | j'ai-re-çu-vo-tre-dé-pê-che-du | — |
| P1 | En réponse à votre dépêche du … | v8 (6×) | "en réponse à votre lettre du 8 février"; "en réponse à votre dépêche du 17 octobre" | en-ré-pon-se-à-vo-tre-dé-pê-che-du | — |
| P1 | mon cher comte | corpus (trigram 53×) | alternative salutation shape (if Zeschau writes familiarly) | mon-cher-com-te | — |
| P1 | mon cher ami | corpus (trigram 27×) | familiar salutation shape | mon-cher-a-mi | — |
| P1 | C'est là le but de ma dépêche | v8 (16 Dec 1840, Nesselrode→Meyendorff) | "C'est là le but de ma dépêche, à laquelle je n'ai, pour le moment, aucune autre observation ou information à ajouter" — purpose formula, verbatim ministerial | c'est-là-le-but-de-ma-dé-pê-che | — |
| P2 | J'ai l'honneur de … | v8 (13× "honneur" incl. "j'ai l'honneur de faire à Sa Majesté Impériale la communication…") | attested as despatch-opening verb, though the crowd's Formula Tester refuted one specific H5 form — drag with care | j'ai-l'hon-neur-de | j'ai l'honneur, onneur |
| P2 | Je m'empresse de … | style | chancellery eagerness formula | je-m'em-pres-se-de | — |
| P2 | Permettez-moi de … | style | permission formula | per-met-tez-moi-de | — |

## F. Formulae — closings
| rank | crib | source | rationale | syllabification | by-ear variants |
|---|---|---|---|---|---|
| P0 | Adieu, mon cher baron | v8 (dozens) | "Adieu, mon cher Meyendorff"; "Adieu, mon très cher baron" — the Nesselrode closing par excellence | a-dieu-mon-cher-ba-ron | — |
| P0 | Tout à vous | v8 (dozens) | the short closing, alternating with Adieu | tout-à-vous | — |
| P1 | J'ai l'honneur, etc. | v8 (1×: "J'ai l'honneur, etc. Le comte Charles de Nesselrode au baron…") | formal closing, attested verbatim | j'ai-l'hon-neur-etc | — |
| P1 | les hommages respectueux de votre très dévoué | v8 | "…ges respectueux de votre très dévoué" — formal ministerial closing | hom-ma-ges-res-pec-tueux-de-vo-tre-très-dé-voué | — |
| P2 | agréez mes plus sincères … | v8 (6× "agréez") | "agréez mes plus sincères et invariables amitiés" (familiar register) | a-gré-ez-mes-plus-sin-cè-res | agréé |
| P2 | Dieu veuille que … | v8 (48× "dieu veuille") | wish formula: "Adieu, mon cher Meyendorff, Dieu veuille que…" | Dieu- veuil-le-que | — |

## G. Diplomatic set phrases & collocations (discourse-level — the Formula Hunter's repeat class)
| rank | crib | source | rationale | syllabification | by-ear variants |
|---|---|---|---|---|---|
| P0 | par le dernier courrier | v8 | "Par le dernier courrier que j'ai…" (firman context) — courier-reference collocation | par-le-der-nier-cour-rier | — |
| P1 | unir … avec l'Angleterre entre dans nos vues | v8 (28 Dec 1840) | "tout ce qui peut servir à unir les deux grandes cours allemandes avec l'Angleterre entre dans nos vues" — policy-intent shape | u-nir…a-vec-l'An-gle-ter-re-en-tre-dans-nos-vues | Angletairre |
| P1 | donner notre bénédiction à … | v8 (16 Dec 1840) | "Nous n'avons qu'à donner notre bénédiction à tout ce qui a été fait en Allemagne sous l'impulsion de la Prusse" | don-ner-no-tre-bé-né-dic-tion-à | benedicsion |
| P1 | sous l'impulsion de la Prusse | v8 (16 Dec 1840) | tail of the above; German-affairs vocabulary | sous-l'im-pul-sion-de-la-Prus-se | inpulsion |
| P1 | l'intéressante expédition | v8 | "j'ai reçu avant-hier l'intéressante expédition que vous m'a[vez adressée]" — chancellery word for a despatch | in-té-res-san-te-ex-pé-di-tion | expedision |
| P1 | je n'ai … aucune autre observation ou information à ajouter | v8 (16 Dec 1840) | tail of the purpose formula | je-n'ai-au-cu-ne-au-tre-ob-ser-va-tion-ou-in-for-ma-tion-à-a-jou-ter | observasion |
| P1 | jusqu'à présent | corpus (51×) | "jusqu'à présent" — time collocation | jus-qu'à-pré-sent | — |
| P1 | sans doute | corpus (48×) | modal collocation | sans-dou-te | — |
| P1 | sous ce rapport | corpus (39×) | "Sous ce rapport la dernière expédition de Brunnow…" — argumentative hinge | sous-ce-rap-port | raport |
| P2 | prendre connaissance | style | "prendre connaissance de…" | pren-dre-con-nais-san-ce | conaissance |
| P2 | porter à la connaissance | style | notification formula | por-ter-à-la-con-nais-san-ce | — |
| P2 | rendre compte | style | reporting formula | ren-dre-comp-te | — |
| P2 | faire part | style | "faire part de…" | fai-re-part | — |
| P2 | à l'égard de | style | "à l'égard de…" | à-l'é-gard-de | egard |

## H. Chancellery background vocabulary (P2 — drag filler, frequency-ranked)
courrier (69× v8) · dépêche (116× v8) · expédition (47× v8) · lettre (427×) ·
rapport · affaires (308×) · cabinet · ministre (302×) · conseil · instructions ·
note · protocole · ratification · signature (si-gna-tu-re) · ordre · pouvoir(s) ·
pleins-pouvoirs · médiation · intervention · neutralité · garanties ·
fois ("la première fois que" — adjacent to the known "la première … que" read) ·
jour(s) · semaine · mois · année · aujourd'hui · hier · avant-hier · demain ·
nouvelle(s) ("j'ai reçu de Londres la nouvelle que…") · bruit · avis · réponse ·
question (298×) · affaire(s) · objet · sujet · circonstance(s) · événement(s) ·
situation · état · disposition(s) · intention(s) · désir · vœu · crainte(s) ·
espérance · assurance(s) · certitude · doute · peine · satisfaction ·
grand · petit · nouveau · dernier · premier · seul · même · tout · chaque ·
beaucoup · peu · très · plus · moins · encore · déjà · toujours · jamais ·
être · avoir · faire · dire · voir · savoir · croire · penser · espérer ·
vouloir · pouvoir · devoir · falloir.

---

## High-value surprises (for the coordinator)
1. **A letter dated "Paris, 18 janvier 1841" exists in v8** — same calendar day as
   R5005. It is the Countess Nesselrode's social letter (Paris fortifications debate,
   Soult, Lamennais ovation) — low topical value, but the date coincidence is worth
   one line in the report.
2. **The Straits formula verbatim**: "…une déclaration que la Porte adresserait aux
   cinq puissances pour leur notifier que l'affaire d'Egypte est terminée et que les
   détroits restent fermés aux bâtiments de guerre de toutes les nations" (v8
   introduction, editor's summary of Nesselrode's late-1840 position — editor voice,
   not Nesselrode's hand; cribs from it marked accordingly).
3. **"les pleins-pouvoirs pour signer la convention orientale"** — Nesselrode's own
   words re: Brunnow (v8). The coming Straits Convention named in-chancellery.
4. **The Danish-patents / Schleswig thread** (Dec 1840 letters): "les lettres patentes
   du roi de Danemark… il est parfaitement dans son droit quant au Schleswig" —
   a live German-question topic a Saxon minister would plausibly relay.
5. **Zollverein refusal vocabulary**: "J'ai fait la sourde oreille et j'ai refusé net";
   "pourquoi faire la moindre chose pour le Zollverein qui ne fait rien pour nous" —
   Zeschau's other portfolio was trade; usable if the despatch touches economics.
6. **"J'ai été témoin, à Dresde, d'une espèce de congrès"** (6 Sep 1840) — Dresden as
   congress city; Seebach-route vocabulary ("par Varsovie et Dresde").
7. **Seebach is IN the corpus**: v9 "M. de Seebach qui me remit votre lettre" (1848);
   v9 "le baron de Seebach" (Chreptowich's brother-in-law — Albin Leo himself);
   index entries "Seebach (comte), 279 — (comtesse Marie), 295". Confirms the
   "baron" address form for 1841. Zeschau: 0 hits (expected — Saxon, not Russian circle).

## Fleet notes
- The corpus's dominant register is **confidential minister-to-ambassador French**
  (Nesselrode→Meyendorff, Berlin, 1840–46) — the closest surviving analogue of a
  Zeschau→Seebach despatch. Formula cards from v8 carry the most weight.
- **Anti-collision**: do not re-propose "première" (already read at 754/1034); the
  known syllables la/pre/m/i/er/e/que/ce/qui/par/le constrain adjacent cribs.
- **Cut model**: expect finer-than-natural cuts (pre|m|i|er) and single-letter units;
  when a crib drag fails at natural syllabification, retry with fused/split variants
  (e.g. "Syrie" → sy|rie vs sy|ri|e; "Constantinople" → cons|tan|ti|no|ple vs
  con|stan|ti|no|ple).
- v7 (1828–39) and v9/v10 (1847–56) were mined for register continuity only; v8
  (1840–46) is the dated anchor. RdM 1841 (v2) adds exact-year Parisian vocabulary.
- miner.py is idempotent: re-run on corpus/ after Harvester drops any new files;
  promote to v3 and note the delta here.

---

## v2 delta (2026-10-07, crib miner) — Harvester drops mined
New corpus since v1: `revue-deux-mondes-1841-q1..q4.txt` (RdM, Parisian quarterly,
12 MB), `guizot-memoires-t5-t6.txt` (Guizot, 2 MB — prints his despatches
**verbatim** with full official formulae), `metternich-papiere-v4.txt` /
`-v6.txt` (3.2 MB, German + embedded French despatches), `levant-correspondence-1841-p3.txt`
(British parliamentary paper, Jan–Feb 1841 Levant despatches, 1.7 MB, English +
French originals), `allgemeine-zeitung-augsburg-1841-01-11.txt` (124 KB, the
Saxon minister's own daily, dated **7 days before R5005**), `adb-zeschau-heinrich-anton-von.txt`
(Zeschau ADB biography), `pozzo-di-borgo-correspondance-v1.txt` (register only,
1814–18). Nesselrode files renamed `nesselrode-v7/v8/v9/v10.txt` (same bytes).
Durable mining output: `code/side-period/work/mine-nesselrode/mine.json`,
`code/side-period/work/mine-rdm/mine.json` (re-run in progress at write time).

### v2 promotions (new P0s)
| rank | crib | source | rationale | syllabification | by-ear variants |
|---|---|---|---|---|---|
| P0 | Recevez, Monsieur, l'assurance de ma considération distinguée | levant-corr P3 (French original, **signed NESSELRODE**, St-Pétersbourg, late 1840, Levant circular) | Nesselrode's OWN official closing — the register Zeschau writes in; Seebach serves in Nesselrode's ministry | re-ce-vez-mon-sieur-l'as-su-ran-ce-de-ma-con-si-dé-ra-tion-dis-tin-guée | — |
| P0 | Agréez, Monsieur le Baron, l'assurance de ma haute considération | guizot t5–t6 (multiple: "Recevez, monsieur l'ambassadeur, l'assurance de ma haute considération"; "l'assurance de sa plus haute considération" (Nouri note); "l'assurance de ma haute considération" (Rechid)) | the official French chancellery closing, multiply attested on 1840–41 instruments | a-gré-ez-mon-sieur-le-Ba-ron-l'as-su-ran-ce-de-ma-hau-te-con-si-dé-ra-tion | agréé |
| P0 | le traité du 15 juillet | RdM (156× across 1841: "15 juillet" 38/21/41/56 per quarter); metternich v6 ("une Convention avait été signée à Londres le 15 Juillet dernier") | the RdM house name for the London treaty — alternative surface form of P0 "traité de Londres" | trai-té-du-quin-ze-juil-let | le traité du 15 juillet |
| P0 | Monsieur le Baron, | levant-corr P3 French original ("Monsieur le Baron, St. Pétersbourg, le … 1840. A la première nouvelle que…"); guizot t5–t6 ("Monsieur le baron, « Je vous envoie le compte-rendu de l'entretien…") | official opening address to a baron — Seebach's rank | mon-sieur-le-Ba-ron | — |

### v2 new cards
**People.** Espartero P1 (RdM 101×; "jouer le rôle d'Espartero"; Spanish regency — in the air Jan 1841; es-par-te-ro). Robert Peel P2 (RdM bigram "robert peel" 134×; opposition leader Jan 1841; ro-bert-peel). Commodore Napier P2 (levant-corr 216×; "Commodore Napier's conditions" accepted by Mehemet Ali; na-pier). Elliot P2 (RdM 45×; Capt. Charles Elliot, British superintendent in China — opium-war thread; el-liot). Soult P2 (RdM 58×; "le maréchal Soult, qui ne veut pas soutenir la loi" — fortifications debate; soult). Molé P2 (RdM 73×; mo-lé). Lamennais P2 (RdM 96×; la-men-nais). **Le prince Jean de Saxe P1** (ADB Zeschau: "l'enge persönliche Freundschaft Zeschau's mit dem… Prinzen, nachherigen König Johann" — Zeschau's close friend, later King Johann of Saxony; prince-Jean-de-Sa-xe). Lindenau P2 (ADB: Zeschau's predecessor; lin-de-nau). Le roi de Saxe P1 (Friedrich August II, Zeschau's master; roi-de-Sa-xe).
**Mehemet-Ali spelling correction (v1 card amended):** attested house forms are **"Méhémet-Ali"** (RdM, 293×, accented + hyphenated) and **"Mehemet-Ali"** (Nesselrode); German form **"Mehemed Ali"** (AZ 11-Jan-1841, 8×) is a live by-ear variant; metternich v6 OCR shows "Me'he'met-Ali". By-ear: Mehmet-Ali, Mehmed-Ali.
**Places.** Damas P1 (AZ 11-Jan-1841: "Ibrahim Pascha… noch zu Damaskus" 13 Dec 1840 — French "Damas"; da-mas). Gaza P1 (levant-corr 240× — evacuation route; ga-za). Jaffa P1 (levant-corr 126×; jaf-fa). Beyrouth P2 (levant-corr 147×; bey-routh). Saint-Jean-d'Acre P2 (levant-corr "Acre" 188×; saint-jean-d'a-cre). Canton P2 (RdM 207×; can-ton). La Chine P2 (RdM "Chine" 111×; chi-ne).
**Titles/institutions.** La Sublime Porte P1 (levant-corr "Sublime" 626× — the English papers' form; French "la Sublime Porte"; su-bli-me-por-te). Sa Hautesse P2 (Nesselrode's Levant note: "Sa Hautesse s'empressera de suivre les avis… de ses Alliés" — Sultan style; sa-hau-tes-se).
**Event vocabulary.** Les fortifications de Paris P1 (RdM Q1 31×: "la Chambre nomme une commission qui vote à l'unanimité pour les fortifications de Paris, et qui choisit M. Thiers pour président et pour rapporteur"; "les observations adressées de Vienne et de Berlin" — for-ti-fi-ca-tions-de-pa-ris). La clôture des détroits P1 (metternich v6: "l'acte relatif à la clôture des détroits" — second Straits formula; clô-tu-re-des-dé-troits). Le Pachalik d'Egypte P1 (metternich v6: "l'offre de l'hérédité dans le Pachalik d'Egypte"; pa-cha-lik-d'é-gyp-te). L'évacuation (de la Syrie) P1 — now with Metternich's hand: "je n'ai rien dit au sujet de l'évacuation, ni à M. le Comte de Sainte-Aulaire ni à personne autre" (é-va-cua-tion). La soumission de Méhémet-Ali P1 (levant-corr TOC: "Mehemet Ali submits…"; sou-mis-sion). Des nouvelles d'Egypte de fraîche date P2 (metternich v6: "J'ai des nouvelles d'Egypte de fraîche date"; nou-vel-les-d'é-gyp-te-de-fraî-che-da-te). Hâter la fin de la crise actuelle P1 (Nesselrode's Levant note; hâ-ter-la-fin-de-la-cri-se-ac-tu-el-le). Les Représentans d'Autriche et de Prusse P2 (same note; re-pré-sen-tans-d'au-tri-che-et-de-prus-se). Rétablir… la paix dans toute l'étendue de son Empire P2 (same note). Les avis bienveillans et désintéressés de ses Alliés P2 (same note).
**Formulae (official register — Guizot t5–t6).** "J'ai l'honneur de transmettre à Votre Excellence" P1 (j'ai-l'hon-neur-de-trans-met-tre-à-vo-tre-ex-cel-len-ce). "J'ai l'honneur de vous remettre" P1. "Monsieur le comte, les motifs que je vous exposais dans ma dépêche n° 7 du 1er de ce mois" P1 — numbered-dépêche reference shape (mon-sieur-le-com-te-les-mo-tifs-que-je-vous-ex-po-sais-dans-ma-dé-pê-che-nu-mé-ro). "Daignez, je vous prie, m'indiquer la conduite que je dois suivre" P2 (dai-gnez-je-vous-prie-m'in-di-quer-la-con-dui-te-que-je-dois-sui-vre). "Le soussigné, ambassadeur extraordinaire et plénipotentiaire de S. M.…" P2 — note-verbale form (le-sou-ssi-gné-am-bas-sa-deur-ex-traor-di-nai-re-et-plé-ni-po-ten-tiai-re). "Votre Excellence vient de m'adresser…" P2. "Agréez, &c." P2 (levant-corr French originals: "Agréez, &c., (Signé) M. LAURIN"; "Agréez, &c., (Signé) A. STEINDL"). "A la première nouvelle que…" P2 (levant-corr: "Monsieur le Baron, St. Pétersbourg… A LA premiére nouvelle que" — note: "première" collides with the known read; drag with care).
**German/Danish thread (AZ + metternich):** "Die Pforte nimmt in der Entscheidung über Mehemed Ali ein unbeschränktes Verfügungsrecht in Anspruch" (AZ 11-Jan-1841 — the Porte's claim over the firman terms; French crib model: "un droit de disposition illimité"). Don Carlos P2 (metternich v6 56× — Carlist aftermath still discussed; car-los).

### v2 surprises
1. **Nesselrode's signed closing** ("Recevez, Monsieur, l'assurance de ma considération distinguée") — the single most authoritative formula in the corpus: his hand, his signature, Levant subject, late 1840.
2. **Guizot t5–t6 print official despatches verbatim** — the official-register formulae ("Monsieur le comte/baron", "j'ai l'honneur de transmettre à Votre Excellence", "l'assurance de ma haute considération") that Nesselrode's private letters lack. The two registers are now separated: private (Adieu/Tout à vous) vs official (assurance-formulae).
3. **"le traité du 15 juillet"** is the RdM house name (156×) — the drag fleet should try both surfaces.
4. **AZ 11-Jan-1841** (7 days before R5005): Ibrahim still at Damascus 13 Dec; Porte claims "unbeschränktes Verfügungsrecht" over Mehemed Ali — the exact news Zeschau had when writing.
5. **ADB Zeschau**: finance/Zollverein man (signed the 30-Mar-1833 Zollverein treaty himself; ex-Bundestagsgesandter 1829) — trade/economic vocabulary is in-character; Prince Johann of Saxony is his close friend (new P1 name).
6. **"la clôture des détroits"** (Metternich) — second Straits formula beside "les détroits restent fermés…".
7. **"le Pachalik d'Egypte"** (Metternich) — the firman's object named Ottoman-style.
8. Kossuth: 0 hits in all 1841 RdM quarters — confirmed NOT a Jan-1841 ministerial topic (his Pesti Hírlap notwithstanding). Demoted off the list.
9. Zollverein: 0 hits in RdM 1841 — the trade thread lives in Nesselrode/AZ/ADB, not Parisian journals.

---

## v3 delta (2026-10-07, crib miner) — Harvester drops mined
**New files (18):** `talleyrand-memoires-v1.txt`, `guizot-memoires-t1-gutenberg.txt`,
`guizot-memoires-t2-gutenberg.txt`, `guizot-memoires-t3-gutenberg.txt`, and
`allgemeine-zeitung-augsburg-1841-01-12..25.txt` (v2 had only 11-Jan). Miner run:
`python3 miner.py work/mine-v3/corpus work/mine-v3` → `code/side-period/work/mine-v3/mine.json`
(symlinked staging of the 18 new files only). Cards here are DELTA-ONLY: nothing v1/v2
is renumbered or re-proposed. Self red-team screen applied before writing:
no post-18-Jan-1841 knowable facts; no direction-reversed formulae; no
"premier*" re-proposals; all addresses as baron, never comte. AZ 19–25 issues were
mined for background vocabulary only — **no card below rests on a post-18-Jan news item**.

### v3 mining notes
1. **AZ 12-Jan-1841** (Constantinople 23 Dec): Mehemet Ali's *Unterwerfung* received;
   divan vs allied diplomats split over a formal *Begnadigung*; Porte asks the
   representatives "Hat sich Mehemed Ali unterworfen?" — the live state of the
   question Zeschau reports on. **Walker** to take over the Ottoman fleet at Alexandria.
2. **AZ 13-Jan-1841** (Examiner reprint): the **Napier–Stopford** convention mess —
   "der erbliche Besitz Aegyptens" promised by Napier, annulled by Stopford,
   "unsere dem Mehemed Ali geleistete Bürgschaft" blamiert.
3. **AZ 18-Jan-1841** (R5005's own date — read with care): Brest telegraphic despatch
   11 Jan — **peace with Buenos-Ayres concluded** (Mackau); **Bugeaud** nominated to
   Algeria (Valée recalled; Soult's letter: "la pacification de l'Algérie");
   Toulon 10 Jan — steamer **Phaéton** for Alexandria with a replacement for **Cochelet**;
   London Gazette 8 Jan — Porte's 9-Dec decree **lifting the blockade of the Syrian ports**;
   Thiers reads his **Paris-fortifications report** 13 Jan. News-lag caveat: the 17–18 Jan
   issues themselves could not reach Dresden by 18 Jan morning; cards from them are
   ranked P2 (or P1 only where the underlying fact predates them and was in the mail).
4. **Talleyrand v1 / Guizot t1–t3:** no new minister→envoy *salutations* beyond v2;
   letters quoted in Guizot t1 supply the transmission frame **"j'ai l'honneur de vous
   adresser copie de …"** (protest letter, 1825 — the "ma protestation" instance is
   private-voice and NOT proposed; the frame is ministerial). The
   "très-humble et très-obéissant serviteur" closings in Guizot t1 are writer→superior
   register — deliberately NOT proposed for a minister→envoy despatch.
5. Nothing P0-grade emerged (the Levant core is already covered at P0 by traité de
   Londres / firman / Porte / Mehemet-Ali / soumission). No P0 ⇒ **cribs-adjudicated.md
   and memo2-period-corpus.md are NOT updated** (per lane orders).

### v3 new cards
| rank | crib | source | rationale | syllabification | by-ear variants |
|---|---|---|---|---|---|
| P1 | la possession héréditaire de l'Egypte | AZ 12-Jan-1841 ("der erbliche Besitz Aegyptens"); AZ 13-Jan ("in den erblichen Besitz Aegyptens restituirt") | the operative settlement formula under negotiation Jan 1841 — the phrase Zeschau would use for the firman's object; complements v2 "Le Pachalik d'Egypte" | pos-ses-sion-hé-ré-di-tai-re-de-l'E-gyp-te | possesion ereditaire, l'hérédité d'Egypte |
| P1 | la convention du commodore Napier | AZ 13-Jan-1841 (Examiner): "l'annulation… de la convention conclue par le commodore Napier"; "Napier's Convention… durch Admiral Stopford… annullirt" | the fresh mid-Jan controversy — Napier promised hereditary Egypt, Stopford voided it; Napier himself is already v2-P2 | con-ven-tion-du-com-mo-do-re-Na-pier | Napie, Nappier |
| P1 | la levée du blocus des ports syriens | AZ 18-Jan-1841 (London Gazette, 8 Jan): Porte's 9-Dec decree "Aufhebung der Blokade der syrischen Häfen" | dated decree, knowable in Dresden by 18 Jan via London press; the Syrian evacuation's sea-side fact | le-vée-du-blo-cus-des-ports-sy-riens | levee du blocus des ports syriens |
| P1 | le général Bugeaud | AZ 18-Jan-1841: nominated to Algeria command (Valée recalled); Soult's letter on "la pacification de l'Algérie" | freshest French appointment news of mid-Jan 1841 — plausible as the French-intelligence paragraph | gé-né-ral-Bu-geaud | Bugo, Bigeaud |
| P2 | restituer la flotte Ottomane | levant-correspondence French originals ("s'il restitue la flotte Ottomane"); AZ 12-Jan: Walker to take over the fleet at Alexandria | fleet-restitution is the live Alexandrian thread; French surface attested | res-ti-tu-er-la-flot-te-ot-to-ma-ne | flote |
| P2 | la conférence de Londres | AZ 12–18 (2× "Londoner Conferenz") | distinct from P0 "traité de Londres" — the body, not the treaty | con-fé-ren-ce-de-Lon-dres | conferance |
| P2 | l'amiral Walker | AZ 12-Jan: "Admiral Walker soll als Pfortencommissär… die Uebernahme der osmanischen Flotte im Hafen von Alexandrien vornehmen" | British admiral, Porte commissioner for the fleet hand-over | a-mi-ral-Wal-ker | Walkere |
| P2 | l'amiral Stopford | AZ 13-Jan (pair with the Napier card) | the annulling authority; English-form Stopford | a-mi-ral-Stop-ford | Stoford |
| P2 | le maréchal Valée | AZ 18-Jan: recalled from Algeria command, replaced by Bugeaud | the outgoing commander in the freshest French news | ma-ré-chal-Va-lée | Valee |
| P2 | la paix avec Buenos-Ayres | AZ 18-Jan (Brest telegraphic despatch, 11 Jan): "der Friede abgeschlossen" | France–Buenos-Aires settlement; news-lag borderline, hence P2 | la-paix-a-vec-Bu-e-nos-Ay-res | Buenos Aires |
| P2 | l'amiral Mackau | AZ 18-Jan: Admiral Mackau negotiating the Buenos-Ayres peace | French naval commander on a live negotiation | a-mi-ral-Ma-ckau | Maco |
| P2 | la pacification de l'Algérie | AZ 18-Jan (Soult letter, verbatim French in the German text: "die Pacification Algeriens") | the Algeria command change's stated object | pa-ci-fi-ca-tion-de-l'Al-gé-rie | pacification d'Algerie |
| P2 | la garantie donnée à Mehemet-Ali | AZ 13-Jan ("unsere dem Mehemed Ali geleistete Bürgschaft") | fuller form of v2's generic "la garantie" — the allies' pledge to the Pasha | ga-ran-tie-don-née-à-Me-he-met-A-li | garanti donnee |
| P2 | M. Cochelet | AZ 18-Jan (Toulon 10 Jan): the Phaéton sails for Alexandria with "der Ersatzmann für Hrn. Cochelet" — France's man at the Pasha's court being replaced | freshest French-Levant personnel news; by-ear spelling likely | co-che-let | Cochele, Cochlet |
| P2 | Dost Mohammed | AZ 12–18 (5×): Afghan-war background still circulating | Central-Asian background of possible interest to a Petersburg-bound despatch | dost-mo-ha-mmed | Dost Mohamet |
| P2 | j'ai l'honneur de vous adresser copie de … | Guizot t1 (letter 1825: "j'ai l'honneur de vous adresser copie de ma protestation" — "ma protestation" NOT proposed, private-voice) | ministerial transmission frame for enclosures; direction minister→envoy is sound | j'ai-l'hon-neur-de-vous-a-dres-ser-co-pie-de | — |
