#!/usr/bin/env python3
"""Dialogue-scoped pausemark census: dislocated demonstratives
(cela/ceci/ça) + NON-comma separators (!, --, ..., :, ;) in drama DIALOGUE.

Same patterns as disloc_demonstrative_drama_pausemark_recall_census.py,
run over dialogue-scoped text:
  1. drop front matter (preface/title/cast list) before the per-file
     play-body cut marker (first ACTE/PARTIE line);
  2. drop whole-line ALL-CAPS speaker/header lines (HERNANI., DON CARLOS.,
     ACTE PREMIER, PERSONNAGES, ...);
  3. drop whole-line parenthetical stage directions "(Il sort.)".

Candidates are mapped back to ORIGINAL file offsets so they can be
compared against the parent census's already-classified candidates
(disloc-demonstrative-drama-pausemark-recall_census.json, 0 genuine):
any candidate not overlapping a parent candidate is NEW and must be
hand-classified.

One Hernani edition only: hugo-hernani.txt (Hetzel 1889);
hugo-hernani-1870.txt EXCLUDED (one-edition rule).
"""
import json, os, re

CORPUS = os.path.expanduser(
    "~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
HERE = os.path.dirname(os.path.abspath(__file__))

# file -> 1-based line of the first play-body line (ACTE/PARTIE marker)
CUT = {
    "dumas-antony.txt": 131,
    "dumas-henri-iii.txt": 50,
    "dumas-kean.txt": 1,
    "dumas-mariage-louis-xv-1841.txt": 100,
    "dumas-tour-de-nesle.txt": 48,
    "hugo-burgraves.txt": 117,
    "hugo-hernani.txt": 104,
    "hugo-ruy-blas.txt": 130,
    "labiche-chapeau-de-paille.txt": 120,
    "labiche-martin-poudre-aux-yeux.txt": 48,
    "musset-comedies-proverbes-1850.txt": 148,
    "scribe-bertrand-et-raton.txt": 54,
    "scribe-verre-d-eau.txt": 23,
    "vigny-chatterton-1835.txt": 918,
}

# patterns verbatim from the parent pausemark-recall census
SEP = r"(?:[!?…:;]|—+|--+|\.{2,})"
DEM = re.compile(r"\b(cela|ceci|ça|ca)\s*" + SEP, re.IGNORECASE)
INF = re.compile(r"\b([A-Za-zÀ-ÿ-]+(?:er|ir|re))\b")
SENT_END = re.compile(r"[.?!]")


def is_header_line(line):
    s = line.strip()
    if not s:
        return True
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 2:
        return True
    upper = sum(1 for c in letters if c.isupper())
    return len(s) <= 80 and upper / len(letters) >= 0.70


def is_stage_line(line):
    s = line.strip()
    return s.startswith("(") and s.endswith(")")


def find_inf_after(txt, pos, limit=70):
    seg = txt[pos:pos + limit]
    m = SENT_END.search(seg)
    if m:
        seg = seg[:m.start()]
    m = INF.search(seg)
    return (m.group(1), pos + m.start()) if m else None


def main():
    parent = json.load(open(os.path.join(
        HERE, "disloc-demonstrative-drama-pausemark-recall_census.json")))
    parent_cands = parent["candidates"]
    out = {"files": {}, "candidates": [], "parent_candidates": len(parent_cands)}
    total_new = 0
    for fn, cut in CUT.items():
        path = os.path.join(CORPUS, fn)
        raw = open(path, encoding="utf-8", errors="replace").read()
        lines = raw.split("\n")
        # original char offset of each line
        off = 0
        line_off = []
        for ln in lines:
            line_off.append(off)
            off += len(ln) + 1
        kept = []
        dropped = {"front": 0, "header": 0, "stage": 0}
        orig_lines = []
        for i, ln in enumerate(lines, start=1):
            if i < cut:
                dropped["front"] += 1
                continue
            if is_header_line(ln):
                dropped["header"] += 1
                continue
            if is_stage_line(ln):
                dropped["stage"] += 1
                continue
            kept.append(ln)
            orig_lines.append(line_off[i - 1])
        stripped = "\n".join(kept)
        # map stripped offset -> original offset
        cum = [0]
        for ln in kept:
            cum.append(cum[-1] + len(ln) + 1)

        def to_orig(pos):
            import bisect
            k = bisect.bisect_right(cum, pos) - 1
            if k >= len(orig_lines):
                k = len(orig_lines) - 1
            return orig_lines[k] + (pos - cum[k])

        hits = list(DEM.finditer(stripped))
        ncand = 0
        for m in hits:
            win = stripped[m.start():m.start() + 70]
            if "!" not in win:
                continue
            ncand += 1
            inf = find_inf_after(stripped, m.end())
            ooff = to_orig(m.start())
            ctx = raw[max(0, ooff - 200):ooff + 300].replace("\n", " / ")
            # overlap with any parent candidate (same file, |offset diff|<=40)?
            matched = [c for c in parent_cands
                       if c["file"] == fn and abs(c["offset"] - ooff) <= 40]
            is_new = not matched
            total_new += is_new
            out["candidates"].append({
                "file": fn,
                "stripped_offset": m.start(),
                "offset": ooff,
                "head": m.group(0).strip(),
                "infinitive": inf[0] if inf else None,
                "infinitive_offset": inf[1] if inf else None,
                "context": ctx,
                "in_parent_census": not is_new,
                "parent_matches": [c["offset"] for c in matched],
            })
        out["files"][fn] = {"chars": len(raw),
                            "stripped_chars": len(stripped),
                            "dropped_lines": dropped,
                            "dem_sep_hits_stripped": len(hits),
                            "candidates_stripped": ncand}
        print(f"{fn}: stripped {len(stripped)} chars "
              f"(dropped {dropped}), {len(hits)} hits, {ncand} candidates")
    out["total_candidates"] = len(out["candidates"])
    out["total_new_vs_parent"] = total_new
    dest = os.path.join(HERE, "disloc-demonstrative-drama-pausemark-dialogue_census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(json.dumps({"total_candidates": len(out["candidates"]),
                      "total_new_vs_parent": total_new, "dest": dest},
                     indent=1))


if __name__ == "__main__":
    main()
