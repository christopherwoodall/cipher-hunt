#!/usr/bin/env python3
"""SOLVED-CONTEXT INVENTORY for the Seebach lane next-token program.

Re-derives the pair stream from data/upstream-ct_R5005.txt +
code/side-keyhunt/repaired_offsets.json (NEVER stale canonical.py),
then enumerates EVERY solved context: every occurrence of every banked
multi-group n-gram plus every single-group banked occurrence usable as a
prediction context.

Output: code/crowd15/next-token/contexts.json

Banked values (12):
  pencil GT: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que
  promoted:  87=ce, 64=qui, 96=par
  provisional (conditioned frames): 59=est, 77="le"
Classes (not values): 31=VERBAL, 33=INF
"""
import json, os, re

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(THIS_DIR)))  # .../code/crowd15/next-token -> lane
DATA = os.path.join(LANE, "data")
OUTDIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(OUTDIR, "contexts.json")

BANKED = {
    "11": ("la", "gt"), "70": ("pre", "gt"), "82": ("m", "gt"),
    "34": ("i", "gt"), "29": ("er", "gt"), "40": ("e", "gt"),
    "46": ("que", "gt"),
    "87": ("ce", "promoted"), "64": ("qui", "promoted"), "96": ("par", "promoted"),
    "59": ("est", "provisional"), "77": ("le", "provisional"),
}
PROVISIONAL = {"59", "77"}
CLASSES = {"31": "VERBAL", "33": "INF"}

# Lane-established neighbor facts (from NOTES.md; NOT banked values unless marked).
# Used for frame-constraint annotation only. (94="ne" is CONFIRMED legs 1-2 /
# provisional-strong; everything else is LEAD-grade or killed as noted.)
def neighbor_note(g, pre, suc):
    notes = []
    if g in CLASSES:
        notes.append("class=%s" % CLASSES[g])
    if g == "94":
        notes.append('94="ne" provisional-strong (CONFIRMED legs 1-2); rival 94="re" disfavored; 94="en" conditioned-islet iff pre==82 or suc==87')
    if g == "93":
        notes.append('{93,8}="l\'" LEAD as unconditioned homophones; 93="l\'" ALONE rate-KILLED')
    if g == "84":
        if pre in ("46", "94", "82"):
            notes.append('84="en" conditioned-islet arm (pre=%s in {46,94,82}, LEAD)' % pre)
        elif pre in ("77", "11"):
            notes.append('84=masc-noun conditioned-islet arm (pre=%s in {77,11}, LEAD)' % pre)
        else:
            notes.append('84 unclassified (neither "en" nor noun arm)')
    if g == "00":
        if pre == "96":
            notes.append('00="le" conditioned-islet LEAD (pre=96, n=3); rival 00="pour" STRONG LEAD unconditioned')
        else:
            notes.append('00: rival 00="pour" STRONG LEAD unconditioned; 00="le" only as pre=96 islet')
    if g == "06":
        if pre == "82":
            notes.append('06="ent" conditioned LEAD iff pre=82 (n=4, n_eff=3)')
        else:
            notes.append('06 general="ent" REFUTED (N22); unclassified here')
    if g == "24":
        notes.append('24="de" scoped KILL inside "en ce qui" (cond. 87=ce/64=qui)')
    if g == "59":
        if pre in ("64", "94", "93"):
            notes.append('59 est-arm (pre=%s in {64,94,93}): word-"est" ISLET 10' % pre)
        elif pre == "84":
            notes.append('59 -este-arm (pre=84): verb-final "-este" ISLET 10')
        else:
            notes.append('59 unclassified: unconditioned 59="est" REFUTED kill-grade')
    if g == "37":
        notes.append('37="le" MEDIUM (rival to 77)')
    if g == "47":
        notes.append('47="ce" LEAD (strengthened F55)')
    if g == "62":
        notes.append('62="on" fenced STRONG LEAD')
    return "; ".join(notes)

def plain(g):
    if g in BANKED:
        v, st = BANKED[g]
        return v + (" (prov)" if st == "provisional" else "")
    return "?%s" % g

def parse_stream():
    rows = []
    for line in open(os.path.join(DATA, "upstream-ct_R5005.txt")):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r"\D", "", digits)))
    off = json.load(open(os.path.join(LANE, "code", "side-keyhunt", "repaired_offsets.json")))
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [(digits[i:i + 2], lid) for i in range(o, len(digits) - 1, 2)]
    return pairs

def hits(seq, ng):
    n = len(ng)
    return [i for i in range(len(seq) - n + 1) if seq[i:i + n] == ng]

def occurrence(seq, lids, pos, ngram):
    L = [seq[pos - k] for k in (3, 2, 1)] if pos >= 3 else [seq[j] for j in range(max(0, pos - 3), pos)]
    L = [None] * (3 - len(L)) + L
    R = [seq[pos + len(ngram) + k] if pos + len(ngram) + k < len(seq) else None for k in range(3)]
    rec = {"pos": pos, "row": lids[pos],
           "left": L, "right": R,
           "left_plain": [plain(g) if g else None for g in L],
           "right_plain": [plain(g) if g else None for g in R],
           "neighbor_notes": {},
           "frame_constraints": []}
    # annotate neighbors
    for tag, gs, side in (("left", L, "L"), ("right", R, "R")):
        for k, g in enumerate(gs):
            if g is None:
                continue
            # local pre/suc of this neighbor inside the stream
            idx = pos - (3 - k) if tag == "left" else pos + len(ngram) + k
            pre = seq[idx - 1] if idx > 0 else None
            suc = seq[idx + 1] if idx + 1 < len(seq) else None
            note = neighbor_note(g, pre, suc)
            if note:
                rec["neighbor_notes"]["%s%d(%s)" % (side, k + 1, g)] = note
    # frame constraints: class flags + islet arms + scoped kills
    fc = rec["frame_constraints"]
    for tag, gs in (("left", L), ("right", R)):
        for g in gs:
            if g in CLASSES:
                fc.append("%s neighbor %s is class %s (not a value)" % (tag, g, CLASSES[g]))
    # context-internal group notes (incl. banked groups: arms/polyvalence matter)
    for k, g in enumerate(ngram):
        idx = pos + k
        pre = seq[idx - 1] if idx > 0 else None
        suc = seq[idx + 1] if idx + 1 < len(seq) else None
        note = neighbor_note(g, pre, suc)
        if note:
            rec["neighbor_notes"]["self[%d](%s)" % (k, g)] = note
    # en-ce-qui scoped kill for 24
    if ngram == ["24", "87"] and pos + 2 < len(seq) and seq[pos + 2] == "64":
        fc.append('24="de" rival scoped-KILLED here (window 24-87-64, cond. 87=ce/64=qui)')
    if ngram == ["82", "06"]:
        fc.append('06="ent" iff pre=82 conditioned LEAD (n=4, n_eff=3)')
    if ngram == ["96", "00"]:
        fc.append('00="le" conditioned-islet LEAD (pre=96); ungrammatical as 00="pour" at all 3 windows per F54')
    if ngram == ["93", "59"]:
        fc.append('93 alone rate-KILLED; {93,8}="l\'" LEAD only as unconditioned homophones')
    if ngram == ["94", "59"]:
        fc.append('94="ne" provisional-strong; 59 est-arm (pre=94)')
    if ngram == ["82", "84"]:
        fc.append('84="en" conditioned-islet arm (pre=82 in {46,94,82})')
    if ngram == ["24", "87"]:
        fc.append('24 unbanked; 24="de" rival scoped-killed inside 24-87-64 windows')
    if ngram == ["96", "87", "46"]:
        fc.append('all three groups banked; 96="par" provisional-grade promoted')
    if ngram == ["11", "70", "82", "34", "29", "40"]:
        fc.append('pencil GT anchor; byte-exact in repair_parse.py')
    return rec

CONTEXTS = [
    ("la-premiere", ["11", "70", "82", "34", "29", "40"], "la première",
     "banked", "pencil GT; expect 2", 2),
    ("par-ce-que", ["96", "87", "46"], "par ce que",
     "banked", "87/96 promoted, 46 GT; expect 3", 3),
    ("par-le", ["96", "00"], "par le",
     "mixed", "96=par banked; 00 unbanked (00=\"le\" conditioned islet LEAD iff pre=96, n=3)", None),
    ("m-en", ["82", "84"], "m'en",
     "mixed", "82=m banked; 84 unbanked (84=\"en\" conditioned islet LEAD iff pre in {46,94,82} — qualifies here)", None),
    ("ment", ["82", "06"], "ment",
     "mixed", "82=m banked; 06 unbanked (06=\"ent\" conditioned LEAD iff pre=82 — qualifies here)", None),
    ("en-ce", ["24", "87"], "en ce",
     "mixed", "87=ce banked; 24 unbanked (24=\"de\" scoped-killed inside 24-87-64)", None),
    ("l-est", ["93", "59"], "l'est",
     "mixed", "59=est provisional; 93 unbanked ({93,8}=\"l'\" LEAD as unconditioned homophones; 93 alone rate-KILLED)", None),
    ("n-est", ["94", "59"], "n'est",
     "mixed", "59=est provisional; 94 unbanked (94=\"ne\" provisional-strong / CONFIRMED legs 1-2)", None),
    ("qui", ["64"], "qui", "banked", "64=qui promoted", None),
    ("que", ["46"], "que", "banked", "46=que pencil GT", None),
    ("ce", ["87"], "ce", "banked", "87=ce promoted", None),
    ("par", ["96"], "par", "banked", "96=par promoted", None),
    ("est", ["59"], "est", "provisional", "59=est provisional; conditioned arms: est-arm iff pre in {64,94,93}, -este-arm iff pre=84", None),
    ("le-77", ["77"], "le", "provisional", "77=\"le\" provisional-conditioned", None),
]

def main():
    pairs = parse_stream()
    seq = [g for g, _ in pairs]
    lids = [l for _, l in pairs]
    assert len(seq) == 1847, len(seq)
    assert len(set(seq)) == 96, len(set(seq))
    out = []
    for cid, ng, pt, status, note, expect in CONTEXTS:
        pos_list = hits(seq, ng)
        if expect is not None and len(pos_list) != expect:
            print("MISMATCH: %s expected %d, got %d" % (cid, expect, len(pos_list)))
        out.append({
            "id": cid,
            "groups": ng,
            "plaintext": pt,
            "status": status,
            "note": note,
            "positions": pos_list,
            "count": len(pos_list),
            "expected": expect,
            "occurrences": [occurrence(seq, lids, p, ng) for p in pos_list],
        })
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print("wrote", OUT, "with", len(out), "contexts")

if __name__ == "__main__":
    main()
