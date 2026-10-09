#!/usr/bin/env python3
"""Census: clause-initial Mais/Or/Donc/Cependant in 1841 French, by left-context frame.

Frames:
  F1 fragment-follow: preceding clause has no finite-verb form (finite list below)
  F2 ordinal-ellipsis: preceding clause ends with nominalized ordinal
     (la/le/les première(s)/premier(s)/seconde/second/début? no: ordinal list)
  F3 fois-final: preceding clause has 'fois' in last 2 word positions
Output: contingency table per particle + JSON with examples.
"""
import json, os, re, sys

CORP = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")

DIPLOMATIC = [
    "levant-correspondence-1841-p3.txt",
    "metternich-papiere-v4.txt",
    "metternich-papiere-v6.txt",
    "pozzo-di-borgo-correspondance-v1.txt",
    "talleyrand-memoires-v1.txt",
    "guizot-memoires-t1-gutenberg.txt",
    "guizot-memoires-t2-gutenberg.txt",
    "guizot-memoires-t3-gutenberg.txt",
    "guizot-memoires-t5-t6.txt",
]

# Common finite verb forms (3sg/3pl + 1/2 forms) in 19th-c French.
# Criterion is documented; hand-audit backs the fragment calls.
FINITE = set("""
est sont etait etaient sera seront serait seraient soit soient fut furent
suis es sommes etes etais etait etions etiez serai seras
a ont avait avaient aura auront aurait auraient ait aient eut eurent
as avez avons ai aurai
fait font faisait faisaient fera feront ferait feraient fais fait
dit disent disait disaient dira diront
doit doivent devait devaient devra devront
peut peuvent pouvait pouvaient pourra pourront
sait savent savait savaient saura sauront
veut veulent voulait voulaient voudra voudront
faut fallait faudra fallut
va vont allait allaient ira iront irait
vient viennent venait venaient viendra viendront
voit voient voyait voyaient verra verront
prend prennent prenait prenaient prendra
met mettent mettait mettaient mettra
donne donnent donnait donnaient donnera
parait paraissent paraissait semblent semble semblaient
devient deviennent devenait restera reste restent restait
trouve trouvent trouvait croyait croit croient
pense pensent pensait porte portent portait
sert servent servait recoit recoivent recoivent
suit suivent suivait connait connaissent
ecrit ecrivent ecrivait parle parlent parlait
tient tiennent tenait passe passent passait
laisse laissent laissait
""".split())

PARTICLES = ["mais", "or", "donc", "cependant"]

ORDINAL_END = re.compile(
    r"\b(l[ae]|les)\s+(premi[eè]re?s?|premiers?|second(e?s)?|troisi[eè]me?s?|derni[eè]re?s?|derniers?)\s*$",
    re.I)

def strip_acc(s):
    return (s.replace("é","e").replace("è","e").replace("ê","e").replace("ë","e")
             .replace("à","a").replace("â","a").replace("î","i").replace("ï","i")
             .replace("ô","o").replace("ù","u").replace("û","u").replace("ç","c"))

def clauses(text):
    # split on sentence/clause terminators and paragraph breaks only;
    # single newlines are line-wraps inside OCR'd texts, NOT boundaries
    parts = re.split(r"[.;:!?…]+|\n\s*\n", text)
    return [p.strip(" \t\"'«»'()") for p in parts if p.strip(" \t\"'«»'()")]

def first_word(cl):
    m = re.match(r"[\"'«»(\s]*([A-Za-zÀ-ÿ]+)", cl)
    return m.group(1) if m else ""

def words(cl):
    return re.findall(r"[A-Za-zÀ-ÿ]+(?:'[A-Za-zÀ-ÿ]+)?", cl)

def is_verbless(cl):
    ws = [strip_acc(w).lower() for w in words(cl)]
    return not any(w in FINITE for w in ws)

def fois_final(cl):
    ws = [strip_acc(w).lower() for w in words(cl)]
    return len(ws) >= 1 and "fois" in ws[-2:]

def ordinal_final(cl):
    return bool(ORDINAL_END.search(cl))

def census(files, label):
    rows = []
    for fn in files:
        p = os.path.join(CORP, fn)
        if not os.path.exists(p):
            continue
        text = open(p, encoding="utf-8", errors="replace").read()
        cls = [c for c in clauses(text) if c]
        for i, cl in enumerate(cls):
            fw = strip_acc(first_word(cl)).lower()
            if fw in PARTICLES:
                # 'or' as gold: skip if clause is about gold/metal (rare); keep, audit later
                prev = cls[i-1] if i > 0 else ""
                rows.append({
                    "file": fn, "particle": fw,
                    "prev": prev[:220],
                    "verbless": is_verbless(prev),
                    "fois_final": fois_final(prev),
                    "ordinal_final": ordinal_final(prev),
                    "cur": cl[:160],
                })
    agg = {p: {"n": 0, "fragment": 0, "fois_final": 0, "ordinal_final": 0} for p in PARTICLES}
    for r in rows:
        a = agg[r["particle"]]
        a["n"] += 1
        if r["verbless"]:
            a["fragment"] += 1
        if r["fois_final"]:
            a["fois_final"] += 1
        if r["ordinal_final"]:
            a["ordinal_final"] += 1
    return agg, rows

def main():
    all_fr = [f for f in os.listdir(CORP)
              if f.endswith(".txt") and not f.startswith("allgemeine")
              and not f.startswith("PROVENANCE") and f != "harvest-log.txt"]
    results = {}
    for label, files in [("diplomatic", DIPLOMATIC), ("full_french", all_fr)]:
        agg, rows = census(files, label)
        results[label] = {"agg": agg, "files": len([f for f in files if os.path.exists(os.path.join(CORP, f))])}
        # save examples of the rare frames for audit
        ex = [r for r in rows if r["verbless"] or r["fois_final"] or r["ordinal_final"]]
        json.dump(ex, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        f"particle20_rivals_examples_{label}.json"), "w"),
                  ensure_ascii=False, indent=1)
        print(f"=== {label} ({results[label]['files']} files) ===")
        for p in PARTICLES:
            a = agg[p]
            print(f"{p:10s} n={a['n']:5d}  fragment={a['fragment']:4d}  fois_final={a['fois_final']:4d}  ordinal_final={a['ordinal_final']:4d}")
    json.dump(results, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "particle20_rivals_census.json"), "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
