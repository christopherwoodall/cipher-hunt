#!/usr/bin/env python3
r"""Census for battery disloc-reinforced-prep-inf-drama.

Target: test whether reinforced demonstrative heads license the GOVERNED
exclamatory infinitive in drama ("celui-là, pour rire !" shape). Follow-up
of the NULL disloc-demonstrative-drama-reinforced (2026-10-09): its drama
near-misses carried governed (non-exclamatory) infinitives — this battery
asks whether the GOVERNED exclamatory infinitive under a reinforced head
attests in the same register.

Bar (pre-registered): ">=1 genuine governed exclamatory infinitive under a
reinforced head in drama pins the fence exactly at BARE; confirmed zero
fences the whole governed family at drama level".

Search patterns (same P1/P2 taxonomy as the parent census; P3 narrowed to
governed infinitives):
  P1 (dislocation): r"DEM_REINF\s*[,;:]" where DEM_REINF =
      ((?:celui|ceux|celle|celles)[-–— ]?(?:l[àa]|ci)|
       ça[-–— ]?(?:l[àa]|ci)) — case-insensitive, hyphen or space.
      - window = text from the demonstrative through the next [!?.]
        (inclusive), capped at 180 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (governed-infinitive candidate): r"\b(?:pour|de|d'|d’|à)\s+
      [a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b" — preposition-led infinitive
      inside the window. Candidates printed for MANUAL classification
      (regex cannot judge exclamatory illocutionary force or whether the
      head is the topic).

Corpus: the drama ingest at code/side-period/corpus/ — 14 unique plays
(hugo-hernani.txt, Hetzel 1889, EXCLUDED: duplicate Hernani edition; keep
hugo-hernani-1870.txt). A register sanity count of "pour [inf] !"
(ungoverned-by-head governed-exclamatory infinitives) is included as a
positive control.

Output: JSON with candidates + manual-classification context. Human
classification happens in the battery report. Files named, sizes in
characters, patterns exact.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DRAMADIR = os.path.join(LANE, "code/side-period/corpus")
EXCLUDE = {"hugo-hernani.txt"}
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
# Reinforced demonstrative heads — same inventory as the parent census.
DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)
# Preposition-led infinitive: pour / de / d' / à + infinitive-shaped word.
GOV_INF = re.compile(
    r"\b(?:pour|de|d'|d’|à)\s+"
    r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
# Positive control: governed exclamatory infinitive anywhere ("pour [inf] !").
CTRL = re.compile(
    r"\b(?:pour|de)\s+[a-zàâäçéèêëîïôöùûü']{2,}(?:er|ir|re|oir)\b[^!?.]{0,60}!",
    re.IGNORECASE)


def windows(text, fname, start_offset=0):
    out = []
    for m in DEM_REINF.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        g = sorted({w.group(0).lower() for w in GOV_INF.finditer(win)})
        if not g:
            continue
        ctx_start = max(0, m.start() - 250)
        ctx = text[ctx_start:m.start() + 320].replace("\n", "/")
        out.append({"file": fname, "offset": start_offset + m.start(),
                    "dem": m.group(1).lower(), "window": win,
                    "gov_inf_hits": g, "context": ctx})
    return out


def main():
    files, cands, ctrls = [], [], []
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
        n_dem = len(DEM_REINF.findall(text))
        c = windows(text, f)
        cands.extend(c)
        ctrl_hits = sorted({w.group(0).lower() for w in CTRL.finditer(text)})
        ctrls.append({"file": f, "pour_inf_excl_hits": len(ctrl_hits),
                      "sample": ctrl_hits[:5]})
        print(f"{f}: {len(text)} chars, {n_dem} dem-comma hits, "
              f"{len(c)} governed-excl candidates, "
              f"{len(ctrl_hits)} 'pour/de [inf] !' in register")
        files.append({"file": f, "chars": len(text),
                      "dem_comma_hits": n_dem,
                      "gov_excl_candidates": len(c)})
    print(f"TOTAL: {len(files)} unique plays, {total} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{len(cands)} governed-exclamatory candidates")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-reinforced-prep-inf-drama_census.json")
    json.dump({"files": files, "total_chars": total,
               "register_control": ctrls, "candidates": cands,
               "note": "hugo-hernani.txt (Hetzel 1889) excluded: duplicate "
                       "Hernani edition; ONE edition per play per queue gate"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
