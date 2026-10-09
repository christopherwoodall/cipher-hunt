#!/usr/bin/env python3
r"""Census for battery reinforced-head-frequency-comedy.

Question: are dislocated reinforced heads genuinely rarer in comedy than in
drama — syntactic locus (heads don't dislocate) vs lexical locus (heads
dislocate but never license infinitives)?

Same P1/P2/P3 taxonomy as disloc_demonstrative_drama_reinforced_census.py:
  P1 (dislocation): DEM_REINF\s*[,;:] where DEM_REINF =
      ((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|
       ça[-\u2011\u2013 ]?(?:l[àa]|ci)) — case-insensitive.
      window = demonstrative through next [!?.] (inclusive), cap 180 chars.
  P2 (exclamatory filter): window must contain "!" before its end.
  P3 (infinitive candidate): \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b
      on the window; MANUAL classification in the report.

Genre sets (period French theatre only; one edition per play):
  COMEDY = labiche-* (13) + scribe-* (5) + musset-comedies-proverbes-1850 (1)
  DRAMA  = delavigne-* (3) + dumas pere (6) + hugo (7, minus duplicate
           hugo-hernani.txt) + vigny-chatterton + musset-lorenzaccio +
           ponsard-lucrece
Also counts raw reinforced heads (no comma) per file for the dislocation-
propensity metric (hits per head occurrence).
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DRAMADIR = os.path.join(LANE, "code/side-period/corpus")

COMEDY = [
    "labiche-29-degres-ombre.txt", "labiche-affaire-rue-lourcine.txt",
    "labiche-baron-fourchevif.txt", "labiche-chapeau-de-paille.txt",
    "labiche-doit-on-le-dire.txt", "labiche-edgard-bonne.txt",
    "labiche-la-cagnotte.txt", "labiche-main-leste.txt",
    "labiche-martin-poudre-aux-yeux.txt", "labiche-misanthrope-auvergnat.txt",
    "labiche-noces-bouchencoeur.txt", "labiche-prix-martin.txt",
    "labiche-voyage-perrichon.txt",
    "scribe-bertrand-et-raton.txt", "scribe-charlatanisme.txt",
    "scribe-le-lorgnon.txt", "scribe-le-savant.txt", "scribe-verre-d-eau.txt",
    "musset-comedies-proverbes-1850.txt",
]
DRAMA = [
    "delavigne-famille-luther.txt", "delavigne-paria.txt",
    "delavigne-vepres-siciliennes.txt",
    "dumas-antony.txt", "dumas-fils-dame-camelias.txt", "dumas-henri-iii.txt",
    "dumas-kean.txt", "dumas-mariage-louis-xv-1841.txt",
    "dumas-tour-de-nesle.txt",
    "hugo-angelo.txt", "hugo-burgraves.txt", "hugo-hernani-1870.txt",
    "hugo-lucrece-borgia.txt", "hugo-marie-tudor.txt", "hugo-roi-samuse.txt",
    "hugo-ruy-blas.txt",
    "vigny-chatterton-1835.txt", "musset-lorenzaccio.txt",
    "ponsard-lucrece.txt",
]

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))", re.IGNORECASE)
DEM_REINF_COMMA = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

def windows(text):
    out = []
    for m in DEM_REINF_COMMA.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        out.append({"dem": m.group(1).lower(), "offset": m.start(),
                    "window": win,
                    "inf_hits": sorted({w.group(0).lower()
                                        for w in INF.finditer(win)})})
    return out

def census(files, label):
    per_file, cands = [], []
    total_chars = total_heads = total_p1 = 0
    on_disk = {f for f in os.listdir(DRAMADIR) if f.endswith(".txt")}
    missing = [f for f in files if f not in on_disk]
    if missing:
        raise SystemExit("GATE FAIL (%s): missing files: %s" % (label, ", ".join(missing)))
    for f in files:
        text = open(os.path.join(DRAMADIR, f), encoding="utf-8",
                    errors="replace").read()
        n_heads = len(DEM_REINF.findall(text))
        n_p1 = len(DEM_REINF_COMMA.findall(text))
        c = windows(text)
        for w in c:
            w["file"] = f
            cands.append(w)
        per_file.append({"file": f, "chars": len(text),
                         "reinforced_heads": n_heads,
                         "p1_hits": n_p1, "p2_candidates": len(c)})
        print("%s: %7d chars, heads=%3d, P1=%2d, P2=%2d" %
              (f, len(text), n_heads, n_p1, len(c)))
        total_chars += len(text); total_heads += n_heads; total_p1 += n_p1
    print("%s TOTAL: %d files, %d chars, heads=%d, P1=%d, P2=%d" %
          (label, len(files), total_chars, total_heads, total_p1, len(cands)))
    return {"label": label, "files": per_file,
            "total_chars": total_chars, "total_heads": total_heads,
            "total_p1": total_p1, "total_p2": len(cands),
            "candidates": cands}

def main():
    comedy = census(COMEDY, "COMEDY")
    drama = census(DRAMA, "DRAMA")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-head-frequency-comedy_census.json")
    json.dump({"comedy": comedy, "drama": drama}, open(out, "w"),
              ensure_ascii=False, indent=1)
    print("wrote", out)

if __name__ == "__main__":
    main()
