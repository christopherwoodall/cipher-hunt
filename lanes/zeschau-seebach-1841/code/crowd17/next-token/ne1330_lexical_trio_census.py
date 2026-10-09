#!/usr/bin/env python3
"""Battery ne-1330-lexical-trio: targeted bare-'ne' + prescrire/preserver/prevoir census.

Searches one or more corpora for bare "ne"/"n'" directly governing the three
cipher-candidate verbs (any tense), then emits every hit with sentence context
for hand-classification.

Methodology fixes vs v1:
- curly apostrophes (U+2019 etc.) normalized to ASCII before tokenizing
- ne/n' detected on accent-PRESERVING lowercase ('né' participle != 'ne')
- partners extended: 'mot' (ne...mot), 'aucunement', 'nulle part' bigram
- whitespace-normalized search per the lane's standing corpus-zero rule

Usage: python3 ne1330_lexical_trio_census.py <corpus_dir> <out_prefix>
"""
import json, os, re, sys, unicodedata

CORPUS_DIR = sys.argv[1]
OUT_PREFIX = sys.argv[2]

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def norm_apos(s):
    return re.sub(r"[‘’ʼ`´]", "'", s)

def ka_low(s):
    """Lowercase preserving accents (for ne/n' detection)."""
    return norm_apos(s).lower()

def sa_low(s):
    """Lowercase, accents stripped (for verb-form matching)."""
    return strip_accents(norm_apos(s)).lower()

# ---- conjugated forms (matched accent-insensitively) ----
def forms_1er(stem, fut_stem=None):
    f = fut_stem or (stem + 'er')
    return [stem+'e', stem+'es', stem+'ons', stem+'ez', stem+'ent',
            stem+'ais', stem+'ait', stem+'ions', stem+'iez', stem+'aient',
            stem+'ai', stem+'as', stem+'a', stem+'ames', stem+'ates', stem+'erent',
            f+'ai', f+'as', f+'a', f+'ons', f+'ez', f+'ont',
            f+'ais', f+'ait', f+'ions', f+'iez', f+'aient']

prescrire = ['prescris','prescrit','prescrivons','prescrivez','prescrivent',
 'prescrivais','prescrivait','prescrivions','prescriviez','prescrivaient',
 'prescrivis','prescrivit','prescrivimes','prescrivites','prescrivirent',
 'prescrirai','prescriras','prescrira','prescrirons','prescrirez','prescriront',
 'prescrirais','prescrirait','prescririons','prescririez','prescriraient',
 'prescrive','prescrives','prescrivions','prescriviez','prescrivent',
 'prescrit','prescrits','prescrite','prescrites']
preserver = forms_1er('preserv')
prevoir = ['prevois','prevoit','prevoyons','prevoyez','prevoient',
 'prevoyais','prevoyait','prevoyions','prevoyiez','prevoyaient',
 'previs','previt','previmes','prevites','previrent',
 'prevoirai','prevoiras','prevoira','prevoirons','prevoirez','prevoiront',
 'prevoirais','prevoirait','prevoirions','prevoiriez','prevoiraient',
 'prevoie','prevoies','prevoyions','prevoyiez','prevoient',
 'prevu','prevus','prevue','prevues']

TRIO = {'prescrire': set(prescrire), 'preserver': set(preserver), 'prevoir': set(prevoir)}
FORM2LEMMA = {}
for lem, fs in TRIO.items():
    for f in fs:
        FORM2LEMMA[sa_low(f)] = lem

# clitics that may intervene between ne and the finite verb
CLITICS = {'le','la','les','lui','leur','me','te','se','nous','vous','en','y',
           "m'","t'","s'","l'","d'","qu'","m","t","s","l","d","qu"}
PARTNERS = {'pas','point','que',"qu'","qu","ni",'jamais','plus','rien','personne',
            'aucun','aucune','guere','mie','goutte','nullement','aucunement','mot'}

def sentences(text):
    t = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)   # unwrap line-wrapped prose
    t = re.sub(r'[ \t]+', ' ', t)
    parts = re.split(r'[.!?…;:]+', t)
    return [p.strip() for p in parts if p.strip()]

def toks_of(s):
    return re.findall(r"[A-Za-zÀ-ÿ']+", norm_apos(s))

def find_trio_hits(sent):
    hits = []
    toks = toks_of(sent)
    ka = [ka_low(x) for x in toks]
    low = [sa_low(x) for x in toks]
    for i, w in enumerate(ka):
        if w == 'ne' or w == "n'":
            j = i + 1
            skipped = 0
            while j < len(low) and low[j] in CLITICS and skipped < 3:
                j += 1; skipped += 1
            if j < len(low) and low[j] in FORM2LEMMA:
                hits.append((toks[i], toks[j], FORM2LEMMA[low[j]],
                             ' '.join(toks[max(0,i-8):j+8])))
    return hits

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

trio_hits, trio_bare = [], []
total_chars = 0
files = sorted(f for f in os.listdir(CORPUS_DIR) if f.endswith('.txt') and not f.startswith('PROVENANCE'))
for fn in files:
    with open(os.path.join(CORPUS_DIR, fn), encoding='utf-8', errors='replace') as fh:
        text = fh.read()
    total_chars += len(text)
    for s in sentences(text):
        for ne_t, vf, lem, win in find_trio_hits(s):
            rec = {'file': fn, 'ne': ne_t, 'form': vf, 'lemma': lem,
                   'partner': has_partner(s), 'window': win, 'sentence': s[:400]}
            trio_hits.append(rec)
            if not rec['partner']:
                trio_bare.append(rec)

json.dump({'corpus': CORPUS_DIR, 'chars': total_chars, 'files': len(files),
           'trio_hits_all': trio_hits, 'trio_bare': trio_bare},
          open(OUT_PREFIX + '_trio.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('chars:', total_chars, 'files:', len(files))
print('trio hits (any):', len(trio_hits), ' bare:', len(trio_bare))
for h in trio_bare:
    print('BARE:', h['file'], '|', h['lemma'], h['form'], '|', h['window'][:120])
