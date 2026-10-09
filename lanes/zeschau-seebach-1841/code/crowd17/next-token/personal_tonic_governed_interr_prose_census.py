#!/usr/bin/env python3
r"""Census for battery personal-tonic-governed-interr-prose.

Interrogative-force variant of personal-tonic-governed-excl-prose-recall:
same prose corpus and P1/P3 taxonomy VERBATIM; only P2 changes:
window must be TERMINATED by "?" (first terminator = "?"), so the
interrogative force plausibly falls on the infinitive phrase itself.
Windows whose first terminator is "!" are excluded (exclamatory arm already
fenced separately).

P1 (dislocation): r"\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]" (case-insens)
    - window = text from the pronoun through the next [?!.] (inclusive),
      capped at 400 chars.
P2 (interrogative filter): window must contain "?" and the FIRST terminator
    in the window must be "?".
P3 (governed-infinitive candidate):
    strict: r"\b(?:pour|de|d'|d’|à)\s+[a-z…]{2,}(er|ir|re|oir)\b"
    loose (clitic-tolerant, tagged separately): same with up to 2
    intervening short words.

Corpus: identical 20-file prose set from
personal_tonic_governed_excl_prose_recall_census.py.

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
    for d, f in FILES:
        p = os.path.join(d, f)
        if not os.path.isfile(p):
            raise SystemExit("GATE FAIL: missing prose file: " + p)
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
    print(f"TOTAL: {len(files)} files, {total} chars, "
          f"{sum(f['pron_comma_hits'] for f in files)} pron-comma hits, "
          f"{len(cands)} governed-interrogative candidates "
          f"({n_strict} strict, {n_loose} loose-only)")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "personal-tonic-governed-interr-prose_census.json")
    json.dump({"files": files, "total_chars": total, "candidates": cands,
               "note": "interrogative-force variant of "
                       "personal-tonic-governed-excl-prose-recall; "
                       "first terminator must be '?'"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
