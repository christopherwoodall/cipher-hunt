#!/usr/bin/env python3
"""bare-subj-corpus census: do bare singular -de-final nouns ever serve as
finite-verb subjects in 1841 French?

Corpus: code/side-period/corpus, French files only (German files excluded:
adb-zeschau-*, allgemeine-zeitung-augsburg-1841-*, metternich-papiere-*).

Method (mirrors battery bare-noun-1841, 2026-10-09):
1. Tokenize (lowercased, apostrophe-preserving, curly-apostrophe normalized).
2. Noun lexicon: tokens following a determiner >=5 times, minus function-word
   stoplist -> filter to singular -de-final nouns (endswith 'de', not 'des').
3. Candidate extraction: [PREV] [NOUN-de] [V] where PREV is not a
   determiner/article/preposition/pronoun (bare check) and V is a finite-verb
   form (curated list UNION data-driven verb-position heuristic).
4. Every candidate is hand-checked with original-text context (see handaudit).
   Regex/auto counts are never trusted alone.
"""
import os, re, json
from collections import Counter, defaultdict

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
CORPUS = os.path.join(LANE, 'code/side-period/corpus')
EXCLUDE = ('adb-zeschau-', 'allgemeine-zeitung-augsburg-1841-', 'metternich-papiere-')
OUTDIR = os.path.join(LANE, 'code/crowd17/next-token')

def norm_apos(s):
    return s.replace('\u2019', "'").replace('\u2018', "'").replace('\u02bc', "'")

TOK = re.compile(r"[a-zA-Z\u00e0\u00e2\u00e4\u00e9\u00e8\u00ea\u00eb\u00ee\u00ef\u00f4\u00f6\u00f9\u00fb\u00fc\u00e7\u0153\u00e6']+")

DET = set("""le la les l' un une des du de d' au aux ce cet cette ces mon ma mes
ton ta tes son sa ses notre nos votre vos leur leurs quel quelle quels quelles chaque
aucun aucune nul nulle tout toute tous toutes quelque quelques tel telle tels telles
autre autres certain certaine certains certaines meme memes plusieurs""".split())

PREP = set("""a au aux de d' des du en dans sur sous par pour sans avec entre vers
contre pendant depuis jusque chez parmi outre malgre hormis sauf selon durant voici
voila envers pres loin autour dessus dessous devant derriere avant apres jusqu
afin hors quant""".split())

PRON = set("""je tu il elle ils elles on nous vous me te se le la les lui leur y en
moi toi soi eux celui celle ceux celles ceci cela ca qu' que qui dont ou quoi
m' t' s' j' c' n' qu' d' l'""".split())

BARE_BLOCK_PREV = DET | PREP | PRON

FUNCTION_STOP = BARE_BLOCK_PREV | set("""et ou ni car donc or mais si comme quand
lorsque puisque parce pourquoi comment combien autant aussi bien plus moins tres
trop peu assez si tant tellement ainsi alors donc ensuite puis enfin deja encore
toujours jamais souvent parfois rarement ne non pas point guere nullement certes
peutetre helas hui aujourd'hui hier demain maintenant ici la bas dessus dessous
dedans dehors devant derriere partout ailleurs autrement ensemble ainsi""".split())

# ---- curated finite 3sg/3pl forms ----
FINITE = set()
def add(*ws):
    for w in ws:
        FINITE.add(norm_apos(w).lower())

# irregulars: present, imperfect, future, conditional, subjunctive, passe simple (3sg/3pl)
add('est','sont','etait','etaient','sera','seront','serait','seraient','soit','soient',
    'fut','furent','ete','a','ont','avait','avaient','aura','auront','aurait','auraient',
    'ait','aient','eut','eurent','fait','font','faisait','faisaient','fera','feront',
    'ferait','feraient','fasse','fassent','fit','firent','dit','disent','disait','disaient',
    'dira','diront','dirait','diraient','dise','disent','peut','peuvent','pouvait','pouvaient',
    'pourra','pourront','pourrait','pourraient','puisse','puissent','put','purent',
    'doit','doivent','devait','devaient','devra','devront','devrait','devraient','doive',
    'durent','veut','veulent','voulait','voulaient','voudra','voudront','voudrait','voudraient',
    'veuille','veuillent','voulut','voulurent','sait','savent','savait','savaient','saura',
    'sauront','saurait','sauraient','sache','sachent','sut','surent','va','vont','allait',
    'allaient','ira','iront','irait','iraient','aille','aillent','alla','allerent','vient',
    'viennent','venait','venaient','viendra','viendront','viendrait','viendraient','vienne',
    'vint','vinrent','tient','tiennent','tenait','tenaient','tiendra','tiendront','tiendrait',
    'tiendraient','tienne','tint','tinrent','prend','prennent','prenait','prenaient','prendra',
    'prendront','prendrait','prendraient','prenne','prit','prirent','met','mettent','mettait',
    'mettaient','mettra','mettront','mettrait','mettraient','mette','mit','mirent','donne',
    'donnent','donnait','donnaient','donnera','donneront','donnerait','donneraient','donna',
    'donnerent','semble','semblent','semblait','semblaient','semblera','sembleront','semblerait',
    'sembleraient','sembla','semblerent','devient','deviennent','devenait','devenaient',
    'deviendra','deviendront','deviendrait','deviendraient','devienne','devint','devinrent',
    'parait','paraissent','paraissait','paraissaient','paraitra','paraitront','paraitrait',
    'paraitraient','paraisse','parut','parurent','reste','restent','restait','restaient',
    'restera','resteront','resterait','resteraient','resta','resterent','passe','passent',
    'passait','passaient','passera','passeront','passerait','passeraient','passa','passerent',
    'porte','portent','portait','portaient','portera','porteront','porterait','porteraient',
    'porta','porterent','suit','suivent','suivait','suivaient','suivra','suivront','suivrait',
    'suivraient','suive','suivit','suivirent','trouve','trouvent','trouvait','trouvaient',
    'trouvera','trouveront','trouverait','trouveraient','trouva','trouverent','permet',
    'permettent','permettait','permettaient','permettra','permettront','permettrait',
    'permettraient','permit','permirent','croit','croient','croyait','croyaient','croira',
    'croiront','croirait','croiraient','croie','crut','crurent','voit','voient','voyait',
    'voyaient','verra','verront','verrait','verraient','voie','vit','virent','pense','pensent',
    'pensait','pensaient','pensera','penseront','penserait','penseraient','pensa','penserent',
    'connait','connaissent','connaissait','connaissaient','connaitra','connaitront',
    'connaitrait','connaissent','connut','connurent','part','partent','partait','partaient',
    'partira','partiront','partirait','partiraient','parte','partit','partirent','sort','sortent',
    'sortait','sortaient','sortira','sortiront','sortirait','sortiraient','sorte','sortit',
    'sortirent','sert','servent','servait','servaient','servira','serviront','servirait',
    'serviraient','serve','servit','servirent','sent','sentent','sentait','sentaient','sentira',
    'sentiront','sentirait','sentiraient','sente','sentit','sentirent','vit','vivent','vivait',
    'vivaient','vivra','vivront','vivrait','vivraient','vive','vecut','vecurent','meurt',
    'meurent','mourait','mouraient','mourra','mourront','mourrait','mourraient','meure','mourut',
    'moururent','nait','naissent','naissait','naissaient','naitra','naitront','naitrait',
    'naitraient','naisse','naquit','naquirent','offre','offrent','offrait','offraient','offrira',
    'offriront','offrirait','offriraient','offrit','offrirent','souffre','souffrent','souffrait',
    'souffraient','souffrira','souffriront','souffrirait','souffriraient','souffrit','souffrirent',
    'ouvre','ouvrent','ouvrait','ouvraient','ouvrira','ouvriront','ouvrirait','ouvriraient',
    'ouvrit','ouvrirent','couvre','couvrent','couvrait','couvraient','couvrira','couvriront',
    'couvrirait','couvriraient','couvrit','couvrirent','decouvre','decouvrent','decouvrait',
    'decouvraient','decouvrira','decouvriront','decouvrirait','decouvriraient','decouvrit',
    'decouvrirent','recoit','recoivent','recevait','recevaient','recevra','recevront','recevrait',
    'recevraient','recoive','recut','recurent','faut','fallait','faudra','faudrait','faille',
    'pleut','plu','sagit','sagissait','sagira','sagirait','vaut','valent','valait','valaient',
    'vaudra','vaudront','vaudrait','vaudraient','vaille','vaillent','valut','valurent','coute',
    'coutent','coutait','coutaient','coutera','couteront','couterait','couteraient','couta',
    'couterent','importe','importent','importait','importaient','importera','importeront',
    'importerait','importeraient','importa','importerent','existe','existent','existait',
    'existaient','existera','existeront','existerait','existeraient','exista','existerent',
    'appartient','appartiennent','appartenait','appartenaient','appartiendra','appartiendront',
    'appartiendrait','appartiendraient','appartienne','convient','conviennent','convenait',
    'convenaient','conviendra','conviendront','conviendrait','conviendraient','convienne',
    'contient','contiennent','contenait','contenaient','contiendra','contiendront','contiendrait',
    'contiendraient','contienne','obtient','obtiennent','obtenait','obtenaient','obtiendra',
    'obtiendront','obtiendrait','obtiendraient','obtienne','appelle','appellent','appelait',
    'appelaient','appellera','appelleront','appellerait','appelleraient','appela','appelerent',
    'jette','jettent','jetait','jetaient','jettera','jetteront','jetterait','jetteraient',
    'jeta','jeterent','mene','menent','menait','menaient','menera','meneront','menerait',
    'meneraient','mena','menerent','amene','amenent','emmena','promene','espere','esperent',
    'esperait','esperaient','esperera','espereront','espererait','espereraient','espera',
    'espererent','repete','repetent','repetait','repetaient','repetera','repeteront','repeterait',
    'repeteraient','repeta','repeterent','cede','cedent','cedait','cedaient','cedera','cederont',
    'cederait','cederaient','ceda','cederent','possede','possedent','possedait','possedaient',
    'possedera','possederont','possederait','possederaient','posseda','possederent','protege',
    'protegent','protegeait','protegeaient','protegera','protegeront','protegerait',
    'protegeraient','protegea','protegerent','dirige','dirigent','dirigeait','dirigeaient',
    'dirigera','dirigeront','dirigerait','dirigeraient','dirigea','dirigerent','oblige',
    'obligent','obligeait','obligeaient','obligera','obligeront','obligerait','obligeraient',
    'obligea','obligerent','change','changent','changeait','changeaient','changera','changeront',
    'changerait','changeraient','changea','changerent','mange','mangent','mangeait','mangeaient',
    'mangera','mangeront','mangerait','mangeraient','mangea','mangerent','partage','partagent',
    'partageait','partageaient','partagera','partageront','partagerait','partageraient',
    'partagea','partagerent','voyage','voyagent','voyageait','voyageaient','voyagera',
    'voyageront','voyagerait','voyageraient','voyagea','voyagerent','commence','commencent',
    'commencait','commencaient','commencera','commenceront','commencerait','commenceraient',
    'commenca','commencerent','place','placent','placait','placaient','placera','placeront',
    'placerait','placeraient','placa','placerent','menace','menacent','menacait','menacaient',
    'menacera','menaceront','menacerait','menaceraient','menaca','menacerent','avance',
    'avancent','avancait','avancaient','avancera','avanceront','avancerait','avanceraient',
    'avanca','avancerent','lance','lancent','lancait','lancaient','lancera','lanceront',
    'lancerait','lanceraient','lanca','lancerent','marche','marchent','marchait','marchaient',
    'marchera','marcheront','marcherait','marcheraient','marcha','marcherent','travaille',
    'travaillent','travaillait','travaillaient','travaillera','travailleront','travaillerait',
    'travailleraient','travailla','travaillerent','cherche','cherchent','cherchait','cherchaient',
    'cherchera','chercheront','chercherait','chercheraient','chercha','chercherent','regarde',
    'regardent','regardait','regardaient','regardera','regarderont','regarderait','regarderaient',
    'regarda','regarderent','ecoute','ecoutent','ecoutait','ecoutaient','ecoutera','ecouteront',
    'ecouterait','ecouteraient','ecouta','ecouterent','parle','parlent','parlait','parlaient',
    'parlera','parleront','parlerait','parleraient','parla','parlerent','joue','jouent','jouait',
    'jouaient','jouera','joueront','jouerait','joueraient','joua','jouerent','aime','aiment',
    'aimait','aimaient','aimera','aimeront','aimerait','aimeraient','aima','aimerent','quitte',
    'quittent','quittait','quittaient','quittera','quitteront','quitterait','quitteraient',
    'quitta','quitterent','habite','habitent','habitait','habitaient','habitera','habiteront',
    'habiterait','habiteraient','habita','habiterent','monte','montent','montait','montaient',
    'montera','monteront','monterait','monteraient','monta','monterent','entre','entrent',
    'entrait','entraient','entrera','entreront','entrerait','entreraient','entra','entrerent',
    'rentre','rentrent','rentrait','rentraient','rentrera','rentreront','rentrerait',
    'rentreraient','rentra','rentrerent','tombe','tombent','tombait','tombaient','tombera',
    'tomberont','tomberait','tomberaient','tomba','tombèrent','arrive','arrivent','arrivait',
    'arrivaient','arrivera','arriveront','arriverait','arriveraient','arriva','arriverent',
    'retourne','retournent','retournait','retournaient','retournera','retourneront','retournerait',
    'retourneraient','retourna','retournerent','tourne','tournent','tournait','tournaient',
    'tournera','tourneront','tournerait','tourneraient','tourna','tournerent','dure','durent',
    'durait','duraient','durera','dureront','durerait','dureraient','dura','durerent','compte',
    'comptent','comptait','comptaient','comptera','compteront','compterait','compteraient',
    'compta','compterent','raconte','racontent','racontait','racontaient','racontera',
    'raconteront','raconterait','raconteraient','raconta','raconterent','montre','montrent',
    'montrait','montraient','montrera','montreront','montrerait','montreraient','montra',
    'montrerent','demande','demandent','demandait','demandaient','demandera','demanderont',
    'demanderait','demanderaient','demanda','demanderent','garde','gardent','gardait','gardaient',
    'gardera','garderont','garderait','garderaient','garda','garderent','commande','commandent',
    'commandait','commandaient','commandera','commanderont','commanderait','commanderaient',
    'commanda','commanderent','repond','repondent','repondait','repondaient','repondra',
    'repondront','repondrait','repondraient','repondit','repondirent','defend','defendent',
    'defendait','defendaient','defendra','defendront','defendrait','defendraient','defendit',
    'defendirent','attend','attendent','attendait','attendaient','attendra','attendront',
    'attendrait','attendraient','attendit','attendirent','entend','entendent','entendait',
    'entendaient','entendra','entendront','entendrait','entendraient','entendit','entendirent',
    'pretend','pretendent','pretendait','pretendaient','pretendra','pretendront','pretendrait',
    'pretendraient','pretendit','pretendirent','rend','rendent','rendait','rendaient','rendra',
    'rendront','rendrait','rendraient','rendit','rendirent','vend','vendent','vendait',
    'vendaient','vendra','vendront','vendrait','vendraient','vendit','vendirent','perd',
    'perdent','perdait','perdaient','perdra','perdront','perdrait','perdraient','perdit',
    'perdirent','mord','mordent','mordait','mordaient','mordra','mordront','mordrait',
    'mordraient','mordit','mordirent','tord','tordent','fend','fendent','etend','etendent',
    'etendait','etendaient','etendra','etendront','etendrait','etendraient','etendit',
    'etendirent','depend','dependent','dependait','dependaient','dependra','dependront',
    'dependrait','dependraient','dependit','dependirent','descend','descendent','descendait',
    'descendaient','descendra','descendront','descendrait','descendraient','descendit',
    'descendirent','confond','confondent','repand','repandent','ecrit','ecrivent','ecrivait',
    'ecrivaient','ecrira','ecriront','ecrirait','ecriraient','ecrive','ecrivit','ecrivirent',
    'decrit','decrivent','lit','lisent','lisait','lisaient','lira','liront','lirait','liraient',
    'lise','lut','lurent','boit','boivent','buvait','buvaient','boira','boiront','boirait',
    'boiraient','boive','but','burent','plait','plaisent','plaisait','plaisaient','plaira',
    'plairont','plairait','plairaient','plaise','plut','plurent','tait','taisent','conclut',
    'conduit','conduisent','conduisait','conduisaient','conduira','conduiront','conduirait',
    'conduiraient','conduise','conduisit','conduisirent','construit','construisent','detruit',
    'detruisent','produit','produisent','produisait','produisaient','produira','produiront',
    'produirait','produiraient','produise','produisit','produisirent','reduit','reduisent',
    'seduit','seduisent','traduit','traduisent','traduisait','traduisaient','traduira',
    'traduiront','traduirait','traduisent','introduit','introduisent','cuit','luisent','nuit',
    'nuisent','rit','rient','riait','riaient','rira','riront','rirait','riraient','rie',
    'sourit','sourient','suffit','suffisent','suffisait','suffisaient','suffira','suffiront',
    'suffirait','suffiraient','suffise','fuit','fuient','fuyait','fuyaient','fuira','fuiront',
    'fuirait','fuiraient','fuie','poursuit','poursuivent','survit','survivent','dort','dorment',
    'dormait','dormaient','dormira','dormiront','dormirait','dormiraient','dorme','ment',
    'mentent','mentait','mentaient','mentira','mentiront','mentirait','mentiraient','mente',
    'court','courent','courait','couraient','courra','courront','courrait','courraient','coure',
    'courut','coururent','rit2')

# ---- corpus load ----
files = sorted(f for f in os.listdir(CORPUS)
               if f.endswith('.txt') and not f.startswith('PROVENANCE')
               and not f.startswith(EXCLUDE))
print(f'{len(files)} files', flush=True)

tok_after_det = Counter()
tok_after_subjpron = Counter()   # verb-position heuristic
total_tokens = 0
total_chars = 0
seqs = []  # (fname, tokens, raw_text)
for fn in files:
    p = os.path.join(CORPUS, fn)
    raw = open(p, encoding='utf-8', errors='replace').read()
    total_chars += len(raw)
    toks = TOK.findall(norm_apos(raw).lower())
    total_tokens += len(toks)
    seqs.append((fn, toks, raw))
    for i, t in enumerate(toks):
        if i == 0:
            continue
        prev = toks[i-1]
        if prev in DET:
            tok_after_det[t] += 1
        if prev in ('il', 'elle', 'ils', 'elles', 'on', 'qui', 'ce', "c'", "qu'"):
            tok_after_subjpron[t] += 1

# noun lexicon: follows determiner >=5x, minus function words
nouns = {t for t, c in tok_after_det.items()
         if c >= 5 and t not in FUNCTION_STOP and len(t) > 2}
# exclude elided-determiner tokens: apostrophe-preserving tokenization keeps
# "l'étude"/"d'habitude" as single tokens -- the article is INSIDE the token,
# so these are not bare even though PREV is not a determiner
de_nouns = sorted(t for t in nouns
                  if t.endswith('de') and not t.endswith('des') and "'" not in t)
de_nouns_set = set(de_nouns)
print(f'noun lexicon: {len(nouns)}; -de-final singular nouns: {len(de_nouns)}', flush=True)

# verb-position heuristic set: follows subject pronoun >=3x, minus function words
verbpos = {t for t, c in tok_after_subjpron.items()
           if c >= 3 and t not in FUNCTION_STOP and len(t) > 2}
V = FINITE | verbpos
print(f'finite list: {len(FINITE)} curated + {len(verbpos)} heuristic = {len(V)}', flush=True)

# ---- candidate extraction ----
ELIDED = ("l'", "d'", "c'", "s'", "j'", "m'", "t'", "n'", "qu'")
def is_bare(i, toks):
    """True iff the noun at toks[i] carries no determiner: no DET in the 3
    preceding tokens (covers 'le seul remede'), no elided-article token
    (l'/d'-prefixed) in the 2 preceding ('l'arriere-garde', 'l'unique remede'),
    and immediate prev not a preposition/pronoun/determiner."""
    prev = toks[i-1]
    if prev in BARE_BLOCK_PREV or prev[0].isdigit():
        return False
    if any(toks[j] in DET for j in range(max(0, i-3), i)):
        return False
    if any(toks[j].startswith(ELIDED) for j in range(max(0, i-2), i)):
        return False
    return True

cands = []   # dicts with file, idx, prev, noun, verb, source
base_det = 0  # baseline: DET + NOUN-de + V (determined subjects, for scale)
for fn, toks, raw in seqs:
    for i in range(1, len(toks) - 1):
        t = toks[i]
        if t not in de_nouns_set:
            continue
        nxt = toks[i+1]
        if nxt not in V:
            continue
        prev = toks[i-1]
        if prev in DET:
            base_det += 1
            continue
        if not is_bare(i, toks):
            continue
        # skip hyphen-split artifacts
        cands.append({'file': fn, 'idx': i, 'prev': prev, 'noun': t,
                      'verb': nxt, 'verb_source': 'curated' if nxt in FINITE else 'heuristic'})

print(f'bare candidates: {len(cands)}; determined baseline (DET+NOUN-de+V): {base_det}', flush=True)
print(f'total tokens: {total_tokens}; total chars: {total_chars}', flush=True)

# attach raw-text context (~140 chars around token char position)
def char_context(raw, toks_target_idx_note):
    return None

# map token index -> char offset via re-scan (only for candidate files)
out = []
for c in cands:
    fn = c['file']
    raw = next(r for f, t, r in seqs if f == fn)
    # find char offsets by scanning tokens
    offs = []
    for m in TOK.finditer(norm_apos(raw)):
        offs.append(m.start())
        if len(offs) > c['idx'] + 6:
            break
    start = offs[c['idx']] if c['idx'] < len(offs) else 0
    ctx = raw[max(0, start-90): start+110].replace('\n', ' ')
    out.append({**c, 'context': ' '.join(ctx.split())})

json.dump({'meta': {'files': len(files), 'tokens': total_tokens, 'chars': total_chars,
                    'de_nouns': len(de_nouns), 'candidates': len(cands),
                    'determined_baseline': base_det},
           'de_noun_inventory': de_nouns,
           'candidates': out},
          open(os.path.join(OUTDIR, 'bare-subj-corpus_census.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('wrote bare-subj-corpus_census.json', flush=True)
