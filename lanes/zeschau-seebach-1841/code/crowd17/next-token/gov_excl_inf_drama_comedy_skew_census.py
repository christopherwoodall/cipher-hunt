#!/usr/bin/env python3
r"""Census for battery gov-excl-inf-drama-comedy-skew.

P1/P2 verbatim from gov_excl_inf_register_drama_census.py (via
gov_excl_inf_drama_n2_census.py): for every "!", 120-char lookback,
GOV_INF pattern = (pour|à|a|de|d') + up to 2 short tokens + infinitive-shaped
word; closest match; skip if [.;] between match end and "!".
All candidates are classified MANUALLY in the battery report using the
parent taxonomy.

Corpus: NEW non-comic drama files only (never censused before):
  hugo-roi-samuse.txt, hugo-lucrece-borgia.txt, hugo-marie-tudor.txt,
  hugo-angelo.txt, musset-lorenzaccio.txt,
  dumas-fils-dame-camelias.txt, ponsard-lucrece.txt

Output: gov-excl-inf-drama-comedy-skew_census.json
"""
import json, os, re

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

FILES = [
    ("hugo-roi-samuse.txt", "Hugo, Le Roi s'amuse (drame, 1832)"),
    ("hugo-lucrece-borgia.txt", "Hugo, Lucrèce Borgia (drame, 1833)"),
    ("hugo-marie-tudor.txt", "Hugo, Marie Tudor (drame, 1833)"),
    ("hugo-angelo.txt", "Hugo, Angelo, tyran de Padoue (drame, 1835)"),
    ("musset-lorenzaccio.txt", "Musset, Lorenzaccio (drame, 1834)"),
    ("dumas-fils-dame-camelias.txt", "Dumas fils, La Dame aux camélias (drame, 1852)"),
    ("ponsard-lucrece.txt", "Ponsard, Lucrèce (tragédie, 1843)"),
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
        out.append({"prep": g.group(1).lower(),
                    "infinitive_shaped": g.group(0).rsplit(None, 1)[-1].lower(),
                    "dist": len(tail),
                    "byte_offset": m.start(),
                    "window": seg + "!"})
    return out

def main():
    files = []
    grand_cands, grand_chars, grand_bangs = 0, 0, 0
    for fn, desc in FILES:
        p = os.path.join(CORPUS, fn)
        with open(p, encoding="utf-8") as f:
            text = f.read()
        cands = candidates(text)
        files.append({"file": fn, "desc": desc, "chars": len(text),
                      "bangs": len(re.findall(r"!", text)),
                      "candidates": len(cands),
                      "windows": cands})
        grand_cands += len(cands)
        grand_chars += len(text)
        grand_bangs += len(re.findall(r"!", text))
        print("%-32s %8d chars  %6d bangs  %4d cands" %
              (fn, len(text), len(re.findall(r"!", text)), len(cands)))
    print("TOTAL %d chars, %d bangs, %d candidates" %
          (grand_chars, grand_bangs, grand_cands))
    with open(os.path.join(NT, "gov-excl-inf-drama-comedy-skew_census.json"),
              "w", encoding="utf-8") as f:
        json.dump({"files": files, "grand": {"chars": grand_chars,
                                             "bangs": grand_bangs,
                                             "candidates": grand_cands}},
                  f, ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
