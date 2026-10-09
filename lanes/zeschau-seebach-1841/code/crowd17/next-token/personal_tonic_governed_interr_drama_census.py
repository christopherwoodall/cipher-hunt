#!/usr/bin/env python3
r"""Census for battery personal-tonic-governed-interr-drama.

Drama-register interrogative-force variant of personal-tonic-governed-excl-drama:
same 14-play drama corpus and P1/P3 taxonomy VERBATIM; only P2 changes:
window must be TERMINATED by "?" (first terminator = "?"), so the
interrogative force plausibly falls on the infinitive phrase itself.
Windows whose first terminator is "!" or "." are excluded.

P1 (dislocation): r"\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]" (case-insens)
    - window = text from the pronoun through the first [?!.] (inclusive),
      capped at 400 chars.
P2 (interrogative filter): first terminator in the window must be "?".
P3 (governed-infinitive candidate):
    strict: r"\b(?:pour|de|d'|d'|à)\s+[a-z…]{2,}(er|ir|re|oir)\b"
    loose (clitic-tolerant, tagged separately): same with up to 2
    intervening short words.

Corpus: the drama ingest at code/side-period/corpus/ — 14 unique plays,
hugo-hernani.txt (Hetzel 1889 duplicate edition) EXCLUDED, one edition
per play per the queue gate (same set as personal_tonic_governed_excl_drama_census.py).

Output: JSON with candidates + ±700-char context for manual classification.
Gates for genuine (stated in the interrogative bar):
  G1 pronoun is a dislocated tonic topic (understood subject of infinitive)
  G2 pour/de/à-governed infinitive present
  G3 the "?" plausibly terminates the infinitive phrase itself
     (question force on the infinitive)
  G4 no finite verb governing the infinitive inside the window
     (self-contained turn/utterance)
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DRAMADIR = os.path.join(LANE, "code/side-period/corpus")
EXCLUDE = {"hugo-hernani.txt"}
FILES = [
    "hugo-hernani-1870.txt",
    "hugo-burgraves.txt",
    "hugo-ruy-blas.txt",
    "dumas-mariage-louis-xv-1841.txt",
    "dumas-antony.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "dumas-tour-de-nesle.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
    "vigny-chatterton-1835.txt",
    "musset-comedies-proverbes-1850.txt",
]
PRON = re.compile(r"\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]", re.IGNORECASE)
GOV_INF_STRICT = re.compile(
    r"\b(?:pour|de|d'|d’|à)\s+"
    r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
GOV_INF_LOOSE = re.compile(
    r"\b(?:pour|de|d'|d’|à)\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü']{1,4}\s+){1,2}"
    r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
TERMINATOR = re.compile(r"[?!.]")


def windows(text, fname):
    out = []
    for m in PRON.finditer(text):
        seg = text[m.start():m.start() + 400]
        t = TERMINATOR.search(seg)
        if not t:
            continue
        if t.group(0) != "?":
            continue  # first terminator must be interrogative
        win = seg[: t.end()]
        strict = sorted({w.group(0).lower() for w in GOV_INF_STRICT.finditer(win)})
        loose = sorted({w.group(0).lower() for w in GOV_INF_LOOSE.finditer(win)
                        if w.group(0).lower() not in strict})
        if not strict and not loose:
            continue
        ctx_start = max(0, m.start() - 700)
        ctx = text[ctx_start:m.start() + 700].replace("\n", " / ")
        out.append({"file": fname, "offset": m.start(),
                    "pron": m.group(1).lower(), "window": win,
                    "strict_gov_inf": strict, "loose_gov_inf": loose,
                    "context": ctx})
    return out


def main():
    files, cands = [], []
    total = 0
    on_disk = {f for f in os.listdir(DRAMADIR) if f.endswith(".txt")}
    missing = [f for f in FILES if f not in on_disk]
    if missing:
        raise SystemExit("GATE FAIL: missing drama files: " + ", ".join(missing))
    assert "hugo-hernani.txt" in on_disk, \
        "GATE FAIL: expected duplicate Hernani edition absent"
    for f in FILES:
        p = os.path.join(DRAMADIR, f)
        text = open(p, encoding="utf-8", errors="replace").read()
        total += len(text)
        n_pron = len(PRON.findall(text))
        c = windows(text, f)
        cands.extend(c)
        print(f"{f}: {len(text)} chars, {n_pron} pron-comma hits, "
              f"{len(c)} governed-interr candidates")
        files.append({"file": f, "chars": len(text),
                      "pron_comma_hits": n_pron,
                      "gov_interr_candidates": len(c)})
    n_strict = sum(1 for c in cands if c["strict_gov_inf"])
    n_loose = sum(1 for c in cands if c["loose_gov_inf"] and not c["strict_gov_inf"])
    print(f"TOTAL: {len(files)} unique plays, {total} chars, "
          f"{sum(f['pron_comma_hits'] for f in files)} pron-comma hits, "
          f"{len(cands)} governed-interrogative candidates "
          f"({n_strict} strict, {n_loose} loose-only)")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "personal-tonic-governed-interr-drama_census.json")
    json.dump({"files": files, "total_chars": total, "candidates": cands,
               "note": "hugo-hernani.txt (Hetzel 1889) excluded: duplicate "
                       "Hernani edition; ONE edition per play per queue gate"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
