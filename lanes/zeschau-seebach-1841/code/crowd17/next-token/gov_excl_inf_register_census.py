#!/usr/bin/env python3
r"""Census for battery gov-excl-inf-register.

Follow-up #2 of the NULL battery-reinforced-pour-inf-diagnostic (2026-10-09).
That battery fenced reinforced-head + governed exclamatory infinitive
(0/4 genuine; parent null kept). THIS battery drops the topic constraint:
corpus-wide census of GOVERNED exclamatory infinitives ("pour rire !",
"à donner lecture !", "de croire !") with ANY topic, in the same
27.66M-char 19th-century French corpus.

Bar (verbatim, pre-registered): "if the construction is unattested
corpus-wide, the zero is register-level (construction absent from 1841
French print, head-licensing moot); if it attests with other topics, the
demonstrative-head gap is specific and the fence stands".

Search patterns (exact, verbatim):
  P1 (candidate): for every "!" in the corpus, take the 120 chars before
      it. Run GOV_INF on that segment:
      r"\b(pour|à|a|de|d['’])\s+(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}
       \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b" (case-insensitive),
      the P3 pattern of the parent battery (prep pour/à/a/de/d' + up to two
      short tokens + infinitive-shaped word). The match closest to the "!"
      is kept; between its end and the "!" there must be no [.;]
      (sentence-internal exclamation only). dist = chars from the end of
      the infinitive-shaped word to the "!".
  P2 (banding): candidates are banded by dist; tight band dist<=40 is the
      discriminating band (the exclaimed element is the infinitive phrase
      itself). Wider band 40<dist<=120 candidates necessarily contain
      intervening finite-clause material and are triaged separately.
  All candidates are printed for MANUAL classification (regex cannot
  separate -er infinitives from nouns/adjectives in -er; unaccented "a"
  is verb-avoir noise; the "!" may belong to a matrix finite clause).

Corpus (identical to disloc-demonstrative-inf/-reinforced and to the
parent diagnostic, sizes recomputed in-session):
  - 1841-register lane corpus: code/side-period/corpus/*.txt (French files
    only; German files excluded and named in the report).
  - Wider 19th-century register: data/gutenberg-17489-miserables1.txt (1862),
    data/gutenberg-30513-tocqueville-t1.txt (1835),
    data/gutenberg-30514-tocqueville-t2.txt (1840).

Output: gov-excl-inf-register_census.json with per-file sizes, band counts,
and all candidate windows + dist; human classification in the battery report.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
GERMAN = {
    "adb-zeschau-heinrich-anton-von.txt",
} | {f"allgemeine-zeitung-augsburg-1841-01-{d:02d}.txt" for d in range(11, 26)}
WIDER = [
    os.path.join(LANE, "data/gutenberg-17489-miserables1.txt"),
    os.path.join(LANE, "data/gutenberg-30513-tocqueville-t1.txt"),
    os.path.join(LANE, "data/gutenberg-30514-tocqueville-t2.txt"),
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
    c1841 = [os.path.join(CORPUS1841, f) for f in os.listdir(CORPUS1841)
             if f.endswith(".txt") and f not in GERMAN]
    res = {"census_1841_register": census(c1841, "1841 register"),
           "census_wider_19c": census(WIDER, "wider 19c")}
    out = os.path.join(NT, "gov-excl-inf-register_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
