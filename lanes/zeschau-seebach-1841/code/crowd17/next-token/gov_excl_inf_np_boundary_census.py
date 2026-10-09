#!/usr/bin/env python3
r"""Census for battery gov-excl-inf-np-boundary.

Target: inventory the governors (pour / à / de) of the Cause-C near-miss
exclaimed NPs ("des perdreaux à tuer!", "mot pompeux pour dire barbarie!",
"Cinq louis d'or à gagner!", "Quel art pour tout s'approprier!", ...) to
map the NP-vs-infinitive-phrase boundary.

Bar (verbatim): "map the NP-vs-infinitive-phrase boundary with byte
evidence per governor class".

Design: same 21-file corpus as the parent batteries (gov_excl_inf_register_
census.py plumbing). For every "!", take the 160 chars before it, run the
parent's GOV_INF pattern, and flag windows whose governed infinitive is
 plausibly embedded in an exclaimed NP (the "!" belongs to the NP, not the
infinitive phrase). All flagged windows are printed for MANUAL
classification: CAUSE-C = exclaimed NP with embedded governed infinitive;
OTHER = finite matrix / OCR noise / quotation / bare exclamatory infinitive.
Counts per governor (pour / à / de) decide whether the boundary is
governor-level (asymmetry) or phrase-level (NP vs infinitive phrase).
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

# NP-exclamation markers: exclamative determiners, or quantifier/numeral
# offer-NPs ("Cinq louis d'or à gagner", "des perdreaux à tuer").
EXCL_MARK = re.compile(r"\b(quel(le)?s?|que de|combien|tant)\s+de\b", re.IGNORECASE)
EXCL_MARK2 = re.compile(r"\b(quel(le)?s?|combien)\b", re.IGNORECASE)
OFFER_HEAD = re.compile(
    r"\b(des|les|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|cent|mille)\b",
    re.IGNORECASE)

def flags(seg, g):
    """Return the NP-flag reason(s) for a window, or []."""
    head = seg[:g.start()]
    reasons = []
    if EXCL_MARK.search(head) or EXCL_MARK2.search(head):
        reasons.append("exclamative-marker")
    if OFFER_HEAD.search(head) and re.search(r"\bà\b", seg[:g.end()], re.IGNORECASE):
        reasons.append("offer-NP")
    if "!" in head:
        reasons.append("compound-exclamation")
    return reasons

def candidates(text):
    out = []
    for m in re.finditer(r"!", text):
        seg = text[max(0, m.start() - 160):m.start()]
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
        fl = flags(seg, g)
        if not fl:
            continue
        prep = g.group(1).lower()
        if prep == "a":
            prep = "à"   # unaccented "a" normalized by GOV_INF to à
        out.append({"prep": prep,
                    "infinitive_shaped": g.group(0).rsplit(None, 1)[-1].lower(),
                    "dist": len(seg[end:]),
                    "flags": fl,
                    "window": seg.strip() + "!"})
    return out

def census(paths, label):
    total_chars = 0
    files, cands = [], []
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        c = candidates(t)
        files.append({"file": name, "chars": len(t),
                      "bang_count": t.count("!"),
                      "np_flagged": len(c)})
        for w in c:
            w["file"] = name
            cands.append(w)
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{sum(f['bang_count'] for f in files)} '!', "
          f"{len(cands)} NP-flagged candidates")
    return {"files": files, "total_chars": total_chars, "candidates": cands}

if __name__ == "__main__":
    c1841 = [os.path.join(CORPUS1841, f) for f in os.listdir(CORPUS1841)
             if f.endswith(".txt") and f not in GERMAN]
    res = {"census_1841_register": census(c1841, "1841 register"),
           "census_wider_19c": census(WIDER, "wider 19c")}
    out = os.path.join(NT, "gov-excl-inf-np-boundary_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
