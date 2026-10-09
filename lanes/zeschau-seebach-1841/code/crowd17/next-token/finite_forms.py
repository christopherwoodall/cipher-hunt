#!/usr/bin/env python3
"""Generate a broad finite-verb form set for 19th-c French fragment detection.

Regular conjugations generated for ~150 common infinitives; irregulars hand-listed.
Criterion is documented in the battery report; hand-audit backs the calls.
"""
import re, unicodedata

def deacc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

VERBS_ER = """parler penser trouver porter passer rester entrer arriver donner
demander garder jouer montrer monter tomber tourner retourner sembler
trembler appeler rappeler jeter acheter achever mener esperer
preferer proteger repeter ceder regler regner durer douter
aimer adorer admirer approuver ecouter regarder chercher
pousser tirer casser passer
marcher travailler etudier continuer commencer recommencer
annoncer denoncer prononcer avancer placer remplacer
oublier remercier crier prier payer essayer
diner dejeuner causer conter raconter chanter danser
sauver prouver eprouver trouver
bruler briller couler rouler
frapper attraper echapper
sembler resembler
oser hesiter
commander ordonner defendre
accorder refuser
louer blamer
tuer blesser
marier
habiter loger
signer
songer
plaisanter
""".split()

VERBS_IR = """finir choisir saisir obeir punir remplir gemir
applaudir batir etablir abolir
fleurir
""".split()

VERBS_RE = """rendre prendre comprendre apprendre reprendre entreprendre
mettre permettre promettre soumettre
attendre entendre pretendre defendre vendre pendre
repondre correspondre
perdre
rompre interrompre
battre combattre abattre
craindre plaindre contraindre
peindre eteindre eteindre
conduire produire reduire deduire
connaitre paraitre apparaitre disparaitre naitre renaitre
plaire deplaire
taire
croire boire
voir revoir prevoir
lire elire relire
dire redire contredire predire
ecrire decrire
rire sourire
suivre poursuivre
vivre survivre
conclure exclure
""".split()

IRREG = """suis es est sommes etes sont etais etait etions etiez etaient
fus fut fumes futes furent serai seras sera serons serez seront
serais serait serions seriez seraient sois soit soyons soyez soient
ete
ai as a avons avez ont avais avait avions aviez avaient
eus eut eumes eutes eurent aurai auras aura aurons aurez auront
aurais aurait aurions auriez auraient aie ait ayons ayez aient
fais fait faisons faites font faisais faisait faisions faisiez faisaient
fis fit fimes fites firent ferai feras fera ferons ferez feront
ferais ferait ferions feriez feraient fasse fasses fassions fassent
dis disons dites disent disais disait disions disiez disaient
dit dimes dites dirent dirai diras dira dirons direz diront
dirais dirait dirions diriez diraient dise dises disions disent
puis peux peut pouvons pouvez peuvent pouvais pouvait pouvions pouviez pouvaient
pus put pumes putes purent pourrai pourras pourra pourrons pourrez pourront
pourrais pourrait pourrions pourriez pourraient puisse puisses puissions puissent
veux veut voulons voulez veulent voulais voulait voulions vouliez voulaient
voulus voulut voulumes voulutes voulurent voudrai voudras voudra voudrons voudrez voudront
voudrais voudrait voudrions voudriez voudraient veuille veuilles veuillions veuillent
dois doit devons devez doivent devais devait devions deviez devaient
dus dut dumes dutes durent devrai devras devra devrons devrez devront
devrais devrait devrions devriez devraient doive doives doivions doivent
sais sait savons savez savent savais savait savions saviez savaient
sus sut sumes sutes surent saurai sauras saura saurons saurez sauront
saurais saurait saurions sauriez sauraient sache saches sachions sachent
vais vas va allons allez vont allais allait allions alliez allaient
allai alla allas allames allates allerent irai iras ira irons irez iront
irais irait irions iriez iraient aille ailles ailles allions alliez aillent
viens vient venons venez viennent venais venait venions veniez venaient
vins vint vinmes vintes vinrent viendrai viendras viendra viendrons viendrez viendront
viendrais viendrait viendrions viendriez viendraient vienne viennes viennions viennent
vois voit voyons voyez voient voyais voyait voyions voyiez voyaient
vis vit vimes vites virent verrai verras verra verrons verrez verront
verrais verrait verrions verriez verraient voie voies voient
prends prend prenons prenez prennent prenais prenait prenions preniez prenaient
pris prit primes prites prirent prendrai prendras prendra prendrons prendrez prendront
prendrais prendrait prendrions prendriez prendraient prenne prennes prenions prennent
mets met mettons mettez mettent mettais mettait mettions mettiez mettaient
mis mit mimes mites mirent mettrai mettras mettra mettrons mettrez mettront
mettrais mettrait mettrions mettriez mettraient mette mettes mettions mettent
faut fallait faudra fallut
pleut plut
sied
suit suivent suivait suivront suivrait suive
connait connaissent connaissait connaitront connaitrait
parait paraissent paraissait paraitront paraitrait
sert servent servait serviront servirait serve
atteint atteignent atteignait atteindront atteindrait atteigne
sort sortent sortait sortiront sortirait sorte
suppose supposent supposait supposeront supposerait
salue saluent saluait salueront saluerait
parfume parfument parfumait
gouverne gouvernent gouvernait gouverneront gouvernerait
existe existent existait existeront existerait
suffit suffisent suffisait suffiront suffirait suffise
appartient appartiennent appartenait
contient contiennent contenait
devient deviennent devenait deviendront deviendrait devienne
souvient souviennent souvenait souviendra
previent previennent prevenait
soutient soutiennent soutenait
obtient obtiennent obtenait obtiendra
maintient maintiennent maintenait
rejoint rejoignent rejoignait
plaint plaignent plaignait
craint craignent craignait craindra
joint joignent joignait
repond repondent repondait repondra repondrait reponde
vend vendent vendait vendra
pend pendent pendait
attend attendent attendait attendra attendrait attende
entend entendent entendait entendra entende
pretend pretendent pretendait
defend defendent defendait defendra
tord tordent tordait
mord mordent mordait
perd perdent perdait perdra perdrait perde
rend rendent rendait rendra rendrait rende
prend prend (dup ok)
convient conviennent convenait
provient proviennent provenait
survient surviennent survenait
advient adviennent
disconvient
ecrie ecrient (arch)
asseoit asseoit asseyent assoyait assiera assoie
meut meuvent mouvait mouvra meuve
peut (dup)
accroit accroitre (skip)
nait naissent naissait naitra naitrait naisse
croit croissent croissait croitra croitrait croisse
decroit decroissent
paraissent (dup)
apparait apparaissent apparaissait apparaitra
disparait disparaissent disparaissait disparaitra
reparait reparaitre
connait (dup)
meconnait meconnaissent
reconnait reconnaissent reconnaissait reconnaitra reconnaitrait reconnaisse
plait plaisent plaisait plaira plairait plaise
deplait deplaisent deplaisait
tait taisent taisait taira taise
gît gisent
eclot
frit frire
clos clot
envoie envoient envoyait enverra enverrait envoie
renvoie renvoient renvoyait renverra
essaie essaient essayait essayera
paie paient payait payera paiera
appuie appuient appuyait appuiera
essuie essuient essuyait
fuit fuient fuyait fuira fuie
suffit (dup)
git
luisent luisait luira
nuisent nuisait nuira nuise
reluit reluisent reluisait
""".split()

def gen_forms():
    forms = set(IRREG)
    for v in VERBS_ER:
        s = v[:-2]
        for e in ["e","es","ons","ez","ent","ais","ait","ions","iez","aient",
                  "ai","as","a","ames","ates","erent",
                  "erai","eras","era","erons","erez","eront",
                  "erais","erait","erions","eriez","eraient"]:
            forms.add(s + e)
    for v in VERBS_IR:
        s = v[:-2]
        for e in ["is","it","issons","issez","issent","issais","issait","issions","issiez","issaient",
                  "is","it","imes","ites","irent",
                  "irai","iras","ira","irons","irez","iront",
                  "irais","irait","irions","iriez","iraient"]:
            forms.add(s + e)
    for v in VERBS_RE:
        # stem approximation: drop final 're' or handle -dre/-tre
        if v.endswith("dre"):
            s = v[:-3]  # rend-
            pres3 = [s+"ds", s+"d"]       # rend(s)/rend
            forms.update([s+"ds", s+"d", s+"dent", s+"dions", s+"diez",
                          s+"dais", s+"dait", s+"dions", s+"diez", s+"daient",
                          s+"dit", s+"dirent", s+"dra", s+"dront", s+"drais", s+"drait"])
        else:
            s = v[:-2]
            forms.update([s+"s", s+"t", s+"ons", s+"ez", s+"ent",
                          s+"ais", s+"ait", s+"ions", s+"iez", s+"aient",
                          s+"it", s+"irent", s+"ra", s+"ront", s+"rais", s+"rait"])
    return set(deacc(f) for f in forms)

FINITE2 = gen_forms()

if __name__ == "__main__":
    print(len(FINITE2), "forms")
