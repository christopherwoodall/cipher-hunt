#!/usr/bin/env python3
r"""Census for battery gov-excl-inf-drama-n2.

Widening arm of the drama register census: runs the IDENTICAL P1/P2
governed-infinitive census (any topic) against drama files NOT covered
by the parent battery gov-excl-inf-register-drama (14 plays) — i.e.
3 additional Scribe plays and 12 additional Labiche comedies ingested
via the Scribe/Labiche comedy-extension and wider-corpus fr.wikisource
harvests (2026-10-09).

Bar (verbatim, pre-registered): ">=1 genuine in a non-Scribe play
confirms drama-wide; zero outside Scribe fences it as Scribe-idiolect".

P1/P2 verbatim from gov_excl_inf_register_drama_census.py. All
candidates are classified MANUALLY in the battery report using the
parent's taxonomy.

Corpus: code/side-period/corpus/ widened drama files only.

Output: gov-excl-inf-drama-n2_census.json with per-file sizes,
band counts, and all candidate windows + dist.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

NEW_SCRIBE = [
    "scribe-charlatanisme.txt",   # Scribe, Le Charlatanisme (1825)
    "scribe-le-lorgnon.txt",      # Scribe, Le Lorgnon (comédie en deux actes)
    "scribe-le-savant.txt",       # Scribe, Le Savant (comédie en cinq actes)
]

NEW_LABICHE = [
    "labiche-29-degres-ombre.txt",
    "labiche-affaire-rue-lourcine.txt",
    "labiche-baron-fourchevif.txt",
    "labiche-doit-on-le-dire.txt",
    "labiche-edgard-bonne.txt",
    "labiche-la-cagnotte.txt",
    "labiche-main-leste.txt",
    "labiche-misanthrope-auvergnat.txt",
    "labiche-noces-bouchencoeur.txt",
    "labiche-prix-martin.txt",
    "labiche-voyage-perrichon.txt",
    # labiche-chapeau-de-paille.txt and labiche-martin-poudre-aux-yeux.txt
    # were already censused by the parent battery; excluded here.
]

GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['’])\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)

def candidates(text):
    out = []
    for m in re.finditer(r"!", text):
        seg = text[max(0, m.start() - 120):m.start()]
        best = None
        for g in GOV_INF.finditer(seg):
            tail = seg[g.end():]
            if re.search(r"[.;]", tail):
                continue
            if best is None or g.end() > best[1]:
                best = (g, g.end())
        if best is None:
            continue
        g, end = best
        tail = seg[end:]
        win = seg + "!"
        out.append({"prep": g.group(1).lower(),
                    "infinitive_shaped": g.group(0).rsplit(None, 1)[-1].lower(),
                    "dist": len(tail),
                    "window": win})
    return out

def census(paths, label):
    total_chars = 0
    files, cands = [], []
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        c = candidates(t)
        tight = [w for w in c if w["dist"] <= 40]
        files.append({"file": name, "chars": len(t),
                      "bang_count": t.count("!"),
                      "candidates_total": len(c),
                      "candidates_tight_le40": len(tight)})
        for w in c:
            w["file"] = name
            cands.append(w)
    cands.sort(key=lambda w: (w["dist"], w["file"]))
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{sum(f['bang_count'] for f in files)} '!', "
          f"{len(cands)} candidates (tight<=40: "
          f"{sum(f['candidates_tight_le40'] for f in files)})")
    return {"files": files, "total_chars": total_chars, "candidates": cands}

if __name__ == "__main__":
    scribe_paths = [os.path.join(CORPUS, f) for f in NEW_SCRIBE]
    labiche_paths = [os.path.join(CORPUS, f) for f in NEW_LABICHE]
    missing = [p for p in scribe_paths + labiche_paths
               if not os.path.exists(p)]
    assert not missing, f"missing corpus files: {missing}"
    res = {
        "census_new_scribe": census(scribe_paths, "new Scribe"),
        "census_new_labiche": census(labiche_paths, "new Labiche"),
    }
    out = os.path.join(NT, "gov-excl-inf-drama-n2_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
