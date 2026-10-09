#!/usr/bin/env python3
r"""Census for battery disloc-tonic-personal-census.

Target: positive-space census of dislocated PERSONAL tonic pronouns
(moi, toi, lui, elle, nous, vous, eux) + bare exclamatory infinitive
("Moi, voler !") in the ingested 19th-century French drama register.

Search patterns (mirroring the sibling disloc_demonstrative_drama_reinforced
census taxonomy):
  P1 (dislocation): r"PRON\s*[,;:]" where PRON =
      (moi|toi|lui|elle|nous|vous|eux) — word-boundary, case-insensitive.
      - window = text from the pronoun through the next [!?.]
        (inclusive), capped at 180 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (infinitive candidate): r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      on the window text; candidates are printed for MANUAL classification
      (regex cannot separate -er infinitives from nouns/adjectives in -er,
      nor finite verb forms).

Corpus: the drama ingest at code/side-period/corpus/ — 14 unique plays,
Hernani in TWO editions (hugo-hernani-1870.txt, Jenkins 1870 archive.org
OCR; hugo-hernani.txt, Hetzel 1889 wikisource) — per the queue note and
PROVENANCE.md ONE edition per play is used: hugo-hernani.txt is EXCLUDED,
hugo-hernani-1870.txt kept (the gate-ingest edition used by the sibling
batteries).

Prior null context (battery-disloc-demonstrative-drama-reinforced, null
2026-10-09): reinforced demonstrative heads never license bare exclamatory
infinitives in drama (0/8 genuine in 2,969,582 chars), but the register
HAS bare exclamatory infinitives (Hernani "Gouverner tout cela !") — the
licensor class of the positive cases is open. This census tests the
personal-tonic-pronoun arm of the tonic-fronting frame.

Output: JSON list of candidate windows; human classification happens in
the battery report. Files named, sizes in characters, patterns exact.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DRAMADIR = os.path.join(LANE, "code/side-period/corpus")
# 14 unique plays: all drama ingest files except the duplicate Hernani
# edition (hugo-hernani.txt — Hetzel 1889; hugo-hernani-1870.txt is the
# gate-ingest edition and stays).
FILES = [
    "hugo-hernani-1870.txt",      # Victor Hugo, Hernani (Jenkins 1870)
    "hugo-burgraves.txt",         # Victor Hugo, Les Burgraves
    "hugo-ruy-blas.txt",          # Victor Hugo, Ruy Blas (1839 ed.)
    "dumas-mariage-louis-xv-1841.txt",  # Dumas père, Un mariage sous Louis XV
    "dumas-antony.txt",           # Dumas père, Antony
    "dumas-henri-iii.txt",        # Dumas père, Henri III
    "dumas-kean.txt",             # Dumas père, Kean
    "dumas-tour-de-nesle.txt",    # Dumas père, La Tour de Nesle
    "scribe-bertrand-et-raton.txt",    # Eugène Scribe, Bertrand et Raton
    "scribe-verre-d-eau.txt",          # Eugène Scribe, Le Verre d'eau (éd. 1861)
    "labiche-chapeau-de-paille.txt",   # Labiche & Marc-Michel, Chapeau de paille
    "labiche-martin-poudre-aux-yeux.txt",  # Labiche & É. Martin, Poudre aux yeux
    "vigny-chatterton-1835.txt",  # Alfred de Vigny, Chatterton
    "musset-comedies-proverbes-1850.txt",  # Musset, Comédies et proverbes (10 plays)
]
# Personal tonic pronouns: moi, toi, lui, elle, nous, vous, eux.
# Note: lui also indirect object, elle also subject pronoun, vous also
# subject — all such confounds are resolved by MANUAL classification of
# the candidate windows, which is why P1 is a coarse net.
PRON = re.compile(r"\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]", re.IGNORECASE)
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

def windows(text):
    out = []
    for m in PRON.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        out.append({"pron": m.group(1).lower(), "window": win,
                    "inf_hits": sorted({w.group(0).lower()
                                        for w in INF.finditer(win)})})
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
        c = windows(text)
        for w in c:
            w["file"] = f
            cands.append(w)
        print(f"{f}: {len(text)} chars, {n_pron} pron-comma hits, "
              f"{len(c)} exclamatory candidates")
        files.append({"file": f, "chars": len(text),
                      "pron_comma_hits": n_pron,
                      "excl_candidates": len(c)})
    print(f"TOTAL: {len(files)} unique plays, {total} chars, "
          f"{sum(f['pron_comma_hits'] for f in files)} pron-comma hits, "
          f"{len(cands)} exclamatory candidates")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-tonic-personal-census.json")
    json.dump({"files": files, "total_chars": total,
               "candidates": cands,
               "note": "hugo-hernani.txt (Hetzel 1889) excluded: duplicate "
                       "Hernani edition; ONE edition per play per queue gate"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)

if __name__ == "__main__":
    main()
