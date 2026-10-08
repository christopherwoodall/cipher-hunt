#!/usr/bin/env python3
"""A4 classification: per-L1 class assignment for the 191 'de ce que' tokens.
Absolute tokens (8, cross-sentence L1) excluded from the class census.
Artifact sets per PREREG.md; post-hoc extensions disclosed in analysis (c).
"""
import json
from collections import Counter
from pathlib import Path

d = json.load(open(Path.home() /
    'workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd14/battery48/a74_raw.json'))
hits = d['A4']['hits']
assert len(hits) == 191

LEX = {
 # --- pre-registered ART_MOD (non-governing modifiers/conjunctions/negation)
 'et':'artifact', 'surtout':'artifact', 'aussi':'artifact', 'enfin':'artifact',
 'exactement':'artifact', 'seulement':'artifact', 'pas':'artifact',
 'autres':'artifact', 'même':'artifact',
 # --- vocatives (pre-registered ART_VOC)
 'roi':'noun', 'majesté':'noun',          # (a): noun; (b): excluded
 # --- nouns
 'contraire':'noun', 'delà':'noun', 'exemple':'noun', 'compte':'noun',
 'partie':'noun', 'appui':'noun', 'courant':'noun', 'rancune':'noun',
 'besoin':'noun', 'jouissance':'noun', 'raison':'noun', 'inquiétude':'noun',
 'humeur':'noun', 'mesure':'noun', 'regrets':'noun', 'moitie':'noun',
 'ensemble':'noun', 'face':'noun', 'responsabilite':'noun', 'égard':'noun',
 'fegard':'noun', 'pégard':'noun', 'monstration':'noun', 'acte':'noun',
 'quietude':'noun', 'justification':'noun', 'recherche':'noun', 'moyen':'noun',
 'utilitö':'noun', 'dessus':'noun', 'dessous':'noun', 'confirmation':'noun',
 'gré':'noun', 'souvenirs':'noun', 'fin':'noun', 'fois':'noun', 'bout':'noun',
 'sentiment':'noun', 'nouvelles':'noun', 'monde':'noun', 'déclaration':'noun',
 'cause':'noun', 'étonnement':'noun', 'secret':'noun', 'explication':'noun',
 'confidence':'noun', 'image':'noun', 'déduction':'noun', 'voie':'noun',
 'mot':'noun', 'preuves':'noun', 'idée':'noun', 'double':'noun', 'preuve':'noun',
 'métier':'noun', 'ciel':'noun', 'plume':'noun', 'oubli':'noun',
 'surprise':'noun', 'nature':'noun', 'historique':'noun',
 # --- adjectives
 'exact':'adjective', 'honteux':'adjective', 'curieux':'adjective',
 'inquiets':'adjective', 'inquiet':'adjective', 'irrécusable':'adjective',
 'contente':'adjective', 'différent':'adjective', 'claire':'adjective',
 'vraie':'adjective', 'exacte':'adjective', 'unique':'adjective',
 'vif':'adjective', 'politique':'adjective', 'süffisante':'adjective',
 'reconnaissant':'adjective', 'monstrueuse':'adjective',
 # --- participles (past, verbal force)
 'peinee':'participle', 'piqué':'participle', 'blessé':'participle',
 'dit':'participle', 'surpris':'participle', 'formalisés':'participle',
 'surchargées':'participle',
 # --- verbs (finite / reflexive / present participle with verbal force)
 'plaindre':'verb', 'plaint':'verb', 'félicite':'verb', 'feliciter':'verb',
 'cite':'verb', 'souvenait':'verb', 'souvient':'verb', 'contenter':'verb',
 'eloigner':'verb', 'rendre':'verb', 'souffrir':'verb', 'repentir':'verb',
 'vais':'verb', 'voit':'verb', 'touche':'verb', 'résulte':'verb',
 'provint':'verb', 'provenait':'verb', 'venait':'verb', 'vient':'verb',
 'dépendent':'verb', 'ressort':'verb', 'mer':'verb', 'répondant':'verb',
 'parlant':'verb', 'profitant':'verb', 'indigne':'verb',
 # --- pronouns
 'rien':'pronoun', 'ceux':'pronoun', 'unes':'pronoun',
 # --- post-hoc artifacts (mis-extracted governors / OCR garble / adverbs)
 'doute':'artifact', 'peu':'artifact', 'haut':'artifact', 'fort':'artifact',
 'moins':'artifact', 'plus':'artifact', 'bien':'artifact', 'aussitôt':'artifact',
 'ici':'artifact', 'sus':'artifact', 'an':'artifact', 'ieu':'artifact',
 'comnie':'artifact', 'petersbourg':'artifact', 'marie':'artifact',
 'que':'artifact', 'on':'artifact',
 # --- missed in first pass
 'egard':'noun', 'mérite':'verb', 'courrier':'noun', 'auprès':'noun',
 'oppose':'noun', 'pant':'artifact',
}
NOTES = {
 'mer': "OCR 's'alarmer' split by tokenizer -> verb",
 'répondant': "present participle, 'répondre de' governs",
 'parlant': "present participle 'en parlant de'",
 'profitant': "present participle, odd context",
 'indigne': "'s'indigner de' pronominal verb",
 'vient': "'venir de ce que' = it comes from what (nominal ce que)",
 'politique': "'une saine politique de ce que' - adj. reading, uncertain",
 'historique': "'l'historique' noun (the historical account)",
 'ressort': "'qui ressort de' verb (ressortir), ambiguous w/ noun",
 'doute': "post-hoc: 'sans doute' parenthetical, governor='plaindra'",
 'haut': "post-hoc: adverb, governor='alarmer'",
 'fort': "post-hoc: adverb, governor='occupe'",
 'moins': "post-hoc: adverb, governor='informe'",
 'plus': "post-hoc: adverb",
 'bien': "post-hoc: adverb, governor='souvenez'",
 'aussitôt': "post-hoc: adverb, governor='avisa'",
 'ici': "post-hoc: adverb",
 'sus': "post-hoc: 'en sus' adverbial",
 'an': "post-hoc: OCR garble, unclassifiable",
 'ieu': "post-hoc: OCR garble",
 'comnie': "post-hoc: OCR garble",
 'petersbourg': "post-hoc: proper noun, cross-phrase",
 'marie': "post-hoc: proper noun, governor='plaindre'",
 'que': "post-hoc: conjunction",
 'on': "post-hoc: subject pronoun, governor='avait'",
 'peu': "post-hoc: 'peu à peu' adverbial",
 'russie': "absolute token, excluded from census",
 'cela': "absolute token, excluded from census",
 'oui': "absolute token, excluded from census",
 'lui': "absolute token, excluded from census",
 'possible': "absolute token, excluded from census",
 'soulignés': "absolute token, excluded from census",
 'conseils': "absolute token, excluded from census",
}

ART_MOD = {'et','aussi','surtout','enfin','exactement','seulement','pas','autres','même'}
ART_VOC = {'roi','majesté'}
POSTHOC_ART = {'doute','peu','haut','fort','moins','plus','bien','aussitôt','ici',
               'sus','an','ieu','comnie','petersbourg','marie','que','on'}

unlexed = set()
rows = []
for h in hits:
    l1 = h['L1']
    if h['absolute']:
        rows.append((h, 'absolute'))
        continue
    if l1 not in LEX:
        unlexed.add(l1)
    rows.append((h, LEX.get(l1, 'UNLEXED')))
assert not unlexed, unlexed

gov = [(h, cls) for h, cls in rows if cls != 'absolute']
print("absolute excluded:", sum(1 for _, c in rows if c == 'absolute'))
print("governor tokens:", len(gov))

def shares(pred):
    sel = [(h, c) for h, c in gov if pred(h, c)]
    tot = len(sel)
    cc = Counter(c for _, c in sel)
    return tot, {k: (v, round(v/tot, 4)) for k, v in cc.most_common()}

# (a) exclude pre-registered ART_MOD only
tot_a, sh_a = shares(lambda h, c: h['L1'] not in ART_MOD)
# (b) exclude ART_MOD + ART_VOC
tot_b, sh_b = shares(lambda h, c: h['L1'] not in ART_MOD and h['L1'] not in ART_VOC)
# (c) sensitivity: also exclude post-hoc artifacts
tot_c, sh_c = shares(lambda h, c: h['L1'] not in ART_MOD and h['L1'] not in ART_VOC
                     and h['L1'] not in POSTHOC_ART)

for name, (tot, sh) in [('(a) mod-excluded', (tot_a, sh_a)),
                        ('(b) mod+voc-excluded', (tot_b, sh_b)),
                        ('(c) +posthoc-excluded', (tot_c, sh_c))]:
    print(f"\n{name}: n={tot}")
    for k, (v, s) in sh.items():
        print(f"  {k:11s} {v:3d}  {s:.1%}")
    dom = max(sh.items(), key=lambda kv: kv[1][1])
    print(f"  dominant: {dom[0]} {dom[1][1]:.1%}  (>=70%: {dom[1][1] >= 0.70})")

# per-class genuine counts for A4-neg (74's pinned class, if any)
out = {"n_total": 191, "n_absolute": 8, "n_governor": len(gov),
       "analyses": {
         "a": {"n": tot_a, "shares": {k: v[1] for k, v in sh_a.items()},
               "counts": {k: v[0] for k, v in sh_a.items()}},
         "b": {"n": tot_b, "shares": {k: v[1] for k, v in sh_b.items()},
               "counts": {k: v[0] for k, v in sh_b.items()}},
         "c": {"n": tot_c, "shares": {k: v[1] for k, v in sh_c.items()},
               "counts": {k: v[0] for k, v in sh_c.items()}}},
       "notes": NOTES}
Path("classify_a4.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print("\nwrote classify_a4.json")
