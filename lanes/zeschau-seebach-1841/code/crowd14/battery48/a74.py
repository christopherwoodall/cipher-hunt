#!/usr/bin/env python3
"""A: 74-class battery (round 14 battery48). Implements PREREG.md Battery 1.

A3 (cipher): re-derive all 34 74-windows, class-signature tests with
pre-registered falsifiers on banked values only.
A4 (era): exhaustive clean-pool "de ce que" census with pre-registered
artifact exclusion; absolute-"de ce que" rate; per-token classification.
"""
import json, re, unicodedata
from collections import Counter
from common import PAIRS, N, VALS, gloss, CORP, FILES

INF = {29, 40, 6, 59}          # inflection inventory (29/40 GT, 6 restr., 59 prov)

# ---------------- A3: cipher ----------------
pos74 = [i for i, p in enumerate(PAIRS) if p == 74]
assert len(pos74) == 34
pre = Counter(PAIRS[i-1] for i in pos74 if i > 0)
suc = Counter(PAIRS[i+1] for i in pos74 if i < N-1)
windows = {}
for i in pos74:
    ctx = PAIRS[max(0,i-3):i+4]
    windows[str(i)] = {"ctx": ctx, "gloss": gloss(ctx)}

# byte-exact re-derivation of the @863 frame
frame = PAIRS[862:866]
frame_ok = (PAIRS[862]==74 and PAIRS[863]==48 and PAIRS[864]==47 and PAIRS[865]==46)
frame_wide = {"860_868": PAIRS[860:869], "gloss": gloss(PAIRS[860:869])}

a3 = {
  "n74": len(pos74),
  "frame_863_rederived": frame_ok,
  "frame_wide": frame_wide,
  # class-signature tests (pre-registered)
  "verb_pin": {"suc_inf": sum(suc.get(c,0) for c in INF),
               "suc_inf_detail": {str(c): suc.get(c,0) for c in sorted(INF)},
               "pre_94_62": pre.get(94,0) + pre.get(62,0),
               "pre_detail": {"94": pre.get(94,0), "62": pre.get(62,0)}},
  "adj_test": {"suc_89": suc.get(89,0), "pre_70": pre.get(70,0)},
  "noun_test": {"pre_11": pre.get(11,0), "pre_87": pre.get(87,0)},
  "part_test": {"pre_59": pre.get(59,0)},
  "func_profile": {"pre": dict(sorted(pre.items())), "suc": dict(sorted(suc.items()))},
  "bigram_74_74": {"n": suc.get(74,0) + pre.get(74,0),
                   "positions": sorted(set([i for i in pos74 if i+1<N and PAIRS[i+1]==74] +
                                           [i for i in pos74 if i>0 and PAIRS[i-1]==74]))},
}
# full contact dicts for the record
a3["pre_full"] = dict(sorted(pre.items()))
a3["suc_full"] = dict(sorted(suc.items()))

# ---------------- A4: era ----------------
WORD = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)?", re.UNICODE)
BOUND = set('.!?;:—«»"()…')
def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('\u2019',"'").replace('\u2018',"'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        for i, p in enumerate(w.split("'")):
            if not p: continue
            toks.append(p + "'" if i < len(w.split("'"))-1 else p)
    # sentence-boundary flags: walk raw text for punctuation before each token
    return toks

def raw_tokens_with_bounds(text):
    """tokens + whether preceded by a sentence boundary"""
    text = unicodedata.normalize('NFC', text.lower().replace('\u2019',"'").replace('\u2018',"'"))
    out = []
    for m in WORD.finditer(text):
        w = m.group(0)
        # look back over whitespace for boundary char
        j = m.start()-1
        while j >= 0 and text[j] in ' \t\n\r':
            j -= 1
        bound = (j < 0) or (text[j] in BOUND)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p: continue
            tok = p + "'" if i < len(parts)-1 else p
            out.append((tok, bound and i == 0))
            bound = False
    return out

hits = []  # (file, idx, L1, L1_prev2, absolute, left3)
for f in FILES:
    toks = raw_tokens_with_bounds((CORP/f).read_text(encoding='utf-8', errors='replace'))
    words = [t for t,_ in toks]
    for i in range(len(words)-3):
        if words[i]=='de' and words[i+1]=='ce' and words[i+2]=='que':
            L1 = words[i-1] if i-1 >= 0 else '<START>'
            absolute = toks[i][1]
            left3 = words[max(0,i-3):i]
            hits.append({"file": f, "i": i, "L1": L1, "absolute": absolute,
                         "left3": left3})

ART_MOD = {'et','aussi','surtout','enfin','exactement','seulement','pas','autres','même'}
ART_VOC = {'roi','majesté'}
def is_artifact_a(l1): return l1 in ART_MOD
def is_artifact_b(l1): return l1 in ART_MOD or l1 in ART_VOC

n_abs = sum(1 for h in hits if h['absolute'])
a4 = {"n_de_ce_que": len(hits), "n_absolute": n_abs,
      "absolute_rate": round(n_abs/len(hits),4) if hits else 0.0,
      "absolute_examples": [(h['file'], h['left3'], h['L1']) for h in hits if h['absolute']][:15],
      "L1_counts": dict(Counter(h['L1'] for h in hits).most_common()),
      "hits": hits}

out = {"A3": a3, "A4": a4}
(CORP and None)
Path = __import__('pathlib').Path
Path.home().joinpath('workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd14/battery48/a74_raw.json').write_text(
    json.dumps(out, ensure_ascii=False, indent=1))
print("n74 =", a3["n74"], "| frame863 ok:", frame_ok)
print("verb_pin: suc_inf =", a3["verb_pin"]["suc_inf"], a3["verb_pin"]["suc_inf_detail"],
      "| pre94+62 =", a3["verb_pin"]["pre_94_62"])
print("adj: suc89 =", a3["adj_test"]["suc_89"], "pre70 =", a3["adj_test"]["pre_70"],
      "| noun: pre11 =", a3["noun_test"]["pre_11"], "pre87 =", a3["noun_test"]["pre_87"],
      "| part: pre59 =", a3["part_test"]["pre_59"])
print("74-74 bigram positions:", a3["bigram_74_74"]["positions"])
print("era: n_de_ce_que =", len(hits), "| absolute =", n_abs,
      "| rate =", round(n_abs/len(hits),4) if hits else 0)
print("top L1s:", Counter(h['L1'] for h in hits).most_common(12))
