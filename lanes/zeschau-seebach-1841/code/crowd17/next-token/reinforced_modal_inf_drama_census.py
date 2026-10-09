#!/usr/bin/env python3
r"""Census for battery reinforced-modal-inf-drama.

Target: census reinforced-demonstrative heads + MODAL/PERCEPTION-governed
bare exclamatory infinitive in the 19th-century French DRAMA corpus.

Definitions (same as reinforced-pour-inf-drama):
  P1 (dislocation): DEM_REINF = reinforced demonstrative head
      (celui|celle|ceux|celles)-là / -ci (also çà-là/çà-ci), followed by
      [,;:]. Window = from the demonstrative through the next [!?.],
      capped at 180 chars.
  P2 (exclamatory filter): window must contain "!".
  P3 (modal/perception-governed bare infinitive): a modal, perception, or
      causative verb form followed by a bare infinitive (er/ir/re/oir
      ending), applied to the window text AFTER the comma.

Corpus: same 14 distinct-play drama files as reinforced-pour-inf-drama
(one edition per play; hugo-hernani-1870.txt excluded, spot-checked
separately).

Output: reinforced-modal-inf-drama_census.json with per-file sizes,
hit counts, and all candidate windows (classified by hand).
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

DRAMA = [
    "dumas-mariage-louis-xv-1841.txt",
    "vigny-chatterton-1835.txt",
    "musset-comedies-proverbes-1850.txt",
    "hugo-hernani.txt",
    "hugo-ruy-blas.txt",
    "hugo-burgraves.txt",
    "dumas-antony.txt",
    "dumas-tour-de-nesle.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
]
EXCLUDED_EDITION = "hugo-hernani-1870.txt"

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)

# Modal / perception / causative governor forms (indicative, subjunctive,
# imperative, conditional, infinitive — plus participles for "faire").
GOV = (
    r"(?:faire|fais|fait|font|faisons|faites|ferez|ferait|faisant|"
    r"laisser|laisse|laisses|laissé|laissez|laissons|laisseront|laisserait|"
    r"pouvoir|peux|peut|pouvons|pouvez|peuvent|pourrai|pourra|pouvait|"
    r"vouloir|veux|veut|voulons|voulez|veulent|voudrait|"
    r"devoir|dois|doit|devons|devez|doivent|devrait|"
    r"savoir|sais|sait|savons|savez|savent|saurait|"
    r"voir|vois|voit|voyons|voyez|voient|verra|verrait|voyant|vu|"
    r"regarder|regarde|regardes|regardez|regardons|"
    r"entendre|entends|entend|entendons|entendez|"
    r"\u00e9couter|\u00e9coute|\u00e9coutes|\u00e9coutez|\u00e9coutons|"
    r"sentir|sens|sent|sentez|senteur)"
)

CLITIC = r"(?:l[ea]|les|se|s['\u2019]|nous|vous|me|m['\u2019]|te|t['\u2019]|lui|leur|y|en|n['\u2019])"

INF = r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)"

# <governor> [0-3 clitics] <bare infinitive>
MOD_INF = re.compile(
    r"\b" + GOV + r"\s+(?:" + CLITIC + r"\s+){0,3}" + INF + r"\b",
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
        hits = [(g.group(0).lower()) for g in MOD_INF.finditer(after_comma)]
        if not hits:
            continue
        out.append({"dem": m.group(1).lower(), "window": win,
                    "mod_inf_hits": sorted(set(hits))})
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
                      "dem_comma_hits": n_dem, "mod_inf_candidates": len(c)})
        for w in c:
            w["file"] = name
            cands.append(w)
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{len(cands)} modal/perception-inf candidates")
    return {"files": files, "total_chars": total_chars, "candidates": cands}

if __name__ == "__main__":
    res = {"census_drama": census(DRAMA, "drama register (14 plays, 1 ed/play)"),
           "excluded_edition_note": f"{EXCLUDED_EDITION} excluded per one-edition-per-play rule; spot-checked separately"}
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-modal-inf-drama_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
