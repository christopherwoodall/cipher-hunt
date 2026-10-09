#!/usr/bin/env python3
r"""Census for battery reinforced-pour-inf-widercorpus.

Same P1/P2/P3 as reinforced_pour_inf_diagnostic_census.py, verbatim,
but against a SECOND 19th-century French corpus not covered by the
diagnostic (1841 register + miserables/tocqueville wider-19c) nor by the
in-flight drama sibling (reinforced-pour-inf-drama): 14 vaudeville
comedies (11 Labiche + 3 Scribe) from code/side-period/corpus.

P1 (dislocation): DEM_REINF\s*[,;:]
    DEM_REINF = r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|ça[-\u2011\u2013 ]?(?:l[àa]|ci))"
    case-insensitive. Window = text from demonstrative through next
    [!?.] inclusive, capped at 180 chars.
P2 (exclamatory filter): window must contain "!" before its end.
P3 (governed-infinitive candidate):
    r"\b(pour|à|a|de|d['’])\s+(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
    on the window text AFTER the comma, case-insensitive.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

# 14 vaudeville comedies. Excluded on purpose: labiche-chapeau-de-paille,
# labiche-martin-poudre-aux-yeux (in drama sibling), scribe-bertrand-et-raton,
# scribe-verre-d-eau (in drama sibling).
FILES = [
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
    "scribe-charlatanisme.txt",
    "scribe-le-lorgnon.txt",
    "scribe-le-savant.txt",
]

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)

GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['’])\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)

def windows(text):
    out = []
    for m in DEM_REINF.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        after_comma = win[m.end() - m.start():]
        gov_hits = [(g.group(1).lower(), g.group(0).lower())
                    for g in GOV_INF.finditer(after_comma)]
        if not gov_hits:
            continue
        out.append({"dem": m.group(1).lower(), "window": win,
                    "gov_inf_hits": sorted({h[0] + " + " + h[1] for h in gov_hits})})
    return out

def main():
    files, cands, total = [], [], 0
    for name in FILES:
        p = os.path.join(CORPUS, name)
        t = open(p, encoding="utf-8", errors="replace").read()
        total += len(t)
        n_dem = len(DEM_REINF.findall(t))
        c = windows(t)
        files.append({"file": name, "chars": len(t),
                      "dem_comma_hits": n_dem, "gov_inf_candidates": len(c)})
        for w in c:
            w["file"] = name
            cands.append(w)
    print(f"{len(files)} files, {total} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{len(cands)} governed-inf exclamatory candidates")
    for f in files:
        print(f"  {f['file']}: {f['chars']} chars, {f['dem_comma_hits']} dem, {f['gov_inf_candidates']} cand")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-pour-inf-widercorpus_census.json")
    json.dump({"files": files, "total_chars": total, "candidates": cands},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)

if __name__ == "__main__":
    main()
