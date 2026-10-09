#!/usr/bin/env python3
"""Classification harness for gov-excl-inf-drama-recall.

Pass 1 (automatic): candidates whose infinitive-shaped word is on the
NEVER_INF denylist (copied verbatim from gov_excl_inf_recall_classify.py)
are excluded as cause A.

Pass 2 (manual): every remaining tight-band (dist<=40) candidate is
printed to /tmp/drama_recall_review.txt with an index for hand
classification into B (finite-matrix embedding), C (exclaimed-NP
embedding), D (quotation/interjection terminator), E (interrogative
matrix, '?' windows), or GENUINE. Decisions are recorded in
/tmp/drama_recall_decisions.json as {idx: cause}; rerunning this script
tallies them.

Wide band (dist>40) goes to /tmp/drama_recall_review_wide.txt for
scanning (parent battery's "scanned" treatment).
"""
import json, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")

NEVER_INF = {
 "notre", "votre", "vôtre", "l'autre", "d'autre", "autre", "quatre",
 "contre", "entre", "outre", "encore", "voire", "arrière",
 "guerre", "chambre", "nature", "l'angleterre", "l'anjïleterre",
 "angleterre", "l'empire", "empire", "l'avenir", "avenir", "l'histoire",
 "histoire", "mesure", "affaire", "l'affaire", "heure", "l'heure",
 "iieure", "père", "mère", "frère", "gloire", "solitaire", "terre",
 "poudre", "livre", "caractère", "titre", "genre", "prêtre", "mémoire",
 "territoire", "plaisir", "papier", "colère", "peinture", "manière",
 "misère", "oeuvre", "salaire", "lumière", "massacre", "maitre",
 "maître", "espoir", "l'ombre", "ombre", "carrossier", "fiacre",
 "cendre", "fardier", "pontarlier", "aventure", "mystère",
 "l'étranger", "l'étrangére", "guêpier", "l'équilibre", "droiture",
 "signature", "lettre", "ordre", "dictature", "dictionnaire",
 "nomenclature", "figure", "damier", "sphère", "foyer", "rivière",
 "dampierre", "matière", "bière", "métier", "routier", "l'ouvrier",
 "grenadier", "berger", "commodore", "maire", "désastre", "traître",
 "d'acre", "insulaire", "fautre",
 "propre", "première", "premier", "entier", "nécessaire",
 "intermédiaire", "contraire", "libre", "légère", "dernier",
 "derniere", "dernière", "pauvre", "moindre", "barbare", "régulier",
 "célèbre", "noir", "intérieure", "cher", "septembre", "novembre",
 "ministre", "ministère",
 "désire", "vibre", "qu'engendre", "enterre", "montpellier",
 "letellier", "thénardier", "palmer", "miutaire", "beer",
 "ratt'ermir", "empörter", "aber", "baviere", "bavière", "fordre",
 "koir", "tempre", "lyser", "raumer", "speare", "giinther",
 "werther", "müller", "grégoire", "théodore", "aboukir", "jupiter",
 "toire", "tempre", "désarpier", "rességuier", "surgére",
 "galaizière", "lavoisier", "colleter", "tionner", "moinsd'enadmirer",
 "guiser",
}

def main():
    d = json.load(open(os.path.join(NT, "gov-excl-inf-drama-recall_census.json")))
    cands = d["candidates"]
    wins = { (g, f, o): w for (g, f, o, w) in json.load(open(
        os.path.join(NT, "gov-excl-inf-drama-recall_windows.json"))) }
    tight = [c for c in cands if c["dist"] <= 40]
    wide = [c for c in cands if c["dist"] > 40]
    auto_a = [c for c in tight if c["infinitive_shaped"] in NEVER_INF]
    toread = [c for c in tight if c["infinitive_shaped"] not in NEVER_INF]
    toread.sort(key=lambda c: (c["gap"], c["dist"], c["file"], c["term_offset"]))
    print(f"tight={len(tight)} auto-A={len(auto_a)} to-read={len(toread)} "
          f"wide={len(wide)}")
    gaps = {}
    for c in toread:
        gaps.setdefault(c["gap"], 0)
        gaps[c["gap"]] += 1
    print("to-read per gap:", gaps)
    with open("/tmp/drama_recall_review.txt", "w") as f:
        for i, c in enumerate(toread):
            w = wins[(c["gap"], c["file"], c["term_offset"])].replace("\n", " / ")
            tail = w[-170:]
            f.write(f"[{i}] {c['gap']} {c['file']} @{c['term_offset']} "
                    f"dist={c['dist']} {c['prep']}+{c['infinitive_shaped']} "
                    f"ntok={c.get('intervening_tokens')}\n    {tail}\n")
    with open("/tmp/drama_recall_review_wide.txt", "w") as f:
        wide.sort(key=lambda c: (c["gap"], c["dist"], c["file"], c["term_offset"]))
        for i, c in enumerate(wide):
            w = wins[(c["gap"], c["file"], c["term_offset"])].replace("\n", " / ")
            tail = w[-170:]
            f.write(f"[W{i}] {c['gap']} {c['file']} @{c['term_offset']} "
                    f"dist={c['dist']} {c['prep']}+{c['infinitive_shaped']}\n"
                    f"    {tail}\n")
    if os.path.exists("/tmp/drama_recall_decisions.json"):
        dec = json.load(open("/tmp/drama_recall_decisions.json"))
        tall = {}
        for i, c in enumerate(toread):
            k = str(i)
            if k in dec:
                tall.setdefault(dec[k], 0)
                tall[k] += 1
        print("decisions so far:", sum(len(v) if False else 0 for v in []), "total tallied:", tall)

if __name__ == "__main__":
    main()
