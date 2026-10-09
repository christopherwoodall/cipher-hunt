#!/usr/bin/env python3
r"""Census for battery gov-excl-inf-drama-n3.

Re-runs the IDENTICAL P1/P2 governed-infinitive census (any topic)
against the FULL 35-file drama corpus (all widenings) in one pass,
to verify the cumulative genuine count and resolve the n2/comedy-skew
arithmetic discrepancy (n=6/n=10 vs the 12-window list).

P1/P2 verbatim from gov_excl_inf_register_drama_census.py (via
gov_excl_inf_drama_n2_census.py). Corpus pinned by name; the
duplicate hugo-hernani.txt edition is excluded (one edition per play).

Bar (verbatim, pre-registered): "genuine count rises above n=2
(gov-excl-inf-recall-drama's count) with multi-playwright attestation;
else fence as drama-concentrated".

Output: gov-excl-inf-drama-n3_census.json with per-file sizes,
bang counts, candidate totals, and all candidate windows
(+byte_offset = absolute terminator offset for byte verification).
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

# Parent battery gov-excl-inf-register-drama (14)
PARENT = [
    "dumas-antony.txt", "dumas-henri-iii.txt", "dumas-kean.txt",
    "dumas-mariage-louis-xv-1841.txt", "dumas-tour-de-nesle.txt",
    "hugo-burgraves.txt", "hugo-hernani-1870.txt", "hugo-ruy-blas.txt",
    "labiche-chapeau-de-paille.txt", "labiche-martin-poudre-aux-yeux.txt",
    "musset-comedies-proverbes-1850.txt", "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt", "vigny-chatterton-1835.txt",
]
# n2 widening (14): 3 new Scribe + 11 new Labiche
N2 = [
    "scribe-charlatanisme.txt", "scribe-le-lorgnon.txt", "scribe-le-savant.txt",
    "labiche-29-degres-ombre.txt", "labiche-affaire-rue-lourcine.txt",
    "labiche-baron-fourchevif.txt", "labiche-doit-on-le-dire.txt",
    "labiche-edgard-bonne.txt", "labiche-la-cagnotte.txt", "labiche-main-leste.txt",
    "labiche-misanthrope-auvergnat.txt", "labiche-noces-bouchencoeur.txt",
    "labiche-prix-martin.txt", "labiche-voyage-perrichon.txt",
]
# comedy-skew widening (7): non-comic drama
COMEDY_SKEW = [
    "hugo-roi-samuse.txt", "hugo-lucrece-borgia.txt", "hugo-marie-tudor.txt",
    "hugo-angelo.txt", "musset-lorenzaccio.txt",
    "dumas-fils-dame-camelias.txt", "ponsard-lucrece.txt",
]
FILES = PARENT + N2 + COMEDY_SKEW
assert len(FILES) == 35 and len(set(FILES)) == 35

GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['\u2019])\s+"
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
                    "byte_offset": m.start(),   # absolute terminator offset
                    "window": seg + "!"})
    return out

def main():
    paths = [os.path.join(CORPUS, f) for f in FILES]
    missing = [p for p in paths if not os.path.exists(p)]
    assert not missing, f"missing corpus files: {missing}"
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
    print(f"=== drama-n3 full corpus: {len(files)} files, {total_chars} chars, "
          f"{sum(f['bang_count'] for f in files)} '!', {len(cands)} candidates "
          f"(tight<=40: {sum(f['candidates_tight_le40'] for f in files)})")
    out = os.path.join(NT, "gov-excl-inf-drama-n3_census.json")
    json.dump({"files": files, "total_chars": total_chars,
               "candidates": cands}, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)

if __name__ == "__main__":
    main()
