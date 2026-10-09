#!/usr/bin/env python3
"""Battery or-fragment-license: census of clause-initial 'Or' after verbless
fragments in DIPLOMATIC 1841 prose.

Bar: >=3 genuine diplomatic attestations licenses 'or' at @760's fragment
reading; confirmed zero across the diplomatic cut narrows the rival set.

Method: reuse the lane's clause splitter + finite-form detector
(finite_forms.FINITE2, ~4,250 forms). Every candidate hand-audited.
"""
import json, os, re, sys

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORP = os.path.join(LANE, "code/side-period/corpus")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from finite_forms import FINITE2, deacc

DIPLOMATIC = [
    "levant-correspondence-1841-p3.txt",
    "metternich-papiere-v4.txt",
    "metternich-papiere-v6.txt",
    "pozzo-di-borgo-correspondance-v1.txt",
    "talleyrand-memoires-v1.txt",
    "guizot-memoires-t1-gutenberg.txt",
    "guizot-memoires-t2-gutenberg.txt",
    "guizot-memoires-t3-gutenberg.txt",
    "guizot-memoires-t5-t6.txt",
]

def strip_acc(s):
    return deacc(s)

def clauses(text):
    # split on sentence/clause terminators and paragraph breaks only;
    # single newlines are line-wraps inside OCR'd texts, NOT boundaries
    parts = re.split(r"[.;:!?…]+|\n\s*\n", text)
    return [p.strip(" \t\"'«»'()") for p in parts if p.strip(" \t\"'«»'()")]

def first_word(cl):
    m = re.match(r"[\"'«»(\s]*([A-Za-zÀ-ÿ]+)", cl)
    return m.group(1) if m else ""

def words(cl):
    return re.findall(r"[A-Za-zÀ-ÿ]+(?:'[A-Za-zÀ-ÿ]+)?", cl)

def is_verbless(cl):
    ws = [strip_acc(w).lower() for w in words(cl)]
    return not any(w in FINITE2 for w in ws)

def main():
    cands = []
    n_or = 0
    chars = 0
    for fn in DIPLOMATIC:
        p = os.path.join(CORP, fn)
        text = open(p, encoding="utf-8", errors="replace").read()
        chars += len(text)
        cls = [c for c in clauses(text) if c]
        for i, cl in enumerate(cls):
            fw = strip_acc(first_word(cl)).lower()
            if fw == "or":
                n_or += 1
                prev = cls[i-1] if i > 0 else ""
                cands.append({
                    "file": fn, "idx": i,
                    "prev": prev[:260],
                    "prev_verbless": is_verbless(prev),
                    "cur": cl[:200],
                })
    print(f"diplomatic chars: {chars}")
    print(f"clause-initial 'Or': {n_or} total, "
          f"{sum(1 for c in cands if c['prev_verbless'])} with verbless prev clause")
    json.dump(cands, open("orfragment_candidates.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    for c in cands:
        if c["prev_verbless"]:
            print("=" * 78)
            print(c["file"], "clause", c["idx"])
            print("PREV:", c["prev"])
            print("CUR :", c["cur"])

if __name__ == "__main__":
    main()
