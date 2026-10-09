#!/usr/bin/env python3
r"""Census for battery reinforced-pour-inf-drama.

Target: run the SAME governed-infinitive search as
battery reinforced-pour-inf-diagnostic (the reinforced-head inventory and
P1/P2/P3 patterns), against the ingested 19th-century French DRAMA corpus.

Search patterns (verbatim, from reinforced_pour_inf_diagnostic_census.py):
  P1 (dislocation): DEM_REINF = r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]" — case-insensitive.
      Window = text from the demonstrative through the next [!?.]
      (inclusive), capped at 180 chars.
  P2 (exclamatory filter): window must contain "!" before its end.
  P3 (governed-infinitive candidate): r"\b(pour|à|a|de|d['’])\s+(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      applied to the window text AFTER the comma (case-insensitive).
  Candidates are printed for MANUAL classification.

Corpus: drama register from PROVENANCE.md Family 9 (archive.org ingest) +
Family "wikisource ingest". ONE edition per play: the Jenkins-1870
Hernani edition (hugo-hernani-1870.txt, archive.org OCR) is EXCLUDED
because hugo-hernani.txt (Hetzel 1889, wikisource) is the same play —
see corpus note. That file is separately spot-checked for any genuine
hit so the edition choice cannot hide an attestation.

Output: reinforced-pour-inf-drama_census.json with per-file sizes,
hit counts, and all candidate windows.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

# 14 distinct plays. Hernani: use the wikisource Hetzel-1889 edition only.
DRAMA = [
    "dumas-mariage-louis-xv-1841.txt",   # archive.org: Un mariage sous Louis XV (comédie, 1841)
    "vigny-chatterton-1835.txt",         # archive.org: Chatterton (drame, 1835)
    "musset-comedies-proverbes-1850.txt",# archive.org: Comédies et proverbes (10 plays)
    "hugo-hernani.txt",                  # wikisource: Hernani (Hetzel 1889) — ONE Hernani edition
    "hugo-ruy-blas.txt",                 # wikisource: Ruy Blas (1839 ed.)
    "hugo-burgraves.txt",                # wikisource: Les Burgraves (1843)
    "dumas-antony.txt",                  # wikisource: Antony (1838 vol. 2)
    "dumas-tour-de-nesle.txt",           # wikisource: La Tour de Nesle (1838 vol. 2)
    "dumas-henri-iii.txt",               # wikisource: Henri III et sa cour (1838 vol. 2)
    "dumas-kean.txt",                    # wikisource: Kean (1838 vol. 2)
    "scribe-bertrand-et-raton.txt",      # wikisource: Bertrand et Raton (comédie, 1833)
    "scribe-verre-d-eau.txt",            # wikisource: Le Verre d'eau (1861 ed.)
    "labiche-chapeau-de-paille.txt",     # wikisource: Un chapeau de paille d'Italie (1851)
    "labiche-martin-poudre-aux-yeux.txt",# wikisource: La Poudre aux yeux (1861)
]
EXCLUDED_EDITION = "hugo-hernani-1870.txt"  # second Hernani edition (OCR); spot-checked separately

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

def census(paths, label):
    total_chars = 0
    files, cands = [], []
    for name in paths:
        p = os.path.join(CORPUS, name)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        n_dem = len(DEM_REINF.findall(t))
        c = windows(t)
        files.append({"file": name, "chars": len(t),
                      "dem_comma_hits": n_dem, "gov_inf_candidates": len(c)})
        for w in c:
            w["file"] = name
            cands.append(w)
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{len(cands)} governed-inf exclamatory candidates")
    return {"files": files, "total_chars": total_chars, "candidates": cands}

if __name__ == "__main__":
    res = {"census_drama": census(DRAMA, "drama register (14 plays, 1 ed/play)"),
           "excluded_edition_note": f"{EXCLUDED_EDITION} excluded per one-edition-per-play rule; spot-checked separately"}
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-pour-inf-drama_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
