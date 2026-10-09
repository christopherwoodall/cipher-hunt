#!/usr/bin/env python3
r"""Extraction + audit script for battery reinforced-head-governed-topology-drama.

Follow-up of reinforced-head-topology-drama (parent, NULL). Differences:
1. Drops the '!' filter entirely: each of the 41 dem-comma windows is audited
   with FULL-TURN context (no 180-char cap, no sentence-end cap) for ANY
   exclamatory resolution tied to the reinforced head.
2. Recall-gap extension (grandparent's fenced gap): dash/parenthesis-delimited
   reinforced heads ("celui-là — ...", "celui-là (...)") are extracted in the
   same 14-play drama corpus and audited for exclamatory-infinitive pairing.

Exclamatory-infinitive detector (applied to full-turn context):
  - any "!" in the turn AND an infinitive (er/ir/re/oir ending) in the same
    clause before the "!", OR
  - pour/à/de + (short modifiers) + infinitive, followed by "!" later in the
    turn without an intervening sentence-ending [.?] or finite clause break.
Outputs flagged windows for hand classification; verdict is by hand audit.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

DRAMA = [
    "dumas-mariage-louis-xv-1841.txt",
    "vigny-chatterton-1835.txt",
    "musset-comedies-proverbes-1850.txt",
    "hugo-hernani.txt",
    "hugo-ruy-blas.txt",
    "hugo-burgraves.txt",
    "dumas-antony.txt",
    "dumas-tour-de-nesle.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
]

DEM = r"(?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|\u00e7a[-\u2011\u2013 ]?(?:l[àa]|ci)"
DEM_REINF_COMMA = re.compile(r"\b(" + DEM + r")\s*[,;:]", re.IGNORECASE)
DEM_REINF_DASH = re.compile(r"\b(" + DEM + r")\s*[\u2014\u2013-]\s*", re.IGNORECASE)
DEM_REINF_PAREN = re.compile(r"\b(" + DEM + r")\s*\(", re.IGNORECASE)

INF = r"[a-zàâäçéèêëîïôöùûü']{2,}(?:er|ir|re|oir)\b"
GOV_INF = re.compile(r"\b(?:pour|[àa]|de|d['\u2019])\s+(?:[a-zàâäçéèêëîïôöùûü'-]{1,8}\s+){0,3}" + INF, re.IGNORECASE)
BARE_INF_EXCL = re.compile(INF + r"\s*!")

def full_turn(text, start, cap=2000):
    seg = text[start:start + cap]
    # cut at next blank line (speaker-turn boundary in most play files)
    m = re.search(r"\n\s*\n", seg)
    if m:
        seg = seg[:m.start()]
    return seg

def audit(turn):
    """Return machine flags; hand audit decides."""
    flags = {}
    excl_marks = [m.start() for m in re.finditer(r"!", turn)]
    flags["n_excl"] = len(excl_marks)
    gov = [(m.start(), m.group(0)) for m in GOV_INF.finditer(turn)]
    flags["gov_inf"] = gov
    bare = [(m.start(), m.group(0)) for m in BARE_INF_EXCL.finditer(turn)]
    flags["bare_inf_excl"] = bare
    # governed infinitive anywhere before a "!" with no intervening [.?;]
    gov_before_excl = []
    for gstart, gtxt in gov:
        rest = turn[gstart:]
        em = re.search(r"[!?.]", rest)
        if em and rest[em.start()] == "!":
            gov_before_excl.append((gstart, gtxt, rest[:em.start() + 1]))
    flags["gov_inf_before_excl"] = gov_before_excl
    return flags

def main():
    wins = json.load(open(os.path.join(
        LANE, "code/crowd17/next-token",
        "reinforced-head-topology-drama_windows.json")))
    assert len(wins) == 41, f"expected 41, got {len(wins)}"
    out = []
    for i, w in enumerate(wins):
        t = open(os.path.join(CORPUS, w["file"]), encoding="utf-8",
                 errors="replace").read()
        turn = full_turn(t, w["off"])
        out.append({"idx": i, "file": w["file"], "off": w["off"],
                    "dem": w["dem"], "kind": "comma",
                    "turn": turn, "flags": audit(turn)})
    # recall-gap extension: dash / parenthesis delimited heads
    extra = []
    for name in DRAMA:
        t = open(os.path.join(CORPUS, name), encoding="utf-8",
                 errors="replace").read()
        for pat, kind in ((DEM_REINF_DASH, "dash"), (DEM_REINF_PAREN, "paren")):
            for m in pat.finditer(t):
                turn = full_turn(t, m.start())
                extra.append({"file": name, "off": m.start(),
                              "dem": m.group(1).lower(), "kind": kind,
                              "turn": turn, "flags": audit(turn)})
    json.dump({"windows41": out, "dash_paren": extra},
              open(os.path.join(LANE, "code/crowd17/next-token",
                   "reinforced-head-governed-topology-drama_windows.json"),
                   "w"), ensure_ascii=False, indent=1)
    print(f"41 comma windows + {len(extra)} dash/paren heads audited")
    # quick machine-flag summary
    n_gov_excl = sum(1 for w in out if w["flags"]["gov_inf_before_excl"])
    n_bare_excl = sum(1 for w in out if w["flags"]["bare_inf_excl"])
    print(f"comma windows with gov-inf-before-! flag: {n_gov_excl}")
    print(f"comma windows with bare-inf-! flag: {n_bare_excl}")
    x_gov_excl = sum(1 for w in extra if w["flags"]["gov_inf_before_excl"])
    x_bare_excl = sum(1 for w in extra if w["flags"]["bare_inf_excl"])
    print(f"dash/paren heads with gov-inf-before-! flag: {x_gov_excl}")
    print(f"dash/paren heads with bare-inf-! flag: {x_bare_excl}")

if __name__ == "__main__":
    main()
