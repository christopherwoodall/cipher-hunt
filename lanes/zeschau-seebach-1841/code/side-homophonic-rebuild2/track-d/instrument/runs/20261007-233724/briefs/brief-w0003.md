# JUDGE WORKER BRIEF — Track D automated judge instrument

You are a FRENCH-FLUENCY JUDGE. This is a blind, mechanical scoring task.
Read every instruction before scoring anything.

## 0. Prompt integrity check (DO THIS FIRST)

The frozen judge prompt lives at this absolute path:

```
/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/judge_prompt.txt
```

Its expected sha256 is:

```
390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d
```

1. Compute the sha256 of that file (e.g. `sha256sum /home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/judge_prompt.txt`
   or Python `hashlib.sha256(open(path,'rb').read()).hexdigest()`).
2. If it does NOT match the expected hash, STOP IMMEDIATELY and return:

```json
{{"aborted": true, "reason": "prompt hash mismatch", "computed": "<your hash>"}}
```

3. If it matches, read the prompt text FROM THAT FILE and use it for
   all scoring below. (The prompt is also reproduced in §2 for
   reference; the file is authoritative.)

Do not score anything if the hash mismatches. This is a hard abort.

## 1. Your assignments

You will score 3 candidate(s). Each assignment is one
(candidate label, pass number, passage). The labels are blind —
they carry no information about the passage's class. Score the
passages in the order given. Judge EACH assignment INDEPENDENTLY:
do not compare candidates to each other, do not anchor on a
previous score, do not try to infer what the "right" answer is.
There is no right answer — only your honest fluency judgment.

Assignments (JSON):
```json
[
 {
  "candidate_label": "1386766b",
  "pass_no": 1,
  "text": "leideUCapitreimirielCapitreiimirielCapitreiiiapurvekeCapitreleCapitrekeviparkiilsaviiCapitreviiiCapitreleparlalAaCapitreCapitredecekilcekillaCapitreilaUdeiiladlaCapitreiiidelledCapitreviCapitreviilededAduCapitreviiilOdelelCapitrelCapitrecekilCapitrelevekeCapitreAlCapitreilCapitreiiCapitreiiiaCapitresikilCapitrevilOCapitreviideCapitreviiidUCapitredelacCapitreiunkiAuneotreCapitreiideiiillaCapitreidUdAleiimnepitreiiiCapitremACapitrealvileCapitreviiaviiipurlaCapitredeCapitreduCapitreledemCapitrededeiduCapitreiilCapitreilalapremiereiideiiiuneUCapitrekelaldAleCapitrevilaalCapitreviilepurCapitreviiideCapitreUdeAaseCapitrelededAcOtreCapitreidAmnepitreiiCapitreiiiCapitrelUCapitreiAmmirielevekedecUdileaceneAodecekedilnnecekepurAalelelekisOoildAlecekOdededAvieedAdetineekecekmetedUoddeOcOtedeluikesOlepurdesaldeaUdAlemirielceOdeluiildsadlapartiedesavieeteomOdeelaleselesemledelaAsadunemaladiedeelleetenakesetildAladetineedemmirielilalladesaledepurlekiledeledelAluidededeilodunaedekisaviedUdeekiAleolkelenAledAsOledAsanlecekOckeildileteAmmirieletedeileteledAunelduunedesaOnelailpurmeUkeletevisiteasOlekidAlseledesaseuneparceseecekimesiremmirielUeUdeleoildeceemmirielakiletepurvekedekiladudAlekOlapartiedelaviedemmirielneledelalammirielilededAiladekiledekiileilevekeeparcekiletepurvekeleOsOnkededudedekededeldukilAdedeadekidAleleleledAUnAnAmmirieladunekietesalekidekeluipurdukeleetelademtreletitredededededeeteuneelilldecekelkilkuneelenetesaviekinetekundepareleunedeedeleAellecekOladlacekietedeladAsapurtedAsadelalelceteunekeceneteunesadadpurkilUUdeunedeUpurkunlaeteuneadesOdadUasOOmmirielAsOleparlekilevekeledeleleluilaleluidsOlavisiteoeollasOevekealiimirieledepurtealilepurteUeApierreoduparAdeladedeetepurvekedeAceeteUledelleleladallededAladekipurteodeeleaAleadeadepurvekeddedeadededepurvekeddedeevekedeedelduevekedledeleeteAdunedeluneeaUUsOlevekellavisitilledeluiledelluilAcdemaladeccekelevekelelelecOtrelecckelenekedeelccekimeeilaUalepurleccekemedAleleunelamaladeCakeclakimetekeleilsedAladdudlevekeUililseledelilkilderiAkedAlaadeleilevekeladuleledeedeililsealuilaledeldireilaunedAiciepurilamOelemacleledAldelevekeleilevekepurtealmmirielndesaeteparlasaunedekioasammirieldelevekeUdeleilsedAladelmildeunepurdelaunedesapurledemapurlelivrealalivrepurledelivredealivredulivredelalivredelivreApurdlivrepurldelivrepurleleladelivrepurdedepurlivreodeddulivreadelivrededededepurldelivrepurlelivremalivrelivrelekiledemmirielneriAdilcelaOledsauneparpurmdealasOlesOpurvekesOlaesOleltreleleileleillaUmlevekeOlaneetekecekialadepareceleUdeamlevekedelealadeedildeUiletedilevekecelalenalakeledepartemAluipurdeAlededAlepurleacetellevekeilsaleAluiUdeamlevekepurdedeedecelalaedUdeldudeoledeladedodemdeUedededAunededededededaladAUdeilnadeOnkaledelaaddeaavideeceluialeAilleilluiedilluidutrelenkeldealeledelaAelledaparlelakilparluilalivrepurleilevekeeasaunedeedepurdudemaladedellivrepurladeCaritedlivrepurladeCaritedelivrelelivrepurlelivrelivreleammirielodeddelevekelleddkilleoadeleakiekialademmiriellelkeleilevekeAdUledeleleledeledeparriAnekilasOdevieekillasOdeladeAkedeAetepurdireacetedilunildelilnAilselkeledeAdelealeduuneadAleedelevekeceluikiUenelkeeledAlduluiceilnekelekeadirekiliiid"
 },
 {
  "candidate_label": "7e5bbba0",
  "pass_no": 1,
  "text": "Pour faire comprendre le ménage intérieur de l'évêque et la manière dont les deux saintes filles pliaient leurs habitudes aux siennes sans qu'il eût à parler, le mieux est de transcrire une lettre de mademoiselle Baptistine à son amie d'enfance, la vicomtesse de Boischevron. En lavant les murs, madame Magloire a fait des découvertes : sous les papiers blanchis à la chaux se cachent d'anciennes peintures — Télémaque reçu chevalier par Minerve, des romains et des romaines — et ma chambre sera bientôt un vrai musée. « Mon frère est si bon. Il donne tout ce qu'il a aux indigents et aux malades. Nous sommes très gênés... Vous voyez que ce sont de grandes douceurs. » La porte de la maison n'est jamais fermée ; entre qui veut. Il ne craint rien, ni la nuit, ni les routes suspectes. L'an dernier, parti seul quinze jours au pays des voleurs malgré nos craintes, il revint bien portant en disant : « Voilà comme on m'a volé ! » et ouvrit une malle pleine des bijoux de la cathédrale d'Embrun que les brigands lui avaient donnés. « À présent j'ai fini par m'y accoutumer... je rentre dans ma chambre, je prie pour lui, et je m'endors... Le diable entrerait dans la maison qu'on le laisserait faire. Après tout... le bon Dieu l'habite. » Suit un long renseignement généalogique sur la famille de Faux, très ancienne noblesse normande, que l'évêque, excellent royaliste et mémorialiste, lui a dicté. Peu après la date de cette lettre, l'évêque fit une chose jugée plus risquée encore que sa promenade chez les bandits. Près de Digne vivait solitaire un ancien conventionnel, nommé G., objet d'horreur dans la petite ville : un quasi-régicide, un athée, disait-on — commérages des oies sur le vautour. N'ayant pas voté la mort du roi, il avait échappé à l'exil et habitait, à trois quarts d'heure de la ville, un repaire perdu dans un vallon sauvage, sans voisins ni passants. L'évêque regardait parfois l'horizon vers ce bouquet d'arbres et disait : « Il y a là une âme qui est seule », ajoutant en lui-même : « Je lui dois ma visite. » Au fond, il partageait l'éloignement général ; la brebis lui semblait bien galeuse pour le pasteur. Mais un jour on apprit que le vieux scélérat se mourait, la paralysie le gagnant. L'évêque prit son bâton, mit son pardessus à cause de sa soutane usée, et partit au soleil déclinant. Il franchit fossé, haie et échalier, et découvrit une cabane basse, indigente et propre, avec une treille à la façade. Devant la porte, un homme aux cheveux blancs souriait au soleil dans une chaise à roulettes, tandis qu'un petit pâtre lui tendait une jatte de lait. « Merci, dit le vieillard, je n'ai plus besoin de rien... Depuis que je suis ici, voilà la première fois qu'on entre chez moi. Qui êtes-vous, monsieur ? — Je me nomme Bienvenu Myriel. » Le conventionnel, qui allait mourir dans trois heures — le froid montait des pieds aux genoux et gagnait la ceinture — renvoya l'enfant se coucher : « Pendant qu'il dormira, je mourrai. » L'évêque, un peu choqué de n'être pas appelé monseigneur, sentit naître en lui une sévérité inaccoutumée devant ce puissant d'autrefois. Le vieillard, lui, gardait tous les gestes de la santé : regard clair, voix vibrante, épaules robustes — chair par en haut, marbre par en bas, comme ce roi du conte oriental."
 },
 {
  "candidate_label": "ecf4db34",
  "pass_no": 1,
  "text": "Les paroles de l'évêque valaient ses actes, et ses actes valaient ses paroles. Un jour, trop petit pour atteindre un livre placé trop haut dans sa bibliothèque, il demanda une chaise à madame Magloire : « Ma grandeur ne va pas jusqu'à cette planche. » Sa cousine, la comtesse de Lô, énumérait complaisamment les « espérances » de ses trois fils — héritages, duché, pairie — quand l'évêque, rêveur, l'interrompit : « Je songe à quelque chose de singulier, dans saint Augustin : Mettez votre espérance dans celui auquel on ne succède point. » Recevant un faire-part funèbre chargé de titres nobiliaires, il s'écria : « Quel bon dos a la mort ! » Un jeune vicaire ayant prêché sur la charité, un riche manufacturier usurier, M. Géborand, qui de sa vie n'avait fait l'aumône, se mit à donner chaque dimanche un sou aux mendiantes du portail. L'évêque, le voyant, dit en souriant à sa soeur : « Voilà monsieur Géborand qui achète pour un sou de paradis. » Quêtant dans un salon, il aborda le marquis de Champtercier, avare et voltairien : « Monsieur le marquis, il faut que vous me donniez quelque chose. — Monseigneur, j'ai mes pauvres. — Donnez-les-moi, » répondit l'évêque. Dans un sermon resté célèbre, il dénonça l'impôt des portes et fenêtres qui entassait les paysans dans des masures sans air, et décrivit la misère du Dauphiné : pas de brouettes, pas de chandelles, le pain cuit pour six mois avec de la bouse séchée. Né Provençal, il parlait tous les patois du Midi, ce qui lui ouvrait toutes les âmes. Se qualifiant lui-même d'ex-pécheur, il professait une doctrine d'indulgence : l'homme traîne sa chair et lui cède ; être saint est l'exception, être juste est la règle ; le péché est une gravitation. Apprenant l'histoire d'un faux-monnayeur perdu par la jalousie qu'un procureur avait savamment attisée chez sa complice, il demanda doucement : « Et où jugera-t-on monsieur le procureur du roi ? » Un condamné à mort, ancien bateleur, se vit refuser l'aumônier de la prison ; l'évêque prit sa place, passa le jour et la nuit auprès du misérable, le suivit en camail violet jusqu'à l'échafaud, l'embrassa avant le couteau : « Celui que l'homme tue, Dieu le ressuscite. » De retour, il dit à sa soeur : « Je viens d'officier pontificalement. » La vue de la guillotine le hanta longtemps ; il en tira une méditation sur cette machine qui n'est pas neutre et ne permet pas de rester neutre. On l'appelait à toute heure au chevet des mourants ; il savait se taire des heures auprès d'un affligé, puis parler pour tourner la douleur vers l'espérance. Sa vie intérieure égalait sa vie publique : une pauvreté volontaire, dont témoignaient ses soutanes qu'il faisait durer trop longtemps."
 }
]
```

## 2. Scoring protocol (frozen prompt — read it from the file verified in §0)

For reference, the frozen prompt text is reproduced below. The FILE
(at `/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/judge_prompt.txt`) is authoritative — if this reproduction ever
differed from the file, the file wins (and the hash check in §0 would
have caught it).

--- PROMPT BEGIN ---
You are a judge of French-language fluency. You will be shown a passage of text. Some passages are fluent French; others are degraded, garbled, or adversarially constructed.

Rate the passage's FRENCHNESS — how much it reads as natural, fluent French prose — on a 0–100 scale:

- 100: flawless, natural French prose (any era)
- 75: clearly French, with minor errors or oddities
- 50: fragmented French; roughly half is broken or non-French
- 25: mostly non-French, with scattered French-like fragments
- 0: not French at all

Judge ONLY fluency as French. Do not reward or penalize subject matter, era of style, or passage length.

Output format (exact): the first line is a single integer from 0 to 100 and nothing else. The second line is exactly one sentence explaining the score. No other text.

PASSAGE:
---
{text}
---
--- PROMPT END ---

For each assignment: substitute the passage text for `{text}`,
apply the prompt, and produce your response in the prompt's EXACT
output format: first line a single integer 0–100, second line
exactly one sentence explaining the score. No other text.

## 3. Hard constraints (violations void the run)

- Score ONLY what the prompt asks: French fluency. Nothing else.
- One integer + one sentence per assignment. No extra commentary,
  no hedging paragraphs, no meta-discussion.
- Do NOT re-score, revise, or "second-guess" any assignment after
  writing it. First honest judgment stands.
- Do NOT discuss these passages with anyone or reference outside
  material. Judge the text in front of you.
- If a passage is empty or unreadable, score it 0 with the
  justification "Empty or unreadable passage." — do not abort.

## 4. Return format (exact)

Return a single JSON object and nothing else:

```json
{{
  "worker_id": "w0003",
  "prompt_sha256_computed": "<sha256 you computed in step 0>",
  "prompt_sha256_expected": "390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d",
  "results": [
    {{"candidate_label": "<label>", "pass_no": <n>,
      "raw_response": "<int>\\n<one sentence>"}}
  ]
}}
```

One entry per assignment, in the order given. `raw_response` is the
literal two-line string: integer, newline, single sentence.
