#!/usr/bin/env python3
"""Corpus test: bare-noun rate after gerund 'en [V]ant' in the 1841 period corpus.

For each 'en <Xant>' window, take the immediately following word token and
classify it as: determined / bare / proper-noun / non-nominal (verb, adverb,
pronoun, punctuation, preposition...). Reports rate of bare nouns among the
nominal slots.
"""
import json, os, re, unicodedata

CORP = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
OUT = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd17/next-token/58-det-gap_census.json")

DETS = {
    # articles / determiners
    "le", "la", "les", "l'", "l’", "un", "une", "des", "du", "de", "d'", "d’",
    "au", "aux", "ce", "cet", "cette", "ces",
    "mon", "ma", "mes", "ton", "ta", "tes", "son", "sa", "ses",
    "notre", "nos", "votre", "vos", "leur", "leurs",
    "quelque", "quelques", "chaque", "plusieurs", "certain", "certaine",
    "certains", "certaines", "tel", "telle", "tels", "telles", "tout", "toute",
    "tous", "toutes", "aucun", "aucune", "nul", "nulle", "même", "mêmes",
    "autre", "autres", "plus", "moins", "peu",
    # numerals
    "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix",
    "premier", "première", "second", "seconde",
}
ADVS = {
    "ainsi", "ici", "là", "bien", "mal", "mieux", "beaucoup", "trop", "trop",
    "très", "toujours", "jamais", "souvent", "parfois", "partout", "ailleurs",
    "enfin", "toutefois", "cependant", "néanmoins", "pourtant", "or",
    "aujourd'hui", "aujourd’hui", "hier", "demain", "alors", "seulement",
    "aussi", "également", "volontiers", "aisément", "facilement",
    "difficilement", "soudain", "soudainement", "subitement", "bientôt",
    "déjà", "encore", "ne", "non", "pas", "point", "guère", "aucunement",
    "présentement", "actuellement", "maintenant", "jadis", "autrefois",
    "lentement", "vite", "rapidement", "doucement", "ferme", "fort", "haut",
    "bas", "loin", "près", "devant", "derrière", "dessus", "dessous",
    "dedans", "dehors", "ensemble", "séparément", "respectivement",
    "successivement", "graduellement", "insensiblement", "incessamment",
    "naturellement", "nécessairement", "certainement", "assurément",
    "vraiment", "effectivement", "réellement", "évidemment", "surtout",
    "principalement", "ordinairement", "habituellement", "ordinairement",
    "communément", "généralement", "particulièrement", "notamment",
    "uniquement", "simplement", "purement", "franchement", "ouvertement",
    "publiquement", "secrètement", "personnellement", "mutuellement",
    "réciproquement", "simultanément", "immédiatement", "aussitôt",
    "incontinent", "tout", "tellement", "si", "tant", "combien",
}
FROZEN_PAIRS = {
    # (gerund_stem, next_word): frozen collocations where the noun is not a
    # free bare-noun complement
    ("prenant", "possession"), ("prenant", "congé"), ("prenant", "connaissance"),
    ("rendant", "compte"), ("rendant", "hommage"), ("rendant", "justice"),
    ("faisant", "allusion"), ("mettant", "fin"), ("tenant", "compte"),
    ("flagrant", "délit"),
}
# note: 'flagrant' is not a gerund-host; the 'en flagrant délit' shape is frozen

PRONS_ELIDED = {"elle", "elles", "lui", "eux", "elles", "moi", "toi", "soi",
                "nous", "vous", "en"}
PRONS = {
    "je", "tu", "il", "elle", "nous", "vous", "ils", "elles", "on",
    "me", "te", "se", "lui", "leur", "y", "en", "moi", "toi", "soi",
    "qui", "que", "quoi", "dont", "où", "celui", "celle", "ceux", "celles",
    "ceci", "cela", "ça", "ci", "là", "tout", "rien", "personne",
}
PREPS = {"à", "de", "dans", "sur", "sous", "par", "pour", "avec", "sans", "entre",
         "chez", "vers", "contre", "pendant", "après", "avant", "durant", "malgré",
         "envers", "auprès", "hormis", "outre", "sauf", "selon"}
CONJS = {"et", "ou", "ni", "mais", "or", "donc", "car", "que", "qu", "comme",
         "si", "lorsque", "quand", "parce", "puisque", "afin", "tandis"}

# 'en' + <xant>: require lowercase present-participle shape; exclude known
# non-participle -ant words is impractical, so record and spot-check.
GERUND = re.compile(r"\ben\s+([a-zàâäéèêëîïôöùûüç]+ant)\b", re.IGNORECASE)
TOK = re.compile(r"[A-Za-zÀÂÄÉÈÊËÎÏÔÖÙÛÜÇàâäéèêëîïôöùûüç]+(?:['’][A-Za-zÀÂÄÉÈÊËÎÏÔÖÙÛÜÇàâäéèêëîïôöùûüç]+)?")

def files():
    out = []
    for root, _, fs in os.walk(CORP):
        for f in fs:
            if f.endswith(".txt") and f != "PROVENANCE.md":
                out.append(os.path.join(root, f))
    return sorted(out)

def classify(gerund, nxt):
    """Returns (class, note)."""
    low = nxt.lower()
    # elided heads: normalize l'/d'/c'/j'/s' + word
    for head in ("l'", "d'", "c'", "j'", "s'", "qu'", "m'", "t'"):
        if low.startswith(head):
            rest = low[len(head):]
            if head == "l'":
                return "determined", nxt
            if head == "d'":
                if rest in {"un", "une", "des"}:
                    return "determined", nxt
                if rest in PRONS_ELIDED:
                    return "non-nominal", nxt
                if rest in {"abord", "avance"}:
                    return "non-nominal-frozen", nxt
                return "non-nominal-prep", nxt  # en Xant d'Y: PP, not bare-N slot
            # c'/j'/s'/m'/t'/qu' + word: clause/verb chunk
            return "non-nominal", nxt
    if low in DETS:
        return "determined", nxt
    if low in ADVS:
        return "non-nominal-adverb", nxt
    if low in PRONS or low in PREPS or low in CONJS:
        return "non-nominal", nxt
    if low.endswith("ant") or low.endswith("ent"):
        return "non-nominal-participle", nxt
    if low.endswith("er") or low.endswith("ir") or low.endswith("re"):
        return "non-nominal-infinitive", nxt
    if (gerund.lower(), low) in FROZEN_PAIRS:
        return "non-nominal-frozen", nxt
    if nxt[0].isupper():
        return "proper-noun", nxt
    return "bare", nxt

hits = []
total_chars = 0
files_scanned = 0
for path in files():
    text = open(path, encoding="utf-8", errors="replace").read()
    text = text.replace("’", "'").replace("‘", "'")
    total_chars += len(text)
    files_scanned += 1
    for m in GERUND.finditer(text):
        ger = m.group(1)
        if ger[0].isupper():
            continue  # 'En <Ant...>' sentence-initial + name noise; exclude
        # following token
        rest = text[m.end():m.end() + 80]
        tm = TOK.match(rest.lstrip(" \t"))
        cls = "none"
        nxt = ""
        if tm:
            nxt = tm.group(0)
            cls, _ = classify(ger, nxt)
        else:
            cls, nxt = "punct", rest[:1]
        start_line = text.count("\n", 0, m.start()) + 1
        hits.append({"file": os.path.basename(path), "line": start_line,
                     "gerund": ger, "next": nxt, "class": cls,
                     "ctx": text[max(0, m.start() - 60):m.end() + 60].replace("\n", " ")})

with open(OUT, "w") as f:
    json.dump({"corpus_chars": total_chars, "files": files_scanned,
               "windows": hits}, f, ensure_ascii=False)

from collections import Counter
c = Counter(h["class"] for h in hits)
print("files:", files_scanned, "chars:", total_chars, "windows:", len(hits))
print(dict(c))
