#!/usr/bin/env python3
"""Triage bare-'pas' candidates into classes; extract prime audit set."""
import json, re
from collections import Counter

IN = "code/crowd17/next-token/pasbare_candidates.json"
OUT = "code/crowd17/next-token/pasbare_triage.json"

DET_LIKE = {"non","un","une","le","la","les","des","de","du","ses","mes","tes","ces",
    "premier","premiers","grand","petit","chaque","aucun","quelque","quelques",
    "son","sa","leur","leurs","notre","nos","votre","vos","mon","ma","ce","cet",
    "cette","tout","toute","tous","toutes","autre","autres","quel","quelle",
    "quels","quelles","deux","trois","dernier","derniers","quatre","cinq",
    "mille","cent","son"}
PREP_NOUN_PAS = {"à","au","aux","en","sur","dans","par","avec","sans","sous","vers",
    "entre","chez","devant","derrière","après"}
# common finite forms (recall-oriented; audit decides)
FINITE = {"est","sont","suis","es","sommes","êtes","a","as","avons","avez","ont",
    "ai","fait","font","fais","faites","faisons","dit","disent","dis","dites",
    "disons","peut","peuvent","peux","pouvons","pouvez","sait","savent","sais",
    "savons","savez","veut","veulent","veux","voulons","voulez","doit","doivent",
    "dois","devons","devez","va","vont","vais","allons","allez","vient",
    "viennent","viens","venons","venez","prend","prennent","prends","prenons",
    "prenez","met","mettent","mets","mettons","mettez","voit","voient","vois",
    "voyons","voyez","faut","fallait","paraît","semble","semblent","reste",
    "restent","devient","deviennent","tient","tiennent","porte","portent",
    "suit","suivent","connaît","sent","rend","comprend","trouve","trouvent",
    "donne","donnent","laisse","laissent","crois","croit","croient","pense",
    "pensent","sais","savoir","étais","était","étaient","serait","seraient",
    "avait","avaient","aurait","auraient","faisait","faisaient","pouvait",
    "voulait","devait","allait","venait","prenait","mettait","voyait","fallait",
    "semblait","paraissait","restait","devenait","tenait","portait","suivait",
    "donnait","laissait","trouvait","rendait","sentait","comprenait","connaissait",
    "fera","feront","dira","diront","pourra","pourront","voudra","voudront",
    "devra","devront","ira","iront","viendra","viendront","prendra","prendront",
    "mettra","mettront","verra","verront","faudra","semblerait","paraîtra",
    "resteront","deviendront","tiendront","porteront","suivront","donneront",
    "laisseront","trouveront","rendront"}
FINITE_END = re.compile(r"(aient|ait|rai$|ras$|ra$|ront$|rons$|rez$|rez\b|rais$|rait$|"
    r"âmes$|âtes$|èrent$|îmes$|îtes$|irent$|ûmes$|ûtes$|urent$|ons$|ez$|ions$|"
    r"iez$|ais$|é$|ées$|és$)$")

def is_finite(w):
    return w in FINITE or bool(FINITE_END.search(w))

d = json.load(open(IN))
cls = Counter()
prime = []      # no det/prep/non before; no pas-de/à after; keep for audit
for c in d["candidates"]:
    lw = c["left"].split(); rw = c["right"].split()
    left1 = lw[-1] if lw else ""
    right1 = rw[0] if rw else ""
    if left1 in DET_LIKE:
        cls["det_non+pas"] += 1; continue
    if left1 in PREP_NOUN_PAS:
        cls["prep+noun-pas"] += 1; continue
    if right1 in ("de","des","du","d","à"):
        cls["pas+de/à"] += 1; continue
    cls["other"] += 1
    prime.append(c)

# within prime: flag verb-adjacent ones (highest audit priority)
vflag = []
for c in prime:
    lw = c["left"].split(); rw = c["right"].split()
    win = lw[-4:] + rw[:4]
    c["_vflag"] = any(is_finite(w) for w in win)
    if c["_vflag"]:
        vflag.append(c)

json.dump({"classes": dict(cls), "prime_n": len(prime), "vflag_n": len(vflag),
           "prime": prime, "vflag": vflag},
          open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
print(json.dumps({"classes": dict(cls), "prime_n": len(prime),
                  "vflag_n": len(vflag)}, ensure_ascii=False))
