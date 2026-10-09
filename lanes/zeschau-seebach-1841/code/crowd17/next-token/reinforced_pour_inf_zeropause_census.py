#!/usr/bin/env python3
r"""Census for battery reinforced-pour-inf-zeropause.

Follow-up #1 (P3) of the NULL battery-reinforced-pour-inf-recall
(2026-10-09). Both the diagnostic and the recall batteries required a
pause mark ([,;:]/dash/paren) after the reinforced head. THIS battery
searches the never-searched shape: reinforced head directly followed
by the governed infinitive with NO pause mark at all, e.g.
"celui-la pour rire !".

Search patterns (exact, verbatim):
  HEAD inventory (same DEM_REINF as diagnostic + recall):
      r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|ça[-\u2011\u2013 ]?(?:l[àa]|ci))" — case-insensitive.
  ZERO-PAUSE P1: immediately after the head, optional whitespace, then
      a NON-pause-mark character: \s*(?![,;:—–\-\(\)\[\]«»"']).
      (A whitespace-only gap followed by a word char is the target
      shape "celui-la pour rire !".)
  P2 (exclamatory filter): window must contain "!" before its end.
  Window = text from the demonstrative through the next [!?.]
      (inclusive), NO 180-char cap (sanity ceiling 4000 chars; flagged
      if hit).
  P3 (governed-infinitive candidate): same as diagnostic/recall:
      r"\b(pour|à|a|de|d['’])\s+(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      applied to window text after the head (case-insensitive).
      Candidates printed for MANUAL classification.

Corpus (identical to diagnostic + recall census; 27,657,940 chars):
  - code/side-period/corpus/: 18 French files (German excluded).
  - data/gutenberg-17489-miserables1.txt, data/gutenberg-30513-tocqueville-t1.txt,
    data/gutenberg-30514-tocqueville-t2.txt.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
FILES_1841 = [
    "guizot-memoires-t1-gutenberg.txt",
    "guizot-memoires-t2-gutenberg.txt",
    "guizot-memoires-t3-gutenberg.txt",
    "guizot-memoires-t5-t6.txt",
    "harvest-log.txt",
    "levant-correspondence-1841-p3.txt",
    "metternich-papiere-v4.txt",
    "metternich-papiere-v6.txt",
    "nesselrode-v10.txt",
    "nesselrode-v7.txt",
    "nesselrode-v8.txt",
    "nesselrode-v9.txt",
    "pozzo-di-borgo-correspondance-v1.txt",
    "revue-deux-mondes-1841-q1.txt",
    "revue-deux-mondes-1841-q2.txt",
    "revue-deux-mondes-1841-q3.txt",
    "revue-deux-mondes-1841-q4.txt",
    "talleyrand-memoires-v1.txt",
]
WIDER = [
    os.path.join(LANE, "data/gutenberg-17489-miserables1.txt"),
    os.path.join(LANE, "data/gutenberg-30513-tocqueville-t1.txt"),
    os.path.join(LANE, "data/gutenberg-30514-tocqueville-t2.txt"),
]

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))", re.IGNORECASE)
# zero-pause: head + whitespace, first NON-space char must NOT be a pause
# mark ([,;:]/dash/paren — those were searched by the diagnostic+recall).
# Done manually (not as one regex) to avoid \s*-backtracking leaks.
ZERO_GAP = re.compile(r"\s*", re.IGNORECASE)
PAUSE_MARKS = set(",;:—–-()[]«»\"'’")

GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['’])\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)

MAXWIN = 4000

def census(paths, label):
    total_chars = 0
    files, cands = [], []
    n_zero = 0
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        n_file_zero, n_file_cand = 0, 0
        for m in DEM_REINF.finditer(t):
            gap = ZERO_GAP.match(t, m.end())
            pos = m.end() + (gap.end() - gap.start())
            if pos >= len(t) or t[pos] in PAUSE_MARKS:
                continue  # pause-mark shape: searched by diagnostic/recall
            # exclusion: if the same occurrence already matched a pause
            # mark shape it was searched before; zero-pause only when no
            # pause mark present
            next_after = t[pos:pos + 1]
            if not next_after:
                continue
            n_file_zero += 1
            seg = t[m.start():m.start() + MAXWIN]
            end = re.search(r"[!?.]", seg)
            win = seg[: end.end()] if end else seg
            capped = end is None
            if "!" not in win:
                continue
            after = t[m.end():m.start() + len(win)]
            gov_hits = [(g.group(1).lower(), g.group(0).lower(), g.start())
                        for g in GOV_INF.finditer(after)]
            if not gov_hits:
                continue
            n_file_cand += 1
            # "tight" = a governed infinitive begins within 60 chars of
            # the head end (the "celui-la pour rire !" shape)
            tight = [g for g in gov_hits if g[2] <= 60]
            cands.append({"dem": t[m.start():m.end()].lower(),
                          "offset": m.start(),
                          "after_head": after[:80],
                          "window": win,
                          "capped": capped,
                          "gov_inf_hits": sorted({h[0] + " + " + h[1]
                                                  for h in gov_hits}),
                          "tight_gov_inf": sorted({h[0] + " + " + h[1]
                                                   for h in tight}),
                          "file": name})
        n_zero += n_file_zero
        files.append({"file": name, "chars": len(t),
                      "zero_pause_occurrences": n_file_zero,
                      "candidates": n_file_cand})
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"zero-pause occurrences={n_zero}, candidates={len(cands)}")
    return {"files": files, "total_chars": total_chars,
            "zero_pause_occurrences": n_zero, "candidates": cands}

if __name__ == "__main__":
    res = {
        "census_1841_register": census(
            [os.path.join(CORPUS1841, f) for f in FILES_1841], "1841 register"),
        "census_wider_19c": census(WIDER, "wider 19c"),
    }
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-pour-inf-zeropause_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
