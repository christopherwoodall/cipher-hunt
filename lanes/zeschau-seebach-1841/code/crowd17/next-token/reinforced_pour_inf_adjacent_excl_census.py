#!/usr/bin/env python3
r"""Census for battery reinforced-pour-inf-adjacent-excl.

Follow-up #3 (P3) of the NULL battery-reinforced-pour-inf-zeropause
(2026-10-09). That battery found 16 declarative zero-pause
reinforced-head + preposition + infinitive windows
("celle-ci pour conquérir le droit, ..."), all non-exclamatory.
THIS battery re-examines each of those 16 windows with a ±500-char
frame for an adjacent exclamatory clause sharing the head
("celle-ci pour conquérir le droit !") — ruling out the recall gap
"the exclamation lives in the next sentence".

Method: re-derive the 16 exact-shape windows byte-exact (zero-pause
reinforced head, whitespace, preposition (pour|à|de|d'), whitespace,
infinitive-shaped word ending er|ir|re|oir — no pause mark between
head and preposition, since pause-mark shapes were searched by the
diagnostic+recall). For each window, dump the ±500-char frame and
flag "!" / "?" occurrences for MANUAL classification of whether any
exclamatory clause shares the head.
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
PAUSE_MARKS = set(",;:—–-()[]«»\"'’")
# preposition immediately after head: head \s+ prep \s+ infinitive-shaped word
PREP_INF = re.compile(
    r"(pour|à|a|de|d['’])\s+[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)

FRAME = 500

def run(paths, label):
    rows = []
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        for m in DEM_REINF.finditer(t):
            pos = m.end()
            # skip whitespace after head
            while pos < len(t) and t[pos].isspace():
                pos += 1
            if pos >= len(t) or t[pos] in PAUSE_MARKS:
                continue  # pause-mark shape: searched by diagnostic/recall
            gm = PREP_INF.match(t, pos)
            if not gm:
                continue
            head = t[m.start():m.end()]
            sent_start = max(0, m.start() - FRAME)
            sent_end = min(len(t), m.end() + FRAME)
            frame = t[sent_start:sent_end]
            rows.append({
                "file": name, "offset": m.start(),
                "head": head.lower(),
                "match": gm.group(0)[:60],
                "bang_in_frame": "!" in frame,
                "qmark_in_frame": "?" in frame,
                "frame": frame,
            })
    print(f"=== {label}: {len(rows)} exact-shape windows")
    return rows

if __name__ == "__main__":
    rows = (run([os.path.join(CORPUS1841, f) for f in FILES_1841],
                "1841 register")
            + run(WIDER, "wider 19c"))
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-pour-inf-adjacent-excl_census.json")
    json.dump(rows, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out, f"({len(rows)} rows)")
    for r in rows:
        print(f"- {r['file']} @{r['offset']} [{r['head']}] {r['match'][:50]!r} "
              f"bang={r['bang_in_frame']} qmark={r['qmark_in_frame']}")
