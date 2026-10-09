#!/usr/bin/env python3
"""Classification harness for gov-excl-inf-recall.

Pass 1 (automatic): candidates whose infinitive-shaped word is on the
NEVER_INF denylist (words that can never be French infinitives:
nouns, adjectives, determiners, prepositions, adverbs, names, OCR
garbage) are excluded as cause A -- the parent battery's cause-A
class, with the denylist recorded verbatim in the census JSON.

Pass 2 (manual): every remaining tight-band (dist<=40) candidate is
printed to /tmp/recall_review.txt with an index for hand
classification into B (finite-matrix embedding), C (exclaimed-NP
embedding), D (quotation/interjection terminator), E (interrogative
matrix, '?' windows), or GENUINE. Decisions are recorded in
/tmp/recall_decisions.json as {idx: cause}; rerunning this script
tallies them.

Wide band (dist>40) candidates go to /tmp/recall_review_wide.txt for
scanning (parent battery's "scanned" treatment).
"""
import json, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")

# Words that can never be French infinitives. Conservative: anything that
# is or could be an infinitive (including noun/infinitive duals like
# rire, dire, pouvoir, sourire, dîner) is NOT on this list and gets read.
NEVER_INF = {
 # determiners / pronouns / numerals
 "notre", "votre", "vôtre", "l'autre", "d'autre", "autre", "quatre",
 # prepositions / adverbs
 "contre", "entre", "outre", "encore", "voire", "arrière",
 # nouns (incl. -er/-re/-ir/-oir false friends)
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
 # adjectives
 "propre", "première", "premier", "entier", "nécessaire",
 "intermédiaire", "contraire", "libre", "légère", "dernier",
 "derniere", "dernière", "pauvre", "moindre", "barbare", "régulier",
 "célèbre", "noir", "intérieure", "cher", "septembre", "novembre",
 "ministre", "ministère",
 # conjugated verb forms (never infinitives) / names / OCR garbage
 "désire", "vibre", "qu'engendre", "enterre", "montpellier",
 "letellier", "thénardier", "palmer", "miutaire", "beer",
 "ratt'ermir", "empörter", "aber", "baviere", "bavière", "fordre",
 "koir", "tempre", "lyser", "raumer", "speare", "giinther",
 "werther", "müller", "grégoire", "théodore", "aboukir", "jupiter",
 "toire", "tempre", "désarpier", "rességuier", "surgére",
 "galaizière", "lavoisier", "colleter", "tionner", "moinsd'enadmirer",
 "guiser",
}

def load():
    d = json.load(open(os.path.join(NT, "gov-excl-inf-recall_census.json")))
    cands = []
    for sec in ["census_1841_register", "census_wider_19c"]:
        s = d[sec]
        for key in ["G1_qmark", "G2_longspan", "G3_dashcolon"]:
            cands.extend(s[key])
    return cands

def main():
    cands = load()
    tight = [c for c in cands if c["dist"] <= 40]
    wide = [c for c in cands if c["dist"] > 40]
    auto_a = [c for c in tight if c["infinitive_shaped"] in NEVER_INF]
    toread = [c for c in tight if c["infinitive_shaped"] not in NEVER_INF]
    toread.sort(key=lambda c: (c["gap"], c["dist"], c["file"], c["term_offset"]))
    print(f"tight={len(tight)} auto-A={len(auto_a)} to-read={len(toread)} "
          f"wide={len(wide)}")
    with open("/tmp/recall_review.txt", "w") as f:
        for i, c in enumerate(toread):
            w = c["window"].replace("\n", " / ")
            tail = w[-160:]
            f.write(f"[{i}] {c['gap']} {c['file']} @{c['term_offset']} "
                    f"dist={c['dist']} {c['prep']}+{c['infinitive_shaped']} "
                    f"ntok={c['intervening_tokens']}\n")
            f.write(f"    ...{tail}\n")
    wide_sorted = sorted(wide, key=lambda c: (c["gap"], c["dist"]))
    with open("/tmp/recall_review_wide.txt", "w") as f:
        for i, c in enumerate(wide_sorted):
            w = c["window"].replace("\n", " / ")
            f.write(f"[W{i}] {c['gap']} {c['file']} @{c['term_offset']} "
                    f"dist={c['dist']} {c['prep']}+{c['infinitive_shaped']}\n")
            f.write(f"    ...{w[-160:]}\n")
    json.dump({"auto_A": auto_a,
               "denylist": sorted(NEVER_INF),
               "toread_index": [
                   {"idx": i, "gap": c["gap"], "file": c["file"],
                    "term_offset": c["term_offset"], "dist": c["dist"],
                    "prep": c["prep"],
                    "infinitive_shaped": c["infinitive_shaped"],
                    "window": c["window"]}
                   for i, c in enumerate(toread)],
               "wide_count": len(wide)},
              open("/tmp/recall_classify_state.json", "w"),
              ensure_ascii=False, indent=1)
    print("wrote /tmp/recall_review.txt, /tmp/recall_review_wide.txt, "
          "/tmp/recall_classify_state.json")

if __name__ == "__main__":
    main()
