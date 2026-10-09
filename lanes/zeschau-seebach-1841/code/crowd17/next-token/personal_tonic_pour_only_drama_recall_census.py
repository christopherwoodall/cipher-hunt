#!/usr/bin/env python3
r"""Census for battery personal-tonic-pour-only-drama-recall.

Follow-up #1 from NULL battery-personal-tonic-pour-inf-drama-corpus
(2026-10-09): pour-only tonic-pronoun net with the sibling's recall
widening — 400-char windows + '?'-termination — on the 14-play drama
corpus. Mirrors the sibling recall battery
(battery-personal-tonic-governed-excl-recall, 356 candidates, 0 genuine),
restricted to the pour-only governor.

Bar (pre-registered, verbatim): ">=1 genuine under the widened net re-opens
the pour-governor question; a confirmed zero closes the recall gap for the
pour governor at drama level."

Search patterns (parent taxonomy, pour-only; recall window):
  P1 (dislocation): r"\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]" (case-insens)
      - window = text from the pronoun through the next [!?] (inclusive),
        capped at 400 chars (parent: 180 chars, [!?.]).
  P2 (exclamatory filter): window must contain "!" or "?" (automatic: window
      always terminates on "!" or "?"; kept as an explicit gate).
  P3 (pour-governed-infinitive candidate):
      strict: r"\bpour\s+[a-z...]{2,}(er|ir|re|oir)\b"
      loose (clitic-tolerant, tagged separately):
      r"\bpour\s+(?:[a-z...]{1,4}\s+){1,2}[a-z...]{2,}(er|ir|re|oir)\b"
  Candidates are printed for MANUAL classification (regex cannot judge
  exclamatory illocutionary force, nor whether the pronoun is the topic).

Corpus: the drama ingest at code/side-period/corpus/ — 14 unique plays,
hugo-hernani.txt (Hetzel 1889 duplicate edition) EXCLUDED, one edition
per play per the queue gate (same pinned FILES as the parent battery).

Output: JSON with candidates + wider context for manual classification.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DRAMADIR = os.path.join(LANE, "code/side-period/corpus")
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
    r"\bpour\s+"
    r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
GOV_INF_LOOSE = re.compile(
    r"\bpour\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü']{1,4}\s+){1,2}"
    r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)


def windows(text, fname):
    out = []
    for m in PRON.finditer(text):
        seg = text[m.start():m.start() + 400]
        end = re.search(r"[!?]", seg)
        if not end:
            continue
        win = seg[: end.end()]
        if "!" not in win and "?" not in win:
            continue
        strict = sorted({w.group(0).lower() for w in GOV_INF_STRICT.finditer(win)})
        loose = sorted({w.group(0).lower() for w in GOV_INF_LOOSE.finditer(win)
                        if w.group(0).lower() not in strict})
        if not strict and not loose:
            continue
        ctx_start = max(0, m.start() - 400)
        ctx = text[ctx_start:m.start() + 600].replace("\n", " / ")
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
              f"{len(c)} pour-governed-excl recall candidates")
        files.append({"file": f, "chars": len(text),
                      "pron_comma_hits": n_pron,
                      "gov_excl_candidates": len(c)})
    n_strict = sum(1 for c in cands if c["strict_gov_inf"])
    n_loose = sum(1 for c in cands if c["loose_gov_inf"] and not c["strict_gov_inf"])
    print(f"TOTAL: {len(files)} unique plays, {total} chars, "
          f"{sum(f['pron_comma_hits'] for f in files)} pron-comma hits, "
          f"{len(cands)} pour-governed-exclamatory recall candidates "
          f"({n_strict} strict, {n_loose} loose-only)")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "personal-tonic-pour-only-drama-recall_census.json")
    json.dump({"files": files, "total_chars": total, "candidates": cands,
               "note": "hugo-hernani.txt (Hetzel 1889) excluded: duplicate "
                       "Hernani edition; ONE edition per play per queue gate; "
                       "governor restricted to 'pour' only; window through "
                       "next [!?] inclusive, cap 400 chars"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
