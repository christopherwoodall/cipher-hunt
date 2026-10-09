#!/usr/bin/env python3
r"""Census for battery disloc-topic-inventory-excl-inf.

Claim: census ALL bare exclamatory infinitives in the 27.66M-char
19th-century French corpus and tabulate which topics license them.

Bar (verbatim, pre-registered): "if any non-pronominal topic
(demonstrative excluded, nouns/others) licenses the bare exclamatory
infinitive, the demonstrative gap is sampling noise -> re-open the
family; if only personal pronouns do, the fence holds and the residual
closes".

Patterns (exact, verbatim):
  P1 (topic inventory): TOPIC\s*[,;:] where TOPIC is one of
      - PRON: \b(moi|toi|lui|elle|nous|vous|eux|elles|soi)\b
        (personal tonic pronouns)
      - DEM: \b(cela|ceci|ça|cel[àa]|cec[iy]|celui|ceux|celle|celles)
        ([-–— ]?(l[àa]|ci))?\b  (bare + reinforced demonstratives,
        excluded from the re-open trigger but inventoried)
      - NP: DET + 1-3 content words, where DET =
        \b(mon|ma|mes|ton|ta|tes|son|sa|ses|notre|nos|votre|vos|leur|leurs|
        le|la|les|l'|un|une|des|du|de l'|ce|cet|cette|ces|tout|toute|
        tous|toutes|quelque|quelques|chaque|aucun|aucune|plusieurs)\b
      - PROP: \b[A-ZÀÂÄÇÉÈÊËÎÏÔÖÙÛÜ][a-zàâäçéèêëîïôöùûü'\-]+
        (proper nouns / capitalized heads)
      - OTH: \b(tout le monde|personne|chacun|chacune|rien|quelqu'un|
        jamais|toujours|encore|souvent|rarement|déjà|bientôt|vite|bien|
        mal|mieux|pis)\b (quantifiers / adverbial topics)
      case-insensitive throughout.
      Window = text from the topic start through the next [!?.]
      (inclusive), capped at 200 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (infinitive candidate): an infinitive-shaped word
      \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b inside the window.
      All candidates are printed for MANUAL classification (regex cannot
      separate -er infinitives from nouns/adjectives in -er).

Corpus (identical to disloc-demonstrative-inf / -reinforced):
  - 1841-register lane corpus: code/side-period/corpus/*.txt (French files
    only; German files excluded and named in the report).
  - Wider 19th-century register: data/gutenberg-17489-miserables1.txt
    (1862), data/gutenberg-30513-tocqueville-t1.txt (1835),
    data/gutenberg-30514-tocqueville-t2.txt (1840).

Output: JSON with per-file sizes, hit counts per topic class, and all
candidate windows; human classification happens in the battery report.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
GERMAN = {
    "adb-zeschau-heinrich-anton-von.txt",
} | {f"allgemeine-zeitung-augsburg-1841-01-{d:02d}.txt" for d in range(11, 26)}
WIDER = [
    os.path.join(LANE, "data/gutenberg-17489-miserables1.txt"),
    os.path.join(LANE, "data/gutenberg-30513-tocqueville-t1.txt"),
    os.path.join(LANE, "data/gutenberg-30514-tocqueville-t2.txt"),
]

PRON = r"(moi|toi|lui|elle|nous|vous|eux|elles|soi)"
DEM = (r"(cela|ceci|ça|cel[àa]|cec[iy]|celui|ceux|celle|celles)"
       r"(?:[-–— ]?(?:l[àa]|ci))?")
DET = (r"(mon|ma|mes|ton|ta|tes|son|sa|ses|notre|nos|votre|vos|leur|leurs|"
       r"le|la|les|l'|un|une|des|du|de l'|ce|cet|cette|ces|tout|toute|"
       r"tous|toutes|quelque|quelques|chaque|aucun|aucune|plusieurs)")
WORD = r"[a-zàâäçéèêëîïôöùûü'\-]+"
NP = DET + r"\s+" + WORD + r"(?:\s+" + WORD + r"){0,2}"
PROP = r"[A-ZÀÂÄÇÉÈÊËÎÏÔÖÙÛÜ]" + WORD
OTH = (r"(tout le monde|personne|chacun|chacune|rien|quelqu'un|jamais|"
       r"toujours|encore|souvent|rarement|déjà|bientôt|vite|bien|mal|"
       r"mieux|pis)")

TOPIC_PAT = re.compile(
    r"\b(?P<topic>(?P<pron>" + PRON + r")"
    r"|(?P<dem>" + DEM + r")"
    r"|(?P<np>" + NP + r")"
    r"|(?P<prop>" + PROP + r")"
    r"|(?P<oth>" + OTH + r"))\s*[,;:]", re.IGNORECASE)
INF = re.compile(r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)


def topic_class(m):
    for g in ("pron", "dem", "np", "prop", "oth"):
        if m.group(g):
            return g
    return "?"


def windows(text):
    out = []
    for m in TOPIC_PAT.finditer(text):
        seg = text[m.start():m.start() + 200]
        end = re.search(r"[!?.]", seg)
        win = seg[:end.end()] if end else seg
        if "!" not in win:
            continue
        infs = sorted({w.group(0) for w in INF.finditer(win)})
        if not infs:
            continue
        out.append({"class": topic_class(m),
                    "topic": m.group("topic").strip().lower(),
                    "window": win, "inf_hits": infs})
    return out


def census(paths, label):
    total_chars = 0
    files, cands = [], []
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        n_top = len(TOPIC_PAT.findall(t))
        c = windows(t)
        files.append({"file": name, "chars": len(t),
                      "topic_comma_hits": n_top, "excl_candidates": len(c)})
        for w in c:
            w["file"] = name
            cands.append(w)
    cls = {}
    for w in cands:
        cls[w["class"]] = cls.get(w["class"], 0) + 1
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{sum(f['topic_comma_hits'] for f in files)} topic-comma hits, "
          f"{len(cands)} exclamatory candidates {cls}")
    return {"files": files, "total_chars": total_chars,
            "by_class": cls, "candidates": cands}


if __name__ == "__main__":
    c1841 = [os.path.join(CORPUS1841, f) for f in os.listdir(CORPUS1841)
             if f.endswith(".txt") and f not in GERMAN]
    res = {"census_1841_register": census(c1841, "1841 register"),
           "census_wider_19c": census(WIDER, "wider 19c")}
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-topic-inventory-excl-inf_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
