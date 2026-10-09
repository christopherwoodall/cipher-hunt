#!/usr/bin/env python3
"""Battery ne-1330-lexical-trio, C2 arm: verb-lexicon distribution of bare-'ne'
strict candidates in the modern Europarl French control corpus.

Extracts every "ne"/"n'" + (0-3 clitics) + head-word instance, keeps the bare
(no strict-tier partner) ones, auto-classifies the head word against the
licensed 7-verb form sets + idiom buckets, and dumps the "other" bucket plus a
random sample for hand-audit.

Methodology: curly apostrophes normalized; ne/n' on accent-preserving
lowercase ('né' != 'ne'); partners extended with 'mot', 'aucunement',
'nulle part' bigram.
"""
import json, re, sys, unicodedata, random

CORPUS_FILE = sys.argv[1]   # one sentence per line
OUT_PREFIX = sys.argv[2]

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def norm_apos(s):
    return re.sub(r"[‘’ʼ`´]", "'", s)

def ka_low(s):
    return norm_apos(s).lower()

def sa_low(s):
    return strip_accents(norm_apos(s)).lower()

def set1(stem, fut_stem=None):
    f = fut_stem or (stem + 'er')
    return {stem+'e', stem+'es', stem+'ons', stem+'ez', stem+'ent',
            stem+'ais', stem+'ait', stem+'ions', stem+'iez', stem+'aient',
            stem+'ai', stem+'as', stem+'a', stem+'ames', stem+'ates', stem+'erent',
            f+'ai', f+'as', f+'a', f+'ons', f+'ez', f+'ont',
            f+'ais', f+'ait', f+'ions', f+'iez', f+'aient'}

LICENSED = {
 'pouvoir': {'puis','peux','peut','pouvons','pouvez','peuvent','pouvais','pouvait','pouvions','pouviez','pouvaient',
             'pus','put','pumes','putes','purent','pourrai','pourras','pourra','pourrons','pourrez','pourront',
             'pourrais','pourrait','pourrions','pourriez','pourraient','puisse','puisses','puissions','puissiez','puissent'},
 'savoir': {'sais','sait','savons','savez','savent','savais','savait','savions','saviez','savaient',
            'sus','sut','sumes','sutes','surent','saurai','sauras','saura','saurons','saurez','sauront',
            'saurais','saurait','saurions','sauriez','sauraient','sache','saches','sachions','sachiez','sachent'},
 'oser': set1('os'),
 'cesser': set1('cess'),
 'falloir': {'faut','fallait','fallut','faudra','faudrait','faille'},
 'vouloir': {'veux','veut','voulons','voulez','veulent','voulais','voulait','voulions','vouliez','voulaient',
             'voulus','voulut','voulumes','voulutes','voulurent','voudrai','voudras','voudra','voudrons','voudrez','voudront',
             'voudrais','voudrait','voudrions','voudriez','voudraient','veuille','veuilles','veuillons','veuillez','veuillent'},
 'devoir': {'dois','doit','devons','devez','doivent','devais','devait','devions','deviez','devaient',
            'dus','dut','dumes','dutes','durent','devrai','devras','devra','devrons','devrez','devront',
            'devrais','devrait','devrions','devriez','devraient','doive','doives','devions','deviez','doivent'},
}
FORM2LEMMA = {}
for lem, fs in LICENSED.items():
    for f in fs:
        FORM2LEMMA.setdefault(sa_low(f), lem)
IDIOM_FORMS = {'importe','importent','eut','eusses','eussions','eussiez','eussent',
               'fut','fusse','fusses','fussions','fussiez','fussent'}

CLITICS = {'le','la','les','lui','leur','me','te','se','nous','vous','en','y',
           "m'","t'","s'","l'","d'","qu'"}
PARTNERS = {'pas','point','que',"qu'","qu",'ni','jamais','plus','rien','personne',
            'aucun','aucune','guere','mie','goutte','nullement','aucunement','mot'}

def toks_of(s):
    return re.findall(r"[A-Za-zÀ-ÿ']+", norm_apos(s))

def has_partner(sent):
    low = [sa_low(x) for x in toks_of(sent)]
    for i, w in enumerate(low):
        if w in PARTNERS:
            return True
        if w.startswith("qu'") or w == "qu":
            return True
        if w == 'nulle' and i + 1 < len(low) and low[i+1] == 'part':
            return True
    return False

cands = []
total_ne = 0
with open(CORPUS_FILE, encoding='utf-8', errors='replace') as fh:
    for line in fh:
        s = line.strip()
        if not s:
            continue
        toks = toks_of(s)
        ka = [ka_low(x) for x in toks]
        low = [sa_low(x) for x in toks]
        for i, w in enumerate(ka):
            if w == 'ne' or w == "n'":
                total_ne += 1
                j = i + 1; skipped = 0
                while j < len(low) and low[j] in CLITICS and skipped < 3:
                    j += 1; skipped += 1
                if j >= len(low):
                    continue
                head = toks[j]
                if not has_partner(s):
                    cands.append({'head': head, 'head_sa': sa_low(head), 'ne': toks[i],
                                  'sent': s[:350]})

def classify(head_sa):
    if head_sa in FORM2LEMMA:
        return ('licensed', FORM2LEMMA[head_sa])
    if head_sa in IDIOM_FORMS:
        return ('idiom', head_sa)
    return ('other', None)

buckets = {'licensed': [], 'idiom': [], 'other': []}
for c in cands:
    b, lem = classify(c['head_sa'])
    c['bucket'] = b; c['lemma'] = lem
    buckets[b].append(c)

random.seed(1330)
sample_licensed = random.sample(buckets['licensed'], min(60, len(buckets['licensed'])))

json.dump({'corpus': CORPUS_FILE, 'ne_instances': total_ne,
           'bare_candidates': len(cands),
           'n_licensed': len(buckets['licensed']), 'n_idiom': len(buckets['idiom']),
           'n_other': len(buckets['other']),
           'other': buckets['other'], 'sample_licensed': sample_licensed},
          open(OUT_PREFIX + '_lexclass.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('ne instances:', total_ne)
print('bare candidates:', len(cands))
print('licensed:', len(buckets['licensed']), 'idiom:', len(buckets['idiom']), 'other:', len(buckets['other']))
from collections import Counter
print(Counter(c['head_sa'] for c in buckets['other']).most_common(30))
