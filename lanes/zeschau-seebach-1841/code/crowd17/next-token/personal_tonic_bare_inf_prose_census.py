#!/usr/bin/env python3
r"""Census for battery personal-tonic-bare-inf-prose-inventory.

Target: ranked head-class inventory of BARE exclamatory infinitives under
tonic-pronoun topics in the 27.66M-char prose corpus.

Prose-register counterpart of disloc-tonic-personal-census (drama, PROMOTE:
21 genuine bare exclamatory infinitives under dislocated personal tonic
pronouns). Follow-up #1 of personal-tonic-governed-excl-prose (NULL: governed
shape fenced in prose; window [14] shows the BARE shape lives in prose too).

Bar (pre-registered): "Ranked head-class inventory of BARE exclamatory
infinitives under tonic-pronoun topics in the prose corpus."

Search patterns (VERBATIM from the drama sibling):
  P1 (dislocation): r"\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]" (case-insens)
      - window = text from the pronoun through the next [!?.] (inclusive),
        capped at 180 chars.
  P2 (exclamatory filter): window must contain "!" before its end.
  P3 (infinitive candidate): r"\b[a-z…]{2,}(er|ir|re|oir)\b" on the window.
  Candidates are printed for MANUAL classification (regex cannot judge
  exclamatory illocutionary force, topic status, or governed-vs-bare).

Corpus (VERBATIM 20-file set from personal-tonic-governed-excl-prose):
  - 1841-register prose (code/side-period/corpus/): 17 files.
  - Wider 19th century (data/): 3 files.

Output: JSON with candidates + wider context for manual classification.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUSDIR = os.path.join(LANE, "code/side-period/corpus")
DATADIR = os.path.join(LANE, "data")
FILES = [  # (dir, filename) — identical to the parent prose battery's corpus
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
INF = re.compile(r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
                 re.IGNORECASE)


def windows(text, fname):
    out = []
    for m in PRON.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        infs = sorted({w.group(0).lower() for w in INF.finditer(win)})
        if not infs:
            continue
        ctx_start = max(0, m.start() - 300)
        ctx = text[ctx_start:m.start() + 350].replace("\n", " / ")
        out.append({"file": fname, "offset": m.start(),
                    "pron": m.group(1).lower(), "window": win,
                    "inf_shaped": infs, "context": ctx})
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
              f"{len(c)} bare-inf candidates")
        files.append({"file": f, "chars": len(text),
                      "pron_comma_hits": n_pron,
                      "bare_inf_candidates": len(c)})
    print(f"TOTAL: {len(files)} files, {total} chars, "
          f"{sum(f['pron_comma_hits'] for f in files)} pron-comma hits, "
          f"{len(cands)} bare-infinitive candidates")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "personal-tonic-bare-inf-prose-inventory_census.json")
    json.dump({"files": files, "total_chars": total, "candidates": cands,
               "note": "prose corpus identical to "
                       "personal-tonic-governed-excl-prose"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
