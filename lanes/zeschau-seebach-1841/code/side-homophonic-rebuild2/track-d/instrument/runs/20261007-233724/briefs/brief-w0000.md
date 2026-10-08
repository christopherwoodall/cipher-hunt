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
  "candidate_label": "5888ca6b",
  "pass_no": 1,
  "text": "Le dialogue du mourant et de l'évêque se poursuivit. « Quant à Louis XVI, j'ai dit non, déclara le conventionnel. Je ne me crois pas le droit de tuer un homme ; mais je me sens le devoir d'exterminer le mal. J'ai voté la fin du tyran, c'est-à-dire la fin de la prostitution pour la femme, la fin de l'esclavage pour l'homme, la fin de la nuit pour l'enfant. En votant la république, j'ai voté la fraternité, la concorde, l'aurore ! » L'évêque murmura : « Oui ? 93 ! » Le vieillard se dressa : « Ah ! vous y voilà ! J'attendais ce mot-là. Un nuage s'est formé pendant quinze cents ans ; au bout de quinze siècles, il a crevé. Vous faites le procès au coup de tonnerre. » L'évêque répondit que le prêtre parle au nom de la pitié, justice plus élevée, et qu'un coup de tonnerre ne doit pas se tromper — puis, fixant le conventionnel : « Louis XVII ? » Le mourant saisit son bras : pleure-t-on l'enfant innocent ou l'enfant royal ? Le frère de Cartouche, pendu en place de Grève pour le seul crime d'être le frère de Cartouche, ne lui semble pas moins douloureux que le petit-fils de Louis XV martyrisé au Temple. « Christ aimait les crudités du vrai, reprit-il ; il ne se fût pas gêné de rapprocher le dauphin de Barabbas du dauphin d'Hérode. L'innocence est aussi auguste déguenillée que fleurdelysée. » L'évêque, à voix basse : « C'est vrai. » Il faut pleurer sur tous les enfants, ceux d'en bas comme ceux d'en haut — « et si la balance doit pencher, que ce soit du côté du peuple. Il y a plus longtemps qu'il souffre. » Puis, explosion : « Qui êtes-vous ? Vous êtes un prince de l'Église, un de ces hommes dorés, rentés, qui roulent carrosse au nom de Jésus-Christ qui allait pieds nus ! Votre nom est arrivé jusqu'à moi, mais les habiles ont tant de manières d'en faire accroire au peuple. » L'évêque baissa la tête : « Vermis sum. — Un ver de terre en carrosse ! » grommela le conventionnel. Doux, l'évêque demanda en quoi son carrosse, sa table et ses vingt-cinq mille livres de rentes prouvaient que la pitié n'est pas une vertu et que 93 fut inexorable. Le vieillard s'excusa de son manque de courtoisie, puis riposta : « Que pensez-vous de Marat battant des mains à la guillotine ? — Que pensez-vous de Bossuet chantant le Te Deum sur les dragonnades ? » Et il aligna les terreurs de la monarchie contre celles de la Révolution : Montrevel, Lamoignon-Bâville, Louvois, et cette huguenote de 1685, liée nue à un poteau, son nourrisson tenu à distance, sommée de choisir entre la mort de son enfant et celle de sa conscience. « La révolution française a eu ses raisons. Les brutalités du progrès s'appellent révolutions. Quand elles sont finies, on reconnaît que le genre humain a été rudoyé, mais qu'il a marché. » L'évêque joua sa dernière carte : « Le progrès doit croire en Dieu. Le bien ne peut pas avoir de serviteur impie. » Le vieillard trembla, une larme coula, et il dit, l'oeil perdu : « O toi ! ô idéal ! toi seul existes ! » Puis, levant un doigt vers le ciel : « L'infini est. Il est là. Si l'infini n'avait pas de moi, le moi serait sa borne ; il ne serait pas infini. Or il est. Donc il a un moi. Ce moi de l'infini, c'est Dieu. » Épuisé, les yeux fermés, il touchait à sa fin. L'évêque prit sa main glacée : « Cette heure est celle de Dieu. Ne trouvez-vous pas regrettable que nous nous fussions rencontrés en vain ? » Le mourant rouvrit les yeux et fit le récit de sa vie : les abus combattus, le territoire défendu, la pauvreté gardée — il dînait à vingt-deux sous rue de l'Arbre-Sec quand les caves du Trésor regorgeaient d'or —, les opprimés secourus, un couvent sauvé en 1793, puis la proscription et l'isolement accepté sans haine. « J'ai quatre-vingt-six ans ; je vais mourir. Qu'est-ce que vous venez me demander ? — Votre bénédiction, » dit l'évêque, et il s'agenouilla. Quand il releva la tête, le conventionnel venait d'expirer, la face devenue auguste. L'évêque rentra absorbé, passa la nuit en prière, et désormais ne répondit aux curieux qu'en montrant le ciel, redoublant de tendresse pour les petits et les souffrants."
 },
 {
  "candidate_label": "b1eee668",
  "pass_no": 1,
  "text": "duceadireladelapurlaladelpurlladlapurllelajecelajelalaljealadeedeledeededelalemOdelemOdedeAsesurleeunedlevekevudireecedukOlaetejAllenleleideelecelanepailledeneleevujemedunedelasalevekeeladuedenekOlediseladulepaeldualealeaasurladedealaceledellevekenesdelesesursauneekUsilsvujceUseoleilavuleodelselkeAluiililleodelaleodelakineotrekunenedenepalapremiereseeilleledelaeledelevekesurkivuecesurljevuecesurljeapurledeleledacekespurledeteledenepakeledladupurldeteledelevekejenemepadepurdevuilUdlevekedeilseedelevunpaleeleluiiluneeilledUdilsilnepaletreleilnesepadeledeedlesaalnakedekecelevekeajcOtinuadevumsurlesurlesurlesurdAcOmsurdAjAjevuleilkeecekiljesurledevukevusurleejesurlevekesesilakecedueilakililneclekililsesurUletreeddesacOmeOOekOelevekeUdeledelceuneilakelecenepacelakevumeemedejenevupakejecejenepalenekekimedeeileaejedepacelanrilelededAaceleajenepaledevullealdelajenevupajevumkelevekecelanemesurAjevukivudevekeceadireddelUdkideldededekidekidekikidedlekiseAdekideekiolekivuUledlavievuclacOmeleecOmelevuAcecelaApacelanempasureavukiladmdelaakiecekejekivulevekelaeUdAdecleededelevekedlevekeAmOkieapaleAeledkejeleAdelemOekelanepaunekelanepadekenapaetelepasalasurcOmepurleUdevuiljevudemejUdvuvumOjevuideeilkejemeaedekejecOtrevuleileledenepamAjevulenelejevulevekealkevumeAkemvukeaetelevekekevuledealakevudeletesurleladureoladunedlevekeAilneluiilledeleesededdelalaldelkiseluilailundleilejeAdelakieuneeunevudelaenevuaduneesuresilvuledumvupurleeUkemldjeejkilelelieenuealaaUltenualesedeeledleeceeelealaeluiaAtreladeeladesakedecedeaunelaasalceledeleilunepurlejjemjedjemedelevekedesaleledusOkeleaetekilalenesepakildlUlotreledelevekeilAdedcedeladeladuleAlnepadecenedukecluikieledunpailUilleeuneclalaledesalivideeilAesealuillelevekeundUlUleleilesilnpadelesailnpaAdilnepaileilaUcdelceleduneeledlcOmesilneilsellilkildeAunelekiluicekildedireldeceluikielallevekeleleccOmekildelilalilileeseleedenvupakilkeAleleuneildlssurlevekeilunekideladlkedeladejevielalelajmOmaemademedejeildejeleeildejleeildeedejeleeelejelelajejnpajejeetelnededelledudokOdleaseledledeljedlajelejelejeladelcecpurledelajelaAdulaejeojelvueilaaAalledetenedlleAkejelejemOelkejejeetedejekelessurledejepurladejneldelajejekecekevumelevekeeilslevekelaladuilUlevekeluiOneilpasalaleldeluieilsealeadeceildelepurleeleacedeleunenekeledelsiAeledesurlasiAnenepadlavisiteunedpurleceladUkeleUdilnpadeakaileteilkildUdledundelakiseluiOdelevekekekiladladuneOdesesilOdekedevekedsackOsadeluiunedkileneterilekUceldledAkeaunAdldemallldelAkelducOmeOladuoamodeleedaceseaespurladelademlmedekisilnkauneeaevekedUsidelalaeldenuemAilkildeideekiladelilviteaOlesurceiljelelejelduneuneotreilkevudejenekUevekeleekilletreilluidedirenekilseUdlelelelecekejenepaceameiladekiiladekiiladeiladeleAcenepaunkeladuladeledAdelaedeleUildededdesdeOeealealealesurUdcOmeladuseOUkiedUekinapaseOdkiauneekinaUdundniddeoladelalelevekecelaccekemlevekedeilnepadkilsurcekeleideeduilseduesesurlelelsiOlilkOlkecOmeneekeneriAdkilpuraleililaleildele"
 },
 {
  "candidate_label": "fc12e892",
  "pass_no": 1,
  "text": "mememememememetremeleursmememememeleurslameleursmememeleursmelamemeleursmemelamememetremememeleursmememeleursmemeleursmemememeleursleursmememeleursmemememememememememememelamemememememememememeleursmememetremememememememememetreleursleurskeleursleursimekeleursmemekemememelamememememememememememelameleursmememeleursmeleursmeleursmekelamekeleursmelamemememememeleursmemememememememeleursimeleurslakeleursileurslamemememeleurslamekemeleursmemememememememememememeleurslamemememelamememememememeleursleursmememememelapremieremememelamememememeleursmeleursmememelamememememememeleursmeiememememeleursmemeleursmemememememememememememeleursmememememememememeleurskemememememememeleursmememememeleursmemememememememememememeleursleursimememelamemeleursmememelameleursleursmemeleursmemememememememememememeleursmememememememeleursmemememememememeleursmememetrelamelakememememememeleursmemememeleursmememememememememememeleursmememeleurslamemememememememememeleursmeleurslamememelaleursmememememeleursmemetremelamememekelamemelameleursmemememeleursmememekememekemeleurslamemeleursleursmemememeleursmememememememeleursmeleurslamemememememeleursimemememememeleursmememeleursmeleursmeleursmemememelameleursmemememeleursmleursileursileursmeleursmemememememekeleursimemememememememeleursmemetrememeleursimememememememememememememememememeleursmememememememememememememeleurskemememememememememeememememememeleurslamemememememekeleursmemememelalamemekelamememememememememeleursmemeleursleursmeleursilamememeleursmeleurslamememeleursmeleurslaleursmemememememememememekeleursmeeleurslameleursmememememeleursmememeleursimemeleursmemeleurslalamememeleursmeleurskemeleurskememememememememememememememememememelamemememememeleursmememememememememeleursmemememelamemeleursmememelamememememememememememememememememememeleurslamemelamememeleursmeleursmemekeleurslamememememememeleursmememememeleursmemememekemelameleursmememeleursmemelaleursmememelakemeleursmemeleursmemememekemelamememeleurskemememememeleursimemeleursmememememetremememeleursmeleursmemelamemetreleurskemeleurskememetreleursmemememememememememeleursmememememememememememememememetremememeleurskemememememeleursmememeleursmememememememelamemememeleursimememememememememememememeleursmemeleursmemememememememememememeleursmememememeleursmemememememememememekemememememeleurslamelamemememeleursmemememetrememelamememeleurslameleursimemememememememememeleursimemelamemememememememememememememememememeleurstreleursmeleurslamemememeememememememememememememememememememememememeleursmemememeleursmemeleursmemeleursmemeleursemememememememeleurskeleursmememememeleurslamememeleursimeleursmeleursmeleursmememememememememememememememeleursmememememeleursmemememememeememememememememekememeleursmemememememememeleursmemeleurskememememememememememememememememememememememeleursimekememememelamememememememekemeleursleursleursimememememememememememememememememememememememememememememelaleursmememememememeleursleursimemememememememememememememememelalamemeekelamemememememememememememememememememememememememememelamemememekeleursmemememelalamemelalamememelalamemelameleursmemememeleursmemememeleursmemememeleursmemememememememememeleursmememememememememekeleursmemeleursleursememeleursimemeememelamememeleursmememelamememememememememememeleursilamemeleurslamemememememememememememememeleursmemememememeleursmemememeleurslamememememelamemetreleursleursileursmememememememeleursimemeleursimememememememeleurslamemelameememememeleurspareleursmemememememememememememeleursmemememememememeleurslamemememeleursmememememeleursmememelalamemememememelamemelamemeleursmemeleursmemememememememememememeimemememeleursimememeleursikememeleursmememeleursmememememeemememelalamememememeleursleursmeleursleursmemeleursmemememeleursmememekememememememememememeleursmememeleursmeleursmememeleurslamemeleursmeemememememememememememeleurslaleursmememememememeleursmemememeleursimemeleursmeleursmemememeleursmeleursleursmeikemememememememeleursmemememememememememelamememememememememeleursmemetretrekememememememememememememememeleursmemeleursmememeleursmelamememememeleursmemememeleursmememelametreleursmemeleurslamelamememememememelamememeleursmemememetreleurskemeleursmelamemememememeleurskememememememeleurslamemememememetremememememelaleurslameleursmemememememememememeleursmemeleurslamememememememememememelaleursimeleursmemememeleursleursmememememeemeemememeleursmeme"
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
  "worker_id": "w0000",
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
