#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-inversion-prose.

Postposed-order test ('[inf] !, cela/ceci/ça') in the PROSE register.

SAME inversion census as disloc_demonstrative_inversion_fullcorpus_census.py
verbatim: same INF suffix pattern, same DEM_POST tonic set, same candidate
rule (DEM match starts after the infinitive inside INF..INF+100, and "!"
occurs between INF start and 20 chars past the DEM match end) — but run on
the 21-file prose corpus (18 French 1841-register prose files + 3 wider
19th-century prose files), the same set as
disloc_demonstrative_prose_clause_initial_census.py.

Output: disloc-demonstrative-inversion-prose_census.json.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")
GUTENBERG = os.path.join(LANE, "data")

PROSE_FILES = [
    os.path.join(CORPUS, "guizot-memoires-t1-gutenberg.txt"),
    os.path.join(CORPUS, "guizot-memoires-t2-gutenberg.txt"),
    os.path.join(CORPUS, "guizot-memoires-t3-gutenberg.txt"),
    os.path.join(CORPUS, "guizot-memoires-t5-t6.txt"),
    os.path.join(CORPUS, "nesselrode-v10.txt"),
    os.path.join(CORPUS, "nesselrode-v7.txt"),
    os.path.join(CORPUS, "nesselrode-v8.txt"),
    os.path.join(CORPUS, "nesselrode-v9.txt"),
    os.path.join(CORPUS, "revue-deux-mondes-1841-q1.txt"),
    os.path.join(CORPUS, "revue-deux-mondes-1841-q2.txt"),
    os.path.join(CORPUS, "revue-deux-mondes-1841-q3.txt"),
    os.path.join(CORPUS, "revue-deux-mondes-1841-q4.txt"),
    os.path.join(CORPUS, "metternich-papiere-v4.txt"),
    os.path.join(CORPUS, "metternich-papiere-v6.txt"),
    os.path.join(CORPUS, "talleyrand-memoires-v1.txt"),
    os.path.join(CORPUS, "pozzo-di-borgo-correspondance-v1.txt"),
    os.path.join(CORPUS, "levant-correspondence-1841-p3.txt"),
    os.path.join(GUTENBERG, "gutenberg-17489-miserables1.txt"),
    os.path.join(GUTENBERG, "gutenberg-30513-tocqueville-t1.txt"),
    os.path.join(GUTENBERG, "gutenberg-30514-tocqueville-t2.txt"),
]

OUT = os.path.join(LANE, "code/crowd17/next-token",
                   "disloc-demonstrative-inversion-prose_census.json")

INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
DEM_POST = re.compile(r"\b(cela|ceci|ça|ca|cel[àa]|cec[iy])\b", re.IGNORECASE)


def main():
    files, cands, seen = [], [], set()
    total = 0
    for p in PROSE_FILES:
        name = os.path.basename(p)
        text = open(p, encoding="utf-8", errors="replace").read()
        n_new = 0
        for im in INF.finditer(text):
            wend = im.end() + 100
            win = text[im.start():wend]
            for dm in DEM_POST.finditer(win):
                if dm.start() < (im.end() - im.start()):
                    continue  # demonstrative precedes the infinitive
                if "!" not in win[:dm.end() + 20]:
                    continue  # exclamatory link not local
                key = (name, im.start())
                if key in seen:
                    continue
                seen.add(key)
                cands.append({
                    "file": name,
                    "inf": im.group(0).lower(),
                    "inf_abs_offset": im.start(),
                    "dem": dm.group(1).lower(),
                    "window": win,
                })
                n_new += 1
        total += len(text)
        print(f"{name}: {len(text)} chars, {n_new} postposed-dem candidates")
        files.append({"file": name, "chars": len(text),
                      "postposed_dem_candidates": n_new})
    json.dump({"files": files, "candidates": cands}, open(OUT, "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT, "| total chars:", total,
          "| total unique candidates:", len(cands))


if __name__ == "__main__":
    main()
