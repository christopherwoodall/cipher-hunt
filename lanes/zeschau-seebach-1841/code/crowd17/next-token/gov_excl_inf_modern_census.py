#!/usr/bin/env python3
"""Battery gov-excl-inf-modern: governed exclamatory infinitive census on a
MODERN French corpus (early-20th-c French fiction; see corpus-modern/PROVENANCE.md),
replicating the P1 candidate design of gov_excl_inf_register_census.py verbatim.

"Governed exclamatory infinitive" = a preposition-governed infinitive phrase
(pour / a / de + infinitive) that IS itself the exclaimed element
("pour rire !"). "Genuine attestation" = the "!" terminates the governed
infinitive phrase itself; the infinitive is not embedded in a finite matrix
clause whose "!" belongs to the matrix, and not embedded in an exclaimed
noun phrase.
"""
import re, os, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "corpus-modern")

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

def main():
    paths = sorted(glob.glob(os.path.join(CORPUS, "pg*.txt")))
    assert paths, "no extracted corpus text files found"
    files, cands, total = [], [], 0
    for p in paths:
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total += len(t)
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
    print(f"=== modern: {len(files)} files, {total} chars, "
          f"{sum(f['bang_count'] for f in files)} '!', "
          f"{len(cands)} candidates (tight<=40: "
          f"{sum(f['candidates_tight_le40'] for f in files)})")
    json.dump({"files": files, "total_chars": total, "candidates": cands},
              open(os.path.join(HERE, "gov-excl-inf-modern_census.json"),
                   "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("wrote gov-excl-inf-modern_census.json")

if __name__ == "__main__":
    main()
