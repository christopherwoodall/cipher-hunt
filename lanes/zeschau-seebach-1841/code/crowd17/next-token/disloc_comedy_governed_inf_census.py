#!/usr/bin/env python3
r"""Census for battery disloc-comedy-governed-inf.

Follow-up #2 of the NULL battery-disloc-comedy-bare-heads-extension
(2026-10-09). That battery fenced the BARE-head bare-exclamatory-infinitive
shape in comedy (0 genuine in 465,531 chars) but noted a near-miss at
scribe-le-savant.txt @4840 ("a etre malade, a se tuer !" — preposition-
governed). THIS battery censuses the GOVERNED shape (pour/a/de + infinitive
as the exclaimed element, any topic) in the same comedy corpus, mirroring
gov-excl-inf-register-drama's register-boundary logic.

Bar (verbatim, pre-registered): ">=1 genuine in comedy tests whether the
fence holds exactly at BARE (mirroring gov-excl-inf-register-drama's
register-boundary logic); confirmed zero fences the governed shape in
comedy too"

Search patterns (verbatim, identical to gov_excl_inf_register_drama_census.py):
  P1 (candidate): for every "!" in the corpus, take the 120 chars before
      it. Run GOV_INF on that segment:
      r"\b(pour|a|de|d['’])\s+(?:[a-z...]{1,6}\s+){0,2}\b[a-z...]{2,}(er|ir|re|oir)\b"
      (case-insensitive). Keep the match closest to the "!"; between its end
      and the "!" there must be no [.;]. dist = chars from the end of the
      infinitive-shaped word to the "!".
  P2 (banding): tight band dist<=40 is the discriminating band; wide band
      40<dist<=120 triaged separately. All candidates are printed for MANUAL
      classification.

Corpus: the 6 comedy-extension files censused by the parent battery
(scribe-le-savant, scribe-le-lorgnon, labiche-voyage-perrichon,
labiche-la-cagnotte, labiche-29-degres-ombre, labiche-affaire-rue-lourcine).
The 4 other comedy-authored files (scribe-bertrand-et-raton,
scribe-verre-d-eau, labiche-chapeau-de-paille, labiche-martin-poudre-aux-yeux)
are EXCLUDED with cause: they were censused as drama by
gov-excl-inf-register-drama (which found 1 genuine there); including them
would double-count the drama finding as a comedy attestation.

Output: disloc-comedy-governed-inf_census.json with per-file sizes, band
counts, and all candidate windows + dist; human classification in the
battery report.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

COMEDY = [
    "labiche-29-degres-ombre.txt",
    "labiche-affaire-rue-lourcine.txt",
    "labiche-la-cagnotte.txt",
    "labiche-voyage-perrichon.txt",
    "scribe-le-lorgnon.txt",
    "scribe-le-savant.txt",
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
    paths = [os.path.join(CORPUS, f) for f in COMEDY]
    missing = [p for p in paths if not os.path.exists(p)]
    assert not missing, f"missing corpus files: {missing}"
    res = {"census_comedy": census(paths, "comedy register")}
    out = os.path.join(NT, "disloc-comedy-governed-inf_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
