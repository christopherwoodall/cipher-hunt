#!/usr/bin/env python3
r"""Census for battery disloc-reinforced-comedy-recall.

Recall check on battery-disloc-reinforced-comedy-extension (null 2026-10-09):
its P1 covered only [,;:] separators with 180-char sentence-capped windows.
This battery extends the separator class to comma + em-dash + en-dash +
hyphen + parenthesis + semicolon + colon, and runs an UNCAPCAPPED pass
(window = demonstrative + 400 chars, NOT truncated at the first [!?.]).

P1-recall: DEM_REINF followed by one of [,;:—–\-()] or DEM_REINF inside
    parens "(celui-là)".
P2 (exclamatory filter, unchanged): window must contain "!" anywhere.
P3 (infinitive candidate): same -er/-ir/-re/-oir token regex as the parent;
    candidates are printed for MANUAL classification.

Corpus: the 6 new comedy files in code/side-period/corpus/ (gate check).
Output: disloc-reinforced-comedy-recall_census.json + console table.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")
FILES = [
    "scribe-le-savant.txt",
    "scribe-le-lorgnon.txt",
    "labiche-voyage-perrichon.txt",
    "labiche-la-cagnotte.txt",
    "labiche-29-degres-ombre.txt",
    "labiche-affaire-rue-lourcine.txt",
]
DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))", re.IGNORECASE)
# recall separator class: anything the parent did NOT search
SEP_RECALL = re.compile(r"\s*([,;:—–\-()])")
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

def windows(text):
    out = []
    for m in DEM_REINF.finditer(text):
        rest = text[m.end():m.end() + 6]
        sep = SEP_RECALL.match(rest)
        if not sep:
            continue
        sepchar = sep.group(1)
        # uncapped window: fixed 400 chars, NOT truncated at sentence end
        win = text[m.start():m.start() + 400]
        if "!" not in win:
            continue
        # did the window close at a sentence mark within 180 chars?
        closed = bool(re.search(r"[!?.]", text[m.start():m.start() + 180]))
        out.append({"dem": m.group(1).lower(), "sep": sepchar,
                    "offset": m.start(), "closed_180": closed,
                    "window": win,
                    "inf_hits": sorted({w.group(0).lower()
                                        for w in INF.finditer(win)})})
    return out

def main():
    on_disk = {f for f in os.listdir(CORPUS) if f.endswith(".txt")}
    missing = [f for f in FILES if f not in on_disk]
    if missing:
        raise SystemExit("GATE FAIL: missing comedy files: " + ", ".join(missing))
    files, cands, total = [], [], 0
    for f in FILES:
        text = open(os.path.join(CORPUS, f), encoding="utf-8",
                    errors="replace").read()
        total += len(text)
        # separator-class coverage check
        n_sep = {}
        for m in DEM_REINF.finditer(text):
            s = SEP_RECALL.match(text[m.end():m.end() + 6])
            if s:
                n_sep[s.group(1)] = n_sep.get(s.group(1), 0) + 1
        c = windows(text)
        for w in c:
            w["file"] = f
            cands.append(w)
        print(f"{f}: {len(text)} chars, sep coverage {n_sep}, "
              f"{len(c)} recall candidates")
        files.append({"file": f, "chars": len(text), "sep_coverage": n_sep,
                      "recall_candidates": len(c)})
    print(f"TOTAL: {len(files)} comedy texts, {total} chars, "
          f"{len(cands)} recall candidates")
    for w in cands:
        print("=" * 70)
        print(f"{w['file']} @{w['offset']} sep={w['sep']!r} "
              f"closed_180={w['closed_180']}")
        print(w["window"][:600].replace("\n", " / "))
        print("inf_hits:", w["inf_hits"])
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-reinforced-comedy-recall_census.json")
    json.dump({"files": files, "total_chars": total, "candidates": cands},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)

if __name__ == "__main__":
    main()
