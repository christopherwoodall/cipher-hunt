#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-inversion-fullcorpus.

Follow-up of battery disloc-demonstrative-inversion (confirmed zero at
quoted-dialogue level). SAME inversion census (verbatim INF suffix pattern,
verbatim DEM_POST tonic set, same candidate rule: DEM match starts after
the infinitive inside INF..INF+100, and "!" occurs between INF start and
20 chars past the DEM match end) but run on FULL-CORPUS windows, not
dialogue-scoped: the whole text of each revue-deux-mondes-1841 qN file is
one searchable window. If the pairing is a narrative-register feature,
dialogue-scoping hides it; this census tests full-corpus windows.

Output: disloc-demonstrative-inversion-fullcorpus_census.json.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
RDM = [os.path.join(LANE, "code/side-period/corpus",
                    f"revue-deux-mondes-1841-q{n}.txt") for n in (1, 2, 3, 4)]
OUT = os.path.join(LANE, "code/crowd17/next-token",
                   "disloc-demonstrative-inversion-fullcorpus_census.json")

INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
DEM_POST = re.compile(r"\b(cela|ceci|ça|ca|cel[àa]|cec[iy])\b", re.IGNORECASE)


def main():
    files, cands, seen = [], [], set()
    for p in RDM:
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
        print(f"{name}: {len(text)} chars, {n_new} postposed-dem candidates")
        files.append({"file": name, "chars": len(text),
                      "postposed_dem_candidates": n_new})
    json.dump({"files": files, "candidates": cands}, open(OUT, "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT, "| total unique candidates:", len(cands))


if __name__ == "__main__":
    main()
