#!/usr/bin/env python3
r"""Census for battery reinforced-pour-inf-recall.

Follow-up #1 (P3) of the NULL battery-reinforced-pour-inf-diagnostic
(2026-10-09). The diagnostic null fenced reinforced-head + GOVERNED
exclamatory infinitive (0/4 genuine) but flagged two recall gaps:
  (a) P1 admitted only [,;:] after the head — dash/parenthesis pause
      marks ("celui-la -- pour rire !") were never searched;
  (b) the 180-char window cap dropped 73/231 windows with no sentence
      end in-window (P2 drop).

THIS battery is a different search, not a re-run: it targets ONLY
unsearched windows:
  - all reinforced-head + DASH/PAREN pause-mark occurrences
    (never matched the diagnostic P1), and
  - the 73 dem-comma occurrences the diagnostic dropped (no sentence
    end within 180 chars), now searched with the cap lifted.

Search patterns (exact, verbatim):
  HEAD inventory (same DEM_REINF as the diagnostic):
      r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|ça[-\u2011\u2013 ]?(?:l[àa]|ci))" — case-insensitive.
  RECALL P1 (pause mark): \s*(?:[,;:]|[—–-]|\( )
  OLD P1 (diagnostic): \s*[,;:]  — used only to identify the already-
      searched set for exclusion.
  Already-searched = OLD-P1 occurrence whose 180-char window contains
      any sentence-end [!?.] (diagnostic's searched set; includes its
      4 classified candidates). Excluded from the recall search.
  NEW P2 (exclamatory filter): window must contain "!" before its end.
  Window = text from the demonstrative through the next [!?.]
      (inclusive), NO 180-char cap (sanity ceiling 4000 chars; any
      candidate hitting the ceiling is flagged in the JSON).
  NEW P3 (governed-infinitive candidate): same regex as diagnostic:
      r"\b(pour|à|a|de|d['’])\s+(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      applied to the window text AFTER the pause mark (case-insensitive).
      Candidates are printed for MANUAL classification.

Corpus (identical to the diagnostic census; character counts re-verified
against reinforced-pour-inf-diagnostic_census.json):
  - code/side-period/corpus/: the same 18 files listed in the
    diagnostic census JSON (French files only; German excluded).
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
OLD_P1 = re.compile(r"\s*[,;:]", re.IGNORECASE)
RECALL_P1 = re.compile(r"\s*(?:[,;:]|[—–-]|\()", re.IGNORECASE)

GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['’])\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)

MAXWIN = 4000  # sanity ceiling; flagged if hit

def classify_occurrences(text):
    """Return (searched_old_positions, recall_positions) where positions
    are (start_offset, pause_mark, is_old_style)."""
    searched, recall = [], []
    for m in DEM_REINF.finditer(text):
        pm = RECALL_P1.match(text, m.end())
        if not pm:
            continue
        mark = pm.group(0).strip()[-1] if pm.group(0).strip() else ""
        is_old = OLD_P1.match(text, m.end()) is not None
        if is_old:
            seg = text[m.start():m.start() + 180]
            if re.search(r"[!?.]", seg):
                searched.append((m.start(), mark))
            else:
                recall.append((m.start(), m.end(), mark, pm.end()))
        else:
            # dash or paren: never searched by the diagnostic
            recall.append((m.start(), m.end(), mark, pm.end()))
    return searched, recall

def recall_windows(text, file, recall):
    out = []
    for start, dem_end, mark, pm_end in recall:
        seg = text[start:start + MAXWIN]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        capped = end is None
        if "!" not in win:
            continue
        after = win[pm_end - start:]
        gov_hits = [(g.group(1).lower(), g.group(0).lower())
                    for g in GOV_INF.finditer(after)]
        if not gov_hits:
            continue
        out.append({"dem": text[start:dem_end].lower(),
                    "pause_mark": mark,
                    "window": win,
                    "capped": capped,
                    "gov_inf_hits": sorted({h[0] + " + " + h[1]
                                            for h in gov_hits}),
                    "file": file})
    return out

def census(paths, label):
    total_chars = 0
    files, cands = [], []
    n_old, n_dropped, n_newmarks = 0, 0, 0
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        searched, recall = classify_occurrences(t)
        n_old += len(searched) + len([r for r in recall if OLD_P1.match(t, r[1])])
        n_dropped += len([r for r in recall if OLD_P1.match(t, r[1])])
        n_newmarks += len([r for r in recall if not OLD_P1.match(t, r[1])])
        c = recall_windows(t, name, recall)
        files.append({"file": name, "chars": len(t),
                      "old_searched": len(searched),
                      "recall_occurrences": len(recall),
                      "recall_candidates": len(c)})
        cands.extend(c)
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"recall occurrences={sum(f['recall_occurrences'] for f in files)}, "
          f"recall candidates={len(cands)}")
    return {"files": files, "total_chars": total_chars,
            "old_searched_windows": n_old - n_dropped,
            "dropped_windows_reopened": n_dropped,
            "new_pause_mark_windows": n_newmarks,
            "candidates": cands}

if __name__ == "__main__":
    res = {
        "census_1841_register": census(
            [os.path.join(CORPUS1841, f) for f in FILES_1841], "1841 register"),
        "census_wider_19c": census(WIDER, "wider 19c"),
    }
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-pour-inf-recall_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
