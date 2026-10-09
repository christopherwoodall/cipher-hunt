#!/usr/bin/env python3
r"""Census for battery reinforced-modal-inf-prose.

Target: run the SAME modal/perception P1/P2/P3 search as
reinforced_modal_inf_drama_census.py on the 27.66M-char 19th-century
PROSE corpus (the 20-file prose set used by the personal-tonic family).

Definitions (verbatim from the drama parent):
  P1 (dislocation): DEM_REINF = reinforced demonstrative head
      (celui|celle|ceux|celles)-là / -ci (also çà-là/çà-ci), followed by
      [,;:]. Window = from the demonstrative through the next [!?.],
      capped at 180 chars.
  P2 (exclamatory filter): window must contain "!".
  P3 (modal/perception-governed bare infinitive): a modal, perception, or
      causative verb form followed by a bare infinitive (er/ir/re/oir
      ending), applied to the window text AFTER the comma.

Corpus: 20 prose files (corpus + data dirs), ~27.66M chars.
Output: reinforced-modal-inf-prose_census.json
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUSDIR = os.path.join(LANE, "code/side-period/corpus")
DATADIR = os.path.join(LANE, "data")

FILES = [
    (CORPUSDIR, "guizot-memoires-t1-gutenberg.txt"),
    (CORPUSDIR, "guizot-memoires-t2-gutenberg.txt"),
    (CORPUSDIR, "guizot-memoires-t3-gutenberg.txt"),
    (CORPUSDIR, "guizot-memoires-t5-t6.txt"),
    (CORPUSDIR, "nesselrode-v7.txt"),
    (CORPUSDIR, "nesselrode-v8.txt"),
    (CORPUSDIR, "nesselrode-v9.txt"),
    (CORPUSDIR, "nesselrode-v10.txt"),
    (CORPUSDIR, "revue-deux-mondes-1841-q1.txt"),
    (CORPUSDIR, "revue-deux-mondes-1841-q2.txt"),
    (CORPUSDIR, "revue-deux-mondes-1841-q3.txt"),
    (CORPUSDIR, "revue-deux-mondes-1841-q4.txt"),
    (CORPUSDIR, "metternich-papiere-v4.txt"),
    (CORPUSDIR, "metternich-papiere-v6.txt"),
    (CORPUSDIR, "talleyrand-memoires-v1.txt"),
    (CORPUSDIR, "pozzo-di-borgo-correspondance-v1.txt"),
    (CORPUSDIR, "levant-correspondence-1841-p3.txt"),
    (DATADIR, "gutenberg-17489-miserables1.txt"),
    (DATADIR, "gutenberg-30513-tocqueville-t1.txt"),
    (DATADIR, "gutenberg-30514-tocqueville-t2.txt"),
]

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)

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

MOD_INF = re.compile(
    r"\b" + GOV + r"\s+(?:" + CLITIC + r"\s+){0,3}" + INF + r"\b",
    re.IGNORECASE)

def windows(text, fname):
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
        out.append({"file": fname, "offset": m.start(),
                    "dem": m.group(1).lower(), "window": win,
                    "mod_inf_hits": sorted(set(hits))})
    return out

def main():
    total_chars = 0
    files, cands = [], []
    for d, name in FILES:
        p = os.path.join(d, name)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        n_dem = len(DEM_REINF.findall(t))
        c = windows(t, name)
        files.append({"file": name, "chars": len(t),
                      "dem_comma_hits": n_dem, "mod_inf_candidates": len(c)})
        cands.extend(c)
    print(f"prose: {len(files)} files, {total_chars} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{len(cands)} modal/perception-inf candidates")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-modal-inf-prose_census.json")
    json.dump({"files": files, "total_chars": total_chars,
               "candidates": cands}, open(out, "w"),
              ensure_ascii=False, indent=1)
    print("wrote", out)

if __name__ == "__main__":
    main()
