#!/usr/bin/env python3
r"""Census for battery disloc-reinforced-comedy-widercorpus.

Re-runs the reinforced-head census (same DEM_REINF + separator class +
uncapped 400-char window + "!" + infinitive-token pattern as
disloc-reinforced-comedy-recall) on the WIDENED comedy corpus:
the 8 earlier comedy files + 8 newly ingested plays (2026-10-09 ~08:52 UTC).

P1: DEM_REINF followed by one of [,;:—–\-()] (or inside parens).
P2: window (demonstrative + 400 chars, uncapped) must contain "!".
P3: -er/-ir/-re/-oir token regex; candidates printed for MANUAL classification.

Corpus: 16 comedy files in code/side-period/corpus/.
Output: disloc-reinforced-comedy-widercorpus_census.json + console table.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")
FILES = [
    # original 8
    "scribe-le-savant.txt",
    "scribe-le-lorgnon.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "labiche-voyage-perrichon.txt",
    "labiche-la-cagnotte.txt",
    "labiche-29-degres-ombre.txt",
    "labiche-affaire-rue-lourcine.txt",
    # widened 8
    "scribe-charlatanisme.txt",
    "labiche-misanthrope-auvergnat.txt",
    "labiche-main-leste.txt",
    "labiche-edgard-bonne.txt",
    "labiche-prix-martin.txt",
    "labiche-noces-bouchencoeur.txt",
    "labiche-baron-fourchevif.txt",
    "labiche-doit-on-le-dire.txt",
]
DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))", re.IGNORECASE)
SEP = re.compile(r"\s*([,;:—–\-()])")
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

def windows(text):
    out = []
    for m in DEM_REINF.finditer(text):
        rest = text[m.end():m.end() + 6]
        sep = SEP.match(rest)
        if not sep:
            continue
        sepchar = sep.group(1)
        win = text[m.start():m.start() + 400]
        if "!" not in win:
            continue
        closed = bool(re.search(r"[!?.]", text[m.start():m.start() + 180]))
        out.append({"dem": m.group(1).lower(), "sep": sepchar,
                    "offset": m.start(), "closed_180": closed,
                    "window": win,
                    "inf_hits": sorted({w.group(0).lower()
                                        for w in INF.finditer(win)})})
    return out

def main():
    on_disk = {f for f in os.listdir(CORPUS) if f.endswith(".txt")}
    missing = [f for f in FILES if f not in on_disk]
    if missing:
        raise SystemExit("GATE FAIL: missing comedy files: " + ", ".join(missing))
    files, cands, total, heads = [], [], 0, 0
    for f in FILES:
        text = open(os.path.join(CORPUS, f), encoding="utf-8",
                    errors="replace").read()
        total += len(text)
        n_sep, n_heads = {}, 0
        for m in DEM_REINF.finditer(text):
            n_heads += 1
            s = SEP.match(text[m.end():m.end() + 6])
            if s:
                n_sep[s.group(1)] = n_sep.get(s.group(1), 0) + 1
        heads += n_heads
        c = windows(text)
        for w in c:
            w["file"] = f
            cands.append(w)
        print(f"{f}: {len(text)} chars, heads={n_heads}, sep coverage {n_sep}, "
              f"{len(c)} candidates")
        files.append({"file": f, "chars": len(text), "heads": n_heads,
                      "sep_coverage": n_sep, "candidates": len(c)})
    print(f"TOTAL: {len(files)} comedy texts, {total} chars, {heads} reinforced heads, "
          f"{len(cands)} candidates")
    for w in cands:
        print("=" * 70)
        print(f"{w['file']} @{w['offset']} dem={w['dem']!r} sep={w['sep']!r} "
              f"closed_180={w['closed_180']}")
        print(w["window"][:600].replace("\n", " / "))
        print("inf_hits:", w["inf_hits"])
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-reinforced-comedy-widercorpus_census.json")
    json.dump({"files": files, "total_chars": total,
               "total_heads": heads, "candidates": cands},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)

if __name__ == "__main__":
    main()
