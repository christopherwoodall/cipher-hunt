#!/usr/bin/env python3
r"""Recall battery disloc-comedy-bare-heads-recall.

Closes the pattern-form artifact gap in
battery-disloc-comedy-bare-heads-extension (2026-10-09, NULL: 51 dem-comma
hits -> 10 candidates -> 0 genuine in 465,531 comedy chars).

Two recall repairs:
  R1 pause-mark variants: the parent P1 only accepted [,;:] after the bare
     head. Here the bare head (cela|ceci|ca|cel[aa]|cec[iy], plus bare "ce"
     as Pass B) may be followed by any of: comma/semicolon/colon (rerun of
     the parent, to dedupe), EM/EN dash or hyphen run, ellipsis, open
     parenthesis, or a clause-terminal ! or ? used as the dislocation pause.
  R2 uncapped pass: the parent window was capped at 180 chars and dropped
     any window whose first [!?.] lay beyond 180. Here the window runs from
     the demonstrative through the next [!?.] with no 180-char cap
     (hard cap 4000 chars to avoid pathological runs), then the P2
     (must contain an exclamatory "!" after the head pause) and P3
     (infinitive-shaped word) filters apply; candidates are classified
     by hand (regex cannot separate -er infinitives from nouns/adjectives).

A window counts genuine under the same rule as the parent: (a) demonstrative
in dislocated topic position set off by a pause mark, (b) a BARE infinitive
(no preposition, no "que", no governing verb between topic and verb), and
(c) exclamatory force where the "!" terminates the infinitive phrase itself.

Corpus: the same 6 comedy files in code/side-period/corpus/.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

COMEDY_FILES = [
    "labiche-29-degres-ombre.txt",
    "labiche-affaire-rue-lourcine.txt",
    "labiche-la-cagnotte.txt",
    "labiche-voyage-perrichon.txt",
    "scribe-le-lorgnon.txt",
    "scribe-le-savant.txt",
]

HEAD = r"(cela|ceci|ça|cel[àa]|cec[iy])"
CE = r"(ce)"

# pause-mark classes: comma-family (parent rerun), dash family, ellipsis,
# open-paren, clause-terminal ! or ?
PAUSE = {
    "comma": r"\s*[,;:]\s*",
    "dash": r"\s*(?:\u2014|\u2013|--|-)(\s|$)",
    "ellipsis": r"\s*\u2026\s*",
    "paren": r"\s*\(\s*",
    "exclq": r"\s*[!?]\s*",
}
INF = re.compile(r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
                 re.IGNORECASE)
MAX_WIN = 4000


def variants(text, head_re):
    """Yield one record per (head match, pause-mark class)."""
    for pm_name, pm_re in PAUSE.items():
        rx = re.compile(r"\b" + head_re + pm_re, re.IGNORECASE)
        for m in rx.finditer(text):
            pause_end = m.end()
            seg = text[m.start():min(len(text), m.start() + MAX_WIN)]
            # P2: window through next [!?.]; for exclq pause the first
            # sentence-terminator is the pause itself, so search the
            # remainder AFTER the pause.
            after_pause = seg[pause_end - m.start():]
            end = re.search(r"[!?.]", after_pause)
            if not end:
                continue
            win = after_pause[:end.end()]
            if "!" not in win:
                continue
            yield {"head": m.group(1).lower(), "pause": pm_name,
                   "start": m.start(), "window": win,
                   "inf_hits": sorted({w.group(0).lower()
                                       for w in INF.finditer(win)})}


def census():
    total = 0
    cands = []
    stats = []
    for name in COMEDY_FILES:
        p = os.path.join(CORPUS, name)
        assert os.path.exists(p), f"missing corpus file: {p}"
        t = open(p, encoding="utf-8", errors="replace").read()
        total += len(t)
        file_cands = 0
        for head_re, passtag in ((HEAD, "A"), (CE, "B")):
            for rec in variants(t, head_re):
                rec["file"] = name
                rec["pass"] = passtag
                cands.append(rec)
                file_cands += 1
        stats.append({"file": name, "chars": len(t),
                      "variant_candidates": file_cands})
    print(f"=== recall: {total} chars, {len(cands)} variant candidates")
    return {"total_chars": total, "files": stats, "candidates": cands}


if __name__ == "__main__":
    res = census()
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-comedy-bare-heads-recall_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
