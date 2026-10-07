#!/usr/bin/env python3
"""FRENCHMAN round 4 — work order 1: third independent leg for 62="on".

Two legs exist: (F31) ear lock; 62->94="on ne" x8 @1.97x in-band.
Task: examine every 62-window; find a THIRD leg independent of both.
Candidate angles:
  A. GT-anchored adjacency legs in new windows (46=que->62 "qu'on"; 62->70=pre "on pre...")
  B. Positional profile: predecessors of 62 vs era word-space "on" predecessors
  C. Ear completion of gappy 62-windows (1841 diplomatic idiom) in NEW windows
  D. Sanity: does "on" survive the by-ear-spelling enlightenment (phonetic "ont")?
Constraints: write to code/crowd4/ only. No invented ciphertext. F30-legal
(word-space era legs only; no era-syllable-conditionals on fragments).
"""
import json, os, re, sys, collections

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
sys.path.insert(0, os.path.join(LANE, "code"))
from crib_attack import load_pairs  # noqa: E402

GT = {"11": "la", "70": "pre", "82": "m", "34": "i", "29": "er", "40": "e", "46": "que"}
PROV = {"87": "[ce]", "64": "[qui]", "96": "[par]", "94": "[ne]"}

def dec(g):
    return GT.get(g, PROV.get(g, g))

pairs, odd, off1 = load_pairs()
assert len(pairs) == 1846, len(pairs)
print(f"pairs={len(pairs)} odd_lines={odd} off1={off1}", file=sys.stderr)

# ---- every 62-window ----
hits = [i for i, g in enumerate(pairs) if g == "62"]
print(f"f(62)={len(hits)}", file=sys.stderr)
EAR_USED = {1328, 100, 839, 1361, 1685, 1703, 508}  # ear-lock windows (round 3 F31)
ONNE = [i for i in hits if i + 1 < len(pairs) and pairs[i + 1] == "94"]
print(f"62->94 x{len(ONNE)} at {ONNE}", file=sys.stderr)
assert len(ONNE) == 8

windows = []
for i in hits:
    lo, hi = max(0, i - 4), min(len(pairs), i + 5)
    seg = pairs[lo:hi]
    mark = [(">>" + g + "<<") if j == i else dec(g) for j, g in enumerate(seg, start=lo)]
    windows.append({
        "pos": i, "prev": pairs[i - 1] if i > 0 else None,
        "next": pairs[i + 1] if i + 1 < len(pairs) else None,
        "in_ear_lock": i in EAR_USED, "in_onne": i in ONNE,
        "render": " ".join(mark),
    })

pre = collections.Counter(w["prev"] for w in windows)
fol = collections.Counter(w["next"] for w in windows)

# ---- era word-space model (Tocqueville t1+t2, F30-legal word space) ----
def words(path):
    t = open(path, encoding="utf-8", errors="replace").read().lower()
    t = re.sub(r"[’']", "'", t)
    # split elisions: qu'on -> qu' + on ; l'homme -> l' + homme
    t = re.sub(r"\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)", r"\1' \2", t)
    toks = re.findall(r"[a-zàâäéèêëîïôöùûüç]+(?:'[a-zàâäéèêëîïôöùûüç]+)?", t)
    return toks

toks = words(os.path.join(LANE, "data/gutenberg-30513-tocqueville-t1.txt")) + \
       words(os.path.join(LANE, "data/gutenberg-30514-tocqueville-t2.txt"))
N = len(toks)
n_on = sum(1 for w in toks if w == "on")
# elided qu' + on
n_quon = sum(1 for a, b in zip(toks, toks[1:]) if a in ("qu", "que") and b == "on")
n_ne_after_on = sum(1 for a, b in zip(toks, toks[1:]) if a == "on" and b in ("ne", "n'"))
pred_on = collections.Counter(a for a, b in zip(toks, toks[1:]) if b == "on")
fol_on = collections.Counter(b for a, b in zip(toks, toks[1:]) if a == "on")
n_que = sum(1 for w in toks if w in ("que", "qu"))
n_on_after_que = sum(1 for a, b in zip(toks, toks[1:]) if a in ("que", "qu") and b == "on")

out = {
    "f62": len(hits), "pairs": len(pairs),
    "onne_n": len(ONNE), "onne_at": ONNE,
    "predecessors": dict(pre), "followers": dict(fol),
    "que_to_62": [w["pos"] for w in windows if w["prev"] == "46"],
    "to_70_pre": [w["pos"] for w in windows if w["next"] == "70"],
    "to_46_que": [w["pos"] for w in windows if w["next"] == "46"],
    "to_11_la": [w["pos"] for w in windows if w["next"] == "11"],
    "to_64_qui": [w["pos"] for w in windows if w["next"] == "64"],
    "era": {
        "words": N, "n_on": n_on, "P_on_word": n_on / N,
        "P_cipher_62": len(hits) / len(pairs),
        "n_ne_after_on": n_ne_after_on, "P_ne_given_on": n_ne_after_on / n_on,
        "n_on_after_que": n_on_after_que, "P_on_given_que": n_on_after_que / n_que if n_que else 0,
        "top_pred_on": pred_on.most_common(15), "top_fol_on": fol_on.most_common(15),
    },
    "windows": windows,
}
p = os.path.join(LANE, "code/crowd4/frenchman4_62_results.json")
json.dump(out, open(p, "w"), indent=1, ensure_ascii=False)
print("wrote", p, file=sys.stderr)
for w in windows:
    tag = ("EAR" if w["in_ear_lock"] else "   ") + ("+ONNE" if w["in_onne"] else "     ")
    print(f"@{w['pos']:>4} [{tag}] {w['render']}")
