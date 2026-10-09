#!/usr/bin/env python3
r"""Census for battery gov-excl-inf-register-drama.

Follow-up #1 of the NULL battery-gov-excl-inf-register (2026-10-09).
The prose battery found 0 genuine governed exclamatory infinitives in
27.66M chars of 19th-century French print. THIS battery runs the
IDENTICAL P1/P2 governed-infinitive census (any topic) against the
ingested drama corpus (14 distinct plays, one edition per play),
testing whether the zero is print-register-specific or generalizes.

Bar (verbatim, pre-registered): ">=1 genuine governed exclamatory
infinitive with a non-demonstrative topic in drama locates the register
boundary; confirmed zero generalizes the prose null".

Search patterns (verbatim, identical to gov_excl_inf_register_census.py):
  P1 (candidate): for every "!" in the corpus, take the 120 chars before
      it. Run GOV_INF on that segment:
      r"\b(pour|à|a|de|d['’])\s+(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}
       \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b" (case-insensitive).
      The match closest to the "!" is kept; between its end and the "!"
      there must be no [.;]. dist = chars from the end of the
      infinitive-shaped word to the "!".
  P2 (banding): tight band dist<=40 is the discriminating band; wider
      band 40<dist<=120 triaged separately.
  All candidates are printed for MANUAL classification.

Corpus: code/side-period/corpus/ drama files only (14 distinct plays,
one edition per play: hugo-hernani-1870.txt kept, hugo-hernani.txt
excluded per the corpus note). German files, the 1841-prose files
(guizot, nesselrode, revue-deux-mondes, metternich, talleyrand,
pozzo-di-borgo, levant), PROVENANCE.md, and harvest-log.txt excluded.

Output: gov-excl-inf-register-drama_census.json with per-file sizes,
band counts, and all candidate windows + dist; human classification in
the battery report.
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
    paths = [os.path.join(CORPUS, f) for f in DRAMA]
    missing = [p for p in paths if not os.path.exists(p)]
    assert not missing, f"missing corpus files: {missing}"
    res = {"census_drama": census(paths, "drama register")}
    out = os.path.join(NT, "gov-excl-inf-register-drama_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
