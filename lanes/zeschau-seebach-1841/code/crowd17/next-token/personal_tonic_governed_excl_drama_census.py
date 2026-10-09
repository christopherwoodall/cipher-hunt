#!/usr/bin/env python3
r"""Census for battery personal-tonic-governed-excl-drama.

Target: test whether personal tonic topics (moi/toi/lui/elle/nous/vous/eux)
license the GOVERNED exclamatory infinitive in drama ("Moi, pour rire !" shape).
Combines the P1/P2 taxonomy of disloc_tonic_personal_census.py with the
preposition-led governed-infinitive P3 of disloc_reinforced_prep_inf_drama_census.py.

Bar (pre-registered): ">=1 genuine opens the licensor class to tonic
pronouns; confirmed zero generalizes the reinforced-head fence to all
dislocated topics".

Search patterns:
  P1 (dislocation): r"\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]" (case-insens)
      - window = text from the pronoun through the next [!?.] (inclusive),
        capped at 180 chars.
  P2 (exclamatory filter): window must contain "!" before its end.
  P3 (governed-infinitive candidate):
      strict: r"\b(?:pour|de|d'|d'|à)\s+[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      loose (clitic-tolerant escapees, tagged separately):
      r"\b(?:pour|de|d'|d’|à)\s+(?:[a-zàâäçéèêëîïôöùûü']{1,4}\s+){1,2}"
      r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
  Candidates are printed for MANUAL classification (regex cannot judge
  exclamatory illocutionary force, nor whether the pronoun is the topic).

Corpus: the drama ingest at code/side-period/corpus/ — 14 unique plays,
hugo-hernani.txt (Hetzel 1889 duplicate edition) EXCLUDED, one edition
per play per the queue gate.

Output: JSON with candidates + wider context for manual classification.
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


def windows(text, fname):
    out = []
    for m in PRON.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        strict = sorted({w.group(0).lower() for w in GOV_INF_STRICT.finditer(win)})
        loose = sorted({w.group(0).lower() for w in GOV_INF_LOOSE.finditer(win)
                        if w.group(0).lower() not in strict})
        if not strict and not loose:
            continue
        ctx_start = max(0, m.start() - 300)
        ctx = text[ctx_start:m.start() + 350].replace("\n", " / ")
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
              f"{len(c)} governed-excl candidates")
        files.append({"file": f, "chars": len(text),
                      "pron_comma_hits": n_pron,
                      "gov_excl_candidates": len(c)})
    n_strict = sum(1 for c in cands if c["strict_gov_inf"])
    n_loose = sum(1 for c in cands if c["loose_gov_inf"] and not c["strict_gov_inf"])
    print(f"TOTAL: {len(files)} unique plays, {total} chars, "
          f"{sum(f['pron_comma_hits'] for f in files)} pron-comma hits, "
          f"{len(cands)} governed-exclamatory candidates "
          f"({n_strict} strict, {n_loose} loose-only)")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "personal-tonic-governed-excl-drama_census.json")
    json.dump({"files": files, "total_chars": total, "candidates": cands,
               "note": "hugo-hernani.txt (Hetzel 1889) excluded: duplicate "
                       "Hernani edition; ONE edition per play per queue gate"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
