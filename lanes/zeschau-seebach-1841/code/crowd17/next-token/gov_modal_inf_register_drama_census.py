#!/usr/bin/env python3
r"""Census for battery gov-modal-inf-register-drama.

Target: corpus-wide census of MODAL/PERCEPTION-governed exclamatory
infinitives in the 14-play drama corpus with ANY topic (the head/topic
restriction of reinforced-modal-inf-drama is dropped here).

Method (mirrors gov_excl_inf_register_drama_census.py exactly):
  P1 (candidate): for every "!" in the corpus, take the 120 chars before
      it. Run MOD_INF on that segment:
        <governor> (clitics 0-3) <bare infinitive>
      governor = modal/perception/causative forms (finite, infinitive,
      participle, impersonal "il faut").
      The match closest to the "!" is kept; between its end and the "!"
      there must be no [.;]. dist = chars from end of infinitive to "!".
  P2 (banding): tight band dist<=40 is the discriminating band; wider
      band 40<dist<=120 triaged separately.
  All candidates printed for MANUAL classification (genuine = governed
  exclamatory infinitive; the infinitive is governed by a modal /
  perception / causative verb and the phrase stands as an exclamation).

Corpus: the same 14 distinct-play drama files as gov-excl-inf-register-drama
(one edition per play: hugo-hernani-1870.txt, hugo-hernani.txt excluded).

Output: gov-modal-inf-register-drama_census.json
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

DRAMA = [
    "dumas-antony.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "dumas-mariage-louis-xv-1841.txt",
    "dumas-tour-de-nesle.txt",
    "hugo-burgraves.txt",
    "hugo-hernani-1870.txt",   # one edition per play; hugo-hernani.txt excluded
    "hugo-ruy-blas.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
    "musset-comedies-proverbes-1850.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "vigny-chatterton-1835.txt",
]

GOV = (
    r"(?:il\s+fau(?:t|llait|dra|drait)|"
    r"faire|fais|fait|font|faisons|faites|ferez|ferait|faisant|"
    r"laisser|laisse|laisses|laissé|laissez|laissons|laisseront|laisserait|"
    r"pouvoir|peux|peut|pouvons|pouvez|peuvent|pourrai|pourra|pouvait|pourrait|"
    r"vouloir|veux|veut|voulons|voulez|veulent|voudrait|"
    r"devoir|dois|doit|devons|devez|doivent|devrait|"
    r"savoir|sais|sait|savons|savez|savent|saurait|"
    r"voir|vois|voit|voyons|voyez|voient|verra|verrait|voyant|vu|"
    r"regarder|regarde|regardes|regardez|regardons|"
    r"entendre|entends|entend|entendons|entendez|"
    r"écouter|écoute|écoutes|écoutez|écoutons|"
    r"sentir|sens|sent|sentez)"
)

CLITIC = (r"(?:l[ea]|les|se|s['\u2019]|nous|vous|me|m['\u2019]|te|t['\u2019]|"
          r"lui|leur|y|en|n['\u2019]|moi|toi|soi)")

INF = r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)"

MOD_INF = re.compile(
    r"\b" + GOV + r"\s+(?:" + CLITIC + r"\s+){0,3}" + INF + r"\b",
    re.IGNORECASE)

def candidates(text):
    out = []
    for m in re.finditer(r"!", text):
        seg = text[max(0, m.start() - 120):m.start()]
        best = None
        for g in MOD_INF.finditer(seg):
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
        inf_word = g.group(0).rsplit(None, 1)[-1].lower()
        gov_part = g.group(0)[:-(len(g.group(0).rsplit(None, 1)[-1]))].strip().lower()
        out.append({"governor": gov_part,
                    "match": g.group(0).lower(),
                    "infinitive_shaped": inf_word,
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
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{sum(f['bang_count'] for f in files)} bangs, "
          f"{sum(f['candidates_total'] for f in files)} candidates total, "
          f"{sum(f['candidates_tight_le40'] for f in files)} tight (<=40)")
    return {"files": files, "total_chars": total_chars, "candidates": cands}

if __name__ == "__main__":
    res = {"census_drama": census([os.path.join(CORPUS, f) for f in DRAMA],
                                  "drama register, modal/perception-governed (14 plays, 1 ed/play)")}
    out = os.path.join(NT, "gov-modal-inf-register-drama_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
